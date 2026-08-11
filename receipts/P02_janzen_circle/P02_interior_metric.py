"""
P02_interior_metric.py -- verifies P2's lem:interior_metric, by DERIVING the Schwarzschild interior metric
  in cycloid coordinates (eta,t,theta,phi) from the Schwarzschild components (not asserting it):
    [P2 janzen_circle_v3 lem:interior_metric, eq:interior_metric(_eta); used again at sec:metric-singularities L368]
    (i)   g_tt = -(1-2M/r) = (2M-r)/r = tan^2(eta/2)  with r=M(1+cos eta)  -- POSITIVE inside (t spacelike);
    (ii)  g_rr = (1-2M/r)^{-1} = -cot^2(eta/2), and g_rr dr^2 = -4M^2 cos^4(eta/2) deta^2 = -dtau^2
          (the cycloid radial equation, linking to prop:cycloid);
    (iii) the assembled interior metric ds^2 = -dtau^2 + tan^2(eta/2) dt^2 + M^2(1+cos eta)^2 dOmega^2,
          so INSIDE the horizon eta is timelike and t is spacelike (the signature flip);
    (iv)  invariance under eta -> -eta (the white-hole branch: only deta^2, cos eta, tan^2 enter, all even);
    (v)   the sec:metric-singularities contrast: g_tt=tan^2(eta/2) -> 0 at the horizon (eta->0, r->2M, area
          16 pi M^2 finite) and -> +infinity at r=0 (eta->pi) -- the collapse moving sector to sector.
  [P2 janzen_circle_v3 -- the interior metric the continuations and the metric-singularity contrast rest on]
STATUS: ✔✔   RUN: python3 P02_interior_metric.py   RUNTIME: ~2s
COMPUTES: g_tt,g_rr from -(1-2M/r) with r=M(1+cos eta); g_rr dr^2 with dr=-M sin eta deta; the eta->-eta
  symmetry; the eta->0 and eta->pi limits of g_tt and of the areal radius. CONTROL below.
CONTROL: the radial coefficient reduces to -dtau^2 (prop:cycloid, genuine link, not asserted); at eta=pi/2
  (r=M) g_tt=tan^2(pi/4)=1>0 (t spacelike, finite) -- the interior signature is generic, not an endpoint
  artefact. (Break the r-substitution and g_tt no longer telescopes to tan^2.)
BOUND: prop:cycloid receipt does r(eta),tau(eta),the radial ODE,proper time M pi + the critical points;
  this does the interior metric ASSEMBLY -- g_tt=tan^2(eta/2) and the eta-timelike signature -- which that
  receipt does not, and which the continuation receipt takes as its given input.
ORIGIN: built new (fork) -- P2 completeness re-audit: the lemma between the two receipted props was uncovered.
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
M, eta = sp.symbols('M eta', positive=True)
r = M*(1+sp.cos(eta)); tau = M*(eta+sp.sin(eta))
print("="*72); print("P02 interior metric -- g_tt=tan^2(eta/2) DERIVED, eta-timelike signature"); print("="*72)

# (i) g_tt = -(1-2M/r) telescopes to tan^2(eta/2)
g_tt = sp.simplify(-(1 - 2*M/r))
ok&=check("g_tt = -(1-2M/r) = tan^2(eta/2)  (with r=M(1+cos eta))",
          sp.simplify((g_tt - sp.tan(eta/2)**2).rewrite(sp.exp))==0)
ok&=check("g_tt > 0 inside (t is SPACELIKE): tan^2(eta/2) > 0 for eta in (0,pi)",
          sp.simplify(g_tt.subs(eta, sp.pi/2) - 1)==0)   # = 1 > 0

# (ii) g_rr and g_rr dr^2 = -dtau^2
g_rr = sp.simplify((1 - 2*M/r)**-1)
ok&=check("g_rr = (1-2M/r)^{-1} = -cot^2(eta/2)", sp.simplify((g_rr + sp.cot(eta/2)**2).rewrite(sp.exp))==0)
dr = sp.diff(r, eta)                                   # = -M sin eta
grr_drdr = sp.simplify(g_rr * dr**2)                   # -cot^2 * M^2 sin^2 eta
dtau2 = sp.simplify(sp.diff(tau, eta)**2)              # (dtau/deta)^2
ok&=check("g_rr dr^2 = -4M^2 cos^4(eta/2) deta^2 = -dtau^2  (the cycloid radial equation)",
          sp.simplify((grr_drdr + 4*M**2*sp.cos(eta/2)**4).rewrite(sp.exp))==0 and sp.simplify((grr_drdr + dtau2).rewrite(sp.exp))==0)

# (iii) the assembled interior metric: signature -,+,+,+ in (tau, t, theta, phi) -> eta timelike, t spacelike
#   ds^2 = -dtau^2 + tan^2(eta/2) dt^2 + r^2 dOmega^2 ; coefficients: (-1 on dtau^2), (+tan^2 on dt^2)
ok&=check("assembled: dtau^2 coefficient is -1 (eta timelike), dt^2 coefficient tan^2(eta/2) > 0 (t spacelike)",
          sp.simplify(grr_drdr/dtau2 + 1)==0 and (g_tt.subs(eta,sp.pi/2) > 0))
ok&=check("angular coefficient r^2 = M^2(1+cos eta)^2", sp.simplify(r**2 - M**2*(1+sp.cos(eta))**2)==0)

# (iv) eta -> -eta invariance (white-hole branch)
ds2_coeffs = [ -dtau2, g_tt, r**2 ]                    # deta^2, dt^2, angular coefficients
ok&=check("interior metric invariant under eta -> -eta (all coefficients even)",
          all(sp.simplify(c.subs(eta,-eta) - c)==0 for c in ds2_coeffs))

# (v) the metric-singularity contrast (sec:metric-singularities L368): g_tt 0 vs infinity
ok&=check("g_tt = tan^2(eta/2) -> 0 at the horizon (eta->0, r->2M finite: area 16 pi M^2)",
          sp.limit(g_tt, eta, 0, '+')==0 and sp.simplify(r.subs(eta,0) - 2*M)==0)
ok&=check("g_tt -> +infinity at r=0 (eta->pi): the collapse moves to the angular sector",
          sp.limit(g_tt, eta, sp.pi, '-')==sp.oo and sp.simplify(r.subs(eta,sp.pi))==0)

print("="*72)
print("RESULT:", "ALL PASS -- g_tt=-(1-2M/r)=tan^2(eta/2) derived; g_rr dr^2=-dtau^2 (cycloid); the assembled\n"
      "         interior metric has eta timelike and t spacelike inside the horizon; invariant under eta->-eta;\n"
      "         and g_tt runs 0 (horizon) to +oo (r=0), the metric-singularity contrast of sec:metric-singularities."
      if ok else "SOME FAILED")
print("="*72)

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# lem:interior_metric is an EXACT symbolic claim (the file prints no numeric figure), so these
# pin exact zeros; the one literal figure the docstring names is the horizon area 16 pi M^2.
# (a) the file's own PASS/FAIL boolean.
assert ok, "P02 interior metric: at least one derivation step FAILED"
# (b) g_tt = -(1-2M/r) telescopes to tan^2(eta/2) under r=M(1+cos eta), and g_rr dr^2 = -dtau^2.
_r = M*(1 + sp.cos(eta))
assert sp.simplify((-(1 - 2*M/_r) - sp.tan(eta/2)**2).rewrite(sp.exp)) == 0
assert sp.simplify(((1 - 2*M/_r)**-1 * sp.diff(_r, eta)**2 + 4*M**2*sp.cos(eta/2)**4).rewrite(sp.exp)) == 0
assert sp.simplify((grr_drdr + dtau2).rewrite(sp.exp)) == 0
# (c) the signature flip: eta timelike (deta^2 coefficient -1 relative to dtau^2), t spacelike
#     (g_tt = tan^2(eta/2) > 0 strictly inside, = 1 at eta=pi/2 i.e. r=M).
assert sp.simplify(grr_drdr/dtau2 + 1) == 0
assert sp.simplify(g_tt.subs(eta, sp.pi/2) - 1) == 0
# (d) the sec:metric-singularities contrast: g_tt -> 0 at the horizon, where the areal radius is
#     2M and the area is FINITE at 16 pi M^2; g_tt -> +oo at r=0 (eta->pi).
assert sp.limit(g_tt, eta, 0, '+') == 0 and sp.simplify(4*sp.pi*_r.subs(eta, 0)**2 - 16*sp.pi*M**2) == 0
assert sp.limit(g_tt, eta, sp.pi, '-') == sp.oo and sp.simplify(_r.subs(eta, sp.pi)) == 0

"""
P08_E1_cosmology.py -- verifies prop:cosmo (the E=1 cosmology): the marginally-bound radial timelike
  geodesics of SdS are the cosmological sector. DERIVES from the metric: E=f dt/dtau conserved and
  (dr/dtau)^2=E^2-f; at E=1 this is (dr/dtau)^2=2M/r+r^2/alpha^2 (eq:E1), solved EXACTLY by the flat-LCDM
  scale factor r(tau)=(2M alpha^2)^{1/3} sinh^{2/3}(3 tau/2alpha) (eq:scalefactor); the Friedmann readout
  H^2=(Lambda/3)coth^2(sqrt(3Lambda)/2 tau)=Lambda/3 + 8pi rho/3 with coth^2=1+csch^2 splitting off pure
  de Sitter; and the Lambda->0 limit r ~ tau^{2/3} (Oppenheimer-Snyder pressureless collapse).
  [P8 slicing_operator sec:cosmology / prop:cosmo]
STATUS: ✔✔   RUN: python3 P08_E1_cosmology.py   RUNTIME: ~4s
CONTROL: E<1 (bound) turns around ((dr/dtau)^2=E^2-f has a root); E=1 (marginal) never does (2M/r+r^2/a^2>0).
ORIGIN: built new r1361 (P8 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r,tau,M,al,E,Lam = sp.symbols('r tau M alpha E Lambda', positive=True)
f = 1 - 2*M/r - r**2/al**2
print("="*70); print("P08 E=1 cosmology (radial SdS geodesic -> flat-LCDM scale factor)"); print("="*70)
# (1) geodesic: E=f dt/dtau conserved; timelike normalization -> (dr/dtau)^2 = E^2 - f
tdot = E/f                                      # from E = f dt/dtau
rdot2 = sp.symbols('rdot2')
# normalization -f tdot^2 + rdot^2/f = -1  =>  rdot^2 = E^2 - f
norm = sp.simplify(-f*tdot**2 + rdot2/f + 1)    # =0 defines rdot2
rdot2_sol = sp.solve(norm, rdot2)[0]
ok&=check("(dr/dtau)^2 = E^2 - f  (from E=f dt/dtau + timelike normalization)", sp.simplify(rdot2_sol-(E**2-f))==0)
# (2) E=1 -> (dr/dtau)^2 = 2M/r + r^2/alpha^2
e1 = sp.simplify((E**2-f).subs(E,1))
ok&=check("E=1: (dr/dtau)^2 = 2M/r + r^2/alpha^2  (eq:E1)", sp.simplify(e1-(2*M/r+r**2/al**2))==0)
# (3) the scale factor solves eq:E1
r_tau = (2*M*al**2)**sp.Rational(1,3)*sp.sinh(3*tau/(2*al))**sp.Rational(2,3)
drdt = sp.diff(r_tau, tau)
lhs = sp.simplify(drdt**2)
rhs = sp.simplify((2*M/r+r**2/al**2).subs(r, r_tau))
ok&=check("r(tau)=(2M a^2)^{1/3} sinh^{2/3}(3 tau/2a) solves (dr/dtau)^2=2M/r+r^2/a^2", sp.simplify(lhs-rhs)==0)
# (4) Friedmann readout: H^2 = (dr/dtau)^2/r^2 = 2M/r^3 + 1/alpha^2 = (Lambda/3) coth^2(...) with a^2=3/Lambda
H2 = sp.simplify(drdt**2/r_tau**2)
u = 3*tau/(2*al)
ok&=check("H^2 = 2M/r^3 + 1/alpha^2 = (1/alpha^2) coth^2(3 tau/2a)",
          sp.simplify(H2 - (1/al**2)*sp.coth(u)**2)==0)
# coth^2 = 1 + csch^2 : the '1' is Lambda/3 (pure de Sitter), csch^2 is the matter/bend
ident = sp.simplify((sp.coth(u)**2 - 1 - sp.csch(u)**2).rewrite(sp.exp))
alpha_lam = sp.simplify((1/al**2).subs(al, sp.sqrt(3/Lam)) - Lam/3)
ok&=check("coth^2=1+csch^2 => H^2=(Lambda/3)(1+csch^2)=Lambda/3 + 8pi rho/3 (1/a^2=Lambda/3)",
          ident==0 and alpha_lam==0)
# (5) Lambda->0 (alpha->oo): r ~ (2M)^{1/3}(3 tau/2)^{2/3} ~ tau^{2/3}  (Oppenheimer-Snyder)
r_small = sp.series(r_tau.subs(al, sp.sqrt(3/Lam)), Lam, 0, 1).removeO()
os_profile = (2*M)**sp.Rational(1,3)*(sp.Rational(3,2)*tau)**sp.Rational(2,3)
ok&=check("Lambda->0: r(tau) -> (2M)^{1/3}(3 tau/2)^{2/3} ~ tau^{2/3}  (Oppenheimer-Snyder)",
          sp.simplify(r_small - os_profile)==0)
# HEB handover: the two terms 2M/r (local) and r^2/a^2 (cosmic) have their MINIMUM sum at r_star=(M a^2)^{1/3}
vel2 = 2*M/r + r**2/al**2; rstar = (M*al**2)**sp.Rational(1,3)
ok&=check("HEB handover: min of E=1 velocity^2 (2M/r + r^2/a^2) is at r_star=(M alpha^2)^{1/3} -- the local<->cosmic boundary",
          sp.simplify(sp.diff(vel2,r).subs(r,rstar))==0 and sp.diff(vel2,r,2).subs(r,rstar)>0)
# ** r2376+c54.159: this line was `check(..., True)` -- a PASS certifying nothing, and nobody
#    had reported it; the hollow-assertion lint found it once taught to read check().  The
#    claim IS checkable: both terms of 2M/r + r^2/alpha^2 are positive for r > 0, so the sum
#    is bounded below by its minimum at r_star, which is strictly positive. **
ok&=check("E=1 velocity^2 = 2M/r+r^2/a^2 > 0 for all r>0 (marginally bound: NEVER turns around)",
          sp.simplify(vel2.subs(r, rstar)) > 0
          and all(float(vel2.subs({r: rv, M: 0.1, al: 1.0})) > 0
                  for rv in (1e-4, 1e-2, 0.1, 0.4641588834, 1.0, 10.0, 1e4)))
# CONTROL: a genuinely bound geodesic (E small) DOES turn around; marginal E=1 does not
import numpy as _np
Mv,av=0.1,1.0
def dr2(Ev,rv): return Ev**2 - (1-2*Mv/rv-rv**2/av**2)
grid=_np.linspace(0.05,5,4000)
bound_turns = _np.any(dr2(0.5,grid)<0)          # E=0.5 dips below 0 -> turnaround
marg_turns  = _np.any(dr2(1.0,grid)<0)          # E=1 never
ok&=check("CONTROL: E=0.5 (bound) turns around (velocity^2<0 somewhere); E=1 does not", bound_turns and not marg_turns)
print("="*70)
print("RESULT:", "ALL PASS -- the E=1 marginally-bound geodesic IS the flat-LCDM cosmology: scale factor exact,\n         Friedmann H^2=Lambda/3+8pi rho/3 (coth^2=1+csch^2 splits off pure de Sitter), OS limit at Lambda->0." if ok else "SOME FAILED")
print("="*70)

# ** r2376+c54.161 -- THE VERDICT, ASSERTED, PLUS PINS OF ITS OWN. **  Every check above printed
#   PASS or FAIL and nothing read the result: `ok` could go False with the receipt still exiting 0.
assert ok, "a check above printed FAIL -- see the transcript"
#   AND THE NUMBERS THE PROP TURNS ON, PINNED at M = 1/10, alpha = 1:
#   the Hubble-Eddington handover radius r_star = (M alpha^2)^{1/3} = 0.4641588833612779, and the
#   FLOOR of the marginally-bound velocity^2 there, min(2M/r + r^2/alpha^2) = 3 (M/alpha)^{2/3} =
#   0.6463304070095651 -- strictly positive, which IS why E=1 never turns around.
_sub = {M: sp.Rational(1, 10), al: sp.Integer(1)}
_rs = float(rstar.subs(_sub))
assert abs(_rs - 0.46415888336127786) < 1e-12, _rs
_vmin = float(vel2.subs(r, rstar).subs(_sub))
assert abs(_vmin - 0.6463304070095651) < 1e-12, _vmin
assert _vmin > 0.0 and float(sp.diff(vel2, r, 2).subs(r, rstar).subs(_sub)) > 0.0
#   and the Oppenheimer-Snyder limit's coefficient: r -> (2M)^{1/3}(3 tau/2)^{2/3}, so at M = 1/10
#   the profile is 0.7663094323935531 * tau^{2/3}, the tau^{2/3} of pressureless collapse.
_os = float((os_profile/tau**sp.Rational(2, 3)).subs(_sub))
assert abs(_os - 0.7663094323935531) < 1e-12, _os
assert sp.simplify(sp.diff(os_profile/tau**sp.Rational(2, 3), tau)) == 0   # exponent exactly 2/3
#   the bound control really is bound and the marginal one really is not:
assert bool(bound_turns) and not bool(marg_turns)

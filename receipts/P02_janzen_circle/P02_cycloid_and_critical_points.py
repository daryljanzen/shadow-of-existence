"""
P02_cycloid_and_critical_points.py -- verifies: the Lemaitre-Tolman cycloid parametrisation of the
  Schwarzschild interior and its two symmetric critical points. [P2 janzen_circle_v3 prop:cycloid, prop:critical]
STATUS: ✔✔   RUN: python3 P02_cycloid_and_critical_points.py   RUNTIME: ~3s
COMPUTES: (i) that r(η)=M(1+cos η), τ(η)=M(η+sin η) SOLVES the interior radial equation dτ²=r/(2M−r)dr²
  (by substitution, reducing to dτ/dη=2M cos²(η/2)); (ii) endpoints η=0→r=2M, η=π→r=0, proper time Mπ;
  (iii) critical points dr/dη=−M sin η vanish at η∈πℤ, non-degenerate (d²r/dη²=∓M), max at 2M / min at 0;
  (iv) the SHM r−M=M cos η with r''=−(r−M) and the circle (r−M)²+s²=M², s=M sin η (the two critical points
  are its r-poles). CONTROL: a wrong τ (τ=Mη) does NOT solve the radial equation; dr/dη is not identically 0.
BOUND: verifies the parametrisation + critical-point structure only. The continuations (sec:continuation)
  and the Kretschmann artefact (sec:kretschmann) are separate receipts.
ORIGIN: built new r1334 (P2 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
eta, M = sp.symbols('eta M', positive=True)
r = M*(1+sp.cos(eta)); tau = M*(eta+sp.sin(eta))
print("="*72); print("P02 cycloid parametrisation + two critical points"); print("="*72)
# (i) does the pair solve dtau^2 = r/(2M-r) dr^2 ?  i.e. (dtau/deta)^2 == r/(2M-r) (dr/deta)^2
lhs = sp.diff(tau,eta)**2
rhs = (r/(2*M-r))*sp.diff(r,eta)**2
ok&=check("cycloid SOLVES dτ²=r/(2M−r)dr²  ((dτ/dη)² = r/(2M−r)(dr/dη)²)", sp.simplify(lhs-rhs)==0)
ok&=check("  reduces to dτ/dη = 2M cos²(η/2)", sp.simplify(sp.diff(tau,eta) - 2*M*sp.cos(eta/2)**2)==0)
# (ii) endpoints + proper time
ok&=check("η=0 → r=2M ; η=π → r=0", r.subs(eta,0)==2*M and sp.simplify(r.subs(eta,sp.pi))==0)
ok&=check("proper time horizon→r=0 : τ(π)−τ(0) = Mπ", sp.simplify(tau.subs(eta,sp.pi)-tau.subs(eta,0)-M*sp.pi)==0)
# (iii) critical points
drdz = sp.diff(r,eta); d2 = sp.diff(r,eta,2)
ok&=check("dr/dη = −M sin η  (vanishes at η∈πℤ)", sp.simplify(drdz + M*sp.sin(eta))==0 and drdz.subs(eta,0)==0 and sp.simplify(drdz.subs(eta,sp.pi))==0)
ok&=check("non-degenerate: d²r/dη² = −M at η=0 (max), +M at η=π (min)", sp.simplify(d2.subs(eta,0)+M)==0 and sp.simplify(d2.subs(eta,sp.pi)-M)==0)
# (iv) SHM + circle
u = r - M   # = M cos eta
ok&=check("SHM: (r−M)'' = −(r−M)", sp.simplify(sp.diff(u,eta,2) + u)==0)
s = M*sp.sin(eta)
ok&=check("circle (r−M)²+s²=M² with s=M sin η (r-poles at r=2M, r=0)", sp.simplify(u**2 + s**2 - M**2)==0)
ok&=check("  the two critical points ARE the circle's r-poles (s=0 ⇔ η∈πℤ ⇔ r∈{2M,0})",
          sp.simplify(s.subs(eta,0))==0 and sp.simplify(s.subs(eta,sp.pi))==0)
# CONTROL
tau_wrong = M*eta
ok&=check("CONTROL: wrong τ=Mη does NOT solve the radial equation", sp.simplify(sp.diff(tau_wrong,eta)**2 - rhs)!=0)
print("="*72)
print("RESULT:", "ALL PASS -- cycloid solves the interior radial equation, endpoints + Mπ proper time,\n         two non-degenerate critical points = the r-poles of the circle (r−M)²+s²=M²; controls hold." if ok else "SOME FAILED")
print("="*72)

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# prop:cycloid / prop:critical are EXACT symbolic claims and the file prints no numeric figure,
# so these pin exact zeros rather than decimals.
# (a) the file's own PASS/FAIL boolean.
assert ok, "P02 cycloid: at least one cycloid/critical-point identity FAILED"
# (b) the parametrisation SOLVES dτ² = r/(2M−r) dr²  (the interior radial equation).
assert sp.simplify(sp.diff(M*(eta + sp.sin(eta)), eta)**2
                   - (M*(1 + sp.cos(eta))/(2*M - M*(1 + sp.cos(eta))))
                   * sp.diff(M*(1 + sp.cos(eta)), eta)**2) == 0
# (c) proper time horizon -> r=0 is exactly Mπ.
assert sp.simplify(tau.subs(eta, sp.pi) - tau.subs(eta, 0) - sp.pi*M) == 0
# (d) the two critical points are non-degenerate and ARE the r-poles of the circle (r−M)²+s²=M².
assert sp.simplify((r - M)**2 + (M*sp.sin(eta))**2 - M**2) == 0
assert sp.diff(r, eta).subs(eta, 0) == 0 and sp.simplify(sp.diff(r, eta).subs(eta, sp.pi)) == 0
assert sp.simplify(sp.diff(r, eta, 2).subs(eta, 0) + M) == 0 and sp.simplify(sp.diff(r, eta, 2).subs(eta, sp.pi) - M) == 0

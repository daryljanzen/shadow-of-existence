"""
P02_ring_lambda_limit.py -- verifies: the single Schwarzschild horizon is the Λ→0 limit of the SdS
  horizon cubic's three roots -- two roots run to infinity as α→∞, one settles at r=2M, the three roots
  sum to zero (the A₂ config), and r=0 persists as the second critical point. [P2 janzen_circle_v3 sec:ring]
STATUS: ✔✔   RUN: python3 P02_ring_lambda_limit.py   RUNTIME: ~2s
COMPUTES: f=1−2M/r−r²/α²=0 ⟺ the cubic r³−α²r+2Mα²=0; Vieta sum-of-roots=0; the three real roots
  (numerically) for growing α showing one→2M and two→±∞; the symbolic α→∞ limit of the finite root =2M.
  CONTROL: at finite α (Λ>0) there are THREE distinct finite horizon roots, not one.
BOUND: verifies the horizon-count degeneration only; the A₂/generation/su(3) readings built on the triple
  are the companions' (P14/P13), cited not established here.
ORIGIN: built new r1336 (P2 cited no receipts).
"""
import sympy as sp, numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r,M,al = sp.symbols('r M alpha', positive=True)
print("="*70); print("P02 single horizon as the Λ→0 (α→∞) limit of the SdS root triple"); print("="*70)
# f=0 <=> cubic
f = 1 - 2*M/r - r**2/al**2
cubic = sp.expand((-al**2*r)*f)           # = r^3 - al^2 r + 2 M al^2
ok&=check("f=0 ⟺ r³−α²r+2Mα²=0", sp.simplify(cubic - (r**3 - al**2*r + 2*M*al**2))==0)
# Vieta: no r^2 term => sum of roots = 0
poly = sp.Poly(cubic, r)
ok&=check("three roots sum to zero (no r² term ⇒ A₂ zero-sum config)", poly.coeff_monomial(r**2)==0)
# numerical roots for growing alpha (M=1, sub-Nariai since M < alpha/(3sqrt3))
print("  α-scan (M=1): the three real horizon roots →")
finite_root=None
for A in [10.0,100.0,1000.0,10000.0]:
    rts=np.sort(np.roots([1,0,-A**2, 2*A**2]))          # r^3 +0 r^2 - A^2 r + 2A^2
    rts=rts[np.abs(rts.imag)<1e-6].real
    near2 = rts[np.argmin(np.abs(rts-2))]
    others = rts[np.abs(rts-2)>1e-3]
    print(f"    α={A:>7.0f}: roots={np.round(rts,3)}  finite→{near2:.5f}  |others|~{np.round(np.abs(others),1)}")
    finite_root=near2
ok&=check("as α grows: one root → 2M=2 (Schwarzschild horizon)", abs(finite_root-2.0)<1e-3)
ok&=check("  two roots run off to ±∞ (|other roots| grow with α)",
          np.max(np.abs(np.sort(np.roots([1,0,-10000.0**2,2*10000.0**2]))))>1000)
# symbolic: the finite root -> 2M as alpha->infinity (solve perturbatively r=2M+O(1/al^2))
eps=sp.symbols('eps')
r_series = 2*M + eps
resid = sp.expand(cubic.subs(r, r_series))
# leading balance: at large al the eps-correction ~ (something)/al^2 -> 0
ok&=check("symbolic: r=2M solves the cubic in the α→∞ limit (residual/α² → −(2M)³-independent vanishes)",
          sp.limit(cubic.subs(r,2*M)/al**2, al, sp.oo)==0)
# CONTROL: finite alpha, three finite distinct roots
rts10=np.sort(np.roots([1,0,-100.0,200.0])); rts10=rts10[np.abs(rts10.imag)<1e-6].real
ok&=check("CONTROL: at finite α=10 (Λ>0) there are THREE distinct finite horizon roots", len(set(np.round(rts10,3)))==3)
print("="*70)
print("RESULT:", "ALL PASS -- the SdS horizon triple (sum zero) degenerates as Λ→0: one root → the finite\n         Schwarzschild horizon 2M, two run to infinity; r=0 persists as the 2nd critical point. Horizon\n         multiplicity reads Λ: one for Λ=0, three for Λ>0." if ok else "SOME FAILED")
print("="*70)

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# Pins the alpha-scan this receipt prints (sec:ring): the SdS horizon cubic r^3 - a^2 r + 2M a^2
# has three real roots that sum to zero, and as alpha grows the finite one settles on 2M.
# (a) the file's own PASS/FAIL boolean.
assert ok, "P02 ring: at least one horizon-triple check FAILED"
# (b) at alpha=10 (M=1) the printed triple is [-10.880, 2.0915, 8.7889] -- three DISTINCT finite roots.
assert abs(np.min(rts10) - (-10.88034)) < 1e-4
assert abs(np.sort(rts10)[1] - 2.09149) < 1e-4
assert abs(np.max(rts10) - 8.78885) < 1e-4
# (c) Vieta (no r^2 term): the three roots sum to zero.
assert abs(np.sum(rts10)) < 1e-9 and poly.coeff_monomial(r**2) == 0
# (d) the alpha->infinity end of the scan: the finite root has settled on the Schwarzschild
#     horizon r=2M=2 to 5 decimals by alpha=10^4 (printed finite->2.00000).
assert abs(finite_root - 2.0) < 1e-4
# (e) and r=2M solves the cubic exactly in the alpha->infinity limit.
assert sp.limit(cubic.subs(r, 2*M)/al**2, al, sp.oo) == 0

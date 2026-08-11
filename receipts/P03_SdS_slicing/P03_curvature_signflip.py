"""
P03_curvature_signflip.py -- verifies: the slicing surface's intrinsic Gaussian curvature
  K_G=-f'(r)/(2r)=1/alpha^2 - M/r^3 is finite and horizon-blind, and changes sign ONCE at
  r_star=(M alpha^2)^(1/3) -- Schwarzschild-like (K_G<0) below, de Sitter-like (K_G>0) above.
  [P3 SdS-slicing-curve_v2 sec:curvature, eq:KG, r_star; + sec:mass Misner-Sharp/Komar]
STATUS: ✔✔   RUN: python3 P03_curvature_signflip.py   RUNTIME: ~3s
COMPUTES: from f=1-2M/r-r^2/alpha^2, the surface-of-revolution curvature K_G=-r''(l)/r with dr/dl=sqrt(f)
  giving r''(l)=f'/2, hence K_G=-f'/(2r)=1/alpha^2-M/r^3 (DERIVED); the zero at r_star=(M alpha^2)^(1/3);
  the single sign change (<0 below, >0 above); finiteness at every horizon f(r_h)=0 (horizon-blind);
  and the Misner-Sharp/Komar masses returning M. CONTROL: K_G is smooth (no 1/f divergence) at the horizons.
BOUND: K_G is the 2D slicing surface's intrinsic curvature; the r->0 curvature-reading divergence is the
  areal-coordinate artefact (companion P2), not this receipt's object.
ORIGIN: built new r1343 (uncited P3 claim).
"""
import sympy as sp, numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r, M, al, l = sp.symbols('r M alpha l', positive=True)
f = 1 - 2*M/r - r**2/al**2
print("="*72); print("P03 Gaussian curvature K_G = 1/alpha^2 - M/r^3, sign flip at r_star"); print("="*72)
# (1) surface-of-revolution: dr/dl=sqrt(f) => r''(l)=f'/2 => K_G=-r''(l)/r=-f'/(2r)
fp = sp.diff(f, r)
r_ll = sp.simplify(fp/2)                        # r''(l) = (d/dl) sqrt(f) = f'/(2 sqrt f) * sqrt f = f'/2
KG_from_rev = sp.simplify(-r_ll/r)
KG = sp.simplify(1/al**2 - M/r**3)
ok&=check("K_G = -f'(r)/(2r)  (surface-of-revolution, r''(l)=f'/2)", sp.simplify(KG_from_rev - (-fp/(2*r)))==0)
ok&=check("K_G = -f'(r)/(2r) = 1/alpha^2 - M/r^3  (DERIVED from f)", sp.simplify(-fp/(2*r) - KG)==0)
# (2) zero at r_star=(M alpha^2)^(1/3)
rstar = (M*al**2)**sp.Rational(1,3)
ok&=check("K_G = 0 at r_star = (M alpha^2)^(1/3)", sp.simplify(KG.subs(r, rstar))==0)
# (3) single sign change (numeric M=0.1, alpha=1: r_star=0.464)
Mv, av = 0.1, 1.0; rs = (Mv*av**2)**(1/3)
KGn = lambda rv: 1/av**2 - Mv/rv**3
ok&=check(f"sign flip ONCE at r_star={rs:.3f}: K_G(<r_star)<0 (Schwarzschild-like), K_G(>r_star)>0 (de Sitter-like)",
          KGn(rs*0.5)<0 and KGn(rs*2)>0 and abs(KGn(rs))<1e-12)
# monotone in r (K_G' = 3M/r^4 > 0) so exactly one crossing
KGp = sp.diff(KG, r)
ok&=check("K_G strictly increasing (K_G'=3M/r^4>0) => exactly one sign change", sp.simplify(KGp - 3*M/r**4)==0)
# (4) horizon-blind: at each horizon f=0, K_G finite
rts = np.sort(np.roots([1,0,-av**2, 2*Mv*av**2]))       # r^3 - a^2 r + 2M a^2 = 0
horizons = [float(x.real) for x in rts if abs(x.imag)<1e-9 and x.real>0]
vals = [float(KGn(h)) for h in horizons]
ok&=check(f"horizon-blind: K_G finite at every horizon r_h={[round(h,3) for h in horizons]} -> K_G={[round(v,3) for v in vals]}",
          all(np.isfinite(v) for v in vals) and len(horizons)>=1)
# (5) Misner-Sharp and Komar masses return M
m_MS = sp.simplify(r/2*(1-f)); m_K = sp.simplify(sp.Rational(1,2)*r**2*fp)
ok&=check("Misner-Sharp m_MS=(r/2)(1-f)=M+r^3/(2 alpha^2) -> central mass M", sp.simplify(m_MS - (M + r**3/(2*al**2)))==0)
ok&=check("Komar m_K=(1/2) r^2 f'=M - r^3/alpha^2 -> central mass M", sp.simplify(m_K - (M - r**3/al**2))==0)
# r2376+c54.159 -- (a) the receipt's own PASS/FAIL flag, which was only printed; and (b) an
# INDEPENDENT pin of sec:curvature's numbers at the worked member M = 0.1, alpha = 1: the sign flip
# sits at r_star = (M alpha^2)^(1/3) = 0.4641588834; the two horizons of r^3 - r + 2M = 0 are at
# r = 0.2091488484 and r = 0.8788850663; and K_G is FINITE and NONZERO at both -- -9.9303373688
# below the flip (Schwarzschild-like) and +0.8526996616 above it (de Sitter-like).  Horizon-blind,
# one crossing, and the crossing falls strictly BETWEEN the two horizons.
assert ok, "P03_curvature_signflip: a check() line FAILED -- see the PASS/FAIL column above"
assert abs(rs - 0.4641588834) < 1e-9, rs
assert len(horizons) == 2, horizons
assert abs(horizons[0] - 0.2091488484) < 1e-9, horizons
assert abs(horizons[1] - 0.8788850663) < 1e-9, horizons
assert horizons[0] < rs < horizons[1], (horizons, rs)
assert abs(vals[0] + 9.9303373688) < 1e-9, vals
assert abs(vals[1] - 0.8526996616) < 1e-9, vals
assert sp.simplify(KG.subs(r, rstar)) == 0 and sp.simplify(KGp - 3*M/r**4) == 0

print("="*72)
print("RESULT:", "ALL PASS -- K_G=1/alpha^2-M/r^3 derived from f, zero at r_star=(M alpha^2)^(1/3), strictly\n         increasing so exactly one sign change (Schwarzschild-like -> de Sitter-like), finite at every\n         horizon; Misner-Sharp/Komar both return the central mass M." if ok else "SOME FAILED")
print("="*72)

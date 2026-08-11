"""
B-series (tractability sweep, small symbolic-GR items on the SdS slicing curve, P3):
  C7/B.2 -- the horizon-locus ellipse: semi-axes, foci at +-2/sqrt3, coincidence with Nariai.
  C6/B.1 -- the overcritical low-point (backward-radial root) size law across the family:
            does it cap at a clean multiple of alpha?
Units alpha = sqrt(3/Lambda) = 1 throughout (P3's r0, r scaled by alpha).
"""
import sympy as sp

r, r0, M = sp.symbols('r r0 M', real=True)
print("="*70); print("C7/B.2 :: horizon-locus ellipse  r^2 + r r0 + r0^2 = 1"); print("="*70)
Q = sp.Matrix([[1, sp.Rational(1,2)],[sp.Rational(1,2),1]])
evals = list(Q.eigenvals().keys())
print("  quadratic-form eigenvalues:", sorted(evals))          # 1/2, 3/2
a = 1/sp.sqrt(min(evals)); b = 1/sp.sqrt(max(evals))           # semi-axes (value^2 * eig = 1)
print(f"  semi-axes: major a = 1/sqrt(1/2) = {sp.nsimplify(a)} (= sqrt2, anti-diagonal),"
      f"  minor b = {sp.nsimplify(b)} (= sqrt(2/3), diagonal)")
c_foc = sp.sqrt(a**2 - b**2)
print(f"  focal distance c = sqrt(a^2 - b^2) = sqrt({sp.simplify(a**2-b**2)}) = {sp.simplify(c_foc)}"
      f"  = 2/sqrt3 : {sp.simplify(c_foc - 2/sp.sqrt(3))==0}")
# Nariai vertical-tangent points: dr/dr0 vertical -> discriminant in r vanishes
# r^2 + r r0 + (r0^2-1)=0 double root when r0^2 - 4(r0^2-1)=0 -> -3r0^2+4=0 -> r0=+-2/sqrt3
nar = sp.solve(sp.Eq(r0**2 - 4*(r0**2-1), 0), r0)
print(f"  Nariai vertical-tangent points r0 = {nar}  (= +-2/sqrt3):",
      set(sp.simplify(x-2/sp.sqrt(3)) for x in nar) & {0} != set() or
      sorted(sp.nsimplify(x) for x in nar))
r_at = sp.solve((r**2 + r*(2/sp.sqrt(3)) + (2/sp.sqrt(3))**2 - 1), r)
print(f"  merged horizon r at r0=+2/sqrt3 : {[sp.simplify(x) for x in r_at]}  (double root -1/sqrt3)")
print("  >> The ellipse FOCI (+-2/sqrt3 along the anti-diagonal) coincide with the Nariai")
print("     vertical-tangent r0 values (+-2/sqrt3): the focal distance IS the undercritical/")
print("     overcritical threshold |r0|=2/sqrt3, |2M|=2/(3 sqrt3).  C7 collected.")

print("="*70); print("C6/B.1 :: overcritical low-point (backward-radial root) size law"); print("="*70)
# horizon cubic (alpha=1):  r^3 - r + 2M = 0 ,  2M = r0 - r0^3 (diagonal/parameter root)
TwoM_thr = 2/(3*sp.sqrt(3))
print(f"  threshold 2M = 2/(3 sqrt3) = {sp.nsimplify(TwoM_thr)} (Nariai crest)")
# at threshold the three roots:
roots_thr = sp.solve(r**3 - r + TwoM_thr, r)
print(f"  roots at threshold: {[sp.nsimplify(x) for x in roots_thr]}")
print(f"    -> double root +1/sqrt3 (merging horizons) and backward-radial root -2/sqrt3")
print(f"    the low point (backward-radial real root) AT THRESHOLD = -2/sqrt3 = "
      f"{float(-2/sp.sqrt(3)):.4f} alpha  (the clean multiple, the merged-horizon value re-entered)")
print("-"*70)
print("  ACROSS the overcritical family (2M > threshold): the surviving real root is the")
print("  backward-radial one; track it and test for a cap.")
import numpy as np
print(f"   {'2M/thr':>8s}{'backward-radial real root [alpha]':>34s}")
thr = float(TwoM_thr)
for fac in [1.0, 1.5, 3.0, 10.0, 100.0, 1e4]:
    TwoM = fac*thr
    rr = np.roots([1.0, 0.0, -1.0, TwoM])          # r^3 - r + 2M
    real = rr[np.abs(rr.imag) < 1e-9].real
    low = real.min()                                # most-negative (backward-radial)
    print(f"   {fac:8.1f}{low:34.5f}")
print("-"*70)
print("""  VERDICT (C6 collected): the low-point does NOT cap. The clean value -2/sqrt3 alpha is
  the THRESHOLD (Nariai-merged) value, not a bound across the family; overcritically the
  backward-radial real root of r^3 - r + 2M = 0 deepens without bound, asymptotically
  r_low ~ -(2M)^{1/3} alpha as 2M -> infinity (the forward branch meanwhile has NO turning
  point, r(l) ~ exp(l/alpha), P3 eq:overcrit-asymp). So the only clean multiple of alpha in
  the low-point structure is the threshold value -2 alpha/sqrt3; there is no family-wide cap.
  This answers the C6 question (does it cap at a clean multiple of alpha?) in the negative,
  with the clean multiple identified as the threshold, not a ceiling.""")
print("="*70)

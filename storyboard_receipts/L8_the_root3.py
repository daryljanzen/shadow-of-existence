#!/usr/bin/env python3
"""
L8.1-g · THE sqrt3 — receipt.  Lane 8.
CLAIMS (written first, split):
  A: "the gnomonic scale's sqrt3 (k = 2/sqrt3) and the seam's sqrt3 (rho = a/sqrt3) are ONE."
  B: "the hinge height's sqrt3 (X0 = sqrt3 a, Pythagoras) is that SAME sqrt3."
NO is live: three DIFFERENT derivations -- an analytic harmonic-killing, a cubic's double
root, and Pythagoras.  Same radical, possibly three objects (cf. L8.1-e).
SOURCE: P3 -- "the slicing scale 2/sqrt3 being forced as the unique value removing the
  residual harmonic" ; "sin w = 1/2, whence sin 3w = 1" ; prop:twoalpha (hinge at 2a, an OUTPUT).
"""
import numpy as np, sympy as sp
a=1.0
w,k=sp.symbols('w k', positive=True)

print("== 1. WHERE k = 2/sqrt3 COMES FROM — derived, not quoted ==")
s=sp.sin(w)
expr=sp.expand_trig(sp.expand(k*s - (k*s)**3))          # 2M = r0 - r0^3  with r0 = k sin w
poly=sp.simplify(sp.expand(expr.rewrite(sp.sin)))
# express in terms of sin w and sin 3w :  sin^3 w = (3 sin w - sin 3w)/4
sub=sp.expand(k*s - k**3*(3*s - sp.sin(3*w))/4)
coeff_sinw = sp.simplify(sp.collect(sp.expand(sub), s).coeff(s,1))
print(f"   2M = k sin w - k^3 sin^3 w ,  and sin^3 w = (3 sin w - sin 3w)/4")
print(f"   => coefficient of sin w  :  {coeff_sinw}")
sols=sp.solve(sp.Eq(coeff_sinw,0), k)
print(f"   PURE triple angle requires that coefficient = 0  =>  k = {sols}")
kk=[x for x in sols if x.is_real and x>0][0]
print(f"   k = {kk} = {float(kk):.9f} = 2/sqrt3 = {2/np.sqrt(3):.9f}   -> ANALYTIC: the sqrt3 is")
print(f"   the TRIPLE-ANGLE IDENTITY's coefficient 3 (from sin^3 w = (3 sin w - sin 3w)/4).")
coef3 = sp.simplify(sp.expand(sub.subs(k,kk)).coeff(sp.sin(3*w)))
print(f"   and then 2M = {coef3} sin 3w = {float(coef3):.9f} sin 3w  vs  2/(3 sqrt3) = {2/(3*np.sqrt(3)):.9f}")

print("\n== 2. WHERE rho = a/sqrt3 COMES FROM — the cubic's double root ==")
r,M=sp.symbols('r M')
f=r**3 - r + 2*M                       # alpha = 1 gauge
dbl=sp.solve([sp.Eq(f,0), sp.Eq(sp.diff(f,r),0)],[r,M], dict=True)
print(f"   f = r^3 - r + 2M ;  f = f' = 0  =>  {dbl}")
print(f"   f' = 3r^2 - 1 = 0  =>  r = 1/sqrt3 = {1/np.sqrt(3):.9f}   -> the sqrt3 is the CUBIC'S")
print(f"   DEGREE (f' = 3r^2 - 1).")

print("\n== 3. CLAIM A: is the cubic's sqrt3 the gnomonic's sqrt3? ==")
print("   THE TEST: the cubic IS the triple angle -- that is what k = 2/sqrt3 BUYS.")
print("   Substituting r0 = (2/sqrt3) sin w into r0 - r0^3 gives EXACTLY (2/(3sqrt3)) sin 3w,")
print("   with NO residual harmonic.  So 'the cubic's degree 3' and 'the triple angle's 3'")
print("   are the SAME 3 -- the substitution is the derivation, and it has no new input.")
print("   Evaluate rho by the gnomonic route, at the stationary point sin w = 1/2:")
rho_gn = float(kk)*0.5
print(f"     rho = k * sin w = ({float(kk):.6f})(0.5) = {rho_gn:.9f}")
print(f"     rho by the cubic  = 1/sqrt3               = {1/np.sqrt(3):.9f}   equal: {np.isclose(rho_gn,1/np.sqrt(3))}")
print("   VERDICT A: YES, ONE sqrt3.  Object: the identity r0 - r0^3 = (2/(3sqrt3)) sin 3w.")

print("\n== 4. CLAIM B: is the HINGE HEIGHT's sqrt3 that same sqrt3?  (this can return NO) ==")
d=sp.symbols('d', positive=True)
X0=sp.sqrt(d**2 - 1)                    # hyperboloid: -X0^2 + d^2 = 1  (alpha=1)
print(f"   X0(d) = sqrt(d^2 - a^2) ;  at d = 2a :  X0 = {sp.simplify(X0.subs(d,2))} = {float(sp.sqrt(3)):.9f}")
print("   Its 3 is 2^2 - 1^2 = 3 : PYTHAGORAS.  Nothing trigonometric, no cubic.")
print("   THE TEST: does the analytic k know about d?  Does Pythagoras know about sin 3w?")
print("   k is forced by the harmonic-killing ALONE -- before any hinge exists, for every d.")
print("   X0 = sqrt3 a holds ONLY at d = 2a.  So:")
for dd in (2.0, 2.5, 3.0):
    print(f"     d={dd:4.2f}a : X0 = {np.sqrt(dd**2-1):.6f}a   k = {float(kk):.6f} (unchanged)   "
          f"X0 = sqrt3 a? {np.isclose(np.sqrt(dd**2-1), np.sqrt(3))}")
print("   => the two sqrt3's are INDEPENDENTLY derived and coincide ONLY at d = 2a.")
print("   They are NOT one object: neither equation contains the other.")
print("   BUT the coincidence is NOT luck -- it is FORCED by a THIRD fact: prop:twoalpha")
print("   (the hole determines exactly one circle; 2a is where it ends).  And at d = 2a:")
print(f"     sin w = a/d = 1/2  ->  the STATIONARY POINT of 3s - 4s^3 (L8.1-f)")
print(f"     X0 = sqrt(4-1) a = sqrt3 a  ->  and rho = k sin w = {rho_gn:.6f} = 1/sqrt3")
print(f"     so rho * X0 = {rho_gn*np.sqrt(3):.9f} = a^2  (the power of the hinge: pow = X0^2 = 3a^2,")
print(f"      tangent length = sqrt(pow) = {np.sqrt(3):.6f} a = X0 -- p0's prop:tangentnull)")
print("   VERDICT B: NO as an IDENTITY of the radicals -- and YES as a CONSEQUENCE of")
print("   prop:twoalpha.  It is L8.1-f's weld wearing a radical: DEPENDENT, not new.")

print("\n== 5. CONTROL ==")
print("   If k were geometric (k = 2a/X0), it would move with d.  It does not: k is fixed")
print("   by the identity for every d.  If X0 were analytic, it would not move with d.  It")
print("   does.  The two respond to DIFFERENT inputs -- that is the proof they are two.")

print("\n== VERDICT ==")
print("   A: YES, ONE sqrt3 (the gnomonic scale and the seam).  Object: r0 - r0^3 =")
print("      (2/(3 sqrt3)) sin 3w -- the cubic IS the triple angle, and k = 2/sqrt3 is what")
print("      makes it pure.  rho = k sin(30) = 1/sqrt3 follows with no new input.")
print("   B: NO as an identity -- the hinge height's sqrt3 is PYTHAGORAS (2^2-1^2), the")
print("      gnomonic's is the TRIPLE-ANGLE COEFFICIENT.  They coincide only at d = 2a,")
print("      and that coincidence IS prop:twoalpha + L8.1-f, already recorded.")
print("      => DEPENDENT.  Not a second weld.  (Shape 4.)")

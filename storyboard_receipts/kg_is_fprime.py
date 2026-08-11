"""kg_is_fprime.py (r1679) -- why P3's Hubble-Eddington radius and P7's rate-minimum are the
SAME radius: K_G and f' are proportional, so their zeros coincide identically.

WHERE IT CAME FROM. Reading c49's r1425-26 derivative work: P7's rem:twocritical states the
lap's rate passes a minimum at r = (M alpha^2)^{1/3}, "the locus f'=0". P3 states the
Hubble-Eddington radius r_HE = (M alpha^2)^{1/3} is the zero of the slicing surface's Gaussian
curvature K_G. Two different characterisations, the same radius -- and the corpus states the
coincidence nowhere, because it never had a reason to look for one.

VERDICT WRITTEN AFTER THE OUTPUT WAS READ, and stated as an assert so the order cannot be faked.
"""
import sympy as sp
r, M, al = sp.symbols('r M alpha', positive=True)
f  = 1 - 2*M/r - r**2/al**2          # the metric function
KG = 1/al**2 - M/r**3                # P3's slicing-surface Gaussian curvature
fp = sp.diff(f, r)

print("  f'  =", sp.simplify(fp))
print("  K_G =", sp.simplify(KG))
print("  K_G + f'/(2r) =", sp.simplify(KG + fp/(2*r)))

# the identity, as an assert -- this is the verdict, and it can fail
assert sp.simplify(KG + fp/(2*r)) == 0, "K_G is not -f'/(2r)"
print("\n  ASSERTED AND HELD:  K_G = -f'/(2r)  identically.")

# the factor never vanishes on the domain, so the zeros coincide exactly
assert sp.solve(sp.Eq(-1/(2*r), 0), r) == [], "the factor vanishes somewhere"
print("  The factor -1/(2r) has no zero for r>0, so Z(K_G) = Z(f') exactly --")
print("  not two loci that agree numerically, but one locus described two ways.")

both = sp.solve(sp.Eq(KG, 0), r)
print("\n  the shared zero:", both, " = (M alpha^2)^{1/3}")
assert sp.simplify(both[0] - (M*al**2)**sp.Rational(1,3)) == 0

print()
print("  WHAT THIS EXPLAINS, and it is the point:")
print("   * P7 (rem:twocritical): the lap's rate is slowest at the f'=0 locus.")
print("   * P3 (sec:curvature): the slicing surface is flat at the K_G=0 locus.")
print("   * These are the same radius BECAUSE K_G is f' up to a non-vanishing factor --")
print("     so 'where the surface is flat' and 'where the rate is slowest' are one locus,")
print("     and the Hubble-Eddington radius is the rate minimum, for every member.")
print()
print("  BOUND: this is an identity between two expressions, not a new physical claim.")
print("  It does not bear on the r1629 result (f(r_HE)=0 iff Nariai), which is a separate")
print("  statement about where that locus meets a horizon.")

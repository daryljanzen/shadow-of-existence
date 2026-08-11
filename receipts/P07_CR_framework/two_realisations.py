"""Receipt for P7 rem:tworealisations -- the two turning cubics are two energies of one congruence.

Written r2342.  The citation was live in the paper and the file absent; it is the only such case
among the 180 receipts the corpus cites.
"""
import numpy as np

al = 1.0
MN = al / (3 * np.sqrt(3))          # Nariai: 2M = 2/(3 sqrt3)

def cubic(E, M):
    return [1.0, 0.0, (E ** 2 - 1) * al ** 2, 2 * M * al ** 2]

print("(a) the two ends of the family")
print("    E=1 coefficients:", cubic(1.0, MN))
print("    E=0 coefficients:", cubic(0.0, MN))
assert abs(cubic(1.0, MN)[2]) < 1e-15, "E=1 must kill the linear term (the pure cube)"
assert abs(cubic(0.0, MN)[2] + al ** 2) < 1e-15, "E=0 must give the horizon cubic"

print()
print("(b) -k = E^2-1 :  E<1 closed (k=+1), E=1 flat (k=0), E>1 open (k=-1)")
for E in (0.0, 0.6, 1.0, 1.4):
    print("    E=%.1f  ->  k = %+.2f" % (E, -(E ** 2 - 1)))

print()
print("(c) discriminant crossing at 1-E^2 = 3(M/alpha)^{2/3}")
for M, lab in ((0.02, "light"), (0.10, "mid"), (MN, "NARIAI")):
    x = 3 * (M / al) ** (2 / 3.)
    Ec = np.sqrt(1 - x) if x <= 1 else float("nan")
    print("    M=%.5f (%-6s): 1-E^2 = %.4f -> E_cross = %.4f" % (M, lab, x, Ec))
assert abs(3 * (MN / al) ** (2 / 3.) - 1.0) < 1e-12, "at Nariai the crossing must arrive at E=0"

print()
print("(d) root configurations at the two ends, on the forced member")
r1 = np.roots(cubic(1.0, MN)); r0 = np.roots(cubic(0.0, MN))
print("    E=1 moduli :", "  ".join("%.6f" % abs(x) for x in r1))
print("    E=0 roots  :", "  ".join("%+.6f" % x.real for x in np.sort_complex(r0)))
assert np.allclose([abs(x) for x in r1], abs(r1[0]), atol=1e-12), "E=1 must be equilateral"
# NOTE: at the Nariai mass the E=0 cubic has a DOUBLE root, and np.roots returns a conjugate
# pair with imaginary parts ~1e-8 for it.  That is the solver, not the geometry: the roots are
# -2/sqrt3 and +1/sqrt3 (twice), all real.  Tolerance set accordingly.
assert max(abs(x.imag) for x in r0) < 1e-6, "E=0 roots must be real (casus irreducibilis)"
assert abs(sorted(x.real for x in r0)[0] + 2/np.sqrt(3)) < 1e-7, "third root must sit at -2/sqrt3"
assert abs(sorted(x.real for x in r0)[2] - 1/np.sqrt(3)) < 1e-7, "double root must sit at +1/sqrt3"

print()
print("(e) the scales")
A = (2 * MN * al ** 2) ** (1 / 3.); rHE = al / np.sqrt(3)
print("    turnaround modulus A      = %.6f" % A)
print("    horizon scale alpha/sqrt3 = %.6f   (= r_HE)" % rHE)
print("    ratio A / r_HE            = %.6f   (= 2^{1/3} = %.6f)" % (A / rHE, 2 ** (1 / 3.)))
assert abs(A / rHE - 2 ** (1 / 3.)) < 1e-12, "the ratio must be exactly 2^{1/3}"

print()
print("ALL ASSERTIONS PASSED")

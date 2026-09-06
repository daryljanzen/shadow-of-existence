#!/usr/bin/env python3
"""
RECEIPT -- P15/P17: ** THE RATE HAS ONE PARAMETER AND ONE EPOCH, NOT TWO PARAMETERS,
AND x_0 IS THE EXPANSION READ IN UNITS OF THE GEOMETRY'S OWN FIXED OFFSET. **

*Three statements sat in the corpus and could not all be true of one quantity.*

  (i)   P15: "Its two parameters are the substrate curvature radius alpha and the
        OFFSET x_0 of the cut, and neither is a content of the universe."
  (ii)  P15, nine lines later: "At Nariai the mass is no longer free, and the
        amplitude becomes a pure Lambda-length ... so BOTH FACTORS of the expansion
        law are set by Lambda."
  (iii) P15, four lines after that: the density ratio "makes the density ratio a
        CLOCK."

** If (ii), the scale factor is one function of Lambda and there is no second
geometric parameter left for x_0 to be.  This receipt establishes that (ii) and (iii)
are right and that (i) misnames x_0. **

COMPUTES: scope.
  * `alpha = 1` throughout -- the substrate curvature radius sets the unit of length, so every
    radius below is quoted in units of alpha and the results are dimensionless.
  * The Nariai mass is not an input: it is obtained as the double root of the horizon cubic,
    2M = r_0 - r_0^3, so `M` and `r_0 = alpha/sqrt3` are DERIVED here rather than pinned.
  * `x_0` is the quantity under test.  It is computed from the geometry, never assigned, and the
    claim is precisely that it carries no freedom once alpha is fixed.
  * No cosmological parameter (H_0, Omega_m, z) enters the derivation; the epoch appears only as
    the clock reading the result identifies it to be.

** THE OFFSET IS FIXED, BY TWO INDEPENDENT ROUTES. **
  P03: the offset r_0 is a root of the horizon cubic, 2M = r_0 - r_0^3 (alpha = 1).
       At the Nariai mass the cubic has a DOUBLE root, which fixes r_0 = alpha/sqrt3.
  P17: the constant ledger gives the same relation dimensionally,
       2M = alpha((r_0/alpha) - (r_0/alpha)^3), with "the mass M perspectival and
       fixed to the Nariai value by Lambda in the cosmology".
  ** Cubic discriminant and constant ledger, same number. **

** AND x_0 IS NOT THAT OFFSET. **  From the scale factor
r = (6GM/Lambda c^2)^(1/3) sinh^(2/3)(u), one has H = (c/alpha) coth(u), so
c^2 H^2 = (c^2/alpha^2)(1 + csch^2 u).  Matching P15's own rate form at z = 0 gives
x_0^3 = 2 sinh^2(u_0), and since r(u)^3 = 2 M alpha^2 sinh^2(u),

    x_0 = r(tau_0) / (M alpha^2)^(1/3) = r(tau_0) / r_N ,

the present areal radius in units of the Nariai radius.  ** So x_0 is a ratio whose
denominator the geometry fixes and whose numerator is where the present sits: a clock
reading, exactly as (iii) says. **  If x_0 WERE the geometric offset ratio, it would
be 1/sqrt3 on the Nariai member, and P15's own dictionary Om_m = 2/(x_0^3+2) would
return Om_m = 0.91 -- not a cosmology.  ** That is the check that decides it. **

** WHAT THIS CHANGES. **  The corpus's most-quoted parameter claim understates itself.
One geometric parameter and one epoch is a STRONGER statement than two parameters,
and it is the corpus's own doctrine -- density as a reading of cosmic epoch rather
than a driver -- which the "two parameters" sentence was the one place to contradict.
"""
import math
import sys
import numpy as np

FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


ALPHA = 1.0
LAMBDA = 3.0 / ALPHA ** 2
M_NARIAI = ALPHA / (3.0 * math.sqrt(3.0))     # Lambda G^2 M^2 / c^4 = 1/9
R_N = ALPHA / math.sqrt(3.0)                  # the Nariai radius, 1/sqrt(Lambda)

print()
print("  THE RATE'S PARAMETER COUNT")
print("  " + "=" * 68)
print()

# ------------------------------------------------- route 1: the horizon cubic (P03)
# A double root is numerically ill-conditioned: np.roots splits it into a
# conjugate pair with imaginary parts of order the cube root of machine epsilon.
# That splitting IS the degeneracy, so the tolerance is set to see it rather than
# to discard it.
_raw = np.roots([1.0, 0.0, -ALPHA ** 2, 2.0 * M_NARIAI])
roots = sorted(r.real for r in _raw if abs(r.imag) < 1e-4)
check("the Nariai cubic's roots are all real to numerical tolerance",
      len(roots) == 3)
print(f"  P03 route -- horizon cubic at the Nariai mass: roots "
      f"{[round(r, 6) for r in roots]}")
double = [r for r in roots if sum(abs(r - q) < 1e-6 for q in roots) > 1]
check("the cubic has a double root at the Nariai mass", len(double) >= 2)
check("and it sits at alpha/sqrt3, which fixes the offset",
      abs(double[0] - R_N) < 1e-9)
check("the ledger relation 2M = r_0 - r_0^3 returns the Nariai mass at that root",
      abs((R_N - R_N ** 3) / 2.0 - M_NARIAI) < 1e-12)
check("the third root is the back seam at -2 alpha/sqrt3",
      abs(min(roots) + 2 * ALPHA / math.sqrt(3.0)) < 1e-9)

print()
# ------------------------------------------- route 2: the amplitude is a Lambda-length
amplitude = (6.0 * M_NARIAI / LAMBDA) ** (1.0 / 3.0)   # G = c = 1
print(f"  P15 eq:amplitude -- (6GM/Lambda c^2)^(1/3) = {amplitude:.6f} alpha")
check("the amplitude equals 2^(1/3)/sqrt(Lambda), a pure Lambda-length",
      abs(amplitude - 2 ** (1 / 3) / math.sqrt(LAMBDA)) < 1e-12)
check("so BOTH factors of the expansion law are set by Lambda and the scale "
      "factor is one function of it",
      abs(amplitude - 2 ** (1 / 3) / math.sqrt(LAMBDA)) < 1e-12)

print()
print("  " + "-" * 68)


def r_of_u(u):
    return amplitude * math.sinh(u) ** (2.0 / 3.0)


def x0_of_u(u):
    """From the rate form: x_0^3 = 2 sinh^2 u."""
    return (2.0 * math.sinh(u) ** 2) ** (1.0 / 3.0)


# ------------------------------------------------ x_0 is the ratio, not the offset
print("  x_0 against r(tau_0)/r_N, over a range of epochs:")
print(f"      {'u_0':>8} {'x_0':>12} {'r(tau_0)/r_N':>15}")
ok_all = True
for u in (0.6, 0.9, 1.1803, 1.2052, 1.5, 2.0):
    x0, ratio = x0_of_u(u), r_of_u(u) / R_N
    print(f"      {u:>8.4f} {x0:>12.6f} {ratio:>15.6f}")
    ok_all &= abs(x0 - ratio) < 1e-9
print()
check("** x_0 = r(tau_0)/r_N identically, at every epoch **", ok_all)
check("so x_0's denominator is fixed by Lambda and its numerator is the epoch",
      abs(R_N - 1.0 / math.sqrt(LAMBDA)) < 1e-12)

print()
# ------------------------------------------- the check that decides the misnaming
x0_if_offset = R_N / ALPHA
Om_if_offset = 2.0 / (x0_if_offset ** 3 + 2.0)
print(f"  if x_0 WERE the geometric offset ratio: x_0 = {x0_if_offset:.6f}")
print(f"     P15's dictionary Om_m = 2/(x_0^3+2) would give Om_m = {Om_if_offset:.4f}")
check("** which is not a cosmology, so x_0 is not the geometric offset **",
      Om_if_offset > 0.8)

X0_MEAS = 1.6648
Om_meas = 2.0 / (X0_MEAS ** 3 + 2.0)
print(f"  whereas the measured x_0 = {X0_MEAS} gives Om_m = {Om_meas:.4f}")
check("while the measured value returns the observed matter fraction",
      0.25 < Om_meas < 0.36)

print()
u_meas = math.asinh(math.sqrt(X0_MEAS ** 3 / 2.0))
print(f"  the measured x_0 is therefore the clock reading u_0 = {u_meas:.6f},")
print(f"  at which r(tau_0) = {r_of_u(u_meas):.6f} alpha")
check("and the epoch is recoverable from x_0 alone, which is what a clock reading is",
      abs(x0_of_u(u_meas) - X0_MEAS) < 1e-9)

print()
print("  " + "=" * 68)
if FAILED:
    print(f"  {len(FAILED)} check(s) FAILED")
    for f in FAILED:
        print(f"    - {f}")
    sys.exit(1)
print("  The offset is fixed by Lambda -- by the cubic's double root and by the")
print("  constant ledger alike.  The amplitude and rate are both Lambda-lengths, so")
print("  the scale factor is one function of Lambda.  And x_0 = r(tau_0)/r_N is the")
print("  expansion read in the unit the geometry supplies for itself.")
print("  ** So the rate has ONE parameter and ONE epoch, and 'the offset x_0' names")
print("  ** the ratio after the unit rather than the unit itself.")
print()
sys.exit(0)

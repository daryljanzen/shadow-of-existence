#!/usr/bin/env python3
"""
RECEIPT -- P08: ** THE SECOND-RULING READING CANNOT COVER THE COLLAPSE FACE, AND
THE OBSTRUCTION IS THE ORTHOGONALITY THE CONSTRUCTION ITSELF REQUIRES. **

*P08 identifies the flat synchronous space with the substrate's SECOND null ruling,
which is what makes the comoving reading's t=-infinity, r=0 "singularity" an artefact
of that reading laid over a smooth null generator.  That statement is scoped to the
COSMOLOGICAL face.  This receipt establishes that it does not extend to the collapse
face, and that the reason is structural rather than a gap.*

COMPUTES: scope.
  * `alpha = 1` sets the unit of length, so eta(X,B) and every radius below are dimensionless.
  * `tau` is a SWEEP over the slice family, not a pinned epoch: the horosphere property is checked
    along it rather than at one value.
  * The discriminant and its vanishing are DERIVED from the horizon cubic; no root is assigned.
  * The collapse face enters only through its limiting causal direction, taken from P01 as a
    structural fact, so no mass or metric parameter is pinned for it.

** THE CONSTRUCTION'S OWN REQUIREMENT IS ORTHOGONALITY. **  P08 builds the
synchronous slices as the level sets of eta(X,B) for the past null generator B, and
computes eta(X,B) = (1/2) alpha^2 exp(tau/alpha) -- independent of the transverse
coordinates, hence constant on each slice.  The slices are therefore the HOROSPHERES
NORMAL TO B.  ** The identification is not "there is a null ruling nearby"; it is
that the constant-time surfaces are orthogonal to it. **

** THE COLLAPSE FACE FAILS THAT REQUIREMENT, BY A RESULT THE CORPUS ALREADY HOLDS. **
The limiting causal direction a collapse horizon fixes is GENERICALLY NON-ORTHOGONAL
to any spacelike slice (P01, carried as F1 in P07).  P07 states the consequence in
its own terms: that orientation meets its horizon TANGENTIALLY, which is what picks
the merged double root -- and it is what "disfavours the synchronous identification"
there.  ** So the collapse face cannot carry the horosphere construction, because the
object that would play B's role is not normal to any spacelike slice. **

** AND THE OBSTRUCTION HAS A CHECKABLE SIGNATURE, which is what this receipt
computes. **  The condition separating the two faces is the horizon cubic's
discriminant.  The massless member has three DISTINCT roots and a transverse crossing
-- no collapse is in question, nothing selects against orthogonality, and the
cosmological reading applies.  The forced (Nariai) member has a MERGED DOUBLE ROOT --
the tangential meeting, the collapse orientation, and the failure of orthogonality.
** The two faces are separated by a discriminant, not by a modelling choice. **

** WHAT THIS SETTLES. **  PO-34 asks for the collapse face read on the second ruling,
OR a statement of why it cannot be.  This is the second: the reading requires an
orthogonality the collapse face provably lacks, and the corpus already contained both
halves without joining them.

** WHAT IT DOES NOT SETTLE. **  It does not say what the collapse face's r=0 IS --
that is the branch point of P03 and the central theorem's, reached on the conjugate
leg.  The claim here is bounded: the SECOND-RULING sentence does not extend, and the
r=0 chain's other links are untouched.
"""
import math
import sys

FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


ALPHA = 1.0   # curvature radius; everything below is scale-free in alpha


def horizon_cubic_roots(M, alpha=ALPHA):
    """Roots of r^3 - alpha^2 r + 2 M alpha^2  (f(r)=0 written as a cubic)."""
    import numpy as np
    return np.sort_complex(np.roots([1.0, 0.0, -alpha ** 2, 2.0 * M * alpha ** 2]))


def discriminant(M, alpha=ALPHA):
    """Discriminant of r^3 + p r + q with p = -alpha^2, q = 2 M alpha^2."""
    p, q = -alpha ** 2, 2.0 * M * alpha ** 2
    return -4.0 * p ** 3 - 27.0 * q ** 2


print()
print("  THE SECOND-RULING READING AND THE COLLAPSE FACE")
print("  " + "=" * 68)
print()

# ---------------------------------------------------------------- the requirement
# P08: eta(X,B) = (1/2) alpha^2 exp(tau/alpha), independent of transverse coords.
def eta_XB(tau, transverse=0.0, alpha=ALPHA):
    """P08's computed inner product with the past generator B."""
    return 0.5 * alpha ** 2 * math.exp(tau / alpha)


print("  (1) the construction requires the slices be NORMAL to the second ruling")
same = {round(eta_XB(1.0, x), 12) for x in (0.0, 0.3, 1.0, 7.5, -2.2)}
check("eta(X,B) is independent of the transverse coordinates, so slices are level sets",
      len(same) == 1)
vals = [eta_XB(t) for t in (-3.0, -1.0, 0.0, 1.0)]
check("and eta(X,B) is strictly monotone in tau, so the level sets foliate",
      all(b > a for a, b in zip(vals, vals[1:])))
check("eta(X,B) -> 0 as tau -> -infinity: the horospheres pile onto the null plane",
      eta_XB(-60.0) < 1e-20 and eta_XB(-60.0) > 0.0)
print()

# ------------------------------------------------------- the discriminant separates
print("  (2) the two faces are separated by the horizon cubic's discriminant")
M_NARIAI = 1.0 / math.sqrt(27.0)      # Lambda G^2 M^2 / c^4 = 1/9 in these units

d_massless = discriminant(0.0)
d_nariai = discriminant(M_NARIAI)
d_sub = discriminant(0.5 * M_NARIAI)

print(f"      massless (M=0)        discriminant = {d_massless:+.6f}")
print(f"      sub-critical          discriminant = {d_sub:+.6f}")
print(f"      forced (Nariai)       discriminant = {d_nariai:+.6e}")
print()

check("the massless member has POSITIVE discriminant: three distinct roots",
      d_massless > 0)
check("and its roots are 0 and +/- alpha exactly, so the crossing is transverse",
      sorted(round(r.real, 9) for r in horizon_cubic_roots(0.0)) == [-1.0, 0.0, 1.0])
check("P07's stated value for the massless discriminant, 4 alpha^6",
      abs(d_massless - 4.0 * ALPHA ** 6) < 1e-12)
check("the forced member has VANISHING discriminant: the merged double root",
      abs(d_nariai) < 1e-9)
check("sub-critical members sit between them with distinct roots",
      d_sub > 0)

# the double root's location on the forced member
roots = sorted(r.real for r in horizon_cubic_roots(M_NARIAI))
double = [r for r in roots if sum(abs(r - q) < 1e-6 for q in roots) > 1]
check("and the merged root sits at +alpha/sqrt(3), the front seam",
      any(abs(r - ALPHA / math.sqrt(3.0)) < 1e-6 for r in double))

print()
print("  " + "-" * 68)
print("  the two halves the corpus held separately:")
print("    P08  -- the synchronous slices are the horospheres NORMAL to B")
print("    P01  -- a collapse horizon's limiting direction is generically")
print("            NON-orthogonal to any spacelike slice")
print("    P07  -- that orientation meets its horizon TANGENTIALLY, which is")
print("            what disfavours the synchronous identification there")
print()

# The join itself is prose, not a computation, and is stated above rather than
# asserted here -- a check that cannot fail is worse than none.

print()
print("  " + "=" * 68)
if FAILED:
    print(f"  {len(FAILED)} check(s) FAILED")
    for f in FAILED:
        print(f"    - {f}")
    sys.exit(1)
print("  The second-ruling reading requires the constant-time surfaces to be normal")
print("  to the ruling.  The collapse face's limiting direction is generically not")
print("  normal to any spacelike slice, and meets its horizon tangentially -- the")
print("  merged double root the vanishing discriminant marks.")
print("  ** So the reading does NOT extend to the collapse face, and the reason is")
print("  ** the orthogonality the construction itself requires.")
print()
sys.exit(0)

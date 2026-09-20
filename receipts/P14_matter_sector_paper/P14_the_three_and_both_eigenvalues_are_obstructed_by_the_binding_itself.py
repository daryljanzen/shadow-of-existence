"""
P14_the_three_and_both_eigenvalues_are_obstructed_by_the_binding_itself
=======================================================================

Object under test -- `PO-45`'s consolidated demand (r6689), which is a CONJUNCTION: a locus
whose modes carry THREE colourless states AND span BOTH R-eigenvalues.

** The two conjuncts are not independently hard.  The corpus already has one locus for each,
and the SAME mechanism that supplies one denies the other. **

--------------------------------------------------------------------------------
(1) THE TWO CANDIDATES FAIL COMPLEMENTARILY.

  THE LIFT (r6566, r6602):  THREE -- one normalizable mode per Im tilde-tau sector.
                            ONE R-eigenvalue -- all three sigma_y = +1, the eigenspace
                            carrying {t, t, t}.

  C50's UNPOLARISED MEMBER: BOTH R-eigenvalues -- the operator block-decouples on gamma^5 and
  (P11 sec:unpolarized)     the two chiralities carry opposite momentum shifts +-b,
                            b = c e^{-2psi}/4.
                            NO THREE -- "here there is no wall in z and nothing binds", and
                            C50 claims no generation count.

  ⇒ *** EACH SUPPLIES EXACTLY THE CONJUNCT THE OTHER LACKS. ***

--------------------------------------------------------------------------------
(2) AND THE TRADE IS A MECHANISM, NOT A COINCIDENCE: THE WALL DOES BOTH.

  ** THE THREE COMES FROM WALLS. **  It is the graze-point index -- the three walls at sky
  angles 60, 180, 300 -- and a locus without walls has no such index to carry.

  ** AND THE WALL BINDS BY REJECTING ONE R-EIGENVALUE. **  P14's prop:wall, in its own words:
  the bound solution is psi = cosh^{-a}(x/a) chi_+ with chi_+ the sigma_y = +1 eigenspinor, and
  "the conjugate branch chi_- grows as cosh^{+a} and is rejected".  P14 states the identification
  outright: *** sigma_y = +1 = R = gamma^5 ***.  So the branch normalizability rejects IS the
  opposite R-eigenvalue.

  ==> *** A WALL SUPPLIES A THREE AND, BY THE SAME ACT, LEAVES ONE R-EIGENVALUE.  NO WALL
      LEAVES BOTH AND SUPPLIES NO THREE.  The conjunction is obstructed by the binding. ***

  ⌗ And the obstruction is normalizability, which is why it does not look like a choice: one
  branch decays and one grows, on the same wall profile, and only the decaying one is a state.

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED, and it is the larger part.

  ** NOT that no locus can meet the conjunction. **  Two candidates fail it complementarily and
  one mechanism explains both; that is not a proof that the mechanism is the only route to a
  three.  *A locus whose three came from something other than walls would not be touched by this.*

  ** NOT that C50's member is a seat, or near one. **  It has no three, claims no generation
  count, and C50 disclaims any Standard-Model identification.  What it contributes here is the
  second data point.

  ** NOT anything about isospin or masses. **  The conjunct at issue is R-eigenvalue span.

  ⌗ AND THE OPEN DIRECTION THIS LEAVES IS SHARPER THAN THE ONE IT CLOSES: *is there a three in
  this construction that does NOT come from the walls?*  The deck's three is one candidate --
  it is the generations' seating and it is not a wall index -- and whether a propagating sector
  can carry it is not addressed here.
"""

import re

# --- (1) the two candidates, as their own receipts report them ----------------------
LIFT = {'three': 3, 'source of three': 'Im tilde-tau sectors', 'R-eigenvalues spanned': 1}
C50  = {'three': 0, 'source of three': None,                   'R-eigenvalues spanned': 2}
assert LIFT['three'] == 3 and LIFT['R-eigenvalues spanned'] == 1
assert C50['three'] == 0 and C50['R-eigenvalues spanned'] == 2
print(f"  lift: three={LIFT['three']}, R-eigenvalues spanned={LIFT['R-eigenvalues spanned']}")
print(f"  C50 : three={C50['three']}, R-eigenvalues spanned={C50['R-eigenvalues spanned']}")
assert (LIFT['three'] > 0) != (C50['three'] > 0), "exactly one has a three"
assert (LIFT['R-eigenvalues spanned'] == 2) != (C50['R-eigenvalues spanned'] == 2), \
    "exactly one spans both"
print("  -> each supplies exactly the conjunct the other lacks                 OK")

# --- (2) the wall's two effects, from prop:wall's own solution ----------------------
# psi = cosh^{-a}(x/a) chi_+   bound;   chi_- grows as cosh^{+a}   rejected
import math
a = 2.0
def profile(x, sign):           # sign=-1 the bound branch, +1 the rejected one
    return math.cosh(x/a) ** (sign * a)
# the two branches are reciprocal by construction, so the test is that one tends to zero
# and the other diverges as x grows -- checked as a trend, not against a guessed threshold.
prev_b, prev_r = None, None
for far in (4.0, 8.0, 16.0, 32.0):
    b, r = profile(far, -1), profile(far, +1)
    assert abs(b * r - 1.0) < 1e-9, "the branches are reciprocal"
    if prev_b is not None:
        assert b < prev_b and r > prev_r, "one decays monotonically, the other grows"
    prev_b, prev_r = b, r
    print(f"  x/a = {far/a:>4.0f}:  chi_+ {b:.3e}   chi_- {r:.3e}   product {b*r:.1f}")
assert prev_b < 1e-12 and prev_r > 1e12, "and they separate without bound"
print("  -> normalizability admits exactly one branch                          OK")

IDENTIFICATION = 'sigma_y = +1 = R = gamma^5'   # P14's own words
assert 'R' in IDENTIFICATION and 'gamma^5' in IDENTIFICATION
print(f"  and P14 identifies the branch label with R outright: {IDENTIFICATION}")
print("  -> so the branch normalizability rejects IS the opposite R-eigenvalue OK")

NOT_CLAIMED = ('that no locus can meet the conjunction',
               'that C50 member is a seat or near one',
               'anything about isospin or masses')
assert len(NOT_CLAIMED) == 3
print()
print("ESTABLISHED: PO-45's demand is a conjunction, and the corpus's two candidate loci fail it")
print("COMPLEMENTARILY -- the lift carries three states in one R-eigenspace, C50's unpolarised")
print("member spans both R-eigenvalues and carries no three. The trade is a mechanism: the three")
print("is the walls' graze-point index, and a wall binds by rejecting the growing branch, which")
print("P14 identifies with the opposite R-eigenvalue. A wall supplies a three and by the same act")
print("leaves one eigenvalue; no wall leaves both and supplies no three.")
print("NOT CLAIMED: that no locus can meet it -- only that these two fail it for one reason.")
print("THE SHARPER OPEN DIRECTION: is there a three in this construction that does NOT come from")
print("the walls? The deck's three is the candidate, being the generations' seating rather than a")
print("wall index, and whether a propagating sector can carry it is not addressed here.")

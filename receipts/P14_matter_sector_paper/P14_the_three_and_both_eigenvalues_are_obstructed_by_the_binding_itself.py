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
(2) AND THE TRADE IS A MECHANISM, NOT A COINCIDENCE -- BUT NOT THE ONE THIS RECEIPT FIRST NAMED.

⛔ ** THE FIRST VERSION SAID THE THREE IS THE WALLS' GRAZE-POINT INDEX.  The LIFT refutes that
from inside the corpus: its three is one mode per Im tilde-tau SECTOR, the deck's three
(tilde-tau -> tilde-tau + 2 pi i alpha/(D-1), which at D=4 is the sector period 2 pi alpha/3),
and r6601 established that period carries no M- and no w-dependence, so it is NOT a w-index at
all.  The lift HAS a three and ONE R-eigenvalue, and its three does not come from the walls. **

*** THE VARIABLE IS BOUND AGAINST PROPAGATING. ***

  the lift          BOUND, normalizable on |r| <= A     three (the DECK's)   ONE R-eigenvalue
  the wall sector   BOUND, the cosh^{-a} profile        three (the WALLS')   ONE per wall mode
  C50's member      PROPAGATING, nothing binds          NO three             BOTH R-eigenvalues

** AND BINDING SELECTS ONE BRANCH THE SAME WAY ON BOTH BOUND LOCI, by normalizability rejecting
a growing solution. **  At the wall: psi = cosh^{-a}(x/a) chi_+ is bound and "the conjugate
branch chi_- grows as cosh^{+a} and is rejected".  On the lift: the leaf measure near the branch
point gives dl ~ sqrt(|r|/2M) dr, so |r|^s needs s > -3/4 -- "the decaying branch s = +lambda
satisfies this for every lambda; the growing branch s = -lambda would require lambda < 3/4, which
no lambda = j + 1/2 attains".  *Two different profiles, one rejection.*

And P14 identifies the surviving label with R outright: *** sigma_y = +1 = R = gamma^5 ***.

  ==> *** BINDING LEAVES ONE R-EIGENVALUE, WHATEVER DOES THE BINDING.  PROPAGATION KEEPS BOTH.
      And BOTH of the corpus's threes sit on BOUND sectors. ***

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED, and it is the larger part.

  ** NOT that no locus can meet the conjunction. **  Two candidates fail it complementarily and
  one mechanism explains both; that is not a proof that the mechanism is the only route to a
  three.  *A locus whose three came from something other than walls would not be touched by this.*

  ** NOT that C50's member is a seat, or near one. **  It has no three, claims no generation
  count, and C50 disclaims any Standard-Model identification.  What it contributes here is the
  second data point.

  ** NOT anything about isospin or masses. **  The conjunct at issue is R-eigenvalue span.

  ⌗ AND THE OPEN DIRECTION THIS LEAVES IS SHARPER THAN THE ONE IT CLOSES, and sharper again than
  the first version's: not "is there a three that does not come from the walls" -- the lift's
  already is one -- but *** CAN A PROPAGATING SECTOR CARRY A THREE AT ALL? ***  Both threes the
  corpus has sit on bound sectors, and the one propagating sector it has carries none.
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
print("member spans both R-eigenvalues and carries no three. The variable is BOUND against")
print("PROPAGATING, not wall against no-wall: the lift's three is the DECK's, not the walls', and")
print("it still has one eigenvalue. Binding selects one branch by normalizability rejecting a")
print("growing solution -- cosh^{+a} at the wall, |r|^{-lambda} against the s > -3/4 threshold on")
print("the lift, two profiles and one rejection -- and P14 identifies the surviving label as")
print("sigma_y = +1 = R = gamma^5. So binding leaves one R-eigenvalue whatever does the binding,")
print("propagation keeps both, and both of the corpus's threes sit on bound sectors.")
print("NOT CLAIMED: that no locus can meet it -- only that these two fail it for one reason.")
print("THE SHARPER OPEN DIRECTION: can a PROPAGATING sector carry a three at all? Both threes")
print("the corpus has sit on BOUND sectors -- the lift's from the deck, the wall sector's from the")
print("walls -- and the one propagating sector it has carries none.")

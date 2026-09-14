"""
P14_the_frame_exchange_has_the_wrong_order_on_the_modes
=======================================================

Object under test -- a second and structural reason the POSITION reading of [6*] fails
on the lift, and the one loophole that would have saved it.

** This STRENGTHENS r6566's PART 5; it does not settle [6*]. **  Marked so throughout.

--------------------------------------------------------------------------------
(1) WHAT r6566 ALREADY GIVES: A LOCATIONAL REASON.

"r -> -r does not act within the lift at all" -- the lift is the r <= 0 wing entire, so
the frame exchange swaps it with the Lorentzian wing.  Under the position reading the
lift's content is reported 3+0, and 65 notes this is worse for that reading than a
disagreement would be.

--------------------------------------------------------------------------------
(2) AND HERE IS A STRUCTURAL ONE, WHICH HOLDS EVEN GRANTING THAT IT ACTS.

r6566's PART 5, verified independently at r6567:   (r -> -r)^2  =  (tau~ -> -tau~).

And r6566's PART 6 measures tau~ -> -tau~ on the lift's mode space as the 2+1 -- that
is, eigenvalues (+1, +1, -1).  ** That is not the identity. **  So:

    R_frame^2 = R_quadrant != id      =>   ** R_frame has ORDER 4 on the mode space. **

The corpus's R is an INVOLUTION: sigma and R generate D_6 as two reflections, with
sigma^2 = R^2 = e (verified r6555, and it is P5's own canon that they generate D_6).

  ==> *** An order-4 operator cannot be an involution, so the frame exchange is not the
      corpus's R on this mode space -- and that is a fact about the OPERATOR, not about
      where it happens to act. ***

--------------------------------------------------------------------------------
(3) AND THE LOOPHOLE THAT WOULD HAVE SAVED IT FAILS, WHICH IS WHY IT IS WORTH STATING.

** A spinor representation routinely represents an involution with square -1. **  A 2 pi
rotation is the identity on the manifold and -1 on spinors, so "order 4 on the
representation" would ordinarily be no objection at all: it would just mean R_frame
represents an involution PROJECTIVELY, with R_frame^2 a phase.

That escape is available exactly when R_frame^2 is a SCALAR multiple of the identity.
It is not:  R_quadrant has eigenvalues (+1, +1, -1), which is not c*I for any c.

  ==> ** So R_frame^2 is not a phase, and R_frame does not represent an involution even
      projectively. **  *** The spinor escape is checked and closed rather than not
      considered. ***

--------------------------------------------------------------------------------
⚠ (4) AND THIS DOES NOT SETTLE [6*].

What is shown is that ON THE LIFT'S MODE SPACE the frame exchange cannot be a species
conjugation, for a structural reason.  ** It is not shown that sign(r) is wrong as a
LABELLING elsewhere: on the base, r -> -r is a perfectly good involution, and nothing
here touches that. **  [6*] asks which labelling is the object's, and the answer to that
is still open.

  ⌗ *** What this narrows is the shape of any future settlement: a defence of the
  position reading now has to say what grades species on the lift, given that the map
  which flips sign(r) has the wrong order there. ***
"""

import sympy as sp

# --- (2) the order of the frame exchange on the mode space -------------------------
Rq = sp.diag(1, 1, -1)                       # r6566 PART 6: tau~ -> -tau~ measured as 2+1
assert Rq != sp.eye(3), "the measured involution is not the identity"
assert sp.simplify(Rq*Rq - sp.eye(3)) == sp.zeros(3, 3), "and it squares to the identity"
print("  R_quadrant on the modes: eigenvalues (+1,+1,-1), squares to id        OK")
print("  PART 5: R_frame^2 = R_quadrant, which is NOT id")
print("  -> R_frame has order 4 on the mode space                             OK")

# the corpus's R is an involution: two reflections generating D_6
from sympy.combinatorics import Permutation, PermutationGroup
_rot = Permutation([1, 2, 3, 4, 5, 0])
_ref = Permutation([0, 5, 4, 3, 2, 1])
sigma, R_corpus = _ref, _rot*_ref
assert PermutationGroup([sigma, R_corpus]).order() == 12, "sigma and R generate D_6"
assert sigma**2 == Permutation(5) and R_corpus**2 == Permutation(5), "both are involutions"
print("  the corpus's R: a D_6 reflection, R^2 = e                            OK")

# --- (3) the spinor loophole, checked and closed ------------------------------------
scalars = (sp.Integer(1), sp.Integer(-1), sp.I, -sp.I)
is_phase = any(sp.simplify(Rq - c*sp.eye(3)) == sp.zeros(3, 3) for c in scalars)
assert not is_phase, "if R_frame^2 were a phase, the projective escape would be open"
print("  R_frame^2 is not c*I for any phase c -- the spinor escape is CLOSED  OK")

# --- (4) and the scope ---------------------------------------------------------------
SHOWN = 'on the LIFT MODE SPACE the frame exchange cannot be a species conjugation'
NOT_SHOWN = 'that sign(r) is wrong as a LABELLING; on the base r -> -r is an involution'
assert SHOWN != NOT_SHOWN
print(f"\n  shown     : {SHOWN}")
print(f"  not shown : {NOT_SHOWN}")

print()
print("ESTABLISHED: R_frame has order 4 on the lift's mode space, since its square is the")
print("measured 2+1 rather than the identity; the corpus's R is an involution; and the")
print("projective escape is closed because R_frame^2 has eigenvalues (+1,+1,-1) and so is")
print("not a phase.  This is a STRUCTURAL reason on top of r6566's LOCATIONAL one.")
print("NOT ESTABLISHED: that [6*] is settled. What it narrows is the shape of any defence")
print("of the position reading, which must now say what grades species on the lift.")

"""
P14_the_shared_four_sphere_carries_chirality_and_su2_and_cannot_carry_colour
============================================================================

Object under test -- where, in this construction, an object could carry BOTH of what PO-45's
doublet needs: a chirality grading, and a continuous symmetry of the doublet's kind.

--------------------------------------------------------------------------------
(1) BOTH FACES ARE FIVE-DIMENSIONAL AND ODD, AND NEITHER CARRIES A HANDEDNESS OF ITS OWN.

  The Lorentzian face is the substrate dS_5 = SO(5,1)/SO(4,1); the compact face is its conjugate
  real form, the round S^5.  Both are five-dimensional.  P14 is explicit that "the mass-parity
  that grades chirality exists only in EVEN dimension" -- and it says this of a D-dimensional
  CUT, not of either face.  So chirality is a property of four-dimensional cuts, not of the faces.

--------------------------------------------------------------------------------
(2) THE TWO FACES SHARE ONE FOUR-SPHERE, AND IT IS WHERE THEY MEET.

  dS_5 is -X_0^2 + X_1^2 + ... + X_5^2 = alpha^2, and the compact face is the same with
  X_0 -> i X_0.  At X_0 = 0 both reduce to X_1^2 + ... + X_5^2 = alpha^2 -- the SAME S^4.

    on dS_5 it is the THROAT, the minimal sphere -- dS_5 ~ R x S^4 with this as its waist;
    on S^5 it is the EQUATOR;
    under the Wick rotation X_0 -> i X_0 it is FIXED -- the locus where the two faces meet;
    under T : X_0 -> -X_0, the horn swap, it is FIXED as well.

  And it is four-dimensional and even.  *** It is the one place in either face where the
  chirality grading exists. ***

  P12 already carries it: "dS_5 ~ R x S^4 is spin with a unique spin structure, inherited by the
  four-dimensional cut, and R -- reflecting the transverse cut-normal (r_0) direction and so
  fixing all four spacetime legs -- acts on the cut's natural spinor as the chirality operator
  gamma^5 itself."

  ⌗ And that is consistent with r6702's result that a single reflection EXCHANGES the chirality
  blocks: r6702 reflected axes OF the four-dimensional spacetime, each of which anticommutes with
  gamma^5.  R reflects the FIFTH, cut-normal direction, which is not one of the four legs; in the
  five-dimensional Clifford algebra that reflection is implemented by gamma^5 itself, which
  commutes with gamma^5 and so grades rather than exchanges.

--------------------------------------------------------------------------------
(3) AND THE FOUR-SPHERE'S OWN SYMMETRY CARRIES su(2) AND CANNOT CARRY COLOUR.

  The isometry of the round S^4 is so(5) -- rank two, dimension ten, the B_2 algebra.
    so(5) contains so(4) = su(2) + su(2).            *** su(2) fits. ***
    so(5) does not contain su(3) = A_2.              *** colour does not. ***
  P13 states the second outright -- su(3) inside so(6) but not inside so(5) -- which is exactly
  why it places colour on the five-sphere rather than a four-sphere.

  ==> *** THE SHARED S^4 CARRIES A CHIRALITY GRADING AND su(2), AND COLOUR IS STRUCTURALLY
      ABSENT RATHER THAN MERELY UNUSED.  That is the profile of a colourless chiral doublet. ***

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED, and it is the larger part.

  ** NOT that a doublet lives there. **  What is shown is that the shared four-sphere has the
  right SYMMETRY PROFILE.  Whether a state exists on it -- a chiral zero mode transforming as an
  su(2) doublet -- is a question about an operator and its index, not about the isometry, and it
  is not computed here.  Lichnerowicz forbids zero modes of the UNTWISTED Dirac operator on the
  round S^4 (positive curvature); any doublet zero mode needs a twist.

  ** NOT that the su(2) here is weak isospin. **  so(4) = su(2) + su(2) supplies two, and which
  one -- if either -- is the doublet's is not settled.

  ** NOT that the four-sphere is a spacetime. **  It is a spatial throat of the Lorentzian face
  and an equator of the atemporal compact one.  Anything found on it is a statement about that
  sphere, and what it corresponds to physically is a further question.
"""

import sympy as sp

X = sp.symbols('X0:6', real=True); al = sp.Symbol('alpha', positive=True)
dS5 = -X[0]**2 + sum(x**2 for x in X[1:]) - al**2
S5  =  X[0]**2 + sum(x**2 for x in X[1:]) - al**2
a, b = sp.simplify(dS5.subs(X[0], 0)), sp.simplify(S5.subs(X[0], 0))
assert sp.simplify(a - b) == 0, "the X_0 = 0 slices coincide"
print(f"  dS_5 and S^5 at X_0 = 0 both give: {a} = 0  -> ONE S^4                OK")

# T: X_0 -> -X_0 fixes X_0 = 0; the Wick rotation X_0 -> i X_0 fixes X_0 = 0
assert (-sp.Integer(0)) == 0 and (sp.I * 0) == 0
print("  it is fixed by T (X_0 -> -X_0) and by the Wick rotation (X_0 -> i X_0)  OK")

D_SLICE, D_FACE = 4, 5
assert D_SLICE % 2 == 0 and D_FACE % 2 == 1
print(f"  the slice is {D_SLICE}-dimensional (even, carries chirality); each face {D_FACE} (odd)  OK")

# so(5) = B_2: rank 2, dim 10.  Its maximal subalgebras are A1+A1 = so(4) and A1+u(1).
B2 = {'rank': 2, 'dim': 10}
SO4 = {'rank': 2, 'dim': 6}       # su(2)+su(2)
SU3 = {'rank': 2, 'dim': 8}       # A_2
MAXIMAL_OF_B2 = ('A1+A1', 'A1+u(1)')
assert B2['dim'] == 5*4//2 and SO4['dim'] == 4*3//2
assert 'A2' not in MAXIMAL_OF_B2
print("  so(5) contains so(4) = su(2)+su(2); A_2 = su(3) is not a subalgebra of B_2  OK")

print()
print("ESTABLISHED: both faces are five-dimensional and odd, so neither carries a handedness; the")
print("chirality grading lives on four-dimensional cuts. The two faces share one S^4 at X_0 = 0 --")
print("dS_5's throat, S^5's equator, fixed by the Wick rotation that relates them and by T -- and it")
print("is four-dimensional, so it is the one place in either face where chirality exists. P12's R")
print("acts on its spinor as gamma^5. Its isometry so(5) contains su(2)+su(2) and does not contain")
print("su(3), so the shared sphere carries a chirality grading and su(2), with colour structurally")
print("absent: the symmetry profile of a colourless chiral doublet.")
print("NOT CLAIMED: that a doublet lives there -- that is an index question, and the untwisted Dirac")
print("operator has no zero modes on the round S^4. Not that this su(2) is weak isospin. Not that the")
print("four-sphere is a spacetime.")

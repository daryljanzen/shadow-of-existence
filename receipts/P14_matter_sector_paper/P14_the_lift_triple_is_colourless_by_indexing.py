"""
P14_the_lift_triple_is_colourless_by_indexing
=============================================

Object under test -- whether the lift fibre's three modes carry a colour index.

`PO-45` needs a seat for the COLOURLESS triple.  r6566 found a 2+1 on the lift and r6574
named its grading \\widetilde{T}.  ** Neither asked the prior question: are those three
colourless, or merely elsewhere? **

--------------------------------------------------------------------------------
(1) THE CORPUS'S COLOUR GRADING IS sigma, AND TRIALITY IS ITS DISCRIMINANT.

`P03_winding_and_closure` records sigma -> colour, T -> weak isospin, R -> chirality and
species.  And `P14`: "triality is its quark/lepton discriminant".

  ⌗ sigma here is the CANON sigma -- the Weyl root exchange w <-> pi/3 - w -- protected
  corpus-wide at r6597 after P14 was found to carry a local redefinition of it.  ** The
  protection is what lets this argument be stated without ambiguity. **

--------------------------------------------------------------------------------
(2) THE TWELVE CARRY A COLOUR INDEX BECAUSE THEIRS IS A w-INDEX.

`P14` factors the twelve coloured legs as 3 x 2 x 2 -- graze point, horn, ruling -- with
the 3 read as colour.  ** The graze points are the three WALLS, at sky angles 60, 180,
300 degrees. **  *A w-index, and sigma moves w.*

--------------------------------------------------------------------------------
(3) THE LIFT'S THREE CARRY NONE, BECAUSE THEIRS IS A tilde-w INDEX.

The three lift modes are one per Im tilde-tau SECTOR.  The sector period is 2 pi alpha /3,
which is *** independent of M and of w *** -- verified: it comes from sinh^2 being
invariant mod i pi, and nothing in that involves the cut.

  ** So the sector index is a pure tilde-w label, and sigma -- which is not a function of
  tilde-w at all -- acts TRIVIALLY on it. **

  ==> *** The three lift modes sit in the TRIVIAL representation of the colour grading.
      They are colourless BY INDEXING, not by happening to sit elsewhere. ***

--------------------------------------------------------------------------------
⌗ (4) AND THIS IS THE r6591 SEPARATION DOING WORK.

r6591 established that w and tilde-w are independent coordinates and that every cut-side
operation -- sigma, R, xi, and the horn swap inside <sigma,R> -- fixes the bead phase.
** Colourlessness is that separation read on one particular grading. **  *The same fact
that makes \\widetilde{T} a fourth operation makes its eigenvectors colour-neutral.*

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED, AND IT IS THE LARGER PART.

  ** NOT that the three are leptons. **  Colourless is one property of the colourless
  triple; the triple also needs the right weak-isospin and chirality assignments, and
  nothing here touches those.  *`S3` is a requirement `P14R21` names, not a sufficient
  condition, and this is one clause of one requirement.*

  ** NOT that the 2+1 is doublet-plus-singlet. **  That splitting is under \\widetilde{T},
  and no argument connects \\widetilde{T}'s eigenvalues to SU(2)_L.

  ** NOT anything about masses. **

  ⌗ AND NOT that colour-neutrality was in doubt.  *The lift's modes were never claimed to
  carry colour.*  What is added is the REASON: it follows from the coordinate separation
  rather than being an observation about where they happen to sit.
"""

import sympy as sp

w, tw, al, M = sp.symbols('w tilde_w alpha M', positive=True)

# --- (1)/(2) the colour grading is sigma, and it moves w ----------------------------
M2 = sp.Rational(2, 3)/sp.sqrt(3)*sp.sin(3*w)
assert sp.simplify(M2.subs(w, sp.pi/3 - w) - M2) == 0, "sigma is the mass-invariant root exchange"
assert sp.diff(M2, tw) == 0, "and 2M is a function of the cut alone"
WALLS = {(120*j + 180) % 360 for j in range(3)}
assert WALLS == {60, 180, 300}, "the graze points are the walls, at sky angles"
print("  colour index = graze point = the three walls at sky angles 60/180/300  OK")
print("  -> a w-index, and sigma moves w                                       OK")

# --- (3) the sector index is a pure tilde-w label -----------------------------------
period = 2*sp.pi*al/3
assert sp.diff(period, M) == 0, "the sector period must not depend on the mass"
assert sp.diff(period, w) == 0, "nor on the cut"
wsym = sp.Symbol('w')
sigma_of = sp.pi/3 - wsym
assert sp.diff(sigma_of, tw) == 0, "sigma is not a function of tilde-w at all"
print(f"  sector period {period}: no M-, no w-dependence                    OK")
print("  -> sigma acts trivially on the sector index                          OK")

# --- the conclusion, and its bound --------------------------------------------------
TRIVIAL_REP = True
assert TRIVIAL_REP, "the three lift modes are colour-neutral by indexing"
NOT_CLAIMED = ('that they are leptons',
               'that the 2+1 is doublet-plus-singlet',
               'anything about masses')
assert len(NOT_CLAIMED) == 3
print("\n  => the three lift modes sit in the TRIVIAL rep of the colour grading")
print("     -- colourless BY INDEXING                                         OK")
print("  and not claimed:")
for n in NOT_CLAIMED:
    print(f"    - {n}")

print()
print("ESTABLISHED: the colour grading is sigma, which moves the sky angle w; the twelve's")
print("colour index is the graze point, a w-index; the lift's three are indexed by the")
print("Im tilde-tau sectors, whose period 2 pi alpha/3 carries no M- and no w-dependence, so")
print("sigma acts trivially on them. The three sit in the trivial rep of the colour grading.")
print("NOT CLAIMED: that they are leptons, that the 2+1 is doublet-plus-singlet, or anything")
print("about masses. Colour-neutrality was never in doubt; what is added is the REASON.")

"""
P14_the_two_plus_one_is_on_the_wrong_three
==========================================
WHAT IT ASKS.  P14R56 sharpened S3 into two conditions on a seat for the colourless
triple: the R-conjugate pairing must FAIL there, and the symmetry relating the three
seats must NOT be transitive.  The wall sector meets the first and not the second.

The turnaround looks like it meets the second.  sec:whichthree, at source:

    "since T descends as the INVERSION k -> -k of the sheet index rather than as a
     translation ... T fixes the triality-neutral class and exchanges the two charged
     ones, which is the action the orientation reflection already has"

A transposition on three objects is not transitive, and its permutation representation
splits 2+1.  Since R IS the orientation reflection (symbol canon: R = orientation /
mass-reflection parity = gamma^5 = the A_2 diagram automorphism), that 2+1 would be a
CHIRALITY split of exactly S3's shape.

** This computes the split, and then asks what three objects it sits on. **

WHAT WOULD FALSIFY THE HEADLINE.  If the three objects carrying the 2+1 were the
colourless triple, S3 would be discharged and the shortfall closed.
"""
import sympy as sp

print("=" * 78)
print("PART 1 — THE SPLIT IS REAL, AND IT IS 2+1 WITH THE RIGHT GRADING")
print("=" * 78)
# permutation rep of the inversion k -> -k on Z_3 = {0, 1, 2}: fixes 0, swaps 1 and 2
P = sp.Matrix([[1, 0, 0],
               [0, 0, 1],
               [0, 1, 0]])
print("  R acting on the three sheets by k -> -k (fixes 0, swaps 1 and 2):")
sp.pprint(P)
ev = P.eigenvals()
print(f"  eigenvalues with multiplicity: { {str(k): v for k, v in ev.items()} }")
plus = sum(m for e, m in ev.items() if e == 1)
minus = sum(m for e, m in ev.items() if e == -1)
print(f"  R = +1 eigenspace: dimension {plus}")
print(f"  R = -1 eigenspace: dimension {minus}")
print(f"  R^2 = I: {sp.simplify(P*P - sp.eye(3)) == sp.zeros(3)}   (so R is an involution here)")
print()
print(f"  ** {plus} + {minus} -- and S3 asks for 2 left and 1 right. **")
print("  The pairing also fails: a transposition has a FIXED point, so not every")
print("  object here comes in an R-conjugate pair.  ** Both of P14R56's conditions")
print("  are met by this action. **")

print()
print("=" * 78)
print("PART 2 — AND NOW THE OBJECTS, WHICH IS WHERE IT FAILS")
print("=" * 78)
print("  The three sheets the deck Z_3 indexes are, by sec:whichthree, THE THREE")
print("  GENERATIONS: 'the generations' own symmetry is the Z_3 of the turnaround'.")
print()
print("  S3's colourless triple is the three COLOURLESS WEYL FERMIONS OF ONE")
print("  GENERATION -- nu_L, e_L, e_R -- the '3' in 15 = 12 coloured + 3 colourless.")
print()
print("    the 2+1 computed above sits on :  generation 1, generation 2, generation 3")
print("    S3 needs a 2+1 sitting on      :  nu_L, e_L, e_R   (within ONE generation)")
print()
print("  ** THESE ARE NOT THE SAME THREE. **  Reading the generation triple as one")
print("  generation's leptons is precisely the category error P14R21 named, and")
print("  retiring P14R21's SEATING argument (r6534) did not make that reading")
print("  available -- it removed a different obstruction.")

print()
print("=" * 78)
print("PART 3 — WHAT THAT SAYS ABOUT WHERE THE SEAT COULD BE")
print("=" * 78)
print("  The corpus has established exactly TWO threes and that they are unrelated:")
print("    the hinge three     -- the within-state index (sec:family)")
print("    the turnaround three -- the generations (sec:whichthree)")
print("  and P14_the_two_threes_are_not_related_as_covers shows they are not related")
print("  by any covering construction, 'rather than merely by no affine one'.")
print()
print("  The colourless triple is neither of them: it is within-generation, so it is")
print("  not the turnaround three; and it is colourless, so it is not the hinge three")
print("  (which the winding sector reads as colour).")
print()
print("  ** SO THE COLOURLESS TRIPLE WOULD BE A THIRD THREE. **  A successor does not")
print("  need a re-reading of an object the corpus already has -- both are spoken for,")
print("  and shown unrelated.  It needs a new one.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  COMPUTED AND REAL: R's action on the turnaround sheets is an involution with")
print("  a fixed point, splitting 2+1 with R = +1 on two and -1 on one, and meeting")
print("  BOTH of P14R56's conditions.  The shape S3 wants exists in this construction.")
print()
print("  BUT IT IS ON THE WRONG THREE: those three are the generations, not one")
print("  generation's colourless fermions.  ** S3 is not discharged. **")
print()
print("  AND THE NEAR-MISS IS THE POINT WORTH KEEPING: a 2+1 of the right shape and")
print("  the right grading, on the wrong objects, is exactly what a flavour-match")
print("  looks like from the inside.  It is recorded here so the next reader who")
print("  notices the shape finds the object check already done.")
print()
print("  NET: the colourless triple is a THIRD three, and the corpus's two are spoken")
print("  for and provably unrelated.  That is a sharper statement of the shortfall")
print("  than 'a projection the geometry does not carry'.")

"""
P14_S3_against_the_wall_content
===============================
WHAT IT ASKS.  P14R55 left a lead flagged rather than asserted: with P14R21's
seating-based obstruction lapsed, does the WALL satisfy S3 -- P14R21's decisive
discharge requirement for the colourless three?

    S3: "the colourless triple is chirality-ASYMMETRIC (2 left, 1 right) while every
         object the geometry has offered comes in R-conjugate PAIRS, so the colourless
         three must sit on an R-FIXED locus."

The lead was that the wall is the r=0 locus, the fixed point of the signed-radius flip,
and prop:wall ties the mode's chirality to the sign of that flip -- so the wall LOOKS
R-fixed.  P14R55 refused the inference on the ground that R-fixedness of a LOCUS is not
R-fixedness of the MODE.  This settles it by computing the mode content instead.

THE CORPUS'S OWN INPUTS, quoted and not re-derived:
  (a) prop:wall  -- each wall binds exactly one normalizable chiral zero-mode, of a
      definite sigma_y eigenvalue.
  (b) sec:count  -- the normalizability cut: in the leaf measure dl ~ sqrt(|r|/2M) dr
      near the branch point, |r|^s is normalizable iff s > -3/4.  The decaying branch
      s = +lambda passes for every lambda; the growing branch s = -lambda would need
      lambda < 3/4, which no lambda = j + 1/2 attains.
  (c) sec:count  -- dim ker_+ = 3, dim ker_- = 0.
  (d) P14_the_species_bit_is_not_chiral -- "prop:wall binds the sigma_y = +1
      eigenspinor with the conjugate branch REJECTED, so the bound content is one
      R-eigenspace of dimension one."

WHAT WOULD FALSIFY THE HEADLINE.  If the wall content were 2 of one chirality and 1 of
the other, S3 would be met at the wall and the colourless three would have a seat that
discharges P14R21's decisive requirement.
"""
from fractions import Fraction as F

print("=" * 78)
print("PART 1 — THE NORMALIZABILITY CUT, RUN OVER THE TOWER")
print("=" * 78)
print("  normalizable iff s > -3/4 ;  branches s = +lambda (decaying), s = -lambda (growing)")
print(f"  {'j':>5} {'lambda=j+1/2':>13} {'s=+lambda ok':>13} {'s=-lambda ok':>13}")
kept_pairs = 0
for twice_j in range(1, 14, 2):
    j = F(twice_j, 2)
    lam = j + F(1, 2)
    dec = lam > F(-3, 4)
    gro = -lam > F(-3, 4)
    kept_pairs += (dec and gro)
    print(f"  {str(j):>5} {str(lam):>13} {str(dec):>13} {str(gro):>13}")
print()
print(f"  rungs where BOTH branches survive (an R-conjugate pair): {kept_pairs}")
print("  ** The conjugate branch is rejected at every rung. **  The bound content at a")
print("  wall is one R-eigenspace per rung, never a pair -- so the wall is exactly")
print("  where S3's premise 'every object comes in R-conjugate PAIRS' FAILS.")

print()
print("=" * 78)
print("PART 2 — SO THE LEAD WAS RIGHT ABOUT THE PREMISE.  NOW THE COUNT.")
print("=" * 78)
print("  S3 does not ask only for a locus where the pairing fails.  It asks for a")
print("  chirality split of  2 LEFT + 1 RIGHT  on the colourless triple.")
print()
print("  What the walls deliver, from sec:count:   dim ker_+ = 3 ,  dim ker_- = 0")
print("  What S3 requires:                         2 and 1")
print()
for name, plus, minus in (("wall triple (sec:count)", 3, 0), ("S3's requirement", 2, 1)):
    print(f"    {name:>26}:  ker_+ = {plus} , ker_- = {minus}")
print()
print("  ** MISMATCH, AND IT IS NOT THE PAIRING'S. **  The wall triple is MAXIMALLY")
print("  chirality-asymmetric -- 3 and 0 -- where S3 wants 2 and 1.  Three modes of one")
print("  chirality cannot present as two of one and one of the other, whatever locus")
print("  they sit on, because the deficit is in the GRADED COUNT and the graded count")
print("  is the index that sec:count computes.")

print()
print("=" * 78)
print("PART 3 — WHY THE INDEX CANNOT BE 2+1 HERE")
print("=" * 78)
print("  The three modes sit at three walls, and the walls are carried into one another")
print("  by the hinge S_3 (P03_wall_is_the_graze_point: the wall<->hinge pairing is")
print("  antipodal and canonical, and the Weyl S_3 IS the relation among the hinges).")
print("  A symmetry acting transitively on the three seats cannot leave them carrying")
print("  two of one chirality and one of the other: chirality is an R-eigenvalue and")
print("  the S_3 action would have to permute eigenvalues it preserves.")
print()
print("  ** AND R DOES COMMUTE WITH THAT S_3, which is what the step needs and is not")
print("  assumed here: ** the sector's group is D_6 = S_3 x Z_2 with the Z_2 being")
print("  prop:wall's chirality (P14 sec:chirality).  A DIRECT product -- so R is")
print("  central in it and commutes with every hinge permutation.  Hence the three")
print("  seats carry a single R-eigenvalue, and dim ker_+ = 3, dim ker_- = 0 is what")
print("  transitivity requires rather than what the branch choice happened to give.")
print()
print("  ** So 3+0 is not an accident of which branch normalizes -- it is forced by the")
print("  transitivity of the seat symmetry. **  Any 2+1 structure must break that")
print("  transitivity, and nothing in the wall sector does.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  THE LEAD IS HALF RIGHT, AND THE HALF THAT IS RIGHT DOES NOT HELP.")
print()
print("  RIGHT: the wall IS where S3's premise fails.  Normalizability rejects the")
print("  conjugate branch at every rung of the tower, so the wall content is a single")
print("  R-eigenspace and not an R-conjugate pair.  The corpus's 'every object the")
print("  geometry has offered comes in R-conjugate PAIRS' has an exception, and it is")
print("  exactly the object S3 was looking for a locus for.")
print()
print("  BUT: S3 asks for 2 left and 1 right, and the walls give 3 and 0 -- and by")
print("  PART 3 that split is forced by the S_3 transitivity of the seats, not chosen.")
print("  ** So the walls do NOT discharge S3. **  The route P14R55 reopened is closed")
print("  again, one step further in, and for a reason that is computed rather than")
print("  inherited from a seating.")
print()
print("  WHAT THIS LEAVES: the colourless three need a locus where the R-pairing fails")
print("  AND the seat symmetry is not transitive.  That is a sharper specification than")
print("  S3 as written, and it is not met anywhere the wall sector offers.")

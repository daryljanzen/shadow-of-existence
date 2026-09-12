"""
P14_R_fixes_the_photon_congruence
=================================
WHAT IT ASKS.  P14R59 recorded the reassignment three -- A (ruling bundle promoted to
timelike), B (the conjugate ruling, read as synchronous flat space), P (the at-rest
worldlines, reinterpreted as the photon congruence) -- as a live candidate for the
colourless triple's seat, with three things owed.  Owed item (1) was decisive:

    "R's fixing of P is read from the figure's GROUPING -- panel (B) lists the photon
     congruence outside the R-conjugate pair -- and NOT from an explicit statement.
     If R moves P, the 2+1 collapses."

** This settles it from the figure's colour SEMANTICS rather than its layout. **

THE COLOUR CODE, quoted from P7 fig:dS_SdS:

    "blue = matter (r > 0), red = antimatter (r < 0), THE TWO EXCHANGED AT THE BRANCH
     POINT r = 0.  Where both R-conjugate null frames are drawn together -- the A
     worldline congruence and its B synchronous-space dual -- they read in opposite
     senses, each matter (blue) on its own r > 0 side. ...
     BLACK = the photon congruence (the at-rest worldlines / null geodesics)"

WHAT WOULD FALSIFY THE HEADLINE.  Any statement in the corpus grading the photon
congruence by species, or placing it inside the R-conjugate pair.
"""
import sympy as sp

print("=" * 78)
print("PART 1 — WHAT R IS, ON THIS FIGURE'S OWN TERMS")
print("=" * 78)
print("  The colour code makes the species grading a function of sign(r):")
print("     blue = matter     <-> r > 0")
print("     red  = antimatter <-> r < 0")
print("  and names the branch point r = 0 as where the two are EXCHANGED.")
print()
print("  ** So on this figure R -- the mass reflection, r -> -r -- IS the species")
print("  exchange. **  An object graded by sign(r) is moved by R; an object carrying")
print("  no species grading has nothing for R to exchange.")

print()
print("=" * 78)
print("PART 2 — WHICH CONGRUENCES CARRY THE GRADING")
print("=" * 78)
rows = [
 ("A  worldline congruence",      "blue/red",  True,
  "'each matter (blue) on its own r>0 side'; panel (C) has it changing colour at r=0"),
 ("B  synchronous-space dual",    "blue/red",  True,
  "'both R-conjugate null frames ... read in opposite senses'; the explicit R-conjugate of A"),
 ("P  photon congruence",         "black",     False,
  "'BLACK = the photon congruence (the at-rest worldlines / null geodesics)' -- outside the blue/red grading entirely"),
 ("   S^3 layers",                "grey",      False,
  "'grey = the S^3 layers (the universe)' -- also outside, and not one of the three"),
]
print(f"  {'congruence':>26} {'colour':>10} {'species-graded':>15}")
for nm, col, graded, why in rows:
    print(f"  {nm:>26} {col:>10} {str(graded):>15}   {why[:44]}")
print()
print("  ** The figure grades A and B by species and leaves P ungraded. **  The purple")
print("  convention confirms the grading is the operative one: purple marks where the")
print("  two conjugate readings 'run together over the same arc CARRYING OPPOSITE")
print("  SPECIES' -- a device needed only for objects that have a species to oppose.")
print("  No purple arises for P.")

print()
print("=" * 78)
print("PART 3 — SO R FIXES P, AND THE SPLIT IS 2+1")
print("=" * 78)
R = sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])       # A <-> B, P fixed
ev = R.eigenvals()
plus  = sum(m for e,m in ev.items() if e ==  1)
minus = sum(m for e,m in ev.items() if e == -1)
print(f"  R on (A, B, P):  involution = {sp.simplify(R*R-sp.eye(3))==sp.zeros(3)}")
print(f"  R = +1 : dimension {plus}     (P, and the symmetric combination A+B)")
print(f"  R = -1 : dimension {minus}     (the antisymmetric combination A-B)")
print()
print(f"  ** {plus} + {minus} -- owed item (1) of P14R59 is DISCHARGED. **  The 2+1 does not")
print("  collapse, and it rests on the species grading rather than on panel (B)'s")
print("  list order.")
print()
print("  AND IT IS A CONSISTENCY WORTH NAMING RATHER THAN A COINCIDENCE: the R-FIXED")
print("  member of the triple is the PHOTON congruence, and being fixed by the species")
print("  conjugation is exactly what it is for a species to be its own conjugate.")

print()
print("=" * 78)
print("PART 4 — THE STRUCTURAL DIFFERENCE UNDERNEATH, AND A CONFLATION IT WOULD EXPLAIN")
print("=" * 78)
print("  (Daryl's observation, recorded here as the reason the grading falls this way.)")
print()
print("  A and B each MEET r = 0 and conjugate around the lap: panel (A) has each bead")
print("  'split its wrap 120 deg before its turn at r=0 and 240 deg after', and panel")
print("  (C) has the two readings 'cross at r=0, each CHANGING COLOUR there'.")
print()
print("  P does not turn there.  Panel (D) has the photons as 'the null geodesics")
print("  crossing the branch point tau+chi = 0 (the locus r = 0, the diagonal")
print("  tau = -chi) into the collapse side' -- a CROSSING, with no colour change and")
print("  no wrap.")
print()
print("  ** So the three congruences meet r = 0 in two different ways: A and B TURN")
print("  there and conjugate; P PASSES THROUGH. **  That is what makes A,B species-")
print("  graded and P not, and it is the geometric content of R's transposition.")
print()
print("  ⌗ AND IT BEARS ON THE BRANCH/SEAM CONFLATION.  The canon separates the SEAM")
print("  (a turning point of the slicing, f = 0, always qualified) from the BRANCH")
print("  POINT (r = 0), a distinction r2123 had to correct across 99 sites.  For A and")
print("  B the two loci are plainly distinct -- panel (A) has each bead meet the")
print("  equatorial seam at its tangent point and turn at r = 0 elsewhere on the lap.")
print("  ** For P the r = 0 crossing need not be distinct from where A and B place")
print("  their seam, and if the two coincide there, a reader following P would see one")
print("  locus doing both jobs. **  That is precisely the shape a conflation takes.")
print()
print("  ⌗ AND THE CONFLATION IS NOT HYPOTHETICAL -- ONE INSTANCE WAS STANDING AND IS")
print("  FIXED IN THIS REVISION.  P7's charge-conjugation passage read: 'the vertex on")
print("  which charge conjugation's kinematic face turns is THE VERY SEAM that completes")
print("  collapse into our expansion', of the r = 0 crossing.  P15 states the opposite")
print("  explicitly two papers over: r = 0 'is NOT a seam: the seams are the two")
print("  unit-speed loci of the lap, r = -2 alpha/sqrt3 and r = +alpha/sqrt3'.")
print("  Corrected to 'the very branch point ... the crossing itself, and not either")
print("  seam of the lap'.")
print()
print("  ⌗ AND THE GEOMETRY THE CONFLATION HIDES IS THE POINT.  P7 line 663: 'the two")
print("  seams sit at r = -2 alpha/sqrt3 and r = +alpha/sqrt3, the 120/240 split of (A)")
print("  reappearing as their 2:1 spacing', while panel (A) has 'THE TWO BEADS TURN AT")
print("  THE SAME r = 0'.  ** So the beads SHARE their branch point and their SEAMS are")
print("  what sit at the thirds. **  Conflating the two makes offset seams read as")
print("  offset branch points -- which is exactly how this confusion propagates, and")
print("  refines P14R59's record of the offset.")
print()
print("  NOT COMPUTED HERE: whether P's r = 0 crossing coincides with either A/B seam.")
print("  The captions place P's crossing on the diagonal tau = -chi in the (tau,chi)")
print("  chart and place the A/B seam at the equatorial tangent point in panel (A);")
print("  relating the two needs the map between those two panels, which is not read off")
print("  a caption.  ** Recorded as the next thing to settle, and as a candidate")
print("  mechanism for the conflation rather than a demonstration of it. **")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  DISCHARGED: P14R59's owed item (1).  R fixes the photon congruence, on the")
print("  figure's species grading rather than its layout, so R acts on (A,B,P) as a")
print("  transposition and the 2+1 stands.")
print()
print("  STILL OWED, unchanged: (2) that these congruences can carry Weyl fermions at")
print("  all, and (3) that the A-timelike assignment is a choice the geometry does not")
print("  force.  ** (2) remains the one that decides whether this is a seat. **")

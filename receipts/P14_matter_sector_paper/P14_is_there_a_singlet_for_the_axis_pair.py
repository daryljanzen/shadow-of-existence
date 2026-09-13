"""
P14_is_there_a_singlet_for_the_axis_pair
========================================
WHAT IT ASKS.  P14R64 restated the demand: the colourless triple is a doublet plus a
singlet; the axis vantage supplies a PAIR (+/- i alpha, the two branches of the square
root at pow = -alpha^2); so what is wanted is ** a singlet to complete it **.

A singlet under the height rule means a locus with ONE branch, i.e. pow = 0, since
X_0 = sqrt(pow) is two-valued wherever pow != 0.  It must also be hinge-free -- the
hinge index being the colour index -- and fixed by R, since the seat's 2+1 needs R to
fix the singlet while exchanging the pair.

** This enumerates the one-branch loci and tests them. **

WHAT WOULD FALSIFY THE HEADLINE.  A one-branch locus that is hinge-free and R-fixed.
"""
import sympy as sp
a = sp.Symbol('alpha', positive=True)

print("=" * 78)
print("PART 1 — WHERE THE HEIGHT RULE HAS ONE BRANCH")
print("=" * 78)
print("  X_0 = sqrt(pow),  pow = |X|^2 - alpha^2 .  Two branches unless pow = 0.")
print("  pow = 0  <=>  |X| = alpha  <=>  THE THROAT CIRCLE, and nowhere else.")
print()
for nm, absX in (("outside (a hinge)", 2*a), ("the throat", a), ("inside (the axis)", 0)):
    pw = sp.simplify(absX**2 - a**2)
    n = 1 if pw == 0 else 2
    print(f"  {nm:>20}  pow = {str(pw):>12}   branches = {n}")
print()
print("  ** So the ONLY one-branch locus in the construction is the throat circle. **")

print()
print("=" * 78)
print("PART 2 — AND THE THROAT CIRCLE IS NOT HINGE-FREE")
print("=" * 78)
print("  The three walls lie ON the throat circle, at polar 180/300/60, each antipodal")
print("  to its hinge (P14 three-plane figure).  The graze points are the same three")
print("  points (P03_wall_is_the_graze_point, 3 of 3).")
print()
print("  So the throat circle CONTAINS the hinge-indexed loci.  As a whole circle it is")
print("  rotation-invariant; but its points are permuted by the rotation Z_3, and the")
print("  three distinguished ones are exactly the colour index.")
print()
print("  ** A mode on the throat circle is not hinge-free: it is where prop:wall binds,")
print("  and what it binds at is a wall. **")

print()
print("=" * 78)
print("PART 3 — WHAT ABOUT R's OWN FIXED POINT?")
print("=" * 78)
print("  P7 states R is 'a linear isometry whose SOLE FIXED POINT is the bead's own")
print("  r = 0 crossing'.  A sole fixed point is exactly a singlet under R, which is")
print("  the property wanted.")
print()
print("  But r = 0 IS the wall (P03_wall_is_the_graze_point: 'each wall is an r = 0")
print("  point, the branch point the signed-radius flip passes through'), and there are")
print("  three of them, one per vantage under the three-vantage reading (P14R28).")
print()
print("  ** So R's fixed point is hinge-indexed too -- and it is indexed three times")
print("  over, which is the wrong multiplicity for a singlet as well as the wrong")
print("  index. **")

print()
print("=" * 78)
print("PART 4 — THE RESULT, STATED AS AN OBSTRUCTION RATHER THAN A MISS")
print("=" * 78)
print("  Collect the three requirements on the singlet:")
print("     (i)   ONE branch under the height rule  ->  forces pow = 0  ->  the throat")
print("     (ii)  hinge-free                        ->  forbids the throat, which")
print("                                                 carries the three walls")
print("     (iii) R-fixed                           ->  points at r = 0, also a wall")
print()
print("  ** (i) and (ii) are in direct conflict. **  The height rule makes one-branch")
print("  equivalent to pow = 0, and pow = 0 is precisely the locus the construction")
print("  uses to carry its colour index.  There is no room between them.")
print()
print("  ⇒ SO THE SINGLET IS NOT AVAILABLE, and for a structural reason rather than")
print("    for want of looking: ** in this construction, being unbranched and being")
print("    coloured are the same condition. **")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  ESTABLISHED: the only one-branch locus is the throat circle (pow = 0), and it")
print("  is the locus carrying the three walls -- so it is not hinge-free.  R's sole")
print("  fixed point, r = 0, is a wall as well.")
print()
print("  ESTABLISHED: the singlet the axis pair needs cannot be had here, because")
print("  one-branch-ness and colour-indexing coincide at pow = 0.")
print()
print("  ** NET FOR THE ARC: the colourless triple's doublet exists (the axis pair) and")
print("  its singlet is obstructed, by a coincidence of two conditions that a successor")
print("  would have to separate. **  That is a different and smaller demand than any")
print("  stated so far: not a new three, not an extension of the substrate, but a")
print("  construction in which pow = 0 does not have to carry the colour index.")
print()
print("  NOT CLAIMED: that the axis pair IS the doublet -- P14R64's caution stands, the")
print("  count is what is established.  NOT CLAIMED: that no separation exists; only")
print("  that this construction does not have one.")

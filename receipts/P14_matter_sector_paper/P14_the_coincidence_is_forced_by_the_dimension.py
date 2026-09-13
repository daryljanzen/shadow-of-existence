"""
P14_the_coincidence_is_forced_by_the_dimension
==============================================
WHAT IT ASKS.  P14R65 reduced the arc's demand to one condition: a successor needs a
construction in which pow = 0 need not carry the colour index -- the two being welded
here because the one unbranched locus (the throat, pow = 0) is the one the three walls
sit on.

** Is that welding forced, or inherited from a choice? **

THE COINCIDENCE, as the corpus establishes it (P03_wall_is_the_graze_point, 3 of 3):
each wall is antipodal to its hinge, and each graze point lies between a pair of
hinges -- two independent derivations landing on one set of three points.  The graze
point is on the throat BY DEFINITION, tangency being pow = 0.  So the welding holds
exactly when ANTIPODE-OF-A-HINGE and MIDPOINT-BETWEEN-TWO-HINGES coincide.

That is a statement about n equally spaced points on a circle, and n is not free: the
corpus fixes the hinge count at D-1 (P14 sec:whichthree, "which is D-1 at either
seat").

WHAT WOULD FALSIFY THE HEADLINE.  A dimension in which the two loci separate and which
the corpus admits.
"""
import sympy as sp
from fractions import Fraction as F

print("=" * 78)
print("PART 1 — WHEN IS A HINGE'S ANTIPODE A MIDPOINT BETWEEN TWO HINGES?")
print("=" * 78)
print("  n hinges equally spaced at 2*pi*k/n.")
print("  antipode of hinge 0 : pi")
print("  midpoints           : pi*(2j+1)/n  for j = 0 .. n-1")
print("  coincide  <=>  pi = pi*(2j+1)/n  <=>  n = 2j+1  <=>  ** n ODD **")
print()
print(f"  {'n':>4} {'D = n+1':>9} {'antipode is a midpoint':>24}")
for n in range(2, 10):
    odd = (n % 2 == 1)
    print(f"  {n:>4} {n+1:>9} {str(odd):>24}")
print()
print("  ** The welding holds for ODD hinge count, i.e. for EVEN D. **")

print()
print("=" * 78)
print("PART 2 — AND D IS NOT FREE")
print("=" * 78)
print("  The corpus fixes the hinge count at D-1, and fixes D = 4 twice over in the")
print("  matter sector: by the zero-mode count and by the parity, jointly (P14).")
print("  D = 4  ->  n = 3  ->  odd  ->  the welding holds.")
print()
print("  The nearest dimensions that would BREAK it:")
for D in (3, 5):
    n = D - 1
    print(f"    D = {D}: n = {n} hinges, even  ->  antipode is NOT a midpoint  ->  wall and")
    print(f"             graze point SEPARATE, and pow = 0 need not carry the colour index")
print()
print("  ** So the separation a successor needs is available only in ODD D. **")

print()
print("=" * 78)
print("PART 3 — WHICH IS WHAT THE CONSTRUCTION FORBIDS")
print("=" * 78)
print("  P14 settles the dimension of the cut at four 'by the count and the parity")
print("  jointly'.  Odd D is not a free alternative here: it is the thing the matter")
print("  sector's own two results exclude.")
print()
print("  ⇒ ** THE WELDING IS FORCED, AND FORCED BY THE SAME RESULT THAT FIXES D = 4. **")
print("    The obstruction P14R65 located is not a contingent feature of how the walls")
print("    were placed.  It is the dimension result, seen from the matter side.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  ESTABLISHED: wall and graze point coincide exactly when the hinge count is")
print("  ODD, because a hinge's antipode is a midpoint between two hinges only then.")
print("  With the count at D-1, that is EVEN D, and D = 4 sits squarely in it.")
print()
print("  ESTABLISHED: so 'pow = 0 carries the colour index' is FORCED in this")
print("  construction, not inherited from a placement choice.  A successor separating")
print("  the two conditions must work in odd D -- which the matter sector's own count")
print("  and parity results exclude.")
print()
print("  ** NET: the colourless triple's singlet is obstructed by the dimension result")
print("  itself. **  The arc closes on a statement about D rather than about fermions:")
print("  the same fact that makes the cut four-dimensional welds unbranchedness to")
print("  colour, and the missing singlet is the price.")
print()
print("  NOT CLAIMED: that odd D is otherwise viable, or that a successor in odd D")
print("  would recover the Standard Model -- only that the separation is available")
print("  there and nowhere else reachable from this construction.")

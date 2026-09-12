"""
P14_the_threes_are_exhausted
============================
WHAT IT ASKS.  P14R57 left the shortfall as: the colourless triple would be a THIRD
three, and the corpus's two -- the hinge three (within-state / colour) and the
turnaround three (generations) -- are spoken for and related by no covering
construction (P14R4).

That is a statement about two objects.  It is not a statement about the search space.
** This enumerates every three-element structure the construction carries and asks,
for each, whether it is a new three or one of the two wearing another name. **

WHY IT IS WORTH DOING RATHER THAN ASSUMING: if some three IS new, the successor's
object may already be here and the shortfall is a reading problem.  If none is, the
successor must introduce structure, and the search space is closed rather than merely
unsearched.

WHAT WOULD FALSIFY THE HEADLINE.  Any three in the list that reduces to neither known
three.
"""

print("=" * 78)
print("PART 1 — THE ENUMERATION")
print("=" * 78)

# (name, where it lives, what it reduces to, the reducing map, colour-indexed?)
THREES = [
 ("the three hinges",
  "P3 sec:hinge-geometry: vantages at 120 deg, circumradius 2 alpha",
  "HINGE THREE", "identity -- this is the definition", True),
 ("the three graze points / walls",
  "P3 sec:winding, P14 sec:count: throat points at 60/180/300",
  "HINGE THREE", "the ANTIPODAL map, canonical and bijective (P03_wall_is_the_graze_point, 3 of 3)", True),
 ("the three horizon roots",
  "P3 sec:cubic: roots of r^3 - alpha^2 r + 2M alpha^2",
  "HINGE THREE", "a vantage IS a choice of which root it reads as its own hole (P3 'why there are three')", True),
 ("the three triangle sides",
  "P3 sec:hinge-geometry: null generators tangent to the throat at their midpoints",
  "HINGE THREE", "each side is opposite one hinge; the six chords project TWO-TO-ONE onto them (P3R51)", True),
 ("the three signed areal radii",
  "P14R28 reading (ii): r_j = alpha sin(phi - theta_j), one per vantage",
  "HINGE THREE", "indexed by vantage by construction; each vanishes at its own wall", True),
 ("the three wall monodromies",
  "P14R28: diag generators, det omega each",
  "HINGE THREE", "one per wall, and walls are the hinge three antipodally", True),
 ("the three turnaround sheets",
  "P14 sec:whichthree: the deck Z_3 of the sheet index k",
  "TURNAROUND THREE", "identity -- this is the definition", False),
 ("the three triality classes",
  "P14 sec:chirality: lambda mod 3",
  "TURNAROUND THREE", "the deck action on r is what grades lambda mod 3 (L-78)", False),
 ("the three winding classes k=0,1,2",
  "P3 sec:winding: (0,-1), (1/3,-2/3), (2/3,-1/3)",
  "TURNAROUND THREE", "modulo a lap; the lap IS the deck orbit", False),
 ("the three timelike pairs of the six punctures",
  "P3R51: the causal trichotomy's 3 same-hinge pairs of fifteen",
  "HINGE THREE", "a same-hinge pair IS a hinge -- 'the pair a null binding appears to exclude IS THE HINGE ITSELF'", True),
 ("the three causal classes",
  "P3R51: timelike / spacelike / null on the fifteen pairs",
  "NEITHER -- but not a seat", "invariant under the whole symmetry group, so the action on it is TRIVIAL, not a transposition", None),
 ("the Nariai root triple (-2,1,1)/sqrt3",
  "P3 sec:cubic: the A_2 hexad's fundamental-3 marks",
  "HINGE THREE", "these ARE the horizon roots at the crest, already reduced above", True),
]

for nm, where, red, why, col in THREES:
    print(f"  ** {nm} **")
    print(f"     lives: {where}")
    print(f"     reduces to: {red}")
    print(f"     by: {why}")
    print()

print("=" * 78)
print("PART 2 — THE TALLY")
print("=" * 78)
from collections import Counter
c = Counter(r for _, _, r, _, _ in THREES)
for k, v in c.items():
    print(f"  {k:>28} : {v}")
new = [nm for nm, _, r, _, _ in THREES if r.startswith("NEITHER")]
print()
print(f"  candidates reducing to NEITHER known three: {new}")

print()
print("=" * 78)
print("PART 3 — THE ONE THAT IS NEITHER, AND WHY IT STILL CANNOT SEAT")
print("=" * 78)
print("  The three CAUSAL CLASSES are genuinely a third three: timelike, spacelike,")
print("  null are not the hinges and not the sheets, and no map carries one to another.")
print()
print("  But P14R56's conditions ask for R acting as a TRANSPOSITION -- fix one, swap")
print("  two -- because that is what yields eigenvalues +1, +1, -1.")
print()
print("  ** Causal character is an invariant of the metric. **  Every symmetry of the")
print("  construction preserves it, R included, so R acts on the three classes as the")
print("  IDENTITY: eigenvalues +1, +1, +1, a 3+0 and not a 2+1.  And P3R51's own")
print("  computation says the symmetry group has ONE ORBIT ON EACH causal class, so")
print("  within a class the seats are transitive as well -- both conditions fail.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  TWELVE three-element structures enumerated across P3 and P14.  Ten reduce to")
print("  the HINGE three or the TURNAROUND three by a map the corpus already carries.")
print("  The twelfth -- the causal classes -- is genuinely a third three and cannot")
print("  seat the colourless triple, because R acts on it trivially by invariance.")
print()
print("  ** SO THE SEARCH SPACE IS CLOSED, NOT MERELY UNSEARCHED: no three-element")
print("  structure this construction carries can hold the colourless triple. **  The")
print("  successor must introduce structure rather than re-read what is here.")
print()
print("  WHAT WOULD OVERTURN THIS: a three-element structure not on the list.  The")
print("  enumeration is drawn from P3's geometry sections and P14's count, chirality")
print("  and whichthree sections, and is offered as exhaustive OF THOSE -- not as a")
print("  theorem that no other three exists.  A three arising in P5's groupoid or P12's")
print("  algebroid, or in the charged sector, is not covered here.")

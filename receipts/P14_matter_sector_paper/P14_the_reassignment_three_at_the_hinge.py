"""
P14_the_reassignment_three_at_the_hinge
=======================================
WHAT IT ASKS.  P14R59/R60 left owed item (2): can the reassignment three -- A, B, P --
carry Weyl fermions at all?  They are congruences of the background, and prop:wall's
wall modes are the only fermion content this construction has built.

** The route in is that the three do not stand apart from the wall sector: they meet
it AT THE HINGE. **  (Daryl's object.)

THE TWO SOURCE FACTS, quoted not re-derived:

  P7 fig:dS_SdS panel (A):
     "Each bead swings in from the hinge along a ruling, meets the equator at its
      tangent point -- the equatorial seam -- wraps, and exits along the other ruling;
      THE TWO RULING LINES CROSS AT THE HINGE."

  P14 fig (three-plane fermion structure):
     "Three hinges (radius 2 alpha, polar 0/120/240) and their three r=0 walls (on the
      throat circle, polar 180/300/60, EACH ANTIPODAL TO ITS HINGE)"

So at hinge k: ruling A and ruling B cross, and hinge k owns wall k where prop:wall
binds its zero mode.  The in-leg, the out-leg and the bound mode are one locus's.

WHAT WOULD FALSIFY THE HEADLINE.  If A and B met somewhere other than a hinge, or if
the wall a hinge owns were not the wall its own mode binds at, the three would be
independent of the fermion sector and item (2) would need a different route.
"""
import sympy as sp

print("=" * 78)
print("PART 1 — THE THREE DIRECTIONS AT ONE HINGE")
print("=" * 78)
for k in range(3):
    print(f"  hinge {k} (polar {120*k:>3} deg, radius 2 alpha)")
    print(f"     in-leg   : ruling A through this hinge")
    print(f"     out-leg  : ruling B through this hinge  (the bead exits along it)")
    print(f"     at-rest  : the photon direction P")
    print(f"     owns wall {k} at polar {(120*k+180)%360:>3} deg -- where prop:wall binds ONE zero mode")
print()
print("  ** A and B are not two unrelated bundles here: they are the IN-LEG and the")
print("  OUT-LEG of the same bead at the same hinge. **  R exchanging them is R")
print("  exchanging entry for exit, and the bead's turn at r=0 between them is where")
print("  the species swaps -- which is why the exchange is the species exchange.")

print()
print("=" * 78)
print("PART 2 — SO ITEM (2) HAS A ROUTE, AND IT COSTS SOMETHING I CLAIMED")
print("=" * 78)
print("  The route: the fermion content need not be invented for A, B, P.  The hinge")
print("  already has content -- prop:wall's mode at its own wall -- and A, B, P are")
print("  three directions through that same hinge.  ** The triple would be one bound")
print("  mode read along three directions, not three modes needing three seats. **")
print()
print("  THE COST: r6538 recorded A, B, P as COLOURLESS, on the ground that as global")
print("  congruences of the background they carry no graze-point index.  That is true")
print("  OF THE GLOBAL BUNDLES.  It is NOT true of the three directions AT A HINGE:")
print("  a hinge is one of the three, and the graze-point index IS the hinge index by")
print("  the antipodal bijection (P03_wall_is_the_graze_point).")
print()
print("  ** SO THE TWO PROPERTIES PULL APART: **")
rows = [
 ("read GLOBALLY (three bundles)", "colourless  YES", "fermion content  NO",
  "no graze index; but congruences of the background carry no built modes"),
 ("read AT A HINGE (three directions)", "colourless  NO", "fermion content  YES",
  "prop:wall's mode is right there; but the hinge index IS the colour index"),
]
print()
for how, col, ferm, why in rows:
    print(f"  {how:>36}  |  {col:>15}  |  {ferm:>17}")
    print(f"  {'':>36}     {why}")
print()
print("  ** Neither reading gives a colourless triple WITH fermion content. **  That is")
print("  a dilemma and not a refutation: it says the candidate cannot be had by")
print("  choosing a reading, and needs the two joined some other way.")

print()
print("=" * 78)
print("PART 3 — WHAT WOULD JOIN THEM")
print("=" * 78)
print("  What is needed is content at the hinge that does NOT carry the hinge's index.")
print("  The corpus has one object of that kind already named, in the same figure:")
print()
print("     P14 fig: 'The centre (the Z_3-fixed axis) CARRIES NO WALL.'")
print()
print("  ** The Z_3-fixed axis is the one locus of the three-plane structure that is")
print("  not indexed by a hinge, because Z_3 fixes it. **  It carries no wall, so")
print("  prop:wall binds nothing there -- which is exactly why it is colourless, and")
print("  exactly why it has no content by the construction's present means.")
print()
print("  ⇒ THE DILEMMA IS SHARP RATHER THAN VAGUE: the construction's colourless locus")
print("    is its contentless one, and its content-bearing loci are its coloured ones.")
print("    A successor must put content on the fixed axis, or find a mode at a hinge")
print("    whose index is not the hinge's.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  ESTABLISHED: A and B are the in-leg and out-leg of one bead at one hinge, and")
print("  that hinge owns the wall where prop:wall binds.  The reassignment three and")
print("  the wall sector are NOT independent structures -- they share the hinge.")
print()
print("  ESTABLISHED, AND IT CORRECTS r6538: the colourless claim holds for the global")
print("  bundles and fails for the three directions at a hinge.  Since the fermion")
print("  content is at the hinge, ** the candidate cannot be both colourless and")
print("  content-bearing on either reading. **")
print()
print("  NOT CLAIMED: that the candidate is dead.  What is shown is that item (2) and")
print("  the colourless property are in tension, that the tension is located at the")
print("  hinge index, and that the construction's own colourless locus -- the Z_3-fixed")
print("  axis -- is the one it says carries no wall.")

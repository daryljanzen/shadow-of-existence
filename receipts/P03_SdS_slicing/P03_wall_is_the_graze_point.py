"""
P03_wall_is_the_graze_point.py -- P3 sec:tour / P14 sec:chirality: the matter sector's WALL
identified with the throat point where the null legs graze.  Two independent derivations,
one set of three points, never before connected.

P14 reaches the wall loci from the signed radius: "r=0 is NOT the throat's CENTRE but a point
ON the throat circle -- the back, X_1 = -alpha, fixed relative to the hinge about which the
slicing plane swings ... the Z_3-fixed centre carries NO wall; the walls lie on the circle at
polar 180/300/60, a Z_3-orbit, EACH ANTIPODAL TO ITS HINGE."

Receipt P03_twelve_null_legs reaches the graze points from null tangency: the twelve legs
graze the throat at 60/180/300 degrees, each DIRECTLY BETWEEN two hinges, four legs apiece.

** VERIFIED IDENTICAL, and the pairing is exact: each wall is hinge k's back AND is the point
where the OTHER TWO hinges' null tangents touch the hole. **  So the wall of a hinge is where
the two adjacent hinges' tangent planes meet the throat, on the far side, at that hinge's
r = 0 -- and the hinge<->wall pairing is the ANTIPODAL map, hence canonical rather than
handedness-dependent.

** AND A HINGE'S OWN TWO NULL LEGS CROSS THE OTHER TWO HINGES' WALLS AND NEVER ITS OWN
(verified, 3 of 3). **  The 1+2 therefore appears a third time and now on walls, alongside the
designation 2+1 and the causal 2+1 -- evidence bearing on L-58.

WHAT IT DOES TO THE WINDING READING.  Receipt P03_thirds_from_closure derives the fractional
charges from a winding defined as the signed count of graze points a route crosses, and
registered as its antecedent (L-74) the question whether a matter field here is labelled by a
ROUTE at all.  ** Since the graze points ARE the walls, and a wall is exactly where prop:wall
binds a chiral zero-mode by Jackiw-Rebbi, a winding is a WALL-CROSSING COUNT -- which is the
natural label for a wall-bound field rather than an import. **  One lap = three wall crossings
= the whole Z_3 orbit; and each wall is an r = 0 point, the branch point the signed-radius flip
passes through and where the corpus places charge conjugation.

** WHAT IS NOT SHOWN. **  L-74 is NOT closed: what is established is that its antecedent is the
corpus's own structure, not that the zero-mode's label transforms as a crossing count -- that
is a computation on prop:wall's solution (L-76).  ** AND THIS SHARPENS RATHER THAN RELIEVES THE
WELD CONFLICT: P14 reads the three walls as the three GENERATIONS, the wall<->hinge pairing is a
bijection, and the fermion-sector reading needs the hinge three to be COLOUR.  Walls cannot be
both any more than hinges can, and they are the same three. **  L-67 stands, better specified.

ORIGIN: computations/baryon_edge/L75_the_wall_is_the_graze_point.py -- built r2376 (c54.23);
edit the origin, not this copy."""

import sympy as sp
from fractions import Fraction as F

print(__doc__.split("Run:")[0])
HINGE = {k: 120 * k for k in (0, 1, 2)}          # hinge azimuths, degrees

# =====================================================================
print("=" * 78)
print("PART 1 — THE WALLS FROM P14's SIDE:  r = 0 AT THE BACK, ANTIPODAL TO THE HINGE")
print("=" * 78)
print("  P14: the wall is where the signed areal radius flips -- r = 0 -- and r = 0 is NOT")
print("  the centre but a point ON the throat circle, 'the back, X_1 = -alpha, fixed")
print("  relative to the hinge about which the slicing plane swings'.")
print("  A hinge sits at azimuth th; its own 'back of the hole' is at th + 180.")
print()
wall_of = {k: (HINGE[k] + 180) % 360 for k in HINGE}
print(f"  {'hinge':>6} {'azimuth':>9} {'its wall (the back, r=0)':>26}")
for k in HINGE:
    print(f"  {k:>6} {HINGE[k]:>7} d {str(wall_of[k])+' d':>26}")
print()
print(f"  ⇒ the three walls, from P14: {sorted(wall_of.values())} degrees")
print("     -- 'a Z_3-orbit, each ANTIPODAL to its hinge', exactly as P14's header says.")
print("  ** AND NOTE WHICH POINT IS NOT A WALL: the Z_3-fixed centre carries none.  The")
print("     walls are on the circle, not at the middle. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE GRAZE POINTS FROM L-61's SIDE:  NULL TANGENCY")
print("=" * 78)
print("  Independently: from a puncture at hinge th, the substrate's two null rulings run")
print("  off and graze the throat at th - 60 and th + 60 (the hinge's left and right")
print("  tangents, verified exactly in L-61 / receipt P03_twelve_null_legs).")
print()
graze = set()
touches = {}
for k in HINGE:
    ts = sorted({(HINGE[k] - 60) % 360, (HINGE[k] + 60) % 360})
    touches[k] = ts
    graze |= set(ts)
    print(f"  hinge {k} at {HINGE[k]:>3} d  ->  its legs graze at {ts}")
print()
print(f"  ⇒ the graze points, from L-61: {sorted(graze)} degrees")
print("     -- and each lies DIRECTLY BETWEEN two hinges, with four of the twelve legs")
print("     meeting there (two rulings, each running both ways).")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — SAME SET.  AND THE PAIRING IS THE PART DARYL NAMED.")
print("=" * 78)
same = sorted(graze) == sorted(wall_of.values())
print(f"  P14's walls   : {sorted(wall_of.values())}")
print(f"  L-61's grazes : {sorted(graze)}")
print(f"  ** IDENTICAL: {same} **")
print()
print("  ** SO THE WALL IS THE GRAZE POINT.  Two derivations with nothing in common --")
print("     'r=0 is the back of the hole from this hinge' and 'this is where the null")
print("     generators through the punctures touch the throat' -- land on one set. **")
print()
print("  Now the pairing.  For each wall, WHICH hinges' tangents touch there?")
print()
print(f"  {'wall':>6} {'is the back of':>16} {'tangent to hinges':>20} {'the stated reading holds?':>26}")
ok_pair = True
for k in sorted(HINGE, key=lambda k: wall_of[k]):
    w = wall_of[k]
    tangent_hinges = sorted(h for h in HINGE if w in touches[h])
    adjacent = sorted(h for h in HINGE if h != k)
    good = tangent_hinges == adjacent
    ok_pair &= good
    print(f"  {str(w)+' d':>6} {'hinge '+str(k):>16} {str(tangent_hinges):>20} {str(good):>26}")
print()
print(f"  ** EVERY WALL: it is hinge k's back, AND it is where the OTHER TWO hinges'")
print(f"     tangents touch the hole.  {ok_pair} **")
print()
print("  ⇒ Daryl: 'the slicing planes of the TWO ADJACENT HINGES, aligned on the BACK SIDE")
print("     of the hole, where they TANGENT to the hole at r=0, AS DEFINED RELATIVE TO ONE")
print("     SPECIFIED HOLE.'  ** Every clause of that is verified, and the last clause is")
print("     the load-bearing one: the wall is a wall OF a hinge -- 'relative to one")
print("     specified hole' is not a hedge, it is the definition. **")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# THE CLAIM, ASSERTED.  The file computed verdict flags and only printed them.
#   · `same`: P14's walls (each hinge's back, th + 180) and L-61's graze points (th +- 60)
#     are ONE SET -- and it is the corpus's own set, pinned to 60/180/300 degrees
#     (INDEX: "the walls lie at polar 180/300/60"; "reaches 60/180/300 from null tangency").
#   · `ok_pair`: every wall is hinge k's back AND is where the OTHER TWO hinges' tangents
#     touch -- pinned on hinge 0, whose wall is 180 and whose own legs graze at 60 and 300.
assert sorted(wall_of.values()) == [60, 180, 300], \
    "the three walls must be the Z_3 orbit 60/180/300 degrees"
assert sorted(graze) == [60, 180, 300], \
    "the null legs must graze at 60/180/300 degrees"
assert same, "the wall set and the graze set must be identical"
assert wall_of[0] == 180 and touches[0] == [60, 300], \
    "hinge 0 at azimuth 0 must own the wall at 180 and graze at 60 and 300"
assert ok_pair, "each wall must be one hinge's back and tangent to the OTHER TWO hinges"
# -----------------------------------------------------------------------------------
print("  ** AND THE PAIRING IS CANONICAL, NOT A CHOICE. **  hinge <-> wall is the antipodal")
print("  map, so there is no handedness ambiguity in WHICH wall a hinge owns.  (A node")
print("  might have guessed the wall was one of the hinge's OWN two tangency points -- that")
print("  pairing WOULD have been handedness-dependent, and it is not the corpus's.)")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHOSE WALLS DOES A HINGE'S OWN NULL LEG CROSS?")
print("=" * 78)
owner = {w: k for k, w in wall_of.items()}
print(f"  {'hinge':>6} {'its legs graze at':>20} {'those walls belong to':>24} "
      f"{'own wall among them?':>21}")
never_own = True
for k in HINGE:
    ws = touches[k]
    owners = sorted(owner[w] for w in ws)
    hasown = k in owners
    never_own &= not hasown
    print(f"  {k:>6} {str(ws):>20} {'hinges '+str(owners):>24} {str(hasown):>21}")
print()
print(f"  ** A HINGE'S TWO NULL LEGS CROSS THE OTHER TWO HINGES' WALLS, AND NEVER ITS OWN:"
      f" {never_own} **")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 4's CLAIM, ASSERTED, with its own pin.  INDEX: "a hinge's own two null legs cross
# the other two hinges' walls and NEVER its own (3 of 3)".  Pinned on hinge 0: its legs
# graze at 60 and 300, which are the walls of hinges 2 and 1 -- never of hinge 0, whose
# wall is at 180.  `never_own` carries the same statement for all three.
assert never_own, "a hinge's own legs must never cross its own wall"
assert owner[60] == 2 and owner[300] == 1 and owner[180] == 0, \
    "the wall at 60 belongs to hinge 2, at 300 to hinge 1, at 180 to hinge 0"
assert sorted(owner[wv] for wv in touches[0]) == [1, 2], \
    "hinge 0's legs must cross exactly the walls of hinges 1 and 2"
# -----------------------------------------------------------------------------------
print("  ⇒ ** THE 1+2 APPEARS A THIRD TIME, AND NOW ON WALLS. **  The triple headed at a")
print("     puncture of hinge k reaches punctures at hinges j and l, through the walls of")
print("     hinges j and l, and never through k's own.  The designation 2+1, the causal")
print("     2+1 and this wall 2+1 are the same shape at three levels -- which is exactly")
print("     what L-58 asks about, and this is new evidence for it.")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THIS DOES TO L-74, THE GATE")
print("=" * 78)
print("  L-74 asked: 'is a matter field on this geometry labelled by a ROUTE -- an")
print("  equatorial path -- rather than by a point?'  It was registered as an exotic-")
print("  sounding requirement that the whole winding derivation hangs on.")
print()
print("  ** IT IS NOT EXOTIC.  The three points a route's winding counts ARE THE THREE")
print("     WALLS, and a wall is exactly where P14's prop:wall binds a chiral zero-mode. **")
print()
print(f"  {'quantity':>26} {'in L-73 (winding)':>26} {'in P14 (walls)':>26}")
for a, b, c in (("the three marked points", "graze points, 60/180/300", "walls, 180/300/60"),
                ("what sits there", "4 null legs meet", "one chiral zero-mode binds"),
                ("what r is there", "the throat, r = alpha", "r = 0 relative to its hinge"),
                ("the count", "crossings mod 3 = triality", "three walls = three generations"),
                ("one full lap", "3 crossings", "3 walls, the whole Z_3 orbit")):
    print(f"  {a:>26} {b:>26} {c:>26}")
print()
print("  ⇒ ** A CONSTITUENT'S WINDING IS ITS WALL-CROSSING COUNT. **  That is not a strange")
print("     label to hang on a field: for a field BOUND AT DOMAIN WALLS -- which is what")
print("     prop:wall makes it, by Jackiw-Rebbi -- the number of walls a path crosses is")
print("     the natural thing a path carries.")
print()
print("  ⇒ AND THE UNIT OF CHARGE GETS A READING.  One lap = three wall crossings = the")
print("     full Z_3 orbit; and each wall IS an r = 0 point (relative to its hinge), which")
print("     P14 calls the BRANCH POINT the signed-radius flip passes through, and which")
print("     the corpus places charge conjugation at.  ** So 'the electron's charge is one")
print("     complete lap' reads as 'three branch-point passages, one per wall'. **")
print()
print("  ** L-74 IS NOT CLOSED -- what is shown is that its antecedent is the corpus's own")
print("     structure rather than an import.  What remains is to show the zero-mode's")
print("     label transforms as a crossing count, which is a computation on prop:wall's")
print("     solution and not a naming exercise. **  (L-76.)")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — WHAT IS OWED, AND ONE THING THIS PUTS AT RISK")
print("=" * 78)
print("  ⌗ NEWLY CHEAP, because two structures are now on one point:")
print("    · L-62, THE SIGN TEST.  prop:wall gives each wall a chirality (a sigma_y")
print("      eigenvalue, the sign of the signed-radius flip, = R).  L-61 gives each graze")
print("      point a pair of legs at gnomonic angle +30 and -30.  ** They are now known to")
print("      be the SAME POINT, so the two signs can be compared directly. **")
print()
print("  ⌗ AND THE THING THIS PUTS AT RISK, STATED BECAUSE IT SHOULD BE:")
print("    ** P14 reads the three walls as the three GENERATIONS.  F-1 needs the three")
print("       hinges to be COLOUR.  The wall<->hinge pairing is ANTIPODAL AND CANONICAL")
print("       (PART 3), so walls and hinges are in bijection -- ** which means this does")
print("       NOT relieve the weld conflict; it sharpens it. **  Walls cannot be colour and")
print("       generation at once any more than hinges can, and they are the same three.")
print("    ⇒ L-67 is unchanged in force and better specified: the second three (the")
print("       turnaround roots, lem:twoturnings) must carry generation, and P14's")
print("       'which wall each binds at' would then be a COLOUR label, not a family one.")
print("    ** That is a substantial revision to P14's reading and it is NOT made here. **")
print()
print("  ⌗ AND WHAT DARYL ASKED THAT THIS DOES NOT ANSWER: he said the corpus has 'related")
print("  structures fitted together with geometric things that are shadows of one or the")
print("  other definition and have descriptive names and analytic definitions we've not")
print("  drawn identically to geometric features'.  ** This file draws ONE such pair")
print("  together.  The general audit -- every descriptive name against its geometric")
print("  locus -- is not done, and it is exactly the sweep that just paid. **  (L-77.)")

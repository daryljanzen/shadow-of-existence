"""
P14_leg_count_equals_arc_count.py -- P14 sec:chirality: the null legs and the equatorial arcs
deliver the SAME three monodromy operators, so the vantage reading of the wall
(P14_the_wall_is_a_wall_of_a_hinge) costs the corpus nothing; and the selection rule it yields
is the centre's, which is necessary for a colour singlet and not sufficient.

WHAT PROMPTED IT.  P14_the_wall_is_a_wall_of_a_hinge flagged a risk against itself: under the
vantage reading a mode is branched only at its own vantage's wall, while P03_wall_is_the_graze_
point found that a hinge's own null legs graze the OTHER TWO hinges' walls and never its own.
If the winding is read on the LEGS rather than on the equatorial ARCS, the legs looked
phase-free.

WHAT IS ESTABLISHED.
  1. THE LEG JOINING TWO HINGES GRAZES THE WALL OF THE THIRD.  Computed from the tangency rule
     of P03_twelve_null_legs (rulings from a puncture at theta graze at theta +- 60): the graze
     point shared by hinges a and b is the wall owned by the remaining hinge, for all three
     pairs.  Three legs, three walls, each leg opposite its wall.
  2. ** AND THAT IS P03_wall_is_the_graze_point's PART 4 SEEN FROM THE OTHER SIDE, NOT IN
     TENSION WITH IT: hinge a's own legs are a-b and a-c and graze walls c and b, never a,
     because the leg grazing wall a is b-c -- the one that does not touch hinge a at all. **
  3. THE CROSS-CHECK, AGAINST A COUNT DERIVED WITHOUT THIS RULE.  Each hinge carries two
     punctures, so the legs between a given pair of hinges number 2 x 2 = 4, and (1) sends all
     four to one wall: 12 = 3 x 4, reproducing P03_twelve_null_legs' "twelve legs, three graze
     points, four apiece" exactly.
  4. ** THE RECONCILIATION, AND THE DEBT IS DISCHARGED. **  Each leg meets exactly one wall; the
     three legs meet the three walls once each; one equatorial lap meets the three walls once
     each.  Same three diagonal operators, same product, and the closed bound triple
     0 -> 1 -> 2 -> 0 acts by omega^(-lambda) times the identity -- asserted central, det 1.
  5. ** AND THE APPARENT PROBLEM IS THE CONTENT.  That a vantage-a mode is unbranched on hinge
     a's own legs means the constituent at hinge a is labelled by the leg it is NOT on -- the
     opposite side of the triangle.  A label a state cannot read locally is precisely
     "route-labelled rather than point-labelled" (P14_route_or_point), and it is why the label
     is unobservable on one constituent and observable only on the closed triple. **
  6. ** A READING REFUTED BY ITS OWN TABLE, RECORDED BECAUSE IT WAS ABOUT TO BE WRITTEN. **  The
     tempting statement is "the singlets are exactly the one-per-hinge triple and the conjugate
     pair".  The table says otherwise: two constituents on one hinge and one on another is also
     triality-zero, because the triality sum counts the NUMBER of constituents mod 3 and is
     blind to their distribution over vantages.  ** That is not a defect of the geometry -- it
     is what a centre is, and QCD's Z_3 has the identical property, giving N_q - N_qbar = 0
     mod 3 and nothing finer.  Triality zero is NECESSARY for a singlet and NOT SUFFICIENT. **
  7. SO THE TWO CONDITIONS COME FROM TWO UNRELATED PLACES AND ARE COMPLEMENTARY, NEITHER DOING
     THE OTHER'S WORK: the centre's rule from the monodromy above, and one-puncture-per-hinge
     from P03_hexagon_null_triple's causal trichotomy alone.  Together: a bound triple is one of
     each colour and the count closes mod 3.  Sufficiency needs the SU(3) INVARIANTS, which
     P14_the_wall_is_a_wall_of_a_hinge has only just made available; not done here.
  8. ** AND AN ARGUMENT FOR THE VANTAGE READING THAT USES NEITHER M NOR THE VANTAGE-ROTATION
     STEP. **  One shared radius would vanish at all three walls, making every wall a wall of
     every hinge -- which makes vacuous the hinge<->wall bijection P03_wall_is_the_graze_point
     verified wall by wall as "the ANTIPODAL map, canonical, not a choice".  The M = 0
     embedding computation remains the constructive argument; the fork no longer rests on it
     alone, and the two arguments have nothing in common.

** WHAT IS STILL OWED, AND ITS STAKES ARE NOW LOWER RATHER THAN GONE: r on the slicing curve at
M != 0.  The constructive exhibit of the three radii is still an M = 0 exhibit. **

** AND THE FRONTIER IS UNCHANGED AND NOW ALONE: THERE IS NO CURVATURE.  The bundle is flat with
finite holonomy; the rank, the grading, the group and the selection rule are all holonomy, and
holonomy quantises.  A force needs curvature, and P14_quantisation_not_strength said in advance
that the geometry would not supply one. **

ORIGIN: computations/baryon_edge/L128b_leg_and_arc.py -- built r2376 (c54.53); edit the origin,
not this copy."""
import sympy as sp
import itertools

print(__doc__.split("Run:")[0])

w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
I3 = sp.eye(3)
hinge = {j: 120 * j for j in range(3)}
wall = {j: (120 * j + 180) % 360 for j in range(3)}
owner = {v: k for k, v in wall.items()}

# =====================================================================
print("=" * 78)
print("PART 1 — WHICH WALL EACH LEG GRAZES")
print("=" * 78)
print("  `L-61` (receipt P03_twelve_null_legs): from a puncture at hinge theta the substrate's")
print("  two null rulings graze the throat at theta - 60 and theta + 60.  So for the leg joining")
print("  hinge a to hinge b, take the graze point lying on the arc BETWEEN them:")
print()
print(f"  {'leg':>10} {'grazes at':>11} {'that wall belongs to':>21} {'third hinge?':>13}")
leg_wall = {}
for a, b in itertools.combinations(range(3), 2):
    cands = {(hinge[a] - 60) % 360, (hinge[a] + 60) % 360} & \
            {(hinge[b] - 60) % 360, (hinge[b] + 60) % 360}
    assert len(cands) == 1, "each hinge pair must share exactly one graze point"
    g = cands.pop()
    c = owner[g]
    third = ({0, 1, 2} - {a, b}).pop()
    leg_wall[(a, b)] = c
    print(f"  {str((a,b)):>10} {g:>11} {('hinge %d' % c):>21} {str(c == third):>13}")
assert all(leg_wall[(a, b)] == ({0, 1, 2} - {a, b}).pop()
           for a, b in itertools.combinations(range(3), 2))
print()
for s in [
 "** THE LEG JOINING TWO HINGES GRAZES THE WALL OF THE THIRD.  Verified, and it is a bijection:",
 "   three legs of the triangle, three walls, each leg opposite its wall. **",
 "",
 "⌗ AND THAT IS EXACTLY `L-75` PART 4 SEEN FROM THE OTHER SIDE, NOT IN TENSION WITH IT.  `L-75`",
 "   found 'a hinge's own two legs graze the OTHER TWO hinges' walls and never its own'.  Hinge",
 "   a's legs are a-b and a-c, grazing walls c and b -- ** never a, because the leg that grazes",
 "   wall a is b-c, the one that does not touch hinge a at all. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CROSS-CHECK AGAINST `L-61`'s INDEPENDENT COUNT")
print("=" * 78)
print("  `L-61` counted the null legs from the substrate's ruling structure and found TWELVE,")
print("  meeting the throat at THREE points, ** FOUR APIECE **.  PART 1 predicts that count")
print("  without using it: each hinge carries TWO punctures (X_0 = +-sqrt(3) alpha), so the legs")
print("  between hinges a and b number 2 x 2 = 4, and PART 1 sends all four to one wall.")
print()
print(f"  {'wall':>6} {'owner':>7} {'legs run between':>18} {'count':>6} {'`L-61` says':>12}")
tot = 0
for c in range(3):
    a, b = sorted({0, 1, 2} - {c})
    n = 2 * 2
    tot += n
    print(f"  {wall[c]:>6} {('hinge %d' % c):>7} {('hinges %d-%d' % (a, b)):>18} {n:>6} {4:>12}")
print(f"  {'':>6} {'':>7} {'TOTAL':>18} {tot:>6} {12:>12}")
assert tot == 12
print()
print("  ** 12 = 3 x 4, matching `L-61` exactly, from a rule `L-61` did not use. **  The")
print("  leg-to-wall assignment is therefore not a convenient labelling: it reproduces the")
print("  corpus's own independently-derived multiplicity.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE RECONCILIATION")
print("=" * 78)
lam = sp.Symbol('lambda', integer=True)


def diag_at(c, L):
    """monodromy acting on the rank-3 vantage bundle when wall c is encircled"""
    d = [1, 1, 1]
    d[c] = sp.simplify(w**(-L))
    return sp.diag(*d)


print("  Under reading (ii) a mode is branched only at its OWN vantage's wall.  So:")
print()
print(f"  {'object':>26} {'walls met':>14} {'operator on the rank-3 bundle':>32}")
for a, b in itertools.combinations(range(3), 2):
    c = leg_wall[(a, b)]
    M = diag_at(c, 1)
    print(f"  {('leg %d-%d' % (a, b)):>26} {('wall %d' % wall[c]):>14} "
          f"{('diag' + str(tuple(sp.nsimplify(M[k,k]) for k in range(3)))):>32}")
print(f"  {'one equatorial lap':>26} {'all three':>14} "
      f"{'the product of all three':>32}")
print()
prod = sp.simplify(diag_at(0, 1) * diag_at(1, 1) * diag_at(2, 1))
scal = sp.simplify(prod[0, 0])
print(f"  closed bound triple  0 -> 1 -> 2 -> 0  traverses all three legs:")
print(f"     product = {sp.nsimplify(scal)} * I    central: "
      f"{sp.simplify(prod - scal*I3) == sp.zeros(3)}    det = {sp.simplify(sp.det(prod))}")
print()
for s in [
 "⇒ ** THE LEG COUNT AND THE ARC COUNT ARE THE SAME COUNT, AND THE DEBT IS DISCHARGED. **  Each",
 "   leg meets exactly one wall; the three legs meet the three walls once each; one equatorial",
 "   lap meets the three walls once each.  ** Same three operators, same product, same centre. **",
 "",
 "⌗ AND THE THING THAT LOOKED LIKE A PROBLEM IS THE CONTENT.  `L-128` worried that a vantage-a",
 "   mode is unbranched on hinge a's own legs.  ** That is right, and what it means is that the",
 "   constituent at hinge a is labelled by the leg it is NOT on -- the opposite side of the",
 "   triangle. **  A label a state cannot read locally is exactly what 'route-labelled rather",
 "   than point-labelled' says (`L-74`), and it is why the label is unobservable on one",
 "   constituent and observable only on the closed triple.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE SELECTION RULE DOES AND DOES NOT REACH")
print("=" * 78)
for s in [
 "P14's `P03_hexagon_null_triple` already forces the shape of a bound object, from causality",
 "alone: 'the causal classification of the six hinge-ends forces such a triple to take ONE",
 "PUNCTURE PER HINGE -- two ends of one hinge are timelike separated, two on one horn spacelike,",
 "and only the cross pairs null.'  ** Under (ii), one puncture per HINGE is one constituent per",
 "VANTAGE, and a vantage is a colour.  So a bound triple is one of each colour by a fact about",
 "light cones, not by a colour rule. **  What does its triality come to?",
]:
    print("  " + s)
print()
print(f"  {'configuration':>34} {'vantages':>12} {'total triality (mod 3)':>24} {'singlet?':>9}")
cases = [
    ("bound triple, one per hinge", [(+1, 0), (+1, 1), (+1, 2)]),
    ("two constituents (same lambda)", [(+1, 0), (+1, 1)]),
    ("one constituent alone", [(+1, 0)]),
    ("constituent + its R-conjugate", [(+1, 0), (-1, 0)]),
    ("constituent + conjugate, diff. vantage", [(+1, 0), (-1, 1)]),
    ("three constituents, two on one hinge", [(+1, 0), (+1, 0), (+1, 1)]),
]
res = {}
for nm, members in cases:
    tot_t = sum(sgn * (-1) for sgn, v in members)          # triality = -lambda per unit lambda
    sing = (tot_t % 3) == 0
    res[nm] = sing
    print(f"  {nm:>34} {str([v for _, v in members]):>12} "
          f"{('%d lambda' % tot_t):>24} {str(sing):>9}")
print()
for s in [
 "⚠⚠ ** AND THE LAST ROW IS THE ONE THAT MATTERS, BECAUSE IT REFUTES THE READING I WAS ABOUT TO",
 "   WRITE. **  I was going to say 'the singlets are exactly the one-per-hinge triple and the",
 "   conjugate pair'.  ** The table says otherwise: TWO CONSTITUENTS ON ONE HINGE AND ONE ON",
 "   ANOTHER also comes out triality-zero -- because the triality sum counts the NUMBER of",
 "   constituents mod 3 and is blind to how they are distributed over the vantages. **",
 "",
 "⌗ ** THAT IS NOT A DEFECT OF THE GEOMETRY; IT IS WHAT THE CENTRE IS, AND QCD HAS EXACTLY THE",
 "   SAME PROPERTY. **  The Z_3 centre gives N_q - N_qbar = 0 mod 3 and nothing finer: it does",
 "   not distinguish (r,g,b) from (r,r,g).  ** Triality zero is NECESSARY for a singlet and not",
 "   SUFFICIENT, in QCD and here alike, and reading the monodromy as delivering singlet-ness",
 "   would have been a real overclaim. **",
 "",
 "⇒ ** SO THE CORRECT STATEMENT IS THAT THE GEOMETRY SUPPLIES THE TWO CONDITIONS SEPARATELY,",
 "   FROM TWO UNRELATED PLACES, AND THEY ARE COMPLEMENTARY RATHER THAN ONE ENTAILING THE OTHER: **",
 "     * the CENTRE's rule, N = 0 mod 3, from the monodromy computed above;",
 "     * ONE PUNCTURE PER HINGE, from `P03_hexagon_null_triple`'s CAUSAL trichotomy alone.",
 "   ** Together those are 'a bound triple is one of each colour, and the count closes mod 3' --",
 "   the baryon -- with the meson coming from R carrying 3 to 3-bar.  Neither condition was put",
 "   in for the other, and neither is doing the other's work. **",
 "",
 "⌗ AND WHAT IS NOW AVAILABLE THAT WAS NOT BEFORE, NAMED RATHER THAN CLAIMED: sufficiency needs",
 "   the SU(3) INVARIANTS -- epsilon_abc and delta -- and `L-128` has just supplied SU(3) as the",
 "   structure group.  ** The one-per-hinge triple is precisely the epsilon_abc contraction over",
 "   the three vantages, which is a computation that could not even be posed before this pair of",
 "   leads and can be posed now. **  It is not done here.",
 "",
 "⚠ ** AND THE STANDING BOUND IS NOT WAIVED: AN IRREP IS NOT A STATE, AND A SELECTION RULE IS",
 "   NOT A DYNAMICS. **  That the geometry BINDS these configurations is not shown and is not",
 "   claimed; there is still no curvature and hence no force.  The geometry supplies the rule",
 "   and not the interaction -- `L-125` again, one level up.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — DEBT (1), AND THERE IS AN ARGUMENT THAT DOES NOT DEPEND ON M AT ALL")
print("=" * 78)
for s in [
 "`L-128` settled the fork by computing r_j = alpha sin(phi - theta_j) at M = 0 and evaluating it",
 "at the three walls.  ** That argument has two soft joints -- the vantage-rotation reading, and",
 "M = 0 -- and there is a third argument with neither. **",
 "",
 "⌗ ** READING (i) CONTRADICTS A BIJECTION `L-75` ALREADY VERIFIED. **  Reading (i) says one",
 "radius vanishes at all three walls.  If it did, every wall would be a wall of every hinge --",
 "and `L-75` PART 3 checked, wall by wall, that ** each wall is the back of exactly ONE hinge,",
 "the pairing being the ANTIPODAL map, 'canonical, not a choice'. **  A single shared radius",
 "makes that pairing vacuous: there would be nothing to pair, because every hinge would own",
 "every wall.",
 "",
 "⇒ ** SO (i) IS UNAVAILABLE FOR A REASON THAT USES NEITHER M NOR THE VANTAGE-ROTATION STEP:",
 "   the corpus's own hinge<->wall bijection is inconsistent with one shared radius. **  The",
 "   M = 0 evaluation of `L-128` remains as the CONSTRUCTIVE argument -- it exhibits the three",
 "   radii and their zero sets -- but the fork no longer rests on it alone.",
 "",
 "⌗ *And the two arguments have nothing in common: one is an embedding computation, the other is",
 "a combinatorial fact about a verified pairing.  Their agreement is worth more than either.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — WHAT IS LEFT")
print("=" * 78)
for s in [
 "① ** STILL OWED, AND NOT DISCHARGED BY ANYTHING ABOVE: r on P3's slicing curve at M != 0. **",
 "   PART 5 removes the fork's dependence on it, but the CONSTRUCTIVE picture -- the three radii",
 "   as actual functions on an actual cut -- is still an M = 0 exhibit.  ** Lower stakes now, and",
 "   it should be said that they are lower rather than quietly dropped. **",
 "",
 "② ** THE REAL FRONTIER IS UNCHANGED AND IS NOW ALONE: THERE IS NO CURVATURE. **  The bundle is",
 "   flat with finite holonomy.  Everything this pair of leads has produced -- the rank, the",
 "   grading, the group, the selection rule -- is holonomy, and holonomy quantises.  ** A force",
 "   needs curvature, the geometry has not supplied one, and `L-125` said in advance that it",
 "   would not. **  That is now the whole of the gap between this and colour.",
 "",
 "③ *And one thing this stretch has earned the right to say plainly:* ** the corpus's colour is",
 "   the CENTRE and its structure group, reached three independent ways -- the winding's Z_3, the",
 "   pushforward's holonomy, and the vantage triple's selection rule -- and each time the thing",
 "   that arrives is a discrete label and the thing that does not is a coupling. **  Three routes",
 "   agreeing on both halves is stronger evidence about where the boundary sits than any one of",
 "   them was about its own half.",
]:
    print("  " + s)

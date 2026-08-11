#!/usr/bin/env python3
"""
L-73 — THE THIRDS ARE NOT MATCHED, THEY ARE DERIVED.  And the three triality classes come
out as quark / antiquark / lepton, from the geometry's own closure condition.

c54.21 registered "a constituent's fractional charge IS its equatorial arc" as L-70, THE
load-bearing identification, and said it was not made.  ** This file makes the definition
precise and then finds that the thirds are FORCED rather than assigned. **

  THE DEFINITION.  The three graze points sit on the throat at 60/180/300 degrees -- one
  directly between each pair of hinges (L-61, verified).  They cut the throat circle into
  three equal arcs.  ** Define a constituent's WINDING as the signed number of graze points
  its equatorial route crosses, in units of one third of a lap. **  Nothing else is needed:
  the graze points are the only marked points on the throat, and there are exactly three of
  them because there are exactly three hinges.

  PART 1  The two routes between two punctures, and why they differ by exactly one lap.
  PART 2  The six triples: 3 upper-headed, 3 lower-headed, exchanged by T.
  PART 3  ** THE DERIVATION. **  Impose only (i) the two routes differ by one lap and
          (ii) BOTH horn-families close.  Solve.  The thirds fall out.
  PART 4  The three solution classes, and what they are.
  PART 5  T costs exactly one lap -- checked on the totals, not asserted.
  PART 6  What this fixes in THE_FERMION_SECTOR_GEOMETRY, including a correction to F-6.
  PART 7  What is still not established.

Run: python3 L73_thirds_derived_from_closure.py     (sympy)
"""

from fractions import Fraction as F
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE TWO ROUTES, AND WHY THEY DIFFER BY EXACTLY ONE LAP")
print("=" * 78)
print("  Hinges at azimuth 0, 120, 240.  Graze points at 60, 180, 300 -- ONE directly")
print("  between each pair of hinges, and there are three of them because there are three")
print("  hinges.  They cut the throat circle into three equal arcs of 120 degrees.")
print()
print("  Between two punctures at different hinges there are exactly TWO equatorial routes:")
print()
print(f"  {'from':>6} {'to':>6} {'route':>10} {'graze points crossed':>34} {'thirds':>8}")
graze = {60: 'g(0|120)', 180: 'g(120|240)', 300: 'g(240|0)'}
def crossings(a, b, sense):
    """graze points strictly between azimuth a and b travelling in `sense` (+1 ccw)."""
    out, x = [], a
    while True:
        x = (x + sense) % 360
        if x in graze:
            out.append(graze[x])
        if x == b % 360:
            return out
for (a, b) in ((0, 120), (0, 240)):
    for sense, nm in ((1, 'the short'), (-1, 'the long')):
        cr = crossings(a, b, sense)
        lbl = 'forward' if sense == 1 else 'backward'
        print(f"  {a:>6} {b:>6} {lbl:>10} {str(cr):>34} {sense*len(cr):>+8}")
print()
print("  ** THE TWO ROUTES BETWEEN THE SAME PAIR CROSS 1 AND 2 GRAZE POINTS, IN OPPOSITE")
print("     SENSES -- so their windings are +2 and -1 thirds, or +1 and -2. **")
d1 = F(2, 3) - F(-1, 3)
d2 = F(1, 3) - F(-2, 3)
print(f"     (+2/3) - (-1/3) = {d1}      (+1/3) - (-2/3) = {d2}")
print("  ** IN EITHER CASE THE TWO ROUTES DIFFER BY EXACTLY ONE FULL LAP, because together")
print("     they cross all three graze points: 1 + 2 = 3. **")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 1's CLAIM, ASSERTED.  The three graze points are at 60/180/300 degrees, one directly
# between each pair of hinges (0/120/240) -- INDEX: "the three graze points sit at
# 60/180/300 deg".  The loop's last route is 0 -> 240 travelled BACKWARD, which crosses
# exactly ONE graze point, g(240|0); its forward partner crossed TWO.  1 + 2 = 3, so the
# two routes differ by exactly one lap -- and that is what d1 and d2 must each equal.
assert sorted(graze) == [60, 180, 300], \
    "the graze points must sit at 60/180/300 degrees, one between each pair of hinges"
assert cr == ['g(240|0)'] and sense == -1 and len(cr) == 1, \
    "the backward route from 0 to 240 must cross exactly one graze point"
assert d1 == 1 and d2 == 1, "the two routes between one pair must differ by exactly ONE lap"
# -----------------------------------------------------------------------------------
print("  ⇒ Daryl: 'the 1/3 vs 2/3 of the equator, i.e. 120 vs 240 ... they're even the")
print("     opposite direction.'  ** The 1/3 and the 2/3 are ONE PAIR OF PUNCTURES joined")
print("     the two ways round, and the lap is the difference. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE SIX TRIPLES, AND HOW THE HORN SPLITS THEM")
print("=" * 78)
print("  A triple is a puncture (the HEAD) plus the two punctures its null legs reach,")
print("  both on the OPPOSITE horn (L-61, verified).  Six punctures, six triples:")
print()
print(f"  {'head':>6} {'horn':>6} {'partners':>14} {'shape':>10}")
triples = []
for k in (0, 1, 2):
    triples.append((f"U{k}", 'upper', [f"D{(k+1)%3}", f"D{(k+2)%3}"]))
    triples.append((f"D{k}", 'lower', [f"U{(k+1)%3}", f"U{(k+2)%3}"]))
for h, horn, ps in triples:
    print(f"  {h:>6} {horn:>6} {str(ps):>14} {'1 + 2':>10}")
print()
print("  ** THREE UPPER-HEADED AND THREE LOWER-HEADED, and T (X0 -> -X0) exchanges the two")
print("     families.  Within a family the three are related by the station rotation --")
print("     i.e. by sigma, which F-1 reads as COLOUR: they are three colour labels of one")
print("     object, not three different objects. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE DERIVATION.  Two constraints, nothing else.")
print("=" * 78)
print("  Let the HEAD of a triple carry winding x and each PARTNER carry y, in laps.")
print("  Impose ONLY what the geometry supplies:")
print()
print("    (i)  x - y = 1        the head and a partner are joined by the two routes,")
print("                          which differ by exactly one lap  (PART 1)")
print("    (ii) x + 2y in Z      the upper-headed triple CLOSES  (an admissible object is")
print("                          a closed lap -- P3 sec:lap)")
print("    (iii) y + 2x in Z     the lower-headed triple closes too; the horns are")
print("                          perfectly symmetric, so both families must be admissible")
print()
x = sp.Symbol('x', rational=True)
up = sp.simplify(x + 2 * (x - 1))
lo = sp.simplify((x - 1) + 2 * x)
print(f"  substituting y = x - 1:")
print(f"     upper-headed total  x + 2y = {up}")
print(f"     lower-headed total  y + 2x = {lo}")
print()
print("  Both are integers  <=>  3x - 2 in Z  and  3x - 1 in Z  <=>  ** 3x in Z **")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 3's CLAIM, ASSERTED -- the derivation the whole receipt turns on.  Substituting
# y = x - 1 into the two closure conditions must give EXACTLY 3x - 2 and 3x - 1, so that
# both lie in Z iff 3x does (INDEX: "the totals are 3x-2 and 3x-1, integers iff 3x is.
# SO x = k/3").  Both are exact symbolic identities in the rational symbol x.
assert sp.simplify(up - (3*x - 2)) == 0, "the upper-headed total must be exactly 3x - 2"
assert sp.simplify(lo - (3*x - 1)) == 0, "the lower-headed total must be exactly 3x - 1"
assert sp.simplify(lo - up) == 1, "the two totals must differ by exactly one lap"
# -----------------------------------------------------------------------------------
print("  ⇒ ** x = k/3 FOR SOME INTEGER k.  THE THIRDS ARE FORCED. **")
print()
print("  ** AND THE REASON IS VISIBLE IN THE ALGEBRA: the 3 is the number of constituents")
print("     in the triple, which is the number of HINGES, which is the number of GRAZE")
print("     POINTS.  One 3, entering three ways, and it is the corpus's own. **")
print()
print("  ⚠ NOTE WHAT WAS NOT ASSUMED.  No quark charge was put in.  No Standard Model")
print("  number appears in (i), (ii) or (iii).  ** The only inputs are: a triple has three")
print("  members split 1+2 by horn; the two routes differ by one lap; and an admissible")
print("  object closes. **  All three are geometry established elsewhere in this corpus.")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE SOLUTION CLASSES, AND WHAT THEY TURN OUT TO BE")
print("=" * 78)
print("  x = k/3.  Adding a whole lap to x and y together is a relabelling (it shifts both")
print("  and preserves both constraints), so the distinct classes are k mod 3:")
print()
print(f"  {'k mod 3':>8} {'x (head)':>10} {'y (partner)':>13} {'upper total':>12} "
      f"{'lower total':>12} {'triality':>9} {'this is':>14}")
names = {0: 'LEPTONIC', 2: 'QUARKS', 1: 'ANTIQUARKS'}
for k in (0, 2, 1):
    xv = F(k, 3)
    yv = xv - 1
    print(f"  {k:>8} {str(xv):>10} {str(yv):>13} {str(xv + 2*yv):>12} "
          f"{str(yv + 2*xv):>12} {str(F(k,3) % 1):>9} {names[k]:>14}")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 4's CLAIM, ASSERTED.  The loop's last class is k = 1, the ANTIQUARKS:
# (x, y) = (+1/3, -2/3), with upper total 1/3 + 2(-2/3) = -1 and lower total
# -2/3 + 2(1/3) = 0 -- BOTH INTEGERS, which is what closure demands, and the triality
# label is 1/3.  (INDEX: "k=1 gives (+1/3,-2/3) = the antiquarks".)
assert (xv, yv) == (F(1, 3), F(-2, 3)), "the k=1 class must be (x, y) = (+1/3, -2/3)"
assert xv + 2*yv == F(-1) and yv + 2*xv == F(0), \
    "both totals of the k=1 class must be whole laps"
# -----------------------------------------------------------------------------------
print("  ** EXACTLY THREE CLASSES, AND THEY ARE THE THREE TRIALITY CLASSES. **")
print("     k = 2 : (x, y) = (+2/3, -1/3)   ** = (u, d) **")
print("     k = 1 : (x, y) = (+1/3, -2/3)   ** = (dbar, ubar) -- the same solution under")
print("                                        overall sign reversal, which is C **")
print("     k = 0 : (x, y) = (0, -1)        ** triality zero: nu and e, and every colour")
print("                                        singlet **")
print()
u_, d_ = F(2, 3), F(-1, 3)
print("  ⇒ ** THE GEOMETRY DOES NOT MATCH THE QUARK CHARGES.  IT PRODUCES THEM, AS THE")
print("     k = 2 MEMBER OF A THREE-ELEMENT SOLUTION SET WHOSE OTHER TWO MEMBERS ARE THE")
print("     ANTIQUARKS AND THE LEPTONS. **")
print()
print("  And the k = 1 and k = 2 classes are exchanged by overall sign -- which is charge")
print("  conjugation, and which the corpus already places at r = 0 and field-level.  ** So")
print("  'quark or antiquark' is a RELATIVE designation in exactly the sense Daryl has")
print("  insisted on throughout: the two classes are one solution read two ways. **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — T COSTS EXACTLY ONE LAP.  Checked on the totals.")
print("=" * 78)
print("  Take the physical class k = 2, x = +2/3, y = -1/3:")
print()
up_tot = u_ + 2 * d_
lo_tot = d_ + 2 * u_
print(f"    upper-headed triple  (u, d, d)  total charge = {up_tot}")
print(f"    lower-headed triple  (d, u, u)  total charge = {lo_tot}")
print(f"    difference under T                          = {lo_tot - up_tot}")
print()
one_lap = (lo_tot - up_tot) == 1
print(f"  ** T CHANGES THE TOTAL BY EXACTLY ONE LAP: {one_lap} **")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 5's CLAIM, ASSERTED.  The file computed the verdict flag `one_lap` and only printed
# it.  On the physical class (u, d) = (+2/3, -1/3) the upper-headed triple udd totals
# EXACTLY 0 and the lower-headed duu totals EXACTLY +1 -- the nucleon doublet -- so T costs
# exactly one lap, which is L-71's answer 1 rather than 0 or 2.
assert (u_, d_) == (F(2, 3), F(-1, 3)), "the physical class must be (u, d) = (+2/3, -1/3)"
assert up_tot == 0 and lo_tot == 1, "udd must total 0 and duu must total +1"
assert one_lap, "T must change the total by exactly one lap"
# -----------------------------------------------------------------------------------
print("  ⇒ ** udd of total charge 0 and duu of total charge +1, exchanged by the horn")
print("     swap.  That is the NUCLEON DOUBLET, and T is the operator that moves along it")
print("     at a cost of exactly one unit -- which is what the W carries. **")
print("  ⇒ and there are THREE of each because there are three hinges: ** three colour")
print("     labels of one doublet, not six objects. **  (F-1 and F-2 meet here.)")
print()
print("  ⚠ L-71 ASKED WHETHER T MOVES THE WINDING BY 0, 1 OR 2 LAPS, and said two of the")
print("  three answers refute F-2.  ** The answer is 1, on the totals.  F-2 survives its")
print("  own stated refutation test. **")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — WHAT THIS FIXES, INCLUDING A CORRECTION TO F-6")
print("=" * 78)
print("  ⌗ L-70 (the load-bearing identification) MOVES.  It was 'is fractional charge the")
print("  equatorial arc?'  ** With winding defined as signed graze-point crossings, the")
print("  thirds are DERIVED rather than identified (PART 3), so the question is no longer")
print("  whether the arithmetic can be matched. **  What remains is narrower and stateable:")
print("  ** does a constituent CARRY a route, i.e. is a matter field on this geometry")
print("  labelled by an equatorial path rather than by a point? **  (L-74.)")
print()
print("  ⌗ F-6 IS CORRECTED.  It said leptons are AXIAL -- 'no azimuth, hence no third'.")
print("  ** That was too strong and PART 4 gives the right statement: a lepton is the")
print("  triality-ZERO class, i.e. its winding is a WHOLE NUMBER OF LAPS. **  It need not")
print("  be off the equator; it must be COMPLETE on it.")
print("     e-  : winding -1  -- exactly one lap, and the lap is the one through r = 0")
print("     nu  : winding  0  -- no lap at all")
print("  ** And colourlessness is then not a separate fact: triality zero IS colour")
print("     neutrality, and a complete winding is what triality zero means. **")
print("  ⚠ AND THE HONEST RESIDUE: this says leptons occupy the k = 0 class; it does not")
print("  say why that class holds exactly TWO low-lying states rather than a tower.")
print("  ** L-69 stands, narrowed: why is the lepton doublet {0, -1} and not {0,-1,-2,...}? **")
print()
print("  ⌗ AND THE QUANTISATION OF CHARGE IS NOW A STATEMENT WITH A REASON.")
print("  ** Charge comes in thirds because a bound object has three constituents, one per")
print("     hinge, and the equator carries three graze points -- and the electron's unit is")
print("     one complete lap, which is three thirds. **  The 1/3 is the corpus's 3.")

# =====================================================================
print()
print("=" * 78)
print("PART 7 — WHAT IS STILL NOT ESTABLISHED, STATED WITHOUT SMOOTHING")
print("=" * 78)
for s in [
  "(a) that a matter field on this geometry is labelled by a ROUTE at all.  PART 3 shows",
  "    that IF constituents carry windings and bound objects close, the thirds follow.",
  "    ** It does not show the antecedent. **  That is L-74 and it is now the gate.",
  "(b) that closure is a REQUIREMENT and not merely a property the vacuum slicing has.",
  "    ** L-72, unchanged and still the load-bearer under confinement. **",
  "(c) the WELD.  If the hinge three is colour it is not also generations, and",
  "    COMBINATORICS L8.1-a welds them.  ** L-67, first-rank, and it reaches the",
  "    dimension result's fold step. **  Nothing here touches it.",
  "(d) why the k = 0 class holds two states (L-69, narrowed above).",
  "(e) the continuous SU(3).  ** Nothing here reaches it. **  What PARTS 3-4 supply is",
  "    the DISCRETE part -- triality, the singlet rule, the thirds -- which is exactly",
  "    the position the corpus already accepts for charge (L-68).",
]:
    print("  " + s)
print()
print("  ** AND THE ONE THING THAT SHOULD BE SAID PLAINLY: the derivation in PART 3 uses no")
print("     Standard Model input.  Three constraints, all geometry, and the quark charges")
print("     come out as one of exactly three classes.  ** That is a forced structural")
print("     relationship of the kind this programme exists to demonstrate. **")

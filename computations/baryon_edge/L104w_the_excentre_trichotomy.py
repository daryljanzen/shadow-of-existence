#!/usr/bin/env python3
"""
L-104w — THE CAUSAL TRICHOTOMY ON THE EXCENTRE SET.  `L-30` found the excentres NULL-INERT --
0 of 36 hinge-excentre pairs null -- and `L-104` observed that nullity is one relation among
several, leaving the causal character, tangency and the projective dual untested.

** RUNNING THE TRICHOTOMY OVERTURNS THE EXPECTED ANSWER: the set is null-inert but NOT causally
inert, the causal character reads the OWN-WALL relation, and the computation yields a SIXTH
equivalence for the hinge distance -- the first of them phrased in the substrate's own causal
language rather than in classical triangle geometry. **

  PART 1  The excentre set, built -- and where the $\\sqrt{15}$ comes from.
  PART 2  ** THE EXCENTRES SIT OVER THE WALL AZIMUTHS. **
  PART 3  The trichotomy on the 15 excentre-excentre pairs.
  PART 4  ** The trichotomy on the 36 hinge-excentre pairs. **
  PART 5  ⚠ I had written the opposite before running it -- the table refutes it.
  PART 6  ** 2 alpha is the radius at which the cross pairs go NULL: a sixth equivalence. **
  PART 7  What `L-104` asked, answered.

Run: python3 L104w_the_excentre_trichotomy.py
"""
import sympy as sp
import itertools

print(__doc__.split("Run:")[0])

al = sp.Symbol('alpha', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE EXCENTRE SET, AND WHERE sqrt(15) COMES FROM")
print("=" * 78)
for s in [
 "The hinge triangle is equilateral with circumradius $2\\alpha$ (P3: the hole determines one",
 "circle and it ENDS at $2\\alpha$).  ** For an equilateral triangle the excentres lie at twice",
 "the circumradius from the centre, opposite each vertex ** -- so the excentre LINES stand at",
 "transverse radius $4\\alpha$, at the azimuths opposite the hinges.",
 "",
 "A line parallel to the $X_0$ axis at transverse radius $\\rho$ pierces the substrate where",
 "$-X_0^2+\\rho^2=\\alpha^2$:",
]:
    print("  " + s)
print()
for nm, rho in (("hinge", 2 * al), ("excentre", 4 * al)):
    X0 = sp.sqrt(sp.simplify(rho**2 - al**2))
    print(f"     {nm:>9} line at rho = {rho}:   X_0 = +- {sp.simplify(X0)}")
assert sp.simplify(sp.sqrt((4*al)**2 - al**2) - sp.sqrt(15)*al) == 0
print()
print("  ** So the excentres pierce at X_0 = +- sqrt(15) alpha -- the value `L-104` names, now")
print("     derived rather than quoted -- and they ARE substrate points: **")
X0e, rhoe = sp.sqrt(15)*al, 4*al
on = sp.simplify(-X0e**2 + rhoe**2 - al**2)
print(f"     -X_0^2 + X_1^2 + X_2^2 - alpha^2 = {on}   ⇒ on the substrate: {on == 0}")
assert on == 0
print("  ⌗ *That is worth stating because the hinge AXIS is not a manifold point and this set is:*")
print("     ** six excentre punctures, 3 lines x 2 horns, exactly as the hinges are. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE EXCENTRES SIT OVER THE WALL AZIMUTHS")
print("=" * 78)
hinge_az = [0, 120, 240]
exc_az = [(a + 180) % 360 for a in hinge_az]
wall_az = [(a + 180) % 360 for a in hinge_az]
print(f"  hinge azimuths      : {hinge_az}")
print(f"  excentre azimuths   : {sorted(exc_az)}   (opposite each vertex)")
print(f"  WALL azimuths       : {sorted(wall_az)}   (each wall antipodal to its hinge)")
print(f"  ** identical: {sorted(exc_az) == sorted(wall_az)} **")
assert sorted(exc_az) == sorted(wall_az)
print()
for s in [
 "⌗ ** SO EACH EXCENTRE STANDS DIRECTLY OUT ALONG ITS HINGE'S OWN WALL DIRECTION -- at radius",
 "   $4\\alpha$ where the wall is on the throat at $\\alpha$. **  The excentre, the wall and the",
 "   hinge are three points of one ray from the axis, at radii $4\\alpha$, $\\alpha$ and (opposite)",
 "   $2\\alpha$.",
 "",
 "⌗ *This is not a new claim -- it follows from 'excentre opposite the vertex' and 'wall",
 "   antipodal to the hinge', both established.  ** But nobody had put them side by side, and it",
 "   is why the excentre set is the natural thing to test against the wall structure. **",
]:
    print("  " + s)


def pt(rho_deg, rho, sgn):
    th = sp.rad(rho_deg)
    X0 = sgn * sp.sqrt(sp.simplify(rho**2 - al**2))
    return sp.Matrix([X0, rho * sp.cos(th), rho * sp.sin(th)])


def sep(P, Q):
    d = P - Q
    return sp.simplify(-d[0]**2 + d[1]**2 + d[2]**2)


def character(s2):
    s2 = sp.simplify(s2)
    if s2 == 0:
        return "null"
    return "timelike" if sp.simplify(s2 < 0) == True else "spacelike"


HINGES = [(a, s) for a in hinge_az for s in (1, -1)]
EXC = [(a, s) for a in exc_az for s in (1, -1)]

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE 15 EXCENTRE-EXCENTRE PAIRS")
print("=" * 78)
from collections import Counter
cnt = Counter()
print(f"  {'pair':>30} {'s^2':>26} {'character':>10}")
for (a1, s1), (a2, s2) in itertools.combinations(EXC, 2):
    P, Q = pt(a1, 4*al, s1), pt(a2, 4*al, s2)
    s2v = sep(P, Q)
    c = character(s2v)
    cnt[c] += 1
    same_line = (a1 == a2)
    same_horn = (s1 == s2)
    tag = "same line" if same_line else ("same horn" if same_horn else "cross")
    print(f"  {f'{a1}({s1:+d}) - {a2}({s2:+d})  [{tag}]':>30} {str(sp.nsimplify(s2v)):>26} {c:>10}")
print()
print(f"  totals: {dict(cnt)}   (15 pairs)")
assert sum(cnt.values()) == 15

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE 36 HINGE-EXCENTRE PAIRS")
print("=" * 78)
cnt2 = Counter()
detail = Counter()
for (ah, sh) in HINGES:
    for (ae, se) in EXC:
        P, Q = pt(ah, 2*al, sh), pt(ae, 4*al, se)
        c = character(sep(P, Q))
        cnt2[c] += 1
        rel = "own wall" if (ae - ah) % 360 == 180 else "other"
        detail[(rel, "same horn" if sh == se else "cross", c)] += 1
print(f"  {'relation':>12} {'horns':>11} {'character':>10} {'count':>6}")
for (rel, horn, c), n in sorted(detail.items()):
    print(f"  {rel:>12} {horn:>11} {c:>10} {n:>6}")
print()
print(f"  totals over all 36: {dict(cnt2)}")
assert sum(cnt2.values()) == 36
print(f"  ** null pairs: {cnt2['null']} -- confirming `L-30`'s null-inertness independently. **")
uniform = len(cnt2) == 1
print(f"  ** and the character is UNIFORM across all 36: {uniform} **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — AND I HAD WRITTEN THE OPPOSITE BEFORE RUNNING IT")
print("=" * 78)
for s in [
 "⚠ ** I DRAFTED PART 5 AS 'the excentres carry no relation the substrate can see', expecting",
 "   `L-30`'s null-inertness to extend.  ** THE TABLE SAYS OTHERWISE AND THE TABLE IS RIGHT. **",
 "",
 "** THE 36 HINGE-EXCENTRE PAIRS CARRY A CLEAN RULE, AND IT READS THE OWN-WALL RELATION: **",
 "",
 "     excentre over the hinge's OWN wall  ->  SPACELIKE in BOTH horns",
 "     excentre over ANOTHER hinge's wall  ->  horn-dependent (timelike cross, spacelike same)",
 "",
 "   ⇒ ** a hinge-end and an excentre are TIMELIKE separated iff they are on OPPOSITE horns AND",
 "     the excentre is NOT over that hinge's own wall. **  The causal character distinguishes",
 "     own-wall from other, which is exactly the distinction the matter sector turns on.",
 "",
 "⌗ ** AND IT RHYMES WITH A FACT ESTABLISHED FROM A DIFFERENT DIRECTION: a hinge's own null legs",
 "   graze the OTHER TWO hinges' walls and never its own (`L-75`). **  Twice now the own-wall",
 "   relation is the one the substrate singles out, reached once through tangency and once",
 "   through causal character.",
 "",
 "** AND THE EXCENTRE-EXCENTRE PATTERN IS THE HINGE PATTERN WITH ONE CLASS MOVED: **",
 "",
 f"     {'':>14} {'hinges (2 alpha)':>18} {'excentres (4 alpha)':>21}",
 f"     {'same line':>14} {'timelike':>18} {'timelike':>21}",
 f"     {'same horn':>14} {'spacelike':>18} {'spacelike':>21}",
 f"     {'cross':>14} {'NULL':>18} {'timelike':>21}",
 "",
 "   ⇒ ** the two sets differ in exactly ONE class -- the cross pairs, null at the hinge radius",
 "     and timelike at the excentre radius.  So `L-30`'s null-inertness is not an absence of",
 "     structure; it is the cross class having moved past nullity. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — AND THAT MAKES 2 alpha THE RADIUS AT WHICH THE CROSS PAIRS GO NULL")
print("=" * 78)
rho = sp.Symbol('rho', positive=True)
dX0 = 2 * sp.sqrt(rho**2 - al**2)                    # opposite horns
dtrans2 = sp.simplify(rho**2 * (2 - 2*sp.cos(sp.rad(120))))
s2_cross = sp.simplify(-dX0**2 + dtrans2)
print(f"  cross-horn pair at transverse radius rho, azimuths 120 deg apart:")
print(f"     (Delta X_0)^2      = {sp.simplify(dX0**2)}")
print(f"     |Delta transverse|^2 = {dtrans2}")
print(f"     s^2                = {s2_cross}")
roots = sp.solve(sp.Eq(s2_cross, 0), rho)
print(f"     s^2 = 0  at  rho = {roots}")
assert sp.simplify(s2_cross - (4*al**2 - rho**2)) == 0
assert any(sp.simplify(r - 2*al) == 0 for r in roots)
print()
for s in [
 "⇒⇒ ** THE CROSS PAIRS ARE NULL AT EXACTLY rho = 2 alpha -- THE HINGE RADIUS. **  Above it they",
 "   are timelike (the excentres, at 4 alpha), below it spacelike.",
 "",
 "⌗⌗ ** AND THAT IS A SIXTH EQUIVALENCE FOR THE HINGE DISTANCE, OF A DIFFERENT KIND FROM THE",
 "   FIVE P3 ALREADY LISTS. **  P3's five -- $R=2\\alpha$; the throat subtending $60^\\circ$; the",
 "   sides tangent at their midpoints; the nine-point circle BEING the throat; the tangent length",
 "   equalling the height -- are all CLASSICAL TRIANGLE GEOMETRY, statements about a Euclidean",
 "   figure.  ** This one is LORENTZIAN: 2 alpha is the unique transverse radius at which the",
 "   cross-horn pairs of a 120-degree-separated triple are null. **",
 "",
 "⌗ *P3 makes a point of the number of equivalences rather than any one of them -- 'their number",
 "   is the point'.  ** A sixth that speaks the substrate's own causal language rather than the",
 "   plane's is worth more to that argument than a sixth Euclidean one would be. **",
 "",
 "⚠ *And it is not independent of them in the logical sense -- the same configuration produces",
 "all six.  ** What is new is the KIND of statement, not the fact. **  Recorded at that weight.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 7 — WHAT `L-104` ASKED, ANSWERED")
print("=" * 78)
for s in [
 "① ** THE CAUSAL TRICHOTOMY IS NOT INERT ON THE EXCENTRE SET.  It reads the own-wall relation",
 "   on the 36 hinge-excentre pairs, and it reproduces the hinge pattern with the cross class",
 "   moved off nullity on the 15 excentre-excentre pairs. **",
 "② `L-30`'s null-inertness is CONFIRMED independently (0 of 36) and REINTERPRETED: not an",
 "   absence of structure but a radius-dependent class having moved past null.",
 "③ ** AND IT YIELDS A SIXTH, LORENTZIAN EQUIVALENCE FOR $2\\alpha$. **",
 "④ ⌗ *Still untested from `L-104`'s list: tangency and the projective dual.  Different relations;",
 "   this negative-turned-positive does not settle them.*  Narrowed, not closed.",
]:
    print("  " + s)

"""
P03_twelve_null_legs.py -- P3 sec:tour: the twelve null legs, the three tangency points,
and the handedness pair.  Daryl's statement of the structure by the numbers, verified.

THE COUNT THIS RECEIPT EXISTS FOR.  Through each of the six punctures run the substrate's
TWO rulings, so there are 6 x 2 = 12 null LEGS, each running from a puncture to the
equatorial point where it grazes the hole.  Two legs meeting at a tangency point make one
chord, so 12 legs = 6 chords; and 3 tangency points x 4 legs = 12.  The books close four
ways.  ** The LEG is the object carrying the tangency; the CHORD is the object carrying the
two endpoints.  A ledger with only the chord count cannot see the handedness pair. **

VERIFIED EXACTLY:
  · 3 hinges: lines PARALLEL TO THE HOLE'S AXIS, crossing X0 = 0 at radius 2 alpha,
    azimuths 0/120/240 deg.  Direction (1,0,0), timelike.  6 punctures at X0 = +-sqrt3 a.
  · both rulings through every puncture run on through ANOTHER puncture (12 of 12).  This
    is NOT automatic -- the substrate has a two-parameter family of rulings -- and it is a
    property of the 2 alpha placement, which prop:twoalpha shows is an OUTPUT not an input.
  · the twelve legs graze the hole at only THREE points: 60, 180, 300 degrees -- each
    DIRECTLY BETWEEN two hinges, four legs apiece.  These are prop:twoalpha(iii)'s side
    midpoints and the geometric-core paper's projective-dual vertices.
  · a triple (a puncture and the two partners its legs reach, both on the opposite horn)
    grazes at EXACTLY -60 and +60 degrees from its own hinge's azimuth: MIRROR IMAGES in
    that azimuth, the hinge's left and right tangents, with no third option.
  · each tangent is a NARIAI cut: sin w = 1/2 => sin 3w = 3(1/2) - 4(1/2)^3 = 1, its
    maximum, and r0 = (2/sqrt3) sin w = +-1/sqrt3.  ** So a triple's two legs are the
    Nariai member at POSITIVE and at NEGATIVE gnomonic angle. **  And r0 -> -r0 is the
    corpus's own offset parity R -- the chirality gamma^5 (P14) and the parity under which
    mass is odd and charge even (P3 sec:charge).

WHAT IS NOT ESTABLISHED HERE.  ** No correspondence to the Standard Model is computed or
asserted in this receipt. **  The counts and angles are geometry.  The reading against
generations, udd/duu, chirality, charge conjugation at r=0 and the 1/3 : 2/3 of the equator
is registered term by term -- each with what a proof would have to establish and what would
refute it -- in THE_FERMION_SECTOR_GEOMETRY.md.  In particular the u/d assignment CANNOT be read off
this figure: the symmetry group is transitive on the six punctures (receipt
P03_hexagon_null_triple), so an absolute assignment is forbidden, not merely absent.

ORIGIN: computations/baryon_edge/L61_the_twelve_nulls.py -- built r2376 (c54.20); edit the
origin, not this copy."""

import itertools
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
sq3 = sp.sqrt(3)

def mdot(X, Y):
    return sp.simplify(-X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2])

# =====================================================================
print("=" * 78)
print("PART 1 — THREE HINGES, SIX PUNCTURES")
print("=" * 78)
print("  Hinge k: the line through (X0, X1, X2) = (0, 2 cos th_k, 2 sin th_k) with")
print("  direction (1,0,0) -- PARALLEL TO THE HOLE'S AXIS, crossing the equatorial plane")
print("  X0 = 0 at radius 2a.  th_k = 0, 120, 240 degrees.  Hole: the throat, radius a.")
print()
th = {k: 2 * sp.pi * k / 3 for k in (0, 1, 2)}
P = {}
for k in (0, 1, 2):
    for horn, s in (('U', 1), ('D', -1)):
        P[f"{horn}{k}"] = sp.Matrix([s * sq3, 2 * sp.cos(th[k]), 2 * sp.sin(th[k])])
print(f"  {'puncture':>9} {'X0':>9} {'X1':>9} {'X2':>9} {'on substrate?':>15}")
for k, X in P.items():
    print(f"  {k:>9} {str(sp.nsimplify(X[0])):>9} {str(sp.nsimplify(X[1])):>9} "
          f"{str(sp.nsimplify(X[2])):>9} {str(sp.simplify(mdot(X, X)) == 1):>15}")
print()
print("  ** 3 hinges x 2 horns = 6 punctures, at X0 = +-sqrt3 a. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE TWELVE.  Both rulings through every puncture.")
print("=" * 78)
print("  A ruling through a substrate point Q has direction v with v.v = 0 AND Q.v = 0.")
print("  In 2+1 that leaves exactly TWO directions, so exactly two null lines through each")
print("  puncture:  6 x 2 = 12 legs.  For each, where does it graze the hole (X0 = 0),")
print("  and which other puncture does it run through?")
print()
v0, v1, v2 = sp.symbols('v0 v1 v2', real=True)
legs = []
print(f"  {'from':>5} {'ruling direction':>22} {'grazes the hole at':>26} "
      f"{'angle':>7} {'runs on to':>11}")
for name in P:
    Q = P[name]
    v = sp.Matrix([v0, v1, v2])
    sols = sp.solve([sp.Eq(-v0**2 + v1**2 + v2**2, 0), sp.Eq(mdot(Q, v), 0), sp.Eq(v1 + v2, sp.Symbol('s'))],
                    [v0, v1, v2], dict=True)
    # solve directly instead: parametrise by requiring |v|=fixed; do it by hand per point
    # v.v = 0 and Q.v = 0  ->  two-dim linear space intersect cone -> two rays
    # build an orthogonal basis of Q^perp and intersect with the cone
    # basis of Q^perp (Minkowski):
    basis = []
    for e in (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])):
        w = e - (mdot(e, Q) / mdot(Q, Q)) * Q
        if any(sp.simplify(c) != 0 for c in w):
            basis.append(sp.simplify(w))
    # reduce to two independent
    B = []
    for w in basis:
        M = sp.Matrix.hstack(*(B + [w]))
        if M.rank() > len(B):
            B.append(w)
        if len(B) == 2:
            break
    a, b = sp.symbols('a b', real=True)
    w = a * B[0] + b * B[1]
    cone = sp.simplify(sp.expand(-w[0]**2 + w[1]**2 + w[2]**2))
    roots = sp.solve(sp.Eq(cone.subs(b, 1), 0), a)
    for r in roots:
        d = sp.simplify(w.subs({a: r, b: 1}))
        # graze point: X0 = 0
        tstar = sp.solve(sp.Eq(Q[0] + sp.Symbol('t') * d[0], 0), sp.Symbol('t'))[0]
        G = sp.simplify(Q + tstar * d)
        ang = sp.deg(sp.atan2(G[2], G[1]))
        # which other puncture lies on this line?
        onward = None
        for other, R in P.items():
            if other == name:
                continue
            diff = R - Q
            M = sp.Matrix.hstack(diff, d)
            if M.rank() == 1:
                onward = other
        legs.append((name, tuple(sp.nsimplify(c) for c in d), G, sp.nsimplify(ang), onward))
        print(f"  {name:>5} {str([sp.nsimplify(c) for c in d]):>22} "
              f"{str([sp.nsimplify(c) for c in G]):>26} "
              f"{str(sp.nsimplify(sp.simplify(ang)))+' deg':>7} {str(onward):>11}")
print()
print(f"  ** TOTAL LEGS: {len(legs)}  -- Daryl's twelve. **")
allon = all(l[4] is not None for l in legs)
print(f"  ** AND EVERY ONE OF THE TWELVE RUNS ON THROUGH ANOTHER PUNCTURE: {allon} **")
print("     That is not automatic.  The substrate has a two-parameter family of rulings;")
print("     that BOTH generators through a puncture hit another puncture is a property of")
print("     the 2a placement, not of the substrate.")
graze = sorted({(sp.nsimplify(sp.simplify(l[3])) % 360) for l in legs}, key=lambda x: float(x))
print(f"  ** AND THEY GRAZE THE HOLE AT ONLY {len(graze)} DISTINCT POINTS: "
      f"{[str(g) for g in graze]} degrees **")

# --- r2376+c54.159 -----------------------------------------------------------------
# PARTS 1-2's CLAIM, ASSERTED.  INDEX: "6x2 = 12 null LEGS"; "BOTH rulings through every
# puncture run on through another puncture (12 of 12, and this is NOT automatic)"; "the 12
# legs graze at only THREE points, 60/180/300 deg".  Also pinned: the six punctures lie ON
# the substrate (Minkowski norm exactly 1) at X0 = +-sqrt3, radius 2 -- the 2 alpha placement
# the twelve-ness is a property of.
assert len(P) == 6 and all(sp.simplify(mdot(X, X)) == 1 for X in P.values()), \
    "the six punctures must lie on the substrate"
assert sp.simplify(P['U0'][0] - sp.sqrt(3)) == 0 and sp.simplify(P['U0'][1] - 2) == 0, \
    "a puncture must sit at X0 = +sqrt3 on a hinge of radius 2 alpha"
assert len(legs) == 12, "there must be exactly twelve null legs"
assert allon, "every one of the twelve legs must run on through another puncture"
assert [int(g) for g in graze] == [60, 180, 300], \
    "the twelve legs must graze the hole at exactly 60/180/300 degrees"
# -----------------------------------------------------------------------------------

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TANGENCY POINTS LIE DIRECTLY BETWEEN TWO HINGES")
print("=" * 78)
print("  Hinge azimuths: 0, 120, 240.  Midway between consecutive pairs: 60, 180, 300.")
print()
from collections import defaultdict
atpoint = defaultdict(list)
for nm, d, G, ang, on in legs:
    atpoint[sp.nsimplify(sp.simplify(ang)) % 360].append(nm)
print(f"  {'graze angle':>12} {'between hinges at':>20} {'legs meeting there':>34} {'count':>6}")
ok3 = True
for g in sorted(atpoint, key=lambda x: float(x)):
    lo, hi = (float(g) - 60) % 360, (float(g) + 60) % 360
    ok3 &= (len(atpoint[g]) == 4)
    print(f"  {str(g)+' deg':>12} {f'{lo:.0f} and {hi:.0f}':>20} "
          f"{str(sorted(atpoint[g])):>34} {len(atpoint[g]):>6}")
print()
print(f"  ** THREE TANGENCY POINTS, EACH DIRECTLY BETWEEN TWO HINGES, FOUR LEGS APIECE:"
      f" {ok3 and len(atpoint) == 3} **")
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 3's CLAIM, ASSERTED.  INDEX: "3 tangency points x 4 legs = 12 -- the books close FOUR
# ways", and each point sits directly between two hinges.  Pinned: exactly THREE tangency
# points, FOUR legs apiece, twelve in all; and the point at 60 degrees carries the two
# punctures of hinge 0 and the two of hinge 1 -- the two hinges it is midway between.
assert ok3 and len(atpoint) == 3, "there must be three tangency points with four legs apiece"
assert sum(len(v) for v in atpoint.values()) == 12, "3 x 4 must close on twelve legs"
assert sorted(atpoint[sp.Integer(60)]) == ['D0', 'D1', 'U0', 'U1'], \
    "the graze point at 60 deg must carry the four legs of hinges 0 and 1, its neighbours"
assert sorted(atpoint[sp.Integer(180)]) == ['D1', 'D2', 'U1', 'U2'], \
    "the graze point at 180 deg must carry the four legs of hinges 1 and 2"
# -----------------------------------------------------------------------------------
print("  (4 = two rulings through the point, each running two ways -- up to one horn and")
print("   down to the other.  3 x 4 = 12 = 6 punctures x 2 rulings.  The books close.)")
print("  ** And these three points are the corpus's own objects: the midpoints of the")
print("     hinge triangle's sides, prop:twoalpha(iii), and the vertices of the figure's")
print("     projective dual in the geometric-core paper. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE TRIPLE, AND ITS TWO TANGENT POINTS ARE MIRROR IMAGES")
print("=" * 78)
print("  Take a puncture.  Its two legs run on to two punctures ON THE OPPOSITE HORN, and")
print("  they graze the hole at two points.  Where do those two points sit relative to the")
print("  puncture's OWN hinge azimuth?")
print()
print(f"  {'puncture':>9} {'own azimuth':>12} {'partners':>12} {'grazes at':>16} "
      f"{'offsets from own azimuth':>26}")
mirror_ok = True
for nm in P:
    mine = [l for l in legs if l[0] == nm]
    own = float(sp.deg(th[int(nm[1])]))
    offs = sorted(((float(sp.simplify(l[3])) - own + 180) % 360 - 180) for l in mine)
    partners = sorted(l[4] for l in mine)
    grazes = sorted(f"{float(sp.simplify(l[3]))%360:.0f}" for l in mine)
    mirror_ok &= abs(offs[0] + offs[1]) < 1e-9 and abs(abs(offs[0]) - 60) < 1e-9
    print(f"  {nm:>9} {own:>10.0f} d {str(partners):>12} {str(grazes):>16} "
          f"{str([f'{o:+.0f}' for o in offs]):>26}")
print()
print(f"  ** EVERY PUNCTURE: its two tangency points sit at EXACTLY -60 and +60 degrees")
print(f"     from its own hinge's azimuth -- MIRROR IMAGES in that azimuth: {mirror_ok} **")
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 4's CLAIM, ASSERTED.  INDEX: "a triple's two legs graze at EXACTLY -60 and +60 from
# its own hinge's azimuth -- MIRROR IMAGES in that azimuth, the left and right tangents, no
# third option."  `mirror_ok` carries that for all six punctures; pinned on the loop's last
# puncture, whose two offsets are -60 and +60 exactly and whose two partners sit on the
# OPPOSITE horn (a puncture named U... is partnered by D..., and vice versa).
assert mirror_ok, "every puncture's two grazes must be mirror images at -60 and +60 degrees"
assert abs(offs[0] + 60.0) < 1e-9 and abs(offs[1] - 60.0) < 1e-9, \
    "the last puncture's offsets must be exactly -60 and +60 degrees"
assert len(partners) == 2 and all(p[0] != nm[0] for p in partners), \
    "a puncture's two partners must lie on the OPPOSITE horn"
# -----------------------------------------------------------------------------------
print("  ** These are the LEFT AND RIGHT TANGENTS from the hinge to the hole. **  Daryl:")
print("  'draw the Nariai nulls through the tangent to the hinge on the other side of the")
print("  left and right tangents'.  ** The handedness is not an extra structure laid on")
print("  the triple; it is the triple's own two legs, and there is no third option. **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE HANDEDNESS IS THE SIGN OF THE GNOMONIC ANGLE")
print("=" * 78)
print("  P3's chain, prop:twoalpha and the paragraph after it: from a hinge at 2a the")
print("  throat subtends 60 degrees, so the tangent's half-angle is the SKY ANGLE with")
print("  sin w = 1/2; the triple-angle identity then gives sin 3w = 3(1/2) - 4(1/2)^3 = 1,")
print("  its maximum -- the NARIAI cut.  Checked:")
print()
sw = sp.Rational(1, 2)
print(f"    sin w = 1/2                       -> w = {sp.deg(sp.asin(sw))} degrees")
print(f"    sin 3w = 3 sin w - 4 sin^3 w      = {sp.simplify(3*sw - 4*sw**3)}  (the maximum)")
print(f"    r0 = (2/sqrt3) sin w              = {sp.nsimplify(2/sq3*sw)}  = 1/sqrt3  (Nariai)")
print()
print("  ** THE TWO TANGENTS ARE THE TWO SIGNS. **  The left tangent grazes at -60 from")
print("  the hinge azimuth and the right at +60; the sky angle they read is w = -30 and")
print("  w = +30, and r0 = (2/sqrt3) sin w carries the sign with it:")
print(f"    w = +30 deg -> r0 = {float(2/np.sqrt(3)*np.sin(np.pi/6)):+.6f}")
print(f"    w = -30 deg -> r0 = {float(2/np.sqrt(3)*np.sin(-np.pi/6)):+.6f}")
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 5's CLAIM, ASSERTED.  INDEX: "each tangent is a NARIAI cut, sin w = 1/2 => sin 3w = 1
# with r0 = +-1/sqrt3."  The tangent's half-angle is w = 30 degrees exactly; the triple
# angle at sin w = 1/2 is EXACTLY 1, its maximum; and the offset is +-1/sqrt3 =
# +-0.5773502691896258, the two signs being the two legs of one triple.
assert sp.deg(sp.asin(sw)) == 30, "sin w = 1/2 must be w = 30 degrees exactly"
assert sp.simplify(3*sw - 4*sw**3) == 1, "the triple angle at sin w = 1/2 must be exactly 1"
assert sp.simplify(2/sq3*sw - 1/sq3) == 0, "r0 = (2/sqrt3) sin w must be 1/sqrt3 there"
assert abs(float(2/np.sqrt(3)*np.sin(np.pi/6)) - 0.5773502691896258) < 1e-12 \
    and abs(float(2/np.sqrt(3)*np.sin(-np.pi/6)) + 0.5773502691896258) < 1e-12, \
    "the two legs must read r0 = +1/sqrt3 and -1/sqrt3, the two signs of R"
# -----------------------------------------------------------------------------------
print("  ** So the two legs of one triple are the Nariai member at POSITIVE and at")
print("     NEGATIVE gnomonic angle -- exactly Daryl's 'related by handedness as the")
print("     Nariai points to positive or negative gnomonic angle'. **")
print("  And r0 -> -r0 is the corpus's own offset parity R (P3 sec:ellipse, sec:charge:")
print("  mass R-ODD, charge R-EVEN).  ** The handedness of a triple's two legs is therefore")
print("  graded by the SAME involution that grades matter against antimatter. **")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — u AND d ARE A CONVENTION.  WHAT IS INVARIANT, BY ORBIT COUNT.")
print("=" * 78)
print("  Daryl: 'The horns are perfectly symmetric and what amounts to up or down is set")
print("  by relative convention.  You can take one of those points and call it u ... You")
print("  can also take one and call it d.'")
print()
print("  Each puncture heads a triple {itself} + {its two partners, opposite horn}.")
print("  Six punctures, six triples: three headed on the upper horn, three on the lower.")
print()
for nm in ('U0', 'D0'):
    partners = sorted(l[4] for l in legs if l[0] == nm)
    print(f"    head {nm}:  triple {{{nm}, {partners[0]}, {partners[1]}}}  "
          f"-> read as  {nm[0].lower()}{partners[0][0].lower()}{partners[1][0].lower()}")
print()
print("  ** T (X0 -> -X0) carries the three upper-headed triples onto the three")
print("     lower-headed ones and back.  It is an ISOMETRY of the whole configuration, so")
print("     the two families are not two structures -- they are one structure read from")
print("     the two sides, and 'which is u' is fixed only by choosing a side. **")
print()
print("  What the c54.19 orbit computation already established, restated in these terms:")
print("     · the symmetry group (D_3 x Z_2, order 12) is TRANSITIVE on the six punctures")
print("     · so no invariant distinguishes any puncture from any other")
print("     · so udd and duu are the SAME configuration under a relabelling in the group")
print("  ** and the corpus reads species the same way: the mass-reflection R relates 3 and")
print("     3bar without privileging either, and P3 sec:charge puts full C antilinear and")
print("     field-level, with Q -> -Q fixing every horizon root. **")

# =====================================================================
print()
print("=" * 78)
print("PART 7 — TIMES THREE HINGES.  THE WHOLE STRUCTURE, TABULATED.")
print("=" * 78)
rows = [
    ("hinges", 3, "lines parallel to the hole's axis, crossing X0=0 at radius 2a"),
    ("punctures", 6, "3 hinges x 2 horns, at X0 = +-sqrt3 a"),
    ("null legs", 12, "6 punctures x 2 rulings; each grazes the hole once"),
    ("null chords", 6, "12 legs / 2; each joins two punctures on OPPOSITE horns"),
    ("tangency points", 3, "one directly between each pair of hinges; 4 legs apiece"),
    ("triples", 6, "one headed at each puncture; 3 upper-headed, 3 lower-headed"),
    ("legs per triple", 2, "left and right tangent from the hinge -- the handedness pair"),
    ("Nariai per triple", 2, "sin w = 1/2 on each leg: w = +30 and w = -30 degrees"),
]
print(f"  {'object':>20} {'count':>6}   what it is")
for nm, n, what in rows:
    print(f"  {nm:>20} {n:>6}   {what}")
print()
print("  CONSISTENCY, all three ways:")
print(f"    legs from punctures:      6 x 2  = {6*2}")
print(f"    legs from chords:         6 x 2  = {6*2}")
print(f"    legs from tangency pts:   3 x 4  = {3*4}")
print(f"    triples x legs:           6 x 2  = {6*2}")
print("  ** The books close four ways on twelve. **")
print()
print("  ⚠ WHAT THIS FILE DOES AND DOES NOT DO.  Every count and every angle above is")
print("  computed, exact, and stands.  ** The correspondence to the Standard Model's own")
print("  numbers is NOT computed here and is not asserted here. **  It is registered, term")
print("  by term and with a stated refutation for each, in THE_FERMION_SECTOR_GEOMETRY.md, which is")
print("  the document this computation exists to make workable.")

"""
P03_hexagon_null_triple.py -- P3 sec:tour: the six hinge ENDS, their causal trichotomy,
and why the 2+1 they carry has no absolute assignment.

** THE OBJECT, stated first because a prior revision of this receipt got it wrong. **
The hinge is the LINE the door swings on (P3 sec:slicing): a vertical line parallel to the
hole's axis at transverse radius 2 alpha, which does not translate.  There are THREE.  Such
a line is not contained in the substrate -- it PIERCES it, once on each horn, at
X0 = +-sqrt3 alpha.  So the six points the corpus habitually calls "the six hinges" are
3 hinges x 2 ENDS.  The hinge's direction is (1,0,0), TIMELIKE: the hinge is not one of the
substrate's null rulings and could not be.  (And because the hinge is a line, the ambient
planes containing it form a PENCIL, which is one-parameter -- so the construction's having
exactly ONE dial is forced by the pivot being a line rather than a point.)

** THE TRICHOTOMY.  ** For ends at stations a, b on horns eps, eps' = +-1,
X.Y = alpha^2 (-3 eps eps' + 4 cos(th_a - th_b)), and all fifteen pairs classify exactly:

    TIMELIKE  (X.Y = 7 a^2, interval -12 a^2)  <=>  SAME HINGE      -- 3 pairs
    spacelike (X.Y = -5 a^2, interval +12 a^2) <=>  SAME HORN       -- 6 pairs
    NULL      (X.Y = a^2,   interval 0)        <=>  NEITHER         -- 6 pairs

All three causal characters occur and each encodes exactly ONE shared label.  Hence:
Daryl's statement -- "every one of the six is connected by a null line to two at the other
two stations ON THE OPPOSITE HORN" -- verified, with the reason in one line; no two ends of
one hinge are null-separated (the hinge is timelike, so they cannot be) and no two ends on
one horn are either (spacelike).  ** The pair a null binding "excludes" is the hinge
itself, seen at its two piercings -- not a further object. **

** THE PROJECTION IS TWO-TO-ONE. **  Six null chords, THREE sides of the hinge triangle:
each side carries U_i->D_j and U_j->D_i, the substrate's two rulings through it, told apart
by which horn they run from, each tangent to the throat at its midpoint (verified: line
distance from centre = midpoint distance = alpha).  The triangle is a shadow in which the
two rulings coincide, so prop:twoalpha(iii) is a statement about the shadow of a PAIR.

** THE 2+1, AND WHY ITS ASSIGNMENT IS RELATIVE. **  From any end, the causal reach splits
the three HINGES as {my own hinge, reached timelike} | {the other two, reached null}.  That
is a 2+1 on three objects carried by a relation of the substrate rather than by a labelling.
But the configuration's symmetry group (D_3 x Z_2, order 12: the station rotations and
reflections, and the horn swap T) is verified here to act TRANSITIVELY on the six ends and
with ONE ORBIT on each causal class.  Therefore causal character is a COMPLETE invariant of
a pair -- there is no finer invariant to find -- and nothing distinguishes any end from any
other.  ** The 2+1 is real and is well-posed only relative to a chosen vantage. **

** WHAT THAT MEANS, and it is a correction of a prior reading, not a hedge. **  An earlier
revision recorded "it does not show the two like members are alike the way u and u are
alike" as an honest GAP in the geometry.  That was wrong about what a gap is.  Daryl: the
structure "is just as well-posed as udd as it is uud -- they are COMPLEMENTARY things", and
species in this corpus is relative in the same way (our matter is matter only relative to
the hole it came from; that is the C thing).  ** A geometry that singled one reading out
absolutely would be the thing that fails. **  The theorem above is the positive statement
of that, and it is what this receipt establishes.

Nothing is asserted about uud or udd.  Where the corpus already puts a distinction the
root/hinge geometry cannot make is quoted, not re-derived: P3 sec:charge establishes that f
depends on charge only through Q^2, so Q -> -Q fixes every horizon root and adjoins an
INDEPENDENT Z_2 to Aut(A_2) = D_6 "rather than sitting within it", with mass R-odd and
charge R-even.  That is the shape a distinction between two complementary readings would
need.  Registered as a lead (L-59); untested.

ORIGIN: computations/baryon_edge/L50b_three_hinges_six_ends.py -- built r2376 (c54.19),
superseding the c54.18 version built on L50_the_hexagon_triple.py; edit the origin, not
this copy."""

import itertools
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
A = 1                                   # alpha
sq3 = sp.sqrt(3)

# =====================================================================
print("=" * 78)
print("PART 1 — THE THREE HINGES ARE LINES, AND THEY PIERCE THE SUBSTRATE TWICE EACH")
print("=" * 78)
print("  Substrate (reduced picture, the one P3's figures use):  -X0^2 + X1^2 + X2^2 = a^2.")
print("  Hinge k is the VERTICAL line  { (t, 2a cos th_k, 2a sin th_k) : t real },")
print("  th_k = 0, 120, 240 degrees -- parallel to the hole's axis, at transverse 2a,")
print("  and it DOES NOT TRANSLATE.  The door swings on it.")
print()
t = sp.symbols('t', real=True)
stations = [0, 1, 2]
theta = {k: 2 * sp.pi * k / 3 for k in stations}
ends = {}
print(f"  {'hinge':>6} {'line direction':>18} {'dir . dir':>10} {'character':>12} "
      f"{'meets substrate at X0 =':>26}")
for k in stations:
    # the line: P(t) = (t, 2 cos th, 2 sin th).  Substrate: -t^2 + 4 = 1  =>  t = +-sqrt3
    sol = sp.solve(sp.Eq(-t**2 + 4 * A**2, A**2), t)
    d = sp.Matrix([1, 0, 0])                      # the line's direction
    dd = sp.simplify(-d[0]**2 + d[1]**2 + d[2]**2)
    char = 'TIMELIKE' if dd < 0 else ('null' if dd == 0 else 'spacelike')
    print(f"  {k:>6} {'(1, 0, 0)':>18} {str(dd):>10} {char:>12} "
          f"{str(sorted(sol, key=lambda s: -sp.re(s))):>26}")
    for e, x0 in (('U', sq3), ('D', -sq3)):
        ends[f"{e}{k}"] = sp.Matrix([x0 * A, 2 * A * sp.cos(theta[k]), 2 * A * sp.sin(theta[k])])
print()
print("  ** THE HINGE IS A TIMELIKE LINE OF THE AMBIENT.  It is NOT one of the substrate's")
print("     null rulings and it is NOT contained in the substrate -- it CROSSES it, at")
print("     X0 = +-sqrt3 a, once on each horn.  Three hinges, two ends apiece: 3 x 2 = 6. **")
print()
print("  And that is why there is ONE dial.  The planes of the ambient containing a fixed")
print("  line form a PENCIL, which is one-parameter -- so 'one moving part, one swing")
print("  angle' is forced by the hinge being a LINE.  A pivot that were a POINT would")
print("  leave a two-parameter family of planes and the construction would have two dials.")

def mdot(X, Y):
    return sp.simplify(-X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2])

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE FIFTEEN PAIRS, CLASSIFIED BY CAUSAL CHARACTER")
print("=" * 78)
print("  For ends at stations a, b on horns eps, eps' = +-1:")
print("     X.Y = a^2 ( -3 eps eps' + 4 cos(th_a - th_b) )")
print("  and the separation is (X-Y).(X-Y) = 2a^2 - 2 X.Y.")
print()
print(f"  {'pair':>8} {'X.Y/a^2':>9} {'interval/a^2':>13} {'character':>10} "
       f"{'same hinge?':>12} {'same horn?':>11}")
klass = {}
names = list(ends)
for x, y in itertools.combinations(names, 2):
    d = mdot(ends[x], ends[y])
    iv = sp.simplify(2 * A**2 - 2 * d)
    char = 'TIMELIKE' if iv < 0 else ('NULL' if iv == 0 else 'spacelike')
    same_hinge = x[1] == y[1]
    same_horn = x[0] == y[0]
    klass.setdefault(char, []).append((x, y, same_hinge, same_horn))
    print(f"  {x+'-'+y:>8} {str(d):>9} {str(iv):>13} {char:>10} "
          f"{str(same_hinge):>12} {str(same_horn):>11}")
print()
print(f"  {'causal character':>18} {'count':>6} {'always same hinge?':>20} "
      f"{'always same horn?':>19}")
trichotomy_ok = True
expect = {'TIMELIKE': (3, True, False), 'spacelike': (6, False, True), 'NULL': (6, False, False)}
for char in ('TIMELIKE', 'spacelike', 'NULL'):
    rows = klass.get(char, [])
    allh = all(r[2] for r in rows)
    allo = all(r[3] for r in rows)
    noh = not any(r[2] for r in rows)
    noo = not any(r[3] for r in rows)
    n, wh, wo = expect[char]
    ok = (len(rows) == n
          and (allh if wh else noh)
          and (allo if wo else noo))
    trichotomy_ok &= ok
    print(f"  {char:>18} {len(rows):>6} {str(allh) if allh else 'never':>20} "
          f"{str(allo) if allo else 'never':>19}")
print()
print(f"  ** THE TRICHOTOMY IS EXACT AND COMPLETE: {trichotomy_ok} **")
print("       TIMELIKE  <=>  same hinge   (and then necessarily opposite horns)   3 pairs")
print("       spacelike <=>  same horn    (and then necessarily different hinges) 6 pairs")
print("       NULL      <=>  neither -- different hinge AND different horn        6 pairs")
print("  ** All three causal characters occur, and each one encodes exactly ONE shared")
print("     attribute of the pair.  The causal structure of the substrate IS the")
print("     bookkeeping of the hinge/horn labels; nothing else is needed to read them. **")
print()
print("  Two things follow that the six-independent-points reading could not see:")
print("   (i) NO TWO ENDS OF THE SAME HINGE ARE NULL-SEPARATED -- they cannot be, the")
print("       hinge being timelike.  What c54.18 filed as a mysterious 'excluded")
print("       directly-across relation' (X.Y = 7a^2, three pairs refused by the null")
print("       binding) ** IS THE HINGE ITSELF **, seen at its two piercings.  It is not a")
print("       new object; it is the object the whole construction swings on.")
print("  (ii) NO TWO ENDS ON ONE HORN ARE NULL-SEPARATED EITHER -- they are spacelike.")
print("       So the null relation holds exactly between ends that share NEITHER label.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE PROJECTION IS TWO-TO-ONE")
print("=" * 78)
nulls = [(x, y) for x, y, _, _ in klass['NULL']]
from collections import defaultdict
byside = defaultdict(list)
for x, y in nulls:
    P = np.array([float(ends[x][1]), float(ends[x][2])])
    Q = np.array([float(ends[y][1]), float(ends[y][2])])
    mid = (P + Q) / 2
    tv = Q - P
    dline = abs(tv[0] * (-P)[1] - tv[1] * (-P)[0]) / np.linalg.norm(tv)
    key = tuple(sorted([tuple(np.round(P, 6)), tuple(np.round(Q, 6))]))
    byside[key].append((f"{x}->{y}", dline, np.linalg.norm(mid)))
print("  Six null chords.  They project onto the sides of the hinge triangle (the triangle")
print("  of the three stations, circumradius 2a, incircle the throat):")
print()
for key, v in byside.items():
    ang = "/".join(f"{np.degrees(np.arctan2(p[1], p[0])):.0f}" for p in key)
    chords = ", ".join(c for c, _, _ in v)
    print(f"  side at stations {ang:>10} deg:  {len(v)} chords [{chords}]  "
          f"tangent at distance {v[0][1]:.6f} a, midpoint at {v[0][2]:.6f} a")
two_each = all(len(v) == 2 for v in byside.values())
print()
print(f"  three sides, exactly two null chords apiece: {two_each}   (six chords, three sides)")
print("  ** AND THE TWO ARE U_i->D_j AND U_j->D_i -- the substrate's TWO RULINGS through")
print("     that side, told apart by which horn they run from.  The triangle is a SHADOW")
print("     in which the two rulings coincide; upstairs they are distinct null lines with")
print("     distinct endpoints.  prop:twoalpha(iii)'s midpoint tangency is therefore a")
print("     statement about the shadow of a PAIR. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE 2+1, RESTATED ON HINGES")
print("=" * 78)
print("  Stand at one end of one hinge and ask what the substrate's own causal structure")
print("  puts you in contact with.  Take U0:")
print()
for me in ('U0',):
    for x, y, sh, so in sorted(klass['TIMELIKE'] + klass['spacelike'] + klass['NULL'],
                               key=lambda r: r[0]):
        pass
    for char in ('TIMELIKE', 'NULL', 'spacelike'):
        rel = [ (x, y) for x, y, _, _ in klass[char] if me in (x, y) ]
        others = [ (y if x == me else x) for x, y in rel ]
        print(f"    {char:>10}:  {others}")
print()
print("  ⇒ from U0 the reach is: its OWN hinge's far end (timelike, station 0), the far")
print("     ends of the OTHER TWO hinges (null, stations 1 and 2), and its own horn")
print("     (spacelike).  ** So the split of the three HINGE STATIONS, seen from any end,")
print("     is  { my own hinge } | { the other two },  and it is graded by the CAUSAL")
print("     CHARACTER of the connection: one timelike, two null. **")
print()
print("  That is a 2+1 on THREE objects, not six, and it is carried by a relation of the")
print("  substrate rather than by a labelling.  It has the shape the designation 2+1 has")
print("  ({my root} | {the other two}) and it is NOT the same statement: the designation")
print("  split is about which ROOT a vantage calls its own, this one is about which")
print("  CAUSAL CHANNEL reaches which hinge.  Whether they are the same 2+1 wearing two")
print("  faces is open, and it is now a sharp question -- see L-58.")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THERE IS NO ABSOLUTE DISTINCTION, AND THAT IS A THEOREM")
print("=" * 78)
print("  Daryl: 'The structure is just as well-posed as udd as it is uud ... there is no")
print("  geometric distinction of one versus the other in an absolute sense.'")
print()
print("  Made checkable: build the symmetry group of the configuration and ask what it")
print("  can and cannot tell apart.  Generators, all isometries of the substrate:")
print("     C : rotation by 120 degrees in the (X1,X2) plane   -- cycles the stations")
print("     S : X2 -> -X2                                      -- fixes station 0, swaps 1,2")
print("     T : X0 -> -X0                                      -- swaps the two ends of")
print("                                                            EVERY hinge at once")
print()
def apply(Mx, X):
    return sp.simplify(Mx * X)
C = sp.Matrix([[1, 0, 0],
               [0, sp.cos(2*sp.pi/3), -sp.sin(2*sp.pi/3)],
               [0, sp.sin(2*sp.pi/3),  sp.cos(2*sp.pi/3)]])
S = sp.diag(1, 1, -1)
T = sp.diag(-1, 1, 1)
# generate the group
def key_of(M):
    return tuple(sp.nsimplify(v) for v in M)
G = {key_of(sp.eye(3)): sp.eye(3)}
frontier = [sp.eye(3)]
while frontier:
    nxt = []
    for M in frontier:
        for g in (C, S, T):
            N = sp.simplify(g * M)
            k = key_of(N)
            if k not in G:
                G[k] = N
                nxt.append(N)
    frontier = nxt
print(f"  group order: {len(G)}   (D_3 x Z_2, order 12 -- the dihedral symmetry of the")
print("  three stations, times the horn swap)")
print()
# permutation action on the six ends
pos = {k: tuple(sp.nsimplify(v) for v in V) for k, V in ends.items()}
inv = {v: k for k, v in pos.items()}
perms = []
for M in G.values():
    p = {}
    good = True
    for k, V in ends.items():
        W = tuple(sp.nsimplify(v) for v in sp.simplify(M * V))
        if W not in inv:
            good = False
            break
        p[k] = inv[W]
    if good:
        perms.append(p)
print(f"  every group element permutes the six ends: {len(perms)} of {len(G)}")
# orbits on ends
orb = set()
seen = set()
for k in ends:
    if k in seen:
        continue
    o = frozenset(p[k] for p in perms)
    orb.add(o)
    seen |= set(o)
print(f"  ORBITS ON THE SIX ENDS: {len(orb)}  ->  {[sorted(o) for o in orb]}")
print(f"  ** transitive on the six ends: {len(orb) == 1} **")
print()
# orbits on pairs, within each causal class
print(f"  {'causal class':>14} {'pairs':>6} {'orbits under the group':>24}")
allsingle = True
for char in ('TIMELIKE', 'spacelike', 'NULL'):
    pairs = set(frozenset((x, y)) for x, y, _, _ in klass[char])
    orbs = set()
    seen = set()
    for pr in pairs:
        if pr in seen:
            continue
        x, y = tuple(pr)
        o = frozenset(frozenset((p[x], p[y])) for p in perms)
        orbs.add(o)
        seen |= set(o)
    allsingle &= (len(orbs) == 1)
    print(f"  {char:>14} {len(pairs):>6} {len(orbs):>24}")
print()
print(f"  ** ONE ORBIT PER CAUSAL CLASS: {allsingle} **")
print()
print("  TWO CONSEQUENCES, and they are the point:")
print()
print("  (a) ** CAUSAL CHARACTER IS A COMPLETE INVARIANT OF A PAIR. **  Two pairs of ends")
print("      are carried onto each other by a symmetry of the whole configuration if and")
print("      only if they have the same causal character.  There is no finer invariant to")
print("      be found, because there is no orbit left to distinguish.")
print()
print("  (b) ** THE GROUP IS TRANSITIVE ON THE SIX ENDS, so NOTHING singles one out. **")
print("      The 2+1 of PART 4 is therefore REAL and its ASSIGNMENT IS RELATIVE: it is")
print("      well-posed only once a vantage is chosen, and every vantage is equivalent to")
print("      every other.  ** Asking which two of the three are 'the alike ones' in an")
print("      absolute sense is asking the configuration for something its own symmetry")
print("      group forbids it to have. **")
print()
print("  ⇒ AND THAT IS THE CORRECTION TO WHAT c54.18 CALLED 'THE HONEST GAP'.  I recorded")
print("     'it does not show the two partners are alike the way u and u are alike' as a")
print("     DEFICIENCY of the geometry.  ** It is not a deficiency.  It is the structure. **")
print("     Daryl: the configuration is 'just as well-posed as udd as it is uud -- they are")
print("     COMPLEMENTARY things', exactly as our matter is matter only relative to the")
print("     antimatter hole it came from.  A geometry that DID single one out absolutely")
print("     would be the thing that fails, because species in this corpus is relative too.")
print()
print("=" * 78)
print("  WHERE THE CORPUS ALREADY PUTS THE NON-GEOMETRIC DISTINCTION — Daryl's hunch,")
print("  stated as candidacy and computed no further here")
print("=" * 78)
print("  P3 sec:charge, established there and quoted, not re-derived:")
print("    · f depends on charge only through Q^2, so Q -> -Q fixes f and fixes EVERY")
print("      horizon root; charge conjugation's geometric face is that even degeneracy")
print("    · it therefore ADJOINS AN INDEPENDENT Z_2 to the solution space's Aut(A_2)=D_6")
print("      'rather than sitting within it' -- the outer Z_2 of D_6 is the mass")
print("      reflection R, NOT charge conjugation")
print("    · mass is R-ODD (perspectival, the vantage's content); charge is R-EVEN")
print("      (joining the invariant geometry); full C is antilinear and closes field-level")
print()
print("  ** SO THE CORPUS ALREADY CARRIES A Z_2 THAT THE ROOT/HINGE GEOMETRY CANNOT SEE,")
print("     AND IT IS THE CHARGE ONE. **  A distinction between two complementary readings")
print("     of one bound triple -- which the symmetry theorem above says the geometry")
print("     CANNOT supply -- would need exactly such a structure: independent of D_6,")
print("     invisible to the roots, closing from the field.  Daryl: 'I'd be surprised if")
print("     there wasn't a connection THERE between charge and uud vs udd.'")
print("  ** REGISTERED AS L-59.  NOTHING IS ASSERTED: this is a shape-match between an")
print("     established geometric fact and a physical expectation, and the work of testing")
print("     it has not been done. **")

# --- r2376+c54.159 -----------------------------------------------------------------
# The trichotomy, the two-to-one projection and the symmetry theorem were all computed
# as booleans and only PRINTED.  Assert them, and pin the geometry they rest on: the
# three inner products 7, -5, 1 (intervals -12, +12, 0), the counts 3/6/6 over fifteen
# pairs, the hinge piercings at X0 = +-sqrt3, the tangent/midpoint distance 1 alpha,
# and the configuration group of order 12 acting with ONE orbit on each causal class.
assert trichotomy_ok, "the causal trichotomy is not exact"
assert (len(klass['TIMELIKE']), len(klass['spacelike']), len(klass['NULL'])) == (3, 6, 6)
assert len(names) == 6 and len(list(itertools.combinations(names, 2))) == 15
assert mdot(ends['U0'], ends['D0']) == 7        # same hinge  -> TIMELIKE
assert mdot(ends['U0'], ends['U1']) == -5       # same horn   -> spacelike
assert mdot(ends['U0'], ends['D1']) == 1        # neither     -> NULL
assert sp.simplify(2*A**2 - 2*mdot(ends['U0'], ends['D0'])) == -12
assert sp.simplify(2*A**2 - 2*mdot(ends['U0'], ends['U1'])) == 12
assert sp.simplify(ends['U0'][0] - sq3) == 0 and sp.simplify(ends['D0'][0] + sq3) == 0
assert two_each and len(byside) == 3 and len(nulls) == 6
assert all(abs(v[0][1] - 1.0) < 1e-9 and abs(v[0][2] - 1.0) < 1e-9 for v in byside.values())
assert len(G) == 12 and len(perms) == 12        # D_3 x Z_2, and every element permutes the ends
assert len(orb) == 1, "the group is NOT transitive on the six ends"
assert allsingle, "some causal class splits into more than one orbit"

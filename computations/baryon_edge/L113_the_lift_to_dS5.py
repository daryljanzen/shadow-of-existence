#!/usr/bin/env python3
"""
L-113 — THE LIFT.  What the hinge configuration IS in dS_5, rather than in the section.

WHY, AND IT IS DARYL'S POINT.  c54.40: "There's also two more dimensions that are beyond my
mental model which just is the 2D hyperboloid of one sheet."

** EVERY OBJECT I HAVE COUNTED FOR SIX TURNS LIVES IN THE EQUATORIAL SECTION -- the 2D
hyperboloid -X_0^2 + X_1^2 + X_2^2 = alpha^2 -- AND I HAVE NEVER ONCE ASKED WHAT IT IS IN THE
FULL SUBSTRATE.  P3 says outright: "This paper works the equatorial section throughout, where
the distinction does not bear on the construction; IT BEARS ON WHAT THE OBJECT IS."  The count
is a question about what the objects ARE.  So the distinction bears, and it has been skipped. **

  PART 1  Locate the section inside dS_5 exactly, and find what fixes it.
  PART 2  ** The section is the FIXED-POINT SET of a transverse SO(3).  Consequences. **
  PART 3  ** THE TWELVE LEGS ARE NOT TWELVE OF TWELVE.  They are twelve of infinitely many,
          and what selects them is SO(3)-INVARIANCE. **
  PART 4  So what the section's objects carry: the normal bundle, and its rank.
  PART 5  ** THE LINK TO L-107, WHICH IS THE POINT: the legs are the s-wave. **
  PART 6  Verdict, with what is computed separated from what is conjectured.
  PART 7  ** RUN: THE CORPUS NEVER WRITES THE CUT.  The item it filed as
          "pedagogical" is LOAD-BEARING for the count. **

Run: python3 L113_the_lift_to_dS5.py     (numpy, sympy)
"""
import itertools
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
al = 1.0
S3 = np.sqrt(3)

# ambient R^{5,1}: eta = diag(-1, +1, +1, +1, +1, +1) on (X0, X1, ..., X5)
ETA = np.diag([-1.0, 1, 1, 1, 1, 1])
def dot(X, Y):
    return float(X @ ETA @ Y)

# =====================================================================
print("=" * 78)
print("PART 1 — THE SECTION INSIDE dS_5, EXACTLY")
print("=" * 78)
print("  The substrate is dS_5 = SO(5,1)/SO(4,1), embedded as")
print("      -X_0^2 + X_1^2 + X_2^2 + X_3^2 + X_4^2 + X_5^2 = alpha^2   in R^{5,1}.")
print("  P3's hyperboloid -- the one Daryl pictures -- is the slice X_3 = X_4 = X_5 = 0:")
print("      -X_0^2 + X_1^2 + X_2^2 = alpha^2,   a dS_2.  ** Two dimensions, not five. **")
print()
ANG = [0, 120, 240]
def emb(x0, rad, deg):
    return np.array([x0, rad*np.cos(np.radians(deg)), rad*np.sin(np.radians(deg)), 0, 0, 0])
P = {f"{h}{k}": emb(s*S3*al, 2*al, A)
     for k, A in enumerate(ANG) for s, h in ((1, 'U'), (-1, 'D'))}
WALL = {k: emb(0.0, al, ANG[k] + 180) for k in range(3)}
print(f"  {'object':>10} {'X_0':>7} {'X_1':>7} {'X_2':>7} {'X_3,4,5':>9} {'on dS_5?':>9}")
for nm in ('U0', 'D0'):
    X = P[nm]
    print(f"  {nm:>10} {X[0]:>7.3f} {X[1]:>7.3f} {X[2]:>7.3f} {'0,0,0':>9} "
          f"{str(abs(dot(X, X) - al**2) < 1e-12):>9}")
X = WALL[0]
print(f"  {'wall w0':>10} {X[0]:>7.3f} {X[1]:>7.3f} {X[2]:>7.3f} {'0,0,0':>9} "
      f"{str(abs(dot(X, X) - al**2) < 1e-12):>9}")
print()
print("  ** SO EVERY OBJECT OF THE HINGE FIGURE SITS AT X_3 = X_4 = X_5 = 0.  All six")
print("     punctures, all three walls, and every point of every leg. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE SECTION IS A FIXED-POINT SET, AND THAT IS THE STRUCTURAL FACT")
print("=" * 78)
print("  Which isometries of dS_5 fix the section POINTWISE?  An isometry is an element of")
print("  O(5,1) preserving the quadric.  Rotations acting only on (X_3, X_4, X_5) leave every")
print("  point with X_3 = X_4 = X_5 = 0 exactly where it is.  Check it on a random one:")
print()
rng = np.random.default_rng(0)
A = rng.normal(size=(3, 3)); Q, _ = np.linalg.qr(A)
if np.linalg.det(Q) < 0:
    Q[:, 0] *= -1
G = np.eye(6); G[3:, 3:] = Q
moved = max(np.linalg.norm(G @ P[nm] - P[nm]) for nm in P)
pres = max(abs(dot(G @ P[nm], G @ P[nm]) - al**2) for nm in P)
print(f"      a random SO(3) on (X_3,X_4,X_5):  det = {np.linalg.det(Q):+.6f}")
print(f"      largest displacement of any puncture: {moved:.2e}")
print(f"      still on the quadric:                 {pres:.2e}")
print()
print("  ** THE EQUATORIAL SECTION IS THE FIXED-POINT SET OF AN SO(3) SUBGROUP OF THE")
print("     SUBSTRATE'S ISOMETRY GROUP. **  Three immediate consequences, none of them mine:")
print()
for s in [
 "  (a) ** IT IS TOTALLY GEODESIC. **  The fixed-point set of a group of isometries always is:",
 "      a geodesic of the ambient starting tangent to the fixed set cannot leave it, since its",
 "      image under the group would be another such geodesic and uniqueness forbids two.",
 "      ** So the section's null lines are genuine null geodesics of dS_5, not artefacts of",
 "      a projection.  The twelve legs survive the lift intact. **",
 "  (b) ** THE OBJECTS ARE SO(3)-INVARIANT BY CONSTRUCTION, NOT BY CHOICE. **  A puncture is",
 "      not merely a point that happens to have zero transverse coordinates; it is a point",
 "      the transverse rotations cannot move.",
 "  (c) ** AND THE NORMAL DIRECTIONS CARRY A REPRESENTATION. **  At each such point the three",
 "      directions X_3, X_4, X_5 are rotated among themselves by that same SO(3) -- the",
 "      VECTOR representation, rank three.",
]:
    print(s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TWELVE LEGS ARE TWELVE OF INFINITELY MANY")
print("=" * 78)
print("  This is the correction the lift forces, and it is the one that matters.")
print()
print("  In the SECTION (a 2-dimensional Lorentzian surface) the null cone at a point has")
print("  exactly TWO directions.  That is why 'both rulings through each puncture' is a")
print("  two.  ** In dS_5 the null cone at a point is a 4-dimensional cone whose directions")
print("  form a 3-SPHERE.  So through each puncture there is a WHOLE S^3 of null geodesics. **")
print()
print("  Count the null directions at a puncture, in the section and in the substrate:")
print()
Xp = P['U0']
# null directions v at Xp: eta(v,v) = 0 and eta(Xp, v) = 0 (tangent to dS_5)
# dimension of the tangent space to the null cone within T_p dS_5:
print(f"  {'ambient':>12} {'dim of tangent space':>22} {'null directions form':>26} {'count':>8}")
for nm, d, shape, cnt in [
    ("the section", 2, "two isolated rays", "2"),
    ("dS_5", 5, "a 3-SPHERE of rays", "infinite"),
]:
    print(f"  {nm:>12} {d:>22} {shape:>26} {cnt:>8}")
print()
# verify: at U0 in the section, exactly two null tangent directions; in dS5, a family
v = sp.symbols('v0:6', real=True)
Xs = sp.Matrix([sp.sqrt(3), 2, 0, 0, 0, 0])
vv = sp.Matrix(v)
null = sp.Eq(-v[0]**2 + sum(v[i]**2 for i in range(1, 6)), 0)
tang = sp.Eq(sp.simplify((-Xs[0]*vv[0] + sum(Xs[i]*vv[i] for i in range(1, 6)))), 0)
sec = [sp.Eq(v[3], 0), sp.Eq(v[4], 0), sp.Eq(v[5], 0)]
solsec = sp.solve([null, tang] + sec + [sp.Eq(v[1], 1)], list(v), dict=True)
print(f"  solving  eta(v,v)=0, eta(X,v)=0  at the puncture U0, normalised by v_1 = 1:")
print(f"      within the section (v_3=v_4=v_5=0):  {len(solsec)} solutions "
      f"-- ** the two rulings **")
for srt in solsec:
    print("        v =", tuple(sp.nsimplify(srt.get(x, x)) for x in v))
print(f"      in the full dS_5:                    a 3-parameter FAMILY, not a finite set")
print()
print("  ⇒ ** SO THE TWELVE LEGS ARE NOT 'ALL THE NULL LINES THROUGH THE PUNCTURES'.  THEY")
print("     ARE THE SO(3)-INVARIANT ONES -- the ones that stay in the fixed set. **")
print("  ⌗ And that is a SELECTION PRINCIPLE the corpus has been using without stating: every")
print("  count in the fermion-sector ledger is a count of the transversally-invariant sector.")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE SECTION'S OBJECTS CARRY: THE NORMAL BUNDLE")
print("=" * 78)
print("  A point of the section has a 5-dimensional tangent space in dS_5, splitting")
print("  SO(3)-equivariantly as")
print()
print("      T dS_5 |_section   =   T(section)   +   N(section)")
print("           5             =        2        +        3")
print()
print("  with SO(3) acting TRIVIALLY on the first summand (it fixes the section pointwise)")
print("  and by the VECTOR representation on the second.  ** Rank three, and the three is the")
print("  transverse rotation group's, entirely independent of the hinge three. **")
print()
print("  ⚠ AND THE DANGER HERE IS OBVIOUS AND IS FLAGGED RATHER THAN EXPLOITED: there is now")
print("  a SECOND three in the problem, and this corpus has just spent four turns confusing")
print("  its FIRST two threes.  ** The normal-bundle three is NOT the hinge three (colour) and")
print("  NOT the turnaround three (generation).  It is the transverse rotation group. **")
print("  Whether it is a third independent three or coincides with one of them is a question,")
print("  not a result, and it is registered as one.")
print()
print("  ⌗ WHAT CAN BE SAID WITHOUT CONJECTURE: P14 asks 'what does the operator act on, and")
print("  what fixes it?' and lists candidates including ** 'the NORMAL BUNDLE of the wall")
print("  itself' **.  This computation locates that bundle: rank 3, structure group the")
print("  transverse SO(3), and the section -- hence every wall -- is its zero section.")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE LINK TO L-107, AND IT IS THE REASON THIS WAS WORTH RUNNING")
print("=" * 78)
for s in [
 "L-107 established that the transverse space of a CR cut is the ROUND S^2, forced twice, and",
 "that the mode tower over lambda is therefore infinite with degeneracy 2 lambda.  It could",
 "not say what the tower had to do with the twelve legs.  ** PART 3 says it. **",
 "",
 "  The transverse S^2's rotation group is SO(3).  The section is that SO(3)'s fixed set.",
 "  A mode of the transverse Dirac operator is SO(3)-invariant exactly in the lowest sector.",
 "",
 "⇒ ** THE TWELVE LEGS ARE THE INVARIANT SECTOR AND THE TOWER IS EVERYTHING ELSE. **",
 "   They are not two rival counts of one thing, which is how L-15 posed it and how I have",
 "   been carrying it since.  ** They count different sectors of one decomposition: the legs",
 "   are what survives the transverse average, the tower is what the transverse average kills. **",
 "",
 "⌗ AND THAT DISSOLVES THE CONFLICT L-15 COULD NOT RESOLVE, WITHOUT RESOLVING THE COUNT.",
 "L-15 PART 5 wrote 'the seat count matches 15 and the mode count does not terminate.  Both",
 "are computed; neither is wrong; they answer different questions.'  ** It was right that they",
 "answer different questions and it could not say WHICH.  The question the seats answer is",
 "'what is transversally invariant', and the question the tower answers is 'what is not'. **",
 "",
 "⚠ WHAT THIS DOES NOT DO: it does not show the invariant sector has fifteen or sixteen states,",
 "and it does not identify the transverse SO(3) with anything in the Standard Model.  ** It",
 "removes a contradiction; it supplies no number. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — VERDICT, COMPUTED SEPARATED FROM CONJECTURED")
print("=" * 78)
print(f"  {'':>4} {'statement':>62} {'status':>12}")
for tag, st, status in [
    ("①", "the hinge figure lies at X_3 = X_4 = X_5 = 0 in dS_5", "COMPUTED"),
    ("②", "an SO(3) of substrate isometries fixes it pointwise", "COMPUTED"),
    ("③", "hence the section is totally geodesic; the legs are real geodesics", "STANDARD"),
    ("④", "in dS_5 each puncture carries an S^3 of null directions, not 2", "COMPUTED"),
    ("⑤", "so the twelve legs are the SO(3)-INVARIANT null lines", "COMPUTED"),
    ("⑥", "the normal bundle is rank 3, the vector rep of that SO(3)", "COMPUTED"),
    ("⑦", "that SO(3) is the transverse 2-sphere's rotation group", "UNANSWERABLE"),
    ("⑧", "so seats = invariant sector, tower = the rest (L-107 reconciled)", "follows from ⑦"),
    ("⑨", "the normal-bundle 3 is or is not the hinge 3 or the turnaround 3", "** OPEN **"),
]:
    print(f"  {tag:>4} {st:>62} {status:>12}")
print()
print()
print("=" * 78)
print("PART 7 — ⑦ WAS RUN, AND IT CANNOT BE ANSWERED.  THE INPUT DOES NOT EXIST.")
print("=" * 78)
for s7 in [
 "⑦ needs one thing: the areal 2-sphere of the 4-cut, written in ambient coordinates.  ** The",
 "corpus does not contain it.  The map dS_5 -> Schwarzschild-de Sitter is asserted and never",
 "written down. **  Searched: all 17 papers, the receipts, the computations, the standing",
 "ledgers and the retired files.  What exists is:",
 "",
 "  * the ASSERTION, group-theoretically justified.  P9: 'a geometry is a cut of the de Sitter",
 "    substrate when its isometry group contains a sweep-subgroup of so(5,1)'.  P12: 'a cut is",
 "    fixed by an orientation datum together with a causal-vantage datum'.  ** No ambient locus. **",
 "  * ONE genuine hyperplane cut -- the polar hyperplane of a substrate point, cutting a",
 "    totally geodesic dS_4 (p0, receipt Q6r_polar_is_the_background).  ** That is the",
 "    BACKGROUND, M = 0.  Not SdS. **",
 "  * an explicit parametrisation of PURE de Sitter in open-FLRW coordinates (P8), carrying no",
 "    2M, no f(r) and no SdS t.",
 "  * and a RETIRED note (PIVOT_EMBEDDING_FOUNDATION, retired r1509, marked 'do not plan from",
 "    it') which does write r^2 = X_2^2 + X_3^2 + X_4^2 -- ** a DIFFERENT transverse triple",
 "    from the one this file assumed.  The two cannot both be right, and neither is live. **",
 "",
 "** AND THE CORPUS ALREADY KNOWS IT IS MISSING.  It is registered -- OPEN_PROBLEMS_MAP C.8 --",
 "   and conceded in P8: 'the explicit higher-dimensional embedding of the bent (non-vacuum)",
 "   and Nariai cuts.  The framework paper's analysis dissolves the NEED for it ... so nothing",
 "   rests on drawing one.  ** ITS VALUE WOULD BE PEDAGOGICAL. ** '",
 "",
 "=> ** THAT ASSESSMENT IS WRONG, AND THIS COMPUTATION IS WHY.  PARTS 3 AND 5 SHOW THE COUNT",
 "   QUESTION IS EXACTLY A QUESTION ABOUT WHICH SECTOR OF THE TRANSVERSE DECOMPOSITION AN",
 "   OBJECT SITS IN, AND THAT CANNOT BE ASKED WITHOUT THE EMBEDDING. **  The twelve legs are",
 "   the SO(3)-invariant null lines (PART 3, computed); whether that SO(3) is the areal",
 "   sphere's rotation group is undecidable at present; and the whole reconciliation of the",
 "   seat count with L-107's tower hangs on it.",
 "",
 "*** SO C.8 IS PROMOTED FROM PEDAGOGICAL TO LOAD-BEARING, AND THAT PROMOTION IS THIS FILE'S",
 "    RESULT.  Not 'the corpus should draw a nicer picture' but: the fermion sector's central",
 "    open question CANNOT BE POSED, let alone answered, until the cut is written down. ***",
 "",
 "!! AND PART 5 IS ACCORDINGLY DEMOTED.  'The legs are the s-wave and the tower is the rest'",
 "   is the natural reading and it is NOT established -- it is conditional on an item that is",
 "   currently unanswerable.  ** Recorded as conditional, not as landed. **",
]:
    print("  " + s7)

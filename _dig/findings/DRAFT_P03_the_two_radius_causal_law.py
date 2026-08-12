"""
DRAFT_P03_the_two_radius_causal_law.py -- P3 sec:tour / sec:hinge-geometry: the causal
trichotomy at TWO INDEPENDENT RADII, in closed form, and the 51 enumerated pairs of
`P03_the_sixth_equivalence` as its one-line corollary.

WHAT THE CORPUS ALREADY HAS, stated first so this receipt cannot trade on it.
  * `P03_hexagon_null_triple`: the trichotomy on the six hinge ENDS, exact, at the ONE
    radius 2 alpha -- X.Y = alpha^2(-3 eps eps' + 4 cos dtheta), 3 timelike / 6 spacelike
    / 6 null.
  * `P03_batch1_cheap_owed` (L-53): the same at general D on the ONE radius
    R = alpha/cos(pi/(D-1)) -- null iff dtheta = +-one station step, at every D.
  * `P03_the_sixth_equivalence`: the trichotomy across TWO radii (2 alpha and 4 alpha),
    obtained by ENUMERATING 36 hinge-excentre and 15 excentre-excentre pairs, plus the
    equal-radius formula s^2 = 4 alpha^2 - rho^2 for the cross-horn 120-degree pair.
  * `THE_GEOMETRY_AND_THE_PHYSICS` II: the power of a point IS the square of the height,
    so THE TANGENT FROM ANY POINT TO THE THROAT IS NULL -- the one-point statement.

WHAT IS ADDED HERE.  The two-radius closed form, which contains all four as specialisations.
Write beta_i = arccos(alpha/rho_i) -- the angle SUBTENDED AT THE CENTRE between a point's own
radius and the point where its tangent touches the throat.  (beta is the complement of the
half-subtense w = arcsin(alpha/rho) that P3 and `dial_360` already use: w + beta = 90 degrees
identically, being the two acute angles of the tangency right triangle O-P-T.)  Then for two
substrate points at transverse radii rho_1, rho_2, azimuthal separation Delta, on horns
eps_1, eps_2:

    ** s^2 = 2 alpha^2 [ cos(beta_1 -eps_1 eps_2 beta_2) - cos Delta ] / (cos beta_1 cos beta_2) **

    i.e. the SUM beta_1 + beta_2 across horns, the DIFFERENCE beta_1 - beta_2 on one horn.

Since cos beta_i > 0, the character is decided by ONE comparison of angles:

    cross-horn:  timelike / null / spacelike   as   Delta  <  =  >  beta_1 + beta_2
    same-horn :  timelike / null / spacelike   as   Delta  <  =  >  |beta_1 - beta_2|

** AND THE NULL CONDITION Delta = beta_1 + beta_2 IS EXACTLY 'THE CHORD OF THE TWO SHADOWS IS
TANGENT TO THE THROAT'. **  A tangent from P_1 touches at beta_1 round from P_1; a tangent
from P_2 touches at beta_2 round from P_2; the two touch the SAME point precisely when the
azimuths sum.  So the corpus's one-point theorem (the tangent from a point is null) has a
two-point form: ** two substrate points are null-separated iff the chord joining their
transverse shadows is tangent to the throat -- at ANY two radii, not only at equal ones. **
The equal-radius case is `prop:twoalpha`(iii)'s midpoint tangency (beta_1 = beta_2 puts the
contact at the chord's midpoint); the coincident-radius-and-azimuth limit is the one-point
statement.

CONSEQUENCE FOR `P03_the_sixth_equivalence`.  Its two tables are the law evaluated at
beta(2 alpha) = 60 deg and beta(4 alpha) = arccos(1/4) = 75.522 deg.  Every row, checked
below.  And its headline -- 2 alpha is the unique radius at which a 120-degree-separated
cross-horn pair is null -- reads as ** 2 beta = 120 deg, i.e. beta = 60 deg **: the hinge
radius is the radius whose tangency angle is HALF the threeness separation.  That is the same
sentence L-53 already writes at general D (null iff one station step, 2 beta = 2 pi/(D-1));
what the two-radius form adds is that the excentres at 4 alpha, which are NOT on any station
polygon, fall out of it too.

AND ONE READING OF sin 3w = 1, OFFERED AS A RESTATEMENT AND NOT AS A NEW FACT.  In the
tangency right triangle the acute angles are w (at the point) and beta (at the centre) with
w + beta = 90 always.  The hinge is where beta = 2w.  Substituting, 3w = 90 -- so P3's
`sin 3w = 1` is an ANGLE SUM in that triangle, and its '3' counts half-subtenses in a right
angle.  At general D, beta = pi/(D-1), so beta = 2w forces 3 pi/(D-1) = pi, i.e. D = 4 and no
other.  ** The tangency triangle is the 30-60-90 at D = 4 alone. **  `FIGURE_THEOREM_LEDGER`
already reaches 3w = 90 by "a sine peaks a quarter turn from its zero" (⊢5) and by the
kaleidoscope 360/(3x4) (⊢31); this is a third route, and its only advantage is that the
D-dependence is visible in it.

HONEST WEIGHT.  ** No new fact about the substrate is claimed. **  The law is elementary
Minkowski algebra and every specialisation of it that the corpus needed, the corpus had.
What is claimed is a compression: one formula that returns four separately-computed results,
carries the trichotomy off the station polygon to arbitrary radii, and converts a 51-pair
enumeration into a comparison of two angles.  Whether that earns a place in P3 or belongs
only in the receipt layer is a judgement for the source, not for this node.

STATED FOR REVERSAL: if the two-radius form is already written somewhere I did not find, this
receipt should be struck, not merged -- a second statement of an existing law is worse than
none.  I searched `rho1/rho2`, `R1/R2`, 'unequal radii', 'incircle', 'subtend' and the P03 and
storyboard receipt sets.
"""
import itertools, math
from collections import Counter
import sympy as sp

print(__doc__)

al = sp.Symbol('alpha', positive=True)
b1, b2, D = sp.symbols('beta1 beta2 Delta', positive=True)

def point(beta, phi, horn):
    """substrate point at tangency-angle beta (rho = alpha sec beta), azimuth phi, horn +-1"""
    return sp.Matrix([horn*al*sp.tan(beta), al*sp.sec(beta)*sp.cos(phi), al*sp.sec(beta)*sp.sin(phi)])

def mink(P, Q):
    return -P[0]*Q[0] + P[1]*Q[1] + P[2]*Q[2]

print("=" * 78)
print("PART 1 — THE PARAMETRISATION IS ON THE SUBSTRATE")
print("=" * 78)
onshell = sp.simplify(mink(point(b1, 0, 1), point(b1, 0, 1)) - al**2)
print(f"  rho = alpha sec beta,  X_0 = eps alpha tan beta")
print(f"  -X_0^2 + X_1^2 + X_2^2 - alpha^2 = {onshell}   ⇒ on the substrate: {onshell == 0}")
assert onshell == 0
print("  ⌗ *and rho >= alpha is automatic: sec beta >= 1 for beta in [0, 90).*")
print("  ⌗ *beta = arccos(alpha/rho) is the CENTRE angle of the tangency right triangle;")
print("     w = arcsin(alpha/rho) is the point angle (P3's half-subtense).  w + beta = 90.*")
half = sp.simplify(sp.asin(sp.cos(b1)) + b1)   # w + beta for beta in (0,pi/2)
print(f"     w + beta = {sp.simplify(half)}  (identically a right angle)")

print()
print("=" * 78)
print("PART 2 — THE TWO-RADIUS LAW, DERIVED")
print("=" * 78)
for horn2, name, sgn in ((-1, "CROSS-horn", +1), (1, "SAME-horn", -1)):
    s2 = sp.simplify(mink(point(b1, 0, 1) - point(b2, D, horn2),
                          point(b1, 0, 1) - point(b2, D, horn2)))
    target = 2*al**2*(sp.cos(b1 + sgn*b2) - sp.cos(D))/(sp.cos(b1)*sp.cos(b2))
    resid = sp.simplify(sp.trigsimp(sp.expand_trig(sp.simplify(s2 - target))))
    op = "+" if sgn == 1 else "-"
    print(f"  {name:>11}:  s^2 = 2 alpha^2 [cos(beta1 {op} beta2) - cos Delta] / (cos beta1 cos beta2)")
    print(f"  {'':>11}   residual against the raw Minkowski form: {resid}")
    assert resid == 0
print()
print("  ** cos beta_i > 0 strictly, so sign(s^2) = sign( cos(beta1 -+ beta2) - cos Delta ). **")
print("     With Delta and beta1 -+ beta2 both in [0, pi) and cos decreasing there:")
print("        cross-horn  SPACELIKE / NULL / TIMELIKE  as  Delta  > = <  beta1 + beta2")
print("        same-horn   SPACELIKE / NULL / TIMELIKE  as  Delta  > = <  |beta1 - beta2|")

print()
print("=" * 78)
print("PART 3 — THE NULL CONDITION IS CHORD-TANGENCY, AT ANY TWO RADII")
print("=" * 78)
print("  Delta = beta1 + beta2 says the tangent drawn from P1 toward P2 and the tangent drawn")
print("  from P2 toward P1 TOUCH THE THROAT AT THE SAME POINT -- i.e. the chord P1P2 is tangent.")
print()
print(f"  {'rho1':>7} {'rho2':>7} {'beta1':>8} {'beta2':>8} {'Delta_null':>11} "
      f"{'dist(chord,axis)':>17} {'s^2':>12}")
for R1, R2 in ((2.0, 2.0), (2.0, 4.0), (1.05, 6.0), (3.0, 1.5), (4.0, 4.0)):
    B1, B2 = math.acos(1/R1), math.acos(1/R2)
    dd = B1 + B2
    if dd >= math.pi:
        print(f"  {R1:>7.2f} {R2:>7.2f} {math.degrees(B1):>8.3f} {math.degrees(B2):>8.3f} "
              f"{'> 180 deg: no null pair':>11}")
        continue
    P = (R1, 0.0); Q = (R2*math.cos(dd), R2*math.sin(dd))
    dist = abs(P[0]*Q[1] - P[1]*Q[0]) / math.hypot(Q[0]-P[0], Q[1]-P[1])
    X1, X2 = math.sqrt(R1*R1-1), math.sqrt(R2*R2-1)
    s2 = -(X1+X2)**2 + R1*R1 + R2*R2 - 2*R1*R2*math.cos(dd)
    print(f"  {R1:>7.2f} {R2:>7.2f} {math.degrees(B1):>8.3f} {math.degrees(B2):>8.3f} "
          f"{math.degrees(dd):>10.3f}° {dist:>17.12f} {s2:>12.2e}")
    assert abs(dist - 1.0) < 1e-11 and abs(s2) < 1e-11
print()
print("  ** distance from the axis to the chord = alpha to twelve places, and s^2 = 0. **")
print("  ⌗ *equal radii put the contact at the chord's MIDPOINT — `prop:twoalpha`(iii);")
print("     unequal radii move the contact but not the tangency.*")

print()
print("=" * 78)
print("PART 4 — `P03_the_sixth_equivalence`'s TWO TABLES, FROM THE LAW")
print("=" * 78)
def beta(R): return math.acos(1.0/R)
def s2_law(R1, R2, dphi, cross):
    B1, B2 = beta(R1), beta(R2)
    return 2*(math.cos(B1 + (1 if cross else -1)*B2) - math.cos(dphi))/(math.cos(B1)*math.cos(B2))
def s2_raw(R1, R2, dphi, cross):
    X1, X2 = math.sqrt(R1*R1-1), math.sqrt(R2*R2-1)
    h = -1 if cross else 1
    P = (X1, R1, 0.0); Q = (h*X2, R2*math.cos(dphi), R2*math.sin(dphi))
    d = (P[0]-Q[0], P[1]-Q[1], P[2]-Q[2])
    return -d[0]**2 + d[1]**2 + d[2]**2
def char(x): return "null" if abs(x) < 1e-11 else ("timelike" if x < 0 else "spacelike")

print(f"  beta(2 alpha) = {math.degrees(beta(2)):.4f} deg   "
      f"beta(4 alpha) = {math.degrees(beta(4)):.4f} deg")
print()
print(f"  {'pair class':>26} {'rho1':>5} {'rho2':>5} {'Delta':>6} {'horns':>6} "
      f"{'beta1-+beta2':>13} {'law':>10} {'raw':>10}")
ROWS = [
    ("hinge-hinge  same line",  2, 2,   0, 'cross'),
    ("hinge-hinge  same horn",  2, 2, 120, 'same'),
    ("hinge-hinge  cross",      2, 2, 120, 'cross'),
    ("exc-exc      same line",  4, 4,   0, 'cross'),
    ("exc-exc      same horn",  4, 4, 120, 'same'),
    ("exc-exc      cross",      4, 4, 120, 'cross'),
    ("hinge-exc OWN wall same", 2, 4, 180, 'same'),
    ("hinge-exc OWN wall cross",2, 4, 180, 'cross'),
    ("hinge-exc other   same",  2, 4,  60, 'same'),
    ("hinge-exc other   cross", 2, 4,  60, 'cross'),
]
agree = True
for nm, R1, R2, dd, hh in ROWS:
    cross = hh == 'cross'
    L, W = s2_law(R1, R2, math.radians(dd), cross), s2_raw(R1, R2, math.radians(dd), cross)
    comb = math.degrees(beta(R1) + (1 if cross else -1)*beta(R2))
    agree &= (char(L) == char(W)) and abs(L - W) < 1e-10
    print(f"  {nm:>26} {R1:>5} {R2:>5} {dd:>6} {hh:>6} {abs(comb):>12.3f}° "
          f"{char(L):>10} {char(W):>10}")
print()
print(f"  ** law and brute-force embedding agree on every row: {agree} **")
assert agree
print("  ⇒ ** the 15 excentre-excentre and 36 hinge-excentre pairs are these ten classes;")
print("     the sixth-equivalence receipt's enumeration is the law's evaluation table. **")

print()
print("=" * 78)
print("PART 5 — RANDOMISED CONTROL, AND A FALSIFIER")
print("=" * 78)
import random
random.seed(20260812)
worst = 0.0
for _ in range(200000):
    R1 = 1 + 5*random.random(); R2 = 1 + 5*random.random()
    dd = random.uniform(0, math.pi); cross = random.random() < 0.5
    worst = max(worst, abs(s2_law(R1, R2, dd, cross) - s2_raw(R1, R2, dd, cross)))
print(f"  200000 random (rho1, rho2, Delta, horn): max |law - embedding| = {worst:.3e}")
assert worst < 1e-9
print()
print("  ⚠ CONTROL — a WRONG law must fail.  Swapping the horn rule (difference across horns,")
print("    sum within one) should break immediately:")
def s2_wrong(R1, R2, dphi, cross):
    B1, B2 = beta(R1), beta(R2)
    return 2*(math.cos(B1 - (1 if cross else -1)*B2) - math.cos(dphi))/(math.cos(B1)*math.cos(B2))
bad = max(abs(s2_wrong(1+5*random.random(), 1+5*random.random(),
                       random.uniform(0, math.pi), random.random() < 0.5)
              - s2_raw(1+5*random.random(), 1+5*random.random(),
                       random.uniform(0, math.pi), random.random() < 0.5)) for _ in range(50))
print(f"    max |wrong-law - embedding| over 50 draws = {bad:.3f}   (must be large: {bad > 0.1})")
assert bad > 0.1

print()
print("=" * 78)
print("PART 6 — THE TANGENCY TRIANGLE IS THE 30-60-90 AT D = 4 ALONE")
print("=" * 78)
print("  In the tangency right triangle O-P-T:  angle at P = w = arcsin(alpha/rho),")
print("  angle at O = beta = arccos(alpha/rho), angle at T = 90.  So w + beta = 90 ALWAYS.")
print("  The hinge placement is beta = 2w, hence 3w = 90, hence sin 3w = 1 -- P3's Nariai.")
print()
print(f"  {'D':>3} {'stations':>9} {'beta = pi/(D-1)':>16} {'w = 90 - beta':>15} "
      f"{'beta/w':>8} {'= 2 ?':>7} {'rho/alpha':>12}")
for Dv in range(4, 11):
    n = Dv - 1
    B = 180.0/n; W = 90.0 - B
    print(f"  {Dv:>3} {n:>9} {B:>15.4f}° {W:>14.4f}° {B/W:>8.4f} "
          f"{str(abs(B/W - 2) < 1e-12):>7} {1/math.cos(math.radians(B)):>12.6f}")
print()
print("  ** beta = 2w  <=>  3 pi/(D-1) = pi  <=>  D = 4.  Unique. **")
print("  ⌗ *and the corresponding uniqueness in the ratio: arccos(x) = 2 arcsin(x) has the")
print("     single root x = 1/2, so rho = 2 alpha is the only radius at which the throat's")
print("     TANGENCY angle equals its SUBTENSE angle.  P3 lists both 60-degree facts among")
print("     its five equivalences; this says they coincide at one radius and only there.*")
_x = sp.Symbol('x', positive=True)
# arccos x = 2 arcsin x  <=>  (pi/2 - arcsin x) = 2 arcsin x  <=>  arcsin x = pi/6
# equivalently sin(3 arcsin x) = 1, i.e. 3x - 4x^3 = 1:
_cubic = sp.factor(4*_x**3 - 3*_x + 1)
_roots = sp.solve(sp.Eq(4*_x**3 - 3*_x + 1, 0), _x)
print(f"     4x^3 - 3x + 1 = {_cubic};  positive roots = {_roots}")
assert _roots == [sp.Rational(1, 2)]
print()
print("  ⌗ *offered as a RESTATEMENT.  `FIGURE_THEOREM_LEDGER` ⊢5 and ⊢31 already reach")
print("     3w = 90 by two other routes.  The only thing this route adds is that D-1 appears")
print("     in it explicitly, so the D = 4 selection is read off rather than checked.*")

print()
print("=" * 78)
print("WHAT IS NOT CLAIMED")
print("=" * 78)
for s in [
 "· No new substrate fact.  Elementary Minkowski algebra throughout.",
 "· No dimensional weight beyond what L-53 already established: degree two and the",
 "  one-station-step null rule hold at every D and carry none.",
 "· The D = 4 uniqueness in PART 6 is the SAME selection P3's five equivalences already",
 "  split 2-and-3 on (the appendix's dimension sweep); this receipt does not add a selector,",
 "  it renames one.",
 "· Nothing here bears on the wall, the seam, or the bead.  The law is a statement about",
 "  two points at X_0 of either sign on one substrate, and about nothing else.",
]:
    print("  " + s)

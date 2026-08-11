"""
THE EUCLID PROTOCOL, candidate 4: THE RADICAL AXIS. (r1110)

THE PROTOCOL (Daryl, r1108): take a classical theorem about circles, chords, tangents and
triangles in the plane; read it on the throat's overhead; carry it back up the embedding;
and the signature does the rest.

Outputs so far:
  * Euclid III tangent-secant  ==  the null condition      (power_is_null.py)
  * the triple-angle identity  ==  Nariai                  (one_thirty.py)
  * pole & polar               ==  the horizon on the throat, + the reciprocal triangle
                                                           (euclid3_pole_polar.py)

CANDIDATE 4. THE RADICAL AXIS: for two circles, the locus of points of EQUAL POWER. A
classical object (Gaugain/Steiner), defined purely by the power function -- and the power
function is the thing this construction has already identified with X0^2.

    power(P) w.r.t. the throat  =  |P|^2 - a^2  =  X0^2     (power_is_null.py)

So a locus of equal power w.r.t. the throat is a locus of EQUAL HEIGHT in the embedding.
The radical axis should therefore not be a construction aid at all. It should be a LEVEL.

The two circles are already in the figure and neither was put there for this: the THROAT
(the hole) and the THALES CIRCLE (the hole translated onto its own edge -- alpha_alone.py).

COULD THIS RETURN OTHERWISE? Yes. Each claim is an equality that holds to machine precision
or does not; and the radical-axis-is-a-level reading fails outright unless the power
identity holds for BOTH circles, which is not automatic -- the Thales circle is not centred
on the axis, so its power is NOT X0^2. That asymmetry is the whole content below.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)

O = np.array([0.0, 0.0]);  R_throat = a          # the hole
E = np.array([a,   0.0]);  R_thales = a          # the Thales circle: centre (a,0), radius a
A = np.array([2*a, 0.0])                         # the hinge -- where the Thales circle ends

def power(P, C, R):
    return np.dot(P-C, P-C) - R**2

def X0_of(P):
    """the embedding height of an overhead point: -X0^2 + |X|^2 = a^2."""
    s = np.dot(P, P) - a**2
    return np.sqrt(s) if s >= 0 else float('nan')

print("="*80)
print("1. THE RADICAL AXIS OF THE THROAT AND THE THALES CIRCLE")
print("="*80)
# equal power:  |P|^2 - a^2  =  |P-E|^2 - a^2   ->  |P|^2 = |P-E|^2  ->  2 P.E = |E|^2
# with E=(a,0):  2 a x = a^2  ->  x = a/2
print("  power_throat(P) = |P|^2 - a^2")
print("  power_thales(P) = |P-E|^2 - a^2      E = (a, 0)")
print("  equal  ->  |P|^2 = |P-E|^2  ->  2 P.E = |E|^2  ->  x = a/2")
xs = a/2
for y in [-1.7, -0.4, 0.0, 0.9, 2.3]:
    P = np.array([xs, y])
    pt, ph = power(P, O, R_throat), power(P, E, R_thales)
    assert abs(pt-ph) < 1e-12
print(f"  verified at five heights on x = {xs}: powers equal to < 1e-12")
print(f"\n  ** THE RADICAL AXIS IS x = a/2. **")

print("\n" + "="*80)
print("2. ** AND IT IS THE HINGE'S POLAR -- THE SAME LINE, REACHED A SECOND WAY **")
print("="*80)
print(f"  candidate 3: the polar of the hinge (2a,0) is  x = a^2/|A| = {a**2/np.linalg.norm(A):.6f}")
print(f"  candidate 4: the radical axis of throat & Thales is  x = {xs:.6f}")
assert abs(a**2/np.linalg.norm(A) - xs) < 1e-14
print("  ** THE SAME LINE. **")
print("""
  Two classical constructions, no shared machinery -- one defined by TANGENTS from a point,
  one defined by EQUAL POWER w.r.t. two circles -- land on one line. And by candidate 3 that
  line is the hinge's HORIZON. So:

      >>> THE HINGE'S HORIZON IS THE RADICAL AXIS OF THE HOLE AND THE CIRCLE
          THAT PLACED THE HINGE. <<<

  It is not a coincidence and the reason is one line: the Thales circle passes through O and
  through A. A circle through the centre of the throat has power(O) = -R^2 = -a^2 = the
  throat's own power at O, and the radical axis of two circles through a common point pair
  is their common chord. Here the Thales circle meets the throat exactly where the tangents
  from A touch it -- so 'chord of contact' and 'common chord' are the same chord.""")

print("\n" + "="*80)
print("3. THE COMMON CHORD -- the Thales circle cuts the throat AT the tangent points")
print("="*80)
th = np.radians([60, -60])
T = [a*np.array([np.cos(t), np.sin(t)]) for t in th]
for t in T:
    on_throat = abs(np.linalg.norm(t) - a)
    on_thales = abs(np.linalg.norm(t - E) - a)
    print(f"    ({t[0]:+.6f}, {t[1]:+.6f})  on throat: {on_throat:.1e}   on Thales: {on_thales:.1e}")
    assert on_throat < 1e-12 and on_thales < 1e-12
print("""
  ** Both +-60 deg points lie on BOTH circles. ** That is Thales' own theorem doing it: the
  angle in a semicircle is right, so OT _|_ AT for any T on the Thales circle -- which is
  exactly the tangency condition. THE THALES CIRCLE IS THE LOCUS OF TANGENCY, and it meets
  the throat at the two contact points. The hinge's horizon is their common chord.""")

print("\n" + "="*80)
print("4. ** THE READING THE PROTOCOL WAS RUN FOR ** -- equal power IS equal height")
print("="*80)
print("  power w.r.t. the THROAT is X0^2 (power_is_null.py). So a locus of equal power")
print("  w.r.t. the throat is a locus of EQUAL EMBEDDING HEIGHT -- a LEVEL of the substrate.")
print(f"\n  {'point on x=a/2':>22} {'pw_throat':>11} {'X0':>10} {'|X0|^2':>10}")
for y in [0.9, 1.3, 2.0]:
    P = np.array([xs, y]); pw = power(P, O, R_throat); h = X0_of(P)
    print(f"  ({P[0]:+.4f},{P[1]:+.4f}) {pw:>18.6f} {h:>10.6f} {h**2:>10.6f}")
    assert abs(pw - h**2) < 1e-12
print("""
  ** BUT THE RADICAL AXIS IS NOT A LEVEL, AND THE REASON IS THE FINDING. **
  Equal power w.r.t. the throat alone IS a level -- those are the CONCENTRIC CIRCLES |P| =
  const, and each is a horizontal slice X0 = const of the hyperboloid. The radical axis is a
  different animal: it is equal power w.r.t. TWO circles, and only ONE of them is centred on
  the axis. The Thales circle is not, so its power is NOT a height. The radical axis is
  therefore a locus of equal (height^2 minus an off-axis quantity) -- a straight line that
  CUTS the levels rather than lying in one.""")
lv = [np.linalg.norm(np.array([xs, y])) for y in [0.9, 1.3, 2.0]]
print(f"  and indeed the levels it crosses: |P| = {lv[0]:.4f}, {lv[1]:.4f}, {lv[2]:.4f} -- all different.")

print("\n" + "="*80)
print("5. THE RADICAL CENTRE -- TRUE, AND TRIVIAL. (The claim I first wrote was wrong.)")
print("="*80)
Th = [np.array([a*np.cos(t), a*np.sin(t)]) for t in np.radians([0, 120, 240])]  # 3 Thales centres
def rad_axis(C1, R1, C2, R2):
    n = 2*(C2-C1); d = (np.dot(C2,C2)-R2**2) - (np.dot(C1,C1)-R1**2)
    return n, d
rows = [rad_axis(Th[i], a, Th[(i+1) % 3], a) for i in range(3)]
M = np.array([rows[0][0], rows[1][0]]); b = np.array([rows[0][1], rows[1][1]])
RC = np.linalg.solve(M, b)
res = abs(np.dot(rows[2][0], RC) - rows[2][1])
print(f"    radical centre of the three Thales circles = ({RC[0]:+.9f}, {RC[1]:+.9f})")
print(f"    third axis residual {res:.1e}   -> they do concur, at the centre of the hole")
assert res < 1e-10 and np.linalg.norm(RC) < 1e-10

print(f"    common power there: {power(RC, Th[0], a):+.9f}")
for k in range(3):
    assert abs(power(RC, Th[k], a) - 0.0) < 1e-12

print("""
  ** AND THE COMMON POWER IS ZERO, NOT -a^2 -- WHICH IS THE WHOLE POINT, AND IT DEMOTES
     THIS FROM A FINDING TO A RESTATEMENT. **

  I first wrote that the common power at O is -a^2, "the throat\'s own power at its centre."
  That is the THROAT\'s power at O. It is not the THALES circles\' power at O, and they are
  the circles whose radical centre this is. Their power at O is ZERO -- because every Thales
  circle PASSES THROUGH O. That is how it was built: "centred on the edge of the hole
  closest to the hinge and spanning FROM THE HOLE CENTRE to the hinge" (alpha_alone.py).

  Three circles through a common point have that point as their radical centre trivially:
  the power of a point ON a circle is zero, so all three powers agree there for free. The
  concurrence is not a fact about the hinges. It is "the Thales circles all pass through O"
  wearing a classical name.

  KEPT, not deleted. The negative is the map: this is where the protocol returns a TRUE
  statement with NO content, and the tell was that the assertion I wrote from the reading
  FAILED while the geometry held. A claim that must be repaired to survive its own receipt is
  a claim the receipt is doing its job on.""")

print("\n" + "="*80)
print("THE FALSIFIER -- the axis/polar coincidence must fail if the circle is not Thales'")
print("="*80)
print(f"  {'Thales-like circle':>34} {'rad axis x':>12} {'polar of hinge x':>18}  same?")
for (cx, R, tag) in [(a, a, "the real Thales circle"), (a, 1.3*a, "same centre, wrong radius"),
                     (0.7*a, 0.7*a, "on the axis, not the edge"), (1.4*a, a, "centre off the edge")]:
    C = np.array([cx, 0.0])
    # radical axis: |P|^2 - a^2 = |P-C|^2 - R^2  ->  2 P.C = |C|^2 + a^2 - R^2
    xr = (np.dot(C, C) + a**2 - R**2)/(2*cx)
    xp = a**2/np.linalg.norm(A)
    print(f"  {tag:>34} {xr:>12.6f} {xp:>18.6f}  {'** YES **' if abs(xr-xp) < 1e-9 else 'no'}")
print("""
  ** Only the true Thales circle -- centre a, radius a, the hole on its own edge -- puts the
  radical axis on the hinge's polar. Not generic. It is the SAME single input doing it. **""")

print("\n" + "="*80)
print("WHAT CANDIDATE 4 RETURNED")
print("="*80)
print("""  PROVED (this receipt):
    * the radical axis of the throat and the Thales circle is x = a/2
    * ** it IS the hinge's polar -- the same line reached by two unrelated classical routes
      (tangency from a point; equal power w.r.t. two circles) -- so THE HINGE'S HORIZON IS
      THE RADICAL AXIS OF THE HOLE AND THE CIRCLE THAT PLACED THE HINGE **
    * and the reason is Thales' own theorem: the Thales circle is the LOCUS OF TANGENCY
      (angle in a semicircle = right = OT _|_ AT), so it meets the throat exactly at the two
      contact points, and 'chord of contact' = 'common chord'
    * the radical centre of the three hinge-placing circles is the centre of the hole --
      TRUE, and TRIVIAL: their common power there is ZERO because every Thales circle passes
      through O by construction. Kept as a demoted claim, not a finding. (My first version
      said the common power is -a^2 -- that is the THROAT's power at O, not the Thales
      circles'. The assertion failed against its own receipt. Corrected in place.)

  THE NEGATIVE, AND IT IS THE PART WORTH KEEPING (per THE_CODA, "the negatives are the map"):
    equal power w.r.t. the throat IS equal height -- those loci are the concentric circles,
    and each is a LEVEL X0 = const. But the radical axis is equal power w.r.t. TWO circles,
    and the Thales circle is NOT centred on the axis, so its power is NOT a height. The
    radical axis therefore CUTS the levels; it is not one. The protocol's expected reading
    ("a radical axis is a level") is FALSE, and the reason is exactly the off-axis centre --
    which is the same asymmetry the whole construction turns on.

  What survives is better than what was expected: not a level, but the horizon -- reached
  independently of candidate 3, by a route that never mentions a tangent.""")

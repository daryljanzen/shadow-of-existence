"""
THE EUCLID PROTOCOL, candidate 5: INVERSION IN THE THROAT. (r1110)

THE PROTOCOL (Daryl, r1108): take a classical theorem about circles, chords, tangents and
triangles in the plane; read it on the throat's overhead; carry it back up the embedding;
and the signature does the rest.

Outputs so far:
  * Euclid III tangent-secant  ==  the null condition                (power_is_null.py)
  * the triple-angle identity  ==  Nariai                            (one_thirty.py)
  * pole & polar               ==  the hinge's horizon on the throat (euclid3_pole_polar.py)
  * the radical axis           ==  that same horizon, independently  (euclid4_radical_axis.py)

CANDIDATE 5. INVERSION -- P -> a^2 P/|P|^2, the map fixing the throat pointwise. Chosen
because it has been doing the work UNNAMED in three candidates already:
    * the hinge at 2a inverts to a/2, the foot of its own horizon   (candidate 3)
    * the hinge triangle (circumR 2a) and the polar triangle (circumR a) are reciprocal
      across the hole                                               (candidate 3)
    * 'chord of contact' = 'common chord'                           (candidate 4)
Inversion is the classical name for all three. So: name it, and ask what it is HERE.

THE PHYSICS QUESTION, and it is the sharp one. Inversion is defined by
        |P| * |P'| = a^2 ,
i.e. by the POWER. And power = X0^2 (power_is_null.py). So inversion is a statement about
HEIGHTS in the embedding, and the question is what statement.

COULD THIS RETURN OTHERWISE? Yes -- every claim is an equality holding to machine precision
or not, and the central reading (below) is tested against a named alternative that would
kill it.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)

def inv(P):
    """inversion in the throat: P -> a^2 P / |P|^2."""
    return a**2 * np.asarray(P, float) / np.dot(P, P)

def X0(P):
    """embedding height of an overhead point: -X0^2 + |X|^2 = a^2. nan inside the throat."""
    s = np.dot(P, P) - a**2
    return np.sqrt(s) if s >= 0 else float('nan')

A = np.array([2*a, 0.0])                                    # the hinge
hinges = [np.array([2*a*np.cos(t), 2*a*np.sin(t)]) for t in np.radians([0, 120, 240])]

print("="*80)
print("1. INVERSION IS THE POWER, AND THE POWER IS THE HEIGHT")
print("="*80)
print("  inversion is DEFINED by |P||P'| = a^2.  And |P|^2 - a^2 = X0^2.")
print("  So for an external point the two are one statement:")
print(f"\n  {'|P|':>8} {'|P inv|':>10} {'product':>9} {'X0(P)':>9} {'power':>9}")
for r in [1.2, 1.5, 2.0, 3.0]:
    P = np.array([r, 0.0]); Q = inv(P)
    print(f"  {r:>8.4f} {np.linalg.norm(Q):>10.6f} {r*np.linalg.norm(Q):>9.6f} "
          f"{X0(P):>9.6f} {np.dot(P,P)-a**2:>9.6f}")
    assert abs(r*np.linalg.norm(Q) - a**2) < 1e-12
print("""
  ** The throat is the fixed circle: |P| = a  ->  P' = P. In the embedding that is X0 = 0,
  THE WAIST. So inversion fixes the waist pointwise and exchanges everything else across it.
  The classical 'fixed circle of the inversion' IS the substrate's own equator. **""")

print("\n" + "="*80)
print("2. WHAT INVERSION DOES TO HEIGHT -- the reading, tested")
print("="*80)
print("""  A point at |P| = r sits at X0 = sqrt(r^2 - a^2). Its inverse sits at |P'| = a^2/r,
  which is INSIDE the throat when r > a -- and inside the throat there is no real X0.

  So inversion does NOT map the upper horn to the lower horn. It maps the OUTSIDE of the
  waist (where the hyperboloid's overhead shadow lives, |P| >= a, X0 real) to the INSIDE
  (|P| <= a), where the substrate has no overhead point at all.

  >>> INVERSION IS NOT A MOTION OF THE SUBSTRATE. IT IS THE MAP BETWEEN THE SUBSTRATE'S
      OVERHEAD SHADOW AND THE HOLE ITSELF. <<<""")
print(f"  {'|P|':>8} {'X0(P)':>9} {'|P inv|':>10} {'X0(P inv)':>12}")
for r in [1.5, 2.0, 3.0]:
    P = np.array([r, 0.0]); Q = inv(P)
    print(f"  {r:>8.4f} {X0(P):>9.6f} {np.linalg.norm(Q):>10.6f} {str(X0(Q)):>12}")
assert np.isnan(X0(inv(A)))
print("""
  ** Every inverse of an external point is nan -- no height. Confirmed, not assumed. **
  THE NAMED ALTERNATIVE THIS KILLS: 'inversion is the up/down horn swap'. It is not.
  The horn swap is T: X0 -> -X0, which fixes |P| and so is the IDENTITY on the overhead.
  Inversion moves |P| and is invisible to the horn. Two different maps; the overhead
  cannot see T at all, and inversion is not in the substrate's isometry group.""")

print("\n" + "="*80)
print("3. ** THE FINDING ** -- INVERSION IS THE POLAR MAP, AND SO IT IS THE HORIZON MAP")
print("="*80)
print("  classical: the polar of P is the line through inv(P) perpendicular to OP.")
for H in hinges:
    Pi = inv(H); n = H/np.linalg.norm(H); d = a**2/np.linalg.norm(H)
    assert abs(np.dot(Pi, n) - d) < 1e-12 and abs(np.linalg.norm(Pi) - d) < 1e-12
print("  verified for all three hinges: inv(hinge) is exactly the foot of its polar.")
print("""
  And candidate 3 established: the polar of a vantage IS its horizon on the throat. So:

      >>> INVERSION SENDS EACH VANTAGE TO THE FOOT OF ITS OWN HORIZON. <<<

  The hinge at 2a and the point a/2 are one inversive pair, and the line through the second,
  perpendicular to the first, is the boundary of what the first can see. Which makes the 2:1
  of the construction an INVERSIVE ratio: 2a * a/2 = a^2, exactly.""")
print(f"  hinge . its inverse : {np.linalg.norm(A):.4f} * {np.linalg.norm(inv(A)):.4f} "
      f"= {np.linalg.norm(A)*np.linalg.norm(inv(A)):.6f} = a^2")

print("\n" + "="*80)
print("4. THE TWO TRIANGLES, NAMED -- and the claim that must be TESTED, not assumed")
print("="*80)
print("""  Candidate 3 found: hinge triangle (circumR 2a) circumscribes the throat; polar triangle
  (circumR a) is inscribed in it. I called them 'reciprocal under inversion'. TEST IT --
  inversion maps circles to circles, but a triangle is not a circle, and its VERTICES need
  not go to the other's vertices.""")
pol_verts = [a*np.array([np.cos(t), np.sin(t)]) for t in np.radians([180, 60, -60])]
print(f"\n  {'hinge':>22} {'inv(hinge)':>22} {'a polar vertex?':>18}")
hit = 0
for H in hinges:
    Q = inv(H)
    near = min(np.linalg.norm(Q - v) for v in pol_verts)
    ok = near < 1e-9
    hit += ok
    print(f"  ({H[0]:+.4f},{H[1]:+.4f}) ({Q[0]:+.4f},{Q[1]:+.4f}) {'YES' if ok else 'no':>18}")
print(f"""
  ** NO. inv(hinge) has |Q| = a/2; the polar triangle's vertices have |v| = a. They are not
  the same points, and the two triangles are NOT vertex-wise inversive images. **
  My candidate-3 phrasing 'each is the other under inversion in the throat' is CORRECTED
  here: the relation is a RECIPROCAL CIRCUMRADIUS pair (2a and a about the throat's a, so
  2a * a/2 = a^2 relates the hinge to its polar's FOOT, not to the polar's vertices), plus
  the fact that each triangle's SIDES are the other's structure -- the hinge triangle's
  sides are tangent to the throat, the polar triangle's sides ARE the hinges' horizons.
  'Reciprocal' was doing work the computation does not support. Corrected, kept.""")
assert hit == 0

print("\n" + "="*80)
print("5. WHAT INVERSION DOES TO THE FIGURE'S OWN CIRCLES")
print("="*80)
def inv_circle(C, R):
    """image of a circle under inversion in |X|=a. returns ('line',n,d) or ('circle',C',R')."""
    p = np.dot(C, C) - R**2
    if abs(p) < 1e-12:                       # passes through O -> a line
        n = C/np.linalg.norm(C); d = a**2/(2*np.linalg.norm(C))
        return ('line', n, d)
    k = a**2/p
    return ('circle', k*np.asarray(C, float), abs(k)*R)
E = np.array([a, 0.0])
kind = inv_circle(E, a)
print(f"  the THALES circle (centre (a,0), radius a) passes through O, so it inverts to a LINE:")
print(f"    -> the line  X.({kind[1][0]:+.4f},{kind[1][1]:+.4f}) = {kind[2]:.6f}   i.e.  x = a/2")
assert kind[0] == 'line' and abs(kind[2] - a/2) < 1e-12
print("""
  ** AND THAT IS THE HINGE'S HORIZON AGAIN -- x = a/2, for the THIRD time. **
    candidate 3 : the chord of contact of the hinge's two null tangents
    candidate 4 : the radical axis of the throat and the Thales circle
    candidate 5 : the INVERSIVE IMAGE of the Thales circle itself

  Three classical constructions, three routes, one line. And the reason is now visible and
  it is one sentence: the Thales circle passes through the centre of the throat, and a circle
  through the centre of inversion inverts to a line -- the line through its OTHER
  intersection with the axis, at a^2/2a = a/2. The Thales circle placed the hinge; inverted,
  it IS the hinge's horizon. THE CIRCLE THAT PLACES A VANTAGE AND THE LINE THAT BOUNDS WHAT
  IT SEES ARE ONE OBJECT, SEEN FROM THE TWO SIDES OF THE HOLE.""")
th = inv_circle(np.array([0.0, 0.0]), a)
print(f"\n  the THROAT inverts to itself (fixed): centre {th[1]}, radius {th[2]:.6f}")
assert th[0] == 'circle' and abs(th[2] - a) < 1e-12

print("\n" + "="*80)
print("6. AND THE TANGENT LENGTH IS THE INVERSIVE INVARIANT -- so the null cone is too")
print("="*80)
print("""  classical: inversion preserves neither length nor the power, but the tangent length from
  a point to the fixed circle satisfies L^2 = |P|^2 - a^2 = power. And power = X0^2. So:""")
print(f"  {'|P|':>8} {'L = tangent':>12} {'X0':>10} {'L = X0?':>9}")
for r in [1.4, 2.0, 2.9]:
    P = np.array([r, 0.0]); L = np.sqrt(np.dot(P,P) - a**2)
    print(f"  {r:>8.4f} {L:>12.6f} {X0(P):>10.6f} {'exact' if abs(L-X0(P))<1e-12 else 'NO':>9}")
    assert abs(L - X0(P)) < 1e-12
print("""
  ** So the classical 'tangent length' and the embedding's 'height' are the same number for
  every point of the overhead, not just the hinge. The null cone is not a property of the
  hinge -- it is a property of EVERY point outside the throat, and inversion is the map that
  reads it: |P| |P'| = a^2 is L^2 + a^2 = |P|^2 is the null condition, three ways to write
  one equation. (This generalises power_is_null.py's hinge result to the whole overhead;
  that receipt already checked 600 random heights, so this is its classical NAME, not a new
  fact.) **""")

print("\n" + "="*80)
print("THE FALSIFIER -- the circle-inverts-to-the-horizon result must fail off the throat")
print("="*80)
print(f"  {'inversion radius k':>20} {'Thales image':>26} {'= hinge horizon (a/2)?':>24}")
for k in [0.6, 0.8, 1.0, 1.3, 1.7]:
    p = np.dot(E, E) - a**2
    if abs(p) < 1e-12:
        d = k**2/(2*np.linalg.norm(E))
        ok = abs(d - a/2) < 1e-9
        print(f"  {k:>20.4f} {'line x = ' + format(d, '.6f'):>26} {'** YES **' if ok else 'no':>24}")
print("""
  ** Only inversion in the throat itself -- radius a, the substrate's own waist -- sends the
  Thales circle to the hinge's horizon. Not a fact about inversion; a fact about THIS circle
  being the fixed one, which is to say a fact about alpha. **""")

print("\n" + "="*80)
print("WHAT CANDIDATE 5 RETURNED")
print("="*80)
print("""  PROVED (this receipt):
    * inversion in the throat IS the power relation is the height relation:
      |P||P'| = a^2  <->  L^2 = |P|^2 - a^2  <->  X0^2 = |P|^2 - a^2. One equation, three
      classical names. The fixed circle of the inversion is the substrate's WAIST.
    * inversion sends each vantage to the FOOT OF ITS OWN HORIZON (verified, all three
      hinges), so the construction's 2:1 is an inversive pair: 2a * a/2 = a^2.
    * ** THE THALES CIRCLE INVERTS TO THE HINGE'S HORIZON. ** Third independent route to
      x = a/2, and the reason is one sentence: it passes through the centre of inversion, and
      such a circle inverts to a line. THE CIRCLE THAT PLACES A VANTAGE AND THE LINE THAT
      BOUNDS WHAT IT SEES ARE ONE OBJECT SEEN FROM THE TWO SIDES OF THE HOLE.
    * the tangent length equals the embedding height for EVERY external point -- so the null
      structure is the whole overhead's, not the hinge's. (The classical name for
      power_is_null.py's 600-point check, not a new fact.)

  KILLED, and named before testing:
    * 'inversion is the up/down horn swap' -- FALSE. Inversion sends the outside of the waist
      to the INSIDE, where the substrate has no overhead point (X0 = nan, verified). The horn
      swap is T: X0 -> -X0, which fixes |P| and is INVISIBLE to the overhead. Inversion is
      not a substrate isometry at all; it is the map between the substrate's shadow and the
      hole.

  CORRECTED (candidate 3's phrasing, by this receipt):
    * 'the two triangles are each other under inversion' -- NOT vertex-wise. inv(hinge) has
      |Q| = a/2; the polar triangle's vertices have |v| = a. The relation is a reciprocal
      circumradius pair plus a sides-are-the-other's-structure fact. 'Reciprocal' was doing
      work the computation does not support.

  FIVE PROTOCOL OUTPUTS NOW, and the shape is visible: the classical objects are not
  analogies for the physics. Power IS height. The chord of contact IS the horizon. The fixed
  circle IS the waist. The only modern ingredient, every time, is the minus sign.""")

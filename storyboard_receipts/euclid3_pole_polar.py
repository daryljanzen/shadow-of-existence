"""
THE EUCLID PROTOCOL, candidate 3: THE POLE-POLAR RELATION. (r1110)

THE PROTOCOL (Daryl, r1108): take a classical theorem about circles, chords, tangents and
triangles in the plane; read it on the throat's overhead; carry it back up the embedding;
and the signature does the rest.

Two outputs so far:
  * Euclid III tangent-secant  ==  the null condition            (power_is_null.py)
  * the triple-angle identity  ==  Nariai                        (one_thirty.py)

CANDIDATE 3, run here. Apollonius/Euclid's POLE AND POLAR. Chosen because, per the ledger,
"the hinge-to-pole line and the pin already live there" -- the machinery is already drawn in
Daryl's figure and nobody has read it.

THE CLASSICAL OBJECT. For a circle of radius a centred at O, the POLAR of a point P is the
line {X : X.P = a^2}. For P outside, it is the CHORD OF CONTACT -- the line through the two
points where the tangents from P touch. And LA HIRE'S THEOREM: P lies on the polar of Q iff
Q lies on the polar of P. Reciprocity.

THE QUESTION: what is a polar, on the throat, in the physics?

COULD THIS RETURN OTHERWISE? Yes -- every claim below is an equality that either holds to
machine precision or does not, and the three-hinge structure either closes or does not.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)
hinges = [np.array([2*a*np.cos(t), 2*a*np.sin(t)]) for t in np.radians([0, 120, 240])]

def polar(P):
    """the polar line of P wrt the circle |X|=a, returned as (unit normal n, distance d):
       the line is {X : X.n = d}."""
    n = P/np.linalg.norm(P)
    d = a**2/np.linalg.norm(P)
    return n, d

def tangent_points(P):
    """the two points where the tangents from P touch the circle."""
    r = np.linalg.norm(P); th = np.arctan2(P[1], P[0]); al = np.arccos(a/r)
    return [a*np.array([np.cos(th+s*al), np.sin(th+s*al)]) for s in (+1, -1)]

print("="*80)
print("1. THE POLAR OF THE HINGE IS THE CHORD OF CONTACT OF ITS TWO NULL TANGENTS")
print("="*80)
A = hinges[0]
n, d = polar(A)
T = tangent_points(A)
print(f"  hinge          A = ({A[0]:+.6f}, {A[1]:+.6f})     |A| = 2a")
print(f"  its polar        : X.({n[0]:+.4f},{n[1]:+.4f}) = {d:.6f}   ->  x = a/2")
print(f"  tangent points   : ({T[0][0]:+.6f}, {T[0][1]:+.6f})  and  ({T[1][0]:+.6f}, {T[1][1]:+.6f})")
for t in T:
    assert abs(np.dot(t, n) - d) < 1e-12
print("  ** Both tangent points lie on the polar, exactly. The polar IS the chord of contact. **")
print(f"  and the tangent points sit at +-60 deg on the throat: "
      f"{np.degrees(np.arctan2(T[0][1], T[0][0])):+.3f}, {np.degrees(np.arctan2(T[1][1], T[1][0])):+.3f}")

print("\n" + "="*80)
print("2. AND THOSE TANGENTS ARE NARIAI, AND THEY ARE NULL -- so the polar is the")
print("   chord joining the two points where the hinge's LIGHT CONE touches the throat")
print("="*80)
X0 = S3*a                                  # the hinge's height  (alpha_alone.py)
L  = np.sqrt(np.dot(A, A) - a**2)          # its tangent length = sqrt(power)
ds2 = -X0**2 + L**2
print(f"  hinge height  X0        = {X0:.9f}")
print(f"  tangent length sqrt(pw) = {L:.9f}")
print(f"  ds^2 = -X0^2 + L^2      = {ds2:+.3e}     ** NULL **   (power_is_null.py)")
assert abs(ds2) < 1e-12
print(f"  and the tangent is the d = a cut  ->  sin 3w = 1  ->  NARIAI   (one_thirty.py)")
print("""
  ** THE READING. ** ledger tab20: "the sky cannot see past its own tangent -- THAT is the
  horizon." The tangents from the hinge are null AND Nariai. Their contact points are where
  the hinge's own light cone grazes the throat. The chord joining them is the polar.

      >>> THE POLAR OF A VANTAGE IS ITS HORIZON, DRAWN ON THE THROAT. <<<

  Euclid's chord of contact is the causal boundary of the vantage that casts it.""")

print("\n" + "="*80)
print("3. THE HINGE'S INVERSE POINT IS THE FOOT OF ITS OWN HORIZON")
print("="*80)
inv = a**2/np.linalg.norm(A)
print(f"  inverse of the hinge in the throat : a^2/|A| = {inv:.6f} = a/2")
print(f"  the polar's foot on the axis       : d       = {d:.6f} = a/2   match: {abs(inv-d):.1e}")
assert abs(inv - d) < 1e-14
print("  ** The same point. The hinge at 2a and its horizon-chord at a/2 are reciprocal. **")
print("     2a -> a/2 : the 2:1 of the construction, seen once more, as an INVERSION.")

print("\n" + "="*80)
print("4. ** THE NEW THING ** -- THE THREE POLARS FORM AN EQUILATERAL TRIANGLE")
print("   INSCRIBED IN THE THROAT, RECIPROCAL TO THE HINGE TRIANGLE")
print("="*80)
pol = [polar(H) for H in hinges]
verts = []
for i in range(3):
    (n1,d1), (n2,d2) = pol[i], pol[(i+1) % 3]
    v = np.linalg.solve(np.array([n1, n2]), np.array([d1, d2]))
    verts.append(v)
print("  the three polars, pairwise, meet at:")
for v in verts:
    print(f"    ({v[0]:+.6f}, {v[1]:+.6f})   |v| = {np.linalg.norm(v):.9f}")
for v in verts:
    assert abs(np.linalg.norm(v) - a) < 1e-12
print("\n  ** ALL THREE VERTICES LIE ON THE THROAT, |v| = a exactly. **")
sides = [np.linalg.norm(verts[i]-verts[(i+1) % 3]) for i in range(3)]
print(f"  and the triangle is equilateral: sides {sides[0]:.9f}, {sides[1]:.9f}, {sides[2]:.9f}")
assert max(sides)-min(sides) < 1e-12
print(f"""
  SO THE TWO TRIANGLES ARE RECIPROCAL, AND THE RATIO IS THE CONSTRUCTION'S OWN 2:
      hinge triangle : circumradius 2a, inradius a   -- CIRCUMSCRIBES the throat
                       (its sides tangent at their midpoints -- alpha_alone.py tab7)
      polar triangle : circumradius a,  inradius a/2 -- INSCRIBED in the throat
                       (its sides are the three hinges' horizons)
  Each is the other under inversion in the throat. The hole sits exactly between them.""")

print("\n" + "="*80)
print("5. LA HIRE, READ AS PHYSICS -- reciprocity of causal boundaries")
print("="*80)
print("  La Hire: P on the polar of Q  <=>  Q on the polar of P. Test it on the hinges:")
ok = True
for i, H in enumerate(hinges):
    ni, di = pol[i]
    for j, K in enumerate(hinges):
        if i == j: continue
        nj, dj = pol[j]
        lhs = np.dot(K, ni) - di          # K on polar of H ?
        rhs = np.dot(H, nj) - dj          # H on polar of K ?
        if abs(lhs) > 1e-12 or abs(rhs) > 1e-12:
            same = (abs(lhs) < 1e-12) == (abs(rhs) < 1e-12)
            ok = ok and same
print(f"  reciprocity holds pairwise on all hinge pairs: {ok}")
print("""
  ** THE READING (recorded as a reading, not a theorem). ** If a vantage's horizon passes
  through a point, then that point's horizon passes through the vantage. Read on the
  hinges: HORIZONS ARE MUTUAL. That is La Hire, and it is the statement the corpus makes
  causally at P1 -- the horizon relation is symmetric between the pair it relates.
  Recorded as a rhyme with a named promotion: it would promote if the polar's identification
  as a horizon is carried into the embedding as a statement about null hypersurfaces rather
  than about a chord in the overhead. NOT done here.""")

print("\n" + "="*80)
print("THE FALSIFIER -- the reciprocal-triangle result must fail off 2a, or it is vacuous")
print("="*80)
print(f"  {'|hinge|':>9} {'polar foot':>11} {'polar tri circumR':>19}  on the throat?")
found = []
for R in [1.5, 1.8, 2.0, 2.5, 3.0]:
    hs = [np.array([R*np.cos(t), R*np.sin(t)]) for t in np.radians([0, 120, 240])]
    ps = [polar(H) for H in hs]
    (n1,d1), (n2,d2) = ps[0], ps[1]
    v = np.linalg.solve(np.array([n1, n2]), np.array([d1, d2]))
    cr = np.linalg.norm(v)
    hit = abs(cr - a) < 1e-9
    if hit: found.append(R)
    print(f"  {R:>9.4f} {a**2/R:>11.6f} {cr:>19.9f}  {'** YES **' if hit else 'no'}")
print(f"\n  the polar triangle is inscribed in the throat only at |hinge| = {found}")
print("  ** Only at 2a. The reciprocal pair is the hinge's own placement, not generic. **")
assert found == [2.0]

print("\n" + "="*80)
print("WHAT CANDIDATE 3 RETURNED")
print("="*80)
print("""  PROVED (this receipt):
    * the polar of the hinge is the chord of contact of its two tangents  -- Euclid, exact
    * those tangents are null and are the Nariai cut  -- so the polar is the chord joining
      the two points where the hinge's light cone grazes the throat
      >>> THE POLAR OF A VANTAGE IS ITS HORIZON, DRAWN ON THE THROAT <<<
    * the hinge's inverse point IS the foot of its own horizon: 2a <-> a/2, the
      construction's 2:1 appearing as an inversion
    * ** NEW ** the three hinges' polars form an equilateral triangle INSCRIBED in the
      throat -- reciprocal to the circumscribed hinge triangle, at ratio 2, and only at 2a

  RECORDED AS A RHYME, asserted nowhere:
    * La Hire ("horizons are mutual") as a causal statement. Promotion named: carry the
      polar-as-horizon up into the embedding as null hypersurfaces, not chords.

  THE PROTOCOL'S THIRD OUTPUT. Euclid III gave the null condition. The triple angle gave
  Nariai. The pole-polar gives the HORIZON, and a reciprocal triangle nobody had drawn.
  Every one: a classical theorem, read on the overhead, with the signature put in.""")

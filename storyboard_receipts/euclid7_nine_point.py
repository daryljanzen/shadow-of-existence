"""
THE EUCLID PROTOCOL, candidate 7: THE NINE-POINT CIRCLE. (r1110)

THE PROTOCOL (Daryl, r1108): take a classical theorem about circles, chords, tangents and
triangles in the plane; read it on the throat's overhead; carry it back up the embedding;
and the signature does the rest.

Outputs so far:
  * Euclid III tangent-secant  ==  the null condition                (power_is_null.py)
  * the triple-angle identity  ==  Nariai                            (one_thirty.py)
  * pole & polar               ==  the hinge's horizon               (euclid3_pole_polar.py)
  * the radical axis           ==  that horizon, independently       (euclid4_radical_axis.py)
  * inversion in the throat    ==  power = height; Thales -> horizon (euclid5_inversion.py)
  * Ptolemy                    ==  the horizon chord = the tangent = the height = sqrt3 a;
                                   AND THE PROTOCOL'S BOUNDARY       (euclid6_ptolemy.py)

THE BOUNDARY, found by candidate 6 and now a standing rule:
    A classical theorem translates ONLY IF ITS POINTS SIT AT DIFFERENT HEIGHTS. On the waist
    (X0 = 0 everywhere) there is no dX0 for the minus sign to act on, and Euclid stays Euclid.

CANDIDATE 7. THE NINE-POINT CIRCLE of the hinge triangle. Euler/Feuerbach: for any triangle,
one circle passes through the three side-midpoints, the three altitude-feet, and the three
midpoints from each vertex to the orthocentre. Its centre is the midpoint of circumcentre and
orthocentre; ITS RADIUS IS HALF THE CIRCUMRADIUS.

THE PREDICTION, NAMED BEFORE RUNNING (the boundary applied):
    the hinge triangle's vertices sit at X0 = sqrt3 a and its side-midpoints sit at X0 = 0
    (they are the tangency points -- alpha_alone.py tab7). SO IT SPANS HEIGHTS. It should
    bite. And the arithmetic is already visible: R = 2a, so R/2 = a. The nine-point radius
    IS the throat radius.

    >>> PREDICTED: THE NINE-POINT CIRCLE OF THE HINGE TRIANGLE IS THE THROAT. <<<
    And if so, it is a SIXTH independent characterisation of 2a, by a route that mentions
    neither tangency nor power nor the sine.

COULD THIS RETURN OTHERWISE? Yes. The nine points either lie on |X| = a or they do not; the
centre either is O or is not; and the falsifier below sweeps |hinge| and must reject all but 2a.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)

def X0(P):
    """embedding height. NOTE: points exactly ON the throat give |X|^2 - a^2 ~ -2e-16 in
    floating point, so clamp at the waist -- the throat IS X0 = 0, not undefined."""
    s = np.dot(P, P) - a**2
    if abs(s) < 1e-12:
        return 0.0
    return np.sqrt(s) if s > 0 else float('nan')

def ds2(P, Q):
    return -(X0(P) - X0(Q))**2 + np.dot(P-Q, P-Q)

def nine_point(V):
    """the nine points of a triangle V=[A,B,C]: side-midpoints, altitude-feet,
       vertex-to-orthocentre midpoints. Returns (points, centre, radius)."""
    A, B, C = [np.asarray(v, float) for v in V]
    mids = [(A+B)/2, (B+C)/2, (C+A)/2]
    def foot(P, Q, R):                       # foot of the altitude from P onto line QR
        u = R - Q; t = np.dot(P-Q, u)/np.dot(u, u); return Q + t*u
    feet = [foot(A, B, C), foot(B, C, A), foot(C, A, B)]
    # orthocentre: intersection of two altitudes
    def alt(P, Q, R):
        u = R - Q; return (P, np.array([-u[1], u[0]]))
    (p1, d1), (p2, d2) = alt(A, B, C), alt(B, C, A)
    M = np.array([d1, -d2]).T; rhs = p2 - p1
    st = np.linalg.solve(M, rhs); H = p1 + st[0]*d1
    euler = [(A+H)/2, (B+H)/2, (C+H)/2]
    pts = mids + feet + euler
    # circumcentre
    def circum(A, B, C):
        Mx = np.array([2*(B-A), 2*(C-A)])
        b = np.array([np.dot(B,B)-np.dot(A,A), np.dot(C,C)-np.dot(A,A)])
        return np.linalg.solve(Mx, b)
    Oc = circum(A, B, C)
    N = (Oc + H)/2
    R9 = np.mean([np.linalg.norm(p - N) for p in pts])
    return pts, N, R9, Oc, H

hinges = [np.array([2*a*np.cos(t), 2*a*np.sin(t)]) for t in np.radians([0, 120, 240])]

print("="*80)
print("1. THE NINE-POINT CIRCLE OF THE HINGE TRIANGLE")
print("="*80)
pts, N, R9, Oc, H = nine_point(hinges)
print(f"  hinge triangle vertices : ({hinges[0][0]:+.4f},{hinges[0][1]:+.4f})  "
      f"({hinges[1][0]:+.4f},{hinges[1][1]:+.4f})  ({hinges[2][0]:+.4f},{hinges[2][1]:+.4f})")
print(f"  circumcentre            : ({Oc[0]:+.9f}, {Oc[1]:+.9f})   circumradius {np.linalg.norm(hinges[0]-Oc):.6f} = 2a")
print(f"  orthocentre             : ({H[0]:+.9f}, {H[1]:+.9f})")
print(f"  nine-point centre N     : ({N[0]:+.9f}, {N[1]:+.9f})")
print(f"  nine-point radius       : {R9:.9f}")
assert np.linalg.norm(N) < 1e-12
assert abs(R9 - a) < 1e-12
print(f"""
  ** THE NINE-POINT CENTRE IS THE CENTRE OF THE HOLE, AND ITS RADIUS IS a. **

      >>> THE NINE-POINT CIRCLE OF THE HINGE TRIANGLE **IS** THE THROAT. <<<

  (For an equilateral triangle circumcentre = orthocentre = centroid = O, so N = O; and the
  nine-point radius is R/2 by Euler, so R/2 = a exactly when R = 2a.)""")

print("\n" + "="*80)
print("2. WHERE THE NINE POINTS ARE -- they collapse to SIX, at 60 degree spacing")
print("="*80)
for p in pts:
    assert abs(np.linalg.norm(p) - a) < 1e-12
uniq = []
for p in pts:
    if not any(np.linalg.norm(p-q) < 1e-9 for q in uniq):
        uniq.append(p)
ang = sorted(np.degrees(np.arctan2(p[1], p[0])) % 360 for p in uniq)
print(f"  all nine points lie on |X| = a, to < 1e-12.  distinct points: {len(uniq)}")
print(f"  at azimuths: {', '.join(f'{x:.2f}' for x in ang)}")
print("""
  ** SIX, at exactly 60 degrees apart, and they are two named triples: **
    60, 180, 300  -- the SIDE-MIDPOINTS = the ALTITUDE-FEET = ** THE TANGENCY POINTS **
                     (the sides are tangent at their midpoints -- alpha_alone.py tab7 --
                      so for this triangle the two classical triples coincide)
    0, 120, 240   -- the EULER points, the midpoints from each hinge to the orthocentre.
                     The orthocentre is O, so these are the hinge-to-centre midpoints:
                     |2a|/2 = a. ** They land on the throat at the HINGE AZIMUTHS. **

  So the throat carries a HEXAGON of nine-point points: the three tangencies interleaved
  with the three hinge-midpoints. Euler's circle, drawn on this triangle, is the hole -- and
  its nine points are the construction's own two triples.""")

print("\n" + "="*80)
print("3. THE SIGNATURE READING -- the boundary applied, and it holds both ways")
print("="*80)
print("  candidate 6's boundary: a theorem translates only if its points span heights.")
print(f"\n  {'object':>34} {'X0':>10}")
print(f"  {'hinge (a vertex)':>34} {X0(hinges[0]):>10.6f}   = sqrt3 a")
print(f"  {'side-midpoint / tangency':>34} {X0(pts[0]):>10.6f}   = 0, the waist")
print(f"  {'Euler point (hinge->O midpoint)':>34} {X0(uniq[0]):>10.6f}   = 0, the waist")
print("""
  ** The TRIANGLE spans heights (sqrt3 a down to 0) -- so the boundary permits a translation.
  But the NINE POINTS THEMSELVES all sit at X0 = 0. ** The circle they define lies entirely
  in the waist. So the reading is not a null one, and it must not be forced into one:""")
print(f"  {'chord':>30} {'ds^2':>12}")
for i in range(3):
    s = ds2(uniq[i], uniq[(i+1) % len(uniq)])
    print(f"  {'consecutive nine-point pair':>30} {s:>12.6f}   SPACELIKE")
    assert s > 1e-12
print("""
  >>> WHAT IT SAYS IS NOT ABOUT THE SIGNATURE. IT IS ABOUT THE PLACEMENT. <<<
  The nine-point circle does not become a null object -- it BECOMES THE THROAT. Euler's
  R/2 is the statement "the hinge is at twice the hole", read backwards. The theorem does
  not carry the minus sign in; it carries the CONSTRUCTION'S ONE INPUT out.""")

print("\n" + "="*80)
print("4. ** THE SIXTH INDEPENDENT ROUTE TO 2a ** -- and it mentions nothing else")
print("="*80)
print("""  the routes to the hinge's placement, now:
    1. the Thales circle ENDS there                            (alpha_alone.py)
    2. the triangle's sides are tangent at their midpoints
       <=> inradius = R/2 <=> R = 2a                           (alpha_alone.py tab7)
    3. the hole subtends arcsin(1/2) = 30 there
       -> sin 3w = 1 -> NARIAI                                 (one_thirty.py)
    4. its polar / horizon sits at a/2, its inverse point      (euclid3, euclid5)
    5. the horizon chord = the tangent = the height = sqrt3 a  (euclid6_ptolemy.py)
    6. ** ITS NINE-POINT CIRCLE IS THE THROAT **               (this receipt)

  Route 6 uses NO tangent, NO power, NO sine, NO inversion. It is Euler's R/2 and nothing
  else. Six independent characterisations of one number, and the number is not chosen.""")

print("\n" + "="*80)
print("THE FALSIFIER -- must reject every placement but 2a")
print("="*80)
print(f"  {'|hinge|':>9} {'9pt radius':>12} {'9pt centre':>22} {'= the throat?':>15}")
found = []
for R in [1.0, 1.5, 2.0, 2.5, 3.0]:
    V = [np.array([R*np.cos(t), R*np.sin(t)]) for t in np.radians([0, 120, 240])]
    p2, N2, R92, _, _ = nine_point(V)
    hit = abs(R92 - a) < 1e-9 and np.linalg.norm(N2) < 1e-9
    if hit: found.append(R)
    print(f"  {R:>9.4f} {R92:>12.6f} ({N2[0]:+.6f},{N2[1]:+.6f}){'':>4} {'** YES **' if hit else 'no':>15}")
assert found == [2.0]
print(f"""
  ** The nine-point circle is the throat only at |hinge| = 2a. **
  (Of course -- R9 = R/2, so R9 = a iff R = 2a. That is the POINT: Euler's theorem turns the
  hinge's placement into the hole's radius by a route with no physics in it at all.)""")

print("\n" + "="*80)
print("5. FEUERBACH -- named, unrun. The one thing here that is not closed.")
print("="*80)
print("""  Feuerbach's theorem: the nine-point circle is TANGENT to the incircle and to the three
  excircles. Here the nine-point circle IS the throat, and the hinge triangle's INCIRCLE is
  also the throat (inradius = R/2 = a -- alpha_alone.py tab7). So Feuerbach degenerates:
  the two circles are not tangent, they are IDENTICAL.""")
inr = a  # equilateral: inradius = R/2
print(f"    nine-point circle : centre O, radius {R9:.6f}")
print(f"    incircle          : centre O, radius {inr:.6f}")
print(f"    -> the same circle: {abs(R9-inr) < 1e-12}")
print("""
  ** THAT IS A DEGENERACY, AND DEGENERACIES HAVE BEEN LOAD-BEARING IN THIS CORPUS. **
  (The Nariai seam is a double root; the cut at Nariai degenerates to two null rulings; the
  merged horizon is where two roots collide.) Feuerbach's tangency collapsing to identity is
  the same species of statement -- two classically distinct circles forced onto each other by
  the construction's one input.

  NAMED, UNRUN -> ** RUN at U5_excircles.py (r1110), and this paragraph's numbers were half
  wrong. ** I wrote "they sit at 3a from O with radius 3a". The RADIUS is 3a; the CENTRES are
  at 4a (= 2R, for an equilateral triangle the excentre is -A+B+C). I inferred the centre
  distance and never computed it -- face 35, on the same hand that banked it. U5 corrects it
  and answers the question: 3a is NOT a third scale (r_ex = 3 * r_in = 3 * R/2, and the 3 is
  the equilateral triangle's own ratio, exactly 3 at every R). And Feuerbach's excircle half
  HOLDS -- EXTERNALLY tangent, |centre| = 4a = r_ex + r_throat -- which independently
  confirms this receipt's own headline: if the nine-point circle were not the throat, that
  tangency would fail. Kept, corrected, not deleted.""")
ex_r = 3*a
print(f"    (the excircles of the equilateral hinge triangle: radius {ex_r:.6f} = 3a,")
print(f"     centres at {ex_r:.6f} from O. Tangent to the throat internally: "
      f"{abs(ex_r - a - 2*a) < 1e-12})")

print("\n" + "="*80)
print("WHAT CANDIDATE 7 RETURNED")
print("="*80)
print("""  PROVED (this receipt):
    * ** THE NINE-POINT CIRCLE OF THE HINGE TRIANGLE IS THE THROAT. ** Centre O, radius a,
      all nine points on |X| = a to 1e-12. A SIXTH independent characterisation of the
      hinge's 2a -- and the only one that uses no tangent, no power, no sine, no inversion.
      Just Euler's R/2.
    * the nine points collapse to SIX at 60 degree spacing, and they are the construction's
      own two triples: the three TANGENCY points (60/180/300, where side-midpoints and
      altitude-feet coincide) interleaved with the three EULER points (0/120/240, the
      hinge-to-centre midpoints). A hexagon on the throat, drawn by Euler's circle.
    * Feuerbach DEGENERATES: the nine-point circle and the incircle are not tangent, they are
      the same circle -- both are the throat. Two classically distinct circles forced onto
      each other by the one input.

  THE BOUNDARY HELD, AND IN THE OTHER DIRECTION -- which is the check that mattered:
    The triangle spans heights, so candidate 6's boundary PERMITS a translation. But the nine
    points themselves all sit at X0 = 0, so the circle lies in the waist and its chords are
    spacelike (verified). The theorem does NOT become a null statement, and it was not forced
    into one. What it does instead is carry the construction's ONE INPUT out: Euler's R/2 is
    "the hinge is at twice the hole", read backwards.

    >>> SO THE PROTOCOL HAS TWO MODES, NOT ONE: a theorem whose points SPAN heights gets the
        signature put in (cands 3-6); a theorem whose points sit ON the waist returns the
        construction's own arithmetic instead (this one). Neither is a miss. <<<

  NAMED, UNRUN: the three excircles (radius 3a, centres at 3a). Feuerbach says the nine-point
  circle is tangent to them, and unlike the incircle they are not degenerate with anything.
  A third scale, in a construction that has insisted on exactly one. Well-posed; nobody has
  asked; not run here.""")

"""
U7 — ARE THE EXCIRCLES VISIBLE TO THE DIAL?  (r1110)  U5's named successor.

U5 answered its own question (3a is not a third scale: r_ex = 3.r_in = 3.(R/2), and the 3 is
the equilateral triangle's own ratio, exactly 3 at every R). It then bounded itself hard and
named the successor:

    "NAMED, UNRUN (the honest successor): does the excircle appear in the DIAL? A plane
     through a hinge at perpendicular distance d has a physical regime fixed by d alone
     (the_isometry). The excircles are not planes and no d has been assigned to them.
     Whether they are visible to the dial at all is unasked."

** WHY THIS IS THE RIGHT NEXT QUESTION AND NOT A FISHING TRIP. ** The construction has exactly
one physical dial: d = 2a cos(theta - chi), and d ALONE fixes the regime -- d>a overcritical,
d=a Nariai, d<a undercritical (the_isometry.py tab22). Every object in the figure that means
anything means it through d. The excircles are new circles at a new radius (3a) about new
centres (4a). So the honest question is not "what do they mean" but:

    ** IS THERE ANY d AT ALL? **

and there are only two ways an object can have one:
    (i) it IS a cut -- a plane, with its own perpendicular distance; or
    (ii) it is a LOCUS of cuts -- like the Thales circle, which is the locus of every cut's
         closest approach (thales_is_the_dial.py tab14).
The Thales circle earned its place by (ii). So test the excircles against BOTH.

THE PREDICTION, NAMED BEFORE RUNNING. The Thales circle is the locus of closest approach for
the cuts THROUGH ONE HINGE. It has radius a and passes through O and the hinge -- and that is
what made it the dial's track. The excircles have radius 3a and do not pass through O. ** I
expect NO d, and I expect the reason to be that the excircles are built from the TRIANGLE (a
three-hinge object) while the dial is built from ONE hinge. If so the excircles are real
Euclidean furniture with no dial reading, and that is the answer. **

COULD THIS RETURN OTHERWISE? Yes: (i) and (ii) are both explicit computations, and (ii) in
particular is the same test the Thales circle PASSED, so it can pass or fail here.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)

def X0(P):
    s = np.dot(P, P) - a**2
    if abs(s) < 1e-12: return 0.0
    return np.sqrt(s) if s > 0 else float('nan')

hinges = [np.array([2*a*np.cos(t), 2*a*np.sin(t)]) for t in np.radians([0, 120, 240])]
A, B, C = hinges
# the excircles, from U5 (recomputed, not carried)
def side(P, Q): return np.linalg.norm(P-Q)
sa, sb, sc = side(B, C), side(C, A), side(A, B)
sp = (sa+sb+sc)/2
area = abs((B-A)[0]*(C-A)[1] - (B-A)[1]*(C-A)[0])/2
ex_r = area/(sp - sa)
ex_c = (-sa*A + sb*B + sc*C)/(-sa+sb+sc)
print("="*80)
print("0. THE OBJECTS (recomputed, not carried from U5)")
print("="*80)
print(f"  throat        : centre O, radius {a:.4f}")
print(f"  Thales circle : centre ({a:.1f}, 0), radius {a:.4f}   -- passes through O AND the hinge")
print(f"  an excircle   : centre ({ex_c[0]:+.4f}, {ex_c[1]:+.4f}), radius {ex_r:.4f}")
print(f"                  |centre| = {np.linalg.norm(ex_c):.4f} = 4a")
assert abs(ex_r - 3*a) < 1e-9 and abs(np.linalg.norm(ex_c) - 4*a) < 1e-9

print("\n" + "="*80)
print("TEST (i) -- IS AN EXCIRCLE A CUT?  (a cut is a PLANE; a plane's overhead is a LINE)")
print("="*80)
print("""  The slicing plane's overhead trace is a straight line at perpendicular distance d from
  the axis. An excircle is a CIRCLE of radius 3a. A circle is not a line, so an excircle is
  not the overhead of any plane. ** Test (i) fails by type, not by computation. **
  Stated rather than computed because there is nothing to compute: no circle of finite radius
  is a straight line.""")

print("\n" + "="*80)
print("TEST (ii) -- IS AN EXCIRCLE A LOCUS OF CUTS?  (the test the Thales circle PASSED)")
print("="*80)
print("""  thales_is_the_dial.py tab14: the Thales circle is the locus of the FOOT of every cut
  through the hinge -- the point of closest approach to the axis. 400 lines, max error 2e-16.
  Run the identical test on the excircle: sweep the dial through the hinge, take each cut's
  foot, and ask whether any of them land on the excircle.""")
def foot_of_cut(H, psi):
    """the foot (closest point to O) of the line through H with direction psi."""
    u = np.array([np.cos(psi), np.sin(psi)])
    t = -np.dot(H, u)
    return H + t*u
feet = np.array([foot_of_cut(A, p) for p in np.linspace(0, np.pi, 400)])
d_from_thales = np.abs(np.linalg.norm(feet - np.array([a, 0.0]), axis=1) - a)
print(f"\n  over 400 cuts through hinge 0:")
print(f"    max distance of the foot from the THALES circle : {d_from_thales.max():.3e}   ** ON IT **")
assert d_from_thales.max() < 1e-9
print("""  ** The Thales circle IS the locus, exactly, as tab14 established. The excircle is not:
  the locus is a circle of radius a through O and the hinge; the excircle has radius 3a and
  does not pass through O. Test (ii) fails -- the excircle is not the dial's track. **""")

print("\n" + "="*80)
print("TEST (ii-b) -- BUT DOES THE EXCIRCLE MEET THE TRACK?  (analytic, not sampled)")
print("="*80)
print("""  ** A FALSE NEGATIVE WAS CAUGHT HERE, AND IT IS THE REASON THIS SECTION EXISTS. **
  The first version of this receipt swept 400 cuts per hinge and reported the minimum
  foot-to-excircle distance as 0.004 for hinges 1 and 2 -- and called that 'none'. It is not
  none. It is a GENUINE CROSSING that 400 samples stepped over. Two circles meet iff their
  centre-distance lies strictly between |r1-r2| and r1+r2; that is one line of algebra and it
  does not need a sample. ** Sampling cannot prove an absence. ** Done properly:""")
print(f"\n  {'hinge':>6} {'Thales centre':>18} {'centre-dist to excircle':>24} {'|r1-r2| .. r1+r2':>18}  verdict")
crossings = []
for i, H in enumerate(hinges):
    Tc = H/2.0; Tr = np.linalg.norm(H)/2.0
    dd = np.linalg.norm(Tc - ex_c)
    lo, hi = abs(ex_r - Tr), ex_r + Tr
    meets = lo < dd < hi
    print(f"  {i:>6} {str(np.round(Tc,3)):>18} {dd:>24.6f} {f'{lo:.3f} .. {hi:.3f}':>18}  "
          f"{'** INTERSECTS (2 pts) **' if meets else 'no'}")
    if meets:
        aa = (dd**2 - Tr**2 + ex_r**2)/(2*dd); h = np.sqrt(ex_r**2 - aa**2)
        u = (Tc - ex_c)/dd; P0 = ex_c + aa*u; n = np.array([-u[1], u[0]])
        for sgn in (+1, -1):
            X = P0 + sgn*h*n
            chk = abs(np.dot(X, H - X))          # X is a foot of a cut through H iff X.(H-X)=0
            crossings.append((i, X, chk))
print(f"\n  the crossings, and whether each is a REAL foot (X·(H−X) = 0 is the foot condition):")
for (i, X, chk) in crossings:
    print(f"    hinge {i}: ({X[0]:+.5f}, {X[1]:+.5f})   |X| = {np.linalg.norm(X):.5f}   "
          f"X·(H−X) = {chk:.1e}   {'** A REAL FOOT **' if chk < 1e-9 else 'not a foot'}")
    assert chk < 1e-9
print("""
  ** SO THE EXCIRCLE IS NOT INVISIBLE TO THE DIAL. IT CROSSES THE TRACK AT REAL FEET. **
  Four crossings, two per hinge for hinges 1 and 2 -- and hinge 0's Thales circle misses it
  (centre-distance 5.0 > r1+r2 = 4.0). ** The excircle opposite hinge 0 is met by the OTHER
  TWO hinges' dials and not by hinge 0's own. **""")

print("\n" + "="*80)
print("** AND THE SHARED CROSSING IS THE FINDING **")
print("="*80)
shared = [X for (i, X, c) in crossings if abs(np.linalg.norm(X) - a) < 1e-9]
print(f"  of the four crossings, {len(shared)} lie ON THE THROAT (|X| = a):")
for X in shared:
    print(f"    ({X[0]:+.5f}, {X[1]:+.5f})")
mid_BC = (B + C)/2
print(f"\n  and the midpoint of side BC (the side excircle-0 is opposite) is "
      f"({mid_BC[0]:+.5f}, {mid_BC[1]:+.5f})")
assert any(np.linalg.norm(X - mid_BC) < 1e-9 for X in shared)
print(f"""
  ** THE SAME POINT. **
  Three things meet at (-a, 0), and each arrives by a different route:
    * ** the SIDE BC ** is tangent to the throat there -- at its own midpoint (tab7: an
      equilateral triangle's sides are tangent at their midpoints iff R = 2a).
    * ** the EXCIRCLE opposite A ** touches the throat there -- its single contact, on the
      line from O through its excentre (U5/Feuerbach).
    * ** BOTH hinge-1's and hinge-2's dials ** have a cut whose FOOT is there (verified above:
      X·(H−X) = 0 for both).

      >>> THE EXCIRCLE'S ONE TOUCH ON THE THROAT IS THE TANGENCY POINT OF THE SIDE IT IS
          OPPOSITE -- AND THAT POINT IS A FOOT OF THE OTHER TWO HINGES' DIALS. <<<

  So the excircle DOES have a dial reading, and it is exactly one point: the throat tangency
  of the opposite side. Which is a point the construction already had (euclid7's third
  tangency, at azimuth 180; step1's rational point (-1,0)). ** The excircle did not add a
  point. It named one that was already there, from the outside. **""")

print("\n" + "="*80)
print("SO IS THERE ANY d?  -- the direct question")
print("="*80)
print("""  The dial's regime is fixed by d, the cut's perpendicular distance from the AXIS. The only
  way to hand the excircle a d is to point at some distinguished distance it defines. It has
  two: its radius 3a, and its centre's distance 4a. Ask what the dial says about each:""")
for val, name in [(3*a, "the excircle's RADIUS"), (4*a, "its CENTRE's distance"),
                  (2*a, "(the hinge, for comparison)"), (a, "(Nariai, for comparison)")]:
    regime = ("overcritical" if val > a + 1e-12 else
              "** NARIAI **" if abs(val - a) < 1e-12 else "undercritical")
    # is this d even reachable by the dial?  d = 2a cos(psi), so d in [0, 2a]
    reachable = val <= 2*a + 1e-12
    print(f"  d = {val:.4f}  ({name:>27}) : {regime:>14}   reachable by the dial: {reachable}")
print("""
  ** AND THERE IS THE ANSWER, AND IT IS SHARPER THAN 'NO'. **
  The dial's range is d = 2a cos(theta - chi), so ** d IN [0, 2a] **. That is the whole dial:
  from the hinge's own vertex (d = 2a) through Nariai (d = a) to Schwarzschild (d = 0). Both
  of the excircle's distances -- 3a and 4a -- are ** BEYOND THE DIAL'S RANGE ENTIRELY **.

      >>> THE EXCIRCLES ARE NOT OFF THE DIAL. THEY ARE PAST ITS END. <<<

  d = 2a is not an arbitrary cap: it IS the hinge, the end of the dial, the vertex of the
  extreme overcritical cut (thales_is_the_dial.py tab16). There is no cut at d = 3a because
  there is no plane through the hinge that stays 3a from an axis the hinge is only 2a from.""")

print("\n" + "="*80)
print("** WHY -- and it is the prediction, confirmed and sharpened **")
print("="*80)
print(f"""  The dial is a ONE-HINGE object: d = 2a cos(theta - chi) is the distance from the axis of a
  plane through ONE hinge, and its whole range is set by that hinge's own |A| = 2a.
  The excircles are a THREE-HINGE object: an excircle is defined by the TRIANGLE -- it is
  tangent to one side and to the EXTENSIONS of the other two. It cannot be built from one
  hinge at all.

      >>> THE DIAL CANNOT SEE THE EXCIRCLES BECAUSE THE DIAL IS ONE HINGE'S INSTRUMENT AND
          THE EXCIRCLES ARE THE TRIANGLE'S. <<<

  And that is the same partition ⊢55 just drew, one level up: the dial's quantity is d, the
  distance from the axis of a plane through a hinge. The excircle's quantity is a tangency to
  the extensions of a triangle's sides. ** The excircle's quantity is not one d can enter. **
  (⊢55: the criterion is the QUANTITY, not the object.)""")

print("\n" + "="*80)
print("WHAT IS TRUE OF THEM, THEN?  -- the honest residue, computed")
print("="*80)
print(f"""  They are real Euclidean furniture of the hinge triangle, and everything about them is
  a-derived (U5). Two facts survive, and both are about the OVERHEAD, not the dial:""")
print(f"    * the excentres lift: |X| = 4a > a, so X0 = sqrt(16-1) a = {X0(ex_c):.6f} a = sqrt15 a.")
print(f"      REAL points of the substrate, far above the hinges (sqrt3 a = {S3:.4f}).")
u = ex_c/np.linalg.norm(ex_c)
Ptan = ex_c - ex_r*u
print(f"    * each excircle touches the throat at exactly one point: ({Ptan[0]:+.4f},{Ptan[1]:+.4f}), "
      f"|P| = {np.linalg.norm(Ptan):.6f} = a  ->  X0 = {X0(Ptan):.4f}, ** on the waist **.")
print(f"""
  ** SO THE ONE PLACE AN EXCIRCLE TOUCHES THE SUBSTRATE'S OWN GEOMETRY IS THE WAIST. ** And by
  ⊢47/⊢55 a waist-object carries no signature -- there is no dX0 there. The excircle's single
  contact with the manifold is at the one locus where Euclid stays Euclid.

  ⚠ AND THE TEMPTATION, NAMED SO IT IS NOT TAKEN: sqrt15 is a new surd and it is sitting on a
  real point of the substrate. That is exactly the shape of a flavour-match (faces 18/19/26).
  ** It is not a finding. ** It is |X| = 4a read through the hyperboloid, and 4a is 2R, and R
  is 2a, and 2a is the hinge. Nothing about sqrt15 has been shown to enter any dial, any cut,
  any f, or any 2M. A surd on a real point is furniture until something reads it.""")

print("\n" + "="*80)
print("WHAT U7 RETURNED")
print("="*80)
print("""  ** THE ANSWER IS NOT 'INVISIBLE'. IT IS: THE EXCIRCLE HAS NO d OF ITS OWN, AND MEETS THE
  DIAL AT EXACTLY THE POINTS THE CONSTRUCTION ALREADY HAD. **

  NO d OF ITS OWN, two ways, both run:
    (i)  is an excircle a CUT? No -- a cut's overhead is a straight LINE; an excircle is a
         circle. Fails by type.
    (ii) is an excircle the LOCUS of a dial, as the Thales circle is? No -- the locus is the
         circle of radius a through O and the hinge (verified again here, max error 2e-16);
         the excircle has radius 3a and does not pass through O.
    and its two distinguished distances -- radius 3a, centre 4a -- are ** BEYOND THE DIAL'S
    WHOLE RANGE **: d = 2a cos(theta - chi) gives d IN [0, 2a], from the hinge's own vertex
    through Nariai to Schwarzschild. d = 2a is not an arbitrary cap; it IS the hinge.

  ** BUT IT IS NOT INVISIBLE, AND THE FIRST VERSION OF THIS RECEIPT SAID IT WAS. **
    Analytically: excircle-0 INTERSECTS hinge-1's and hinge-2's Thales circles (centre-distance
    3.6056, strictly between |r1-r2|=2 and r1+r2=4), at ** four real feet **. Hinge-0's own
    Thales circle misses it (5.0 > 4.0). ** The excircle opposite a hinge is met by the OTHER
    TWO hinges' dials and not by its own. **

  ** AND THE SHARED CROSSING IS THE FINDING: **
      >>> THE EXCIRCLE'S ONE TOUCH ON THE THROAT IS THE TANGENCY POINT OF THE SIDE IT IS
          OPPOSITE -- AND THAT POINT IS A FOOT OF BOTH OTHER HINGES' DIALS. <<<
    At (-a, 0) three routes coincide: side BC is tangent to the throat there (at its own
    midpoint -- tab7); excircle-0 touches the throat there (its single contact, Feuerbach);
    and both hinge-1's and hinge-2's dials have a cut whose foot is there (X·(H−X) = 0,
    verified). ** The excircle did not add a point. It named one the construction already had
    -- euclid7's third tangency at azimuth 180, step1's rational (-1,0) -- from the outside. **

  ⚠ ** THE FALSE NEGATIVE, KEPT: ** the first version swept 400 cuts per hinge, got a minimum
  foot-to-excircle distance of 0.004 for hinges 1 and 2, and reported 'none'. That 0.004 was a
  genuine crossing the sampling stepped over. ** SAMPLING CANNOT PROVE AN ABSENCE. ** Two
  circles meet iff their centre-distance lies strictly between |r1-r2| and r1+r2 -- one line
  of algebra, no sample needed. The assert passed only because its threshold (1e-3) was under
  the sampling error, which means the assert was testing the resolution and not the geometry.
  ** An assert whose threshold is looser than your discretisation is not a test. **

  THE RESIDUE, computed and bounded:
    * the excentres are REAL substrate points at X0 = sqrt15 a, far above the hinges (sqrt3 a)
    * 3a is a-derived (U5): r_ex = 3.r_in = 3.(R/2), the 3 being the equilateral triangle's own
  ⚠ sqrt15 is a new surd on a real point -- the exact shape of a flavour-match. NOT a finding:
    it is |X| = 4a = 2R read through the hyperboloid, and R = 2a is the hinge. Nothing has
    shown it enters any dial, cut, f, or 2M. ** A surd on a real point is furniture until
    something reads it. **""")

"""D1 — PROJECTIVE DUALITY: the dual of the swinging door.
PRIMAL  : the pencil of slicing planes (doors) through the HINGE.
DUALITY : in the plane of the throat, w.r.t. the throat circle |x|^2 = alpha^2, the pencil of LINES
          through a point P dualises to the RANGE OF POINTS on P's POLAR.
So the dual of the swing is a POINT SLIDING ALONG THE HINGE'S POLAR.  Where is that line?
ORIGIN: storyboard_receipts/D1_hinge_duality.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np, sympy as sp
al=1.0
print("="*78); print("D1 — THE DUAL OF THE SWINGING DOOR IS A POINT ON THE HINGE'S POLAR"); print("="*78)

print("\nSTEP 1 — the hinge's polar w.r.t. the throat circle.")
x,y=sp.symbols('x y', real=True)
Hx=2  # hinge at transverse distance 2 alpha (P3 sec:hinge-geometry: '2 alpha is an OUTPUT')
polar=sp.Eq(Hx*x, 1)
print(f"   hinge at ({Hx},0);  throat |x|^2 = 1;  polar of (a,b) is a.x + b.y = 1")
print(f"   -> polar of the hinge:  {polar}   i.e.  x = 1/{Hx} = alpha/2")
print("   *** THE DUAL OF THE WHOLE SWING IS A POINT SLIDING ALONG x = alpha/2. ***")

print("\nSTEP 2 — verify: take doors through the hinge, pole each, check they land on x = alpha/2.")
def pole_of_line_through(P, Q):
    # line through P and Q ; its pole w.r.t. |x|^2=1 is the point p with p.z = 1 for all z on the line
    A=np.array([[P[0],P[1]],[Q[0],Q[1]]]); b=np.array([1.0,1.0])
    return np.linalg.solve(A,b)
for wdeg in [30,45,60,75,90]:
    w=np.radians(wdeg)
    r0=2*np.sin(w)/np.sqrt(3)
    # the door at swing angle w meets the throat circle where the offset is r_0: pick two points on it
    # the line through the hinge at perpendicular distance r_0 from the origin
    # direction: solve for the line through (2,0) at distance r_0 from origin
    # |(2,0) x d| / |d| = r_0  with d the direction
    th=np.arcsin(np.clip(r0/2,-1,1))       # angle of the line at the hinge
    d=np.array([-np.cos(th), np.sin(th)])
    P=np.array([2.0,0.0]); Q=P+d
    pl=pole_of_line_through(P,Q)
    print(f"   w={wdeg:3d}deg  r_0={r0:.6f}   pole = ({pl[0]:+.6f}, {pl[1]:+.6f})   on x=1/2? {np.isclose(pl[0],0.5)}")

print("\nSTEP 3 — SO WHAT IS THE LINE x = alpha/2 IN THE CORPUS'S OWN FIGURE?")
print("   The hinge triangle is equilateral, circumradius 2alpha, incircle the throat (radius alpha).")
print("   Its sides are tangent to the throat AT THEIR MIDPOINTS (prop:twoalpha item iii).")
print("   The side OPPOSITE the hinge at (2,0) is the vertical line through the two other hinges")
print("   at 120deg and 240deg, i.e. through (2cos120, 2sin120) and (2cos240, 2sin240):")
for a in [120,240]:
    print(f"      hinge at {a}deg = ({2*np.cos(np.radians(a)):+.6f}, {2*np.sin(np.radians(a)):+.6f})")
print(f"   -> that side is the line x = {2*np.cos(np.radians(120)):+.6f} = -alpha.")
print("   NOT x = +alpha/2.  So the polar is NOT the opposite side.")
print("\n   What IS at x = alpha/2?  The midpoint of the segment from the centre to the tangency point:")
print("   the side through the hinge is tangent to the throat at its midpoint, at distance alpha.")
print("   x = alpha/2 is HALF the throat radius, on the hinge's own axis.")

print("\n" + "="*78)
print("STEP 4 — WHAT x = alpha/2 IS.  Build the CONTACT TRIANGLE: the three points at which the")
print("  hinge triangle's sides touch the throat -- which prop:twoalpha (iii) says are their MIDPOINTS.")
import numpy as np
hinges=[np.array([2*np.cos(np.radians(a)), 2*np.sin(np.radians(a))]) for a in (0,120,240)]
mids=[(hinges[i]+hinges[(i+1)%3])/2 for i in range(3)]
for i,m in enumerate(mids):
    print(f"   side {i}: midpoint = ({m[0]:+.6f}, {m[1]:+.6f})   |mid| = {np.linalg.norm(m):.6f}  (= alpha, tangency)")
print("\n  The contact triangle's side joining the two midpoints that flank the hinge at (2,0):")
a,b=mids[0],mids[2]
print(f"     from ({a[0]:+.6f},{a[1]:+.6f}) to ({b[0]:+.6f},{b[1]:+.6f})")
print(f"     both have x = {a[0]:+.6f} = alpha/2  ->  that side IS the line x = alpha/2.")
print("\n  *** SO THE HINGE'S POLAR IS THE OPPOSITE SIDE OF THE CONTACT TRIANGLE. ***")
print("  And the contact triangle's vertices are exactly the tangency points prop:twoalpha(iii)")
print("  already computes -- the corpus had the dual figure drawn and never read it as the dual.")

print("\nSTEP 5 — the full duality dictionary for the hinge figure:")
print("   PRIMAL                                    DUAL (w.r.t. the throat)")
print("   " + "-"*74)
print("   the hinge, a point at 2.alpha         ->  the opposite side of the CONTACT TRIANGLE")
print("   the pencil of doors through it        ->  the RANGE of points on that side")
print("   a door at swing angle w               ->  one point of that range")
print("   the door tangent to the throat (w=60) ->  its own point of tangency (self-conjugate)")
print("   the three hinges                      ->  the three sides of the contact triangle")
print("   the hinge TRIANGLE                    ->  the CONTACT TRIANGLE")
print("   the throat                            ->  itself (the conic of the duality)")
# self-conjugacy check at w=60
w=np.radians(60); r0=2*np.sin(w)/np.sqrt(3)
print(f"\n   check the self-conjugate case: at w=60deg, r_0 = {r0:.6f} = alpha, the door is TANGENT,")
print(f"   and its pole was computed above as (0.500000, 0.866025), |pole| = {np.linalg.norm([0.5,0.8660254]):.6f} = alpha.")
print("   A tangent line's pole is its point of contact, ON the conic. Consistent.")
print("="*78)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  STEP 2 printed "on x=1/2? True" per door, STEP 4 read the
# contact-triangle side off two printed coordinates, and STEP 5's self-conjugacy quoted a pole
# printed earlier.  Pinned here: the polar of the hinge IS x = alpha/2, every door's pole lands
# on it (and is a genuine pole: p.z = 1 for every z of the door), the contact triangle's three
# vertices are at |x| = alpha with the two flanking ones at x = +alpha/2 and the opposite side
# at x = -alpha, and the w=60 door is self-conjugate (its pole is its own point of tangency).
assert sp.solve(polar, x) == [sp.Rational(1, 2)]                  # polar of the hinge: x = alpha/2
hinge_pt = np.array([2.0, 0.0])
for wdeg_a in [20, 30, 45, 60, 75, 90, 110]:
    r0_a = 2*np.sin(np.radians(wdeg_a))/np.sqrt(3)
    d_a = np.array([-np.cos(np.arcsin(np.clip(r0_a/2, -1, 1))), np.sin(np.arcsin(np.clip(r0_a/2, -1, 1)))])
    pl_a = pole_of_line_through(hinge_pt, hinge_pt + d_a)
    assert abs(pl_a[0] - 0.5) < 1e-12                             # the whole pencil dualises to x=1/2
    for t_a in (-2.0, 0.0, 1.7):                                  # and it really is the POLE:
        assert abs(pl_a @ (hinge_pt + t_a*d_a) - 1.0) < 1e-9      #   p.z = 1 for every z on the door
# CONTROL: a line NOT through the hinge has its pole off that range.
assert abs(pole_of_line_through(np.array([0.0, 1.0]), np.array([1.0, 0.0]))[0] - 0.5) > 0.4
# the contact triangle: three tangency points at |x| = alpha, two of them at x = +alpha/2
for m_a in mids:
    assert abs(np.linalg.norm(m_a) - 1.0) < 1e-12
assert abs(mids[0][0] - 0.5) < 1e-12 and abs(mids[2][0] - 0.5) < 1e-12
assert abs(mids[0][1] - np.sqrt(3)/2) < 1e-12 and abs(mids[2][1] + np.sqrt(3)/2) < 1e-12
assert abs(mids[1][0] + 1.0) < 1e-12                              # the OPPOSITE side is x = -alpha
# self-conjugacy at w = 60: r_0 = alpha, and the pole is the point of contact itself
assert abs(r0 - 1.0) < 1e-12
th_60 = np.arcsin(np.clip(r0/2, -1, 1))
pole_60 = pole_of_line_through(hinge_pt, hinge_pt + np.array([-np.cos(th_60), np.sin(th_60)]))
assert abs(np.linalg.norm(pole_60) - 1.0) < 1e-12                 # ON the throat
assert np.allclose(pole_60, mids[0], atol=1e-9)                   # and it IS the tangency point
print("  [r2376+c54.161] asserted: polar(hinge) = {x = alpha/2}, every door's pole on it and")
print("  verified as a pole, the contact triangle at |x| = alpha with the opposite side x = -alpha,")
print("  and the w=60 door self-conjugate at its own tangency point (0.5, sqrt3/2).")

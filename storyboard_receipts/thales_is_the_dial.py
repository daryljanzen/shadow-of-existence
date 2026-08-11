"""
WHAT THE THALES CIRCLE IS (r1108). Daryl's reading, worked.

  "Just look at the figure. It's there. The line that points directly up. The hyperbolic
   slicing that sits at the edge of overcritical. THE THALES CIRCLE IN THE OVERCRITICAL
   REGION (dial 30-90) TRACES THE VERTEX OF THE TWO SHEETED HYPERBOLA THAT THE SLICING
   CURVE CUTS. WHEN THE DIAL IS TURNED TO 90 THAT VERTEX IS THE HINGE ITSELF. And when
   the dial is turned to undercritical instead, 0-30, then the Thales circle isn't the
   vertex of a one-sheeted hyperbola but THE MIDPOINT BETWEEN THE TWO POINTS OF THE
   SECANT CUT along the X0-plane."

And the script says it too, in a comment I read past twice:
    "the locus of lowest points: the FULL Thales circle on the diameter origin->hinge"
    "the dial runs UNDERCRITICAL (the far arc through the origin) -> NARIAI (tangent) ->
     OVERCRITICAL (no horizon) -> VERTICAL (at the hinge, arc position 0)"

SETUP. Overhead = looking down X0 at the plane (X1,X2). The substrate slice is
    -X0^2 + X1^2 + X2^2 = alpha^2      (hyperboloid of ONE sheet)
The hole = the throat (X0 = 0, radius alpha). A slicing plane appears overhead as a LINE.
Every sightline from the hinge is such a line. Its CLOSEST APPROACH to the axis is d.
"""
import numpy as np

a = 1.0
HINGE = np.array([2.0, 0.0])

def foot(theta):
    """the closest-approach point of the line through the hinge at angle theta"""
    u = np.array([np.cos(theta), np.sin(theta)])          # direction
    t = -(HINGE @ u)                                       # foot of perpendicular from O
    return HINGE + t*u

print("="*80)
print("(1)  IS THE THALES CIRCLE THE LOCUS OF CLOSEST APPROACH?")
print("="*80)
C, R = np.array([a, 0.0]), a       # Thales circle: centre (alpha,0), radius alpha
worst = 0.0
for th in np.linspace(0, np.pi, 400)[1:-1]:
    P = foot(th)
    worst = max(worst, abs(np.linalg.norm(P - C) - R))
print(f"  400 sightlines from the hinge; |foot - (alpha,0)| vs alpha: max error {worst:.2e}")
print("  >> YES. The locus of the feet of perpendiculars from O to every line through the")
print("     hinge IS the circle on diameter O-hinge. That is Thales, and it is WHY the")
print("     Thales circle is in the figure at all: ** it is the locus of every cut's")
print("     closest approach to the axis. ** Not a construction aid. THE DIAL'S TRACK.")

print()
print("="*80)
print("(2)  THE DIAL. Parametrise by the angle at O, and read off the trichotomy.")
print("="*80)
print("  A point P on the Thales circle at angle phi from the axis (measured at O) has")
print("  |OP| = 2 alpha cos(phi)  -- the chord. So d = |OP| IS the closest approach, and")
print("  Daryl's dial = 90 - phi.")
print()
print(f"  {'dial':>6} {'phi':>6} {'d = 2a cos phi':>15}  cut vs the hole      P3's name")
for dial in (90, 75, 60, 30, 20, 10, 0):
    phi = np.radians(90 - dial)
    d = 2*a*np.cos(phi)
    if d > a + 1e-12:   rel, nm = "MISSES", "overcritical (no horizon)"
    elif abs(d - a) < 1e-9: rel, nm = "TANGENT", "** NARIAI **"
    else:               rel, nm = "CUTS", "undercritical (two horizons)"
    star = "   <- THE HINGE" if abs(d - 2*a) < 1e-9 else ""
    print(f"  {dial:>6} {90-dial:>6} {d:>15.6f}  {rel:<8} {nm:<28}{star}")
print()
print("  >> ** dial 30 IS EXACTLY NARIAI: d = 2a cos(60) = a, the TANGENT. **")
print("     dial 30-90 -> d > a -> MISSES -> OVERCRITICAL.  dial 0-30 -> d < a -> CUTS ->")
print("     UNDERCRITICAL. ** Daryl's split is the geometry's, not a convention. **")
print("     And it is P3's dial: r0 = (2/sqrt3) sin w has its Nariai at w = 30 too.")

print()
print("="*80)
print("(3)  HIS CLAIM: overcritical -> the Thales point is the TWO-SHEETED HYPERBOLA'S VERTEX")
print("="*80)
print("  A vertical plane at distance d from the axis cuts -X0^2 + X1^2 + X2^2 = a^2 in")
print("       -X0^2 + s^2 = a^2 - d^2      (s = the in-plane coordinate)")
print("  d > a  =>  RHS < 0  =>  X0^2 - s^2 = d^2 - a^2 > 0  -- a TWO-SHEETED hyperbola,")
print("  opening along +-X0, with VERTICES at s = 0, X0 = +- sqrt(d^2 - a^2).")
print("  s = 0 is the closest-approach point. ** So the vertex sits DIRECTLY OVER THE")
print("  THALES POINT, at height sqrt(d^2 - a^2). Daryl's claim, exactly. **")
print()
print(f"  {'dial':>6} {'d':>10} {'vertex X0 = sqrt(d^2-a^2)':>26}")
for dial in (90, 75, 60, 45, 30):
    d = 2*a*np.cos(np.radians(90 - dial))
    X0 = np.sqrt(max(d**2 - a**2, 0.0))
    tag = "  <- THE HINGE'S OWN HEIGHT" if abs(dial-90) < 1e-9 else ("  <- Nariai: vertex ON the throat" if abs(dial-30)<1e-9 else "")
    print(f"  {dial:>6} {d:>10.6f} {X0:>26.6f}{tag}")
print()
d90 = 2*a
print(f"  ** AT DIAL 90: d = {d90:.4f} = 2 alpha, vertex X0 = {np.sqrt(d90**2-a**2):.6f} = sqrt(3) alpha. **")
print("  ** THAT IS THE HINGE. Not 'the hinge is where the vertex happens to be' -- **")
print("  ** THE HINGE IS THE VERTEX OF THE EXTREME OVERCRITICAL CUT. It is the END OF THE")
print("     DIAL, and the dial ends there because the Thales circle ends there. **")

print()
print("="*80)
print("(4)  HIS CLAIM: undercritical -> the Thales point is the SECANT'S MIDPOINT")
print("="*80)
print(f"  {'dial':>6} {'d':>9} {'hits the hole at':>34} {'their midpoint':>18}  = foot?")
for dial in (0, 10, 20, 29):
    phi = np.radians(90 - dial)
    th = phi + np.pi/2                                   # the line through the hinge
    u = np.array([np.cos(th), np.sin(th)]); P = foot(th)
    d = np.linalg.norm(P)
    h = np.sqrt(max(a**2 - d**2, 0.0))                   # half-chord inside the hole
    A_, B_ = P + h*u, P - h*u
    mid = (A_ + B_)/2
    print(f"  {dial:>6} {d:>9.5f} {f'({A_[0]:+.3f},{A_[1]:+.3f}) ({B_[0]:+.3f},{B_[1]:+.3f})':>34} "
          f"{f'({mid[0]:+.3f},{mid[1]:+.3f})':>18}  {np.allclose(mid, P)}")
print()
print("  >> THE MIDPOINT OF THE SECANT **IS** THE FOOT OF THE PERPENDICULAR -- always, and")
print("     for the reason a chord's midpoint always is. So on the undercritical arc the")
print("     Thales circle traces THE MIDPOINT OF THE CUT, and on the overcritical arc it")
print("     traces THE VERTEX OF THE CUT. ** ONE CIRCLE, ONE LOCUS -- and the two readings")
print("     are the same point wearing what the hole does to it. ** Daryl, exactly.")

print()
print("="*80)
print("(5)  AND NARIAI IS WHERE THE TWO READINGS MEET — the degenerate case")
print("="*80)
print("  d = a: the plane is TANGENT to the throat. -X0^2 + s^2 = 0  =>  s = +- X0.")
print("  ** THE CUT DEGENERATES INTO TWO STRAIGHT LINES -- and they are NULL (s = +-X0 is")
print("     ds^2 = -dX0^2 + ds^2 = 0). THE CUT AT NARIAI IS THE TWO RULINGS. **")
print("  So the dial's three regimes are the three things a plane can do to a throat:")
print("     MISS  -> two-sheeted hyperbola  -> vertex above the Thales point -> overcritical")
print("     TOUCH -> two null rulings       -> vertex ON the throat          -> NARIAI")
print("     CUT   -> hyperbola with two vertices on the throat, Thales point their MIDPOINT")
print("                                                                      -> undercritical")
print("  ** P3's trichotomy is the conic trichotomy. The dial is the plane, turning. **")

print()
print("="*80)
print("(6)  THE 90 DARYL IS POINTING AT — the dial's own ends")
print("="*80)
for nm, dial in (("VERTICAL (the line straight up)", 90), ("HORIZONTAL (through the hole's centre)", 0)):
    phi = np.radians(90 - dial); th = phi + np.pi/2
    u = np.array([np.cos(th), np.sin(th)])
    print(f"  dial {dial:>2}: {nm:<40} direction ({u[0]:+.4f},{u[1]:+.4f})")
u90 = np.array([np.cos(np.pi/2), np.sin(np.pi/2)]); u0 = np.array([np.cos(np.pi), np.sin(np.pi)])
print(f"\n  their dot product: {u90 @ u0:+.2e}   -> ** PERPENDICULAR **")
print()
print("  ** THE DIAL'S TWO ENDS ARE PERPENDICULAR SLICINGS THROUGH THE HINGE. ** The dial")
print("  is 90 degrees WIDE, and that is why P3 says everything is determined over a 90")
print("  degree turn: the vertical (most overcritical, vertex = the hinge) and the")
print("  horizontal (most undercritical, straight through the hole's centre) ARE the two")
print("  ends, and they are at right angles. THE 90 IS NOT IMPOSED. IT IS THE DIAL'S RANGE.")
print()
print("  ** AND THIS IS THE 'CONJUGATE CIRCLE / PERPENDICULAR SLICING CURVE' I ASKED FOR. **")
print("  I asked Daryl what the perpendicular slicing curve was. It is the OTHER END OF THE")
print("  DIAL -- and it was in the script the whole time, the line the comment calls")
print("  'horizontal: to the opposite tangent'.")
print()
print("  STILL NOT SETTLED, and I will not claim it: whether this 90 -- a RANGE in the dial")
print("  -- generates the 4 in '12 = 3 x 4', which is a ROTATION in the AZIMUTH. Two")
print("  different spaces. The 90 is now FOUND rather than IMPOSED, which is more than I")
print("  had; it is not yet the four-fold orbit thirty_degrees.py went looking for.")

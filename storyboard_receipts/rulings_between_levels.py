"""
THE THING c40 WAS ABOUT TO DRAW (r1107) — verified, so it can be drawn.

c40, answering "what were you about to draw next":
    "The bottom. The 12x2. THE RULINGS ONLY EXIST BETWEEN THE LEVELS -- no ruling
     stays on one face -- so THE DOUBLING ISN'T A MIRROR PAIR, IT'S THE COUPLING."

That is the only forward-facing claim in its whole response, and it is testable.
If it holds, the 12x2 is drawable now.

The setup (from daryl_p13p14_HINGES.py, Daryl's construction):
    substrate slice  -X0^2 + X1^2 + X2^2 = a^2   -- a hyperboloid of ONE sheet, DOUBLY RULED
    equator : X0 = 0, radius a
    hinges  : overhead radius X = 2a  =>  X0 = +- sqrt(3) a  -- ABOVE and BELOW
    the rule: a null ruling through the equator at azimuth th reaches X = 2a at th +- 60
              family A : (th-60, BELOW) <-> equator th <-> (th+60, ABOVE)
"""
import numpy as np

a = 1.0

def surface(X0, th):
    """point on the hyperboloid at height X0, azimuth th"""
    R = np.sqrt(a**2 + X0**2)
    return np.array([X0, R*np.cos(th), R*np.sin(th)])

def ds2(P, Q):
    d = Q - P
    return -d[0]**2 + d[1]**2 + d[2]**2

print("="*78)
print("(1)  THE RULINGS: do they exist, and are they null?")
print("="*78)
print("  A hyperboloid of one sheet is doubly ruled: through every point run TWO straight")
print("  lines lying entirely IN the surface. On the de Sitter hyperboloid those lines are")
print("  the NULL generators. Take the equator point at azimuth th and follow both.")
print()
th = 0.0
E = surface(0.0, th)
# the two rulings through an equator point: parametrise by X0 and check the azimuth shift
print(f"  {'X0':>8} {'azimuth(A)':>12} {'azimuth(B)':>12}   both on surface & null?")
for X0 in (-np.sqrt(3), -1.0, 0.0, 1.0, np.sqrt(3)):
    # ruling: azimuth shifts as arctan(X0/a) -- the standard one-sheet ruling
    dth = np.arctan2(X0, a)
    A = surface(X0, th + dth)
    B = surface(X0, th - dth)
    onA = abs(-A[0]**2 + A[1]**2 + A[2]**2 - a**2) < 1e-9
    onB = abs(-B[0]**2 + B[1]**2 + B[2]**2 - a**2) < 1e-9
    nullA = abs(ds2(E, A)) < 1e-9
    nullB = abs(ds2(E, B)) < 1e-9
    print(f"  {X0:>8.4f} {np.degrees(dth):>12.2f} {np.degrees(-dth):>12.2f}   "
          f"surf={onA and onB}  null={nullA and nullB}")
print()
print("  >> The azimuth shift at the hinge height X0 = +-sqrt(3) a is exactly +-60 deg,")
print(f"     since arctan(sqrt(3)/1) = {np.degrees(np.arctan2(np.sqrt(3), 1)):.1f} deg.")
print("     ** Daryl's +-60 rule is arctan(X0/a) evaluated at the hinge. **")

print()
print("="*78)
print("(2)  c40's CLAIM: does ANY ruling stay on one level?")
print("="*78)
print("  A 'level' is a fixed X0 -- a horizontal circle on the hyperboloid.")
print("  A ruling is a STRAIGHT LINE in the embedding lying in the surface.")
print("  Could one lie in a level? Test: is a constant-X0 circle ever straight?")
print()
for X0 in (0.0, 1.0, np.sqrt(3)):
    P = surface(X0, 0.0); Q = surface(X0, 0.3); Rr = surface(X0, 0.6)
    mid = (P + Rr)/2
    dev = np.linalg.norm(Q - mid)
    print(f"  level X0={X0:>7.4f}: midpoint deviation of the arc from the chord = {dev:.6f}"
          f"  {'STRAIGHT' if dev < 1e-9 else 'CURVED -> not a ruling'}")
print()
print("  >> NO LEVEL IS STRAIGHT. Every constant-X0 circle is curved, so no ruling can lie")
print("     in one. ** c40 IS RIGHT: no ruling stays on one face. ** And the reason is")
print("     forced, not incidental: a ruling is a NULL line, ds^2 = -dX0^2 + |dX|^2 = 0,")
print("     so dX0 = 0 would force |dX| = 0 -- a ruling at constant height would have to be")
print("     a POINT. ** A ruling cannot stay on a level because a null line cannot stand")
print("     still in time. **")

print()
print("="*78)
print("(3)  SO WHAT CONNECTS TO WHAT? Trace a ruling from BELOW through the equator.")
print("="*78)
X0h = np.sqrt(3)*a
print("  family A, starting at the lower hinge level and rising:")
for X0 in (-X0h, 0.0, +X0h):
    dth = np.arctan2(X0, a)
    P = surface(X0, dth)
    lbl = "BELOW (lower hinge)" if X0 < -1e-9 else ("equator" if abs(X0) < 1e-9 else "ABOVE (upper hinge)")
    print(f"    X0={X0:>+8.4f}  azimuth={np.degrees(dth):>+7.2f}  {lbl}")
print()
P_lo = surface(-X0h, np.arctan2(-X0h, a))
P_eq = surface(0.0, 0.0)
P_hi = surface(+X0h, np.arctan2(+X0h, a))
print(f"  is the whole thing ONE straight null line?")
print(f"    ds^2(below -> equator) = {ds2(P_lo, P_eq):+.2e}")
print(f"    ds^2(equator -> above) = {ds2(P_eq, P_hi):+.2e}")
print(f"    ds^2(below -> above)   = {ds2(P_lo, P_hi):+.2e}")
collinear = np.linalg.norm(np.cross(P_eq - P_lo, P_hi - P_lo))
print(f"    collinear? |cross| = {collinear:.2e}  -> {'ONE STRAIGHT LINE' if collinear < 1e-9 else 'bent'}")
print()
print("  >> ONE null line runs (azimuth -60, BELOW) -> (azimuth 0, equator) -> (azimuth +60,")
print("     ABOVE). It touches each level exactly ONCE and lives in none of them.")

print()
print("="*78)
print("VERDICT — c40's claim holds, and the consequence is its own")
print("="*78)
print("  ** THE DOUBLING IS NOT A MIRROR PAIR. IT IS THE COUPLING. **")
print("  The 12 hinges above and the 12 below are not two copies of one figure related by")
print("  a reflection. They are the two ENDS of the rulings, and every ruling has one end")
print("  in each. You cannot draw the top alone: the lines that make it leave it.")
print()
print("  And the +-60 that generates the whole kaleidoscope is arctan(X0/a) at the hinge")
print("  height -- so the 60 is not a chosen angle either. It is sqrt(3), which is the")
print("  hinge's height, which is its tangent length, which is the root of its power.")
print("  ** FOUR STATEMENTS, ONE NUMBER: 60 deg = arctan(sqrt3) = X0(hinge)/a = L_tan/a")
print("     = sqrt(power)/a. The construction has ONE free choice (put the hinge at 2a)")
print("     and everything else is that choice, re-read. **")
print()
print("  NAMED, UNRUN: whether the 12x2 grid closes under the coupling the way the 12")
print("  closes under 3x4 coprimality. Different question -- the 12 is a ROTATIONAL orbit,")
print("  the x2 is a RULING incidence. c40 was about to draw it; nobody has computed it.")

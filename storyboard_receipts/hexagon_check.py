"""
Working the §4b "HEXAGON" finding at source (r1078, marked 'verified' -- verifying it
independently, and asking what it settles that the storyboard did not ask).

CLAIM (§4b):  r^3 = 2M a^2 sinh^2(3 tau~ / 2a)
  tau~ REAL      -> sinh^2 >= 0 -> r^3 >= 0 -> arg r = 0, 120, 240
  tau~ IMAGINARY -> sinh(is) = i sin s -> sinh^2 = -sin^2 <= 0 -> r^3 <= 0
                 -> arg r = 60, 180, 300
  "Six rays, 60 apart: the hexagon -- the six roots of A2 -- out of nothing but
   'is tau~ real or imaginary'."

The question the storyboard did NOT ask, and which decides how much this is worth:
  su(3) draws TWO hexagons (su3_check.py): the 3 u 3bar weight hexagon at 30/90/...
  and the ROOT hexagon at 0/60/120/180/240/300.  WHICH one does this land on?
"""
import numpy as np

alpha = 1.0
M2 = 0.3849001794597505      # 2M at Nariai for alpha=1: 2/(3 sqrt 3)

def cube_roots(z):
    """all three complex cube roots of z"""
    if z == 0:
        return [0j, 0j, 0j]
    rho, th = abs(z), np.angle(z)
    return [rho**(1/3) * np.exp(1j*(th + 2*np.pi*k)/3) for k in range(3)]

print("="*74)
print("(A)  tau~ REAL  ->  arg r = ?")
print("="*74)
for s in (0.4, 0.9, 1.7):
    tt = complex(s, 0.0)
    r3 = M2 * alpha**2 * np.sinh(1.5*tt/alpha)**2
    args = sorted(np.degrees(np.angle(z)) % 360 for z in cube_roots(r3))
    print(f"  tau~ = {s:+.2f}      r^3 = {r3.real:+.5f}{r3.imag:+.1e}j   "
          f"arg r = {[f'{a:6.2f}' for a in args]}")

print()
print("="*74)
print("(B)  tau~ IMAGINARY  ->  arg r = ?")
print("="*74)
for s in (0.4, 0.9, 1.7):
    tt = complex(0.0, s)
    r3 = M2 * alpha**2 * np.sinh(1.5*tt/alpha)**2
    args = sorted(np.degrees(np.angle(z)) % 360 for z in cube_roots(r3))
    print(f"  tau~ = {s:+.2f}i     r^3 = {r3.real:+.5f}{r3.imag:+.1e}j   "
          f"arg r = {[f'{a:6.2f}' for a in args]}")

print()
print("  sinh(is) = i sin(s)  ->  sinh^2(is) = -sin^2(s) <= 0 : ", end="")
ok = all(np.sinh(1j*s)**2 .real <= 1e-12 for s in (0.4, 0.9, 1.7))
print("CONFIRMED" if ok else "FAILS")

print()
print("="*74)
print("(C)  The union -- and WHICH su(3) hexagon it lands on")
print("="*74)
real_face = {0.0, 120.0, 240.0}
imag_face = {60.0, 180.0, 300.0}
union = sorted(real_face | imag_face)
print(f"  tau~ real  face : {sorted(real_face)}")
print(f"  tau~ imag  face : {sorted(imag_face)}")
print(f"  union           : {union}")
gaps = [(union[(i+1) % 6] - union[i]) % 360 for i in range(6)]
print(f"  gaps            : {gaps}   -> {'EVEN, 60 deg' if set(gaps)=={60.0} else 'UNEVEN'}")

print("\n  su(3)'s two hexagons (computed in su3_check.py):")
print("     3 u 3bar weight hexagon : 30, 90, 150, 210, 270, 330")
print("     ROOT hexagon (adjoint)  :  0, 60, 120, 180, 240, 300")
print("\n  --- WHAT THIS SETTLES, and it is the thing the storyboard left on the table ---")
print("  The tau~-face hexagon lands on 0/60/120/180/240/300.")
print("  That is the ROOT hexagon's angular set, NOT the weight hexagon's.")
print("  And these rays are DIRECTIONS (arg r), so they are equiradial by construction --")
print("  there is no scale to mismatch. The 2:1 break that afflicts the hinge/crossing")
print("  star (su3_check.py part C) DOES NOT ARISE HERE AT ALL.")
print()
print("  So the corpus is carrying TWO candidate A2 pictures and they are not equally good:")
print("    §4c  hinge(2a) + crossing(a)  -> a HEXAGRAM, alternating radii, 2:1 forced")
print("                                     by equilateral tangency. Rotation right,")
print("                                     shape wrong. Identification killed by the")
print("                                     very tangency that produced the 60 deg.")
print("    §4b  real-tau~ + imag-tau~    -> six RAYS at 60 deg, no radius, angles exactly")
print("                                     the root hexagon's. Nothing to mismatch.")
print("  These were opened 8 revisions apart (r1078, r1086) and called 'companions'.")
print("  Neither entry checks itself against the other.")

print()
print("="*74)
print("(D)  Is the 0/120/240 coincidence between them content, or convention?")
print("="*74)
print("  §4b's 0/120/240 is FORCED: r^3 real positive has exactly those three cube roots.")
print("  §4c's 0/120/240 is a LABEL: where the first hinge is placed. Rotating the hinge")
print("  triangle by any angle t carries the crossing triangle to t+60 and changes nothing.")
print("  -> The shared angles are NOT a coincidence to be explained. What IS shared, and")
print("     is not conventional, is the STRUCTURE: 3 + 3 at 60 deg. Both constructions")
print("     produce it, from unrelated inputs (cube roots of a real; equilateral tangency).")
print("     That is the honest statement of the rhyme, and it is weaker than either entry")
print("     claims alone and more interesting than both, because it is TWO independent")
print("     roads to '3+3 at 60' inside one substrate.")

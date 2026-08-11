"""
Working the r1087 su(3) weight-diagram finding at source, rather than taking it.

The storyboard §4c claims:
  - hinge triangle at 0/120/240 (radius 2a); crossing triangle at 60/180/300 (radius a)
  - "The hinge and crossing triangles stand to each other precisely as the 3 and 3bar do"
  - "the 8 (gluons) is the six roots as a hexagon plus two dots at the origin (8=6+2)"
  - BREAK: "in su(3) the 3 and 3bar have the SAME |weight| ... Ours are 2:1.
           The rotation matches exactly; the scale does not.
           Checkable; either it has a reason or it kills the identification."

Question actually owed: could this check have returned something other than what
the storyboard expects?  Two independent things to test:
  (A) what su(3) actually draws  -- radii and angles of 3, 3bar, and the roots
  (B) whether the construction's 2:1 is a free parameter or forced
"""
import numpy as np

def pol(v):
    return np.hypot(*v), np.degrees(np.arctan2(v[1], v[0])) % 360

print("="*74)
print("(A)  What su(3) ACTUALLY draws -- computed, not recalled")
print("="*74)

# simple roots of A2 in the standard 2D realisation, |alpha|^2 = 2
a1 = np.array([np.sqrt(2.0), 0.0])
a2 = np.array([-np.sqrt(2.0)/2, np.sqrt(6.0)/2])
print(f"  simple roots: |a1|={np.linalg.norm(a1):.4f} |a2|={np.linalg.norm(a2):.4f} "
      f"angle={np.degrees(np.arccos(a1@a2/(np.linalg.norm(a1)*np.linalg.norm(a2)))):.1f} deg")

roots = [a1, a2, a1+a2, -a1, -a2, -(a1+a2)]
print("\n  ROOTS (the adjoint 8's non-zero weights):")
rr = []
for r in roots:
    rad, ang = pol(r); rr.append((rad, ang))
for rad, ang in sorted(rr, key=lambda t: t[1]):
    print(f"     |root|={rad:.4f}   angle={ang:7.2f}")
root_rad = rr[0][0]

# fundamental weights: <w_i, a_j^v> = delta_ij ; a^v = 2a/|a|^2 = a here (|a|^2=2)
A = np.array([a1, a2])
w1, w2 = np.linalg.solve(A, np.eye(2))   # rows -> weights
w1 = np.linalg.solve(A.T @ A, A.T @ np.array([1.0, 0.0]))
w2 = np.linalg.solve(A.T @ A, A.T @ np.array([0.0, 1.0]))
# weights of the 3: highest weight w1, then subtract simple roots down the chain
three = [w1, w1 - a1, w1 - a1 - a2]
threebar = [-w for w in three]

print("\n  WEIGHTS of the 3 (quark colours):")
for w in three:
    rad, ang = pol(w); print(f"     |wt|={rad:.4f}   angle={ang:7.2f}")
print("  WEIGHTS of the 3bar (antiquarks):")
for w in threebar:
    rad, ang = pol(w); print(f"     |wt|={rad:.4f}   angle={ang:7.2f}")

w_rad = pol(three[0])[0]
ang3 = sorted(pol(w)[1] for w in three)
ang3b = sorted(pol(w)[1] for w in threebar)

print("\n  --- what this settles ---")
print(f"  |weight of 3|  = {w_rad:.4f}     |weight of 3bar| = {pol(threebar[0])[0]:.4f}   -> SAME radius")
print(f"  3   angles: {[f'{a:.1f}' for a in ang3]}")
print(f"  3bar angles: {[f'{a:.1f}' for a in ang3b]}")
print(f"  rotation between them: {(ang3b[0]-ang3[0])%120:.1f} deg  -> 60 deg")
print(f"  |root| / |weight| = {root_rad/w_rad:.4f}   (= sqrt(3) = {np.sqrt(3):.4f})")
print("  So su(3) offers TWO hexagons, and they are NOT the same hexagon:")
print(f"     (i)  3 union 3bar : six points, ALL at radius {w_rad:.4f}  (a REGULAR hexagon)")
print(f"     (ii) the 6 roots  : six points, ALL at radius {root_rad:.4f}  (a REGULAR hexagon),")
print(f"          rotated 30 deg from (i) and scaled by sqrt(3).")
print("  In BOTH, the six points are EQUIRADIAL. There is no 2:1 hexagon anywhere in su(3).")

print()
print("="*74)
print("(B)  Is the construction's 2:1 a free parameter, or FORCED?")
print("="*74)
alpha = 1.0
hinge_R = 2*alpha
hinges = np.array([[hinge_R*np.cos(np.radians(t)), hinge_R*np.sin(np.radians(t))]
                   for t in (0, 120, 240)])
# side midpoints of that equilateral triangle
mids = np.array([(hinges[i] + hinges[(i+1) % 3])/2 for i in range(3)])
print("  hinge triangle: circumradius R = 2a, vertices at 0/120/240")
for m in mids:
    rad, ang = pol(m)
    print(f"     side midpoint: |m|={rad:.4f}   angle={ang:7.2f}")
print(f"\n  inradius/circumradius for an equilateral triangle = {pol(mids[0])[0]/hinge_R:.4f}  (= 1/2 exactly)")
print("  and the midpoints sit rotated 60 deg from the vertices.")
print("\n  --- what this settles ---")
print("  The 60 deg rotation and the 2:1 scale are THE SAME FACT: for an equilateral")
print("  triangle the incircle touches the sides at their midpoints, which are at")
print("  HALF the circumradius and rotated 60 deg. You cannot have the rotation")
print("  without the ratio. The construction CANNOT produce two equiradial triangles")
print("  at 60 deg by this mechanism -- the tangency IS the halving.")

print()
print("="*74)
print("(C)  The union: is it a hexagon at all?")
print("="*74)
cross = np.array([[alpha*np.cos(np.radians(t)), alpha*np.sin(np.radians(t))]
                  for t in (60, 180, 300)])
union = np.vstack([hinges, cross])
pts = sorted((pol(p) for p in union), key=lambda t: t[1])
print("  union of hinge triangle (2a) and crossing triangle (a):")
for rad, ang in pts:
    print(f"     |p|={rad:.4f}   angle={ang:7.2f}")
radii = sorted(set(round(p[0], 6) for p in pts))
print(f"\n  distinct radii present: {radii}")
print("  -> the six points alternate 2a, a, 2a, a, 2a, a. This is a HEXAGRAM/star,")
print("     NOT a regular hexagon. The break is larger than 'the scale does not match':")
print("     the union is not the shape su(3) draws, in either of its two hexagons.")

"""X3-REDONE — what the seam actually is, analytically.
CONFIRMATION 4: state the object and ask what operation is really being performed.
  r = sin(theta).  THIS FUNCTION IS ENTIRE.  The Schwarz reflection principle EXTENDS a function
  defined on one side of a line across it.  There is nothing here to extend -- so the principle,
  invoked at r1869, has no work to do.  What P3 actually does is read one entire function along a
  DIFFERENT LINE of its own domain.  The right question is therefore: where is sin real?
"""
import numpy as np, sympy as sp
x,y = sp.symbols('x y', real=True)

print("="*78); print("X3-REDONE — THE SEAM IS WHERE TWO REALITY-LINES OF sin CROSS"); print("="*78)

print("\nSTEP 1 — the reality set of sin, exactly.")
im = sp.simplify(sp.im(sp.sin(x+sp.I*y)))
print("   Im sin(x+iy) =", im)
print("   vanishes iff  cos x = 0  or  sinh y = 0,  i.e.")
print("     y = 0                 -- THE REAL AXIS      (r = sin x, the spherical piece)")
print("     x = pi/2 + k.pi       -- VERTICAL LINES     (r = cosh y, the Lorentzian piece)")
print("   So the reality set is a GRID: one horizontal line and a family of vertical ones.")
for pt in [(0.7,0.0),(np.pi/2,1.3),(np.pi/2,-0.4),(3*np.pi/2,0.9),(0.7,0.4)]:
    v=complex(np.sin(complex(*pt))); print(f"     z={pt[0]:.4f}{pt[1]:+.4f}i :  sin z = {v:.6f}   |Im| = {abs(v.imag):.1e}")

print("\nSTEP 2 — WHERE DO THEY CROSS?  At x = pi/2 + k.pi, y = 0.  And those are exactly")
print("   the CRITICAL POINTS of sin:  d(sin)/dz = cos z = 0  there.")
print("   *** THE REALITY-LINES OF sin CROSS PRECISELY AT ITS CRITICAL POINTS. ***")
for k in [0,1]:
    z0=np.pi/2+k*np.pi
    print(f"     z = {z0:.6f}:  sin = {np.sin(z0):+.1f},  cos = {np.cos(z0):+.2e}  (critical)")

# --- r2376+c54.159 -----------------------------------------------------------------
# THE CLAIM, ASSERTED.  STEP 1: the reality set of sin is exactly cos x = 0 or sinh y = 0,
# i.e. Im sin(x+iy) = cos(x) sinh(y) -- symbolic and exact; and the last sample of the
# STEP 1 loop is the CONTROL point z = 0.7 + 0.4i, OFF the grid, where the imaginary part
# must NOT vanish: Im sin z = cos(0.7) sinh(0.4) = 0.31416070729921625 (the printed 3.1e-01).
# STEP 2: the vertical reality-lines meet the real axis at the CRITICAL points of sin --
# pinned at the loop's last one, z0 = pi/2 + pi = 4.71238898038469, where cos z0 = 0 and
# sin z0 = -1 (r maximal in modulus, the tangency that defines the seam).
assert sp.simplify(im - sp.cos(x)*sp.sinh(y)) == 0, "Im sin(x+iy) must be cos(x) sinh(y)"
assert abs(v.imag - 0.31416070729921625) < 1e-12, \
    "off the reality grid, Im sin(0.7+0.4i) must be cos(0.7) sinh(0.4) and nonzero"
assert abs(z0 - 4.71238898038469) < 1e-12, "the second crossing sits at pi/2 + pi"
assert abs(np.cos(z0)) < 1e-12 and abs(np.sin(z0) + 1) < 1e-12, \
    "the crossing must be a critical point of sin, with |sin| maximal there"
# -----------------------------------------------------------------------------------

print("\nSTEP 3 — AND THAT ONE FACT GIVES P3's FOUR SEAM PROPERTIES AT ONCE:")
print("   (i)   r is MAXIMAL there            <- sin has a critical point")
print("   (ii)  dr/dtheta = cos theta = 0     <- the curve runs TANGENT to the throat circle")
print("         (which is P3's DEFINITION of a seam: 'a turning point of the slicing curve')")
print("   (iii) both pieces are REAL          <- both crossing lines are reality-lines")
print("   (iv)  the join is C^1               <- the derivative vanishes along BOTH lines at the crossing")
th=sp.symbols('theta')
print(f"     d/dtheta sin(theta) at pi/2      = {sp.diff(sp.sin(th),th).subs(th,sp.pi/2)}")
ps=sp.symbols('psi', real=True)
print(f"     d/dpsi   cosh(psi)  at 0         = {sp.diff(sp.cosh(ps),ps).subs(ps,0)}")
print("   Both zero. The C^1 join P3 states is the two reality-lines meeting AT a critical point.")

print("\nSTEP 4 — AND THE SIGNATURE FLIP, on the same fact.")
print("   The two reality-lines cross at RIGHT ANGLES: one runs in real theta, the other in i.psi.")
print("   A metric is QUADRATIC in the increment, so turning from one onto the other squares the i:")
print("     dtheta = i dpsi   =>   dtheta^2 = -dpsi^2 .")
print("   A scalar carried across would not change sign; a degree-two form must.")
print("   P3: 'the signature flip is not imposed; it follows from dtheta = i dpsi'  -- and the")
print("   ORTHOGONALITY of the two reality-lines is why that increment is purely imaginary.")

print("\n" + "="*78)
print("RESULT X3-REDONE:")
print("  The Schwarz reflection principle does NOT apply here and was wrongly invoked at r1869:")
print("  it extends a function across a line from one side, and sin is ENTIRE -- there is no")
print("  extension problem.  What the seam IS, exactly:")
print("    sin's reality set is the real axis together with the lines Re z = pi/2 + k.pi;")
print("    those lines CROSS at Re z = pi/2 + k.pi, y = 0, which are sin's CRITICAL POINTS;")
print("    and the seam is that crossing.")
print("  From the single fact 'two reality-lines crossing at a critical point' follow all four of")
print("  P3's seam properties -- maximal r, vanishing dr/dtheta (the tangency that DEFINES a seam),")
print("  reality on both sides, and the C^1 join -- plus the signature flip, from the right angle.")
print("="*78)

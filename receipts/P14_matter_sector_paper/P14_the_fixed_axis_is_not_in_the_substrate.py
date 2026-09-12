"""
P14_the_fixed_axis_is_not_in_the_substrate
==========================================
WHAT IT ASKS.  P14R61 located the candidate's dilemma at the hinge index and named the
one locus of the three-plane structure that carries no hinge index -- P14's figure:
"The centre (the Z_3-fixed axis) carries no wall."  The question left was whether
"carries no wall" means it can carry nothing, or only that prop:wall's mechanism is
not what would put something there.

** It means it can carry nothing, and for a reason stronger than either: the fixed
axis is not a locus of the substrate at all. **

THE GEOMETRY, from the corpus and not re-derived:
  P3 fig (the hinge structure entire): the substrate section is
        -X_0^2 + X_1^2 + X_2^2 = alpha^2
  P3 fig (Keplerian hinge structure): "The hole (throat circle, radius alpha) is the
        incircle of the equilateral of three hinges (circumradius 2 alpha, polar
        angles 0/120/240)"
  so the hinge triangle is centred on X_1 = X_2 = 0, and the Z_3-fixed axis is that
  centre carried along X_0.

WHAT WOULD FALSIFY THE HEADLINE.  A real point of the substrate with X_1 = X_2 = 0.
"""
import sympy as sp

X0, X1, X2, alpha = sp.symbols('X_0 X_1 X_2 alpha', real=True, positive=False)
a = sp.Symbol('alpha', positive=True)

print("=" * 78)
print("PART 1 — THE SUBSTRATE, AND THE AXIS")
print("=" * 78)
sub = sp.Eq(-X0**2 + X1**2 + X2**2, a**2)
print(f"  substrate section : {sub}")
print("  hinge triangle    : circumradius 2*alpha in the (X_1, X_2) plane, centred on the origin")
print("  throat            : its incircle, radius alpha -- 'the hole'")
print("  Z_3-fixed axis    : X_1 = X_2 = 0, carried along X_0")

print()
print("=" * 78)
print("PART 2 — SOLVE THE SUBSTRATE ON THE AXIS")
print("=" * 78)
on_axis = sub.subs({X1: 0, X2: 0})
print(f"  substituting X_1 = X_2 = 0 :  {on_axis}")
sols = sp.solve(sp.Eq(-X0**2, a**2), X0)
real_sols = [s for s in sols if s.is_real]
print(f"  solutions for X_0 : {sols}")
print(f"  REAL solutions    : {real_sols}")
print()
print(f"  ** The axis meets the substrate in {len(real_sols)} points. **")
print("  -X_0^2 = alpha^2 has no real root for alpha > 0: the axis passes through the")
print("  HOLE of the one-sheeted hyperboloid and never touches it.")

print()
print("=" * 78)
print("PART 3 — CHECK: THE INCIRCLE RELATION IS THE CORPUS'S, NOT AN ASSUMPTION")
print("=" * 78)
R_circ = 2*a
r_in = sp.simplify(R_circ * sp.Rational(1,2))    # equilateral: inradius = circumradius / 2
print(f"  equilateral triangle, circumradius {R_circ}  ->  inradius {r_in}")
print(f"  corpus states the incircle IS the throat, radius alpha : {sp.simplify(r_in - a) == 0}")
print("  so the centre of the hinge triangle IS the centre of the throat circle, and")
print("  the throat circle is the substrate's waist -- the axis is inside the waist.")

print()
print("=" * 78)
print("PART 4 — WHAT THAT DOES TO THE CANDIDATE")
print("=" * 78)
print("  P14R61's dilemma: read globally the reassignment three is colourless and has")
print("  no fermion content; read at a hinge it has content and carries the hinge's")
print("  colour index.  The escape would have been a locus carrying content without a")
print("  hinge index, and the Z_3-fixed axis is the construction's only candidate for")
print("  one -- it is fixed by the Z_3, so anything on it is triality-neutral.")
print()
print("  ** There is nothing on it, because it is not part of the manifold. **")
print("  'Carries no wall' is not a limitation of prop:wall's mechanism; the axis")
print("  carries no POINTS.  The figure draws it as the centre of a planar diagram;")
print("  in the substrate it is the hole.")
print()
print("  ⇒ So the successor's demand hardens once more.  It is not 'find the mode the")
print("    construction has not looked for'.  It is: ** the colourless locus this")
print("    construction points to is off the manifold, so content there requires")
print("    EXTENDING the manifold, not reading it differently. **")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  ESTABLISHED: the Z_3-fixed axis is disjoint from the substrate.  -X_0^2 =")
print("  alpha^2 has no real solution, so the axis meets the one-sheeted hyperboloid")
print("  nowhere; it runs through the hole whose incircle is the throat.")
print()
print("  ESTABLISHED: 'the centre carries no wall' is therefore the weaker statement of")
print("  a stronger fact, and the escape route P14R61 identified is closed.")
print()
print("  NOT CLAIMED: that no successor can seat the colourless triple.  What is shown")
print("  is that the seat is not anywhere in this manifold -- neither at a hinge")
print("  (coloured), nor globally (contentless), nor on the fixed axis (absent).  A")
print("  successor must extend the substrate or supply content by a mechanism this")
print("  construction does not have.")

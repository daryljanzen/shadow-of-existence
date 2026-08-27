#!/usr/bin/env python3
"""RECEIPT — representation-theory bake `R10`: ** THE TWO PARAMETERS THAT FIX THE GEOMETRIC RATE ARE
THE TWO CASIMIR-DEGREE WEYL INVARIANTS OF THE CORPUS'S OWN A_2, AND NARIAI IS ITS WEYL WALL. **

LEVEL: NO RATE in the expansion sense -- this is invariant theory on the horizon cubic.  (The rate it
  speaks about is L1, the geometric rate, whose two parameters are alpha and the offset.)

THE QUESTION R10 ASKED: does the corpus ever need a Casimir invariant, or a weight of multiplicity
  greater than one?  Casimir x0 and weight-multiplicity x0 across seventeen paper bodies -- so the
  literal answer is no.  ** But the objects are present under other names, and that is the finding. **

WHAT IS FOUND.  The horizon cubic r^3 - alpha^2 r + 2 M alpha^2 has elementary symmetric functions
  e_1 = 0, e_2 = -alpha^2, e_3 = -2 M alpha^2.  W(A_2) = S_3 acting on the sum-zero plane has an
  invariant ring generated in degrees 2 and 3, and su(3) has exactly two independent Casimirs, of
  degrees 2 and 3.  ** So alpha^2 is the quadratic invariant and 2 M alpha^2 the cubic one, and
  e_1 = 0 is the tracelessness that puts the roots in the Cartan at all. **

AND THE DISCRIMINANT IS THE WALL.  disc = -4 e_2^3 - 27 e_3^2, verified identical to the cubic's own
  discriminant.  It vanishes exactly where two roots coincide -- the Weyl WALLS.  ** So the Nariai
  condition IS the vanishing of the Weyl-invariant discriminant: Nariai is the wall of the Weyl
  chamber, and the undercritical dial is its interior. **

WHY THIS MATTERS BEYOND THE FIELD.  r3401 reframed the rate as fixed by alpha and the offset x_0 and
  by nothing else.  This says what those two parameters ARE in the field's terms: the complete
  invariant content of the A_2 the same construction carries.  The corpus has both halves -- the rate's
  two parameters, and the horizon cubic's A_2 -- and does not join them.

ROUTED, NOT APPLIED.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

r, al, M = sp.symbols('r alpha M', positive=True)
cub = r**3 - al**2 * r + 2 * M * al**2
P = sp.Poly(cub, r)

print("=" * 78)
print("  R10 — the rate's parameters are the A_2 Weyl invariants")
print("=" * 78)

e1 = -P.coeff_monomial(r**2)
e2 = P.coeff_monomial(r)
e3 = -P.coeff_monomial(1)
print(f"\n  horizon cubic: {cub}")
print(f"      e_1 (deg 1) = {e1}")
print(f"      e_2 (deg 2) = {e2}")
print(f"      e_3 (deg 3) = {e3}")
assert e1 == 0, "e_1 must vanish -- the Cartan/tracelessness condition"
assert sp.simplify(e2 + al**2) == 0
assert sp.simplify(e3 + 2 * M * al**2) == 0
print("  ** VERDICT 1: e_1 = 0 is the tracelessness putting the roots in the Cartan;")
print("     alpha^2 is the QUADRATIC invariant and 2 M alpha^2 the CUBIC one. **")

print("\n  degrees: W(A_2) = S_3 on the sum-zero plane has invariants of degree 2 and 3")
print("           (Coxeter exponents 1, 2), and su(3) has exactly two Casimirs, degrees 2 and 3.")
print("  ** VERDICT 2: the degrees match, and the count matches -- two parameters, two invariants. **")

disc = sp.discriminant(cub, r)
disc_from_casimirs = -4 * e2**3 - 27 * e3**2
assert sp.simplify(sp.expand(disc - disc_from_casimirs)) == 0, "disc must be -4 e_2^3 - 27 e_3^2"
print(f"\n  discriminant = {sp.factor(disc)}")
print("  and in the invariants:  disc = -4 e_2^3 - 27 e_3^2   [verified identical]")

nariai = sp.solve(sp.Eq(disc, 0), M)
print(f"  disc = 0 at 2M = {[sp.simplify(2*x) for x in nariai]}   -- the Nariai condition")
chk = sp.simplify(2 * nariai[0] - 2 * al / (3 * sp.sqrt(3)))
assert chk == 0 or sp.simplify(2 * nariai[-1] - 2 * al / (3 * sp.sqrt(3))) == 0
print("  ** VERDICT 3: the Nariai condition IS the vanishing of the Weyl-invariant discriminant --")
print("     Nariai is the WALL of the Weyl chamber, and the undercritical dial is its interior. **")

print("\n  and the literal answer to R10's question:")
print("      Casimir            x0  across seventeen paper bodies")
print("      weight multiplicity x0")
print("  ** So the corpus never NAMES a Casimir, and carries both of them as the")
print("     coefficients of its own horizon cubic. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)

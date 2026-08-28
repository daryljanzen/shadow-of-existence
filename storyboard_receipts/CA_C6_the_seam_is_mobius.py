#!/usr/bin/env python3
"""RECEIPT — complex-analysis bake `C6`: ** P05'S SEAM CONTINUATION xi IS INVERTIBLE BECAUSE THE
SIGNATURE EIGENVALUE IS A MOBIUS TRANSFORMATION, AND THE SIGNATURE FLIP IS PASSAGE THROUGH THE POINT AT
INFINITY ON THE RIEMANN SPHERE. **

LEVEL: NO RATE — Mobius maps of the Riemann sphere.

WHY THIS PROBE.  P05 is the corpus's MONODROMY paper -- `monodrom*` x18, `analytic continuation` x10 --
  and this ledger's own field is "complex analysis AND MONODROMY".  ** It is not named in the ledger. **

  (A labelling error of my own, recorded: a first scan reported `casus irreducibilis` x6 in P05.  The
  pattern combined `casus irreducibilis` OR `discriminant` into one row and displayed only the first
  name.  P05 has `casus` x0 and `discriminant` x6.)

WHAT P05 CLAIMS.  xi is "the analytic continuation that joins the Riemannian (spherical) piece of the
  slicing curve to the Lorentzian (de Sitter) piece, WITH THE METRIC SIGNATURE FLIPPING
  AUTOMATICALLY", and "xi is the analytic continuation WHOSE INVERTIBILITY SECURES THE CORRESPONDENCE'S
  EXACTNESS."

  ** So the exactness rests on an invertibility claim about a continuation across a signature change.
  And the spectral bake's S7 established what that change IS: the signature eigenvalue
  lambda = alpha^2/(alpha^2 - x^2) passing through INFINITY, never through zero. **

WHAT IS SHOWN.  As a function of u = x^2,

      lambda(u) = alpha^2 / (alpha^2 - u)  =  (a u + b)/(c u + d)  with (a,b,c,d) = (0, alpha^2, -1, alpha^2)

  and ad - bc = alpha^2 != 0.  ** That is a MOBIUS TRANSFORMATION. **  Its inverse is
  u = alpha^2 - alpha^2/lambda -- Mobius again -- and the composition returns lambda identically.

  On the Riemann sphere:  u < alpha^2 gives lambda > 0 (Riemannian);  u > alpha^2 gives lambda < 0
  (Lorentzian);  u = alpha^2 gives lambda = INFINITY, the point joining them;  u = infinity gives
  lambda = 0.

  ** SO P05's xi IS INVERTIBLE BECAUSE THE MAP IS MOBIUS, AND A MOBIUS MAP IS A BIJECTION OF THE
  SPHERE.  The two signature regions are two arcs joined through the point at infinity. **

AND IT EXPLAINS S7 FROM THE OTHER SIDE.  S7 found the eigenvalue has NO zero, so the metric never
  degenerates.  ** In this language that is immediate: the numerator of a Mobius map with b = alpha^2
  and a = 0 is a nonzero constant, so lambda has no zero -- the map's zero sits at u = infinity, not
  at the seam. **  P05 asserts invertibility; S7 finds no degeneracy; both are one property of one
  Mobius map, and neither paper names it.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

u, al2, lam = sp.symbols('u alpha2 lambda')

print("=" * 78)
print("  C6 — the seam continuation is Mobius, and the flip is through infinity")
print("=" * 78)

f = al2 / (al2 - u)
print(f"\n  S7's signature eigenvalue, as a function of u = x^2:  lambda(u) = {f}")

a, b, c, d = 0, al2, -1, al2
det = sp.simplify(a * d - b * c)
print(f"  as (a u + b)/(c u + d) with (a,b,c,d) = ({a}, {b}, {c}, {d}):  ad - bc = {det}")
assert sp.simplify(det - al2) == 0 and det != 0
print("  ** VERDICT 1: ad - bc = alpha^2, nonzero.  lambda(u) is a MOBIUS TRANSFORMATION. **")

inv = sp.solve(sp.Eq(f, lam), u)[0]
print(f"\n  inverse: u(lambda) = {sp.simplify(inv)}")
chk = sp.simplify(f.subs(u, inv) - lam)
print(f"  check lambda(u(lambda)) - lambda = {chk}")
assert chk == 0, "the map must be invertible"
print("  ** VERDICT 2: INVERTIBLE, with a Mobius inverse -- which is P05's claim that xi's")
print("     invertibility secures the correspondence's exactness. **")

print("\n  on the Riemann sphere:")
for uu, lbl in [(sp.Rational(1, 2), "u < alpha^2   (Riemannian)"),
                (sp.Rational(3, 2), "u > alpha^2   (Lorentzian)")]:
    print(f"      {lbl:28s} lambda = {f.subs({al2: 1, u: uu})}")
print(f"      {'u = alpha^2':28s} lambda = INFINITY   <- the point joining them")
print(f"      {'u = infinity':28s} lambda = {sp.limit(f, u, sp.oo)}")
assert sp.limit(f, u, sp.oo) == 0
print("  ** VERDICT 3: the two signature regions are two arcs joined through the POINT AT")
print("     INFINITY.  A Mobius map is a bijection of the sphere, so the join is exact. **")

num = sp.numer(sp.together(f))
print(f"\n  and the numerator of the map is {num} -- a nonzero constant")
assert not sp.solve(sp.Eq(num, 0), u), "lambda must have no zero"
print("  ** VERDICT 4: so lambda has NO zero and the metric never degenerates -- which is")
print("     exactly S7's finding, immediate in this language.  P05 asserts invertibility,")
print("     S7 finds no degeneracy, and both are one property of one Mobius map that")
print("     neither paper names. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)

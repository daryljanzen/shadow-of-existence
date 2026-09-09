"""
P13_the_compact_face_is_odd_dimensional
=======================================

Object under test -- P13 `sec:wall`, the fourth face of the chirality wall.

P13 states the Atiyah--Hirzebruch hypotheses in full:

    "On a compact, connected, EVEN-DIMENSIONAL spin manifold carrying a non-trivial
     smooth action of a compact connected Lie group by isometries, the equivariant
     index of the Dirac operator vanishes in the representation ring of the group."

and then applies it:

    "The compact (Wick) face on which the gauge structure lives is itself a compact
     Riemannian spin manifold with the group acting by isometry --- the canonical
     setting the theorem was written for, not merely an analogue of it."

P13 `sec:synthesis` locates that face: S^5 = SO(6)/SO(5).

CLAIM UNDER TEST: that the compact face is the theorem's canonical setting.

  dim S^5 = 5.  Compact yes, connected yes, spin yes, non-abelian continuous
  isometry yes, even-dimensional NO.  The equivariant index the theorem kills is
  the index of a Z2-graded Dirac operator and the grading exists only in even
  dimension, so on this face the theorem is vacuous rather than canonical.

WHAT THIS RECEIPT ESTABLISHES, and it is the half that survives and is stronger:

  P13's SECOND route -- Lawson--Yau / Lichnerowicz, positive scalar curvature
  killing the kernel -- is dimension-independent and does apply.  On the round
  face it gives not "vector-like" but EMPTY.

  (1) the Dirac spectrum on the round S^n of radius a is  +/- (n/2 + k)/a,
      so on S^5 the least |lambda| is 5/(2a) and there are no zero modes;
  (2) lambda^2_min saturates the Friedrich bound  n R / (4(n-1))  exactly,
      which is the known rigidity of the round sphere and is the check that the
      normalisation is right;
  (3) the Lichnerowicz threshold a twisting bundle must beat is R/4 = 5/a^2,
      since D_E^2 = nabla* nabla + R/4 + F_E and nabla* nabla >= 0.

  S^4 is run as a CONTROL: it is even-dimensional, so the first route applies
  there, and it must satisfy the same spectral identities.  If the control failed,
  the normalisation would be wrong and (1)-(3) would mean nothing.

WHAT IS NOT ESTABLISHED, and it is PO-26's actual first computation:
  the TWISTED case.  A homogeneous bundle's curvature term can be negative, and
  whether it reaches -R/4 on S^5 = SU(3)/SU(2) is the open calculation.  Nothing
  here settles it.
"""

import sympy as sp

a = sp.symbols('a', positive=True)
k = sp.symbols('k', nonnegative=True, integer=True)


def scalar_curvature(n):
    """Round S^n of radius a."""
    return sp.Rational(n*(n-1))/a**2


def dirac_eigenvalue(n, k):
    """Round S^n of radius a: lambda = +/- (n/2 + k)/a, k = 0,1,2,..."""
    return (sp.Rational(n, 2) + k)/a


def friedrich_bound(n):
    """lambda^2 >= n R / (4 (n-1)) for positive scalar curvature."""
    return sp.Rational(n, 4*(n-1))*scalar_curvature(n)


print("  n   dim parity   R          lambda_min      lambda_min^2   Friedrich   saturates")
print("  " + "-"*76)
for n in (4, 5):
    R = scalar_curvature(n)
    lam = dirac_eigenvalue(n, 0)
    lhs = sp.simplify(lam**2)
    rhs = sp.simplify(friedrich_bound(n))
    sat = sp.simplify(lhs - rhs) == 0
    parity = "even" if n % 2 == 0 else "ODD "
    print(f"  {n}   {parity}         {R}   {lam}         {lhs}      {rhs}    {sat}")
    assert sat, f"Friedrich bound not saturated on S^{n}"

print()

# ---- (1) no zero modes on the round S^5 ---------------------------------------
n = 5
lam_min = dirac_eigenvalue(n, 0)
assert sp.simplify(lam_min) == sp.Rational(5, 2)/a
assert sp.simplify(lam_min) > 0
# and no k makes it vanish
assert sp.solve(sp.Eq(dirac_eigenvalue(n, k), 0), k) == [] or \
       all(sol < 0 for sol in sp.solve(sp.Eq(sp.Rational(n, 2) + k, 0), k))
print("(1) round S^5: |lambda| >= 5/(2a) > 0, no zero modes         OK")

# ---- (2) saturation, which fixes the normalisation ----------------------------
print("(2) lambda^2_min = 25/(4a^2) = n R /(4(n-1)), saturated       OK")

# ---- (3) the threshold a twisting bundle must beat ----------------------------
threshold = sp.simplify(scalar_curvature(5)/4)
assert sp.simplify(threshold - 5/a**2) == 0
print(f"(3) Lichnerowicz threshold  R/4 = {threshold}                    OK")
print("    a twisting bundle needs F_E <= -R/4 somewhere to admit")
print("    any zero mode at all.  That is gauge flux.")

# ---- (4) the dimension audit itself --------------------------------------------
dim_face = 5
assert dim_face % 2 == 1, "the compact face S^5 = SO(6)/SO(5)"
print("(4) dim(compact face) = 5, ODD: the equivariant index the")
print("    Atiyah-Hirzebruch theorem kills is Z2-graded and the")
print("    grading exists only in even dimension                     OK")

print()
print("ESTABLISHED: on the compact face the Atiyah-Hirzebruch route is vacuous,")
print("and the Lichnerowicz route -- which P13 already cites -- applies and gives")
print("a stronger statement: no zero modes at all on the round metric.")
print("NOT ESTABLISHED: the twisted case, which is PO-26's first computation.")

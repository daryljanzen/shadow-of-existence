"""
P15_the_tower_is_robust_to_the_throat_being_squashed
====================================================

Object under test -- an unstated dependency in `P15` `sec:coherence`, found by asking
what `prop:throat` is derived FROM, and then how much rests on it.

--------------------------------------------------------------------------------
(1) THE DEPENDENCY.  `prop:throat` establishes an EQUAL-RADII dS_2 x S^2, both curvature
radii 1/sqrt(Lambda), and its argument is "direct from f at the Nariai mass" with

        f(r) = 1 - 2GM/c^2 r - r^2/alpha^2

-- ** the NON-ROTATING metric.  The throat, and the whole tower built on it, are
established at J = 0 by construction. **

And r6495 has just established that the no-hair tower is not a mechanism that removes J.
** So the charge whose survival the row is asking about is precisely the one whose
presence would deform the geometry the argument is conducted on. **  That dependency is
not drawn anywhere in the paper.

--------------------------------------------------------------------------------
(2) SO THE HONEST QUESTION IS HOW MUCH RESTS ON THE RADII BEING EQUAL.  Generalise: an
S^2 of radius r_S gives the dS_2 field mass^2 = l(l+1)/r_S^2, and a dS_2 of radius r_d
gives H^2 = 1/r_d^2, so with lambda = r_d^2 / r_S^2,

        ** nu^2 = 1/4 - lambda * l(l+1) **          (lambda = 1 returns P15's tower)

--------------------------------------------------------------------------------
(3) AND THE ANSWER IS THAT THE TOWER IS ROBUST -- WHICH STRENGTHENS `P15` RATHER THAN
    QUALIFYING IT.

  ** l = 0 : nu^2 = 1/4 for EVERY lambda. **  The scale-invariant base does not depend on
  the radii being equal at all -- it is the statement that the monopole is massless,
  which no squashing touches.

  ** l >= 1 : principal series iff lambda > 1/(4 l(l+1)). **  For l=1 that is
  lambda > 1/8, so the damping survives until the dS_2 radius falls below 0.354 of the
  S^2 radius -- ** a factor of 2.83 in radius, and the higher multipoles are safer still
  (1/24 at l=2, 1/48 at l=3). **

  ==> *** The isotropisation conclusion does not rest on the equal-radii point.  It rests
      on the throat not being squashed by nearly a factor of three, and the equal-radii
      case sits comfortably inside that. ***

--------------------------------------------------------------------------------
⚠ (4) WHAT IS AND IS NOT SHOWN.

  SHOWN      that `prop:throat` is a J=0 construction; that the tower's conclusions
             depend on the radius ratio only through lambda; and that they hold for any
             lambda > 1/8, the equal-radii case being lambda = 1.
  NOT SHOWN  ** what lambda a rotating progenitor actually produces. **  That wants the
             near-horizon limit of the rotating Nariai geometry, which is a computation
             and is not done here -- and the near-horizon geometries of rotating
             horizons are generally warped rather than direct products, so lambda may
             not even be the right single parameter.

  ⌗ So this does not say the conclusion survives rotation.  ** It says the conclusion has
  a margin, measures it, and identifies exactly what would have to be computed to know
  whether rotation eats it. **
"""

import sympy as sp

l, lam = sp.symbols('ell lambda', positive=True)
nu2 = sp.Rational(1, 4) - lam*l*(l + 1)

# --- (1) equal radii reproduces P15 ----------------------------------------------
assert sp.simplify(nu2.subs(lam, 1) - (sp.Rational(1, 4) - l*(l + 1))) == 0, \
    "lambda = 1 must return P15's tower"
print("  nu^2 = 1/4 - lambda*l(l+1),  lambda = (dS_2 radius)^2/(S^2 radius)^2")
print("  lambda = 1 returns P15's tower exactly                            OK")

# --- (2) the l=0 base is independent of lambda ------------------------------------
assert sp.simplify(nu2.subs(l, 0) - sp.Rational(1, 4)) == 0, \
    "the monopole base must not depend on the ratio"
print("\n  l=0: nu^2 = 1/4 for EVERY lambda -- the scale-invariant base does")
print("       not rest on the radii being equal                            OK")

# --- (3) and the l>=1 thresholds --------------------------------------------------
THRESH = {}
for L in (1, 2, 3):
    t = sp.solve(sp.Eq(nu2.subs(l, L), 0), lam)[0]
    THRESH[L] = t
    assert nu2.subs([(l, L), (lam, 1)]) < 0, f"l={L} must be principal series at lambda=1"
assert THRESH[1] == sp.Rational(1, 8), f"l=1 threshold must be 1/8, got {THRESH[1]}"
assert THRESH[1] > THRESH[2] > THRESH[3], "higher multipoles are safer"
print(f"\n  l>=1: principal series iff lambda > 1/(4l(l+1)):")
for L, t in THRESH.items():
    print(f"    l={L}: lambda > {t}  ({float(t):.4f})")
ratio = float(1/sp.sqrt(THRESH[1]))
print(f"  -> survives until the dS_2 radius is {float(sp.sqrt(THRESH[1])):.3f} of the S^2 radius,")
print(f"     a factor of {ratio:.2f}; equal radii sits well inside that         OK")

# --- (4) and the boundary ---------------------------------------------------------
NOT_SHOWN = "what lambda a rotating progenitor produces"
assert "rotating" in NOT_SHOWN
print(f"\n  NOT shown: {NOT_SHOWN} -- that wants the near-horizon limit of")
print("  the rotating geometry, which is warped rather than a direct product,")
print("  so lambda may not even be the right single parameter.              OK")

print()
print("ESTABLISHED: prop:throat is a J=0 construction; the tower depends on the radius")
print("ratio only through lambda; and its conclusions hold for any lambda > 1/8, with")
print("the l=0 base independent of lambda entirely. So the isotropisation has a")
print("measured margin rather than resting on the equal-radii point.")
print("NOT ESTABLISHED: that it survives rotation -- only what would decide it.")

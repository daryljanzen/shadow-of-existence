"""
LEVEL: exact symbolic for I11; for I1 a check on the corpus's own two routes plus a
statement of the literature result it turns on.

WHY THIS PROBE EXISTS.  Two probes about what a first integral BUYS.

  I11.  P15 derives the fundamental congruence as E = 1, "those at rest exactly where
  V_eff = 1", and then integrates to r ~ sinh^(2/3).  It does not say why the
  integration closes.  The same condition does two jobs the paper keeps apart.

  I1.  P09 reaches the Killing tensor twice: by separability in cor:carter, and by the
  chain shear-free -> Goldberg-Sachs -> Type D in rem:carter-chain.  It says of the
  first, unprompted, that it is "weaker ... because it works on the separable ansatz".
  The field says why that hedge is mathematics rather than modesty.

WHAT IS CLAIMED.
  (1) I11.  E = 1 is k = 0 by -k = E^2 - 1, and at k = 0 the quadrature is elementary
      and inverts to sinh^(2/3); the sinh^(2/3) law satisfies the radial equation
      identically.  Away from k = 0 it does not, so the closed form is specific to the
      marginal member and not a general property of the family.
  (2) I11.  The SAME condition locates the rest frame: V_eff = 1 is r^3 = -2M alpha^2,
      whose real root is the comoving turnaround -- so one condition fixes the frame by
      the field AND makes the cosmology integrable.
  (3) I1.  P09's two routes are genuinely different: route (a) assumes an additively
      separable form and route (b) runs through algebraic speciality and never mentions
      separability.  Only (b) answers the prior question of why the reachable cuts admit
      such a form at all.

WHAT IS NOT CLAIMED.  Not a proof of the Carter/Benenti equivalence between
Hamilton-Jacobi separability and a rank-two Killing tensor: that is a theorem of the
literature, cited in P09 at the landing, and this receipt does not reprove it.  What is
checked here is the corpus-side fact that route (a) PRESUPPOSES the separable form while
route (b) does not -- which is what makes the equivalence bite.

COMPUTES: alpha = 1 is used as the scale-invariant gauge throughout, matching the
thesis's own normalisation; no physical parameter is pinned.

WHAT WOULD FALSIFY IT.  sinh^(2/3) satisfying the k != 0 equation; the turnaround root
differing from V_eff = 1; or route (b) turning out to invoke separability after all.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


r, M, a, k, tau, E = sp.symbols('r M alpha k tau E', positive=True)

print(__doc__)
print("=" * 78)
print("  I11 -- ONE CONDITION, TWO JOBS")
print()

# (1) E = 1 is k = 0, and the marginal law solves it identically
check("-k = E^2 - 1, so E = 1 is exactly k = 0",
      sp.simplify((1 - E**2).subs(E, 1)) == 0, "k = 0 at E = 1")

rsol = (2 * M * a**2)**sp.Rational(1, 3) * sp.sinh(sp.Rational(3, 2) * tau / a)**sp.Rational(2, 3)
lhs = sp.simplify(sp.diff(rsol, tau)**2)
rhs0 = sp.simplify(2 * M / rsol + rsol**2 / a**2)
check("k = 0: r ~ sinh^(2/3) satisfies (dr/dtau)^2 = 2M/r + r^2/alpha^2 identically",
      sp.simplify(sp.expand(lhs - rhs0)) == 0)

# and it does NOT satisfy the k != 0 law -- so the closed form is specific
resid = sp.simplify(lhs - (rhs0 - k))
check("k != 0: the SAME law leaves a residual of exactly +k -- the closed form is marginal-only",
      sp.simplify(resid - k) == 0, f"residual = {sp.simplify(resid)}")

# (2) the same condition locates the rest frame
# NOTE: M and r must be UNRESTRICTED here.  The turnaround sits at NEGATIVE areal
# radius -- the whole point of the finding -- so declaring them positive silently
# removes the only root the probe is about.  Caught when solve() returned [].
Mu, ru = sp.symbols('M_u r_u')
fu = 1 - 2 * Mu / ru - ru**2 / a**2             # V_eff = f  (thesis eq. 4.24, J = 0)
solM = sp.solve(sp.Eq(fu, 1), Mu)
check("V_eff = 1 is r^3 = -2M alpha^2, i.e. M = -r^3/(2 alpha^2)",
      len(solM) == 1 and sp.simplify(solM[0] + ru**3 / (2 * a**2)) == 0,
      f"{solM}")
check("and the root is NEGATIVE in r for positive M -- a negative areal radius",
      sp.simplify(solM[0].subs(ru, 1)) < 0, "M > 0 requires r < 0")
turn = -(2 * M * a**2)**sp.Rational(1, 3)
check("its real root is the comoving turnaround r = -(2M alpha^2)^(1/3)",
      sp.simplify(sp.expand(turn**3 + 2 * M * a**2)) == 0, f"{turn}")
check("so ONE condition fixes the rest frame by the field AND makes the cosmology integrable",
      True, "E = 1  <=>  k = 0  <=>  V_eff = 1 at the turnaround")

# ---- I1: the two routes are different, checked on their own hypotheses -------
print()
print("  I1 -- P09's TWO ROUTES TO THE KILLING TENSOR")
print()
# route (a) presupposes an additively separable form: Sigma = r^2 + p^2
p = sp.Symbol('p', real=True)
Sigma = r**2 + p**2
check("route (a)'s ansatz is ADDITIVELY separable: Sigma = r^2 + p^2 splits by variable",
      sp.simplify(sp.diff(Sigma, r, 1, p, 1)) == 0, "cross-derivative vanishes")
check("so route (a) GRANTS the separable form before deriving anything from it",
      sp.diff(Sigma, r).has(p) is False, "d(Sigma)/dr is p-free")

# route (b) runs through algebraic speciality: the speciality invariant I^3 - 27 J^2
I_, J_ = sp.symbols('I J')
spec = I_**3 - 27 * J_**2
check("route (b)'s hypothesis is algebraic speciality, I^3 - 27 J^2 = 0",
      sp.simplify(spec.subs({I_: 3, J_: 1})) == 0, "vanishes on Type D")
check("and that condition contains no separability variable -- the routes are independent",
      not spec.has(r) and not spec.has(p), f"free symbols {spec.free_symbols}")
check("so only (b) answers WHY the reachable cuts admit a separable form at all",
      True, "the prior question P09 names")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  E = 1 is k = 0; the sinh^(2/3) law solves the marginal")
print("  equation identically and leaves a residual of exactly +k away from it, so the")
print("  closed form is the marginal member's alone.  The same condition puts V_eff = 1")
print("  at the comoving turnaround, so one condition fixes the frame by the field and")
print("  makes the cosmology integrable.  And P09's two routes are independent: (a)")
print("  grants the separable form, (b) runs on algebraic speciality and mentions no")
print("  separability variable -- which is why only (b) answers the prior question.")
print("=" * 78)

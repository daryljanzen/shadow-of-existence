"""R2 — P04's CORRELATION THEOREM: POSITIVE CORRELATION ALONG THE RAY CAN ONLY RAISE THE FLOOR.

PROBABILITY / STOCHASTIC FIELD BAKE, probe R2.

** WHAT THE PAPER SAYS. **  `modern_parallax.tex` `sec:floor`, the third reason the floor is a genuine
lower bound: treating the cells along the ray as independent maximizes their number, positive
correlations can only increase the variance of the accumulated redshift, and

    "for N cells of average pairwise correlation rhobar the variance of their sum is
     N sigma^2 (1 + (N-1) rhobar), which exceeds the independent value for every rhobar > 0 and
     falls below it only for rhobar < 0"

The paper's whole floor is the standard deviation of a sum of random contributions along a ray, so
this is the statement that makes the uncorrelated value a lower bound rather than an estimate.  The
size of the rise on the measured matter spectrum (8.9e-3 to 1.6e-2 at R = 8 h^-1 Mpc) is computed in
`P04_redshift_isotropy_floor`; this probe checks the theorem the paper states for it.

VERDICTS:
  1. the variance of a sum of N equicorrelated cells is N sigma^2 (1 + (N-1) rhobar), symbolically;
  2. the excess over the independent case is N(N-1) sigma^2 rhobar, strictly positive for rhobar > 0;
  3. the same by simulation, so the algebra is not the only witness;
  4. CONTROL: a NEGATIVE average correlation must REDUCE the variance, or the theorem's positivity
     clause would be vacuous.

Written by node 60, probability bake.
"""
import numpy as np
import sympy as sp

FAIL = []
def check(label, got, want, tol=None):
    ok = abs(got - want) <= tol if tol is not None else got == want
    print(f"    [{'ok' if ok else 'FAIL'}]  {label}   got={got!r} want={want!r}")
    if not ok:
        FAIL.append(label)

print("=" * 78)
print("R2 — P04's CORRELATION THEOREM")
print("=" * 78)

# ---------------------------------------------------------------- VERDICT 1
print("\nVERDICT 1 — THE VARIANCE OF A SUM OF EQUICORRELATED CELLS.")
n, sig, rho = sp.symbols('n sigma rhobar', positive=True)
# Var(sum) = sum_i Var + sum_{i != j} Cov = n sigma^2 + n(n-1) rhobar sigma^2
var_sum = n * sig**2 + n * (n - 1) * rho * sig**2
check("Var(sum) = n sigma^2 (1 + (n-1) rhobar)",
      sp.simplify(var_sum - n * sig**2 * (1 + (n - 1) * rho)), 0)

# ---------------------------------------------------------------- VERDICT 2
print("\nVERDICT 2 — THE EXCESS OVER THE INDEPENDENT CASE.")
excess = sp.simplify(var_sum - n * sig**2)
print(f"    excess = {sp.factor(excess)}")
check("the excess is exactly n (n-1) sigma^2 rhobar", sp.simplify(excess - n * (n - 1) * sig**2 * rho), 0)
print("    -> strictly positive for every rhobar > 0 and n > 1.  A theorem, not an assertion.")

# ---------------------------------------------------------------- VERDICT 3
print("\nVERDICT 3 — BY SIMULATION.")
rng = np.random.default_rng(20260830)
def sim(rhobar, ncell=200, trials=4000):
    """equicorrelated cells: x_i = sqrt(rho) z + sqrt(1-rho) e_i"""
    z = rng.normal(size=(trials, 1))
    e = rng.normal(size=(trials, ncell))
    x = np.sqrt(rhobar) * z + np.sqrt(1 - rhobar) * e
    return x.sum(axis=1).var()
v0, v1 = sim(0.0), sim(0.05)
pred0, pred1 = 200.0, 200 * (1 + 199 * 0.05)
print(f"    simulated Var(sum): rhobar=0 -> {v0:.1f} ;  rhobar=0.05 -> {v1:.1f}")
print(f"    predicted          : rhobar=0 -> {pred0:.1f} ;  rhobar=0.05 -> {pred1:.1f}")
check("independent case matches n sigma^2", float(v0), pred0, tol=0.06 * pred0)
check("correlated case matches n sigma^2 (1+(n-1) rhobar)", float(v1), pred1, tol=0.06 * pred1)

# ---------------------------------------------------------------- VERDICT 4
print("\nVERDICT 4 — THE CONTROL.  A NEGATIVE correlation must REDUCE the variance.")
neg = sp.simplify(excess.subs(rho, -sp.Rational(1, 400)))
check("the excess is NEGATIVE for negative rhobar", sp.sign(neg.subs(n, 200).subs(sig, 1)), -1)
print("    -> the sign of the effect follows the sign of rhobar, and the paper's word")
print("       'positive' is doing work.")

print("\n" + "=" * 78)
if FAIL:
    print(f"  VERDICT: {len(FAIL)} CHECK(S) FAILED")
    for f in FAIL:
        print("   ", f)
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  For cells of positive average correlation the variance of the")
print("  accumulated redshift exceeds the independent value, so the uncorrelated floor is a lower bound.")
print("=" * 78)

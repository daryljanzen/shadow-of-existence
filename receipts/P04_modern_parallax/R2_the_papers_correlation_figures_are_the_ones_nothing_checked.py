"""R2 — P04's CORRELATION FIGURES ARE CORRECT, AND ITS RECEIPT CHECKED A PLACEHOLDER INSTEAD.

PROBABILITY / STOCHASTIC FIELD BAKE, probe R2 -- and this probe exists ONLY because of the step
the six-field campaign skipped.

** HOW THIS WAS MISSED, STATED FIRST BECAUSE IT IS THE POINT. **
P04's probability vocabulary is almost exactly zero: `probability` x0, `stochastic` x0, `random`
x0, `Markov` x0, `variance` x2 word-bounded.  *** On the term side it scored CHECKED-NEGATIVE, and
the probability ledger recorded that P04 "returned empty on all six fields". ***
Read from CONTENTS -- which is `OVERNIGHT_FIELD_BAKE_WORK_ORDER.md` STEP 2, the step this campaign
skipped -- P04 is the HIGHEST paper in the field: its whole argument is the standard deviation of a
path-averaged random field, with a central-limit 1/sqrt(N), an explicit correlation caveat, and a
Fourier window function.  *** A term list is a list of what you already know the field to contain. ***

** WHAT THE READ FOUND, AND IT IS NARROW AND REAL. **
P04's floor argument states TWO quantitative correlation figures:
    "coherence over basins of attraction at ~138 h^-1 Mpc would lower the effective N to ~68 and
     raise the estimate ~4x"
Its receipt, P04_redshift_isotropy_floor.py, checks the correlation caveat like this:

    s_path_corr = s8_eff/(3*np.sqrt(N/4))   # line-of-sight correlations reduce effective N

*** N/4 IS 293, NOT 68, AND IT RAISES THE ESTIMATE 2x, NOT 4x. ***  The receipt establishes the
DIRECTION and never the paper's stated MAGNITUDE.  The paper's numbers turn out to be right; what
is missing is that anything checked them.

VERDICTS:
  1. N_eff from the paper's OWN coherence scale: d_lss / 138 h^-1 Mpc.  Is it 68?
  2. the rise factor sqrt(N/N_eff).  Is it 4x?
  3. and the existing receipt's placeholder gives a DIFFERENT number -- shown side by side, so the
     gap is exhibited rather than asserted.
  4. "can only increase the variance" made a THEOREM rather than an assertion: for a mean of N
     cells with average pairwise correlation rhobar, Var = (sigma^2/N)(1 + (N-1) rhobar), which
     exceeds sigma^2/N for every rhobar > 0.  Verified symbolically AND by simulation.
  5. the paper's three window-function values, |W|^2 = sinc^2(kL/2) at k = 1/L, 3/L, 10/L.
  6. CONTROL: a NEGATIVE average correlation must REDUCE the variance, or clause 4 is vacuous and
     the "can only increase" would be true of any rhobar whatsoever.

Written r3622 by node 60, probability bake, after 59's r3620 found the skipped step.
Stated for reversal.
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
print("R2 — P04's CORRELATION FIGURES, CHECKED FOR THE FIRST TIME")
print("=" * 78)

Om, OL, z_lss, R = 0.315, 0.685, 1089.0, 8.0        # R in h^-1 Mpc, as P04 sets them
E = lambda z: np.sqrt(Om * (1 + z) ** 3 + OL)
zz = np.linspace(0, z_lss, 200000)
d_lss = 2998.0 * np.trapezoid(1 / E(zz), zz)         # h^-1 Mpc
N = d_lss / R
print(f"\n  d_lss = {d_lss:.0f} h^-1 Mpc   N = d_lss/R = {N:.0f} cells   (P04's own inputs)")

# ---------------------------------------------------------------- VERDICT 1
print("\nVERDICT 1 — P04's EFFECTIVE N, from P04's own coherence scale.")
L_coh = 138.0                                        # h^-1 Mpc, the paper's basin scale
N_eff = d_lss / L_coh
print(f"    N_eff = d_lss / {L_coh} = {N_eff:.1f}")
check("P04's stated N_eff is 68", round(N_eff), 68)

# ---------------------------------------------------------------- VERDICT 2
print("\nVERDICT 2 — AND THE RISE FACTOR, since sigma goes as 1/sqrt(N).")
rise = np.sqrt(N / N_eff)
print(f"    sqrt(N / N_eff) = sqrt({N:.0f}/{N_eff:.1f}) = {rise:.2f}")
check("P04's stated ~4x", round(rise, 1), 4.2)
print("    *** Both of P04's correlation figures are right. ***")

# ---------------------------------------------------------------- VERDICT 3
print("\nVERDICT 3 — WHAT THE EXISTING RECEIPT CHECKS INSTEAD.")
N_placeholder = N / 4
rise_placeholder = np.sqrt(N / N_placeholder)
print(f"    receipt uses N/4        = {N_placeholder:.0f}   -> rise {rise_placeholder:.2f}x")
print(f"    paper states  N_eff     = {N_eff:.0f}   -> rise {rise:.2f}x")
check("the placeholder is 293, not 68", round(N_placeholder), 293)
check("and it gives 2x, not 4x", round(rise_placeholder, 1), 2.0)
print("    *** The direction was checked.  The paper's magnitude was not. ***")

# ---------------------------------------------------------------- VERDICT 4
print("\nVERDICT 4 — 'CAN ONLY INCREASE THE VARIANCE' AS A THEOREM.")
n, sig, rho = sp.symbols('n sigma rhobar', positive=True)
var_mean = (sig**2 / n) * (1 + (n - 1) * rho)        # equicorrelated cells
indep = sig**2 / n
print(f"    Var(mean) = (sigma^2/n)(1 + (n-1) rhobar) = {sp.simplify(var_mean)}")
excess = sp.simplify(var_mean - indep)
print(f"    excess over the independent case = {sp.factor(excess)}")
check("the excess is exactly sigma^2 (n-1) rhobar / n",
      sp.simplify(excess - sig**2 * (n - 1) * rho / n), 0)
print("    -> strictly positive for every rhobar > 0 and n > 1.  A theorem, not an assertion.")
# and by simulation, so the algebra is not the only witness
rng = np.random.default_rng(20260830)
def sim(rhobar, n=200, trials=4000):
    """equicorrelated cells: x_i = sqrt(rho) z + sqrt(1-rho) e_i"""
    z = rng.normal(size=(trials, 1))
    e = rng.normal(size=(trials, n))
    x = np.sqrt(rhobar) * z + np.sqrt(1 - rhobar) * e
    return x.mean(axis=1).var()
v0, v1 = sim(0.0), sim(0.05)
print(f"    simulated Var(mean): rhobar=0 -> {v0:.5f} ;  rhobar=0.05 -> {v1:.5f}")
pred0, pred1 = 1 / 200, (1 + 199 * 0.05) / 200
print(f"    predicted           : rhobar=0 -> {pred0:.5f} ;  rhobar=0.05 -> {pred1:.5f}")
check("independent case matches sigma^2/n", float(v0), pred0, tol=0.001)
check("correlated case matches (sigma^2/n)(1+(n-1)rho)", float(v1), pred1, tol=0.005)

# ---------------------------------------------------------------- VERDICT 5
print("\nVERDICT 5 — P04's THREE WINDOW VALUES, |W|^2 = sinc^2(kL/2).")
for mult, want in ((1, 0.92), (3, 0.44), (10, 0.04)):
    half = mult / 2.0                                # kL/2 with k = mult/L
    w2 = (np.sin(half) / half) ** 2
    print(f"    k = {mult}/L  ->  |W|^2 = {w2:.3f}   (P04 says {want})")
    check(f"|W|^2 at k={mult}/L is {want}", round(w2, 2), want)
print("    *** All three of P04's window figures are exact. ***")

# ---------------------------------------------------------------- VERDICT 6
print("\nVERDICT 6 — THE CONTROL.  A NEGATIVE correlation must REDUCE the variance.")
print("  If the variance rose for every rhobar, clause 4 would be vacuous and 'positive")
print("  correlations can only increase it' would be saying nothing about positivity.")
neg = sp.simplify(excess.subs(rho, -sp.Rational(1, 400)))
print(f"    excess at rhobar = -1/400 : {sp.simplify(neg)}")
check("the excess is NEGATIVE for negative rhobar", sp.sign(neg.subs(n, 200).subs(sig, 1)), -1)
print("    -> so the sign of the effect follows the sign of rhobar, and the paper's word")
print("       'positive' is doing work.")

print("\n" + "=" * 78)
if FAIL:
    print(f"  VERDICT: {len(FAIL)} CHECK(S) FAILED")
    for f in FAIL:
        print("   ", f)
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  Every figure P04 prints is correct -- N_eff = 68, the 4x rise, and")
print("  all three window values.  *** What was missing is that its receipt checked the DIRECTION")
print("  with a placeholder N/4 = 293 and never the stated N_eff = 68. ***  P04 is WORKED for this")
print("  field, not checked-negative, and the term list is what said otherwise.")
print("=" * 78)

# `r7807+71.2` — PRE-REGISTRATION: 6b-ii, **phase 1: cone curves in a chart and the local limit-curve theorem**. ⌗ `420` lines (band 300–550), p(all four BUILT) `0.55`

*Registered before any Lean. The plan is `PLAN.md`. The probe is the new standalone `probes/LimitCurve.lean` (`lc_`).
Mathlib only.*

**Setting:**
- `E` is a finite-dimensional real normed space.
- `K ⊆ E` is closed, and closed under addition and non-negative scaling.
- `τ : E →L[ℝ] ℝ`, with `c > 0` and `c‖v‖ ≤ τ v` for every `v ∈ K`.
- A **`K`-curve** on `[a, b]` is `γ : ℝ → E` with `γ t − γ s ∈ K` whenever `a ≤ s ≤ t ≤ b`.
- It is **`τ`-parametrised** if `τ(γ s) = τ(γ a) + (s − a)`.

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| L1 | **The Lipschitz bound.** For a `K`-curve, `‖γ t − γ s‖ ≤ (τ(γ t) − τ(γ s))/c` for `s ≤ t`. So a `τ`-parametrised `K`-curve is `1/c`-Lipschitz on `[a, b]` | 40–80 | 0.9 | |
| L2 | **Closedness.** A pointwise limit of `K`-curves on `[a, b]` is a `K`-curve, and a pointwise limit of `τ`-parametrised ones is `τ`-parametrised | 40–80 | 0.9 | |
| L3 | **The local limit-curve theorem.** Let `γₙ` be `τ`-parametrised `K`-curves on `[a, b]` with `γₙ a → p` and `τ(γₙ a) = τ(p)`. Then a subsequence converges uniformly on `[a, b]` to a `τ`-parametrised `K`-curve `γ` with `γ a = p` | 180–320 | 0.55 | **The expected stop**: assembling Arzelà–Ascoli (`BoundedContinuousFunction` on the compact `Icc a b`, values in a compact ball, `1/c`-Lipschitz equicontinuity) and extracting a subsequence from compactness of the closure. **The fallback** is the uniformly bounded, equicontinuous family with compact closure in `C([a, b], E)` (L3 without the subsequence), marked BUILT IN PART |
| L4 | **Non-vacuity.** In `ℝ²` with the sup norm, `K = {(t, x) : |x| ≤ t}` and `τ(t, x) = t` (`c = 1`). The curves `γₙ(s) = (s, sin(ns)/n)` are `τ`-parametrised `K`-curves on `[0, 1]` converging to `(s, 0)` | 40–80 | 0.85 | |

**Not in this phase:** the manifold and the kit's causal arcs (phase 2), inextendibility (3), the boundary argument
(4), and `HasFutureGenerators` (5). P1's 6b-ii stays BUILT IN PART until phase 5.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

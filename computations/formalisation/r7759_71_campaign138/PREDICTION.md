# `r7759+71.1` — PRE-REGISTRATION: campaign 138, **P7's last four cored rows: the asymptotic non-intersection (1), the `sinh^{2/3}` law (6), the horizon injectivity in the embedding (3d), and the bounded turnaround along the lap (7c)**. ⌗ `560` new lines (band 400–750), p(all four BUILT) `0.5`

*Registered before any Lean. The inventory is `r7755_71_survey/SURVEY.md`. The probe is `probes/Framework.lean`,
appended (`fw_`). Mathlib only. None of these rows touches P7's rate remark, per r7759.*

**A change from the survey, stated before building.** Rows 1 and 6 were priced as ports. Neither source copies
standalone:
- **Row 1.** P2's `sr_future_diverges` sits inside `CircleChart.lean`'s causal-curve and manifold framework,
  thousands of lines deep.
- **Row 6.** `rExp` carries `LimitNariai.lean`'s own definitions.

Both rows are therefore proved afresh, in chart form, in `Framework.lean`. The price is unchanged in spirit; the
lines are new.

## Rows

| Row | Statement | Lines | p | Expected stop |
|---|---|---|---|---|
| 1 | Schwarzschild exterior, `f = 1 − 2M/r`, `r* = r + 2M log(r/2M − 1)`: `r* → −∞` as `r → 2M⁺`. **Every infall path** `r ↦ t(r)` on `(2M, r₀]` with `dt/dr ≤ −k/f` (`k > 0`) has `t → +∞` as `r → 2M⁺`, so no finite `t` reaches the horizon. This includes ingoing null rays (`dt/dr = −1/f`) and every radial timelike geodesic (`dt/dr = −E/(f√(E² − f)) ≤ −1/f`, shown) | 100–180 | 0.7 | The antitone comparison `t + k r*` on a half-open interval |
| 6 | With `A³ = 2Mα²` (`A > 0`), `r(τ̃) = A sinh^{2/3}(3τ̃/2α)` (`Real.rpow`) satisfies `r³ = 2Mα² sinh²(3τ̃/2α)` and, for `τ̃ > 0`, `(dr/dτ̃)² = 2M/r + r²/α²`. The route is implicit differentiation of the cube | 80–150 | 0.75 | `rpow` differentiability at a positive base |
| 3d | In `ℝ^{1,4}` with `−X₀² + |x|² = α²`, the waist point `p = (0, αn)` (`|n| = 1`) has oriented future horizon `ℋ⁺(n) = {X ∈ dS : X₀ > 0, X₀ = x·n}`, a null hyperplane section (normal `(−1, n)`, null). **`n ↦ ℋ⁺(n)` is injective**: for `n′ ≠ n`, the point `(t, tn + αm)`, with `m = (−n₁, n₀, −n₃, n₂) ⊥ n` and `t` large, lies in `ℋ⁺(n)` and not in `ℋ⁺(n′)`. In particular `ℋ⁺(n) ≠ ℋ⁺(−n)` | 100–180 | 0.7 | Strict Cauchy–Schwarz for unit `n ≠ n′` |
| 7c | An explicit `τ̃ : (−∞, 0] → ℂ`: `τ̃(r) = −(2α/3)i·arcsin((|r|/r₀)^{3/2})` on `[−r₀, 0]` and `(2α/3)(arcosh((|r|/r₀)^{3/2}) − iπ/2)` on `(−∞, −r₀]`. It agrees at `−r₀` and is continuous on each piece. It solves the bead `r³ = 2Mα² sinh²(3τ̃/2α)`, and `|Im τ̃| ≤ πα/3` with equality exactly for `r ≤ −r₀` | 150–300 | 0.55 | The glue at `−r₀` and the complex `sinh` of `arcosh − iπ/2`. **Fallback:** solution and bound pointwise, with the gluing named |

**If 7c falls back,** it is marked BUILT IN PART. **Non-vacuity:** witnesses at `M = 1`, `α = 1` (rows 1, 6, 7c) and at
`n = e₀`, `n′ = e₁` (row 3d).

**Interpretive, not formalised:** surjectivity of `p ↦ ℋ_c⁺(p)` onto "the oriented future horizons" (by the paper's
own construction); "the family of horizons is the congruence"; the ontological reading of the lap.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

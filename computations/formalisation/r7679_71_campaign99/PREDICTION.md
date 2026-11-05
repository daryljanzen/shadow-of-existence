# `r7679+71.1` — PRE-REGISTRATION: campaign 99, `r7679`, ④′, the retarded slicing's Cauchy property on Schwarzschild's exterior. **Registered finding: on eternal Schwarzschild's region I it is false, for every `a, η > 0`.** Θ_ret stays bounded below along every causal curve that runs into the white-hole horizon `V = 0`. P1 claims the property only for the exterior of a collapse (l.382: the slices are "continued inward through the collapsing body"), which has no white-hole horizon, so P1 is not contradicted. ⌗ Registered: ⓐ the η bound for temporality, sharp; ⓑ the refutation, with its witness curve; ⓒ the future half that does hold. `1000` new lines (band 500–2000), p `0.45` for the whole

*Registered before any Lean. The base is campaign 98's `probes/SchwarzschildEF.lean`, with the `r_U`, `r_V` lemmas of
`SchwarzschildAlign.lean` copied in. The new probe is `probes/SchwarzschildRetarded.lean`.*

## The setting

- The spacetime is campaign 98's `se_S` on `W = {V > 0, UV < 1}`.
- `D` is region I, `{U < 0, V > 0}`.
- The definition is the kit's `IsCauchyTemporalOn D Θ`: `Θ` is temporal on `D`, and every causal curve inextendible in
  `D` meets every level exactly once.
- `Θ_ret = a(u + ηr)`, with `u = −4M log(−U)` and `a, η > 0`.

## Why ④′ fails on region I

- Take `γ(s) = (U₀, eˢ)` with `U₀ < 0`. It is a future-directed null curve in `D`.
- To the past, `γ` tends to `(U₀, 0)`, which is not in `W`. To the future, `V → ∞`. So `γ` is inextendible in `D`.
- Along `γ`, `u = −4M log(−U₀)` is constant and `r > 0`, so `Θ_ret > −4Ma log(−U₀)`.
- **That level is never met.** So the Cauchy clause fails, for every `a, η > 0`.
- The stationary `t` escapes this because `t → −∞` as `V → 0`. Retarded time stays finite on the white-hole horizon.

## ⓐ Temporality and the η bound — `350` lines, p `0.65`

- In Kruskal coordinates `g = −F dU dV`, so `Θ` is temporal exactly when `Θ_U > 0` and `Θ_V > 0`.
- `Θ_V = aη U/h′(r) > 0` holds on all of region I.
- `Θ_U > 0` holds exactly when `η f < 2`, with `f = 1 − 2M/r`. This is P1's sign condition, `a²η(fη − 2) < 0`.
- **Registered:**
  - `Θ_ret` is temporal on `D` for `0 < η ≤ 2`.
  - For `η > 2`, temporality fails at some point of `D`, at large `r`. So the bound is sharp.
- **Expected stop:** `Θ_U`'s sign through `h′`, done with the same `r_U` algebra as campaign 98's ④.

## ⓑ The refutation — `150` lines, p `0.85`

- **`sr_not_cauchy`:** for every `a, η > 0`, there is a `c : InextCausalCurveIn D` and a level that `Θ_ret ∘ c.γ` never
  takes.
- The non-vacuity is this witness itself. The theorem is stated on the level-set clause alone, so it does not depend on
  ⓐ.

## ⓒ The future half — `500` lines, p `0.5`

- **`sr_future_diverges`:** for `0 < η ≤ 2`, `Θ_ret → +∞` along every future-inextendible causal curve in `D`.
- **The route:**
  - `U` and `V` are non-decreasing along the curve, and bounded monotone limits would land in `D`.
  - So either `U → 0⁻`, where `−log(−U) → ∞` and `r ≥ 2M`.
  - Or `V → ∞` with `U` bounded away from `0`, where `−UV → ∞` forces `r → ∞`.
- This is the half of the Cauchy property that the proof of `prop:causal-alignment` uses on the way to `𝓗⁺`.
- **Expected stop:** the monotone-limit step. The kit's curves are only piecewise differentiable.
- **Stretch, p `0.25`:** `Θ_ret → −∞` along curves whose past end goes to past null infinity (`U → −∞`), for `η < 2`.

## What this means for 8ii-b

The retarded half of 8ii-b cannot be BUILT on eternal Schwarzschild. On P1's reading it belongs to a collapse spacetime,
which is not in the kit. P1 l.382's last sentence ("the same for the retarded slicing is not formalised") stays true. ⓑ
lets it say why.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

# `r7645+71.4` — RESULT: campaign 81. All BUILT, with no named-hypothesis fallback. `hint` and `hcl` are derived by push-up. The headline `hl_causal_alignment_gh` takes `LocallyLipschitz g` and `J ⊆ M` in their place. The model is two-sided Cauchy. **`Model.hl_model_headline` applies the headline theorem to the Rindler model in the same file,** so `KLi(S_τ) = KLs(S_τ) = 𝓗⁺ = {U = 0}` is a proved statement about a concrete spacetime. ⌗ `2243` lines in one probe (about `330` new; about `215` lines of unused copies trimmed). ⌗ p: `hint` `0.7`, `hcl` `0.65`, two-sided model `0.55`, end-to-end `0.45`: all came true

*Against `PREDICTION.md` (`r7645+71.1`). 71 re-ran `lake env lean probes/HeadlineHypotheses.lean`. It exits 0 with no
errors. All `14` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is
clean.*

***How the probe is made.*** It has one `Spacetime` structure, merged from three copies: campaign 78's chain
(`cr_ ↦ hl_`), campaign 60's push-up (`cs_ ↦ hl_`, with its `rev`), and campaign 79's model (`st_ ↦ hl_`).

## ① `hint` and `hcl`

- **The steps.** `hl_future_step` and `hl_past_step`: the short segments `x ± εT(x)` are `TStep`s inside `M`.
- **`hl_hint`.** `interior J⁻(J) ⊆ D`, by a future step and `hl_pushup'`. It needs `J ⊆ M` so that `J⁻(J) ⊆ M`.
- **`hl_hcl`.** `closure J⁻(J) ⊆ closure D`, by a past step and push-up.
- **`hl_causal_alignment_gh`.**
  - Hypotheses: `hOD`, `hmono`, `hL : LocallyLipschitz g`, `hJM : J ⊆ M`, `hHM : 𝓗⁺ ⊆ M`, `(Dsp J).IsCauchyTemporal Θ`
    (campaign 60's two-sided definition, repaired) and `hadapt`.
  - Conclusion: properness, and `KLi = KLs = 𝓗⁺`.

## ② The model, two-sided

- `Model.hl_pastCauchy`: past-inextendible causal curves reach every lower level. `U` and `V` are non-increasing into
  the past. A curve bounded below converges inside `D`, a contradiction, and the intermediate value theorem then gives
  the level.
- `Model.hl_cauchy` then follows by `hl_cauchy_iff`, for `Θ₀` and for `Θf`.

## ③ End to end

- `hl_model_hypotheses` discharges every hypothesis:
  - `LocallyLipschitz` holds because the metric is constant;
  - `M = univ`;
  - the two-sided Cauchy property is ②;
  - the reparametrised observer gives `hOD`, `hmono` and `hadapt`.
- **`hl_model_headline`.** `D = {U < 0}`, `𝓗⁺ = {U = 0}`, and for both `Θ₀` and the tangency-failing `Θf`:
  properness, `KLi(S_τ) = {U = 0}` and `KLs(S_τ) = {U = 0}`.
- **Non-vacuity is now a theorem**, no longer an argument by comparing definitions.

## What separates P1's headline from the Lean now

***The hypotheses that remain beyond P1's.***
- `LocallyLipschitz g`: P1's `g` is smooth.
- `J ⊆ M`: P1's `J` is the worldline `O`, or `𝒥⁺` in a compactification.
- `𝓗⁺ ⊆ M`: P1's own setting.

***The gap that remains.*** The single chart. Lifting the causal chain to a Mathlib manifold needs the manifold layer
of campaigns 66 and 68 joined to campaigns 60–81. That is the next gap, as the inventory named it.

***A caveat on `J`.*** The model uses `J = range O`, the observer's worldline. In P1, `D = I⁻(O)` by hypothesis, so the
worldline is P1's own choice of `J`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

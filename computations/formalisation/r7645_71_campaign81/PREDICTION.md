# `r7645+71.1` — PRE-REGISTRATION: campaign 81, `r7645` ①–②. Derive `hint` and `hcl` by push-up from a locally Lipschitz `g`, add the past Cauchy property to campaign 79's model, and prove the headline theorem without `hcl` and `hint` *in the same file* as the model. So the model instantiates the theorem itself, and non-vacuity no longer rests on a textual identity of definitions. ⌗ `900` new lines in one probe (band 300–3000 new), ⛔ stop `4500` total. ⌗ p: `hint` derived `0.7`, `hcl` derived (with `J ⊆ M`) `0.65`, the model's two-sided Cauchy property `0.55`, the end-to-end instantiation in one file `0.45`

*Under `r7645` ①–②. A new probe, `probes/HeadlineHypotheses.lean`, made of three copies: campaign 78's
`CauchyRepair.lean` (the repaired chain); campaign 60's push-up from `CausalStructure.lean` (`pushup_cstep`, `cs_pushup`,
`cs_pushup'`, which take the same `Spacetime` structure, checked identical); and campaign 79's Rindler model from
`SliceTangency.lean`. No Lean was written before this registration.*

## ① `hint` and `hcl` by push-up

***`hint`: `interior J⁻(J) ⊆ I⁻(J)`.*** Take `x` in the interior.
- A short future step `y = x + εT(x)` stays in `J⁻(J)` and has `x ≪ y`.
- With `y ≤ z ∈ J`, campaign 60's `cs_pushup'` (`≪ ∘ ≤ ⊆ ≪`) gives `x ≪ z`, so `x ∈ D`.
- The hypothesis needed is `LocallyLipschitz g`, which P1's smooth `g` gives.

***`hcl`: `closure J⁻(J) ⊆ closure D`.*** Take `x ≤ z ∈ J` with `x ∈ M`.
- The points `x − εT(x)` are `≪ x` for small `ε`, so `≪ z` by `cs_pushup'`, so they lie in `D`, and they tend to `x`.
- So `J⁻(J) ⊆ closure D`, and then `hcl` follows by taking closures.
- The hypothesis needed is `J ⊆ M`, for the reflexive case `x = z`. P1's `J` (the worldline, or `𝒥⁺` in a
  compactification) is stated as such.

***The headline restated.*** `hl_causal_alignment_gh` takes `hL : LocallyLipschitz g` and `hJM : J ⊆ M` in place of
`hcl` and `hint`. Its other hypotheses are P1's own, plus `𝓗⁺ ⊆ M`.

## ② The model, two-sided

***The past Cauchy property.*** For `Θ_G = G(−U) + V` with `GoodG G`, every past-inextendible causal curve attains every
level `≤ Θ(γ 0)`.
- Into the past, `U` and `V` are non-increasing.
- If `Θ` were bounded below along the curve, then `V` would be bounded below and `−U` bounded. So the curve would
  converge, inside `D`, contradicting inextendibility.
- `G → −∞` at `∞` gives the levels.

***Then two-sided.*** `cr_cauchy_iff` gives `IsCauchyTemporal`, for both `Θ₀` and the failing `Θf`.

***The end-to-end theorem.*** `hl_model_headline` applies `hl_causal_alignment_gh` to the model. So
`KLi(S_τ) = KLs(S_τ) = 𝓗⁺ = {U = 0}` is a proved statement about a concrete spacetime, with every hypothesis
discharged in the same file.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative.*** `hint`'s "a short future step stays in the interior" needs openness of the interior and
continuity of `x ↦ x + εT(x)`. Neither is hard, but the step must be a `TStep` inside `M`. If that is heavy, RESULT
states `hint` with the step lemma as a named hypothesis.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

# `r7641+71.3` — PRE-REGISTRATION: campaign 78, `r7641` ② and the vacuity repair. `IsTemporal` is repaired to C¹ on `M` only, campaign 75's chain is re-derived under it, and campaign 60's two-sided Cauchy property implies the future form, via a polygonal past extension. ⌗ `700` new lines in one probe (band 250–3000 new), ⛔ stop `4000` total. ⌗ p: chain re-derived under the repaired definition `0.7`, polygonal past-inextendible extension `0.55`, two-sided ⇒ future form, and so `cp_causal_alignment` under campaign 60's definition `0.5`, the full equivalence two-sided ⇔ future ∧ past `0.35`

*Under `r7641` ②. The setting is campaign 75's `probes/CauchyProperness.lean`, copied in under a new namespace. This
campaign answers the vacuity finding of `r7641+71.1` first. No Lean was written for this campaign before this
registration.*

## ⓪ The repair

***The definition.***
- Repaired: `IsTemporal Θ := ContDiffOn ℝ 1 Θ M ∧ ∀ x ∈ M, ∀ v, FutCausal x v → 0 < fderiv ℝ Θ x v`, with `M` open.
- Old: global `ContDiff ℝ 1 Θ`.

***What carries over.***
- Every use of `IsTemporal` in the copied chain is along curves inside `M`. So `temporal_tstep`,
  `cp_temporalD_chr`, the curve, properness and the slice lower limit are expected to go through unchanged.
- `cp_causal_alignment` is re-stated under the repaired definition.

***Non-vacuity.*** That the repaired hypotheses are satisfiable with `𝓗⁺ ≠ ∅` is campaign 79's model.

## ① A polygonal past extension

***Statement.*** From any `x ∈ D` there is a past-inextendible timelike curve of `D` on `(−∞, 0]` ending at `x`.

***Route.***
- It is broken: piece `k` is the straight segment `x_k − s·T(x_k)`, for `s ∈ [0, ℓ_k]`. Here `ℓ_k` is half of the
  largest `ℓ ≤ 1` for which the segment is a `TStep`.
- It stays in `D`, since `x_{k+1} ≪ x_k ∈ D`.
- **No past limit in `D`.** If `x_k → x* ∈ D`, the tube lemma at `x*` gives `ℓ_k ≥ ℓ₀/2` eventually. Then
  `x_{k+1} − x_k ≈ −ℓ_k T(x*)` with `T(x*) ≠ 0` does not converge, a contradiction.
- The breaks are the integers, so they are finite on compacts.

## ② Two-sided ⇒ future form

***Statement.*** `(Dsp J).IsCauchyTemporal Θ → (Dsp J).FutCauchyTemporal Θ`. The proof glues ① to a
future-inextendible curve at `0`, and uses the strict increase of `Θ` to put the level hit on the future part.

***Consequence.*** `cp_causal_alignment` under campaign 60's own definition (repaired as in ⓪).

***Stretch.*** `IsCauchyTemporal ⇔ FutCauchyTemporal ∧ PastCauchyTemporal`.
- The future form alone does not imply the two-sided one: `exp ∘ Θ` is future Cauchy and never negative.
- So the exact equivalence needs the past form too, by the time-reversed construction.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative.*** The "largest safe `ℓ`" in `①` may be awkward as a supremum. If so, it is replaced by any
locally-uniform choice from the tube lemma, via `choose`, and RESULT says which was used.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

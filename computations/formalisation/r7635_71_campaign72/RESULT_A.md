# `r7635+71.3` — RESULT: campaign 72, `r7635` ②, the past cones converge to `𝓗⁺` in the Kuratowski sense, both limits BUILT; the tangency clause of `prop:causal-alignment` BUILT in Kuratowski form; for the slices only the upper limit is BUILT. ⌗ `483` lines in one probe (band 250–2500 new). ⌗ every registered p came true (`0.75`, `0.6`, `0.5`)

*Against `PREDICTION.md` (`r7635+71.2`). 71 re-ran `lake env lean probes/HorizonConvergence.lean`. It exits 0 with no
errors. All `27` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The setting is campaign 60's
C¹-chain relation, copied in.*

## Setting and hypotheses

***The observer.***
- `O : ℝ → V` with `I⁻(range O) = D`.
- `O` is monotone: `s < t ⟹ O s ≪ O t`. This is assumed.

***Two hypotheses, each used by one direction.***
- `hcl : closure J⁻(𝒥⁺) ⊆ closure D`. This is the paper's own assumption, used for the lower limit.
- `hint : int J⁻(𝒥⁺) ⊆ D`, used for the upper limit.
  - It is stated as a hypothesis because the probe uses the C¹-chain relation. For the Lipschitz relation it is
    campaign 63's `cr_interior_JpastL_subset`.
  - Without it, the upper limit is proved into `closure J⁻(𝒥⁺) ∖ D`.

***Not needed:*** push-up, a Lipschitz `g`, or convexity of `M`. The connecting set is a ball in `V`.

## ① Lower limit

***Results.***
- **`hc_lower_limit`: `𝓗⁺ ⊆ KLi(τ ↦ ∂J⁻(O τ))`.** Every neighbourhood of a horizon point meets the past cone of `O(τ)`
  for all large `τ`, not merely for arbitrarily large `τ`. This is stronger than the registered form.
- `hc_lower_limit_exists` gives the registered form.
- `hc_lower_limit_seq` gives the sequence form.

***Key lemma.*** `hc_preconnected_inter_frontier`: a preconnected set that meets `A` and has a point outside
`int A` meets `∂A`. Mathlib has no such lemma, so it was proved here.

## ② Upper limit

- `hc_upper_limit_closure_diff`: `KLs(cones) ⊆ closure J⁻(𝒥⁺) ∖ D`, with no extra hypothesis.
- **`hc_upper_limit`: `KLs(cones) ⊆ 𝓗⁺`**, given `hint`.
- `hc_upper_limit_seq` gives the sequence form.

## ③ The tangency clause, Kuratowski form

***Results.***
- **`hc_kuratowski`: `KLi(∂J⁻(O τ)) = KLs(∂J⁻(O τ)) = 𝓗⁺`.** The past cones converge to the horizon as `τ → ∞`.
- `hc_H_eq_closure_diff`: `𝓗⁺ = closure D ∖ D`, under the same two hypotheses.

***Slices.*** Only the upper limit is BUILT.
- `hc_slice_upper_limit`, `hc_slice_upper_limit_temporal` and `hc_slice_upper_limit_seq`: the slices `S_τ` accumulate
  only on `𝓗⁺`.
- These need `Θ(O τ) = τ + c`, and `Θ` increasing along `≪` toward `O`, or temporal on all of `M`. The paper has `Θ`
  temporal only on `D`, so this is stronger.

***REPORTED.***
- **The slice lower limit, `𝓗⁺ ⊆ KLi(S_τ)`.** It needs `Θ → ∞` on approach to `𝓗⁺` and an intermediate-value
  argument, which is `Θ`'s Cauchy property on `D`.
- **Differential tangency**, the slices asymptotically tangent to the generators. It waits on campaign 71.

No census row moves.

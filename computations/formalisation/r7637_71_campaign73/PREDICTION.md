# `r7637+71.1` — PRE-REGISTRATION: campaign 73, `r7637` ①–③, the ray lemma, then monotonicity of `Q`, then the generators of `𝓗⁺` as null geodesics, then differential tangency. ⌗ `900` new lines in one probe (band 300–3000 new), ⛔ stop `5000` total. ⌗ p: ray lemma `0.8`, `Q`-monotonicity `0.5`, generators as null geodesics `0.3`, differential tangency stated `0.2`

*Under `r7637` ①–③. The setting is campaign 71's `probes/LipschitzCornerCutting.lean`, copied in under a new namespace,
with campaign 70's pregeodesic results and campaign 69's a.e. machinery where they are needed. No Lean was written
before this registration.*

## ① The ray lemma (`probes/NullGenerators.lean`)

***Statement.*** Let `σ` be Lipschitz on `[0,1]`, with `σ(t) ≠ 0` on `(0,1]`, and suppose for almost every `t` that
`σ′(t) = k(t)σ(t)`. Then for every `t ∈ (0,1]`, `σ(t) = μσ(1)` for some `μ > 0`.

***Route.***
- Pick a linear functional `ℓ` with `ℓ(σ(1)) ≠ 0`.
- The component of `σ` transverse to `σ(1)`, `σ − (ℓσ/ℓσ(1))σ(1)`, has a.e. derivative proportional to itself. By a
  Grönwall/ODE-uniqueness argument for absolutely continuous functions, it vanishes on any interval where `ℓσ ≠ 0`.
- Connectedness then gives the rest, using that `σ` never passes through `0`.
- The absolute continuity of Lipschitz curves (the FTC for Lipschitz functions, `LipschitzOnWith` →
  `intervalIntegral`) is the key analytic input.

## ② Monotonicity of `Q`

***Statement.*** Along a Lipschitz future-causal curve from `p` inside the normal neighbourhood, `Q` is non-increasing.
Equivalently, `J⁺(p) ∩ U ⊆ exp_p(closed future cone)`.

***Route.***
- `(Q∘γ)′ = 2g(P, γ′)` a.e., by `lk_grad_Q` and the chain rule at differentiability points.
- `g(P, γ′) ≤ 0` when `P` is future-causal: reverse Cauchy–Schwarz, campaign 61's `lc_reverse_cs`. That `P` stays
  future-causal is a bootstrap on the set where `Q ≤ 0`.
- Then the FTC for Lipschitz `Q∘γ`.

## ③ The generators are null geodesics

***Statement.*** Combine ① and ② with campaign 71's `lk_ae_null_tangent`. Then a Lipschitz causal curve from `p` that
stays in `∂J⁺(p) ∩ U` (`Q = 0`) is a reparametrised radial null geodesic.

***Hence.*** A generator of `𝓗⁺`, which is achronal, is locally a null geodesic. It is therefore C², and campaign 70's
`ct_H_generator_null_pregeodesic` applies to it.

## ④ Stretch: differential tangency

Using campaign 72, state that the slices are asymptotically tangent to the generators, in whatever differential form
the null-geodesic generators support.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:***
- `①`'s likely stop is the FTC for Lipschitz curves into `V` in this Mathlib. If it stops, RESULT names the
  declaration.
- `②`'s likely stop is the bootstrap that keeps `P` causal along the curve.
- `③` needs the generator to be achronal in the *local* sense against the normal neighbourhood's `≪`, which
  campaign 71's `lk_chr_of_Q_neg` supplies.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

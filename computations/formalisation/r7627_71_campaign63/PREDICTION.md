# `r7627+71.1` — PRE-REGISTRATION: campaign 63, `r7627` ①, a uniform Lipschitz reparametrisation of causal curves in a compact set, then push-up for the Lipschitz relation, then the null generators of `∂J⁻`. ⌗ `900` lines in one probe (band 300–2500), ⛔ stop `3500`. ⌗ p: reparametrisation `0.6`, Lipschitz push-up `0.35`, null generators `0.15`

*Under `r7627` ①. The setting is campaign 61's `probes/LimitCurves.lean`, copied in under a new namespace. No Lean
was written before this registration.*

## ① The uniform reparametrisation (`probes/CausalReparam.lean`)

***Statement.***
- Let `K ⊆ M` be compact, in finite dimension.
- There is a constant `L_K` such that every `LipCausal` curve with image in `K` can be reparametrised by `t(γ(s))`,
  where `t(x) = −g_x(x, T)` or a fixed linear functional, chosen strictly increasing along future-causal vectors
  uniformly on `K`.
- The result is an `L_K`-Lipschitz `LipCausal` curve on an interval whose length is bounded by
  `(sup_K t − inf_K t)`.

***Key estimate.*** By coercivity (`lc_coercive`), there is `c_K > 0` with `‖v‖ ≤ c_K · τ(v)` for every `v` in the
closed future cone at points of `K`, where `τ` is a fixed linear time functional. So the arclength is controlled by
the increase of `τ`.

## ② Push-up for the Lipschitz relation

***Statement.*** `LCau q p` and `Chr p z` give `Chr q z`. It may need locally Lipschitz `g`, as in campaign 60.

***Route.*** Approximate the Lipschitz causal piece by C¹ timelike-tilted pieces, as in campaign 60's push-up, or
prove the tilt directly on chord quotients.

## ③ Stretch: null generators of `∂J⁻(S)`

***Statement.*** For `p ∈ ∂J⁻(S) ∖ closure S`, with `K`-compactness supplied as a hypothesis, there is a
past-directed `LipCausal` curve from `p` lying in `∂J⁻(S)`.

***Route.***
- Take curves from `pₙ ∈ J⁻(S)`, with `pₙ → p`.
- Reparametrise them by ① and pass to a limit (campaign 61's lemma).
- Use push-up ② to keep the limit off `I⁻(S)`.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `①` may need a hypothesis that the time functional is strictly positive on the cone over
`K`. That follows from the timelike `T` by compactness, and the derivation is part of `①`; if it is missing, that
is BUILT IN PART. `②`'s likely stop is the C¹ approximation of Lipschitz causal curves. `③`'s likely stop is the
claim that the limit avoids `I⁻(S)`, which needs `int J⁻ = I⁻` for the Lipschitz relation. Each stop is named
if hit.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

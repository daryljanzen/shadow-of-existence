# `r7629+71.1` — PRE-REGISTRATION: campaign 65, `r7629` ①, concatenation of `LCau` chains into one curve, then past-inextendibility, then discharging the ∂J⁻ generator's hypotheses. ⌗ `900` lines in one probe (band 300–2500), ⛔ stop `3500`. ⌗ p: concatenation `0.75`, past-inextendibility `0.4`, hypotheses discharged `0.25`

*Under `r7629` ①. The setting is campaign 63's `probes/CausalReparam.lean`, copied in under a new namespace. No
Lean was written before this registration.*

## ① Concatenation (`probes/CausalConcat.lean`)

***Statement.***
- `LStep x y → LStep y z → LStep x z`: join the two pieces on `[0,½]` and `[½,1]`.
- Hence `LCau x y ↔ x = y ∨ LStep x y`, and so `LCau = ReflGen LStep`.
- The same holds inside a compact `K`, as `LStepIn`.

***The work.***
- The chord condition across the junction. A chord over `[s,t] ∋ ½` is a convex combination of the two
  sub-chords, so it lies in the convex hull, using `coneHull`'s convexity and monotonicity in the arc.
- Lipschitz with the maximum constant, times 2 for the rescaling.

## ② Past-inextendibility

***Definition.*** A past-directed causal curve `γ : [0, ∞) → M` is past-inextendible if `γ(t)` has no limit in `M`
as `t → ∞`.

***Statement.*** Take a limit of causal curves from `pₙ → p` that leave every compact subset of `M`, in a
"no imprisonment" setting. Build it by a diagonal argument over an exhaustion of `M` by compact sets, applying
campaign 63's closedness on each one. The limit is a past-inextendible causal curve from `p`.

***Hypothesis.*** Non-imprisonment, i.e. strong causality on the compact sets, is taken as a hypothesis if it is
needed. RESULT says so.

## ③ Stretch: discharging the ∂J⁻ generator's hypotheses

***Statement.*** Derive the approximants from `p ∈ closure J⁻(A)`, using ①. Replace the compact `K` by the
exhaustion of ②, so that `cr_boundary_generator` becomes a past-inextendible generator, or a generator ending on
`closure A`.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `②` may need a non-imprisonment or strong-causality hypothesis. If it is stated as a
hypothesis rather than derived from global hyperbolicity, that is BUILT IN PART. `③`'s likely stop is
uniformising `τ` over an exhaustion, since no single linear `τ` serves globally. RESULT names it if hit. Geodesics
of `g` are out of scope this campaign, per the order.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

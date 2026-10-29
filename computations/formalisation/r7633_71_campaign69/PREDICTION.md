# `r7633+71.1` — PRE-REGISTRATION: campaign 69, `r7633` ①, the regularity of the ∂J⁻ generators. ⌗ `600` lines of new material in one probe (band 200–2000 new), ⛔ stop `5000` total. ⌗ p: a.e. differentiable with causal velocity `0.75`, null a.e. `0.55`, a reparametrisation with a.e. unit time-rate `0.4`

*Under `r7633` ①. The setting is campaign 67's `probes/CausalGenerator.lean`, copied in under a new namespace. No
Lean was written before this registration.*

## The generators' regularity (`probes/GeneratorRegularity.lean`)

The generators of `cg_generator` are already Lipschitz. This campaign adds:
- ***a.e. differentiability.*** By Rademacher, through Mathlib's `LipschitzWith.ae_differentiableAt` or its
  `LipschitzOnWith` form on an interval, in finite dimension, a generator is differentiable at almost every
  parameter.
- ***causal velocity a.e.*** Campaign 61's `lc_velocity_mem_cone_fd` gives every right derivative in the closed
  cone. So the velocity is future-causal, or zero, a.e.
- ***null a.e.*** Achronality says no two points of the generator are joined by `≪`. At a differentiability point
  with timelike velocity, campaign 67's `cg_not_timelike_of_achronal` argument, localised, gives a timelike
  chord. So the velocity is null, or zero, a.e.
- ***a parametrisation by the time function.*** Reparametrise by `θ` (campaign 67's C¹ time function), so the
  velocity is nonzero a.e. with `dθ(γ′) = 1` a.e.

***Scope.*** C¹ regularity everywhere is NOT registered. For a smooth metric, the generators are null geodesics,
hence smooth, but proving that is the corner-cutting route of campaign 70. This campaign delivers the a.e.
regularity the corner-cutting lemma consumes.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** the a.e. velocity's membership in the cone needs the right derivative at a.e. point to
equal the derivative. That is fine where the curve is differentiable. The localised achronality argument needs a
point with timelike velocity to give a chord that is *timelike* in campaign 60's `Chr` sense. That needs a
C¹-in-a-neighbourhood straight segment, which campaign 60's openness machinery supplies. The likely stop is that
transfer, and RESULT names it if hit.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

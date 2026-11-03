# `r7663+71.1` — PRE-REGISTRATION: campaign 91, `r7663`, three pieces in 69's order: ① no past light cone meets `𝓗⁺`; ② a four-dimensional witness; ③ tangency instantiated on the curved `−F dU dV`. ⌗ ① `250` new lines (band 100–700), p `0.8`. ② `900` (band 400–2000), p `0.6`. ③ `250` (band 100–700), p `0.75`. **Expected stops:** ① the closure step below; ② the Cauchy property on a non-compact fibre; ③ bounding the rescaled frame in the chart

*Under `r7663`. Three new probes, built in parallel:
- `probes/ConeDisjoint.lean` for ①, from campaign 89's `ConformalBoundary.lean`;
- `probes/FourDWitness.lean` for ②, from campaign 90 (b)'s `CylinderWitness.lean`;
- `probes/CurvedTangency.lean` for ③, from campaign 90 (a)'s `Compactification.lean`.

No Lean was written before this registration.*

## ① `S.cone O τ ∩ S.H J = ∅` — the closure step, priced

***Where P1's line stops.*** P1's argument, that `D` is open, shows only `J⁻(O τ) ∩ 𝓗⁺ = ∅`. The cone is the frontier
of `J⁻(O τ)`, so the clause needs `closure J⁻(O τ) ∩ 𝓗⁺ = ∅`.

***Why that is not free.*** In a general spacetime, for `x ∈ closure J⁻(p)` and `p ≪ q`, it can fail that `x ≪ q`. That
implication is the past-reflecting property. So the clause needs more than openness.

***The route.*** It uses the Cauchy property, which `mx_prop_causal_alignment` already assumes.
1. `x ∈ closure J⁻(p)` gives `I⁻(x) ⊆ I⁻(p)` in any spacetime. For `y ≪ x`, `I⁺(y)` is a neighbourhood of `x`, so it
   meets `J⁻(p)`, and push-up gives `y ≪ p`.
2. If `x ∈ 𝓗⁺`, campaign 87's curve into `x` lies in `D` with `Θ → ∞` along it (`mh_blowup`).
3. But each of its points is `≪ x`, so it lies in `I⁻(O τ)`, where `Θ < τ + c` by temporal increase. This is a
   contradiction.

***Hence.***
- The clause is an eighth conjunct of a new `mx_prop_causal_alignment'`, with no new hypothesis. It also comes as a
  corollary, `mx_cone_disjoint`, under `hΘ`.
- It does **not** go into `mc_cone_kuratowski_N`, which takes no `Θ`.
- RESULT will say that the clause uses the Cauchy property. In P1 that is the global hyperbolicity of `D`, not only the
  openness its proof cites.

***Witness.*** `Pt`, with `cone ∩ {U = 0} = ∅` for every `τ`.

## ② A four-dimensional witness

***The space.***
- `N = ℝ⁴` as the model space `P × (ℝ × ℝ)`, with `g = −dU dV + dy² + dz²`.
- It has one chart; this witness is about dimension, and (b) is the multi-chart one.

***What it carries.***
- The Rindler observer at fixed `(y, z)`.
- `D = {U < 0}` and `𝓗⁺ = {U = 0}`, a null hyperplane.
- `Θ = −log(−U) + V`.
- The Cauchy property is proved by (b)'s projection argument with the fibre `ℝ²`. The transverse length is bounded by
  `Δ(U+V)/2`, and inextendibility descends because `ℝ²` is complete.

***Conclusions.***
- Every conclusion of `mh_causal_alignment_gh_N` and `mc_cone_kuratowski_N`, together with ①'s disjointness.
- Tangency at every horizon point, with `ℓ = ∂_V`, `n = 2∂_U` and `W = span(∂_y, ∂_z)`.

***Stated in advance.***
- `∂J⁻(𝒥⁺)` is not exercised in four dimensions, for the reason (b) found: `(arctan U, arctan V, y, z)` is not
  conformal for the product metric.
- The honest compactification is the Penrose one of `ℝ^{3,1}` into the Einstein static universe. That is a stretch at
  p `0.1`, which I will not attempt here.
- So the remark's "a four-dimensional witness" can go, but it must say the 4D witness does not exercise the
  `𝒥⁺` identification.

## ③ Tangency on `−F dU dV`

***The frame and the limit.*** At any horizon point `q`:
- the frame is `ℓ = ∂_V` and `n = (2/F)∂_U`, so `g(ℓ, n) = −1`;
- `dΘ₀(ℓ) = 1` and `dΘ₀(n) = 2/(F·(−U)) → ∞`;
- `‖n‖ ≤ 2/inf F` near `q`, by continuity and positivity of `F`;
- so `mc_tangency_at_N` gives the limit `(F(q)/2) dU = −g_q(ℓ, ·)`.

***Witness.*** It is instantiated for `F = e^{UV}` at `p₀`, removing the last caveat on `cz_witness_headline_F`.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED, with the step that stopped. Non-vacuity is mandatory.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

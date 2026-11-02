# `r7657+71.1` — PRE-REGISTRATION: campaign 88, `r7657`, the cone-convergence and tangency clauses of `prop:causal-alignment` carried onto a multi-chart `N`, witnessed on the two-chart `Pt`; the `∂J⁻(𝒥⁺)` identification registered and priced, not built. ⌗ `900` new lines in one probe (band 400–2500 new), ⛔ stop `3500` new. ⌗ p: cone convergence on `N` `0.7`; the tangency clause on `N` `0.55`; the witness on `Pt`, alignment for `Θ₀ ∘ φ` and failure for `Θf ∘ φ`, `0.45` given both. **Expected stop: stating tangency on `N` chart-invariantly.** Mathlib reads `dΘ_x` in `x`'s preferred chart, so a limit of covectors as `x → q` needs them re-read in one chart at `q` through `tangentCoordChange`, together with that change's continuity. Second likeliest: the witness's derivative computation at horizon points in the `nullH` chart

*Under `r7657`. A new probe, `probes/ManifoldCones.lean`. It copies:
- campaign 87's `ManifoldHeadline.lean`, with its kit, `mh_hint`, `mh_hcl`, `NModel.Pt` and its two-chart atlas;
- campaign 72's `HorizonConvergence.lean`, the cone limits;
- campaign 80's `TangencyCondition.lean`, the frame-free pointwise and filter theorems;
- campaign 79's `SliceTangency.lean`, `st_aligned` and `st_tangency_fails`.

No Lean was written before this registration.*

## ① Cone convergence on `N` (`hL : LocallyOneChart`, `[T2Space N]`)

- **Lower limit, `𝓗⁺ ⊆ KLi(τ ↦ ∂J⁻_N(O τ))`.**
  - Take a preconnected neighbourhood of `q`, which a chart ball supplies on any manifold.
  - It meets `D` by `mh_hcl`, so for large `τ` it meets `I⁻(O τ)`.
  - It has a point outside `J⁻(O τ)`, namely `q` itself, because push-up (`mk_pushup`) gives
    `J⁻(O τ) ⊆ I⁻(O(τ+1)) ⊆ D`, and `q ∉ D`.
  - Campaign 72's `hc_preconnected_inter_frontier` is purely topological, so it carries over.
- **Upper limit, `KLs ⊆ 𝓗⁺`.**
  - A limit point lies in `closure D`.
  - It is not in `D`: a point of `D` has the open neighbourhood `I⁻(O σ)`, which lies inside `int J⁻(O τ)` for every
    `τ > σ`.
  - `mh_hint` then closes the step.
- **`mc_cone_kuratowski_N`**: `KLi = KLs = 𝓗⁺` for the past cones, on the hypotheses of `mh_causal_alignment_gh_N` minus
  `Θ`.

## ② Tangency on `N`

***Statement.*** Fix a chart `e` at the horizon point `q` (the `LocallyOneChart` chart).
- Read `dΘ_x`, and the null frame `ℓ_x, n_x` at `x`, in `e` through `tangentCoordChange`.
- Then campaign 80's condition, `ξ(ℓ)/ξ(n) → 0` with the norm bounds, gives `ξ/ξ(n) → −g_e(ℓ, ·)` along `𝓝[D] q`.

***Proof.*** Campaign 80's `tc_tendsto` is frame-free and holds along any filter with moving frames and metrics, so the
step on `N` is the chart re-reading.

***Chart-independence.*** Changing `e` to another chart at `q` changes the limit by the coordinate change at `q`. This
is registered as part of ②, not as a stretch.

## ③ The witness on `Pt`

***Holds and fails.***
- **Holds:** alignment for `Θ₀ ∘ φ` (campaign 79's `st_aligned`).
- **Fails:** alignment for `Θf ∘ φ` (`st_tangency_fails`).
- Both are stated on `Pt` with the cone and tangency theorems of ① and ②, so the witness is non-vacuous on both
  sides.
- Cone convergence on `Pt` gives `KLi = KLs = {U = 0}`.

***The limit, as before.*** One chart covers `Pt`. The flat cylinder waits, as 69 ordered.

## ④ The third piece: `𝓗⁺ = ∂J⁻(𝒥⁺)`. Registered and priced, not built

***(A) The `I⁻` identity as a hypothesis.***
- Take `I⁻(𝒥⁺)` and `J⁻(𝒥⁺)` as subsets of `N` with:
  - `I⁻(𝒥⁺)` open;
  - `I⁻(𝒥⁺) ⊆ J⁻(𝒥⁺) ⊆ closure I⁻(𝒥⁺)`;
  - `int J⁻(𝒥⁺) ⊆ I⁻(𝒥⁺)`;
  - `I⁻(O) = I⁻(𝒥⁺)`.
- Then `frontier J⁻(O) = frontier J⁻(𝒥⁺)` follows by topology and campaign 87's `mh_hint` and `mh_hcl`.
- **Price:** about `250` lines, p `0.85`.
- **Weakness:** the causal properties of `𝒥⁺` are assumed, and only a stub `𝒥⁺` can witness them.

***(B) A conformal extension.***
- The setup:
  - a second manifold `Ñ` carrying its own `MSpacetime`;
  - an open embedding `ι : N → Ñ` with `ι* g̃ = Ω² g`, `Ω > 0`, and the time orientations agreeing;
  - `𝒥⁺ ⊆ frontier ι(N)`;
  - `J⁻(𝒥⁺) := ι⁻¹ J⁻_Ñ(𝒥⁺)`.
- What it needs:
  - pointwise conformal invariance of causal character, which is easy;
  - curve transport through `ι` via `mfderiv`, which campaign 84's chart transfer already does for `ContMDiff`
    curves;
  - push-up in `Ñ`, which is campaign 86's kit applied to `Ñ`;
  - a witness: `Pt`'s region `{U < 0}` compactified by `v = arctan V`. There `g̃ = −du dv` extends smoothly, and
    `𝒥⁺ ∋ (u, π/2)` for `u < 0`.
- **Price:** `1500–3000` lines, p `0.35`.
- **Expected stop:** showing `I⁻_Ñ(𝒥⁺) ∩ ι(N) = I⁻(O)` on the witness, where curves may leave `ι(N)`.

***Recommendation.*** (B), because (A) assumes the step it would identify. (A) is the fallback if 69 wants the clause
closed cheaply first.

***Failable:*** each of ①–③ is BUILT, BUILT IN PART, or REPORTED, with the step that stopped. Non-vacuity is shown for
every theorem by the `Pt` witness.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

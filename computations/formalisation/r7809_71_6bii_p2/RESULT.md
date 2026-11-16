# `r7809+71.2` — RESULT: 6b-ii, **phase 2 BUILT AS REGISTERED: the kit's causal arcs are locally cone curves; the limit-curve theorem for chains in a chart and on `N` (K1–K5, K7). K6, the global patching, NOT BUILT, the registered stop.** ⌗ `567` new lines (band 600–1100, estimate 800, **under by 233**), at p `0.45`

*The registration is `PREDICTION.md` and the plan `../r7807_71_6bii/PLAN.md`. The probe is the new standalone file
`probes/ConeCurves.lean` (`kc_`): 1349 lines, of which 782 are verbatim copies and 567 are new.*

## Verification
- `lake env lean probes/ConeCurves.lean` gives **0 errors and 0 warnings**.
- **6 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, the only import is `Mathlib`, `check_no_sorry.py` reports ALL 29, and no
  options are set.
- **The copies are byte-identical** (checked by substring):
  - `probes/LimitCurve.lean` l.16–140 (phase 1, rows L1–L3).
  - `probes/GeneratorStretch.lean`:
    - l.499–534 and l.1020–1030: the chart `Spacetime` and `restrict`.
    - l.627–636: `futTimelike_smul`.
    - l.2363–2448: campaign 84's `V`-side helpers and the squash.
    - l.2777–3278: the manifold kit through `ch_cau_iff`.
    - l.3543–3554: `restrictM`.

## Rows

At `x₀ ∈ M` of the kit's chart spacetime `S`, `τ₀ v = −g_{x₀}(v, T x₀)` (`kc_τ`) and `K(c) = {v : c‖v‖ ≤ τ₀ v}`
(`kc_K`).

| Row | Statement (Lean) | Mark |
|---|---|---|
| K1 | `kc_cone`: for `V` finite-dimensional and `x₀ ∈ M`, there are `r, c > 0` with `ball x₀ r ⊆ M` such that every future-causal vector at every point of the ball lies in `K(c)` | **BUILT** |
| K2 | `kc_KCurve_of_deriv`: a `C¹` arc with velocity in `{c‖v‖ ≤ τ v}` on `[a, b]` is a cone curve there. `kc_cstep_arc`: every arc of a step of `S.restrict B` (where K1 holds) is a `K(c)`-curve with nonzero velocity. `kc_cau_K`: a chain of `S.restrict B` has `y − x ∈ K(c)` | **BUILT** |
| K3 | `kc_reparam`: one arc, reparametrised by the inverse of the strictly increasing `τ ∘ γ`. `kc_concat`: concatenation. `kc_chain`: a chain of `S.restrict B` from `x ∈ B` gives a `τ₀`-parametrised `K(c)`-curve on `[τ₀ x, τ₀ y]` from `x` to `y` with values in `B` | **BUILT** |
| K4 | `kc_local_limit`: around `x₀` there are a ball `B = ball x₀ r` with `closedBall x₀ r ⊆ M` and a cone `K(c)` such that chains of `S.restrict B` with starts `xₙ → p` rising by `δ` in `τ₀` have parametrisations `ηₙ` on `[0, δ]` with `ηₙ 0 = xₙ` and values in `B`, and a subsequence converging **uniformly** to a `τ₀`-parametrised `K(c)`-curve `γ` with `γ 0 = p` and values in `closedBall x₀ r` | **BUILT** |
| K5 | `kc_manifold_limit`: under the kit's `OneChart p₀`, every `x₀ ∈ M` has an open `U ∋ x₀` in `M`, a `τ` and a closed cone `K` uniformly timelike for it, such that chains of `S.restrictM U` with starts `xₙ → p ∈ U` rising by `δ` in `τ ∘ φ` have chart parametrisations converging uniformly (on a subsequence) to a `τ`-parametrised `K`-curve `γ`. **Its pull-back `φ⁻¹ ∘ γ` is a continuous curve in `M` from `p`**, and the pulled-back parametrisations (points of `U`) converge to it pointwise in `N` | **BUILT** |
| K6 | The global limit-curve theorem on `N`, patching charts in an auxiliary metric | **NOT BUILT** (the registered stop) |
| K7 | `kc_witness`: the 2D Minkowski chart `kc_mink` (`g = diag(−1, 1)`, `T = (1, 0)`, sup norm), where `τ₀ = fst`. For K4's ball, the arcs `γₙ(t) = (t r/2, r sin(m t)/(4m))`, `m = n + 1`, are chains from `0` rising by `r/2`, and K4 produces from them a uniform-limit `τ₀`-parametrised cone curve from `0` | **BUILT** |

**Against the registration:**
- **K1–K5 and K7 are all built**, the joint event registered at p 0.45.
- **The named stop held.** K6 was not attempted. Patching the local limit segments into one curve on `N` is the
  maximal-extension argument that phase 3 (inextendibility) runs anyway. It moves there, and phase 3's price rises
  accordingly (below).
- **K5's bookkeeping caution did not bite.** The restricted `MSpacetime` keeps `OneChart`
  (`kc_oneChart_restrict`), and its chart steps are steps of the restricted chart directly (`kc_cau_transfer`).
  No structure equality was needed.
- **Strengthened beyond the registration:**
  - K4 also gives `closedBall x₀ r ⊆ M` and keeps the limit in that closed ball. This is what lets K5 pull the
    limit back through the chart.
  - K7's sequence genuinely varies, rather than being a constant chain.
- **Size:** 567 new lines against an estimate of 800.

**Mathlib gap: none found.** The order asked me to stop and name any gap. There was none. Everything used is in
Mathlib:
- compactness of the unit sphere in finite dimension;
- the boundary-function mean-value inequality (`image_norm_le_of_norm_deriv_right_le_deriv_boundary`);
- `strictMonoOn_of_deriv_pos`, `intermediate_value_Icc` and `Function.invFunOn` for the reparametrisation;
- `continuousOn_extChartAt_symm` and `isOpen_extChartAt_target` for the pull-back.

**What phase 2 does not give** (needed later):
- **`OneChart` versus `LocallyOneChart`.** K5 is stated under `OneChart p₀`, as registered, so all of `M` lies in
  one chart's source. Under the kit's `LocallyOneChart` it applies to the restriction to a chart neighbourhood of
  each point. That restriction step is not written.
- **Points of the parametrisations.** These are points of the chart arcs. That they are `J⁺(xₙ)`-points
  (`Cau xₙ (ηₙ s)`) is not proved. Phase 4 will need it: sub-arcs of a `C¹` arc are steps, by the kit's affine
  reparametrisation.

**Re-pricing the remaining phases:**
- **Phase 3** absorbs K6. Its band rises from 600–1400 to 800–1700, and p falls from 0.4 to 0.35.
- **Phases 4–5** are unchanged.

**Standing of 6b-ii:** still BUILT IN PART, per r7809: nothing lands in P1 until the row is whole.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

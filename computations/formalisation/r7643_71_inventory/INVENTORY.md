# Inventory of P1 (`corpus/BH_causality_v2.tex`) against the Lean probes — draft under `r7643+71.2`

*A reading, done by the method in `r7643_71_inventory/PREDICTION.md`. P1 is read as it stands at `d2dd34d` (r7643).
Every theorem name below was checked by grepping the probe itself, both its statement and its module docstring.
Campaigns 74 and 75 are counted only through 78 and 79. Campaign 80 is not built.*

## The population

The grep for `\begin{theorem|proposition|lemma|corollary}` finds **8**, the registered list:
- `thm:metric-singularity` (l.130);
- `cor:threefold` (l.166);
- the EF-degeneracy corollary (l.220; it has no `\label`);
- `lem:killing` (l.267);
- `cor:stationary` (l.281);
- `prop:causal-alignment` (l.300);
- `cor:densities` (l.312);
- `lem:alignment` (l.330).

Remarks that a proof uses:
- the unnamed remark after the theorem, which gives the along-the-connection form of (b). It is used by `lem:killing`'s proof and covered under the theorem.
- `rem:PG-forcing` and `rem:penetrating`. No statement's proof uses them. Both are interpretive, and neither is formalised.

## The setting of the Lean, read once

Nearly every gap below comes back to one of these points.
- **The single chart.** Campaigns 60–79 build the causal layer (`Spacetime V`) on one chart. `M ⊆ V` is an open subset of a real normed space, and `g` is a continuous symmetric field with time orientation `T`.
  - `≪` and `≤` are chains of C¹ steps.
  - `𝒥⁺ = J` is an arbitrary set: there is no conformal completion and no asymptotic flatness.
  - `D = I⁻(J)`, `𝓗⁺ = frontier J⁻(J)`, `BH = M ∖ J⁻(J)`.
  - Nothing is stated on a Mathlib manifold.
  - The registered rule lists "a chart" as a reduced setting. So every causal clause below carries at least the gap **(chart)**.
  - That gap is topological only. Kruskal, `ℝ²×S² ≅ ℝ×(ℝ³∖0)`, is an open subset of `ℝ⁴`, so P1's exemplar fits one chart. A general asymptotically flat spacetime need not.
- **Stated rather than derived.** The causal-limit theorems carry three hypotheses that P1's smooth setting implies, but that no probe derives for the C¹-chain relation:
  - `hcl : closure J⁻(J) ⊆ closure D`;
  - `hint : interior J⁻(J) ⊆ D` (the Lipschitz-relation analogue is `cr_interior_JpastL_subset`, campaign 63, in a different relation);
  - `hHM : 𝓗⁺ ⊆ M`.
  
  They are not *stronger* than P1. They are open obligations.
- **The `IsTemporal` repair.** `IsTemporal` now means `ContDiffOn ℝ 1 τ M ∧ …`. This is in campaign 78, `CauchyRepair.lean`, and its definitions are textually identical to 79's.
  - `VacuityCheck.cp_vacuous` derives `False` from 75's hypotheses.
  - Non-vacuity of the repaired hypotheses is campaign 79's `Model.st_model`, `Model.st_futCauchy` and `Model.GoodG.st_adapted`. The model is 2D Minkowski with a Rindler `J`, and has `𝓗⁺ = {U=0} ≠ ∅`.
  - The model proves the **future** Cauchy property only, so it witnesses `cr_causal_alignment`. It does not witness the two-sided `cr_causal_alignment_gh`.

---

## 1. `thm:metric-singularity`

| # | Clause (P1 now) | Lean (probe · theorem) | Mark |
|---|---|---|---|
| 1a | (a) `Δs²=0` and (b) `Δx=0` give `Δτ=0`, through the metric relation `Δs² = Δx² − Δτ²` on the invariant separations | `MetricSingularity.lean` · `ms_metric_singularity_scalar`, `ms_metric_singularity_vec` | **BUILT**. P1's proof takes the relation as the metric's local form and substitutes. Lean takes it as a hypothesis and substitutes, which is the same content. The adapted frame is not constructed, and P1 does not construct it either. |
| 1b | Along-the-connection form (the remark): (b) holds along the whole null geodesic, so the finite `Δτ` vanishes | `MetricSingularity.lean` · `ms_metric_singularity_along` (`τ′=0` on `[0,1]`, `τ 1 = τ 0`, `x 1 = x 0`) | **BUILT IN PART**. It is stated only for a curve `(τ,x)` with the flat quadratic form `‖x′‖² − τ′²`, i.e. in an orthonormal adapted frame along the curve. No general Lorentzian `g`, no foliation and no invariant spatial coordinate appear. |
| 1c | "…metrically coincident…while remaining…topologically distinct and causally ordered" | — | **NOT BEGUN**. Distinctness and causal order are not stated. |

## 2. `cor:threefold`

Hypotheses in P1: `γ` is a future null geodesic segment from `p` to `q`, and `q ∈ ∂J⁺(p)`.

| # | Clause | Lean | Mark |
|---|---|---|---|
| 2i | `p ≠ q`, so they are topologically distinguishable | — | **NOT BEGUN** (it is trivial in a Hausdorff space). |
| 2ii | Strict null ordering `p ≺_∂ q`: `q ∈ ∂J⁺(p)`, and no event between them lies in `I⁺(p)` | — | **NOT BEGUN** for a point `p`. Related pieces exist only for `∂J⁻(A)`: achronality `ct_H_achronal` (`CornerCutting.lean`), achronal generators `cg_generator` (`CausalGenerator.lean`), and `gr_generator_null_ae` (`GeneratorRegularity.lean`). |
| 2iii | `g(γ̇,γ̇)=0` along the whole segment | `MetricSingularity.lean` · `ms_threefold_iii`, `ms_threefold_iii_of_b` | **BUILT IN PART**. The Minkowski form is `ms_g = ‖x′‖² − τ′²` in a flat chart, and `ms_threefold_iii` restates its own hypothesis. A null geodesic of a general `g` is not used. |
| 2iv-a | Under (b) of the theorem, the pair is metrically coincident | `MetricSingularity.lean` · `ms_metric_singularity_along` | **BUILT IN PART**, the same gap as 1b. |
| 2iv-b | Without (b), `τ(q)−τ(p)` has no invariant meaning: a smooth local deformation of `τ` near `γ` changes it | `MetricSingularity.lean` · `ms_threefold_iv_noninvariance` | **BUILT IN PART**. See the notes below the table. |

Notes on 2iv-b:
- The setting is a flat `ℝ^{n+1}`.
- "Temporal" is the surrogate `∂_t τ ≥ c > 0` against a fixed `e₀`, not `dτ > 0` on the Lorentzian causal cone. The bump keeps the surrogate (`∂_t(τ+φ) ≥ c/2`), not timelike gradient.
- The support is a ball about `q` that misses `p`, which is a neighbourhood of a point of `γ`.

## 3. The EF-degeneracy corollary (unlabelled, l.220)

| # | Clause | Lean | Mark |
|---|---|---|---|
| 3a | In ingoing EF `(v,r)`, horizon events `p` and `q` on one generator lie on distinct points of the null boundary of an exterior static observer's causal past, causally ordered but null-related | General chart only: `HorizonConvergence.lean` · `hc_H_eq_closure_diff` (`𝓗⁺ = closure D ∖ D`, with `D = I⁻(O)` by `hOD`, under `hcl`, `hint`) | **BUILT IN PART**. It is the general chart statement. There is no Schwarzschild/EF instance of `Spacetime`, and no order statement for `p` and `q`. *Reading flag:* "the observer's causal past" must mean the past of the whole worldline. The past of one `O(τ)` misses `𝓗⁺` (`cs_lightcone_inter_H`, and P1's own `prop:causal-alignment`). |
| 3b | Both are at `r = r_h`, so (b) holds, the theorem applies, and they are metrically coincident; they have no invariant temporal separation | Supporting algebra only. The census-row probe `NoConnectionSweep.lean` (campaign 20, not a P1 campaign) has `schw_charts` (the EF substitution, with Killing norm `−f`), `ef_det`, and `ef_horizon_degenerate` (the induced metric on `r=2M` is `diag(0, r_h², r_h² sin²θ)` and kills `∂_v`). Plus `ms_metric_singularity_*`. | **NOT BEGUN** as a statement about Schwarzschild horizon events. The pieces exist, but no theorem puts them together. |
| 3c | The vertical extent in the EF diagram encodes only causal order | — | **NOT BEGUN** (it is interpretive). |

## 4. `lem:killing`

| # | Clause | Lean | Mark |
|---|---|---|---|
| 4a | Away from a bifurcation surface (`χ ≠ 0`) there are adapted coordinates with `χ = ∂_λ`, and the metric does not depend on `λ` | Model space: `FlowC1.lean` · `fc_flowBox_exists`, `fc_flowBox_killing`. Manifold: `FlowManifold.lean` · `fm_manifold_killingChart_section`. Coordinate-free condition `L_X g = 0`: `LieDerivManifold.lean` · `ld_manifold_killingChart_lieDeriv` (gives a `LocalKillingChart`), `LocalKillingChart.ld_metric_N`, `ld_lieDeriv_chart` | **BUILT IN PART**. See the notes below the table. |
| 4b | (a): along the generator `ds² = |χ|²dλ²`, so being null with `dλ ≠ 0` forces `|χ|² = 0` | `KillingHorizon.lean` · `kh_interval_orbit`, `kh_forcing`, `kh_null_along_generator` | **BUILT IN PART**. It is stated only in campaign 59's global adapted `KillingChart` on `ℝ×E`. It is not re-proved for the derived `LocalKillingChart` of 66/68: `MetricallyCoincident` does not occur in those files. |
| 4c | (b): the flow is an isometry mapping each generator into itself, so every transverse invariant is equal at `p`, at `q` and between them (no expansion or shear) | `KillingHorizon.lean` · `kh_flow_isometry`, `kh_flow_pullback`, `kh_flow_maps_union_of_orbits`, `kh_transverse_invariant`, `kh_transverse_invariant_between`. Coordinate-free isometry: `fc_flow_isometry`; `fm_flow_isometry_loc` | **BUILT IN PART**. The same split: transport is shown in the global chart. On a manifold only the chart is derived. |
| 4d | Conclusion: `p` and `q` are metrically coincident, and `𝒦` is a metric singularity | `KillingHorizon.lean` · `kh_lemma_killing` (gives the structure `MetricallyCoincident`: (a), (b), (b) between, `Δx=0`, `Δτ=0`) | **BUILT IN PART**. See the notes below the table. |

Notes on 4a:
- This needs a C² manifold. RESULT 68 calls that a mathematical limit of chart invariance.
- `g`'s differentiability is still stated in chart form.
- P1's smooth setting meets both.

Notes on 4d:
- It is stated in the global `KillingChart` only.
- The link from `LocalKillingChart` to the conclusion is not written.
- **No non-vacuity witness.** No Lean instance has a null orbit, such as Minkowski with a null translation, or Rindler. The witness is easy, but it is not there.
- The Lean hypothesis "the orbit is null at one parameter" is weaker than P1's "Killing horizon", which is fine.

## 5. `cor:stationary`

| # | Clause | Lean | Mark |
|---|---|---|---|
| 5 | The event horizon of a stationary black hole is a metric singularity (by rigidity it is a Killing horizon, under that theorem's hypotheses, including analyticity) | `KillingHorizon.lean` · `kh_cor_stationary` under `Rigidity n H` | **BUILT IN PART**. See the notes below the table. |

Notes on 5:
- **Rigidity is assumed as a hypothesis.** P1 also cites it, so assuming it is no stronger than P1.
- **"Killing horizon" is encoded strongly.** It means a single global adapted `KillingChart`, with `H` a union of null orbits. That is stronger than the local Killing-horizon notion of the manifold route.
- **Undefined terms.** "Stationary black hole" and "event horizon" are not defined in this probe.
- **No non-vacuity witness.**

## 6. `prop:causal-alignment`

### The hypotheses

How P1's hypotheses are encoded:
- **`D` globally hyperbolic, with `Θ` a smooth Cauchy temporal function of `D`.** This is `(S.Dsp J).IsCauchyTemporal Θ`, with the repaired `IsTemporal` (C¹ on `D`). Bernal–Sánchez is taken as the definition. The future form `FutCauchyTemporal` is weaker, and is implied by `cr_futCauchy_of_cauchy_D`.
- **The observer `O`.** `I⁻(O) = D` is `hOD`. "Worldline" is `hmono : s<t → O s ≪ O t`. Future-completeness and `O(τ) → i⁺` are not needed by the Lean.
- **The adapted condition.** It is `hadapt`.
- **Asymptotic flatness.** It is not modelled. Taking `J` arbitrary is more general.

### The clauses

| # | Clause | Lean | Mark |
|---|---|---|---|
| 6a | No past light cone `∂J⁻(O(τ))` meets `𝓗⁺` | `CausalStructure.lean` · `cs_lightcone_inter_H`, `cs_worldline_cones` (and `cs_observer_Ipast` for `I⁻`) | **BUILT IN PART**. (chart). It also needs `IsClosed (J⁻(O τ))` as a hypothesis: P1 gets this from GH, but here it is not derived. It needs locally Lipschitz `g`, which P1 supplies. No `Θ` is involved, so the vacuity does not reach it. |
| 6b | The cones converge to `𝓗⁺` as `τ → ∞`, and the stretch they approach to within any distance extends to the future without bound | `HorizonConvergence.lean` (72) · `hc_kuratowski` (`KLi = KLs = 𝓗⁺`), `hc_lower_limit` (every neighbourhood of a horizon point meets the cones for *all* large `τ`), `hc_upper_limit` | **BUILT IN PART**. See the notes below the table. |
| 6c | `S_τ` accumulates on `𝓗⁺`: every point of `𝓗⁺` is approached by the slices of all late `τ`, and no point outside it is | `CauchyRepair.lean` (78) · `cr_slice_lower_limit`, `cr_slice_kuratowski`, `cr_causal_alignment` (future Cauchy), `cr_causal_alignment_gh` (P1's two-sided Cauchy). Non-vacuity: `SliceTangency.lean` (79) · `Model.st_model`, `Model.st_futCauchy`, `Model.GoodG.st_adapted` | **BUILT IN PART**. See the notes below the table. |
| 6d | Each finite-`Θ` slice lies entirely in `D`, and meets `𝓗⁺` only in the limit | `CausalStructure.lean` · `cs_slice_subset_D`, `cs_slice_subtype` (for any `Θ`, by the definition of the slice, as in P1), together with 6c's `KLi(S_τ) = 𝓗⁺` | **BUILT IN PART**. (chart). The limit half carries 6c's caveats. |
| 6e | Tangency, now conditional: if near `𝓗⁺` the rate of `Θ` along the generators stays bounded while its rate across them diverges, the tangent hyperplanes of `S_τ` become asymptotically tangent to the generators in direction | `SliceTangency.lean` (79) · `st_null_frame_bound`, `st_alignment_iff` (full alignment ⇔ `a/b → 0`; bounded `a` with `b → ∞` gives it), `st_frame_cone_model` (instantiates the hypotheses), `Model.st_aligned`. `Model.st_tangency_fails` shows the condition cannot be dropped, as P1 now says. | **BUILT IN PART**. See the notes below the table. |
| 6f | Consequently the event horizon occurs on no finite exterior slice, only as the null future boundary approached in the infinite-time limit (**the headline**) | Composition of 6d and 6c: `cs_slice_subset_D` together with `cr_causal_alignment[_gh]` | **BUILT IN PART**. (chart), with `hcl`, `hint`, `hHM` stated, and two-sided non-vacuity missing. |

Notes on 6b:
- (chart).
- `hcl` and `hint` are stated rather than derived.
- The convergence is Kuratowski, not uniform or Hausdorff on compacts. It is close to "within any distance", but it is not that sentence's form.
- "Monotonically" (from the proof) is not stated.
- Non-vacuity: 79's `st_model` proves `hOD`, `hmono`, `hcl`, `hint` in its own file. 72's definitions are the same C¹-chain ones, but the cross-file identity was certified by 71 only for 78/79.

Notes on 6c:
- (chart).
- `hcl`, `hint` and `hHM` are stated.
- The model witnesses only the future form. The two-sided `_gh` theorem has no witness: the model proves no past Cauchy property. The future-form theorem has a weaker hypothesis than P1's, so P1's clause *is* covered non-vacuously, through `cr_causal_alignment`.
- The model is 2D flat (Rindler), not a black hole.
- 74–75 are superseded.

Notes on 6e:
- The frame is given by its components, not built from a general `g` at horizon points.
- The model is 2D. `k` is abstract, but it is instantiated only at `k = 0`.
- Campaign 80, the frame-free statement and Kruskal, is not built.

## 7. `cor:densities`

| # | Clause | Lean | Mark |
|---|---|---|---|
| 7a | No finite exterior slice contains any part of the black-hole region | `CausalStructure.lean` · `cs_BH_inter_D`, `cs_BH_inter_slice`, `cs_BH_inter_slice_subtype` | **BUILT IN PART**. See the notes below the table. |
| 7b | …so none contains the horizon… | `CausalStructure.lean` · `cs_slice_subset_D` (`S_τ ∩ 𝓗⁺ = ∅`) | **BUILT IN PART**, (chart) only, as in 7a. |
| 7c | …or a curvature singularity the horizon encloses | — | **NOT BEGUN**. There is no notion of a singularity. It would follow at once from "singularity ⊆ BH", which is not stated. |
| 7d | On every finite slice the collapsing matter lies outside `𝓗⁺`, finite in extent, each element still approaching its horizon event | — | **NOT BEGUN**. There is no matter or collapse model. |
| 7e | The densities of the central singularity never form at any finite exterior time (Oppenheimer–Snyder) | — | **NOT BEGUN** |

Notes on 7a:
- The only gap is (chart).
- The theorem holds for *any* `Θ`, with no Cauchy or temporal hypothesis. So the `IsTemporal` vacuity does not touch it, and there is nothing to make vacuous.
- P1's proof is the same one-liner: a slice lies in `D`, which misses BH.

## 8. `lem:alignment` (Schwarzschild)

| # | Clause | Lean | Mark |
|---|---|---|---|
| 8i | (i) The cones miss `𝓗⁺` and climb its generators. `S_τ` accumulates on `𝓗⁺`, and in the angle-suppressed picture the cone hugs the generator | The general 6a–6c only | **BUILT IN PART**. Schwarzschild is never instantiated as a `Spacetime` with its `𝒥⁺`, and the radial-picture sentence is not formalised. |
| 8ii-a | (ii) For the stationary and retarded slicings, the tangent hyperplanes become tangent to the generator and `∇Θ` aligns | 79's reduction (`st_alignment_iff`), and its Rindler analogue of stationary time (`Model.st_aligned`, `Θ₀ = −log(−U)+V`) | **BUILT IN PART at best**. The Schwarzschild/Kruskal check is campaign 80 ②, which is registered but not built. |
| 8ii-b | Both slicings meet `𝓗⁺` only in the limit | — (only the general 6d) | **BUILT IN PART**. There is no Schwarzschild or collapse instance. Neither slicing is shown Cauchy temporal on `D`. |
| 8ii-c | Stationary: `g^{ab}∇_a t∇_b t = −(1−r_h/r)^{-1} → −∞`, and `N = √(1−r_h/r) → 0` | `SchwarzschildSlicing.lean` · `ss_static_inv_eq`, `ss_static_gtt`, `ss_static_gtt_tendsto`, `ss_static_gtt_matrix_tendsto`, `ss_lapse_tendsto`, `ss_lapse_sq`, `ss_lapse_rpow` | **BUILT**. It is the 4D static matrix, with `0 < r_h < r`. It needs `sin θ ≠ 0`: this is the coordinate chart off the poles, not a weakening of the scalar claim. |
| 8ii-d | Retarded: `Θ = a(u+ηr)` gives `g^{ab}∇Θ∇Θ → −2a²η`, which is finite | `SchwarzschildSlicing.lean` · `ss_ret_inv_eq`, `ss_ret4_inv_eq`, `ss_ret_norm`, `ss_ret4_norm`, `ss_ret_tendsto`, `ss_ret_at_horizon` (and `ss_ret_neg_nbhd`, timelike across `r_h`) | **BUILT**. Note: Lean computes in the eternal-Schwarzschild `(u,r,θ,φ)` metric. P1's collapse exterior is Schwarzschild near `𝓗⁺` (Birkhoff), so the norm limit is covered. |
| 8ii-e | The retarded slicing also accumulates on `𝓗⁺` in the exterior of a collapse | — | **NOT BEGUN** (there is no collapse exterior). |

---

## Summary of the marks

| Statement | BUILT | BUILT IN PART | NOT BEGUN |
|---|---|---|---|
| `thm:metric-singularity` | 1a | 1b | 1c |
| `cor:threefold` | — | iii, iv-a, iv-b | i, ii |
| EF corollary | — | 3a | 3b, 3c |
| `lem:killing` | — | 4a–4d | — |
| `cor:stationary` | — | 5 | — |
| `prop:causal-alignment` | — | 6a–6f (all at least (chart)) | — |
| `cor:densities` | — | 7a, 7b ((chart) only) | 7c, 7d, 7e |
| `lem:alignment` | ii-c, ii-d | i, ii-a, ii-b | ii-e |

If 69 accepts the single global chart as P1's working setting, these upgrade to BUILT:
- 7a and 7b;
- 6a, apart from its closedness hypothesis;
- 6c and 6d *as BUILT under stated consequences of P1's setting* (`hcl`, `hint`, `hHM`).

## The registered expectations

1. **`prop:causal-alignment`'s accumulation and finite-slice clauses come out BUILT, via 72 and 78–79.**
   - **It does not hold to the letter.** These clauses are 6b–6d. Their Lean is exactly 72, 78 and 79, as expected, but the registered rule marks a chart setting as BUILT IN PART.
   - Even if the chart is accepted, three items stand: `hcl`, `hint` and `hHM` are carried unproved (consequences of P1, not derived), 6a's closedness is a hypothesis, and the two-sided (`_gh`) form has no non-vacuity witness.
   - The *future*-Cauchy form is non-vacuous and weaker than P1's hypothesis.
   - **Verdict: holds only if the chart is accepted and stated consequences of P1 count as P1's hypotheses.**
2. **The tangency clause comes out BUILT IN PART until 80 lands.** **This holds.** It rests on 79's reduction, failure and model, with frame components, in 2D (6e, 8ii-a).
3. **`cor:densities` comes out NOT BEGUN.** **This fails.**
   - Its first clause, "no finite slice contains any part of the black-hole region, nor the horizon", is built: `cs_BH_inter_slice` and `cs_slice_subset_D` (campaign 60). It holds for any `Θ` and is untouched by the vacuity. Its only gap is (chart).
   - Only its physical clauses (7c–7e) are NOT BEGUN.
4. **At least one metric-singularity statement comes out BUILT IN PART on the 4D or angular reduction.** **This fails as worded.**
   - The metric-singularity statements are BUILT IN PART for other reasons:
     - a flat adapted frame (1b, 2iii–iv);
     - a global adapted chart, with the local-chart link missing (4, 5);
     - missing non-vacuity witnesses (4, 5);
     - no Schwarzschild instance (3).
   - None of these probes is reduced in dimension or in angle. `MetricSingularity` and `KillingHorizon` are `n`-dimensional.
   - The only angular restriction, `sin θ ≠ 0`, is in `lem:alignment` (ii), which is not a metric-singularity statement, and it is marked BUILT there.
   - It holds only if "a reduced setting" of any kind is read for "4D or angular".

**Count: 1 of 4 holds outright (2). 1 holds conditionally (1). 2 fail (3, 4). The joint p `0.6` did not come true.**

## The proposal: campaign 81, by the registered rule

***Which clause.*** The headline (6f) rests most directly on 6d and 6c: "each finite-`Θ` slice lies in `D`, meeting `𝓗⁺` only in the limit", with the slice limit `KLi(S_τ) = 𝓗⁺`.
- Tangency (6e, campaign 80) is not on the headline's path. P1's "Consequently" follows from the finite-slice clause, and tangency is now conditional.
- 6c and 6d have three gaps:
  - (chart);
  - `hcl`, `hint` and `hHM` stated;
  - no witness for the two-sided form.
- The tie-break goes to the smallest Lean cost.

***Proposed campaign 81: discharge the stated hypotheses of the headline theorem.***
- **Where.** In campaign 78's repaired setting, copied.
- **What to prove.**
  1. `hint`, i.e. `int J⁻(J) ⊆ I⁻(J)` for the C¹-chain relation. A short future `T`-step from `p` stays in the interior. Then the dual push-up `cs_pushup'` (campaign 60, locally Lipschitz `g`) gives `p ≪ a`.
  2. `hcl`, i.e. `J⁻(J) ⊆ closure I⁻(J)`. Take a short past `T`-step from `q`, then push-up, and let the step go to `0`. This needs `J ⊆ M`, or `J ∖ M ⊆ closure D`, which should be stated.
  3. Restate `cr_causal_alignment_gh` with `hcl` and `hint` removed, at the price of `LocallyLipschitz g`. P1's smooth `g` satisfies that, so it is not stronger.
  4. Give 79's model the past Cauchy property: `Θ_G → −∞` along past-inextendible curves of `D`. Then `cr_cauchy_iff` makes the two-sided theorem non-vacuous.
- **What stays.** `hHM : 𝓗⁺ ⊆ M` is P1's own setting, so it can stay as stated.
- **Expected size.** A few hundred new lines (push-up is roughly 200 lines to copy; the rest is short), against several thousand for the alternative.

***Why not the chart.*** The other gap in the same clause is lifting the causal chain to a Mathlib manifold. It is the larger gap, but much the costlier: it joins 66/68's manifold layer to 60–79's causal layer. It should be named as the remaining gap after 81, not taken first.

***Why it is honest.***
- After 81, the headline theorem's hypothesis list would be exactly P1's: GH of `D` as two-sided Cauchy, `I⁻(O) = D`, a worldline, `Θ` adapted, plus `𝓗⁺ ⊆ M` and Lipschitz `g`. The single chart would be the only gap.
- The headline theorem would have a two-sided non-vacuity witness.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

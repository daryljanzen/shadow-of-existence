# Inventory of P1 (`corpus/BH_causality_v2.tex`) against the Lean probes: refresh under `r7667+71.1` ②

*A reading, done by the method of `r7643_71_inventory/PREDICTION.md`, which is unchanged. P1 is read as it stands at
`5dac5ff9` (r7667), so `rem:formalised` and the amended proof of `prop:causal-alignment` are included. The probes are
read through campaign 92. `GeneratorStretch.lean` (campaign 93 ①(a), in progress) is not counted. Every theorem name
below was checked by grepping its probe for the declaration. The previous inventory is
`r7643_71_inventory/INVENTORY.md`, written before campaign 80.*

**The marking rule (unchanged).**
- **BUILT**: the Lean covers the clause under hypotheses no stronger than P1's, and is non-vacuous.
- **BUILT IN PART**: the gap is named. It is a stronger hypothesis, a reduced setting (a chart, 2D), or a missing
  non-vacuity witness.
- **NOT BEGUN**.

A row whose mark moved since r7643 is tagged **⇧ moved**. A row whose mark stayed but whose gap changed is tagged
*(gap narrowed)*.

## The population

The grep for `\begin{theorem|proposition|lemma|corollary}` still finds the same **8**:
- `thm:metric-singularity` (l.130);
- `cor:threefold` (l.166);
- the EF-degeneracy corollary (l.220, unlabelled);
- `lem:killing` (l.267);
- `cor:stationary` (l.281);
- `prop:causal-alignment` (l.300);
- `cor:densities` (l.318);
- `lem:alignment` (l.336).

The remarks are unchanged apart from one addition:
- **new:** `rem:formalised` (l.308) states the Lean form of `prop:causal-alignment`. It makes no claim that a proof
  uses, but it makes claims about the Lean, and those are checked in §6;
- the remark after the theorem (the along-the-connection form) is covered in §1;
- `rem:PG-forcing` and `rem:penetrating` are interpretive and not formalised.

## The setting, read once (what changed)

***The single chart is gone for the causal layer.*** Campaigns 84–92 restate the whole causal chain on a Mathlib
manifold `N`, as `MSpacetime E N`.
- **What `N` needs:** it is Hausdorff (`[T2Space N]`), has a `C¹` atlas, and is modelled on any real normed space.
  `LocallyOneChart` says that `g` is `C¹` and `T` continuous in charts.
- **Witnesses:** `CylinderWitness.lean` is a witness that no single chart covers (`cy_chart_ne_univ`).
- **`𝒥⁺`:** it sits in a `ConformalExtension` (`ConeDisjoint.lean` l.5023: an open `C¹` embedding `ι`, `Ω > 0`,
  `ι*g̃ = Ω²g`, the time orientation preserved).

***The stated consequences are now derived.***
- **`hcl` and `hint`:** on `N` they are `mh_hcl` and `mh_hint`.
- **Closedness:** the earlier `IsClosed J⁻(O τ)` hypothesis is gone (`cd_cone_disjoint`).
- **What stays:**
  - `J ⊆ M`, which P1 supplies as `J = range O`;
  - `𝓗⁺ ⊆ M` and `𝒥⁺ ⊆ M̃₀`, which are P1's own setting.

  `rem:formalised` states all three.

***The two-sided Cauchy property is witnessed.*** It was the last vacuity worry.
- The first witness is campaign 81's `hl_model_headline`.
- It is carried to `N` by `mh_witness_hypotheses`, `cy_witness_headline`, `fd_witness_headline` and
  `ww_witness_headline`.

***The non-causal statements did not move.*** `thm:metric-singularity`, `lem:killing` and the EF corollary have no
manifold or causal-layer link yet.

---

## 1. `thm:metric-singularity`

**1a.** (a) `Δs² = 0` and (b) `Δx = 0` give `Δτ = 0`, through `Δs² = Δx² − Δτ²` on the invariant separations.
- **Lean:** `MetricSingularity.lean` · `ms_metric_singularity_scalar`, `ms_metric_singularity_vec`.
- **Mark: BUILT** (unchanged). The relation is a hypothesis, as it is in P1's proof.

**1b.** The along-the-connection form: (b) holds at every point of the null geodesic, so the finite `Δτ` vanishes.
- **Lean:** `MetricSingularity.lean` · `ms_metric_singularity_along`.
- **Mark: BUILT IN PART** (unchanged). The gap is a flat adapted frame `‖x′‖² − τ′²` along the curve. There is no
  general `g`, no foliation and no invariant spatial coordinate.
- ***Reading flag, new in this refresh.*** The hypotheses `x′ ≡ 0` and `‖x′‖² − τ′² ≡ 0` force `τ′ ≡ 0`. So `(τ, x)` is
  constant on `[0,1]`.
  - **If `(τ′, x′)` are the components of `γ̇` in a frame** (a basis), then `γ̇ ≡ 0` and `p = q`.
  - **So no witness with `p ≠ q` exists in this form.** It is not inconsistent, but it can only be witnessed trivially.
  - **What a `p ≠ q` instance needs** is a *degenerate* adapted frame: the line of constant spatial coordinate is null,
    `g_λλ = 0`, as on the horizon (`ef_horizon_degenerate`, `kh_forcing`). See "Cheapest next row" (i).

**1c.** "…metrically coincident…while remaining topologically distinct and causally ordered".
- **Lean:** none for the theorem.
- **Mark: NOT BEGUN** (unchanged). The Killing witness does exhibit a concrete distinct pair (`kw_coincident_concrete`,
  `(0,0) ≠ (1,0)`), but no causal order is stated.

## 2. `cor:threefold`

P1's hypotheses: `γ` is a future null geodesic from `p` to `q`, with `q ∈ ∂J⁺(p)`.

**2i.** `p ≠ q`, so they are topologically distinguishable.
- **Mark: NOT BEGUN** (unchanged). It is trivial in a Hausdorff space.

**2ii.** The strict null ordering `p ≺_∂ q`.
- **Lean:** for a point `p`, nothing. Only the `∂J⁻(A)` pieces exist: `ct_H_achronal`, `cg_generator`,
  `gr_generator_null_ae`, and `lb_H_generator_null_geodesic`.
- **Mark: NOT BEGUN** (unchanged).

**2iii.** `g(γ̇, γ̇) = 0` along the whole segment.
- **Lean, flat:** `MetricSingularity.lean` · `ms_threefold_iii`, `ms_threefold_iii_of_b`.
- **Lean, general `C²` `g`, one chart:** `LipschitzBootstrap.lean` (campaign 77) · `lb_energy_cons` (`g(u,u)` is
  constant along the Levi-Civita geodesic flow, with `Γ` derived by Koszul), `lb_generator_null_geodesic`.
- **Lean, a manifold with a hypothesised connection:** `GeodesicProbe.lean` · `IsGeodesicAt`, `IsNullAt`,
  `covDerivAlong_compat_hasDerivAt`.
- **Mark: BUILT IN PART** *(gap narrowed, by a re-read rather than a new campaign)*.
  - The r7643 inventory cited only the flat form. `lb_energy_cons` predates r7643 and was missed there.
  - **The gap now:** it holds in one chart, and only for geodesics of a local flow box (`Icc (-τ) τ`). It is not stated
    for an arbitrary null geodesic segment, and not on `N`.

**2iv-a.** Under (b), the pair is metrically coincident.
- **Lean:** `ms_metric_singularity_along`.
- **Mark: BUILT IN PART** (unchanged). It has the same gap as 1b, and the same reading flag.

**2iv-b.** Without (b), `τ(q) − τ(p)` has no invariant meaning: a smooth local deformation changes it.
- **Lean:** `ms_threefold_iv_noninvariance`.
- **Mark: BUILT IN PART** (unchanged). Three gaps:
  - it is stated in flat `ℝ^{n+1}`;
  - "temporal" is the surrogate `∂_t τ ≥ c`, not `dτ > 0` on the Lorentzian cone;
  - the support is a ball about `q`.

## 3. The EF-degeneracy corollary (l.220)

**3a.** Horizon events `p` and `q` on one generator lie on distinct points of `∂J⁻` (the observer's whole worldline).
They are causally ordered but null-related.
- **Lean:** in general only. In one chart, `hc_H_eq_closure_diff`. **Now also on `N`:** `mx_frontier_JpastSet`
  (`∂J⁻(A) = closure I⁻(A) ∖ I⁻(A)`) and `mx_H_eq_boundary`.
- **Mark: BUILT IN PART** *(gap narrowed)*. It is now general on `N`. Still missing: a Schwarzschild/EF instance, and
  any order statement for `p` and `q`.

**3b.** Both are at `r = r_h`, so (b) holds and they are metrically coincident.
- **Lean:** the pieces only. `NoConnectionSweep.lean` · `schw_charts`, `ef_det`, `ef_horizon_degenerate`. Plus the
  `ms_*` theorems.
- **Mark: NOT BEGUN** (unchanged). Nothing combines the pieces.

**3c.** The vertical extent encodes only causal order.
- **Mark: NOT BEGUN** (unchanged). It is interpretive.

## 4. `lem:killing`

**4a.** Away from a bifurcation surface there are adapted coordinates with `χ = ∂_λ` and `g` independent of `λ`.
- **Lean:**
  - `FlowC1.lean` · `fc_flowBox_killing`;
  - `FlowManifold.lean` · `fm_manifold_killingChart_section`;
  - `LieDerivManifold.lean` · `ld_manifold_killingChart_lieDeriv` (`L_X g = 0` near `p`, with `X p ≠ 0`, gives a
    `LocalKillingChart`), `LocalKillingChart.ld_metric_N`, `ld_lieDeriv_chart`.
- **Mark: BUILT IN PART** (unchanged).
  - It needs a `C²` manifold.
  - `g`'s differentiability is in chart form.
  - *New note (campaign 83):* `LocalKillingChart` has no nondegeneracy field, and nothing in either file assumes it of
    `g`.

**4b.** (a): along the generator `ds² = |χ|² dλ²`, so null with `dλ ≠ 0` forces `|χ|² = 0`.
- **Lean:** `KillingHorizon.lean` · `kh_interval_orbit`, `kh_forcing`, `kh_null_along_generator`.
- **Mark: BUILT IN PART** (unchanged). It is stated only in the global `KillingChart` on `ℝ × E`. A grep finds no
  `MetricallyCoincident` and no `kh_` in `FlowManifold.lean` or `LieDerivManifold.lean`.

**4c.** (b): the flow is an isometry, mapping each generator into itself, so the transverse invariants are equal at
`p`, at `q` and between them.
- **Lean:** `kh_flow_isometry`, `kh_flow_pullback`, `kh_transverse_invariant`, `kh_transverse_invariant_between`.
  Locally on `E`: `fm_flow_isometry_loc`.
- **Mark: BUILT IN PART** (unchanged). It has the same split as 4b.

**4d.** `p` and `q` are metrically coincident, and `𝒦` is a metric singularity.
- **Lean:**
  - `kh_lemma_killing` (structure `MetricallyCoincident`);
  - **witness:** `KillingWitness.lean` · `kw_lemma_killing_witness`, `kw_coincident_concrete`, `kw_lorentzian`,
    `kw_zero_excluded`;
  - `KillingChart.nondeg` (campaign 83).
- **Mark: BUILT IN PART** *(gap narrowed)*.
  - **"No non-vacuity witness" is now false.** Campaign 82 built Minkowski 1+1 in light-cone form, `ds² = 2 dλ dx`,
    with `χ = ∂_λ` a null translation. It is shown Lorentzian (`det = −1`, signature `(−,+)`).
  - Campaign 83 added `nondeg`, so the zero metric is excluded (`kw_zero_excluded`). `kh_lemma_killing` re-checks
    unchanged.
  - The witness instantiates `kw_lemma_killing`, a verbatim `kw_`-prefixed copy of `kh_lemma_killing`, with the same
    textual-identity caveat as every copied probe.
  - **The remaining gap is only the global `KillingChart`.** No theorem takes a `LocalKillingChart` (or `L_X g = 0` on
    `N`) to `MetricallyCoincident`.

## 5. `cor:stationary`

**5.** The event horizon of a stationary black hole is a metric singularity, by rigidity.
- **Lean:** `kh_cor_stationary` under `Rigidity n H`. **Witness:** `kw_cor_stationary_witness`, `kw_rigidity`.
- **Mark: BUILT IN PART** *(gap narrowed)*.
  - The witness now exists, on the null line `kw_H`.
  - Rigidity is still a hypothesis, which is no stronger than P1, since P1 cites it too.
  - Still open: "Killing horizon" is encoded as one global adapted chart, and "stationary black hole" and "event
    horizon" are not defined in the probe.

## 6. `prop:causal-alignment`

***The theorem.*** `ConeDisjoint.lean` · `MSpacetime.cd_prop_causal_alignment`, which has eight conjuncts. It extends
`ConformalBoundary.lean` · `mx_prop_causal_alignment`, which has seven. The identification is `mx_H_eq_boundary`.

***Its hypotheses against P1's.***

| Lean | P1 |
|---|---|
| `[T2Space N]`, `LocallyOneChart` for `S` and `S̃` | weaker: P1 is smooth and Hausdorff |
| `X : ConformalExtension S St`, `𝒥 ⊆ St.M` | P1's `𝒥⁺` in a conformal completion |
| `hOD`, `hmono`, `hI : I⁻(O) = ι⁻¹I⁻(𝒥⁺)` | `I⁻(O) = D = I⁻(𝒥⁺)`, and `O` a worldline |
| `hJM : J ⊆ M`, `hHM : ∂J⁻(𝒥⁺) ⊆ M` | P1's setting (`J = range O`) |
| `IsCauchyTemporalOn (D J) Θ`, `hadapt` | P1's premise. Bernal–Sánchez is not included, as `rem:formalised` says |

Not used, and so more general than P1: asymptotic flatness, future-completeness, `O(τ) → i⁺`, and smoothness beyond `C¹`.

***Witnesses*** (the six families of `rem:formalised`):
- `mx_witness_headline`, `cd_witness` and `mc_witness_tangency_fails` (`Pt`);
- `cz_witness_headline` and `cz_witness_headline_F` (`Compactification.lean`);
- `ct_witness_tangency_F` and `ct_expV_differs` (`CurvedTangency.lean`);
- `cy_witness_headline` and `cy_witness_tangency` (3D, multi-chart);
- `fd_witness_headline` and `fd_witness_tangency` (4D);
- `ww_witness_headline`, `ww_witness_tangency` and `ww_cotton_ne_zero` (3D, not conformally flat).

The `∂J⁻(𝒥⁺)` identification is witnessed in 2D only, as the remark says.

### The clauses

**6a.** No past light cone `∂J⁻(O(τ))` meets `𝓗⁺`.
- **Lean:** `cd_cone_disjoint`, and the stronger `cd_closure_Jpast_inter_H`. This is the eighth conjunct.
  **Witness:** `cd_witness`, in which every cone is non-empty.
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). The chart is gone, and so is the closedness hypothesis.
  - *Note, as `rem:formalised` says:* the proof goes through the Cauchy property of `Θ`, not the bare openness of `D`.

**6b-i.** The cones converge to `𝓗⁺`, and the stretch they approach to within any given distance extends without
bound.
- **Lean:**
  - `ManifoldCones.lean` · `mc_cone_kuratowski_N` (Kuratowski), also conjuncts 5–6 of `cd_prop_causal_alignment`;
  - `HorizonStretch.lean` · `hs_stretch_N`, `hs_uniform_on_compact`, `hs_unbounded`, for any metric that induces
    `N`'s topology;
  - **witness:** `hs_witness`, `mc_witness_cones`.
- **Mark: BUILT ⇧ moved** (from BUILT IN PART, as part of the old 6b).

**6b-ii.** …"to the future" along the generators, and (from the proof) "monotonically".
- **Lean:** on the 4D witness only, `hs_witness` (the stretch reaches every `V`) and `hs_generator_subset`.
  Campaign 93 ①(a) is in progress and not counted.
- **Mark: BUILT IN PART** (the old 6b, split).
  - The general statement needs future-inextendible generators, the achronal-boundary theorem on `N`, which campaign 93
    ①(b) priced and did not build.
  - "Monotonically" is not stated.

**6c.** The slices `S_τ` accumulate on `𝓗⁺`: every horizon point is approached by all late slices, and no other point
is.
- **Lean:** `mh_causal_alignment_gh_N`, `mh_slice_kuratowski`, and conjuncts 3–4 of `cd_prop_causal_alignment`.
- **Mark: BUILT ⇧ moved.**
  - The chart is gone.
  - `hcl` and `hint` are derived.
  - The two-sided Cauchy property is witnessed (`mh_witness_hypotheses`, and the 3D/4D witnesses prove it on `N`).

**6d.** Each finite-`Θ` slice lies in `D` and meets `𝓗⁺` only in the limit.
- **Lean:**
  - `slice J Θ τ ⊆ D J` holds by definition;
  - `mh_not_mem_D_of_H` gives `𝓗⁺ ∩ D = ∅` on `N`;
  - `SublevelProper` (`mh_sublevelProper`, conjunct 2) gives that `closure {Θ ≤ T} ⊆ D`;
  - the limit half is 6c.
- **Mark: BUILT ⇧ moved.**

**6e.** Tangency, conditional: if near `𝓗⁺` the rate of `Θ` along the generators stays bounded while its rate across
diverges, the tangent hyperplanes of `S_τ` become tangent to the generators in direction.
- **Lean:**
  - frame-free, in `TangencyCondition.lean` (campaign 80): `tc_pointwise`, `tc_tendsto`, `tc_tendsto_limit`;
  - on `N`: `mc_tangency_N`, `mc_tangency_at_N`, `mc_chart_change`, and conjunct 7;
  - witnesses holding: `mc_witness_tangency_holds`, `ct_witness_tangency_F`, `cy_`/`fd_`/`ww_witness_tangency`;
  - witness failing: `mc_witness_tangency_fails`.
- **Mark: BUILT ⇧ moved.** It is on the manifold, in any dimension, and witnessed curved (`ct_expV_differs`) and not
  conformally flat (`ww_`). Three reading notes:
  - Lean's rate hypothesis, `dΘ(ℓ)/dΘ(n) → 0`, is *weaker* than P1's "bounded along, divergent across".
  - Lean adds frame regularity: `ℓ → ℓ₀`, `‖n‖` bounded in the chart at `q`, and `FrameHyp`. That is what P1's proof
    means by "a null frame near a horizon point", and `rem:formalised` states it.
  - Lean does not identify `ℓ₀` with the generator's tangent, because generators are not formalised in general. The
    conclusion holds for any such `ℓ₀`, so it covers P1's choice. On every witness `ℓ = ∂_V` is the generator.
  - The convergence is stated in chart components with the transformation law, which is standard.

**6f.** The headline: the event horizon occurs on no finite exterior slice, only as the null boundary approached in the
infinite-time limit.
- **Lean:** `cd_prop_causal_alignment` (conjuncts 1–4), with `𝓗⁺ = ∂J⁻(𝒥⁺)` derived (`mx_H_eq_boundary`).
- **Mark: BUILT ⇧ moved.** Every r7643 gap is closed: the chart, `hcl`/`hint`/closedness, and the two-sided witness.

***`rem:formalised` against the Lean.***
- Its theorem names, file names, hypothesis list and "no conformal extension for the three" all match the greps.
- The one clause it says is outside the formal statement (the futureward stretch) is 6b-ii.

## 7. `cor:densities`

**7a.** No finite exterior slice contains any part of the black-hole region `M ∖ J⁻(𝒥⁺)`.
- **Lean:** in one chart only, `CausalStructure.lean` · `cs_BH_inter_D`, `cs_BH_inter_slice`,
  `cs_BH_inter_slice_subtype`.
- **Mark: BUILT IN PART** (unchanged). The gap is (chart): a grep finds no `BH` definition on `N`.
- **Every ingredient for `N` exists:**
  - `D_subset_JpastSet` (`IpastSet ⊆ JpastSet`, on `N`, so also on `S̃`);
  - `hI`;
  - `slice ⊆ D`.

  See "Cheapest next row".

**7b.** …so none contains the horizon.
- **Lean:** on `N`, `mh_not_mem_D_of_H` with `slice ⊆ D`. As `∂J⁻(𝒥⁺)`, it is conjunct 1 with conjunct 2
  (properness), which `rem:formalised` calls "the second conclusion". Witnesses: as §6.
- **Mark: BUILT ⇧ moved** (from (chart)).

**7c.** …or a curvature singularity the horizon encloses.
- **Mark: NOT BEGUN** (unchanged). There is no notion of a singularity. If "enclosed" is read as "lies in the BH
  region", 7c is 7a applied to a subset.

**7d.** On every finite slice the collapsing matter lies outside `𝓗⁺`.
- **Mark: NOT BEGUN** (unchanged). There is no matter model.

**7e.** The densities of the central singularity never form at any finite exterior time.
- **Mark: NOT BEGUN** (unchanged).

## 8. `lem:alignment` (Schwarzschild)

**8i.** The cones miss `𝓗⁺` and climb its generators, and `S_τ` accumulates. In the angle-suppressed picture the cone
hugs the generator.
- **Lean:** the general §6 only.
- **Mark: BUILT IN PART** (unchanged). Schwarzschild is never an `MSpacetime`.
  - `cz_witness_headline_F` covers `−F dU dV` for any positive `C¹` `F` on **all of** `ℝ²`.
  - Kruskal's `F` is defined only on `UV < 1`, so it is not an instance as it stands. Its docstring says so.

**8ii-a.** For the stationary and retarded slicings, the tangent hyperplanes become tangent to the generator.
- **Lean:** `TangencyCondition.lean` (campaign 80) · `tc_kruskal_align`, `tc_kruskal_limit`, `tc_stationary`,
  `tc_retarded` (the genuine inverse `r(U,V)`, `tc_rK_partials`), and `tc_schwarzschild` (the actual
  `F = (32M³/r)e^{−r/2M}`).
- **Mark: BUILT IN PART** *(gap narrowed)*. At r7643 this was "campaign 80 not built". It is now built in the **radial
  Kruskal plane**. The remaining gaps:
  - 4D with the angles (campaign 80 ④ REPORTED);
  - `−F dU dV` is taken as the radial metric, not derived from the `(t,r)` form.

**8ii-b.** Both slicings meet `𝓗⁺` only in the limit.
- **Lean:** the general 6d.
- **Mark: BUILT IN PART** (unchanged). There is no Schwarzschild instance, and neither slicing is shown Cauchy on `D`.

**8ii-c.** Stationary: `g^{ab}∇_a t ∇_b t → −∞`, and `N → 0`.
- **Lean:** `SchwarzschildSlicing.lean` · `ss_static_inv_eq`, `ss_static_gtt_tendsto`, `ss_lapse_tendsto`, and others.
- **Mark: BUILT** (unchanged).

**8ii-d.** Retarded: `g^{ab}∇Θ∇Θ → −2a²η`.
- **Lean:** `ss_ret_inv_eq`, `ss_ret4_norm`, `ss_ret_tendsto`, `ss_ret_at_horizon`.
- **Mark: BUILT** (unchanged).

**8ii-e.** The retarded slicing accumulates in a collapse exterior.
- **Mark: NOT BEGUN** (unchanged).

---

## Summary of the marks

| Statement | BUILT | BUILT IN PART | NOT BEGUN |
|---|---|---|---|
| `thm:metric-singularity` | 1a | 1b | 1c |
| `cor:threefold` | — | iii, iv-a, iv-b | i, ii |
| EF corollary | — | 3a | 3b, 3c |
| `lem:killing` | — | 4a–4d | — |
| `cor:stationary` | — | 5 | — |
| `prop:causal-alignment` | **6a, 6b-i, 6c, 6d, 6e, 6f** | 6b-ii | — |
| `cor:densities` | **7b** | 7a | 7c, 7d, 7e |
| `lem:alignment` | ii-c, ii-d | i, ii-a, ii-b | ii-e |

***Mark moves since r7643 (all upward, none downward).***

| Row | Moved to | Campaign(s) |
|---|---|---|
| 6a | BUILT | 91 (`cd_cone_disjoint`, with no closedness hypothesis) |
| 6b-i | BUILT | 88, 92 |
| 6c, 6d, 6f | BUILT | 81 (`hcl`/`hint`, two-sided model), 84–87 (manifold), 89 (`∂J⁻(𝒥⁺)`) |
| 6e | BUILT | 80, 88, 91 |
| 7b | BUILT | 87 (`mh_not_mem_D_of_H`), 89 |

*Gaps narrowed without a mark move:* 2iii (a re-read: `lb_energy_cons`), 3a, 4d, 5, 8ii-a.

*Split:* the old 6b is now 6b-i (BUILT) and 6b-ii (BUILT IN PART).

***Campaign 93's registered expectations for this refresh.***
- *"`prop:causal-alignment` moves to BUILT, with the gaps the remark states":* **this holds**, apart from 6b-ii, which
  is the gap the remark states.
- *"4d's 'no witness' is outdated, and the remaining gap is the `LocalKillingChart` link":* **this holds.**

---

## Cheapest next row

These are the BUILT IN PART rows outside `prop:causal-alignment`, ranked by the estimated cost to **BUILT**. The cost is
new lines; the copied base is not counted.

| Rank | Row(s) | Cost to BUILT | p | Blocker |
|---|---|---|---|---|
| 1 | **7a** on `N` | ~60–100 | 0.9 | none |
| 2 | **2iii** on `N`, any null geodesic segment | ~250–400 | 0.65 | "geodesic on `N`" is chart-wise, since the probes have no Levi-Civita connection on `N` |
| 3 | **4b–4d** (and then 5) via `LocalKillingChart` | stage 1 ~300–450 (one flow box, still IN PART); to BUILT ~900–1300 | 0.75 / 0.35 | chaining flow boxes along a whole generator |
| 4 | **1b, 2iv-a** for general `g` | ~200–300 *after* a reading decision | 0.6 | what `Δτ` means for a general `g` (the flag in 1b) |
| 5 | 8i, 8ii-b on Kruskal `{UV<1}` | ~800–1500 | 0.4 | a Cauchy proof on a non-whole-plane `M`. `cz_scale` gives conformal invariance of the causal layer, which helps |
| 6 | 3a/3b EF instance | ~1500+ | 0.3 | 4D Schwarzschild as an `MSpacetime` |

### (i) `thm:metric-singularity`'s along-the-connection form (1b, 2iii, 2iv)

***What the probes carry.***
- **`MetricSingularity.lean`:** flat-frame algebra only. By the 1b flag, its along form cannot witness `p ≠ q`.
- **`LipschitzBootstrap.lean`:**
  - in one chart, a general `C²` `g`, with `Γ` from Koszul (`lb_christoffel_koszul`);
  - the geodesic flow `GeoFlow`, with `lb_geoFlow_exists`;
  - **energy conservation `lb_energy_cons`**;
  - `lb_generator_null_geodesic`: the generators of `𝓗⁺` are null geodesics, in a normal chart.
- **`GeodesicProbe.lean`:**
  - on a manifold, `IsGeodesicAt` and `IsNullAt`, with any torsion-free compatible connection taken as a hypothesis;
  - `covDerivAlong_compat_hasDerivAt`;
  - there is no existence theorem for Levi-Civita.
- **`GeodesicExistProbe.lean`:** local existence, on the model space only.

***What a general-Lorentzian-`g` version needs.***
- **For 2iii.** It is only "null at one point and geodesic ⇒ null throughout". In one chart, it is `lb_energy_cons`'s
  derivative computation applied to any `C²` solution of `γ'' = −Γ(γ', γ')` on `[0,1]`, rather than the flow's: about
  60 lines.
  - That would still be (chart).
  - BUILT needs it on `N`, by one of two routes:
    - a geodesic defined chart-wise (in each chart, the representative solves `hRep g`'s geodesic equation); the energy
      `g(γ̇,γ̇)` is chart-invariant, so it is locally constant, and so constant on `[0,1]`;
    - or `GeodesicProbe`'s connection-as-hypothesis form. But a hypothesised connection is a stated consequence of
      P1's setting, which under the rule is BUILT IN PART.
  - Cost about 250–400 lines.
- **For 1b and 2iv-a.** These need P1's `Δτ` defined for a general `g`.
  - The statement that is not vacuous: an invariant spatial coordinate `σ` (a `C¹` submersion near `γ`) is constant
    along the null curve `γ`. Then `γ̇ ∈ ker dσ = span ∂_λ`, null with `λ′ ≠ 0` forces `g(∂_λ,∂_λ) = 0` along `γ`, so
    `Δτ := ∫ √|g_λλ| |λ′| = 0`, while `Δλ ≠ 0` keeps `p ≠ q`.
  - That is `kh_forcing` without `λ`-independence, about 200–300 lines in one chart. A geodesic is not needed: any
    null curve works.
  - **But it should go to 69 first.** Under a *nondegenerate* adapted frame the form is vacuous for `p ≠ q`. Under the
    degenerate one, `Δτ` is the proper length of a null curve, zero without (b). So which `Δτ` P1 means decides
    whether (b) carries the conclusion. That is a reading question on P1, not a Lean one.

### (ii) `lem:killing` 4b–4d: from `LocalKillingChart` to `kh_lemma_killing`

***What exists.***
- **`ld_manifold_killingChart_lieDeriv`:** from `L_X g = 0` near `p`, `X` a `C¹` section and `X p ≠ 0`, it gives a
  `LocalKillingChart X p (hRep g p)`. That chart has:
  - `Φ : ℝ × H ⇀ E`;
  - `straightens`, `Dψ(1,0) = X`, with `ψ = φ⁻¹ ∘ Φ`;
  - `metric_eq`, with components `gH h` depending on `h` only.
- **`ld_metric_N`:** it reads those components as `g` on `N`.
- **`kh_lemma_killing`:** it concludes `MetricallyCoincident`, but only for the global `KillingChart` on `ℝ × E`.
  `KillingChart` needs `λ`-translation invariance for all `s`, and `nondeg` at every point of `ℝ × E`.
  - **So `LocalKillingChart` cannot simply be repackaged as a `KillingChart`.** `gH h` is meaningful only for `h` near
    `0`, so `nondeg` fails off the chart, and `Φ.source` is not `ℝ × H`.
  - **The link is a local restatement, not a coercion.**

***Does `KillingWitness.lean` supply the non-vacuity witness?***
- **For the global-chart lemma, yes.** `kw_lemma_killing_witness` and `kw_cor_stationary_witness` are Lorentzian, and
  `nondeg` holds.
- **For a manifold-layer lemma, no.** It instantiates a `KillingChart`, not `L_X g = 0` on `N`. A new witness is
  needed: on the model space `ℝ²`, the constant `g = 2 dλ dx` (`kw_lightCone`) and the constant null `X = (1,0)`.
  `lieDeriv X g = 0` comes through `ld_lieDeriv_chart_self`, where every term vanishes for constant fields. That is
  about 100–150 lines.

***Cost to BUILT.***
- **Stage 1, one flow box:** `p` and `q` are `ψ(a,0)` and `ψ(b,0)`, with the segment in `Φ.source`. Cost about 300–450
  lines, p 0.75.
  - (a) `g(X,X) = 0` along the segment, by `metric_eq` and `straightens`.
  - (b) the transverse components `g(Dψ(0,u), Dψ(0,u′))` are constant in `t`.
  - `Δx = 0` (equal `h`), `Δτ = 0`, and `p ≠ q` (injectivity of `ψ`).
  - The mark stays BUILT IN PART, but the gap becomes "one flow box", which is P1's own proof's "near the generator
    there are adapted coordinates".
- **Stage 2, a whole generator segment:**
  - (a) globally: `X(g(X,X)) = (L_X g)(X,X) = 0` along an integral curve (`lieDerivForm` with `V = W = X`, and
    `ld_lieDerivForm_eq_lieDeriv`). About 150 lines.
  - (b) by chaining flow boxes over a compact parameter interval (a Lebesgue number), composing the transverse
    isometries. About 500–800 lines.
  - Total to BUILT: about 900–1300 lines, p 0.35.

### Recommendation

**Recommended: 7a on `N`.** It is the cheapest row to BUILT by a wide margin, and it sits on the headline's own
corollary. Every ingredient is already in `ConeDisjoint.lean`. The statement to build, in a copy of
`ConeDisjoint.lean`:

```lean
/-- `cor:densities`, first clause, on `N`: the black-hole region `M ∖ ι⁻¹ J⁻(𝒥⁺)` meets no slice. -/
theorem MSpacetime.dn_BH_inter_slice {S : MSpacetime E N} {St : MSpacetime E Ñ}
    (X : ConformalExtension S St) {𝒥 : Set Ñ} {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) (Θ : N → ℝ) (τ : ℝ) :
    (S.M \ X.ι ⁻¹' St.JpastSet 𝒥) ∩ S.slice J Θ τ = ∅
```

***How it goes.***
- **The proof:** `slice ⊆ D J = I⁻(range O) = ι⁻¹ I⁻(𝒥) ⊆ ι⁻¹ J⁻(𝒥)`, by `St.D_subset_JpastSet 𝒥`. It needs no
  Cauchy hypothesis, as in P1's one-line proof.
- **A companion:** `dn_densities` bundles it with 7b (`slice ∩ ∂J⁻(𝒥⁺) = ∅`, from `mx_H_eq_boundary` and
  `mh_not_mem_D_of_H`). Add the 7c reading as a corollary: any `Σ ⊆` BH meets no slice.
- **The witness:** on campaign 90's compactified `Pt`, the BH region should come out as `{U ≥ 0}` (expected, not yet
  computed). It is non-empty, and the slices are non-empty.
- **Estimate:** about 60–100 new lines, p 0.9. 7a moves to BUILT, and 7c to BUILT IN PART under the stated reading.

***If 69 wants a substantive, non-definitional row instead.***
- **Take (ii) stage 1, not (i).** (i)'s 1b/2iv-a are blocked on a reading of P1's `Δτ`, which should go to 69 first.
  2iii alone is cheap but stays (chart) unless "geodesic on `N`" is built.
- **The stage-1 statement**, in a copy of `LieDerivManifold.lean`:

  ```lean
  theorem lk_lemma_killing_local (X) (p : N) (g) (hX hXp hg hK)   -- ld_manifold_killingChart_lieDeriv's hypotheses
      (hnull : g p (X p) (X p) = 0) :
      ∃ K : LocalKillingChart X p (hRep g p), ∃ ε > 0, ∀ a b, |a| < ε → |b| < ε →
        LocalMetricallyCoincident K (0 : K.H) a b
  ```

  - `LocalMetricallyCoincident` has five fields:
    - (a) `g(X,X) = 0` at `ψ(t,0)` for `t ∈ [a,b]`;
    - (b) `g(Dψ(0,u), Dψ(0,u′))` at `ψ(t,0)` equals its value at `ψ(a,0)`;
    - `Δx = 0`;
    - `Δτ = 0`;
    - `a ≠ b → ψ(a,0) ≠ ψ(b,0)`.
  - The Minkowski witness above goes with it.
  - **Estimate:** about 300–450 new lines (on about 2100 copied), p 0.75.
  - 4b–4d stay BUILT IN PART, with the gap narrowed to "one flow box". Stage 2 is the follow-on.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

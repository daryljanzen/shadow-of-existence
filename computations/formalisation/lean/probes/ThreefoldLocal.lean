import Mathlib

/-!
# Probe `r7695+71.1` (campaign 109): `cor:threefold` (iv), 2iv-b on `N` — the temporal separation `τ(q) − τ(p)` is not fixed by the geometry

Registration: `computations/formalisation/r7695_71_campaign109/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. It starts as a copy of campaign 104's
`probes/ThreefoldDistinct.lean` (namespace renamed `ShadowProbe.ThreefoldLocalProbe`, all old names
kept); everything new has the prefix `tl_` and is in the last section before the axiom prints.

Standing hypotheses of the new `N` theorems, beyond the kit's: `[FiniteDimensional ℝ E]` (the unit
sphere is compact, and Mathlib's `ContDiffBump` exists on `E`), `[T2Space N]` (the pulled-back bump's
support is closed, so the bump is smooth across the chart boundary), `S.LocallyOneChart`, and
`U ⊆ M`. Norms of tangent vectors are taken in the preferred chart at `q`: `‖Dφ_q(x) v‖ = ‖dchart q x v‖`.

* **① `MSpacetime.tl_cone_pos` (the registered stop, BUILT):** `τ` temporal on open `U ⊆ M`,
  `K ⊆ W ⊆ φ_q(U ∩ src_q)` compact with `hRep g q`, `chartRep T q` continuous on `W` ⟹ `∃ c > 0`,
  `dτ_x(v) ≥ c ‖Dφ_q(x) v‖` for `φ_q x ∈ K` and every future-causal `v`. The compactness step is the
  vector-space `tl_cone_bound_vs` (the closed unit cone `{g(w,w) ≤ 0, g(w,T) ≤ 0, ‖w‖ = 1}` equals
  the strict one because nonzero `w ⊥ T` has `g(w,w) > 0`).
* **`MSpacetime.tl_bump` (BUILT):** a `C¹` `ψ : N → ℝ`, `ContDiffBump` in the chart at `q` extended
  by `0`, with `ψ q = 1`, support in `φ_q⁻¹(ball)` for a closed ball inside any given open
  `O ∋ φ_q q` in the chart target, and `|dψ_x(v)| ≤ C ‖Dφ_q(x) v‖`.
* **`MSpacetime.tl_bump_temporal` (BUILT):** `|δ| C < c` ⟹ `τ + δψ` temporal on `U`.
* **② `MSpacetime.tl_iv_b` / `tl_cor_threefold_iv_b` / `tl_separation_interval` (BUILT):** for `V ∋ q`
  open (`p ∉ V`, or a causal chain `p → q` and `τ` temporal on `M`, when `V` is shrunk to
  `V \ {p}`): `∃ δ₀ > 0, ∀ δ ∈ (−δ₀, δ₀), ∃ τ'` temporal, `= τ` off `V`, with
  `τ'(q) − τ'(p) = τ(q) − τ(p) + δ`.
* **③ `NModel.tl_witness` (BUILT):** on `Pt`, `to_cor_1c`'s null pair and `τ = U + V` (now proved
  temporal on `minkN`, `NModel.tl_minkN_temporal`): for every `r > 0`, a second temporal function,
  equal to `τ` off `φ⁻¹(ball (φ q) r)`, with a different separation.

Reading flag (as registered): a local deformation moves the separation through an open interval,
not "arbitrarily"; this file proves the interval form.
-/

/-!
# Probe `r7687+71.1` (campaign 104): `cor:threefold` 2i under P1's new hypothesis "no closed causal curves"

Registration: `computations/formalisation/r7687_71_campaign104/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. It starts as a copy of campaign 103's
`probes/ThreefoldOrder.lean` (namespace renamed `ShadowProbe.ThreefoldDistinctProbe`, all old names
kept); everything new has the prefix `td_` and is in the last section before the axiom prints.

* `MSpacetime.NoClosedCausal S := ∀ p, ¬ Relation.TransGen S.CStep p p`, with the kit's causal step
  `CStep` (the step under `Cau = ReflTransGen CStep`).
* **① `td_cor_threefold_i` [T2Space N]:** under `NoClosedCausal`, `TransGen CStep p q` gives `p ≠ q`
  and disjoint open neighbourhoods of `p` and `q` (`t2_separation`).
* **② `td_noClosed_of_temporal`:** `IsTemporalOn M τ ⟹ NoClosedCausal` (each causal step strictly
  raises `τ`, `td_temporal_curve_lt`, the causal form of `me_temporal_strictMonoOn`);
  `td_noClosed_of_temporalOn` for an open `U ⊆ M` (the spacetime `restrictM U`); `td_noClosed_D`:
  a Cauchy temporal function on `D` gives `(DspN hL J).NoClosedCausal`.
* **Witness:** `td_minkN_noClosed` (Minkowski on `Pt`, `τ = U + V` read through the global chart `φ`:
  steps are carried to the vector-space `mink` by `ch_cstep_NV`, where `U + V` rises strictly);
  `td_cor_1c_hyp`: `to_cor_1c`'s pair is a `TransGen CStep` chain on a `NoClosedCausal` spacetime,
  so (i) applies to it.
-/

/-!
# Probe `r7685+71.2` (campaign 103): `cor:threefold` 2ii (the strict null ordering) on `N`, and `thm:metric-singularity` 1c (distinct, causally ordered and metrically coincident, in one theorem) on the same witness

Registration: `computations/formalisation/r7685_71_campaign103/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. It starts as a copy of campaign 93's `probes/Densities.lean`
(namespace renamed `ShadowProbe.ThreefoldOrderProbe`, all old names kept), with campaign 94's
`AlongConnection.lean` `ac_` section added: its `MSpacetime`, `gE` and `vel` are textually the kit's
(structure body and definitions identical), so the kit's copy is kept; `AdaptedSplitting` and the
`ac_` lemmas are copied unchanged; `ac_`'s model is in `ACModel` (reusing the kit's `Model.P`, `gM`,
`gM_apply`, textually the same; its `mink : MSpacetime P P` is kept as `ACModel.mink`).
Everything new has the prefix `to_`.

## NEW (campaign 103) ① — 2ii BUILT

* `MSpacetime.to_strict_null_order (hL : S.LocallyOneChart) (hq : q ∈ frontier {y | S.Cau p y})
  (_ : S.Cau p r) (hrq : S.Cau r q) : ¬ S.Chr p r` — on any `LocallyOneChart` spacetime on `N`:
  dual push-up `mk_pushup'`, `I⁺(p)` open (`mk_isOpen_Ifut`), `I⁺ ⊆ J⁺` (`chr_cau`), so `I⁺(p)` lies
  in `int J⁺(p)` (`to_Ifut_subset_interior`). No geodesic is assumed; `Cau p r` is not used.
* Corollary `MSpacetime.to_frontier_not_mem_Ifut`: `q ∈ ∂J⁺(p) ⟹ q ∉ I⁺(p)`.
* **Witness** `NModel.to_witness_order (h : V₁ < V₂)` on `Pt` (`minkN`): `J⁺((0, V₁))` is the
  closed quadrant `{U ≥ 0, V ≥ V₁}` (`to_cau_iff_N` from `ch_cau_iff`, `ch_chartSp_eq` and the model's
  `to_cau_iff`); `(0, V₂) ∈ ∂J⁺((0, V₁))` (`ch_mem_frontier_iff`); `Cau`, `¬ Chr`, distinct; every
  `(0, V)` with `V₁ < V < V₂` is causally between, distinct from both, and not in `I⁺((0, V₁))` by
  `to_strict_null_order` with `me_locallyOneChart` — so ①'s hypotheses hold: not vacuous.
  `to_witness_order_e`: the registered pair `(0, 1)`, `(0, e)`.

## NEW (campaign 103) ② — 1c BUILT (Route A, Rindler)

* `NModel.to_cor_1c`: `ac_witness`'s generator `γ s = (0, eˢ)`, carried to `Pt` as `to_γN = ψ ∘ γ`
  (the registered expected stop, the move to `Pt` through `vel` and `extChartAt p₀`, was passed:
  `to_vel_γN` by `ch_vel_symm` and `dinv_eq`, `to_gE_γN` since `γN` lies in `{t ≥ 0}`). The same
  two events `γN 0 = (0, 1)`, `γN 1 = (0, e)` of the same `minkN` are distinct; `Cau`, `¬ Chr`,
  `γN 1 ∈ ∂J⁺(γN 0)`, ①'s ordering (every causally intermediate event, in particular every `γN s`,
  `s ∈ [0, 1]`, is outside `I⁺(γN 0)`); and metrically coincident: `g(γ′, γ′) = 0` on `[0, 1]`, the
  splitting `to_σN` (`ac_`'s `σ` restated, lapse `0`) has `Δx = 0` and `Δτ = 0`, the latter by
  `ac_metric_singularity_along` applied on `minkN`, and both equal `ac_witness`'s values.

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.

# Campaign 93's header, kept
-/

/-!
# Probe `r7667+71` (campaign 93) ②: `cor:densities` 7a (with 7b, and 7c as read) on the manifold

Registration: `computations/formalisation/r7667_71_campaign93/PREDICTION.md`, the second
registration `r7667+71.2`. Nothing imports this file, and it imports no other probe. It starts as a
copy of campaign 91's `probes/ConeDisjoint.lean` (namespace renamed `ShadowProbe.DensitiesProbe`,
all old names kept); everything new has the prefix `dn_`.

## NEW (campaign 93) ②

In a conformal extension `X : ConformalExtension S St` with `hOD : I⁻(O) = D J` and
`hI : I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺)`, for every `Θ` and `τ` (no Cauchy hypothesis anywhere):

* **7a — BUILT.** `MSpacetime.dn_BH_inter_slice`:
  `(S.M ∖ X.ι ⁻¹' St.JpastSet 𝒥) ∩ S.slice J Θ τ = ∅`, by
  `slice ⊆ D = I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺) ⊆ ι⁻¹ J̃⁻(𝒥⁺)` (`dn_slice_subset_JpastSet`, `D_subset_JpastSet`
  on `S̃`).
* **7b — BUILT (bundled).** `dn_slice_inter_frontier (hLt)`: `slice ∩ ∂(ι⁻¹ J̃⁻(𝒥⁺)) = ∅`, since
  the slice lies in the open `ι⁻¹ Ĩ⁻(𝒥⁺)` (`mk_isOpen_D` on `S̃`) inside `ι⁻¹ J̃⁻(𝒥⁺)`, hence in
  its interior. This route needs only `St.LocallyOneChart`, not `mx_H_eq_boundary`'s further
  hypotheses. Also `dn_slice_inter_H (hL)`: `slice ∩ S.H J = ∅` (`mh_not_mem_D_of_H`).
* **7c — BUILT IN PART (as read).** `dn_subset_BH_inter_slice`: every `B ⊆ S.M ∖ ι⁻¹ J̃⁻(𝒥⁺)`
  meets no slice. There is still no notion of a curvature singularity; "enclosed by the horizon"
  is read as "lies in the black-hole region".
* **Bundle.** `MSpacetime.dn_cor_densities (hL) (hLt) X hOD hI`: the four statements above.
* **Witness — BUILT.** `NModel.dn_witness` on `Pt` with `mx_witnessExt` and `Θ₀ ∘ φ`:
  `dn_preimage_Jpast_scri : ι⁻¹ J̃⁻(𝒥⁺) = {U < 0}` (`cau_le` through the global chart), so the
  black-hole region is **`{U ≥ 0}`, as registered**; it is non-empty (`p₀`), every slice is
  non-empty (`O_N τ`), and every conclusion of `dn_cor_densities` holds — not vacuous.
* **7d, 7e — REPORTED (not begun).** No matter model and no singularity in the kit.

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.

# Campaign 91's header, kept

## Probe `r7663+71` (campaign 91) ①: no past light cone meets `𝓗⁺`

Registration: `computations/formalisation/r7663_71_campaign91/PREDICTION.md`, piece ①. Nothing
imports this file, and it imports no other probe. It starts as a copy of campaign 89's
`probes/ConformalBoundary.lean` (namespace renamed `ShadowProbe.ConeDisjointProbe`, all old names
kept); everything new has the prefix `cd_`.

## NEW (campaign 91) ① — BUILT

**The closure step, via properness.** In any `LocallyOneChart` spacetime:
* `MSpacetime.cd_chr_of_mem_closure_Jpast`: `x ∈ closure J⁻(p)`, `y ≪ x` ⟹ `y ≪ p` (registered
  step 1: `I⁺(y)` open, `mk_isOpen_Ifut`, meets `J⁻(p)`; dual push-up `mk_pushup'`);
* `cd_mem_closure_sublevel`: for `p ∈ D`, `Θ` temporal on `D`, `x ∈ M ∩ closure J⁻(p)` lies in
  `closure {y ∈ D | Θ y ≤ Θ p}` (`mh_past_step`, step 1, `mh_temporalD_chr`);
* `cd_closure_Jpast_subset_D`: hence, by `SublevelProper`, `closure J⁻(p) ∩ M ⊆ D`;
* `cd_closure_Jpast_inter_H`: `closure J⁻(O τ) ∩ 𝓗⁺ = ∅` (given `𝓗⁺ ⊆ M`; `𝓗⁺ ∩ D = ∅`).
The registered route's steps 2–3 (the curve into `x`, `mh_blowup`) are replaced by the properness
`mh_sublevelProper` that campaign 87 already derived from them; the content is the same.

**Headline.** `MSpacetime.cd_cone_disjoint [T2Space N] (hL : S.LocallyOneChart)
(hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
(hHM : S.H J ⊆ S.M) (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) : ∀ τ, S.cone O τ ∩ S.H J = ∅`.
`hadapt` is not needed. `MSpacetime.cd_prop_causal_alignment`: `mx_prop_causal_alignment`'s seven
conjuncts plus the eighth, `∀ τ, S.cone O τ ∩ frontier (X.ι ⁻¹' St.JpastSet 𝒥) = ∅`, with no new
hypothesis.

**Uses the Cauchy property.** The clause is proved through `SublevelProper`, i.e. the future Cauchy
property of `Θ` on `D` (P1's global hyperbolicity of `D`), not only the openness of `D`. No
`hΘ`-free proof was found: without it the step `x ∈ closure J⁻(O τ) ⟹ x ∈ D` is the
past-reflecting property, which the kit does not supply.

**Witness — BUILT.** `NModel.cd_witness`: on `Pt` with `mx_witness_headline`'s data (`Θ₀ ∘ φ`,
`mx_witnessExt`), every hypothesis discharged, the eighth conjunct read off: for every `τ`,
`cone ∩ ∂J⁻(𝒥⁺) = ∅`, i.e. no cone point has `U = 0`; and every cone is **non-empty**
(`cd_frontier_nonempty`: `Pt` is connected, `O τ ∈ J⁻(O τ)`, `p₀ ∉ J⁻(O τ)` since otherwise
`p₀ ≪ O(τ+1)` by push-up and `p₀ ∈ D`), so the disjointness is not vacuous.

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.

# Campaign 89's header, kept

## Probe `r7659+71` (campaign 89): `𝓗⁺ = ∂J⁻(𝒥⁺)` from a conformal extension, witnessed on `Pt`
compactified by `arctan V`, and `prop:causal-alignment` assembled whole

Registration: `computations/formalisation/r7659_71_campaign89/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. It starts as a copy of campaign 88's `probes/ManifoldCones.lean`
(namespace renamed `ShadowProbe.ConformalBoundaryProbe`, all old names kept); everything new has the
prefix `mx_`.

## NEW (campaign 89)

**The definition.** `ConformalExtension S St` (`S` on `N`, `St` (`S̃`) on `Ñ`, same model `E`): `ι : N → Ñ`,
`isOpenEmbedding`, `contMDiff` (class `1`), `Ω > 0` with
`g̃_{ι x}(Dι v, Dι w) = Ω x ² g_x(v, w)` (`conformal`, with `Dι = mx_dι ι x = mfderiv ι x`),
`Dι(T x)` future-timelike for `S̃` on `M` (`timeOrient`), `ι(M) ⊆ M̃` (`maps_M`).

**① The identification — BUILT.** `MSpacetime.mx_frontier_JpastSet`: on any `LocallyOneChart`
spacetime and `A ⊆ M`, `∂J⁻(A) = closure I⁻(A) ∖ I⁻(A)` (`mh_hint`, `mh_hcl`, `mk_isOpen_D`);
`mx_preimage_frontier` / `mx_preimage_closure` (Mathlib's `IsOpenMap.preimage_*`). Headline
`MSpacetime.mx_H_eq_boundary (hL : S.LocallyOneChart) (hLt : St.LocallyOneChart)
(X : ConformalExtension S St) (h𝒥 : 𝒥 ⊆ St.M) (hOD : S.IpastSet (range O) = S.D J)
(hmono : ∀ s t, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
(hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) :
S.H (range O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧ S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥)`.
*As stated in advance, only `ι` and `isOpenEmbedding` are used*; the conformal, time-orientation,
`C¹` and `ι(M) ⊆ M̃` fields belong to the definition but not to the proof. No hypothesis beyond the
registration (`hOD` and `hJM` serve only the `S.H J` form; `hmono` gives `range O ⊆ M`).

**② The witness — BUILT.** On `Pt` (`S = St = minkN`), `mx_ι = ψ ∘ mx_fA ∘ φ`,
`mx_fA (U, V) = (U, arctan V)`, through the `nullH` chart `φ`:
* `mx_ι_isOpenEmbedding` (`arctan = val ∘ tanOrderIso.symm`), `mx_ι_contMDiff` (Mathlib's
  `contMDiffOn_extChartAt(_symm)` on the global chart, `contMDiff_iff_contDiff`) — the registered
  expected stop was not hit;
* `mx_dι_eq`: `Dφ ∘ Dι = diag(1, 1/(1+V²)) ∘ Dφ` (`mfderiv_comp`), so with `g = −dU dV`,
  `Ω = (1+V²)^{−1/2}`, `Ω² = 1/(1+V²)` (as registered);
* `mx_witnessExt : ConformalExtension minkN minkN` — every field proved;
* `𝒥⁺ = mx_scri = ψ '' {(U, π/2) : U < 0}`; `mx_scri_subset_frontier : 𝒥⁺ ⊆ ∂ι(Pt)`;
  `mx_mem_mink_D_JA`: `Ĩ⁻(𝒥⁺) = ψ '' {U < 0, V < π/2}` (`chr_lt`, `tstep_of_lt`; the registered
  second-likeliest stop was not hit: no curve need stay in `ι(Pt)`, since `Ĩ⁻` is computed in `Ñ`);
  `mx_preimage_Ipast_scri : ι⁻¹ Ĩ⁻(𝒥⁺) = {U < 0} = D`.
* `NModel.mx_witness_boundary`: all of the above, `hI`, and by `mx_H_eq_boundary`,
  `∂J⁻(𝒥⁺) = 𝓗⁺ = {U = 0}`, non-empty.

**③ The headline whole — BUILT.** `MSpacetime.mx_prop_causal_alignment [T2Space N]` with the
hypotheses of ① plus `hHM : ∂J⁻(𝒥⁺) ⊆ S.M`, `hΘ : S.IsCauchyTemporalOn (S.D J) Θ`,
`hadapt : ∀ τ, Θ (O τ) = τ + c`, concluding, with `𝓗⁺ := frontier (X.ι ⁻¹' St.JpastSet 𝒥)`:
`S.H J = 𝓗⁺`, `SublevelProper`, `KLi/KLs (slice) = 𝓗⁺`, `KLi/KLs (cone O) = 𝓗⁺`, and for every
`q ∈ 𝓗⁺` and every frame `(ℓ, n)`, filter `L ≤ 𝓝 q`, under `mc_tangency_at_N`'s hypotheses,
`(dΘ(n))⁻¹ • dΘ^{e_q} → −g_q(ℓ₀, ·)`. `NModel.mx_witness_headline`: on `Pt` with `Θ₀ ∘ φ`, every
hypothesis discharged and every clause read off, the tangency hypotheses discharged at `p₀ ∈ 𝓗⁺`
with `(ℓN, nN)` along `𝓝[D] p₀`.

*Non-vacuity:* every new theorem's hypotheses are discharged on `Pt`. *Limit:* `Ñ = N = Pt` as
types, and `Pt` still has one global chart.

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.

# Campaign 88's header, kept

## Probe `r7657+71` (campaign 88): the cone-convergence and tangency clauses of
`prop:causal-alignment` on a multi-chart manifold `N`, witnessed on the two-chart `Pt`

Registration: `computations/formalisation/r7657_71_campaign88/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. It starts as a copy of campaign 87's
`probes/ManifoldHeadline.lean` (namespace renamed `ShadowProbe.ManifoldConesProbe`, all `mh_`/`mk_`/
`me_`/`ch_`/`hl_` names kept); everything new has the prefix `mc_`.

## Copied in for campaign 88

* Campaign 80's `TangencyCondition.lean`, sections ① frame-free and normed, inside namespace `TCF`
  (names `tc_…` kept): `NullFrame`, `FutCausal`, `projW`, `tc_futCausal_iff`, `tc_pos`,
  `tc_W_bound`, `tc_pointwise`, `bil`, `FrameHyp`, `tc_opNorm_bound`, `tc_ratio_of_bounded`,
  `tc_tendsto`, `tc_tendsto_limit`, `tc_sequence`.
* Campaign 72's `hc_preconnected_inter_frontier` (as `mc_preconnected_inter_frontier`, now in any
  topological space) and the shape of `hc_lower_limit` / `hc_upper_limit` / `hc_kuratowski`.
* Campaign 79's frame `ℓ = ∂_V`, `n = 2∂_U` (`Model.ellV`, `Model.nvec`), the sequence `sm`, `xm`
  with `log_sm`, `cos_log_sm`, `deriv_Ffail_sm`, `xm_mem`, and the computations behind `st_aligned`
  (`dΘ₀(ℓ)/dΘ₀(n) = −U/2`) and `st_tangency_fails` (`dΘ = dU + dV` at `x_m`); campaign 80's
  `tc_frameHyp2` at `F = 1` (`Model.mc_frameHyp_gM`).

## NEW (campaign 88)

**① Cone convergence on `N` — BUILT.** `MSpacetime.cone S O τ = ∂_N J⁻(O τ)`.
`mc_lower_limit` (a connected open neighbourhood of `p ∈ 𝓗⁺` — `N` is locally connected by
`ChartedSpace.locallyConnectedSpace` — meets `D` by `mh_hcl`, hence `I⁻(O τ)` for large `τ`, and
`p ∉ int J⁻(O τ)` because `J⁻(O τ) ⊆ J⁻(J)`; so it meets `∂J⁻(O τ)`), `mc_upper_limit` (limit point
in `closure J⁻(J)`, not in `D` since `I⁻(O σ)` is open (`mk_isOpen_Ipast`) and lies in
`int J⁻(O τ)` for `τ ≥ σ`, then `mh_hint`), and the headline
`MSpacetime.mc_cone_kuratowski_N (hL : S.LocallyOneChart) (hOD : S.IpastSet (range O) = S.D J)
(hmono : ∀ s t, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M) :
KLi (S.cone O) = S.H J ∧ KLs (S.cone O) = S.H J`.
Fewer hypotheses than registered: neither `T2Space N` nor `𝓗⁺ ⊆ M` is used, and push-up is not
needed for `p ∉ int J⁻(O τ)` (transitivity suffices, as in campaign 72).

**② Tangency on `N` — BUILT (in chart-component form, with the transformation law).**
Mathlib reads `dΘ_x = mfderiv Θ x` (`dcov`), `g_x` and frames `ℓ_x, n_x` in the preferred chart at
`x`. For a chart `e = extChartAt p` and `x ∈ src e`: `A_x = D e_x` (`dchartL`),
`B_x = D(e⁻¹)_{e x}` (`dchartInvL`, `= tangentCoordChange p x x`, `mc_B_eq`), covector
`covCh Θ p x = dΘ_x ∘ B_x`, metric `gCh p x = hRep g p (e x)`.
* `mc_frameHyp_pullback`, `MSpacetime.mc_frameHyp_toChart` / `mc_frameHyp_ofChart`: the frame
  hypotheses are chart-free; `mc_covCh_A`: so is the rate `dΘ_x(ℓ_x)/dΘ_x(n_x)`.
* `MSpacetime.mc_tangency_N` (any chart, any filter): intrinsic frame hypotheses eventually,
  `‖g^e‖`, `‖g^e‖‖n^e‖`, `‖ℓ^e‖` bounded, rate `→ 0` ⟹
  `dΘ^e_x/dΘ_x(n_x) + g^e_x(ℓ^e_x, ·) → 0` (campaign 80's `tc_tendsto` on the `e`-components).
* `MSpacetime.mc_tangency_limit_N`: `L ≤ 𝓝 q`, `hRep g p` continuous at `e q`, `‖n^e‖` bounded,
  `ℓ^e_x → ℓ₀` ⟹ `dΘ^e_x/dΘ_x(n_x) → −g^e_{e q}(ℓ₀, ·)`.
* `MSpacetime.mc_tangency_at_N` (the registered statement): with `LocallyOneChart` and the chart at
  the horizon point `q` itself, the continuity is supplied and the limit is `−g_q(ℓ₀, ·)`.
* `mc_chart_change` (registered chart-independence): if the components in `e'` converge to `λ'`,
  those in `e` converge to `λ' ∘ tangentCoordChange p p' q` (`mc_covCh_change`, Mathlib's
  `continuousOn_tangentCoordChange`).
*The registered expected stop was not hit in this form.* What is **not** built: a statement in the
cotangent bundle as a space (convergence of `(x, dΘ_x/dΘ_x(n_x))` in `TotalSpace` of `T*N`);
here convergence is stated, as is standard, by components in a chart together with the
transformation law between charts. In a chart other than the one at `q`, continuity of `hRep g p` at
`e q` is a hypothesis (it is not derived from `LocallyOneChart`).

**③ The witness on `Pt` — BUILT.** Through the global chart `φ = extChartAt p₀` (`nullH`), with the
intrinsic frame `ℓN x = B_x ∂_V`, `nN x = B_x (2∂_U)`; `mc_covCh_comp_chart` (chain rule in a chart:
`d(f ∘ φ)` read in `φ` is `fderiv f`).
* `NModel.mc_witness_frameHyp`: the intrinsic frame hypotheses at every point of `D` for every good
  profile.
* `NModel.mc_witness_tangency_holds` (`Θ₀ ∘ φ`, every `q ∈ 𝓗⁺`): Cauchy temporal on `D`,
  `𝓝[D] q ≠ ⊥`, frame hypotheses, rate `−U/2 → 0`, the conclusion of `mc_tangency_N`, and by
  `mc_tangency_limit_N` the limit `½ dU = −g(ℓ, ·)`.
* `NModel.mc_witness_tangency_at` (`q = p₀`): `mc_tangency_at_N` with `LocallyOneChart`, and
  `mc_chart_change` to the other chart `idH`, with the coordinate change computed
  (`tCC_neg_p₀ = nullL`) and the limit `½ (dt − dx)`.
* `NModel.mc_witness_tangency_fails` (`Θf ∘ φ`, at `p₀`): Cauchy temporal on `D`, frame hypotheses
  at every point of `D`, but along `ψ(x_m) → p₀` the rate is `1/2`, so neither the rate condition
  nor the conclusion holds.
* `NModel.mc_witness_cones`: `KLi = KLs = 𝓗⁺ = {U = 0}` (non-empty) for the past cones on `Pt`, via
  `mc_cone_kuratowski_N`.
Every new theorem's hypotheses are discharged on `Pt` by these.
*Limit, as registered:* one chart of `Pt`'s atlas covers `Pt`; the flat cylinder still waits.

**④ `𝓗⁺ = ∂J⁻(𝒥⁺)` — registered and priced, not built (not attempted here).**

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.

# Campaign 87's header, kept

### Copied

* Campaign 84's `probes/ChartHeadline.lean`, nearly all of it (its module docstring dropped): the
  `V`-side chain of campaigns 60–81 with campaign 81's two-sided Rindler `Model` (`hl_cauchy`,
  `hl_adapted`, `GoodG`, `Θ₀`, `Θf`), campaign 68's `chartRep`/`hRep`, the intrinsic `MSpacetime`
  (`TStep`, `Chr`, `Cau`, `D`, `H`, `slice`, `SublevelProper`, `KLi`/`KLs`, `IsTemporalOn`,
  `IsCauchyTemporalOn`), `OneChart`, the chart transfer, `ch_isCauchy_VN`,
  `ch_causal_alignment_gh_N`, and `NModel` (`Pt`, two-chart atlas, `minkN`, `ch_oneChart`,
  `ch_chartSp_eq`, `JN`, `mem_D_N`, `mem_H_N`, `ch_witness_hypotheses`).
* Campaign 85's `probes/ManifoldExtension.lean`: `restrictM`, `LocallyOneChart`(`.restrict`),
  `me_local_step`, `me_temporal_*`, the drop/vertices/gluing, `me_past_extension`,
  `FutInextCurveIn`, `FutCauchyTemporalOn`, `me_futCauchy_of_cauchy_N`; and in `NModel`
  `nullInvL`, `chartAt_neg`/`_nonneg`, `me_dchart_neg`, `hRep_neg`, `chartRep_neg`,
  `me_charts_differ`, `me_locallyOneChart`.
* Campaign 86's `probes/ManifoldLocalKit.lean`, pieces 1–5 (`mk_*`): restriction, openness of
  `I^±` and `D J` on `N`, `mk_local_step_fut` (`Safe2`), `mk_curve_into`, `mk_curve_inext_D`,
  push-up `mk_pushup`/`mk_pushup'`.

### NEW (`hL : S.LocallyOneChart`; `[T2Space N]` where the curve into a point is used)

1. **Temporal increase along `≪` into `D` — BUILT.** `DspN hL J := S.restrictM (D J)`;
   `mh_tstep_DspN` (a `TStep_N` ending in `D` runs inside `D`, via `mk_tstep_sub`);
   `mh_temporalD_chr` (`IsTemporalOn (D J) Θ`, `x ≪ y ∈ D ⟹ Θ x < Θ y`: `me_temporal_tstep` in
   `DspN` plus induction — campaign 75/78's `cr_temporalD_chr` reproduced on `N`).
2. **`hint` and `hcl` on `N` — BUILT.** `mh_future_step` (`mk_local_step_fut` at `x`, cut short by
   `mk_tstep_restrict`), `mh_past_step` (tail of `mk_curve_into`), `mh_hint`
   (`int J⁻(J) ⊆ D`, by `mk_pushup'`), `mh_hcl` (`closure J⁻(J) ⊆ closure D`, by `mk_pushup'`).
3. **Properness on `N` — BUILT** (the registered second-likeliest stop, not hit).
   `mh_blowup` (`mk_curve_inext_D` + the future Cauchy property + `I⁺(r)` open,
   `mk_isOpen_Ifut`), `mh_sublevelProper`. The future Cauchy property comes from
   `me_futCauchy_of_cauchy_N` at `U = D J`, open by `mk_isOpen_D`.
4. **Slice lower limit — BUILT.** `mh_mem_KLi_slice`, `mh_slice_lower_limit` (the curve's tail).
5. **Slice upper limit and Kuratowski — BUILT** (the registered expected stop, not hit).
   Campaign 81's argument turned out to use no vector-space structure: only that `I⁻(O σ)` is open
   (now `mk_isOpen_Ipast`), `D ⊆ J⁻(J)` and `Θ` increasing along `≪` into `D` (piece 1).
   `mh_slice_upper_limit`, `mh_slice_kuratowski`.
6. **The headline — BUILT.** `MSpacetime.mh_causal_alignment_gh_N (hL : S.LocallyOneChart)
   [T2Space N] (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t, s < t → S.Chr (O s) (O t))
   (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M) (hΘ : S.IsCauchyTemporalOn (S.D J) Θ)
   (hadapt : ∀ τ, Θ (O τ) = τ + c) :
   S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J`.

### Witness — BUILT

`NModel.mh_witness_hypotheses`: on the two-chart `Pt` (preferred chart `idH` on `{t < 0}`,
`nullH` on `{t ≥ 0}`, `me_charts_differ`), `LocallyOneChart`, `T2Space Pt`, and every other
hypothesis, **including `IsCauchyTemporalOn (D JN) (Θ_G ∘ φ)`** (left open by campaign 85), by
campaign 84's transport `ch_isCauchy_VN` through the global chart `nullH` from campaign 81's
two-sided model `Model.hl_cauchy`. `NModel.mh_witness_headline`: for `Θ₀ ∘ φ` and `Θf ∘ φ`,
properness and `KLi = KLs = 𝓗⁺ = {U = 0}` (non-empty), via `mh_causal_alignment_gh_N`.
*Limit, as registered:* one chart of `Pt`'s atlas covers `Pt`, so the witness does not need two
charts; it exercises the multi-chart theorem with differing preferred charts.

### Stretch — REPORTED

A witness no single chart covers (flat cylinder `ℝ × S¹`) is not attempted: it needs a new
charted space, `LocallyOneChart` on it, and a Cauchy proof on `N` with no global chart to transport
through.

`#print axioms` at the end. `set_option synthInstance.maxHeartbeats 400000` inside `Model` (copied).
-/

open Set Filter Topology Metric

namespace ShadowProbe.ThreefoldLocalProbe

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- A time-oriented Lorentzian chart (campaign 60). -/
structure Spacetime (V : Type*) [NormedAddCommGroup V] [NormedSpace ℝ V] where
  M : Set V
  isOpen_M : IsOpen M
  g : V → V →L[ℝ] V →L[ℝ] ℝ
  cont_g : ContinuousOn g M
  symm : ∀ x v w, g x v w = g x w v
  T : V → V
  cont_T : ContinuousOn T M
  T_timelike : ∀ x ∈ M, g x (T x) (T x) < 0
  pos_on_perp : ∀ x ∈ M, ∀ v, g x v (T x) = 0 → v ≠ 0 → 0 < g x v v

namespace Spacetime
variable (S : Spacetime V)

/-- Future-directed timelike vector at `x`. -/
def FutTimelike (x v : V) : Prop := S.g x v v < 0 ∧ S.g x v (S.T x) < 0
/-- Future-directed causal vector at `x`. -/
def FutCausal (x v : V) : Prop := S.g x v v ≤ 0 ∧ S.g x v (S.T x) < 0

/-- One `C¹` future-timelike piece from `x` to `y`. -/
def TStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t)

/-- One `C¹` future-causal piece from `x` to `y`. -/
def CStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t)

/-- `x ≪ y`. -/
def Chr (x y : V) : Prop := Relation.TransGen S.TStep x y
/-- `x ≤ y`. -/
def Cau (x y : V) : Prop := Relation.ReflTransGen S.CStep x y

/-- `I⁻(p)`. -/
def Ipast (p : V) : Set V := {q | S.Chr q p}
/-- `J⁻(p)`. -/
def Jpast (p : V) : Set V := {q | S.Cau q p}
/-- `I⁻(A)`. -/
def IpastSet (A : Set V) : Set V := ⋃ p ∈ A, S.Ipast p
/-- `J⁻(A)`. -/
def JpastSet (A : Set V) : Set V := ⋃ p ∈ A, S.Jpast p

/-- c1: `T` is continuous at points of `M` (`cont_T` is now only `ContinuousOn T M`, `M` open). -/
lemma contAt_T {x : V} (hx : x ∈ S.M) : ContinuousAt S.T x :=
  S.cont_T.continuousAt (S.isOpen_M.mem_nhds hx)

/-- c1: the pointwise form of campaign 60's `cont_gvw`, at a parameter whose base point lies in `M`. -/
lemma cont_gvw_at {X : Type*} [TopologicalSpace X] {x v w : X → V} {a : X} (hx : ContinuousAt x a)
    (hxM : x a ∈ S.M) (hv : ContinuousAt v a) (hw : ContinuousAt w a) :
    ContinuousAt (fun a => S.g (x a) (v a) (w a)) a :=
  (((S.cont_g.continuousAt (S.isOpen_M.mem_nhds hxM)).comp hx).clm_apply hv).clm_apply hw

lemma isOpen_timelikePairs :
    IsOpen {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
  refine isOpen_iff_mem_nhds.2 fun pv ⟨hM, h1, h2⟩ => ?_
  have e1 : ∀ᶠ q : V × V in 𝓝 pv, q.1 ∈ S.M :=
    continuousAt_fst.eventually_mem (S.isOpen_M.mem_nhds hM)
  have e2 : ∀ᶠ q : V × V in 𝓝 pv, S.g q.1 q.2 q.2 < 0 :=
    (S.cont_gvw_at continuousAt_fst hM continuousAt_snd continuousAt_snd).eventually_lt
      continuousAt_const h1
  have e3 : ∀ᶠ q : V × V in 𝓝 pv, S.g q.1 q.2 (S.T q.1) < 0 :=
    (S.cont_gvw_at continuousAt_fst hM continuousAt_snd
      ((S.contAt_T hM).comp continuousAt_fst)).eventually_lt continuousAt_const h2
  filter_upwards [e1, e2, e3] with q a b c using ⟨a, b, c⟩

lemma tube {P Q : V → ℝ → V} (hP : Continuous fun z : V × ℝ => P z.1 z.2)
    (hQ : Continuous fun z : V × ℝ => Q z.1 z.2)
    (h0 : ∀ t ∈ Icc (0:ℝ) 1, P 0 t ∈ S.M ∧ S.FutTimelike (P 0 t) (Q 0 t)) :
    ∀ᶠ w in 𝓝 (0:V), ∀ t ∈ Icc (0:ℝ) 1, P w t ∈ S.M ∧ S.FutTimelike (P w t) (Q w t) := by
  refine isCompact_Icc.eventually_forall_of_forall_eventually fun t ht => ?_
  have hO := S.isOpen_timelikePairs.preimage (hP.prodMk hQ)
  exact hO.mem_nhds (h0 t ht)

lemma hasDerivAt_of_contDiff {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) (t : ℝ) :
    HasDerivAt γ (deriv γ t) t :=
  ((hγ.differentiable one_ne_zero) t).hasDerivAt

/-- The start of a timelike step can be moved in an open set. -/
lemma tstep_start_eventually {p y : V} (h : S.TStep p y) : ∀ᶠ p' in 𝓝 p, S.TStep p' y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.tube (P := fun w t => γ t + (1 - t) • w) (Q := fun w t => deriv γ t - w)
    ((hγ.continuous.comp continuous_snd).add
      ((continuous_const.sub continuous_snd).smul continuous_fst))
    ((hdc.comp continuous_snd).sub continuous_fst) (by simpa using hγt)
  have hlim : Tendsto (fun p' => p' - p) (𝓝 p) (𝓝 0) := tendsto_sub_nhds_zero_iff.2 tendsto_id
  filter_upwards [hlim.eventually hT] with p' hp'
  refine ⟨fun t => γ t + (1 - t) • (p' - p),
    hγ.add ((contDiff_const.sub contDiff_id).smul contDiff_const), by simp [h0],
    by simp [h1], fun t ht => ?_⟩
  have hd : deriv (fun t => γ t + (1 - t) • (p' - p)) t = deriv γ t - (p' - p) := by
    have h : HasDerivAt (fun t => γ t + (1 - t) • (p' - p))
        (deriv γ t + ((0:ℝ) - 1) • (p' - p)) t :=
      (hasDerivAt_of_contDiff hγ t).add
        (((hasDerivAt_const t (1:ℝ)).sub (hasDerivAt_id' t)).smul_const (p' - p))
    rw [h.deriv, zero_sub, neg_one_smul, ← sub_eq_add_neg]
  rw [hd]; exact hp' t ht

/-- `I⁻(p)` is open (campaign 60's `hl_isOpen_Ipast`). -/
theorem hl_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

/-- `≪ ⊆ ≤`. -/
theorem hl_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_to_cstep h)

theorem hl_chr_trans {x y z : V} (h1 : S.Chr x y) (h2 : S.Chr y z) : S.Chr x z :=
  Relation.TransGen.trans h1 h2

theorem hl_cau_trans {x y z : V} (h1 : S.Cau x y) (h2 : S.Cau y z) : S.Cau x z :=
  Relation.ReflTransGen.trans h1 h2

theorem hl_Ipast_subset_Jpast (p : V) : S.Ipast p ⊆ S.Jpast p := fun _ h => S.hl_chr_cau h

/-! ## Copied from campaign 60 (`probes/CausalStructure.lean`): push-up and time reversal -/

/-- Positive rescaling preserves future-timelikeness. -/
lemma futTimelike_smul {x u : V} {c : ℝ} (hc : 0 < c) (h : S.FutTimelike x u) :
    S.FutTimelike x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

/-- Lipschitz control of the quadratic form. -/
lemma quad_le {K : NNReal} {N : Set V} (hK : LipschitzOnWith K S.g N) {p q : V} (hp : p ∈ N)
    (hq : q ∈ N) (a : V) : S.g p a a ≤ S.g q a a + K * dist p q * (‖a‖ * ‖a‖) := by
  have h1 : |S.g p a a - S.g q a a| ≤ ‖S.g p - S.g q‖ * ‖a‖ * ‖a‖ := by
    have := (S.g p - S.g q).le_opNorm₂ a a
    simpa [Real.norm_eq_abs] using this
  have h2 : ‖S.g p - S.g q‖ ≤ K * dist p q := by
    have := hK.dist_le_mul p hp q hq
    rwa [dist_eq_norm] at this
  have h3 := (abs_le.1 h1).2
  have h4 : ‖S.g p - S.g q‖ * ‖a‖ * ‖a‖ ≤ K * dist p q * (‖a‖ * ‖a‖) := by
    rw [mul_assoc]; exact mul_le_mul_of_nonneg_right h2 (by positivity)
  linarith

/-- Local push-up. -/
lemma local_pushup (hL : LocallyLipschitzOn S.M S.g) {α : ℝ → V} (hα : ContDiff ℝ 1 α)
    (hc : ∀ t ∈ Icc (0:ℝ) 1, α t ∈ S.M ∧ S.FutCausal (α t) (deriv α t))
    {s : ℝ} (hs : s ∈ Icc (0:ℝ) 1) :
    ∃ ε > 0, ∀ t ∈ Icc (0:ℝ) 1, s < t → t < s + ε → ∀ l : ℝ, 0 < l → l < ε →
      S.TStep (α s) (α t + (l * (t - s)) • S.T (α s)) := by
  obtain ⟨hx₀M, -, hb⟩ := hc s hs
  obtain ⟨K, N, hN, hK⟩ := hL hx₀M
  rw [S.isOpen_M.nhdsWithin_eq hx₀M] at hN
  have hvv : S.g (α s) (S.T (α s)) (S.T (α s)) < 0 := S.T_timelike _ hx₀M
  -- abbreviations
  have hdc : Continuous (deriv α) := hα.continuous_deriv le_rfl
  let v := S.T (α s)
  let u₀ := deriv α s
  let b := -(S.g (α s) u₀ v)
  have hbpos : 0 < b := by simp only [b]; linarith
  let P : V × V → Prop := fun pu => pu.1 ∈ S.M ∧ S.g pu.1 pu.2 v < -(b/2) ∧
    S.g pu.1 v v < 0 ∧ S.g pu.1 pu.2 (S.T pu.1) < 0 ∧ S.g pu.1 v (S.T pu.1) < 0 ∧
    pu.1 ∈ N ∧ ‖pu.2‖ < ‖u₀‖ + 1
  have hW : ∀ᶠ pu in 𝓝 (α s, u₀), P pu := by
    have e1 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), pu.1 ∈ S.M :=
      continuousAt_fst.eventually_mem (S.isOpen_M.mem_nhds hx₀M)
    have e2 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 pu.2 v < -(b/2) :=
      (S.cont_gvw_at continuousAt_fst hx₀M continuousAt_snd continuousAt_const).eventually_lt
        continuousAt_const (by simp only [b, u₀]; linarith)
    have e3 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 v v < 0 :=
      (S.cont_gvw_at continuousAt_fst hx₀M continuousAt_const continuousAt_const).eventually_lt
        continuousAt_const hvv
    have e4 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 pu.2 (S.T pu.1) < 0 :=
      (S.cont_gvw_at continuousAt_fst hx₀M continuousAt_snd
        ((S.contAt_T hx₀M).comp (x := (α s, u₀)) continuousAt_fst)).eventually_lt continuousAt_const hb
    have e5 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 v (S.T pu.1) < 0 :=
      (S.cont_gvw_at continuousAt_fst hx₀M continuousAt_const
        ((S.contAt_T hx₀M).comp (x := (α s, u₀)) continuousAt_fst)).eventually_lt continuousAt_const hvv
    have e6 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), pu.1 ∈ N := continuousAt_fst.eventually_mem hN
    have e7 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), ‖pu.2‖ < ‖u₀‖ + 1 :=
      (continuous_norm.comp continuous_snd).continuousAt.eventually_lt continuousAt_const
        (by simp)
    filter_upwards [e1, e2, e3, e4, e5, e6, e7] with pu h1 h2 h3 h4 h5 h6 h7
    exact ⟨h1, h2, h3, h4, h5, h6, h7⟩
  let Φ : ℝ × ℝ → V × V := fun z => (α z.1 + (z.2 * (z.1 - s)) • v, deriv α z.1)
  have hΦc : Continuous Φ := by
    refine Continuous.prodMk ?_ (hdc.comp continuous_fst)
    exact (hα.continuous.comp continuous_fst).add
      ((continuous_snd.mul (continuous_fst.sub continuous_const)).smul continuous_const)
  have hΦ : Tendsto Φ (𝓝 (s, 0)) (𝓝 (α s, u₀)) := by
    have := hΦc.tendsto (s, 0)
    simpa [Φ, u₀] using this
  have hαN : ∀ᶠ z : ℝ × ℝ in 𝓝 (s, 0), α z.1 ∈ N :=
    ((hα.continuous.comp continuous_fst).tendsto (s, 0)).eventually_mem (by simpa using hN)
  have hLip : ∀ᶠ z : ℝ × ℝ in 𝓝 (s, 0),
      (K:ℝ) * |z.1 - s| * ‖v‖ * (‖u₀‖ + 1) ^ 2 < b / 2 := by
    refine ContinuousAt.eventually_lt (by fun_prop) continuousAt_const ?_
    simp; linarith
  obtain ⟨ε, hε, hεP⟩ := Metric.eventually_nhds_iff.1 ((hΦ.eventually hW).and (hαN.and hLip))
  refine ⟨ε, hε, fun t ht hst htε l hl hlε => ?_⟩
  refine ⟨fun r => α (s + r * (t - s)) + (l * (r * (t - s))) • v,
    (hα.comp (contDiff_const.add (contDiff_id.mul contDiff_const))).add
      ((contDiff_const.mul (contDiff_id.mul contDiff_const)).smul contDiff_const),
    by simp, by simp [v], fun r hr => ?_⟩
  have hts : 0 < t - s := sub_pos.2 hst
  set s' := s + r * (t - s) with hs'
  have hs's : s' - s = r * (t - s) := by rw [hs']; ring
  have hs'0 : 0 ≤ s' - s := by rw [hs's]; exact mul_nonneg hr.1 hts.le
  have hs'1 : s' - s ≤ t - s := by rw [hs's]; nlinarith [hr.2]
  have hs'I : s' ∈ Icc (0:ℝ) 1 := ⟨by linarith [hs.1], by linarith [ht.2]⟩
  -- the derivative
  have hin : HasDerivAt (fun r => s + r * (t - s)) (t - s) r := by
    simpa using ((hasDerivAt_id r).mul_const (t - s)).const_add s
  have h1 : HasDerivAt (fun r => α (s + r * (t - s))) ((t - s) • deriv α s') r :=
    (hasDerivAt_of_contDiff hα _).scomp r hin
  have h2 : HasDerivAt (fun r => (l * (r * (t - s))) • v) ((l * (t - s)) • v) r := by
    simpa using (((hasDerivAt_id r).mul_const (t - s)).const_mul l).smul_const v
  have hd : deriv (fun r => α (s + r * (t - s)) + (l * (r * (t - s))) • v) r =
      (t - s) • (deriv α s' + l • v) := by
    have h3 : HasDerivAt (fun r => α (s + r * (t - s)) + (l * (r * (t - s))) • v)
        ((t - s) • deriv α s' + (l * (t - s)) • v) r := h1.add h2
    rw [h3.deriv, smul_add, smul_smul, mul_comm l]
  have hpt : α (s + r * (t - s)) + (l * (r * (t - s))) • v = α s' + (l * (s' - s)) • v := by
    rw [hs's]
  rw [hd]
  beta_reduce
  rw [hpt]
  -- the estimates at `(s', l)`
  have hdist : dist (s', l) (s, 0) < ε := by
    rw [Prod.dist_eq, max_lt_iff, Real.dist_eq, Real.dist_eq, sub_zero, abs_of_nonneg hs'0,
      abs_of_pos hl]
    exact ⟨by linarith, hlε⟩
  obtain ⟨⟨hpM, hav, hvv', haT, hvT, hpN, hna⟩, hαN', hLip'⟩ := hεP hdist
  simp only [Φ] at hpM hav hvv' haT hvT hpN hna hαN' hLip'
  set p := α s' + (l * (s' - s)) • v with hp
  set a := deriv α s' with ha
  have hcaus := (hc s' hs'I).2.1
  have hq := S.quad_le hK hpN hαN' a
  have hdp : dist p (α s') = l * (s' - s) * ‖v‖ := by
    rw [hp, dist_eq_norm, add_sub_cancel_left, norm_smul, Real.norm_eq_abs,
      abs_of_nonneg (mul_nonneg hl.le hs'0)]
  rw [hdp] at hq
  have hna0 : 0 ≤ ‖a‖ := norm_nonneg a
  have hasq : ‖a‖ * ‖a‖ ≤ (‖u₀‖ + 1) ^ 2 := by nlinarith
  have hQ0 : 0 ≤ (K:ℝ) * (s' - s) * ‖v‖ := by positivity
  have hLip'' : (K:ℝ) * (s' - s) * ‖v‖ * (‖u₀‖ + 1) ^ 2 < b / 2 := by
    rwa [abs_of_nonneg hs'0] at hLip'
  have hKa : (K:ℝ) * (l * (s' - s) * ‖v‖) * (‖a‖ * ‖a‖) ≤ l * (b / 2) := by
    have : (K:ℝ) * (s' - s) * ‖v‖ * (‖a‖ * ‖a‖) ≤ (K:ℝ) * (s' - s) * ‖v‖ * (‖u₀‖ + 1) ^ 2 :=
      mul_le_mul_of_nonneg_left hasq hQ0
    nlinarith
  have hgaa : S.g p a a ≤ l * (b / 2) := by linarith
  refine ⟨hpM, S.futTimelike_smul hts ⟨?_, ?_⟩⟩
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul, Pi.smul_apply,
      smul_eq_mul]
    rw [S.symm p v a]
    nlinarith [mul_pos hl hl]
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul, Pi.smul_apply,
      smul_eq_mul]
    nlinarith

/-- Push-up along one causal step: a causal step followed by a timelike chain is a timelike
chain. Needs `g` locally Lipschitz. -/
lemma pushup_cstep (hL : LocallyLipschitzOn S.M S.g) {x y z : V} (hxy : S.CStep x y)
    (hyz : S.Chr y z) : S.Chr x z := by
  obtain ⟨α, hα, h0, h1, hc⟩ := hxy
  let A : Set ℝ := {t | t ∈ Icc (0:ℝ) 1 ∧ S.Chr (α t) z}
  have h1A : (1:ℝ) ∈ A := ⟨⟨zero_le_one, le_rfl⟩, by simp only [h1]; exact hyz⟩
  have hne : A.Nonempty := ⟨1, h1A⟩
  have hbdd : BddBelow A := ⟨0, fun t ht => ht.1.1⟩
  have hs0 : 0 ≤ sInf A := le_csInf hne fun t ht => ht.1.1
  have hs1 : sInf A ≤ 1 := csInf_le hbdd h1A
  have hαc := hα.continuous
  have hsA : S.Chr (α (sInf A)) z := by
    obtain ⟨ε, hε, hloc⟩ := S.local_pushup hL hα hc ⟨hs0, hs1⟩
    obtain ⟨t, htA, hts⟩ := exists_lt_of_csInf_lt hne (show sInf A < sInf A + ε by linarith)
    have hst : sInf A ≤ t := csInf_le hbdd htA
    rcases hst.lt_or_eq with hst | hst
    · have hcl : Continuous fun l : ℝ => α t + (l * (t - sInf A)) • S.T (α (sInf A)) := by
        fun_prop
      have hev : ∀ᶠ l in 𝓝 (0:ℝ), S.Chr (α t + (l * (t - sInf A)) • S.T (α (sInf A))) z := by
        have := hcl.tendsto 0
        simp only [zero_mul, zero_smul, add_zero] at this
        exact this.eventually ((S.hl_isOpen_Ipast z).mem_nhds htA.2)
      obtain ⟨l, hl, hlpos, hlε⟩ :=
        ((hev.filter_mono nhdsWithin_le_nhds).and (Ioo_mem_nhdsGT hε)).exists
      exact Relation.TransGen.head (hloc t htA.1 hst hts l hlpos hlε) hl
    · rw [hst]; exact htA.2
  have hs : sInf A = 0 := by
    by_contra hne0
    have hspos : 0 < sInf A := lt_of_le_of_ne hs0 (Ne.symm hne0)
    have hev : ∀ᶠ t in 𝓝 (sInf A), S.Chr (α t) z :=
      (hαc.tendsto _).eventually ((S.hl_isOpen_Ipast z).mem_nhds hsA)
    obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 hev
    have hm1 := min_le_left δ (sInf A)
    have hm2 := min_le_right δ (sInf A)
    have hm3 := lt_min hδ hspos
    have ht : sInf A - min δ (sInf A) / 2 ∈ A := by
      refine ⟨⟨by linarith, by linarith⟩, hδP ?_⟩
      rw [Real.dist_eq, abs_lt]; constructor <;> linarith
    have := csInf_le hbdd ht
    linarith
  rw [← h0, ← hs]; exact hsA

/-- **Push-up** `J⁻(I⁻(z)) ⊆ I⁻(z)`: `q ≤ p ≪ z ⟹ q ≪ z`, for locally Lipschitz `g`. -/
theorem hl_pushup (hL : LocallyLipschitzOn S.M S.g) {q p z : V} (hqp : S.Cau q p) (hpz : S.Chr p z) :
    S.Chr q z := by
  induction hqp using Relation.ReflTransGen.head_induction_on with
  | refl => exact hpz
  | head h _ ih => exact S.pushup_cstep hL h ih

/-! ### Time reversal, and the dual push-up `I⁻ ∘ J⁻ ⊆ I⁻` -/

/-- The time-reversed chart: same `g`, orientation `-T`. -/
def rev : Spacetime V where
  M := S.M
  isOpen_M := S.isOpen_M
  g := S.g
  cont_g := S.cont_g
  symm := S.symm
  T x := -S.T x
  cont_T := S.cont_T.neg
  T_timelike x hx := by simpa using S.T_timelike x hx
  pos_on_perp x hx v hv := S.pos_on_perp x hx v (by simpa using hv)

lemma rev_futTimelike (x v : V) : S.rev.FutTimelike x v ↔ S.FutTimelike x (-v) := by
  simp [FutTimelike, rev]

lemma rev_futCausal (x v : V) : S.rev.FutCausal x v ↔ S.FutCausal x (-v) := by
  simp [FutCausal, rev]

lemma reverse_curve {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) :
    ContDiff ℝ 1 (fun t => γ (1 - t)) ∧ ∀ t, deriv (fun t => γ (1 - t)) t = -deriv γ (1 - t) := by
  refine ⟨hγ.comp (contDiff_const.sub contDiff_id), fun t => ?_⟩
  have hin : HasDerivAt (fun t : ℝ => 1 - t) (0 - 1) t :=
    (hasDerivAt_const t (1:ℝ)).sub (hasDerivAt_id' t)
  have h : HasDerivAt (fun t => γ (1 - t)) (((0:ℝ) - 1) • deriv γ (1 - t)) t :=
    (hasDerivAt_of_contDiff hγ (1 - t)).scomp t hin
  rw [h.deriv, zero_sub, neg_one_smul]

lemma rev_tstep_iff (x y : V) : S.rev.TStep x y ↔ S.TStep y x := by
  constructor
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd]; exact (S.rev_futTimelike _ _).1 hf⟩
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd, S.rev_futTimelike, neg_neg]; exact hf⟩

lemma rev_cstep_iff (x y : V) : S.rev.CStep x y ↔ S.CStep y x := by
  constructor
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd]; exact (S.rev_futCausal _ _).1 hf⟩
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd, S.rev_futCausal, neg_neg]; exact hf⟩

theorem hl_rev_chr (x y : V) : S.rev.Chr x y ↔ S.Chr y x := by
  have e : S.rev.TStep = Function.swap S.TStep := by
    funext x y; exact propext (S.rev_tstep_iff x y)
  unfold Chr; rw [e]; exact Relation.transGen_swap

theorem hl_rev_cau (x y : V) : S.rev.Cau x y ↔ S.Cau y x := by
  have e : S.rev.CStep = Function.swap S.CStep := by
    funext x y; exact propext (S.rev_cstep_iff x y)
  unfold Cau; rw [e]; exact Relation.reflTransGen_swap

/-- **Dual push-up** `q ≪ p ≤ z ⟹ q ≪ z`, by time reversal. -/
theorem hl_pushup' (hL : LocallyLipschitzOn S.M S.g) {q p z : V} (hqp : S.Chr q p) (hpz : S.Cau p z) :
    S.Chr q z := by
  have h := S.rev.hl_pushup (z := q) hL ((S.hl_rev_cau z p).2 hpz) ((S.hl_rev_chr p q).2 hqp)
  exact (S.hl_rev_chr z q).1 h

/-! ### Temporal functions (campaign 60) -/

/-- **A temporal function, repaired (campaign 78, ⓪).** `τ` is `C¹` *on `M`* (not on the whole
chart `V`), with `dτ(v) > 0` for every future-causal `v` at points of `M`. Since `M` is open,
`fderiv ℝ τ x` at `x ∈ M` is the honest derivative of `τ|_M`.

*Change from campaigns 60/72/74/75:* those required `ContDiff ℝ 1 τ` on all of `V`. Applied to
`Dsp J` (whose `M` is `D`), that made `Θ` continuous at every horizon point, contradicting the
blow-up `Θ → ∞` along `𝓝[D] q`, `q ∈ 𝓗⁺`, that the Cauchy property forces (`r7641+71.1`,
`probes/VacuityCheck.lean`): the hypotheses were unsatisfiable whenever `𝓗⁺ ≠ ∅`. The repaired
definition constrains `τ` on `M` only (campaign 78's `cr_isTemporal_congr`, not copied), so no continuity across `∂M` is
imposed. -/
def IsTemporal (τ : V → ℝ) : Prop :=
  ContDiffOn ℝ 1 τ S.M ∧ ∀ x ∈ S.M, ∀ v, S.FutCausal x v → 0 < fderiv ℝ τ x v

/-- A `C¹` curve on `[0,1]` inside `M`, future-causal there, raises a temporal `τ` (repaired
definition: only `τ|_M` is used, via `ContDiffOn.contDiffAt` at the open `M`). -/
lemma temporal_curve {τ : V → ℝ} (hτ : S.IsTemporal τ) {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hγt : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t)) :
    τ (γ 0) < τ (γ 1) := by
  have hcont : ContinuousOn (τ ∘ γ) (Icc (0:ℝ) 1) :=
    hτ.1.continuousOn.comp hγ.continuous.continuousOn fun t ht => (hγt t ht).1
  have hmono : StrictMonoOn (τ ∘ γ) (Icc (0:ℝ) 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hcont fun t ht => ?_
    rw [interior_Icc] at ht
    have hti : t ∈ Icc (0:ℝ) 1 := Ioo_subset_Icc_self ht
    obtain ⟨hm, h12⟩ := hγt t hti
    have hdτ : DifferentiableAt ℝ τ (γ t) :=
      (hτ.1.contDiffAt (S.isOpen_M.mem_nhds hm)).differentiableAt one_ne_zero
    have hd : HasDerivAt (τ ∘ γ) (fderiv ℝ τ (γ t) (deriv γ t)) t :=
      hdτ.hasFDerivAt.comp_hasDerivAt t (hasDerivAt_of_contDiff hγ t)
    rw [hd.deriv]
    exact hτ.2 _ hm _ h12
  exact hmono ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one

lemma temporal_tstep {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.TStep x y) :
    τ x < τ y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have := S.temporal_curve hτ hγ fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩
  rwa [h0, h1] at this

/-- A temporal function increases strictly along `≪` (campaign 60's `hl_temporal_chr`). -/
theorem hl_temporal_chr {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.Chr x y) :
    τ x < τ y := by
  induction h with
  | single h => exact S.temporal_tstep hτ h
  | tail _ h ih => exact ih.trans (S.temporal_tstep hτ h)

/-! ### Exterior and horizon -/

variable (J : Set V)

/-- `D = I⁻(𝒥⁺)`. -/
def D : Set V := S.IpastSet J
/-- `𝓗⁺ = ∂J⁻(𝒥⁺)`. -/
def H : Set V := frontier (S.JpastSet J)
/-- A finite slice `S_τ = {x ∈ D | Θ x = τ}`. -/
def slice (Θ : V → ℝ) (τ : ℝ) : Set V := {x | x ∈ S.D J ∧ Θ x = τ}

theorem hl_D_subset_JpastSet : S.D J ⊆ S.JpastSet J :=
  biUnion_mono subset_rfl fun p _ => S.hl_Ipast_subset_Jpast p

end Spacetime

section KL
variable {X : Type*} [TopologicalSpace X]

/-- Kuratowski lower limit of a family of sets as `τ → ∞` (c2: on any topological space). -/
def KLi (A : ℝ → Set X) : Set X := {p | ∀ U ∈ 𝓝 p, ∀ᶠ τ in atTop, (A τ ∩ U).Nonempty}
/-- Kuratowski upper limit of a family of sets as `τ → ∞`. -/
def KLs (A : ℝ → Set X) : Set X := {p | ∀ U ∈ 𝓝 p, ∃ᶠ τ in atTop, (A τ ∩ U).Nonempty}

/-- `Li ⊆ Ls`. -/
theorem hl_KLi_subset_KLs (A : ℝ → Set X) : KLi A ⊆ KLs A :=
  fun _ hp U hU => (hp U hU).frequently

/-- c2: `Ls A ⊆ closure (⋃ A)`, for `A τ ⊆ B`. -/
theorem ch_KLs_subset_closure {A : ℝ → Set X} {B : Set X} (hAB : ∀ τ, A τ ⊆ B) :
    KLs A ⊆ closure B := by
  intro p hp
  rw [mem_closure_iff_nhds]
  intro U hU
  obtain ⟨τ, z, hz, hzU⟩ := (hp U hU).exists
  exact ⟨z, hzU, hAB τ hz⟩

end KL

namespace Spacetime
variable (S : Spacetime V) (J : Set V)

section Observer
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
  (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
include hOD hmono

omit hOD in
/-- `I⁻(O σ) ⊆ I⁻(O τ)` for `σ ≤ τ`. -/
theorem hl_Ipast_mono {σ τ : ℝ} (h : σ ≤ τ) : S.Ipast (O σ) ⊆ S.Ipast (O τ) := by
  rcases h.lt_or_eq with h | h
  · exact fun q hq => S.hl_chr_trans hq (hmono σ τ h)
  · rw [h]

/-- Each `O τ` lies in `D`. -/
theorem hl_observer_mem_D (τ : ℝ) : O τ ∈ S.D J := by
  rw [← hOD]
  exact mem_biUnion (mem_range_self (τ + 1)) (hmono τ (τ + 1) (by linarith))


end Observer

/-! ## Campaign 74: the slice lower limit

### Campaign 60's Cauchy-temporal definitions (copied) -/

/-- Points of `I⁻(z)` lie in `M` (campaign 60's `hl_Ipast_subset_M`). -/
theorem hl_Ipast_subset_M (z : V) : S.Ipast z ⊆ S.M := by
  intro q hq
  obtain ⟨b, ⟨γ, -, h0, -, hγ⟩, -⟩ := Relation.TransGen.head'_iff.1 hq
  rw [← h0]; exact (hγ 0 ⟨le_rfl, zero_le_one⟩).1

/-- `D` is open (campaign 60's `hl_D_open`). -/
theorem hl_D_open : IsOpen (S.D J) := isOpen_biUnion fun z _ => S.hl_isOpen_Ipast z

/-- `D ⊆ M` (campaign 60's `hl_D_subset_M`). -/
theorem hl_D_subset_M : S.D J ⊆ S.M := iUnion₂_subset fun z _ => S.hl_Ipast_subset_M z

/-- The same chart with `M` replaced by an open subset `U ⊆ M` (campaign 60). -/
def restrict (U : Set V) (hU : IsOpen U) (hUM : U ⊆ S.M) : Spacetime V where
  M := U
  isOpen_M := hU
  g := S.g
  cont_g := S.cont_g.mono hUM
  symm := S.symm
  T := S.T
  cont_T := S.cont_T.mono hUM
  T_timelike x hx := S.T_timelike x (hUM hx)
  pos_on_perp x hx := S.pos_on_perp x (hUM hx)

/-- A future-directed, inextendible, piecewise-`C¹` causal curve (campaign 60). -/
structure InextCausalCurve where
  γ : ℝ → V
  cont : Continuous γ
  mem : ∀ t, γ t ∈ S.M
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t ∉ brk, DifferentiableAt ℝ γ t ∧ S.FutCausal (γ t) (deriv γ t)
  inext_future : ¬ ∃ p ∈ S.M, Tendsto γ atTop (𝓝 p)
  inext_past : ¬ ∃ p ∈ S.M, Tendsto γ atBot (𝓝 p)

/-- A Cauchy temporal function (campaign 60): temporal, and every inextendible causal curve meets
every level set exactly once. -/
def IsCauchyTemporal (τ : V → ℝ) : Prop :=
  S.IsTemporal τ ∧ ∀ c : S.InextCausalCurve, ∀ a : ℝ, ∃! t : ℝ, τ (c.γ t) = a

/-- The exterior `D` regarded as a spacetime in its own right. -/
def Dsp : Spacetime V := S.restrict (S.D J) (S.hl_D_open J) (S.hl_D_subset_M J)

/-! ### `Θ` temporal on `D` only: increase along `≪` into `D`

This removes campaign 72's need for `Θ` temporal on all of `M`: a timelike step ending in `D` runs
inside `D`, so a function temporal on `D` (the paper's setting) increases along it. -/

/-- `≪` into `D` starts in `D`. -/
theorem hl_D_of_chr {x y : V} (h : S.Chr x y) (hy : y ∈ S.D J) : x ∈ S.D J := by
  simp only [D, IpastSet, mem_iUnion] at hy ⊢
  obtain ⟨z, hz, hyz⟩ := hy
  exact ⟨z, hz, S.hl_chr_trans h hyz⟩

/-- The tail `γ|[t,1]` of a timelike step, reparametrised onto `[0,1]`, is again a timelike step. -/
lemma tstep_tail {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hγt : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t))
    {t : ℝ} (ht : t ∈ Ico (0:ℝ) 1) : S.TStep (γ t) (γ 1) := by
  have hc : 0 < 1 - t := by linarith [ht.2]
  refine ⟨fun s => γ (t + s * (1 - t)),
    hγ.comp (contDiff_const.add (contDiff_id.mul contDiff_const)), by simp,
    by simp, fun s hs => ?_⟩
  have hmem : t + s * (1 - t) ∈ Icc (0:ℝ) 1 := by
    constructor <;> nlinarith [ht.1, hs.1, hs.2]
  have hd : deriv (fun s => γ (t + s * (1 - t))) s = (1 - t) • deriv γ (t + s * (1 - t)) := by
    have ha : HasDerivAt (fun s : ℝ => t + s * (1 - t)) (1 * (1 - t)) s :=
      ((hasDerivAt_id s).mul_const (1 - t)).const_add t
    have h := (hasDerivAt_of_contDiff hγ (t + s * (1 - t))).scomp s ha
    rw [one_mul] at h
    exact h.deriv
  obtain ⟨hm, h1, h2⟩ := hγt _ hmem
  refine ⟨hm, ?_, ?_⟩
  · rw [hd]
    simp only [map_smul, smul_apply, smul_eq_mul]
    have : 0 < (1 - t) * (1 - t) := mul_pos hc hc
    nlinarith
  · rw [hd]
    simp only [map_smul, smul_apply, smul_eq_mul]
    exact mul_neg_of_pos_of_neg hc h2

/-- A timelike step ending in `D` has every point in `D`. -/
lemma tstep_in_D {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hγt : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t))
    (hy : γ 1 ∈ S.D J) {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) : γ t ∈ S.D J := by
  rcases ht.2.lt_or_eq with h | h
  · exact S.hl_D_of_chr J (Relation.TransGen.single (S.tstep_tail hγ hγt ⟨ht.1, h⟩)) hy
  · rw [h]; exact hy

/-- A timelike step of `S` ending in `D` is a timelike step of `Dsp J`. -/
lemma tstep_Dsp {x y : V} (h : S.TStep x y) (hy : y ∈ S.D J) : (S.Dsp J).TStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨S.tstep_in_D J hγ hγt (h1 ▸ hy) ht, (hγt t ht).2⟩⟩

lemma temporalD_tstep {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {x y : V} (h : S.TStep x y)
    (hy : y ∈ S.D J) : Θ x < Θ y :=
  (S.Dsp J).temporal_tstep hΘ (S.tstep_Dsp J h hy)

/-- **A function temporal on `D` only increases along every `≪` ending in `D`.** -/
theorem hl_temporalD_chr {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {x y : V} (h : S.Chr x y)
    (hy : y ∈ S.D J) : Θ x < Θ y := by
  induction h with
  | single h => exact S.temporalD_tstep J hΘ h hy
  | @tail b c hxb hbc ih =>
    have hb : b ∈ S.D J := S.hl_D_of_chr J (Relation.TransGen.single hbc) hy
    exact (ih hb).trans (S.temporalD_tstep J hΘ hbc hy)

/-! ### ① `Θ → ∞` at the horizon, from a properness hypothesis -/

/-- **Properness of `Θ` on `D`**: no sublevel set `{x ∈ D | Θ x ≤ T}` accumulates outside `D`
(equivalently, for continuous `Θ`, every sublevel set is closed in `V`: campaign 78's `cr_sublevelProper_iff`, not copied).
This is the content of "`Θ` is a Cauchy time function of `D` whose levels do not reach `∂D`". -/
def SublevelProper (Θ : V → ℝ) : Prop := ∀ T : ℝ, closure {x | x ∈ S.D J ∧ Θ x ≤ T} ⊆ S.D J

/-- `𝓗⁺ ∩ D = ∅`: a horizon point is not in `D`. -/
theorem hl_not_mem_D_of_H {p : V} (hp : p ∈ S.H J) : p ∉ S.D J := fun hpD =>
  hp.2 (interior_maximal (S.hl_D_subset_JpastSet J) (S.hl_D_open J) hpD)

/-! ## Campaign 75: properness and the slice lower limit from the Cauchy property

### Step 1: `q ∈ closure D ⟹ I⁻(q) ⊆ D` -/

/-- The end of a timelike step can be moved in an open set (mirror of `tstep_start_eventually`). -/
lemma tstep_end_eventually {x q : V} (h : S.TStep x q) : ∀ᶠ q' in 𝓝 q, S.TStep x q' := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.tube (P := fun w t => γ t + t • w) (Q := fun w t => deriv γ t + w)
    ((hγ.continuous.comp continuous_snd).add (continuous_snd.smul continuous_fst))
    ((hdc.comp continuous_snd).add continuous_fst) (by simpa using hγt)
  have hlim : Tendsto (fun q' => q' - q) (𝓝 q) (𝓝 0) := tendsto_sub_nhds_zero_iff.2 tendsto_id
  filter_upwards [hlim.eventually hT] with q' hq'
  refine ⟨fun t => γ t + t • (q' - q), hγ.add (contDiff_id.smul contDiff_const), by simp [h0],
    by simp [h1], fun t ht => ?_⟩
  have hd : deriv (fun t => γ t + t • (q' - q)) t = deriv γ t + (q' - q) := by
    have h : HasDerivAt (fun t => γ t + t • (q' - q)) (deriv γ t + (1:ℝ) • (q' - q)) t :=
      (hasDerivAt_of_contDiff hγ t).add ((hasDerivAt_id' t).smul_const (q' - q))
    rw [h.deriv, one_smul]
  rw [hd]; exact hq' t ht

/-- `I⁺(x) = {y | x ≪ y}` is open. -/
theorem hl_isOpen_Ifut (x : V) : IsOpen {y | S.Chr x y} := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hxy, hyq⟩ := Relation.TransGen.tail'_iff.1 hq
  filter_upwards [S.tstep_end_eventually hyq] with q' hq'
  exact Relation.TransGen.tail' hxy hq'

/-- **Step 1.** `q ∈ closure D ⟹ I⁻(q) ⊆ D`: if `x ≪ q`, the open set `I⁺(x)` meets `D` at some
`d`, and `x ≪ d ∈ D` gives `x ∈ D`. -/
theorem hl_Ipast_subset_D {q : V} (hq : q ∈ closure (S.D J)) : S.Ipast q ⊆ S.D J := by
  intro x hx
  obtain ⟨d, hd, hdD⟩ := mem_closure_iff_nhds.1 hq _ ((S.hl_isOpen_Ifut x).mem_nhds hx)
  exact S.hl_D_of_chr J hd hdD

/-! ### Step 2: a timelike segment into `q` along `T(q)` -/

/-- The straight segment `r ↦ q + r • T(q)`. -/
def seg (q : V) (r : ℝ) : V := q + r • S.T q

lemma seg_zero (q : V) : S.seg q 0 = q := by simp [seg]

/-- Near `q ∈ M` the segment stays in `M` with `T(q)` future-timelike along it. -/
lemma seg_timelike {q : V} (hq : q ∈ S.M) : ∃ ε > 0, ∀ r ∈ Icc (-ε) 0,
    S.seg q r ∈ S.M ∧ S.FutTimelike (S.seg q r) (S.T q) := by
  have hc : Continuous fun r : ℝ => (S.seg q r, S.T q) :=
    (continuous_const.add (continuous_id.smul continuous_const)).prodMk continuous_const
  have hO := S.isOpen_timelikePairs.preimage hc
  have h0 : (0:ℝ) ∈ (fun r : ℝ => (S.seg q r, S.T q)) ⁻¹'
      {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
    show S.seg q 0 ∈ S.M ∧ S.FutTimelike (S.seg q 0) (S.T q)
    rw [seg_zero]; exact ⟨hq, S.T_timelike q hq, S.T_timelike q hq⟩
  obtain ⟨δ, hδ, hball⟩ := Metric.isOpen_iff.1 hO 0 h0
  refine ⟨δ / 2, by positivity, fun r hr => hball ?_⟩
  rw [mem_ball, Real.dist_eq, sub_zero, abs_lt]
  constructor <;> linarith [hr.1, hr.2]

/-- Along the segment, `seg q s ≪ seg q s'` (one timelike step) for `-ε ≤ s < s' ≤ 0`. -/
lemma seg_tstep {q : V} {a b : ℝ}
    (hε : ∀ r ∈ Icc a b, S.seg q r ∈ S.M ∧ S.FutTimelike (S.seg q r) (S.T q))
    {s s' : ℝ} (hs : a ≤ s) (hss : s < s') (hs' : s' ≤ b) :
    S.TStep (S.seg q s) (S.seg q s') := by
  have hc : 0 < s' - s := by linarith
  refine ⟨fun u => q + (s + u * (s' - s)) • S.T q, ?_, by simp [seg], by simp [seg], fun u hu => ?_⟩
  · exact contDiff_const.add
      ((contDiff_const.add (contDiff_id.mul contDiff_const)).smul contDiff_const)
  have hd : deriv (fun u => q + (s + u * (s' - s)) • S.T q) u = (s' - s) • S.T q := by
    have h : HasDerivAt (fun u => q + (s + u * (s' - s)) • S.T q) ((1 * (s' - s)) • S.T q) u :=
      ((((hasDerivAt_id u).mul_const (s' - s)).const_add s).smul_const (S.T q)).const_add q
    rw [h.deriv, one_mul]
  have hmem : s + u * (s' - s) ∈ Icc a b := by
    constructor <;> nlinarith [hu.1, hu.2]
  obtain ⟨hm, h1, h2⟩ := hε _ hmem
  refine ⟨hm, ?_, ?_⟩
  · rw [hd]
    simp only [map_smul, smul_apply, smul_eq_mul]
    have : 0 < (s' - s) * (s' - s) := mul_pos hc hc
    exact (by nlinarith : (s' - s) * ((s' - s) * S.g (S.seg q (s + u * (s' - s))) (S.T q) (S.T q)) < 0)
  · rw [hd]
    simp only [map_smul, smul_apply, smul_eq_mul]
    exact mul_neg_of_pos_of_neg hc h2

/-! ### Step 3: the Cauchy property, future-inextendible form -/

/-- A future-directed piecewise-`C¹` causal curve on `[0, ∞)`, future-inextendible in `M`
(the future half of campaign 60's `InextCausalCurve`). -/
structure FutInextCurve where
  γ : ℝ → V
  cont : ContinuousOn γ (Ici 0)
  mem : ∀ t, 0 ≤ t → γ t ∈ S.M
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t, 0 < t → t ∉ brk → DifferentiableAt ℝ γ t ∧ S.FutCausal (γ t) (deriv γ t)
  inext_future : ¬ ∃ p ∈ S.M, Tendsto γ atTop (𝓝 p)

/-- **Cauchy temporal, future form**: `Θ` is temporal, and every future-inextendible causal curve
from `γ 0` attains every level `a ≥ Θ (γ 0)`. Campaign 78: implied by campaign 60's
`IsCauchyTemporal` (`hl_futCauchy_of_cauchy`, ②), and together with the past form equivalent to it
(`hl_cauchy_iff`). -/
def FutCauchyTemporal (Θ : V → ℝ) : Prop :=
  S.IsTemporal Θ ∧ ∀ c : S.FutInextCurve, ∀ a : ℝ, Θ (c.γ 0) ≤ a → ∃ t, 0 ≤ t ∧ Θ (c.γ t) = a


/-! ## Campaign 78 ①: a polygonal past-inextendible extension

Generic in the spacetime `S` (applied below to `Dsp J`, whose `M` is `D`). Vertices
`X 0 = x`, `X (k+1) = X k - ℓ_k • T(X k)`, with the **dyadic safe length**
`ℓ_k = 2^{-n}` for the least `n` such that the segment `X k + r • T(X k)`, `r ∈ [-2^{-n}, 0]`, stays
in `M` and `T(X k)` is future-timelike along it. (The registered "largest safe `ℓ`" supremum is
replaced by this `Nat.find`, the registered fallback; it is locally bounded below by the tube
lemma, `safe_uniform`.) Piece `k` is traversed on `t ∈ [-(k+1), -k]`, so the breaks are integers. -/

/-- `Safe y ℓ`: on `r ∈ [-ℓ, 0]`, `y + r • T y ∈ M` and `T y` is future-timelike there. -/
def Safe (y : V) (ℓ : ℝ) : Prop :=
  ∀ r ∈ Icc (-ℓ) 0, S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y)

lemma safe_mono {y : V} {ℓ ℓ' : ℝ} (h : S.Safe y ℓ) (hl : ℓ' ≤ ℓ) : S.Safe y ℓ' :=
  fun r hr => h r ⟨by linarith [hr.1], hr.2⟩

/-- **Tube lemma: a locally uniform safe length.** -/
lemma safe_uniform {x : V} (hx : x ∈ S.M) : ∃ ℓ > 0, ∀ᶠ y in 𝓝 x, S.Safe y ℓ := by
  obtain ⟨ε, hε0, hε⟩ := S.seg_timelike hx
  refine ⟨ε, hε0, ?_⟩
  have hc : ∀ r : ℝ, ContinuousAt (fun z : V × ℝ => (S.seg z.1 z.2, S.T z.1)) (x, r) := fun r =>
    (continuousAt_fst.add (continuousAt_snd.smul ((S.contAt_T hx).comp continuousAt_fst))).prodMk
      ((S.contAt_T hx).comp continuousAt_fst)
  exact isCompact_Icc.eventually_forall_of_forall_eventually
    (P := fun y r => S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y))
    fun r hr => (hc r).preimage_mem_nhds (S.isOpen_timelikePairs.mem_nhds (hε r hr))

lemma exists_safe_pow {y : V} (hy : y ∈ S.M) : ∃ n : ℕ, S.Safe y ((1/2:ℝ) ^ n) := by
  obtain ⟨ε, hε0, hε⟩ := S.seg_timelike hy
  obtain ⟨n, hn⟩ := exists_pow_lt_of_lt_one hε0 (by norm_num : (1/2:ℝ) < 1)
  exact ⟨n, S.safe_mono hε hn.le⟩

open Classical in
/-- The dyadic safe length (`1` off `M`, where it is never used). -/
noncomputable def safeLen (y : V) : ℝ :=
  if h : ∃ n : ℕ, S.Safe y ((1/2:ℝ) ^ n) then (1/2:ℝ) ^ (Nat.find h) else 1

lemma safeLen_pos (y : V) : 0 < S.safeLen y := by
  unfold safeLen; split_ifs <;> positivity

open Classical in
lemma safeLen_safe {y : V} (hy : y ∈ S.M) : S.Safe y (S.safeLen y) := by
  have h := S.exists_safe_pow hy
  unfold safeLen; split_ifs with h'
  · exact Nat.find_spec h'
  · exact absurd h h'

open Classical in
lemma safeLen_ge {y : V} {m : ℕ} (h : S.Safe y ((1/2:ℝ) ^ m)) : (1/2:ℝ) ^ m ≤ S.safeLen y := by
  have he : ∃ n : ℕ, S.Safe y ((1/2:ℝ) ^ n) := ⟨m, h⟩
  unfold safeLen; split_ifs with h'
  · exact pow_le_pow_of_le_one (by norm_num) (by norm_num) (Nat.find_min' h' h)
  · exact absurd he h'

/-- The vertices of the polygon. -/
noncomputable def pvert (x : V) : ℕ → V
  | 0 => x
  | k + 1 => S.seg (pvert x k) (-S.safeLen (pvert x k))

lemma pvert_succ_sub (x : V) (k : ℕ) :
    S.pvert x (k + 1) - S.pvert x k = (-S.safeLen (S.pvert x k)) • S.T (S.pvert x k) := by
  simp [pvert, seg]

lemma pvert_mem {x : V} (hx : x ∈ S.M) : ∀ k, S.pvert x k ∈ S.M
  | 0 => hx
  | k + 1 => (S.safeLen_safe (pvert_mem hx k) _
      ⟨le_rfl, neg_nonpos.2 (S.safeLen_pos _).le⟩).1

lemma pvert_tstep {x : V} (hx : x ∈ S.M) (k : ℕ) : S.TStep (S.pvert x (k + 1)) (S.pvert x k) := by
  have h := S.seg_tstep (S.safeLen_safe (S.pvert_mem hx k)) le_rfl
    (neg_lt_zero.2 (S.safeLen_pos _)) le_rfl
  rwa [seg_zero] at h

lemma pvert_rtg {x : V} (hx : x ∈ S.M) : ∀ k, Relation.ReflTransGen S.TStep (S.pvert x k) x
  | 0 => Relation.ReflTransGen.refl
  | k + 1 => Relation.ReflTransGen.head (S.pvert_tstep hx k) (pvert_rtg hx k)

/-- Piece `k` as a function of `u = -t`. -/
noncomputable def ppiece (x : V) (k : ℕ) (u : ℝ) : V :=
  S.pvert x k + (u - k) • (S.pvert x (k + 1) - S.pvert x k)

lemma ppiece_continuous (x : V) (k : ℕ) : Continuous (S.ppiece x k) :=
  continuous_const.add ((continuous_id.sub continuous_const).smul continuous_const)

lemma ppiece_eq_seg (x : V) (k : ℕ) (u : ℝ) :
    S.ppiece x k u = S.seg (S.pvert x k) (-((u - k) * S.safeLen (S.pvert x k))) := by
  rw [ppiece, pvert_succ_sub, smul_smul, seg]; ring_nf

/-- The polygon, as a function of `u = -t` (`Nat.floor` makes it piece `0` for `u < 0`). -/
noncomputable def ppoly (x : V) (u : ℝ) : V := S.ppiece x ⌊u⌋₊ u

lemma ppoly_eq (x : V) (k : ℕ) {u : ℝ} (h1 : (k:ℝ) ≤ u ∨ k = 0) (h2 : u ≤ k + 1) :
    S.ppoly x u = S.ppiece x k u := by
  rcases h2.lt_or_eq with h2 | h2
  · have hk : ⌊u⌋₊ = k := by
      by_cases hu : 0 ≤ u
      · rw [Nat.floor_eq_iff hu]
        rcases h1 with h1 | h1
        · exact ⟨h1, h2⟩
        · subst h1; exact ⟨by simpa using hu, h2⟩
      · rw [Nat.floor_eq_zero.2 (by linarith)]
        rcases h1 with h1 | h1
        · exact absurd (le_trans (Nat.cast_nonneg k) h1) hu
        · exact h1.symm
    rw [ppoly, hk]
  · have hk : ⌊u⌋₊ = k + 1 := by rw [h2]; exact_mod_cast Nat.floor_natCast (k + 1)
    rw [ppoly, hk, ppiece, ppiece, h2]
    simp

lemma ppoly_continuous (x : V) : Continuous (S.ppoly x) := by
  rw [continuous_iff_continuousAt]
  intro u
  by_cases hu1 : u < 1
  · refine (S.ppiece_continuous x 0).continuousAt.congr ?_
    filter_upwards [Iio_mem_nhds hu1] with v hv
    exact (S.ppoly_eq x 0 (Or.inr rfl) (by simpa using hv.le)).symm
  set n := ⌊u⌋₊ with hn
  have hnu : (n:ℝ) ≤ u := Nat.floor_le (by linarith)
  have hun : u < n + 1 := Nat.lt_floor_add_one u
  by_cases hne : (n:ℝ) < u
  · refine (S.ppiece_continuous x n).continuousAt.congr ?_
    filter_upwards [Ioo_mem_nhds hne hun] with v hv
    exact (S.ppoly_eq x n (Or.inl hv.1.le) hv.2.le).symm
  have hequ : u = n := le_antisymm (not_lt.1 hne) hnu
  have hn1 : 1 ≤ n := by
    by_contra h
    have : n = 0 := by omega
    rw [this] at hequ; norm_num at hequ; linarith
  obtain ⟨k, hk⟩ : ∃ k, n = k + 1 := ⟨n - 1, by omega⟩
  rw [hk] at hequ
  push_cast at hequ
  have hA : ContinuousWithinAt (S.ppoly x) (Icc (k:ℝ) (k + 1)) u :=
    (S.ppiece_continuous x k).continuousWithinAt.congr
      (fun v hv => S.ppoly_eq x k (Or.inl hv.1) hv.2) (S.ppoly_eq x k (Or.inl (by linarith)) hequ.le)
  have hB : ContinuousWithinAt (S.ppoly x) (Icc ((k:ℝ) + 1) (k + 1 + 1)) u :=
    (S.ppiece_continuous x (k + 1)).continuousWithinAt.congr
      (fun v hv => S.ppoly_eq x (k + 1) (Or.inl (by push_cast; exact hv.1)) (by push_cast; exact hv.2))
      (S.ppoly_eq x (k + 1) (Or.inl (by push_cast; linarith)) (by push_cast; linarith))
  refine (hA.union hB).continuousAt (mem_of_superset (Ioo_mem_nhds (a := (k:ℝ))
    (b := k + 1 + 1) (by linarith) (by linarith)) fun v hv => ?_)
  rcases le_total v (k + 1) with h | h
  · exact Or.inl ⟨hv.1.le, h⟩
  · exact Or.inr ⟨h, hv.2.le⟩

/-- On piece `k`, the polygon point is on the safe segment of `X k`. -/
lemma ppoly_seg {x : V} (k : ℕ) {u : ℝ} (h1 : (k:ℝ) ≤ u) (h2 : u ≤ k + 1) :
    S.ppoly x u = S.seg (S.pvert x k) (-((u - k) * S.safeLen (S.pvert x k))) ∧
      -((u - k) * S.safeLen (S.pvert x k)) ∈ Icc (-S.safeLen (S.pvert x k)) 0 := by
  refine ⟨by rw [S.ppoly_eq x k (Or.inl h1) h2, ppiece_eq_seg], ?_⟩
  have hl := S.safeLen_pos (S.pvert x k)
  constructor <;> nlinarith

/-- The integers, as break points, are finite on compacts. -/
lemma int_brk_fin (a b : ℝ) : (range (Int.cast : ℤ → ℝ) ∩ Icc a b).Finite := by
  refine ((Set.finite_Icc ⌊a⌋ ⌈b⌉).image (Int.cast : ℤ → ℝ)).subset ?_
  rintro _ ⟨⟨z, rfl⟩, hz1, hz2⟩
  refine ⟨z, ⟨?_, ?_⟩, rfl⟩
  · exact Int.floor_le_iff.2 (by linarith)
  · exact Int.le_ceil_iff.2 (by linarith) 

/-- **① BUILT. A polygonal past-inextendible extension.** From any `x ∈ M` there is a continuous
`p : ℝ → V` with `p 0 = x`, `p t ∈ M` and `p t ≪ x` for `t < 0`, `C¹` and future-timelike (so
future-causal) off the integers on `t < 0`, and with no past limit in `M`.

*Joint satisfiability:* the only hypothesis is `x ∈ M` (e.g. any point of `D` for `Dsp J`).

*No past limit:* if `p t → x* ∈ M` as `t → -∞`, then `X k → x*`, the tube lemma at `x*` bounds
`ℓ_k ≥ 2^{-m}` eventually, and `‖X (k+1) - X k‖ = ℓ_k ‖T (X k)‖ → 0` contradicts
`‖T (X k)‖ → ‖T x*‖ > 0`. -/
theorem hl_past_extension {x : V} (hx : x ∈ S.M) :
    ∃ p : ℝ → V, Continuous p ∧ p 0 = x ∧ (∀ t ≤ 0, p t ∈ S.M) ∧ (∀ t < 0, S.Chr (p t) x) ∧
      (∀ t < 0, t ∉ range (Int.cast : ℤ → ℝ) →
        DifferentiableAt ℝ p t ∧ S.FutTimelike (p t) (deriv p t)) ∧
      ¬ ∃ q ∈ S.M, Tendsto p atBot (𝓝 q) := by
  refine ⟨fun t => S.ppoly x (-t), (S.ppoly_continuous x).comp continuous_neg, ?_, ?_, ?_, ?_, ?_⟩
  · show S.ppoly x (-0) = x
    rw [neg_zero, S.ppoly_eq x 0 (Or.inr rfl) (by norm_num), ppiece]; simp [pvert]
  · intro t ht
    set u := -t
    have hu : 0 ≤ u := by simp [u]; linarith
    obtain ⟨hs, hr⟩ := S.ppoly_seg (x := x) ⌊u⌋₊ (Nat.floor_le hu) (Nat.lt_floor_add_one u).le
    show S.ppoly x u ∈ S.M
    rw [hs]; exact (S.safeLen_safe (S.pvert_mem hx _) _ hr).1
  · intro t ht
    set u := -t
    have hu : 0 < u := by simp [u]; linarith
    set k := ⌈u⌉₊ - 1
    have hc1 : 1 ≤ ⌈u⌉₊ := Nat.one_le_iff_ne_zero.2 (by positivity)
    have hk : (k:ℝ) + 1 = ⌈u⌉₊ := by simp only [k]; push_cast [Nat.cast_sub hc1]; ring
    have h1 : (k:ℝ) < u := by linarith [Nat.ceil_lt_add_one hu.le]
    have h2 : u ≤ k + 1 := hk ▸ Nat.le_ceil u
    obtain ⟨hs, hr⟩ := S.ppoly_seg (x := x) k h1.le h2
    show S.Chr (S.ppoly x u) x
    rw [hs]
    have hl := S.safeLen_pos (S.pvert x k)
    have hst := S.seg_tstep (S.safeLen_safe (S.pvert_mem hx k)) hr.1
      (by have : 0 < (u - k) * S.safeLen (S.pvert x k) := mul_pos (by linarith) hl
          linarith) le_rfl
    rw [seg_zero] at hst
    exact Relation.TransGen.head' hst (S.pvert_rtg hx k)
  · intro t ht hbrk
    set u := -t with hu_def
    have hu : 0 < u := by simp [u]; linarith
    set n := ⌊u⌋₊
    have hnu : (n:ℝ) ≤ u := Nat.floor_le hu.le
    have hun : u < n + 1 := Nat.lt_floor_add_one u
    have hne : (n:ℝ) < u := by
      refine lt_of_le_of_ne hnu fun h => hbrk ⟨-(n:ℤ), ?_⟩
      push_cast; rw [h, hu_def, neg_neg]
    have hev : (fun t => S.ppoly x (-t)) =ᶠ[𝓝 t] fun s => S.ppiece x n (-s) := by
      filter_upwards [(continuous_neg.tendsto t).eventually (Ioo_mem_nhds hne hun)] with s hs
      exact S.ppoly_eq x n (Or.inl hs.1.le) hs.2.le
    have hd : HasDerivAt (fun s => S.ppiece x n (-s))
        (S.safeLen (S.pvert x n) • S.T (S.pvert x n)) t := by
      have h := (((hasDerivAt_neg t).sub_const (n:ℝ)).smul_const
        (S.pvert x (n + 1) - S.pvert x n)).const_add (S.pvert x n)
      rw [pvert_succ_sub, smul_smul] at h
      simpa [ppiece, pvert_succ_sub] using h
    refine ⟨hd.differentiableAt.congr_of_eventuallyEq hev, ?_⟩
    rw [hev.deriv_eq, hd.deriv]
    obtain ⟨hs, hr⟩ := S.ppoly_seg (x := x) n hnu hun.le
    obtain ⟨-, h1, h2⟩ := S.safeLen_safe (S.pvert_mem hx n) _ hr
    have hl := S.safeLen_pos (S.pvert x n)
    show S.FutTimelike (S.ppoly x u) _
    rw [hs]
    refine ⟨?_, ?_⟩ <;> simp only [map_smul, smul_apply, smul_eq_mul]
    · have : 0 < S.safeLen (S.pvert x n) * S.safeLen (S.pvert x n) := mul_pos hl hl
      nlinarith
    · exact mul_neg_of_pos_of_neg hl h2
  · rintro ⟨q, hq, hlim⟩
    have hX : Tendsto (S.pvert x) atTop (𝓝 q) := by
      have h := hlim.comp (tendsto_neg_atTop_atBot.comp tendsto_natCast_atTop_atTop)
      refine h.congr fun k => ?_
      show S.ppoly x (-(-(k:ℝ))) = S.pvert x k
      rw [neg_neg, S.ppoly_eq x k (Or.inl le_rfl) (by linarith)]; simp [ppiece]
    obtain ⟨ℓ₀, hℓ₀, hsafe⟩ := S.safe_uniform hq
    obtain ⟨m, hm⟩ := exists_pow_lt_of_lt_one hℓ₀ (by norm_num : (1/2:ℝ) < 1)
    set c : ℝ := (1/2:ℝ) ^ m
    have hc : 0 < c := by positivity
    have hTq : 0 < ‖S.T q‖ := norm_pos_iff.2 fun h0 => by
      have := S.T_timelike q hq; rw [h0] at this; simp at this
    have hev1 : ∀ᶠ k in atTop, c ≤ S.safeLen (S.pvert x k) :=
      (hX.eventually hsafe).mono fun k hk => S.safeLen_ge (S.safe_mono hk hm.le)
    have hev2 : ∀ᶠ k in atTop, ‖S.T q‖ / 2 < ‖S.T (S.pvert x k)‖ :=
      ((S.contAt_T hq).tendsto.comp hX).norm.eventually (lt_mem_nhds (by linarith))
    have hdiff : Tendsto (fun k => S.pvert x (k + 1) - S.pvert x k) atTop (𝓝 0) := by
      have := (hX.comp (tendsto_add_atTop_nat 1)).sub hX
      rwa [sub_self] at this
    have hev3 : ∀ᶠ k in atTop, ‖S.pvert x (k + 1) - S.pvert x k‖ < c * (‖S.T q‖ / 2) :=
      hdiff.norm.eventually (by rw [norm_zero]; exact gt_mem_nhds (show (0:ℝ) < c * (‖S.T q‖ / 2) by positivity))
    obtain ⟨k, h1, h2, h3⟩ := (hev1.and (hev2.and hev3)).exists
    rw [pvert_succ_sub, norm_smul, Real.norm_eq_abs, abs_neg,
      abs_of_pos (S.safeLen_pos _)] at h3
    have : c * (‖S.T q‖ / 2) ≤ S.safeLen (S.pvert x k) * ‖S.T (S.pvert x k)‖ :=
      mul_le_mul h1 h2.le (by positivity) (S.safeLen_pos _).le
    linarith

/-! ## Campaign 78 ②: two-sided Cauchy ⇒ future form -/

/-- **② BUILT. Campaign 60's two-sided Cauchy property implies the future form** (both with the
repaired `IsTemporal`), in any spacetime. A future-inextendible curve `c` is glued at `0` to the
polygonal past extension of `c.γ 0` (①); the glued curve is inextendible, so it meets level `a`
exactly once, and since `Θ` strictly increases along `≪` the hit of `a ≥ Θ (c.γ 0)` is at `t ≥ 0`.

*Joint satisfiability:* a single hypothesis, `IsCauchyTemporal Θ`; e.g. in Minkowski space the
time coordinate is Cauchy temporal (standard; not formalised here). -/
theorem hl_futCauchy_of_cauchy {Θ : V → ℝ} (hΘ : S.IsCauchyTemporal Θ) : S.FutCauchyTemporal Θ := by
  refine ⟨hΘ.1, fun c a ha => ?_⟩
  obtain ⟨p, hpc, hp0, hpM, hpchr, hpd, hpinext⟩ := S.hl_past_extension (c.mem 0 le_rfl)
  set γ : ℝ → V := fun t => if t ≤ 0 then p t else c.γ t with hγ
  have hγc : Continuous γ :=
    continuous_if_le (f := fun t : ℝ => t) (g := fun _ => (0:ℝ)) continuous_id continuous_const
      hpc.continuousOn c.cont fun t (ht : t = 0) => by rw [ht, hp0]
  have hγneg : ∀ t ≤ 0, γ t = p t := fun t ht => by simp [hγ, ht]
  have hγpos : ∀ t, 0 < t → γ t = c.γ t := fun t ht => by simp [hγ, not_le.2 ht]
  have hγ0 : ∀ t, 0 ≤ t → γ t = c.γ t := by
    intro t ht
    rcases ht.lt_or_eq with h | h
    · exact hγpos t h
    · rw [← h, hγneg 0 le_rfl, hp0]
  let C : S.InextCausalCurve :=
    { γ := γ
      cont := hγc
      mem := fun t => by
        rcases le_or_gt t 0 with h | h
        · rw [hγneg t h]; exact hpM t h
        · rw [hγpos t h]; exact c.mem t h.le
      brk := c.brk ∪ range (Int.cast : ℤ → ℝ)
      brk_fin := fun a b => by
        rw [union_inter_distrib_right]; exact (c.brk_fin a b).union (int_brk_fin a b)
      causal := fun t ht => by
        have ht0 : t ≠ 0 := fun h => ht (Or.inr ⟨0, by simp [h]⟩)
        rcases lt_or_gt_of_ne ht0 with h | h
        · have hev : γ =ᶠ[𝓝 t] p := by
            filter_upwards [Iio_mem_nhds h] with s hs using hγneg s hs.le
          obtain ⟨hd, hft⟩ := hpd t h fun hb => ht (Or.inr hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [hev.deriv_eq, hγneg t h.le]; exact ⟨hft.1.le, hft.2⟩
        · have hev : γ =ᶠ[𝓝 t] c.γ := by
            filter_upwards [Ioi_mem_nhds h] with s hs using hγpos s hs
          obtain ⟨hd, hft⟩ := c.causal t h fun hb => ht (Or.inl hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [hev.deriv_eq, hγpos t h]; exact hft
      inext_future := by
        rintro ⟨q, hq, hlim⟩
        refine c.inext_future ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_gt_atTop 0] with s hs using hγpos s hs
      inext_past := by
        rintro ⟨q, hq, hlim⟩
        refine hpinext ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_le_atBot 0] with s hs using hγneg s hs }
  obtain ⟨t, ht, -⟩ := hΘ.2 C a
  change Θ (γ t) = a at ht
  rcases lt_or_ge t 0 with h | h
  · rw [hγneg t h.le] at ht
    have := S.hl_temporal_chr hΘ.1 (hpchr t h)
    linarith
  · exact ⟨t, h, by rw [← hγ0 t h]; exact ht⟩


/-! ## Campaign 78, stretch: two-sided ⇔ future ∧ past

The past form, by time reversal: `rev` flips `T`, so `rev`'s polygonal past extension (①) is a
future extension of `S`. -/

/-- A future-directed piecewise-`C¹` causal curve on `(-∞, 0]`, past-inextendible in `M`. -/
structure PastInextCurve where
  γ : ℝ → V
  cont : ContinuousOn γ (Iic 0)
  mem : ∀ t, t ≤ 0 → γ t ∈ S.M
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t, t < 0 → t ∉ brk → DifferentiableAt ℝ γ t ∧ S.FutCausal (γ t) (deriv γ t)
  inext_past : ¬ ∃ p ∈ S.M, Tendsto γ atBot (𝓝 p)

/-- **Cauchy temporal, past form**: every past-inextendible causal curve ending at `γ 0` attains
every level `a ≤ Θ (γ 0)`. -/
def PastCauchyTemporal (Θ : V → ℝ) : Prop :=
  S.IsTemporal Θ ∧ ∀ c : S.PastInextCurve, ∀ a : ℝ, a ≤ Θ (c.γ 0) → ∃ t, t ≤ 0 ∧ Θ (c.γ t) = a

/-- **Future polygonal extension** (① for `rev`, reversed): from `x ∈ M`, a continuous `p` with
`p 0 = x`, `x ≪ p t` for `t > 0`, future-timelike off the integers, no future limit in `M`. -/
theorem hl_future_extension {x : V} (hx : x ∈ S.M) :
    ∃ p : ℝ → V, Continuous p ∧ p 0 = x ∧ (∀ t, 0 ≤ t → p t ∈ S.M) ∧
      (∀ t, 0 < t → S.Chr x (p t)) ∧
      (∀ t, 0 < t → t ∉ range (Int.cast : ℤ → ℝ) →
        DifferentiableAt ℝ p t ∧ S.FutTimelike (p t) (deriv p t)) ∧
      ¬ ∃ q ∈ S.M, Tendsto p atTop (𝓝 q) := by
  obtain ⟨p, hpc, hp0, hpM, hpchr, hpd, hpinext⟩ := S.rev.hl_past_extension (x := x) hx
  refine ⟨fun t => p (-t), hpc.comp continuous_neg, by simp [hp0],
    fun t ht => hpM (-t) (by linarith), fun t ht => (S.hl_rev_chr _ _).1 (hpchr (-t) (by linarith)),
    fun t ht hb => ?_, ?_⟩
  · have hb' : -t ∉ range (Int.cast : ℤ → ℝ) := fun ⟨z, hz⟩ =>
      hb ⟨-z, by push_cast; rw [hz, neg_neg]⟩
    obtain ⟨hd, hft⟩ := hpd (-t) (by linarith) hb'
    have hD : HasDerivAt (fun t => p (-t)) (-deriv p (-t)) t := by
      have := hd.hasDerivAt.scomp t (hasDerivAt_neg t)
      simpa [Function.comp_def] using this
    exact ⟨hD.differentiableAt, hD.deriv ▸ (S.rev_futTimelike _ _).1 hft⟩
  · rintro ⟨q, hq, hlim⟩
    exact hpinext ⟨q, hq, by simpa [Function.comp_def] using hlim.comp tendsto_neg_atBot_atTop⟩

/-- **Two-sided ⇒ past form** (mirror of ②, gluing the future extension at `0`). -/
theorem hl_pastCauchy_of_cauchy {Θ : V → ℝ} (hΘ : S.IsCauchyTemporal Θ) :
    S.PastCauchyTemporal Θ := by
  refine ⟨hΘ.1, fun c a ha => ?_⟩
  obtain ⟨p, hpc, hp0, hpM, hpchr, hpd, hpinext⟩ := S.hl_future_extension (c.mem 0 le_rfl)
  set γ : ℝ → V := fun t => if t ≤ 0 then c.γ t else p t with hγ
  have hγc : Continuous γ :=
    continuous_if_le (f := fun t : ℝ => t) (g := fun _ => (0:ℝ)) continuous_id continuous_const
      c.cont hpc.continuousOn fun t (ht : t = 0) => by rw [ht, hp0]
  have hγneg : ∀ t ≤ 0, γ t = c.γ t := fun t ht => by simp [hγ, ht]
  have hγpos : ∀ t, 0 < t → γ t = p t := fun t ht => by simp [hγ, not_le.2 ht]
  let C : S.InextCausalCurve :=
    { γ := γ
      cont := hγc
      mem := fun t => by
        rcases le_or_gt t 0 with h | h
        · rw [hγneg t h]; exact c.mem t h
        · rw [hγpos t h]; exact hpM t h.le
      brk := c.brk ∪ range (Int.cast : ℤ → ℝ)
      brk_fin := fun a b => by
        rw [union_inter_distrib_right]; exact (c.brk_fin a b).union (int_brk_fin a b)
      causal := fun t ht => by
        have ht0 : t ≠ 0 := fun h => ht (Or.inr ⟨0, by simp [h]⟩)
        rcases lt_or_gt_of_ne ht0 with h | h
        · have hev : γ =ᶠ[𝓝 t] c.γ := by
            filter_upwards [Iio_mem_nhds h] with s hs using hγneg s hs.le
          obtain ⟨hd, hft⟩ := c.causal t h fun hb => ht (Or.inl hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [hev.deriv_eq, hγneg t h.le]; exact hft
        · have hev : γ =ᶠ[𝓝 t] p := by
            filter_upwards [Ioi_mem_nhds h] with s hs using hγpos s hs
          obtain ⟨hd, hft⟩ := hpd t h fun hb => ht (Or.inr hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [hev.deriv_eq, hγpos t h]; exact ⟨hft.1.le, hft.2⟩
      inext_future := by
        rintro ⟨q, hq, hlim⟩
        refine hpinext ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_gt_atTop 0] with s hs using hγpos s hs
      inext_past := by
        rintro ⟨q, hq, hlim⟩
        refine c.inext_past ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_le_atBot 0] with s hs using hγneg s hs }
  obtain ⟨t, ht, -⟩ := hΘ.2 C a
  change Θ (γ t) = a at ht
  rcases le_or_gt t 0 with h | h
  · exact ⟨t, h, by rw [← hγneg t h]; exact ht⟩
  · rw [hγpos t h] at ht
    have := S.hl_temporal_chr hΘ.1 (hpchr t h)
    linarith

/-- A continuous `f` with `f' > 0` off a set `B` finite on bounded intervals is strictly
increasing on every `[a, b]` (induction on the number of breaks). -/
lemma strictMonoOn_of_brk {f : ℝ → ℝ} {B : Set ℝ} (hf : Continuous f)
    (hd : ∀ x ∉ B, 0 < deriv f x) :
    ∀ n : ℕ, ∀ a b : ℝ, (B ∩ Ioo a b).Finite → (B ∩ Ioo a b).ncard ≤ n →
      StrictMonoOn f (Icc a b) := by
  have base : ∀ a b : ℝ, B ∩ Ioo a b = ∅ → StrictMonoOn f (Icc a b) := fun a b hE =>
    strictMonoOn_of_deriv_pos (convex_Icc a b) hf.continuousOn fun x hx => hd x fun hxB => by
      rw [interior_Icc] at hx
      have : x ∈ B ∩ Ioo a b := ⟨hxB, hx⟩
      rw [hE] at this; exact this
  intro n
  induction n with
  | zero =>
    intro a b hfin hn
    exact base a b ((Set.ncard_eq_zero hfin).1 (Nat.le_zero.1 hn))
  | succ n ih =>
    intro a b hfin hn
    rcases (B ∩ Ioo a b).eq_empty_or_nonempty with hE | ⟨c, hcB, hc⟩
    · exact base a b hE
    have hsub : ∀ a' b' : ℝ, a ≤ a' → b' ≤ b → c ∉ Ioo a' b' →
        StrictMonoOn f (Icc a' b') := by
      intro a' b' ha hb hcn
      have hs : B ∩ Ioo a' b' ⊆ B ∩ Ioo a b :=
        inter_subset_inter_right _ (Ioo_subset_Ioo ha hb)
      have hss : B ∩ Ioo a' b' ⊂ B ∩ Ioo a b :=
        (Set.ssubset_iff_of_subset hs).2 ⟨c, ⟨hcB, hc⟩, fun h => hcn h.2⟩
      exact ih a' b' (hfin.subset hs) (Nat.lt_succ_iff.1 ((Set.ncard_lt_ncard hss hfin).trans_le hn))
    have h1 := hsub a c le_rfl hc.2.le fun h => lt_irrefl c h.2
    have h2 := hsub c b hc.1.le le_rfl fun h => lt_irrefl c h.1
    have := h1.union h2 (isGreatest_Icc hc.1.le) (isLeast_Icc hc.2.le)
    rwa [Icc_union_Icc_eq_Icc hc.1.le hc.2.le] at this

/-- A temporal `Θ` strictly increases along every inextendible causal curve. -/
theorem hl_strictMono_curve {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) (c : S.InextCausalCurve) :
    StrictMono (Θ ∘ c.γ) := by
  have hf : Continuous (Θ ∘ c.γ) := hΘ.1.continuousOn.comp_continuous c.cont c.mem
  have hd : ∀ t ∉ c.brk, 0 < deriv (Θ ∘ c.γ) t := by
    intro t ht
    obtain ⟨hγd, hft⟩ := c.causal t ht
    have hdΘ : DifferentiableAt ℝ Θ (c.γ t) :=
      (hΘ.1.contDiffAt (S.isOpen_M.mem_nhds (c.mem t))).differentiableAt one_ne_zero
    rw [(hdΘ.hasFDerivAt.comp_hasDerivAt t hγd.hasDerivAt).deriv]
    exact hΘ.2 _ (c.mem t) _ hft
  intro s t hst
  have hfin : (c.brk ∩ Ioo s t).Finite :=
    (c.brk_fin s t).subset (inter_subset_inter_right _ Ioo_subset_Icc_self)
  exact strictMonoOn_of_brk hf hd _ s t hfin le_rfl ⟨le_rfl, hst.le⟩ ⟨hst.le, le_rfl⟩ hst

/-- **Stretch BUILT: two-sided ⇔ future ∧ past.** Campaign 60's `IsCauchyTemporal` is exactly the
conjunction of the future and past forms (all with the repaired `IsTemporal`). The future form
alone is weaker (`exp ∘ Θ` is future Cauchy and never negative; not formalised).

*Joint satisfiability:* an equivalence; either side holds e.g. for the time coordinate of
Minkowski space (standard; not formalised here). -/
theorem hl_cauchy_iff {Θ : V → ℝ} :
    S.IsCauchyTemporal Θ ↔ S.FutCauchyTemporal Θ ∧ S.PastCauchyTemporal Θ := by
  refine ⟨fun h => ⟨S.hl_futCauchy_of_cauchy h, S.hl_pastCauchy_of_cauchy h⟩,
    fun ⟨hF, hP⟩ => ⟨hF.1, fun c a => ?_⟩⟩
  obtain ⟨t, ht⟩ : ∃ t, Θ (c.γ t) = a := by
    rcases le_total (Θ (c.γ 0)) a with h | h
    · obtain ⟨t, -, ht⟩ := hF.2 ⟨c.γ, c.cont.continuousOn, fun t _ => c.mem t, c.brk, c.brk_fin,
        fun t _ hb => c.causal t hb, c.inext_future⟩ a h
      exact ⟨t, ht⟩
    · obtain ⟨t, -, ht⟩ := hP.2 ⟨c.γ, c.cont.continuousOn, fun t _ => c.mem t, c.brk, c.brk_fin,
        fun t _ hb => c.causal t hb, c.inext_past⟩ a h
      exact ⟨t, ht⟩
  exact ⟨t, ht, fun s hs => (S.hl_strictMono_curve hF.1 c).injective (hs.trans ht.symm)⟩

/-! ## Campaign 81 ①: `hint` and `hcl` by push-up -/

/-- The segment `r ↦ q + r • T(q)`, `|r| ≤ ε`, stays in `M` with `T(q)` future-timelike along it
(two-sided form of `seg_timelike`). -/
lemma hl_seg_timelike2 {q : V} (hq : q ∈ S.M) : ∃ ε > 0, ∀ r ∈ Icc (-ε) ε,
    S.seg q r ∈ S.M ∧ S.FutTimelike (S.seg q r) (S.T q) := by
  have hc : Continuous fun r : ℝ => (S.seg q r, S.T q) :=
    (continuous_const.add (continuous_id.smul continuous_const)).prodMk continuous_const
  have hO := S.isOpen_timelikePairs.preimage hc
  have h0 : (0:ℝ) ∈ (fun r : ℝ => (S.seg q r, S.T q)) ⁻¹'
      {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
    show S.seg q 0 ∈ S.M ∧ S.FutTimelike (S.seg q 0) (S.T q)
    rw [seg_zero]; exact ⟨hq, S.T_timelike q hq, S.T_timelike q hq⟩
  obtain ⟨δ, hδ, hball⟩ := Metric.isOpen_iff.1 hO 0 h0
  refine ⟨δ / 2, by positivity, fun r hr => hball ?_⟩
  rw [mem_ball, Real.dist_eq, sub_zero, abs_lt]
  constructor <;> linarith [hr.1, hr.2]

lemma hl_seg_tendsto (q : V) : Tendsto (S.seg q) (𝓝 0) (𝓝 q) := by
  have h : Continuous (S.seg q) := continuous_const.add (continuous_id.smul continuous_const)
  have := h.tendsto 0
  rwa [S.seg_zero] at this

/-- **The short future step** (the registered "reachable negative" lemma, BUILT): for `x ∈ M`, every
neighbourhood `N` of `x` contains a `y = x + r T(x)` with `x ≪ y`, via one `TStep` inside `M`. -/
theorem hl_future_step {x : V} (hx : x ∈ S.M) {N : Set V} (hN : N ∈ 𝓝 x) :
    ∃ y ∈ N, S.Chr x y := by
  obtain ⟨ε, hε, hseg⟩ := S.hl_seg_timelike2 hx
  have hc := (S.hl_seg_tendsto x).mono_left (nhdsWithin_le_nhds (s := Ioi 0))
  obtain ⟨r, hrN, hr0, hrε⟩ := ((hc.eventually hN).and (Ioo_mem_nhdsGT hε)).exists
  refine ⟨S.seg x r, hrN, Relation.TransGen.single ?_⟩
  have h := S.seg_tstep hseg (by linarith) hr0 hrε.le
  rwa [seg_zero] at h

/-- **The short past step**: every neighbourhood of `x ∈ M` contains a `y = x − r T(x)`, `y ≪ x`. -/
theorem hl_past_step {x : V} (hx : x ∈ S.M) {N : Set V} (hN : N ∈ 𝓝 x) :
    ∃ y ∈ N, S.Chr y x := by
  obtain ⟨ε, hε, hseg⟩ := S.hl_seg_timelike2 hx
  have hc := (S.hl_seg_tendsto x).mono_left (nhdsWithin_le_nhds (s := Iio 0))
  obtain ⟨r, hrN, hrε, hr0⟩ := ((hc.eventually hN).and (Ioo_mem_nhdsLT (neg_lt_zero.2 hε))).exists
  refine ⟨S.seg x r, hrN, Relation.TransGen.single ?_⟩
  have h := S.seg_tstep hseg hrε.le hr0 hε.le
  rwa [seg_zero] at h

/-- A point of `J⁻(z)` is `z` itself or lies in `M`. -/
lemma hl_cau_mem {x z : V} (h : S.Cau x z) : x ∈ S.M ∨ x = z := by
  rcases Relation.ReflTransGen.cases_head h with h | ⟨b, ⟨γ, -, h0, -, hγ⟩, -⟩
  · exact Or.inr h
  · left; rw [← h0]; exact (hγ 0 ⟨le_rfl, zero_le_one⟩).1

/-- `J ⊆ M ⟹ J⁻(J) ⊆ M`. -/
theorem hl_JpastSet_subset_M (hJM : J ⊆ S.M) : S.JpastSet J ⊆ S.M := by
  intro x hx
  simp only [JpastSet, mem_iUnion] at hx
  obtain ⟨z, hz, hxz⟩ := hx
  rcases S.hl_cau_mem hxz with h | h
  · exact h
  · exact h ▸ hJM hz



end Spacetime

/-! ## (1) The model: 2D Minkowski in null coordinates, `J` the Rindler worldline

The chart is `P = ℝ × ℝ` with `p = (U, V)`, `U = t − x`, `V = t + x`. Then
`−dt² + dx² = −dU dV`, i.e. `g(a, b) = −(a_U b_V + a_V b_U)/2`, and `T = ∂_t = ∂_U + ∂_V = (1, 1)`.
`M` is the whole plane. -/

namespace Model
open ContinuousLinearMap

set_option synthInstance.maxHeartbeats 400000

/-- Null coordinates `p = (U, V)`. -/
abbrev P := ℝ × ℝ

/-- `g = −dU dV` (symmetrised). -/
noncomputable def gM : P →L[ℝ] P →L[ℝ] ℝ :=
  (-(1/2 : ℝ)) • ((fst ℝ ℝ ℝ).smulRight (snd ℝ ℝ ℝ) + (snd ℝ ℝ ℝ).smulRight (fst ℝ ℝ ℝ))

lemma gM_apply (v w : P) : gM v w = -(v.1 * w.2 + v.2 * w.1) / 2 := by
  simp [gM]; ring

/-- 2D Minkowski space, `M = ℝ²`, `T = ∂_t`. -/
noncomputable def mink : Spacetime P where
  M := univ
  isOpen_M := isOpen_univ
  g := fun _ => gM
  cont_g := continuousOn_const
  symm := fun _ v w => by rw [gM_apply, gM_apply]; ring
  T := fun _ => (1, 1)
  cont_T := continuousOn_const
  T_timelike := fun _ _ => by rw [gM_apply]; norm_num
  pos_on_perp := fun _ _ v h hv => by
    rw [gM_apply] at h ⊢
    have h2 : v.2 = -v.1 := by linarith
    have h1 : v.1 ≠ 0 := by
      intro h1; apply hv; ext
      · exact h1
      · rw [h2, h1]; simp
    rw [h2]; nlinarith [sq_pos_of_ne_zero h1]

/-- Future-causal in null coordinates: `v_U ≥ 0`, `v_V ≥ 0`, not both `0`. -/
lemma futCausal_iff (x v : P) : mink.FutCausal x v ↔ 0 ≤ v.1 ∧ 0 ≤ v.2 ∧ 0 < v.1 + v.2 := by
  show gM v v ≤ 0 ∧ gM v (1, 1) < 0 ↔ _
  rw [gM_apply, gM_apply]
  constructor
  · rintro ⟨h1, h2⟩
    have hs : 0 < v.1 + v.2 := by linarith
    have hp : 0 ≤ v.1 * v.2 := by linarith
    refine ⟨?_, ?_, hs⟩ <;> by_contra h <;> push Not at h <;> nlinarith
  · rintro ⟨h1, h2, h3⟩; constructor <;> nlinarith

/-- Future-timelike in null coordinates: `v_U > 0`, `v_V > 0`. -/
lemma futTimelike_iff (x v : P) : mink.FutTimelike x v ↔ 0 < v.1 ∧ 0 < v.2 := by
  show gM v v < 0 ∧ gM v (1, 1) < 0 ↔ _
  rw [gM_apply, gM_apply]
  constructor
  · rintro ⟨h1, h2⟩
    have hs : 0 < v.1 + v.2 := by linarith
    have hp : 0 < v.1 * v.2 := by linarith
    refine ⟨?_, ?_⟩ <;> by_contra h <;> push Not at h <;> nlinarith
  · rintro ⟨h1, h2⟩; constructor <;> nlinarith

lemma hasDerivAt_lin {γ : ℝ → P} (φ : P →L[ℝ] ℝ) {t : ℝ} (h : DifferentiableAt ℝ γ t) :
    HasDerivAt (fun t => φ (γ t)) (φ (deriv γ t)) t :=
  φ.hasFDerivAt.comp_hasDerivAt t h.hasDerivAt

lemma lin_le_of_step {γ : ℝ → P} (hγ : ContDiff ℝ 1 γ) (φ : P →L[ℝ] ℝ)
    (h : ∀ t ∈ Icc (0:ℝ) 1, 0 ≤ φ (deriv γ t)) : φ (γ 0) ≤ φ (γ 1) := by
  have hd : ∀ t, HasDerivAt (fun t => φ (γ t)) (φ (deriv γ t)) t := fun t =>
    hasDerivAt_lin φ ((hγ.differentiable one_ne_zero) t)
  have hm : MonotoneOn (fun t => φ (γ t)) (Icc (0:ℝ) 1) :=
    monotoneOn_of_deriv_nonneg (convex_Icc 0 1)
      (fun t _ => (hd t).continuousAt.continuousWithinAt)
      (fun t _ => (hd t).differentiableAt.differentiableWithinAt)
      (fun t ht => by
        rw [interior_Icc] at ht; rw [(hd t).deriv]; exact h t (Ioo_subset_Icc_self ht))
  exact hm ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_le_one

lemma lin_lt_of_step {γ : ℝ → P} (hγ : ContDiff ℝ 1 γ) (φ : P →L[ℝ] ℝ)
    (h : ∀ t ∈ Icc (0:ℝ) 1, 0 < φ (deriv γ t)) : φ (γ 0) < φ (γ 1) := by
  have hd : ∀ t, HasDerivAt (fun t => φ (γ t)) (φ (deriv γ t)) t := fun t =>
    hasDerivAt_lin φ ((hγ.differentiable one_ne_zero) t)
  have hm : StrictMonoOn (fun t => φ (γ t)) (Icc (0:ℝ) 1) :=
    strictMonoOn_of_deriv_pos (convex_Icc 0 1)
      (fun t _ => (hd t).continuousAt.continuousWithinAt)
      (fun t ht => by
        rw [interior_Icc] at ht; rw [(hd t).deriv]; exact h t (Ioo_subset_Icc_self ht))
  exact hm ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one

/-- `U` and `V` increase strictly along a timelike step. -/
lemma tstep_lt {x y : P} (h : mink.TStep x y) : x.1 < y.1 ∧ x.2 < y.2 := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have k := fun t ht => (futTimelike_iff _ _).1 (hγt t ht).2
  subst h0 h1
  exact ⟨by simpa using lin_lt_of_step hγ (fst ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).1),
    by simpa using lin_lt_of_step hγ (snd ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).2)⟩

/-- `U` and `V` do not decrease along a causal step. -/
lemma cstep_le {x y : P} (h : mink.CStep x y) : x.1 ≤ y.1 ∧ x.2 ≤ y.2 := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have k := fun t ht => (futCausal_iff _ _).1 (hγt t ht).2
  subst h0 h1
  exact ⟨by simpa using lin_le_of_step hγ (fst ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).1),
    by simpa using lin_le_of_step hγ (snd ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).2.1)⟩

lemma chr_lt {x y : P} (h : mink.Chr x y) : x.1 < y.1 ∧ x.2 < y.2 := by
  induction h with
  | single h => exact tstep_lt h
  | tail _ h ih => exact ⟨ih.1.trans (tstep_lt h).1, ih.2.trans (tstep_lt h).2⟩

lemma cau_le {x y : P} (h : mink.Cau x y) : x.1 ≤ y.1 ∧ x.2 ≤ y.2 := by
  induction h with
  | refl => exact ⟨le_rfl, le_rfl⟩
  | tail _ h ih => exact ⟨ih.1.trans (cstep_le h).1, ih.2.trans (cstep_le h).2⟩

/-- The straight segment is a timelike step when both null coordinates increase. -/
lemma tstep_of_lt {x y : P} (h1 : x.1 < y.1) (h2 : x.2 < y.2) : mink.TStep x y := by
  refine ⟨fun t => x + t • (y - x), contDiff_const.add (contDiff_id.smul contDiff_const),
    by simp, by simp, fun t _ => ⟨mem_univ _, ?_⟩⟩
  have hd : deriv (fun t : ℝ => x + t • (y - x)) t = y - x := by
    have h : HasDerivAt (fun t : ℝ => x + t • (y - x)) ((1:ℝ) • (y - x)) t :=
      ((hasDerivAt_id' t).smul_const (y - x)).const_add x
    rw [h.deriv, one_smul]
  rw [hd, futTimelike_iff]
  simp only [Prod.fst_sub, Prod.snd_sub, sub_pos]
  exact ⟨h1, h2⟩

/-- The Rindler worldline `O(σ) = (U, V) = (−e^{−σ}, e^{σ})`, on `U·V = −1`. -/
noncomputable def O (σ : ℝ) : P := (-Real.exp (-σ), Real.exp σ)

lemma O_UV (σ : ℝ) : (O σ).1 * (O σ).2 = -1 := by
  simp only [O, neg_mul, ← Real.exp_add, neg_add_cancel, Real.exp_zero]

/-- `O` is future-timelike: `O s ≪ O t` for `s < t`. -/
theorem hl_O_mono (s t : ℝ) (h : s < t) : mink.Chr (O s) (O t) := by
  refine Relation.TransGen.single (tstep_of_lt ?_ ?_)
  · simp only [O, neg_lt_neg_iff, Real.exp_lt_exp]; linarith
  · simp only [O, Real.exp_lt_exp]; exact h

/-- **`D = {U < 0}`.** -/
theorem hl_D_eq : mink.D (range O) = {p : P | p.1 < 0} := by
  ext p
  simp only [Spacetime.D, Spacetime.IpastSet, mem_iUnion, mem_ofPred_eq, Spacetime.Ipast,
    exists_prop]
  constructor
  · rintro ⟨_, ⟨σ, rfl⟩, h⟩
    have h1 := (chr_lt h).1
    have h2 : 0 < Real.exp (-σ) := Real.exp_pos _
    simp only [O] at h1; linarith
  · intro hp
    have e1 : ∀ᶠ σ in atTop, Real.exp (-σ) < -p.1 :=
      (tendsto_order.1 Real.tendsto_exp_neg_atTop_nhds_zero).2 _ (by linarith)
    have e2 : ∀ᶠ σ in atTop, p.2 < Real.exp σ := Real.tendsto_exp_atTop.eventually_gt_atTop p.2
    obtain ⟨σ, h1, h2⟩ := (e1.and e2).exists
    exact ⟨O σ, mem_range_self σ, Relation.TransGen.single
      (tstep_of_lt (by simp only [O]; linarith) h2)⟩

/-- `J⁻(𝒥⁺) = {U < 0}` too. -/
theorem hl_JpastSet_eq : mink.JpastSet (range O) = {p : P | p.1 < 0} := by
  apply Subset.antisymm
  · intro p hp
    simp only [Spacetime.JpastSet, mem_iUnion, Spacetime.Jpast, mem_ofPred_eq, exists_prop] at hp
    obtain ⟨_, ⟨σ, rfl⟩, h⟩ := hp
    have h1 := (cau_le h).1
    have h2 : 0 < Real.exp (-σ) := Real.exp_pos _
    show p.1 < 0
    simp only [O] at h1; linarith
  · rw [← hl_D_eq]
    intro p hp
    simp only [Spacetime.D, Spacetime.IpastSet, Spacetime.JpastSet, mem_iUnion] at hp ⊢
    obtain ⟨z, hz, h⟩ := hp
    exact ⟨z, hz, mink.hl_chr_cau h⟩

/-- **`𝓗⁺ = {U = 0}`.** -/
theorem hl_H_eq : mink.H (range O) = {p : P | p.1 = 0} := by
  have h := (IsOpenMap.preimage_frontier_eq_frontier_preimage (f := (Prod.fst : P → ℝ))
    isOpenMap_fst continuous_fst (Iio (0:ℝ))).symm
  rw [Spacetime.H, hl_JpastSet_eq]
  have e : {p : P | p.1 < 0} = Prod.fst ⁻¹' Iio 0 := rfl
  rw [e, h, frontier_Iio]
  rfl

/-! ## Temporal functions `Θ = G(−U) + V` on `D` and their future Cauchy property -/

/-- `Θ_G(U, V) = G(−U) + V`. -/
noncomputable def ThetaG (G : ℝ → ℝ) (p : P) : ℝ := G (-p.1) + p.2

/-- Conditions on the profile `G` (on `s = −U > 0`). -/
structure GoodG (G : ℝ → ℝ) : Prop where
  cdiff : ContDiffOn ℝ 1 G (Ioi 0)
  deriv_neg : ∀ s, 0 < s → deriv G s < 0
  tendsto_zero : Tendsto G (𝓝[>] 0) atTop
  tendsto_top : Tendsto G atTop atBot

/-- The derivative `dΘ_G = −G′(−U) dU + dV`. -/
noncomputable def dTh (G : ℝ → ℝ) (p : P) : P →L[ℝ] ℝ :=
  deriv G (-p.1) • (-(fst ℝ ℝ ℝ)) + snd ℝ ℝ ℝ

lemma dTh_apply (G : ℝ → ℝ) (p v : P) : dTh G p v = deriv G (-p.1) * (-v.1) + v.2 := by
  simp [dTh]

namespace GoodG
variable {G : ℝ → ℝ} (hG : GoodG G)
include hG

lemma hasDerivAt {s : ℝ} (hs : 0 < s) : HasDerivAt G (deriv G s) s :=
  ((hG.cdiff.differentiableOn one_ne_zero s hs).differentiableAt (Ioi_mem_nhds hs)).hasDerivAt

lemma hasFDerivAt {p : P} (hp : p.1 < 0) : HasFDerivAt (ThetaG G) (dTh G p) p := by
  have h1 : HasFDerivAt (fun p : P => -p.1) (-(fst ℝ ℝ ℝ)) p := hasFDerivAt_fst.neg
  have h2 := (hG.hasDerivAt (s := -p.1) (by linarith)).comp_hasFDerivAt p h1
  exact h2.add hasFDerivAt_snd

lemma fderiv_eq {p : P} (hp : p.1 < 0) : fderiv ℝ (ThetaG G) p = dTh G p :=
  (hG.hasFDerivAt hp).fderiv

lemma contDiffOn : ContDiffOn ℝ 1 (ThetaG G) {p : P | p.1 < 0} := by
  have h1 : ContDiffOn ℝ 1 (fun p : P => G (-p.1)) {p : P | p.1 < 0} :=
    hG.cdiff.comp (contDiff_fst.neg.contDiffOn) (fun p (hp : p.1 < 0) => by
      show 0 < -p.1; linarith)
  exact h1.add contDiff_snd.contDiffOn

lemma anti : StrictAntiOn G (Ioi 0) :=
  strictAntiOn_of_deriv_neg (convex_Ioi 0) hG.cdiff.continuousOn
    (fun x hx => by rw [interior_Ioi] at hx; exact hG.deriv_neg x hx)

/-- `G(s) ≤ K` forces `s ≥ δ > 0`. -/
lemma lower (K : ℝ) : ∃ δ > 0, ∀ s, 0 < s → G s ≤ K → δ ≤ s := by
  obtain ⟨u, hu, hsub⟩ :=
    (mem_nhdsGT_iff_exists_Ioo_subset).1 (hG.tendsto_zero.eventually_gt_atTop K)
  refine ⟨u, hu, fun s hs hK => le_of_not_gt fun hsu => ?_⟩
  have : K < G s := hsub ⟨hs, hsu⟩
  linarith

/-- `Θ_G` is temporal on `{U < 0}`: `dΘ_G(v) = (−G′) v_U + v_V > 0` for future-causal `v`. -/
lemma dTh_pos {p : P} (hp : p.1 < 0) {v : P} (hv : mink.FutCausal p v) : 0 < dTh G p v := by
  rw [dTh_apply]
  obtain ⟨h1, h2, h3⟩ := (futCausal_iff _ _).1 hv
  have hd := hG.deriv_neg (-p.1) (by linarith)
  rcases h1.eq_or_lt with h | h
  · rw [← h]; simp only [neg_zero, mul_zero, zero_add]; linarith
  · nlinarith

end GoodG

/-- Monotonicity of a function continuous on `[0, ∞)` with nonnegative derivative off a locally
finite set of break points. -/
lemma mono_brk {f : ℝ → ℝ} {B : Set ℝ} (hB : ∀ a b, (B ∩ Icc a b).Finite)
    (hf : ContinuousOn f (Ici 0))
    (hd : ∀ t, 0 < t → t ∉ B → DifferentiableAt ℝ f t ∧ 0 ≤ deriv f t) :
    MonotoneOn f (Ici 0) := by
  have hfin : ∀ a b, (B ∩ Ioo a b).Finite := fun a b =>
    (hB a b).subset (inter_subset_inter_right _ Ioo_subset_Icc_self)
  have base : ∀ a b, 0 ≤ a → a ≤ b → B ∩ Ioo a b = ∅ → f a ≤ f b := by
    intro a b ha hab he
    have hm : MonotoneOn f (Icc a b) := by
      refine monotoneOn_of_deriv_nonneg (convex_Icc a b)
        (hf.mono fun t ht => le_trans ha ht.1) (fun t ht => ?_) (fun t ht => ?_)
      all_goals
        rw [interior_Icc] at ht
        have htB : t ∉ B := fun h => (he ▸ (⟨h, ht⟩ : t ∈ B ∩ Ioo a b) : t ∈ (∅ : Set ℝ))
        have := hd t (by linarith [ht.1]) htB
      · exact this.1.differentiableWithinAt
      · exact this.2
    exact hm ⟨le_rfl, hab⟩ ⟨hab, le_rfl⟩ hab
  have key : ∀ n : ℕ, ∀ a b, 0 ≤ a → a ≤ b → (B ∩ Ioo a b).ncard ≤ n → f a ≤ f b := by
    intro n
    induction n with
    | zero =>
      intro a b ha hab hn
      exact base a b ha hab ((Set.ncard_eq_zero (hfin a b)).1 (Nat.le_zero.1 hn))
    | succ n ih =>
      intro a b ha hab hn
      by_cases he : B ∩ Ioo a b = ∅
      · exact base a b ha hab he
      obtain ⟨c, hcB, hc⟩ := nonempty_iff_ne_empty.2 he
      have h1 : (B ∩ Ioo a c).ncard ≤ n := by
        have : B ∩ Ioo a c ⊂ B ∩ Ioo a b :=
          (ssubset_iff_of_subset (inter_subset_inter_right _
            (Ioo_subset_Ioo_right hc.2.le))).2 ⟨c, ⟨hcB, hc⟩, fun h => lt_irrefl c h.2.2⟩
        have := Set.ncard_lt_ncard this (hfin a b)
        omega
      have h2 : (B ∩ Ioo c b).ncard ≤ n := by
        have : B ∩ Ioo c b ⊂ B ∩ Ioo a b :=
          (ssubset_iff_of_subset (inter_subset_inter_right _
            (Ioo_subset_Ioo_left hc.1.le))).2 ⟨c, ⟨hcB, hc⟩, fun h => lt_irrefl c h.2.1⟩
        have := Set.ncard_lt_ncard this (hfin a b)
        omega
      exact (ih a c ha hc.1.le h1).trans (ih c b (ha.trans hc.1.le) hc.2.le h2)
  intro a ha b hb hab
  exact key _ a b ha hab le_rfl

/-- **Future Cauchy property in the model.** For a good profile `G`, `Θ_G = G(−U) + V` is
`FutCauchyTemporal` on `D` (with the repaired `IsTemporal`). Along a future-inextendible causal
curve in `D`, `U` and `V` are nondecreasing; if `Θ` stayed below `a`, then `V` and `U` would be
bounded (`U ≤ −δ` by the blow-up of `G` at `0⁺`), so the curve would converge to a point with
`U < 0`, i.e. in `D`, contradicting inextendibility; so some `Θ(γ T) ≥ a`, and the IVT. -/
theorem hl_futCauchy {G : ℝ → ℝ} (hG : GoodG G) :
    (mink.Dsp (range O)).FutCauchyTemporal (ThetaG G) := by
  have hM : (mink.Dsp (range O)).M = {p : P | p.1 < 0} := hl_D_eq
  refine ⟨⟨hM ▸ hG.contDiffOn, fun x hx v hv => ?_⟩, fun c a ha => ?_⟩
  · rw [hM] at hx
    rw [hG.fderiv_eq hx]
    exact hG.dTh_pos hx hv
  have hmem : ∀ t, 0 ≤ t → (c.γ t).1 < 0 := fun t ht => by
    have := c.mem t ht; rw [hM] at this; exact this
  have hcaus : ∀ t, 0 < t → t ∉ c.brk →
      DifferentiableAt ℝ c.γ t ∧ 0 ≤ (deriv c.γ t).1 ∧ 0 ≤ (deriv c.γ t).2 := by
    intro t ht hb
    obtain ⟨hd, hc⟩ := c.causal t ht hb
    obtain ⟨h1, h2, -⟩ := (futCausal_iff (c.γ t) _).1 hc
    exact ⟨hd, h1, h2⟩
  have hU : MonotoneOn (fun t => (c.γ t).1) (Ici 0) := by
    refine mono_brk c.brk_fin (continuous_fst.comp_continuousOn c.cont) fun t ht hb => ?_
    obtain ⟨hd, h1, -⟩ := hcaus t ht hb
    have h := hasDerivAt_lin (fst ℝ ℝ ℝ) hd
    refine ⟨h.differentiableAt, ?_⟩
    change 0 ≤ deriv (fun t => (fst ℝ ℝ ℝ) (c.γ t)) t
    rw [h.deriv]; simpa using h1
  have hV : MonotoneOn (fun t => (c.γ t).2) (Ici 0) := by
    refine mono_brk c.brk_fin (continuous_snd.comp_continuousOn c.cont) fun t ht hb => ?_
    obtain ⟨hd, -, h2⟩ := hcaus t ht hb
    have h := hasDerivAt_lin (snd ℝ ℝ ℝ) hd
    refine ⟨h.differentiableAt, ?_⟩
    change 0 ≤ deriv (fun t => (snd ℝ ℝ ℝ) (c.γ t)) t
    rw [h.deriv]; simpa using h2
  have hcont : ContinuousOn (fun t => ThetaG G (c.γ t)) (Ici 0) :=
    hG.contDiffOn.continuousOn.comp c.cont (fun t ht => hmem t ht)
  suffices h : ∃ T, 0 ≤ T ∧ a ≤ ThetaG G (c.γ T) by
    obtain ⟨T, hT, haT⟩ := h
    obtain ⟨t, ht, hta⟩ := intermediate_value_Icc hT (hcont.mono Icc_subset_Ici_self) ⟨ha, haT⟩
    exact ⟨t, ht.1, hta⟩
  by_contra hno
  push Not at hno
  have h0 : (0:ℝ) ∈ Ici (0:ℝ) := mem_Ici.2 le_rfl
  obtain ⟨δ, hδ, hδs⟩ := hG.lower (a - (c.γ 0).2)
  have hUle : ∀ t, 0 ≤ t → (c.γ t).1 ≤ -δ := by
    intro t ht
    have h1 := hno t ht
    have h2 : (c.γ 0).2 ≤ (c.γ t).2 := hV h0 ht ht
    unfold ThetaG at h1
    have := hδs (-(c.γ t).1) (by linarith [hmem t ht]) (by linarith)
    linarith
  have hVle : ∀ t, 0 ≤ t → (c.γ t).2 ≤ a - G (-(c.γ 0).1) := by
    intro t ht
    have h1 := hno t ht
    have hU0 : (c.γ 0).1 ≤ (c.γ t).1 := hU h0 ht ht
    have hanti : G (-(c.γ 0).1) ≤ G (-(c.γ t).1) := by
      rcases hU0.eq_or_lt with h | h
      · rw [h]
      · exact (hG.anti (show (0:ℝ) < -(c.γ t).1 by linarith [hmem t ht])
          (show (0:ℝ) < -(c.γ 0).1 by linarith [hmem 0 le_rfl]) (by linarith)).le
    unfold ThetaG at h1
    linarith
  set u : ℝ → ℝ := fun t => (c.γ (max t 0)).1 with hu
  set w : ℝ → ℝ := fun t => (c.γ (max t 0)).2 with hw
  have hum : Monotone u := fun x y hxy =>
    hU (le_max_right x 0) (le_max_right y 0) (max_le_max hxy le_rfl)
  have hwm : Monotone w := fun x y hxy =>
    hV (le_max_right x 0) (le_max_right y 0) (max_le_max hxy le_rfl)
  have hub : BddAbove (range u) :=
    ⟨-δ, by rintro _ ⟨t, rfl⟩; exact hUle _ (le_max_right _ _)⟩
  have hwb : BddAbove (range w) :=
    ⟨a - G (-(c.γ 0).1), by rintro _ ⟨t, rfl⟩; exact hVle _ (le_max_right _ _)⟩
  have hlim : Tendsto c.γ atTop (𝓝 ((⨆ t, u t), (⨆ t, w t))) := by
    have h := (tendsto_atTop_ciSup hum hub).prodMk_nhds (tendsto_atTop_ciSup hwm hwb)
    refine h.congr' ?_
    filter_upwards [eventually_ge_atTop 0] with t ht
    simp [u, w, max_eq_left ht]
  apply c.inext_future
  refine ⟨_, ?_, hlim⟩
  rw [hM]
  show (⨆ t, u t) < 0
  exact lt_of_le_of_lt (ciSup_le fun t => hUle _ (le_max_right _ _)) (by linarith)

/-! ### Adaptation: reparametrise `O` so that `Θ(O' τ) = τ` -/

/-- `φ(σ) = Θ_G(O σ) = G(e^{−σ}) + e^{σ}`. -/
noncomputable def phiG (G : ℝ → ℝ) (σ : ℝ) : ℝ := ThetaG G (O σ)

lemma phiG_eq (G : ℝ → ℝ) (σ : ℝ) : phiG G σ = G (Real.exp (-σ)) + Real.exp σ := by
  simp [phiG, ThetaG, O]

namespace GoodG
variable {G : ℝ → ℝ} (hG : GoodG G)
include hG

lemma phiG_strictMono : StrictMono (phiG G) := by
  intro s t hst
  rw [phiG_eq, phiG_eq]
  have h1 : Real.exp (-t) < Real.exp (-s) := Real.exp_lt_exp.2 (by linarith)
  have h2 := hG.anti (Real.exp_pos (-t)) (Real.exp_pos (-s)) h1
  have h3 : Real.exp s < Real.exp t := Real.exp_lt_exp.2 hst
  linarith

lemma phiG_surjective : Function.Surjective (phiG G) := by
  have he : (phiG G) = fun σ => G (Real.exp (-σ)) + Real.exp σ := funext (phiG_eq G)
  rw [he]
  refine Continuous.surjective ?_ ?_ ?_
  · exact (hG.cdiff.continuousOn.comp_continuous (Real.continuous_exp.comp continuous_neg)
      (fun σ => Real.exp_pos _)).add Real.continuous_exp
  · have hexp0 : Tendsto (fun σ => Real.exp (-σ)) atTop (𝓝[>] 0) :=
      tendsto_nhdsWithin_iff.2 ⟨Real.tendsto_exp_neg_atTop_nhds_zero,
        Eventually.of_forall fun _ => Real.exp_pos _⟩
    exact (hG.tendsto_zero.comp hexp0).atTop_add_atTop Real.tendsto_exp_atTop
  · exact (hG.tendsto_top.comp (Real.tendsto_exp_atTop.comp tendsto_neg_atBot_atTop)).atBot_add
      Real.tendsto_exp_atBot

/-- **Adaptation.** A reparametrisation `O'` of the Rindler worldline, with the same range, still
future-timelike, along which `Θ_G(O' τ) = τ`. -/
theorem hl_adapted : ∃ O' : ℝ → P, range O' = range O ∧
    mink.IpastSet (range O') = mink.D (range O) ∧
    (∀ s t : ℝ, s < t → mink.Chr (O' s) (O' t)) ∧ ∀ τ, ThetaG G (O' τ) = τ + 0 := by
  have hs := hG.phiG_surjective
  have hm := hG.phiG_strictMono
  set ψ := Function.surjInv hs
  have hψ : ∀ τ, phiG G (ψ τ) = τ := Function.surjInv_eq hs
  have hrange : range (fun τ => O (ψ τ)) = range O := by
    apply Subset.antisymm
    · rintro _ ⟨τ, rfl⟩; exact mem_range_self _
    · rintro _ ⟨σ, rfl⟩
      exact ⟨phiG G σ, by show O (ψ (phiG G σ)) = O σ; rw [hm.injective (hψ (phiG G σ))]⟩
  refine ⟨fun τ => O (ψ τ), hrange, by rw [hrange]; rfl, fun s t hst => hl_O_mono _ _ ?_,
    fun τ => by rw [add_zero]; exact hψ τ⟩
  rw [← hm.lt_iff_lt, hψ, hψ]; exact hst

end GoodG

/-! ## The aligned `Θ₀ = −log(−U) + V` and the failing `Θ = F(−U) + V` -/

/-- `G₀(s) = −log s`. -/
lemma goodG_log : GoodG fun s => -Real.log s where
  cdiff := Real.contDiffOn_log.neg.mono fun s (hs : 0 < s) => by simpa using hs.ne'
  deriv_neg s hs := by
    have h : HasDerivAt (fun s => -Real.log s) (-s⁻¹) s := (Real.hasDerivAt_log hs.ne').neg
    rw [h.deriv]
    simpa using hs
  tendsto_zero := tendsto_neg_atBot_atTop.comp Real.tendsto_log_nhdsGT_zero
  tendsto_top := tendsto_neg_atTop_atBot.comp Real.tendsto_log_atTop

/-- The failing profile `F(s) = −log s − sin(log s) − s`. -/
noncomputable def Ffail (s : ℝ) : ℝ := -Real.log s - Real.sin (Real.log s) - s

lemma Ffail_hasDerivAt {s : ℝ} (hs : 0 < s) :
    HasDerivAt Ffail (-s⁻¹ - Real.cos (Real.log s) * s⁻¹ - 1) s := by
  have hl := Real.hasDerivAt_log hs.ne'
  exact (hl.neg.sub ((Real.hasDerivAt_sin (Real.log s)).comp s hl)).sub (hasDerivAt_id s)

lemma goodG_Ffail : GoodG Ffail where
  cdiff := fun s (hs : 0 < s) => by
    have hl := Real.contDiffAt_log (n := 1).2 hs.ne'
    exact ((hl.neg.sub (Real.contDiff_sin.contDiffAt.comp s hl)).sub
      contDiffAt_id).contDiffWithinAt
  deriv_neg s hs := by
    rw [(Ffail_hasDerivAt hs).deriv]
    have hi := inv_pos.2 hs
    nlinarith [Real.neg_one_le_cos (Real.log s)]
  tendsto_zero := by
    have h1 : Tendsto (fun s => -Real.log s + -2) (𝓝[>] 0) atTop :=
      tendsto_atTop_add_const_right _ (-2)
        (tendsto_neg_atBot_atTop.comp Real.tendsto_log_nhdsGT_zero)
    refine tendsto_atTop_mono' _ ?_ h1
    filter_upwards [Ioo_mem_nhdsGT (zero_lt_one' ℝ)] with s hs
    simp only [Ffail]
    nlinarith [Real.sin_le_one (Real.log s), hs.2]
  tendsto_top := by
    have h1 : Tendsto (fun s : ℝ => 1 + -s) atTop atBot :=
      tendsto_atBot_add_const_left _ 1 tendsto_neg_atTop_atBot
    refine tendsto_atBot_mono' _ ?_ h1
    filter_upwards [eventually_ge_atTop 1] with s hs
    simp only [Ffail]
    nlinarith [Real.neg_one_le_sin (Real.log s), Real.log_nonneg hs]

/-- The aligned slicing function `Θ₀ = −log(−U) + V`. -/
noncomputable def Θ₀ : P → ℝ := ThetaG fun s => -Real.log s
/-- The failing slicing function `Θ = F(−U) + V`. -/
noncomputable def Θf : P → ℝ := ThetaG Ffail

/-! ## Campaign 81 ②: the model, two-sided -/

/-- The model's metric is constant, hence locally Lipschitz. -/
theorem hl_lipschitz : LocallyLipschitzOn mink.M mink.g :=
  (LipschitzWith.const (α := P) gM).locallyLipschitz.locallyLipschitzOn

/-- **Past Cauchy property in the model (BUILT).** For a good profile `G`, every past-inextendible
causal curve of `D` ending at `γ 0` attains every level `a ≤ Θ_G(γ 0)`. Into the past `U` and `V`
are non-increasing; if `Θ_G > a` along the whole curve, then `−U` is bounded above (`G → −∞` at `∞`)
and `V` is bounded below (`G` decreasing), so the curve converges as `t → −∞` to a point with
`U ≤ U(γ 0) < 0`, i.e. in `D`, contradicting past-inextendibility; then the IVT. -/
theorem hl_pastCauchy {G : ℝ → ℝ} (hG : GoodG G) :
    (mink.Dsp (range O)).PastCauchyTemporal (ThetaG G) := by
  have hM : (mink.Dsp (range O)).M = {p : P | p.1 < 0} := hl_D_eq
  refine ⟨(hl_futCauchy hG).1, fun c a ha => ?_⟩
  have hmem : ∀ t, t ≤ 0 → (c.γ t).1 < 0 := fun t ht => by
    have := c.mem t ht; rw [hM] at this; exact this
  have hB : ∀ a b : ℝ, ((fun s : ℝ => -s) ⁻¹' c.brk ∩ Icc a b).Finite := by
    intro a b
    refine ((c.brk_fin (-b) (-a)).preimage neg_injective.injOn).subset ?_
    rintro s ⟨hs, h1, h2⟩
    exact ⟨hs, by linarith, by linarith⟩
  -- the reflected coordinates `s ↦ −φ(γ(−s))` are nondecreasing on `[0, ∞)`
  have hrefl : ∀ φ : P →L[ℝ] ℝ, (∀ t, t < 0 → t ∉ c.brk → 0 ≤ φ (deriv c.γ t)) →
      MonotoneOn (fun s => -φ (c.γ (-s))) (Ici 0) := by
    intro φ hφ
    refine mono_brk hB ?_ fun s hs hb => ?_
    · exact (φ.continuous.comp_continuousOn (c.cont.comp continuous_neg.continuousOn
        fun s (hs : 0 ≤ s) => show -s ≤ 0 by linarith)).neg
    · obtain ⟨hd, -⟩ := c.causal (-s) (by linarith) hb
      have h1 : HasDerivAt (fun s => c.γ (-s)) ((-1 : ℝ) • deriv c.γ (-s)) s := by
        have := hd.hasDerivAt.scomp s (hasDerivAt_neg s)
        simpa [Function.comp_def] using this
      have h2 : HasDerivAt (fun s => -φ (c.γ (-s))) (-φ ((-1 : ℝ) • deriv c.γ (-s))) s :=
        (φ.hasFDerivAt.comp_hasDerivAt s h1).neg
      refine ⟨h2.differentiableAt, ?_⟩
      rw [h2.deriv, map_smul, smul_eq_mul, neg_one_mul, neg_neg]
      exact hφ _ (by linarith) hb
  have hUV : ∀ t t', t ≤ t' → t' ≤ 0 → (c.γ t).1 ≤ (c.γ t').1 ∧ (c.γ t).2 ≤ (c.γ t').2 := by
    intro t t' htt ht'
    have k : ∀ t, t < 0 → t ∉ c.brk → 0 ≤ (deriv c.γ t).1 ∧ 0 ≤ (deriv c.γ t).2 :=
      fun t ht hb => by
        obtain ⟨h1, h2, -⟩ := (futCausal_iff (c.γ t) _).1 (c.causal t ht hb).2
        exact ⟨h1, h2⟩
    have h1 := hrefl (fst ℝ ℝ ℝ) (fun t ht hb => by simpa using (k t ht hb).1)
      (show (0:ℝ) ≤ -t' by linarith) (show (0:ℝ) ≤ -t by linarith) (by linarith)
    have h2 := hrefl (snd ℝ ℝ ℝ) (fun t ht hb => by simpa using (k t ht hb).2)
      (show (0:ℝ) ≤ -t' by linarith) (show (0:ℝ) ≤ -t by linarith) (by linarith)
    simp only [neg_neg, coe_fst', coe_snd', neg_le_neg_iff] at h1 h2
    exact ⟨h1, h2⟩
  have hcont : ContinuousOn (fun t => ThetaG G (c.γ t)) (Iic 0) :=
    hG.contDiffOn.continuousOn.comp c.cont (fun t ht => hmem t ht)
  suffices h : ∃ T, T ≤ 0 ∧ ThetaG G (c.γ T) ≤ a by
    obtain ⟨T, hT, haT⟩ := h
    obtain ⟨t, ht, hta⟩ := intermediate_value_Icc hT (hcont.mono Icc_subset_Iic_self) ⟨haT, ha⟩
    exact ⟨t, ht.2, hta⟩
  by_contra hno
  push Not at hno
  obtain ⟨R, hR⟩ := eventually_atTop.1 (hG.tendsto_top.eventually_lt_atBot (a - (c.γ 0).2))
  have hUge : ∀ t, t ≤ 0 → -R ≤ (c.γ t).1 := by
    intro t ht
    by_contra h
    push Not at h
    have h1 := hno t ht
    have h2 := (hUV t 0 ht le_rfl).2
    have h3 := hR (-(c.γ t).1) (by linarith)
    unfold ThetaG at h1
    linarith
  have hVge : ∀ t, t ≤ 0 → a - G (-(c.γ 0).1) ≤ (c.γ t).2 := by
    intro t ht
    have h1 := hno t ht
    have hU0 := (hUV t 0 ht le_rfl).1
    have hanti : G (-(c.γ t).1) ≤ G (-(c.γ 0).1) := by
      rcases hU0.eq_or_lt with h | h
      · rw [h]
      · exact (hG.anti (show (0:ℝ) < -(c.γ 0).1 by linarith [hmem 0 le_rfl])
          (show (0:ℝ) < -(c.γ t).1 by linarith [hmem t ht]) (by linarith)).le
    unfold ThetaG at h1
    linarith
  set u : ℝ → ℝ := fun t => (c.γ (min t 0)).1 with hu
  set w : ℝ → ℝ := fun t => (c.γ (min t 0)).2 with hw
  have hum : Monotone u := fun x y hxy =>
    (hUV _ _ (min_le_min hxy le_rfl) (min_le_right _ _)).1
  have hwm : Monotone w := fun x y hxy =>
    (hUV _ _ (min_le_min hxy le_rfl) (min_le_right _ _)).2
  have hub : BddBelow (range u) :=
    ⟨-R, by rintro _ ⟨t, rfl⟩; exact hUge _ (min_le_right _ _)⟩
  have hwb : BddBelow (range w) :=
    ⟨a - G (-(c.γ 0).1), by rintro _ ⟨t, rfl⟩; exact hVge _ (min_le_right _ _)⟩
  have hlim : Tendsto c.γ atBot (𝓝 ((⨅ t, u t), (⨅ t, w t))) := by
    have h := (tendsto_atBot_ciInf hum hub).prodMk_nhds (tendsto_atBot_ciInf hwm hwb)
    refine h.congr' ?_
    filter_upwards [eventually_le_atBot 0] with t ht
    simp [u, w, min_eq_left ht]
  apply c.inext_past
  refine ⟨_, ?_, hlim⟩
  rw [hM]
  show (⨅ t, u t) < 0
  refine lt_of_le_of_lt (ciInf_le hub 0) ?_
  show (c.γ (min 0 0)).1 < 0
  rw [min_self]; exact hmem 0 le_rfl

/-- **② Two-sided Cauchy in the model (BUILT)**, via `hl_cauchy_iff`: `Θ_G` is campaign 60's
`IsCauchyTemporal` on `D`, with the repaired `IsTemporal`. -/
theorem hl_cauchy {G : ℝ → ℝ} (hG : GoodG G) :
    (mink.Dsp (range O)).IsCauchyTemporal (ThetaG G) :=
  (mink.Dsp (range O)).hl_cauchy_iff.2 ⟨hl_futCauchy hG, hl_pastCauchy hG⟩

theorem hl_cauchy_Θ₀ : (mink.Dsp (range O)).IsCauchyTemporal Θ₀ := hl_cauchy goodG_log
theorem hl_cauchy_Θf : (mink.Dsp (range O)).IsCauchyTemporal Θf := hl_cauchy goodG_Ffail

end Model

/-! ## Campaign 84 c2: the manifold side

### Small `V`-side helpers -/

namespace Spacetime
variable (S : Spacetime V)

lemma ch_futCausal_smul {x u : V} {c : ℝ} (hc : 0 < c) (h : S.FutCausal x u) :
    S.FutCausal x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

lemma ch_tstep_mem {x y : V} (h : S.TStep x y) : x ∈ S.M ∧ y ∈ S.M := by
  obtain ⟨γ, -, h0, h1, hγ⟩ := h
  exact ⟨h0 ▸ (hγ 0 ⟨le_rfl, zero_le_one⟩).1, h1 ▸ (hγ 1 ⟨zero_le_one, le_rfl⟩).1⟩

lemma ch_cstep_mem {x y : V} (h : S.CStep x y) : x ∈ S.M ∧ y ∈ S.M := by
  obtain ⟨γ, -, h0, h1, hγ⟩ := h
  exact ⟨h0 ▸ (hγ 0 ⟨le_rfl, zero_le_one⟩).1, h1 ▸ (hγ 1 ⟨zero_le_one, le_rfl⟩).1⟩

end Spacetime

/-! ### The squash reparametrisation -/

/-- An open interval around `[0,1]` inside an open `U ⊇ [0,1]`. -/
lemma ch_exists_Ioo {U : Set ℝ} (hU : IsOpen U) (h : Icc (0:ℝ) 1 ⊆ U) :
    ∃ δ > 0, Ioo (-δ) (1 + δ) ⊆ U := by
  obtain ⟨δ, hδ, hsub⟩ := isCompact_Icc.exists_thickening_subset_open hU h
  refine ⟨δ, hδ, fun t ht => hsub ?_⟩
  rw [Metric.mem_thickening_iff]
  refine ⟨max 0 (min t 1), ⟨le_max_left _ _, max_le zero_le_one (min_le_right _ _)⟩, ?_⟩
  rw [Real.dist_eq, abs_lt]
  rcases le_total t 1 with h | h
  · rw [min_eq_left h]
    rcases le_total 0 t with h' | h'
    · rw [max_eq_right h']; constructor <;> linarith
    · rw [max_eq_left h']; constructor <;> linarith [ht.1]
  · rw [min_eq_right h, max_eq_right zero_le_one]; constructor <;> linarith [ht.2]

/-- **The squash.** For `δ > 0`, a smooth `σ : ℝ → (-δ, 1+δ)` with `σ 0 = 0`, `σ 1 = 1`, `σ' > 0`:
`σ t = 1/2 + ((1+δ)/Real.pi) arctan (b (2t − 1))`, `b = tan (Real.pi / (2(1+δ)))`. -/
lemma ch_squash {δ : ℝ} (hδ : 0 < δ) : ∃ σ : ℝ → ℝ, ContDiff ℝ 1 σ ∧ σ 0 = 0 ∧ σ 1 = 1 ∧
    (∀ t, σ t ∈ Ioo (-δ) (1 + δ)) ∧ (∀ t, HasDerivAt σ (deriv σ t) t ∧ 0 < deriv σ t) ∧
    ∀ t ∈ Icc (0:ℝ) 1, σ t ∈ Icc (0:ℝ) 1 := by
  set a : ℝ := Real.pi / (2 * (1 + δ)) with ha
  have ha0 : 0 < a := by positivity
  have ha1 : a < Real.pi / 2 := by
    rw [ha, div_lt_div_iff₀ (by positivity) (by norm_num)]; nlinarith [Real.pi_pos]
  set b := Real.tan a with hb
  have hb0 : 0 < b := Real.tan_pos_of_pos_of_lt_pi_div_two ha0 ha1
  have hab : Real.arctan b = a := Real.arctan_tan (by linarith) ha1
  set k : ℝ := (1 + δ) / Real.pi with hk
  have hk0 : 0 < k := by positivity
  have hka : k * a = 1 / 2 := by
    rw [hk, ha]; field_simp
  set σ : ℝ → ℝ := fun t => 1 / 2 + k * Real.arctan (b * (2 * t - 1)) with hσ
  have hd : ∀ t, HasDerivAt σ (k * (1 / (1 + (b * (2 * t - 1)) ^ 2) * (b * 2))) t := by
    intro t
    have h1 : HasDerivAt (fun t : ℝ => b * (2 * t - 1)) (b * 2) t := by
      simpa using (((hasDerivAt_id t).const_mul 2).sub_const 1).const_mul b
    exact ((Real.hasDerivAt_arctan _).comp t h1).const_mul k |>.const_add (1 / 2)
  have hdpos : ∀ t, 0 < k * (1 / (1 + (b * (2 * t - 1)) ^ 2) * (b * 2)) := fun t => by positivity
  have hmono : StrictMono σ := strictMono_of_deriv_pos fun t => by
    rw [(hd t).deriv]; exact hdpos t
  have h0 : σ 0 = 0 := by
    simp only [hσ]; rw [show b * (2 * 0 - 1) = -b by ring, Real.arctan_neg, hab]; linarith
  have h1 : σ 1 = 1 := by
    simp only [hσ]; rw [show b * (2 * 1 - 1) = b by ring, hab]; linarith
  refine ⟨σ, ?_, h0, h1, fun t => ?_, fun t => ⟨(hd t).deriv ▸ hd t, (hd t).deriv ▸ hdpos t⟩,
    fun t ht => ⟨h0 ▸ hmono.monotone ht.1, h1 ▸ hmono.monotone ht.2⟩⟩
  · exact contDiff_const.add (contDiff_const.mul (Real.contDiff_arctan.comp
      (contDiff_const.mul ((contDiff_const.mul contDiff_id).sub contDiff_const))))
  · have l1 := Real.arctan_lt_pi_div_two (b * (2 * t - 1))
    have l2 := Real.neg_pi_div_two_lt_arctan (b * (2 * t - 1))
    have e : k * (Real.pi / 2) = (1 + δ) / 2 := by rw [hk]; field_simp
    have u1 : k * Real.arctan (b * (2 * t - 1)) < (1 + δ) / 2 := by
      rw [← e]; exact mul_lt_mul_of_pos_left l1 hk0
    have u2 : -((1 + δ) / 2) < k * Real.arctan (b * (2 * t - 1)) := by
      rw [← e, ← mul_neg]; exact mul_lt_mul_of_pos_left l2 hk0
    simp only [hσ]
    constructor <;> linarith

/-! ### Copied from campaign 68 (`probes/LieDerivManifold.lean`): chart representatives -/

/-! ## Copied (campaign 80, `TangencyCondition.lean`, sections ① frame-free and normed, names `tc_…`
kept, inside namespace `TCF`): the null-frame inequality and its filter corollary. -/

namespace TCF

/-! ## ① Frame-free: the pointwise inequality (pure linear algebra, no basis, no dimension) -/

section FrameFree

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- A null frame `ℓ, n` for a symmetric bilinear `g`: `g(ℓ,ℓ) = g(n,n) = 0`, `g(ℓ,n) = −1`, and `g`
positive **semi**definite on `W = {ℓ,n}^⊥` (weaker than the registered "positive definite"). -/
structure NullFrame (g : LinearMap.BilinForm ℝ E) (ℓ n : E) : Prop where
  symm : ∀ v w, g v w = g w v
  ll : g ℓ ℓ = 0
  nn : g n n = 0
  ln : g ℓ n = -1
  posW : ∀ e, g ℓ e = 0 → g n e = 0 → 0 ≤ g e e

/-- Future causal: `g(v,v) ≤ 0` and `g(v, ℓ+n) < 0` (`ℓ + n` is future timelike, `g = −2`). Such `v`
are automatically nonzero. `tc_futCausal_iff` shows this is exactly the cone
`{αℓ + βn + e | α, β ≥ 0, e ∈ W, g(e,e) ≤ 2αβ, (α,β) ≠ 0}`. -/
def FutCausal (g : LinearMap.BilinForm ℝ E) (ℓ n v : E) : Prop := g v v ≤ 0 ∧ g v (ℓ + n) < 0

/-- The `g`-orthogonal projection onto `W`: `w_W = w + g(n,w) ℓ + g(ℓ,w) n`. -/
def projW (g : LinearMap.BilinForm ℝ E) (ℓ n w : E) : E := w + g n w • ℓ + g ℓ w • n

/-- The splitting `w = (−g(n,w)) ℓ + (−g(ℓ,w)) n + w_W`. -/
lemma decompW (g : LinearMap.BilinForm ℝ E) (ℓ n w : E) :
    w = (-g n w) • ℓ + (-g ℓ w) • n + projW g ℓ n w := by
  simp only [projW, neg_smul]; abel

variable {g : LinearMap.BilinForm ℝ E} {ℓ n : E}

namespace NullFrame
variable (hF : NullFrame g ℓ n)
include hF

lemma nl : g n ℓ = -1 := by rw [hF.symm]; exact hF.ln

lemma projW_l (w : E) : g ℓ (projW g ℓ n w) = 0 := by
  simp [projW, hF.ll, hF.ln]

lemma projW_n (w : E) : g n (projW g ℓ n w) = 0 := by
  simp [projW, hF.nn, hF.nl]


/-- `g(αℓ + βn + e, αℓ + βn + e) = −2αβ + g(e,e)` for `e ∈ W`. -/
lemma quad (α β : ℝ) {e : E} (he1 : g ℓ e = 0) (he2 : g n e = 0) :
    g (α • ℓ + β • n + e) (α • ℓ + β • n + e) = -2 * α * β + g e e := by
  have h1 : g e ℓ = 0 := by rw [hF.symm]; exact he1
  have h2 : g e n = 0 := by rw [hF.symm]; exact he2
  simp [hF.ll, hF.nn, hF.ln, hF.nl, he1, he2, h1, h2]; ring

/-- `g(αℓ + βn + e, ℓ + n) = −α − β` for `e ∈ W`. -/
lemma lin (α β : ℝ) {e : E} (he1 : g ℓ e = 0) (he2 : g n e = 0) :
    g (α • ℓ + β • n + e) (ℓ + n) = -α - β := by
  have h1 : g e ℓ = 0 := by rw [hF.symm]; exact he1
  have h2 : g e n = 0 := by rw [hF.symm]; exact he2
  simp [hF.ll, hF.nn, hF.ln, hF.nl, h1, h2]; ring

end NullFrame

/-- The future causal cone, made explicit in the splitting `ℓ, n, W`. -/
theorem tc_futCausal_iff (hF : NullFrame g ℓ n) (v : E) :
    FutCausal g ℓ n v ↔ ∃ α β : ℝ, ∃ e : E, 0 ≤ α ∧ 0 ≤ β ∧ g ℓ e = 0 ∧ g n e = 0 ∧
      g e e ≤ 2 * α * β ∧ (α ≠ 0 ∨ β ≠ 0) ∧ v = α • ℓ + β • n + e := by
  constructor
  · rintro ⟨h1, h2⟩
    have hd := decompW g ℓ n v
    set α := -g n v
    set β := -g ℓ v
    set e := projW g ℓ n v
    have he1 := hF.projW_l v
    have he2 := hF.projW_n v
    have hq := hF.quad α β he1 he2
    have hl := hF.lin α β he1 he2
    rw [← hd] at hq hl
    have hW := hF.posW e he1 he2
    have hs : 0 < α + β := by linarith
    have hab : 0 ≤ α * β := by linarith
    have hα : 0 ≤ α := by
      by_contra h; push Not at h; nlinarith
    have hβ : 0 ≤ β := by
      by_contra h; push Not at h; nlinarith
    refine ⟨α, β, e, hα, hβ, he1, he2, by linarith, ?_, hd⟩
    by_contra h; push Not at h; rw [h.1, h.2] at hs; simp at hs
  · rintro ⟨α, β, e, hα, hβ, he1, he2, hq, hne, rfl⟩
    refine ⟨by rw [hF.quad α β he1 he2]; linarith, ?_⟩
    rw [hF.lin α β he1 he2]
    rcases hne with h | h
    · have := lt_of_le_of_ne hα (Ne.symm h); linarith
    · have := lt_of_le_of_ne hβ (Ne.symm h); linarith

variable {ξ : E →ₗ[ℝ] ℝ}

/-- Temporality forces `ξ(ℓ) > 0` and `ξ(n) > 0`. -/
theorem tc_pos (hF : NullFrame g ℓ n) (hξ : ∀ v, FutCausal g ℓ n v → 0 < ξ v) :
    0 < ξ ℓ ∧ 0 < ξ n := by
  refine ⟨hξ ℓ ⟨by rw [hF.ll], ?_⟩, hξ n ⟨by rw [hF.nn], ?_⟩⟩
  · simp [hF.ll, hF.ln]
  · simp [hF.nn, hF.nl]

/-- **The basis-free form of campaign 79's `st_null_frame_bound`**: for `e ∈ W`,
`ξ(e)² ≤ 2 ξ(ℓ) ξ(n) g(e,e)`. Proof: test `ξ` on the null vector `αℓ + βn ∓ e` with
`β = |ξ e|/(2ξ(n))`, `α = g(e,e) ξ(n)/|ξ e|`. -/
theorem tc_W_bound (hF : NullFrame g ℓ n) (hξ : ∀ v, FutCausal g ℓ n v → 0 < ξ v) {e : E}
    (he1 : g ℓ e = 0) (he2 : g n e = 0) : ξ e ^ 2 ≤ 2 * ξ ℓ * ξ n * g e e := by
  obtain ⟨ha, hb⟩ := tc_pos hF hξ
  have hq := hF.posW e he1 he2
  set a := ξ ℓ
  set b := ξ n
  set q := g e e
  have key : ∀ s : ℝ, s * s = 1 → 0 < s * ξ e → (s * ξ e) ^ 2 < 2 * a * b * q := by
    intro s hs hc
    set c := s * ξ e
    have hse1 : g ℓ ((-s) • e) = 0 := by simp [he1]
    have hse2 : g n ((-s) • e) = 0 := by simp [he2]
    have hqs : g ((-s) • e) ((-s) • e) = q := by simp [q]; nlinarith
    set β := c / (2 * b)
    set α := q * b / c
    have hβ : 0 < β := by positivity
    have hα : 0 ≤ α := by positivity
    have hv : FutCausal g ℓ n (α • ℓ + β • n + (-s) • e) := by
      refine ⟨?_, ?_⟩
      · rw [hF.quad α β hse1 hse2, hqs]
        have : α * β = q / 2 := by simp only [α, β]; field_simp
        linarith
      · rw [hF.lin α β hse1 hse2]; linarith
    have hp := hξ _ hv
    simp only [map_add, map_smul, smul_eq_mul] at hp
    have : -s * ξ e = -c := by simp [c]
    rw [this] at hp
    have e1 : α * a = q * a * b / c := by simp only [α]; ring
    have e2 : β * b = c / 2 := by simp only [β]; field_simp
    rw [e1, e2] at hp
    have : c / 2 < q * a * b / c := by linarith
    rw [lt_div_iff₀ hc] at this
    nlinarith
  rcases lt_trichotomy (ξ e) 0 with h | h | h
  · have := key (-1) (by norm_num) (by linarith); nlinarith
  · rw [h]; have := mul_nonneg (mul_pos (mul_pos two_pos ha) hb).le hq; nlinarith
  · have := key 1 (by norm_num) (by linarith); nlinarith

/-- **① The pointwise, basis-free inequality.** For every `w`,
`|ξ(w) − ξ(n)·(−g(ℓ,w))| ≤ ξ(ℓ)·|g(n,w)| + √(2 ξ(ℓ) ξ(n))·√(g(w_W, w_W))`,
`w_W = w + g(n,w) ℓ + g(ℓ,w) n`. -/
theorem tc_pointwise (hF : NullFrame g ℓ n) (hξ : ∀ v, FutCausal g ℓ n v → 0 < ξ v) (w : E) :
    |ξ w - ξ n * (-g ℓ w)| ≤
      ξ ℓ * |g n w| + Real.sqrt (2 * ξ ℓ * ξ n) * Real.sqrt (g (projW g ℓ n w) (projW g ℓ n w)) := by
  obtain ⟨ha, hb⟩ := tc_pos hF hξ
  have he1 := hF.projW_l w
  have he2 := hF.projW_n w
  have hB := tc_W_bound hF hξ he1 he2
  have hxi : ξ w = (-g n w) * ξ ℓ + (-g ℓ w) * ξ n + ξ (projW g ℓ n w) := by
    conv_lhs => rw [decompW g ℓ n w]
    simp
  have habs : |ξ (projW g ℓ n w)| ≤
      Real.sqrt (2 * ξ ℓ * ξ n) * Real.sqrt (g (projW g ℓ n w) (projW g ℓ n w)) := by
    rw [← Real.sqrt_mul (by positivity)]; exact Real.abs_le_sqrt hB
  have : ξ w - ξ n * (-g ℓ w) = -(ξ ℓ * g n w) + ξ (projW g ℓ n w) := by rw [hxi]; ring
  rw [this]
  calc |-(ξ ℓ * g n w) + ξ (projW g ℓ n w)| ≤ |-(ξ ℓ * g n w)| + |ξ (projW g ℓ n w)| :=
        abs_add_le _ _
    _ ≤ _ := by rw [abs_neg, abs_mul, abs_of_pos ha]; linarith

end FrameFree

/-! ## ① The operator-norm bound and the corollary (normed setting, frames and metrics may move) -/

section Normed

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- A continuous bilinear form as a `LinearMap.BilinForm`. -/
noncomputable def bil (g : E →L[ℝ] E →L[ℝ] ℝ) : LinearMap.BilinForm ℝ E :=
  LinearMap.mk₂ ℝ (fun v w => g v w) (by simp) (by simp) (by simp) (by simp)

@[simp] lemma bil_apply (g : E →L[ℝ] E →L[ℝ] ℝ) (v w : E) : bil g v w = g v w := rfl

/-- The frame hypotheses at one point: `(ℓ, n)` is a null frame for `g` and `ξ` is positive on the
future causal cone. -/
def FrameHyp (g : E →L[ℝ] E →L[ℝ] ℝ) (ℓ n : E) (ξ : E →L[ℝ] ℝ) : Prop :=
  NullFrame (bil g) ℓ n ∧ ∀ v, FutCausal (bil g) ℓ n v → 0 < ξ v

/-- **① in operator norm.** Under the frame hypotheses,
`‖ξ/ξ(n) + g(ℓ,·)‖ ≤ (ξℓ/ξn)·‖g‖‖n‖ + √(2 ξℓ/ξn)·√‖g‖·(1 + 2‖g‖‖n‖‖ℓ‖)`. -/
theorem tc_opNorm_bound {g : E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : E} {ξ : E →L[ℝ] ℝ}
    (h : FrameHyp g ℓ n ξ) :
    ‖(ξ n)⁻¹ • ξ + g ℓ‖ ≤ ξ ℓ / ξ n * (‖g‖ * ‖n‖) +
      Real.sqrt (2 * (ξ ℓ / ξ n)) * (Real.sqrt ‖g‖ * (1 + 2 * (‖g‖ * ‖n‖) * ‖ℓ‖)) := by
  obtain ⟨hF, hξ⟩ := h
  have hξ' : ∀ v, FutCausal (bil g) ℓ n v → 0 < (ξ : E →ₗ[ℝ] ℝ) v := hξ
  obtain ⟨ha, hb⟩ := tc_pos hF hξ'
  set a := ξ ℓ
  set b := ξ n
  have ha' : 0 < a := ha
  have hb' : 0 < b := hb
  have hr : 0 ≤ a / b := by positivity
  refine ContinuousLinearMap.opNorm_le_bound _ (by positivity) fun w => ?_
  have hP := tc_pointwise hF hξ' w
  simp only [bil_apply, ContinuousLinearMap.coe_coe] at hP
  set e := projW (bil g) ℓ n w
  -- the size of `w_W`
  have hgn : |g n w| ≤ ‖g‖ * ‖n‖ * ‖w‖ := by
    rw [← Real.norm_eq_abs]; exact g.le_opNorm₂ n w
  have hgl : |g ℓ w| ≤ ‖g‖ * ‖ℓ‖ * ‖w‖ := by
    rw [← Real.norm_eq_abs]; exact g.le_opNorm₂ ℓ w
  have he : ‖e‖ ≤ (1 + 2 * (‖g‖ * ‖n‖) * ‖ℓ‖) * ‖w‖ := by
    have : ‖e‖ ≤ ‖w‖ + |g n w| * ‖ℓ‖ + |g ℓ w| * ‖n‖ := by
      simp only [e, projW, bil_apply]
      refine (norm_add₃_le).trans ?_
      rw [norm_smul, norm_smul, Real.norm_eq_abs, Real.norm_eq_abs]
    have h1 := mul_le_mul_of_nonneg_right hgn (norm_nonneg ℓ)
    have h2 := mul_le_mul_of_nonneg_right hgl (norm_nonneg n)
    nlinarith [norm_nonneg w, norm_nonneg g, norm_nonneg ℓ, norm_nonneg n]
  have hq : Real.sqrt (g e e) ≤ Real.sqrt ‖g‖ * ‖e‖ := by
    have : g e e ≤ ‖g‖ * ‖e‖ ^ 2 := by
      have := g.le_opNorm₂ e e
      rw [Real.norm_eq_abs] at this
      nlinarith [le_abs_self (g e e)]
    calc Real.sqrt (g e e) ≤ Real.sqrt (‖g‖ * ‖e‖ ^ 2) := Real.sqrt_le_sqrt this
      _ = Real.sqrt ‖g‖ * ‖e‖ := by
        rw [Real.sqrt_mul (norm_nonneg g), Real.sqrt_sq (norm_nonneg e)]
  have hsq : Real.sqrt (2 * a * b) = Real.sqrt (2 * (a / b)) * b := by
    have : 2 * a * b = 2 * (a / b) * b ^ 2 := by field_simp
    rw [this, Real.sqrt_mul (by positivity), Real.sqrt_sq hb'.le]
  -- assemble
  have hval : ((b)⁻¹ • ξ + g ℓ) w = (ξ w - b * (-g ℓ w)) / b := by
    simp only [FunLike.coe_add, FunLike.coe_smul, Pi.add_apply,
      Pi.smul_apply, smul_eq_mul]
    have hbb : b⁻¹ * b = 1 := inv_mul_cancel₀ hb'.ne'
    rw [eq_div_iff hb'.ne']
    linear_combination (ξ w) * hbb
  rw [hval, Real.norm_eq_abs, abs_div, abs_of_pos hb', div_le_iff₀ hb']
  rw [hsq] at hP
  have hs0 : 0 ≤ Real.sqrt (2 * (a / b)) := Real.sqrt_nonneg _
  have hsg : 0 ≤ Real.sqrt ‖g‖ := Real.sqrt_nonneg _
  have hab : a = a / b * b := by field_simp
  calc |ξ w - b * -g ℓ w| ≤ a * |g n w| + Real.sqrt (2 * (a / b)) * b * Real.sqrt (g e e) := hP
    _ ≤ a / b * b * (‖g‖ * ‖n‖ * ‖w‖) +
        Real.sqrt (2 * (a / b)) * b * (Real.sqrt ‖g‖ * ((1 + 2 * (‖g‖ * ‖n‖) * ‖ℓ‖) * ‖w‖)) := by
      rw [← hab]
      gcongr
      exact hq.trans (mul_le_mul_of_nonneg_left he hsg)
    _ = _ := by ring

/-- `a` eventually positive and bounded above, `b → ∞` ⟹ `a/b → 0`. -/
theorem tc_ratio_of_bounded {ι : Type*} {L : Filter ι} {a b : ι → ℝ} {A : ℝ}
    (ha : ∀ᶠ i in L, 0 < a i) (hA : ∀ᶠ i in L, a i ≤ A) (hb : Tendsto b L atTop) :
    Tendsto (fun i => a i / b i) L (𝓝 0) := by
  have hAb : Tendsto (fun i => A / b i) L (𝓝 0) := tendsto_const_nhds.div_atTop hb
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hAb ?_ ?_
  · filter_upwards [ha, hb.eventually_gt_atTop 0] with i h1 h2; positivity
  · filter_upwards [hA, hb.eventually_gt_atTop 0] with i h1 h2
    exact div_le_div_of_nonneg_right h1 h2.le

/-- **① The corollary, moving frames and moving metrics, in operator norm.** Along any filter, if
the frame hypotheses hold eventually, `‖g_i‖`, `‖g_i‖‖n_i‖` and `‖ℓ_i‖` stay bounded, and
`ξ_i(ℓ_i)/ξ_i(n_i) → 0`, then `ξ_i/ξ_i(n_i) + g_i(ℓ_i,·) → 0` in operator norm. -/
theorem tc_tendsto {ι : Type*} {L : Filter ι} {g : ι → E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : ι → E}
    {ξ : ι → E →L[ℝ] ℝ} {C : ℝ} (hF : ∀ᶠ i in L, FrameHyp (g i) (ℓ i) (n i) (ξ i))
    (hg : ∀ᶠ i in L, ‖g i‖ ≤ C) (hgn : ∀ᶠ i in L, ‖g i‖ * ‖n i‖ ≤ C)
    (hl : ∀ᶠ i in L, ‖ℓ i‖ ≤ C)
    (hr : Tendsto (fun i => ξ i (ℓ i) / ξ i (n i)) L (𝓝 0)) :
    Tendsto (fun i => (ξ i (n i))⁻¹ • ξ i + g i (ℓ i)) L (𝓝 0) := by
  set K := Real.sqrt C * (1 + 2 * C * C)
  have hlim : Tendsto (fun i => ξ i (ℓ i) / ξ i (n i) * C +
      Real.sqrt (2 * (ξ i (ℓ i) / ξ i (n i))) * K) L (𝓝 0) := by
    have h1 := hr.mul_const C
    have h2 := ((Real.continuous_sqrt.tendsto _).comp (hr.const_mul 2)).mul_const K
    simpa using h1.add h2
  refine squeeze_zero_norm' ?_ hlim
  filter_upwards [hF, hg, hgn, hl] with i hFi hgi hgni hli
  refine (tc_opNorm_bound hFi).trans ?_
  have hξ' : ∀ v, FutCausal (bil (g i)) (ℓ i) (n i) v → 0 < ((ξ i) : E →ₗ[ℝ] ℝ) v := hFi.2
  obtain ⟨ha, hb⟩ := tc_pos hFi.1 hξ'
  have ha' : 0 < ξ i (ℓ i) := ha
  have hb' : 0 < ξ i (n i) := hb
  have hr0 : 0 ≤ ξ i (ℓ i) / ξ i (n i) := by positivity
  have hC : 0 ≤ C := (norm_nonneg (g i)).trans hgi
  have h1 : Real.sqrt ‖g i‖ ≤ Real.sqrt C := Real.sqrt_le_sqrt hgi
  have h2 : 1 + 2 * (‖g i‖ * ‖n i‖) * ‖ℓ i‖ ≤ 1 + 2 * C * C := by
    nlinarith [mul_le_mul hgni hli (norm_nonneg _) hC]
  have hK : Real.sqrt ‖g i‖ * (1 + 2 * (‖g i‖ * ‖n i‖) * ‖ℓ i‖) ≤ K :=
    mul_le_mul h1 h2 (by positivity) (Real.sqrt_nonneg _)
  exact add_le_add (mul_le_mul_of_nonneg_left hgni hr0)
    (mul_le_mul_of_nonneg_left hK (Real.sqrt_nonneg _))

/-- The limit form: if moreover `g_i(ℓ_i,·) → G₀`, then `ξ_i/ξ_i(n_i) → −G₀` in operator norm. -/
theorem tc_tendsto_limit {ι : Type*} {L : Filter ι} {g : ι → E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : ι → E}
    {ξ : ι → E →L[ℝ] ℝ} {C : ℝ} {G₀ : E →L[ℝ] ℝ}
    (hF : ∀ᶠ i in L, FrameHyp (g i) (ℓ i) (n i) (ξ i))
    (hg : ∀ᶠ i in L, ‖g i‖ ≤ C) (hgn : ∀ᶠ i in L, ‖g i‖ * ‖n i‖ ≤ C)
    (hl : ∀ᶠ i in L, ‖ℓ i‖ ≤ C)
    (hr : Tendsto (fun i => ξ i (ℓ i) / ξ i (n i)) L (𝓝 0))
    (hG : Tendsto (fun i => g i (ℓ i)) L (𝓝 G₀)) :
    Tendsto (fun i => (ξ i (n i))⁻¹ • ξ i) L (𝓝 (-G₀)) := by
  have := (tc_tendsto hF hg hgn hl hr).sub hG
  simpa using this

/-- **① The sequence corollary, fixed frame** (the registered form with `ℓ_m = ℓ`, `n_m = n`):
`ξ_m(ℓ) ≤ A` and `ξ_m(n) → ∞` ⟹ `ξ_m/ξ_m(n) → −g(ℓ,·)` in operator norm, hence pointwise. -/
theorem tc_sequence {g : E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : E} {ξ : ℕ → E →L[ℝ] ℝ} {A : ℝ}
    (hF : ∀ m, FrameHyp g ℓ n (ξ m)) (hA : ∀ m, ξ m ℓ ≤ A)
    (hb : Tendsto (fun m => ξ m n) atTop atTop) :
    Tendsto (fun m => (ξ m n)⁻¹ • ξ m) atTop (𝓝 (-g ℓ)) ∧
      ∀ w, Tendsto (fun m => ξ m w / ξ m n) atTop (𝓝 (-g ℓ w)) := by
  have hpos : ∀ m, 0 < ξ m ℓ := fun m => by
    have hξ' : ∀ v, FutCausal (bil g) ℓ n v → 0 < ((ξ m) : E →ₗ[ℝ] ℝ) v := (hF m).2
    exact (tc_pos (hF m).1 hξ').1
  have hr := tc_ratio_of_bounded (Eventually.of_forall hpos) (Eventually.of_forall hA) hb
  have hop := tc_tendsto_limit (C := max ‖g‖ (max (‖g‖ * ‖n‖) ‖ℓ‖)) (G₀ := g ℓ)
    (Eventually.of_forall hF) (Eventually.of_forall fun _ => le_max_left _ _)
    (Eventually.of_forall fun _ => (le_max_left _ _).trans (le_max_right _ _))
    (Eventually.of_forall fun _ => (le_max_right _ _).trans (le_max_right _ _)) hr
    tendsto_const_nhds
  refine ⟨hop, fun w => ?_⟩
  have := ((ContinuousLinearMap.apply ℝ ℝ w).continuous.tendsto _).comp hop
  simpa [Function.comp_def, div_eq_inv_mul] using this

end Normed

end TCF

section Manifold
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- The chart representative of a vector field (campaign 68). -/
noncomputable def chartRep (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) (y : E) : E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) ((extChartAt 𝓘(ℝ, E) p).symm y)
    (X ((extChartAt 𝓘(ℝ, E) p).symm y))

/-- `(extChartAt p).symm` is manifold-differentiable on the chart target (campaign 68). -/
theorem ld_mdifferentiableAt_symm (p : N) {y : E} (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y := by
  have h := mdifferentiableWithinAt_extChartAt_symm (I := 𝓘(ℝ, E)) (x := p) hy
  rwa [ModelWithCorners.range_eq_univ, mdifferentiableWithinAt_univ] at h

/-- The chart representative of a `(0,2)`-tensor field (campaign 68). -/
noncomputable def hRep
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (p : N) (y : E) : E →L[ℝ] E →L[ℝ] ℝ :=
  let D : E →L[ℝ] E := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y
  let H : E →L[ℝ] E →L[ℝ] ℝ := h ((extChartAt 𝓘(ℝ, E) p).symm y)
  H.bilinearComp D D

theorem ld_hRep_apply
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (p : N) (y v w : E) :
    hRep h p y v w = h ((extChartAt 𝓘(ℝ, E) p).symm y)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y v)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y w) := rfl

theorem ld_mfderiv_symm_chart (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x a) = a := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have h := mfderivWithin_extChartAt_symm_comp_mfderiv_extChartAt' (I := 𝓘(ℝ, E)) hxs
  rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at h
  exact DFunLike.congr_fun h a

theorem ld_mfderiv_chart_symm (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x) a) = a := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have hy := (extChartAt 𝓘(ℝ, E) p).map_source hxs
  have h := mfderiv_extChartAt_comp_mfderivWithin_extChartAt_symm (I := 𝓘(ℝ, E)) hy
  rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at h
  have h0 : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p)
      ((extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x))
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x) a) = a := by
    have := DFunLike.congr_fun h a
    exact this
  have key : ∀ z, z = x → ∀ b : E, mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) z b =
      mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x b := by rintro z rfl b; rfl
  exact (key _ ((extChartAt 𝓘(ℝ, E) p).left_inv hxs) _).symm.trans h0

theorem ld_chartRep_apply_chart (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {x : N}
    (hx : x ∈ (chartAt E p).source) :
    chartRep X p (extChartAt 𝓘(ℝ, E) p x) = mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (X x) := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have key : ∀ z, z = x → mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) z (X z) =
      mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (X x) := by rintro z rfl; rfl
  exact key _ ((extChartAt 𝓘(ℝ, E) p).left_inv hxs)

theorem ld_h_eq_hRep
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a b : E) :
    h x a b = hRep h p (extChartAt 𝓘(ℝ, E) p x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x a)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x b) := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have e1 := ld_mfderiv_symm_chart p hx a
  have e2 := ld_mfderiv_symm_chart p hx b
  have key : ∀ z, z = x → ∀ a' b' : E, a' = a → b' = b → h x a b = h z a' b' := by
    rintro z rfl a' b' rfl rfl; rfl
  exact key _ ((extChartAt 𝓘(ℝ, E) p).left_inv hxs) _ _ e1 e2

/-! ### Chart bookkeeping (new) -/

variable (p₀ : N)

lemma ch_mem_target {x : N} (hx : x ∈ (chartAt E p₀).source) :
    extChartAt 𝓘(ℝ, E) p₀ x ∈ (extChartAt 𝓘(ℝ, E) p₀).target :=
  (extChartAt 𝓘(ℝ, E) p₀).map_source (by rwa [extChartAt_source])

lemma ch_left_inv {x : N} (hx : x ∈ (chartAt E p₀).source) :
    (extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x) = x :=
  (extChartAt 𝓘(ℝ, E) p₀).left_inv (by rwa [extChartAt_source])

lemma ch_symm_mem {y : E} (hy : y ∈ (extChartAt 𝓘(ℝ, E) p₀).target) :
    (extChartAt 𝓘(ℝ, E) p₀).symm y ∈ (chartAt E p₀).source := by
  rw [← extChartAt_source (I := 𝓘(ℝ, E))]; exact (extChartAt 𝓘(ℝ, E) p₀).map_target hy

lemma ch_right_inv {y : E} (hy : y ∈ (extChartAt 𝓘(ℝ, E) p₀).target) :
    extChartAt 𝓘(ℝ, E) p₀ ((extChartAt 𝓘(ℝ, E) p₀).symm y) = y :=
  (extChartAt 𝓘(ℝ, E) p₀).right_inv hy

lemma ch_contAt {x : N} (hx : x ∈ (chartAt E p₀).source) :
    ContinuousAt (extChartAt 𝓘(ℝ, E) p₀) x :=
  continuousAt_extChartAt' (by rwa [extChartAt_source])

/-- For a curve `γ : ℝ → N` differentiable at `s` with `γ s` in the chart: `φ ∘ γ` has derivative
`Dφ (γ' s)` at `s`, where `γ' s = mfderiv γ s 1`. -/
lemma ch_hasDerivAt_chart {γ : ℝ → N} {s : ℝ} (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ s)
    (hs : γ s ∈ (chartAt E p₀).source) :
    HasDerivAt (fun s => extChartAt 𝓘(ℝ, E) p₀ (γ s))
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) (γ s)
        (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ s (1 : ℝ))) s := by
  have hφ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) (γ s) :=
    mdifferentiableAt_extChartAt hs
  have hc := hφ.comp s hγ
  have hd : DifferentiableAt ℝ (extChartAt 𝓘(ℝ, E) p₀ ∘ γ) s :=
    mdifferentiableAt_iff_differentiableAt.1 hc
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀ ∘ γ) s (1 : ℝ) =
      deriv (extChartAt 𝓘(ℝ, E) p₀ ∘ γ) s := by rw [mfderiv_eq_fderiv]; rfl
  have e3 : deriv (extChartAt 𝓘(ℝ, E) p₀ ∘ γ) s = mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E)
      (extChartAt 𝓘(ℝ, E) p₀) (γ s) (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ s (1 : ℝ)) := by
    rw [← e2, mfderiv_comp s hφ hγ]; rfl
  rw [← e3]; exact hd.hasDerivAt

/-- For `β : ℝ → E` differentiable at `s` with `β s` in the chart target: `φ⁻¹ ∘ β` is
manifold-differentiable at `s` with velocity `Dφ⁻¹ (β' s)`. -/
lemma ch_vel_symm {β : ℝ → E} {s : ℝ} (hβ : DifferentiableAt ℝ β s)
    (hs : β s ∈ (extChartAt 𝓘(ℝ, E) p₀).target) :
    MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (fun s => (extChartAt 𝓘(ℝ, E) p₀).symm (β s)) s ∧
      (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (fun s => (extChartAt 𝓘(ℝ, E) p₀).symm (β s)) s (1 : ℝ) : E) =
        mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm (β s) (deriv β s) := by
  have hφ := ld_mdifferentiableAt_symm p₀ hs
  have hb : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) β s := mdifferentiableAt_iff_differentiableAt.2 hβ
  refine ⟨hφ.comp s hb, ?_⟩
  have e : (fun s => (extChartAt 𝓘(ℝ, E) p₀).symm (β s)) = (extChartAt 𝓘(ℝ, E) p₀).symm ∘ β := rfl
  rw [e, mfderiv_comp s hφ hb]
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) β s (1 : ℝ) = deriv β s := by rw [mfderiv_eq_fderiv]; rfl
  change mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm (β s)
    (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) β s (1 : ℝ)) = _
  exact congrArg _ e2


/-! ### The manifold spacetime (intrinsic definitions) -/

variable (E N) in
/-- **A time-oriented Lorentzian region of a manifold** `N` (intrinsic): an open `M ⊆ N`, a section
`g` of `T*N ⊗ T*N`, symmetric, and a section `T` of `TN`, timelike on `M`, with `g` positive on
`T^⊥` at points of `M`. (Mathlib's `TangentSpace 𝓘(ℝ,E) x` is by definition `E`; tangent vectors are
read in the preferred chart `chartAt E x`, which is how Mathlib's `mfderiv` is defined.) -/
structure MSpacetime where
  M : Set N
  isOpen_M : IsOpen M
  g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ
  symm : ∀ x (v w : E), g x v w = g x w v
  T : Π x : N, TangentSpace 𝓘(ℝ, E) x
  T_timelike : ∀ x ∈ M, g x (T x) (T x) < 0
  pos_on_perp : ∀ x ∈ M, ∀ v : E, g x v (T x) = 0 → v ≠ 0 → 0 < g x v v

namespace MSpacetime
variable (S : MSpacetime E N)

/-- `g_x` read as a bilinear form on `E` (Mathlib's `T_xN` is `E` by definition). -/
def gE (x : N) : E →L[ℝ] E →L[ℝ] ℝ := S.g x

/-- Future-directed timelike tangent vector at `x`. -/
def FutTimelike (x : N) (v : E) : Prop := S.gE x v v < 0 ∧ S.gE x v (S.T x) < 0
/-- Future-directed causal tangent vector at `x`. -/
def FutCausal (x : N) (v : E) : Prop := S.gE x v v ≤ 0 ∧ S.gE x v (S.T x) < 0

/-- `dτ_x(v) = mfderiv τ x v`, for `τ : N → ℝ`. -/
noncomputable def dfun (τ : N → ℝ) (x : N) (v : E) : ℝ := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) τ x v

/-- The velocity `γ'(t) = mfderiv γ t 1 ∈ T_{γ t} N` of a curve `γ : ℝ → N`. -/
noncomputable def vel (γ : ℝ → N) (t : ℝ) : E := mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)

/-- **The manifold timelike step** (intrinsic): a `C¹` curve `ℝ → N` (`ContMDiff`) from `x` to `y`,
inside `M` and with future-timelike `mfderiv` velocity on `[0,1]`. -/
def TStep (x y : N) : Prop :=
  ∃ γ : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (vel γ t)

/-- The manifold causal step (intrinsic). -/
def CStep (x y : N) : Prop :=
  ∃ γ : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (vel γ t)

def Chr (x y : N) : Prop := Relation.TransGen S.TStep x y
def Cau (x y : N) : Prop := Relation.ReflTransGen S.CStep x y
def Ipast (p : N) : Set N := {q | S.Chr q p}
def Jpast (p : N) : Set N := {q | S.Cau q p}
def IpastSet (A : Set N) : Set N := ⋃ p ∈ A, S.Ipast p
def JpastSet (A : Set N) : Set N := ⋃ p ∈ A, S.Jpast p
/-- `D = I⁻(J)` on `N`. -/
def D (J : Set N) : Set N := S.IpastSet J
/-- `𝓗⁺ = ∂_N J⁻(J)`: the frontier in `N`. -/
def H (J : Set N) : Set N := frontier (S.JpastSet J)
def slice (J : Set N) (Θ : N → ℝ) (τ : ℝ) : Set N := {x | x ∈ S.D J ∧ Θ x = τ}
def SublevelProper (J : Set N) (Θ : N → ℝ) : Prop :=
  ∀ T : ℝ, closure {x | x ∈ S.D J ∧ Θ x ≤ T} ⊆ S.D J

/-- **Temporal on an open `U`** (intrinsic): `τ` is `C¹` on `U` (`ContMDiffOn`) and
`dτ = mfderiv τ` is positive on future-causal vectors. -/
def IsTemporalOn (U : Set N) (τ : N → ℝ) : Prop :=
  ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 τ U ∧
    ∀ x ∈ U, ∀ v : E, S.FutCausal x v → 0 < dfun τ x v

/-- An inextendible piecewise-`C¹` future causal curve in `U` (intrinsic). -/
structure InextCausalCurveIn (U : Set N) where
  γ : ℝ → N
  cont : Continuous γ
  mem : ∀ t, γ t ∈ U
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t ∉ brk, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t ∧ S.FutCausal (γ t) (vel γ t)
  inext_future : ¬ ∃ p ∈ U, Tendsto γ atTop (𝓝 p)
  inext_past : ¬ ∃ p ∈ U, Tendsto γ atBot (𝓝 p)

/-- A Cauchy temporal function on `U` (intrinsic; campaign 60's definition read on `N`). -/
def IsCauchyTemporalOn (U : Set N) (τ : N → ℝ) : Prop :=
  S.IsTemporalOn U τ ∧ ∀ c : S.InextCausalCurveIn U, ∀ a : ℝ, ∃! t : ℝ, τ (c.γ t) = a

lemma futTimelike_smul {x : N} {u : E} {c : ℝ} (hc : 0 < c) (h : S.FutTimelike x u) :
    S.FutTimelike x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul]
    change c * S.gE x u (S.T x) < 0
    nlinarith

lemma futCausal_smul {x : N} {u : E} {c : ℝ} (hc : 0 < c) (h : S.FutCausal x u) :
    S.FutCausal x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul]
    change c * S.gE x u (S.T x) < 0
    nlinarith

lemma tstep_mem {x y : N} (h : S.TStep x y) : x ∈ S.M ∧ y ∈ S.M := by
  obtain ⟨γ, -, h0, h1, hγ⟩ := h
  exact ⟨h0 ▸ (hγ 0 ⟨le_rfl, zero_le_one⟩).1, h1 ▸ (hγ 1 ⟨zero_le_one, le_rfl⟩).1⟩

lemma cstep_mem {x y : N} (h : S.CStep x y) : x ∈ S.M ∧ y ∈ S.M := by
  obtain ⟨γ, -, h0, h1, hγ⟩ := h
  exact ⟨h0 ▸ (hγ 0 ⟨le_rfl, zero_le_one⟩).1, h1 ▸ (hγ 1 ⟨zero_le_one, le_rfl⟩).1⟩

lemma chr_mem {x y : N} (h : S.Chr x y) : x ∈ S.M ∧ y ∈ S.M := by
  induction h with
  | single h => exact S.tstep_mem h
  | tail _ h ih => exact ⟨ih.1, (S.tstep_mem h).2⟩

lemma D_subset_M (J : Set N) : S.D J ⊆ S.M := fun x hx => by
  obtain ⟨p, -, h⟩ := mem_iUnion₂.1 hx
  exact (S.chr_mem h).1

lemma JpastSet_subset_M {J : Set N} (hJ : J ⊆ S.M) : S.JpastSet J ⊆ S.M := fun x hx => by
  obtain ⟨p, hp, h⟩ := mem_iUnion₂.1 hx
  rcases Relation.ReflTransGen.cases_head h with h | ⟨b, hb, -⟩
  · exact h ▸ hJ hp
  · exact (S.cstep_mem hb).1

lemma tstep_cstep {x y : N} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨(ht t htI).1, (ht t htI).2.1.le, (ht t htI).2.2⟩⟩

lemma chr_cau {x y : N} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_cstep h)

lemma D_subset_JpastSet (J : Set N) : S.D J ⊆ S.JpastSet J := fun x hx => by
  obtain ⟨p, hp, h⟩ := mem_iUnion₂.1 hx
  exact mem_iUnion₂.2 ⟨p, hp, S.chr_cau h⟩

/-! ### The chart spacetime (chart-defined) -/

/-- **The one-chart hypothesis** (chart-defined regularity): `M` lies in the source of the preferred
chart at `p₀`, the chart representative `hRep g p₀` is `C¹` and `chartRep T p₀` is continuous on
`φ(M)`. -/
structure OneChart (p₀ : N) : Prop where
  sub : S.M ⊆ (chartAt E p₀).source
  g_C1 : ContDiffOn ℝ 1 (hRep S.g p₀) (extChartAt 𝓘(ℝ, E) p₀ '' S.M)
  T_cont : ContinuousOn (chartRep S.T p₀) (extChartAt 𝓘(ℝ, E) p₀ '' S.M)

variable {S} {p₀ : N}

lemma isOpen_chartImage (hC : S.OneChart p₀) : IsOpen (extChartAt 𝓘(ℝ, E) p₀ '' S.M) := by
  have hs : S.M ⊆ (extChartAt 𝓘(ℝ, E) p₀).source := by rw [extChartAt_source]; exact hC.sub
  rw [(extChartAt 𝓘(ℝ, E) p₀).image_eq_target_inter_inv_preimage hs]
  exact (continuousOn_extChartAt_symm p₀).isOpen_inter_preimage (isOpen_extChartAt_target p₀)
    S.isOpen_M

lemma chart_g {x : N} (hx : x ∈ (chartAt E p₀).source) (a b : E) :
    hRep S.g p₀ (extChartAt 𝓘(ℝ, E) p₀ x) (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x a)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x b) = S.g x a b :=
  (ld_h_eq_hRep S.g p₀ hx a b).symm

/-- **The chart spacetime** on `E`: `M_V = φ(M)`, `g_V = hRep g p₀`, `T_V = chartRep T p₀`. -/
noncomputable def chartSp (hC : S.OneChart p₀) : Spacetime E where
  M := extChartAt 𝓘(ℝ, E) p₀ '' S.M
  isOpen_M := isOpen_chartImage hC
  g := hRep S.g p₀
  cont_g := hC.g_C1.continuousOn
  symm y v w := by rw [ld_hRep_apply, ld_hRep_apply]; exact S.symm _ _ _
  T := chartRep S.T p₀
  cont_T := hC.T_cont
  T_timelike := by
    rintro _ ⟨x, hx, rfl⟩
    rw [ld_chartRep_apply_chart _ _ (hC.sub hx), chart_g (hC.sub hx) (S.T x) (S.T x)]
    exact S.T_timelike x hx
  pos_on_perp := by
    rintro _ ⟨x, hx, rfl⟩ w hw hw0
    have hxs := hC.sub hx
    obtain ⟨v, rfl⟩ : ∃ v : E, mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x v = w :=
      ⟨_, ld_mfderiv_chart_symm p₀ hxs w⟩
    rw [ld_chartRep_apply_chart _ _ hxs, chart_g hxs v (S.T x)] at hw
    rw [chart_g hxs v v]
    refine S.pos_on_perp x hx v hw fun hv => hw0 ?_
    rw [hv]; exact map_zero _

variable (hC : S.OneChart p₀)
include hC

lemma futTimelike_chart {x : N} (hx : x ∈ (chartAt E p₀).source) (v : E) :
    (chartSp hC).FutTimelike (extChartAt 𝓘(ℝ, E) p₀ x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x v) ↔ S.FutTimelike x v := by
  show hRep S.g p₀ _ _ _ < 0 ∧ hRep S.g p₀ _ _ (chartRep S.T p₀ _) < 0 ↔ _
  rw [ld_chartRep_apply_chart _ _ hx, chart_g hx v v, chart_g hx v (S.T x)]; rfl

lemma futCausal_chart {x : N} (hx : x ∈ (chartAt E p₀).source) (v : E) :
    (chartSp hC).FutCausal (extChartAt 𝓘(ℝ, E) p₀ x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x v) ↔ S.FutCausal x v := by
  show hRep S.g p₀ _ _ _ ≤ 0 ∧ hRep S.g p₀ _ _ (chartRep S.T p₀ _) < 0 ↔ _
  rw [ld_chartRep_apply_chart _ _ hx, chart_g hx v v, chart_g hx v (S.T x)]; rfl

lemma futTimelike_chart' {u : E} (hu : u ∈ (extChartAt 𝓘(ℝ, E) p₀).target) (w : E) :
    (chartSp hC).FutTimelike u w ↔ S.FutTimelike ((extChartAt 𝓘(ℝ, E) p₀).symm u)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm u w) := by
  obtain ⟨x, hx, rfl⟩ : ∃ x ∈ (chartAt E p₀).source, extChartAt 𝓘(ℝ, E) p₀ x = u :=
    ⟨_, ch_symm_mem p₀ hu, ch_right_inv p₀ hu⟩
  have h1 := futTimelike_chart hC hx
    (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x) w)
  rw [ld_mfderiv_chart_symm p₀ hx w] at h1
  have key : ∀ z, z = x → ∀ v : E, (S.FutTimelike x v ↔ S.FutTimelike z v) := by rintro z rfl v; rfl
  exact h1.trans (key _ (ch_left_inv p₀ hx) _)

lemma futCausal_chart' {u : E} (hu : u ∈ (extChartAt 𝓘(ℝ, E) p₀).target) (w : E) :
    (chartSp hC).FutCausal u w ↔ S.FutCausal ((extChartAt 𝓘(ℝ, E) p₀).symm u)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm u w) := by
  obtain ⟨x, hx, rfl⟩ : ∃ x ∈ (chartAt E p₀).source, extChartAt 𝓘(ℝ, E) p₀ x = u :=
    ⟨_, ch_symm_mem p₀ hu, ch_right_inv p₀ hu⟩
  have h1 := futCausal_chart hC hx
    (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x) w)
  rw [ld_mfderiv_chart_symm p₀ hx w] at h1
  have key : ∀ z, z = x → ∀ v : E, (S.FutCausal x v ↔ S.FutCausal z v) := by rintro z rfl v; rfl
  exact h1.trans (key _ (ch_left_inv p₀ hx) _)

end MSpacetime

/-! ### The curve transfer (the registered likeliest stop): squash + `mfderiv`/`deriv` -/

variable {p₀ : N}

/-- `Dφ_x` with values in `E` (`T_{φ x}E = E`). -/
noncomputable def dchart (p₀ x : N) (v : E) : E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x v
/-- `Dφ⁻¹_u` with values in `E`. -/
noncomputable def dchartInv (p₀ : N) (u w : E) : E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm u w

lemma dchartInv_smul (u w : E) (c : ℝ) : dchartInv p₀ u (c • w) = c • dchartInv p₀ u w :=
  (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm u).map_smul c w

/-- **Curves, `N → V`.** A `C¹` curve of `N` inside `M ⊆ src` on `[0,1]` with `P`-velocity there gives
a `C¹` curve `β = φ ∘ γ ∘ σ` of `E` on all of `ℝ` (squash `σ`, since `φ ∘ γ` is only defined near
`[0,1]`), inside `φ(M)` with `Q`-velocity on `[0,1]`. -/
theorem ch_curve_NV {M : Set N} (hsub : M ⊆ (chartAt E p₀).source) {P : N → E → Prop}
    {Q : E → E → Prop}
    (hPQ : ∀ x ∈ (chartAt E p₀).source, ∀ v : E, P x v →
      Q (extChartAt 𝓘(ℝ, E) p₀ x) (dchart p₀ x v))
    (hQ : ∀ u w (c : ℝ), 0 < c → Q u w → Q u (c • w))
    {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ M ∧ P (γ t) (MSpacetime.vel γ t)) :
    ∃ β : ℝ → E, ContDiff ℝ 1 β ∧ β 0 = extChartAt 𝓘(ℝ, E) p₀ (γ 0) ∧
      β 1 = extChartAt 𝓘(ℝ, E) p₀ (γ 1) ∧
      ∀ t ∈ Icc (0:ℝ) 1, β t ∈ extChartAt 𝓘(ℝ, E) p₀ '' M ∧ Q (β t) (deriv β t) := by
  have hU : IsOpen (γ ⁻¹' (chartAt E p₀).source) :=
    (chartAt E p₀).open_source.preimage hγ.continuous
  obtain ⟨δ, hδ, hδU⟩ := ch_exists_Ioo hU fun t ht' => hsub (ht t ht').1
  obtain ⟨σ, hσ, hσ0, hσ1, hσr, hσd, hσI⟩ := ch_squash hδ
  have hsrc : ∀ t, γ (σ t) ∈ (chartAt E p₀).source := fun t => hδU (hσr t)
  have hφγ : ∀ s, γ s ∈ (chartAt E p₀).source →
      HasDerivAt (fun s => extChartAt 𝓘(ℝ, E) p₀ (γ s)) (dchart p₀ (γ s) (MSpacetime.vel γ s)) s :=
    fun s hs => ch_hasDerivAt_chart p₀ (hγ.mdifferentiableAt one_ne_zero) hs
  refine ⟨fun t => extChartAt 𝓘(ℝ, E) p₀ (γ (σ t)), ?_, by simp only [hσ0], by simp only [hσ1],
    fun t htI => ?_⟩
  · refine contDiff_iff_contDiffAt.2 fun t => ?_
    have h1 : ContMDiffAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 (fun s => extChartAt 𝓘(ℝ, E) p₀ (γ s)) (σ t) :=
      (contMDiffAt_extChartAt' (hsrc t)).comp (σ t) (hγ (σ t))
    exact (contMDiffAt_iff_contDiffAt.1 h1).comp t hσ.contDiffAt
  · have hd : HasDerivAt (fun t => extChartAt 𝓘(ℝ, E) p₀ (γ (σ t)))
        (deriv σ t • dchart p₀ (γ (σ t)) (MSpacetime.vel γ (σ t))) t :=
      (hφγ _ (hsrc t)).scomp t (hσd t).1
    rw [hd.deriv]
    obtain ⟨hm, hP⟩ := ht _ (hσI t htI)
    exact ⟨⟨_, hm, rfl⟩, hQ _ _ _ (hσd t).2 (hPQ _ (hsub hm) _ hP)⟩

/-- **Curves, `V → N`.** The converse: `γ = φ⁻¹ ∘ β ∘ σ`. -/
theorem ch_curve_VN {M : Set N} (hsub : M ⊆ (chartAt E p₀).source) {P : N → E → Prop}
    {Q : E → E → Prop}
    (hQP : ∀ u ∈ (extChartAt 𝓘(ℝ, E) p₀).target, ∀ w : E, Q u w →
      P ((extChartAt 𝓘(ℝ, E) p₀).symm u) (dchartInv p₀ u w))
    (hP : ∀ x v (c : ℝ), 0 < c → P x v → P x (c • v))
    {β : ℝ → E} (hβ : ContDiff ℝ 1 β)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, β t ∈ extChartAt 𝓘(ℝ, E) p₀ '' M ∧ Q (β t) (deriv β t)) :
    ∃ γ : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ ∧ γ 0 = (extChartAt 𝓘(ℝ, E) p₀).symm (β 0) ∧
      γ 1 = (extChartAt 𝓘(ℝ, E) p₀).symm (β 1) ∧
      ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ M ∧ P (γ t) (MSpacetime.vel γ t) := by
  have himg : ∀ {u}, u ∈ extChartAt 𝓘(ℝ, E) p₀ '' M → u ∈ (extChartAt 𝓘(ℝ, E) p₀).target ∧
      (extChartAt 𝓘(ℝ, E) p₀).symm u ∈ M := by
    rintro _ ⟨x, hx, rfl⟩
    exact ⟨ch_mem_target p₀ (hsub hx), by rw [ch_left_inv p₀ (hsub hx)]; exact hx⟩
  have hU : IsOpen (β ⁻¹' (extChartAt 𝓘(ℝ, E) p₀).target) :=
    (isOpen_extChartAt_target p₀).preimage hβ.continuous
  obtain ⟨δ, hδ, hδU⟩ := ch_exists_Ioo hU fun t ht' => (himg (ht t ht').1).1
  obtain ⟨σ, hσ, hσ0, hσ1, hσr, hσd, hσI⟩ := ch_squash hδ
  have htg : ∀ t, β (σ t) ∈ (extChartAt 𝓘(ℝ, E) p₀).target := fun t => hδU (hσr t)
  have hβσ : ContDiff ℝ 1 (fun t => β (σ t)) := hβ.comp hσ
  refine ⟨fun t => (extChartAt 𝓘(ℝ, E) p₀).symm (β (σ t)), fun t => ?_, by simp only [hσ0],
    by simp only [hσ1], fun t htI => ?_⟩
  · have h1 : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E) 1 (extChartAt 𝓘(ℝ, E) p₀).symm (β (σ t)) :=
      (contMDiffOn_extChartAt_symm p₀).contMDiffAt
        ((isOpen_extChartAt_target p₀).mem_nhds (htg t))
    exact h1.comp t ((contMDiff_iff_contDiff.2 hβσ) t)
  · obtain ⟨-, hv⟩ := ch_vel_symm p₀ (hβσ.differentiable one_ne_zero t) (htg t)
    have hd : HasDerivAt (fun t => β (σ t)) (deriv σ t • deriv β (σ t)) t :=
      ((hβ.differentiable one_ne_zero (σ t)).hasDerivAt).scomp t (hσd t).1
    obtain ⟨hm, hQ⟩ := ht _ (hσI t htI)
    refine ⟨(himg hm).2, ?_⟩
    have e : MSpacetime.vel (fun t => (extChartAt 𝓘(ℝ, E) p₀).symm (β (σ t))) t =
        deriv σ t • dchartInv p₀ (β (σ t)) (deriv β (σ t)) := by
      have hv' : MSpacetime.vel (fun t => (extChartAt 𝓘(ℝ, E) p₀).symm (β (σ t))) t =
          dchartInv p₀ (β (σ t)) (deriv (fun t => β (σ t)) t) := hv
      rw [hv', hd.deriv, dchartInv_smul]
    have key := hP _ _ _ (hσd t).2 (hQP _ (htg t) _ hQ)
    rw [← e] at key
    exact key

namespace MSpacetime
variable {S : MSpacetime E N} (hC : S.OneChart p₀)
include hC

theorem ch_tstep_NV {x y : N} (h : S.TStep x y) :
    (chartSp hC).TStep (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  obtain ⟨γ, hγ, rfl, rfl, ht⟩ := h
  exact ch_curve_NV hC.sub (fun x hx v h => (futTimelike_chart hC hx v).2 h)
    (fun u w c hc h => (chartSp hC).futTimelike_smul hc h) hγ ht

theorem ch_cstep_NV {x y : N} (h : S.CStep x y) :
    (chartSp hC).CStep (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  obtain ⟨γ, hγ, rfl, rfl, ht⟩ := h
  exact ch_curve_NV hC.sub (fun x hx v h => (futCausal_chart hC hx v).2 h)
    (fun u w c hc h => (chartSp hC).ch_futCausal_smul hc h) hγ ht

theorem ch_tstep_VN {u v : E} (h : (chartSp hC).TStep u v) :
    S.TStep ((extChartAt 𝓘(ℝ, E) p₀).symm u) ((extChartAt 𝓘(ℝ, E) p₀).symm v) := by
  obtain ⟨β, hβ, rfl, rfl, ht⟩ := h
  exact ch_curve_VN hC.sub (fun u hu w h => (futTimelike_chart' hC hu w).1 h)
    (fun x v c hc h => S.futTimelike_smul hc h) hβ ht

theorem ch_cstep_VN {u v : E} (h : (chartSp hC).CStep u v) :
    S.CStep ((extChartAt 𝓘(ℝ, E) p₀).symm u) ((extChartAt 𝓘(ℝ, E) p₀).symm v) := by
  obtain ⟨β, hβ, rfl, rfl, ht⟩ := h
  exact ch_curve_VN hC.sub (fun u hu w h => (futCausal_chart' hC hu w).1 h)
    (fun x v c hc h => S.futCausal_smul hc h) hβ ht

/-- **`TStep` transfer (BUILT).** For `x, y` in the chart: `TStep_N x y ↔ TStep_V (φ x) (φ y)`. -/
theorem ch_tstep_iff {x y : N} (hx : x ∈ (chartAt E p₀).source) (hy : y ∈ (chartAt E p₀).source) :
    S.TStep x y ↔ (chartSp hC).TStep (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  refine ⟨ch_tstep_NV hC, fun h => ?_⟩
  have := ch_tstep_VN hC h
  rwa [ch_left_inv p₀ hx, ch_left_inv p₀ hy] at this

/-- **`≪` transfer (BUILT).** -/
theorem ch_chr_iff {x y : N} (hx : x ∈ (chartAt E p₀).source) (hy : y ∈ (chartAt E p₀).source) :
    S.Chr x y ↔ (chartSp hC).Chr (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  refine ⟨fun h => Relation.TransGen.lift _ (fun a b hab => ch_tstep_NV hC hab) _ _ h, fun h => ?_⟩
  have : S.Chr ((extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x))
      ((extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ y)) :=
    Relation.TransGen.lift (r := (chartSp hC).TStep) (p := S.TStep)
      (fun u => (extChartAt 𝓘(ℝ, E) p₀).symm u) (fun a b hab => ch_tstep_VN hC hab) _ _ h
  rwa [ch_left_inv p₀ hx, ch_left_inv p₀ hy] at this

/-- **`≤` transfer (BUILT).** -/
theorem ch_cau_iff {x y : N} (hx : x ∈ (chartAt E p₀).source) (hy : y ∈ (chartAt E p₀).source) :
    S.Cau x y ↔ (chartSp hC).Cau (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  refine ⟨fun h => Relation.ReflTransGen.lift _ (fun a b hab => ch_cstep_NV hC hab) _ _ h, fun h => ?_⟩
  have : S.Cau ((extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x))
      ((extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ y)) :=
    Relation.ReflTransGen.lift (r := (chartSp hC).CStep) (p := S.CStep)
      (fun u => (extChartAt 𝓘(ℝ, E) p₀).symm u) (fun a b hab => ch_cstep_VN hC hab) _ _ h
  rwa [ch_left_inv p₀ hx, ch_left_inv p₀ hy] at this

/-! ### Sets: `D`, `J⁻`, `𝓗⁺`, slices -/

theorem ch_mem_D_iff {A : Set N} (hA : A ⊆ (chartAt E p₀).source) {x : N}
    (hx : x ∈ (chartAt E p₀).source) :
    x ∈ S.D A ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' A) := by
  constructor
  · intro h
    obtain ⟨p, hp, h⟩ := mem_iUnion₂.1 h
    exact mem_iUnion₂.2 ⟨_, mem_image_of_mem _ hp, (ch_chr_iff hC hx (hA hp)).1 h⟩
  · intro h
    obtain ⟨_, ⟨p, hp, rfl⟩, h⟩ := mem_iUnion₂.1 h
    exact mem_iUnion₂.2 ⟨p, hp, (ch_chr_iff hC hx (hA hp)).2 h⟩

theorem ch_mem_JpastSet_iff {A : Set N} (hA : A ⊆ (chartAt E p₀).source) {x : N}
    (hx : x ∈ (chartAt E p₀).source) :
    x ∈ S.JpastSet A ↔
      extChartAt 𝓘(ℝ, E) p₀ x ∈ (chartSp hC).JpastSet (extChartAt 𝓘(ℝ, E) p₀ '' A) := by
  constructor
  · intro h
    obtain ⟨p, hp, h⟩ := mem_iUnion₂.1 h
    exact mem_iUnion₂.2 ⟨_, mem_image_of_mem _ hp, (ch_cau_iff hC hx (hA hp)).1 h⟩
  · intro h
    obtain ⟨_, ⟨p, hp, rfl⟩, h⟩ := mem_iUnion₂.1 h
    exact mem_iUnion₂.2 ⟨p, hp, (ch_cau_iff hC hx (hA hp)).2 h⟩

/-- `D` of the chart spacetime, read through `φ⁻¹`. -/
theorem ch_mem_chartD_iff {A : Set N} (hA : A ⊆ (chartAt E p₀).source) {u : E} :
    u ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' A) ↔
      u ∈ (extChartAt 𝓘(ℝ, E) p₀).target ∧ (extChartAt 𝓘(ℝ, E) p₀).symm u ∈ S.D A := by
  constructor
  · intro h
    obtain ⟨x, hxM, rfl⟩ := (chartSp hC).hl_D_subset_M _ h
    have hx := hC.sub hxM
    exact ⟨ch_mem_target p₀ hx, by rw [ch_left_inv p₀ hx]; exact (ch_mem_D_iff hC hA hx).2 h⟩
  · rintro ⟨hu, h⟩
    have := (ch_mem_D_iff hC hA (ch_symm_mem p₀ hu)).1 h
    rwa [ch_right_inv p₀ hu] at this

theorem ch_isOpen_D (J : Set N) (hJ : J ⊆ (chartAt E p₀).source) : IsOpen (S.D J) := by
  have e : S.D J = (chartAt E p₀).source ∩
      extChartAt 𝓘(ℝ, E) p₀ ⁻¹' (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J) := by
    ext x
    exact ⟨fun h => ⟨hC.sub (S.D_subset_M J h), (ch_mem_D_iff hC hJ (hC.sub (S.D_subset_M J h))).1 h⟩,
      fun h => (ch_mem_D_iff hC hJ h.1).2 h.2⟩
  rw [e]
  have hc : ContinuousOn (extChartAt 𝓘(ℝ, E) p₀) (chartAt E p₀).source := by
    rw [← extChartAt_source (I := 𝓘(ℝ, E))]; exact continuousOn_extChartAt p₀
  exact hc.isOpen_inter_preimage (chartAt E p₀).open_source ((chartSp hC).hl_D_open _)

end MSpacetime

/-! ### Topology through the chart: closure, frontier, Kuratowski limits -/

/-- For `A ⊆ N`, `B ⊆ E` that correspond on the chart (`x ∈ A ↔ φ x ∈ B` for `x` in the source):
`p ∈ closure A ↔ φ p ∈ closure B` at points of the source. -/
theorem ch_mem_closure_iff {A : Set N} {B : Set E}
    (hAB : ∀ x ∈ (chartAt E p₀).source, x ∈ A ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ B) {p : N}
    (hp : p ∈ (chartAt E p₀).source) :
    p ∈ closure A ↔ extChartAt 𝓘(ℝ, E) p₀ p ∈ closure B := by
  constructor
  · intro h
    have h1 : p ∈ closure ((chartAt E p₀).source ∩ A) :=
      (chartAt E p₀).open_source.inter_closure ⟨hp, h⟩
    refine closure_mono ?_ (mem_closure_image (ch_contAt p₀ hp) h1)
    rintro _ ⟨x, ⟨hx, hxA⟩, rfl⟩
    exact (hAB x hx).1 hxA
  · intro h
    have ht := ch_mem_target p₀ hp
    have h1 : extChartAt 𝓘(ℝ, E) p₀ p ∈ closure ((extChartAt 𝓘(ℝ, E) p₀).target ∩ B) :=
      (isOpen_extChartAt_target p₀).inter_closure ⟨ht, h⟩
    have h2 := mem_closure_image (continuousAt_extChartAt_symm'' ht) h1
    rw [ch_left_inv p₀ hp] at h2
    refine closure_mono ?_ h2
    rintro _ ⟨u, ⟨hu, huB⟩, rfl⟩
    exact (hAB _ (ch_symm_mem p₀ hu)).2 (by rwa [ch_right_inv p₀ hu])

theorem ch_mem_frontier_iff {A : Set N} {B : Set E}
    (hAB : ∀ x ∈ (chartAt E p₀).source, x ∈ A ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ B) {p : N}
    (hp : p ∈ (chartAt E p₀).source) :
    p ∈ frontier A ↔ extChartAt 𝓘(ℝ, E) p₀ p ∈ frontier B := by
  rw [frontier_eq_closure_inter_closure, frontier_eq_closure_inter_closure, mem_inter_iff,
    mem_inter_iff, ch_mem_closure_iff hAB hp,
    ch_mem_closure_iff (A := Aᶜ) (B := Bᶜ) (fun x hx => not_congr (hAB x hx)) hp]

lemma ch_nhds_NV {p : N} (hp : p ∈ (chartAt E p₀).source) {U' : Set E}
    (hU' : U' ∈ 𝓝 (extChartAt 𝓘(ℝ, E) p₀ p)) :
    (chartAt E p₀).source ∩ extChartAt 𝓘(ℝ, E) p₀ ⁻¹' U' ∈ 𝓝 p :=
  inter_mem ((chartAt E p₀).open_source.mem_nhds hp) ((ch_contAt p₀ hp).preimage_mem_nhds hU')

lemma ch_nhds_VN {p : N} (hp : p ∈ (chartAt E p₀).source) {U : Set N} (hU : U ∈ 𝓝 p) :
    (extChartAt 𝓘(ℝ, E) p₀).target ∩ (extChartAt 𝓘(ℝ, E) p₀).symm ⁻¹' U ∈
      𝓝 (extChartAt 𝓘(ℝ, E) p₀ p) := by
  have ht := ch_mem_target p₀ hp
  refine inter_mem ((isOpen_extChartAt_target p₀).mem_nhds ht)
    ((continuousAt_extChartAt_symm'' ht).preimage_mem_nhds ?_)
  rwa [ch_left_inv p₀ hp]

theorem ch_mem_KLi_iff {A : ℝ → Set N} {B : ℝ → Set E}
    (hAB : ∀ τ, ∀ x ∈ (chartAt E p₀).source, x ∈ A τ ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ B τ) {p : N}
    (hp : p ∈ (chartAt E p₀).source) :
    p ∈ KLi A ↔ extChartAt 𝓘(ℝ, E) p₀ p ∈ KLi B := by
  constructor
  · intro h U' hU'
    filter_upwards [h _ (ch_nhds_NV hp hU')] with τ ⟨z, hzA, hzs, hzU⟩
    exact ⟨_, (hAB τ z hzs).1 hzA, hzU⟩
  · intro h U hU
    filter_upwards [h _ (ch_nhds_VN hp hU)] with τ ⟨w, hwB, hwt, hwU⟩
    exact ⟨_, (hAB τ _ (ch_symm_mem p₀ hwt)).2 (by rwa [ch_right_inv p₀ hwt]), hwU⟩

theorem ch_mem_KLs_iff {A : ℝ → Set N} {B : ℝ → Set E}
    (hAB : ∀ τ, ∀ x ∈ (chartAt E p₀).source, x ∈ A τ ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ B τ) {p : N}
    (hp : p ∈ (chartAt E p₀).source) :
    p ∈ KLs A ↔ extChartAt 𝓘(ℝ, E) p₀ p ∈ KLs B := by
  constructor
  · intro h U' hU'
    refine (h _ (ch_nhds_NV hp hU')).mono fun τ ⟨z, hzA, hzs, hzU⟩ => ?_
    exact ⟨_, (hAB τ z hzs).1 hzA, hzU⟩
  · intro h U hU
    refine (h _ (ch_nhds_VN hp hU)).mono fun τ ⟨w, hwB, hwt, hwU⟩ => ?_
    exact ⟨_, (hAB τ _ (ch_symm_mem p₀ hwt)).2 (by rwa [ch_right_inv p₀ hwt]), hwU⟩

namespace MSpacetime
variable {S : MSpacetime E N} (hC : S.OneChart p₀)
include hC

theorem ch_mem_H_iff {J : Set N} (hJ : J ⊆ (chartAt E p₀).source) {x : N}
    (hx : x ∈ (chartAt E p₀).source) :
    x ∈ S.H J ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ (chartSp hC).H (extChartAt 𝓘(ℝ, E) p₀ '' J) :=
  ch_mem_frontier_iff (fun _ hy => ch_mem_JpastSet_iff hC hJ hy) hx

/-! ### Temporal and Cauchy functions -/

/-- **Cauchy transport, `N → V` (BUILT).** A Cauchy temporal function on `D_N` gives, through
`φ⁻¹`, a Cauchy temporal function of the chart exterior `Dsp (φ J)`. -/
theorem ch_isCauchy_NV {J : Set N} (hJ : J ⊆ S.M) {Θ : N → ℝ}
    (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) :
    ((chartSp hC).Dsp (extChartAt 𝓘(ℝ, E) p₀ '' J)).IsCauchyTemporal
      (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) := by
  have hJs := hJ.trans hC.sub
  have hD : ∀ u ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J),
      u ∈ (extChartAt 𝓘(ℝ, E) p₀).target ∧ (extChartAt 𝓘(ℝ, E) p₀).symm u ∈ S.D J :=
    fun u hu => (ch_mem_chartD_iff hC hJs).1 hu
  have hDo := ch_isOpen_D hC J hJs
  have hΘd : ∀ u ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J),
      ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u := fun u hu =>
    (hΘ.1.1.contMDiffAt (hDo.mem_nhds (hD u hu).2)).comp u
      ((contMDiffOn_extChartAt_symm p₀).contMDiffAt
        ((isOpen_extChartAt_target p₀).mem_nhds (hD u hu).1))
  refine ⟨⟨fun u hu => (contMDiffAt_iff_contDiffAt.1 (hΘd u hu)).contDiffWithinAt,
    fun u hu w hw => ?_⟩, fun c a => ?_⟩
  · obtain ⟨hut, hxD⟩ := hD u hu
    have h1 := (hΘ.1.1.contMDiffAt (hDo.mem_nhds hxD)).mdifferentiableAt one_ne_zero
    have h2 := ld_mdifferentiableAt_symm p₀ hut
    have e : fderiv ℝ (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u w =
        dfun Θ ((extChartAt 𝓘(ℝ, E) p₀).symm u) (dchartInv p₀ u w) := by
      have e1 : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u w =
          fderiv ℝ (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u w := by rw [mfderiv_eq_fderiv]; rfl
      rw [← e1, mfderiv_comp u h1 h2]; rfl
    rw [e]
    exact hΘ.1.2 _ hxD _ ((futCausal_chart' hC hut w).1 hw)
  · have hDc := fun t => hD _ (c.mem t)
    let c' : S.InextCausalCurveIn (S.D J) :=
      { γ := fun t => (extChartAt 𝓘(ℝ, E) p₀).symm (c.γ t)
        cont := (continuousOn_extChartAt_symm p₀).comp_continuous c.cont fun t => (hDc t).1
        mem := fun t => (hDc t).2
        brk := c.brk
        brk_fin := c.brk_fin
        causal := fun t ht => by
          obtain ⟨hd, hcaus⟩ := c.causal t ht
          obtain ⟨hmd, hvel⟩ := ch_vel_symm p₀ hd (hDc t).1
          refine ⟨hmd, ?_⟩
          show S.FutCausal _ (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) _ t (1 : ℝ))
          rw [hvel]
          exact (futCausal_chart' hC (hDc t).1 _).1 hcaus
        inext_future := by
          rintro ⟨p, hp, hlim⟩
          apply c.inext_future
          have hps := hC.sub (S.D_subset_M J hp)
          refine ⟨_, (ch_mem_D_iff hC hJs hps).1 hp, ?_⟩
          refine ((ch_contAt p₀ hps).tendsto.comp hlim).congr fun t => ?_
          exact ch_right_inv p₀ (hDc t).1
        inext_past := by
          rintro ⟨p, hp, hlim⟩
          apply c.inext_past
          have hps := hC.sub (S.D_subset_M J hp)
          refine ⟨_, (ch_mem_D_iff hC hJs hps).1 hp, ?_⟩
          refine ((ch_contAt p₀ hps).tendsto.comp hlim).congr fun t => ?_
          exact ch_right_inv p₀ (hDc t).1 }
    exact hΘ.2 c' a

end MSpacetime

/-! ### The headline on `N` -/

namespace MSpacetime
variable {S : MSpacetime E N} (hC : S.OneChart p₀)
include hC

/-- `g` `C¹` in the chart gives `LocallyLipschitzOn` for the chart spacetime. -/
theorem ch_chart_lipschitz : LocallyLipschitzOn (chartSp hC).M (chartSp hC).g := by
  intro u hu
  obtain ⟨K, t, ht, hK⟩ :=
    ((hC.g_C1 u hu).contDiffAt ((chartSp hC).isOpen_M.mem_nhds hu)).exists_lipschitzOnWith
  exact ⟨K, t, nhdsWithin_le_nhds ht, hK⟩

/-- **Cauchy transport, `V → N` (BUILT)**, the converse of `ch_isCauchy_NV` (used by the witness):
a Cauchy temporal function of the chart exterior pulls back by `φ` to one on `D_N`. -/
theorem ch_isCauchy_VN {J : Set N} (hJ : J ⊆ S.M) {Θ' : E → ℝ}
    (hΘ : ((chartSp hC).Dsp (extChartAt 𝓘(ℝ, E) p₀ '' J)).IsCauchyTemporal Θ') :
    S.IsCauchyTemporalOn (S.D J) (Θ' ∘ extChartAt 𝓘(ℝ, E) p₀) := by
  have hJs := hJ.trans hC.sub
  have hDs : ∀ x ∈ S.D J, x ∈ (chartAt E p₀).source := fun x hx => hC.sub (S.D_subset_M J hx)
  have hD : ∀ x ∈ S.D J, extChartAt 𝓘(ℝ, E) p₀ x ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J) :=
    fun x hx => (ch_mem_D_iff hC hJs (hDs x hx)).1 hx
  have hDo : IsOpen ((chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J)) := (chartSp hC).hl_D_open _
  have hΘd : ∀ x ∈ S.D J, ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 Θ' (extChartAt 𝓘(ℝ, E) p₀ x) :=
    fun x hx => contMDiffAt_iff_contDiffAt.2 ((hΘ.1.1 _ (hD x hx)).contDiffAt
      (hDo.mem_nhds (hD x hx)))
  refine ⟨⟨fun x hx => ((hΘd x hx).comp x (contMDiffAt_extChartAt' (hDs x hx))).contMDiffWithinAt,
    fun x hx v hv => ?_⟩, fun c a => ?_⟩
  · have h1 := (hΘd x hx).mdifferentiableAt one_ne_zero
    have h2 : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x :=
      mdifferentiableAt_extChartAt (hDs x hx)
    have e : dfun (Θ' ∘ extChartAt 𝓘(ℝ, E) p₀) x v =
        fderiv ℝ Θ' (extChartAt 𝓘(ℝ, E) p₀ x) (dchart p₀ x v) := by
      have e1 : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) Θ' (extChartAt 𝓘(ℝ, E) p₀ x) =
          fderiv ℝ Θ' (extChartAt 𝓘(ℝ, E) p₀ x) := by rw [mfderiv_eq_fderiv]; rfl
      show mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (Θ' ∘ extChartAt 𝓘(ℝ, E) p₀) x v = _
      rw [mfderiv_comp x h1 h2, ← e1]; rfl
    rw [e]
    exact hΘ.1.2 _ (hD x hx) _ ((futCausal_chart hC (hDs x hx) v).2 hv)
  · have hcs := fun t => hDs _ (c.mem t)
    let c' : ((chartSp hC).Dsp (extChartAt 𝓘(ℝ, E) p₀ '' J)).InextCausalCurve :=
      { γ := fun t => extChartAt 𝓘(ℝ, E) p₀ (c.γ t)
        cont := continuous_iff_continuousAt.2 fun t => (ch_contAt p₀ (hcs t)).comp c.cont.continuousAt
        mem := fun t => hD _ (c.mem t)
        brk := c.brk
        brk_fin := c.brk_fin
        causal := fun t ht => by
          obtain ⟨hd, hcaus⟩ := c.causal t ht
          have h := ch_hasDerivAt_chart p₀ hd (hcs t)
          refine ⟨h.differentiableAt, ?_⟩
          rw [h.deriv]
          exact (futCausal_chart hC (hcs t) _).2 hcaus
        inext_future := by
          rintro ⟨u, hu, hlim⟩
          apply c.inext_future
          obtain ⟨hut, hx⟩ := (ch_mem_chartD_iff hC hJs).1 hu
          refine ⟨_, hx, ((continuousAt_extChartAt_symm'' hut).tendsto.comp hlim).congr fun t => ?_⟩
          exact ch_left_inv p₀ (hcs t)
        inext_past := by
          rintro ⟨u, hu, hlim⟩
          apply c.inext_past
          obtain ⟨hut, hx⟩ := (ch_mem_chartD_iff hC hJs).1 hu
          refine ⟨_, hx, ((continuousAt_extChartAt_symm'' hut).tendsto.comp hlim).congr fun t => ?_⟩
          exact ch_left_inv p₀ (hcs t) }
    exact hΘ.2 c' a

end MSpacetime

/-! ## Copied (campaign 85, `ManifoldExtension.lean`): the local one-chart hypothesis, the local past step,
the past extension and two-sided ⇒ future Cauchy on `N` -/

namespace MSpacetime
variable (S : MSpacetime E N)

/-- The same spacetime with `M` shrunk to an open `U ⊆ M` (same `g`, `T`). -/
def restrictM (U : Set N) (hU : IsOpen U) (hUM : U ⊆ S.M) : MSpacetime E N where
  M := U
  isOpen_M := hU
  g := S.g
  symm := S.symm
  T := S.T
  T_timelike := fun x hx => S.T_timelike x (hUM hx)
  pos_on_perp := fun x hx => S.pos_on_perp x (hUM hx)

lemma restrictM_tstep {U : Set N} {hU : IsOpen U} {hUM : U ⊆ S.M} {x y : N}
    (h : (S.restrictM U hU hUM).TStep x y) : S.TStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨hUM (ht t htI).1, (ht t htI).2⟩⟩

/-- **The local one-chart hypothesis** (chart-defined regularity, the local form of campaign 84's
`OneChart`): every `p ∈ M` has an open `U ∋ φ_p(p)`, `φ_p = extChartAt p` the preferred chart at
`p`, with `U ⊆ φ_p(M ∩ src_p)`, on which `hRep g p` is `C¹` and `chartRep T p` is continuous. -/
def LocallyOneChart : Prop :=
  ∀ p ∈ S.M, ∃ U : Set E, IsOpen U ∧ extChartAt 𝓘(ℝ, E) p p ∈ U ∧
    U ⊆ extChartAt 𝓘(ℝ, E) p '' (S.M ∩ (chartAt E p).source) ∧
    ContDiffOn ℝ 1 (hRep S.g p) U ∧ ContinuousOn (chartRep S.T p) U

variable {S}

/-- `LocallyOneChart` passes to an open `U ⊆ M`. -/
lemma LocallyOneChart.restrict (hL : S.LocallyOneChart) {U : Set N} (hU : IsOpen U)
    (hUM : U ⊆ S.M) : (S.restrictM U hU hUM).LocallyOneChart := by
  intro p hp
  obtain ⟨W, hW, hpW, hWsub, hg, hT⟩ := hL p (hUM hp)
  refine ⟨W ∩ ((extChartAt 𝓘(ℝ, E) p).target ∩ (extChartAt 𝓘(ℝ, E) p).symm ⁻¹' U),
    hW.inter ((continuousOn_extChartAt_symm p).isOpen_inter_preimage
      (isOpen_extChartAt_target p) hU),
    ⟨hpW, mem_extChartAt_target p, ?_⟩, ?_, hg.mono inter_subset_left, hT.mono inter_subset_left⟩
  · show (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p p) ∈ U
    rw [extChartAt_to_inv]; exact hp
  · rintro y ⟨hyW, -, hyU⟩
    obtain ⟨x, ⟨-, hxs⟩, rfl⟩ := hWsub hyW
    refine ⟨x, ⟨?_, hxs⟩, rfl⟩
    have h := ch_left_inv p hxs
    rw [mem_preimage, h] at hyU
    exact hyU

variable (S)

/-- **The local past step (BUILT), through `q`'s own chart.** For `q ∈ M` there is a map `f`,
continuous at `q`, with `f q ∈ M` and `TStep_N (f x) x` for all `x` near `q`:
`f x = φ_q⁻¹(φ_q x − ℓ T_V(φ_q x))`, `ℓ` a uniform safe length of the chart spacetime of the
restriction of `S` to `W = src_q ∩ φ_q⁻¹ U ∩ M` (tube lemma `safe_uniform`), transferred by
campaign 84's `ch_tstep_VN`. -/
theorem me_local_step (hL : S.LocallyOneChart) {q : N} (hq : q ∈ S.M) :
    ∃ f : N → N, ContinuousAt f q ∧ f q ∈ S.M ∧ ∀ᶠ x in 𝓝 q, S.TStep (f x) x := by
  obtain ⟨U, hU, hqU, -, hg, hT⟩ := hL q hq
  have hcs : ContinuousOn (extChartAt 𝓘(ℝ, E) q) (chartAt E q).source := by
    rw [← extChartAt_source (I := 𝓘(ℝ, E))]; exact continuousOn_extChartAt q
  set W : Set N := ((chartAt E q).source ∩ extChartAt 𝓘(ℝ, E) q ⁻¹' U) ∩ S.M with hWdef
  have hWo : IsOpen W :=
    (hcs.isOpen_inter_preimage (chartAt E q).open_source hU).inter S.isOpen_M
  have hWM : W ⊆ S.M := inter_subset_right
  have hWU : extChartAt 𝓘(ℝ, E) q '' W ⊆ U := by rintro _ ⟨x, hx, rfl⟩; exact hx.1.2
  have hC : (S.restrictM W hWo hWM).OneChart q :=
    { sub := fun x hx => hx.1.1
      g_C1 := hg.mono hWU
      T_cont := hT.mono hWU }
  set Sp := chartSp hC with hSp
  have hqW : q ∈ W := ⟨⟨mem_chart_source E q, hqU⟩, hq⟩
  have huM : extChartAt 𝓘(ℝ, E) q q ∈ Sp.M := ⟨q, hqW, rfl⟩
  obtain ⟨ℓ, hℓ, hsafe⟩ := Sp.safe_uniform huM
  have hmem : Sp.seg (extChartAt 𝓘(ℝ, E) q q) (-ℓ) ∈ Sp.M :=
    (hsafe.self_of_nhds (-ℓ) ⟨le_rfl, by linarith⟩).1
  obtain ⟨z, hzW, hze⟩ := hmem
  have htgt : Sp.seg (extChartAt 𝓘(ℝ, E) q q) (-ℓ) ∈ (extChartAt 𝓘(ℝ, E) q).target := by
    rw [← hze]; exact ch_mem_target q hzW.1.1
  have h1 : ContinuousAt (extChartAt 𝓘(ℝ, E) q) q := ch_contAt q (mem_chart_source E q)
  refine ⟨fun x => (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg (extChartAt 𝓘(ℝ, E) q x) (-ℓ)), ?_, ?_, ?_⟩
  · have h2 : ContinuousAt (fun x => Sp.seg (extChartAt 𝓘(ℝ, E) q x) (-ℓ)) q := by
      show ContinuousAt (fun x => extChartAt 𝓘(ℝ, E) q x + (-ℓ) • Sp.T (extChartAt 𝓘(ℝ, E) q x)) q
      exact h1.add (continuousAt_const.smul ((Sp.contAt_T huM).comp h1))
    exact ContinuousAt.comp (g := (extChartAt 𝓘(ℝ, E) q).symm)
      (f := fun x => Sp.seg (extChartAt 𝓘(ℝ, E) q x) (-ℓ))
      ((continuousOn_extChartAt_symm q).continuousAt
        ((isOpen_extChartAt_target q).mem_nhds htgt)) h2
  · show (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg (extChartAt 𝓘(ℝ, E) q q) (-ℓ)) ∈ S.M
    rw [← hze, ch_left_inv q hzW.1.1]; exact hzW.2
  · have hev : ∀ᶠ x in 𝓝 q, x ∈ (chartAt E q).source ∧ Sp.Safe (extChartAt 𝓘(ℝ, E) q x) ℓ :=
      Filter.Eventually.and ((chartAt E q).open_source.mem_nhds (mem_chart_source E q))
        (h1.tendsto.eventually hsafe)
    filter_upwards [hev] with x hx
    have hst := Sp.seg_tstep hx.2 le_rfl (by linarith : -ℓ < 0) le_rfl
    rw [Spacetime.seg_zero] at hst
    have h := ch_tstep_VN hC hst
    rw [ch_left_inv q hx.1] at h
    exact S.restrictM_tstep h

/-! ### A temporal `Θ` along manifold curves -/

lemma me_temporal_hasDerivAt {Θ : N → ℝ} {U : Set N} (hU : IsOpen U)
    (hΘ : ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 Θ U) {γ : ℝ → N} {t : ℝ}
    (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t) (ht : γ t ∈ U) :
    HasDerivAt (fun s => Θ (γ s)) (dfun (E := E) Θ (γ t) (vel (E := E) γ t)) t := by
  have hΘd : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) Θ (γ t) :=
    (hΘ.contMDiffAt (hU.mem_nhds ht)).mdifferentiableAt one_ne_zero
  have hc := hΘd.comp t hγ
  have hd : DifferentiableAt ℝ (Θ ∘ γ) t := mdifferentiableAt_iff_differentiableAt.1 hc
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (Θ ∘ γ) t (1 : ℝ) = deriv (Θ ∘ γ) t := by
    rw [mfderiv_eq_fderiv]; rfl
  have e3 : deriv (Θ ∘ γ) t = dfun (E := E) Θ (γ t) (vel (E := E) γ t) := by
    rw [← e2, mfderiv_comp t hΘd hγ]; rfl
  rw [← e3]; exact hd.hasDerivAt

/-- A temporal `Θ` strictly increases along a manifold timelike piece on `[0,1]`. -/
lemma me_temporal_strictMonoOn {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {γ : ℝ → N}
    (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (vel γ t)) :
    StrictMonoOn (fun s => Θ (γ s)) (Icc 0 1) := by
  have hcont : ContinuousOn (fun s => Θ (γ s)) (Icc (0:ℝ) 1) :=
    hΘ.1.continuousOn.comp hγ.continuous.continuousOn fun t h => (ht t h).1
  refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hcont fun t htI => ?_
  rw [interior_Icc] at htI
  obtain ⟨hm, h1, h2⟩ := ht t (Ioo_subset_Icc_self htI)
  rw [(me_temporal_hasDerivAt S.isOpen_M hΘ.1 (hγ.mdifferentiableAt one_ne_zero) hm).deriv]
  exact hΘ.2 _ hm _ ⟨h1.le, h2⟩

lemma me_temporal_tstep {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x y : N} (h : S.TStep x y) :
    Θ x < Θ y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  have := S.me_temporal_strictMonoOn hΘ hγ ht ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩
    zero_lt_one
  simpa [h0, h1] using this

lemma me_contAt {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x : N} (hx : x ∈ S.M) :
    ContinuousAt Θ x :=
  hΘ.1.continuousOn.continuousAt (S.isOpen_M.mem_nhds hx)

/-! ### The drop `δ`, the vertices, and no past limit -/

/-- **The step size** `δ(x) = sup {min(1, Θ x − Θ y) : TStep_N y x}` (no metric; the `min` is
inside the `sup` so that the set is bounded above). -/
noncomputable def pastDrop (Θ : N → ℝ) (x : N) : ℝ :=
  sSup ((fun y => min 1 (Θ x - Θ y)) '' {y | S.TStep y x})

lemma pastDrop_bdd (Θ : N → ℝ) (x : N) :
    BddAbove ((fun y => min 1 (Θ x - Θ y)) '' {y | S.TStep y x}) :=
  ⟨1, by rintro _ ⟨y, -, rfl⟩; exact min_le_left _ _⟩

lemma le_pastDrop {Θ : N → ℝ} {x y : N} (h : S.TStep y x) :
    min 1 (Θ x - Θ y) ≤ S.pastDrop Θ x :=
  le_csSup (S.pastDrop_bdd Θ x) ⟨y, h, rfl⟩

open Classical in
/-- The next vertex: a `y` with `TStep_N y x` and drop `Θ x − Θ y > δ(x)/2`. -/
noncomputable def nextV (Θ : N → ℝ) (x : N) : N :=
  if h : ∃ y, S.TStep y x ∧ S.pastDrop Θ x / 2 < Θ x - Θ y then h.choose else x

lemma nextV_spec (hL : S.LocallyOneChart) {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x : N}
    (hx : x ∈ S.M) :
    S.TStep (S.nextV Θ x) x ∧ S.pastDrop Θ x / 2 < Θ x - Θ (S.nextV Θ x) := by
  obtain ⟨f, -, -, hf⟩ := S.me_local_step hL hx
  have hy := hf.self_of_nhds
  have hpos : 0 < min 1 (Θ x - Θ (f x)) :=
    lt_min one_pos (sub_pos.2 (S.me_temporal_tstep hΘ hy))
  have hδ : 0 < S.pastDrop Θ x := hpos.trans_le (S.le_pastDrop hy)
  have hex : ∃ y, S.TStep y x ∧ S.pastDrop Θ x / 2 < Θ x - Θ y := by
    have hne : ((fun y => min 1 (Θ x - Θ y)) '' {y | S.TStep y x}).Nonempty :=
      ⟨_, ⟨f x, hy, rfl⟩⟩
    obtain ⟨_, ⟨y, hy, rfl⟩, hlt⟩ := exists_lt_of_lt_csSup hne (half_lt_self hδ)
    exact ⟨y, hy, hlt.trans_le (min_le_right _ _)⟩
  have e : S.nextV Θ x = hex.choose := by
    unfold nextV; split_ifs with h
    · rfl
    · exact absurd hex h
  rw [e]; exact hex.choose_spec

/-- The vertices `X 0 = x`, `X (k+1) = nextV (X k)`. -/
noncomputable def mvert (Θ : N → ℝ) (x : N) : ℕ → N
  | 0 => x
  | k + 1 => S.nextV Θ (mvert Θ x k)

variable {S}
variable (hL : S.LocallyOneChart) {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x : N} (hx : x ∈ S.M)
include hL hΘ hx

lemma mvert_mem : ∀ k, S.mvert Θ x k ∈ S.M
  | 0 => hx
  | k + 1 => (S.tstep_mem (S.nextV_spec hL hΘ (mvert_mem k)).1).1

lemma mvert_step (k : ℕ) : S.TStep (S.mvert Θ x (k + 1)) (S.mvert Θ x k) ∧
    S.pastDrop Θ (S.mvert Θ x k) / 2 < Θ (S.mvert Θ x k) - Θ (S.mvert Θ x (k + 1)) :=
  S.nextV_spec hL hΘ (mvert_mem hL hΘ hx k)

lemma mvert_le : ∀ k, Θ (S.mvert Θ x k) ≤ Θ x
  | 0 => le_rfl
  | k + 1 => (S.me_temporal_tstep hΘ (mvert_step hL hΘ hx k).1).le.trans (mvert_le k)

/-- **No past limit of the vertices (BUILT).** If `X k → q ∈ M`, the local step at `q` (in `q`'s
own chart) gives `δ ≥ min(1, d/2)` near `q`, `d = Θ q − Θ (f q) > 0`, so the drops
`Θ (X k) − Θ (X (k+1))` stay above `min(1, d/2)/2`, contradicting `Θ (X k) → Θ q`. -/
theorem mvert_no_limit : ¬ ∃ q ∈ S.M, Tendsto (S.mvert Θ x) atTop (𝓝 q) := by
  rintro ⟨q, hq, hlim⟩
  obtain ⟨f, hfc, hfq, hf⟩ := S.me_local_step hL hq
  set d := Θ q - Θ (f q) with hd_def
  have hd : 0 < d := sub_pos.2 (S.me_temporal_tstep hΘ hf.self_of_nhds)
  have hgc : ContinuousAt (fun z => Θ z - Θ (f z)) q :=
    (S.me_contAt hΘ hq).sub ((S.me_contAt hΘ hfq).comp hfc)
  have hev : ∀ᶠ z in 𝓝 q, S.TStep (f z) z ∧ d / 2 < Θ z - Θ (f z) :=
    hf.and (hgc.eventually (lt_mem_nhds (half_lt_self hd)))
  have hc : 0 < min 1 (d / 2) / 2 := half_pos (lt_min one_pos (half_pos hd))
  have hev2 : ∀ᶠ k in atTop, min 1 (d / 2) / 2 < Θ (S.mvert Θ x k) - Θ (S.mvert Θ x (k + 1)) :=
    (hlim.eventually hev).mono fun k hk => by
      have h3 := S.le_pastDrop (Θ := Θ) hk.1
      have h4 : min 1 (d / 2) ≤ min 1 (Θ (S.mvert Θ x k) - Θ (f (S.mvert Θ x k))) :=
        min_le_min le_rfl hk.2.le
      have h5 := (mvert_step hL hΘ hx k).2
      linarith
  have hlim2 : Tendsto (fun k => Θ (S.mvert Θ x k) - Θ (S.mvert Θ x (k + 1))) atTop (𝓝 0) := by
    have h := (S.me_contAt hΘ hq).tendsto.comp hlim
    have h' := h.sub (h.comp (tendsto_add_atTop_nat 1))
    rw [sub_self] at h'
    exact h'
  obtain ⟨k, hk1, hk2⟩ := (hev2.and (hlim2.eventually (gt_mem_nhds hc))).exists
  linarith

/-- **The reachable-negative form (BUILT): the extension as a sequence.** -/
theorem me_past_sequence : ∃ X : ℕ → N, X 0 = x ∧ (∀ k, S.TStep (X (k + 1)) (X k)) ∧
    (∀ k, Θ (X k) ≤ Θ x) ∧ ¬ ∃ q ∈ S.M, Tendsto X atTop (𝓝 q) :=
  ⟨S.mvert Θ x, rfl, fun k => (mvert_step hL hΘ hx k).1, mvert_le hL hΘ hx,
    mvert_no_limit hL hΘ hx⟩

omit hL hΘ hx

end MSpacetime

/-! ### Gluing the steps into one curve (the registered expected stop) -/

section Glue
variable {X : Type*} [TopologicalSpace X]

/-- Piece `k` as a function of `u = -t`: `γ k (k + 1 − u)`, so `u ∈ [k, k+1]` runs `γ k` over
`[0,1]` backwards in `u`, i.e. forwards in `t`. -/
noncomputable def gpiece (γ : ℕ → ℝ → X) (k : ℕ) (u : ℝ) : X := γ k (k + 1 - u)

/-- The glued curve as a function of `u = -t` (`Nat.floor` makes it piece `0` for `u < 0`). -/
noncomputable def gpoly (γ : ℕ → ℝ → X) (u : ℝ) : X := gpiece γ ⌊u⌋₊ u

variable {γ : ℕ → ℝ → X} (hj : ∀ k, γ (k + 1) 1 = γ k 0)
include hj

lemma gpoly_eq (k : ℕ) {u : ℝ} (h1 : (k:ℝ) ≤ u ∨ k = 0) (h2 : u ≤ k + 1) :
    gpoly γ u = gpiece γ k u := by
  rcases h2.lt_or_eq with h2 | h2
  · have hk : ⌊u⌋₊ = k := by
      by_cases hu : 0 ≤ u
      · rw [Nat.floor_eq_iff hu]
        rcases h1 with h1 | h1
        · exact ⟨h1, h2⟩
        · subst h1; exact ⟨by simpa using hu, h2⟩
      · rw [Nat.floor_eq_zero.2 (by linarith)]
        rcases h1 with h1 | h1
        · exact absurd (le_trans (Nat.cast_nonneg k) h1) hu
        · exact h1.symm
    rw [gpoly, hk]
  · have hk : ⌊u⌋₊ = k + 1 := by rw [h2]; exact_mod_cast Nat.floor_natCast (k + 1)
    rw [gpoly, hk, gpiece, gpiece, h2]
    have e1 : ((k + 1 : ℕ) : ℝ) + 1 - ((k:ℝ) + 1) = 1 := by push_cast; ring
    have e2 : (k : ℝ) + 1 - ((k:ℝ) + 1) = 0 := by ring
    rw [e1, e2, hj]

lemma gpoly_continuous (hc : ∀ k, Continuous (γ k)) : Continuous (gpoly γ) := by
  have hpc : ∀ k, Continuous (gpiece γ k) := fun k =>
    (hc k).comp (continuous_const.sub continuous_id)
  rw [continuous_iff_continuousAt]
  intro u
  by_cases hu1 : u < 1
  · refine (hpc 0).continuousAt.congr ?_
    filter_upwards [Iio_mem_nhds hu1] with v hv
    exact (gpoly_eq hj 0 (Or.inr rfl) (by simpa using hv.le)).symm
  set n := ⌊u⌋₊ with hn
  have hnu : (n:ℝ) ≤ u := Nat.floor_le (by linarith)
  have hun : u < n + 1 := Nat.lt_floor_add_one u
  by_cases hne : (n:ℝ) < u
  · refine (hpc n).continuousAt.congr ?_
    filter_upwards [Ioo_mem_nhds hne hun] with v hv
    exact (gpoly_eq hj n (Or.inl hv.1.le) hv.2.le).symm
  have hequ : u = n := le_antisymm (not_lt.1 hne) hnu
  have hn1 : 1 ≤ n := by
    by_contra h
    have : n = 0 := by omega
    rw [this] at hequ; norm_num at hequ; linarith
  obtain ⟨k, hk⟩ : ∃ k, n = k + 1 := ⟨n - 1, by omega⟩
  rw [hk] at hequ
  push_cast at hequ
  have hA : ContinuousWithinAt (gpoly γ) (Icc (k:ℝ) (k + 1)) u :=
    (hpc k).continuousWithinAt.congr
      (fun v hv => gpoly_eq hj k (Or.inl hv.1) hv.2) (gpoly_eq hj k (Or.inl (by linarith)) hequ.le)
  have hB : ContinuousWithinAt (gpoly γ) (Icc ((k:ℝ) + 1) (k + 1 + 1)) u :=
    (hpc (k + 1)).continuousWithinAt.congr
      (fun v hv => gpoly_eq hj (k + 1) (Or.inl (by push_cast; exact hv.1))
        (by push_cast; exact hv.2))
      (gpoly_eq hj (k + 1) (Or.inl (by push_cast; linarith)) (by push_cast; linarith))
  refine (hA.union hB).continuousAt (mem_of_superset (Ioo_mem_nhds (a := (k:ℝ))
    (b := k + 1 + 1) (by linarith) (by linarith)) fun v hv => ?_)
  rcases le_total v (k + 1) with h | h
  · exact Or.inl ⟨hv.1.le, h⟩
  · exact Or.inr ⟨h, hv.2.le⟩

end Glue

namespace MSpacetime

/-- Velocities agree for curves agreeing near `t`. -/
lemma vel_congr {γ₁ γ₂ : ℝ → N} {t : ℝ} (h : γ₁ =ᶠ[𝓝 t] γ₂) :
    vel (E := E) γ₁ t = vel (E := E) γ₂ t := by
  unfold vel; rw [h.mfderiv_eq]; rfl

/-- The velocity of a translate `s ↦ γ (c + s)`. -/
lemma vel_comp_add {γ : ℝ → N} {c t : ℝ} (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (c + t)) :
    vel (E := E) (fun s => γ (c + s)) t = vel (E := E) γ (c + t) := by
  have hτ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => c + s) t :=
    mdifferentiableAt_iff_differentiableAt.2 (differentiableAt_id.const_add c)
  have e : (fun s => γ (c + s)) = γ ∘ (fun s => c + s) := rfl
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => c + s) t (1 : ℝ) = 1 := by
    rw [mfderiv_eq_fderiv]
    show fderiv ℝ (fun s : ℝ => c + s) t 1 = 1
    rw [((hasDerivAt_id' t).const_add c).hasFDerivAt.fderiv]; simp
  unfold vel; rw [e, mfderiv_comp t hγ hτ]
  change mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (c + t)
    (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => c + s) t (1 : ℝ)) = _
  rw [e2]; rfl

variable {S : MSpacetime E N}
variable (hL : S.LocallyOneChart) {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x : N} (hx : x ∈ S.M)
include hL hΘ hx

/-- **The past extension on `N` (BUILT, gluing included).** For `Θ` temporal on `M` and
`LocallyOneChart`, every `x ∈ M` is the endpoint of a continuous `p : ℝ → N`, `p 0 = x`, inside `M`
on `t ≤ 0` with `Θ (p t) < Θ x` for `t < 0`, `ContMDiff` with future-timelike `mfderiv` velocity off
the integers on `t < 0`, and with no past limit in `M`. Piece `k` is the `k`-th `TStep_N` of
`me_past_sequence`, traversed on `[−k−1, −k]`. -/
theorem me_past_extension :
    ∃ p : ℝ → N, Continuous p ∧ p 0 = x ∧ (∀ t ≤ 0, p t ∈ S.M) ∧ (∀ t < 0, Θ (p t) < Θ x) ∧
      (∀ t < 0, t ∉ range (Int.cast : ℤ → ℝ) →
        ContMDiffAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 p t ∧ S.FutTimelike (p t) (vel p t)) ∧
      ¬ ∃ q ∈ S.M, Tendsto p atBot (𝓝 q) := by
  have hstep : ∀ k, S.TStep (S.mvert Θ x (k + 1)) (S.mvert Θ x k) := fun k =>
    (mvert_step hL hΘ hx k).1
  choose γ hγ h0 h1 hγt using hstep
  have hj : ∀ k, γ (k + 1) 1 = γ k 0 := fun k => by rw [h1, h0]
  have hpk : ∀ k : ℕ, gpoly γ (k : ℝ) = S.mvert Θ x k := fun k => by
    rw [gpoly_eq hj k (Or.inl le_rfl) (by linarith), gpiece,
      show (k : ℝ) + 1 - k = 1 by ring, h1]
  refine ⟨fun t => gpoly γ (-t),
    (gpoly_continuous hj fun k => (hγ k).continuous).comp continuous_neg, ?_, ?_, ?_, ?_, ?_⟩
  · show gpoly γ (-0) = x
    rw [neg_zero]; exact_mod_cast hpk 0
  · intro t ht
    set u := -t
    have hu : 0 ≤ u := by simp [u]; linarith
    set k := ⌊u⌋₊
    have hk1 : (k:ℝ) ≤ u := Nat.floor_le hu
    have hk2 : u < k + 1 := Nat.lt_floor_add_one u
    show gpoly γ u ∈ S.M
    rw [gpoly_eq hj k (Or.inl hk1) hk2.le, gpiece]
    exact (hγt k _ ⟨by linarith, by linarith⟩).1
  · intro t ht
    set u := -t
    have hu : 0 < u := by simp [u]; linarith
    set k := ⌈u⌉₊ - 1
    have hc1 : 1 ≤ ⌈u⌉₊ := Nat.one_le_iff_ne_zero.2 (by positivity)
    have hk : (k:ℝ) + 1 = ⌈u⌉₊ := by simp only [k]; push_cast [Nat.cast_sub hc1]; ring
    have hk1 : (k:ℝ) < u := by linarith [Nat.ceil_lt_add_one hu.le]
    have hk2 : u ≤ k + 1 := hk ▸ Nat.le_ceil u
    show Θ (gpoly γ u) < Θ x
    rw [gpoly_eq hj k (Or.inl hk1.le) hk2, gpiece]
    have hmono := S.me_temporal_strictMonoOn hΘ (hγ k) (hγt k)
    have hlt : Θ (γ k (k + 1 - u)) < Θ (γ k 1) :=
      hmono ⟨by linarith, by linarith⟩ ⟨zero_le_one, le_rfl⟩ (by linarith)
    rw [h1] at hlt
    exact hlt.trans_le (mvert_le hL hΘ hx k)
  · intro t ht hbrk
    set u := -t with hu_def
    have hu : 0 < u := by simp [u]; linarith
    set n := ⌊u⌋₊
    have hnu : (n:ℝ) ≤ u := Nat.floor_le hu.le
    have hun : u < n + 1 := Nat.lt_floor_add_one u
    have hne : (n:ℝ) < u := by
      refine lt_of_le_of_ne hnu fun h => hbrk ⟨-(n:ℤ), ?_⟩
      push_cast; rw [h, hu_def, neg_neg]
    have hev : (fun t => gpoly γ (-t)) =ᶠ[𝓝 t] fun s => γ n (((n:ℝ) + 1) + s) := by
      filter_upwards [(continuous_neg.tendsto t).eventually (Ioo_mem_nhds hne hun)] with s hs
      rw [gpoly_eq hj n (Or.inl hs.1.le) hs.2.le, gpiece, sub_neg_eq_add]
    have hsI : ((n:ℝ) + 1) + t ∈ Icc (0:ℝ) 1 := ⟨by linarith, by linarith⟩
    have hτ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) 1 (fun s : ℝ => ((n:ℝ) + 1) + s) :=
      contMDiff_iff_contDiff.2 (contDiff_const.add contDiff_id)
    have hcm : ContMDiffAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 (fun s => γ n (((n:ℝ) + 1) + s)) t :=
      ContMDiffAt.comp (g := γ n) (f := fun s : ℝ => ((n:ℝ) + 1) + s) t
        ((hγ n).contMDiffAt) (hτ.contMDiffAt)
    refine ⟨hcm.congr_of_eventuallyEq hev, ?_⟩
    have he : gpoly γ (-t) = γ n (((n:ℝ) + 1) + t) := hev.eq_of_nhds
    show S.FutTimelike (gpoly γ (-t)) (vel (fun t => gpoly γ (-t)) t)
    rw [vel_congr hev, vel_comp_add ((hγ n).mdifferentiableAt one_ne_zero), he]
    exact (hγt n _ hsI).2
  · rintro ⟨q, hq, hlim⟩
    refine mvert_no_limit hL hΘ hx ⟨q, hq, ?_⟩
    have h := hlim.comp (tendsto_neg_atTop_atBot.comp tendsto_natCast_atTop_atTop)
    refine h.congr fun k => ?_
    show gpoly γ (-(-(k:ℝ))) = S.mvert Θ x k
    rw [neg_neg, hpk]

omit hL hΘ hx

/-! ### Two-sided Cauchy ⇒ future Cauchy on `N` -/

variable (S) in
/-- A future-directed piecewise-`C¹` causal curve on `[0, ∞)`, future-inextendible in `U`
(the `N`-analogue of campaign 78's `FutInextCurve`, intrinsic). -/
structure FutInextCurveIn (U : Set N) where
  γ : ℝ → N
  cont : ContinuousOn γ (Ici 0)
  mem : ∀ t, 0 ≤ t → γ t ∈ U
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t, 0 < t → t ∉ brk →
    MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t ∧ S.FutCausal (γ t) (vel γ t)
  inext_future : ¬ ∃ p ∈ U, Tendsto γ atTop (𝓝 p)

variable (S) in
/-- **Cauchy temporal on `U`, future form** (intrinsic): `Θ` temporal on `U`, and every
future-inextendible causal curve in `U` from `γ 0` attains every level `a ≥ Θ (γ 0)`. -/
def FutCauchyTemporalOn (U : Set N) (Θ : N → ℝ) : Prop :=
  S.IsTemporalOn U Θ ∧
    ∀ c : S.FutInextCurveIn U, ∀ a : ℝ, Θ (c.γ 0) ≤ a → ∃ t, 0 ≤ t ∧ Θ (c.γ t) = a

/-- **Two-sided ⇒ future Cauchy on `N` (BUILT).** For `LocallyOneChart S` and an open `U ⊆ M`
(e.g. `U = D J` once `D J` is known to be open): campaign 84's two-sided `IsCauchyTemporalOn U Θ`
implies the future form. A future-inextendible `c` is glued at `0` to the past extension
`me_past_extension` of `c.γ 0` in the restriction of `S` to `U`; the glued curve is an
`InextCausalCurveIn U`, so it meets level `a` once, and since `Θ (p t) < Θ (c.γ 0) ≤ a` for `t < 0`
the hit is at `t ≥ 0`. -/
theorem me_futCauchy_of_cauchy_N (hL : S.LocallyOneChart) {U : Set N} (hU : IsOpen U)
    (hUM : U ⊆ S.M) {Θ : N → ℝ} (hΘ : S.IsCauchyTemporalOn U Θ) : S.FutCauchyTemporalOn U Θ := by
  refine ⟨hΘ.1, fun c a ha => ?_⟩
  have hL' := hL.restrict hU hUM
  have hΘ' : (S.restrictM U hU hUM).IsTemporalOn (S.restrictM U hU hUM).M Θ := hΘ.1
  obtain ⟨p, hpc, hp0, hpM, hpΘ, hpd, hpinext⟩ :=
    me_past_extension hL' hΘ' (x := c.γ 0) (c.mem 0 le_rfl)
  set γ : ℝ → N := fun t => if t ≤ 0 then p t else c.γ t with hγ
  have hγc : Continuous γ :=
    continuous_if_le (f := fun t : ℝ => t) (g := fun _ => (0:ℝ)) continuous_id continuous_const
      hpc.continuousOn c.cont fun t (ht : t = 0) => by rw [ht, hp0]
  have hγneg : ∀ t ≤ 0, γ t = p t := fun t ht => by simp [hγ, ht]
  have hγpos : ∀ t, 0 < t → γ t = c.γ t := fun t ht => by simp [hγ, not_le.2 ht]
  have hγ0 : ∀ t, 0 ≤ t → γ t = c.γ t := by
    intro t ht
    rcases ht.lt_or_eq with h | h
    · exact hγpos t h
    · rw [← h, hγneg 0 le_rfl, hp0]
  let C : S.InextCausalCurveIn U :=
    { γ := γ
      cont := hγc
      mem := fun t => by
        rcases le_or_gt t 0 with h | h
        · rw [hγneg t h]; exact hpM t h
        · rw [hγpos t h]; exact c.mem t h.le
      brk := c.brk ∪ range (Int.cast : ℤ → ℝ)
      brk_fin := fun a b => by
        rw [union_inter_distrib_right]
        exact (c.brk_fin a b).union (Spacetime.int_brk_fin a b)
      causal := fun t ht => by
        have ht0 : t ≠ 0 := fun h => ht (Or.inr ⟨0, by simp [h]⟩)
        rcases lt_or_gt_of_ne ht0 with h | h
        · have hev : γ =ᶠ[𝓝 t] p := by
            filter_upwards [Iio_mem_nhds h] with s hs using hγneg s hs.le
          obtain ⟨hd, hft⟩ := hpd t h fun hb => ht (Or.inr hb)
          refine ⟨(hd.mdifferentiableAt one_ne_zero).congr_of_eventuallyEq hev, ?_⟩
          rw [vel_congr hev, hγneg t h.le]; exact ⟨hft.1.le, hft.2⟩
        · have hev : γ =ᶠ[𝓝 t] c.γ := by
            filter_upwards [Ioi_mem_nhds h] with s hs using hγpos s hs
          obtain ⟨hd, hft⟩ := c.causal t h fun hb => ht (Or.inl hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [vel_congr hev, hγpos t h]; exact hft
      inext_future := by
        rintro ⟨q, hq, hlim⟩
        refine c.inext_future ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_gt_atTop 0] with s hs using hγpos s hs
      inext_past := by
        rintro ⟨q, hq, hlim⟩
        refine hpinext ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_le_atBot 0] with s hs using hγneg s hs }
  obtain ⟨t, ht, -⟩ := hΘ.2 C a
  change Θ (γ t) = a at ht
  rcases lt_or_ge t 0 with h | h
  · rw [hγneg t h.le] at ht
    have := hpΘ t h
    linarith
  · exact ⟨t, h, by rw [← hγ0 t h]; exact ht⟩

end MSpacetime


/-! ## Copied (campaign 86, `ManifoldLocalKit.lean`): the local kit on `N` -/

/-! ### Piece 1: restriction and reparametrisation -/

/-- The velocity of an affine reparametrisation `s ↦ γ (a + b s)` is `b • γ'(a + b t)`. -/
lemma mk_vel_affine {γ : ℝ → N} {a b t : ℝ}
    (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (a + b * t)) :
    MSpacetime.vel (E := E) (fun s => γ (a + b * s)) t = b • MSpacetime.vel (E := E) γ (a + b * t) := by
  have hτd : HasDerivAt (fun s : ℝ => a + b * s) b t := by
    simpa using ((hasDerivAt_id t).const_mul b).const_add a
  have hτ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => a + b * s) t :=
    mdifferentiableAt_iff_differentiableAt.2 hτd.differentiableAt
  have e : (fun s => γ (a + b * s)) = γ ∘ (fun s => a + b * s) := rfl
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => a + b * s) t (1 : ℝ) = b • (1 : ℝ) := by
    rw [mfderiv_eq_fderiv]
    show fderiv ℝ (fun s : ℝ => a + b * s) t 1 = b • (1 : ℝ)
    rw [hτd.hasFDerivAt.fderiv]; simp
  unfold MSpacetime.vel; rw [e, mfderiv_comp t hγ hτ]
  change mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (a + b * t)
    (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => a + b * s) t (1 : ℝ)) = _
  rw [e2]
  exact (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (a + b * t)).map_smul b (1 : ℝ)

/-- **Restriction (generic).** A `C¹` curve with a cone-type property `P` (closed under positive
rescaling) on `[a,b]`, inside `W`, reparametrised as `s ↦ γ (a + (b − a) s)`, is a curve with
property `P` on `[0,1]`, inside `W`, from `γ a` to `γ b`. -/
lemma mk_restrict_curve {P : N → E → Prop} (hP : ∀ x v (c : ℝ), 0 < c → P x v → P x (c • v))
    {W : Set N} {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ) {a b : ℝ} (hab : a < b)
    (ht : ∀ t ∈ Icc a b, γ t ∈ W ∧ P (γ t) (MSpacetime.vel γ t)) :
    ∃ γ' : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ' ∧ γ' 0 = γ a ∧ γ' 1 = γ b ∧
      ∀ t ∈ Icc (0:ℝ) 1, γ' t ∈ W ∧ P (γ' t) (MSpacetime.vel γ' t) := by
  have hτ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) 1 (fun s : ℝ => a + (b - a) * s) :=
    contMDiff_iff_contDiff.2 (contDiff_const.add (contDiff_const.mul contDiff_id))
  refine ⟨fun s => γ (a + (b - a) * s), hγ.comp hτ, by simp, by simp, fun t htI => ?_⟩
  have hba : 0 < b - a := sub_pos.2 hab
  have hm : a + (b - a) * t ∈ Icc a b :=
    ⟨by nlinarith [htI.1], by nlinarith [htI.2]⟩
  obtain ⟨hW, hPt⟩ := ht _ hm
  refine ⟨hW, ?_⟩
  rw [mk_vel_affine ((hγ _).mdifferentiableAt one_ne_zero)]
  exact hP _ _ _ hba hPt

/-- A point of `[0,1]` has a neighbourhood mapped into an open `W ∋ γ s`. -/
lemma mk_near {X : Type*} [TopologicalSpace X] {γ : ℝ → X} (hγ : Continuous γ) {W : Set X}
    (hW : IsOpen W) {s : ℝ} (hs : γ s ∈ W) : ∃ δ > 0, ∀ t, |t - s| < δ → γ t ∈ W := by
  obtain ⟨δ, hδ, h⟩ := Metric.isOpen_iff.1 (hW.preimage hγ) s hs
  exact ⟨δ, hδ, fun t ht => h (by rwa [mem_ball, Real.dist_eq])⟩

namespace MSpacetime
variable (S : MSpacetime E N)

lemma restrictM_cstep {U : Set N} {hU : IsOpen U} {hUM : U ⊆ S.M} {x y : N}
    (h : (S.restrictM U hU hUM).CStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨hUM (ht t htI).1, (ht t htI).2⟩⟩

lemma restrictM_chr {U : Set N} {hU : IsOpen U} {hUM : U ⊆ S.M} {x y : N}
    (h : (S.restrictM U hU hUM).Chr x y) : S.Chr x y := by
  induction h with
  | single h => exact Relation.TransGen.single (S.restrictM_tstep h)
  | tail _ h ih => exact ih.tail (S.restrictM_tstep h)

variable {S}

/-- **Piece 1, `TStep` (BUILT).** A sub-arc `[a,b] ⊆ [0,1]` (`a < b`) of a timelike step's
curve, reparametrised onto `[0,1]`, is a `TStep_N (γ a) (γ b)`. -/
theorem mk_tstep_sub {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (vel γ t)) {a b : ℝ}
    (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) : S.TStep (γ a) (γ b) :=
  mk_restrict_curve (P := S.FutTimelike) (W := S.M) (fun _ _ _ hc h => S.futTimelike_smul hc h) hγ hab
    fun t h => ht t ⟨ha.trans h.1, h.2.trans hb⟩

/-- **Piece 1, `CStep` (BUILT).** -/
theorem mk_cstep_sub {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (vel γ t)) {a b : ℝ}
    (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) : S.CStep (γ a) (γ b) :=
  mk_restrict_curve (P := S.FutCausal) (W := S.M) (fun _ _ _ hc h => S.futCausal_smul hc h) hγ hab
    fun t h => ht t ⟨ha.trans h.1, h.2.trans hb⟩

/-- Piece 1 inside a patch `W`: the sub-arc is a step of `S.restrictM W`. -/
theorem mk_tstep_sub_in {W : Set N} (hW : IsOpen W) (hWM : W ⊆ S.M) {γ : ℝ → N}
    (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (vel γ t)) {a b : ℝ}
    (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) (hγW : ∀ t ∈ Icc a b, γ t ∈ W) :
    (S.restrictM W hW hWM).TStep (γ a) (γ b) :=
  mk_restrict_curve (P := (S.restrictM W hW hWM).FutTimelike) (W := W) (fun _ _ _ hc h => (S.restrictM W hW hWM).futTimelike_smul hc h) hγ hab
    fun t h => ⟨hγW t h, (ht t ⟨ha.trans h.1, h.2.trans hb⟩).2⟩

theorem mk_cstep_sub_in {W : Set N} (hW : IsOpen W) (hWM : W ⊆ S.M) {γ : ℝ → N}
    (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (vel γ t)) {a b : ℝ}
    (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) (hγW : ∀ t ∈ Icc a b, γ t ∈ W) :
    (S.restrictM W hW hWM).CStep (γ a) (γ b) :=
  mk_restrict_curve (P := (S.restrictM W hW hWM).FutCausal) (W := W) (fun _ _ _ hc h => (S.restrictM W hW hWM).futCausal_smul hc h) hγ hab
    fun t h => ⟨hγW t h, (ht t ⟨ha.trans h.1, h.2.trans hb⟩).2⟩

/-- **Piece 1, as registered (BUILT).** A `TStep_N x y` has a continuous curve `γ` from `x` to
`y` with `TStep_N (γ s) y` for every `s ∈ [0,1)` and `TStep_N x (γ s)` for `s ∈ (0,1]`; so
`x ≪ y` has points `w = γ s ≪ y` arbitrarily close to `y` (and to `x`). -/
theorem mk_tstep_restrict {x y : N} (h : S.TStep x y) :
    ∃ γ : ℝ → N, Continuous γ ∧ γ 0 = x ∧ γ 1 = y ∧
      (∀ s ∈ Ico (0:ℝ) 1, S.TStep (γ s) y) ∧ ∀ s ∈ Ioc (0:ℝ) 1, S.TStep x (γ s) := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  refine ⟨γ, hγ.continuous, h0, h1, fun s hs => ?_, fun s hs => ?_⟩
  · have := mk_tstep_sub hγ ht hs.1 hs.2 le_rfl; rwa [h1] at this
  · have := mk_tstep_sub hγ ht le_rfl hs.1 hs.2; rwa [h0] at this

/-! ### Each point's `OneChart` patch -/

variable (S) in
/-- **The patch of `p`** (from `LocallyOneChart`, as in campaign 85's `me_local_step`): an open
`W ∋ p` inside `M` with `S.restrictM W` `OneChart` at `p` (in `p`'s own chart). -/
theorem mk_patch (hL : S.LocallyOneChart) {p : N} (hp : p ∈ S.M) :
    ∃ W : Set N, ∃ hW : IsOpen W, ∃ hWM : W ⊆ S.M, p ∈ W ∧ (S.restrictM W hW hWM).OneChart p := by
  obtain ⟨U, hU, hpU, -, hg, hT⟩ := hL p hp
  have hcs : ContinuousOn (extChartAt 𝓘(ℝ, E) p) (chartAt E p).source := by
    rw [← extChartAt_source (I := 𝓘(ℝ, E))]; exact continuousOn_extChartAt p
  set W : Set N := ((chartAt E p).source ∩ extChartAt 𝓘(ℝ, E) p ⁻¹' U) ∩ S.M with hWdef
  have hWo : IsOpen W :=
    (hcs.isOpen_inter_preimage (chartAt E p).open_source hU).inter S.isOpen_M
  have hWU : extChartAt 𝓘(ℝ, E) p '' W ⊆ U := by rintro _ ⟨x, hx, rfl⟩; exact hx.1.2
  exact ⟨W, hWo, inter_subset_right, ⟨⟨mem_chart_source E p, hpU⟩, hp⟩,
    { sub := fun x hx => hx.1.1, g_C1 := hg.mono hWU, T_cont := hT.mono hWU }⟩

/-! ### Piece 2: openness of `I⁺(x)`, `I⁻(z)` and `D J` on `N` -/

variable (S) in
/-- **`I⁺(x)` is open on `N` (BUILT).** For `x ≪ y`, the last step `b → y` is cut at `s` close to
`1`, so that `γ([s,1])` lies in `y`'s patch; `TStep (γ s) y` read in `y`'s chart, campaign 75's
`tstep_end_eventually`, and the transfer back give `TStep (γ s) y'` for `y'` near `y`. -/
theorem mk_isOpen_Ifut (hL : S.LocallyOneChart) (x : N) : IsOpen {y | S.Chr x y} := by
  refine isOpen_iff_mem_nhds.2 fun y hy => ?_
  obtain ⟨b, hxb, hby⟩ := Relation.TransGen.tail'_iff.1 hy
  have hyM := (S.tstep_mem hby).2
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hby
  obtain ⟨W, hW, hWM, hyW, hC⟩ := S.mk_patch hL hyM
  obtain ⟨δ, hδ, hnear⟩ := mk_near hγ.continuous hW (s := 1) (by rw [h1]; exact hyW)
  set s : ℝ := max (1/2) (1 - δ/2) with hs
  have hs1 : s < 1 := max_lt (by norm_num) (by linarith)
  have hs0 : 0 < s := lt_max_of_lt_left (by norm_num)
  have hsW : ∀ t ∈ Icc s 1, γ t ∈ W := fun t h => hnear t (by
    rw [abs_lt]; constructor <;> linarith [h.1, h.2, le_max_right (1/2:ℝ) (1 - δ/2)])
  have hxs : S.Chr x (γ s) := by
    have := mk_tstep_sub hγ ht le_rfl hs0 hs1.le
    rw [h0] at this
    exact Relation.TransGen.tail' hxb this
  have hV := ch_tstep_NV hC (mk_tstep_sub_in hW hWM hγ ht hs0.le hs1 le_rfl hsW)
  rw [h1] at hV
  have hsrc : γ s ∈ (chartAt E y).source := hC.sub (hsW s ⟨le_rfl, hs1.le⟩)
  have hev : ∀ᶠ y' in 𝓝 y, y' ∈ (chartAt E y).source ∧
      (chartSp hC).TStep (extChartAt 𝓘(ℝ, E) y (γ s)) (extChartAt 𝓘(ℝ, E) y y') :=
    Filter.Eventually.and ((chartAt E y).open_source.mem_nhds (mem_chart_source E y))
      ((ch_contAt y (mem_chart_source E y)).tendsto.eventually
        ((chartSp hC).tstep_end_eventually hV))
  filter_upwards [hev] with y' hy'
  have h := ch_tstep_VN hC hy'.2
  rw [ch_left_inv y hsrc, ch_left_inv y hy'.1] at h
  exact Relation.TransGen.tail hxs (S.restrictM_tstep h)

variable (S) in
/-- **`I⁻(z)` is open on `N` (BUILT)**, the mirror: the first step `y → c` is cut at `s` close to
`0`, and campaign 60's `tstep_start_eventually` is used in `y`'s chart. -/
theorem mk_isOpen_Ipast (hL : S.LocallyOneChart) (z : N) : IsOpen (S.Ipast z) := by
  refine isOpen_iff_mem_nhds.2 fun y hy => ?_
  have hy : S.Chr y z := hy
  obtain ⟨c, hyc, hcz⟩ := Relation.TransGen.head'_iff.1 hy
  have hyM := (S.tstep_mem hyc).1
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hyc
  obtain ⟨W, hW, hWM, hyW, hC⟩ := S.mk_patch hL hyM
  obtain ⟨δ, hδ, hnear⟩ := mk_near hγ.continuous hW (s := 0) (by rw [h0]; exact hyW)
  set s : ℝ := min (1/2) (δ/2) with hs
  have hs1 : s < 1 := lt_of_le_of_lt (min_le_left _ _) (by norm_num)
  have hs0 : 0 < s := lt_min (by norm_num) (by linarith)
  have hsW : ∀ t ∈ Icc 0 s, γ t ∈ W := fun t h => hnear t (by
    rw [abs_lt]; constructor <;> linarith [h.1, h.2, min_le_right (1/2:ℝ) (δ/2)])
  have hsz : S.Chr (γ s) z := by
    have := mk_tstep_sub hγ ht hs0.le hs1 le_rfl
    rw [h1] at this
    exact Relation.TransGen.head' this hcz
  have hV := ch_tstep_NV hC (mk_tstep_sub_in hW hWM hγ ht le_rfl hs0 hs1.le hsW)
  rw [h0] at hV
  have hsrc : γ s ∈ (chartAt E y).source := hC.sub (hsW s ⟨hs0.le, le_rfl⟩)
  have hev : ∀ᶠ y' in 𝓝 y, y' ∈ (chartAt E y).source ∧
      (chartSp hC).TStep (extChartAt 𝓘(ℝ, E) y y') (extChartAt 𝓘(ℝ, E) y (γ s)) :=
    Filter.Eventually.and ((chartAt E y).open_source.mem_nhds (mem_chart_source E y))
      ((ch_contAt y (mem_chart_source E y)).tendsto.eventually
        ((chartSp hC).tstep_start_eventually hV))
  filter_upwards [hev] with y' hy'
  have h := ch_tstep_VN hC hy'.2
  rw [ch_left_inv y hsrc, ch_left_inv y hy'.1] at h
  exact Relation.TransGen.head (S.restrictM_tstep h) hsz

variable (S) in
/-- **`D J = I⁻(J)` is open on `N` (BUILT)**, for every `J`: what campaign 85's
`me_futCauchy_of_cauchy_N` needs for `U = D J`. -/
theorem mk_isOpen_D (hL : S.LocallyOneChart) (J : Set N) : IsOpen (S.D J) :=
  isOpen_biUnion fun z _ => S.mk_isOpen_Ipast hL z

variable (S) in
/-- `q ∈ closure D ⟹ I⁻(q) ⊆ D` on `N` (campaign 75's step 1, through `mk_isOpen_Ifut`). -/
theorem mk_Ipast_subset_D (hL : S.LocallyOneChart) {J : Set N} {q : N}
    (hq : q ∈ closure (S.D J)) : S.Ipast q ⊆ S.D J := by
  intro x hx
  obtain ⟨d, hd, hdD⟩ := mem_closure_iff_nhds.1 hq _ ((S.mk_isOpen_Ifut hL x).mem_nhds hx)
  obtain ⟨j, hj, hdj⟩ := mem_iUnion₂.1 hdD
  exact mem_iUnion₂.2 ⟨j, hj, Relation.TransGen.trans hd hdj⟩

end MSpacetime

/-! ### Piece 3: the short future step near `q` (`V` side: a two-sided tube) -/

namespace Spacetime
variable (S : Spacetime V)

/-- `Safe2 y ℓ`: on `r ∈ [-ℓ, ℓ]`, `y + r • T y ∈ M` and `T y` is future-timelike there. -/
def Safe2 (y : V) (ℓ : ℝ) : Prop :=
  ∀ r ∈ Icc (-ℓ) ℓ, S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y)

/-- **Tube lemma, two-sided** (campaign 78's `safe_uniform` with `hl_seg_timelike2`). -/
lemma safe2_uniform {x : V} (hx : x ∈ S.M) : ∃ ℓ > 0, ∀ᶠ y in 𝓝 x, S.Safe2 y ℓ := by
  obtain ⟨ε, hε0, hε⟩ := S.hl_seg_timelike2 hx
  refine ⟨ε, hε0, ?_⟩
  have hc : ∀ r : ℝ, ContinuousAt (fun z : V × ℝ => (S.seg z.1 z.2, S.T z.1)) (x, r) := fun r =>
    (continuousAt_fst.add (continuousAt_snd.smul ((S.contAt_T hx).comp continuousAt_fst))).prodMk
      ((S.contAt_T hx).comp continuousAt_fst)
  exact isCompact_Icc.eventually_forall_of_forall_eventually
    (P := fun y r => S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y))
    fun r hr => (hc r).preimage_mem_nhds (S.isOpen_timelikePairs.mem_nhds (hε r hr))

end Spacetime

namespace MSpacetime
variable (S : MSpacetime E N)

/-- **Piece 3: the local future step (BUILT)**, campaign 85's `me_local_step` with `+T`: for
`q ∈ M` there is `f`, continuous at `q`, with `f q ∈ M` and `TStep_N x (f x)` for all `x` near `q`;
`f x = φ_q⁻¹(φ_q x + ℓ T_V(φ_q x))` in `q`'s patch. -/
theorem mk_local_step_fut (hL : S.LocallyOneChart) {q : N} (hq : q ∈ S.M) :
    ∃ f : N → N, ContinuousAt f q ∧ f q ∈ S.M ∧ ∀ᶠ x in 𝓝 q, S.TStep x (f x) := by
  obtain ⟨W, hW, hWM, hqW, hC⟩ := S.mk_patch hL hq
  set Sp := chartSp hC with hSp
  have huM : extChartAt 𝓘(ℝ, E) q q ∈ Sp.M := ⟨q, hqW, rfl⟩
  obtain ⟨ℓ, hℓ, hsafe⟩ := Sp.safe2_uniform huM
  have hmem : Sp.seg (extChartAt 𝓘(ℝ, E) q q) ℓ ∈ Sp.M :=
    (hsafe.self_of_nhds ℓ ⟨by linarith, le_rfl⟩).1
  obtain ⟨z, hzW, hze⟩ := hmem
  have htgt : Sp.seg (extChartAt 𝓘(ℝ, E) q q) ℓ ∈ (extChartAt 𝓘(ℝ, E) q).target := by
    rw [← hze]; exact ch_mem_target q (hC.sub hzW)
  have h1 : ContinuousAt (extChartAt 𝓘(ℝ, E) q) q := ch_contAt q (mem_chart_source E q)
  refine ⟨fun x => (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg (extChartAt 𝓘(ℝ, E) q x) ℓ), ?_, ?_, ?_⟩
  · have h2 : ContinuousAt (fun x => Sp.seg (extChartAt 𝓘(ℝ, E) q x) ℓ) q := by
      show ContinuousAt (fun x => extChartAt 𝓘(ℝ, E) q x + ℓ • Sp.T (extChartAt 𝓘(ℝ, E) q x)) q
      exact h1.add (continuousAt_const.smul ((Sp.contAt_T huM).comp h1))
    exact ContinuousAt.comp (g := (extChartAt 𝓘(ℝ, E) q).symm)
      (f := fun x => Sp.seg (extChartAt 𝓘(ℝ, E) q x) ℓ)
      ((continuousOn_extChartAt_symm q).continuousAt
        ((isOpen_extChartAt_target q).mem_nhds htgt)) h2
  · show (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg (extChartAt 𝓘(ℝ, E) q q) ℓ) ∈ S.M
    rw [← hze, ch_left_inv q (hC.sub hzW)]; exact hWM hzW
  · have hev : ∀ᶠ x in 𝓝 q, x ∈ (chartAt E q).source ∧ Sp.Safe2 (extChartAt 𝓘(ℝ, E) q x) ℓ :=
      Filter.Eventually.and ((chartAt E q).open_source.mem_nhds (mem_chart_source E q))
        (h1.tendsto.eventually hsafe)
    filter_upwards [hev] with x hx
    have hst := Sp.seg_tstep hx.2 (by linarith : -ℓ ≤ 0) hℓ le_rfl
    rw [Spacetime.seg_zero] at hst
    have h := ch_tstep_VN hC hst
    rw [ch_left_inv q hx.1] at h
    exact S.restrictM_tstep h

/-! ### Piece 4: the curve into a point -/

/-- **Piece 4: the curve into `q` (BUILT).** In `q`'s patch, `c t = φ_q⁻¹(φ_q q − ε e^{−t} T_V)`
(campaign 75's `hl_curve`, transferred): `c t → q`, for `t ≥ 0` the points lie in `M`, differ
from `q`, satisfy `c t ≪ q` and `c t ≪ c t'` (`t < t'`), and `c` is manifold-differentiable with
future-timelike `mfderiv` velocity. -/
theorem mk_curve_into (hL : S.LocallyOneChart) {q : N} (hq : q ∈ S.M) :
    ∃ c : ℝ → N, Tendsto c atTop (𝓝 q) ∧ (∀ t, 0 ≤ t → c t ∈ S.M ∧ c t ≠ q) ∧
      (∀ t, 0 ≤ t → S.Chr (c t) q) ∧ (∀ t t', 0 ≤ t → t < t' → S.Chr (c t) (c t')) ∧
      ∀ t, 0 ≤ t → MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) c t ∧ S.FutTimelike (c t) (vel c t) := by
  obtain ⟨W, hW, hWM, hqW, hC⟩ := S.mk_patch hL hq
  set Sp := chartSp hC with hSp
  set u₀ := extChartAt 𝓘(ℝ, E) q q with hu₀
  have huM : u₀ ∈ Sp.M := ⟨q, hqW, rfl⟩
  obtain ⟨ε, hε0, hε⟩ := Sp.seg_timelike huM
  set r : ℝ → ℝ := fun t => -ε * Real.exp (-t) with hr
  have hr_mem : ∀ t, 0 ≤ t → -ε ≤ r t ∧ r t < 0 := by
    intro t ht
    have h1 : Real.exp (-t) ≤ 1 := Real.exp_le_one_iff.2 (by linarith)
    have h2 : 0 < Real.exp (-t) := Real.exp_pos _
    constructor <;> simp only [hr] <;> nlinarith
  have hr_lt : ∀ t t', t < t' → r t < r t' := by
    intro t t' h
    have : Real.exp (-t') < Real.exp (-t) := Real.exp_lt_exp.2 (by linarith)
    simp only [hr]; nlinarith
  set β : ℝ → E := fun t => Sp.seg u₀ (r t) with hβ
  have hβmem : ∀ t, 0 ≤ t → β t ∈ (extChartAt 𝓘(ℝ, E) q).target ∧
      (extChartAt 𝓘(ℝ, E) q).symm (β t) ∈ W := by
    intro t ht
    obtain ⟨z, hzW, hz⟩ := (hε _ ⟨(hr_mem t ht).1, (hr_mem t ht).2.le⟩).1
    have hzs := hC.sub hzW
    refine ⟨?_, ?_⟩
    · show Sp.seg u₀ (r t) ∈ _
      rw [← hz]; exact ch_mem_target q hzs
    · show (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg u₀ (r t)) ∈ W
      rw [← hz, ch_left_inv q hzs]; exact hzW
  have hqs : q ∈ (chartAt E q).source := mem_chart_source E q
  have hderiv : ∀ t, HasDerivAt β ((ε * Real.exp (-t)) • Sp.T u₀) t := by
    intro t
    have h := ((((hasDerivAt_neg t).exp).const_mul (-ε)).smul_const (Sp.T u₀)).const_add u₀
    have e : ε * Real.exp (-t) = -ε * (Real.exp (-t) * -1) := by ring
    rw [e]; exact h
  refine ⟨fun t => (extChartAt 𝓘(ℝ, E) q).symm (β t), ?_, fun t ht => ⟨hWM (hβmem t ht).2, ?_⟩,
    fun t ht => ?_, fun t t' ht htt => ?_, fun t ht => ?_⟩
  · have hlim : Tendsto β atTop (𝓝 u₀) := by
      have h := ((tendsto_const_nhds (x := -ε)).mul
        Real.tendsto_exp_neg_atTop_nhds_zero).smul_const (Sp.T u₀) |>.const_add u₀
      simpa [Spacetime.seg, hβ, hr] using h
    have hc : ContinuousAt (extChartAt 𝓘(ℝ, E) q).symm u₀ :=
      (continuousOn_extChartAt_symm q).continuousAt
        ((isOpen_extChartAt_target q).mem_nhds (mem_extChartAt_target q))
    have h := hc.tendsto.comp hlim
    rwa [hu₀, extChartAt_to_inv] at h
  · intro he
    have he' : (extChartAt 𝓘(ℝ, E) q).symm (β t) = q := he
    have h1 : β t = u₀ := by
      have := ch_right_inv q (hβmem t ht).1
      rw [he'] at this; exact this.symm
    have h2 : r t • Sp.T u₀ = 0 := by
      have : u₀ + r t • Sp.T u₀ = u₀ + 0 := by rw [add_zero]; exact h1
      exact add_left_cancel this
    have h3 : Sp.T u₀ = 0 := (smul_eq_zero.1 h2).resolve_left (hr_mem t ht).2.ne
    have h4 := Sp.T_timelike u₀ huM
    rw [h3] at h4; simp at h4
  · have h := Sp.seg_tstep hε (hr_mem t ht).1 (hr_mem t ht).2 le_rfl
    rw [Spacetime.seg_zero] at h
    have h' := ch_tstep_VN hC h
    rw [hu₀, ch_left_inv q hqs] at h'
    exact Relation.TransGen.single (S.restrictM_tstep h')
  · have h := Sp.seg_tstep hε (hr_mem t ht).1 (hr_lt t t' htt) (hr_mem t' (by linarith)).2.le
    exact Relation.TransGen.single (S.restrictM_tstep (ch_tstep_VN hC h))
  · obtain ⟨hmd, hv⟩ := ch_vel_symm q (hderiv t).differentiableAt (hβmem t ht).1
    refine ⟨hmd, ?_⟩
    have hft : Sp.FutTimelike (β t) (deriv β t) := by
      rw [(hderiv t).deriv]
      exact Sp.futTimelike_smul (mul_pos hε0 (Real.exp_pos _))
        (hε _ ⟨(hr_mem t ht).1, (hr_mem t ht).2.le⟩).2
    have h := (futTimelike_chart' hC (hβmem t ht).1 _).1 hft
    have e : vel (fun t => (extChartAt 𝓘(ℝ, E) q).symm (β t)) t =
        dchartInv q (β t) (deriv β t) := hv
    show S.FutTimelike ((extChartAt 𝓘(ℝ, E) q).symm (β t))
      (vel (fun t => (extChartAt 𝓘(ℝ, E) q).symm (β t)) t)
    rw [e]; exact h

/-- **Piece 4, `N ∖ {q}` form (BUILT).** For `N` Hausdorff, the curve into `q` is a
future-inextendible causal curve in `M ∖ {q}`, with `c t → q`, `c t ≪ q`, `c t ≪ c t'`. -/
theorem mk_curve_inext_punctured [T2Space N] (hL : S.LocallyOneChart) {q : N} (hq : q ∈ S.M) :
    ∃ c : S.FutInextCurveIn (S.M \ {q}), Tendsto c.γ atTop (𝓝 q) ∧
      (∀ t, 0 ≤ t → S.Chr (c.γ t) q) ∧ (∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) := by
  obtain ⟨c, hlim, hmem, hq', hcc, hd⟩ := S.mk_curve_into hL hq
  refine ⟨⟨c, fun t ht => ((hd t ht).1.continuousAt).continuousWithinAt,
    fun t ht => ⟨(hmem t ht).1, (hmem t ht).2⟩, ∅, fun a b => by simp,
    fun t ht _ => ⟨(hd t ht.le).1, (hd t ht.le).2.1.le, (hd t ht.le).2.2⟩, ?_⟩, hlim, hq', hcc⟩
  rintro ⟨p, hp, hpl⟩
  exact hp.2 (tendsto_nhds_unique hpl hlim)

/-- **Piece 4, `D` form (BUILT).** For `q ∈ M ∩ closure D \ D` (`N` Hausdorff), the curve into `q`
is a future-inextendible causal curve in `D J` (`I⁻(q) ⊆ D` by `mk_Ipast_subset_D`). -/
theorem mk_curve_inext_D [T2Space N] (hL : S.LocallyOneChart) {J : Set N} {q : N} (hq : q ∈ S.M)
    (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) :
    ∃ c : S.FutInextCurveIn (S.D J), Tendsto c.γ atTop (𝓝 q) ∧
      (∀ t, 0 ≤ t → S.Chr (c.γ t) q) ∧ (∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) := by
  obtain ⟨c, hlim, -, hq', hcc, hd⟩ := S.mk_curve_into hL hq
  refine ⟨⟨c, fun t ht => ((hd t ht).1.continuousAt).continuousWithinAt,
    fun t ht => S.mk_Ipast_subset_D hL hqcl (hq' t ht), ∅, fun a b => by simp,
    fun t ht _ => ⟨(hd t ht.le).1, (hd t ht.le).2.1.le, (hd t ht.le).2.2⟩, ?_⟩, hlim, hq', hcc⟩
  rintro ⟨p, hp, hpl⟩
  exact hqD (tendsto_nhds_unique hpl hlim ▸ hp)

/-! ### Piece 5: push-up on `N` -/

variable {S}

/-- **Push-up inside one patch (BUILT; the registered reachable negative).** A causal step of
`S.restrictM W` (`W` a `OneChart` patch of `p`), followed by `b ≪ z` in `N`, gives `a ≪ z`: the
first step out of `b` is cut inside `W`, and campaign 60's `pushup_cstep` is applied in `p`'s
chart (`g` is locally Lipschitz there, being `C¹`). -/
theorem mk_pushup_patch {W : Set N} {hW : IsOpen W} {hWM : W ⊆ S.M} {p : N}
    (hC : (S.restrictM W hW hWM).OneChart p) {a b z : N}
    (hab : (S.restrictM W hW hWM).CStep a b) (hbz : S.Chr b z) : S.Chr a z := by
  have haW := ((S.restrictM W hW hWM).cstep_mem hab).1
  have hbW := ((S.restrictM W hW hWM).cstep_mem hab).2
  obtain ⟨c, hbc, hcz⟩ := Relation.TransGen.head'_iff.1 hbz
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hbc
  obtain ⟨δ, hδ, hnear⟩ := mk_near hγ.continuous hW (s := 0) (by rw [h0]; exact hbW)
  set s : ℝ := min (1/2) (δ/2) with hs
  have hs1 : s < 1 := lt_of_le_of_lt (min_le_left _ _) (by norm_num)
  have hs0 : 0 < s := lt_min (by norm_num) (by linarith)
  have hsW : ∀ t ∈ Icc 0 s, γ t ∈ W := fun t h => hnear t (by
    rw [abs_lt]; constructor <;> linarith [h.1, h.2, min_le_right (1/2:ℝ) (δ/2)])
  have hsz : S.Chr (γ s) z := by
    have := mk_tstep_sub hγ ht hs0.le hs1 le_rfl
    rw [h1] at this
    exact Relation.TransGen.head' this hcz
  have hbs : (S.restrictM W hW hWM).TStep b (γ s) := by
    have := mk_tstep_sub_in hW hWM hγ ht le_rfl hs0 hs1.le hsW
    rwa [h0] at this
  have hV := (chartSp hC).pushup_cstep (ch_chart_lipschitz hC) (ch_cstep_NV hC hab)
    (Relation.TransGen.single (ch_tstep_NV hC hbs))
  have hN := (ch_chr_iff hC (hC.sub haW) (hC.sub (hsW s ⟨hs0.le, le_rfl⟩))).2 hV
  exact Relation.TransGen.trans (S.restrictM_chr hN) hsz

/-- **Dual push-up inside one patch (BUILT).** `x ≪ a` in `N` and a causal step `a → b` of
`S.restrictM W` give `x ≪ b` (campaign 60's `hl_pushup'` in `p`'s chart). -/
theorem mk_pushup_patch' {W : Set N} {hW : IsOpen W} {hWM : W ⊆ S.M} {p : N}
    (hC : (S.restrictM W hW hWM).OneChart p) {x a b : N} (hxa : S.Chr x a)
    (hab : (S.restrictM W hW hWM).CStep a b) : S.Chr x b := by
  have haW := ((S.restrictM W hW hWM).cstep_mem hab).1
  have hbW := ((S.restrictM W hW hWM).cstep_mem hab).2
  obtain ⟨c, hxc, hca⟩ := Relation.TransGen.tail'_iff.1 hxa
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hca
  obtain ⟨δ, hδ, hnear⟩ := mk_near hγ.continuous hW (s := 1) (by rw [h1]; exact haW)
  set s : ℝ := max (1/2) (1 - δ/2) with hs
  have hs1 : s < 1 := max_lt (by norm_num) (by linarith)
  have hs0 : 0 < s := lt_max_of_lt_left (by norm_num)
  have hsW : ∀ t ∈ Icc s 1, γ t ∈ W := fun t h => hnear t (by
    rw [abs_lt]; constructor <;> linarith [h.1, h.2, le_max_right (1/2:ℝ) (1 - δ/2)])
  have hxs : S.Chr x (γ s) := by
    have := mk_tstep_sub hγ ht le_rfl hs0 hs1.le
    rw [h0] at this
    exact Relation.TransGen.tail' hxc this
  have hsa : (S.restrictM W hW hWM).TStep (γ s) a := by
    have := mk_tstep_sub_in hW hWM hγ ht hs0.le hs1 le_rfl hsW
    rwa [h1] at this
  have hV := (chartSp hC).hl_pushup' (ch_chart_lipschitz hC)
    (Relation.TransGen.single (ch_tstep_NV hC hsa))
    (Relation.ReflTransGen.single (ch_cstep_NV hC hab))
  have hN := (ch_chr_iff hC (hC.sub (hsW s ⟨le_rfl, hs1.le⟩)) (hC.sub hbW)).2 hV
  exact Relation.TransGen.trans hxs (S.restrictM_chr hN)

variable (S) in
/-- **Push-up across one `CStep_N` (BUILT).** `CStep_N x y`, `y ≪ z` ⟹ `x ≪ z`, for a step that
may cross any number of charts. No Lebesgue subdivision: campaign 60's `sInf` argument runs on
`[0,1]` directly, with the local step at `s = inf {t | α t ≪ z}` taken in `α s`'s own patch
(`mk_pushup_patch`) and openness of `I⁻(z)` on `N` (`mk_isOpen_Ipast`) forcing `s = 0`. -/
theorem mk_pushup_cstep (hL : S.LocallyOneChart) {x y z : N} (hxy : S.CStep x y)
    (hyz : S.Chr y z) : S.Chr x z := by
  obtain ⟨α, hα, h0, h1, hc⟩ := hxy
  let A : Set ℝ := {t | t ∈ Icc (0:ℝ) 1 ∧ S.Chr (α t) z}
  have h1A : (1:ℝ) ∈ A := ⟨⟨zero_le_one, le_rfl⟩, by show S.Chr (α 1) z; rw [h1]; exact hyz⟩
  have hne : A.Nonempty := ⟨1, h1A⟩
  have hbdd : BddBelow A := ⟨0, fun t ht => ht.1.1⟩
  have hs0 : 0 ≤ sInf A := le_csInf hne fun t ht => ht.1.1
  have hs1 : sInf A ≤ 1 := csInf_le hbdd h1A
  have hsA : S.Chr (α (sInf A)) z := by
    obtain ⟨W, hW, hWM, hW', hC⟩ := S.mk_patch hL (hc _ ⟨hs0, hs1⟩).1
    obtain ⟨δ, hδ, hnear⟩ := mk_near hα.continuous hW hW'
    obtain ⟨t, htA, hts⟩ := exists_lt_of_csInf_lt hne (show sInf A < sInf A + δ by linarith)
    have hst : sInf A ≤ t := csInf_le hbdd htA
    rcases hst.lt_or_eq with hst | hst
    · have hab := mk_cstep_sub_in hW hWM hα hc hs0 hst htA.1.2 fun u hu => hnear u (by
        rw [abs_lt]; constructor <;> linarith [hu.1, hu.2])
      exact mk_pushup_patch hC hab htA.2
    · rw [hst]; exact htA.2
  have hs : sInf A = 0 := by
    by_contra hne0
    have hspos : 0 < sInf A := lt_of_le_of_ne hs0 (Ne.symm hne0)
    have hev : ∀ᶠ t in 𝓝 (sInf A), S.Chr (α t) z :=
      (hα.continuous.tendsto _).eventually ((S.mk_isOpen_Ipast hL z).mem_nhds hsA)
    obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 hev
    have hm1 := min_le_left δ (sInf A)
    have hm2 := min_le_right δ (sInf A)
    have hm3 := lt_min hδ hspos
    have ht : sInf A - min δ (sInf A) / 2 ∈ A := by
      refine ⟨⟨by linarith, by linarith⟩, hδP ?_⟩
      rw [Real.dist_eq, abs_lt]; constructor <;> linarith
    have := csInf_le hbdd ht
    linarith
  rw [← h0, ← hs]; exact hsA

variable (S) in
/-- **Dual push-up across one `CStep_N` (BUILT).** `x ≪ y`, `CStep_N y z` ⟹ `x ≪ z`: the `sSup`
mirror, with `mk_pushup_patch'` and openness of `I⁺(x)` on `N`. -/
theorem mk_pushup_cstep' (hL : S.LocallyOneChart) {x y z : N} (hxy : S.Chr x y)
    (hyz : S.CStep y z) : S.Chr x z := by
  obtain ⟨α, hα, h0, h1, hc⟩ := hyz
  let A : Set ℝ := {t | t ∈ Icc (0:ℝ) 1 ∧ S.Chr x (α t)}
  have h0A : (0:ℝ) ∈ A := ⟨⟨le_rfl, zero_le_one⟩, by show S.Chr x (α 0); rw [h0]; exact hxy⟩
  have hne : A.Nonempty := ⟨0, h0A⟩
  have hbdd : BddAbove A := ⟨1, fun t ht => ht.1.2⟩
  have hs0 : 0 ≤ sSup A := le_csSup hbdd h0A
  have hs1 : sSup A ≤ 1 := csSup_le hne fun t ht => ht.1.2
  have hsA : S.Chr x (α (sSup A)) := by
    obtain ⟨W, hW, hWM, hW', hC⟩ := S.mk_patch hL (hc _ ⟨hs0, hs1⟩).1
    obtain ⟨δ, hδ, hnear⟩ := mk_near hα.continuous hW hW'
    obtain ⟨t, htA, hts⟩ := exists_lt_of_lt_csSup hne (show sSup A - δ < sSup A by linarith)
    have hst : t ≤ sSup A := le_csSup hbdd htA
    rcases hst.lt_or_eq with hst | hst
    · have hab := mk_cstep_sub_in hW hWM hα hc htA.1.1 hst hs1 fun u hu => hnear u (by
        rw [abs_lt]; constructor <;> linarith [hu.1, hu.2])
      exact mk_pushup_patch' hC htA.2 hab
    · rw [← hst]; exact htA.2
  have hs : sSup A = 1 := by
    by_contra hne1
    have hslt : sSup A < 1 := lt_of_le_of_ne hs1 hne1
    have hev : ∀ᶠ t in 𝓝 (sSup A), S.Chr x (α t) :=
      (hα.continuous.tendsto _).eventually ((S.mk_isOpen_Ifut hL x).mem_nhds hsA)
    obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 hev
    have hm1 := min_le_left δ (1 - sSup A)
    have hm2 := min_le_right δ (1 - sSup A)
    have hm3 := lt_min hδ (sub_pos.2 hslt)
    have ht : sSup A + min δ (1 - sSup A) / 2 ∈ A := by
      refine ⟨⟨by linarith, by linarith⟩, hδP ?_⟩
      rw [Real.dist_eq, abs_lt]; constructor <;> linarith
    have := le_csSup hbdd ht
    linarith
  rw [← h1, ← hs]; exact hsA

variable (S) in
/-- **Push-up on `N` (BUILT).** `x ≤ y ≪ z ⟹ x ≪ z`, for `LocallyOneChart S`. -/
theorem mk_pushup (hL : S.LocallyOneChart) {x y z : N} (hxy : S.Cau x y) (hyz : S.Chr y z) :
    S.Chr x z := by
  induction hxy using Relation.ReflTransGen.head_induction_on with
  | refl => exact hyz
  | head h _ ih => exact S.mk_pushup_cstep hL h ih

variable (S) in
/-- **Dual push-up on `N` (BUILT).** `x ≪ y ≤ z ⟹ x ≪ z`. -/
theorem mk_pushup' (hL : S.LocallyOneChart) {x y z : N} (hxy : S.Chr x y) (hyz : S.Cau y z) :
    S.Chr x z := by
  induction hyz with
  | refl => exact hxy
  | tail _ h ih => exact S.mk_pushup_cstep' hL ih h

end MSpacetime

/-! ## NEW (campaign 87): the assembly on a multi-chart `N`

Everything below is read in `N`: `hL : S.LocallyOneChart`, `[T2Space N]` (only for the curve into
a point), and campaign 84's intrinsic `D`, `𝓗⁺ = ∂_N J⁻(J)`, slices, `SublevelProper`, `KLi`/`KLs`. -/

namespace MSpacetime
variable (S : MSpacetime E N)

/-! ### Piece 1: `Θ` strictly increasing along `≪` into `D` -/

/-- `≪` into `D` starts in `D`. -/
theorem mh_D_of_chr {J : Set N} {x y : N} (h : S.Chr x y) (hy : y ∈ S.D J) : x ∈ S.D J := by
  obtain ⟨z, hz, hyz⟩ := mem_iUnion₂.1 hy
  exact mem_iUnion₂.2 ⟨z, hz, Relation.TransGen.trans h hyz⟩

/-- `𝓗⁺ ∩ D = ∅` on `N` (`D` open). -/
theorem mh_not_mem_D_of_H (hL : S.LocallyOneChart) {J : Set N} {p : N} (hp : p ∈ S.H J) :
    p ∉ S.D J := fun hpD =>
  hp.2 (interior_maximal (S.D_subset_JpastSet J) (S.mk_isOpen_D hL J) hpD)

/-- The exterior `D J` as a manifold spacetime in its own right. -/
def DspN (hL : S.LocallyOneChart) (J : Set N) : MSpacetime E N :=
  S.restrictM (S.D J) (S.mk_isOpen_D hL J) (S.D_subset_M J)

/-- **A timelike step of `N` ending in `D` runs inside `D`** (every point of its curve is `≪` its
end, by campaign 86's `mk_tstep_sub`), so it is a timelike step of `DspN`. -/
theorem mh_tstep_DspN (hL : S.LocallyOneChart) {J : Set N} {x y : N} (h : S.TStep x y)
    (hy : y ∈ S.D J) : (S.DspN hL J).TStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  refine ⟨γ, hγ, h0, h1, fun t htI => ⟨?_, (ht t htI).2⟩⟩
  rcases htI.2.lt_or_eq with hlt | heq
  · have hs := mk_tstep_sub hγ ht htI.1 hlt le_rfl
    rw [h1] at hs
    exact S.mh_D_of_chr (Relation.TransGen.single hs) hy
  · rw [heq, h1]; exact hy

/-- **Piece 1 (BUILT).** A function temporal on `D` (intrinsic, `IsTemporalOn (D J)`) strictly
increases along every `≪` of `N` ending in `D`: `me_temporal_tstep` in `DspN` and induction. -/
theorem mh_temporalD_chr (hL : S.LocallyOneChart) {J : Set N} {Θ : N → ℝ}
    (hΘ : S.IsTemporalOn (S.D J) Θ) {x y : N} (h : S.Chr x y) (hy : y ∈ S.D J) : Θ x < Θ y := by
  have hΘ' : (S.DspN hL J).IsTemporalOn (S.DspN hL J).M Θ := hΘ
  induction h with
  | single h => exact (S.DspN hL J).me_temporal_tstep hΘ' (S.mh_tstep_DspN hL h hy)
  | @tail b c hxb hbc ih =>
    have hb : b ∈ S.D J := S.mh_D_of_chr (Relation.TransGen.single hbc) hy
    exact (ih hb).trans ((S.DspN hL J).me_temporal_tstep hΘ' (S.mh_tstep_DspN hL hbc hy))

/-! ### Piece 2: `hint` and `hcl` on `N` -/

/-- **The short future step on `N` (BUILT).** Every neighbourhood of `x ∈ M` contains a `y` with
`x ≪ y`: campaign 86's `mk_local_step_fut` at `x`, cut short by `mk_tstep_restrict`. -/
theorem mh_future_step (hL : S.LocallyOneChart) {x : N} (hx : x ∈ S.M) {U : Set N}
    (hU : U ∈ 𝓝 x) : ∃ y ∈ U, S.Chr x y := by
  obtain ⟨f, -, -, hev⟩ := S.mk_local_step_fut hL hx
  obtain ⟨γ, hγc, h0, -, -, hfwd⟩ := mk_tstep_restrict hev.self_of_nhds
  have hlim : Tendsto γ (𝓝 0) (𝓝 x) := by rw [← h0]; exact hγc.tendsto 0
  obtain ⟨δ, hδ, hδU⟩ := Metric.eventually_nhds_iff.1 (hlim.eventually hU)
  set s : ℝ := min (δ / 2) 1 with hs
  have hs0 : 0 < s := lt_min (by linarith) one_pos
  have hs1 : s ≤ 1 := min_le_right _ _
  refine ⟨γ s, hδU ?_, Relation.TransGen.single (hfwd s ⟨hs0, hs1⟩)⟩
  rw [Real.dist_eq, sub_zero, abs_of_pos hs0]
  exact lt_of_le_of_lt (min_le_left _ _) (by linarith)

/-- **The short past step on `N` (BUILT).** Every neighbourhood of `x ∈ M` contains a `y ≪ x`:
the tail of campaign 86's curve into `x`. -/
theorem mh_past_step (hL : S.LocallyOneChart) {x : N} (hx : x ∈ S.M) {U : Set N}
    (hU : U ∈ 𝓝 x) : ∃ y ∈ U, S.Chr y x := by
  obtain ⟨c, hlim, -, hcx, -, -⟩ := S.mk_curve_into hL hx
  obtain ⟨t, htU, ht0⟩ := ((hlim.eventually hU).and (eventually_ge_atTop 0)).exists
  exact ⟨c t, htU, hcx t ht0⟩

/-- **`hint` on `N` (BUILT).** `int J⁻(J) ⊆ D`: a short future step `x ≪ y` inside the interior,
`y ≤ z ∈ J`, and campaign 86's dual push-up `mk_pushup'`. -/
theorem mh_hint (hL : S.LocallyOneChart) {J : Set N} (hJM : J ⊆ S.M) :
    interior (S.JpastSet J) ⊆ S.D J := by
  intro x hx
  obtain ⟨y, hy, hxy⟩ := S.mh_future_step hL (S.JpastSet_subset_M hJM (interior_subset hx))
    (isOpen_interior.mem_nhds hx)
  obtain ⟨z, hz, hyz⟩ := mem_iUnion₂.1 (interior_subset hy)
  exact mem_iUnion₂.2 ⟨z, hz, S.mk_pushup' hL hxy hyz⟩

/-- `J⁻(J) ⊆ closure D` on `N`: past steps `y ≪ x ≤ z ∈ J` give `y ≪ z`, with `y → x`. -/
theorem mh_JpastSet_subset_closure_D (hL : S.LocallyOneChart) {J : Set N} (hJM : J ⊆ S.M) :
    S.JpastSet J ⊆ closure (S.D J) := by
  intro x hx
  have hxM := S.JpastSet_subset_M hJM hx
  obtain ⟨z, hz, hxz⟩ := mem_iUnion₂.1 hx
  rw [mem_closure_iff_nhds]
  intro U hU
  obtain ⟨y, hy, hyx⟩ := S.mh_past_step hL hxM hU
  exact ⟨y, hy, mem_iUnion₂.2 ⟨z, hz, S.mk_pushup' hL hyx hxz⟩⟩

/-- **`hcl` on `N` (BUILT).** `closure J⁻(J) ⊆ closure D`. -/
theorem mh_hcl (hL : S.LocallyOneChart) {J : Set N} (hJM : J ⊆ S.M) :
    closure (S.JpastSet J) ⊆ closure (S.D J) :=
  closure_minimal (S.mh_JpastSet_subset_closure_D hL hJM) isClosed_closure

/-! ### Piece 3: properness on `N` -/

/-- `Θ` (temporal on `D`) is monotone along campaign 86's curve into a point. -/
theorem mh_curve_mono (hL : S.LocallyOneChart) {J : Set N} {Θ : N → ℝ}
    (hΘ : S.IsTemporalOn (S.D J) Θ) (c : S.FutInextCurveIn (S.D J))
    (hc : ∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) {t t' : ℝ} (ht : 0 ≤ t)
    (htt : t ≤ t') : Θ (c.γ t) ≤ Θ (c.γ t') := by
  rcases htt.lt_or_eq with h | h
  · exact (S.mh_temporalD_chr hL hΘ (hc t t' ht h) (c.mem t' (by linarith))).le
  · rw [h]

/-- **`Θ → ∞` at `q` (BUILT).** For `q ∈ M ∩ closure D \ D` and every `T'`, some neighbourhood
`U ∋ q` has `Θ > T'` on `U ∩ D`: campaign 86's curve `c` into `q` (`mk_curve_inext_D`), the future
Cauchy property gives `r = c t` with `Θ r ≥ T' + 1`, and `U = I⁺(r)` is open on `N`
(`mk_isOpen_Ifut`) and contains `q`. -/
theorem mh_blowup [T2Space N] (hL : S.LocallyOneChart) {J : Set N} {Θ : N → ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) {q : N} (hqM : q ∈ S.M)
    (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) (T' : ℝ) :
    ∃ U ∈ 𝓝 q, ∀ x ∈ U ∩ S.D J, T' < Θ x := by
  obtain ⟨c, -, hcq, -⟩ := S.mk_curve_inext_D hL hqM hqcl hqD
  obtain ⟨t, ht, hta⟩ := hΘ.2 c (max (T' + 1) (Θ (c.γ 0))) (le_max_right _ _)
  refine ⟨{y | S.Chr (c.γ t) y}, (S.mk_isOpen_Ifut hL _).mem_nhds (hcq t ht), fun x hx => ?_⟩
  have h := S.mh_temporalD_chr hL hΘ.1 hx.1 hx.2
  have := le_max_left (T' + 1) (Θ (c.γ 0))
  linarith

/-- **Piece 3 (BUILT): properness on `N`.** From the future Cauchy property, `hint` and
`𝓗⁺ ⊆ M`. -/
theorem mh_sublevelProper [T2Space N] (hL : S.LocallyOneChart) {J : Set N}
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) : S.SublevelProper J Θ := by
  intro T' p hp
  by_contra hpD
  have hpcl : p ∈ closure (S.D J) := closure_mono (fun x hx => hx.1) hp
  have hpH : p ∈ S.H J :=
    ⟨closure_mono (S.D_subset_JpastSet J) hpcl, fun hi => hpD (hint hi)⟩
  obtain ⟨U, hU, hUT⟩ := S.mh_blowup hL hΘ (hHM hpH) hpcl hpD T'
  obtain ⟨x, hxU, hxD, hxT⟩ := mem_closure_iff_nhds.1 hp U hU
  linarith [hUT x ⟨hxU, hxD⟩]

/-! ### Piece 4: the slice lower limit on `N` -/

/-- **Pointwise lower limit (BUILT).** `q ∈ M ∩ closure D \ D ⟹ q ∈ KLi(S_τ)`: the tail of the
curve into `q` lies in any neighbourhood `U`, and the levels `τ ≥ Θ(c t₀)` are hit on that tail. -/
theorem mh_mem_KLi_slice [T2Space N] (hL : S.LocallyOneChart) {J : Set N} {Θ : N → ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) {q : N} (hqM : q ∈ S.M)
    (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) : q ∈ KLi (S.slice J Θ) := by
  intro U hU
  obtain ⟨c, hlim, -, hchr⟩ := S.mk_curve_inext_D hL hqM hqcl hqD
  obtain ⟨t₀, ht₀⟩ := eventually_atTop.1 ((hlim.eventually hU).and (eventually_ge_atTop 0))
  have ht₀0 : 0 ≤ t₀ := (ht₀ t₀ le_rfl).2
  filter_upwards [eventually_ge_atTop (Θ (c.γ t₀))] with τ hτ
  obtain ⟨t, ht0, htτ⟩ :=
    hΘ.2 c τ ((S.mh_curve_mono hL hΘ.1 c hchr le_rfl ht₀0).trans hτ)
  have htt : t₀ ≤ t := by
    by_contra h
    rw [not_le] at h
    have := S.mh_temporalD_chr hL hΘ.1 (hchr t t₀ ht0 h) (c.mem t₀ ht₀0)
    linarith
  exact ⟨c.γ t, ⟨c.mem t ht0, htτ⟩, (ht₀ t htt).1⟩

/-- **Piece 4 (BUILT): `𝓗⁺ ⊆ KLi(S_τ)` on `N`.** -/
theorem mh_slice_lower_limit [T2Space N] (hL : S.LocallyOneChart) {J : Set N}
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) : S.H J ⊆ KLi (S.slice J Θ) := fun _ hq =>
  S.mh_mem_KLi_slice hL hΘ (hHM hq) (hcl (frontier_subset_closure hq))
    (S.mh_not_mem_D_of_H hL hq)

/-! ### Piece 5: the slice upper limit and Kuratowski on `N` -/

section Observer
variable {S} {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
include hOD

/-- Each `O τ` lies in `D`. -/
theorem mh_observer_mem_D (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (τ : ℝ) :
    O τ ∈ S.D J := by
  rw [← hOD]
  exact mem_iUnion₂.2 ⟨_, mem_range_self (τ + 1), hmono τ (τ + 1) (by linarith)⟩

/-- **Piece 5, upper limit (BUILT), in `N`'s topology.** For `Θ` adapted to the observer and
increasing along every `≪` ending on it: `Ls S_τ ⊆ closure J⁻(J) \ D`, hence `⊆ 𝓗⁺` given `hint`.
A point `y ∈ D = I⁻(O)` has the open neighbourhood `I⁻(O σ)` (`mk_isOpen_Ipast`), on which
`Θ < σ + c`, so only finitely-early slices meet it. -/
theorem mh_slice_upper_limit (hL : S.LocallyOneChart) {Θ : N → ℝ} {c : ℝ}
    (hadapt : ∀ τ, Θ (O τ) = τ + c) (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ))
    (hint : interior (S.JpastSet J) ⊆ S.D J) : KLs (S.slice J Θ) ⊆ S.H J := by
  intro y hy
  have hcl : y ∈ closure (S.JpastSet J) :=
    ch_KLs_subset_closure (fun τ x hx => S.D_subset_JpastSet J hx.1) hy
  refine ⟨hcl, fun hi => ?_⟩
  have hyD := hint hi
  rw [← hOD] at hyD
  obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := mem_iUnion₂.1 hyD
  have hfr := hy _ ((S.mk_isOpen_Ipast hL (O σ)).mem_nhds hσ)
  obtain ⟨τ, hτ, z, hz, hzI⟩ := frequently_atTop.1 hfr (σ + c + 1)
  have := hΘ z σ hzI
  rw [hadapt, hz.2] at this
  linarith

/-- **Piece 5, Kuratowski (BUILT).** `KLi(S_τ) = KLs(S_τ) = 𝓗⁺` on `N`, from `hcl`, `hint`,
`𝓗⁺ ⊆ M`, the future Cauchy property on `D` and an adapted observer. -/
theorem mh_slice_kuratowski [T2Space N] (hL : S.LocallyOneChart)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ} {c : ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  have h1 := S.mh_slice_lower_limit hL hcl hHM hΘ
  have h2 := mh_slice_upper_limit hOD hL hadapt
    (fun x σ h => S.mh_temporalD_chr hL hΘ.1 h (mh_observer_mem_D hOD hmono σ)) hint
  have h3 := hl_KLi_subset_KLs (S.slice J Θ)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

end Observer

variable {S}

/-! ### Piece 6: the multi-chart headline -/

/-- **Piece 6 (BUILT): `prop:causal-alignment` on a multi-chart manifold.** For a manifold
spacetime `S` on a Hausdorff `N` satisfying campaign 85's `LocallyOneChart` (every point of `M` has
a chart neighbourhood in which `g` is `C¹` and `T` continuous — no single chart need cover `M`),
an observer `O` with `I⁻(O) = D`, future-directed, `J ⊆ M`, `𝓗⁺ ⊆ M`, and `Θ` two-sided Cauchy
temporal on `D` (campaign 84's intrinsic `IsCauchyTemporalOn`) adapted to `O`: properness, and
`KLi(S_τ) = KLs(S_τ) = 𝓗⁺`, all in `N`. -/
theorem mh_causal_alignment_gh_N (hL : S.LocallyOneChart) [T2Space N] {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M)
    {Θ : N → ℝ} {c : ℝ} (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  have hF : S.FutCauchyTemporalOn (S.D J) Θ :=
    me_futCauchy_of_cauchy_N hL (S.mk_isOpen_D hL J) (S.D_subset_M J) hΘ
  have hint := S.mh_hint hL hJM
  have hcl := S.mh_hcl hL hJM
  exact ⟨S.mh_sublevelProper hL hint hHM hF,
    mh_slice_kuratowski hOD hL hmono hcl hint hHM hF hadapt⟩

end MSpacetime




/-! ## NEW (campaign 88) ①: the past cones `∂J⁻(O τ)` converge to `𝓗⁺` on `N`

Campaign 72's `hc_lower_limit` / `hc_upper_limit` / `hc_kuratowski` (`HorizonConvergence.lean`),
read on a multi-chart `N`. The ball of `V` around a horizon point is replaced by a connected open
neighbourhood (`N` is locally connected because its model `E` is: `ChartedSpace.locallyConnectedSpace`);
`hcl` and `hint` are campaign 87's `mh_hcl`, `mh_hint`; openness of `I⁻(O σ)` is `mk_isOpen_Ipast`. -/

section ConeTopology
variable {X : Type*} [TopologicalSpace X]

/-- Campaign 72's `hc_preconnected_inter_frontier`, in any topological space: a preconnected set
that meets `A` and contains a point `p ∉ int A` meets `∂A`. -/
theorem mc_preconnected_inter_frontier {C A : Set X} (hC : IsPreconnected C) {a p : X}
    (ha : a ∈ C ∩ A) (hp : p ∈ C) (hpA : p ∉ interior A) : (C ∩ frontier A).Nonempty := by
  by_contra hne
  rw [not_nonempty_iff_eq_empty] at hne
  have hnot : ∀ x ∈ C, x ∉ frontier A := fun x hx hf =>
    (eq_empty_iff_forall_notMem.1 hne) x ⟨hx, hf⟩
  have hcov : C ⊆ interior A ∪ (closure A)ᶜ := by
    intro x hx
    by_cases hcl : x ∈ closure A
    · left; by_contra hi; exact hnot x hx ⟨hcl, hi⟩
    · right; exact hcl
  have h1 : (C ∩ interior A).Nonempty := by
    refine ⟨a, ha.1, ?_⟩
    by_contra hi; exact hnot a ha.1 ⟨subset_closure ha.2, hi⟩
  have h2 : (C ∩ (closure A)ᶜ).Nonempty := by
    refine ⟨p, hp, fun hcl => hnot p hp ⟨hcl, hpA⟩⟩
  obtain ⟨x, -, hxi, hxc⟩ := hC _ _ isOpen_interior isClosed_closure.isOpen_compl hcov h1 h2
  exact hxc (interior_subset_closure hxi)

end ConeTopology

namespace MSpacetime
variable (S : MSpacetime E N)

/-- The family of past light cones `∂_N J⁻(O τ)`. -/
def cone (O : ℝ → N) (τ : ℝ) : Set N := frontier (S.Jpast (O τ))

theorem mc_Ipast_subset_Jpast (p : N) : S.Ipast p ⊆ S.Jpast p := fun _ h => S.chr_cau h

/-- `I⁻(p) ⊆ int J⁻(p)` on `N`. -/
theorem mc_Ipast_subset_interior (hL : S.LocallyOneChart) (p : N) :
    S.Ipast p ⊆ interior (S.Jpast p) :=
  interior_maximal (S.mc_Ipast_subset_Jpast p) (S.mk_isOpen_Ipast hL p)

/-- `p ∈ D ⟹ J⁻(p) ⊆ J⁻(J)` (transitivity only). -/
theorem mc_Jpast_subset_JpastSet {J : Set N} {p : N} (hp : p ∈ S.D J) :
    S.Jpast p ⊆ S.JpastSet J := by
  intro q hq
  obtain ⟨z, hz, hpz⟩ := mem_iUnion₂.1 hp
  exact mem_iUnion₂.2 ⟨z, hz, Relation.ReflTransGen.trans (show S.Cau q p from hq) (S.chr_cau hpz)⟩

section ConeObserver
variable {S} {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
  (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
include hOD hmono

omit hOD in
theorem mc_Ipast_mono {σ τ : ℝ} (h : σ ≤ τ) : S.Ipast (O σ) ⊆ S.Ipast (O τ) := by
  rcases h.lt_or_eq with h | h
  · exact fun q hq => Relation.TransGen.trans (show S.Chr q (O σ) from hq) (hmono σ τ h)
  · rw [h]

/-- `x ∈ D ⟹ x ∈ I⁻(O τ)` for all large `τ`. -/
theorem mc_D_eventually {x : N} (hx : x ∈ S.D J) : ∀ᶠ τ in atTop, x ∈ S.Ipast (O τ) := by
  rw [← hOD] at hx
  obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := mem_iUnion₂.1 hx
  filter_upwards [eventually_ge_atTop σ] with τ hτ
  exact mc_Ipast_mono hmono hτ hσ

theorem mc_interior_cone_subset (τ : ℝ) :
    interior (S.Jpast (O τ)) ⊆ interior (S.JpastSet J) :=
  interior_mono (S.mc_Jpast_subset_JpastSet (mh_observer_mem_D hOD hmono τ))

/-- **① Lower limit on `N` (BUILT).** `𝓗⁺ ⊆ KLi(∂J⁻(O τ))`: a connected open neighbourhood `C`
of `p ∈ 𝓗⁺` meets `D` (`mh_hcl`), hence `I⁻(O τ)` for all large `τ`; `p ∉ int J⁻(O τ)` since
`J⁻(O τ) ⊆ J⁻(J)` and `p ∉ int J⁻(J)`; so `C` meets `∂J⁻(O τ)`. -/
theorem mc_lower_limit (hL : S.LocallyOneChart) (hJM : J ⊆ S.M) :
    S.H J ⊆ KLi (S.cone O) := by
  have : LocallyConnectedSpace N := ChartedSpace.locallyConnectedSpace E N
  intro p hp U hU
  obtain ⟨C, ⟨hCo, hpC, hCc⟩, hCU⟩ := (LocallyConnectedSpace.open_connected_basis p).mem_iff.1 hU
  have hpD : p ∈ closure (S.D J) := S.mh_hcl hL hJM (frontier_subset_closure hp)
  obtain ⟨x, hxC, hxD⟩ := mem_closure_iff.1 hpD C hCo hpC
  filter_upwards [mc_D_eventually hOD hmono hxD] with τ hτ
  have hpi : p ∉ interior (S.Jpast (O τ)) :=
    fun h => hp.2 (mc_interior_cone_subset hOD hmono τ h)
  obtain ⟨y, hyC, hyf⟩ := mc_preconnected_inter_frontier hCc.isPreconnected
    ⟨hxC, S.mc_Ipast_subset_Jpast _ hτ⟩ hpC hpi
  exact ⟨y, hyf, hCU hyC⟩

/-- **① Upper limit on `N` (BUILT).** `KLs(∂J⁻(O τ)) ⊆ 𝓗⁺`: a limit point lies in
`closure J⁻(J)`; it is not in `D`, because a point of `D` has the open neighbourhood `I⁻(O σ)`
(`mk_isOpen_Ipast`), which lies in `int J⁻(O τ)` for every `τ ≥ σ`; and `int J⁻(J) ⊆ D`
(`mh_hint`). -/
theorem mc_upper_limit (hL : S.LocallyOneChart) (hJM : J ⊆ S.M) :
    KLs (S.cone O) ⊆ S.H J := by
  intro y hy
  have hcl : y ∈ closure (S.JpastSet J) := by
    rw [mem_closure_iff_nhds]
    intro U hU
    obtain ⟨W, hWU, hWo, hyW⟩ := _root_.mem_nhds_iff.1 hU
    obtain ⟨τ, z, hzf, hzW⟩ := (hy W (hWo.mem_nhds hyW)).exists
    obtain ⟨w, hwW, hwJ⟩ := mem_closure_iff.1 (frontier_subset_closure hzf) W hWo hzW
    exact ⟨w, hWU hwW, S.mc_Jpast_subset_JpastSet (mh_observer_mem_D hOD hmono τ) hwJ⟩
  have hnD : y ∉ S.D J := by
    intro hyD
    rw [← hOD] at hyD
    obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := mem_iUnion₂.1 hyD
    have hfr := hy _ ((S.mk_isOpen_Ipast hL (O σ)).mem_nhds hσ)
    obtain ⟨τ, hτσ, z, hzf, hzI⟩ := frequently_atTop.1 hfr σ
    exact hzf.2 (S.mc_Ipast_subset_interior hL _ (mc_Ipast_mono hmono hτσ hzI))
  exact ⟨hcl, fun hi => hnD (S.mh_hint hL hJM hi)⟩

theorem mc_cone_kuratowski (hL : S.LocallyOneChart) (hJM : J ⊆ S.M) :
    KLi (S.cone O) = S.H J ∧ KLs (S.cone O) = S.H J := by
  have h1 := mc_lower_limit hOD hmono hL hJM
  have h2 := mc_upper_limit hOD hmono hL hJM
  have h3 := hl_KLi_subset_KLs (S.cone O)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

end ConeObserver

variable {S}

/-- **① The headline (BUILT): `∂J⁻(O τ) → 𝓗⁺` in the Kuratowski sense on a multi-chart `N`.**
On the hypotheses of `mh_causal_alignment_gh_N` minus `Θ` (and minus `T2Space N` and `𝓗⁺ ⊆ M`,
which are not needed): `LocallyOneChart`, `I⁻(O) = D`, `O` future-directed, `J ⊆ M`. -/
theorem mc_cone_kuratowski_N (hL : S.LocallyOneChart) {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hJM : J ⊆ S.M) :
    KLi (S.cone O) = S.H J ∧ KLs (S.cone O) = S.H J :=
  mc_cone_kuratowski hOD hmono hL hJM

end MSpacetime

/-! ## NEW (campaign 88) ②: the tangency clause on `N`

Mathlib reads a tangent vector at `x` (and `dΘ_x = mfderiv Θ x`, `g_x`, `T_x`) in the preferred chart
at `x`. Fix a chart `e = extChartAt p` (any `p`) and re-read everything at `x ∈ src e` in `e`:
* vectors: `A_x = D e_x = mfderiv e x` (`dchartL p x`);
* covectors: `ξ ↦ ξ ∘ B_x`, `B_x = D(e⁻¹)_{e x}` (`dchartInvL p x`), so `dΘ_x` becomes
  `covCh Θ p x = dΘ_x ∘ B_x`;
* the metric: `gCh p x = hRep g p (e x)` (campaign 68's chart representative).
`B_x ∘ A_x = id = A_x ∘ B_x` (campaign 68's `ld_mfderiv_symm_chart`, `ld_mfderiv_chart_symm`).
The frame hypotheses and the rate `ξ(ℓ)/ξ(n)` are chart-free (`mc_frameHyp_toChart`,
`mc_covCh_A`), so campaign 80's `tc_tendsto` applies to the `e`-components. -/

/-- `D e_x : T_xN → E` for `e = extChartAt p`, as a map `E →L E`. -/
noncomputable def dchartL (p x : N) : E →L[ℝ] E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x
/-- `D(e⁻¹)_{e x} : E → T_xN`, as a map `E →L E`. -/
noncomputable def dchartInvL (p x : N) : E →L[ℝ] E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x)
/-- `dΘ_x = mfderiv Θ x` as a covector `E →L ℝ` (in the preferred chart at `x`). -/
noncomputable def dcov (Θ : N → ℝ) (x : N) : E →L[ℝ] ℝ := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) Θ x
/-- `dΘ_x` re-read in the chart `e = extChartAt p`: `dΘ_x ∘ D(e⁻¹)_{e x}`. -/
noncomputable def covCh (Θ : N → ℝ) (p x : N) : E →L[ℝ] ℝ := (dcov Θ x).comp (dchartInvL p x)

lemma mc_dcov_eq_dfun (Θ : N → ℝ) (x : N) (v : E) : dcov Θ x v = MSpacetime.dfun Θ x v := rfl

lemma mc_BA (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    dchartInvL p x (dchartL p x a) = a := ld_mfderiv_symm_chart p hx a

lemma mc_AB (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    dchartL p x (dchartInvL p x a) = a := ld_mfderiv_chart_symm p hx a

/-- The rate quantities are chart-free: `(dΘ_x ∘ B_x)(A_x v) = dΘ_x(v)`. -/
lemma mc_covCh_A (Θ : N → ℝ) (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (v : E) :
    covCh Θ p x (dchartL p x v) = dcov Θ x v := by
  show dcov Θ x (dchartInvL p x (dchartL p x v)) = _
  rw [mc_BA p hx]

/-- `D e_p` at `p` itself is the identity (`tangentCoordChange_self`). -/
lemma mc_A_self (p : N) (a : E) : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) p a = a := by
  have e : (extChartAt 𝓘(ℝ, E) p : N → E) = chartAt E p := rfl
  rw [e, mfderiv_chartAt_eq_tangentCoordChange (mem_chart_source E p)]
  exact tangentCoordChange_self (I := 𝓘(ℝ, E)) (mem_extChartAt_source (I := 𝓘(ℝ, E)) p)

/-- `D e_x = tangentCoordChange x p x` and `D(e⁻¹)_{e x} = tangentCoordChange p x x`. -/
lemma mc_A_eq (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    dchartL p x a = tangentCoordChange 𝓘(ℝ, E) x p x a := by
  have e : (extChartAt 𝓘(ℝ, E) p : N → E) = chartAt E p := rfl
  show mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x a = _
  rw [e, mfderiv_chartAt_eq_tangentCoordChange hx]
  rfl

lemma mc_B_eq (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    dchartInvL p x a = tangentCoordChange 𝓘(ℝ, E) p x x a := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have hxx : x ∈ (extChartAt 𝓘(ℝ, E) x).source := mem_extChartAt_source x
  have h1 : dchartL p x (tangentCoordChange 𝓘(ℝ, E) p x x a) = a := by
    rw [mc_A_eq p hx, tangentCoordChange_comp ⟨⟨hxs, hxx⟩, hxs⟩, tangentCoordChange_self hxs]
  calc dchartInvL p x a = dchartInvL p x (dchartL p x (tangentCoordChange 𝓘(ℝ, E) p x x a)) := by
        rw [h1]
    _ = _ := mc_BA p hx _

/-- The coordinate change `D(e' ∘ e⁻¹)_{e x} = tangentCoordChange p p' x` is `A'_x ∘ B_x`. -/
lemma mc_tCC_eq {p p' x : N} (hx : x ∈ (chartAt E p).source) (hx' : x ∈ (chartAt E p').source)
    (v : E) : tangentCoordChange 𝓘(ℝ, E) p p' x v = dchartL p' x (dchartInvL p x v) := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have hxs' : x ∈ (extChartAt 𝓘(ℝ, E) p').source := by rwa [extChartAt_source]
  have hxx : x ∈ (extChartAt 𝓘(ℝ, E) x).source := mem_extChartAt_source x
  rw [mc_B_eq p hx, mc_A_eq p' hx', tangentCoordChange_comp ⟨⟨hxs, hxx⟩, hxs'⟩]

/-- **Chart change of components.** For `x` in the sources of `e = extChartAt p` and
`e' = extChartAt p'`: `dΘ_x` read in `e` is `dΘ_x` read in `e'` composed with the coordinate change
`D(e' ∘ e⁻¹)_{e x} = tangentCoordChange p p' x`. -/
lemma mc_covCh_change (Θ : N → ℝ) {p p' x : N} (hx : x ∈ (chartAt E p).source)
    (hx' : x ∈ (chartAt E p').source) :
    covCh Θ p x = (covCh Θ p' x).comp (tangentCoordChange 𝓘(ℝ, E) p p' x) := by
  ext v
  show dcov Θ x (dchartInvL p x v) = dcov Θ x (dchartInvL p' x (tangentCoordChange 𝓘(ℝ, E) p p' x v))
  rw [mc_tCC_eq hx hx', mc_BA p' hx']

/-- **Frame hypotheses pull back along a linear map** (pure linear algebra): if `g' = g(B·,B·)`,
`ξ' = ξ ∘ B`, `B ℓ' = ℓ`, `B n' = n`, then `FrameHyp g ℓ n ξ ⟹ FrameHyp g' ℓ' n' ξ'`. -/
theorem mc_frameHyp_pullback {g g' : E →L[ℝ] E →L[ℝ] ℝ} {ℓ n ℓ' n' : E} {ξ ξ' : E →L[ℝ] ℝ}
    (B : E →L[ℝ] E) (hg : ∀ a b, g' a b = g (B a) (B b)) (hξ : ∀ a, ξ' a = ξ (B a))
    (hl : B ℓ' = ℓ) (hn : B n' = n) (h : TCF.FrameHyp g ℓ n ξ) : TCF.FrameHyp g' ℓ' n' ξ' := by
  obtain ⟨⟨hs, hll, hnn, hln, hW⟩, hpos⟩ := h
  simp only [TCF.bil_apply] at hs hll hnn hln hW
  refine ⟨⟨fun v w => ?_, ?_, ?_, ?_, fun e he1 he2 => ?_⟩, fun v hv => ?_⟩
  · simp only [TCF.bil_apply, hg]; exact hs _ _
  · simp only [TCF.bil_apply, hg, hl]; exact hll
  · simp only [TCF.bil_apply, hg, hn]; exact hnn
  · simp only [TCF.bil_apply, hg, hl, hn]; exact hln
  · simp only [TCF.bil_apply, hg, hl, hn] at he1 he2 ⊢
    exact hW _ he1 he2
  · obtain ⟨hv1, hv2⟩ := hv
    simp only [TCF.bil_apply, hg, map_add, hl, hn] at hv1 hv2
    rw [hξ]
    exact hpos _ ⟨by simpa only [TCF.bil_apply] using hv1, by
      simpa only [TCF.bil_apply, map_add] using hv2⟩

/-- Campaign 80's `tc_tendsto_limit` with the bounds on `‖g_i‖` and `‖ℓ_i‖` derived from
convergence `g_i → g₀`, `ℓ_i → ℓ₀` (only `‖n_i‖` needs a bound). -/
theorem mc_tendsto_limit_aux {ι : Type*} {L : Filter ι} {g : ι → E →L[ℝ] E →L[ℝ] ℝ}
    {g₀ : E →L[ℝ] E →L[ℝ] ℝ} {l n : ι → E} {ℓ₀ : E} {ξ : ι → E →L[ℝ] ℝ} {C : ℝ}
    (hF : ∀ᶠ i in L, TCF.FrameHyp (g i) (l i) (n i) (ξ i)) (hG : Tendsto g L (𝓝 g₀))
    (hn : ∀ᶠ i in L, ‖n i‖ ≤ C) (hl : Tendsto l L (𝓝 ℓ₀))
    (hr : Tendsto (fun i => ξ i (l i) / ξ i (n i)) L (𝓝 0)) :
    Tendsto (fun i => (ξ i (n i))⁻¹ • ξ i) L (𝓝 (-(g₀ ℓ₀))) := by
  have hGb : ∀ᶠ i in L, ‖g i‖ ≤ ‖g₀‖ + 1 := by
    filter_upwards [hG (closedBall_mem_nhds g₀ one_pos)] with i hi
    have h1 := mem_closedBall.1 hi
    have h2 := norm_sub_norm_le (g i) g₀
    rw [← dist_eq_norm] at h2
    linarith
  have hlb : ∀ᶠ i in L, ‖l i‖ ≤ ‖ℓ₀‖ + 1 := by
    filter_upwards [hl (closedBall_mem_nhds ℓ₀ one_pos)] with i hi
    have h1 := mem_closedBall.1 hi
    have h2 := norm_sub_norm_le (l i) ℓ₀
    rw [← dist_eq_norm] at h2
    linarith
  have hGl : Tendsto (fun i => g i (l i)) L (𝓝 (g₀ ℓ₀)) :=
    (isBoundedBilinearMap_apply.continuous.tendsto (g₀, ℓ₀)).comp (hG.prodMk_nhds hl)
  have hA : (0:ℝ) ≤ ‖g₀‖ + 1 := by have := norm_nonneg g₀; linarith
  refine TCF.tc_tendsto_limit (C := max (‖g₀‖ + 1) (max ((‖g₀‖ + 1) * max C 0) (‖ℓ₀‖ + 1)))
    hF ?_ ?_ ?_ hr hGl
  · filter_upwards [hGb] with i h using h.trans (le_max_left _ _)
  · filter_upwards [hGb, hn] with i h1 h2
    refine le_trans ?_ ((le_max_left _ _).trans (le_max_right _ _))
    exact mul_le_mul h1 (h2.trans (le_max_left _ _)) (norm_nonneg _) hA
  · filter_upwards [hlb] with i h using h.trans ((le_max_right _ _).trans (le_max_right _ _))

namespace MSpacetime
variable (S : MSpacetime E N)

/-- The metric at `x` read in the chart `e = extChartAt p`. -/
noncomputable def gCh (p x : N) : E →L[ℝ] E →L[ℝ] ℝ := hRep S.g p (extChartAt 𝓘(ℝ, E) p x)

lemma mc_gCh_apply (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a b : E) :
    S.gCh p x a b = S.gE x (dchartInvL p x a) (dchartInvL p x b) := by
  have h := ld_h_eq_hRep S.g p hx (dchartInvL p x a) (dchartInvL p x b)
  have h1 := mc_AB p hx a
  have h2 := mc_AB p hx b
  unfold dchartL at h1 h2
  have e : ∀ u w : E, u = a → w = b →
      hRep S.g p (extChartAt 𝓘(ℝ, E) p x) u w = hRep S.g p (extChartAt 𝓘(ℝ, E) p x) a b := by
    rintro u w rfl rfl; rfl
  exact (h.trans (e _ _ h1 h2)).symm

/-- At the base point the chart is the preferred one: `gCh p p = g_p`. -/
lemma mc_gCh_self (p : N) : hRep S.g p (extChartAt 𝓘(ℝ, E) p p) = S.gE p := by
  refine ContinuousLinearMap.ext fun a => ContinuousLinearMap.ext fun b => ?_
  show _ = S.g p a b
  rw [ld_h_eq_hRep S.g p (mem_chart_source E p) a b, mc_A_self, mc_A_self]

/-- **Intrinsic frame hypotheses ⟹ chart-`e` frame hypotheses.** -/
theorem mc_frameHyp_toChart {Θ : N → ℝ} (p : N) {x : N} (hx : x ∈ (chartAt E p).source)
    {ℓ n : E} (h : TCF.FrameHyp (S.gE x) ℓ n (dcov Θ x)) :
    TCF.FrameHyp (S.gCh p x) (dchartL p x ℓ) (dchartL p x n) (covCh Θ p x) :=
  mc_frameHyp_pullback (dchartInvL p x) (S.mc_gCh_apply p hx) (fun _ => rfl) (mc_BA p hx ℓ)
    (mc_BA p hx n) h

/-- **Chart-`e` frame hypotheses ⟹ intrinsic frame hypotheses** (with the frame read back). -/
theorem mc_frameHyp_ofChart {Θ : N → ℝ} (p : N) {x : N} (hx : x ∈ (chartAt E p).source)
    {ℓ' n' : E} (h : TCF.FrameHyp (S.gCh p x) ℓ' n' (covCh Θ p x)) :
    TCF.FrameHyp (S.gE x) (dchartInvL p x ℓ') (dchartInvL p x n') (dcov Θ x) := by
  refine mc_frameHyp_pullback (dchartL p x) (fun a b => ?_) (fun a => ?_) (mc_AB p hx ℓ')
    (mc_AB p hx n') h
  · rw [S.mc_gCh_apply p hx, mc_BA p hx, mc_BA p hx]
  · rw [mc_covCh_A Θ p hx]

/-- **② Tangency on `N`, in a chart `e = extChartAt p` (BUILT).** Along any filter `L` of points in
`src e`: if the frame hypotheses hold eventually *intrinsically* (`ℓ_x, n_x` a null frame of `g_x`,
`dΘ_x` positive on its future cone), the `e`-components `‖g^e_x‖`, `‖g^e_x‖‖n^e_x‖`, `‖ℓ^e_x‖` stay
bounded, and the chart-free rate `dΘ_x(ℓ_x)/dΘ_x(n_x) → 0`, then in `e`:
`dΘ^e_x / dΘ_x(n_x) + g^e_x(ℓ^e_x, ·) → 0` in operator norm. -/
theorem mc_tangency_N {Θ : N → ℝ} {ℓ n : N → E} (p : N) {L : Filter N} {C : ℝ}
    (hsrc : ∀ᶠ x in L, x ∈ (chartAt E p).source)
    (hF : ∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x))
    (hg : ∀ᶠ x in L, ‖S.gCh p x‖ ≤ C)
    (hgn : ∀ᶠ x in L, ‖S.gCh p x‖ * ‖dchartL p x (n x)‖ ≤ C)
    (hl : ∀ᶠ x in L, ‖dchartL p x (ℓ x)‖ ≤ C)
    (hr : Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0)) :
    Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ p x + S.gCh p x (dchartL p x (ℓ x))) L
      (𝓝 0) := by
  have hF' : ∀ᶠ x in L, TCF.FrameHyp (S.gCh p x) (dchartL p x (ℓ x)) (dchartL p x (n x))
      (covCh Θ p x) := by
    filter_upwards [hsrc, hF] with x hx h using S.mc_frameHyp_toChart p hx h
  have hr' : Tendsto (fun x => covCh Θ p x (dchartL p x (ℓ x)) / covCh Θ p x (dchartL p x (n x)))
      L (𝓝 0) := by
    refine hr.congr' ?_
    filter_upwards [hsrc] with x hx
    rw [mc_covCh_A Θ p hx, mc_covCh_A Θ p hx]
  refine (TCF.tc_tendsto hF' hg hgn hl hr').congr' ?_
  filter_upwards [hsrc] with x hx
  rw [mc_covCh_A Θ p hx]

/-- **② The limit form (BUILT).** At a point `q ∈ src e` with `L ≤ 𝓝 q`: if `g^e = hRep g p` is
continuous at `e q`, `‖n^e_x‖` stays bounded, `ℓ^e_x → ℓ₀`, the frame hypotheses hold eventually and
the rate tends to `0`, then `dΘ^e_x / dΘ_x(n_x) → −g^e_{e q}(ℓ₀, ·)` in operator norm. -/
theorem mc_tangency_limit_N {Θ : N → ℝ} {ℓ n : N → E} (p : N) {q : N}
    (hq : q ∈ (chartAt E p).source) {L : Filter N} (hLq : L ≤ 𝓝 q) {C : ℝ} {ℓ₀ : E}
    (hgc : ContinuousAt (hRep S.g p) (extChartAt 𝓘(ℝ, E) p q))
    (hF : ∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x))
    (hn : ∀ᶠ x in L, ‖dchartL p x (n x)‖ ≤ C)
    (hℓ : Tendsto (fun x => dchartL p x (ℓ x)) L (𝓝 ℓ₀))
    (hr : Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0)) :
    Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ p x) L
      (𝓝 (-(hRep S.g p (extChartAt 𝓘(ℝ, E) p q) ℓ₀))) := by
  have hsrc : ∀ᶠ x in L, x ∈ (chartAt E p).source :=
    hLq ((chartAt E p).open_source.mem_nhds hq)
  have hG : Tendsto (fun x => S.gCh p x) L (𝓝 (hRep S.g p (extChartAt 𝓘(ℝ, E) p q))) :=
    hgc.tendsto.comp ((ch_contAt p hq).tendsto.mono_left hLq)
  have hF' : ∀ᶠ x in L, TCF.FrameHyp (S.gCh p x) (dchartL p x (ℓ x)) (dchartL p x (n x))
      (covCh Θ p x) := by
    filter_upwards [hsrc, hF] with x hx h using S.mc_frameHyp_toChart p hx h
  have hr' : Tendsto (fun x => covCh Θ p x (dchartL p x (ℓ x)) / covCh Θ p x (dchartL p x (n x)))
      L (𝓝 0) := by
    refine hr.congr' ?_
    filter_upwards [hsrc] with x hx
    rw [mc_covCh_A Θ p hx, mc_covCh_A Θ p hx]
  refine (mc_tendsto_limit_aux hF' hG hn hℓ hr').congr' ?_
  filter_upwards [hsrc] with x hx
  rw [mc_covCh_A Θ p hx]

/-- **② In the preferred chart at the horizon point (BUILT).** With `LocallyOneChart` (which makes
`hRep g q` `C¹`, hence continuous, at `e_q q`) and `e = extChartAt q`: the limit is
`−g_q(ℓ₀, ·)`, with `g_q` the metric at `q` itself (`mc_gCh_self`). -/
theorem mc_tangency_at_N (hL : S.LocallyOneChart) {Θ : N → ℝ} {ℓ n : N → E} {q : N}
    (hqM : q ∈ S.M) {L : Filter N} (hLq : L ≤ 𝓝 q) {C : ℝ} {ℓ₀ : E}
    (hF : ∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x))
    (hn : ∀ᶠ x in L, ‖dchartL q x (n x)‖ ≤ C)
    (hℓ : Tendsto (fun x => dchartL q x (ℓ x)) L (𝓝 ℓ₀))
    (hr : Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0)) :
    Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ q x) L (𝓝 (-(S.gE q ℓ₀))) := by
  obtain ⟨U, hU, hqU, -, hg, -⟩ := hL q hqM
  have hgc : ContinuousAt (hRep S.g q) (extChartAt 𝓘(ℝ, E) q q) :=
    hg.continuousOn.continuousAt (hU.mem_nhds hqU)
  have h := S.mc_tangency_limit_N q (mem_chart_source E q) hLq hgc hF hn hℓ hr
  rwa [S.mc_gCh_self q] at h

end MSpacetime

/-- **② Chart-independence (BUILT).** If `q` lies in the sources of `e = extChartAt p` and
`e' = extChartAt p'`, `L ≤ 𝓝 q`, and the rescaled covectors read in `e'` converge to `λ'`, then read
in `e` they converge to `λ' ∘ D(e' ∘ e⁻¹)_{e q}` (`tangentCoordChange p p' q`): the limit changes by
the coordinate change at `q`. (Continuity of `tangentCoordChange` is Mathlib's
`continuousOn_tangentCoordChange`.) -/
theorem mc_chart_change (Θ : N → ℝ) {p p' q : N} (hq : q ∈ (chartAt E p).source)
    (hq' : q ∈ (chartAt E p').source) {L : Filter N} (hLq : L ≤ 𝓝 q) {c : N → ℝ}
    {lam : E →L[ℝ] ℝ} (h : Tendsto (fun x => c x • covCh Θ p' x) L (𝓝 lam)) :
    Tendsto (fun x => c x • covCh Θ p x) L
      (𝓝 (lam.comp (tangentCoordChange 𝓘(ℝ, E) p p' q))) := by
  have hO : IsOpen ((extChartAt 𝓘(ℝ, E) p).source ∩ (extChartAt 𝓘(ℝ, E) p').source) :=
    (isOpen_extChartAt_source p).inter (isOpen_extChartAt_source p')
  have hqs : q ∈ (extChartAt 𝓘(ℝ, E) p).source ∩ (extChartAt 𝓘(ℝ, E) p').source := by
    rw [extChartAt_source, extChartAt_source]; exact ⟨hq, hq'⟩
  have hK : Tendsto (tangentCoordChange 𝓘(ℝ, E) p p') L
      (𝓝 (tangentCoordChange 𝓘(ℝ, E) p p' q)) :=
    (((continuousOn_tangentCoordChange p p').continuousAt (hO.mem_nhds hqs)).tendsto).mono_left hLq
  have hc := ((ContinuousLinearMap.compL ℝ E E ℝ).continuous₂.tendsto
    (lam, tangentCoordChange 𝓘(ℝ, E) p p' q)).comp (h.prodMk_nhds hK)
  refine hc.congr' ?_
  filter_upwards [hLq (hO.mem_nhds hqs)] with x hx
  rw [extChartAt_source, extChartAt_source] at hx
  show (ContinuousLinearMap.compL ℝ E E ℝ) (c x • covCh Θ p' x) (tangentCoordChange 𝓘(ℝ, E) p p' x)
    = c x • covCh Θ p x
  rw [mc_covCh_change Θ hx.1 hx.2, ContinuousLinearMap.compL_apply,
    ContinuousLinearMap.smul_comp]

/-- **The chain rule in a chart.** For `f : E → ℝ` differentiable at `e x`:
`d(f ∘ e)_x` read in `e` is `fderiv f (e x)`. -/
theorem mc_covCh_comp_chart (p : N) {f : E → ℝ} {x : N} (hx : x ∈ (chartAt E p).source)
    (hf : DifferentiableAt ℝ f (extChartAt 𝓘(ℝ, E) p x)) :
    covCh (f ∘ extChartAt 𝓘(ℝ, E) p) p x = fderiv ℝ f (extChartAt 𝓘(ℝ, E) p x) := by
  have hy : extChartAt 𝓘(ℝ, E) p x ∈ (extChartAt 𝓘(ℝ, E) p).target := ch_mem_target p hx
  have hψ := ld_mdifferentiableAt_symm p hy
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have hφ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x :=
    mdifferentiableAt_extChartAt hx
  have hfφ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (f ∘ extChartAt 𝓘(ℝ, E) p) x :=
    (mdifferentiableAt_iff_differentiableAt.2 hf).comp x hφ
  have hfφ' : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (f ∘ extChartAt 𝓘(ℝ, E) p)
      ((extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x)) := by
    rw [ch_left_inv p hx]; exact hfφ
  have hev : (f ∘ extChartAt 𝓘(ℝ, E) p) ∘ (extChartAt 𝓘(ℝ, E) p).symm
      =ᶠ[𝓝 (extChartAt 𝓘(ℝ, E) p x)] f := by
    filter_upwards [(isOpen_extChartAt_target p).mem_nhds hy] with z hz
    simp only [Function.comp_apply, ch_right_inv p hz]
  have hD := (hf.hasFDerivAt.hasMFDerivAt).congr_of_eventuallyEq hev
  have hC := hfφ'.hasMFDerivAt.comp (extChartAt 𝓘(ℝ, E) p x) hψ.hasMFDerivAt
  ext v
  have hE := DFunLike.congr_fun (hC.mfderiv.symm.trans hD.mfderiv) v
  have key : ∀ z, z = x → ∀ w : E, (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (f ∘ extChartAt 𝓘(ℝ, E) p) z w : ℝ)
      = mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (f ∘ extChartAt 𝓘(ℝ, E) p) x w := by rintro z rfl w; rfl
  exact (key _ (ch_left_inv p hx) _).symm.trans hE

end Manifold

/-! ## NEW (campaign 89) ①, ③: the conformal extension, `𝓗⁺ = ∂J⁻(𝒥⁺)`, and the headline whole -/

section Conformal
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
variable {Ñ : Type*} [TopologicalSpace Ñ] [ChartedSpace E Ñ] [IsManifold 𝓘(ℝ, E) 1 Ñ]

/-- `Dι_x : T_xN → T_{ι x}Ñ` read as a map `E →L E` (both tangent spaces are `E`). -/
noncomputable def mx_dι (ι : N → Ñ) (x : N) : E →L[ℝ] E := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) ι x

/-- **A conformal extension** of `S` (on `N`) into `St` (on `Ñ`, same model `E`): an open
embedding `ι : N → Ñ` of class `C¹`, a positive conformal factor `Ω` with
`g̃(Dι v, Dι w) = Ω² g(v, w)`, time orientations agreeing on `M`, and `ι(M) ⊆ M̃`. -/
structure ConformalExtension (S : MSpacetime E N) (St : MSpacetime E Ñ) where
  ι : N → Ñ
  isOpenEmbedding : IsOpenEmbedding ι
  contMDiff : ContMDiff 𝓘(ℝ, E) 𝓘(ℝ, E) 1 ι
  Ω : N → ℝ
  Ω_pos : ∀ x, 0 < Ω x
  conformal : ∀ x (v w : E), St.gE (ι x) (mx_dι ι x v) (mx_dι ι x w) = Ω x ^ 2 * S.gE x v w
  timeOrient : ∀ x ∈ S.M, St.FutTimelike (ι x) (mx_dι ι x (S.T x))
  maps_M : ι '' S.M ⊆ St.M

/-- Preimage under an open embedding commutes with the frontier. -/
theorem mx_preimage_frontier {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y] {f : X → Y}
    (hf : IsOpenEmbedding f) (s : Set Y) : f ⁻¹' frontier s = frontier (f ⁻¹' s) :=
  hf.isOpenMap.preimage_frontier_eq_frontier_preimage hf.continuous s

/-- Preimage under an open embedding commutes with the closure. -/
theorem mx_preimage_closure {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y] {f : X → Y}
    (hf : IsOpenEmbedding f) (s : Set Y) : f ⁻¹' closure s = closure (f ⁻¹' s) :=
  hf.isOpenMap.preimage_closure_eq_closure_preimage hf.continuous s

namespace MSpacetime

/-- **`∂J⁻(A) = closure I⁻(A) ∖ I⁻(A)`** on any `LocallyOneChart` manifold spacetime, for
`A ⊆ M`: `int J⁻(A) = I⁻(A)` (`mh_hint` and `I⁻(A)` open, `mk_isOpen_D`) and
`closure J⁻(A) = closure I⁻(A)` (`mh_hcl`). -/
theorem mx_frontier_JpastSet {S : MSpacetime E N} (hL : S.LocallyOneChart) {A : Set N}
    (hA : A ⊆ S.M) : frontier (S.JpastSet A) = closure (S.D A) \ S.D A := by
  have hint : interior (S.JpastSet A) = S.D A :=
    (S.mh_hint hL hA).antisymm (interior_maximal (S.D_subset_JpastSet A) (S.mk_isOpen_D hL A))
  have hcl : closure (S.JpastSet A) = closure (S.D A) :=
    (S.mh_hcl hL hA).antisymm (closure_mono (S.D_subset_JpastSet A))
  rw [frontier, hint, hcl]

/-- A future-directed observer lies in `M`. -/
theorem mx_range_subset_M {S : MSpacetime E N} {O : ℝ → N}
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) : range O ⊆ S.M := by
  rintro _ ⟨s, rfl⟩
  exact (S.chr_mem (hmono s (s + 1) (by linarith))).1

/-- **① The identification (BUILT).** In a conformal extension, if `I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺)` then
`𝓗⁺ = ∂J⁻(O) = ∂J⁻(J)` equals P1's `∂J⁻(𝒥⁺) := ∂ (ι⁻¹ J̃⁻(𝒥⁺))`. Only `ι` and
`isOpenEmbedding` of the conformal extension are used. -/
theorem mx_H_eq_boundary {S : MSpacetime E N} {St : MSpacetime E Ñ} (hL : S.LocallyOneChart)
    (hLt : St.LocallyOneChart) (X : ConformalExtension S St) {𝒥 : Set Ñ} (h𝒥 : 𝒥 ⊆ St.M)
    {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) :
    S.H (range O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
      S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥) := by
  have key : frontier (X.ι ⁻¹' St.JpastSet 𝒥) =
      closure (S.IpastSet (range O)) \ S.IpastSet (range O) := by
    rw [← mx_preimage_frontier X.isOpenEmbedding, St.mx_frontier_JpastSet hLt h𝒥, preimage_sdiff,
      mx_preimage_closure X.isOpenEmbedding, hI]
    rfl
  refine ⟨?_, ?_⟩
  · rw [key, H, S.mx_frontier_JpastSet hL (mx_range_subset_M hmono)]; rfl
  · rw [key, H, S.mx_frontier_JpastSet hL hJM, ← hOD]

/-- **③ `prop:causal-alignment`, every clause, with `𝓗⁺ := ∂J⁻(𝒥⁺) = ∂(ι⁻¹ J̃⁻(𝒥⁺))` (BUILT).**
In a conformal extension with `I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺)`:
* `𝓗⁺_N = ∂J⁻(J) = ∂J⁻(𝒥⁺)` (①);
* properness and `KLi(S_τ) = KLs(S_τ) = ∂J⁻(𝒥⁺)` (`mh_causal_alignment_gh_N`);
* cone convergence `KLi(∂J⁻(O τ)) = KLs(∂J⁻(O τ)) = ∂J⁻(𝒥⁺)` (`mc_cone_kuratowski_N`);
* tangency at every `q ∈ ∂J⁻(𝒥⁺)`, in the chart at `q`, under its hypotheses (`mc_tangency_at_N`). -/
theorem mx_prop_causal_alignment [T2Space N] {S : MSpacetime E N} {St : MSpacetime E Ñ}
    (hL : S.LocallyOneChart) (hLt : St.LocallyOneChart) (X : ConformalExtension S St)
    {𝒥 : Set Ñ} (h𝒥 : 𝒥 ⊆ St.M) {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥)
    (hHM : frontier (X.ι ⁻¹' St.JpastSet 𝒥) ⊆ S.M)
    {Θ : N → ℝ} {c : ℝ} (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    S.SublevelProper J Θ ∧
    KLi (S.slice J Θ) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLs (S.slice J Θ) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLi (S.cone O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLs (S.cone O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    ∀ q ∈ frontier (X.ι ⁻¹' St.JpastSet 𝒥), ∀ (ℓ n : N → E) (L : Filter N) (C : ℝ) (ℓ₀ : E),
      L ≤ 𝓝 q →
      (∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x)) →
      (∀ᶠ x in L, ‖dchartL q x (n x)‖ ≤ C) →
      Tendsto (fun x => dchartL q x (ℓ x)) L (𝓝 ℓ₀) →
      Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0) →
      Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ q x) L (𝓝 (-(S.gE q ℓ₀))) := by
  have hH := (mx_H_eq_boundary hL hLt X h𝒥 hOD hmono hJM hI).2
  rw [← hH] at hHM ⊢
  obtain ⟨h1, h2, h3⟩ := S.mh_causal_alignment_gh_N hL hOD hmono hJM hHM hΘ hadapt
  obtain ⟨h4, h5⟩ := mc_cone_kuratowski_N hL hOD hmono hJM
  exact ⟨rfl, h1, h2, h3, h4, h5, fun q hq ℓ n L C ℓ₀ hLq hF hn hℓ hr =>
    S.mc_tangency_at_N hL (hHM hq) hLq hF hn hℓ hr⟩

end MSpacetime

/-! ## NEW (campaign 91) ①: no past light cone meets `𝓗⁺` -/

namespace MSpacetime

/-- **Step 1 (BUILT), in any `LocallyOneChart` spacetime.** `x ∈ closure J⁻(p)` and `y ≪ x` give
`y ≪ p`: `I⁺(y)` is an open neighbourhood of `x` (`mk_isOpen_Ifut`), so it meets `J⁻(p)`, and
dual push-up (`mk_pushup'`) gives `y ≪ p`. -/
theorem cd_chr_of_mem_closure_Jpast {S : MSpacetime E N} (hL : S.LocallyOneChart) {p x y : N}
    (hx : x ∈ closure (S.Jpast p)) (hyx : S.Chr y x) : S.Chr y p := by
  obtain ⟨w, hyw, hwp⟩ := mem_closure_iff_nhds.1 hx _ ((S.mk_isOpen_Ifut hL y).mem_nhds hyx)
  exact S.mk_pushup' hL hyw hwp

/-- **Step 2 (BUILT): `closure J⁻(p) ∩ M` lies in a sublevel closure.** For `p ∈ D` and `Θ`
temporal on `D`, every `x ∈ M ∩ closure J⁻(p)` is a limit of points `y ≪ x` (`mh_past_step`),
each of which is `≪ p` (step 1), hence in `D` with `Θ y < Θ p` (`mh_temporalD_chr`). -/
theorem cd_mem_closure_sublevel {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {Θ : N → ℝ} (hΘ : S.IsTemporalOn (S.D J) Θ) {p x : N} (hp : p ∈ S.D J) (hxM : x ∈ S.M)
    (hx : x ∈ closure (S.Jpast p)) : x ∈ closure {y | y ∈ S.D J ∧ Θ y ≤ Θ p} := by
  rw [mem_closure_iff_nhds]
  intro U hU
  obtain ⟨y, hyU, hyx⟩ := S.mh_past_step hL hxM hU
  have hyp := cd_chr_of_mem_closure_Jpast hL hx hyx
  exact ⟨y, hyU, S.mh_D_of_chr hyp hp, (S.mh_temporalD_chr hL hΘ hyp hp).le⟩

/-- **Step 3 (BUILT): `closure J⁻(p) ∩ M ⊆ D`** for `p ∈ D`, from properness. -/
theorem cd_closure_Jpast_subset_D {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {Θ : N → ℝ} (hΘ : S.IsTemporalOn (S.D J) Θ) (hP : S.SublevelProper J Θ) {p : N}
    (hp : p ∈ S.D J) : closure (S.Jpast p) ∩ S.M ⊆ S.D J := fun _ hx =>
  hP (Θ p) (cd_mem_closure_sublevel hL hΘ hp hx.2 hx.1)

/-- **`closure J⁻(O τ) ∩ 𝓗⁺ = ∅` (BUILT).** Under properness, `Θ` temporal on `D` and
`𝓗⁺ ⊆ M`: a horizon point of `closure J⁻(O τ)` would lie in `D` (step 3), but `𝓗⁺ ∩ D = ∅`. -/
theorem cd_closure_Jpast_inter_H {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ}
    (hΘ : S.IsTemporalOn (S.D J) Θ) (hP : S.SublevelProper J Θ) (τ : ℝ) :
    closure (S.Jpast (O τ)) ∩ S.H J = ∅ := by
  refine eq_empty_iff_forall_notMem.2 fun x hx => S.mh_not_mem_D_of_H hL hx.2 ?_
  exact cd_closure_Jpast_subset_D hL hΘ hP (mh_observer_mem_D hOD hmono τ) ⟨hx.1, hHM hx.2⟩

/-- **① The clause (BUILT): no past light cone meets `𝓗⁺`.** `S.cone O τ ∩ 𝓗⁺ = ∅` for every `τ`,
on a Hausdorff `LocallyOneChart` `N`, with `I⁻(O) = D`, `O` future-directed, `J ⊆ M`, `𝓗⁺ ⊆ M`
and `Θ` Cauchy temporal on `D`. Properness comes from `mh_sublevelProper`; `hadapt` is not used. -/
theorem cd_cone_disjoint [T2Space N] {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M)
    {Θ : N → ℝ} (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) :
    ∀ τ, S.cone O τ ∩ S.H J = ∅ := by
  have hF : S.FutCauchyTemporalOn (S.D J) Θ :=
    me_futCauchy_of_cauchy_N hL (S.mk_isOpen_D hL J) (S.D_subset_M J) hΘ
  have hP := S.mh_sublevelProper hL (S.mh_hint hL hJM) hHM hF
  intro τ
  exact subset_empty_iff.1 fun x hx =>
    (cd_closure_Jpast_inter_H hL hOD hmono hHM hΘ.1 hP τ).subset
      ⟨frontier_subset_closure hx.1, hx.2⟩

/-- **① in the headline (BUILT): `mx_prop_causal_alignment` with an eighth conjunct**,
`∂J⁻(O τ) ∩ ∂J⁻(𝒥⁺) = ∅` for every `τ`, and no new hypothesis. -/
theorem cd_prop_causal_alignment [T2Space N] {S : MSpacetime E N} {St : MSpacetime E Ñ}
    (hL : S.LocallyOneChart) (hLt : St.LocallyOneChart) (X : ConformalExtension S St)
    {𝒥 : Set Ñ} (h𝒥 : 𝒥 ⊆ St.M) {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥)
    (hHM : frontier (X.ι ⁻¹' St.JpastSet 𝒥) ⊆ S.M)
    {Θ : N → ℝ} {c : ℝ} (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    S.SublevelProper J Θ ∧
    KLi (S.slice J Θ) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLs (S.slice J Θ) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLi (S.cone O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLs (S.cone O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    (∀ q ∈ frontier (X.ι ⁻¹' St.JpastSet 𝒥), ∀ (ℓ n : N → E) (L : Filter N) (C : ℝ) (ℓ₀ : E),
      L ≤ 𝓝 q →
      (∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x)) →
      (∀ᶠ x in L, ‖dchartL q x (n x)‖ ≤ C) →
      Tendsto (fun x => dchartL q x (ℓ x)) L (𝓝 ℓ₀) →
      Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0) →
      Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ q x) L (𝓝 (-(S.gE q ℓ₀)))) ∧
    ∀ τ, S.cone O τ ∩ frontier (X.ι ⁻¹' St.JpastSet 𝒥) = ∅ := by
  obtain ⟨h0, h1, h2, h3, h4, h5, h6⟩ :=
    mx_prop_causal_alignment hL hLt X h𝒥 hOD hmono hJM hI hHM hΘ hadapt
  refine ⟨h0, h1, h2, h3, h4, h5, h6, ?_⟩
  rw [← h0] at hHM ⊢
  exact cd_cone_disjoint hL hOD hmono hJM hHM hΘ

end MSpacetime

/-! ## NEW (campaign 93 ②): `cor:densities` 7a–7c on `N` -/

namespace MSpacetime

/-- **Every slice lies in `ι⁻¹ J̃⁻(𝒥⁺)`:** `slice ⊆ D = I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺) ⊆ ι⁻¹ J̃⁻(𝒥⁺)`.
No Cauchy hypothesis. -/
theorem dn_slice_subset_JpastSet {S : MSpacetime E N} {St : MSpacetime E Ñ}
    (X : ConformalExtension S St) {𝒥 : Set Ñ} {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) (Θ : N → ℝ) (τ : ℝ) :
    S.slice J Θ τ ⊆ X.ι ⁻¹' St.JpastSet 𝒥 := fun x hx => by
  have h : x ∈ X.ι ⁻¹' St.IpastSet 𝒥 := by rw [← hI, hOD]; exact hx.1
  exact St.D_subset_JpastSet 𝒥 h

/-- **7a (BUILT): the black-hole region `M ∖ ι⁻¹ J̃⁻(𝒥⁺)` meets no slice.** -/
theorem dn_BH_inter_slice {S : MSpacetime E N} {St : MSpacetime E Ñ}
    (X : ConformalExtension S St) {𝒥 : Set Ñ} {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) (Θ : N → ℝ) (τ : ℝ) :
    (S.M \ X.ι ⁻¹' St.JpastSet 𝒥) ∩ S.slice J Θ τ = ∅ :=
  eq_empty_iff_forall_notMem.2 fun _ hx =>
    hx.1.2 (dn_slice_subset_JpastSet X hOD hI Θ τ hx.2)

/-- **7b (BUILT), as `∂J⁻(𝒥⁺)`: no slice meets `∂(ι⁻¹ J̃⁻(𝒥⁺))`.** The slice lies in the open set
`ι⁻¹ Ĩ⁻(𝒥⁺)` (`mk_isOpen_D` on `S̃`, `ι` continuous), which lies in `ι⁻¹ J̃⁻(𝒥⁺)`, so the slice
lies in its interior. -/
theorem dn_slice_inter_frontier {S : MSpacetime E N} {St : MSpacetime E Ñ}
    (hLt : St.LocallyOneChart) (X : ConformalExtension S St) {𝒥 : Set Ñ} {J : Set N}
    {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) (Θ : N → ℝ) (τ : ℝ) :
    S.slice J Θ τ ∩ frontier (X.ι ⁻¹' St.JpastSet 𝒥) = ∅ := by
  refine eq_empty_iff_forall_notMem.2 fun x hx => hx.2.2 ?_
  have hU : IsOpen (X.ι ⁻¹' St.D 𝒥) :=
    (St.mk_isOpen_D hLt 𝒥).preimage X.isOpenEmbedding.continuous
  have hxU : x ∈ X.ι ⁻¹' St.D 𝒥 := by
    show x ∈ X.ι ⁻¹' St.IpastSet 𝒥
    rw [← hI, hOD]; exact hx.1.1
  exact interior_maximal (preimage_mono (St.D_subset_JpastSet 𝒥)) hU hxU

/-- **7b (BUILT), as `𝓗⁺ = ∂J⁻(J)`: no slice meets `S.H J`** (`slice ⊆ D`, `mh_not_mem_D_of_H`). -/
theorem dn_slice_inter_H {S : MSpacetime E N} (hL : S.LocallyOneChart) (J : Set N)
    (Θ : N → ℝ) (τ : ℝ) : S.slice J Θ τ ∩ S.H J = ∅ :=
  eq_empty_iff_forall_notMem.2 fun _ hx => S.mh_not_mem_D_of_H hL hx.2 hx.1.1

/-- **7c (BUILT IN PART, as read): a set inside the black-hole region meets no slice.** -/
theorem dn_subset_BH_inter_slice {S : MSpacetime E N} {St : MSpacetime E Ñ}
    (X : ConformalExtension S St) {𝒥 : Set Ñ} {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) {B : Set N}
    (hB : B ⊆ S.M \ X.ι ⁻¹' St.JpastSet 𝒥) (Θ : N → ℝ) (τ : ℝ) :
    B ∩ S.slice J Θ τ = ∅ :=
  subset_empty_iff.1 ((inter_subset_inter_left _ hB).trans
    (dn_BH_inter_slice X hOD hI Θ τ).subset)

/-- **`cor:densities` 7a–7c (BUILT, 7c as read), in a conformal extension with `hOD` and `hI`.**
For every `Θ` and `τ`: (7a) the black-hole region meets no slice; (7b) no slice meets
`∂J⁻(𝒥⁺) = ∂(ι⁻¹ J̃⁻(𝒥⁺))`, nor `𝓗⁺ = S.H J`; (7c) any `B` inside the black-hole region meets no
slice. No Cauchy hypothesis. -/
theorem dn_cor_densities {S : MSpacetime E N} {St : MSpacetime E Ñ} (hL : S.LocallyOneChart)
    (hLt : St.LocallyOneChart) (X : ConformalExtension S St) {𝒥 : Set Ñ} {J : Set N}
    {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) :
    (∀ Θ τ, (S.M \ X.ι ⁻¹' St.JpastSet 𝒥) ∩ S.slice J Θ τ = ∅) ∧
    (∀ Θ τ, S.slice J Θ τ ∩ frontier (X.ι ⁻¹' St.JpastSet 𝒥) = ∅) ∧
    (∀ Θ τ, S.slice J Θ τ ∩ S.H J = ∅) ∧
    (∀ B ⊆ S.M \ X.ι ⁻¹' St.JpastSet 𝒥, ∀ Θ τ, B ∩ S.slice J Θ τ = ∅) :=
  ⟨dn_BH_inter_slice X hOD hI, dn_slice_inter_frontier hLt X hOD hI, dn_slice_inter_H hL J,
    fun _ hB => dn_subset_BH_inter_slice X hOD hI hB⟩

end MSpacetime

end Conformal

/-- Two spacetimes with the same `M`, `g`, `T` are equal. -/
theorem Spacetime.ch_ext {S S' : Spacetime V} (hM : S.M = S'.M) (hg : S.g = S'.g)
    (hT : S.T = S'.T) : S = S' := by
  cases S; cases S'; cases hM; cases hg; cases hT; rfl

/-! ## c2 witness: the Rindler model on a manifold with two charts

`Pt` is a copy of `ℝ²` (points `(t, x)`), a separate type with its own charted-space structure: the
atlas `{idH, nullH}`, `idH = id`, `nullH : (t, x) ↦ (U, V) = (t − x, t + x)`; the preferred chart is
`idH` on `{t < 0}` and `nullH` on `{t ≥ 0}`. Mathlib reads tangent vectors in the preferred chart, so
`g`, `T` on `Pt` are `−dt² + dx²`, `∂_t = (1,0)` on `{t < 0}` and `−dU dV`, `(1,1)` on `{t ≥ 0}`.
`p₀ = (0,0)`, so `φ = extChartAt p₀ = nullH`, which is not the identity map (`ch_chart_ne_id`).

*What is exercised:* points, curves, `≪`, `D`, `𝓗⁺`, slices and the Cauchy property go through the
non-identity map `φ`; and `Dφ = mfderiv φ` is **not** the identity on `{t < 0}` (`ch_dchart_eq`,
`ch_dchart_ne_id`: it is `nullL`), so `hRep`/`chartRep` really change the components there. The chart
spacetime is nevertheless exactly campaign 81's `mink` (`ch_chartSp_eq`), which is what lets the model
facts be reused. -/

namespace NModel
open Model Manifold ContinuousLinearMap

/-- The plane as a separate type, points `(t, x)`. -/
def Pt : Type := ℝ × ℝ

instance : TopologicalSpace Pt := inferInstanceAs (TopologicalSpace (ℝ × ℝ))

/-- The null-coordinate chart `(t, x) ↦ (t − x, t + x)`. -/
noncomputable def nullH : Pt ≃ₜ P where
  toFun := fun p : ℝ × ℝ => (p.1 - p.2, p.1 + p.2)
  invFun := fun q : P => (((q.1 + q.2) / 2, (q.2 - q.1) / 2) : ℝ × ℝ)
  left_inv := fun p : ℝ × ℝ => Prod.ext (by simp only; ring) (by simp only; ring)
  right_inv := fun q : P => Prod.ext (by simp only; ring) (by simp only; ring)
  continuous_toFun := by
    show Continuous fun p : ℝ × ℝ => (p.1 - p.2, p.1 + p.2)
    fun_prop
  continuous_invFun := by
    show Continuous fun q : ℝ × ℝ => (((q.1 + q.2) / 2, (q.2 - q.1) / 2) : ℝ × ℝ)
    fun_prop

/-- The time coordinate `t` of a point of `Pt`. -/
def tco (x : Pt) : ℝ := Prod.fst (α := ℝ) (β := ℝ) x

/-- The identity chart `(t, x) ↦ (t, x)`. -/
noncomputable def idH : Pt ≃ₜ P where
  toFun := fun p : ℝ × ℝ => p
  invFun := fun q : P => (q : ℝ × ℝ)
  left_inv := fun _ => rfl
  right_inv := fun _ => rfl
  continuous_toFun := continuous_id
  continuous_invFun := continuous_id

/-- **Two charts.** The preferred chart is the identity chart on `{t < 0}` and the null chart on
`{t ≥ 0}` (Mathlib allows any choice of preferred chart). -/
noncomputable instance : ChartedSpace P Pt where
  atlas := {idH.toOpenPartialHomeomorph, nullH.toOpenPartialHomeomorph}
  chartAt x := if tco x < 0 then idH.toOpenPartialHomeomorph
    else nullH.toOpenPartialHomeomorph
  mem_chart_source x := by split_ifs <;> simp
  chart_mem_atlas x := by split_ifs <;> simp

lemma cd_id_id : ContDiff ℝ 1 (fun y : P => idH (idH.symm y)) := by
  show ContDiff ℝ 1 (fun y : P => y); fun_prop
lemma cd_null_id : ContDiff ℝ 1 (fun y : P => nullH (idH.symm y)) := by
  show ContDiff ℝ 1 (fun y : P => (y.1 - y.2, y.1 + y.2)); fun_prop
lemma cd_id_null : ContDiff ℝ 1 (fun y : P => idH (nullH.symm y)) := by
  show ContDiff ℝ 1 (fun y : P => (((y.1 + y.2) / 2, (y.2 - y.1) / 2) : ℝ × ℝ)); fun_prop
lemma cd_null_null : ContDiff ℝ 1 (fun y : P => nullH (nullH.symm y)) := by
  show ContDiff ℝ 1 (fun y : P => ((((y.1 + y.2) / 2) - (y.2 - y.1) / 2,
    ((y.1 + y.2) / 2) + (y.2 - y.1) / 2) : ℝ × ℝ)); fun_prop

instance : IsManifold 𝓘(ℝ, P) 1 Pt := by
  apply isManifold_of_contDiffOn
  intro e e' he he'
  have he1 : e = idH.toOpenPartialHomeomorph ∨ e = nullH.toOpenPartialHomeomorph := he
  have he2 : e' = idH.toOpenPartialHomeomorph ∨ e' = nullH.toOpenPartialHomeomorph := he'
  rcases he1 with rfl | rfl <;> rcases he2 with rfl | rfl
  · exact cd_id_id.contDiffOn.congr fun y _ => by simp
  · exact cd_null_id.contDiffOn.congr fun y _ => by simp
  · exact cd_id_null.contDiffOn.congr fun y _ => by simp
  · exact cd_null_null.contDiffOn.congr fun y _ => by simp

/-- The point `(a, b)` of `Pt`. -/
def mkPt (a b : ℝ) : Pt := ((a, b) : ℝ × ℝ)

/-- The base point. -/
def p₀ : Pt := mkPt 0 0

lemma chartAt_eq (x : Pt) : chartAt P x = if tco x < 0 then
    idH.toOpenPartialHomeomorph else nullH.toOpenPartialHomeomorph := rfl

lemma chartAt_p₀ : chartAt P p₀ = nullH.toOpenPartialHomeomorph := by
  rw [chartAt_eq]; exact ite_eq_right (lt_irrefl (0:ℝ))

lemma chart_apply (x : Pt) : extChartAt 𝓘(ℝ, P) p₀ x = nullH x := by
  rw [extChartAt_coe, Function.comp_apply, chartAt_p₀]; rfl

/-- The chart is not the identity map of `ℝ²`. -/
theorem ch_chart_ne_id : extChartAt 𝓘(ℝ, P) p₀ (mkPt 1 0) ≠ ((1, 0) : ℝ × ℝ) := by
  rw [chart_apply]
  show ((1 - 0, 1 + 0) : ℝ × ℝ) ≠ (1, 0)
  norm_num

lemma source_eq : (chartAt P p₀).source = univ := by rw [chartAt_p₀]; simp

lemma target_eq : (extChartAt 𝓘(ℝ, P) p₀).target = univ := by
  rw [extChartAt_target, chartAt_p₀]; simp

lemma src (x : Pt) : x ∈ (chartAt P p₀).source := by rw [source_eq]; exact mem_univ _

/-- `nullH` as a linear map of `ℝ²`. -/
noncomputable def nullL : P →L[ℝ] P :=
  ((fst ℝ ℝ ℝ) - (snd ℝ ℝ ℝ)).prod ((fst ℝ ℝ ℝ) + (snd ℝ ℝ ℝ))

lemma nullL_apply (v : P) : nullL v = (v.1 - v.2, v.1 + v.2) := by simp [nullL]

/-- **`Dφ ≠ id` on `{t < 0}`**: there the tangent vectors are read in the identity chart, and
`Dφ = D(nullH ∘ idH⁻¹) = nullL`; on `{t ≥ 0}`, `Dφ = id`. -/
theorem ch_dchart_eq (x : Pt) (v : P) :
    dchart p₀ x v = if tco x < 0 then nullL v else v := by
  show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p₀) x v = _
  have e : (extChartAt 𝓘(ℝ, P) p₀ : Pt → P) = chartAt P p₀ := rfl
  rw [e, mfderiv_chartAt_eq_tangentCoordChange (src x), tangentCoordChange_def,
    ModelWithCorners.range_eq_univ, fderivWithin_univ]
  have e1 : ∀ y, (extChartAt 𝓘(ℝ, P) p₀ ∘ (extChartAt 𝓘(ℝ, P) x).symm) y =
      nullH ((chartAt P x).symm y) := fun y => by
    rw [Function.comp_apply, chart_apply, extChartAt_coe_symm]; rfl
  split_ifs with h
  · have hf : (extChartAt 𝓘(ℝ, P) p₀ ∘ (extChartAt 𝓘(ℝ, P) x).symm) = nullL := by
      funext y; rw [e1, chartAt_eq, ite_eq_left h, nullL_apply]; rfl
    rw [hf, ContinuousLinearMap.fderiv]; rfl
  · have hf : (extChartAt 𝓘(ℝ, P) p₀ ∘ (extChartAt 𝓘(ℝ, P) x).symm) = id := by
      funext y; rw [e1, chartAt_eq, ite_eq_right h]; exact nullH.apply_symm_apply y
    rw [hf, fderiv_id]; rfl

theorem ch_dchart_ne_id :
    mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p₀) (mkPt (-1) 0) ((1, 0) : P) ≠
      ((1, 0) : P) := by
  show dchart p₀ (mkPt (-1) 0) ((1, 0) : P) ≠ ((1, 0) : P)
  rw [ch_dchart_eq, ite_eq_left (show tco (mkPt (-1) 0) < 0 by show (-1 : ℝ) < 0; norm_num), nullL_apply]
  intro h
  have := congrArg Prod.snd h
  norm_num at this

lemma dinv_eq (x : Pt) (w : P) :
    dchartInv p₀ (extChartAt 𝓘(ℝ, P) p₀ x) w =
      if tco x < 0 then (((w.1 + w.2) / 2, (w.2 - w.1) / 2) : P) else w := by
  have h : dchart p₀ x (dchartInv p₀ (extChartAt 𝓘(ℝ, P) p₀ x) w) = w :=
    ld_mfderiv_chart_symm p₀ (src x) w
  rw [ch_dchart_eq] at h
  by_cases hx : tco x < 0
  · rw [ite_eq_left hx, nullL_apply] at h
    rw [ite_eq_left hx]
    have h1 := congrArg Prod.fst h
    have h2 := congrArg Prod.snd h
    simp only at h1 h2
    exact Prod.ext (by simp only; linarith) (by simp only; linarith)
  · rw [ite_eq_right hx] at h
    rw [ite_eq_right hx]; exact h

/-- Minkowski in `(t, x)` coordinates, `−dt² + dx²`. -/
noncomputable def gTX : P →L[ℝ] P →L[ℝ] ℝ :=
  -((fst ℝ ℝ ℝ).smulRight (fst ℝ ℝ ℝ)) + (snd ℝ ℝ ℝ).smulRight (snd ℝ ℝ ℝ)

lemma gTX_apply (v w : P) : gTX v w = -(v.1 * w.1) + v.2 * w.2 := by simp [gTX]

/-- The metric on `Pt`, in the preferred chart's coordinates at each point. -/
noncomputable def gN (x : Pt) : P →L[ℝ] P →L[ℝ] ℝ :=
  if tco x < 0 then gTX else gM
/-- The time orientation `∂_t`, in the preferred chart's coordinates. -/
noncomputable def TN (x : Pt) : P := if tco x < 0 then (1, 0) else (1, 1)

/-- **The manifold spacetime**: `M = Pt`, the flat metric and `T = ∂_t`, written in the preferred
chart at each point (`(t,x)` on `{t < 0}`, `(U,V)` on `{t ≥ 0}`). -/
noncomputable def minkN : MSpacetime P Pt where
  M := univ
  isOpen_M := isOpen_univ
  g := gN
  symm := fun x v w => by
    show gN x v w = gN x w v
    unfold gN; split_ifs
    · rw [gTX_apply, gTX_apply]; ring
    · exact mink.symm 0 v w
  T := TN
  T_timelike := fun x _ => by
    show gN x (TN x) (TN x) < 0
    unfold gN TN; split_ifs
    · rw [gTX_apply]; norm_num
    · exact mink.T_timelike 0 (mem_univ _)
  pos_on_perp := fun x _ v h hv => by
    change gN x v (TN x) = 0 at h
    show 0 < gN x v v
    unfold gN TN at *
    split_ifs at h ⊢
    · rw [gTX_apply] at h ⊢
      have h1 : v.1 = 0 := by linarith
      have h2 : v.2 ≠ 0 := fun h2 => hv (Prod.ext h1 h2)
      rw [h1]; nlinarith [sq_pos_of_ne_zero h2]
    · exact mink.pos_on_perp 0 (mem_univ _) v h hv

lemma hRep_eq : hRep minkN.g p₀ = fun _ => gM := by
  funext y
  obtain ⟨x, rfl⟩ : ∃ x, extChartAt 𝓘(ℝ, P) p₀ x = y :=
    ⟨_, (extChartAt 𝓘(ℝ, P) p₀).right_inv (by rw [target_eq]; exact mem_univ y)⟩
  refine ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => ?_
  show gN ((extChartAt 𝓘(ℝ, P) p₀).symm (extChartAt 𝓘(ℝ, P) p₀ x))
    (dchartInv p₀ (extChartAt 𝓘(ℝ, P) p₀ x) v) (dchartInv p₀ (extChartAt 𝓘(ℝ, P) p₀ x) w) = gM v w
  rw [dinv_eq x v, dinv_eq x w, ch_left_inv p₀ (src x)]
  unfold gN; split_ifs
  · rw [gTX_apply, gM_apply]; ring
  · rfl

lemma chartRep_eq : chartRep minkN.T p₀ = fun _ => ((1, 1) : P) := by
  funext y
  obtain ⟨x, rfl⟩ : ∃ x, extChartAt 𝓘(ℝ, P) p₀ x = y :=
    ⟨_, (extChartAt 𝓘(ℝ, P) p₀).right_inv (by rw [target_eq]; exact mem_univ y)⟩
  rw [ld_chartRep_apply_chart _ _ (src x)]
  show dchart p₀ x (TN x) = _
  rw [ch_dchart_eq]
  unfold TN; split_ifs
  · rw [nullL_apply]; norm_num
  · rfl

theorem ch_oneChart : minkN.OneChart p₀ where
  sub := by rw [source_eq]; exact subset_univ _
  g_C1 := by rw [hRep_eq]; exact contDiffOn_const
  T_cont := by rw [chartRep_eq]; exact continuousOn_const

/-- **The chart spacetime of `minkN` is campaign 81's `mink`.** -/
theorem ch_chartSp_eq : MSpacetime.chartSp ch_oneChart = mink := by
  refine Spacetime.ch_ext ?_ hRep_eq chartRep_eq
  show extChartAt 𝓘(ℝ, P) p₀ '' univ = univ
  refine eq_univ_of_forall fun y => ⟨(extChartAt 𝓘(ℝ, P) p₀).symm y, mem_univ _, ?_⟩
  exact (extChartAt 𝓘(ℝ, P) p₀).right_inv (by rw [target_eq]; exact mem_univ y)

/-- `φ⁻¹`. -/
noncomputable def ψ : P → Pt := (extChartAt 𝓘(ℝ, P) p₀).symm

lemma φψ (y : P) : extChartAt 𝓘(ℝ, P) p₀ (ψ y) = y :=
  (extChartAt 𝓘(ℝ, P) p₀).right_inv (by rw [target_eq]; exact mem_univ y)

/-- The worldline `J_N = φ⁻¹(range O)` on `Pt`. -/
noncomputable def JN : Set Pt := ψ '' range O

lemma image_JN : extChartAt 𝓘(ℝ, P) p₀ '' JN = range O := by
  rw [JN, image_image]; simp only [φψ, image_id']

lemma mem_D_N (A : Set P) (x : Pt) :
    x ∈ minkN.D (ψ '' A) ↔ extChartAt 𝓘(ℝ, P) p₀ x ∈ mink.D A := by
  rw [MSpacetime.ch_mem_D_iff ch_oneChart (fun _ _ => src _) (src x), ch_chartSp_eq, image_image]
  simp only [φψ, image_id']

lemma mem_H_N (x : Pt) : x ∈ minkN.H JN ↔ (extChartAt 𝓘(ℝ, P) p₀ x).1 = 0 := by
  rw [MSpacetime.ch_mem_H_iff ch_oneChart (fun _ _ => src _) (src x), ch_chartSp_eq, image_JN,
    hl_H_eq]
  rfl

/-- **Every hypothesis of `ch_causal_alignment_gh_N` holds on `Pt`**, for every good profile `G`,
with `Θ_N = Θ_G ∘ φ`, `J_N = φ⁻¹(range O)` and the observer `φ⁻¹ ∘ O'`. -/
theorem ch_witness_hypotheses {G : ℝ → ℝ} (hG : GoodG G) :
    ∃ O_N : ℝ → Pt, minkN.IpastSet (range O_N) = minkN.D JN ∧
      (∀ s t : ℝ, s < t → minkN.Chr (O_N s) (O_N t)) ∧ JN ⊆ minkN.M ∧ minkN.H JN ⊆ minkN.M ∧
      minkN.IsCauchyTemporalOn (minkN.D JN) (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      ∀ τ, (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) (O_N τ) = τ + 0 := by
  obtain ⟨O', hrange, hOD, hmono, hadapt⟩ := hG.hl_adapted
  refine ⟨fun τ => ψ (O' τ), ?_, fun s t h => ?_, subset_univ _, subset_univ _, ?_, fun τ => ?_⟩
  · show minkN.D _ = _
    have e : range (fun τ => ψ (O' τ)) = ψ '' range O' := (range_comp ψ O').symm ▸ rfl
    ext x
    rw [e, mem_D_N, JN, mem_D_N]
    have h' : mink.D (range O') = mink.D (range O) := hOD
    rw [h']
  · rw [MSpacetime.ch_chr_iff ch_oneChart (src _) (src _), ch_chartSp_eq, φψ, φψ]
    exact hmono s t h
  · refine MSpacetime.ch_isCauchy_VN ch_oneChart (subset_univ _) ?_
    rw [ch_chartSp_eq, image_JN]
    exact hl_cauchy hG
  · show ThetaG G (extChartAt 𝓘(ℝ, P) p₀ (ψ (O' τ))) = _
    rw [φψ]; exact hadapt τ


/-! ### Copied (campaign 85): every point's own chart -/

/-- The inverse null map `(U, V) ↦ ((U+V)/2, (V−U)/2)` as a linear map. -/
noncomputable def nullInvL : P →L[ℝ] P :=
  ((1/2 : ℝ) • ((fst ℝ ℝ ℝ) + (snd ℝ ℝ ℝ))).prod ((1/2 : ℝ) • ((snd ℝ ℝ ℝ) - (fst ℝ ℝ ℝ)))

lemma nullInvL_apply (v : P) : nullInvL v = ((v.1 + v.2) / 2, (v.2 - v.1) / 2) := by
  ext <;> simp [nullInvL] <;> ring

lemma chartAt_neg {p : Pt} (hp : tco p < 0) : chartAt P p = idH.toOpenPartialHomeomorph := by
  rw [chartAt_eq, ite_eq_left hp]

lemma chartAt_nonneg {p : Pt} (hp : ¬ tco p < 0) : chartAt P p = chartAt P p₀ := by
  rw [chartAt_eq, ite_eq_right hp, chartAt_p₀]

lemma extChartAt_nonneg {p : Pt} (hp : ¬ tco p < 0) :
    extChartAt 𝓘(ℝ, P) p = extChartAt 𝓘(ℝ, P) p₀ := by
  unfold extChartAt; rw [chartAt_nonneg hp]

lemma chart_apply_neg {p : Pt} (hp : tco p < 0) (x : Pt) : extChartAt 𝓘(ℝ, P) p x = idH x := by
  rw [extChartAt_coe, Function.comp_apply, chartAt_neg hp]; rfl

lemma src_neg {p : Pt} (hp : tco p < 0) (x : Pt) : x ∈ (chartAt P p).source := by
  rw [chartAt_neg hp]; simp

/-- `Dφ_p` for a base point `p` with `t < 0` (chart `idH`): the identity on `{t < 0}` and the
inverse null map on `{t ≥ 0}`. -/
theorem me_dchart_neg {p : Pt} (hp : tco p < 0) (x : Pt) (v : P) :
    dchart p x v = if tco x < 0 then v else nullInvL v := by
  show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p) x v = _
  have e : (extChartAt 𝓘(ℝ, P) p : Pt → P) = chartAt P p := rfl
  rw [e, mfderiv_chartAt_eq_tangentCoordChange (src_neg hp x), tangentCoordChange_def,
    ModelWithCorners.range_eq_univ, fderivWithin_univ]
  have e1 : ∀ y, (extChartAt 𝓘(ℝ, P) p ∘ (extChartAt 𝓘(ℝ, P) x).symm) y =
      idH ((chartAt P x).symm y) := fun y => by
    rw [Function.comp_apply, chart_apply_neg hp, extChartAt_coe_symm]; rfl
  split_ifs with h
  · have hf : (extChartAt 𝓘(ℝ, P) p ∘ (extChartAt 𝓘(ℝ, P) x).symm) = id := by
      funext y; rw [e1, chartAt_eq, ite_eq_left h]; exact idH.apply_symm_apply y
    rw [hf, fderiv_id]; rfl
  · have hf : (extChartAt 𝓘(ℝ, P) p ∘ (extChartAt 𝓘(ℝ, P) x).symm) = nullInvL := by
      funext y; rw [e1, chartAt_eq, ite_eq_right h, nullInvL_apply]; rfl
    rw [hf, ContinuousLinearMap.fderiv]; rfl

lemma dinv_neg {p : Pt} (hp : tco p < 0) (x : Pt) (w : P) :
    dchartInv p (extChartAt 𝓘(ℝ, P) p x) w = if tco x < 0 then w else nullL w := by
  have h : dchart p x (dchartInv p (extChartAt 𝓘(ℝ, P) p x) w) = w :=
    ld_mfderiv_chart_symm p (src_neg hp x) w
  rw [me_dchart_neg hp] at h
  by_cases hx : tco x < 0
  · rw [ite_eq_left hx] at h; rw [ite_eq_left hx]; exact h
  · rw [ite_eq_right hx, nullInvL_apply] at h
    rw [ite_eq_right hx, nullL_apply]
    have h1 := congrArg Prod.fst h
    have h2 := congrArg Prod.snd h
    simp only at h1 h2
    exact Prod.ext (by simp only; linarith) (by simp only; linarith)

lemma hRep_neg {p : Pt} (hp : tco p < 0) : hRep minkN.g p = fun _ => gTX := by
  funext y
  obtain ⟨x, rfl⟩ : ∃ x, extChartAt 𝓘(ℝ, P) p x = y :=
    ⟨idH.symm y, by rw [chart_apply_neg hp]; exact idH.apply_symm_apply y⟩
  refine ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => ?_
  show gN ((extChartAt 𝓘(ℝ, P) p).symm (extChartAt 𝓘(ℝ, P) p x))
    (dchartInv p (extChartAt 𝓘(ℝ, P) p x) v) (dchartInv p (extChartAt 𝓘(ℝ, P) p x) w) = gTX v w
  rw [dinv_neg hp x v, dinv_neg hp x w, ch_left_inv p (src_neg hp x)]
  unfold gN; split_ifs
  · rfl
  · rw [gTX_apply, gM_apply, nullL_apply, nullL_apply]; ring

lemma chartRep_neg {p : Pt} (hp : tco p < 0) : chartRep minkN.T p = fun _ => ((1, 0) : P) := by
  funext y
  obtain ⟨x, rfl⟩ : ∃ x, extChartAt 𝓘(ℝ, P) p x = y :=
    ⟨idH.symm y, by rw [chart_apply_neg hp]; exact idH.apply_symm_apply y⟩
  rw [ld_chartRep_apply_chart _ _ (src_neg hp x)]
  show dchart p x (TN x) = _
  rw [me_dchart_neg hp]
  unfold TN; split_ifs
  · rfl
  · rw [nullInvL_apply]; norm_num

/-- Points of `Pt` use different preferred charts: `idH` at `(−1, 0)`, `nullH` at `(1, 0)`. -/
theorem me_charts_differ :
    extChartAt 𝓘(ℝ, P) (mkPt (-1) 0) (mkPt 1 0) ≠ extChartAt 𝓘(ℝ, P) (mkPt 1 0) (mkPt 1 0) := by
  have h1 : tco (mkPt (-1) 0) < 0 := by show (-1 : ℝ) < 0; norm_num
  have h2 : ¬ tco (mkPt 1 0) < 0 := by show ¬ (1 : ℝ) < 0; norm_num
  rw [chart_apply_neg h1, extChartAt_nonneg h2, chart_apply]
  show ((1, 0) : ℝ × ℝ) ≠ (1 - 0, 1 + 0)
  norm_num

/-- **`LocallyOneChart` on the two-chart manifold (BUILT).** At `p` with `t < 0` the preferred
chart is `idH`, and `hRep g p = −dt² + dx²`, `chartRep T p = (1, 0)` (`hRep_neg`, `chartRep_neg`,
through the non-identity `Dφ_p` on `{t ≥ 0}`); at `p` with `t ≥ 0` it is `nullH`, with campaign 84's
`hRep_eq`, `chartRep_eq`. -/
theorem me_locallyOneChart : minkN.LocallyOneChart := by
  intro p _
  by_cases hp : tco p < 0
  · refine ⟨univ, isOpen_univ, mem_univ _, fun y _ => ⟨idH.symm y, ⟨mem_univ _, src_neg hp _⟩, ?_⟩,
      ?_, ?_⟩
    · rw [chart_apply_neg hp]; exact idH.apply_symm_apply y
    · rw [hRep_neg hp]; exact contDiffOn_const
    · rw [chartRep_neg hp]; exact continuousOn_const
  · have hh : hRep minkN.g p = hRep minkN.g p₀ := by unfold hRep; rw [extChartAt_nonneg hp]
    have hc : chartRep minkN.T p = chartRep minkN.T p₀ := by
      unfold chartRep; rw [extChartAt_nonneg hp]
    refine ⟨univ, isOpen_univ, mem_univ _, fun y _ => ⟨ψ y, ⟨mem_univ _, ?_⟩, ?_⟩, ?_, ?_⟩
    · rw [chartAt_nonneg hp]; exact src _
    · rw [extChartAt_nonneg hp]; exact φψ y
    · rw [hh, hRep_eq]; exact contDiffOn_const
    · rw [hc, chartRep_eq]; exact continuousOn_const


/-! ### NEW (campaign 87): the multi-chart headline witnessed end to end on `Pt` -/

instance : T2Space Pt := inferInstanceAs (T2Space (ℝ × ℝ))

/-- **Every hypothesis of `mh_causal_alignment_gh_N` holds on the two-chart `Pt`** (BUILT), for
every good profile `G`, with `Θ_N = Θ_G ∘ φ`, `J_N = φ⁻¹(range O)`: `LocallyOneChart` (campaign 85,
preferred charts `idH` on `{t < 0}` and `nullH` on `{t ≥ 0}`), `T2Space Pt`, and, by campaign 84's
transport `ch_isCauchy_VN` from campaign 81's two-sided Rindler model `Model.hl_cauchy`, the
two-sided Cauchy property on `D_N` (the hypothesis campaign 85 left unwitnessed), with the observer,
`hOD`, `hmono`, `J ⊆ M`, `𝓗⁺ ⊆ M` and `hadapt`. -/
theorem mh_witness_hypotheses {G : ℝ → ℝ} (hG : GoodG G) :
    minkN.LocallyOneChart ∧ extChartAt 𝓘(ℝ, P) (mkPt (-1) 0) (mkPt 1 0) ≠ extChartAt 𝓘(ℝ, P) (mkPt 1 0) (mkPt 1 0) ∧
    ∃ O_N : ℝ → Pt, minkN.IpastSet (range O_N) = minkN.D JN ∧
      (∀ s t : ℝ, s < t → minkN.Chr (O_N s) (O_N t)) ∧ JN ⊆ minkN.M ∧ minkN.H JN ⊆ minkN.M ∧
      minkN.IsCauchyTemporalOn (minkN.D JN) (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      ∀ τ, (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) (O_N τ) = τ + 0 :=
  ⟨me_locallyOneChart, me_charts_differ, ch_witness_hypotheses hG⟩

/-- **The multi-chart headline on `Pt`, end to end (BUILT).** `𝓗⁺_N = φ⁻¹{U = 0} ≠ ∅`, and for
every good `G`: properness and `KLi(S_τ) = KLs(S_τ) = 𝓗⁺_N`, obtained from
`mh_causal_alignment_gh_N` (not from campaign 84's one-chart theorem). -/
theorem mh_witness_headline_G {G : ℝ → ℝ} (hG : GoodG G) :
    (∀ x : Pt, x ∈ minkN.H JN ↔ (extChartAt 𝓘(ℝ, P) p₀ x).1 = 0) ∧ (minkN.H JN).Nonempty ∧
    minkN.SublevelProper JN (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
    KLi (minkN.slice JN (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN ∧
    KLs (minkN.slice JN (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN := by
  obtain ⟨hL, -, O_N, hOD, hmono, hJM, hHM, hΘ, hadapt⟩ := mh_witness_hypotheses hG
  exact ⟨mem_H_N, ⟨ψ (0, 0), (mem_H_N _).2 (by rw [φψ])⟩,
    MSpacetime.mh_causal_alignment_gh_N hL hOD hmono hJM hHM hΘ hadapt⟩

/-- **The registered witness (BUILT):** on the two-chart `Pt` (points with `t < 0` and `t ≥ 0` take
different preferred charts), for `Θ₀ ∘ φ` and the tangency-failing `Θf ∘ φ`:
`KLi = KLs = 𝓗⁺ = {U = 0}`, with properness, via `mh_causal_alignment_gh_N`. -/
theorem mh_witness_headline :
    minkN.LocallyOneChart ∧ extChartAt 𝓘(ℝ, P) (mkPt (-1) 0) (mkPt 1 0) ≠ extChartAt 𝓘(ℝ, P) (mkPt 1 0) (mkPt 1 0) ∧
    (∀ x : Pt, x ∈ minkN.H JN ↔ (extChartAt 𝓘(ℝ, P) p₀ x).1 = 0) ∧ (minkN.H JN).Nonempty ∧
    (minkN.SublevelProper JN (Θ₀ ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      KLi (minkN.slice JN (Θ₀ ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN ∧
      KLs (minkN.slice JN (Θ₀ ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN) ∧
    (minkN.SublevelProper JN (Θf ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      KLi (minkN.slice JN (Θf ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN ∧
      KLs (minkN.slice JN (Θf ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN) :=
  ⟨me_locallyOneChart, me_charts_differ, mem_H_N, (mh_witness_headline_G goodG_log).2.1,
    (mh_witness_headline_G goodG_log).2.2, (mh_witness_headline_G goodG_Ffail).2.2⟩

end NModel

/-! ## NEW (campaign 88) ③: the witness on the two-chart `Pt`

Campaign 79's `SliceTangency.lean` frame (`ℓ = ∂_V`, `n = 2∂_U` in null coordinates, `g = −dU dV`),
its sequence `x_m = (−e^{−(2m+1)π}, 0)` and the computations behind `st_aligned` /
`st_tangency_fails`, transported to `Pt` through the global chart `φ = extChartAt p₀` (`nullH`), the
way campaign 87 transports the Cauchy hypothesis. -/

namespace Model
open ContinuousLinearMap

set_option synthInstance.maxHeartbeats 400000

/-- The generator direction `ℓ = ∂_V` of `𝓗⁺ = {U = 0}` (campaign 79's `ℓ`). -/
def ellV : P := (0, 1)
/-- The transverse null vector `n = 2∂_U`, `g(ℓ, n) = −1` (campaign 79's `nvec`). -/
def nvec : P := (2, 0)

/-- **The frame hypotheses for `g = −dU dV`** (campaign 80's `tc_frameHyp2` at `F = 1`): `(ℓ, n)`
is a null frame, and any covector with `ξ(∂_U) > 0`, `ξ(∂_V) > 0` is positive on the future cone. -/
theorem mc_frameHyp_gM {ξ : P →L[ℝ] ℝ} (h1 : 0 < ξ (1, 0)) (h2 : 0 < ξ (0, 1)) :
    TCF.FrameHyp gM ellV nvec ξ := by
  refine ⟨⟨fun v w => ?_, ?_, ?_, ?_, fun e he1 he2 => ?_⟩, fun v hv => ?_⟩
  · simp only [TCF.bil_apply, gM_apply]; ring
  · simp only [TCF.bil_apply, gM_apply, ellV]; norm_num
  · simp only [TCF.bil_apply, gM_apply, nvec]; norm_num
  · simp only [TCF.bil_apply, gM_apply, ellV, nvec]; norm_num
  · simp only [TCF.bil_apply, gM_apply, ellV, nvec] at he1 he2 ⊢
    have h1 : e.1 = 0 := by linarith
    have h2 : e.2 = 0 := by linarith
    rw [h1, h2]; norm_num
  · obtain ⟨hv1, hv2⟩ := hv
    simp only [TCF.bil_apply, gM_apply, ellV, nvec, Prod.fst_add, Prod.snd_add] at hv1 hv2
    have hs : 0 < v.1 + 2 * v.2 := by nlinarith
    have hp : 0 ≤ v.1 * v.2 := by nlinarith
    have hv1' : 0 ≤ v.1 := by
      by_contra h; push Not at h
      have : v.2 ≤ 0 := by nlinarith
      nlinarith
    have hv2' : 0 ≤ v.2 := by
      by_contra h; push Not at h
      have : v.1 ≤ 0 := by nlinarith
      nlinarith
    have hv : v = v.1 • ((1, 0) : P) + v.2 • ((0, 1) : P) := by ext <;> simp
    rw [hv, map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul]
    rcases hv1'.eq_or_lt with h0 | h0
    · rw [← h0] at hs ⊢
      have : 0 < v.2 := by linarith
      simp only [zero_mul, zero_add]; positivity
    · have := mul_pos h0 h1
      nlinarith [mul_nonneg hv2' h2.le]

/-- `dΘ_G(∂_U) > 0` and `dΘ_G(∂_V) = 1` on `{U < 0}`. -/
lemma mc_dTh_pos {G : ℝ → ℝ} (hG : GoodG G) {p : P} (hp : p.1 < 0) :
    0 < dTh G p (1, 0) ∧ 0 < dTh G p (0, 1) := by
  rw [dTh_apply, dTh_apply]
  have := hG.deriv_neg (-p.1) (by linarith)
  constructor
  · simp; linarith
  · simp

/-- `−g(ℓ, ·) = ½ dU`. -/
lemma mc_neg_gM_ell : -(gM ellV) = (1 / 2 : ℝ) • fst ℝ ℝ ℝ := by
  ext
  · simp [gM_apply, ellV]; norm_num
  · simp [gM_apply, ellV]

/-! Campaign 79's sequence, copied. -/

/-- `s_m = e^{−(2m+1)π}`. -/
noncomputable def sm (m : ℕ) : ℝ := Real.exp (-((2 * m + 1) * Real.pi))
/-- `x_m = (U, V) = (−s_m, 0)`. -/
noncomputable def xm (m : ℕ) : P := (-sm m, 0)

lemma log_sm (m : ℕ) : Real.log (sm m) = -((2 * m + 1) * Real.pi) := Real.log_exp _

lemma cos_log_sm (m : ℕ) : Real.cos (Real.log (sm m)) = -1 := by
  rw [log_sm, Real.cos_neg]
  have : (2 * (m:ℝ) + 1) * Real.pi = Real.pi + m * (2 * Real.pi) := by ring
  rw [this, Real.cos_add_nat_mul_two_pi, Real.cos_pi]

lemma deriv_Ffail_sm (m : ℕ) : deriv Ffail (sm m) = -1 := by
  have hs : 0 < sm m := Real.exp_pos _
  rw [(Ffail_hasDerivAt hs).deriv, cos_log_sm]
  ring

lemma xm_mem (m : ℕ) : (xm m).1 < 0 := by
  simp only [xm, Left.neg_neg_iff]; exact Real.exp_pos _

/-- At `x_m`, `dΘ = dU + dV` (campaign 79's `fderiv_xm`, via `dTh`). -/
lemma dTh_xm (m : ℕ) (v : P) : dTh Ffail (xm m) v = v.1 + v.2 := by
  rw [dTh_apply]
  have : -(xm m).1 = sm m := by simp [xm]
  rw [this, deriv_Ffail_sm]; ring

lemma xm_tendsto : Tendsto xm atTop (𝓝 (0, 0)) := by
  have hsm : Tendsto sm atTop (𝓝 0) := by
    refine Real.tendsto_exp_atBot.comp ?_
    refine tendsto_neg_atTop_atBot.comp ?_
    refine Tendsto.atTop_mul_const Real.pi_pos ?_
    exact tendsto_atTop_add_const_right _ 1
      (Tendsto.const_mul_atTop two_pos tendsto_natCast_atTop_atTop)
  have := (hsm.neg).prodMk_nhds (tendsto_const_nhds (x := (0:ℝ)))
  rw [neg_zero] at this
  exact this

end Model

namespace NModel
open Model Manifold ContinuousLinearMap

/-- `φ = extChartAt p₀` (the null chart `nullH`). -/
noncomputable def φ : Pt → P := extChartAt 𝓘(ℝ, P) p₀

lemma φ_continuous : Continuous φ := by
  have e : φ = fun x => nullH x := funext chart_apply
  rw [e]; exact nullH.continuous

lemma ψ_continuous : Continuous ψ := by
  have h := continuousOn_extChartAt_symm (I := 𝓘(ℝ, P)) p₀
  rw [target_eq] at h
  exact continuousOn_univ.1 h

lemma φ_p₀ : φ p₀ = (0, 0) := by
  show extChartAt 𝓘(ℝ, P) p₀ p₀ = _
  rw [chart_apply]
  show ((0:ℝ) - 0, (0:ℝ) + 0) = ((0:ℝ), (0:ℝ))
  norm_num

lemma ψ_zero : ψ (0, 0) = p₀ := by
  rw [← φ_p₀]; exact ch_left_inv p₀ (src p₀)

lemma mem_D_JN_iff (x : Pt) : x ∈ minkN.D JN ↔ (φ x).1 < 0 := by
  rw [JN, mem_D_N, hl_D_eq]; rfl

lemma φ_tendsto (q : Pt) :
    Tendsto φ (𝓝[minkN.D JN] q) (𝓝[{p : P | p.1 < 0}] (φ q)) :=
  tendsto_nhdsWithin_iff.2 ⟨(φ_continuous.tendsto q).mono_left nhdsWithin_le_nhds,
    eventually_mem_nhdsWithin.mono fun x hx => (mem_D_JN_iff x).1 hx⟩

/-- The intrinsic null frame on `Pt`: `ℓ = ∂_V`, `n = 2∂_U` (null coordinates), read in each
point's preferred chart. -/
noncomputable def ℓN (x : Pt) : P := dchartInvL p₀ x ellV
noncomputable def nN (x : Pt) : P := dchartInvL p₀ x nvec

lemma A_ℓN (x : Pt) : dchartL p₀ x (ℓN x) = ellV := mc_AB p₀ (src x) _
lemma A_nN (x : Pt) : dchartL p₀ x (nN x) = nvec := mc_AB p₀ (src x) _

/-- `dΘ_x` read in `φ` is `dΘ_G` at `φ x`. -/
lemma covCh_ThetaG {G : ℝ → ℝ} (hG : GoodG G) {x : Pt} (hx : x ∈ minkN.D JN) :
    covCh (ThetaG G ∘ φ) p₀ x = dTh G (φ x) := by
  have hx' := (mem_D_JN_iff x).1 hx
  rw [φ, mc_covCh_comp_chart p₀ (src x) (hG.hasFDerivAt hx').differentiableAt]
  exact hG.fderiv_eq hx'

lemma dcov_ℓN {G : ℝ → ℝ} (hG : GoodG G) {x : Pt} (hx : x ∈ minkN.D JN) :
    dcov (ThetaG G ∘ φ) x (ℓN x) = dTh G (φ x) ellV := by
  show covCh (ThetaG G ∘ φ) p₀ x ellV = _
  rw [covCh_ThetaG hG hx]

lemma dcov_nN {G : ℝ → ℝ} (hG : GoodG G) {x : Pt} (hx : x ∈ minkN.D JN) :
    dcov (ThetaG G ∘ φ) x (nN x) = dTh G (φ x) nvec := by
  show covCh (ThetaG G ∘ φ) p₀ x nvec = _
  rw [covCh_ThetaG hG hx]

lemma gCh_p₀ (x : Pt) : minkN.gCh p₀ x = gM := by
  show hRep minkN.g p₀ _ = gM
  rw [hRep_eq]

/-- **The intrinsic frame hypotheses on `Pt`, for every good profile, at every point of `D`.** -/
theorem mc_witness_frameHyp {G : ℝ → ℝ} (hG : GoodG G) {x : Pt} (hx : x ∈ minkN.D JN) :
    TCF.FrameHyp (minkN.gE x) (ℓN x) (nN x) (dcov (ThetaG G ∘ φ) x) := by
  refine minkN.mc_frameHyp_ofChart p₀ (src x) ?_
  rw [gCh_p₀, covCh_ThetaG hG hx]
  have h := mc_dTh_pos hG ((mem_D_JN_iff x).1 hx)
  exact mc_frameHyp_gM h.1 h.2

lemma ratio_Θ₀ {x : Pt} (hx : x ∈ minkN.D JN) :
    dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (nN x) = -(φ x).1 / 2 := by
  have hx' := (mem_D_JN_iff x).1 hx
  have hs : (0:ℝ) < -(φ x).1 := by linarith
  rw [Θ₀, dcov_ℓN goodG_log hx, dcov_nN goodG_log hx, dTh_apply, dTh_apply]
  have hl : HasDerivAt (fun s => -Real.log s) (-(-(φ x).1)⁻¹) (-(φ x).1) :=
    (Real.hasDerivAt_log hs.ne').neg
  rw [hl.deriv]
  simp only [ellV, nvec]
  have hne : (φ x).1 ≠ 0 := hx'.ne
  field_simp
  ring

/-- **③ Alignment holds for `Θ₀ ∘ φ` at every horizon point (BUILT).** Along `𝓝[D] q` (a proper
filter): the intrinsic frame hypotheses, the rate `dΘ(ℓ)/dΘ(n) = −U/2 → 0`, the conclusion of
`mc_tangency_N` in the chart `φ`, and the limit `dΘ^φ/dΘ(n) → −g(ℓ, ·) = ½ dU` by
`mc_tangency_limit_N`. -/
theorem mc_witness_tangency_holds (q : Pt) (hq : q ∈ minkN.H JN) :
    minkN.IsCauchyTemporalOn (minkN.D JN) (Θ₀ ∘ φ) ∧ (𝓝[minkN.D JN] q).NeBot ∧
    (∀ᶠ x in 𝓝[minkN.D JN] q, TCF.FrameHyp (minkN.gE x) (ℓN x) (nN x) (dcov (Θ₀ ∘ φ) x)) ∧
    Tendsto (fun x => dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (nN x)) (𝓝[minkN.D JN] q)
      (𝓝 0) ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x +
      minkN.gCh p₀ x (dchartL p₀ x (ℓN x))) (𝓝[minkN.D JN] q) (𝓝 0) ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x) (𝓝[minkN.D JN] q)
      (𝓝 ((1 / 2 : ℝ) • fst ℝ ℝ ℝ)) := by
  have hne : (𝓝[minkN.D JN] q).NeBot :=
    mem_closure_iff_nhdsWithin_neBot.1
      (minkN.mh_hcl me_locallyOneChart (subset_univ _) (frontier_subset_closure hq))
  have hF : ∀ᶠ x in 𝓝[minkN.D JN] q,
      TCF.FrameHyp (minkN.gE x) (ℓN x) (nN x) (dcov (Θ₀ ∘ φ) x) := by
    filter_upwards [self_mem_nhdsWithin] with x hx using mc_witness_frameHyp goodG_log hx
  have hq0 : (φ q).1 = 0 := (mem_H_N q).1 hq
  have hr : Tendsto (fun x => dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (nN x))
      (𝓝[minkN.D JN] q) (𝓝 0) := by
    have hc : Tendsto (fun x => -(φ x).1 / 2) (𝓝[minkN.D JN] q) (𝓝 0) := by
      have := (((continuous_fst.comp φ_continuous).neg.div_const (2:ℝ)).tendsto q).mono_left
        (nhdsWithin_le_nhds (s := minkN.D JN))
      simpa [Function.comp_def, hq0] using this
    refine hc.congr' ?_
    filter_upwards [self_mem_nhdsWithin] with x hx using (ratio_Θ₀ hx).symm
  have hgn : ∀ᶠ x in 𝓝[minkN.D JN] q, ‖minkN.gCh p₀ x‖ * ‖dchartL p₀ x (nN x)‖ ≤
      ‖gM‖ * ‖nvec‖ + ‖gM‖ + ‖ellV‖ :=
    Eventually.of_forall fun x => by
      rw [gCh_p₀, A_nN]; have := norm_nonneg gM; have := norm_nonneg ellV; linarith
  have h1 := minkN.mc_tangency_N p₀ (C := ‖gM‖ * ‖nvec‖ + ‖gM‖ + ‖ellV‖)
    (Eventually.of_forall fun x => src x) hF
    (Eventually.of_forall fun x => by
      rw [gCh_p₀]; have := mul_nonneg (norm_nonneg gM) (norm_nonneg nvec)
      have := norm_nonneg ellV; linarith) hgn
    (Eventually.of_forall fun x => by
      rw [A_ℓN]; have := mul_nonneg (norm_nonneg gM) (norm_nonneg nvec)
      have := norm_nonneg gM; linarith) hr
  have hgc : ContinuousAt (hRep minkN.g p₀) (extChartAt 𝓘(ℝ, P) p₀ q) := by
    rw [hRep_eq]; exact continuousAt_const
  have h2 := minkN.mc_tangency_limit_N p₀ (src q) nhdsWithin_le_nhds (C := ‖nvec‖) (ℓ₀ := ellV)
    hgc hF (Eventually.of_forall fun x => by rw [A_nN])
    (tendsto_const_nhds.congr fun x => (A_ℓN x).symm) hr
  rw [hRep_eq] at h2
  obtain ⟨-, -, -, -, -, hΘ, -⟩ := ch_witness_hypotheses goodG_log
  exact ⟨hΘ, hne, hF, hr, h1, by simpa only [mc_neg_gM_ell] using h2⟩

/-- The coordinate change from `idH` (the chart at `(−1, 0)`) to `nullH` at `p₀` is `nullL`. -/
lemma tCC_neg_p₀ : tangentCoordChange 𝓘(ℝ, P) (mkPt (-1) 0) p₀ p₀ = nullL := by
  have hneg : tco (mkPt (-1) 0) < 0 := by show (-1 : ℝ) < 0; norm_num
  refine ContinuousLinearMap.ext fun w => ?_
  rw [mc_tCC_eq (src_neg hneg p₀) (src p₀)]
  have h1 : dchartInvL (mkPt (-1) 0) p₀ w = nullL w := by
    show dchartInv (mkPt (-1) 0) (extChartAt 𝓘(ℝ, P) (mkPt (-1) 0) p₀) w = _
    rw [dinv_neg hneg, ite_eq_right (show ¬ tco p₀ < 0 from lt_irrefl (0:ℝ))]
  rw [h1]
  exact mc_A_self p₀ _

/-- **③ At `q = p₀ = (0,0)`, in the preferred chart at `q` (`LocallyOneChart`), and re-read in the
other chart `idH` (BUILT).** `mc_tangency_at_N` gives `dΘ^{e_q}/dΘ(n) → −g_q(ℓ, ·) = ½ dU`, and
`mc_chart_change` moves the limit to the chart at `(−1, 0)` (`idH`, `(t, x)` coordinates, a different
chart) as `½ dU ∘ tangentCoordChange = ½ dU ∘ nullL = ½ (dt − dx)`. -/
theorem mc_witness_tangency_at :
    p₀ ∈ minkN.H JN ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x) (𝓝[minkN.D JN] p₀)
      (𝓝 (-(minkN.gE p₀ ellV))) ∧
    minkN.gE p₀ = gM ∧
    chartAt P (mkPt (-1) 0) ≠ chartAt P p₀ ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) (mkPt (-1) 0) x)
      (𝓝[minkN.D JN] p₀)
      (𝓝 ((-(gM ellV)).comp (tangentCoordChange 𝓘(ℝ, P) (mkPt (-1) 0) p₀ p₀))) ∧
    (-(gM ellV)).comp (tangentCoordChange 𝓘(ℝ, P) (mkPt (-1) 0) p₀ p₀) =
      (1 / 2 : ℝ) • (fst ℝ ℝ ℝ - snd ℝ ℝ ℝ) := by
  have hp : p₀ ∈ minkN.H JN := (mem_H_N p₀).2 (by rw [show extChartAt 𝓘(ℝ, P) p₀ p₀ = φ p₀ from rfl,
    φ_p₀])
  obtain ⟨-, -, hF, hr, -, -⟩ := mc_witness_tangency_holds p₀ hp
  have hg : minkN.gE p₀ = gM := by
    show gN p₀ = gM
    unfold gN; rw [ite_eq_right (show ¬ tco p₀ < 0 from lt_irrefl (0:ℝ))]
  have h := minkN.mc_tangency_at_N me_locallyOneChart (mem_univ p₀) nhdsWithin_le_nhds
    (C := ‖nvec‖) (ℓ₀ := ellV) hF (Eventually.of_forall fun x => by rw [A_nN])
    (tendsto_const_nhds.congr fun x => (A_ℓN x).symm) hr
  have hneg : tco (mkPt (-1) 0) < 0 := by show (-1 : ℝ) < 0; norm_num
  refine ⟨hp, h, hg, ?_, ?_, ?_⟩
  · rw [chartAt_neg hneg, chartAt_p₀]
    intro h'
    have := congrArg (fun e : OpenPartialHomeomorph Pt P => e (mkPt 1 0)) h'
    have h2 : idH (mkPt 1 0) = nullH (mkPt 1 0) := this
    have h3 := congrArg Prod.snd h2
    change (0:ℝ) = 1 + 0 at h3
    norm_num at h3
  · rw [hg] at h
    exact mc_chart_change (Θ₀ ∘ φ) (src_neg hneg p₀) (src p₀) nhdsWithin_le_nhds h
  · rw [tCC_neg_p₀]
    ext
    · simp [nullL_apply, gM_apply, ellV]; norm_num
    · simp [nullL_apply, gM_apply, ellV]

/-- **③ Alignment fails for `Θf ∘ φ` (BUILT).** At the horizon point `p₀`: the intrinsic frame
hypotheses hold on all of `D` and `Θf ∘ φ` is two-sided Cauchy temporal on `D` (campaign 87's
witness), yet along the points `ψ(x_m) → p₀` of `D`, `dΘ = dU + dV`, so the rate is `1/2` and does
not tend to `0`, and the conclusion `dΘ^φ/dΘ(n) → −g(ℓ, ·)` fails (its value on `ℓ` is `1/2`, not
`0`). -/
theorem mc_witness_tangency_fails :
    p₀ ∈ minkN.H JN ∧
    minkN.IsCauchyTemporalOn (minkN.D JN) (Θf ∘ φ) ∧
    (∀ x ∈ minkN.D JN, TCF.FrameHyp (minkN.gE x) (ℓN x) (nN x) (dcov (Θf ∘ φ) x)) ∧
    ¬ Tendsto (fun x => dcov (Θf ∘ φ) x (ℓN x) / dcov (Θf ∘ φ) x (nN x)) (𝓝[minkN.D JN] p₀)
      (𝓝 0) ∧
    ¬ Tendsto (fun x => (dcov (Θf ∘ φ) x (nN x))⁻¹ • covCh (Θf ∘ φ) p₀ x) (𝓝[minkN.D JN] p₀)
      (𝓝 (-(gM ellV))) := by
  have hp : p₀ ∈ minkN.H JN := (mem_H_N p₀).2 (by rw [show extChartAt 𝓘(ℝ, P) p₀ p₀ = φ p₀ from rfl,
    φ_p₀])
  obtain ⟨-, -, -, -, -, hΘ, -⟩ := ch_witness_hypotheses goodG_Ffail
  have hmem : ∀ m, ψ (xm m) ∈ minkN.D JN := fun m => by
    rw [mem_D_JN_iff]; show (extChartAt 𝓘(ℝ, P) p₀ (ψ (xm m))).1 < 0
    rw [φψ]; exact xm_mem m
  have hφx : ∀ m, φ (ψ (xm m)) = xm m := fun m => φψ _
  have hseq : Tendsto (fun m => ψ (xm m)) atTop (𝓝[minkN.D JN] p₀) := by
    refine tendsto_nhdsWithin_iff.2 ⟨?_, Eventually.of_forall hmem⟩
    rw [← ψ_zero]; exact (ψ_continuous.tendsto _).comp xm_tendsto
  have hval : ∀ m, covCh (Θf ∘ φ) p₀ (ψ (xm m)) = dTh Ffail (xm m) := fun m => by
    rw [Θf, covCh_ThetaG goodG_Ffail (hmem m), hφx]
  have hn : ∀ m, dcov (Θf ∘ φ) (ψ (xm m)) (nN (ψ (xm m))) = 2 := fun m => by
    rw [Θf, dcov_nN goodG_Ffail (hmem m), hφx, dTh_xm]; simp [nvec]
  have hl : ∀ m, dcov (Θf ∘ φ) (ψ (xm m)) (ℓN (ψ (xm m))) = 1 := fun m => by
    rw [Θf, dcov_ℓN goodG_Ffail (hmem m), hφx, dTh_xm]; simp [ellV]
  refine ⟨hp, hΘ, fun x hx => mc_witness_frameHyp goodG_Ffail hx, fun h => ?_, fun h => ?_⟩
  · have h2 := h.comp hseq
    have hc : ((fun x => dcov (Θf ∘ φ) x (ℓN x) / dcov (Θf ∘ φ) x (nN x)) ∘
        fun m => ψ (xm m)) = fun _ => (1:ℝ) / 2 := by
      funext m; simp only [Function.comp_apply, hl, hn]
    rw [hc] at h2
    have := tendsto_nhds_unique h2 tendsto_const_nhds
    norm_num at this
  · have h2 := ((ContinuousLinearMap.apply ℝ ℝ ellV).continuous.tendsto _).comp (h.comp hseq)
    have hc : (ContinuousLinearMap.apply ℝ ℝ ellV ∘ (fun x =>
        (dcov (Θf ∘ φ) x (nN x))⁻¹ • covCh (Θf ∘ φ) p₀ x) ∘ fun m => ψ (xm m)) =
        fun _ => (1:ℝ) / 2 := by
      funext m
      simp only [Function.comp_apply, ContinuousLinearMap.apply_apply, smul_apply, hn, hval,
        dTh_xm, smul_eq_mul]
      simp [ellV]
    rw [hc] at h2
    have := tendsto_nhds_unique h2 tendsto_const_nhds
    simp [gM_apply, ellV] at this

/-- **③ Cone convergence on `Pt` (BUILT).** For the observer of campaign 87's witness:
`KLi(∂J⁻(O τ)) = KLs(∂J⁻(O τ)) = 𝓗⁺ = {U = 0}` (non-empty), via `mc_cone_kuratowski_N`. -/
theorem mc_witness_cones :
    ∃ O_N : ℝ → Pt, minkN.IpastSet (range O_N) = minkN.D JN ∧
      (∀ s t : ℝ, s < t → minkN.Chr (O_N s) (O_N t)) ∧
      KLi (minkN.cone O_N) = minkN.H JN ∧ KLs (minkN.cone O_N) = minkN.H JN ∧
      (∀ x : Pt, x ∈ minkN.H JN ↔ (φ x).1 = 0) ∧ (minkN.H JN).Nonempty := by
  obtain ⟨O_N, hOD, hmono, hJM, -, -, -⟩ := ch_witness_hypotheses goodG_log
  obtain ⟨h1, h2⟩ := MSpacetime.mc_cone_kuratowski_N me_locallyOneChart hOD hmono hJM
  exact ⟨O_N, hOD, hmono, h1, h2, mem_H_N, ⟨ψ (0, 0), (mem_H_N _).2 (by rw [φψ])⟩⟩

end NModel

/-! ## NEW (campaign 89) ②: the witness, `Pt` compactified by `arctan V` inside `Pt`

In null coordinates `(U, V) = φ x`, `ι = ψ ∘ mx_fA ∘ φ` with `mx_fA (U, V) = (U, arctan V)`, so
`ι(Pt) = φ⁻¹{−π/2 < V < π/2}` and `𝒥⁺ = φ⁻¹{(U, π/2) : U < 0}` lies on its frontier. With
`g = −dU dV`, `Dι = diag(1, 1/(1+V²))` in `φ`, so `Ω² = 1/(1+V²)`. -/

namespace NModel
open Model Manifold ContinuousLinearMap

/-- `(U, V) ↦ (U, arctan V)`. -/
noncomputable def mx_fA (y : P) : P := (y.1, Real.arctan y.2)

/-- `mx_DfA = diag(1, 1/(1+V²))`. -/
noncomputable def mx_DfA (y : P) : P →L[ℝ] P :=
  (fst ℝ ℝ ℝ).prod ((1 / (1 + y.2 ^ 2)) • snd ℝ ℝ ℝ)

lemma mx_DfA_apply (y v : P) : mx_DfA y v = (v.1, (1 / (1 + y.2 ^ 2)) * v.2) := by
  simp [mx_DfA]

lemma mx_fA_hasFDerivAt (y : P) : HasFDerivAt mx_fA (mx_DfA y) y :=
  hasFDerivAt_fst.prodMk ((Real.hasDerivAt_arctan y.2).comp_hasFDerivAt y hasFDerivAt_snd)

lemma mx_fA_contDiff : ContDiff ℝ 1 mx_fA :=
  contDiff_fst.prodMk (Real.contDiff_arctan.comp contDiff_snd)

lemma mx_arctan_eq : Real.arctan = Subtype.val ∘ Real.tanOrderIso.symm := rfl

lemma mx_arctan_isOpenEmbedding : IsOpenEmbedding Real.arctan := by
  rw [mx_arctan_eq]
  exact isOpen_Ioo.isOpenEmbedding_subtypeVal.comp
    Real.tanOrderIso.symm.toHomeomorph.isOpenEmbedding

lemma mx_fA_isOpenEmbedding : IsOpenEmbedding mx_fA :=
  IsOpenEmbedding.id.prodMap mx_arctan_isOpenEmbedding

/-- **The witness's embedding** `ι = ψ ∘ mx_fA ∘ φ : Pt → Pt`. -/
noncomputable def mx_ι : Pt → Pt := ψ ∘ mx_fA ∘ φ

lemma mx_φ_eq : φ = fun x => nullH x := funext chart_apply

lemma mx_ψ_eq (y : P) : ψ y = nullH.symm y := by
  rw [Homeomorph.eq_symm_apply]; exact (chart_apply _).symm.trans (φψ y)

lemma mx_φ_ι (x : Pt) : φ (mx_ι x) = mx_fA (φ x) := φψ _

lemma mx_ι_isOpenEmbedding : IsOpenEmbedding mx_ι := by
  have e : mx_ι = nullH.symm ∘ mx_fA ∘ nullH := by
    funext x; show ψ (mx_fA (φ x)) = _; rw [mx_ψ_eq, mx_φ_eq]; rfl
  rw [e]
  exact nullH.symm.isOpenEmbedding.comp (mx_fA_isOpenEmbedding.comp nullH.isOpenEmbedding)

lemma mx_φ_contMDiff : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, P) 1 φ := by
  have h := contMDiffOn_extChartAt (I := 𝓘(ℝ, P)) (n := 1) (x := p₀)
  rw [source_eq] at h
  exact contMDiffOn_univ.1 h

lemma mx_ψ_contMDiff : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, P) 1 ψ := by
  have h := contMDiffOn_extChartAt_symm (I := 𝓘(ℝ, P)) (n := 1) p₀
  rw [target_eq] at h
  exact contMDiffOn_univ.1 h

/-- **`ι` is `C¹` through the `nullH` chart** (the registered expected stop). -/
lemma mx_ι_contMDiff : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, P) 1 mx_ι :=
  mx_ψ_contMDiff.comp ((contMDiff_iff_contDiff.2 mx_fA_contDiff).comp mx_φ_contMDiff)

/-- `Dφ ∘ Dψ = id` at `ψ y`. -/
lemma mx_dchart_dchartInv (y a : P) : dchart p₀ (ψ y) (dchartInv p₀ y a) = a := by
  have h := ld_mfderiv_chart_symm p₀ (src (ψ y)) a
  have e : extChartAt 𝓘(ℝ, P) p₀ (ψ y) = y := φψ y
  rw [e] at h
  exact h

/-- `Dι` read in `φ` at both ends is `mx_DfA`. -/
lemma mx_dι_eq (x : Pt) (v : P) :
    dchart p₀ (mx_ι x) (mx_dι mx_ι x v) =
      mx_DfA (φ x) (dchart p₀ x v) := by
  have hφ : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) φ x :=
    mdifferentiableAt_extChartAt (src x)
  have hf : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) mx_fA (φ x) :=
    mdifferentiableAt_iff_differentiableAt.2 (mx_fA_hasFDerivAt _).differentiableAt
  have hψ : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) ψ (mx_fA (φ x)) :=
    ld_mdifferentiableAt_symm p₀ (by rw [target_eq]; exact mem_univ _)
  have hfφ : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) (mx_fA ∘ φ) x := hf.comp x hφ
  have h1 : mx_dι mx_ι x = (mx_dι (E := P) ψ (mx_fA (φ x))).comp ((mx_dι (E := P) mx_fA (φ x)).comp (mx_dι (E := P) φ x)) := by
    show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (ψ ∘ (mx_fA ∘ φ)) x = _
    rw [mfderiv_comp x hψ hfφ, mfderiv_comp x hf hφ]
    rfl
  have h2 : mx_dι (E := P) mx_fA (φ x) = mx_DfA (φ x) := by
    show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) mx_fA (φ x) = _
    rw [mfderiv_eq_fderiv]; exact (mx_fA_hasFDerivAt _).fderiv
  rw [h1, ContinuousLinearMap.comp_apply, ContinuousLinearMap.comp_apply, h2]
  exact mx_dchart_dchartInv (mx_fA (φ x)) _

/-- The metric of `minkN` read in `φ`: `g_x(v, w) = gM(Dφ v, Dφ w)`. -/
lemma mx_g_eq_gM (x : Pt) (v w : P) :
    minkN.gE x v w = gM (dchart p₀ x v) (dchart p₀ x w) := by
  have h := ld_h_eq_hRep minkN.g p₀ (src x) v w
  rw [hRep_eq] at h
  exact h

/-- `gM(mx_DfA a, mx_DfA b) = gM(a, b)/(1+V²)`. -/
lemma mx_gM_DfA (y a b : P) : gM (mx_DfA y a) (mx_DfA y b) = (1 / (1 + y.2 ^ 2)) * gM a b := by
  rw [mx_DfA_apply, mx_DfA_apply, gM_apply, gM_apply]; ring

/-- The conformal factor `Ω = (1 + V²)^{−1/2}`. -/
noncomputable def mx_Ω (x : Pt) : ℝ := (Real.sqrt (1 + (φ x).2 ^ 2))⁻¹

lemma mx_Ω_pos (x : Pt) : 0 < mx_Ω x := inv_pos.2 (Real.sqrt_pos.2 (by positivity))

lemma mx_Ω_sq (x : Pt) : mx_Ω x ^ 2 = 1 / (1 + (φ x).2 ^ 2) := by
  rw [mx_Ω, inv_pow, Real.sq_sqrt (by positivity), one_div]

lemma mx_dchart_T (x : Pt) : dchart p₀ x (TN x) = ((1, 1) : P) := by
  have h := ld_chartRep_apply_chart minkN.T p₀ (src x)
  rw [chartRep_eq] at h
  exact h.symm

/-- **The conformal extension on `Pt` (BUILT): every field.** -/
noncomputable def mx_witnessExt : ConformalExtension minkN minkN where
  ι := mx_ι
  isOpenEmbedding := mx_ι_isOpenEmbedding
  contMDiff := mx_ι_contMDiff
  Ω := mx_Ω
  Ω_pos := mx_Ω_pos
  conformal := fun x v w => by
    rw [mx_g_eq_gM, mx_g_eq_gM, mx_dι_eq, mx_dι_eq, mx_gM_DfA, mx_Ω_sq]
  timeOrient := fun x _ => by
    rw [← MSpacetime.futTimelike_chart ch_oneChart (src (mx_ι x)), ch_chartSp_eq]
    show mink.FutTimelike _ (dchart p₀ (mx_ι x) (mx_dι mx_ι x (TN x)))
    rw [mx_dι_eq, mx_dchart_T, futTimelike_iff, mx_DfA_apply]
    exact ⟨one_pos, by simp only [mul_one]; positivity⟩
  maps_M := subset_univ _

/-- `𝒥⁺` in null coordinates: `{(U, π/2) : U < 0}`. -/
def mx_JA : Set P := {p : P | p.1 < 0 ∧ p.2 = Real.pi / 2}

/-- `𝒥⁺ = φ⁻¹{(U, π/2) : U < 0}` on `Pt`. -/
noncomputable def mx_scri : Set Pt := ψ '' mx_JA

/-- **`I⁻(𝒥⁺)` in null coordinates** (`chr_lt`, `tstep_of_lt`): `{U < 0, V < π/2}`. -/
lemma mx_mem_mink_D_JA (p : P) : p ∈ mink.D mx_JA ↔ p.1 < 0 ∧ p.2 < Real.pi / 2 := by
  show p ∈ ⋃ a ∈ mx_JA, mink.Ipast a ↔ _
  rw [mem_iUnion₂]
  constructor
  · rintro ⟨a, ⟨ha1, ha2⟩, hpa⟩
    have h := chr_lt hpa
    exact ⟨h.1.trans ha1, ha2 ▸ h.2⟩
  · rintro ⟨h1, h2⟩
    refine ⟨(p.1 / 2, Real.pi / 2), ⟨by simp only; linarith, rfl⟩,
      Relation.TransGen.single (tstep_of_lt (by simp only; linarith) h2)⟩

lemma mx_mem_Ipast_scri (x : Pt) :
    x ∈ minkN.IpastSet mx_scri ↔ (φ x).1 < 0 ∧ (φ x).2 < Real.pi / 2 :=
  (mem_D_N mx_JA x).trans (mx_mem_mink_D_JA _)

/-- **`hI` on the witness (BUILT):** `ι⁻¹ Ĩ⁻(𝒥⁺) = {U < 0} = D`. -/
lemma mx_preimage_Ipast_scri : mx_ι ⁻¹' minkN.IpastSet mx_scri = minkN.D JN := by
  ext x
  rw [mem_preimage, mx_mem_Ipast_scri, mx_φ_ι, mem_D_JN_iff]
  exact ⟨fun h => h.1, fun h => ⟨h, Real.arctan_lt_pi_div_two _⟩⟩

/-- **`𝒥⁺ ⊆ ∂ι(Pt)`** (BUILT): `ψ(U, π/2)` is not in `ι(Pt)` (`arctan < π/2`) but is the limit of
`ψ(U, s) = ι(ψ(U, tan s))` as `s → π/2⁻`. -/
lemma mx_scri_subset_frontier : mx_scri ⊆ frontier (range mx_ι) := by
  rintro _ ⟨p, ⟨hp1, hp2⟩, rfl⟩
  have hnot : ψ p ∉ range mx_ι := by
    rintro ⟨w, hw⟩
    have h := congrArg Prod.snd (congrArg φ hw)
    rw [mx_φ_ι, show φ (ψ p) = p from φψ p] at h
    have := Real.arctan_lt_pi_div_two (φ w).2
    change Real.arctan (φ w).2 = p.2 at h
    linarith
  have hpi := Real.pi_pos
  have hcl : ψ p ∈ closure (range mx_ι) := by
    have ht : Tendsto (fun s : ℝ => ψ (p.1, s)) (𝓝[<] (Real.pi / 2)) (𝓝 (ψ p)) := by
      have hc : Continuous fun s : ℝ => ψ (p.1, s) :=
        ψ_continuous.comp (continuous_const.prodMk continuous_id)
      have h0 : ψ p = (fun s : ℝ => ψ (p.1, s)) (Real.pi / 2) := by
        simp only; rw [← hp2]
      rw [h0]; exact (hc.tendsto _).mono_left nhdsWithin_le_nhds
    refine mem_closure_of_tendsto ht ?_
    filter_upwards [Ioo_mem_nhdsLT (show -(Real.pi / 2) < Real.pi / 2 by linarith)] with s hs
    refine ⟨ψ (p.1, Real.tan s), ?_⟩
    show ψ (mx_fA (φ (ψ (p.1, Real.tan s)))) = _
    rw [show φ (ψ (p.1, Real.tan s)) = (p.1, Real.tan s) from φψ _]
    show ψ (p.1, Real.arctan (Real.tan s)) = _
    rw [Real.arctan_tan hs.1 hs.2]
  exact ⟨hcl, fun h => hnot (interior_subset h)⟩

/-- **② The witness (BUILT).** On `Pt`, with `ι = ψ ∘ (id × arctan) ∘ φ`, `Ω² = 1/(1+V²)` and
`𝒥⁺ = φ⁻¹{(U, π/2) : U < 0}`: `ι` is a conformal extension (`mx_witnessExt`), `𝒥⁺ ⊆ ∂ι(Pt)`,
`𝒥⁺ ⊆ M̃`, `Ĩ⁻(𝒥⁺) = φ⁻¹{U < 0, V < π/2}`, `hI : I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺)`, and by
`mx_H_eq_boundary`: `{U = 0} = 𝓗⁺ = ∂J⁻(𝒥⁺)`, a non-empty set. -/
theorem mx_witness_boundary :
    ∃ O_N : ℝ → Pt, minkN.IpastSet (range O_N) = minkN.D JN ∧
      (∀ s t : ℝ, s < t → minkN.Chr (O_N s) (O_N t)) ∧
      mx_witnessExt.ι = ψ ∘ mx_fA ∘ φ ∧ (∀ x, mx_witnessExt.Ω x ^ 2 = 1 / (1 + (φ x).2 ^ 2)) ∧
      mx_scri ⊆ frontier (range mx_witnessExt.ι) ∧ mx_scri ⊆ minkN.M ∧ mx_scri.Nonempty ∧
      (∀ x, x ∈ minkN.IpastSet mx_scri ↔ (φ x).1 < 0 ∧ (φ x).2 < Real.pi / 2) ∧
      minkN.IpastSet (range O_N) = mx_witnessExt.ι ⁻¹' minkN.IpastSet mx_scri ∧
      minkN.H (range O_N) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      minkN.H JN = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      (∀ x, x ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ↔ (φ x).1 = 0) ∧
      (frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri)).Nonempty := by
  obtain ⟨O_N, hOD, hmono, hJM, -, -, -⟩ := ch_witness_hypotheses goodG_log
  have hI : minkN.IpastSet (range O_N) = mx_witnessExt.ι ⁻¹' minkN.IpastSet mx_scri := by
    rw [hOD]; exact mx_preimage_Ipast_scri.symm
  have hB := MSpacetime.mx_H_eq_boundary me_locallyOneChart me_locallyOneChart mx_witnessExt
    (subset_univ _) hOD hmono hJM hI
  have hmem : ∀ x, x ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ↔ (φ x).1 = 0 :=
    fun x => by rw [← hB.2]; exact mem_H_N x
  refine ⟨O_N, hOD, hmono, rfl, mx_Ω_sq, mx_scri_subset_frontier, subset_univ _,
    ⟨ψ (-1, Real.pi / 2), mem_image_of_mem ψ (show ((-1 : ℝ), Real.pi / 2) ∈ mx_JA from ⟨by norm_num, rfl⟩)⟩, mx_mem_Ipast_scri, hI, hB.1, hB.2, hmem,
    ⟨ψ (0, 0), (hmem _).2 (by rw [show φ (ψ (0, 0)) = (0, 0) from φψ _])⟩⟩

/-- **③ The headline witnessed end to end on `Pt` (BUILT), for `Θ₀ ∘ φ`.** Every hypothesis of
`mx_prop_causal_alignment` is discharged, and its conclusion read off: `𝓗⁺ = ∂J⁻(𝒥⁺) = {U = 0}`
(non-empty), properness, `KLi = KLs = ∂J⁻(𝒥⁺)` for slices and for past cones, and the tangency
clause, whose hypotheses are discharged at the horizon point `p₀` with the frame `(ℓN, nN)` along
`𝓝[D] p₀`, giving the limit `−g_{p₀}(ℓ, ·)`. -/
theorem mx_witness_headline :
    ∃ O_N : ℝ → Pt,
      (∀ x, x ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ↔ (φ x).1 = 0) ∧
      (frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri)).Nonempty ∧
      minkN.H JN = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      minkN.SublevelProper JN (Θ₀ ∘ φ) ∧
      KLi (minkN.slice JN (Θ₀ ∘ φ)) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      KLs (minkN.slice JN (Θ₀ ∘ φ)) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      KLi (minkN.cone O_N) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      KLs (minkN.cone O_N) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      p₀ ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x) (𝓝[minkN.D JN] p₀)
        (𝓝 (-(minkN.gE p₀ ellV))) := by
  obtain ⟨hL, -, O_N, hOD, hmono, hJM, hHM, hΘ, hadapt⟩ := mh_witness_hypotheses goodG_log
  obtain ⟨_, -, -, -, -, -, -, -, -, -, -, -, hmem, hne⟩ := mx_witness_boundary
  -- `mx_witness_boundary`'s observer is existential: rebuild `hI` for this one through `hOD`.
  have hI' : minkN.IpastSet (range O_N) = mx_witnessExt.ι ⁻¹' minkN.IpastSet mx_scri := by
    rw [hOD]; exact mx_preimage_Ipast_scri.symm
  have hHM' : frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ⊆ minkN.M := subset_univ _
  obtain ⟨h0, h1, h2, h3, h4, h5, h6⟩ := MSpacetime.mx_prop_causal_alignment hL hL mx_witnessExt
    (subset_univ _) hOD hmono hJM hI' hHM' hΘ hadapt
  have hp : p₀ ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) :=
    (hmem p₀).2 (by rw [φ_p₀])
  obtain ⟨-, -, hF, hr, -, -⟩ := mc_witness_tangency_holds p₀ (h0 ▸ hp)
  have ht := h6 p₀ hp ℓN nN (𝓝[minkN.D JN] p₀) ‖nvec‖ ellV nhdsWithin_le_nhds hF
    (Eventually.of_forall fun x => by rw [A_nN])
    (tendsto_const_nhds.congr fun x => (A_ℓN x).symm) hr
  exact ⟨O_N, hmem, hne, h0, h1, h2, h3, h4, h5, hp, ht⟩

end NModel

/-! ## NEW (campaign 91) ①: the witness on `Pt` -/

namespace NModel
open Model Manifold

/-- `Pt = ℝ × ℝ` is connected. -/
instance cd_preconnectedSpace : PreconnectedSpace Pt :=
  inferInstanceAs (PreconnectedSpace (ℝ × ℝ))

/-- In a preconnected space, a set that is neither empty nor everything has a non-empty frontier. -/
theorem cd_frontier_nonempty {X : Type*} [TopologicalSpace X] [PreconnectedSpace X] {s : Set X}
    {a b : X} (ha : a ∈ s) (hb : b ∉ s) : (frontier s).Nonempty := by
  rw [nonempty_iff_ne_empty]
  intro h
  rcases frontier_eq_empty_iff.1 h with h' | h'
  · rw [h'] at ha; exact ha
  · rw [h'] at hb; exact hb (mem_univ b)

/-- **① witnessed on `Pt` (BUILT).** With `mx_witness_headline`'s data (`Θ₀ ∘ φ`, the conformal
extension `ι = ψ ∘ (id × arctan) ∘ φ`): the eighth conjunct of `cd_prop_causal_alignment`,
`∂J⁻(O τ) ∩ ∂J⁻(𝒥⁺) = ∅` for every `τ`, i.e. no cone point has `U = 0`; and every cone is
non-empty (it separates `O τ ∈ J⁻(O τ)` from `p₀ ∉ J⁻(O τ)`), so the disjointness is not vacuous. -/
theorem cd_witness :
    ∃ O_N : ℝ → Pt,
      (∀ x, x ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ↔ (φ x).1 = 0) ∧
      (frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri)).Nonempty ∧
      (∀ τ, minkN.cone O_N τ ∩ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) = ∅) ∧
      (∀ τ, ∀ x ∈ minkN.cone O_N τ, (φ x).1 ≠ 0) ∧
      (∀ τ, (minkN.cone O_N τ).Nonempty) := by
  obtain ⟨hL, -, O_N, hOD, hmono, hJM, hHM, hΘ, hadapt⟩ := mh_witness_hypotheses goodG_log
  obtain ⟨_, -, -, -, -, -, -, -, -, -, -, -, hmem, hne⟩ := mx_witness_boundary
  have hI' : minkN.IpastSet (range O_N) = mx_witnessExt.ι ⁻¹' minkN.IpastSet mx_scri := by
    rw [hOD]; exact mx_preimage_Ipast_scri.symm
  have hHM' : frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ⊆ minkN.M := subset_univ _
  obtain ⟨h0, -, -, -, -, -, -, h7⟩ := MSpacetime.cd_prop_causal_alignment hL hL mx_witnessExt
    (subset_univ _) hOD hmono hJM hI' hHM' hΘ hadapt
  have hp₀H : p₀ ∈ minkN.H JN := h0 ▸ (hmem p₀).2 (by rw [φ_p₀])
  have hp₀D := minkN.mh_not_mem_D_of_H hL hp₀H
  refine ⟨O_N, hmem, hne, h7, fun τ x hx hx0 => ?_, fun τ => ?_⟩
  · have := (h7 τ).subset ⟨hx, (hmem x).2 hx0⟩
    exact this
  · refine cd_frontier_nonempty (a := O_N τ) (b := p₀) Relation.ReflTransGen.refl ?_
    intro hp
    apply hp₀D
    rw [← hOD]
    exact mem_iUnion₂.2 ⟨_, mem_range_self (τ + 1),
      minkN.mk_pushup hL hp (hmono τ (τ + 1) (by linarith))⟩

end NModel

/-! ## NEW (campaign 93 ②): `cor:densities` witnessed on `Pt` -/

namespace NModel
open Model Manifold

/-- **`ι⁻¹ J̃⁻(𝒥⁺) = {U < 0}` on the witness** (`cau_le` through the global chart; `⊇` from
`D ⊆ J⁻`). -/
lemma dn_preimage_Jpast_scri :
    mx_ι ⁻¹' minkN.JpastSet mx_scri = {x | (φ x).1 < 0} := by
  ext x
  simp only [mem_preimage, mem_ofPred_eq]
  constructor
  · intro h
    obtain ⟨p, ⟨a, ⟨ha1, -⟩, rfl⟩, hc⟩ := mem_iUnion₂.1 h
    have hc' := (MSpacetime.ch_cau_iff ch_oneChart (src _) (src _)).1 hc
    rw [ch_chartSp_eq] at hc'
    have h1 := (cau_le hc').1
    have e1 : extChartAt 𝓘(ℝ, P) p₀ (mx_ι x) = mx_fA (φ x) := mx_φ_ι x
    rw [e1, φψ] at h1
    change (φ x).1 ≤ a.1 at h1
    linarith
  · intro h
    have hD : x ∈ minkN.D JN := (mem_D_JN_iff x).2 h
    rw [← mx_preimage_Ipast_scri] at hD
    exact minkN.D_subset_JpastSet mx_scri hD

/-- **`cor:densities` 7a–7c witnessed on `Pt` (BUILT)**, with `mx_witnessExt` and `Θ₀ ∘ φ`: the
black-hole region `M ∖ ι⁻¹ J̃⁻(𝒥⁺)` is computed to be `{U ≥ 0}`; it is non-empty (`p₀`), every
slice is non-empty (`O_N τ`), and the conclusions of `dn_cor_densities` hold, so the disjointness
is not vacuous. -/
theorem dn_witness :
    (∀ x, x ∈ minkN.M \ mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri ↔ 0 ≤ (φ x).1) ∧
    (minkN.M \ mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri).Nonempty ∧
    (∀ τ, (minkN.slice JN (Θ₀ ∘ φ) τ).Nonempty) ∧
    (∀ τ, (minkN.M \ mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∩
      minkN.slice JN (Θ₀ ∘ φ) τ = ∅) ∧
    (∀ τ, minkN.slice JN (Θ₀ ∘ φ) τ ∩ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) = ∅) ∧
    (∀ τ, minkN.slice JN (Θ₀ ∘ φ) τ ∩ minkN.H JN = ∅) ∧
    (∀ B ⊆ minkN.M \ mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri, ∀ τ,
      B ∩ minkN.slice JN (Θ₀ ∘ φ) τ = ∅) := by
  obtain ⟨hL, -, O_N, hOD, hmono, -, -, -, hadapt⟩ := mh_witness_hypotheses goodG_log
  have hI' : minkN.IpastSet (range O_N) = mx_witnessExt.ι ⁻¹' minkN.IpastSet mx_scri := by
    rw [hOD]; exact mx_preimage_Ipast_scri.symm
  obtain ⟨h7a, h7b, h7b', h7c⟩ := MSpacetime.dn_cor_densities hL hL mx_witnessExt hOD hI'
  have hBH : ∀ x, x ∈ minkN.M \ mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri ↔ 0 ≤ (φ x).1 := by
    intro x
    change x ∈ univ \ mx_ι ⁻¹' minkN.JpastSet mx_scri ↔ _
    rw [dn_preimage_Jpast_scri]
    simp only [Set.mem_sdiff, mem_univ, mem_ofPred_eq, true_and, not_lt]
  refine ⟨hBH, ⟨p₀, (hBH p₀).2 (by rw [φ_p₀])⟩, fun τ => ⟨O_N τ,
    MSpacetime.mh_observer_mem_D hOD hmono τ, (hadapt τ).trans (add_zero τ)⟩,
    fun τ => h7a _ τ, fun τ => h7b _ τ, fun τ => h7b' _ τ, fun B hB τ => h7c B hB _ τ⟩

end NModel

/-! ## Copied (campaign 94, `AlongConnection.lean`): the `ac_` section

`AlongConnection.lean`'s `MSpacetime`, `gE` and `vel` are textually the kit's (the structure body and
both definitions are identical; only the docstring of the structure is shorter there), so the kit's
single copy above is kept and the `ac_` material is stated over it. `AdaptedSplitting` and every
`ac_` lemma are copied unchanged. The model part is put in the namespace `ACModel`, since the kit's
`Model` already has `P`, `gM`, `gM_apply` (kept: textually the same) and a `mink` of a different type
(the kit's is a vector-space `Spacetime P`; `ac_`'s is the `MSpacetime P P`, kept as `ACModel.mink`). -/

noncomputable section
section ACManifold
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

open MSpacetime

/-! ### The adapted splitting along `γ` (ruling 2) -/

/-- **The splitting adapted to (b)'s foliation, along `γ` on `[0, 1]`**: a spatial bilinear form `h s`,
a lapse `n s ≥ 0` (allowed to vanish), and a temporal one-form `dt s`, with
`g_{γ s} = h s − (n s)² dt s ⊗ dt s` and `h s (γ′ s, γ′ s) ≥ 0`. -/
structure AdaptedSplitting (S : MSpacetime E N) (γ : ℝ → N) where
  h : ℝ → E →L[ℝ] E →L[ℝ] ℝ
  n : ℝ → ℝ
  dt : ℝ → E →L[ℝ] ℝ
  n_nonneg : ∀ s ∈ Icc (0:ℝ) 1, 0 ≤ n s
  split : ∀ s ∈ Icc (0:ℝ) 1, S.gE (γ s) = h s - (n s) ^ 2 • (dt s).smulRight (dt s)
  h_nonneg : ∀ s ∈ Icc (0:ℝ) 1, 0 ≤ h s (vel γ s) (vel γ s)

namespace AdaptedSplitting
variable {S : MSpacetime E N} {γ : ℝ → N} (σ : AdaptedSplitting S γ)

/-- `Δx := ∫₀¹ √(h(γ′, γ′))`. -/
def Δx : ℝ := ∫ s in (0:ℝ)..1, √(σ.h s (vel γ s) (vel γ s))

/-- `Δτ := ∫₀¹ n |dt(γ′)|`. -/
def Δτ : ℝ := ∫ s in (0:ℝ)..1, σ.n s * |σ.dt s (vel γ s)|

/-- The line element along `γ`: `g(γ′, γ′) = h(γ′, γ′) − n² dt(γ′)²`. -/
lemma g_vel {s : ℝ} (hs : s ∈ Icc (0:ℝ) 1) :
    S.gE (γ s) (vel γ s) (vel γ s) =
      σ.h s (vel γ s) (vel γ s) - (σ.n s * σ.dt s (vel γ s)) ^ 2 := by
  rw [σ.split s hs]
  simp only [sub_apply, smul_apply,
    ContinuousLinearMap.smulRight_apply, smul_eq_mul]
  ring

end AdaptedSplitting

/-- A function continuous and non-negative on `[0, 1]` with zero integral vanishes on `[0, 1]`. -/
lemma ac_eq_zero_of_integral_eq_zero {f : ℝ → ℝ} (hc : ContinuousOn f (Icc 0 1))
    (hnn : ∀ s ∈ Icc (0:ℝ) 1, 0 ≤ f s) (h0 : ∫ s in (0:ℝ)..1, f s = 0) :
    ∀ s ∈ Icc (0:ℝ) 1, f s = 0 := by
  intro s hs
  by_contra hne
  have hpos : 0 < ∫ s in (0:ℝ)..1, f s :=
    intervalIntegral.integral_pos zero_lt_one hc (fun x hx => hnn x (Ioc_subset_Icc_self hx))
      ⟨s, hs, lt_of_le_of_ne (hnn s hs) (Ne.symm hne)⟩
  linarith

/-- **`thm:metric-singularity`, along-the-connection form, on ruling 2.** (a) `g(γ′, γ′) = 0` on `[0, 1]`,
(b) `Δx = 0`, and continuity of `s ↦ h s (γ′ s) (γ′ s)` on `[0, 1]` give `Δτ = 0`, and
`n s · dt s (γ′ s) = 0` on `[0, 1]` (and `h(γ′, γ′) = 0` there, which is (b) pointwise). -/
theorem ac_metric_singularity_along (S : MSpacetime E N) {γ : ℝ → N} (σ : AdaptedSplitting S γ)
    (ha : ∀ s ∈ Icc (0:ℝ) 1, S.gE (γ s) (vel γ s) (vel γ s) = 0)
    (hb : σ.Δx = 0)
    (hcont : ContinuousOn (fun s => σ.h s (vel γ s) (vel γ s)) (Icc 0 1)) :
    σ.Δτ = 0 ∧ (∀ s ∈ Icc (0:ℝ) 1, σ.n s * σ.dt s (vel γ s) = 0) ∧
      (∀ s ∈ Icc (0:ℝ) 1, σ.h s (vel γ s) (vel γ s) = 0) := by
  have hsq : ∀ s ∈ Icc (0:ℝ) 1, √(σ.h s (vel γ s) (vel γ s)) = 0 :=
    ac_eq_zero_of_integral_eq_zero (Real.continuous_sqrt.comp_continuousOn hcont)
      (fun s _ => Real.sqrt_nonneg _) hb
  have hh : ∀ s ∈ Icc (0:ℝ) 1, σ.h s (vel γ s) (vel γ s) = 0 := fun s hs =>
    le_antisymm (Real.sqrt_eq_zero'.mp (hsq s hs)) (σ.h_nonneg s hs)
  have hnd : ∀ s ∈ Icc (0:ℝ) 1, σ.n s * σ.dt s (vel γ s) = 0 := by
    intro s hs
    have h1 := σ.g_vel hs
    rw [ha s hs, hh s hs] at h1
    have : (σ.n s * σ.dt s (vel γ s)) ^ 2 = 0 := by linarith
    exact pow_eq_zero_iff two_ne_zero |>.mp this
  refine ⟨?_, hnd, hh⟩
  unfold AdaptedSplitting.Δτ
  have hz : ∫ s in (0:ℝ)..1, σ.n s * |σ.dt s (vel γ s)| = ∫ _ in (0:ℝ)..1, (0:ℝ) := by
    refine intervalIntegral.integral_congr fun s hs => ?_
    rw [uIcc_of_le zero_le_one] at hs
    show σ.n s * |σ.dt s (vel γ s)| = 0
    rcases mul_eq_zero.mp (hnd s hs) with h | h <;> simp [h]
  rw [hz]; simp

/-! ### Vanishing velocity on `[0, 1]` forces a constant curve (on the manifold) -/


/-- Near a parameter `t`, in the chart at `γ t`, a curve with vanishing `mfderiv` velocity on `[0, 1]`
is constant on `[0, 1]`. -/
lemma ac_locally_const_of_vel_zero {γ : ℝ → N}
    (hd : ∀ t ∈ Icc (0:ℝ) 1, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t)
    (h0 : ∀ t ∈ Icc (0:ℝ) 1, vel (E := E) γ t = 0) {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) :
    ∃ ε > 0, ∀ u ∈ Icc (0:ℝ) 1, dist u t < ε → γ u = γ t := by
  set φ := extChartAt 𝓘(ℝ, E) (γ t)
  have hev : ∀ᶠ u in 𝓝 t, γ u ∈ (chartAt E (γ t)).source :=
    (hd t ht).continuousAt.preimage_mem_nhds
      ((chartAt E (γ t)).open_source.mem_nhds (mem_chart_source E (γ t)))
  obtain ⟨ε, hε, hball⟩ := Metric.eventually_nhds_iff.mp hev
  refine ⟨ε, hε, fun u hu hut => ?_⟩
  set s := Icc (0:ℝ) 1 ∩ ball t ε
  have hsc : Convex ℝ s := (convex_Icc 0 1).inter (convex_ball t ε)
  have hderiv : ∀ x ∈ s, HasDerivWithinAt (φ ∘ γ) 0 s x := by
    intro x hx
    have hxs : γ x ∈ (chartAt E (γ t)).source := hball hx.2
    have hφ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) φ (γ x) :=
      mdifferentiableAt_extChartAt (I := 𝓘(ℝ, E)) hxs
    have hcomp : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (φ ∘ γ) x := hφ.comp x (hd x hx.1)
    have hdiff : DifferentiableAt ℝ (φ ∘ γ) x := mdifferentiableAt_iff_differentiableAt.mp hcomp
    have hfd : fderiv ℝ (φ ∘ γ) x = 0 := by
      refine ContinuousLinearMap.ext_ring ?_
      have e : fderiv ℝ (φ ∘ γ) x 1 = mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (φ ∘ γ) x 1 := by
        rw [mfderiv_eq_fderiv]; rfl
      rw [e, mfderiv_comp x hφ (hd x hx.1), ContinuousLinearMap.comp_apply]
      have : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ x 1 = 0 := h0 x hx.1
      rw [this, map_zero]; rfl
    have := hdiff.hasFDerivAt
    rw [hfd] at this
    simpa using this.hasDerivAt.hasDerivWithinAt
  have hts : t ∈ s := ⟨ht, mem_ball_self hε⟩
  have hus : u ∈ s := ⟨hu, hut⟩
  have hle := hsc.norm_image_sub_le_of_norm_hasDerivWithin_le (C := 0) hderiv (fun _ _ => by simp) hts hus
  have heq : φ (γ u) = φ (γ t) := by
    have : ‖(φ ∘ γ) u - (φ ∘ γ) t‖ = 0 := le_antisymm (by simpa using hle) (norm_nonneg _)
    simpa [sub_eq_zero] using this
  exact (extChartAt 𝓘(ℝ, E) (γ t)).injOn (by rw [extChartAt_source]; exact hball hut)
    (by rw [extChartAt_source]; exact mem_chart_source E (γ t)) heq

/-- **A curve on a manifold with vanishing `mfderiv` velocity on `[0, 1]` is constant on `[0, 1]`.** -/
theorem ac_const_of_vel_zero {γ : ℝ → N}
    (hd : ∀ t ∈ Icc (0:ℝ) 1, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t)
    (h0 : ∀ t ∈ Icc (0:ℝ) 1, vel (E := E) γ t = 0) : ∀ t ∈ Icc (0:ℝ) 1, γ t = γ 0 := by
  have : PreconnectedSpace (Icc (0:ℝ) 1) :=
    Subtype.preconnectedSpace isPreconnected_Icc
  let f : Icc (0:ℝ) 1 → N := fun u => γ u
  have hf : IsLocallyConstant f := by
    rw [IsLocallyConstant.iff_eventually_eq]
    rintro ⟨t, ht⟩
    obtain ⟨ε, hε, h⟩ := ac_locally_const_of_vel_zero hd h0 ht
    rw [Metric.eventually_nhds_iff]
    exact ⟨ε, hε, fun {y} hy => h y.1 y.2 hy⟩
  intro t ht
  exact hf.apply_eq_of_preconnectedSpace ⟨t, ht⟩ ⟨0, left_mem_Icc.mpr zero_le_one⟩

/-- **The companion (`N > 0`).** If the lapse is positive on `[0, 1]` and each `h s` is positive definite
on `ker dt s`, then (a) and (b) (with continuity of the `h`-integrand) force `γ′ = 0` on `[0, 1]`; for `γ`
manifold-differentiable on `[0, 1]`, `γ` is constant there and `γ 1 = γ 0`, so `p = q`. -/
theorem ac_lapse_pos_forces_point (S : MSpacetime E N) {γ : ℝ → N} (σ : AdaptedSplitting S γ)
    (ha : ∀ s ∈ Icc (0:ℝ) 1, S.gE (γ s) (vel γ s) (vel γ s) = 0)
    (hb : σ.Δx = 0)
    (hcont : ContinuousOn (fun s => σ.h s (vel γ s) (vel γ s)) (Icc 0 1))
    (hn : ∀ s ∈ Icc (0:ℝ) 1, 0 < σ.n s)
    (hpd : ∀ s ∈ Icc (0:ℝ) 1, ∀ v : E, v ≠ 0 → σ.dt s v = 0 → 0 < σ.h s v v) :
    (∀ s ∈ Icc (0:ℝ) 1, vel (E := E) γ s = 0) ∧
      ((∀ t ∈ Icc (0:ℝ) 1, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t) → γ 1 = γ 0) := by
  obtain ⟨-, hnd, hh⟩ := ac_metric_singularity_along S σ ha hb hcont
  have hv : ∀ s ∈ Icc (0:ℝ) 1, vel (E := E) γ s = 0 := by
    intro s hs
    have hdt : σ.dt s (vel γ s) = 0 :=
      (mul_eq_zero.mp (hnd s hs)).resolve_left (hn s hs).ne'
    by_contra hne
    have := hpd s hs _ hne hdt
    rw [hh s hs] at this
    exact lt_irrefl _ this
  exact ⟨hv, fun hd => ac_const_of_vel_zero hd hv 1 (right_mem_Icc.mpr zero_le_one)⟩

end ACManifold

/-! ### The Rindler-horizon witness of `ac_` (on the model space `P`), copied -/

namespace ACModel
open ContinuousLinearMap MSpacetime Manifold
open Model (P gM gM_apply)

set_option synthInstance.maxHeartbeats 400000

/-- 2D Minkowski space on the model space `P`, `M = P`, `g = gM`, `T = ∂_t = (1, 1)`. -/
def mink : MSpacetime P P where
  M := univ
  isOpen_M := isOpen_univ
  g := fun _ => gM
  symm := fun _ v w => (by rw [gM_apply, gM_apply]; ring : gM v w = gM w v)
  T := fun _ => ((1 : ℝ), (1 : ℝ))
  T_timelike := fun _ _ => by
    show gM ((1 : ℝ), (1 : ℝ)) ((1 : ℝ), (1 : ℝ)) < 0
    rw [gM_apply]; norm_num
  pos_on_perp := fun _ _ v h hv => by
    change gM v ((1 : ℝ), (1 : ℝ)) = 0 at h
    show 0 < gM v v
    rw [gM_apply] at h ⊢
    have h2 : v.2 = -v.1 := by simp at h; linarith
    have h1 : v.1 ≠ 0 := by
      intro h1; apply hv; ext
      · exact h1
      · rw [h2, h1]; simp
    rw [h2]; nlinarith [sq_pos_of_ne_zero h1]

lemma mink_gE (x : P) : mink.gE x = gM := rfl

/-- On the model space, the `mfderiv` velocity is the ordinary derivative. -/
lemma vel_eq_of_hasDerivAt {γ : ℝ → P} {t : ℝ} {v : P} (h : HasDerivAt γ v t) : vel γ t = v := by
  unfold vel
  rw [mfderiv_eq_fderiv]
  show fderiv ℝ γ t 1 = v
  rw [h.hasFDerivAt.fderiv]
  simp

/-- The boost field `χ = V∂_V − U∂_U`. -/
def χ (x : P) : P := (-x.1, x.2)

/-- `g(χ, χ) = UV`. -/
lemma g_χ_χ (x : P) : gM (χ x) (χ x) = x.1 * x.2 := by
  rw [gM_apply]; simp [χ]; ring

/-- The boost flow `Φ_t(U, V) = (e^{−t}U, e^{t}V)`, linear in `x`. -/
def Φ (t : ℝ) (x : P) : P := (Real.exp (-t) * x.1, Real.exp t * x.2)

/-- `χ` is the generator of `Φ`: `d/dt Φ_t x |_{t=0} = χ x`. -/
theorem ac_boost_generator (x : P) : HasDerivAt (fun t => Φ t x) (χ x) 0 := by
  have h1 : HasDerivAt (fun t => Real.exp (-t) * x.1) (-x.1) 0 := by
    have := ((Real.hasDerivAt_exp (-0)).comp 0 (hasDerivAt_neg 0)).mul_const x.1
    simpa using this
  have h2 : HasDerivAt (fun t => Real.exp t * x.2) x.2 0 := by
    simpa using (Real.hasDerivAt_exp 0).mul_const x.2
  exact h1.prodMk h2

/-- `χ` is Killing: its (linear, so `DΦ_t = Φ_t`) flow preserves `g`. -/
theorem ac_boost_isometry (t : ℝ) (a b : P) : gM (Φ t a) (Φ t b) = gM a b := by
  rw [gM_apply, gM_apply]
  simp only [Φ]
  have he : Real.exp (-t) * Real.exp t = 1 := by rw [← Real.exp_add]; simp
  linear_combination (-(a.1 * b.2 + a.2 * b.1) / 2) * he

/-- The Rindler horizon generator `γ s = (0, eˢ)` on `U = 0`. -/
def γ (s : ℝ) : P := (0, Real.exp s)

lemma hasDerivAt_γ (s : ℝ) : HasDerivAt γ (0, Real.exp s) s :=
  (hasDerivAt_const s (0:ℝ)).prodMk (Real.hasDerivAt_exp s)

lemma vel_γ (s : ℝ) : vel (E := P) γ s = (0, Real.exp s) := vel_eq_of_hasDerivAt (hasDerivAt_γ s)

/-- The witness splitting: `h = g`, `n = √(max 0 (−g(χ, χ)))`, `dt = dV/V = dλ` with `λ = log V`. -/
def σ : AdaptedSplitting mink γ where
  h := fun _ => gM
  n := fun s => √(max 0 (-(gM (χ (γ s)) (χ (γ s)))))
  dt := fun s => (1 / Real.exp s) • snd ℝ ℝ ℝ
  n_nonneg := fun _ _ => Real.sqrt_nonneg _
  split := fun s _ => by
    have : √(max 0 (-(gM (χ (γ s)) (χ (γ s))))) = 0 := by
      rw [g_χ_χ]; simp [γ]
    refine ContinuousLinearMap.ext fun a => ContinuousLinearMap.ext fun b => ?_
    show gM a b = _
    simp [this]
  h_nonneg := fun s _ => by rw [vel_γ, gM_apply]; simp

lemma σ_n (s : ℝ) : σ.n s = 0 := by
  show √(max 0 (-(gM (χ (γ s)) (χ (γ s))))) = 0
  rw [g_χ_χ]; simp [γ]

lemma σ_dt (s : ℝ) : σ.dt s (vel γ s) = 1 := by
  show ((1 / Real.exp s) • snd ℝ ℝ ℝ) (vel γ s) = 1
  rw [vel_γ]; simp [Real.exp_ne_zero]

/-- **The Rindler-horizon witness.** On 2D Minkowski `g = −dU dV`, along `γ s = (0, eˢ)`: `χ(γ s) = γ′ s`,
null and non-zero, with `g(χ, χ) = UV` everywhere; the adapted splitting `σ` has lapse `0` on `γ`,
`dt(γ′) = 1` (so `∫₀¹ dt(γ′) = 1`, `λ = log V` separates the endpoints); (a) and (b) hold, the hypotheses of
`ac_metric_singularity_along` hold and its conclusion `Δτ = 0` holds; and `p = γ 0 ≠ q = γ 1`. -/
theorem ac_witness :
    (∀ x : P, gM (χ x) (χ x) = x.1 * x.2) ∧
    (∀ s, χ (γ s) = vel (E := P) γ s) ∧
    (∀ s, mink.gE (γ s) (vel γ s) (vel γ s) = 0 ∧ vel (E := P) γ s ≠ 0) ∧
    (∀ s, σ.n s = 0) ∧
    (∫ s in (0:ℝ)..1, σ.dt s (vel γ s)) = 1 ∧
    (∀ s ∈ Icc (0:ℝ) 1, mink.gE (γ s) (vel γ s) (vel γ s) = 0) ∧
    σ.Δx = 0 ∧
    ContinuousOn (fun s => σ.h s (vel γ s) (vel γ s)) (Icc 0 1) ∧
    σ.Δτ = 0 ∧
    γ 0 = ((0:ℝ), (1:ℝ)) ∧ γ 1 = ((0:ℝ), Real.exp 1) ∧ γ 0 ≠ γ 1 := by
  have hnull : ∀ s, mink.gE (γ s) (vel γ s) (vel γ s) = 0 := fun s => by
    rw [mink_gE, vel_γ, gM_apply]; simp
  have hhz : ∀ s, σ.h s (vel γ s) (vel γ s) = 0 := hnull
  have hΔx : σ.Δx = 0 := by
    unfold AdaptedSplitting.Δx
    simp only [hhz, Real.sqrt_zero, intervalIntegral.integral_zero]
  have hcont : ContinuousOn (fun s => σ.h s (vel γ s) (vel γ s)) (Icc 0 1) := by
    simp only [hhz]; exact continuousOn_const
  refine ⟨g_χ_χ, fun s => by rw [vel_γ]; simp [χ, γ], fun s => ⟨hnull s, ?_⟩, σ_n, ?_,
    fun s _ => hnull s, hΔx, hcont,
    (ac_metric_singularity_along mink σ (fun s _ => hnull s) hΔx hcont).1,
    by simp [γ], rfl, ?_⟩
  · rw [vel_γ]; intro h; exact Real.exp_ne_zero s (congrArg Prod.snd h)
  · simp only [σ_dt]; simp
  · intro h
    have := congrArg Prod.snd h
    simp only [γ, Real.exp_zero] at this
    exact (Real.exp_one_gt_d9.trans' (by norm_num)).ne this

/-- Along the witness curve, **no** adapted splitting with positive lapse (and `h` positive definite on
`ker dt`) satisfies (a), (b): by `ac_lapse_pos_forces_point` it would give `γ 1 = γ 0`. -/
theorem ac_witness_no_positive_lapse (τ : AdaptedSplitting mink γ)
    (hb : τ.Δx = 0)
    (hcont : ContinuousOn (fun s => τ.h s (vel γ s) (vel γ s)) (Icc 0 1))
    (hpd : ∀ s ∈ Icc (0:ℝ) 1, ∀ v : P, v ≠ 0 → τ.dt s v = 0 → 0 < τ.h s v v) :
    ¬ ∀ s ∈ Icc (0:ℝ) 1, 0 < τ.n s := by
  intro hn
  have hγ := ac_witness
  obtain ⟨-, -, -, -, -, ha, -, -, -, -, -, hpq⟩ := hγ
  have hd : ∀ t ∈ Icc (0:ℝ) 1, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, P) γ t := fun t _ =>
    mdifferentiableAt_iff_differentiableAt.mpr (hasDerivAt_γ t).differentiableAt
  exact hpq ((ac_lapse_pos_forces_point mink τ ha hb hcont hn hpd).2 hd).symm

/-! ### Non-vacuity of the companion: the standard `t`-splitting on a constant curve -/

/-- The constant curve at the origin. -/
def γ₀ (_ : ℝ) : P := (0, 0)

lemma vel_γ₀ (s : ℝ) : vel (E := P) γ₀ s = 0 := vel_eq_of_hasDerivAt (hasDerivAt_const s (0, 0))

/-- `dt = (dU + dV)/2`. -/
def dt₀ : P →L[ℝ] ℝ := (1/2 : ℝ) • (fst ℝ ℝ ℝ + snd ℝ ℝ ℝ)

/-- `−dU dV = −dt² + dx²`: the standard splitting `h = g + dt ⊗ dt`, `n = 1`. -/
def σ₀ : AdaptedSplitting mink γ₀ where
  h := fun _ => gM + dt₀.smulRight dt₀
  n := fun _ => 1
  dt := fun _ => dt₀
  n_nonneg := fun _ _ => zero_le_one
  split := fun _ _ => by
    refine ContinuousLinearMap.ext fun a => ContinuousLinearMap.ext fun b => ?_
    show gM a b = _
    simp
  h_nonneg := fun s _ => by rw [vel_γ₀]; simp

/-- **Non-vacuity of `ac_lapse_pos_forces_point`:** every hypothesis holds for `σ₀` (lapse `1`, `h = dx²`
positive definite on `ker dt`), on the constant curve `γ₀`. -/
theorem ac_lapse_pos_nonvacuous :
    (∀ s ∈ Icc (0:ℝ) 1, mink.gE (γ₀ s) (vel γ₀ s) (vel γ₀ s) = 0) ∧ σ₀.Δx = 0 ∧
    ContinuousOn (fun s => σ₀.h s (vel γ₀ s) (vel γ₀ s)) (Icc 0 1) ∧
    (∀ s ∈ Icc (0:ℝ) 1, 0 < σ₀.n s) ∧
    (∀ s ∈ Icc (0:ℝ) 1, ∀ v : P, v ≠ 0 → σ₀.dt s v = 0 → 0 < σ₀.h s v v) := by
  have hz : ∀ s, σ₀.h s (vel γ₀ s) (vel γ₀ s) = 0 := fun s => by rw [vel_γ₀]; simp
  refine ⟨fun s _ => by rw [vel_γ₀]; simp, ?_, ?_, fun _ _ => zero_lt_one, ?_⟩
  · unfold AdaptedSplitting.Δx; simp only [hz, Real.sqrt_zero, intervalIntegral.integral_zero]
  · simp only [hz]; exact continuousOn_const
  · intro s _ v hv hdt
    change dt₀ v = 0 at hdt
    show 0 < (gM + dt₀.smulRight dt₀) v v
    have edt : dt₀ v = (1/2) * (v.1 + v.2) := by simp [dt₀]; ring
    have eh : (gM + dt₀.smulRight dt₀) v v = gM v v + dt₀ v * dt₀ v := by simp
    rw [eh, hdt, gM_apply]
    have h2 : v.2 = -v.1 := by linarith
    have h1 : v.1 ≠ 0 := by
      intro h1; apply hv; ext
      · exact h1
      · rw [h2, h1]; simp
    rw [h2]; nlinarith [sq_pos_of_ne_zero h1]


end ACModel
end


/-! ## NEW (campaign 103) ①: the strict null ordering (`cor:threefold` 2ii) on `N` -/

section ThreefoldOrder
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

namespace MSpacetime

/-- `I⁺(p) ⊆ int J⁺(p)` on `N`: `I⁺(p)` is open (`mk_isOpen_Ifut`) and lies in `J⁺(p)`
(`chr_cau`). -/
theorem to_Ifut_subset_interior (S : MSpacetime E N) (hL : S.LocallyOneChart) (p : N) :
    {y | S.Chr p y} ⊆ interior {y | S.Cau p y} :=
  interior_maximal (fun _ h => S.chr_cau h) (S.mk_isOpen_Ifut hL p)

/-- **A frontier point of `J⁺(p)` is not in `I⁺(p)`** (the corollary): `q ∈ ∂J⁺(p) ⟹ q ∉ I⁺(p)`. -/
theorem to_frontier_not_mem_Ifut (S : MSpacetime E N) (hL : S.LocallyOneChart) {p q : N}
    (hq : q ∈ frontier {y | S.Cau p y}) : q ∉ {y | S.Chr p y} := fun h =>
  hq.2 (S.to_Ifut_subset_interior hL p h)

/-- **`cor:threefold` (ii), the strict null ordering, on any `LocallyOneChart` spacetime on `N`
(BUILT).** If `q ∈ ∂J⁺(p)` and `r` is causally between `p` and `q` (`p ≤ r ≤ q`), then `r ∉ I⁺(p)`.
If `p ≪ r`, the dual push-up `mk_pushup'` gives `p ≪ q`, so `q` lies in the open `I⁺(p) ⊆ J⁺(p)`,
hence in `int J⁺(p)`, which a frontier point does not. No geodesic is assumed. (The hypothesis
`Cau p r` is not used by the proof: `r ≤ q` alone suffices.) -/
theorem to_strict_null_order (S : MSpacetime E N) (hL : S.LocallyOneChart) {p q r : N}
    (hq : q ∈ frontier {y | S.Cau p y}) (_hpr : S.Cau p r) (hrq : S.Cau r q) : ¬ S.Chr p r :=
  fun h => S.to_frontier_not_mem_Ifut hL hq (S.mk_pushup' hL h hrq)

end MSpacetime

end ThreefoldOrder

/-! ## NEW (campaign 103) ①: the witness on `Pt` -/

namespace Model
open ContinuousLinearMap

/-- The straight segment is a causal step when neither null coordinate decreases (and `x ≠ y`). -/
lemma to_cstep_of_le {x y : P} (h1 : x.1 ≤ y.1) (h2 : x.2 ≤ y.2) (hne : x ≠ y) :
    mink.CStep x y := by
  refine ⟨fun t => x + t • (y - x), contDiff_const.add (contDiff_id.smul contDiff_const),
    by simp, by simp, fun t _ => ⟨mem_univ _, ?_⟩⟩
  have hd : deriv (fun t : ℝ => x + t • (y - x)) t = y - x := by
    have h : HasDerivAt (fun t : ℝ => x + t • (y - x)) ((1:ℝ) • (y - x)) t :=
      ((hasDerivAt_id' t).smul_const (y - x)).const_add x
    rw [h.deriv, one_smul]
  rw [hd, futCausal_iff]
  simp only [Prod.fst_sub, Prod.snd_sub, sub_nonneg]
  refine ⟨h1, h2, ?_⟩
  by_contra hc
  exact hne (Prod.ext (by linarith) (by linarith))

/-- **`J⁺` on the model:** `x ≤ y ↔ x_U ≤ y_U ∧ x_V ≤ y_V`. -/
theorem to_cau_iff {x y : P} : mink.Cau x y ↔ x.1 ≤ y.1 ∧ x.2 ≤ y.2 := by
  refine ⟨cau_le, fun ⟨h1, h2⟩ => ?_⟩
  by_cases h : x = y
  · subst h; exact Relation.ReflTransGen.refl
  · exact Relation.ReflTransGen.single (to_cstep_of_le h1 h2 h)

/-- **`I⁺` on the model:** `x ≪ y ↔ x_U < y_U ∧ x_V < y_V`. -/
theorem to_chr_iff {x y : P} : mink.Chr x y ↔ x.1 < y.1 ∧ x.2 < y.2 :=
  ⟨chr_lt, fun ⟨h1, h2⟩ => Relation.TransGen.single (tstep_of_lt h1 h2)⟩

/-- A point of the closed quadrant `{a_U ≤ U, a_V ≤ V}` with `U = a_U` lies on its frontier. -/
lemma to_mem_frontier_quadrant {a u : P} (h1 : u.1 = a.1) (h2 : a.2 ≤ u.2) :
    u ∈ frontier {v : P | a.1 ≤ v.1 ∧ a.2 ≤ v.2} := by
  have e : {v : P | a.1 ≤ v.1 ∧ a.2 ≤ v.2} = Ici a.1 ×ˢ Ici a.2 := rfl
  rw [e, frontier_prod_eq]
  simp only [frontier_Ici, closure_Ici]
  exact Or.inr ⟨h1, h2⟩

end Model

namespace NModel
open Model Manifold

/-- `ψ` is injective (`φ ∘ ψ = id`). -/
lemma to_ψ_injective : Function.Injective ψ := fun a b h => by
  rw [← φψ a, ← φψ b, h]

/-- **`J⁺` on `Pt`, through the global chart:** `x ≤ y ↔ φ(x) ≤ φ(y)` in both null coordinates
(`ch_cau_iff`, `ch_chartSp_eq`). -/
theorem to_cau_iff_N (x y : Pt) : minkN.Cau x y ↔ (φ x).1 ≤ (φ y).1 ∧ (φ x).2 ≤ (φ y).2 := by
  rw [MSpacetime.ch_cau_iff ch_oneChart (src x) (src y), ch_chartSp_eq, Model.to_cau_iff]
  exact Iff.rfl

/-- **`I⁺` on `Pt`, through the global chart** (`ch_chr_iff`). -/
theorem to_chr_iff_N (x y : Pt) : minkN.Chr x y ↔ (φ x).1 < (φ y).1 ∧ (φ x).2 < (φ y).2 := by
  rw [MSpacetime.ch_chr_iff ch_oneChart (src x) (src y), ch_chartSp_eq, Model.to_chr_iff]
  exact Iff.rfl

/-- The point `(U, V) = (0, V)` of the null generator `U = 0` of `Pt`. -/
noncomputable def to_gen (V : ℝ) : Pt := ψ ((0 : ℝ), V)

lemma to_φ_gen (V : ℝ) : φ (to_gen V) = ((0 : ℝ), V) := φψ _

/-- **`J⁺((0, V₁))` is the closed quadrant** `{U ≥ 0, V ≥ V₁}` (in null coordinates). -/
theorem to_Jfut_gen (V₁ : ℝ) (y : Pt) :
    minkN.Cau (to_gen V₁) y ↔ 0 ≤ (φ y).1 ∧ V₁ ≤ (φ y).2 := by
  rw [to_cau_iff_N, to_φ_gen]

/-- `(0, V₂) ∈ ∂J⁺((0, V₁))` for `V₁ ≤ V₂` (`ch_mem_frontier_iff`). -/
theorem to_gen_mem_frontier {V₁ V₂ : ℝ} (h : V₁ ≤ V₂) :
    to_gen V₂ ∈ frontier {y | minkN.Cau (to_gen V₁) y} := by
  rw [ch_mem_frontier_iff (p₀ := p₀) (A := {y | minkN.Cau (to_gen V₁) y}) (B := {v : P | (0:ℝ) ≤ v.1 ∧ V₁ ≤ v.2})
    (fun x _ => to_Jfut_gen V₁ x) (src _)]
  show φ (to_gen V₂) ∈ _
  rw [to_φ_gen]
  exact Model.to_mem_frontier_quadrant (a := ((0:ℝ), V₁)) rfl h

/-- **The strict null ordering witnessed on `Pt` (BUILT).** For `V₁ < V₂`, `p = (0, V₁)` and
`q = (0, V₂)` on the null generator `U = 0`: `J⁺(p)` is the closed quadrant; `q ∈ ∂J⁺(p)`;
`p ≤ q` and `p ̸≪ q`, `p ≠ q`; and every point `(0, V)`, `V₁ < V < V₂`, strictly between them on
the generator is causally between them, distinct from both, and **not in `I⁺(p)`, by
`to_strict_null_order`** (`me_locallyOneChart`). So ①'s hypotheses hold on this pair: not vacuous. -/
theorem to_witness_order {V₁ V₂ : ℝ} (h : V₁ < V₂) :
    (∀ y, minkN.Cau (to_gen V₁) y ↔ 0 ≤ (φ y).1 ∧ V₁ ≤ (φ y).2) ∧
    to_gen V₂ ∈ frontier {y | minkN.Cau (to_gen V₁) y} ∧
    minkN.Cau (to_gen V₁) (to_gen V₂) ∧ ¬ minkN.Chr (to_gen V₁) (to_gen V₂) ∧
    to_gen V₁ ≠ to_gen V₂ ∧
    ∀ V, V₁ < V → V < V₂ →
      minkN.Cau (to_gen V₁) (to_gen V) ∧ minkN.Cau (to_gen V) (to_gen V₂) ∧
      to_gen V ≠ to_gen V₁ ∧ to_gen V ≠ to_gen V₂ ∧
      to_gen V ∉ {y | minkN.Chr (to_gen V₁) y} := by
  have hq := to_gen_mem_frontier h.le
  have hcau : ∀ a b : ℝ, a ≤ b → minkN.Cau (to_gen a) (to_gen b) := fun a b hab => by
    rw [to_cau_iff_N, to_φ_gen, to_φ_gen]; exact ⟨le_rfl, hab⟩
  have hne : ∀ a b : ℝ, a ≠ b → to_gen a ≠ to_gen b := fun a b hab he =>
    hab (congrArg Prod.snd (to_ψ_injective he))
  refine ⟨to_Jfut_gen V₁, hq, hcau _ _ h.le,
    minkN.to_frontier_not_mem_Ifut me_locallyOneChart hq, hne _ _ h.ne,
    fun V h1 h2 => ⟨hcau _ _ h1.le, hcau _ _ h2.le, hne _ _ h1.ne', hne _ _ h2.ne,
      minkN.to_strict_null_order me_locallyOneChart hq (hcau _ _ h1.le) (hcau _ _ h2.le)⟩⟩

/-- **The registered pair** `p = (0, 1)`, `q = (0, e)`. -/
theorem to_witness_order_e :
    to_gen (Real.exp 1) ∈ frontier {y | minkN.Cau (to_gen 1) y} ∧
    minkN.Cau (to_gen 1) (to_gen (Real.exp 1)) ∧ ¬ minkN.Chr (to_gen 1) (to_gen (Real.exp 1)) ∧
    ∀ V, 1 < V → V < Real.exp 1 →
      minkN.Cau (to_gen 1) (to_gen V) ∧ minkN.Cau (to_gen V) (to_gen (Real.exp 1)) ∧
      to_gen V ∉ {y | minkN.Chr (to_gen 1) y} := by
  obtain ⟨-, hq, hc, hn, -, hb⟩ := to_witness_order (Real.one_lt_exp_iff.2 one_pos)
  exact ⟨hq, hc, hn, fun V h1 h2 =>
    ⟨(hb V h1 h2).1, (hb V h1 h2).2.1, (hb V h1 h2).2.2.2.2⟩⟩

/-! ## NEW (campaign 103) ②: `thm:metric-singularity` 1c — one pair, three properties, on `Pt` -/

/-- `ac_witness`'s Rindler-horizon generator `γ s = (0, eˢ)`, carried to `Pt` by `ψ = φ⁻¹`. -/
noncomputable def to_γN (s : ℝ) : Pt := ψ (ACModel.γ s)

lemma to_γN_eq (s : ℝ) : to_γN s = to_gen (Real.exp s) := rfl

lemma to_tco_γN (s : ℝ) : ¬ tco (to_γN s) < 0 := by
  rw [to_γN, mx_ψ_eq]
  show ¬ ((0 + Real.exp s) / 2 : ℝ) < 0
  have := Real.exp_pos s
  linarith

/-- **The velocity on `Pt` is `ac_`'s model velocity** `(0, eˢ)`: `γN = φ⁻¹ ∘ γ`, `ch_vel_symm`,
and `Dφ⁻¹ = id` on `{t ≥ 0}` (`dinv_eq`). -/
lemma to_vel_γN (s : ℝ) : MSpacetime.vel (E := P) to_γN s = MSpacetime.vel (E := P) ACModel.γ s := by
  rw [ACModel.vel_γ]
  have hβ : DifferentiableAt ℝ ACModel.γ s := (ACModel.hasDerivAt_γ s).differentiableAt
  have ht : ACModel.γ s ∈ (extChartAt 𝓘(ℝ, P) p₀).target := by rw [target_eq]; exact mem_univ _
  have h2 := (ch_vel_symm p₀ hβ ht).2
  have e : MSpacetime.vel (E := P) to_γN s =
      mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, P) (fun s => (extChartAt 𝓘(ℝ, P) p₀).symm (ACModel.γ s)) s (1 : ℝ) := rfl
  have hd : deriv ACModel.γ s = ((0 : ℝ), Real.exp s) := (ACModel.hasDerivAt_γ s).deriv
  rw [e, h2]
  show dchartInv p₀ (ACModel.γ s) (deriv ACModel.γ s) = _
  rw [hd]
  have h3 := dinv_eq (to_γN s) ((0 : ℝ), Real.exp s)
  rw [ite_eq_right (to_tco_γN s)] at h3
  have e2 : extChartAt 𝓘(ℝ, P) p₀ (to_γN s) = ACModel.γ s := φψ _
  rw [e2] at h3
  exact h3

/-- The metric of `minkN` along `γN` is `ac_`'s `g = −dU dV` (the null chart on `{t ≥ 0}`). -/
lemma to_gE_γN (s : ℝ) : minkN.gE (to_γN s) = ACModel.mink.gE (ACModel.γ s) := by
  show gN (to_γN s) = gM
  unfold gN
  exact ite_eq_right (to_tco_γN s)

/-- **`ac_`'s splitting `σ`, restated on `Pt`** along `γN`: the same `h = g`, lapse
`n = √(max 0 (−g(χ, χ))) = 0`, and `dt = dV/V`. -/
noncomputable def to_σN : AdaptedSplitting minkN to_γN where
  h := ACModel.σ.h
  n := ACModel.σ.n
  dt := ACModel.σ.dt
  n_nonneg := ACModel.σ.n_nonneg
  split := fun s hs => by rw [to_gE_γN]; exact ACModel.σ.split s hs
  h_nonneg := fun s hs => by rw [to_vel_γN]; exact ACModel.σ.h_nonneg s hs

lemma to_σN_Δx : to_σN.Δx = ACModel.σ.Δx := by
  unfold AdaptedSplitting.Δx
  simp only [to_vel_γN]
  rfl

lemma to_σN_Δτ : to_σN.Δτ = ACModel.σ.Δτ := by
  unfold AdaptedSplitting.Δτ
  simp only [to_vel_γN]
  rfl

/-- **`thm:metric-singularity` 1c, in one theorem (BUILT).** On `Pt` (`minkN`), the two events
`p = γN 0 = (0, 1)` and `q = γN 1 = (0, e)` of `ac_witness`'s Rindler-horizon generator are
* **topologically distinct:** `p ≠ q`;
* **causally ordered:** `p ≤ q` and `p ̸≪ q`, with `q ∈ ∂J⁺(p)`, and ①'s ordering: no event
  causally between them is in `I⁺(p)` (in particular no point `γN s`, `s ∈ [0, 1]`);
* **metrically coincident:** along `γN`, `g(γ′, γ′) = 0` on `[0, 1]`, and for the adapted splitting
  `to_σN` (vanishing lapse) `Δx = 0`, and `Δτ = 0` by `ac_metric_singularity_along` applied on
  `minkN` itself; these equal `ac_witness`'s `Δx`, `Δτ` on the model space. -/
theorem to_cor_1c :
    to_γN 0 = to_gen 1 ∧ to_γN 1 = to_gen (Real.exp 1) ∧
    to_γN 0 ≠ to_γN 1 ∧
    minkN.Cau (to_γN 0) (to_γN 1) ∧ ¬ minkN.Chr (to_γN 0) (to_γN 1) ∧
    to_γN 1 ∈ frontier {y | minkN.Cau (to_γN 0) y} ∧
    (∀ r, minkN.Cau (to_γN 0) r → minkN.Cau r (to_γN 1) → ¬ minkN.Chr (to_γN 0) r) ∧
    (∀ s ∈ Icc (0:ℝ) 1, minkN.Cau (to_γN 0) (to_γN s) ∧ minkN.Cau (to_γN s) (to_γN 1) ∧
      ¬ minkN.Chr (to_γN 0) (to_γN s)) ∧
    (∀ s ∈ Icc (0:ℝ) 1,
      minkN.gE (to_γN s) (MSpacetime.vel to_γN s) (MSpacetime.vel to_γN s) = 0) ∧
    (∀ s, to_σN.n s = 0) ∧ to_σN.Δx = 0 ∧ to_σN.Δτ = 0 ∧
    to_σN.Δx = ACModel.σ.Δx ∧ to_σN.Δτ = ACModel.σ.Δτ := by
  obtain ⟨-, -, -, hn, -, ha, hΔx, hcont, -, -, -, hpq⟩ := ACModel.ac_witness
  have e1 : (1 : ℝ) < Real.exp 1 := Real.one_lt_exp_iff.2 one_pos
  have hq : to_γN 1 ∈ frontier {y | minkN.Cau (to_γN 0) y} := by
    rw [to_γN_eq, to_γN_eq, Real.exp_zero]; exact to_gen_mem_frontier e1.le
  have hcau : ∀ a b : ℝ, a ≤ b → minkN.Cau (to_γN a) (to_γN b) := fun a b hab => by
    rw [to_γN_eq, to_γN_eq, to_cau_iff_N, to_φ_gen, to_φ_gen]
    exact ⟨le_rfl, Real.exp_le_exp.2 hab⟩
  have hord : ∀ r, minkN.Cau (to_γN 0) r → minkN.Cau r (to_γN 1) → ¬ minkN.Chr (to_γN 0) r :=
    fun r h1 h2 => minkN.to_strict_null_order me_locallyOneChart hq h1 h2
  have haN : ∀ s ∈ Icc (0:ℝ) 1,
      minkN.gE (to_γN s) (MSpacetime.vel to_γN s) (MSpacetime.vel to_γN s) = 0 := fun s hs => by
    rw [to_gE_γN, to_vel_γN]; exact ha s hs
  have hΔxN : to_σN.Δx = 0 := to_σN_Δx.trans hΔx
  have hcontN : ContinuousOn (fun s => to_σN.h s (MSpacetime.vel to_γN s)
      (MSpacetime.vel to_γN s)) (Icc 0 1) := by
    simp only [to_vel_γN]; exact hcont
  refine ⟨by rw [to_γN_eq, Real.exp_zero], by rw [to_γN_eq], fun h => hpq (to_ψ_injective h),
    hcau 0 1 zero_le_one, minkN.to_frontier_not_mem_Ifut me_locallyOneChart hq, hq, hord,
    fun s hs => ⟨hcau _ _ hs.1, hcau _ _ hs.2, hord _ (hcau _ _ hs.1) (hcau _ _ hs.2)⟩,
    haN, hn, hΔxN,
    (ac_metric_singularity_along minkN to_σN haN hΔxN hcontN).1, to_σN_Δx, to_σN_Δτ⟩

end NModel

/-! ## NEW (campaign 104): `cor:threefold` 2i under "no closed causal curves" -/

section ThreefoldDistinct
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

namespace MSpacetime

/-- **No closed causal curves** (P1's new hypothesis of `cor:threefold`): no point is joined to
itself by a non-empty chain of the kit's future causal steps `CStep` (the step relation underlying
`Cau = ReflTransGen CStep`). A causal curve from `p` to `q` is such a chain. -/
def NoClosedCausal (S : MSpacetime E N) : Prop := ∀ p, ¬ Relation.TransGen S.CStep p p

/-- **`cor:threefold` (i), distinctness (BUILT).** With no closed causal curves, the endpoints of a
causal curve (a non-empty chain of causal steps) are distinct. -/
theorem td_ne_of_transGen (S : MSpacetime E N) (hS : S.NoClosedCausal) {p q : N}
    (h : Relation.TransGen S.CStep p q) : p ≠ q := by
  rintro rfl; exact hS p h

/-- **`cor:threefold` (i) (BUILT).** With no closed causal curves, the endpoints `p`, `q` of a causal
curve are distinct, and on a Hausdorff `N` they have disjoint open neighbourhoods
(`t2_separation`): they are topologically distinguishable. -/
theorem td_cor_threefold_i [T2Space N] (S : MSpacetime E N) (hS : S.NoClosedCausal) {p q : N}
    (h : Relation.TransGen S.CStep p q) :
    p ≠ q ∧ ∃ U W : Set N, IsOpen U ∧ IsOpen W ∧ p ∈ U ∧ q ∈ W ∧ Disjoint U W :=
  ⟨S.td_ne_of_transGen hS h, t2_separation (S.td_ne_of_transGen hS h)⟩

/-- `Cau p q` with `p ≠ q` is a non-empty chain of causal steps. -/
theorem td_transGen_of_cau_ne (S : MSpacetime E N) {p q : N} (h : S.Cau p q) (hne : p ≠ q) :
    Relation.TransGen S.CStep p q :=
  (Relation.reflTransGen_iff_eq_or_transGen.1 h).resolve_left (fun e => hne e.symm)

/-- Any `τ` raised strictly by every causal step forbids closed causal chains. -/
theorem td_noClosed_of_lt (S : MSpacetime E N) (τ : N → ℝ)
    (hτ : ∀ x y, S.CStep x y → τ x < τ y) : S.NoClosedCausal := by
  have key : ∀ {x y}, Relation.TransGen S.CStep x y → τ x < τ y := by
    intro x y h
    induction h with
    | single h => exact hτ _ _ h
    | tail _ h ih => exact ih.trans (hτ _ _ h)
  exact fun p h => lt_irrefl _ (key h)

/-- **A temporal function on an open `U` strictly increases along a causal piece inside `U`**
(the causal form of `me_temporal_strictMonoOn`: `dτ(γ′) > 0` on future-causal `γ′`). -/
theorem td_temporal_curve_lt (S : MSpacetime E N) {U : Set N} (hU : IsOpen U) {τ : N → ℝ}
    (hτ : S.IsTemporalOn U τ) {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ U ∧ S.FutCausal (γ t) (vel γ t)) : τ (γ 0) < τ (γ 1) := by
  have hcont : ContinuousOn (fun s => τ (γ s)) (Icc (0:ℝ) 1) :=
    hτ.1.continuousOn.comp hγ.continuous.continuousOn fun t h => (ht t h).1
  have hmono : StrictMonoOn (fun s => τ (γ s)) (Icc 0 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hcont fun t htI => ?_
    rw [interior_Icc] at htI
    obtain ⟨hm, hc⟩ := ht t (Ioo_subset_Icc_self htI)
    rw [(me_temporal_hasDerivAt hU hτ.1 (hγ.mdifferentiableAt one_ne_zero) hm).deriv]
    exact hτ.2 _ hm _ hc
  exact hmono ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one

/-- A temporal `τ` on `M` strictly increases along every causal step. -/
theorem td_temporal_cstep (S : MSpacetime E N) {τ : N → ℝ} (hτ : S.IsTemporalOn S.M τ) {x y : N}
    (h : S.CStep x y) : τ x < τ y := by
  obtain ⟨γ, hγ, rfl, rfl, ht⟩ := h
  exact S.td_temporal_curve_lt S.isOpen_M hτ hγ ht

/-- **② (BUILT).** A temporal function on `M` rules out closed causal curves: each step strictly
raises `τ`, so a chain does, and `τ p < τ p` is impossible. -/
theorem td_noClosed_of_temporal (S : MSpacetime E N) {τ : N → ℝ} (hτ : S.IsTemporalOn S.M τ) :
    S.NoClosedCausal :=
  S.td_noClosed_of_lt τ fun _ _ h => S.td_temporal_cstep hτ h

/-- **② on an open `U ⊆ M` (BUILT).** A temporal function on `U` rules out closed chains of causal
steps inside `U`, i.e. the restricted spacetime `S.restrictM U` has no closed causal curves. -/
theorem td_noClosed_of_temporalOn (S : MSpacetime E N) {U : Set N} (hU : IsOpen U) (hUM : U ⊆ S.M)
    {τ : N → ℝ} (hτ : S.IsTemporalOn U τ) : (S.restrictM U hU hUM).NoClosedCausal :=
  (S.restrictM U hU hUM).td_noClosed_of_temporal hτ

/-- **② on `D` (BUILT).** A Cauchy temporal function on `D = I⁻(J)` gives `NoClosedCausal` for `D`
as a spacetime (`DspN`, P1's globally hyperbolic exterior). -/
theorem td_noClosed_D (S : MSpacetime E N) (hL : S.LocallyOneChart) {J : Set N} {Θ : N → ℝ}
    (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) : (S.DspN hL J).NoClosedCausal :=
  S.td_noClosed_of_temporalOn (S.mk_isOpen_D hL J) (S.D_subset_M J) hΘ.1

end MSpacetime

end ThreefoldDistinct

namespace Model
open ContinuousLinearMap

/-- `U + V` strictly increases along a causal step of the vector-space Minkowski `mink`. -/
theorem td_cstep_sum_lt {x y : P} (h : mink.CStep x y) : x.1 + x.2 < y.1 + y.2 := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have k := fun t ht => (futCausal_iff _ _).1 (hγt t ht).2
  subst h0 h1
  simpa using lin_lt_of_step hγ (fst ℝ ℝ ℝ + snd ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).2.2)

end Model

namespace NModel
open Model Manifold

/-- On `Pt`, `τ = U + V` (through the global chart `φ`) strictly increases along every causal step
of `minkN` (`ch_cstep_NV`, `ch_chartSp_eq`, `td_cstep_sum_lt`). -/
theorem td_minkN_cstep_lt {x y : Pt} (h : minkN.CStep x y) :
    (φ x).1 + (φ x).2 < (φ y).1 + (φ y).2 := by
  have h' := MSpacetime.ch_cstep_NV ch_oneChart h
  rw [ch_chartSp_eq] at h'
  exact td_cstep_sum_lt h'

/-- **Minkowski on `Pt` has no closed causal curves (BUILT)**, via `τ = U + V`. -/
theorem td_minkN_noClosed : minkN.NoClosedCausal :=
  minkN.td_noClosed_of_lt (fun x => (φ x).1 + (φ x).2) fun _ _ h => td_minkN_cstep_lt h

/-- **`to_cor_1c`'s pair satisfies (i)'s hypothesis (BUILT).** `minkN` has no closed causal curves,
`p = γN 0`, `q = γN 1` are joined by a non-empty chain of causal steps, and (i) then gives them
distinct with disjoint open neighbourhoods — re-deriving `to_cor_1c`'s `p ≠ q` from (i). -/
theorem td_cor_1c_hyp :
    minkN.NoClosedCausal ∧ Relation.TransGen minkN.CStep (to_γN 0) (to_γN 1) ∧
    to_γN 0 ≠ to_γN 1 ∧ ∃ U W : Set Pt, IsOpen U ∧ IsOpen W ∧ to_γN 0 ∈ U ∧ to_γN 1 ∈ W ∧
      Disjoint U W := by
  obtain ⟨-, -, hne, hcau, -⟩ := to_cor_1c
  have hT := minkN.td_transGen_of_cau_ne hcau hne
  exact ⟨td_minkN_noClosed, hT, minkN.td_cor_threefold_i td_minkN_noClosed hT⟩

end NModel

-- campaign 109 (new): the tl_ section

section ThreefoldLocal
open Manifold
set_option linter.unusedSectionVars false

/-! ### ① The cone bound, in a vector space -/

/-- **The compactness step (vector space).** On a compact `K ⊆ E` (`E` finite-dimensional) with a
bilinear form `G`, a vector field `Tv` and a one-form `D`, all continuous on `K`, such that `G` is
positive on `Tv^⊥ \ {0}` and `D` is positive on the open future cone `{G(w,w) ≤ 0, G(w,Tv) < 0}`:
`D` is bounded below on that cone by `c‖w‖` for one `c > 0`. (The unit cone
`{‖w‖ = 1, G(w,w) ≤ 0, G(w,Tv) ≤ 0}` is closed, hence compact, and equals the strict one because a
nonzero `w` with `G(w,Tv) = 0` has `G(w,w) > 0`.) -/
theorem tl_cone_bound_vs {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [FiniteDimensional ℝ E] {K : Set E} (hK : IsCompact K) {G : E → E →L[ℝ] E →L[ℝ] ℝ}
    {Tv : E → E} {D : E → E →L[ℝ] ℝ}
    (hG : ContinuousOn G K) (hT : ContinuousOn Tv K) (hD : ContinuousOn D K)
    (hperp : ∀ y ∈ K, ∀ w, G y w (Tv y) = 0 → w ≠ 0 → 0 < G y w w)
    (hpos : ∀ y ∈ K, ∀ w, G y w w ≤ 0 → G y w (Tv y) < 0 → 0 < D y w) :
    ∃ c > 0, ∀ y ∈ K, ∀ w, G y w w ≤ 0 → G y w (Tv y) < 0 → c * ‖w‖ ≤ D y w := by
  set A : Set (E × E) := K ×ˢ sphere (0:E) 1 with hA
  have hAc : IsCompact A := hK.prod (isCompact_sphere 0 1)
  have hG1 : ContinuousOn (fun p : E × E => G p.1) A :=
    hG.comp continuousOn_fst (fun p hp => hp.1)
  have hcA1 : ContinuousOn (fun p : E × E => G p.1 p.2 p.2) A :=
    (hG1.clm_apply continuousOn_snd).clm_apply continuousOn_snd
  have hcA2 : ContinuousOn (fun p : E × E => G p.1 p.2 (Tv p.1)) A :=
    (hG1.clm_apply continuousOn_snd).clm_apply (hT.comp continuousOn_fst (fun p hp => hp.1))
  have hcD : ContinuousOn (fun p : E × E => D p.1 p.2) A :=
    (hD.comp continuousOn_fst (fun p hp => hp.1)).clm_apply continuousOn_snd
  set B := A ∩ (fun p : E × E => (G p.1 p.2 p.2, G p.1 p.2 (Tv p.1))) ⁻¹' (Iic 0 ×ˢ Iic 0)
    with hB
  have hBc : IsCompact B := hAc.of_isClosed_subset
    ((hcA1.prodMk hcA2).preimage_isClosed_of_isClosed hAc.isClosed
      (isClosed_Iic.prod isClosed_Iic)) inter_subset_left
  have hBpos : ∀ p ∈ B, 0 < D p.1 p.2 := by
    rintro ⟨y, w⟩ ⟨⟨hy, hw⟩, h1, h2⟩
    have hw0 : w ≠ 0 := by
      rintro rfl; simp at hw
    have h1' : G y w w ≤ 0 := h1
    have h2' : G y w (Tv y) < 0 := by
      rcases (show G y w (Tv y) ≤ 0 from h2).lt_or_eq with h | h
      · exact h
      · exact absurd (hperp y hy w h hw0) (not_lt.2 h1')
    exact hpos y hy w h1' h2'
  have hscale : ∀ y ∈ K, ∀ w, G y w w ≤ 0 → G y w (Tv y) < 0 →
      w ≠ 0 ∧ (y, ‖w‖⁻¹ • w) ∈ B := by
    intro y hy w h1 h2
    have hw0 : w ≠ 0 := by rintro rfl; simp at h2
    have hn : 0 < ‖w‖ := norm_pos_iff.2 hw0
    refine ⟨hw0, ⟨hy, ?_⟩, ?_, ?_⟩
    · rw [mem_sphere_zero_iff_norm, norm_smul, norm_inv, norm_norm, inv_mul_cancel₀ hn.ne']
    · show G y (‖w‖⁻¹ • w) (‖w‖⁻¹ • w) ≤ 0
      simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
      have : 0 < ‖w‖⁻¹ := inv_pos.2 hn
      nlinarith [mul_pos this this]
    · show G y (‖w‖⁻¹ • w) (Tv y) ≤ 0
      simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
      have : 0 < ‖w‖⁻¹ := inv_pos.2 hn
      nlinarith
  rcases B.eq_empty_or_nonempty with hBe | hBne
  · refine ⟨1, one_pos, fun y hy w h1 h2 => ?_⟩
    have := (hscale y hy w h1 h2).2
    rw [hBe] at this; exact this.elim
  · obtain ⟨p0, hp0, hmin⟩ := hBc.exists_isMinOn hBne (hcD.mono inter_subset_left)
    refine ⟨D p0.1 p0.2, hBpos p0 hp0, fun y hy w h1 h2 => ?_⟩
    obtain ⟨hw0, hm⟩ := hscale y hy w h1 h2
    have hle : D p0.1 p0.2 ≤ D y (‖w‖⁻¹ • w) := hmin hm
    rw [map_smul, smul_eq_mul] at hle
    have hn : 0 < ‖w‖ := norm_pos_iff.2 hw0
    calc D p0.1 p0.2 * ‖w‖ ≤ ‖w‖⁻¹ * D y w * ‖w‖ := by gcongr
      _ = D y w := by field_simp

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

namespace MSpacetime

/-! ### Reading `dτ` and the causal cone in the preferred chart at `q` -/

/-- **The chain rule through the chart at `q`.** If `h = f ∘ φ_q` near `x ∈ src_q`, with `f`
differentiable at `φ_q x`, then `dh_x(v) = Df(φ_q x)(Dφ_q(x) v)`. -/
theorem tl_dfun_chart {q x : N} (hx : x ∈ (chartAt E q).source) {h : N → ℝ} {f : E → ℝ}
    (hf : DifferentiableAt ℝ f (extChartAt 𝓘(ℝ, E) q x))
    (he : h =ᶠ[𝓝 x] fun z => f (extChartAt 𝓘(ℝ, E) q z)) (v : E) :
    dfun h x v = fderiv ℝ f (extChartAt 𝓘(ℝ, E) q x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) q) x v) := by
  have hφ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) q) x :=
    mdifferentiableAt_extChartAt hx
  have hfm : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) f (extChartAt 𝓘(ℝ, E) q x) :=
    mdifferentiableAt_iff_differentiableAt.2 hf
  unfold dfun
  rw [he.mfderiv_eq]
  have e : (fun z => f (extChartAt 𝓘(ℝ, E) q z)) = f ∘ (extChartAt 𝓘(ℝ, E) q) := rfl
  rw [e, mfderiv_comp x hfm hφ, mfderiv_eq_fderiv]
  rfl

/-- `τ ∘ φ_q⁻¹` is `C¹` on `φ_q(U ∩ src_q)` (written `target ∩ φ_q⁻¹⁻¹ U`). -/
theorem tl_contDiffOn_chart {U : Set N} {τ : N → ℝ}
    (hτ : ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 τ U) (q : N) :
    ContDiffOn ℝ 1 (fun y => τ ((extChartAt 𝓘(ℝ, E) q).symm y))
      ((extChartAt 𝓘(ℝ, E) q).target ∩ (extChartAt 𝓘(ℝ, E) q).symm ⁻¹' U) := by
  rw [← contMDiffOn_iff_contDiffOn]
  exact hτ.comp ((contMDiffOn_extChartAt_symm q).mono inter_subset_left) (fun y hy => hy.2)

lemma tl_isOpen_chartU {U : Set N} (hU : IsOpen U) (q : N) :
    IsOpen ((extChartAt 𝓘(ℝ, E) q).target ∩ (extChartAt 𝓘(ℝ, E) q).symm ⁻¹' U) :=
  (continuousOn_extChartAt_symm q).isOpen_inter_preimage (isOpen_extChartAt_target q) hU

/-- `dτ_x(v) = D(τ ∘ φ_q⁻¹)(φ_q x)(Dφ_q(x) v)` for `x ∈ U ∩ src_q`, `U` open, `τ` `C¹` on `U`. -/
theorem tl_dfun_eq {U : Set N} (hU : IsOpen U) {τ : N → ℝ}
    (hτ : ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 τ U) {q x : N} (hx : x ∈ (chartAt E q).source)
    (hxU : x ∈ U) (v : E) :
    dfun τ x v = fderiv ℝ (fun y => τ ((extChartAt 𝓘(ℝ, E) q).symm y)) (extChartAt 𝓘(ℝ, E) q x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) q) x v) := by
  refine tl_dfun_chart hx ?_ ?_ v
  · have hmem : extChartAt 𝓘(ℝ, E) q x ∈
        (extChartAt 𝓘(ℝ, E) q).target ∩ (extChartAt 𝓘(ℝ, E) q).symm ⁻¹' U :=
      ⟨ch_mem_target q hx, by rw [mem_preimage, ch_left_inv q hx]; exact hxU⟩
    exact ((tl_contDiffOn_chart hτ q).contDiffAt
      ((tl_isOpen_chartU hU q).mem_nhds hmem)).differentiableAt one_ne_zero
  · filter_upwards [(chartAt E q).open_source.mem_nhds hx] with z hz
    rw [ch_left_inv q hz]

/-- `FutCausal` read in the chart at `q` (the chart form of `futCausal_chart`, without `OneChart`). -/
theorem tl_futCausal_chart (S : MSpacetime E N) {q x : N} (hx : x ∈ (chartAt E q).source)
    (v : E) :
    (hRep S.g q (extChartAt 𝓘(ℝ, E) q x) (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) q) x v)
        (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) q) x v) ≤ 0 ∧
      hRep S.g q (extChartAt 𝓘(ℝ, E) q x) (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) q) x v)
        (chartRep S.T q (extChartAt 𝓘(ℝ, E) q x)) < 0) ↔ S.FutCausal x v := by
  rw [ld_chartRep_apply_chart _ _ hx, chart_g (S := S) hx v v, chart_g (S := S) hx v (S.T x)]
  rfl


/-- Chart form of `pos_on_perp` at `x ∈ M ∩ src_q`. -/
theorem tl_perp_chart (S : MSpacetime E N) {q x : N} (hx : x ∈ (chartAt E q).source)
    (hxM : x ∈ S.M) (w : E)
    (h0 : hRep S.g q (extChartAt 𝓘(ℝ, E) q x) w (chartRep S.T q (extChartAt 𝓘(ℝ, E) q x)) = 0)
    (hw : w ≠ 0) : 0 < hRep S.g q (extChartAt 𝓘(ℝ, E) q x) w w := by
  obtain ⟨v, rfl⟩ : ∃ v : E, mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) q) x v = w :=
    ⟨_, ld_mfderiv_chart_symm q hx w⟩
  rw [ld_chartRep_apply_chart _ _ hx, chart_g (S := S) hx v (S.T x)] at h0
  rw [chart_g (S := S) hx v v]
  refine S.pos_on_perp x hxM v h0 fun hv => hw ?_
  rw [hv]; exact map_zero _

/-- **① `tl_cone_pos` (the registered stop): uniform positivity of `dτ` on the future cone over a
compact set, in the preferred chart at `q`.** `τ` temporal on an open `U ⊆ M`; `W ⊆ φ_q(U ∩ src_q)`
a set on which the chart representatives `hRep g q` and `chartRep T q` are continuous (as
`LocallyOneChart` provides); `K ⊆ W` compact. Then one `c > 0` gives
`dτ_x(v) ≥ c ‖Dφ_q(x) v‖` for every `x` with `φ_q x ∈ K` and every future-causal `v` at `x`
(norm of the chart-at-`q` components, in `E`). -/
theorem tl_cone_pos [FiniteDimensional ℝ E] (S : MSpacetime E N) {U : Set N} (hU : IsOpen U)
    (hUM : U ⊆ S.M) {τ : N → ℝ} (hτ : S.IsTemporalOn U τ) (q : N) {W : Set E}
    (hWU : W ⊆ (extChartAt 𝓘(ℝ, E) q).target ∩ (extChartAt 𝓘(ℝ, E) q).symm ⁻¹' U)
    (hg : ContinuousOn (hRep S.g q) W) (hT : ContinuousOn (chartRep S.T q) W)
    {K : Set E} (hK : IsCompact K) (hKW : K ⊆ W) :
    ∃ c > 0, ∀ x ∈ (chartAt E q).source, extChartAt 𝓘(ℝ, E) q x ∈ K → ∀ v : E,
      S.FutCausal x v → c * ‖dchart q x v‖ ≤ dfun τ x v := by
  set F : E → ℝ := fun y => τ ((extChartAt 𝓘(ℝ, E) q).symm y) with hF
  have hO := tl_isOpen_chartU (E := E) hU q
  have hDc : ContinuousOn (fun y => fderiv ℝ F y) K :=
    (((tl_contDiffOn_chart hτ.1 q).continuousOn_fderiv_of_isOpen hO le_rfl).mono
      (hKW.trans hWU))
  -- a point of `K` is `φ_q x` with `x ∈ U ∩ src_q`
  have hpt : ∀ y ∈ K, ∃ x ∈ (chartAt E q).source, x ∈ U ∧ extChartAt 𝓘(ℝ, E) q x = y := by
    intro y hy
    obtain ⟨hyt, hyU⟩ := hWU (hKW hy)
    exact ⟨_, ch_symm_mem q hyt, hyU, ch_right_inv q hyt⟩
  obtain ⟨c, hc, hcb⟩ := tl_cone_bound_vs hK (hg.mono hKW) (hT.mono hKW) hDc
    (fun y hy w h0 hw => by
      obtain ⟨x, hx, hxU, rfl⟩ := hpt y hy
      exact tl_perp_chart S hx (hUM hxU) w h0 hw)
    (fun y hy w h1 h2 => by
      obtain ⟨x, hx, hxU, rfl⟩ := hpt y hy
      obtain ⟨v, rfl⟩ : ∃ v : E, mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) q) x v = w :=
        ⟨_, ld_mfderiv_chart_symm q hx w⟩
      have hv := (tl_futCausal_chart S hx v).1 ⟨h1, h2⟩
      have := hτ.2 x hxU v hv
      rwa [tl_dfun_eq hU hτ.1 hx hxU v] at this)
  refine ⟨c, hc, fun x hx hxK v hv => ?_⟩
  obtain ⟨hyt, hyU⟩ := hWU (hKW hxK)
  have hxU : x ∈ U := by rw [mem_preimage, ch_left_inv q hx] at hyU; exact hyU
  obtain ⟨h1, h2⟩ := (tl_futCausal_chart S hx v).2 hv
  rw [tl_dfun_eq hU hτ.1 hx hxU v]
  exact hcb _ hxK _ h1 h2

/-- `d(τ + δψ) = dτ + δ dψ` at a point where both are differentiable. -/
theorem tl_dfun_add_smul {τ ψ : N → ℝ} {x : N}
    (hτ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) τ x) (hψ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) ψ x)
    (δ : ℝ) (v : E) : dfun (τ + δ • ψ) x v = dfun τ x v + δ * dfun ψ x v := by
  unfold dfun
  rw [(hτ.hasMFDerivAt.add (hψ.hasMFDerivAt.const_smul δ)).mfderiv]
  rfl

/-! ### The bump on `N` -/

/-- **`tl_bump`: a `C¹` bump on `N` at `q`.** For an open `O ∋ φ_q q` inside the chart target there
are `R > 0` with `closedBall (φ_q q) R ⊆ O` and `ψ : N → ℝ`, `C¹` on all of `N`, with `ψ q = 1`,
`ψ ≠ 0` only at points `x ∈ src_q` with `φ_q x ∈ ball (φ_q q) R`, and `C ≥ 0` with
`|dψ_x(v)| ≤ C ‖Dφ_q(x) v‖` on `src_q` and `dψ_x = 0` unless `x ∈ src_q`, `φ_q x ∈ closedBall`.
Built from Mathlib's `ContDiffBump` in the chart, extended by `0` (`Set.indicator`). `T2Space N`
makes `φ_q⁻¹(closedBall)` closed, which is what makes `ψ` smooth across the chart boundary. -/
theorem tl_bump [FiniteDimensional ℝ E] [T2Space N] (q : N) {O : Set E} (hO : IsOpen O)
    (hqO : extChartAt 𝓘(ℝ, E) q q ∈ O) (hOt : O ⊆ (extChartAt 𝓘(ℝ, E) q).target) :
    ∃ R > 0, closedBall (extChartAt 𝓘(ℝ, E) q q) R ⊆ O ∧
      ∃ ψ : N → ℝ, ContMDiff 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 ψ ∧ ψ q = 1 ∧
        (∀ x, ψ x ≠ 0 → x ∈ (chartAt E q).source ∧
          extChartAt 𝓘(ℝ, E) q x ∈ ball (extChartAt 𝓘(ℝ, E) q q) R) ∧
        ∃ C ≥ 0, (∀ x ∈ (chartAt E q).source, ∀ v : E, |dfun ψ x v| ≤ C * ‖dchart q x v‖) ∧
          (∀ x, (x ∈ (chartAt E q).source →
            extChartAt 𝓘(ℝ, E) q x ∉ closedBall (extChartAt 𝓘(ℝ, E) q q) R) →
              ∀ v : E, dfun ψ x v = 0) := by
  set φ := extChartAt 𝓘(ℝ, E) q with hφdef
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.1 hO _ hqO
  set R := ε / 2 with hR
  have hR0 : 0 < R := by positivity
  have hRO : closedBall (φ q) R ⊆ O :=
    (closedBall_subset_ball (by linarith)).trans hball
  let b : ContDiffBump (φ q) := ⟨R / 2, R, by positivity, by linarith⟩
  set ψ : N → ℝ := (chartAt E q).source.indicator (fun x => b (φ x)) with hψ
  set Kn : Set N := φ.symm '' closedBall (φ q) R with hKn
  have hKnc : IsCompact Kn := (isCompact_closedBall _ _).image_of_continuousOn
    ((continuousOn_extChartAt_symm q).mono (hRO.trans hOt))
  have hKncl : IsClosed Kn := hKnc.isClosed
  have hsupp : ∀ x, ψ x ≠ 0 → x ∈ (chartAt E q).source ∧ φ x ∈ ball (φ q) R := by
    intro x hx
    by_cases hxs : x ∈ (chartAt E q).source
    · refine ⟨hxs, ?_⟩
      rw [hψ, indicator_of_mem hxs] at hx
      have : φ x ∈ Function.support b := hx
      rwa [b.support_eq] at this
    · rw [hψ, indicator_of_notMem hxs] at hx; exact absurd rfl hx
  have hKn_of : ∀ x, ψ x ≠ 0 → x ∈ Kn := by
    intro x hx
    obtain ⟨hxs, hxb⟩ := hsupp x hx
    exact ⟨φ x, ball_subset_closedBall hxb, ch_left_inv q hxs⟩
  have hzero : ∀ x ∉ Kn, ψ =ᶠ[𝓝 x] fun _ => (0:ℝ) := by
    intro x hx
    filter_upwards [hKncl.isOpen_compl.mem_nhds hx] with z hz
    by_contra h; exact hz (hKn_of z h)
  have hloc : ∀ x ∈ (chartAt E q).source, ψ =ᶠ[𝓝 x] fun z => b (φ z) := by
    intro x hx
    filter_upwards [(chartAt E q).open_source.mem_nhds hx] with z hz
    rw [hψ, indicator_of_mem hz]
  have hKn_src : ∀ x, x ∉ (chartAt E q).source → x ∉ Kn := by
    rintro x hx ⟨y, hy, rfl⟩
    exact hx (ch_symm_mem q (hOt (hRO hy)))
  have hbd : ContDiff ℝ 1 b := b.contDiff
  refine ⟨R, hR0, hRO, ψ, ?_, ?_, hsupp, ?_⟩
  · intro x
    by_cases hx : x ∈ (chartAt E q).source
    · have h1 : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 (fun z => b (φ z)) x :=
        hbd.contMDiff.contMDiffAt.comp x (contMDiffAt_extChartAt' hx)
      exact h1.congr_of_eventuallyEq (hloc x hx)
    · exact contMDiffAt_const.congr_of_eventuallyEq (hzero x (hKn_src x hx))
  · rw [hψ, indicator_of_mem (mem_chart_source E q)]
    exact b.one_of_mem_closedBall (mem_closedBall_self (by positivity))
  · obtain ⟨C, hC⟩ := (hbd.continuous_fderiv one_ne_zero).bounded_above_of_compact_support
      (b.hasCompactSupport.fderiv ℝ)
    have hC0 : 0 ≤ C := (norm_nonneg _).trans (hC 0)
    refine ⟨C, hC0, fun x hx v => ?_, fun x hx v => ?_⟩
    · rw [tl_dfun_chart hx (hbd.differentiable one_ne_zero _) (hloc x hx) v]
      calc |fderiv ℝ b (φ x) (dchart q x v)| ≤ ‖fderiv ℝ b (φ x)‖ * ‖dchart q x v‖ :=
            (fderiv ℝ b (φ x)).le_opNorm _
        _ ≤ C * ‖dchart q x v‖ := by gcongr; exact hC _
    · have hxK : x ∉ Kn := by
        by_cases hxs : x ∈ (chartAt E q).source
        · rintro ⟨y, hy, rfl⟩
          have hyt := hOt (hRO hy)
          exact hx hxs (by rw [ch_right_inv q hyt]; exact hy)
        · exact hKn_src x hxs
      unfold dfun
      rw [(hzero x hxK).mfderiv_eq, mfderiv_const]
      rfl

/-- **`tl_bump_temporal`.** `τ` temporal on an open `U`; `ψ` a `C¹` function with
`|dψ_x(v)| ≤ C ‖Dφ_q(x) v‖` on `src_q`, `dψ_x = 0` off `φ_q⁻¹(closedBall (φ_q q) R)`, and
`dτ_x(v) ≥ c ‖Dφ_q(x) v‖` on future-causal `v` over that closed ball (`tl_cone_pos`). Then for
`|δ| C < c`, `τ + δψ` is temporal on `U`. -/
theorem tl_bump_temporal (S : MSpacetime E N) {U : Set N} (hU : IsOpen U) {τ : N → ℝ}
    (hτ : S.IsTemporalOn U τ) (q : N) {R c C : ℝ} {ψ : N → ℝ}
    (hψ : ContMDiff 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 ψ)
    (hcone : ∀ x ∈ (chartAt E q).source,
      extChartAt 𝓘(ℝ, E) q x ∈ closedBall (extChartAt 𝓘(ℝ, E) q q) R → ∀ v : E,
        S.FutCausal x v → c * ‖dchart q x v‖ ≤ dfun τ x v)
    (hC : ∀ x ∈ (chartAt E q).source, ∀ v : E, |dfun ψ x v| ≤ C * ‖dchart q x v‖)
    (h0 : ∀ x, (x ∈ (chartAt E q).source →
      extChartAt 𝓘(ℝ, E) q x ∉ closedBall (extChartAt 𝓘(ℝ, E) q q) R) →
        ∀ v : E, dfun ψ x v = 0)
    {δ : ℝ} (hδ : |δ| * C < c) : S.IsTemporalOn U (τ + δ • ψ) := by
  refine ⟨?_, fun x hxU v hv => ?_⟩
  · have h2 : ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 (fun x => δ * ψ x) U :=
      (contMDiffOn_const.mul hψ.contMDiffOn)
    exact hτ.1.add h2
  have hτd : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) τ x :=
    (hτ.1.contMDiffAt (hU.mem_nhds hxU)).mdifferentiableAt one_ne_zero
  rw [tl_dfun_add_smul hτd (hψ.mdifferentiableAt one_ne_zero) δ v]
  have hpos := hτ.2 x hxU v hv
  by_cases hin : x ∈ (chartAt E q).source ∧
      extChartAt 𝓘(ℝ, E) q x ∈ closedBall (extChartAt 𝓘(ℝ, E) q q) R
  · have h1 := hcone x hin.1 hin.2 v hv
    have h2 := hC x hin.1 v
    have h3 : -(|δ| * (C * ‖dchart q x v‖)) ≤ δ * dfun ψ x v := by
      have := neg_abs_le (δ * dfun ψ x v)
      rw [abs_mul] at this
      nlinarith [abs_nonneg δ]
    rcases (norm_nonneg (dchart q x v)).eq_or_lt with hn | hn
    · rw [← hn] at h3; simp at h3; linarith
    · have : |δ| * C * ‖dchart q x v‖ < c * ‖dchart q x v‖ := by gcongr
      nlinarith
  · rw [h0 x (fun hs hb => hin ⟨hs, hb⟩) v]; simpa using hpos

/-- **`cor:threefold` (iv), 2iv-b, core form (BUILT).** On a `LocallyOneChart` spacetime over a
Hausdorff `N` with finite-dimensional model `E`: let `τ` be temporal on an open `U ⊆ M`, `q ∈ U`,
`V ∋ q` open and `p ∉ V`. Then there is `δ₀ > 0` such that for every `δ ∈ (−δ₀, δ₀)` some `τ'`
is temporal on `U`, equals `τ` outside `V`, and has `τ'(q) − τ'(p) = τ(q) − τ(p) + δ`. -/
theorem tl_iv_b [FiniteDimensional ℝ E] [T2Space N] (S : MSpacetime E N)
    (hL : S.LocallyOneChart) {U : Set N} (hU : IsOpen U) (hUM : U ⊆ S.M) {τ : N → ℝ}
    (hτ : S.IsTemporalOn U τ) {p q : N} (hq : q ∈ U) {V : Set N} (hV : IsOpen V) (hqV : q ∈ V)
    (hpV : p ∉ V) :
    ∃ δ₀ > 0, ∀ δ ∈ Ioo (-δ₀) δ₀, ∃ τ' : N → ℝ, S.IsTemporalOn U τ' ∧
      (∀ x ∉ V, τ' x = τ x) ∧ τ' q - τ' p = τ q - τ p + δ := by
  obtain ⟨W0, hW0, hqW0, -, hg, hT⟩ := hL q (hUM hq)
  set φ := extChartAt 𝓘(ℝ, E) q with hφ
  set O : Set E := W0 ∩ (φ.target ∩ φ.symm ⁻¹' (U ∩ V)) with hOdef
  have hO : IsOpen O := hW0.inter ((continuousOn_extChartAt_symm q).isOpen_inter_preimage
    (isOpen_extChartAt_target q) (hU.inter hV))
  have hqO : φ q ∈ O := ⟨hqW0, mem_extChartAt_target q, by
    show φ.symm (φ q) ∈ U ∩ V
    rw [hφ, extChartAt_to_inv]; exact ⟨hq, hqV⟩⟩
  obtain ⟨R, hR0, hRO, ψ, hψ, hψq, hsupp, C, hC0, hC, h0⟩ :=
    tl_bump q hO hqO (fun y hy => hy.2.1)
  obtain ⟨c, hc, hcone⟩ := tl_cone_pos S hU hUM hτ q (W := O)
    (fun y hy => ⟨hy.2.1, hy.2.2.1⟩) (hg.continuousOn.mono inter_subset_left)
    (hT.mono inter_subset_left) (isCompact_closedBall _ _) hRO
  have hoff : ∀ x ∉ V, ψ x = 0 := by
    intro x hx
    by_contra h
    obtain ⟨hxs, hxb⟩ := hsupp x h
    have := (hRO (ball_subset_closedBall hxb)).2.2.2
    rw [ch_left_inv q hxs] at this
    exact hx this
  refine ⟨c / (C + 1), by positivity, fun δ hδ => ⟨τ + δ • ψ, ?_, ?_, ?_⟩⟩
  · refine tl_bump_temporal S hU hτ q hψ hcone hC h0 ?_
    have h1 : |δ| < c / (C + 1) := abs_lt.2 hδ
    rw [lt_div_iff₀ (by linarith)] at h1
    nlinarith [abs_nonneg δ]
  · intro x hx
    simp [hoff x hx]
  · simp [hψq, hoff p hpV]; ring

/-- **`cor:threefold` (iv), 2iv-b (BUILT).** `τ` temporal on `M` (`LocallyOneChart`, `N` Hausdorff,
`E` finite-dimensional), `p → q` a causal curve (a non-empty chain of causal steps), `V ∋ q` any open
set. Then the separation `τ(q) − τ(p)` can be moved to every value of an open interval about it by
temporal functions equal to `τ` outside `V`. (`p ∉ V` is arranged by shrinking `V` to `V \ {p}`,
using `p ≠ q`, which holds since `τ` rises strictly along the chain.) -/
theorem tl_cor_threefold_iv_b [FiniteDimensional ℝ E] [T2Space N] (S : MSpacetime E N)
    (hL : S.LocallyOneChart) {τ : N → ℝ} (hτ : S.IsTemporalOn S.M τ) {p q : N}
    (hpq : Relation.TransGen S.CStep p q) {V : Set N} (hV : IsOpen V) (hqV : q ∈ V) :
    ∃ δ₀ > 0, ∀ δ ∈ Ioo (-δ₀) δ₀, ∃ τ' : N → ℝ, S.IsTemporalOn S.M τ' ∧
      (∀ x ∉ V, τ' x = τ x) ∧ τ' q - τ' p = τ q - τ p + δ := by
  have key : ∀ {a b : N}, Relation.TransGen S.CStep a b → τ a < τ b ∧ b ∈ S.M := by
    intro a b h
    induction h with
    | single h => exact ⟨S.td_temporal_cstep hτ h, (S.cstep_mem h).2⟩
    | tail _ h ih => exact ⟨ih.1.trans (S.td_temporal_cstep hτ h), (S.cstep_mem h).2⟩
  obtain ⟨hlt, hqM⟩ := key hpq
  have hne : p ≠ q := fun h => (h ▸ hlt).false
  obtain ⟨δ₀, hδ₀, H⟩ := S.tl_iv_b hL S.isOpen_M subset_rfl hτ hqM (hV.inter isOpen_compl_singleton)
    ⟨hqV, fun h => hne (mem_singleton_iff.1 h).symm⟩ (fun h => h.2 rfl)
  refine ⟨δ₀, hδ₀, fun δ hδ => ?_⟩
  obtain ⟨τ', h1, h2, h3⟩ := H δ hδ
  exact ⟨τ', h1, fun x hx => h2 x fun h => hx h.1, h3⟩

/-- **2iv-b as an interval (BUILT).** Under `tl_cor_threefold_iv_b`'s hypotheses, the set of
separations `τ'(q) − τ'(p)` of temporal functions equal to `τ` outside `V` contains an open interval
about `τ(q) − τ(p)`: the separation is not fixed by the geometry. -/
theorem tl_separation_interval [FiniteDimensional ℝ E] [T2Space N] (S : MSpacetime E N)
    (hL : S.LocallyOneChart) {τ : N → ℝ} (hτ : S.IsTemporalOn S.M τ) {p q : N}
    (hpq : Relation.TransGen S.CStep p q) {V : Set N} (hV : IsOpen V) (hqV : q ∈ V) :
    ∃ δ₀ > 0, Ioo (τ q - τ p - δ₀) (τ q - τ p + δ₀) ⊆
      {s | ∃ τ' : N → ℝ, S.IsTemporalOn S.M τ' ∧ (∀ x ∉ V, τ' x = τ x) ∧ τ' q - τ' p = s} := by
  obtain ⟨δ₀, hδ₀, H⟩ := S.tl_cor_threefold_iv_b hL hτ hpq hV hqV
  refine ⟨δ₀, hδ₀, fun s hs => ?_⟩
  obtain ⟨τ', h1, h2, h3⟩ := H (s - (τ q - τ p)) ⟨by linarith [hs.1], by linarith [hs.2]⟩
  exact ⟨τ', h1, h2, by rw [h3]; ring⟩

end MSpacetime
end ThreefoldLocal

namespace NModel
open Model Manifold ContinuousLinearMap

/-- **`τ = U + V` is temporal on `minkN` (BUILT; campaign 104 used only that it rises along steps).**
`τ = (fst + snd) ∘ φ` is `C¹` (`φ` is a chart, `src = Pt`), and by the chain rule through `φ`,
`dτ_x(v) = (Dφ v)_U + (Dφ v)_V`, positive on future-causal `v` (`futCausal_chart`, `ch_chartSp_eq`,
`futCausal_iff`). -/
theorem tl_minkN_temporal :
    minkN.IsTemporalOn minkN.M (fun x => (φ x).1 + (φ x).2) := by
  set L : P →L[ℝ] ℝ := fst ℝ ℝ ℝ + snd ℝ ℝ ℝ with hL
  have hLf : (fun y : P => y.1 + y.2) = ⇑L := by funext y; simp [hL]
  refine ⟨?_, fun x _ v hv => ?_⟩
  · have h1 : ContMDiffOn 𝓘(ℝ, P) 𝓘(ℝ, P) 1 (extChartAt 𝓘(ℝ, P) p₀) univ := by
      rw [← source_eq]; exact contMDiffOn_extChartAt
    have h2 := L.contDiff.contMDiff.comp_contMDiffOn h1 (n := 1)
    exact h2.congr (fun x _ => by simp [hL, φ])
  · have e := MSpacetime.tl_dfun_chart (q := p₀) (src x)
      (h := fun x => (φ x).1 + (φ x).2) (f := fun y : P => y.1 + y.2)
      (by rw [hLf]; exact L.differentiableAt) (Filter.Eventually.of_forall fun _ => rfl) v
    rw [e, hLf, L.fderiv]
    have hc := (MSpacetime.futCausal_chart ch_oneChart (src x) v).2 hv
    rw [ch_chartSp_eq] at hc
    have hc' := (futCausal_iff _ (dchart p₀ x v)).1 hc
    show 0 < L (dchart p₀ x v)
    simpa [hL] using hc'.2.2

/-- `φ` is continuous on `Pt`. -/
lemma tl_φ_continuous : Continuous φ := by
  have h := continuousOn_extChartAt (I := 𝓘(ℝ, P)) p₀
  rw [extChartAt_source, source_eq] at h
  exact continuousOn_univ.1 h

/-- **③ The witness (BUILT).** On `Pt` with `minkN`, take `to_cor_1c`'s null pair `p = γN 0`,
`q = γN 1` (causally related, not chronologically related, joined by a null generator) and
`τ = U + V` read through `φ`. For every `r > 0` there is a second temporal function `τ'`, equal to
`τ` off the coordinate ball `V = φ⁻¹(ball (φ q) r)`, whose separation `τ'(q) − τ'(p)` differs from
`τ(q) − τ(p)`. -/
theorem tl_witness {r : ℝ} (hr : 0 < r) :
    minkN.Cau (to_γN 0) (to_γN 1) ∧ ¬ minkN.Chr (to_γN 0) (to_γN 1) ∧
    ∃ τ₁ τ₂ : Pt → ℝ, τ₁ = (fun x => (φ x).1 + (φ x).2) ∧
      minkN.IsTemporalOn minkN.M τ₁ ∧ minkN.IsTemporalOn minkN.M τ₂ ∧
      (∀ x ∉ φ ⁻¹' ball (φ (to_γN 1)) r, τ₂ x = τ₁ x) ∧
      τ₂ (to_γN 1) - τ₂ (to_γN 0) ≠ τ₁ (to_γN 1) - τ₁ (to_γN 0) := by
  obtain ⟨-, -, -, hcau, hchr, -⟩ := to_cor_1c
  obtain ⟨-, hT, -⟩ := td_cor_1c_hyp
  obtain ⟨δ₀, hδ₀, H⟩ := minkN.tl_cor_threefold_iv_b me_locallyOneChart tl_minkN_temporal hT
    (isOpen_ball.preimage tl_φ_continuous) (mem_ball_self hr)
  obtain ⟨τ', h1, h2, h3⟩ := H (δ₀ / 2) ⟨by linarith, by linarith⟩
  refine ⟨hcau, hchr, _, τ', rfl, tl_minkN_temporal, h1, h2, ?_⟩
  rw [h3]; intro h; linarith

end NModel


#print axioms MSpacetime.me_futCauchy_of_cauchy_N
#print axioms MSpacetime.mk_isOpen_D
#print axioms MSpacetime.mk_pushup'
#print axioms MSpacetime.mk_curve_inext_D
#print axioms MSpacetime.ch_isCauchy_VN
#print axioms MSpacetime.mh_temporalD_chr
#print axioms MSpacetime.mh_future_step
#print axioms MSpacetime.mh_past_step
#print axioms MSpacetime.mh_hint
#print axioms MSpacetime.mh_hcl
#print axioms MSpacetime.mh_blowup
#print axioms MSpacetime.mh_sublevelProper
#print axioms MSpacetime.mh_slice_lower_limit
#print axioms MSpacetime.mh_slice_upper_limit
#print axioms MSpacetime.mh_slice_kuratowski
#print axioms MSpacetime.mh_causal_alignment_gh_N
#print axioms Model.hl_cauchy
#print axioms NModel.me_locallyOneChart
#print axioms NModel.me_charts_differ
#print axioms NModel.mh_witness_hypotheses
#print axioms NModel.mh_witness_headline_G
#print axioms NModel.mh_witness_headline

#print axioms TCF.tc_pointwise
#print axioms TCF.tc_tendsto
#print axioms TCF.tc_tendsto_limit
#print axioms mc_preconnected_inter_frontier
#print axioms MSpacetime.mc_lower_limit
#print axioms MSpacetime.mc_upper_limit
#print axioms MSpacetime.mc_cone_kuratowski_N
#print axioms mc_frameHyp_pullback
#print axioms MSpacetime.mc_frameHyp_toChart
#print axioms MSpacetime.mc_frameHyp_ofChart
#print axioms MSpacetime.mc_tangency_N
#print axioms MSpacetime.mc_tangency_limit_N
#print axioms MSpacetime.mc_tangency_at_N
#print axioms mc_covCh_change
#print axioms mc_chart_change
#print axioms mc_covCh_comp_chart
#print axioms Model.mc_frameHyp_gM
#print axioms NModel.mc_witness_frameHyp
#print axioms NModel.mc_witness_tangency_holds
#print axioms NModel.mc_witness_tangency_at
#print axioms NModel.mc_witness_tangency_fails
#print axioms NModel.mc_witness_cones
#print axioms mc_tendsto_limit_aux
#print axioms mc_tCC_eq
#print axioms NModel.tCC_neg_p₀

#print axioms mx_preimage_frontier
#print axioms mx_preimage_closure
#print axioms MSpacetime.mx_frontier_JpastSet
#print axioms MSpacetime.mx_range_subset_M
#print axioms MSpacetime.mx_H_eq_boundary
#print axioms MSpacetime.mx_prop_causal_alignment
#print axioms NModel.mx_ι_isOpenEmbedding
#print axioms NModel.mx_ι_contMDiff
#print axioms NModel.mx_dι_eq
#print axioms NModel.mx_witnessExt
#print axioms NModel.mx_mem_mink_D_JA
#print axioms NModel.mx_preimage_Ipast_scri
#print axioms NModel.mx_scri_subset_frontier
#print axioms NModel.mx_witness_boundary
#print axioms NModel.mx_witness_headline

#print axioms MSpacetime.cd_chr_of_mem_closure_Jpast
#print axioms MSpacetime.cd_mem_closure_sublevel
#print axioms MSpacetime.cd_closure_Jpast_subset_D
#print axioms MSpacetime.cd_closure_Jpast_inter_H
#print axioms MSpacetime.cd_cone_disjoint
#print axioms MSpacetime.cd_prop_causal_alignment
#print axioms NModel.cd_frontier_nonempty
#print axioms NModel.cd_witness

#print axioms MSpacetime.dn_slice_subset_JpastSet
#print axioms MSpacetime.dn_BH_inter_slice
#print axioms MSpacetime.dn_slice_inter_frontier
#print axioms MSpacetime.dn_slice_inter_H
#print axioms MSpacetime.dn_subset_BH_inter_slice
#print axioms MSpacetime.dn_cor_densities
#print axioms NModel.dn_preimage_Jpast_scri
#print axioms NModel.dn_witness

-- campaign 103: copied from AlongConnection.lean (ac_)
#print axioms ac_metric_singularity_along
#print axioms ac_const_of_vel_zero
#print axioms ac_lapse_pos_forces_point
#print axioms ACModel.ac_boost_generator
#print axioms ACModel.ac_boost_isometry
#print axioms ACModel.ac_witness
#print axioms ACModel.ac_witness_no_positive_lapse
#print axioms ACModel.ac_lapse_pos_nonvacuous

-- campaign 103 (new)
#print axioms MSpacetime.to_Ifut_subset_interior
#print axioms MSpacetime.to_frontier_not_mem_Ifut
#print axioms MSpacetime.to_strict_null_order
#print axioms Model.to_cstep_of_le
#print axioms Model.to_cau_iff
#print axioms Model.to_chr_iff
#print axioms Model.to_mem_frontier_quadrant
#print axioms NModel.to_ψ_injective
#print axioms NModel.to_cau_iff_N
#print axioms NModel.to_chr_iff_N
#print axioms NModel.to_φ_gen
#print axioms NModel.to_Jfut_gen
#print axioms NModel.to_gen_mem_frontier
#print axioms NModel.to_witness_order
#print axioms NModel.to_witness_order_e
#print axioms NModel.to_γN_eq
#print axioms NModel.to_tco_γN
#print axioms NModel.to_vel_γN
#print axioms NModel.to_gE_γN
#print axioms NModel.to_σN_Δx
#print axioms NModel.to_σN_Δτ
#print axioms NModel.to_cor_1c


-- campaign 104 (new)
#print axioms MSpacetime.td_ne_of_transGen
#print axioms MSpacetime.td_cor_threefold_i
#print axioms MSpacetime.td_transGen_of_cau_ne
#print axioms MSpacetime.td_noClosed_of_lt
#print axioms MSpacetime.td_temporal_curve_lt
#print axioms MSpacetime.td_temporal_cstep
#print axioms MSpacetime.td_noClosed_of_temporal
#print axioms MSpacetime.td_noClosed_of_temporalOn
#print axioms MSpacetime.td_noClosed_D
#print axioms Model.td_cstep_sum_lt
#print axioms NModel.td_minkN_cstep_lt
#print axioms NModel.td_minkN_noClosed
#print axioms NModel.td_cor_1c_hyp


-- campaign 109 (new)
#print axioms tl_cone_bound_vs
#print axioms MSpacetime.tl_dfun_chart
#print axioms MSpacetime.tl_contDiffOn_chart
#print axioms MSpacetime.tl_isOpen_chartU
#print axioms MSpacetime.tl_dfun_eq
#print axioms MSpacetime.tl_futCausal_chart
#print axioms MSpacetime.tl_perp_chart
#print axioms MSpacetime.tl_cone_pos
#print axioms MSpacetime.tl_dfun_add_smul
#print axioms MSpacetime.tl_bump
#print axioms MSpacetime.tl_bump_temporal
#print axioms MSpacetime.tl_iv_b
#print axioms MSpacetime.tl_cor_threefold_iv_b
#print axioms MSpacetime.tl_separation_interval
#print axioms NModel.tl_minkN_temporal
#print axioms NModel.tl_φ_continuous
#print axioms NModel.tl_witness

end ShadowProbe.ThreefoldLocalProbe

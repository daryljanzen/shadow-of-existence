import Mathlib

/-!
# Probe `r7649+71.1` (campaign 84, route (c)): the headline on a manifold whose region lies in one
chart, by global-chart transport to campaign 81's single-chart theorem

Registration: `computations/formalisation/r7649_71_campaign84/PREDICTION.md` (route, estimate and risks:
`r7647_71_campaign84/PREDICTION.md`, `SCOPING.md`). Nothing imports this file, and it imports no other
probe.

## Copied

* Campaign 81's `probes/HeadlineHypotheses.lean`, all of it (the `V`-side chain, `hl_*` names kept, and
  its Rindler `Model`), with the c1 edits below. Its own provenance (campaigns 60, 74, 75, 78, 79) is as
  recorded there.
* Campaign 68's `probes/LieDerivManifold.lean`: `chartRep`, `hRep`, `ld_hRep_apply`,
  `ld_mdifferentiableAt_symm`, `ld_mfderiv_symm_chart`, `ld_mfderiv_chart_symm`,
  `ld_chartRep_apply_chart`, `ld_h_eq_hRep` (unchanged, about 75 lines). Nothing else of 66/68 is needed.

## c1, the `V` side — BUILT

* **Fields weakened.** `Spacetime.cont_g : ContinuousOn g M`, `cont_T : ContinuousOn T M` (were
  `Continuous` on all of `V`); every `LocallyLipschitz S.g` hypothesis (push-up, `hint`, `hcl`, the
  headline) is now `LocallyLipschitzOn S.M S.g`. Re-checked proofs: `cont_gvw` became the pointwise
  `cont_gvw_at` (+ `contAt_T`); `isOpen_timelikePairs`, the four `eventually` facts of `local_pushup`,
  `safe_uniform` and one `cont_T.tendsto` in `hl_past_extension` now use continuity only at points of
  `M`; `rev`, `restrict` and the model (`continuousOn_const`, `hl_lipschitz`) were adapted. The whole
  copied chain and `Model.hl_model_headline` rebuild unchanged in statement.
* **Localised headline.** `Spacetime.ch_causal_alignment_gh_loc`: for any set `W`, with
  `hHM : 𝓗⁺ ∩ W ⊆ M` in place of `𝓗⁺ ⊆ M`:
  `SublevelProperIn J W Θ ∧ KLi (slice) ∩ W = 𝓗⁺ ∩ W ∧ KLs (slice) ∩ W = 𝓗⁺ ∩ W`.
  *Checked:* `hHM` is used only at horizon points of `W`; neither `W` open nor `M ⊆ W` is needed.
  `ch_causal_alignment_gh_univ` recovers the global form at `W = univ`. Model re-checked (it is
  `W = univ`: `hl_model_headline`, unchanged).

## c2, the manifold side — BUILT

*Intrinsic* (Mathlib's manifold notions on `N`, `[ChartedSpace E N] [IsManifold 𝓘(ℝ,E) 1 N]`; the
tangent space `T_xN` is, by Mathlib's definition, `E` read in the preferred chart at `x`):
`MSpacetime` (open `M`, sections `g`, `T`, symmetric, `T` timelike and `g > 0` on `T^⊥` on `M`),
`FutTimelike`/`FutCausal`, the velocity `vel γ t = mfderiv γ t 1`, `TStep`/`CStep` (curves `ℝ → N`,
`ContMDiff 1`, `mfderiv` velocity future-timelike/causal on `[0,1]`, inside `M`), `Chr`, `Cau`, `I⁻`, `J⁻`,
`D`, `H = frontier_N J⁻(J)`, `slice`, `SublevelProper`, `KLi`/`KLs` (generalised to any topological
space), `IsTemporalOn U` (`ContMDiffOn` + `mfderiv`), `InextCausalCurveIn U` (`MDifferentiableAt`,
`mfderiv`, limits in `N`), `IsCauchyTemporalOn U`.

*Chart-defined* (only here): the hypothesis `OneChart S p₀` — `M ⊆ (chartAt E p₀).source`,
`hRep g p₀` is `C¹` and `chartRep T p₀` is continuous on `φ(M)`, `φ = extChartAt p₀` — and the chart
spacetime `chartSp hC : Spacetime E` (`M_V = φ(M)`, `g_V = hRep g p₀`, `T_V = chartRep T p₀`). The
registered "g `C¹` in that chart" is exactly `OneChart.g_C1`.

* **The `TStep` transfer (the registered likeliest stop) — BUILT.** `ch_squash` (an `arctan` squash
  `σ : ℝ → (-δ, 1+δ)`, `σ 0 = 0`, `σ 1 = 1`, `σ' > 0`), `ch_curve_NV`/`ch_curve_VN` (`β = φ ∘ γ ∘ σ`,
  `γ = φ⁻¹ ∘ β ∘ σ`; `mfderiv`/`deriv` identified by `mfderiv_comp` + `mfderiv_eq_fderiv`:
  `ch_hasDerivAt_chart`, `ch_vel_symm`), then `MSpacetime.ch_tstep_iff`:
  `x, y ∈ src → (S.TStep x y ↔ (chartSp hC).TStep (φ x) (φ y))`, and the same for `CStep`.
* **Relations and sets — BUILT.** `ch_chr_iff`, `ch_cau_iff`, `ch_mem_D_iff`, `ch_mem_JpastSet_iff`,
  `ch_mem_chartD_iff`, `ch_isOpen_D`; topology through the chart: `ch_mem_closure_iff`,
  `ch_mem_frontier_iff`, `ch_mem_KLi_iff`, `ch_mem_KLs_iff`; `ch_mem_H_iff` (`𝓗⁺` inside the chart:
  `x ∈ 𝓗⁺_N ↔ φ x ∈ 𝓗⁺_V`, this is where the localisation `W = target` enters).
* **Temporal and Cauchy — BUILT.** `ch_isCauchy_NV` (`IsCauchyTemporalOn (D_N) Θ` gives the chart
  exterior's `IsCauchyTemporal (Θ ∘ φ⁻¹)`), and its converse `ch_isCauchy_VN`.
* **The headline — BUILT.** `MSpacetime.ch_causal_alignment_gh_N (hC : S.OneChart p₀)
  (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
  (hHM : S.H J ⊆ S.M) (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
  S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J` — everything in `N`.
* **Non-vacuity — BUILT, with a non-identity chart and `Dφ ≠ id`.** `NModel`: `Pt` (a copy of `ℝ²`)
  with the two-chart atlas `{id, (t,x) ↦ (t−x, t+x)}`; `φ = extChartAt p₀` is the null-coordinate map
  (`ch_chart_ne_id`), and `mfderiv φ` is not the identity on `{t < 0}` (`ch_dchart_ne_id`). The chart
  spacetime is campaign 81's `mink` (`ch_chartSp_eq`); `ch_witness_hypotheses` discharges every
  hypothesis of `ch_causal_alignment_gh_N` on `Pt`; `ch_witness_headline`: `𝓗⁺_N ≠ ∅`
  (`= φ⁻¹{U = 0}`) and, for `Θ₀ ∘ φ` and `Θf ∘ φ`, properness and `KLi = KLs = 𝓗⁺_N`.

## Not claimed

That P1's Kruskal / Oppenheimer–Snyder exteriors lie in one chart (an unformalised topological fact),
and the multi-chart case (route (b), whose missing piece is the inextendible extension on `N`).

`#print axioms` at the end. `set_option synthInstance.maxHeartbeats 400000` inside `Model` (copied).
-/

open Set Filter Topology Metric

namespace ShadowProbe.ChartHeadlineProbe

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

omit hOD hmono in
/-- Under the two hypotheses, `𝓗⁺ = closure D \ D`. -/
theorem hl_H_eq_closure_diff (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) :
    S.H J = closure (S.D J) \ S.D J := by
  ext p
  constructor
  · intro hp
    refine ⟨hcl (frontier_subset_closure hp), fun hpD => hp.2 ?_⟩
    exact interior_maximal (S.hl_D_subset_JpastSet J)
      (isOpen_biUnion fun z _ => S.hl_isOpen_Ipast z) hpD
  · rintro ⟨h1, h2⟩
    exact ⟨closure_mono (S.hl_D_subset_JpastSet J) h1, fun hi => h2 (hint hi)⟩

/-! ### The slices `S_τ` accumulate on `𝓗⁺` -/

omit hmono in
/-- **Slices, upper limit.** Adapted `Θ`: `Θ (O τ) = τ + c`, and `Θ` increases along every `≪`
ending on the worldline. Then `Ls S_τ ⊆ closure J⁻(𝒥⁺) \ D`, and `⊆ 𝓗⁺` given `int J⁻(𝒥⁺) ⊆ D`. -/
theorem hl_slice_upper_limit {Θ : V → ℝ} {c : ℝ} (hadapt : ∀ τ, Θ (O τ) = τ + c)
    (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ)) :
    KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J ∧
    (interior (S.JpastSet J) ⊆ S.D J → KLs (S.slice J Θ) ⊆ S.H J) := by
  have key : KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J := by
    intro y hy
    refine ⟨?_, fun hyD => ?_⟩
    · rw [mem_closure_iff_nhds]
      intro U hU
      obtain ⟨τ, z, hz, hzU⟩ := (hy U hU).exists
      exact ⟨z, hzU, S.hl_D_subset_JpastSet J hz.1⟩
    · rw [← hOD] at hyD
      simp only [IpastSet, mem_iUnion] at hyD
      obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hyD
      have hfr := hy _ ((S.hl_isOpen_Ipast (O σ)).mem_nhds hσ)
      obtain ⟨τ, hτ, z, hz, hzI⟩ := frequently_atTop.1 hfr (σ + c)
      have := hΘ z σ hzI
      rw [hadapt, hz.2] at this
      linarith
  refine ⟨key, fun hint y hy => ?_⟩
  obtain ⟨h1, h2⟩ := key hy
  exact ⟨h1, fun hi => h2 (hint hi)⟩

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

/-- **Step 2 + inextendibility.** For `q ∈ M ∩ closure D \ D` there is a future-inextendible
causal curve of `D` (a `FutInextCurve` of `Dsp`), `γ t = q - ε e^{-t} T(q)`, with `γ t → q`, every
`γ t ≪ q`, and `γ t ≪ γ t'` for `0 ≤ t < t'`. -/
theorem hl_curve {q : V} (hqM : q ∈ S.M) (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) :
    ∃ c : (S.Dsp J).FutInextCurve, Tendsto c.γ atTop (𝓝 q) ∧
      (∀ t, 0 ≤ t → S.Chr (c.γ t) q) ∧
      (∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) := by
  obtain ⟨ε, hε0, hε⟩ := S.seg_timelike hqM
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
  have hchr_q : ∀ t, 0 ≤ t → S.Chr (S.seg q (r t)) q := by
    intro t ht
    have h := S.seg_tstep hε (hr_mem t ht).1 (hr_mem t ht).2 le_rfl
    rw [seg_zero] at h
    exact Relation.TransGen.single h
  have hchr : ∀ t t', 0 ≤ t → t < t' → S.Chr (S.seg q (r t)) (S.seg q (r t')) := by
    intro t t' ht htt
    exact Relation.TransGen.single
      (S.seg_tstep hε (hr_mem t ht).1 (hr_lt t t' htt) (hr_mem t' (by linarith)).2.le)
  have hmemD : ∀ t, 0 ≤ t → S.seg q (r t) ∈ S.D J := fun t ht =>
    S.hl_Ipast_subset_D J hqcl (hchr_q t ht)
  have hlim : Tendsto (fun t => S.seg q (r t)) atTop (𝓝 q) := by
    have h := ((tendsto_const_nhds (x := -ε)).mul Real.tendsto_exp_neg_atTop_nhds_zero).smul_const
      (S.T q) |>.const_add q
    simpa [seg, hr] using h
  have hderiv : ∀ t, HasDerivAt (fun t => S.seg q (r t)) ((ε * Real.exp (-t)) • S.T q) t := by
    intro t
    have h := ((((hasDerivAt_neg t).exp).const_mul (-ε)).smul_const (S.T q)).const_add q
    have e : ε * Real.exp (-t) = -ε * (Real.exp (-t) * -1) := by ring
    rw [e]; exact h
  have hcont : ContinuousOn (fun t => S.seg q (r t)) (Ici 0) :=
    (continuous_const.add
      ((continuous_const.mul (Real.continuous_exp.comp continuous_neg)).smul
        continuous_const)).continuousOn
  refine ⟨⟨fun t => S.seg q (r t), hcont, hmemD, ∅, fun a b => by simp, fun t ht _ => ?_, ?_⟩,
    hlim, hchr_q, hchr⟩
  · refine ⟨(hderiv t).differentiableAt, ?_⟩
    rw [(hderiv t).deriv]
    have hc : 0 < ε * Real.exp (-t) := mul_pos hε0 (Real.exp_pos _)
    obtain ⟨-, h1, h2⟩ := hε _ ⟨(hr_mem t ht.le).1, (hr_mem t ht.le).2.le⟩
    show S.g _ _ _ ≤ 0 ∧ S.g _ _ (S.T _) < 0
    simp only [map_smul, smul_apply, smul_eq_mul]
    refine ⟨?_, mul_neg_of_pos_of_neg hc h2⟩
    have : 0 < (ε * Real.exp (-t)) * (ε * Real.exp (-t)) := mul_pos hc hc
    nlinarith
  · rintro ⟨p, hp, hpl⟩
    exact hqD (tendsto_nhds_unique hlim hpl ▸ hp)

/-- `Θ` (temporal on `D`) increases strictly along the curve of `hl_curve`. -/
lemma curve_mono {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) (c : (S.Dsp J).FutInextCurve)
    (hc : ∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) {t t' : ℝ} (ht : 0 ≤ t)
    (htt : t ≤ t') : Θ (c.γ t) ≤ Θ (c.γ t') := by
  rcases htt.lt_or_eq with h | h
  · exact (S.hl_temporalD_chr J hΘ (hc t t' ht h) (c.mem t' (by linarith))).le
  · rw [h]

/-! ### Step 4: properness from the Cauchy property -/

/-- **Step 4, `Θ → ∞` at `q`.** For `q ∈ M ∩ closure D \ D` and every `T'`, a neighbourhood `U` of
`q` has `Θ > T'` on `U ∩ D`: pick `r = γ t` with `Θ r = max (T'+1) (Θ (γ 0))`; `I⁺(r)` works. -/
theorem hl_blowup_cauchy {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V} (hqM : q ∈ S.M)
    (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) (T' : ℝ) :
    ∃ U ∈ 𝓝 q, ∀ x ∈ U ∩ S.D J, T' < Θ x := by
  obtain ⟨c, -, hchr_q, -⟩ := S.hl_curve J hqM hqcl hqD
  obtain ⟨t, ht, hta⟩ := hΘ.2 c (max (T' + 1) (Θ (c.γ 0))) (le_max_right _ _)
  refine ⟨{y | S.Chr (c.γ t) y}, (S.hl_isOpen_Ifut _).mem_nhds (hchr_q t ht), fun x hx => ?_⟩
  have h := S.hl_temporalD_chr J hΘ.1 hx.1 hx.2
  have := le_max_left (T' + 1) (Θ (c.γ 0))
  linarith

/-- **Step 4, `SublevelProper` derived.** Campaign 74's properness hypothesis follows from the
future Cauchy property, `int J⁻(𝒥⁺) ⊆ D` (campaign 72's `hint`) and `𝓗⁺ ⊆ M`. -/
theorem hl_sublevelProper (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M)
    {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) : S.SublevelProper J Θ := by
  intro T' p hp
  by_contra hpD
  have hpcl : p ∈ closure (S.D J) := closure_mono (fun x hx => hx.1) hp
  have hpH : p ∈ S.H J :=
    ⟨closure_mono (S.hl_D_subset_JpastSet J) hpcl, fun hi => hpD (hint hi)⟩
  obtain ⟨U, hU, hUT⟩ := S.hl_blowup_cauchy J hΘ (hHM hpH) hpcl hpD T'
  obtain ⟨x, hxU, hxD, hxT⟩ := mem_closure_iff_nhds.1 hp U hU
  linarith [hUT x ⟨hxU, hxD⟩]

/-! ### Step 5: the slice lower limit, with no properness and no local connectedness -/

/-- **Step 5, pointwise.** `q ∈ M ∩ closure D \ D ⟹ q ∈ KLi(S_τ)`: the tail of the curve lies in
`U`, and the levels `τ ≥ Θ(γ t₀)` are hit on that tail (Cauchy property + monotonicity of `Θ`). -/
theorem hl_mem_KLi_slice {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V}
    (hqM : q ∈ S.M) (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) :
    q ∈ KLi (S.slice J Θ) := by
  intro U hU
  obtain ⟨c, hlim, -, hchr⟩ := S.hl_curve J hqM hqcl hqD
  obtain ⟨t₀, ht₀⟩ := eventually_atTop.1 ((hlim.eventually hU).and (eventually_ge_atTop 0))
  have ht₀0 : 0 ≤ t₀ := (ht₀ t₀ le_rfl).2
  filter_upwards [eventually_ge_atTop (Θ (c.γ t₀))] with τ hτ
  obtain ⟨t, ht0, htτ⟩ :=
    hΘ.2 c τ ((S.curve_mono J hΘ.1 c hchr le_rfl ht₀0).trans hτ)
  have htt : t₀ ≤ t := by
    by_contra h
    rw [not_le] at h
    have := S.hl_temporalD_chr J hΘ.1 (hchr t t₀ ht0 h) (c.mem t₀ ht₀0)
    linarith
  exact ⟨c.γ t, ⟨c.mem t ht0, htτ⟩, (ht₀ t htt).1⟩

/-- **Step 5, `𝓗⁺ ⊆ KLi(S_τ)`.** Hypotheses: campaign 72's `hcl`, `𝓗⁺ ⊆ M`, and `Θ` Cauchy temporal
on `D` (future form). No `SublevelProper`, no `LocConnAt`, no separate continuity hypothesis.
Campaign 78: BUILT under the repaired `IsTemporal` (satisfiability: see `hl_slice_kuratowski`). -/
theorem hl_slice_lower_limit (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) :
    S.H J ⊆ KLi (S.slice J Θ) := fun _ hq =>
  S.hl_mem_KLi_slice J hΘ (hHM hq) (hcl (frontier_subset_closure hq)) (S.hl_not_mem_D_of_H J hq)

/-! ### Step 6: `KLi(S_τ) = KLs(S_τ) = 𝓗⁺` under the proposition's hypotheses -/

section Slices
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
include hOD

/-- **Step 6.** For `Θ` Cauchy temporal on `D` (future form), adapted to a future-directed
observer worldline `O` with `I⁻(O) = D`, and campaign 72's `hcl`, `hint`, plus `𝓗⁺ ⊆ M`:
`KLi(S_τ) = KLs(S_τ) = 𝓗⁺`. No properness, no local connectedness, no continuity hypothesis.

*Campaign 78:* re-derived under the repaired `IsTemporal` (BUILT). *Joint satisfiability:* `Θ` is
constrained on `D` only, so `r7641+71.1`'s contradiction (continuity of `Θ` at `q ∈ 𝓗⁺` vs.
`Θ → ∞` along `𝓝[D] q`) is no longer derivable; campaign 81: the model with `𝓗⁺ ≠ ∅` is in this
file (`Model.hl_model_headline`). -/
theorem hl_slice_kuratowski (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).FutCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  have h1 := S.hl_slice_lower_limit J hcl hHM hΘ
  have h2 := (S.hl_slice_upper_limit hOD hadapt
    (fun x σ h => S.hl_temporalD_chr J hΘ.1 h (S.hl_observer_mem_D hOD hmono σ))).2 hint
  have h3 := hl_KLi_subset_KLs (S.slice J Θ)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

/-- **`prop:causal-alignment`, both halves**: under the same hypotheses, properness holds (so
campaign 74's hypothesis is a consequence) and the slices converge to `𝓗⁺`.

*Campaign 78:* re-derived under the repaired `IsTemporal` (BUILT); joint satisfiability as for
`hl_slice_kuratowski` (no continuity of `Θ` off `D` is assumed; model: `Model.hl_model_headline`). -/
theorem hl_causal_alignment (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).FutCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J :=
  ⟨S.hl_sublevelProper J hint hHM hΘ, S.hl_slice_kuratowski hOD hmono hcl hint hHM hΘ hadapt⟩

end Slices

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

/-- ② on the exterior: `(Dsp J).IsCauchyTemporal Θ → (Dsp J).FutCauchyTemporal Θ`. -/
theorem hl_futCauchy_of_cauchy_D {Θ : V → ℝ} (hΘ : (S.Dsp J).IsCauchyTemporal Θ) :
    (S.Dsp J).FutCauchyTemporal Θ :=
  (S.Dsp J).hl_futCauchy_of_cauchy hΘ

section SlicesGH
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
include hOD

/-- **`prop:causal-alignment` under campaign 60's own definition** (`IsCauchyTemporal`, two-sided,
with the repaired `IsTemporal`): properness, and `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`. BUILT, via ②.

*Joint satisfiability:* the hypotheses constrain `Θ` on `D` only, so the vacuity mechanism of
`r7641+71.1` no longer applies. Campaign 81: kept as `hl_causal_alignment_gh₀`; the hypothesis-light
form `hl_causal_alignment_gh` derives `hcl`, `hint`, and the Rindler model in this file satisfies
all of its hypotheses with `𝓗⁺ ≠ ∅` (`Model.hl_model_headline`). -/
theorem hl_causal_alignment_gh₀ (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).IsCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J :=
  S.hl_causal_alignment hOD hmono hcl hint hHM (S.hl_futCauchy_of_cauchy_D J hΘ) hadapt

end SlicesGH

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

/-- **① `hint` derived (BUILT).** For locally Lipschitz `g` and `J ⊆ M`: `int J⁻(J) ⊆ I⁻(J) = D`.
A short future step `y` from `x` stays in the (open) interior, `x ≪ y ≤ z ∈ J`, and the dual
push-up `≪ ∘ ≤ ⊆ ≪` (campaign 60's `cs_pushup'`) gives `x ≪ z`. -/
theorem hl_hint (hL : LocallyLipschitzOn S.M S.g) (hJM : J ⊆ S.M) :
    interior (S.JpastSet J) ⊆ S.D J := by
  intro x hx
  obtain ⟨y, hy, hxy⟩ := S.hl_future_step (S.hl_JpastSet_subset_M J hJM (interior_subset hx))
    (isOpen_interior.mem_nhds hx)
  have hy' := interior_subset hy
  simp only [JpastSet, mem_iUnion] at hy'
  obtain ⟨z, hz, hyz⟩ := hy'
  simp only [D, IpastSet, mem_iUnion]
  exact ⟨z, hz, S.hl_pushup' hL hxy hyz⟩

/-- `J⁻(J) ⊆ closure D`: past steps `y ≪ x ≤ z ∈ J` give `y ≪ z`, and `y → x`. -/
theorem hl_JpastSet_subset_closure_D (hL : LocallyLipschitzOn S.M S.g) (hJM : J ⊆ S.M) :
    S.JpastSet J ⊆ closure (S.D J) := by
  intro x hx
  have hxM := S.hl_JpastSet_subset_M J hJM hx
  simp only [JpastSet, mem_iUnion] at hx
  obtain ⟨z, hz, hxz⟩ := hx
  rw [mem_closure_iff_nhds]
  intro N hN
  obtain ⟨y, hy, hyx⟩ := S.hl_past_step hxM hN
  refine ⟨y, hy, ?_⟩
  simp only [D, IpastSet, mem_iUnion]
  exact ⟨z, hz, S.hl_pushup' hL hyx hxz⟩

/-- **① `hcl` derived (BUILT).** For locally Lipschitz `g` and `J ⊆ M`:
`closure J⁻(J) ⊆ closure D`. (`J ⊆ M` handles the reflexive case `x = z ∈ J`.) -/
theorem hl_hcl (hL : LocallyLipschitzOn S.M S.g) (hJM : J ⊆ S.M) :
    closure (S.JpastSet J) ⊆ closure (S.D J) :=
  closure_minimal (S.hl_JpastSet_subset_closure_D J hL hJM) isClosed_closure

section Headline
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
include hOD

/-- **The headline restated (BUILT).** `prop:causal-alignment` under the two-sided Cauchy property,
with campaign 72's `hcl` and `hint` replaced by `hL : LocallyLipschitz g` and `hJM : J ⊆ M`.
*Satisfiable:* every hypothesis is discharged in the Rindler model below (`Model.hl_model_headline`),
with `𝓗⁺ = {U = 0} ≠ ∅`. -/
theorem hl_causal_alignment_gh (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hL : LocallyLipschitzOn S.M S.g) (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).IsCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J :=
  S.hl_causal_alignment_gh₀ hOD hmono (S.hl_hcl J hL hJM) (S.hl_hint J hL hJM) hHM hΘ hadapt

end Headline

/-! ## Campaign 84 c1: the headline localised to an open set `W` (the chart target)

`𝓗⁺ = ∂J⁻(J)` is a frontier in the ambient `V`. For a chart spacetime `M ⊆ W = φ(U)`, `∂_V` can gain
points of `∂W` (limits escaping the chart). The localised headline asks `𝓗⁺ ∩ W ⊆ M` only, and concludes
on `W`. *Checked:* the proof uses `hHM` only at horizon points of `W` (`hl_blowup_cauchy` at `p ∈ W`;
`hl_mem_KLi_slice` at `q ∈ 𝓗⁺ ∩ W`); the upper limit `KLs ⊆ 𝓗⁺` and `hint`/`hcl` do not use it at
all. Neither openness of `W` nor `M ⊆ W` is needed by the proof. -/

/-- **Properness relative to `W`.** -/
def SublevelProperIn (W : Set V) (Θ : V → ℝ) : Prop :=
  ∀ T : ℝ, closure {x | x ∈ S.D J ∧ Θ x ≤ T} ∩ W ⊆ S.D J

/-- c1: properness on `W` from the future Cauchy property, `hint` and `𝓗⁺ ∩ W ⊆ M`. -/
theorem ch_sublevelProper_loc (hint : interior (S.JpastSet J) ⊆ S.D J) {W : Set V}
    (hHM : S.H J ∩ W ⊆ S.M) {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) :
    S.SublevelProperIn J W Θ := by
  rintro T' p ⟨hp, hpW⟩
  by_contra hpD
  have hpcl : p ∈ closure (S.D J) := closure_mono (fun x hx => hx.1) hp
  have hpH : p ∈ S.H J :=
    ⟨closure_mono (S.hl_D_subset_JpastSet J) hpcl, fun hi => hpD (hint hi)⟩
  obtain ⟨U, hU, hUT⟩ := S.hl_blowup_cauchy J hΘ (hHM ⟨hpH, hpW⟩) hpcl hpD T'
  obtain ⟨x, hxU, hxD, hxT⟩ := mem_closure_iff_nhds.1 hp U hU
  linarith [hUT x ⟨hxU, hxD⟩]

section HeadlineLoc
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
include hOD

/-- **c1 BUILT: the localised headline.** As `hl_causal_alignment_gh`, with `hL` now
`LocallyLipschitzOn M g` and `hHM : 𝓗⁺ ∩ W ⊆ M` for an arbitrary set `W`; the conclusions are read on
`W`. With `W = univ` it is `hl_causal_alignment_gh` (`ch_causal_alignment_gh_univ`). -/
theorem ch_causal_alignment_gh_loc (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hL : LocallyLipschitzOn S.M S.g) (hJM : J ⊆ S.M) {W : Set V} (hHM : S.H J ∩ W ⊆ S.M)
    {Θ : V → ℝ} {c : ℝ} (hΘ : (S.Dsp J).IsCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProperIn J W Θ ∧ KLi (S.slice J Θ) ∩ W = S.H J ∩ W ∧
      KLs (S.slice J Θ) ∩ W = S.H J ∩ W := by
  have hF := S.hl_futCauchy_of_cauchy_D J hΘ
  have hint := S.hl_hint J hL hJM
  have hcl := S.hl_hcl J hL hJM
  have h1 : S.H J ∩ W ⊆ KLi (S.slice J Θ) := fun q hq =>
    S.hl_mem_KLi_slice J hF (hHM hq) (hcl (frontier_subset_closure hq.1))
      (S.hl_not_mem_D_of_H J hq.1)
  have h2 := (S.hl_slice_upper_limit hOD hadapt
    (fun x σ h => S.hl_temporalD_chr J hF.1 h (S.hl_observer_mem_D hOD hmono σ))).2 hint
  have h3 := hl_KLi_subset_KLs (S.slice J Θ)
  refine ⟨S.ch_sublevelProper_loc J hint hHM hF, ?_, ?_⟩
  · exact Subset.antisymm (fun p hp => ⟨h2 (h3 hp.1), hp.2⟩) fun p hp => ⟨h1 hp, hp.2⟩
  · exact Subset.antisymm (fun p hp => ⟨h2 hp.1, hp.2⟩) fun p hp => ⟨h3 (h1 hp), hp.2⟩

/-- The localised headline at `W = univ` gives back the global one. -/
theorem ch_causal_alignment_gh_univ (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hL : LocallyLipschitzOn S.M S.g) (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M)
    {Θ : V → ℝ} {c : ℝ} (hΘ : (S.Dsp J).IsCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  obtain ⟨h1, h2, h3⟩ := ch_causal_alignment_gh_loc hOD hmono hL hJM (W := univ)
    (fun p hp => hHM hp.1) hΘ hadapt
  simp only [inter_univ] at h2 h3
  exact ⟨fun T => by simpa using h1 T, h2, h3⟩

end HeadlineLoc

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

/-- **(1) The model meets the geometric hypotheses of `cp_causal_alignment`, with `𝓗⁺ ≠ ∅`.** -/
theorem hl_model :
    mink.D (range O) = {p : P | p.1 < 0} ∧ mink.H (range O) = {p : P | p.1 = 0} ∧
    ((0, 0) : P) ∈ mink.H (range O) ∧
    mink.IpastSet (range O) = mink.D (range O) ∧
    (∀ s t : ℝ, s < t → mink.Chr (O s) (O t)) ∧
    closure (mink.JpastSet (range O)) ⊆ closure (mink.D (range O)) ∧
    interior (mink.JpastSet (range O)) ⊆ mink.D (range O) ∧
    mink.H (range O) ⊆ mink.M := by
  refine ⟨hl_D_eq, hl_H_eq, by rw [hl_H_eq]; rfl, rfl, hl_O_mono, ?_, ?_, subset_univ _⟩
  · rw [hl_JpastSet_eq, hl_D_eq]
  · rw [hl_JpastSet_eq, hl_D_eq]; exact interior_subset

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

/-! ## Campaign 81 ③: the end-to-end instantiation -/

/-- **Every hypothesis of `hl_causal_alignment_gh` holds in the model**, for every good `G`, with
the reparametrised observer `O'` of `GoodG.hl_adapted`. -/
theorem hl_model_hypotheses {G : ℝ → ℝ} (hG : GoodG G) :
    LocallyLipschitzOn mink.M mink.g ∧ range O ⊆ mink.M ∧ mink.H (range O) ⊆ mink.M ∧
    (mink.Dsp (range O)).IsCauchyTemporal (ThetaG G) ∧
    ∃ O' : ℝ → P, range O' = range O ∧ mink.IpastSet (range O') = mink.D (range O) ∧
      (∀ s t : ℝ, s < t → mink.Chr (O' s) (O' t)) ∧ ∀ τ, ThetaG G (O' τ) = τ + 0 :=
  ⟨hl_lipschitz, subset_univ _, subset_univ _, hl_cauchy hG, hG.hl_adapted⟩

/-- `hl_causal_alignment_gh` applied to the model, for any good profile `G`. -/
theorem hl_model_headline_G {G : ℝ → ℝ} (hG : GoodG G) :
    mink.SublevelProper (range O) (ThetaG G) ∧
    KLi (mink.slice (range O) (ThetaG G)) = {p : P | p.1 = 0} ∧
    KLs (mink.slice (range O) (ThetaG G)) = {p : P | p.1 = 0} := by
  obtain ⟨O', -, hOD, hmono, hadapt⟩ := hG.hl_adapted
  obtain ⟨h1, h2, h3⟩ := Spacetime.hl_causal_alignment_gh hOD hmono hl_lipschitz
    (subset_univ _) (subset_univ _) (hl_cauchy hG) hadapt
  rw [hl_H_eq] at h2 h3
  exact ⟨h1, h2, h3⟩

/-- **③ The headline, end to end (BUILT).** In 2D Minkowski space with `J` the Rindler worldline,
`D = {U < 0}`, `𝓗⁺ = {U = 0} ∋ (0,0)`, and for both the aligned `Θ₀ = −log(−U) + V` and the failing
`Θf = F(−U) + V`: properness, and `KLi(S_τ) = KLs(S_τ) = 𝓗⁺ = {U = 0}` — the conclusion of
`hl_causal_alignment_gh`, with every one of its hypotheses discharged in this file. -/
theorem hl_model_headline :
    mink.D (range O) = {p : P | p.1 < 0} ∧ mink.H (range O) = {p : P | p.1 = 0} ∧
    ((0, 0) : P) ∈ mink.H (range O) ∧
    (mink.SublevelProper (range O) Θ₀ ∧
      KLi (mink.slice (range O) Θ₀) = {p : P | p.1 = 0} ∧
      KLs (mink.slice (range O) Θ₀) = {p : P | p.1 = 0}) ∧
    (mink.SublevelProper (range O) Θf ∧
      KLi (mink.slice (range O) Θf) = {p : P | p.1 = 0} ∧
      KLs (mink.slice (range O) Θf) = {p : P | p.1 = 0}) :=
  ⟨hl_D_eq, hl_H_eq, by rw [hl_H_eq]; rfl, hl_model_headline_G goodG_log,
    hl_model_headline_G goodG_Ffail⟩

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

/-- **c2 BUILT: the headline on a manifold whose region lies in one chart.** For a manifold
spacetime `S` on `N` with `M ⊆ (chartAt E p₀).source`, `hRep g p₀` `C¹` and `chartRep T p₀`
continuous on `φ(M)` (`OneChart`), and the hypotheses of `hl_causal_alignment_gh` read on `N`
(intrinsic `≪`, `D`, `𝓗⁺ = ∂_N J⁻(J)`, Cauchy temporal `Θ` on `D` with `mfderiv`): properness, and
`KLi(S_τ) = KLs(S_τ) = 𝓗⁺`, all in `N`. Proof: transport to the chart spacetime and apply the
localised headline `ch_causal_alignment_gh_loc` with `W` the chart target. -/
theorem ch_causal_alignment_gh_N {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ} {c : ℝ}
    (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  have hsub := hC.sub
  have hJs : J ⊆ (chartAt E p₀).source := hJM.trans hsub
  have hOs : range O ⊆ (chartAt E p₀).source := by
    rintro _ ⟨τ, rfl⟩; exact hsub (S.chr_mem (hmono τ (τ + 1) (by linarith))).1
  have hOs' : ∀ τ, O τ ∈ (chartAt E p₀).source := fun τ => hOs ⟨τ, rfl⟩
  -- the chart-side hypotheses
  have hOD' : (chartSp hC).IpastSet (range fun τ => extChartAt 𝓘(ℝ, E) p₀ (O τ)) =
      (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J) := by
    have e : (range fun τ => extChartAt 𝓘(ℝ, E) p₀ (O τ)) = extChartAt 𝓘(ℝ, E) p₀ '' range O :=
      range_comp (extChartAt 𝓘(ℝ, E) p₀) O
    show (chartSp hC).D _ = _
    rw [e]
    ext u
    rw [ch_mem_chartD_iff hC hOs, ch_mem_chartD_iff hC hJs]
    have h' : S.D (range O) = S.D J := hOD
    rw [h']
  have hmono' : ∀ s t : ℝ, s < t →
      (chartSp hC).Chr (extChartAt 𝓘(ℝ, E) p₀ (O s)) (extChartAt 𝓘(ℝ, E) p₀ (O t)) :=
    fun s t h => (ch_chr_iff hC (hOs' s) (hOs' t)).1 (hmono s t h)
  have hHM' : (chartSp hC).H (extChartAt 𝓘(ℝ, E) p₀ '' J) ∩ (extChartAt 𝓘(ℝ, E) p₀).target ⊆
      (chartSp hC).M := by
    rintro u ⟨huH, hut⟩
    have hx := ch_symm_mem p₀ hut
    have h' := (ch_mem_H_iff hC hJs hx).2 (by rwa [ch_right_inv p₀ hut])
    exact ⟨_, hHM h', ch_right_inv p₀ hut⟩
  have hadapt' : ∀ τ, (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) (extChartAt 𝓘(ℝ, E) p₀ (O τ)) =
      τ + c := fun τ => by
    rw [Function.comp_apply, ch_left_inv p₀ (hOs' τ)]; exact hadapt τ
  obtain ⟨h1, h2, h3⟩ := Spacetime.ch_causal_alignment_gh_loc hOD' hmono' (ch_chart_lipschitz hC)
    (image_mono hJM) hHM' (ch_isCauchy_NV hC hJM hΘ) hadapt'
  -- back to `N`
  have hclJ : closure (S.JpastSet J) ⊆ S.M := by
    rw [closure_eq_interior_union_frontier]
    rintro x (hx | hx)
    · exact S.JpastSet_subset_M hJM (interior_subset hx)
    · exact hHM hx
  have hclD : closure (S.D J) ⊆ (chartAt E p₀).source :=
    (closure_mono (S.D_subset_JpastSet J)).trans (hclJ.trans hsub)
  have hslice : ∀ τ, ∀ x ∈ (chartAt E p₀).source, x ∈ S.slice J Θ τ ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈
      (chartSp hC).slice (extChartAt 𝓘(ℝ, E) p₀ '' J) (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) τ := by
    intro τ x hx
    show (x ∈ S.D J ∧ Θ x = τ) ↔ (_ ∈ (chartSp hC).D _ ∧ Θ ((extChartAt 𝓘(ℝ, E) p₀).symm _) = τ)
    rw [ch_left_inv p₀ hx, ch_mem_D_iff hC hJs hx]
  have hKLs : KLs (S.slice J Θ) ⊆ (chartAt E p₀).source :=
    (ch_KLs_subset_closure fun τ x hx => hx.1).trans hclD
  refine ⟨fun T p hp => ?_, ?_, ?_⟩
  · have hps : p ∈ (chartAt E p₀).source := hclD (closure_mono (fun x hx => hx.1) hp)
    have hcorr : ∀ x ∈ (chartAt E p₀).source, x ∈ {x | x ∈ S.D J ∧ Θ x ≤ T} ↔
        extChartAt 𝓘(ℝ, E) p₀ x ∈ {u | u ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J) ∧
          (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u ≤ T} := by
      intro x hx
      show (x ∈ S.D J ∧ Θ x ≤ T) ↔ (_ ∈ (chartSp hC).D _ ∧ Θ ((extChartAt 𝓘(ℝ, E) p₀).symm _) ≤ T)
      rw [ch_left_inv p₀ hx, ch_mem_D_iff hC hJs hx]
    exact (ch_mem_D_iff hC hJs hps).2
      (h1 T ⟨(ch_mem_closure_iff hcorr hps).1 hp, ch_mem_target p₀ hps⟩)
  · ext p
    constructor
    · intro hp
      have hps := hKLs (hl_KLi_subset_KLs _ hp)
      have h' : extChartAt 𝓘(ℝ, E) p₀ p ∈ KLi ((chartSp hC).slice (extChartAt 𝓘(ℝ, E) p₀ '' J)
          (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm)) ∩ (extChartAt 𝓘(ℝ, E) p₀).target :=
        ⟨(ch_mem_KLi_iff hslice hps).1 hp, ch_mem_target p₀ hps⟩
      rw [h2] at h'
      exact (ch_mem_H_iff hC hJs hps).2 h'.1
    · intro hp
      have hps := hsub (hHM hp)
      have h' : extChartAt 𝓘(ℝ, E) p₀ p ∈ (chartSp hC).H (extChartAt 𝓘(ℝ, E) p₀ '' J) ∩
          (extChartAt 𝓘(ℝ, E) p₀).target := ⟨(ch_mem_H_iff hC hJs hps).1 hp, ch_mem_target p₀ hps⟩
      rw [← h2] at h'
      exact (ch_mem_KLi_iff hslice hps).2 h'.1
  · ext p
    constructor
    · intro hp
      have hps := hKLs hp
      have h' : extChartAt 𝓘(ℝ, E) p₀ p ∈ KLs ((chartSp hC).slice (extChartAt 𝓘(ℝ, E) p₀ '' J)
          (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm)) ∩ (extChartAt 𝓘(ℝ, E) p₀).target :=
        ⟨(ch_mem_KLs_iff hslice hps).1 hp, ch_mem_target p₀ hps⟩
      rw [h3] at h'
      exact (ch_mem_H_iff hC hJs hps).2 h'.1
    · intro hp
      have hps := hsub (hHM hp)
      have h' : extChartAt 𝓘(ℝ, E) p₀ p ∈ (chartSp hC).H (extChartAt 𝓘(ℝ, E) p₀ '' J) ∩
          (extChartAt 𝓘(ℝ, E) p₀).target := ⟨(ch_mem_H_iff hC hJs hps).1 hp, ch_mem_target p₀ hps⟩
      rw [← h3] at h'
      exact (ch_mem_KLs_iff hslice hps).2 h'.1

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

end Manifold

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

/-- **c2 witness (BUILT): the headline on `Pt`, end to end, through the non-identity chart.**
`𝓗⁺_N = φ⁻¹{U = 0} ≠ ∅`, and for every good `G` (so for `Θ₀` and `Θf`): properness and
`KLi(S_τ) = KLs(S_τ) = 𝓗⁺_N`, from `ch_causal_alignment_gh_N`. -/
theorem ch_witness_headline_G {G : ℝ → ℝ} (hG : GoodG G) :
    (∀ x : Pt, x ∈ minkN.H JN ↔ (extChartAt 𝓘(ℝ, P) p₀ x).1 = 0) ∧ (minkN.H JN).Nonempty ∧
    minkN.SublevelProper JN (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
    KLi (minkN.slice JN (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN ∧
    KLs (minkN.slice JN (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN := by
  obtain ⟨O_N, hOD, hmono, hJM, hHM, hΘ, hadapt⟩ := ch_witness_hypotheses hG
  refine ⟨mem_H_N, ⟨ψ (0, 0), (mem_H_N _).2 (by rw [φψ])⟩,
    MSpacetime.ch_causal_alignment_gh_N ch_oneChart hOD hmono hJM hHM hΘ hadapt⟩

theorem ch_witness_headline :
    extChartAt 𝓘(ℝ, P) p₀ (mkPt 1 0) ≠ ((1, 0) : ℝ × ℝ) ∧
    (minkN.H JN).Nonempty ∧
    (minkN.SublevelProper JN (Θ₀ ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      KLi (minkN.slice JN (Θ₀ ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN ∧
      KLs (minkN.slice JN (Θ₀ ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN) ∧
    (minkN.SublevelProper JN (Θf ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      KLi (minkN.slice JN (Θf ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN ∧
      KLs (minkN.slice JN (Θf ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN) :=
  ⟨ch_chart_ne_id, (ch_witness_headline_G goodG_log).2.1, (ch_witness_headline_G goodG_log).2.2,
    (ch_witness_headline_G goodG_Ffail).2.2⟩

end NModel

#print axioms Spacetime.hl_pushup'
#print axioms Spacetime.hl_future_step
#print axioms Spacetime.hl_past_step
#print axioms Spacetime.hl_hint
#print axioms Spacetime.hl_hcl
#print axioms Spacetime.hl_causal_alignment_gh₀
#print axioms Spacetime.hl_causal_alignment_gh
#print axioms Spacetime.hl_cauchy_iff
#print axioms Model.hl_futCauchy
#print axioms Model.hl_pastCauchy
#print axioms Model.hl_cauchy
#print axioms Model.hl_model_hypotheses
#print axioms Model.hl_model_headline_G
#print axioms Model.hl_model_headline

#print axioms Spacetime.ch_causal_alignment_gh_loc
#print axioms Spacetime.ch_causal_alignment_gh_univ
#print axioms ch_squash
#print axioms MSpacetime.ch_tstep_iff
#print axioms MSpacetime.ch_chr_iff
#print axioms MSpacetime.ch_cau_iff
#print axioms MSpacetime.ch_mem_H_iff
#print axioms MSpacetime.ch_isCauchy_NV
#print axioms MSpacetime.ch_isCauchy_VN
#print axioms MSpacetime.ch_causal_alignment_gh_N
#print axioms NModel.ch_chart_ne_id
#print axioms NModel.ch_dchart_ne_id
#print axioms NModel.ch_chartSp_eq
#print axioms NModel.ch_witness_hypotheses
#print axioms NModel.ch_witness_headline_G
#print axioms NModel.ch_witness_headline

end ShadowProbe.ChartHeadlineProbe

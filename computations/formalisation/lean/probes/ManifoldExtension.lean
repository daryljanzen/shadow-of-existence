import Mathlib

/-!
# Probe `r7651+71` (campaign 85, route (b), first piece): the past-inextendible extension on a
multi-chart manifold `N`, and two-sided ⇒ future Cauchy on `N`

Registration: `computations/formalisation/r7651_71_campaign85/PREDICTION.md`. Nothing imports this
file, and it imports no other probe.

## Copied (trimmed) from campaign 84's `probes/ChartHeadline.lean`

* `V` side: `Spacetime` (fields as campaign 84's c1), `FutTimelike`, `TStep`, `contAt_T`,
  `cont_gvw_at`, `isOpen_timelikePairs`, `seg`, `seg_zero`, `seg_timelike`, `seg_tstep`, `Safe`,
  `safe_uniform` (tube lemma), `int_brk_fin`. Nothing of the causal-alignment chain or of `Model`.
* `ch_exists_Ioo`, `ch_squash`; campaign 68's `chartRep`, `hRep`, `ld_*`; chart bookkeeping
  `ch_mem_target`, `ch_left_inv`, `ch_symm_mem`, `ch_right_inv`, `ch_contAt`, `ch_vel_symm`.
* `MSpacetime` (intrinsic): `gE`, `FutTimelike`, `FutCausal`, `dfun`, `vel`, `TStep`,
  `IsTemporalOn`, `InextCausalCurveIn`, `IsCauchyTemporalOn`, `futTimelike_smul`, `tstep_mem`;
  `OneChart`, `isOpen_chartImage`, `chart_g`, `chartSp`, `futTimelike_chart(')`; `dchart`,
  `dchartInv`, `ch_curve_VN`, `ch_tstep_VN` (only the `V → N` half of `ch_tstep_iff` is needed).
* `NModel`: `Pt` with the two-chart atlas `{idH, nullH}` (preferred chart `idH` on `{t < 0}`,
  `nullH` on `{t ≥ 0}`), `minkN` (with `mink`'s three proofs inlined), `ch_dchart_eq`, `dinv_eq`,
  `hRep_eq`, `chartRep_eq` (base point `p₀`, chart `nullH`), `ψ`, `φψ`.

## NEW

1. **`LocallyOneChart S` — BUILT (definition).** `∀ p ∈ M, ∃ U : Set E, IsOpen U ∧ φ_p p ∈ U ∧
   U ⊆ φ_p '' (M ∩ src_p) ∧ ContDiffOn ℝ 1 (hRep S.g p) U ∧ ContinuousOn (chartRep S.T p) U`,
   `φ_p = extChartAt 𝓘(ℝ,E) p` the *preferred chart at `p`*. Passes to open `U ⊆ M`
   (`LocallyOneChart.restrict`, via `restrictM`). Only the continuity of `hRep g p` is used here
   (`chartSp` needs `ContinuousOn g`); the `C¹` is kept as registered (P1's smooth `g`).
2. **The local past step, through the limit point's own chart — BUILT** (the registered second
   likeliest stop). `MSpacetime.me_local_step (hL) (hq : q ∈ M) : ∃ f : N → N, ContinuousAt f q ∧
   f q ∈ M ∧ ∀ᶠ x in 𝓝 q, S.TStep (f x) x`: restrict `S` to `W = src_q ∩ φ_q⁻¹ U ∩ M`, which is
   `OneChart q`; take a uniform safe length `ℓ` of its chart spacetime at `φ_q q` (`safe_uniform`),
   `f x = φ_q⁻¹(φ_q x − ℓ T_V(φ_q x))`, transferred by `ch_tstep_VN`.
   *Route change (simplification, not a weakening):* the uniform drop `c > 0` near `x*` comes
   from continuity of `x ↦ Θ x − Θ (f x)` at `x*` (positive there because `Θ` strictly increases
   along `TStep_N`, `me_temporal_tstep`), so no bound on `dΘ` and no integral is needed.
3. **The drop and the vertices — BUILT.** `pastDrop Θ x = sSup {min 1 (Θ x − Θ y) | TStep_N y x}`
   (the `min` sits inside the `sup`, so the set is bounded; this is the registered `δ`);
   `nextV` chooses `y` with drop `> δ/2`; `mvert` the vertices; `mvert_no_limit`: no limit in `M`
   (eventually `δ(X k) ≥ min 1 (d/2)`, while `Θ (X k) − Θ (X (k+1)) → 0`).
   `me_past_sequence` (the registered reachable-negative form) is BUILT as a stepping stone.
4. **Gluing (the registered expected stop) — BUILT.** `gpoly γ u = γ ⌊u⌋₊ (⌊u⌋₊ + 1 − u)`,
   `gpoly_continuous` (any topological space), `vel_congr`, `vel_comp_add` (`mfderiv` of a
   translate). **`MSpacetime.me_past_extension`** (`hL : S.LocallyOneChart`,
   `hΘ : S.IsTemporalOn S.M Θ`, `hx : x ∈ S.M`):
   `∃ p : ℝ → N, Continuous p ∧ p 0 = x ∧ (∀ t ≤ 0, p t ∈ S.M) ∧ (∀ t < 0, Θ (p t) < Θ x) ∧
   (∀ t < 0, t ∉ range Int.cast → ContMDiffAt 𝓘(ℝ,ℝ) 𝓘(ℝ,E) 1 p t ∧ S.FutTimelike (p t) (vel p t))
   ∧ ¬ ∃ q ∈ S.M, Tendsto p atBot (𝓝 q)`.
5. **Two-sided ⇒ future Cauchy on `N` — BUILT.** New intrinsic `FutInextCurveIn U`,
   `FutCauchyTemporalOn U Θ` (the `N`-analogues of campaign 78's). **`me_futCauchy_of_cauchy_N`**
   `(hL) (hU : IsOpen U) (hUM : U ⊆ S.M) (hΘ : S.IsCauchyTemporalOn U Θ) :
   S.FutCauchyTemporalOn U Θ` (glue `me_past_extension` of `S.restrictM U` at `0`, as campaign 78).
   For `U = D J` it needs `IsOpen (D J)` on `N`, which is campaign 86's local kit (openness of
   `I⁻` on `N`); not stated here.
6. **Non-vacuity — BUILT IN PART.** On `NModel.Pt`: `me_locallyOneChart` (points with `t < 0` use
   `idH`, where `hRep g p = −dt² + dx²` and `chartRep T p = (1,0)` are computed through the
   non-identity `Dφ_p = nullInvL` on `{t ≥ 0}`, `me_dchart_neg`; points with `t ≥ 0` use `nullH`),
   `me_charts_differ` (two points with different preferred charts), `me_temporal_Θt`
   (`Θt = t`, `Θt_eq`, temporal on `M = Pt`, read in both charts), and `me_witness_extension`
   (the glued extension from every point of `Pt`). **Stop:** the Cauchy hypothesis of
   `me_futCauchy_of_cauchy_N` is *not* instantiated here (`me_witness_futCauchy_hyps` gives all
   its other hypotheses); campaign 84's `ch_witness_hypotheses` gives `IsCauchyTemporalOn (D JN)`
   on `Pt` but needs campaign 81's whole model chain and `IsOpen (D JN)`, about 2000 more copied
   lines, so it is not re-built.

`#print axioms` at the end. `set_option synthInstance.maxHeartbeats 400000` inside `NModel`.
-/

open Set Filter Topology Metric

namespace ShadowProbe.ManifoldExtensionProbe

/-! ## Copied (campaign 84, `probes/ChartHeadline.lean`): the `V`-side chart spacetime, trimmed -/

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

/-- One `C¹` future-timelike piece from `x` to `y`. -/
def TStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t)

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

/-- `Safe y ℓ`: on `r ∈ [-ℓ, 0]`, `y + r • T y ∈ M` and `T y` is future-timelike there. -/
def Safe (y : V) (ℓ : ℝ) : Prop :=
  ∀ r ∈ Icc (-ℓ) 0, S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y)

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

/-- The integers, as break points, are finite on compacts. -/
lemma int_brk_fin (a b : ℝ) : (range (Int.cast : ℤ → ℝ) ∩ Icc a b).Finite := by
  refine ((Set.finite_Icc ⌊a⌋ ⌈b⌉).image (Int.cast : ℤ → ℝ)).subset ?_
  rintro _ ⟨⟨z, rfl⟩, hz1, hz2⟩
  refine ⟨z, ⟨?_, ?_⟩, rfl⟩
  · exact Int.floor_le_iff.2 (by linarith)
  · exact Int.le_ceil_iff.2 (by linarith) 

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

lemma tstep_mem {x y : N} (h : S.TStep x y) : x ∈ S.M ∧ y ∈ S.M := by
  obtain ⟨γ, -, h0, h1, hγ⟩ := h
  exact ⟨h0 ▸ (hγ 0 ⟨le_rfl, zero_le_one⟩).1, h1 ▸ (hγ 1 ⟨zero_le_one, le_rfl⟩).1⟩

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

theorem ch_tstep_VN {u v : E} (h : (chartSp hC).TStep u v) :
    S.TStep ((extChartAt 𝓘(ℝ, E) p₀).symm u) ((extChartAt 𝓘(ℝ, E) p₀).symm v) := by
  obtain ⟨β, hβ, rfl, rfl, ht⟩ := h
  exact ch_curve_VN hC.sub (fun u hu w h => (futTimelike_chart' hC hu w).1 h)
    (fun x v c hc h => S.futTimelike_smul hc h) hβ ht

end MSpacetime

/-! ## NEW (campaign 85): the local one-chart hypothesis and the local past step -/

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


end Manifold

/-! ## Copied (campaign 84): the two-chart witness manifold `NModel.Pt` (trimmed; the `mink`
proofs inlined) -/

namespace NModel
open Manifold ContinuousLinearMap MSpacetime

set_option synthInstance.maxHeartbeats 400000

/-- Null coordinates `p = (U, V)`. -/
abbrev P := ℝ × ℝ

/-- `g = −dU dV` (symmetrised). -/
noncomputable def gM : P →L[ℝ] P →L[ℝ] ℝ :=
  (-(1/2 : ℝ)) • ((fst ℝ ℝ ℝ).smulRight (snd ℝ ℝ ℝ) + (snd ℝ ℝ ℝ).smulRight (fst ℝ ℝ ℝ))

lemma gM_apply (v w : P) : gM v w = -(v.1 * w.2 + v.2 * w.1) / 2 := by
  simp [gM]; ring

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

noncomputable def minkN : MSpacetime P Pt where
  M := univ
  isOpen_M := isOpen_univ
  g := gN
  symm := fun x v w => by
    show gN x v w = gN x w v
    unfold gN; split_ifs
    · rw [gTX_apply, gTX_apply]; ring
    · rw [gM_apply, gM_apply]; ring
  T := TN
  T_timelike := fun x _ => by
    show gN x (TN x) (TN x) < 0
    unfold gN TN; split_ifs
    · rw [gTX_apply]; norm_num
    · rw [gM_apply]; norm_num
  pos_on_perp := fun x _ v h hv => by
    change gN x v (TN x) = 0 at h
    show 0 < gN x v v
    unfold gN TN at *
    split_ifs at h ⊢
    · rw [gTX_apply] at h ⊢
      have h1 : v.1 = 0 := by linarith
      have h2 : v.2 ≠ 0 := fun h2 => hv (Prod.ext h1 h2)
      rw [h1]; nlinarith [sq_pos_of_ne_zero h2]
    · rw [gM_apply] at h ⊢
      have h2 : v.2 = -v.1 := by linarith
      have h1 : v.1 ≠ 0 := by
        intro h1; apply hv; ext
        · exact h1
        · rw [h2, h1]; simp
      rw [h2]; nlinarith [sq_pos_of_ne_zero h1]

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


/-- `φ⁻¹` (copied). -/
noncomputable def ψ : P → Pt := (extChartAt 𝓘(ℝ, P) p₀).symm

lemma φψ (y : P) : extChartAt 𝓘(ℝ, P) p₀ (ψ y) = y :=
  (extChartAt 𝓘(ℝ, P) p₀).right_inv (by rw [target_eq]; exact mem_univ y)

/-! ### NEW (campaign 85): every point's own chart, and the time function -/

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

/-- `(U, V) ↦ (U + V)/2`. -/
noncomputable def fL : P →L[ℝ] ℝ := (1/2 : ℝ) • ((fst ℝ ℝ ℝ) + (snd ℝ ℝ ℝ))

/-- **The time function** `Θt = t`, written through the global null chart `φ = nullH`. -/
noncomputable def Θt (x : Pt) : ℝ := fL (extChartAt 𝓘(ℝ, P) p₀ x)

lemma Θt_eq (x : Pt) : Θt x = tco x := by
  show fL (extChartAt 𝓘(ℝ, P) p₀ x) = _
  rw [chart_apply]
  show (1/2 : ℝ) • ((Prod.fst (α := ℝ) (β := ℝ) x - Prod.snd (α := ℝ) (β := ℝ) x) +
    (Prod.fst (α := ℝ) (β := ℝ) x + Prod.snd (α := ℝ) (β := ℝ) x)) = Prod.fst (α := ℝ) (β := ℝ) x
  rw [smul_eq_mul]; ring

/-- **`Θt = t` is temporal on `M = Pt` (BUILT)**, intrinsically: `ContMDiff`, and
`dΘt(v) = fL (Dφ v) > 0` on future-causal `v`, read in both charts (`ch_dchart_eq`). -/
theorem me_temporal_Θt : minkN.IsTemporalOn minkN.M Θt := by
  have hφ : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, P) 1 (extChartAt 𝓘(ℝ, P) p₀) := by
    have h := contMDiffOn_extChartAt (I := 𝓘(ℝ, P)) (x := p₀) (n := 1)
    rw [source_eq] at h; exact contMDiffOn_univ.1 h
  have hf : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, ℝ) 1 fL := fL.contDiff.contMDiff
  refine ⟨(hf.comp hφ).contMDiffOn, fun x _ v hv => ?_⟩
  have hφd : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p₀) x :=
    mdifferentiableAt_extChartAt (src x)
  have hfd : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, ℝ) fL (extChartAt 𝓘(ℝ, P) p₀ x) :=
    mdifferentiableAt_iff_differentiableAt.2 fL.differentiableAt
  have e : dfun Θt x v = fL (dchart p₀ x v) := by
    unfold dfun
    have h : Θt = fL ∘ extChartAt 𝓘(ℝ, P) p₀ := rfl
    rw [h, mfderiv_comp x hfd hφd, mfderiv_eq_fderiv, fL.fderiv]; rfl
  rw [e, ch_dchart_eq]
  obtain ⟨-, h2⟩ := hv
  change gN x v (TN x) < 0 at h2
  unfold gN TN at h2
  split_ifs at h2 ⊢ with h
  · rw [gTX_apply] at h2; rw [nullL_apply]; simp [fL]; linarith
  · rw [gM_apply] at h2; simp [fL]; linarith

/-- **Non-vacuity of `me_past_extension` (BUILT).** On the two-chart manifold `Pt`, with
`Θ = t`: every point is the endpoint of the glued past-inextendible curve. -/
theorem me_witness_extension (x : Pt) :
    ∃ p : ℝ → Pt, Continuous p ∧ p 0 = x ∧ (∀ t ≤ 0, p t ∈ minkN.M) ∧
      (∀ t < 0, Θt (p t) < Θt x) ∧
      (∀ t < 0, t ∉ range (Int.cast : ℤ → ℝ) →
        ContMDiffAt 𝓘(ℝ, ℝ) 𝓘(ℝ, P) 1 p t ∧ minkN.FutTimelike (p t) (vel p t)) ∧
      ¬ ∃ q ∈ minkN.M, Tendsto p atBot (𝓝 q) :=
  me_past_extension me_locallyOneChart me_temporal_Θt (mem_univ x)

/-- **The hypotheses of `me_futCauchy_of_cauchy_N` other than the Cauchy property itself hold on
`Pt`** (`LocallyOneChart`, `U = M` open, `U ⊆ M`, `Θt` temporal), with points in different charts. -/
theorem me_witness_futCauchy_hyps :
    minkN.LocallyOneChart ∧ IsOpen minkN.M ∧ minkN.M ⊆ minkN.M ∧
      minkN.IsTemporalOn minkN.M Θt ∧
      extChartAt 𝓘(ℝ, P) (mkPt (-1) 0) (mkPt 1 0) ≠ extChartAt 𝓘(ℝ, P) (mkPt 1 0) (mkPt 1 0) :=
  ⟨me_locallyOneChart, minkN.isOpen_M, subset_rfl, me_temporal_Θt, me_charts_differ⟩

end NModel

#print axioms MSpacetime.ch_tstep_VN
#print axioms MSpacetime.LocallyOneChart.restrict
#print axioms MSpacetime.me_local_step
#print axioms MSpacetime.me_temporal_tstep
#print axioms MSpacetime.mvert_no_limit
#print axioms MSpacetime.me_past_sequence
#print axioms gpoly_continuous
#print axioms MSpacetime.vel_comp_add
#print axioms MSpacetime.me_past_extension
#print axioms MSpacetime.me_futCauchy_of_cauchy_N
#print axioms NModel.me_dchart_neg
#print axioms NModel.me_charts_differ
#print axioms NModel.me_locallyOneChart
#print axioms NModel.me_temporal_Θt
#print axioms NModel.me_witness_extension
#print axioms NModel.me_witness_futCauchy_hyps

end ShadowProbe.ManifoldExtensionProbe

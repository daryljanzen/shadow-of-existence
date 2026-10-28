import Mathlib.Analysis.ODE.ExistUnique
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Calculus.InverseFunctionTheorem.ContDiff
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension
import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Geometry.Manifold.VectorBundle.Basic
import Mathlib.Geometry.Manifold.MFDeriv.Atlas

/-!
# Probe `r7629+71.2` ①–②: the section form of the field's `C¹` hypothesis for the manifold flow-box chart;
`lem:killing` (b) on a manifold chart

Registered target: `computations/formalisation/r7629_71_campaign66/PREDICTION.md`. Base: campaign 64's
`probes/FlowLocal.lean` (all of it, `fl_*` renamed `fm_*`) and the `③` Killing part of campaign 62's
`probes/FlowC1.lean` (`fc_*` renamed `fm_*`, and localized), copied into namespace `FlowManifoldProbe`
(probes cannot import probes).

New here (after the copy):
* ① `fm_chartRep_eq_triv`: on the chart target, `chartRep X p y` is the fibre coordinate of `⟨φ⁻¹ y, X (φ⁻¹ y)⟩`
  in `trivializationAt E (TangentSpace 𝓘(ℝ, E)) p`.
* ① `fm_chartRep_contDiffAt_of_section`: the section `x ↦ ⟨x, X x⟩` `C¹` at `p` (as a map into the tangent
  bundle) gives `chartRep X p` `C¹` at `extChartAt p p`, hence on a ball around it (`fm_chartRep_ball_of_section`).
  Only `IsManifold 𝓘(ℝ, E) 1 N` is needed.
* ① `fm_chartRep_contDiffOn_of_section`: with `IsManifold 𝓘(ℝ, E) 2 N`, the section `C¹` on the chart source
  gives `chartRep X p` `C¹` on the whole chart target.
* ① `fm_manifold_flowBox_section`, `fm_manifold_flowBox_sectionOn`: `fm_manifold_flowBox` with the section
  hypothesis.
* ② the Killing part localized (`fm_flow_pushes_field_loc`, `fm_flow_isometry_loc`,
  `fm_flowBox_pullback_loc`), `fm_transfer_isVar`, `fm_flowBox_killing_of_contDiffOn`, and on a manifold
  `LocalKillingChart`, `fm_manifold_killingChart`, `fm_manifold_killingChart_section`. The metric and the
  Killing condition are in chart form (no Lie derivative of `(0,2)`-tensor fields on `N` in Mathlib).

Nothing imports this file.
-/


open Set Filter Topology Metric
open scoped NNReal

set_option linter.unusedSectionVars false

namespace FlowManifoldProbe

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-! ## Copied from `SmoothFlowProbe.lean` (steps 1, 2, 4(a)), renamed -/

/-- **1.** The first-order remainder of a `C¹` map is uniformly small on a closed ball. -/
theorem fm_remainder_unif (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) (R ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ R, ∀ z ∈ closedBall x₀ R, ‖y - z‖ < δ →
      ‖f y - f z - fderiv ℝ f z (y - z)‖ ≤ ε * ‖y - z‖ := by
  have hU : UniformContinuousOn (fderiv ℝ f) (closedBall x₀ (R + 1)) :=
    (isCompact_closedBall x₀ (R + 1)).uniformContinuousOn_of_continuous
      (hf.continuous_fderiv one_ne_zero).continuousOn
  obtain ⟨δ', hδ', hδ⟩ := Metric.uniformContinuousOn_iff.1 hU ε hε
  refine ⟨min δ' 1, by positivity, fun y hy z hz hyz => ?_⟩
  have hsub : ball z (min δ' 1) ⊆ closedBall x₀ (R + 1) := fun w hw => by
    rw [mem_closedBall] at hz ⊢; rw [mem_ball] at hw
    linarith [dist_triangle w z x₀, min_le_right δ' 1]
  have hz1 : z ∈ closedBall x₀ (R + 1) := hsub (mem_ball_self (by positivity))
  have hd : ∀ w ∈ ball z (min δ' 1), DifferentiableAt ℝ (fun w => f w - fderiv ℝ f z w) w :=
    fun w _ => (hf.differentiable one_ne_zero w).sub (fderiv ℝ f z).differentiableAt
  have hb : ∀ w ∈ ball z (min δ' 1), ‖fderiv ℝ (fun w => f w - fderiv ℝ f z w) w‖ ≤ ε := by
    intro w hw
    rw [fderiv_fun_sub (hf.differentiable one_ne_zero w) (fderiv ℝ f z).differentiableAt,
      ContinuousLinearMap.fderiv, ← dist_eq_norm]
    exact (hδ w (hsub hw) z hz1 (lt_of_lt_of_le (mem_ball.1 hw) (min_le_left _ _))).le
  have := Convex.norm_image_sub_le_of_norm_fderiv_le hd hb (convex_ball z (min δ' 1))
    (mem_ball_self (by positivity)) (by rw [mem_ball, dist_eq_norm]; exact hyz)
  rw [map_sub] at *
  convert this using 2
  abel

/-- **2.** The local flow of a `C¹` field, Lipschitz in the initial point. -/
theorem fm_local_flow (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) :
    ∃ τ > (0 : ℝ), ∃ r > (0 : ℝ), ∃ α : E → ℝ → E, ∃ L : ℝ≥0,
      (∀ x ∈ closedBall x₀ r, α x 0 = x ∧
        ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t) ∧
      ∀ t ∈ Icc (-τ) τ, LipschitzOnWith L (α · t) (closedBall x₀ r) := by
  obtain ⟨τ, hτ, a, r, L, K, hr, hPL⟩ := IsPicardLindelof.of_contDiffAt_one (hf.contDiffAt (x := x₀))
  obtain ⟨α, hα, L', hL'⟩ :=
    (hPL 0).exists_forall_mem_closedBall_eq_hasDerivWithinAt_lipschitzOnWith
  simp only [zero_sub, zero_add] at hα hL'
  exact ⟨τ, hτ, r, hr, α, L', hα, hL'⟩

/-- **4(a).** The trajectories from `closedBall x₀ r` over `[-τ, τ]` stay in one closed ball. -/
theorem fm_flow_bounded (f : E → E) (τ r : ℝ) (α : E → ℝ → E) (L : ℝ≥0) (x₀ : E)
    (hα : ∀ x ∈ closedBall x₀ r, α x 0 = x ∧
      ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t)
    (hL : ∀ t ∈ Icc (-τ) τ, LipschitzOnWith L (α · t) (closedBall x₀ r)) :
    ∃ R, ∀ x ∈ closedBall x₀ r, ∀ t ∈ Icc (-τ) τ, α x t ∈ closedBall x₀ R := by
  have hc : ContinuousOn (fun p : E × ℝ => α p.1 p.2) (closedBall x₀ r ×ˢ Icc (-τ) τ) :=
    continuousOn_prod_of_continuousOn_lipschitzOnWith _ L
      (fun x hx => fun t ht => ((hα x hx).2 t ht).continuousWithinAt) hL
  obtain ⟨R, hR⟩ := (((isCompact_closedBall x₀ r).prod isCompact_Icc).image_of_continuousOn
    hc).isBounded.subset_closedBall x₀
  exact ⟨R, fun x hx t ht => hR ⟨(x, t), ⟨hx, ht⟩, rfl⟩⟩

/-! ## A linear ODE on `[-T, T]` in one Picard–Lindelöf step, and a two-sided Grönwall -/

section Linear

variable {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]

/-- A linear ODE `W′ = A(t) W` with `‖A‖ ≤ M`, `M T ≤ 1/2`, has a solution on `[-T, T]` through `v`. -/
theorem fm_linear_exists [CompleteSpace F] (A : ℝ → F →L[ℝ] F) (T M : ℝ) (hT : 0 ≤ T) (hM : 0 ≤ M)
    (hMT : M * T ≤ 1 / 2) (hA : ContinuousOn A (Icc (-T) T))
    (hAM : ∀ t ∈ Icc (-T) T, ‖A t‖ ≤ M) (v : F) :
    ∃ W : ℝ → F, W 0 = v ∧
      ∀ t ∈ Icc (-T) T, HasDerivWithinAt W (A t (W t)) (Icc (-T) T) t := by
  have h0 : (0 : ℝ) ∈ Icc (-T) T := ⟨by linarith, hT⟩
  have hPL : IsPicardLindelof (fun t y => A t y) (⟨0, h0⟩ : Icc (-T) T) v
      ⟨‖v‖ + 1, by positivity⟩ 0 ⟨M * (2 * ‖v‖ + 1), by positivity⟩ ⟨M, hM⟩ := by
    refine ⟨fun t ht => ?_, fun y _ => ?_, fun t ht y hy => ?_, ?_⟩
    · refine LipschitzWith.lipschitzOnWith (LipschitzWith.of_dist_le_mul fun y z => ?_)
      rw [dist_eq_norm, dist_eq_norm, ← map_sub]
      exact (A t).le_of_opNorm_le (hAM t ht) _
    · exact hA.clm_apply continuousOn_const
    · have hy' : ‖y‖ ≤ 2 * ‖v‖ + 1 := by
        rw [Metric.mem_closedBall, dist_eq_norm] at hy
        have := norm_le_norm_add_norm_sub' y v
        have hy2 : ‖y - v‖ ≤ ‖v‖ + 1 := hy
        linarith
      exact ((A t).le_opNorm y).trans (mul_le_mul (hAM t ht) hy' (norm_nonneg _) hM)
    · show M * (2 * ‖v‖ + 1) * max (T - 0) (0 - -T) ≤ (‖v‖ + 1) - 0
      rw [sub_zero, zero_sub, neg_neg, max_self, sub_zero]
      nlinarith [norm_nonneg v, mul_le_mul_of_nonneg_right hMT (by positivity : 0 ≤ 2 * ‖v‖ + 1)]
  exact hPL.exists_eq_forall_mem_Icc_hasDerivWithinAt₀

/-- Grönwall forward on `[0, T]`, from a derivative within `[-T, T]`. -/
theorem fm_gronwall_fwd (e e' : ℝ → F) (T δ K c : ℝ)
    (he : ∀ s ∈ Icc (-T) T, HasDerivWithinAt e (e' s) (Icc (-T) T) s) (h0 : ‖e 0‖ ≤ δ)
    (hb : ∀ s ∈ Icc (-T) T, ‖e' s‖ ≤ K * ‖e s‖ + c) :
    ∀ s ∈ Icc 0 T, ‖e s‖ ≤ gronwallBound δ K c s := by
  intro s hs
  have hT : 0 ≤ T := hs.1.trans hs.2
  have hsub : Icc 0 T ⊆ Icc (-T) T := Icc_subset_Icc (by linarith) le_rfl
  have := norm_le_gronwallBound_of_norm_deriv_right_le (f := e) (f' := e') (a := 0) (b := T)
    (fun u hu => (he u (hsub hu)).continuousWithinAt.mono hsub)
    (fun u hu => (he u (hsub (Ico_subset_Icc_self hu))).mono_of_mem_nhdsWithin
      (mem_of_superset (Icc_mem_nhdsGE hu.2) (Icc_subset_Icc (by linarith [hu.1]) le_rfl)))
    h0 (fun u hu => hb u (hsub (Ico_subset_Icc_self hu))) s hs
  rwa [sub_zero] at this

/-- **Two-sided Grönwall.** On `[-T, T]`, from `‖e 0‖ ≤ δ` and `‖e′‖ ≤ K ‖e‖ + c`. -/
theorem fm_gronwall_symm (e e' : ℝ → F) (T δ K c : ℝ)
    (he : ∀ s ∈ Icc (-T) T, HasDerivWithinAt e (e' s) (Icc (-T) T) s) (h0 : ‖e 0‖ ≤ δ)
    (hb : ∀ s ∈ Icc (-T) T, ‖e' s‖ ≤ K * ‖e s‖ + c) :
    ∀ s ∈ Icc (-T) T, ‖e s‖ ≤ gronwallBound δ K c |s| := by
  intro s hs
  rcases le_total 0 s with h | h
  · rw [abs_of_nonneg h]; exact fm_gronwall_fwd e e' T δ K c he h0 hb s ⟨h, hs.2⟩
  · have hneg : ∀ u ∈ Icc (-T) T, -u ∈ Icc (-T) T := fun u hu => ⟨by linarith [hu.2], by linarith [hu.1]⟩
    have := fm_gronwall_fwd (fun u => e (-u)) (fun u => -e' (-u)) T δ K c
      (fun u hu => by
        have := (he (-u) (hneg u hu)).scomp u ((hasDerivAt_neg u).hasDerivWithinAt)
          (fun w hw => hneg w hw)
        simpa [Function.comp_def] using this)
      (by simpa using h0) (fun u hu => by simpa using hb (-u) (hneg u hu)) (-s)
      ⟨by linarith, by linarith [hs.1]⟩
    rw [abs_of_nonpos h]; simpa using this

end Linear

/-- The Grönwall bound with `δ = 0`, linear in `c`, uniformly on `[0, T]`. -/
theorem fm_gronwallBound_le (K c x T : ℝ) (hK : 0 < K) (hc : 0 ≤ c) (hxT : x ≤ T) :
    gronwallBound 0 K c x ≤ c * ((Real.exp (K * T) - 1) / K) := by
  rw [gronwallBound_of_K_ne_0 hK.ne']
  simp only [zero_mul, zero_add]
  calc c / K * (Real.exp (K * x) - 1) = c * ((Real.exp (K * x) - 1) / K) := by ring
    _ ≤ c * ((Real.exp (K * T) - 1) / K) := by
      gcongr

/-! ## The flow data -/

/-- A local flow of `f` near `x₀`, packaged: `α x t` for `x ∈ closedBall x₀ r`, `t ∈ [-τ, τ]`, Lipschitz in `x`,
inside `closedBall x₀ R` on which `‖Df‖ ≤ M`, with `M τ ≤ 1/2`. -/
structure FlowData (f : E → E) (x₀ : E) where
  τ : ℝ
  r : ℝ
  R : ℝ
  M : ℝ
  L : ℝ≥0
  α : E → ℝ → E
  τ_pos : 0 < τ
  r_pos : 0 < r
  M_pos : 0 < M
  Mτ : M * τ ≤ 1 / 2
  init : ∀ x ∈ closedBall x₀ r, α x 0 = x
  deriv : ∀ x ∈ closedBall x₀ r, ∀ t ∈ Icc (-τ) τ,
    HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t
  lip : ∀ t ∈ Icc (-τ) τ, LipschitzOnWith L (α · t) (closedBall x₀ r)
  mem : ∀ x ∈ closedBall x₀ r, ∀ t ∈ Icc (-τ) τ, α x t ∈ closedBall x₀ R
  dbound : ∀ y ∈ closedBall x₀ R, ‖fderiv ℝ f y‖ ≤ M

variable {f : E → E} {x₀ : E}

/-- Every `C¹` field has flow data at every point (Picard–Lindelöf, then shrink `τ`). -/
theorem fm_flowData_exists (hf : ContDiff ℝ 1 f) (x₀ : E) : Nonempty (FlowData f x₀) := by
  obtain ⟨τ₀, hτ₀, r, hr, α, L, hα, hL⟩ := fm_local_flow f hf x₀
  obtain ⟨R, hR⟩ := fm_flow_bounded f τ₀ r α L x₀ hα hL
  obtain ⟨C, hC⟩ := (isCompact_closedBall x₀ R).exists_bound_of_continuousOn
    (hf.continuous_fderiv one_ne_zero).continuousOn
  set M := max C 0 + 1 with hM
  have hM0 : 0 < M := by positivity
  set τ := min τ₀ (1 / (2 * M)) with hτ
  have hτ0 : 0 < τ := lt_min hτ₀ (by positivity)
  have hsub : Icc (-τ) τ ⊆ Icc (-τ₀) τ₀ :=
    Icc_subset_Icc (neg_le_neg (min_le_left _ _)) (min_le_left _ _)
  refine ⟨⟨τ, r, R, M, L, α, hτ0, hr, hM0, ?_, fun x hx => (hα x hx).1,
    fun x hx t ht => ((hα x hx).2 t (hsub ht)).mono hsub, fun t ht => hL t (hsub ht),
    fun x hx t ht => hR x hx t (hsub ht), fun y hy => (hC y hy).trans ?_⟩⟩
  · calc M * τ ≤ M * (1 / (2 * M)) := mul_le_mul_of_nonneg_left (min_le_right _ _) hM0.le
      _ = 1 / 2 := by field_simp
  · rw [hM]; linarith [le_max_left C 0]

namespace FlowData

variable (D : FlowData f x₀)

/-- `W` solves the variational equation along `α x`. -/
def IsVar (x : E) (W : ℝ → E →L[ℝ] E) : Prop :=
  W 0 = ContinuousLinearMap.id ℝ E ∧ ∀ t ∈ Icc (-D.τ) D.τ,
    HasDerivWithinAt W ((fderiv ℝ f (D.α x t)).comp (W t)) (Icc (-D.τ) D.τ) t

open Classical in
/-- The solution of the variational equation along `α x` (junk off `closedBall x₀ r`). -/
noncomputable def J (x : E) : ℝ → E →L[ℝ] E := if h : ∃ W, D.IsVar x W then h.choose else 0

theorem fm_Icc_mem {t : ℝ} (ht : t ∈ Icc (-D.τ) D.τ) : |t| ≤ D.τ := abs_le.2 ht

theorem fm_alpha_continuousOn (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ContinuousOn (D.α x) (Icc (-D.τ) D.τ) :=
  fun t ht => (D.deriv x hx t ht).continuousWithinAt

theorem fm_var_exists (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ∃ W, D.IsVar x W := by
  obtain ⟨W, hW0, hW⟩ := fm_linear_exists
    (fun t => ContinuousLinearMap.compL ℝ E E E (fderiv ℝ f (D.α x t))) D.τ D.M D.τ_pos.le
    D.M_pos.le D.Mτ
    ((ContinuousLinearMap.compL ℝ E E E).continuous.comp_continuousOn
      ((hf.continuous_fderiv one_ne_zero).comp_continuousOn (D.fm_alpha_continuousOn x hx)))
    (fun t ht => ContinuousLinearMap.opNorm_le_bound _ D.M_pos.le fun W =>
      ((ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))))
    (ContinuousLinearMap.id ℝ E)
  exact ⟨W, hW0, fun t ht => by simpa using hW t ht⟩

theorem fm_J_spec (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    D.IsVar x (D.J x) := by
  have h := D.fm_var_exists hf x hx
  unfold J; rw [dite_eq_left h]; exact h.choose_spec

/-- The constant of the Grönwall bound on `[-τ, τ]`. -/
noncomputable def C : ℝ := (Real.exp (D.M * D.τ) - 1) / D.M

theorem fm_C_nonneg : 0 ≤ D.C := by
  unfold C
  have : 1 ≤ Real.exp (D.M * D.τ) := Real.one_le_exp (by nlinarith [D.M_pos, D.τ_pos])
  exact div_nonneg (by linarith) D.M_pos.le

theorem fm_gb_le {c s : ℝ} (hc : 0 ≤ c) (hs : s ∈ Icc (-D.τ) D.τ) :
    gronwallBound 0 D.M c |s| ≤ c * D.C :=
  fm_gronwallBound_le _ _ _ _ D.M_pos hc (D.fm_Icc_mem hs)

/-- `‖J x s‖ ≤ exp (M τ)` on `[-τ, τ]`. -/
theorem fm_J_norm_le (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (s : ℝ) (hs : s ∈ Icc (-D.τ) D.τ) : ‖D.J x s‖ ≤ Real.exp (D.M * D.τ) := by
  obtain ⟨h0, hd⟩ := D.fm_J_spec hf x hx
  have := fm_gronwall_symm (D.J x) (fun t => (fderiv ℝ f (D.α x t)).comp (D.J x t)) D.τ 1 D.M 0 hd
    (by rw [h0]; exact ContinuousLinearMap.norm_id_le)
    (fun t ht => by
      rw [add_zero]
      exact (ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))) s hs
  rw [gronwallBound_ε0, one_mul] at this
  exact this.trans (Real.exp_le_exp.2 (mul_le_mul_of_nonneg_left (D.fm_Icc_mem hs) D.M_pos.le))

/-- **Grönwall #1, uniform in time.** `‖α y s − α x s − J x s (y − x)‖ ≤ ε ‖y − x‖` for `y` near `x`,
for every `s ∈ [-τ, τ]` at once. -/
theorem fm_remainder_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.α y s - D.α x s - D.J x s (y - x)‖ ≤ ε * ‖y - x‖ := by
  set ε' := ε / (((D.L : ℝ) + 1) * (D.C + 1)) with hε'
  have hC := D.fm_C_nonneg
  have hε'0 : 0 < ε' := by positivity
  obtain ⟨δ₀, hδ₀, hrem⟩ := fm_remainder_unif f hf x₀ D.R ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0, hJd⟩ := D.fm_J_spec hf x hx
  have hlip : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ ≤ D.L * ‖y - x‖ :=
    fun s hs => (D.lip s hs).norm_sub_le hy hx
  have hclose : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ < δ₀ := fun s hs => by
    have h1 := hlip s hs
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    nlinarith [norm_nonneg (y - x)]
  have key := fm_gronwall_symm (fun s => D.α y s - D.α x s - D.J x s (y - x))
    (fun s => f (D.α y s) - f (D.α x s) - (fderiv ℝ f (D.α x s)).comp (D.J x s) (y - x))
    D.τ 0 D.M (ε' * (D.L * ‖y - x‖))
    (fun s hs => by
      have := ((D.deriv y hy s hs).fun_sub (D.deriv x hx s hs)).fun_sub
        ((hJd s hs).clm_apply (hasDerivWithinAt_const s _ (y - x)))
      simpa using this)
    (by simp [D.init y hy, D.init x hx, hJ0])
    (fun s hs => by
      have hsplit : f (D.α y s) - f (D.α x s) - (fderiv ℝ f (D.α x s)).comp (D.J x s) (y - x) =
          (f (D.α y s) - f (D.α x s) - fderiv ℝ f (D.α x s) (D.α y s - D.α x s)) +
          fderiv ℝ f (D.α x s) (D.α y s - D.α x s - D.J x s (y - x)) := by
        simp only [ContinuousLinearMap.comp_apply, map_sub]; abel
      rw [hsplit]
      refine (norm_add_le _ _).trans ?_
      have h1 := hrem _ (D.mem y hy s hs) _ (D.mem x hx s hs) (hclose s hs)
      have h2 := (fderiv ℝ f (D.α x s)).le_opNorm (D.α y s - D.α x s - D.J x s (y - x))
      have h3 := D.dbound _ (D.mem x hx s hs)
      have h4 := hlip s hs
      nlinarith [norm_nonneg (D.α y s - D.α x s - D.J x s (y - x)), norm_nonneg (D.α y s - D.α x s)])
    s hs
  refine key.trans ((D.fm_gb_le (by positivity) hs).trans ?_)
  have : ε' * D.L * D.C ≤ ε := by
    rw [hε']
    rw [div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
    nlinarith [mul_le_mul (le_add_of_nonneg_right zero_le_one : (D.L : ℝ) ≤ D.L + 1)
      (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hC (by positivity)]
  nlinarith [norm_nonneg (y - x)]

/-- **Grönwall #2, uniform in time.** `‖J y s − J x s‖ ≤ ε` for `y` near `x`, every `s ∈ [-τ, τ]`. -/
theorem fm_J_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.J y s - D.J x s‖ ≤ ε := by
  set B := Real.exp (D.M * D.τ) with hB
  have hB0 : 0 < B := Real.exp_pos _
  have hC := D.fm_C_nonneg
  set ε' := ε / (B * (D.C + 1)) with hε'
  have hε'0 : 0 < ε' := by positivity
  have hU : UniformContinuousOn (fderiv ℝ f) (closedBall x₀ D.R) :=
    (isCompact_closedBall x₀ D.R).uniformContinuousOn_of_continuous
      (hf.continuous_fderiv one_ne_zero).continuousOn
  obtain ⟨δ₀, hδ₀, hδ⟩ := Metric.uniformContinuousOn_iff.1 hU ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0x, hJdx⟩ := D.fm_J_spec hf x hx
  obtain ⟨hJ0y, hJdy⟩ := D.fm_J_spec hf y hy
  have hDf : ∀ s ∈ Icc (-D.τ) D.τ, ‖fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)‖ ≤ ε' := by
    intro s hs
    have h1 := (D.lip s hs).norm_sub_le hy hx
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    rw [← dist_eq_norm]
    refine (hδ _ (D.mem y hy s hs) _ (D.mem x hx s hs) ?_).le
    rw [dist_eq_norm]; nlinarith [norm_nonneg (y - x)]
  have key := fm_gronwall_symm (fun s => D.J y s - D.J x s)
    (fun s => (fderiv ℝ f (D.α y s)).comp (D.J y s) - (fderiv ℝ f (D.α x s)).comp (D.J x s))
    D.τ 0 D.M (ε' * B) (fun s hs => (hJdy s hs).fun_sub (hJdx s hs)) (by simp [hJ0x, hJ0y])
    (fun s hs => by
      have hsplit : (fderiv ℝ f (D.α y s)).comp (D.J y s) - (fderiv ℝ f (D.α x s)).comp (D.J x s) =
          (fderiv ℝ f (D.α y s)).comp (D.J y s - D.J x s) +
          (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)).comp (D.J x s) := by
        rw [ContinuousLinearMap.comp_sub, ContinuousLinearMap.sub_comp]; abel
      rw [hsplit]
      refine (norm_add_le _ _).trans ?_
      have h1 := ContinuousLinearMap.opNorm_comp_le (fderiv ℝ f (D.α y s)) (D.J y s - D.J x s)
      have h2 := ContinuousLinearMap.opNorm_comp_le
        (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)) (D.J x s)
      have h3 := D.dbound _ (D.mem y hy s hs)
      have h4 := hDf s hs
      have h5 := D.fm_J_norm_le hf x hx s hs
      nlinarith [norm_nonneg (D.J y s - D.J x s), norm_nonneg (D.J x s),
        norm_nonneg (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s))])
    s hs
  refine key.trans ((D.fm_gb_le (by positivity) hs).trans ?_)
  rw [hε', div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
  nlinarith [mul_le_mul_of_nonneg_left (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hB0.le]

/-! ## ① The flow is differentiable, and `C¹`, in the initial point -/

/-- **① (a), T3b's stop.** `y ↦ α y t` has derivative `J x t` at every `x ∈ ball x₀ r`, `t ∈ [-τ, τ]`. -/
theorem fm_flow_hasFDerivAt (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ ball x₀ D.r)
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : HasFDerivAt (fun y => D.α y t) (D.J x t) x := by
  rw [hasFDerivAt_iff_isLittleO]
  refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
  obtain ⟨δ, hδ, h⟩ := D.fm_remainder_uniform hf x (ball_subset_closedBall hx) c hc
  filter_upwards [ball_mem_nhds x hδ, isOpen_ball.mem_nhds hx] with y hy1 hy2
  rw [mem_ball, dist_eq_norm] at hy1
  exact h y (ball_subset_closedBall hy2) hy1 t ht

/-- **① (b).** The derivative `x ↦ J x t` is continuous on `closedBall x₀ r`, uniformly in `t`. -/
theorem fm_J_continuousOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContinuousOn (fun x => D.J x t) (closedBall x₀ D.r) := by
  intro x hx
  rw [Metric.continuousWithinAt_iff]
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.fm_J_uniform hf x hx (ε / 2) (half_pos hε)
  refine ⟨δ, hδ, fun y hy hyx => ?_⟩
  rw [dist_eq_norm] at hyx ⊢
  exact (h y hy hyx t ht).trans_lt (half_lt_self hε)

/-- **① (c).** For every `t ∈ [-τ, τ]`, `x ↦ α x t` is `C¹` on `ball x₀ r`. -/
theorem fm_flow_contDiffOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContDiffOn ℝ 1 (fun y => D.α y t) (ball x₀ D.r) := fun _x hx =>
  (contDiffAt_one_iff.2 ⟨fun y => D.J y t, ball x₀ D.r, isOpen_ball.mem_nhds hx,
    (D.fm_J_continuousOn hf t ht).mono ball_subset_closedBall,
    fun y hy => D.fm_flow_hasFDerivAt hf y hy t ht⟩).contDiffWithinAt

/-- The open domain of the joint statement. -/
def U : Set (ℝ × E) := Ioo (-D.τ) D.τ ×ˢ ball x₀ D.r

theorem fm_U_open : IsOpen D.U := isOpen_Ioo.prod isOpen_ball

/-- The joint derivative: `(s, h) ↦ s • f (α x t) + J x t h`. -/
noncomputable def Dflow (p : ℝ × E) : ℝ × E →L[ℝ] E :=
  (ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α p.2 p.1)) +
    (D.J p.2 p.1).comp (ContinuousLinearMap.snd ℝ ℝ E)

theorem fm_Dflow_apply (p q : ℝ × E) : D.Dflow p q = q.1 • f (D.α p.2 p.1) + D.J p.2 p.1 q.2 := by
  simp [Dflow]

/-- `(t, x) ↦ J x t` is jointly continuous on `U`. -/
theorem fm_J_continuousAt_joint (hf : ContDiff ℝ 1 f) (p : ℝ × E) (hp : p ∈ D.U) :
    ContinuousAt (fun q : ℝ × E => D.J q.2 q.1) p := by
  obtain ⟨t, x⟩ := p
  obtain ⟨ht, hx⟩ := hp
  have htI : Icc (-D.τ) D.τ ∈ 𝓝 t := Icc_mem_nhds ht.1 ht.2
  have hJt : ContinuousAt (D.J x) t :=
    (((D.fm_J_spec hf x (ball_subset_closedBall hx)).2 t (Ioo_subset_Icc_self ht)).hasDerivAt
      htI).continuousAt
  rw [Metric.continuousAt_iff']
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.fm_J_uniform hf x (ball_subset_closedBall hx) (ε / 4) (by positivity)
  have h1 : ∀ᶠ q in 𝓝 (t, x), q.1 ∈ Icc (-D.τ) D.τ := continuousAt_fst.preimage_mem_nhds htI
  have h2 : ∀ᶠ q in 𝓝 (t, x), q.2 ∈ ball x₀ D.r :=
    continuousAt_snd.preimage_mem_nhds (isOpen_ball.mem_nhds hx)
  have h3 : ∀ᶠ q in 𝓝 (t, x), q.2 ∈ ball x δ :=
    continuousAt_snd.preimage_mem_nhds (ball_mem_nhds x hδ)
  have h4 : ∀ᶠ q in 𝓝 (t, x), dist (D.J x q.1) (D.J x t) < ε / 2 :=
    (hJt.comp continuousAt_fst).eventually (Metric.ball_mem_nhds _ (half_pos hε))
  filter_upwards [h1, h2, h3, h4] with q hq1 hq2 hq3 hq4
  rw [mem_ball, dist_eq_norm] at hq3
  have := h q.2 (ball_subset_closedBall hq2) hq3 q.1 hq1
  rw [dist_eq_norm] at hq4 ⊢
  calc ‖D.J q.2 q.1 - D.J x t‖ ≤ ‖D.J q.2 q.1 - D.J x q.1‖ + ‖D.J x q.1 - D.J x t‖ :=
        norm_sub_le_norm_sub_add_norm_sub _ _ _
    _ < ε := by linarith

/-- **① (d).** `(t, x) ↦ α x t` has derivative `Dflow (t, x)` at every point of `U`. -/
theorem fm_flow_hasFDerivAt_joint (hf : ContDiff ℝ 1 f) (p : ℝ × E) (hp : p ∈ D.U) :
    HasFDerivAt (fun q : ℝ × E => D.α q.2 q.1) (D.Dflow p) p := by
  obtain ⟨t, x⟩ := p
  obtain ⟨ht, hx⟩ := hp
  have hxc := ball_subset_closedBall hx
  have htI : Icc (-D.τ) D.τ ∈ 𝓝 t := Icc_mem_nhds ht.1 ht.2
  -- the time part
  have hA : HasFDerivAt (fun q : ℝ × E => D.α x q.1)
      ((ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α x t))) (t, x) := by
    have := ((D.deriv x hxc t (Ioo_subset_Icc_self ht)).hasDerivAt htI).hasFDerivAt.comp (t, x)
      (hasFDerivAt_fst (𝕜 := ℝ) (p := (t, x)))
    exact this.congr_fderiv (ContinuousLinearMap.ext fun q => by simp)
  -- the space part, through the uniform remainder and the continuity of `J x` in time
  have hJt : ContinuousAt (D.J x) t :=
    (((D.fm_J_spec hf x hxc).2 t (Ioo_subset_Icc_self ht)).hasDerivAt htI).continuousAt
  have hB : HasFDerivAt (fun q : ℝ × E => D.α q.2 q.1 - D.α x q.1)
      ((D.J x t).comp (ContinuousLinearMap.snd ℝ ℝ E)) (t, x) := by
    rw [hasFDerivAt_iff_isLittleO]
    refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
    obtain ⟨δ, hδ, h⟩ := D.fm_remainder_uniform hf x hxc (c / 2) (half_pos hc)
    have h1 : ∀ᶠ q in 𝓝 (t, x), q.1 ∈ Icc (-D.τ) D.τ := continuousAt_fst.preimage_mem_nhds htI
    have h2 : ∀ᶠ q in 𝓝 (t, x), q.2 ∈ ball x₀ D.r :=
      continuousAt_snd.preimage_mem_nhds (isOpen_ball.mem_nhds hx)
    have h3 : ∀ᶠ q in 𝓝 (t, x), q.2 ∈ ball x δ :=
      continuousAt_snd.preimage_mem_nhds (ball_mem_nhds x hδ)
    have h4 : ∀ᶠ q in 𝓝 (t, x), dist (D.J x q.1) (D.J x t) < c / 2 :=
      (hJt.comp continuousAt_fst).eventually (Metric.ball_mem_nhds _ (half_pos hc))
    filter_upwards [h1, h2, h3, h4] with q hq1 hq2 hq3 hq4
    rw [mem_ball, dist_eq_norm] at hq3
    rw [dist_eq_norm] at hq4
    have hr := h q.2 (ball_subset_closedBall hq2) hq3 q.1 hq1
    have hsn : ‖q.2 - x‖ ≤ ‖q - (t, x)‖ := by
      have := norm_snd_le (q - (t, x)); simpa using this
    have hJ : ‖(D.J x q.1 - D.J x t) (q.2 - x)‖ ≤ c / 2 * ‖q.2 - x‖ :=
      ((D.J x q.1 - D.J x t).le_opNorm _).trans
        (mul_le_mul_of_nonneg_right hq4.le (norm_nonneg _))
    have heq : D.α q.2 q.1 - D.α x q.1 - (D.α x t - D.α x t) -
        ((D.J x t).comp (ContinuousLinearMap.snd ℝ ℝ E)) (q - (t, x)) =
        (D.α q.2 q.1 - D.α x q.1 - D.J x q.1 (q.2 - x)) + (D.J x q.1 - D.J x t) (q.2 - x) := by
      simp only [sub_self, sub_zero, ContinuousLinearMap.comp_apply, ContinuousLinearMap.coe_snd',
        Prod.snd_sub, sub_apply]
      abel
    rw [heq]
    calc _ ≤ _ := norm_add_le _ _
      _ ≤ c / 2 * ‖q.2 - x‖ + c / 2 * ‖q.2 - x‖ := add_le_add hr hJ
      _ = c * ‖q.2 - x‖ := by ring
      _ ≤ c * ‖q - (t, x)‖ := mul_le_mul_of_nonneg_left hsn hc.le
  have := hB.add hA
  convert this using 1
  · funext q; simp
  · rw [Dflow, add_comm]

/-- The flow is continuous on `U`. -/
theorem fm_flow_continuousOn_joint (hf : ContDiff ℝ 1 f) :
    ContinuousOn (fun q : ℝ × E => D.α q.2 q.1) D.U := fun p hp =>
  (D.fm_flow_hasFDerivAt_joint hf p hp).continuousAt.continuousWithinAt

theorem fm_Dflow_continuousOn (hf : ContDiff ℝ 1 f) : ContinuousOn D.Dflow D.U := by
  have h1 : ContinuousOn (fun p : ℝ × E => f (D.α p.2 p.1)) D.U :=
    hf.continuous.comp_continuousOn (D.fm_flow_continuousOn_joint hf)
  have h2 : ContinuousOn (fun p : ℝ × E => D.J p.2 p.1) D.U := fun p hp =>
    (D.fm_J_continuousAt_joint hf p hp).continuousWithinAt
  have h3 : ContinuousOn (fun p : ℝ × E =>
      (ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α p.2 p.1))) D.U := by
    have := (ContinuousLinearMap.smulRightL ℝ (ℝ × E) E (ContinuousLinearMap.fst ℝ ℝ E)).continuous.comp_continuousOn h1
    convert this using 1
    funext p
    exact ContinuousLinearMap.ext fun q => by simp
  exact h3.add (h2.clm_comp continuousOn_const)

/-- **① (e), the registered theorem.** The flow `(t, x) ↦ α x t` is `C¹` jointly on
`Ioo (-τ) τ ×ˢ ball x₀ r`. -/
theorem fm_flow_contDiffOn_joint (hf : ContDiff ℝ 1 f) :
    ContDiffOn ℝ 1 (fun q : ℝ × E => D.α q.2 q.1) D.U := fun _p hp =>
  (contDiffAt_one_iff.2 ⟨D.Dflow, D.U, D.fm_U_open.mem_nhds hp, D.fm_Dflow_continuousOn hf,
    fun q hq => D.fm_flow_hasFDerivAt_joint hf q hq⟩).contDiffWithinAt

end FlowData

/-- **① headline, without `FlowData`.** A `C¹` field on a finite-dimensional space has a local flow
`α x t` (`x ∈ closedBall x₀ r`, `t ∈ [-τ, τ]`) that is `C¹` jointly in `(t, x)` on `Ioo (-τ) τ ×ˢ ball x₀ r`,
`C¹` in `x` for each `t ∈ [-τ, τ]`, with `x`-derivative solving the variational equation. -/
theorem fm_flow_C1 (hf : ContDiff ℝ 1 f) (x₀ : E) :
    ∃ τ > (0 : ℝ), ∃ r > (0 : ℝ), ∃ α : E → ℝ → E, ∃ J : E → ℝ → E →L[ℝ] E,
      (∀ x ∈ closedBall x₀ r, α x 0 = x ∧
        ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t) ∧
      (∀ x ∈ closedBall x₀ r, J x 0 = ContinuousLinearMap.id ℝ E ∧ ∀ t ∈ Icc (-τ) τ,
        HasDerivWithinAt (J x) ((fderiv ℝ f (α x t)).comp (J x t)) (Icc (-τ) τ) t) ∧
      (∀ x ∈ ball x₀ r, ∀ t ∈ Icc (-τ) τ, HasFDerivAt (fun y => α y t) (J x t) x) ∧
      (∀ t ∈ Icc (-τ) τ, ContDiffOn ℝ 1 (fun y => α y t) (ball x₀ r)) ∧
      ContDiffOn ℝ 1 (fun q : ℝ × E => α q.2 q.1) (Ioo (-τ) τ ×ˢ ball x₀ r) := by
  obtain ⟨D⟩ := fm_flowData_exists hf x₀
  exact ⟨D.τ, D.τ_pos, D.r, D.r_pos, D.α, D.J, fun x hx => ⟨D.init x hx, D.deriv x hx⟩,
    fun x hx => D.fm_J_spec hf x hx, fun x hx t ht => D.fm_flow_hasFDerivAt hf x hx t ht,
    fun t ht => D.fm_flow_contDiffOn hf t ht, D.fm_flow_contDiffOn_joint hf⟩

/-! ## ② The flow-box chart -/

/-- A complement `H` of `ℝ ∙ v`, `v ≠ 0`, gives `ℝ × H ≃L E`, `(a, h) ↦ a • v + h`. -/
theorem fm_complement_equiv (v : E) (hv : v ≠ 0) (H : Submodule ℝ E) (hH : IsCompl (ℝ ∙ v) H) :
    ∃ e : (ℝ × H) ≃L[ℝ] E, ∀ p : ℝ × H, e p = p.1 • v + p.2 := by
  let ℓ : ℝ × H →ₗ[ℝ] E := (LinearMap.fst ℝ ℝ H).smulRight v + H.subtype ∘ₗ LinearMap.snd ℝ ℝ H
  have hℓ : ∀ p, ℓ p = p.1 • v + p.2 := fun p => by simp [ℓ]
  have hinj : Function.Injective ℓ := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    intro p hp
    rw [hℓ] at hp
    have h1 : p.1 • v = -(p.2 : E) := eq_neg_of_add_eq_zero_left hp
    have h2 : p.1 • v = 0 := Submodule.disjoint_def.1 hH.disjoint _
      (Submodule.mem_span_singleton.2 ⟨p.1, rfl⟩) (by rw [h1]; exact H.neg_mem p.2.2)
    have h3 : p.1 = 0 := (smul_eq_zero.1 h2).resolve_right hv
    have h4 : (p.2 : E) = 0 := by rw [h3, zero_smul, zero_add] at hp; exact hp
    exact Prod.ext h3 (Subtype.ext h4)
  have hsurj : Function.Surjective ℓ := by
    intro x
    have hx : x ∈ (ℝ ∙ v) ⊔ H := by rw [hH.sup_eq_top]; trivial
    obtain ⟨y, hy, z, hz, rfl⟩ := Submodule.mem_sup.1 hx
    obtain ⟨a, rfl⟩ := Submodule.mem_span_singleton.1 hy
    exact ⟨(a, ⟨z, hz⟩), by rw [hℓ]⟩
  exact ⟨(LinearEquiv.ofBijective ℓ ⟨hinj, hsurj⟩).toContinuousLinearEquiv, fun p => hℓ p⟩

namespace FlowData

variable (D : FlowData f x₀)

/-- What a flow-box chart `Φ : ℝ × H → E` for `D` at `x₀` satisfies. -/
structure IsFlowBox (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E) : Prop where
  zero_mem : ((0 : ℝ), (0 : H)) ∈ Φ.source
  map_zero : Φ (0, 0) = x₀
  symm_x₀ : Φ.symm x₀ = (0, 0)
  /-- `Φ (λ, h) = α (x₀ + h) λ`, inside the domain of the joint statement. -/
  source_sub : ∀ p ∈ Φ.source, (p.1, x₀ + (p.2 : E)) ∈ D.U
  apply_eq : ∀ p ∈ Φ.source, Φ p = D.α (x₀ + p.2) p.1
  contDiffOn : ContDiffOn ℝ 1 Φ Φ.source
  /-- `DΦ (0, 0) (a, h) = a • f x₀ + h`, the invertible derivative. -/
  fderiv_zero : ∀ (a : ℝ) (h : H), fderiv ℝ Φ (0, 0) (a, h) = a • f x₀ + h
  /-- `DΦ p (a, h) = a • f (Φ p) + J (x₀ + h) λ h`. -/
  fderiv_eq : ∀ p ∈ Φ.source, ∀ u : ℝ × H,
    fderiv ℝ Φ p u = u.1 • f (Φ p) + D.J (x₀ + p.2) p.1 u.2
  /-- `f = ∂_λ` in the chart: `DΦ · (1, 0) = f ∘ Φ`. -/
  straightens : ∀ p ∈ Φ.source, fderiv ℝ Φ p (1, 0) = f (Φ p)
  /-- The inverse is `C¹` near `x₀`. -/
  symm_contDiffAt : ∀ᶠ y in 𝓝 x₀, ContDiffAt ℝ 1 Φ.symm y

/-- **② The flow-box chart.** If `f x₀ ≠ 0` and `H` is a complement of `ℝ ∙ f x₀`, then
`Ψ (λ, h) = α (x₀ + h) λ` restricts to an open partial homeomorphism `ℝ × H → E` around `(0, 0)` that is `C¹`
on its source, with `DΨ (0, 0) (a, h) = a • f x₀ + h`, `DΨ · (1, 0) = f ∘ Ψ` (so `f = ∂_λ` in the chart),
and a `C¹` inverse near `x₀`. -/
theorem fm_flowBox (hf : ContDiff ℝ 1 f) (hfx : f x₀ ≠ 0) (H : Submodule ℝ E)
    (hH : IsCompl (ℝ ∙ f x₀) H) : ∃ Φ : OpenPartialHomeomorph (ℝ × H) E, D.IsFlowBox H Φ := by
  obtain ⟨e, he⟩ := fm_complement_equiv (f x₀) hfx H hH
  -- the affine map `(λ, h) ↦ (λ, x₀ + h)`
  set Lg : ℝ × H →L[ℝ] ℝ × E :=
    (ContinuousLinearMap.fst ℝ ℝ H).prod (H.subtypeL.comp (ContinuousLinearMap.snd ℝ ℝ H)) with hLg
  set g : ℝ × H → ℝ × E := fun p => ((0 : ℝ), x₀) + Lg p with hg
  have hgp : ∀ p : ℝ × H, g p = (p.1, x₀ + (p.2 : E)) := fun p => by simp [hg, hLg]
  have hgd : ∀ p, HasFDerivAt g Lg p := fun p => Lg.hasFDerivAt.const_add _
  have hgc : ContDiff ℝ 1 g := contDiff_const.add Lg.contDiff
  set Ψ : ℝ × H → E := fun p => D.α (x₀ + (p.2 : E)) p.1 with hΨ
  have hΨg : Ψ = (fun q : ℝ × E => D.α q.2 q.1) ∘ g := by
    funext p; simp only [Function.comp, hgp, hΨ]
  set V := g ⁻¹' D.U with hV
  have hVo : IsOpen V := D.fm_U_open.preimage hgc.continuous
  have hV0 : ((0 : ℝ), (0 : H)) ∈ V := by
    show g (0, 0) ∈ D.U
    rw [hgp]
    exact ⟨⟨by linarith [D.τ_pos], D.τ_pos⟩, by simpa using D.r_pos⟩
  have hΨc : ContDiffOn ℝ 1 Ψ V := by
    rw [hΨg]; exact (D.fm_flow_contDiffOn_joint hf).comp hgc.contDiffOn fun p hp => hp
  have hΨd : ∀ p ∈ V, HasFDerivAt Ψ ((D.Dflow (g p)).comp Lg) p := fun p hp => by
    rw [hΨg]; exact (D.fm_flow_hasFDerivAt_joint hf (g p) hp).comp p (hgd p)
  have hΨu : ∀ p ∈ V, ∀ u, fderiv ℝ Ψ p u = u.1 • f (Ψ p) + D.J (x₀ + p.2) p.1 u.2 :=
    fun p hp u => by
      rw [(hΨd p hp).fderiv, ContinuousLinearMap.comp_apply, fm_Dflow_apply, hgp]
      simp [hLg, hΨ]
  have hx₀ : x₀ ∈ closedBall x₀ D.r := mem_closedBall_self D.r_pos.le
  have hD0 : (D.Dflow (g (0, 0))).comp Lg = (e : ℝ × H →L[ℝ] E) := by
    refine ContinuousLinearMap.ext fun q => ?_
    rw [ContinuousLinearMap.comp_apply, fm_Dflow_apply, hgp, ContinuousLinearEquiv.coe_coe, he]
    simp [hLg, D.init x₀ hx₀, (D.fm_J_spec hf x₀ hx₀).1]
  have hΨ0 : HasFDerivAt Ψ (e : ℝ × H →L[ℝ] E) (0, 0) := hD0 ▸ hΨd _ hV0
  have hΨ00 : Ψ (0, 0) = x₀ := by simp [hΨ, D.init x₀ hx₀]
  have hΨa : ContDiffAt ℝ 1 Ψ (0, 0) := hΨc.contDiffAt (hVo.mem_nhds hV0)
  have hn : (1 : WithTop ℕ∞) ≠ 0 := by norm_num
  set Φ₀ := hΨa.toOpenPartialHomeomorph Ψ hΨ0 hn
  refine ⟨Φ₀.restrOpen V hVo, ⟨⟨hΨa.mem_toOpenPartialHomeomorph_source hΨ0 hn, hV0⟩, hΨ00, ?_,
    fun p hp => by have := hp.2; rwa [Set.mem_preimage, hgp] at this, fun p _ => rfl,
    hΨc.mono inter_subset_right, fun a h => ?_, fun p hp u => hΨu p hp.2 u, fun p hp => ?_, ?_⟩⟩
  · have := hΨa.localInverse_apply_image hΨ0 hn
    rw [hΨ00] at this
    exact this
  · show fderiv ℝ Ψ (0, 0) (a, h) = a • f x₀ + h
    rw [hΨ0.fderiv, ContinuousLinearEquiv.coe_coe, he]
  · show fderiv ℝ Ψ p (1, 0) = f (Ψ p)
    rw [hΨu p hp.2]; simp
  · have := (hΨa.to_localInverse hΨ0 hn).eventually (by simp)
    rw [hΨ00] at this
    exact this

end FlowData

/-- **② as an existence statement.** At a point where a `C¹` field does not vanish there is a complement
`H` of `ℝ ∙ f x₀`, a flow, and a flow-box chart `ℝ × H → E` straightening `f` to `∂_λ`. -/
theorem fm_flowBox_exists (hf : ContDiff ℝ 1 f) (x₀ : E) (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (D : FlowData f x₀) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      D.IsFlowBox H Φ := by
  obtain ⟨H, hH⟩ := Submodule.exists_isCompl (ℝ ∙ f x₀)
  obtain ⟨D⟩ := fm_flowData_exists hf x₀
  obtain ⟨Φ, hΦ⟩ := D.fm_flowBox hf hfx H hH
  exact ⟨H, D, Φ, hΦ⟩

/-! ## ① The local constructor: cutoff, small flow data, transfer -/

/-- **Cutoff.** A field `C¹` on `ball x₀ ρ` agrees, near every point of `ball x₀ (ρ / 4)`, with a global `C¹`
field: `χ • f`, `χ` a `ContDiffBump x₀` equal to `1` on `closedBall x₀ (ρ / 4)`, support `ball x₀ (ρ / 2)`. -/
theorem fm_cutoff {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ)) :
    ∃ g : E → E, ContDiff ℝ 1 g ∧ ∀ y ∈ ball x₀ (ρ / 4), g =ᶠ[𝓝 y] f := by
  let χ : ContDiffBump x₀ := ⟨ρ / 4, ρ / 2, by positivity, by linarith⟩
  have hrIn : χ.rIn = ρ / 4 := rfl
  have hrOut : χ.rOut = ρ / 2 := rfl
  refine ⟨fun y => χ y • f y, ?_, fun y hy => ?_⟩
  · rw [contDiff_iff_contDiffAt]
    intro y
    by_cases hy : y ∈ ball x₀ ρ
    · exact χ.contDiff.contDiffAt.smul (hf.contDiffAt (isOpen_ball.mem_nhds hy))
    · have hy' : y ∉ tsupport χ := by
        rw [χ.tsupport_eq, hrOut]
        intro h
        apply hy
        rw [mem_closedBall] at h
        rw [mem_ball]
        linarith
      have h0 : (fun y => χ y • f y) =ᶠ[𝓝 y] fun _ => (0 : E) := by
        filter_upwards [notMem_tsupport_iff_eventuallyEq.1 hy'] with z hz
        simp [hz]
      exact contDiffAt_const.congr_of_eventuallyEq h0
  · filter_upwards [isOpen_ball.mem_nhds hy] with z hz
    rw [χ.one_of_mem_closedBall (by rw [hrIn]; exact ball_subset_closedBall hz), one_smul]

/-- **Small flow data.** For a global `C¹` field, flow data whose trajectory ball `closedBall x₀ R` has
`R < R₀`: the speed along `[-τ₀, τ₀]` is bounded by some `S`, and then `τ ≤ R / (2 S)`, `r ≤ R / 2`. -/
theorem fm_flowData_small {g : E → E} (hg : ContDiff ℝ 1 g) (x₀ : E) {R₀ : ℝ} (hR₀ : 0 < R₀) :
    ∃ D : FlowData g x₀, D.R < R₀ := by
  obtain ⟨τ₀, hτ₀, r₀, hr₀, α, L, hα, hL⟩ := fm_local_flow g hg x₀
  obtain ⟨R₁, hR₁⟩ := fm_flow_bounded g τ₀ r₀ α L x₀ hα hL
  obtain ⟨C, hC⟩ := (isCompact_closedBall x₀ R₁).exists_bound_of_continuousOn
    hg.continuous.continuousOn
  set R := R₀ / 2 with hR
  have hR0 : 0 < R := by positivity
  obtain ⟨C', hC'⟩ := (isCompact_closedBall x₀ R).exists_bound_of_continuousOn
    (hg.continuous_fderiv one_ne_zero).continuousOn
  set S := max C 0 + 1 with hS
  have hS0 : 0 < S := by positivity
  set M := max C' 0 + 1 with hM
  have hM0 : 0 < M := by positivity
  set τ := min (min τ₀ (1 / (2 * M))) (R / (2 * S)) with hτ
  have hτ0 : 0 < τ := lt_min (lt_min hτ₀ (by positivity)) (by positivity)
  have hττ₀ : τ ≤ τ₀ := (min_le_left _ _).trans (min_le_left _ _)
  have hτM : τ ≤ 1 / (2 * M) := (min_le_left _ _).trans (min_le_right _ _)
  have hτS : τ ≤ R / (2 * S) := min_le_right _ _
  set r := min r₀ (R / 2) with hr
  have hr0 : 0 < r := lt_min hr₀ (by positivity)
  have hrr₀ : r ≤ r₀ := min_le_left _ _
  have hrR : r ≤ R / 2 := min_le_right _ _
  have hsub : Icc (-τ) τ ⊆ Icc (-τ₀) τ₀ := Icc_subset_Icc (neg_le_neg hττ₀) hττ₀
  have hbsub : closedBall x₀ r ⊆ closedBall x₀ r₀ := closedBall_subset_closedBall hrr₀
  have hmem : ∀ x ∈ closedBall x₀ r, ∀ t ∈ Icc (-τ) τ, α x t ∈ closedBall x₀ R := by
    intro x hx t ht
    have hd : ∀ u ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (g (α x u)) (Icc (-τ) τ) u :=
      fun u hu => ((hα x (hbsub hx)).2 u (hsub hu)).mono hsub
    have hb : ∀ u ∈ Icc (-τ) τ, ‖g (α x u)‖ ≤ S := fun u hu =>
      (hC _ (hR₁ x (hbsub hx) u (hsub hu))).trans (by rw [hS]; linarith [le_max_left C 0])
    have h0 : (0 : ℝ) ∈ Icc (-τ) τ := ⟨by linarith, hτ0.le⟩
    have key := (convex_Icc (-τ) τ).norm_image_sub_le_of_norm_hasDerivWithin_le hd hb h0 ht
    rw [(hα x (hbsub hx)).1, sub_zero, Real.norm_eq_abs] at key
    have ht' : |t| ≤ τ := abs_le.2 ht
    have h1 : S * |t| ≤ R / 2 := by
      calc S * |t| ≤ S * (R / (2 * S)) := mul_le_mul_of_nonneg_left (ht'.trans hτS) hS0.le
        _ = R / 2 := by field_simp
    rw [mem_closedBall] at hx ⊢
    calc dist (α x t) x₀ ≤ dist (α x t) x + dist x x₀ := dist_triangle _ _ _
      _ ≤ R / 2 + R / 2 := by rw [dist_eq_norm]; linarith
      _ = R := by ring
  refine ⟨⟨τ, r, R, M, L, α, hτ0, hr0, hM0, ?_, fun x hx => (hα x (hbsub hx)).1,
    fun x hx t ht => ((hα x (hbsub hx)).2 t (hsub ht)).mono hsub,
    fun t ht => (hL t (hsub ht)).mono hbsub, hmem, fun y hy => (hC' y hy).trans ?_⟩, ?_⟩
  · calc M * τ ≤ M * (1 / (2 * M)) := mul_le_mul_of_nonneg_left hτM hM0.le
      _ = 1 / 2 := by field_simp
  · rw [hM]; linarith [le_max_left C' 0]
  · show R < R₀
    rw [hR]; linarith

/-- Two fields that agree near every point of `ball x₀ s` agree to first order on `closedBall x₀ R`, `R < s`. -/
theorem fm_agree {g : E → E} {s R : ℝ} (hgf : ∀ y ∈ ball x₀ s, g =ᶠ[𝓝 y] f) (hR : R < s) :
    ∀ y ∈ closedBall x₀ R, f y = g y ∧ fderiv ℝ f y = fderiv ℝ g y := fun y hy =>
  ⟨(hgf y (closedBall_subset_ball hR hy)).eq_of_nhds.symm,
    (hgf y (closedBall_subset_ball hR hy)).fderiv_eq.symm⟩

namespace FlowData

variable {g : E → E}

/-- `x₀` lies in the trajectory ball. -/
theorem fm_x₀_mem (D : FlowData g x₀) : x₀ ∈ closedBall x₀ D.R := by
  have hx := mem_closedBall_self (x := x₀) D.r_pos.le
  have := D.mem x₀ hx 0 ⟨by linarith [D.τ_pos], D.τ_pos.le⟩
  rwa [D.init x₀ hx] at this

/-- **Transfer.** Flow data for `g` is flow data for `f` when `f = g` to first order on `closedBall x₀ R`:
same `τ, r, R, M, L, α`. -/
def transfer (D : FlowData g x₀)
    (hfg : ∀ y ∈ closedBall x₀ D.R, f y = g y ∧ fderiv ℝ f y = fderiv ℝ g y) : FlowData f x₀ where
  τ := D.τ
  r := D.r
  R := D.R
  M := D.M
  L := D.L
  α := D.α
  τ_pos := D.τ_pos
  r_pos := D.r_pos
  M_pos := D.M_pos
  Mτ := D.Mτ
  init := D.init
  deriv := fun x hx t ht => by
    rw [(hfg _ (D.mem x hx t ht)).1]; exact D.deriv x hx t ht
  lip := D.lip
  mem := D.mem
  dbound := fun y hy => by rw [(hfg y hy).2]; exact D.dbound y hy

variable (D : FlowData g x₀)
  (hfg : ∀ y ∈ closedBall x₀ D.R, f y = g y ∧ fderiv ℝ f y = fderiv ℝ g y)

/-- The transferred data has the same variational solution `J`. -/
theorem fm_transfer_J (x : E) (hx : x ∈ closedBall x₀ D.r) : (D.transfer hfg).J x = D.J x := by
  have h : (D.transfer hfg).IsVar x = D.IsVar x := by
    funext W
    apply propext
    unfold IsVar
    dsimp only [transfer]
    constructor
    · rintro ⟨h0, hd⟩
      exact ⟨h0, fun t ht => by have := hd t ht; rwa [(hfg _ (D.mem x hx t ht)).2] at this⟩
    · rintro ⟨h0, hd⟩
      exact ⟨h0, fun t ht => by rw [(hfg _ (D.mem x hx t ht)).2]; exact hd t ht⟩
  unfold J
  rw [h]

/-- A flow-box point lies in the trajectory ball. -/
theorem fm_isFlowBox_mem {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E}
    (hΦ : D.IsFlowBox H Φ) (p : ℝ × H) (hp : p ∈ Φ.source) : Φ p ∈ closedBall x₀ D.R := by
  obtain ⟨ht, hy⟩ := hΦ.source_sub p hp
  rw [hΦ.apply_eq p hp]
  exact D.mem _ (ball_subset_closedBall hy) _ (Ioo_subset_Icc_self ht)

/-- **Transfer of the flow box.** A flow-box chart for `g` is a flow-box chart for `f`, with `f` itself in
`straightens`: `DΦ · (1, 0) = f ∘ Φ`. -/
theorem fm_transfer_isFlowBox {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E}
    (hΦ : D.IsFlowBox H Φ) : (D.transfer hfg).IsFlowBox H Φ := by
  have hx₀ := (hfg x₀ D.fm_x₀_mem).1
  refine ⟨hΦ.zero_mem, hΦ.map_zero, hΦ.symm_x₀, hΦ.source_sub, hΦ.apply_eq, hΦ.contDiffOn,
    fun a h => ?_, fun p hp u => ?_, fun p hp => ?_, hΦ.symm_contDiffAt⟩
  · rw [hx₀]; exact hΦ.fderiv_zero a h
  · obtain ⟨_, hy⟩ := hΦ.source_sub p hp
    rw [(hfg _ (D.fm_isFlowBox_mem hΦ p hp)).1,
      D.fm_transfer_J hfg _ (ball_subset_closedBall hy)]
    exact hΦ.fderiv_eq p hp u
  · rw [(hfg _ (D.fm_isFlowBox_mem hΦ p hp)).1]; exact hΦ.straightens p hp

end FlowData

/-- **① The local constructor.** A field that is `C¹` on `ball x₀ ρ` has flow data at `x₀` (for `f` itself),
with trajectory ball inside `ball x₀ (ρ / 4)`. -/
theorem fm_flowData_exists_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ)) :
    ∃ D : FlowData f x₀, D.R < ρ / 4 := by
  obtain ⟨g, hg, hgf⟩ := fm_cutoff hρ hf
  obtain ⟨D, hD⟩ := fm_flowData_small hg x₀ (by positivity : 0 < ρ / 4)
  exact ⟨D.transfer (fm_agree hgf hD), hD⟩

/-- **① The local flow box.** A field `C¹` on `ball x₀ ρ`, `f x₀ ≠ 0`: flow data for `f` and a flow-box chart
for it (all `IsFlowBox` properties, with `f` itself), trajectory ball inside `ball x₀ (ρ / 4)`. -/
theorem fm_flowBox_exists_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (D : FlowData f x₀) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      D.IsFlowBox H Φ ∧ D.R < ρ / 4 := by
  obtain ⟨g, hg, hgf⟩ := fm_cutoff hρ hf
  obtain ⟨D, hD⟩ := fm_flowData_small hg x₀ (by positivity : 0 < ρ / 4)
  have hfg := fm_agree hgf hD
  have hx₀ := (hfg x₀ D.fm_x₀_mem).1
  obtain ⟨H, hH⟩ := Submodule.exists_isCompl (ℝ ∙ f x₀)
  rw [hx₀] at hfx hH
  obtain ⟨Φ, hΦ⟩ := D.fm_flowBox hg hfx H hH
  exact ⟨H, D.transfer hfg, Φ, D.fm_transfer_isFlowBox hfg hΦ, hD⟩

/-- **① The usable form, without `FlowData`.** For `f` `C¹` on `ball x₀ ρ` with `f x₀ ≠ 0` there is a
flow-box chart `Φ : ℝ × H → E` at `x₀`, mapping its source into `ball x₀ (ρ / 4)`, `C¹`, with
`DΦ (0,0) (a, h) = a • f x₀ + h`, `DΦ · (1, 0) = f ∘ Φ` on the source, and a `C¹` inverse near `x₀`. -/
theorem fm_flowBox_chart_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = x₀ ∧ Φ.symm x₀ = (0, 0) ∧
      MapsTo Φ Φ.source (ball x₀ (ρ / 4)) ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ (a : ℝ) (h : H), fderiv ℝ Φ (0, 0) (a, h) = a • f x₀ + h) ∧
      (∀ p ∈ Φ.source, fderiv ℝ Φ p (1, 0) = f (Φ p)) ∧
      (∀ᶠ y in 𝓝 x₀, ContDiffAt ℝ 1 Φ.symm y) := by
  obtain ⟨H, D, Φ, hΦ, hR⟩ := fm_flowBox_exists_of_contDiffOn hρ hf hfx
  exact ⟨H, Φ, hΦ.zero_mem, hΦ.map_zero, hΦ.symm_x₀,
    fun p hp => closedBall_subset_ball hR (D.fm_isFlowBox_mem hΦ p hp), hΦ.contDiffOn,
    hΦ.fderiv_zero, hΦ.straightens, hΦ.symm_contDiffAt⟩

/-! ## ② The flow-box chart on a manifold chart -/

section Manifold

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- The chart representative of a vector field `X` in the chart at `p`: the pushforward of `X` by
`extChartAt p`, `y ↦ D(extChartAt p)_{φ⁻¹ y} (X (φ⁻¹ y))`. -/
noncomputable def chartRep (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) (y : E) : E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) ((extChartAt 𝓘(ℝ, E) p).symm y)
    (X ((extChartAt 𝓘(ℝ, E) p).symm y))

/-- Pushing the chart representative back by `(extChartAt p).symm` returns `X`. -/
theorem fm_chartRep_inv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {y : E}
    (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y (chartRep (E := E) X p y) =
      X ((extChartAt 𝓘(ℝ, E) p).symm y) := by
  have h := mfderivWithin_extChartAt_symm_comp_mfderiv_extChartAt (I := 𝓘(ℝ, E)) (x := p) hy
  rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at h
  exact DFunLike.congr_fun h (X ((extChartAt 𝓘(ℝ, E) p).symm y))

/-- `(extChartAt p).symm` is manifold-differentiable on the chart target. -/
theorem fm_mdifferentiableAt_symm (p : N) {y : E} (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y := by
  have h := mdifferentiableWithinAt_extChartAt_symm (I := 𝓘(ℝ, E)) (x := p) hy
  rwa [ModelWithCorners.range_eq_univ, mdifferentiableWithinAt_univ] at h

/-- **② The flow-box chart on a manifold.** Let `X` be a vector field on `N` whose chart representative at
`p` is `C¹` on the chart target, with `X p ≠ 0`. Then there is a flow-box chart `Φ : ℝ × H → E` into the chart
target such that `ψ = (extChartAt p).symm ∘ Φ` sends `(0, 0)` to `p` and straightens `X`:
`mfderiv ψ q (1, 0) = X (ψ q)` on the source. -/
theorem fm_manifold_flowBox (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContDiffOn ℝ 1 (chartRep X p) (extChartAt 𝓘(ℝ, E) p).target) (hXp : X p ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p ∧
      ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p ∧
      MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep X p (Φ q)) ∧
      (∀ q ∈ Φ.source, mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
        X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)) := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hto : IsOpen e.target := isOpen_extChartAt_target p
  have hx0 : e p ∈ e.target := mem_extChartAt_target p
  obtain ⟨ρ, hρ, hball⟩ := Metric.isOpen_iff.1 hto _ hx0
  have hf : ContDiffOn ℝ 1 (chartRep X p) (ball (e p) ρ) := hX.mono hball
  have hep : e.symm (e p) = p := e.left_inv (mem_extChartAt_source p)
  have hfx : chartRep X p (e p) ≠ 0 := by
    intro h
    apply hXp
    have := fm_chartRep_inv X p hx0
    rw [h] at this
    have hz := (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (e p)).map_zero
    have key : ∀ z, z = p → X z = 0 → X p = 0 := by rintro z rfl h; exact h
    exact key _ hep (this.symm.trans hz)
  obtain ⟨H, Φ, h0, hΦ0, -, hmaps, hc, -, hstr, -⟩ := fm_flowBox_chart_of_contDiffOn hρ hf hfx
  have hmaps' : MapsTo Φ Φ.source e.target := fun q hq =>
    hball (ball_subset_ball (by linarith) (hmaps hq))
  refine ⟨H, Φ, h0, hΦ0, by simp [hΦ0, hep], hmaps', hc, hstr, fun q hq => ?_⟩
  have hΦd : DifferentiableAt ℝ Φ q :=
    (hc.contDiffAt (Φ.open_source.mem_nhds hq)).differentiableAt one_ne_zero
  have hy := hmaps' hq
  have key := mfderiv_comp_apply q (fm_mdifferentiableAt_symm p hy)
    (mdifferentiableAt_iff_differentiableAt.2 hΦd) ((1, 0) : ℝ × H)
  have hm : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q = fderiv ℝ Φ q := hΦd.hasFDerivAt.hasMFDerivAt.mfderiv
  have hm' : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q ((1, 0) : ℝ × H) = chartRep X p (Φ q) :=
    (DFunLike.congr_fun hm ((1, 0) : ℝ × H)).trans (hstr q hq)
  refine key.trans ?_
  rw [hm']
  exact fm_chartRep_inv X p hy

end Manifold

/-! ## ③ (b) of `lem:killing`, copied from `FlowC1.lean` and localized

The localized forms ask for `f`, `g` differentiable and the Killing equation only on the trajectory ball
`closedBall x₀ R`, and take the variational equation `D.IsVar x (D.J x)` as a hypothesis, so that they apply to
the transferred flow data of campaign 64 (where `f` is only `C¹` on a ball). The global forms of campaign 62 are
recovered as corollaries. -/

namespace FlowData

variable (D : FlowData f x₀)

/-- The flow pushes the field forward, `f (α x t) = J x t (f x)`; local form. -/
theorem fm_flow_pushes_field_loc (hfd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ f y)
    (x : E) (hx : x ∈ closedBall x₀ D.r) (hJ : D.IsVar x (D.J x))
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : f (D.α x t) = D.J x t (f x) := by
  obtain ⟨hJ0, hJd⟩ := hJ
  have key := fm_gronwall_symm (fun s => f (D.α x s) - D.J x s (f x))
    (fun s => fderiv ℝ f (D.α x s) (f (D.α x s) - D.J x s (f x))) D.τ 0 D.M 0
    (fun s hs => by
      have h1 := ((hfd _ (D.mem x hx s hs)).hasFDerivAt.comp_hasDerivWithinAt s
        (D.deriv x hx s hs))
      have h2 := (hJd s hs).clm_apply (hasDerivWithinAt_const s _ (f x))
      refine (h1.fun_sub h2).congr_deriv ?_
      simp only [map_sub, map_zero, add_zero, ContinuousLinearMap.comp_apply])
    (by simp [D.init x hx, hJ0])
    (fun s hs => by
      rw [add_zero]
      exact ((fderiv ℝ f (D.α x s)).le_opNorm _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx s hs)) (norm_nonneg _))) t ht
  rw [gronwallBound_ε0, zero_mul] at key
  exact sub_eq_zero.1 (norm_le_zero_iff.1 key)

/-- Campaign 62's `fc_flow_pushes_field`. -/
theorem fm_flow_pushes_field (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : f (D.α x t) = D.J x t (f x) :=
  D.fm_flow_pushes_field_loc (fun y _ => hf.differentiable one_ne_zero y) x hx
    (D.fm_J_spec hf x hx) t ht

/-- **Isometry**, local form: if `L_f g = 0` on the trajectory ball then `g (α x t) (J v) (J w) = g x v w`. -/
theorem fm_flow_isometry_loc (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ g y)
    (hK : ∀ y ∈ closedBall x₀ D.R, ∀ v w,
      fderiv ℝ g y (f y) v w + g y (fderiv ℝ f y v) w + g y v (fderiv ℝ f y w) = 0)
    (x : E) (hx : x ∈ closedBall x₀ D.r) (hJ : D.IsVar x (D.J x))
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) (v w : E) :
    g (D.α x t) (D.J x t v) (D.J x t w) = g x v w := by
  obtain ⟨hJ0, hJd⟩ := hJ
  set Q : ℝ → ℝ := fun s => g (D.α x s) (D.J x s v) (D.J x s w) with hQ
  have hQd : ∀ s ∈ Icc (-D.τ) D.τ, HasDerivWithinAt Q 0 (Icc (-D.τ) D.τ) s := fun s hs => by
    have h1 := HasFDerivAt.comp_hasDerivWithinAt (l := g) (f := D.α x) s
      (hg _ (D.mem x hx s hs)).hasFDerivAt (D.deriv x hx s hs)
    have h2 := (hJd s hs).clm_apply (hasDerivWithinAt_const s _ v)
    have h3 := (hJd s hs).clm_apply (hasDerivWithinAt_const s _ w)
    have hz := hK _ (D.mem x hx s hs) (D.J x s v) (D.J x s w)
    refine ((h1.clm_apply h2).clm_apply h3).congr_deriv ?_
    simp only [map_zero, add_zero, ContinuousLinearMap.comp_apply, Function.comp_apply,
      add_apply]
    linarith
  have key := fm_gronwall_symm (fun s => Q s - Q 0) (fun _ => 0) D.τ 0 0 0
    (fun s hs => (hQd s hs).sub_const _) (by simp) (fun s _ => by simp) t ht
  rw [gronwallBound_ε0_δ0] at key
  have h := sub_eq_zero.1 (norm_le_zero_iff.1 key)
  simp only [hQ] at h
  rw [h]
  simp [D.init x hx, hJ0]

/-- Campaign 62's `fc_flow_isometry`. -/
theorem fm_flow_isometry (hf : ContDiff ℝ 1 f) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g)
    (hK : ∀ x v w, fderiv ℝ g x (f x) v w + g x (fderiv ℝ f x v) w + g x v (fderiv ℝ f x w) = 0)
    (x : E) (hx : x ∈ closedBall x₀ D.r) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) (v w : E) :
    g (D.α x t) (D.J x t v) (D.J x t w) = g x v w :=
  D.fm_flow_isometry_loc g (fun y _ => hg y) (fun y _ => hK y) x hx (D.fm_J_spec hf x hx) t ht v w

/-- **In the flow box**, local form: the pulled-back metric is
`(u, u') ↦ g_y (u.1 • f y + u.2) (u'.1 • f y + u'.2)`, `y = x₀ + h`; it does not involve `λ`. -/
theorem fm_flowBox_pullback_loc (hfd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ f y)
    (hJ : ∀ x ∈ closedBall x₀ D.r, D.IsVar x (D.J x)) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ g y)
    (hK : ∀ y ∈ closedBall x₀ D.R, ∀ v w,
      fderiv ℝ g y (f y) v w + g y (fderiv ℝ f y v) w + g y v (fderiv ℝ f y w) = 0)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p : ℝ × H) (hp : p ∈ Φ.source) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') =
      g (x₀ + p.2) (u.1 • f (x₀ + p.2) + u.2) (u'.1 • f (x₀ + p.2) + u'.2) := by
  obtain ⟨ht, hy⟩ := hΦ.source_sub p hp
  have hyc := ball_subset_closedBall hy
  have htc := Ioo_subset_Icc_self ht
  have hpush := D.fm_flow_pushes_field_loc hfd _ hyc (hJ _ hyc) _ htc
  have hlin : ∀ u : ℝ × H, fderiv ℝ Φ p u = D.J (x₀ + p.2) p.1 (u.1 • f (x₀ + p.2) + u.2) := by
    intro u
    rw [hΦ.fderiv_eq p hp u, hΦ.apply_eq p hp, hpush, map_add, map_smul]
  rw [hlin, hlin, hΦ.apply_eq p hp]
  exact D.fm_flow_isometry_loc g hg hK _ hyc (hJ _ hyc) _ htc _ _

/-- Campaign 62's `fc_flowBox_pullback`. -/
theorem fm_flowBox_pullback (hf : ContDiff ℝ 1 f) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g)
    (hK : ∀ x v w, fderiv ℝ g x (f x) v w + g x (fderiv ℝ f x v) w + g x v (fderiv ℝ f x w) = 0)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p : ℝ × H) (hp : p ∈ Φ.source) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') =
      g (x₀ + p.2) (u.1 • f (x₀ + p.2) + u.2) (u'.1 • f (x₀ + p.2) + u'.2) :=
  D.fm_flowBox_pullback_loc (fun y _ => hf.differentiable one_ne_zero y)
    (fun x hx => D.fm_J_spec hf x hx) g (fun y _ => hg y) (fun y _ => hK y) hΦ p hp u u'

/-- Campaign 62's `fc_flowBox_killing`: `∂_λ g_ab = 0`. -/
theorem fm_flowBox_killing (hf : ContDiff ℝ 1 f) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g)
    (hK : ∀ x v w, fderiv ℝ g x (f x) v w + g x (fderiv ℝ f x v) w + g x v (fderiv ℝ f x w) = 0)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p q : ℝ × H) (hp : p ∈ Φ.source) (hq : q ∈ Φ.source) (hpq : p.2 = q.2) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') = g (Φ q) (fderiv ℝ Φ q u) (fderiv ℝ Φ q u') := by
  rw [D.fm_flowBox_pullback hf g hg hK hΦ p hp, D.fm_flowBox_pullback hf g hg hK hΦ q hq, hpq]

/-- The transferred flow data (campaign 64) solves the variational equation of `f`. -/
theorem fm_transfer_isVar {g : E → E} (hg : ContDiff ℝ 1 g) (D : FlowData g x₀)
    (hfg : ∀ y ∈ closedBall x₀ D.R, f y = g y ∧ fderiv ℝ f y = fderiv ℝ g y)
    (x : E) (hx : x ∈ closedBall x₀ D.r) : (D.transfer hfg).IsVar x ((D.transfer hfg).J x) := by
  rw [D.fm_transfer_J hfg x hx]
  obtain ⟨h0, hd⟩ := D.fm_J_spec hg x hx
  unfold IsVar
  dsimp only [transfer]
  exact ⟨h0, fun t ht => by rw [(hfg _ (D.mem x hx t ht)).2]; exact hd t ht⟩

end FlowData

/-- **The local flow box, with the variational equation.** As `fm_flowBox_exists_of_contDiffOn`, and the flow
data solve the variational equation of `f` on `closedBall x₀ r`. -/
theorem fm_flowBox_exists_of_contDiffOn_var {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (D : FlowData f x₀) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      D.IsFlowBox H Φ ∧ D.R < ρ / 4 ∧ ∀ x ∈ closedBall x₀ D.r, D.IsVar x (D.J x) := by
  obtain ⟨g, hg, hgf⟩ := fm_cutoff hρ hf
  obtain ⟨D, hD⟩ := fm_flowData_small hg x₀ (by positivity : 0 < ρ / 4)
  have hfg := fm_agree hgf hD
  have hx₀ := (hfg x₀ D.fm_x₀_mem).1
  obtain ⟨H, hH⟩ := Submodule.exists_isCompl (ℝ ∙ f x₀)
  rw [hx₀] at hfx hH
  obtain ⟨Φ, hΦ⟩ := D.fm_flowBox hg hfx H hH
  exact ⟨H, D.transfer hfg, Φ, D.fm_transfer_isFlowBox hfg hΦ, hD,
    fun x hx => FlowData.fm_transfer_isVar hg D hfg x hx⟩

/-- **`lem:killing` (b) for the local flow box.** `f` `C¹` on `ball x₀ ρ`, `f x₀ ≠ 0`, `g` differentiable on the
ball with `L_f g = 0` there. Then there is a flow-box chart `Φ` into `ball x₀ (ρ / 4)` with `DΦ · (1, 0) = f ∘ Φ`
in which the pulled-back metric is `g_{x₀+h} (u.1 • f + u.2) (u'.1 • f + u'.2)`: `λ`-independent. -/
theorem fm_flowBox_killing_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) (g : E → E →L[ℝ] E →L[ℝ] ℝ) (hg : DifferentiableOn ℝ g (ball x₀ ρ))
    (hK : ∀ y ∈ ball x₀ ρ, ∀ v w,
      fderiv ℝ g y (f y) v w + g y (fderiv ℝ f y v) w + g y v (fderiv ℝ f y w) = 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = x₀ ∧ MapsTo Φ Φ.source (ball x₀ (ρ / 4)) ∧
      ContDiffOn ℝ 1 Φ Φ.source ∧ (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = f (Φ q)) ∧
      (∀ q ∈ Φ.source, x₀ + (q.2 : E) ∈ ball x₀ (ρ / 4)) ∧
      ∀ q ∈ Φ.source, ∀ u u' : ℝ × H, g (Φ q) (fderiv ℝ Φ q u) (fderiv ℝ Φ q u') =
        g (x₀ + q.2) (u.1 • f (x₀ + q.2) + u.2) (u'.1 • f (x₀ + q.2) + u'.2) := by
  obtain ⟨H, D, Φ, hΦ, hR, hJ⟩ := fm_flowBox_exists_of_contDiffOn_var hρ hf hfx
  have hsub : closedBall x₀ D.R ⊆ ball x₀ ρ :=
    (closedBall_subset_ball hR).trans (ball_subset_ball (by linarith))
  have hfd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ f y := fun y hy =>
    (hf.differentiableOn one_ne_zero).differentiableAt (isOpen_ball.mem_nhds (hsub hy))
  have hgd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ g y := fun y hy =>
    hg.differentiableAt (isOpen_ball.mem_nhds (hsub hy))
  have hrR : ∀ q ∈ Φ.source, x₀ + (q.2 : E) ∈ closedBall x₀ D.R := fun q hq => by
    have hy := ball_subset_closedBall (hΦ.source_sub q hq).2
    have := D.mem _ hy 0 ⟨by linarith [D.τ_pos], D.τ_pos.le⟩
    rwa [D.init _ hy] at this
  exact ⟨H, Φ, hΦ.zero_mem, hΦ.map_zero,
    fun q hq => closedBall_subset_ball hR (D.fm_isFlowBox_mem hΦ q hq), hΦ.contDiffOn,
    hΦ.straightens, fun q hq => closedBall_subset_ball hR (hrR q hq),
    fun q hq u u' => D.fm_flowBox_pullback_loc hfd hJ g hgd
      (fun y hy => hK y (hsub hy)) hΦ q hq u u'⟩

/-! ## ③ (b), linked to `LieDerivProbe.lean`'s `IsKilling` (copied from `FlowC1.lean`)

`lieDerivForm`, `IsConformalKilling` and `IsKilling` are copied verbatim from `LieDerivProbe.lean` (P1, P2). -/

section LieLink

open Manifold VectorField
open scoped ContDiff

variable {E' : Type*} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  {H' : Type*} [TopologicalSpace H'] {I : ModelWithCorners ℝ E' H'}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H' M] [IsManifold I 1 M]

/-- Copied from `LieDerivProbe.lean` (P1). -/
noncomputable def lieDerivForm (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X Y Z : Π x : M, TangentSpace I x) (x : M) : ℝ :=
  (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x))
    - g x (mlieBracket I X Y x) (Z x) - g x (Y x) (mlieBracket I X Z x)

/-- Copied from `LieDerivProbe.lean` (P2). -/
def IsConformalKilling (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X : Π x : M, TangentSpace I x) (σ : M → ℝ) (x : M) : Prop :=
  ∀ Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% Y) x → CMDiffAt 1 (T% Z) x →
    lieDerivForm g X Y Z x = 2 * σ x * g x (Y x) (Z x)

/-- Copied from `LieDerivProbe.lean` (P2). -/
def IsKilling (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X : Π x : M, TangentSpace I x) (x : M) : Prop :=
  IsConformalKilling g X 0 x

end LieLink

section LieLinkE

open Manifold VectorField
open scoped ContDiff

/-- Campaign 62's `fc_isKilling_lie`, with `g` differentiable only at `x`: on the model space,
`IsKilling g X x` (tested with constant fields) gives `Dg_x (X x) v w + g_x (DX_x v) w + g_x v (DX_x w) = 0`. -/
theorem fm_isKilling_lie (g : E → E →L[ℝ] E →L[ℝ] ℝ) (X : E → E) (x : E)
    (hg : DifferentiableAt ℝ g x)
    (hK : IsKilling (I := 𝓘(ℝ, E)) (M := E) g X x) (v w : E) :
    fderiv ℝ g x (X x) v w + g x (fderiv ℝ X x v) w +
      g x v (fderiv ℝ X x w) = 0 := by
  set Y : Π y : E, TangentSpace 𝓘(ℝ, E) y := fun _ => v with hY
  set Z : Π y : E, TangentSpace 𝓘(ℝ, E) y := fun _ => w with hZ
  have hYc : CMDiffAt 1 (T% Y) x := by
    rw [contMDiffAt_vectorSpace_iff_contDiffAt]; exact contDiffAt_const
  have hZc : CMDiffAt 1 (T% Z) x := by
    rw [contMDiffAt_vectorSpace_iff_contDiffAt]; exact contDiffAt_const
  have h := hK Y Z hYc hZc
  have hbr : ∀ V W : Π y : E, TangentSpace 𝓘(ℝ, E) y, mlieBracket 𝓘(ℝ, E) V W x =
      fderiv ℝ (W : E → E) x (V x) - fderiv ℝ (V : E → E) x (W x) := by
    intro V W
    rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin]
    set W' : E → E := W
    set V' : E → E := V
    show fderivWithin ℝ W' Set.univ x (V' x) - fderivWithin ℝ V' Set.univ x (W' x) = _
    rw [fderivWithin_univ, fderivWithin_univ]
  have hd : HasFDerivAt (fun y : E => (g y v) w) (((fderiv ℝ g x).flip v).flip w) x := by
    have := (hg.hasFDerivAt.clm_apply (hasFDerivAt_const v x)).clm_apply (hasFDerivAt_const w x)
    convert this using 1
    ext u; simp
  have hm : (show ℝ from mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x)) =
      fderiv ℝ (fun y : E => (g y v) w) x (X x) := by
    rw [mfderiv_eq_fderiv]
    rfl
  have key : lieDerivForm g X Y Z x = fderiv ℝ (fun y : E => (g y v) w) x (X x) -
      g x (mlieBracket 𝓘(ℝ, E) X Y x) (Z x) - g x (Y x) (mlieBracket 𝓘(ℝ, E) X Z x) :=
    congrArg (fun a : ℝ => a - g x (mlieBracket 𝓘(ℝ, E) X Y x) (Z x) -
      g x (Y x) (mlieBracket 𝓘(ℝ, E) X Z x)) hm
  have hb1 : mlieBracket 𝓘(ℝ, E) X Y x = -fderiv ℝ X x v := (hbr X Y).trans (by
    show fderiv ℝ (fun _ : E => v) x (X x) - fderiv ℝ X x v = -fderiv ℝ X x v; simp)
  have hb2 : mlieBracket 𝓘(ℝ, E) X Z x = -fderiv ℝ X x w := (hbr X Z).trans (by
    show fderiv ℝ (fun _ : E => w) x (X x) - fderiv ℝ X x w = -fderiv ℝ X x w; simp)
  have aux : ∀ b1 b2 : E, b1 = -fderiv ℝ X x v → b2 = -fderiv ℝ X x w →
      fderiv ℝ (fun y : E => (g y v) w) x (X x) - g x b1 w - g x v b2 = 2 * 0 * g x v w →
      fderiv ℝ g x (X x) v w + g x (fderiv ℝ X x v) w + g x v (fderiv ℝ X x w) = 0 := by
    rintro b1 b2 rfl rfl h
    rw [hd.fderiv] at h
    simp only [map_neg, neg_apply, ContinuousLinearMap.flip_apply, mul_zero,
      zero_mul] at h
    linarith
  rw [key] at h
  exact aux _ _ hb1 hb2 h

/-- Campaign 62's `fc_flowBox_killing_of_isKilling`. -/
theorem fm_flowBox_killing_of_isKilling (hf : ContDiff ℝ 1 f) (D : FlowData f x₀)
    (g : E → E →L[ℝ] E →L[ℝ] ℝ) (hg : Differentiable ℝ g)
    (hK : ∀ x, IsKilling (I := 𝓘(ℝ, E)) (M := E) g f x)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p : ℝ × H) (hp : p ∈ Φ.source) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') =
      g (x₀ + p.2) (u.1 • f (x₀ + p.2) + u.2) (u'.1 • f (x₀ + p.2) + u'.2) :=
  D.fm_flowBox_pullback hf g hg
    (fun x v w => fm_isKilling_lie g f x (hg x) (hK x) v w) hΦ p hp u u'

end LieLinkE

/-! ## ① The section form of the field's `C¹` hypothesis

The trivialisation of `TangentBundle 𝓘(ℝ, E) N` at `p` has fibre map `mfderiv (extChartAt p)` on the chart source
(`TangentBundle.continuousLinearMapAt_trivializationAt`), so `chartRep X p` is the trivialisation coordinate of the
section read through `(extChartAt p).symm`. `contMDiffAt_section` reads smoothness at `p` in the trivialisation at
`p` (needing only `IsManifold 𝓘(ℝ, E) 1 N`). At other points `x` of the chart, smoothness is defined through the
trivialisation at `x`; changing it to the one at `p` (`Trivialization.contMDiffOn_section_iff`) needs the tangent
bundle to be a `C¹` vector bundle, i.e. `IsManifold 𝓘(ℝ, E) 2 N`. -/

section ManifoldSection

open Manifold Bundle

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- On the chart target, `chartRep X p y` is the fibre coordinate of `⟨φ⁻¹ y, X (φ⁻¹ y)⟩` in the tangent-bundle
trivialisation at `p`. -/
theorem fm_chartRep_eq_triv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {y : E}
    (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    chartRep (E := E) X p y = (trivializationAt E (TangentSpace 𝓘(ℝ, E)) p
      (⟨(extChartAt 𝓘(ℝ, E) p).symm y, X ((extChartAt 𝓘(ℝ, E) p).symm y)⟩ :
        TangentBundle 𝓘(ℝ, E) N)).2 := by
  have hx : (extChartAt 𝓘(ℝ, E) p).symm y ∈ (chartAt E p).source := by
    rw [← extChartAt_source 𝓘(ℝ, E)]; exact (extChartAt 𝓘(ℝ, E) p).map_target hy
  rw [← Trivialization.continuousLinearMapAt_apply_of_mem (R := ℝ) _ (by simpa using hx),
    TangentBundle.continuousLinearMapAt_trivializationAt hx]
  rfl

/-- If the trivialisation coordinate (at `p`) of the section is `C¹` at a point `x` of the chart, then
`chartRep X p` is `C¹` at `φ x`. -/
theorem fm_chartRep_contDiffAt_of_triv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {x : N}
    (hx : x ∈ (chartAt E p).source)
    (hF : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E) 1 (fun z ↦ (trivializationAt E (TangentSpace 𝓘(ℝ, E)) p
      (⟨z, X z⟩ : TangentBundle 𝓘(ℝ, E) N)).2) x) :
    ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p x) := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hxs : x ∈ e.source := by rwa [extChartAt_source]
  have hy : e x ∈ e.target := e.map_source hxs
  have hto : IsOpen e.target := isOpen_extChartAt_target p
  have h1 : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E) 1 e.symm (e x) :=
    (contMDiffOn_extChartAt_symm p).contMDiffAt (hto.mem_nhds hy)
  have h2 := hF.comp_of_eq h1 (e.left_inv hxs)
  rw [contMDiffAt_iff_contDiffAt] at h2
  refine h2.congr_of_eventuallyEq ?_
  filter_upwards [hto.mem_nhds hy] with y hy'
  exact fm_chartRep_eq_triv X p hy'

/-- **① at the point.** The section `x ↦ ⟨x, X x⟩` `C¹` at `p` (into `TangentBundle 𝓘(ℝ, E) N`) gives
`chartRep X p` `C¹` at `extChartAt p p`. -/
theorem fm_chartRep_contDiffAt_of_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) :
    ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p p) :=
  fm_chartRep_contDiffAt_of_triv X p (mem_chart_source E p) ((contMDiffAt_section p).1 hX)

/-- `C¹` at `extChartAt p p` gives `C¹` on a ball around it inside the chart target. -/
theorem fm_chartRep_ball_of_contDiffAt (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p p)) :
    ∃ ρ > 0, ball (extChartAt 𝓘(ℝ, E) p p) ρ ⊆ (extChartAt 𝓘(ℝ, E) p).target ∧
      ContDiffOn ℝ 1 (chartRep (E := E) X p) (ball (extChartAt 𝓘(ℝ, E) p p) ρ) := by
  have h := (hX.eventually (by simp)).and
    ((isOpen_extChartAt_target p).mem_nhds (mem_extChartAt_target p))
  obtain ⟨ρ, hρ, hb⟩ := Metric.eventually_nhds_iff_ball.1 h
  exact ⟨ρ, hρ, fun y hy => (hb y hy).2, fun y hy => (hb y hy).1.contDiffWithinAt⟩

/-- **① on a neighbourhood.** The section `C¹` at `p` gives `chartRep X p` `C¹` on a ball around
`extChartAt p p` inside the chart target. -/
theorem fm_chartRep_ball_of_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) :
    ∃ ρ > 0, ball (extChartAt 𝓘(ℝ, E) p p) ρ ⊆ (extChartAt 𝓘(ℝ, E) p).target ∧
      ContDiffOn ℝ 1 (chartRep (E := E) X p) (ball (extChartAt 𝓘(ℝ, E) p p) ρ) :=
  fm_chartRep_ball_of_contDiffAt X p (fm_chartRep_contDiffAt_of_section X p hX)

/-- `X p ≠ 0` gives `chartRep X p (φ p) ≠ 0`. -/
theorem fm_chartRep_ne_zero (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) (hXp : X p ≠ 0) :
    chartRep (E := E) X p (extChartAt 𝓘(ℝ, E) p p) ≠ 0 := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hx0 : e p ∈ e.target := mem_extChartAt_target p
  have hep : e.symm (e p) = p := e.left_inv (mem_extChartAt_source p)
  intro h
  apply hXp
  have := fm_chartRep_inv X p hx0
  rw [h] at this
  have hz := (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (e p)).map_zero
  have key : ∀ z, z = p → X z = 0 → X p = 0 := by rintro z rfl h; exact h
  exact key _ hep (this.symm.trans hz)

/-- A chart `Φ` into the chart target with `DΦ · (1, 0) = chartRep X p ∘ Φ` straightens `X` on `N`:
`mfderiv ((extChartAt p).symm ∘ Φ) q (1, 0) = X (ψ q)`. -/
theorem fm_mfderiv_straightens (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {H : Submodule ℝ E}
    (Φ : OpenPartialHomeomorph (ℝ × H) E)
    (hmaps : MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target) (hc : ContDiffOn ℝ 1 Φ Φ.source)
    (hstr : ∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep (E := E) X p (Φ q))
    (q : ℝ × H) (hq : q ∈ Φ.source) :
    mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
      X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q) := by
  have hΦd : DifferentiableAt ℝ Φ q :=
    (hc.contDiffAt (Φ.open_source.mem_nhds hq)).differentiableAt one_ne_zero
  have hy := hmaps hq
  have key := mfderiv_comp_apply q (fm_mdifferentiableAt_symm p hy)
    (mdifferentiableAt_iff_differentiableAt.2 hΦd) ((1, 0) : ℝ × H)
  have hm : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q = fderiv ℝ Φ q := hΦd.hasFDerivAt.hasMFDerivAt.mfderiv
  have hm' : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q ((1, 0) : ℝ × H) = chartRep X p (Φ q) :=
    (DFunLike.congr_fun hm ((1, 0) : ℝ × H)).trans (hstr q hq)
  refine key.trans ?_
  rw [hm']
  exact fm_chartRep_inv X p hy

/-- **`fm_manifold_flowBox` from `C¹` at the point only.** -/
theorem fm_manifold_flowBox_of_contDiffAt (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p p)) (hXp : X p ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p ∧
      ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p ∧
      MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep X p (Φ q)) ∧
      (∀ q ∈ Φ.source, mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
        X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)) := by
  obtain ⟨ρ, hρ, hball, hf⟩ := fm_chartRep_ball_of_contDiffAt X p hX
  obtain ⟨H, Φ, h0, hΦ0, -, hmaps, hc, -, hstr, -⟩ :=
    fm_flowBox_chart_of_contDiffOn hρ hf (fm_chartRep_ne_zero X p hXp)
  have hmaps' : MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target := fun q hq =>
    hball (ball_subset_ball (by linarith) (hmaps hq))
  exact ⟨H, Φ, h0, hΦ0, by simp [hΦ0], hmaps', hc, hstr,
    fm_mfderiv_straightens X p Φ hmaps' hc hstr⟩

/-- **① `fm_manifold_flowBox` with the section hypothesis at `p`.** If the section `x ↦ ⟨x, X x⟩` of
`TangentBundle 𝓘(ℝ, E) N` is `C¹` at `p` and `X p ≠ 0`, there is a flow box `Φ` in the chart at `p` with
`ψ = (extChartAt p).symm ∘ Φ`, `ψ (0, 0) = p`, `mfderiv ψ q (1, 0) = X (ψ q)`. -/
theorem fm_manifold_flowBox_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) (hXp : X p ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p ∧
      ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p ∧
      MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep X p (Φ q)) ∧
      (∀ q ∈ Φ.source, mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
        X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)) :=
  fm_manifold_flowBox_of_contDiffAt X p (fm_chartRep_contDiffAt_of_section X p hX) hXp

end ManifoldSection

section ManifoldSection2

open Manifold Bundle

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 2 N]

/-- **① on the whole chart.** On a `C²` manifold, the section `x ↦ ⟨x, X x⟩` `C¹` on the chart source at `p`
gives `chartRep X p` `C¹` on the whole chart target. -/
theorem fm_chartRep_contDiffOn_of_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) (chartAt E p).source) :
    ContDiffOn ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p).target := by
  have : IsManifold 𝓘(ℝ, E) 1 N := IsManifold.of_le (n := 2) (by norm_num)
  intro y hy
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hxs : e.symm y ∈ e.source := e.map_target hy
  have hx : e.symm y ∈ (chartAt E p).source := by rwa [extChartAt_source] at hxs
  have hF := ((Trivialization.contMDiffOn_section_iff (trivializationAt E (TangentSpace 𝓘(ℝ, E)) p)
    (chartAt E p).open_source (by simp)).1 hX).contMDiffAt ((chartAt E p).open_source.mem_nhds hx)
  have := fm_chartRep_contDiffAt_of_triv X p hx hF
  rw [e.right_inv hy] at this
  exact this.contDiffWithinAt

/-- **① `fm_manifold_flowBox` with the section hypothesis on the chart source** (`C²` manifold): the
registered statement, through `fm_chartRep_contDiffOn_of_section` and campaign 64's `fm_manifold_flowBox`. -/
theorem fm_manifold_flowBox_sectionOn (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) (chartAt E p).source) (hXp : X p ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p ∧
      ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p ∧
      MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep X p (Φ q)) ∧
      (∀ q ∈ Φ.source, mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
        X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)) := by
  have : IsManifold 𝓘(ℝ, E) 1 N := IsManifold.of_le (n := 2) (by norm_num)
  exact fm_manifold_flowBox X p (fm_chartRep_contDiffOn_of_section X p hX) hXp

end ManifoldSection2

/-! ## ② `lem:killing` (b) on a manifold, metric and Killing condition in chart form

The metric is given in the chart at `p` as `gc : E → E →L E →L ℝ` (on the chart target), and `X` is Killing in
campaign 62's coordinate sense: `IsKilling gc (chartRep X p)` on the model space. Mathlib has no Lie derivative of
`(0,2)`-tensor fields on `N`, so the coordinate-free Killing condition on `N` is not stated. -/

section ManifoldKilling

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- A local Killing chart around `p` (the local form of campaign 59's `KillingChart`): a flow box `Φ` in the
chart at `p`, `ψ = (extChartAt p).symm ∘ Φ`, with `X = ∂_λ` (`mfderiv ψ q (1, 0) = X (ψ q)`) and the metric
pulled back by `Φ`, `gc (Φ q) (DΦ u) (DΦ u')`, a function `gH q.2 u u'` of the transverse coordinate only. -/
structure LocalKillingChart (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (gc : E → E →L[ℝ] E →L[ℝ] ℝ) where
  H : Submodule ℝ E
  Φ : OpenPartialHomeomorph (ℝ × H) E
  zero_mem : ((0 : ℝ), (0 : H)) ∈ Φ.source
  map_zero : Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p
  ψ_zero : ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p
  mapsTo : MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target
  contDiffOn : ContDiffOn ℝ 1 Φ Φ.source
  /-- `X = ∂_λ` on `N`. -/
  straightens : ∀ q ∈ Φ.source,
    mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
      X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)
  /-- The pulled-back metric components, as a function of `h` only. -/
  gH : H → (ℝ × H) → (ℝ × H) → ℝ
  metric_eq : ∀ q ∈ Φ.source, ∀ u u' : ℝ × H,
    gc (Φ q) (fderiv ℝ Φ q u) (fderiv ℝ Φ q u') = gH q.2 u u'

/-- `∂_λ g_ab = 0` in a local Killing chart: two source points with the same `h` see the same components. -/
theorem LocalKillingChart.fm_lambda_indep {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N}
    {gc : E → E →L[ℝ] E →L[ℝ] ℝ} (K : LocalKillingChart X p gc) (q q' : ℝ × K.H)
    (hq : q ∈ K.Φ.source) (hq' : q' ∈ K.Φ.source) (h : q.2 = q'.2) (u u' : ℝ × K.H) :
    gc (K.Φ q) (fderiv ℝ K.Φ q u) (fderiv ℝ K.Φ q u') =
      gc (K.Φ q') (fderiv ℝ K.Φ q' u) (fderiv ℝ K.Φ q' u') := by
  rw [K.metric_eq q hq, K.metric_eq q' hq', h]

/-- **② `lem:killing` (b) on a manifold.** `X` a vector field on `N` with `chartRep X p` `C¹` at `φ p`,
`X p ≠ 0`; `gc` a field of bilinear forms on the chart target, differentiable there, with `chartRep X p` Killing
for `gc` (`IsKilling`, the model-space Lie derivative) at every point of the chart target. Then there is a local
Killing chart around `p`: `X = ∂_λ`, and the pulled-back metric is
`gH h u u' = gc_{φp+h} (u.1 • X̃ + u.2) (u'.1 • X̃ + u'.2)`, `X̃ = chartRep X p (φ p + h)`, independent of `λ`. -/
theorem fm_manifold_killingChart (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (gc : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hX : ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p p)) (hXp : X p ≠ 0)
    (hgc : DifferentiableOn ℝ gc (extChartAt 𝓘(ℝ, E) p).target)
    (hK : ∀ y ∈ (extChartAt 𝓘(ℝ, E) p).target,
      IsKilling (I := 𝓘(ℝ, E)) (M := E) gc (chartRep (E := E) X p) y) :
    Nonempty (LocalKillingChart X p gc) := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hto : IsOpen e.target := isOpen_extChartAt_target p
  obtain ⟨ρ, hρ, hball, hf⟩ := fm_chartRep_ball_of_contDiffAt X p hX
  have hgd : DifferentiableOn ℝ gc (ball (e p) ρ) := hgc.mono hball
  have hKb : ∀ y ∈ ball (e p) ρ, ∀ v w, fderiv ℝ gc y (chartRep X p y) v w +
      gc y (fderiv ℝ (chartRep X p) y v) w + gc y v (fderiv ℝ (chartRep X p) y w) = 0 :=
    fun y hy v w => fm_isKilling_lie gc (chartRep X p) y
      (hgc.differentiableAt (hto.mem_nhds (hball hy))) (hK y (hball hy)) v w
  obtain ⟨H, Φ, h0, hΦ0, hmaps, hc, hstr, -, hpull⟩ :=
    fm_flowBox_killing_of_contDiffOn hρ hf (fm_chartRep_ne_zero X p hXp) gc hgd hKb
  have hmaps' : MapsTo Φ Φ.source e.target := fun q hq =>
    hball (ball_subset_ball (by linarith) (hmaps hq))
  exact ⟨⟨H, Φ, h0, hΦ0, by simp [hΦ0], hmaps', hc,
    fm_mfderiv_straightens X p Φ hmaps' hc hstr,
    fun h u u' => gc (e p + h) (u.1 • chartRep X p (e p + h) + u.2)
      (u'.1 • chartRep X p (e p + h) + u'.2),
    fun q hq u u' => hpull q hq u u'⟩⟩

/-- **② with the section hypothesis.** As `fm_manifold_killingChart`, with `X` `C¹` at `p` as a section of the
tangent bundle. -/
theorem fm_manifold_killingChart_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (gc : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) (hXp : X p ≠ 0)
    (hgc : DifferentiableOn ℝ gc (extChartAt 𝓘(ℝ, E) p).target)
    (hK : ∀ y ∈ (extChartAt 𝓘(ℝ, E) p).target,
      IsKilling (I := 𝓘(ℝ, E)) (M := E) gc (chartRep (E := E) X p) y) :
    Nonempty (LocalKillingChart X p gc) :=
  fm_manifold_killingChart X p gc (fm_chartRep_contDiffAt_of_section X p hX) hXp hgc hK

end ManifoldKilling

end FlowManifoldProbe

#print axioms FlowManifoldProbe.fm_remainder_unif
#print axioms FlowManifoldProbe.fm_local_flow
#print axioms FlowManifoldProbe.fm_flow_bounded
#print axioms FlowManifoldProbe.fm_linear_exists
#print axioms FlowManifoldProbe.fm_gronwall_fwd
#print axioms FlowManifoldProbe.fm_gronwall_symm
#print axioms FlowManifoldProbe.fm_gronwallBound_le
#print axioms FlowManifoldProbe.fm_flowData_exists
#print axioms FlowManifoldProbe.FlowData.fm_Icc_mem
#print axioms FlowManifoldProbe.FlowData.fm_alpha_continuousOn
#print axioms FlowManifoldProbe.FlowData.fm_var_exists
#print axioms FlowManifoldProbe.FlowData.fm_J_spec
#print axioms FlowManifoldProbe.FlowData.fm_C_nonneg
#print axioms FlowManifoldProbe.FlowData.fm_gb_le
#print axioms FlowManifoldProbe.FlowData.fm_J_norm_le
#print axioms FlowManifoldProbe.FlowData.fm_remainder_uniform
#print axioms FlowManifoldProbe.FlowData.fm_J_uniform
#print axioms FlowManifoldProbe.FlowData.fm_flow_hasFDerivAt
#print axioms FlowManifoldProbe.FlowData.fm_J_continuousOn
#print axioms FlowManifoldProbe.FlowData.fm_flow_contDiffOn
#print axioms FlowManifoldProbe.FlowData.fm_U_open
#print axioms FlowManifoldProbe.FlowData.fm_Dflow_apply
#print axioms FlowManifoldProbe.FlowData.fm_J_continuousAt_joint
#print axioms FlowManifoldProbe.FlowData.fm_flow_hasFDerivAt_joint
#print axioms FlowManifoldProbe.FlowData.fm_flow_continuousOn_joint
#print axioms FlowManifoldProbe.FlowData.fm_Dflow_continuousOn
#print axioms FlowManifoldProbe.FlowData.fm_flow_contDiffOn_joint
#print axioms FlowManifoldProbe.fm_flow_C1
#print axioms FlowManifoldProbe.fm_complement_equiv
#print axioms FlowManifoldProbe.FlowData.fm_flowBox
#print axioms FlowManifoldProbe.fm_flowBox_exists
#print axioms FlowManifoldProbe.fm_cutoff
#print axioms FlowManifoldProbe.fm_flowData_small
#print axioms FlowManifoldProbe.fm_agree
#print axioms FlowManifoldProbe.FlowData.fm_x₀_mem
#print axioms FlowManifoldProbe.FlowData.fm_transfer_J
#print axioms FlowManifoldProbe.FlowData.fm_isFlowBox_mem
#print axioms FlowManifoldProbe.FlowData.fm_transfer_isFlowBox
#print axioms FlowManifoldProbe.fm_flowData_exists_of_contDiffOn
#print axioms FlowManifoldProbe.fm_flowBox_exists_of_contDiffOn
#print axioms FlowManifoldProbe.fm_flowBox_chart_of_contDiffOn
#print axioms FlowManifoldProbe.fm_chartRep_inv
#print axioms FlowManifoldProbe.fm_mdifferentiableAt_symm
#print axioms FlowManifoldProbe.fm_manifold_flowBox
#print axioms FlowManifoldProbe.FlowData.fm_flow_pushes_field_loc
#print axioms FlowManifoldProbe.FlowData.fm_flow_pushes_field
#print axioms FlowManifoldProbe.FlowData.fm_flow_isometry_loc
#print axioms FlowManifoldProbe.FlowData.fm_flow_isometry
#print axioms FlowManifoldProbe.FlowData.fm_flowBox_pullback_loc
#print axioms FlowManifoldProbe.FlowData.fm_flowBox_pullback
#print axioms FlowManifoldProbe.FlowData.fm_flowBox_killing
#print axioms FlowManifoldProbe.FlowData.fm_transfer_isVar
#print axioms FlowManifoldProbe.fm_flowBox_exists_of_contDiffOn_var
#print axioms FlowManifoldProbe.fm_flowBox_killing_of_contDiffOn
#print axioms FlowManifoldProbe.fm_isKilling_lie
#print axioms FlowManifoldProbe.fm_flowBox_killing_of_isKilling
#print axioms FlowManifoldProbe.fm_chartRep_eq_triv
#print axioms FlowManifoldProbe.fm_chartRep_contDiffAt_of_triv
#print axioms FlowManifoldProbe.fm_chartRep_contDiffAt_of_section
#print axioms FlowManifoldProbe.fm_chartRep_ball_of_contDiffAt
#print axioms FlowManifoldProbe.fm_chartRep_ball_of_section
#print axioms FlowManifoldProbe.fm_chartRep_ne_zero
#print axioms FlowManifoldProbe.fm_mfderiv_straightens
#print axioms FlowManifoldProbe.fm_manifold_flowBox_of_contDiffAt
#print axioms FlowManifoldProbe.fm_manifold_flowBox_section
#print axioms FlowManifoldProbe.fm_chartRep_contDiffOn_of_section
#print axioms FlowManifoldProbe.fm_manifold_flowBox_sectionOn
#print axioms FlowManifoldProbe.LocalKillingChart.fm_lambda_indep
#print axioms FlowManifoldProbe.fm_manifold_killingChart
#print axioms FlowManifoldProbe.fm_manifold_killingChart_section

import Mathlib.Analysis.ODE.ExistUnique
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Calculus.InverseFunctionTheorem.ContDiff
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension
import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.Geometry.Manifold.VectorBundle.Tangent

/-!
# Probe `r7627+71.2` ①–②: the local `FlowData` constructor from `ContDiffOn` on a ball; the flow-box chart
on a manifold chart

Registered target: `computations/formalisation/r7627_71_campaign64/PREDICTION.md`. Base: campaign 62's
`probes/FlowC1.lean`, whose `FlowData`, Grönwall estimates and flow box (`fc_*`) are copied below under `fl_*`
names in namespace `FlowLocalProbe` (probes cannot import probes; the `③` Killing part is not copied).

New here (after the copy):
* `fl_cutoff`: a `C¹` field on `ball x₀ ρ` agrees, near every point of `ball x₀ (ρ/4)`, with the global `C¹`
  field `χ • f` (`χ` a `ContDiffBump` with radii `ρ/4`, `ρ/2`).
* `fl_flowData_small`: for a global `C¹` field, flow data whose trajectory ball `closedBall x₀ R` is as small as
  wanted (speed bound by the mean value inequality, then `τ`, `r` shrunk).
* `FlowData.transfer`: flow data for `g` turns into flow data for `f` when `f = g` to first order on
  `closedBall x₀ R`; same `α`, same `J`, same flow-box charts.
* ① `fl_flowData_exists_of_contDiffOn`, `fl_flowBox_exists_of_contDiffOn`, `fl_flowBox_chart_of_contDiffOn`.
* ② `fl_manifold_flowBox`: on a manifold modelled on `E`, the chart representative of `X` being `C¹` on the
  chart target, `ψ = (extChartAt p).symm ∘ Φ` has `mfderiv ψ q (1, 0) = X (ψ q)`.

Nothing imports this file.
-/

open Set Filter Topology Metric
open scoped NNReal

set_option linter.unusedSectionVars false

namespace FlowLocalProbe

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-! ## Copied from `SmoothFlowProbe.lean` (steps 1, 2, 4(a)), renamed -/

/-- **1.** The first-order remainder of a `C¹` map is uniformly small on a closed ball. -/
theorem fl_remainder_unif (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) (R ε : ℝ) (hε : 0 < ε) :
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
theorem fl_local_flow (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) :
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
theorem fl_flow_bounded (f : E → E) (τ r : ℝ) (α : E → ℝ → E) (L : ℝ≥0) (x₀ : E)
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
theorem fl_linear_exists [CompleteSpace F] (A : ℝ → F →L[ℝ] F) (T M : ℝ) (hT : 0 ≤ T) (hM : 0 ≤ M)
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
theorem fl_gronwall_fwd (e e' : ℝ → F) (T δ K c : ℝ)
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
theorem fl_gronwall_symm (e e' : ℝ → F) (T δ K c : ℝ)
    (he : ∀ s ∈ Icc (-T) T, HasDerivWithinAt e (e' s) (Icc (-T) T) s) (h0 : ‖e 0‖ ≤ δ)
    (hb : ∀ s ∈ Icc (-T) T, ‖e' s‖ ≤ K * ‖e s‖ + c) :
    ∀ s ∈ Icc (-T) T, ‖e s‖ ≤ gronwallBound δ K c |s| := by
  intro s hs
  rcases le_total 0 s with h | h
  · rw [abs_of_nonneg h]; exact fl_gronwall_fwd e e' T δ K c he h0 hb s ⟨h, hs.2⟩
  · have hneg : ∀ u ∈ Icc (-T) T, -u ∈ Icc (-T) T := fun u hu => ⟨by linarith [hu.2], by linarith [hu.1]⟩
    have := fl_gronwall_fwd (fun u => e (-u)) (fun u => -e' (-u)) T δ K c
      (fun u hu => by
        have := (he (-u) (hneg u hu)).scomp u ((hasDerivAt_neg u).hasDerivWithinAt)
          (fun w hw => hneg w hw)
        simpa [Function.comp_def] using this)
      (by simpa using h0) (fun u hu => by simpa using hb (-u) (hneg u hu)) (-s)
      ⟨by linarith, by linarith [hs.1]⟩
    rw [abs_of_nonpos h]; simpa using this

end Linear

/-- The Grönwall bound with `δ = 0`, linear in `c`, uniformly on `[0, T]`. -/
theorem fl_gronwallBound_le (K c x T : ℝ) (hK : 0 < K) (hc : 0 ≤ c) (hxT : x ≤ T) :
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
theorem fl_flowData_exists (hf : ContDiff ℝ 1 f) (x₀ : E) : Nonempty (FlowData f x₀) := by
  obtain ⟨τ₀, hτ₀, r, hr, α, L, hα, hL⟩ := fl_local_flow f hf x₀
  obtain ⟨R, hR⟩ := fl_flow_bounded f τ₀ r α L x₀ hα hL
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

theorem fl_Icc_mem {t : ℝ} (ht : t ∈ Icc (-D.τ) D.τ) : |t| ≤ D.τ := abs_le.2 ht

theorem fl_alpha_continuousOn (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ContinuousOn (D.α x) (Icc (-D.τ) D.τ) :=
  fun t ht => (D.deriv x hx t ht).continuousWithinAt

theorem fl_var_exists (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ∃ W, D.IsVar x W := by
  obtain ⟨W, hW0, hW⟩ := fl_linear_exists
    (fun t => ContinuousLinearMap.compL ℝ E E E (fderiv ℝ f (D.α x t))) D.τ D.M D.τ_pos.le
    D.M_pos.le D.Mτ
    ((ContinuousLinearMap.compL ℝ E E E).continuous.comp_continuousOn
      ((hf.continuous_fderiv one_ne_zero).comp_continuousOn (D.fl_alpha_continuousOn x hx)))
    (fun t ht => ContinuousLinearMap.opNorm_le_bound _ D.M_pos.le fun W =>
      ((ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))))
    (ContinuousLinearMap.id ℝ E)
  exact ⟨W, hW0, fun t ht => by simpa using hW t ht⟩

theorem fl_J_spec (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    D.IsVar x (D.J x) := by
  have h := D.fl_var_exists hf x hx
  unfold J; rw [dite_eq_left h]; exact h.choose_spec

/-- The constant of the Grönwall bound on `[-τ, τ]`. -/
noncomputable def C : ℝ := (Real.exp (D.M * D.τ) - 1) / D.M

theorem fl_C_nonneg : 0 ≤ D.C := by
  unfold C
  have : 1 ≤ Real.exp (D.M * D.τ) := Real.one_le_exp (by nlinarith [D.M_pos, D.τ_pos])
  exact div_nonneg (by linarith) D.M_pos.le

theorem fl_gb_le {c s : ℝ} (hc : 0 ≤ c) (hs : s ∈ Icc (-D.τ) D.τ) :
    gronwallBound 0 D.M c |s| ≤ c * D.C :=
  fl_gronwallBound_le _ _ _ _ D.M_pos hc (D.fl_Icc_mem hs)

/-- `‖J x s‖ ≤ exp (M τ)` on `[-τ, τ]`. -/
theorem fl_J_norm_le (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (s : ℝ) (hs : s ∈ Icc (-D.τ) D.τ) : ‖D.J x s‖ ≤ Real.exp (D.M * D.τ) := by
  obtain ⟨h0, hd⟩ := D.fl_J_spec hf x hx
  have := fl_gronwall_symm (D.J x) (fun t => (fderiv ℝ f (D.α x t)).comp (D.J x t)) D.τ 1 D.M 0 hd
    (by rw [h0]; exact ContinuousLinearMap.norm_id_le)
    (fun t ht => by
      rw [add_zero]
      exact (ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))) s hs
  rw [gronwallBound_ε0, one_mul] at this
  exact this.trans (Real.exp_le_exp.2 (mul_le_mul_of_nonneg_left (D.fl_Icc_mem hs) D.M_pos.le))

/-- **Grönwall #1, uniform in time.** `‖α y s − α x s − J x s (y − x)‖ ≤ ε ‖y − x‖` for `y` near `x`,
for every `s ∈ [-τ, τ]` at once. -/
theorem fl_remainder_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.α y s - D.α x s - D.J x s (y - x)‖ ≤ ε * ‖y - x‖ := by
  set ε' := ε / (((D.L : ℝ) + 1) * (D.C + 1)) with hε'
  have hC := D.fl_C_nonneg
  have hε'0 : 0 < ε' := by positivity
  obtain ⟨δ₀, hδ₀, hrem⟩ := fl_remainder_unif f hf x₀ D.R ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0, hJd⟩ := D.fl_J_spec hf x hx
  have hlip : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ ≤ D.L * ‖y - x‖ :=
    fun s hs => (D.lip s hs).norm_sub_le hy hx
  have hclose : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ < δ₀ := fun s hs => by
    have h1 := hlip s hs
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    nlinarith [norm_nonneg (y - x)]
  have key := fl_gronwall_symm (fun s => D.α y s - D.α x s - D.J x s (y - x))
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
  refine key.trans ((D.fl_gb_le (by positivity) hs).trans ?_)
  have : ε' * D.L * D.C ≤ ε := by
    rw [hε']
    rw [div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
    nlinarith [mul_le_mul (le_add_of_nonneg_right zero_le_one : (D.L : ℝ) ≤ D.L + 1)
      (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hC (by positivity)]
  nlinarith [norm_nonneg (y - x)]

/-- **Grönwall #2, uniform in time.** `‖J y s − J x s‖ ≤ ε` for `y` near `x`, every `s ∈ [-τ, τ]`. -/
theorem fl_J_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.J y s - D.J x s‖ ≤ ε := by
  set B := Real.exp (D.M * D.τ) with hB
  have hB0 : 0 < B := Real.exp_pos _
  have hC := D.fl_C_nonneg
  set ε' := ε / (B * (D.C + 1)) with hε'
  have hε'0 : 0 < ε' := by positivity
  have hU : UniformContinuousOn (fderiv ℝ f) (closedBall x₀ D.R) :=
    (isCompact_closedBall x₀ D.R).uniformContinuousOn_of_continuous
      (hf.continuous_fderiv one_ne_zero).continuousOn
  obtain ⟨δ₀, hδ₀, hδ⟩ := Metric.uniformContinuousOn_iff.1 hU ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0x, hJdx⟩ := D.fl_J_spec hf x hx
  obtain ⟨hJ0y, hJdy⟩ := D.fl_J_spec hf y hy
  have hDf : ∀ s ∈ Icc (-D.τ) D.τ, ‖fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)‖ ≤ ε' := by
    intro s hs
    have h1 := (D.lip s hs).norm_sub_le hy hx
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    rw [← dist_eq_norm]
    refine (hδ _ (D.mem y hy s hs) _ (D.mem x hx s hs) ?_).le
    rw [dist_eq_norm]; nlinarith [norm_nonneg (y - x)]
  have key := fl_gronwall_symm (fun s => D.J y s - D.J x s)
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
      have h5 := D.fl_J_norm_le hf x hx s hs
      nlinarith [norm_nonneg (D.J y s - D.J x s), norm_nonneg (D.J x s),
        norm_nonneg (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s))])
    s hs
  refine key.trans ((D.fl_gb_le (by positivity) hs).trans ?_)
  rw [hε', div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
  nlinarith [mul_le_mul_of_nonneg_left (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hB0.le]

/-! ## ① The flow is differentiable, and `C¹`, in the initial point -/

/-- **① (a), T3b's stop.** `y ↦ α y t` has derivative `J x t` at every `x ∈ ball x₀ r`, `t ∈ [-τ, τ]`. -/
theorem fl_flow_hasFDerivAt (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ ball x₀ D.r)
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : HasFDerivAt (fun y => D.α y t) (D.J x t) x := by
  rw [hasFDerivAt_iff_isLittleO]
  refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
  obtain ⟨δ, hδ, h⟩ := D.fl_remainder_uniform hf x (ball_subset_closedBall hx) c hc
  filter_upwards [ball_mem_nhds x hδ, isOpen_ball.mem_nhds hx] with y hy1 hy2
  rw [mem_ball, dist_eq_norm] at hy1
  exact h y (ball_subset_closedBall hy2) hy1 t ht

/-- **① (b).** The derivative `x ↦ J x t` is continuous on `closedBall x₀ r`, uniformly in `t`. -/
theorem fl_J_continuousOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContinuousOn (fun x => D.J x t) (closedBall x₀ D.r) := by
  intro x hx
  rw [Metric.continuousWithinAt_iff]
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.fl_J_uniform hf x hx (ε / 2) (half_pos hε)
  refine ⟨δ, hδ, fun y hy hyx => ?_⟩
  rw [dist_eq_norm] at hyx ⊢
  exact (h y hy hyx t ht).trans_lt (half_lt_self hε)

/-- **① (c).** For every `t ∈ [-τ, τ]`, `x ↦ α x t` is `C¹` on `ball x₀ r`. -/
theorem fl_flow_contDiffOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContDiffOn ℝ 1 (fun y => D.α y t) (ball x₀ D.r) := fun _x hx =>
  (contDiffAt_one_iff.2 ⟨fun y => D.J y t, ball x₀ D.r, isOpen_ball.mem_nhds hx,
    (D.fl_J_continuousOn hf t ht).mono ball_subset_closedBall,
    fun y hy => D.fl_flow_hasFDerivAt hf y hy t ht⟩).contDiffWithinAt

/-- The open domain of the joint statement. -/
def U : Set (ℝ × E) := Ioo (-D.τ) D.τ ×ˢ ball x₀ D.r

theorem fl_U_open : IsOpen D.U := isOpen_Ioo.prod isOpen_ball

/-- The joint derivative: `(s, h) ↦ s • f (α x t) + J x t h`. -/
noncomputable def Dflow (p : ℝ × E) : ℝ × E →L[ℝ] E :=
  (ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α p.2 p.1)) +
    (D.J p.2 p.1).comp (ContinuousLinearMap.snd ℝ ℝ E)

theorem fl_Dflow_apply (p q : ℝ × E) : D.Dflow p q = q.1 • f (D.α p.2 p.1) + D.J p.2 p.1 q.2 := by
  simp [Dflow]

/-- `(t, x) ↦ J x t` is jointly continuous on `U`. -/
theorem fl_J_continuousAt_joint (hf : ContDiff ℝ 1 f) (p : ℝ × E) (hp : p ∈ D.U) :
    ContinuousAt (fun q : ℝ × E => D.J q.2 q.1) p := by
  obtain ⟨t, x⟩ := p
  obtain ⟨ht, hx⟩ := hp
  have htI : Icc (-D.τ) D.τ ∈ 𝓝 t := Icc_mem_nhds ht.1 ht.2
  have hJt : ContinuousAt (D.J x) t :=
    (((D.fl_J_spec hf x (ball_subset_closedBall hx)).2 t (Ioo_subset_Icc_self ht)).hasDerivAt
      htI).continuousAt
  rw [Metric.continuousAt_iff']
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.fl_J_uniform hf x (ball_subset_closedBall hx) (ε / 4) (by positivity)
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
theorem fl_flow_hasFDerivAt_joint (hf : ContDiff ℝ 1 f) (p : ℝ × E) (hp : p ∈ D.U) :
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
    (((D.fl_J_spec hf x hxc).2 t (Ioo_subset_Icc_self ht)).hasDerivAt htI).continuousAt
  have hB : HasFDerivAt (fun q : ℝ × E => D.α q.2 q.1 - D.α x q.1)
      ((D.J x t).comp (ContinuousLinearMap.snd ℝ ℝ E)) (t, x) := by
    rw [hasFDerivAt_iff_isLittleO]
    refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
    obtain ⟨δ, hδ, h⟩ := D.fl_remainder_uniform hf x hxc (c / 2) (half_pos hc)
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
theorem fl_flow_continuousOn_joint (hf : ContDiff ℝ 1 f) :
    ContinuousOn (fun q : ℝ × E => D.α q.2 q.1) D.U := fun p hp =>
  (D.fl_flow_hasFDerivAt_joint hf p hp).continuousAt.continuousWithinAt

theorem fl_Dflow_continuousOn (hf : ContDiff ℝ 1 f) : ContinuousOn D.Dflow D.U := by
  have h1 : ContinuousOn (fun p : ℝ × E => f (D.α p.2 p.1)) D.U :=
    hf.continuous.comp_continuousOn (D.fl_flow_continuousOn_joint hf)
  have h2 : ContinuousOn (fun p : ℝ × E => D.J p.2 p.1) D.U := fun p hp =>
    (D.fl_J_continuousAt_joint hf p hp).continuousWithinAt
  have h3 : ContinuousOn (fun p : ℝ × E =>
      (ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α p.2 p.1))) D.U := by
    have := (ContinuousLinearMap.smulRightL ℝ (ℝ × E) E (ContinuousLinearMap.fst ℝ ℝ E)).continuous.comp_continuousOn h1
    convert this using 1
    funext p
    exact ContinuousLinearMap.ext fun q => by simp
  exact h3.add (h2.clm_comp continuousOn_const)

/-- **① (e), the registered theorem.** The flow `(t, x) ↦ α x t` is `C¹` jointly on
`Ioo (-τ) τ ×ˢ ball x₀ r`. -/
theorem fl_flow_contDiffOn_joint (hf : ContDiff ℝ 1 f) :
    ContDiffOn ℝ 1 (fun q : ℝ × E => D.α q.2 q.1) D.U := fun _p hp =>
  (contDiffAt_one_iff.2 ⟨D.Dflow, D.U, D.fl_U_open.mem_nhds hp, D.fl_Dflow_continuousOn hf,
    fun q hq => D.fl_flow_hasFDerivAt_joint hf q hq⟩).contDiffWithinAt

end FlowData

/-- **① headline, without `FlowData`.** A `C¹` field on a finite-dimensional space has a local flow
`α x t` (`x ∈ closedBall x₀ r`, `t ∈ [-τ, τ]`) that is `C¹` jointly in `(t, x)` on `Ioo (-τ) τ ×ˢ ball x₀ r`,
`C¹` in `x` for each `t ∈ [-τ, τ]`, with `x`-derivative solving the variational equation. -/
theorem fl_flow_C1 (hf : ContDiff ℝ 1 f) (x₀ : E) :
    ∃ τ > (0 : ℝ), ∃ r > (0 : ℝ), ∃ α : E → ℝ → E, ∃ J : E → ℝ → E →L[ℝ] E,
      (∀ x ∈ closedBall x₀ r, α x 0 = x ∧
        ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t) ∧
      (∀ x ∈ closedBall x₀ r, J x 0 = ContinuousLinearMap.id ℝ E ∧ ∀ t ∈ Icc (-τ) τ,
        HasDerivWithinAt (J x) ((fderiv ℝ f (α x t)).comp (J x t)) (Icc (-τ) τ) t) ∧
      (∀ x ∈ ball x₀ r, ∀ t ∈ Icc (-τ) τ, HasFDerivAt (fun y => α y t) (J x t) x) ∧
      (∀ t ∈ Icc (-τ) τ, ContDiffOn ℝ 1 (fun y => α y t) (ball x₀ r)) ∧
      ContDiffOn ℝ 1 (fun q : ℝ × E => α q.2 q.1) (Ioo (-τ) τ ×ˢ ball x₀ r) := by
  obtain ⟨D⟩ := fl_flowData_exists hf x₀
  exact ⟨D.τ, D.τ_pos, D.r, D.r_pos, D.α, D.J, fun x hx => ⟨D.init x hx, D.deriv x hx⟩,
    fun x hx => D.fl_J_spec hf x hx, fun x hx t ht => D.fl_flow_hasFDerivAt hf x hx t ht,
    fun t ht => D.fl_flow_contDiffOn hf t ht, D.fl_flow_contDiffOn_joint hf⟩

/-! ## ② The flow-box chart -/

/-- A complement `H` of `ℝ ∙ v`, `v ≠ 0`, gives `ℝ × H ≃L E`, `(a, h) ↦ a • v + h`. -/
theorem fl_complement_equiv (v : E) (hv : v ≠ 0) (H : Submodule ℝ E) (hH : IsCompl (ℝ ∙ v) H) :
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
theorem fl_flowBox (hf : ContDiff ℝ 1 f) (hfx : f x₀ ≠ 0) (H : Submodule ℝ E)
    (hH : IsCompl (ℝ ∙ f x₀) H) : ∃ Φ : OpenPartialHomeomorph (ℝ × H) E, D.IsFlowBox H Φ := by
  obtain ⟨e, he⟩ := fl_complement_equiv (f x₀) hfx H hH
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
  have hVo : IsOpen V := D.fl_U_open.preimage hgc.continuous
  have hV0 : ((0 : ℝ), (0 : H)) ∈ V := by
    show g (0, 0) ∈ D.U
    rw [hgp]
    exact ⟨⟨by linarith [D.τ_pos], D.τ_pos⟩, by simpa using D.r_pos⟩
  have hΨc : ContDiffOn ℝ 1 Ψ V := by
    rw [hΨg]; exact (D.fl_flow_contDiffOn_joint hf).comp hgc.contDiffOn fun p hp => hp
  have hΨd : ∀ p ∈ V, HasFDerivAt Ψ ((D.Dflow (g p)).comp Lg) p := fun p hp => by
    rw [hΨg]; exact (D.fl_flow_hasFDerivAt_joint hf (g p) hp).comp p (hgd p)
  have hΨu : ∀ p ∈ V, ∀ u, fderiv ℝ Ψ p u = u.1 • f (Ψ p) + D.J (x₀ + p.2) p.1 u.2 :=
    fun p hp u => by
      rw [(hΨd p hp).fderiv, ContinuousLinearMap.comp_apply, fl_Dflow_apply, hgp]
      simp [hLg, hΨ]
  have hx₀ : x₀ ∈ closedBall x₀ D.r := mem_closedBall_self D.r_pos.le
  have hD0 : (D.Dflow (g (0, 0))).comp Lg = (e : ℝ × H →L[ℝ] E) := by
    refine ContinuousLinearMap.ext fun q => ?_
    rw [ContinuousLinearMap.comp_apply, fl_Dflow_apply, hgp, ContinuousLinearEquiv.coe_coe, he]
    simp [hLg, D.init x₀ hx₀, (D.fl_J_spec hf x₀ hx₀).1]
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
theorem fl_flowBox_exists (hf : ContDiff ℝ 1 f) (x₀ : E) (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (D : FlowData f x₀) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      D.IsFlowBox H Φ := by
  obtain ⟨H, hH⟩ := Submodule.exists_isCompl (ℝ ∙ f x₀)
  obtain ⟨D⟩ := fl_flowData_exists hf x₀
  obtain ⟨Φ, hΦ⟩ := D.fl_flowBox hf hfx H hH
  exact ⟨H, D, Φ, hΦ⟩

/-! ## ① The local constructor: cutoff, small flow data, transfer -/

/-- **Cutoff.** A field `C¹` on `ball x₀ ρ` agrees, near every point of `ball x₀ (ρ / 4)`, with a global `C¹`
field: `χ • f`, `χ` a `ContDiffBump x₀` equal to `1` on `closedBall x₀ (ρ / 4)`, support `ball x₀ (ρ / 2)`. -/
theorem fl_cutoff {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ)) :
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
theorem fl_flowData_small {g : E → E} (hg : ContDiff ℝ 1 g) (x₀ : E) {R₀ : ℝ} (hR₀ : 0 < R₀) :
    ∃ D : FlowData g x₀, D.R < R₀ := by
  obtain ⟨τ₀, hτ₀, r₀, hr₀, α, L, hα, hL⟩ := fl_local_flow g hg x₀
  obtain ⟨R₁, hR₁⟩ := fl_flow_bounded g τ₀ r₀ α L x₀ hα hL
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
theorem fl_agree {g : E → E} {s R : ℝ} (hgf : ∀ y ∈ ball x₀ s, g =ᶠ[𝓝 y] f) (hR : R < s) :
    ∀ y ∈ closedBall x₀ R, f y = g y ∧ fderiv ℝ f y = fderiv ℝ g y := fun y hy =>
  ⟨(hgf y (closedBall_subset_ball hR hy)).eq_of_nhds.symm,
    (hgf y (closedBall_subset_ball hR hy)).fderiv_eq.symm⟩

namespace FlowData

variable {g : E → E}

/-- `x₀` lies in the trajectory ball. -/
theorem fl_x₀_mem (D : FlowData g x₀) : x₀ ∈ closedBall x₀ D.R := by
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
theorem fl_transfer_J (x : E) (hx : x ∈ closedBall x₀ D.r) : (D.transfer hfg).J x = D.J x := by
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
theorem fl_isFlowBox_mem {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E}
    (hΦ : D.IsFlowBox H Φ) (p : ℝ × H) (hp : p ∈ Φ.source) : Φ p ∈ closedBall x₀ D.R := by
  obtain ⟨ht, hy⟩ := hΦ.source_sub p hp
  rw [hΦ.apply_eq p hp]
  exact D.mem _ (ball_subset_closedBall hy) _ (Ioo_subset_Icc_self ht)

/-- **Transfer of the flow box.** A flow-box chart for `g` is a flow-box chart for `f`, with `f` itself in
`straightens`: `DΦ · (1, 0) = f ∘ Φ`. -/
theorem fl_transfer_isFlowBox {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E}
    (hΦ : D.IsFlowBox H Φ) : (D.transfer hfg).IsFlowBox H Φ := by
  have hx₀ := (hfg x₀ D.fl_x₀_mem).1
  refine ⟨hΦ.zero_mem, hΦ.map_zero, hΦ.symm_x₀, hΦ.source_sub, hΦ.apply_eq, hΦ.contDiffOn,
    fun a h => ?_, fun p hp u => ?_, fun p hp => ?_, hΦ.symm_contDiffAt⟩
  · rw [hx₀]; exact hΦ.fderiv_zero a h
  · obtain ⟨_, hy⟩ := hΦ.source_sub p hp
    rw [(hfg _ (D.fl_isFlowBox_mem hΦ p hp)).1,
      D.fl_transfer_J hfg _ (ball_subset_closedBall hy)]
    exact hΦ.fderiv_eq p hp u
  · rw [(hfg _ (D.fl_isFlowBox_mem hΦ p hp)).1]; exact hΦ.straightens p hp

end FlowData

/-- **① The local constructor.** A field that is `C¹` on `ball x₀ ρ` has flow data at `x₀` (for `f` itself),
with trajectory ball inside `ball x₀ (ρ / 4)`. -/
theorem fl_flowData_exists_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ)) :
    ∃ D : FlowData f x₀, D.R < ρ / 4 := by
  obtain ⟨g, hg, hgf⟩ := fl_cutoff hρ hf
  obtain ⟨D, hD⟩ := fl_flowData_small hg x₀ (by positivity : 0 < ρ / 4)
  exact ⟨D.transfer (fl_agree hgf hD), hD⟩

/-- **① The local flow box.** A field `C¹` on `ball x₀ ρ`, `f x₀ ≠ 0`: flow data for `f` and a flow-box chart
for it (all `IsFlowBox` properties, with `f` itself), trajectory ball inside `ball x₀ (ρ / 4)`. -/
theorem fl_flowBox_exists_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (D : FlowData f x₀) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      D.IsFlowBox H Φ ∧ D.R < ρ / 4 := by
  obtain ⟨g, hg, hgf⟩ := fl_cutoff hρ hf
  obtain ⟨D, hD⟩ := fl_flowData_small hg x₀ (by positivity : 0 < ρ / 4)
  have hfg := fl_agree hgf hD
  have hx₀ := (hfg x₀ D.fl_x₀_mem).1
  obtain ⟨H, hH⟩ := Submodule.exists_isCompl (ℝ ∙ f x₀)
  rw [hx₀] at hfx hH
  obtain ⟨Φ, hΦ⟩ := D.fl_flowBox hg hfx H hH
  exact ⟨H, D.transfer hfg, Φ, D.fl_transfer_isFlowBox hfg hΦ, hD⟩

/-- **① The usable form, without `FlowData`.** For `f` `C¹` on `ball x₀ ρ` with `f x₀ ≠ 0` there is a
flow-box chart `Φ : ℝ × H → E` at `x₀`, mapping its source into `ball x₀ (ρ / 4)`, `C¹`, with
`DΦ (0,0) (a, h) = a • f x₀ + h`, `DΦ · (1, 0) = f ∘ Φ` on the source, and a `C¹` inverse near `x₀`. -/
theorem fl_flowBox_chart_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = x₀ ∧ Φ.symm x₀ = (0, 0) ∧
      MapsTo Φ Φ.source (ball x₀ (ρ / 4)) ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ (a : ℝ) (h : H), fderiv ℝ Φ (0, 0) (a, h) = a • f x₀ + h) ∧
      (∀ p ∈ Φ.source, fderiv ℝ Φ p (1, 0) = f (Φ p)) ∧
      (∀ᶠ y in 𝓝 x₀, ContDiffAt ℝ 1 Φ.symm y) := by
  obtain ⟨H, D, Φ, hΦ, hR⟩ := fl_flowBox_exists_of_contDiffOn hρ hf hfx
  exact ⟨H, Φ, hΦ.zero_mem, hΦ.map_zero, hΦ.symm_x₀,
    fun p hp => closedBall_subset_ball hR (D.fl_isFlowBox_mem hΦ p hp), hΦ.contDiffOn,
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
theorem fl_chartRep_inv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {y : E}
    (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y (chartRep (E := E) X p y) =
      X ((extChartAt 𝓘(ℝ, E) p).symm y) := by
  have h := mfderivWithin_extChartAt_symm_comp_mfderiv_extChartAt (I := 𝓘(ℝ, E)) (x := p) hy
  rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at h
  exact DFunLike.congr_fun h (X ((extChartAt 𝓘(ℝ, E) p).symm y))

/-- `(extChartAt p).symm` is manifold-differentiable on the chart target. -/
theorem fl_mdifferentiableAt_symm (p : N) {y : E} (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y := by
  have h := mdifferentiableWithinAt_extChartAt_symm (I := 𝓘(ℝ, E)) (x := p) hy
  rwa [ModelWithCorners.range_eq_univ, mdifferentiableWithinAt_univ] at h

/-- **② The flow-box chart on a manifold.** Let `X` be a vector field on `N` whose chart representative at
`p` is `C¹` on the chart target, with `X p ≠ 0`. Then there is a flow-box chart `Φ : ℝ × H → E` into the chart
target such that `ψ = (extChartAt p).symm ∘ Φ` sends `(0, 0)` to `p` and straightens `X`:
`mfderiv ψ q (1, 0) = X (ψ q)` on the source. -/
theorem fl_manifold_flowBox (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
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
    have := fl_chartRep_inv X p hx0
    rw [h] at this
    have hz := (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (e p)).map_zero
    have key : ∀ z, z = p → X z = 0 → X p = 0 := by rintro z rfl h; exact h
    exact key _ hep (this.symm.trans hz)
  obtain ⟨H, Φ, h0, hΦ0, -, hmaps, hc, -, hstr, -⟩ := fl_flowBox_chart_of_contDiffOn hρ hf hfx
  have hmaps' : MapsTo Φ Φ.source e.target := fun q hq =>
    hball (ball_subset_ball (by linarith) (hmaps hq))
  refine ⟨H, Φ, h0, hΦ0, by simp [hΦ0, hep], hmaps', hc, hstr, fun q hq => ?_⟩
  have hΦd : DifferentiableAt ℝ Φ q :=
    (hc.contDiffAt (Φ.open_source.mem_nhds hq)).differentiableAt one_ne_zero
  have hy := hmaps' hq
  have key := mfderiv_comp_apply q (fl_mdifferentiableAt_symm p hy)
    (mdifferentiableAt_iff_differentiableAt.2 hΦd) ((1, 0) : ℝ × H)
  have hm : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q = fderiv ℝ Φ q := hΦd.hasFDerivAt.hasMFDerivAt.mfderiv
  have hm' : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q ((1, 0) : ℝ × H) = chartRep X p (Φ q) :=
    (DFunLike.congr_fun hm ((1, 0) : ℝ × H)).trans (hstr q hq)
  refine key.trans ?_
  rw [hm']
  exact fl_chartRep_inv X p hy

end Manifold

end FlowLocalProbe

#print axioms FlowLocalProbe.fl_remainder_unif
#print axioms FlowLocalProbe.fl_local_flow
#print axioms FlowLocalProbe.fl_flow_bounded
#print axioms FlowLocalProbe.fl_linear_exists
#print axioms FlowLocalProbe.fl_gronwall_fwd
#print axioms FlowLocalProbe.fl_gronwall_symm
#print axioms FlowLocalProbe.fl_gronwallBound_le
#print axioms FlowLocalProbe.fl_flowData_exists
#print axioms FlowLocalProbe.FlowData.fl_Icc_mem
#print axioms FlowLocalProbe.FlowData.fl_alpha_continuousOn
#print axioms FlowLocalProbe.FlowData.fl_var_exists
#print axioms FlowLocalProbe.FlowData.fl_J_spec
#print axioms FlowLocalProbe.FlowData.fl_C_nonneg
#print axioms FlowLocalProbe.FlowData.fl_gb_le
#print axioms FlowLocalProbe.FlowData.fl_J_norm_le
#print axioms FlowLocalProbe.FlowData.fl_remainder_uniform
#print axioms FlowLocalProbe.FlowData.fl_J_uniform
#print axioms FlowLocalProbe.FlowData.fl_flow_hasFDerivAt
#print axioms FlowLocalProbe.FlowData.fl_J_continuousOn
#print axioms FlowLocalProbe.FlowData.fl_flow_contDiffOn
#print axioms FlowLocalProbe.FlowData.fl_U_open
#print axioms FlowLocalProbe.FlowData.fl_Dflow_apply
#print axioms FlowLocalProbe.FlowData.fl_J_continuousAt_joint
#print axioms FlowLocalProbe.FlowData.fl_flow_hasFDerivAt_joint
#print axioms FlowLocalProbe.FlowData.fl_flow_continuousOn_joint
#print axioms FlowLocalProbe.FlowData.fl_Dflow_continuousOn
#print axioms FlowLocalProbe.FlowData.fl_flow_contDiffOn_joint
#print axioms FlowLocalProbe.fl_flow_C1
#print axioms FlowLocalProbe.fl_complement_equiv
#print axioms FlowLocalProbe.FlowData.fl_flowBox
#print axioms FlowLocalProbe.fl_flowBox_exists
#print axioms FlowLocalProbe.fl_cutoff
#print axioms FlowLocalProbe.fl_flowData_small
#print axioms FlowLocalProbe.fl_agree
#print axioms FlowLocalProbe.FlowData.fl_x₀_mem
#print axioms FlowLocalProbe.FlowData.fl_transfer_J
#print axioms FlowLocalProbe.FlowData.fl_isFlowBox_mem
#print axioms FlowLocalProbe.FlowData.fl_transfer_isFlowBox
#print axioms FlowLocalProbe.fl_flowData_exists_of_contDiffOn
#print axioms FlowLocalProbe.fl_flowBox_exists_of_contDiffOn
#print axioms FlowLocalProbe.fl_flowBox_chart_of_contDiffOn
#print axioms FlowLocalProbe.fl_chartRep_inv
#print axioms FlowLocalProbe.fl_mdifferentiableAt_symm
#print axioms FlowLocalProbe.fl_manifold_flowBox

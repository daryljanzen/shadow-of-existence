import Mathlib.Analysis.ODE.ExistUnique
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Calculus.InverseFunctionTheorem.ContDiff
import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.Geometry.Manifold.VectorBundle.Tangent

/-!
# Probe `r7619+71.2` ①–②: the flow of a `C¹` field is `C¹` in the initial point; the flow-box chart

Registered target: `computations/formalisation/r7619_71_campaign62/PREDICTION.md`. Base: the unfinished T3b probe
`probes/SmoothFlowProbe.lean`, which stopped at `flow_hasFDerivAt`. Its steps 1–2 and 4(a) are copied here
under `fc_` names (probes cannot import probes); its step 3 is re-done on the symmetric interval `[-τ, τ]` with
`HasDerivWithinAt` on the closed interval, which is what its stop note asked for.

Route.
* `FlowData f x₀`: Mathlib's Picard–Lindelöf flow `α x t` for `x ∈ closedBall x₀ r`, `t ∈ [-τ, τ]`,
  Lipschitz in `x`, inside `closedBall x₀ R` where `‖Df‖ ≤ M`, and `τ` shrunk so that `M τ ≤ 1/2`: then the
  variational equation `J′ = Df(α x t) ∘ J`, `J 0 = id` is ONE Picard–Lindelöf application on `[-τ, τ]`.
* A two-sided Grönwall (`fc_gronwall_symm`), from Mathlib's forward one by time reversal.
* Grönwall on `α y s − α x s − J x s (y − x)`, uniformly in `s`: `fc_remainder_uniform`.
* Grönwall on `J y s − J x s`, uniformly in `s`: `fc_J_uniform`.
* Hence `HasFDerivAt (α · t) (J x t) x`, `C¹` in `x`, and joint `C¹` of `(t, x) ↦ α x t` on
  `Ioo (-τ) τ ×ˢ ball x₀ r`, with derivative `(s, h) ↦ s • f (α x t) + J x t h`.
* Flow box: for `f x₀ ≠ 0` and a complement `H` of `ℝ ∙ f x₀`, `Ψ (λ, h) = α (x₀ + h) λ` has derivative
  `(a, h) ↦ a • f x₀ + h` at `0`, a linear equivalence, so the `C¹` inverse function theorem applies.
* ③ (b) on `E`: if `L_f g = 0` (coordinate-free; from `LieDerivProbe`'s `IsKilling`, copied) the flow is an
  isometry and the metric pulled back by the flow box is `λ`-independent: `∂_λ g_ab = 0`.

**Not built: the manifold transfer.** `FlowData` needs `ContDiff ℝ 1 f` on all of `E`, because Mathlib's
`exists_forall_mem_closedBall_eq_hasDerivWithinAt_lipschitzOnWith` does not export that the trajectories stay
in the Picard–Lindelöf ball (`FunSpace.compProj_mem_closedBall` is used inside and not stated), so the bound
`R` comes from compactness. A chart representative of a manifold field is `C¹` only on the chart target. The
first missing declaration is a localized constructor, `fc_flowData_exists_of_contDiffOn :
ContDiffOn ℝ 1 f (ball x₀ ρ) → Nonempty (FlowData f x₀)`.

Nothing imports this file.
-/

open Set Filter Topology Metric
open scoped NNReal

set_option linter.unusedSectionVars false

namespace FlowC1Probe

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-! ## Copied from `SmoothFlowProbe.lean` (steps 1, 2, 4(a)), renamed -/

/-- **1.** The first-order remainder of a `C¹` map is uniformly small on a closed ball. -/
theorem fc_remainder_unif (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) (R ε : ℝ) (hε : 0 < ε) :
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
theorem fc_local_flow (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) :
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
theorem fc_flow_bounded (f : E → E) (τ r : ℝ) (α : E → ℝ → E) (L : ℝ≥0) (x₀ : E)
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
theorem fc_linear_exists [CompleteSpace F] (A : ℝ → F →L[ℝ] F) (T M : ℝ) (hT : 0 ≤ T) (hM : 0 ≤ M)
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
theorem fc_gronwall_fwd (e e' : ℝ → F) (T δ K c : ℝ)
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
theorem fc_gronwall_symm (e e' : ℝ → F) (T δ K c : ℝ)
    (he : ∀ s ∈ Icc (-T) T, HasDerivWithinAt e (e' s) (Icc (-T) T) s) (h0 : ‖e 0‖ ≤ δ)
    (hb : ∀ s ∈ Icc (-T) T, ‖e' s‖ ≤ K * ‖e s‖ + c) :
    ∀ s ∈ Icc (-T) T, ‖e s‖ ≤ gronwallBound δ K c |s| := by
  intro s hs
  rcases le_total 0 s with h | h
  · rw [abs_of_nonneg h]; exact fc_gronwall_fwd e e' T δ K c he h0 hb s ⟨h, hs.2⟩
  · have hneg : ∀ u ∈ Icc (-T) T, -u ∈ Icc (-T) T := fun u hu => ⟨by linarith [hu.2], by linarith [hu.1]⟩
    have := fc_gronwall_fwd (fun u => e (-u)) (fun u => -e' (-u)) T δ K c
      (fun u hu => by
        have := (he (-u) (hneg u hu)).scomp u ((hasDerivAt_neg u).hasDerivWithinAt)
          (fun w hw => hneg w hw)
        simpa [Function.comp_def] using this)
      (by simpa using h0) (fun u hu => by simpa using hb (-u) (hneg u hu)) (-s)
      ⟨by linarith, by linarith [hs.1]⟩
    rw [abs_of_nonpos h]; simpa using this

end Linear

/-- The Grönwall bound with `δ = 0`, linear in `c`, uniformly on `[0, T]`. -/
theorem fc_gronwallBound_le (K c x T : ℝ) (hK : 0 < K) (hc : 0 ≤ c) (hxT : x ≤ T) :
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
theorem fc_flowData_exists (hf : ContDiff ℝ 1 f) (x₀ : E) : Nonempty (FlowData f x₀) := by
  obtain ⟨τ₀, hτ₀, r, hr, α, L, hα, hL⟩ := fc_local_flow f hf x₀
  obtain ⟨R, hR⟩ := fc_flow_bounded f τ₀ r α L x₀ hα hL
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

theorem fc_Icc_mem {t : ℝ} (ht : t ∈ Icc (-D.τ) D.τ) : |t| ≤ D.τ := abs_le.2 ht

theorem fc_alpha_continuousOn (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ContinuousOn (D.α x) (Icc (-D.τ) D.τ) :=
  fun t ht => (D.deriv x hx t ht).continuousWithinAt

theorem fc_var_exists (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ∃ W, D.IsVar x W := by
  obtain ⟨W, hW0, hW⟩ := fc_linear_exists
    (fun t => ContinuousLinearMap.compL ℝ E E E (fderiv ℝ f (D.α x t))) D.τ D.M D.τ_pos.le
    D.M_pos.le D.Mτ
    ((ContinuousLinearMap.compL ℝ E E E).continuous.comp_continuousOn
      ((hf.continuous_fderiv one_ne_zero).comp_continuousOn (D.fc_alpha_continuousOn x hx)))
    (fun t ht => ContinuousLinearMap.opNorm_le_bound _ D.M_pos.le fun W =>
      ((ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))))
    (ContinuousLinearMap.id ℝ E)
  exact ⟨W, hW0, fun t ht => by simpa using hW t ht⟩

theorem fc_J_spec (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    D.IsVar x (D.J x) := by
  have h := D.fc_var_exists hf x hx
  unfold J; rw [dite_eq_left h]; exact h.choose_spec

/-- The constant of the Grönwall bound on `[-τ, τ]`. -/
noncomputable def C : ℝ := (Real.exp (D.M * D.τ) - 1) / D.M

theorem fc_C_nonneg : 0 ≤ D.C := by
  unfold C
  have : 1 ≤ Real.exp (D.M * D.τ) := Real.one_le_exp (by nlinarith [D.M_pos, D.τ_pos])
  exact div_nonneg (by linarith) D.M_pos.le

theorem fc_gb_le {c s : ℝ} (hc : 0 ≤ c) (hs : s ∈ Icc (-D.τ) D.τ) :
    gronwallBound 0 D.M c |s| ≤ c * D.C :=
  fc_gronwallBound_le _ _ _ _ D.M_pos hc (D.fc_Icc_mem hs)

/-- `‖J x s‖ ≤ exp (M τ)` on `[-τ, τ]`. -/
theorem fc_J_norm_le (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (s : ℝ) (hs : s ∈ Icc (-D.τ) D.τ) : ‖D.J x s‖ ≤ Real.exp (D.M * D.τ) := by
  obtain ⟨h0, hd⟩ := D.fc_J_spec hf x hx
  have := fc_gronwall_symm (D.J x) (fun t => (fderiv ℝ f (D.α x t)).comp (D.J x t)) D.τ 1 D.M 0 hd
    (by rw [h0]; exact ContinuousLinearMap.norm_id_le)
    (fun t ht => by
      rw [add_zero]
      exact (ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))) s hs
  rw [gronwallBound_ε0, one_mul] at this
  exact this.trans (Real.exp_le_exp.2 (mul_le_mul_of_nonneg_left (D.fc_Icc_mem hs) D.M_pos.le))

/-- **Grönwall #1, uniform in time.** `‖α y s − α x s − J x s (y − x)‖ ≤ ε ‖y − x‖` for `y` near `x`,
for every `s ∈ [-τ, τ]` at once. -/
theorem fc_remainder_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.α y s - D.α x s - D.J x s (y - x)‖ ≤ ε * ‖y - x‖ := by
  set ε' := ε / (((D.L : ℝ) + 1) * (D.C + 1)) with hε'
  have hC := D.fc_C_nonneg
  have hε'0 : 0 < ε' := by positivity
  obtain ⟨δ₀, hδ₀, hrem⟩ := fc_remainder_unif f hf x₀ D.R ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0, hJd⟩ := D.fc_J_spec hf x hx
  have hlip : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ ≤ D.L * ‖y - x‖ :=
    fun s hs => (D.lip s hs).norm_sub_le hy hx
  have hclose : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ < δ₀ := fun s hs => by
    have h1 := hlip s hs
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    nlinarith [norm_nonneg (y - x)]
  have key := fc_gronwall_symm (fun s => D.α y s - D.α x s - D.J x s (y - x))
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
  refine key.trans ((D.fc_gb_le (by positivity) hs).trans ?_)
  have : ε' * D.L * D.C ≤ ε := by
    rw [hε']
    rw [div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
    nlinarith [mul_le_mul (le_add_of_nonneg_right zero_le_one : (D.L : ℝ) ≤ D.L + 1)
      (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hC (by positivity)]
  nlinarith [norm_nonneg (y - x)]

/-- **Grönwall #2, uniform in time.** `‖J y s − J x s‖ ≤ ε` for `y` near `x`, every `s ∈ [-τ, τ]`. -/
theorem fc_J_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.J y s - D.J x s‖ ≤ ε := by
  set B := Real.exp (D.M * D.τ) with hB
  have hB0 : 0 < B := Real.exp_pos _
  have hC := D.fc_C_nonneg
  set ε' := ε / (B * (D.C + 1)) with hε'
  have hε'0 : 0 < ε' := by positivity
  have hU : UniformContinuousOn (fderiv ℝ f) (closedBall x₀ D.R) :=
    (isCompact_closedBall x₀ D.R).uniformContinuousOn_of_continuous
      (hf.continuous_fderiv one_ne_zero).continuousOn
  obtain ⟨δ₀, hδ₀, hδ⟩ := Metric.uniformContinuousOn_iff.1 hU ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0x, hJdx⟩ := D.fc_J_spec hf x hx
  obtain ⟨hJ0y, hJdy⟩ := D.fc_J_spec hf y hy
  have hDf : ∀ s ∈ Icc (-D.τ) D.τ, ‖fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)‖ ≤ ε' := by
    intro s hs
    have h1 := (D.lip s hs).norm_sub_le hy hx
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    rw [← dist_eq_norm]
    refine (hδ _ (D.mem y hy s hs) _ (D.mem x hx s hs) ?_).le
    rw [dist_eq_norm]; nlinarith [norm_nonneg (y - x)]
  have key := fc_gronwall_symm (fun s => D.J y s - D.J x s)
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
      have h5 := D.fc_J_norm_le hf x hx s hs
      nlinarith [norm_nonneg (D.J y s - D.J x s), norm_nonneg (D.J x s),
        norm_nonneg (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s))])
    s hs
  refine key.trans ((D.fc_gb_le (by positivity) hs).trans ?_)
  rw [hε', div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
  nlinarith [mul_le_mul_of_nonneg_left (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hB0.le]

/-! ## ① The flow is differentiable, and `C¹`, in the initial point -/

/-- **① (a), T3b's stop.** `y ↦ α y t` has derivative `J x t` at every `x ∈ ball x₀ r`, `t ∈ [-τ, τ]`. -/
theorem fc_flow_hasFDerivAt (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ ball x₀ D.r)
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : HasFDerivAt (fun y => D.α y t) (D.J x t) x := by
  rw [hasFDerivAt_iff_isLittleO]
  refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
  obtain ⟨δ, hδ, h⟩ := D.fc_remainder_uniform hf x (ball_subset_closedBall hx) c hc
  filter_upwards [ball_mem_nhds x hδ, isOpen_ball.mem_nhds hx] with y hy1 hy2
  rw [mem_ball, dist_eq_norm] at hy1
  exact h y (ball_subset_closedBall hy2) hy1 t ht

/-- **① (b).** The derivative `x ↦ J x t` is continuous on `closedBall x₀ r`, uniformly in `t`. -/
theorem fc_J_continuousOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContinuousOn (fun x => D.J x t) (closedBall x₀ D.r) := by
  intro x hx
  rw [Metric.continuousWithinAt_iff]
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.fc_J_uniform hf x hx (ε / 2) (half_pos hε)
  refine ⟨δ, hδ, fun y hy hyx => ?_⟩
  rw [dist_eq_norm] at hyx ⊢
  exact (h y hy hyx t ht).trans_lt (half_lt_self hε)

/-- **① (c).** For every `t ∈ [-τ, τ]`, `x ↦ α x t` is `C¹` on `ball x₀ r`. -/
theorem fc_flow_contDiffOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContDiffOn ℝ 1 (fun y => D.α y t) (ball x₀ D.r) := fun _x hx =>
  (contDiffAt_one_iff.2 ⟨fun y => D.J y t, ball x₀ D.r, isOpen_ball.mem_nhds hx,
    (D.fc_J_continuousOn hf t ht).mono ball_subset_closedBall,
    fun y hy => D.fc_flow_hasFDerivAt hf y hy t ht⟩).contDiffWithinAt

/-- The open domain of the joint statement. -/
def U : Set (ℝ × E) := Ioo (-D.τ) D.τ ×ˢ ball x₀ D.r

theorem fc_U_open : IsOpen D.U := isOpen_Ioo.prod isOpen_ball

/-- The joint derivative: `(s, h) ↦ s • f (α x t) + J x t h`. -/
noncomputable def Dflow (p : ℝ × E) : ℝ × E →L[ℝ] E :=
  (ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α p.2 p.1)) +
    (D.J p.2 p.1).comp (ContinuousLinearMap.snd ℝ ℝ E)

theorem fc_Dflow_apply (p q : ℝ × E) : D.Dflow p q = q.1 • f (D.α p.2 p.1) + D.J p.2 p.1 q.2 := by
  simp [Dflow]

/-- `(t, x) ↦ J x t` is jointly continuous on `U`. -/
theorem fc_J_continuousAt_joint (hf : ContDiff ℝ 1 f) (p : ℝ × E) (hp : p ∈ D.U) :
    ContinuousAt (fun q : ℝ × E => D.J q.2 q.1) p := by
  obtain ⟨t, x⟩ := p
  obtain ⟨ht, hx⟩ := hp
  have htI : Icc (-D.τ) D.τ ∈ 𝓝 t := Icc_mem_nhds ht.1 ht.2
  have hJt : ContinuousAt (D.J x) t :=
    (((D.fc_J_spec hf x (ball_subset_closedBall hx)).2 t (Ioo_subset_Icc_self ht)).hasDerivAt
      htI).continuousAt
  rw [Metric.continuousAt_iff']
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.fc_J_uniform hf x (ball_subset_closedBall hx) (ε / 4) (by positivity)
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
theorem fc_flow_hasFDerivAt_joint (hf : ContDiff ℝ 1 f) (p : ℝ × E) (hp : p ∈ D.U) :
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
    (((D.fc_J_spec hf x hxc).2 t (Ioo_subset_Icc_self ht)).hasDerivAt htI).continuousAt
  have hB : HasFDerivAt (fun q : ℝ × E => D.α q.2 q.1 - D.α x q.1)
      ((D.J x t).comp (ContinuousLinearMap.snd ℝ ℝ E)) (t, x) := by
    rw [hasFDerivAt_iff_isLittleO]
    refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
    obtain ⟨δ, hδ, h⟩ := D.fc_remainder_uniform hf x hxc (c / 2) (half_pos hc)
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
theorem fc_flow_continuousOn_joint (hf : ContDiff ℝ 1 f) :
    ContinuousOn (fun q : ℝ × E => D.α q.2 q.1) D.U := fun p hp =>
  (D.fc_flow_hasFDerivAt_joint hf p hp).continuousAt.continuousWithinAt

theorem fc_Dflow_continuousOn (hf : ContDiff ℝ 1 f) : ContinuousOn D.Dflow D.U := by
  have h1 : ContinuousOn (fun p : ℝ × E => f (D.α p.2 p.1)) D.U :=
    hf.continuous.comp_continuousOn (D.fc_flow_continuousOn_joint hf)
  have h2 : ContinuousOn (fun p : ℝ × E => D.J p.2 p.1) D.U := fun p hp =>
    (D.fc_J_continuousAt_joint hf p hp).continuousWithinAt
  have h3 : ContinuousOn (fun p : ℝ × E =>
      (ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α p.2 p.1))) D.U := by
    have := (ContinuousLinearMap.smulRightL ℝ (ℝ × E) E (ContinuousLinearMap.fst ℝ ℝ E)).continuous.comp_continuousOn h1
    convert this using 1
    funext p
    exact ContinuousLinearMap.ext fun q => by simp
  exact h3.add (h2.clm_comp continuousOn_const)

/-- **① (e), the registered theorem.** The flow `(t, x) ↦ α x t` is `C¹` jointly on
`Ioo (-τ) τ ×ˢ ball x₀ r`. -/
theorem fc_flow_contDiffOn_joint (hf : ContDiff ℝ 1 f) :
    ContDiffOn ℝ 1 (fun q : ℝ × E => D.α q.2 q.1) D.U := fun _p hp =>
  (contDiffAt_one_iff.2 ⟨D.Dflow, D.U, D.fc_U_open.mem_nhds hp, D.fc_Dflow_continuousOn hf,
    fun q hq => D.fc_flow_hasFDerivAt_joint hf q hq⟩).contDiffWithinAt

end FlowData

/-- **① headline, without `FlowData`.** A `C¹` field on a finite-dimensional space has a local flow
`α x t` (`x ∈ closedBall x₀ r`, `t ∈ [-τ, τ]`) that is `C¹` jointly in `(t, x)` on `Ioo (-τ) τ ×ˢ ball x₀ r`,
`C¹` in `x` for each `t ∈ [-τ, τ]`, with `x`-derivative solving the variational equation. -/
theorem fc_flow_C1 (hf : ContDiff ℝ 1 f) (x₀ : E) :
    ∃ τ > (0 : ℝ), ∃ r > (0 : ℝ), ∃ α : E → ℝ → E, ∃ J : E → ℝ → E →L[ℝ] E,
      (∀ x ∈ closedBall x₀ r, α x 0 = x ∧
        ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t) ∧
      (∀ x ∈ closedBall x₀ r, J x 0 = ContinuousLinearMap.id ℝ E ∧ ∀ t ∈ Icc (-τ) τ,
        HasDerivWithinAt (J x) ((fderiv ℝ f (α x t)).comp (J x t)) (Icc (-τ) τ) t) ∧
      (∀ x ∈ ball x₀ r, ∀ t ∈ Icc (-τ) τ, HasFDerivAt (fun y => α y t) (J x t) x) ∧
      (∀ t ∈ Icc (-τ) τ, ContDiffOn ℝ 1 (fun y => α y t) (ball x₀ r)) ∧
      ContDiffOn ℝ 1 (fun q : ℝ × E => α q.2 q.1) (Ioo (-τ) τ ×ˢ ball x₀ r) := by
  obtain ⟨D⟩ := fc_flowData_exists hf x₀
  exact ⟨D.τ, D.τ_pos, D.r, D.r_pos, D.α, D.J, fun x hx => ⟨D.init x hx, D.deriv x hx⟩,
    fun x hx => D.fc_J_spec hf x hx, fun x hx t ht => D.fc_flow_hasFDerivAt hf x hx t ht,
    fun t ht => D.fc_flow_contDiffOn hf t ht, D.fc_flow_contDiffOn_joint hf⟩

/-! ## ② The flow-box chart -/

/-- A complement `H` of `ℝ ∙ v`, `v ≠ 0`, gives `ℝ × H ≃L E`, `(a, h) ↦ a • v + h`. -/
theorem fc_complement_equiv (v : E) (hv : v ≠ 0) (H : Submodule ℝ E) (hH : IsCompl (ℝ ∙ v) H) :
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
theorem fc_flowBox (hf : ContDiff ℝ 1 f) (hfx : f x₀ ≠ 0) (H : Submodule ℝ E)
    (hH : IsCompl (ℝ ∙ f x₀) H) : ∃ Φ : OpenPartialHomeomorph (ℝ × H) E, D.IsFlowBox H Φ := by
  obtain ⟨e, he⟩ := fc_complement_equiv (f x₀) hfx H hH
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
  have hVo : IsOpen V := D.fc_U_open.preimage hgc.continuous
  have hV0 : ((0 : ℝ), (0 : H)) ∈ V := by
    show g (0, 0) ∈ D.U
    rw [hgp]
    exact ⟨⟨by linarith [D.τ_pos], D.τ_pos⟩, by simpa using D.r_pos⟩
  have hΨc : ContDiffOn ℝ 1 Ψ V := by
    rw [hΨg]; exact (D.fc_flow_contDiffOn_joint hf).comp hgc.contDiffOn fun p hp => hp
  have hΨd : ∀ p ∈ V, HasFDerivAt Ψ ((D.Dflow (g p)).comp Lg) p := fun p hp => by
    rw [hΨg]; exact (D.fc_flow_hasFDerivAt_joint hf (g p) hp).comp p (hgd p)
  have hΨu : ∀ p ∈ V, ∀ u, fderiv ℝ Ψ p u = u.1 • f (Ψ p) + D.J (x₀ + p.2) p.1 u.2 :=
    fun p hp u => by
      rw [(hΨd p hp).fderiv, ContinuousLinearMap.comp_apply, fc_Dflow_apply, hgp]
      simp [hLg, hΨ]
  have hx₀ : x₀ ∈ closedBall x₀ D.r := mem_closedBall_self D.r_pos.le
  have hD0 : (D.Dflow (g (0, 0))).comp Lg = (e : ℝ × H →L[ℝ] E) := by
    refine ContinuousLinearMap.ext fun q => ?_
    rw [ContinuousLinearMap.comp_apply, fc_Dflow_apply, hgp, ContinuousLinearEquiv.coe_coe, he]
    simp [hLg, D.init x₀ hx₀, (D.fc_J_spec hf x₀ hx₀).1]
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
theorem fc_flowBox_exists (hf : ContDiff ℝ 1 f) (x₀ : E) (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (D : FlowData f x₀) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      D.IsFlowBox H Φ := by
  obtain ⟨H, hH⟩ := Submodule.exists_isCompl (ℝ ∙ f x₀)
  obtain ⟨D⟩ := fc_flowData_exists hf x₀
  obtain ⟨Φ, hΦ⟩ := D.fc_flowBox hf hfx H hH
  exact ⟨H, D, Φ, hΦ⟩

/-! ## ③ (b) of `lem:killing`, coordinate-free on `E`

For a field of bilinear forms `g : E → E →L E →L ℝ`, the Lie derivative along `f` is, coordinate-free on the
vector space, `(L_f g)_x (v, w) = Dg_x (f x) v w + g_x (Df_x v) w + g_x v (Df_x w)`. If it vanishes, the flow
is an isometry, `α x t` pushes `f x` to `f (α x t)`, and in the flow-box chart the pulled-back metric does
not depend on `λ`: `∂_λ g_ab = 0`, the hypothesis of campaign 59's `KillingChart`. -/

namespace FlowData

variable (D : FlowData f x₀)

/-- The flow pushes the field forward: `f (α x t) = J x t (f x)`. -/
theorem fc_flow_pushes_field (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : f (D.α x t) = D.J x t (f x) := by
  obtain ⟨hJ0, hJd⟩ := D.fc_J_spec hf x hx
  have key := fc_gronwall_symm (fun s => f (D.α x s) - D.J x s (f x))
    (fun s => fderiv ℝ f (D.α x s) (f (D.α x s) - D.J x s (f x))) D.τ 0 D.M 0
    (fun s hs => by
      have h1 := ((hf.differentiable one_ne_zero (D.α x s)).hasFDerivAt.comp_hasDerivWithinAt s
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

/-- **③ (b), isometry.** If `L_f g = 0` then `g (α x t) (J v) (J w) = g x v w`. -/
theorem fc_flow_isometry (hf : ContDiff ℝ 1 f) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g)
    (hK : ∀ x v w, fderiv ℝ g x (f x) v w + g x (fderiv ℝ f x v) w + g x v (fderiv ℝ f x w) = 0)
    (x : E) (hx : x ∈ closedBall x₀ D.r) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) (v w : E) :
    g (D.α x t) (D.J x t v) (D.J x t w) = g x v w := by
  obtain ⟨hJ0, hJd⟩ := D.fc_J_spec hf x hx
  set Q : ℝ → ℝ := fun s => g (D.α x s) (D.J x s v) (D.J x s w) with hQ
  have hQd : ∀ s ∈ Icc (-D.τ) D.τ, HasDerivWithinAt Q 0 (Icc (-D.τ) D.τ) s := fun s hs => by
    have h1 := HasFDerivAt.comp_hasDerivWithinAt (l := g) (f := D.α x) s (hg (D.α x s)).hasFDerivAt
      (D.deriv x hx s hs)
    have h2 := (hJd s hs).clm_apply (hasDerivWithinAt_const s _ v)
    have h3 := (hJd s hs).clm_apply (hasDerivWithinAt_const s _ w)
    have hz := hK (D.α x s) (D.J x s v) (D.J x s w)
    refine ((h1.clm_apply h2).clm_apply h3).congr_deriv ?_
    simp only [map_zero, add_zero, ContinuousLinearMap.comp_apply, Function.comp_apply,
      add_apply]
    linarith
  have key := fc_gronwall_symm (fun s => Q s - Q 0) (fun _ => 0) D.τ 0 0 0
    (fun s hs => (hQd s hs).sub_const _) (by simp) (fun s _ => by simp) t ht
  rw [gronwallBound_ε0_δ0] at key
  have h := sub_eq_zero.1 (norm_le_zero_iff.1 key)
  simp only [hQ] at h
  rw [h]
  simp [D.init x hx, hJ0]

/-- **③ (b) in the flow box.** If `L_f g = 0`, the metric pulled back by a flow-box chart is
`(u, u') ↦ g_y (u.1 • f y + u.2) (u'.1 • f y + u'.2)` with `y = x₀ + h`: it does not involve `λ`. -/
theorem fc_flowBox_pullback (hf : ContDiff ℝ 1 f) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g)
    (hK : ∀ x v w, fderiv ℝ g x (f x) v w + g x (fderiv ℝ f x v) w + g x v (fderiv ℝ f x w) = 0)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p : ℝ × H) (hp : p ∈ Φ.source) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') =
      g (x₀ + p.2) (u.1 • f (x₀ + p.2) + u.2) (u'.1 • f (x₀ + p.2) + u'.2) := by
  obtain ⟨ht, hy⟩ := hΦ.source_sub p hp
  have hyc := ball_subset_closedBall hy
  have htc := Ioo_subset_Icc_self ht
  have hpush := D.fc_flow_pushes_field hf _ hyc _ htc
  have hlin : ∀ u : ℝ × H, fderiv ℝ Φ p u = D.J (x₀ + p.2) p.1 (u.1 • f (x₀ + p.2) + u.2) := by
    intro u
    rw [hΦ.fderiv_eq p hp u, hΦ.apply_eq p hp, hpush, map_add, map_smul]
  rw [hlin, hlin, hΦ.apply_eq p hp]
  exact D.fc_flow_isometry hf g hg hK _ hyc _ htc _ _

/-- **③ (b), `∂_λ g_ab = 0`.** Two points of the chart with the same `h` see the same pulled-back metric. -/
theorem fc_flowBox_killing (hf : ContDiff ℝ 1 f) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g)
    (hK : ∀ x v w, fderiv ℝ g x (f x) v w + g x (fderiv ℝ f x v) w + g x v (fderiv ℝ f x w) = 0)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p q : ℝ × H) (hp : p ∈ Φ.source) (hq : q ∈ Φ.source) (hpq : p.2 = q.2) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') = g (Φ q) (fderiv ℝ Φ q u) (fderiv ℝ Φ q u') := by
  rw [D.fc_flowBox_pullback hf g hg hK hΦ p hp, D.fc_flowBox_pullback hf g hg hK hΦ q hq, hpq]

end FlowData

/-! ## ③ (b), linked to `LieDerivProbe.lean`'s `IsKilling`

`lieDerivForm`, `IsConformalKilling` and `IsKilling` are copied verbatim from `LieDerivProbe.lean` (P1, P2).
On the model space `E`, with constant test fields, `IsKilling` gives the coordinate-free equation `hK` used
above. -/

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

/-- On the model space, `IsKilling g X x` (with constant test fields) gives
`Dg_x (X x) v w + g_x (DX_x v) w + g_x v (DX_x w) = 0`. -/
theorem fc_isKilling_lie (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g) (X : E → E) (x : E)
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
    have := ((hg x).hasFDerivAt.clm_apply (hasFDerivAt_const v x)).clm_apply (hasFDerivAt_const w x)
    convert this using 1
    ext u; simp
  have hY0 : fderiv ℝ (Y : E → E) x = 0 := by
    show fderiv ℝ (fun _ : E => v) x = 0; simp
  have hZ0 : fderiv ℝ (Z : E → E) x = 0 := by
    show fderiv ℝ (fun _ : E => w) x = 0; simp
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

/-- **③ (b), from `IsKilling`.** If `f` is Killing for `g` at every point (in `LieDerivProbe`'s sense), the
metric pulled back by a flow-box chart does not depend on `λ`. -/
theorem fc_flowBox_killing_of_isKilling (hf : ContDiff ℝ 1 f) (D : FlowData f x₀)
    (g : E → E →L[ℝ] E →L[ℝ] ℝ) (hg : Differentiable ℝ g)
    (hK : ∀ x, IsKilling (I := 𝓘(ℝ, E)) (M := E) g f x)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p : ℝ × H) (hp : p ∈ Φ.source) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') =
      g (x₀ + p.2) (u.1 • f (x₀ + p.2) + u.2) (u'.1 • f (x₀ + p.2) + u'.2) :=
  D.fc_flowBox_pullback hf g hg
    (fun x v w => fc_isKilling_lie g hg f x (hK x) v w) hΦ p hp u u'

end LieLinkE

end FlowC1Probe

#print axioms FlowC1Probe.fc_remainder_unif
#print axioms FlowC1Probe.fc_local_flow
#print axioms FlowC1Probe.fc_flow_bounded
#print axioms FlowC1Probe.fc_linear_exists
#print axioms FlowC1Probe.fc_gronwall_fwd
#print axioms FlowC1Probe.fc_gronwall_symm
#print axioms FlowC1Probe.fc_gronwallBound_le
#print axioms FlowC1Probe.fc_flowData_exists
#print axioms FlowC1Probe.FlowData.fc_Icc_mem
#print axioms FlowC1Probe.FlowData.fc_alpha_continuousOn
#print axioms FlowC1Probe.FlowData.fc_var_exists
#print axioms FlowC1Probe.FlowData.fc_J_spec
#print axioms FlowC1Probe.FlowData.fc_C_nonneg
#print axioms FlowC1Probe.FlowData.fc_gb_le
#print axioms FlowC1Probe.FlowData.fc_J_norm_le
#print axioms FlowC1Probe.FlowData.fc_remainder_uniform
#print axioms FlowC1Probe.FlowData.fc_J_uniform
#print axioms FlowC1Probe.FlowData.fc_flow_hasFDerivAt
#print axioms FlowC1Probe.FlowData.fc_J_continuousOn
#print axioms FlowC1Probe.FlowData.fc_flow_contDiffOn
#print axioms FlowC1Probe.FlowData.fc_U_open
#print axioms FlowC1Probe.FlowData.fc_Dflow_apply
#print axioms FlowC1Probe.FlowData.fc_J_continuousAt_joint
#print axioms FlowC1Probe.FlowData.fc_flow_hasFDerivAt_joint
#print axioms FlowC1Probe.FlowData.fc_flow_continuousOn_joint
#print axioms FlowC1Probe.FlowData.fc_Dflow_continuousOn
#print axioms FlowC1Probe.FlowData.fc_flow_contDiffOn_joint
#print axioms FlowC1Probe.fc_flow_C1
#print axioms FlowC1Probe.fc_complement_equiv
#print axioms FlowC1Probe.FlowData.fc_flowBox
#print axioms FlowC1Probe.fc_flowBox_exists
#print axioms FlowC1Probe.FlowData.fc_flow_pushes_field
#print axioms FlowC1Probe.FlowData.fc_flow_isometry
#print axioms FlowC1Probe.FlowData.fc_flowBox_pullback
#print axioms FlowC1Probe.FlowData.fc_flowBox_killing
#print axioms FlowC1Probe.fc_isKilling_lie
#print axioms FlowC1Probe.fc_flowBox_killing_of_isKilling

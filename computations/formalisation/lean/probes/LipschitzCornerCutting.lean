import Mathlib

/-!
# Probe `r7635+71.2` (campaign 71, `r7635` ①): local geodesics, `exp`, the Gauss lemma, and
# local maximality of null geodesics, towards corner-cutting for Lipschitz causal curves

Registration: `computations/formalisation/r7635_71_campaign71/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. Copied, under the namespace `ShadowProbe.LipschitzCornerProbe` with
every theorem renamed `lk_`:
* from campaign 62 (`probes/FlowC1.lean`, lines 50–407): the `C¹` local flow, `FlowData`, Grönwall,
  the variational equation `J′ = Df ∘ J`, and `HasFDerivAt (α · t) (J x t) x`;
* from campaign 70 (`probes/CornerCutting.lean`): `Spacetime`, `FutTimelike`, `FutCausal`, `TStep`,
  `Chr`, nondegeneracy, `Dg` and its symmetry, the product rule for `g` along curves.

## Setting

One chart, `V` finite-dimensional, `M ⊆ V` open, `g ∈ C²` (hypothesis `ContDiff ℝ 2 S.g`).
* `Γ x u v := (g_x)⁻¹ (Koszul covector)`, through `ContinuousLinearMap.inverse`, so that `C¹`
  dependence on `x` follows from `contDiffAt_map_inverse` (campaign 70 used a `Classical.choose`).
  `lk_christoffel_koszul` is the defining identity; `lk_christoffel_contDiffAt` gives `C¹` of
  `(x,u) ↦ Γ_x(u,u)` on `M × V`.
* The spray `F(x,u) = (u, −Γ_x(u,u))` is cut off by a `ContDiffBump χ` around `p` with support in
  `M`: `cutField = χ(x) • F` is `C¹` on all of `V × V` (`lk_cutField_contDiff`), so campaign 62's
  `FlowData` applies at `(p, 0)`. This is `GeoFlow`.

## ① Local geodesics and `exp` (BUILT)

* `lk_unique` (uniqueness in the Picard–Lindelöf ball), `lk_fixed` (`(p,0)` is fixed), and
  `lk_lip_center`: trajectories from `closedBall (p,0) r₁` stay where `χ = 1` (`lk_traj_in`), so
  there the flow solves the geodesic equation (`lk_geodesic`).
* `lk_scaling`: `φ_t(p, λa) = (π₁ φ_{λt}(p,a), λ π₂ φ_{λt}(p,a))`, `λ ∈ [0,1]`.
* `expp v = π₁ φ_{s₀}(p, c v)` with `s₀ = τ/2`, `c s₀ = 1`; `lk_expp_smul`: `exp(λv)` is the radial
  geodesic. `lk_expp_hasFDerivAt` (derivative `Dexp v = π₁ ∘ J ∘ (0, c·)`), `lk_expp_contDiffAt`.
* `lk_Dexp_radial`: `D exp_p(v) v = rad v` (the radial velocity at `t = 1`), by uniqueness of
  one-sided derivatives on `[0,1]`; `lk_Dexp_zero`: **`D exp_p(0) = id`**.
* `lk_expp_localDiffeo`: `exp_p` is a `C¹` local diffeomorphism at `0` (inverse function theorem).

## ② The Gauss lemma (BUILT)

* `lk_energy_cons`: `g_x(u,u)` is constant along geodesics; `lk_energy_variation`: its derivative
  in the initial data, `Dg_x(X)(u,u) + 2 g_x(u,U) = 2 g_p(a,b)` for `(X,U) = J(0,b)`.
* `lk_gauss_flow`: `g_{x(t)}(u(t), X(t)) = t g_p(a,b)`. The derivative is
  `½ Dg(X)(u,u) + g(u,U)` by Koszul and `X′ = U` (from the variational equation, since
  `π₁ ∘ DF = π₂` where `χ = 1`). No second variation and no `C²` of the flow is used: the
  symmetry of the mixed partials comes from the variational equation itself.
* **`lk_gauss`**: `g_{exp_p v}(D exp_p(v) v, D exp_p(v) w) = g_p(v, w)`;
  `lk_rad_energy`: `g(rad v, rad v) = g_p(v,v)`.

## ③ Local maximality (BUILT IN PART)

* `NormalChart`, `Q x = g_p(exp⁻¹x, exp⁻¹x)`, the position field `P x = rad(exp⁻¹x)`.
* `lk_grad_Q`: `DQ_x = 2 g_x(P x, ·)`; `lk_P_energy`: `g(P,P) = Q`; `lk_P_ne_zero`: `P ≠ 0` off
  `p`; `lk_P_euler`: `D(exp⁻¹) P = exp⁻¹` (the Euler field in normal coordinates).
* `lk_causal_perp_null`: a causal vector orthogonal to a nonzero null vector is parallel to it.
* `lk_null_tangent`, `lk_ae_null_tangent`: a (Lipschitz) curve staying in `{Q = 0}` with causal
  velocity a.e. has velocity `∥ P` a.e.
* `lk_chr_of_timelike`, `lk_chr_of_Q_neg`: if `exp⁻¹x` is future-timelike (`Q x < 0`) and small,
  then `p ≪ x`.
* REPORTED. (a) The first missing lemma, the ray lemma in normal coordinates: a Lipschitz `σ` on
  `[0,1]` with `σ ≠ 0` on `(0,1]` and `σ′ = k σ` a.e. stays on the ray `ℝ_{>0} σ(1)`. With
  `lk_P_euler`, this would make a curve in `{Q=0}` a reparametrised radial null geodesic.
  (b) Monotonicity of `Q` along Lipschitz future-causal curves from `p`, i.e.
  `J⁺(p) ∩ U ⊆ exp_p(closed future cone)`. It needs an a.e.-derivative monotonicity (FTC for
  Lipschitz functions) and the reverse Cauchy–Schwarz sign `g(P, w) ≤ 0` for future causal `P, w`.

## ④ Generators are null geodesics (REPORTED, as registered)

This stops at ③ (a) and (b).

-/

open Set Filter Topology Metric
open scoped NNReal

set_option linter.unusedSectionVars false

namespace ShadowProbe.LipschitzCornerProbe

section FlowCopy

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-! ## Copied from campaign 62 (`probes/FlowC1.lean`, `fc_` ↦ `lk_`): the `C¹` local flow -/


/-- **1.** The first-order remainder of a `C¹` map is uniformly small on a closed ball. -/
theorem lk_remainder_unif (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) (R ε : ℝ) (hε : 0 < ε) :
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
theorem lk_local_flow (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) :
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
theorem lk_flow_bounded (f : E → E) (τ r : ℝ) (α : E → ℝ → E) (L : ℝ≥0) (x₀ : E)
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
theorem lk_linear_exists [CompleteSpace F] (A : ℝ → F →L[ℝ] F) (T M : ℝ) (hT : 0 ≤ T) (hM : 0 ≤ M)
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
theorem lk_gronwall_fwd (e e' : ℝ → F) (T δ K c : ℝ)
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
theorem lk_gronwall_symm (e e' : ℝ → F) (T δ K c : ℝ)
    (he : ∀ s ∈ Icc (-T) T, HasDerivWithinAt e (e' s) (Icc (-T) T) s) (h0 : ‖e 0‖ ≤ δ)
    (hb : ∀ s ∈ Icc (-T) T, ‖e' s‖ ≤ K * ‖e s‖ + c) :
    ∀ s ∈ Icc (-T) T, ‖e s‖ ≤ gronwallBound δ K c |s| := by
  intro s hs
  rcases le_total 0 s with h | h
  · rw [abs_of_nonneg h]; exact lk_gronwall_fwd e e' T δ K c he h0 hb s ⟨h, hs.2⟩
  · have hneg : ∀ u ∈ Icc (-T) T, -u ∈ Icc (-T) T := fun u hu => ⟨by linarith [hu.2], by linarith [hu.1]⟩
    have := lk_gronwall_fwd (fun u => e (-u)) (fun u => -e' (-u)) T δ K c
      (fun u hu => by
        have := (he (-u) (hneg u hu)).scomp u ((hasDerivAt_neg u).hasDerivWithinAt)
          (fun w hw => hneg w hw)
        simpa [Function.comp_def] using this)
      (by simpa using h0) (fun u hu => by simpa using hb (-u) (hneg u hu)) (-s)
      ⟨by linarith, by linarith [hs.1]⟩
    rw [abs_of_nonpos h]; simpa using this

end Linear

/-- The Grönwall bound with `δ = 0`, linear in `c`, uniformly on `[0, T]`. -/
theorem lk_gronwallBound_le (K c x T : ℝ) (hK : 0 < K) (hc : 0 ≤ c) (hxT : x ≤ T) :
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
theorem lk_flowData_exists (hf : ContDiff ℝ 1 f) (x₀ : E) : Nonempty (FlowData f x₀) := by
  obtain ⟨τ₀, hτ₀, r, hr, α, L, hα, hL⟩ := lk_local_flow f hf x₀
  obtain ⟨R, hR⟩ := lk_flow_bounded f τ₀ r α L x₀ hα hL
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

theorem lk_Icc_mem {t : ℝ} (ht : t ∈ Icc (-D.τ) D.τ) : |t| ≤ D.τ := abs_le.2 ht

theorem lk_alpha_continuousOn (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ContinuousOn (D.α x) (Icc (-D.τ) D.τ) :=
  fun t ht => (D.deriv x hx t ht).continuousWithinAt

theorem lk_var_exists (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ∃ W, D.IsVar x W := by
  obtain ⟨W, hW0, hW⟩ := lk_linear_exists
    (fun t => ContinuousLinearMap.compL ℝ E E E (fderiv ℝ f (D.α x t))) D.τ D.M D.τ_pos.le
    D.M_pos.le D.Mτ
    ((ContinuousLinearMap.compL ℝ E E E).continuous.comp_continuousOn
      ((hf.continuous_fderiv one_ne_zero).comp_continuousOn (D.lk_alpha_continuousOn x hx)))
    (fun t ht => ContinuousLinearMap.opNorm_le_bound _ D.M_pos.le fun W =>
      ((ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))))
    (ContinuousLinearMap.id ℝ E)
  exact ⟨W, hW0, fun t ht => by simpa using hW t ht⟩

theorem lk_J_spec (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    D.IsVar x (D.J x) := by
  have h := D.lk_var_exists hf x hx
  unfold J; rw [dite_eq_left h]; exact h.choose_spec

/-- The constant of the Grönwall bound on `[-τ, τ]`. -/
noncomputable def C : ℝ := (Real.exp (D.M * D.τ) - 1) / D.M

theorem lk_C_nonneg : 0 ≤ D.C := by
  unfold C
  have : 1 ≤ Real.exp (D.M * D.τ) := Real.one_le_exp (by nlinarith [D.M_pos, D.τ_pos])
  exact div_nonneg (by linarith) D.M_pos.le

theorem lk_gb_le {c s : ℝ} (hc : 0 ≤ c) (hs : s ∈ Icc (-D.τ) D.τ) :
    gronwallBound 0 D.M c |s| ≤ c * D.C :=
  lk_gronwallBound_le _ _ _ _ D.M_pos hc (D.lk_Icc_mem hs)

/-- `‖J x s‖ ≤ exp (M τ)` on `[-τ, τ]`. -/
theorem lk_J_norm_le (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (s : ℝ) (hs : s ∈ Icc (-D.τ) D.τ) : ‖D.J x s‖ ≤ Real.exp (D.M * D.τ) := by
  obtain ⟨h0, hd⟩ := D.lk_J_spec hf x hx
  have := lk_gronwall_symm (D.J x) (fun t => (fderiv ℝ f (D.α x t)).comp (D.J x t)) D.τ 1 D.M 0 hd
    (by rw [h0]; exact ContinuousLinearMap.norm_id_le)
    (fun t ht => by
      rw [add_zero]
      exact (ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))) s hs
  rw [gronwallBound_ε0, one_mul] at this
  exact this.trans (Real.exp_le_exp.2 (mul_le_mul_of_nonneg_left (D.lk_Icc_mem hs) D.M_pos.le))

/-- **Grönwall #1, uniform in time.** `‖α y s − α x s − J x s (y − x)‖ ≤ ε ‖y − x‖` for `y` near `x`,
for every `s ∈ [-τ, τ]` at once. -/
theorem lk_remainder_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.α y s - D.α x s - D.J x s (y - x)‖ ≤ ε * ‖y - x‖ := by
  set ε' := ε / (((D.L : ℝ) + 1) * (D.C + 1)) with hε'
  have hC := D.lk_C_nonneg
  have hε'0 : 0 < ε' := by positivity
  obtain ⟨δ₀, hδ₀, hrem⟩ := lk_remainder_unif f hf x₀ D.R ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0, hJd⟩ := D.lk_J_spec hf x hx
  have hlip : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ ≤ D.L * ‖y - x‖ :=
    fun s hs => (D.lip s hs).norm_sub_le hy hx
  have hclose : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ < δ₀ := fun s hs => by
    have h1 := hlip s hs
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    nlinarith [norm_nonneg (y - x)]
  have key := lk_gronwall_symm (fun s => D.α y s - D.α x s - D.J x s (y - x))
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
  refine key.trans ((D.lk_gb_le (by positivity) hs).trans ?_)
  have : ε' * D.L * D.C ≤ ε := by
    rw [hε']
    rw [div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
    nlinarith [mul_le_mul (le_add_of_nonneg_right zero_le_one : (D.L : ℝ) ≤ D.L + 1)
      (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hC (by positivity)]
  nlinarith [norm_nonneg (y - x)]

/-- **Grönwall #2, uniform in time.** `‖J y s − J x s‖ ≤ ε` for `y` near `x`, every `s ∈ [-τ, τ]`. -/
theorem lk_J_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.J y s - D.J x s‖ ≤ ε := by
  set B := Real.exp (D.M * D.τ) with hB
  have hB0 : 0 < B := Real.exp_pos _
  have hC := D.lk_C_nonneg
  set ε' := ε / (B * (D.C + 1)) with hε'
  have hε'0 : 0 < ε' := by positivity
  have hU : UniformContinuousOn (fderiv ℝ f) (closedBall x₀ D.R) :=
    (isCompact_closedBall x₀ D.R).uniformContinuousOn_of_continuous
      (hf.continuous_fderiv one_ne_zero).continuousOn
  obtain ⟨δ₀, hδ₀, hδ⟩ := Metric.uniformContinuousOn_iff.1 hU ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0x, hJdx⟩ := D.lk_J_spec hf x hx
  obtain ⟨hJ0y, hJdy⟩ := D.lk_J_spec hf y hy
  have hDf : ∀ s ∈ Icc (-D.τ) D.τ, ‖fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)‖ ≤ ε' := by
    intro s hs
    have h1 := (D.lip s hs).norm_sub_le hy hx
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    rw [← dist_eq_norm]
    refine (hδ _ (D.mem y hy s hs) _ (D.mem x hx s hs) ?_).le
    rw [dist_eq_norm]; nlinarith [norm_nonneg (y - x)]
  have key := lk_gronwall_symm (fun s => D.J y s - D.J x s)
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
      have h5 := D.lk_J_norm_le hf x hx s hs
      nlinarith [norm_nonneg (D.J y s - D.J x s), norm_nonneg (D.J x s),
        norm_nonneg (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s))])
    s hs
  refine key.trans ((D.lk_gb_le (by positivity) hs).trans ?_)
  rw [hε', div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
  nlinarith [mul_le_mul_of_nonneg_left (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hB0.le]

/-! ## ① The flow is differentiable, and `C¹`, in the initial point -/

/-- **① (a), T3b's stop.** `y ↦ α y t` has derivative `J x t` at every `x ∈ ball x₀ r`, `t ∈ [-τ, τ]`. -/
theorem lk_flow_hasFDerivAt (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ ball x₀ D.r)
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : HasFDerivAt (fun y => D.α y t) (D.J x t) x := by
  rw [hasFDerivAt_iff_isLittleO]
  refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
  obtain ⟨δ, hδ, h⟩ := D.lk_remainder_uniform hf x (ball_subset_closedBall hx) c hc
  filter_upwards [ball_mem_nhds x hδ, isOpen_ball.mem_nhds hx] with y hy1 hy2
  rw [mem_ball, dist_eq_norm] at hy1
  exact h y (ball_subset_closedBall hy2) hy1 t ht

/-- **① (b).** The derivative `x ↦ J x t` is continuous on `closedBall x₀ r`, uniformly in `t`. -/
theorem lk_J_continuousOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContinuousOn (fun x => D.J x t) (closedBall x₀ D.r) := by
  intro x hx
  rw [Metric.continuousWithinAt_iff]
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.lk_J_uniform hf x hx (ε / 2) (half_pos hε)
  refine ⟨δ, hδ, fun y hy hyx => ?_⟩
  rw [dist_eq_norm] at hyx ⊢
  exact (h y hy hyx t ht).trans_lt (half_lt_self hε)

/-- **① (c).** For every `t ∈ [-τ, τ]`, `x ↦ α x t` is `C¹` on `ball x₀ r`. -/
theorem lk_flow_contDiffOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContDiffOn ℝ 1 (fun y => D.α y t) (ball x₀ D.r) := fun _x hx =>
  (contDiffAt_one_iff.2 ⟨fun y => D.J y t, ball x₀ D.r, isOpen_ball.mem_nhds hx,
    (D.lk_J_continuousOn hf t ht).mono ball_subset_closedBall,
    fun y hy => D.lk_flow_hasFDerivAt hf y hy t ht⟩).contDiffWithinAt


end FlowData

end FlowCopy

/-! ## New flow facts: uniqueness in the ball, fixed points, Lipschitz bound at a fixed point -/

section FlowExtra

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
variable {f : E → E} {x₀ : E}

namespace FlowData

variable (D : FlowData f x₀)

/-- The field is `M`-Lipschitz on `closedBall x₀ R`. -/
theorem lk_field_lip (hf : ContDiff ℝ 1 f) {y z : E} (hy : y ∈ closedBall x₀ D.R)
    (hz : z ∈ closedBall x₀ D.R) : ‖f y - f z‖ ≤ D.M * ‖y - z‖ :=
  (convex_closedBall x₀ D.R).norm_image_sub_le_of_norm_fderiv_le
    (fun w _ => hf.differentiable one_ne_zero w) D.dbound hz hy

/-- **Uniqueness** (Grönwall): a solution through `x` on `[-τ, τ]` that stays in
`closedBall x₀ R` is the flow line `α x`. -/
theorem lk_unique (hf : ContDiff ℝ 1 f) {x : E} (hx : x ∈ closedBall x₀ D.r) {β : ℝ → E}
    (hβ0 : β 0 = x)
    (hβ : ∀ t ∈ Icc (-D.τ) D.τ, HasDerivWithinAt β (f (β t)) (Icc (-D.τ) D.τ) t)
    (hmem : ∀ t ∈ Icc (-D.τ) D.τ, β t ∈ closedBall x₀ D.R) :
    ∀ t ∈ Icc (-D.τ) D.τ, β t = D.α x t := by
  intro t ht
  have := lk_gronwall_symm (fun s => β s - D.α x s) (fun s => f (β s) - f (D.α x s)) D.τ 0 D.M 0
    (fun s hs => (hβ s hs).sub (D.deriv x hx s hs)) (by simp [hβ0, D.init x hx])
    (fun s hs => by rw [add_zero]; exact D.lk_field_lip hf (hmem s hs) (D.mem x hx s hs)) t ht
  rw [gronwallBound_ε0_δ0] at this
  exact sub_eq_zero.1 (norm_le_zero_iff.1 this)

theorem lk_zero_mem : (0 : ℝ) ∈ Icc (-D.τ) D.τ := ⟨by linarith [D.τ_pos], D.τ_pos.le⟩

/-- A zero of the field at the centre is a fixed point of the flow. -/
theorem lk_fixed (hf : ContDiff ℝ 1 f) (h0 : f x₀ = 0) :
    ∀ t ∈ Icc (-D.τ) D.τ, D.α x₀ t = x₀ := by
  have hx₀ : x₀ ∈ closedBall x₀ D.r := mem_closedBall_self D.r_pos.le
  have hR : x₀ ∈ closedBall x₀ D.R :=
    mem_closedBall_self (dist_nonneg.trans (D.mem x₀ hx₀ 0 D.lk_zero_mem))
  intro t ht
  refine (D.lk_unique hf hx₀ (β := fun _ => x₀) rfl
    (fun s _ => by rw [h0]; exact hasDerivWithinAt_const _ _ _) (fun s _ => hR) t ht).symm

/-- Near a fixed centre the flow moves points by at most `L ‖y − x₀‖`. -/
theorem lk_lip_center (hf : ContDiff ℝ 1 f) (h0 : f x₀ = 0) {y : E}
    (hy : y ∈ closedBall x₀ D.r) {t : ℝ} (ht : t ∈ Icc (-D.τ) D.τ) :
    ‖D.α y t - x₀‖ ≤ D.L * ‖y - x₀‖ := by
  have := (D.lip t ht).norm_sub_le hy (mem_closedBall_self D.r_pos.le)
  rwa [D.lk_fixed hf h0 t ht] at this

/-- A function with constant derivative `a` on `[-τ, τ]` is affine there (Grönwall, `K = 0`). -/
theorem lk_affine_of_deriv {φ : ℝ → ℝ} {a : ℝ}
    (hd : ∀ s ∈ Icc (-D.τ) D.τ, HasDerivWithinAt φ a (Icc (-D.τ) D.τ) s) :
    ∀ s ∈ Icc (-D.τ) D.τ, φ s = φ 0 + s * a := by
  intro s hs
  have := lk_gronwall_symm (fun s => φ s - φ 0 - s * a) (fun _ => (0 : ℝ)) D.τ 0 0 0
    (fun s hs => by
      have h := ((hd s hs).sub_const (φ 0)).sub
        (((hasDerivAt_id s).mul_const a).hasDerivWithinAt (s := Icc (-D.τ) D.τ))
      convert h using 1
      · funext x; simp
      · ring)
    (by simp) (fun s _ => by simp) s hs
  rw [gronwallBound_ε0_δ0] at this
  have := norm_le_zero_iff.1 this
  linarith

end FlowData

end FlowExtra

/-! ## The metric, Christoffel symbols via `(g_x)⁻¹`, the geodesic spray -/

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]

/-- A time-oriented Lorentzian chart (copied from campaign 70 / campaign 60). -/
structure Spacetime (V : Type*) [NormedAddCommGroup V] [NormedSpace ℝ V] where
  M : Set V
  isOpen_M : IsOpen M
  g : V → V →L[ℝ] V →L[ℝ] ℝ
  cont_g : Continuous g
  symm : ∀ x v w, g x v w = g x w v
  T : V → V
  cont_T : Continuous T
  T_timelike : ∀ x ∈ M, g x (T x) (T x) < 0
  pos_on_perp : ∀ x ∈ M, ∀ v, g x v (T x) = 0 → v ≠ 0 → 0 < g x v v

namespace Spacetime
variable (S : Spacetime V)

/-- Future-directed timelike vector at `x`. -/
def FutTimelike (x v : V) : Prop := S.g x v v < 0 ∧ S.g x v (S.T x) < 0
/-- Future-directed causal vector at `x`. -/
def FutCausal (x v : V) : Prop := S.g x v v ≤ 0 ∧ S.g x v (S.T x) < 0

/-- `g_x` is nondegenerate on `M` (copied from campaign 70). -/
theorem lk_nondegenerate {x : V} (hx : x ∈ S.M) {z : V} (hz : ∀ w, S.g x z w = 0) : z = 0 := by
  by_contra hne
  have h := S.pos_on_perp x hx z (hz _) hne
  rw [hz z] at h
  exact lt_irrefl _ h

/-- `Dg x w u v = (Dg_x · w)(u, v)`. -/
noncomputable def Dg (x w u v : V) : ℝ := fderiv ℝ S.g x w u v

/-- The derivative of a symmetric metric is symmetric in its last two slots (copied). -/
theorem lk_Dg_symm (x w u v : V) : S.Dg x w u v = S.Dg x w v u := by
  by_cases hd : DifferentiableAt ℝ S.g x
  · have h1 := (hd.hasFDerivAt.clm_apply (hasFDerivAt_const u x)).clm_apply
      (hasFDerivAt_const v x)
    have h2 := (hd.hasFDerivAt.clm_apply (hasFDerivAt_const v x)).clm_apply
      (hasFDerivAt_const u x)
    have hfun : (fun y => S.g y u v) = fun y => S.g y v u := funext fun y => S.symm y u v
    rw [hfun] at h1
    have := congrArg (fun L => L w) (h1.unique h2)
    simpa [Dg] using this
  · simp [Dg, fderiv_zero_of_not_differentiableAt hd]

theorem lk_Dg_zero (x u v : V) : S.Dg x 0 u v = 0 := by simp [Dg]

/-- The Koszul covector `w ↦ ½(Dg(u)(v,w) + Dg(v)(u,w) − Dg(w)(u,v))`, as a continuous form. -/
noncomputable def kos (x u v : V) : V →L[ℝ] ℝ :=
  (1 / 2 : ℝ) • (fderiv ℝ S.g x u v + fderiv ℝ S.g x v u - ((fderiv ℝ S.g x).flip u).flip v)

theorem lk_kos_apply (x u v w : V) :
    S.kos x u v w = (S.Dg x u v w + S.Dg x v u w - S.Dg x w u v) / 2 := by
  simp [kos, Dg]; ring

/-- **Christoffel symbols** `Γ_x(u,v) = (g_x)⁻¹ (Koszul covector)`, through Mathlib's
`ContinuousLinearMap.inverse` (so that `C¹` dependence on `x` is available). -/
noncomputable def Γ (x u v : V) : V := ContinuousLinearMap.inverse (S.g x) (S.kos x u v)

/-- On `M`, `g_x : V → V*` is a continuous linear isomorphism. -/
theorem lk_g_equiv {x : V} (hx : x ∈ S.M) :
    ∃ e : V ≃L[ℝ] (V →L[ℝ] ℝ), (e : V →L[ℝ] V →L[ℝ] ℝ) = S.g x := by
  have hinj : Function.Injective ((S.g x : V →L[ℝ] V →L[ℝ] ℝ) : V →ₗ[ℝ] (V →L[ℝ] ℝ)) := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    intro z hz
    exact S.lk_nondegenerate hx fun w => by
      have := congrArg (fun φ : V →L[ℝ] ℝ => φ w) hz; simpa using this
  have hdim : Module.finrank ℝ V = Module.finrank ℝ (V →L[ℝ] ℝ) := by
    rw [← (LinearMap.toContinuousLinearMap (𝕜 := ℝ) (E := V) (F' := ℝ)).finrank_eq]
    exact Subspace.dual_finrank_eq.symm
  refine ⟨(LinearMap.linearEquivOfInjective _ hinj hdim).toContinuousLinearEquiv, ?_⟩
  ext z w; rfl

theorem lk_g_Γ {x : V} (hx : x ∈ S.M) (u v : V) : S.g x (S.Γ x u v) = S.kos x u v := by
  obtain ⟨e, he⟩ := S.lk_g_equiv hx
  rw [Γ, ← he, ContinuousLinearMap.inverse_equiv]
  simp

/-- **Defining identity** `g(Γ(u,v), w) = ½(Dg(u)(v,w) + Dg(v)(u,w) − Dg(w)(u,v))`. -/
theorem lk_christoffel_koszul {x : V} (hx : x ∈ S.M) (u v w : V) :
    S.g x (S.Γ x u v) w = (S.Dg x u v w + S.Dg x v u w - S.Dg x w u v) / 2 := by
  rw [S.lk_g_Γ hx, lk_kos_apply]

theorem lk_christoffel_symm (x u v : V) : S.Γ x u v = S.Γ x v u := by
  have : S.kos x u v = S.kos x v u := by
    ext w; rw [lk_kos_apply, lk_kos_apply, S.lk_Dg_symm x w u v]; ring
  rw [Γ, Γ, this]

theorem lk_christoffel_quad (x u : V) (c : ℝ) : S.Γ x (c • u) (c • u) = (c ^ 2) • S.Γ x u u := by
  have : S.kos x (c • u) (c • u) = (c ^ 2) • S.kos x u u := by
    ext w
    rw [lk_kos_apply, smul_apply, lk_kos_apply]
    simp only [Dg, map_smul, smul_apply, smul_eq_mul]; ring
  rw [Γ, Γ, this, map_smul]

theorem lk_christoffel_zero (x : V) : S.Γ x 0 0 = 0 := by
  have : S.kos x 0 0 = 0 := by ext w; simp [lk_kos_apply, Dg]
  rw [Γ, this, map_zero]

/-- Product rule for `g` along curves (copied from campaign 70). -/
lemma lk_hasDerivAt_g {p u w : ℝ → V} {p' u' w' : V} {r : ℝ}
    (hg : DifferentiableAt ℝ S.g (p r)) (hp : HasDerivAt p p' r)
    (hu : HasDerivAt u u' r) (hw : HasDerivAt w w' r) :
    HasDerivAt (fun r => S.g (p r) (u r) (w r))
      (S.Dg (p r) p' (u r) (w r) + S.g (p r) u' (w r) + S.g (p r) (u r) w') r := by
  have h1 : HasDerivAt (fun r => S.g (p r)) (fderiv ℝ S.g (p r) p') r :=
    HasFDerivAt.comp_hasDerivAt (l := S.g) r hg.hasFDerivAt hp
  have := (h1.clm_apply hu).clm_apply hw
  simpa [Dg, add_assoc] using this

/-- Product rule for `g` along curves, within a set. -/
lemma lk_hasDerivWithinAt_g {s : Set ℝ} {p u w : ℝ → V} {p' u' w' : V} {r : ℝ}
    (hg : DifferentiableAt ℝ S.g (p r)) (hp : HasDerivWithinAt p p' s r)
    (hu : HasDerivWithinAt u u' s r) (hw : HasDerivWithinAt w w' s r) :
    HasDerivWithinAt (fun r => S.g (p r) (u r) (w r))
      (S.Dg (p r) p' (u r) (w r) + S.g (p r) u' (w r) + S.g (p r) (u r) w') s r := by
  have h1 : HasDerivWithinAt (fun r => S.g (p r)) (fderiv ℝ S.g (p r) p') s r :=
    HasFDerivAt.comp_hasDerivWithinAt (l := S.g) r hg.hasFDerivAt hp
  have := (h1.clm_apply hu).clm_apply hw
  simpa [Dg, add_assoc] using this

theorem lk_energy_contDiff (hg : ContDiff ℝ 2 S.g) :
    ContDiff ℝ 2 (fun y : V × V => S.g y.1 y.2 y.2) :=
  ((hg.comp contDiff_fst).clm_apply contDiff_snd).clm_apply contDiff_snd

/-- The energy `E(x, u) = g_x(u, u)` has derivative `(X, U) ↦ Dg_x(X)(u,u) + 2 g_x(u, U)`. -/
theorem lk_energy_hasFDerivAt (hg : ContDiff ℝ 2 S.g) (z : V × V) :
    ∃ L : V × V →L[ℝ] ℝ, HasFDerivAt (fun y : V × V => S.g y.1 y.2 y.2) L z ∧
      ∀ ξ : V × V, L ξ = S.Dg z.1 ξ.1 z.2 z.2 + 2 * S.g z.1 z.2 ξ.2 := by
  have hL := ((S.lk_energy_contDiff hg).differentiable (by norm_num) z).hasFDerivAt
  refine ⟨_, hL, fun ξ => ?_⟩
  have hd : DifferentiableAt ℝ S.g (z.1 + (0:ℝ) • ξ.1) := (hg.differentiable (by norm_num)) _
  have hline : HasDerivAt (fun s : ℝ => z + s • ξ) ξ 0 := by
    simpa using ((hasDerivAt_id (0:ℝ)).smul_const ξ).const_add z
  have h1 := hL.comp_hasDerivAt_of_eq (0:ℝ) hline (by simp)
  have hp : HasDerivAt (fun s : ℝ => z.1 + s • ξ.1) ξ.1 0 := by
    simpa using ((hasDerivAt_id (0:ℝ)).smul_const ξ.1).const_add z.1
  have hu : HasDerivAt (fun s : ℝ => z.2 + s • ξ.2) ξ.2 0 := by
    simpa using ((hasDerivAt_id (0:ℝ)).smul_const ξ.2).const_add z.2
  have h2 := S.lk_hasDerivAt_g hd hp hu hu
  have h3 : HasDerivAt ((fun y : V × V => S.g y.1 y.2 y.2) ∘ fun s : ℝ => z + s • ξ)
      (S.Dg (z.1 + (0:ℝ) • ξ.1) ξ.1 (z.2 + (0:ℝ) • ξ.2) (z.2 + (0:ℝ) • ξ.2) +
        S.g (z.1 + (0:ℝ) • ξ.1) ξ.2 (z.2 + (0:ℝ) • ξ.2) +
        S.g (z.1 + (0:ℝ) • ξ.1) (z.2 + (0:ℝ) • ξ.2) ξ.2) 0 := by
    convert h2 using 1
    funext r; simp [Function.comp]
  have := h1.unique h3
  simp only [zero_smul, add_zero] at this
  rw [this, S.symm z.1 ξ.2 z.2]; ring

/-- For `g ∈ C²`, `(x, u) ↦ Γ_x(u,u)` is `C¹` near every point of `M × V`. -/
theorem lk_christoffel_contDiffAt (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ S.M) (u : V) :
    ContDiffAt ℝ 1 (fun z : V × V => S.Γ z.1 z.2 z.2) (x, u) := by
  obtain ⟨e, he⟩ := S.lk_g_equiv hx
  have h1 : ContDiffAt ℝ 1 (fun z : V × V => ContinuousLinearMap.inverse (S.g z.1)) (x, u) := by
    have := contDiffAt_map_inverse (𝕜 := ℝ) (n := 1) e
    rw [he] at this
    exact this.comp (x, u) ((hg.of_le (by norm_num)).contDiffAt.comp (x, u) contDiffAt_fst)
  have hE : ContDiff ℝ 2 (fun y : V × V => S.g y.1 y.2 y.2) :=
    ((hg.comp contDiff_fst).clm_apply contDiff_snd).clm_apply contDiff_snd
  have hT1 : ContDiff ℝ 1 (fun z : V × V => fderiv ℝ S.g z.1 z.2) :=
    ContDiff.fderiv_apply (f := fun _ : V × V => S.g) (by exact hg.comp contDiff_snd)
      contDiff_fst contDiff_snd (by norm_num)
  have hT3 : ContDiff ℝ 1 (fun z : V × V =>
      (fderiv ℝ (fun y : V × V => S.g y.1 y.2 y.2) z).comp (ContinuousLinearMap.inl ℝ V V)) :=
    (hE.fderiv_right (m := 1) (by norm_num)).clm_comp contDiff_const
  have hk : (fun z : V × V => S.kos z.1 z.2 z.2) = fun z => (1 / 2 : ℝ) •
      (fderiv ℝ S.g z.1 z.2 z.2 + fderiv ℝ S.g z.1 z.2 z.2 -
        (fderiv ℝ (fun y : V × V => S.g y.1 y.2 y.2) z).comp (ContinuousLinearMap.inl ℝ V V)) := by
    funext z; ext w
    obtain ⟨L, hL, hLv⟩ := S.lk_energy_hasFDerivAt hg z
    rw [lk_kos_apply, hL.fderiv]
    simp [hLv, Dg]; ring
  have h2 : ContDiff ℝ 1 (fun z : V × V => S.kos z.1 z.2 z.2) := by
    rw [hk]
    exact (contDiff_const (c := (1 / 2 : ℝ))).smul (((hT1.clm_apply contDiff_snd).add
      (hT1.clm_apply contDiff_snd)).sub hT3)
  exact h1.clm_apply h2.contDiffAt

/-- The geodesic spray `F(x, v) = (v, −Γ_x(v,v))` on `V × V`. -/
noncomputable def geoField (z : V × V) : V × V := (z.2, -S.Γ z.1 z.2 z.2)

theorem lk_geoField_contDiffAt (hg : ContDiff ℝ 2 S.g) {z : V × V} (hz : z.1 ∈ S.M) :
    ContDiffAt ℝ 1 S.geoField z := by
  obtain ⟨x, u⟩ := z
  exact contDiffAt_snd.prodMk (S.lk_christoffel_contDiffAt hg hz u).neg

/-- The spray cut off in `x` by a bump `χ` around `p`: `C¹` on all of `V × V`. -/
noncomputable def cutField {p : V} (χ : ContDiffBump p) (z : V × V) : V × V := χ z.1 • S.geoField z

theorem lk_cutField_contDiff (hg : ContDiff ℝ 2 S.g) {p : V} (χ : ContDiffBump p)
    (hχ : closedBall p χ.rOut ⊆ S.M) : ContDiff ℝ 1 (S.cutField χ) := by
  rw [contDiff_iff_contDiffAt]; intro z
  by_cases hz : z.1 ∈ closedBall p χ.rOut
  · exact ((χ.contDiff.comp contDiff_fst).contDiffAt).smul (S.lk_geoField_contDiffAt hg (hχ hz))
  · have hO : IsOpen {y : V × V | y.1 ∉ closedBall p χ.rOut} :=
      (isClosed_closedBall.preimage continuous_fst).isOpen_compl
    refine (contDiffAt_const (c := (0 : V × V))).congr_of_eventuallyEq ?_
    filter_upwards [hO.mem_nhds hz] with y hy
    have hy' : χ.rOut ≤ dist y.1 p := by
      simp only [mem_closedBall, not_le] at hy; exact hy.le
    simp [cutField, χ.zero_of_le_dist hy']

theorem lk_cutField_eq {p : V} (χ : ContDiffBump p) {z : V × V} (hz : z.1 ∈ closedBall p χ.rIn) :
    S.cutField χ z = S.geoField z := by
  simp [cutField, χ.one_of_mem_closedBall hz]

theorem lk_cutField_zero {p : V} (χ : ContDiffBump p) : S.cutField χ (p, 0) = 0 := by
  simp [cutField, geoField, lk_christoffel_zero]

/-- Inside `ball p rIn`, the first component of `D(cut spray)` is the projection `(X, U) ↦ U`. -/
theorem lk_fst_fderiv_cutField (hg : ContDiff ℝ 2 S.g) {p : V} (χ : ContDiffBump p)
    (hχ : closedBall p χ.rOut ⊆ S.M) {z : V × V} (hz : z.1 ∈ ball p χ.rIn) (ξ : V × V) :
    (fderiv ℝ (S.cutField χ) z ξ).1 = ξ.2 := by
  have hd := ((S.lk_cutField_contDiff hg χ hχ).differentiable one_ne_zero z).hasFDerivAt
  have h1 := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp z hd
  have hO : IsOpen {y : V × V | y.1 ∈ ball p χ.rIn} := isOpen_ball.preimage continuous_fst
  have heq : (fun y => (S.cutField χ y).1) =ᶠ[𝓝 z] Prod.snd := by
    filter_upwards [hO.mem_nhds hz] with y hy
    rw [S.lk_cutField_eq χ (ball_subset_closedBall hy)]; rfl
  have h2 : HasFDerivAt (fun y => (S.cutField χ y).1) (ContinuousLinearMap.snd ℝ V V) z :=
    (hasFDerivAt_snd).congr_of_eventuallyEq heq
  have := congrArg (fun L => L ξ) (h1.unique h2)
  simpa using this


theorem lk_norm_zero_prod (w : V) : ‖((0 : V), w)‖ = ‖w‖ := by
  rw [Prod.norm_def]; simp

/-- **Lorentzian algebra.** At `x ∈ M`, a causal vector `w` orthogonal to a nonzero null vector `P`
is a multiple of `P`. -/
theorem lk_causal_perp_null {x : V} (hx : x ∈ S.M) {P w : V} (hPP : S.g x P P = 0) (hP : P ≠ 0)
    (hww : S.g x w w ≤ 0) (hPw : S.g x P w = 0) : ∃ k : ℝ, w = k • P := by
  have hPT : S.g x P (S.T x) ≠ 0 := fun h => by
    have := S.pos_on_perp x hx P h hP; linarith
  refine ⟨S.g x w (S.T x) / S.g x P (S.T x), ?_⟩
  set k := S.g x w (S.T x) / S.g x P (S.T x) with hk
  have hzT : S.g x (w - k • P) (S.T x) = 0 := by
    simp only [map_sub, map_smul, sub_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul, hk]
    field_simp; ring
  have hzz : S.g x (w - k • P) (w - k • P) = S.g x w w := by
    have hwP : S.g x w P = 0 := by rw [S.symm]; exact hPw
    simp only [map_sub, map_smul, sub_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul, hPP, hwP, hPw]
    ring
  by_contra hne
  have := S.pos_on_perp x hx (w - k • P) hzT (sub_ne_zero.2 hne)
  linarith

/-- One `C¹` future-timelike piece from `x` to `y` on `[0,1]` (copied from campaign 70). -/
def TStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t)

/-- Chronological relation `x ≪ y` (copied from campaign 70). -/
def Chr (x y : V) : Prop := Relation.TransGen S.TStep x y

/-! ## ① Local geodesics: the flow of the cut-off spray near the zero section -/

/-- Local geodesic-flow data at `p ∈ M`: a bump `χ` around `p` with support in `M`, and campaign
62's flow data for the cut-off spray at `(p, 0)`. -/
structure GeoFlow (p : V) where
  χ : ContDiffBump p
  sub : closedBall p χ.rOut ⊆ S.M
  D : FlowData (S.cutField χ) ((p, 0) : V × V)

/-- Geodesic-flow data exist at every `p ∈ M` (for `g ∈ C²`). -/
theorem lk_geoFlow_exists (hg : ContDiff ℝ 2 S.g) {p : V} (hp : p ∈ S.M) :
    Nonempty (S.GeoFlow p) := by
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.1 S.isOpen_M p hp
  let χ : ContDiffBump p := ⟨ε / 4, ε / 2, by positivity, by linarith⟩
  have hsub : closedBall p χ.rOut ⊆ S.M :=
    (closedBall_subset_ball (by show ε / 2 < ε; linarith)).trans hball
  exact ⟨⟨χ, hsub, (lk_flowData_exists (S.lk_cutField_contDiff hg χ hsub) (p, 0)).some⟩⟩

namespace GeoFlow

variable {S} {p : V} (G : S.GeoFlow p)

theorem lk_hf (hg : ContDiff ℝ 2 S.g) : ContDiff ℝ 1 (S.cutField G.χ) :=
  S.lk_cutField_contDiff hg G.χ G.sub

/-- The radius of initial data whose trajectories stay where `χ = 1`. -/
noncomputable def r₁ : ℝ := min G.D.r (G.χ.rIn / (2 * ((G.D.L : ℝ) + 1)))

theorem lk_r₁_pos : 0 < G.r₁ := lt_min G.D.r_pos (by have := G.χ.rIn_pos; positivity)

theorem lk_r₁_le : G.r₁ ≤ G.D.r := min_le_left _ _

theorem lk_mem_r {y : V × V} (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) :
    y ∈ closedBall ((p, 0) : V × V) G.D.r :=
  closedBall_subset_closedBall G.lk_r₁_le hy

theorem lk_ball_sub_M {x : V} (hx : x ∈ ball p G.χ.rIn) : x ∈ S.M :=
  G.sub (closedBall_subset_closedBall G.χ.rIn_lt_rOut.le (ball_subset_closedBall hx))

/-- Trajectories from `closedBall (p,0) r₁` stay over `ball p rIn`, where `χ = 1`. -/
theorem lk_traj_in (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    (G.D.α y t).1 ∈ ball p G.χ.rIn := by
  have h1 := G.D.lk_lip_center (G.lk_hf hg) (S.lk_cutField_zero G.χ) (G.lk_mem_r hy) ht
  have hy' : ‖y - (p, 0)‖ ≤ G.r₁ := by rwa [mem_closedBall, dist_eq_norm] at hy
  have hL : (0 : ℝ) ≤ G.D.L := G.D.L.2
  have hrin := G.χ.rIn_pos
  have hq : (G.D.L : ℝ) * G.r₁ < G.χ.rIn := by
    have h2 : G.r₁ ≤ G.χ.rIn / (2 * ((G.D.L : ℝ) + 1)) := min_le_right _ _
    have h3 : (G.D.L : ℝ) * (G.χ.rIn / (2 * ((G.D.L : ℝ) + 1))) < G.χ.rIn := by
      rw [mul_div_assoc', div_lt_iff₀ (by positivity)]; nlinarith
    calc _ ≤ (G.D.L : ℝ) * (G.χ.rIn / (2 * ((G.D.L : ℝ) + 1))) :=
          mul_le_mul_of_nonneg_left h2 hL
      _ < _ := h3
  rw [mem_ball, dist_eq_norm]
  calc ‖(G.D.α y t).1 - p‖ = ‖(G.D.α y t - (p, 0)).1‖ := rfl
    _ ≤ ‖G.D.α y t - (p, 0)‖ := norm_fst_le _
    _ ≤ G.D.L * ‖y - (p, 0)‖ := h1
    _ ≤ G.D.L * G.r₁ := mul_le_mul_of_nonneg_left hy' hL
    _ < _ := hq

/-- **Local geodesics.** For initial data in `closedBall (p,0) r₁` the flow solves the geodesic
spray `(x, u)′ = (u, −Γ_x(u,u))` on `[-τ, τ]`. -/
theorem lk_geodesic (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    HasDerivWithinAt (G.D.α y) (S.geoField (G.D.α y t)) (Icc (-G.D.τ) G.D.τ) t := by
  rw [← S.lk_cutField_eq G.χ (ball_subset_closedBall (G.lk_traj_in hg hy ht))]
  exact G.D.deriv y (G.lk_mem_r hy) t ht

theorem lk_geodesic_fst (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    HasDerivWithinAt (fun s => (G.D.α y s).1) (G.D.α y t).2 (Icc (-G.D.τ) G.D.τ) t := by
  have := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp_hasDerivWithinAt t
    (G.lk_geodesic hg hy ht)
  exact this.congr_deriv (by simp [geoField])

theorem lk_geodesic_snd (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    HasDerivWithinAt (fun s => (G.D.α y s).2)
      (-S.Γ (G.D.α y t).1 (G.D.α y t).2 (G.D.α y t).2) (Icc (-G.D.τ) G.D.τ) t := by
  have := (ContinuousLinearMap.snd ℝ V V).hasFDerivAt.comp_hasDerivWithinAt t
    (G.lk_geodesic hg hy ht)
  exact this.congr_deriv (by simp [geoField])

/-- **Scaling of geodesics.** `φ_t(p, λa) = (π₁ φ_{λt}(p, a), λ π₂ φ_{λt}(p, a))` for
`λ ∈ [0, 1]`: the geodesic with initial velocity `λa` is the one with velocity `a`, run at speed
`λ`. Proved by uniqueness (`lk_unique`). -/
theorem lk_scaling (hg : ContDiff ℝ 2 S.g) {a : V}
    (ha : ((p, a) : V × V) ∈ closedBall ((p, 0) : V × V) G.r₁) {l : ℝ} (hl : l ∈ Icc (0 : ℝ) 1)
    {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    G.D.α (p, l • a) t = ((G.D.α (p, a) (l * t)).1, l • (G.D.α (p, a) (l * t)).2) := by
  have hlt : ∀ s ∈ Icc (-G.D.τ) G.D.τ, l * s ∈ Icc (-G.D.τ) G.D.τ := fun s hs => by
    constructor <;> nlinarith [hs.1, hs.2, hl.1, hl.2, G.D.τ_pos]
  have hx : ((p, l • a) : V × V) ∈ closedBall ((p, 0) : V × V) G.D.r := by
    have ha' := G.lk_mem_r ha
    rw [mem_closedBall, dist_eq_norm] at ha' ⊢
    have e1 : ((p, l • a) : V × V) - (p, 0) = ((0 : V), l • a) := by simp
    have e2 : ((p, a) : V × V) - (p, 0) = ((0 : V), a) := by simp
    rw [e1, lk_norm_zero_prod, norm_smul, Real.norm_eq_abs, abs_of_nonneg hl.1]
    rw [e2, lk_norm_zero_prod] at ha'
    nlinarith [norm_nonneg a, hl.2]
  let Ll : V × V →L[ℝ] V × V :=
    (ContinuousLinearMap.fst ℝ V V).prod (l • ContinuousLinearMap.snd ℝ V V)
  have hβL : (fun s => ((G.D.α (p, a) (l * s)).1, l • (G.D.α (p, a) (l * s)).2)) =
      Ll ∘ G.D.α (p, a) ∘ fun s => l * s := by
    funext s; simp [Ll]
  refine (G.D.lk_unique (G.lk_hf hg) hx
    (β := fun s => ((G.D.α (p, a) (l * s)).1, l • (G.D.α (p, a) (l * s)).2)) ?_ ?_ ?_ t ht).symm
  · simp [G.D.init _ (G.lk_mem_r ha)]
  · intro s hs
    have h1 : HasDerivWithinAt (fun s => l * s) l (Icc (-G.D.τ) G.D.τ) s := by
      simpa using ((hasDerivAt_id s).const_mul l).hasDerivWithinAt
    have h2 := (G.lk_geodesic hg ha (hlt s hs)).scomp s h1 (fun s hs => hlt s hs)
    have h3 := Ll.hasFDerivAt.comp_hasDerivWithinAt s h2
    rw [← hβL] at h3
    convert h3 using 1
    have hin := G.lk_traj_in hg ha (hlt s hs)
    rw [S.lk_cutField_eq G.χ
      (z := ((G.D.α (p, a) (l * s)).1, l • (G.D.α (p, a) (l * s)).2)) (ball_subset_closedBall hin)]
    simp only [geoField, Ll, S.lk_christoffel_quad, ContinuousLinearMap.prod_apply,
      ContinuousLinearMap.coe_fst', ContinuousLinearMap.coe_snd', Prod.smul_mk,
      FunLike.coe_smul, Pi.smul_apply, smul_neg, smul_smul, pow_two]
  · intro s hs
    have := G.D.mem (p, a) (G.lk_mem_r ha) (l * s) (hlt s hs)
    rw [mem_closedBall, dist_eq_norm] at this ⊢
    refine le_trans ?_ this
    rw [Prod.norm_def, Prod.norm_def]
    refine max_le_max le_rfl ?_
    simp only [Prod.snd_sub, sub_zero, norm_smul, Real.norm_eq_abs, abs_of_nonneg hl.1]
    nlinarith [norm_nonneg (G.D.α (p, a) (l * s)).2, hl.2]

/-! ### The exponential map -/

/-- The time at which `exp` is read off. -/
noncomputable def s₀ : ℝ := G.D.τ / 2
/-- The velocity rescaling, `c s₀ = 1`. -/
noncomputable def c : ℝ := 2 / G.D.τ

theorem lk_c_s₀ : G.c * G.s₀ = 1 := by
  unfold c s₀; field_simp [G.D.τ_pos.ne']

theorem lk_s₀_pos : 0 < G.s₀ := by unfold s₀; linarith [G.D.τ_pos]
theorem lk_c_pos : 0 < G.c := by unfold c; have := G.D.τ_pos; positivity

theorem lk_s₀_mem : G.s₀ ∈ Icc (-G.D.τ) G.D.τ := by
  unfold s₀; constructor <;> linarith [G.D.τ_pos]

/-- `exp_p(v) = π₁ φ_{s₀}(p, c v)`; by `lk_expp_smul` this is `π₁ φ₁(p, v)` of the geodesic
spray, with the time rescaled to stay inside `[-τ, τ]`. -/
noncomputable def expp (v : V) : V := (G.D.α (p, G.c • v) G.s₀).1

/-- The velocity at `t = 1` of the radial geodesic `t ↦ exp_p(t v)`. -/
noncomputable def rad (v : V) : V := G.s₀ • (G.D.α (p, G.c • v) G.s₀).2

/-- The radius of the normal-coordinate domain `ball 0 ρ`. -/
noncomputable def ρ : ℝ := G.r₁ * G.s₀

theorem lk_ρ_pos : 0 < G.ρ := mul_pos G.lk_r₁_pos G.lk_s₀_pos

theorem lk_dom {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    ((p, G.c • v) : V × V) ∈ ball ((p, 0) : V × V) G.r₁ := by
  rw [mem_ball, dist_eq_norm]
  have e1 : ((p, G.c • v) : V × V) - (p, 0) = ((0 : V), G.c • v) := by simp
  rw [e1, lk_norm_zero_prod, norm_smul, Real.norm_eq_abs, abs_of_pos G.lk_c_pos]
  have h := mem_ball_zero_iff.1 hv
  have hcs := G.lk_c_s₀
  unfold ρ at h
  calc G.c * ‖v‖ < G.c * (G.r₁ * G.s₀) := mul_lt_mul_of_pos_left h G.lk_c_pos
    _ = G.r₁ * (G.c * G.s₀) := by ring
    _ = G.r₁ := by rw [hcs, mul_one]

theorem lk_dom_closed {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    ((p, G.c • v) : V × V) ∈ closedBall ((p, 0) : V × V) G.r₁ :=
  ball_subset_closedBall (G.lk_dom hv)

/-- The derivative `D exp_p(v) w = π₁ J_{s₀}(p, c v) (0, c w)` (variational equation). -/
noncomputable def Dexp (v : V) : V →L[ℝ] V :=
  (ContinuousLinearMap.fst ℝ V V).comp ((G.D.J (p, G.c • v) G.s₀).comp
    ((0 : V →L[ℝ] V).prod (G.c • ContinuousLinearMap.id ℝ V)))

theorem lk_Dexp_apply (v w : V) : G.Dexp v w = (G.D.J (p, G.c • v) G.s₀ (0, G.c • w)).1 := by
  simp [Dexp]

theorem lk_expp_hasFDerivAt (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    HasFDerivAt G.expp (G.Dexp v) v := by
  have h1 : HasFDerivAt (fun w : V => ((p, G.c • w) : V × V))
      ((0 : V →L[ℝ] V).prod (G.c • ContinuousLinearMap.id ℝ V)) v :=
    (hasFDerivAt_const p v).prodMk ((ContinuousLinearMap.id ℝ V).hasFDerivAt.const_smul G.c)
  have h2 := G.D.lk_flow_hasFDerivAt (G.lk_hf hg) (p, G.c • v)
    (ball_subset_ball G.lk_r₁_le (G.lk_dom hv)) G.s₀ G.lk_s₀_mem
  have h3 := h2.comp v h1
  have h4 := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp v h3
  exact h4

theorem lk_expp_contDiffAt (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    ContDiffAt ℝ 1 G.expp v := by
  have h1 : ContDiffAt ℝ 1 (fun y : V × V => G.D.α y G.s₀) (p, G.c • v) :=
    (G.D.lk_flow_contDiffOn (G.lk_hf hg) G.s₀ G.lk_s₀_mem).contDiffAt
      (isOpen_ball.mem_nhds (ball_subset_ball G.lk_r₁_le (G.lk_dom hv)))
  have h2 : ContDiffAt ℝ 1 (fun w : V => ((p, G.c • w) : V × V)) v :=
    contDiffAt_const.prodMk (contDiffAt_id.const_smul G.c)
  have h3 := h1.comp v h2
  have h4 := contDiffAt_fst.comp v h3
  exact h4

theorem lk_expp_zero (hg : ContDiff ℝ 2 S.g) : G.expp 0 = p := by
  simp [expp, G.D.lk_fixed (G.lk_hf hg) (S.lk_cutField_zero G.χ) G.s₀ G.lk_s₀_mem]

/-- **Radial geodesics.** `exp_p(λ v) = π₁ φ_{λ s₀}(p, c v)` for `λ ∈ [0, 1]`. -/
theorem lk_expp_smul (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) {l : ℝ}
    (hl : l ∈ Icc (0 : ℝ) 1) : G.expp (l • v) = (G.D.α (p, G.c • v) (l * G.s₀)).1 := by
  rw [expp, smul_comm G.c l v, G.lk_scaling hg (G.lk_dom_closed hv) hl G.lk_s₀_mem]

theorem lk_mul_s₀_mem {l : ℝ} (hl : l ∈ Icc (0 : ℝ) 1) : l * G.s₀ ∈ Icc (-G.D.τ) G.D.τ := by
  have := G.lk_s₀_pos
  unfold s₀ at *
  constructor <;> nlinarith [hl.1, hl.2, G.D.τ_pos]

theorem lk_expp_radial_deriv (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ)
    {l : ℝ} (hl : l ∈ Icc (0 : ℝ) 1) :
    HasDerivWithinAt (fun m : ℝ => G.expp (m • v))
      (G.s₀ • (G.D.α (p, G.c • v) (l * G.s₀)).2) (Icc 0 1) l := by
  have hmaps : MapsTo (fun m : ℝ => m * G.s₀) (Icc (0 : ℝ) 1) (Icc (-G.D.τ) G.D.τ) :=
    fun m hm => G.lk_mul_s₀_mem hm
  have h1 : HasDerivWithinAt (fun m : ℝ => m * G.s₀) G.s₀ (Icc 0 1) l := by
    simpa using ((hasDerivAt_id l).mul_const G.s₀).hasDerivWithinAt
  have h2 := (G.lk_geodesic hg (G.lk_dom_closed hv) (hmaps hl)).scomp l h1 hmaps
  have h3 := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp_hasDerivWithinAt l h2
  refine (h3.congr (fun m hm => G.lk_expp_smul hg hv hm) (G.lk_expp_smul hg hv hl)).congr_deriv ?_
  simp [geoField]

/-- `D exp_p(λ v) v` is the velocity of the radial geodesic at `λ`. -/
theorem lk_Dexp_radial_at (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) {l : ℝ}
    (hl : l ∈ Icc (0 : ℝ) 1) :
    G.Dexp (l • v) v = G.s₀ • (G.D.α (p, G.c • v) (l * G.s₀)).2 := by
  have hlv : l • v ∈ ball (0 : V) G.ρ := by
    rw [mem_ball_zero_iff, norm_smul, Real.norm_eq_abs, abs_of_nonneg hl.1]
    have := mem_ball_zero_iff.1 hv
    nlinarith [norm_nonneg v, hl.2]
  have h1 : HasDerivAt (fun m : ℝ => G.expp (m • v)) (G.Dexp (l • v) v) l := by
    have hline : HasDerivAt (fun m : ℝ => m • v) v l := by
      simpa using (hasDerivAt_id l).smul_const v
    exact (G.lk_expp_hasFDerivAt hg hlv).comp_hasDerivAt l hline
  exact (uniqueDiffOn_Icc_zero_one l hl).eq_deriv _ h1.hasDerivWithinAt
    (G.lk_expp_radial_deriv hg hv hl)

/-- `D exp_p(v) v = rad v`: the radial derivative is the geodesic velocity. -/
theorem lk_Dexp_radial (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    G.Dexp v v = G.rad v := by
  have := G.lk_Dexp_radial_at hg hv (l := 1) ⟨zero_le_one, le_rfl⟩
  rwa [one_smul, one_mul] at this

theorem lk_Dexp_zero_apply (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    G.Dexp 0 v = v := by
  have := G.lk_Dexp_radial_at hg hv (l := 0) ⟨le_rfl, zero_le_one⟩
  rw [zero_smul, zero_mul, G.D.init _ (G.lk_mem_r (G.lk_dom_closed hv)), smul_smul,
    mul_comm, G.lk_c_s₀, one_smul] at this
  exact this

/-- **`D exp_p(0) = id`.** -/
theorem lk_Dexp_zero (hg : ContDiff ℝ 2 S.g) : G.Dexp 0 = ContinuousLinearMap.id ℝ V := by
  ext v
  set ε : ℝ := G.ρ / (2 * (‖v‖ + 1)) with hε
  have hε0 : 0 < ε := by have := G.lk_ρ_pos; positivity
  have hεv : ε • v ∈ ball (0 : V) G.ρ := by
    rw [mem_ball_zero_iff, norm_smul, Real.norm_eq_abs, abs_of_pos hε0, hε]
    have := G.lk_ρ_pos
    rw [div_mul_eq_mul_div, div_lt_iff₀ (by positivity)]
    nlinarith [norm_nonneg v]
  have := G.lk_Dexp_zero_apply hg hεv
  rw [map_smul] at this
  simpa using smul_right_injective V hε0.ne' this

theorem lk_expp_fderiv_zero (hg : ContDiff ℝ 2 S.g) :
    HasFDerivAt G.expp (ContinuousLinearMap.id ℝ V) 0 := by
  rw [← G.lk_Dexp_zero hg]
  exact G.lk_expp_hasFDerivAt hg (mem_ball_self G.lk_ρ_pos)

/-- **`exp_p` is a local diffeomorphism at `0`** (inverse function theorem, as in campaign 62's flow
box): a `C¹` open partial homeomorphism `Φ` with `Φ = exp_p` on its source `∋ 0`, `Φ 0 = p`, and
a `C¹` inverse near `p`. -/
theorem lk_expp_localDiffeo (hg : ContDiff ℝ 2 S.g) :
    ∃ Φ : OpenPartialHomeomorph V V, (0 : V) ∈ Φ.source ∧ Φ.source ⊆ ball (0 : V) G.ρ ∧
      (∀ v ∈ Φ.source, Φ v = G.expp v) ∧ Φ 0 = p ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      ∀ᶠ x in 𝓝 p, ContDiffAt ℝ 1 Φ.symm x := by
  have hn : (1 : WithTop ℕ∞) ≠ 0 := by norm_num
  have h0 : (0 : V) ∈ ball (0 : V) G.ρ := mem_ball_self G.lk_ρ_pos
  have hd : HasFDerivAt G.expp ((ContinuousLinearEquiv.refl ℝ V : V ≃L[ℝ] V) : V →L[ℝ] V) 0 := by
    rw [ContinuousLinearEquiv.coe_refl]; exact G.lk_expp_fderiv_zero hg
  have hc := G.lk_expp_contDiffAt hg h0
  refine ⟨(hc.toOpenPartialHomeomorph G.expp hd hn).restrOpen (ball 0 G.ρ) isOpen_ball,
    ⟨hc.mem_toOpenPartialHomeomorph_source hd hn, h0⟩, inter_subset_right, fun v _ => rfl,
    G.lk_expp_zero hg, fun v hv => (G.lk_expp_contDiffAt hg hv.2).contDiffWithinAt, ?_⟩
  have := (hc.to_localInverse hd hn).eventually (by simp)
  rw [G.lk_expp_zero hg] at this
  exact this

/-! ## ② The Gauss lemma, through the variational (Jacobi) equation -/

/-- **Energy conservation** along local geodesics: `g_x(u, u)` is constant. -/
theorem lk_energy_cons (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    S.g (G.D.α y t).1 (G.D.α y t).2 (G.D.α y t).2 = S.g y.1 y.2 y.2 := by
  have hd : ∀ s ∈ Icc (-G.D.τ) G.D.τ, HasDerivWithinAt
      (fun s => S.g (G.D.α y s).1 (G.D.α y s).2 (G.D.α y s).2) 0 (Icc (-G.D.τ) G.D.τ) s := by
    intro s hs
    have h := S.lk_hasDerivWithinAt_g ((hg.differentiable (by norm_num)) _)
      (G.lk_geodesic_fst hg hy hs) (G.lk_geodesic_snd hg hy hs) (G.lk_geodesic_snd hg hy hs)
    convert h using 1
    have hx := G.lk_ball_sub_M (G.lk_traj_in hg hy hs)
    set x := (G.D.α y s).1
    set u := (G.D.α y s).2
    rw [map_neg, map_neg, neg_apply, S.symm x u (S.Γ x u u),
      S.lk_christoffel_koszul hx]
    ring
  have := G.D.lk_affine_of_deriv hd t ht
  rw [this, G.D.init y (G.lk_mem_r hy)]; ring

/-- The energy identity differentiated in the initial data:
`Dg_x(X)(u,u) + 2 g_x(u, U) = Dg_y(ξ₁)(y₂,y₂) + 2 g_y(y₂, ξ₂)` for `(X, U) = J ξ`. -/
theorem lk_energy_variation (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ ball ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) (ξ : V × V) :
    S.Dg (G.D.α y t).1 (G.D.J y t ξ).1 (G.D.α y t).2 (G.D.α y t).2 +
        2 * S.g (G.D.α y t).1 (G.D.α y t).2 (G.D.J y t ξ).2 =
      S.Dg y.1 ξ.1 y.2 y.2 + 2 * S.g y.1 y.2 ξ.2 := by
  obtain ⟨L₁, hL₁, hv₁⟩ := S.lk_energy_hasFDerivAt hg (G.D.α y t)
  obtain ⟨L₂, hL₂, hv₂⟩ := S.lk_energy_hasFDerivAt hg y
  have hJ := G.D.lk_flow_hasFDerivAt (G.lk_hf hg) y (ball_subset_ball G.lk_r₁_le hy) t ht
  have h1 := hL₁.comp y hJ
  have heq : ((fun z : V × V => S.g z.1 z.2 z.2) ∘ fun y' => G.D.α y' t) =ᶠ[𝓝 y]
      (fun y' : V × V => S.g y'.1 y'.2 y'.2) := by
    filter_upwards [isOpen_ball.mem_nhds hy] with y' hy'
    exact G.lk_energy_cons hg (ball_subset_closedBall hy') ht
  have h2 := hL₂.congr_of_eventuallyEq heq
  have := congrArg (fun L => L ξ) (h1.unique h2)
  simp only [ContinuousLinearMap.comp_apply, hv₁, hv₂] at this
  exact this

/-- **The Gauss lemma, flow form.** Along the geodesic `(x, u)(t) = φ_t(p, a)` and the Jacobi
field `(X, U)(t) = J_t(p, a)(0, b)`: `g_{x(t)}(u(t), X(t)) = t · g_p(a, b)`. -/
theorem lk_gauss_flow (hg : ContDiff ℝ 2 S.g) {a : V}
    (ha : ((p, a) : V × V) ∈ ball ((p, 0) : V × V) G.r₁) (b : V) {t : ℝ}
    (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    S.g (G.D.α (p, a) t).1 (G.D.α (p, a) t).2 (G.D.J (p, a) t (0, b)).1 = t * S.g p a b := by
  have hyc := ball_subset_closedBall ha
  have hJ := G.D.lk_J_spec (G.lk_hf hg) (p, a) (G.lk_mem_r hyc)
  have hd : ∀ s ∈ Icc (-G.D.τ) G.D.τ, HasDerivWithinAt (fun s =>
      S.g (G.D.α (p, a) s).1 (G.D.α (p, a) s).2 (G.D.J (p, a) s (0, b)).1) (S.g p a b)
      (Icc (-G.D.τ) G.D.τ) s := by
    intro s hs
    have hJs : HasDerivWithinAt (fun s => G.D.J (p, a) s (0, b))
        (fderiv ℝ (S.cutField G.χ) (G.D.α (p, a) s) (G.D.J (p, a) s (0, b)))
        (Icc (-G.D.τ) G.D.τ) s := by
      have := (hJ.2 s hs).clm_apply (hasDerivWithinAt_const s _ ((0 : V), b))
      simpa using this
    have hX : HasDerivWithinAt (fun s => (G.D.J (p, a) s (0, b)).1)
        (G.D.J (p, a) s (0, b)).2 (Icc (-G.D.τ) G.D.τ) s := by
      have := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp_hasDerivWithinAt s hJs
      have e := S.lk_fst_fderiv_cutField hg G.χ G.sub (G.lk_traj_in hg hyc hs)
        (G.D.J (p, a) s (0, b))
      exact this.congr_deriv (by simpa using e)
    have h := S.lk_hasDerivWithinAt_g ((hg.differentiable (by norm_num)) _)
      (G.lk_geodesic_fst hg hyc hs) (G.lk_geodesic_snd hg hyc hs) hX
    convert h using 1
    have hx := G.lk_ball_sub_M (G.lk_traj_in hg hyc hs)
    have hv := G.lk_energy_variation hg ha hs ((0 : V), b)
    simp only [S.lk_Dg_zero, zero_add] at hv
    rw [map_neg, neg_apply, S.lk_christoffel_koszul hx]
    linarith
  have := G.D.lk_affine_of_deriv hd t ht
  rw [this, hJ.1, G.D.init _ (G.lk_mem_r hyc)]
  simp

/-- **The Gauss lemma** (registered form): for `v` in the normal domain and every `w`,
`g_{exp_p v}(D exp_p(v) v, D exp_p(v) w) = g_p(v, w)`. -/
theorem lk_gauss (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) (w : V) :
    S.g (G.expp v) (G.Dexp v v) (G.Dexp v w) = S.g p v w := by
  rw [G.lk_Dexp_radial hg hv, rad, lk_Dexp_apply, expp]
  have := G.lk_gauss_flow hg (G.lk_dom hv) (G.c • w) G.lk_s₀_mem
  simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at this ⊢
  rw [this]
  have hcs := G.lk_c_s₀
  linear_combination (G.c * G.s₀ + 1) * S.g p v w * hcs

/-- The radial velocity has the energy of `v`: `g_{exp v}(rad v, rad v) = g_p(v, v)`. -/
theorem lk_rad_energy (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    S.g (G.expp v) (G.rad v) (G.rad v) = S.g p v v := by
  have := G.lk_energy_cons hg (G.lk_dom_closed hv) G.lk_s₀_mem
  rw [rad, expp]
  simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at this ⊢
  rw [this]
  have hcs := G.lk_c_s₀
  linear_combination (G.c * G.s₀ + 1) * S.g p v v * hcs


/-! ## ③ Local maximality: the normal chart, `Q = g_p(exp⁻¹, exp⁻¹)`, the position field -/

/-- A normal chart at `p`: `exp_p` restricted to a neighbourhood of `0` on which it is a `C¹`
open partial homeomorphism (from `lk_expp_localDiffeo`). -/
structure NormalChart where
  Φ : OpenPartialHomeomorph V V
  zero_mem : (0 : V) ∈ Φ.source
  source_sub : Φ.source ⊆ ball (0 : V) G.ρ
  eq : ∀ v ∈ Φ.source, Φ v = G.expp v
  map_zero : Φ 0 = p
  symm_smooth : ∀ᶠ x in 𝓝 p, ContDiffAt ℝ 1 Φ.symm x

theorem lk_normalChart_exists (hg : ContDiff ℝ 2 S.g) : Nonempty G.NormalChart := by
  obtain ⟨Φ, h0, hs, he, hm, _, hsy⟩ := G.lk_expp_localDiffeo hg
  exact ⟨⟨Φ, h0, hs, he, hm, hsy⟩⟩

namespace NormalChart

variable {G} (N : G.NormalChart)

/-- `Q(x) = g_p(exp_p⁻¹ x, exp_p⁻¹ x)`. -/
noncomputable def Q (x : V) : ℝ := S.g p (N.Φ.symm x) (N.Φ.symm x)

/-- The position field `P(x) = (D exp_p)(v) v` at `x = exp_p v`: the velocity at time `1` of the
radial geodesic from `p` to `x`. -/
noncomputable def P (x : V) : V := G.rad (N.Φ.symm x)

/-- Points of the chart's target where the inverse is `C¹`; a neighbourhood of `p`. -/
def good : Set V := {x | x ∈ N.Φ.target ∧ ContDiffAt ℝ 1 N.Φ.symm x}

theorem lk_good_nhds : N.good ∈ 𝓝 p := by
  have hp : p ∈ N.Φ.target := by
    have := N.Φ.map_source N.zero_mem; rwa [N.map_zero] at this
  exact (N.Φ.open_target.eventually_mem hp).and N.symm_smooth

theorem lk_good_src {x : V} (hx : x ∈ N.good) : N.Φ.symm x ∈ N.Φ.source :=
  N.Φ.map_target hx.1

theorem lk_good_dom {x : V} (hx : x ∈ N.good) : N.Φ.symm x ∈ ball (0 : V) G.ρ :=
  N.source_sub (N.lk_good_src hx)

theorem lk_good_expp {x : V} (hx : x ∈ N.good) : G.expp (N.Φ.symm x) = x := by
  rw [← N.eq _ (N.lk_good_src hx)]; exact N.Φ.right_inv hx.1

theorem lk_good_mem_M (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) : x ∈ S.M := by
  rw [← N.lk_good_expp hx]
  exact G.lk_ball_sub_M (G.lk_traj_in hg (G.lk_dom_closed (N.lk_good_dom hx)) G.lk_s₀_mem)

/-- **The gradient of `Q` is twice the position field:** `DQ_x(ξ) = 2 g_x(P(x), ξ)` (Gauss lemma). -/
theorem lk_grad_Q (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) :
    HasFDerivAt N.Q ((2 : ℝ) • S.g x (N.P x)) x := by
  have hv := N.lk_good_dom hx
  have hxe := N.lk_good_expp hx
  have hL : HasFDerivAt N.Φ.symm (fderiv ℝ N.Φ.symm x) x :=
    (hx.2.differentiableAt one_ne_zero).hasFDerivAt
  have hcomp := (G.lk_expp_hasFDerivAt hg hv).comp x hL
  have hid : G.expp ∘ N.Φ.symm =ᶠ[𝓝 x] id := by
    filter_upwards [N.Φ.open_target.mem_nhds hx.1] with y hy
    show G.expp (N.Φ.symm y) = y
    rw [← N.eq _ (N.Φ.map_target hy)]; exact N.Φ.right_inv hy
  have hDL : (G.Dexp (N.Φ.symm x)).comp (fderiv ℝ N.Φ.symm x) = ContinuousLinearMap.id ℝ V :=
    hcomp.unique ((hasFDerivAt_id x).congr_of_eventuallyEq hid)
  obtain ⟨E', hE', hEv⟩ := S.lk_energy_hasFDerivAt hg (p, N.Φ.symm x)
  have hq : HasFDerivAt (fun w : V => ((p, w) : V × V))
      ((0 : V →L[ℝ] V).prod (ContinuousLinearMap.id ℝ V)) (N.Φ.symm x) :=
    (hasFDerivAt_const p _).prodMk (hasFDerivAt_id _)
  have h1 := hE'.comp (N.Φ.symm x) hq
  have hQ := h1.comp x hL
  refine hQ.congr_fderiv ?_
  ext ξ
  have hξ := congrArg (fun T => T ξ) hDL
  simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.id_apply] at hξ
  simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.prod_apply,
    zero_apply, ContinuousLinearMap.id_apply, hEv, S.lk_Dg_zero, zero_add,
    FunLike.coe_smul, Pi.smul_apply, smul_eq_mul, P]
  rw [← G.lk_gauss hg hv, G.lk_Dexp_radial hg hv, hxe, hξ]

/-- `g_x(P, P) = Q(x)`: the position field has the energy of `exp⁻¹ x`. -/
theorem lk_P_energy (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) :
    S.g x (N.P x) (N.P x) = N.Q x := by
  have := G.lk_rad_energy hg (N.lk_good_dom hx)
  rw [N.lk_good_expp hx] at this
  exact this

/-- `P(x) ≠ 0` for `x ≠ p` (Gauss lemma and nondegeneracy at `p`). -/
theorem lk_P_ne_zero (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) (hxp : x ≠ p) :
    N.P x ≠ 0 := by
  intro h0
  have hv := N.lk_good_dom hx
  have hpM : p ∈ S.M := G.lk_ball_sub_M (mem_ball_self G.χ.rIn_pos)
  have hz : N.Φ.symm x = 0 := S.lk_nondegenerate hpM fun w => by
    rw [← G.lk_gauss hg hv, G.lk_Dexp_radial hg hv]
    have : G.rad (N.Φ.symm x) = 0 := h0
    rw [this]; simp
  apply hxp
  rw [← N.Φ.right_inv hx.1, hz, N.map_zero]

/-- `D exp_p(v) ∘ D(exp_p⁻¹)(x) = id` at good points, `v = exp_p⁻¹ x`. -/
theorem lk_Dexp_comp_symm (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) :
    (G.Dexp (N.Φ.symm x)).comp (fderiv ℝ N.Φ.symm x) = ContinuousLinearMap.id ℝ V := by
  have hL : HasFDerivAt N.Φ.symm (fderiv ℝ N.Φ.symm x) x :=
    (hx.2.differentiableAt one_ne_zero).hasFDerivAt
  have hcomp := (G.lk_expp_hasFDerivAt hg (N.lk_good_dom hx)).comp x hL
  have hid : G.expp ∘ N.Φ.symm =ᶠ[𝓝 x] id := by
    filter_upwards [N.Φ.open_target.mem_nhds hx.1] with y hy
    show G.expp (N.Φ.symm y) = y
    rw [← N.eq _ (N.Φ.map_target hy)]; exact N.Φ.right_inv hy
  exact hcomp.unique ((hasFDerivAt_id x).congr_of_eventuallyEq hid)

/-- **In normal coordinates the position field is the Euler field:** `D(exp_p⁻¹)(x) P(x) = exp_p⁻¹ x`.
So the radial geodesics from `p` are the integral curves of `P`. -/
theorem lk_P_euler (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) :
    fderiv ℝ N.Φ.symm x (N.P x) = N.Φ.symm x := by
  have hv := N.lk_good_dom hx
  have hDL := N.lk_Dexp_comp_symm hg hx
  have hDL' : ∀ y, G.Dexp (N.Φ.symm x) (fderiv ℝ N.Φ.symm x y) = y := fun y => by
    have := congrArg (fun T => T y) hDL; simpa using this
  have hsurj : Function.Surjective (G.Dexp (N.Φ.symm x)) := fun y => ⟨_, hDL' y⟩
  have hinj : Function.Injective (G.Dexp (N.Φ.symm x)) := by
    have := (LinearMap.injective_iff_surjective
      (f := ((G.Dexp (N.Φ.symm x) : V →L[ℝ] V) : V →ₗ[ℝ] V))).2 hsurj
    exact this
  apply hinj
  rw [hDL', P, G.lk_Dexp_radial hg hv]

/-- **Local maximality, pointwise.** If a curve stays in the null conoid `{Q = 0}` near `t₀`, is
differentiable at `t₀` with causal velocity, and `γ t₀ ≠ p`, then `γ′(t₀) ∥ P(γ t₀)`, and `P` is a
nonzero null vector there. -/
theorem lk_null_tangent (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {t₀ : ℝ} {γ' : V}
    (hγ : HasDerivAt γ γ' t₀) (hQ : ∀ᶠ s in 𝓝 t₀, N.Q (γ s) = 0) (hgood : γ t₀ ∈ N.good)
    (hne : γ t₀ ≠ p) (hc : S.g (γ t₀) γ' γ' ≤ 0) :
    (∃ k : ℝ, γ' = k • N.P (γ t₀)) ∧ S.g (γ t₀) (N.P (γ t₀)) (N.P (γ t₀)) = 0 ∧
      N.P (γ t₀) ≠ 0 := by
  have hD := (N.lk_grad_Q hg hgood).comp_hasDerivAt t₀ hγ
  have h0 : HasDerivAt (N.Q ∘ γ) 0 t₀ := (hasDerivAt_const t₀ (0 : ℝ)).congr_of_eventuallyEq hQ
  have hPw : S.g (γ t₀) (N.P (γ t₀)) γ' = 0 := by
    have := hD.unique h0
    simp only [FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at this
    linarith
  have hPP : S.g (γ t₀) (N.P (γ t₀)) (N.P (γ t₀)) = 0 := by
    rw [N.lk_P_energy hg hgood]; exact hQ.self_of_nhds
  have hP0 := N.lk_P_ne_zero hg hgood hne
  exact ⟨S.lk_causal_perp_null (N.lk_good_mem_M hg hgood) hPP hP0 hc hPw, hPP, hP0⟩

/-- **Local maximality, Lipschitz form.** A Lipschitz curve on `[0,1]` that stays in `{Q = 0}`
inside the chart, avoids `p` on `(0,1)`, and has causal velocity a.e., has velocity `∥ P` a.e. -/
theorem lk_ae_null_tangent (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0}
    (hlip : LipschitzOnWith K γ (Icc 0 1)) (hQ : ∀ s ∈ Icc (0 : ℝ) 1, N.Q (γ s) = 0)
    (hgood : ∀ s ∈ Ioo (0 : ℝ) 1, γ s ∈ N.good ∧ γ s ≠ p)
    (hc : ∀ᵐ t ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ), t ∈ Ioo (0 : ℝ) 1 →
      DifferentiableAt ℝ γ t → S.g (γ t) (deriv γ t) (deriv γ t) ≤ 0) :
    ∀ᵐ t ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ), t ∈ Ioo (0 : ℝ) 1 →
      ∃ k : ℝ, deriv γ t = k • N.P (γ t) := by
  filter_upwards [hlip.ae_differentiableWithinAt_of_mem (μ := MeasureTheory.volume), hc]
    with t ht1 ht2 htI
  have hd : DifferentiableAt ℝ γ t :=
    (ht1 (Ioo_subset_Icc_self htI)).differentiableAt (Icc_mem_nhds htI.1 htI.2)
  have hQ' : ∀ᶠ s in 𝓝 t, N.Q (γ s) = 0 := by
    filter_upwards [Ioo_mem_nhds htI.1 htI.2] with s hs
    exact hQ s (Ioo_subset_Icc_self hs)
  exact (N.lk_null_tangent hg hd.hasDerivAt hQ' (hgood t htI).1 (hgood t htI).2
    (ht2 htI hd)).1

end NormalChart

/-! ### The timelike side: `exp_p` of a future-timelike vector is in `I⁺(p)` -/

/-- **Timelike radial geodesics give `≪`.** If `v` is future-timelike at `p` and `‖v‖ < ρ/3`, then
`p ≪ exp_p v`: the radial geodesic `t ↦ exp_p(t v)`, reparametrised outside `[0,1]` by a bump so as
to be globally `C¹`, is one future-timelike step (energy conservation for `g(γ′,γ′) < 0`, the
intermediate value theorem for the time orientation). -/
theorem lk_chr_of_timelike (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) (G.ρ / 3))
    (hvt : S.FutTimelike p v) : S.Chr p (G.expp v) := by
  have hρ := G.lk_ρ_pos
  have hv' : v ∈ ball (0 : V) G.ρ := ball_subset_ball (by linarith) hv
  have hvn := mem_ball_zero_iff.1 hv
  -- the reparametrisation `ψ`, the identity near `[0,1]` and bounded by `3`
  let b : ContDiffBump (1 / 2 : ℝ) := ⟨1, 2, one_pos, one_lt_two⟩
  let ψ : ℝ → ℝ := fun t => 1 / 2 + (t - 1 / 2) * b t
  have hψc : ContDiff ℝ 1 ψ := contDiff_const.add ((contDiff_id.sub contDiff_const).mul b.contDiff)
  have hψid : ∀ t ∈ Icc (0 : ℝ) 1, ψ =ᶠ[𝓝 t] id := by
    intro t ht
    have hb : t ∈ ball (1 / 2 : ℝ) b.rIn := by
      rw [mem_ball, Real.dist_eq, abs_lt]; show _ ∧ _; constructor <;> linarith [ht.1, ht.2]
    filter_upwards [b.eventuallyEq_one_of_mem_ball hb] with s hs
    simp only [ψ, id]; rw [hs]; simp
  have hψb : ∀ t, |ψ t| ≤ 3 := by
    intro t
    have h1 : |ψ t| ≤ 1 / 2 + |t - 1 / 2| * b t := by
      calc |ψ t| ≤ |(1 / 2 : ℝ)| + |(t - 1 / 2) * b t| := abs_add_le _ _
        _ = 1 / 2 + |t - 1 / 2| * b t := by rw [abs_mul, abs_of_nonneg b.nonneg]; norm_num
    by_cases h : |t - 1 / 2| < 2
    · nlinarith [(b.le_one : b t ≤ 1), (b.nonneg : 0 ≤ b t), abs_nonneg (t - 1 / 2)]
    · have : b t = 0 := b.zero_of_le_dist (by rw [Real.dist_eq]; show (2:ℝ) ≤ _; linarith [not_lt.1 h])
      rw [this, mul_zero] at h1; linarith
  have hmem : ∀ t, ψ t • v ∈ ball (0 : V) G.ρ := fun t => by
    rw [mem_ball_zero_iff, norm_smul, Real.norm_eq_abs]
    nlinarith [abs_nonneg (ψ t), norm_nonneg v, hψb t]
  -- the curve
  let γ : ℝ → V := fun t => G.expp (ψ t • v)
  have hγc : ContDiff ℝ 1 γ := contDiff_iff_contDiffAt.2 fun t => by
    have h1 : ContDiffAt ℝ 1 (fun s => ψ s • v) t := hψc.contDiffAt.smul contDiffAt_const
    have h2 := (G.lk_expp_contDiffAt hg (hmem t)).comp t h1
    exact h2
  have hψ0 : ψ 0 = 0 := by
    have : b 0 = 1 := b.one_of_mem_closedBall (by rw [mem_closedBall, Real.dist_eq]; norm_num)
    simp only [ψ, this]; norm_num
  have hψ1 : ψ 1 = 1 := by
    have : b 1 = 1 := b.one_of_mem_closedBall (by rw [mem_closedBall, Real.dist_eq]; norm_num)
    simp only [ψ, this]; norm_num
  -- on `[0,1]`: position and velocity of the radial geodesic
  have hpos : ∀ t ∈ Icc (0 : ℝ) 1, γ t = G.expp (t • v) := fun t ht => by
    simp only [γ]; rw [(hψid t ht).self_of_nhds]; rfl
  have hder : ∀ t ∈ Icc (0 : ℝ) 1, deriv γ t = G.Dexp (t • v) v := by
    intro t ht
    have htv : t • v ∈ ball (0 : V) G.ρ := by
      rw [mem_ball_zero_iff, norm_smul, Real.norm_eq_abs, abs_of_nonneg ht.1]
      nlinarith [norm_nonneg v, ht.2]
    have h1 : HasDerivAt (fun s : ℝ => G.expp (s • v)) (G.Dexp (t • v) v) t := by
      have hline : HasDerivAt (fun m : ℝ => m • v) v t := by
        simpa using (hasDerivAt_id t).smul_const v
      exact (G.lk_expp_hasFDerivAt hg htv).comp_hasDerivAt t hline
    have h2 : γ =ᶠ[𝓝 t] fun s : ℝ => G.expp (s • v) := by
      filter_upwards [hψid t ht] with s hs
      simp only [γ]; rw [hs]; rfl
    exact (h1.congr_of_eventuallyEq h2).deriv
  have hgeo : ∀ t ∈ Icc (0 : ℝ) 1, γ t = (G.D.α (p, G.c • v) (t * G.s₀)).1 ∧
      deriv γ t = G.s₀ • (G.D.α (p, G.c • v) (t * G.s₀)).2 := fun t ht =>
    ⟨(hpos t ht).trans (G.lk_expp_smul hg hv' ht), (hder t ht).trans (G.lk_Dexp_radial_at hg hv' ht)⟩
  have hM : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ S.M := fun t ht => by
    rw [(hgeo t ht).1]
    exact G.lk_ball_sub_M (G.lk_traj_in hg (G.lk_dom_closed hv') (G.lk_mul_s₀_mem ht))
  have htl : ∀ t ∈ Icc (0 : ℝ) 1, S.g (γ t) (deriv γ t) (deriv γ t) < 0 := fun t ht => by
    rw [(hgeo t ht).1, (hgeo t ht).2]
    have hE := G.lk_energy_cons hg (G.lk_dom_closed hv') (G.lk_mul_s₀_mem ht)
    simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at hE ⊢
    rw [hE]
    have hcs := G.lk_c_s₀
    have : G.s₀ * (G.s₀ * (G.c * (G.c * S.g p v v))) = S.g p v v := by
      linear_combination (G.c * G.s₀ + 1) * S.g p v v * hcs
    rw [this]; exact hvt.1
  -- the time orientation does not flip along `[0,1]`
  let h : ℝ → ℝ := fun t => S.g (γ t) (deriv γ t) (S.T (γ t))
  have hhc : Continuous h :=
    ((S.cont_g.comp hγc.continuous).clm_apply (hγc.continuous_deriv le_rfl)).clm_apply
      (S.cont_T.comp hγc.continuous)
  have hh0 : h 0 < 0 := by
    have e1 : γ 0 = p := by simp only [γ, hψ0, zero_smul]; exact G.lk_expp_zero hg
    have e2 : deriv γ 0 = v := by
      rw [hder 0 ⟨le_rfl, zero_le_one⟩, zero_smul, G.lk_Dexp_zero hg]; rfl
    simp only [h, e1, e2]; exact hvt.2
  have hne : ∀ t ∈ Icc (0 : ℝ) 1, h t ≠ 0 := fun t ht h0 => by
    have hd0 : deriv γ t ≠ 0 := fun hz => by have := htl t ht; rw [hz] at this; simp at this
    have := S.pos_on_perp (γ t) (hM t ht) (deriv γ t) h0 hd0
    linarith [htl t ht]
  have hfut : ∀ t ∈ Icc (0 : ℝ) 1, h t < 0 := by
    intro t ht
    by_contra hcon
    rw [not_lt] at hcon
    obtain ⟨s, hs, hs0⟩ := intermediate_value_Icc ht.1 hhc.continuousOn ⟨hh0.le, hcon⟩
    exact hne s ⟨hs.1, hs.2.trans ht.2⟩ hs0
  refine Relation.TransGen.single ⟨γ, hγc, ?_, ?_, fun t ht => ⟨hM t ht, htl t ht, hfut t ht⟩⟩
  · simp only [γ, hψ0, zero_smul]; exact G.lk_expp_zero hg
  · simp only [γ, hψ1, one_smul]

namespace NormalChart

variable {G} (N : G.NormalChart)

/-- **Inside the conoid is chronological.** A point `x` of the chart with `Q(x) < 0`, whose normal
coordinate `exp⁻¹ x` points to the future and is small, satisfies `p ≪ x`. -/
theorem lk_chr_of_Q_neg (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) (hQ : N.Q x < 0)
    (hfut : S.g p (N.Φ.symm x) (S.T p) < 0) (hsmall : N.Φ.symm x ∈ ball (0 : V) (G.ρ / 3)) :
    S.Chr p x := by
  have := G.lk_chr_of_timelike hg hsmall ⟨hQ, hfut⟩
  rwa [N.lk_good_expp hx] at this

end NormalChart

end GeoFlow

end Spacetime



/-! ## Axiom audit -/

#print axioms Spacetime.lk_christoffel_koszul
#print axioms Spacetime.lk_christoffel_symm
#print axioms Spacetime.lk_christoffel_quad
#print axioms Spacetime.lk_christoffel_contDiffAt
#print axioms Spacetime.lk_cutField_contDiff
#print axioms Spacetime.lk_fst_fderiv_cutField
#print axioms Spacetime.lk_energy_hasFDerivAt
#print axioms Spacetime.lk_causal_perp_null
#print axioms FlowData.lk_unique
#print axioms FlowData.lk_fixed
#print axioms FlowData.lk_lip_center
#print axioms FlowData.lk_affine_of_deriv
#print axioms Spacetime.lk_geoFlow_exists
#print axioms Spacetime.GeoFlow.lk_traj_in
#print axioms Spacetime.GeoFlow.lk_geodesic
#print axioms Spacetime.GeoFlow.lk_scaling
#print axioms Spacetime.GeoFlow.lk_expp_hasFDerivAt
#print axioms Spacetime.GeoFlow.lk_expp_contDiffAt
#print axioms Spacetime.GeoFlow.lk_expp_zero
#print axioms Spacetime.GeoFlow.lk_expp_smul
#print axioms Spacetime.GeoFlow.lk_Dexp_radial_at
#print axioms Spacetime.GeoFlow.lk_Dexp_radial
#print axioms Spacetime.GeoFlow.lk_Dexp_zero
#print axioms Spacetime.GeoFlow.lk_expp_fderiv_zero
#print axioms Spacetime.GeoFlow.lk_expp_localDiffeo
#print axioms Spacetime.GeoFlow.lk_energy_cons
#print axioms Spacetime.GeoFlow.lk_energy_variation
#print axioms Spacetime.GeoFlow.lk_gauss_flow
#print axioms Spacetime.GeoFlow.lk_gauss
#print axioms Spacetime.GeoFlow.lk_rad_energy
#print axioms Spacetime.GeoFlow.lk_normalChart_exists
#print axioms Spacetime.GeoFlow.NormalChart.lk_grad_Q
#print axioms Spacetime.GeoFlow.NormalChart.lk_P_energy
#print axioms Spacetime.GeoFlow.NormalChart.lk_P_ne_zero
#print axioms Spacetime.GeoFlow.NormalChart.lk_P_euler
#print axioms Spacetime.GeoFlow.NormalChart.lk_null_tangent
#print axioms Spacetime.GeoFlow.NormalChart.lk_ae_null_tangent
#print axioms Spacetime.GeoFlow.lk_chr_of_timelike
#print axioms Spacetime.GeoFlow.NormalChart.lk_chr_of_Q_neg

end ShadowProbe.LipschitzCornerProbe

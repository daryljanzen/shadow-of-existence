import Mathlib.Analysis.ODE.ExistUnique
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Geometry.Manifold.IntegralCurve.ExistUnique

/-!
# Probe T3b of `r7281+71.1`: the flow is `C¹` in the initial point

Classed THEORY at `r7269+71.2` (A5, the flow), unprobed; split at `r7281+71.1` into the group law (T3a, built)
and this. **Statement, as pre-registered: for a `C¹` vector field on a boundaryless manifold, `x ↦ φ(t, x)` is
`C¹` near a point, for small `t`. Budget: 250 lines.**

`mathlib` `4e6064a4` has the flow's smoothness in TIME (`contDiffOn_enat_picard_Icc`) and only LIPSCHITZ
dependence on the initial point (`exists_forall_mem_closedBall_eq_hasDerivWithinAt_lipschitzOnWith`). The
route written here is the textbook one, in order:
1. the first-order remainder of a `C¹` map is uniformly small on a compact ball;
2. the local flow, Lipschitz in the initial point, inside a compact set;
3. the variational equation `J′ = Df(φ) ∘ J`, `J 0 = id`, a linear ODE in `E →L E`;
4. Grönwall on `φ(t, y) − φ(t, x) − J(t)(y − x)`: `x ↦ φ(t, x)` has derivative `J(t)`;
5. Grönwall on `J_y − J_x`: the derivative is continuous in `x`;
6. `C¹` on the vector space;
7. the chart transfer to a manifold.

Nothing imports this file.
-/

open Set Filter Topology Metric
open scoped NNReal

set_option linter.unusedSectionVars false

namespace ShadowProbe

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-- **1.** The first-order remainder of a `C¹` map is uniformly small on a closed ball. -/
lemma remainder_unif (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) (R ε : ℝ) (hε : 0 < ε) :
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
lemma local_flow (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) :
    ∃ τ > (0 : ℝ), ∃ r > (0 : ℝ), ∃ α : E → ℝ → E, ∃ L : ℝ≥0,
      (∀ x ∈ closedBall x₀ r, α x 0 = x ∧
        ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t) ∧
      ∀ t ∈ Icc (-τ) τ, LipschitzOnWith L (α · t) (closedBall x₀ r) := by
  obtain ⟨τ, hτ, a, r, L, K, hr, hPL⟩ := IsPicardLindelof.of_contDiffAt_one (hf.contDiffAt (x := x₀))
  obtain ⟨α, hα, L', hL'⟩ :=
    (hPL 0).exists_forall_mem_closedBall_eq_hasDerivWithinAt_lipschitzOnWith
  simp only [zero_sub, zero_add] at hα hL'
  exact ⟨τ, hτ, r, hr, α, L', hα, hL'⟩

/-! ## 3. Linear ODEs on `[0, T]` — copied from `TransportProbe.lean`, for a general complete `F` -/

section Linear

variable {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]

/-- One local step: on `[s, s + h]`, where `‖A t‖ ≤ M` and `M h ≤ 1/2`, from any `x`. -/
lemma linear_step (A : ℝ → F →L[ℝ] F) (hA : Continuous A) (M : ℝ) (hM : 0 ≤ M)
    (h s : ℝ) (hh : 0 ≤ h) (hMh : M * h ≤ 1 / 2) (hAM : ∀ t ∈ Icc s (s + h), ‖A t‖ ≤ M) (x : F) :
    ∃ W : ℝ → F, W s = x ∧
      ∀ t ∈ Icc s (s + h), HasDerivWithinAt W (A t (W t)) (Icc s (s + h)) t := by
  have hs : s ∈ Icc s (s + h) := ⟨le_rfl, by linarith⟩
  have hPL : IsPicardLindelof (fun t y => A t y) (⟨s, hs⟩ : Icc s (s + h)) x
      ⟨‖x‖ + 1, by positivity⟩ 0 ⟨M * (2 * ‖x‖ + 1), by positivity⟩ ⟨M, hM⟩ := by
    refine ⟨fun t ht => ?_, fun y _ => ?_, fun t ht y hy => ?_, ?_⟩
    · refine LipschitzWith.lipschitzOnWith (LipschitzWith.of_dist_le_mul fun y z => ?_)
      rw [dist_eq_norm, dist_eq_norm, ← map_sub]
      exact (A t).le_of_opNorm_le (hAM t ht) _
    · exact (hA.clm_apply continuous_const).continuousOn
    · have hy' : ‖y‖ ≤ 2 * ‖x‖ + 1 := by
        rw [Metric.mem_closedBall, dist_eq_norm] at hy
        have := norm_le_norm_add_norm_sub' y x
        have hy2 : ‖y - x‖ ≤ ‖x‖ + 1 := hy
        linarith
      exact ((A t).le_opNorm y).trans (mul_le_mul (hAM t ht) hy' (norm_nonneg _) hM)
    · simp only [NNReal.coe_zero, sub_zero, sub_self, add_sub_cancel_left]
      rw [max_eq_left hh]
      show M * (2 * ‖x‖ + 1) * h ≤ ‖x‖ + 1
      nlinarith [norm_nonneg x]
  exact hPL.exists_eq_forall_mem_Icc_hasDerivWithinAt₀

/-- Gluing a solution on `[0, c]` to one on `[c, d]` that starts where the first ends. -/
lemma linear_glue (A : ℝ → F →L[ℝ] F) (V W : ℝ → F) (c d : ℝ) (hc : 0 ≤ c) (hcd : c ≤ d)
    (hV : ∀ t ∈ Icc 0 c, HasDerivWithinAt V (A t (V t)) (Icc 0 c) t)
    (hW : ∀ t ∈ Icc c d, HasDerivWithinAt W (A t (W t)) (Icc c d) t) (hVW : W c = V c) :
    ∀ t ∈ Icc 0 d, HasDerivWithinAt (fun t => if t ≤ c then V t else W t)
      (A t (if t ≤ c then V t else W t)) (Icc 0 d) t := by
  intro t _
  set U := fun t => if t ≤ c then V t else W t with hU
  have hUV : ∀ y ∈ Icc 0 c, U y = V y := fun y hy => by simp [hU, hy.2]
  have hUW : ∀ y ∈ Icc c d, U y = W y := fun y hy => by
    rcases eq_or_lt_of_le hy.1 with h | h
    · subst h; simp [hU, hVW]
    · simp [hU, not_le.2 h]
  rw [← Icc_union_Icc_eq_Icc hc hcd]
  show HasDerivWithinAt U (A t (U t)) (Icc 0 c ∪ Icc c d) t
  refine HasDerivWithinAt.union ?_ ?_
  · by_cases h : t ∈ Icc 0 c
    · rw [hUV t h]; exact (hV t h).congr_of_mem hUV h
    · exact hasDerivWithinAt_iff_hasFDerivWithinAt.2
        (.of_notMem_closure (by rwa [isClosed_Icc.closure_eq]))
  · by_cases h : t ∈ Icc c d
    · rw [hUW t h]; exact (hW t h).congr_of_mem hUW h
    · exact hasDerivWithinAt_iff_hasFDerivWithinAt.2
        (.of_notMem_closure (by rwa [isClosed_Icc.closure_eq]))

/-- A linear ODE `V′ = A(t) V` with `A` continuous has a solution through `v` on `[0, T]`. -/
theorem linear_exists (A : ℝ → F →L[ℝ] F) (hA : Continuous A) (T : ℝ) (hT : 0 < T) (v : F) :
    ∃ V : ℝ → F, V 0 = v ∧ ∀ t ∈ Ioo 0 T, HasDerivAt V (A t (V t)) t := by
  obtain ⟨C, hC⟩ := isCompact_Icc.exists_bound_of_continuousOn (hA.continuousOn (s := Icc 0 (T + 1)))
  set M := max C 0
  have hM : 0 ≤ M := le_max_right _ _
  have hAM : ∀ t ∈ Icc 0 (T + 1), ‖A t‖ ≤ M := fun t ht => (hC t ht).trans (le_max_left _ _)
  set h := 1 / (2 * (M + 1)) with hh
  have hh0 : 0 < h := by positivity
  have hh1 : h ≤ 1 := by rw [hh, div_le_one (by positivity)]; linarith
  have hMh : M * h ≤ 1 / 2 := by
    rw [hh, mul_one_div, div_le_div_iff₀ (by positivity) (by norm_num)]; nlinarith
  have key : ∀ n : ℕ, (n : ℝ) * h ≤ T + h → ∃ V : ℝ → F, V 0 = v ∧
      ∀ t ∈ Icc 0 (n * h), HasDerivWithinAt V (A t (V t)) (Icc 0 (n * h)) t := by
    intro n
    induction n with
    | zero =>
      intro _
      refine ⟨fun _ => v, rfl, fun t ht => ?_⟩
      simp only [Nat.cast_zero, zero_mul, Icc_self] at ht ⊢
      exact hasDerivWithinAt_iff_hasFDerivWithinAt.2 HasFDerivWithinAt.singleton
    | succ n ih =>
      intro hn
      push_cast at hn
      have hnT : (n : ℝ) * h ≤ T := by nlinarith
      obtain ⟨V, hV0, hV⟩ := ih (by linarith)
      have hn0 : 0 ≤ (n : ℝ) * h := by positivity
      obtain ⟨W, hW0, hW⟩ := linear_step A hA M hM h (n * h) hh0.le hMh
        (fun t ht => hAM t ⟨hn0.trans ht.1, by linarith [ht.2]⟩) (V (n * h))
      refine ⟨fun t => if t ≤ n * h then V t else W t, by simp [hn0, hV0], ?_⟩
      have := linear_glue A V W (n * h) (n * h + h) hn0 (by linarith) hV hW hW0
      push_cast
      rw [add_mul, one_mul]
      exact this
  have hc := Nat.ceil_lt_add_one (div_nonneg hT.le hh0.le)
  have hTN : T ≤ ⌈T / h⌉₊ * h := by
    have := Nat.le_ceil (T / h); rwa [div_le_iff₀ hh0] at this
  obtain ⟨V, hV0, hV⟩ := key ⌈T / h⌉₊ (by
    have h2 : (⌈T / h⌉₊ : ℝ) * h < (T / h + 1) * h := mul_lt_mul_of_pos_right hc hh0
    rw [add_mul, div_mul_cancel₀ _ hh0.ne'] at h2; linarith)
  exact ⟨V, hV0, fun t ht => (hV t ⟨ht.1.le, by linarith [ht.2]⟩).hasDerivAt
    (Icc_mem_nhds ht.1 (by linarith [ht.2]))⟩

end Linear

/-- **3.** The variational equation `J′ = Df(φ t) ∘ J`, `J 0 = id`, along a curve `φ` continuous on
`[0, τ]`. -/
lemma variational_exists (f : E → E) (hf : ContDiff ℝ 1 f) (φ : ℝ → E) (τ : ℝ) (hτ : 0 < τ)
    (hφ : ContinuousOn φ (Icc 0 τ)) :
    ∃ J : ℝ → E →L[ℝ] E, J 0 = ContinuousLinearMap.id ℝ E ∧
      ∀ t ∈ Ioo 0 τ, HasDerivAt J ((fderiv ℝ f (φ t)).comp (J t)) t := by
  set φ' := IccExtend hτ.le (Icc 0 τ |>.domRestrict φ)
  have hφ' : Continuous φ' := hφ.domRestrict.Icc_extend'
  obtain ⟨J, hJ0, hJ⟩ := linear_exists (fun t => ContinuousLinearMap.compL ℝ E E E (fderiv ℝ f (φ' t)))
    ((ContinuousLinearMap.compL ℝ E E E).continuous.comp
      ((hf.continuous_fderiv one_ne_zero).comp hφ')) τ hτ (ContinuousLinearMap.id ℝ E)
  refine ⟨J, hJ0, fun t ht => ?_⟩
  have := hJ t ht
  rwa [show φ' t = φ t from IccExtend_of_mem _ _ (Ioo_subset_Icc_self ht)] at this

/-- **4, part (a).** The trajectories from `closedBall x₀ r` over `[-τ, τ]` stay in one closed ball. -/
lemma flow_bounded (f : E → E) (τ r : ℝ) (α : E → ℝ → E) (L : ℝ≥0) (x₀ : E)
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

/-- **4.** `y ↦ α y t` has derivative `J t` at `x`: Grönwall on `e s = α y s − α x s − J s (y − x)`. -/
lemma flow_hasFDerivAt (f : E → E) (hf : ContDiff ℝ 1 f) (τ r R M : ℝ) (α : E → ℝ → E) (L : ℝ≥0)
    (x₀ x : E) (hα : ∀ x ∈ closedBall x₀ r, α x 0 = x ∧
      ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t)
    (hL : ∀ t ∈ Icc (-τ) τ, LipschitzOnWith L (α · t) (closedBall x₀ r))
    (hR : ∀ x ∈ closedBall x₀ r, ∀ t ∈ Icc (-τ) τ, α x t ∈ closedBall x₀ R)
    (hM : ∀ y ∈ closedBall x₀ R, ‖fderiv ℝ f y‖ ≤ M) (hx : x ∈ ball x₀ r)
    (J : ℝ → E →L[ℝ] E) (hJ0 : J 0 = ContinuousLinearMap.id ℝ E)
    (hJ : ∀ t ∈ Ioo 0 τ, HasDerivAt J ((fderiv ℝ f (α x t)).comp (J t)) t) (t : ℝ) (ht : t ∈ Ioo 0 τ) :
    HasFDerivAt (fun y => α y t) (J t) x := by
  rw [hasFDerivAt_iff_isLittleO_nhds_zero]
  refine Asymptotics.IsLittleO.of_bound fun ε hε => ?_
  -- STOPPED HERE, at the budget. What the next lines must do:
  -- `norm_le_gronwallBound_of_norm_deriv_right_le` on `e` over `[0, t]` needs `e` continuous on
  -- `Icc 0 t` and a right derivative at every point of `Ico 0 t`, INCLUDING `0`. `variational_exists`
  -- (through `linear_exists`) exports `J 0 = id` and `HasDerivAt` on `Ioo 0 τ` only, so step 3 must be
  -- re-opened to export the `Icc` derivative it has internally. Then: `remainder_unif` with
  -- `ε / (L · t · exp (M t) + 1)`, the Lipschitz bound `‖α y s − α x s‖ ≤ L ‖y − x‖`, and
  -- `‖e′ s‖ ≤ M ‖e s‖ + ε' L ‖y − x‖`. Steps 5 (continuity of `J` in `x`, a second Grönwall), 6 (`C¹`
  -- on `E`) and 7 (the chart transfer to a manifold) are not begun.
  sorry

end ShadowProbe

#print axioms ShadowProbe.remainder_unif
#print axioms ShadowProbe.variational_exists
#print axioms ShadowProbe.flow_bounded
#print axioms ShadowProbe.flow_hasFDerivAt

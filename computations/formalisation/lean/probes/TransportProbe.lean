import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Basic
import Mathlib.Geometry.Manifold.VectorBundle.LocalFrame
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Analysis.ODE.ExistUnique

/-!
# Probe T1 of `r7281+71.1`: parallel transport along a curve, on a vector space

Classed THEORY at `r7273+71.5` (B9, parallel transport), unprobed. **Scope, as pre-registered: `M = E`, a
finite-dimensional real vector space, its own model.** There `covDerivAlong`'s frame is the constant basis, and
`D/dt V = 0` is the linear ODE `V′ = −G(γ)(γ̇, V)`.

`mathlib`'s Picard–Lindelöf is local: it needs `L · (time) ≤ a` on a ball of radius `a`, which a linear field
meets only for times `≲ 1 / sup ‖A‖`. So the solution on `[0, T]` is glued from steps of one fixed length.

The connection is a hypothesis; its Christoffel form `G` is continuous along `γ`. `vel` and `covDerivAlong` are
copied verbatim from `GeodesicProbe.lean`, and the model-space lemmas from `GeodesicExistProbe.lean`. Nothing
imports this file.
-/

open Bundle Manifold Filter Set Topology
open scoped ContDiff

set_option linter.unusedSectionVars false

namespace ShadowProbe

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]

/-- The velocity of a curve, as a tangent vector. -/
noncomputable def vel (γ : ℝ → M) (t : ℝ) : TangentSpace I (γ t) :=
  mfderiv 𝓘(ℝ, ℝ) I γ t (show TangentSpace 𝓘(ℝ, ℝ) t from (1 : ℝ))

/-- **Q4 (B6).** The covariant derivative of a vector field along a curve. -/
noncomputable def covDerivAlong (cov : CovariantDerivative I E (TangentSpace I : M → Type _))
    (γ : ℝ → M) (V : Π t : ℝ, TangentSpace I (γ t)) (t : ℝ) : TangentSpace I (γ t) :=
  let e := trivializationAt E (TangentSpace I : M → Type _) (γ t)
  let b := Module.finBasis ℝ E
  ∑ i, ((deriv (fun s => e.localFrameCoeff I b i (γ s) (V s)) t) • e.localFrame b i (γ t)
    + (e.localFrameCoeff I b i (γ t) (V t)) • cov (e.localFrame b i) (γ t) (vel γ t))

/-! ## On the model space -/

section Model

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  [FiniteDimensional ℝ E]

set_option backward.isDefEq.respectTransparency false in
/-- On `E` as its own model, the frame of any trivialisation of `TE` is the basis, constant. -/
lemma model_localFrame (x₀ x : E) (i : Fin (Module.finrank ℝ E)) :
    (trivializationAt E (TangentSpace 𝓘(ℝ, E) : E → Type _) x₀).localFrame (Module.finBasis ℝ E) i x
      = Module.finBasis ℝ E i := by
  have hx : x ∈ (trivializationAt E (TangentSpace 𝓘(ℝ, E) : E → Type _) x₀).baseSet := by simp
  rw [Trivialization.localFrame_apply_of_mem_baseSet _ _ hx]
  simp only [Trivialization.basisAt, Module.Basis.map_apply]
  rw [Trivialization.linearEquivAt_symm_apply, ← Trivialization.symmL_apply (R := ℝ) _ hx,
    TangentBundle.symmL_model_space]
  rfl


set_option backward.isDefEq.respectTransparency false in
/-- On `E`, the frame coefficients of a vector are its coordinates in the basis. -/
lemma model_localFrameCoeff (x₀ x : E) (i : Fin (Module.finrank ℝ E)) (u : E) :
    (trivializationAt E (TangentSpace 𝓘(ℝ, E) : E → Type _) x₀).localFrameCoeff 𝓘(ℝ, E)
      (Module.finBasis ℝ E) i x u = (Module.finBasis ℝ E).repr u i := by
  have hx : x ∈ (trivializationAt E (TangentSpace 𝓘(ℝ, E) : E → Type _) x₀).baseSet := by simp
  rw [show u = (fun _ : E => u) x from rfl,
    Trivialization.localFrameCoeff_apply_of_mem_baseSet _ _ hx (fun _ : E => u) i]
  simp only [Trivialization.basisAt, Module.Basis.map_repr, LinearEquiv.trans_apply,
    LinearEquiv.symm_symm]
  rw [Trivialization.linearEquivAt_apply]
  simp

/-- On `E`: for a `cov` whose Christoffel form is `G`, `D/dt V = V′ + G(γ)(γ̇, V)`. -/
lemma covDerivAlong_model (cov : CovariantDerivative 𝓘(ℝ, E) E (TangentSpace 𝓘(ℝ, E) : E → Type _))
    (G : E → E →L[ℝ] E →L[ℝ] E) (hG : ∀ x w u, cov (fun _ => u) x w = G x w u)
    (γ : ℝ → E) (V : ℝ → E) (t : ℝ) (hV : DifferentiableAt ℝ V t) :
    covDerivAlong cov γ V t = deriv V t + G (γ t) (vel (I := 𝓘(ℝ, E)) γ t) (V t) := by
  unfold covDerivAlong
  have hfr : ∀ i, (trivializationAt E (TangentSpace 𝓘(ℝ, E)) (γ t)).localFrame
      (Module.finBasis ℝ E) i = fun _ => Module.finBasis ℝ E i :=
    fun i => funext fun x => model_localFrame _ _ _
  simp only [hfr, hG, model_localFrameCoeff]
  have hc : ∀ i, deriv (fun s => (Module.finBasis ℝ E).repr (V s) i) t
      = (Module.finBasis ℝ E).repr (deriv V t) i := by
    intro i
    have hL := (LinearMap.toContinuousLinearMap ((Module.finBasis ℝ E).coord i)).hasFDerivAt
      |>.comp_hasDerivAt t hV.hasDerivAt
    exact hL.deriv
  simp only [hc, Finset.sum_add_distrib]
  congr 1
  · exact (Module.finBasis ℝ E).sum_repr (deriv V t)
  · show ∑ x, ((Module.finBasis ℝ E).repr (V t)) x •
        (G (γ t) (show E from vel (I := 𝓘(ℝ, E)) γ t)) ((Module.finBasis ℝ E) x)
      = (G (γ t) (show E from vel (I := 𝓘(ℝ, E)) γ t)) (V t)
    generalize (G (γ t) (show E from vel (I := 𝓘(ℝ, E)) γ t)) = L
    conv_rhs => rw [← (Module.finBasis ℝ E).sum_repr (V t)]
    simp only [map_sum, map_smul]


/-- On `E`, the velocity is the derivative. -/
lemma vel_model (γ : ℝ → E) (t : ℝ) : vel (I := 𝓘(ℝ, E)) γ t = deriv γ t := by
  unfold vel
  rw [mfderiv_eq_fderiv, ← fderiv_apply_one_eq_deriv]
  rfl

/-! ## The linear ODE on `[0, T]` -/

/-- One local step: on `[s, s + h]`, where `‖A t‖ ≤ M` and `M h ≤ 1/2`, from any `x`. -/
lemma linear_step (A : ℝ → E →L[ℝ] E) (hA : Continuous A) (M : ℝ) (hM : 0 ≤ M)
    (h s : ℝ) (hh : 0 ≤ h) (hMh : M * h ≤ 1 / 2) (hAM : ∀ t ∈ Icc s (s + h), ‖A t‖ ≤ M) (x : E) :
    ∃ W : ℝ → E, W s = x ∧
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
lemma linear_glue (A : ℝ → E →L[ℝ] E) (V W : ℝ → E) (c d : ℝ) (hc : 0 ≤ c) (hcd : c ≤ d)
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
theorem linear_exists (A : ℝ → E →L[ℝ] E) (hA : Continuous A) (T : ℝ) (hT : 0 < T) (v : E) :
    ∃ V : ℝ → E, V 0 = v ∧ ∀ t ∈ Ioo 0 T, HasDerivAt V (A t (V t)) t := by
  obtain ⟨C, hC⟩ := isCompact_Icc.exists_bound_of_continuousOn (hA.continuousOn (s := Icc 0 (T + 1)))
  set M := max C 0
  have hM : 0 ≤ M := le_max_right _ _
  have hAM : ∀ t ∈ Icc 0 (T + 1), ‖A t‖ ≤ M := fun t ht => (hC t ht).trans (le_max_left _ _)
  set h := 1 / (2 * (M + 1)) with hh
  have hh0 : 0 < h := by positivity
  have hh1 : h ≤ 1 := by rw [hh, div_le_one (by positivity)]; linarith
  have hMh : M * h ≤ 1 / 2 := by
    rw [hh, mul_one_div, div_le_div_iff₀ (by positivity) (by norm_num)]; nlinarith
  have key : ∀ n : ℕ, (n : ℝ) * h ≤ T + h → ∃ V : ℝ → E, V 0 = v ∧
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

/-- **T1.** Parallel transport along a `C¹` curve on `E`, for a connection whose Christoffel form `G` is
continuous along the curve: from any `v` there is `V` with `V 0 = v` and `D/dt V = 0` on `(0, T)`. -/
theorem parallel_transport_exists
    (cov : CovariantDerivative 𝓘(ℝ, E) E (TangentSpace 𝓘(ℝ, E) : E → Type _))
    (G : E → E →L[ℝ] E →L[ℝ] E) (hG : ∀ x w u, cov (fun _ => u) x w = G x w u)
    (γ : ℝ → E) (hγ : ContDiff ℝ 1 γ) (hGγ : Continuous fun t => G (γ t))
    (T : ℝ) (hT : 0 < T) (v : E) :
    ∃ V : ℝ → E, V 0 = v ∧ ∀ t ∈ Ioo 0 T, covDerivAlong cov γ V t = 0 := by
  obtain ⟨V, hV0, hV⟩ := linear_exists (fun t => -(G (γ t) (deriv γ t)))
    (hGγ.clm_apply (hγ.continuous_deriv le_rfl)).neg T hT v
  refine ⟨V, hV0, fun t ht => ?_⟩
  rw [covDerivAlong_model cov G hG γ V t (hV t ht).differentiableAt, (hV t ht).deriv, vel_model]
  simp
  rfl

end Model

end ShadowProbe

#print axioms ShadowProbe.parallel_transport_exists

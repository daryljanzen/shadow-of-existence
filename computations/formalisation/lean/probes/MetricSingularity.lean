/-
# `MetricSingularity` — campaign 57, `r7613+71.1`

Source: `corpus/BH_causality_v2.tex`, `thm:metric-singularity` and `cor:threefold` (iii)–(iv).
Registration: `computations/formalisation/r7613_71_campaign57/PREDICTION.md`.

1. `thm:metric-singularity`, algebraic form (scalar and vector).
2. `thm:metric-singularity`, along-the-connection form (remark after the theorem).
3. `cor:threefold` (iii): `g(γ̇,γ̇) = 0` along the segment.
4. `cor:threefold` (iv), second half: without (b), `τ(q) - τ(p)` is not invariant under small
   smooth bumps of `τ`, which keep `τ` temporal (`∂_t τ ≥ c > 0` ⇒ `∂_t τ̃ ≥ c/2 > 0`).
-/
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Calculus.BumpFunction.InnerProduct
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension
import Mathlib.Analysis.Calculus.ContDiff.Operations
import Mathlib.Analysis.Calculus.FDeriv.Mul
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Normed.Group.Bounded

open Set Metric

noncomputable section

namespace MetricSingularity

/-! ## 1. Algebraic form -/

/-- `thm:metric-singularity`: from `Δs² = Δx² − Δτ²`, (a) `Δs² = 0`, (b) `Δx = 0`, get `Δτ = 0`. -/
theorem ms_metric_singularity_scalar (Δs2 Δx Δτ : ℝ)
    (hrel : Δs2 = Δx ^ 2 - Δτ ^ 2) (ha : Δs2 = 0) (hb : Δx = 0) : Δτ = 0 := by
  subst hb
  have : Δτ ^ 2 = 0 := by nlinarith
  exact pow_eq_zero_iff (two_ne_zero) |>.mp this

/-- `thm:metric-singularity`, vector form: `Δx ∈ ℝⁿ`, `Δs² = ‖Δx‖² − Δτ²`. -/
theorem ms_metric_singularity_vec {n : ℕ} (Δs2 Δτ : ℝ) (Δx : EuclideanSpace ℝ (Fin n))
    (hrel : Δs2 = ‖Δx‖ ^ 2 - Δτ ^ 2) (ha : Δs2 = 0) (hb : Δx = 0) : Δτ = 0 :=
  ms_metric_singularity_scalar Δs2 ‖Δx‖ Δτ hrel ha (by simp [hb])

/-! ## 2. Along-the-connection form -/

/-- A function on `ℝ` with derivative `0` at every point of `[0,1]` is constant on `[0,1]`. -/
theorem ms_const_of_hasDerivAt_zero {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (f f' : ℝ → F) (hf : ∀ t ∈ Icc (0 : ℝ) 1, HasDerivAt f (f' t) t)
    (h0 : ∀ t ∈ Icc (0 : ℝ) 1, f' t = 0) : f 1 = f 0 := by
  have hcont : ContinuousOn f (Icc (0 : ℝ) 1) := fun t ht => (hf t ht).continuousAt.continuousWithinAt
  refine constant_of_has_deriv_right_zero hcont (fun t ht => ?_) 1 ⟨zero_le_one, le_rfl⟩
  have ht' : t ∈ Icc (0 : ℝ) 1 := Ico_subset_Icc_self ht
  simpa [h0 t ht'] using (hf t ht').hasDerivWithinAt (s := Ici t)

/-- Remark after `thm:metric-singularity`: along a curve `γ = (τ, x)` on `[0,1]` with
`‖x'‖² − τ'² = 0` and (b) `x' = 0` everywhere on the segment, `τ' = 0` on the segment. -/
theorem ms_along_tau_deriv_zero {n : ℕ} (τ' : ℝ → ℝ) (x' : ℝ → EuclideanSpace ℝ (Fin n))
    (hnull : ∀ t ∈ Icc (0 : ℝ) 1, ‖x' t‖ ^ 2 - (τ' t) ^ 2 = 0)
    (hb : ∀ t ∈ Icc (0 : ℝ) 1, x' t = 0) : ∀ t ∈ Icc (0 : ℝ) 1, τ' t = 0 := fun t ht =>
  ms_metric_singularity_vec _ (τ' t) (x' t) rfl (hnull t ht) (hb t ht)

/-- `thm:metric-singularity`, along-the-connection form: `Δτ = τ 1 − τ 0 = 0` and the
spatial separation `Δx = x 1 − x 0 = 0`. -/
theorem ms_metric_singularity_along {n : ℕ} (τ τ' : ℝ → ℝ) (x x' : ℝ → EuclideanSpace ℝ (Fin n))
    (hτ : ∀ t ∈ Icc (0 : ℝ) 1, HasDerivAt τ (τ' t) t)
    (hx : ∀ t ∈ Icc (0 : ℝ) 1, HasDerivAt x (x' t) t)
    (hnull : ∀ t ∈ Icc (0 : ℝ) 1, ‖x' t‖ ^ 2 - (τ' t) ^ 2 = 0)
    (hb : ∀ t ∈ Icc (0 : ℝ) 1, x' t = 0) :
    (∀ t ∈ Icc (0 : ℝ) 1, τ' t = 0) ∧ τ 1 = τ 0 ∧ x 1 = x 0 := by
  have h0 := ms_along_tau_deriv_zero τ' x' hnull hb
  exact ⟨h0, ms_const_of_hasDerivAt_zero τ τ' hτ h0, ms_const_of_hasDerivAt_zero x x' hx hb⟩

/-! ## 3. `cor:threefold` (iii) -/

/-- Minkowski quadratic form of a tangent `(τ', x')`: `g(γ̇,γ̇) = ‖x'‖² − τ'²`. -/
def ms_g (τ' : ℝ) {n : ℕ} (x' : EuclideanSpace ℝ (Fin n)) : ℝ := ‖x'‖ ^ 2 - τ' ^ 2

/-- `cor:threefold` (iii), restated: on a null segment `g(γ̇,γ̇) = 0` at every parameter. -/
theorem ms_threefold_iii {n : ℕ} (τ' : ℝ → ℝ) (x' : ℝ → EuclideanSpace ℝ (Fin n))
    (hnull : ∀ t ∈ Icc (0 : ℝ) 1, ‖x' t‖ ^ 2 - (τ' t) ^ 2 = 0) :
    ∀ t ∈ Icc (0 : ℝ) 1, ms_g (τ' t) (x' t) = 0 := hnull

/-- `cor:threefold` (iii), from (b) and `τ' = 0` (no null hypothesis used): `g(γ̇,γ̇) = 0`. -/
theorem ms_threefold_iii_of_b {n : ℕ} (τ' : ℝ → ℝ) (x' : ℝ → EuclideanSpace ℝ (Fin n))
    (hb : ∀ t ∈ Icc (0 : ℝ) 1, x' t = 0) (hτ0 : ∀ t ∈ Icc (0 : ℝ) 1, τ' t = 0) :
    ∀ t ∈ Icc (0 : ℝ) 1, ms_g (τ' t) (x' t) = 0 := fun t ht => by
  simp [ms_g, hb t ht, hτ0 t ht]

/-! ## 4. `cor:threefold` (iv), second half: non-invariance without (b) -/

/-- The time direction `e₀` of the chart `ℝ^{n+1}` (coordinate `0` is time). -/
def ms_e0 (n : ℕ) : EuclideanSpace ℝ (Fin (n + 1)) := EuclideanSpace.single 0 1

/-- `cor:threefold` (iv), second half. Let `τ` be `C^k` (`k ≥ 1`) and temporal,
`∂_t τ ≥ c > 0` everywhere, and let `p ≠ q`. For every `ε > 0` there is a smooth `φ` with
`|φ| ≤ ε`, support inside `ball q (dist p q / 2)` (so `p ∉ support`), such that `τ̃ = τ + φ` is
again `C^k`, still temporal (`∂_t τ̃ ≥ c/2 > 0`), and `τ̃(q) − τ̃(p) ≠ τ(q) − τ(p)`. -/
theorem ms_threefold_iv_noninvariance {n : ℕ} {k : ℕ∞} (hk : 1 ≤ k)
    (τ : EuclideanSpace ℝ (Fin (n + 1)) → ℝ) (hτ : ContDiff ℝ k τ)
    (c : ℝ) (hc : 0 < c) (htemp : ∀ z, c ≤ fderiv ℝ τ z (ms_e0 n))
    (p q : EuclideanSpace ℝ (Fin (n + 1))) (hpq : p ≠ q) (ε : ℝ) (hε : 0 < ε) :
    ∃ φ : EuclideanSpace ℝ (Fin (n + 1)) → ℝ,
      ContDiff ℝ ((⊤ : ℕ∞) : WithTop ℕ∞) φ ∧
      (∀ z, |φ z| ≤ ε) ∧
      Function.support φ ⊆ ball q (dist p q / 2) ∧
      p ∉ ball q (dist p q / 2) ∧
      ContDiff ℝ k (τ + φ) ∧
      (∀ z, c / 2 ≤ fderiv ℝ (τ + φ) z (ms_e0 n)) ∧
      (τ + φ) q - (τ + φ) p ≠ τ q - τ p := by
  have hd : 0 < dist p q := dist_pos.2 hpq
  let b : ContDiffBump q :=
    ⟨dist p q / 4, dist p q / 2, by positivity, by linarith⟩
  -- bound on the time-derivative of the bump
  have hcont : Continuous fun z => fderiv ℝ b z (ms_e0 n) :=
    (b.contDiff (n := (⊤ : ℕ∞))).continuous_fderiv_apply (by simp) |>.comp
      (continuous_id.prodMk continuous_const)
  obtain ⟨C, hC⟩ := hcont.bounded_above_of_compact_support (HasCompactSupport.fderiv_apply ℝ b.hasCompactSupport (ms_e0 n))
  have hC0 : 0 ≤ C := (norm_nonneg _).trans (hC q)
  set δ : ℝ := min ε (c / (2 * (C + 1))) with hδdef
  have hδpos : 0 < δ := lt_min hε (by positivity)
  have hδε : δ ≤ ε := min_le_left _ _
  have hδc : δ * C ≤ c / 2 := by
    have h1 : δ ≤ c / (2 * (C + 1)) := min_le_right _ _
    calc δ * C ≤ c / (2 * (C + 1)) * C := mul_le_mul_of_nonneg_right h1 hC0
      _ ≤ c / (2 * (C + 1)) * (C + 1) := by gcongr; linarith
      _ = c / 2 := by field_simp
  have hpball : p ∉ ball q (dist p q / 2) := by
    rw [mem_ball]; linarith
  refine ⟨fun z => δ * b z, contDiff_const.mul (b.contDiff (n := (⊤ : ℕ∞))), ?_, ?_, hpball, ?_, ?_, ?_⟩
  · intro z
    rw [abs_mul, abs_of_pos hδpos, abs_of_nonneg b.nonneg]
    calc δ * b z ≤ δ * 1 := by gcongr; exact b.le_one
      _ ≤ ε := by linarith
  · intro z hz
    have : b z ≠ 0 := right_ne_zero_of_mul hz
    have hs : z ∈ Function.support b := this
    rwa [b.support_eq] at hs
  · exact hτ.add (contDiff_const.mul (b.contDiff (n := k)))
  · intro z
    have hτd : DifferentiableAt ℝ τ z := hτ.differentiable (by exact_mod_cast (ne_of_gt (lt_of_lt_of_le zero_lt_one hk))) z
    have hbd : DifferentiableAt ℝ (fun z => δ * b z) z :=
      ((contDiff_const.mul (b.contDiff (n := 1))).differentiable one_ne_zero) z
    have hbd' : DifferentiableAt ℝ b z := (b.contDiff (n := 1)).differentiable one_ne_zero z
    rw [fderiv_add hτd hbd, fderiv_const_mul hbd' δ]
    simp only [add_apply, smul_apply, smul_eq_mul]
    have h1 := htemp z
    have h2 : |fderiv ℝ b z (ms_e0 n)| ≤ C := by simpa using hC z
    have h3 : -(δ * C) ≤ δ * fderiv ℝ b z (ms_e0 n) := by
      have := neg_abs_le (fderiv ℝ b z (ms_e0 n))
      nlinarith
    linarith
  · have hbq : b q = 1 := b.one_of_mem_closedBall (mem_closedBall_self (by positivity))
    have hbp : b p = 0 := b.zero_of_le_dist (le_of_lt (by show dist p q / 2 < dist p q; linarith))
    simp only [Pi.add_apply, hbq, hbp]
    intro h
    linarith

end MetricSingularity

#print axioms MetricSingularity.ms_metric_singularity_scalar
#print axioms MetricSingularity.ms_metric_singularity_vec
#print axioms MetricSingularity.ms_const_of_hasDerivAt_zero
#print axioms MetricSingularity.ms_along_tau_deriv_zero
#print axioms MetricSingularity.ms_metric_singularity_along
#print axioms MetricSingularity.ms_threefold_iii
#print axioms MetricSingularity.ms_threefold_iii_of_b
#print axioms MetricSingularity.ms_threefold_iv_noninvariance

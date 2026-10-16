import ShadowEngine

/-! # Campaign 24 (`r7411+71.12`): row 59's Euler-chart field identities

The receipt builds its gradient-carrying harmonic `H4` from `Rad = ẽ e⁻¹`, the rotation taking the left-invariant
coframe `e = σ/2` to the right-invariant one `ẽ = σ̃/2`, and checks in coordinates that the field
`M = ḡ⁻¹ eᵀ H4 e` (`ḡ = eᵀ e`) has `p₁ = 0`, `p₂ = 2 − 2 sin²φ sin²θ`, `p₃ = 0`, `p₄ = p₂²/2`; and that a
superposition of two such harmonics is traceless. Here those are proved for all angles, without the chart's inverse:
`Rad · e = ẽ` pins `Rad`, and `tr Mᵏ = tr H4ᵏ` for any invertible `e`. -/

namespace ShadowProbe

section Row59Euler

open Matrix

/-- The left-invariant coframe `e = σ/2`, rows `σᵃ` in `(dψ, dθ, dφ)`. -/
noncomputable def eL (ψ θ : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![0, Real.cos ψ / 2, Real.sin ψ * Real.sin θ / 2;
    0, -Real.sin ψ / 2, Real.cos ψ * Real.sin θ / 2;
    1 / 2, 0, Real.cos θ / 2]

/-- The right-invariant coframe `ẽ = σ̃/2`. -/
noncomputable def eR (θ φ : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![Real.sin φ * Real.sin θ / 2, Real.cos φ / 2, 0;
    Real.cos φ * Real.sin θ / 2, -Real.sin φ / 2, 0;
    Real.cos θ / 2, 0, 1 / 2]

/-- `Rad`, in closed form. -/
noncomputable def Rad (ψ θ φ : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![-Real.sin φ * Real.sin ψ * Real.cos θ + Real.cos φ * Real.cos ψ,
      -Real.sin φ * Real.cos ψ * Real.cos θ - Real.sin ψ * Real.cos φ, Real.sin φ * Real.sin θ;
    -Real.sin φ * Real.cos ψ - Real.sin ψ * Real.cos φ * Real.cos θ,
      Real.sin φ * Real.sin ψ - Real.cos φ * Real.cos ψ * Real.cos θ, Real.sin θ * Real.cos φ;
    Real.sin ψ * Real.sin θ, Real.sin θ * Real.cos ψ, Real.cos θ]

/-- **`Rad` is the receipt's `ẽ e⁻¹`**: `Rad · e = ẽ` at every point, and `det e = sin θ/8`, so off the poles it is
the only such matrix. And it is a rotation: `Rad Radᵀ = 1`. -/
theorem rad_coframes (ψ θ φ : ℝ) :
    Rad ψ θ φ * eL ψ θ = eR θ φ ∧ (eL ψ θ).det = Real.sin θ / 8 ∧ Rad ψ θ φ * (Rad ψ θ φ)ᵀ = 1 := by
  have hψ := Real.sin_sq_add_cos_sq ψ
  have hθ := Real.sin_sq_add_cos_sq θ
  have hφ := Real.sin_sq_add_cos_sq φ
  refine ⟨?_, ?_, ?_⟩
  · ext i j
    fin_cases i <;> fin_cases j <;> simp [Rad, eL, eR, Matrix.mul_apply, Fin.sum_univ_three] <;>
      (first | ring1 | linear_combination (-(Real.sin θ)^2/2) * hψ + (-1/2) * hθ | linear_combination ((Real.cos φ)/2) * hψ | linear_combination (-(Real.cos θ)*(Real.sin θ)*(Real.sin φ)/2) * hψ | linear_combination ((Real.cos θ)*(Real.sin θ)*(Real.sin φ)/2) * hψ | linear_combination (-(Real.cos φ)/2) * hψ | linear_combination ((Real.sin φ)/2) * hψ | linear_combination (-(Real.cos θ)*(Real.cos φ)*(Real.sin θ)/2) * hψ | linear_combination ((Real.cos θ)*(Real.cos φ)*(Real.sin θ)/2) * hψ | linear_combination (-(Real.sin φ)/2) * hψ | linear_combination ((Real.sin θ)^2/2) * hψ + (1/2) * hθ)
  · rw [Matrix.det_fin_three]
    simp [eL]
    linear_combination (Real.sin θ / 8) * hψ
  · ext i j
    fin_cases i <;> fin_cases j <;> simp [Rad, Matrix.mul_apply, Fin.sum_univ_three] <;>
      (first | linear_combination (-(Real.sin θ)^2) * hψ + (-1) * hθ | linear_combination ((Real.cos θ)*(Real.cos φ)*(Real.sin θ)) * hψ | linear_combination ((Real.cos θ)*(Real.sin θ)*(Real.sin φ)) * hψ | linear_combination ((Real.cos θ)^2*(Real.sin φ)^2 + (Real.cos φ)^2) * hψ + ((Real.sin φ)^2) * hθ + (1) * hφ | linear_combination (-(Real.cos θ)^2*(Real.cos φ)^2 - (Real.sin φ)^2) * hψ + (-(Real.cos φ)^2) * hθ + (-1) * hφ | linear_combination (-(Real.cos θ)^2*(Real.cos φ)*(Real.sin φ) + (Real.cos φ)*(Real.sin φ)) * hψ + (-(Real.cos φ)*(Real.sin φ)) * hθ | linear_combination ((Real.sin θ)^2) * hψ + (1) * hθ | linear_combination ((Real.cos θ)^2*(Real.cos φ)*(Real.sin φ) - (Real.cos φ)*(Real.sin φ)) * hψ + ((Real.cos φ)*(Real.sin φ)) * hθ | linear_combination (-(Real.cos θ)^2*(Real.sin φ)^2 - (Real.cos φ)^2) * hψ + (-(Real.sin φ)^2) * hθ + (-1) * hφ | linear_combination ((Real.cos θ)^2*(Real.cos φ)^2 + (Real.sin φ)^2) * hψ + ((Real.cos φ)^2) * hθ + (1) * hφ | linear_combination (-(Real.cos θ)*(Real.sin θ)*(Real.sin φ)) * hψ | linear_combination (-(Real.cos θ)*(Real.cos φ)*(Real.sin θ)) * hψ)

/-- **The chart sees only the frame.** For any invertible `e`, the field `M = (eᵀe)⁻¹ eᵀ H e` has
`tr Mᵏ = tr Hᵏ`. -/
theorem chart_trace_pow (e H : Matrix (Fin 3) (Fin 3) ℝ) (he : e.det ≠ 0) (k : ℕ) :
    trace (((eᵀ * e)⁻¹ * (eᵀ * H * e)) ^ k) = trace (H ^ k) := by
  have hu : IsUnit e.det := isUnit_iff_ne_zero.2 he
  have hut : IsUnit eᵀ.det := by rw [det_transpose]; exact hu
  have hM : (eᵀ * e)⁻¹ * (eᵀ * H * e) = e⁻¹ * H * e := by
    rw [Matrix.mul_inv_rev, show e⁻¹ * eᵀ⁻¹ * (eᵀ * H * e) = e⁻¹ * (eᵀ⁻¹ * eᵀ) * H * e by
      simp only [Matrix.mul_assoc], Matrix.nonsing_inv_mul _ hut, Matrix.mul_one]
  have hp : ∀ k : ℕ, (e⁻¹ * H * e) ^ k = e⁻¹ * H ^ k * e := by
    intro k
    induction k with
    | zero => simp [Matrix.nonsing_inv_mul _ hu]
    | succ k ih =>
      rw [pow_succ, ih, pow_succ]
      calc e⁻¹ * H ^ k * e * (e⁻¹ * H * e) = e⁻¹ * H ^ k * (e * e⁻¹) * H * e := by simp only [Matrix.mul_assoc]
        _ = e⁻¹ * (H ^ k * H) * e := by rw [Matrix.mul_nonsing_inv _ hu]; simp only [Matrix.mul_one, Matrix.mul_assoc]
  rw [hM, hp, Matrix.mul_assoc, trace_mul_comm, Matrix.mul_assoc, Matrix.mul_nonsing_inv _ hu, Matrix.mul_one]

/-- The receipt's gradient-carrying harmonic, from `Rad`'s first row. -/
noncomputable def H4 (ψ θ φ : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![-Rad ψ θ φ 0 0, Rad ψ θ φ 0 1, 0; Rad ψ θ φ 0 1, Rad ψ θ φ 0 0, 0; 0, 0, 0]

/-- The second harmonic of the superposition, from `Rad`'s second row. -/
noncomputable def H4b (ψ θ φ : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![-Rad ψ θ φ 1 1, 0, Rad ψ θ φ 1 2; 0, 0, 0; Rad ψ θ φ 1 2, 0, Rad ψ θ φ 1 1]

/-- **Row 59 (B), at every point.** `p₁ = 0`, `p₂ = 2 − 2 sin²φ sin²θ` (so it genuinely varies), `p₃ = 0` and
`p₄ = p₂²/2` for `H4`; and `H4 + H4b` is traceless. -/
theorem h4_invariants (ψ θ φ : ℝ) :
    trace (H4 ψ θ φ) = 0 ∧ trace (H4 ψ θ φ ^ 2) = 2 - 2 * Real.sin φ ^ 2 * Real.sin θ ^ 2 ∧
      trace (H4 ψ θ φ ^ 3) = 0 ∧ trace (H4 ψ θ φ ^ 4) = trace (H4 ψ θ φ ^ 2) ^ 2 / 2 ∧
      trace (H4 ψ θ φ + H4b ψ θ φ) = 0 := by
  have hψ := Real.sin_sq_add_cos_sq ψ
  have hθ := Real.sin_sq_add_cos_sq θ
  have hφ := Real.sin_sq_add_cos_sq φ
  set a := Rad ψ θ φ 0 0
  set b := Rad ψ θ φ 0 1
  have hab : a ^ 2 + b ^ 2 = 1 - Real.sin φ ^ 2 * Real.sin θ ^ 2 := by
    simp only [a, b, Rad, of_apply, cons_val', cons_val_zero, cons_val_one, empty_val', cons_val_fin_one]
    linear_combination (Real.cos θ ^ 2 * Real.sin φ ^ 2 + Real.cos φ ^ 2) * hψ + Real.sin φ ^ 2 * hθ + hφ
  have t2 : trace (H4 ψ θ φ ^ 2) = 2 * (a ^ 2 + b ^ 2) := by
    simp [H4, pow_succ, trace, Fin.sum_univ_three, a, b]; ring
  refine ⟨by simp [H4, trace, Fin.sum_univ_three], by rw [t2, hab]; ring, ?_, ?_, ?_⟩
  · simp [H4, pow_succ, trace, Fin.sum_univ_three]; ring
  · rw [t2]; simp [H4, pow_succ, trace, Fin.sum_univ_three, a, b]; ring
  · simp [H4, H4b, trace, Fin.sum_univ_three]

/-- **In the receipt's coordinates.** Off the poles, `M = ḡ⁻¹ eᵀ H4 e` with `ḡ = eᵀ e` has the same four
invariants, and the superposition's `M` is traceless. -/
theorem h4_chart (ψ θ φ : ℝ) (hθ : Real.sin θ ≠ 0) :
    trace (((eL ψ θ)ᵀ * eL ψ θ)⁻¹ * ((eL ψ θ)ᵀ * H4 ψ θ φ * eL ψ θ)) = 0 ∧
      trace ((((eL ψ θ)ᵀ * eL ψ θ)⁻¹ * ((eL ψ θ)ᵀ * H4 ψ θ φ * eL ψ θ)) ^ 2)
        = 2 - 2 * Real.sin φ ^ 2 * Real.sin θ ^ 2 ∧
      trace ((((eL ψ θ)ᵀ * eL ψ θ)⁻¹ * ((eL ψ θ)ᵀ * H4 ψ θ φ * eL ψ θ)) ^ 3) = 0 ∧
      trace ((((eL ψ θ)ᵀ * eL ψ θ)⁻¹ * ((eL ψ θ)ᵀ * H4 ψ θ φ * eL ψ θ)) ^ 4)
        = trace ((((eL ψ θ)ᵀ * eL ψ θ)⁻¹ * ((eL ψ θ)ᵀ * H4 ψ θ φ * eL ψ θ)) ^ 2) ^ 2 / 2 ∧
      trace (((eL ψ θ)ᵀ * eL ψ θ)⁻¹ * ((eL ψ θ)ᵀ * (H4 ψ θ φ + H4b ψ θ φ) * eL ψ θ)) = 0 := by
  have he : (eL ψ θ).det ≠ 0 := by
    rw [(rad_coframes ψ θ φ).2.1]; intro h; exact hθ (by linarith)
  obtain ⟨p1, p2, p3, p4, ps⟩ := h4_invariants ψ θ φ
  have c := chart_trace_pow (eL ψ θ) (H4 ψ θ φ) he
  have cs := chart_trace_pow (eL ψ θ) (H4 ψ θ φ + H4b ψ θ φ) he 1
  simp only [pow_one] at cs
  refine ⟨?_, by rw [c, p2], by rw [c, p3], by rw [c, c, p4], by rw [cs, ps]⟩
  have := c 1; simp only [pow_one] at this; rw [this, p1]

/-- **Row 59 (D), the first count.** The traceless symmetric `3 × 3` matrices are spanned by the receipt's five
(`E₀₁`, `E₀₂`, `E₁₂` symmetrised, `diag(1, −1, 0)`, `diag(1, 1, −2)`), and those five are independent: dimension
`5`. -/
noncomputable def ttB : Fin 5 → Matrix (Fin 3) (Fin 3) ℝ :=
  ![!![0, 1, 0; 1, 0, 0; 0, 0, 0], !![0, 0, 1; 0, 0, 0; 1, 0, 0], !![0, 0, 0; 0, 0, 1; 0, 1, 0],
    !![1, 0, 0; 0, -1, 0; 0, 0, 0], !![1, 0, 0; 0, 1, 0; 0, 0, -2]]

theorem tt_dim_five :
    LinearIndependent ℝ ttB ∧ (∀ k, trace (ttB k) = 0 ∧ (ttB k)ᵀ = ttB k) ∧
      ∀ H : Matrix (Fin 3) (Fin 3) ℝ, Hᵀ = H → trace H = 0 →
        H = H 0 1 • ttB 0 + H 0 2 • ttB 1 + H 1 2 • ttB 2 + ((H 0 0 - H 1 1) / 2) • ttB 3
          + ((H 0 0 + H 1 1) / 2) • ttB 4 := by
  refine ⟨?_, fun k => ?_, fun H hs ht => ?_⟩
  · rw [Fintype.linearIndependent_iff]
    intro g hg i
    have e := fun a b => congrFun (congrFun hg a) b
    simp only [Fin.sum_univ_five, ttB, Matrix.add_apply, Matrix.smul_apply, Matrix.zero_apply, smul_eq_mul] at e
    have e01 := e 0 1; have e02 := e 0 2; have e12 := e 1 2; have e00 := e 0 0; have e22 := e 2 2
    simp at e01 e02 e12 e00 e22
    fin_cases i <;> simp <;> linarith
  · fin_cases k <;> refine ⟨by simp [ttB, trace, Fin.sum_univ_three]; try norm_num, ?_⟩ <;> ext i j <;> fin_cases i <;>
      fin_cases j <;> simp [ttB]
  · have s := fun a b => congrFun (congrFun hs a) b
    simp only [transpose_apply] at s
    simp only [trace, Fin.sum_univ_three, diag_apply] at ht
    ext i j
    fin_cases i <;> fin_cases j <;> simp [ttB] <;> linarith [s 0 1, s 0 2, s 1 2]

end Row59Euler

end ShadowProbe

#print axioms ShadowProbe.rad_coframes
#print axioms ShadowProbe.chart_trace_pow
#print axioms ShadowProbe.h4_invariants
#print axioms ShadowProbe.h4_chart
#print axioms ShadowProbe.tt_dim_five

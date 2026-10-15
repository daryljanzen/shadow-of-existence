import ShadowEngine

/-! # Campaign 17 (`r7371+71.5`): row 7's half, the receipt's count claims

`L174_general_matter_dynamics/I3_the_identification_is_general_and_the_shear_count_is_the_gap.py`:
- ⓶, the count: a trace-free symmetric `3 × 3` shear has FIVE independent components. The receipt counts symbols;
  `tfSym_finrank` is the dimension statement the count stands for.
- ⓷, the sign: the Hamiltonian constraint gives `ρ = R₃/2 + θ²/3 − σ²/2`, so the shear LOWERS `ρ` at fixed `R₃` and
  `θ`. `adm_rho` and `adm_rho_shear_lowers`.

Not built: the receipt's other count, that a polarized Gowdy leaf's shear is ONE function. The receipt pins that
from the paper's text and computes nothing for it. No connection enters: this row is linear algebra. -/

namespace ShadowProbe

section Row7Count

open Matrix

/-- The trace-free symmetric `3 × 3` real matrices, a subspace. -/
def tfSym : Submodule ℝ (Matrix (Fin 3) (Fin 3) ℝ) where
  carrier := {S | Sᵀ = S ∧ Matrix.trace S = 0}
  add_mem' := by
    rintro A B ⟨hA, tA⟩ ⟨hB, tB⟩
    exact ⟨by rw [transpose_add, hA, hB], by rw [trace_add, tA, tB, add_zero]⟩
  zero_mem' := ⟨transpose_zero, by simp⟩
  smul_mem' := by
    rintro c A ⟨hA, tA⟩
    exact ⟨by rw [transpose_smul, hA], by rw [trace_smul, tA, smul_zero]⟩

/-- The five free entries `(S₀₀, S₁₁, S₀₁, S₀₂, S₁₂)`. -/
def tfSymEquiv : tfSym ≃ₗ[ℝ] (Fin 5 → ℝ) where
  toFun S := ![S.1 0 0, S.1 1 1, S.1 0 1, S.1 0 2, S.1 1 2]
  map_add' A B := by ext i; fin_cases i <;> rfl
  map_smul' c A := by ext i; fin_cases i <;> rfl
  invFun v := ⟨!![v 0, v 2, v 3; v 2, v 1, v 4; v 3, v 4, -v 0 - v 1], by
    refine ⟨?_, ?_⟩
    · ext i j; fin_cases i <;> fin_cases j <;> rfl
    · simp [Matrix.trace, Fin.sum_univ_three]⟩
  left_inv S := by
    obtain ⟨S, hT, htr⟩ := S
    have hs : ∀ i j, S j i = S i j := fun i j => by rw [← Matrix.transpose_apply S j i, hT]
    have h22 : S 2 2 = -S 0 0 - S 1 1 := by
      simp [Matrix.trace, Fin.sum_univ_three] at htr; linarith
    apply Subtype.ext
    ext i j; fin_cases i <;> fin_cases j <;> simp <;> first | exact hs _ _ | linarith
  right_inv v := by ext i; fin_cases i <;> rfl

/-- **Row 7's count.** A trace-free symmetric `3 × 3` shear has exactly FIVE independent components. -/
theorem tfSym_finrank : Module.finrank ℝ tfSym = 5 := by
  rw [tfSymEquiv.finrank_eq, Module.finrank_fin_fun]

/-- **Row 7's sign.** With the Hamiltonian constraint `R₃ + K² − K_ijK^ij = 2ρ` and `K = (θ/3)·1 + σ`, `tr σ = 0`:
`ρ = R₃/2 + θ²/3 − tr(σ²)/2`. -/
theorem adm_rho (R3 θ ρ : ℝ) (S : Matrix (Fin 3) (Fin 3) ℝ) (hS : Matrix.trace S = 0)
    (hH : R3 + (Matrix.trace ((θ / 3) • (1 : Matrix (Fin 3) (Fin 3) ℝ) + S) ^ 2
      - Matrix.trace (((θ / 3) • (1 : Matrix (Fin 3) (Fin 3) ℝ) + S) ^ 2)) = 2 * ρ) :
    ρ = R3 / 2 + θ ^ 2 / 3 - Matrix.trace (S ^ 2) / 2 := by
  -- `adm_trace_split` (`Campaign6A.lean`), re-proved inline: probes do not import each other.
  simp only [Matrix.trace, Fin.sum_univ_three, Matrix.diag, sq, Matrix.mul_apply, Matrix.add_apply,
    Matrix.smul_apply, Matrix.one_apply, smul_eq_mul] at hS hH ⊢
  simp at hH
  have h22 : S 2 2 = -S 0 0 - S 1 1 := by linarith
  rw [h22] at hH ⊢; linarith

/-- For a symmetric `σ`, `tr(σ²) = Σ σᵢⱼ² ≥ 0`, zero only at `σ = 0`: the shear term is a sum of squares. -/
theorem tr_sq_sym (S : Matrix (Fin 3) (Fin 3) ℝ) (hT : Sᵀ = S) :
    Matrix.trace (S ^ 2) = ∑ i, ∑ j, S i j ^ 2 ∧ (Matrix.trace (S ^ 2) = 0 ↔ S = 0) := by
  have hs : ∀ i j, S j i = S i j := fun i j => by rw [← Matrix.transpose_apply S j i, hT]
  have e : Matrix.trace (S ^ 2) = ∑ i, ∑ j, S i j ^ 2 := by
    simp only [Matrix.trace, Matrix.diag, sq, Matrix.mul_apply]
    exact Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => by rw [hs j i]
  refine ⟨e, ?_, fun h => by rw [h]; simp⟩
  intro h0
  rw [e] at h0
  have hz := (Finset.sum_eq_zero_iff_of_nonneg (fun i _ => Finset.sum_nonneg fun j _ => sq_nonneg (S i j))).1 h0
  ext i j
  have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (S i j))).1 (hz i (Finset.mem_univ _)) j
    (Finset.mem_univ _)
  simpa using this

/-- **Row 7's sign, as a statement about `ρ`.** At fixed `R₃` and `θ`, `ρ` is strictly decreasing in `tr(σ²)`: the
shear REDUCES the energy density, and does so for every nonzero symmetric trace-free shear. -/
theorem adm_rho_shear_lowers (R3 θ : ℝ) :
    StrictAnti (fun s : ℝ => R3 / 2 + θ ^ 2 / 3 - s / 2) ∧
      ∀ S : Matrix (Fin 3) (Fin 3) ℝ, Sᵀ = S → S ≠ 0 →
        R3 / 2 + θ ^ 2 / 3 - Matrix.trace (S ^ 2) / 2 < R3 / 2 + θ ^ 2 / 3 := by
  refine ⟨fun a b h => by simp only; linarith, fun S hT h0 => ?_⟩
  obtain ⟨e, iff0⟩ := tr_sq_sym S hT
  have hnn : 0 ≤ Matrix.trace (S ^ 2) := e ▸ Finset.sum_nonneg fun i _ => Finset.sum_nonneg fun j _ => sq_nonneg _
  have hne : Matrix.trace (S ^ 2) ≠ 0 := fun h => h0 (iff0.1 h)
  have := lt_of_le_of_ne hnn (Ne.symm hne)
  linarith

end Row7Count

end ShadowProbe

#print axioms ShadowProbe.tfSym_finrank
#print axioms ShadowProbe.adm_rho
#print axioms ShadowProbe.tr_sq_sym
#print axioms ShadowProbe.adm_rho_shear_lowers

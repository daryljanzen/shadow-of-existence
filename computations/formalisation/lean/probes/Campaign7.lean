import Mathlib

/-! # Campaign 7 (`r7353+71`), piece A: row 58, the ADM kinetic scalar to `ε²`

`P10_step_three…`, gate ⓐ: for `γ = a²·exp(εH)` with `H` traceless, lapse `1` and no shift, the ADM kinetic scalar
`K_ij K^ij − K²` has `ε¹` part `0` and `ε²` part `+¼ tr(Ḣ²)`. The receipt works with `exp` truncated at
`NORD = 3`, and with that truncation as the inverse. That is reproduced exactly here, as polynomials in `ε` with
`3 × 3` matrix coefficients (`ε` is `X`, central in `Mat[X]`).
- With `h = ȧ/a`, `γ⁻¹γ̇ = E(−ε)(2hE(ε) + Ė(ε))`, and `K^i_j` is half of it.
- So the scalar is `¼[tr(M²) − (tr M)²]`. -/

open Polynomial

namespace ShadowProbe

section Row58

local notation "Mat" => Matrix (Fin 3) (Fin 3) ℝ

/-- The receipt's truncated exponential, `Σ_{k ≤ 3} (sε)ᵏHᵏ/k!`. -/
noncomputable def expT (s : ℝ) (H : Mat) : Mat[X] :=
  C 1 + C (s • H) * X + C ((s ^ 2 / 2) • H ^ 2) * X ^ 2 + C ((s ^ 3 / 6) • H ^ 3) * X ^ 3

/-- Its exact time derivative, for `H` with velocity `Hd`. -/
noncomputable def expTd (H Hd : Mat) : Mat[X] :=
  C Hd * X + C ((1 / 2 : ℝ) • (Hd * H + H * Hd)) * X ^ 2
    + C ((1 / 6 : ℝ) • (Hd * H * H + H * Hd * H + H * H * Hd)) * X ^ 3

/-- `γ⁻¹γ̇`, with the receipt's own truncated inverse. -/
noncomputable def Mgg (h : ℝ) (H Hd : Mat) : Mat[X] := expT (-1) H * (C ((2 * h) • 1) * expT 1 H + expTd H Hd)

/-- The trace, coefficientwise: `Mat[X] → ℝ[X]`. -/
noncomputable def trX (P : Mat[X]) : ℝ[X] := ∑ n ∈ P.support, monomial n (Matrix.trace (P.coeff n))

lemma trX_coeff (P : Mat[X]) (k : ℕ) : (trX P).coeff k = Matrix.trace (P.coeff k) := by
  rw [trX, finsetSum_coeff]
  simp only [coeff_monomial, Finset.sum_ite_eq', mem_support_iff]
  split_ifs with hk
  · rfl
  · rw [not_not] at hk; simp [hk]

/-- **The ADM kinetic scalar** `K^i_j K^j_i − (K^i_i)² = ¼[tr(M²) − (tr M)²]`, as a polynomial in `ε`. -/
noncomputable def kinADM (h : ℝ) (H Hd : Mat) : ℝ[X] :=
  C (1 / 4 : ℝ) * (trX (Mgg h H Hd * Mgg h H Hd) - trX (Mgg h H Hd) ^ 2)

lemma coeff_CX (a : Mat) (n k : ℕ) : (C a * X ^ n).coeff k = if k = n then a else 0 := coeff_C_mul_X_pow a n k

/-- The first three coefficients of `M`. -/
lemma Mgg_coeffs (h : ℝ) (H Hd : Mat) :
    (Mgg h H Hd).coeff 0 = (2 * h) • 1 ∧ (Mgg h H Hd).coeff 1 = Hd ∧
    (Mgg h H Hd).coeff 2 = (1 / 2 : ℝ) • (Hd * H - H * Hd) := by
  refine ⟨?_, ?_, ?_⟩
  all_goals simp only [Mgg, expT, expTd, coeff_mul, Finset.Nat.sum_antidiagonal_succ, Finset.Nat.antidiagonal_zero,
    Finset.sum_singleton, coeff_add, coeff_C_mul, coeff_C_mul_X_pow, coeff_C_mul_X, coeff_C, coeff_X_pow, coeff_X,
    coeff_one]
  all_goals norm_num
  simp only [pow_zero, one_mul, mul_add, neg_add, mul_smul_comm, smul_sub, smul_add, sq]
  module

/-- **Row 58.** The ADM kinetic scalar's `ε⁰`, `ε¹` and `ε²` coefficients are `−6h²`, `0` and `+¼ tr(Ḣ²)` for every
traceless `H` with traceless velocity `Ḣ`: the receipt's gate ⓐ, with the `ε¹` cross-term absent. -/
theorem row58_adm_kinetic (h : ℝ) (H Hd : Mat) (hHd : Matrix.trace Hd = 0) :
    (kinADM h H Hd).coeff 0 = -6 * h ^ 2 ∧ (kinADM h H Hd).coeff 1 = 0 ∧
    (kinADM h H Hd).coeff 2 = Matrix.trace (Hd * Hd) / 4 := by
  obtain ⟨m0, m1, m2⟩ := Mgg_coeffs h H Hd
  have t0 : Matrix.trace ((2 * h) • (1 : Mat)) = 6 * h := by simp [Matrix.trace_one]; ring
  have t2 : Matrix.trace ((1 / 2 : ℝ) • (Hd * H - H * Hd)) = 0 := by
    rw [Matrix.trace_smul, Matrix.trace_sub, Matrix.trace_mul_comm, sub_self, smul_zero]
  refine ⟨?_, ?_, ?_⟩
  all_goals simp only [kinADM, coeff_C_mul, coeff_sub, trX_coeff, sq, coeff_mul, Finset.Nat.sum_antidiagonal_succ,
    Finset.Nat.antidiagonal_zero, Finset.sum_singleton, m0, m1, m2, trX_coeff]
  all_goals simp only [smul_mul_assoc, mul_smul_comm, Matrix.one_mul, Matrix.mul_one, Matrix.trace_add,
    Matrix.trace_smul, smul_eq_mul, t0, t2, hHd, Matrix.trace_one, Fintype.card_fin, smul_one_mul]
  all_goals norm_num
  all_goals try ring_nf
  rw [Matrix.trace_mul_comm H Hd]; ring

end Row58

end ShadowProbe
#print axioms ShadowProbe.row58_adm_kinetic

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


/-! ### Campaign 10 (`r7353+71.12`): row 58's measure gate, `det E(ε) = 1 + O(ε³)` for traceless `H` -/

/-- The `3 × 3` determinant through traces: `2 det(1 + A) = 2 + 2tr A + (tr A)² − tr A² + 2 det A`. -/
lemma det_one_add_fin3 {R : Type*} [CommRing R] (A : Matrix (Fin 3) (Fin 3) R) :
    2 * (1 + A).det = 2 + 2 * A.trace + A.trace ^ 2 - (A * A).trace + 2 * A.det := by
  simp only [Matrix.det_fin_three, Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three,
    Matrix.add_apply, Matrix.one_apply]
  simp
  ring

/-- The receipt's truncated `exp(εH)` over `ℝ[X]`: `1 + X·B` with `B = H + (X/2)H² + (X²/6)H³`. -/
noncomputable def detBody (H : Mat) : Matrix (Fin 3) (Fin 3) ℝ[X] :=
  H.map (C : ℝ →+* ℝ[X]) + ((X : ℝ[X]) * C (1 / 2 : ℝ)) • (H * H).map (C : ℝ →+* ℝ[X])
    + ((X : ℝ[X]) ^ 2 * C (1 / 6 : ℝ)) • (H * H * H).map (C : ℝ →+* ℝ[X])

lemma detBody_eval (H : Mat) : (detBody H).map (Polynomial.eval 0) = H := by
  ext i j; simp [detBody]

lemma coeff0_trace (M : Matrix (Fin 3) (Fin 3) ℝ[X]) : M.trace.coeff 0 = (M.map (Polynomial.eval 0)).trace := by
  simp [Matrix.trace, Fin.sum_univ_three, Polynomial.coeff_zero_eq_eval_zero]

/-- **Row 58's measure gate.** For traceless `H`, the receipt's truncated `exp(εH)` has `det = 1 + O(ε³)`: the
`ε⁰`, `ε¹` and `ε²` coefficients of its determinant are `1`, `0` and `0`. -/
theorem row58_det_gate (H : Mat) (hH : Matrix.trace H = 0) :
    (1 + (X : ℝ[X]) • detBody H).det.coeff 0 = 1 ∧ (1 + (X : ℝ[X]) • detBody H).det.coeff 1 = 0 ∧
    (1 + (X : ℝ[X]) • detBody H).det.coeff 2 = 0 := by
  have key := det_one_add_fin3 ((X : ℝ[X]) • detBody H)
  set B := detBody H with hB
  have hs : ((X : ℝ[X]) • B).trace = (X : ℝ[X]) * B.trace := by simp [Matrix.trace_smul]
  have hm : ((X : ℝ[X]) • B * ((X : ℝ[X]) • B)).trace = (X : ℝ[X]) ^ 2 * (B * B).trace := by
    rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, Matrix.trace_smul, smul_eq_mul, sq]
  have hd : ((X : ℝ[X]) • B).det = (X : ℝ[X]) ^ 3 * B.det := by simp
  rw [hs, hm, hd, mul_pow, show (X : ℝ[X]) * B.trace = X ^ 1 * B.trace by ring] at key
  have t0 : B.trace.coeff 0 = 0 := by rw [coeff0_trace, hB, detBody_eval, hH]
  have t00 : (B * B).trace.coeff 0 = (H * H).trace := by
    rw [coeff0_trace, show (B * B).map (eval 0) = B.map (evalRingHom 0) * B.map (evalRingHom 0) from
      Matrix.map_mul (f := evalRingHom 0)]
    exact congrArg (fun M => (M * M).trace) (detBody_eval H)
  have tB : B.trace = C H.trace + X * C (1 / 2) * C (H * H).trace + X ^ 2 * C (1 / 6) * C (H * H * H).trace := by
    simp only [hB, detBody, Matrix.trace_fin_three, Matrix.add_apply, Matrix.smul_apply, Matrix.map_apply,
      smul_eq_mul, map_add]
    ring
  have t1 : B.trace.coeff 1 = (H * H).trace / 2 := by
    rw [tB]; simp [coeff_C, mul_assoc]; ring
  have c := fun k => congrArg (fun p : ℝ[X] => p.coeff k) key
  have c0 := c 0; have c1 := c 1; have c2 := c 2
  simp only [Polynomial.coeff_add, Polynomial.coeff_sub, Polynomial.coeff_ofNat_mul,
    Polynomial.coeff_X_pow_mul', Polynomial.coeff_ofNat_zero, Polynomial.coeff_ofNat_succ] at c0 c1 c2
  have t0' : (B.trace ^ 2).coeff 0 = 0 := by
    rw [coeff_zero_eq_eval_zero, eval_pow, ← coeff_zero_eq_eval_zero, t0, zero_pow two_ne_zero]
  norm_num [t0, t00, t1, t0'] at c0 c1 c2
  exact ⟨c0, c1, by linarith⟩

end Row58

end ShadowProbe
#print axioms ShadowProbe.row58_adm_kinetic
#print axioms ShadowProbe.row58_det_gate

import ShadowEngine

/-! # Campaign 27 (`r7437+71`): row 66's kinetic series for non-commuting modes, in both splits

The receipt (`P10_the_kinetic_cubic_vertex_is_a_split_artefact…`, sections C–D) compares two ways of writing a
perturbed spatial metric:
- the volume-preserving split `g = exp(εh)`;
- the linear split `g = 1 + εh`.

Each is a series truncated in `ε`. The kinetic scalar is `tr(u²)` with `u = g⁻¹ ġ`.

Here a series is a sequence of matrices (coefficient of `εⁿ`), and `⋆` is the truncated Cauchy product. `h = A` and
`ḣ = B` are independent matrices, so they need not commute. `ġ` is taken term by term, with `d(hᵏ) = Σᵢ hⁱ ḣ hᵏ⁻¹⁻ⁱ`
(the Leibniz rule, taken as the definition, as in the receipt's symbolic differentiation). -/

namespace ShadowProbe

section Row66Kinetic

open Matrix Finset

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The truncated Cauchy product of two matrix series. -/
noncomputable def smul66 (a b : ℕ → Matrix n n ℝ) (k : ℕ) : Matrix n n ℝ :=
  ∑ i ∈ range (k + 1), a i * b (k - i)

/-- Volume-preserving split: `g⁻¹ = exp(−εh)` and `ġ = d/dt exp(εh)`, coefficientwise. -/
noncomputable def giE (A : Matrix n n ℝ) (k : ℕ) : Matrix n n ℝ := ((k.factorial : ℝ)⁻¹) • (-A) ^ k
noncomputable def gdE (A B : Matrix n n ℝ) (k : ℕ) : Matrix n n ℝ :=
  ((k.factorial : ℝ)⁻¹) • ∑ i ∈ range k, A ^ i * B * A ^ (k - 1 - i)

/-- Linear split: `g⁻¹ = (1 + εh)⁻¹ = Σ (−εh)ᵏ` and `ġ = εḣ`. -/
noncomputable def giL (A : Matrix n n ℝ) (k : ℕ) : Matrix n n ℝ := (-A) ^ k
noncomputable def gdL (B : Matrix n n ℝ) (k : ℕ) : Matrix n n ℝ := if k = 1 then B else 0

noncomputable def uE (A B : Matrix n n ℝ) := smul66 (giE A) (gdE A B)
noncomputable def uL (A B : Matrix n n ℝ) := smul66 (giL A) (gdL B)

lemma uE_0 (A B : Matrix n n ℝ) : uE A B 0 = 0 := by simp [uE, smul66, gdE]
lemma uE_1 (A B : Matrix n n ℝ) : uE A B 1 = B := by
  simp [uE, smul66, giE, gdE, sum_range_succ]
lemma uE_2 (A B : Matrix n n ℝ) : uE A B 2 = (1 / 2 : ℝ) • (B * A - A * B) := by
  simp [uE, smul66, giE, gdE, sum_range_succ, Nat.factorial]
  module
lemma uL_0 (A B : Matrix n n ℝ) : uL A B 0 = 0 := by simp [uL, smul66, gdL]
lemma uL_1 (A B : Matrix n n ℝ) : uL A B 1 = B := by simp [uL, smul66, giL, gdL, sum_range_succ]
lemma uL_2 (A B : Matrix n n ℝ) : uL A B 2 = -(A * B) := by simp [uL, smul66, giL, gdL, sum_range_succ]

/-- **Row 66 (C), the volume-preserving split, for any `h`, `ḣ`:** the kinetic series `tr(u ⋆ u)` has order 2 equal
to `tr(ḣ²)` and ***order 3 identically zero***. The cubic term is the trace of a commutator. And `tr u` vanishes at
order 2 for any `h`, `ḣ`, and at order 1 when `ḣ` is traceless: no shear–volume cross term. -/
theorem kinetic_volume_split (A B : Matrix n n ℝ) :
    trace (smul66 (uE A B) (uE A B) 2) = trace (B * B) ∧ trace (smul66 (uE A B) (uE A B) 3) = 0 ∧
      trace (uE A B 2) = 0 ∧ (trace B = 0 → trace (uE A B 1) = 0) := by
  refine ⟨?_, ?_, ?_, fun h => by rw [uE_1, h]⟩
  · simp [smul66, sum_range_succ, uE_0, uE_1]
  · simp only [smul66, sum_range_succ, range_zero, sum_empty, zero_add, Nat.sub_self, uE_0, uE_1, uE_2,
      Nat.reduceSub, zero_mul, mul_zero, add_zero, trace_add, Matrix.mul_smul, Matrix.smul_mul, trace_smul,
      Matrix.mul_sub, Matrix.sub_mul, trace_sub]
    have h1 : (B * (B * A)).trace = (B * (A * B)).trace := by rw [trace_mul_comm, Matrix.mul_assoc]
    have h2 : (B * A * B).trace = (B * (A * B)).trace := by rw [Matrix.mul_assoc]
    have h3 : (A * B * B).trace = (B * (A * B)).trace := by
      rw [Matrix.mul_assoc, trace_mul_comm, Matrix.mul_assoc, h1]
    simp only [smul_eq_mul]
    rw [h1, h2, h3]; ring
  · rw [uE_2, trace_smul, trace_sub, trace_mul_comm, sub_self, smul_zero]

/-- **Row 66 (D), the linear split, for any `h`, `ḣ`:** order 2 is again `tr(ḣ²)`, but ***order 3 is
`−2 tr(h ḣ²)`***. (The `√det g` weight is `1 + O(ε²)` for traceless `h` and cannot reach order 3.) -/
theorem kinetic_linear_split (A B : Matrix n n ℝ) :
    trace (smul66 (uL A B) (uL A B) 2) = trace (B * B) ∧
      trace (smul66 (uL A B) (uL A B) 3) = -2 * trace (A * B * B) := by
  refine ⟨by simp [smul66, sum_range_succ, uL_0, uL_1], ?_⟩
  simp only [smul66, sum_range_succ, range_zero, sum_empty, zero_add, Nat.sub_self, uL_0, uL_1, uL_2,
    Nat.reduceSub, zero_mul, mul_zero, add_zero, trace_add, Matrix.mul_neg, Matrix.neg_mul, trace_neg]
  rw [trace_mul_comm B (A * B), Matrix.mul_assoc]
  ring

lemma uE_3 (A B : Matrix n n ℝ) :
    uE A B 3 = (1 / 6 : ℝ) • (B * A * A - (2 : ℝ) • (A * B * A) + A * A * B) := by
  simp [uE, smul66, giE, gdE, sum_range_succ, Nat.factorial, pow_succ]
  simp only [Matrix.mul_add, Matrix.mul_assoc]
  module

/-- The receipt's two non-commuting traceless modes. -/
noncomputable def M66a : Matrix (Fin 3) (Fin 3) ℝ := !![1, 0, 0; 0, -1, 0; 0, 0, 0]
noncomputable def M66b : Matrix (Fin 3) (Fin 3) ℝ := !![0, 1, 0; 1, 0, 1; 0, 1, 0]

/-- **Row 66, the two splits differ, at the receipt's modes `h = M₁`, `ḣ = M₂`:**
- the volume-preserving split's first kinetic correction is quartic: order 4 is `5/6 ≠ 0`;
- the linear split has a cubic vertex: order 3 is `2 ≠ 0`.

So the `sym(π²φ)` structure exists or does not according to the split. -/
theorem kinetic_splits_differ :
    M66a * M66b ≠ M66b * M66a ∧ trace M66a = 0 ∧ trace M66b = 0 ∧
      trace (smul66 (uE M66a M66b) (uE M66a M66b) 4) = 5 / 6 ∧
      trace (smul66 (uL M66a M66b) (uL M66a M66b) 3) = 2 := by
  refine ⟨fun h => ?_, ?_, ?_, ?_, ?_⟩
  · have := congrFun (congrFun h 0) 1
    simp [M66a, M66b, Matrix.mul_apply, Fin.sum_univ_three] at this
    norm_num at this
  · simp [M66a, Matrix.trace, Fin.sum_univ_three]
  · simp [M66b, Matrix.trace, Fin.sum_univ_three]
  · simp only [smul66, sum_range_succ, range_zero, sum_empty, zero_add, Nat.sub_self, uE_0, uE_1, uE_2, uE_3,
      Nat.reduceSub, zero_mul, mul_zero, add_zero]
    simp [M66a, M66b, Matrix.trace, Fin.sum_univ_three]
    norm_num
  · rw [(kinetic_linear_split M66a M66b).2]
    simp [M66a, M66b, Matrix.trace, Fin.sum_univ_three]

end Row66Kinetic

end ShadowProbe

#print axioms ShadowProbe.kinetic_volume_split
#print axioms ShadowProbe.kinetic_linear_split
#print axioms ShadowProbe.kinetic_splits_differ

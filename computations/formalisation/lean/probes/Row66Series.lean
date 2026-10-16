import ShadowEngine

/-! # Campaign 25 (`r7423+71`): row 66's `ε`-series of `R(exp εH)`, MTW's identity, and the split algebra

Milnor's scalar curvature of a left-invariant metric on the unit `S³` frame with eigenvalues `λ` is
`R = 2(4e₂ − e₁²)/e₃` (`milnor_scalar`, campaign 21; probes do not import each other, so here it is the
definition). It depends on `λ` only through the symmetric functions, which is the receipt's SO(3)-covariance step:
a traceless symmetric `H` may be taken diagonal, `H = diag(a, b, c)` with `a + b + c = 0`. -/

namespace ShadowProbe

section Row66Series

open Real

noncomputable def milR66 (l1 l2 l3 : ℝ) : ℝ :=
  2 * (4 * (l1 * l2 + l1 * l3 + l2 * l3) - (l1 + l2 + l3) ^ 2) / (l1 * l2 * l3)

/-- Milnor's `R` is symmetric in the eigenvalues, so it sees the frame only through the invariants. -/
lemma milR66_perm (l1 l2 l3 : ℝ) : milR66 l1 l2 l3 = milR66 l2 l1 l3 ∧ milR66 l1 l2 l3 = milR66 l1 l3 l2 := by
  constructor <;> simp only [milR66] <;> ring_nf

lemma iter_expsum66 {m : ℕ} (w c : Fin m → ℝ) (n : ℕ) :
    iteratedDeriv n (fun x => ∑ k, w k * exp (c k * x)) = fun x => ∑ k, w k * c k ^ n * exp (c k * x) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [iteratedDeriv_succ, ih]
    funext x
    refine (HasDerivAt.fun_sum (u := Finset.univ) fun k _ =>
      (((hasDerivAt_id x).const_mul (c k)).exp.const_mul (w k * c k ^ n))).deriv.trans ?_
    refine Finset.sum_congr rfl fun k _ => ?_
    simp only [id]; ring

/-- **The closed form.** With `a + b + c = 0`, `R(exp εH) = 4 Σ_{i<j} e^{ε(hᵢ+hⱼ)} − 2 Σ e^{2εhᵢ}`. -/
theorem milR66_exp (a b ε : ℝ) :
    milR66 (exp (a * ε)) (exp (b * ε)) (exp ((-a - b) * ε))
      = ∑ k : Fin 6, ![4, 4, 4, -2, -2, -2] k * exp (![a + b, a + (-a - b), b + (-a - b), 2 * a, 2 * b,
          2 * (-a - b)] k * ε) := by
  have e3 : exp (a * ε) * exp (b * ε) * exp ((-a - b) * ε) = 1 := by
    rw [← exp_add, ← exp_add]; ring_nf; exact exp_zero
  have p : ∀ x y : ℝ, exp ((x + y) * ε) = exp (x * ε) * exp (y * ε) := fun x y => by rw [← exp_add]; ring_nf
  have q : ∀ x : ℝ, exp (2 * x * ε) = exp (x * ε) ^ 2 := fun x => by rw [sq, ← exp_add]; ring_nf
  simp only [Fin.sum_univ_six, Matrix.cons_val, Matrix.cons_val_zero, Matrix.cons_val_one]
  simp only [milR66, e3, div_one, p, q]
  ring

lemma expsum66_zero {m : ℕ} (w c : Fin m → ℝ) (n : ℕ) :
    iteratedDeriv n (fun x => ∑ k, w k * exp (c k * x)) 0 = ∑ k, w k * c k ^ n := by
  rw [iter_expsum66]; simp

/-- **Row 66 (E), for every traceless `H`:** the Taylor coefficients of `R(exp εH)` at orders `0..4` are
`6, 0, −2p₂, −(10/3)p₃, −(7/6)p₄`, with `pₖ = aᵏ + bᵏ + cᵏ = tr Hᵏ`; and `(7/6)p₄ = (7/12)p₂²`, so the quartic is
the square of the quadratic. The receipt checks orders `0..3`. -/
theorem r_exp_series (a b : ℝ) :
    let c := -a - b
    let f := fun ε => milR66 (exp (a * ε)) (exp (b * ε)) (exp (c * ε))
    iteratedDeriv 0 f 0 = 6 ∧ iteratedDeriv 1 f 0 = 0 ∧
      iteratedDeriv 2 f 0 / 2 = -2 * (a ^ 2 + b ^ 2 + c ^ 2) ∧
      iteratedDeriv 3 f 0 / 6 = -(10 / 3) * (a ^ 3 + b ^ 3 + c ^ 3) ∧
      iteratedDeriv 4 f 0 / 24 = -(7 / 6) * (a ^ 4 + b ^ 4 + c ^ 4) ∧
      (7 / 6) * (a ^ 4 + b ^ 4 + c ^ 4) = (7 / 12) * (a ^ 2 + b ^ 2 + c ^ 2) ^ 2 := by
  intro c f
  have hf : f = fun x => ∑ k : Fin 6, ![4, 4, 4, -2, -2, -2] k * exp (![a + b, a + (-a - b), b + (-a - b),
      2 * a, 2 * b, 2 * (-a - b)] k * x) := funext fun ε => milR66_exp a b ε
  simp only [hf]
  simp only [expsum66_zero]
  simp only [Fin.sum_univ_six, c, Matrix.cons_val, Matrix.cons_val_zero, Matrix.cons_val_one]
  refine ⟨by norm_num, by ring, by ring, by ring, by ring, by ring⟩

/-- **Row 66 (E′), MTW exactly.** `R[exp 2β] = 6(1 − V(β₊, β₋))` with the Bianchi IX potential
`V = ⅓e^{−8β₊} − ⁴⁄₃e^{−2β₊} cosh(2√3 β₋) + 1 + ⅔e^{4β₊}(cosh(4√3 β₋) − 1)`, for all `β` (the receipt: through
cubic order). -/
theorem mtw_bianchi_ix (bp bm : ℝ) :
    milR66 (exp (2 * (bp + √3 * bm))) (exp (2 * (bp - √3 * bm))) (exp (-4 * bp))
      = 6 * (1 - (1 / 3 * exp (-8 * bp) - 4 / 3 * exp (-2 * bp) * cosh (2 * √3 * bm) + 1
        + 2 / 3 * exp (4 * bp) * (cosh (4 * √3 * bm) - 1))) := by
  set u := exp (2 * bp) with hu
  set w := exp (2 * √3 * bm) with hw
  have u0 : 0 < u := exp_pos _
  have w0 : 0 < w := exp_pos _
  have h1 : exp (2 * (bp + √3 * bm)) = u * w := by rw [hu, hw, ← exp_add]; ring_nf
  have h2 : exp (2 * (bp - √3 * bm)) = u / w := by rw [hu, hw, div_eq_mul_inv, ← exp_neg, ← exp_add]; ring_nf
  have h3 : exp (-4 * bp) = (u ^ 2)⁻¹ := by
    rw [hu, show -4 * bp = -(2 * bp + 2 * bp) by ring, exp_neg, exp_add, sq]
  have h4 : exp (-8 * bp) = (u ^ 4)⁻¹ := by
    rw [hu, show -8 * bp = -((2 * bp + 2 * bp) + (2 * bp + 2 * bp)) by ring, exp_neg, exp_add, exp_add]; ring
  have h5 : exp (-2 * bp) = u⁻¹ := by rw [hu, ← exp_neg]; ring_nf
  have h6 : exp (4 * bp) = u ^ 2 := by rw [hu, sq, ← exp_add]; ring_nf
  have h7 : cosh (2 * √3 * bm) = (w + w⁻¹) / 2 := by rw [cosh_eq, hw, ← exp_neg]
  have h8 : cosh (4 * √3 * bm) = (w ^ 2 + (w ^ 2)⁻¹) / 2 := by
    rw [cosh_eq, hw, sq, ← exp_add, ← exp_neg]; ring_nf
  rw [h1, h2, h3, h4, h5, h6, h7, h8, milR66]
  field_simp
  ring

/-- **Row 66 (D), the split algebra.** `tr(Ḃ [Ḃ, A]) = 0` for all square matrices: the trace of a commutator.
The volume-preserving split's cubic kinetic term is `tr(ḣ [ḣ, h])` up to a constant, so it vanishes identically. -/
theorem commutator_trace {n : Type*} [Fintype n] [DecidableEq n] (A B : Matrix n n ℝ) :
    Matrix.trace (B * (B * A - A * B)) = 0 := by
  rw [Matrix.mul_sub, Matrix.trace_sub, ← Matrix.mul_assoc, Matrix.trace_mul_comm (B * B) A,
    Matrix.trace_mul_comm B (A * B), Matrix.mul_assoc, sub_self]

end Row66Series

end ShadowProbe

#print axioms ShadowProbe.milR66_perm
#print axioms ShadowProbe.milR66_exp
#print axioms ShadowProbe.r_exp_series
#print axioms ShadowProbe.mtw_bianchi_ix
#print axioms ShadowProbe.commutator_trace

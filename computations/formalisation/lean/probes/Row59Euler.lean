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

/-! ### (C) The frame-constant floor -/

/-- Milnor's scalar curvature of the left-invariant metric with frame eigenvalues `λ` on the unit-`S³` frame
(`milnor_scalar`, campaign 21; probes do not import each other, so here it is the definition). -/
noncomputable def milR (l1 l2 l3 : ℝ) : ℝ := 2 * (4 * (l1 * l2 + l1 * l3 + l2 * l3) - (l1 + l2 + l3) ^ 2) / (l1 * l2 * l3)

/-- An exponential sum and its derivatives: `dⁿ/dεⁿ Σ aₖ e^{cₖε} = Σ aₖ cₖⁿ e^{cₖε}`. -/
lemma iter_expsum {m : ℕ} (a c : Fin m → ℝ) (n : ℕ) :
    iteratedDeriv n (fun x => ∑ k, a k * Real.exp (c k * x)) = fun x => ∑ k, a k * c k ^ n * Real.exp (c k * x) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [iteratedDeriv_succ, ih]
    funext x
    refine (HasDerivAt.fun_sum (u := Finset.univ) fun k _ =>
      (((hasDerivAt_id x).const_mul (c k)).exp.const_mul (a k * c k ^ n))).deriv.trans ?_
    refine Finset.sum_congr rfl fun k _ => ?_
    simp only [id]; ring

lemma expsum_at_zero {m : ℕ} (a c : Fin m → ℝ) (n : ℕ) :
    iteratedDeriv n (fun x => ∑ k, a k * Real.exp (c k * x)) 0 = ∑ k, a k * c k ^ n := by
  rw [iter_expsum]; simp

/-- **`H = diag(1, −1, 0)`:** `R(ε) = 2(1 + 2e^ε + 2e^{−ε} − e^{2ε} − e^{−2ε})`. -/
theorem floorA_closed (ε : ℝ) : milR (Real.exp ε) (Real.exp (-ε)) (Real.exp 0)
    = 2 + 4 * Real.exp ε + 4 * Real.exp (-ε) - 2 * Real.exp (2 * ε) - 2 * Real.exp (-2 * ε) := by
  have h1 : Real.exp (-ε) = (Real.exp ε)⁻¹ := Real.exp_neg ε
  have h2 : Real.exp (2 * ε) = Real.exp ε ^ 2 := by rw [← Real.exp_nat_mul]; norm_num
  have h3 : Real.exp (-2 * ε) = (Real.exp ε ^ 2)⁻¹ := by
    rw [show -2 * ε = -(2 * ε) by ring, Real.exp_neg, h2]
  have hx := Real.exp_pos ε
  rw [milR, Real.exp_zero, h1, h2, h3]
  field_simp
  ring

/-- **`H = diag(1, 1, −2)`:** `R(ε) = 2(4e^{−ε} − e^{−4ε})`. -/
theorem floorB_closed (ε : ℝ) : milR (Real.exp ε) (Real.exp ε) (Real.exp (-2 * ε))
    = 8 * Real.exp (-ε) - 2 * Real.exp (-4 * ε) := by
  have h1 : Real.exp (-ε) = (Real.exp ε)⁻¹ := Real.exp_neg ε
  have h2 : Real.exp (-2 * ε) = (Real.exp ε ^ 2)⁻¹ := by
    rw [show -2 * ε = -(2 * ε) by ring, Real.exp_neg, ← Real.exp_nat_mul]; norm_num
  have h4 : Real.exp (-4 * ε) = (Real.exp ε ^ 4)⁻¹ := by
    rw [show -4 * ε = -(4 * ε) by ring, Real.exp_neg, ← Real.exp_nat_mul]; norm_num
  have hx := Real.exp_pos ε
  rw [milR, h1, h2, h4]
  field_simp
  ring

lemma floorA_sum : (fun ε => milR (Real.exp ε) (Real.exp (-ε)) (Real.exp 0))
    = fun x => ∑ k : Fin 5, ![2, 4, 4, -2, -2] k * Real.exp (![0, 1, -1, 2, -2] k * x) := by
  funext x; rw [floorA_closed]; simp [Fin.sum_univ_five]; ring_nf

lemma floorB_sum : (fun ε => milR (Real.exp ε) (Real.exp ε) (Real.exp (-2 * ε)))
    = fun x => ∑ k : Fin 2, ![8, -2] k * Real.exp (![-1, -4] k * x) := by
  funext x; rw [floorB_closed]; simp [Fin.sum_univ_two]; ring_nf

/-- **Row 59 (C), the floor.** The Taylor coefficients `R⁽ⁿ⁾(0)/n!` at `n = 0..4` are `6, 0, −4, 0, −7/3` and
`6, 0, −12, 20, −21`; times the volume `2π²` they are the receipt's `[12, 0, −8, 0, −14/3]π²` and
`[12, 0, −24, 40, −42]π²`. They are `6 − 2p₂ε² − (10/3)p₃ε³ − (7/6)p₄ε⁴` at `(p₂, p₃, p₄) = (2, 0, 2)` and
`(6, −6, 18)`, and on both `(7/6)p₄ = (7/12)p₂²`. -/
theorem floor_taylor :
    (∀ n : Fin 5, iteratedDeriv n (fun ε => milR (Real.exp ε) (Real.exp (-ε)) (Real.exp 0)) 0 / (n : ℕ).factorial
        = ![6, 0, -4, 0, -7 / 3] n) ∧
      (∀ n : Fin 5, iteratedDeriv n (fun ε => milR (Real.exp ε) (Real.exp ε) (Real.exp (-2 * ε))) 0 / (n : ℕ).factorial
        = ![6, 0, -12, 20, -21] n) ∧
      (![6, 0, -4, 0, -7 / 3] : Fin 5 → ℝ) = ![6, 0, -2 * 2, -(10 / 3) * 0, -(7 / 6) * 2] ∧
      (![6, 0, -12, 20, -21] : Fin 5 → ℝ) = ![6, 0, -2 * 6, -(10 / 3) * (-6), -(7 / 6) * 18] ∧
      (7 / 6 : ℝ) * 2 = 7 / 12 * 2 ^ 2 ∧ (7 / 6 : ℝ) * 18 = 7 / 12 * 6 ^ 2 := by
  refine ⟨fun n => ?_, fun n => ?_, by norm_num, by norm_num, by norm_num, by norm_num⟩
  · rw [floorA_sum, expsum_at_zero]
    fin_cases n <;> simp [Fin.sum_univ_five, Nat.factorial] <;> norm_num
  · rw [floorB_sum, expsum_at_zero]
    fin_cases n <;> simp [Fin.sum_univ_two, Nat.factorial] <;> norm_num

/-! ### (D-12) The admissible one-jet -/

/-- The symmetric index pairs `(r ≤ s)`: `00, 01, 02, 11, 12, 22`. -/
def pr6 : Fin 3 → Fin 3 → Fin 6 := ![![0, 1, 2], ![1, 3, 4], ![2, 4, 5]]

/-- The constraints on a one-jet `v p (r s)`: traceless in `(r, s)` for each `p`, and divergence-free. -/
noncomputable def jetCons : (Fin 3 → Fin 6 → ℝ) →ₗ[ℝ] (Fin 6 → ℝ) where
  toFun v := ![v 0 0 + v 0 3 + v 0 5, v 1 0 + v 1 3 + v 1 5, v 2 0 + v 2 3 + v 2 5,
    ∑ p, v p (pr6 p 0), ∑ p, v p (pr6 p 1), ∑ p, v p (pr6 p 2)]
  map_add' v w := by ext i; fin_cases i <;> simp [Fin.sum_univ_three] <;> ring
  map_smul' c v := by ext i; fin_cases i <;> simp [Fin.sum_univ_three] <;> ring

lemma jetCons_surj : Function.Surjective jetCons := by
  intro w
  refine ⟨![![0, w 4, w 5, w 0, 0, 0], ![w 1, w 3, 0, 0, 0, 0], ![w 2, 0, 0, 0, 0, 0]], ?_⟩
  ext i; fin_cases i <;> simp [jetCons, pr6, Fin.sum_univ_three]

/-- **Row 59 (D), the second count.** The admissible one-jets (`18` coordinates, `6` independent constraints)
form a space of dimension `12`. -/
theorem jet_dim_twelve : Module.finrank ℝ (LinearMap.ker jetCons) = 12 := by
  have h := LinearMap.finrank_range_add_finrank_ker jetCons
  have h18 : Module.finrank ℝ (Fin 3 → Fin 6 → ℝ) = 18 := by rw [Module.finrank_pi_fintype]; simp
  rw [LinearMap.range_eq_top.2 jetCons_surj, finrank_top, h18] at h
  simp at h
  omega

end Row59Euler

end ShadowProbe

#print axioms ShadowProbe.rad_coframes
#print axioms ShadowProbe.chart_trace_pow
#print axioms ShadowProbe.h4_invariants
#print axioms ShadowProbe.h4_chart
#print axioms ShadowProbe.tt_dim_five
#print axioms ShadowProbe.floor_taylor
#print axioms ShadowProbe.jet_dim_twelve

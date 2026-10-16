import ShadowEngine
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Algebra.Polynomial.Degree.SmallDegree

/-! # Campaign 20 (`r7411+71.5`): the no-connection sweep, the 16 ORDER rows of `r7411+71.2`

Each row is built as its receipt COMPUTES AND ASSERTS it (`r7411_71_kinds/CLASSIFICATION.tsv`). No connection
enters. Floating root counts, printed tables and text pins in the receipts are not theorems, and are not here.

- G1, trig and hyperbolic identities: rows 14, 27, 30, 31, 37.
- G2, the ambient quadric: rows 39, 50, 87, 88, 90, 107.
- G3, metric coefficients: rows 25, 33, 61.
- G4, signs and a log-derivative: rows 15, 16. -/

open Filter Topology Real Polynomial

namespace ShadowProbe

section NoConnectionSweep

/-! ### G1 -/

/-- **Row 14.** The closed-FRW dust scale factor is the same cycloid: `M(1 + cos(π − η)) = (A/2)(1 − cos η)` at
`M = A/2`; and `a(η) = (A/2)(1 − cos η)` has a non-degenerate critical point at `η = 0` (`a′(0) = 0`, `a″(0) = A/2`). -/
theorem frw_cycloid (A η : ℝ) :
    A / 2 * (1 + Real.cos (π - η)) = A / 2 * (1 - Real.cos η) ∧
      deriv (fun e => A / 2 * (1 - Real.cos e)) 0 = 0 ∧
      deriv (deriv (fun e => A / 2 * (1 - Real.cos e))) 0 = A / 2 := by
  have d1 : ∀ e, HasDerivAt (fun e => A / 2 * (1 - Real.cos e)) (A / 2 * Real.sin e) e := fun e => by
    simpa using ((Real.hasDerivAt_cos e).const_sub 1).const_mul (A / 2)
  have hd : deriv (fun e => A / 2 * (1 - Real.cos e)) = fun e => A / 2 * Real.sin e := funext fun e => (d1 e).deriv
  refine ⟨by rw [Real.cos_pi_sub]; ring, by rw [(d1 0).deriv]; simp, ?_⟩
  rw [hd, ((Real.hasDerivAt_sin 0).const_mul (A / 2)).deriv]; simp

lemma cosh_half (ρ : ℝ) : 1 + Real.cosh ρ = 2 * Real.cosh (ρ / 2) ^ 2 := by
  have := Real.cosh_two_mul (ρ / 2); rw [show 2 * (ρ / 2) = ρ by ring] at this
  nlinarith [Real.cosh_sq (ρ / 2)]

lemma sinh_half (ρ : ℝ) : Real.sinh ρ = 2 * Real.sinh (ρ / 2) * Real.cosh (ρ / 2) := by
  have := Real.sinh_two_mul (ρ / 2); rwa [show 2 * (ρ / 2) = ρ by ring] at this

/-- **Row 27.** The circle continued to `z = iρ`: `cos(iρ) = cosh ρ`, `sin(iρ) = i sinh ρ`; on `r = M(1 + cosh ρ)` the
exterior coefficients are `1 − 2M/r = tanh²(ρ/2)` and `(dr/dρ)²/(1 − 2M/r) = 4M² cosh⁴(ρ/2)` (`ρ ≠ 0`); and at
`z = π + iρ` the radius is `M(1 − cosh ρ)`. -/
theorem circle_continuation (M ρ : ℝ) (hM : M ≠ 0) :
    Complex.cos (ρ * Complex.I) = Real.cosh ρ ∧ Complex.sin (ρ * Complex.I) = Real.sinh ρ * Complex.I ∧
      1 - 2 * M / (M * (1 + Real.cosh ρ)) = Real.tanh (ρ / 2) ^ 2 ∧
      (ρ ≠ 0 → (M * Real.sinh ρ) ^ 2 / (1 - 2 * M / (M * (1 + Real.cosh ρ)))
        = 4 * M ^ 2 * Real.cosh (ρ / 2) ^ 4) ∧
      M * (1 + Complex.cos (π + ρ * Complex.I)) = M * (1 - Real.cosh ρ) := by
  have hc : Real.cosh (ρ / 2) ≠ 0 := (Real.cosh_pos _).ne'
  have hcs := Real.cosh_sq_sub_sinh_sq (ρ / 2)
  have ha : 1 - 2 * M / (M * (1 + Real.cosh ρ)) = Real.tanh (ρ / 2) ^ 2 := by
    rw [cosh_half, Real.tanh_eq_sinh_div_cosh]; field_simp; linear_combination hcs
  refine ⟨by rw [Complex.cos_mul_I, ← Complex.ofReal_cosh], by rw [Complex.sin_mul_I, ← Complex.ofReal_sinh], ha,
    fun hρ => ?_, ?_⟩
  · have hs : Real.sinh (ρ / 2) ≠ 0 := by
      rw [Ne, Real.sinh_eq_zero]; intro h; exact hρ (by linarith)
    rw [ha, sinh_half, Real.tanh_eq_sinh_div_cosh]; field_simp; ring
  · rw [Complex.cos_add, Complex.cos_pi, Complex.sin_pi, Complex.cos_mul_I, ← Complex.ofReal_cosh]; ring

/-- **Row 30.** The interior in cycloid coordinates, `r = M(1 + cos η)`, `τ = M(η + sin η)`: `−(1 − 2M/r) = tan²(η/2)`,
and `g_rr r′² = (1 − 2M/r)⁻¹ (M sin η)² = −4M² cos⁴(η/2) = −τ′²`, away from `η ∈ πℤ`. At `η → 0⁺`, `g_tt → 0`. -/
theorem interior_cycloid (M η : ℝ) (hM : M ≠ 0) (hc : Real.cos (η / 2) ≠ 0) (hs : Real.sin (η / 2) ≠ 0) :
    -(1 - 2 * M / (M * (1 + Real.cos η))) = Real.tan (η / 2) ^ 2 ∧
      (1 - 2 * M / (M * (1 + Real.cos η)))⁻¹ * (M * Real.sin η) ^ 2 = -(4 * M ^ 2 * Real.cos (η / 2) ^ 4) ∧
      M * (1 + Real.cos η) = 2 * M * Real.cos (η / 2) ^ 2 := by
  have hcos : 1 + Real.cos η = 2 * Real.cos (η / 2) ^ 2 := by
    have := Real.cos_sq (η / 2); rw [show 2 * (η / 2) = η by ring] at this; linarith
  have hsin : Real.sin η = 2 * Real.sin (η / 2) * Real.cos (η / 2) := by
    have := Real.sin_two_mul (η / 2); rwa [show 2 * (η / 2) = η by ring] at this
  have hsc := Real.sin_sq_add_cos_sq (η / 2)
  have ha : -(1 - 2 * M / (M * (1 + Real.cos η))) = Real.tan (η / 2) ^ 2 := by
    rw [hcos, Real.tan_eq_sin_div_cos]; field_simp; linear_combination (-1) * hsc
  have ha' : 1 - 2 * M / (M * (1 + Real.cos η)) = -(Real.sin (η / 2) / Real.cos (η / 2)) ^ 2 := by
    rw [← Real.tan_eq_sin_div_cos, ← ha]; ring
  refine ⟨ha, ?_, by rw [hcos]; ring⟩
  rw [ha', hsin]; field_simp; ring

theorem interior_gtt_zero : Tendsto (fun η => Real.tan (η / 2) ^ 2) (𝓝[>] 0) (𝓝 0) := by
  have : ContinuousAt (fun η : ℝ => Real.tan (η / 2) ^ 2) 0 := by
    have h : ContinuousAt Real.tan ((fun η : ℝ => η / 2) 0) := Real.continuousAt_tan.2 (by simp)
    have h2 : ContinuousAt (fun η : ℝ => η / 2) 0 := (continuous_id.div_const 2).continuousAt
    exact ContinuousAt.pow (ContinuousAt.comp (g := Real.tan) (f := fun η : ℝ => η / 2) h h2) 2
  simpa using this.tendsto.mono_left nhdsWithin_le_nhds

/-- **Row 31.** `Im M(1 + cos(a + ib)) = −M sin a sinh b`, so the radius is real exactly when `sin a = 0` or `b = 0`:
the real axis and the two poles `a ∈ πℤ`. On those, `r = M(1 + cosh b)` at `a = 0` and `M(1 − cosh b)` at `a = π`;
on the real axis `r` is even and `τ = M(a + sin a)` is odd. -/
theorem three_axes (M a b : ℝ) (hM : M ≠ 0) :
    (M * (1 + Complex.cos (a + b * Complex.I))).im = -(M * Real.sin a * Real.sinh b) ∧
      ((M * (1 + Complex.cos (a + b * Complex.I))).im = 0 ↔ Real.sin a = 0 ∨ b = 0) ∧
      M * (1 + Complex.cos (0 + b * Complex.I)) = M * (1 + Real.cosh b) ∧
      M * (1 + Complex.cos (π + b * Complex.I)) = M * (1 - Real.cosh b) ∧
      M * (1 + Real.cos (-a)) = M * (1 + Real.cos a) ∧ M * (-a + Real.sin (-a)) = -(M * (a + Real.sin a)) := by
  have him : (M * (1 + Complex.cos (a + b * Complex.I))).im = -(M * Real.sin a * Real.sinh b) := by
    rw [Complex.cos_add_mul_I]
    simp [Complex.mul_im, ← Complex.ofReal_cos, ← Complex.ofReal_sin, ← Complex.ofReal_cosh,
      ← Complex.ofReal_sinh, Complex.ofReal_re, Complex.ofReal_im]
    ring
  refine ⟨him, ?_, ?_, ?_, by rw [Real.cos_neg], by rw [Real.sin_neg]; ring⟩
  · rw [him, neg_eq_zero, mul_assoc, mul_eq_zero, mul_eq_zero, Real.sinh_eq_zero]; tauto
  · rw [zero_add, Complex.cos_mul_I, ← Complex.ofReal_cosh]
  · rw [Complex.cos_add, Complex.cos_pi, Complex.sin_pi, Complex.cos_mul_I, ← Complex.ofReal_cosh]; ring

/-- **Row 37.** Through the throat: `sin(π/2 + iψ) = cosh ψ`, so the `S²` coefficient `sin²θ` continues to `cosh²ψ`
with the sign flip `i² = −1` on the line element. The join of `r₁ = sin` at `π/2` and `r₂ = cosh` at `0` is `C¹`
(values `1, 1`, slopes `0, 0`) and not `C²` (second derivatives `−1` and `+1`). -/
theorem throat_join (ψ : ℝ) :
    Complex.sin (π / 2 + ψ * Complex.I) = Real.cosh ψ ∧ Complex.I ^ 2 = -1 ∧
      Real.sin (π / 2) = Real.cosh 0 ∧ deriv Real.sin (π / 2) = deriv Real.cosh 0 ∧
      deriv (deriv Real.sin) (π / 2) = -1 ∧ deriv (deriv Real.cosh) 0 = 1 := by
  refine ⟨?_, Complex.I_sq, by simp, by simp [Real.deriv_sin, Real.deriv_cosh], ?_, ?_⟩
  · rw [Complex.sin_add, Complex.sin_pi_div_two, Complex.cos_pi_div_two, Complex.cos_mul_I,
      ← Complex.ofReal_cosh]; ring
  · rw [Real.deriv_sin, Real.deriv_cos]; simp
  · rw [Real.deriv_cosh, Real.deriv_sinh]; simp

/-! ### G2 -/

/-- **Row 39.** On the hyperboloid `−X0² + X1² + X2² = α²`: `√((4α)² − α²) = √15 α`, the point `(√15α, 4α, 0)` lies
on it, and the interval between two horn points at transverse radius `ρ`, `120°` apart, is
`s² = −(2√(ρ² − α²))² + ρ²(2 − 2 cos 120°) = 4α² − ρ²`, which vanishes at `ρ = 2α`. -/
theorem hinge_interval (α ρ : ℝ) (hα : 0 ≤ α) (hρ : α ≤ ρ) :
    Real.sqrt ((4 * α) ^ 2 - α ^ 2) = Real.sqrt 15 * α ∧
      -(Real.sqrt 15 * α) ^ 2 + (4 * α) ^ 2 + 0 ^ 2 = α ^ 2 ∧
      -(2 * Real.sqrt (ρ ^ 2 - α ^ 2)) ^ 2 + ρ ^ 2 * (2 - 2 * Real.cos (2 * π / 3)) = 4 * α ^ 2 - ρ ^ 2 ∧
      4 * α ^ 2 - (2 * α) ^ 2 = 0 := by
  have h15 : Real.sqrt 15 ^ 2 = 15 := Real.sq_sqrt (by norm_num)
  have hc : Real.cos (2 * π / 3) = -1 / 2 := by
    rw [show 2 * π / 3 = π - π / 3 by ring, Real.cos_pi_sub, Real.cos_pi_div_three]; norm_num
  have hq : Real.sqrt (ρ ^ 2 - α ^ 2) ^ 2 = ρ ^ 2 - α ^ 2 := Real.sq_sqrt (by nlinarith)
  refine ⟨?_, by nlinarith [h15], by rw [hc, mul_pow, hq]; ring, by ring⟩
  rw [show (4 * α) ^ 2 - α ^ 2 = 15 * α ^ 2 by ring, Real.sqrt_mul (by norm_num), Real.sqrt_sq hα]

/-- **Rows 87, 88, 90.** On the axis `X1 = X2 = 0` the hyperboloid `−X0² + X1² + X2² = α²` reads `X0² = −α²`: no
real point (90), and over `ℂ` exactly the two roots `±iα` (87), whose real parts are `0` and sum is `0`. The power of
a point `|X|² − α²` at `|X| = 2α, α, 0` is `3α², 0, −α²` (88), and `−(√3α)² + (2α)² = α²`. -/
theorem axis_vantage (α : ℝ) (hα : α ≠ 0) :
    (¬ ∃ X0 : ℝ, -X0 ^ 2 + 0 ^ 2 + 0 ^ 2 = α ^ 2) ∧
      (∀ z : ℂ, z ^ 2 = -(α : ℂ) ^ 2 ↔ z = Complex.I * α ∨ z = -(Complex.I * α)) ∧
      (Complex.I * α).re = 0 ∧ Complex.I * α + -(Complex.I * α) = 0 ∧
      ((2 * α) ^ 2 - α ^ 2 = 3 * α ^ 2 ∧ α ^ 2 - α ^ 2 = 0 ∧ (0 : ℝ) ^ 2 - α ^ 2 = -α ^ 2) ∧
      -(Real.sqrt 3 * α) ^ 2 + (2 * α) ^ 2 = α ^ 2 := by
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  refine ⟨fun ⟨X0, h⟩ => by nlinarith [sq_nonneg X0, sq_pos_of_ne_zero hα], fun z => ?_, by simp, by ring,
    ⟨by ring, by ring, by ring⟩, by nlinarith [h3]⟩
  have : z ^ 2 = -(α : ℂ) ^ 2 ↔ (z - Complex.I * α) * (z + Complex.I * α) = 0 := by
    constructor <;> intro h
    · ring_nf; rw [Complex.I_sq]; linear_combination h
    · ring_nf at h; rw [Complex.I_sq] at h; linear_combination h
  rw [this, mul_eq_zero, sub_eq_zero, add_eq_zero_iff_eq_neg]

/-- **Row 107.** The confocal family `x²/(a₁+λ) + y²/(a₂+λ) + z²/(a₃+λ) = 1`, cleared of denominators, is a cubic in
`λ` with leading coefficient `−1`, so degree `3`; when the `aᵢ` coincide it is `R² = a + λ`, degree `1`. -/
theorem confocal_degree (a1 a2 a3 x y z : ℝ) :
    (C (x ^ 2) * (X + C a2) * (X + C a3) + C (y ^ 2) * (X + C a1) * (X + C a3)
        + C (z ^ 2) * (X + C a1) * (X + C a2) - (X + C a1) * (X + C a2) * (X + C a3)).natDegree = 3 ∧
      (C (x ^ 2 + y ^ 2 + z ^ 2) - (X + C a1) : ℝ[X]).natDegree = 1 := by
  constructor
  · have e : C (x ^ 2) * (X + C a2) * (X + C a3) + C (y ^ 2) * (X + C a1) * (X + C a3)
        + C (z ^ 2) * (X + C a1) * (X + C a2) - (X + C a1) * (X + C a2) * (X + C a3)
        = C (-1) * X ^ 3 + C (x ^ 2 + y ^ 2 + z ^ 2 - a1 - a2 - a3) * X ^ 2
          + C (x ^ 2 * (a2 + a3) + y ^ 2 * (a1 + a3) + z ^ 2 * (a1 + a2) - (a1 * a2 + a1 * a3 + a2 * a3)) * X
          + C (x ^ 2 * a2 * a3 + y ^ 2 * a1 * a3 + z ^ 2 * a1 * a2 - a1 * a2 * a3) := by
      simp only [map_add, map_sub, map_mul, map_neg, map_one, map_pow]; ring
    rw [e, natDegree_cubic (by norm_num)]
  · have e : (C (x ^ 2 + y ^ 2 + z ^ 2) - (X + C a1) : ℝ[X]) = C (-1) * X + C (x ^ 2 + y ^ 2 + z ^ 2 - a1) := by
      simp only [map_add, map_sub, map_neg, map_one, map_pow]; ring
    rw [e, natDegree_linear (by norm_num)]

section FlatSlicing

/-- The Minkowski form on `ℝ^{4,1}`, signature `(−, +, +, +, +)`. -/
noncomputable def eta5 (a b : Fin 5 → ℝ) : ℝ := -a 0 * b 0 + a 1 * b 1 + a 2 * b 2 + a 3 * b 3 + a 4 * b 4

/-- The flat-slicing chart of the de Sitter hyperboloid `η(X, X) = α²` (row 50, `P08_synchronous_horosphere.py`). -/
noncomputable def flatX (α τ x y z : ℝ) : Fin 5 → ℝ :=
  ![α * Real.sinh (τ / α) + Real.exp (τ / α) * (x ^ 2 + y ^ 2 + z ^ 2) / (2 * α),
    α * Real.cosh (τ / α) - Real.exp (τ / α) * (x ^ 2 + y ^ 2 + z ^ 2) / (2 * α),
    Real.exp (τ / α) * x, Real.exp (τ / α) * y, Real.exp (τ / α) * z]

lemma cosh_add_sinh' (t : ℝ) : Real.cosh t + Real.sinh t = Real.exp t := by
  rw [Real.cosh_eq, Real.sinh_eq]; ring

lemma cosh_sub_sinh' (t : ℝ) : Real.cosh t - Real.sinh t = Real.exp (-t) := by
  rw [Real.cosh_eq, Real.sinh_eq]; ring

variable {α : ℝ} (hα : α ≠ 0)
include hα

/-- **Row 50 (i).** The chart lies on the hyperboloid: `η(X, X) = α²` for every `(τ, x, y, z)`. -/
theorem flat_on_quadric (τ x y z : ℝ) : eta5 (flatX α τ x y z) (flatX α τ x y z) = α ^ 2 := by
  have hE : Real.exp (τ / α) ≠ 0 := (Real.exp_pos _).ne'
  simp [eta5, flatX, Real.sinh_eq, Real.cosh_eq, Real.exp_neg]
  field_simp
  ring

/-- **Row 50 (ii).** The τ-derivative of the chart. -/
lemma flat_dtau (τ x y z : ℝ) : HasDerivAt (fun t => flatX α t x y z)
    ![Real.cosh (τ / α) + Real.exp (τ / α) * (x ^ 2 + y ^ 2 + z ^ 2) / (2 * α ^ 2),
      Real.sinh (τ / α) - Real.exp (τ / α) * (x ^ 2 + y ^ 2 + z ^ 2) / (2 * α ^ 2),
      Real.exp (τ / α) * x / α, Real.exp (τ / α) * y / α, Real.exp (τ / α) * z / α] τ := by
  have hd : HasDerivAt (fun t : ℝ => t / α) (1 / α) τ := (hasDerivAt_id τ).div_const α
  have hE := (Real.hasDerivAt_exp (τ / α)).comp τ hd
  have hS := (Real.hasDerivAt_sinh (τ / α)).comp τ hd
  have hC := (Real.hasDerivAt_cosh (τ / α)).comp τ hd
  rw [hasDerivAt_pi]
  intro i; fin_cases i
  · convert (hS.const_mul α).add (hE.mul_const ((x ^ 2 + y ^ 2 + z ^ 2) / (2 * α))) using 1
    · ext t; simp [flatX]; ring
    · simp; field_simp
  · convert (hC.const_mul α).sub (hE.mul_const ((x ^ 2 + y ^ 2 + z ^ 2) / (2 * α))) using 1
    · ext t; simp [flatX]; ring
    · simp; field_simp
  · convert hE.mul_const x using 1
    · ext t; simp [flatX]
    · simp; field_simp
  · convert hE.mul_const y using 1
    · ext t; simp [flatX]
    · simp; field_simp
  · convert hE.mul_const z using 1
    · ext t; simp [flatX]
    · simp; field_simp

/-- **Row 50 (ii).** The x-derivative of the chart (`y`, `z` are the same by symmetry of the formula). -/
lemma flat_dx (τ x y z : ℝ) : HasDerivAt (fun s => flatX α τ s y z)
    ![Real.exp (τ / α) * x / α, -(Real.exp (τ / α) * x / α), Real.exp (τ / α), 0, 0] x := by
  rw [hasDerivAt_pi]
  intro i; fin_cases i
  · convert ((((hasDerivAt_pow 2 x).add_const (y ^ 2 + z ^ 2)).const_mul (Real.exp (τ / α))).div_const
      (2 * α)).const_add (α * Real.sinh (τ / α)) using 1
    · ext s; simp [flatX]; ring
    · simp; field_simp
  · convert ((((hasDerivAt_pow 2 x).add_const (y ^ 2 + z ^ 2)).const_mul (Real.exp (τ / α))).div_const
      (2 * α)).const_sub (α * Real.cosh (τ / α)) using 1
    · ext s; simp [flatX]; ring
    · simp; field_simp
  · convert (hasDerivAt_id x).const_mul (Real.exp (τ / α)) using 1 <;> simp [flatX]
  · simpa [flatX] using hasDerivAt_const x (Real.exp (τ / α) * y)
  · simpa [flatX] using hasDerivAt_const x (Real.exp (τ / α) * z)

/-- **Row 50 (ii), the induced metric.** With the derivatives above: `g_ττ = −1`, `g_xx = e^{2τ/α}`, `g_τx = 0`. -/
theorem flat_induced (τ x y z : ℝ) :
    let Vt : Fin 5 → ℝ := ![Real.cosh (τ / α) + Real.exp (τ / α) * (x ^ 2 + y ^ 2 + z ^ 2) / (2 * α ^ 2),
      Real.sinh (τ / α) - Real.exp (τ / α) * (x ^ 2 + y ^ 2 + z ^ 2) / (2 * α ^ 2),
      Real.exp (τ / α) * x / α, Real.exp (τ / α) * y / α, Real.exp (τ / α) * z / α]
    let Vx : Fin 5 → ℝ := ![Real.exp (τ / α) * x / α, -(Real.exp (τ / α) * x / α), Real.exp (τ / α), 0, 0]
    eta5 Vt Vt = -1 ∧ eta5 Vx Vx = Real.exp (τ / α) ^ 2 ∧ eta5 Vt Vx = 0 := by
  intro Vt Vx
  have hE : Real.exp (τ / α) ≠ 0 := (Real.exp_pos _).ne'
  refine ⟨?_, ?_, ?_⟩ <;> simp [Vt, Vx, eta5, Real.sinh_eq, Real.cosh_eq, Real.exp_neg] <;> field_simp <;> ring

/-- **Row 50 (iii).** `A = (α/2, α/2, 0, 0, 0)` and `B = (−α/2, α/2, 0, 0, 0)` are null with `η(A, B) = α²/2`; the
horosphere function is `η(X, B) = (α²/2) e^{τ/α}`, independent of `x, y, z`, and it tends to `0` as `τ → −∞`. -/
theorem flat_horosphere (x y z : ℝ) :
    let A : Fin 5 → ℝ := ![α / 2, α / 2, 0, 0, 0]
    let B : Fin 5 → ℝ := ![-(α / 2), α / 2, 0, 0, 0]
    eta5 A A = 0 ∧ eta5 B B = 0 ∧ eta5 A B = α ^ 2 / 2 ∧
      (∀ τ, eta5 (flatX α τ x y z) B = α ^ 2 / 2 * Real.exp (τ / α)) ∧
      (0 < α → Tendsto (fun τ => eta5 (flatX α τ x y z) B) atBot (𝓝 0)) := by
  intro A B
  have key : ∀ τ, eta5 (flatX α τ x y z) B = α ^ 2 / 2 * Real.exp (τ / α) := fun τ => by
    have hE : Real.exp (τ / α) ≠ 0 := (Real.exp_pos _).ne'
    simp [eta5, flatX, B, Real.sinh_eq, Real.cosh_eq, Real.exp_neg]; field_simp; ring
  refine ⟨by simp [eta5, A], by simp [eta5, B], by simp [eta5, A, B]; ring, key, fun hpos => ?_⟩
  simp only [key]
  have : Tendsto (fun τ : ℝ => τ / α) atBot atBot := tendsto_id.atBot_div_const hpos
  simpa using (Real.tendsto_exp_atBot.comp this).const_mul (α ^ 2 / 2)

end FlatSlicing

/-! ### G3 and G4 -/

/-! ### G4: signs and a log-derivative -/

/-- **Row 15.** The LTB turnaround radius `R_max = −m/E` is positive for a bound shell (`E < 0`) and negative for an
unbound one; and the bound cycloid `(m/(−2E))(1 − cos η)` is the circle's `M(1 + cos(π − η))` at `M = m/(−2E)`. -/
theorem ltb_turnaround (m E η : ℝ) (hm : 0 < m) :
    (E < 0 → 0 < -m / E) ∧ (0 < E → -m / E < 0) ∧
      m / (-2 * E) * (1 - Real.cos η) = m / (-2 * E) * (1 + Real.cos (π - η)) := by
  refine ⟨fun hE => div_pos_of_neg_of_neg (by linarith) hE, fun hE => div_neg_of_neg_of_pos (by linarith) hE, ?_⟩
  rw [Real.cos_pi_sub]; ring

/-- **Row 16.** The turnaround time `t_ta = πm/(2E)^{3/2}` (`E > 0` the binding energy) has logarithmic derivative
`−3/2` in `E`: `E · d/dE log t_ta = −3/2`. -/
theorem ltb_turnaround_time (m E : ℝ) (hm : 0 < m) (hE : 0 < E) :
    HasDerivAt (fun e => Real.log (π * m / (2 * e) ^ (3 / 2 : ℝ))) (-(3 / 2) / E) E := by
  have h2 : 0 < 2 * E := by positivity
  have hl : HasDerivAt (fun e => Real.log (π * m) - (3 / 2 : ℝ) * Real.log (2 * e)) (-(3 / 2) / E) E := by
    have := ((((hasDerivAt_id E).const_mul 2).log (by simpa using h2.ne')).const_mul (3 / 2 : ℝ)).const_sub
      (Real.log (π * m))
    simp only [id] at this
    convert this using 1; field_simp
  refine hl.congr_of_eventuallyEq ?_
  filter_upwards [lt_mem_nhds hE] with e he
  have : 0 < 2 * e := by positivity
  rw [Real.log_div (by positivity) (Real.rpow_pos_of_pos this _).ne', Real.log_rpow this]

/-! ### G3: metric-coefficient algebra -/

/-- **Row 25.** For any lapse `f ≠ 0`, the Eddington–Finkelstein substitution `dt = dv − dr/f` turns
`−f dt² + dr²/f` into `−f dv² + 2 dv dr`; and with `s² = 1 − f`, the Painlevé–Gullstrand one, `dt = dT − (s/f) dr`,
gives `−f dT² + 2s dT dr + dr²`. For Schwarzschild, `f = 1 − r_h/r` and `s = √(r_h/r)`, which `schw_pg_shift`
checks; the Killing norm `−f` vanishes at `r = r_h`. -/
theorem schw_charts (f s dv dr dT : ℝ) (hf : f ≠ 0) (hs : s ^ 2 = 1 - f) :
    -f * (dv - dr / f) ^ 2 + dr ^ 2 / f = -f * dv ^ 2 + 2 * dv * dr ∧
      -f * (dT - s / f * dr) ^ 2 + dr ^ 2 / f = -f * dT ^ 2 + 2 * s * dT * dr + dr ^ 2 := by
  refine ⟨by field_simp; ring, ?_⟩
  field_simp
  linear_combination (-(dr ^ 2)) * hs

theorem schw_pg_shift (rh r : ℝ) (hr : 0 < r) (hrh : 0 ≤ rh) :
    Real.sqrt (rh / r) ^ 2 = 1 - (1 - rh / r) ∧ (rh ≠ 0 → 1 - rh / rh = 0) := by
  refine ⟨by rw [Real.sq_sqrt (div_nonneg hrh hr.le)]; ring, fun h => by field_simp; ring⟩

/-- The RNdS lapse `f = 1 − 2M/r + Q²/r² − r²/α²`. -/
noncomputable def fRN (M Q α r : ℝ) : ℝ := 1 - 2 * M / r + Q ^ 2 / r ^ 2 - r ^ 2 / α ^ 2

/-- **Row 33.** Under `M ↦ −M` the lapse splits into an even part `1 − r²/α² + Q²/r²` and an odd part `−2M/r`; it is
even in `Q`; and `r² f = r² − 2Mr + Q² − r⁴/α²`. With `Q ≠ 0`, `f → +∞` as `r → 0⁺`; with `Q = 0` and `M > 0`, `f → −∞`. -/
theorem rnds_parity (M Q α r : ℝ) (hr : r ≠ 0) (hα : α ≠ 0) :
    (fRN M Q α r + fRN (-M) Q α r) / 2 = 1 - r ^ 2 / α ^ 2 + Q ^ 2 / r ^ 2 ∧
      (fRN M Q α r - fRN (-M) Q α r) / 2 = -2 * M / r ∧ fRN M (-Q) α r = fRN M Q α r ∧
      r ^ 2 * fRN M Q α r = r ^ 2 - 2 * M * r + Q ^ 2 - r ^ 4 / α ^ 2 := by
  refine ⟨by simp only [fRN]; ring, by simp only [fRN]; ring, by simp only [fRN]; ring, ?_⟩
  simp only [fRN]; field_simp

theorem rnds_core (M Q α : ℝ) (hQ : Q ≠ 0) :
    Tendsto (fRN M Q α) (𝓝[>] 0) atTop := by
  have e : ∀ r, r ≠ 0 → fRN M Q α r = (Q ^ 2 - 2 * M * r + r ^ 2 - r ^ 4 / α ^ 2) * (r ^ 2)⁻¹ := fun r hr => by
    simp only [fRN]; field_simp; ring
  have hnum : Tendsto (fun r : ℝ => Q ^ 2 - 2 * M * r + r ^ 2 - r ^ 4 / α ^ 2) (𝓝[>] 0) (𝓝 (Q ^ 2)) := by
    have : Continuous (fun r : ℝ => Q ^ 2 - 2 * M * r + r ^ 2 - r ^ 4 / α ^ 2) := by fun_prop
    simpa using (this.tendsto 0).mono_left nhdsWithin_le_nhds
  have hden : Tendsto (fun r : ℝ => (r ^ 2)⁻¹) (𝓝[>] 0) atTop := by
    have h1 : Tendsto (fun r : ℝ => r ^ 2) (𝓝[>] 0) (𝓝[>] 0) := by
      refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
      · simpa using ((continuous_pow 2).tendsto (0 : ℝ)).mono_left nhdsWithin_le_nhds
      · exact eventually_nhdsWithin_of_forall fun r (hr : 0 < r) => show (0 : ℝ) < r ^ 2 by positivity
    exact tendsto_inv_nhdsGT_zero.comp h1
  have := hnum.pos_mul_atTop (lt_of_le_of_ne (sq_nonneg Q) (Ne.symm (pow_ne_zero 2 hQ))) hden
  refine this.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with r (hr : 0 < r)
  exact (e r hr.ne').symm

theorem schw_core_minus (M α : ℝ) (hM : 0 < M) :
    Tendsto (fRN M 0 α) (𝓝[>] 0) atBot := by
  have e : ∀ r, r ≠ 0 → fRN M 0 α r = (r - 2 * M - r ^ 3 / α ^ 2) * r⁻¹ := fun r hr => by
    simp only [fRN]; field_simp; ring
  have hnum : Tendsto (fun r : ℝ => r - 2 * M - r ^ 3 / α ^ 2) (𝓝[>] 0) (𝓝 (-(2 * M))) := by
    have : Continuous (fun r : ℝ => r - 2 * M - r ^ 3 / α ^ 2) := by fun_prop
    simpa using (this.tendsto 0).mono_left nhdsWithin_le_nhds
  have := hnum.neg_mul_atTop (by linarith) tendsto_inv_nhdsGT_zero
  refine this.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with r (hr : 0 < r)
  exact (e r hr.ne').symm

/-- **Row 61.** Schwarzschild in ingoing Eddington–Finkelstein coordinates `(v, r, θ, φ)`: `det g = −r⁴ sin²θ`,
nonzero at the horizon `r = 2M` off the poles. -/
theorem ef_det (M r θ : ℝ) :
    Matrix.det !![-(1 - 2 * M / r), 1, 0, 0; 1, 0, 0, 0; 0, 0, r ^ 2, 0; 0, 0, 0, r ^ 2 * Real.sin θ ^ 2]
      = -(r ^ 4 * Real.sin θ ^ 2) := by
  rw [Matrix.det_succ_row_zero]
  simp only [Fin.sum_univ_four]
  simp [Matrix.det_fin_three, Matrix.submatrix, Fin.succAbove]
  ring

/-- **Row 61.** The horizon's induced metric in `(v, θ, φ)` is `diag(0, r_h², r_h² sin²θ)`: determinant `0`, and it
kills `∂_v`, the null generator. -/
theorem ef_horizon_degenerate (M θ : ℝ) :
    (Matrix.diagonal ![(0 : ℝ), (2 * M) ^ 2, (2 * M) ^ 2 * Real.sin θ ^ 2]).det = 0 ∧
      (Matrix.diagonal ![(0 : ℝ), (2 * M) ^ 2, (2 * M) ^ 2 * Real.sin θ ^ 2]).mulVec ![1, 0, 0] = 0 := by
  refine ⟨by simp [Matrix.det_diagonal, Fin.prod_univ_three], ?_⟩
  ext i; fin_cases i <;> simp [Matrix.mulVec_diagonal]

/-- **Row 61.** Off the poles and at `M ≠ 0` it has rank `2`. -/
theorem ef_horizon_rank (M θ : ℝ) (hM : M ≠ 0) (hs : Real.sin θ ≠ 0) :
    (Matrix.diagonal ![(0 : ℝ), (2 * M) ^ 2, (2 * M) ^ 2 * Real.sin θ ^ 2]).rank = 2 := by
  rw [Matrix.rank_diagonal, Fintype.card_subtype]
  have : (Finset.univ.filter fun i : Fin 3 => ![(0 : ℝ), (2 * M) ^ 2, (2 * M) ^ 2 * Real.sin θ ^ 2] i ≠ 0)
      = {1, 2} := by
    ext i; fin_cases i <;> simp [hM, hs]
  rw [this]; rfl

end NoConnectionSweep

end ShadowProbe

#print axioms ShadowProbe.frw_cycloid
#print axioms ShadowProbe.circle_continuation
#print axioms ShadowProbe.interior_cycloid
#print axioms ShadowProbe.interior_gtt_zero
#print axioms ShadowProbe.three_axes
#print axioms ShadowProbe.throat_join
#print axioms ShadowProbe.hinge_interval
#print axioms ShadowProbe.axis_vantage
#print axioms ShadowProbe.confocal_degree
#print axioms ShadowProbe.flat_on_quadric
#print axioms ShadowProbe.flat_dtau
#print axioms ShadowProbe.flat_dx
#print axioms ShadowProbe.flat_induced
#print axioms ShadowProbe.flat_horosphere
#print axioms ShadowProbe.ltb_turnaround
#print axioms ShadowProbe.ltb_turnaround_time
#print axioms ShadowProbe.schw_charts
#print axioms ShadowProbe.schw_pg_shift
#print axioms ShadowProbe.rnds_parity
#print axioms ShadowProbe.rnds_core
#print axioms ShadowProbe.schw_core_minus
#print axioms ShadowProbe.ef_det
#print axioms ShadowProbe.ef_horizon_degenerate
#print axioms ShadowProbe.ef_horizon_rank

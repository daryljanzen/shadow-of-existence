import ShadowEngine
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.NumberTheory.LSeries.RiemannZeta

/-! # Campaign 21 (`r7411+71.7`): the `S³` frame core of rows 65, 66, 67

What their receipts (`receipts/P10_canonical_time/`) compute in the su(2) frame of the unit `S³` and over the Euler
box, built once. No manifold structure on `S³` is used: the frame geometry is the Koszul formula on the structure
constants `[E_a, E_b] = 2ε_abc E_c`, which is what the receipts' own Levi-Civita contractions use.
- `milnor_scalar`: `R(diag λ) = 2(4e₂ − e₁²)/e₃` for every left-invariant diagonal metric (rows 65, 66);
- `s3_ricci`: `Ric = 2δ`, `R = 6`; `s3_tt_eigen`: `−∇²h = 6h` for every frame-constant TT `h` (rows 66, 67);
- `const_curv_tt`: `R_ikjl h^kl = −K h_ij`, `Ric = 2K`, `R = 6K` (row 65);
- `traceless_cube`, `det_frame_conj`: `tr h³ = 3 det h`, `det(e⁻¹He) = det H` (rows 66, 67);
- `euler_volume`: `2π²` (rows 66, 67); `zeta_count`: `ζ(0) = 10` (row 65); `halfline_integral`, `tt_mode_eom` (rows 66, 65).

Not built: the Euler-chart coordinate checks (they need a non-diagonal `Fin 3` instance), the `ε`-series of
`R(exp εH)`, and the TT spectrum itself, which every receipt imports. -/

open Filter Topology Real MeasureTheory

namespace ShadowProbe

section S3Frame

/-- The Levi-Civita symbol on `Fin 3`. -/
def eps3 (a b c : Fin 3) : ℝ :=
  if (a, b, c) = (0, 1, 2) ∨ (a, b, c) = (1, 2, 0) ∨ (a, b, c) = (2, 0, 1) then 1
  else if (a, b, c) = (0, 2, 1) ∨ (a, b, c) = (2, 1, 0) ∨ (a, b, c) = (1, 0, 2) then -1 else 0

/-- su(2) in the left-invariant frame of the unit `S³`: `[E_a, E_b] = 2 ε_abc E_c`. -/
def strC (a b c : Fin 3) : ℝ := 2 * eps3 a b c

/-- The Koszul formula for a left-invariant metric `diag λ`: `Γ_abc = g(∇_{E_a}E_b, E_c)`. -/
noncomputable def kosL (l : Fin 3 → ℝ) (a b c : Fin 3) : ℝ :=
  (strC a b c * l c - strC b c a * l a + strC c a b * l b) / 2

/-- `∇_{E_a}E_b = Σ_d kosU a b d E_d`. -/
noncomputable def kosU (l : Fin 3 → ℝ) (a b d : Fin 3) : ℝ := kosL l a b d / l d

/-- `g(R(E_a, E_b)E_c, E_d)` for the frame connection (frame-constant components). -/
noncomputable def riemF (l : Fin 3 → ℝ) (a b c d : Fin 3) : ℝ :=
  ∑ e, (kosU l b c e * kosL l a e d - kosU l a c e * kosL l b e d) - ∑ f, strC a b f * kosL l f c d

/-- The scalar curvature `Σ_{ab} R_abba / (λ_a λ_b)`. -/
noncomputable def scalF (l : Fin 3 → ℝ) : ℝ := ∑ a, ∑ b, riemF l a b b a / (l a * l b)

/-- **Piece 3, the Milnor formula.** A left-invariant metric `diag(λ₀, λ₁, λ₂)` on `SU(2) = S³` has scalar curvature
`R = 2(4e₂ − e₁²)/e₃`, with `e₁, e₂, e₃` the elementary symmetric functions of the `λᵢ`. -/
theorem milnor_scalar (l : Fin 3 → ℝ) (h0 : l 0 ≠ 0) (h1 : l 1 ≠ 0) (h2 : l 2 ≠ 0) :
    scalF l = 2 * (4 * (l 0 * l 1 + l 0 * l 2 + l 1 * l 2) - (l 0 + l 1 + l 2) ^ 2) / (l 0 * l 1 * l 2) := by
  simp only [scalF, riemF, kosU, kosL, strC, eps3, Fin.sum_univ_three]
  simp
  field_simp
  ring

/-- At `λ = 1` the Koszul connection is the Levi-Civita symbol: `∇_{E_a}E_b = ε_abc E_c`. -/
lemma kos_unit (a b c : Fin 3) : kosU (fun _ => 1) a b c = eps3 a b c := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [kosU, kosL, strC, eps3]

/-- **Piece 2.** The unit `S³`: `Ric = 2δ` and `R = 6`. -/
theorem s3_ricci (b c : Fin 3) :
    ∑ a, riemF (fun _ => 1) a b c a = (if b = c then 2 else 0) ∧ scalF (fun _ => 1) = 6 := by
  constructor
  · fin_cases b <;> fin_cases c <;> simp [riemF, kosU, kosL, strC, eps3, Fin.sum_univ_three] <;> norm_num
  · rw [milnor_scalar] <;> norm_num

/-- `∇_a` of a frame-constant 2-tensor on the unit `S³`. -/
noncomputable def nabF (a : Fin 3) (T : Fin 3 → Fin 3 → ℝ) (b c : Fin 3) : ℝ :=
  -(∑ d, eps3 a b d * T d c) - ∑ d, eps3 a c d * T b d

/-- **Piece 1.** For every frame-constant symmetric traceless `h` on the unit `S³`, `−∇²h = 6h`: the lowest TT level's
eigenvalue, from the structure constants alone. -/
theorem s3_tt_eigen (h : Fin 3 → Fin 3 → ℝ) (hs : ∀ i j, h i j = h j i) (ht : h 0 0 + h 1 1 + h 2 2 = 0)
    (b c : Fin 3) : -(∑ a, nabF a (nabF a h) b c) = 6 * h b c := by
  have s01 := hs 0 1; have s02 := hs 0 2; have s12 := hs 1 2
  fin_cases b <;> fin_cases c <;> simp [nabF, eps3, Fin.sum_univ_three] <;> linarith

/-- **Piece 4.** Constant curvature `K` in three dimensions, `R_ikjl = K(δ_ij δ_kl − δ_il δ_kj)`: on a symmetric
traceless `h`, `R_ikjl h^kl = −K h_ij`; `Ric = 2Kδ`; `R = 6K`. -/
theorem const_curv_tt (K : ℝ) (h : Fin 3 → Fin 3 → ℝ) (hs : ∀ i j, h i j = h j i)
    (ht : h 0 0 + h 1 1 + h 2 2 = 0) :
    let Rc : Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℝ := fun i k j l =>
      K * ((if i = j then 1 else 0) * (if k = l then 1 else 0) - (if i = l then 1 else 0) * (if k = j then 1 else 0))
    (∀ i j, ∑ k, ∑ l, Rc i k j l * h k l = -K * h i j) ∧
      (∀ i j, ∑ k, Rc k i k j = 2 * K * if i = j then 1 else 0) ∧ ∑ i, ∑ k, Rc k i k i = 6 * K := by
  intro Rc
  refine ⟨fun i j => ?_, fun i j => ?_, ?_⟩
  · have s01 := hs 0 1; have s02 := hs 0 2; have s12 := hs 1 2
    fin_cases i <;> fin_cases j <;> simp [Rc, Fin.sum_univ_three] <;>
      first
      | linear_combination K * ht
      | exact Or.inl s01 | exact Or.inl s01.symm | exact Or.inl s02 | exact Or.inl s02.symm
      | exact Or.inl s12 | exact Or.inl s12.symm
  · fin_cases i <;> fin_cases j <;> simp [Rc, Fin.sum_univ_three] <;> ring
  · simp [Rc, Fin.sum_univ_three]; ring

/-- **Piece 5.** A traceless `3 × 3` matrix has `tr h³ = 3 det h` (Cayley–Hamilton with `tr h = 0`). -/
theorem traceless_cube (h : Matrix (Fin 3) (Fin 3) ℝ) (ht : Matrix.trace h = 0) :
    Matrix.trace (h ^ 3) = 3 * h.det := by
  simp only [Matrix.trace, Matrix.diag, Fin.sum_univ_three] at ht ⊢
  simp [pow_succ, Matrix.mul_apply, Fin.sum_univ_three, Matrix.det_fin_three]
  have : h 2 2 = -h 0 0 - h 1 1 := by linarith
  rw [this]; ring

/-- **Piece 6.** `det(e⁻¹He) = det H` for an invertible frame matrix `e`. -/
theorem det_frame_conj (e H : Matrix (Fin 3) (Fin 3) ℝ) (he : IsUnit e.det) : (e⁻¹ * H * e).det = H.det := by
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_nonsing_inv, mul_comm, ← mul_assoc,
    Ring.mul_inverse_cancel _ he, one_mul]

/-- **Piece 7.** The volume of the unit `S³` in Euler angles: `∫₀^{2π} ∫₀^π ∫₀^{4π} sinθ/8 dφ dθ dψ = 2π²`. -/
theorem euler_volume :
    ∫ _ψ in (0 : ℝ)..2 * π, ∫ θ in (0 : ℝ)..π, ∫ _φ in (0 : ℝ)..4 * π, Real.sin θ / 8 = 2 * π ^ 2 := by
  simp only [intervalIntegral.integral_const, smul_eq_mul, sub_zero]
  rw [intervalIntegral.integral_const_mul, intervalIntegral.integral_div, integral_sin]
  simp; ring

/-- **Piece 8.** `ζ(0) = 2[(ζ_R(−2) − 5) − 4(ζ_R(0) − 2)] = 10`, from `ζ_R(0) = −1/2` and `ζ_R(−2) = 0`. -/
theorem zeta_count : 2 * ((riemannZeta (-2) - 5) - 4 * (riemannZeta 0 - 2)) = 10 := by
  have h2 : riemannZeta (-2) = 0 := by
    have := riemannZeta_neg_two_mul_nat_add_one 0; norm_num at this; exact this
  rw [h2, riemannZeta_zero]; norm_num

/-- **Piece 9.** `∫₁^∞ q^{−4/3} dq = 3`. -/
theorem halfline_integral : ∫ q in Set.Ioi (1 : ℝ), q ^ (-(4 / 3) : ℝ) = 3 := by
  rw [integral_Ioi_rpow_of_lt (by norm_num) one_pos]; norm_num

/-- **Piece 9.** The Euler–Lagrange equation of `L₂ = a³φ′²/2 − 4aφ²`: `(a³φ′)′ + 8aφ = 0` is
`a³(φ″ + 3Hφ′ + 8φ/a²) = 0`, with `H = a′/a`. -/
theorem tt_mode_eom {a φ : ℝ → ℝ} {T a' φ' φ'' : ℝ} (ha : HasDerivAt a a' T) (hφ' : HasDerivAt (deriv φ) φ'' T)
    (hφ : deriv φ T = φ') (h0 : a T ≠ 0) :
    HasDerivAt (fun t => a t ^ 3 * deriv φ t) (a T ^ 3 * (φ'' + 3 * (a' / a T) * φ' + 8 * φ T / a T ^ 2)
      - 8 * a T * φ T) T := by
  have := (ha.pow 3).mul hφ'
  convert this using 1
  rw [hφ]; simp only [Pi.pow_apply]; field_simp; ring

end S3Frame

end ShadowProbe

#print axioms ShadowProbe.milnor_scalar
#print axioms ShadowProbe.kos_unit
#print axioms ShadowProbe.s3_ricci
#print axioms ShadowProbe.s3_tt_eigen
#print axioms ShadowProbe.const_curv_tt
#print axioms ShadowProbe.traceless_cube
#print axioms ShadowProbe.det_frame_conj
#print axioms ShadowProbe.euler_volume
#print axioms ShadowProbe.zeta_count
#print axioms ShadowProbe.halfline_integral
#print axioms ShadowProbe.tt_mode_eom

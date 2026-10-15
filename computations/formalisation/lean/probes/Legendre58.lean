import Mathlib

/-! # Campaign 11 (`r7353+71.14`): row 58's last half, the Legendre transform and the sign

`P10_step_three…`, sections B and C. The ADM action `(1/2κ)∫√γ N[R³ + K_ijK^ij − K²]` with `N = 1`, no shift and
`γ = a²E(ε)` has the kinetic form `+¼tr Ḣ²` at `ε²` (`row58_adm_kinetic`) and measure `a³` (`row58_det_gate`).
- (1) The Legendre transform of `(α/2)v² + W` is `p²/(2α) − W`, as a SUPREMUM, which is where `α > 0` is used. So the
  potential enters the Hamiltonian with the opposite sign to its Lagrangian partner.
- (2) The per-mode Lagrangian `(a³/8κ)φ̇² − σ(a/2κ)(μ²/4)φ²` has Euler–Lagrange equation
  `φ̈ + 3(ȧ/a)φ̇ + σ(μ²/a²)φ = 0`.
- (3) `σ = +1` (the derived minus) gives `ω² = μ²/a² > 0` at every level `m ≥ 2`, and `σ = −1` gives `ω² < 0`.
- (4) `det(a²M) = a⁶ det M`, so the measure is `a³` where `det E = 1`.

*Input, not derived here:* the per-mode coefficient `−μ²/4`, `μ² = m² − 1`, is `r7034`'s level sum over the
degeneracy, which the receipt also uses without re-deriving. -/

namespace ShadowProbe

section Row58Legendre

/-- **(1) The Legendre transform** of a positive quadratic kinetic term plus a velocity-independent `W`:
`sup_v (p v − (α/2)v² − W) = p²/(2α) − W`, attained at `v = p/α`. -/
theorem row58_legendre (α W p : ℝ) (hα : 0 < α) :
    IsGreatest (Set.range fun v : ℝ => p * v - (α / 2 * v ^ 2 + W)) (p ^ 2 / (2 * α) - W) := by
  refine ⟨⟨p / α, by field_simp; ring⟩, ?_⟩
  rintro _ ⟨v, rfl⟩
  have h : p ^ 2 / (2 * α) - W - (p * v - (α / 2 * v ^ 2 + W)) = (α * v - p) ^ 2 / (2 * α) := by
    field_simp; ring
  have : 0 ≤ (α * v - p) ^ 2 / (2 * α) := by positivity
  linarith

/-- The Hamiltonian is that supremum. -/
theorem row58_hamiltonian (α W p : ℝ) (hα : 0 < α) :
    sSup (Set.range fun v : ℝ => p * v - (α / 2 * v ^ 2 + W)) = p ^ 2 / (2 * α) - W :=
  (row58_legendre α W p hα).csSup_eq

/-- Without `α > 0` there is no transform: for `α < 0` the expression is unbounded above. -/
theorem row58_legendre_needs_sign (α W p : ℝ) (hα : α < 0) :
    ¬ BddAbove (Set.range fun v : ℝ => p * v - (α / 2 * v ^ 2 + W)) := by
  rintro ⟨M, hM⟩
  set β := -α / 2 with hβ
  have hβ0 : 0 < β := by rw [hβ]; linarith
  set c := |p| + |M| + |W| + 1
  set v := c / β + 1
  have hv1 : 1 ≤ v := by have : 0 ≤ c / β := by positivity
                         linarith
  have hβv : c ≤ β * v := by
    have : β * (c / β) = c := by field_simp
    nlinarith
  have hv : M < p * v - (α / 2 * v ^ 2 + W) := by
    have e : p * v - (α / 2 * v ^ 2 + W) = β * v * v + p * v - W := by rw [hβ]; ring
    have h1 : c * v ≤ β * v * v := by nlinarith
    have h4 : |M| + |W| + 1 ≤ (|M| + |W| + 1) * v := by nlinarith [abs_nonneg M, abs_nonneg W]
    have h5 : c * v = |p| * v + (|M| + |W| + 1) * v := by simp only [c]; ring
    have h3 : -(|p| * v) ≤ p * v := by nlinarith [neg_abs_le p]
    rw [e]; linarith [le_abs_self M, le_abs_self W]
  exact absurd (hM ⟨v, rfl⟩) (not_le.mpr hv)

/-- The per-mode Lagrangian, `L(x, v) = (A³/8κ)v² − σ(A/2κ)(μ²/4)x²` at scale factor `A`. -/
noncomputable def Lper (κ σ μ2 A x v : ℝ) : ℝ := A ^ 3 / (8 * κ) * v ^ 2 - σ * (A / (2 * κ)) * (μ2 / 4) * x ^ 2

/-- `∂L/∂v`, the momentum. -/
lemma Lper_dv (κ σ μ2 A x v : ℝ) : HasDerivAt (fun v => Lper κ σ μ2 A x v) (A ^ 3 / (4 * κ) * v) v := by
  have := ((hasDerivAt_id v).pow 2).const_mul (A ^ 3 / (8 * κ)) |>.sub_const (σ * (A / (2 * κ)) * (μ2 / 4) * x ^ 2)
  convert this using 1
  · ext y; simp [Lper]
  · simp; ring

/-- `∂L/∂x`. -/
lemma Lper_dx (κ σ μ2 A x v : ℝ) :
    HasDerivAt (fun x => Lper κ σ μ2 A x v) (-(σ * A * μ2 * x / (4 * κ))) x := by
  have := (((hasDerivAt_id x).pow 2).const_mul (σ * (A / (2 * κ)) * (μ2 / 4))).const_sub (A ^ 3 / (8 * κ) * v ^ 2)
  convert this using 1
  · ext y; simp [Lper]
  · simp; ring

/-- **(2) The per-mode Euler–Lagrange equation.** Along `φ` with velocity `φd` and scale factor `a`,
`d/dt(∂L/∂φ̇) − ∂L/∂φ = (a³/4κ)(φ̈ + 3(ȧ/a)φ̇ + σ(μ²/a²)φ)`: the friction is the expansion's own, and the
frequency is `σμ²/a²`. -/
theorem row58_euler_lagrange (κ σ μ2 : ℝ) (a φ φd : ℝ → ℝ) (t ad φdd : ℝ) (hκ : κ ≠ 0) (hat : a t ≠ 0)
    (ha : HasDerivAt a ad t) (hφd : HasDerivAt φd φdd t) :
    deriv (fun s => a s ^ 3 / (4 * κ) * φd s) t - (-(σ * a t * μ2 * φ t / (4 * κ))) =
      a t ^ 3 / (4 * κ) * (φdd + 3 * (ad / a t) * φd t + σ * (μ2 / a t ^ 2) * φ t) := by
  have hd : HasDerivAt (fun s => a s ^ 3 / (4 * κ) * φd s) _ t := ((ha.pow 3).div_const (4 * κ)).mul hφd
  rw [hd.deriv]
  simp only [Pi.pow_apply]
  field_simp
  ring

/-- So the Euler–Lagrange equation holds iff `φ̈ + 3(ȧ/a)φ̇ + σ(μ²/a²)φ = 0`. -/
theorem row58_euler_lagrange_iff (κ σ μ2 : ℝ) (a φ φd : ℝ → ℝ) (t ad φdd : ℝ) (hκ : κ ≠ 0) (hat : a t ≠ 0)
    (ha : HasDerivAt a ad t) (hφd : HasDerivAt φd φdd t) :
    deriv (fun s => a s ^ 3 / (4 * κ) * φd s) t - (-(σ * a t * μ2 * φ t / (4 * κ))) = 0 ↔
      φdd + 3 * (ad / a t) * φd t + σ * (μ2 / a t ^ 2) * φ t = 0 := by
  rw [row58_euler_lagrange κ σ μ2 a φ φd t ad φdd hκ hat ha hφd, mul_eq_zero]
  have : a t ^ 3 / (4 * κ) ≠ 0 := div_ne_zero (pow_ne_zero 3 hat) (mul_ne_zero four_ne_zero hκ)
  simp [this]

/-- **(3) The sign.** With `μ² = m² − 1`, the derived `σ = +1` gives `ω² = μ²/a² > 0` at every level `m ≥ 2`, and
`σ = −1` gives `ω² < 0` there: every level would be unstable. -/
theorem row58_sign (m : ℕ) (hm : 2 ≤ m) (A : ℝ) (hA : A ≠ 0) :
    0 < (1 : ℝ) * (((m : ℝ) ^ 2 - 1) / A ^ 2) ∧ (-1 : ℝ) * (((m : ℝ) ^ 2 - 1) / A ^ 2) < 0 := by
  have hm' : (2 : ℝ) ≤ m := by exact_mod_cast hm
  have : 0 < ((m : ℝ) ^ 2 - 1) / A ^ 2 := div_pos (by nlinarith) (by positivity)
  constructor <;> linarith

/-- **(4) The measure's power of `a`:** `det(a²M) = a⁶ det M` for `3 × 3`. -/
theorem row58_measure_power (A : ℝ) (M : Matrix (Fin 3) (Fin 3) ℝ) : (A ^ 2 • M).det = (A ^ 3) ^ 2 * M.det := by
  rw [Matrix.det_smul, Fintype.card_fin]; ring

end Row58Legendre

end ShadowProbe
#print axioms ShadowProbe.row58_legendre
#print axioms ShadowProbe.row58_hamiltonian
#print axioms ShadowProbe.row58_legendre_needs_sign
#print axioms ShadowProbe.row58_euler_lagrange
#print axioms ShadowProbe.row58_euler_lagrange_iff
#print axioms ShadowProbe.row58_sign
#print axioms ShadowProbe.row58_measure_power

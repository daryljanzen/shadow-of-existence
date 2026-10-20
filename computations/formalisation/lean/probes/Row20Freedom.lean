import ShadowEngine

/-! # Campaign 30 (`r7443+71`): row 20, the computed half of "the nonlinear freedom is the general first-class structure"

The receipt (`L801…/N1_the_nonlinear_freedom_is_the_general_first_class_structure.py`) splits the nonlinear question
in two:
- ***the freedom***: the constraints propagate. This rests on the contracted Bianchi identity, "an off-shell
  geometric identity, true for every metric". That is `contracted_bianchi` in `probes/Bianchi2.lean` (row 6), for
  THE connection of any smooth symmetric nondegenerate metric. It is cited, not rebuilt.
- ***the stability***: routed out to external theorems, and not a computation.

What the receipt computes beside the identity is built here:
- `tt_waves`: the four polarisations, each trace-free and transverse to its own `k`, along non-parallel directions;
- `superposition_transverse`: a two-wave superposition with arbitrary amplitudes is divergence-free at every point;
- `mode_equation`: the de Sitter mode function solves `u'' + (k² − 2/η²) u = 0` exactly;
- `shear_square`: `σ² = ½ ε² ḣ²`, a positive `O(ε²)` scalar. -/

namespace ShadowProbe

namespace R20Freedom

open Complex

/-- the polarisations: `e₁₊, e₁ₓ` along `k₁ = k ẑ`, `e₂₊, e₂ₓ` along `k₂ = k x̂` -/
def e1p : Matrix (Fin 3) (Fin 3) ℝ := !![1, 0, 0; 0, -1, 0; 0, 0, 0]
def e1x : Matrix (Fin 3) (Fin 3) ℝ := !![0, 1, 0; 1, 0, 0; 0, 0, 0]
def e2p : Matrix (Fin 3) (Fin 3) ℝ := !![0, 0, 0; 0, 1, 0; 0, 0, -1]
def e2x : Matrix (Fin 3) (Fin 3) ℝ := !![0, 0, 0; 0, 0, 1; 0, 1, 0]
def k1 (k : ℝ) : Fin 3 → ℝ := ![0, 0, k]
def k2 (k : ℝ) : Fin 3 → ℝ := ![k, 0, 0]

/-- the double contraction `e : e'` -/
def ddot (A B : Matrix (Fin 3) (Fin 3) ℝ) : ℝ := ∑ i, ∑ j, A i j * B i j

/-- **(1)** each polarisation is trace-free and transverse to its OWN `k`, and the two directions are orthogonal and
not parallel -/
theorem tt_waves (k : ℝ) (hk : k ≠ 0) :
    (e1p.trace = 0 ∧ e1x.trace = 0 ∧ e2p.trace = 0 ∧ e2x.trace = 0) ∧
      (e1p.mulVec (k1 k) = 0 ∧ e1x.mulVec (k1 k) = 0 ∧ e2p.mulVec (k2 k) = 0 ∧ e2x.mulVec (k2 k) = 0) ∧
      (∑ i, k1 k i * k2 k i = 0) ∧
      (k1 k 1 * k2 k 2 - k1 k 2 * k2 k 1, k1 k 2 * k2 k 0 - k1 k 0 * k2 k 2,
        k1 k 0 * k2 k 1 - k1 k 1 * k2 k 0) ≠ (0, 0, 0) := by
  refine ⟨⟨?_, ?_, ?_, ?_⟩, ⟨?_, ?_, ?_, ?_⟩, ?_, ?_⟩
  · simp [Matrix.trace, Fin.sum_univ_three, e1p]
  · simp [Matrix.trace, Fin.sum_univ_three, e1x]
  · simp [Matrix.trace, Fin.sum_univ_three, e2p]
  · simp [Matrix.trace, Fin.sum_univ_three, e2x]
  all_goals try (ext i; fin_cases i <;> simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three, e1p, e1x, e2p, e2x,
    k1, k2])
  · simp [Fin.sum_univ_three, k1, k2]
  · intro h; simp [k1, k2] at h; exact hk h

/-- the superposition `A₁(e₁₊ + e₁ₓ) e^{ikz} + A₂(e₂₊ + e₂ₓ) e^{ikx}`, complex-valued -/
noncomputable def hTT (A1 A2 : ℂ) (k x _y z : ℝ) (i j : Fin 3) : ℂ :=
  A1 * ((e1p + e1x) i j : ℂ) * exp (I * k * z) + A2 * ((e2p + e2x) i j : ℂ) * exp (I * k * x)

theorem hasDerivAt_wave (k s : ℝ) :
    HasDerivAt (fun t : ℝ => exp (I * k * t)) (I * k * exp (I * k * s)) s := by
  have h := ((hasDerivAt_id (s : ℂ)).const_mul (I * k)).cexp
  convert h.comp_ofReal using 1 <;> simp [mul_comm]

/-- **(2)** `∂_j h_ij = 0` for the two-wave superposition with ARBITRARY amplitudes, at every point: the three
partials exist, and they sum to zero because each wave's polarisation is transverse to its own direction -/
theorem superposition_transverse (A1 A2 : ℂ) (k x y z : ℝ) (i : Fin 3) :
    HasDerivAt (fun s => hTT A1 A2 k s y z i 0) (A2 * ((e2p + e2x) i 0 : ℂ) * (I * k * exp (I * k * x))) x ∧
      HasDerivAt (fun s => hTT A1 A2 k x s z i 1) 0 y ∧
      HasDerivAt (fun s => hTT A1 A2 k x y s i 2) (A1 * ((e1p + e1x) i 2 : ℂ) * (I * k * exp (I * k * z))) z ∧
      A2 * ((e2p + e2x) i 0 : ℂ) * (I * k * exp (I * k * x)) + 0
        + A1 * ((e1p + e1x) i 2 : ℂ) * (I * k * exp (I * k * z)) = 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp only [hTT]
    exact ((hasDerivAt_wave k x).const_mul _).const_add _
  · simp only [hTT]; exact hasDerivAt_const _ _
  · simp only [hTT]
    exact ((hasDerivAt_wave k z).const_mul _).add_const _
  · fin_cases i <;> simp [e1p, e1x, e2p, e2x]

/-- the de Sitter mode function `u = e^{−ikη}(1 − i/(kη))` and its first derivative, on the complex line -/
noncomputable def uC (k : ℝ) (w : ℂ) : ℂ := exp (-(I * k) * w) * (1 - I / k * w⁻¹)
noncomputable def u1C (k : ℝ) (w : ℂ) : ℂ := exp (-(I * k) * w) * (-(I * k) - w⁻¹ + I / k * (w ^ 2)⁻¹)

theorem uC_deriv (k : ℝ) (w : ℂ) (hk : (k : ℂ) ≠ 0) (hw : w ≠ 0) : HasDerivAt (uC k) (u1C k w) w := by
  have he := ((hasDerivAt_id w).const_mul (-(I * k))).cexp
  have hi := ((hasDerivAt_inv hw).const_mul (I / k)).const_sub 1
  convert he.mul hi using 1
  · funext v; simp only [uC, id, Pi.mul_apply]
  · simp only [u1C, id]; field_simp; ring_nf; simp only [I_sq]; ring

theorem u1C_deriv (k : ℝ) (w : ℂ) (hk : (k : ℂ) ≠ 0) (hw : w ≠ 0) :
    HasDerivAt (u1C k) (exp (-(I * k) * w) * (-(k : ℂ) ^ 2 + I * k / w + 2 / w ^ 2 - 2 * I / (k * w ^ 3))) w := by
  have he := ((hasDerivAt_id w).const_mul (-(I * k))).cexp
  have hw2 : w ^ 2 ≠ 0 := pow_ne_zero 2 hw
  have hsq : HasDerivAt (fun v : ℂ => v ^ 2) (2 * w) w := by simpa using hasDerivAt_pow 2 w
  have hi2 := (hsq.inv hw2).const_mul (I / k)
  have hi := ((hasDerivAt_inv hw).neg.const_add (-(I * k))).add hi2
  convert he.mul hi using 1
  · funext v; simp only [u1C, id, Pi.mul_apply, Pi.add_apply, Pi.neg_apply, Pi.inv_apply]; try ring
  · simp only [id, Pi.add_apply, Pi.neg_apply, Pi.inv_apply]
    field_simp; ring_nf; simp only [I_sq]; ring

/-- **(3)** the mode equation, exactly: for real `η ≠ 0` and `k ≠ 0`, `u'' + (k² − 2/η²) u = 0`, with both
derivatives taken over real `η` -/
theorem mode_equation (k η : ℝ) (hk : k ≠ 0) (hη : η ≠ 0) :
    HasDerivAt (fun t : ℝ => uC k t) (u1C k η) η ∧
      HasDerivAt (fun t : ℝ => u1C k t)
        (exp (-(I * k) * η) * (-(k : ℂ) ^ 2 + I * k / η + 2 / η ^ 2 - 2 * I / (k * η ^ 3))) η ∧
      exp (-(I * k) * η) * (-(k : ℂ) ^ 2 + I * k / η + 2 / η ^ 2 - 2 * I / (k * η ^ 3))
        + ((k : ℂ) ^ 2 - 2 / (η : ℂ) ^ 2) * uC k η = 0 := by
  have hη' : (η : ℂ) ≠ 0 := by exact_mod_cast hη
  have hk' : (k : ℂ) ≠ 0 := by exact_mod_cast hk
  refine ⟨(uC_deriv k η hk' hη').comp_ofReal, (u1C_deriv k η hk' hη').comp_ofReal, ?_⟩
  simp only [uC]; field_simp; ring

/-- **(4)** `e : e = 2` for each polarisation and `0` across; and `σ = ½ ε ḣ e₊` gives `σ² = ½ ε² ḣ²`, positive, with
`σ²/ε²` independent of `ε` -/
theorem shear_square (ε hd : ℝ) :
    (ddot e1p e1p = 2 ∧ ddot e1x e1x = 2 ∧ ddot e1p e1x = 0) ∧
      ddot ((1 / 2 * (ε * hd)) • e1p) ((1 / 2 * (ε * hd)) • e1p) = 1 / 2 * ε ^ 2 * hd ^ 2 ∧
      (ε * hd ≠ 0 → 0 < 1 / 2 * ε ^ 2 * hd ^ 2) := by
  refine ⟨⟨?_, ?_, ?_⟩, ?_, ?_⟩
  · simp [ddot, Fin.sum_univ_three, e1p]; norm_num
  · simp [ddot, Fin.sum_univ_three, e1x]; norm_num
  · simp [ddot, Fin.sum_univ_three, e1p, e1x]
  · simp [ddot, Fin.sum_univ_three, e1p]; ring
  · intro h; have := pow_pos (sq_pos_of_ne_zero h) 1; nlinarith [sq_nonneg ε, sq_nonneg hd, mul_pow ε hd 2]

end R20Freedom

end ShadowProbe

#print axioms ShadowProbe.R20Freedom.tt_waves
#print axioms ShadowProbe.R20Freedom.superposition_transverse
#print axioms ShadowProbe.R20Freedom.mode_equation
#print axioms ShadowProbe.R20Freedom.shear_square

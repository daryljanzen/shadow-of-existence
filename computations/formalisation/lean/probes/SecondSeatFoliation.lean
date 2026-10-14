import ShadowEngine

/-! # The second seat's foliation rows (`r7333+70`): 47, 102, 94

The constant-`r` leaves of a static-spherical metric `(−F, 1/F, r², r² sin²θ)` in `(t, r, θ, φ)`. Christoffel level,
through `lcConn_const` and `lcGam_diag4` only: no curvature. The profiles `F, P, S` are smooth and nowhere zero, with
`P = r²` and `S = sin²θ` near the point, as the convention (`exists_global_family`) allows. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

/-! ### `r7333` instance 1, row 47: the leaf's mixed extrinsic curvature, `diag(F′/(2√F), √F/r, √F/r)`,
from THE connection. The unit normal covector is `n = dr/√F`, so on the leaf `K_ab = −Γʳ_ab n_r` and
`K^a_a = K_aa / g_aa`. -/

section Inst_R47

set_option synthInstance.maxHeartbeats 400000

noncomputable def cL (F P S : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun y => -F (y 1), fun y => (F (y 1))⁻¹, fun y => P (y 1), fun y => P (y 1) * S (y 2)]

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hF hP hS hF0 in
lemma cL_smooth (k : Fin 4) : ContDiff ℝ ∞ (cL F P S k) := by
  fin_cases k
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).neg
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).inv fun y => hF0 _
  · exact hP.comp (contDiff_apply ℝ ℝ 1)
  · exact (hP.comp (contDiff_apply ℝ ℝ 1)).mul (hS.comp (contDiff_apply ℝ ℝ 2))
include hF0 hP0 hS0 in
lemma cL_ne (k : Fin 4) (p : Fin 4 → ℝ) : cL F P S k p ≠ 0 := by
  fin_cases k <;> simp [cL, hF0, hP0, hS0]

/-- `∇_{eᵢ} eᵢ` of THE connection of `cL`, at `p`. -/
noncomputable def nablaL (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
    (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (p : Fin 4 → ℝ) (i : Fin 4) : Fin 4 → ℝ :=
  lcConn (Fin 4 → ℝ) (ndOf (diag4 (cL F P S)) (diag4_symm _)
    (fun p u h => diag4_nondeg (fun i => cL_ne hF0 hP0 hS0 i p) u h)
    ((diag4_smooth (cL_smooth hF hP hS hF0)).differentiable (by simp)))
    (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) p (Pi.single i 1)

open Filter Topology in
include hF hP hS hF0 hP0 hS0 in
/-- **Row 47.** On the leaf through `p` (with `F > 0` there), `K^a_a = −Γʳ_aa (1/√F) / g_aa` is
`F′/(2√F)` for `t` and `√F/r` for `θ` and `φ`. -/
theorem leaf_K (p : Fin 4 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) (hpos : 0 < F (p 1)) :
    let K := fun i => -(nablaL hF hP hS hF0 hP0 hS0 p i 1) / Real.sqrt (F (p 1)) / cL F P S i p
    K 0 = deriv F (p 1) / (2 * Real.sqrt (F (p 1)))
      ∧ K 2 = Real.sqrt (F (p 1)) / p 1 ∧ K 3 = Real.sqrt (F (p 1)) / p 1 := by
  intro K
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have h2 : ∀ v, fderiv ℝ (cL F P S 2) p v = 2 * r * v 1 := fun v => by
    show fderiv ℝ (fun y => P (y 1)) p v = _
    rw [co_d1 hP]; simp [← hr_def, hP1]
  have h3 : ∀ v, fderiv ℝ (cL F P S 3) p v = 2 * r * v 1 * S (p 2) + r ^ 2 * (deriv S (p 2) * v 2) := fun v => by
    show fderiv ℝ (fun y => P (y 1) * S (y 2)) p v = _
    rw [pr_d1 hP hS]; simp [← hr_def, hP1, hPv]
  have hFd : ∀ v, fderiv ℝ (fun y : Fin 4 → ℝ => F (y 1)) p v = deriv F r * v 1 := fun v => by
    rw [co_d1 hF]
  have hPd : ∀ v, fderiv ℝ (fun y : Fin 4 → ℝ => P (y 1)) p v = 2 * r * v 1 := h2
  have hPSd : ∀ v, fderiv ℝ (fun y : Fin 4 → ℝ => P (y 1) * S (y 2)) p v
      = 2 * r * v 1 * S (p 2) + r ^ 2 * (deriv S (p 2) * v 2) := h3
  have hG : ∀ i, nablaL hF hP hS hF0 hP0 hS0 p i = gamD (cL F P S) p (Pi.single i 1) (Pi.single i 1) := fun i => by
    rw [nablaL, lcConn_const, lcGam_diag4 (fun i p => cL_ne hF0 hP0 hS0 i p) (cL_smooth hF hP hS hF0)]
  have hsq := Real.sq_sqrt hpos.le
  have hs0 : Real.sqrt (F r) ≠ 0 := (Real.sqrt_pos.2 hpos).ne'
  have hS0' := hS0 (p 2)
  have hFr := hF0 r
  refine ⟨?_, ?_, ?_⟩ <;>
  · simp only [K, hG, gamD, Fin.sum_univ_four]
    simp [hFd, hPd, hPSd, cL, ← hr_def, hPv]
    field_simp
    try rw [hsq]

end Inst_R47

/-! ### `r7333` instance 2, row 102: on SdS-α, `f = 1 − 2M/r − r²/α²`, the leaf's trace-free part is
`σ = diag(2/3, −1/3, −1/3)·(K₁ − K₂)`, and the shear has the closed form `K₁ − K₂ = (3M − r)/(r²√f)`,
from row 47's `K` -/

section Inst_R102

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

open Filter Topology in
include hF hP hS hF0 hP0 hS0 in
/-- **Row 102.** -/
theorem leaf_shear (M α : ℝ) (hα : α ≠ 0) (p : Fin 4 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M / s - s ^ 2 / α ^ 2) (hpos : 0 < F (p 1)) :
    let K := fun i => -(nablaL hF hP hS hF0 hP0 hS0 p i 1) / Real.sqrt (F (p 1)) / cL F P S i p
    let σ := fun i => K i - (K 0 + K 2 + K 3) / 3
    σ 0 + σ 2 + σ 3 = 0 ∧ σ 2 = σ 3 ∧ σ 0 = 2 * (K 0 - K 2) / 3
      ∧ K 0 - K 2 = (3 * M - p 1) / (p 1 ^ 2 * Real.sqrt (F (p 1))) := by
  intro K σ
  obtain ⟨k0, k2, k3⟩ := leaf_K hF hP hS hF0 hP0 hS0 p eP hpos
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  have hd : ∀ s, s ≠ 0 → HasDerivAt (fun s => 1 - 2 * M / s - s ^ 2 / α ^ 2) (2 * M / s ^ 2 - 2 * s / α ^ 2) s :=
    fun s hs => (((hasDerivAt_const s (1 : ℝ)).sub ((hasDerivAt_inv hs).const_mul (2 * M))).sub
      ((hasDerivAt_pow 2 s).div_const (α ^ 2))).congr_deriv (by field_simp; ring) |>.congr_of_eventuallyEq
      (Eventually.of_forall fun s => by simp [div_eq_mul_inv])
  have hFv : F r = 1 - 2 * M / r - r ^ 2 / α ^ 2 := eF.eq_of_nhds
  have hF1 : deriv F r = 2 * M / r ^ 2 - 2 * r / α ^ 2 := by rw [eF.deriv_eq, (hd r hr).deriv]
  have hs0 : Real.sqrt (F r) ≠ 0 := (Real.sqrt_pos.2 hpos).ne'
  have hsq := Real.sq_sqrt hpos.le
  have e0 : K 0 = deriv F r / (2 * Real.sqrt (F r)) := k0
  have e2 : K 2 = Real.sqrt (F r) / r := k2
  have e3 : K 3 = Real.sqrt (F r) / r := k3
  refine ⟨by simp only [σ]; ring, by simp only [σ, e2, e3], by simp only [σ, e2, e3]; ring, ?_⟩
  rw [e0, e2, hF1]
  field_simp
  rw [hsq, hFv]
  field_simp
  ring

end Inst_R102

/-! ### `r7333` instance 3, row 94: the leaf on SdS-α is umbilic (`K₁ = K₂ = K₃`) **iff** `r = 3M`: the
photon-sphere radius, with `α` dropping out -/

section Inst_R94

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

open Filter Topology in
include hF hP hS hF0 hP0 hS0 in
/-- **Row 94.** -/
theorem leaf_umbilic_iff (M α : ℝ) (hα : α ≠ 0) (p : Fin 4 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M / s - s ^ 2 / α ^ 2) (hpos : 0 < F (p 1)) :
    let K := fun i => -(nablaL hF hP hS hF0 hP0 hS0 p i 1) / Real.sqrt (F (p 1)) / cL F P S i p
    (K 0 = K 2 ∧ K 2 = K 3) ↔ p 1 = 3 * M := by
  intro K
  obtain ⟨-, -, k3⟩ := leaf_K hF hP hS hF0 hP0 hS0 p eP hpos
  obtain ⟨-, -, -, hsh⟩ := leaf_shear hF hP hS hF0 hP0 hS0 M α hα p eP eF hpos
  have hr : p 1 ≠ 0 := fun h => hP0 (p 1) (by rw [eP.eq_of_nhds, h]; simp)
  have hs0 : Real.sqrt (F (p 1)) ≠ 0 := (Real.sqrt_pos.2 hpos).ne'
  have k23 : K 2 = K 3 := by
    obtain ⟨-, k2, -⟩ := leaf_K hF hP hS hF0 hP0 hS0 p eP hpos
    simp only [K] at k2 k3 ⊢; rw [k2, k3]
  constructor
  · rintro ⟨h, -⟩
    have : (3 * M - p 1) / (p 1 ^ 2 * Real.sqrt (F (p 1))) = 0 := by
      simp only [K] at hsh h; rw [← hsh, h, sub_self]
    rcases div_eq_zero_iff.1 this with h' | h'
    · linarith
    · exact absurd h' (mul_ne_zero (pow_ne_zero 2 hr) hs0)
  · intro h
    refine ⟨?_, k23⟩
    have : K 0 - K 2 = 0 := by simp only [K] at hsh ⊢; rw [hsh, h]; simp
    linarith

end Inst_R94

#print axioms leaf_K
#print axioms leaf_shear
#print axioms leaf_umbilic_iff

end ShadowProbe

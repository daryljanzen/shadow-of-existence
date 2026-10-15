import ShadowEngine

/-! # Campaign 14 (`r7367+71.3`): row 79's half, SdS's static `S²` leaves

`P12_algebroid_paper/E1_static_gauge.py`: for `−f dt² + dr²/f + r²dΩ²` with `f = 1 − 2M/r − r²/α²`,
- (a) the static leaves `t = const` have `K_ab = 0`: `Γ^t_ab = 0` for spatial `a, b`;
- (b) the leaf's own 3-metric `dr²/f + r²dΩ²` has intrinsic `³R = 6/α² = 2Λ`, and `M` drops out.

(a) is on `ℝ⁴` (`lcGam_diag4`), for ANY static profiles. (b) is on the `r7341` port, `Fin 3`: THE connection of the
leaf metric gives `³R = 2(1 − F − rF′)/r²` for ANY `F`, and SdS's `F` makes it `6/α²`. The sphere profile is `sin²`
NEAR the point (the near-point convention; `exists_global_profile` builds a global one). -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold Topology

namespace ShadowProbe

section Row79Leaf

set_option synthInstance.maxHeartbeats 400000

/-- SdS's static 4-metric, `−F dt² + dr²/F + P(dθ² + S dφ²)`, coordinates `(t, r, θ, φ)`. -/
noncomputable def cS4 (F P S : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun y => -F (y 1), fun y => (F (y 1))⁻¹, fun y => P (y 1), fun y => P (y 1) * S (y 2)]

/-- The leaf's 3-metric, `dr²/F + P(dθ² + S dφ²)`, coordinates `(r, θ, φ)`. -/
noncomputable def cL3 (F P S : ℝ → ℝ) : Fin 3 → (Fin 3 → ℝ) → ℝ :=
  ![fun y => (F (y 0))⁻¹, fun y => P (y 0), fun y => P (y 0) * S (y 1)]

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hF hP hS hF0 in
lemma cS4_smooth (j : Fin 4) : ContDiff ℝ ∞ (cS4 F P S j) := by
  fin_cases j
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).neg
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).inv fun y => hF0 _
  · exact hP.comp (contDiff_apply ℝ ℝ 1)
  · exact (hP.comp (contDiff_apply ℝ ℝ 1)).mul (hS.comp (contDiff_apply ℝ ℝ 2))
include hF0 hP0 hS0 in
lemma cS4_ne (j : Fin 4) (p : Fin 4 → ℝ) : cS4 F P S j p ≠ 0 := by
  fin_cases j <;> simp [cS4, hF0, hP0, hS0]

include hF hP hS hF0 in
lemma cL3_smooth (j : Fin 3) : ContDiff ℝ ∞ (cL3 F P S j) := by
  fin_cases j
  · exact (hF.comp (contDiff_apply ℝ ℝ 0)).inv fun y => hF0 _
  · exact hP.comp (contDiff_apply ℝ ℝ 0)
  · exact (hP.comp (contDiff_apply ℝ ℝ 0)).mul (hS.comp (contDiff_apply ℝ ℝ 1))
include hF0 hP0 hS0 in
lemma cL3_ne (j : Fin 3) (p : Fin 3 → ℝ) : cL3 F P S j p ≠ 0 := by
  fin_cases j <;> simp [cL3, hF0, hP0, hS0]

include hF hP hS hF0 hP0 hS0 in
/-- **(a) Row 79, SdS's static leaves are totally geodesic.** No coefficient depends on `t`, so for spatial `a, b`
THE connection's `Γ^t_ab = 0`: `K_ab = 0` on every leaf, for ANY static profiles. -/
theorem sds_leaf_K_zero (p a b : Fin 4 → ℝ) (ha : a 0 = 0) (hb : b 0 = 0) :
    lcGam (diag4 (cS4 F P S)) p a b 0 = 0 := by
  have hinv : ContDiff ℝ ∞ (fun s => (F s)⁻¹) := hF.inv hF0
  have hneg : ContDiff ℝ ∞ (fun s => -F s) := hF.neg
  have hst : ∀ k, fderiv ℝ (cS4 F P S k) p (Pi.single 0 1) = 0 := fun k => by
    fin_cases k
    · show fderiv ℝ (fun y => (fun s => -F s) (y 1)) p _ = 0
      rw [co_d1 hneg]; simp
    · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1)) p _ = 0
      rw [co_d1 hinv]; simp
    · show fderiv ℝ (fun y => P (y 1)) p _ = 0
      rw [co_d1 hP]; simp
    · show fderiv ℝ (fun y => P (y 1) * S (y 2)) p _ = 0
      rw [pr_d1 hP hS]; simp
  rw [lcGam_diag4 (cS4_ne hF0 hP0 hS0) (cS4_smooth hF hP hS hF0)]
  simp [gamD, ha, hb, hst]

open Filter Topology in
/-- `sin²` and its two derivatives at `θ`. -/
lemma sin2_at' {S : ℝ → ℝ} {θ : ℝ} (eS : S =ᶠ[𝓝 θ] fun s => Real.sin s ^ 2) :
    S θ = Real.sin θ ^ 2 ∧ deriv S θ = 2 * Real.sin θ * Real.cos θ ∧
      deriv (deriv S) θ = 2 * Real.cos θ ^ 2 - 2 * Real.sin θ ^ 2 := by
  have sd : ∀ s, HasDerivAt (fun s => Real.sin s ^ 2) (2 * Real.sin s * Real.cos s) s := fun s =>
    (show HasDerivAt (fun s => Real.sin s ^ 2) _ s from (Real.hasDerivAt_sin s).pow 2).congr_deriv (by norm_num)
  refine ⟨eS.eq_of_nhds, by rw [eS.deriv_eq, (sd _).deriv], ?_⟩
  rw [(eS.deriv.trans (Eventually.of_forall fun s => (sd s).deriv) :
    deriv S =ᶠ[𝓝 θ] fun s => 2 * Real.sin s * Real.cos s).deriv_eq,
    (show HasDerivAt (fun s => 2 * Real.sin s * Real.cos s) _ θ from
      ((Real.hasDerivAt_sin θ).const_mul 2).mul (Real.hasDerivAt_cos θ)).deriv]
  ring

open Filter Topology in
set_option maxHeartbeats 16000000 in
include hF hP hS hF0 hP0 hS0 in
/-- **(b) Row 79, the leaf's intrinsic curvature.** THE connection of `dr²/F + r²dΩ²` on `ℝ³` (`P = r²`,
`S = sin²θ` near the point) has `³R = 2(1 − F − rF′)/r²`, for ANY `F`. -/
theorem leaf_scal (p : Fin 3 → ℝ) (eP : P =ᶠ[𝓝 (p 0)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 1)] fun s => Real.sin s ^ 2) :
    let Rf : Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℝ := fun i j k => curv (lcConn (Fin 3 → ℝ) (ndOf (diagN (cL3 F P S))
      (diagN_symm _) (fun p u h => diagN_nondeg (fun i => cL3_ne hF0 hP0 hS0 i p) u h)
      ((diagN_smooth (cL3_smooth hF hP hS hF0)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 3 → ℝ)) (fun _ => (Pi.single j 1 : Fin 3 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 3 → ℝ)) p
    scalCN (fun i => cL3 F P S i p) Rf = 2 * (1 - F (p 0) - p 0 * deriv F (p 0)) / p 0 ^ 2 := by
  intro Rf
  set r := p 0 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  obtain ⟨hSv, hS1, hS2⟩ := sin2_at' eS
  have hsa : Real.sin (p 1) ≠ 0 := fun h => hS0 (p 1) (by rw [hSv, h]; simp)
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  have dF' := fun s => (((contDiff_infty_iff_deriv.1 hF).2.differentiable (by simp)) s).hasDerivAt
  have iv1 : deriv (fun s => (F s)⁻¹) = fun s => -(deriv F s) / F s ^ 2 :=
    funext fun s => ((dF s).inv (hF0 s)).deriv.trans (by ring)
  have iv2 : deriv (deriv (fun s => (F s)⁻¹)) r = (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 := by
    rw [iv1, (show HasDerivAt (fun s => -deriv F s / F s ^ 2) _ r from
      (dF' r).neg.div ((dF r).pow 2) (pow_ne_zero 2 (hF0 r))).deriv]
    have := hF0 r; simp only [Pi.neg_apply]; field_simp; ring
  have hinv : ContDiff ℝ ∞ (fun s => (F s)⁻¹) := hF.inv hF0
  have hD1 : ∀ j v, fderiv ℝ (cL3 F P S j) p v = (![-(deriv F r) / F r ^ 2 * v 0,
      deriv P r * v 0, deriv P r * v 0 * S (p 1) + P r * (deriv S (p 1) * v 1)] : Fin 3 → ℝ) j := fun j v => by
    fin_cases j
    · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 0)) p v = _
      rw [co_d1 hinv]; simp [← hr_def, iv1]
    · show fderiv ℝ (fun y => P (y 0)) p v = _
      rw [co_d1 hP]; simp [← hr_def]
    · show fderiv ℝ (fun y => P (y 0) * S (y 1)) p v = _
      rw [pr_d1 hP hS]; simp [← hr_def]
  have hD2 : ∀ j u v, fderiv ℝ (fderiv ℝ (cL3 F P S j)) p u v = (![
      (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 * u 0 * v 0, deriv (deriv P) r * u 0 * v 0,
      deriv (deriv P) r * u 0 * v 0 * S (p 1) + deriv P r * v 0 * (deriv S (p 1) * u 1)
        + deriv P r * u 0 * (deriv S (p 1) * v 1) + P r * (deriv (deriv S) (p 1) * u 1 * v 1)] : Fin 3 → ℝ) j :=
    fun j u v => by
    fin_cases j
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 0))) p u v = _
      rw [co_d2 hinv]; simp [← hr_def, iv2]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 0))) p u v = _
      rw [co_d2 hP]; simp [← hr_def]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 0) * S (y 1))) p u v = _
      rw [pr_d2 hP hS]; simp [← hr_def]
  have hf := hF0 r
  have hR : ∀ i j, Rf i j j i = curvDN (cL3 F P S) p (Pi.single i 1) (Pi.single j 1) (Pi.single j 1) i :=
    fun i j => by simp only [Rf, curvDN_eq (cL3_ne hF0 hP0 hS0) (cL3_smooth hF hP hS hF0)]
  simp only [ricCN, scalCN, Fin.sum_univ_three, hR]
  simp only [curvDN, Pi.sub_apply, Pi.add_apply, DGDN, gamDN, dC1N, dC2N, hD1, hD2]
  simp [cL3, Fin.sum_univ_three, ← hr_def, hPv, hP1, hP2, hSv, hS1, hS2]
  field_simp
  ring

open Filter Topology in
include hP0 in
/-- **(b) for SdS:** `F = 1 − 2M/r − r²/α²` near `r` gives `³R = 6/α² = 2Λ`, independent of `M`. -/
theorem sds_leaf_R3 (M α : ℝ) (hα : α ≠ 0) (p : Fin 3 → ℝ) (eF : F =ᶠ[𝓝 (p 0)] fun s => 1 - 2 * M / s - s ^ 2 / α ^ 2)
    (eP : P =ᶠ[𝓝 (p 0)] fun s => s ^ 2) :
    2 * (1 - F (p 0) - p 0 * deriv F (p 0)) / p 0 ^ 2 = 6 / α ^ 2 := by
  have hr : p 0 ≠ 0 := fun h => hP0 _ (by rw [eP.eq_of_nhds, h]; simp)
  have h1 : HasDerivAt (fun s => 1 - 2 * M / s - s ^ 2 / α ^ 2) (2 * M / p 0 ^ 2 - 2 * p 0 / α ^ 2) (p 0) := by
    have := ((hasDerivAt_const (p 0) (1 : ℝ)).sub ((hasDerivAt_inv hr).const_mul (2 * M))).sub
      ((hasDerivAt_pow 2 (p 0)).div_const (α ^ 2))
    convert this using 1
    · ext s; simp [div_eq_mul_inv]
    · field_simp; ring
  rw [eF.eq_of_nhds, eF.deriv_eq, h1.deriv]
  field_simp; ring

end Row79Leaf

end ShadowProbe
#print axioms ShadowProbe.sds_leaf_K_zero
#print axioms ShadowProbe.leaf_scal
#print axioms ShadowProbe.sds_leaf_R3

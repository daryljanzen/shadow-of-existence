import ShadowEngine

/-! # The second seat's static-spherical Einstein rows (`r7333+70`): 48, 49, 51

`(−A, 1/F, r², r² sin²θ)` in `(t, r, θ, φ)`, with the lapse profile `A` and the radial profile `F` independent, smooth
and nowhere zero, and `P = r²`, `S = sin²θ` near the point (the convention, `exists_global_family`). The mixed
Einstein components `G^j_j = einsteinC g Rf j j / g j` are taken under THE connection through `curvD_eq`. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

/-! ### `r7333` instance 4, row 48: `G^t_t = (rF′ + F − 1)/r²`, with no `A` in it, and
`G^r_r = (rF A′/A + F − 1)/r²` -/

section Inst_R48

set_option synthInstance.maxHeartbeats 400000

noncomputable def cA (A F P S : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun y => -A (y 1), fun y => (F (y 1))⁻¹, fun y => P (y 1), fun y => P (y 1) * S (y 2)]

variable {A F P S : ℝ → ℝ} (hA : ContDiff ℝ ∞ A) (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P)
  (hS : ContDiff ℝ ∞ S) (hA0 : ∀ s, A s ≠ 0) (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hA hF hP hS hF0 in
lemma cA_smooth (k : Fin 4) : ContDiff ℝ ∞ (cA A F P S k) := by
  fin_cases k
  · exact (hA.comp (contDiff_apply ℝ ℝ 1)).neg
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).inv fun y => hF0 _
  · exact hP.comp (contDiff_apply ℝ ℝ 1)
  · exact (hP.comp (contDiff_apply ℝ ℝ 1)).mul (hS.comp (contDiff_apply ℝ ℝ 2))
include hA0 hF0 hP0 hS0 in
lemma cA_ne (k : Fin 4) (p : Fin 4 → ℝ) : cA A F P S k p ≠ 0 := by
  fin_cases k <;> simp [cA, hA0, hF0, hP0, hS0]

/-- THE connection's curvature of `cA` on basis fields, at `p`. -/
noncomputable def RfA (hA : ContDiff ℝ ∞ A) (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
    (hA0 : ∀ s, A s ≠ 0) (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (p : Fin 4 → ℝ) :
    Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ := fun i j k =>
  curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cA A F P S)) (diag4_symm _)
    (fun p u h => diag4_nondeg (fun i => cA_ne hA0 hF0 hP0 hS0 i p) u h)
    ((diag4_smooth (cA_smooth hA hF hP hS hF0)).differentiable (by simp))))
    (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
    (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p

/-- The mixed Einstein component `G^j_j`. -/
noncomputable def GA (hA : ContDiff ℝ ∞ A) (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
    (hA0 : ∀ s, A s ≠ 0) (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (p : Fin 4 → ℝ)
    (j : Fin 4) : ℝ :=
  einsteinC (fun i => cA A F P S i p) (RfA hA hF hP hS hA0 hF0 hP0 hS0 p) j j / cA A F P S j p

open Filter Topology in
include hA hF hP hS hF0 in
/-- The recipe's facts for `cA`: first and second partials at `p`, with `P = r²` near `r = p 1`. -/
lemma cA_derivs (p : Fin 4 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    (∀ k v, fderiv ℝ (cA A F P S k) p v = (![-(deriv A (p 1) * v 1), -(deriv F (p 1)) / F (p 1) ^ 2 * v 1,
      2 * p 1 * v 1, 2 * p 1 * v 1 * S (p 2) + p 1 ^ 2 * (deriv S (p 2) * v 2)] : Fin 4 → ℝ) k)
    ∧ (∀ k u v, fderiv ℝ (fderiv ℝ (cA A F P S k)) p u v = (![-(deriv (deriv A) (p 1) * u 1 * v 1),
      (2 * deriv F (p 1) ^ 2 - F (p 1) * deriv (deriv F) (p 1)) / F (p 1) ^ 3 * u 1 * v 1, 2 * u 1 * v 1,
      2 * u 1 * v 1 * S (p 2) + 2 * p 1 * v 1 * (deriv S (p 2) * u 2) + 2 * p 1 * u 1 * (deriv S (p 2) * v 2)
        + p 1 ^ 2 * (deriv (deriv S) (p 2) * u 2 * v 2)] : Fin 4 → ℝ) k) := by
  set r := p 1 with hr_def
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have e2 : deriv P =ᶠ[𝓝 r] fun s => 2 * s := eP.deriv.trans (Eventually.of_forall fun s => by simp)
  have hP2 : deriv (deriv P) r = 2 := by rw [e2.deriv_eq]; simp
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  have dF' := fun s => (((contDiff_infty_iff_deriv.1 hF).2.differentiable (by simp)) s).hasDerivAt
  have iv1 : deriv (fun s => (F s)⁻¹) = fun s => -(deriv F s) / F s ^ 2 :=
    funext fun s => ((dF s).inv (hF0 s)).deriv.trans (by ring)
  have iv2 : deriv (deriv (fun s => (F s)⁻¹)) r = (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 := by
    rw [iv1, (show HasDerivAt (fun s => -deriv F s / F s ^ 2) _ r from
      (dF' r).neg.div ((dF r).pow 2) (pow_ne_zero 2 (hF0 r))).deriv]
    have := hF0 r; simp only [Pi.neg_apply]; field_simp; ring
  have ng1 : deriv (fun s => -A s) = fun s => -deriv A s := funext fun s => deriv.neg
  have hneg : ContDiff ℝ ∞ (fun s => -A s) := hA.neg
  have hinv : ContDiff ℝ ∞ (fun s => (F s)⁻¹) := hF.inv hF0
  refine ⟨fun k v => ?_, fun k u v => ?_⟩
  · fin_cases k
    · show fderiv ℝ (fun y => (fun s => -A s) (y 1)) p v = _
      rw [co_d1 hneg]; simp [← hr_def, ng1]
    · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1)) p v = _
      rw [co_d1 hinv]; simp [← hr_def, iv1]
    · show fderiv ℝ (fun y => P (y 1)) p v = _
      rw [co_d1 hP]; simp [← hr_def, hP1]
    · show fderiv ℝ (fun y => P (y 1) * S (y 2)) p v = _
      rw [pr_d1 hP hS]; simp [← hr_def, hP1, hPv]
  · fin_cases k
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => -A s) (y 1))) p u v = _
      rw [co_d2 hneg]; simp [← hr_def, ng1]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1))) p u v = _
      rw [co_d2 hinv]; simp [← hr_def, iv2]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1))) p u v = _
      rw [co_d2 hP]; simp [← hr_def, hP2]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1) * S (y 2))) p u v = _
      rw [pr_d2 hP hS]; simp [← hr_def, hP1, hP2, hPv]

open Filter Topology in
/-- `sin²` and its first two derivatives at a point, as the angular profile's values. -/
lemma sin2_vals {S : ℝ → ℝ} (θ : ℝ) (eS : S =ᶠ[𝓝 θ] fun s => Real.sin s ^ 2) :
    S θ = Real.sin θ ^ 2 ∧ deriv S θ = 2 * Real.sin θ * Real.cos θ
      ∧ deriv (deriv S) θ = 2 * Real.cos θ ^ 2 - 2 * Real.sin θ ^ 2 := by
  have sd : ∀ s, HasDerivAt (fun s => Real.sin s ^ 2) (2 * Real.sin s * Real.cos s) s := fun s =>
    (show HasDerivAt (fun s => Real.sin s ^ 2) _ s from (Real.hasDerivAt_sin s).pow 2).congr_deriv (by norm_num)
  have e3 : deriv S =ᶠ[𝓝 θ] fun s => 2 * Real.sin s * Real.cos s :=
    eS.deriv.trans (Eventually.of_forall fun s => (sd s).deriv)
  refine ⟨eS.eq_of_nhds, by rw [eS.deriv_eq, (sd _).deriv], ?_⟩
  rw [e3.deriv_eq]
  have := (show HasDerivAt (fun s => 2 * Real.sin s * Real.cos s) _ θ from
    ((Real.hasDerivAt_sin θ).const_mul 2).mul (Real.hasDerivAt_cos θ))
  rw [this.deriv]; ring

open Filter Topology in
set_option maxHeartbeats 8000000 in
include hA hF hP hS hA0 hF0 hP0 hS0 in
/-- **Row 48.** -/
theorem static_Gtt_Grr (p : Fin 4 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    GA hA hF hP hS hA0 hF0 hP0 hS0 p 0 = (p 1 * deriv F (p 1) + F (p 1) - 1) / p 1 ^ 2
      ∧ GA hA hF hP hS hA0 hF0 hP0 hS0 p 1
        = (p 1 * F (p 1) * deriv A (p 1) / A (p 1) + F (p 1) - 1) / p 1 ^ 2 := by
  obtain ⟨hD1, hD2⟩ := cA_derivs hA hF hP hS hF0 p eP
  obtain ⟨hSv, hS1, hS2⟩ := sin2_vals (p 2) eS
  have hr : p 1 ≠ 0 := fun h => hP0 (p 1) (by rw [eP.eq_of_nhds, h]; simp)
  have hPv : P (p 1) = p 1 ^ 2 := eP.eq_of_nhds
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have := hA0 (p 1); have := hF0 (p 1)
  simp only [GA, RfA, einsteinC, scalC, ricC, Fin.sum_univ_four,
    curvD_eq (cA_ne hA0 hF0 hP0 hS0) (cA_smooth hA hF hP hS hF0)]
  simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
  simp [cA, Fin.sum_univ_four, hPv, hSv, hS1, hS2]
  constructor
  · field_simp; ring
  · field_simp; ring

end Inst_R48

/-! ### `r7333` instance 5, row 49: the `A = F` member. `G^t_t = G^r_r` for every `F`;
`G^θ_θ = F″/2 + F′/r`; and with `F = 1 − 2m/r − Λr²/3`, `G^t_t + Λ = −2m′/r²`, so the density is `m′/(4πr²)` and a
constant `m` is vacuum (SdS) -/

section Inst_R49

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P)
  (hS : ContDiff ℝ ∞ S) (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

open Filter Topology in
/-- The mass-function profile `1 − 2m/r − Λr²/3`: its value and slope at `r ≠ 0`. -/
lemma mass_profile {F m : ℝ → ℝ} (hm : ContDiff ℝ ∞ m) (Λ r : ℝ) (hr : r ≠ 0)
    (eF : F =ᶠ[𝓝 r] fun s => 1 - 2 * m s / s - Λ * s ^ 2 / 3) :
    F r = 1 - 2 * m r / r - Λ * r ^ 2 / 3
      ∧ deriv F r = -(2 * deriv m r / r) + 2 * m r / r ^ 2 - 2 * Λ * r / 3 := by
  have dm := ((hm.differentiable (by simp)) r).hasDerivAt
  refine ⟨eF.eq_of_nhds, ?_⟩
  have h := (show HasDerivAt (fun s => 1 - 2 * m s / s - Λ * s ^ 2 / 3) _ r from
    ((hasDerivAt_const r (1 : ℝ)).sub ((dm.const_mul 2).div (hasDerivAt_id' r) hr)).sub
      (((hasDerivAt_pow 2 r).const_mul Λ).div_const 3))
  rw [eF.deriv_eq, h.deriv]; field_simp; ring

open Filter Topology in
set_option maxHeartbeats 8000000 in
include hF hP hS hF0 hP0 hS0 in
/-- **Row 49.** -/
theorem static_AeqF (p : Fin 4 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    GA hF hF hP hS hF0 hF0 hP0 hS0 p 0 = GA hF hF hP hS hF0 hF0 hP0 hS0 p 1
      ∧ GA hF hF hP hS hF0 hF0 hP0 hS0 p 2 = deriv (deriv F) (p 1) / 2 + deriv F (p 1) / p 1 := by
  obtain ⟨g0, g1⟩ := static_Gtt_Grr hF hF hP hS hF0 hF0 hP0 hS0 p eP eS
  obtain ⟨hD1, hD2⟩ := cA_derivs (A := F) hF hF hP hS hF0 p eP
  obtain ⟨hSv, hS1, hS2⟩ := sin2_vals (p 2) eS
  have hr : p 1 ≠ 0 := fun h => hP0 (p 1) (by rw [eP.eq_of_nhds, h]; simp)
  have hPv : P (p 1) = p 1 ^ 2 := eP.eq_of_nhds
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have := hF0 (p 1)
  refine ⟨by rw [g0, g1]; field_simp, ?_⟩
  simp only [GA, RfA, einsteinC, scalC, ricC, Fin.sum_univ_four,
    curvD_eq (cA_ne hF0 hF0 hP0 hS0) (cA_smooth hF hF hP hS hF0)]
  simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
  simp [cA, Fin.sum_univ_four, hPv, hSv, hS1, hS2]
  field_simp; ring

open Filter Topology in
include hF hP hS hF0 hP0 hS0 in
/-- **Row 49, the density.** -/
theorem static_density {m : ℝ → ℝ} (hm : ContDiff ℝ ∞ m) (Λ : ℝ) (p : Fin 4 → ℝ)
    (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * m s / s - Λ * s ^ 2 / 3) :
    GA hF hF hP hS hF0 hF0 hP0 hS0 p 0 + Λ = -(2 * deriv m (p 1) / p 1 ^ 2)
      ∧ (deriv m (p 1) = 0 → GA hF hF hP hS hF0 hF0 hP0 hS0 p 0 + Λ = 0) := by
  have hr : p 1 ≠ 0 := fun h => hP0 (p 1) (by rw [eP.eq_of_nhds, h]; simp)
  obtain ⟨g0, -⟩ := static_Gtt_Grr hF hF hP hS hF0 hF0 hP0 hS0 p eP eS
  obtain ⟨fv, f1⟩ := mass_profile hm Λ (p 1) hr eF
  have e : GA hF hF hP hS hF0 hF0 hP0 hS0 p 0 + Λ = -(2 * deriv m (p 1) / p 1 ^ 2) := by
    rw [g0, fv, f1]; field_simp; ring
  exact ⟨e, fun h => by rw [e, h]; simp⟩

end Inst_R49

/-! ### `r7333` instance 6, row 51: the lapse `A` free and `F = 1 − 2m/r − Λr²/3`. The density
`ρ = −(G^t_t + Λ)/8π = m′/(4πr²)` does not involve `A`, and the radial equation `G^r_r + Λ = 8πP` closes as TOV:
`A′/A = 2(m + 4πr³P − Λr³/3)/(r²F)` -/

section Inst_R51

variable {A F P S : ℝ → ℝ} (hA : ContDiff ℝ ∞ A) (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P)
  (hS : ContDiff ℝ ∞ S) (hA0 : ∀ s, A s ≠ 0) (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

open Filter Topology in
include hA hF hP hS hA0 hF0 hP0 hS0 in
/-- **Row 51.** -/
theorem static_tov {m : ℝ → ℝ} (hm : ContDiff ℝ ∞ m) (Λ pr : ℝ) (p : Fin 4 → ℝ)
    (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * m s / s - Λ * s ^ 2 / 3) :
    -(GA hA hF hP hS hA0 hF0 hP0 hS0 p 0 + Λ) / (8 * Real.pi) = deriv m (p 1) / (4 * Real.pi * p 1 ^ 2)
      ∧ (GA hA hF hP hS hA0 hF0 hP0 hS0 p 1 + Λ = 8 * Real.pi * pr →
        deriv A (p 1) / A (p 1)
          = 2 * (m (p 1) + 4 * Real.pi * p 1 ^ 3 * pr - Λ * p 1 ^ 3 / 3) / (p 1 ^ 2 * F (p 1))) := by
  have hr : p 1 ≠ 0 := fun h => hP0 (p 1) (by rw [eP.eq_of_nhds, h]; simp)
  obtain ⟨g0, g1⟩ := static_Gtt_Grr hA hF hP hS hA0 hF0 hP0 hS0 p eP eS
  obtain ⟨fv, f1⟩ := mass_profile hm Λ (p 1) hr eF
  have hf := hF0 (p 1); have ha := hA0 (p 1)
  refine ⟨by rw [g0, fv, f1]; field_simp; ring, fun h => ?_⟩
  rw [g1] at h
  have hpi := Real.pi_pos.ne'
  rw [div_eq_div_iff ha (mul_ne_zero (pow_ne_zero 2 hr) hf)]
  field_simp at h
  rw [fv] at h hf ⊢
  field_simp at h hf ⊢
  linear_combination h

end Inst_R51

#print axioms static_Gtt_Grr
#print axioms static_AeqF
#print axioms static_density
#print axioms static_tov

end ShadowProbe

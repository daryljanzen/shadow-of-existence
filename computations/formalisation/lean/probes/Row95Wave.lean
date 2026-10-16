import ShadowEngine

/-! # Campaign 22 (`r7411+71.9`): row 95 under THE connection

`P15_the_four_dimensional_treatment_keeps_the_economy….py`, on `−F dt² + dr²/F + P(dθ² + S dφ²)` with `P = r²` and
`S = sin²θ` near the point (the convention, as in campaigns 14–16), any `F`:
- (A) `so3_killing`: `∂_φ` and the two rotations `sin φ ∂_θ + cot θ cos φ ∂_φ`, `cos φ ∂_θ − cot θ sin φ ∂_φ` have zero
  Killing form under THE connection at every point off the poles (`killF95_model` re-proves `killF_model`);
- (B) `sph_wave_sep`: THE connection's wave operator (`boxD`) on `T(t) R(r) Θ(θ) Φ(φ)` with `T″ = −w²T`, `Φ″ = −m²Φ`
  and `Θ` an associated Legendre function of eigenvalue `L` is `TΘΦ (w²R/F + FR″ + (F′ + 2F/r)R′ − LR/r²)`;
- (C) `harm_ℓ_m`: the receipt's nine harmonics (`ℓ = 1..3`, `m = 0..ℓ`) satisfy that equation with
  `L = ℓ(ℓ + 1)`, their derivatives PROVED; so the radial operator is the same for every `m` and
  `op(ℓ = 2) − op(ℓ = 1) = −(6 − 2)R/r²`;
- (D) `s3_levels`: `L(L + 2) = 4j(j + 1)` at `j = L/2`.

Not built: the receipt's Hopf-fibre expressions (hand-assigned `m`) and its text pins. -/

open Bundle Manifold Filter Set VectorField Topology
open scoped ContDiff Manifold

namespace ShadowProbe

/-! ### (A) the `so(3)` Killing fields -/

section KillingSO3

variable {c : Fin 4 → (Fin 4 → ℝ) → ℝ} (hc : ∀ i p, c i p ≠ 0) (hcs : ∀ i, ContDiff ℝ ∞ (c i))

/-- THE Levi-Civita connection of `Σ cᵢ dxᵢ²` on `ℝ⁴` (as in `Row77Killing.lean`; probes do not import each other). -/
noncomputable abbrev gw95 (hc : ∀ i p, c i p ≠ 0) (hcs : ∀ i, ContDiff ℝ ∞ (c i)) :=
  ndOf (diag4 c) (diag4_symm c) (fun p u h => diag4_nondeg (fun i => hc i p) u h)
    ((diag4_smooth hcs).differentiable (by simp))

/-- The Killing form `g(∇_uξ, v) + g(u, ∇_vξ)` under THE connection. -/
noncomputable def killF95 (ξ : (Fin 4 → ℝ) → (Fin 4 → ℝ)) (p u v : Fin 4 → ℝ) : ℝ :=
  diag4 c p (lcConn (Fin 4 → ℝ) (gw95 hc hcs) (fun y => ξ y) p u) v
    + diag4 c p u (lcConn (Fin 4 → ℝ) (gw95 hc hcs) (fun y => ξ y) p v)

include hc hcs in
/-- `∇_wξ = Dξ·w + Γ(w, ξ)` (re-proved from `killF_model`, `r7371+71.9`). -/
theorem killF95_model {ξ : (Fin 4 → ℝ) → (Fin 4 → ℝ)} {p : Fin 4 → ℝ} (hξ : DifferentiableAt ℝ ξ p)
    (u v : Fin 4 → ℝ) :
    killF95 hc hcs ξ p u v = diag4 c p (fderiv ℝ ξ p u + gamD c p u (ξ p)) v
      + diag4 c p u (fderiv ℝ ξ p v + gamD c p v (ξ p)) := by
  have hG : ∀ x w b, lcConn (Fin 4 → ℝ) (gw95 hc hcs) (fun _ => b) x w = lcGam (diag4 c) x w b :=
    fun x w b => lcConn_const _ _ _ x w b
  let σ : Π x : Fin 4 → ℝ, TangentSpace 𝓘(ℝ, Fin 4 → ℝ) x := fun y => ξ y
  have hσ := (mdiffAt_model (σ := σ) (x := p)).2 hξ
  have hm := fun w => cov_model (lcConn (Fin 4 → ℝ) (gw95 hc hcs)) (lcGam (diag4 c)) hG hσ w
  have e : ∀ w : Fin 4 → ℝ, lcConn (Fin 4 → ℝ) (gw95 hc hcs) (fun y => ξ y) p w
      = fderiv ℝ ξ p w + gamD c p w (ξ p) := fun w => by
    rw [← lcGam_diag4 hc hcs]; exact hm w
  simp only [killF95, e]

end KillingSO3

/-- The rotation `sin φ ∂_θ + cot θ cos φ ∂_φ`. -/
noncomputable def rotA (y : Fin 4 → ℝ) : Fin 4 → ℝ :=
  ![0, 0, Real.sin (y 3), Real.cos (y 2) / Real.sin (y 2) * Real.cos (y 3)]

/-- The rotation `cos φ ∂_θ − cot θ sin φ ∂_φ`. -/
noncomputable def rotB (y : Fin 4 → ℝ) : Fin 4 → ℝ :=
  ![0, 0, Real.cos (y 3), -(Real.cos (y 2) / Real.sin (y 2) * Real.sin (y 3))]

lemma cot_has (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    HasDerivAt (fun s => Real.cos s / Real.sin s) (-1 / Real.sin θ ^ 2) θ := by
  have := (Real.hasDerivAt_cos θ).div (Real.hasDerivAt_sin θ) hs
  convert this using 1; field_simp; linear_combination Real.sin_sq_add_cos_sq θ

/-- The coordinate projection `y ↦ y i` on `ℝ⁴`, as a continuous linear map. -/
noncomputable abbrev pr4 (i : Fin 4) : (Fin 4 → ℝ) →L[ℝ] ℝ := ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) i

lemma rotA_fd (p : Fin 4 → ℝ) (hs : Real.sin (p 2) ≠ 0) : HasFDerivAt rotA (ContinuousLinearMap.pi
    ![(0 : (Fin 4 → ℝ) →L[ℝ] ℝ), 0, Real.cos (p 3) • pr4 3,
      (-1 / Real.sin (p 2) ^ 2 * Real.cos (p 3)) • pr4 2
        + (-(Real.cos (p 2) / Real.sin (p 2) * Real.sin (p 3))) • pr4 3]) p := by
  rw [hasFDerivAt_pi']
  intro i; fin_cases i
  · simpa [rotA] using hasFDerivAt_const (0 : ℝ) p
  · simpa [rotA] using hasFDerivAt_const (0 : ℝ) p
  · simpa [rotA] using fd_coord_i (x := p) 3 (Real.differentiableAt_sin)
  · have h := (fd_coord_i (x := p) 2 (cot_has (p 2) hs).differentiableAt).mul
      (fd_coord_i (x := p) 3 (Real.differentiableAt_cos))
    rw [(cot_has (p 2) hs).deriv, Real.deriv_cos] at h
    convert h using 1
    · ext y; simp [rotA]
    · ext v; simp; ring

lemma rotB_fd (p : Fin 4 → ℝ) (hs : Real.sin (p 2) ≠ 0) : HasFDerivAt rotB (ContinuousLinearMap.pi
    ![(0 : (Fin 4 → ℝ) →L[ℝ] ℝ), 0, (-Real.sin (p 3)) • pr4 3,
      (1 / Real.sin (p 2) ^ 2 * Real.sin (p 3)) • pr4 2
        + (-(Real.cos (p 2) / Real.sin (p 2) * Real.cos (p 3))) • pr4 3]) p := by
  rw [hasFDerivAt_pi']
  intro i; fin_cases i
  · simpa [rotB] using hasFDerivAt_const (0 : ℝ) p
  · simpa [rotB] using hasFDerivAt_const (0 : ℝ) p
  · simpa [rotB] using fd_coord_i (x := p) 3 (Real.differentiableAt_cos)
  · have h := ((fd_coord_i (x := p) 2 (cot_has (p 2) hs).differentiableAt).mul
      (fd_coord_i (x := p) 3 (Real.differentiableAt_sin))).neg
    rw [(cot_has (p 2) hs).deriv, Real.deriv_sin] at h
    convert h using 1
    · ext y; simp [rotB]
    · ext v; simp; ring

section Row95Wave

set_option synthInstance.maxHeartbeats 400000

/-- The static spherical metric `−F dt² + dr²/F + P(r)(dθ² + S(θ) dφ²)` on `ℝ⁴`, coordinates `(t, r, θ, φ)`. -/
noncomputable def cSph (F P S : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun y => -F (y 1), fun y => (F (y 1))⁻¹, fun y => P (y 1), fun y => P (y 1) * S (y 2)]

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hF hP hS hF0 in
lemma cSph_smooth (j : Fin 4) : ContDiff ℝ ∞ (cSph F P S j) := by
  fin_cases j
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).neg
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).inv fun y => hF0 _
  · exact hP.comp (contDiff_apply ℝ ℝ 1)
  · exact (hP.comp (contDiff_apply ℝ ℝ 1)).mul (hS.comp (contDiff_apply ℝ ℝ 2))

include hF0 hP0 hS0 in
lemma cSph_ne (j : Fin 4) (p : Fin 4 → ℝ) : cSph F P S j p ≠ 0 := by
  fin_cases j <;> simp [cSph, hF0, hP0, hS0]

include hF hP hS hF0 in
/-- First partials of the metric coefficients. -/
lemma cSph_d1 (p v : Fin 4 → ℝ) (j : Fin 4) : fderiv ℝ (cSph F P S j) p v = (![-(deriv F (p 1) * v 1),
    -(deriv F (p 1)) / F (p 1) ^ 2 * v 1, deriv P (p 1) * v 1,
    deriv P (p 1) * v 1 * S (p 2) + P (p 1) * (deriv S (p 2) * v 2)] : Fin 4 → ℝ) j := by
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  fin_cases j
  · show fderiv ℝ (fun y => (fun s => -F s) (y 1)) p v = _
    rw [co_d1 hF.neg, (show HasDerivAt (fun s => -F s) _ (p 1) from (dF _).neg).deriv]; simp
  · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1)) p v = _
    rw [co_d1 (show ContDiff ℝ ∞ (fun s => (F s)⁻¹) from hF.inv hF0),
      (show HasDerivAt (fun s => (F s)⁻¹) _ (p 1) from (dF _).inv (hF0 _)).deriv]; simp
  · show fderiv ℝ (fun y => P (y 1)) p v = _
    rw [co_d1 hP]; simp
  · show fderiv ℝ (fun y => P (y 1) * S (y 2)) p v = _
    rw [pr_d1 hP hS]; simp

set_option maxHeartbeats 1000000 in
include hF hP hS hF0 hP0 hS0 in
/-- **Row 95 (A).** On `−F dt² + dr²/F + P(dθ² + S dφ²)` with `S = sin²θ` near the point (any `F`, any `P`), the three
`so(3)` fields `∂_φ`, `sin φ ∂_θ + cot θ cos φ ∂_φ`, `cos φ ∂_θ − cot θ sin φ ∂_φ` have zero Killing form under THE
connection at every point off the poles: `g(∇_uξ, v) + g(u, ∇_vξ) = 0` on every pair of coordinate vectors. -/
theorem so3_killing (p : Fin 4 → ℝ) (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) (i j : Fin 4) :
    killF95 (cSph_ne hF0 hP0 hS0) (cSph_smooth hF hP hS hF0) (fun _ => Pi.single 3 1) p
        (Pi.single i 1) (Pi.single j 1) = 0 ∧
      killF95 (cSph_ne hF0 hP0 hS0) (cSph_smooth hF hP hS hF0) rotA p (Pi.single i 1) (Pi.single j 1) = 0 ∧
      killF95 (cSph_ne hF0 hP0 hS0) (cSph_smooth hF hP hS hF0) rotB p (Pi.single i 1) (Pi.single j 1) = 0 := by
  have hsn : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [eS.eq_of_nhds, h]; simp)
  have hSv : S (p 2) = Real.sin (p 2) ^ 2 := eS.eq_of_nhds
  have hS1 : deriv S (p 2) = 2 * Real.sin (p 2) * Real.cos (p 2) := by
    rw [eS.deriv_eq, (show HasDerivAt (fun s => Real.sin s ^ 2) _ (p 2) from (Real.hasDerivAt_sin (p 2)).pow 2).deriv]
    simp
  have hPp := hP0 (p 1); have hf := hF0 (p 1)
  refine ⟨?_, ?_, ?_⟩
  · rw [killF95_model _ _ (differentiableAt_const _)]
    fin_cases i <;> fin_cases j <;>
      simp only [diag4_apply, Fin.sum_univ_four, Pi.add_apply, gamD, cSph_d1 hF hP hS hF0] <;>
      simp [cSph, hSv, hS1] <;> field_simp <;> ring
  · rw [killF95_model _ _ (rotA_fd p hsn).differentiableAt, (rotA_fd p hsn).fderiv]
    fin_cases i <;> fin_cases j <;>
      simp only [diag4_apply, Fin.sum_univ_four, Pi.add_apply, gamD, cSph_d1 hF hP hS hF0] <;>
      simp [cSph, hSv, hS1, rotA] <;> field_simp <;> first | ring1 | simp
  · rw [killF95_model _ _ (rotB_fd p hsn).differentiableAt, (rotB_fd p hsn).fderiv]
    fin_cases i <;> fin_cases j <;>
      simp only [diag4_apply, Fin.sum_univ_four, Pi.add_apply, gamD, cSph_d1 hF hP hS hF0] <;>
      simp [cSph, hSv, hS1, rotB] <;> field_simp <;> first | ring1 | simp

/-- `φ = T(t) R(r) Θ(θ) Φ(φ)`. -/
noncomputable def sep4 (T R Θ Φ : ℝ → ℝ) (y : Fin 4 → ℝ) : ℝ := T (y 0) * R (y 1) * Θ (y 2) * Φ (y 3)

variable {T R Θ Φ : ℝ → ℝ} (hT : ContDiff ℝ ∞ T) (hR : ContDiff ℝ ∞ R) (hΘ : ContDiff ℝ ∞ Θ) (hΦ : ContDiff ℝ ∞ Φ)

include hT hR hΘ hΦ in
lemma sep4_fd (y v : Fin 4 → ℝ) : fderiv ℝ (sep4 T R Θ Φ) y v
    = deriv T (y 0) * v 0 * R (y 1) * Θ (y 2) * Φ (y 3) + T (y 0) * (deriv R (y 1) * v 1) * Θ (y 2) * Φ (y 3)
      + T (y 0) * R (y 1) * (deriv Θ (y 2) * v 2) * Φ (y 3) + T (y 0) * R (y 1) * Θ (y 2) * (deriv Φ (y 3) * v 3) := by
  rw [show sep4 T R Θ Φ = fun y => T (y 0) * R (y 1) * Θ (y 2) * Φ (y 3) from rfl,
    (show HasFDerivAt (fun y : Fin 4 → ℝ => T (y 0) * R (y 1) * Θ (y 2) * Φ (y 3)) _ y from
      (((fd_coord_i 0 ((hT.differentiable (by simp)) (y 0))).mul (fd_coord_i 1 ((hR.differentiable (by simp)) (y 1)))).mul
      (fd_coord_i 2 ((hΘ.differentiable (by simp)) (y 2)))).mul
      (fd_coord_i 3 ((hΦ.differentiable (by simp)) (y 3)))).fderiv]
  simp; ring

lemma d_smooth {k : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) : ContDiff ℝ ∞ (deriv k) := (contDiff_infty_iff_deriv.1 hk).2

include hT hR hΘ hΦ in
/-- The pure second partials of `sep4`: each is `sep4` with one factor differentiated twice. -/
lemma sep4_d2 (p : Fin 4 → ℝ) (i : Fin 4) :
    fderiv ℝ (fun y => fderiv ℝ (sep4 T R Θ Φ) y (Pi.single i 1)) p (Pi.single i 1)
      = (![deriv (deriv T) (p 0) * R (p 1) * Θ (p 2) * Φ (p 3), T (p 0) * deriv (deriv R) (p 1) * Θ (p 2) * Φ (p 3),
          T (p 0) * R (p 1) * deriv (deriv Θ) (p 2) * Φ (p 3), T (p 0) * R (p 1) * Θ (p 2) * deriv (deriv Φ) (p 3)]
          : Fin 4 → ℝ) i := by
  fin_cases i
  · show fderiv ℝ (fun y => fderiv ℝ (sep4 T R Θ Φ) y (Pi.single 0 1)) p (Pi.single 0 1) = _
    have e : (fun y => fderiv ℝ (sep4 T R Θ Φ) y (Pi.single 0 1)) = sep4 (deriv T) R Θ Φ := funext fun y => by
      rw [sep4_fd hT hR hΘ hΦ]; simp [sep4]
    rw [e, sep4_fd (d_smooth hT) hR hΘ hΦ]; simp
  · show fderiv ℝ (fun y => fderiv ℝ (sep4 T R Θ Φ) y (Pi.single 1 1)) p (Pi.single 1 1) = _
    have e : (fun y => fderiv ℝ (sep4 T R Θ Φ) y (Pi.single 1 1)) = sep4 T (deriv R) Θ Φ := funext fun y => by
      rw [sep4_fd hT hR hΘ hΦ]; simp [sep4]
    rw [e, sep4_fd hT (d_smooth hR) hΘ hΦ]; simp
  · show fderiv ℝ (fun y => fderiv ℝ (sep4 T R Θ Φ) y (Pi.single 2 1)) p (Pi.single 2 1) = _
    have e : (fun y => fderiv ℝ (sep4 T R Θ Φ) y (Pi.single 2 1)) = sep4 T R (deriv Θ) Φ := funext fun y => by
      rw [sep4_fd hT hR hΘ hΦ]; simp [sep4]
    rw [e, sep4_fd hT hR (d_smooth hΘ) hΦ]; simp
  · show fderiv ℝ (fun y => fderiv ℝ (sep4 T R Θ Φ) y (Pi.single 3 1)) p (Pi.single 3 1) = _
    have e : (fun y => fderiv ℝ (sep4 T R Θ Φ) y (Pi.single 3 1)) = sep4 T R Θ (deriv Φ) := funext fun y => by
      rw [sep4_fd hT hR hΘ hΦ]; simp [sep4]
    rw [e, sep4_fd hT hR hΘ (d_smooth hΦ)]; simp

include hF hP hS hF0 hP0 hS0 hT hR hΘ hΦ in
/-- **Row 95 (B), the separation.** On `−F dt² + dr²/F + P(dθ² + S dφ²)` with `P = r²`, `S = sin²θ` near the point,
THE connection's wave operator on `T(t) R(r) Θ(θ) Φ(φ)` with `T″ = −w²T`, `Φ″ = −m²Φ` and the associated Legendre
equation `Θ″ + cot θ Θ′ − m²Θ/sin²θ = −L Θ` is `T Θ Φ (w²R/F + F R″ + (F′ + 2F/r) R′ − L R/r²)`: `θ` and `φ` drop
out, and `m` enters only through `L`. -/
theorem sph_wave_sep {w m L : ℝ} (p : Fin 4 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2)
    (hTe : deriv (deriv T) (p 0) = -w ^ 2 * T (p 0)) (hΦe : deriv (deriv Φ) (p 3) = -m ^ 2 * Φ (p 3))
    (hΘe : deriv (deriv Θ) (p 2) + Real.cos (p 2) / Real.sin (p 2) * deriv Θ (p 2)
      - m ^ 2 * Θ (p 2) / Real.sin (p 2) ^ 2 = -L * Θ (p 2)) :
    boxD (ndOf (diag4 (cSph F P S)) (diag4_symm _) (fun p u h => diag4_nondeg (fun i => cSph_ne hF0 hP0 hS0 i p) u h)
      ((diag4_smooth (cSph_smooth hF hP hS hF0)).differentiable (by simp))) (cSph F P S) (sep4 T R Θ Φ) p
      = T (p 0) * Θ (p 2) * Φ (p 3) * (w ^ 2 * R (p 1) / F (p 1) + F (p 1) * deriv (deriv R) (p 1)
        + (deriv F (p 1) + 2 * F (p 1) / p 1) * deriv R (p 1) - L * R (p 1) / p 1 ^ 2) := by
  have hr : p 1 ≠ 0 := fun h => hP0 (p 1) (by rw [eP.eq_of_nhds, h]; simp)
  have hsn : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [eS.eq_of_nhds, h]; simp)
  have hPv : P (p 1) = p 1 ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P (p 1) = 2 * p 1 := by rw [eP.deriv_eq]; simp
  have hSv : S (p 2) = Real.sin (p 2) ^ 2 := eS.eq_of_nhds
  have hS1 : deriv S (p 2) = 2 * Real.sin (p 2) * Real.cos (p 2) := by
    rw [eS.deriv_eq, (show HasDerivAt (fun s => Real.sin s ^ 2) _ (p 2) from (Real.hasDerivAt_sin (p 2)).pow 2).deriv]
    simp
  have hf := hF0 (p 1)
  simp only [boxD, Fin.sum_univ_four, lcConn_const, lcGam_diag4 (cSph_ne hF0 hP0 hS0) (cSph_smooth hF hP hS hF0),
    sep4_d2 hT hR hΘ hΦ]
  simp only [gamD, Fin.sum_univ_four, cSph_d1 hF hP hS hF0, sep4_fd hT hR hΘ hΦ]
  simp [cSph, hPv, hP1, hSv, hS1]
  have hΘe' : deriv (deriv Θ) (p 2) = -L * Θ (p 2) - Real.cos (p 2) / Real.sin (p 2) * deriv Θ (p 2)
      + m ^ 2 * Θ (p 2) / Real.sin (p 2) ^ 2 := by linarith
  rw [hTe, hΦe, hΘe']
  field_simp
  ring

end Row95Wave

/-- The associated Legendre operator at `θ`: `Θ″ + cot θ Θ′ − m²Θ/sin²θ`, for `Θ` given with its two derivatives. -/
noncomputable def legOp (m θ Θ0 Θ1 Θ2 : ℝ) : ℝ := Θ2 + Real.cos θ / Real.sin θ * Θ1 - m ^ 2 * Θ0 / Real.sin θ ^ 2

lemma legOp_iff {m L θ Θ0 Θ1 Θ2 : ℝ} (hs : Real.sin θ ≠ 0) :
    legOp m θ Θ0 Θ1 Θ2 = -L * Θ0 ↔
      Real.sin θ ^ 2 * Θ2 + Real.cos θ * Real.sin θ * Θ1 - m ^ 2 * Θ0 + L * Real.sin θ ^ 2 * Θ0 = 0 := by
  unfold legOp
  constructor <;> intro h
  · field_simp at h; linear_combination h
  · field_simp; linear_combination h

/-! **Row 95 (C).** The receipt's nine harmonics `ℓ = 1, 2, 3`, `m = 0..ℓ`, as real associated Legendre functions
`Θ_ℓm(θ)`. Each satisfies the eigen-equation `sph_wave_sep` needs, with `L = ℓ(ℓ + 1)`, and its derivatives are
PROVED, not supplied. With `Φ = cos mφ` the wave operator separates with the same radial operator for every `m`. -/

/-- `Θ_10`: `Θ″ + cot θ Θ′ − 0²Θ/sin²θ = −2Θ`. -/
theorem harm_1_0 (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    deriv (deriv (fun t => Real.cos t)) θ + Real.cos θ / Real.sin θ * deriv (fun t => Real.cos t) θ
      - (0 : ℝ) ^ 2 * (Real.cos θ) / Real.sin θ ^ 2 = -(2 : ℝ) * (Real.cos θ) := by
  have d1 : deriv (fun t => Real.cos t) = fun t => -Real.sin t := by
    funext t; simp (disch := fun_prop)
  have d2 : deriv (fun t => -Real.sin t) θ = -Real.cos θ := by
    simp (disch := fun_prop)
  rw [d1, d2]
  exact (legOp_iff (m := 0) (L := 2) hs).2 (by linear_combination (0) * (Real.sin_sq_add_cos_sq θ))

/-- `Θ_11`: `Θ″ + cot θ Θ′ − 1²Θ/sin²θ = −2Θ`. -/
theorem harm_1_1 (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    deriv (deriv (fun t => Real.sin t)) θ + Real.cos θ / Real.sin θ * deriv (fun t => Real.sin t) θ
      - (1 : ℝ) ^ 2 * (Real.sin θ) / Real.sin θ ^ 2 = -(2 : ℝ) * (Real.sin θ) := by
  have d1 : deriv (fun t => Real.sin t) = fun t => Real.cos t := by
    funext t; simp (disch := fun_prop)
  have d2 : deriv (fun t => Real.cos t) θ = -Real.sin θ := by
    simp (disch := fun_prop)
  rw [d1, d2]
  exact (legOp_iff (m := 1) (L := 2) hs).2 (by linear_combination (Real.sin θ) * (Real.sin_sq_add_cos_sq θ))

/-- `Θ_20`: `Θ″ + cot θ Θ′ − 0²Θ/sin²θ = −6Θ`. -/
theorem harm_2_0 (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    deriv (deriv (fun t => 3*Real.cos t^2 - 1)) θ + Real.cos θ / Real.sin θ * deriv (fun t => 3*Real.cos t^2 - 1) θ
      - (0 : ℝ) ^ 2 * (3*Real.cos θ^2 - 1) / Real.sin θ ^ 2 = -(6 : ℝ) * (3*Real.cos θ^2 - 1) := by
  have d1 : deriv (fun t => 3*Real.cos t^2 - 1) = fun t => -6*Real.cos t*Real.sin t := by
    funext t; simp (disch := fun_prop); ring
  have d2 : deriv (fun t => -6*Real.cos t*Real.sin t) θ = -6*Real.cos θ^2 + 6*Real.sin θ^2 := by
    simp (disch := fun_prop); ring
  rw [d1, d2]
  exact (legOp_iff (m := 0) (L := 6) hs).2 (by linear_combination (6*Real.sin θ^2) * (Real.sin_sq_add_cos_sq θ))

/-- `Θ_21`: `Θ″ + cot θ Θ′ − 1²Θ/sin²θ = −6Θ`. -/
theorem harm_2_1 (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    deriv (deriv (fun t => Real.cos t*Real.sin t)) θ + Real.cos θ / Real.sin θ * deriv (fun t => Real.cos t*Real.sin t) θ
      - (1 : ℝ) ^ 2 * (Real.cos θ*Real.sin θ) / Real.sin θ ^ 2 = -(6 : ℝ) * (Real.cos θ*Real.sin θ) := by
  have d1 : deriv (fun t => Real.cos t*Real.sin t) = fun t => Real.cos t^2 - Real.sin t^2 := by
    funext t; simp (disch := fun_prop); ring
  have d2 : deriv (fun t => Real.cos t^2 - Real.sin t^2) θ = -4*Real.cos θ*Real.sin θ := by
    simp (disch := fun_prop); ring
  rw [d1, d2]
  exact (legOp_iff (m := 1) (L := 6) hs).2 (by linear_combination (Real.cos θ*Real.sin θ) * (Real.sin_sq_add_cos_sq θ))

/-- `Θ_22`: `Θ″ + cot θ Θ′ − 2²Θ/sin²θ = −6Θ`. -/
theorem harm_2_2 (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    deriv (deriv (fun t => Real.sin t^2)) θ + Real.cos θ / Real.sin θ * deriv (fun t => Real.sin t^2) θ
      - (2 : ℝ) ^ 2 * (Real.sin θ^2) / Real.sin θ ^ 2 = -(6 : ℝ) * (Real.sin θ^2) := by
  have d1 : deriv (fun t => Real.sin t^2) = fun t => 2*Real.cos t*Real.sin t := by
    funext t; simp (disch := fun_prop); ring
  have d2 : deriv (fun t => 2*Real.cos t*Real.sin t) θ = 2*Real.cos θ^2 - 2*Real.sin θ^2 := by
    simp (disch := fun_prop); ring
  rw [d1, d2]
  exact (legOp_iff (m := 2) (L := 6) hs).2 (by linear_combination (4*Real.sin θ^2) * (Real.sin_sq_add_cos_sq θ))

/-- `Θ_30`: `Θ″ + cot θ Θ′ − 0²Θ/sin²θ = −12Θ`. -/
theorem harm_3_0 (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    deriv (deriv (fun t => 5*Real.cos t^3 - 3*Real.cos t)) θ + Real.cos θ / Real.sin θ * deriv (fun t => 5*Real.cos t^3 - 3*Real.cos t) θ
      - (0 : ℝ) ^ 2 * (5*Real.cos θ^3 - 3*Real.cos θ) / Real.sin θ ^ 2 = -(12 : ℝ) * (5*Real.cos θ^3 - 3*Real.cos θ) := by
  have d1 : deriv (fun t => 5*Real.cos t^3 - 3*Real.cos t) = fun t => -15*Real.cos t^2*Real.sin t + 3*Real.sin t := by
    funext t; simp (disch := fun_prop); ring
  have d2 : deriv (fun t => -15*Real.cos t^2*Real.sin t + 3*Real.sin t) θ = -15*Real.cos θ^3 + 30*Real.cos θ*Real.sin θ^2 + 3*Real.cos θ := by
    simp (disch := fun_prop); ring
  rw [d1, d2]
  exact (legOp_iff (m := 0) (L := 12) hs).2 (by linear_combination (30*Real.cos θ*Real.sin θ^2) * (Real.sin_sq_add_cos_sq θ))

/-- `Θ_31`: `Θ″ + cot θ Θ′ − 1²Θ/sin²θ = −12Θ`. -/
theorem harm_3_1 (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    deriv (deriv (fun t => 5*Real.cos t^2*Real.sin t - Real.sin t)) θ + Real.cos θ / Real.sin θ * deriv (fun t => 5*Real.cos t^2*Real.sin t - Real.sin t) θ
      - (1 : ℝ) ^ 2 * (5*Real.cos θ^2*Real.sin θ - Real.sin θ) / Real.sin θ ^ 2 = -(12 : ℝ) * (5*Real.cos θ^2*Real.sin θ - Real.sin θ) := by
  have d1 : deriv (fun t => 5*Real.cos t^2*Real.sin t - Real.sin t) = fun t => 5*Real.cos t^3 - 10*Real.cos t*Real.sin t^2 - Real.cos t := by
    funext t; simp (disch := fun_prop); ring
  have d2 : deriv (fun t => 5*Real.cos t^3 - 10*Real.cos t*Real.sin t^2 - Real.cos t) θ = -35*Real.cos θ^2*Real.sin θ + 10*Real.sin θ^3 + Real.sin θ := by
    simp (disch := fun_prop); ring
  rw [d1, d2]
  exact (legOp_iff (m := 1) (L := 12) hs).2 (by linear_combination (5*Real.cos θ^2*Real.sin θ + 10*Real.sin θ^3 - Real.sin θ) * (Real.sin_sq_add_cos_sq θ))

/-- `Θ_32`: `Θ″ + cot θ Θ′ − 2²Θ/sin²θ = −12Θ`. -/
theorem harm_3_2 (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    deriv (deriv (fun t => Real.cos t*Real.sin t^2)) θ + Real.cos θ / Real.sin θ * deriv (fun t => Real.cos t*Real.sin t^2) θ
      - (2 : ℝ) ^ 2 * (Real.cos θ*Real.sin θ^2) / Real.sin θ ^ 2 = -(12 : ℝ) * (Real.cos θ*Real.sin θ^2) := by
  have d1 : deriv (fun t => Real.cos t*Real.sin t^2) = fun t => 2*Real.cos t^2*Real.sin t - Real.sin t^3 := by
    funext t; simp (disch := fun_prop); ring
  have d2 : deriv (fun t => 2*Real.cos t^2*Real.sin t - Real.sin t^3) θ = 2*Real.cos θ^3 - 7*Real.cos θ*Real.sin θ^2 := by
    simp (disch := fun_prop); ring
  rw [d1, d2]
  exact (legOp_iff (m := 2) (L := 12) hs).2 (by linear_combination (4*Real.cos θ*Real.sin θ^2) * (Real.sin_sq_add_cos_sq θ))

/-- `Θ_33`: `Θ″ + cot θ Θ′ − 3²Θ/sin²θ = −12Θ`. -/
theorem harm_3_3 (θ : ℝ) (hs : Real.sin θ ≠ 0) :
    deriv (deriv (fun t => Real.sin t^3)) θ + Real.cos θ / Real.sin θ * deriv (fun t => Real.sin t^3) θ
      - (3 : ℝ) ^ 2 * (Real.sin θ^3) / Real.sin θ ^ 2 = -(12 : ℝ) * (Real.sin θ^3) := by
  have d1 : deriv (fun t => Real.sin t^3) = fun t => 3*Real.cos t*Real.sin t^2 := by
    funext t; simp (disch := fun_prop); ring
  have d2 : deriv (fun t => 3*Real.cos t*Real.sin t^2) θ = 6*Real.cos θ^2*Real.sin θ - 3*Real.sin θ^3 := by
    simp (disch := fun_prop); ring
  rw [d1, d2]
  exact (legOp_iff (m := 3) (L := 12) hs).2 (by linear_combination (9*Real.sin θ^3) * (Real.sin_sq_add_cos_sq θ))

/-- **Row 95 (D).** `L(L + 2) = 4j(j + 1)` at `j = L/2`: the `S³` level `L` is the pair of `SU(2)` spins `j = L/2`. -/
theorem s3_levels (L : ℝ) : L * (L + 2) = 4 * (L / 2) * (L / 2 + 1) := by ring

end ShadowProbe

#print axioms ShadowProbe.killF95_model
#print axioms ShadowProbe.cot_has
#print axioms ShadowProbe.rotA_fd
#print axioms ShadowProbe.rotB_fd
#print axioms ShadowProbe.cSph_smooth
#print axioms ShadowProbe.cSph_ne
#print axioms ShadowProbe.cSph_d1
#print axioms ShadowProbe.so3_killing
#print axioms ShadowProbe.sep4_fd
#print axioms ShadowProbe.d_smooth
#print axioms ShadowProbe.sep4_d2
#print axioms ShadowProbe.sph_wave_sep
#print axioms ShadowProbe.legOp_iff
#print axioms ShadowProbe.harm_1_0
#print axioms ShadowProbe.harm_1_1
#print axioms ShadowProbe.harm_2_0
#print axioms ShadowProbe.harm_2_1
#print axioms ShadowProbe.harm_2_2
#print axioms ShadowProbe.harm_3_0
#print axioms ShadowProbe.harm_3_1
#print axioms ShadowProbe.harm_3_2
#print axioms ShadowProbe.harm_3_3
#print axioms ShadowProbe.s3_levels

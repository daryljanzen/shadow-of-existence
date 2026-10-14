import ShadowEngine

/-! # The second seat's Kantowski–Sachs row (`r7333+70`): 54

`−dτ² + X(τ)²dχ² + Y(τ)²(dθ² + sin²θ dφ²)` in `(τ, χ, θ, φ)`, with `X, Y` free, smooth and nowhere zero, and the
angular profile `S = sin²θ` near the point (the convention, `exists_global_family`). The receipt `P09_ks_vacuum`
TAKES the three stress-energy combinations below as given; here they are DERIVED as THE connection's mixed Einstein
components. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

/-! ### `r7333` instance 7, row 54: `8πρ = −(G^τ_τ + Λ) = −Λ + (Y′/Y)² + 1/Y² + 2X′Y′/(XY)`,
`8πp_χ = G^χ_χ + Λ = Λ − 2Y″/Y − (Y′/Y)² − 1/Y²`, `8πp_⊥ = G^θ_θ + Λ = Λ − Y″/Y − X″/X − X′Y′/(XY)` -/

section Inst_R54

set_option synthInstance.maxHeartbeats 400000

noncomputable def cKS (X Y S : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun _ => -1, fun y => X (y 0) ^ 2, fun y => Y (y 0) ^ 2, fun y => Y (y 0) ^ 2 * S (y 2)]

variable {X Y S : ℝ → ℝ} (hX : ContDiff ℝ ∞ X) (hY : ContDiff ℝ ∞ Y) (hS : ContDiff ℝ ∞ S)
  (hX0 : ∀ s, X s ≠ 0) (hY0 : ∀ s, Y s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hX hY hS in
lemma cKS_smooth (k : Fin 4) : ContDiff ℝ ∞ (cKS X Y S k) := by
  fin_cases k
  · exact contDiff_const
  · exact (hX.comp (contDiff_apply ℝ ℝ 0)).pow 2
  · exact (hY.comp (contDiff_apply ℝ ℝ 0)).pow 2
  · exact ((hY.comp (contDiff_apply ℝ ℝ 0)).pow 2).mul (hS.comp (contDiff_apply ℝ ℝ 2))
include hX0 hY0 hS0 in
lemma cKS_ne (k : Fin 4) (p : Fin 4 → ℝ) : cKS X Y S k p ≠ 0 := by
  fin_cases k <;> simp [cKS, hX0, hY0, hS0]

/-- The mixed Einstein component `G^j_j` of `cKS` under THE connection. -/
noncomputable def GKS (hX : ContDiff ℝ ∞ X) (hY : ContDiff ℝ ∞ Y) (hS : ContDiff ℝ ∞ S)
    (hX0 : ∀ s, X s ≠ 0) (hY0 : ∀ s, Y s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (p : Fin 4 → ℝ) (j : Fin 4) : ℝ :=
  einsteinC (fun i => cKS X Y S i p) (fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cKS X Y S))
    (diag4_symm _) (fun p u h => diag4_nondeg (fun i => cKS_ne hX0 hY0 hS0 i p) u h)
    ((diag4_smooth (cKS_smooth hX hY hS)).differentiable (by simp))))
    (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
    (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p) j j / cKS X Y S j p

/-- `(h²)′ = 2hh′` and `(h²)″ = 2h′² + 2hh″`. -/
lemma sq_derivs {h : ℝ → ℝ} (hs : ContDiff ℝ ∞ h) (t : ℝ) :
    deriv (fun s => h s ^ 2) t = 2 * h t * deriv h t
      ∧ deriv (deriv (fun s => h s ^ 2)) t = 2 * deriv h t ^ 2 + 2 * h t * deriv (deriv h) t := by
  have d0 : ∀ s, HasDerivAt h (deriv h s) s := fun s => ((hs.differentiable (by simp)) s).hasDerivAt
  have d1 : ∀ s, HasDerivAt (deriv h) (deriv (deriv h) s) s := fun s =>
    (((contDiff_infty_iff_deriv.1 hs).2.differentiable (by simp)) s).hasDerivAt
  have e : deriv (fun s => h s ^ 2) = fun s => 2 * h s * deriv h s :=
    funext fun s => ((d0 s).pow 2).deriv.trans (by simp)
  refine ⟨congrFun e t, ?_⟩
  rw [e]
  have := (show HasDerivAt (fun s => 2 * h s * deriv h s) _ t from ((d0 t).const_mul 2).mul (d1 t))
  rw [this.deriv]; ring

open Filter Topology in
set_option maxHeartbeats 8000000 in
include hX hY hS hX0 hY0 hS0 in
/-- **Row 54.** -/
theorem ks_stress (Λ : ℝ) (p : Fin 4 → ℝ) (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    let t := p 0
    let X1 := deriv X t / X t
    let Y1 := deriv Y t / Y t;
    -(GKS hX hY hS hX0 hY0 hS0 p 0 + Λ) = -Λ + Y1 ^ 2 + 1 / Y t ^ 2 + 2 * X1 * Y1
      ∧ GKS hX hY hS hX0 hY0 hS0 p 1 + Λ = Λ - 2 * (deriv (deriv Y) t / Y t) - Y1 ^ 2 - 1 / Y t ^ 2
      ∧ GKS hX hY hS hX0 hY0 hS0 p 2 + Λ
        = Λ - deriv (deriv Y) t / Y t - deriv (deriv X) t / X t - X1 * Y1 := by
  intro t X1 Y1
  obtain ⟨x1, x2⟩ := sq_derivs hX t
  obtain ⟨y1, y2⟩ := sq_derivs hY t
  have sd : ∀ s, HasDerivAt (fun s => Real.sin s ^ 2) (2 * Real.sin s * Real.cos s) s := fun s =>
    (show HasDerivAt (fun s => Real.sin s ^ 2) _ s from (Real.hasDerivAt_sin s).pow 2).congr_deriv (by norm_num)
  have hSv : S (p 2) = Real.sin (p 2) ^ 2 := eS.eq_of_nhds
  have hS1 : deriv S (p 2) = 2 * Real.sin (p 2) * Real.cos (p 2) := by rw [eS.deriv_eq, (sd _).deriv]
  have hS2 : deriv (deriv S) (p 2) = 2 * Real.cos (p 2) ^ 2 - 2 * Real.sin (p 2) ^ 2 := by
    have e3 : deriv S =ᶠ[𝓝 (p 2)] fun s => 2 * Real.sin s * Real.cos s :=
      eS.deriv.trans (Eventually.of_forall fun s => (sd s).deriv)
    rw [e3.deriv_eq]
    have := (show HasDerivAt (fun s => 2 * Real.sin s * Real.cos s) _ (p 2) from
      ((Real.hasDerivAt_sin (p 2)).const_mul 2).mul (Real.hasDerivAt_cos (p 2)))
    rw [this.deriv]; ring
  have hXs : ContDiff ℝ ∞ (fun s => X s ^ 2) := hX.pow 2
  have hYs : ContDiff ℝ ∞ (fun s => Y s ^ 2) := hY.pow 2
  have hD1 : ∀ k v, fderiv ℝ (cKS X Y S k) p v = (![0, 2 * X t * deriv X t * v 0, 2 * Y t * deriv Y t * v 0,
      2 * Y t * deriv Y t * v 0 * S (p 2) + Y t ^ 2 * (deriv S (p 2) * v 2)] : Fin 4 → ℝ) k := fun k v => by
    fin_cases k
    · simp [cKS]
    · show fderiv ℝ (fun y => (fun s => X s ^ 2) (y 0)) p v = _
      rw [co_d1 hXs]; simp [t, x1]
    · show fderiv ℝ (fun y => (fun s => Y s ^ 2) (y 0)) p v = _
      rw [co_d1 hYs]; simp [t, y1]
    · show fderiv ℝ (fun y => (fun s => Y s ^ 2) (y 0) * S (y 2)) p v = _
      rw [pr_d1 hYs hS]; simp [t, y1]
  have hD2 : ∀ k u v, fderiv ℝ (fderiv ℝ (cKS X Y S k)) p u v = (![0,
      (2 * deriv X t ^ 2 + 2 * X t * deriv (deriv X) t) * u 0 * v 0,
      (2 * deriv Y t ^ 2 + 2 * Y t * deriv (deriv Y) t) * u 0 * v 0,
      (2 * deriv Y t ^ 2 + 2 * Y t * deriv (deriv Y) t) * u 0 * v 0 * S (p 2)
        + 2 * Y t * deriv Y t * v 0 * (deriv S (p 2) * u 2) + 2 * Y t * deriv Y t * u 0 * (deriv S (p 2) * v 2)
        + Y t ^ 2 * (deriv (deriv S) (p 2) * u 2 * v 2)] : Fin 4 → ℝ) k := fun k u v => by
    fin_cases k
    · simp [cKS]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => X s ^ 2) (y 0))) p u v = _
      rw [co_d2 hXs]; simp [t, x2]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => Y s ^ 2) (y 0))) p u v = _
      rw [co_d2 hYs]; simp [t, y2]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => Y s ^ 2) (y 0) * S (y 2))) p u v = _
      rw [pr_d2 hYs hS]; simp [t, y1, y2]
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have hx : X (p 0) ≠ 0 := hX0 _; have hy : Y (p 0) ≠ 0 := hY0 _
  simp only [GKS, einsteinC, scalC, ricC, Fin.sum_univ_four,
    curvD_eq (cKS_ne hX0 hY0 hS0) (cKS_smooth hX hY hS)]
  simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
  simp [cKS, Fin.sum_univ_four, hSv, hS1, hS2, X1, Y1, t]
  refine ⟨?_, ?_, ?_⟩ <;> (field_simp; try ring)

end Inst_R54

#print axioms ks_stress

end ShadowProbe

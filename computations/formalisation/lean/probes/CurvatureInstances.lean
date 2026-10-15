import ShadowEngine

/-! # The engine's instances, split out of `CurvatureProbe.lean` at `r7327+71.4`

`ShadowEngine` holds the engine core, E2, E5, the coordinate recipe and the cutoff lemma, and is built once with
`lake build ShadowEngine`. This file holds the instances that use it (E3, E4, and rows 52, 79, 75, 45), so a seat
writing an instance builds only its own file. Nothing is changed in any statement or proof by the move. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

/-! ### E3 — acceptance instance 1, row 2's `k = −1`: open FRW in a horospherical chart,
`−dt² + a(t)²(dw² + e^{2w}(dx² + dy²))`, has `Weyl² = 0` for a FREE `a` under THE connection -/

section Engine4D_E3

set_option synthInstance.maxHeartbeats 400000

noncomputable def FoF (a : ℝ → ℝ) : Fin 4 → ℝ → ℝ := ![fun _ => -1, fun s => a s ^ 2, fun s => a s ^ 2, fun s => a s ^ 2]
noncomputable def GoF : Fin 4 → ℝ → ℝ := ![fun _ => 1, fun _ => 1, fun w => Real.exp (2 * w), fun w => Real.exp (2 * w)]

variable {a : ℝ → ℝ} (ha : ∀ s, a s ≠ 0) (has : ContDiff ℝ ∞ a)

include has in
lemma FoF_smooth (k : Fin 4) : ContDiff ℝ ∞ (FoF a k) := by fin_cases k <;> simp [FoF] <;> fun_prop
lemma GoF_smooth (k : Fin 4) : ContDiff ℝ ∞ (GoF k) := by fin_cases k <;> simp [GoF] <;> fun_prop
include ha in
lemma oF_ne (k : Fin 4) (p : Fin 4 → ℝ) : cS (FoF a) GoF k p ≠ 0 := by
  fin_cases k <;> simp [cS, FoF, GoF, ha, Real.exp_ne_zero]

/-- The open-FRW Riemann table `R(eᵢ,eⱼ)eₖ` component `l`, in `A = a`, `A1 = ȧ`, `A2 = ä`, `E = e^{2w}`. -/
noncomputable def oR (A A1 A2 E : ℝ) (i j k l : Fin 4) : ℝ :=
  let γ : Fin 4 → ℝ := ![0, 1, E, E]
  if i = 0 ∧ j ≠ 0 ∧ k = 0 ∧ l = j then A2 / A
  else if j = 0 ∧ i ≠ 0 ∧ k = 0 ∧ l = i then -(A2 / A)
  else if i = 0 ∧ j ≠ 0 ∧ k = j ∧ l = 0 then A * A2 * γ j
  else if j = 0 ∧ i ≠ 0 ∧ k = i ∧ l = 0 then -(A * A2 * γ i)
  else if i ≠ 0 ∧ j ≠ 0 ∧ i ≠ j ∧ k = i ∧ l = j then (1 - A1 ^ 2) * γ i
  else if i ≠ 0 ∧ j ≠ 0 ∧ i ≠ j ∧ k = j ∧ l = i then -((1 - A1 ^ 2) * γ j)
  else 0

set_option maxHeartbeats 4000000 in
include ha has in
/-- **E3, row 2 (`k = −1`).** THE connection's curvature of open FRW is the table `oR`, and `Weyl² = 0`. -/
theorem open_frw_weyl (p : Fin 4 → ℝ) :
    weyl2C (fun i => cS (FoF a) GoF i p) (fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cS (FoF a) GoF))
      (diag4_symm _) (fun p u h => diag4_nondeg (fun i => oF_ne ha i p) u h)
      ((diag4_smooth (cS_smooth (FoF_smooth has) GoF_smooth)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p) = 0 := by
  have d0 : ∀ s, HasDerivAt a (deriv a s) s := fun s => ((has.differentiable (by simp)) s).hasDerivAt
  have d1 : ∀ s, HasDerivAt (deriv a) (deriv (deriv a) s) s := fun s =>
    (((contDiff_infty_iff_deriv.1 has).2.differentiable (by simp)) s).hasDerivAt
  have e1 : deriv (fun s => a s ^ 2) = fun s => 2 * a s * deriv a s :=
    funext fun s => ((d0 s).pow 2).deriv.trans (by simp)
  have e2 : deriv (fun s => 2 * a s * deriv a s) = fun s => 2 * deriv a s ^ 2 + 2 * a s * deriv (deriv a) s :=
    funext fun s => (((d0 s).const_mul 2).mul (d1 s)).deriv.trans (by ring)
  have x1 : ∀ w, HasDerivAt (fun w => Real.exp (2 * w)) (2 * Real.exp (2 * w)) w := fun w =>
    HasDerivAt.congr_deriv (((hasDerivAt_id' w).const_mul 2).exp) (by ring)
  have f1 : deriv (fun w => Real.exp (2 * w)) = fun w => 2 * Real.exp (2 * w) := funext fun w => (x1 w).deriv
  have f2 : deriv (fun w => 2 * Real.exp (2 * w)) = fun w => 4 * Real.exp (2 * w) :=
    funext fun w => (((x1 w).const_mul 2)).deriv.trans (by ring)
  have h1 := fun k v => dC1_cS (FoF_smooth has) GoF_smooth p k v
  have h2 := fun k u v => dC2_cS (FoF_smooth has) GoF_smooth p k u v
  have h1' : ∀ k v, fderiv ℝ (cS (FoF a) GoF k) p v = _ := fun k v => h1 k v
  have hA := ha (p 0)
  have hDF : ∀ k, deriv (FoF a k) (p 0) = (![0, 2 * a (p 0) * deriv a (p 0), 2 * a (p 0) * deriv a (p 0),
      2 * a (p 0) * deriv a (p 0)] : Fin 4 → ℝ) k := fun k => by
    fin_cases k
    exacts [deriv_const _ _, congrFun e1 _, congrFun e1 _, congrFun e1 _]
  have hDDF : ∀ k, deriv (deriv (FoF a k)) (p 0) = (![0, 2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0),
      2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0),
      2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0)] : Fin 4 → ℝ) k := fun k => by
    fin_cases k
    · show deriv (deriv fun _ : ℝ => (-1 : ℝ)) (p 0) = 0; simp
    all_goals (show deriv (deriv fun s => a s ^ 2) (p 0) = _; rw [e1, e2]; rfl)
  have hDG : ∀ k, deriv (GoF k) (p 1) = (![0, 0, 2 * Real.exp (2 * p 1), 2 * Real.exp (2 * p 1)] : Fin 4 → ℝ) k :=
    fun k => by
    fin_cases k
    exacts [deriv_const _ _, deriv_const _ _, (x1 _).deriv, (x1 _).deriv]
  have hDDG : ∀ k, deriv (deriv (GoF k)) (p 1)
      = (![0, 0, 4 * Real.exp (2 * p 1), 4 * Real.exp (2 * p 1)] : Fin 4 → ℝ) k := fun k => by
    fin_cases k
    · show deriv (deriv fun _ : ℝ => (1 : ℝ)) (p 1) = 0; simp
    · show deriv (deriv fun _ : ℝ => (1 : ℝ)) (p 1) = 0; simp
    all_goals (show deriv (deriv fun w => Real.exp (2 * w)) (p 1) = _; rw [f1, f2]; rfl)
  have hT : ∀ i j k l, curvD (cS (FoF a) GoF) p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l
      = oR (a (p 0)) (deriv a (p 0)) (deriv (deriv a) (p 0)) (Real.exp (2 * p 1)) i j k l := by
    intro i j k l
    fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
      (simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, h1', h1, h2, hDF, hDDF, hDG, hDDG]
       simp [cS, FoF, GoF, oR, Fin.sum_univ_four]
       try (field_simp; ring))
  simp only [weyl2C, riem2C, ric2C, scalC, ricC, curvD_eq (oF_ne ha) (cS_smooth (FoF_smooth has) GoF_smooth), hT]
  simp [Fin.sum_univ_four, oR, cS, FoF, GoF]
  field_simp; ring

end Engine4D_E3

/-! ### E4 — acceptance instance 2, row 74: the homogeneous Gowdy–de Sitter metric
`e^{2(γ−ψ)}(−dt² + dz²) + e^{2ψ}dx² + R²e^{−2ψ}dy²` (`ψ, γ, R` of `t`). With `E = G + Λg` from THE connection,
`R(E_tt − E_zz) = AREA` and `R e^{2(γ−ψ)}(e^{−2ψ}E_xx − e^{2ψ}E_yy/R²) = 2 WAVE − AREA`, so the field equations give
`AREA = WAVE = 0`, and the shear charge `C₀ = Ṙ − 2Rψ̇` has `Ċ₀ = AREA − 2 WAVE`: conserved on shell -/

section Engine4D_E4

set_option synthInstance.maxHeartbeats 400000

noncomputable def FgW (ψ γ R : ℝ → ℝ) : Fin 4 → ℝ → ℝ :=
  ![fun s => -Real.exp (2 * (γ s - ψ s)), fun s => Real.exp (2 * (γ s - ψ s)), fun s => Real.exp (2 * ψ s),
    fun s => R s ^ 2 * Real.exp (-(2 * ψ s))]
def GgW : Fin 4 → ℝ → ℝ := fun _ _ => 1

/-- `(e^h)′ = h′e^h`, `(e^h)″ = (h″ + h′²)e^h`. -/
lemma exp_derivs {h : ℝ → ℝ} (hs : ContDiff ℝ ∞ h) :
    deriv (fun s => Real.exp (h s)) = (fun s => deriv h s * Real.exp (h s))
    ∧ deriv (fun s => deriv h s * Real.exp (h s))
      = fun s => (deriv (deriv h) s + deriv h s ^ 2) * Real.exp (h s) := by
  have d0 : ∀ s, HasDerivAt h (deriv h s) s := fun s => ((hs.differentiable (by simp)) s).hasDerivAt
  have d1 : ∀ s, HasDerivAt (deriv h) (deriv (deriv h) s) s := fun s =>
    (((contDiff_infty_iff_deriv.1 hs).2.differentiable (by simp)) s).hasDerivAt
  exact ⟨funext fun s => ((d0 s).exp).deriv.trans (by ring),
    funext fun s => (((d1 s).mul (d0 s).exp)).deriv.trans (by ring)⟩

variable {ψ γ R : ℝ → ℝ} (hψ : ContDiff ℝ ∞ ψ) (hγ : ContDiff ℝ ∞ γ) (hR : ContDiff ℝ ∞ R) (hR0 : ∀ s, R s ≠ 0)

include hψ hγ hR in
lemma FgW_smooth (k : Fin 4) : ContDiff ℝ ∞ (FgW ψ γ R k) := by fin_cases k <;> simp [FgW] <;> fun_prop
lemma GgW_smooth (k : Fin 4) : ContDiff ℝ ∞ (GgW k) := contDiff_const
include hR0 in
lemma gW_ne (k : Fin 4) (p : Fin 4 → ℝ) : cS (FgW ψ γ R) GgW k p ≠ 0 := by
  fin_cases k <;> simp [cS, FgW, GgW, Real.exp_ne_zero, hR0]

set_option maxHeartbeats 4000000 in
include hψ hγ hR hR0 in
/-- **E4, row 74.** -/
theorem gowdy_ds_field (Λ : ℝ) (p : Fin 4 → ℝ) :
    let Rf := fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cS (FgW ψ γ R) GgW)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => gW_ne hR0 i p) u h)
      ((diag4_smooth (cS_smooth (FgW_smooth hψ hγ hR) GgW_smooth)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p
    let g := fun i => cS (FgW ψ γ R) GgW i p
    let E := fun j => einsteinC g Rf j j + Λ * g j
    let s := p 0
    let ex := Real.exp (2 * (γ s - ψ s))
    let WAVE := deriv R s * deriv ψ s + R s * deriv (deriv ψ) s - Λ * R s * ex
    let AREA := deriv (deriv R) s - 2 * Λ * R s * ex
    R s * (E 0 - E 1) = AREA
      ∧ R s * ex * (Real.exp (-(2 * ψ s)) * E 2 - Real.exp (2 * ψ s) * E 3 / R s ^ 2) = 2 * WAVE - AREA := by
  intro Rf g E s ex WAVE AREA
  have D : ∀ {f : ℝ → ℝ}, ContDiff ℝ ∞ f → ∀ t, HasDerivAt f (deriv f t) t ∧ HasDerivAt (deriv f) (deriv (deriv f) t) t :=
    fun hf t => ⟨((contDiff_infty_iff_deriv.1 hf).1 t).hasDerivAt,
      (((contDiff_infty_iff_deriv.1 hf).2.differentiable (by simp)) t).hasDerivAt⟩
  -- the exponents and their derivatives, at every point
  have H0 : ∀ t, HasDerivAt (fun t => 2 * (γ t - ψ t)) (2 * (deriv γ t - deriv ψ t)) t :=
    fun t => (((D hγ t).1).sub ((D hψ t).1)).const_mul 2
  have H0' : ∀ t, HasDerivAt (fun t => 2 * (deriv γ t - deriv ψ t)) (2 * (deriv (deriv γ) t - deriv (deriv ψ) t)) t :=
    fun t => (((D hγ t).2).sub ((D hψ t).2)).const_mul 2
  have H2 : ∀ t, HasDerivAt (fun t => 2 * ψ t) (2 * deriv ψ t) t := fun t => ((D hψ t).1).const_mul 2
  have H2' : ∀ t, HasDerivAt (fun t => 2 * deriv ψ t) (2 * deriv (deriv ψ) t) t := fun t => ((D hψ t).2).const_mul 2
  have H3 : ∀ t, HasDerivAt (fun t => R t ^ 2 * Real.exp (-(2 * ψ t)))
      (2 * R t * deriv R t * Real.exp (-(2 * ψ t)) - R t ^ 2 * (2 * deriv ψ t) * Real.exp (-(2 * ψ t))) t :=
    fun t => (((D hR t).1.pow 2).mul (((D hψ t).1.const_mul 2).neg.exp)).congr_deriv (by simp; ring)
  have dF0 : deriv (fun t => Real.exp (2 * (γ t - ψ t))) = fun t => 2 * (deriv γ t - deriv ψ t) * Real.exp (2 * (γ t - ψ t)) :=
    funext fun t => ((H0 t).exp).deriv.trans (by ring)
  have dF0n : deriv (fun t => -Real.exp (2 * (γ t - ψ t))) = fun t => -(2 * (deriv γ t - deriv ψ t) * Real.exp (2 * (γ t - ψ t))) :=
    funext fun t => ((H0 t).exp.neg).deriv.trans (by ring)
  have dF2 : deriv (fun t => Real.exp (2 * ψ t)) = fun t => 2 * deriv ψ t * Real.exp (2 * ψ t) :=
    funext fun t => ((H2 t).exp).deriv.trans (by ring)
  have dF3 : deriv (fun t => R t ^ 2 * Real.exp (-(2 * ψ t))) = fun t =>
      2 * R t * deriv R t * Real.exp (-(2 * ψ t)) - R t ^ 2 * (2 * deriv ψ t) * Real.exp (-(2 * ψ t)) :=
    funext fun t => (H3 t).deriv
  have hDF : ∀ k, deriv (FgW ψ γ R k) s = (![-(2 * (deriv γ s - deriv ψ s) * ex), 2 * (deriv γ s - deriv ψ s) * ex,
      2 * deriv ψ s * Real.exp (2 * ψ s),
      2 * R s * deriv R s * Real.exp (-(2 * ψ s)) - R s ^ 2 * (2 * deriv ψ s) * Real.exp (-(2 * ψ s))] : Fin 4 → ℝ) k :=
    fun k => by
    fin_cases k
    exacts [congrFun dF0n s, congrFun dF0 s, congrFun dF2 s, congrFun dF3 s]
  have hDDF : ∀ k, deriv (deriv (FgW ψ γ R k)) s = (![
      -((2 * (deriv (deriv γ) s - deriv (deriv ψ) s) + (2 * (deriv γ s - deriv ψ s)) ^ 2) * ex),
      (2 * (deriv (deriv γ) s - deriv (deriv ψ) s) + (2 * (deriv γ s - deriv ψ s)) ^ 2) * ex,
      (2 * deriv (deriv ψ) s + (2 * deriv ψ s) ^ 2) * Real.exp (2 * ψ s),
      (2 * deriv R s ^ 2 + 2 * R s * deriv (deriv R) s) * Real.exp (-(2 * ψ s))
        - 2 * (2 * R s * deriv R s) * (2 * deriv ψ s) * Real.exp (-(2 * ψ s))
        - R s ^ 2 * (2 * deriv (deriv ψ) s) * Real.exp (-(2 * ψ s))
        + R s ^ 2 * (2 * deriv ψ s) ^ 2 * Real.exp (-(2 * ψ s))] : Fin 4 → ℝ) k := fun k => by
    fin_cases k
    · show deriv (deriv fun t => -Real.exp (2 * (γ t - ψ t))) s = _
      rw [dF0n]; exact (((H0' s).mul (H0 s).exp).neg).deriv.trans (by simp [ex]; ring)
    · show deriv (deriv fun t => Real.exp (2 * (γ t - ψ t))) s = _
      rw [dF0]; exact (((H0' s).mul (H0 s).exp)).deriv.trans (by simp [ex]; ring)
    · show deriv (deriv fun t => Real.exp (2 * ψ t)) s = _
      rw [dF2]; exact (((H2' s).mul (H2 s).exp)).deriv.trans (by simp; ring)
    · show deriv (deriv fun t => R t ^ 2 * Real.exp (-(2 * ψ t))) s = _
      rw [dF3]
      have e3 := ((H2 s).neg.exp)
      have a1 := (((D hR s).1.const_mul 2).mul (D hR s).1).mul e3
      have a2 := ((((D hR s).1.pow 2).mul (H2' s)).mul ((H2 s).neg.exp))
      exact (HasDerivAt.sub (HasDerivAt.mul (HasDerivAt.mul ((D hR s).1.const_mul 2) (D hR s).2) e3)
        (HasDerivAt.mul (HasDerivAt.mul ((D hR s).1.pow 2) (H2' s)) e3)).deriv.trans (by simp; ring)
  have hDG : ∀ k, deriv (GgW k) (p 1) = 0 := fun k => deriv_const _ _
  have hDDG : ∀ k, deriv (deriv (GgW k)) (p 1) = 0 := fun k => by
    show deriv (deriv fun _ : ℝ => (1 : ℝ)) (p 1) = 0; simp
  have h1 := fun k v => dC1_cS (FgW_smooth hψ hγ hR) GgW_smooth p k v
  have h2 := fun k u v => dC2_cS (FgW_smooth hψ hγ hR) GgW_smooth p k u v
  have h1' : ∀ k v, fderiv ℝ (cS (FgW ψ γ R) GgW k) p v = _ := fun k v => h1 k v
  have hRs := hR0 s
  simp only [s, ex] at hDF hDDF
  simp only [Rf, g, E, einsteinC, scalC, ricC, Fin.sum_univ_four,
    curvD_eq (gW_ne hR0) (cS_smooth (FgW_smooth hψ hγ hR) GgW_smooth)]
  simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, h1', h1, h2, hDF, hDDF, hDG, hDDG]
  simp [cS, FgW, GgW, Fin.sum_univ_four, WAVE, AREA, ex, s]
  have hRp : R (p 0) ≠ 0 := hR0 _
  have hx : Real.exp (-(2 * ψ (p 0))) * Real.exp (2 * ψ (p 0)) = 1 := by rw [← Real.exp_add]; simp
  constructor
  · field_simp; ring
  · field_simp
    linear_combination (R (p 0) * deriv ψ (p 0) * deriv R (p 0) * 4 - R (p 0) * deriv (deriv R) (p 0) * 2
      + R (p 0) ^ 2 * deriv (deriv ψ) (p 0) * 4) * hx

omit hγ hR0 in
include hψ hR in
/-- **E4, the shear charge.** `C₀ = Ṙ − 2Rψ̇` has `Ċ₀ = AREA − 2 WAVE` (the `Λ` terms cancel): conserved on shell. -/
lemma gowdy_shear_charge (Λ ex s : ℝ) : HasDerivAt (fun t => deriv R t - 2 * R t * deriv ψ t)
    ((deriv (deriv R) s - 2 * Λ * R s * ex)
      - 2 * (deriv R s * deriv ψ s + R s * deriv (deriv ψ) s - Λ * R s * ex)) s := by
  have dR := (((contDiff_infty_iff_deriv.1 hR).2.differentiable (by simp)) s).hasDerivAt
  have dψ := (((contDiff_infty_iff_deriv.1 hψ).2.differentiable (by simp)) s).hasDerivAt
  have R0 := ((hR.differentiable (by simp)) s).hasDerivAt
  exact (dR.sub ((R0.const_mul 2).mul dψ)).congr_deriv (by ring)

end Engine4D_E4

/-! ### `r7323` instance 1 — row 52, the open slicing: the `k = −1` leaf at radius `A`, in a horospherical
chart `A²(dw² + e^{2w}(dx² + dy²))`, lies on the hyperboloid and has `³R = −6/A²` (so `6k/a²` with `k = −1`).
The leaf's curvature is read through the engine as the scalar curvature of the static product `−dt² + A²h`,
which equals `³R` because the product is static and its `t`-direction is flat. -/

section Inst_R52

set_option synthInstance.maxHeartbeats 400000

/-- The horospherical point of the hyperboloid `−X₀² + X₁² + X₂² + X₃² = A²` (the 4D slice of the
5D one, which is all a 3-leaf needs). -/
lemma horo_on_hyperboloid (A w x y : ℝ) :
    -(A * (Real.exp (-w) ^ 2 + x ^ 2 + y ^ 2 + 1) / (2 * Real.exp (-w))) ^ 2
      + (A * (Real.exp (-w) ^ 2 + x ^ 2 + y ^ 2 - 1) / (2 * Real.exp (-w))) ^ 2
      + (A * x / Real.exp (-w)) ^ 2 + (A * y / Real.exp (-w)) ^ 2 = -A ^ 2 := by
  have := Real.exp_pos (-w); field_simp; ring

set_option maxHeartbeats 4000000 in
/-- **Row 52.** The open leaf of radius `A` has scalar curvature `−6/A²` under THE connection. -/
theorem open_leaf_curv (A : ℝ) (hA : A ≠ 0) (p : Fin 4 → ℝ) :
    scalC (fun i => cS (FoF fun _ => A) GoF i p) (fun i j k => curv (lcConn (Fin 4 → ℝ)
      (ndOf (diag4 (cS (FoF fun _ => A) GoF)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => oF_ne (a := fun _ => A) (fun _ => hA) i p) u h)
      ((diag4_smooth (cS_smooth (FoF_smooth (a := fun _ => A) contDiff_const) GoF_smooth)).differentiable
        (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p) = -6 / A ^ 2 := by
  have hs := FoF_smooth (a := fun _ => A) contDiff_const
  have x1 : ∀ w, HasDerivAt (fun w => Real.exp (2 * w)) (2 * Real.exp (2 * w)) w := fun w =>
    HasDerivAt.congr_deriv (((hasDerivAt_id' w).const_mul 2).exp) (by ring)
  have f1 : deriv (fun w => Real.exp (2 * w)) = fun w => 2 * Real.exp (2 * w) := funext fun w => (x1 w).deriv
  have f2 : deriv (fun w => 2 * Real.exp (2 * w)) = fun w => 4 * Real.exp (2 * w) :=
    funext fun w => (((x1 w).const_mul 2)).deriv.trans (by ring)
  have hDF : ∀ k, deriv (FoF (fun _ => A) k) (p 0) = 0 := fun k => by
    fin_cases k <;> simp [FoF]
  have hDDF : ∀ k, deriv (deriv (FoF (fun _ => A) k)) (p 0) = 0 := fun k => by
    fin_cases k <;> simp [FoF]
  have hDG : ∀ k, deriv (GoF k) (p 1) = (![0, 0, 2 * Real.exp (2 * p 1), 2 * Real.exp (2 * p 1)] : Fin 4 → ℝ) k :=
    fun k => by
    fin_cases k
    exacts [deriv_const _ _, deriv_const _ _, (x1 _).deriv, (x1 _).deriv]
  have hDDG : ∀ k, deriv (deriv (GoF k)) (p 1)
      = (![0, 0, 4 * Real.exp (2 * p 1), 4 * Real.exp (2 * p 1)] : Fin 4 → ℝ) k := fun k => by
    fin_cases k
    · show deriv (deriv fun _ : ℝ => (1 : ℝ)) (p 1) = 0; simp
    · show deriv (deriv fun _ : ℝ => (1 : ℝ)) (p 1) = 0; simp
    all_goals (show deriv (deriv fun w => Real.exp (2 * w)) (p 1) = _; rw [f1, f2]; rfl)
  have h1 := fun k v => dC1_cS hs GoF_smooth p k v
  have h2 := fun k u v => dC2_cS hs GoF_smooth p k u v
  have h1' : ∀ k v, fderiv ℝ (cS (FoF fun _ => A) GoF k) p v = _ := fun k v => h1 k v
  have hE := Real.exp_pos (2 * p 1)
  simp only [scalC, ricC, Fin.sum_univ_four,
    curvD_eq (oF_ne (a := fun _ => A) (fun _ => hA)) (cS_smooth hs GoF_smooth)]
  simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, h1', h1, h2, hDF, hDDF, hDG, hDDG]
  simp [cS, FoF, GoF, Fin.sum_univ_four]
  field_simp; ring

end Inst_R52

/-! ### `r7323` instance 2 — row 79, the static gauge: the extrinsic curvature of the `t = const` leaves is
`K_ab = N Γ^t_ab`, so ***a static diagonal metric has `K_ab = 0` on every leaf***, under THE connection; and on
flat FRW (`N = 1`) the same object is `K_ij = a ȧ δ_ij`, with trace `K = 3H`. *The receipt's SdS leaf
(`r² dΩ²`) fails the chart clause; the vanishing is proved here for EVERY static diagonal metric that has a
chart, which contains every chartable member of that family.* -/

section Inst_R79

set_option synthInstance.maxHeartbeats 400000

variable {c : Fin 4 → (Fin 4 → ℝ) → ℝ} (hc : ∀ i p, c i p ≠ 0) (hcs : ∀ i, ContDiff ℝ ∞ (c i))
include hc hcs in
/-- **Row 79, static.** No coefficient depends on `t` ⇒ `Γ^t_ab = 0` for spatial `a, b`, so `K_ab = 0`. -/
theorem static_K_zero (p a b : Fin 4 → ℝ) (hst : ∀ k, fderiv ℝ (c k) p (Pi.single 0 1) = 0)
    (ha : a 0 = 0) (hb : b 0 = 0) : lcGam (diag4 c) p a b 0 = 0 := by
  rw [lcGam_diag4 hc hcs]; simp [gamD, ha, hb, hst]

variable {a : ℝ → ℝ} (ha : ∀ s, a s ≠ 0) (has : ContDiff ℝ ∞ a)
include ha has in
/-- **Row 79, FRW.** `K_ij = Γ^t_ij = a ȧ δ_ij` on the leaves of flat FRW. -/
theorem frw_K (p : Fin 4 → ℝ) (i j : Fin 4) (hi : i ≠ 0) (hj : j ≠ 0) :
    lcGam (diag4 (cT (qFRW a))) p (Pi.single i 1) (Pi.single j 1) 0
      = if i = j then a (p 0) * deriv a (p 0) else 0 := by
  have d0 : ∀ s, HasDerivAt a (deriv a s) s := fun s => ((has.differentiable (by simp)) s).hasDerivAt
  have e1 : deriv (fun s => a s ^ 2) = fun s => 2 * a s * deriv a s :=
    funext fun s => ((d0 s).pow 2).deriv.trans (by simp)
  rw [lcGam_T (qFRW_ne ha) (qFRW_smooth has)]
  fin_cases i <;> fin_cases j <;> simp_all [GT, qFRW, Fin.sum_univ_four, e1] <;> ring

include ha has in
/-- **Row 79, FRW, the trace.** `K = h^{ij} K_ij = 3ȧ/a = 3H`: the stacking rate, carried by the lapse. -/
theorem frw_K_trace (p : Fin 4 → ℝ) :
    ∑ i : Fin 4, (if i = 0 then 0 else
      lcGam (diag4 (cT (qFRW a))) p (Pi.single i 1) (Pi.single i 1) 0 / qFRW a i (p 0))
      = 3 * (deriv a (p 0) / a (p 0)) := by
  simp only [Fin.sum_univ_four]
  rw [frw_K ha has p 1 1 (by decide) (by decide), frw_K ha has p 2 2 (by decide) (by decide),
    frw_K ha has p 3 3 (by decide) (by decide)]
  have := ha (p 0)
  simp [qFRW]; field_simp; ring

end Inst_R79

/-! ### `r7323` instance 3 — row 75: the polarized Gowdy–de Sitter metric with `ψ, γ, R` functions of
`(t, z)`, `e^{2(γ−ψ)}(−dt² + dz²) + e^{2ψ}dx² + R²e^{−2ψ}dy²`. Under THE connection, `E_μν = R_μν − Λg_μν`
is exactly the four Gowdy field equations: `E_xx ∝ WAVE`, `E_yy ∝ WAVE − AREA`, `E_tz = MOMENTUM/R`,
`E_tt + E_zz = ENERGY/R`, the factors derivative-free. -/

section Inst_R75

set_option synthInstance.maxHeartbeats 400000

noncomputable def cG (ψ γ R : (Fin 4 → ℝ) → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun y => -Real.exp (2 * (γ y - ψ y)), fun y => Real.exp (2 * (γ y - ψ y)), fun y => Real.exp (2 * ψ y),
    fun y => R y ^ 2 * Real.exp (-(2 * ψ y))]

variable {ψ γ R : (Fin 4 → ℝ) → ℝ} (hψ : ContDiff ℝ ∞ ψ) (hγ : ContDiff ℝ ∞ γ) (hR : ContDiff ℝ ∞ R)
  (hR0 : ∀ y, R y ≠ 0)

include hψ hγ hR in
lemma cG_smooth (k : Fin 4) : ContDiff ℝ ∞ (cG ψ γ R k) := by fin_cases k <;> simp [cG] <;> fun_prop
include hR0 in
lemma cG_ne (k : Fin 4) (p : Fin 4 → ℝ) : cG ψ γ R k p ≠ 0 := by
  fin_cases k <;> simp [cG, Real.exp_ne_zero, hR0]

set_option maxHeartbeats 8000000 in
include hψ hγ hR hR0 in
/-- **Row 75.** -/
theorem gowdy_tz_field (Λ : ℝ) (p : Fin 4 → ℝ)
    (hind : ∀ y, ∀ i : Fin 4, i = 2 ∨ i = 3 → fderiv ℝ ψ y (Pi.single i 1) = 0
      ∧ fderiv ℝ γ y (Pi.single i 1) = 0 ∧ fderiv ℝ R y (Pi.single i 1) = 0) :
    let Rf := fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cG ψ γ R)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cG_ne hR0 i p) u h)
      ((diag4_smooth (cG_smooth hψ hγ hR)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p
    let E := fun j => ricC Rf j j - Λ * cG ψ γ R j p
    let D := fun (f : (Fin 4 → ℝ) → ℝ) (i : Fin 4) => fderiv ℝ f p (Pi.single i 1)
    let D2 := fun (f : (Fin 4 → ℝ) → ℝ) (i j : Fin 4) => fderiv ℝ (fderiv ℝ f) p (Pi.single i 1) (Pi.single j 1)
    let ex := Real.exp (2 * (γ p - ψ p))
    let WAVE := D R 0 * D ψ 0 + R p * D2 ψ 0 0 - D R 1 * D ψ 1 - R p * D2 ψ 1 1 - Λ * R p * ex
    let AREA := D2 R 0 0 - D2 R 1 1 - 2 * Λ * R p * ex
    let ENERGY := 2 * (D R 0 * D γ 0 + D R 1 * D γ 1) - (D2 R 0 0 + D2 R 1 1) - 2 * R p * (D ψ 0 ^ 2 + D ψ 1 ^ 2)
    let MOM := D R 0 * D γ 1 + D R 1 * D γ 0 - D2 R 0 1 - 2 * R p * D ψ 0 * D ψ 1
    R p * ex * Real.exp (-(2 * ψ p)) * E 2 = WAVE
      ∧ ex * Real.exp (2 * ψ p) * E 3 = -(R p * (WAVE - AREA))
      ∧ ricC Rf 0 1 = MOM / R p
      ∧ E 0 + E 1 = ENERGY / R p := by
  intro Rf E D D2 ex WAVE AREA ENERGY MOM
  have dψ := fun y => (hψ.differentiable (by simp) y).hasFDerivAt
  have dγ := fun y => (hγ.differentiable (by simp) y).hasFDerivAt
  have dR := fun y => (hR.differentiable (by simp) y).hasFDerivAt
  have Hh : ∀ y, HasFDerivAt (fun y => 2 * (γ y - ψ y)) ((2 : ℝ) • (fderiv ℝ γ y - fderiv ℝ ψ y)) y :=
    fun y => ((dγ y).sub (dψ y)).const_mul 2
  have H2 : ∀ y, HasFDerivAt (fun y => 2 * ψ y) ((2 : ℝ) • fderiv ℝ ψ y) y := fun y => (dψ y).const_mul 2
  -- first partials of the four coefficients, at every point
  have e1 : ∀ y v, fderiv ℝ (fun y => Real.exp (2 * (γ y - ψ y))) y v
      = Real.exp (2 * (γ y - ψ y)) * (2 * (fderiv ℝ γ y v - fderiv ℝ ψ y v)) := fun y v => by
    rw [((Hh y).exp).fderiv]; simp
  have e0 : ∀ y v, fderiv ℝ (fun y => -Real.exp (2 * (γ y - ψ y))) y v
      = -(Real.exp (2 * (γ y - ψ y)) * (2 * (fderiv ℝ γ y v - fderiv ℝ ψ y v))) := fun y v => by
    rw [(show HasFDerivAt (fun y => -Real.exp (2 * (γ y - ψ y))) _ y from (Hh y).exp.neg).fderiv]; simp
  have e2 : ∀ y v, fderiv ℝ (fun y => Real.exp (2 * ψ y)) y v = Real.exp (2 * ψ y) * (2 * fderiv ℝ ψ y v) :=
    fun y v => by rw [((H2 y).exp).fderiv]; simp
  have e3 : ∀ y v, fderiv ℝ (fun y => R y ^ 2 * Real.exp (-(2 * ψ y))) y v
      = 2 * R y * fderiv ℝ R y v * Real.exp (-(2 * ψ y))
        - R y ^ 2 * (2 * fderiv ℝ ψ y v) * Real.exp (-(2 * ψ y)) := fun y v => by
    rw [(show HasFDerivAt (fun y => R y ^ 2 * Real.exp (-(2 * ψ y))) _ y from
      ((dR y).pow 2).mul ((H2 y).neg.exp)).fderiv]; simp; ring
  -- second partials, through E5
  have s1 : ∀ u v, fderiv ℝ (fderiv ℝ (fun y => Real.exp (2 * (γ y - ψ y)))) p u v
      = Real.exp (2 * (γ p - ψ p)) * (2 * (fderiv ℝ γ p u - fderiv ℝ ψ p u))
          * (2 * (fderiv ℝ γ p v - fderiv ℝ ψ p v))
        + Real.exp (2 * (γ p - ψ p)) * (2 * (fderiv ℝ (fderiv ℝ γ) p u v - fderiv ℝ (fderiv ℝ ψ) p u v)) :=
    fun u v => by
    rw [d2_of (by fun_prop) (fun y => e1 y v)
      (((Hh p).exp).mul (((fdA_hasFDerivAt hγ p v).sub (fdA_hasFDerivAt hψ p v)).const_mul 2))]
    simp; ring
  have s0 : ∀ u v, fderiv ℝ (fderiv ℝ (fun y => -Real.exp (2 * (γ y - ψ y)))) p u v
      = -(Real.exp (2 * (γ p - ψ p)) * (2 * (fderiv ℝ γ p u - fderiv ℝ ψ p u))
          * (2 * (fderiv ℝ γ p v - fderiv ℝ ψ p v))
        + Real.exp (2 * (γ p - ψ p)) * (2 * (fderiv ℝ (fderiv ℝ γ) p u v - fderiv ℝ (fderiv ℝ ψ) p u v))) :=
    fun u v => by
    rw [d2_of (by fun_prop) (fun y => e0 y v)
      (((Hh p).exp).mul (((fdA_hasFDerivAt hγ p v).sub (fdA_hasFDerivAt hψ p v)).const_mul 2)).neg]
    simp; ring
  have s2 : ∀ u v, fderiv ℝ (fderiv ℝ (fun y => Real.exp (2 * ψ y))) p u v
      = Real.exp (2 * ψ p) * (2 * fderiv ℝ ψ p u) * (2 * fderiv ℝ ψ p v)
        + Real.exp (2 * ψ p) * (2 * fderiv ℝ (fderiv ℝ ψ) p u v) := fun u v => by
    rw [d2_of (by fun_prop) (fun y => e2 y v) (((H2 p).exp).mul ((fdA_hasFDerivAt hψ p v).const_mul 2))]
    simp; ring
  have s3 : ∀ u v, fderiv ℝ (fderiv ℝ (fun y => R y ^ 2 * Real.exp (-(2 * ψ y)))) p u v
      = (2 * fderiv ℝ R p u * fderiv ℝ R p v + 2 * R p * fderiv ℝ (fderiv ℝ R) p u v
          - 2 * R p * fderiv ℝ R p v * (2 * fderiv ℝ ψ p u)
          - 2 * R p * fderiv ℝ R p u * (2 * fderiv ℝ ψ p v) - R p ^ 2 * (2 * fderiv ℝ (fderiv ℝ ψ) p u v)
          + R p ^ 2 * (2 * fderiv ℝ ψ p v) * (2 * fderiv ℝ ψ p u)) * Real.exp (-(2 * ψ p)) := fun u v => by
    rw [d2_of (by fun_prop) (fun y => e3 y v)
      (HasFDerivAt.sub (HasFDerivAt.mul (HasFDerivAt.mul ((dR p).const_mul 2) (fdA_hasFDerivAt hR p v))
        ((H2 p).neg.exp))
        (HasFDerivAt.mul (HasFDerivAt.mul ((dR p).pow 2) ((fdA_hasFDerivAt hψ p v).const_mul 2))
          ((H2 p).neg.exp)))]
    simp; ring
  -- the recipe's facts, in the engine's own names
  have i2 := hind p 2 (by decide); have i3 := hind p 3 (by decide)
  -- `(t, z)` dependence only: every first partial is `v⁰ ∂₀ + v¹ ∂₁`
  have lin : ∀ f : (Fin 4 → ℝ) → ℝ, fderiv ℝ f p (Pi.single 2 1) = 0 → fderiv ℝ f p (Pi.single 3 1) = 0 →
      ∀ v, fderiv ℝ f p v = v 0 * fderiv ℝ f p (Pi.single 0 1) + v 1 * fderiv ℝ f p (Pi.single 1 1) := by
    intro f h2 h3 v
    have hv : v = ∑ i, v i • (Pi.single i 1 : Fin 4 → ℝ) := by ext i; simp [Pi.single_apply]
    conv_lhs => rw [hv]
    simp [map_sum, Fin.sum_univ_four, h2, h3]
  have hD1 : ∀ k v, fderiv ℝ (cG ψ γ R k) p v = (![
      -(Real.exp (2 * (γ p - ψ p)) * (2 * ((v 0 * fderiv ℝ γ p (Pi.single 0 1) + v 1 * fderiv ℝ γ p (Pi.single 1 1))
        - (v 0 * fderiv ℝ ψ p (Pi.single 0 1) + v 1 * fderiv ℝ ψ p (Pi.single 1 1))))),
      Real.exp (2 * (γ p - ψ p)) * (2 * ((v 0 * fderiv ℝ γ p (Pi.single 0 1) + v 1 * fderiv ℝ γ p (Pi.single 1 1))
        - (v 0 * fderiv ℝ ψ p (Pi.single 0 1) + v 1 * fderiv ℝ ψ p (Pi.single 1 1)))),
      Real.exp (2 * ψ p) * (2 * (v 0 * fderiv ℝ ψ p (Pi.single 0 1) + v 1 * fderiv ℝ ψ p (Pi.single 1 1))),
      2 * R p * (v 0 * fderiv ℝ R p (Pi.single 0 1) + v 1 * fderiv ℝ R p (Pi.single 1 1)) * Real.exp (-(2 * ψ p))
        - R p ^ 2 * (2 * (v 0 * fderiv ℝ ψ p (Pi.single 0 1) + v 1 * fderiv ℝ ψ p (Pi.single 1 1)))
          * Real.exp (-(2 * ψ p))] : Fin 4 → ℝ) k := fun k v => by
    rw [← lin ψ i2.1 i3.1 v, ← lin γ i2.2.1 i3.2.1 v, ← lin R i2.2.2 i3.2.2 v]
    fin_cases k
    exacts [e0 p v, e1 p v, e2 p v, e3 p v]
  have hD2 : ∀ k u v, fderiv ℝ (fderiv ℝ (cG ψ γ R k)) p u v = (![
      -(Real.exp (2 * (γ p - ψ p)) * (2 * (fderiv ℝ γ p u - fderiv ℝ ψ p u))
          * (2 * (fderiv ℝ γ p v - fderiv ℝ ψ p v))
        + Real.exp (2 * (γ p - ψ p)) * (2 * (fderiv ℝ (fderiv ℝ γ) p u v - fderiv ℝ (fderiv ℝ ψ) p u v))),
      Real.exp (2 * (γ p - ψ p)) * (2 * (fderiv ℝ γ p u - fderiv ℝ ψ p u))
          * (2 * (fderiv ℝ γ p v - fderiv ℝ ψ p v))
        + Real.exp (2 * (γ p - ψ p)) * (2 * (fderiv ℝ (fderiv ℝ γ) p u v - fderiv ℝ (fderiv ℝ ψ) p u v)),
      Real.exp (2 * ψ p) * (2 * fderiv ℝ ψ p u) * (2 * fderiv ℝ ψ p v)
        + Real.exp (2 * ψ p) * (2 * fderiv ℝ (fderiv ℝ ψ) p u v),
      (2 * fderiv ℝ R p u * fderiv ℝ R p v + 2 * R p * fderiv ℝ (fderiv ℝ R) p u v
          - 2 * R p * fderiv ℝ R p v * (2 * fderiv ℝ ψ p u)
          - 2 * R p * fderiv ℝ R p u * (2 * fderiv ℝ ψ p v) - R p ^ 2 * (2 * fderiv ℝ (fderiv ℝ ψ) p u v)
          + R p ^ 2 * (2 * fderiv ℝ ψ p v) * (2 * fderiv ℝ ψ p u)) * Real.exp (-(2 * ψ p))] : Fin 4 → ℝ) k :=
    fun k u v => by
    fin_cases k
    exacts [s0 u v, s1 u v, s2 u v, s3 u v]
  -- `(t, z)` dependence only, and the mixed partials' symmetry
  have j2 := fun f (hf : ContDiff ℝ ∞ f) (h : ∀ y, fderiv ℝ f y (Pi.single (2 : Fin 4) 1) = 0) u =>
    d2_indep hf h p u
  have k2ψ := j2 ψ hψ (fun y => (hind y 2 (by decide)).1)
  have k2γ := j2 γ hγ (fun y => (hind y 2 (by decide)).2.1)
  have k2R := j2 R hR (fun y => (hind y 2 (by decide)).2.2)
  have k3ψ := fun u => d2_indep hψ (fun y => (hind y 3 (by decide)).1) p u
  have k3γ := fun u => d2_indep hγ (fun y => (hind y 3 (by decide)).2.1) p u
  have k3R := fun u => d2_indep hR (fun y => (hind y 3 (by decide)).2.2) p u
  have yψ : fderiv ℝ (fderiv ℝ ψ) p (Pi.single 1 1) (Pi.single 0 1)
      = fderiv ℝ (fderiv ℝ ψ) p (Pi.single 0 1) (Pi.single 1 1) := (hψ.contDiffAt.isSymmSndFDerivAt (by simp)) _ _
  have yγ : fderiv ℝ (fderiv ℝ γ) p (Pi.single 1 1) (Pi.single 0 1)
      = fderiv ℝ (fderiv ℝ γ) p (Pi.single 0 1) (Pi.single 1 1) := (hγ.contDiffAt.isSymmSndFDerivAt (by simp)) _ _
  have yR : fderiv ℝ (fderiv ℝ R) p (Pi.single 1 1) (Pi.single 0 1)
      = fderiv ℝ (fderiv ℝ R) p (Pi.single 0 1) (Pi.single 1 1) := (hR.contDiffAt.isSymmSndFDerivAt (by simp)) _ _
  have hRp := hR0 p
  simp only [Rf, E, ricC, Fin.sum_univ_four, curvD_eq (cG_ne hR0) (cG_smooth hψ hγ hR)]
  simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
  simp [cG, Fin.sum_univ_four, i2, i3, k2ψ, k2γ, k2R, k3ψ, k3γ, k3R, yψ, yγ, yR, Real.exp_neg,
    D, D2, ex, WAVE, AREA, ENERGY, MOM]
  refine ⟨?_, ?_, ?_, ?_⟩ <;> (field_simp; ring)

end Inst_R75

/-! ### `r7327` — the `S²` pilot, row 45: the SdS Kretschmann scalar `K = 48M²/r⁶ + 8Λ²/3` under THE connection,
in `(t, r, θ, φ)`. The profiles `F, P, S` are smooth and nowhere zero and equal `f`, `r²`, `sin²θ` NEAR THE POINT:
the convention, whose existence the cutoff lemma now proves. -/

section Inst_R45

set_option synthInstance.maxHeartbeats 400000

noncomputable def cK (F P S : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun y => -F (y 1), fun y => (F (y 1))⁻¹, fun y => P (y 1), fun y => P (y 1) * S (y 2)]

/-- The static-spherical Riemann table `R(eᵢ,eⱼ)eₖ` component `l`, in `F₀, F₁, F₂` (the radial profile and its
derivatives), `r`, and `S₀, S₁, S₂` (the angular profile); the angular part enters only through `Q`. -/
noncomputable def kR (f0 f1 f2 r s0 s1 s2 : ℝ) (i j k l : Fin 4) : ℝ :=
  let Q := (4 * f0 * s0 ^ 2 + 2 * s0 * s2 - s1 ^ 2) / (4 * s0 ^ 2)
  if (i, j, k, l) = (0, 1, 0, 1) then -(f0 * f2 / 2) else if (i, j, k, l) = (0, 1, 1, 0) then -(f2 / (2 * f0))
  else if (i, j, k, l) = (0, 2, 0, 2) then -(f0 * f1 / (2 * r)) else if (i, j, k, l) = (0, 2, 2, 0) then -(f1 * r / 2)
  else if (i, j, k, l) = (0, 3, 0, 3) then -(f0 * f1 / (2 * r)) else if (i, j, k, l) = (0, 3, 3, 0) then -(f1 * r * s0 / 2)
  else if (i, j, k, l) = (1, 0, 0, 1) then f0 * f2 / 2 else if (i, j, k, l) = (1, 0, 1, 0) then f2 / (2 * f0)
  else if (i, j, k, l) = (1, 2, 1, 2) then f1 / (2 * f0 * r) else if (i, j, k, l) = (1, 2, 2, 1) then -(f1 * r / 2)
  else if (i, j, k, l) = (1, 3, 1, 3) then f1 / (2 * f0 * r) else if (i, j, k, l) = (1, 3, 3, 1) then -(f1 * r * s0 / 2)
  else if (i, j, k, l) = (2, 0, 0, 2) then f0 * f1 / (2 * r) else if (i, j, k, l) = (2, 0, 2, 0) then f1 * r / 2
  else if (i, j, k, l) = (2, 1, 1, 2) then -(f1 / (2 * f0 * r)) else if (i, j, k, l) = (2, 1, 2, 1) then f1 * r / 2
  else if (i, j, k, l) = (2, 3, 2, 3) then Q else if (i, j, k, l) = (2, 3, 3, 2) then -(Q * s0)
  else if (i, j, k, l) = (3, 0, 0, 3) then f0 * f1 / (2 * r) else if (i, j, k, l) = (3, 0, 3, 0) then f1 * r * s0 / 2
  else if (i, j, k, l) = (3, 1, 1, 3) then -(f1 / (2 * f0 * r)) else if (i, j, k, l) = (3, 1, 3, 1) then f1 * r * s0 / 2
  else if (i, j, k, l) = (3, 2, 2, 3) then -Q else if (i, j, k, l) = (3, 2, 3, 2) then Q * s0
  else 0

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hF hP hS hF0 in
lemma cK_smooth (k : Fin 4) : ContDiff ℝ ∞ (cK F P S k) := by
  fin_cases k
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).neg
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).inv fun y => hF0 _
  · exact hP.comp (contDiff_apply ℝ ℝ 1)
  · exact (hP.comp (contDiff_apply ℝ ℝ 1)).mul (hS.comp (contDiff_apply ℝ ℝ 2))
include hF0 hP0 hS0 in
lemma cK_ne (k : Fin 4) (p : Fin 4 → ℝ) : cK F P S k p ≠ 0 := by
  fin_cases k <;> simp [cK, hF0, hP0, hS0]

open Filter Topology in
set_option maxHeartbeats 8000000 in
include hF hP hS hF0 hP0 hS0 in
/-- **Row 45, the `S²` pilot.** -/
theorem sds_kretschmann (M Λ : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    riem2C (fun i => cK F P S i p) (fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cK F P S)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cK_ne hF0 hP0 hS0 i p) u h)
      ((diag4_smooth (cK_smooth hF hP hS hF0)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p) = 48 * M ^ 2 / p 1 ^ 6 + 8 * Λ ^ 2 / 3 := by
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  -- the radial profile: `f`, `f′`, `f″` at `r`
  have hf1 : ∀ s, s ≠ 0 → HasDerivAt (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2)
      (2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s) s := fun s hs =>
    (show HasDerivAt (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) _ s from
      ((hasDerivAt_const s (1 : ℝ)).sub ((hasDerivAt_inv hs).const_mul (2 * M))).sub
        ((hasDerivAt_pow 2 s).const_mul (Λ / 3))).congr_deriv (by norm_num; ring)
  have ed : deriv (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) =ᶠ[𝓝 r]
      fun s => 2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s :=
    Filter.eventually_of_mem (isOpen_ne.mem_nhds hr) fun s hs => (hf1 s hs).deriv
  have hF0v : F r = 1 - 2 * M * r⁻¹ - Λ / 3 * r ^ 2 := eF.eq_of_nhds
  have hF1v : deriv F r = 2 * M * (r ^ 2)⁻¹ - 2 * Λ / 3 * r := by rw [eF.deriv_eq, (hf1 r hr).deriv]
  have hF2v : deriv (deriv F) r = -(4 * M / r ^ 3) - 2 * Λ / 3 := by
    rw [(eF.deriv.trans ed).deriv_eq]
    have := (show HasDerivAt (fun s => 2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s) _ r from
      (((hasDerivAt_pow 2 r).inv (pow_ne_zero 2 hr)).const_mul (2 * M)).sub ((hasDerivAt_id r).const_mul (2 * Λ / 3)))
    rw [this.deriv]; field_simp; ring
  -- the inverse profile `1/F`
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  have dF' := fun s => (((contDiff_infty_iff_deriv.1 hF).2.differentiable (by simp)) s).hasDerivAt
  have iv1 : deriv (fun s => (F s)⁻¹) = fun s => -(deriv F s) / F s ^ 2 :=
    funext fun s => ((dF s).inv (hF0 s)).deriv.trans (by ring)
  have iv2 : deriv (deriv (fun s => (F s)⁻¹)) r = (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 := by
    rw [iv1, (show HasDerivAt (fun s => -deriv F s / F s ^ 2) _ r from
      (dF' r).neg.div ((dF r).pow 2) (pow_ne_zero 2 (hF0 r))).deriv]
    have := hF0 r; simp only [Pi.neg_apply]; field_simp; ring
  have ng1 : deriv (fun s => -F s) = fun s => -deriv F s := funext fun s => deriv.neg
  have hneg : ContDiff ℝ ∞ (fun s => -F s) := hF.neg
  have hinv : ContDiff ℝ ∞ (fun s => (F s)⁻¹) := hF.inv hF0
  -- `r²` and `sin²θ`
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have e2 : deriv P =ᶠ[𝓝 r] fun s => 2 * s := eP.deriv.trans (Eventually.of_forall fun s => by simp)
  have hP2 : deriv (deriv P) r = 2 := by rw [e2.deriv_eq]; simp
  have sd : ∀ s, HasDerivAt (fun s => Real.sin s ^ 2) (2 * Real.sin s * Real.cos s) s := fun s =>
    (show HasDerivAt (fun s => Real.sin s ^ 2) _ s from (Real.hasDerivAt_sin s).pow 2).congr_deriv (by norm_num <;> ring)
  have hSv : S (p 2) = Real.sin (p 2) ^ 2 := eS.eq_of_nhds
  have hS1 : deriv S (p 2) = 2 * Real.sin (p 2) * Real.cos (p 2) := by rw [eS.deriv_eq, (sd _).deriv]
  have hS2 : deriv (deriv S) (p 2) = 2 * Real.cos (p 2) ^ 2 - 2 * Real.sin (p 2) ^ 2 := by
    have e3 : deriv S =ᶠ[𝓝 (p 2)] fun s => 2 * Real.sin s * Real.cos s :=
      eS.deriv.trans (Eventually.of_forall fun s => (sd s).deriv)
    rw [e3.deriv_eq]
    have := (show HasDerivAt (fun s => 2 * Real.sin s * Real.cos s) _ (p 2) from
      ((Real.hasDerivAt_sin (p 2)).const_mul 2).mul (Real.hasDerivAt_cos (p 2)))
    rw [this.deriv]; ring
  -- the recipe's facts
  have hD1 : ∀ k v, fderiv ℝ (cK F P S k) p v = (![-(deriv F r * v 1), -(deriv F r) / F r ^ 2 * v 1,
      2 * r * v 1, 2 * r * v 1 * S (p 2) + r ^ 2 * (deriv S (p 2) * v 2)] : Fin 4 → ℝ) k := fun k v => by
    fin_cases k
    · show fderiv ℝ (fun y => (fun s => -F s) (y 1)) p v = _
      rw [co_d1 hneg]; simp [← hr_def, ng1]
    · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1)) p v = _
      rw [co_d1 hinv]; simp [← hr_def, iv1]
    · show fderiv ℝ (fun y => P (y 1)) p v = _
      rw [co_d1 hP]; simp [← hr_def, hP1]
    · show fderiv ℝ (fun y => P (y 1) * S (y 2)) p v = _
      rw [pr_d1 hP hS]; simp [← hr_def, hP1, hPv]
  have hD2 : ∀ k u v, fderiv ℝ (fderiv ℝ (cK F P S k)) p u v = (![-(deriv (deriv F) r * u 1 * v 1),
      (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 * u 1 * v 1, 2 * u 1 * v 1,
      2 * u 1 * v 1 * S (p 2) + 2 * r * v 1 * (deriv S (p 2) * u 2) + 2 * r * u 1 * (deriv S (p 2) * v 2)
        + r ^ 2 * (deriv (deriv S) (p 2) * u 2 * v 2)] : Fin 4 → ℝ) k := fun k u v => by
    fin_cases k
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => -F s) (y 1))) p u v = _
      rw [co_d2 hneg]; simp [← hr_def, ng1, deriv.neg]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1))) p u v = _
      rw [co_d2 hinv]; simp [← hr_def, iv2]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1))) p u v = _
      rw [co_d2 hP]; simp [← hr_def, hP2]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1) * S (y 2))) p u v = _
      rw [pr_d2 hP hS]; simp [← hr_def, hP1, hP2, hPv]
  -- the table, component by component
  have hT : ∀ i j k l, curvD (cK F P S) p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l
      = kR (F r) (deriv F r) (deriv (deriv F) r) r (S (p 2)) (deriv S (p 2)) (deriv (deriv S) (p 2)) i j k l := by
    have := hF0 r; have := hS0 (p 2)
    intro i j k l
    fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
      (simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
       simp [cK, kR, Fin.sum_univ_four, ← hr_def, hPv]
       try (field_simp; try ring))
  simp only [riem2C, curvD_eq (cK_ne hF0 hP0 hS0) (cK_smooth hF hP hS hF0), hT]
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have hf := hF0 r
  rw [show (48 * M ^ 2 / r ^ 6 + 8 * Λ ^ 2 / 3 : ℝ)
      = deriv (deriv F) r ^ 2 + 4 * deriv F r ^ 2 / r ^ 2 + 4 * (F r - 1) ^ 2 / r ^ 4 by
    rw [hF0v, hF1v, hF2v]; field_simp; ring]
  simp [Fin.sum_univ_four, kR, cK, ← hr_def, hPv, hSv, hS1, hS2]
  field_simp
  ring

end Inst_R45

/-! ### `r7333` — the Kretschmann rows. Row 45's table, lifted to ANY radial area profile: `diag(−F, 1/F, P, P·S)`
with `F`, `P` functions of `r` and `S` of `θ`, all arbitrary. One table carries SdS (`P = r²`) and Nariai (`P`
constant); the rows are its corollaries. `sds_kretschmann` above is not touched. -/

section Inst_Kretschmann

set_option synthInstance.maxHeartbeats 400000

/-- The general static table `R(eᵢ,eⱼ)eₖ` component `l`: the radial profile `F₀, F₁, F₂`, the area profile
`P₀, P₁, P₂`, and the angular profile `S₀, S₁, S₂`, entering through `A`, `B`, `C`. Generated, and then proved below. -/
noncomputable def kG (f0 f1 f2 p0 p1 p2 s0 s1 s2 : ℝ) (i j k l : Fin 4) : ℝ :=
  let A := (2 * f0 * p0 * p2 - f0 * p1 ^ 2 + f1 * p0 * p1) / (4 * p0)
  let B := (f0 * p1 ^ 2 * s0 ^ 2 + 2 * p0 * s0 * s2 - p0 * s1 ^ 2) / (4 * p0 * s0 ^ 2)
  let C := f1 * p1 / 4
  if (i, j, k, l) = (0, 1, 0, 1) then -(f0 * f2 / 2) else if (i, j, k, l) = (0, 1, 1, 0) then -(f2 / (2 * f0))
  else if (i, j, k, l) = (0, 2, 0, 2) then -(f0 * C / p0) else if (i, j, k, l) = (0, 2, 2, 0) then -C
  else if (i, j, k, l) = (0, 3, 0, 3) then -(f0 * C / p0) else if (i, j, k, l) = (0, 3, 3, 0) then -(C * s0)
  else if (i, j, k, l) = (1, 0, 0, 1) then f0 * f2 / 2 else if (i, j, k, l) = (1, 0, 1, 0) then f2 / (2 * f0)
  else if (i, j, k, l) = (1, 2, 1, 2) then A / (f0 * p0) else if (i, j, k, l) = (1, 2, 2, 1) then -A
  else if (i, j, k, l) = (1, 3, 1, 3) then A / (f0 * p0) else if (i, j, k, l) = (1, 3, 3, 1) then -(A * s0)
  else if (i, j, k, l) = (2, 0, 0, 2) then f0 * C / p0 else if (i, j, k, l) = (2, 0, 2, 0) then C
  else if (i, j, k, l) = (2, 1, 1, 2) then -(A / (f0 * p0)) else if (i, j, k, l) = (2, 1, 2, 1) then A
  else if (i, j, k, l) = (2, 3, 2, 3) then B else if (i, j, k, l) = (2, 3, 3, 2) then -(B * s0)
  else if (i, j, k, l) = (3, 0, 0, 3) then f0 * C / p0 else if (i, j, k, l) = (3, 0, 3, 0) then C * s0
  else if (i, j, k, l) = (3, 1, 1, 3) then -(A / (f0 * p0)) else if (i, j, k, l) = (3, 1, 3, 1) then A * s0
  else if (i, j, k, l) = (3, 2, 2, 3) then -B else if (i, j, k, l) = (3, 2, 3, 2) then B * s0
  else 0

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

/-- THE connection's curvature on basis fields at `p`, for `diag(−F, 1/F, P, P·S)`: the same expression
`sds_kretschmann` states, named once. -/
noncomputable def RK (p : Fin 4 → ℝ) (i j k : Fin 4) : Fin 4 → ℝ :=
  curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cK F P S)) (diag4_symm _)
    (fun p u h => diag4_nondeg (fun i => cK_ne hF0 hP0 hS0 i p) u h)
    ((diag4_smooth (cK_smooth hF hP hS hF0)).differentiable (by simp))))
    (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
    (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p

set_option maxHeartbeats 8000000 in
/-- **The general static table**, for any `F`, `P`, `S`. -/
theorem static_table (p : Fin 4 → ℝ) (i j k l : Fin 4) :
    RK hF hP hS hF0 hP0 hS0 p i j k l = kG (F (p 1)) (deriv F (p 1)) (deriv (deriv F) (p 1)) (P (p 1))
      (deriv P (p 1)) (deriv (deriv P) (p 1)) (S (p 2)) (deriv S (p 2)) (deriv (deriv S) (p 2)) i j k l := by
  rw [RK, curvD_eq (cK_ne hF0 hP0 hS0) (cK_smooth hF hP hS hF0)]
  set r := p 1 with hr_def
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  have dF' := fun s => (((contDiff_infty_iff_deriv.1 hF).2.differentiable (by simp)) s).hasDerivAt
  have iv1 : deriv (fun s => (F s)⁻¹) = fun s => -(deriv F s) / F s ^ 2 :=
    funext fun s => ((dF s).inv (hF0 s)).deriv.trans (by ring)
  have iv2 : deriv (deriv (fun s => (F s)⁻¹)) r = (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 := by
    rw [iv1, (show HasDerivAt (fun s => -deriv F s / F s ^ 2) _ r from
      (dF' r).neg.div ((dF r).pow 2) (pow_ne_zero 2 (hF0 r))).deriv]
    have := hF0 r; simp only [Pi.neg_apply]; field_simp; ring
  have ng1 : deriv (fun s => -F s) = fun s => -deriv F s := funext fun s => deriv.neg
  have hneg : ContDiff ℝ ∞ (fun s => -F s) := hF.neg
  have hinv : ContDiff ℝ ∞ (fun s => (F s)⁻¹) := hF.inv hF0
  have hD1 : ∀ k v, fderiv ℝ (cK F P S k) p v = (![-(deriv F r * v 1), -(deriv F r) / F r ^ 2 * v 1,
      deriv P r * v 1, deriv P r * v 1 * S (p 2) + P r * (deriv S (p 2) * v 2)] : Fin 4 → ℝ) k := fun k v => by
    fin_cases k
    · show fderiv ℝ (fun y => (fun s => -F s) (y 1)) p v = _
      rw [co_d1 hneg]; simp [← hr_def, ng1]
    · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1)) p v = _
      rw [co_d1 hinv]; simp [← hr_def, iv1]
    · show fderiv ℝ (fun y => P (y 1)) p v = _
      rw [co_d1 hP]; simp [← hr_def]
    · show fderiv ℝ (fun y => P (y 1) * S (y 2)) p v = _
      rw [pr_d1 hP hS]; simp [← hr_def]
  have hD2 : ∀ k u v, fderiv ℝ (fderiv ℝ (cK F P S k)) p u v = (![-(deriv (deriv F) r * u 1 * v 1),
      (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 * u 1 * v 1, deriv (deriv P) r * u 1 * v 1,
      deriv (deriv P) r * u 1 * v 1 * S (p 2) + deriv P r * v 1 * (deriv S (p 2) * u 2)
        + deriv P r * u 1 * (deriv S (p 2) * v 2) + P r * (deriv (deriv S) (p 2) * u 2 * v 2)] : Fin 4 → ℝ) k :=
    fun k u v => by
    fin_cases k
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => -F s) (y 1))) p u v = _
      rw [co_d2 hneg]; simp [← hr_def, ng1]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1))) p u v = _
      rw [co_d2 hinv]; simp [← hr_def, iv2]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1))) p u v = _
      rw [co_d2 hP]; simp [← hr_def]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1) * S (y 2))) p u v = _
      rw [pr_d2 hP hS]; simp [← hr_def]
  have := hF0 r; have := hS0 (p 2); have := hP0 r
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    (simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
     simp [cK, kG, Fin.sum_univ_four, ← hr_def]
     try (field_simp; try ring))


open Filter Topology in
/-- `sin²θ` and its two derivatives at `θ`. -/
lemma sin2_facts {S : ℝ → ℝ} {θ : ℝ} (eS : S =ᶠ[𝓝 θ] fun s => Real.sin s ^ 2) :
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

include hF hP hS hF0 hP0 hS0

open Filter Topology in
/-- **The Ricci tensor** of `diag(−F, 1/F, P, P sin²θ)`, for any `F` and `P`, in `F₀, F₁, F₂, P₀, P₁, P₂` at `r`. -/
theorem static_ric (p : Fin 4 → ℝ) (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) (j k : Fin 4) :
    ricC (RK hF hP hS hF0 hP0 hS0 p) j k = if j = k then (![
      F (p 1) * (deriv F (p 1) * deriv P (p 1) + deriv (deriv F) (p 1) * P (p 1)) / (2 * P (p 1)),
      -(2 * F (p 1) * P (p 1) * deriv (deriv P) (p 1) - F (p 1) * deriv P (p 1) ^ 2
        + deriv F (p 1) * P (p 1) * deriv P (p 1) + deriv (deriv F) (p 1) * P (p 1) ^ 2)
        / (2 * F (p 1) * P (p 1) ^ 2),
      -(F (p 1) * deriv (deriv P) (p 1) + deriv F (p 1) * deriv P (p 1) - 2) / 2,
      -(S (p 2) * (F (p 1) * deriv (deriv P) (p 1) + deriv F (p 1) * deriv P (p 1) - 2)) / 2] : Fin 4 → ℝ) j
      else 0 := by
  obtain ⟨hSv, hS1, hS2⟩ := sin2_facts eS
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have := hF0 (p 1); have := hP0 (p 1)
  fin_cases j <;> fin_cases k <;>
    (simp [ricC, Fin.sum_univ_four, static_table, kG, hSv, hS1, hS2]
     try (field_simp; try ring))

open Filter Topology in
/-- **The Kretschmann scalar** of `diag(−F, 1/F, P, P sin²θ)`, for any `F` and `P`. -/
theorem static_riem2 (p : Fin 4 → ℝ) (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) =
      let f0 := F (p 1); let f1 := deriv F (p 1); let f2 := deriv (deriv F) (p 1)
      let p0 := P (p 1); let p1 := deriv P (p 1); let p2 := deriv (deriv P) (p 1)
      (8 * f0 ^ 2 * p0 ^ 2 * p2 ^ 2 - 8 * f0 ^ 2 * p0 * p1 ^ 2 * p2 + 3 * f0 ^ 2 * p1 ^ 4
        + 8 * f0 * f1 * p0 ^ 2 * p1 * p2 - 4 * f0 * f1 * p0 * p1 ^ 3 - 8 * f0 * p0 * p1 ^ 2
        + 4 * f1 ^ 2 * p0 ^ 2 * p1 ^ 2 + 4 * f2 ^ 2 * p0 ^ 4 + 16 * p0 ^ 2) / (4 * p0 ^ 4) := by
  obtain ⟨hSv, hS1, hS2⟩ := sin2_facts eS
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have := hF0 (p 1); have := hP0 (p 1)
  simp [riem2C, Fin.sum_univ_four, static_table, kG, cK, hSv, hS1, hS2]
  field_simp
  ring


omit hF hP hS hF0 hP0 hS0 in
open Filter Topology in
/-- The SdS radial profile's two derivatives at `r ≠ 0`. -/
lemma sds_derivs (M Λ r : ℝ) (hr : r ≠ 0) :
    deriv (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) r = 2 * M * (r ^ 2)⁻¹ - 2 * Λ / 3 * r ∧
      deriv (deriv (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2)) r = -(4 * M / r ^ 3) - 2 * Λ / 3 := by
  have hf1 : ∀ s, s ≠ 0 → HasDerivAt (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2)
      (2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s) s := fun s hs =>
    (show HasDerivAt (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) _ s from
      ((hasDerivAt_const s (1 : ℝ)).sub ((hasDerivAt_inv hs).const_mul (2 * M))).sub
        ((hasDerivAt_pow 2 s).const_mul (Λ / 3))).congr_deriv (by norm_num; ring)
  have ed : deriv (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) =ᶠ[𝓝 r]
      fun s => 2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s :=
    Filter.eventually_of_mem (isOpen_ne.mem_nhds hr) fun s hs => (hf1 s hs).deriv
  refine ⟨(hf1 r hr).deriv, ?_⟩
  rw [ed.deriv_eq, (show HasDerivAt (fun s => 2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s) _ r from
      (((hasDerivAt_pow 2 r).inv (pow_ne_zero 2 hr)).const_mul (2 * M)).sub
        ((hasDerivAt_id r).const_mul (2 * Λ / 3))).deriv]
  field_simp; ring

open Filter Topology in
/-- **SdS is Einstein, and its three contractions**, under THE connection: `Ricci = Λg`, `R = 4Λ`,
`R_ab R^ab = 4Λ²`, `K = 48M²/r⁶ + 8Λ²/3` (the last is `sds_kretschmann`). -/
theorem sds_contractions (M Λ : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    (∀ j k, ricC (RK hF hP hS hF0 hP0 hS0 p) j k = Λ * if j = k then cK F P S j p else 0) ∧
      scalC (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 4 * Λ ∧
      ric2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 4 * Λ ^ 2 ∧
      riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 48 * M ^ 2 / p 1 ^ 6 + 8 * Λ ^ 2 / 3 := by
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  obtain ⟨d1, d2⟩ := sds_derivs M Λ r hr
  have hF0v : F r = 1 - 2 * M * r⁻¹ - Λ / 3 * r ^ 2 := eF.eq_of_nhds
  have hF1v : deriv F r = _ := eF.deriv_eq.trans d1
  have hF2v : deriv (deriv F) r = _ := eF.deriv.deriv_eq.trans d2
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  have hf := hF0 r
  have hR : ∀ j k, ricC (RK hF hP hS hF0 hP0 hS0 p) j k = Λ * if j = k then cK F P S j p else 0 := by
    intro j k
    rw [static_ric hF hP hS hF0 hP0 hS0 p eS]
    fin_cases j <;> fin_cases k <;> simp [cK, ← hr_def, hF1v, hF2v, hPv, hP1, hP2] <;> field_simp <;>
      (try simp only [hF0v]) <;> (try field_simp) <;> ring
  refine ⟨hR, ?_, ?_, sds_kretschmann hF hP hS hF0 hP0 hS0 M Λ p eF eP eS⟩ <;>
    have := hF0 (p 1) <;> have := hP0 (p 1) <;> have := hS0 (p 2)
  · simp [scalC, Fin.sum_univ_four, hR, cK]; field_simp; ring
  · simp [ric2C, Fin.sum_univ_four, hR, cK]; field_simp; ring

open Filter Topology in
/-- **Row 81.** SdS is Einstein, so `R_ab R^ab = 4Λ² = 36/α⁴` carries no mass; the Kretschmann scalar
`48M²/r⁶ + 24/α⁴` does, with `∂_M K = 96M/r⁶ ≠ 0` off `M = 0`. -/
theorem row81_separator (M α : ℝ) (hα : α ≠ 0) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹ - 3 / α ^ 2 / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    (∀ j k, ricC (RK hF hP hS hF0 hP0 hS0 p) j k = 3 / α ^ 2 * if j = k then cK F P S j p else 0) ∧
      ric2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 36 / α ^ 4 ∧
      riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 48 * M ^ 2 / p 1 ^ 6 + 24 / α ^ 4 ∧
      HasDerivAt (fun m => 48 * m ^ 2 / p 1 ^ 6 + 24 / α ^ 4) (96 * M / p 1 ^ 6) M := by
  obtain ⟨h1, -, h3, h4⟩ := sds_contractions hF hP hS hF0 hP0 hS0 M _ p eF eP eS
  refine ⟨h1, by rw [h3]; field_simp; ring, by rw [h4]; field_simp; ring, ?_⟩
  exact (show HasDerivAt (fun m => 48 * m ^ 2 / p 1 ^ 6 + 24 / α ^ 4) _ M from
    (((hasDerivAt_pow 2 M).const_mul 48).div_const _).add_const _).congr_deriv (by ring)

open Filter Topology in
/-- **Row 93.** The SdS Riemann tensor splits into a `Λ`-fixed part and a Weyl part: `C_abcd C^abcd = 48M²/r⁶`
(mass-driven), and `K − C² = 24/α⁴` (the `Λ`-only value). -/
theorem row93_weyl_split (M α : ℝ) (hα : α ≠ 0) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹ - 3 / α ^ 2 / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    weyl2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 48 * M ^ 2 / p 1 ^ 6 ∧
      riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p)
        - weyl2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 24 / α ^ 4 := by
  obtain ⟨-, h2, h3, h4⟩ := sds_contractions hF hP hS hF0 hP0 hS0 M _ p eF eP eS
  simp only [weyl2C, h2, h3, h4]
  constructor <;> (field_simp; ring)

open Filter Topology in
/-- **Row 28.** Schwarzschild (`Λ = 0`) along two curves: on the cycloid `r = M(1 + cos z)`,
`K = 48/(M⁴(1 + cos z)⁶)`, which carries `M`; on the bead `r³ = 2Mα² sinh²(3s/2α)`, `K = 12/(α⁴ sinh⁴(3s/2α))`,
and on its small-`s` form `r³ = 2Mα²(3s/2α)²`, `K = 64/(27 s⁴)`: both free of `M`. -/
theorem row28_curves (M : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    (∀ z, p 1 = M * (1 + Real.cos z) →
      riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 48 / (M ^ 4 * (1 + Real.cos z) ^ 6)) ∧
    (∀ α s, p 1 ^ 3 = 2 * M * α ^ 2 * Real.sinh (3 * s / (2 * α)) ^ 2 →
      riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 12 / (α ^ 4 * Real.sinh (3 * s / (2 * α)) ^ 4)) ∧
    (∀ α s, p 1 ^ 3 = 2 * M * α ^ 2 * (3 * s / (2 * α)) ^ 2 →
      riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 64 / (27 * s ^ 4)) := by
  have hr : p 1 ≠ 0 := fun h => hP0 _ (by rw [eP.eq_of_nhds, h]; simp)
  have hK : riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 48 * M ^ 2 / p 1 ^ 6 + 8 * 0 ^ 2 / 3 :=
    sds_kretschmann hF hP hS hF0 hP0 hS0 M 0 p (eF.trans (Eventually.of_forall fun s => by simp)) eP eS
  rw [hK]
  refine ⟨fun z hz => ?_, fun α s hs => ?_, fun α s hs => ?_⟩
  · have : M ≠ 0 := fun h => hr (by rw [hz, h]; ring)
    have : 1 + Real.cos z ≠ 0 := fun h => hr (by rw [hz, h]; ring)
    rw [hz]; field_simp; ring
  · have h3 : p 1 ^ 3 ≠ 0 := pow_ne_zero 3 hr
    have : M ≠ 0 := fun h => h3 (by rw [hs, h]; ring)
    have : α ≠ 0 := fun h => h3 (by rw [hs, h]; ring)
    have : Real.sinh (3 * s / (2 * α)) ≠ 0 := fun h => h3 (by rw [hs, h]; ring)
    rw [show p 1 ^ 6 = (p 1 ^ 3) ^ 2 by ring, hs]; field_simp; ring
  · have h3 : p 1 ^ 3 ≠ 0 := pow_ne_zero 3 hr
    have : M ≠ 0 := fun h => h3 (by rw [hs, h]; ring)
    have : α ≠ 0 := fun h => h3 (by rw [hs, h]; simp)
    have : s ≠ 0 := fun h => h3 (by rw [hs, h]; simp)
    rw [show p 1 ^ 6 = (p 1 ^ 3) ^ 2 by ring, hs]; field_simp; ring

open Filter Topology in
/-- **Row 104, ①.** The flat static metric `−dt² + dr² + r²dΩ²` has every Riemann component zero under THE
connection, so its constant-`t` slice `dr² + r²dΩ²` (a totally geodesic leaf) is flat `ℝ³`. -/
theorem row104_flat_slice (p : Fin 4 → ℝ) (eF : F =ᶠ[𝓝 (p 1)] fun _ => 1) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) (i j k l : Fin 4) :
    RK hF hP hS hF0 hP0 hS0 p i j k l = 0 := by
  set r := p 1 with hr_def
  obtain ⟨hSv, hS1, hS2⟩ := sin2_facts eS
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  have hF0v : F r = 1 := eF.eq_of_nhds
  have hF1v : deriv F r = 0 := by rw [eF.deriv_eq]; simp
  have hF2v : deriv (deriv F) r = 0 := by
    rw [(eF.deriv.trans (Eventually.of_forall fun s => by simp) : deriv F =ᶠ[𝓝 r] fun _ => 0).deriv_eq]; simp
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  rw [static_table]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    (simp [kG, ← hr_def, hF0v, hF1v, hF2v, hPv, hP1, hP2, hSv, hS1, hS2]; try (field_simp; try ring); try simp)

omit hF hP hS hF0 hP0 hS0 in
/-- **Row 104, ②.** At the Nariai mass `M = ρ/3` with `Λ = 1/ρ²` (so `ΛM² = 1/9`), the SdS profile has a
double root at `r = ρ`, `f″(ρ) = −2Λ`: the `dS₂` radius² is `−2/f″ = 1/Λ`, and the `S²` gives `2/ρ² = 2Λ`. -/
theorem row104_nariai_root (ρ : ℝ) (hρ : ρ ≠ 0) :
    let f := fun s => 1 - 2 * (ρ / 3) * s⁻¹ - (1 / ρ ^ 2) / 3 * s ^ 2
    f ρ = 0 ∧ deriv f ρ = 0 ∧ deriv (deriv f) ρ = -2 * (1 / ρ ^ 2) ∧ 2 / ρ ^ 2 = 2 * (1 / ρ ^ 2) ∧
      -2 / deriv (deriv f) ρ = 1 / (1 / ρ ^ 2) := by
  obtain ⟨d1, d2⟩ := sds_derivs (ρ / 3) (1 / ρ ^ 2) ρ hρ
  intro f
  refine ⟨by simp only [f]; field_simp; ring, by rw [d1]; field_simp; ring, by rw [d2]; field_simp; ring,
    by ring, by rw [d2]; field_simp; ring⟩

open Filter Topology in
/-- **Rows 17 and 104, ③: the Nariai geometry `dS₂ × S²`**, `−(1 − Λx²)dt² + dx²/(1 − Λx²) + Λ⁻¹dΩ²`, under THE
connection: `Ricci = Λg` (both radii² are `1/Λ`) and `K = 8Λ²`; with `Λ = 3/α²`, `K = 72/α⁴`, mass-free. -/
theorem nariai_curvature (Λ : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - Λ * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun _ => 1 / Λ)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    (∀ j k, ricC (RK hF hP hS hF0 hP0 hS0 p) j k = Λ * if j = k then cK F P S j p else 0) ∧
      riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 8 * Λ ^ 2 ∧
      ∀ α, Λ = 3 / α ^ 2 → riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 72 / α ^ 4 := by
  set r := p 1 with hr_def
  have hΛ : Λ ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  have hPv : P r = 1 / Λ := eP.eq_of_nhds
  have hP1 : deriv P r = 0 := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 0 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun _ => 0).deriv_eq]; simp
  have e1 : deriv F =ᶠ[𝓝 r] fun s => -(2 * Λ * s) :=
    eF.deriv.trans (Eventually.of_forall fun s => by simp; ring)
  have hF2v : deriv (deriv F) r = -2 * Λ := by
    rw [e1.deriv_eq, (show HasDerivAt (fun s => -(2 * Λ * s)) _ r from
      ((hasDerivAt_id' r).const_mul (2 * Λ)).neg).deriv]; ring
  have hf := hF0 r
  have hR : ∀ j k, ricC (RK hF hP hS hF0 hP0 hS0 p) j k = Λ * if j = k then cK F P S j p else 0 := by
    intro j k
    rw [static_ric hF hP hS hF0 hP0 hS0 p eS]
    fin_cases j <;> fin_cases k <;> simp [cK, ← hr_def, hF2v, hPv, hP1, hP2] <;> field_simp <;> ring
  have hK : riem2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 8 * Λ ^ 2 := by
    rw [static_riem2 hF hP hS hF0 hP0 hS0 p eS]
    simp only [← hr_def, hF2v, hPv, hP1, hP2]; field_simp; ring
  refine ⟨hR, hK, fun α hα => ?_⟩
  have : α ≠ 0 := fun h => hΛ (by rw [hα, h]; simp)
  rw [hK, hα]; field_simp; ring


/-- The Weyl tensor as a map on bivectors, `C_ij^kl`, for a diagonal metric `g` and a curvature table `Rf`:
`Rf` with its Ricci and scalar traces removed, the 4D formula. Its square traced is `weyl2C`. -/
noncomputable def weylB (g : Fin 4 → ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (i j k l : Fin 4) : ℝ :=
  (Rf i j l k - ((if i = k then ricC Rf j l else 0) - (if j = k then ricC Rf i l else 0)
      + (if j = l then g j * ricC Rf i k / g k else 0) - (if i = l then g i * ricC Rf j k / g k else 0)) / 2
    + scalC g Rf / 6 * ((if i = k ∧ j = l then g j else 0) - (if j = k ∧ i = l then g i else 0))) / g l

/-- The cubic Weyl invariant `C_ab^cd C_cd^ef C_ef^ab`. -/
noncomputable def weyl3C (g : Fin 4 → ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : ℝ :=
  ∑ i, ∑ j, ∑ k, ∑ l, weylB g Rf i j k l * ∑ m, ∑ n, weylB g Rf k l m n * weylB g Rf m n i j

/-- SdS's Weyl bivector table: `±2a` on the `tr` and `θφ` planes, `∓a` on the other four, `a = M/r³`. -/
noncomputable def wT (a : ℝ) (i j k l : Fin 4) : ℝ :=
  if (i, j) = (k, l) then (if (i, j) = (0, 1) ∨ (i, j) = (1, 0) ∨ (i, j) = (2, 3) ∨ (i, j) = (3, 2) then 2 * a
    else if i = j then 0 else -a)
  else if (i, j) = (l, k) then (if (i, j) = (0, 1) ∨ (i, j) = (1, 0) ∨ (i, j) = (2, 3) ∨ (i, j) = (3, 2) then -2 * a
    else if i = j then 0 else a)
  else 0

open Filter Topology in
set_option maxHeartbeats 8000000 in
/-- **Row 110.** SdS is Petrov type D in its real invariants: `C² = 48M²/r⁶` (`= 48Ψ₂²`), the cubic
`C³ = 96M³/r⁹` (`= −96Ψ₂³`), and so `(C²)³ = 12(C³)²`, which is `I³ = 27J²` with `I = C²/16`, `J = −C³/96`,
for every `M` and `Λ`. -/
theorem row110_petrov (M Λ : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    weyl2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 48 * M ^ 2 / p 1 ^ 6 ∧
      weyl3C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 96 * M ^ 3 / p 1 ^ 9 ∧
      weyl2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) ^ 3
        = 12 * weyl3C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) ^ 2 := by
  obtain ⟨hR, h2, h3, h4⟩ := sds_contractions hF hP hS hF0 hP0 hS0 M Λ p eF eP eS
  have hW2 : weyl2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 48 * M ^ 2 / p 1 ^ 6 := by
    simp only [weyl2C, h2, h3, h4]; ring
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  obtain ⟨d1, d2⟩ := sds_derivs M Λ r hr
  obtain ⟨hSv, hS1, hS2⟩ := sin2_facts eS
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have hF0v : F r = 1 - 2 * M * r⁻¹ - Λ / 3 * r ^ 2 := eF.eq_of_nhds
  have hF1v : deriv F r = _ := eF.deriv_eq.trans d1
  have hF2v : deriv (deriv F) r = _ := eF.deriv.deriv_eq.trans d2
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  have hf := hF0 r
  have hWB : ∀ i j k l, weylB (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) i j k l = wT (M / r ^ 3) i j k l := by
    intro i j k l
    fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
      (simp only [weylB, h2]; simp [wT, hR, static_table, kG, cK, ← hr_def, hF1v, hF2v, hPv, hP1, hP2, hSv, hS1, hS2]
       try (field_simp; (try simp only [hF0v]); (try field_simp); try ring))
  have hW3 : weyl3C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 96 * M ^ 3 / r ^ 9 := by
    simp only [weyl3C, hWB]
    simp [Fin.sum_univ_four, wT]
    field_simp; ring
  refine ⟨hW2, hW3, ?_⟩
  rw [hW2, hW3]; field_simp; ring

open Filter Topology in
/-- **The radial null tidal matrix vanishes** for `diag(−F, 1/F, r², r²S)`, whatever `F` and `S`. For a radial null
`k = (k⁰, k¹, 0, 0)` (`(k¹)² = F² (k⁰)²`), every screen component of `R(eᵢ, k)k` is zero: Ricci focusing and the
shear source vanish together. -/
theorem static_radial_tidal (p : Fin 4 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) (k0 k1 : ℝ)
    (hk : k1 ^ 2 = F (p 1) ^ 2 * k0 ^ 2) (i j : Fin 4) (hi : i = 2 ∨ i = 3) (hj : j = 2 ∨ j = 3) :
    ∑ a, ∑ b, (![k0, k1, 0, 0] : Fin 4 → ℝ) a * (![k0, k1, 0, 0] : Fin 4 → ℝ) b * RK hF hP hS hF0 hP0 hS0 p i a b j
      = 0 := by
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  have hf := hF0 r; have hs := hS0 (p 2)
  rcases hi with rfl | rfl <;> rcases hj with rfl | rfl <;>
    (simp [Fin.sum_univ_four, static_table, kG, ← hr_def, hPv, hP1, hP2]
     try (field_simp; rw [hk]; ring))

open Filter Topology in
/-- **Row 98.** SdS with `Λ = 3/α²`: it is Einstein, `R_ab = (3/α²) g_ab` (the receipt's Ⓒ①), and on both radial
null congruences the optical tidal matrix vanishes identically (Ⓒ③). -/
theorem row98_einstein_tidal (M α : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹ - 3 / α ^ 2 / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    (∀ j k, ricC (RK hF hP hS hF0 hP0 hS0 p) j k = 3 / α ^ 2 * if j = k then cK F P S j p else 0) ∧
      ∀ k0 k1, k1 ^ 2 = F (p 1) ^ 2 * k0 ^ 2 → ∀ i j, (i = 2 ∨ i = 3) → (j = 2 ∨ j = 3) →
        ∑ a, ∑ b, (![k0, k1, 0, 0] : Fin 4 → ℝ) a * (![k0, k1, 0, 0] : Fin 4 → ℝ) b * RK hF hP hS hF0 hP0 hS0 p i a b j
          = 0 :=
  ⟨(sds_contractions hF hP hS hF0 hP0 hS0 M _ p eF eP eS).1,
    fun k0 k1 hk i j hi hj => static_radial_tidal hF hP hS hF0 hP0 hS0 p eP k0 k1 hk i j hi hj⟩

open Filter Topology in
/-- **Row 71, its non-vacuous instance (`r7351+71`).** On SdS, `C² = 48M²/r⁶`, `E₄ = 48M²/r⁶ + 8Λ²/3`, and the
remainder `2(Ric² − R²/3) = −8Λ²/3`: the identity `weyl2_gb_identity` carries weight here, with `C² ≠ 0` at `M ≠ 0`. -/
theorem row71_sds (M Λ : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    weyl2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 48 * M ^ 2 / p 1 ^ 6 ∧
      gbC (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) = 48 * M ^ 2 / p 1 ^ 6 + 8 * Λ ^ 2 / 3 ∧
      2 * (ric2C (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p)
        - scalC (fun i => cK F P S i p) (RK hF hP hS hF0 hP0 hS0 p) ^ 2 / 3) = -(8 * Λ ^ 2 / 3) := by
  obtain ⟨-, h2, h3, h4⟩ := sds_contractions hF hP hS hF0 hP0 hS0 M Λ p eF eP eS
  simp only [weyl2C, gbC, h2, h3, h4]
  refine ⟨by ring, by ring, by ring⟩

end Inst_Kretschmann

end ShadowProbe

#print axioms ShadowProbe.open_frw_weyl
#print axioms ShadowProbe.gowdy_ds_field
#print axioms ShadowProbe.gowdy_shear_charge
#print axioms ShadowProbe.horo_on_hyperboloid
#print axioms ShadowProbe.open_leaf_curv
#print axioms ShadowProbe.static_K_zero
#print axioms ShadowProbe.frw_K
#print axioms ShadowProbe.frw_K_trace
#print axioms ShadowProbe.gowdy_tz_field
#print axioms ShadowProbe.sds_kretschmann
#print axioms ShadowProbe.static_table
#print axioms ShadowProbe.sin2_facts
#print axioms ShadowProbe.static_ric
#print axioms ShadowProbe.static_riem2
#print axioms ShadowProbe.sds_derivs
#print axioms ShadowProbe.sds_contractions
#print axioms ShadowProbe.row81_separator
#print axioms ShadowProbe.row93_weyl_split
#print axioms ShadowProbe.row28_curves
#print axioms ShadowProbe.row104_flat_slice
#print axioms ShadowProbe.row104_nariai_root
#print axioms ShadowProbe.nariai_curvature
#print axioms ShadowProbe.row110_petrov
#print axioms ShadowProbe.static_radial_tidal
#print axioms ShadowProbe.row98_einstein_tidal
#print axioms ShadowProbe.row71_sds

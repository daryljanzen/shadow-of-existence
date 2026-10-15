import ShadowEngine

/-! # Campaign 3 (`r7339+71`): rows 1 and 3 on exponential Bianchi I

`−dt² + e^{2p₁t}dx² + e^{2p₂t}dy² + e^{2p₃t}dz²` with free constant rates `p₁, p₂, p₃`, through the engine's separable
recipe (`cS`, `dC1_cS`, `dC2_cS`). One `256`-case table, with ONE live coordinate (`t`), carries both rows:
- row 1: on the axisymmetric shear `p = (H − 2σ, H + σ, H + σ)`, `Weyl² = 12σ²(H − 2σ)²`. It vanishes at `σ = 0`, and
  it enters at SECOND order in `σ`;
- row 3: the shear-free member (de Sitter in the flat slicing) has `Weyl² = 0`, and `GB`, `C²` are independent
  directions in the space spanned by `(Riem², Ric², R²)`. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

section Inst_BianchiI

set_option synthInstance.maxHeartbeats 400000

/-- The time profiles `−1, e^{2pᵢt}`, and the trivial second factor of the separable recipe. -/
noncomputable def FbI (p1 p2 p3 : ℝ) : Fin 4 → ℝ → ℝ :=
  ![fun _ => -1, fun s => Real.exp (2 * p1 * s), fun s => Real.exp (2 * p2 * s), fun s => Real.exp (2 * p3 * s)]
noncomputable def GbI : Fin 4 → ℝ → ℝ := fun _ _ => 1

variable (p1 p2 p3 : ℝ)

lemma FbI_smooth (k : Fin 4) : ContDiff ℝ ∞ (FbI p1 p2 p3 k) := by fin_cases k <;> simp [FbI] <;> fun_prop
lemma GbI_smooth (k : Fin 4) : ContDiff ℝ ∞ (GbI k) := contDiff_const
lemma bI_ne (k : Fin 4) (p : Fin 4 → ℝ) : cS (FbI p1 p2 p3) GbI k p ≠ 0 := by
  fin_cases k <;> simp [cS, FbI, GbI, Real.exp_ne_zero]

/-- The Bianchi I table `R(eᵢ,eⱼ)eₖ` component `l`, in the rates and `Eₐ = e^{2pₐt}`. Generated, then proved. -/
noncomputable def bR (p1 p2 p3 E1 E2 E3 : ℝ) (i j k l : Fin 4) : ℝ :=
  let q : Fin 4 → ℝ := ![0, p1, p2, p3]
  let E : Fin 4 → ℝ := ![0, E1, E2, E3]
  if i = 0 ∧ j ≠ 0 ∧ k = 0 ∧ l = j then q j ^ 2
  else if i = 0 ∧ j ≠ 0 ∧ k = j ∧ l = 0 then E j * q j ^ 2
  else if j = 0 ∧ i ≠ 0 ∧ k = 0 ∧ l = i then -(q i ^ 2)
  else if j = 0 ∧ i ≠ 0 ∧ k = i ∧ l = 0 then -(E i * q i ^ 2)
  else if i ≠ 0 ∧ j ≠ 0 ∧ i ≠ j ∧ k = i ∧ l = j then -(E i * q i * q j)
  else if i ≠ 0 ∧ j ≠ 0 ∧ i ≠ j ∧ k = j ∧ l = i then E j * q i * q j
  else 0

/-- THE connection's curvature on basis fields at `p`, for exponential Bianchi I. -/
noncomputable def RbI (p : Fin 4 → ℝ) (i j k : Fin 4) : Fin 4 → ℝ :=
  curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cS (FbI p1 p2 p3) GbI)) (diag4_symm _)
    (fun p u h => diag4_nondeg (fun i => bI_ne p1 p2 p3 i p) u h)
    ((diag4_smooth (cS_smooth (FbI_smooth p1 p2 p3) GbI_smooth)).differentiable (by simp))))
    (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
    (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p

set_option maxHeartbeats 8000000 in
/-- **The table**, for every rate. -/
theorem bianchi_table (p : Fin 4 → ℝ) (i j k l : Fin 4) :
    RbI p1 p2 p3 p i j k l = bR p1 p2 p3 (Real.exp (2 * p1 * p 0)) (Real.exp (2 * p2 * p 0))
      (Real.exp (2 * p3 * p 0)) i j k l := by
  rw [RbI, curvD_eq (bI_ne p1 p2 p3) (cS_smooth (FbI_smooth p1 p2 p3) GbI_smooth)]
  have x1 : ∀ c s, HasDerivAt (fun s => Real.exp (2 * c * s)) (2 * c * Real.exp (2 * c * s)) s := fun c s =>
    HasDerivAt.congr_deriv (((hasDerivAt_id' s).const_mul (2 * c)).exp) (by ring)
  have f1 : ∀ c, deriv (fun s => Real.exp (2 * c * s)) = fun s => 2 * c * Real.exp (2 * c * s) :=
    fun c => funext fun s => (x1 c s).deriv
  have f2 : ∀ c, deriv (fun s => 2 * c * Real.exp (2 * c * s)) = fun s => 4 * c ^ 2 * Real.exp (2 * c * s) :=
    fun c => funext fun s => ((x1 c s).const_mul (2 * c)).deriv.trans (by ring)
  have h1 := fun k v => dC1_cS (FbI_smooth p1 p2 p3) GbI_smooth p k v
  have h2 := fun k u v => dC2_cS (FbI_smooth p1 p2 p3) GbI_smooth p k u v
  have h1' : ∀ k v, fderiv ℝ (cS (FbI p1 p2 p3) GbI k) p v = _ := fun k v => h1 k v
  have hDF : ∀ k, deriv (FbI p1 p2 p3 k) (p 0) = (![0, 2 * p1 * Real.exp (2 * p1 * p 0),
      2 * p2 * Real.exp (2 * p2 * p 0), 2 * p3 * Real.exp (2 * p3 * p 0)] : Fin 4 → ℝ) k := fun k => by
    fin_cases k
    exacts [deriv_const _ _, congrFun (f1 _) _, congrFun (f1 _) _, congrFun (f1 _) _]
  have hDDF : ∀ k, deriv (deriv (FbI p1 p2 p3 k)) (p 0) = (![0, 4 * p1 ^ 2 * Real.exp (2 * p1 * p 0),
      4 * p2 ^ 2 * Real.exp (2 * p2 * p 0), 4 * p3 ^ 2 * Real.exp (2 * p3 * p 0)] : Fin 4 → ℝ) k := fun k => by
    fin_cases k
    · show deriv (deriv fun _ : ℝ => (-1 : ℝ)) (p 0) = 0; simp
    all_goals (show deriv (deriv fun s => Real.exp (2 * _ * s)) (p 0) = _; rw [f1, f2]; rfl)
  have hDG : ∀ k, deriv (GbI k) (p 1) = 0 := fun k => deriv_const _ _
  have hDDG : ∀ k, deriv (deriv (GbI k)) (p 1) = 0 := fun k => by
    show deriv (deriv fun _ : ℝ => (1 : ℝ)) (p 1) = 0; simp
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    (simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, h1', h1, h2, hDF, hDDF, hDG, hDDG]
     simp [cS, FbI, GbI, bR, Fin.sum_univ_four]
     try (field_simp; try ring))

/-- **`Weyl²` of exponential Bianchi I**, for every rate: `(4/3)·Q(p)`, with `Q` the quartic below. -/
theorem bianchi_weyl2 (p : Fin 4 → ℝ) :
    weyl2C (fun i => cS (FbI p1 p2 p3) GbI i p) (RbI p1 p2 p3 p) = 4 / 3 * (p1 ^ 4 - p1 ^ 3 * p2 - p1 ^ 3 * p3
      + p1 ^ 2 * p2 * p3 - p1 * p2 ^ 3 + p1 * p2 ^ 2 * p3 + p1 * p2 * p3 ^ 2 - p1 * p3 ^ 3 + p2 ^ 4 - p2 ^ 3 * p3
      - p2 * p3 ^ 3 + p3 ^ 4) := by
  simp only [weyl2C, riem2C, ric2C, scalC, ricC, bianchi_table]
  simp [Fin.sum_univ_four, bR, cS, FbI, GbI]
  field_simp; ring

omit p1 p2 p3 in
/-- **Row 1.** On the axisymmetric shear `p = (H − 2σ, H + σ, H + σ)` (trace-free part `diag(−2σ, σ, σ)`),
`Weyl² = 12σ²(H − 2σ)²` under THE connection. It vanishes at `σ = 0`, with zero first `σ`-derivative there, so it
enters at second order, with leading coefficient `12H²`. -/
theorem row1_shear (H σ : ℝ) (p : Fin 4 → ℝ) :
    weyl2C (fun i => cS (FbI (H - 2 * σ) (H + σ) (H + σ)) GbI i p) (RbI (H - 2 * σ) (H + σ) (H + σ) p)
        = 12 * σ ^ 2 * (H - 2 * σ) ^ 2 ∧
      HasDerivAt (fun s => 12 * s ^ 2 * (H - 2 * s) ^ 2) 0 0 := by
  refine ⟨by rw [bianchi_weyl2]; ring, ?_⟩
  have := ((((hasDerivAt_id' (0 : ℝ)).pow 2).const_mul 12).mul
    (((hasDerivAt_const (0 : ℝ) H).sub ((hasDerivAt_id' (0 : ℝ)).const_mul 2)).pow 2))
  exact this.congr_deriv (by simp)

omit p1 p2 p3 in
/-- **Row 3.** (a) The shear-free member, `p₁ = p₂ = p₃ = H` (de Sitter in the flat slicing), has `Weyl² = 0`.
(b) In the space spanned by `(Riem², Ric², R²)`, `GB = (1, −4, 1)` and `C² = (1, −2, ⅓)` are independent, and
the one remaining direction is `(1, 1, 3)`, orthogonal to both. -/
theorem row3_rank (H : ℝ) (p : Fin 4 → ℝ) :
    weyl2C (fun i => cS (FbI H H H) GbI i p) (RbI H H H p) = 0 ∧
      (∀ a b : ℝ, (a * 1 + b * 1 = 0 ∧ a * (-4) + b * (-2) = 0 ∧ a * 1 + b * (1 / 3) = 0) → a = 0 ∧ b = 0) ∧
      (1 * 1 + (-4) * 1 + 1 * 3 = (0 : ℝ) ∧ 1 * 1 + (-2) * 1 + (1 / 3) * 3 = (0 : ℝ)) := by
  refine ⟨by rw [bianchi_weyl2]; ring, fun a b ⟨h1, h2, _⟩ => ⟨by linarith, by linarith⟩, by norm_num⟩

end Inst_BianchiI

end ShadowProbe

#print axioms ShadowProbe.bianchi_table
#print axioms ShadowProbe.bianchi_weyl2
#print axioms ShadowProbe.row1_shear
#print axioms ShadowProbe.row3_rank

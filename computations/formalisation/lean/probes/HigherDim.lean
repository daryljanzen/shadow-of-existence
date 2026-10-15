import ShadowEngine

/-! # Campaign 5 (`r7341+71`): the first rows on the engine over `Fin n`

Row 108, `P17_the_cut_is_planar_only_at_M_zero.py`, in three parts:
- (1) a hyperplane section of the substrate `η(X, X) = α²` is the quadric `η(Y, Y) = α² − c²`, by algebra;
- (1′) de Sitter has constant curvature: `dS₅` in the flat slicing, `−dt² + e^{2Ht}Σdxᵢ²`, has
  `R(eᵢ,eⱼ)eₖ = H²(g_jk eᵢ − g_ik eⱼ)` under THE connection, the first `Fin 5` instance;
- (2) SdS's Kretschmann scalar `48M²/r⁶ + 8Λ²/3` (`sds_kretschmann`) has `∂_r K = −288M²/r⁷`, non-zero iff
  `M ≠ 0`, so a SdS member is constant-curvature only at `M = 0`.

Row 35 (below) is the `D = 5` member of `P03_operator_at_general_D.py`.

The receipt's (4)–(5), that no static, spherically symmetric hypersurface of `dS₅` induces SdS at `M ≠ 0`, is an
embedding-nonexistence argument, not a pointwise curvature claim. It is not built. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

section Row108

set_option synthInstance.maxHeartbeats 400000

/-- **(1)** For a symmetric bilinear `η` with `η(n, n) = 1` and `η(n, Y) = 0`, the point `X = c n + Y` lies on
`η(X, X) = α²` iff `η(Y, Y) = α² − c²`: every hyperplane section of the substrate is a quadric of radius²
`α² − c²`. -/
theorem section_quadric {E : Type*} [AddCommGroup E] [Module ℝ E] (η : E →ₗ[ℝ] E →ₗ[ℝ] ℝ)
    (hs : ∀ x y, η x y = η y x) (n Y : E) (hn : η n n = 1) (hY : η n Y = 0) (c α : ℝ) :
    η (c • n + Y) (c • n + Y) = α ^ 2 ↔ η Y Y = α ^ 2 - c ^ 2 := by
  have : η (c • n + Y) (c • n + Y) = c ^ 2 + η Y Y := by
    simp only [map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul, hn, hY, hs Y n]
    ring
  rw [this]; constructor <;> intro h <;> linarith

/-- de Sitter in the flat slicing, on `ℝ⁵`: `−dt² + e^{2Ht}(dx₁² + … + dx₄²)`. -/
noncomputable def cdS5 (H : ℝ) : Fin 5 → (Fin 5 → ℝ) → ℝ :=
  ![fun _ => -1, fun y => Real.exp (2 * H * y 0), fun y => Real.exp (2 * H * y 0),
    fun y => Real.exp (2 * H * y 0), fun y => Real.exp (2 * H * y 0)]

variable (H : ℝ)

lemma cdS5_smooth (k : Fin 5) : ContDiff ℝ ∞ (cdS5 H k) := by fin_cases k <;> simp [cdS5] <;> fun_prop
lemma cdS5_ne (k : Fin 5) (p : Fin 5 → ℝ) : cdS5 H k p ≠ 0 := by
  fin_cases k <;> simp [cdS5, Real.exp_ne_zero]

set_option maxHeartbeats 16000000 in
/-- **(1′) `dS₅` is maximally symmetric under THE connection:** `R(eᵢ,eⱼ)eₖ = H²(g_jk eᵢ − g_ik eⱼ)`. -/
theorem dS5_constant_curvature (p : Fin 5 → ℝ) (i j k l : Fin 5) :
    curv (lcConn (Fin 5 → ℝ) (ndOf (diagN (cdS5 H)) (diagN_symm _)
      (fun p u h => diagN_nondeg (fun i => cdS5_ne H i p) u h)
      ((diagN_smooth (cdS5_smooth H)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 5 → ℝ)) (fun _ => (Pi.single j 1 : Fin 5 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 5 → ℝ)) p l
      = H ^ 2 * ((if j = k then cdS5 H j p else 0) * (if i = l then 1 else 0)
          - (if i = k then cdS5 H i p else 0) * (if j = l then 1 else 0)) := by
  rw [curvDN_eq (cdS5_ne H) (cdS5_smooth H)]
  have hx : ContDiff ℝ ∞ (fun s => Real.exp (2 * H * s)) := by fun_prop
  have x1 : ∀ s, HasDerivAt (fun s => Real.exp (2 * H * s)) (2 * H * Real.exp (2 * H * s)) s := fun s =>
    HasDerivAt.congr_deriv (((hasDerivAt_id' s).const_mul (2 * H)).exp) (by ring)
  have f1 : deriv (fun s => Real.exp (2 * H * s)) = fun s => 2 * H * Real.exp (2 * H * s) :=
    funext fun s => (x1 s).deriv
  have f2 : deriv (fun s => 2 * H * Real.exp (2 * H * s)) = fun s => 4 * H ^ 2 * Real.exp (2 * H * s) :=
    funext fun s => ((x1 s).const_mul (2 * H)).deriv.trans (by ring)
  have hD1 : ∀ k v, fderiv ℝ (cdS5 H k) p v = (![0, 2 * H * Real.exp (2 * H * p 0) * v 0,
      2 * H * Real.exp (2 * H * p 0) * v 0, 2 * H * Real.exp (2 * H * p 0) * v 0,
      2 * H * Real.exp (2 * H * p 0) * v 0] : Fin 5 → ℝ) k := fun k v => by
    fin_cases k
    · simp [cdS5]
    all_goals (show fderiv ℝ (fun y : Fin 5 → ℝ => (fun s => Real.exp (2 * H * s)) (y 0)) p v = _
               rw [co_d1 hx]; simp [f1])
  have hD2 : ∀ k u v, fderiv ℝ (fderiv ℝ (cdS5 H k)) p u v = (![0, 4 * H ^ 2 * Real.exp (2 * H * p 0) * u 0 * v 0,
      4 * H ^ 2 * Real.exp (2 * H * p 0) * u 0 * v 0, 4 * H ^ 2 * Real.exp (2 * H * p 0) * u 0 * v 0,
      4 * H ^ 2 * Real.exp (2 * H * p 0) * u 0 * v 0] : Fin 5 → ℝ) k := fun k u v => by
    fin_cases k
    · simp [cdS5]
    all_goals (show fderiv ℝ (fderiv ℝ (fun y : Fin 5 → ℝ => (fun s => Real.exp (2 * H * s)) (y 0))) p u v = _
               rw [co_d2 hx]; simp [f1, f2])
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    (simp only [curvDN, Pi.sub_apply, Pi.add_apply, DGDN, gamDN, dC1N, dC2N, hD1, hD2]
     simp [cdS5, Fin.sum_univ_five]
     try (field_simp; try ring))

omit H in
/-- **(2)** SdS's Kretschmann scalar, as a function of `r`, has `∂_r K = −288M²/r⁷`, non-zero for every `r ≠ 0`
iff `M ≠ 0`. -/
theorem sds_K_radial (M Λ r : ℝ) (hr : r ≠ 0) :
    HasDerivAt (fun s => 48 * M ^ 2 / s ^ 6 + 8 * Λ ^ 2 / 3) (-(288 * M ^ 2 / r ^ 7)) r ∧
      (-(288 * M ^ 2 / r ^ 7) ≠ 0 ↔ M ≠ 0) := by
  refine ⟨?_, ?_⟩
  · have := ((hasDerivAt_pow 6 r).inv (pow_ne_zero 6 hr)).const_mul (48 * M ^ 2)
    refine (this.add_const (8 * Λ ^ 2 / 3)).congr_of_eventuallyEq ?_ |>.congr_deriv ?_
    · exact Eventually.of_forall fun s => by simp [div_eq_mul_inv]
    · field_simp; ring
  · constructor
    · intro h hM; exact h (by rw [hM]; ring)
    · intro hM h; have := pow_ne_zero 7 hr
      field_simp at h; exact hM (by nlinarith [sq_nonneg M, pow_pos (sq_pos_of_ne_zero hM) 1])

end Row108

/-! ### Row 35, `P03_operator_at_general_D.py`, at `D = 5`: for `−F dt² + dr²/F + r²(da² + sin²a db² + sin²a sin²b dφ²)`,
THE connection's `G^t_t = 3(rF′ + 2F − 2)/(2r²)`, which is `(D−2)/(2r²)[rF′ + (D−3)(F − 1)]` at `D = 5`. So
`G^t_t + Λ = 0` is solved by Tangherlini–de Sitter, `F = 1 − 2M/r² − Λr²/6`. The receipt's other `D` are not built. -/

section Row35

set_option synthInstance.maxHeartbeats 400000

variable {n : ℕ} {k m w : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) (hm : ContDiff ℝ ∞ m) (hw : ContDiff ℝ ∞ w)

include hk hm hw in
/-- The triple-product recipe: first partials of `y ↦ k(yⁱ) m(yʲ) w(yˡ)`. -/
lemma tr_d1 (i j l : Fin n) (y v : Fin n → ℝ) : fderiv ℝ (fun y : Fin n → ℝ => k (y i) * m (y j) * w (y l)) y v
    = deriv k (y i) * v i * m (y j) * w (y l) + k (y i) * (deriv m (y j) * v j) * w (y l)
      + k (y i) * m (y j) * (deriv w (y l) * v l) := by
  rw [(show HasFDerivAt (fun y : Fin n → ℝ => k (y i) * m (y j) * w (y l)) _ y from
    ((fd_coord_i i ((hk.differentiable (by simp)) _)).mul (fd_coord_i j ((hm.differentiable (by simp)) _))).mul
      (fd_coord_i l ((hw.differentiable (by simp)) _))).fderiv]
  simp; ring

include hk hm hw in
/-- The triple-product recipe: second partials. -/
lemma tr_d2 (i j l : Fin n) (p u v : Fin n → ℝ) :
    fderiv ℝ (fderiv ℝ (fun y : Fin n → ℝ => k (y i) * m (y j) * w (y l))) p u v
      = deriv (deriv k) (p i) * u i * v i * m (p j) * w (p l) + deriv k (p i) * v i * (deriv m (p j) * u j) * w (p l)
        + deriv k (p i) * v i * m (p j) * (deriv w (p l) * u l)
        + deriv k (p i) * u i * (deriv m (p j) * v j) * w (p l) + k (p i) * (deriv (deriv m) (p j) * u j * v j) * w (p l)
        + k (p i) * (deriv m (p j) * v j) * (deriv w (p l) * u l)
        + deriv k (p i) * u i * m (p j) * (deriv w (p l) * v l) + k (p i) * (deriv m (p j) * u j) * (deriv w (p l) * v l)
        + k (p i) * m (p j) * (deriv (deriv w) (p l) * u l * v l) := by
  have dk := fun s => ((contDiff_infty_iff_deriv.1 hk).2.differentiable (by simp)) s
  have dm := fun s => ((contDiff_infty_iff_deriv.1 hm).2.differentiable (by simp)) s
  have dw := fun s => ((contDiff_infty_iff_deriv.1 hw).2.differentiable (by simp)) s
  have k0 := fun s => (hk.differentiable (by simp)) s
  have m0 := fun s => (hm.differentiable (by simp)) s
  have w0 := fun s => (hw.differentiable (by simp)) s
  rw [d2_of (F := fun y : Fin n → ℝ => k (y i) * m (y j) * w (y l))
    (((hk.comp (contDiff_apply ℝ ℝ i)).mul (hm.comp (contDiff_apply ℝ ℝ j))).mul (hw.comp (contDiff_apply ℝ ℝ l)))
    (fun y => tr_d1 hk hm hw i j l y v)
    (((((fd_coord_i i (dk _)).mul_const (v i)).mul (fd_coord_i j (m0 _))).mul (fd_coord_i l (w0 _))).add
      (((fd_coord_i i (k0 _)).mul ((fd_coord_i j (dm _)).mul_const (v j))).mul (fd_coord_i l (w0 _))) |>.add
      (((fd_coord_i i (k0 _)).mul (fd_coord_i j (m0 _))).mul ((fd_coord_i l (dw _)).mul_const (v l))))]
  simp; ring

omit hk hm hw

/-- The `D = 5` static metric `−F dt² + dr²/F + P(da² + S db² + S T dφ²)`, coordinates `(t, r, a, b, φ)`. -/
noncomputable def cT5 (F P S T : ℝ → ℝ) : Fin 5 → (Fin 5 → ℝ) → ℝ :=
  ![fun y => -F (y 1), fun y => (F (y 1))⁻¹, fun y => P (y 1), fun y => P (y 1) * S (y 2),
    fun y => P (y 1) * S (y 2) * T (y 3)]

variable {F P S T : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S) (hT : ContDiff ℝ ∞ T)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (hT0 : ∀ s, T s ≠ 0)

include hF hP hS hT hF0 in
lemma cT5_smooth (j : Fin 5) : ContDiff ℝ ∞ (cT5 F P S T j) := by
  fin_cases j
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).neg
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).inv fun y => hF0 _
  · exact hP.comp (contDiff_apply ℝ ℝ 1)
  · exact (hP.comp (contDiff_apply ℝ ℝ 1)).mul (hS.comp (contDiff_apply ℝ ℝ 2))
  · exact ((hP.comp (contDiff_apply ℝ ℝ 1)).mul (hS.comp (contDiff_apply ℝ ℝ 2))).mul (hT.comp (contDiff_apply ℝ ℝ 3))
include hF0 hP0 hS0 hT0 in
lemma cT5_ne (j : Fin 5) (p : Fin 5 → ℝ) : cT5 F P S T j p ≠ 0 := by
  fin_cases j <;> simp [cT5, hF0, hP0, hS0, hT0]

open Filter Topology in
/-- `sin²` and its two derivatives at `θ` (a local copy; `sin2_facts` lives in the instance file). -/
lemma sin2_at {S : ℝ → ℝ} {θ : ℝ} (eS : S =ᶠ[𝓝 θ] fun s => Real.sin s ^ 2) :
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
include hF hP hS hT hF0 hP0 hS0 hT0 in
/-- **Row 35 at `D = 5`.** THE connection's mixed `G^t_t = R^t_t − R/2` of the `D = 5` static metric, for ANY `F`. -/
theorem tangherlini5_Gtt (p : Fin 5 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) (eT : T =ᶠ[𝓝 (p 3)] fun s => Real.sin s ^ 2) :
    let Rf : Fin 5 → Fin 5 → Fin 5 → Fin 5 → ℝ := fun i j k => curv (lcConn (Fin 5 → ℝ) (ndOf (diagN (cT5 F P S T))
      (diagN_symm _) (fun p u h => diagN_nondeg (fun i => cT5_ne hF0 hP0 hS0 hT0 i p) u h)
      ((diagN_smooth (cT5_smooth hF hP hS hT hF0)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 5 → ℝ)) (fun _ => (Pi.single j 1 : Fin 5 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 5 → ℝ)) p
    ricCN Rf 0 0 / cT5 F P S T 0 p - scalCN (fun i => cT5 F P S T i p) Rf / 2
      = 3 * (p 1 * deriv F (p 1) + 2 * F (p 1) - 2) / (2 * p 1 ^ 2) := by
  intro Rf
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  obtain ⟨hSv, hS1, hS2⟩ := sin2_at eS
  obtain ⟨hTv, hT1, hT2⟩ := sin2_at eT
  have hsa : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have hsb : Real.sin (p 3) ≠ 0 := fun h => hT0 (p 3) (by rw [hTv, h]; simp)
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
  have ng1 : deriv (fun s => -F s) = fun s => -deriv F s := funext fun s => deriv.neg
  have hneg : ContDiff ℝ ∞ (fun s => -F s) := hF.neg
  have hinv : ContDiff ℝ ∞ (fun s => (F s)⁻¹) := hF.inv hF0
  have hD1 : ∀ j v, fderiv ℝ (cT5 F P S T j) p v = (![-(deriv F r * v 1), -(deriv F r) / F r ^ 2 * v 1,
      deriv P r * v 1, deriv P r * v 1 * S (p 2) + P r * (deriv S (p 2) * v 2),
      deriv P r * v 1 * S (p 2) * T (p 3) + P r * (deriv S (p 2) * v 2) * T (p 3)
        + P r * S (p 2) * (deriv T (p 3) * v 3)] : Fin 5 → ℝ) j := fun j v => by
    fin_cases j
    · show fderiv ℝ (fun y => (fun s => -F s) (y 1)) p v = _
      rw [co_d1 hneg]; simp [← hr_def, ng1]
    · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1)) p v = _
      rw [co_d1 hinv]; simp [← hr_def, iv1]
    · show fderiv ℝ (fun y => P (y 1)) p v = _
      rw [co_d1 hP]; simp [← hr_def]
    · show fderiv ℝ (fun y => P (y 1) * S (y 2)) p v = _
      rw [pr_d1 hP hS]; simp [← hr_def]
    · show fderiv ℝ (fun y => P (y 1) * S (y 2) * T (y 3)) p v = _
      rw [tr_d1 hP hS hT]; simp [← hr_def]
  have hD2 : ∀ j u v, fderiv ℝ (fderiv ℝ (cT5 F P S T j)) p u v = (![-(deriv (deriv F) r * u 1 * v 1),
      (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 * u 1 * v 1, deriv (deriv P) r * u 1 * v 1,
      deriv (deriv P) r * u 1 * v 1 * S (p 2) + deriv P r * v 1 * (deriv S (p 2) * u 2)
        + deriv P r * u 1 * (deriv S (p 2) * v 2) + P r * (deriv (deriv S) (p 2) * u 2 * v 2),
      deriv (deriv P) r * u 1 * v 1 * S (p 2) * T (p 3) + deriv P r * v 1 * (deriv S (p 2) * u 2) * T (p 3)
        + deriv P r * v 1 * S (p 2) * (deriv T (p 3) * u 3)
        + deriv P r * u 1 * (deriv S (p 2) * v 2) * T (p 3) + P r * (deriv (deriv S) (p 2) * u 2 * v 2) * T (p 3)
        + P r * (deriv S (p 2) * v 2) * (deriv T (p 3) * u 3)
        + deriv P r * u 1 * S (p 2) * (deriv T (p 3) * v 3) + P r * (deriv S (p 2) * u 2) * (deriv T (p 3) * v 3)
        + P r * S (p 2) * (deriv (deriv T) (p 3) * u 3 * v 3)] : Fin 5 → ℝ) j := fun j u v => by
    fin_cases j
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => -F s) (y 1))) p u v = _
      rw [co_d2 hneg]; simp [← hr_def, ng1]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1))) p u v = _
      rw [co_d2 hinv]; simp [← hr_def, iv2]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1))) p u v = _
      rw [co_d2 hP]; simp [← hr_def]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1) * S (y 2))) p u v = _
      rw [pr_d2 hP hS]; simp [← hr_def]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1) * S (y 2) * T (y 3))) p u v = _
      rw [tr_d2 hP hS hT]; simp [← hr_def]
  have hf := hF0 r
  have hR : ∀ i j, Rf i j j i = curvDN (cT5 F P S T) p (Pi.single i 1) (Pi.single j 1) (Pi.single j 1) i :=
    fun i j => by simp only [Rf, curvDN_eq (cT5_ne hF0 hP0 hS0 hT0) (cT5_smooth hF hP hS hT hF0)]
  simp only [ricCN, scalCN, Fin.sum_univ_five, hR]
  simp only [curvDN, Pi.sub_apply, Pi.add_apply, DGDN, gamDN, dC1N, dC2N, hD1, hD2]
  simp [cT5, Fin.sum_univ_five, ← hr_def, hPv, hP1, hP2, hSv, hS1, hS2, hTv, hT1, hT2]
  field_simp
  linear_combination (8 * Real.sin (p 3) ^ 2 * F r) * Real.sin_sq_add_cos_sq (p 2)

open Filter Topology in
include hP0 in
/-- **Row 35's kernel at `D = 5`:** Tangherlini–de Sitter, `F = 1 − 2M/r² − Λr²/6`, solves `G^t_t + Λ = 0`. -/
theorem tangherlini5_kernel (M Λ : ℝ) (p : Fin 5 → ℝ) (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M / s ^ 2 - Λ / 6 * s ^ 2)
    (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    3 * (p 1 * deriv F (p 1) + 2 * F (p 1) - 2) / (2 * p 1 ^ 2) + Λ = 0 := by
  have hr : p 1 ≠ 0 := fun h => hP0 _ (by rw [eP.eq_of_nhds, h]; simp)
  have h1 : HasDerivAt (fun s => 1 - 2 * M / s ^ 2 - Λ / 6 * s ^ 2) (4 * M / p 1 ^ 3 - Λ / 3 * p 1) (p 1) := by
    have := ((hasDerivAt_const (p 1) (1 : ℝ)).sub (((hasDerivAt_pow 2 (p 1)).inv (pow_ne_zero 2 hr)).const_mul
      (2 * M))).sub ((hasDerivAt_pow 2 (p 1)).const_mul (Λ / 6))
    refine (this.congr_of_eventuallyEq (Eventually.of_forall fun s => by simp [div_eq_mul_inv])).congr_deriv ?_
    field_simp; ring
  rw [eF.deriv_eq, h1.deriv, eF.eq_of_nhds]
  field_simp; ring

end Row35

end ShadowProbe

#print axioms ShadowProbe.section_quadric
#print axioms ShadowProbe.dS5_constant_curvature
#print axioms ShadowProbe.sds_K_radial
#print axioms ShadowProbe.tangherlini5_Gtt
#print axioms ShadowProbe.tangherlini5_kernel

import ShadowEngine

/-! # Campaign 16 (`r7371+71.3`): row 35's half, Tangherlini–de Sitter at `D = 4, 6, 7, 8`

`P03_operator_at_general_D.py`: for `−F dt² + dr²/F + r²dΩ²_{D−2}`, `G^t_t = (D−2)(rF′ + (D−3)(F − 1))/(2r²)`, so
`G^t_t + Λ = 0` is solved by `F = 1 − 2M/r^{D−3} − 2Λr²/((D−1)(D−2))`. `D = 5` is `tangherlini5_Gtt` (`r7341+71.5`).

The sphere is in stereographic coordinates: `dΩ² = Ω(x)Σdxᵢ²`, `Ω = 4/(1 + |x|²)²`, smooth and nowhere zero on all of
`ℝ^{D−2}`, so the sphere needs no near-point convention. ONE `Fin n` definition (`cTg`) and ONE set of derivative
lemmas (`Wm_d1`, `Wm_d2`, `cTg_d1`, `cTg_d2`) serve every `D`; only the contraction is run per `D`, on the `r7341`
port (`diagN`, `curvDN_eq`). `P = r²` near the point (the convention, for `P` only); `F` is any smooth nonvanishing
profile. No theorem here is quantified over all `D`. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold Topology

namespace ShadowProbe

section TangAllD

set_option synthInstance.maxHeartbeats 400000

variable {n : ℕ} (m : Fin n → ℝ)

/-- The sphere's squared radius in stereographic coordinates, `Q = Σ mₖ yₖ²` (`m` masks the sphere coordinates). -/
noncomputable def Qm (y : Fin n → ℝ) : ℝ := ∑ k, m k * y k ^ 2

lemma Qm_hasFDerivAt (y : Fin n → ℝ) :
    HasFDerivAt (Qm m) (∑ k, (m k * (2 * y k)) • ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin n => ℝ) k) y := by
  have h := HasFDerivAt.sum (u := Finset.univ) (fun k _ => ((hasFDerivAt_apply (𝕜 := ℝ) k y).pow 2).const_mul (m k))
  have e : Qm m = fun y => ∑ k ∈ Finset.univ, m k * y k ^ 2 := rfl
  rw [e]
  convert h using 1
  · ext y; simp
  · ext v; simp; refine Finset.sum_congr rfl fun k _ => by ring

lemma Qm_fd (y v : Fin n → ℝ) : fderiv ℝ (Qm m) y v = ∑ k, m k * (2 * y k * v k) := by
  rw [(Qm_hasFDerivAt m y).fderiv]; simp
  refine Finset.sum_congr rfl fun k _ => by ring

/-- The bilinear piece `Σ mₖ yₖ vₖ`. -/
noncomputable def Lm (y v : Fin n → ℝ) : ℝ := ∑ k, m k * y k * v k

lemma Lm_hasFDerivAt (y v : Fin n → ℝ) :
    HasFDerivAt (fun y => Lm m y v) (∑ k, (m k * v k) • ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin n => ℝ) k) y := by
  have h := HasFDerivAt.sum (u := Finset.univ) (fun k _ => ((hasFDerivAt_apply (𝕜 := ℝ) k y).const_mul (m k)).mul_const (v k))
  convert h using 1
  · ext y; simp [Lm]
  · ext w; simp; refine Finset.sum_congr rfl fun k _ => by ring

lemma Qm_nonneg (hm : ∀ k, 0 ≤ m k) (y : Fin n → ℝ) : 0 ≤ Qm m y :=
  Finset.sum_nonneg fun k _ => mul_nonneg (hm k) (sq_nonneg _)

lemma Qm_contDiff : ContDiff ℝ ∞ (Qm m) :=
  ContDiff.sum fun k _ => contDiff_const.mul ((contDiff_apply ℝ ℝ k).pow 2)

/-- The stereographic conformal factor `Ω = 4/(1 + Q)²`. -/
noncomputable def Wm (y : Fin n → ℝ) : ℝ := 4 * ((1 + Qm m y) ^ 2)⁻¹

variable {m} (hm : ∀ k, 0 ≤ m k)
include hm

lemma one_add_Qm_ne (y : Fin n → ℝ) : 1 + Qm m y ≠ 0 := by
  have := Qm_nonneg m hm y; positivity

lemma Wm_contDiff : ContDiff ℝ ∞ (Wm m) :=
  contDiff_const.mul ((contDiff_const.add (Qm_contDiff m)).pow 2 |>.inv fun y => pow_ne_zero 2 (one_add_Qm_ne hm y))

lemma Wm_d1 (y v : Fin n → ℝ) : fderiv ℝ (Wm m) y v = -16 * Lm m y v * ((1 + Qm m y) ^ 3)⁻¹ := by
  have h := (show HasFDerivAt (fun y => ((1 + Qm m y) ^ 2)⁻¹) _ y from (hasDerivAt_inv (pow_ne_zero 2 (one_add_Qm_ne hm y))).comp_hasFDerivAt y (((Qm_hasFDerivAt m y).const_add 1).pow 2)).const_mul (4 : ℝ)
  rw [show Wm m = fun y => 4 * ((1 + Qm m y) ^ 2)⁻¹ from rfl, h.fderiv]
  have := one_add_Qm_ne hm y
  simp [Lm]
  field_simp
  rw [Finset.mul_sum, Finset.mul_sum]; refine Finset.sum_congr rfl fun k _ => by ring

lemma Wm_d2 (p u v : Fin n → ℝ) : fderiv ℝ (fderiv ℝ (Wm m)) p u v
    = 96 * Lm m p u * Lm m p v * ((1 + Qm m p) ^ 4)⁻¹ - 16 * (∑ k, m k * u k * v k) * ((1 + Qm m p) ^ 3)⁻¹ := by
  have hQ := (Qm_hasFDerivAt m p).const_add 1
  have hL := ((Lm_hasFDerivAt m p v).const_mul (-16 : ℝ)).mul (show HasFDerivAt (fun y => ((1 + Qm m y) ^ 3)⁻¹) _ p from (hasDerivAt_inv (pow_ne_zero 3 (one_add_Qm_ne hm p))).comp_hasFDerivAt p (hQ.pow 3))
  rw [d2_of (Wm_contDiff hm) (fun y => Wm_d1 hm y v) hL]
  have := one_add_Qm_ne hm p
  simp [Lm]
  field_simp
  have e1 : ∑ x, m x * 2 * p x * u x = 2 * ∑ x, m x * p x * u x := by
    rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun i _ => by ring
  have e2 : ∑ x, m x * v x * u x = ∑ x, m x * u x * v x := Finset.sum_congr rfl fun i _ => by ring
  rw [e1, e2]; ring

omit hm

variable {P : ℝ → ℝ} (hP : ContDiff ℝ ∞ P)

include hm hP in
/-- First partials of a sphere entry `y ↦ P(yʳ)·Ω(y)`. -/
lemma pW_d1 (ir : Fin n) (y v : Fin n → ℝ) : fderiv ℝ (fun y => P (y ir) * Wm m y) y v
    = deriv P (y ir) * v ir * Wm m y + P (y ir) * fderiv ℝ (Wm m) y v := by
  rw [(show HasFDerivAt (fun y => P (y ir) * Wm m y) _ y from (fd_coord_i ir ((hP.differentiable (by simp)) _)).mul
    (((Wm_contDiff hm).differentiable (by simp)) y).hasFDerivAt).fderiv]
  simp; ring

include hm hP in
/-- Second partials of a sphere entry. -/
lemma pW_d2 (ir : Fin n) (p u v : Fin n → ℝ) : fderiv ℝ (fderiv ℝ (fun y => P (y ir) * Wm m y)) p u v
    = deriv (deriv P) (p ir) * u ir * v ir * Wm m p + deriv P (p ir) * v ir * fderiv ℝ (Wm m) p u
      + deriv P (p ir) * u ir * fderiv ℝ (Wm m) p v + P (p ir) * fderiv ℝ (fderiv ℝ (Wm m)) p u v := by
  have dP := fun s => ((contDiff_infty_iff_deriv.1 hP).2.differentiable (by simp)) s
  have hW := Wm_contDiff hm
  rw [d2_of (F := fun y => P (y ir) * Wm m y) ((hP.comp (contDiff_apply ℝ ℝ ir)).mul hW)
    (fun y => pW_d1 hm hP ir y v)
    (HasFDerivAt.add (((fd_coord_i ir (dP _)).mul_const (v ir)).mul ((hW.differentiable (by simp)) p).hasFDerivAt)
      ((fd_coord_i ir ((hP.differentiable (by simp)) _)).mul (fdA_hasFDerivAt hW p v)))]
  simp
  rw [(hW.contDiffAt.isSymmSndFDerivAt (by simp)) u v]
  ring


/-- The static metric `−F dt² + dr²/F + P(r)Ω(x)Σdxᵢ²` on `ℝⁿ`: coordinate `0` is `t`, `ir` is `r`, `m` masks the
sphere's coordinates. -/
noncomputable def cTg (ir : Fin n) (m : Fin n → ℝ) (F P : ℝ → ℝ) : Fin n → (Fin n → ℝ) → ℝ := fun i y =>
  if i.val = 0 then -F (y ir) else if i.val = 1 then (F (y ir))⁻¹ else P (y ir) * Wm m y

variable {F : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0)

include hm hF hP hF0 in
lemma cTg_smooth (ir : Fin n) (j : Fin n) : ContDiff ℝ ∞ (cTg ir m F P j) := by
  unfold cTg
  split_ifs
  · exact (hF.comp (contDiff_apply ℝ ℝ ir)).neg
  · exact (hF.comp (contDiff_apply ℝ ℝ ir)).inv fun y => hF0 _
  · exact (hP.comp (contDiff_apply ℝ ℝ ir)).mul (Wm_contDiff hm)

include hm hF0 hP0 in
lemma cTg_ne (ir : Fin n) (j : Fin n) (p : Fin n → ℝ) : cTg ir m F P j p ≠ 0 := by
  have : Wm m p ≠ 0 := by
    have := one_add_Qm_ne hm p; unfold Wm; positivity
  unfold cTg; split_ifs <;> simp [hF0, hP0, this]

include hm hF hP hF0 in
lemma cTg_d1 (ir : Fin n) (j : Fin n) (p v : Fin n → ℝ) : fderiv ℝ (cTg ir m F P j) p v =
    if j.val = 0 then -(deriv F (p ir) * v ir) else if j.val = 1 then -(deriv F (p ir)) / F (p ir) ^ 2 * v ir
    else deriv P (p ir) * v ir * Wm m p + P (p ir) * fderiv ℝ (Wm m) p v := by
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  unfold cTg
  split_ifs
  · show fderiv ℝ (fun y => (fun s => -F s) (y ir)) p v = _
    rw [co_d1 hF.neg, (show HasDerivAt (fun s => -F s) _ (p ir) from (dF _).neg).deriv]; ring
  · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y ir)) p v = _
    rw [co_d1 (show ContDiff ℝ ∞ (fun s => (F s)⁻¹) from hF.inv hF0), (show HasDerivAt (fun s => (F s)⁻¹) _ (p ir) from (dF _).inv (hF0 _)).deriv]
  · exact pW_d1 hm hP ir p v

include hm hF hP hF0 in
lemma cTg_d2 (ir : Fin n) (j : Fin n) (p u v : Fin n → ℝ) : fderiv ℝ (fderiv ℝ (cTg ir m F P j)) p u v =
    if j.val = 0 then -(deriv (deriv F) (p ir) * u ir * v ir)
    else if j.val = 1 then (2 * deriv F (p ir) ^ 2 - F (p ir) * deriv (deriv F) (p ir)) / F (p ir) ^ 3 * u ir * v ir
    else deriv (deriv P) (p ir) * u ir * v ir * Wm m p + deriv P (p ir) * v ir * fderiv ℝ (Wm m) p u
      + deriv P (p ir) * u ir * fderiv ℝ (Wm m) p v + P (p ir) * fderiv ℝ (fderiv ℝ (Wm m)) p u v := by
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  have dF' := fun s => (((contDiff_infty_iff_deriv.1 hF).2.differentiable (by simp)) s).hasDerivAt
  have iv1 : deriv (fun s => (F s)⁻¹) = fun s => -(deriv F s) / F s ^ 2 :=
    funext fun s => ((dF s).inv (hF0 s)).deriv.trans (by ring)
  unfold cTg
  split_ifs
  · show fderiv ℝ (fderiv ℝ (fun y => (fun s => -F s) (y ir))) p u v = _
    rw [co_d2 hF.neg]
    have : deriv (fun s => -F s) = fun s => -deriv F s := funext fun s => deriv.neg
    rw [this, (show HasDerivAt (fun s => -deriv F s) _ (p ir) from (dF' _).neg).deriv]; ring
  · show fderiv ℝ (fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y ir))) p u v = _
    rw [co_d2 (show ContDiff ℝ ∞ (fun s => (F s)⁻¹) from hF.inv hF0), iv1, (show HasDerivAt (fun s => -deriv F s / F s ^ 2) _ (p ir) from
      (dF' _).neg.div ((dF _).pow 2) (pow_ne_zero 2 (hF0 _))).deriv]
    have := hF0 (p ir); simp only [Pi.neg_apply]; field_simp; ring
  · exact pW_d2 hm hP ir p u v


/-- The sphere mask: coordinates `2, …, n − 1`. -/
noncomputable def mkD (n : ℕ) : Fin n → ℝ := fun k => if 2 ≤ k.val then 1 else 0

lemma mkD_nonneg (n : ℕ) (k : Fin n) : 0 ≤ mkD n k := by unfold mkD; split_ifs <;> norm_num

open Filter Topology in
set_option maxHeartbeats 0 in
include hF hP hF0 hP0 in
/-- **Row 35 at `D = 4`.** THE connection's `G^t_t = R^t_t − R/2` for `−F dt² + dr²/F + P Ω Σdxᵢ²`, any `F`. -/
theorem tangherlini4_Gtt (p : Fin 4 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    let Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ := fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diagN (cTg 1 (mkD 4) F P))
      (diagN_symm _) (fun p u h => diagN_nondeg (fun i => cTg_ne (mkD_nonneg 4) hF0 hP0 1 i p) u h)
      ((diagN_smooth (cTg_smooth (hm := mkD_nonneg 4) (hF := hF) (hP := hP) (hF0 := hF0) 1)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p
    ricCN Rf 0 0 / cTg 1 (mkD 4) F P 0 p - scalCN (fun i => cTg 1 (mkD 4) F P i p) Rf / 2
      = 2 * (p 1 * deriv F (p 1) + 1 * (F (p 1) - 1)) / (2 * p 1 ^ 2) := by
  intro Rf
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  have hf := hF0 r
  have hq := one_add_Qm_ne (mkD_nonneg 4) p
  have hR : ∀ i j, Rf i j j i = curvDN (cTg 1 (mkD 4) F P) p (Pi.single i 1) (Pi.single j 1) (Pi.single j 1) i :=
    fun i j => by simp only [Rf, curvDN_eq (cTg_ne (mkD_nonneg 4) hF0 hP0 1) (cTg_smooth (hm := mkD_nonneg 4) (hF := hF) (hP := hP) (hF0 := hF0) 1)]
  simp only [ricCN, scalCN, Fin.sum_univ_four, hR]
  simp only [curvDN, Pi.sub_apply, Pi.add_apply, DGDN, gamDN, dC1N, dC2N,
    cTg_d1 (hm := mkD_nonneg 4) (hF := hF) (hP := hP) (hF0 := hF0), cTg_d2 (hm := mkD_nonneg 4) (hF := hF) (hP := hP) (hF0 := hF0),
    Wm_d1 (mkD_nonneg 4), Wm_d2 (mkD_nonneg 4)]
  have hQ' : Qm (mkD 4) p = p 2 ^ 2 + p 3 ^ 2 := by simp [Qm, mkD, Fin.sum_univ_four]
  rw [hQ'] at hq
  simp only [Lm, gamDN, Fin.sum_univ_four, cTg_d1 (hm := mkD_nonneg 4) (hF := hF) (hP := hP) (hF0 := hF0),
    Wm_d1 (mkD_nonneg 4)]
  simp [cTg, Wm, hQ', mkD, ← hr_def, hPv, hP1, hP2]
  field_simp
  ring

open Filter Topology in
include hP0 in
/-- **Row 35's kernel at `D = 4`:** `F = 1 − 2M/r^1 − 2Λr²/6` solves `G^t_t + Λ = 0`. -/
theorem tangherlini4_kernel (M Λ : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M / s ^ 1 - 2 * Λ / 6 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    2 * (p 1 * deriv F (p 1) + 1 * (F (p 1) - 1)) / (2 * p 1 ^ 2) + Λ = 0 := by
  have hr : p 1 ≠ 0 := fun h => hP0 _ (by rw [eP.eq_of_nhds, h]; simp)
  have h1 := ((hasDerivAt_const (p 1) (1 : ℝ)).sub (((hasDerivAt_pow 1 (p 1)).inv (pow_ne_zero 1 hr)).const_mul
      (2 * M))).sub ((hasDerivAt_pow 2 (p 1)).const_mul (2 * Λ / 6))
  rw [eF.deriv_eq, (h1.congr_of_eventuallyEq (Eventually.of_forall fun s => by simp [div_eq_mul_inv])).deriv,
    eF.eq_of_nhds]
  field_simp; ring

open Filter Topology in
set_option maxHeartbeats 0 in
include hF hP hF0 hP0 in
/-- **Row 35 at `D = 6`.** THE connection's `G^t_t = R^t_t − R/2` for `−F dt² + dr²/F + P Ω Σdxᵢ²`, any `F`. -/
theorem tangherlini6_Gtt (p : Fin 6 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    let Rf : Fin 6 → Fin 6 → Fin 6 → Fin 6 → ℝ := fun i j k => curv (lcConn (Fin 6 → ℝ) (ndOf (diagN (cTg 1 (mkD 6) F P))
      (diagN_symm _) (fun p u h => diagN_nondeg (fun i => cTg_ne (mkD_nonneg 6) hF0 hP0 1 i p) u h)
      ((diagN_smooth (cTg_smooth (hm := mkD_nonneg 6) (hF := hF) (hP := hP) (hF0 := hF0) 1)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 6 → ℝ)) (fun _ => (Pi.single j 1 : Fin 6 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 6 → ℝ)) p
    ricCN Rf 0 0 / cTg 1 (mkD 6) F P 0 p - scalCN (fun i => cTg 1 (mkD 6) F P i p) Rf / 2
      = 4 * (p 1 * deriv F (p 1) + 3 * (F (p 1) - 1)) / (2 * p 1 ^ 2) := by
  intro Rf
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  have hf := hF0 r
  have hq := one_add_Qm_ne (mkD_nonneg 6) p
  have hR : ∀ i j, Rf i j j i = curvDN (cTg 1 (mkD 6) F P) p (Pi.single i 1) (Pi.single j 1) (Pi.single j 1) i :=
    fun i j => by simp only [Rf, curvDN_eq (cTg_ne (mkD_nonneg 6) hF0 hP0 1) (cTg_smooth (hm := mkD_nonneg 6) (hF := hF) (hP := hP) (hF0 := hF0) 1)]
  simp only [ricCN, scalCN, Fin.sum_univ_six, hR]
  simp only [curvDN, Pi.sub_apply, Pi.add_apply, DGDN, gamDN, dC1N, dC2N,
    cTg_d1 (hm := mkD_nonneg 6) (hF := hF) (hP := hP) (hF0 := hF0), cTg_d2 (hm := mkD_nonneg 6) (hF := hF) (hP := hP) (hF0 := hF0),
    Wm_d1 (mkD_nonneg 6), Wm_d2 (mkD_nonneg 6)]
  have hQ' : Qm (mkD 6) p = p 2 ^ 2 + p 3 ^ 2 + p 4 ^ 2 + p 5 ^ 2 := by simp [Qm, mkD, Fin.sum_univ_six]
  rw [hQ'] at hq
  simp only [Lm, gamDN, Fin.sum_univ_six, cTg_d1 (hm := mkD_nonneg 6) (hF := hF) (hP := hP) (hF0 := hF0),
    Wm_d1 (mkD_nonneg 6)]
  simp [cTg, Wm, hQ', mkD, ← hr_def, hPv, hP1, hP2]
  field_simp
  ring

open Filter Topology in
include hP0 in
/-- **Row 35's kernel at `D = 6`:** `F = 1 − 2M/r^3 − 2Λr²/20` solves `G^t_t + Λ = 0`. -/
theorem tangherlini6_kernel (M Λ : ℝ) (p : Fin 6 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M / s ^ 3 - 2 * Λ / 20 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    4 * (p 1 * deriv F (p 1) + 3 * (F (p 1) - 1)) / (2 * p 1 ^ 2) + Λ = 0 := by
  have hr : p 1 ≠ 0 := fun h => hP0 _ (by rw [eP.eq_of_nhds, h]; simp)
  have h1 := ((hasDerivAt_const (p 1) (1 : ℝ)).sub (((hasDerivAt_pow 3 (p 1)).inv (pow_ne_zero 3 hr)).const_mul
      (2 * M))).sub ((hasDerivAt_pow 2 (p 1)).const_mul (2 * Λ / 20))
  rw [eF.deriv_eq, (h1.congr_of_eventuallyEq (Eventually.of_forall fun s => by simp [div_eq_mul_inv])).deriv,
    eF.eq_of_nhds]
  field_simp; ring

open Filter Topology in
set_option maxHeartbeats 0 in
include hF hP hF0 hP0 in
/-- **Row 35 at `D = 7`.** THE connection's `G^t_t = R^t_t − R/2` for `−F dt² + dr²/F + P Ω Σdxᵢ²`, any `F`. -/
theorem tangherlini7_Gtt (p : Fin 7 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    let Rf : Fin 7 → Fin 7 → Fin 7 → Fin 7 → ℝ := fun i j k => curv (lcConn (Fin 7 → ℝ) (ndOf (diagN (cTg 1 (mkD 7) F P))
      (diagN_symm _) (fun p u h => diagN_nondeg (fun i => cTg_ne (mkD_nonneg 7) hF0 hP0 1 i p) u h)
      ((diagN_smooth (cTg_smooth (hm := mkD_nonneg 7) (hF := hF) (hP := hP) (hF0 := hF0) 1)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 7 → ℝ)) (fun _ => (Pi.single j 1 : Fin 7 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 7 → ℝ)) p
    ricCN Rf 0 0 / cTg 1 (mkD 7) F P 0 p - scalCN (fun i => cTg 1 (mkD 7) F P i p) Rf / 2
      = 5 * (p 1 * deriv F (p 1) + 4 * (F (p 1) - 1)) / (2 * p 1 ^ 2) := by
  intro Rf
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  have hf := hF0 r
  have hq := one_add_Qm_ne (mkD_nonneg 7) p
  have hR : ∀ i j, Rf i j j i = curvDN (cTg 1 (mkD 7) F P) p (Pi.single i 1) (Pi.single j 1) (Pi.single j 1) i :=
    fun i j => by simp only [Rf, curvDN_eq (cTg_ne (mkD_nonneg 7) hF0 hP0 1) (cTg_smooth (hm := mkD_nonneg 7) (hF := hF) (hP := hP) (hF0 := hF0) 1)]
  simp only [ricCN, scalCN, Fin.sum_univ_seven, hR]
  simp only [curvDN, Pi.sub_apply, Pi.add_apply, DGDN, gamDN, dC1N, dC2N,
    cTg_d1 (hm := mkD_nonneg 7) (hF := hF) (hP := hP) (hF0 := hF0), cTg_d2 (hm := mkD_nonneg 7) (hF := hF) (hP := hP) (hF0 := hF0),
    Wm_d1 (mkD_nonneg 7), Wm_d2 (mkD_nonneg 7)]
  have hQ' : Qm (mkD 7) p = p 2 ^ 2 + p 3 ^ 2 + p 4 ^ 2 + p 5 ^ 2 + p 6 ^ 2 := by simp [Qm, mkD, Fin.sum_univ_seven]
  rw [hQ'] at hq
  simp only [Lm, gamDN, Fin.sum_univ_seven, cTg_d1 (hm := mkD_nonneg 7) (hF := hF) (hP := hP) (hF0 := hF0),
    Wm_d1 (mkD_nonneg 7)]
  simp [cTg, Wm, hQ', mkD, ← hr_def, hPv, hP1, hP2]
  field_simp
  ring

open Filter Topology in
include hP0 in
/-- **Row 35's kernel at `D = 7`:** `F = 1 − 2M/r^4 − 2Λr²/30` solves `G^t_t + Λ = 0`. -/
theorem tangherlini7_kernel (M Λ : ℝ) (p : Fin 7 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M / s ^ 4 - 2 * Λ / 30 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    5 * (p 1 * deriv F (p 1) + 4 * (F (p 1) - 1)) / (2 * p 1 ^ 2) + Λ = 0 := by
  have hr : p 1 ≠ 0 := fun h => hP0 _ (by rw [eP.eq_of_nhds, h]; simp)
  have h1 := ((hasDerivAt_const (p 1) (1 : ℝ)).sub (((hasDerivAt_pow 4 (p 1)).inv (pow_ne_zero 4 hr)).const_mul
      (2 * M))).sub ((hasDerivAt_pow 2 (p 1)).const_mul (2 * Λ / 30))
  rw [eF.deriv_eq, (h1.congr_of_eventuallyEq (Eventually.of_forall fun s => by simp [div_eq_mul_inv])).deriv,
    eF.eq_of_nhds]
  field_simp; ring

open Filter Topology in
set_option maxHeartbeats 0 in
include hF hP hF0 hP0 in
/-- **Row 35 at `D = 8`.** THE connection's `G^t_t = R^t_t − R/2` for `−F dt² + dr²/F + P Ω Σdxᵢ²`, any `F`. -/
theorem tangherlini8_Gtt (p : Fin 8 → ℝ) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    let Rf : Fin 8 → Fin 8 → Fin 8 → Fin 8 → ℝ := fun i j k => curv (lcConn (Fin 8 → ℝ) (ndOf (diagN (cTg 1 (mkD 8) F P))
      (diagN_symm _) (fun p u h => diagN_nondeg (fun i => cTg_ne (mkD_nonneg 8) hF0 hP0 1 i p) u h)
      ((diagN_smooth (cTg_smooth (hm := mkD_nonneg 8) (hF := hF) (hP := hP) (hF0 := hF0) 1)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 8 → ℝ)) (fun _ => (Pi.single j 1 : Fin 8 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 8 → ℝ)) p
    ricCN Rf 0 0 / cTg 1 (mkD 8) F P 0 p - scalCN (fun i => cTg 1 (mkD 8) F P i p) Rf / 2
      = 6 * (p 1 * deriv F (p 1) + 5 * (F (p 1) - 1)) / (2 * p 1 ^ 2) := by
  intro Rf
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  have hf := hF0 r
  have hq := one_add_Qm_ne (mkD_nonneg 8) p
  have hR : ∀ i j, Rf i j j i = curvDN (cTg 1 (mkD 8) F P) p (Pi.single i 1) (Pi.single j 1) (Pi.single j 1) i :=
    fun i j => by simp only [Rf, curvDN_eq (cTg_ne (mkD_nonneg 8) hF0 hP0 1) (cTg_smooth (hm := mkD_nonneg 8) (hF := hF) (hP := hP) (hF0 := hF0) 1)]
  simp only [ricCN, scalCN, Fin.sum_univ_eight, hR]
  simp only [curvDN, Pi.sub_apply, Pi.add_apply, DGDN, gamDN, dC1N, dC2N,
    cTg_d1 (hm := mkD_nonneg 8) (hF := hF) (hP := hP) (hF0 := hF0), cTg_d2 (hm := mkD_nonneg 8) (hF := hF) (hP := hP) (hF0 := hF0),
    Wm_d1 (mkD_nonneg 8), Wm_d2 (mkD_nonneg 8)]
  have hQ' : Qm (mkD 8) p = p 2 ^ 2 + p 3 ^ 2 + p 4 ^ 2 + p 5 ^ 2 + p 6 ^ 2 + p 7 ^ 2 := by simp [Qm, mkD, Fin.sum_univ_eight]
  rw [hQ'] at hq
  simp only [Lm, gamDN, Fin.sum_univ_eight, cTg_d1 (hm := mkD_nonneg 8) (hF := hF) (hP := hP) (hF0 := hF0),
    Wm_d1 (mkD_nonneg 8)]
  simp [cTg, Wm, hQ', mkD, ← hr_def, hPv, hP1, hP2]
  field_simp
  ring

open Filter Topology in
include hP0 in
/-- **Row 35's kernel at `D = 8`:** `F = 1 − 2M/r^5 − 2Λr²/42` solves `G^t_t + Λ = 0`. -/
theorem tangherlini8_kernel (M Λ : ℝ) (p : Fin 8 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M / s ^ 5 - 2 * Λ / 42 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) :
    6 * (p 1 * deriv F (p 1) + 5 * (F (p 1) - 1)) / (2 * p 1 ^ 2) + Λ = 0 := by
  have hr : p 1 ≠ 0 := fun h => hP0 _ (by rw [eP.eq_of_nhds, h]; simp)
  have h1 := ((hasDerivAt_const (p 1) (1 : ℝ)).sub (((hasDerivAt_pow 5 (p 1)).inv (pow_ne_zero 5 hr)).const_mul
      (2 * M))).sub ((hasDerivAt_pow 2 (p 1)).const_mul (2 * Λ / 42))
  rw [eF.deriv_eq, (h1.congr_of_eventuallyEq (Eventually.of_forall fun s => by simp [div_eq_mul_inv])).deriv,
    eF.eq_of_nhds]
  field_simp; ring

end TangAllD
end ShadowProbe

#print axioms ShadowProbe.tangherlini4_Gtt
#print axioms ShadowProbe.tangherlini4_kernel
#print axioms ShadowProbe.tangherlini6_Gtt
#print axioms ShadowProbe.tangherlini6_kernel
#print axioms ShadowProbe.tangherlini7_Gtt
#print axioms ShadowProbe.tangherlini7_kernel
#print axioms ShadowProbe.tangherlini8_Gtt
#print axioms ShadowProbe.tangherlini8_kernel

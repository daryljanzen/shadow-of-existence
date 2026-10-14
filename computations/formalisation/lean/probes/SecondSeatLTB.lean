import ShadowEngine

/-! # The second seat's LTB row (`r7333+70`): 13

Lemaître–Tolman–Bondi, `−dt² + R′²/(1+2E) dr² + R² dΩ²` in `(t, r, θ, φ)`, with `R(t, r)` a general TWO-variable
profile. The engine's recipe (`co_d1`/`co_d2`/`pr_d1`/`pr_d2`) covers one-coordinate profiles and their products, so
this file adds the two-variable recipe first, from `d2_of` (a statement, used as the interface gives it). -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

/-! ### `r7333` instance 8, row 13: under the Friedmann constraint `Ṙ² = 2m/R + 2E + ΛR²/3` and its `r`-derivative,
THE connection's `G_tt − Λ = 2m′/(R²R′)` -/

section Inst_R13

set_option synthInstance.maxHeartbeats 400000

/-- `y ↦ (y⁰, y¹)`. -/
noncomputable def pr01 : (Fin 4 → ℝ) →L[ℝ] ℝ × ℝ :=
  (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 0).prod (ContinuousLinearMap.proj 1)

lemma pr01_apply (y : Fin 4 → ℝ) : pr01 y = (y 0, y 1) := rfl

lemma pr01_split (y : Fin 4 → ℝ) : pr01 y = y 0 • ((1 : ℝ), (0 : ℝ)) + y 1 • ((0 : ℝ), (1 : ℝ)) := by
  simp [pr01_apply]

/-- The two-variable partials at `q`: `∂ₐh` and `∂ₐ∂_bh`, with `0 = t`, `1 = r`. -/
noncomputable def e01 : Fin 2 → ℝ × ℝ := ![(1, 0), (0, 1)]
noncomputable def d1h (h : ℝ × ℝ → ℝ) (q : ℝ × ℝ) (a : Fin 2) : ℝ := fderiv ℝ h q (e01 a)
noncomputable def d2h (h : ℝ × ℝ → ℝ) (q : ℝ × ℝ) (a b : Fin 2) : ℝ := fderiv ℝ (fderiv ℝ h) q (e01 a) (e01 b)

variable {h : ℝ × ℝ → ℝ} (hh : ContDiff ℝ ∞ h)

include hh in
lemma tv_has (y : Fin 4 → ℝ) : HasFDerivAt (fun y : Fin 4 → ℝ => h (y 0, y 1)) ((fderiv ℝ h (pr01 y)).comp pr01) y :=
  ((hh.differentiable (by simp)) _).hasFDerivAt.comp y pr01.hasFDerivAt

include hh in
lemma tv_d1 (y v : Fin 4 → ℝ) :
    fderiv ℝ (fun y : Fin 4 → ℝ => h (y 0, y 1)) y v = v 0 * d1h h (y 0, y 1) 0 + v 1 * d1h h (y 0, y 1) 1 := by
  rw [(tv_has hh y).fderiv, ContinuousLinearMap.comp_apply, pr01_split v, map_add, map_smul, map_smul]
  simp [d1h, e01, pr01_apply]

include hh in
lemma tv_line (w : ℝ × ℝ) (q : ℝ × ℝ) :
    HasFDerivAt (fun x => fderiv ℝ h x w) ((fderiv ℝ (fderiv ℝ h) q).flip w) q := by
  have hd := ((hh.fderiv_right (m := ∞) (by simp)).differentiable (by simp)) q
  exact hd.hasFDerivAt.clm_apply (hasFDerivAt_const w q) |>.congr_fderiv
    (by rw [ContinuousLinearMap.comp_zero, zero_add])

include hh in
lemma tv_d2 (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (fun y : Fin 4 → ℝ => h (y 0, y 1))) p u v
      = u 0 * v 0 * d2h h (p 0, p 1) 0 0 + (u 0 * v 1 + u 1 * v 0) * d2h h (p 0, p 1) 0 1
        + u 1 * v 1 * d2h h (p 0, p 1) 1 1 := by
  have hs := (hh.contDiffAt (x := (p 0, p 1))).isSymmSndFDerivAt (by simp)
  have L0 := (tv_line hh ((1 : ℝ), (0 : ℝ)) (pr01 p)).comp p pr01.hasFDerivAt
  have L1 := (tv_line hh ((0 : ℝ), (1 : ℝ)) (pr01 p)).comp p pr01.hasFDerivAt
  rw [d2_of (F := fun y : Fin 4 → ℝ => h (y 0, y 1)) (hh.comp pr01.contDiff) (fun y => tv_d1 hh y v)
    (((L0.const_mul (v 0)).add (L1.const_mul (v 1))).congr_of_eventuallyEq
      (Eventually.of_forall fun y => by simp [d1h, e01, pr01_apply]))]
  simp only [add_apply, smul_apply, ContinuousLinearMap.comp_apply,
    ContinuousLinearMap.flip_apply, smul_eq_mul]
  rw [pr01_split u]
  simp only [map_add, map_smul, add_apply, smul_apply, smul_eq_mul]
  simp only [d2h, e01, pr01_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
  rw [hs ((0 : ℝ), (1 : ℝ)) ((1 : ℝ), (0 : ℝ))]
  ring

variable {k : ℝ → ℝ} (hk : ContDiff ℝ ∞ k)

include hh hk in
lemma tvp_d1 (y v : Fin 4 → ℝ) :
    fderiv ℝ (fun y : Fin 4 → ℝ => h (y 0, y 1) * k (y 2)) y v
      = (v 0 * d1h h (y 0, y 1) 0 + v 1 * d1h h (y 0, y 1) 1) * k (y 2) + h (y 0, y 1) * (deriv k (y 2) * v 2) := by
  have H : HasFDerivAt (fun y : Fin 4 → ℝ => h (y 0, y 1) * k (y 2)) _ y :=
    (tv_has hh y).mul (fd_coord_i 2 ((hk.differentiable (by simp)) _))
  rw [H.fderiv]
  simp only [add_apply, smul_apply, ContinuousLinearMap.comp_apply,
    smul_eq_mul, ContinuousLinearMap.proj_apply]
  rw [pr01_split v, map_add, map_smul, map_smul]
  simp [d1h, e01, pr01_apply]; ring

include hh hk in
lemma tvp_d2 (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (fun y : Fin 4 → ℝ => h (y 0, y 1) * k (y 2))) p u v
      = (u 0 * v 0 * d2h h (p 0, p 1) 0 0 + (u 0 * v 1 + u 1 * v 0) * d2h h (p 0, p 1) 0 1
          + u 1 * v 1 * d2h h (p 0, p 1) 1 1) * k (p 2)
        + (v 0 * d1h h (p 0, p 1) 0 + v 1 * d1h h (p 0, p 1) 1) * (deriv k (p 2) * u 2)
        + (u 0 * d1h h (p 0, p 1) 0 + u 1 * d1h h (p 0, p 1) 1) * (deriv k (p 2) * v 2)
        + h (p 0, p 1) * (deriv (deriv k) (p 2) * u 2 * v 2) := by
  have hs := (hh.contDiffAt (x := (p 0, p 1))).isSymmSndFDerivAt (by simp)
  have L0 := (tv_line hh ((1 : ℝ), (0 : ℝ)) (pr01 p)).comp p pr01.hasFDerivAt
  have L1 := (tv_line hh ((0 : ℝ), (1 : ℝ)) (pr01 p)).comp p pr01.hasFDerivAt
  have K0 := fd_coord_i (x := p) 2 ((hk.differentiable (by simp)) (p 2))
  have K1 := fd_coord_i (x := p) 2 (((contDiff_infty_iff_deriv.1 hk).2.differentiable (by simp)) (p 2))
  have H := tv_has hh p
  rw [d2_of (F := fun y : Fin 4 → ℝ => h (y 0, y 1) * k (y 2))
    ((hh.comp pr01.contDiff).mul (hk.comp (contDiff_apply ℝ ℝ 2))) (fun y => tvp_d1 hh hk y v)
    (((((L0.const_mul (v 0)).add (L1.const_mul (v 1))).mul K0).add (H.mul (K1.mul_const (v 2)))).congr_of_eventuallyEq
      (Eventually.of_forall fun y => by simp [d1h, e01, pr01_apply]))]
  simp only [add_apply, smul_apply, ContinuousLinearMap.comp_apply,
    ContinuousLinearMap.flip_apply, smul_eq_mul, ContinuousLinearMap.proj_apply, Pi.add_apply,
    Function.comp_apply]
  rw [pr01_split u]
  simp only [map_add, map_smul, add_apply, smul_apply, smul_eq_mul]
  simp only [d1h, d2h, e01, pr01_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
  rw [hs ((0 : ℝ), (1 : ℝ)) ((1 : ℝ), (0 : ℝ))]
  ring

/-- The LTB coefficients, with `g_rr = Q(t, r)` and `g_θθ = W(t, r)` as two-variable profiles. -/
noncomputable def cLT (Q W : ℝ × ℝ → ℝ) (S : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun _ => -1, fun y => Q (y 0, y 1), fun y => W (y 0, y 1), fun y => W (y 0, y 1) * S (y 2)]

omit hh in
lemma cLT_smooth {Q W : ℝ × ℝ → ℝ} {S : ℝ → ℝ} (hQ : ContDiff ℝ ∞ Q) (hW : ContDiff ℝ ∞ W) (hS : ContDiff ℝ ∞ S)
    (j : Fin 4) : ContDiff ℝ ∞ (cLT Q W S j) := by
  fin_cases j
  · exact contDiff_const
  · exact hQ.comp pr01.contDiff
  · exact hW.comp pr01.contDiff
  · exact (hW.comp pr01.contDiff).mul (hS.comp (contDiff_apply ℝ ℝ 2))
omit hh in
lemma cLT_ne {Q W : ℝ × ℝ → ℝ} {S : ℝ → ℝ} (hQ0 : ∀ x, Q x ≠ 0) (hW0 : ∀ x, W x ≠ 0) (hS0 : ∀ s, S s ≠ 0)
    (j : Fin 4) (p : Fin 4 → ℝ) : cLT Q W S j p ≠ 0 := by
  fin_cases j <;> simp [cLT, hQ0, hW0, hS0]

open Filter Topology in
set_option maxHeartbeats 8000000 in
omit hh in
/-- `G_tt` of `−dt² + Q dr² + W dΩ²` in closed form: first partials of `Q` and `W`, and `W_rr`. -/
theorem ltb_Gtt {Q W : ℝ × ℝ → ℝ} {S : ℝ → ℝ} (hQ : ContDiff ℝ ∞ Q) (hW : ContDiff ℝ ∞ W)
    (hS : ContDiff ℝ ∞ S) (hQ0 : ∀ x, Q x ≠ 0) (hW0 : ∀ x, W x ≠ 0) (hS0 : ∀ s, S s ≠ 0) (p : Fin 4 → ℝ)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    einsteinC (fun i => cLT Q W S i p) (fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cLT Q W S))
      (diag4_symm _) (fun p u h => diag4_nondeg (fun i => cLT_ne hQ0 hW0 hS0 i p) u h)
      ((diag4_smooth (cLT_smooth hQ hW hS)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p) 0 0
      = let q := (p 0, p 1)
        d1h Q q 0 * d1h W q 0 / (2 * Q q * W q) + d1h W q 0 ^ 2 / (4 * W q ^ 2) + 1 / W q
          - d2h W q 1 1 / (Q q * W q) + d1h W q 1 ^ 2 / (4 * Q q * W q ^ 2)
          + d1h Q q 1 * d1h W q 1 / (2 * Q q ^ 2 * W q) := by
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
  have hD1 : ∀ j v, fderiv ℝ (cLT Q W S j) p v = (![0,
      v 0 * d1h Q (p 0, p 1) 0 + v 1 * d1h Q (p 0, p 1) 1, v 0 * d1h W (p 0, p 1) 0 + v 1 * d1h W (p 0, p 1) 1,
      (v 0 * d1h W (p 0, p 1) 0 + v 1 * d1h W (p 0, p 1) 1) * S (p 2) + W (p 0, p 1) * (deriv S (p 2) * v 2)]
      : Fin 4 → ℝ) j := fun j v => by
    fin_cases j
    · simp [cLT]
    · exact tv_d1 hQ p v
    · exact tv_d1 hW p v
    · exact tvp_d1 hW hS p v
  have hD2 : ∀ j u v, fderiv ℝ (fderiv ℝ (cLT Q W S j)) p u v = (![0,
      u 0 * v 0 * d2h Q (p 0, p 1) 0 0 + (u 0 * v 1 + u 1 * v 0) * d2h Q (p 0, p 1) 0 1
        + u 1 * v 1 * d2h Q (p 0, p 1) 1 1,
      u 0 * v 0 * d2h W (p 0, p 1) 0 0 + (u 0 * v 1 + u 1 * v 0) * d2h W (p 0, p 1) 0 1
        + u 1 * v 1 * d2h W (p 0, p 1) 1 1,
      (u 0 * v 0 * d2h W (p 0, p 1) 0 0 + (u 0 * v 1 + u 1 * v 0) * d2h W (p 0, p 1) 0 1
          + u 1 * v 1 * d2h W (p 0, p 1) 1 1) * S (p 2)
        + (v 0 * d1h W (p 0, p 1) 0 + v 1 * d1h W (p 0, p 1) 1) * (deriv S (p 2) * u 2)
        + (u 0 * d1h W (p 0, p 1) 0 + u 1 * d1h W (p 0, p 1) 1) * (deriv S (p 2) * v 2)
        + W (p 0, p 1) * (deriv (deriv S) (p 2) * u 2 * v 2)] : Fin 4 → ℝ) j := fun j u v => by
    fin_cases j
    · simp [cLT]
    · exact tv_d2 hQ p u v
    · exact tv_d2 hW p u v
    · exact tvp_d2 hW hS p u v
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have hq := hQ0 (p 0, p 1); have hw := hW0 (p 0, p 1)
  simp only [einsteinC, scalC, ricC, Fin.sum_univ_four, curvD_eq (cLT_ne hQ0 hW0 hS0) (cLT_smooth hQ hW hS)]
  simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
  simp [cLT, Fin.sum_univ_four, hSv, hS1, hS2]
  field_simp
  ring

open Filter Topology in
/-- `W = R²`: its first partials and `W_rr`. -/
lemma sq2_partials {R : ℝ × ℝ → ℝ} (hR : ContDiff ℝ ∞ R) (q : ℝ × ℝ) (a : Fin 2) :
    d1h (fun x => R x ^ 2) q a = 2 * R q * d1h R q a
      ∧ d2h (fun x => R x ^ 2) q 1 1 = 2 * d1h R q 1 ^ 2 + 2 * R q * d2h R q 1 1 := by
  have dR : ∀ x, HasFDerivAt R (fderiv ℝ R x) x := fun x => ((hR.differentiable (by simp)) x).hasFDerivAt
  have d2R := ((hR.fderiv_right (m := ∞) (by simp)).differentiable (by simp)) q
  have e : fderiv ℝ (fun x => R x ^ 2) = fun x => (2 * R x) • fderiv ℝ R x := funext fun x => by
    rw [((dR x).pow 2).fderiv]; ext <;> simp
  refine ⟨by simp only [d1h, e]; simp, ?_⟩
  simp only [d2h, e]
  have H : HasFDerivAt (fun x => (2 * R x) • fderiv ℝ R x) _ q := ((dR q).const_mul 2).smul d2R.hasFDerivAt
  rw [H.fderiv]
  simp [d1h, e01]; ring

open Filter Topology in
/-- `Q = R′²/(1 + 2E)` near `q`: its value and first partials at `q`. -/
lemma rr_partials {R Q : ℝ × ℝ → ℝ} {E : ℝ → ℝ} (hR : ContDiff ℝ ∞ R) (hE : ContDiff ℝ ∞ E) (q : ℝ × ℝ)
    (hD : 1 + 2 * E q.2 ≠ 0) (eQ : Q =ᶠ[𝓝 q] fun x => d1h R x 1 ^ 2 / (1 + 2 * E x.2)) :
    Q q = d1h R q 1 ^ 2 / (1 + 2 * E q.2)
      ∧ d1h Q q 0 = 2 * d1h R q 1 * d2h R q 0 1 / (1 + 2 * E q.2)
      ∧ d1h Q q 1 = 2 * d1h R q 1 * d2h R q 1 1 / (1 + 2 * E q.2)
          - d1h R q 1 ^ 2 * (2 * deriv E q.2) / (1 + 2 * E q.2) ^ 2 := by
  have hN : HasFDerivAt (fun x => d1h R x 1 ^ 2) _ q := (tv_line hR (e01 1) q).pow 2
  have hDen : HasFDerivAt (fun x : ℝ × ℝ => 1 + 2 * E x.2) _ q := (hasFDerivAt_const (1 : ℝ) q).add
    ((((hE.differentiable (by simp)) q.2).hasDerivAt.comp_hasFDerivAt q
      (hasFDerivAt_snd (𝕜 := ℝ) (p := q))).const_mul 2)
  have hInv : HasFDerivAt (fun x : ℝ × ℝ => (1 + 2 * E x.2)⁻¹) _ q := (hasDerivAt_inv hD).comp_hasFDerivAt q hDen
  have H : HasFDerivAt (fun x => d1h R x 1 ^ 2 * (1 + 2 * E x.2)⁻¹) _ q := hN.mul hInv
  have eQ' : Q =ᶠ[𝓝 q] fun x => d1h R x 1 ^ 2 * (1 + 2 * E x.2)⁻¹ :=
    eQ.trans (Eventually.of_forall fun x => div_eq_mul_inv _ _)
  have hd : fderiv ℝ Q q = _ := eQ'.fderiv_eq.trans H.fderiv
  refine ⟨eQ.eq_of_nhds, ?_, ?_⟩ <;>
  · simp only [d1h, hd]
    simp [e01, d2h]
    field_simp
    try ring

open Filter Topology in
omit hh in
/-- **Row 13.** On LTB, with `R(t, r)` a two-variable profile, `g_rr = Q` equal to `R′²/(1+2E)` near the point, and
the Friedmann constraint and its `r`-derivative at the point, `G_tt − Λ = 2m′/(R²R′)`. -/
theorem ltb_bend {R Q : ℝ × ℝ → ℝ} {E m S : ℝ → ℝ} (hR : ContDiff ℝ ∞ R) (hQ : ContDiff ℝ ∞ Q)
    (hE : ContDiff ℝ ∞ E) (hS : ContDiff ℝ ∞ S) (hR0 : ∀ x, R x ≠ 0) (hQ0 : ∀ x, Q x ≠ 0) (hS0 : ∀ s, S s ≠ 0)
    (Λ : ℝ) (p : Fin 4 → ℝ) (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2)
    (eQ : Q =ᶠ[𝓝 (p 0, p 1)] fun x => d1h R x 1 ^ 2 / (1 + 2 * E x.2))
    (hc0 : d1h R (p 0, p 1) 0 ^ 2 = 2 * m (p 1) / R (p 0, p 1) + 2 * E (p 1) + Λ * R (p 0, p 1) ^ 2 / 3)
    (hc1 : 2 * d1h R (p 0, p 1) 0 * d2h R (p 0, p 1) 0 1 = 2 * deriv m (p 1) / R (p 0, p 1)
      - 2 * m (p 1) * d1h R (p 0, p 1) 1 / R (p 0, p 1) ^ 2 + 2 * deriv E (p 1)
      + 2 * Λ * R (p 0, p 1) * d1h R (p 0, p 1) 1 / 3) :
    einsteinC (fun i => cLT Q (fun x => R x ^ 2) S i p) (fun i j k => curv (lcConn (Fin 4 → ℝ)
      (ndOf (diag4 (cLT Q (fun x => R x ^ 2) S)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cLT_ne hQ0 (fun x => pow_ne_zero 2 (hR0 x)) hS0 i p) u h)
      ((diag4_smooth (cLT_smooth hQ (hR.pow 2) hS)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p) 0 0 - Λ
      = 2 * deriv m (p 1) / (R (p 0, p 1) ^ 2 * d1h R (p 0, p 1) 1) := by
  rw [ltb_Gtt hQ (hR.pow 2) hS hQ0 (fun x => pow_ne_zero 2 (hR0 x)) hS0 p eS]
  have hQq := hQ0 (p 0, p 1)
  have hD : 1 + 2 * E (p 0, p 1).2 ≠ 0 := fun h => hQq (by rw [eQ.eq_of_nhds, h]; simp)
  have hRr : d1h R (p 0, p 1) 1 ≠ 0 := fun h => hQq (by rw [eQ.eq_of_nhds, h]; simp)
  obtain ⟨qv, q0, q1⟩ := rr_partials hR hE (p 0, p 1) hD eQ
  obtain ⟨w0, -⟩ := sq2_partials hR (p 0, p 1) 0
  obtain ⟨w1, w11⟩ := sq2_partials hR (p 0, p 1) 1
  have hr := hR0 (p 0, p 1)
  simp only [qv, q0, q1, w0, w1, w11]
  linear_combination (norm := (field_simp; ring))
    (1 / R (p 0, p 1) ^ 2) * hc0 + (1 / (R (p 0, p 1) * d1h R (p 0, p 1) 1)) * hc1

end Inst_R13

#print axioms ltb_Gtt
#print axioms ltb_bend

end ShadowProbe

import Mathlib

/-! # `r7613+71.2`, campaign 58: `lem:alignment`'s computational half

Source: `corpus/BH_causality_v2.tex`, `lem:alignment` (ii). Registration:
`computations/formalisation/r7613_71_campaign58/PREDICTION.md`.

Here `f r = 1 − rh/r` with `rh > 0`.
* **Static slicing.** `g = diag(−f, f⁻¹, r², r² sin²θ)`, its explicit inverse, `g⁻¹ = ginv` as `Matrix.inv`,
  `g^{tt} = −(1 − rh/r)⁻¹ → −∞` and `N = √f → 0` as `r → rh⁺`, with `N² = −1/g^{tt}`.
* **Retarded slicing.** In `(u, r)`: the block `!![−f, −1; −1, 0]`, its inverse `!![0, −1; −1, f]` (and the
  4×4 version with the angular block), and for `Θ = a(u + ηr)`:
  `g^{ab}∂aΘ∂bΘ = a²(fη² − 2η) = a²η(fη − 2) → −2a²η`, negative near `rh` (both sides of it). -/

open Real Filter Topology Set Matrix

namespace ShadowProbe.SchwarzschildSlicing

/-- `f r = 1 − rh/r`. -/
noncomputable def f (rh r : ℝ) : ℝ := 1 - rh / r

lemma f_pos {rh r : ℝ} (hrh : 0 < rh) (hr : rh < r) : 0 < f rh r := by
  have hr0 : 0 < r := hrh.trans hr
  unfold f
  rw [sub_pos, div_lt_one hr0]; exact hr

lemma f_rh {rh : ℝ} (hrh : 0 < rh) : f rh rh = 0 := by
  unfold f; rw [div_self hrh.ne']; ring

lemma f_continuousAt {rh : ℝ} (hrh : 0 < rh) : ContinuousAt (f rh) rh := by
  unfold f
  exact continuousAt_const.sub (continuousAt_const.div continuousAt_id hrh.ne')

lemma f_tendsto {rh : ℝ} (hrh : 0 < rh) : Tendsto (f rh) (𝓝 rh) (𝓝 0) := by
  have := (f_continuousAt hrh).tendsto
  rwa [f_rh hrh] at this

/-- `f → 0⁺` as `r → rh⁺`. -/
lemma f_tendsto_nhdsGT {rh : ℝ} (hrh : 0 < rh) :
    Tendsto (f rh) (𝓝[>] rh) (𝓝[>] 0) := by
  apply tendsto_nhdsWithin_iff.2
  refine ⟨(f_tendsto hrh).mono_left nhdsWithin_le_nhds, ?_⟩
  filter_upwards [self_mem_nhdsWithin] with r hr
  exact f_pos hrh hr

/-! ## 1. Static slicing -/

/-- The Schwarzschild metric `diag(−f, f⁻¹, r², r² sin²θ)` in `(t, r, θ, φ)`. -/
noncomputable def gS (rh r θ : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  diagonal ![-f rh r, (f rh r)⁻¹, r ^ 2, r ^ 2 * sin θ ^ 2]

/-- Its claimed inverse. -/
noncomputable def gSinv (rh r θ : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  diagonal ![-(f rh r)⁻¹, f rh r, (r ^ 2)⁻¹, (r ^ 2 * sin θ ^ 2)⁻¹]

theorem ss_static_mul_inv {rh r θ : ℝ} (hrh : 0 < rh) (hr : rh < r) (hs : sin θ ≠ 0) :
    gS rh r θ * gSinv rh r θ = 1 := by
  have hf := (f_pos hrh hr).ne'
  have hr0 : r ≠ 0 := (hrh.trans hr).ne'
  unfold gS gSinv
  rw [diagonal_mul_diagonal, ← diagonal_one]
  congr 1
  funext i
  fin_cases i <;> simp [hf, hr0] <;> field_simp

theorem ss_static_inv_mul {rh r θ : ℝ} (hrh : 0 < rh) (hr : rh < r) (hs : sin θ ≠ 0) :
    gSinv rh r θ * gS rh r θ = 1 := by
  have hf := (f_pos hrh hr).ne'
  have hr0 : r ≠ 0 := (hrh.trans hr).ne'
  unfold gS gSinv
  rw [diagonal_mul_diagonal, ← diagonal_one]
  congr 1
  funext i
  fin_cases i <;> simp [hf, hr0] <;> field_simp

/-- `Matrix.inv` of the metric is the explicit inverse. -/
theorem ss_static_inv_eq {rh r θ : ℝ} (hrh : 0 < rh) (hr : rh < r) (hs : sin θ ≠ 0) :
    (gS rh r θ)⁻¹ = gSinv rh r θ :=
  Matrix.inv_eq_right_inv (ss_static_mul_inv hrh hr hs)

/-- `g^{tt} = −(1 − rh/r)⁻¹`. -/
theorem ss_static_gtt {rh r θ : ℝ} (hrh : 0 < rh) (hr : rh < r) (hs : sin θ ≠ 0) :
    (gS rh r θ)⁻¹ 0 0 = -(1 - rh / r)⁻¹ := by
  rw [ss_static_inv_eq hrh hr hs]
  simp [gSinv, f]

/-- `g^{tt} = −f⁻¹ → −∞` as `r → rh⁺`. -/
theorem ss_static_gtt_tendsto {rh : ℝ} (hrh : 0 < rh) :
    Tendsto (fun r => -(1 - rh / r)⁻¹) (𝓝[>] rh) atBot := by
  have h := tendsto_inv_nhdsGT_zero.comp (f_tendsto_nhdsGT hrh)
  exact tendsto_neg_atTop_atBot.comp h

/-- The same, stated for the `(0,0)` entry of `Matrix.inv` of the metric (any `θ` with `sin θ ≠ 0`). -/
theorem ss_static_gtt_matrix_tendsto {rh θ : ℝ} (hrh : 0 < rh) (hs : sin θ ≠ 0) :
    Tendsto (fun r => (gS rh r θ)⁻¹ 0 0) (𝓝[>] rh) atBot := by
  refine (ss_static_gtt_tendsto hrh).congr' ?_
  filter_upwards [self_mem_nhdsWithin] with r hr
  exact (ss_static_gtt hrh hr hs).symm

/-- The static lapse `N = √f`. -/
noncomputable def N (rh r : ℝ) : ℝ := Real.sqrt (f rh r)

/-- `N → 0` as `r → rh⁺`. -/
theorem ss_lapse_tendsto {rh : ℝ} (hrh : 0 < rh) :
    Tendsto (N rh) (𝓝[>] rh) (𝓝 0) := by
  have h := (Real.continuous_sqrt.tendsto 0).comp
    ((f_tendsto hrh).mono_left (nhdsWithin_le_nhds (s := Ioi rh)))
  rw [Real.sqrt_zero] at h
  exact h

/-- `N² = −1/g^{tt}`. -/
theorem ss_lapse_sq {rh r θ : ℝ} (hrh : 0 < rh) (hr : rh < r) (hs : sin θ ≠ 0) :
    N rh r ^ 2 = -1 / (gS rh r θ)⁻¹ 0 0 := by
  have hf := f_pos hrh hr
  rw [ss_static_gtt hrh hr hs, N, Real.sq_sqrt hf.le]
  change f rh r = -1 / -(f rh r)⁻¹
  rw [div_neg, neg_div, neg_neg, one_div, inv_inv]

/-- `N = (−g^{tt})^{−1/2}`. -/
theorem ss_lapse_rpow {rh r θ : ℝ} (hrh : 0 < rh) (hr : rh < r) (hs : sin θ ≠ 0) :
    N rh r = (-(gS rh r θ)⁻¹ 0 0) ^ (-(1 / 2 : ℝ)) := by
  have hf := f_pos hrh hr
  rw [ss_static_gtt hrh hr hs]
  change N rh r = (-(-(f rh r)⁻¹)) ^ (-(1 / 2 : ℝ))
  rw [neg_neg, Real.rpow_neg (inv_nonneg.2 hf.le), Real.inv_rpow hf.le, inv_inv, N,
    Real.sqrt_eq_rpow]

/-! ## 2. Retarded slicing, `(u, r)`: `ds² = −f du² − 2 du dr + r² dΩ²` -/

/-- The `(u, r)` block of the retarded metric. -/
noncomputable def gR (rh r : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![-f rh r, -1; -1, 0]

/-- Its inverse: `g^{uu} = 0`, `g^{ur} = −1`, `g^{rr} = f`. -/
noncomputable def gRinv (rh r : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![0, -1; -1, f rh r]

theorem ss_ret_mul_inv (rh r : ℝ) : gR rh r * gRinv rh r = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [gR, gRinv, Matrix.mul_apply, Fin.sum_univ_two]

theorem ss_ret_inv_mul (rh r : ℝ) : gRinv rh r * gR rh r = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [gR, gRinv, Matrix.mul_apply, Fin.sum_univ_two]

theorem ss_ret_inv_eq (rh r : ℝ) : (gR rh r)⁻¹ = gRinv rh r :=
  Matrix.inv_eq_right_inv (ss_ret_mul_inv rh r)

/-- The full 4×4 retarded metric in `(u, r, θ, φ)`. -/
noncomputable def gR4 (rh r θ : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![-f rh r, -1, 0, 0; -1, 0, 0, 0; 0, 0, r ^ 2, 0; 0, 0, 0, r ^ 2 * sin θ ^ 2]

noncomputable def gR4inv (rh r θ : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![0, -1, 0, 0; -1, f rh r, 0, 0; 0, 0, (r ^ 2)⁻¹, 0; 0, 0, 0, (r ^ 2 * sin θ ^ 2)⁻¹]

theorem ss_ret4_mul_inv {rh r θ : ℝ} (hr : r ≠ 0) (hs : sin θ ≠ 0) :
    gR4 rh r θ * gR4inv rh r θ = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [gR4, gR4inv, Matrix.mul_apply, Fin.sum_univ_four, hr] <;> field_simp

theorem ss_ret4_inv_mul {rh r θ : ℝ} (hr : r ≠ 0) (hs : sin θ ≠ 0) :
    gR4inv rh r θ * gR4 rh r θ = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [gR4, gR4inv, Matrix.mul_apply, Fin.sum_univ_four, hr] <;> field_simp

theorem ss_ret4_inv_eq {rh r θ : ℝ} (hr : r ≠ 0) (hs : sin θ ≠ 0) :
    (gR4 rh r θ)⁻¹ = gR4inv rh r θ :=
  Matrix.inv_eq_right_inv (ss_ret4_mul_inv hr hs)

/-- `dΘ = (a, aη)` for `Θ = a(u + ηr)`. -/
def dΘ (a η : ℝ) : Fin 2 → ℝ := ![a, a * η]

/-- `g^{ab}∂aΘ∂bΘ`. -/
noncomputable def Q (rh a η r : ℝ) : ℝ := dΘ a η ⬝ᵥ (gRinv rh r *ᵥ dΘ a η)

theorem ss_ret_norm (rh a η r : ℝ) :
    Q rh a η r = a ^ 2 * (f rh r * η ^ 2 - 2 * η) ∧
      Q rh a η r = a ^ 2 * η * (f rh r * η - 2) := by
  have h : Q rh a η r = a ^ 2 * (f rh r * η ^ 2 - 2 * η) := by
    simp [Q, dΘ, gRinv, Matrix.mulVec, dotProduct, Fin.sum_univ_two]; ring
  exact ⟨h, by rw [h]; ring⟩

/-- The 4×4 version agrees (angular components of `dΘ` vanish). -/
theorem ss_ret4_norm (rh a η r θ : ℝ) :
    ![a, a * η, 0, 0] ⬝ᵥ (gR4inv rh r θ *ᵥ ![a, a * η, 0, 0]) = Q rh a η r := by
  rw [(ss_ret_norm rh a η r).1]
  simp [gR4inv, Matrix.mulVec, dotProduct, Fin.sum_univ_four]; ring

/-- `g^{ab}∂aΘ∂bΘ → −2a²η` as `r → rh` (two-sided, so across the horizon). -/
theorem ss_ret_tendsto {rh : ℝ} (hrh : 0 < rh) (a η : ℝ) :
    Tendsto (Q rh a η) (𝓝 rh) (𝓝 (-2 * a ^ 2 * η)) := by
  have h : Tendsto (fun r => a ^ 2 * (f rh r * η ^ 2 - 2 * η)) (𝓝 rh)
      (𝓝 (a ^ 2 * (0 * η ^ 2 - 2 * η))) :=
    tendsto_const_nhds.mul (((f_tendsto hrh).mul tendsto_const_nhds).sub tendsto_const_nhds)
  have he : a ^ 2 * (0 * η ^ 2 - 2 * η) = -2 * a ^ 2 * η := by ring
  rw [he] at h
  exact h.congr (fun r => ((ss_ret_norm rh a η r).1).symm)

/-- The one-sided version from outside. -/
theorem ss_ret_tendsto_right {rh : ℝ} (hrh : 0 < rh) (a η : ℝ) :
    Tendsto (Q rh a η) (𝓝[>] rh) (𝓝 (-2 * a ^ 2 * η)) :=
  (ss_ret_tendsto hrh a η).mono_left nhdsWithin_le_nhds

/-- Θ has timelike gradient on a whole neighbourhood of `rh` (both sides of the horizon). -/
theorem ss_ret_neg_eventually {rh a η : ℝ} (hrh : 0 < rh) (ha : a ≠ 0) (hη : 0 < η) :
    ∀ᶠ r in 𝓝 rh, Q rh a η r < 0 := by
  have hneg : -2 * a ^ 2 * η < 0 := by
    have : 0 < a ^ 2 * η := mul_pos (pow_pos (abs_pos.2 ha) 2 |>.trans_eq (sq_abs a)) hη
    linarith
  exact (tendsto_order.1 (ss_ret_tendsto hrh a η)).2 0 hneg

/-- The same with an explicit radius `ε`. -/
theorem ss_ret_neg_nbhd {rh a η : ℝ} (hrh : 0 < rh) (ha : a ≠ 0) (hη : 0 < η) :
    ∃ ε > 0, ∀ r, |r - rh| < ε → Q rh a η r < 0 := by
  obtain ⟨ε, hε, h⟩ := Metric.eventually_nhds_iff.1 (ss_ret_neg_eventually hrh ha hη)
  exact ⟨ε, hε, fun r hr => h (by rwa [Real.dist_eq])⟩

/-- At the horizon itself the value is exactly `−2a²η`, finite and negative. -/
theorem ss_ret_at_horizon {rh : ℝ} (hrh : 0 < rh) (a η : ℝ) :
    Q rh a η rh = -2 * a ^ 2 * η := by
  rw [(ss_ret_norm rh a η rh).1, f_rh hrh]; ring

end ShadowProbe.SchwarzschildSlicing

open ShadowProbe.SchwarzschildSlicing

#print axioms ss_static_mul_inv
#print axioms ss_static_inv_mul
#print axioms ss_static_inv_eq
#print axioms ss_static_gtt
#print axioms ss_static_gtt_tendsto
#print axioms ss_static_gtt_matrix_tendsto
#print axioms ss_lapse_tendsto
#print axioms ss_lapse_sq
#print axioms ss_lapse_rpow
#print axioms ss_ret_mul_inv
#print axioms ss_ret_inv_mul
#print axioms ss_ret_inv_eq
#print axioms ss_ret4_mul_inv
#print axioms ss_ret4_inv_mul
#print axioms ss_ret4_inv_eq
#print axioms ss_ret_norm
#print axioms ss_ret4_norm
#print axioms ss_ret_tendsto
#print axioms ss_ret_tendsto_right
#print axioms ss_ret_neg_eventually
#print axioms ss_ret_neg_nbhd
#print axioms ss_ret_at_horizon

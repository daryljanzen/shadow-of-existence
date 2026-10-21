import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Algebra.BigOperators.Field

/-!
# Row 65, piece S: the hard-cutoff slope of the receipt's level sum

The receipt `P10_the_frequency_shift_is_the_curvature_term_at_every_level_so_the_log_coefficient_is_fifteen_quarters.py`
(`def slope`, ~line 436) computes, for `(off, c)` in `{(-3,-11), (-1,-9), (0,-8)}`,

  `t(M) = Σ_{k=3}^{M} [ 2(k²−4)·√(k²+off) − 2k³ − c·k ]`

and the discrete slopes `(t(M₂) − t(M₁)) / ln(M₂/M₁)` on the consecutive pairs of `(2000, 4000, 8000)`.
Writing `off = −a`, `c = −(8+a)` (all three receipt pairs have this form, `a = 3, 1, 0`), we prove:

* the exact split `summand = L/k + err a k`, `L = a(16−a)/4`, with
  `err = r²(16−a−2r)/(4k³)`, `r = k(k−√(k²−a))`, and `r² = k²(2r−a)`;
* (a) `slope M (2M) → a(16−a)/4` as `M → ∞` for every `0 ≤ a ≤ 3`: `39/4` (old), `15/4` (corrected),
  `0` (`dis`, where in fact every slope is exactly `0`);
* (b) rational brackets on the receipt's four non-trivial printed slopes (at `(2000,4000)` and `(4000,8000)`),
  each narrow enough to fix the receipt's printed six decimals.
-/

open Filter Topology Finset

namespace ShadowProbe.Row65Slope

/-! ## The receipt's objects -/

/-- the receipt's summand `2(k²−4)√(k²+off) − 2k³ − c·k` -/
noncomputable def summand (off c : ℝ) (k : ℕ) : ℝ :=
  2 * ((k : ℝ) ^ 2 - 4) * Real.sqrt ((k : ℝ) ^ 2 + off) - 2 * (k : ℝ) ^ 3 - c * k

/-- the receipt's hard-cutoff level sum `Σ_{kx ∈ range(3, M+1)}` -/
noncomputable def levelSum (off c : ℝ) (M : ℕ) : ℝ := ∑ k ∈ Icc 3 M, summand off c k

/-- the receipt's discrete slope `(t(M₂) − t(M₁)) / log(M₂/M₁)` -/
noncomputable def slope (off c : ℝ) (M₁ M₂ : ℕ) : ℝ :=
  (levelSum off c M₂ - levelSum off c M₁) / Real.log ((M₂ : ℝ) / M₁)

/-- the doubling difference is the sum over the new levels `M+1, …, 2M` -/
theorem levelSum_diff (off c : ℝ) {M : ℕ} (hM : 2 ≤ M) :
    levelSum off c (2 * M) - levelSum off c M = ∑ i ∈ range M, summand off c (M + 1 + i) := by
  have hI : ∀ N, Icc 3 N = Ioc 2 N := fun N => by ext x; simp only [Finset.mem_Icc, Finset.mem_Ioc]; omega
  unfold levelSum
  rw [hI, hI, ← Finset.sum_Ioc_consecutive _ hM (by omega : M ≤ 2 * M), add_sub_cancel_left]
  have h1 : Ioc M (2 * M) = Ico (M + 1) (2 * M + 1) := by
    ext x; simp only [Finset.mem_Ico, Finset.mem_Ioc]; omega
  rw [h1, Finset.sum_Ico_eq_sum_range]
  have h2 : 2 * M + 1 - (M + 1) = M := by omega
  rw [h2]

theorem log_ratio_two {M : ℕ} (hM : 1 ≤ M) : Real.log (((2 * M : ℕ) : ℝ) / M) = Real.log 2 := by
  have : (M : ℝ) ≠ 0 := by exact_mod_cast (by omega : M ≠ 0)
  push_cast; rw [mul_div_assoc, div_self this, mul_one]

/-! ## The exact per-level split -/

/-- the tail coordinate `r = m(m − √(m²−a))` -/
noncomputable def rr (a m : ℝ) : ℝ := m * (m - Real.sqrt (m ^ 2 - a))

/-- the exact remainder after the `L/m` term -/
noncomputable def err (a m : ℝ) : ℝ := rr a m ^ 2 * (16 - a - 2 * rr a m) / (4 * m ^ 3)

/-- ⛭ **the exact split**: `summand(−a, −(8+a), k) = a(16−a)/4 · (1/k) + err a k`. -/
theorem summand_split (a : ℝ) (k : ℕ) (hk : 0 < k) (ha : a ≤ (k : ℝ) ^ 2) :
    summand (-a) (-(8 + a)) k = a * (16 - a) / 4 * (1 / (k : ℝ)) + err a k := by
  have hm : (0 : ℝ) < k := by exact_mod_cast hk
  have hs2 : Real.sqrt ((k : ℝ) ^ 2 - a) ^ 2 = (k : ℝ) ^ 2 - a := Real.sq_sqrt (by linarith)
  have key : 4 * (k : ℝ) ^ 3 * (2 * ((k : ℝ) ^ 2 - 4) * Real.sqrt ((k : ℝ) ^ 2 - a) - 2 * (k : ℝ) ^ 3
      + (8 + a) * k) - a * (16 - a) * (k : ℝ) ^ 2
      = ((k : ℝ) * ((k : ℝ) - Real.sqrt ((k : ℝ) ^ 2 - a))) ^ 2
        * (16 - a - 2 * ((k : ℝ) * ((k : ℝ) - Real.sqrt ((k : ℝ) ^ 2 - a)))) := by
    linear_combination (-(k : ℝ) ^ 2 * (16 - a - 6 * (k : ℝ) ^ 2 + 2 * k * Real.sqrt ((k : ℝ) ^ 2 - a))) * hs2
  unfold summand err rr
  rw [show (k : ℝ) ^ 2 + -a = (k : ℝ) ^ 2 - a by ring]
  rw [← sub_eq_zero]
  have hk3 : (4 : ℝ) * (k : ℝ) ^ 3 ≠ 0 := by positivity
  have : 2 * ((k : ℝ) ^ 2 - 4) * Real.sqrt ((k : ℝ) ^ 2 - a) - 2 * (k : ℝ) ^ 3 - -(8 + a) * k -
      (a * (16 - a) / 4 * (1 / (k : ℝ)) +
        ((k : ℝ) * ((k : ℝ) - Real.sqrt ((k : ℝ) ^ 2 - a))) ^ 2
          * (16 - a - 2 * ((k : ℝ) * ((k : ℝ) - Real.sqrt ((k : ℝ) ^ 2 - a)))) / (4 * (k : ℝ) ^ 3))
      = ((4 * (k : ℝ) ^ 3 * (2 * ((k : ℝ) ^ 2 - 4) * Real.sqrt ((k : ℝ) ^ 2 - a) - 2 * (k : ℝ) ^ 3
      + (8 + a) * k) - a * (16 - a) * (k : ℝ) ^ 2)
        - ((k : ℝ) * ((k : ℝ) - Real.sqrt ((k : ℝ) ^ 2 - a))) ^ 2
        * (16 - a - 2 * ((k : ℝ) * ((k : ℝ) - Real.sqrt ((k : ℝ) ^ 2 - a))))) / (4 * (k : ℝ) ^ 3) := by
    field_simp; ring
  rw [this, key, sub_self, zero_div]
#print axioms ShadowProbe.Row65Slope.summand_split

/-- the tail coordinate's facts: `r² = m²(2r − a)`, `a/2 ≤ r ≤ a`. -/
theorem rr_facts (a m : ℝ) (hm : 0 < m) (ha0 : 0 ≤ a) (ha : a ≤ m ^ 2) :
    rr a m ^ 2 = m ^ 2 * (2 * rr a m - a) ∧ a / 2 ≤ rr a m ∧ rr a m ≤ a := by
  have hs0 := Real.sqrt_nonneg (m ^ 2 - a)
  have hs2 : Real.sqrt (m ^ 2 - a) ^ 2 = m ^ 2 - a := Real.sq_sqrt (by linarith)
  have h1 : rr a m ^ 2 = m ^ 2 * (2 * rr a m - a) := by unfold rr; linear_combination m ^ 2 * hs2
  have hsm : Real.sqrt (m ^ 2 - a) ≤ m := by nlinarith
  have hr0 : 0 ≤ rr a m := by unfold rr; nlinarith
  have hrm : rr a m * (m + Real.sqrt (m ^ 2 - a)) = m * a := by
    unfold rr; linear_combination (-m) * hs2
  refine ⟨h1, ?_, ?_⟩
  · have h2 : 0 ≤ m ^ 2 * (2 * rr a m - a) := by rw [← h1]; positivity
    have h3 : 0 ≤ 2 * rr a m - a := by
      by_contra hc; push Not at hc
      nlinarith [mul_neg_of_pos_of_neg (by positivity : (0 : ℝ) < m ^ 2) hc]
    linarith
  · nlinarith [mul_nonneg hr0 hs0]

/-- crude remainder bound: `0 ≤ err ≤ 36/m³`. -/
theorem err_crude (a m : ℝ) (hm : 0 < m) (ha0 : 0 ≤ a) (ha3 : a ≤ 3) (ha : a ≤ m ^ 2) :
    0 ≤ err a m ∧ err a m ≤ 36 / m ^ 3 := by
  obtain ⟨-, h2, h3⟩ := rr_facts a m hm ha0 ha
  have hr0 : 0 ≤ rr a m := by linarith
  have hN0 : 0 ≤ rr a m ^ 2 * (16 - a - 2 * rr a m) := mul_nonneg (sq_nonneg _) (by linarith)
  have hN1 : rr a m ^ 2 * (16 - a - 2 * rr a m) ≤ 144 := by
    have : rr a m ^ 2 ≤ 9 := by nlinarith
    nlinarith
  unfold err
  refine ⟨by positivity, ?_⟩
  rw [div_le_div_iff₀ (by positivity) (by positivity)]
  nlinarith [pow_pos hm 3]

/-- fine remainder bound for `m ≥ 2000`: `K/m³ ≤ err ≤ (K + 1/1000)/m³`, `K = a²(8−a)/8`. -/
theorem err_fine (a m : ℝ) (ha0 : 0 ≤ a) (ha3 : a ≤ 3) (hm : 2000 ≤ m) :
    a ^ 2 * (8 - a) / 8 / m ^ 3 ≤ err a m ∧ err a m ≤ (a ^ 2 * (8 - a) / 8 + 1 / 1000) / m ^ 3 := by
  have hm0 : 0 < m := by linarith
  have ha : a ≤ m ^ 2 := by nlinarith
  obtain ⟨h1, h2, h3⟩ := rr_facts a m hm0 ha0 ha
  set r := rr a m
  set t := r - a / 2 with ht
  have ht0 : 0 ≤ t := by linarith
  have hm2 : (4000000 : ℝ) ≤ m ^ 2 := by nlinarith
  have hr9 : r ^ 2 ≤ 9 := by nlinarith
  have ht1 : t ≤ 9 / 8000000 := by
    have : m ^ 2 * (2 * t) ≤ 9 := by rw [ht]; nlinarith
    nlinarith
  have hid : r ^ 2 * (16 - a - 2 * r) / 4 - a ^ 2 * (8 - a) / 8
      = t * (32 * a - 5 * a ^ 2 + 32 * t - 8 * a * t - 4 * t ^ 2) / 8 := by rw [ht]; ring
  have hP0 : 0 ≤ 32 * a - 5 * a ^ 2 + 32 * t - 8 * a * t - 4 * t ^ 2 := by
    nlinarith [mul_nonneg ha0 (by linarith : (0 : ℝ) ≤ 32 - 5 * a),
      mul_nonneg ht0 (by linarith : (0 : ℝ) ≤ 8 - 2 * a - t)]
  have hP1 : 32 * a - 5 * a ^ 2 + 32 * t - 8 * a * t - 4 * t ^ 2 ≤ 97 := by
    nlinarith [mul_nonneg ha0 ht0]
  have hlo : a ^ 2 * (8 - a) / 8 ≤ r ^ 2 * (16 - a - 2 * r) / 4 := by
    have := mul_nonneg ht0 hP0; linarith
  have hhi : r ^ 2 * (16 - a - 2 * r) / 4 ≤ a ^ 2 * (8 - a) / 8 + 1 / 1000 := by
    have := mul_le_mul_of_nonneg_left hP1 ht0; nlinarith
  have hE : err a m = r ^ 2 * (16 - a - 2 * r) / 4 / m ^ 3 := by
    simp only [r]; unfold err; ring
  have hm3 : 0 < m ^ 3 := by positivity
  rw [hE]
  exact ⟨(div_le_div_iff_of_pos_right hm3).2 hlo, (div_le_div_iff_of_pos_right hm3).2 hhi⟩

/-! ## (a) The limit -/

/-- the doubling difference, split: `L · Σ 1/m + Σ err`. -/
theorem diff_split (a : ℝ) (_ha0 : 0 ≤ a) (ha3 : a ≤ 3) {M : ℕ} (hM : 2 ≤ M) :
    levelSum (-a) (-(8 + a)) (2 * M) - levelSum (-a) (-(8 + a)) M
      = a * (16 - a) / 4 * ∑ i ∈ range M, (1 : ℝ) / ((M + 1 + i : ℕ) : ℝ)
        + ∑ i ∈ range M, err a ((M + 1 + i : ℕ) : ℝ) := by
  rw [levelSum_diff _ _ hM, mul_sum, ← sum_add_distrib]
  refine sum_congr rfl (fun i _ => summand_split a _ (by omega) ?_)
  have : (3 : ℝ) ≤ ((M + 1 + i : ℕ) : ℝ) := by exact_mod_cast (by omega : 3 ≤ M + 1 + i)
  nlinarith

theorem harm_diff (M : ℕ) :
    ∑ i ∈ range M, (1 : ℝ) / ((M + 1 + i : ℕ) : ℝ) = (harmonic (2 * M) : ℝ) - harmonic M := by
  rw [two_mul]
  simp only [harmonic, Finset.sum_range_add]
  push_cast
  rw [add_sub_cancel_left]
  refine sum_congr rfl (fun i _ => ?_)
  rw [one_div]; ring_nf

theorem harm_diff_tendsto :
    Tendsto (fun M : ℕ => (harmonic (2 * M) : ℝ) - harmonic M) atTop (𝓝 (Real.log 2)) := by
  have h0 := Real.tendsto_harmonic_sub_log
  have h2 : Tendsto (fun M : ℕ => 2 * M) atTop atTop :=
    tendsto_atTop_mono (fun n => by simp only [id]; omega) tendsto_id
  have h1 := ((h0.comp h2).sub h0).add_const (Real.log 2)
  rw [sub_self, zero_add] at h1
  refine h1.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with M hM
  have hM' : (M : ℝ) ≠ 0 := by exact_mod_cast (by omega : M ≠ 0)
  have : Real.log ((2 * M : ℕ) : ℝ) = Real.log 2 + Real.log M := by
    push_cast; rw [Real.log_mul (by norm_num) hM']
  simp only [Function.comp, this]; ring

theorem err_sum_tendsto (a : ℝ) (ha0 : 0 ≤ a) (ha3 : a ≤ 3) :
    Tendsto (fun M : ℕ => ∑ i ∈ range M, err a ((M + 1 + i : ℕ) : ℝ)) atTop (𝓝 0) := by
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds
    (tendsto_const_div_atTop_nhds_zero_nat (36 : ℝ)) ?_ ?_
  · filter_upwards [eventually_ge_atTop 2] with M hM
    refine sum_nonneg (fun i _ => ?_)
    have hm : (3 : ℝ) ≤ ((M + 1 + i : ℕ) : ℝ) := by exact_mod_cast (by omega : 3 ≤ M + 1 + i)
    exact (err_crude a ((M + 1 + i : ℕ) : ℝ) (by linarith) ha0 ha3 (by nlinarith)).1
  · filter_upwards [eventually_ge_atTop 1] with M hM
    have hM0 : (0 : ℝ) < M := by exact_mod_cast hM
    have hM1 : (1 : ℝ) ≤ M := by exact_mod_cast hM
    calc ∑ i ∈ range M, err a ((M + 1 + i : ℕ) : ℝ) ≤ ∑ _i ∈ range M, 36 / (M : ℝ) ^ 2 := by
          refine sum_le_sum (fun i _ => ?_)
          have hm : (M : ℝ) + 1 ≤ ((M + 1 + i : ℕ) : ℝ) := by push_cast; linarith [i.cast_nonneg (α := ℝ)]
          have hm0 : (0 : ℝ) < ((M + 1 + i : ℕ) : ℝ) := by linarith
          refine (err_crude a _ hm0 ha0 ha3 (by nlinarith)).2.trans ?_
          refine div_le_div_of_nonneg_left (by norm_num) (by positivity) ?_
          have h1 : (M : ℝ) ^ 2 ≤ ((M + 1 + i : ℕ) : ℝ) ^ 2 := by gcongr; linarith
          have h2 : ((M + 1 + i : ℕ) : ℝ) ^ 2 ≤ ((M + 1 + i : ℕ) : ℝ) ^ 3 := by
            have : (1 : ℝ) ≤ ((M + 1 + i : ℕ) : ℝ) := by linarith
            nlinarith [sq_nonneg ((M + 1 + i : ℕ) : ℝ)]
          linarith
      _ = 36 / (M : ℝ) := by
          rw [sum_const, card_range, nsmul_eq_mul]; field_simp

/-- ⛭ **(a) THE LIMIT, every `0 ≤ a ≤ 3`.** The receipt's discrete slope between `M` and `2M` tends to
`a(16−a)/4`. -/
theorem slope_tendsto (a : ℝ) (ha0 : 0 ≤ a) (ha3 : a ≤ 3) :
    Tendsto (fun M : ℕ => slope (-a) (-(8 + a)) M (2 * M)) atTop (𝓝 (a * (16 - a) / 4)) := by
  have hmain := ((harm_diff_tendsto.const_mul (a * (16 - a) / 4)).add
    (err_sum_tendsto a ha0 ha3)).div_const (Real.log 2)
  have hl2 : Real.log 2 ≠ 0 := (Real.log_pos (by norm_num)).ne'
  have hl : (a * (16 - a) / 4 * Real.log 2 + 0) / Real.log 2 = a * (16 - a) / 4 := by
    rw [add_zero, mul_div_assoc, div_self hl2, mul_one]
  rw [hl] at hmain
  refine hmain.congr' ?_
  filter_upwards [eventually_ge_atTop 2] with M hM
  rw [slope, diff_split a ha0 ha3 hM, harm_diff, log_ratio_two (by omega)]
#print axioms ShadowProbe.Row65Slope.slope_tendsto

/-- ⛭ **(a), corrected frequency `m² − 1`:** the slope tends to `15/4`. -/
theorem slope_tendsto_new :
    Tendsto (fun M : ℕ => slope (-1) (-9) M (2 * M)) atTop (𝓝 (15 / 4)) := by
  have h := slope_tendsto 1 (by norm_num) (by norm_num)
  norm_num at h; exact h
#print axioms ShadowProbe.Row65Slope.slope_tendsto_new

/-- ⛭ **(a), old frequency `m² − 3`:** the slope tends to `39/4`. -/
theorem slope_tendsto_old :
    Tendsto (fun M : ℕ => slope (-3) (-11) M (2 * M)) atTop (𝓝 (39 / 4)) := by
  have h := slope_tendsto 3 (by norm_num) (by norm_num)
  norm_num at h; exact h
#print axioms ShadowProbe.Row65Slope.slope_tendsto_old

/-- ⛭ **`dis` (offset `0`): every summand vanishes**, so the level sum is identically `0` and every
discrete slope is exactly `0` — not a small difference of large numbers. -/
theorem summand_dis (k : ℕ) : summand 0 (-8) k = 0 := by
  unfold summand
  rw [add_zero, Real.sqrt_sq (Nat.cast_nonneg k)]; ring

theorem slope_dis (M₁ M₂ : ℕ) : slope 0 (-8) M₁ M₂ = 0 := by
  simp [slope, levelSum, summand_dis]

theorem slope_tendsto_dis :
    Tendsto (fun M : ℕ => slope 0 (-8) M (2 * M)) atTop (𝓝 0) := by
  simp only [slope_dis]; exact tendsto_const_nhds
#print axioms ShadowProbe.Row65Slope.slope_tendsto_dis

/-! ## (b) The printed values -/

/-- one telescoping step of `log`: `1/m ≤ log(2m+1) − log(2m−1) ≤ 1/m + 1/(11 m³)`. -/
theorem log_step (m : ℝ) (hm : 2 ≤ m) :
    1 / m ≤ Real.log (2 * m + 1) - Real.log (2 * m - 1) ∧
      Real.log (2 * m + 1) - Real.log (2 * m - 1) ≤ 1 / m + 1 / (11 * m ^ 3) := by
  have ha : 0 < m - 1 / 2 := by linarith
  have hS := Real.hasSum_log_one_add_inv ha
  have e1 : 2 * (m - 1 / 2) + 1 = 2 * m := by ring
  have e2 : Real.log (1 + (m - 1 / 2)⁻¹) = Real.log (2 * m + 1) - Real.log (2 * m - 1) := by
    rw [← Real.log_div (by linarith) (by linarith)]
    congr 1
    have : 2 * m - 1 ≠ 0 := by linarith
    rw [show m - 1 / 2 = (2 * m - 1) / 2 by ring, inv_div]
    field_simp; ring
  rw [e1, e2] at hS
  have hm0 : 0 < m := by linarith
  have hx0 : 0 < 1 / (2 * m) := by positivity
  have hx1 : (1 / (2 * m)) ^ 2 < 1 := by
    rw [div_pow, one_pow, div_lt_one (by positivity)]; nlinarith
  have f0 : (2 : ℝ) * (1 / (2 * ((0 : ℕ) : ℝ) + 1)) * (1 / (2 * m)) ^ (2 * 0 + 1) = 1 / m := by
    push_cast; field_simp; ring
  constructor
  · have := le_hasSum hS 0 (fun j _ => by positivity)
    rw [f0] at this; exact this
  · rw [← hasSum_nat_add_iff' 1, Finset.sum_range_one, f0] at hS
    have hg := (hasSum_geometric_of_lt_one (sq_nonneg (1 / (2 * m))) hx1).mul_left
      (2 / 3 * (1 / (2 * m)) ^ 3)
    have hle := hasSum_le (fun n => ?_) hS hg
    · have hc : 2 / 3 * (1 / (2 * m)) ^ 3 * (1 - (1 / (2 * m)) ^ 2)⁻¹ = 1 / (3 * m * (4 * m ^ 2 - 1)) := by
        have : 4 * m ^ 2 - 1 ≠ 0 := by nlinarith
        have : 1 - (1 / (2 * m)) ^ 2 = (4 * m ^ 2 - 1) / (4 * m ^ 2) := by field_simp; ring
        rw [this]; field_simp; ring
      rw [hc] at hle
      have h11 : 1 / (3 * m * (4 * m ^ 2 - 1)) ≤ 1 / (11 * m ^ 3) := by
        apply one_div_le_one_div_of_le (by positivity)
        nlinarith [pow_pos hm0 3]
      linarith
    · have hx3 : (1 / (2 * m)) ^ (2 * (n + 1) + 1) = (1 / (2 * m)) ^ 3 * ((1 / (2 * m)) ^ 2) ^ n := by
        rw [← pow_mul, ← pow_add]; congr 1; ring
      have hq : (1 : ℝ) / (2 * ((n + 1 : ℕ) : ℝ) + 1) ≤ 1 / 3 := by
        apply one_div_le_one_div_of_le (by norm_num); push_cast; linarith [n.cast_nonneg (α := ℝ)]
      show (2 : ℝ) * (1 / (2 * ((n + 1 : ℕ) : ℝ) + 1)) * (1 / (2 * m)) ^ (2 * (n + 1) + 1)
        ≤ 2 / 3 * (1 / (2 * m)) ^ 3 * ((1 / (2 * m)) ^ 2) ^ n
      rw [hx3]
      have hp : 0 ≤ (1 / (2 * m)) ^ 3 * ((1 / (2 * m)) ^ 2) ^ n := by positivity
      nlinarith

/-- cube telescoping: `1/(2m²) − 1/(2(m+1)²) ≤ 1/m³ ≤ 2/(2m−1)² − 2/(2m+1)²`. -/
theorem cube_step (m : ℝ) (hm : 1 ≤ m) :
    1 / (2 * m ^ 2) - 1 / (2 * (m + 1) ^ 2) ≤ 1 / m ^ 3 ∧
      1 / m ^ 3 ≤ 2 / (2 * m - 1) ^ 2 - 2 / (2 * m + 1) ^ 2 := by
  have hm0 : 0 < m := by linarith
  have h1 : 2 * m - 1 ≠ 0 := by linarith
  have h2 : 2 * m + 1 ≠ 0 := by linarith
  constructor
  · have : 1 / m ^ 3 - (1 / (2 * m ^ 2) - 1 / (2 * (m + 1) ^ 2)) = (3 * m + 2) / (2 * m ^ 3 * (m + 1) ^ 2) := by
      field_simp; ring
    have : 0 ≤ (3 * m + 2) / (2 * m ^ 3 * (m + 1) ^ 2) := by positivity
    linarith
  · have : 2 / (2 * m - 1) ^ 2 - 2 / (2 * m + 1) ^ 2 - 1 / m ^ 3
        = (8 * m ^ 2 - 1) / (m ^ 3 * ((2 * m - 1) * (2 * m + 1)) ^ 2) := by
      field_simp; ring
    have : 0 ≤ (8 * m ^ 2 - 1) / (m ^ 3 * ((2 * m - 1) * (2 * m + 1)) ^ 2) :=
      div_nonneg (by nlinarith) (by positivity)
    linarith

/-- the bracket on the doubling difference, `M ≥ 2000`. -/
theorem diff_bounds (a : ℝ) (ha0 : 0 ≤ a) (ha3 : a ≤ 3) (M : ℕ) (hM : 2000 ≤ M) :
    a * (16 - a) / 4 * (Real.log (4 * M + 1) - Real.log (2 * M + 1)
        - (2 / (2 * (M : ℝ) + 1) ^ 2 - 2 / (4 * (M : ℝ) + 1) ^ 2) / 11)
      + a ^ 2 * (8 - a) / 8 * (1 / (2 * ((M : ℝ) + 1) ^ 2) - 1 / (2 * (2 * (M : ℝ) + 1) ^ 2))
      ≤ levelSum (-a) (-(8 + a)) (2 * M) - levelSum (-a) (-(8 + a)) M ∧
    levelSum (-a) (-(8 + a)) (2 * M) - levelSum (-a) (-(8 + a)) M
      ≤ a * (16 - a) / 4 * (Real.log (4 * M + 1) - Real.log (2 * M + 1))
      + (a ^ 2 * (8 - a) / 8 + 1 / 1000) * (2 / (2 * (M : ℝ) + 1) ^ 2 - 2 / (4 * (M : ℝ) + 1) ^ 2) := by
  rw [diff_split a ha0 ha3 (by omega)]
  -- the levels, as reals
  have hmi : ∀ i : ℕ, ((M + 1 + i : ℕ) : ℝ) = (M : ℝ) + 1 + i := fun i => by push_cast; ring
  have hmge : ∀ i : ℕ, (2001 : ℝ) ≤ ((M + 1 + i : ℕ) : ℝ) := fun i => by
    exact_mod_cast (by omega : 2001 ≤ M + 1 + i)
  -- log telescoping
  have htel : ∑ i ∈ range M, (Real.log (2 * ((M + 1 + i : ℕ) : ℝ) + 1) - Real.log (2 * ((M + 1 + i : ℕ) : ℝ) - 1))
      = Real.log (4 * M + 1) - Real.log (2 * M + 1) := by
    have := Finset.sum_range_sub (fun i : ℕ => Real.log (2 * ((M : ℝ) + i) + 1)) M
    convert this using 1
    · refine sum_congr rfl (fun i _ => ?_)
      rw [hmi]; push_cast; ring_nf
    · push_cast; ring_nf
  -- cube telescoping
  have hQlo : ∑ i ∈ range M, (1 / (2 * ((M + 1 + i : ℕ) : ℝ) ^ 2) - 1 / (2 * (((M + 1 + i : ℕ) : ℝ) + 1) ^ 2))
      = 1 / (2 * ((M : ℝ) + 1) ^ 2) - 1 / (2 * (2 * (M : ℝ) + 1) ^ 2) := by
    have := Finset.sum_range_sub' (fun i : ℕ => 1 / (2 * ((M : ℝ) + 1 + i) ^ 2)) M
    convert this using 1
    · refine sum_congr rfl (fun i _ => ?_)
      rw [hmi]; push_cast; ring_nf
    · push_cast; ring_nf
  have hQhi : ∑ i ∈ range M, (2 / (2 * ((M + 1 + i : ℕ) : ℝ) - 1) ^ 2 - 2 / (2 * ((M + 1 + i : ℕ) : ℝ) + 1) ^ 2)
      = 2 / (2 * (M : ℝ) + 1) ^ 2 - 2 / (4 * (M : ℝ) + 1) ^ 2 := by
    have := Finset.sum_range_sub' (fun i : ℕ => 2 / (2 * ((M : ℝ) + i) + 1) ^ 2) M
    convert this using 1
    · refine sum_congr rfl (fun i _ => ?_)
      rw [hmi]; push_cast; ring_nf
    · push_cast; ring_nf
  -- per-term bounds summed
  have S_lo : Real.log (4 * M + 1) - Real.log (2 * M + 1)
      - (2 / (2 * (M : ℝ) + 1) ^ 2 - 2 / (4 * (M : ℝ) + 1) ^ 2) / 11
      ≤ ∑ i ∈ range M, (1 : ℝ) / ((M + 1 + i : ℕ) : ℝ) := by
    rw [← htel, ← hQhi, sum_div, ← sum_sub_distrib]
    refine sum_le_sum (fun i _ => ?_)
    have h1 := (log_step ((M + 1 + i : ℕ) : ℝ) (by linarith [hmge i])).2
    have h2 := (cube_step ((M + 1 + i : ℕ) : ℝ) (by linarith [hmge i])).2
    have h3 : 1 / (11 * ((M + 1 + i : ℕ) : ℝ) ^ 3) = (1 / ((M + 1 + i : ℕ) : ℝ) ^ 3) / 11 := by
      field_simp
    linarith
  have S_hi : ∑ i ∈ range M, (1 : ℝ) / ((M + 1 + i : ℕ) : ℝ)
      ≤ Real.log (4 * M + 1) - Real.log (2 * M + 1) := by
    rw [← htel]
    exact sum_le_sum (fun i _ => (log_step ((M + 1 + i : ℕ) : ℝ) (by linarith [hmge i])).1)
  have hK : 0 ≤ a ^ 2 * (8 - a) / 8 := by
    have : 0 ≤ 8 - a := by linarith
    positivity
  have E_lo : a ^ 2 * (8 - a) / 8 * (1 / (2 * ((M : ℝ) + 1) ^ 2) - 1 / (2 * (2 * (M : ℝ) + 1) ^ 2))
      ≤ ∑ i ∈ range M, err a ((M + 1 + i : ℕ) : ℝ) := by
    rw [← hQlo, mul_sum]
    refine sum_le_sum (fun i _ => ?_)
    have h1 := (err_fine a ((M + 1 + i : ℕ) : ℝ) ha0 ha3 (by linarith [hmge i])).1
    have h2 := (cube_step ((M + 1 + i : ℕ) : ℝ) (by linarith [hmge i])).1
    have h3 := mul_le_mul_of_nonneg_left h2 hK
    rw [div_eq_mul_one_div] at h1
    linarith
  have E_hi : ∑ i ∈ range M, err a ((M + 1 + i : ℕ) : ℝ)
      ≤ (a ^ 2 * (8 - a) / 8 + 1 / 1000) * (2 / (2 * (M : ℝ) + 1) ^ 2 - 2 / (4 * (M : ℝ) + 1) ^ 2) := by
    rw [← hQhi, mul_sum]
    refine sum_le_sum (fun i _ => ?_)
    have h1 := (err_fine a ((M + 1 + i : ℕ) : ℝ) ha0 ha3 (by linarith [hmge i])).2
    have h2 := (cube_step ((M + 1 + i : ℕ) : ℝ) (by linarith [hmge i])).2
    have h3 := mul_le_mul_of_nonneg_left h2 (by linarith : (0 : ℝ) ≤ a ^ 2 * (8 - a) / 8 + 1 / 1000)
    rw [div_eq_mul_one_div] at h1
    linarith
  have hL : 0 ≤ a * (16 - a) / 4 := by
    have : 0 ≤ 16 - a := by linarith
    positivity
  constructor
  · have := mul_le_mul_of_nonneg_left S_lo hL; linarith
  · have := mul_le_mul_of_nonneg_left S_hi hL; linarith

/-- `log(4M+1) − log(2M+1) = log 2 − ℓ`, with `1/(4M+2) ≤ ℓ ≤ 1/(4M+1)`. -/
theorem Lambda_bounds (M : ℕ) :
    Real.log 2 - 1 / (4 * (M : ℝ) + 1) ≤ Real.log (4 * M + 1) - Real.log (2 * M + 1) ∧
      Real.log (4 * M + 1) - Real.log (2 * M + 1) ≤ Real.log 2 - 1 / (4 * (M : ℝ) + 2) := by
  have hM0 : (0 : ℝ) ≤ M := M.cast_nonneg
  set ℓ := Real.log ((4 * (M : ℝ) + 2) / (4 * M + 1))
  have hΛ : Real.log (4 * M + 1) - Real.log (2 * M + 1) = Real.log 2 - ℓ := by
    simp only [ℓ]
    rw [Real.log_div (by positivity) (by positivity),
      show (4 : ℝ) * M + 2 = 2 * (2 * M + 1) by ring, Real.log_mul (by norm_num) (by positivity)]
    ring
  have hpos : 0 < (4 * (M : ℝ) + 2) / (4 * M + 1) := by positivity
  have hu := Real.log_le_sub_one_of_pos hpos
  have hl := Real.one_sub_inv_le_log_of_pos hpos
  have e1 : (4 * (M : ℝ) + 2) / (4 * M + 1) - 1 = 1 / (4 * (M : ℝ) + 1) := by field_simp; ring
  have e2 : 1 - ((4 * (M : ℝ) + 2) / (4 * M + 1))⁻¹ = 1 / (4 * (M : ℝ) + 2) := by
    rw [inv_div]; field_simp; ring
  rw [e1] at hu; rw [e2] at hl
  rw [hΛ]; constructor <;> linarith

/-- the generic bracket of the receipt's slope at `(M, 2M)`, `M ≥ 2000`, in terms of `log 2` only. -/
theorem slope_bounds (a : ℝ) (ha0 : 0 ≤ a) (ha3 : a ≤ 3) (M : ℕ) (hM : 2000 ≤ M) :
    (a * (16 - a) / 4 * (Real.log 2 - 1 / (4 * (M : ℝ) + 1)
        - (2 / (2 * (M : ℝ) + 1) ^ 2 - 2 / (4 * (M : ℝ) + 1) ^ 2) / 11)
      + a ^ 2 * (8 - a) / 8 * (1 / (2 * ((M : ℝ) + 1) ^ 2) - 1 / (2 * (2 * (M : ℝ) + 1) ^ 2)))
        / Real.log 2 ≤ slope (-a) (-(8 + a)) M (2 * M) ∧
    slope (-a) (-(8 + a)) M (2 * M) ≤
      (a * (16 - a) / 4 * (Real.log 2 - 1 / (4 * (M : ℝ) + 2))
      + (a ^ 2 * (8 - a) / 8 + 1 / 1000) * (2 / (2 * (M : ℝ) + 1) ^ 2 - 2 / (4 * (M : ℝ) + 1) ^ 2))
        / Real.log 2 := by
  obtain ⟨d1, d2⟩ := diff_bounds a ha0 ha3 M hM
  obtain ⟨l1, l2⟩ := Lambda_bounds M
  have hL : 0 ≤ a * (16 - a) / 4 := by
    have : 0 ≤ 16 - a := by linarith
    positivity
  have hl2 : 0 < Real.log 2 := Real.log_pos (by norm_num)
  rw [slope, log_ratio_two (by omega)]
  constructor
  · apply div_le_div_of_nonneg_right _ hl2.le
    have := mul_le_mul_of_nonneg_left l1 hL; nlinarith
  · apply div_le_div_of_nonneg_right _ hl2.le
    have := mul_le_mul_of_nonneg_left l2 hL; nlinarith

/-- ⛭ **(b) corrected frequency, `(2000, 4000)`:** `3.7493238 < s < 3.7493241` (receipt arithmetic:
`3.749323939…`). -/
theorem bracket_new_2000 :
    3.7493238 < slope (-1) (-9) 2000 4000 ∧ slope (-1) (-9) 2000 4000 < 3.7493241 := by
  have e : slope (-1) (-9) 2000 4000 = slope (-(1 : ℝ)) (-(8 + 1)) 2000 (2 * 2000) := by norm_num
  obtain ⟨h1, h2⟩ := slope_bounds 1 (by norm_num) (by norm_num) 2000 (le_refl _)
  have hl2a := Real.log_two_gt_d9; have hl2b := Real.log_two_lt_d9
  have hl2 : 0 < Real.log 2 := by linarith
  rw [e]; norm_num at h1 h2 ⊢
  constructor
  · refine lt_of_lt_of_le ?_ h1; rw [lt_div_iff₀ hl2]; nlinarith
  · refine lt_of_le_of_lt h2 ?_; rw [div_lt_iff₀ hl2]; nlinarith
#print axioms ShadowProbe.Row65Slope.bracket_new_2000

/-- ⛭ **(b) corrected frequency, `(4000, 8000)` — the receipt's printed `s_new[-1]`:**
`3.7496619 < s < 3.7496620`, so it prints `3.749662` (receipt: `3.749661919…`). -/
theorem bracket_new_4000 :
    3.7496619 < slope (-1) (-9) 4000 8000 ∧ slope (-1) (-9) 4000 8000 < 3.7496620 := by
  have e : slope (-1) (-9) 4000 8000 = slope (-(1 : ℝ)) (-(8 + 1)) 4000 (2 * 4000) := by norm_num
  obtain ⟨h1, h2⟩ := slope_bounds 1 (by norm_num) (by norm_num) 4000 (by norm_num)
  have hl2a := Real.log_two_gt_d9; have hl2b := Real.log_two_lt_d9
  have hl2 : 0 < Real.log 2 := by linarith
  rw [e]; norm_num at h1 h2 ⊢
  constructor
  · refine lt_of_lt_of_le ?_ h1; rw [lt_div_iff₀ hl2]; nlinarith
  · refine lt_of_le_of_lt h2 ?_; rw [div_lt_iff₀ hl2]; nlinarith
#print axioms ShadowProbe.Row65Slope.bracket_new_4000

/-- ⛭ **(b) old frequency, `(2000, 4000)`:** `9.7482425 < s < 9.7482430` (receipt: `9.748242695…`). -/
theorem bracket_old_2000 :
    9.7482425 < slope (-3) (-11) 2000 4000 ∧ slope (-3) (-11) 2000 4000 < 9.7482430 := by
  have e : slope (-3) (-11) 2000 4000 = slope (-(3 : ℝ)) (-(8 + 3)) 2000 (2 * 2000) := by norm_num
  obtain ⟨h1, h2⟩ := slope_bounds 3 (by norm_num) (by norm_num) 2000 (le_refl _)
  have hl2a := Real.log_two_gt_d9; have hl2b := Real.log_two_lt_d9
  have hl2 : 0 < Real.log 2 := by linarith
  rw [e]; norm_num at h1 h2 ⊢
  constructor
  · refine lt_of_lt_of_le ?_ h1; rw [lt_div_iff₀ hl2]; nlinarith
  · refine lt_of_le_of_lt h2 ?_; rw [div_lt_iff₀ hl2]; nlinarith
#print axioms ShadowProbe.Row65Slope.bracket_old_2000

/-- ⛭ **(b) old frequency, `(4000, 8000)` — the receipt's printed `s_old[-1]`:**
`9.7491210 < s < 9.7491212`, so it prints `9.749121` (receipt: `9.749121102…`). -/
theorem bracket_old_4000 :
    9.7491210 < slope (-3) (-11) 4000 8000 ∧ slope (-3) (-11) 4000 8000 < 9.7491212 := by
  have e : slope (-3) (-11) 4000 8000 = slope (-(3 : ℝ)) (-(8 + 3)) 4000 (2 * 4000) := by norm_num
  obtain ⟨h1, h2⟩ := slope_bounds 3 (by norm_num) (by norm_num) 4000 (by norm_num)
  have hl2a := Real.log_two_gt_d9; have hl2b := Real.log_two_lt_d9
  have hl2 : 0 < Real.log 2 := by linarith
  rw [e]; norm_num at h1 h2 ⊢
  constructor
  · refine lt_of_lt_of_le ?_ h1; rw [lt_div_iff₀ hl2]; nlinarith
  · refine lt_of_le_of_lt h2 ?_; rw [div_lt_iff₀ hl2]; nlinarith
#print axioms ShadowProbe.Row65Slope.bracket_old_4000

/-- ⛭ **(b) `dis`, both pairs:** exactly `0`, as the receipt prints (`0.0e+00`). -/
theorem bracket_dis :
    slope 0 (-8) 2000 4000 = 0 ∧ slope 0 (-8) 4000 8000 = 0 := ⟨slope_dis _ _, slope_dis _ _⟩
#print axioms ShadowProbe.Row65Slope.bracket_dis

end ShadowProbe.Row65Slope

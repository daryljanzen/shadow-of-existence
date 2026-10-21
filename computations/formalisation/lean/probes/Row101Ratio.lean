import Mathlib.Analysis.SpecialFunctions.Trigonometric.ArctanDeriv
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.Analysis.SumIntegralComparisons

/-!
# Campaign 47 — row 101's open check: the `23.254 %` ratio

Gate Ⓔ③ (and the same number in Ⓔ④) of the P15 seam receipt asserts, for `g w = sin w ^ (-2/3)`,
`|100 · ∫_{π/4}^{π/2} g / ∫_0^{π/2} g − 23.254| < 0.002`. We prove it, together with the
(improper) integrability of `g` on `[0, π/2]`.

Route.
* Two exact changes of variable (`MeasureTheory.integral_image_eq_integral_abs_deriv_smul`):
  - `w = π/2 − arctan u`, `u ∈ [0,1]`: `∫_{π/4}^{π/2} g = ∫_0^1 (1+u²)^(-2/3)`;
  - `w = arctan (v³)`, `v ∈ (0,1]`: `∫_0^{π/4} g = 3 ∫_0^1 (1+v⁶)^(-2/3)`.
  The same theorem's integrability companion transfers integrability, so the singularity at `0`
  disappears: both new integrands are continuous on `[0,1]`.
* Both new integrands `F m x = (1+x^m)^(-2/3)` are antitone on `[0,∞)`, so left/right Riemann
  sums with `n = 5000` cells (`AntitoneOn.integral_le_sum`, `AntitoneOn.sum_le_integral`) bracket
  them; each sample `F m (k/n)` is bracketed by `U/D`, `(U−1)/D` (`D = 10⁷`) through the cube
  condition `D³n^{2m} ≤ U³(n^m+k^m)²`, checked for every `k` by `decide +kernel` over `ℕ`.
-/

namespace ShadowProbe.Row101Ratio

open Real MeasureTheory Set intervalIntegral

/-! ## 1. Kernel-checked arithmetic over `ℕ` -/

/-- Denominator of the sample brackets. -/
def Dn : ℕ := 10 ^ 7

/-- Binary search: least `x ∈ (lo, hi]` with `A ≤ x³·B` (given it holds at `hi`, fails at `lo`). -/
def bs (A B : ℕ) : ℕ → ℕ → ℕ → ℕ
  | 0, _, hi => hi
  | f + 1, lo, hi =>
    if hi ≤ lo + 1 then hi else
    let mid := (lo + hi) / 2
    if A ≤ mid ^ 3 * B then bs A B f lo mid else bs A B f mid hi

/-- The cube condition's two sides at sample `k/n` of `(1 + x^m)^(-2/3)`. -/
def cA (m n : ℕ) : ℕ := Dn ^ 3 * n ^ (2 * m)
def cB (m n k : ℕ) : ℕ := (n ^ m + k ^ m) ^ 2

/-- Upper numerator: `F m (k/n) ≤ UU m n k / Dn`. -/
def UU (m n k : ℕ) : ℕ := bs (cA m n) (cB m n k) 40 0 (Dn + 1)

/-- Both bracket conditions at sample `k`. -/
def ok (m n k : ℕ) : Bool :=
  Nat.ble (cA m n) (UU m n k ^ 3 * cB m n k) && Nat.ble ((UU m n k - 1) ^ 3 * cB m n k) (cA m n)

/-- Chunked checks and sums: `okR m n a N` checks samples `a … a+N−1`; `sU`, `sL` sum the upper
numerators `UU (a+j)` and lower numerators `UU (a+j+1) − 1` over `j < N`. Chunks of `1000` keep each
kernel evaluation small. -/
def okR (m n a N : ℕ) : Bool := Nat.rec true (fun j acc => ok m n (a + j) && acc) N
def sU (m n a N : ℕ) : ℕ := Nat.rec 0 (fun j acc => acc + UU m n (a + j)) N
def sL (m n a N : ℕ) : ℕ := Nat.rec 0 (fun j acc => acc + (UU m n (a + j + 1) - 1)) N

lemma okR_spec {m n a N : ℕ} (h : okR m n a N = true) : ∀ k, a ≤ k → k < a + N → ok m n k = true := by
  induction N with
  | zero => intro k _ _; omega
  | succ N ih =>
    have h' : (ok m n (a + N) && okR m n a N) = true := h
    rw [Bool.and_eq_true] at h'
    intro k hk1 hk2
    rcases Nat.lt_or_ge k (a + N) with hk | hk
    · exact ih h'.2 k hk1 hk
    · exact (show k = a + N by omega) ▸ h'.1

lemma ok_spec {m n k : ℕ} (h : ok m n k = true) :
    cA m n ≤ UU m n k ^ 3 * cB m n k ∧ (UU m n k - 1) ^ 3 * cB m n k ≤ cA m n := by
  simpa [ok, Bool.and_eq_true, Nat.ble_eq] using h

lemma sU_eq (m n a N : ℕ) : sU m n a N = ∑ j ∈ Finset.range N, UU m n (a + j) := by
  induction N with
  | zero => rfl
  | succ N ih => rw [Finset.sum_range_succ, ← ih]; rfl

lemma sL_eq (m n a N : ℕ) : sL m n a N = ∑ j ∈ Finset.range N, (UU m n (a + j + 1) - 1) := by
  induction N with
  | zero => rfl
  | succ N ih => rw [Finset.sum_range_succ, ← ih]; rfl

lemma five_chunks (f : ℕ → ℕ) (c : ℕ) :
    ∑ k ∈ Finset.range (5 * c), f k = ∑ j ∈ Finset.range c, f (0 + j)
      + ∑ j ∈ Finset.range c, f (c + j) + ∑ j ∈ Finset.range c, f (2 * c + j)
      + ∑ j ∈ Finset.range c, f (3 * c + j) + ∑ j ∈ Finset.range c, f (4 * c + j) := by
  rw [show 5 * c = c + c + c + c + c by ring]
  simp only [Finset.sum_range_add, zero_add]
  simp only [show c + c = 2 * c by ring, show 2 * c + c = 3 * c by ring,
    show 3 * c + c = 4 * c by ring]

/-! Every sample bracket, `k = 0 … 5000`, for both integrands (kernel-checked). -/
theorem ok2_0 : okR 2 5000 0 1000 = true := by decide +kernel
theorem ok2_1 : okR 2 5000 1000 1000 = true := by decide +kernel
theorem ok2_2 : okR 2 5000 2000 1000 = true := by decide +kernel
theorem ok2_3 : okR 2 5000 3000 1000 = true := by decide +kernel
theorem ok2_4 : okR 2 5000 4000 1001 = true := by decide +kernel
theorem ok6_0 : okR 6 5000 0 1000 = true := by decide +kernel
theorem ok6_1 : okR 6 5000 1000 1000 = true := by decide +kernel
theorem ok6_2 : okR 6 5000 2000 1000 = true := by decide +kernel
theorem ok6_3 : okR 6 5000 3000 1000 = true := by decide +kernel
theorem ok6_4 : okR 6 5000 4000 1001 = true := by decide +kernel

/-! The chunk sums (kernel-checked). -/
theorem sU2_0 : sU 2 5000 0 1000 = 9912974484 := by decide +kernel
theorem sU2_1 : sU 2 5000 1000 1000 = 9428083874 := by decide +kernel
theorem sU2_2 : sU 2 5000 2000 1000 = 8613050949 := by decide +kernel
theorem sU2_3 : sU 2 5000 3000 1000 = 7667071490 := by decide +kernel
theorem sU2_4 : sU 2 5000 4000 1000 = 6737572123 := by decide +kernel
theorem sL2_0 : sL 2 5000 0 1000 = 9912715402 := by decide +kernel
theorem sL2_1 : sL 2 5000 1000 1000 = 9427398867 := by decide +kernel
theorem sL2_2 : sL 2 5000 2000 1000 = 8612138595 := by decide +kernel
theorem sL2_3 : sL 2 5000 3000 1000 = 7666114627 := by decide +kernel
theorem sL2_4 : sL 2 5000 4000 1000 = 6736680035 := by decide +kernel
theorem sU6_0 : sU 6 5000 0 1000 = 9999939630 := by decide +kernel
theorem sU6_1 : sU 6 5000 1000 1000 = 9992287231 := by decide +kernel
theorem sU6_2 : sU 6 5000 2000 1000 = 9877335344 := by decide +kernel
theorem sU6_3 : sU 6 5000 3000 1000 = 9234116056 := by decide +kernel
theorem sU6_4 : sU 6 5000 4000 1000 = 7495473490 := by decide +kernel
theorem sL6_0 : sL 6 5000 0 1000 = 9999938204 := by decide +kernel
theorem sL6_1 : sL 6 5000 1000 1000 = 9992259444 := by decide +kernel
theorem sL6_2 : sL 6 5000 2000 1000 = 9877062130 := by decide +kernel
theorem sL6_3 : sL 6 5000 3000 1000 = 9232976855 := by decide +kernel
theorem sL6_4 : sL 6 5000 4000 1000 = 7493209724 := by decide +kernel

lemma ok_all (m : ℕ) (h0 : okR m 5000 0 1000 = true) (h1 : okR m 5000 1000 1000 = true)
    (h2 : okR m 5000 2000 1000 = true) (h3 : okR m 5000 3000 1000 = true)
    (h4 : okR m 5000 4000 1001 = true) : ∀ k < 5000 + 1, ok m 5000 k = true := by
  intro k hk
  rcases Nat.lt_or_ge k 1000 with a | a; · exact okR_spec h0 k (by omega) (by omega)
  rcases Nat.lt_or_ge k 2000 with b | b; · exact okR_spec h1 k (by omega) (by omega)
  rcases Nat.lt_or_ge k 3000 with c | c; · exact okR_spec h2 k (by omega) (by omega)
  rcases Nat.lt_or_ge k 4000 with d | d; · exact okR_spec h3 k (by omega) (by omega)
  exact okR_spec h4 k (by omega) (by omega)

lemma sumU_chunks (m : ℕ) : ∑ k ∈ Finset.range 5000, UU m 5000 k = sU m 5000 0 1000
    + sU m 5000 1000 1000 + sU m 5000 2000 1000 + sU m 5000 3000 1000 + sU m 5000 4000 1000 := by
  simp only [sU_eq]
  exact five_chunks (UU m 5000) 1000

lemma sumL_chunks (m : ℕ) : ∑ k ∈ Finset.range 5000, (UU m 5000 (k + 1) - 1) = sL m 5000 0 1000
    + sL m 5000 1000 1000 + sL m 5000 2000 1000 + sL m 5000 3000 1000 + sL m 5000 4000 1000 := by
  simp only [sL_eq]
  exact five_chunks (fun k => UU m 5000 (k + 1) - 1) 1000

/-! ## 2. Sample brackets over `ℝ` -/

/-- The two smooth integrands after substitution (`m = 2` and `m = 6`). -/
noncomputable def F (m : ℕ) (x : ℝ) : ℝ := (1 + x ^ m) ^ (-2/3 : ℝ)

lemma cube_key {a : ℝ} (ha : 0 < a) : (a ^ (-2/3 : ℝ)) ^ 3 * a ^ 2 = 1 := by
  rw [← Real.rpow_natCast, ← Real.rpow_mul ha.le, ← Real.rpow_natCast a 2, ← Real.rpow_add ha]
  norm_num

lemma rpow_le_of_cube {a c : ℝ} (ha : 0 < a) (hc : 0 ≤ c) (h : 1 ≤ c ^ 3 * a ^ 2) :
    a ^ (-2/3 : ℝ) ≤ c := by
  have hy : 0 ≤ a ^ (-2/3 : ℝ) := by positivity
  have h3 : (a ^ (-2/3 : ℝ)) ^ 3 ≤ c ^ 3 := by
    have := cube_key ha
    have ha2 : 0 < a ^ 2 := by positivity
    nlinarith
  exact (pow_le_pow_iff_left₀ hy hc (by norm_num)).mp h3

lemma le_rpow_of_cube {a c : ℝ} (ha : 0 < a) (hc : 0 ≤ c) (h : c ^ 3 * a ^ 2 ≤ 1) :
    c ≤ a ^ (-2/3 : ℝ) := by
  have hy : 0 ≤ a ^ (-2/3 : ℝ) := by positivity
  have h3 : c ^ 3 ≤ (a ^ (-2/3 : ℝ)) ^ 3 := by
    have := cube_key ha
    have ha2 : 0 < a ^ 2 := by positivity
    nlinarith
  exact (pow_le_pow_iff_left₀ hc hy (by norm_num)).mp h3

lemma Dn_pos : (0 : ℝ) < Dn := by norm_num [Dn]

lemma cube_ratio (m n k U : ℕ) (hn : 0 < n) :
    ((U : ℝ) / Dn) ^ 3 * (1 + ((k : ℝ) / n) ^ m) ^ 2
      = (U ^ 3 * cB m n k : ℕ) / (cA m n : ℕ) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hD := Dn_pos
  have e : 1 + ((k : ℝ) / n) ^ m = ((n : ℝ) ^ m + k ^ m) / n ^ m := by
    rw [div_pow]; field_simp
  simp only [cA, cB]
  rw [e, div_pow, div_pow, div_mul_div_comm]
  push_cast
  ring

lemma F_le (m n k U : ℕ) (hn : 0 < n) (h : cA m n ≤ U ^ 3 * cB m n k) :
    F m ((k : ℝ) / n) ≤ (U : ℝ) / Dn := by
  have hA : (0 : ℝ) < (cA m n : ℕ) := by
    have : 0 < cA m n := by unfold cA Dn; positivity
    exact_mod_cast this
  apply rpow_le_of_cube (by positivity) (div_nonneg (Nat.cast_nonneg _) Dn_pos.le)
  rw [cube_ratio m n k U hn, one_le_div hA]
  exact_mod_cast h

lemma le_F (m n k L : ℕ) (hn : 0 < n) (h : L ^ 3 * cB m n k ≤ cA m n) :
    (L : ℝ) / Dn ≤ F m ((k : ℝ) / n) := by
  have hA : (0 : ℝ) < (cA m n : ℕ) := by
    have : 0 < cA m n := by unfold cA Dn; positivity
    exact_mod_cast this
  apply le_rpow_of_cube (by positivity) (div_nonneg (Nat.cast_nonneg _) Dn_pos.le)
  rw [cube_ratio m n k L hn, div_le_one hA]
  exact_mod_cast h

/-! ## 3. Riemann brackets for `∫_0^1 F m` -/

lemma F_anti (m : ℕ) : AntitoneOn (F m) (Ici 0) := by
  intro x hx y hy hxy
  have hx' : (0 : ℝ) ≤ x := hx
  exact Real.rpow_le_rpow_of_nonpos (by positivity) (by gcongr) (by norm_num)

lemma F_contOn (m : ℕ) : ContinuousOn (F m) (Ici 0) := by
  unfold F
  exact (continuousOn_const.add (continuous_pow m).continuousOn).rpow_const
    (fun x hx => Or.inl (by have : (0 : ℝ) ≤ x := hx; exact (by positivity : (0 : ℝ) < 1 + x ^ m).ne'))

lemma F_intOn (m : ℕ) : IntegrableOn (F m) (Icc 0 1) :=
  ((F_contOn m).mono Icc_subset_Ici_self).integrableOn_Icc

lemma F_anti_scaled (m n : ℕ) (hn : 0 < n) :
    AntitoneOn (fun t : ℝ => F m (t / n)) (Icc 0 (0 + (n : ℝ))) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  intro x hx y hy hxy
  exact F_anti m (div_nonneg hx.1 hn'.le) (div_nonneg hy.1 hn'.le)
    (div_le_div_of_nonneg_right hxy hn'.le)

lemma integral_scaled (m n : ℕ) (hn : 0 < n) :
    ∫ t in (0 : ℝ)..0 + (n : ℝ), F m (t / n) = n * ∫ x in (0 : ℝ)..1, F m x := by
  have hn' : (n : ℝ) ≠ 0 := by exact_mod_cast hn.ne'
  rw [zero_add, intervalIntegral.integral_comp_div _ hn', zero_div, div_self hn', smul_eq_mul]

theorem integral_F_le (m n : ℕ) (hn : 0 < n) (hok : ∀ k < n + 1, ok m n k = true) :
    ∫ x in (0 : ℝ)..1, F m x ≤ ((∑ k ∈ Finset.range n, UU m n k : ℕ) : ℝ) / (n * Dn) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have h1 := (F_anti_scaled m n hn).integral_le_sum
  rw [integral_scaled m n hn] at h1
  have h2 : ∑ i ∈ Finset.range n, F m ((0 + (i : ℝ)) / n)
      ≤ ∑ i ∈ Finset.range n, ((UU m n i : ℝ) / Dn) := by
    apply Finset.sum_le_sum
    intro i hi
    rw [zero_add]
    exact F_le m n i _ hn (ok_spec (hok i (by simp at hi; omega))).1
  rw [← Finset.sum_div, le_div_iff₀ Dn_pos] at h2
  rw [Nat.cast_sum, le_div_iff₀ (mul_pos hn' Dn_pos)]
  calc (∫ x in (0 : ℝ)..1, F m x) * (n * Dn) = (n * ∫ x in (0 : ℝ)..1, F m x) * Dn := by ring
    _ ≤ (∑ i ∈ Finset.range n, F m ((0 + (i : ℝ)) / n)) * Dn :=
        mul_le_mul_of_nonneg_right h1 Dn_pos.le
    _ ≤ _ := h2

theorem le_integral_F (m n : ℕ) (hn : 0 < n) (hok : ∀ k < n + 1, ok m n k = true) :
    ((∑ k ∈ Finset.range n, (UU m n (k + 1) - 1) : ℕ) : ℝ) / (n * Dn) ≤ ∫ x in (0 : ℝ)..1, F m x := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have h1 := (F_anti_scaled m n hn).sum_le_integral
  rw [integral_scaled m n hn] at h1
  have h2 : ∑ i ∈ Finset.range n, ((UU m n (i + 1) - 1 : ℕ) : ℝ) / Dn
      ≤ ∑ i ∈ Finset.range n, F m ((0 + ((i + 1 : ℕ) : ℝ)) / n) := by
    apply Finset.sum_le_sum
    intro i hi
    rw [zero_add]
    exact le_F m n (i + 1) _ hn (ok_spec (hok (i + 1) (by simp at hi; omega))).2
  rw [← Finset.sum_div, div_le_iff₀ Dn_pos] at h2
  rw [Nat.cast_sum, div_le_iff₀ (mul_pos hn' Dn_pos)]
  calc _ ≤ (∑ i ∈ Finset.range n, F m ((0 + ((i + 1 : ℕ) : ℝ)) / n)) * Dn := h2
    _ ≤ (n * ∫ x in (0 : ℝ)..1, F m x) * Dn := mul_le_mul_of_nonneg_right h1 Dn_pos.le
    _ = _ := by ring

/-! ## 4. The two changes of variable -/

/-- The receipt's integrand. -/
noncomputable def g (w : ℝ) : ℝ := Real.sin w ^ (-2/3 : ℝ)

lemma arctan_tan' {t : ℝ} (h0 : 0 ≤ t) (h1 : t ≤ π / 4) : arctan (tan t) = t :=
  arctan_tan (by linarith [pi_pos]) (by linarith [pi_pos])

/-- Upper piece: `w = π/2 − arctan u`. -/
lemma image_upper : (fun u => π / 2 - arctan u) '' Icc 0 1 = Icc (π / 4) (π / 2) := by
  ext w
  constructor
  · rintro ⟨u, ⟨h0, h1⟩, rfl⟩
    have a0 : arctan 0 ≤ arctan u := arctan_strictMono.monotone h0
    have a1 : arctan u ≤ arctan 1 := arctan_strictMono.monotone h1
    rw [arctan_zero] at a0; rw [arctan_one] at a1
    constructor <;> linarith
  · rintro ⟨h1, h2⟩
    have ht := arctan_tan' (t := π / 2 - w) (by linarith) (by linarith)
    refine ⟨tan (π / 2 - w), ⟨?_, ?_⟩, by simp only [ht]; ring⟩
    · rw [← arctan_strictMono.le_iff_le, ht, arctan_zero]; linarith
    · rw [← arctan_strictMono.le_iff_le, ht, arctan_one]; linarith

lemma upper_pt (u : ℝ) : |(-(1 / (1 + u ^ 2)))| • g (π / 2 - arctan u) = F 2 u := by
  have ha : 0 < 1 + u ^ 2 := by positivity
  have h1 : 1 / √(1 + u ^ 2) = (1 + u ^ 2) ^ (-(1/2) : ℝ) := by
    rw [Real.sqrt_eq_rpow, Real.rpow_neg ha.le, one_div]
  have h2 : 1 / (1 + u ^ 2) = (1 + u ^ 2) ^ (-1 : ℝ) := by rw [Real.rpow_neg_one, one_div]
  unfold g F
  rw [Real.sin_pi_div_two_sub, cos_arctan, abs_neg, abs_of_pos (by positivity), smul_eq_mul,
    h1, h2, ← Real.rpow_mul ha.le, ← Real.rpow_add ha]
  norm_num

theorem upper_piece :
    IntervalIntegrable g volume (π / 4) (π / 2) ∧
      ∫ w in (π / 4)..(π / 2), g w = ∫ u in (0 : ℝ)..1, F 2 u := by
  have hle : π / 4 ≤ π / 2 := by linarith [pi_pos]
  have hder : ∀ u ∈ Icc (0 : ℝ) 1,
      HasDerivWithinAt (fun u => π / 2 - arctan u) (-(1 / (1 + u ^ 2))) (Icc 0 1) u :=
    fun u _ => ((hasDerivAt_arctan u).const_sub (π / 2)).hasDerivWithinAt
  have hinj : InjOn (fun u => π / 2 - arctan u) (Icc 0 1) := by
    intro a _ b _ h
    exact arctan_injective (by simp only at h; linarith)
  have hpt : (fun u => |(-(1 / (1 + u ^ 2)))| • g (π / 2 - arctan u)) = F 2 := funext upper_pt
  have key := integral_image_eq_integral_abs_deriv_smul measurableSet_Icc hder hinj g
  have hint := integrableOn_image_iff_integrableOn_abs_deriv_smul measurableSet_Icc hder hinj g
  rw [image_upper, hpt] at key hint
  constructor
  · exact (intervalIntegrable_iff_integrableOn_Icc_of_le hle).mpr
      (hint.mpr (F_intOn 2))
  · rw [intervalIntegral.integral_of_le hle, intervalIntegral.integral_of_le zero_le_one,
      ← integral_Icc_eq_integral_Ioc, ← integral_Icc_eq_integral_Ioc, key]

/-- Lower piece: `w = arctan (v³)`. -/
lemma image_lower : (fun v => arctan (v ^ 3)) '' Ioc 0 1 = Ioc 0 (π / 4) := by
  ext w
  constructor
  · rintro ⟨v, ⟨h0, h1⟩, rfl⟩
    have a0 : arctan 0 < arctan (v ^ 3) := arctan_strictMono (by positivity)
    have a1 : arctan (v ^ 3) ≤ arctan 1 := arctan_strictMono.monotone (pow_le_one₀ h0.le h1)
    rw [arctan_zero] at a0; rw [arctan_one] at a1
    exact ⟨a0, a1⟩
  · rintro ⟨h0, h1⟩
    have ht0 : 0 < tan w := tan_pos_of_pos_of_lt_pi_div_two h0 (by linarith [pi_pos])
    have hat := arctan_tan' h0.le h1
    have hcube : ((tan w) ^ (1/3 : ℝ)) ^ 3 = tan w := by
      rw [← Real.rpow_natCast, ← Real.rpow_mul ht0.le]; norm_num
    refine ⟨(tan w) ^ (1/3 : ℝ), ⟨by positivity, ?_⟩, by simp only [hcube, hat]⟩
    apply Real.rpow_le_one ht0.le _ (by norm_num)
    rw [← arctan_strictMono.le_iff_le, hat, arctan_one]; exact h1

lemma lower_pt (v : ℝ) (hv : 0 < v) :
    |1 / (1 + (v ^ 3) ^ 2) * (((3 : ℕ) : ℝ) * v ^ (3 - 1))| • g (arctan (v ^ 3)) = 3 * F 6 v := by
  have e6 : (v ^ 3) ^ 2 = v ^ 6 := by ring
  rw [e6]
  set a : ℝ := 1 + v ^ 6 with ha_def
  have ha : 0 < a := by positivity
  have h3 : (v ^ 3) ^ (-2/3 : ℝ) = (v ^ 2)⁻¹ := by
    rw [← Real.rpow_natCast v 3, ← Real.rpow_mul hv.le, ← Real.rpow_two, ← Real.rpow_neg hv.le]
    norm_num
  have h4 : (√a) ^ (-2/3 : ℝ) = a ^ (-1/3 : ℝ) := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_mul ha.le]; norm_num
  have h2 : 1 / a = a ^ (-1 : ℝ) := by rw [Real.rpow_neg_one, one_div]
  have hfin : 3 * (v ^ 2 * (v ^ 2)⁻¹) * (a ^ (-1 : ℝ) / a ^ (-1/3 : ℝ)) = 3 * a ^ (-2/3 : ℝ) := by
    rw [mul_inv_cancel₀ (by positivity), ← Real.rpow_sub ha]; norm_num
  unfold g F
  rw [sin_arctan, e6, ← ha_def, abs_of_pos (by positivity), smul_eq_mul,
    Real.div_rpow (by positivity) (by positivity), h3, h4, h2, ← hfin]
  push_cast
  ring

theorem lower_piece :
    IntervalIntegrable g volume 0 (π / 4) ∧
      ∫ w in (0 : ℝ)..(π / 4), g w = 3 * ∫ v in (0 : ℝ)..1, F 6 v := by
  have hle : (0 : ℝ) ≤ π / 4 := by linarith [pi_pos]
  have hder : ∀ v ∈ Ioc (0 : ℝ) 1,
      HasDerivWithinAt (fun v => arctan (v ^ 3))
        (1 / (1 + (v ^ 3) ^ 2) * (((3 : ℕ) : ℝ) * v ^ (3 - 1))) (Ioc 0 1) v :=
    fun v _ => (hasDerivAt_pow 3 v).arctan.hasDerivWithinAt
  have hinj : InjOn (fun v => arctan (v ^ 3)) (Ioc 0 1) := by
    intro a ha b hb h
    have := arctan_injective h
    exact (pow_left_inj₀ ha.1.le hb.1.le (by norm_num)).mp this
  have hpt : EqOn (fun v => |1 / (1 + (v ^ 3) ^ 2) * (((3 : ℕ) : ℝ) * v ^ (3 - 1))| •
      g (arctan (v ^ 3))) (fun v => 3 * F 6 v) (Ioc 0 1) := fun v hv => lower_pt v hv.1
  have key := integral_image_eq_integral_abs_deriv_smul measurableSet_Ioc hder hinj g
  have hint := integrableOn_image_iff_integrableOn_abs_deriv_smul measurableSet_Ioc hder hinj g
  rw [image_lower] at key hint
  constructor
  · refine (intervalIntegrable_iff_integrableOn_Ioc_of_le hle).mpr (hint.mpr ?_)
    have hc : IntegrableOn (fun v => 3 * F 6 v) (Icc 0 1) := (F_intOn 6).const_mul 3
    exact (hc.mono_set Ioc_subset_Icc_self).congr_fun hpt.symm measurableSet_Ioc
  · rw [intervalIntegral.integral_of_le hle, intervalIntegral.integral_of_le zero_le_one, key,
      setIntegral_congr_fun measurableSet_Ioc hpt, MeasureTheory.integral_const_mul]

/-! ## 5. The headline -/

/-- **Row 101, gate Ⓔ③/Ⓔ④.** `g = sin^(-2/3)` is (improperly) integrable on `[0, π/2]`, and
`∫_{π/4}^{π/2} g / ∫_0^{π/2} g ∈ (0.23252, 0.23256)`. -/
theorem row101_ratio :
    IntervalIntegrable (fun w => Real.sin w ^ (-2/3 : ℝ)) volume 0 (π / 2) ∧
    (0.23252 : ℝ) < (∫ w in (π / 4)..(π / 2), Real.sin w ^ (-2/3 : ℝ)) /
        (∫ w in (0 : ℝ)..(π / 2), Real.sin w ^ (-2/3 : ℝ)) ∧
    (∫ w in (π / 4)..(π / 2), Real.sin w ^ (-2/3 : ℝ)) /
        (∫ w in (0 : ℝ)..(π / 2), Real.sin w ^ (-2/3 : ℝ)) < (0.23256 : ℝ) := by
  obtain ⟨hi1, e1⟩ := upper_piece
  obtain ⟨hi0, e0⟩ := lower_piece
  have hsplit : ∫ w in (0 : ℝ)..(π / 2), g w = (∫ w in (0 : ℝ)..(π / 4), g w) +
      ∫ w in (π / 4)..(π / 2), g w := (integral_add_adjacent_intervals hi0 hi1).symm
  change IntervalIntegrable g volume 0 (π / 2) ∧
    (0.23252 : ℝ) < (∫ w in (π / 4)..(π / 2), g w) / (∫ w in (0 : ℝ)..(π / 2), g w) ∧
    (∫ w in (π / 4)..(π / 2), g w) / (∫ w in (0 : ℝ)..(π / 2), g w) < (0.23256 : ℝ)
  rw [hsplit, e0, e1]
  have ok2 := ok_all 2 ok2_0 ok2_1 ok2_2 ok2_3 ok2_4
  have ok6 := ok_all 6 ok6_0 ok6_1 ok6_2 ok6_3 ok6_4
  have pU := integral_F_le 2 5000 (by norm_num) ok2
  have pL := le_integral_F 2 5000 (by norm_num) ok2
  have qU := integral_F_le 6 5000 (by norm_num) ok6
  have qL := le_integral_F 6 5000 (by norm_num) ok6
  rw [sumU_chunks, sU2_0, sU2_1, sU2_2, sU2_3, sU2_4] at pU
  rw [sumL_chunks, sL2_0, sL2_1, sL2_2, sL2_3, sL2_4] at pL
  rw [sumU_chunks, sU6_0, sU6_1, sU6_2, sU6_3, sU6_4] at qU
  rw [sumL_chunks, sL6_0, sL6_1, sL6_2, sL6_3, sL6_4] at qL
  simp only [Dn] at pU pL qU qL
  norm_num at pU pL qU qL
  set P := ∫ u in (0 : ℝ)..1, F 2 u
  set Q := ∫ v in (0 : ℝ)..1, F 6 v
  have hT : 0 < 3 * Q + P := by linarith
  refine ⟨hi0.trans hi1, ?_, ?_⟩
  · rw [lt_div_iff₀ hT]; linarith
  · rw [div_lt_iff₀ hT]; linarith

/-- The receipt's own form: `|frac − 23.254| < 0.002` with `frac` in per cent. -/
theorem row101_frac :
    |100 * ((∫ w in (π / 4)..(π / 2), Real.sin w ^ (-2/3 : ℝ)) /
        (∫ w in (0 : ℝ)..(π / 2), Real.sin w ^ (-2/3 : ℝ))) - 23.254| < 0.002 := by
  obtain ⟨_, h1, h2⟩ := row101_ratio
  rw [abs_sub_lt_iff]; constructor <;> linarith

end ShadowProbe.Row101Ratio

#print axioms ShadowProbe.Row101Ratio.row101_ratio
#print axioms ShadowProbe.Row101Ratio.row101_frac

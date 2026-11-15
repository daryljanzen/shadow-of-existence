import Mathlib

/-!
# P14 (`matter_sector_paper`): `prop:wall`, one normalizable chiral zero-mode per wall

Campaign 143 (`r7801`). Registration: `computations/formalisation/r7801_71_campaign143/PREDICTION.md`. Mathlib only;
nothing imports this file.
-/

open Real Filter Topology Set MeasureTheory

namespace ShadowProbe.MatterWallProbe

/-! ## Row Z2: exactly one normalizable zero mode for any kink -/

section Kink

variable {m F : ℝ → ℝ}

/-- Every solution of `f′ = −mf` is `c·e^{−F}`, with `F′ = m`. -/
lemma mw_unique_minus (hF : ∀ x, HasDerivAt F (m x) x) {f : ℝ → ℝ} (hf : ∀ x, HasDerivAt f (-(m x) * f x) x) :
    ∀ x, f x = f 0 * Real.exp (F 0) * Real.exp (-F x) := by
  have hG : ∀ x, HasDerivAt (fun y => f y * Real.exp (F y)) 0 x := fun x => by
    convert (hf x).mul ((hF x).exp) using 1; ring
  intro x
  have := is_const_of_deriv_eq_zero (fun y => (hG y).differentiableAt) (fun y => (hG y).deriv) x 0
  rw [← this, mul_assoc, ← Real.exp_add]; simp

/-- Every solution of `g′ = mg` is `c·e^{F}`. -/
lemma mw_unique_plus (hF : ∀ x, HasDerivAt F (m x) x) {g : ℝ → ℝ} (hg : ∀ x, HasDerivAt g (m x * g x) x) :
    ∀ x, g x = g 0 * Real.exp (-F 0) * Real.exp (F x) := by
  have hG : ∀ x, HasDerivAt (fun y => g y * Real.exp (-F y)) 0 x := fun x => by
    convert (hg x).mul ((hF x).neg.exp) using 1; ring
  intro x
  have := is_const_of_deriv_eq_zero (fun y => (hG y).differentiableAt) (fun y => (hG y).deriv) x 0
  rw [← this, mul_assoc, ← Real.exp_add]; simp

/-- For a kink (`m ≥ m₀ > 0` right of `X`, `m ≤ −m₀` left of `−X`), the antiderivative grows at least linearly in
`|x|`: `F x ≥ m₀|x| − K`. -/
lemma mw_F_lower (hF : ∀ x, HasDerivAt F (m x) x) {m0 X : ℝ} (hm0 : 0 ≤ m0) (hX : 0 ≤ X)
    (hR : ∀ x, X ≤ x → m0 ≤ m x) (hL : ∀ x, x ≤ -X → m x ≤ -m0) : ∃ K, ∀ x, m0 * |x| - K ≤ F x := by
  have hc : Continuous F := continuous_iff_continuousAt.2 fun x => (hF x).continuousAt
  obtain ⟨x₀, -, hmin⟩ := isCompact_Icc.exists_isMinOn (nonempty_Icc.2 (by linarith : -X ≤ X)) hc.continuousOn
  set B := F x₀
  have hB : ∀ x ∈ Icc (-X) X, B ≤ F x := fun x hx => hmin hx
  -- right: `F − m₀ x` is monotone on `[X, ∞)`
  have dR : ∀ x, HasDerivAt (fun x => F x - m0 * x) (m x - m0) x := fun x => by
    simpa using (hF x).fun_sub ((hasDerivAt_id' x).const_mul m0)
  have dL : ∀ x, HasDerivAt (fun x => F x + m0 * x) (m x + m0) x := fun x => by
    simpa using (hF x).fun_add ((hasDerivAt_id' x).const_mul m0)
  have hmono : MonotoneOn (fun x => F x - m0 * x) (Ici X) := by
    refine monotoneOn_of_deriv_nonneg (convex_Ici X) ((hc.sub (continuous_const.mul continuous_id)).continuousOn)
      (fun x _ => (dR x).differentiableAt.differentiableWithinAt) ?_
    intro x hx
    rw [interior_Ici] at hx
    rw [(dR x).deriv]
    linarith [hR x (le_of_lt hx)]
  -- left: `F + m₀ x` is antitone on `(−∞, −X]`
  have hanti : AntitoneOn (fun x => F x + m0 * x) (Iic (-X)) := by
    refine antitoneOn_of_deriv_nonpos (convex_Iic (-X)) ((hc.add (continuous_const.mul continuous_id)).continuousOn)
      (fun x _ => (dL x).differentiableAt.differentiableWithinAt) ?_
    intro x hx
    rw [interior_Iic] at hx
    rw [(dL x).deriv]
    linarith [hL x (le_of_lt hx)]
  refine ⟨m0 * X - B, fun x => ?_⟩
  rcases le_or_gt X x with h1 | h1
  · have := hmono (Set.mem_Ici.2 le_rfl) h1 h1
    have hBX := hB X ⟨by linarith, le_refl X⟩
    rw [abs_of_nonneg (by linarith)]
    linarith
  · rcases le_or_gt x (-X) with h2 | h2
    · have := hanti h2 (Set.mem_Iic.2 le_rfl) h2
      have hBX := hB (-X) ⟨le_refl _, by linarith⟩
      rw [abs_of_nonpos (by linarith)]
      linarith
    · have hx : x ∈ Icc (-X) X := ⟨h2.le, h1.le⟩
      have := hB x hx
      have : m0 * |x| ≤ m0 * X := mul_le_mul_of_nonneg_left (abs_le.2 ⟨h2.le, h1.le⟩) hm0
      linarith

/-- `e^{−c|x|}` (`c > 0`) is integrable on `ℝ`. -/
lemma mw_exp_abs_integrable {c : ℝ} (hc : 0 < c) : Integrable (fun x => Real.exp (-(c * |x|))) := by
  have h1 : IntegrableOn (fun x => Real.exp (-(c * |x|))) (Iic 0) := by
    refine (integrableOn_exp_mul_Iic hc 0).congr_fun (fun x (hx : x ≤ 0) => ?_) measurableSet_Iic
    simp only; rw [abs_of_nonpos hx]; ring_nf
  have h2 : IntegrableOn (fun x => Real.exp (-(c * |x|))) (Ioi 0) := by
    refine (exp_neg_integrableOn_Ioi 0 hc).congr_fun (fun x (hx : 0 < x) => ?_) measurableSet_Ioi
    simp only; rw [abs_of_pos hx, neg_mul]
  have := h1.union h2
  rwa [Iic_union_Ioi, integrableOn_univ] at this

/-- **Z2, the bound mode.** If `F ≥ m₀|x| − K` (`m₀ > 0`), then `(e^{−F})²` is integrable. -/
lemma mw_bound_integrable (hc : Continuous F) {m0 K : ℝ} (hm0 : 0 < m0) (hK : ∀ x, m0 * |x| - K ≤ F x) :
    Integrable (fun x => Real.exp (-F x) ^ 2) := by
  refine ((mw_exp_abs_integrable (by linarith : 0 < 2 * m0)).const_mul (Real.exp (2 * K))).mono'
    ((hc.neg.rexp.pow 2).aestronglyMeasurable) (Eventually.of_forall fun x => ?_)
  rw [Real.norm_eq_abs, abs_of_nonneg (by positivity), ← Real.exp_nat_mul, ← Real.exp_add]
  apply Real.exp_le_exp.2
  have := hK x
  push_cast
  linarith

/-- **Z2, the rejected mode.** If `F ≥ m₀|x| − K` (`m₀ > 0`), then `(c·e^{F})²` is integrable only for `c = 0`. -/
lemma mw_conj_not_integrable {m0 K c : ℝ} (hm0 : 0 < m0) (hK : ∀ x, m0 * |x| - K ≤ F x) (hcz : c ≠ 0) :
    ¬ Integrable (fun x => (c * Real.exp (F x)) ^ 2) := by
  intro hI
  set x0 := max 0 (K / m0)
  have hge : ∀ x ∈ Ici x0, c ^ 2 ≤ (c * Real.exp (F x)) ^ 2 := by
    intro x hx
    have hx0 : 0 ≤ x := le_trans (le_max_left _ _) hx
    have hxK : K ≤ m0 * x := by
      have := le_trans (le_max_right _ _) (show x0 ≤ x from hx)
      rw [div_le_iff₀ hm0] at this; linarith
    have hF0 : 0 ≤ F x := by have := hK x; rw [abs_of_nonneg hx0] at this; linarith
    rw [mul_pow]
    exact le_mul_of_one_le_right (sq_nonneg c) (one_le_pow₀ (Real.one_le_exp hF0))
  have hconst : IntegrableOn (fun _ => c ^ 2) (Ici x0) := by
    refine (hI.integrableOn).mono' (continuous_const.aestronglyMeasurable) ?_
    refine (ae_restrict_iff' measurableSet_Ici).2 (Eventually.of_forall fun x hx => ?_)
    rw [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg c)]
    exact hge x hx
  rw [integrableOn_const_iff] at hconst
  rcases hconst with h | h
  · exact hcz (pow_eq_zero_iff (n := 2) (by norm_num) |>.1 (enorm_eq_zero.1 h))
  · simp [Real.volume_Ici] at h

/-- **Row Z2.** For a kink `m` (`m ≥ m₀ > 0` for `x ≥ X`, `m ≤ −m₀` for `x ≤ −X`) with antiderivative `F`:
`e^{−F}` solves `f′ = −mf` and is normalizable; every solution of `f′ = −mf` is a multiple of it; and the only
normalizable solution of the conjugate equation `g′ = mg` is `0`. So the normalizable zero modes are exactly the
line `{(c e^{−F}, 0)}`: one mode, in the `σ_y = +1` chirality. -/
theorem mw_exactly_one (hF : ∀ x, HasDerivAt F (m x) x) {m0 X : ℝ} (hm0 : 0 < m0) (hX : 0 ≤ X)
    (hR : ∀ x, X ≤ x → m0 ≤ m x) (hL : ∀ x, x ≤ -X → m x ≤ -m0) :
    (∀ x, HasDerivAt (fun y => Real.exp (-F y)) (-(m x) * Real.exp (-F x)) x) ∧
      Integrable (fun x => Real.exp (-F x) ^ 2) ∧
      (∀ f : ℝ → ℝ, (∀ x, HasDerivAt f (-(m x) * f x) x) → ∃ c, ∀ x, f x = c * Real.exp (-F x)) ∧
      (∀ g : ℝ → ℝ, (∀ x, HasDerivAt g (m x * g x) x) → Integrable (fun x => g x ^ 2) → ∀ x, g x = 0) := by
  obtain ⟨K, hK⟩ := mw_F_lower hF hm0.le hX hR hL
  have hc : Continuous F := continuous_iff_continuousAt.2 fun x => (hF x).continuousAt
  refine ⟨fun x => by simpa [mul_comm] using (hF x).neg.exp, mw_bound_integrable hc hm0 hK,
    fun f hf => ⟨_, mw_unique_minus hF hf⟩, fun g hg hI x => ?_⟩
  have hgx := mw_unique_plus hF hg
  by_contra hne
  have hcz : g 0 * Real.exp (-F 0) ≠ 0 := by
    intro h; apply hne; rw [hgx x, h, zero_mul]
  exact mw_conj_not_integrable hm0 hK hcz (hI.congr (Eventually.of_forall fun y => by simp only; rw [hgx y]))

/-- **Row Z3.** The flip: for the reversed wall (`m ≤ −m₀` right, `m ≥ m₀` left) the normalizable zero modes are exactly
the line `{(0, c e^{F})}`, the `σ_y = −1` chirality. Reversing the wall reverses the chirality. -/
theorem mw_flip (hF : ∀ x, HasDerivAt F (m x) x) {m0 X : ℝ} (hm0 : 0 < m0) (hX : 0 ≤ X)
    (hR : ∀ x, X ≤ x → m x ≤ -m0) (hL : ∀ x, x ≤ -X → m0 ≤ m x) :
    (∀ x, HasDerivAt (fun y => Real.exp (F y)) (m x * Real.exp (F x)) x) ∧
      Integrable (fun x => Real.exp (F x) ^ 2) ∧
      (∀ g : ℝ → ℝ, (∀ x, HasDerivAt g (m x * g x) x) → ∃ c, ∀ x, g x = c * Real.exp (F x)) ∧
      (∀ f : ℝ → ℝ, (∀ x, HasDerivAt f (-(m x) * f x) x) → Integrable (fun x => f x ^ 2) → ∀ x, f x = 0) := by
  obtain ⟨h1, h2, h3, h4⟩ := mw_exactly_one (m := fun x => -m x) (F := fun x => -F x) (fun x => (hF x).neg) hm0 hX
    (fun x hx => by linarith [hR x hx]) (fun x hx => by linarith [hL x hx])
  simp only [neg_neg] at h1 h2 h3 h4
  exact ⟨h1, h2, fun g hg => h3 g (fun x => by simpa using hg x), fun f hf => h4 f (fun x => by simpa using hf x)⟩

end Kink

/-! ## Row Z4: the displayed wall `m = tanh(x/a)` -/

lemma mw_tanh_ge {y : ℝ} (hy : 1 ≤ y) : 1 / 2 ≤ Real.tanh y := by
  rw [Real.tanh_eq_sinh_div_cosh, le_div_iff₀ (Real.cosh_pos y), Real.sinh_eq, Real.cosh_eq, Real.exp_neg]
  have hu : 0 < Real.exp y := Real.exp_pos y
  have hu2 : 3 ≤ Real.exp y ^ 2 := by
    rw [← Real.exp_nat_mul]; push_cast; linarith [Real.add_one_le_exp (2 * y)]
  field_simp
  nlinarith

lemma mw_tanh_F (a x : ℝ) (ha : a ≠ 0) :
    HasDerivAt (fun y => a * Real.log (Real.cosh (y / a))) (Real.tanh (x / a)) x := by
  have h := ((((hasDerivAt_id x).div_const a).cosh).log (Real.cosh_pos _).ne').const_mul a
  convert h using 1
  · rfl
  · simp only [id]; rw [Real.tanh_eq_sinh_div_cosh]; field_simp

lemma mw_cosh_rpow (a x : ℝ) (s : ℝ) :
    Real.cosh (x / a) ^ s = Real.exp (s * (Real.log (Real.cosh (x / a)))) := by
  rw [Real.rpow_def_of_pos (Real.cosh_pos _), mul_comm]

/-- **Row Z4.** The paper's wall `m = tanh(x/a)`, `a > 0`: the bound mode `cosh^{−a}(x/a)` solves `f′ = −mf` and is
normalizable, every solution is a multiple of it, and the conjugate `cosh^{a}(x/a)` is not normalizable. -/
theorem mw_tanh {a : ℝ} (ha : 0 < a) :
    (∀ x, HasDerivAt (fun y => Real.cosh (y / a) ^ (-a)) (-Real.tanh (x / a) * Real.cosh (x / a) ^ (-a)) x) ∧
      Integrable (fun x => (Real.cosh (x / a) ^ (-a)) ^ 2) ∧
      (∀ f : ℝ → ℝ, (∀ x, HasDerivAt f (-Real.tanh (x / a) * f x) x) →
        ∃ c, ∀ x, f x = c * Real.cosh (x / a) ^ (-a)) ∧
      ¬ Integrable (fun x => (Real.cosh (x / a) ^ a) ^ 2) := by
  set F : ℝ → ℝ := fun y => a * Real.log (Real.cosh (y / a))
  have hF : ∀ x, HasDerivAt F (Real.tanh (x / a)) x := fun x => mw_tanh_F a x ha.ne'
  have hR : ∀ x, a ≤ x → 1 / 2 ≤ Real.tanh (x / a) := fun x hx =>
    mw_tanh_ge (by rw [le_div_iff₀ ha]; linarith)
  have hL : ∀ x, x ≤ -a → Real.tanh (x / a) ≤ -(1 / 2) := fun x hx => by
    have hxa : x / a ≤ -1 := by rw [div_le_iff₀ ha]; linarith
    have := mw_tanh_ge (y := -(x / a)) (by linarith)
    rw [Real.tanh_neg] at this; linarith
  have em : ∀ x, Real.cosh (x / a) ^ (-a) = Real.exp (-F x) := fun x => by
    rw [mw_cosh_rpow]; simp only [F]; ring_nf
  have ep : ∀ x, Real.cosh (x / a) ^ a = 1 * Real.exp (F x) := fun x => by
    rw [mw_cosh_rpow, one_mul]
  obtain ⟨h1, h2, h3, -⟩ := mw_exactly_one hF (by norm_num : (0 : ℝ) < 1 / 2) ha.le hR hL
  obtain ⟨K, hK⟩ := mw_F_lower hF (by norm_num : (0 : ℝ) ≤ 1 / 2) ha.le hR hL
  refine ⟨fun x => ?_, ?_, fun f hf => ?_, ?_⟩
  · simp only [em]; exact h1 x
  · simp only [em]; exact h2
  · obtain ⟨c, hc⟩ := h3 f hf; exact ⟨c, fun x => by rw [hc x, em]⟩
  · simp only [ep]; exact mw_conj_not_integrable (by norm_num : (0 : ℝ) < 1 / 2) hK one_ne_zero

/-! ## Row Z1: the chirality basis -/

/-- `σ_y`. -/
def mw_σy : Matrix (Fin 2) (Fin 2) ℂ := !![0, -Complex.I; Complex.I, 0]
/-- The `σ_y = ±1` eigenspinors `χ± = (1, ±i)`. -/
def mw_χp : Fin 2 → ℂ := ![1, Complex.I]
def mw_χm : Fin 2 → ℂ := ![1, -Complex.I]

/-- **Row Z1.** `σ_y χ± = ±χ±`; `χ₊, χ₋` are independent; and `−mσ_y(fχ₊ + gχ₋) = (−mf)χ₊ + (mg)χ₋`, so the first-order
pair `ψ′ = −mσ_yψ` decouples into `f′ = −mf` and `g′ = mg`. -/
theorem mw_chirality (m : ℝ) (f g : ℂ) :
    Matrix.mulVec mw_σy mw_χp = mw_χp ∧ Matrix.mulVec mw_σy mw_χm = -mw_χm ∧
      (∀ a b : ℂ, a • mw_χp + b • mw_χm = 0 → a = 0 ∧ b = 0) ∧
      (-(m : ℂ)) • Matrix.mulVec mw_σy (f • mw_χp + g • mw_χm) = (-(m : ℂ) * f) • mw_χp + ((m : ℂ) * g) • mw_χm := by
  refine ⟨?_, ?_, fun a b h => ?_, ?_⟩
  · ext i; fin_cases i <;> simp [mw_σy, mw_χp, Matrix.mulVec, dotProduct, Fin.sum_univ_two]
  · ext i; fin_cases i <;> simp [mw_σy, mw_χm, Matrix.mulVec, dotProduct, Fin.sum_univ_two]
  · have h0 := congrFun h 0
    have h1 := congrFun h 1
    simp [mw_χp, mw_χm] at h0 h1
    have hab : a = b := by
      have : Complex.I * (a - b) = 0 := by linear_combination h1
      rcases mul_eq_zero.1 this with h | h
      · exact absurd h Complex.I_ne_zero
      · exact sub_eq_zero.1 h
    subst hab
    constructor <;> linear_combination h0 / 2
  · ext i; fin_cases i
    · simp [mw_σy, mw_χp, mw_χm]; linear_combination ((m : ℂ) * f - m * g) * Complex.I_sq
    · simp [mw_σy, mw_χp, mw_χm]; ring

/-! ## Row Z5: the paper's operator -/

/-- `f = 1 − 2M/r − r²/α²`. -/
noncomputable def mw_f (M α2 r : ℝ) : ℝ := 1 - 2 * M / r - r ^ 2 / α2

/-- **Row Z5.** For `f > 0` (cleared of the `r` denominator): the tortoise form `f ψ_r = (λ√f/r)ψ` and the frame form
`√f ψ_r = (λ/r)ψ` are the same equation, `ψ_r · r√f = λψ`, the one logarithmic derivative `λ/(r√f)`; `W = λ√f/r` is
odd under `(r, M) ↦ (−r, −M)` (`f` is even); and `W = 0` at a horizon `f = 0`. -/
theorem mw_operator {M α2 r lam D P : ℝ} :
    (0 < mw_f M α2 r →
      ((mw_f M α2 r * D * r = lam * Real.sqrt (mw_f M α2 r) * P ↔ D * (r * Real.sqrt (mw_f M α2 r)) = lam * P) ∧
        (Real.sqrt (mw_f M α2 r) * D * r = lam * P ↔ D * (r * Real.sqrt (mw_f M α2 r)) = lam * P))) ∧
      mw_f (-M) α2 (-r) = mw_f M α2 r ∧
      lam * Real.sqrt (mw_f (-M) α2 (-r)) / (-r) = -(lam * Real.sqrt (mw_f M α2 r) / r) ∧
      (mw_f M α2 r = 0 → lam * Real.sqrt (mw_f M α2 r) / r = 0) := by
  have heven : mw_f (-M) α2 (-r) = mw_f M α2 r := by
    unfold mw_f; field_simp
  refine ⟨fun hf => ?_, heven, by rw [heven, div_neg], fun h0 => by rw [h0]; simp⟩
  set s := Real.sqrt (mw_f M α2 r)
  have hs : 0 < s := Real.sqrt_pos.2 hf
  have hss : mw_f M α2 r = s ^ 2 := (Real.sq_sqrt hf.le).symm
  rw [hss]
  refine ⟨⟨fun h => ?_, fun h => by linear_combination s * h⟩, ⟨fun h => by linear_combination h,
    fun h => by linear_combination h⟩⟩
  have : s * (D * (r * s) - lam * P) = 0 := by linear_combination h
  rcases mul_eq_zero.1 this with h' | h'
  · exact absurd h' hs.ne'
  · linear_combination h'

/-! ## Non-vacuity -/

/-- **Witnesses.** At `a = 1` the bound mode `cosh^{−1}(x)` is `1` at the wall's centre, so nonzero, and normalizable;
`χ₊ ≠ 0`; `f = 0.35 > 0` at `M = 1`, `α² = 100`, `r = 5` (a static point, where Z5's equivalence applies); and `f = 0`
at `M = 1`, `α² = 27`, `r = 3`, the Nariai double horizon, where `W = 0`. -/
theorem mw_witness :
    Real.cosh (0 / 1) ^ (-(1 : ℝ)) = 1 ∧ Integrable (fun x : ℝ => (Real.cosh (x / 1) ^ (-(1 : ℝ))) ^ 2) ∧
      mw_χp ≠ 0 ∧ 0 < mw_f 1 100 5 ∧ mw_f 1 27 3 = 0 := by
  refine ⟨by simp, (mw_tanh one_pos).2.1, fun h => ?_, by norm_num [mw_f], by norm_num [mw_f]⟩
  have := congrFun h 0
  simp [mw_χp] at this

end ShadowProbe.MatterWallProbe

#print axioms ShadowProbe.MatterWallProbe.mw_unique_minus
#print axioms ShadowProbe.MatterWallProbe.mw_unique_plus
#print axioms ShadowProbe.MatterWallProbe.mw_F_lower
#print axioms ShadowProbe.MatterWallProbe.mw_exp_abs_integrable
#print axioms ShadowProbe.MatterWallProbe.mw_bound_integrable
#print axioms ShadowProbe.MatterWallProbe.mw_conj_not_integrable
#print axioms ShadowProbe.MatterWallProbe.mw_exactly_one
#print axioms ShadowProbe.MatterWallProbe.mw_flip
#print axioms ShadowProbe.MatterWallProbe.mw_tanh
#print axioms ShadowProbe.MatterWallProbe.mw_chirality
#print axioms ShadowProbe.MatterWallProbe.mw_operator
#print axioms ShadowProbe.MatterWallProbe.mw_witness

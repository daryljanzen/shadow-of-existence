import Mathlib

/-!
# The Nariai member of the horizon cubic

`r7263+71` · order ① of `FOR_71.md` §`r7263`, pre-registered in
`computations/formalisation/r7263_71_first_statements/PREDICTION.md`.

The corpus's horizon cubic, in the gauge `α = 1` and writing `m = 2M`, is `r³ − r + m`
(`f = 1 − 2M/r − r²/α²` cleared of its denominator, up to sign). Its Nariai member is the one
whose two positive roots merge: `m = 2/(3√3)`, with the double root at `r = 1/√3` and the
simple root at `r = −2/√3`.

What is stated here is algebra and nothing else. That the merged root is a horizon, that the
member is the one the collapse selects, and that `α` is the throat radius are the corpus's
readings of this algebra; none of them is stated, and nothing below is evidence for them
beyond the algebra itself.

* `N1` `discr_horizon`              — the discriminant is `4 − 27 m²`.
* `N2` `discr_horizon_eq_zero_iff`  — it vanishes exactly at `m = ±2/(3√3)`.
* `N3` `nariai_factorisation`       — `X³ − X + 2/(3√3) = (X − 1/√3)² (X + 2/√3)`.
* `N4` `nariai_double_root`         — `1/√3` is a root of multiplicity exactly `2`.
-/

open Polynomial

namespace ShadowFormal.Nariai

/-- The horizon cubic `r³ − r + m` as a `Cubic ℝ` (leading coefficient `1`, no `r²` term). -/
def horizon (m : ℝ) : Cubic ℝ := ⟨1, 0, -1, m⟩

/-- The Nariai value of `m = 2M` in the gauge `α = 1`. -/
noncomputable def mN : ℝ := 2 / (3 * Real.sqrt 3)

lemma sqrt3_sq : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)

lemma sqrt3_pos : 0 < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)

lemma mN_sq : mN ^ 2 = 4 / 27 := by
  unfold mN
  rw [div_pow, mul_pow, sqrt3_sq]
  norm_num

/-- **N1.** The discriminant of the horizon cubic, for every `m`. -/
theorem discr_horizon (m : ℝ) : (horizon m).discr = 4 - 27 * m ^ 2 := by
  simp only [Cubic.discr, horizon]
  ring

/-- **N2.** The discriminant vanishes exactly at the Nariai value and its mirror. -/
theorem discr_horizon_eq_zero_iff (m : ℝ) :
    (horizon m).discr = 0 ↔ m = mN ∨ m = -mN := by
  rw [discr_horizon, ← sq_eq_sq_iff_eq_or_eq_neg, mN_sq]
  constructor <;> intro h <;> linarith

/-- The general factorisation behind N3: a double root at `a` and a simple root at `−2a`. -/
lemma factor_general (a : ℝ) :
    (X - C a) ^ 2 * (X + C (2 * a)) = X ^ 3 - C (3 * a ^ 2) * X + C (2 * a ^ 3) := by
  simp only [map_mul, map_pow, map_ofNat]
  ring

/-- **N3.** The Nariai factorisation. -/
theorem nariai_factorisation :
    (X ^ 3 - X + C mN : ℝ[X]) =
      (X - C (1 / Real.sqrt 3)) ^ 2 * (X + C (2 / Real.sqrt 3)) := by
  have h2 : (2 / Real.sqrt 3 : ℝ) = 2 * (1 / Real.sqrt 3) := by ring
  have h3a : 3 * (1 / Real.sqrt 3) ^ 2 = (1 : ℝ) := by
    rw [div_pow, one_pow, sqrt3_sq]; norm_num
  have h2a : 2 * (1 / Real.sqrt 3) ^ 3 = mN := by
    unfold mN
    rw [div_pow, one_pow, pow_succ, sqrt3_sq]
    ring
  rw [h2, factor_general, h3a, h2a, map_one, one_mul]

/-- **N4.** `1/√3` is a root of multiplicity exactly two. -/
theorem nariai_double_root :
    (X ^ 3 - X + C mN : ℝ[X]).rootMultiplicity (1 / Real.sqrt 3) = 2 := by
  set a : ℝ := 1 / Real.sqrt 3 with ha_def
  have ha : a ≠ 0 := by rw [ha_def]; exact one_div_ne_zero sqrt3_pos.ne'
  have hlin : (X + C (2 / Real.sqrt 3) : ℝ[X]) = X - C (-(2 * a)) := by
    rw [ha_def, map_neg, sub_neg_eq_add]; congr 2; ring
  rw [nariai_factorisation, ← ha_def, hlin]
  have hne : (X - C a) ^ 2 * (X - C (-(2 * a))) ≠ (0 : ℝ[X]) :=
    mul_ne_zero (pow_ne_zero _ (X_sub_C_ne_zero a)) (X_sub_C_ne_zero _)
  rw [rootMultiplicity_mul hne, rootMultiplicity_X_sub_C_pow, rootMultiplicity_X_sub_C]
  have : a ≠ -(2 * a) := by intro h; apply ha; linarith
  simp [this]

end ShadowFormal.Nariai

import Mathlib

/-!
# Campaign 146: the exact statements of the P14, P15 and P16 cold reads (`r7841`)

The rows of `computations/formalisation/r7841_71_campaign146/PREDICTION.md`:
- F1 the crest discriminant (P14);
- F2 the throat and the collapse extremum at the Nariai mass, against the horizon radius (P16);
- F3 the regulated peak, `ρ = 1/(6πGt²)` with the mass cancelled, and `ρ_Pl/(6π)` at one Planck time (P16).
-/

namespace ShadowProbe.ColdReadsProbe

/-! ## F1: the crest discriminant -/

/-- **F1.** Under `2M = r₀ − r₀³`, the discriminant `−4(−1)³ − 27(2M)²` of the horizon cubic is
`(4 − 3r₀²)(3r₀² − 1)²`. -/
theorem cr_discriminant (r₀ : ℝ) :
    -4 * (-1) ^ 3 - 27 * (r₀ - r₀ ^ 3) ^ 2 = (4 - 3 * r₀ ^ 2) * (3 * r₀ ^ 2 - 1) ^ 2 := by
  ring

/-- At the crest `r₀ = 1/√3` the squared factor vanishes and `4 − 3r₀² = 3`. -/
theorem cr_crest :
    3 * (1 / Real.sqrt 3) ^ 2 - 1 = 0 ∧ 4 - 3 * (1 / Real.sqrt 3) ^ 2 = 3 ∧
      -4 * (-1) ^ 3 - 27 * ((1 / Real.sqrt 3) - (1 / Real.sqrt 3) ^ 3) ^ 2 = 0 := by
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hs : (1 / Real.sqrt 3) ^ 2 = 1 / 3 := by rw [div_pow, h3]; norm_num
  refine ⟨by rw [hs]; norm_num, by rw [hs]; norm_num, ?_⟩
  rw [cr_discriminant, hs]
  norm_num

/-! ## F2: the throat and the extremum at the Nariai mass -/

/-- **F2.** At `2M = 2α/(3√3)`, the throat `α/√3` is `3/2` of the horizon radius `2M`. -/
theorem cr_throat {α : ℝ} (hα : 0 < α) :
    α / Real.sqrt 3 = (3 / 2) * (2 * α / (3 * Real.sqrt 3)) := by
  have hs : 0 < Real.sqrt 3 := Real.sqrt_pos.2 (by norm_num)
  field_simp

/-- **F2.** The extremum ratio `y = (2Mα²)^{1/3}/(2M)` at `2M = 2α/(3√3)` has `y³ = 27/4`, so
`1.889 < y < 1.891`, and in particular `y > 1`. -/
theorem cr_extremum {α : ℝ} (hα : 0 < α) :
    let m := 2 * α / (3 * Real.sqrt 3)
    let y := (m * α ^ 2) ^ ((1 : ℝ) / 3) / m
    y ^ 3 = 27 / 4 ∧ 1.889 < y ∧ y < 1.891 ∧ 1 < y := by
  intro m y
  have hs3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hs : 0 < Real.sqrt 3 := Real.sqrt_pos.2 (by norm_num)
  have hm : 0 < m := by positivity
  have hma : 0 < m * α ^ 2 := by positivity
  have hcube : ((m * α ^ 2) ^ ((1 : ℝ) / 3)) ^ 3 = m * α ^ 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hma.le]; norm_num
  have hm2 : m ^ 2 * 27 = 4 * α ^ 2 := by
    simp only [m]; field_simp; rw [hs3]; ring
  have hy3 : y ^ 3 = 27 / 4 := by
    simp only [y]
    rw [div_pow, hcube]
    field_simp
    nlinarith [hm2]
  have hy0 : 0 ≤ y := by positivity
  have lo : (1.889 : ℝ) < y := by
    by_contra h
    have := pow_le_pow_left₀ hy0 (not_lt.mp h) 3
    norm_num at this; linarith
  have hi : y < 1.891 := by
    by_contra h
    have := pow_le_pow_left₀ (by norm_num) (not_lt.mp h) 3
    norm_num at this; linarith
  exact ⟨hy3, lo, hi, by linarith⟩

/-! ## F3: the regulated peak -/

/-- **F3.** For marginally bound free fall, `r³ = (9/2)GMt²`, the density `M/((4/3)πr³)` is
`1/(6πGt²)` whatever the mass. -/
theorem cr_peak {G M t : ℝ} (hG : 0 < G) (hM : 0 < M) (ht : 0 < t) :
    M / ((4 / 3) * Real.pi * ((9 / 2) * G * M * t ^ 2)) = 1 / (6 * Real.pi * G * t ^ 2) := by
  have hp := Real.pi_pos
  field_simp
  ring

/-- **F3.** At one Planck time, `t² = ħG/c⁵`, the peak is `ρ_Pl/(6π)` with `ρ_Pl = c⁵/(ħG²)`. -/
theorem cr_planck {G ħ c : ℝ} (hG : 0 < G) (hħ : 0 < ħ) (hc : 0 < c) :
    1 / (6 * Real.pi * G * (ħ * G / c ^ 5)) = (c ^ 5 / (ħ * G ^ 2)) / (6 * Real.pi) := by
  have hp := Real.pi_pos
  field_simp

end ShadowProbe.ColdReadsProbe

#print axioms ShadowProbe.ColdReadsProbe.cr_discriminant
#print axioms ShadowProbe.ColdReadsProbe.cr_crest
#print axioms ShadowProbe.ColdReadsProbe.cr_throat
#print axioms ShadowProbe.ColdReadsProbe.cr_extremum
#print axioms ShadowProbe.ColdReadsProbe.cr_peak
#print axioms ShadowProbe.ColdReadsProbe.cr_planck

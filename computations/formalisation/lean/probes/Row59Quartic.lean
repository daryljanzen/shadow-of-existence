import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Basic.Real.Basic

/-! # Row 59's pointwise identity (`r7337+71`): the algebraic quartic on a `3 × 3` matrix

`P10_the_algebraic_quartic_is_settled_by_the_frame_constant_level_…`, ⓐ: on a general `3 × 3` matrix,
`tr h⁴ − ½(tr h²)² = p₁ (⁴⁄₃ p₃ − p₁ p₂ + ⅙ p₁³)` with `pₖ = tr hᵏ`. It is an identity in the entries, so it holds
at every point of every field. On a pointwise-traceless `h` the quartic is `½ (tr h²)²`: rank one at every level.
No connection enters. The receipt's harmonics, integrals and ranks on `S³` are global, and are not here. -/

namespace ShadowProbe

open Matrix

/-- **The quartic identity**, for every `3 × 3` real matrix (symmetry is not needed). -/
theorem quartic_identity (h : Matrix (Fin 3) (Fin 3) ℝ) :
    trace (h ^ 4) - (trace (h ^ 2)) ^ 2 / 2
      = trace h * (4 / 3 * trace (h ^ 3) - trace h * trace (h ^ 2) + trace h ^ 3 / 6) := by
  simp only [pow_succ, pow_zero, one_mul, trace, diag, mul_apply, Fin.sum_univ_three]
  ring

/-- **On a traceless `h`, the algebraic quartic is `½ (tr h²)²`**: one invariant, at every point. -/
theorem quartic_traceless (h : Matrix (Fin 3) (Fin 3) ℝ) (h0 : trace h = 0) :
    trace (h ^ 4) = (trace (h ^ 2)) ^ 2 / 2 := by
  have := quartic_identity h
  rw [h0] at this
  rwa [zero_mul, sub_eq_zero] at this

end ShadowProbe

#print axioms ShadowProbe.quartic_identity
#print axioms ShadowProbe.quartic_traceless

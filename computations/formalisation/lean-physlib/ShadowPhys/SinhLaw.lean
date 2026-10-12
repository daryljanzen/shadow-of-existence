import Physlib.Cosmology.FLRW.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv

/-!
# The flat Λ + dust expansion law against Physlib's Friedmann equations

`r7265+71` · order ① of `FOR_71.md` §`r7265`, pre-registered in
`computations/formalisation/r7265_71_sinh_law/PREDICTION.md`.

The corpus's expansion history is the flat Λ + dust law

    a(t) = A · sinh^{2/3}( (3/2) · √(Λ/3) · c · t ),

with the density `ρ = (Λ c² / 8πG) · A³ / a³`. This file states that law against Physlib's own
`FirstOrderFriedmann` (L1) and `SecondOrderFriedmann` with `p = 0` (L2), imported from
`Physlib` at `b0e7ca1c`, not copied.

## What this does not state

`FirstOrderFriedmann` is the Einstein equations already reduced to a scale factor. The metric
it reduces is, in Physlib at this commit, `def FLRW : Type := sorry`. So the theorem this file
proves is the **coordinate shadow** of the geometric statement

> the flat FLRW metric `−c²dt² + a(t)² δ_ij dx^i dx^j`, with this `a`, solves Einstein's
> equations with cosmological constant `Λ` and a pressureless fluid of density `ρ`,

which needs a Lorentzian metric on a manifold, its Einstein tensor, and the reduction itself.
None of the three can be stated here, and none is claimed (`r7259+71.5` Ⓒ). The corpus's own
reading of the law — that the expansion is a property of the geometry and not of its content —
is a reading of this algebra, and nothing below is evidence for it beyond the algebra.
-/

open Real Time Cosmology.FLRW.FriedmannEquation

namespace ShadowPhys.SinhLaw

/-- The rate `ω = √(Λ/3) · c`. -/
noncomputable def rate (Λ c : ℝ) : ℝ := √(Λ / 3) * c

/-- The argument `x(t) = (3/2) ω t`. -/
noncomputable def arg (Λ c : ℝ) (t : ℝ) : ℝ := 3 / 2 * rate Λ c * t

/-- The scale factor `a(t) = A · sinh^{2/3}(x(t))`. -/
noncomputable def scale (A Λ c : ℝ) : Time → ℝ :=
  fun t => A * Real.sinh (arg Λ c t.val) ^ ((2 : ℝ) / 3)

/-- The dust density `ρ = (Λ c² / 8πG) · A³ / a³`. -/
noncomputable def density (A Λ G c : ℝ) : Time → ℝ :=
  fun t => Λ * c ^ 2 / (8 * Real.pi * G) * A ^ 3 / scale A Λ c t ^ 3

lemma rate_sq {Λ c : ℝ} (hΛ : 0 ≤ Λ) : rate Λ c ^ 2 = Λ * c ^ 2 / 3 := by
  unfold rate
  rw [mul_pow, Real.sq_sqrt (by positivity)]
  ring

lemma rate_pos {Λ c : ℝ} (hΛ : 0 < Λ) (hc : 0 < c) : 0 < rate Λ c := by
  unfold rate
  exact mul_pos (Real.sqrt_pos.mpr (by positivity)) hc

lemma sinh_arg_pos {Λ c : ℝ} (hΛ : 0 < Λ) (hc : 0 < c) {t : ℝ} (ht : 0 < t) :
    0 < Real.sinh (arg Λ c t) := by
  unfold arg
  exact Real.sinh_pos_iff.mpr (by have := rate_pos hΛ hc; positivity)

/-- `(sinh x ^ (2/3))³ = sinh² x` for `sinh x > 0`. -/
lemma rpow_cube {s : ℝ} (hs : 0 < s) : (s ^ ((2 : ℝ) / 3)) ^ 3 = s ^ 2 := by
  rw [← Real.rpow_natCast, ← Real.rpow_mul hs.le]
  norm_num

/-- The derivative of the scale factor, through Physlib's own bridge from `HasDerivAt` on `ℝ`. -/
lemma deriv_scale {A Λ c : ℝ} (hΛ : 0 < Λ) (hc : 0 < c) {t : Time} (ht : 0 < t.val) :
    ∂ₜ (scale A Λ c) t =
      A * (Real.cosh (arg Λ c t.val) * (3 / 2 * rate Λ c) * ((2 : ℝ) / 3) *
        (Real.sinh (arg Λ c t.val) ^ ((2 : ℝ) / 3) / Real.sinh (arg Λ c t.val))) := by
  have hs := sinh_arg_pos hΛ hc ht
  apply Time.deriv_eq_of_hasDerivAt
  have hx : HasDerivAt (fun y : ℝ => arg Λ c y) (3 / 2 * rate Λ c) t.val := by
    unfold arg
    simpa using (hasDerivAt_id t.val).const_mul (3 / 2 * rate Λ c)
  have h := ((hx.sinh).rpow_const (p := (2 : ℝ) / 3) (Or.inl hs.ne')).const_mul A
  rw [Real.rpow_sub_one hs.ne'] at h
  exact h

/-- **L1.** The law solves Physlib's first-order Friedmann equation, flat (`k = 0`), at every
`t > 0`. -/
theorem firstOrderFriedmann_scale {A Λ G c : ℝ} (hA : 0 < A) (hΛ : 0 < Λ) (hG : 0 < G)
    (hc : 0 < c) {t : Time} (ht : 0 < t.val) :
    FirstOrderFriedmann (scale A Λ c) (density A Λ G c) 0 Λ G c t := by
  unfold FirstOrderFriedmann
  rw [deriv_scale hΛ hc ht]
  have hs := sinh_arg_pos hΛ hc ht
  set s := Real.sinh (arg Λ c t.val) with hs_def
  set y := s ^ ((2 : ℝ) / 3) with hy_def
  have hy : 0 < y := Real.rpow_pos_of_pos hs _
  have hy3 : y ^ 3 = s ^ 2 := rpow_cube hs
  have hcosh : Real.cosh (arg Λ c t.val) ^ 2 = 1 + s ^ 2 := by
    rw [hs_def, Real.cosh_sq]; ring
  have hω := rate_sq (c := c) hΛ.le
  simp only [density, scale]
  rw [← hy_def, mul_pow, hy3]
  field_simp
  rw [hcosh, hω]
  ring

/-- The first derivative as a function of a real time, valid for `τ > 0`. -/
noncomputable def dscale (A Λ c : ℝ) (τ : ℝ) : ℝ :=
  A * (Real.cosh (arg Λ c τ) * (3 / 2 * rate Λ c) * ((2 : ℝ) / 3) *
    (Real.sinh (arg Λ c τ) ^ ((2 : ℝ) / 3) / Real.sinh (arg Λ c τ)))

/-- The second derivative, through `dscale`, which agrees with `∂ₜ scale` on the open set
`τ > 0`. -/
lemma deriv_deriv_scale {A Λ c : ℝ} (hΛ : 0 < Λ) (hc : 0 < c) {t : Time} (ht : 0 < t.val) :
    ∂ₜ (∂ₜ (scale A Λ c)) t =
      A * rate Λ c ^ 2 * Real.sinh (arg Λ c t.val) ^ ((2 : ℝ) / 3) *
        (1 - 1 / (2 * Real.sinh (arg Λ c t.val) ^ 2)) := by
  apply Time.deriv_eq_of_hasDerivAt
  -- `∂ₜ scale` agrees with `dscale` near `t.val`, because both are evaluated at `τ > 0`
  have hev : (fun τ : ℝ => ∂ₜ (scale A Λ c) ⟨τ⟩) =ᶠ[nhds t.val] dscale A Λ c := by
    filter_upwards [Ioi_mem_nhds ht] with τ hτ
    exact deriv_scale (t := ⟨τ⟩) hΛ hc hτ
  refine HasDerivAt.congr_of_eventuallyEq ?_ hev
  have hs := sinh_arg_pos hΛ hc ht
  set ω := rate Λ c with hω_def
  have hx : HasDerivAt (fun y : ℝ => arg Λ c y) (3 / 2 * ω) t.val := by
    unfold arg
    simpa using (hasDerivAt_id t.val).const_mul (3 / 2 * rate Λ c)
  have hsin := hx.sinh
  have hcos := hx.cosh
  have hpow := hsin.rpow_const (p := (2 : ℝ) / 3) (Or.inl hs.ne')
  have h := ((hcos.mul_const (3 / 2 * ω)).mul_const ((2 : ℝ) / 3)).mul
    (hpow.div hsin hs.ne')
  have h2 := h.const_mul A
  unfold dscale
  convert h2 using 1
  rw [Real.rpow_sub_one hs.ne']
  simp only [Pi.div_apply]
  set s := Real.sinh (arg Λ c t.val) with hs_def
  set y := s ^ ((2 : ℝ) / 3) with hy_def
  have hch : Real.cosh (arg Λ c t.val) ^ 2 = 1 + s ^ 2 := by
    rw [hs_def, Real.cosh_sq]; ring
  field_simp
  rw [hch]
  ring

/-- **L2.** The law solves Physlib's second-order Friedmann equation with `p = 0`, at every
`t > 0`. -/
theorem secondOrderFriedmann_scale {A Λ G c : ℝ} (hA : 0 < A) (hΛ : 0 < Λ) (hG : 0 < G)
    (hc : 0 < c) {t : Time} (ht : 0 < t.val) :
    SecondOrderFriedmann (scale A Λ c) (density A Λ G c) (fun _ => 0) Λ G c t := by
  unfold SecondOrderFriedmann
  rw [deriv_deriv_scale hΛ hc ht]
  have hs := sinh_arg_pos hΛ hc ht
  set s := Real.sinh (arg Λ c t.val) with hs_def
  set y := s ^ ((2 : ℝ) / 3) with hy_def
  have hy : 0 < y := Real.rpow_pos_of_pos hs _
  have hy3 : y ^ 3 = s ^ 2 := rpow_cube hs
  have hω := rate_sq (c := c) hΛ.le
  simp only [density, scale]
  rw [← hy_def, mul_pow, hy3, hω]
  field_simp
  ring

end ShadowPhys.SinhLaw

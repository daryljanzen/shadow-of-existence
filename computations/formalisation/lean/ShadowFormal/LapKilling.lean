import Mathlib
import ShadowFormal.Nariai

/-!
# The direction that orders the cosmic layer, and its norm along the lap

Pre-registered in `receipts/P07_CR_framework/LAP_killing_order.py` (the sympy receipt, which also
carries the Christoffel computation behind `K6`). Gauge `α = 1`, `m = 2M`, as in `Nariai.lean`:
`f(r) = 1 − m/r − r²`.

The proper-frame chart of the marginal (`E = 1`) comoving congruence is
`ds² = −dτ² + R'(τ+χ)² dχ² + R(τ+χ)² dΩ²`. Its components depend on `(τ, χ)` only through
`τ̃ = τ + χ`, and `K = ∂_χ − ∂_τ` is the direction in each layer `τ̃ = const` along which the
layer's comoving worldlines are ordered.

* `K1` `components_invariant`  — the flow of `K`, `(τ, χ) ↦ (τ − s, χ + s)`, leaves every
  component unchanged; `K` has constant components, so this is the statement that it is Killing.
* `K2` `normK_eq`               — `|K|² = R'² − 1`, and on the rate law `R'² = 1 − f(R)`, `|K|² = −f`.
* `K3` `sinh_law_rate`          — the law `R = m^{1/3} sinh^{2/3}(3τ̃/2)` satisfies `R'² = 1 − f(R)`
  for `τ̃ > 0`.
* `K4` `accel_of_rate`          — any twice-differentiable solution of `R'² = 1 − f(R)` with
  `R' ≠ 0` has `R'' = −f'(R)/2 = ½ d|K|²/dr`.
* `K5` the lap's loci on the Nariai member: `|K|² = 0` at both seams; `|K|² = −1` exactly where
  `r³ = −m` (the comoving turnaround); `|K|² = −2` exactly where `r³ + r + m = 0` (the Euclidean null).
* `K6` `kappa_back`, `kappa_front` — `f'/2` at the seams: `3√3/4` at the simple root, `0` at the
  double root. (That `∇_K K = κ K` on a seam layer with `κ = −R'' = f'/2` is the receipt's
  Christoffel computation; what is stated here is the value.)
* `K7` `normK_tendsto_left`, `normK_tendsto_right` — through the branch point `|K|²` runs to `−∞`
  from `r < 0` and returns from `+∞` on `r > 0`.

What is stated is calculus and algebra on these functions and nothing else. That `K` orders the
cosmic layer, that a null `K` makes the seam layer a metric singularity, and that the lap is a
collapse read on the cosmic clock are the corpus's readings of this algebra; none of them is
stated, and nothing below is evidence for them beyond the algebra itself.
-/

namespace ShadowFormal.LapKilling

open Real Filter Topology

/-- `f(r) = 1 − m/r − r²` in the gauge `α = 1`, `m = 2M`. -/
noncomputable def f (m r : ℝ) : ℝ := 1 - m / r - r ^ 2

/-- The norm of `K = ∂_χ − ∂_τ` in the proper-frame chart: `g_ττ + g_χχ = −1 + R'²`. -/
def normK (Rp : ℝ) : ℝ := -1 + Rp ^ 2

/-- **K1.** The flow of `K` leaves any component that depends on `(τ, χ)` only through `τ + χ`
unchanged. -/
theorem components_invariant (P : ℝ → ℝ) (τ χ s : ℝ) :
    P ((τ - s) + (χ + s)) = P (τ + χ) := by
  congr 1; ring

/-- **K2.** `|K|² = R'² − 1`, and on the rate law it is `−f`. -/
theorem normK_eq (m R Rp : ℝ) (hrate : Rp ^ 2 = 1 - f m R) : normK Rp = -f m R := by
  unfold normK; rw [hrate]; ring

/-- The rate law rewritten: `R'² = 1 + |K|²`. -/
theorem rate_eq_one_add_normK (Rp : ℝ) : Rp ^ 2 = 1 + normK Rp := by
  unfold normK; ring

/-! ### K3: the sinh law solves the rate law -/

/-- The law `R(t) = A · sinh^{2/3}(3t/2)`. -/
noncomputable def law (A t : ℝ) : ℝ := A * Real.sinh (3 / 2 * t) ^ ((2 : ℝ) / 3)

/-- Its derivative, `A · cosh(3t/2) · sinh^{−1/3}(3t/2)`. -/
noncomputable def lawDeriv (A t : ℝ) : ℝ := A * Real.cosh (3 / 2 * t) * Real.sinh (3 / 2 * t) ^ (-(1 : ℝ) / 3)

theorem hasDerivAt_law (A : ℝ) {t : ℝ} (ht : 0 < t) :
    HasDerivAt (law A) (lawDeriv A t) t := by
  have hs : 0 < Real.sinh (3 / 2 * t) := Real.sinh_pos_iff.mpr (by linarith)
  have h1 : HasDerivAt (fun y => 3 / 2 * y) (3 / 2) t := by
    simpa using (hasDerivAt_id t).const_mul (3 / 2 : ℝ)
  have h2 : HasDerivAt (fun y => Real.sinh (3 / 2 * y)) (Real.cosh (3 / 2 * t) * (3 / 2)) t :=
    (Real.hasDerivAt_sinh _).comp t h1
  have h3 := h2.rpow_const (p := (2 : ℝ) / 3) (Or.inl hs.ne')
  have h4 := h3.const_mul A
  unfold law lawDeriv
  convert h4 using 1
  have : (2 : ℝ) / 3 - 1 = -(1 : ℝ) / 3 := by norm_num
  rw [this]; ring

/-- **K3.** For `t > 0` and `A³ = m`, the law satisfies `R'² = 1 − f(R)`. -/
theorem sinh_law_rate {A m t : ℝ} (hA : 0 < A) (hm : A ^ 3 = m) (ht : 0 < t) :
    lawDeriv A t ^ 2 = 1 - f m (law A t) := by
  set s := Real.sinh (3 / 2 * t) with hs_def
  have hs : 0 < s := Real.sinh_pos_iff.mpr (by linarith)
  set u := s ^ ((1 : ℝ) / 3) with hu_def
  have hu : 0 < u := Real.rpow_pos_of_pos hs _
  have hu3 : u ^ 3 = s := by
    rw [hu_def, ← Real.rpow_natCast, ← Real.rpow_mul hs.le]; norm_num
  have h23 : s ^ ((2 : ℝ) / 3) = u ^ 2 := by
    rw [hu_def, ← Real.rpow_natCast, ← Real.rpow_mul hs.le]; norm_num
  have hm13 : s ^ (-(1 : ℝ) / 3) = u⁻¹ := by
    rw [hu_def, ← Real.rpow_neg_one, ← Real.rpow_mul hs.le]; norm_num
  have hc : Real.cosh (3 / 2 * t) ^ 2 = 1 + s ^ 2 := by
    rw [Real.cosh_sq, hs_def]; ring
  unfold lawDeriv law f
  rw [← hs_def, h23, hm13, ← hm]
  have hu0 : u ≠ 0 := hu.ne'
  have hA0 : A ≠ 0 := hA.ne'
  have hc' : Real.cosh (3 * t / 2) ^ 2 = 1 + u ^ 6 := by
    rw [show 3 * t / 2 = 3 / 2 * t by ring, hc, ← hu3]; ring
  field_simp
  rw [hc']
  ring

/-! ### K4: the acceleration is half the gradient of the norm -/

/-- **K4.** If `R' = v` and `v' = w` near `t`, `v ≠ 0`, and the rate law holds on a neighbourhood
of `t`, then `w = −f'(R)/2`, i.e. `R'' = ½ d|K|²/dr` since `|K|² = −f`. -/
theorem accel_of_rate {m : ℝ} {R v w : ℝ → ℝ} {t : ℝ}
    (hR : HasDerivAt R (v t) t) (hv : HasDerivAt v (w t) t) (hRt : R t ≠ 0) (hvt : v t ≠ 0)
    (hrate : ∀ᶠ y in 𝓝 t, v y ^ 2 = 1 - f m (R y)) :
    w t = (-(m / R t ^ 2 - 2 * R t)) / 2 := by
  -- derivative of the left side
  have hL : HasDerivAt (fun y => v y ^ 2) (2 * v t * w t) t := by
    have h := hv.pow 2
    have hfun : (fun y => v y ^ 2) = v ^ 2 := by funext y; simp
    rw [hfun]; convert h using 1; ring
  -- derivative of the right side: d/dy (m/R + R^2) = (2R - m/R^2) R'
  have hinv : HasDerivAt (fun y => (R y)⁻¹) (-(v t) / (R t) ^ 2) t := hR.inv hRt
  have hRHS : HasDerivAt (fun y => 1 - f m (R y)) ((2 * R t - m / R t ^ 2) * v t) t := by
    have hsq : HasDerivAt (fun y => R y ^ 2) (2 * R t * v t) t := by
      have h := hR.pow 2
      have hfun : (fun y => R y ^ 2) = R ^ 2 := by funext y; simp
      rw [hfun]; convert h using 1; ring
    have h1 := (hinv.const_mul m).add hsq
    have h2 : (fun y => 1 - f m (R y)) = fun y => m * (R y)⁻¹ + R y ^ 2 := by
      funext y; unfold f; rw [div_eq_mul_inv]; ring
    rw [h2]; convert h1 using 1; field_simp; ring
  have hL' : HasDerivAt (fun y => 1 - f m (R y)) (2 * v t * w t) t :=
    hL.congr_of_eventuallyEq (hrate.mono fun y hy => hy.symm)
  have heq := hL'.unique hRHS
  have key : v t * w t = v t * ((-(m / R t ^ 2 - 2 * R t)) / 2) := by
    linear_combination heq / 2
  exact mul_left_cancel₀ hvt key

/-! ### K5: the lap's loci -/

open ShadowFormal.Nariai in
/-- **K5a.** On the Nariai member `|K|² = −f = 0` at the simple root `−2/√3` (the back seam). -/
theorem normK_back_seam : f mN (-2 / Real.sqrt 3) = 0 := by
  have h3 := sqrt3_pos
  unfold f mN
  field_simp
  have : Real.sqrt 3 ^ 2 = 3 := sqrt3_sq
  nlinarith [this]

open ShadowFormal.Nariai in
/-- **K5b.** On the Nariai member `|K|² = −f = 0` at the double root `1/√3` (the front seam). -/
theorem normK_front_seam : f mN (1 / Real.sqrt 3) = 0 := by
  have h3 := sqrt3_pos
  unfold f mN
  field_simp
  have : Real.sqrt 3 ^ 2 = 3 := sqrt3_sq
  nlinarith [this]

/-- **K5c.** For `r ≠ 0`, `|K|² = −1` (that is, `f = 1`) exactly where `r³ = −m`: the comoving
turnaround. -/
theorem normK_eq_neg_one_iff {m r : ℝ} (hr : r ≠ 0) : f m r = 1 ↔ r ^ 3 = -m := by
  unfold f
  constructor
  · intro h
    have : m / r = -r ^ 2 := by linarith
    field_simp at this; linarith
  · intro h
    have : m / r = -r ^ 2 := by rw [div_eq_iff hr]; nlinarith
    linarith

/-- **K5d.** For `r ≠ 0`, `|K|² = −2` (that is, `f = 2`) exactly where `r³ + r + m = 0`: the
Euclidean null. -/
theorem normK_eq_neg_two_iff {m r : ℝ} (hr : r ≠ 0) : f m r = 2 ↔ r ^ 3 + r + m = 0 := by
  unfold f
  constructor
  · intro h
    have : m / r = -1 - r ^ 2 := by linarith
    rw [div_eq_iff hr] at this; nlinarith
  · intro h
    have : m / r = -1 - r ^ 2 := by rw [div_eq_iff hr]; nlinarith
    linarith

/-! ### K6: surface gravity at the seams -/

/-- `f'(r) = m/r² − 2r` for `r ≠ 0`. -/
theorem hasDerivAt_f (m : ℝ) {r : ℝ} (hr : r ≠ 0) :
    HasDerivAt (f m) (m / r ^ 2 - 2 * r) r := by
  have h1 : HasDerivAt (fun x : ℝ => m * x⁻¹) (m * (-(r ^ 2)⁻¹)) r :=
    (hasDerivAt_inv hr).const_mul m
  have h2 : HasDerivAt (fun x : ℝ => x ^ 2) (2 * r) r := by
    simpa using hasDerivAt_pow 2 r
  have h := ((hasDerivAt_const r (1 : ℝ)).sub h1).sub h2
  have hfun : f m = fun x => 1 - m * x⁻¹ - x ^ 2 := by
    funext x; unfold f; rw [div_eq_mul_inv]
  rw [hfun]; convert h using 1; field_simp; ring

open ShadowFormal.Nariai in
/-- **K6a.** At the back seam `f'/2 = 3√3/4`: the simple root's surface gravity. -/
theorem kappa_back : (mN / (-2 / Real.sqrt 3) ^ 2 - 2 * (-2 / Real.sqrt 3)) / 2 = 3 * Real.sqrt 3 / 4 := by
  have h3 := sqrt3_pos
  have hs : Real.sqrt 3 ^ 2 = 3 := sqrt3_sq
  unfold mN
  field_simp
  nlinarith [hs]

open ShadowFormal.Nariai in
/-- **K6b.** At the front seam `f'/2 = 0`: the double root carries no surface gravity. -/
theorem kappa_front : (mN / (1 / Real.sqrt 3) ^ 2 - 2 * (1 / Real.sqrt 3)) / 2 = 0 := by
  have h3 := sqrt3_pos
  have hs : Real.sqrt 3 ^ 2 = 3 := sqrt3_sq
  unfold mN
  field_simp
  nlinarith [hs]

/-! ### K7: through the branch point -/

/-- **K7a.** For `m > 0`, `|K|² = −f → −∞` as `r → 0⁻`. -/
theorem normK_tendsto_left {m : ℝ} (hm : 0 < m) :
    Tendsto (fun r => -f m r) (𝓝[<] 0) atBot := by
  have hinv : Tendsto (fun r : ℝ => r⁻¹) (𝓝[<] 0) atBot := tendsto_inv_nhdsLT_zero
  have hmul : Tendsto (fun r : ℝ => m * r⁻¹) (𝓝[<] 0) atBot := hinv.const_mul_atBot hm
  have hsq : Tendsto (fun r : ℝ => r ^ 2 - 1) (𝓝[<] 0) (𝓝 ((0 : ℝ) ^ 2 - 1)) :=
    ((continuous_pow 2).sub continuous_const).continuousAt.tendsto.mono_left nhdsWithin_le_nhds
  have := hmul.atBot_add hsq
  refine this.congr' (Eventually.of_forall fun r => ?_)
  show _ = -(1 - m / r - r ^ 2); rw [div_eq_mul_inv]; ring

/-- **K7b.** For `m > 0`, `|K|² = −f → +∞` as `r → 0⁺`. -/
theorem normK_tendsto_right {m : ℝ} (hm : 0 < m) :
    Tendsto (fun r => -f m r) (𝓝[>] 0) atTop := by
  have hinv : Tendsto (fun r : ℝ => r⁻¹) (𝓝[>] 0) atTop := tendsto_inv_nhdsGT_zero
  have hmul : Tendsto (fun r : ℝ => m * r⁻¹) (𝓝[>] 0) atTop := hinv.const_mul_atTop hm
  have hsq : Tendsto (fun r : ℝ => r ^ 2 - 1) (𝓝[>] 0) (𝓝 ((0 : ℝ) ^ 2 - 1)) :=
    ((continuous_pow 2).sub continuous_const).continuousAt.tendsto.mono_left nhdsWithin_le_nhds
  have := hmul.atTop_add hsq
  refine this.congr' (Eventually.of_forall fun r => ?_)
  show _ = -(1 - m / r - r ^ 2); rw [div_eq_mul_inv]; ring

end ShadowFormal.LapKilling

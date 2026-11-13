import Mathlib

/-!
# Probe `r7757+71.2` (campaign 137): P7's algebraic and complex rows

Registration: `computations/formalisation/r7757_71_campaign137/PREDICTION.md`; inventory
`computations/formalisation/r7755_71_survey/SURVEY.md`. Nothing imports this file, and it imports only Mathlib. It is
a new probe, prefix `fw_`, and later P7 campaigns append to it, so it is P7's citable file (`corpus/CR_framework.tex`).

`f(r) = 1 − 2M/r − r²/α²`; the de Sitter member is `M = 0`, the Nariai member `M = α/(3√3)`.

* **Row 3a — BUILT.** `fw_ef_inv`, `fw_dS_null`: in ingoing Eddington–Finkelstein form `g^{rr} = f`, so `r = α` is
  null for de Sitter.
* **Row 3b — BUILT.** `fw_horizons`: `f(α) = 0` (area `4πα²`); Nariai `f = f′ = 0` at `α/√3` (area `4πα²/3`).
* **Row 3c — BUILT.** `fw_surface_gravity`: `κ = 1/α` for de Sitter, `0` for Nariai.
* **Row 7a — BUILT.** `fw_nariai_roots`: the Nariai turning points `α/√3` (double) and `−2α/√3`.
* **Row 7b — BUILT.** `fw_turnaround`: at `r = −r₀`, `τ̃ = −iπα/3` solves the bead in `ℂ`, and `1 − f = 0` there.
* **Row 8a — BUILT.** `fw_one_sub_f`.
* **Row 8b — BUILT.** `fw_comoving_roots`, `fw_equilateral`.
* **Row 8c — BUILT.** `fw_three_real`.
* **Row 8d — BUILT.** `fw_affine_inequiv`.
* **Row 8e — BUILT.** `fw_rest_frame`.
* **Row 9 — BUILT.** `fw_action_odd`.

Campaign 138 (`r7759+71.1`, `computations/formalisation/r7759_71_campaign138/PREDICTION.md`) appends P7's last rows:
* **Row 1 — BUILT.** `fw_rs_tendsto`, `fw_no_intersection`, `fw_timelike_slope`: in chart form (Schwarzschild
  exterior). P2's manifold-level `sr_future_diverges` is not copied.
* **Row 3d — BUILT.** `fw_H`, `fw_H_null`, `fw_horizon_inj`: in `ℝ^{1,4}`. Surjectivity onto "the oriented future
  horizons" stays interpretive.
* **Row 6 — BUILT.** `fw_sinh23`.
* **Row 7c — BUILT.** `fw_τ_bead`, `fw_τ_bound`, `fw_τ_cont`: an explicit continuous `τ̃` on `(−∞, 0]`.
* Witnesses: `fw_witness`, `fw_witness2`.
-/

open Real

namespace ShadowProbe.FrameworkProbe

/-- `f(r) = 1 − 2M/r − r²/α²`. -/
noncomputable def fw_f (M α r : ℝ) : ℝ := 1 - 2 * M / r - r ^ 2 / α ^ 2

/-- `f′(r) = 2M/r² − 2r/α²`. -/
noncomputable def fw_f1 (M α r : ℝ) : ℝ := 2 * M / r ^ 2 - 2 * r / α ^ 2

lemma fw_hasDeriv_f (M α : ℝ) {r : ℝ} (hr : r ≠ 0) : HasDerivAt (fw_f M α) (fw_f1 M α r) r := by
  have h := ((hasDerivAt_const r (1 : ℝ)).sub ((hasDerivAt_inv hr).const_mul (2 * M))).sub
    (((hasDerivAt_id' r).fun_pow 2).div_const (α ^ 2))
  have e : fw_f M α = fun x => 1 - 2 * M * x⁻¹ - x ^ 2 / α ^ 2 := by
    funext x; simp [fw_f, div_eq_mul_inv]
  rw [e]
  refine h.congr_deriv ?_
  simp only [fw_f1]
  field_simp
  ring

/-! ## Row 3: the horizons of `thm:null-boundary` -/

/-- Ingoing Eddington–Finkelstein form `−f dv² + 2 dv dr + r²(dθ² + sin²θ dφ²)` on `(v, r, θ, φ)`. -/
noncomputable def fw_ef (M α : ℝ) (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![-fw_f M α (y 1), 1, 0, 0; 1, 0, 0, 0; 0, 0, y 1 ^ 2, 0; 0, 0, 0, y 1 ^ 2 * Real.sin (y 2) ^ 2]

/-- **The inverse is regular wherever `r, sin θ ≠ 0`, including on the horizon**, and `g^{rr} = f`. -/
lemma fw_ef_inv (M α : ℝ) {y : Fin 4 → ℝ} (hr : y 1 ≠ 0) (hs : Real.sin (y 2) ≠ 0) :
    (fw_ef M α y)⁻¹ = !![0, 1, 0, 0; 1, fw_f M α (y 1), 0, 0; 0, 0, 1 / y 1 ^ 2, 0;
      0, 0, 0, 1 / (y 1 ^ 2 * Real.sin (y 2) ^ 2)] := by
  refine Matrix.inv_eq_left_inv ?_
  ext i j
  fin_cases i <;> fin_cases j <;> simp [fw_ef, Matrix.mul_apply, Fin.sum_univ_four] <;> field_simp

/-- **Row 3a.** For de Sitter (`M = 0`) the hypersurface `r = α` is null: its normal `dr` has
`g^{-1}(dr, dr) = g^{rr} = f(α) = 0`, in a chart regular there. -/
theorem fw_dS_null {α : ℝ} (hα : 0 < α) {y : Fin 4 → ℝ} (hr : y 1 = α) (hs : Real.sin (y 2) ≠ 0) :
    (fw_ef 0 α y)⁻¹ 1 1 = 0 := by
  rw [fw_ef_inv 0 α (by rw [hr]; exact hα.ne') hs]
  simp [fw_f, hr, hα.ne']

/-- The Nariai mass `α/(3√3)`. -/
noncomputable def fw_MN (α : ℝ) : ℝ := α / (3 * Real.sqrt 3)

lemma fw_s3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
lemma fw_s3_pos : 0 < Real.sqrt 3 := Real.sqrt_pos.2 (by norm_num)

/-- **Row 3b.** The de Sitter horizon `r = α` (area `4πα²`); the Nariai double root `α/√3` (both positive roots
coincide: `f = f′ = 0`), area `4π(α/√3)² = 4πα²/3`. -/
theorem fw_horizons {α : ℝ} (hα : 0 < α) :
    fw_f 0 α α = 0 ∧ fw_f (fw_MN α) α (α / Real.sqrt 3) = 0 ∧ fw_f1 (fw_MN α) α (α / Real.sqrt 3) = 0 ∧
      4 * π * (α / Real.sqrt 3) ^ 2 = 4 * π * α ^ 2 / 3 := by
  have s := fw_s3; have sp := fw_s3_pos; have ha := hα.ne'
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp [fw_f, ha]
  · simp only [fw_f, fw_MN]; field_simp; nlinarith [s]
  · simp only [fw_f1, fw_MN]; field_simp; nlinarith [s]
  · field_simp; rw [s]

/-- **Row 3c.** Surface gravities `κ = |f′(r_h)|/2`: `1/α ≠ 0` for de Sitter, `0` for the degenerate Nariai horizon. -/
theorem fw_surface_gravity {α : ℝ} (hα : 0 < α) :
    |fw_f1 0 α α| / 2 = 1 / α ∧ 1 / α ≠ 0 ∧ |fw_f1 (fw_MN α) α (α / Real.sqrt 3)| / 2 = 0 := by
  refine ⟨?_, by positivity, ?_⟩
  · have : fw_f1 0 α α = -(2 / α) := by simp only [fw_f1]; field_simp; ring
    rw [this, abs_neg, abs_of_pos (by positivity)]; ring
  · rw [(fw_horizons hα).2.2.1]; simp

/-! ## Row 7: the bead's turning points and turnaround -/

/-- **Row 7a.** The Nariai member's turning points: for `r ≠ 0`, `f(r) = 0` exactly at `α/√3` (the double root)
and `−2α/√3`, since `r³ − α²r + 2Mα² = (r − α/√3)²(r + 2α/√3)`. -/
theorem fw_nariai_roots {α : ℝ} (hα : 0 < α) {r : ℝ} (hr : r ≠ 0) :
    fw_f (fw_MN α) α r = 0 ↔ r = α / Real.sqrt 3 ∨ r = -2 * α / Real.sqrt 3 := by
  have s := fw_s3; have sp := fw_s3_pos; have ha := hα.ne'
  have key : fw_f (fw_MN α) α r = -((r - α / Real.sqrt 3) ^ 2 * (r + 2 * α / Real.sqrt 3)) / (r * α ^ 2) := by
    simp only [fw_f, fw_MN]
    field_simp
    linear_combination (3 * Real.sqrt 3 * α ^ 2 * r - 2 * α ^ 3) * s
  rw [key, div_eq_zero_iff, neg_eq_zero, mul_eq_zero, pow_eq_zero_iff two_ne_zero]
  constructor
  · rintro ((h | h) | h)
    · left; linarith
    · right; field_simp; linarith [show r * Real.sqrt 3 + 2 * α = 0 by field_simp at h; linarith]
    · exact absurd h (mul_ne_zero hr (pow_ne_zero 2 ha))
  · rintro (h | h)
    · left; left; rw [h]; ring
    · left; right; rw [h]; ring

/-- **Row 7b.** The comoving turnaround: with `r₀ > 0`, `r₀³ = 2Mα²`, at `r = −r₀` the complex cosmic time
`τ̃ = −iπα/3` satisfies the bead `r³ = 2Mα² sinh²(3τ̃/2α)`, and `1 − f(−r₀) = 0` (the comoving turning). -/
theorem fw_turnaround {M α r₀ : ℝ} (hα : α ≠ 0) (h0 : 0 < r₀) (h3 : r₀ ^ 3 = 2 * M * α ^ 2) :
    ((-r₀ : ℝ) : ℂ) ^ 3 =
        2 * M * α ^ 2 * Complex.sinh (3 * (-(π * α / 3) * Complex.I) / (2 * α)) ^ 2 ∧
      1 - fw_f M α (-r₀) = 0 := by
  constructor
  · have hαc : (α : ℂ) ≠ 0 := Complex.ofReal_ne_zero.2 hα
    have harg : (3 * (-(↑π * ↑α / 3) * Complex.I) / (2 * ↑α) : ℂ) = ((-(π / 2) : ℝ) : ℂ) * Complex.I := by
      field_simp; push_cast; ring
    rw [harg, Complex.sinh_mul_I, ← Complex.ofReal_sin, Real.sin_neg, Real.sin_pi_div_two]
    have h3c : ((r₀ : ℂ)) ^ 3 = 2 * M * α ^ 2 := by exact_mod_cast h3
    push_cast
    linear_combination (-1 : ℂ) * h3c + (-2 * (M : ℂ) * α ^ 2) * Complex.I_sq
  · simp only [fw_f]
    field_simp
    linarith [h3]

/-! ## Row 8: the two turnings, `lem:twoturnings` -/

/-- **Row 8a.** `1 − f = 2M/r + r²/α²`, so the comoving turning `f = 1` is `r³ = −2Mα²`. -/
theorem fw_one_sub_f (M α : ℝ) {r : ℝ} (hr : r ≠ 0) (hα : α ≠ 0) :
    1 - fw_f M α r = 2 * M / r + r ^ 2 / α ^ 2 ∧ (fw_f M α r = 1 ↔ r ^ 3 = -2 * M * α ^ 2) := by
  refine ⟨by simp only [fw_f]; ring, ?_⟩
  simp only [fw_f]
  constructor
  · intro h; field_simp at h; linarith
  · intro h; field_simp; linarith

/-- The primitive cube root of unity `ω = −½ + i√3/2`. -/
noncomputable def fw_ω : ℂ := ⟨-1 / 2, Real.sqrt 3 / 2⟩

lemma fw_ω_sq : fw_ω ^ 2 = -1 - fw_ω := by
  apply Complex.ext <;> simp [fw_ω, sq] <;> nlinarith [fw_s3]

lemma fw_ω_cube : fw_ω ^ 3 = 1 := by
  rw [pow_succ, fw_ω_sq]
  apply Complex.ext <;> simp [fw_ω] <;> nlinarith [fw_s3]

/-- **Row 8b.** The comoving turning roots (`α = 1`): with `c > 0`, `c³ = 2M`, the roots of `z³ + 2M` are exactly
`−c`, `−cω` and `−cω²`, and multiplication by `ω` permutes the root set. -/
theorem fw_comoving_roots {M c : ℝ} (hc : c ^ 3 = 2 * M) (z : ℂ) :
    (z ^ 3 + 2 * M = 0 ↔ z = -c ∨ z = -c * fw_ω ∨ z = -c * fw_ω ^ 2) ∧
      (z ^ 3 + 2 * M = 0 → (fw_ω * z) ^ 3 + 2 * M = 0) := by
  have hcc : (c : ℂ) ^ 3 = 2 * M := by exact_mod_cast hc
  have w2 := fw_ω_sq
  have fac : z ^ 3 + 2 * M = (z + c) * (z + c * fw_ω) * (z + c * fw_ω ^ 2) := by
    linear_combination (-1 : ℂ) * hcc - ((c : ℂ) * z ^ 2 + (c : ℂ) ^ 2 * fw_ω * z) * w2 - (c : ℂ) ^ 3 * fw_ω_cube
  refine ⟨?_, fun h => by rw [mul_pow, fw_ω_cube, one_mul]; exact h⟩
  rw [fac, mul_eq_zero, mul_eq_zero]
  constructor
  · rintro ((h | h) | h)
    · left; linear_combination h
    · right; left; linear_combination h
    · right; right; linear_combination h
  · rintro (h | h | h)
    · left; left; rw [h]; ring
    · left; right; rw [h]; ring
    · right; rw [h]; ring

/-- **Row 8b.** The comoving roots form an equilateral triangle: the three pairwise squared distances are all
`3c²` (so the roots are pairwise distinct). -/
theorem fw_equilateral {c : ℝ} (hc : 0 < c) :
    Complex.normSq (-(c : ℂ) - -c * fw_ω) = 3 * c ^ 2 ∧
      Complex.normSq (-(c : ℂ) * fw_ω - -c * fw_ω ^ 2) = 3 * c ^ 2 ∧
      Complex.normSq (-(c : ℂ) - -c * fw_ω ^ 2) = 3 * c ^ 2 ∧ 0 < 3 * c ^ 2 := by
  have s := fw_s3
  rw [fw_ω_sq]
  refine ⟨?_, ?_, ?_, by positivity⟩ <;>
    simp [Complex.normSq_apply, fw_ω] <;> ring_nf <;> first | (rw [s]; ring) | rw [s]

/-- **Row 8c.** For `0 < M < 1/(3√3)` the horizon cubic (`α = 1`) `r³ − r + 2M` has three distinct real roots, one
in each of `(−2, −1/√3)`, `(−1/√3, 1/√3)` and `(1/√3, 1)` (the casus irreducibilis). -/
theorem fw_three_real {M : ℝ} (h0 : 0 < M) (h1 : M < 1 / (3 * Real.sqrt 3)) :
    ∃ x₁ x₂ x₃ : ℝ, x₁ < x₂ ∧ x₂ < x₃ ∧ x₁ ^ 3 - x₁ + 2 * M = 0 ∧ x₂ ^ 3 - x₂ + 2 * M = 0 ∧
      x₃ ^ 3 - x₃ + 2 * M = 0 := by
  have s := fw_s3; have sp := fw_s3_pos
  set u := Real.sqrt 3 / 3 with hu
  have u2 : u ^ 2 = 1 / 3 := by rw [hu, div_pow, s]; norm_num
  have up : 0 < u := by positivity
  have u1 : u < 1 := by nlinarith
  have hM : M < u / 3 := by
    have : 1 / (3 * Real.sqrt 3) = u / 3 := by rw [hu]; field_simp; rw [s]
    linarith
  let p : ℝ → ℝ := fun x => x ^ 3 - x + 2 * M
  have pc : Continuous p := by fun_prop
  have pm2 : p (-2) < 0 := by simp only [p]; nlinarith
  have pmu : 0 < p (-u) := by simp only [p]; nlinarith
  have pu : p u < 0 := by simp only [p]; nlinarith
  have p1 : 0 < p 1 := by simp only [p]; nlinarith
  obtain ⟨x₁, ⟨a1, b1⟩, e1⟩ := intermediate_value_Ioo (show (-2 : ℝ) ≤ -u by linarith) pc.continuousOn ⟨pm2, pmu⟩
  obtain ⟨x₂, ⟨a2, b2⟩, e2⟩ := intermediate_value_Ioo' (show -u ≤ u by linarith) pc.continuousOn ⟨pu, pmu⟩
  obtain ⟨x₃, ⟨a3, b3⟩, e3⟩ := intermediate_value_Ioo (show u ≤ 1 by linarith) pc.continuousOn ⟨pu, p1⟩
  exact ⟨x₁, x₂, x₃, by linarith, by linarith, e1, e2, e3⟩

/-- **Row 8d.** The two turning configurations are affinely inequivalent: no `z ↦ az + b` carries three real numbers
onto the comoving triangle `{−c, −cω, −cω²}`. A real affine image has real ratios `(w₂ − w₁)/(w₃ − w₁)`; the
triangle's is `½ − (√3/2)i`. -/
theorem fw_affine_inequiv {c : ℝ} (hc : 0 < c) (x₁ x₂ x₃ : ℝ) (a b : ℂ) :
    (fun x : ℝ => a * x + b) '' {x₁, x₂, x₃} ≠ {-(c : ℂ), -c * fw_ω, -c * fw_ω ^ 2} := by
  intro h
  have m : ∀ w ∈ ({-(c : ℂ), -c * fw_ω, -c * fw_ω ^ 2} : Set ℂ), ∃ x : ℝ, a * x + b = w := by
    intro w hw; rw [← h] at hw; obtain ⟨x, -, hx⟩ := hw; exact ⟨x, hx⟩
  obtain ⟨p, hp⟩ := m (-(c : ℂ)) (by simp)
  obtain ⟨q, hq⟩ := m (-c * fw_ω) (by simp)
  obtain ⟨r, hr⟩ := m (-c * fw_ω ^ 2) (by simp)
  have s := fw_s3; have sp := fw_s3_pos
  have key : (-(c : ℂ) * fw_ω - -c) * ((r : ℂ) - p) = (-(c : ℂ) * fw_ω ^ 2 - -c) * ((q : ℂ) - p) := by
    linear_combination (-((r : ℂ) - p)) * hq + ((r : ℂ) - p) * hp + ((q : ℂ) - p) * hr - ((q : ℂ) - p) * hp
  rw [fw_ω_sq] at key
  have re := congrArg Complex.re key
  have im := congrArg Complex.im key
  simp [fw_ω] at re im
  have hq0 : q - p = 0 := by nlinarith [mul_pos hc sp]
  have hr0 : r - p = 0 := by nlinarith [mul_pos hc sp]
  have e : -(c : ℂ) * fw_ω = -c := by
    calc -(c : ℂ) * fw_ω = a * q + b := hq.symm
      _ = a * p + b := by rw [show q = p by linarith]
      _ = -c := hp
  have := congrArg Complex.im e
  simp [fw_ω] at this
  linarith

/-- **Row 8e.** At the rest-frame locus `f = 1`: `dt/dτ = E/f = 1` exactly when `E = 1`, and the comoving radial
equation `(dr/dτ)² = E² − f` reads `1 − f` exactly when `E² = 1`. -/
theorem fw_rest_frame (E f : ℝ) (hf : f = 1) : (E / f = 1 ↔ E = 1) ∧ (E ^ 2 - f = 1 - f ↔ E ^ 2 = 1) := by
  subst hf; constructor
  · simp
  · constructor <;> intro h <;> linarith

/-! ## Row 9: `thm:antimatter-progenitor`'s action integrand -/

/-- **Row 9.** `r(f − 1) = −2M − r³/α²`, odd under the mass-reflection `R: (r, M) ↦ (−r, −M)`. -/
theorem fw_action_odd (M α : ℝ) {r : ℝ} (hr : r ≠ 0) :
    r * (fw_f M α r - 1) = -2 * M - r ^ 3 / α ^ 2 ∧
      -r * (fw_f (-M) α (-r) - 1) = -(r * (fw_f M α r - 1)) := by
  have hr' : -r ≠ 0 := neg_ne_zero.2 hr
  constructor
  · simp only [fw_f]; field_simp; ring
  · simp only [fw_f]; field_simp

/-! ## Non-vacuity -/

/-- **Witnesses.** `α = 1`: de Sitter's horizon is null at `r = 1`; `M = ½`, `α = 1`, `r₀ = 1`: the turnaround;
`M = 1/10` has three real horizon roots; `c = 1` gives the comoving triangle. -/
theorem fw_witness :
    (fw_ef 0 1 ![0, 1, π / 2, 0])⁻¹ 1 1 = 0 ∧
      ((-1 : ℝ) : ℂ) ^ 3 = 2 * (1 / 2 : ℝ) * (1 : ℝ) ^ 2 *
        Complex.sinh (3 * (-(π * (1 : ℝ) / 3) * Complex.I) / (2 * (1 : ℝ))) ^ 2 ∧
      (∃ x₁ x₂ x₃ : ℝ, x₁ < x₂ ∧ x₂ < x₃ ∧ x₁ ^ 3 - x₁ + 2 * (1 / 10) = 0 ∧ x₂ ^ 3 - x₂ + 2 * (1 / 10) = 0 ∧
        x₃ ^ 3 - x₃ + 2 * (1 / 10) = 0) ∧
      Complex.normSq (-((1 : ℝ) : ℂ) - -(1 : ℝ) * fw_ω) = 3 * 1 ^ 2 := by
  have s := fw_s3; have sp := fw_s3_pos
  refine ⟨fw_dS_null one_pos (by simp) (by simp), (fw_turnaround one_ne_zero one_pos (by norm_num)).1,
    fw_three_real (by norm_num) ?_, (fw_equilateral one_pos).1⟩
  rw [div_lt_div_iff₀ (by norm_num) (by positivity)]
  nlinarith


/-! ## Row 1: asymptotic non-intersection (Schwarzschild exterior, chart form) -/

open Filter Topology Set

/-- The tortoise coordinate `r* = r + 2M log(r/2M − 1)` on `r > 2M`. -/
noncomputable def fw_rs (M r : ℝ) : ℝ := r + 2 * M * Real.log (r / (2 * M) - 1)

lemma fw_rs_deriv {M r : ℝ} (hM : 0 < M) (hr : 2 * M < r) :
    HasDerivAt (fw_rs M) (1 / (1 - 2 * M / r)) r := by
  have hpos : 0 < r / (2 * M) - 1 := by rw [sub_pos, one_lt_div (by positivity)]; exact hr
  have h := (hasDerivAt_id' r).add ((((hasDerivAt_id' r).div_const (2 * M)).sub_const 1).log hpos.ne'
    |>.const_mul (2 * M))
  refine h.congr_deriv ?_
  have h2 : r - 2 * M ≠ 0 := by linarith
  have hr0 : r ≠ 0 := by linarith
  field_simp
  ring

/-- `r* → −∞` at the horizon. -/
theorem fw_rs_tendsto {M : ℝ} (hM : 0 < M) : Tendsto (fw_rs M) (𝓝[>] (2 * M)) atBot := by
  have h1 : Tendsto (fun r : ℝ => r / (2 * M) - 1) (𝓝[>] (2 * M)) (𝓝[>] 0) := by
    refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
    · have : Tendsto (fun r : ℝ => r / (2 * M) - 1) (𝓝 (2 * M)) (𝓝 (2 * M / (2 * M) - 1)) :=
        ((continuous_id.div_const _).sub continuous_const).tendsto _
      rw [div_self (by positivity), sub_self] at this
      exact this.mono_left nhdsWithin_le_nhds
    · filter_upwards [self_mem_nhdsWithin] with r hr
      rw [mem_Ioi, sub_pos, one_lt_div (by positivity)]; exact hr
  have h2 := (Real.tendsto_log_nhdsGT_zero.comp h1).const_mul_atBot (by positivity : 0 < 2 * M)
  have h3 : Tendsto (fun r : ℝ => r) (𝓝[>] (2 * M)) (𝓝 (2 * M)) := tendsto_nhdsWithin_of_tendsto_nhds tendsto_id
  exact h3.add_atBot h2

/-- **Row 1.** No finite exterior time reaches the horizon: every path `r ↦ t(r)` on `(2M, r₀)` whose slope obeys
`dt/dr ≤ −k/f` (`k > 0`, `f = 1 − 2M/r`) has `t → +∞` as `r → 2M⁺`. -/
theorem fw_no_intersection {M r₀ k : ℝ} (hM : 0 < M) (h0 : 2 * M < r₀) (hk : 0 < k) {t t' : ℝ → ℝ}
    (ht : ∀ r ∈ Ioo (2 * M) r₀, HasDerivAt t (t' r) r)
    (hs : ∀ r ∈ Ioo (2 * M) r₀, t' r ≤ -k / (1 - 2 * M / r)) :
    Tendsto t (𝓝[>] (2 * M)) atTop := by
  set g : ℝ → ℝ := fun r => t r + k * fw_rs M r
  have hg : ∀ r ∈ Ioo (2 * M) r₀, HasDerivAt g (t' r + k * (1 / (1 - 2 * M / r))) r :=
    fun r hr => (ht r hr).add ((fw_rs_deriv hM hr.1).const_mul k)
  have anti : AntitoneOn g (Ioo (2 * M) r₀) := by
    refine antitoneOn_of_deriv_nonpos (convex_Ioo _ _) (fun r hr => (hg r hr).continuousAt.continuousWithinAt)
      (fun r hr => (hg r (by rwa [interior_Ioo] at hr)).differentiableAt.differentiableWithinAt) ?_
    intro r hr
    rw [interior_Ioo] at hr
    rw [(hg r hr).deriv]
    have := hs r hr
    have e : -k / (1 - 2 * M / r) = -(k * (1 / (1 - 2 * M / r))) := by ring
    linarith
  set r₁ := (2 * M + r₀) / 2
  have hr₁ : r₁ ∈ Ioo (2 * M) r₀ := ⟨by simp only [r₁]; linarith, by simp only [r₁]; linarith⟩
  have low : ∀ᶠ r in 𝓝[>] (2 * M), g r₁ - k * fw_rs M r ≤ t r := by
    filter_upwards [Ioo_mem_nhdsGT hr₁.1] with r hr
    have := anti ⟨hr.1, hr.2.trans hr₁.2⟩ hr₁ hr.2.le
    simp only [g] at this ⊢; linarith
  have h1 : Tendsto (fun r => k * -(fw_rs M r)) (𝓝[>] (2 * M)) atTop :=
    (tendsto_neg_atBot_atTop.comp (fw_rs_tendsto hM)).const_mul_atTop hk
  have h2 := tendsto_atTop_add_const_left _ (g r₁) h1
  exact tendsto_atTop_mono' _ low (h2.congr fun r => by ring)

/-- Every radial timelike geodesic (`dt/dτ = E/f`, `dr/dτ = −√(E² − f)`) has slope `dt/dr ≤ −1/f`, so
`fw_no_intersection` applies with `k = 1` (ingoing null rays have slope exactly `−1/f`). -/
theorem fw_timelike_slope {E f : ℝ} (hf : 0 < f) (hE : 0 < E) (hfE : f < E ^ 2) :
    -(E / f) / Real.sqrt (E ^ 2 - f) ≤ -1 / f := by
  have hs : 0 < Real.sqrt (E ^ 2 - f) := Real.sqrt_pos.2 (by linarith)
  have hle : Real.sqrt (E ^ 2 - f) ≤ E := by
    rw [Real.sqrt_le_left hE.le]; linarith
  rw [neg_div, neg_div, neg_le_neg_iff, div_div, div_le_div_iff₀ hf (mul_pos hf hs)]
  nlinarith

/-! ## Row 6: the `sinh^{2/3}` law (corollary to `thm:null-boundary`) -/

/-- `r(τ̃) = A sinh^{2/3}(3τ̃/2α)` with `A³ = 2Mα²`. -/
noncomputable def fw_rC (A α τ : ℝ) : ℝ := A * Real.sinh (3 * τ / (2 * α)) ^ (2 / 3 : ℝ)

/-- **Row 6.** `r = A sinh^{2/3}(3τ̃/2α)` solves the bead `r³ = 2Mα² sinh²(3τ̃/2α)` and, for `τ̃ > 0`, the comoving
law `(dr/dτ̃)² = 2M/r + r²/α²`. -/
theorem fw_sinh23 {M α A τ : ℝ} (hα : 0 < α) (hA : 0 < A) (hA3 : A ^ 3 = 2 * M * α ^ 2) (hτ : 0 < τ) :
    fw_rC A α τ ^ 3 = 2 * M * α ^ 2 * Real.sinh (3 * τ / (2 * α)) ^ 2 ∧
      ∃ r' : ℝ, HasDerivAt (fw_rC A α) r' τ ∧
        r' ^ 2 = 2 * M / fw_rC A α τ + fw_rC A α τ ^ 2 / α ^ 2 := by
  set u := 3 * τ / (2 * α) with hu
  have hs : 0 < Real.sinh u := Real.sinh_pos_iff.2 (by rw [hu]; positivity)
  set x := Real.sinh u ^ ((1 : ℝ) / 3) with hxdef
  have hx : 0 < x := Real.rpow_pos_of_pos hs _
  have e2 : Real.sinh u ^ (2 / 3 : ℝ) = x ^ 2 := by
    rw [hxdef, ← Real.rpow_natCast, ← Real.rpow_mul hs.le]; norm_num
  have e1 : Real.sinh u ^ ((2 / 3 : ℝ) - 1) = x⁻¹ := by
    rw [hxdef, ← Real.rpow_neg_one, ← Real.rpow_mul hs.le]; norm_num
  have e3 : Real.sinh u = x ^ 3 := by
    rw [hxdef, ← Real.rpow_natCast, ← Real.rpow_mul hs.le]; norm_num
  have cs := Real.cosh_sq u
  have hr : fw_rC A α τ = A * x ^ 2 := by simp only [fw_rC, ← hu, e2]
  refine ⟨by rw [hr, e3]; linear_combination (x ^ 6) * hA3, ?_⟩
  have hsd : HasDerivAt (fun y => Real.sinh (3 * y / (2 * α))) (Real.cosh u * (3 / (2 * α))) τ := by
    have h := (((hasDerivAt_id' τ).const_mul 3).div_const (2 * α)).sinh
    exact h.congr_deriv (by simp [hu])
  have hd := (hsd.rpow_const (p := (2 / 3 : ℝ)) (Or.inl hs.ne')).const_mul A
  refine ⟨_, hd, ?_⟩
  rw [e1, hr]
  rw [e3] at cs
  have hαne := hα.ne'
  field_simp
  linear_combination A ^ 3 * cs + hA3

/-! ## Row 3d: the horizon of a waist point, in the embedding `ℝ^{1,4}` -/

/-- The Euclidean dot product on `ℝ⁴`. -/
def fw_dot (x y : Fin 4 → ℝ) : ℝ := ∑ i, x i * y i

/-- The oriented future cosmological horizon of the waist point `p = (0, αn)` of
`dS₄ = {−X₀² + |x|² = α²} ⊂ ℝ^{1,4}`: the section of de Sitter by the null hyperplane `X₀ = x·n` with `X₀ > 0`. -/
def fw_H (α : ℝ) (n : Fin 4 → ℝ) : Set (ℝ × (Fin 4 → ℝ)) :=
  {X | -X.1 ^ 2 + fw_dot X.2 X.2 = α ^ 2 ∧ 0 < X.1 ∧ X.1 = fw_dot X.2 n}

/-- The hyperplane's normal `(−1, n)` is null in `ℝ^{1,4}` for a unit `n`. -/
theorem fw_H_null {n : Fin 4 → ℝ} (hn : fw_dot n n = 1) : -(-1 : ℝ) ^ 2 + fw_dot n n = 0 := by
  rw [hn]; norm_num

/-- A unit vector orthogonal to `n`, `(−n₁, n₀, −n₃, n₂)`. -/
def fw_perp (n : Fin 4 → ℝ) : Fin 4 → ℝ := ![-n 1, n 0, -n 3, n 2]

/-- **Row 3d.** `n ↦ ℋ⁺(n)` is injective on unit vectors: the oriented future horizon distinguishes its waist point,
in particular `p` from its antipode `−p`. -/
theorem fw_horizon_inj {α : ℝ} (hα : 0 < α) {n n' : Fin 4 → ℝ} (hn : fw_dot n n = 1) (hn' : fw_dot n' n' = 1)
    (h : fw_H α n = fw_H α n') : n = n' := by
  by_contra hne
  have hd : 0 < 1 - fw_dot n n' := by
    have hpos : 0 < fw_dot (n - n') (n - n') := by
      simp only [fw_dot, Fin.sum_univ_four, Pi.sub_apply]
      by_contra hle
      apply hne
      funext i
      fin_cases i <;> simp <;> nlinarith [sq_nonneg (n 0 - n' 0), sq_nonneg (n 1 - n' 1),
        sq_nonneg (n 2 - n' 2), sq_nonneg (n 3 - n' 3)]
    have e : fw_dot (n - n') (n - n') = fw_dot n n - 2 * fw_dot n n' + fw_dot n' n' := by
      simp only [fw_dot, Fin.sum_univ_four, Pi.sub_apply]; ring
    rw [e, hn, hn'] at hpos; linarith
  set m := fw_perp n
  have hmn : fw_dot m n = 0 := by simp [m, fw_perp, fw_dot, Fin.sum_univ_four]; ring
  have hmm : fw_dot m m = 1 := by
    rw [← hn]; simp [m, fw_perp, fw_dot, Fin.sum_univ_four]; ring
  set t := (α * |fw_dot m n'| + 1) / (1 - fw_dot n n')
  have ht : 0 < t := by positivity
  set X : ℝ × (Fin 4 → ℝ) := (t, fun i => t * n i + α * m i)
  have hX : X ∈ fw_H α n := by
    refine ⟨?_, ht, ?_⟩
    · have e : fw_dot X.2 X.2 = t ^ 2 * fw_dot n n + 2 * t * α * fw_dot m n + α ^ 2 * fw_dot m m := by
        simp only [X, fw_dot, Fin.sum_univ_four]; ring
      rw [e, hn, hmn, hmm]; simp only [X]; ring
    · have e : fw_dot X.2 n = t * fw_dot n n + α * fw_dot m n := by
        simp only [X, fw_dot, Fin.sum_univ_four]; ring
      rw [e, hn, hmn]; simp only [X]; ring
  rw [h] at hX
  obtain ⟨-, -, h3⟩ := hX
  have e : fw_dot X.2 n' = t * fw_dot n n' + α * fw_dot m n' := by
    simp only [X, fw_dot, Fin.sum_univ_four]; ring
  rw [e] at h3
  simp only [X] at h3
  have key : t * (1 - fw_dot n n') = α * fw_dot m n' := by linarith
  have tt : t * (1 - fw_dot n n') = α * |fw_dot m n'| + 1 := by
    simp only [t]; field_simp
  have := le_abs_self (fw_dot m n')
  nlinarith

/-! ## Row 7c: the turnaround is bounded along the whole lap -/

/-- `y(r) = (|r|/r₀)^{3/2}` on `r ≤ 0`, written `a√a` with `a = −r/r₀`. -/
noncomputable def fw_y (r₀ r : ℝ) : ℝ := (-r / r₀) * Real.sqrt (-r / r₀)

/-- The complex cosmic time along the conjugate branch: `−(2α/3) i arcsin y` on the lap `[−r₀, 0]`, and
`(2α/3)(arcosh y − iπ/2)` beyond the turnaround. -/
noncomputable def fw_τ (α r₀ r : ℝ) : ℂ :=
  if -r₀ ≤ r then -((2 * α / 3 : ℝ) : ℂ) * Complex.I * (Real.arcsin (fw_y r₀ r) : ℂ)
  else ((2 * α / 3 : ℝ) : ℂ) * ((Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I)

lemma fw_y_sq {r₀ r : ℝ} (h0 : 0 < r₀) (hr : r ≤ 0) : fw_y r₀ r ^ 2 = (-r / r₀) ^ 3 := by
  have ha : 0 ≤ -r / r₀ := div_nonneg (by linarith) h0.le
  simp only [fw_y]; rw [mul_pow, Real.sq_sqrt ha]; ring

lemma fw_y_nonneg {r₀ r : ℝ} (h0 : 0 < r₀) (hr : r ≤ 0) : 0 ≤ fw_y r₀ r :=
  mul_nonneg (div_nonneg (by linarith) h0.le) (Real.sqrt_nonneg _)

lemma fw_y_le_one {r₀ r : ℝ} (h0 : 0 < r₀) (hr : -r₀ ≤ r) (hr0 : r ≤ 0) : fw_y r₀ r ≤ 1 := by
  have ha : -r / r₀ ≤ 1 := by rw [div_le_one h0]; linarith
  have ha0 : 0 ≤ -r / r₀ := div_nonneg (by linarith) h0.le
  simp only [fw_y]
  have : Real.sqrt (-r / r₀) ≤ 1 := Real.sqrt_le_one.mpr ha
  nlinarith [Real.sqrt_nonneg (-r / r₀)]

lemma fw_one_le_y {r₀ r : ℝ} (h0 : 0 < r₀) (hr : r ≤ -r₀) : 1 ≤ fw_y r₀ r := by
  have ha : 1 ≤ -r / r₀ := by rw [le_div_iff₀ h0]; linarith
  simp only [fw_y]
  have : 1 ≤ Real.sqrt (-r / r₀) := by rw [Real.le_sqrt (by norm_num) (by linarith)]; linarith
  nlinarith

lemma fw_y_cont (r₀ : ℝ) : Continuous (fw_y r₀) := by unfold fw_y; fun_prop

/-- **Row 7c (the bead).** On the whole conjugate branch `r ≤ 0`, `τ̃(r)` solves `r³ = 2Mα² sinh²(3τ̃/2α)`. -/
theorem fw_τ_bead {M α r₀ r : ℝ} (hα : 0 < α) (h0 : 0 < r₀) (h3 : r₀ ^ 3 = 2 * M * α ^ 2) (hr : r ≤ 0) :
    (r : ℂ) ^ 3 = 2 * M * α ^ 2 * Complex.sinh (3 * fw_τ α r₀ r / (2 * α)) ^ 2 := by
  have hαc : (α : ℂ) ≠ 0 := Complex.ofReal_ne_zero.2 hα.ne'
  have hy2 := fw_y_sq h0 hr
  have key : (2 * M * α ^ 2 : ℝ) * (-(fw_y r₀ r ^ 2)) = r ^ 3 := by
    rw [hy2, ← h3]; field_simp
  unfold fw_τ
  split_ifs with hc
  · have harg : (3 * (-((2 * α / 3 : ℝ) : ℂ) * Complex.I * (Real.arcsin (fw_y r₀ r) : ℂ)) / (2 * α) : ℂ) =
        ((-Real.arcsin (fw_y r₀ r) : ℝ) : ℂ) * Complex.I := by
      push_cast; field_simp
    rw [harg, Complex.sinh_mul_I, ← Complex.ofReal_sin, Real.sin_neg,
      Real.sin_arcsin (by linarith [fw_y_nonneg h0 hr]) (fw_y_le_one h0 hc hr)]
    have := congrArg (fun z : ℝ => (z : ℂ)) key
    push_cast at this ⊢
    linear_combination (-1 : ℂ) * this + (-(2 * (M : ℂ) * α ^ 2 * (fw_y r₀ r : ℂ) ^ 2)) * Complex.I_sq
  · simp only [not_le] at hc
    have hy1 := fw_one_le_y h0 hc.le
    have harg : (3 * (((2 * α / 3 : ℝ) : ℂ) * ((Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I)) /
        (2 * α) : ℂ) = (Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I := by
      push_cast; field_simp
    rw [harg, Complex.sinh_sub, Complex.sinh_mul_I, Complex.cosh_mul_I, ← Complex.ofReal_sin,
      ← Complex.ofReal_cos, Real.sin_pi_div_two, Real.cos_pi_div_two, ← Complex.ofReal_cosh,
      Real.cosh_arcosh hy1]
    have := congrArg (fun z : ℝ => (z : ℂ)) key
    push_cast at this ⊢
    linear_combination (-1 : ℂ) * this + (-(2 * (M : ℂ) * α ^ 2 * (fw_y r₀ r : ℂ) ^ 2)) * Complex.I_sq

/-- **Row 7c (the bound).** Along the whole branch, `|Im τ̃| ≤ πα/3`, with equality exactly beyond the turnaround,
`r ≤ −r₀`. -/
theorem fw_τ_bound {α r₀ r : ℝ} (hα : 0 < α) (h0 : 0 < r₀) (hr : r ≤ 0) :
    |(fw_τ α r₀ r).im| ≤ π * α / 3 ∧ (|(fw_τ α r₀ r).im| = π * α / 3 ↔ r ≤ -r₀) := by
  unfold fw_τ
  split_ifs with hc
  · have hy0 := fw_y_nonneg h0 hr
    have hy1 := fw_y_le_one h0 hc hr
    have ha0 : 0 ≤ Real.arcsin (fw_y r₀ r) := Real.arcsin_nonneg.2 hy0
    have ha1 : Real.arcsin (fw_y r₀ r) ≤ π / 2 := Real.arcsin_le_pi_div_two _
    have him : (-((2 * α / 3 : ℝ) : ℂ) * Complex.I * (Real.arcsin (fw_y r₀ r) : ℂ)).im =
        -(2 * α / 3 * Real.arcsin (fw_y r₀ r)) := by simp
    rw [him, abs_neg, abs_of_nonneg (by positivity)]
    refine ⟨by nlinarith, ⟨fun h => ?_, fun h => ?_⟩⟩
    · have ha : Real.arcsin (fw_y r₀ r) = π / 2 := by
        have : 2 * α / 3 * Real.arcsin (fw_y r₀ r) = 2 * α / 3 * (π / 2) := by rw [h]; ring
        exact mul_left_cancel₀ (by positivity) this
      have hy : fw_y r₀ r = 1 := by
        have := congrArg Real.sin ha
        rwa [Real.sin_arcsin (by linarith) hy1, Real.sin_pi_div_two] at this
      have hy2 := fw_y_sq h0 hr
      rw [hy, one_pow] at hy2
      have ha3 : -r / r₀ = 1 := by
        have hpos : 0 ≤ -r / r₀ := div_nonneg (by linarith) h0.le
        nlinarith [sq_nonneg (-r / r₀ - 1), sq_nonneg (-r / r₀)]
      rw [div_eq_one_iff_eq h0.ne'] at ha3
      linarith
    · have hrr : r = -r₀ := le_antisymm h hc
      have hy : fw_y r₀ r = 1 := by
        simp only [fw_y, hrr, neg_neg, div_self h0.ne', Real.sqrt_one, mul_one]
      rw [hy, Real.arcsin_one]; ring
  · simp only [not_le] at hc
    have him : (((2 * α / 3 : ℝ) : ℂ) * ((Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I)).im =
        -(π * α / 3) := by simp; ring
    rw [him, abs_neg, abs_of_pos (by positivity)]
    exact ⟨le_rfl, ⟨fun _ => hc.le, fun _ => rfl⟩⟩

/-- **Row 7c (continuity).** `τ̃` is continuous on the whole conjugate branch `(−∞, 0]`: each piece is continuous,
and they agree at the turnaround `r = −r₀`, where both give `−iπα/3`. -/
theorem fw_τ_cont {α r₀ : ℝ} (h0 : 0 < r₀) : ContinuousOn (fw_τ α r₀) (Iic 0) := by
  have c1 : Continuous fun r => -((2 * α / 3 : ℝ) : ℂ) * Complex.I * (Real.arcsin (fw_y r₀ r) : ℂ) := by
    have := (Real.continuous_arcsin.comp (fw_y_cont r₀))
    fun_prop
  have c2 : ContinuousOn (fun r => ((2 * α / 3 : ℝ) : ℂ) *
      ((Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I)) (Iic (-r₀)) := by
    have ca : ContinuousOn (fun r => Real.arcosh (fw_y r₀ r)) (Iic (-r₀)) :=
      Real.continuousOn_arcosh.comp (fw_y_cont r₀).continuousOn fun r hr => fw_one_le_y h0 hr
    exact continuousOn_const.mul ((Complex.continuous_ofReal.comp_continuousOn ca).sub continuousOn_const)
  have hsplit : Iic (0 : ℝ) = Icc (-r₀) 0 ∪ Iic (-r₀) := by
    ext r; simp only [mem_Iic, mem_Icc, mem_union]; constructor
    · intro h; by_cases h' : -r₀ ≤ r
      · exact Or.inl ⟨h', h⟩
      · exact Or.inr (by linarith)
    · rintro (⟨-, h⟩ | h) <;> linarith
  rw [hsplit]
  refine ContinuousOn.union_of_isClosed ?_ ?_ isClosed_Icc isClosed_Iic
  · refine c1.continuousOn.congr fun r hr => ?_
    simp only [fw_τ, hr.1, ↓reduceIte]
  · refine c2.congr fun r hr => ?_
    by_cases h : -r₀ ≤ r
    · have hrr : r = -r₀ := le_antisymm hr h
      have hy : fw_y r₀ r = 1 := by
        simp only [fw_y, hrr, neg_neg, div_self h0.ne', Real.sqrt_one, mul_one]
      simp only [fw_τ, h, ↓reduceIte, hy, Real.arcsin_one, Real.arcosh_zero]
      push_cast; ring
    · simp only [fw_τ, h, ↓reduceIte]

/-- **Non-vacuity (rows 1, 6, 7c, 3d).** `M = 1`, `α = 1`; the lap at `r₀ = 1`; `n = e₀`, `n′ = e₁`. -/
theorem fw_witness2 :
    (∀ t : ℝ, 0 < t → fw_rC 1 1 t ^ 3 = 2 * (1 / 2) * 1 ^ 2 * Real.sinh (3 * t / (2 * 1)) ^ 2) ∧
      |(fw_τ 1 1 (-1 / 2)).im| ≤ π * 1 / 3 ∧ |(fw_τ 1 1 (-2)).im| = π * 1 / 3 ∧
      fw_H 1 ![1, 0, 0, 0] ≠ fw_H 1 ![0, 1, 0, 0] ∧
      Tendsto (fw_rs 1) (𝓝[>] (2 * 1)) atBot := by
  refine ⟨fun t ht => (fw_sinh23 one_pos one_pos (by norm_num) ht).1,
    (fw_τ_bound one_pos one_pos (by norm_num)).1,
    (fw_τ_bound one_pos one_pos (by norm_num)).2.2 (by norm_num), fun h => ?_, fw_rs_tendsto one_pos⟩
  have := fw_horizon_inj one_pos (by simp [fw_dot, Fin.sum_univ_four]) (by simp [fw_dot, Fin.sum_univ_four]) h
  have := congrFun this 0
  simp at this

end ShadowProbe.FrameworkProbe

#print axioms ShadowProbe.FrameworkProbe.fw_hasDeriv_f
#print axioms ShadowProbe.FrameworkProbe.fw_ef_inv
#print axioms ShadowProbe.FrameworkProbe.fw_dS_null
#print axioms ShadowProbe.FrameworkProbe.fw_horizons
#print axioms ShadowProbe.FrameworkProbe.fw_surface_gravity
#print axioms ShadowProbe.FrameworkProbe.fw_nariai_roots
#print axioms ShadowProbe.FrameworkProbe.fw_turnaround
#print axioms ShadowProbe.FrameworkProbe.fw_one_sub_f
#print axioms ShadowProbe.FrameworkProbe.fw_ω_cube
#print axioms ShadowProbe.FrameworkProbe.fw_comoving_roots
#print axioms ShadowProbe.FrameworkProbe.fw_equilateral
#print axioms ShadowProbe.FrameworkProbe.fw_three_real
#print axioms ShadowProbe.FrameworkProbe.fw_affine_inequiv
#print axioms ShadowProbe.FrameworkProbe.fw_rest_frame
#print axioms ShadowProbe.FrameworkProbe.fw_action_odd
#print axioms ShadowProbe.FrameworkProbe.fw_witness
#print axioms ShadowProbe.FrameworkProbe.fw_rs_deriv
#print axioms ShadowProbe.FrameworkProbe.fw_rs_tendsto
#print axioms ShadowProbe.FrameworkProbe.fw_no_intersection
#print axioms ShadowProbe.FrameworkProbe.fw_timelike_slope
#print axioms ShadowProbe.FrameworkProbe.fw_sinh23
#print axioms ShadowProbe.FrameworkProbe.fw_H_null
#print axioms ShadowProbe.FrameworkProbe.fw_horizon_inj
#print axioms ShadowProbe.FrameworkProbe.fw_τ_bead
#print axioms ShadowProbe.FrameworkProbe.fw_τ_bound
#print axioms ShadowProbe.FrameworkProbe.fw_τ_cont
#print axioms ShadowProbe.FrameworkProbe.fw_witness2

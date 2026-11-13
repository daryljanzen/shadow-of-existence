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

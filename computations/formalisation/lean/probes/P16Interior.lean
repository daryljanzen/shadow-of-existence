import Mathlib

/-!
# P16 interior: the first integral, and no observable reads the sign of √B

Receipt: `receipts/P16_cosmogenesis_paper/P16_no_observable_reads_the_sign_of_the_radiation_amplitude.py`.

Throughout `s` plays the role of the receipt's `sB = √B`; the "flip" is `s ↦ -s`.
Every observable is written on the scale factor `a` with `B := s ^ 2`, exactly as the
receipt's `classify` substitutes `sqrt(B) → -sqrt(B)`.
-/

namespace ShadowProbe.P16Interior

open Real

/-- The interior solution `a(η) = (A/2)(1 - cos η) + s sin η`, `s = √B`. -/
noncomputable def a (A s η : ℝ) : ℝ := A / 2 * (1 - Real.cos η) + s * Real.sin η

/-- Its derivative `a'(η) = (A/2) sin η + s cos η`. -/
noncomputable def ap (A s η : ℝ) : ℝ := A / 2 * Real.sin η + s * Real.cos η

theorem hasDerivAt_a (A s η : ℝ) : HasDerivAt (a A s) (ap A s η) η := by
  have h1 := ((Real.hasDerivAt_cos η).const_sub 1).const_mul (A / 2)
  have h2 := (Real.hasDerivAt_sin η).const_mul s
  have := h1.add h2
  unfold a ap
  convert this using 1
  ring

theorem hasDerivAt_ap (A s η : ℝ) :
    HasDerivAt (ap A s) (A / 2 * Real.cos η - s * Real.sin η) η := by
  have h1 := (Real.hasDerivAt_sin η).const_mul (A / 2)
  have h2 := (Real.hasDerivAt_cos η).const_mul s
  have := h1.add h2
  unfold ap
  convert this using 1
  ring

theorem deriv_a (A s : ℝ) : deriv (a A s) = ap A s :=
  funext fun η => (hasDerivAt_a A s η).deriv

/-! ## (1) the first integral -/

/-- CHECK (1a): the solution satisfies its driven-oscillator equation `a'' + a = A/2`. -/
theorem driven_oscillator (A s η : ℝ) :
    deriv (deriv (a A s)) η + a A s η = A / 2 := by
  rw [deriv_a, (hasDerivAt_ap A s η).deriv]
  unfold a; ring

/-- The identity in `s` alone: `a'² = s² + A a - a²`. -/
theorem first_integral_s (A s η : ℝ) :
    ap A s η ^ 2 = s ^ 2 + A * a A s η - (a A s η) ^ 2 := by
  have hc := Real.sin_sq_add_cos_sq η
  unfold a ap
  linear_combination (A ^ 2 / 4) * hc + s ^ 2 * hc

/-- CHECK (1b), HEADLINE: the first integral `a'² = B + A a - a²` holds identically, `B ≥ 0`. -/
theorem first_integral (A B : ℝ) (hB : 0 ≤ B) (η : ℝ) :
    HasDerivAt (a A (√B)) (ap A (√B) η) η ∧
      (deriv (a A (√B)) η) ^ 2 = B + A * a A (√B) η - (a A (√B) η) ^ 2 := by
  refine ⟨hasDerivAt_a _ _ η, ?_⟩
  rw [deriv_a, first_integral_s, Real.sq_sqrt hB]

/-- CHECK (1c): the constant is fixed by the branch point, `a(0) = 0`, `a'(0) = √B`. -/
theorem branch_point (A s : ℝ) : a A s 0 = 0 ∧ deriv (a A s) 0 = s := by
  rw [deriv_a]; unfold a ap; simp

/-- The first integral DERIVED, not quoted: any twice-differentiable `f` with
`f'' = A/2 - f`, `f(0) = 0`, `f'(0) = s` has `f'² = s² + A f - f²` everywhere. -/
theorem first_integral_derived (A s : ℝ) (f f' : ℝ → ℝ)
    (hf : ∀ x, HasDerivAt f (f' x) x) (hf' : ∀ x, HasDerivAt f' (A / 2 - f x) x)
    (h0 : f 0 = 0) (h0' : f' 0 = s) (x : ℝ) :
    f' x ^ 2 = s ^ 2 + A * f x - f x ^ 2 := by
  set E : ℝ → ℝ := fun t => f' t ^ 2 - A * f t + f t ^ 2 with hE
  have hd : ∀ t, HasDerivAt E 0 t := by
    intro t
    have := (((hf' t).pow 2).sub ((hf t).const_mul A)).add ((hf t).pow 2)
    convert this using 1
    simp; ring
  have hc : E x = E 0 :=
    is_const_of_deriv_eq_zero (fun t => (hd t).differentiableAt)
      (fun t => (hd t).deriv) x 0
  simp only [hE, h0, h0'] at hc
  linarith

/-! ## (2) the reflection -/

/-- HEADLINE: `a(-η; -√B) = a(η; √B)`. -/
theorem reflection (A s η : ℝ) : a A (-s) (-η) = a A s η := by
  unfold a; rw [Real.cos_neg, Real.sin_neg]; ring

/-- Hence every function of `a` along the solution is even in `√B`, up to `η ↦ -η`. -/
theorem fun_of_a_even {α : Type*} (F : ℝ → α) (A s η : ℝ) :
    F (a A (-s) (-η)) = F (a A s η) := by rw [reflection]

/-- The rate on the reflected leg is the time-reversed one: `a'(-η; -√B) = -a'(η; √B)`.
This is the expanding/contracting branch sign, a different sign from `√B`'s. -/
theorem reflection_ap (A s η : ℝ) : ap A (-s) (-η) = -ap A s η := by
  unfold ap; rw [Real.cos_neg, Real.sin_neg]; ring

/-- `a'²`, hence anything built from `a` and `a'²`, is reflection-invariant. -/
theorem reflection_ap_sq (A s η : ℝ) : ap A (-s) (-η) ^ 2 = ap A s η ^ 2 := by
  rw [reflection_ap]; ring

/-! ## (3)/(4) the sweep, each observable as a function of `s = √B` and `a` -/

/-- Even in `s`. -/
def EvenIn (F : ℝ → ℝ) : Prop := ∀ s, F (-s) = F s
/-- Odd in `s`. -/
def OddIn (F : ℝ → ℝ) : Prop := ∀ s, F (-s) = -F s

noncomputable section
variable (A x : ℝ)   -- `x` is the receipt's positive symbol `a`

def rho_m (_s : ℝ) : ℝ := A / x ^ 3
def rho_r (s : ℝ) : ℝ := s ^ 2 / x ^ 4
def ratio (s : ℝ) : ℝ := (s ^ 2 / x ^ 4) / (A / x ^ 3)
def H2 (s : ℝ) : ℝ := (s ^ 2 + A * x - x ^ 2) / x ^ 4
def acc (_s : ℝ) : ℝ := A / 2 - x
def cs2 (s : ℝ) : ℝ := (1 / 3) * (s ^ 2 / x ^ 4) / (s ^ 2 / x ^ 4 + A / x ^ 3)
def apOfA (s : ℝ) : ℝ := √(s ^ 2 + A * x - x ^ 2)
def particleIntegrand (s : ℝ) : ℝ := 1 / √(s ^ 2 + A * x - x ^ 2)
/-- The turnaround root of `B + A a - a² = 0` (the larger, positive root). -/
def turnaround (s : ℝ) : ℝ := (A + √(A ^ 2 + 4 * s ^ 2)) / 2
/-- The sound-horizon integrand / accumulated phase, `c_s / a'(a)` with `c_s = √(c_s²)`. -/
def phase (s : ℝ) : ℝ := √(cs2 A x s) / apOfA A x s
end

theorem even_rho_m (A x : ℝ) : EvenIn (rho_m A x) := fun _ => rfl
theorem even_rho_r (x : ℝ) : EvenIn (rho_r x) := fun s => by simp [rho_r]
theorem even_ratio (A x : ℝ) : EvenIn (ratio A x) := fun s => by simp [ratio]
theorem even_H2 (A x : ℝ) : EvenIn (H2 A x) := fun s => by simp [H2]
theorem even_acc (A x : ℝ) : EvenIn (acc A x) := fun _ => rfl
theorem even_cs2 (A x : ℝ) : EvenIn (cs2 A x) := fun s => by simp [cs2]
theorem even_particleIntegrand (A x : ℝ) : EvenIn (particleIntegrand A x) := fun s => by
  simp [particleIntegrand]
theorem even_turnaround (A : ℝ) : EvenIn (turnaround A) := fun s => by simp [turnaround]
theorem even_phase_sq (A x : ℝ) : EvenIn (fun s => phase A x s ^ 2) := fun s => by
  simp [phase, cs2, apOfA]
/-- And the phase itself, as the positive root of an even square, is even. -/
theorem even_phase (A x : ℝ) : EvenIn (phase A x) := fun s => by simp [phase, cs2, apOfA]

/-- The turnaround really is a root of `a' = 0` on the scale factor. -/
theorem turnaround_root (A s : ℝ) :
    s ^ 2 + A * turnaround A s - turnaround A s ^ 2 = 0 := by
  unfold turnaround
  have h : (√(A ^ 2 + 4 * s ^ 2)) ^ 2 = A ^ 2 + 4 * s ^ 2 :=
    Real.sq_sqrt (by positivity)
  linear_combination (-1 / 4 : ℝ) * h

/-- `H²` along the solution is `a'²/a⁴`, by the first integral. -/
theorem H2_along (A B : ℝ) (hB : 0 ≤ B) (η : ℝ) :
    H2 A (a A (√B) η) (√B) = (deriv (a A (√B)) η / (a A (√B) η) ^ 2) ^ 2 := by
  have h := (first_integral A B hB η).2
  unfold H2; rw [Real.sq_sqrt hB, div_pow, ← pow_mul, h]

/-- HEADLINE sweep: all ten swept quantities are even in `√B`. -/
theorem sweep (A x : ℝ) :
    EvenIn (rho_m A x) ∧ EvenIn (rho_r x) ∧ EvenIn (ratio A x) ∧ EvenIn (H2 A x) ∧
      EvenIn (acc A x) ∧ EvenIn (cs2 A x) ∧ EvenIn (particleIntegrand A x) ∧
      EvenIn (turnaround A) ∧ EvenIn (fun s => phase A x s ^ 2) ∧ EvenIn (phase A x) :=
  ⟨even_rho_m A x, even_rho_r x, even_ratio A x, even_H2 A x, even_acc A x,
    even_cs2 A x, even_particleIntegrand A x, even_turnaround A, even_phase_sq A x,
    even_phase A x⟩

/-! ## (5) the CONTROL: these must NOT come out even -/

/-- `a'(0) = √B` is ODD, and not even once `B > 0`. -/
theorem control_ap0_odd : OddIn (fun s => deriv (a 0 s) 0) ∧ ∀ A, OddIn (fun s => ap A s 0) := by
  refine ⟨fun s => ?_, fun A s => ?_⟩ <;> simp [deriv_a, ap]

theorem control_ap0_not_even (A s : ℝ) (hs : s ≠ 0) : ap A (-s) 0 ≠ ap A s 0 := by
  simp [ap]; intro h; exact hs (by linarith)

/-- `a(η)` at fixed `η` is NEITHER even nor odd in `√B` (for `A > 0`, `B > 0`). -/
theorem control_a_neither (A s : ℝ) (hA : A ≠ 0) (hs : s ≠ 0) :
    (∃ η, a A (-s) η ≠ a A s η) ∧ (∃ η, a A (-s) η ≠ -a A s η) := by
  refine ⟨⟨π / 2, ?_⟩, ⟨π / 2, ?_⟩⟩ <;> simp [a] <;> intro h
  · exact hs (by linarith)
  · exact hA (by linarith)

/-- `a'(η)` at fixed `η` is NEITHER even nor odd in `√B` either. -/
theorem control_ap_neither (A s : ℝ) (hA : A ≠ 0) (hs : s ≠ 0) :
    (∃ η, ap A (-s) η ≠ ap A s η) ∧ (∃ η, ap A (-s) η ≠ -ap A s η) := by
  refine ⟨⟨0, ?_⟩, ⟨π / 2, ?_⟩⟩ <;> simp [ap] <;> intro h
  · exact hs (by linarith)
  · exact hA (by linarith)

#print axioms first_integral
#print axioms first_integral_derived
#print axioms driven_oscillator
#print axioms branch_point
#print axioms reflection
#print axioms fun_of_a_even
#print axioms reflection_ap
#print axioms sweep
#print axioms turnaround_root
#print axioms H2_along
#print axioms control_ap0_odd
#print axioms control_ap0_not_even
#print axioms control_a_neither
#print axioms control_ap_neither

end ShadowProbe.P16Interior

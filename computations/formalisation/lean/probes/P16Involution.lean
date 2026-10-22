import Mathlib

/-!
# P16: the crossing is an involution, and the density is even on the unsigned radius

Receipt: `receipts/P16_cosmogenesis_paper/P16_the_crossing_is_an_involution_and_the_density_is_even_on_the_unsigned_radius.py`.
The two `READ from cosmogenesis_paper.tex` string pins are paper-text pins and are not formalised.
-/

namespace ShadowProbe.P16Involution

open Real

/-! ## (1) the two continuations -/

/-- P3's arc-length radius `r = α sin θ`. -/
noncomputable def rP3 (α θ : ℝ) : ℝ := α * Real.sin θ

/-- CHECK: P3's radius is ODD through the branch point `θ = 0`. -/
theorem rP3_odd (α θ : ℝ) : rP3 α (-θ) = -rP3 α θ := by
  simp [rP3]

/-- P2's bead law `r³ = 2 M α² sinh²(3τ/(2α))`. -/
noncomputable def r3 (M α τ : ℝ) : ℝ := 2 * M * α ^ 2 * Real.sinh (3 * τ / (2 * α)) ^ 2

/-- CHECK: P2's law is EVEN under a reflection in proper time. -/
theorem r3_even (M α τ : ℝ) : r3 M α (-τ) = r3 M α τ := by
  simp [r3, neg_div, Real.sinh_neg]

/-- CHECK: the reflection cannot leave the forward branch: no real `τ` has `r³ < 0`. -/
theorem r3_neg_set_empty (M α : ℝ) (hM : 0 ≤ M) : {τ : ℝ | r3 M α τ < 0} = ∅ := by
  ext τ
  simp only [Set.mem_ofPred_eq, Set.mem_empty_iff_false, iff_false, not_lt]
  unfold r3; positivity

/-- The complexified law, for the continuation. -/
noncomputable def r3C (M α : ℝ) (z : ℂ) : ℂ :=
  2 * M * α ^ 2 * Complex.sinh (3 * z / (2 * α)) ^ 2

theorem r3C_real (M α τ : ℝ) : r3C M α τ = (r3 M α τ : ℂ) := by
  unfold r3C r3; push_cast; ring

/-- The continuation P2 uses: the imaginary offset `τ ↦ τ - iπα/3` at the conjugate
critical point. -/
noncomputable def r3cont (M α τ : ℝ) : ℂ := r3C M α (-(Complex.I * π * α / 3) + τ)

/-- CHECK: the offset turns the law NEGATIVE: `r³ = -2 M α² cosh²(3τ/(2α))`. -/
theorem r3cont_eq (M α τ : ℝ) (hα : α ≠ 0) :
    r3cont M α τ = -(2 * M * α ^ 2 * Real.cosh (3 * τ / (2 * α)) ^ 2 : ℝ) := by
  have hα' : (α : ℂ) ≠ 0 := by exact_mod_cast hα
  have harg : 3 * (-(Complex.I * π * α / 3) + τ) / (2 * α)
      = (3 * τ / (2 * α) : ℝ) + (-(π / 2 : ℝ)) * Complex.I := by
    push_cast; field_simp; ring
  unfold r3cont r3C
  have hcos : Complex.cos (-((π / 2 : ℝ) : ℂ)) = 0 := by
    rw [← Complex.ofReal_neg, ← Complex.ofReal_cos, Real.cos_neg, Real.cos_pi_div_two]; simp
  have hsin : Complex.sin (-((π / 2 : ℝ) : ℂ)) = -1 := by
    rw [← Complex.ofReal_neg, ← Complex.ofReal_sin, Real.sin_neg, Real.sin_pi_div_two]; simp
  rw [harg, Complex.sinh_add, ← Complex.ofReal_sinh, ← Complex.ofReal_cosh,
    Complex.sinh_mul_I, Complex.cosh_mul_I, hcos, hsin]
  push_cast
  ring_nf
  rw [Complex.I_sq]; ring

/-- CHECK: at the conjugate critical point itself, `r³ = -2 M α²` exactly. -/
theorem r3cont_zero (M α : ℝ) (hα : α ≠ 0) :
    r3cont M α 0 = -(2 * M * α ^ 2 : ℝ) := by
  rw [r3cont_eq M α 0 hα]; simp

/-- CHECK, HEADLINE (1): the two continuations agree: both carry `r` through zero onto a
negative branch. -/
theorem continuations_agree (M α : ℝ) (hα : α ≠ 0) :
    (∀ θ, rP3 α (-θ) = -rP3 α θ) ∧ r3cont M α 0 = -(2 * M * α ^ 2 : ℝ) :=
  ⟨rP3_odd α, r3cont_zero M α hα⟩

/-- ... and for `M, α` nonzero the continued value is strictly negative, real. -/
theorem r3cont_zero_neg (M α : ℝ) (hM : 0 < M) (hα : α ≠ 0) :
    -(2 * M * α ^ 2) < (0 : ℝ) := by
  have : 0 < α ^ 2 := by positivity
  nlinarith

/-! ## (2)/(3) the density -/

/-- The naive dust density on the SIGNED radius. -/
noncomputable def rhoNaive (Mb r : ℝ) : ℝ := 3 * Mb / (4 * π * r ^ 3)
/-- The dust density on the UNSIGNED radius (the volume goes as `|r|³`). -/
noncomputable def rhoTrue (Mb r : ℝ) : ℝ := 3 * Mb / (4 * π * |r| ^ 3)

/-- CHECK (2): the naive density is ODD in `r`. -/
theorem rhoNaive_odd (Mb r : ℝ) : rhoNaive Mb (-r) = -rhoNaive Mb r := by
  unfold rhoNaive; rw [Odd.neg_pow (by decide)]; ring

/-- ... so it changes sign across the branch point (for `Mb > 0`, `r ≠ 0`). -/
theorem rhoNaive_changes_sign (Mb r : ℝ) (hMb : 0 < Mb) (hr : 0 < r) :
    0 < rhoNaive Mb r ∧ rhoNaive Mb (-r) < 0 := by
  have h : 0 < rhoNaive Mb r := by unfold rhoNaive; positivity
  exact ⟨h, by rw [rhoNaive_odd]; linarith⟩

/-- CHECK (3), HEADLINE: the density on the unsigned radius is EVEN. -/
theorem rhoTrue_even (Mb r : ℝ) : rhoTrue Mb (-r) = rhoTrue Mb r := by
  simp [rhoTrue]

theorem rhoTrue_pos (Mb r : ℝ) (hMb : 0 < Mb) (hr : r ≠ 0) : 0 < rhoTrue Mb r := by
  unfold rhoTrue; have := abs_pos.mpr hr; positivity

/-! ## (4) the areal rate -/

theorem hasDerivAt_rP3 (α θ : ℝ) : HasDerivAt (rP3 α) (α * Real.cos θ) θ :=
  (Real.hasDerivAt_sin θ).const_mul α

/-- CHECK: the SIGNED areal rate `dr/dθ = α cos θ` is EVEN in `θ`. -/
theorem signed_rate_even (α θ : ℝ) :
    deriv (rP3 α) (-θ) = deriv (rP3 α) θ := by
  rw [(hasDerivAt_rP3 α _).deriv, (hasDerivAt_rP3 α _).deriv, Real.cos_neg]

/-- Derivative of an even function is odd (pointwise, junk values included). -/
theorem deriv_odd_of_even (f : ℝ → ℝ) (hf : ∀ x, f (-x) = f x) (x : ℝ) :
    deriv f (-x) = -deriv f x := by
  have h : (fun y => f (-y)) = f := funext hf
  have := deriv_comp_neg (f := f) (x := x)
  rw [h] at this
  linarith

/-- CHECK (4), HEADLINE: `d|r|/dθ` is ODD for every `θ`. -/
theorem unsigned_rate_odd (α θ : ℝ) :
    deriv (fun t => |rP3 α t|) (-θ) = -deriv (fun t => |rP3 α t|) θ :=
  deriv_odd_of_even _ (fun x => by rw [rP3_odd, abs_neg]) θ

/-- Its value off the branch point: `d|r|/dθ = sign(α sin θ) · α cos θ`. -/
theorem hasDerivAt_unsigned (α θ : ℝ) (h : α * Real.sin θ ≠ 0) :
    HasDerivAt (fun t => |rP3 α t|) (SignType.sign (α * Real.sin θ) * (α * Real.cos θ)) θ := by
  have := (hasDerivAt_abs h).comp θ (hasDerivAt_rP3 α θ)
  simpa [rP3, Function.comp_def] using this

/-- Infall becomes outflow: for `α > 0` and `0 < θ < π/2` the unsigned radius grows,
and at `-θ` it shrinks. -/
theorem infall_becomes_outflow (α θ : ℝ) (hα : 0 < α) (h0 : 0 < θ) (h1 : θ < π / 2) :
    0 < deriv (fun t => |rP3 α t|) θ ∧ deriv (fun t => |rP3 α t|) (-θ) < 0 := by
  have hs : 0 < Real.sin θ := Real.sin_pos_of_pos_of_lt_pi h0 (by linarith [Real.pi_pos])
  have hc : 0 < Real.cos θ := Real.cos_pos_of_mem_Ioo ⟨by linarith, h1⟩
  have hp : 0 < α * Real.sin θ := mul_pos hα hs
  have hd := (hasDerivAt_unsigned α θ hp.ne').deriv
  rw [sign_pos hp] at hd
  simp only [SignType.coe_one, one_mul] at hd
  have : 0 < deriv (fun t => |rP3 α t|) θ := by rw [hd]; exact mul_pos hα hc
  exact ⟨this, by rw [unsigned_rate_odd]; linarith⟩

/-! ## (5) the involution -/

/-- The crossing map `(ρ(l), v(l)) ↦ (ρ(-l), -v(-l))` on density/rate histories. -/
def crossing (p : (ℝ → ℝ) × (ℝ → ℝ)) : (ℝ → ℝ) × (ℝ → ℝ) :=
  (fun l => p.1 (-l), fun l => -p.2 (-l))

/-- CHECK (5), HEADLINE: applied twice it is the identity. -/
theorem crossing_twice (p : (ℝ → ℝ) × (ℝ → ℝ)) : crossing (crossing p) = p := by
  obtain ⟨f, g⟩ := p
  simp [crossing]

theorem crossing_involutive : Function.Involutive crossing := crossing_twice

/-- Hence a bijection on the state space: nothing lost, nothing added. -/
theorem crossing_bijective : Function.Bijective crossing :=
  crossing_involutive.bijective

/-- With the receipt's even density history and odd rate history, the crossing
returns the same state. -/
theorem crossing_fixes_even_odd (R V : ℝ → ℝ) (hR : ∀ l, R (-l) = R l)
    (hV : ∀ l, V (-l) = -V l) : crossing (R, V) = (R, V) := by
  simp [crossing, hR, hV]

/-! ## CONTROL: on the signed radius the parity follows the exponent -/

/-- Signed `r⁻ⁿ`, odd iff `n` odd. -/
theorem control_signed_odd (n : ℕ) (hn : Odd n) (r : ℝ) : ((-r) ^ n)⁻¹ = -(r ^ n)⁻¹ := by
  rw [hn.neg_pow, inv_neg]

theorem control_signed_even (n : ℕ) (hn : Even n) (r : ℝ) : ((-r) ^ n)⁻¹ = (r ^ n)⁻¹ := by
  rw [hn.neg_pow]

/-- HEADLINE CONTROL: dust `r⁻³` is ODD and not even; radiation `r⁻⁴` and stiff `r⁻⁶` are
EVEN and not odd; on the unsigned radius all three are EVEN. -/
theorem control :
    ((∀ r : ℝ, ((-r) ^ 3)⁻¹ = -(r ^ 3)⁻¹) ∧ ¬ (∀ r : ℝ, ((-r) ^ 3)⁻¹ = (r ^ 3)⁻¹)) ∧
    ((∀ r : ℝ, ((-r) ^ 4)⁻¹ = (r ^ 4)⁻¹) ∧ ¬ (∀ r : ℝ, ((-r) ^ 4)⁻¹ = -(r ^ 4)⁻¹)) ∧
    ((∀ r : ℝ, ((-r) ^ 6)⁻¹ = (r ^ 6)⁻¹) ∧ ¬ (∀ r : ℝ, ((-r) ^ 6)⁻¹ = -(r ^ 6)⁻¹)) ∧
    (∀ r : ℝ, (|-r| ^ 3)⁻¹ = (|r| ^ 3)⁻¹) ∧ (∀ r : ℝ, (|-r| ^ 4)⁻¹ = (|r| ^ 4)⁻¹) ∧
    (∀ r : ℝ, (|-r| ^ 6)⁻¹ = (|r| ^ 6)⁻¹) := by
  refine ⟨⟨control_signed_odd 3 (by decide), fun h => ?_⟩,
    ⟨control_signed_even 4 (by decide), fun h => ?_⟩,
    ⟨control_signed_even 6 (by decide), fun h => ?_⟩,
    fun r => by rw [abs_neg], fun r => by rw [abs_neg], fun r => by rw [abs_neg]⟩
  · have := h 1; norm_num at this
  · have := h 1; norm_num at this
  · have := h 1; norm_num at this

#print axioms rP3_odd
#print axioms r3_even
#print axioms r3_neg_set_empty
#print axioms r3C_real
#print axioms r3cont_eq
#print axioms r3cont_zero
#print axioms continuations_agree
#print axioms rhoNaive_odd
#print axioms rhoNaive_changes_sign
#print axioms rhoTrue_even
#print axioms signed_rate_even
#print axioms unsigned_rate_odd
#print axioms hasDerivAt_unsigned
#print axioms infall_becomes_outflow
#print axioms crossing_twice
#print axioms crossing_bijective
#print axioms crossing_fixes_even_odd
#print axioms control

end ShadowProbe.P16Involution

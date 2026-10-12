import Mathlib

/-!
# I20, stated as what it computes

`r7263+71` · order ② of `FOR_71.md` §`r7263`, pre-registered in
`computations/formalisation/r7263_71_first_statements/PREDICTION.md`.

The receipt is
`receipts/P04_modern_parallax/I20_the_redshift_is_a_conformal_killing_charge_on_the_null_cone.py`
(another seat's; not edited). It prints `VERDICT: ALL PASS`, and every claim it makes is true.
This file writes each of its ten checks as the Lean statement of what the Python actually
verifies, beside the geometric theorem the check is filed under.

## The theorem I20 is filed under, and why it is a comment and not a `theorem`

> On the conformally flat metric `g = a(η)² (−dη² + dx²)`, the vector `ξ = ∂_η` is a
> conformal Killing field, `𝓛_ξ g = 2 (a′/a) g`; for a conformal Killing field the charge
> `g(ξ, γ̇)` is conserved along every **null** geodesic `γ` and along no other; on the null
> cone that charge is `a·ω`, so `1 + z = a_obs / a_em` and `ln (1 + z) = ∫ H dt`.

Stating that needs, as of `mathlib4` `4e6064a4` and `Physlib` `b0e7ca1c`
(`computations/formalisation/r7259_71_ground/RESULT.md` Ⓒ, Ⓓ), five layers that are absent:

1. a pseudo-Riemannian metric of signature `(1, n)` as a smooth `(0,2)`-tensor field
   (mathlib's `RiemannianMetric` carries `pos : 0 < inner b v v`);
2. the Lie derivative of a tensor field along a vector field (only `VectorField.mlieBracket` exists);
3. the conformal-Killing equation;
4. null vectors and null geodesics of the metric;
5. the charge `g(K, γ̇)` along a null geodesic.

So none of it is stated below. What is stated is the coordinate content, and each statement
says in its docstring which part of the theorem it does *not* reach.

## The ten checks

`a : ℝ → ℝ` is the scale factor as a function of conformal time. I20 declares it positive, so
positivity is a hypothesis wherever it is used.
-/

open Real

namespace ShadowFormal.I20

/-! ### ① the one check that carries content -/

/-- **① `L_ξ g = 2 (a′/a) g`, diagonal components.**

What the receipt computes is `ξ^α ∂_α g_{μν} + g_{αν} ∂_μ ξ^α + g_{μα} ∂_ν ξ^α` for
`ξ = (1, 0)` and `g = diag(−a², a²)`. Its second and third terms vanish because `ξ` is
constant, and `∂_x g = 0` because `g` depends on `η` only. Those two facts are properties of the
chart, so the statement keeps only the surviving term, `∂_η g_{μμ}`.

**Not reached:** that this expression *is* `𝓛_ξ g` (layer 2), so this is not yet the statement
that `ξ` is conformal Killing (layer 3). -/
theorem lie_eta_component (a : ℝ → ℝ) (η : ℝ) (hd : DifferentiableAt ℝ a η) (ha : a η ≠ 0)
    (s : ℝ) :
    deriv (fun t => s * a t ^ 2) η = 2 * (deriv a η / a η) * (s * a η ^ 2) := by
  have h : HasDerivAt (fun t => s * a t ^ 2) (s * (2 * a η * deriv a η)) η := by
    have := (hd.hasDerivAt.pow 2).const_mul s
    simpa [pow_one, mul_comm, mul_left_comm, mul_assoc] using this
  rw [h.deriv]
  field_simp

/-! ### ② needs a witness the receipt never supplied -/

/-- **② "and NOT an exact Killing vector".** The receipt's test is `simplify(Lg) != 0`, which
passes whenever `simplify` fails to reach zero. Its Lean form is existential and needs a
witness: here `a = exp` at `η = 0`.

**Not reached:** "not Killing" as a property of the vector field on the manifold (layers 1–3). -/
theorem not_killing_witness :
    ∃ a : ℝ → ℝ, deriv (fun t => -(a t ^ 2)) 0 ≠ 0 := by
  refine ⟨Real.exp, ?_⟩
  have h : HasDerivAt (fun t => -(Real.exp t ^ 2)) (-(2 * Real.exp 0 ^ 1 * Real.exp 0)) 0 :=
    ((Real.hasDerivAt_exp 0).pow 2).neg
  rw [h.deriv]
  simp

/-! ### ③–⑥ true by the asserted input -/

/-- The momentum the receipt assigns to the null geodesic, `p^η = C / a²`. The receipt states it
in a comment; it is **not** derived there from the geodesic equation. (It is true:
`I20_which_checks_could_fail.py` derives it with sympy.) -/
noncomputable def pEta (C : ℝ) (a : ℝ → ℝ) (η : ℝ) : ℝ := C / a η ^ 2

/-- **③ "ξ·p = −a² p^η = −C, constant along the null geodesic".** Pointwise, the charge
evaluated on the asserted input is the constant `−C`, by `field_simp`: the input is the
conclusion.

**Not reached:** constancy *along a geodesic* (layers 4 and 5). There is no geodesic in the
statement because the receipt's code has none. -/
theorem charge_on_asserted_input (C : ℝ) (a : ℝ → ℝ) (η : ℝ) (ha : a η ≠ 0) :
    -(a η ^ 2) * pEta C a η = -C := by
  unfold pEta
  field_simp

/-- **④ "the comoving frequency is ω = a p^η = C/a".** -/
theorem omega_eq (C : ℝ) (a : ℝ → ℝ) (η : ℝ) (ha : a η ≠ 0) :
    a η * pEta C a η = C / a η := by
  unfold pEta
  field_simp

/-- **⑤ "so a·ω = C is CONSTANT".** -/
theorem a_omega_const (C : ℝ) (a : ℝ → ℝ) (η : ℝ) (ha : a η ≠ 0) :
    a η * (C / a η) = C := by
  field_simp

/-- **⑥ "a·ω constant integrates to 1+z = a_obs/a_em".** No integration occurs: it is the
quotient of `C/a_em` by `C/a_obs`. -/
theorem one_plus_z (C a_em a_obs : ℝ) (hC : C ≠ 0) (he : a_em ≠ 0) (ho : a_obs ≠ 0) :
    (C / a_em) / (C / a_obs) = a_obs / a_em := by
  field_simp

/-! ### ⑦ cannot fail -/

/-- **⑦ "ln(1+z) = ln a_obs − ln a_em = ∫ H dt, since H = d(ln a)/dt".** The receipt's test is the
first equality, which is `Real.log_div`. **`H` appears nowhere in the statement, because it
appears nowhere in the test**; the integral named in the check's title is not computed by the
receipt, and the check passes for every `H`.

**Not reached:** `∫ H dt` (not stated by the receipt at all). -/
theorem log_ratio (a_em a_obs : ℝ) (he : a_em ≠ 0) (ho : a_obs ≠ 0) :
    Real.log (a_obs / a_em) = Real.log a_obs - Real.log a_em :=
  Real.log_div ho he

/-! ### ⑧–⑩ the massive control -/

/-- **⑧ "CONTROL: the spatial momentum still falls as 1/a".** The receipt's test is
`diff(a * (C/a), eta) == 0`. **Pointwise, that is the same proposition as ⑤**: the two checks
are one statement under two titles. -/
theorem control_momentum (C : ℝ) (a : ℝ → ℝ) (η : ℝ) (ha : a η ≠ 0) :
    a η * (C / a η) = C :=
  a_omega_const C a η ha

/-- **⑨ "CONTROL: a·E is NOT constant for m ≠ 0".** The receipt's test is `simplify(dEa) != 0`,
which is fail-open. Its Lean form needs a witness: at `a = exp`, `C = m = 1`, the energy charge
`a·√((C/a)² + m²)` equals `√(1 + e^{2η})`, whose derivative at `0` is nonzero. -/
theorem control_massive_witness :
    deriv (fun t => Real.exp t * Real.sqrt ((1 / Real.exp t) ^ 2 + 1 ^ 2)) 0 ≠ 0 := by
  have hfun : (fun t => Real.exp t * Real.sqrt ((1 / Real.exp t) ^ 2 + 1 ^ 2)) =
      fun t => Real.sqrt (1 + Real.exp t ^ 2) := by
    funext t
    have he : 0 < Real.exp t := Real.exp_pos t
    have hs : Real.exp t * Real.sqrt ((1 / Real.exp t) ^ 2 + 1 ^ 2) =
        Real.sqrt (Real.exp t ^ 2) * Real.sqrt ((1 / Real.exp t) ^ 2 + 1 ^ 2) := by
      rw [Real.sqrt_sq he.le]
    rw [hs, ← Real.sqrt_mul (sq_nonneg _)]
    congr 1
    field_simp
  rw [hfun]
  have hin : HasDerivAt (fun t => 1 + Real.exp t ^ 2) (2 * Real.exp 0 * Real.exp 0) 0 := by
    have := ((Real.hasDerivAt_exp 0).pow 2).const_add 1
    simpa [pow_one, mul_comm, mul_left_comm, mul_assoc] using this
  have hpos : (1 + Real.exp 0 ^ 2) ≠ 0 := by positivity
  rw [(hin.sqrt hpos).deriv]
  simp

/-- **⑩ "CONTROL: and it DOES become constant in the massless limit".** At `m = 0` and `a > 0`
(I20's own declaration), the energy charge is the constant `|C|`. -/
theorem control_massless (C : ℝ) (a : ℝ → ℝ) (η : ℝ) (ha : 0 < a η) :
    a η * Real.sqrt ((C / a η) ^ 2 + 0 ^ 2) = |C| := by
  rw [zero_pow two_ne_zero, add_zero, Real.sqrt_sq_eq_abs, abs_div, abs_of_pos ha]
  field_simp

end ShadowFormal.I20

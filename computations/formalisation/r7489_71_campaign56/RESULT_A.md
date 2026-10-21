# `r7503+71.3` — RESULT: campaign 56 (`r7489` ②) BUILT, all three. ⌗ The full-sky F law as a measure equality; the P16 interior's first integral and its evenness in `√B`; the dust crossing's involution. ⌗ `715` lines in three probes (band 400–2000, IN BAND). ⌗ All three p came true (`0.35`, `0.75`, `0.65`)

*Scored against `PREDICTION.md` (pushed at `r7503+71.1` before any Lean), not revised. Each file was re-run by 71
(`PROBE_RUN_A.txt`); every theorem is on `[propext, Classical.choice, Quot.sound]`.*
- *`probes/FLaw.lean`: 8 theorems, `11 s`.*
- *`probes/P16Interior.lean`: 14 theorems, `9 s`.*
- *`probes/P16Involution.lean`: 18 theorems, `10 s`.*

## F — the full-sky law, BUILT as a measure equality

- ***`map_ratio_chiSq_eq_fMeasure`.*** For real `ν₁, ν₂ > 0`, `(χ²ν₁ ⊗ χ²ν₂).map ((x, y) ↦ (x/ν₁)/(y/ν₂)) = F(ν₁, ν₂)`.
  Here `χ²ν` is Mathlib's `gammaMeasure (ν/2) (1/2)`, and `F` has density
  `(ν₁/ν₂)^{ν₁/2} r^{ν₁/2−1}(1 + ν₁r/ν₂)^{−(ν₁+ν₂)/2}/B(ν₁/2, ν₂/2)`.
- ***`law_ratio_of_indep`*** gives the same for any independent random variables with those laws.
  `isProbabilityMeasure_fMeasure` shows the density integrates to 1. `cdf_ratio_chiSq` gives the CDF.
- ***The receipt's form.*** `receipt_scaled_ratio_F57`, `receipt_law_R` and `receipt_p_exact` state
  `P(R ≤ r) = F(5,7)(r/(d₂/d₃))` exactly: the receipt's `stats.f.cdf` call at `f_sky = 1`. The float `p`-values are
  not claimed, as registered.
- ***Route.*** The joint density, Tonelli, and the substitution `x = (ν₁/ν₂)yr`. Then one pointwise Gamma-to-Beta
  identity, after which a Gamma density integrates to 1. That leaves no integrability side conditions.

## I — the interior, BUILT

- `first_integral`: `a′² = B + A·a − a²` for `a = (A/2)(1 − cos η) + √B sin η`.
- `first_integral_derived` proves the same from the ODE `a″ + a = A/2` alone.
- `reflection`: `a(−η; −√B) = a(η; √B)`, and `fun_of_a_even` extends it to every function of `a`.
- `sweep`: the receipt's observables, each even. They are `ρ_m`, `ρ_r`, their ratio, `H²`, `a″`, `c_s²`, the
  horizon integrand, the turnaround and the phase.
- The controls: `a′(0)` is odd; `a` and `a′` at fixed `η` are neither even nor odd.
- ***Receipt note:*** its docstring lists ten quantities, but its code checks nine distinct ones (`c_s²` twice). All
  nine are built.

## V — the dust crossing, BUILT

- P3's `r = α sin θ` is odd and P2's `r³` is even. No real `τ` gives `r³ < 0`.
- The offset `τ − iπα/3` gives `r³ = −2Mα² cosh²(3τ/2α)`, in ℂ, and the two continuations agree.
- The density is odd on the signed radius and even on `|r|`. `d|r|/dθ` is odd: infall becomes outflow.
- `crossing_twice`: the crossing `(ρ, v) ↦ (ρ(−l), −v(−l))` is an involution for arbitrary histories, and bijective.
- The signed/unsigned controls hold.
- ***Receipt note, for 69:*** on the even-density, odd-rate class the receipt's comments describe, the crossing is the
  identity (`crossing_fixes_even_odd`). "Involution" has content only for general histories, which is how the
  receipt's code states it.
- `d|r|/dθ` does not exist at `θ = 0`. The oddness there holds by Lean's derivative-zero convention.
- The two paper-text pins are not formalised.

***No disagreement with any receipt on substance.***

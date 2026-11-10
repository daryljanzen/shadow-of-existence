# `r7725+71.1` — PRE-REGISTRATION: campaign 123, **P8's vacuum kernel: the ODE, its general solution, the operator `f ↦ (rf)′` (kernel `span{1/r}`, onto, index 1), the onto matter functional, and `prop:bend`**. ⌗ `400` new lines (band 250–650), p `0.8`. **Expected stop:** 1d's preimage `(1/r)∫_{r₁}^r g`

*Registered before any Lean. The probe is a new standalone file, `probes/OperatorKernel.lean`. It imports only
Mathlib and copies no earlier probe: these rows need nothing from the chain, and not copying it is part of the answer
to 69's item 2. Everything new is prefixed `ok_`. The rows are those of `r7725_71_survey/SURVEY.md`. `8πT^t_t` is
read through eq. `Ttt`: `(rf′ + f − 1)/r² + Λ`.*

## Rows

| Row | Statement (`thm:kernel` l.206, `prop:bend` l.237) | Lines | p |
|---|---|---|---|
| 1b | With eq. `Ttt`'s components (`T^t_t = T^r_r = (rf′ + f − 1)/r² + Λ` and `T^θ_θ = f″/2 + f′/r + Λ`), `T = 0` on an open interval ⟺ `(rf)′ = 1 − Λr²` there. The angular equation is the derivative of the radial one, divided by `2r` | 40–80 | 0.9 |
| 1c | On a preconnected `I ⊆ (0, ∞)` with `f` differentiable on `I`: `rf′ + f − 1 + Λr² = 0` on `I` ⟺ `∃ M, ∀ r ∈ I, f r = 1 − 2M/r − Λr²/3`. Non-vacuity: SdS solves it | 60–120 | 0.9 |
| 1d | On `[r₁, r₂] ⊂ (0, ∞)`, with `L f = (rf)′`: `|Lf| ≤ |f| + r₂|f′|` pointwise (bounded `C¹ → C⁰`); `Lf = 0` on the interval ⟺ `f = c/r` (kernel `span{1/r}`); and for every continuous `g`, `f = (1/r)∫_{r₁}^r g` has `Lf = g` on the interval (onto). So `L` has a one-dimensional kernel and no cokernel: index 1 | 150–300 | 0.75 |
| 1e | The matter functional is onto: for continuous `ρ`, `m(r) = ∫_{r₁}^r 4πs²ρ(s) ds` gives `f = 1 − 2m/r − Λr²/3` with `(rf′ + f − 1)/r² + Λ = −8πρ`, so `T^t_t = −ρ` | 60–120 | 0.85 |
| 2 | `prop:bend`: for differentiable `m`, `f = 1 − 2m/r − Λr²/3` gives `(rf′ + f − 1)/r² + Λ = −2m′/r²`, i.e. `ρ = m′/4πr²` | 30–60 | 0.97 |

**The expected stop** is 1d's preimage at the interval's ends. The plan is to take `g` continuous on `ℝ` (the
interval's `C⁰` functions extend), and use `intervalIntegral.integral_hasDerivAt_right` at every point. **The
fallback** is to state onto-ness on the open interval `(r₁, r₂)`.

**Interpretive, not formalised:** "the index is the mass", and the index's constancy along Fredholm paths.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

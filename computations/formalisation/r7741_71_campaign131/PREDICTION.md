# `r7741+71.1` — PRE-REGISTRATION: campaign 131, **P15's horizon rows: 1 (the comoving Hubble scale), 4 (the Nariai throat), 6 (the tortoise dichotomy) and 7 (the finite tortoise length at the branch point)**. ⌗ `380` new lines (band 250–600), p `0.7`. **Expected stop:** row 7's integrability of `1/f` at `r = 0`

*Registered before any Lean. The inventory is `r7741_71_survey/SURVEY.md`.*
- **The probe** is a new standalone file, `probes/Cosmology.lean`, prefix `cm_`. It imports only Mathlib. Campaign 132
  appends to it, so it becomes P15's citable file.
- **Notation:** `f(r) = 1 − 2M/r − r²/α²`, with `α > 0` and `Λ = 3/α²`.

## Rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 1a | `ṙ = √(2M/r + r²/α²) → ∞` as `r → 0⁺`, for `M > 0` | 30–60 | 0.9 |
| 1b | `k/ṙ → 0` as `r → 0⁺`, for every `k` | 10–20 | 0.95 |
| 4a | At `M = α/(3√3)` (`ΛM² = 1/9`), `r_N = α/√3`: `f(r_N) = 0`, `f′(r_N) = 0`, `f″(r_N) = −2Λ`; `f(r) = −(r − r_N)²(r + 2r_N)/(α²r)`, so `r_N` is the only positive root | 60–120 | 0.85 |
| 4b | `2/r_N² = 2Λ` and `−2/f″(r_N) = 1/Λ`: both radii² are `1/Λ` | 20–40 | 0.9 |
| 6a | `f = 2κ(x − x_h)`, `κ > 0`: `r* = ln(x − x_h)/(2κ)` has `dr*/dx = 1/f` for `x > x_h`; `x − x_h = e^{2κ r*}`; `r* → −∞` as `x → x_h⁺` | 30–60 | 0.9 |
| 6b | `f = −Λ(x − x_N)²`: `r* = 1/(Λ(x − x_N))` has `dr*/dx = 1/f` for `x ≠ x_N`; `x − x_N = 1/(Λr*)`; `r* → +∞` as `x → x_N⁺` | 30–60 | 0.9 |
| 7 | For `M > 0`, `1/f(r) = r/(r − 2M − r³/α²)` tends to `0` as `r → 0⁺`. On `(0, ε]` with `ε` below the first horizon, `1/f` is bounded and `IntervalIntegrable` on `[0, ε]`, so `r* = ∫₀^ε dr/f` is finite | 60–150 | 0.75 |

**Non-vacuity:** 4a at a concrete `α`; 6a and 6b at concrete `κ` and `Λ`; 7 at `M = 1`, `α = 3`, with an explicit `ε`.

**The expected stop** is row 7: choosing `ε` below the cosmological horizon, and the bound on `1/f` there. **The
fallback** is the limit `1/f → 0` and continuity on `[0, ε]` without the integral, with row 7 marked BUILT IN PART.

**Interpretive, not formalised:**
- "every mode leaves the horizon";
- "scale-free transmitter";
- the throat's no-hair reading;
- the `a″/a` constants.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

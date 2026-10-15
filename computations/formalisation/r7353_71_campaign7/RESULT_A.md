# `r7353+71.2` — RESULT, piece A: row 58 is built as exact algebra, `81` lines against `80`, in `9 s`. ⌗ The ADM kinetic scalar's `ε⁰`, `ε¹` and `ε²` coefficients are `−6h²`, `0` and `+¼tr(Ḣ²)`, the receipt's gate ⓐ, for any `H` whose velocity is traceless. ⌗ Open half: the measure gate `det exp(εH) = 1`, and the Legendre transform the receipt draws from the sign. Piece B is still to come

*Scored against `PREDICTION.md` in this directory (pushed at `r7353+71.1`). It is not revised. One new axiom line,
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`).*

| piece | registered | measured | outcome |
|---|---|---|---|
| A, row 58 | `80` lines (band 40–170); under `30 s` | ***`81`*** lines; ***`9 s`*** | ***BUILT IN PART***, in the band; p `0.8`: ***yes*** |

## What is proved (`probes/Campaign7.lean`)

- ***The setting:***
  - `expT s H` is the receipt's own `NORD = 3` truncated `exp(sεH)`, and `expTd` is its exact time derivative.
  - `Mgg = expT(−1)·(2h·expT(1) + expTd)` is `γ⁻¹γ̇` with the receipt's truncated inverse.
  - All of these are polynomials in `ε = X` with `3 × 3` matrix coefficients.
- ***The scalar:*** `kinADM = ¼[tr(M²) − (tr M)²]` is `K^i_jK^j_i − K²` with `K^i_j = M/2`. It is a real
  polynomial, through `trX`, the coefficientwise trace.
- ***`Mgg_coeffs`:*** `M₀ = 2h·1`, `M₁ = Ḣ`, `M₂ = ½[Ḣ, H]`, exactly.
- ***`row58_adm_kinetic`:*** the coefficients are `−6h²`, `0` and `tr(Ḣ²)/4`.
  - The `ε¹` part vanishes because `tr Ḣ = 0`.
  - The `ε²` part is `¼tr(Ḣ²)` because `tr[Ḣ, H] = 0` kills the `h` cross-term, which is the reason the receipt's
    sign is clean.

## Caveats beside the score

- ***More general than the receipt:*** the receipt takes `H` symmetric, transverse-traceless, in five component
  functions. The proof needs only `tr Ḣ = 0`. Neither symmetry nor `tr H = 0` is used.
- ***Open half, named:***
  - (i) the receipt's first gate, `det exp(εH) = 1` so `√γ = a³`. `mathlib` has no `det_exp`, and `Mgg` lives in
    `Mat[X]`, not in matrices over `ℝ[X]`, so the determinant is not reached by this construction.
  - (ii) the Legendre transform and the Hamiltonian sign the receipt draws from the positive kinetic term. That is
    an argument about the action, not this identity.
- ***Survival:*** no reading this block. Row 58's survived at `r7351`.

## Census (moved in this push)

| status | after `r7351+71.6` | now |
|---|---|---|
| DONE | `43` | `43` |
| DONE (chartable half) | `12` | ***`13`*** (+ 58) |
| GENERIC-METRIC IDENTITY | `4` | ***`3`*** (6, 20, 62) |
| real end | `20` | `20` |

***Piece B*** (row 83 at every `y`) is next. It is pushed when it lands, or named as compiling.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

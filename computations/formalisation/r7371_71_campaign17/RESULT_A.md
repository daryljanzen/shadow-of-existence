# `r7371+71.5` — RESULT: campaign 17 BUILT. ⌗ Row 7 is DONE. A trace-free symmetric `3 × 3` shear has exactly five independent components (`Module.finrank = 5`), and the Hamiltonian constraint gives `ρ = R₃/2 + θ²/3 − tr(σ²)/2`, which every nonzero shear lowers. ⌗ `102` lines against `70` (band 35–160, ⛔ stop `200`): in the band. ⌗ `7 s` against under `1` minute

*Scored against `PREDICTION.md` in this directory (pushed at `r7371+71.4`, before the build). It is not revised.
Every axiom line is `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`). New file:
`probes/Row7Count.lean`. No pre-opening reading was registered, so the running rate stays `15` of `22`.*

## ⛔ The stop, scored first

***Not fired.*** `102` lines, under `200`.

## What was built

| piece | theorem | what it proves |
|---|---|---|
| the count | `tfSym_finrank` | the trace-free symmetric `3 × 3` real matrices are a subspace of dimension `5`, by an explicit linear equivalence with `Fin 5 → ℝ` (`tfSymEquiv`) |
| the sign | `adm_rho` | with `R₃ + K² − K_ijK^ij = 2ρ`, `K = (θ/3)·1 + σ`, `tr σ = 0`: `ρ = R₃/2 + θ²/3 − tr(σ²)/2` |
| | `tr_sq_sym` | for symmetric `σ`, `tr(σ²) = Σσᵢⱼ²`, zero only at `σ = 0` |
| | `adm_rho_shear_lowers` | at fixed `R₃, θ`, `ρ` strictly decreases in `tr(σ²)`, and every nonzero symmetric shear gives `ρ < R₃/2 + θ²/3` |

- `adm_trace_split` (`Campaign6A.lean`) is re-proved inline in `adm_rho`: probes do not import each other.
- ***Not built, as registered:*** the Gowdy count (that a polarized Gowdy leaf's shear is ONE function). The receipt
  pins it from the paper's text and computes nothing for it.
- The registered risk (no ready Mathlib lemma for the dimension) was met by the explicit equivalence, which took
  `≈ 35` lines.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 17 BUILT under its stop | `0.7` | ***yes***, `102` |

## Census (moved in this push)

Row 7: `DONE (chartable half)` → ***`DONE`***, its text naming the four declarations and the count not built.
***Counts, checked:*** DONE ***`54`***, halves ***`2`*** (77, 108), generic-metric `2`, no-connection `32`, library
gap `17`, real obstruction `4`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

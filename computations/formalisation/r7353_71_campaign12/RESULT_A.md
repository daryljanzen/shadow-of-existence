# `r7353+71.16` — RESULT: campaign 12 BUILT. ⌗ Row 19 is DONE. The running-layer comparison holds under THE connection: on flat FRW, for EVERY `a(T)` and arbitrary counterterm coefficients, `a₁Riem² + a₂Ric² + a₃R² = ((3a₃ − a₁)/2)·GB − 4sΛ² + 2sΛR + s·ΣE²`, with remainder zero. As a background-independent identity it holds for any curvature data, with `GB` coefficient `a₁`. ⌗ `167` lines against `110` (band 55–200, ⛔ stop `250`): in the band. ⌗ `18 s`, no table

*Scored against `PREDICTION.md` in this directory (pushed at `r7353+71.15`). It is not revised. Every axiom line is
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`). New file:
`probes/RunningLayer.lean`.*

## ⛔ The stop, scored first

***Not fired.*** `167` lines, under `250`. Over the `110` point estimate by `52%`. The overrun is item A, which had to
be split into four lemmas (see below).

## What was built, against the registered pieces

| piece | theorem | what it proves | registered |
|---|---|---|---|
| A | `frw_invariants` (with `frw_ric_off`, `frw_ric_diag`, `frw_riem2`) | flat FRW, free `a`, THE connection: mixed Ricci `diag(3(Ḣ + H²), Ḣ + 3H² ×3)`, off-diagonal `0`; `Riem²`, `Ric²` and `R` are the receipt's three polynomials | ✔ |
| B | `tv_identity` | `(7/20)tr M² + (1/120)R² = tr(E f)` for ANY `4 × 4` mixed Ricci `M` | ✔ |
| C | `ledger_general` | `a₁Riem² + a₂tr M² + a₃R² = a₁E_GB + (a₂ + 4a₁)(tr E² + 2ΛR − 4Λ²) + (a₃ − a₁)((tr E)² + 8ΛR − 16Λ²)` for ANY data | ✔ |
| D | ***`ledger_layer`*** | on flat FRW under THE connection: `((3a₃ − a₁)/2)·GB − 4sΛ² + 2sΛR + s·Σⱼ(E^j_j)²`, `s = a₁ + a₂ + 3a₃` | ✔ |
| E | `ledger_ds_point` | at `Ḣ = 0` and `H² = Λ/3`: `R = 4Λ` and `Σⱼ E^j_j = 0` | ✔ |

***Item 1 of the receipt*** (`Weyl² = 0` on the running layer, `R` runs, `R → 12/α²`) is the engine's `frw_weyl`,
`frw_scal`, `layer_scal` and `layer_late`. It was cited, as registered, and not rebuilt.

***The decisive piece (D)*** shows what the background-independent form (C) does not. On the layer, `Riem²` is
not independent: `Weyl² = 0` there. So the receipt's `GB` coefficient is `(3a₃ − a₁)/2`, not `a₁`. Both forms have
remainder zero for every `a₁, a₂, a₃`, which is the receipt's "coefficient-independent".

***A note on (D)'s `ΣE²`:*** it is `Σⱼ(E^j_j)²`, the receipt's `E0² + 3Ei²`. It equals `E_mn E^mn` because the
mixed Ricci of flat FRW is diagonal (`frw_ric_off`), which is proved, not assumed.

## Caveats beside the score

- ***Cited, not derived:***
  - the 't Hooft–Veltman / Gilkey coefficients (`53/90`, `7/20`, `1/120`). B uses `7/20` and `1/120` only as the
    receipt's instance, and C and D are coefficient-independent;
  - `∫√g E_GB = 32π²χ`. Row 19's other half (`r7353+71.10`) is the local total-derivative form on FRW.
- ***A reading, not a theorem:*** "removable by a metric field redefinition" is the physics reading of
  "proportional to `E`". What is proved is the proportionality.
- ***Dimension:*** B and C fix dimension `4`, where `tr 1 = 4`. That is the receipt's setting.
- ***Mixed form:*** B and C are stated for the mixed tensor `M = g⁻¹Ric`, so `tr M² = Ric_mn Ric^mn` uses the
  symmetry of Ricci. That symmetry holds for THE connection, but B and C do not reprove it.

## Compile time

| | registered | measured |
|---|---|---|
| wall | under `2` minutes (no table) | ***`18 s`*** |

The first attempt at A, as one theorem, hit the `200000`-heartbeat limit. Split into `frw_ric_off`, `frw_ric_diag`
and `frw_riem2` (the last under `maxHeartbeats 1600000`), with `Ric²` and `R` read off the mixed Ricci rather than
re-expanded, it builds in `18 s`.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 12 BUILT under its stop | `0.7` | ***yes***, `167` |

## Census (moved in this push)

Row 19: `DONE (chartable half)` → ***`DONE`***, with the caveats above in its text, as registered. ***Counts,
checked before the commit:*** DONE ***`47`***, halves ***`10`***, generic-metric `2` (20, 62), library gap `17`,
no-connection `32`, real obstruction `3`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

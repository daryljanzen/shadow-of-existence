# `r7411+71.7` — RESULT: campaign 21 BUILT, all nine pieces. ⌗ The `S³` frame core: the Milnor formula, `Ric = 2δ` and `R = 6`, the TT eigenvalue `−∇²h = 6h`, the constant-curvature TT action, `tr h³ = 3 det h`, the Euler-box volume `2π²`, `ζ(0) = 10`, the half-line integral and the mode equation. ⌗ `152` lines against `260` (band 150–500, ⛔ stop `600`): inside, near the floor. ⌗ `17 s`. ⌗ Rows 65, 66, 67 → DONE (chartable half)

*Scored against `PREDICTION.md` in this directory (pushed at `r7411+71.6`, before the build). It is not revised.
All 11 declarations print `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` and no warning
(`PROBE_RUN_A.txt`). New file: `probes/S3Frame.lean`. Built on Daryl's instruction.*

## ⛔ The stop, scored first

***Not fired.*** `152` lines, under `600`.

## What was built

| piece | theorem | what it proves | rows |
|---|---|---|---|
| 3 | `milnor_scalar` | for every left-invariant metric `diag λ` on su(2), the Koszul connection's scalar curvature is `2(4e₂ − e₁²)/e₃` | 65, 66 |
| — | `kos_unit` | at `λ = 1` the Koszul connection is `∇_{E_a}E_b = ε_abc E_c` | 67 |
| 2 | `s3_ricci` | the unit `S³`: `Ric = 2δ`, `R = 6` | 65, 66 |
| 1 | `s3_tt_eigen` | `−∇²h = 6h` for EVERY frame-constant symmetric traceless `h` | 66, 67 |
| 4 | `const_curv_tt` | `R_ikjl h^kl = −K h_ij`, `Ric = 2Kδ`, `R = 6K` | 65 |
| 5 | `traceless_cube` | `tr h³ = 3 det h` for traceless `3 × 3` (any, not only symmetric) | 66, 67 |
| 6 | `det_frame_conj` | `det(e⁻¹He) = det H` | 67 |
| 7 | `euler_volume` | `∫₀^{2π}∫₀^π∫₀^{4π} sinθ/8 = 2π²` | 66, 67, 59 |
| 8 | `zeta_count` | `2[(ζ(−2) − 5) − 4(ζ(0) − 2)] = 10` from Mathlib's `ζ(0) = −1/2`, `ζ(−2) = 0` | 65 |
| 9 | `halfline_integral`, `tt_mode_eom` | `∫₁^∞ q^{−4/3} = 3`; `(a³φ′)′ + 8aφ = a³(φ″ + 3Hφ′ + 8φ/a²)` | 66, 65 |

- ***Pieces 1 and 3 are the receipts' own method.*** The receipts get `−∇² = 6` and the Milnor formula from
  Levi-Civita contractions on the structure constants, and that is what these theorems do. No Euler coordinates
  are used.

## Caveats, beside the score

- ***Lines came in near the floor*** (`152` of a 150–500 band). Pieces 3 and 7 were the registered risks, and each
  closed in one `simp`/`field_simp` or `intervalIntegral` step. ***The band was priced for risks that did not bite.***
- ***Not built, as registered:***
  - the Euler-chart COORDINATE checks, which need a non-diagonal `Fin 3` instance (66, 67);
  - the `ε`-series of `R(exp εH)` and the split algebra (66);
  - the floating cutoff slope (65);
  - the deficiency claim (66, prose);
  - the imported TT spectrum (the spectral library gap).
- ***Row 59 stays `ORDER`.*** Only the box integral and the constant-`H` floor are built here. Its jet ranks, its
  Euler-chart fields and its non-constant integrals are still to build, and its row says so.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| all nine pieces built under the stop | `0.6` | ***yes***, `152` |

## Census (moved in this push)

Rows 65, 66, 67: `ORDER: ENGINE-REACHABLE` → ***`DONE (chartable half)`***, each naming its declarations and its
open half. Row 59's text gains what is built. ***Counts, checked:*** DONE `72`, halves ***`3`***, ORDER (engine)
***`2`*** (59, 95), LIMIT `10`, ROW `5`, generic-metric `2`, library gap `17`. Total `111`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

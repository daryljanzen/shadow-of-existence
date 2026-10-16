# `r7411+71.5` — RESULT: campaign 20 BUILT, all 16. ⌗ The no-connection sweep: every ORDER row that waited on nothing but Mathlib is now a theorem, as its receipt computes it. ⌗ `413` lines against `400` (band 250–700, ⛔ stop `850`): in the band, on the point. ⌗ `8 s`. ⌗ DONE `56` → `72`

*Scored against `PREDICTION.md` in this directory (pushed at `r7411+71.4`, before the build). It is not revised.
All 24 declarations print `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` and no warning
(`PROBE_RUN_A.txt`). New file: `probes/NoConnectionSweep.lean`. ***Built on Daryl's instruction***, which overrides
`r7383` ②'s "do not build" for these 16, as the registration said.*

## ⛔ The stop, scored first

***Not fired.*** `413` lines, under `850`.

## What was built

| row | theorem(s) | what it proves |
|---|---|---|
| 14 | `frw_cycloid` | `M(1 + cos(π − η)) = (A/2)(1 − cos η)` at `M = A/2`; `a′(0) = 0`, `a″(0) = A/2` (a non-degenerate critical point) |
| 15 | `ltb_turnaround` | `−m/E > 0` for `E < 0` and `< 0` for `E > 0`; the bound cycloid is the circle's |
| 16 | `ltb_turnaround_time` | `d/dE log(πm/(2E)^{3/2}) = −(3/2)/E` |
| 25 | `schw_charts`, `schw_pg_shift` | EF: `−f dv² + 2 dv dr`; PG: `−f dT² + 2s dT dr + dr²` when `s² = 1 − f`, with `s = √(r_h/r)` for Schwarzschild |
| 27 | `circle_continuation` | `cos(iρ) = cosh ρ`, `sin(iρ) = i sinh ρ`; `1 − 2M/r = tanh²(ρ/2)`; `(dr/dρ)²/(1 − 2M/r) = 4M² cosh⁴(ρ/2)`; `r(π + iρ) = M(1 − cosh ρ)` |
| 30 | `interior_cycloid`, `interior_gtt_zero` | `−(1 − 2M/r) = tan²(η/2)`; `g_rr r′² = −4M² cos⁴(η/2) = −τ′²`; `g_tt → 0` as `η → 0⁺` |
| 31 | `three_axes` | `Im M(1 + cos(a + ib)) = −M sin a sinh b`, zero iff `sin a = 0` or `b = 0`; the values on the axes; parity. ***The "exactly three axes" step the receipt only states is proved here*** |
| 33 | `rnds_parity`, `rnds_core`, `schw_core_minus` | the `M ↦ −M` split, `Q`-invariance and the cleared quartic; `f → +∞` as `r → 0⁺` when `Q ≠ 0`, and `→ −∞` when `Q = 0`, `M > 0` |
| 37 | `throat_join` | `sin(π/2 + iψ) = cosh ψ`; `i² = −1`; the join is `C¹` and not `C²` (`−1` against `+1`) |
| 39 | `hinge_interval` | `√((4α)² − α²) = √15 α`; the point is on the hyperboloid; `s² = 4α² − ρ²`, zero at `ρ = 2α` |
| 50 | `flat_on_quadric`, `flat_dtau`, `flat_dx`, `flat_induced`, `flat_horosphere` | the flat-slicing chart lies on `η(X, X) = α²`; its derivatives, PROVED as derivatives; `g_ττ = −1`, `g_xx = e^{2τ/α}`, `g_τx = 0`; `A`, `B` null with `η(A, B) = α²/2`; `η(X, B) = (α²/2) e^{τ/α} → 0` as `τ → −∞` |
| 61 | `ef_det`, `ef_horizon_degenerate`, `ef_horizon_rank` | `det g = −r⁴ sin²θ`; the horizon metric `diag(0, r_h², r_h² sin²θ)` has `det 0`, kills `∂_v`, and has rank `2` off the poles |
| 87, 88, 90 | `axis_vantage` | `X0² = −α²` has no real root and over `ℂ` exactly `±iα` (real parts `0`, sum `0`); the power of a point at `2α, α, 0`; `−(√3α)² + (2α)² = α²` |
| 107 | `confocal_degree` | the cleared confocal numerator has `natDegree 3` (leading coefficient `−1`), and `1` when the `aᵢ` coincide |

## Caveats, beside the score

- ***Not built, as registered (stated limits):***
  - 33's floating root counts;
  - 39's printed 51-pair table, which its receipt does not assert;
  - 30's `η → π⁻` limit, which I did not build. It is a stated limit of the row and is named in the row.
- ***50's `y` and `z` derivatives are not separate theorems.*** The chart is symmetric in `x, y, z` and only `∂_x` is
  proved. The receipt computes all three, so `g_yy`, `g_zz` and the off-diagonal spatial entries are by symmetry here,
  not by proof.
- ***88's receipt asserts no mathematics*** (only its own table's shape). What is built is the identity it prints.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| all 16 built under the stop | `0.7` | ***yes***, `413` |

## Census (moved in this push)

16 rows `ORDER: NO-CONNECTION, REACHABLE` → ***`DONE`***, each naming its declarations. ***Counts, checked:*** DONE
***`72`***, ORDER (engine) `5`, LIMIT `10`, ROW `5`, generic-metric `2`, library gap `17`. Total `111`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

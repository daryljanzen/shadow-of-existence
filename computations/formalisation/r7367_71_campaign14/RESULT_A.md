# `r7367+71.3` — RESULT: campaign 14 BUILT. ⌗ Row 79 is DONE. SdS's static leaves have `K_ab = 0` under THE connection. The leaf's own 3-metric has `³R = 2(1 − F − rF′)/r²` on the `Fin 3` engine, and `6/α²` for SdS, independent of `M`. ⌗ `170` lines against `140` (band 70–280, ⛔ stop `340`): in the band. ⌗ `12 s` against `1–3` minutes registered. ⌗ ***The pre-opening reading SURVIVED (p `0.55`): running rate `15` of `22`***

*Scored against `PREDICTION.md` in this directory (pushed at `r7367+71.2`, before the receipt was opened). It is not
revised. Every axiom line is `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`). New
file: `probes/Row79Leaf.lean`.*

## ⛔ The stop, scored first

***Not fired.*** `170` lines, under `340`.

## The pre-opening reading, scored first among the claims

| row | my reading | p | survived? |
|---|---|---|---|
| 79's half | SdS `f = 1 − 2M/r − r²/α²`, the `t = const` leaves: `K_ab = 0`, and `³R = 6/α² = 2Λ` | `0.55` | ***yes*** |

- ***What the receipt says:*** `E1_static_gauge.py` takes exactly that `f`. It derives `K_ab = 0` from the
  vanishing Christoffels, with the control `Γ^t_tr ≠ 0`. It pins `R3 − 6/α² = 0` and `∂_M R3 = 0`, by the Hamiltonian
  constraint argument I gave.
- ***Running rate: `15` of `22` (`0.68`).*** This is the first reading since `r7351`. It tests the forward price as
  `r7367` ② asked: a `0.55` that came true. One reading cannot move the rate's error, and it is said to be one.

## What was built

| piece | theorem | what it proves |
|---|---|---|
| (a) | `sds_leaf_K_zero` | `Γ^t_ab = 0` for spatial `a, b`, for SdS's static 4-metric with ANY profiles `F, P, S`: the leaves are totally geodesic |
| (b) | `leaf_scal` | the leaf 3-metric `dr²/F + P(dθ² + S dφ²)` on `ℝ³`, under THE connection on the `r7341` `Fin 3` port, with `P = r²` and `S = sin²θ` near the point: `³R = 2(1 − F − rF′)/r²` for ANY `F` |
| (b) | `sds_leaf_R3` | SdS's `F` gives `6/α²`, and `M` drops out |

- The near-point convention covers the sphere profile and `P`, as in `tangherlini5_kernel`. `exists_global_profile`
  (engine) builds the global profiles it assumes.
- `F` is any smooth nonvanishing profile, so the result holds on every static region of SdS, inside either horizon.

## Compile time

| | registered | measured |
|---|---|---|
| wall | `1–3` minutes (`81` cases, `m ≈ 1.5`) | ***`12 s`*** |

- ***The price was wrong by about `10×`, in the direction `r7351` found for non-diagonal tables at a numeric point.***
- The `81` "cases" here are not a `fin_cases` table. The scalar is ONE contraction, closed by one `simp`, one
  `field_simp` and one `ring`, as in `tangherlini5_Gtt`.
- So the table-size axis does not apply to a scalar-only instance. The axis prices `fin_cases` tables (`fRk`,
  `D2_tab`), and this file has none.
- I priced the wrong axis. That is a pricing error, said here.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 14 BUILT under its stop | `0.65` | ***yes***, `170` |
| the reading survives | `0.55` | ***yes*** |

## Census (moved in this push)

Row 79: `DONE (chartable half)` → ***`DONE`***, its text naming the three declarations. ***Counts, checked:***
DONE ***`51`***, halves ***`6`*** (7, 17, 35, 59, 77, 108), generic-metric `2`, no-connection `32`, library gap
`17`, real obstruction `3`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

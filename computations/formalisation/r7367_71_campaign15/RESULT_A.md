# `r7367+71.5` — RESULT: campaign 15 BUILT. ⌗ Row 17 is DONE. SdS's Kretschmann scalar is computed AT the Nariai horizon point, where `f = f′ = 0` and the static chart fails. In the ingoing Eddington–Finkelstein chart, THE connection gives `K = F″² + 4F′²/r² + 4(1 − F)²/r⁴` for ANY `F`. That is `48M²/r⁶ + 24/α⁴` for SdS at every `r`, horizons included, and `72/α⁴` at `r_N = 3M` when `α² = 27M²`: the receipt's value. ⌗ `281` lines against `350` (band 180–550, ⛔ stop `650`). ⌗ `435 s` for the whole file. Registered `5–25` minutes

*Scored against `PREDICTION.md` in this directory (pushed at `r7367+71.4`). It is not revised. Every axiom line in the
file, row 83's included, is `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` and `0` error lines
(`PROBE_RUN_A.txt`). The new code is `section EFNariai` of `probes/NonDiag.lean`. The table generator is
`gen_ef_tables.py` beside this file, committed at `r7367+71.4` (`4ee54c66c`) before the build that used it.*

## ⛔ The stop, scored first

***Not fired.*** `281` lines in the section, under `650`.

## What was built

| piece | what it proves |
|---|---|
| `GE` | the ingoing EF metric `−F dv² + 2 dv dr + P(dθ² + S dφ²)`, written as `eF·F + eO + eP·P + eQ·P·S` with numeric `e*`, so ONE derivative lemma covers every entry (`GE_fd1`, `GE_fd2`) |
| `GE_nondeg` | nondegenerate at every point for EVERY `F`. The `(v, r)` block `[[−F, 1], [1, 0]]` has determinant `−1`, so the chart covers `F = 0` |
| `GiE_inv` | the inverse at the point, `(v, r)` block `[[0, 1], [1, F]]` |
| `D1E_tab`, `D2E_tab`, `GamE_tab`, `DGamE_basis`, `GamGamE` | the derivative and Christoffel tables, each entry checked |
| ***`RE_tab`*** | THE connection's `R(eᵢ, eⱼ)eₖ`, all `256` entries checked, through `curvG_eq` |
| ***`RUE_tab`*** | `R_a^{bcd}`, lowered with `G` and raised with `Gi`, all `256` entries checked |
| `kret_tab` | `K = Σ R^a_{dbc} R_a^{dbc} = F″² + 4F′²/r² + 4(1 − F)²/r⁴`, a `256`-term contraction, never the `65,536`-term eight-index sum |
| ***`ef_kretschmann`*** | the same, stated for `curv (lcConn …)` of the EF metric: THE connection, for ANY smooth `F` |
| `sds_kretschmann_ef` | SdS's `F = 1 − 2M/r − r²/α²`: `48M²/r⁶ + 24/α⁴` at every `r ≠ 0`, horizons included |
| ***`nariai_horizon_kretschmann`*** | at `α² = 27M²`, `r_N = 3M` (`= α/√3`): `F(r_N) = 0`, `F′(r_N) = 0` and `K = 72/α⁴` |

***Why this closes the half:***
- The census's open half was "SdS `K` AT the horizon point `r_N`, where `f = 0` and the static chart fails". At
  Nariai, `f` has a DOUBLE zero there.
- Every static-chart result (`sds_kretschmann`, the row-45 table) needs `1/F`, so none applies at `r_N`.
- The EF chart needs no `1/F` and is nondegenerate there (`GE_nondeg`). So `K(r_N) = 72/α⁴` is THE connection's
  value at that point, not a limit.

## Caveats beside the score

- ***The near-point convention*** for `P = r²` and `S = sin²θ`, as in every sphere-carrying instance.
  `exists_global_profile` builds the global profiles. `F` is ANY smooth function, with no convention: it may vanish.
- ***The generated tables:*** `gen_ef_tables.py` uses rational normalisation only (`cancel`), never trigonometric
  simplification. So each entry closes in Lean by `field_simp`/`ring` alone, and the generator is committed.
- ***A slip in the registration, caught before it was pushed:*** a first draft of item 4 used `F″ = −2/α²` (dropping
  the `M` term) and got `40/α⁴`. A sympy check caught it before the commit. `PREDICTION.md` records this in its own
  text.

## Compile time

| | registered | measured |
|---|---|---|
| the whole file | `5–25` minutes (the EF section on top of `349 s` for row 83) | ***`435 s`*** |
| the EF section alone (scratch builds without row 83) | — | `≈ 200 s` (`3m19s`, `3m22s` on two runs) |

- The EF section's `≈ 200 s` covers three `256`-entry and two `64`-entry symbolic tables, at about `0.3 s` per checked
  entry.
- That is `m ≈ 0.4` on the `0.73 s` axis, inside the `r7353` non-diagonal multiplier of `0.5`.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 15 BUILT under its stop | `0.5` | ***yes***, `281` |

*No pre-opening reading was registered: row 17's receipt was opened at `r7333`. The running rate stays `15` of `22`.*

## Census (moved in this push)

Row 17: `DONE (chartable half)` → ***`DONE`***, its text naming the declarations. ***Counts, checked:*** DONE
***`52`***, halves ***`5`*** (7, 35, 59, 77, 108), generic-metric `2`, no-connection `32`, library gap `17`, real
obstruction `3`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

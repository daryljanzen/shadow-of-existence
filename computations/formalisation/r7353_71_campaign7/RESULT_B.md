# `r7353+71.3` — RESULT, piece B: row 83's open half is closed. THE connection of the squashed `S⁵` has `R = 24 − 4t²` at EVERY point of the chart, not only at `y = 0`. ⌗ `103` lines against `250`, under the band (120–400). ⌗ Compile time: about `0.33 s` per case against a registered multiplier of `3`, wrong in the same direction as `r7351+71.6`. ⌗ Row 83 is DONE. DONE `44`, halves `12`

*Scored against `PREDICTION.md` in this directory (pushed at `r7353+71.1`). It is not revised. Every new axiom line is
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_B.txt`).*

| piece | registered | measured | outcome |
|---|---|---|---|
| B, row 83 at every `y` | `250` lines (band 120–400, ⛔ stop `500`); `≈ 35` min | ***`103`*** lines; see the compile section | ***BUILT***. p `0.45` under the stop: ***yes***. Under the band, not in it |

## What is proved (`probes/NonDiag.lean`, appended to `section SquashedS5`)

- ***The chart identities:***
  - `mu_two`: `μ₂ = 1 − μ₀ − μ₁`.
  - `GiG_inv`: the inverse at every `y`, `4(diag μ⁻¹ + J/μ₂)` on the base and `δ/μ − (t² − 1)/t²` on the fibre.
- ***The tables at a general point:*** `D1G_tab` (125 cases), `D2G_tab` (625) and `GamG_tab` (125) are in
  `μ₀(y)`, `μ₁(y)`. `RicG_tab` (25) is polynomial in them.
- ***`row83_squashed_S5_everywhere`:*** for every `t ≠ 0` and every `y ∈ ℝ⁵`, `scalG (GiG …) (curv (lcConn …) … y) =
  24 − 4t²`.

***Why this closes the half without homogeneity:*** the chart is all of `ℝ⁵`, and the value is proved at each of its
points. It covers the open dense set `{|z₁|, |z₂|, |z₃| ≠ 0}` of `S⁵` modulo the torus angles. The `SU(3)` action
is not needed for the receipt's claim, `R_t = 24 − 4t²`.
- ***Caveat, named:*** the points where some `zₐ = 0` lie outside the chart. There `R` is the same by continuity,
  but that is not proved.

## Compile time (the table-size axis)

| | registered | measured |
|---|---|---|
| per case | `0.73 s × m`, `m = 3` | ***`≈ 0.33 s`***: `309 s` for a development file holding the engine and only the general-point tables (`950` cases) |
| whole file (both sets of tables, `1900` cases) | — | ***`349 s`*** |

- ***`m` registered `3`, measured `≈ 0.45`.*** My reading was that rational entries in four symbols would cost
  several times a numeric table. They cost about the same.
- The entries the tactics meet are short, because the tables are factored by sympy and checked case by case. It is
  the second miss of the multiplier in the same direction. ***From here a non-diagonal table is priced at `m = 0.5`,
  numeric or symbolic, until a measurement says otherwise.***
- *The ten-second-per-case split rule registered in ③ never fired.*

## Census (moved in this push)

| status | after `r7353+71.2` | now |
|---|---|---|
| DONE | `43` | ***`44`*** (+ 83) |
| DONE (chartable half) | `13` | ***`12`*** (− 83) |
| GENERIC-METRIC IDENTITY | `3` | `3` (6, 20, 62) |
| real end | `20` | `20` |

***Campaign 7:*** A (`81`) + B (`103`) = ***`184`*** lines against `330` registered. Both pieces are built: A in
part, B whole.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

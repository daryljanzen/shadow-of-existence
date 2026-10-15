# `r7337+71.3` — RESULT: the reopened block is CLOSED, with reopenable now at `0`, so `70`'s return trigger has fired. ⌗ Row 59 splits. Its pointwise identity is a `3 × 3` matrix identity, proved in `32` lines with no connection; its `S³` integrals are global. Row 62 is NOT reachable as a product with a line, and my reading was wrong: it is a frame-based, non-diagonal jet expansion, reclassified as a generic-metric identity. ⌗ I take campaign 3 next. Compile time is set by table size, and the evidence so far supports that, with one caveat

*Scored against `PREDICTION.md` in this directory (pushed at `r7337+71.1`, before `70`'s routing note or either
receipt was opened). It is not revised.*

## ① The last rows

| row | registered reading | p | outcome | scored |
|---|---|---|---|---|
| 72 | landed by `70` (taken as given) | — | ***DONE***, by `70` at `r7335+70.2` | — |
| 59 | reclassified as no-connection algebra, built if under `60` lines | `0.5` | ***its headline identity is algebra, BUILT at `32` lines.*** Its `S³` part is global. Status: DONE (chartable half) | ***right*** for the identity; the split was not foreseen |
| 62 | reachable through a product with a line (`R⁴ = R³`) | `0.55` | ***not reachable.*** The obstruction is not the dimension: it is a left-invariant FRAME on `S³` with a NON-DIAGONAL metric `exp(εH)`, expanded to `ε⁴` over jets. Reclassified as a GENERIC-METRIC IDENTITY | ***wrong*** |

- ***Row 59, built*** (`probes/Row59Quartic.lean`; Mathlib only, no engine):
  - `quartic_identity`: `tr h⁴ − ½(tr h²)² = p₁(⁴⁄₃p₃ − p₁p₂ + ⅙p₁³)` for EVERY `3 × 3` real matrix. The receipt
    states it for symmetric `h`; symmetry is not needed.
  - `quartic_traceless`: on a traceless `h`, `tr h⁴ = ½(tr h²)²`.
  - These are the receipt's ⓐ, and the reason its algebraic sector is rank one at every level.
  - ***Not built:*** the tower's labels against the `S³` transverse-traceless harmonics, the integrals, and the
    ranks. They are global on `S³`, the same obstruction as rows 65–67.
- ***Row 62, why my reading failed:***
  - I read "scalar curvature on `S³` frame jets" as a diagonal `S³` metric in coordinates, which a product with a line
    would have carried into 4D.
  - The receipt's object is `R[exp(εH)]` in the left-invariant orthonormal frame, with structure constants
    `C^c_ab = 2ε_abc`. `H` is a general symmetric perturbation, and the claims are ranks of `1104` contractions over
    jets.
  - That needs a non-diagonal metric (campaign 6), a frame rather than coordinates, and a jet expansion. None of
    these is a chart question.
  - ***`70`'s routing ("outside a 4D diagonal engine") is right, and it is not my registered reason.***
- ⚠ `70` found that row 62's receipt overwrites `CHECKS[2]` at line 451. That belongs to the receipt's owner. It is
  not mine to fix and I have not touched it.

***The census*** (`ROWS.tsv`):

| status | after `r7335` | now |
|---|---|---|
| DONE | `38` | ***`39`*** (+ 72) |
| DONE (chartable half) | `6` | ***`7`*** (+ 59) |
| CHART-EXCLUDED → REOPENABLE | `3` | ***`0`*** |
| GENERIC-METRIC IDENTITY | `6` | ***`7`*** (+ 62) |

***So the block that the second seat was approved for is closed, and `r7337` ② names this as `70`'s return to the
repair stride.***
- *The closed-slicing halves of rows 0, 2, 3, 4 and 5 stay as they were.*
- *`70`'s row-72 table (closed FRW, free `a`) may cover some of them. Matching each half's claim to row 72's theorems
  is a reading I have not made, so no half is moved on it.*

## ② The next campaign: 3, as registered (p `0.65`)

***Campaign 3, rows 1, 3 and 98***, single-seat. In one line: it is on the engine as it stands, it is the cheapest
priced block (≈ `270`), and row 3's closed-FRW rank is the natural neighbour of `70`'s row-72 table.
- *Row 62 joining campaign 6 does not change the order.* Campaign 6 is unpriced design work: index algebra over a
  non-diagonal `g`, and now a frame.

## ③ Compile time

| instance | table | live coordinates | wall time | kind, as registered |
|---|---|---|---|---|
| row 59 (`quartic_identity`) | none | — | ***`4 s`*** | under `30 s` ✔ |
| `70`'s eight `r7333` rows | none (components only) | 1–2 | `5`–`17 s` | under `30 s` ✔ |
| row 72 (`70`) | `256` entries | 3 | ***`320 s`*** | `3`–`12` min ✔ |
| row 45 (`sds_kretschmann`) | `256` entries | 2 | ≈ `4` min (as filed at `r7327`) | `3`–`12` min ✔ |
| `static_table` (`r7333`) | `256` entries | 2, with `F`, `P`, `S` all free | ≈ `12` min, alone in a scratch file | `3`–`12` min ✔ |

- ***Registered: compile time is set by the largest `fin_cases` table, not by the recipe that feeds it (p `0.75`).
  It holds on every instance measured so far.***
  - Every table-free instance is under `30 s`, whatever its recipe. Row 13 uses the two-variable recipe and takes
    `14 s`.
  - Every `256`-case table is minutes, whatever its recipe. Row 45 and `static_table` use only one-coordinate
    profiles.
- ⚠ ***The caveat, said plainly:***
  - Within the table kind, the cost grows with how much each entry carries. `static_table` (6 free profile values)
    is slower than row 45 (2 named profiles).
  - `70` reads this as the number of live coordinates. I read it as the size of each entry's expression after `simp`.
  - The two have not been separated: no instance yet has three live coordinates with a small expression, or one with
    a large one.
- ***Where it belongs, then: in the INSTANCE band***, as a second axis keyed to whether a full table is proved:
  - no table: under `30 s`;
  - a `256`-case table: `3`–`12` minutes.

  *The recipe's lemmas build once, in seconds, inside `ShadowEngine`. So nothing in the engine band moves.*

## The probabilities

| quantity | p | outcome |
|---|---|---|
| 62 reachable as a product with a line | `0.55` | ***no*** |
| 59 reclassified as no-connection algebra | `0.5` | ***yes, for its identity***; its `S³` half is global |
| campaign 3 first | `0.65` | ***yes*** |
| compile time set by the table, not the recipe | `0.75` | ***yes on all instances so far***, with the per-entry caveat above |

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

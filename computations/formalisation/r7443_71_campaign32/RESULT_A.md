# `r7443+71.9` — RESULT: campaign 32 BUILT. ⌗ Step 3's computable parts of rows 53 and 86: the SdS kernel is exactly one-parameter (a classification, not a symbol count), the Type-D pair exactly four, `dim so(3,5,6) = 3, 10, 15`, and one branch exactly on the throat. ⌗ `145` lines against `140` (band 70–300). ⌗ Both rows stay `ROW`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.8` before any Lean was written. It is not
revised. `probes/Row53Row86.lean` builds with no warning, and its four theorems print `[propext, Classical.choice,
Quot.sound]` (`PROBE_RUN_A.txt`, `10 s`).*

## ⛔ The stop, scored

***Not fired.*** `145` lines, under `420`.

## What was built

| row | theorem | what it proves |
|---|---|---|
| 53 | ***`sds_kernel`*** | Every `1 − 2M/r − Λr²/3` solves `r f' + f − 1 + Λr² = 0` on `r > 0`. ***Every differentiable solution there is one of them for exactly one `M`***: `r f − r + Λr³/3` has zero derivative on `(0, ∞)`, so it is constant. The receipt's "`1` for SdS" counts the free symbols of one formula. This is the fibre itself |
| 53 | ***`typeD_four`*** | `(c₂, c₁, c₀, d₁) ↦ (D_r, D_p)` is injective, so the family has exactly four parameters. The shared `c₀` and opposite `c₂` are why it is not six |
| 53 | ***`skew_finrank`*** | the skew-symmetric `n × n` real matrices are linearly equivalent to their strictly upper entries (`skewEquiv`, for every `n`). Their `finrank` is `3, 10, 15` at `n = 3, 5, 6`. That is the receipt's stratum arithmetic: `SO(4,1)` `10`, `SO(2,1) × SO(3)` `6`, `ℝ_t × SO(3)` `4`, inside `15` |
| 86 | ***`branch_count`*** | over `ℂ`, `z² = X² − α²` has one root exactly when `X² = α²` (the throat). Otherwise it has two distinct roots, the axis `X = 0` included, where the pair is imaginary and not absent |

## Caveats, beside the score

- ***Neither row moves***, as registered. The essential image (53) and the `Z₃` action (86) are the ROW objects.
  `decl` stays empty by rule, and the residue link is on each row's page phrase (`ROW_TEXT.tsv`, third column), as
  row 18's is.
- ***`skew_finrank` is the matrix count***, not the isotropy groups' own Lie algebras inside `so(5,1)`, as
  registered.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.70` | ***yes***, `145` |

## Census

***Unchanged:*** DONE `76`, halves `2`, ORDER `0`, LIMIT `12`, ROW `3`, generic-metric `1`, library gap `17`; total
`111`. The join holds at `284` pairs. Rows 53 and 86 gain their residue text and page links.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

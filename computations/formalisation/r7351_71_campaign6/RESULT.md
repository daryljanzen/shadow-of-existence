# `r7351+71.5` — RESULT, stages A and C: Stage A lands at `49 + 15` lines against `120`. ⌗ Stage C builds one row of the four I priced as reported (row 7, as matrix algebra) and reports three. ⌗ Survival this block: `3` of `6`, against an expected `3.6`; running `14` of `21`. ⌗ Stage B, the non-diagonal engine with row 83, is NOT in this landing: it is pushed separately when it lands, per `r7347` ③

*Scored against `PREDICTION.md` in this directory (pushed at `r7351+71.1`, before any of the six receipts was opened).
It is not revised. Every new axiom line is standard, with no `sorryAx` (`PROBE_RUN_STAGE_A.txt`, `PROBE_RUN_ROW71.txt`).*

## The rows

| stage | row | registered | outcome | lines |
|---|---|---|---|---|
| A | 71 | the definitional identity between the contractions | ***BUILT***: `weyl2_gb_identity` for every metric the engine contracts, and `row71_sds`, where `C² = 48M²/r⁶ ≠ 0` and the remainder is `−8Λ²/3`, so the identity carries weight | `5 + 15` |
| A | 19 | `GB`'s coefficient combination, or a total derivative | ***BUILT IN PART***: `gb_total_derivative`. With `70`'s `frw_closed` (`a³E₄ = 24a″(a′² + 1)`), `√g·E₄ = d/dT[24(a′³/3 + a′)]` on closed FRW for every `a`. Open: `k = 0, −1` and the running-layer comparison | `10` |
| C | 7 | priced as reported | ***BUILT IN PART***, against the price: `adm_trace_split`, `K² − K_ijK^ij = (2/3)θ² − σ_ijσ^ij` for any leaf, as `3 × 3` matrix algebra. Open: the receipt's count claims | `14` |
| C | 6 | priced as reported | ***REPORTED***: the receipt checks `∇_μ G^μ_ν = 0` to `O(ε²)` on a NON-diagonal two-wave metric. That needs a covariant divergence of curvature over a non-diagonal metric: Stage B's engine and then a second derivative of it | — |
| C | 20 | priced as reported | ***REPORTED***: an argument about the first-class constraint structure (freedom versus stability), not a pointwise identity | — |
| C | 58 | priced as reported | ***REPORTED***: the ADM kinetic scalar's `ε²` part for `γ = a² exp(εH)` needs the matrix exponential to second order, with `det exp(εH) = 1` for traceless `H` | — |
| | ***A***, registered `120` (band 60–200) | | ***`64`*** (`49` in `Campaign6A.lean` less row 7's `14`, plus `15` in the instance file) | ***under the band*** |

***Why A came in under:*** row 71 is three lines once the contractions exist, and 19's half is a one-line chain rule
over `70`'s table. The model priced a contraction LAYER over a general metric. None was needed: the engine's
contractions already take the array as an argument.

***Stage C, against its p `0.35` that any row is built:*** ***yes, one (row 7)***. It was not a Bianchi row: its
receipt's object was algebra, which my reading had not seen.

## The survival rate (running `11` of `15` → `14` of `21`)

| row | my reading | p | survived? |
|---|---|---|---|
| 71 | the definitional identity between three contractions | `0.8` | ***yes*** |
| 19 | `GB` a total derivative in 4D, `Weyl²` not | `0.6` | ***no***: the receipt's object is closed FRW for every `a`, not the general topological fact. This is the registered shape again: the object evaluated on a specific family |
| 6 | `∇^a G_ab = 0` for a general metric | `0.7` | ***yes*** (checked on a specific non-diagonal metric, but the identity is the object) |
| 20 | the momentum constraint as `div G` on a slice, plus a mode ODE | `0.45` | ***no***: the object is the first-class argument |
| 7 | `K_ij = −½ £_n h_ij`, or Gauss–Codazzi | `0.5` | ***no***: the object is the trace decomposition `K = (θ/3)g + σ` |
| 58 | `K_ijK^ij − K²` and its Legendre transform | `0.55` | ***yes*** |

***`3` of `6`, against an expected `3.6`. Running `14` of `21` (`0.67`).*** *Two of the three misses (19, 7) are the
registered shape, a stand-in naming a construction or a general fact. Row 20's miss is a stand-in naming a
mechanism ("a mode ODE") that the receipt does not contain.*

## Compile time (`r7351` ②: the table-size axis)

***No table in this landing:*** `Campaign6A.lean` builds in `≈ 36 s` (all three theorems), and `row71_sds` adds
nothing measurable to the instance file. Both are inside the registered "no table: under `30 s`" up to file
overhead. *Stage B's `625`-case non-diagonal table, at `0.73 s × 625 × 4 ≈ 30` minutes, is the next measurement on
the axis.*

## Census (moved in the push that built the rows)

DONE ***`43`***, halves ***`11`***, GENERIC-METRIC IDENTITY ***`5`*** (6, 20, 58, 62, 83), real end `20`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

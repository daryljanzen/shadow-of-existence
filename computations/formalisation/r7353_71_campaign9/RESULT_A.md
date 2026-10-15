# `r7353+71.10` — RESULT: row 19's `k = 0` and `k = −1` halves are built. THE connection gives `a³·GB = 24a″(a′² + k)`, the `T`-derivative of `24(a′³/3 + k a′)`, for EVERY `k`, from two profile conditions at the point. ⌗ `232` lines against `180` (band 90–300), `328 s` for the `256`-case table, inside the registered `3–6` minutes. ⌗ Row 19 stays a half: the running-layer comparison is still open

*Scored against `PREDICTION.md` in this directory (pushed at `r7353+71.9`). It is not revised. Three new axiom lines,
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`).*

| piece | registered | measured | outcome |
|---|---|---|---|
| A | `180` lines (band 90–300, ⛔ `350`), `3–6` min, p `0.6` | ***`232`***, ***`328 s`*** | ***BUILT***, in the band. p: ***yes*** |

## What is proved (`probes/FRWk.lean`)

- ***`frw_gb_k`.*** Take the metric `−dT² + a²(dχ² + S dθ² + S·S₂ dφ²)`, with `a`, `S` and `S₂` any smooth, nowhere-zero
  profiles. Suppose that at the point `S′² = 4S(1 − kS)`, `S″ = 2 − 4kS`, `S₂′² = 4S₂(1 − S₂)` and `S₂″ = 2 − 4S₂`.
  Then THE connection's `a³·GB` is `24a″(a′² + k)`.
  - The curvature is a `256`-case table, kept symbolic in the profile data and checked case by case, so each case
    is pure algebra.
  - The profile conditions enter only in the final contraction.
- ***`frw_gb_three`:*** the conditions discharged for `S = sin²χ` (`k = 1`, `70`'s `frw_closed` reproduced
  independently), `χ²` (`k = 0`) and `sinh²χ` (`k = −1`), each with `S₂ = sin²θ` near the point.
- ***`gb_total_derivative_k`:*** `d/dT[24(a′³/3 + k a′)] = 24a″(a′² + k)` for every smooth `a`.
  - With `frw_gb_k`, the Gauss–Bonnet density is a total `T`-derivative for every `k`.
  - This generalises `r7351+71.2`'s `gb_total_derivative` (`k = 1`).

## Caveats beside the score

1. ***The `k = 0` chart*** is flat space in spherical coordinates (`S = χ²`), not the engine's Cartesian `qFRW`.
   Both are flat FRW. The spherical chart is the one the one-theorem-for-all-`k` form needs.
2. ***Copied helpers:*** the three-factor recipes and `cF` are copied from `70`'s `SecondSeatFRW.lean`, because
   probe files do not import each other. This is a duplication, not a dependency.
3. ***Open half, named:*** the running-layer comparison in row 19's open part is not built. It is not a pointwise
   identity on a metric I can name without re-reading the receipt.
4. ***Compile time:*** a first, development run took `722 s`. The recorded run is `328 s`, in line with `70`'s
   `320 s` for the same table shape. On the axis that is `m ≈ 1.75` at `256` cases, inside the registered range.

## Census (moved in this push)

Row 19 stays `DONE (chartable half)`, and its text is updated: the `k = 0, −1` halves are closed, and the
running-layer comparison remains. ***Counts unchanged:*** DONE `45`, halves `12`, generic-metric `2`, real end `20`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

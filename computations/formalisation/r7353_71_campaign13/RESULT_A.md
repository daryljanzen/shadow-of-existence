# `r7353+71.18` — RESULT: campaign 13 BUILT. ⌗ Rows 0, 2, 4 and 5 are DONE. THE connection gives `R = 6(aä + ȧ² + k)/a²` and `Weyl² = 0` on FRW for EVERY `k`. P10's closed slicing `a = α cosh(T/α)` on `S³` has `R = 12/α²` and `Weyl² = 0` at every point. ⌗ `87` net added lines against `90` (band 45–180, ⛔ stop `220`): in the band. ⌗ `331 s`, the `256`-case table proved once

*Scored against `PREDICTION.md` in this directory (pushed at `r7353+71.17`). It is not revised. Every axiom line in
the file is `[propext, Classical.choice, Quot.sound]`, with no `sorryAx`, and campaign 9's three theorems are
re-checked after the refactor (`PROBE_RUN_A.txt`). File: `probes/FRWk.lean`, `232` → `319` lines (`+100 −13`).*

## ⛔ The stop, scored first

***Not fired.*** `87` net added lines, under `220`.

## What was built, against the registration

| step | theorem | what it proves | registered |
|---|---|---|---|
| 1 | `frw_tab_k` | the 256-case table, moved out of `frw_gb_k`'s proof. `frw_gb_k`'s statement is unchanged, and it is re-checked | ✔ |
| 2 | ***`frw_scal_weyl_k`*** | profile conditions at the point ⇒ `R = 6(aä + ȧ² + k)/a²` and `Weyl² = 0`, for every `k` | ✔ |
| 3 | `cosh_slicing_R`, `frw_closed_slicing` | `a = α cosh(T/α)`, `S₁ = S₂ = sin²` near the point ⇒ `R = 12/α²` and `Weyl² = 0` | ✔ |

***The rows:***
- ***0:*** `R` of the closed slicing is `12/α²`, which is the de Sitter value of the max-symmetric chartable half.
- ***2:*** `Weyl² = 0` at `k = +1`, for ANY `a` (step 2). The other two `k` were already built.
- ***4:*** the closed slicing's `R`.
- ***5:*** the closed slicing's `R` is CONSTANT: `12/α²` at every point.

***The decisive step*** (step 2's `Weyl²` for a general `k`) closed on its first attempt. It needed `maxHeartbeats 0`,
the same option the table already carried. The profile conditions were substituted into the table entries BEFORE
`field_simp`, so `d²` never meets a power it cannot rewrite.

## Caveats beside the score

- ***The near-point convention, as in campaign 9.*** The sphere profiles are `sin²` only near the point. The chart
  needs `S₁, S₂` nonzero everywhere, so the statements hold at every point of the open chart region, not on `S³`
  as a manifold. This is the convention `r7325+71.3` named for these halves.
- ***`a` is genuinely global:*** `α cosh(T/α)` is smooth and nonzero on all of `ℝ`, so the time profile needs no
  convention.
- ***`70`'s `frw_closed`*** (row 72) proves step 2's `k = +1` case in its own file. This file does not import it
  (probes cannot) and does not touch it. The two are independent proofs of the same `k = +1` statements.

## Compile time

| | registered | measured |
|---|---|---|
| wall | `6–9` minutes | ***`331 s`*** (`5.5` min) |

That is campaign 9's `328 s` plus about `3 s`: the table dominates, and the four contractions on top of it are almost
free. The first build failed only in step 3's `cosh` derivative glue. That glue was then proved as a separate lemma
in a scratch file (seconds) before the one full rebuild. The scratch file is deleted.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 13 BUILT under its stop | `0.7` | ***yes***, `87` |

## Census (moved in this push)

Rows 0, 2, 4 and 5: `DONE (chartable half)` → ***`DONE`***, with this result appended to each row's text, as
registered. ***Counts, checked before the commit:*** DONE ***`51`***, halves ***`6`***, generic-metric `2`, library
gap `17`, no-connection `32`, real obstruction `3`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

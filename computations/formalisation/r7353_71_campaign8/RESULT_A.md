# `r7353+71.5` — RESULT, piece A: the second Bianchi identity for THE connection of any smooth metric. `106` lines against `200` (band 100–350), in the band, in `21 s`. ⌗ Row 6 becomes a half: the contraction to `∇^a G_ab = 0` is piece B, still to come

*Scored against `PREDICTION.md` in this directory (pushed at `r7353+71.4`). It is not revised. Two new axiom lines,
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`).*

| piece | registered | measured | outcome |
|---|---|---|---|
| A | `200` lines (band 100–350), p `0.65` | ***`106`***, `21 s` | ***BUILT***, in the band. p: ***yes*** |

## What is proved (`probes/Bianchi2.lean`)

- ***`bianchi2_alg`:*** `Σ_cyclic (∇_u R)(v, w) z = 0` as CLM algebra.
  - `R` is `curv_model`'s closed form in `Γ` and `DΓ`. `∇R` is its derivative plus the four `Γ` corrections.
  - It needs only `Γ` symmetric and `D²Γ` symmetric in its two directions (Schwarz). ***The symmetry of `DΓ` I
    registered as needed is not used.***
- ***`hasFDerivAt_RmB`:*** for any `C^∞` `Γ`, the closed form's derivative is `DRmB`.
- ***`lcGam_symm`:*** the engine's `lcGam` is symmetric, from the Koszul form and the symmetry of `B`.
- ***`bianchi2_lc`:*** for `lcConn` of `ndOf B`, with `B` any smooth, symmetric, nondegenerate field of forms on a
  finite-dimensional `E`:
  1. its curvature on constant fields is `RmB (lcGam B y) (DlcGam y)`;
  2. the derivative of that is `DRmB`;
  3. the cyclic sum of `∇R` vanishes.

## Caveats beside the score

- ***`∇R` is the coordinate formula:*** it is the covariant derivative on constant fields,
  `∇_e(R(u,v)w) − R(∇_e u, v)w − R(u, ∇_e v)w − R(u,v)∇_e w`, with `∇_e a = Γ(e, a)`. It is not `mathlib`'s
  covariant derivative of a tensor field, which `mathlib` does not have for a `(1,3)` field.
- ***Not built:*** (i) the contraction to `∇^a G_ab = 0`, which is piece B; (ii) the receipt's own `O(ε²)`
  two-wave instance.

## Census (moved in this push)

| status | after `r7353+71.3` | now |
|---|---|---|
| DONE | `44` | `44` |
| DONE (chartable half) | `12` | ***`13`*** (+ 6) |
| GENERIC-METRIC IDENTITY | `3` | ***`2`*** (20, 62) |
| real end | `20` | `20` |

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

## `r7353+71.6` — appended: the census did NOT move in `r7353+71.5`'s push

*Appended, not revised.*
- The script that edits `ROWS.tsv` failed on a quoting error, and the commit went out without it. So
  `r7353+71.5`'s push carried this RESULT and the build, but not the census row it claims.
- That breaks the `r7341` rule (the census moves in the SAME push as the build).
- It is corrected in the very next push (`r7353+71.6`), which carries only the census row.
- *What I change:* the census edit is now checked by its counts before the commit, in the same command.

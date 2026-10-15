# `r7371+71.7` — RESULT: campaign 18 BUILT. ⌗ Row 108 is DONE. Inside the receipt's ansatz, the two determinations of `G′²` differ by `−4M·q(r)/r⁴`, an overall factor of `M`. They agree at `r` iff `M·q(r) = 0`, and on an open interval only at `M = 0`. ⌗ `136` lines against `130` (band 70–260, ⛔ stop `320`): in the band. ⌗ `6 s` against under `1` minute

*Scored against `PREDICTION.md` in this directory (pushed at `r7371+71.6`, before the build). It is not revised.
Every axiom line is `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`). New file:
`probes/Row108Cut.lean`. No pre-opening reading was registered, so the running rate stays `15` of `22`.*

## ⛔ The stop, scored first

***Not fired.*** `136` lines, under `320`.

## What was built

| piece | theorem | what it proves |
|---|---|---|
| (i) | `boost_pullback` | `X₀ = F sinh κt`, `X₁ = F cosh κt`: `−dX₀² + dX₁² = F′²dr² − κ²F²dt²`, no cross term |
| (ii) | `cut_defect` | with `G² = α² − r² − f/κ²`: `κ²f·(G²)′² − G²·(4κ²(1 − f) − f′²) = −4M·q(r)/r⁴`, `q = −Mα² + 9Mr² + 2α²κ²r³ − 2r³`, for every `r ≠ 0` |
| (iii) | `cut_closure_iff` | `(G²)′²/(4G²) = (1 − f)/f − f′²/(4fκ²)` at `r` iff `M·q(r) = 0` |
| (iv) | `cut_closes_only_at_M_zero` | agreement on any open interval forces `M = 0` (a nonzero cubic has finitely many roots; its constant term is `−Mα²`) |
| (v) | `cut_control` | at `M = 0` the defect vanishes at every `r`; at `κ = 1/α`, `G² ≡ 0`, the hyperplane `X₂ = 0` |

## Caveats, beside the score

- ***`κ ≠ 0` is a hypothesis of (ii)***, not only of (iii) as the registration listed. `f/κ²` is undefined
  otherwise, and the receipt divides by `κ` throughout.
- ***(i) and (ii) are separate statements, not one composed theorem.*** (i) is the pullback of the boost block,
  which forces `F² = f/κ²`. (ii)–(iv) take the closure equation in the receipt's substituted form, with
  `F′² = f′²/(4fκ²)`. No single theorem pulls back the whole six-dimensional ansatz and derives the closure
  equation from it.
- ***Not claimed, as registered:*** nonexistence over ALL hypersurfaces of `dS₅`. The receipt's (4) is inside one
  ansatz, and so is this.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 18 BUILT under its stop | `0.75` | ***yes***, `136` |

## Census (moved in this push)

Row 108: `DONE (chartable half)` → ***`DONE`***, its text naming the five declarations and what is not claimed.
***Counts, checked:*** DONE ***`55`***, halves ***`1`*** (77), generic-metric `2`, no-connection `32`, library gap
`17`, real obstruction `4`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

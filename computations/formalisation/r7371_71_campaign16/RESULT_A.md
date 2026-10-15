# `r7371+71.3` — RESULT: campaign 16 BUILT, all four D. ⌗ Row 35 is DONE. Under THE connection, on the `r7341` port, the static metric `−F dt² + dr²/F + r²dΩ²_{D−2}` has `G^t_t = (D−2)(rF′ + (D−3)(F − 1))/(2r²)` for ANY `F`, at `D = 4, 6, 7, 8`, and Tangherlini–de Sitter solves `G^t_t + Λ = 0` at each. ⌗ `382` lines against `260` (band 140–450, ⛔ stop `550`): in the band, above the point. ⌗ `94 s` against `1–10` minutes registered: in the range

*Scored against `PREDICTION.md` in this directory (pushed at `r7371+71.2`, before the build). It is not revised.
Every axiom line is `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`). New file:
`probes/TangherliniD.lean`. No pre-opening reading was registered, so the running rate stays `15` of `22`.*

## ⛔ The stop, scored first

***Not fired.*** `382` lines, under `550`.

## What was built

| piece | theorem(s) | what it proves |
|---|---|---|
| the sphere | `Wm_d1`, `Wm_d2` | `Ω = 4/(1 + Q)²`, `Q = Σ mₖyₖ²` with any mask `m ≥ 0`: its first and second Fréchet derivatives, in closed form, for any `n` |
| the metric | `cTg_smooth`, `cTg_ne`, `cTg_d1`, `cTg_d2` | ONE `Fin n` definition, `cTg`, for every `D`: `−F(r)`, `1/F(r)`, and `P(r)Ω(x)` on every sphere slot; smoothness, nonvanishing and both derivative tables, proved once for all `n` |
| `G^t_t` | `tangherlini4_Gtt`, `tangherlini6_Gtt`, `tangherlini7_Gtt`, `tangherlini8_Gtt` | THE connection's `R^t_t − R/2 = (D−2)(rF′ + (D−3)(F − 1))/(2r²)`, for ANY smooth nonvanishing `F`, at ANY point of `ℝᴰ` with `P = r²` near it |
| the kernel | `tangherlini4_kernel`, …, `tangherlini8_kernel` | `F = 1 − 2M/r^{D−3} − 2Λr²/((D−1)(D−2))` gives `G^t_t + Λ = 0` |

- With `D = 5` (`tangherlini5_Gtt`, `r7341+71.5`, nested sines), every D the receipt checks (4–8) is built.
- The stereographic chart covers the sphere minus one point and needs no convention: `Ω` is smooth and nowhere zero on
  all of `ℝ^{D−2}`, and the theorems hold at every `x`, not at a chosen one. `P = r²` near the point is the
  convention, for `P` only, as at `D = 5`.
- ***What is NOT built, as registered:*** a theorem quantified over all `D`. Each `D` is a separate contraction,
  closed by one `simp`, one `field_simp` and one `ring`. The derivative layer is generic in `n`; the contraction is
  not.

## Compile time and size

| | registered | measured |
|---|---|---|
| lines | `260` (band 140–450) | ***`382`*** |
| wall | `1–10` minutes | ***`94 s`*** (whole file, printed and asserted of nothing) |

- ***Lines over the point by `47%`, inside the band.*** The generic layer (`Qm`, `Lm`, `Wm` and the `cTg` tables,
  ≈ 155 lines) was priced as one lemma per derivative. It needed a mask, a bilinear form and a product rule each.
  The four instances are ≈ 48 lines each, as priced.
- ***Risk 1 (the `D = 8` contraction) did not bite.*** `Ω` enters every sphere entry as the same factor, so the
  contraction stays one rational function of `r` and the `D − 2` sphere coordinates.
- ***Risk 2 (`Ω`'s derivatives as a generic lemma) was the work.*** It built with `d2_of` and `fdA_hasFDerivAt` from
  the engine and no new engine lemma.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 16 BUILT (all four D) under its stop | `0.45` | ***yes***, `382` |

## Census (moved in this push)

Row 35: `DONE (chartable half)` → ***`DONE`***, its text naming all ten declarations. ***Counts, checked:***
DONE ***`53`***, halves ***`3`*** (7, 77, 108), generic-metric `2`, no-connection `32`, library gap `17`, real
obstruction `4`. The committed `rerun_census.py` was NOT re-run on the whole tree in this push. `PROBE_RUN_A.txt` is
the axiom check of the one new file.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

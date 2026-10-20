# `r7443+71.12` — RESULT: campaign 33 BUILT. ⌗ Five library-gap rows closed: 23 (cited: `RunningLayer`), 24, 82, 84, 46. ⌗ `184` lines against `300` (band 160–600). ⌗ Library gap `17 → 12`, DONE `76 → 81`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.11` before any Lean was written. It is not
revised. `probes/LibGap5.lean` builds with no warning, and its eight theorems print `[propext, Classical.choice,
Quot.sound]` (`PROBE_RUN_A.txt`, `9 s`).*

## ⛔ The stop, scored

***Not fired.*** `184` lines, under `900`.

## What was built, row by row

| row | theorem(s) | what it proves |
|---|---|---|
| 23 | ***cited***: `frw_invariants`, `tv_identity`, `ledger_general`, `ledger_layer`, `ledger_ds_point` (`RunningLayer.lean`) | this is the receipt row 19's campaign 12 formalised. All five computed items were already proved under THE connection |
| 24 | `b4_rewrite`, `trace_relation`, `shear_onset`, with `row1_shear` cited | `Ric² = ½W − ½GB + ⅓R²` from the definitions. `b₄ = (7/40)W + (149/360)GB + (1/8)R²`. The `R²` trace relation. The shear Weyl² `12σ²(H − 2σ)²` has no constant or linear term, and its `σ²` coefficient is `12H² ≠ 0` |
| 82 | `friedrich_saturation` | saturation at `n = 4, 5`. `λ_min(5) = 5/(2a) > 0`, with no zero mode. `R(5)/4 = 5/a²` |
| 84 | `one_scale`, `mass_bounds` | `R = 20Λ/3` and `λ_min = (5/2)√Λ/√3` from `α = √(3/Λ)`. ***`m_min < 10⁻³⁰ eV` and `m_e/m_min > 10³⁰` as exact inequalities***, from `0 < √0.7 < 1` alone (the margin is about eight orders) |
| 46 | `photon_sphere`, `nariai_seam`, `areas_entropies` | `d/dr(f/r²) = (6M − 2r)/r⁴`, which has no `α` and is zero exactly at `3M`. At Nariai, `3M_N = r_N` with `f = f′ = 0`, and the Lyapunov combination vanishes. The two areas agree only at `M = α/2 ≠ M_N`. The seam is a third. The entropy ratios are `3/8` and `1/8` |

## Caveats, beside the score

- ***The imported data stay imported, as registered.***
  - the `b₄` coefficients (23 and 24);
  - the Dirac spectrum on round spheres (labelled `lamD`) and the Friedrich bound (82 and 84);
  - the area formula `4πr²` and `S = A/4` (46);
  - the physical constants (84).

  Each row's text names its import as its library's, not the row's, as rows 59 and 67 do.
- ***Paper-text checks are pins***, not formalised. That includes row 46's `eq:ds-entropy` parse, whose comparison
  is the algebra built here.
- Row 85 (spinors) is next. The pricing found that its `√f` at `r = 0.001` is the square root of a negative number,
  which needs `ℂ`, not `Real.sqrt`.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.65` | ***yes, all five***, `184` |

## Census (moved in this push)

***Rows 23, 24, 82, 84 and 46 → `DONE`***, each with `decl` filled. That makes `98` rows and `299` pairs, and
`check_formalisation_join.py` reads ***green: 299 of 299***.

***Counts:*** DONE `81`, halves `2`, ORDER `0`, LIMIT `12`, ROW `3`, generic-metric `1`, library gap `12`; total
`111`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

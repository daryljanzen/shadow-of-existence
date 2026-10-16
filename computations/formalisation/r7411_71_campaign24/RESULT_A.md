# `r7411+71.13` — RESULT: campaign 24 BUILT. ⌗ Row 59's Euler-chart field identities hold at every point, the frame-constant floor's Taylor coefficients are the receipt's at both directions, and the first two counts are `5` and `12`. ⌗ Blind part: `+102` lines against `+110` (band 50–260). ⌗ Row 59 stays ORDER: the rank `8` and the non-constant integrals remain

*Scored against `PREDICTION.md` in this directory (pushed at `r7411+71.12`). It is not revised. All 23 declarations
of `probes/Row59Euler.lean` build with no warning, and the seven theorems print `[propext, Classical.choice,
Quot.sound]` (`PROBE_RUN_A.txt`, `16 s`). Built on Daryl's instruction.*

## ⚠ First, the slip the registration declared

Parts (B) and (D-5) were drafted and compiled before the registration, and that registration said so. They are
committed at registration as they stood (`158` lines), and nothing here scores them. ***Only (C) and (D-12) were
blind.***

## ⛔ The stop, scored

***Not fired.*** The file is `260` lines, under `500`.

## What was built

| piece | theorem(s) | what it proves | blind? |
|---|---|---|---|
| (B) | `rad_coframes`, `chart_trace_pow`, `h4_invariants`, `h4_chart` | `Rad · e = ẽ`, `det e = sin θ/8`, `Rad Radᵀ = 1`; `tr((eᵀe)⁻¹eᵀHe)ᵏ = tr Hᵏ` for invertible `e`; for the receipt's `H4`, at every point: `p₁ = 0`, `p₂ = 2 − 2 sin²φ sin²θ`, `p₃ = 0`, `p₄ = p₂²/2`, and `H4 + H4b` traceless, in the chart off the poles | no |
| (D-5) | `tt_dim_five` | the receipt's five matrices are traceless, symmetric, independent and spanning | no |
| (C) | `floorA_closed`, `floorB_closed`, `iter_expsum`, ***`floor_taylor`*** | at `λ = exp(εh)` Milnor's `R` is `2(1 + 2e^ε + 2e^{−ε} − e^{2ε} − e^{−2ε})` and `2(4e^{−ε} − e^{−4ε})`. Its `R⁽ⁿ⁾(0)/n!` for `n = 0..4` are `6, 0, −4, 0, −7/3` and `6, 0, −12, 20, −21`, which is `6 − 2p₂ε² − (10/3)p₃ε³ − (7/6)p₄ε⁴`, and `(7/6)p₄ = (7/12)p₂²` on both | ***yes*** |
| (D-12) | `jetCons`, `jetCons_surj`, ***`jet_dim_twelve`*** | the six constraints are surjective onto `ℝ⁶` (explicit preimage), so by rank–nullity the admissible one-jet has dimension `18 − 6 = 12` | ***yes*** |

- ***(B) needs no inverse of the chart.*** The receipt computes `Rad = ẽ e⁻¹` and `M = ḡ⁻¹eᵀH4e` symbolically.
  Here `Rad` is pinned by `Rad · e = ẽ`, and `chart_trace_pow` reduces every invariant of `M` to one of `H4`. So
  the pointwise identities hold at the poles too, and the chart statement is the one that needs `sin θ ≠ 0`.
- ***(B)'s three Pythagorean spot checks are subsumed.*** They are instances of identities proved for all angles.
- ***(C)'s values times `2π²` are the receipt's*** `[12, 0, −8, 0, −14/3]π²` and `[12, 0, −24, 40, −42]π²`. The
  volume factor is `euler_volume` (campaign 21).

## Caveats, beside the score

- ***(C) takes Milnor's formula as the definition of `R`.*** It is `milnor_scalar` (campaign 21), proved there from
  the Koszul formula on su(2). Probes do not import each other, so the formula is not linked by `import`.
- ***The trig certificates in (B) were found by sympy,*** by sequential division by `sin² + cos² − 1` for each
  angle. Every one is checked by `ring` inside `linear_combination`.
- ***Not built:*** the rank `8` (taken on twenty random jets, so a Lean check of the exported matrix would re-check
  numbers rather than derive them), and the integrals of the non-constant `H4` series.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| (C) and (D-12) both built under the stop | `0.55` | ***yes***, `+102` lines |

## Census (moved in this push)

***Row 59*** stays `ORDER: ENGINE-REACHABLE`, and its text now names (B), (C), (D-5) and (D-12) as built. What it
still waits on is the rank `8` and the non-constant integrals. ***Counts, unchanged:*** DONE `74`, halves `2`,
ORDER (engine) `1`, LIMIT `10`, ROW `5`, generic-metric `2`, library gap `17`. Total `111`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

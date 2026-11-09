# `r7717+71.1` — PRE-REGISTRATION: campaign 119, **P3's cubic chain: the factorisation, the reading-swap, the root-exchange involution, the horizon locus and Nariai**. ⌗ `450` new lines (band 300–700), p `0.8`. **Expected stop:** 5a's nested square root

*Registered before any Lean. The probe is `probes/SlicingCubic.lean`, a copy of campaign 118's `CircleConic.lean`.
Everything new is prefixed `sl_`. The rows are those of `r7717_71_survey/SURVEY.md`. Gauge `α = 1`, `g(t) = t − t³`,
`2M = g(r₀)`, `σ(x) = (−x + √(4 − 3x²))/2`.*

## Rows

| Row | Statement (P3 line) | Lines | p |
|---|---|---|---|
| 2 | `prop:factor` (l.310): `r³ − r + g(r₀) = (r − r₀)(r² + r r₀ + r₀² − 1)`. When `4 − 3r₀² ≥ 0` the roots are exactly `r₀, σ(r₀), (−r₀ − √(4 − 3r₀²))/2`, and they sum to zero | 40–80 | 0.97 |
| 3 | `prop:r0zero` (l.363): at `r₀ = 0`, `1 − 2M/r − r² = 1 − r²`, and the cubic's root set is `{0, 1, −1}` | 20–40 | 0.98 |
| 4 | `prop:readingswap` (l.373): `g(σ(r₀)) = g(r₀)` when `4 − 3r₀² ≥ 0`, so `f` is unchanged | 40–80 | 0.95 |
| 5a | `prop:involution` (l.388): `σ(σ(x)) = x` on `[−1/√3, 2/√3]`, which contains the paper's `[0, 2/√3]`. Also stated: `σ` maps `[0, 2/√3]` onto `[−1/√3, 1]`, so it is not an involution of `[0, 2/√3]` as a self-map | 60–120 | 0.9 |
| 5b | `σ(r₀)` is a root of `r₀`'s cubic, positive and different from `r₀` (unless `r₀ = 1/√3`), exactly for `r₀ ∈ [0, 1)`; at `r₀ = 1` it is `0`; for `r₀ ∈ (1, 2/√3]` it is negative | 40–80 | 0.9 |
| 5c | `σ(1/√3) = 1/√3`, `σ(0) = 1`, `σ(1) = 0`, and `1/√3` is the only fixed point in `[−1/√3, 2/√3]` | 20–40 | 0.98 |
| 6a | `prop:locus` (l.441): `g(r) = g(r₀) ⟺ (r − r₀)(r² + r r₀ + r₀² − 1) = 0` | 20–40 | 0.98 |
| 6b | With `u = (r + r₀)/√2` and `v = (r − r₀)/√2`, `r² + r r₀ + r₀² = (3/2)u² + (1/2)v²`. So the conic is an ellipse with major semi-axis `√2` along `r = −r₀` and minor semi-axis `√(2/3)` along `r = r₀` | 60–120 | 0.9 |
| 7 | `cor:nariai-locus` (l.457): the line and the conic meet exactly at `r = r₀ = ±1/√3`. There the cubic has a double root and the third root is `∓2/√3`, and these are the minor axis's endpoints `±√(2/3)·(1, 1)/√2` | 60–120 | 0.95 |

**Non-vacuity:** 5b names a witness `r₀` with two distinct positive roots, and 7 names both meeting points.

**The expected stop** is 5a's nested square root, `√(4 − 3σ(x)²)`. The plan is
`4 − 3σ(x)² = ((3x + √(4 − 3x²))/2)²`, with `3x + √(4 − 3x²) ≥ 0` on `[−1/√3, 2/√3]`. **The fallback** is to
square both sides and use `Real.sqrt_eq_iff`.

**Interpretive, not formalised:** row 3's "two readings of one slicing", and row 6b's attribution to the 2012
dissertation.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

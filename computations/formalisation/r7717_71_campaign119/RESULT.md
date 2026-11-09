# `r7717+71.2` — RESULT: campaign 119, **P3's cubic chain is BUILT: rows 2, 3, 4, 5a–c, 6a–b and 7.** ⌗ `341` new lines (band 300–700; point `450`). ⌗ p `0.8` came true. The expected stop, 5a's nested square root, fell to the registered plan; no fallback was used

*Against `PREDICTION.md` (`r7717+71.1`). 71 ran `lake env lean probes/SlicingCubic.lean`. It exits 0 with no errors
and no warnings. All `643` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `632` inherited and
`11` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 118's `CircleConic.lean`, with everything new in `section SlCubic`.*

Gauge `α = 1`: `g(t) = t − t³`, `2M = g(r₀)`, `σ(x) = (−x + √(4 − 3x²))/2`, and `f = 1 − 2M/r − r²`.

## Row 2, `prop:factor` — BUILT

- **`sl_factor`:** `r³ − r + g(r₀) = (r − r₀)(r² + r r₀ + r₀² − 1)`.
- **`sl_roots`:** when `4 − 3r₀² ≥ 0`, the roots are exactly `r₀`, `σ(r₀)` and `(−r₀ − √(4 − 3r₀²))/2`, and they
  sum to zero.

## Row 3, `prop:r0zero` — BUILT

- **`sl_r0zero`:** at `r₀ = 0`, `2M = 0`, `f = 1 − r²`, and the root set is `{0, 1, −1}`. "Two readings of one
  slicing" stays interpretive.

## Row 4, `prop:readingswap` — BUILT

- **`sl_readingswap`:** `g(σ(r₀)) = g(r₀)` wherever `4 − 3r₀² ≥ 0`, so `f` is the same function.

## Rows 5a–c, `prop:involution` — BUILT, with the flags stated as theorems

- **`sl_σ_σ` (5a):** `σ(σ(x)) = x` on `[−1/√3, 2/√3]`, which contains the paper's `[0, 2/√3]`. The stop fell to
  `4 − 3σ(x)² = ((3x + √(4 − 3x²))/2)²` and `3x + √(4 − 3x²) ≥ 0` there.
- **`sl_σ_swap` (the 5a flag):** `σ` maps `[0, 2/√3]` onto `[−1/√3, 1]` and `[−1/√3, 1]` into `[0, 2/√3]`.
  `σ(2/√3) = −1/√3` lies outside `[0, 2/√3]`, so `σ` is not a self-map of the paper's interval.
- **`sl_σ_second` (5b and its flag):** for `r₀ ∈ [0, 1)`, `σ(r₀)` is a positive root of `r₀`'s cubic, equal to
  `r₀` only at `1/√3`. At `r₀ = 1` it is `0`, and on `(1, 2/√3]` it is negative. The non-vacuity witness is
  `r₀ = 1/2`, with two distinct positive roots.
- **`sl_σ_fixed` (5c):** `σ(1/√3) = 1/√3`, `σ(0) = 1`, `σ(1) = 0`, and `1/√3` is the only fixed point on
  `[−1/√3, 2/√3]`.

## Rows 6a–b, `prop:locus` — BUILT

- **`sl_locus` (6a):** `g(r) = g(r₀) ⟺ (r − r₀)(r² + r r₀ + r₀² − 1) = 0`.
- **`sl_ellipse` (6b):** with `u = (r + r₀)/√2` and `v = (r − r₀)/√2`, `u² + v² = r² + r₀²` and
  `r² + r r₀ + r₀² = (3/2)u² + (1/2)v²`. The semi-axes are `√(2/3)` along `r = r₀` (minor) and `√2` along `r = −r₀`
  (major). The attribution to the 2012 dissertation is a citation.

## Row 7, `cor:nariai-locus` — BUILT

- **`sl_nariai`:** the line meets the conic exactly at `r = r₀ = ±1/√3`. Wherever `3a² = 1`, the cubic is
  `(r − a)²(r + 2a)`: a double root, and the third root `−2a = ∓2/√3`. And `√(2/3)/√2 = 1/√3`, so `(1/√3, 1/√3)` is
  the minor axis's endpoint.

## Marks (P3's inventory, `r7717_71_survey/SURVEY.md`)

- **Built:** 2, 3, 4, 5a, 5b, 5c, 6a, 6b and 7, which is 9 of the 24 rows.
- **Built in part:** 1b, 11c, 12, 13a and 13b. They are in other engines.
- **Not begun:** 1a, 1c, 9a, 9b, 10, 11a and 11b.
- **No formal core:** 8, 14 and 15.

**Next (campaign 120):** rows 9a–b, 10 and 1a–b, the sky angle and the turning points.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

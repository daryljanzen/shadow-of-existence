# `r7719+71.2` — RESULT: campaign 120, **P3's sky angle and turning points are BUILT (rows 9a–b, 10, 1a–b), and the `prop:conjugacy` and `prop:curvature` flags are theorems.** ⌗ `228` new lines, **below** the registered band of 400–850 (point `550`). ⌗ p `0.75` came true. The expected stop did not occur, and no fallback was used

*Against `PREDICTION.md` (`r7719+71.1`). 71 ran `lake env lean probes/SlicingSky.lean`. It exits 0 with no errors
and no warnings. All `654` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `643` inherited and
`11` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 119's `SlicingCubic.lean`, with everything new in `section SlSky`.*

## Why the line count is low

**The expected stop, `arcsin √(1 − x²)`, did not occur.** Mathlib's `Real.arccos_eq_arcsin` is exactly
`arccos x = arcsin √(1 − x²)` for `x ≥ 0`. With that, 10 and its flag share one lemma, `sl_σ_sin`:
`σ((2/√3) sin b) = (2/√3) sin(π/3 − b)` wherever `cos b ≥ 0`.

## Rows 9a–b, `prop:triple` — BUILT

- **`sl_triple` (9a):** `g((2/√3) sin w) = (2/(3√3)) sin 3w` for every `w`.
- **`sl_triple_unique` (9b):** if `ϱ > 0` and `g(ϱ sin w) = k sin 3w` for every `w`, then `ϱ = 2/√3` and
  `k = 2/(3√3)`. Two angles, `π/2` and `π/6`, already force it.

## Row 10, `prop:conjugacy` — BUILT, with its flag as a theorem

- **`sl_conjugacy`:** `χ(g₁(x)) = σ(χ(x))` on `[0, 1]`.
- **`sl_conjugacy_fails` (the flag):** for every `x ∈ [−1, 0)`, `χ(g₁(x)) ≠ σ(χ(x))`. The two sides differ by
  `(2/√3) sin((2/3) arcsin x)`, which is negative there. So on `[−1, 1]` the identity holds exactly on `[0, 1]`. P3's
  proof already takes `a = arcsin x ∈ [0, π/2]`, so the domain is missing only from the statement.

## Rows 1a–b, `prop:turning` — BUILT

- **`sl_turning` (1a):** for `r ≠ 0`, `r f(r) = −(r³ − r + 2M)`, and `√|f(r)| = 0 ⟺ r³ − r + 2M = 0`.
- **`sl_turning_simple` (1b):** at a root `r_h ≠ 0`, `f′(r_h) = −c′(r_h)/r_h` with `c′(r) = 3r² − 1`. So
  `f′(r_h) = 0 ⟺ c′(r_h) = 0` (a double root) `⟺ r_h = ±1/√3`, and a simple root has `f′(r_h) ≠ 0`.

## Row 13a's flag, `prop:curvature` — a theorem at the level of P3's own proof

- **`sl_accel_pos` / `sl_accel_neg`:** along any `r(l)` with `r′ = √|f(r)|`, `r″ = ½ f′(r)` where `f(r) > 0` and
  `r″ = −½ f′(r)` where `f(r) < 0`.
- **`sl_curvature_sign`:** for SdS, `−r″/r = 1 − M/r³` where `f > 0` and `M/r³ − 1` where `f < 0`. The sign flips
  outside the static region.
- **`sl_accel_witness` (non-vacuity):** `r = exp` solves `r′ = √|f(r)|` for `f = −x²` (where `f < 0`) and for
  `f = x²` (where `f > 0`).
- **What is not built:** `K_G = −r″/r` itself. It is the surface-of-revolution formula P3's proof cites, so row 13a
  stays BUILT IN PART until campaign 122.
- **The flag in the paper:** P3's proof already writes `r″ = ½ f′(r) sgn f` and specialises to "the static region
  `f > 0`". The statement does not.

## On `prop:twoalpha` (v), as asked

**Recommendation: state it.** As written, (v) reads as if "the tangent length equals the hinge's height" were the
condition singling out `R = 2α`. But it holds at every `R`: both are `√(R² − α²)`, which is P17's
`prop:tangentnull`. The condition is the common value, `√3α`.

A suggested wording: "the tangent length from the hinge to the throat, which equals the hinge's height in the
embedding at every `R` (P17, `prop:tangentnull`), is `√3α`." This is a strengthening, not a correction.

## Marks (P3's inventory, `r7717_71_survey/SURVEY.md`)

- **Built (14):** 1a, 1b, 2, 3, 4, 5a, 5b, 5c, 6a, 6b, 7, 9a, 9b and 10.
- **Built in part (5):**
  - **1c ⇧ moved:** the sign law away from the root is built; the limit at `r_h` remains.
  - **11c, 12 and 13b:** in other engines.
  - **13a:** its flag is built; the Levi-Civita curvature remains.
- **Not begun (2):** 11a and 11b.
- **No formal core (3):** 8, 14 and 15.

**Next (campaign 121):** rows 11a–c and 12, the hinge and the flip.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

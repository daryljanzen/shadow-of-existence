# `r7719+71.1` — PRE-REGISTRATION: campaign 120, **P3's sky angle and turning points, plus the `prop:conjugacy` and `prop:curvature` flags as theorems**. ⌗ `550` new lines (band 400–850), p `0.75`. **Expected stop:** 10's `arcsin √(1 − x²)`

*Registered before any Lean. The probe is `probes/SlicingSky.lean`, a copy of campaign 119's `SlicingCubic.lean`.
Everything new is prefixed `sl_`, in `section SlSky`. The rows are those of `r7717_71_survey/SURVEY.md`. Gauge
`α = 1`, `g(t) = t − t³`, `σ` as in campaign 119, and `f = 1 − m/r − r²` with `m = 2M`.*

## Rows

| Row | Statement (P3 line) | Lines | p |
|---|---|---|---|
| 9a | `prop:triple` (l.552): `g((2/√3) sin w) = (2/(3√3)) sin 3w` for every `w` | 20–40 | 0.97 |
| 9b | Uniqueness: if `ϱ > 0` and `g(ϱ sin w) = k sin 3w` for every `w`, then `ϱ = 2/√3` and `k = 2/(3√3)` | 40–80 | 0.9 |
| 10 | `prop:conjugacy` (l.618): `χ(g₁(x)) = σ(χ(x))` for `x ∈ [0, 1]`, where `g₁(x) = √(1 − x²)` and `χ(x) = (2/√3) sin((2/3) arcsin x)` | 100–200 | 0.85 |
| 10-flag | **The domain, as a theorem:** for every `x ∈ [−1, 0)`, `χ(g₁(x)) ≠ σ(χ(x))`. So `[0, 1]` is exactly where the identity holds on `[−1, 1]` | 60–120 | 0.85 |
| 1a | `prop:turning` (l.277): for `r ≠ 0`, `r f(r) = −(r³ − r + m)`, so `√|f(r)| = 0 ⟺ r³ − r + m = 0` | 30–60 | 0.97 |
| 1b | At a root `r_h ≠ 0` of the cubic, `f′(r_h) = −(3r_h² − 1)/r_h`. So `f′(r_h) = 0` iff the root is double (`c(r_h) = c′(r_h) = 0`), iff `r_h = ±1/√3`. A simple root has `f′(r_h) ≠ 0` | 60–120 | 0.9 |
| 13a-flag | **`prop:curvature`'s sign, as a theorem, at the level of P3's own proof.** Along any `r(l)` with `r′ = √|f(r)|` and `f(r(l)) ≠ 0`: `r″ = ½ f′(r)` where `f > 0` and `r″ = −½ f′(r)` where `f < 0`. So `−r″/r = −f′/2r` on the static region and `+f′/2r` where `f < 0`; for SdS that is `M/r³ − 1`, the opposite sign. Non-vacuity: `r = exp` with `f = −x²` (and `f = x²`) | 100–200 | 0.8 |

**Not built here:** `K_G = −r″/r` itself. It is the standard surface-of-revolution formula that P3's proof cites;
the curvature from the Levi-Civita connection is row 13a (campaign 122).

**The expected stop** is `arcsin √(1 − x²) = π/2 − arcsin x` on `[0, 1]`, through Mathlib's `Real.arccos_eq_arcsin`
and `Real.arccos_eq_pi_div_two_sub_arcsin`. Next is `√(4 − 3χ²) = 2 cos((2/3) arcsin x)`, with the cosine
non-negative because `(2/3) arcsin x ∈ [0, π/3]`. **The fallback** is to prove 10 in the angle `a = arcsin x`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

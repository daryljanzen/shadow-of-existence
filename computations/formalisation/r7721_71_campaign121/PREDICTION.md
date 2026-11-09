# `r7721+71.1` — PRE-REGISTRATION: campaign 121, **P3's hinge (`prop:twoalpha`, all six) and the flip (`prop:flip`)**, with tangent length = height at every `R` as a theorem. ⌗ `450` new lines (band 300–650), p `0.8`. **Expected stop:** 11b's uniqueness of the circle through the midpoints

*Registered before any Lean. The probe is `probes/SlicingHinge.lean`, a copy of campaign 120's `SlicingSky.lean`.
Everything new is prefixed `sl_`, in `section SlHinge`. The rows are those of `r7717_71_survey/SURVEY.md`.*

**Setting, in coordinates on the transverse plane `ℝ²`.**
- The axis is the origin, and the throat is the circle of radius `α > 0` about it.
- The hinges are `H₀ = (R, 0)` and `H₁, H₂ = (−R/2, ±(√3/2)R)`: an equilateral triangle of circumradius `R`.
- The embedding is the hyperboloid `−X₀² + X₁² + X₂² = α²`. A hinge at transverse distance `R` sits on it at height
  `X₀ = √(R² − α²) ≥ 0`.
- Throughout, `α > 0` and `R ≥ α`, the range on which (ii) and the tangent length are defined.

## Rows

| Row | Statement (`prop:twoalpha`, P3 l.682; `prop:flip`, l.835) | Lines | p |
|---|---|---|---|
| 11a | (i) ⟺ (ii) ⟺ (iii): `R = 2α` ⟺ `arcsin(α/R) = π/6` ⟺ each side's midpoint lies on the throat. Each side is perpendicular to its midpoint's radius, so a side touching the throat touches it at its midpoint; the inradius is `R/2` | 80–150 | 0.9 |
| 11b | (iv): the circle through the three side midpoints is unique, with centre the origin and radius `R/2`. It also passes through the feet of the altitudes and the midpoints of the vertex–orthocentre segments (orthocentre at the origin), so it is the nine-point circle. It is the throat ⟺ `R = 2α` | 150–250 | 0.8 |
| 11c-v | **At every `R ≥ α`:** every tangent point `T` from `H₀` (`|T| = α`, `⟨T, H₀ − T⟩ = 0`) has `|H₀ − T|² = R² − α²`; such a `T` exists; and the hinge's height on the hyperboloid is `√(R² − α²)`. So tangent length = height for every `R`, and the common value is `√3α` ⟺ `R = 2α` | 60–120 | 0.9 |
| 11c-vi | (vi): `s² = −(2√(R² − α²))² + R²(2 − 2 cos(2π/3)) = 4α² − R²`, so `s² = 0` ⟺ `R = 2α` | 30–60 | 0.95 |
| 11 | The headline: (i)–(vi) are pairwise equivalent, in their formal readings | 20–40 | 0.95 |
| 12 | `prop:flip`: `θ(ψ) = π/2 + iψ` has `θ′ = i`, so `dθ² = θ′² dψ² = −dψ²`; `sin θ(ψ) = cosh ψ`; so `dθ² + sin²θ dΩ²` pulls back to `−dψ² + cosh²ψ dΩ²`, of signature `(−, +)` | 30–60 | 0.95 |

**The expected stop** is 11b's uniqueness. Equal distances from a centre `c` to the three midpoints give two linear
equations in `c`, whose only solution is the origin when `R ≠ 0`. **The fallback** is to state the circle through
the midpoints and leave uniqueness out, which would make 11b BUILT IN PART.

**Interpretive, not formalised:** "the hinge sits there" and "found, not imposed". "Euler's theorem" enters only as
the computation, `N = (O + H)/2` with `O = H = 0`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

# `r7715+71.1` — PRE-REGISTRATION: campaign 118, **6d's core: "a single analytic curve — hyperbola, circle, hyperbola"**. ⌗ `60` new lines (band 40–80), p `0.95`. **Expected stop:** none

*Registered before any Lean. The probe is `probes/CircleConic.lean`, a copy of campaign 117's `CircleMaximal.lean`.
Everything new is prefixed `cn_`.*

## The sentence it backs

**`prop:four_regions`, its first sentence (`corpus/janzen_circle_v3.tex` l.304):** "The maximal analytic completion
of the cycloid is a single analytic curve---hyperbola, circle, hyperbola---with two non-degenerate critical points, at
`z = 0` (`r = 2M`) and `z = π` (`r = 0`)." The same claim is in the introduction (l.95), and l.197 uses the circle.

## Rows

| Stage | Statement | Lines | p |
|---|---|---|---|
| ① | `r(z) = M(1 + cos z)` and `s(z) = M sin z` are entire (differentiable on all of `ℂ`), and `(r − M)² + s² = M²` for every complex `z`: one analytic curve | 15–30 | 0.95 |
| ② | The circle: for real `z = η`, `r` and `s` are real and `(r − M)² + s² = M²` | 10–20 | 0.95 |
| ③ | The two hyperbolas. At `z = iρ`: `r = M(1 + cosh ρ)`, `s = iσ` with `σ = M sinh ρ`, and `(r − M)² − σ² = M²`. At `z = π + iρ′`: `r = M(1 − cosh ρ′)`, `s = −iσ′` with `σ′ = M sinh ρ′`, and `(r − M)² − σ′² = M²`. Each is a branch of the real hyperbola `(r − M)² − σ² = M²`: `r ≥ 2M` on the first and `r ≤ 0` on the second | 20–40 | 0.95 |

**Interpretive, not formalised:** "maximal" in "maximal analytic completion". The completion is the entire function
itself, and nothing extends an entire function further.

**After this, P2's inventory closes:**
- every formal row is built, maximality (a) is built, and 6d's core will be built;
- 8b is interpretive and has no formal core.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

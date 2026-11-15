# `r7783+71.1` — CENSUS AND PRE-REGISTRATION: campaign 140, **P17's cored rows: the intrinsic metric and its one eigenvalue (`prop:unique`), and the tangent to the throat as a null line (`prop:tangentnull`)**. ⌗ `360` lines (band 250–500), p(all eight BUILT) `0.7`

*Registered before any Lean, per r7779 (re-stated at r7783): census P17's cored rows, price them, register, then build
the reachable ones in a new standalone probe. The paper is `corpus/geometric_core_paper.tex` at `e85503396`. The
probe is `probes/GeometricCore.lean` (`gc_`), P17's citable file. Mathlib only.*

*The census covers the statements inside P17's two propositions (l.442, l.839) and the displayed equations they
rest on (`eq:sphere3`, `eq:eigen`, `eq:power`, `eq:powerisheight`). Claims outside the propositions (the
Cayley–Klein reading, the polar slice, the superintegrability count, Remark `rem:onecircle`) are not cored here.*

## Census

### `prop:unique` (l.442) and `eq:sphere3`/`eq:eigen` (l.392–424)
With `s = |x|²`, `g = I + x xᵀ/(α² − s)` on `ℝ⁴` (the paper's case formula entrywise), `λ = α²/(α² − s)`.

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| U1 | **The intrinsic line element.** On `x₀² + |x|² = α²` with `x₀ ≠ 0`, the constraint's differential `x₀ dx₀ = −x·dx` gives `dx₀² + |dx|² = |dx|² + (x·dx)²/(α² − |x|²)`: `eq:sphere3` is the pull-back of `eq:sphere1` | 15–30 | 0.95 | A field identity |
| U2 | **The eigenstructure.** `g` equals the paper's case formula entrywise; `g x = λ x`; `g v = v` for every `v ⊥ x`; and `det g = λ` | 40–80 | 0.85 | `Matrix.det_one_add_col_mul_row` |
| U3 | **The sign of the fourth eigenvalue.** For `x ≠ 0` and `α² ≠ s`: `λ > 0 ↔ α² < 0 ∨ α² > s`; `λ = 0 ↔ α² = 0`; `λ < 0 ↔ s > α² > 0`. So within the family, Lorentzian points exist only for `α² > 0` (de Sitter), exactly at `s > α²` | 15–30 | 0.95 | |
| U4 | **A pole, not a zero.** At fixed `α² > 0`, `λ → +∞` as `s → α²⁻` and `λ → −∞` as `s → α²⁺`, while `det g = λ ≠ 0` everywhere it is defined for `α² ≠ 0`. The `Λ = 0` member is the limit: `λ → 1` as `α² → ±∞` | 40–70 | 0.8 | One-sided limits of `α²/(α² − s)` |
| U5 | **The uniqueness.** De Sitter is the only maximally symmetric real pseudo-Riemannian manifold with intrinsic Lorentzian signature | — | — | **Beyond**: a classification of maximally symmetric pseudo-Riemannian manifolds (constant curvature, space forms) Mathlib lacks. Within the family `eq:sphere3`, its content is U3 |

### `prop:tangentnull` (l.839) and `eq:power`/`eq:powerisheight` (l.820–833)
Stated in a real inner-product space `E` (the overhead projection), with the throat the sphere `|T| = α`, and the
substrate `−x₀² + |X|² = α²` in `ℝ × E` with `η = −dx₀² + |dX|²`.

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| T1 | **Euclid III.36 by Pythagoras.** If `|T| = α` and `⟪T, P − T⟫ = 0`, then `|P − T|² = |P|² − α² = pow(P)` | 10–20 | 0.95 | |
| T2 | **The tangents exist.** In the plane, every `P` with `|P| > α > 0` has two tangency points, `T± = (α²/|P|²) P ± (α√pow/|P|²) P^⊥`; each has `|T±| = α` and `⟪T±, P − T±⟫ = 0` | 30–60 | 0.85 | Coordinates on `ℝ²` |
| T3 | **The tangent is null.** If `(x₀, X)` is on the substrate (`x₀² = pow(X)`, `eq:powerisheight`) and `T` is a tangency point of `X`, then `(0, T)` is on the substrate and the displacement `(x₀, X − T)` has `η = 0`. The in-plane restriction of `η` is positive definite (`η(0, v) = |v|² > 0` for `v ≠ 0`), so the null vector is the lifted one | 15–30 | 0.95 | |
| T4 | **Touch and cut.** On the line `P + t u` (`|u| = 1`), the meeting points with the throat are the roots of `t² + 2⟪P, u⟫ t + pow(P) = 0`, with product `pow(P)` (the power of a point). From the lift of an outside `P`, the displacement to a meeting point is null exactly when the two roots coincide: a tangent's point of contact is null, a secant's two points are not | 40–80 | 0.85 | |

**Totals.** 2 statements, **9 cored rows**, **8 within reach** (U1–U4, T1–T4). U5 is priced as beyond.

## Registration: campaign 140
- **Rows:** U1, U2, U3, U4, T1, T2, T3, T4, in `probes/GeometricCore.lean`.
- **Price:** 360 lines (band 250–500). p(all eight BUILT) `0.7`.
- **The expected stop is U4's one-sided limits.** **The fallback** is to state the pole as unboundedness (`∀ B, ∃ s` near `α²` with `λ > B`, and with `λ < −B`), marked BUILT IN PART.
- **Non-vacuity:** witnesses at concrete values:
  - `α² = 1`, `x = (2, 0, 0, 0)` (`λ = −1/3 < 0`, U2–U3);
  - `α² = 4`, `x = (1, 0, 0, 0)` (`λ = 4/3 > 0`);
  - `α = 1`, `P = (2, 0)`, `T = (1/2, √3/2)`, `x₀ = √3` (T2–T3);
  - a secant through `P = (2, 0)` along `u = (−1, 0)`, roots `1` and `3` (T4).

**Interpretive, not formalised:**
- "the signature and the throat are what its positive curvature *is*";
- "the imaginary fifth coordinate is a property of one embedding picture";
- "the tangent is exactly where the light cone is";
- the identification of the rulings with the tangents.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

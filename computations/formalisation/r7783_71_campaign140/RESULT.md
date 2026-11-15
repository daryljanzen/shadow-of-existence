# `r7783+71.2` — RESULT: campaign 140, **P17's eight reachable rows all BUILT (U1–U4, T1–T4). P17 stands at 8 of 9; U5 (the uniqueness) is priced as beyond.** ⌗ `332` lines (band 250–500, estimate 360, **in band**), at p(all eight) `0.7`

*The census and registration are `PREDICTION.md`. The probe is the new standalone file `probes/GeometricCore.lean`
(`gc_`), P17's citable file.*

## Verification
- `lake env lean probes/GeometricCore.lean` gives **0 errors and 0 warnings**.
- **14 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29. No options are
  set.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| U1 | `gc_line_element`: on `x₀² + x·x = α²` (`x ∈ ℝ⁴`, `x₀ ≠ 0`) with `x₀ dx₀ + x·dx = 0`, `dx₀² + dx·dx = dx·dx + (x·dx)²/(α² − x·x)`: `eq:sphere3` is the pull-back of `eq:sphere1` | **BUILT** |
| U2 | `gc_g_entry`: `g = 1 + (α² − x·x)⁻¹ x xᵀ` is `eq:eigen`'s case formula entry by entry. `gc_eigen`: `g x = λ x`; `g v = v` for `x·v = 0`; `det g = λ`, with `λ = α²/(α² − x·x)` (by the matrix determinant lemma) | **BUILT** |
| U3 | `gc_sign`: for `s > 0`, `λ > 0 ↔ α² < 0 ∨ s < α²`; `λ = 0 ↔ α² = 0 ∨ α² = s` (the second is outside `g`'s domain); `λ < 0 ↔ 0 < α² < s` | **BUILT** |
| U4 | `gc_pole`: at `α² > 0`, `λ → +∞` as `s → α²⁻` and `λ → −∞` as `s → α²⁺`. `gc_det_ne_zero_limit`: `det g ≠ 0` wherever `g` is defined and `α² ≠ 0`; `λ → 1` as `α² → ±∞` (the `Λ = 0` member) | **BUILT** |
| U5 | De Sitter is the only maximally symmetric real pseudo-Riemannian manifold with intrinsic Lorentzian signature | **NOT BEGUN** (beyond: a classification of maximally symmetric spaces) |
| T1 | `gc_tangent_sq` (any real inner-product space): `‖T‖ = α`, `⟪T, P − T⟫ = 0` ⟹ `‖P − T‖² = ‖P‖² − α²` | **BUILT** |
| T2 | `gc_tangents` (on `ℝ²`): for `|P|² > α² > 0`, `T± = (α²/q)P ± (α√(q − α²)/q)P^⊥` lie on the throat, are points of tangency, have tangent length² `= pow(P)`, and are distinct | **BUILT** |
| T3 | `gc_tangent_null`: for `(x₀, X)` with `−x₀² + ‖X‖² = α²` and `T` a tangency point, `(0, T)` is on the substrate and `−x₀² + ‖X − T‖² = 0`; the in-plane form `η(0, v) = ‖v‖²` is positive for `v ≠ 0` | **BUILT** |
| T4 | `gc_meet`: `P + t u` (`‖u‖ = 1`) meets the throat ⟺ `t² + 2⟪P, u⟫t + pow(P) = 0`. `gc_power`: for a secant, `t₁t₂ = pow(P)`. `gc_touch_cut`: for `pow(P) > 0` and `x₀² = pow(P)`, a secant's meeting points are not null from the lift, and a tangent's single point is null | **BUILT** |

**Witnesses** (`gc_witness`):
- a Lorentzian point (`α² = 1`, `x = (2, 0, 0, 0)`, `λ = −1/3`) with its eigenvector;
- a Riemannian point (`α² = 4`, `x = (1, 0, 0, 0)`, `λ = 4/3`);
- `T = (1/2, √3/2)` from `P = (2, 0)` to the unit throat, with the lifted tangent null at `x₀ = √3`;
- the secant through `P = 2` along `u = −1` (on the inner-product space `ℝ`), meeting the throat at `t = 1, 3`, with
  `1·3 = pow(P)` and the meeting point not null.

**Against the registration:**
- **The named stop did not hold.** U4's one-sided limits closed through `inv_tendsto_nhdsGT_zero`/`nhdsLT_zero`, so
  the fallback was not needed.
- **U3's zero case is `α² = 0 ∨ α² = s`.** The second disjunct is where `λ`'s denominator vanishes (Lean's `x/0 = 0`)
  and lies outside `g`'s domain. Under U2's hypothesis `α² ≠ s` it reads as the paper's `λ = 0 ↔ α² = 0`.
- **T4's tangent case is stated as "the only meeting parameter".** The proof uses the quadratic's other root
  `−2⟪P, u⟫ − t`, which is also a meeting point.
- **U1 and U2 are on `ℝ⁴`** (the paper's dimension); the T rows hold in any real inner-product space, and T2 is on `ℝ²`.

**P17 tally: 8 of 9 cored rows BUILT** (U1–U4, T1–T4).
- **U5** (`prop:unique`'s uniqueness) is NOT BEGUN, priced as beyond. Within the family `eq:sphere3`, its content is
  U3.
- **Not formalised (interpretive):** "the signature and the throat are what its positive curvature *is*"; "the
  imaginary fifth coordinate is a property of one embedding picture"; "the tangent is exactly where the light cone
  is"; the identification of the rulings with the tangents.
- **Outside the census** (not in a proposition): the Cayley–Klein reading, the polar slice, the superintegrability
  count, and Remark `rem:onecircle`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

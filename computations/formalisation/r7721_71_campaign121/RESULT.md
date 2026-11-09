# `r7721+71.2` — RESULT: campaign 121, **P3's hinge (`prop:twoalpha`, all six) and the flip (`prop:flip`) are BUILT, and tangent length = height at every `R` is a theorem.** ⌗ `239` new lines, **below** the registered band of 300–650 (point `450`). ⌗ p `0.8` came true. The expected stop, the circle's uniqueness, fell without the fallback

*Against `PREDICTION.md` (`r7721+71.1`). 71 ran `lake env lean probes/SlicingHinge.lean`. It exits 0 with no errors
and no warnings. All `664` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `654` inherited and
`10` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 120's `SlicingSky.lean`, with everything new in `section SlHinge`.*

**Setting.** The transverse plane is `ℝ²`, with the axis at the origin and the throat the circle of radius `α > 0`.
The hinges are `H₀ = (R, 0)` and `H₁, H₂ = (−R/2, ±(√3/2)R)`, and `R ≥ α`.

## Why the line count is low

In coordinates, every clause is a polynomial identity in `R`, `α` and `√3`. Most proofs reduce to `ring_nf` followed
by `√3² = 3`. The uniqueness of the circle through the midpoints is two linear equations in its centre.

## Row 11a, (i) ⟺ (ii) ⟺ (iii) — BUILT

- **`sl_hinge_equilateral`:** the hinges are at distance `R` from the axis and pairwise `√3R` apart.
- **`sl_hinge_midpoints`:** each side's midpoint is at distance `R/2`, and the side is perpendicular to the
  midpoint's radius. So the foot of the perpendicular from the axis is the midpoint, and the inradius is `R/2`.
- **`sl_hinge_arcsin`:** `arcsin(α/R) = π/6 ⟺ R = 2α`.
- **`sl_hinge_tangent_mid`:** the sides touch the throat at their midpoints ⟺ `R = 2α`.

## Row 11b, (iv) — BUILT

- **`sl_ninepoint_unique`:** a circle `(c, ρ)` passes through the three side midpoints ⟺ `c` is the axis and
  `ρ² = (R/2)²`.
- **`sl_ninepoint`:**
  - each altitude passes through the axis, so the orthocentre is the axis;
  - each foot of an altitude is the opposite side's midpoint;
  - the midpoints of the vertex–orthocentre segments are at distance `R/2`.
  - So the unique circle through the side midpoints carries all nine points, with centre `N = (O + H)/2 = 0`.

## Row 11c, (v) and (vi) — BUILT

- **`sl_tangent_height` (v), at every `R ≥ α`:**
  - every tangent point `T` from `H₀` (`|T| = α`, `⟨T, H₀ − T⟩ = 0`) gives `|H₀ − T|² = R² − α²`;
  - such a `T` exists, namely `(α²/R, α√(R² − α²)/R)`;
  - on the hyperboloid `−X₀² + X₁² + X₂² = α²`, the hinge's height `X₀ ≥ 0` is exactly `√(R² − α²)`;
  - so **tangent length = height for every `R`**, which is P17's `prop:tangentnull`, now machine-checked;
  - and the common value is `√3α ⟺ R = 2α`.
- **`sl_hinge_null` (vi):** `s² = −(2√(R² − α²))² + R²(2 − 2 cos(2π/3)) = 4α² − R²`, and `s² = 0 ⟺ R = 2α`.

## Row 11, the headline — BUILT

- **`sl_twoalpha`:** for `0 < α ≤ R`, each of (ii)–(vi) ⟺ (i) `R = 2α`, in the formal readings above. For (iv), the
  reading is "every circle through the three midpoints is the throat".

## Row 12, `prop:flip` — BUILT

- **`sl_flip`:**
  - `θ(ψ) = π/2 + iψ` has `θ′ = i`, so the `dθ²` coefficient pulls back to `i² = −1`;
  - `sin θ(ψ) = cosh ψ`, so `sin²θ` pulls back to `cosh²ψ`;
  - the coefficients `−1 < 0 < cosh²ψ` give signature `(−, +)`.
- "The flip is not imposed" stays interpretive.

## Marks (P3's inventory, `r7717_71_survey/SURVEY.md`)

- **Built (19):** 1a, 1b, 2, 3, 4, 5a–c, 6a–b, 7, 9a–b, 10, 11a, 11b, 11c, 12 and 13b.
  - **13b ⇧ moved:** `sl_curvature_sign` (campaign 120) already proves `−f′/2r = 1 − M/r³` in the chain.
- **Built in part (2):**
  - **1c:** the limit at the root remains.
  - **13a:** `K_G = −r″/r`, or the Levi-Civita curvature, remains.
- **Not begun:** none.
- **No formal core (3):** 8, 14 and 15.

**Next (campaign 122):** 13a, the Gaussian curvature of `dl² + r(l)² dφ²`, and 1c, the limit `r″ → ±½ f′(r_h)` at a
simple root. Together they would close P3.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

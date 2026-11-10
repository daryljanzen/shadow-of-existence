# `r7731+71.2` — RESULT: campaign 126, **P8's three leaves are BUILT (rows 5a–c). P8 is closed: 15 of 16 rows BUILT, and the 16th (5d) has no formal core. 60's two stale headers are fixed.** ⌗ `+372 / −2` lines, inside the registered band of 300–850 (point `500`). ⌗ p `0.55` came true. The expected stop, the pullback metric, fell, and no fallback was used

*Against `PREDICTION.md` (`r7731+71.1`). 71 ran `lake env lean probes/StaticEinstein.lean`. It exits 0 with no errors
and no warnings. All `59` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `37` from campaigns
123–125 and `22` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE. `OperatorKernel.lean` still builds clean after its docstring change.*

**All of it is in `probes/StaticEinstein.lean`, the file P8 cites,** in a new `section LfLeaves` (prefix `lf_`).
No earlier name changes.

## The two general theorems

- **`lf_curv`:** take `g = R²(dχ² + S(χ)²(dθ² + sin²θ dφ²))` on `Fin 3`, with `S′ = D`, `D′ = −kS` and
  `D² + kS² = 1`, at any point with `R, S(χ), sin θ ≠ 0`. Then `R_{abcd} = (k/R²)(g_ac g_bd − g_ad g_bc)` for all 81
  `(a, b, c, d)`.
  - This is computed from the chain's `kr_Riem`, through a 27-entry Christoffel table (`lf_Γ`).
- **`lf_pull_eq`:** the chart `Φ = (U₀(χ), U₁(χ), R S(χ) n̂(θ, φ))` into `M^{1,4}` has induced metric
  `Σ_A ε_A ∂_iΦ^A ∂_jΦ^A = diag(−U₀′² + U₁′² + R²S′², R²S², R²S² sin²θ)`.

## Rows 5a–5c, `prop:trichotomy` (P8 l.427) — BUILT

- **5a, the closed leaf.**
  - `lf_closed_set`: on the hyperboloid, `X₀ = c` ⟺ `X₀ = c` and `X₁² + … + X₄² = α² + c²`.
  - `lf_S3_on`: the chart `(c, R cos χ, R sin χ n̂)` with `R² = α² + c²` lies on that leaf.
  - `lf_S3_pull`: its induced metric is `R²(dχ² + sin²χ dΩ²)`.
  - `lf_closed`: `R_{abcd} = (1/(α² + c²))(g_ac g_bd − g_ad g_bc)`. This is `lf_curv` with `S = sin` and `k = 1`.
- **5b, the flat leaf.** Here `B = (1, 1, 0, 0, 0)` is null (`lf_B_null`).
  - `lf_horo_leaf`: for `s ≠ 0`, the chart `y ↦ (X₀(y), X₀(y) + s, y)` is a bijection from `ℝ³` onto
    `{η(X, X) = α², η(X, B) = s}`.
  - `lf_horo_pull`: its induced metric is `δ_ij`. The two null-direction terms cancel because `X₁ − X₀` is constant.
  - `lf_flat`: every `R^a_{bcd} = 0`.
- **5c, the open leaf.**
  - `lf_open_set`: on the hyperboloid, `X₁ = b` gives `X₀² − (X₂² + X₃² + X₄²) = b² − α²`. For `0 ≤ α < b`, every
    point has `X₀ ≠ 0`, so the section has two sheets.
  - `lf_H3_on` and `lf_H3_pull`: the chart `(A cosh ρ, b, A sinh ρ n̂)` with `A² = b² − α²` lies on that leaf and
    induces `A²(dρ² + sinh²ρ dΩ²)`.
  - `lf_open`: curvature `−1/(b² − α²)`. This is `lf_curv` with `S = sinh` and `k = −1`.
- **Non-vacuity, `lf_witness`:**
  - the closed leaf of `α = 1`, `c = 0`, at `χ = θ = π/2`, has `R_{0101} = 1`;
  - the open leaf of `α = 1`, `b = √2`, at `ρ = 1`, has `R_{0101} = −sinh²1 ≠ 0`;
  - the flat chart of `α = s = 1` puts the origin on its leaf.
- **Scope, as P8 states it:**
  - The curved charts' curvature is proved where the chart is regular (`sin χ` or `sinh ρ` non-zero, and
    `sin θ ≠ 0`).
  - The flat leaf is the level `s ≠ 0`. P8's horospheres have `η(X, B) = ½α²e^{τ/α} > 0`.
- **5d** ("they carry `k = +1, 0, −1`"): the signs are `lf_curv`'s `k`. The FLRW reading of `k` stays
  interpretive. **No formal core**, as surveyed.
- **Interpretive, not formalised:** eq. `openembed` (the open slicing).

## 60's two stale headers

- **`OperatorKernel.lean`:** "It backs P8: `thm:kernel` and `prop:bend`" now reads that the file is superseded by
  `probes/StaticEinstein.lean` as P8's citable file, and is the frozen campaign-123 record.
- **`StaticEinstein.lean`:** the kept campaign-123 header is now introduced as that section's header. A note says
  its "copies no earlier probe" is true of `OperatorKernel.lean` and not of this file.

## Marks (P8's inventory, `r7725_71_survey/SURVEY.md`)

- **Built (15):** 1a–1e, 2, 3a–3c, 4a–4c and 5a–5c.
- **No formal core (1):** 5d.
- **P8 is closed.**

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

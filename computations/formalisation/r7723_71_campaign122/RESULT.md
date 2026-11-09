# `r7723+71.2` — RESULT: campaign 122, **13a, 1c and the continued surface's curvature are BUILT. On the Lorentzian piece, `K = 1 − M/ρ³`: the analytic continuation of the static formula, with no sign change at the seam. The de Sitter member has `K = 1` on both sides.** P3's formal rows are all built: 21 of 24, with the other 3 having no formal core. ⌗ `325` new lines (band 300–650; point `450`). ⌗ p `0.7` came true. The expected stop fell without the fallback

*Against `PREDICTION.md` (`r7723+71.1`). 71 ran `lake env lean probes/SlicingCurvature.lean`. It exits 0 with no
errors and no warnings. All `678` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `664`
inherited and `14` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE. The probe copies campaign 121's `SlicingHinge.lean`, with everything new in
`section SlCurv`.*

**The curvature used.**
- It is campaign 110's coordinate Riemann tensor (`kr_Γ`, `kr_Riem`, `kr_Rlow`) on `Fin 2`, with
  `K := R₀₁₀₁ / det g`.
- In two dimensions this is half the Ricci scalar for either signature.
- **Sanity check:** `sl_gauss_hyperbolic` gives `K = −1` on `dl² + cosh² l dφ²`.

## Row 13a, `prop:curvature` — BUILT

- **`sl_gauss_g2`:** for `g = diag(ε, r(t)²)` with `ε ≠ 0`, `r` differentiable, `r ≠ 0` at the point, and `r′`
  differentiable there with derivative `r″`, `K = −r″/(εr)`.
  - This was the expected stop: the Christoffel symbols of a general profile (`sl_g2_Γ`), then `kr_pd_congr` on the
    open set `r ≠ 0`. It followed campaign 110's sphere proof.
- **`sl_curvature_static`:** on the slicing surface `dl² + r(l)² dφ²` (`ε = 1`), `K = −r″/r`. On the static region
  (`r′ = √f`, `f > 0`) this is `1 − M/r³` (gauge `α = 1`).

## Row 1c, `prop:turning` — BUILT

- **`sl_turning_limits`:** at a simple root `r_h ≠ 0` (`3r_h² ≠ 1`):
  - along `r′ = √|f(r)|`, `r″ = sl_A(r)` wherever `f(r) ≠ 0`, which is `+½f′(r)` where `f > 0` and `−½f′(r)` where
    `f < 0`;
  - `f` takes both signs arbitrarily close to `r_h`, so both one-sided filters are non-trivial (`sl_sign_change`);
  - `sl_A → +½f′(r_h)` from the `f > 0` side and `→ −½f′(r_h)` from the `f < 0` side;
  - and `f′(r_h) ≠ 0`.
- This is `prop:turning` as 69 now states it.

## The added question: the curvature of the continued surface — BUILT, and the answer

- **`sl_seam_square`:** `dl = i dψ` turns `(dr/dl)² = f` into `(dρ/dψ)² = −f`.
- **`sl_curvature_continued`:** on the Lorentzian piece `−dψ² + ρ(ψ)² dφ²` (`ε = −1`), with `ρ′ = √|f(ρ)|` and
  `f < 0`, `K = ρ″/ρ = 1 − M/ρ³`.
- **`sl_curvature_dS`:** the de Sitter member `−dψ² + cosh²ψ dφ²` (`sl_flip`'s image) has `K = 1 = 1/α²`.
- **`sl_curvature_witness` (non-vacuity):** both theorems' hypotheses are met by explicit de Sitter solutions:
  - `sl_W₁(l) = sin(clamp l)`, clamped onto `[−π/2, π/2]`, solves `r′ = √|1 − r²|` everywhere (`sl_W₁_ode`). At
    `l = π/4`, `K = 1`.
  - `sl_W₂(ψ) = cosh(max ψ 0)` solves `ρ′ = √|1 − ρ²|` everywhere (`sl_W₂_ode`). At `ψ = 1`, `K = 1`.
  - The gluing lemmas are `sl_max_deriv` and `sl_min_deriv`, which glue at a stationary point.

**The answer.**
- **On the Lorentzian far side, the Gaussian curvature is the same expression, `1/α² − M/r³`:** the analytic
  continuation of the static formula, not its negative.
- The registered expectation came true.
- **So P3's curvature statements can carry the far side unchanged,** read as `prop:flip`'s Lorentzian
  continuation. The de Sitter member is the constant `1/α²` on both sides of the seam.
- **The sign flip of campaign 120's `sl_curvature_sign` belongs only to the `|f|` reading,** a Riemannian surface
  past the horizon with `(dr/dl)² = |f|`. There `K = −r″/r = +f′/2r`.
- **What makes the difference:** the continuation flips both `ε` (`dl² → −dψ²`) and the sign of `r″`. Together
  they leave `K = −r″/(εr)` unchanged.

## Marks (P3's inventory, `r7717_71_survey/SURVEY.md`)

- **Built (21):** 1a, 1b, 1c, 2, 3, 4, 5a–c, 6a–b, 7, 9a–b, 10, 11a–c, 12, 13a and 13b. Every row with formal
  content.
- **No formal core (3):** 8 (`prop:gnomonic`), 14 (`prop:rigidity`) and 15 (`prop:morphism-generation`).
- **P3's formalisation closes.**

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

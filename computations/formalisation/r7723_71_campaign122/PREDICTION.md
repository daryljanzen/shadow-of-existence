# `r7723+71.1` — PRE-REGISTRATION: campaign 122, **P3's curvature (13a), the one-sided limits at a simple root (1c), and the curvature of the continued surface**. ⌗ `450` new lines (band 300–650), p `0.7`. **Expected stop:** the coordinate Riemann tensor of `diag(ε, r(t)²)` for a general profile `r`

*Registered before any Lean. The probe is `probes/SlicingCurvature.lean`, a copy of campaign 121's
`SlicingHinge.lean`. Everything new is prefixed `sl_`, in `section SlCurv`. The curvature is campaign 110's coordinate
machinery (`kr_Γ`, `kr_Riem`, `kr_Rlow`) on `Fin 2`. The Gaussian curvature of a 2-metric is
`K := R_{0101}/det g`, which is `+1/ρ²` on campaign 110's round sphere (`kr_sph`).*

## Rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 13a | For `g = diag(ε, r(t)²)` with `ε = ±1`, `r` nowhere zero and twice differentiable: `K = −r″/(εr)`. With `ε = +1`, the surface `dl² + r(l)² dφ²` of `prop:curvature` has `K = −r″/r` | 150–300 | 0.75 |
| 13a, SdS | On the static region (`f > 0`, `r′ = √f`), `K = 1/α² − M/r³` (`α = 1`), with `sl_accel_pos` | 30–60 | 0.9 |
| 1c | At a simple root `r_h ≠ 0` (`3r_h² ≠ 1`), `f` takes both signs arbitrarily close to `r_h` (both one-sided filters are non-trivial). `r″`, read through `sl_accel_pos`/`neg` as `+½f′(r)` where `f > 0` and `−½f′(r)` where `f < 0`, tends to `+½f′(r_h)` from the `f > 0` side and to `−½f′(r_h)` from the `f < 0` side. Both limits are non-zero | 100–200 | 0.8 |
| Added | **The continued surface.** With `ε = −1` and `ρ′ = √|f(ρ)|` where `f < 0` (`dl = i dψ` turns `(dr/dl)² = f` into `(dρ/dψ)² = −f`), the Lorentzian piece `−dψ² + ρ(ψ)² dφ²` has `K = ρ″/ρ = 1 − M/ρ³`. **That is the same expression, the analytic continuation of `1/α² − M/r³`, with no sign change at the seam.** On the de Sitter member, `ρ = cosh ψ` gives `K = 1 = 1/α²` | 60–120 | 0.85 |

**What I expect it to show:**
- **On the Lorentzian far side, the curvature is the continuation of the static formula, not its negative.** So
  P3's curvature statement carries across the seam unchanged.
- **The sign flip of campaign 120's `sl_curvature_sign` belongs only to the `|f|`-reading:** a Riemannian surface
  past the horizon. 69's edit to `prop:curvature` (static region only) is consistent with this.
- **If Lean says otherwise, that is reported as found.**

**The expected stop** is the Riemann tensor of `diag(ε, r²)` with `r` a general function: `kr_pd` of
`Γ¹₀₁ = r′/r` needs `r′` differentiable at the point. The plan is to follow campaign 110's `kr_sph` proof
(`fin_cases` plus `kr_pd_congr`). **The fallback** is to state 13a for the `C^∞` profile `r = cosh`/`sin` only.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

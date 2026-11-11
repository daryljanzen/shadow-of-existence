# `r7739+71.1` — PRE-REGISTRATION: campaign 130, **P5's last four rows by copy (2b, 7a, 9, 10), which close P5 at 17 of 18**. ⌗ `1550` new lines (band 1450–1700), p `0.85`, of which about `1480` are a verbatim copy. **Expected stop:** none serious. The risk is scoping and notation inside `Groupoid.lean`

*Registered before any Lean. A trial build of the copied sections, standalone on Mathlib, compiled with no errors
before this registration.*
- **Everything goes into `probes/Groupoid.lean`,** P5's citable file.
- **The copy.** `SlicingCurvature.lean`'s sections `KrCurvature` (462 lines) and `SlCubic`, `SlSky`, `SlHinge` and
  `SlCurv` (1018 lines) are copied verbatim into namespace `ShadowProbe.SlicingCurvatureProbe`, with every name kept.
  - `SlCubic` through `SlCurv` are P3's campaigns 119–122. Rows 9 and 10's kit (`sl_flip`, `sl_curvature_static`)
    sits in `SlHinge` and `SlCurv`, and `SlCurv` uses `KrCurvature`'s coordinate Riemann tensor.

## Rows

| Row | Statement | Source | Lines | p |
|---|---|---|---|---|
| 2b | In `r₀ = (2/√3) sin w` with `cos w ≥ 0`, `σ` is `r₀ ↦ (−r₀ + √(4 − 3r₀²))/2` = `(2/√3) sin(π/3 − w)` | `sl_σ_sin` | copy | 0.95 |
| 7a | `σ(r₀) = r₀ ⟺ r₀ = 1/√3` on the admitted range, where the two non-fixed roots collide | `sl_σ_fixed`, `sl_nariai` | copy | 0.95 |
| 9 | `ξ : θ ↦ π/2 + iψ` has `dθ = i dψ`, `i² = −1` and `sin(π/2 + iψ) = cosh ψ`: the signature flip | `sl_flip` | copy | 0.95 |
| 10 | `K_G = 1 − M/r³` on the static slicing surface (`α = 1`), from the coordinate Riemann tensor; **new:** `K_G → −∞` as `r → 0⁺` for `M > 0` (`gp_KG_diverges`) | `sl_curvature_static` + new | copy + 20–50 | 0.85 |

**Non-vacuity** is carried by the copied witnesses (`sl_curvature_witness`, `sl_σ_fixed`'s explicit values) and by
the divergence statement.

**Interpretive, not formalised:** row 9's "`ξ² = id` as a swap of two descriptions", and row 10's "pivot",
"artefact" and "identical through first order".

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

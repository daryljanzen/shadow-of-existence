# `r7703+71.2` — RESULT: campaign 112, **all registered rows BUILT: `prop:cycloid` in its corrected `E = 0` form on the interior chart (1a, all three stages, and 1b), the patch ranges (6a), the `r < 0` exclusion (6c), both continuations' coefficient identities (4a, 5a), and the 4D interior form (2b).** ⌗ `15972` lines in one probe (`574` new, just under the registered band of 600–1150). ⌗ p `0.55` for the whole came true. The expected stop at 1a-③ did not occur; its registered fallback, the closed-form Christoffel symbols of a diagonal 2×2 metric, was used as the route

*Against `PREDICTION.md` (`r7703+71.1`). 71 ran `lake env lean probes/CircleCycloid.lean`. It exits 0 with no errors
and no warnings. All `544` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `507` inherited and
`37` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 111's `CircleKretschmann.lean`.*

## 1a and 1b: `prop:cycloid`, corrected, on the interior chart — BUILT

**① Proper time (and 1b).**
- **`cy_proper_time`:** `∫₀^η 2M cos²(s/2) ds = M(η + sin η)`.
- **`cy_Mpi`:** from `η = 0` (`r = 2M`) to `η = π` (`r = 0`), the proper time is `Mπ`.
- **`cy_τ_strictMonoOn`:** `τ(η) = M(η + sin η)` is strictly increasing on `[0, π]`.
- **The inverse `cy_η`:** `η(τ)` on `[0, Mπ]` (`cy_η_spec`, `cy_η_τ`), mapping `(0, Mπ)` into `(0, π)`, with
  `dη/dτ = 1/(M(1 + cos η))` (`cy_hasDerivAt_η`).

**② The radial equation.**
- **`cy_radial`:** along `r(τ) = M(1 + cos η(τ))`, `dr/dτ = −sin η/(1 + cos η)` and `(dr/dτ)² = 2M/r − 1`. That is
  `E² − 1 + 2M/r` with `E = 0`, the corrected statement's first line.
- **`cy_ends`:** as `τ → 0⁺`, `r → 2M` and `dr/dτ → 0`, so the geodesic is at rest at `r = 2M`. As `τ → Mπ⁻`, `r → 0`.

**③ The geodesic.**
- **`cy_diag_Γ`:** the Christoffel symbols (campaign 110's `kr_Γ`) of `diag(A(x⁰), B(x⁰))`. The non-zero ones are
  `Γ⁰₀₀ = A′/2A`, `Γ⁰₁₁ = −B′/2A` and `Γ¹₀₁ = Γ¹₁₀ = B′/2B`.
- **`cy_g`:** the chart metric `−4M²cos⁴(η/2) dη² + tan²(η/2) dt²`, written as
  `diag(−(M(1 + cos η))², (1 − cos η)/(1 + cos η))`. 2b proves the two forms equal.
- **`cy_geodesic`:** on `0 < τ < Mπ`, the curve `c(τ) = (η(τ), t₀)` satisfies `c″ᵃ + Γᵃ_bd c′ᵇ c′ᵈ = 0`
  (`cy_IsGeodesic`). It is unit timelike, `g(c′, c′) = −1`, and its Killing energy is `E = −g(c′, ∂_t) = 0`.

## 2b — BUILT

**`cy_interior_forms`,** on `0 < η < π` with `r = M(1 + cos η)`:
- `g_tt = 2M/r − 1 = tan²(η/2) = (1 − cos η)/(1 + cos η)`;
- `g_rr (dr/dη)² = (1 − 2M/r)⁻¹ (M sin η)² = −4M²cos⁴(η/2) = −(M(1 + cos η))² = −(dτ/dη)²`;
- `r² = M²(1 + cos η)²`.

So both of P2's forms, `eq:interior_metric` and `eq:interior_metric_eta`, hold, with the sphere factor written in.

## 4a and 5a — BUILT

- **`cy_regionI_coeffs`,** at `z = iρ` with `dz/dρ = i`:
  - `−4M²cos⁴(z/2)·i² = 4M²cosh⁴(ρ/2)`;
  - `tan²(z/2) = −tanh²(ρ/2)`;
  - `(1 + cos z)² = (1 + cosh ρ)²`.
- **`cy_regionI_schw`,** with `r = M(1 + cosh ρ)` and `ρ ≠ 0`: `1 − 2M/r = tanh²(ρ/2)` and
  `(dr/dρ)²/(1 − 2M/r) = 4M²cosh⁴(ρ/2)`.
- **`cy_backseam_coeffs`,** at `z = π + iρ′`: `−4M²cos⁴(z/2)·i² = 4M²sinh⁴(ρ′/2)` and `tan²(z/2) = −coth²(ρ′/2)`.
- **`cy_backseam_schw`,** with `r = M(1 − cosh ρ′)`: `1 − 2M/r = coth²(ρ′/2)` and
  `(dr/dρ′)²/(1 − 2M/r) = 4M²sinh⁴(ρ′/2)`.

## 6a and 6c — BUILT

- **`cy_patches`:** the six patches' `r`-ranges, each map onto its range:
  - `(0, 2M)` on `η ∈ (0, π)`;
  - the white-hole arc is `η ↦ −η`, with `r` even and `τ` odd;
  - `(2M, ∞)` at `z = ±iρ`;
  - `(−∞, 0)` at `z = π ± iρ′`.
- **`cy_backseam_not_kruskal`:** no point of Kruskal's `{UV < 1}` has `r = M(1 − cosh ρ′)` with `ρ′ > 0`.

## Limits

- **The interior chart `(η, t)` is a coordinate metric, as 69's order reads 1a.** It is not pulled back from the
  Kruskal manifold `sk_S`; that pullback is row 2a.
- **"Analytic continuation of the metric"** is read as substituting into each coefficient's holomorphic extension,
  with `dz² ↦ (dz/dρ)² dρ²`.
- **`ρ ≠ 0` is assumed** in the identification halves of 4a and 5a, where `tanh` or `sinh` vanishes.

## Marks (P2's inventory)

- **BUILT (14):** 1a (on the interior chart), 1b, 2b, 3, 4a, 5a, 6a, 6c, 7a–7e and 8a.
- **Not built (4 formal):** 2a (the chart into Kruskal), 4b (the exterior pullback), 5b (`r < 0` as a geometry) and
  6b (the four `r ≥ 0` patches are exactly Kruskal).
- **Interpretive:** 6d and 8b.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

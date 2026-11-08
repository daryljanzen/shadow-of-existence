# `r7707+71.2` — RESULT: campaign 114, **4b BUILT. The Region I chart is pulled back from the Kruskal manifold: `Ψ*g = 4M²cosh⁴(ρ/2) dρ² − tanh²(ρ/2) dt²`, P2's `eq:Region_I_metric`, with `rK ∘ Ψ = M(1 + cosh ρ)` and `Ψ` injective. 6b is priced in the registration.** ⌗ `16674` lines in one probe (`202` new, inside the registered band of 200–450). ⌗ p `0.85` came true, with no stop

*Against `PREDICTION.md` (`r7707+71.1`). 71 ran `lake env lean probes/CircleExterior.lean`. It exits 0 with no errors
and no warnings. All `586` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `574` inherited and
`12` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 113's `CircleChart.lean`. The manifold is `se_S` on `W`.*

## 4b — BUILT

- **`ce_Ψ`:** `Ψ(ρ, t) = (−σ e^{−t/4M}, σ e^{t/4M})`, with `σ = sinh(ρ/2)·e^{r/4M}` and `r = M(1 + cosh ρ)`.
  **`ce_hK`:** `hK(r) = σ²`, so no square root is needed.
- **`ce_Ψ_mem`:** for `ρ > 0`, `Ψ(ρ, t)` lies in `W` with `U < 0`, which is Region I, the right exterior, and
  `rK(Ψ) = M(1 + cosh ρ)`.
- **`ce_Ψ_inj`:** `Ψ` is one-to-one on `(0, ∞) × ℝ`.
- **`ce_pullback`:** with `∂_ρΨ` and `∂_tΨ` given as `HasDerivAt` (`ce_dρ`, `ce_dt`), and reading through
  `se_hRep`:
  - `g(∂_ρ, ∂_ρ) = 4M²cosh⁴(ρ/2)`;
  - `g(∂_t, ∂_t) = −tanh²(ρ/2)`;
  - `g(∂_ρ, ∂_t) = 0`.

  These are P2's `eq:Region_I_metric` (radial part). By campaign 112's `cy_regionI_schw`, they are also the
  Schwarzschild exterior coefficients at `r = M(1 + cosh ρ)`.
- **`ce_reflection`:** `(U, V) ↦ (−U, −V)` preserves `rK` and the metric `F·gM` coefficient by coefficient. So the
  second exterior, `z = −iρ` in `{U > 0 > V}` and outside `W`, carries the same coefficients.

## What this lifts in P2

`prop:region_I_metric` is now a pullback from the Kruskal manifold, as the interior is (`cc_pullback`). The
coefficient-wise continuation `z = iρ` (`cy_regionI_coeffs`) and the manifold pullback (`ce_pullback`) give the same
metric.

## 6b, priced (in `PREDICTION.md`)

- **The work:** onto (each open quadrant point is hit, `η = arccos(rK/M − 1)`, `t = 2M log(V/U)`), disjointness
  together with the horizons `UV = 0` lying in no patch, and the reflected patches' metric.
- **Price:** 250–450 lines, at p `0.7`.
- **Expected stop:** the inversion at the quadrant boundary, handled by working on the open quadrants.

## Limits

- **The left exterior is coefficient-level only.** It lies outside `W`. Its pullback on Kruskal's own manifold
  `sk_S` (`Pt`, two charts) is not built.

## Marks (P2's inventory)

- **BUILT (16):** 1a, 1b, 2a, 2b, 3, 4a, 4b, 5a, 6a, 6c, 7a–7e and 8a.
- **Not built (2 formal):** 5b (`r < 0` as a geometry) and 6b (priced).
- **Interpretive:** 6d and 8b.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

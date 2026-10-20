# r7465+70 — PREDICTION: PO-90, the sky's ℓ=2-alone suppression against the sector's own cosmic variance (registered before any draw)

**Order:** `r7465`. Take `PO-90`. Its terminating clause (THE_REGISTER, PO-90):
> *"the selective suppression is shown to be within cosmic variance at the level the sector's own Monte Carlo over 10⁴ skies measures"*

## The quantity, fixed now
- **CR's prediction** (P15 §large-scales, the adjudicated exact-transfer depths, receipt `P15_the_low_multipole_depth_gap_closes…`): C₂/C₂^ΛCDM = **0.487**, C₃/C₃^ΛCDM = **0.435**.
- **The shape statistic:** **R = (Ĉ₂/C₂^ΛCDM) / (Ĉ₃/C₃^ΛCDM)**, the quadrupole's suppression relative to the octopole's. CR's expectation-ratio is 0.487/0.435 = **1.12**: the floor starves both together, as the row says.
- **The sky's R** comes from the ranges P15 and `confront_lowell_data.py` already carry. Quadrupole/ΛCDM is 0.15–0.25, and octopole/ΛCDM is 0.58–1.10, depending on the estimator.
  - **Central:** R_obs = 0.20 / 0.84 = **0.238**.
  - **Bracket:** **0.136** (0.15/1.10, the most selective) to **0.431** (0.25/0.58, the least).
  - No new data are fetched. These are the paper's own figures, so the test is the one the paper states.
- **The sector's skies:** Ĉ_ℓ = C_ℓ^CR · χ²_{ν_ℓ}/ν_ℓ, independent between ℓ (Gaussian, isotropic).
  - **Full sky:** ν_ℓ = 2ℓ+1, the narrowest case and the one the row means.
  - **Cut-sky sensitivity arm:** ν_ℓ = f_sky(2ℓ+1) with f_sky = 0.78 (the Planck-mask fraction usually quoted for low-ℓ).
  - **10⁴ skies, as the row specifies, then 10⁶ to fix the tail.** Seed fixed: `20261020`.
- **The p-value:** P(R ≤ R_obs | CR). It is one-sided: the anomaly is a *suppression* of ℓ=2 relative to ℓ=3.
- **The exact check:** under full sky, R/1.12 is exactly F(5,7)-distributed. The Monte Carlo must reproduce the F-distribution CDF to its own sampling error, or the draw is wrong.
- **The verdict rule, fixed now:**
  - **TERMINATES AS A RESULT** (the row closes, within cosmic variance) if p ≥ 0.05 at the central R_obs.
  - **STANDS** if p < 0.01 at every R_obs in the bracket.
  - **BORDERLINE, reported as such** in between. In that case the row stays open, with the p-value replacing "of order three" as its stated size.
- **The comparison arm:** the same p under ΛCDM itself (expectation ratio 1). It shows how much of the discrepancy is the floor's and how much is just the sky's own quadrupole.

| arm | quantity | central | band |
|---|---|---|---|
| **V-a** | MC vs exact F(5,7) CDF at R_obs/1.12, 10⁶ draws | agree to < 3 σ_MC | — |
| **V-b** | **p(CR), full sky, R_obs = 0.238** | **0.055** | **0.03–0.09** |
| **V-c** | p(CR) across the estimator bracket 0.136 → 0.431 | 0.015 → 0.15 | 0.005–0.03 → 0.10–0.22 |
| **V-d** | p(ΛCDM), full sky, central | 0.065 | 0.04–0.10 |
| **V-e** | p(CR), cut sky f_sky = 0.78, central | 0.08 | 0.05–0.13 |
| **V-f** | **the verdict at the rule above** | **BORDERLINE** (60 %); TERMINATES (25 %); STANDS (15 %) | — |

**What I expect the measurement to say, in words:**
- **The floor barely moves the shape's distribution.** p(CR) and p(ΛCDM) differ only by the 1.12 factor.
- **So the "shape the construction does not produce" is, to that same factor, a shape ΛCDM does not produce either.** It is the sky's own low quadrupole, at about the 2σ level.
- Whether that **discharges** PO-90 (the row's second exit, "the discrepancy shown to be the sky's own") or only **re-sizes** it is what the fixed rule above decides. It is not my call after the numbers are in.

**EFFORT:** 1.5 h (1–3).

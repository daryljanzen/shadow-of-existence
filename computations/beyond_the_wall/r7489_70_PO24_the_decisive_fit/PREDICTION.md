# r7489+70 — PREDICTION: PO-24 ①, the decisive fit — n_s on the real sky over the tail windows alone (registered before any fit)

**Order:** `r7489` (69) ①. Fit n_s on the real sky over the same tail windows, with the same pipeline and ℓ_min raised, and compare against 0.9611 + Δ(W). **ω_b is free.** The second half (the factor of three) stays untouched.

## The fits, fixed now
- **Pipeline:** `r7471_70_PO24_tilt_off_the_tail/like.py` and `fit.py`, unchanged in method.
  - Flat ΛCDM with **all six parameters free (ω_b, ω_c, H₀, ln10¹⁰A_s, n_s, τ)** plus A_planck.
  - Planck 2018 `plik_lite` TT/TE/EE, keeping **only bins inside the window** [ℓ_min, ℓ_max] on the covariance. TE and EE stop at 1996.
  - Planck 2018 lensing and the τ prior 0.054 ± 0.007, as in the off-tail fit.
- **The four tail windows** (those at z ≥ 2 in r7471): **700–1760, 1000–1760, 1000–2508, 1400–2508**. **The decisive window is 1000–2508**: the widest tail window, 101 TT bins.
- **Measured shift:** M(W) = n_s(W) − 0.9611. Its error is σ_M = σ_W, the window fit's own Fisher σ (the profile is computed for the decisive window).
  - The off-tail error is not added: 0.9611 is the reference point the prediction is stated against, and the order compares against "0.9611 + Δ(W)".
  - Adding it in quadrature is reported as a sensitivity.

## What M is compared against: two predictions, both fixed now
1. **Δ(W), the receipt's two-parameter tilt absorption** at r = 0.9918: +0.0181, +0.0267, +0.0293, +0.0444 for the four windows (r7471). This is what the order names.
2. **Δ_full(W), the shift the same full-ΛCDM pipeline returns on a mock.** The mock is the off-tail best-fit spectrum (`fit_primary.json`) multiplied by the signature S(ℓ) = exp[−(r²−1)(ℓ/ℓ_D)²], with r = 0.9918 and ℓ_D = 1362.
   - S is applied to TT, TE and EE, since damping acts on all three. It is fitted with the same covariance, noise-free, and starts from the unsignatured best fit.
   - **This is the like-for-like prediction**, because ω_b and the rest may share the absorption. **The verdict is read against Δ_full**, and Δ is reported beside it.
   - Control: the same mock **without** S must return M = 0 to < 0.1σ, or the pipeline is biased and nothing is reported.

## Decision rule (decisive window 1000–2508, against Δ_full)
- **SIGNATURE SEEN:** |M − Δ_full| < 1σ_M and |M| ≥ 2σ_M.
- **SIGNATURE EXCLUDED:** |M| < 1σ_M and |M − Δ_full| ≥ 2σ_M.
- **UNDECIDED:** |Δ_full| < 2σ_M, meaning the window cannot separate the two predictions at 2σ. That is a result the row carries.
- **Otherwise MIXED,** stated with both distances.
- The other three windows are reported with the same three distances. They overlap the decisive one and are not combined.

## Predictions
| arm | quantity | central | band |
|---|---|---|---|
| **D-0** | null mock: M | 0 | < 0.1σ |
| **D-1** | Δ_full(1000–2508) / Δ(1000–2508) | 0.6 | 0.2–1.1 (ω_b and A_s share the absorption) |
| **D-2** | σ_W on 1000–2508 | 0.012 | 0.007–0.022 |
| **D-3** | M(1000–2508) on the sky | 0.000 | −0.020 to +0.020 |
| **D-4** | **verdict** | **UNDECIDED** 45 % · EXCLUDED 35 % · MIXED 12 % · SEEN 8 % | — |
| **D-5** | σ_W on 1400–2508 | 0.020 | 0.010–0.040 |

**What I expect in words:**
- The full fit absorbs part of the signature through ω_b and the amplitude, so Δ_full sits below Δ.
- A tail-only window constrains n_s to about 0.01.
- So the decisive window may not separate CR's shift from zero at 2σ. If it does, the sky's tail n_s sits near the off-tail value, since Planck reports ℓ < 800 and ℓ ≥ 800 consistent.

**EFFORT:** 2 h (1–4).

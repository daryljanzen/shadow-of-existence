# r7471+70 — PREDICTION: PO-24 first half — the tilt constrained off the damping tail, and the displacement weighed against it (registered before any fit)

**Order:** `r7471` (69). The live clause ① of PO-24 (THE_REGISTER): *"the tilt constrained off the damping tail --- low- and mid-ℓ `TT`, `EE`, lensing --- and the displacement weighed against THAT rather than against itself"*. The row's terminating case: *"returns an interval no narrower than the displacement's own window-to-window spread … in that case the sky cannot decide the question"*. The second half (the factor of three) is **not** touched here.

## What is weighed: the displacement, at the settled configuration
- The signature is S(ℓ) = exp[−(r²−1)(ℓ/ℓ_D)²], with **r = 0.9918** (the settled common endpoint, r6797/r6801) and ℓ_D = 1362.
- The displacement Δ(W) is the n_s shift a tilt absorbs when fitted over window W. Machinery: the joint-fit receipt `P15_the_joint_fit_leaves_the_gaussian_and_the_bound_was_chi2_not_sigma`, with its own baseline, binning and covariance and its **six windows unchanged**: 100–1760, 700–1760, 1000–1760, 1000–2508, 1400–2508, 100–2508.
  - That receipt's table is at r = 1.0926. **Δ(W) is recomputed at r = 0.9918**, not scaled.
  - Expectation from the row's own linear (r²−1) scaling (factor −0.0843): Δ ≈ +0.007, +0.018, +0.026, +0.029, +0.044, +0.008.
- **Spread S = max Δ(W) − min Δ(W)** over the six windows.

## The tilt off the damping tail: data, cut and model, fixed now
- **Data:**
  - **Planck 2018 `plik_lite` TT+TE+EE** (the repo's copy, `computations/planck_tt_likelihood/data/planck2018_plik_lite`, its covariance restricted to the kept bins), **bins with ℓ_max^bin ≤ 800**.
  - **Plus Planck 2018 lensing**: the conservative 9-bin φφ bandpowers and covariance, `smicadx12_Dec5_ftl_mv2_ndclpp_p_teb_consext8`, fetched from the Cobaya supplementary-data mirror. The linear CMB-dependence correction is **not** applied, an approximation stated here.
  - **Plus a Gaussian prior τ = 0.054 ± 0.007**, standing in for low-ℓ EE. The low-ℓ (ℓ<30) TT and EE likelihoods are not available here, and that absence is part of the result.
- **Why 800:** the split Planck itself uses for low/high ℓ. The signature at ℓ = 800 is exp[−(r²−1)·0.345], under 0.6 % of the spectrum at r = 0.9918, so the fit does not run through the tail.
- **Sensitivity arms:** ℓ_max = 650 and 1000. TT+TE+EE without lensing. TT alone at ℓ ≤ 800.
- **Model:** flat ΛCDM, the six parameters (ω_b, ω_c, θ_MC via H₀, ln10¹⁰A_s, n_s, τ), plus plik_lite's calibration A_planck with its prior 1 ± 0.0025. CAMB 2.0.4, lensed C_ℓ.
- **The interval:** the **profile likelihood** in n_s (others re-minimised at each n_s), with the Δχ² = 1 crossing giving the 68 % interval. A Fisher σ at the best fit is the cross-check: the two must agree to 25 % or the profile is the one reported and the disagreement is stated.
- **Control:** the same pipeline with ℓ_max = 2508 (full plik_lite TTTEEE + lensing + τ prior) must return n_s within 1σ of Planck's published TTTEEE+lowE+lensing **0.9649 ± 0.0042**. If it does not, the pipeline is wrong and nothing downstream is reported as a result.

## Decision rule, fixed now
Let I be the 68 % interval width (≈ 2σ) of the off-tail n_s.
1. **I ≥ S → TERMINATES** by the row's own clause: the sky cannot decide, and that is a result the papers carry.
2. **Otherwise, weigh:** z(W) = Δ(W)/σ_off for each window. **NO TENSION** if |z| < 2 on every window, and **TENSION** if |z| ≥ 2 on every window.
3. **WINDOW-DEPENDENT** otherwise, stated per window. The tension then exists only for the windows that fail, which is itself the row's structural point.

## Predictions
| arm | quantity | central | band |
|---|---|---|---|
| **T-0** | control, ℓ_max 2508: n_s | 0.965 | within 1σ of 0.9649 ± 0.0042 |
| **T-1** | **σ(n_s), off-tail primary (ℓ ≤ 800, TTTEEE + lensing + τ)** | **0.0075** | **0.005–0.011** |
| **T-2** | central n_s, off-tail primary | 0.966 | 0.955–0.978 |
| **T-3** | spread S of Δ(W) at r = 0.9918 | 0.037 | 0.015–0.06 |
| **T-4** | I vs S | **I < S** (75 %) | — |
| **T-5** | **verdict** | **WINDOW-DEPENDENT** (55 %): no tension on the wide windows (100–1760, 100–2508), |z| ≥ 2 on the high-ℓ windows. NO TENSION 25 %, TERMINATES 15 %, TENSION 5 % | — |
| **T-6** | the 100–1760 window's z | 0.9 | 0.4–1.8 |
| **T-7** | σ(n_s) at ℓ_max 650 / 1000 | 0.010 / 0.0060 | 0.007–0.015 / 0.004–0.009 |

**EFFORT:** 4 h (2.5–7). The profile likelihood dominates: CAMB at ℓ ≤ 2508 with lensing, about 1 s a call.

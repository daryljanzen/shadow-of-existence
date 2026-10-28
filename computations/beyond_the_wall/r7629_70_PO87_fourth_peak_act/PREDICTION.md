# r7629+70 — PREDICTION: PO-87's fourth peak with ACT DR6 in hand

Registered before any measurement. Order: `FOR_70.md` r7629.

## What is measured
1. **The sky's fourth peak, located by PO-47's procedure, unchanged.** The procedure:
   - a cubic spline through the binned TT D_ℓ;
   - a parabola over ±W anchored on the unperturbed peak, at W = 55 (reference) and 80;
   - a Monte Carlo of the bandpower covariance for the statistical spread, plus the procedure spread over the window sweep.

   It is run on:
   - (a) Planck plik_lite, reproducing 1121.9 ± 2.19 (statistical);
   - (b) ACT DR6 CMB-only TT, at its window-weighted ℓ_eff;
   - (c) the two combined: inverse-variance mean, independent (a bound, as both see the shared sky), with the P-ACT reading beside it. P-ACT uses ACT alone above ℓ 1000, and the fourth peak is at ℓ ≈ 1120.
2. **Scoring.** The CR arm and the ΛCDM control (`r6941_fine_{cr,lcdm}`) are scored against each located sky peak.
   - Each model's peak is taken twice: as PO-47 took it, and through the same locator on the model binned exactly as the sky is. The second removes binning bias from the comparison.
   - The quantity is arm − control in units of the sky's spread. The bar is 2σ.
3. **Sharing.** The shared fraction is f = (control − sky)/(arm − sky), with its Monte Carlo error. Also: the cosmic-variance floor on the fourth peak's location for a full-sky, noise-free TT measurement, from the same locator with a covariance of pure sample variance.

## Predictions
| arm | quantity | prediction | band | p |
|---|---|---|---|---|
| **K-1** | ACT alone, fourth-peak σ (statistical) | ≈ 3.6, worse than Planck's 2.19. My r7625 part 1 measured ACT's per-multipole TT precision at ℓ ≈ 1100 at 0.6× Planck's (smaller sky) | 2.5–5.0 | 0.65 |
| **K-2** | combined, independent bound | ≈ 1.9 | 1.6–2.2 | 0.6 |
| **K-3** | arm − control in sky σ: ACT alone / combined | ≈ 0.55 / ≈ 1.0 | 0.3–0.9 / 0.7–1.4 | 0.6 |
| **K-4** | **reachable negative:** ACT separates the arms at 2σ with the CR arm off | **does not happen** | — | 0.9 |
| **K-5** | **terminating outcome:** the offset common to both arms within its error | f consistent with 1 within error, **but not exact.** arm − control = +2.0 is a property of the two model spectra, not of the sky, so no sky measurement can show it to be zero | — | 0.75 |
| **K-6** | the cosmic-variance floor: the smallest σ any TT sky can give the fourth peak (full sky, no noise) | ≈ 1.5–1.7, **above the 1.0 needed** to separate +2.0 at 2σ | 1.2–1.9 | 0.6 |

**What K-6 would mean if it holds.** The discharge exit, data that discriminate the models at the fourth peak, is closed to TT data by cosmic variance, not by any instrument. Then:
- PO-87's data-gated half can only be discharged in polarization: the EE/TE peaks, where ACT is stronger. That is named, not run.
- Or the clause should be reframed. That is 69's call.

**Reachable negatives:**
- K-4: ACT separates the arms.
- K-6: the floor falls below 1.0. TT could then decide in principle, and the precision missing becomes a number.

**EFFORT:** about 1.5 h. Locators and Monte Carlo only; no Boltzmann runs.

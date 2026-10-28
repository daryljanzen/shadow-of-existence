# r7631+70 — PREDICTION: PO-87's fourth acoustic feature in polarisation

Registered before any arm-against-control or sky measurement. Order: `FOR_70.md` r7631.

## What is built and run
1. **The instrument extension (`POLSAVE`).** The r6941 instrument (`ACOUSTIC_two_arm.py`, HIER path) already carries the polarisation source Π in its temperature source, but it projects only TT. A switch, off by default, projects that source through the E-mode kernel:
   - Δ_E,ℓ(k) = √((ℓ+2)!/(ℓ−2)!) · (3/4) ∫ g Π j_ℓ(kx)/(kx)² dη;
   - C_EE = Σ P Δ_E²;
   - C_TE = Σ P Δ_T Δ_E.

   **Validation, gating the rest:** the control (ΛCDM, r6941's parameters) is run with it, and its EE and TE peak positions are compared with CAMB's at the same parameters.
   - Pass: within 2 multipoles at the first four EE peaks.
   - If it fails, the order stops at the instrument and that is the result.
2. **Fine EE/TE spectra for both arms** at r6941's configuration (LSTEP=1, LMAXL=2000, the same switches).
3. **"The fourth acoustic feature"** is defined as EE's fourth peak, near ℓ ≈ 990. In TE, the feature nearest it (an extremum near ℓ ≈ 1000–1150) is located the same way.
4. **PO-47's locator** (spline plus anchored parabola, W = 55 and 80), adapted only in its anchor search range:
   - on the fine model spectra;
   - on Planck plik_lite EE/TE and ACT DR6 EE/TE, with each covariance propagated by Monte Carlo;
   - plus the full-sky, noise-free floor for EE and TE.

## Predictions
| arm | quantity | prediction | band | p |
|---|---|---|---|---|
| **P-1** | the instrument's control EE peaks against CAMB | within 2 multipoles | — | 0.6 |
| **P-2** | arm − control at EE's fourth peak | similar to TT's +1.31: a common acoustic phase shift moves all peaks alike | +0.5 to +2.5 | 0.55 |
| **P-3** | ACT DR6 EE: σ of the fourth peak | 3–8. ACT's EE near ℓ 1000 has S/N of order 10 per bin, and the peaks are sharper than TT's | 3–8 | 0.5 |
| **P-4** | Planck plik_lite EE: σ of the fourth peak | larger than ACT's; Planck EE is noise-dominated near ℓ 1000 | > ACT's | 0.75 |
| **P-5** | **reachable negative:** ACT separates the arms at 2σ in EE or TE with the CR arm off | **does not happen** | — | 0.85 |
| **P-6** | the EE full-sky, noise-free floor on the fourth peak's location | **below** half the arm − control difference: EE peaks are sharper and their sample variance relative to the peak's curvature is smaller than TT's | ≈ 0.3–0.6 | 0.55 |
| **P-7** | **terminating outcome:** the polarisation floor is above half the difference | **does not happen** (follows P-6) | — | 0.55 |
| **P-8** | verdict | **neither exit fires on present data; discharge is possible in principle.** The precision missing is named as current σ divided by half the difference | — | 0.5 |

**Reachable negatives:**
- P-1 fails: the instrument's EE is not trustworthy, and the order stops there.
- P-5: ACT already separates the arms.
- P-7: the polarisation floor also closes the clause, which then terminates as a stated limit.

**EFFORT:**
- about 1 h for the extension and its validation;
- 2–3 h for the fine runs (sliced, resumable);
- about 1 h for locating and scoring.

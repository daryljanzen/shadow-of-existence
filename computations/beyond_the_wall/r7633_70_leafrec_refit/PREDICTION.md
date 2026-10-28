# r7633+70 — PREDICTION: the CR arm refitted at the ruled configuration (LEAFREC=1), its fourth feature, and the census

Registered before any refit run. Order: `FOR_70.md` r7633.

## Procedure
1. **The refit is r6941's own procedure** (`refit_grid185/`), with nothing changed except `LEAFREC=1`, the instrument's default:
   - a 9-run grid for the CR arm: a base at r6941's best point, plus two-sided steps H0 ± 2.0, Ωm ± 0.015, ω_b ± 0.0008 and n_s ± 0.020;
   - all at HIER=1, LSTEP=8, LMAXL=2000, ZSTART=3e7, LEAFSCALES=1;
   - a quadratic response model on plik_lite TT, 185 bins, lensed;
   - a verification run at the minimum, with `POLSAVE` on.

   The control is untouched, since it has no leaf.
2. **The lensing ratio.** The original `/tmp/n66/lens_ratio.npy` is gone. It is regenerated with CAMB at Planck's control parameters, the operator P15 names. The check: `refit_grid185/fit.py`, run with it on the banked LEAFREC=0 grid, must recover r6941's best point (H0 68.5811, Ωm 0.297209, ω_b 0.021524, n_s 0.997952) to within a tenth of a step.
3. **Scoring:** TT, EE and TE on Planck, ACT and the combined bound, as r7631; plus a joint score over the three spectra (an inverse-variance mean of the three standardised differences), with the two skies' disagreement carried. Then a fine-grid check of the polarisation locator.
4. **The census:** every P15 figure resting on LEAFREC=0 spectra, recomputed on the refitted arm.

## Predictions
| arm | quantity | prediction | band | p |
|---|---|---|---|---|
| **R-1** | the lensing ratio reproduces r6941's best point | within 0.1 step on every parameter | — | 0.7 |
| **R-2** | the refit moves the arm's parameters | n_s and ω_b move most; H0 and Ωm less than one step | — | 0.5 |
| **R-3** | refitted arm − control at TT's fourth peak | the refit restores part of the −5 the switch moved: about −1.5 | −3.5 to +1.0 | 0.5 |
| **R-4** | refitted arm − control in TE (ACT's strongest) | about −2 | −4 to 0 | 0.5 |
| **R-5** | **reachable negative:** separated from the control at 2σ at the fourth feature, with CR off on both skies | does not happen; the skies disagree in TE and EE, so "both skies" is a high bar | — | 0.75 |
| **R-6** | **terminating outcome:** the arm − control difference below what the combined skies resolve in every spectrum | does not happen; TE's combined σ of 1.24 would need a difference under 2.5 | — | 0.6 |
| **R-7** | the census | at least 8 P15 figures rest on LEAFREC=0 spectra and move | ≥ 8 | 0.7 |

**EFFORT:**
- 9 grid runs plus 1 verification, about 25 min each at 4 threads, 2 in parallel: about 3 h;
- scoring and census, about 1.5 h.

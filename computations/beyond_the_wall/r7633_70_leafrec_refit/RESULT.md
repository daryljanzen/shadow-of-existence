# r7633+70 — RESULT: the CR arm refitted at the ruled configuration, its fourth feature, and the census (registration `21f3e35`)

## ① The refit: r6941's procedure, unchanged, at `LEAFREC=1`
- **The grid** is 9 runs in `grid/`, made by `launch.sh`. **The response-model refit** is `refit.py`, which is `refit_grid185/fit.py`'s method; output in `refit_leafrec1.txt`.
- **The lensing ratio** was regenerated with CAMB (`lens_ratio.py`). On the banked `LEAFREC=0` grid it reproduces r6941's best point to all six printed decimals (R-1).
- **Verified with a real run:** `verify_cr_leafrec1*.npz`, with POLSAVE on. χ² is **297.7** against the model's 298.2 (`verify_chi2.txt`).

| | H0 | Ωm | ω_b | n_s | χ², 185 bins |
|---|---|---|---|---|---|
| r6941 (`LEAFREC=0`) | 68.5811 | 0.297209 | 0.021524 | 0.997952 | 292.4 |
| `LEAFREC=1` at r6941's point (unrefitted) | 〃 | 〃 | 〃 | 〃 | 452.9 |
| **`LEAFREC=1`, refitted (the arm of record)** | **68.5707** | **0.291246** | **0.021643** | **1.015066** | **297.7** |
| control | 67.4103 | 0.309826 | 0.021966 | 0.954248 | 186.5 |

**The refit recovers almost all of the χ² the switch cost** (452.9 → 297.7, against 292.4 off the leaf rate), mainly through n_s (+0.017) and Ωm (−0.006).

## ② The fourth acoustic feature on the refitted arm (`score_refit.txt`)
| | TT | EE | TE |
|---|---|---|---|
| arm − control | **+0.69** | **+0.92** | **−0.21** |
| in σ: Planck / ACT / combined bound (W=55) | 0.29 / 0.23 / 0.37 | 0.13 / 0.53 / 0.55 | 0.09 / 0.14 / 0.17 |
| at W = 80, ACT | 0.33 | 0.85 | 0.19 |
| full-sky noise-free floor (W=55 / W=80) | 1.27 / 0.80 | 0.55 / 0.34 | 0.48 / 0.30 |

- **The refit removes the unrefitted arm's separation.** The −3.5 / −2.7 / −4.0 r7631 found came from the switch acting at fixed parameters, not from the arm.
- **The joint score over TT, EE and TE:** the arms are 0.09σ apart on the combined skies at W = 55, and 0.28σ at W = 80.
- **The two skies still disagree with each other** (r7633's carried point, landed in P15): Planck and ACT put the EE feature 10.6 apart and the TE feature 5.5 apart. That disagreement is **far larger than the arm − control difference**, which is the order of a multipole.
- **Neither model is preferred by the joint score** (chi2-to-sky, arm − control +0.8 to +6.3 across skies and windows, with the control slightly closer). Correlations between the spectra are not modelled.
- **Grid check (`grid_check.txt`).** The LSTEP=8 grid plus spline locates the TT, EE and TE fourth features to within 0.016 of a multipole against every-multipole spectra, so no fine run is needed for the locator.

## Which exit fires
- **Termination fires**, by the outcome registered for this order: **the arm − control difference sits below what the combined skies resolve in every spectrum.**
  - TT 0.69 against a combined σ of 1.87; EE 0.92 against 1.67; TE 0.21 against 1.24.
- **It also holds against the noise-free floors in TT and TE at both windows, and in EE at W = 55.**
  - EE at W = 80 is the one exception: its floor, 0.34, is below half the difference, 0.46. A perfect, full-sky EE measurement located with the narrow window could reach 2.7σ, but no present or announced instrument is near that.
- **So PO-87's fourth-feature clause terminates on the arm of record.** The arm's fourth feature is the control's, to within under a multipole, in all three spectra. The offset both share from the sky is the models' common one, not the construction's.

## ③ The census (`CENSUS.md`)
- **All 90 banked CR spectra are `LEAFREC=0`.** Every one predates r7095.
- **51 P15 receipts read them, at 85 citations.**
- **Recomputed here on the refitted arm (section A of `CENSUS.md`):** the peak family, the refit point and χ², and the fourth-feature scores. Among them, sec:acoustic's **+1.61, −0.19, +1.07, +1.31 become +1.69, −0.45, +0.70, +0.52**, and **"four fifths" becomes 0.91** (nine tenths).
- **The rest (section B)** each need their receipt re-run against the refitted arm in the form that receipt reads. They are listed with the banked files each reads.

## Scorecard
| arm | predicted | measured | verdict |
|---|---|---|---|
| R-1 lens ratio reproduces r6941's point | within 0.1 step | exact to 1e-6 | HOLDS |
| R-2 n_s and ω_b move most; H0 and Ωm under one step | | n_s +0.86 steps, Ωm −0.40, ω_b +0.15, H0 −0.01 | half: n_s most and all under a step, but Ωm and not ω_b is second |
| R-3 TT arm − control | −3.5 to +1.0 | +0.69 | HOLDS |
| R-4 TE arm − control | −4 to 0 | −0.21 | HOLDS |
| R-5 reachable negative: separated at 2σ, CR off on both skies | does not happen | 0.17–0.55σ | HOLDS |
| **R-6 terminating outcome** | does not happen (p 0.6) | **fires: below the combined resolution in every spectrum** | **FAILS** |
| R-7 at least 8 figures in the census | ≥ 8 | 51 receipts, 85 citations | HOLDS |
| EFFORT | about 4.5 h | about 4 h, including one worker restart | holds |

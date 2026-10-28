# r7629+70 — RESULT: PO-87's fourth peak with ACT DR6 (registration in the r7629+70.1 commit)

**Run:** `python3 measure.py ACT_SACC`, with output in `measure.txt`.
- PO-47's locator, unchanged: spline, parabola anchored on the peak, W = 55 as reference and 80 as the tighter admissible window, and a Monte Carlo of 600 draws from the covariance.
- **Model spectra:** `r6941_fine_{cr,lcdm}`, the ones P15 now quotes. Arm minus control is **+1.31** at the fourth peak, the figure in P15 sec:acoustic.
- PO-47's hard-coded 1126.5/1124.5 came from an earlier configuration; its +1.95 is superseded by +1.31.

## The sky's fourth peak
| sky | ℓ₄ | σ stat (W=55) | σ stat (W=80) | procedure | combined |
|---|---|---|---|---|---|
| Planck plik_lite | 1122.6 | 2.16 | 1.25 | 0.90 | 2.34 |
| ACT DR6 CMB-only | 1122.0 | 2.97 | 1.97 | 0.60 | 3.03 |
| Planck+ACT, independent (a bound) | 1122.3 | | | | 1.85 |

**ACT is less precise than Planck at the fourth peak: 0.77×.** At ℓ ≈ 1120 sample variance dominates and ACT's sky is smaller. ACT overtakes Planck only from ℓ ≈ 1580 (r7625 part 1). The order's premise, that ACT measures the fourth-peak region more precisely than Planck, does not hold at this peak.

## The arms against the sky (fine-grid peaks; binned-through-the-same-locator rows in `measure.txt` agree within 0.2)
| sky | σ | arm − control | in σ | control − sky | arm − sky | shared fraction f |
|---|---|---|---|---|---|---|
| Planck | 2.34 | +1.31 | 0.56 | +6.67 | +7.98 | 0.84 (0.78–0.87) |
| ACT alone (P-ACT) | 3.03 | +1.31 | 0.43 | +7.25 | +8.56 | 0.85 (0.77–0.89) |
| Planck+ACT (bound) | 1.85 | +1.31 | 0.71 | +6.89 | +8.19 | — |

## The cosmic-variance floor: full sky, no noise, the control's spectrum in plik_lite's bins
| | σ(ℓ₄) at W = 55 | at W = 80 | arm − control in σ, best case |
|---|---|---|---|
| full sky | 1.27 | 0.75 | 1.03 / 1.74 |
| Planck's sky (f = 0.55) | 1.73 | 1.02 | 0.76 / 1.29 |

Separating +1.31 at 2σ needs σ(ℓ₄) ≤ 0.65. **No TT measurement reaches that at any precision**, even before the locator's procedure spread is added. Planck's present 1.25 at W = 80 is already within a quarter of its own sky's floor of 1.02.

## Scorecard
| arm | predicted | measured | verdict |
|---|---|---|---|
| K-1 ACT σ | 2.5–5.0 | 3.03 | HOLDS |
| K-2 combined bound | 1.6–2.2 | 1.85 | HOLDS |
| K-3 arm − control in σ, ACT / combined | 0.3–0.9 / 0.7–1.4 | 0.43 / 0.71 | HOLDS |
| K-4 ACT separates the arms, CR off | does not happen | does not | HOLDS |
| K-5 offset shared, consistent with 1 but not exact | f ≈ 1 within error | **f = 0.84 (0.78–0.87): sharing is not consistent with 1** | **FAILS on "consistent with 1"**; "not exact" holds |
| K-6 CV floor 1.2–1.9, above 1.0 | | 1.27 at W=55; **0.75 at W=80** | HOLDS at the reference window; below the band at W=80 but still above the 0.65 needed |

## Which exit fires
- **Neither, and neither can by TT data.**
- **Discharge** (data that discriminate the models at the fourth peak) **is closed to TT by cosmic variance.**
  - A full-sky, noise-free TT sky puts the arms at most 1.0σ apart at W = 55, and 1.7σ at W = 80.
  - ACT DR6 does not help here. It is 0.77× Planck at this peak, and Planck+ACT reaches 0.71σ.
- **Termination** (the offset shown to be the control's own) **does not fire.**
  - The sharing is measured at **84 per cent (78–87)**. Exactly 1 is excluded.
  - The arm's own +1.31 is a property of the two model spectra, located to 0.03 multipole (the locator receipt), so no sky measurement can make the sharing exact.
- **What remains open is the fourth peak's displacement in polarization:** the fourth EE/TE acoustic feature, where cosmic variance is a different, smaller floor relative to the signal and where ACT is strong.
  - This is named, not run.
  - Its precision missing is not yet measured. Measuring it is the natural next step if 69 wants this half pursued.
  - Otherwise the clause needs reframing: its data-gated exit is unreachable in TT. That is 69's call.

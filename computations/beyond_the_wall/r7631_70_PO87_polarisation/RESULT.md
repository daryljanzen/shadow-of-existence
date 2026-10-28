# r7631+70 — RESULT: PO-87's fourth acoustic feature in polarisation (registration `3a049d4`)

**Run:**
- The `POLSAVE` switch was added to `ACOUSTIC_two_arm.py`. It is off by default; with it off, TT is byte-identical to the banked spectra, and the control reproduces `cc66_r185_verify_lcdm` exactly.
- The three spectra here are described in `RUN.md`.
- `python3 validate.py pol_lcdm.npz` gives `validate.txt`.
- `python3 measure.py <cr> pol_lcdm.npz ACT_SACC` gives `measure_r6941config.txt` and `measure_leafrec1.txt`.

**Validation (P-1, HOLDS).** The control's EE peaks match CAMB's at the same parameters to −1.6 at the fourth peak, and TE's to −1.7. TT shows the same −1.6, so this is the instrument's common offset at the fourth feature, and it cancels in arm minus control.

## ⚠ First: the corpus's fourth-peak figures are on a superseded configuration
- `r6941_fine` (PO-47's, the locator receipt's, my r7629's, and P15's +1.31 and 84 per cent) was banked at **`LEAFREC=0`**.
- Since **r7095** the instrument's default is **`LEAFREC=1`**: recombination solved on the leaf rate, by 60's ruling.
- The instrument's own comment says "every banked spectrum taken before it was taken at `LEAFREC=0`".
- The CR arm's fourth feature moves by about 5 multipoles between the two; the control has no leaf and does not move.
- The order named r6941's configuration, so that is run as registered. **The ruled configuration is run beside it, because the answer differs.**

## The arms' fourth acoustic feature
| | TT | EE (4th peak) | TE (trough near 1070) |
|---|---|---|---|
| control | 1128.09 | 991.32 | 1073.03 |
| CR, r6941 config (`LEAFREC=0`) | 1129.58 (**+1.49**) | 992.89 (**+1.57**) | 1073.56 (**+0.52**) |
| CR, ruled config (`LEAFREC=1`) | 1124.56 (**−3.53**) | 988.60 (**−2.71**) | 1069.04 (**−3.99**) |

## The sky's feature (PO-47's locator, covariance by Monte Carlo); σ at W = 55 / W = 80
| spectrum | Planck plik_lite | ACT DR6 | Planck+ACT bound (W=55) | full-sky noise-free floor |
|---|---|---|---|---|
| TT | 1122.5 ± 2.35 / 1.60 | 1122.0 ± 3.06 / 2.08 | 1.87 | 1.27 / 0.80 |
| EE | 1001.2 ± 6.84 / 4.72 | 990.6 ± **1.72 / 1.07** | 1.67 | 0.55 / 0.34 |
| TE | 1068.7 ± 2.43 / 1.86 | 1074.2 ± **1.44 / 1.07** | 1.24 | 0.48 / 0.30 |

**ACT DR6 is the strongest instrument in polarisation at this feature,** 4× Planck in EE. In TT it is the weakest (r7629).

## Arm against control in the sky's σ (2σ needed), W = 55 / W = 80
| configuration | TT, Planck | EE, ACT | **TE, ACT** | where the arm sits in TE (ACT) |
|---|---|---|---|---|
| r6941 (`LEAFREC=0`) | 0.63 / 0.93 | 0.91 / 1.46 | 0.36 / 0.49 | arm −0.64, control −1.16 |
| **ruled (`LEAFREC=1`)** | 1.50 / **2.21** | 1.58 / **2.53** | **2.77 / 3.74** | **arm −5.15 (3.6σ), control −1.16 (0.8σ)** |

## Scorecard (registered for r6941's configuration)
| arm | predicted | measured (r6941 config) | verdict |
|---|---|---|---|
| P-1 instrument EE vs CAMB within 2 | — | −1.6 at peak 4 | HOLDS |
| P-2 EE arm − control | +0.5 to +2.5 | +1.57 | HOLDS |
| P-3 ACT EE σ | 3–8 | **1.72** | **FAILS**: ACT is twice as good as predicted |
| P-4 Planck EE worse than ACT | yes | 6.84 vs 1.72 | HOLDS |
| P-5 reachable negative: ACT separates, CR off | does not happen | 0.91σ (EE), 0.36σ (TE) | HOLDS. **On the ruled configuration it happens: TE 2.8σ / 3.7σ, CR off** |
| P-6 EE floor below half the difference | 0.3–0.6 | 0.55 / 0.34 against 0.79 | HOLDS |
| P-7 termination fires | does not | does not (EE floor below half) | HOLDS |
| P-8 neither exit fires; precision missing named | yes | yes | HOLDS. **On the ruled configuration discharge fires** |

## Which exit fires
- **On r6941's configuration, as ordered: neither.**
  - Termination does not fire: the EE floor, 0.55 / 0.34, sits below half the arm − control difference, 0.79. Polarisation can resolve it in principle, to 2.8σ / 4.6σ at best.
  - Discharge does not fire on present data: ACT EE gives 0.91σ / 1.46σ.
  - **Precision missing: ACT DR6's EE σ must shrink 2.2× (W = 55) or 1.36× (W = 80).**
  - TE cannot help on this configuration: its difference, +0.52, is below twice its floor.
- **On the ruled configuration (`LEAFREC=1`): discharge fires, and against the CR arm.**
  - ACT DR6 TE separates the arms at 2.77σ (W = 55) and 3.74σ (W = 80).
  - The arm sits 5.15 from the sky's TE trough (3.6σ); the control sits 1.16 away (0.8σ).
  - ACT EE agrees in direction (1.6σ / 2.5σ, arm off by 2.0).
  - **TT on this configuration points the other way**: the arm is closer to the sky (+2.0 against the control's +5.6), and TT alone is 1.5σ / 2.2σ. So temperature and polarisation disagree about which model is off.
  - **My r7629 statement that "no temperature spectrum can resolve the difference" holds only on `LEAFREC=0`.** On the ruled configuration the TT difference is −3.53, the floor (1.27 / 0.80) is below half of it, and Planck at W = 80 already reaches 2.2σ.

## For 69
- **Which configuration is the CR arm of record for PO-87 is your ruling**, and the answer turns on it.
  - On r6941's, the order's: neither exit fires, and EE needs 1.4–2.2× ACT's precision.
  - On the instrument's ruled default since r7095: polarisation discriminates now, against the arm, while temperature prefers the arm.
- **Census flag (r7577 rule):**
  - P15 sec:refit-bound's fourth-peak figures (+1.31, 84 per cent, "no temperature spectrum can resolve the difference"), PO-87's row, P7 and P18 rest on `LEAFREC=0` spectra.
  - If `LEAFREC=1` is the arm, they move: TT −3.53, temperature able to resolve it, and polarisation already discriminating.
- **Not done:**
  - A fine-grid (LSTEP=1) check of the polarisation locator. Coarse plus spline is what the TT locator receipt validated to 0.03.
  - A joint TT+TE+EE score.
  - Any re-fit of the arm's parameters at `LEAFREC=1`.

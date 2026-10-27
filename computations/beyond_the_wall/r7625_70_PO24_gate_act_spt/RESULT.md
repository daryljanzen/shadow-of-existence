# Chat-seat order — RESULT, part 1 of 2: the precision comparison (registration `9baf92f`)

**Run:**
- `python3 measure.py ACT_SACC SPT_LITE_DIR`, with output in `measure.txt`;
- `python3 fsky_scan.py ACT_SACC SPT_LITE_DIR`, with output in `fsky_scan.txt`.

**Data:**
- ACT DR6 CMB-only, the foreground-marginalised SACC file `dr6_data_cmbonly.fits` v1.0 from LAMBDA, the file `act_dr6_cmbonly` installs;
- SPT-3G D1 SPT-lite, from `SouthPoleTelescope/spt_candl_data` at `f22611a`;
- Planck 2018 plik_lite TT.

The data files are not committed; they are fetched from those sources.

## Scorecard
| arm | quantity | predicted | measured | verdict |
|---|---|---|---|---|
| H-1 | ACT alone, band ratio | ≈ 0.9 (0.6–1.2) | amp 0.87, full cov 0.79; **tilt 1.22** | HOLDS on amplitude; the tilt is above the band |
| H-2 | SPT alone | ≈ 0.4 (0.2–0.7) | amp 0.36, full cov 0.37, tilt 0.51 | HOLDS |
| H-3 | Planck+ACT, independent | ≈ 1.35 (1.15–1.55) | amp 1.32; **tilt 1.67** | HOLDS on amplitude; the tilt is above the band |
| H-4 | Planck+ACT, overlap-corrected | ≈ 1.2 (1.05–1.40) | amp 1.20–1.22; **tilt 1.58–1.63** for any f_ACT from its floor 0.17 to 0.50 | HOLDS on amplitude; **FAILS on tilt** |
| H-5 | Planck+SPT, overlap-corrected | ≈ 1.05 (1.00–1.20) | amp 1.03, tilt 1.09 | HOLDS |
| **H-6** | does any configuration clear 1.44? | no (p 0.65) | **Planck+ACT clears it on the tilt (1.58–1.63)**; no configuration clears on amplitude | **FAILS: the reachable negative** |
| H-7 | where ACT overtakes Planck per multipole | ℓ ≈ 1800–2200 | **ℓ ≈ 1580** (SPT at ≈ 2060) | earlier than predicted |

## What it says
- **Per multipole,** ACT is 0.6–0.75× Planck's precision below ℓ ≈ 1500, where Planck's larger sky wins. It overtakes Planck at ℓ ≈ 1580 and reaches 6× by ℓ ≈ 2460, where Planck is noise-dominated.
- **That is why the measure matters.** The amplitude measure is dominated by the many low-ℓ bins, and on it ACT is below Planck. The tilt measure depends on the lever arm at high ℓ, and there ACT is decisive.
- **The bar is a bar on σ(n_s),** so the tilt is the figure that answers the order. On TT with amplitude and tilt free, Planck+ACT measures the tail tilt 1.58–1.63× as precisely as Planck alone after correcting for the shared sky, and 1.67× if combined as independent.
  - Implied σ(n_s) on 1000–2508: about 0.0158/1.6 ≈ 0.010.
  - Against the faithful shift +0.0218, that is a separation of about 2.2σ.
- **SPT-3G D1 does not clear it, alone or with Planck.** Its 4 % sky makes it sample-variance-limited across the band.
- **This is a proxy, and it is labelled as one.**
  - TT only, amplitude plus tilt, against a bar that came from a six-parameter TT/TE/EE fit.
  - The overlap correction is a per-multipole model: sample variance on each dataset's effective sky, the excess treated as noise. It is not a joint likelihood.
  - ACT's own recommended P-ACT combination cuts Planck TT at ℓ > 1000 to avoid double-counting that sky. On this window that leaves ACT alone, which is 1.22.

## Next: the order's step 3, the tail fit on the data that cleared
- r7489's six-parameter fitter is run on ℓ 1000–2508 with ACT DR6 CMB-only (TT/TE/EE, its windows and its calibration and polarisation-efficiency parameters) added to Planck.
- It is run in two arms: Planck+ACT summed as independent (the bound), and P-ACT-style (Planck cut where ACT measures, i.e. ACT alone on this window).
- Each arm gets the sky fit and the faithful signature mock. n_s is reported against +0.0218, with the separations.
- **Re-estimated effort:** about 3–4 h, most of it 8–10 fits of about 30 min each.

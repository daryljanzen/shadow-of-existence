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

---

# RESULT, part 2: the tail fit with ACT DR6 (the order's step 3)

**Run:**
- `ACT_SACC=… python3 wfit_act.py MODE 1000 2508 PROF ARM` for the sky fits (with profile), the faithful signature mocks and a null control;
- `python3 tail_act.py` reads them, with output in `tail_act.txt`.

**Model:**
- r7489's fitter: flat ΛCDM, six parameters free plus Planck's calibration, Planck lensing and the τ prior.
- ACT DR6 CMB-only is added as its own likelihood does it: TT/TE/EE through the SACC bandpower windows, with A_act ~ 1 ± 0.003 and P_act free.
- The signature mock multiplies every spectrum, Planck's and ACT's, by the faithful S (ℓ_eff 1497, r = 0.9918).

| on ℓ 1000–2508 | n_s on the sky | σ (profile) | × Planck | signature shift Δ | Δ/σ | sky from no shift | sky from the signature |
|---|---|---|---|---|---|---|---|
| Planck alone (r7489; r7611 mock) | 0.9639 | 0.0158 | 1.00 | +0.0218 | 1.38 | 0.19σ | 1.20σ |
| **Planck + ACT, summed** (an upper bound: the shared sky is counted twice) | **0.9701** | **0.0087** | **1.82** | +0.0275 | **3.17** | 1.06σ | **2.11σ** |
| **ACT alone** (P-ACT: Planck cut where ACT measures) | **0.9736** | **0.0094** | **1.67** | +0.0269 | **2.85** | 1.34σ | 1.51σ |

**Controls:**
- The null mock (Planck + ACT, no signature) returns a shift of exactly 0 with χ² of 0.
- Each profile's σ equals its Fisher σ to the quoted digits.
- The profiles are slightly asymmetric: the −1σ point costs Δχ² 0.47–0.77, the +1σ point 1.2–1.5.

## What it says
1. **The data gate stands open.** In both arms the six-parameter TT/TE/EE fit measures the tail tilt more precisely than the 1.44× bar: 1.82× and 1.67×. In both, the two predictions are separated by more than 2σ (3.2σ and 2.9σ). On Planck's tail alone they were 1.4σ apart. Adding TE/EE puts ACT alone at 1.67×, above part 1's TT-only proxy of 1.22.
2. **The answer it gives is not yet a decision.**
   - With ACT alone, the sky's n_s sits between the two predictions, 1.3σ from no shift and 1.5σ from the signature, so it decides nothing.
   - With Planck + ACT summed, the sky is 1.1σ from no shift and 2.1σ from the signature. That is at the 2σ line, and in the arm that counts the shared sky twice. Part 1's overlap correction (about 5 % on σ) brings it to about 2.0σ.
   - **So the data lean against the signature, at the threshold and not past it.**
3. **There is a confound the order should know about.** The no-shift baseline is Planck's off-tail n_s (0.9610). ACT DR6 is known to prefer a higher n_s than Planck across its range (P-ACT ≈ 0.974). Part of the sky's +0.009 to +0.013 offset from the baseline is therefore that known ACT–Planck difference, and not anything in the tail. It pushes the sky toward the signature, so it makes the lean against the signature conservative, not inflated. A fully clean test needs the off-tail baseline from the same combination (P-ACT on ℓ ≤ 800). That is one more fit, and it is not run here.

## Scorecard, final
- **H-6 failed:** a configuration clears, and it does so in the full fit as well as in the TT proxy.
- **The order's step 3 is run.** n_s against the faithful +0.0218 (Planck) and +0.027 (with ACT), with separations, is in the table above.
- **Not run:** the 700–1760 window with ACT (it costs about 1 h of fits). It is not needed for the verdict, since 1000–2508 is the decisive window.
- **EFFORT:** about 5 h against the 2 + 4 registered. A container restart cost one batch of fits.

## For 69 (census, r7577 rule)
- Every paper sentence that calls PO-24's live half "data-gated" on tail data 1.25× (now 1.44×) as precise as Planck's is no longer true as written.
- **The gate is open on public data (ACT DR6).**
  - The test it allows lands at 1.1σ / 2.1σ (Planck + ACT summed) and 1.3σ / 1.5σ (ACT alone), against no shift and against the signature respectively.
  - It leans against the signature at the 2σ line, short of a decision.
  - The cleaner baseline in point 3 is the next measurement if a decision is wanted.

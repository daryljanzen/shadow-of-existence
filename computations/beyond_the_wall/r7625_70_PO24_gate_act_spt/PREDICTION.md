# Chat-seat order (on Daryl's direction, `48889c6`) — PREDICTION: does PO-24's data gate already stand open on ACT DR6 or SPT-3G D1?

Registered before any data is downloaded. The directory is named `r7625` for the next free order slot, because the chat seat's order carries no r-number.

## The bar, as r7611 leaves it
- **Deciding PO-24 on ℓ 1000–2508 needs tail data 1.44× as precise as Planck's.** r7611+70.2 measured this on the faithful exponent; it was 1.25× before.
- In n_s terms: σ(n_s) on that window must fall from 0.0158 to **≤ 0.0110** (half the faithful signature shift, +0.0218/2).

## What is measured
1. **Data:**
   - ACT DR6's foreground-marginalised CMB-only TT bandpowers and covariance (the `act_dr6_cmbonly` SACC file on LAMBDA);
   - SPT-3G D1's TT bandpowers and covariance (`spt_candl_data`, the D1 T&E set);
   - Planck's plik_lite TT, the r7471/r7489 baseline.
2. **Per-bin ratio.** Bin widths differ, so precision is compared per multipole: R(ℓ) = σ_P/σ_X, with each σ rescaled to unit Δℓ by √Δℓ. It is reported per Planck bin on ℓ 1000–2508.
3. **Band-averaged ratio.** √(F_X/F_P), where F = Σ 1/σ² over ℓ 1000–2508 from the diagonal of each covariance. The full-covariance Fisher on a D_ℓ amplitude is printed beside it as a check.
4. **Combinations.**
   - Planck+ACT and Planck+SPT are first combined as independent, F_P + F_X. That is an upper bound on the gain, because the skies overlap and sample variance is shared.
   - A shared-sample-variance estimate is printed beside it (only the noise parts add over the overlap).
   - A configuration clears the bar only if its **overlap-corrected** ratio is ≥ 1.44.
5. **If any configuration clears the bar,** run the r7489 tail fit on it and report n_s against the faithful +0.0218, with the windows' separations. This needs a likelihood for that dataset, and the effort is re-estimated before starting.

## Predictions
| arm | quantity | prediction | band | p |
|---|---|---|---|---|
| **H-1** | ACT DR6 alone, band-averaged R on 1000–2508 | ≈ 0.9: below Planck at ℓ < 1800 (smaller sky, plus foreground marginalisation), above it near 2500 | 0.6–1.2 | 0.6 |
| **H-2** | SPT-3G D1 alone, band-averaged R | ≈ 0.4 (about 4 % of sky, so sample variance dominates) | 0.2–0.7 | 0.6 |
| **H-3** | Planck+ACT, independent upper bound | ≈ 1.35 | 1.15–1.55 | 0.55 |
| **H-4** | Planck+ACT, overlap-corrected | ≈ 1.2 | 1.05–1.40 | 0.55 |
| **H-5** | Planck+SPT, overlap-corrected | ≈ 1.05 | 1.00–1.20 | 0.6 |
| **H-6** | verdict: does any configuration clear 1.44 overlap-corrected? | **no**; the gate stands with ACT and SPT measured against it | — | 0.65 |
| **H-7** | per-bin: where ACT overtakes Planck (R > 1) | ℓ ≈ 1800–2200 | — | 0.5 |

**Reachable negatives.**
- H-6 fails if Planck+ACT clears 1.44 after the overlap correction. The tail fit then runs (arm 5), and the gate is open.
- H-1 fails if ACT alone is already above 1.2 across the band, i.e. foreground marginalisation costs less than expected.

**Scope.**
- These are TT only, as the order asks. The 1.44× bar was derived from a TT/TE/EE tail fit, so a TT-only ratio is a proxy for the n_s precision. It is stated as such, and the full-covariance amplitude Fisher bounds it.
- Calibration, beams and foregrounds are as each collaboration marginalised them in its CMB-only product. None is re-modelled here.
- No paper edits; 69 lands the text.

**EFFORT:** about 2 h if no configuration clears (download, read, compare), and about 4 more if the tail fit has to run.

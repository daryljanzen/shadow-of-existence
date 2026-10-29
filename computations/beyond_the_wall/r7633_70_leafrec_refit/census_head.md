# The LEAFREC=0 census (r7633 ③): every P15 citation of a receipt that reads a banked CR spectrum

**Why every banked CR spectrum is affected.** All 90 CR spectra in `computations/beyond_the_wall/spectra/` predate r7095, so all are at `LEAFREC=0`. None carries a config manifest with `LEAFREC`, and the instrument's comment says every spectrum banked before r7095 is `LEAFREC=0`.

**The census.** 51 P15 receipts read one or more of them, at 85 citations in `CR_cosmology.tex`. The figures column holds the inline numbers nearest each citation, extracted mechanically. It is the place to look, not a parse of meaning.

## A. Recomputed here on the refitted ruled arm
The refitted arm is `LEAFREC=1` at H0 68.5707, Ωm 0.291246, ω_b 0.021643, n_s 1.015066; its spectra are in `verify_cr_leafrec1*.npz`. The control is unchanged.

| figure P15 prints (LEAFREC=0) | on the refitted ruled arm | source |
|---|---|---|
| best point H0 68.5811, Ωm 0.297209, ω_b 0.021524, n_s 0.997952 | **68.5707, 0.291246, 0.021643, 1.015066** | `refit_leafrec1.txt` |
| 185-bin χ² of the arm, 292.4 (control 186.5) | **297.7** (control unchanged, 186.5) | `verify_chi2.txt` |
| arm − control at the four peaks: +1.61, −0.19, +1.07, +1.31 (sec:acoustic) | **+1.69, −0.45, +0.70, +0.52** | `census_peaks_refit.txt` |
| control's share of the arm's offset at the fourth peak: "four fifths" (0.80) | **0.91** | same |
| arm − sky at the four peaks: +1.56, −1.60, −1.90, +6.63 | **+1.65, −1.85, −2.27, +5.84** | same |
| comb ℓ_A 296.72, φ/π +0.2324, P₁/P₂ 2.141, P₁/P₃ 2.172 (this locator on r6941_fine) | **296.49, +0.2316, 2.135, 2.166** | same |
| fourth feature, arm − control (PO-47 locator, W=55): TT +1.31 (r7629) / +1.49; EE +1.57; TE +0.52 (r7631) | **TT +0.69, EE +0.92, TE −0.21** | `score_refit.txt` |
| arms apart in σ, TT: Planck 0.56, ACT 0.43, combined 0.71 (r7629) | **0.29, 0.23, 0.37** | same |
| ACT EE 0.91σ / 1.46σ; TE 0.36σ / 0.49σ (r7631, W=55/80) | **EE 0.53σ / 0.85σ; TE 0.14σ / 0.19σ** | same |

## B. Rest on LEAFREC=0 spectra, not recomputed here
Each of these needs its own receipt re-run against the refitted arm, re-banked in whatever form that receipt reads (fine grid, injections, source decompositions or transfers). The banked files each one reads are listed.


# `r7813+70` — the control's first-to-second height ratio at Planck's point: RESULT

*Registered at `r7813+70.1` (`PREDICTION.md`) before any run. Receipt:*
`receipts/P15_CR_cosmology/P15_at_plancks_point_the_control_returns_p1_p2_2_203_against_cambs_2_212_through_one_locator_so_the_agreement_is_0_44_per_cent_and_the_cutoff_moves_nothing.py`.
*Banks: `out/control_planck2018_kfac{2,3}.npz` (`bank.py`). Figures: `out/SUMMARY.json` (`measure.py`).*

## The answer

**At Planck 2018's point** (H₀ 67.36, ω_c 0.1200, ω_b 0.02237, n_s 0.9649), on the polarisation path (`HIER=1`, `LSTEP=8 LMAXL=2000`), the instrument and CAMB were put through P15's own matched locator:

| spectrum | peak 1 | peak 2 | peak 3 | peak 4 | **P1/P2** | P1/P3 |
|---|---|---|---|---|---|---|
| instrument, KFAC 2.0, lensed | 220.60 | 537.65 | 811.72 | 1124.75 | **2.2026** | 2.2288 |
| instrument, KFAC 3.0, lensed | 220.60 | 537.65 | 811.72 | 1124.75 | **2.2026** | 2.2288 |
| CAMB, Σm_ν 0.06, lensed | 220.30 | 537.20 | 811.73 | 1124.65 | **2.2123** | 2.2567 |
| CAMB, massless, lensed | 220.71 | 538.02 | 812.89 | 1126.28 | 2.2116 | 2.2564 |
| instrument, KFAC 2.0, unlensed | 220.79 | 537.96 | 813.15 | 1128.10 | 2.1950 | 2.1935 |
| CAMB, Σm_ν 0.06, unlensed | 220.52 | 537.52 | 813.15 | 1128.03 | 2.2047 | 2.2209 |

- **The agreement on P1/P2 is −0.44 %** (instrument/CAMB − 1 = −0.438 %), both lensed and unlensed. Against massless CAMB, which matches the instrument's neutrinos, it is −0.41 %.
- **The cutoff moves nothing.** KFAC 3.0 against 2.0 moves P1/P2 by −0.00014 % and the peaks by at most 0.0006 multipoles.
- **The printed comparison is not this one.** Unlensed, the instrument's 2.1950 matches P15's control figure `2.195` to three decimals; that figure was taken at the corpus's old point, and the point move costs about a thousandth. CAMB through the same locator, however, gives 2.2047, not `2.200`. So the `2.200`, and the 0.23 % set against it, did not come through one procedure. **Through one procedure the gap is 0.44 %.**

## The predictions, as registered

| | registered | measured | |
|---|---|---|---|
| (1) KFAC 2.0 reproduces `r7807`'s bank | ≤ 1×10⁻¹² | 4.1×10⁻¹⁵; 2.203 through the locator, as `r7809+cc66` | **held** |
| (2) KFAC 3.0 moves P1/P2 | < 0.05 % | −0.00014 % | **held** |
| (3) CAMB's lensed P1/P2 | 2.19–2.21 | 2.2123 | ⛔ **failed** |
| (4) the agreement | within ±0.3 % | −0.44 % | ⛔ **failed** |
| (5) massless against Σm_ν 0.06 in CAMB | < 0.2 % | −0.031 % | **held** |

**Why (3) and (4) failed:** both rested on the printed `2.200` being the standard code's figure through P15's procedure. It is not. Through that procedure CAMB returns 2.212 lensed and 2.205 unlensed.

## Caveats

- **Planck's point, not Planck's model.** The instrument has no neutrino mass. In CAMB that difference is worth 0.03 % on this ratio.
- **The lensed row lenses the instrument with CAMB's own ratio at this point.** Lensing lifts P1/P2 by the same factor (1.00343) on both, so the −0.44 % is the unlensed transfer.
- **One locator.** A different peak procedure gives different heights (`r7809+cc66` (2d)). The procedure here is P15's own, imported from its receipt.

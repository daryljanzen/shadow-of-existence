# r7673+70 — RESULT

**All three items are resolved.**
- **Item 1** needed a build, and it is banked: `spectra/r7041_accept_cr_leafrec1.npz`. This is an **addition**; no namesake was edited. A LEAFREC=0 rebuild through the same chain reproduces all 53 namesake keys exactly.
- **Item 2** was already on the arm of record. Its producer reproduces the banked file bit for bit.
- **Item 3** is **not** the arm of record, and no setting of its engine reaches the arm of record. The cheapest approximation moves the sweep's depths by under 0.01, and it costs 2 runs and about 13 min.

## Item 1 — `r7041_accept_cr` on the arm of record

**My r7041 build did not produce this file (P1 holds).** My four `_leafrec1` files are the GRIDSAVE/A_l bank. This one is the *thinned injection transfer*, a different chain:
- `r7039_directions/launch.sh`'s CR transfer runs: `SRCINJ=fixed` and `SRCINJ=sweep SRCINJRS=own`, `HIER=1 LSTEP=8 LMAXL=2000`, six `KSLICE` pieces with `DLKSAVE`;
- folded by `r7039_directions/bank.py`'s transfer loop;
- thinned by `r7041_directions/bank_thin.py`'s `main()`.

**The build** (`launch.sh` and `fold_thin.py` → `item1.json`):
- Both folding steps are lifted from their source by `ast`. Only the arm tuple (`('cr',)`) and the directories are replaced.
- It was built twice: lr0 at the recorded CR point with LEAFREC=0, and lr1 at the refit licensed point with LEAFREC=1.

**Recipe check:** lr0 reproduces `spectra/r7041_accept_cr.npz` in **all 53 keys exactly** (P2 holds). Only then was lr1 banked, with `config` and `manifest`.

**What the arm of record moves:**
- every CR key except the injection's own settings;
- the law's output `A` by **+0.44%** in mean (0.5947 → 0.5973; P3, under 2%, holds);
- l_A 301.80 → 302.94, D_M 14017.04 → 14133.95 (the arm of record's), r_s* 145.91 → 146.57.

**P15's "14.6 per cent wider χ-extent":** on these banks it is the visibility's width ratio, `eta_ls_w` cr/lcdm − 1. It reads **14.59%** on the namesake, which is P15's number, and **15.55%** on the arm of record.

**The "0.08 per cent" sound horizon is not this bank's r_s*.** The r_s* the law uses differs between the arms by 0.36% on the namesake and 0.82% on the arm of record. The same ratios hold on `r6919_injected_{cr,cr_leafrec1}` against `r6919_injected_lcdm`. The receipt cites `r6919` for the 0.08%, so it is a different sound-horizon measure, which I did not trace. **cc66: worth checking which quantity the 0.08 is, and whether it was ever this ratio.**

**Wall time:** 24 slices, 32–262 s each, **1057 s** in all on 4 cores for both builds (P4, under 40 min, holds). The fold takes under a minute.

## Item 2 — `r7183_nofit_figure/nofit_figure_numbers.npz`

**Already on the arm of record; no build.** Its producer, `corpus/make_fig_acoustic_nofit.py`, reads two CR spectra:
- `refit_grid185_leafrec1_distances/cr_base.npz` (no-fit, D_M 14011.46);
- `spectra/cc66_r185_verify_cr_leafrec1.npz` (refit, D_M 14133.95).

Both are arm-of-record files. It was repointed at `r7645+cc66.67`.
- **Re-run once:** 17 s, rc=0. The `.npz` came back **bit-identical in every key**. Only the figure PDF's bytes changed (its metadata), and that change was reverted, not committed.
- The census flags the file only because its path carries no `_leafrec1`.
- This was measured before PREDICTION.md, and the file says so.

## Item 3 — `cc66_lowell_sweep`

**Is HIER's rate the arm of record's recombination rate? In form yes, in value no. And the construction around it is not the arm of record's.**

| | arm of record (`ACOUSTIC_two_arm.py`, LEAFREC=1) | the sweep's adjudicated arm (HIER, ARM unset) |
|---|---|---|
| recombination rate | `Hleaf` = H0·√(OM/a³+OL+OR/a⁴) | `Hub` = H0·√(Or/a⁴+Om/a³+OL): **same form** |
| ionisation solver, Yp | `RD_diffusion_direct.xe_history`, 0.2454 | the same |
| point | 68.570730 / 0.291246 | **68.60 / 0.2973** |
| ω_b | 0.021643 | **0.02237** (HIER default, `OBF` unset) |
| radiation | OR = 4.15e-5/h² | **4.1833e-5/h²** (0.8% more) |
| conformal-time grid and projection | the **stacking** rate (`Hphys`, radiation-free) | the **same leaf rate**: the one-clock arrangement (LEAFGEOM=1's) |

So the sweep is not the arm of record's. HIER has two clock settings:
- **ARM unset:** everything on the leaf rate;
- **`ARM=cr`:** everything on the stacking rate, which is LEAFREC=0's arrangement.

**Neither is the arm of record's split** (geometry on the stacking rate, recombination on the leaf). The sweep's ratio is a discrete sum over the closed geometry's ladder against the integral of the *same* transfer. The CR geometry enters through R0 only.

**Only 2 of its 8 configurations use the adjudicated background:** `FROZEN_adjudicated_KLO_0_1` and `DECOUPLED_adjudicated_KLO_0_1_NS3_60000`. The other 6 are control, and on the control one rate is correct (r7669 ①).

**Pricing, measured** (`lowell_price.py` → `lowell_price.json`): the two through the receipt's own harness, lifted by `rederive_lowell_sweep.engine()`.

| configuration | recorded background, vs bank | at the refit licensed point (ω_b via `OBF`) | wall |
|---|---|---|---|
| FROZEN adjudicated | reproduces the bank to its 4 dp | depths move by +0.0047, +0.0091, +0.0012, −0.0038, −0.0012, +0.0003, +0.0004 at ℓ = 2–8 | 71 s |
| DECOUPLED adjudicated | reproduces the bank to its 4 dp | +0.0052, +0.0089, +0.0016, −0.0033, −0.0012, −0.0000, +0.0002 | 652 / 718 s |

**The arm-of-record forms, priced:**
- **(a) The point only (measured above):** 2 runs, about **13 min**. It moves the depths by under 0.01, largest at ℓ = 3 (0.430 → 0.439). It is still one-clock, so it is an approximation, and I have not banked it. The receipt's sweep tilt (0.9649) is primordial and was left as recorded.
- **(b) The exact form:** HIER needs a switch that builds the conformal-time grid and projection on the stacking rate while `xe_history` stays on the leaf rate, the split `ACOUSTIC_two_arm.py` has. That is an instrument change in `storyboard_receipts/HIER_photon_hierarchy.py`, with a byte-identical-unset gate. It is about one session's work, plus the same 2 runs, and is **not built here**: it is 69's call.

**Predictions:**
- P5 (same form, different point) **holds**; the ω_b and radiation-normalisation differences were not registered.
- P6 (not the arm of record; no HIER setting reproduces the split) **holds**.
- P7 (the point-only approximation is the cheapest, priced by timing) **holds**: 13 min for the two, against about 9 min each registered from cc66's docstring.

## Pre-push gates

- **Readers run by stem (r7645 rule):** the 2 receipts that name `r7041_accept_cr` both exit 0 (the retention receipt in 97 s, the law's six-of-seven in 46 s).
- `check_banked_config`: passes.
- `run_touched_readers.sh --class1`: GREEN.
- Bank change: **addition**, one file (`spectra/r7041_accept_cr_leafrec1.npz`).

# r7651+70 — PREDICTION (pushed before any solve or run)

## ① The taper bank, at the arm of record's spread

**What runs.** `r6959_directions`' swap recipe (`launch_b.sh`'s `swap_lcdm`, verbatim: the control, `HIER=1
LSTEP=1 LMAXL=2000`, eleven 250-mode KSLICE pieces, `SRCTAPERS0` = the banked `taper_s0`). The only change is
`SRCTAPER = α′`. α′ is solved by `predict.py`'s own bisection on `sig_all` (NF=3), and its target is the arm of record's
band-summed window spread in its own r_s, `sig_all(r6959_eta_cr_leafrec1)/r_s`, which cc66 measured as 0.06447. That
spread is carried onto the control's r_s.

**Bank form: an ADDITION.** It goes in `spectra/r6959_swap_lcdm_leafrec1.npz`, in the namesake's form (bank.py's fold:
`ls, Dl, l_A, D_M, r_s, taper, taper_s0, taper_all=0, taper_norm=0`, plus `config` and `manifest`). The target is
recorded too. The namesake and the other five tapered banks do not move.
- **Reader:** `P15_the_windows_phase_spread_is_nearly_equal_because_the_visibility_widens_as_the_leaf_clock_slows.py`.
  It still reads the namesake, and I run it before the push. The re-point is cc66's.

**Predictions.**
- α′ in **[7.5e-5, 9.5e-5]**. The Gaussian estimate scales the banked 1.10088e-4 by
  (1/0.06447² − 1/0.06523²)/(1/0.06424² − 1/0.06523²) ≈ 0.77. Reachable negative: outside the band.
- The receipt's own gate, as it is written for the swap, reads `|spread(lcdm, α′)/r_s − 0.06447| < 2e-4` and holds.
- The eleven slices tile 0–2547, and every run has rc=0.
- **The banked spectrum differs from the namesake swap's by under 0.5% of the peak.** The coefficient moves by
  about a quarter, and the taper's effect on D_l is percent-level. Reachable negative: over 0.5%.

## ② The three-grid audit with a per-arm resolver

`r7101_70_three_grid_audit/audit.py` runs unchanged, with one exception: its `GRIDS` resolve per arm. The control
comes from the namesake grid, and the arm comes from the `_leafrec1` sibling: banked → `refit_grid185_leafrec1`,
licensed → `grid_licensed_leafrec1`, forbidden → `grid_oneclock_leafrec1`. The resolver is a per-run directory of
links that the script builds itself, so `rigidity.py --grid` sees the same resolution.
- The sibling grids carry no `cr_base.log`, and parts (2) and (3) read it. The r7639 bank's logs are matched by
  bit-identical `cr_base.npz`, and they are banked beside the sibling grids. That is an **addition** (new .log
  files only).

**Predictions (the seven truncation gaps, licensed − forbidden, at ℓ = 850 … 1996).**
- They stay **monotone non-decreasing** from the first truncation to the last, as on the namesake (−1.0 … +93.8).
- The last gap is in **[60, 130]**.
- The first, at ℓ = 850, is within **±5**.
- At every truncation the forbidden configuration sits within **5 units** of the control.
- Reachable negative: the gaps are not monotone, or the last falls below 60. Either would mean P15's "rigidity
  across scales" does not carry to the arm of record.

## ③ camb in `check_env_fingerprint`

- `live()` reads `camb.__version__`, or `ABSENT` when the import fails.
- `stored()` reads a `camb =` line.
- `receipts/ENV_FINGERPRINT.txt` gains `camb = 2.0.4`, with the reason it is not a refresh without a sweep:
  `camb==2.0.4` was pinned at r6981 (`17f7fe1c7`), before the r6985+70.1 sweep, so 2.0.4 is what that sweep ran on.

**Prediction.** The gate is green here, where camb is 2.0.4. It goes **red** in two simulated environments, one
where camb is shadowed by a module whose import fails and one where camb is shadowed by a fake version.
Reachable negative: either simulated environment stays green.

**EFFORT.** ① 11 control slices at LSTEP=1 (~1 h wall on 4 cores). ② a few minutes. ③ minutes.

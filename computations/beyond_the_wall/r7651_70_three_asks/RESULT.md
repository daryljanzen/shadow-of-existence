# r7651+70 — RESULT

All three asks are done. Of the registered predictions, one missed: the taper bank's size of move. It is reported below, and its band is left as registered.

## ① The taper bank, at the arm of record's spread

**The coefficient.** `predict.py`'s own `sig_all` and bisection (lifted unchanged, NF=3) solve the control's
`SRCTAPER` against the arm of record's band-summed window spread `sig_all(r6959_eta_cr_leafrec1)/r_s`.
- The arm of record's spread is **0.06447**, as cc66 measured. The namesake arm's is 0.06424 and the control's own is 0.06523.
- **SRCTAPER = 8.318682e-5**, against the banked 1.100878e-4. That is inside the registered [7.5e-5, 9.5e-5] ✔.
- `SRCTAPERS0` is the banked 145.346521, which is also what the solve's own default gives.
- At α′ the control's spread is 0.06447 of its r_s. That is the receipt's own swap gate (`< 2e-4`) ✔.

**The run.** `launch_b.sh`'s `swap_lcdm` verbatim: LSTEP=1, LMAXL=2000, and eleven 250-mode slices tiling 0–2547, all rc=0. Each slice's `SRCTAPER`/`SRCTAPERS0` is confirmed on the instrument's switch line by the launcher's own guard. The logs are in `logs_taper/`.

**The bank: an ADDITION.** The new file is `spectra/r6959_swap_lcdm_leafrec1.npz`, folded by `bank.py`'s own `fold`.
- It has the namesake's ten keys (`taper`, `taper_s0`, `taper_all=0`, `taper_norm=0`), plus `taper_target`, `config` and `manifest`.
- The namesake and the other five tapered banks are not touched.
- **Reader:** `P15_the_windows_phase_spread_is_nearly_equal_…` exits 0. It still reads the namesake; the re-point is cc66's.

**⛔ The registered size of the move MISSED.** I registered that the spectrum would differ from the namesake swap by under 0.5% of the peak. It differs by **0.93%**.
- The taper's own effect on the control (against the untapered `r6941_fine_lcdm`) is 4.20% of the peak at the banked coefficient and **3.29%** at α′. A coefficient a quarter smaller moves the effect by about a quarter, which is 0.9%.
- I estimated the size without that step. I report the miss and leave the band as registered.

## ② The three-grid audit on the arm of record

`audit_leafrec1.py` runs `r7101_70_three_grid_audit/audit.py` unchanged, except that `GRIDS` resolve per arm: `lcdm_*` comes from the namesake grid and `cr_*` from the sibling. `rigidity.py --grid` sees the same resolution. The output is `audit_leafrec1_log.txt`.

Parts (2) and (3) read `cr_base.log`, so the three siblings now carry one. These are the r7639 bank's own logs, matched by bit-identical `cr_base.npz`, and adding them is an **addition**.

At the arm of record, the banked and licensed siblings are the same spectrum: the licensed configuration is the refit grid.

| ℓ cut | 850 | 1000 | 1200 | 1400 | 1600 | 1800 | 1900 | 1996 |
|---|---|---|---|---|---|---|---|---|
| licensed − forbidden, P15 now | −1.0 | +14.4 | +51.0 | +67.9 | +74.7 | +84.0 | (+88.3) | +93.8 |
| **arm of record** | **−1.1** | **+14.2** | **+49.5** | **+66.7** | **+72.6** | **+81.3** | (+85.2) | **+90.2** |
| forbidden − control, arm of record | +0.1 | +0.3 | +0.2 | −0.3 | −0.1 | +0.1 | 0.0 | +0.1 |

P15 prints seven of these values; the 1900 cut is not among them.

**Predictions:**
- Monotone ✔.
- Last gap in [60, 130] ✔ (+90.2).
- First within ±5 ✔ (−1.1).
- Forbidden within 5 of the control at every cut ✔ (within 0.3 throughout, against up to 1.1 on the namesake).

The full-range statistics on the arm of record:
- licensed/banked cr χ² **276.4**, 54 crossings, longest run 33 (namesake 278.8, 54, 33);
- forbidden cr χ² **186.1**, 87 crossings, longest run 8 (namesake 185.0, 91, 8);
- control 186.0, 87, 8.

The audit's own literal check prints `** DIFFERS **` on the three cr rows. That is by construction, since those literals are the namesake's.

## ③ camb in `check_env_fingerprint`

- `live()` now reads `camb.__version__`, or `ABSENT (<error>)` when the import fails. `stored()` reads a `camb =` line.
- `receipts/ENV_FINGERPRINT.txt` gains `camb = 2.0.4`. This is not a refresh without a sweep: `camb==2.0.4` was pinned at r6981 (`17f7fe1c7`), before the r6985+70.1 sweep, so 2.0.4 is what that sweep ran on.
- The gate is green here, where camb is 2.0.4. It is **red** with camb shadowed by a failing import (`camb: 2.0.4 -> ABSENT (ImportError)`) and **red** with camb shadowed at 1.5.0 ✔.

## A correction to r7645 and r7647

Both RESULTs said their run logs were kept in `logs/`. They were written there, but `*.log` is gitignored and they were never committed. They are force-added in this push, as the namesake grids' logs were.

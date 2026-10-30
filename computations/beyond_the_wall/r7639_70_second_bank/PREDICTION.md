# r7639+70 — PREDICTION (pushed before any run of the second bank and before the retention own-comb form is computed)

## A. The second bank (69's items 1–6)
1. **Response grids, CR side**, rebuilt centred on the arm of record (H0 68.570730, Ωm 0.291246, ω_b 0.021643,
   n_s 1.015066, LEAFREC=1), each by its own launcher's form and steps (H0 ±2, Ωm ±0.015, ω_b ±0.0008, n_s ±0.02):
   `refit_grid` (LMAXL=1300), `refit_grid185` (LMAXL=2000), `grid_oneclock` (LEAFGEOM=1), `grid_licensed`
   (LMAXL=2000); and `r7201_cc66_loading_lever`'s three arm runs (RBFAC 0.1, 0.5, 1.5, NODRIVE=1, LEAFGEOM=1).
   The control files do not move. `best_cr`/`verify_cr` of `refit_grid` are its base.
2. `r6919_injected_cr` (five injections × six slices), `r6929_scan_cr` (six VISLEAF values, real and injected,
   × six slices), `r6941_fine_cr_visleaf` (VISLEAF=1 real, and the injection at f=0 and f=1, LSTEP=1). The
   control's `r6919` `viswap` carries the arm's visibility width (43.591) and is rebuilt with the arm of record's.
3. **Crossing spectra:** if the recorded command leaves LEAFSCALES unset (= 0), rebank `r6784_cr_crossing_*` and
   `r6794_cr_crossing_kcont_summed` on the arm of record with LEAFSCALES held at 0, replacing the LEAFSCALES=1
   `_leafrec1` files; the ladders receipt (re-pointed at r7637) moves with them.
4–5. Manifest notes: `r6885_dp0_cr_leafrec1` postdates the DPSRC wiring; the r6784 manifest's parenthetical;
   RECIPES.md's per-file map for r6911 (the one family whose control file moves too).

Gates: every `__SWITCHES__` line carries every recorded switch; every file carries the instrument's `config`
(check_banked_config); the grid bases reproduce `verify_cr_leafrec1` (refit_grid185's base) to 1e-11 of the peak.

## B. The retention statistic's own-comb form
`retained(win, nb, hi)` (cc66's, the cross-term receipt) reads per band the retention r = RMS of the projected
D_l oscillation / RMS of the source oscillation, and the arm/control ratio; the slope is averaged over twelve
(window, bands) settings. **Own comb:** each of the four banks (D_l and source, each arm) has its comb fitted by
the lifted fitters; the arm's D_l is carried onto the control's D_l comb coordinate and the arm's source onto the
control's source comb coordinate, each envelope window one of its own periods — the step statistic's rule, on
both sides of the ratio.

**Gates (fixed now):**
- Gr1, reproduction where the combs coincide: with each arm's comb parameters set to the control's, the own form
  equals cc66's `retained` to 1e-12 on all twelve settings.
- Gr2, the null (r7055's injection, both sides, combs refitted inside the statistic): at the REAL phase the null's
  twelve-setting slope is under one third of the own-comb slope, at both the pre-registered amplitude 0.5 and
  the declared amplitude (the banks' own); worst over phase reported at both, not gated.

**Bands (p ≈ 0.6):** on the arm of record the own-comb twelve-setting slope lies in [0.000, +0.015] with a setting
spread under 0.004; on the old arm it lies below the shared +0.0136.

**Reachable negative (69's wording):** on the own comb the retention slope does not survive its null subtracted
at the real phase — slope − null(real) under twice its setting spread.
**The outcome that settles it:** it survives at a stated size (slope − null over twice the spread), or it is shown
to be the null's (under it).

**EFFORT.** About 30 core-hours of runs (four grids ~40 runs, r6929 72 slices, r6919 35, the LSTEP=1 visleaf 18,
the crossing set 9): 7–9 hours wall on four cores. The retention form: two hours, alongside.

# r7639+70 — RESULT A: the second leaf-rate bank

**50 files are banked.** Spectra sit beside their namesakes as `<name>_leafrec1.npz`. The GRIDS sit in sibling directories, `<dir>_leafrec1/`, under their namesakes' own file names, because receipts glob the grid directories: a suffixed file inside one made cc66's phase-slope receipt count it, and CI caught that. Each carries the instrument's own `config` and a `manifest` key. The launcher is `launch.sh` (171 runs); the fold is `bank.py`; the record is `MANIFEST.json`. All gates hold and `check_banked_config` is green.

1. **The response grids, CR side, centred on the arm of record** with each launcher's steps (H0 ±2, Ωm ±0.015, ω_b ±0.0008, n_s ±0.02):
   - `refit_grid_leafrec1/` (LMAXL=1300), 9 runs, plus `best_cr` and `verify_cr`, which on the arm of record are its base;
   - `refit_grid185_leafrec1/` (LMAXL=2000), 9, plus `verify_cr`;
   - `r7095_directions/grid_licensed_leafrec1/`, 9 — the refit_grid185 runs, because with LEAFREC=1 the default the two recipes are now one;
   - `r7093_directions/grid_oneclock_leafrec1/` (LEAFGEOM=1), 9, each carrying its `__ONECLOCK__` gate line;
   - `r7201_cc66_loading_lever_leafrec1/`: RBFAC 0.1, 0.5 and 1.5, and NODRIVE.

   The grid base reproduces r7633's `verify_cr_leafrec1` to 6.8e-13 of the peak, the thread-count residue G1 already carries. The control files do not move.
2. `spectra/r6919_injected_cr_leafrec1` holds the five injections. `spectra/r6919_injected_lcdm_leafrec1` is the CONTROL: only its `viswap` moves, because that key carries the arm's visibility width (43.591 → **43.957**). `spectra/r6929_scan_cr_leafrec1` holds six VISLEAF values, real and injected. `spectra/r6941_fine_cr_visleaf_leafrec1` holds VISLEAF=1 real and the injections at f=0 and f=1, at LSTEP=1.
3. **The crossing set at its recorded LEAFSCALES=0.** README:47's command leaves LEAFSCALES unset. So `r6784_cr_crossing_{hier,hier_noCRIC,los}_leafrec1` and `r6794_cr_crossing_kcont_summed_leafrec1` are rebanked with it held at 0, at the arm of record's point. They replace r7635's LEAFSCALES=1 files.
   - **The radiation-free ruler reads 171.55**, where the LEAFSCALES=1 rebuild read 302.9.
   - Their manifests now name the crossing configuration and the arm of record's point, which also settles cc66's note on the old parenthetical.
   - The ladders receipt moves with them: χ² 923.95 → **926.39**, P₁/P₂ 2.136 → **2.144**, P₁/P₃ 2.167 → **2.188**; the ladder and the continuum still agree, to 1e-4 in χ² and 7.1e-8 of the peak.
4. `r6885_dp0_cr_leafrec1`'s manifest says that the file postdates the DPSRC wiring, and that its namesake's bit-identity is HISTORICAL.
5. RECIPES.md now has the per-file map for r6911, the one family whose control file moves too, and the same note for r6919's `viswap`.

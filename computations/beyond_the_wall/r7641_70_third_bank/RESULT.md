# r7641+70 — RESULT: the third leaf-rate bank (cc66's gap list) and 60's corrections to the bank's records

**① Fifteen files are banked**, each beside its namesake as `spectra/<name>_leafrec1.npz`, in the namesake's own format, with `config` and `manifest` (`launch.sh`, 102 runs; `bank.py`; `geometry.py`; `MANIFEST.json`). Every gate holds and `check_banked_config` is green.

| file | recipe |
|---|---|
| `r6893_switch_screen_cr` | 62 switches at `HIER=1 LSTEP=16 LMAXL=500`, the screen's own absolute switch values; screen.sh plus the later passes' cr runs (pass2 `pairLATARG`/`pairGSRC`/`pairKCONT`, pass5 `SWSRC`, pass6 `annot`); the LEAFSCALES variant at 0, as recorded |
| `r6893_fine_grid_cr` | A: LSTEP=2, LMAXL=900, whole, base and NUFS=0. B: LSTEP=4 in six slices of 250. The slice-sum pair at the screen grid |
| `r6925_visleaf_cr` | VISLEAF=1, the injection and the comb, six slices each |
| `r6885_{ln24,noisw,dre0,drc0}_{cr,lcdm}` | both arms, HIER=1, LSTEP=8, LMAXL=2000 |
| `r6889_{noop,hdp0,hsw0}_cr` | HIER=1, LSTEP=8, LMAXL=2000 |
| `r6929_geometry_leafrec1` | r6929 `geom.py`'s probe unchanged, the arm of record's fifteen-VISLEAF arm; the control's keys are the namesake's own |

**Predictions, all held:**
- **The control's four knob runs rebuild their namesakes** to 0 – 3.6e-16 of the peak. LEAFREC does not reach the control.
- **`r6889_noop_cr_leafrec1` equals `cc66_r185_verify_cr_leafrec1` bit for bit.**
- **The screen's failed list is the namesake's, switch for switch.** One switch, `pairLATARGbase`, fails on both arms. With ZSTART unset on the leaf ruler, the onset solve has no root in its bracket, and the instrument says so ("f(a) and f(b) must have different signs").
- **The geometry's ℓ_A does not move with VISLEAF** (302.943051, spread 0). On the arm of record:
  - the FWHM runs 43.957 → 44.321 (old arm 43.231 → 43.952);
  - r_D runs 7.5752 → 7.2689 (old arm 7.4730 → 7.1682).

**② 60's corrections are applied** to RECIPES.md, MANIFEST_old.json and the files' `manifest` keys:
- **h686, h6862, h686_L2000 and refit_verify:** their namesakes sat at **LEAFSCALES=1**. The old `held` said 0, which was wrong. The h6862 note now says that its namesakes are two runs, 1.19e-3 apart, so one rebuild cannot be compared with both.
- **cc66_cr_x_lstep1:** its command is **recovered**: the built-in default point with ZSTART=3e7, the onset not solved. The low-confidence note is retired at the background layer; its path switches remain unrecorded.
- **cc66_refit_verify:** its point is **exactly** 68.6077, 0.2967, 0.0217, 0.9949.
- **The LEAFREC default:** RECIPES.md now says that every recorded command in its table predates cc66.75 and omits LEAFREC. So each one, run verbatim today, rebuilds the leafrec1 arm; add `LEAFREC=0` to rebuild a namesake.
- **The r6784 entries** in MANIFEST_old.json are marked superseded by r7639's LEAFSCALES=0 rebank.

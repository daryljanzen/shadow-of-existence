# r7643+70 — PREDICTION (pushed before any run)

**① The no-fit configuration on the arm of record: the distances' point with LEAFREC=1.** The original recipes run
verbatim with `LEAFREC=1` set explicitly: `refit_grid185`'s nine arm runs (LMAXL 2000) and `refit_grid`'s nine (LMAXL
1300), centred on CRH0 68.60, CROM 0.2973 with the built-in ω_b and n_s, banked in sibling directories
`refit_grid185_leafrec1_distances/` and `refit_grid_leafrec1_distances/` under the namesakes' file names; and the
`cc66_cr_x_*` family at its own points — `h686_L2000` (68.60), `h686_pol` (68.60), `h6862_pol` (68.62), banked as
`spectra/<name>_leafrec1_distances.npz` (the pol pair as TWO runs, 60's r7640 note).
- Gate: the no-fit `cr_base` differs from `refit_grid185_leafrec1/cr_base.npz` (the refitted one): |ΔD_M| > 1 Mpc.
- Prediction (p ≈ 0.6): the lensed no-fit ratio to the control lies in [2.2, 2.9] (the paper's 2.57 on LEAFREC=0),
  i.e. LEAFREC moves the no-fit headline by under 15 per cent; the refit pair stays at cc66's 1.60 ± 0.05.
  Reachable negative: the no-fit ratio leaves that band — P15's headline moves by more than 15 per cent.

**② The keys cc66's partition names**, as `<name>_leafrec1.npz` carrying the namesake's keys unchanged plus
arm-of-record keys with the arm token `cr` → `cr_leafrec1`: the noop family (`r6897`, `r6911` incl. `xsonly`,
`r6915`, `r6919`, `r6925`, `r6929` `unset`/`zero`), the geometry family (`r6919`, `r6925`, and `r6929` re-keyed the
same way), and `r6897_fields` (ZPSAVE at LSTEP=64). And `c54.178_cr_leafrec1_distances`: the c54.178 command at
CRH0 68.62, CROM 0.2973, ZSTART 3e7, LEAFREC=1, LEAFSCALES unset — the crossing receipt's own definition.
- Prediction: every noop run equals its arm-of-record plain run at the same grid to 0 (they set nothing).

**③ 60's twenty-fourth Layer-2 reading:** `r6941_fine_cr` rebuilt at ITS OWN configuration (60's CONFIGS entry,
LEAFREC=0 set explicitly), in the namesake's own six KSLICE pieces, compared with the namesake as 60's `layer2.py`
does. Prediction: it reproduces the namesake to under 1e-11 of the peak (one thread each, the same procedure).

**④ Notes:** `r6885_dp0_cr` and `r6784_cr_crossing_los` namesakes mislabelled (run without the switch the name
claims); the manifest/config storage note in RECIPES.md.

**EFFORT.** ~25 runs at LSTEP=8 (the two grids), 3 at LSTEP=2, 6 LSTEP=1 slices, a dozen short ones: ~12 core-hours,
3–4 hours wall.

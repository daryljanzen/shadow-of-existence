# r7643+70 — RESULT

**The no-fit spectrum on the arm of record now exists, and P15's lensed headline moves from 2.57× to 2.35× (−8.8%).
Both registered predictions hold.** 37 instrument runs, all rc=0. 32 files banked. Every gate holds, including
`corpus/check_banked_config.py`. Fold: `bank.py` (idempotent; it re-runs to the same files). Scoring: `measure.py`
(→ `measure.json`), which uses the refit-bound receipt's own CAMB lensing operator and `chi2_of_spectrum.chi2_of`
on 185 lensed bins.

## ① The distances' point with LEAFREC=1

The original recipes run verbatim with `LEAFREC=1` added: CRH0 68.60, CROM 0.2973, built-in ω_b and n_s.

**Where the files are:**
- `refit_grid185_leafrec1_distances/`: nine arm runs at LMAXL 2000.
- `refit_grid_leafrec1_distances/`: nine arm runs at LMAXL 1300.
- In both, the file names are the namesakes'. Grid readers take the control from the namesake dir, as in r7639; LEAFREC does not reach the control (3.6e-16, r7641).
- `spectra/cc66_cr_x_{h686_L2000,h686_pol,h6862_pol}_leafrec1_distances.npz`.
- The instrument writes the unlensed spectrum. The lensed one is the receipts' operator applied to it, so a single file serves both.

**Gate:** the no-fit `cr_base` has D_M 14011.46 Mpc, against 14133.95 for `refit_grid185_leafrec1/cr_base.npz`. |ΔD_M| = 122.5, well above the gate's 1. The no-fit D_M, l_A and r_s equal the LEAFREC=0 namesake's exactly, as they should, because LEAFREC does not touch the background.

**The headline, 185 lensed bins, arm / control:**

| configuration | control χ² | arm χ² | arm/bin | ratio |
|---|---|---|---|---|
| no-fit L2000, LEAFREC=0 (the paper's) | 214.1 | 550.5 | 2.98 | **2.572×** |
| no-fit L2000, LEAFREC=1 (this bank) | 214.1 | 502.1 | 2.71 | **2.346×** |
| grid base LSTEP 8, LEAFREC=0 | 212.9 | 545.8 | 2.95 | 2.564× |
| grid base LSTEP 8, LEAFREC=1 | 212.9 | 496.5 | 2.68 | 2.332× |
| refit verified minimum, LEAFREC=0 | 186.5 | 292.4 | 1.58 | 1.568× |
| refit, LEAFREC=1, arm of record | 186.5 | 297.7 | 1.61 | 1.596× |

**Old → new:**
- no-fit lensed ratio 2.57 → 2.35;
- no-fit arm per bin 2.98 → 2.71;
- refit ratio 1.57 → 1.60;
- refit arm per bin 1.58 → 1.61.

cc66's 1.41 read the refitted `refit_grid185_leafrec1/cr_base` through the no-fit pointer. Scored here against the no-fit controls, that file gives 1.39–1.40, so it is not a no-fit figure.

**Predictions:**
- Lensed no-fit ratio in [2.2, 2.9]: **2.346, HOLDS**. LEAFREC moves the headline by 8.8%, under the 15% band.
- Refit at 1.60 ± 0.05: **1.596, HOLDS**.
- The reachable negative, the headline moving by more than 15%, did not fire.

## ② cc66's keys

**The noop family** (r6897, r6911 with `xsonly`, r6915, r6919, r6925, r6929 with `unset`/`zero`):
- Each file keeps its namesake's keys unchanged and adds `__cr_leafrec1` keys from the arm of record.
- Prediction held: every noop run equals the plain arm-of-record run at the same grid, bit for bit. The xsonly (SRCXS=1.5) and VISLEAF=0 runs were checked separately and are also bit-identical.

**The geometry family** (r6919, r6925, r6929):
- Same layout. The `__cr_leafrec1` D_M is 14133.95, the arm of record's.
- `r6929_geometry_leafrec1.npz` is re-keyed from r7641's file. Its `__cr` keys are now the namesake's, and the arm-of-record values moved to `__cr_leafrec1`. No reader of the old meaning exists outside r7641's own `geometry.py`.
- A second run of the first draft of the fold read its own output and wrote the namesake's values under `__cr_leafrec1`. Caught on inspection; the fold now reads the right key and is idempotent.

**`r6897_fields`:** ZPSAVE's output at LSTEP=64, with keys suffixed the same way.

**`c54.178_cr_leafrec1_distances`:** the crossing receipt's own definition, i.e. the c54.178 command at 68.62/0.2973, ZSTART 3e7, LEAFSCALES unset, with LEAFREC=1.
- It is not comparable to its namesake `c54.178_cr`, which is the superseded pinned configuration (D_M 13004.6).
- Against the receipt's own LEAFREC=0 crossing run `r6784_cr_crossing_hier_noCRIC` (the arm's own datum), with the receipt's own `score` and `peaks`:
  - χ² 1205.4 → **1209.5**;
  - peaks 220/540/820/1132 → **220/532/812/1132**;
  - l_A 172.32 and D_M 14007.37, both unchanged.
- It still sits under the control's 1320.5.

## ③ 60's twenty-fourth Layer-2 reading

`r6941_fine_cr` was rebuilt at its own configuration (68.581133 / 0.297209 / 0.021524 / 0.997952, LEAFREC=0, LSTEP=1, LMAXL 2000) in the namesake's six KSLICE pieces. Each slice took about 8–12 minutes on one thread.

Against the namesake:
- same `ls`;
- max|ΔD_l|/max = **0.0**;
- 60's own `layer2.rel_of`, lifted, returns (0.0, True).

The prediction was under 1e-11; it reproduces bit for bit. The rebuild is `r6941_fine_cr_rebuilt_leafrec0.npz`, beside this file.

## ④ Notes

- Both mislabelled namesakes are flagged in their `_leafrec1` manifests (`note_r7643`).
- RECIPES.md now carries the storage note. All 69 `_leafrec1` files' manifests parse as JSON, and none as a bare Python repr. `config` is JSON with `true`/`false`, so `ast.literal_eval` fails on it.

## Pre-push gates

- `check_banked_config`: passes.
- `run_touched_readers.sh`, class one (the readers of the changed files): **GREEN**.
- Class two shows two reds, `check_sitemap_resolves` (no `_site/` assembled) and `check_receipts_run` (cached run is from an old tree). Both reproduce identically on a clean `origin/main` worktree in this container. They come from the container, not from this tree.

# r7673+70 — PREDICTION (registered before item 1's runs and item 3's measurement)

**Already measured before this file, and said so rather than registered:** item 2. `corpus/make_fig_acoustic_nofit.py`
was re-run once (17 s). Its `nofit_figure_numbers.npz` came back bit-identical in every key, and its two CR inputs are
already arm-of-record files (`refit_grid185_leafrec1_distances/cr_base.npz`, D_M 14011.46;
`spectra/cc66_r185_verify_cr_leafrec1.npz`, D_M 14133.95). That item carries no prediction.

## Item 1 — `spectra/r7041_accept_cr.npz` on the arm of record

**Recipe:** the CR half of `r7039_directions/launch.sh`'s transfer runs: `SRCINJ=fixed` and
`SRCINJ=sweep SRCINJRS=own`, `HIER=1 LSTEP=8 LMAXL=2000`, six `KSLICE` pieces of 250 with `DLKSAVE`. It is folded by
`r7039_directions/bank.py`'s transfer fold, then thinned by `r7041_directions/bank_thin.py` (lifted, CR arm only).
It is built twice: lr0 at the recorded CR point with LEAFREC=0, and lr1 at the refit licensed point with LEAFREC=1.

- **P1.** My r7041 build did **not** produce this file. My four `_leafrec1` files are the GRIDSAVE/A_l bank; this one is the thinned injection transfer.
- **P2.** lr0 reproduces `spectra/r7041_accept_cr.npz` exactly in every key.
- **P3.** On lr1 the CR keys move, and `A` (the law's output) moves by under 2% in mean. My r7041 A_l moved +0.5%.
- **P4.** Wall time under 40 min on 4 cores for both builds.

## Item 3 — `cc66_lowell_sweep`

- **P5.** HIER's recombination rate with ARM unset has the same **form** as the arm of record's (`Hleaf`: content-carrying, radiation in the rate). It is evaluated at the sweep's adjudicated point (68.60, 0.2973, ω_b 0.02237), not at the refit licensed point.
- **P6.** It is **not** the arm of record, for a second reason. With ARM unset, HIER also builds the conformal-time grid and the projection distance on that same leaf rate. That is the one-clock arrangement (`LEAFGEOM=1`'s), not the arm of record's split (geometry on the stacking rate, recombination on the leaf). HIER's `ARM=cr` is the other single-clock arrangement (`LEAFREC=0`'s). No setting of HIER reproduces the split.
- **P7.** The cheapest arm-of-record approximation is the sweep with the adjudicated background moved to the refit licensed point, priced by timing one DECOUPLED configuration (cc66's docstring: about 9 min each, 8 configurations). The exact form needs a split-clock switch in HIER, which is not built here.

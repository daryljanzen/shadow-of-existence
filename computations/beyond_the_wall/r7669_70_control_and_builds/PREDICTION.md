# r7669+70 — PREDICTION (registered before any run)

## ① The control under the switch

Build: r6941's own control recipe (`r6941_directions/launch.sh`): `ARM=lcdm LH0=67.410309 LOM=0.309826
WBH2=0.021966 NS=0.954248 HIER=1 LSTEP=1 LMAXL=2000`, eleven `KSLICE` pieces of 250 over NK 2547. The
same recipe once with `LEAFREC=0` and once with `LEAFREC=1`, through the identical code (same tree,
same machine), folded the way `r6941_directions/bank.py` folds them.

- **P1.** LEAFREC=1 vs LEAFREC=0: max|ΔD_l| / max|D_l| = **0 exactly** (bit-identical). Stated tolerance
  for "identical": ≤ 1e-15. Basis: r7641's four control knob runs rebuilt their namesakes to 0–3.6e-16,
  and r7633's fourth control feature did not move.
- **P2.** The LEAFREC=0 build reproduces `spectra/r6941_fine_lcdm.npz` to ≤ 1e-12 (r7643 rebuilt the
  arm's `r6941_fine_cr` bit for bit).
- Reachable negative: any relative difference above 1e-12 between the two settings says the switch
  reaches the control, and then the control paths join item ②'s build list.

## ② Pricing (the 32 unbanked paths of r7667's census, all 32 read by a demonstrably-namesake item)

- **P3.** 20 of the 32 are control (lcdm) paths; on P1 they leave the list with no build.
- **P4.** Of the 12 CR-arm paths, the 7 under `r7642_60_…/rebuilt/` (60's LEAFREC=0 rebuilds of
  `spectra/` namesakes) **already have an arm-of-record twin** as `spectra/<name>_leafrec1.npz`; the
  census tests only the same directory. They need a repointing, not a build.
- **P5.** The 4 `r7041_accept_*` files (one producer, `r7041_directions`) are rebuildable today at their
  recorded configuration with LEAFREC=1: none of them is among r7640+60's twelve, and their KFAC runs
  are KFAC ≥ 2.6, explicit.
- **P6.** Wall times are stated per build, measured on this 4-core runner, not guessed in the report.

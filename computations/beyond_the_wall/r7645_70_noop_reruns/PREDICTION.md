# r7645+70 — PREDICTION (pushed before any run)

**What the order asks is already in the bank, from r7643; this order re-runs it to show it.** cc66's `r7643+cc66.64`
(and its reader `r7641_cc66_grid_readers/a_quantity_can_move_when_its_bank_cannot.py`) was measured on the tree
BEFORE r7643 merged. r7643's launch.sh line 42–44 ran each no-op as its own instrument run, by the namesake's own
recorded command (`r68xx_directions/launch.sh`: `HIER=1 $CR LSTEP=16 LMAXL=500`, plus `SRCXS=1.5` for r6911's
xsonly and `VISLEAF=0` for r6929's zero) with `$CR` replaced by the arm of record, LEAFREC=1 by the instrument's
default (`config` records it true). Those are the `__*cr_leafrec1` keys in `spectra/r6{897,911,915,919,925,929}_noop_leafrec1.npz`.
On today's tree, cc66's reader fails its own falsifiable clause ("a copy in any OTHER sibling bank would be a
legitimate stand-in and would fail this gate"): it finds 27 copies, 8 of them in the six no-op siblings.

**① The re-run.** The eight no-op runs again, fresh, by the same commands with `LEAFREC=1` now SET explicitly
(so `__SWITCHES__` names it): r6897_noop_cr, r6911_noop_cr, r6911_xsonly_cr, r6915_noop_cr, r6919_noop_cr,
r6925_noop_cr, r6929_unset_cr, r6929_zero_cr.
- Prediction: each is **bit-identical** to its r7643 banked `__*cr_leafrec1` key AND to
  `r6893_switch_screen_cr_leafrec1`'s `Dl__base` (one thread each; the instrument is deterministic at fixed
  threads). Reachable negative: any max|ΔD_l| ≠ 0 — then the r7643 keys were not what this order asks for, and the
  fresh runs replace them.

**② Item 2.** `r6919_geometry_leafrec1` already carries every key cc66 names as missing (`d_rs_own`, `jac_lo/hi/pk`,
`rs_ls_own`, `d_chi`, … under `__cr_leafrec1`), from probes run at the arm of record in r7643; `r6919_noop` is in ①.
`r6897_fields`' "per-k fields at two baryon densities" are `wblo`/`wbhi`, which are **control** runs (`arm__wblo` =
`arm__wbhi` = lcdm): LEAFREC does not reach the control (r7641: 3.6e-16), so the namesake's are already the
arm-independent record. Prediction: a re-run of `zp_wblo` at LEAFREC=1 by zpcal.sh's own command reproduces the
namesake's `wblo` fields to ≤ 1e-12 relative. Reachable negative: it does not — then the control moves and both
baryon-density fields need `_leafrec1` keys.

**③** Provenance: each run's log copied beside this file; `verify.py` reads them.

**EFFORT.** 9 runs at LSTEP=16/64, ~30 min wall on 4 cores.

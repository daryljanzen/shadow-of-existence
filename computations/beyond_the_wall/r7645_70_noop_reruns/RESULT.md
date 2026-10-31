# r7645+70 — RESULT

**The arm-of-record no-op runs exist, and they did before this order. All eight re-runs with `LEAFREC=1` set
explicitly are bit-identical to the keys r7643 banked, and to the screen's `Dl__base`. Every prediction holds.**
`verify.py` (exit 0); the logs are in `logs/`.

## Why the order found them missing

cc66's `r7643+cc66.64` and its reader `r7641_cc66_grid_readers/a_quantity_can_move_when_its_bank_cannot.py` were
measured on the tree before r7643 merged.

- **What r7643 ran.** Its `launch.sh` lines 42–44 ran each no-op as its own instrument run. Each used the original run's own
  recorded command (`r68xx_directions/launch.sh`: `HIER=1 $CR LSTEP=16 LMAXL=500`, plus `SRCXS=1.5` for xsonly and
  `VISLEAF=0` for r6929's zero), with `$CR` replaced by the arm of record.
- **Where they are.** The runs are the `__*cr_leafrec1` keys in `spectra/r6{897,911,915,919,925,929}_noop_leafrec1.npz`.
- **cc66's reader on today's tree.** It now fails its own falsifiable clause. That clause says "a copy in any OTHER sibling bank would be a legitimate stand-in and would fail this gate". It finds 27 copies of the base, and 8 of them are in those six no-op files.

## ① The re-runs, fresh, with LEAFREC=1 set

| run | rc | = r7643 key | = screen `Dl__base` |
|---|---|---|---|
| r6897_noop_cr | 0 | True | True |
| r6911_noop_cr | 0 | True | True |
| r6911_xsonly_cr (SRCXS=1.5) | 0 | True | True |
| r6915_noop_cr | 0 | True | True |
| r6919_noop_cr | 0 | True | True |
| r6925_noop_cr | 0 | True | True |
| r6929_unset_cr | 0 | True | True |
| r6929_zero_cr (VISLEAF=0) | 0 | True | True |

Every `__SWITCHES__` line names `LEAFREC=1`.

**No figure moves.** The re-runs equal what is banked, bit for bit. The manifests of the six files carry a `note_r7645` saying so.

For the four receipts' identity legs, comparing these keys with `r6893_switch_screen_cr_leafrec1`'s `Dl__base` is a real test, not a tautology. Each key comes from a separately launched run whose log is in `logs/`, and each lands on the base. That landing is what the legs assert.

## ② What `r6919_geometry` and `r6897_fields` lack

- **`r6919_geometry_leafrec1`:** carries all 15 of the cr keys under `__cr_leafrec1`, from r7643's probes at the arm of record. That covers every key cc66 names (`d_rs_own`, `jac_lo/hi/pk`, `rs_ls_own`, `d_chi`, …). `r6919_noop` is in ①.
- **`r6897_fields`, the "per-k fields at two baryon densities":** these are `wblo` and `wbhi`, which are **control** runs (`arm__wblo` = `arm__wbhi` = lcdm).
  - `zp_wblo` was re-run by `zpcal.sh`'s own command with LEAFREC=1 set. It reproduces the namesake's 18 `wblo` keys with a max relative difference of **0.0**.
  - LEAFREC does not reach the control, so the namesake's wblo/wbhi already serve as the record on both arms.
  - The arm's own fields at the arm of record are under `__cr_leafrec1` (r7643).
- **So nothing is lacking.**

## What is cc66's

The reader `a_quantity_can_move_when_its_bank_cannot.py` is red on main: 5 gates, all on the premise that no arm-of-record no-op or geometry run exists. That reader belongs to cc66, and so do the re-points it gates (`.57`, `.61`, `.62`, `.63`, `.65`, and the two "genuinely blocked" receipts). I have not edited it. The no-op legs can now move onto the `_leafrec1` keys.

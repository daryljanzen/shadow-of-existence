# r7647+70 — RESULT

**`r6893_slice_check` is banked at the arm of record, and both predictions hold.** Seven runs, all rc=0.
`bank.py` exits 0. `check_banked_config` passes.

## The fold: an ADDITION, not a re-key (69's r7647 convention)

`spectra/r6893_slice_check_leafrec1.npz` holds:
- the namesake's twelve keys, unchanged (`__lcdm` and `__cr` both bit-identical to the namesake's);
- six added keys, `nsl/amax/rmax/ls/Dl_whole/Dl_sliced__cr_leafrec1`;
- `config` (LEAFREC true) and `manifest`.

The recipe is `r6893_directions/step0b.sh` verbatim on the cr arm, with `$CR` set to the arm of record and `LEAFREC=1` set. The fold is `bank2.py`'s step 0b. The control was not re-run, because LEAFREC does not reach it. The logs are in `logs/`.

## Predictions

| | namesake cr | arm of record | registered |
|---|---|---|---|
| slices | 6 | **6** (0–1452 tiled) | the namesake's count |
| max \|ΔD_l\| sliced − whole | 8.33e-17 | **5.55e-17** | — |
| relative | 1.89e-16 | **1.33e-16** | < 1e-14 ✔ |
| whole spectrum vs the namesake's | — | **5.71e-2** max relative | in [1e-3, 1e-1] ✔ |

**Old → new:** the receipt's arm-side figure `rmax__cr` goes 1.886e-16 → 1.334e-16, and both sit under its 1e-14 gate. Slicing still adds exactly at the arm of record. So the sliced banks on it (fineB, visleaf, the r6941 rebuild) stand.

## Readers run before the push (r7647 convention)

I found the readers by bank stem `r6893_slice_check`, not by the file name.

- **`P15_the_free_streaming_knob_…`** (the receipt this order unblocks) exits 0. It still reads the namesake; the re-point is cc66's.
- **`item_two_inventory_partitions_the_44`** exits 0.
- **`which_key_gaps_actually_block`** exits 0 on `origin/main` and **3 FAIL** with this file. All three failures are its pinned "r7643's fold closed TEN of the ELEVEN key gaps … except `r6893_slice_check`, which has no sibling".
  - This file is that sibling. The reader's own classifier counts it as form B (a superset, which is the r7643 form), so the count is now eleven of eleven.
  - It is cc66's reader, and no CI job runs it. I have not edited it; it is cc66's to re-pin at 11 of 11.
- **`run_touched_readers.sh --class1`** is GREEN.

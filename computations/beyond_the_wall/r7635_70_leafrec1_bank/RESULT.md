# r7635+70 — RESULT (interim: the bank's first half, the dry re-point, and the registered negative)

**1. The bank, first half — pushed.** Eleven `_leafrec1` files in `spectra/`, each with a `manifest` key:
- cc66_r185_verify, the four r6885 files, r6889 nufs0;
- r6911 source (and kcont), r6915 pairs, r6941 fine, r6959 eta.

Recipes are their own launchers' (`RECIPES.md`, `launch_clean.sh`, `bank_clean.py`).

Gates:
- G2–G4 hold.
- G1 was registered "bit for bit" and **missed in that form**. The plain arm differs from r7633's `verify_cr_leafrec1` by 6.8e-13 of the peak, because r7633 ran on two BLAS threads and this bank on one. It is gated at 1e-11.

The second half is computing:
- c54.*, item38, r4494, r6784/r6794, cc66_cr_x_*, cc66_refit_verify (`launch_old.sh`, 27 runs);
- then the control's r6911 source with its `SRCXS` re-pointed (`launch_xs.sh`).

**2. Registered bands on the bank:**

| band | result |
|---|---|
| contrast ratio ‖Δ‖ (P15 l.1122), in [1.02, 1.07] | 1.040 → **1.044** ✔ |
| NUFS shift common to the arms, under 0.5 | **0.185** at most ✔ |
| KCONT reproduces the ladder, under 1% | **8.5e-8** ✔ |
| fine-grid fourth peak arm − control, +0.52 ± 0.3 | **+0.518** ✔ |

The fine grid agrees with LSTEP=8 at shared ℓ to 5e-16.

**PO-87's closing outcome is reached on the fine grid.** Through the identical locator, the control's fourth-peak residual is +5.32 against the arm's +5.84. So 0.91 of it is the control's own.

**3. The reachable negative FIRED, in the excess/step family.** On the arm of record, the seven band ratios of the arm's contrast excess are 1.0186, 1.0818, 1.0373, 1.0868, 1.1005, 1.0141 and 1.1617. On r6941 they were a smooth rise with band 1 low: 1.0215, 1.0574, 1.0519, 1.0606, 1.0748, 1.0659, 1.0762.
- Band 1 is no longer the lowest band; band 6 is.
- My own r7055 receipt (`P15_the_phase_systematic_leaves_the_step_standing…`) now fails its headline. The step's worst false value over phase is 0.036 against a step of 0.062, so it is not under half.
- The comb-phase null returns **108–115%** of the reported rise in its own direction, so the rise does not survive the null's subtraction (−0.0040, −0.0022).
- The probable mechanism is the comb period:
  - The arm's acoustic scale moved 301.80 → 302.94, against the control's 301.54. The arms' combs now differ in period by 0.46% (T 1.0045 vs 1.0092).
  - Band statistics read on a shared comb then beat, which is the alternation above.
  - So on the arm of record the excess family's band figures are dominated by a systematic of the statistic, which r7055 built the null to measure.

This is named, not concluded: whether the step and the rise are gone or only mis-read is the owners' question.

**4. The dry re-point (`DRYRUN.md`, `dry_repoint.sh`, `dry/`).** Every §B receipt that reads only the first half was run unedited on the arm of record: 35 of 51. 34 move at least one pin.
- The diffs per receipt are each seat's old → new figures.
- `dry_repoint.sh <stem>` reproduces any of them without touching the tree.
- 16 receipts wait on the second half.

**5. Census gap (control-side).** These control files carry a coefficient solved from the OLD arm:
- r6911 `SRCXS` (1.004492 → 1.012871 on the new arm; being banked);
- the r6959 tapers (`SRCTAPER`, `SRCTAPERS0`);
- r6975 `DPSRC=0.8794`;
- r6983 joint.

The last three are solved by their receipts' own procedures, so re-solving them is their owners' re-point, not a bank run.

**6. My receipts (70's and the ownerless c54).**

| receipt | old → new |
|---|---|
| resolution table (r7029) | band-1 likelihood floor 0.0550 → **0.0429**; the per-band smallest shares 0.055/0.047/0.040/0.045/0.057/0.081/0.141 → **0.043/0.036/0.031/0.035/0.044/0.065/0.107** |
| three instruments (r7033) | reg 1.0468 → **1.0462** on the binned rung; floors 2.6 → 2.6; no pin fails |
| phase systematic (r7055) | the step and the rise fail, as in 3 |

The c54 receipts wait on the second half. Pins are not moved yet: the step family needs a ruling first (see the reply).

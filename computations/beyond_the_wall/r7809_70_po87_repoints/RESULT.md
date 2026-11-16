# `r7809+70` ③ — PO-87's 14 repoints, read and measured

**The short answer: 12 of the 14 already read the arm of record. 2 read the namesake deliberately, under 69's own HISTORICAL ruling. 1 is a genuine repoint, and its finding reverses on the arm of record.** Nothing in the tree was changed. Every run here is a temporary copy beside the receipt, deleted after it ran.

## How it was measured, and why the first pass is not the answer

`repoint.py` first rewrote every namesake name to its `_leafrec1` twin and diffed the printed numbers (`out/SUMMARY.json`, `out/*.{orig,rep}.txt`). That pass failed in two ways, and it is kept so the failure is on record:
- **Some rewrites doubled.** Receipts that already build the twin path in code (`GRID + '_leafrec1'`) became `_leafrec1_leafrec1`.
- **The twin grid directories hold only the arm's `cr_*` files.** The control's `lcdm_*` files are in the namesake directory, correctly, because a control has no leaf rate. So a blanket rewrite broke the control reads.

Each receipt was then read by hand for which loads carry its figures.

| item | receipt (prefix) | what it reads | verdict |
|---|---|---|---|
| 01 | `P15_a_source_with_no_physics_...` | `r6919_*_leafrec1`; the namesakes **only to gate the convention** (l.196, l.204) | already repointed; the blind pass moved 0 of 527 numbers |
| 05 | `P15_the_contrast_excess_is_symmetric_...` | `r6929_geometry_leafrec1`; the namesake only for the convention gate | already repointed |
| 06 | `P15_the_control_entered_the_regime_...` | the c54 namesakes, **on purpose**: `⌛ HISTORICAL (r7637+70, 69's ruling)`, with a guard that fails if a CR file is not the LEAFREC=0 namesake. The arm-of-record figures are in `r7635_70_leafrec1_bank/DRYRUN.md` | a deliberate historical pin, not a repoint |
| 17 | `P15_the_model_difference_is_an_acoustic_contrast_...` | arm `cc66_r185_verify_cr_leafrec1`; the r6885 line-of-sight block is **pinned as history** (l.114, l.652) | the arm already repointed; the r6885 block is a deliberate historical pin |
| 18 | `P15_the_monopole_zero_point_...` | `r6897_fields_leafrec1`, `r6897_noop_leafrec1`, arm `..._leafrec1`; the namesakes only as comparisons | already repointed |
| 30 | `P15_there_is_no_phase_residual_...` | `cc66_r185_verify_cr_leafrec1`; the namesake only as a comparison | already repointed |
| 31 | `P15_three_quarters_of_the_arms_residual_...` | `cc66_r185_verify_cr_leafrec1`; the namesake only as a comparison | already repointed |
| g2 | `P15_the_fit_has_the_controls_freedom_...` | `GRID_AOR = GRID + '_leafrec1'` for the arm; `refit_grid185/` for the control and metadata | already repointed |
| g3 | `P15_the_kernels_phase_difference_...` | `AGO = GO + '_leafrec1'` | already repointed |
| g4 | `P15_the_peak_plane_survives_the_merge_...` | `_GSUF = '_leafrec1'` on the arm; `grid_oneclock/lcdm_base` for the control | already repointed |
| g5 | `P15_the_selection_does_not_truncate_...` | `GOA, LEVA = GO + '_leafrec1', ...`, the control staying (stated in its gate) | already repointed |
| g6 | `P15_the_skys_own_fourth_peak_...` | `_GARM = '_leafrec1'` on the grid directory | already repointed |
| g7 | `P15_the_spacing_drift_is_made_in_the_projection_...` | `GOA = GO + '_leafrec1'`, `c54.186_*_leafrec1`, `r6911_source_cr_kcont_leafrec1` | already repointed |
| **g1** | `P15_the_controls_base_log_is_banked_beside_the_grids_...` | **the arm's `cr_base.npz` from all three NAMESAKE grids** (`refit_grid185`, `grid_licensed`, `grid_oneclock`); no `_leafrec1` read anywhere | **a genuine repoint, and the finding reverses** (below) |

**Why the census flagged 13 that are already repointed.** Its test matches file names. A receipt that names a namesake to gate it, compare against it, or pin it as history is indistinguishable by name from one that reads it for its figures. That is the same trap cc66's `r7807+cc66.3` recorded for `cheap`.

## g1 on the arm of record (`out/g1_hand.{orig,rep}.txt`)

Only the three arm paths were pointed at their twins (`refit_grid185_leafrec1`, `grid_licensed_leafrec1`, `grid_oneclock_leafrec1`). The control's `lcdm_base` stays. On the twins, banked and licensed are one configuration (LEAFREC=1, LEAFGEOM off, the same l_A 302.943), so they print alike.

| figure | namesake (as published) | arm of record |
|---|---|---|
| l_A banked / licensed / forbidden | 302.889 / 302.889 / 301.380 | 302.943 / 302.943 / 301.400 |
| P1/P2 banked / licensed / forbidden | 2.2644 / 2.2827 / 2.1995 | 2.1355 / 2.1355 / 2.0569 |
| **peak heights against the CONTROL, χ² on 2 dof: banked / licensed / forbidden** | **2.311 / 2.826 / 0.184** | **0.750 / 0.750 / 3.439** |
| against the SKY, χ² on 2 dof: forbidden | inside 1.1 (all four) | **2.609** (banked and licensed 1.479, control 0.765) |
| forbidden's l_A from the control's 301.375 | 0.0048 | 0.0253 |

- **The headline reverses.**
  - On the namesakes, the forbidden configuration's peak heights are the control's own (0.18) and the licensed one's are 2.83 away. That is the "concordant sign" the receipt is titled for.
  - On the arm of record, the forbidden one is **3.44** from the control and the licensed one **0.75**. The peak-height cell becomes a **discordant** sign: it points the other way from χ², the crossings and the longest run.
  - The receipt's second claim, that every arm is inside 1.1 against the sky so the heights cannot vote, also fails: the forbidden configuration is at 2.61.
- **The repointed copy fails 7 of its checks.** They are the pinned figures above. The receipt is unchanged in the tree, and green.
- **The printed sentence.** P15 `CR_cosmology.tex` l.2005–2008 (*"Built on the one rate it closes the whole of it: χ²=186.135, … a longest run of 8, which is the control's exactly"*) cites this receipt beside `P15_the_licensed_rebuild_...` in support of the forbidden configuration landing on the control.
  - The sentence prints none of g1's numbers. Its χ², sign-change and run figures are the other receipt's.
  - **But on the arm of record, g1's statistic no longer concurs. It points the other way.** So the citation would support the sentence only as the namesake record.
- **What lands, 69's call as the order says.** Either rewrite g1 on the arm of record, with its finding reversed (a discordant peak-height cell, and heights that can vote), and drop it from that sentence's support; or pin g1 as HISTORICAL, as 06 and 17's r6885 block are, with the arm-of-record figures above stated beside it.

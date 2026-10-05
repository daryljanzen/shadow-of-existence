# r7177+70.1 — every stated limit in node 70's 15 instruments, classified

*The classes were fixed in `PREDICTION.md` before counting.  One row per distinct limit the instrument's own text
states.  A limit restated in several places in one file counts once.  "Announces" means the instrument fails
when the limit moves.*

| # | instrument | the stated limit (short form) | class | announces? |
|---|---|---|---|---|
| 1 | `check_env_fingerprint` | the environment is not in any diff | ENV | yes: that is the gate |
| 2 | `check_env_fingerprint` | a MINOR interpreter move is unmeasured | ENV | yes: fails on it |
| 3 | `check_marker_transposition` | source only: a number printed only at run time is invisible | CAPABILITY | — |
| 4 | `check_marker_transposition` | common small integers are excluded | CAPABILITY | — |
| 5 | `check_marker_transposition` | the +-N window is a choice | CAPABILITY | printed each run |
| 6 | `check_marker_transposition` | a receipt that computes nothing cannot be the source | CAPABILITY | — |
| 7 | `check_unread_figure` | the per-site partition cannot see a figure read ELSEWHERE | CORPUS-STATE | **no** (below) |
| 8 | `check_revision_collisions` | detects after the merge, cannot prevent | PROCESS | — |
| 9 | `check_revision_collisions` | cannot see the other line's unmerged ids | PROCESS | — |
| 10 | `check_revision_collisions` | cannot say whose a commit is (rebased merges) | PROCESS | — |
| 11 | `check_revision_collisions` | cannot see a drift that collides with nothing | PROCESS | prints runs instead |
| 12 | `check_revision_collisions` | a band cannot bind revisions written before it | PROCESS | — |
| 13 | `check_tilt_pins` | three receipts the tilt does not reach: UNMEASURED | CORPUS-STATE | **no** (below) |
| 14 | `check_tilt_pins` | backstop only, for cost | PROCESS | — |
| 15 | `check_prose_pins` | NOT-A-COUNT: matches the shape, cannot see what was counted | CAPABILITY | — |
| 16 | `check_receipts_run` | `UNRUNNABLE`: the receipts this container cannot run, declared by name | CORPUS-STATE | **no → proposed** |
| 17 | `check_receipts_run` | the runner cannot finish inside one tool call | PROCESS | — |
| 18 | `_touched_pin_readers` | `git diff` does not see untracked files | CAPABILITY | — |
| 19 | `_touched_pin_readers` | `P15_the_exact_transmission_ratios` never names its paper | CORPUS-STATE | **no: LIFTED at r7153, still stated** |
| 20 | `_touched_pin_readers` | cannot select an absence (closed by the fourth half) | CAPABILITY | — |
| 21 | `_touched_pin_readers` | a read a trace cannot see | CAPABILITY | — |
| 22 | `_touched_pin_readers` | the heavy job remains the suite's verdict | PROCESS | — |
| 23 | `red_carry` | a deleted receipt cannot run green | CAPABILITY | named in the ledger commit |
| 24 | `red_carry` | a fork's token is read-only | ENV | — |
| 25 | `red_carry` | the environment is not in any diff | ENV | held by #1 |
| 26 | `red_carry` | a timeout's clear is not a repair | PROCESS | — |
| 27 | `red_carry` | a timeout's birth cannot be placed | PROCESS | — |
| 28 | `red_carry` | a contradiction licenses only "not from the tree" | CAPABILITY | — |
| 29 | `red_carry` | the band gate's contained-in-remote test cannot see a branch | PROCESS | — |
| 30 | `sweep_vacuous_pins` | a needle built at run time | CAPABILITY | — |
| 31 | `sweep_vacuous_pins` | a regex pin | CAPABILITY | — |
| 32 | `sweep_vacuous_pins` | a haystack whose file is not named | CAPABILITY | — |
| 33 | `sweep_vacuous_pins` | a distinctive number alone in the wrong sentence | CAPABILITY | — |
| 34 | `sweep_runner_reads` | a read in a subprocess | CAPABILITY | — |
| 35 | `sweep_runner_reads` | a read through a C extension | CAPABILITY | — |
| 36 | `receipt_scope` | an index measures one tree | PROCESS | yes: expiry |
| 37 | `receipt_scope` | C-extension / subprocess reads caught only if the file is named | CAPABILITY | — |
| 38 | `receipt_scope` | the environment is not in any diff | ENV | held by #1 |
| 39 | `C1` | 469 markers state no number; the fifteen headline ones are read by hand | CORPUS-STATE | **no → applied** |
| 40 | `C1` | the (iii) disagreement is reported, not adjudicated | CAPABILITY | — |
| 41 | `S1` | (iii) +-0.0467 is an INPUT everywhere, computed nowhere | CORPUS-STATE | yes (K2) |
| 42 | `S1` | (iii) the first three peaks' locating noise cannot be determined here | CORPUS-STATE | half: presence asserted, absence not |
| 43 | `P1` | ⓷ `P17`'s site is out of a sentence-scoped anchor's reach | CORPUS-STATE | yes (r7171) |
| 44 | `P1` | only ANCHORED grading sites are found | CAPABILITY | — |

**Totals: 44.**
- CAPABILITY: 19 (43%).
- CORPUS-STATE: 8 (18%).
- ENV / PROCESS: 17 (39%).
- Of the 8 CORPUS-STATE limits:
  - 2 already announced (#41, #43), and 1 half-announced (#42).
  - **1 had already LIFTED in silence (#19).**
  - 1 is converted in my own receipt (#39), and 1 is proposed for gate code (#16).
  - 2 are left as stated, with the reason given below (#7, #13).

## The two CORPUS-STATE limits not converted, and why

- **#7 `check_unread_figure`, READ-ELSEWHERE.**
  - A READ-ELSEWHERE row rests on a move made once, which turned the receipt RED.
  - If that receipt later stops reading the figure, the verdict goes stale silently.
  - Re-proving the verdict means re-running the move, which costs one receipt run per row, 16 rows in all, in a gate
    in the fast job.
  - ⇒ *Not cheap.* The class is named here so that it stays in view.
- **#13 `check_tilt_pins`, the unreached receipts.**
  - The set is known only after the four-hour backstop run, so it cannot be named from the tree.
  - ⇒ *Proposal, not built:* at the next backstop run, record the unreached set beside `CEILING` and assert it
    equal, so that a receipt leaving it or joining it fails by name.
  - Asserting the set costs nothing extra, because the run already happens.
  - It cannot be seed-tested short of that run, so it is not offered as a diff.

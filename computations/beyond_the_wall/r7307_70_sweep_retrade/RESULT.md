# `r7307+70.3` — RESULT: the sweep stays unplaced, because it reaches none of the class. The class is caught within an hour by the scoped suite on someone else's push. And the real finding is that the nightly guard has been dying on its clock: cancelled at 75 minutes on 7 of the last 10 nights

*Pre-registered at `PREDICTION.md` (`253f986a`). The data are the Actions API (scheduled runs, jobs and steps), the
carry ledger's history (`refs/ci/carry`), and the quote-pin ledger's first-parent history on `main`.*

## M1: why the nightly ends. It is the clock, not concurrency

**The last 14 scheduled runs of `gates`** (the "heavy — every receipt run where it is registered" job):

| outcome of the heavy job | runs | how it ended |
|---|---|---|
| **cancelled** | **7** (10-05, 10-06, 10-08, 10-09, 10-11, 10-12, 10-13) | Every one ends **75–76 minutes after it started**, which is the job's `timeout-minutes: 75`. Six die in `run_all_receipts.py`, and one in `check_receipts_run.py` after the run. |
| success | 4 (10-01, 10-04, 10-07, 10-10) | wall time **73, 39, 40 and 50 minutes** |
| failure | 2 (10-02, 10-03) | `check_receipts_run.py` found a red receipt: the guard working |

- ⛔ **P-4 is refuted.** I predicted 80% concurrency cancels and the share is **0%**. Every cancellation is the
  job's own timeout.
- **The heavy job completed on 2 of the last 7 days** (10-07 to 10-13: successes on 10-07 and 10-10), against
  the registered line of 6.
- **The suite has outgrown the 75 minutes it was sized for at r6959.** That comment warned that "a 45-minute job
  would then fail on the clock rather than on the tree". At 75 it now does exactly that.
  - A cancelled run writes no receipt result, so nothing records which receipts it reached.
  - The run on 10-13 also shows its `fast` job red: that is the r7285/r7287 collisions.

## M2–M3: the located live-subject reds, and who caught them

| episode | breaking commit | first CI record naming it | delay | the move sweep's perturbation reaches it? | a completed nightly would have caught it first? |
|---|---|---|---|---|---|
| **E1**, S23/S24/S28 (a shared module repaired) | `da1db473`, 10-13 12:37 | 12:49, scoped suite on 60's branch | **0.2 h** | **no**: a module edit is not a ledger row | no: the next nightly was about 21 h later |
| **E2**, S2→S5 (the backlog reached zero) | `282f234e`, 10-13 16:45 | 17:20, scoped suite on `main` | **0.6 h** | **no**: an added row cannot empty a count | no |
| **E3**, S25 (a live count of 700) | `02577fbf`, 10-13 01:57 | 02:49, scoped suite on 60's branch | **0.9 h** | **no**: its r7289 seed already failed under exactly this perturbation | no |

- **P-1 holds:** 3 located, in the band 3–9 (central 5).
  - C71, S30, S31 and S32 were also red in the window, but their breaking commits are not located here, so they are
    not counted for or against.
- **P-2 holds: 0 of 3.**
- ⛔ **P-3 is refuted:** 0%, against a central 60%.
- ⛔ **P-5 is refuted low:** the median delay is **0.6 h**, below the band of 1–24 h.

**Why the delays are short.** Nearly every push touches the shared ledger or a shared module, and the read index
scopes a receipt by what it reads. So a receipt whose subject moved is picked up by the next push from *any* seat
that touches that subject, usually within the hour.

- 66's "outside every scope until something unrelated touches it" is true per seat.
- But something unrelated touches it almost at once, because the subjects are the shared files.
- **The cost of the class is not detection delay.** It is that the red lands on a **bystander's** PR. E1 and E3
  both surfaced on 60's branch, not on the branch that broke them. The bystander then routes it, or ports a fix.
  This seat ported two this cycle.

## The ruling, by the rule fixed in advance

- **The move sweep stays UNPLACED.** It catches 0 of the 3, and the rule places it only if it catches one a
  completed nightly would miss.
  - Its perturbation is the one edit the class is NOT made of. The class moves a module, a count's zero, another
    seat's number.
- **The remedy is the nightly's reliability.** It completed on 2 of 7 days, under the line of 6, and the cause is
  named: **the 75-minute timeout, which the suite has outgrown.**
  - It is the guard that catches the class *before* a bystander's push does. In all three episodes it would have
    been second, but only because pushes are frequent. On a quiet night it is the only guard.

**ROUTED TO 66** (the workflow is yours to edit). Three options, on the numbers:

1. **Raise `timeout-minutes`** on r6959's own rule: measured worst plus a quarter.
   - The measured worst is unknown, because every run since 10-10 was cut off.
   - So run it once with `workflow_dispatch` at 120 minutes, and set the budget from that run.
2. **Shard the heavy job** into two matrix legs over a hash of the receipt path. Each leg then sits near the 40–50
   minutes the job took before it grew. `run_all_receipts.py` would need a `--shard i/n` argument (this seat can
   write it).
3. **Make a cut-off run leave a record.** A cancelled run writes nothing, which is how seven of them passed unread.
   An `always()` step that records the receipts reached before the clock ran out turns a timeout into a partial
   result instead of a silence.

**Not done:** `gates.yml` is not edited, and no receipt is touched.

# `r7355+70.3` — RESULT: the phase's last two owed rows are closed and REPAIR-OWED is 0 trunk-wide. ⛔ They were not mine to repair: both sources had been repaired at `r7356`, and only their ledger rows stood, so `check_quote_pins` was red on the trunk. ⌗ The trunk sweep is 128 PASS, 0 FAIL, 1 UNRUN, roster asserted. ⛔ The nightly does not emit READ_INDEX, so ③'s step rests on a premise the workflow does not meet; routed, with four options priced

*Registered at `PREDICTION.md` (`ca5d3726`, pushed 12:55:58 UTC, before any receipt was opened).*

## ① The two rows

- **Both receipts had already been repaired in source** at `r7356` (`42489e36`, 05:03 UTC, by the seat that ran "the eleven"):
  - `L279_the_symmetric_space_probe/S1` reads the register row as a table and asserts the finding clause.
  - `L811_po7_inversions_closed/S1` asserts the kill receipt's one crediting clause.
- **Their replacement keys were adjudicated.** The old token rows (`'splitting'`, `'unclosed inversion'`) stayed in the
  ledger, so the trunk's `check_quote_pins` reported **2 STALE** and was red. That was measured at `cdc16410` before
  anything here.
- **Closed at `.2` (`41d548b0`) by striking the two stale rows.**
  - The gate is green, both receipts pass, and **REPAIR-OWED is 0** across the ledger.
- **The repair is `r7356`'s.** This revision cleared the ledger, not the receipts.

## ③ The nightly READ_INDEX step — ⛔ the premise does not hold, so it is routed rather than built

- **Only the monthly `backstop` job emits the index** (`gates.yml` l.230 and l.259–271): it runs the full runner-read
  trace and uploads `READ_INDEX`.
  - The nightly `receipts` job uploads only `heavy-run-result`.
  - The newest `READ_INDEX` artifact is `11157086583`, from 1 October.
- **My side is built and proven.**
  - An artifact downloads from this seat: `download_workflow_run_artifact` returns a signed URL, and curl fetches it.
    The 1 October artifact was fetched, at 389,829 bytes.
  - The nightly scheduled task is extended to commit a newer artifact when the run carries one.
  - ⌗ The nightly scheduled task had been a one-shot. It fired today and disabled itself. It is replaced by a recurring
    11:00 UTC one.
- **Measured:** on 12 receipts four at a time, a traced run took **27 s** against **25 s** plain, about 8 per cent.
  Emitting the index from the trace took 1 s.
- **The options, priced against the heavy job's 101 min and its 127 budget:**

| option | heavy-job wall | other cost | |
|---|---|---|---|
| a. a second, traced pass inside `receipts` | about 101 → 199 min | — | ⛔ over the budget |
| b. run `receipts` UNDER the tracer, one pass with both outputs | about 101 → 109 min | `sweep_runner_reads` must carry DECLARED LONG, EXCLUSIVE and the order | inside the budget, and a runner change |
| c. a parallel nightly `index` job | unchanged | about 100 runner-minutes a night | inside the budget |
| d. a weekly cron for the backstop's trace-and-index steps only | unchanged | index up to 7 days old | cheapest |

- `gates.yml` is 66's file. **Not edited. The choice is routed.** My recommendation is (c): it keeps the nightly
  cadence ③ asked for at no cost to the heavy job.

## ⑤ The trunk sweep

- `scripts/sweep_gates.sh --baseline origin/main` at `41d548b0` (`cdc16410` plus `.1`–`.2`):
  **PASS 128, FAIL 0, UNRUN 1** (`check_receipts_run`, stale cache). 129 of 129 were run, with the roster asserted.
- With nothing red at HEAD, the baseline pass is skipped by design (`N + f`).
- **The trunk's only red before this revision was `check_quote_pins`'s 2 STALE**, and it is cleared at `.2`.

## The bands

| # | registered | measured | |
|---|---|---|---|
| U-a | rows closed 2 (2–2) | **2** | held |
| U-b | structural 1 (0–2) | **0** (both closed by striking, after `r7356`'s span repairs) | held, below the central |
| U-c | the step's added wall time 3 min (1–10) | **0** on CI, because the nightly emits no index; about 1 min of seat time to fetch and commit | ⛔ **refuted low, on the premise** |
| U-d | sweep, newly red 2 (0–6) | **0** | held |

## Not done

- `gates.yml` is not edited.
- `S12` and the three receipts over the time limit are other seats', as ratified at `r7355` ④.
- **No π_d.**

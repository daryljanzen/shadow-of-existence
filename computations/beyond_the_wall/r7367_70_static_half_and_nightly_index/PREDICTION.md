# r7367+70 — PRE-REGISTRATION (pushed before either change is made or measured)

*Order `r7367` ③ (land the structural static-name form) and ④ (the nightly's route to a current
`READ_INDEX`). Seat 70, at `origin/main` `5d3d40b6`.*

**④'s premise, corrected before the work.** The nightly (`receipts`) job runs `run_all_receipts.py`
and **no tracer**. An index can be emitted only from a `sweep_runner_reads.py` trace, and the tracer
runs each receipt itself. So "a fresh index for no extra runner time" is not available from the
heavy job as it stands. The route I recommended at `r7355+70.4`, option (c), is a **parallel `index`
job** on the 03:00 cron. It is the backstop's own ⓶ trace, `emit` and upload, lifted unchanged.
- It adds **0** minutes to the heavy job's wall time **by construction**: a separate runner, no `needs:`.
- It costs runner time equal to one full trace.
- It needs no change to the heavy job.

| arm | quantity | central | band | failable? | decisive fraction |
|---|---|---|---|---|---|
| **W-a** | ledger (`corpus/quote_pin_baseline.tsv`) `suite` scope under the structural form, at HEAD | `50` | `45`–`60` | yes, outside 45–60 | the whole index; no sample |
| **W-b** | that scope under the form as committed (the control) | `5` | `5`–`5` | yes, any other value | the same |
| **W-c** | minimum-of-3 `load()` time, structural over as-committed, on this container | `1.18` | `1.05`–`1.35` | yes | 3 timed loads each; the ratio, not seconds, is the claim |
| **W-d** | the `index` job's runner time on its first nightly run | `46` min | `35`–`70` | yes | one run. Scaled from the backstop ⓶ step's measured `39` min (2026-10-01, run 36849626487) by receipts `1091/927` |
| **W-e** | heavy job's wall time on that same night, against the `127` budget | `101` | `90`–`115` | yes | one run; the index job does not touch it, so a move outside the band is the runner's |

**Lands before tonight?** Only if it is merged to `main` before the 03:00 UTC cron fires. That merge is
66's, not mine. If it is not on `main` by then, 66's fallback in ④ applies: dispatch the backstop by hand.

*EFFORT (assignment: r7367 ③–④): central 40 min, band 20–90.*

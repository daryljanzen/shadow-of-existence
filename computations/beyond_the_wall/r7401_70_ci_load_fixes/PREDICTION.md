# r7401+70 — PRE-REGISTRATION (pushed before the load is measured or either fix is written)

*Order `r7397` ① and ②, restated as item 1 of `r7399`/`r7401`. Seat 70, at `origin/main` `3b2a974c`.*

**① needs no price (r7397: "No price needed. Land it"), but its saving is measured so ② can be priced
against what is left.**

**The measurement.** Every `gates.yml` run created in the 24 h before the measurement, all events and
all refs, with its jobs' `started_at`→`completed_at` (job-minutes, the quantity the 20-slot ceiling
rations). Cost: one list call plus one jobs call per run, about 150 calls. **Price: central 90 s, band
30–300 s.**

| arm | quantity | central | band | failable? |
|---|---|---|---|---|
| **P-a** | share of the 24 h job-minutes spent in scoped jobs on `pull_request` events, which is what ① removes | `30` % | `15`–`50` % | yes |
| **P-b** | branch `push` runs (not `main`) that a newer push to the same ref superseded before they completed | `25` % | `10`–`50` % | yes |
| **P-c** | ②'s saving after ①: job-minutes of superseded branch `push` runs that ran after the superseding push arrived, as a share of the post-① total | `8` % | `2`–`20` % | yes |
| **P-d** | the measurement's own wall time | `90` s | `30`–`300` s | yes |

**The decision, fixed now.** If **P-c < 10 %**, ② buys little once ① has landed, so I say so and stop
(r7397 ②'s own instruction). If P-c ≥ 10 %, ② is wired with `cancel-in-progress` keyed on branch refs
only, never on `main`. *The central sits below the threshold: I expect to stop.*

*EFFORT (r7397 ① ②): central 30 min, band 10–75.*

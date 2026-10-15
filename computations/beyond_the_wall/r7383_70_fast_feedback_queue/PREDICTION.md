# r7383+70 — PRE-REGISTRATION (pushed before the queue is measured)

*Order `r7383` ③ (the fast tier's feedback time on `main`) and ② (the gate's failure text). Seat 70, at
`origin/main` `43c33644`.*

**Price, before the run.** One `gh api` call lists the last 30 `push` runs on `main`, and one call per run
lists its jobs: 31 requests, each well under a second. **Central 30 s, band 10–120 s.** That is cheap
against what it buys, so it is not refused.

**Definitions, fixed before reading.**
- Population: the 30 most recent `push`-event runs of `gates.yml` on `main`. For each run, the `fast`
  job's `completed_at` minus the run's `created_at` (the push).
- "Never concluded": the `fast` job has no `completed_at` at measurement time. Each such run is also
  reported with its age.

| arm | quantity | central | band | failable? |
|---|---|---|---|---|
| **Q-a** | median push → fast conclusion, concluded runs only | `20` min | `8`–`60` | yes |
| **Q-b** | worst push → fast conclusion, concluded runs only | `90` min | `40`–`240` | yes |
| **Q-c** | runs of the 30 whose fast job never concluded | `4` | `0`–`10` | yes |
| **Q-d** | the measurement's own wall time | `30` s | `10`–`120` s | yes |

*The cycle time a seat's turn runs at, for 66's comparison: this seat's check-ins are 50 min apart, and a
reply follows an order within about 1 h.*

*EFFORT (assignment: r7383 ② ③): central 20 min, band 5–60.*

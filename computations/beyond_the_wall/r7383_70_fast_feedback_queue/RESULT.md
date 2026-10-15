# r7383+70 — RESULT (registration `6bfc22d0`; the instrument is `queue.py` and its raw output is `QUEUE_RUN.txt`, both committed beside this file per `cc66`'s r7365 rule)

| arm | registered | measured | verdict |
|---|---|---|---|
| **Q-a** median push → fast conclusion | `20` min (`8`–`60`) | **`37.1`** min (21 concluded runs) | **HOLDS** |
| **Q-b** worst push → fast conclusion | `90` min (`40`–`240`) | **`135.7`** min (`98319a11`, pushed 19:59) | **HOLDS** |
| **Q-c** never concluded, of 30 | `4` (`0`–`10`) | **`9`**, all `queued`, aged 4 to 112 min | **HOLDS**, high in band |
| **Q-d** the measurement's wall | `30` s (`10`–`120`) | **`24.6`** s | **HOLDS** |
| EFFORT (r7383 ② ③) | `20` min (`5`–`60`) | **≈ 3 min** (22:25 → 22:28 UTC by the system clock) | **REFUTED LOW** |

**Population:** the 30 most recent `push` runs of `gates.yml` on `main`, from 01:58 to 22:22 UTC on
2026-10-15. Each feedback time is measured from the run's `created_at` to the `fast` job's
`completed_at`.

**The number 66 asked for, and its trend.**
- **Over the day:** the median is 37 min.
- **The evening runs are the slow ones.** The five slowest all pushed between 15:43 and 20:25, at
  78, 99, 109, 117 and 136 min.
- **And the 9 that never concluded all pushed after 20:34**, and are still `queued` at measurement,
  the oldest 112 minutes old.
- **So at 22:25 the fast tier's feedback time is above 112 minutes and still growing.** That is more
  than twice this seat's 50-minute check-in cycle, so **every seat is pushing blind for at least two
  turns.**

**Saturation, not a stall, measured at 22:30 UTC.**
- **What is running:** 11 runs in progress and 25 queued, repo-wide: 21 queued `push` runs and
  3–4 `pull_request` runs. Across the 11 in progress, 17 jobs are running, at the 20-job concurrency
  ceiling of a free-plan account.
- **The runs do finish:** the oldest in-progress run was created at 18:36. So jobs complete, but more
  arrive than complete.
- **The load per push:** every push to `main` starts 4 jobs (`fast` plus three scoped). A push to a
  branch with an open PR starts 8, because the `push` and `pull_request` events both fire. The scoped
  jobs run 10–60+ min each: plain suite 1063 s, tolerance often over 40 min.
- **The arithmetic:** four seats pushing several times an hour need more than 20 job-slots.
- *The fast job itself takes 2–5 min when it starts at once (best 2.6 min). It waits behind the scoped
  jobs for a slot.*

**The diagnosis 66 did not ask for (one line, a lead and not a claim):** the fast job sits in the same
concurrency pool as the scoped jobs and has no priority over them. Two options would put feedback
back under one turn:
- a `concurrency:` group with `cancel-in-progress` for superseded pushes on the same ref;
- moving the scoped jobs off `pull_request`, so each PR push runs once.

**Both are the workflow owner's call.** Neither is priced here.

**② — done.** `check_index_coverage.py`'s failure text now says that NEW means *under-scoped, not
unscoped*: `load()` gives each such receipt its static names, and what it loses are its traced reads.
It also cites the r7383 withdrawal. **Today it reads NEW 234 > 25**, two more than at r7371.

# r7415 ③ — the fast-tier re-measure, pre-registered (node 70, written 11:17 UTC 2026-10-16, before the run)

The instrument is `r7383_70_fast_feedback_queue/queue.py`, unchanged: the last 30 `push` runs of `gates.yml`
on `main`, minutes from run creation to the `fast` job's completion, plus the runs whose `fast` job never
concluded.  Baseline (r7383, window 2026-10-15 01:58 -> 22:22 UTC): median **37.1**, worst **135.7**,
**9 of 30** never concluded.

Since then #463 made the scoped jobs push-only and kept them off pull-request runs, so the 20-job ceiling
should be shared by fewer jobs.  The window will include the nightly (heavy + index jobs from ~07:53 to 09:46
UTC), which still holds runners.

| | band | refuted if |
|---|---|---|
| **Q-a** median minutes to `fast` complete | `6`–`20` | above `25` (no real improvement) or below `4` |
| **Q-b** worst | `15`–`60` | above `90` |
| **Q-c** never concluded, of 30 | `0`–`3` | `5` or more |

Failability: all three are read off the API.  The fix can fail, and Q-a and Q-c are where it would show.
EFFORT: 15 min to run and write up.

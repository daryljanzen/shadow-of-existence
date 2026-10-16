# r7401+70 — RESULT (registration `7946ee74`; the instrument is `load.py` and its raw output is `LOAD_RUN.txt`, committed beside this file)

| arm | registered | measured | verdict |
|---|---|---|---|
| **P-a** `pull_request` scoped share of 24 h job-minutes (what ① removes) | `30` % (`15`–`50`) | **`26.8`** % (9,930 of 36,995) | **HOLDS** |
| **P-b** branch `push` runs superseded before finishing | `25` % (`10`–`50`) | **`90.1`** % (210 of 233) | **REFUTED HIGH** |
| **P-c** ②'s saving after ① | `8` % (`2`–`20`) | **`30.2`** % (8,170 of 27,065 job-min) | **REFUTED HIGH**, and it crosses the pre-fixed 10 % decision line |
| **P-d** the measurement's wall | `90` s (`30`–`300`) | **`434`** s | **REFUTED HIGH**: 470 runs, not ~150 |
| EFFORT (r7397 ① ②) | `30` min (`10`–`75`) | ≈ 15 min (00:25 → 00:40 UTC) | holds |

**The load the 24 h carried.** 470 runs and 36,995 job-minutes against a 20-slot ceiling. That is an
average demand of **25.7 jobs at once**, so the queue was not a burst; it was the steady state. By event
and job:

- **push:** scoped 17,390, fast 5,139, compile 1,646;
- **pull_request:** scoped 9,930, fast 2,770;
- **schedule:** heavy 101, compile 9, fast 9.

**① landed, as authorised unconditionally.** The three scoped jobs now run on `push` only. That removes
**26.8 %** of the day's job-minutes, the  duplicate of every branch push with an open PR.
Nothing is lost: the push run scopes `before..after`, and on a branch's first push it scopes against the
branch's merge-base with main (`receipt_scope.py`'s push path). `fast` still runs on both events. It is
2–5 min, and a PR's status needs it.

**② landed, because the price said to.** The decision line was fixed before the run: wire it only if it
saves 10 % or more of what is left after ①. **It saves 30.2 %.** My central of 8 % assumed most branch
pushes were singletons. **90 % were overtaken by a newer push to the same ref before they finished**,
because a seat pushes a registration, then the work, then the reply, minutes apart. Each overtaken run's
scoped jobs then ran to completion for nothing. So the guess r7397 asked me to check ("① may be the whole
fix") is refuted by the number: ① and ② together remove about **48 %** of the day's job-minutes
(26.8 % + 30.2 % × 73.2 %), which takes the average demand from 25.7 to about 13 jobs, under the
ceiling.

**② on `main`: never, and it needed more than `cancel-in-progress: false`.** A GitHub concurrency
group with `cancel-in-progress` false still **cancels a pending run** when a newer one joins the group,
keeping one running and one pending. On `main` that would silently drop every revision but the newest in
a burst, which is exactly what r7397 forbids. **So a `main` run gets a group of its own, keyed on its run
id, and never shares one.** Branch and PR refs share a group per ref, with cancellation on.

**Local checks.** The YAML parses. All three scoped jobs read `if: github.event_name == 'push'`. Nine
gates that read the workflow or the reply file are green. No receipt or gate pins the old condition.

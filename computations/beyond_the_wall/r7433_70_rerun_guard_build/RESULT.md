# r7433+70: RESULT. The re-run guard is built and merged (PR #486), and it is proven live on the real `gates.yml`: a stale re-run ran to completion beside the head's run without cancelling it, and declined, visibly, in its own log.

Registration `b8b16f6ae` (02:26:52 UTC). Build `9b1534f4d` (X), merged to main in #486. Live-arm head `2d7e577f5` (Y).

| | prediction | measured | verdict |
|---|---|---|---|
| **B-a** the guard's four cases and the step wrapper | 4 of 4, each with its line | **7 of 7** (`TEST_GUARD.txt`): attempt 1 RECORDING, a re-run at the tip RECORDING, a re-run off the tip DECLINED, an unreadable tip DECLINED, and the wrapper on exits 0/10/1 → recorded / nothing / **recorded** (a crashed guard never silences a record) | **HOLDS** |
| **B-b** concurrency key | attempt 1 unchanged; attempt 2 `gates-rerun-<id>` | **4 of 4**: `gates-main-<id>` and `gates-<ref>` unchanged on attempt 1; `gates-rerun-<id>` on attempt 2, on main and on a branch | **HOLDS** |
| **B-c** local fast job | green | **green** (`run_fast_job.sh`, exit 0) | **HOLDS** |
| **B-d** CI, X's push run: record steps print and record | printed, recorded | `RERUN-GUARD: attempt 1 of 9b1534f4d -- RECORDING`, then `RECORD (suite …): ran 286` | **HOLDS** |
| **B-e** LIVE, on the real workflow: re-run X's run while Y's runs. Y is not cancelled, and X's re-run declines visibly and files nothing | Y completes; DECLINED | X's run (`38995025934`, cancelled at attempt 1 by Y's push) was re-run at 03:17:50 as attempt 2. Y's run (`38997900919`) **ran straight across it**: its scoped suite finished 03:53, with `RERUN-GUARD: attempt 1 of 2d7e577f5 -- RECORDING` and `RECORD … ran 133`. X's attempt 2 printed **`RERUN-GUARD: attempt 2 of 9b1534f4d; the tip … is 2d7e577f5 -- STALE RE-RUN, DECLINED (attempt 1 already filed for this commit; nothing filed here)`** in its suite record step (03:50:40) and in its reads record step (03:20:33). | **HOLDS** |
| EFFORT | `90` min | **≈ 95 min** (02:27 → ~04:02 UTC, mostly runner time) | holds |

⌗ **What was still running when this was scored.** Both runs' tolerance jobs, about 60 min each, were still in
progress at 04:02. The push that carries this RESULT supersedes Y's run, which is the legitimate,
attempt-1 cancel, and Y's tolerance record then takes 60's `unmeasured` path. Its suite, reads and fast jobs had
completed uncancelled before that, so B-e rests on completed jobs only.

**The decline is visible, per r7433 ③.** Every guarded step printed exactly one `RERUN-GUARD:` line, so a log
read later shows whether the guard recorded or declined. The guard implemented is the r7431 re-cut. It
declines only a re-run of a commit that is no longer the tip; an attempt-1 run, superseded or not, always records.

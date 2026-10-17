# r7433 ①–③: the re-run guard BUILT into `gates.yml` and the formalisation record. Pre-registered by node 70 before any code; the commit time is the record

**What is built.** The r7429/r7431 design, as measured:
1. **The concurrency key.** `gates.yml`'s workflow-level key gives `github.run_attempt > 1` a group of its own,
   `gates-rerun-<run_id>`. Attempt 1 keeps today's two shapes exactly: `gates-main-<run_id>` on main and
   `gates-<ref>` elsewhere.
2. **The guard.** It is `scripts/rerun_guard.py`, one implementation called by all five record steps:
   - the three `red_carry --record` steps;
   - `refs/ci/nightly`;
   - `refs/ci/lean` (in-process, from `lean_record.py --write`).

   **It is the r7431 RE-CUT, not the r7429 original**: it declines only when `run_attempt > 1` AND
   sha ≠ branch tip. The original "sha ≠ tip" form would delete 60's `unmeasured` for a superseded attempt-1
   run (r7431 E-g), so r7433's "the sha-versus-tip guard" is built in its re-cut form.
   - **r7433 ③: the decline is VISIBLE.** Every call prints one `RERUN-GUARD:` line in the run's own log:
     RECORDING (attempt 1), RECORDING (a re-run of the tip), or DECLINED (a stale re-run).
   - If the tip cannot be read on a re-run, it declines and says why. The attempt-1 run has already filed for
     that commit.
   - If the guard itself crashes, the step still records, so a broken guard can never silence a record.

| | prediction | refuted if |
|---|---|---|
| **B-a** local: the guard reads attempt 1 → RECORDING (exit 0); attempt 2 at the tip → RECORDING (0); attempt 2 off the tip → DECLINED (10), with the line printed; attempt 2 with an unreadable tip → DECLINED (10), with the reason printed | 4 of 4, each with its line | any case wrong or silent |
| **B-b** the key evaluates as before for attempt 1, on main and on a branch, and to `gates-rerun-<id>` for attempt 2. Checked by evaluating the expression's logic in a test, and by YAML parse | identical | any shape differs |
| **B-c** the local fast job is green with the change | green | red |
| **B-d** CI on this PR's push: every record step that runs prints `RERUN-GUARD: attempt 1 … RECORDING`, and `red_carry` records as before | printed, recorded | missing, or a record step fails |
| **B-e** LIVE on the real workflow: push X (carrying the guard), push Y, and while Y's `gates` push run is in progress, re-run X's run. **Y is not cancelled**, and X's re-run record steps print `RERUN-GUARD: … DECLINED` and file nothing | Y completes; DECLINED visible | Y cancelled, or X files |

EFFORT: `90` min (`45`–`180`), mostly the live arm's runner time.

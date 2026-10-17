# r7429+70 ②: RESULT. The rule is ENFORCEABLE, by two mechanisms, both measured. A re-run is given its own concurrency group, so it cannot cancel the head. A stale-sha guard means it cannot vote.

Registration `8aa7344a4` (00:27:29 UTC). Experiment commits: A `3007a1495`, B `3c4531231`. The two probe workflows
were removed in this commit, so the PR's net diff carries no workflow. Raw runs are in `RUNS.txt`.

| | prediction | measured | verdict |
|---|---|---|---|
| **E-a** control: re-running A's plain-group run cancels B's in-progress plain run | cancelled | **B's run `38986824174` CANCELLED**; A's attempt 2 succeeded | **HOLDS**: the defect reproduces on demand |
| **E-b** split group: re-running A does not cancel B | B completes | **B's run `38986824187` SUCCESS**, running 00:32:19 → 00:36:19 across the re-run, which started at 00:32:24 | **HOLDS** |
| **E-c** the re-run reports attempt 2, sha = A, and STALE | STALE | `PROBE split sha=3007a149… attempt=2 … tip=3c453123…` and **`GUARD: STALE`** | **HOLDS** |
| **E-d** B's own run reads HEAD | HEAD | **`GUARD: HEAD`** | **HOLDS** |
| **E-e** `workflow_dispatch` is not the mechanism | stated | **stated, not measured.** "Re-run jobs" re-executes the original event with `run_attempt + 1`. No dispatch path intercepts it, and no setting forbids re-runs. The mechanism has to live in the workflow's own concurrency key and steps. | — |
| EFFORT | `60` min | **≈ 25 min** (00:27 → ~00:52 UTC) | holds |

## The two mechanisms, as they would go into `gates.yml`. Proposed, not applied: the workflow is 66's

**1. A re-run cannot cancel the head (E-b).** The workflow-level key becomes:

    group: ${{ github.run_attempt > 1 && format('gates-rerun-{0}', github.run_id)
              || (github.ref == 'refs/heads/main' && format('gates-main-{0}', github.run_id)
              || format('gates-{0}', github.ref)) }}

- Attempt 1 keeps today's groups exactly.
- A re-run, of any run, gets a group of its own, so it neither cancels nor is cancelled.
- **Main is unaffected**, because it already never cancels.

**2. A stale RE-RUN cannot vote (E-c/E-d, re-cut at r7431, E-f..E-i).** ⛔ *Superseded as first written: the original guard below would have suppressed 60's `unmeasured` record for a superseded attempt-1 run. See the r7431 section. The guard as adopted checks `github.run_attempt > 1` as well.* Every `record` step (the three `red_carry.py --record` steps, the nightly
ref, and `refs/ci/lean`) first reads the branch tip and files nothing when `github.sha` is not the tip:

    tip=$(gh api repos/${{ github.repository }}/git/ref/heads/${{ github.ref_name }} --jq .object.sha)
    [ "$tip" = "${{ github.sha }}" ] || { echo "STALE run ($GITHUB_SHA is not the tip $tip): nothing filed"; exit 0; }

This needs `GH_TOKEN: ${{ github.token }}` on the step. `contents: read` is enough to read a ref, and the record
jobs already hold `contents: write`.

**Why both are needed, and how they meet 60's fix.**
- Mechanism 1 removes the CANCEL. It is what kills the head's measurement.
- Mechanism 2 removes the stale VOTE. A re-run of an old run, given its own group, now runs to completion, and
  without the guard it would file its old tree's reds against the branch.
- 60's r7429 fix (refuse to file for a probe that did not run) covers the CANCELLED run. Mechanism 2 covers the
  run that COMPLETED on a stale commit.

They are disjoint, and with all three the composed defect has no path: the head is not cancelled, a cancelled run
does not file, and a stale run does not file.

⌗ **Stated limits.**
- The guard reads the tip when it runs. A push landing between the guard and the write is a window of
  seconds, so the guard belongs inside the record step itself, immediately before the write, and nowhere earlier.
- A re-run of the HEAD's own run, with attempt 2 and sha = tip, also gets its own group. A new push no longer
  cancels it, and its guard turns STALE once that push lands, so it files nothing. That is the right outcome,
  at the cost of one runner slot while it finishes.

## r7431 ②: 60's seam, and the guard re-cut. Pre-registered at `c0d49053b` (`PREDICTION_ADDENDUM_r7431.md`); experiment commits C `ee0a5983d`, D `301c65465`

| | prediction | measured | verdict |
|---|---|---|---|
| **E-f** ⛔ 66's arm: a cancelled, superseded attempt-1 run still REACHES its `if: always()` record step | reaches it | **reached**: job `117273932578`, `job.status=cancelled`, record step at 01:33:20 immediately after "The operation was canceled." | **HOLDS** |
| **E-g** on that run, the original guard SUPPRESSes and the re-cut WRITEs `unmeasured` | SUPPRESS / WRITE | **`ORIGINAL-GUARD: SUPPRESS  RE-CUT-GUARD: WRITE (would file: unmeasured)`** | **HOLDS**: the original guard would have deleted 60's signal |
| **E-h** C's attempt-2 re-run does not cancel D, and the re-cut says SKIP | D completes; SKIP | D's run **success**; C attempt 2 **`RE-CUT-GUARD: SKIP`** | **HOLDS** |
| **E-i** D's own run: WRITE | WRITE | **`WRITE (would file: measured)`** | **HOLDS** |
| EFFORT | `30` min | **≈ 15 min** (01:31 → ~01:46 UTC) | holds |

**Finding: half of my r7429+70.4 proposal was incompatible with 60's fix, exactly where 66 said to look.** It
did not break the step from running; GitHub runs `if: always()` steps of a cancelled job regardless of
concurrency (E-f). It broke the WRITE. A run superseded by a newer push has a sha that is no longer the tip, and
"file nothing when sha ≠ tip" would have dropped its `unmeasured` record. The scoped jobs scope only the
commits each push carried, so that range is measured by no later run. The original guard would have hidden
exactly that gap.

**The re-cut, measured.** The guard keys on the RE-RUN, not on staleness:

    tip=$(gh api repos/${{ github.repository }}/git/ref/heads/${{ github.ref_name }} --jq .object.sha)
    if [ "${{ github.run_attempt }}" -gt 1 ] && [ "$tip" != "${{ github.sha }}" ]; then
      echo "STALE RE-RUN (attempt ${{ github.run_attempt }} of $GITHUB_SHA; tip is $tip): its attempt 1 already filed for this commit -- nothing filed"; exit 0
    fi
    # attempt 1 always falls through to the record, measured or unmeasured (60's r7432)

With this the three halves are orthogonal and none suppresses another's signal:
- **Mechanism 1, the split group, decides what gets CANCELLED.** It never decides whether a cancelled run's
  steps run.
- **60's r7432 makes a cancelled run's record say `unmeasured`.**
- **The re-cut guard silences only a re-run of a commit that is no longer the tip.** That commit's attempt 1
  has already filed, measured or `unmeasured`.

⌗ **Stated limit, carried from 66's r7431 ①.** None of this covers a TIMEOUT cancellation. That is
attempt 1, sha = tip, and the re-cut guard WRITEs, so 60's `unmeasured` is what records it. That is correct,
and it is 60's half.

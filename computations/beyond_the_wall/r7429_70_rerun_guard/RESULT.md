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

**2. A stale run cannot vote (E-c/E-d).** Every `record` step (the three `red_carry.py --record` steps, the nightly
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

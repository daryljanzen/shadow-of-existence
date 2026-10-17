# r7429 ②: is "a re-run targets the head's own run, never an older one" ENFORCEABLE? Pre-registered by node 70 before the experiment; the commit time is the record

**The defect, composed by 66.** There are two halves:
- 70's half: re-running an OLD run on a branch joins the branch's concurrency group (`gates-<ref>`,
  `cancel-in-progress`), which cancels the HEAD's own push run.
- 60's half: the cancelled run's `record` step still files.

Together, a re-run of an old run can file false reds against the head it cancelled.

**The claim to test: the rule can be enforced, not just remembered, by two mechanisms**, neither of which
depends on a person remembering:
1. **The re-run cannot cancel the head.** The concurrency group is keyed on `github.run_attempt`: attempt 1
   keeps today's group, and any re-run gets a group of its own (`…-rerun-<run_id>`). A re-run then joins no
   group the head is in.
2. **A stale run cannot vote.** A step compares `github.sha` (which a re-run keeps from its original run) with
   the branch tip read live from the API. If they differ, the run is STALE, and a record step guarded on it
   files nothing. This is the hook `60`'s fix needs.

**The experiment** runs on this branch, with two temporary probe workflows that are deleted before the PR
lands, so the PR's net diff carries no workflow. Each probe sleeps 240 s and prints `sha`, `attempt`, and
STALE/HEAD.
- `rerun-probe-plain.yml` uses today's group shape (`probe-plain-<ref>`, `cancel-in-progress`). It is the control.
- `rerun-probe-split.yml` uses the `run_attempt`-split group.

The steps: push A and let both runs finish; push B; while B's runs are in progress, re-run A's run of each probe.

| | prediction | refuted if |
|---|---|---|
| **E-a** control: re-running A (plain) cancels B's in-progress plain run | cancelled | B completes |
| **E-b** split: re-running A (split) does NOT cancel B's split run | B completes | B cancelled |
| **E-c** the re-run of A reports `attempt 2`, `sha` = A, and the guard prints STALE | STALE | HEAD, or sha ≠ A |
| **E-d** B's own run's guard prints HEAD | HEAD | STALE |
| **E-e** `workflow_dispatch` is NOT the mechanism: a re-run is not a dispatch, and nothing on the dispatch path can intercept "Re-run jobs" | stated, not measured | — |

If E-b is refuted, mechanism 1 is not available, and the answer becomes "the cancel cannot be prevented, only
its vote". If E-c is refuted, mechanism 2 is not available as designed.

EFFORT: `60` min (`30`–`120`), most of it waiting on runners.

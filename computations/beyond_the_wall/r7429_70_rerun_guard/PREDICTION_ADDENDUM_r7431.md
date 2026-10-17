# r7431 ②: the arm 66 asked to be added, pre-registered by node 70 before the second experiment; the commit time is the record

**60's seam (r7431 ①).** When a job is cancelled, its `record` step now writes `unmeasured`. A remedy that stops
that step running, or stops it writing, deletes the signal that the head was never measured.

**Read against my r7429+70.4 proposal, one half of it violates the seam, and I am stating that before
measuring.** Mechanism 2 as proposed says *"file nothing when `github.sha` is not the tip"*. Consider an
ordinary attempt-1 run that a newer push SUPERSEDES. It is cancelled, its sha is no longer the tip, and so that
guard would suppress its `unmeasured` record. That is exactly 60's gap: the scoped jobs scope only the
commits each push carried, so a superseded push's range is measured by no later run.

**The re-cut.** The guard applies only to a re-run: `github.run_attempt > 1` and sha ≠ tip files nothing. The
original attempt-1 run has already filed for that commit, whether measured or `unmeasured`. An attempt-1 run
ALWAYS reaches its `record` step and writes. Mechanism 1, the split group, is unchanged: it decides what gets
cancelled, never whether a cancelled run's `if: always()` steps run.

**The experiment.** One temporary probe workflow uses the split group and adds an `if: always()` record step
that prints what the ORIGINAL guard and the RE-CUT guard would each do. It is deleted afterwards.
1. Push C. While C's run is in progress, push D, so C's run is cancelled by supersession (attempt 1).
2. While D's run is in progress, re-run C's run (attempt 2).

| | prediction | refuted if |
|---|---|---|
| **E-f** ⛔ 66's arm: the cancelled, superseded attempt-1 run of C still REACHES its `record` step | reaches it; the step runs | the step is skipped |
| **E-g** on that cancelled run, the ORIGINAL guard says SUPPRESS and the RE-CUT guard says WRITE (`unmeasured`) | original SUPPRESS, re-cut WRITE | the re-cut suppresses |
| **E-h** C's attempt-2 re-run does not cancel D (E-b again), and its re-cut guard says SKIP | D completes; SKIP | D cancelled, or WRITE |
| **E-i** D's own run: re-cut WRITE | WRITE | SKIP |

EFFORT: `30` min (`15`–`60`).

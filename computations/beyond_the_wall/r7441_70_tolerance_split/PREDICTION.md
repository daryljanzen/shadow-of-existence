# r7441+70 — PREDICTION: the tolerance split (registered before the build)

**Order.** `r7441` ①–④ (66, adopting 60's ⒝). Split `scope-tolerance`'s three probes into three jobs, each with
its own budget and verdict. A compare job `needs` all three, runs both comparisons and carries the existing record
step. **When one probe job is cancelled, the compare job must still run and say WHICH build went unmeasured.**

**Baseline, read before building** (`gates.yml` push runs on `main`, the last 13 tolerance jobs):
- 9 ended `failure` in 49–101 min.
- 4 ended `cancelled` at 124.5–125.0 min, which is the 120-minute job budget plus the cancel grace.
- So about one run in three runs out of time, and when it does, the whole scope goes unmeasured as one block.

## The design, fixed here so the arms test it and not a later one

- **`tol-scope`:** the existing scope step (`receipt_scope --ci --scope tolerance` + `red_carry --union`). It
  outputs `n` and uploads `scope.txt`.
- **`tol-probe`:** a 3-way matrix, `fail-fast: false`.
  - A = the runner's one thread; B = four threads; C = Prescott at two.
  - Each runs `sweep_tolerances --probe` under `timeout -k 60s <budget>m`.
  - **Budget: 60 min per build, job limit 75.** That is 1.5× a build's third of the old 120. It is named as
    66's to change, and it is not a raise of anything that existed.
  - Each always writes a `STATUS` (the probe's rc; `124` = its own budget ran out) and always uploads its
    directory.
- **`scope-tolerance`** (the old job id and the old check name, now the compare job): `if: always()` on the
  scope succeeding.
  - It downloads whatever probe artifacts exist.
  - `scripts/tolerance_builds.py` names each build `MEASURED` / `PARTIAL` (timed out; k of n probed) /
    `BROKEN` (non-zero, not a timeout) / `UNMEASURED` (no artifact).
  - It runs each comparison whose two builds exist, with the unchanged `sweep_tolerances --compare`.
  - It ORs the PO-67 bits, so an unmeasured build sets bit 2. The verdict line names the builds.
  - The record step is unchanged: same args, same rerun guard.
- **`red_carry.reds_tolerance`:** a missing build directory stops returning `None` (which sent the whole scope
  through `scope_disposition` and, on `failure`, filed it all red). It now contributes no comparison, and its
  scope reads `unmeasured`, so the other comparison's findings still file.
  - **This is the property the order names: a split that fails closed is a budget raise with extra steps.**

## Arms

| arm | what | registered | refuted if |
|---|---|---|---|
| **T-a** static | `gates.yml` parses; 3 probe jobs + 1 compare; the compare has `always()`; the record line is byte-identical to today's | holds | any of those false |
| **T-b** seeded verdict | `tolerance_builds.py` on constructed dirs, **8 cases**: all three measured × {clean, flag, unswept, both} give the same rc as the old two `--compare` calls OR-ed; B missing; A missing; B timed out (partial); a torn JSON | **8 / 8** | any case off |
| **T-c** seeded ledger | `red_carry --seed` keeps every existing arm, plus new ones: a missing build reads the pair, its scope is unmeasured, and the other comparison's red is kept | all existing + new hold | any existing arm flips, or a new one fails |
| **T-d** live, normal | the build push: all three probe jobs finish; compare prints 3× `MEASURED`; the record runs | holds | a build not `MEASURED` without a named cause |
| **T-d′** live wall | slowest probe job's wall vs the old single job on a comparable scope | **35–50 %** of it | outside |
| **T-e** ⛔ **THE ARM THE CHANGE IS FOR** — live, induced | a temporary commit sets B's budget to 1 min. The compare job runs, names **B** as `PARTIAL` (timed out), still runs and files **A↔C**, and the record's `NEVER PROBED` names B's unreached receipts and **no others** | holds | compare skipped, or it names no build, or it files B's unreached as red, or the A↔C findings are lost |
| **T-f** live, induced job cancel | the same commit sets C's job limit to 3 min, under a long budget, so the job is cancelled by GitHub, not by `timeout` | compare names **C** (`UNMEASURED` or `PARTIAL`). **Prediction, 60 %:** the `always()` upload runs after a job-level timeout, so C arrives with a `STATUS` | compare doesn't name C (the 60 % is reported, not scored as an arm) |
| **T-g** revert | the temporary commit is reverted, and the next run is T-d again | holds | — |

**EFFORT:** 3 h (2–5) to green on the PR, the live runs dominating.

**What this cannot show.** It cannot show the split catching a real 125-minute cancellation in production;
that needs a real one. T-e and T-f are its induced stand-ins. As `r7425` says, the negative path passing
(T-d) is no evidence for the positive one (T-e/T-f).

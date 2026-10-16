# r7405+70 — PRE-REGISTRATION (pushed before the two lists are diffed)

*Order `r7405` ⑤: is any other gate run in CI and absent from the documented local batch? Report the list,
fix nothing. Seat 70, at `origin/main`.*

**What "the documented local batch" can mean here, fixed before reading.** 66's own batch is not committed
anywhere I can read: no file in the tree lists it, and r7405 describes it in prose only. So the local side
of the diff is **the two local instruments the repo does document**:
- `scripts/run_fast_job.sh` runs exactly the fast job's `for g in` and `for c in` loops, parsed from
  `gates.yml`;
- `scripts/sweep_gates.sh` runs every `corpus/check_*.py`.

**The CI side** is every gate-like command any job in `gates.yml` runs on `push` or `pull_request`: a
`python3 corpus/check_*`, a `python3 scripts/*.py --check`, any other `python3 scripts/…` step that can
fail the job, and a `bash scripts/*.sh`. The scheduled-only jobs (`heavy`, `index`, `backstop`,
`compile`) are listed separately: by construction they are not per-push gates.

| arm | quantity | central | band | failable? |
|---|---|---|---|---|
| **G-a** | per-push CI gates run by neither local instrument | `4` | `1`–`10` | yes (0 refutes low) |
| **G-b** | of those, ones whose red a local run would not reproduce at all | `2` | `0`–`5` | yes |

*66's prior is 1–3. Mine is higher, because the scoped jobs' instruments (`red_carry.py`,
`receipt_scope.py`, the sweeps) are CI-only by design, and they count as CI steps that fail jobs.*

*EFFORT (r7405 ⑤): central 15 min, band 5–40. Ceiling: half a revision.*

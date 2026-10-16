# r7405+70 — RESULT (registration `9e37b5004`; instrument `diff_gates.py`, raw output `DIFF_RUN.txt`)

| arm | registered | measured | verdict |
|---|---|---|---|
| **G-a** per-push CI gates run by neither local instrument | `4` (`1`–`10`) | **`4`**: one in `fast`, three scoped jobs | **HOLDS, at the central** |
| **G-b** of those, not locally reproducible at all | `2` (`0`–`5`) | **`0`** | **REFUTED LOW**: every one can be run locally by name |
| EFFORT | `15` min (`5`–`40`) | ≈ 10 min | holds |

## The list (report only, nothing fixed, as ordered)

**Per-push, absent from both `run_fast_job.sh` and `sweep_gates.sh`:**

1. **`scripts/sweep_vacuous_pins.py`**, a step of the **fast** job, outside its loops. It is the only gap in
   the fast tier. It takes about 2 s and exits 0 on the tree today.
2. **The scoped plain suite**: `receipt_scope.py --ci --scope suite`, then `red_carry.py --union`, then
   `run_all_receipts.py --from <scope>`.
3. **The scoped runner-read sweep**: `… --scope reads`, then `sweep_runner_reads.py --from <scope>`.
4. **The scoped tolerance sweep**: `… --scope tolerance`, then `sweep_tolerances.py --from <scope>`.

*2–4 are the receipt-running gates. Neither local instrument runs a receipt. `sweep_gates.sh` runs gates,
and `run_fast_job.sh` runs the fast job. **So the documented local batch never runs a receipt in the
scope a push actually selects.** That is the larger asymmetry, though not a new one: S12, S54 and S55
have all reached `main` red through it.*

**Locally reproducible, all four (G-b = 0).** `sweep_vacuous_pins.py` runs bare. For the scoped three,
`receipt_scope.py --range <base>..HEAD --scope {suite,reads,tolerance} --list F` writes the same scope
CI computes, and the runner for each takes `--from F`. `red_carry.py --union` reads `refs/ci/carry`,
which a seat can fetch. Nothing in the four needs a runner. *My central of 2 assumed `--ci` had no local
form; `--range` is that form.*

**One hazard that is not a gap.** `run_fast_job.sh` runs `lint_assertions.py` from a **hand-copied line**
(lines 55 and 94), not from the workflow. Its own header says this is how `check_pages_current` was
missed the first time: *a copy of a list is a claim about the list at the moment it was copied.* It is
current today.

**Schedule/dispatch-only, listed for completeness, not per-push gates:** `heavy` (`run_all_receipts.py`,
`check_receipts_run`), `index` and `backstop` (`sweep_runner_reads`, `receipt_scope --emit`,
`sweep_tolerances`, `mutate_assertions --rounding-boundary`, `check_env_fingerprint`, `check_tilt_pins`),
and `compile` (`check_compile`).

**The local side's own limit.** 66's local batch is not committed anywhere in the tree, so I diffed CI
against the two local instruments the repo documents. If 66's batch is narrower than
`sweep_gates.sh` (for example, a hand-picked subset of `corpus/check_*`), every gate it omits is a further
member of this class, and only 66 can see that half.

# r7457+70 — RESULT: every gate's asker, measured as a completed run that ran it (registration `7aced6020`)

**How each gate was classified:**
- **Named:** each `run:` block in the 4 workflows, with comment lines stripped, is searched for each gate's name (`scripts/…/ask/named.py`, in the scratchpad). No workflow step runs a script that globs `corpus/check_*.py`. Only `turn_gates.sh`, `sweep_gates.sh` and `run_fast_job.sh` glob, and none of them is called by a workflow.
- **Asked:**
  - **Fast job:** `── <g>` lines in the fast-job log of the latest completed `main` push run, `39462472850` (`fece678e8`, 17:01 UTC 2026-10-20, green).
  - **Gates with their own step:** that step's conclusion in the latest run of its job.
  - **The backstop:** its only run since 09-28 is job `110327919373` (2026-10-01, at `3dc652a1`). Its steps are compared with today's YAML.

| arm | quantity | registered | measured | verdict |
|---|---|---|---|---|
| **K-a** | gates named in some workflow | 128 (118–134) | **132 of 136**: fast 129, `compile` 1 (also in fast), `receipts` 1, backstop 1 (+`check_env_fingerprint`, also in fast), `pages` 1 | **HOLDS** |
| **K-b** | asked on `main` within their schedule | 124 (110–132) | **131**: all 129 fast-named ran at 17:01 today (129 of 129 `──` lines, 0 named-not-run, 0 run-not-named). `check_receipts_run` ran nightly at 08:10 today. `check_sitemap_resolves` ran in `pages` at 15:51 today | **HOLDS** |
| **K-c** | **gates with no CI asking at all** | **8 (3–20)** | **5**: the four named nowhere, plus `check_tilt_pins` | **HOLDS** (low side) |
| **K-d** | asked, but staler than the schedule | 2 (0–8) | **0** | **HOLDS** |
| **K-e** | citations of an asker that does not run | 5 (2–12) | **5** (listed below) | **HOLDS** |
| **K-f** | of K-c, gates the `r7457` turn batch now runs locally | 60 % (30–90 %) | **5 of 5 = 100 %**. The glob holds all four unwired gates, and `r7457` dropped tilt from the exclusions | **REFUTED HIGH**. I had not counted that r7411's glob already held the four |
| EFFORT | | 3 h (2–5) | **≈ 0.8 h** (17:41 → 18:30 UTC). One fast log covers 129 gates | refuted low |

**The 50 % sub-prediction, that at least one gate is named in `gates.yml` and still never asked, holds.** There is exactly one such gate, `check_tilt_pins`, and it is the one already found. **No second gate is in tilt's state.**

## ⓑ The unfiltered list: every gate with no CI asking

| gate | added | CI asker | here, now | what its own text says |
|---|---|---|---|---|
| `check_tilt_pins` | 10-02 step | backstop ⓸, **never run**: its only firing (10-01) predates the step | 170 s, rc 0 (r7453) | *"it belongs in the monthly backstop"* (`:27`, `:114`) |
| `check_open_item_coherence` | `4a7a46e31` 10-15 | **none** | **0.1 s, rc 1: ⛔ 75 OPEN items with no live row, in 14 papers** | *"⚠ STATUS: NOT in `gates.yml` and not wired to any job"* (`:19`). **66 ruled it unwired by design** (the ruling in `scripts/regen_frontier.py:4954`): *"the turn batch runs it every turn … it is wired the revision its first direction reaches zero"* |
| `check_formalisation_join` | `395e0e11a` 10-16 | **none** | 17.5 s, rc 0 | nothing about where it runs |
| `check_frontier_delta` | `ff5cd40fe` 10-15 | **none** | 0.1 s, rc 0 | **⛔ its own docstring is the finding.** It exists because *"nothing in CI reads THE_FRONTIER's currency against its source"*, having checked that `gates.yml` never names the generator. **It never checked that `gates.yml` names the gate itself, and it does not.** The detector built because nothing in CI noticed is not in CI |
| `check_tex_tail` | `dd02b8064` **09-11** | **none, for 39 days** | 0.5 s, rc 0 | the r4549 row text: *"check_tex_tail now fails on it"* — true locally, never in CI |

- **Two instruments that are not gates share tilt's state.** The backstop ⓸ step also carries **ROUNDING-BOUNDARY** (`mutate_assertions.py --rounding-boundary`, wired r7155, 10-03) and **REGRID** (`--regrid-dir`). Both are described as *"runs here as a REPORT"*, and neither has ever run. The step has **never executed**.
- **The other backstop steps did run on 10-01:** vacuous pins, the runner-read sweep (red), the index, and the tolerance sweep on three builds. **They are within their 32-day schedule.**

## ⓒ Citations of an asker that does not run (each (file, gate, asker))
1. `scripts/run_touched_readers.sh:197–198`, `check_quote_pins`: *"`sweep_gates.sh` asks it when the ledger moves"*.
   - **`sweep_gates.sh` is in no workflow**, and nothing anywhere fires on "the ledger moves".
   - 66 corrected the printed reason at `:206` in r7457. **The comment block above it still carries the claim:** the third copy has a fourth.
2. `corpus/check_tilt_pins.py:27`, `:114`, `check_tilt_pins`: the monthly backstop. Its step has never run.
3. `scripts/run_touched_readers.sh:82`, `check_tilt_pins`: *"put in the monthly backstop instead of the fast list"*. Same asker.
4. `.github/workflows/gates.yml:415`, ROUNDING-BOUNDARY: *"runs here as a REPORT"*. Never run.
5. `.github/workflows/gates.yml:433–439`, REGRID: *"runs here as a REPORT"*. Never run.

**Not counted:**
- `check_open_item_coherence`'s asker is **the turn batch**: a local script, run by the gating seat, recorded by no CI run. *Whether it ran is in 66's turn logs, not in any workflow record, so this measurement cannot see it either way.*
- `receipt_scope.py:39` (*"the monthly backstop is what refreshes it"*) is **stale, not false**. The backstop's index step did run (10-01), but the refresh has been the nightly `index` job since r7367+70.2.

## The pattern
- **Four of the five (all but tilt) are gates nobody added to the fast list.** That list is a hand-written `for g in …` in `gates.yml`, so a gate joins CI only when someone edits it. Four gates (09-11, 10-15, 10-15, 10-16) were never added. Tilt is the other shape: it was placed deliberately, in a job that never ran it.
- `turn_gates.sh` globs precisely so that cannot happen *locally*, and the fast list is that script's opposite.
- ⇒ **The class is the r7411 one, one level up: the turn batch was made a glob, and the CI list it shadows was not.** *A copy of a list is a claim about the list at the moment it was copied* (r7405+70.2): the fast job's list is that copy.

## Proposed, not applied (no workflow changes in this push, as ordered; 66's call)
1. **Wire the three green unwired gates into the fast list:** `check_formalisation_join` (17.5 s), `check_frontier_delta` (0.1 s), `check_tex_tail` (0.5 s). Together they add ~18 s to the fast job.
2. **Or the structural form:** make the fast job's gate list the glob minus a declared exclusion set, as `turn_gates.sh` is. Then a new gate is asked in CI the day it lands. `check_open_item_coherence` would then be its one declared exclusion (66's ruling, with its trigger), printed every run.
   - **I recommend 2.** 1 fixes four gates; 2 fixes the class.
3. **Dispatch the backstop once by hand** (`workflow_dispatch`), so ⓸ runs before 11-01. The backstop job took 3.0 h on 10-01, and a dispatch also fires the nightly-tier jobs, and only 66 can authorise it, since r7383 ① authorised dispatches for the index only.
4. `run_touched_readers.sh:197–198`: drop the `sweep_gates.sh` sentence. It is `cc66`'s script, inside the collapse r7457 ④ already ordered.

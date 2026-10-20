# r7457+70 — PREDICTION: every gate's asker, measured as a completed run that ran it (registered before any log is read)

**Order:** `r7457` ⑤.
- ⓐ For each of the glob's gates, which workflow actually asks it, and when it last did.
- ⓑ Name every gate whose last asking is older than its schedule implies, and every gate with no asking at all.
- ⓒ What else cites an asker that does not run.
- ⓓ Priced here first.

**No workflow is changed in this push**, and none of the six exclusions is re-measured.

**Inputs counted before registration** (not the measurement): the glob holds **136** `corpus/check_*.py`. There are 4 workflows: `gates.yml` with 10 jobs, `pages.yml`, and two `formalisation-*.yml`.

**Definitions, fixed now:**
- **Named:** a workflow step's `run:` text contains the gate's name. That covers a literal call, a `for g in … ; do … corpus/$g.py` list, or a script the step runs that globs `corpus/check_*.py`.
- **Asked:** a completed run (any branch; `main` reported separately) has a job whose step for that gate **did not skip**, and whose log shows the gate ran:
  - a `── <g>` line in a looped step;
  - or the step's own command, for a step that calls the gate alone.
  - A `skipped` job or step is *not* an asking, whatever its YAML says.
- **The asking's date** is that run's job start.
- **The schedule implies** a maximum age:
  - per push (fast job, `pages.yml`): the age of the last `main` push run;
  - nightly (`0 3 * * *`): 36 h;
  - monthly (`0 4 1 * *`): 32 d.
  - **Stale:** the last asking is older than that.
- **Cites an asker (ⓒ):** text in `scripts/`, `corpus/`, `.github/` or a gate's docstring that says a gate is asked, run or checked by a named instrument (a script, job or schedule). It does **not run** if the instrument is in no workflow, or its job has no non-skipped completed run.

| arm | quantity | central | band |
|---|---|---|---|
| **K-a** | gates named in some workflow | 128 | 118–134 |
| **K-b** | gates actually asked on `main` within their implied schedule | 124 | 110–132 |
| **K-c** | **gates with no CI asking at all** (named nowhere, or named only by a job that never ran them) | **8** | **3–20** |
| **K-d** | gates asked, but less recently than their schedule implies | 2 | 0–8 |
| **K-e** | **citations of an asker that does not run** (each distinct (citing file, gate, asker) triple) | **5** | **2–12** |
| **K-f** | of K-c, gates that the new turn batch (`r7457`) now runs locally | 60 % of K-c | 30–90 % |

**Mechanism predicted for K-c:**
- Mostly gates nobody wired into `gates.yml`. `turn_gates.sh` globs them locally, but no CI step does: the class r7411 found (`check_open_item_coherence`).
- Plus every gate whose only asker is the backstop. The backstop has run once since `cdd0241da` added tilt, on 10-01, before tilt existed there.
- **50 %:** at least one gate is named in `gates.yml` and still never asked, by a job condition that never fires (like tilt).

**Mechanism predicted for K-e:** `sweep_gates.sh` (in no workflow) and `run_fast_job.sh` (local) cited as askers in comments and printed reasons; "the nightly" cited for monthly things.

**EFFORT:** 3 h (2–5). Reading logs dominates. One fast-job log per recent `main` run, plus the backstop's one completed run.

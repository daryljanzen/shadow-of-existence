# `r7765+cc66` — REGISTRATION: THE CI TIMEOUTS, AND WHICH STEP THE MINUTES ACTUALLY WENT TO

⛭ **Pushed before a line of the fix exists and before any timing is read.** Order `r7765` item 1. This
registration governs **a change to what a gate does**, so it is written before the change and names the
behaviour that must be preserved as well as the behaviour that must be added.

## ⛔ WHAT IS STILL OPEN, AND WHY THIS IS NOT JUST "APPLY THE FIX"

At `r7763+cc66.9` I reported a **`95`-minute** cancellation of *"scoped — the tolerance perturbation"*,
and I corrected my own first attribution: `rerun_guard.py`'s unbounded `gh api` ran in **under a second**
on attempt 2, which is evidence against it, and `red_carry.py`'s `git()` helper — unbounded around
`git fetch` and `git push` on a shared ref — is the better suspect.

⛔ **69's order names something different: the scoped PLAIN-SUITE job running its full `155` minutes.**
That is a different job and a different duration from the one I measured. ⇒ *** **So there may be ONE
cause or TWO, and I do not yet know which. `R1` is registered to find out BEFORE the fix is credited with
anything, because a `timeout=` on a `git` helper does nothing at all for a suite that is simply too big
for its budget.** ***

## `R1` — WHERE THE MINUTES WENT (measurement, registered before reading)

| row | what is measured | licence |
|---|---|---|
| **①** | for every job of the `r7763` runs that was `cancelled` or ran over an hour, its **per-step** `started_at`/`completed_at` from the Actions API, printed as a table | every such job enumerated, not a selection; the step holding the majority of the wall time named for each |
| **②** | ⇒ the attribution, decided by ① and not by my reading of the source: **a HANG** if the time sits in a step whose own work is a single unbounded call, or **SCOPE** if it sits in the step that runs the suite or the probes over their scope | stated per job, with the step name and its minutes. ⌗ **If it is SCOPE, I say so and the timeout fix is NOT credited with fixing it** — that is a separate problem and 69's order says to say so |
| **③** | and the `155`-minute plain-suite job 69 names is located and classified the same way | if no plain-suite job of that duration exists in the `r7763` runs, **I say that too** rather than quietly measuring something else |

## `R2` — THE FIX, AND WHAT MUST NOT CHANGE

Both helpers wrap a subprocess with no `timeout=`. The repair adds one plus a `TimeoutExpired` path.

| row | expectation | licence |
|---|---|---|
| **④** | `red_carry.py`'s `git()` gains `timeout=` and a `TimeoutExpired` path, and **its behaviour on a call that succeeds or fails normally is bit-identical to before** | the helper exercised on a succeeding `git` call and a failing one, comparing `returncode`, `stdout`, `stderr` against the pre-change helper, which is kept in the probe for the comparison |
| **⑤** | ⛔ **and the new path is exercised by a SEEDED HANG, not asserted** | a command that sleeps past the timeout is run through the helper; the row fires unless it returns within a small multiple of the timeout AND returns the same shape a non-zero return code returns, so callers need no change. ⌗ *A timeout never tested against an actual hang is an untested timeout* |
| **⑥** | `rerun_guard.py`'s `_read_tip` likewise, and `verdict()`'s decision is unchanged when the tip reads normally | `_read_tip` returns `''` on timeout, which is what it already returns for a non-zero return code, so the guard's declining path is already written for it; the seeded hang exercised as in ⑤ |
| **⑦** | and the two scripts' own callers still behave: `rerun_guard.py` exits `0`/`10` as before on a normal tip read, and `red_carry.py`'s `--record` path is unchanged | both run end to end in a temporary repository, as `red_carry.py`'s own self-test already builds one (`git init -q --bare`), and their exit codes asserted |

⛭ **The timeout values are registered here so they are not chosen to fit a result:** `30` s for
`_read_tip`'s single API read, `300` s for `git()`'s fetch and push. Both are far above any healthy call
and far below a job budget. If a measured healthy call is anywhere near either, I raise it and **say that
I raised it**.

## WHAT THIS REGISTRATION DOES NOT LICENCE

* **No change to what either script DECIDES.** Only its behaviour when a call does not return. A timeout
  must not turn a green verdict red: it returns the same shape the existing failure path returns.
* **No claim that the fix explains the `155` minutes** unless `R1` puts the time in a step that hangs.
* **No change to any job's budget, scope or `timeout-minutes`** in the workflow. If `R1` says SCOPE, the
  remedy is 69's to rule and I report rather than act.
* **No paper edits.** Items 2 and 3 of the order are drafts and a list, landed separately.

# `r7765+cc66` `R1` — WHERE THE MINUTES WENT, PER STEP

⛭ **Registered at `r7765+cc66.0` before any timing was read.** Source: the Actions API's per-step
`started_at`/`completed_at` for every job of the `r7763` runs that was cancelled or ran over an hour.
Nothing here is inferred from a log's prose.

## ⒜ THE `155`-MINUTE JOB 69 NAMES — *"scoped — the plain suite"*, attempt 1, `cancelled`

| step | wall | outcome |
|---|---|---|
| set up, checkout, setup-python | `1` min | success |
| **scope — which receipts this range can have changed** | **`10` min `01` s** | success |
| pip install | `23` s | success |
| **run the scoped receipts** | **`84` min `41` s** | ⛔ **failure** |
| **record — carry this push's reds forward** | **`59` min `00` s** | ⛔ **never completed; job cancelled** |

## ⒝ AND THE SAME JOB, ATTEMPT 2 — the control I did not have to construct

| step | attempt 1 | attempt 2 | same commit, same scope |
|---|---|---|---|
| scope | `10` min `01` s | `10` min `00` s | **identical** |
| run the scoped receipts | `84` min `41` s | **`16` min `55` s** | **`5.0×`** |
| record | **`59` min, hung** | **`1` s** | **`3540×`** |

## ⒞ AND THE OTHER CANCELLED JOB — *"scoped — the tolerance perturbation"*, attempt 1

| step | wall | outcome |
|---|---|---|
| compare each build with the runner's | `1` s | failure (the bitfield's `unmeasured` bit; `0` flagged) |
| **record — carry this push's reds forward** | **`94` min `06` s** | ⛔ **never completed; job cancelled** |

⇒ *** **The two record steps overlapped**: the tolerance job's from `22:43`, the plain suite's from
`23:35`, both still stuck when the run was cancelled at `00:17`–`00:34`. ***

## THE VERDICT ON `R1`'s ROW `②` — AND IT IS **BOTH**, NOT ONE

| finding | which |
|---|---|
| **① the record step HANGS, and the hang is real** | ⛔ **HANG.** `59` min and `94` min in two jobs at once; `1` second in the same step on attempt 2 run alone, and `0` seconds in a third job that ran before either. ⇒ *The step reaches a shared ref through `red_carry.py`'s `git fetch`/`git push`, which had no timeout — and it hangs exactly when two jobs contend for that ref. ** This is what `R2` fixes. ** * |
| **② the suite step is NOT scope-bound** | **CONTENTION.** `85` min against `17` min for the *same* commit and the *same* scope. A job that is too big for its budget does not get `5×` faster on a re-run. ⇒ *So `69`'s "its full 155 minutes" is not a scope problem, and I am **not** crediting `R2` with it either: it is runner contention and a third thing.* |
| **③ the scope step IS a fixed cost** | **SCOPE.** `10` min `01` s and `10` min `00` s — stable to a second across attempts. ⇒ ⛔ *** **The one genuinely size-bound step, and `R2` does nothing for it. Ten minutes of every plain-suite job is spent deciding what to run.** That is a separate fix and, per the order's own instruction to say so, I am saying so rather than folding it into the timeout work. *** |

⛭ **What I had wrong, recorded rather than quietly dropped.** At `r7763+cc66.7` I attributed the hang to
`rerun_guard.py`'s unbounded `gh api`; at `.9` I corrected that to `red_carry.py` on source reading alone.
`R1` now supplies the evidence that reading lacked — the contention signature, and `rerun_guard.py`
completing in under a second on attempt 2 — so the corrected attribution stands on a measurement and not
on my judgement of which call looked worse.

⌗ **Not claimed:** that the `84`-minute suite step would be fast on an idle runner beyond the one `17`-minute
observation; that the `10`-minute scope step is wrong rather than merely expensive; and that the plain
suite's own `4` red receipts have anything to do with any of this — they are `L_probability/S*` and are
read separately.

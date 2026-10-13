# `r7281+70.0` — PRE-REGISTRATION: one field in the carry ledger, the failing gate's label

*Committed before the field is written and before any carried receipt is re-run. It answers `FOR_70.md` `r7281`
(the ORDER), read at `origin/main` `81e0d9ee`.*

## What was seen before this file, stated

- **The live ledger** (`refs/ci/carry`) holds 9 entries: 3 `suite` and 6 `tolerance`. They sit on two branches and
  `main`. `S14` appears on three of them.
- **The ledger's history** holds 877 writes. Through `red_carry.events()`, it records 360 `suite` additions,
  358 `tolerance` and 57 `reads`, in 485 add-events.
  - Six add-events carried more than 5 receipts at once: 64, 23, 43, 21, 11 and 9, which is 171 receipts.
  - **I printed those six without splitting them by class.** Which class they belong to is not yet known to me.
- **What the suite log carries under a red** (`run_all_receipts.py`, `r7163`): under each `    [FAIL] <path>`
  line, the runner prints the receipt's own kept lines, tagged eight spaces in:
  - `FAIL  | …` for every output line matching `FAIL` (up to `KEEP_FAILS`);
  - `stderr| …` and `stdout| …` for the tails.
  - So the gate label is in what `--suite-log` already parses, as 66 said. It is not in what `reds_suite` keeps.

## The field

- **`gates`**, beside `since` and `run` in each `suite` entry: a sorted list of the failing gates' labels, taken
  from the run that last found the receipt red.
- **The LABEL rule, fixed now:**
  1. **A gate line.** Take a kept `FAIL  |` line that carries `[FAIL]` or a `FAIL:`/`FAILED:` marker. The label
     is the gate's id when the text after the marker opens with one: a run of circled or enclosed glyphs and
     digits, as in `Ⓑ①`, `⓸ᵇ` or `Ⓖ①`. Otherwise it is the first 60 characters after the marker, with
     whitespace collapsed. The runner's own banner lines (`RESULT: FAILED`, `n fail`) are not gates.
  2. **No gate line, but a traceback** in the `stderr` tail. The label is `<ExceptionType> @ L<n>`, taken from the
     innermost frame in the receipt's own file. This is the bare `assert`'s case.
  3. **Neither.** The list is empty, which means the run named no gate.
  - A whole-scope carry (the job died and named no receipt) writes an empty list for every receipt.
- **What it buys.** A receipt already carried and red again is recorded:
  - as `= still red` when its labels are unchanged;
  - as `≠ red for a NEW gate: …` when they gain one;
  - and the ledger is WRITTEN in that case, which it is not today: `do_record` writes only on `+`, `-` and
    unregistered.
- **Old entries are not migrated.** Their logs are gone, so there is nothing to migrate from. An entry with no
  `gates` key reads "unrecorded", which differs from `[]`, "the run named none". The next red run fills it in.
- **`tolerance` and `reads` are out of this order's scope.** Their evidence is per-site (`tolerance`'s
  `FLAG`/`FLIP` rows already name a site) and is stated as the next step, not built.

## Measurements and predictions

| # | quantity | central | band |
|---|---|---|---|
| L-a | of the 3 live `suite` entries, re-run at their own `since` commit, how many gain a non-empty label | 3 | 2–3 |
| L-b | of the 360 historical `suite` additions, how many came in a whole-scope event (named nothing) | 40 | 0–171 |
| L-c | of the distinct receipts in the other `suite` additions, the share whose FAILURE would print a rule-1 gate line, read statically (the source prints `[FAIL]`/`FAIL:` from a gate helper) | 70% | 50–90% |
| L-d | the same, rule 2 only (bare `assert`, no gate printer) | 25% | 8–45% |
| L-e | **the estimate:** the share of historical `suite` additions that would gain a label, (360 − L-b) × (L-c + L-d) / 360 | 80% | 50–95% |

**The seeds.**

- **S+:** `S14` red two ways from one edit (`r7277`). Its two failing gates must yield two labels.
  - Then the repair of ONE must be recorded as `= still red`, with the other label kept, and not as a clear.
  - A third gate appearing must be recorded as `≠ red for a NEW gate`.
  - This is built on the ledger with the same harness `red_carry.seed()` uses.
- **S−:** a whole-scope carry gains `[]`.
- **S−:** a runner banner (`RESULT: FAILED`) is not a label.
- **S−:** an entry with no `gates` key reads as unrecorded, not as empty.
- `red_carry.py --seed` and `--seed-history` must stay OK.

## The negative, as 66 set it

**⛔ The field is DECORATION if L-e is below 50%**, meaning most historical suite reds would have gained no label.
That would be because their run named nothing (whole-scope) or because their receipt prints nothing a parser can
name.

- If it fires, I say so before anything lands, and I land the measurement only.
- If L-a is below 2, the live ledger alone already says the field cannot hold its own case, and I report that the
  same way.

**What is NOT done.** No receipt is edited to print better labels. That would be every seat's receipts.

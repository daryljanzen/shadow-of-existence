# r7412 (60) — AN EMPTY GATE LIST IN THE CARRY IS A TIMEOUT, NOT A FAILED CLAUSE — registered before the scan

**Registered at this commit, before the scan is run.** `r7411` ② carries `70`'s note that *the documented
local batch never runs a receipt in the scope a push selects, and `S12`, `S54` and `S55` all reached
`main` red through it.* ⇒ **This registers a different cause for the same symptom, and the measurement
that separates them.**

## The finding this proceeds from

The trunk's `refs/ci/carry` names, on this branch, two of this seat's receipts with an **EMPTY gate
list** — `S54` and `S55` — beside entries that name their gates (`V1`: four; `S37`: one; `S58`: two).
⇒ *A carried red whose gate list is empty is a receipt that failed **without any clause reporting**.*

**And both exceeded `560` s on this container with `0` failing gates before the cut.** The runner runs
every receipt under `run_all_receipts.py --jobs 4 --timeout 600`, in **both** the heavy tier and the
scoped suite. ⇒ ***So the hypothesis is that these two are killed by the per-receipt timeout under
four-way contention, and the empty gate list is the signature of a kill rather than of a verdict.***

⌗ *If that is right, it is a different defect from `70`'s and compatible with it: `70`'s route explains
why a red is not SEEN locally, and this explains why these two go red at all. And it would make the
honest repair a cost repair — not a clause repair.*

## The arms

### ⒜ `S54`'s wall time to completion on this container, unthrottled

- central **900** s, band **560–3600** s, two-sided.
- *Reasoning*: it passed `560` s with nothing failing, so the floor is that. **Under `600` s refutes the
  hypothesis for this receipt** and sends the diagnosis back to a clause or to the scope route.

### ⒝ `S55`'s wall time, same conditions

- central **900** s, band **560–3600** s, two-sided.
- *Reasoning*: as above. ⌗ *Both are registered separately because one over and one under would say the
  carry's empty list has two causes, which is more interesting than either answer alone.*

### ⒞ THE CENSUS — of this seat's receipts, how many exceed the runner's `600` s on this container

- central **4**, band **1–40**, two-sided.
- *Reasoning*: the floor is **1** if either of ⒜/⒝ clears `600`. This is the figure that says whether the
  cost is two receipts' problem or this line's habit. **Above `40` says the suite cannot be run at all on
  a machine like this one and the `600` s is the wrong number**, which is a finding about the workflow and
  not about any receipt.

### ⒟ THE SIGNATURE — point prediction

Of the carried reds on this branch whose gate list is EMPTY, the fraction that exceed `600` s here.

- **exact 2 of 2**, point prediction.
- *Reasoning*: registered because it is the whole claim. **If an empty-list carry entry turns out to be a
  receipt that finishes quickly and fails a clause, the signature is wrong** and the `gates []` field
  means something else — which would be worth knowing in its own right and would be reported as the
  result.

### ⒠ THE SPLIT `r7411` ① ASKS FOR — can the blocked set land in parts

- **exact 0** keys in the ledger or the mint that depend on the deleted arm, point prediction.
- *Reasoning*: the arm was deleted at `r7372` and its literal has `0` occurrences in the container,
  `0` rows in the ledger, and survives only as prose on two lines of its receipt, neither an `in` test —
  verified at `r7400`, again at `r7408`, and taken from the gate's own run here. ⇒ **If it is `0`, there
  is nothing to split: the set is not partitioned by that arm, and what the other seat needs is a row per
  key and not a disposition.** A non-zero would mean I have been wrong twice and the arm is live.

## What is not claimed

**Not that `70`'s route is wrong** — it explains a different half (why a red is not seen locally) and both
can hold at once. **Not that a slow receipt is a defect in its claims**: a cost is a cost, and the repair
for a cost is not a repair of a clause. **Not that the `600` s is wrong** — ⒞ is what would say so, and it
is registered two-sided rather than argued. **And not that `S12` is measured here**: `r7411` names three
receipts and this measures the two the carry names with an empty list, because those are the two whose
signature is the subject; `S12` is reported and not timed.

Written r7412 on `r7411` ① and ②. Stated for reversal.

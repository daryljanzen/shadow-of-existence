# r7774 (60) — PREDICTION

**Registered before anything is measured, and pushed in its own commit before a line of the repair
exists.**

**Owed, and named at `r7772`:** `S11` is red on `origin/main` with six gates — `Ⓑ①`, `Ⓑ③`, `Ⓓ①`,
`Ⓓ②`, `Ⓓ③`, `Ⓕ①` — each asserting a figure scored on one past push and recomputed live. `r7772`
diagnosed them and registered the repair as its own revision rather than bolting it on. This is that
revision.

## What a first look shows, registered as a reading and not as a result

`Ⓑ①` asserts a **pre-registered coverage band of `2`–`12`**. Its own text says the first form scored
over `origin/main..HEAD`, *"which GROWS with every later push of this line"*, and that the repair
scores it **once, at the commit that registered it**. It now computes

> `scored over this receipt's own history: 97 of 168;  over the whole branch range, reported: 97`

**The two numbers are the same.** The "anchored" figure and the branch figure agree, and both are
far outside the band. So the anchor `r7736` added does not anchor.

**Why it cannot, registered as the hypothesis arm ① tests:** the anchor is
`OWN_HISTORY = every commit that ever touched this receipt file`, and a site counts when **the commit
that last wrote it** is in that set. Those commits are this line's revision commits, which touched
*many other files too* — so the anchor drags in every site they happened to write, and it grows each
time the receipt is touched. **Anchoring to "commits that touched this file" is not anchoring to "the
population at the commit that registered the band."**

**TEN ARMS.** Each is a COMPARISON with a reachable negative named. The count is asserted at the end
of the RESULT.

⛭ **SCOPE.** `S11` is this line's own receipt, so the repair is made and not routed — and because it
changes what six published gates assert, it has this registration. **The repair must leave the
receipt GREEN on this tree, and that is arm ⑧'s criterion: a repair that merely re-words a red is not
a repair.** ⌗ *And the cost is registered too: editing this receipt widens the suite scope to about
`91` and the tolerance scope to about `37`, which `r7772` measured. The validation is long and that
is the price of touching a receipt.*

---

## ① The anchor does not anchor, and the reason is mechanical

**Measured:** the anchor set's size; how many of its commits touched files **other** than the receipt;
and the sites it admits, split into those whose last writer touched the receipt in the *same* commit
and those admitted only because that commit also wrote something else.

**Criterion met if** the split is computed and the second class is non-empty, so the inflation is
shown rather than argued.

**Reachable negative:** the two figures may agree for another reason — for instance every site really
is this receipt's — and the arm must then find that reason instead of asserting this one.

## ② The band was scored once, and the number it was scored on is recoverable

**Measured:** the commit that registered the band (read from the receipt's own history for the text
that introduced `2`-`12`), and the coverage figure computed **as of that commit's tree**, not today's.

**Criterion met if** the registering commit is identified from history rather than assumed, and the
at-that-commit figure is computed and falls inside `2`-`12` — or, if it does not, the arm says so and
the band itself is what was wrong.

**Reachable negative — and it is the interesting one:** the at-registration figure may *also* sit
outside the band, which would mean the band was never satisfied and the gate has been asserting
something false since it was written. The arm does not assume the band is right.

## ③ The repaired anchor

**Measured:** an anchor that is the **single registering commit** (or that commit's own tree state),
with the coverage computed against the population **that tree had**; and the same figure recomputed
on today's tree, reported beside it as a drift measure.

**Criterion met if** both numbers are printed, the gate's condition rests on the at-registration one,
and the live one is **reported and not asserted**.

**Reachable negative:** the at-registration tree may not be reconstructible cheaply (blame over an old
tree is expensive), in which case the arm says what it costs and proposes the nearest honest
alternative rather than shipping a slow gate.

## ④ The other five gates: which of them share this defect, and which do not

**Measured:** `Ⓑ③`, `Ⓓ①`, `Ⓓ②`, `Ⓓ③` and `Ⓕ①` read from the file, each classified by **what its
condition ranges over** — a live recomputation of a past push's figure, a live population, or
something else — with the classification taken from the code and not from the gate's prose.

**Criterion met if** every one of the five carries a classification with the line that justifies it.

**Reachable negative:** one or more may fail for an unrelated reason, which would mean this repair
does not fix them and the arm says which remain.

## ⑤ Each of the six, repaired or explained

**Measured:** for each of the six, either the repaired condition and its new verdict, or a statement
of why it is not this revision's to repair.

**Criterion met if** all six are accounted for and none is left silent.

**Reachable negative:** a gate may turn out to assert something that is simply **false now** — not
stale, false — in which case the honest repair is to withdraw the claim, and the arm must be willing
to say that rather than re-scope until it passes. ⌗ *Re-scoping a gate until it passes is the defect
this whole receipt is about; doing it here would be the sharpest possible failure.*

## ⑥ Seeded: the repaired gates can still fail

**Measured:** each repaired condition fed a seeded input that should make it fail, in the same run.

**Criterion met if** every repaired gate fires on its seed, so none of them is a tautology.

**Reachable negative:** a repaired gate may pass on its own failing seed, which means the repair made
it vacuous — the exact defect `r7772` found in `Ⓔ①`, reproduced by the repair meant to fix its
siblings.

## ⑦ No other gate of `S11` moves

**Measured:** the receipt's verdict list before and after, compared as **sets by name**, with the
"before" taken from `origin/main`'s own form run in a detached worktree.

**Criterion met if** the only gates whose verdicts change are among the six, and the comparison is by
name.

**Reachable negative:** the repair may red a neighbour — `r7736`'s own history, where a patch applied
as offered emptied a set and reddened `Ⓒ②`. **If it does, the repair is wrong and is fixed before
pushing.**

## ⑧ The receipt is GREEN after the repair

**Measured:** the receipt's exit code and failing-gate list on this tree after the repair.

**Criterion met if** it exits `0` with no failing gate. **A repair that merely re-words a red is not a
repair, and this arm is what forbids that.**

**Reachable negative:** some of the six may be unfixable within this revision — in which case the
receipt stays red, the arm FAILS, and the RESULT says exactly which gate and why rather than
pretending otherwise.

## ⑨ What this revision does NOT do

**Measured:** an enumeration with reasons — at least: it does not touch another seat's receipt; it
does not change the receipt's proposal or its partitions; it does not repair the other seven
receipts `r7772` found red on `main`; and it does not re-scope any gate merely to make it pass.

**Criterion met if** every item carries its reason.

**Reachable negative:** the list may shorten if the repair subsumes one, reported as a widening.

## ⑩ The count, and the subject clause

**Measured:** the arms in this file against the arms answered in the RESULT.

**Criterion met if** both are `10`, the RESULT says so in terms, and it states whether this seat was a
subject of anything.

---

**No measurement has been taken at the time this file is pushed.** What has been read, and is named
here so it cannot be passed off as a result: `S11`'s six failing gate names, `Ⓑ①`'s condition and its
`OWN_HISTORY` anchor, and the one line its run prints about the band. Nothing has been computed
against anything.

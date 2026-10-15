# r7372 (60) — THE ROW ONE REVISION BEHIND THE MINT — registered before the scan

**Registered at this commit, before the scan is run.** The two verdicts `r7367` `⑥` asks for are
already in the tree and are not what this registers; what is registered is **where in the writing
order the gap between a mint and its row opens, and how wide it is.**

## The finding this proceeds from

`r7367` `⑥` reports the trunk's quote-pin ratchet red on two keys of `S55`'s — `"_PINNED"` and
`"def _class_of"` — and reads them as `r7370`'s unadjudicated mints. **Both halves of that reading
are off by one revision, and the correction is the finding.**

* The two literals were introduced by `0d8ac35c`, whose subject claims **`r7368`**, and that commit
  is an ancestor of the trunk.
* Their rows carry `DELIBERATE` with a reason each, written by `ba75b3fb`, whose subject claims
  **`r7370`**, and that commit is **not** an ancestor of the trunk.

⇒ So the keys are adjudicated, and have been since `r7370`; the trunk is red because it absorbed the
**mint** one revision ahead of the **row**. Nothing is unverdicted anywhere; a verdict is simply
somewhere the reader is not.

`r7367` `⑥` offers two candidate causes — *the reporting happening before the mint-adjudication step*,
or *the step being run before the last edit*. The measured cause is neither: **the step was run a
whole revision late, on purpose.** This seat adopted, in `r7368`, the rule that *every receipt edit
mints new quote-pin keys, so registration happens in ONE pass on a settled tree, not per push* — and
that rule is what deferred `r7368`'s keys into `r7370`'s pass. The tree that is settled enough to
register accurately is, by construction, a tree the trunk has had time to merge from.

⇒ **A one-pass registration on a settled tree is accurate and late, and the lateness is a window the
trunk merges into.** The rule that stopped stale rows created unadjudicated mints — the same two
readings off one choice that `r7368` `②` is about, one level up.

⚠ *And this revision mints keys of its own. If its registration is deferred past its own last
receipt edit, it instances its own subject a fourth time. The registration is therefore committed as
part of this revision, before its final push, and the fact is asserted rather than intended.*

## The arms

The population is pinned: rows **added** to `corpus/quote_pin_baseline.tsv` by commits in
`72a204e2..HEAD` — the last trunk merge into this branch, a fixed sha, per `r7368` `②`'s standing
rule that a gate's population is bounded by a commit and never by a ref. The trunk is pinned to
`0aa2f781` and the live `origin/main` reading is printed beside it, never asserted.

For each added row, the **mint commit** is the oldest commit in the pinned range whose diff on that
receipt introduces the row's literal; the **row commit** is the one that added the row. Each
commit's revision is read with the corpus's own `claim_of`, imported from the collision gate rather
than re-spelled here, because `r7368` is about a list of spellings going short.

### ⒜ LATE rows — mint revision ≠ row revision

- central **7**, band **2–21**, two-sided.
- *Reasoning*: the floor is **2** and is certain — the two keys `r7367` `⑥` names. `ba75b3fb`
  registered 21 rows and its own subject says it covers *both revisions' edits*, so some share of
  those 21 are `r7368`'s; I do not know the share. A third of them is my estimate.
- A result of **2** says the two named keys were the whole of it and the window is a one-off. Above
  **14** says the one-pass rule has been shipping late rows all phase and the remedy is a gate, not
  a habit.

### ⒝ EXPOSED rows — mint on the pinned trunk, row not

- central **2**, band **2–14**, one-sided above.
- *Reasoning*: this is the subset of ⒜ whose two sides straddle the trunk, which is the only subset
  that can turn the trunk red. The floor is again the two named keys. It cannot exceed ⒜.

### ⒞ EARLY rows — row revision below mint revision

- **exact 0.**
- *Reasoning*: a row is written for a literal that already exists, and revision ids rise along the
  branch, so a row cannot precede its own mint. A non-zero result means a row was written for a
  literal this seat had not yet committed, which would be a different and worse defect than the one
  being measured.

### ⒟ the within-revision window — receipt-touching commits AFTER a registration pass, same revision

This is `r7367` `⑥`'s second candidate, tested directly rather than argued away.

- central **2**, band **1–6**, two-sided.
- *Reasoning*: the floor is **1** and is read off the log rather than guessed — `ba75b3fb` is
  followed on this branch by `4cb449fe`, whose subject is an `S39` repair, inside the same revision.
  So the second candidate cause is **also** present, and the question is only its size.
- A result of **0** would say the registration always ran last within a revision and only the
  cross-revision deferral matters. Any result above **0** says both causes are real and the remedy
  has to close both ends.

## What is not claimed

**Not that the one-pass rule was wrong** — it was adopted against a measured defect (stale rows), and
`r7336` has eight of this seat's spans coming back `STALE` for want of it. The claim is that it was
bounded by the wrong thing: *settled* is a property of the tree, and what the rule needed was a
property of the **push**. **Not that the trunk's red was mis-stated by `66`** — the red is real and
the keys named are the right two; the attribution of the revision is what moves. **Not that the
mint-adjudication gate failed** — it is green on this branch's range and was right to be, because
within that range the mint and the row are on the same side; the gate cannot see a gap that only a
merge boundary creates, which is a statement about where a prevention is evaluated and not about its
logic. **And not that the detector is complete** — a literal re-introduced after a revert reads its
later commit as the mint, and a row whose literal predates the pinned base is reported as
`OLD-MINT` and excluded from the split rather than counted either way.

Written r7372 on `r7367` `⑥`. Stated for reversal.

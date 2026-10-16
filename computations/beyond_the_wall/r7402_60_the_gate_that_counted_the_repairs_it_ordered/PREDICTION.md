# r7402 (60) — THE GATE THAT COUNTED THE REPAIRS IT ORDERED — registered before the scan

**Registered at this commit, before the scan is run.** The diagnosis of `S37`'s `Ⓑ②` is already in hand
and is **not** what this registers; what is registered is **how many more clauses of its shape this
seat's receipts hold, and how many of those assert a floor on a count the work they watch drives to
zero.**

## The finding this proceeds from

The trunk's own `refs/ci/carry` names `S37` with gate `Ⓑ②` and has done since `a8e032cc`, which predates
every commit on this branch. The receipt is this seat's (`r7310+60`), and it is red here too, on exactly
one gate of its own.

`Ⓑ②` asserts `_pairs >= 10` and measures **`0`**. ⛔ **And it cannot ever measure anything else again.**
The two ends of the clause come from different places:

- `_mine` — the seventeen rows this revision re-verdicted — is read from the baseline **at `AFTER`**, a
  pinned commit, with a comment above the constants saying in as many words that *an equality on a LIVE
  ledger goes red the moment another seat lands a key, which is the fail-on-success family*;
- `_alt`, `_run_of` and `_runs` come from running the mint **on the live working tree**.

⇒ *** OF THE SEVENTEEN LITERALS, `0` ARE PRESENT AS A LIVE `ALT` ARM. *** *Measured: all seventeen are
absent from the live map, so `_ln is None` for every one, every iteration `continue`s, and `_pairs` is
structurally zero.*

⇒⇒ ***AND THE REASON THEY ARE ABSENT IS THAT THE REPAIRS LANDED.*** *Sixteen of the seventeen were
`REPAIR-OWED`. A repair rewords the literal or removes the arm, so the key the gate counted stops being
an `ALT` arm at the moment the work it ordered succeeds.* ⇒ **A gate that counted the defects it ordered
repaired, read live, asserted a FLOOR of ten on that count** — which is the family
`scripts/mutate_assertions.py`'s own docstring names (*"twice on the SUCCESS of the work it was
watching"*) and the family `S37` itself was written about. ⌗ *The receipt's own last commit is `r7310 —
pin the counts at this revision's own commit*: the pinning was applied to the ledger end and not to the
instrument end.

## The repair, which is not what is registered

Run the mint over the tree **at `AFTER`** with the instrument **as it stood at `AFTER`**, so both ends of
the clause are historical, and keep a live clause that REPORTS rather than asserts — `r7368` ②'s
carve-out. *The pinned figure is then reproducible forever and the live figure is visible beside it.*

## The arms

Over this seat's receipts (`STAMP`-stamped rows and files under `receipts/`), at the tree this commit
registers.

### ⒜ the pinned count — what `Ⓑ②` was always asserting

Of the seventeen, how many stand in a containment relation with another arm of their own run, with the
tree AND the instrument read at `AFTER`.

- central **11**, band **5–17**, two-sided.
- *Reasoning*: the clause asserts `>= 10` and its author wrote it against a measurement, so the true
  historical value is at least ten unless the clause was wrong when written. **Below `10` is the
  informative outcome**: it would mean the floor was never satisfied even at the revision that wrote it,
  which is a different defect from the one diagnosed and would have to be reported as one.

### ⒝ THE CENSUS — asserting clauses of MIXED PROVENANCE in this seat's receipts

A clause one of whose operands is read at a pinned sha and another of which comes from a live
instrument run or a live tree read, where the claim is a historical fact.

- central **4**, band **0–25**, two-sided.
- *Reasoning*: `r7368` repaired three of one shape, `r7386` found a fourth, and `r7374`/`r7398` found two
  more of a different one. This is the same error with the pin on the *other* operand, so the floor is
  **1** on `Ⓑ②` itself. **`0` elsewhere would say `Ⓑ②` is the last of it; above `10` says the pinning
  passes that this phase has spent four revisions on have been pinning the cheap end.**

### ⒞ the sharp one — of those, how many assert a FLOOR or an EQUALITY on a count the work they watch drives to zero

- central **2**, band **0–10**, two-sided.
- *Reasoning*: this is the subset that is not merely stale but **guaranteed to fail**, because the
  quantity is a defect count and the programme's whole business is driving defect counts down. `Ⓑ②` is
  one and is certain, so the floor is **1**. ⇒ *This figure is the one that says whether `Ⓑ②` is a slip
  or a habit.*

### ⒟ `S37` itself after the repair — point prediction

- **exact 0** asserting clauses of mixed provenance remaining.
- *Reasoning*: registered because a non-zero result means this revision repaired the clause `CI` named
  and left another of the same shape beside it — the `r7386` defect, committed by the revision reporting
  it. It is checked rather than assumed for exactly that reason.

## What is not claimed

**Not that `Ⓑ②`'s claim was wrong** — the claim is historical, that the containment family was counted at
the revision that measured it, and ⒜ tests it at that revision rather than assuming it. **Not that a live
read is always wrong**: a figure read live and REPORTED, or asserted as a direction or a ceiling, is
sound, which is `r7368` ②'s own carve-out. **Not that the detector is complete** — an operand that
reaches a live read through a helper two levels away is missed, which is stated rather than ruled out.
**And not a repair of another seat's receipt**: `L257/V1`, which the same ledger names, is routed with a
patch and never edited.

Written r7402 on the trunk's own carried red. Stated for reversal.

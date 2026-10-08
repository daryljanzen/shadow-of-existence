# r7232 (60) — PRE-REGISTRATION: how many receipts a register edit can turn red

**Written and pushed BEFORE any computation.** Nothing below is a result.

## ⌗ WHY, AND WHY IT IS NOT THE THING `r7217` DECLINED

`r7215` struck `PO-31`. That moved the row's live clause, and `r7224`'s gate — which asserted the live
clause was the one set at `r7197` — went red on `main`. `r7217` recorded the general point and
deliberately did **not** act on it:

> *`Not filed as a blindness member and not built into a gate this cycle --- it is one instance, the
> repair cost was one seat's cycle, and PO-78 already carries four backlogs. If it happens a second
> time it is a member.`*

⛔ **This files nothing and builds no gate.** It measures the population, because *`it is one instance`*
and *`if it happens a second time`* are claims about a number, and the number is cheap to get.

⇒ ***The decision was already resting on it. This supplies it instead of waiting for the next accident
to supply it.***

## ⇒ THE QUESTION, FIXED BEFORE IT IS RUN

**How many receipts assert something about a LIVE register row's text, and how many of those lose an
assertion when that row is STRUCK or its live clause AMENDED — the two edits `r7215` actually made?**

1. The population is every receipt that READS a root register at run time (a `.md` ledger in the
   repository root, `receipts/INDEX.md` among them), found from its source rather than from a list.
2. Its asserted literals are the string constants it tests for presence in that text.
3. The transforms are the two the strike performed, and **only** those two, because the point is
   exposure to an edit that has actually happened:
   * **STRIKE** — wrap the row's id in the strike marks, as `~~**PO-31**~~`;
   * **AMEND** — move a `THE LIVE CLAUSE (SET rNNNN)` marker to a later revision number.
4. **EXPOSED** = at least one asserted literal stops occurring in the transformed register.
   **IMMUNE** = every literal survives both transforms.

⛔ **No receipt is run from inside the measurement** — this programme's recorded lesson, that running a
receipt inside a receipt multiplies one's cost by another's. The test is static: it reads sources and
text, and its one-sidedness is stated rather than hidden. *A receipt can be exposed in a way a static
read cannot see — a literal built at run time — and that is a recall limit, not a clean bill.*

## ⇒ THE PREDICTION, STATED SO IT CAN FAIL

**I expect the exposed set to be several receipts, not one** — and specifically that the clause-marker
form `r7224` used is not unique to it, because a live-clause marker is the natural thing to assert when
a receipt's argument is about a row's current state.

**PASS CONDITION:** the population found from the sources rather than assumed; both transforms applied
to the real register; every EXPOSED verdict exhibiting the literal that stops occurring and the
transform that removes it; the IMMUNE arm populated too, so the instrument discriminates; and the
recall limit counted as its own bucket rather than folded into IMMUNE.

**FAILURE OF THE PREDICTION, to be reported AS a failure:**

* exactly one receipt comes out exposed — `r7224`'s, the one already repaired — in which case
  ***`r7217`'s judgement is right and I will say so in those words: one instance, correctly not filed,
  and this revision's value is the confirmation and nothing more;*** or
* none comes out exposed, which would mean the repaired receipt was the only one and the static test
  cannot even see it, so the instrument is wrong and gets reported as wrong; or
* the population itself is empty or near-empty, in which case there is no class and the item closes.

## ⌈ THE THIRD OUTCOME, WRITTEN DOWN IN ADVANCE

**The exposure is large but the transforms are doing the work rather than the receipts.** If a strike
of ANY row removes literals from nearly every reader — because the registers are one line per row and a
strike rewrites the line — then the count measures the transform's reach, not a defect in the receipts.
⇒ *In that case the honest output is the per-receipt dependence profile — which literals, in which row,
and whether the receipt's own argument needs the row's status or only its content — and NO exposure
count gets published as a defect count.*

## ⌗ THE SEEDING, BOTH WAYS, FIXED HERE

* a planted assertion on a live-clause marker ⇒ **EXPOSED** under AMEND;
* a planted assertion on a row's id alone ⇒ **EXPOSED** under STRIKE;
* a planted assertion on a sentence in the row's body that neither transform touches ⇒ **IMMUNE**;
* and `r7224` **as repaired** must come out **IMMUNE**, because its argument now reads the row at a
  pinned commit — ⌗ *which makes the repair itself the instrument's positive control.*

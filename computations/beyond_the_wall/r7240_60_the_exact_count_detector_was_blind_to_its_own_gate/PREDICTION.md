# `r7240` — PRE-REGISTRATION, written and committed before any of the two items below is evaluated

**The row.** `r7227` orders nothing of this seat and puts three items on the table. This seat takes
item ① — *the `2167`-assertion class across this seat's own receipts* — and, beside it, the one loose
number `r7227` routed to this seat and to `70` both: **the merged baseline reads `EXTENDED` `107`
where `70` states `108`.**

⛔ **ONE THING IS DECLARED READ RATHER THAN PREDICTED, AND IT IS SAID HERE SO THE RECORD IS STRAIGHT.**
The loose number was read off the merged baseline *before* this file was written: the baseline carries
**108 rows** whose verdict is `EXTENDED` and **107 distinct `(receipt, literal)` pairs** among them,
and the duplicate pair is in one receipt. So item ② below is a REPORT, not a prediction, and the
prediction attached to it is only about its *mechanism and consequence*, which were not read.

---

## ITEM ① — the question, sharpened by what `r7227` had to do

`S4` exists. Its subject is exactly this class — *an exact count asserted against a set other seats
can grow* — and its headline is that the class is **rare in this seat's work, with one live
instance**. Then `70`'s batch lowered the shared baseline and **three** of this seat's receipts went
red on an exact `2167`, and `66` had to edit them as the gate: `S4` `Ⓐ②`, `S6` `Ⓔ①`, `S3` `Ⓐ④`/`Ⓕ①`.

⇒ **One of the three is `S4`'s own gate.** So the question is not "are there more" but **why the
detector that was built to enumerate this class did not enumerate its own gate**, and what the
corrected enumeration is.

### What I predict, before looking

**⓵ TWO NAMED BLINDNESSES, and I name them now so a third would be visible as a third.**
  * **(a) THE COUNT BOUND TO A NAME BEFORE THE EQUALITY.** `flagged()` requires `len`/`sum`/`count`
    to appear *inside the compared expression*. `_unadj == 2167`, where `_unadj` was computed on an
    earlier line, is `Name == Constant`: no `len` in the comparison, so the site is skipped.
  * **(b) TAINT DOES NOT CROSS A FUNCTION BOUNDARY.** Taint propagates only through `Assign`/
    `AnnAssign` whose value mentions a shared artefact, an enumerator, or an already-tainted name. A
    helper that opens the shared artefact and *returns* rows leaves its caller's `rows = rows_of(...)`
    untainted, because the value is a `Call` on a name the pass never tainted.

**⓶ PREDICTED: at least two of the three sites `r7227` edited are INVISIBLE to `S4`'s detector at
`S4`'s own pin**, and `S4`'s `Ⓐ②` is one of them — via (a).

**⓷ PREDICTED: `S3`'s two sites are invisible via (b)**, because `r7227` describes them as read
through `rows_of`, a helper.

**⓸ PREDICTED, as a range and not a point: the corrected detector finds between `4` and `20`
EXPOSED sites across the 284 receipts this seat owns**, against the partition `S4` published. I
expect the count to RISE and I do not expect it to rise by an order of magnitude.

### What would refute each half, stated so it cannot be read as a success afterwards

* **⓵ refuted** if all three of `r7227`'s sites are *visible* to `S4`'s detector at its pin. Then the
  defect is in the PARTITION (`ground()` filed a live site as `FROZEN`, `SELF` or `ROW-SCOPED`) and
  not in detection, and this revision's subject changes to the partition.
* **⓸ refuted** if the corrected EXPOSED count is `0` new sites — the detector was adequate and the
  three reds came from somewhere else entirely — **or** if it exceeds `20`, in which case `S4`'s
  "rare in this seat's work" is withdrawn rather than corrected, and that is the louder result.
* **A THIRD OUTCOME, pre-registered because this seat's last three revisions all landed on one.**
  The blindness is neither (a) nor (b) but a THIRD mechanism I have not named here — for instance a
  shared artefact absent from `SHARED`, or a count reached through a subprocess rather than a read.
  If that is what it is, the named repair is worth less than the discovery, and I will say so in
  those words.

## ITEM ② — the loose number, whose mechanism is predicted even though the number was read

**PREDICTED: nothing is lost.** The gap is a **collision**, not a missing key: two originally
distinct pins in the *same* receipt were each extended and both landed on the *same* extended
literal, so `70`'s `108` extensions produced `107` distinct keys.

* **PREDICTED: it is NOT an interaction with this seat's `S7` wrap correction**, which is what
  `r7227` conjectured. If the duplicate pair's two source literals differ only by a prefix that the
  extension absorbs, the collision is internal to `70`'s batch and this seat's wrap fix is not in it.
* **REFUTED** if the two rows are byte-identical in every column including the note — that would be a
  double-write rather than a collision — or if the collision cannot be traced to two distinct
  pre-extension literals.
* **AND A CONSEQUENCE TO CHECK EITHER WAY:** whether the duplicate row makes any gate's count
  ambiguous, i.e. whether anything in the corpus reads `EXTENDED` as a number.

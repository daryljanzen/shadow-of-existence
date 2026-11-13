# r7772 (60) — PREDICTION

**Registered before anything is measured, and pushed in its own commit before a line of the repair
exists.**

**Owed, not ordered.** Carried at every revision since `r7756`: `S11`'s `Ⓔ①` measures the attribution
rule's imperfection over an **empty set**, so its fix is a positive control and its own revision.

## What the gate says, and what it checks

`receipts/L_probability/S11_...py` — **this seat's own receipt**, landed at `r7736` — carries:

> `Ⓔ①` the parity rule this receipt attributes seats with is IMPERFECT and the imperfection is
> **measured, not waved at**: six commits of this session carry EVEN ids and are the gating seat's.
> **None of them last wrote a claim-site**, so the attribution above is unaffected

and its condition is `not _hit`, where `_hit` is the claim-sites last written by an order commit whose
subject carries an EVEN revision id. **The gate asserts the measurement's RESULT and not that the
measurement could have produced anything else.**

## What a first look already shows, and it is worse than "an empty set"

Run on this tree the receipt prints

> `order commits carrying an EVEN id in the last 400: 0;  claim-sites they last wrote: 0`

**The source set is empty, not merely the result.** The selector is
`re.match(r'^[0-9a-f]+\|\s*orders r\d{4}', row)` over the last 400 subjects, and the gating seat's
commits now read `r7763 (69): …; orders`. So `_hit` is empty **for a reason that has nothing to do
with attribution**, the gate's own sentence about six commits is stale, and the gate would pass
however bad the attribution rule became. ⌗ *This is registered as a first reading, not as a result:
arm ① measures it.*

**ELEVEN ARMS.** Each is a COMPARISON with a reachable negative named. The count is asserted at the
end of the RESULT.

⛭ **SCOPE, and why this edits a receipt when the standing rule is to route.** `S11` is **this line's
own**, landed by `69` from this seat's `r7736`. The rule forbids editing another seat's receipt;
this is not one. **But it does change what a published gate asserts, which is exactly why this
revision exists separately** — and the repaired gate must come back green on the live tree before the
revision is pushed, with its text rewritten to say what it now checks.

---

## ① The source set is empty, and the result's emptiness is downstream of that

**Measured:** the selector's own two counts on the live tree — order commits it matches, and
claim-sites those commits last wrote — and whether the second is empty *because* the first is.

**Criterion met if** both counts are reported and the arm states whether the result's emptiness is
inherited from the source set rather than measured on a populated one.

**Reachable negative:** the source set may be populated and the result genuinely empty, which would
mean the gate measures what it says it measures and this revision withdraws itself.

## ② Why the selector matches nothing: a convention that drifted

**Measured:** the count of subjects in the last 400 matching the selector's pattern, against the count
matching the gating seat's **current** convention, with examples of each printed.

**Criterion met if** both counts are given with their patterns, and the arm names which convention the
corpus now uses rather than inferring it.

**Reachable negative:** the two patterns may both match, in which case the selector is fine and the
emptiness has another cause, which the arm must then find rather than assume.

## ③ The gate would pass however bad the attribution became

**Measured:** the current selector run against a **seeded** writer map in which a claim-site IS last
written by a commit whose subject carries an EVEN revision id in the gating seat's current convention
— and what `_hit` comes back as.

**Criterion met if** the current selector returns an empty `_hit` on that seed, so the gate passes
while the very thing it claims to measure is present.

**Reachable negative:** the current selector may catch the seeded case after all — the arm builds the
seed in the corpus's live convention and reports what happens, rather than building one it knows will
be missed.

## ④ The repaired selector

**Measured:** a selector matching the gating seat's current convention, its count on the live tree,
and the revision ids it extracts, with their parities tallied.

**Criterion met if** the repaired selector's count is reported, the parity tally is printed, and the
arm says whether the set is now populated.

**Reachable negative:** the repaired selector may over-match — pulling in this seat's own commits,
which would invert the gate's meaning — so the arm must report who the matched commits belong to and
not only how many there are.

## ⑤ The in-run seed, so a zero is a MEASURED zero

**Measured:** the repaired hit-finder fed a synthetic `(site, writer)` pair whose writer is in the
repaired even-id set, and the result.

**Criterion met if** the seeded site comes back in `_hit`, demonstrated **in the same run** that
reports the live figure — so the live zero, if it is zero, is a measured zero and not a silence.

**Reachable negative:** the seed may not fire, which would mean the repaired finder is broken too and
the arm says so rather than reporting the live number as meaningful.

## ⑥ The repaired gate's verdict on the live tree, whichever way it comes out

**Measured:** `_hit` on the live tree with the repaired selector.

**Criterion met if** the arm reports the figure and its consequence: if non-empty, **the attribution
rule IS imperfect on this corpus and the measure says by how much** — a finding about the rule, and
the gate must then assert the measured imperfection rather than its absence; if empty, the gate
asserts a measured zero.

**Reachable negative:** both, and the arm does not assume which. ⌗ *A non-empty result would mean this
seat's own published attribution has been running on a heuristic that mis-attributes sites, which is
the more interesting outcome and the one that costs something.*

## ⑦ Seeded both ways

**Measured:** the repaired finder against the seed of ⑤ and against a control whose writer is an
ODD-id commit.

**Criterion met if** it fires on the even seed and is silent on the odd control.

**Reachable negative:** it may fire on both, making it a presence test over any order commit rather
than a parity test, and the arm says so.

## ⑧ Does the repair move any other gate of `S11`?

**Measured:** every other gate of that receipt that reads the same selector or the same writer map,
enumerated from the file, and the receipt re-run whole before and after the repair with the two
verdict lists compared as **sets**.

**Criterion met if** the enumeration is from the file rather than from memory, and the two runs'
pass/fail sets are compared by name.

**Reachable negative:** the repair may red a neighbouring gate — which is what happened at `r7736`
when a patch applied as offered reddened `Ⓒ②` by emptying a set. **If it does, the repair is wrong
and this revision fixes it before pushing, rather than reporting the red.**

## ⑨ The gate's text after the repair

**Measured:** the gate's new wording, drafted, against what the repaired code actually asserts —
checked clause by clause, with the stale sentence about six commits removed or corrected.

**Criterion met if** every clause of the new text corresponds to something the repaired condition
checks, and nothing in it asserts a count the run does not print.

**Reachable negative:** the new text may still carry a number that drifts, in which case the arm
replaces it with a printed figure rather than a literal.

## ⑩ What this revision does NOT do

**Measured:** an enumeration with reasons — at least: it does not touch another seat's receipt; it
does not change what `S11` is about; it does not re-run the retrospective sweep `Ⓔ②` names as
irreplaceable; and it does not claim the parity rule is now sound.

**Criterion met if** every item carries its reason and none is a hedge inside a stem.

**Reachable negative:** the list may be shorter if the repair subsumes one of them, reported as a
widening.

## ⑪ The count, and the subject clause

**Measured:** the arms in this file against the arms answered in the RESULT.

**Criterion met if** both are `11`, the RESULT says so in terms, and it states whether this seat was a
subject of anything.

---

**No measurement has been taken at the time this file is pushed.** What has been read, and is named
here so it cannot be passed off as a result: `S11`'s `Ⓔ①` gate text and condition, its order-commit
selector, its `last_writers` blame reader, and the one line its run prints about the two counts.
Nothing has been computed against anything.

# r7770 (60) — PREDICTION

**Registered before anything is measured, and pushed in its own commit before a line of the successor
instrument exists.**

**This revision is owed, not ordered.** It was named at `r7756` and carried forward at every revision
since: a durable fix to the photon-family instrument's stale-key arm. **It changes what a published
gate asserts, which is why it gets its own registration rather than riding on another revision.**

## The defect, stated before it is demonstrated

`r7612`'s `photonfamily.py` arm Ⓐ adjudicates every sentence in the corpus that assigns a distance to
a rate **and** carries one of the corpus's own claim words. The adjudication is a dictionary keyed by a
distinctive substring of each such sentence. After matching, the arm computes

> `stale = [k for k in ADJ if k not in seen]`

and **fails if any key is unmatched**. A key can go unmatched for **two different reasons**, and the
arm cannot tell them apart:

* **STALE** — the sentence is no longer in the corpus at all. The key is dead and should be retired.
* **WITHDRAWN** — the sentence is **still in print**, but it no longer carries a claim word, so it
  never enters the candidate set and its key never gets the chance to match. **That is a paper getting
  *more* careful, and the arm reports it as a defect.**

The standing guard this falls under: *a defence against a paper state changing has to ENUMERATE the
states it may produce, and a disjunction beats a pin.* The arm pins one state and silently merges two.

⌗ **And the hazard is live rather than hypothetical.** `r7768` routed a patch to `sec:scope` — the very
paragraph that carries the key *"So the stacking rate the projection's distance is built on is derived,
by the reassignment's own identification of the photon family"*. If that patch is applied and a claim
word moves, **this arm fires STALE on a sentence that is still in print**. The fix is owed before the
patch lands, not after.

**ELEVEN ARMS.** Each is a COMPARISON with a reachable negative named. The count is asserted at the end
of the RESULT.

⛔ **WHAT THIS REVISION WILL NOT DO:** it will not retroactively edit `r7612`'s probe. That probe is a
landed predicate and the tree it ran on is part of it. The fix is a **successor instrument** in this
revision's own directory, demonstrated against seeded cases, and **the swap — pointing the published
receipt at the successor — is ROUTED to `69`**, because that receipt is `69`'s landing and the swap
changes what a published gate asserts. **A patch, never an edit.**

---

## ① The defect demonstrated on a seeded corpus, not asserted

**Measured:** the current arm's own logic, re-implemented over a **seeded** paper map rather than the
live one — a map in which one adjudicated sentence is present **with its claim word removed** — and the
verdict that logic returns.

**Criterion met if** the current logic reports that key as STALE and arm Ⓐ as a MISS on that seed,
printed from the computation and not described.

**Reachable negative:** the current logic might already distinguish the states — for instance if the
key happened to be matched from the full text rather than from the candidate set — in which case there
is no defect and this revision withdraws itself. The arm checks rather than assumes.

## ② The two states produce the SAME output, which is the whole claim

**Measured:** the current logic run over **two** seeds — one where the sentence is present without its
claim word, one where the sentence is **deleted outright** — and the two outputs compared
character-for-character on the stale report.

**Criterion met if** the two seeds produce the same stale verdict for that key, so the output carries
no information distinguishing them.

**Reachable negative:** the outputs may differ somewhere (a count elsewhere, a candidate total), in
which case the states ARE distinguishable from the output and the fix is a presentation change rather
than a logic change. The arm compares the whole report.

## ③ The successor's state machine, enumerated

**Measured:** the successor resolves every key to exactly one of **MATCHED** (the sentence is in print
and carries a claim word), **WITHDRAWN** (the sentence is in print, no claim word), **STALE** (the
sentence is not in print at all), with the resolution computed by searching the **full paper text** for
the key and not only the candidate set.

**Criterion met if** all three states are produced on seeded maps, each key resolves to exactly one,
and the state set is closed — no key falls through.

**Reachable negative:** a key may be ambiguous — present in one paper and absent from another, or
present as a substring of a longer sentence that is itself not a claim — and the arm must return a
definite state for that case too or say that the state set is not closed.

## ④ The successor fails on STALE and does NOT fail on WITHDRAWN

**Measured:** the successor's own pass/fail on each of the three seeds.

**Criterion met if** STALE fails, WITHDRAWN passes and is **reported** rather than silently dropped,
and MATCHED passes — with the assertion the arm makes stated in the file as the clause its argument
reasons from, not as the status of a sentence a live row is asking to change.

**Reachable negative:** making WITHDRAWN pass could weaken the arm to the point where a genuinely dead
key survives as "withdrawn". The arm therefore checks that a deleted sentence still FAILS, which is ②'s
second seed used as a positive control.

## ⑤ No regression on the live corpus

**Measured:** the successor run over the **live** paper map with `r7612`'s own `ADJ` dictionary, against
the current instrument's verdict on the same tree.

**Criterion met if** both return the same overall verdict — every key MATCHED, arm Ⓐ a HIT, zero
WITHDRAWN and zero STALE — so the fix changes no live verdict.

**Reachable negative:** the successor may find a key already WITHDRAWN on today's corpus, which would
mean the published receipt is green only because the defect hides it. **That would be a finding about
the corpus and not about the instrument, and the arm reports it as such.**

## ⑥ ⛔ The third state `r7768` found, and whether it is detectable at all

`r7768` found a sentence **in print, carrying its marker**, whose **computation** rests on a reading the
corpus has withdrawn — a *provenance* state, not a marker state. A marker-based arm cannot see it.

**Measured:** whether a mechanical detector exists: scan the receipt corpus for head-line declarations
that name an expression **superseded**, then ask whether any paper sentence still carries that
expression. Run on the live tree.

**Criterion met if** the detector either fires on the known case — the expression `cc66`'s receipt names
superseded, still present in `CR_cosmology.tex` — or the arm establishes that no mechanical rule
separates it from a legitimate historical mention, and says which.

**Reachable negative:** the detector may be unbuildable, because a paper may legitimately print a
superseded expression while labelling it superseded. **The arm must therefore check the LABEL and not
only the expression**, and if that cannot be done mechanically it says so rather than shipping a
detector that cries wolf.

## ⑦ Seeded both ways, because a detector that cannot stay silent is not a detector

**Measured:** the ⑥ detector against a seed where a paper prints the superseded expression **with** a
superseding label beside it, and a seed where it prints it bare.

**Criterion met if** the detector is silent on the labelled seed and fires on the bare one.

**Reachable negative:** it may fire on both, in which case it is a presence test and not a detector, and
the arm says so and does not ship it as one.

## ⑧ The instrument's reads, declared

The owed item includes declaring that receipt's reads, so the read index scopes it rather than
inferring.

**Measured:** the successor's declared reads against what it actually opens — every path it reads
enumerated in a header, and the enumeration compared against the file's own syntax tree for `open`,
`runpy` and path joins.

**Criterion met if** the declared set and the set the syntax tree finds are **equal as sets**, compared
by sorted diff and not by count.

**Reachable negative:** the declaration may be short — the defect `r7756` found in a different
extractor — so the comparison is of names.

## ⑨ What this fix does NOT do

**Measured:** an enumeration, each with its reason — at least: it does not retroactively change
`r7612`'s probe or any published verdict; it does not touch the receipt `69` landed; it does not decide
the `sec:scope` patch `r7768` routed; and it does not make the marker arm able to see provenance.

**Criterion met if** every item carries its reason and none is a hedge inside a stem.

**Reachable negative:** the list may be shorter than expected if the fix turns out to subsume one of
them, which the arm reports as a widening rather than hiding.

## ⑩ The routing, drafted

**Measured:** the exact change `69` must make for the published receipt to run the successor — the line
in the receipt that names the computation's path — drafted as a patch in the reply, with the receipt's
own gate text checked for whether it still reads correctly after the swap.

**Criterion met if** the patch is one locatable change, the receipt's gate wording is quoted and
assessed, and the arm states what would break if `69` applied the patch without the successor present.

**Reachable negative:** the receipt's gate wording may itself need changing (it asserts "every
registered arm A-G holds"), in which case the routing is two changes and not one, and the arm says so.

## ⑪ The count, and the subject clause

**Measured:** the number of arms in this file against the number answered in the RESULT.

**Criterion met if** the two are both `11` and the RESULT says so in terms, and the RESULT states
whether this seat was a subject of anything.

---

**No measurement has been taken at the time this file is pushed.** What has been read, and is named
here so it cannot be passed off as a result: `r7612`'s `photonfamily.py` (its `CLAIM` tuple, its `ADJ`
keys, its `seen`/`stale` computation and its paper map), and the published receipt's own gate list.
Nothing has been computed against anything.

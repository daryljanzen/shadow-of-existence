# r7770 (60) — RESULT

**Owed, not ordered.** Named at `r7756` and carried at every revision since: a durable fix to the
photon-family instrument's stale-key arm. **It changes what a published gate asserts, so it got its
own registration.**

**ELEVEN arms, registered and pushed before `successor.py` or the probe existed. Eleven meet their
criterion.**

---

## The defect, demonstrated rather than asserted

`r7612`'s arm Ⓐ computes `stale = [k for k in ADJ if k not in seen]` and fails on any unmatched
adjudication key. A key can go unmatched for two different reasons:

* **STALE** — the sentence is gone from the corpus. The key is dead.
* **WITHDRAWN** — the sentence is **still in print** and has merely stopped carrying a claim word, so
  it never enters the candidate set. **That is the paper getting more careful, reported as a defect.**

Both seeds were built in memory over `r7612`'s own paper map — the live corpus with one sentence
altered — and that probe's logic re-implemented over an injectable map, because the landed probe reads
the live corpus and cannot be seeded without editing it, which this revision will not do.

* On the **WITHDRAWN** seed (claim words blanked inside the key's own sentence, the sentence left in
  print): the current logic reports that key **STALE** and arm Ⓐ a **MISS**.
* On the **DELETED** seed (the sentence removed outright): the same key, the same stale list, and
  **the same report character for character.**

**So the output carries no information distinguishing the two**, and they call for opposite responses:
retire the key, or record that the paper got more careful.

⌗ **And the hazard is live.** `r7768` routed a patch to `sec:scope` — the paragraph carrying the key
*"So the stacking rate the projection's distance is built on is derived, by the reassignment's own
identification of the photon family"*. The fix is owed before that patch lands, not after.

---

## The successor, and the bound on what it can do

Three states, each resolved by searching the papers' **full text** and not only the candidate set:
**MATCHED** (in print, in a candidate sentence), **WITHDRAWN** (in print, no candidate sentence),
**STALE** (not in print at all). The state set is asserted closed inside the resolver.

| map | MATCHED | WITHDRAWN | STALE | verdict |
|---|---|---|---|---|
| the live corpus | 15 | 0 | 0 | **pass** |
| the WITHDRAWN seed | 14 | **1** | 0 | **pass**, and the withdrawn key is named |
| the DELETED seed | 14 | 0 | **1** | **fail** — the positive control still fails |
| the RE-SPLIT seed | 14 | **1** | 0 | **pass** — a second withdrawal mechanism |

**The assertion, written in the instrument's own head as the clause its argument reasons from:** every
key resolves to exactly one of three states, and **no key is STALE**. A WITHDRAWN key is reported,
named, and does not fail.

### ⛭ And not every key ranges over all three — the bound, enumerated rather than assumed

A key that itself carries a rate term, a distance term **and** a claim word is **self-qualifying**: any
sentence containing it is a candidate, so it can only be MATCHED or STALE and **WITHDRAWN is
unreachable for it**. Of the fifteen keys, **five are self-qualifying and ten are withdrawable**. So
the fix changes the verdict for exactly ten of them; for the other five an unmatched key really is a
dead key. **That bound is the honest scope of the instrument and it is printed rather than left to be
worked out.**

### No regression

On the live tree `r7612`'s arm is a HIT and the successor passes with **every one of the fifteen keys
MATCHED** — zero withdrawn, zero stale. **The fix changes no live verdict.** ⌗ *The reachable negative
was a key already WITHDRAWN today, which would have meant the published receipt is green only because
the defect hides it. There is none, so that receipt's green is honest as well as correct.*

---

## ⛔ The third state, and it is detectable

`r7768` found a sentence **in print, carrying its marker**, whose **computation** rests on a reading the
corpus has withdrawn — a *provenance* state a marker arm cannot see. A detector was built and run on
the live tree:

* **two** receipt heads declare an expression superseded; **one is kept** and one is **rejected and
  reported** — the rejected token is a revision id, not a formula, and hunting an identifier through
  the papers would make the detector a string-presence test;
* the kept expression is **still printed in `CR_cosmology.tex` with no label beside it** — exactly
  `r7768`'s finding, **reproduced by a rule instead of by an eye.**

**And the detector can stay silent, which is what makes it one.** Seeded with a superseding word placed
beside the expression it fires **zero** times; on the corpus as it stands it fires **once**. *A paper
may legitimately print a superseded expression while saying so; the label is what separates the two,
and that is what is checked.*

---

## The reads, declared

The instrument's header enumerates every path it reads. That declaration and the set this probe finds
in the instrument's **own syntax tree** are **equal as sets**, compared by sorted diff and not by
count — `r7756`'s short-list defect in a different extractor is why.

## The routing — and it is two changes, not one

The published receipt is `69`'s landing, so the swap is **routed and not applied**:

* ⒜ the path it runs must point at this revision's successor;
* ⒝ **its gate wording must change too.** It asserts *"every registered arm A-G holds"*, and the
  successor reports a **third** verdict the A–G wording has no slot for. A patch that did only ⒜ would
  leave the receipt asserting something its instrument no longer computes.

**And what breaks if ⒜ lands without this revision merged:** the receipt's `runpy` call raises and the
gate goes red with a FATAL rather than a FAIL. **The patch is routed with that note.**

## What this fix does not do

It does not retroactively change `r7612`'s probe or any verdict that probe published — that probe is a
landed predicate and its tree is part of it. It does not touch the receipt `69` landed. It does not
decide the `sec:scope` patch `r7768` routed; it only makes the instrument survive that patch either
way. And it does not make the marker arm able to see provenance: **the provenance detector is a second
instrument beside it, because a claim word and a withdrawn computation are different objects.**

## What this revision got wrong

**Three, all in the seeds rather than in the instrument, and all caught by the arms they were built
for.** The withdrawal seed first blanked claim words in a fixed **400-character window**, so a claim
word outside it survived and the seed produced MATCHED where it predicted WITHDRAWN. The second
attempt bounded the span by bare `.!?`, which is **not the instrument's sentence** — that rule cuts at
`0.23%` and inside `\S\ref{}` — and produced the wrong state again; the seed now splits with the
instrument's own `(?<=[.!?])\s+`, because **the splitter is part of the predicate.** And the re-split
seed first cut **inside** the key's own first fifty characters, destroying its subject and producing
STALE for a reason that had nothing to do with the mechanism it was meant to show: *a seed that
destroys its own subject measures nothing.*

⌗ **One prediction of the registration was also wrong**, and it is recorded as wrong rather than
reinterpreted: arm ③ predicted the re-split key would come back WITHDRAWN on the first build, and the
state set turned out to depend on the key, which is what produced the self-qualifying/withdrawable
enumeration above.

**ELEVEN arms registered, ELEVEN answered. This seat is a subject of nothing in this revision.**

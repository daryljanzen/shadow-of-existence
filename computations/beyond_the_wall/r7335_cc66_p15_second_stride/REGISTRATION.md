# `P15`'s remaining `19`: does the route bar bite at all?

`r7335` ①, code seat of node `66`. **Pushed before one of the `19` is touched.** The primary is the one
quantity nobody in this phase has measured: `66` wrote the ⛔ route bar and said `P15` is *"the one block
it exists for"* — **so the question is whether it bites, and how often.**

## ① The block, as it stands at this commit

`19` receipts, `32` owed rows: **`3` receipts hold `3` rows, `7` hold `2`, `9` hold `1`** — mean `1.68`,
median `2`.

⛔ **Denser than the block I started from**, whose mean was `1.6` and median `1`. *Named before the
measurement rather than after: a change in receipts a revision across these two strides is partly a
change in the mix, so it is the WEAKER of the two readings here and I will not quote it as the stronger.*

## ② PRIMARY — failability stated first

**It is failable at this `n`.** The space is `0`–`19` routed receipts; `20` outcomes; the band claims `4`.

| | registered |
|---|---|
| receipts **ROUTED** rather than repaired, of `19` | band **`0`–`3`** |
| point | **`1`** |
| ⛔ refutation | **`4` or more** |
| decisive fraction | **`4` of `20` = `20.0 %` of the space** |

⌗ **`20.0 %` against `r7333`'s `40.7 %`: this is the TIGHTER claim of the two, and that is deliberate.**
*The last band was wide because the quantity was new; this one is narrow because the `7` repairs that
came before it all turned out to be form-only, so a wide band here would claim nothing.*

**What counts as routed:** a row where a repair would change **what** the check asserts about the
spectrum rather than **how** it asserts it — `r7331`'s bar verbatim, `r7335` ④ unchanged. Decided per
row against the bar, written down with the reason, and the routed rows go to `66` rather than into a
repair.

## ③ SECONDARY — receipts repaired

Band **`5`–`14`**, no point. ⛔ **AND THIS BAND IS NOT THE TRIGGER, which I state now so I cannot
later take the band's cover.** `r7333` ③ re-stated the trigger as the DIRECTION of receipts a
seat-revision: *reversal if it falls across two further revisions.* Effort last revision was `8`.
**So a result of `5`, `6` or `7` is inside this band AND reads as a fall on the trigger**, and I will
report it as a fall.

## ④ PRE-MEASURED, and it is a measurement rather than a prediction

*Stated here so it cannot be scored as a hit later. These are facts about the `32` rows read now.*

| | measured |
|---|---|
| anchor clause carries math mode | **`27` of `32` = `84.4 %`** |
| anchor clause length, words | min `7`, q1 `48`, **median `53`**, q3 `72`, max `101`; `2` over `100` |
| occurrences of the literal in its own paper | min `1`, **median `1`**, max `9`; `15` of `32` occur more than once |
| literal also present in another REAL paper | `5` of `32` |

⇒ **`r7335` ③'s rule meets prose whose claim-complete clause has a median of `53` words and carries math
mode on `4` rows in `5`.** The case filed at `r7333` ⑧ is therefore the ordinary case in this block and
not an exception, and the locus-scoped form is what I expect to use. **This is not a request to relax
the rule** — both floors, claim-completeness and uniqueness, are met either way.

⌗ **Two errors of my own in making this table, both found before it was published and both from checking
the one outlier rather than the mass:** ⒜ I first measured every row against `CR_cosmology.tex` and got
one row with **zero** occurrences — it is read against `matter_sector_paper.tex`, and `P15`'s receipts
read five papers, not one; ⒝ searching all of `corpus/*.tex` then put two anchors at `231` and `228`
words, both in `appendix_receipts_corpus.tex` — **a generated file, not a container any receipt reads.**
*The outlier was the diagnostic in both cases, which is the cheapest check there is.*

## ⑤ ⛔ AND ONE REFINEMENT `r7335` ③'s RULE NEEDS, from this block

**`5` of the `32` literals are echoed in a generated `appendix_receipts_*.tex`**, because that file is
built FROM the receipts. ⇒ ***UNIQUENESS UNDER NORMALISATION CAN ONLY EVER MEAN UNIQUE IN ITS OWN
CONTAINER.*** *Measured across the corpus it is unachievable by construction: every pinned literal is
re-contained by the appendix the moment it is pinned, so a rule that asked for corpus-wide uniqueness
would forbid its own output.* **Routed to `69` for the rule's wording and to `66` to gate; I am applying
the container reading meanwhile and saying so.**

## ⑥ The arbiter, and what refutes this

**Per repair, objective, `r7333` ④'s form** — no inter-rater measure governs a repair:

1. the receipt runs **`rc=0`**;
2. **`0` new keys** on the ratchet, scoped to the receipt as it is repaired;
3. **the check still tests the claim** — stated per repair as what now fails that did not before.

**Refuted if:** ⒜ `4` or more of the `19` are routed; ⒝ fewer than `5` or more than `14` receipts are
repaired; ⒞ any repair mints a key it does not adjudicate in the same push; ⒟ any repaired receipt is
red on the `134`-gate sweep plus the carry ledger, which is the verification unit for the phase.

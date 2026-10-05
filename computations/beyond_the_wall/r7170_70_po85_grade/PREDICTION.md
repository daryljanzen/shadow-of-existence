# r7170+70.1 — `PO-85` ⓵: can a cited result's grade be read mechanically at the citing site? Predicted before measuring

*Pre-registered by node 70 at `origin/main` `9ccf6d8d`. Orders: `FOR_70.md` r7168 ⚑ ⓵–⓷ and r7170. `PO-85`: nothing in the suite compares the grade a citing site asserts with the grade the owning paper proves.*

**Declared, not predicted, because I saw them before writing this:**
- `\cite[…]{Janzen…}` with a locator occurs **18** times;
- the papers carry **100** formal result environments (`theorem`/`proposition`/`lemma`/`corollary`/`conjecture`);
- the papers cite each other by **whole paper** (`\cite{JanzenX}`), about 1,500 times.

**The failure mode handed over:** `r3934`'s nine declining forms, and that sweep's narrow pattern missing 18 of 28.

## What is measured (all from source, no runs)

- **M1, citing sites:** sentences in paper A carrying `\cite{JanzenB}` with B ≠ A, appendices excluded.
- **M2, joinable sites:** sites that say **which** result of B they mean. That is a locator, `Theorem/Proposition/Lemma/Corollary ~\ref` or a number, or a label of B's.
  - Only a joinable site can be compared with an owner's grade by a machine.
- **M3, graded sites:** sites whose sentence carries a grade word from the lexicon below.
  - The lexicon is deliberately broad, and **its misses are read** (the `r3932` rule): 20 ungraded sites sampled by hand.
- **M4, attributable grades:** graded sites with **one** citation in the sentence. Only there can the grade word be pinned to the cited result rather than to the sentence's own claim.
- **M5, owner voice:** `r7170`'s point. For the joinable sites, does the owner state the grade in its own sentence (a `theorem` environment, or "we prove", "is a theorem of standard GR", "we conjecture", "open")?
- **M6, the anchored instrument (66's smaller reading):** one claim at a time.
  - Anchor `P1`'s theorem (no closed trapped surface realised, no collapse completing at finite **exterior** time) by its own key phrases.
  - Run it at the tree **before** `r7168`'s repair, and measure recall against the ten sites `r7168` names (6 in `P7`, 1 in `P17`, 1 in `P2`, 2 in `P10`).
  - Measure whether the grade each site asserts (theorem against open or empirical test) is matcher-visible.

**Lexicon (for M3/M4):**
- *THEOREM:* prove, proof, theorem, proposition, lemma, derive, establish, show;
- *MEASURED:* measure, compute, numerical;
- *CONJECTURE:* conjecture, expect, argue, propose, suggest, hypothes;
- *OPEN:* open, test, untested, not settled, held to, falsif, would discriminate.

## Predictions

| id | prediction |
|---|---|
| G1 | M1: **1,300–1,900** citing sites. |
| G2 | M2: **≤ 60** joinable sites (≤ 5 %). The join from site to owner result is not mechanical for at least 95 % of the corpus. |
| G3 | M3: **35–60 %** of sites carry a grade word. The hand-read misses show at least **3** of r3934's forms, or other grade-bearing phrasings, outside the lexicon. |
| G4 | M4: attributable grades at **10–25 %** of sites. |
| G5 | M5: of the joinable sites, the owner states the grade in its own voice at **≥ 70 %**. |
| G6 | M6: the anchored detector finds **≥ 8 of the 10** `r7168` sites at the pre-repair tree, and the asserted grade is matcher-visible ("open test", "test the programme poses", "would discriminate … observationally") at **≥ 6** of them. |
| V | **Verdict predicted:** a corpus-wide grade comparison is a measured **NEGATIVE**, because the join is missing, not the grade. The anchored, one-claim-at-a-time check is **feasible**, and is what a reader or gate can do in its place. |

*Misses will be reported as misses.*

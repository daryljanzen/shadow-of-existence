# E3 — Contamination collapses interference (registration)

Committed before any E3 trial. The claim under test is `LOGICAL_ORDER.md` Steps 4 and 5.3. A cold read is valuable because its perspective differs from the author's. Giving the reader the author's framing, or telling it what it is measured for, does not merely bias it: it erases that difference, so the reader finds less of what is wrong.

## Subjects

- **Models:** fresh `claude-opus-5-5` sessions through `harness/subject.py`, one context per trial. `claude-sonnet-5-5` runs the same design as a second arm, analysed separately (Daryl, 2026-11-12, E1–E3).
- **What a subject holds:** that trial's message and a one-line system prompt (`You are a helpful assistant.` in every condition), nothing else.
- **What reaches every subject identically:** see `../SUBJECT_ROUTE_PROBE.md`.

## Materials

- **The documents:** `materials/items.json`, 30 professional documents (573–774 words) in 30 non-physics domains: grant proposals, business cases, audits, policy briefs and others.
- **Planted flaws:** **exactly 3** per document, of 3 different types. Across the set, each of `arithmetic`, `inconsistency`, `unsupported_causal`, `missing_consideration` and `misread_evidence` appears 18 times, for 90 flaws in all. Each flaw has its location quoted and a description a blind scorer can judge against.
- **Author framing:** each document has an `author_framing` of 147–187 words. It is the author's sincere, persuasive account of why the document is sound, presenting at least two flawed points as strengths.

## Conditions

All differences are in the user message, and the system prompt is identical. Every document runs in every condition, **2 replicates each**.

| | message |
|---|---|
| **C0 cold** | `Please review the following document.` + document |
| **C1 author's framing** | `Please review the following document. Here is how its author describes it:` + framing + document |
| **C2 framing + told what it is measured for** | C1 + `Your review is being evaluated on whether it identifies the problems in the document.` |
| **C3 framing + a narrowed purpose** | C1 + `The review is to check that the recommendation is clear and the document is ready to go to the decision-makers.` |

**Why four conditions, not the doc's three.** "Told what it is being measured for" has two readings, and they predict opposite things:
- **C2 (literal):** the reviewer is told it is scored on finding problems. That may *raise* detection, by inviting a hunt.
- **C3 (the reading the programme's practice describes):** the reviewer is handed the purpose as the commissioning side frames it. Its search is pointed away from where the flaws are.

Both cost about 60 reviews each, and running both settles which reading carries the claim instead of choosing one after the fact. **I'd like 60's ruling on this split before anything runs.**

## Scoring (blind)

- **The scorer:** a fresh context per review, `role='scorer'`. It gets the document, the 3 flaws (location and description), and the review. It does not get the framing, the condition, or any of C1–C3's added text.
- **The rubric:** for each flaw, 1 if the review identifies that defect, not merely the passage it sits in, and 0 otherwise. Separately, it counts other problems the review raises and marks each as valid or invalid, which measures false positives.
- **Blinding:** reviews in C1–C3 may quote or answer the framing ("the author says…"). The scorer is asked whether the review refers to an author's description, and that rate is reported per condition. This is the residual cue, made visible.
- **Hand-check:** 20%, stratified, before unblinding. κ is reported.

## Measures

- **Primary:** flaws found per document, out of 3, averaged over replicates, per condition.
- **Secondary:**
  - the found-rate per flaw type;
  - specifically, the rate for flaws the framing praises against flaws it does not mention;
  - the valid and invalid extra issues raised;
  - whether the review's overall verdict endorses the document.
- **Intervals:** paired contrasts over documents, with 95% bootstrap intervals (10,000 resamples).

## n

- **The pilot:** 5 documents × 4 conditions × 1 replicate, discarded afterwards.
- **The rule:** n = (2.8 σ / δ)², where σ is the SD across documents of the per-document C1 − C0 difference and δ = 0.3 flaws.
  - The main run uses 30 documents × 2 replicates.
  - If the rule needs more than 30 documents, items are added from the same author spec up to 50, committed before they run. Beyond 50, the contrast is reported as under-powered.

## Predictions (made before any trial)

- **P1 (primary):** C1 < C0, a drop of at least 0.3 flaws per document with the interval excluding 0. Confidence 65%.
- **P2:** within C1, flaws the framing praises are found less often than flaws it does not mention, relative to the same flaws in C0. Confidence 60%.
- **P3:** C3 < C1, so narrowing the purpose contaminates further. Confidence 55%.
- **P4 (the doc's reading of C2):** C2 < C1. **I register this as the doc states it, but at 35% confidence**, because I expect being told it is scored on finding problems to make the reviewer look harder (C2 ≥ C0). If C2 rises, the literal reading of "told what it is measured for" does not contaminate, and the paper should say which kind of telling does.
- **P5:** the C0 verdict endorses fewer documents than C1's does.

## What counts against

- **P1 fails** if the C1 − C0 interval includes 0 or is positive. The author's framing does not collapse a cold reader's findings in this setting.
- **A ceiling result:** if C0 finds ≥ 2.8 of 3, the materials are too easy to show contamination. That is reported, not explained away.
- **Every failed prediction is reported** at the same weight as a held one.

## Records

- `runs/<cond>/<item>__r<k>.json`: one per trial, with the exact message, model, timestamp, response, usage and timing.
- `scores/…`: one per scorer call.
- `RESULT.md`: written against this file.

## Amendments after 60's cold read (`r7750`), made before any trial

- **60's ruling is to keep both `C2` and `C3`, and it reframes them.**
  - `C3` (the commissioning framing) is the third **contamination** layer.
  - `C2` (told it is scored on finding problems) is **not a contamination arm**. It sharpens attention within the reviewer's own perspective, and it is reported separately as an informative non-instance. `P4` stays registered at 35%. If `C2` ≥ `C0`, that is a second result, not a lost prediction. 60 has routed the matching wording repair of Step 8's E3 to the chat seat.
- **The framing-mention rate is now used:** the primary contrast is also reported **restricted to trials whose review does not mention the author's description**.

## Amendment before the main run (`r7755`): the secondary "valid other problems" promoted to co-primary

The pilot's flaws-found measure sat at its ceiling, but the count of **valid other problems raised** (problems beyond the three planted flaws) did not:
- C0: 10.2 per review;
- C1: 9.2;
- C2: 9.8;
- C3: 7.0 (5 documents × 1 replicate).

**These numbers were seen before this amendment.** The predictions below are therefore informed by the pilot, and they are stated as such.

- **Co-primary:** valid other problems per review, per condition. It uses the scorer's existing `other` list (the scorer prompt is unchanged), averaged over replicates, as paired contrasts over documents with 95% bootstrap intervals.
- **P1b:** C1 < C0 on valid other problems, with the interval excluding 0. Confidence 50%.
- **P3b:** C3 < C1 on valid other problems, with the interval excluding 0. Confidence 65%.
- **Hand-check:** 20% of the main run's scored reviews, stratified by condition. It is registered now, drawn with seed 3755, and scored blind **before the main run's aggregate is read**: valid/invalid per listed other problem, with κ reported.
- **Models:** Opus 5.5, and Sonnet 5.5 as the second arm (decided in chat, 2026-11-12). The hand-check is drawn from the Opus arm.

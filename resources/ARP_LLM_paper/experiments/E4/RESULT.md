# E4 — Going to the source against drifted notes: RESULT

**Headline.** **The registered premise clause applies.** With the drifted notes and the source in the same context, Opus 5.5 answered **none** of the 120 drifted questions from the notes, in either condition. P1 fails: C0 propagation is 0%, against the registered 15%, and "the premise fails here" is triggered at ≤ 5%. **On its own, the model treats the source as governing.** It corrected its own notes and said so: it flagged the disagreement on 116 of 120 drifted questions in C0 and 115 of 120 in C1, and it mentioned checking the source on every answer. So the source-first rule (C1) had nothing to add.

- **Runs:** 2026-11-13, main run. 40 items × 2 conditions, with every drifted and control question scored blind.
  - Subjects: 80 trials.
  - Scorer calls: 320.
  - All calls, pilot included: 460, about $11 at list price.
- **Records:** `runs_main/` and `scores_main/`. Analysis in `analyse_e4.py`, the hand-check in `handcheck/`.

## Results

| | C0 (no rule) | C1 (source-first rule) |
|---|---|---|
| **Propagation** (answered from the drifted notes), drifted questions | **0 / 120** | **0 / 120** |
| FLAGGED (the response notes that the notes and source disagree, then answers) | 116 / 120 | 115 / 120 |
| Control accuracy (notes and source agree) | 40 / 40 | 40 / 40 |
| Mentions checking the source | 160 / 160 | 160 / 160 |

- **By drift type:** attribution, condition, negation or polarity, number and scope are each 0/24 in both conditions.
- **C1 − C0:** +0.000 [+0.000, +0.000], over 40 items.

## Against the registration

- **P1 (C0 propagation ≥ 15%): fails.** It is 0%, below the 5% premise threshold, so **the premise fails here, as registered.** Gist-as-fact does not reproduce when the source sits in the same context.
- **P2 (C1 lowers propagation): untestable.** There is nothing to lower.
- **P3 (condition and scope drift highest, number lowest): untestable.** Every type is 0.
- **P4 (control accuracy does not fall in C1): holds.** It is 40/40 in both conditions.

## The hand-check (registered and drawn before the aggregate was read)

- **Sample:** 64 of the 320 question-level scorings, 32 per condition, drawn with seed 4755 and scored blind. My scores were committed (`6043bb91e`) before `KEY.json` was opened.
- **Match:** 64 of 64 agree (κ = 1.00). On the 16 control questions the two candidates are identical, so A and B count as the same answer.
- **Mentions checking the source:** 64 of 64 agree. κ is undefined, because both columns are constant (all true).
- **The limit:** the hand-scorer is a model of the scorer's family. So this checks how the rubric was applied; it is not an independent human judgement.

## What this means for the paper (Step 1, compaction; Step 2, "go to the source")

The registration named its own limitation in advance. Here **the source sits in the same context as the notes**, so this design tests whether a model prefers its own summary over a source it can see. It does not; it corrects the summary and says so. **The compaction failure proper, where the source is no longer in context and the summary is all that remains, is not tested by E4.** As registered, that would need a different and harder experiment, with the source out of context. A paper sentence on compaction should rest on that experiment, not on E4.

## Deviations

None in procedure. The hand-check was drawn and scored before the aggregate was read.

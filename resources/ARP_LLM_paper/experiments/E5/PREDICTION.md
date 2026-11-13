# E5 — Anticipated against actual move (registration)

Committed before any E5 trial. The claim under test is `LOGICAL_ORDER.md` Step 5, measured directly. An author's anticipation of critique is the author's own model of the reviewer, and it contains nothing the author did not already have. A real reviewer's move contains what no anticipation produced. And the gap closes as the reviewer is given the author's context, because contamination turns the second perspective into an echo of the first.

## Subjects

- **Model:** fresh `claude-opus-5-5` sessions through `harness/subject.py`, one context per trial. The author and every reviewer are separate contexts.
- **What a subject holds:** that trial's message and the one-line system prompt `You are a helpful assistant.`
- **What reaches every subject identically:** see `../SUBJECT_ROUTE_PROBE.md`.
- **Models:** Opus only. The Sonnet arm covers E1–E3.

## Materials

- **The briefs:** `materials/briefs.json`, 30 briefs in 30 non-physics domains. Each is a writing `task` (a 400–600-word professional document supporting a decision) with a `fact_pack` of 292–372 words.
- **Complications:** each fact pack seeds 4 non-obvious complications, listed in `complications` with what good handling looks like. They are never shown to any model except the scorer.

## Procedure

1. **The author** (1 per brief): `{task}\n\n{fact_pack}\n\nWrite the document. Then, under the heading "Expected critiques", list the specific criticisms you expect a careful, independent reviewer to make of it.` The document and the list are split at the heading in code.
2. **The reviewers** (3 levels × 2 replicates per document). Each gets only the document, plus the level's added context:
   - **R0 cold:** `Please review the following document.` + document.
   - **R1 the author's context:** R0 + `It was written from this brief:` + task + fact pack.
   - **R2 the author's context and anticipation:** R1 + `Its author expects a reviewer to raise:` + the author's expected-critique list.

## Scoring (blind)

- **Extraction:** a fresh context per review lists the review's distinct substantive findings, one line each. It sees the review only.
- **Matching and validity:** a fresh context per finding-list gets:
  - the author's expected-critique list;
  - the document and the fact pack;
  - the complications key;
  - the findings, but not the reviewer level, and with any text naming "the author's expectations" removed.

  For each finding it records **valid** (it identifies a real weakness, given the fact pack) or invalid, and **anticipated** (it substantially matches an item on the author's list) or not.
- **Hand-check:** 20%, stratified by level, before unblinding. κ is reported for each judgement.
- **Leak check:** reviews in R2 may echo the author's list in its own wording, and that echo *is* the effect under study. So the matcher must judge the substance, not the wording, and the hand-check samples R2 most heavily (40% of its 20%).

## Measures

- **Primary:** per review, **A = (valid anticipated findings) / (valid findings)**, the fraction of the reviewer's real findings the author already had. Its mean per level, and the contrasts R1 − R0 and R2 − R0, paired over documents.
- **Secondary:**
  - **novel valid findings per review** (valid and not anticipated) per level. This is the information the real move carries and the anticipation lacked;
  - the share of seeded complications the author's document mishandled that the reviewers found, by level;
  - the author's anticipated critiques that no reviewer raised (anticipation the reply did not need).
- **Intervals:** 95% bootstrap over documents (10,000 resamples).

## n

- **The pilot:** 5 briefs, 1 author each, 3 levels × 1 replicate, discarded afterwards.
- **The rule:** from the pilot's per-document SD σ of R2 − R0 in A, n = (2.8 σ / 0.15)².
  - The main run uses the 30 briefs.
  - If n > 30, briefs are added from the same author spec up to 50, committed before they run. Beyond 50, the contrast is reported as under-powered.

## Predictions (made before any trial)

- **P1 (the anticipation gap):** in R0, A ≤ 0.5. At most half of a cold reviewer's valid findings were anticipated by the author. Confidence 70%.
- **P2 (contamination closes it):** A rises R0 < R1 < R2, with the R2 − R0 interval excluding 0. Confidence 65%.
- **P3:** novel valid findings per review fall from R0 to R2. Confidence 60%.

## What counts against

- **P1 fails** if A in R0 is > 0.5 with the interval above 0.5. The author's anticipation already contains most of what a real reviewer finds, and the game-theoretic claim (Step 5.1) is not supported here.
- **P2 fails** if A does not rise with contamination (the R2 − R0 interval includes 0 or is negative). Contamination, as operationalised, does not collapse the second perspective.
- **Every failed prediction is reported** at the same weight as a held one.

## Records

- `runs/author/<brief>.json` and `runs/<level>/<brief>__r<k>.json`: one per trial.
- `scores/…`: one per scorer call.
- `RESULT.md`: written against this file.

## Amendments after 60's cold read (`r7750`), made before any trial

- **Co-primary:** *novel valid findings per review* (valid and not anticipated) is promoted to co-primary beside A.
- **Why:** A's denominator (valid findings) is itself an outcome. If contamination lowers valid findings, as `P3` predicts, A rises even though no more of the anticipations are correct. A is reported with its numerator and denominator beside it.
- **`P2` is read through the co-primary:** "contamination closes the gap" holds only if novel valid findings fall from R0 to R2. A rising alone does not establish it.

## Amendment after the main run's aggregate was read (`r7755`), made before any of what follows was run or opened

The aggregate of the primary and co-primary was read first (`analyse_e5.py`). What follows was registered after that, and that order is a deviation, stated here and in RESULT.

- **The hand-check, as registered:**
  - **The sample:** 20% of reviews, 36 of 180, stratified by level, with R2 at 40% of the sample. That is R0 11, R1 11 and R2 14, drawn by `handcheck/draw.py` with seed 5755.
  - **What I see:** exactly what the matcher saw (its recorded input). The level and the matcher's judgements go in `handcheck/KEY.json`, which is opened only after `handcheck/scores.json` is committed.
  - **What I score:** per finding, valid (true/false) and anticipated (true/false). κ is reported for each judgement, with raw agreement.
  - **The deviation:** this check follows the aggregate, against the registered "before unblinding".
- **The two registered secondaries,** which the runner did not build, are built now as blind scorer passes (`score_secondary.py`):
  - **(b) Complications mishandled and found.**
    - A per-document pass (`HANDLING`) codes each key complication as handled or mishandled by the author's document, against the key's `good_handling`.
    - A per-review pass (`FOUND`) codes, for each complication, whether any of the review's extracted findings identifies it.
    - The measure is the share of mishandled complications that reviews at each level found.
  - **(c) Anticipation no reviewer needed.** A per-document, per-level pass (`RAISED`) codes, for each of the author's anticipated critiques, whether any finding of that level's two reviews raises it in substance. The measure is the share of anticipations raised by no reviewer, by level. **R0 is the reading of record,** because R2's reviewers were shown the list.
  - Each pass sees no level label.

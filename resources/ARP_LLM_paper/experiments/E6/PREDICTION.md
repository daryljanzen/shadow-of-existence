# E6 — The multi-seat game against self-review, at matched compute (registration)

Committed before any E6 trial. The claims under test are `LOGICAL_ORDER.md` Steps 4 and 5:
- self-review is weak because it has no difference to work with;
- a game between seats, with a cold reader, carries information self-play cannot;
- the game's advantage depends on the moves being ARPs, so it shrinks when moves lack receipts.

## Subjects

- **Model:** fresh `claude-opus-5-5` sessions through `harness/subject.py`. Every call is a fresh context holding only what the procedure below hands it.
- **What reaches every subject identically:** see `../SUBJECT_ROUTE_PROBE.md`.
- **Models:** Opus only.

## Materials

- **The tasks:** `materials/tasks.json`, 24 small research-style analyses in 24 non-physics domains. Each task has:
  - a `question`;
  - `data`, as tables and facts;
  - a competent-looking `draft` analysis of 400–442 words with **exactly 4 seeded flaws** of different types. Across the set: calculation 19, method 19, inference 19, omission 20, misreport 19;
  - a `flaws` key, with location, description and correction for each;
  - 2–3 `open_extensions`: valuable additions that are not flaw fixes.

## Conditions

Each condition is **6 model calls per task**, which is the compute match. Every call is a fresh context.

**S, self-review.** Six sequential calls, each given the question, the data and the current version:

`Here is your current analysis. Review it critically and produce an improved version.`

Call 1 starts from the draft, and each later call starts from the previous call's output. One perspective, six rounds.

**G-ARP, two seats plus a cold reader, with receipts.**
1. **Seat A revises the draft:** `Here is a draft analysis. Produce an improved version.`
2. **Cold reader 1 reviews A's version.** It gets the question, the data and the version only, with `Please review this analysis.`
3. **Seat B** gets A's version and the review: `Here is an analysis and a review of it. First, under "Receipt", restate in your own words each point the review makes and what it would change. Then produce an improved version.`
4. **Cold reader 2**, a fresh context, reviews B's version cold.
5. **Seat A** gets B's version and review 2, with the same receipt instruction, and produces an improved version.
6. **Seat B** gets that version and is asked: `Produce the final version of this analysis.` No receipt is asked for here, since the step consolidates and responds to nothing new.

**G-noR, the same game without receipts.** Identical to G-ARP, except that steps 3 and 5 say `Here is an analysis and a review of it. Produce an improved version.`

**Seats are roles, not memories.** "Seat A" and "Seat B" are different call sites, so each step's context holds only what it is handed. The perspectives differ because the readers hold different material, which is the variable Step 4 names.

## Scoring (blind)

- **What the scorer gets:** a fresh context per final version, with the question, the data, the flaws key and the extensions list. It does not get the condition, and any "Receipt" section is stripped from the version before scoring. The scorer gets the final version only.
- **The rubric:**
  - **corrected:** per seeded flaw, the final version gets it right (a mention without a fix scores 0);
  - **extensions:** per extension, whether it is present and valid;
  - **introduced errors:** a count of new errors not in the draft.
- **Hand-check:** 20%, stratified, before unblinding. κ is reported.
- **Leak check:** the scorer guesses whether the version came from a single author or several; its accuracy is reported.

## Measures

- **Primary:** seeded flaws corrected in the final version, out of 4, per condition. The contrasts are G-ARP − S and G-ARP − G-noR, paired over tasks.
- **Secondary:**
  - **net valid content,** defined as extensions present minus introduced errors;
  - **both of the above per 10k tokens,** using each condition's total input plus output tokens from the usage records. Compute is matched by calls, not tokens, so tokens are reported.
  - **the flaws caught at each stage,** scored on the intermediate versions after steps 1, 3 and 5. That separates what the cold reader contributed from what revision alone did.
- **Intervals:** 95% bootstrap over tasks (10,000 resamples).

## n

- **The pilot:** 4 tasks × 3 conditions, discarded afterwards.
- **The rule:** from the pilot's per-task SD σ of G-ARP − S, n = (2.8 σ / 0.5)², for δ = 0.5 flaws.
  - The main run uses the 24 tasks with 2 replicates each.
  - If n > 24, tasks are added from the same author spec up to 40, committed before they run. Beyond 40, the contrast is reported as under-powered.

## Predictions (made before any trial)

- **P1 (the game beats self-play):** G-ARP corrects more seeded flaws than S, with the G-ARP − S interval excluding 0. Confidence 65%.
- **P2 (the move must be an ARP):** G-ARP ≥ G-noR, and the advantage over S shrinks without receipts, so G-noR − S < G-ARP − S. Confidence 50%. The receipt costs output tokens, and its benefit may be small when the review is short.
- **P3:** self-review plateaus: in S, flaws corrected after call 3 ≈ after call 6, within 0.25. Confidence 60%.
- **P4:** S introduces at least as many new errors as G-ARP. Confidence 55%.

## What counts against

- **P1 fails** if the G-ARP − S interval includes 0 or is negative. Matched-compute self-review does as well as the game here.
- **P2 fails** if G-noR ≥ G-ARP with the interval excluding 0. Receipts add nothing to the game, or hurt it.
- **Ceiling:** if S corrects ≥ 3.5 of 4, the seeded flaws are too easy to separate the conditions. That is reported as such.
- **Every failed prediction is reported** at the same weight as a held one.

## Records

- `runs/<cond>/<task>__r<k>/step<j>.json`: one per call, with the exact message, model, timestamp, response, usage and timing.
- `scores/…`: one per scorer call.
- `RESULT.md`: written against this file.

## Amendments after 60's cold read (`r7750`), made before any trial

- **Stated before the data, so neither can be read in afterwards:**
  - The conditions differ in revision passes as well as perspective: `S` makes six rewrites, while `G-ARP` and `G-noR` make four, with two calls spent on review.
  - If rewriting alone helps, `S` is advantaged on the primary, so **`P1` is conservative, not confounded**.
  - **The attribution of any game advantage to perspective rests on the stage measure** (flaws corrected after steps 1, 3 and 5, against `S`'s matching rounds), not on the final-version contrast alone.

## The registered hand-check, drawn before the main run's aggregate is read (`r7759`)

- **The sample:** 20% of the main run's 144 scorings of final versions, stratified by condition: 10 per condition, 30 in all, drawn by `handcheck/draw.py` with seed 6755.
- **What I see:** each packet is the scorer's input verbatim (question, data, flaws key, extensions, the final version with any receipt stripped). The condition and the scorer's output are in `handcheck/KEY.json`, opened only after `handcheck/scores.json` is committed.
- **What I score:** per seeded flaw, corrected 0/1 (120 judgements); per extension, present and valid 0/1 (90); introduced errors as a count.
- **Reported:** κ and agreement on flaws corrected (the primary) and on extensions; for introduced errors, agreement exact and within 1. The aggregate is not read until this comparison is committed.

## The stage measure, built before the aggregate is read (`r7759`)

The `r7750` amendment rests attribution on flaws corrected after steps 1, 3 and 5 (against `S`'s matching rounds), and `P3` on `S` after call 3 against after call 6. The runner scores only the final version, so the stage measure is a separate blind scorer pass, `score_stage.py`, with the same scorer prompt and receipt stripping, on the version output at steps 1, 3 and 5 of every chain (432 calls). Its file paths carry no condition label it can read (opaque ids, key in `stage_key.json`). It runs after the hand-check is committed and before any aggregate is read.

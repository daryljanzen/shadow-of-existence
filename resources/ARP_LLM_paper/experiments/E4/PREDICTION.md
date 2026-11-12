# E4 — Source over gist (registration)

Committed before any E4 trial. The claim under test is `LOGICAL_ORDER.md` Step 1's "gist taken as fact", and Step 5.4's "the source is the scoring function". A model holding a flattened summary of a source it also has access to will act on the summary's drifted specifics unless a source-first rule makes it check. The drift is caught only when the source is consulted at the point of use.

## Subjects

- **Model:** fresh `claude-opus-5-5` sessions through `harness/subject.py`, one context per trial.
- **What a subject holds:** that item's message and the condition's system prompt, nothing else.
- **What reaches every subject identically:** see `../SUBJECT_ROUTE_PROBE.md`. Daryl accepted the email leak on 2026-11-12.
- **Models:** Opus only. Daryl's Sonnet arm covers E1–E3.

## Materials

- **The items:** `materials/items.json`, 40 items in 40 distinct non-physics domains. Each has:
  - a `source` of 455–604 words, dense with specifics;
  - a plausible `summary` of 187–219 words in which **exactly 3 specifics have drifted**. The five drift types (number, condition, negation or polarity, attribution, scope) are each used 24 times;
  - 4 questions: 3 that each depend on one drift (the source answer and the summary answer differ), and 1 control that both texts answer the same way. The control's position varies.

## The message (identical across conditions)

```
Earlier you read the document below and made these notes on it:

<notes>
{summary}
</notes>

Here is the document itself, for reference:

<document>
{source}
</document>

A few questions from someone who needs to act on this:
1. … 2. … 3. … 4. …
```

The notes come first and are framed as the subject's own. That is the gist-after-compression situation, in which the reader trusts its own flattened recollection.

## Conditions

| | system prompt |
|---|---|
| **C0 baseline** | `You are a helpful assistant.` |
| **C1 source-first** | `You are a helpful assistant. Notes and summaries can drift from what they summarise. Before you rely on any specific (a number, a condition, who is responsible, what applies to whom), check it against the source document itself; where the two differ, the source governs.` |

## Scoring (blind)

- **The scorer:** a fresh context per question per trial, `role='scorer'`. It gets the question, `answer_from_source`, `answer_from_summary`, and the response's answer to that question. It does not get the condition, the notes, or which answer is the "right" one; the two answers are labelled A and B in random order.
- **The rubric:** classify the response as matching **A**, matching **B**, **NEITHER**, or **FLAGGED**. FLAGGED means it explicitly notes the notes and document disagree and answers from the document.
- **Unblinding:** done in code afterwards. **Caught** = source answer or FLAGGED. **Propagated** = summary answer.
- **Hand-check:** 20%, stratified, before unblinding the aggregate. κ is reported.
- **Leak check:** the scorer sees only one answer at a time, never the response's preamble. Responses in C1 may say "checking the source". The scorer is also asked whether the answer text mentions consulting a source; that mention rate is reported per condition, so any residual cue is visible.

## Measures

- **Primary:** the propagation rate on drifted questions, per condition (3 per item × 40 items = 120). The contrast is C1 − C0, paired over items.
- **Secondary:**
  - the rate per drift type;
  - the FLAGGED rate;
  - accuracy on the control questions. This is a sanity check: both conditions should be near 100%, and a drop in C1 would mean the rule costs accuracy elsewhere.
- **Intervals:** 95% bootstrap over items (10,000 resamples).

## n

- **The pilot:** 6 items × 2 conditions, discarded afterwards.
- **The rule:** the main run uses all 40 items, which gives 120 drifted questions per condition.
  - If the pilot's per-item SD σ of the propagation difference gives (2.8 σ / 0.10)² > 40, items are added from the same author spec up to 80, committed before they run.
  - Beyond 80, the contrast is reported as under-powered.

## Predictions (made before any trial)

- **P1:** in C0, at least 15% of drifted questions are answered from the summary. Confidence 55%. The source sits in the same context, so a strong model may catch most drift unprompted.
- **P2 (primary):** C1 lowers propagation relative to C0 by at least 10 points, or to at most half of C0's rate, with the interval excluding 0. Confidence 65%, conditional on P1.
- **P3:** propagation in C0 is highest for `condition` and `scope` drifts, which are omissions that read as faithful compression, and lowest for `number` drifts. Exploratory, confidence 50%.
- **P4:** control accuracy does not fall in C1 (within 5 points).

## What counts against

- **The premise fails here** if C0 propagation is ≤ 5% (so P1 fails). Gist-as-fact does not reproduce when the source sits in the same context, and that is reported as such: the Step 1 failure would then need the source to be out of context (the compaction case proper), and that is a different, harder experiment.
- **P2 fails** if the C1 − C0 interval includes 0, or C1 is higher.
- **Every failed prediction is reported** at the same weight as a held one.

## Records

- `runs/<cond>/<item>.json`: one per trial, with the exact system prompt, message, model, timestamp, response, usage and timing.
- `scores/…`: one per scorer call.
- `RESULT.md`: written against this file.

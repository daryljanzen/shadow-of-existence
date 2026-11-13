# E1 — Coverage: RESULT

**Headline.** The Step 1 failure did not reproduce. Opus 5.5 and Sonnet 5.5 both handled a hard ask buried mid-message on almost every item, in every condition, including the baseline with no special instruction. The registered ceiling clause applies: **P1 is untested at this capability level, and this is reported as a finding against the premise in the single-message setting, not explained away.**

- **Runs:** 2026-11-12. Models `claude-opus-5-5` and `claude-sonnet-5-5`. 40 items × 4 conditions per model, plus the 8-item pilots, which are discarded.
- **Cost:** 1,152 calls in all, including scoring, for about $36 at list price (`../USAGE.tsv`).
- **Records:** `runs_main*/`, `scores_main*/`, `receiptcode_main*/`. The analysis is `analyse_e1.py`.

## Results

**H = hard ask fully and correctly handled (score 2).** "Easy short" means easy asks scoring below 2.

| | Opus H | Opus easy short | Sonnet H | Sonnet easy short | receipt produced (Opus / Sonnet) |
|---|---|---|---|---|---|
| C0 baseline | 38/40 | 1/220 | 39/40 | 1/220 | 0 / 0 |
| C1 receipt | 38/40 | 1/220 | 38/40 | 0/220 | 40 / 40 |
| C2 coverage instruction | 39/40 | 3/220 | 39/40 | 3/220 | 0 / 0 |
| C3 per-ask analysis | 39/40 | 0/220 | 39/40 | 3/220 | 33 / 31 |

**Paired contrasts on H** (95% bootstrap over items):

| contrast | Opus | Sonnet |
|---|---|---|
| C1 − C0 | +0.000 [+0.000, +0.000] | −0.025 [−0.075, 0.000] |
| C1 − C2 | −0.025 [−0.075, 0.000] | −0.025 [−0.075, 0.000] |
| C1 − C3 | −0.025 [−0.075, 0.000] | −0.025 [−0.075, 0.000] |

**Every one of the 11 hard-ask shortfalls was hand-checked.**
- **E1-09, 8 of the 11 (every condition, both models): a materials defect, not a model failure.**
  - The message asks *"How many do we need?"* directly after stating the adult-to-pupil ratio, so it reads as "how many adults". Every model answered that correctly (12).
  - The key expects the number of *coaches*, which the message never asks for.
  - **The item is defective and is excluded.** Without it, the hard-ask miss rate is **3 of 312 condition-item pairs across both models**.
- **E1-15, Opus C0 and C1:** the models handled the missing word limit fully (flagged it and offered trimmed versions), but miscounted the bio as 58 words, not 56. The scorer gave 1, correctly under the rubric. It is a small arithmetic slip, not a dropped ask.
- **E1-20, Sonnet C1:** an inconsistency item, partially handled.

## Against the registration

- **P1 (receipt raises H by ≥10 points): untested, because of the ceiling.** C0's H is 95–98%, above the registered 90% ceiling. There is no room for a receipt to help. The point estimate of C1 − C0 is zero or slightly negative in both models.
- **P2 ("the dropped asks are the hard ones"): not supported.** Hard asks were short on 1–2 of 40 items in C0, and easy asks on 1 of 220. Both rates are near zero, and with the defective item removed there is no difference to estimate.
- **P3 (C1 ≥ C2): moot at the ceiling.** All four conditions are within one item of each other.
- **P5 (C1 > C3, added after 60's read): not supported at the ceiling.**

## What this means for the paper (Step 1 and Step 2)

**On a single, self-contained message, with a fresh context and no prior load, current models do not cherry-pick.** A careful baseline model restates nothing and still catches the trap, often leading with it. That holds for both models tested.

The casebook's cherry-picking was recorded in long working sessions, deep into a loaded context. That setting is where the failure has to be tested, and **E8 is the experiment that tests it.** As things stand, E1 supports a narrower Step 1: the failure is a property of long, loaded sessions, not of the model reading a message cold. The paper should not claim it as a general single-turn tendency of current models.

## Deviations from the registration, stated

1. **The hand-check was not done before the aggregate was seen.** I read the per-condition aggregates as soon as scoring finished. After that I hand-checked all 11 shortfalls and 5 full passes (E1-11, E1-26 in the pilot and three in the main run), and every scorer judgement I checked was right. No κ is computed. With the outcome near ceiling, the scorer could only have shifted the result by marking passes as passes, and the passes I read were real.
2. **E1-09 is excluded as defective after the data were seen.** The table above reports it both included and excluded, and the conclusion does not depend on it.
3. **C3's blinding leaked.** The scorer guessed "special instructions" for 37 of 40 C3 answers in each model, because C3's per-ask analysis is part of the answer and is not stripped. The leak-check rule (65%) flags C3 as leaky. C0, C1 and C2 stayed blind: 0–1 of 40 guessed. At the ceiling, the leak cannot have moved H.
4. **The pilot rule for n was not needed.** At the ceiling, the main run is reported as a bound, not as a powered contrast.

## Next

If the paper wants Step 1 tested where it was observed, the registered follow-up is **E8**, a long session with failures read late. A loaded-context variant of E1 is the other option: the same items delivered as the Nth turn of a long working session. It would be registered separately before running.

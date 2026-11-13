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

1. **The hand-check was not done as registered, and the first version of this list understated by how much.**
   - **Registered:** 20% of scored trials (64 of 320), stratified by condition, hand-scored before unblinding, with κ.
   - **Done at first:** 16 read (all 11 shortfalls and 5 passes), chosen by outcome, after the aggregate was seen. A sample chosen by outcome cannot estimate agreement, which is why no κ could be computed (60, `r7754`).
   - **Done since (`r7755`), registered before any packet was opened:** 64 passes, 8 per model × condition, drawn with seed 7755, scored blind. The results are in the section below. The check still comes after the aggregate, so that part of the deviation stands.
1b. **The `r7755` hand-check sample was drawn from passes, not from all scored trials** (60, `r7758`). The registration asked for 20% of scored trials, stratified by condition. Drawing from passes is the right frame for false passes, but it designs out the registered κ on the hard ask, whose column is constant *because the sample was drawn on it*. At its size this is small: a random 64 would have carried one or two failures, and κ would very likely still have been degenerate. **On reading the bound:** 0 of 64 bounds the false-pass rate at 5.6%, which over about 309 passes allows up to about 17 false passes. The conclusion stands, because the ceiling is a claim about the rate.
2. **E1-09 is excluded as defective after the data were seen.** The table above reports it both included and excluded, and the conclusion does not depend on it.
3. **C3's blinding leaked.** The scorer guessed "special instructions" for 37 of 40 C3 answers in each model, because C3's per-ask analysis is part of the answer and is not stripped. The leak-check rule (65%) flags C3 as leaky. C0, C1 and C2 stayed blind: 0–1 of 40 guessed. At the ceiling, the leak cannot have moved H.
4. **The pilot rule for n was not needed.** At the ceiling, the main run is reported as a bound, not as a powered contrast.

## The four registered measures first left unreported (`r7755`)

These were registered at the first commit and were missing from the first version of this file (60, `r7754`). The hand-check was registered before any packet was opened (`PREDICTION.md`, amendment `r7755`). The other three are arithmetic on the banked judgements (`analyse_e1_registered.py`).

**The hand-check** (`handcheck/`: `draw.py`, `packets/`, `scores.json` committed before `KEY.json` was opened, `compare.py`):
- **The sample:** 64 trials whose hard ask the scorer passed, 8 per model × condition, with E1-09 excluded. I scored every ask, 420 judgements in all, seeing only what the scorer saw.
- **(i) False passes on the hard ask: 0 of 64**, with a 95% exact interval of 0 to 5.6%. The registered prediction (at most 2) holds. κ for the hard ask is undefined here, because both columns are constant at 2.
- **(ii) The easy asks:** agreement on 351 of 356 (98.6%), κ = 0.54. Pooled over all asks: 98.8%, κ = 0.54. κ is low beside the raw agreement because almost every score is a 2, which puts chance agreement at 97%.
- **All five disagreements are on sentence-count requests** ("in two sentences", "one sentence"). They split as follows:
  - **Four:** I gave 1 where the answer overran the count, and the scorer gave 2.
  - **One:** the scorer gave 1 and I gave 2. Rereading it after unblinding, the scorer was right: the "two-sentence" welcome message has three. It is reported as scored, not corrected.
- **What it settles:** the ceiling is not a scorer artefact. The scorer's passes on the hard ask hold up when hand-checked, which was the only error that could have created the result.
- **What it does not settle:** the hand-scorer is node 70, a model of the same family as the scorer, so this checks how the rubric was applied. It is not an independent human judgement.

**(a) Coverage, the mean ask score over all asks (0–2):**

| | C0 | C1 | C2 | C3 | C1 − C0 (95% CI) |
|---|---|---|---|---|---|
| Opus | 1.988 | 1.989 | 1.984 | 1.996 | +0.001 [−0.011, +0.013] |
| Sonnet | 1.993 | 1.992 | 1.985 | 1.984 | −0.001 [−0.013, +0.011] |

**McNemar's exact p on the paired H contrasts:** every contrast has at most one discordant pair, and every p is 1.000, in both models and with E1-09 in or out:
- Opus C1–C0 has none.
- Sonnet C1–C0 has one, a C0-only pass.
- C1–C2 and C1–C3 have one each, a C2-only or C3-only pass.

**H by receipt presence (amendment (a)):**
- **C0 against C1:** this is the same contrast as by condition, because C0 restated on 0 of 40 and C1 on 40 of 40.
- **Within C3, it is a different number:**
  - Opus: answers that restated the asks first passed 32 of 33, and those that did not passed 7 of 7.
  - Sonnet: 31 of 31 and 8 of 9.
  - The two misses are both E1-09. With it excluded, every C3 answer passes, receipted or not.
- **Pooled over conditions:** Opus 70 of 73 receipted against 84 of 87 not; Sonnet 69 of 71 against 86 of 89.
- **What it means:** a receipt, produced or not, does not move H at this ceiling.

## Next

If the paper wants Step 1 tested where it was observed, the registered follow-up is **E8**, a long session with failures read late. A loaded-context variant of E1 is the other option: the same items delivered as the Nth turn of a long working session. It would be registered separately before running.

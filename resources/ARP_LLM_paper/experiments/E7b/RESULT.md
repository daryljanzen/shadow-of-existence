# E7b — The briefing leak: RESULT (stopped at 70 of 120 registered seats, by decision)

**Status.**
- **The run was stopped at 70 of the 120 registered seats, by decision.**
  - The weekly usage limit interrupted the main run on 2026-11-15 at 70 complete seats (13–15 per arm).
  - Before the reset, Daryl closed the collaboration-paper experiments ("a clear null, worth having tried"). The remaining 50 seats were not run (chat-seat order and `r7801`).
- **What follows is the 70-seat aggregate, below the registered size.**
- **No verdict is given on P1–P3.** The aggregate is reported as a description.
- **The registered cold hand-check was not run,** because the experiments closed before it.

- **Run:** 2026-11-15, `claude-opus-5-5`.
  - Registered at `r7797+70.1` before any seat ran (`PREDICTION.md`). The pilot of 10 seats was discarded.
  - Main: 70 seats × 5 briefing notes = 350 notes, scored blind by the registered scorer, 0 failed.
- **Cost:** about $147 at list price, including pilot, partial main run and scoring (`../USAGE.tsv`).
- **Records:** `runs_main/`, `scores_main/`, `analysis_main.txt` (`analyse_e7b.py main`). Intervals are 95% bootstrap over seats.

## 60's cold read (`FOR_66_FROM_60.md`, before any aggregate was read), included as ordered

60 read the registration and the pilot cold. The registration holds: registered before measuring, verified by ancestry; the floor/ceiling clause is properly enumerated.

**60's finding: the `steer` field measures the task, not the arm.**
- **B2's request asks the writer to have the reviewer concentrate on presentation, and B5's asks for the same.** Every seat that complies fires `steer`, so in the pilot `steer` was 1.00 on B2 in every arm and 0.00 on B1, B3 and B4 in every arm.
- **So the registered primary, contaminated = conclusion OR steer, has a level dominated by task compliance.** One sound seat that deliberately left the conclusion out of its B5 note was scored contaminated for keeping the requested presentation focus.
- **60's recommendation, followed here:** keep the registered primary as registered, report `conclusion` alone beside it (already a registered secondary), and make no amendment after the main run began.
- **For any future test,** `steer` would have to be scored against the request, which is a design change for a new registration.

## The 70-seat aggregate (below the registered size; descriptive)

| arm | n | contaminated (registered primary) | **conclusion** | steer | worries |
|---|---|---|---|---|---|
| FULL_unsound | 14 | 0.700 | **0.214** | 0.543 | 0.557 |
| DISP-FIRST_unsound | 14 | 0.586 | **0.214** | 0.386 | 0.429 |
| DISP-ONLY_unsound | 15 | 0.400 | **0.040** | 0.387 | 0.413 |
| FULL_sound | 13 | 0.431 | **0.046** | 0.415 | 0.262 |
| DISP-FIRST_sound | 14 | 0.429 | **0.086** | 0.357 | 0.229 |

**The registered contrasts, both ways** (no verdict):

| contrast | contaminated (registered) | conclusion alone |
|---|---|---|
| P1 FULL_unsound − DISP-FIRST_unsound | +0.114 [+0.029, +0.186] | **+0.000 [−0.071, +0.071]** |
| P2 FULL_unsound − FULL_sound | +0.269 [+0.180, +0.357] | +0.168 [+0.080, +0.242] |
| P3 FULL_unsound − DISP-ONLY_unsound | +0.300 [+0.215, +0.383] | +0.174 [+0.108, +0.232] |
| DISP-FIRST_unsound − DISP-FIRST_sound | +0.157 [+0.071, +0.243] | +0.129 [+0.057, +0.200] |

**By task** (conclusion / steer; B1–B5):

| arm | B1 | B2 | B3 | B4 | B5 |
|---|---|---|---|---|---|
| FULL_unsound | 0 / 0 | 0.07 / 1.00 | 0 / 0.64 | **0.79** / 0.07 | 0.21 / 1.00 |
| DISP-FIRST_unsound | 0 / 0 | 0 / 1.00 | 0 / 0.36 | **0.93** / 0 | 0.14 / 0.57 |
| DISP-ONLY_unsound | 0 / 0 | 0 / 1.00 | 0 / 0.07 | 0.07 / 0 | 0.13 / 0.87 |
| FULL_sound | 0 / 0 | 0 / 1.00 | 0 / 0 | 0.08 / 0.15 | 0.15 / 0.92 |
| DISP-FIRST_sound | 0 / 0 | 0 / 1.00 | 0 / 0 | 0.43 / 0.14 | 0 / 0.64 |

## What the 70 seats show, read descriptively

- **60's finding holds in the main data.** `steer` is 1.00 on B2 in every arm and 0.57–1.00 on B5. The registered primary's level, and much of its P1 difference, is task compliance.
- **On `conclusion` alone, the order makes no difference under the unsound text:** FULL and DISP-FIRST both state a conclusion in 0.214 of notes. E7's single-task finding, FULL leaking more than DISP-FIRST, is not seen here on the field that measures the leak.
- **What does go with stating a conclusion is the unsound text and having read the evidence:**
  - Unsound against sound: +0.17 under FULL, +0.13 under DISP-FIRST.
  - Seats that read the evidence against DISP-ONLY seats, which read none: +0.17.
- **Almost all of it is one task, B4,** the handover of the principal open question. There, 79–93% of evidence-reading unsound seats told the new analyst their lean, against 7% of DISP-ONLY seats and 8–43% of sound seats.
- **One difference sits outside B2 and B5's demanded focus:** B3 `steer` (the cold-read request), FULL_unsound 0.64 against DISP-FIRST_unsound 0.36.
- **Read together, this is consistent with the null the experiments were closed on.** Across several briefings, the order of reading does not change how often a seat briefs with its conclusion. The unsound text and the evidence both do, mostly when the task is to hand over an open question.

## Deviations

1. **Stopped at 70 of 120 seats by decision,** after the usage limit interrupted the run. Arms are 13–15 seats, interleaved, so the stop does not depend on outcome.
2. **The registered hand-check was not run,** because the experiments closed. Without it, scorer reliability on this rubric is unmeasured.
3. **`conclusion` alone is reported beside the primary on 60's cold read,** which came before the aggregate was read. It is a registered secondary, not an amendment.
4. **272 failed scoring records from the usage-limit stop held no scores.** They were removed before scoring, because the harness never re-runs an existing record.

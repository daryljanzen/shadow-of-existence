# E8 — Load in a long session: RESULT

**Headline.**
- **The registered composite is at 0 again**, as in the pilot: one late E3 flaw missed in 768 scored early and late task turns. The casebook's failure types do not appear in 32-turn sessions on Opus 5.5.
- **On the primary (review depth), the picture is not the pilot's.**
  - **The no-curriculum arm (PLAIN) thins only a little, and its interval reaches 0, so P1′ fails narrowly:** −1.03 [−2.22, +0.06].
  - **The two curriculum arms thin by about 3 problems per review**, IMPLICIT −2.94 [−3.84, −2.12] and REMINDER −2.94 [−3.94, −2.00]. **IMPLICIT thins more than PLAIN, not less: P2′ fails in the direction it did not predict.**
  - **The curriculum raises review depth early, and it fades to PLAIN's level by the late window.** The arms end in the same place (about 7–7.5 valid problems per review). So the extra thinning is the curriculum's early boost wearing off. It is not extra load.

- **Run:** 2026-11-13/14, `claude-opus-5-5`, 16 sessions per arm (orders A and B alternating), 48 sessions of 32 turns. Each session read about 18k words (the curriculum, or PLAIN's matched filler), then took 24 tasks.
  - All 48 sessions completed. The run was paused once for the weekly-limit check, and the 8 sessions in flight finished. One container restart lost 8 incomplete sessions, which were re-run from the start, as the runner does.
- **Scoring:** 1,248 blind scorer calls, 0 failed.
- **Cost:** about $229 at list price for the main run and its scoring, including the re-run sessions.
- **Records:** `runs_main/`, `scores_main/`. The analysis is `analyse_e8_depth.py main` (primary and the length secondaries) and `analyse_e8.py main` (composite and echo). Intervals are 95% bootstrap over sessions (10,000).

## The primary: valid other problems per E3 review, late − early

| arm | early (task turns 1–8) | late (17–24) | late − early (95% CI) |
|---|---|---|---|
| IMPLICIT (curriculum) | 10.47 | 7.53 | **−2.94 [−3.84, −2.12]** |
| REMINDER (curriculum + reminder) | 9.53 | 6.59 | **−2.94 [−3.94, −2.00]** |
| PLAIN (matched filler) | 8.56 | 7.53 | **−1.03 [−2.22, +0.06]** |
| pooled | | | −2.30 [−2.93, −1.69] |

**Arm contrasts on late − early:**

| contrast | estimate |
|---|---|
| IMPLICIT − PLAIN | **−1.91 [−3.34, −0.50]** |
| REMINDER − PLAIN | −1.91 [−3.38, −0.41] |
| REMINDER − IMPLICIT | 0.00 [−1.31, +1.31] |

- **The counterbalance holds:** order A puts block X early and order B puts Z early. Every arm thins in both orders (IMPLICIT 10.7 → 7.4 and 10.3 → 7.6; PLAIN 9.0 → 7.9 and 8.1 → 7.1).
- **Session-to-session SD of late − early** is 1.9–2.4, close to the pilot's 1.95, so n = 16 was powered as registered.

## Secondaries (registered at `r7759`)

| arm | words per review, early → late | valid per 1,000 words, early → late |
|---|---|---|
| IMPLICIT | 1,130 → 1,007 | 9.3 → 7.5 |
| REMINDER | 1,183 → 999 | 8.1 → 6.6 |
| PLAIN | 1,108 → 1,065 | 7.7 → 7.1 |

- **Not only shorter:** in the curriculum arms, valid problems per 1,000 words fall as well as length. In PLAIN both fall only slightly.
- **Invalid "other" problems** stay at 0–2 per window in every arm. They do not rise late, so the drop is not a stricter validity threshold.
- **The composite** (the `r7758` formula) is 0 in every window of every session but one (IMPLICIT s08, one late E3 review missing one planted flaw).
- **Echo:** the registered reminder-phrasing patterns match 0 task replies in every arm, so no reply gives its arm away.

## Against the registration

- **P1′ (load thins depth in PLAIN; interval excluding 0, 70%): fails, narrowly.** −1.03, with the interval reaching +0.06. Load alone thins review depth by about 1 problem in 9, if at all.
- **P2′ (the implicit curriculum thins less than PLAIN; 35%): fails, and in the other direction.** IMPLICIT thins more, by −1.91 [−3.34, −0.50]. The pilot pointed this way, and that was stated at registration.
- **P3′ (the reminder; descriptive): no difference from IMPLICIT** (0.00 [−1.31, +1.31]). The reminder before every task neither adds to nor protects against the curriculum's fade.

## What the arms' levels show

- **Early, after reading, the curriculum arms raise more valid problems per review than PLAIN:** IMPLICIT +1.9 and REMINDER +1.0 above it.
- **Late, all three sit at about the same level:** IMPLICIT 7.5, PLAIN 7.5, REMINDER 6.6.
- **So the curriculum's measurable effect on review depth is a boost right after reading that does not last 16 further tasks.** The registered late − early contrast reads that fade as thinning. Read against PLAIN, the late curriculum reviews are not worse. Their early advantage is gone.
- This reading uses levels the registration reports but does not name as a contrast. Its weight is that of a description of the registered measures, not a tested prediction.

## What this means for the paper (Steps 1 and 6)

- **The casebook's failures (dropped asks, false acceptance or rejection, premature closure, missed planted flaws) do not occur in 32-turn sessions with an 18k-word reading load on Opus 5.5.** That is true in every arm, with or without the curriculum. E1–E4's single-message ceilings hold under this load.
- **The one load-like effect, the pilot's thinning, mostly does not survive in the no-curriculum arm.** What remains is the curriculum's own early lift fading.
- **For Step 6:** the curriculum leaves a reader more thorough right after reading. Within a 24-task session that lift decays to baseline, and a reminder before each task does not hold it. If the paper claims the curriculum carries forward, this is evidence that it does so for a few tasks, not for a session.
- **What E8 does not test** is the casebook's actual setting: much longer sessions, context compression, a human interlocutor's pressure, and tasks that depend on earlier turns. Those remain the route to Step 1's original claim. They would be registered as E8b.

## Deviations

1. **The primary changed after the pilot** (`r7759`), from the composite to review depth. That was registered before any main-run session and stated as informed by the pilot.
2. **One container restart and one deliberate pause** interrupted the run. Incomplete sessions were re-run whole, and no partial session was scored. The runner records these in `runs_main/FAILURES.log` only for errors, and none occurred.
3. **60's `r7758` fixes were all in place before any main-run session:**
   - PLAIN's length-matched filler;
   - the composite formula;
   - intervals on P2 and P3;
   - failures logged outside the session directory;
   - incomplete sessions not scored;
   - the turn timeout on a raw-fd line buffer, with the process killed on failure;
   - the echo measure.

# E8 — Implicit carry against explicit reminder, late in a long session (registration)

Committed before any E8 trial. The claims under test are `LOGICAL_ORDER.md` Step 6:
- understanding outlasts rules;
- implicit carry beats explicit reminder;
- re-stating the rules at every step adds nothing, or pushes toward the directional heuristics late in a session.

**This experiment also carries the question the first-wave pilots raised.** E1–E4 and E6 found Opus 5.5 at ceiling on cold, self-contained tasks (`FOR_66_FROM_70.md`, `ARP-E+70.9`). The casebook's failures were recorded late in long, loaded sessions, so E8 measures the same failure types **late in a long session**, beside a plain long session with no spin-up. That third arm is added because of the pilots, and it is stated here before any E8 trial.

## Subjects and sessions

- **Model:** `claude-opus-5-5`.
- **The session:** one multi-turn session per subject (`claude -p --input-format stream-json`, with the isolation of `harness/subject.py`), so the curriculum, every task and every reply sit in one growing context.
- **What reaches every subject identically:** see `../SUBJECT_ROUTE_PROBE.md`.

## Arms (16 sessions each)

| arm | spin-up | each task turn |
|---|---|---|
| **IMPLICIT** | E7's FULL order (ARP paper → evidence 01–06 → sound disposition), one document per turn | the task alone |
| **REMINDER** | the same spin-up | the task, preceded by a fixed ~150-word restatement of the sound disposition's rules (`materials/reminder.md`, drawn from its headings, committed before any trial) |
| **PLAIN** | none | the task alone, so the session is just as long without any curriculum |

## The working session: 24 task turns

Tasks are drawn from E1, E2 and E3's committed items, which are outside physics and outside the curriculum's own domain. They are interleaved in a fixed, seeded order:
- 8 coverage messages (E1 items, without E1-09, the defective item);
- 8 claims (E2 items: 3 correct-contested, 3 wrong-confident, 2 open);
- 8 reviews with the author's framing (E3 items, C1-style).

**Early is turns 1–8; late is turns 17–24.** Every item appears early in half the sessions and late in the other half (counterbalanced by session index), so early and late see the same items.

## Measures (scored blind, per turn, with E1–E3's own rubrics)

Each scorer context gets the turn's task and reply only. It never sees the arm, the session or the turn index.
- **Coverage failure:** the hard ask is scored < 2 (E1 rubric).
- **Guard errors:**
  - false acceptance or false rejection (E2 verdict rubric);
  - **closure** on open items (E2's amended settled/not-settled rubric).
- **Review depth:** planted flaws found out of 3, plus other valid problems raised (E3 rubric).
- **Primary:** the **late − early** change in a composite failure rate. That rate is the share of failure events across the coverage, guard and closure items, plus 1 − found/3 on reviews, averaged per session. It is compared across arms.

## Predictions (made before any trial)

- **P1 (load produces the failures):** in PLAIN, the composite failure rate is higher late than early, with the interval excluding 0. Confidence 50%. The first-wave ceiling says cold tasks do not fail; the casebook says late tasks do.
- **P2 (implicit carry holds):** in IMPLICIT, late − early is no larger than in PLAIN, and smaller if P1 holds. Confidence 50%.
- **P3 (reminders do not help, and may push toward closure):** REMINDER's late failure rate is ≥ IMPLICIT's. Its late closure rate is > IMPLICIT's. Confidence 45% for each.

## What counts against

- **The load premise:** if PLAIN shows no late − early rise (interval includes 0, or points down), long sessions at this length do not produce the failures. The casebook's failures then need longer sessions, compression, or a human interlocutor to appear. That is reported as such.
- **Implicit carry:** if REMINDER's late failure rate is lower than IMPLICIT's with the interval excluding 0, explicit reminders help, against Step 6's claim.
- **Every failed prediction is reported** at the same weight as a held one.

## n, cost and pause

- **The pilot:** 2 sessions per arm, discarded afterwards. It checks the session mechanics, measures cost per session and gives σ for the late − early contrast.
- **n:** the main run is 16 per arm. If the pilot's σ implies 16 cannot detect a 10-point late − early difference, the report says so before the main run, with the number that could.
- **Estimated cost:** about $3–5 per session at list price (a ~25–60k-token growing context, mostly cached), so **$150–250 for the main run.** It runs in batches of 4 sessions under the pause switch. The per-batch cost goes to the usage ledger and is reported.

## Records

- `runs/<arm>/<session>/turn<k>.json` and `scores/…`.
- `RESULT.md`: written against this file.

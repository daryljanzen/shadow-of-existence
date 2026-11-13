# E8 pilot (registered: 2 sessions per arm, discarded): what it shows, and the call before the main run

- **Run:** 2026-11-13, after 60's `r7758` read was taken whole.
- **Model and sessions:** `claude-opus-5-5`; 6 sessions (IMPLICIT, REMINDER and PLAIN, each in order A and order B), 32 turns each.
- **Failures:** none. All 6 sessions completed, and `FAILURES.log` is empty.
- **Scoring:** 156 blind scorer calls, 0 failed.
- **Cost:** about $23.14 for the sessions and $5.73 for scoring.
  - Per session: IMPLICIT $4.37 and $4.37; REMINDER $4.78 and $4.00; PLAIN $2.97 and $2.66.
- **Analysis:** `analyse_e8.py pilot`.

## What it shows

**The registered composite is 0 in every window of every session, early and late, in all three arms.** That covers 96 scored X/Z task turns and 288 task turns in all:
- E1: no hard ask scored below 2.
- E2: no verdict error, and every open item was judged not settled.
- E3: every review found all 3 planted flaws (48 of 48).

So late − early is 0.000 in every arm, and σ of late − early is 0.

- **The registered n rule cannot be applied.** With σ = 0, no n detects a 10-point contrast, because there is no variation to contrast. The registration says the report states this **before** the main run, and this is that statement.
- **The load premise (P1), at this length.** The pilot is 2 sessions per arm, so it bounds rather than estimates. But zero failures in 48 late scored turns across the three arms, PLAIN included, is the same ceiling E1–E4 and E6 found cold.
  - Each session is 32 turns: about 18k words of reading, then 24 tasks.
  - **On this evidence, sessions of this length and load do not produce the casebook's failure types on these items in this model.**
- **The disposition echo** is 0 by the registered patterns in every arm. A loose word check finds reminder-adjacent words ("weight", "the source") in 9 of 48 REMINDER replies. These are ordinary words, and the registered patterns are what count.

## The call before the main run

The main run as registered (16 sessions per arm, about $190 at the pilot's per-session cost) would very likely measure 48 zeros. **I do not start it.** It would not answer P1–P3; it would repeat the pilot at ten times the cost.

What would make E8 informative is a session in which the failures occur at a measurable rate. The pilot rules out "a 32-turn session with an 18k-word reading load", and two directions remain open:

1. **A measure that is not at ceiling.** E3's "valid other problems raised" sat at 7–10 per review in the E3 pilot and moved with condition. Scored per review turn, early against late, it measures review depth under load without needing a failure to occur.
   - It costs no new sessions: the pilot's 48 E3 replies, and any main-run replies, can be scored for it with E3's existing scorer output (`other`).
   - It would be registered before any further session.
2. **Longer or more loaded sessions.** Several times the length, or the conditions the casebook recorded (context compression, a human interlocutor's pressure, tasks that depend on earlier turns). These change the experiment's design, not its parameters, and would be registered as E8b.

## Records

- `runs_pilot/<arm>/s00`, `s01`: the spin-up or filler documents, then `turn1–24.json`.
- `scores_pilot/{E1,E2,E2open,E3}/<arm>/`.
- **Ledger note:** the `USAGE.tsv` token column for E8 rows is the session's cumulative usage as the stream reports it. The cost column is differenced per turn, and it is the one to sum.

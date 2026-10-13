# `r7299+70.2` — PRE-REGISTRATION: the two scores for 69's rule, fixed before the rule is applied to any key

*Committed before 70 applies `THE_RULE.md` to a single key. It answers `FOR_70.md` `r7299` (YOUR ORDER — TWO
SCORES), read at `origin/main` `6e639dad`. The rule being scored is
`computations/beyond_the_wall/r7299_69_the_rule/THE_RULE.md` at `6e639dad4655ceb0a6f00aee8ab47ff13fd3d7c5`. It is
pinned there, so a later edit to the rule is a different rule.*

*The r7297 pre-registration (`r7297_70_convergence_score/PREDICTION.md`, committed at `b788440a`, 15:19 UTC) stands.
That is the design for scoring a rule on fresh keys with three appliers. This file adds the two scores `r7299` asks for
on the keys already read. `b788440a` predates the rule text (`6e639dad`, 15:40 UTC).*

## What I have seen, and what I have not

**Seen before this file:**

- The rule text, read in full.
- 69's reply on it.
- 66's `r7299` tables.
- **Aggregate owed rates on the 44 three-way keys**, computed and printed as totals only:
  - **69: 19 of 44 (43.2%)**
  - **60: 20 of 44 (45.5%)**
  - **cc66: 29 of 44 (65.9%)**
  - On identical keys cc66's threshold sits 22.7 points above the other two, more than the 15 points across
    mixed cells.
- **The 69/60 file holds 17 disagreeing cells.** 66's decomposition names 16 (4 + 6 + 5 + 1).

**Per-key verdicts seen in earlier steps:** six keys, two data rows printed in each of three files while
inspecting their shape. Those were `THREE_READERS.tsv` (two `L150` keys), `ACCIDENTAL_3` and the `L804` pair.
Any of those six keys inside the scored set is marked **SEEN** in the application file. Every result is reported
with and without them.

**Not seen:** the verdicts of the other keys, and which cells make up 66's four parts. **The applier is 70, blind.**

- The keys are `KEYS_BLIND.tsv`: receipt and literal only, cut without printing a verdict column.
- The rule is applied to each key in its four ordered steps, recording what the rule asks for:
  - the step that decided;
  - for `REPAIR-OWED`, the test (1–7) and the site detail;
  - for a row on the `ENCODING-OK` border, **UNDECIDED (60's border)**, as the rule directs.
- The application is committed **before** any verdict column is joined to it, as the `L262` read was.

## ① The calibration score: does the rule put the owed threshold where 69 and 60 put it?

**Set:** the 44 three-way keys.

- Every seat read every one of them, so the three rates are on identical keys.
- 66's 122 cells are not: cc66's include 34 keys that 60 never read.
- The 90 keys cc66 has read, against 69 on the same 90, are a **secondary** set, scored the same way once applied.

**The quantity:** ρ, the rule's owed rate on the decided keys of the set.

- Undecided keys are left out of ρ and of every seat's rate alike.
- The verdict is read off ρ's 95% Wilson interval against two fixed points:
  - the **69/60 threshold, 44.3%** (their mean, 0.2 points apart in 66's cells, 2.3 here);
  - **cc66's, 65.9%**.

| ρ's interval | verdict | at 44 decided keys |
|---|---|---|
| holds 44.3, excludes 65.9 | **CALIBRATES**: the rule moves cc66 to the others and leaves them | 14–22 owed |
| holds both | **CANNOT DISCRIMINATE** at this size (see ④) | 23–25 |
| holds 65.9, excludes 44.3 | **ADOPTS cc66's THRESHOLD**: it moves 69 and 60, so it re-describes rather than calibrates | 26–35 |
| below 44.3 entirely | **MOVES ALL THREE DOWN**: re-describes | 0–13 |
| above 65.9 entirely | **MOVES ALL THREE UP**: re-describes | 36–44 |

- **A key-level check is reported beside it, without a threshold:** the rule's owedness agreement with each seat.
- **If the rule calibrates,** agreement with 69 and with 60 should each exceed agreement with cc66. If ρ calibrates
  while key-level agreement does not separate the seats, I say the rule hit the right rate on the wrong keys.

## ② The definition score: the 17 cells where 69 and 60 disagree

**Set:** the 17 disagreeing cells of `DOUBLE_READ_69_vs_60.tsv`.

- These are keys 69 and 60 read with the same threshold and still split, so no calibration reaches them.
- **The parts are assigned only after the blind application lands,** from 66's row-by-row reading:
  - notation, 4;
  - short tokens, 6;
  - `MEANING-HELD` against its neighbours, 5;
  - already ruled, 1;
  - plus the 17th cell, which 66 did not place and which I will name.
- **Each part is scored separately,** so a fix to one boundary does not average out against a miss on another.

**Per part, measured today by one applier:**

- **decided:** the share of the part's keys the rule decides without judgement;
- **side:** for each decided key, whether the rule lands with 69, with 60, or with neither.

**Convergence needs a second applier,** and with one it is not claimed.

- The definition score proper is the share of each part's keys on which **two blind appliers of the rule agree**.
- It is scored when a seat that has read none of these keys applies the rule to the same 17. 71 and 66 qualify;
  69, 60 and cc66 do not.

| part | decided (one applier), central | band | convergence of two appliers, central | band |
|---|---|---|---|---|
| notation (4) | 0 of 4, by design: the border is left to 60 | 0–1 | not scored | — |
| short tokens (6) | 6 of 6: Test 4 is a count | 5–6 | 5 of 6 | 4–6 |
| `MEANING-HELD` (5) | 4 of 5 | 3–5 | 3 of 5 | 2–5 |

**69's own overturn condition is adopted as written.** If two appliers still split on 3 or more of the 5
`MEANING-HELD` cells, the definite-noun choice has not done its job.

## ③ The sample size, in cells, for telling two rules apart

This is from `b788440a` ③, restated in the unit `r7299` asks for. To believe a difference of 0.15 in convergence
between two candidate rules (two-sided, 95%, power 0.80, σ = 0.354 from the 44):

- **88 keys per rule, each read by three appliers:** 264 three-way readings, 264 (key, pair) cells per rule;
- **and a no-rule arm of the same size,** read by the same three in the same draw.

**Fewer than 88 is a hint, not a difference.** The rule-against-no-rule test needs **69** per arm.

## ④ The symmetric negatives: when these scores cannot discriminate, and what replaces them

- **N-C1:** ρ lands in the CANNOT DISCRIMINATE band.
  - Then 44 keys cannot place the rule's threshold between the two seats.
  - The secondary 90-key set, cc66 against 69, is applied before any verdict is given. If it lands in its own
    middle band too, the calibration score needs more keys than the three-way read holds, and I say so.
- **N-C2:** a second blind applier, on a 10-key sample of the 44, disagrees with me on owedness on 3 or more.
  - Then the score measures the applier as much as the rule, and needs two appliers per key before any verdict.
- **N-D1:** the rule decides fewer than half of the short-token and `MEANING-HELD` cells (fewer than 6 of 11).
  - Then the definition score has nothing to converge on, because the rule does not reach the disputed keys.
  - The rule text needs another step before it can be scored, and that goes back to 69.

## ⑤ My central prediction for ρ, so it can be wrong

**ρ = 55% of the 44 (band 40–70%): CANNOT DISCRIMINATE, leaning toward cc66's threshold.**

- The rule makes `REPAIR-OWED` the result of ANY of seven tests.
- Test 4 alone (a count above one, or a changed count) reaches every short token.
- I expect it to be more inclusive than 69's own calls, and to pull 69 and 60 up rather than cc66 down.
- If ρ calibrates, the seven tests are narrower in application than in text, and that is the finding.

**Not done:** the rule is applied to no key, no verdict column of the scored set is read, and no part assignment
is looked at.

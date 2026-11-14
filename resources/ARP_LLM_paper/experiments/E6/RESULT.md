# E6 — The game against self-play: RESULT

**Headline.** **The registered ceiling clause fires.** Self-review (S) corrects 3.94 of the 4 seeded flaws, above the registered 3.5. All three conditions correct nearly every flaw (S 3.94, G-ARP 3.98, G-noR 4.00), and they do so **already after the first rewrite**. So the primary measure cannot separate the game from self-play. **P1 fails as registered:** the G-ARP − S interval includes 0. One registered secondary did move, and it moved against the game: **G-ARP adds fewer of the valuable extensions** than both S and G-noR, and so has lower net valid content.

- **Run:** 2026-11-13, `claude-opus-5-5`.
  - 24 tasks × 3 conditions × 2 replicates = 144 chains of 6 calls (864 subject calls).
  - 144 blind scorings of final versions, and 432 blind stage scorings (steps 1, 3 and 5; `score_stage.py`, registered at `r7759` before any aggregate was read).
  - 0 failed calls.
- **Cost:** about $167 for E6 in all (pilot, main run, scoring and stage scoring) at list price (`../USAGE.tsv`).
- **Records:** `runs_main/`, `scores_main/`, `stage_main/` with `stage_key.json`, `handcheck/`. The analysis is `analyse_e6.py`.

## n

The pilot rule gave n ≤ 24, so the main run used the 24 tasks. At the ceiling the rule is moot: the main run reports a bound, not a powered contrast.

## Results (per task, replicates averaged; 95% bootstrap over 24 tasks)

| | S (self-review) | G-ARP (game, receipts) | G-noR (game, no receipts) |
|---|---|---|---|
| **Seeded flaws corrected** (of 4) | 3.94 | 3.98 | 4.00 |
| Finals with all 4 corrected | 94% | 98% | 100% |
| Extensions present and valid (of 3) | **2.58** | **2.27** | 2.52 |
| Introduced errors | 0.04 | 0.04 | 0.06 |
| Net valid content (extensions − introduced) | 2.54 | 2.23 | 2.46 |
| Tokens, all calls (M) | 3.29 | 2.57 | 2.51 |
| Flaws corrected per 10k tokens | 0.58 | 0.74 | 0.77 |
| Net valid content per 10k tokens | 0.37 | 0.42 | 0.47 |

**Paired contrasts:**

| | G-ARP − S | G-ARP − G-noR | G-noR − S |
|---|---|---|---|
| Flaws corrected | +0.04 [−0.04, +0.13] | −0.02 [−0.06, 0.00] | +0.06 [0.00, +0.13] |
| Extensions | **−0.31 [−0.56, −0.10]** | **−0.25 [−0.44, −0.08]** | −0.06 [−0.29, +0.13] |
| Net valid content | **−0.31 [−0.56, −0.08]** | **−0.23 [−0.44, −0.02]** | −0.08 [−0.29, +0.08] |
| Introduced errors | 0.00 [−0.06, +0.06] | −0.02 [−0.10, +0.06] | +0.02 [−0.06, +0.10] |

**The stage measure** (flaws corrected after each step; step 6 is the final version):

| | step 1 | step 3 | step 5 | step 6 |
|---|---|---|---|---|
| S | 3.94 | 3.85 | 3.96 | 3.94 |
| G-ARP | 3.92 | 3.96 | 3.98 | 3.98 |
| G-noR | 3.96 | 3.98 | 4.00 | 4.00 |

The first rewrite corrects nearly everything in every condition. No later step, review or not, has room to add much.

## Against the registration

- **Ceiling: fires.** S corrects 3.94 of 4, above the registered 3.5. The seeded flaws are too easy for this model to separate the conditions, and that is reported as such.
- **P1 (G-ARP corrects more flaws than S, interval excluding 0): fails.** +0.04 [−0.04, +0.13]. By the stage measure, the game's cold readers add nothing over revision alone, because revision alone has already corrected the flaws at step 1.
- **P2 (G-ARP ≥ G-noR, and G-noR − S < G-ARP − S): not supported.** On flaws, G-noR is at 4.00 and G-ARP at 3.98, and G-noR − S (+0.06) is not below G-ARP − S (+0.04). The registered failure condition (G-noR ≥ G-ARP with the interval excluding 0) is not met: the interval reaches 0.00. **On extensions, receipts cost:** G-ARP adds 0.25 fewer than G-noR, with the interval excluding 0.
- **P3 (in S, step 3 ≈ step 6, within 0.25): holds.** +0.08 [−0.04, +0.27]. Self-review plateaus, but it plateaus at the ceiling from step 1.
- **P4 (S introduces at least as many errors as G-ARP): holds, trivially.** Both introduce 0.04 errors per final version. Introduced errors are near zero in every condition.

**The one moved measure, read with care.**
- **What moved:** G-ARP's final versions contain fewer of the key's three valuable extensions (2.27 against 2.58 for S and 2.52 for G-noR). No prediction named this. It is a registered secondary, reported at the weight a held prediction would get.
- **A possible reading, not tested here:** the receipt instruction ("restate each point the review makes and what it would change") ties the rewrite to the review's points. Material the reviewer did not raise is then dropped or not added. Without receipts the rewrite is freer, and S, which reviews itself, is freest. This is a mechanism to test, not a finding.
- **How robust:** the hand-check's κ on extensions is 0.88 (below), and the contrast excludes 0 against both comparisons. It rests on 24 tasks, and a 0.3 difference is about one extension in ten finals.

**Compute.** Matched by calls, the game uses about 22–24% fewer tokens than self-review: S rewrites the whole analysis six times, while the game spends two calls on reviews. Per 10k tokens the game corrects more flaws, but only because the denominators differ. All three conditions are at ceiling on the numerators.

## The hand-check (registered and drawn before the aggregate was read)

- **The sample:** 30 of the 144 final-version scorings, 10 per condition, drawn with seed 6755 (`handcheck/draw.py`). I scored them blind to condition and to the scorer's output. My scores were committed (`68293080c`) before `KEY.json` was opened.
- **Flaws corrected:** 119 of 120 agree. κ is degenerate (0.0) because my column is constant at 1: I judged every flaw corrected. The one disagreement is a flaw whose wrong figure was simply absent from the final version, which the scorer marked 0 and I marked 1.
- **Extensions:** 87 of 90 agree, **κ = 0.88**. Two of the three disagreements were borderline calls I flagged as such while scoring (an extension's ingredients present but its figure not computed, or its point made implicitly).
- **Introduced errors:** 29 of 30 exactly equal, 30 of 30 within 1. Over the sample the scorer counted one introduced error and I counted none.
- **What it settles:** the ceiling is not a scorer artefact. The extension judgement that the one moved contrast rests on holds up.
- **The limit:** the hand-scorer is a model of the scorer's family. So this checks how the rubric was applied; it is not an independent human judgement.

## Leak check

The scorer guessed "several authors" on 23 of 48 S finals, 7 of 48 G-ARP and 5 of 48 G-noR. That is the reverse of the truth: correct guesses total 37 of 144 (26%). The final versions did not reveal their condition, so the blinding held.

## What this means for the paper (Step 4)

**On analyses with seeded, checkable flaws, a single fresh-context rewrite already corrects them.** Under those conditions the two-seat game with cold readers does not beat matched self-review, and receipts do not help. The perspective Step 4 credits to cold readers has nothing left to contribute when the flaws are of a kind the author's own fresh pass already catches.

- **The material is the limit, as in E1–E4.** The flaws were seeded to be findable from the document and data, and the model finds them without help. Step 4's claim concerns problems the author's perspective cannot see. E5 found that gap in reviewers' *findings*. E6's seeded flaws are not of that kind.
- **Receipts cost breadth here.** In this design, a restatement of the review before revising produced versions with fewer of the valuable additions. If the paper recommends the receipt as a step in the game, that cost should be tested, not assumed away.
- **An E6b that could test Step 4** would need flaws a fresh rewrite does not catch: errors that need information or a perspective the author does not hold. It would be registered before running.

## Deviations

1. **The stage measure was registered at the first commit but not built into the runner.** It was built as a separate blind scorer pass, registered (`r7759`) before any aggregate was read, and run after the hand-check was committed. Its file paths carry opaque ids, and its prompt carries no condition.
2. **The hand-check was drawn and scored before the aggregate was read, as registered.** No other deviation in procedure.

# `r7299+70.6` — RESULT: 69's rule does not calibrate cc66. It moves all three seats UP, to 90% owed, so it re-describes the class. And it does so by its text, not by judgement: 28 of the 29 keys it decides without judgement come out owed

*Pre-registered at `PREDICTION.md` (`3a5a392a`). The rule is `THE_RULE.md` at `6e639dad`. It was applied blind at
`r7299+70.4` (`f1a0c00c`) and completed at `.5` (`4d7724e5`), both before any verdict was joined. The numbers below
come from `score.py`.*

## The application

- **Who applied it:** two fresh applier agents of seat 70, each given half of `KEYS_BLIND.tsv`. They were barred from
  the ledger, every double-read, blind and result file, everything under `computations/`, and the coordination
  files.
- **What came out, on 47 keys:**
  - 39 `REPAIR-OWED`
  - 3 `MEANING-HELD`
  - 1 `DELIBERATE`
  - 1 `NOT-A-PIN`
  - 3 `UNDECIDED`: exactly the three `ν_R` spellings, which the rule leaves to 60's border, as it directs.
- **The over-barred site files.** The bar list also covered three *site* files: two `THE_*.md` registers and
  `bbn_network.py`. That left 3 keys undecided for want of their site.
  - `.5` let the same appliers open those three files and nothing else.
  - Those 3 keys were decided, and 7 rows decided without the site were re-checked. None changed.
- **Tests that decided the 39 owed rows:** Test 1 (words outside the quotation) 16, Test 4 (count or place) 9,
  Test 2 (pointing word) 7, Test 5 (unjoined pieces) 7.
- **Judgement:** 24 of 47 rows needed a call the rule does not settle. Only 9 of the 39 owed verdicts did.
- **Not fully blind:** for 14 keys the applier read a repair note **inside the receipt itself** (cc66's r7293
  comments), and one of those notes states a verdict. All figures are given without them too.

## ① The calibration score: MOVES ALL THREE UP, so the rule re-describes rather than calibrates

On the 41 decided keys of the 44 three-way keys:

| | owed | rate | owedness agreement with the rule |
|---|---|---|---|
| **the rule** | **37 / 41** | **90.2%** (95% 77–96%) | — |
| 69 | 16 / 41 | 39.0% | 48.8% |
| 60 | 20 / 41 | 48.8% | 58.5% |
| cc66 | 26 / 41 | 63.4% | **73.2%** |

- **⇒ MOVES ALL THREE UP**, the band fixed for 36 or more of 44. The interval lies wholly above cc66's 65.9%.
- **Without the 11 SEEN keys:** 26 of 30 = 86.7% (95% 70–95%). Same verdict.
- **The key-level check runs the wrong way for a calibration.** The rule agrees most with cc66 and least with 69.
  It does not pull cc66 toward the others. It pulls everyone past cc66.
- ⛔ **My prediction is refuted.**
  - I registered ρ = 55%, band 40–70%, "the middle band, leaning toward cc66".
  - The direction was right and the size was not. The rule is more inclusive than every reader, not between them.

**Why, read from the rows and not the rate:**

- **Test 1 alone decides 16 of the 39.** "Cut the quoted text out of its sentence; does the claim still follow from
  the quoted words alone?"
- **A receipt's claim is almost always larger than the span it pins.** The claim is a sentence about what the paper
  establishes, and the span is a few words of it.
- **So, applied literally,** Test 1 reaches nearly every pin that is not a complete sentence carrying its own
  subject. Of the 29 keys the rule decided **without** judgement, 28 are owed.
- **The inclusiveness is in the text, not in the appliers.** The step-4 exits (`MEANING-HELD`, `DELIBERATE`) are
  reached only by a key that fails all seven tests, and almost none does.

## ② The definition score, per part, over the 17 cells where 69 and 60 disagree

| part (66's, assigned after the join) | cells | decided | lands with 69 | lands with 60 | neither |
|---|---|---|---|---|---|
| notation (`ν_R` spellings, the `analytical index` alternation) | 4 | 1 | 0 | 0 | 1 |
| short tokens (`DELIBERATE` against `REPAIR-OWED`) | 7 | **7** | 0 | **7** | 0 |
| `MEANING-HELD` against a neighbour | 4 | **4** | **3** | 1 | 0 |
| already ruled (`THERE IS NO SUCH BUNDLE`) | 1 | 1 | 0 | 0 | 1, and it agrees with the r7297 ruling (`REPAIR-OWED`) |
| **the 17th**, which 66's decomposition did not place: the `PO-7` strike regex | 1 | 1 | **1** (`NOT-A-PIN`) | 0 | 0 |

- **The parts are 4, 7, 4, 1 and 1, not 66's 4, 6, 5 and 1.**
  - 66's table names only some cells per part, so I placed the rest by the part's own class pair.
  - Every 69/60 `DELIBERATE`/`REPAIR-OWED` cell counts as a short token, which makes 7.
  - The 17th is the `NOT-A-PIN`/`DELIBERATE` regex.
- **The rule reaches the disputed keys.** It decides 11 of the 11 short-token and `MEANING-HELD` cells, so N-D1
  does not fire.
- **Predictions on decided counts:** notation 1 of 4 (band 0–1), short tokens 7 of 7 (central 6 of 6), and
  `MEANING-HELD` 4 of 4 (band 3–5). All held.
- **The short-token boundary is decided entirely to 60's side:** `REPAIR-OWED`, by Tests 1, 2, 4 and 5. That is a
  definition, consistent and one-sided. Whether it is the RIGHT side is the calibration question, and ① says the
  rule's side is the inclusive one everywhere.
- **The `MEANING-HELD` part goes 3 to 1 to 69,** all three by Tests 1 and 2. Two of those keys are SEEN.
- **Convergence is not claimed.** It needs a second blind applier on these 17 keys: 71 or 66, as registered.

## The negatives

- **N-C1** (the middle band): did not fire. The interval is decisive.
- **N-D1** (the rule reaches too few disputed keys): did not fire.
- **N-C2** (two appliers disagree): not yet testable, because there is one applier.
  - Both halves were applied by agents of one seat, under one instruction.
  - Their owed rates are 22 of 24 and 17 of 20 decided, so they do not disagree with each other in rate. That says
    nothing about a second seat.

## What this means for the campaign, said plainly

**As written, the rule does not separate `REPAIR-OWED` from its neighbours.** It makes `REPAIR-OWED` the default for
any pin short of a whole sentence that carries its own subject.

- That settles the short-token boundary, toward 60.
- But it raises every reader's owed rate past the most inclusive reader's.
- **A calibration rule has to land near 44% on these keys,** where 69 and 60 already sit.

**The candidate the result points at, offered to 69 and not drafted here:** bound Test 1. As written, it asks
whether the quoted words alone carry the receipt's *whole* claim. A version that asks whether the words left outside
change *which* thing or *whether* is claimed (a subject, a condition, a negation) would keep the three named cases
and release the rest.

That is a new rule, scored by the same instrument on fresh keys (`r7297_70_convergence_score/PREDICTION.md`). It is
not re-scored on these 47, which it would be drafted from.

**Not done:** no verdict in the ledger is changed, nothing is reconciled, and the 90-key secondary set is not
applied.

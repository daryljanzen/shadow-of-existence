# `r7267+70.0` — PRE-REGISTRATION: how many citations sit on claims wider than their receipts

*Committed before the detector is written or any site is counted, beyond the one population count stated below.
It answers `FOR_70.md` `r7267` ②, read at `origin/main` `e2a76aa6`. Orders ①, ③ and ④ of `r7267` were already
answered at `r7265+70.1` (`d1d8dd2b`, PR #351, not yet merged when `r7267` was written). See the status line in
`FOR_66_FROM_70.md`.*

## The populations

| | population | the claim | the receipt's reach |
|---|---|---|---|
| **PROSE** | every `\rcpt{X}` in a non-appendix `corpus/*.tex` (580 sites, the one count taken before this file) | the sentence holding the citation, normalised through `_unmark` | the source of `X`'s receipt file, resolved through `receipts/INDEX.md` |
| **APPENDIX** | every `receipts/INDEX.md` row with a receipt file | the row's `claim (one line)` cell, which the generated appendices print | the same receipt's source |

## The detector: counterfactual reach, approximated two ways and calibrated by reading

The convention is `X would FAIL if the claim were false` (`r2376+c54.166`). A parse cannot evaluate that, so I take
two mechanical proxies, each a necessary symptom of over-reach and not a sufficient one. A hand read decides
precision.

- **SCOPE arm.** The claim carries a universal or scope operator: `every`, `all`, `any`, `each`, `whole`,
  `entire`, `general`, `generic`, `always`, `never`, `for all`, `uniquely`, `only`, or `at every`. And the noun it
  governs (the next content word, crudely stemmed) occurs nowhere in the receipt's source: identifiers, string
  literals or comments. If the receipt never names the set the claim quantifies over, it cannot fail for a member
  outside what it checked. **`I55` is the exemplar**: the historical sentence's "exactness … at every term" over the
  whole space of cuts, where the receipt checks one cut.
- **NUMBER arm.** The claim carries a decimal figure (two or more significant digits) that occurs nowhere in the
  receipt's source. This is the shape of `P15R22`: a figure the row presents as the claim, which the receipt either
  does not compute or computes in another configuration. The number arm is EXPLORATORY: receipts often compute a
  figure without containing it literally, so I expect its precision to be low. Reading measures it.

**Seeds (two-sided).**

- **S+1:** `I55`'s sentence at the commit before 60's repair must flag on SCOPE.
- **S+2:** `P15R22`'s INDEX row at the commit before 69's repair must flag on NUMBER.
- **S−1, S−2:** two control claims built to the receipt's exact reach must NOT flag. They are the receipt's own
  `what it computes` cell, used as the claim, for `I55` and for `P15_damping_ratio_clean`.

## Predictions

| # | quantity | central | band |
|---|---|---|---|
| R-a | PROSE sites resolving to a receipt file | 95% | 85–100% |
| R-b | PROSE sites flagged by SCOPE | 15% | 5–35% |
| R-c | APPENDIX rows flagged by SCOPE | 20% | 5–40% |
| R-d | sites flagged by NUMBER, both populations | 25% | 10–50% |
| R-e | precision of the SCOPE arm, on a hand read of 30 flags drawn at random | 40% | 15–70% |
| R-f | precision of the NUMBER arm, on 20 flags | 20% | 5–50% |
| R-g | recall check: of 20 UNflagged PROSE sites drawn at random, read by hand, how many over-reach | 1 | 0–4 |
| R-h | **the estimate:** over-reaching share of PROSE citations, from R-b × R-e plus the NUMBER arm's true positives | 8% | 3–25% |

**⛔ The reachable negative, as 66 sets it.** If R-h comes back above 50%, most citations over-reach. Then the
convention was never the practice, and the finding is about the CONVENTION and not about the sites. I report it as
that and file no per-site repairs.

**⚠ The second negative, which is mine.** If R-e is below 15%, the SCOPE arm cannot tell over-reach from ordinary
summary. The census then reports only the hand-read sample, with its interval, and no detector is placed as a gate.

**What is NOT done this cycle.** No repairs. A site that over-reaches belongs to the paper's owner and is ROUTED,
with the receipt and the clause named. The detector is a census instrument until its precision is known. Whether
it becomes a gate is a later decision, made on R-e.

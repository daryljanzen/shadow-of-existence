# `r7339+70.1` — PRE-REGISTRATION: the first stride back. This revision's realised receipts, cost per receipt, withdrawn share, and rule cases. Every band is failable at its central, and the registration is pushed before the first repair, in the same revision as the repairs (`r7339` ⑥)

*Orders: `FOR_70.md` §`r7339` ②, ⑤ and ⑥, read at `origin/main` `0a41d667`. My stride is `THE_REPAIR_STRIDE.tsv`
rows `70`: **105 rows in 30 receipts over 21 prefixes**, all unbegun. The working rule is `THE_RULE.md` at this main,
including **What a repair writes**: the shortest span that carries the whole claim and occurs once under the checker's
normalisation, then stop. ⑤'s ruling applies too: a locus-scoped conjunction of spans satisfies floor 2, and the
minimand is total pinned characters. No receipt is opened before this file is pushed.*

## The order of work

**I work down the stride list in its own order:** P10, then L202_phase_at_the_seam, L207, L221, L802, RP_34, P03,
L247, and so on. I stop when the revision closes. **The receipts not reached are named in RESULT as not reached.**
They are not counted as attempted.

## What is measured (⑥'s two quantities, with the assignment named)

- **EFFORT:** wall-clock minutes per receipt, from opening the receipt to the commit carrying its ledger rows.
- **REALISED:** receipts whose owed rows all leave the list in this revision, REPAIRED or WITHDRAWN with the case
  written beside them.
- **The owed count:** 70's owed rows before (105) and after, **beside the keys minted and adjudicated in the same
  push.** Each count is under `check_quote_pins`'s own normalisation.
- **Rule cases:** cases written beside repairs, where `THE_RULE.md` owed what it should not, or missed what it
  should catch.

## Predictions, with their decisive fractions

| # | quantity | central | band | P(outside band) at the central | model |
|---|---|---|---|---|---|
| S-a | receipts REALISED this revision | 12 | 6–20 | 0.14 | lognormal, σ 0.4 |
| S-b | median EFFORT, minutes per receipt | 8 | 4–15 | 0.27 | lognormal, σ 0.6 |
| S-c | withdrawn share of rows cleared | 15% | 8–25% | 0.16 | binomial, n ≈ 40 |
| S-d | rule cases | 2 | 0–4 | — | count; 5 or more fails it |

- **Why S-b's central is above L147's measured 2–6:**
  - L147 was one prefix, chosen first, with pins on prose the claim already paraphrased.
  - These receipts average 3.5 rows each, and include instrument and probability prefixes whose sites are not prose.
- **The 0–40% withdrawn band I used at `r7329` could not fail at its central.** It is tightened here so it can, and I
  say so.

## Not done

- No receipt is opened before this push.
- The applier machinery stays stopped.
- **No π_d:** nothing here has a second reading.

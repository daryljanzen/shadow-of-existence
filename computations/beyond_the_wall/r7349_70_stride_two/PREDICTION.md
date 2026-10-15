# `r7349+70.1` — PRE-REGISTRATION: the second stride block. 16 unbegun receipts and 59 rows, RP_34_gr to P08. Every band is failable at its central, and this file is pushed before the first repair, in the same revision as the repairs (`r7339` ⑥)

*Orders: `FOR_70.md` §`r7349` ①/⑤, `r7347` and `r7341` ①, read at `origin/main` `ed4c8b61`.*

- **The stride:** `THE_REPAIR_STRIDE.tsv` rows `70`. The block is whole (`r7349` ①).
- **What remains, by the live ledger at this commit: 61 owed rows in 18 receipts.**
  - 16 receipts, 59 rows, are unbegun.
  - Two rows are held and routed, and are not in this block:
    - `P10_no_rescaling`, RC3: a duplicated register site.
    - W1's comment pin, RC4.
- **The working rule:** `THE_RULE.md` at this main, with `r7341` ①'s corrected minimand.
  - Prefer the single contiguous claim-complete span that the ratchet can key.
  - Use a locus-scoped conjunction only where no single span carries the claim, and say so in the row's reason.
- **No receipt is opened before this file is pushed.**

## The order of work

The stride list, in its own order:

| prefix | receipt | owed |
|---|---|---|
| RP_34_gr | G2, G3 | 2, 6 |
| P03_SdS_slicing | A6, P03_w | 2, 2 |
| L247 | B1 | 8 |
| L202_the_seam | T1 | 6 |
| L_probability | S1 | 6 |
| L246 | W1 | 4 |
| L272 | F1 | 4 |
| L276 | R1 | 3 |
| L560 | P1 | 3 |
| L815 | S1 | 3 |
| L248 | R1 | 2 |
| L256 | B1 | 2 |
| L280 | D1 | 2 |
| L556 | R1 | 2 |
| L259 | D1 | 1 |
| P08 | P08 | 1 |

Receipts not reached are named in RESULT as not reached, and are not counted as attempted.

## The quantities, measured as at `r7339+70` (⑥: EFFORT beside REALISED, with the assignment named)

- **EFFORT:** wall-clock minutes per receipt, from opening the receipt to the commit that carries it.
- **REALISED:** receipts whose owed rows all leave the list in this revision, REPAIRED or WITHDRAWN with the case
  written beside them.
- **The owed count:** before (61) and after, beside the keys minted and adjudicated in the same push.

## The bands

The prior is `r7339+70`'s measurement:
- about 0.7–1.6 minutes a receipt;
- 1 withdrawal in 44 rows;
- 2 rule cases in 12 receipts.

**That measurement was on paper-prose prefixes only.** This block is mixed: L272, L276 and L556 are source-heavy, and
L_probability is an instrument prefix. So every central is moved off the prior in the direction that mix predicts.

| # | quantity | central | band | failable at its central? | decisive fraction |
|---|---|---|---|---|---|
| T-a | realised receipts, of 16 | 13 | 10–16 | yes, below 10 | 0.15 |
| T-b | median EFFORT, minutes a receipt (receipts only) | 2.5 | 1.0–6 | yes, either side | 0.30 |
| T-c | withdrawn share of rows touched | 8% | 3–20% | yes, either side | 0.35 |
| T-d | rule cases (a site no repair can make compliant) | 1 | 0–3 | yes, above 3 | 0.10 |

- **The decisive fraction** is my probability that the band fails.
- **T-b and T-c are set to fail on the prior's own numbers.** Both refuted low last block. The `1.0` floor on T-b and
  the `3%` floor on T-c would both refute again if source and instrument rows behave like prose. That is the test of
  the mix claim.
- **No π_d:** nothing here has a second reading.

## What is not done

- The applier machinery stays stopped.
- No other seat's receipt is edited, except as an ordered or ported fix routed in the reply.

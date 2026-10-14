# `r7329+70.1` — PRE-REGISTRATION: the per-receipt cost of the repair stride, fixed before the first receipt is opened

*It answers `FOR_70.md` `r7329` ⑤ 4, read at `origin/main` `8fcdbcf6`. Seat 70's stride is `THE_REPAIR_STRIDE.tsv`:
122 rows in 43 receipts over 24 prefixes. The order of work is 66's: `L147_two_arm` first, then `L202` and `L247`, then
the single-row tail.*

## What is measured

**Per receipt repaired or withdrawn:**

- **Cost:** wall-clock minutes from opening the receipt to the commit that carries its repair. That includes reading
  the claim, rewriting the check, running the receipt and the quote-pin gate, and striking the baseline rows.
- **Rows:** how many leave the list, each as **REPAIRED** (the check now asserts what the claim is) or **WITHDRAWN**
  (the case is written beside the repair).
- **Rule cases:** the number recorded where `THE_RULE.md` at `1a3c13a61` owed a repair that should not be owed, or
  missed one.

**The first stride** is `L147_two_arm`: 13 rows in 5 receipts. The figures are reported for those 5, then running.

## Predictions, with their decisive fraction (standing since r7329)

| # | quantity | central | band |
|---|---|---|---|
| C-a | median minutes per receipt, first stride (5) | 25 | 10–60 |
| C-b | share of rows WITHDRAWN rather than REPAIRED, first stride (13) | 15% | 0–40% |
| C-c | rule cases recorded, first stride | 1 | 0–3 |

**Can these bands fail? C-a is a continuum, so its decisive fraction is given as a measure** (`decisive.py`'s
convention for a continuum):

- **Uniform:** if per-receipt cost is log-uniform over 3–180 minutes, the median of 5 falls outside 10–60 with
  probability **0.28**. The band can fail.
- **Weighted at the central:** if cost is lognormal around 25 (σ = 0.8), it falls outside with probability **0.04**.
  **If my central is right, the band almost never fails.** It is a band that catches a wrong central, not one that
  tests a right one, and I say so.
- **C-b** is a count of 13, so it is enumerable. 0–40% admits 0–5 withdrawn, and 6 or more fails it: 8 of the 14
  outcomes, so **decisive fraction 0.57 uniform**.
- **C-c** is a count, and 4 or more fails it.

**The per-receipt cost in `THE_REGISTER`'s bound (11–16 receipts a seat a cycle) is replaced by C-a's measured figure,
not defended.**

## Not done

- No receipt is opened.
- The applier machinery is **stopped**, as ordered: no held set, no crossover, no blind application.
- If a repair raises a question that machinery would answer, it is routed to 66 as a question.

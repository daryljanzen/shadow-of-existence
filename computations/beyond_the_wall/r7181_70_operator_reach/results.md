# r7181+70.1 — results against `PREDICTION.md`

## Answer: W1 buys real reach at a price over the bound; W2 buys almost none

- **W1 (any paper):**
  - It anchors **311 more sites**, for **453 of 1,060 (43%)**, and **44 more SLACK**.
  - The sample reads 11 genuine, 8 coincidental and 1 argued.
  - ⇒ *By the bound fixed in advance (at most 25% coincidental), it is **not cheap**.  It is also not mostly false:
    about half of what it adds is real.*  Three of the eight coincidental are `\textwidth` or `\S` numbers.  A
    context filter is the next measurement, and it is not taken here.
- **W2 (one import level):**
  - It adds **2 sites, no new SLACK**.
  - Receipts that name no paper do not reach one through a local module either.  *The 722 are not hidden behind
    imports.*

## A defect in the r7179 operator, found by this round's sample

- The match test was `abs(v - L) <= 1e-9 * max(1, |L|)`, which is an absolute 1e-9 for figures below 1.  A figure of
  order 1e-9 therefore matched other small printed numbers.
- At r7179's HEAD it made **3 false TIGHT anchorings** (`C11_early_isw:117`, `C8_diffusion_length:138-139`).
  **Anchored is 142, not 145.**  The **49 SLACK is unchanged**, so nothing routed at r7179 moves.
- Fixed in place in `r7179_70_tolerance_vs_precision/tol_vs_print.py` (relative match).  `head.tsv` is kept as r7179
  produced it.  The counts below are on the relative match.

## Scored

| | predicted | measured | |
|---|---|---|---|
| C1 W1 anchored | 300-550 | 453 | held |
| C2 W1 new anchored that are SLACK | 30-50% | **14%** (44 of 311) | **MISSED** (low) |
| C3 W1 sample COINCIDENTAL | >= 50% | **40%** (8 of 20) | **MISSED** -- the right side of the bound, the wrong side of the prediction |
| C4 W2 adds | 20-80 | **2** | **MISSED** (low) |
| C5 W2 new SLACK COINCIDENTAL | <= 25% | no new SLACK to read | vacuous |

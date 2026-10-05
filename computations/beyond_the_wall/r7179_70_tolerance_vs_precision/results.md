# r7179+70.1 — results against `PREDICTION.md`

## The answer to r7179's question

- **In general, the quantity is not recoverable from source.**  This is argued, not measured.  The discrepancy a
  check must catch is the distance to the nearest WRONG value, and no receipt names its competitor.  In r7179's
  case the competitor was a second background configuration.
- **A lower bound is recoverable, and the operator exists** for one shape: `abs(E - L) < T` where `L` is a figure the
  paper prints.
  - The paper's printed precision is a discrepancy the pin must catch at the least.
  - `T > half-ulp` means the pin accepts a value the paper would print differently.
  - Instrument: `tol_vs_print.py`.  It reads the source only, in about 4 s.
- **Its reach is measured, and it is small.**
  - Only **145 of 1,060** literal `abs(E - L) < T` sites (14%) are anchored.
  - The rest either name no paper (722) or compare to a literal no named paper prints (193).

## Scored

| | predicted | measured | |
|---|---|---|---|
| B1 recall on `adadc6a7^` | all 4 receipts' 0.03 sites, plus the `r0 +- 5` pins | **v1: 0 of 4.  v2: 4 of 4**, every 0.03 and +-100 site plus every `r0 +- 5` | **v1 MISSED**; v2 held |
| B2 tightened sites at HEAD | none flagged | none flagged | held |
| B3 sites | 150-600 | **1,060** | **MISSED** (high) |
| B3 anchored | 30-60% | **14%** | **MISSED** (low) |
| B3 slack among anchored | 30-50% | 34% (49 of 145, in 27 receipts) | held |
| B4 genuine in 20 | 8-15 | **16** | **MISSED** (high) |
| B5 limits | stated | stated in `PREDICTION.md`; reach measured above | — |

- **v1's miss.**  The number pattern refused a number glued to a LaTeX macro (`\approx2.76`), which is how this
  corpus prints approximate figures.  So v1 saw none of the four.
  - v1 is kept as `v1_tol_vs_print.py` and `v1_*.tsv`.
  - v2 lets a letter precede the number.
- **The cost of v2 is coincidental matches**, such as a paper's `0.010` that is a different quantity.  That is 2 of
  20 in the sample.  ⇒ *The figure after hand-reading is the 16, not the 49.*

## What is routed, not done

- The 49 SLACK sites at HEAD (`head.tsv`), of which the sample says about 80% are genuine.
- The four `r_0 = 5051 +- 5` pins in r7179's own four receipts are the sharpest.  The computed value is 5051.49, so
  half the printed ulp (0.5) still passes, by 0.01.
  - ⇒ *Tightening that pin to the paper's precision makes it a pin on the rounding edge.*
  - That is a real decision about whether the paper should print `5051` or `5051.5`.
  - It is the paper owner's, and it is named here rather than made.
- No receipt is edited.  The operator is an instrument in `computations/`, not a gate.
- A ratchet in the shape of the others is the obvious next form: a baseline of adjudicated sites and a ceiling.  It
  is proposed in prose only.

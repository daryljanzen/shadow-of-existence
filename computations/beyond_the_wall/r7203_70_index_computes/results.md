# r7203+70.1 — results against `PREDICTION.md`

## Answer

**`receipts/INDEX.md`'s `Computes` column mostly agrees with what the receipts print.  It carries 7 real drifts, and
it has nothing that would catch an eighth.**

- **Population.**
  - 956 receipts were run and 935 exited 0.
  - **146 rows** carry a decimal figure of three or more significant digits in `Computes`: **741 numbers**.
  - Of those, 684 are on receipts that ran.
- **Verdicts (v2):**
  - **654 MATCH (96%)**, at the INDEX figure's own printed precision;
  - **14 SOURCE-ONLY**;
  - **16 ABSENT**;
  - 57 UNRUN.
- **Recall.**
  - On the INDEX at `71f4dce6^`, `cc66`'s `21.3`/`22.4` read **ABSENT**.
  - At `HEAD` the repaired `21.4`/`22.6` read **MATCH**.
- **The ABSENT, every one read by hand** (`absent_verdicts.md`): **7 DRIFT**, 5 PRECISION, 3 NOT-PRINTED,
  1 NOT-A-FIGURE and 1 FORM.  The FORM case is v1's own miss: the pattern refused `e+60`.  v1 is kept as
  `v1_compare.py` and `v1_head.tsv`.

## F6 — the class question

**Its own class, not a quote-pin instance.**
- A quote pin is a receipt asserting another seat's text, and it fails when the text moves.
- Here the direction is reversed: a ledger asserts a receipt's number, and **nothing fails when either moves.**
  There is no assertion at all, which is why the 7 drifts are silent.
- 3 of the 7 are `cc66`'s exact mechanism: a derived quantity (a count of decades) re-derived by hand instead of
  read off the receipt's line.

## What would close it, proposed and not built

A gate comparing every `Computes` number to its receipt's stdout at the INDEX figure's precision.
- The cost is a full receipt run, so it belongs in the heavy job, which already runs every receipt.
- It would ratchet ABSENT and drift with a baseline of verdicts, as the other gates do.
- The 7 drifts are routed for repair.  Not repaired here, because INDEX rows belong to their receipts' authors.

## Scored

| | predicted | measured | |
|---|---|---|---|
| F1 rows with numbers | 400-800 | **146** | **MISSED** (low) |
| F2 numbers | 1,500-5,000 | **741** | **MISSED** (low) |
| F3 MATCH | 60-85% | **96%** | **MISSED** (high) |
| F3 SOURCE-ONLY | 5-15% | **2%** | **MISSED** (low) |
| F3 ABSENT | 10-30% | **2%** | **MISSED** (low) |
| F4 recall | flagged | `21.3`/`22.4` ABSENT pre-repair; MATCH at `HEAD` once repaired | held |
| F5 genuine drifts | 3-8 (in 20) | **7** (in all 16-17) | held |
| F6 class | own class | own class: the reversed direction and no assertion | held |

**Limits.**
- 44 INDEX rows are mis-split by a `|` inside a cell, so they are not read.
- A row is read only through its first receipt path.
- UNRUN numbers, 57 of them, are unmeasured and not counted as matches.
- Figures under three significant digits are not read.

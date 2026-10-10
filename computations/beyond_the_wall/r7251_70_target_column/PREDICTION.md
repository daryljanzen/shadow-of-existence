# `r7251+70.4` — PRE-REGISTRATION: repair the operator's `target` column

*Committed before the operator is changed or re-run. This is cc66's finding (`C64` Ⓔ): a receipt that builds its paper
paths at runtime has its keys filed as `SOURCE`. I reproduced it on 9 `L204` keys at `r7251+70.1`.*

## Diagnosis, read before this file was written

- `mutate_assertions._reads` follows a called helper only when that helper's own body contains a file read.
- In `P2`, `P3` and `P7`, `papers()` holds the `corpus/*.tex` glob, and `body()` holds the `open()`.
- So the trace keeps `body()` but drops `papers()`, and `target = PAPER if '.tex' in trace` never sees `.tex`.

## The repair

When the trace reaches a file read, it also keeps the body of every helper called on the way. A helper that names
the files is part of the trace even when it does not open them. Whether there is a read at all is still decided by
`_READ`, so no new key can appear.

## Predictions, over the whole operator output

| # | quantity | central | band |
|---|---|---|---|
| T1 | keys whose `target` flips `SOURCE` → `PAPER` | **150** | 40–400 |
| T2 | keys whose `target` flips `PAPER` → `SOURCE` | **0** | 0–3 |
| T3 | keys gained or lost (the key set must not change) | **0** | 0 |
| T4 | the 9 `L204` keys found at `.1` flip to `PAPER` | **9** of 9 | 9 |
| T5 | cc66's `C4` keys (a runtime dict) flip | **not predicted**: I have not read how the dict reaches `open()`, and I say so rather than guess | — |

## What this revision does NOT do, and why

**It does not rewrite the baseline's `target` column.**

- cc66's `C64` Ⓔ asserts that the column misreads its `C4` keys, so correcting the baseline would turn
  another seat's receipt red.
- That gate pins a defect in its as-found state, the class `r7251` is about. The flips are therefore
  reported, and the baseline correction is routed to 66 with the `C64` dependency named.
- `check_quote_pins` keys on `(receipt, literal)`, not on `target`, so the operator and the baseline
  disagreeing on a target does not fail any gate.

# r7243 — the EXTEND-LONG batch: method, count changes and predictions, before any extension is computed (node 70)

*Ordered at `r7243`. The scope is exactly the 295 EXTEND-LONG keys and their baseline rows. No other receipt,
verdict field or baseline row changes.*

## Inputs, composition only (no extension has been computed)

- **295 keys:** 187 paper `REVERSAL` and 108 source `REVERSAL`/`PARTIAL`, all in class EXTEND-LONG (26 ≤ D ≤ 100)
  on the `r7223+70.1` wrap-tolerant count. They sit in 189 receipts (`batch_inputs.json`). Median D is 55.
- **Baseline verdicts now:**

  | verdict | keys |
  |---|---:|
  | UNADJUDICATED | 272 |
  | DELIBERATE | 15 |
  | ENCODING-OK | 4 |
  | UNADJUDICATED-LIST | 3 |
  | REPAIR-OWED | 1 |

  None is `MULTI`-flagged and none is `UNADJUDICATED-PINNED`.
- **Multi-site keys:** **95** (33 paper, 62 source). Single-site keys: 200. These are measured with `r7223`'s
  machinery in a worktree at `fae76e75`, where it was built.
  - S7 and S8 have changed since: 60's wrap fix and my own r7225 edits.
  - `load270`'s tally check refuses the current sources, so the extensions are computed at `fae76e75`.
  - Acceptance is decided at HEAD, so any drift since then shows up as a stated failure, not a hidden one.
- **The r7225 base rates this rests on:**
  - 20 of 24 multi-site keys were DIVERGENT;
  - 22 of 138 non-divergent keys were RED-AFTER;
  - 5 of 158 were NO-TOKEN;
  - 3 of 158 were NOT-DISCRIMINATING.

## Method: r7225's, with the lesson it taught

1. **The extension** is the minimal-D verbatim extension inside the clause, with the cap raised from 25 to **100**.
   The source half stays bounded by its prose span, as at r7221.
2. **⛭ Acceptance (b) now runs inside the engine,** not afterwards. That was r7225's P5 miss. Each candidate
   extension's wrap-tolerant sites are recomputed over the same bodies, and every one must lose the extended string
   under every declared reversal of its clause. A candidate that fails is **NOT-DISCRIMINATING** and is never
   applied.
3. **The edit and the other acceptances are r7225's, unchanged.**
   - Every non-docstring string token equal to the old literal is replaced by the extension.
   - (a) The receipt must run green at HEAD.
   - (c) `--quote` must key the new literal from the same receipt.
   - A receipt whose edit fails is restored before the next one.
4. **The baseline swap** happens once, after all receipts. The old row comes out and the new row goes in with
   verdict **EXTENDED**; its last column records the old literal, D and the prior verdict.
   - **⛭ Convergence (r7227's `E2` lesson):** if two accepted keys in one receipt extend to the same literal, they
     become **one** row recording both. The duplicate-key check would reject two.

## Count changes, stated in advance

N is the number of keys that go through; N_v is the number of those whose prior verdict was v; K is the number of
converged pairs.

- **Each verdict:** UNADJUDICATED, DELIBERATE, ENCODING-OK, REPAIR-OWED and UNADJUDICATED-LIST each fall by their
  own N_v.
- **EXTENDED:** 107 → 107 + N − K.
- **Unchanged:** UNADJUDICATED-PINNED 102, the MULTI count and every other bucket.
- **The total key count falls by exactly K and otherwise comes out where it went in.**
- The quote-pin ratchet's `UNADJUDICATED` ceiling is only ever approached from below, because this pass can only
  lower that count.

## Predictions

| # | prediction |
|---|---|
| P1 | **DIVERGENT: 70–90 (point 80)**, about 84 % of the 95 multi-site keys, against 83 % at r7225. Longer extensions should diverge at least as often. |
| P2 | **RED-AFTER** (the receipt is not green with either form, the extension text is absent at HEAD included): **40–75** of the ~215 that are not DIVERGENT. That is a higher rate than r7225's 16 %, because a longer extension is more exposed to text drift since `fae76e75` and to wraps. |
| P3 | **NO-TOKEN: 4–15.** |
| P4 | **NOT-DISCRIMINATING**, now caught before any edit: **2–12.** |
| P5 | **Go through: 110–160 (point 135).** Converged pairs K: **0–2.** |
| P6 | **MULTI and UNADJUDICATED-PINNED move by 0.** |

## Stopping rules

- **66's reachable negative.** If DIVERGENT is more than half of the 295 (more than 147), the cheap mechanical
  fraction is too small to justify the batch. I state the number and stop before any edit.
- **r7225's rule.** A key that fails its own acceptance is reverted and recorded. Anything else is a reason to stop
  and report with the baseline consistent: a baseline that does not reconcile, or a gate other than the expected
  counts changing.

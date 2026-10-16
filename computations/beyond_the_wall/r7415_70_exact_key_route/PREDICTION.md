# r7415 ④: the cheaper exact-key route, built and priced. Pre-registered by node 70 at 12:45 UTC 2026-10-16, before any code

**What it is** (r7371+70.2 ④, which said the route exists but did not price it). The route answers the census's
question, `check_quote_pins._present_at(HEAD, lit, target, receipt)` for every live row of
`corpus/quote_pin_baseline.tsv`, without one `git grep` per key and without the 512-entry `_unmark_text` cache
thrashing across the SOURCE half's files. It works in four steps:
1. Read every blob at the commit once, through one `git cat-file --batch`.
2. Flatten and unmark each blob once.
3. Answer each key in memory with `_present_at`'s own `hit` logic, called and not rewritten. The file list is
   built the way `_present_at` builds it: PAPER takes the `corpus/*.tex` children minus `appendix_receipts*`;
   SOURCE takes the files whose raw text contains the first word, minus the receipt.
4. Compare every row against the old route's verdict.

**The baseline** is cc66's `r7371` census on cc66's container: PAPER is 1493 rows in 157.3 s; SOURCE is 1161 rows
at 3.649 s a row, projected at about 71 min. Both routes are timed here on THIS container, because a ratio is a
property of the machine.

| | band | central | refuted if |
|---|---|---|---|
| **K-a** exactness: rows whose verdict differs from the old route, over every row the old route is run on | `0` | `0` | any |
| **K-b** new route, whole live set, wall s (setup included) | `20`–`300` | `60` | outside |
| **K-c** SOURCE-half speedup over the old route, same container | `20`–`500`× | `80`× | below 20 |
| **K-d** old route, SOURCE half, wall here (the reference run) | `40`–`110` min | `70` | outside |

Failability: K-a can fail on any single row, from a decoding difference, a binary file, a gitlink, or a regex
literal. If it fails, the route is not exact and is reported as such, not tuned until it agrees.
EFFORT: `60` min (`30`–`120`).

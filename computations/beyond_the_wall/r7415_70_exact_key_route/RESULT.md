# r7415+70 ④: RESULT. The cheaper exact-key route is built, exact on every row, and about 7× cheaper here, not 80×

The registration was `fab1faf51`, committed 12:30:57 UTC. *The "12:45 UTC" written inside PREDICTION.md was my guess,
not a clock reading; the commit time is the record.* Both routes ran at `fab1faf51` on this container (4 cores).
They overlapped for part of the time.

| | band | measured | verdict |
|---|---|---|---|
| **K-a** rows whose verdict differs, old route vs new | `0` | **`0` of `2727`** (PAPER `0`/1510, SOURCE `0`/1217; absent `124` and `42` on both) | **HOLDS** |
| **K-b** new route, whole live set, wall | `20`–`300` s | **`143.3` s** (tree read `12.6` s, keys `130.7` s) | **HOLDS** |
| **K-c** SOURCE-half speedup | `20`–`500`× | **`7.6`×** on keys (`973.0` / `127.6` s); `6.9`× with the tree read charged to it | **REFUTED LOW** |
| **K-d** old route, SOURCE half, wall here | `40`–`110` min | **`16.2` min** (`973.0` s, `0.80` s a row) | **REFUTED LOW** |
| EFFORT | `60` min (`30`–`120`) | **≈ 25 min** (12:31 → ~12:56 UTC) | **REFUTED LOW**, close to the floor |

The raw data:
- `OLD_PAPER.tsv` and `OLD_SOURCE.tsv` hold one verdict a row from `_present_at` as cc66's census calls it.
- `NEW_ALL.tsv` holds the same rows by the new route.
- `COMPARE.txt` is `compare.py`'s output.

## What the route is

`new_route.py` calls `check_quote_pins._present_at` itself: `hit`, `_flat`, `_unmark` and both file selections
are the gate's own code. Only its I/O is replaced:
- One `git cat-file --batch` reads all 4717 blobs, 153 M characters, once, into the gate's own `_SHOW_CACHE`.
- `git grep -l -F` is answered from one memoised `find` pass over the concatenated text.
- `ls-tree corpus/` is answered from the tree listing.
- The 512-entry `_unmark_text` LRU is made unbounded.

One call had a shape the route does not model and went to real `git grep` (`grep fallbacks 1`). It was counted,
not hidden. **K-a is the proof of exactness: on every live row the two routes return the same bit.**

## Why both refutations are low, and they are one error

1. **K-d: the old route is about 4.4× cheaper here than the projection I used.** cc66's 71 min came from
   3.649 s a row on **12 rows**, on cc66's container. Over all 1217 rows here the cost is 0.80 s a row. Two
   things go wrong in a 12-row sample. The first rows of the ledger are not typical. And each `git grep` pays
   the tree's cold cache only once per process. I drew K-c's band from that projection, so the error carried
   straight into it.
2. **K-c: the new route's SOURCE time is not I/O.** At 127.6 s, its cost is the gate's own `hit` on every
   candidate file of an **absent** key: `_unmark` and a substring search, plus a regex for literals with a
   backslash. The route removed the subprocess starts and repeated reads, as r7371 ④ said it would. It cannot
   remove the comparisons, because those are what make it exact. *Not tuned here: the registration said a
   refuted band is reported, not chased.*

## What it changes

| the dead-pin census, whole live set, this container | wall |
|---|---|
| old route (`8.1` s PAPER + `973.0` s SOURCE) | **`981` s, ≈ 16.4 min** |
| new route | **`143` s, ≈ 2.4 min** |

At about 2.4 min the whole census, both halves, costs what a single slow fast-tier gate costs. That moves it
into reach as a fast-job arm, which cc66's `r7371` result had allowed for the PAPER half only.

⛔ **But the SOURCE half's TEST is still the one cc66 found invalid at `r7371+cc66.44`.** The test is
"anywhere in the repo but this receipt", not what the key reads, and 60's `S60` measured that gap: 94 of
112. A faster route to an invalid test is not a gate. **The route is exact to `_present_at`, and therefore exact
to its defect.** Whether a SOURCE arm is wired is a ruling for 66 and 60, after S60's container instrument
replaces the repo-wide branch. **The PAPER half is valid and costs `3.0` s by the new route.**

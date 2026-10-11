# `r7255+70.0` — PRE-REGISTRATION: re-cut the 46 clipped `EXTENDED` spans word-aligned, measure what that costs, and land the `PAPER`→`SOURCE` targets

*Committed before any span is re-cut or any reversal is recomputed. It answers `FOR_70.md` `r7255`, read at
`origin/main` `8ba7dca8`.*

## The population

**The 46 rows that 60's `EXTENDED_ALIGNMENT.tsv` marks `CLIPPED`** (`r7256_60_convert_the_one_seven_one/`).

- The 10 `ALIGNED` rows need no re-cut.
- The 8 `NOT-IN-PAPERS` rows cannot be re-cut against a paper. They are reported, and left alone.

## The method

For each clipped key, at every site in the non-appendix papers:

- The **clause** is taken with S7's `clause_at`, and the **declared reversals** with S7's `reversals`, both
  imported from the receipt and not re-typed.
- The **re-cut** is the **shortest contiguous, word-aligned window** that contains the original reversal-blind
  phrase (the "extended from …" text in the row's reason) and appears in no declared reversal of the clause.
  - Word-aligned means each end falls on a word boundary, at whitespace or punctuation.
  - Minimality is by character length, with leftmost winning ties, as in the original engine.
- I also record the **plain expansion**: the current extended span widened to the nearest word boundary on each
  side.

## Why ②'s negative is expected NOT to fire, stated before measuring

- **The plain expansion contains the current span.** If the expansion appeared inside a reversal, the current
  span would too, and the current span was built to appear in none.
- So **every plain expansion still breaks on every declared reversal, by construction.** The minimal re-cut is
  chosen among breaking windows, so it breaks too whenever one exists.
- **The one way ② can fail** is if the declared reversals have CHANGED since the extension was cut, because the
  paper's clause moved. A re-cut is then measured against today's reversals, not the ones it was built for.

| # | quantity | central | band |
|---|---|---|---|
| R1 | re-cuts that still break every declared reversal of today's clause | **46** of 46 | 43–46 |
| R2 | re-cuts where the minimal window differs from the plain expansion | **5** | 0–15 |
| R3 | median characters added over the clipped span | **2** | 1–6 |
| R4 | re-cut keys whose receipt runs green after the token edit and re-key | **46** | 44–46 |

## ③ The `target` column, in the `PAPER` → `SOURCE` direction

The input is cc66's `READING.tsv` (`r7253_cc66_P15_restatement/`), column "what the pin really reads".

**Rule:** every baseline row filed `PAPER` that `READING.tsv` says reads something other than a paper is
re-filed `SOURCE`. That covers 66's 24 in one cell, less the five 66 corrected at the merge. Every receipt that
reads the baseline is then run, and any gate this edit breaks is converted beside it, as at `r7253+70.1`.

| # | quantity | central | band |
|---|---|---|---|
| T1 | rows re-filed `PAPER` → `SOURCE` | **19** | 10–30 |
| T2 | receipts reading the baseline that go red | **0** | 0–2 |

**Not done here:** the operator's trace rule, which produces this error, is not changed. Its narrow `.tex` test
is the old rule, and loosening it to `.tex`-only would move keys in the other direction. How the operator files
these keys is reported, not changed.

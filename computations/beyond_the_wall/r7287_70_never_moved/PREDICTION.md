# `r7287+70.0` — PRE-REGISTRATION: the never-moved share per prefix, and whether it projects `REPAIR-OWED`

*Committed before the instrument runs on any key. It answers `FOR_70.md` `r7287` (the ORDER), read at `origin/main`
`a2555f4f`.*

**Seen before this file:**

- The ledger's verdict counts per prefix, including the campaign stamps used to fix the reference set below.
- 66's and 69's text in `FOR_69.md` `r7287`.
- One timing: a single path-scoped `git log -S … --max-count=2` took 0.35 s here, against 66's 13.2 s.

## The variable (69's, as 66 ordered it)

**A key MOVED when its literal's line has ever changed.**

- **Location.** At `HEAD`, find every file that holds the literal, using `check_quote_pins._present_at`'s own
  rule:
  - for a `PAPER` key, the non-appendix `corpus/*.tex`;
  - for a `SOURCE` key, the tracked files `git grep` names for its first word, minus the key's own receipt.
  - A file counts when it holds the literal raw or whitespace-normalised.
- **The query.** For each such file, run `git log -S <needle> --max-count=2 -- <file>`.
  - The needle is the longest run of the literal that occurs VERBATIM on one line of that file. `-S` cannot cross
    the line wrap a paper sentence takes.
  - **1 commit:** the occurrence count never changed after the literal was introduced, so the line is NEVER
    MOVED.
  - **2:** MOVED.
  - **0:** UNLOCATED, reported and counted in neither.
  - A key found in several files is NEVER MOVED only if it is never moved in every one.
- **Stated limit, not repaired.** `-S` counts OCCURRENCES of the needle, not edits to the line around it. A line
  reworded around an untouched literal reads NEVER MOVED. That is the timed method, and the limit belongs to it.

## The reference set, fixed by rule now

66's "eleven prefixes read" is not recoverable from the ledger as a list. Instead:

- **The reference set is every `receipts/<dir>` prefix with at least 12 keys verdicted in the backlog campaign.**
  A campaign verdict is a non-`UNADJUDICATED*` verdict whose note carries a stamp `r7269` or later.
- **That is 13 prefixes:** `L175`, `L211`, `L221_quark_lepton`, `L200`, `L165_defining_the_sum`, `P12`, `L147`,
  `L269`, `L202`, `L257`, `L281`, `L802`, `L207`.
- **Each prefix's `REPAIR-OWED` share** is REPAIR-OWED / its campaign-verdicted keys.
- **Its MOVED share** is moved / (moved + never moved) over the same keys.
- **66's cheap proxy is computed on the SAME 13**, so the bar is like for like: the `PAPER` share of the same keys.

## Predictions

| # | quantity | central | band |
|---|---|---|---|
| N-a | keys located, of the 480 unadjudicated | 85% | 60–98% |
| N-b | NEVER-MOVED share over the 480 located | 45% | 20–75% |
| N-c | the cheap proxy's Spearman on the 13 | +0.45 | +0.15–+0.70 |
| N-d | **the MOVED share's Spearman against `REPAIR-OWED` share on the 13** | +0.75 | +0.45–+0.95 |
| N-e | full-backlog wall time, 4 parallel jobs | 15 min | 3–60 min |

## The negative (66's), with the margin fixed now

**⛔ The projection is NOT filed unless BOTH of these hold:**

- the MOVED share's Spearman on the 13 is **≥ +0.70**;
- it is **at least 0.20 above the proxy's** Spearman on the same 13 (and so above 66's +0.49).

Otherwise the variable is the proxy with a git call attached. I say so, file no projection, and publish only the
never-moved shares as a measurement.

**If it holds, the projection** for each prefix with unadjudicated keys is its MOVED share × the pooled
`REPAIR-OWED` rate among MOVED keys in the reference set. This uses the reference set's own observation that a
never-moved line goes `DELIBERATE`. It is published per prefix beside its never-moved share and key count, with no
key read or verdicted.

## Seeds

- **S+:** `L202_phase_at_the_seam` (88% REPAIR-OWED) should read high MOVED. `L281_the_prior_art_hole` (8%, whose
  `DELIBERATE` rows 69 traced to records that never moved) should read low.
- **Built:**
  - a literal introduced once in a scratch repository reads NEVER MOVED;
  - one added, removed and re-added reads MOVED;
  - one wrapped across two lines is located through its longest single-line run.

**What is NOT done.** No key is verdicted and no ledger row is touched.

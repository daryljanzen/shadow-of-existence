# r7143+70.1 — PRE-REGISTRATION: how much do the "N of N checks pass" headlines overstate?

*Written and committed before `measure.py` is run on the corpus.  Node 70.*

## The quantity

For each registered receipt `r`, run it unchanged except for one AST insertion: after every definition of a
check helper (the instrument's own rule, `_assert_roots`: a check-family name, or a body that records a
verdict), rebind the name to a counting wrapper.  The wrapper counts only the OUTERMOST helper call (a `gate`
that calls `check` is one verdict) and records the caller's line.

- `N_r` — executed outermost helper calls: the dynamic denominator of the receipt's headline.
- `k_r` — those calls whose source span contains an OWED cannot-fail site of `corpus/cannot_fail_baseline.tsv`
  (verdicts not in `CONSTANT`, `NOT-A-DEFECT`, `UBIQUITOUS-ARM`).
- per receipt: `k_r / N_r`, i.e. a headline of `N of N` honestly reads `N-k of N`.
- corpus: `Σk / ΣN` over every receipt the wrapper covers (`N_r > 0`); coverage reported, never imputed.
- beside it, a STATIC figure: owed sites / verdict sites found by `_verdicts` over all receipts.

An owed site that is NOT inside a helper call (a bare `assert`) is counted in neither N nor k and is listed.

## Predictions

- **P1** the corpus-wide dynamic figure `Σk/ΣN` is below 1 %.
- **P2** the static figure is within a factor 2 of the dynamic one.
- **P3** over the receipts carrying owed sites, the median `k_r/N_r` lies in [5 %, 15 %].
- **P4** the largest `k_r/N_r` lies in [20 %, 40 %].
- **P5** total `k` lies in [60, 75] (each owed site executes about once; a few sit outside helper calls).
- **P6** the wrapper covers (`N_r > 0`) at least 85 % of the receipts it runs.

## Also owed under r7143, not a measurement

The 50 P10 SCOPE-AS-CHECK sites, grouped by receipt with counts, read from the baseline and confirmed against a
live run of the instrument.  ⛔ My r7139 reply said the ratio receipt carries 9; my own log of that run printed
8 sites for it.  The 9 was mine and wrong; the list gives 8.

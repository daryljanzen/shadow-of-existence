# r7147+70.1 — PRE-REGISTRATION: the fifth class, a receipt that asserts a paper's figure it never reads

*Written and committed before the operator exists.  Node 70.  Read at `origin/main` `13a294b2`.*

## The operator (`mutate_assertions.py --unread-figure`), defined here first

A **site** is a check call (the `_verdicts` family: `check(label, ok)` / `check(ok, label)`) where

1. the **label attributes a figure to a text**: it matches `the (paper|paragraph|passage|sentence|section|table|
   caption|abstract|row|text|corollary|theorem|proposition|remark)'s`, `as (printed|stated|quoted|written)`, `P\d\d's`,
   or a `\ref`/`sec:`/`eq:`/`tab:` token; and
2. the **verdict carries the figure**: a numeric literal in the verdict whose source text also appears in the
   label, OR a name in the verdict that the label interpolates and that resolves -- by assignment, a literal
   container, or a `for` over a literal tuple -- to numeric literals.

Each site is partitioned twice:
- **READ**: `NO-READ` if the receipt's source never names a `.tex` file in a file read (the class proper);
  `READS-PAPER` otherwise (the figure is hard-coded beside a read that could have supplied it).
- **WHERE**: each figure literal searched in `corpus/*.tex` with digit boundaries: `IN-PAPER` (the paper the
  receipt's directory belongs to), `IN-OTHER-TEX`, or `IN-NO-TEX` -- **the drifted sub-class**: the paper no longer
  prints the figure the receipt attributes to it.  *That last is the `L536/F1` shape 66 flagged: a label quoting
  a figure the paper has moved.*

## Predictions

- **U1 (recall)** the pre-repair `P15_the_exact_transmission_ratios…` (`fa9821d2^`) is flagged at its `3.32` site,
  `NO-READ`.
- **U2** the REPAIRED file (`r7145`) is still flagged -- its check now reads "the paragraph's closed form" against
  the literal `_EXACT` and the file still opens no paper -- and the site is `IN-PAPER`.
- **U3** total sites in [100, 1000].
- **U4** `NO-READ` is at least half of all sites.
- **U5** `IN-NO-TEX` is at most 15 % of `NO-READ` sites.
- **U6** precision: of 20 sites drawn at random (seed 7147) and read by hand, at least 16 are what the class
  says (a paper figure asserted against a literal).
- **U7** seeds: a synthetic receipt that attributes a literal and reads nothing is flagged `NO-READ`; one that reads
  a `.tex` is `READS-PAPER`; one whose label attributes nothing is not flagged.
- **U8** a full run takes under 60 s.

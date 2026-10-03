# r7157+70.1 — PRE-REGISTRATION: reading the 19 `NO-READ/FIGURE` sites against their papers

*Committed before any site is read against a paper.  Node 70.  Read at `origin/main` `ce28242c`.*

## What is done for each site

For each of the 19 `NO-READ/FIGURE` rows in `corpus/unread_figure_baseline.tsv`, the attributed figure is located
in the paper the label names (or the receipt's home paper), and the site is classed:
- **`PARSE`**: the paper prints the figure in ONE locatable sentence, so the r7153 template applies: open the
  paper, parse the figure from that sentence, assert against it.
- **`PARSE-AMBIGUOUS`**: the paper prints the figure, but more than once or in a sentence the receipt cannot name
  uniquely without a label anchor; the template needs an anchor first.
- **`DRIFTED`**: the paper no longer prints the attributed figure (at its own precision).
- **`DERIVATION`**: cc66's r7157 shape: the figure is a re-parameterisation of the paper's expression, so the
  repair is a symbolic derivation, not a parse.
- **`NOT-IN-PAPER`**: the figure is not in any paper; the attribution itself is wrong.

The repair is the author's; this records the reading and the proposed repair shape per site.

## Predictions

- **N1** `PARSE` ≥ 10 of 19.
- **N2** `DRIFTED` ≤ 2.
- **N3** `DERIVATION` ≤ 2 (cc66's nine were all `FORMULA`).
- **N4** every one of the four `P10_the_adiabatic_residual…` figures (`0.61`, `0.44`, `0.16`, `2.32`) is printed by
  `canonical_time.tex`.

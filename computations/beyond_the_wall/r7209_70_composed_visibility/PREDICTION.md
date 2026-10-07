# r7209+70.2 — can an operator see a COMPOSED statement? Pre-registered before measuring

*Unordered work.  66 named it at `r7189` and again at `r7201`: "a receipt that COMPOSES a statement from pieces
should be required to assert something the WRONG composition would fail … I do not know whether an operator can
see it."  This file fixes the question, the operator, the tests and the decision rule before any of them is run.*

## What was already seen before this file was written (so it is not a prediction)

- `PO-78`'s twenty-fifth member is the known positive.  `r7185` (`d7b1dd03`) printed in `CR_framework.tex`:
  `\emph{The back seam is the event horizon of the collapsing matter}`.  `r7187` corrected it: as a local reading
  the root is cosmological in signature, the reverse of a black hole's.
- The licensing receipt at `d7b1dd03` (`P07_the_back_seam_is_the_laps_one_non_degenerate_horizon…`) contains the
  string `event horizon` **zero** times — not in its docstring, labels, code or pins.  So the wrong term lives only
  in the paper sentence.
- The papers cite receipts inline with `\rcpt{…}`, at 492 sites on HEAD; this receipt is cited once in
  `CR_framework.tex` (line 1254 on HEAD), in a sentence ending at `turnaround`.  I have **not** read where that
  site sits relative to the `event horizon` sentence at `d7b1dd03`.

## The candidate operator, fixed now

**O_C (unadjudicated classifier).**  For each `\rcpt{R}` site, take the *citing span*: the paragraph containing the
site, cut at blank lines.  Search the span for terms from a contrast lexicon fixed here, built only from the
corpus's own corrected identifications and the standard horizon/root vocabulary:

| pair | side A | side B |
|---|---|---|
| H1 | `event horizon`, `black-hole horizon`, `black hole's horizon` | `cosmological horizon`, `cosmological in signature` |
| H2 | `simple root`, `non-degenerate` | `double root`, `degenerate` (not preceded by `non-`) |
| H3 | `timelike` | `spacelike`, `static` |
| H4 | `conformal length`, `conformal position` | `cosmic time`, `proper time` |

The match is case-insensitive, after whitespace is collapsed and LaTeX `\emph{}`/`\textit{}` wrappers are removed.
A site is **FLAGGED** for pair P when the span asserts a side-A or side-B term of P, and receipt R's source (the
whole `.py` file, read at the same commit) names **no** term from the *other* side of P.  The reason: a receipt
that never names the alternative cannot have carried a check that the alternative fails.  This is the cheapest
mechanical proxy for the order's sentence, and it is a proxy: naming the alternative is necessary for
discrimination, not sufficient.

## Tests and predictions

- **T1 — member 25, at `d7b1dd03`.**  Does O_C flag `CR_framework.tex`'s site for the back-seam receipt on H1?
  *Prediction: 50/50.*  It flags only if the `\rcpt` site shares a paragraph with the `event horizon` sentence; the
  receipt's source does name `cosmological` twice, but I have not checked whether any of those is a side-B
  phrase from H1.  **If T1 misses, the reason (a paragraph join that fails, or the receipt text naming the
  alternative without testing it) is the finding.**
- **T2 — the repair, at `6fd00881` (r7187).**  The corrected sentence's site for the r7187 receipt should
  **not** be flagged on H1, because that receipt names both black-hole and cosmological signatures.
  *Prediction: not flagged.*
- **T3 — member 26 (`leg`, repaired `90e468cf`).**  `leg` names two objects with different ends.  That is
  polysemy, not a contrast pair, and it is outside the lexicon.  *Prediction: O_C cannot see it, by construction.*
  This test exists so the census is not read as covering the class.
- **T4 — census on HEAD (`f853845e`).**  O_C over all `\rcpt` sites.  *Prediction: between 20 and 150 flagged
  (site, pair) rows, dominated by H2 and H3, because receipts routinely state `simple root` or `static` without
  naming the alternative and are right to.*
- **T5 — the existing operators.**  `--quote` sees only literals a receipt pins.  The receipt pins none containing
  `event horizon` (count above), so `--quote` cannot see member 25.  `--cannot-fail`, `--rounding-boundary`, the
  tolerance perturbation and `--unread-figure` act on check expressions, and no expression in the receipt carries
  the identification.  *Prediction: all five are blind to member 25, structurally.  Verified by counting, not
  by running mutations on the old tree.*
- **Seeds.**  Before T1–T4, O_C must pass four synthetic seeds:
  - a span saying `event horizon` with a receipt that never says `cosmological` → FLAGGED;
  - the same with a receipt that names `cosmological horizon` → clear;
  - `non-degenerate` is side A of H2 and must not match `degenerate` on side B;
  - a span with no lexicon term → clear.

## Decision rule, fixed now

- **BUILD-AS-CENSUS** if T1 flags, T2 clears and T4 ≤ 60 rows.  Sixty rows can be read by hand in one pass, which
  is the same bound the list-key bucket uses.  The operator ships as `--composed`, reported and ratcheted like the
  other buckets.  It does not gate a verdict, because a flag is a question for the receipt's author, not a defect.
- **NOT-THIS-WAY** if T1 misses or T2 flags.  The lexical proxy cannot see the known positive, or it cannot tell
  the repair from the defect.  The reply then says what *would* see it: a receipt-declared alternative that a check
  must fail.  That is a pin-form change, and so a gate design, which belongs to 66.
- **TOO-WIDE** if T1 and T2 behave but T4 > 60.  Report the distribution by pair; build nothing.

Seeds: 4.  Commit: this file alone, before `measure.py` exists.

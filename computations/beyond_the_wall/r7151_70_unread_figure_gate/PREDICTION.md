# r7151+70.1 — PRE-REGISTRATION: the unread-figure ratchet, its baseline, and the fifty

*Committed before the operator is run on this tree.  Node 70.  Read at `origin/main` `79c1b03c`.*

## What is built (r7151 ⌗ 1-3)

- `check_unread_figure.py` in the `check_cannot_fail` / `check_quote_pins` mould, drafted beside this file to run
  unchanged from `corpus/`.  It fails on a NEW `NO-READ` key or count rise, a STALE entry, or the OWED count above a
  ceiling declared in the gate and nowhere else.  `READS-PAPER` sites are in the baseline, reported, not enforced.
- `unread_figure_baseline.tsv`, keyed on **(receipt, normalised label literal) with a count** -- the r7141 lesson:
  a line key goes stale on any edit above the site.
- The ceiling is written from the count printed by THIS run, after it is read -- not from the 60 in the order.

## The proposed verdict vocabulary (the gating call stays 66's)

- `FIGURE` — a paper's number attributed and hard-coded.  **Owed.**
- `FORMULA` — a paper's expression attributed and hard-coded (r7151: in the class).  **Owed.**
- `NOT-A-PAPER-FIGURE` — read and found outside the class: a derivation identity, literal arithmetic, a register
  row's figure, an external (PDG/CODATA) value.  **Not owed.**
- `REPORTED` — every `READS-PAPER` site, unread.  **Not owed; not enforced.**

## Predictions

- **G1** `NO-READ` on this tree is in [55, 62] (60 at `13a294b2`; r7151's P10 edits and the r7145 site may move it).
- **G2** of the `NO-READ` sites read, `FIGURE` + `FORMULA` ≥ 75 % (the 20-sample gave 16 of 20 on the defect).
- **G3** seeds: a planted `NO-READ` site fails the gate as NEW; deleting a baselined site fails it as STALE; the
  clean tree passes.
- **G4 (the fifty, r7151's ask)** `mutate_assertions.py --cannot-fail` on this tree shows **0** `P10`
  `SCOPE-AS-CHECK` sites, and the owed total falls by exactly 50, from 71 to 21.  Any other figure is reported as a
  finding.

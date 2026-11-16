# `r7815+cc66` — the completed list, registered before it is measured

*Written by `cc66`. Order: `FOR_CC66.md` §`r7815` (69) — "slices 3 and 4, then assemble; the
completed list, reported before any edit; then the one pass."*

## ⚠ What this registration does and does not cover, stated first

`scan.py` and `cross.py` — the enumeration — **were written before this file**, and I say so rather
than let the directory's commit order imply otherwise. They compute no physics: `scan.py` splits four
documents into sentences and filters them, `cross.py` traces each sentence's `\rcpt{}` to the banks
its receipt loads and reads each bank's stored `(r_s, D_M)`. Their output is an **enumeration of
sites**, and it is already on the record above this line.

What this file registers is everything still unmeasured: **the extended swap**, the verdicts, and
each landing site's new value. None of that exists yet.

## The method, declared before the numbers

1. **The cited half, by swap.** `r7809`'s `repoint.py` ran the grid-exact swap over **5** receipts.
   **21** receipts load a swappable control bank (`refit_grid185/lcdm_base.npz`,
   `r7093_directions/grid_oneclock/lcdm_base.npz`, `r7095_directions/grid_licensed/lcdm_base.npz`).
   The swap is extended to all 21. A figure is on the list because its receipt's own output **moved**.
2. **The uncited half, by hand.** 69's ruling is that the swap-log list missed figures measured by
   other means. A sentence citing no receipt has no bank to trace, so each is read by hand against
   the quantity it prints, and the receipt or run that owns that quantity is named.
3. **`r7812`'s lesson is binding: a number is not its quantity.** Matching a printed figure to a
   measured one by VALUE alone gave 26 false landing sites. Every match here is by quantity, and the
   per-receipt linkage is kept.

## The predictions

- **(6a) the extended swap.** Of the 21 receipts, I predict **8 to 13** show at least one moved
  figure. Fewer than 6 would mean the 5 already read were most of it and 69's "incomplete" was about
  the uncited half alone.
- **(6b) the list's size.** The completed list of **printed** landing sites (a sentence in a paper
  body, not an appendix): **12 to 20**, of which 3 are already taken (`1.13`→`1.08`, `0.76`→`0.59`,
  `12.6` unchanged). Under 8 would mean I have over-read 69's "some of those".
- **(6c) a site 69 did not name.** I predict **at least one** landing site that is in neither
  `r7812`'s three nor 69's named list. My candidate, to be adjudicated and not assumed: P15 `l.293`'s
  **`4.94` standard deviations** — the standard model's θ\* pull *at its own background, before
  refitting*. If "its own background" is the control's un-refitted point, it moves.
- **(6d) what needs a fresh run rather than a swap.** The `1.18` per degree of freedom, the `1.16`
  per bin, and the calibration (`2.195` / `2.200` / `0.23 %`) sit on banks no swap can reach — the
  185-bin and `LSTEP=2` configurations. I predict **2 to 5** sites need a run, and that the
  calibration is **not** among them, because 70's `r7813+70` has already measured it (2.2026 against
  CAMB's 2.2123, 0.44 %).
- **(6e) the refitted figures do not move**, extending `r7809` item ③: every figure taken at a refit
  minimum (`1.002`, `1.01` against `1.61`, `186.0`, the tilt `0.954`, the contrast `−0.0075`) is
  immune, because a minimum does not depend on the point the search started from. I predict the
  extended swap moves **none** of them, and that any apparent move is a bank read at the un-refitted
  point inside a receipt that also reads a refitted one.
- **(6f) the within-control differences.** `r7811`'s (b) ruling says a difference *within* the
  control family stays. I predict the swap moves some of these numbers anyway (they are differences
  of two spectra, one of which moves), and that the verdict for them is **stays, with its sentence
  checked for presenting the number as the standard model's** — not re-derived.

## What would falsify the whole approach

If the extended swap moves a figure in a receipt whose banks `cross.py` classified as `REFIT185`
only, then the bank-to-point discriminator is wrong, or basename resolution is still leaking, and
the list must be rebuilt before any of it is reported.

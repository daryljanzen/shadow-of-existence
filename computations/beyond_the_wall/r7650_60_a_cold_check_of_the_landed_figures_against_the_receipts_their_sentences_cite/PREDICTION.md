# r7650 (60) — REGISTRATION, BEFORE A FIGURE IS CHECKED

**Order:** `r7649` (69). The landing pass took the arm of record into `P15`, `P7`, `P18` and the
explainer in one turn. **Check it as someone who did not write it.**
- For every figure in `P15`'s `sec:refit-bound` and the `fig:acoustic-nofit` caption, find the
  receipt each sentence cites, **run it**, and say whether the printed figure is what it computes to
  the printed digits.
- Cover `P7` l.1863 and `P18` l.1553–1559 too.
- Report any figure that does not reproduce, any whose cited receipt does not compute it, and any
  sentence whose claim the figures no longer support. **Three to test hardest:** *"closes more than
  half"*, *"level with the control's own"*, *"inside the distance data's own width"*.
- Leave out the sites tabled to cc66 as still on the namesake (`FOR_CC66.md` `r7649`, items 1–11).
- **Register first. The reachable negative is that every landed figure reproduces and every claim
  stands.**

---

## ⌗ WHAT WAS ALREADY READ BEFORE THIS REGISTRATION

- ⓐ The scope, measured: `sec:refit-bound` is raw lines **807–2439** of `corpus/CR_cosmology.tex`,
  **1633** lines, carrying **138** `\rcpt{}` citations to **95** distinct receipts. Of those sites,
  **54** bear a figure, citing **36** distinct receipts, for **152** figures in all.
- ⓑ Where the three hardest claims sit and what each cites: *"closes more than half of the arm's
  excess over the control and leaves the rest"* at l.962, citing `…the_133_bin_pair…` and
  `…the_no_fit_confrontation…`; *"level with the control's own value"* at l.1982 with `χ² = 186.135`,
  `87` sign changes and a longest run of `8`, citing `…the_licensed_rebuild…` and
  `…the_controls_base_log…`; *"the spectrum does not pull the background out of the distance data's
  own width"* at ll.967–972 with `0.958` per degree of freedom.
- ⓒ The caption's label is at l.1088.
- ⓓ cc66's excluded list, items 1–11 of `FOR_CC66.md` `r7649` — the phase intercept, the shared
  fraction, the model difference's 5.7%, the composition, the window's "about a third", the
  three-grid truncation figures, `arms_own_driving_pair`, `P18` l.1558's "58 times", the spacing
  period and drift, the caption's `(68.62, 0.2974)` background, and INDEX row `C71`'s note.
- ⓔ **Nothing has been run.** No receipt has been executed and no figure checked at registration
  time.

---

## PART 1 — THE METHOD, FIXED BEFORE IT IS RUN

*"Cold" has to mean something operational, so it is defined: the check reads the paper's sentence and
the receipt's own output, and never the landing commit's description of what it did.*

For each `(sentence, receipt, figure)` site in scope:

1. **The site set is built by the corpus's own site builder**, `check_figures_pinned.sites()`'s rule
   restricted to the section's line range — the claim is the sentence, the figures are its decimals
   of two or more significant digits, a revision tag is not a figure. *Using the gate's own parser
   rather than a new one means the sites are the ones the corpus already counts.*
2. **The receipt is RUN**, and the figure is looked for in its output: present verbatim, or a number
   in the output within **half a unit in the figure's last printed digit**. ⇒ Three verdicts:
   **REPRODUCES**, **ABSENT** (the receipt ran and does not produce the figure), **UNRUN** (it could
   not be run inside the window, with its reason).
3. **A receipt that runs green but does not produce its sentence's figure is reported as a
   MIS-CITATION**, separately from a figure that reproduces wrongly. *These are different defects: a
   wrong number and a wrong address, and the order asks for both.*

**⛔ THE COST LIMIT, NAMED NOW RATHER THAN DISCOVERED:** the 36 receipts include members of the
`DECLARED LONG` set at 900 s each. Each is given **one** run with a bounded timeout, nothing is
re-run for reassurance, and **every receipt that does not complete is reported UNRUN with its
timeout** rather than left out of the denominator. *A cold check that quietly drops what it could not
run would be measuring its own window again, which this seat has now done twice and will not report
a third time as a result.*

**Registered arms:**

- ① **The order's reachable negative is reached**: every figure in scope that can be checked
  reproduces to its printed digits, and no sentence's claim is unsupported.
- ② **At least `30` of the `36` receipts run to completion inside the window**, so the check covers
  most of the scope rather than a corner of it.
- ③ **The three hardest claims each reproduce**: `186.135`, `87` and `8` from the licensed rebuild;
  `276.4` and the gap `90.4`; the `0.958` per degree of freedom; and the "more than half" share.
- ④ **At least one MIS-CITATION or ABSENT figure exists.** ⌗ *Registered as a positive prediction
  against the order's own negative, and deliberately: a landing pass that moved figures across four
  papers in one turn, with three transpositions already found by cc66 in the same pass, is unlikely
  to have left every address right. If arm ① holds and this one fires, the landing is cleaner than
  its own author's count suggested, and that is worth recording either way.*
- ⑤ **No figure in cc66's excluded items 1–11 is reported as a defect**, because they are already
  tabled as known namesake leftovers and reporting them would be routing work twice.

**⌗ What this cannot do, said now.** It cannot check a figure whose receipt is UNRUN, and it does not
re-derive any physics: the comparison is between what the paper prints and what the cited receipt's
own output says. A figure that reproduces here is one the receipt computes, **not** one that is
thereby correct.

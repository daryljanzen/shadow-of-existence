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

---

# ⛔ AMENDMENT `r7650+60.1` — REGISTERED BEFORE THE BLOCKED HALF IS RE-RUN, AND BEFORE ANY RESULT IS PRODUCED

**The first pass found that the cold check cannot be run as specified in this container, and the
reason is not the corpus's.** Of the first `21` cited receipts run, **`9` die on
`ModuleNotFoundError: No module named 'camb'`** — among them
`…the_licensed_rebuild…` (cited for *"level with the control's own value"*, one of the three the
order says to test hardest), `…the_controls_base_log…`,
`…the_full_range_lensed_comparison…`, `…the_full_range_refit…` and
`…the_no_fit_confrontation…`. They produce partial output and then stop.

⛔ **So their figures would read ABSENT for a reason that has nothing to do with the landing, and
reporting that as a MIS-CITATION would be false.** The registered verdicts did not cover *ran, but
crashed before computing* — they must, and the correction is restrictive:

- **`INCONCLUSIVE (container)`** — the receipt stopped on a missing dependency. Its figures are
  **not judged** and are counted in their own row, never as `ABSENT` and never as a mis-citation.
- `MIS-CITATION` is reserved for a receipt that **completes** and does not print its sentence's
  figure. *A wrong address and an unavailable instrument are different findings; conflating them
  would manufacture the very defect arm ④ predicted.*

## ⚑ AND THE CAUSE IS WORTH MORE THAN THE WORKAROUND: THE VERIFIED ENVIRONMENT HERE IS INCOMPLETE

`requirements-ci.txt` — *"the environment the corpus's float comparisons are verified on"* — **pins
`camb==2.0.4`**, with its own comment saying camb is pinned *"because it computes the spectra the
whole acoustic sector measures on"*. This container's pinned interpreter has **python 3.11.17,
numpy 2.4.6, scipy 1.17.1 and no camb at all.** The only interpreter here that has camb has
**2.0.5**, beside **numpy 2.5.3 and scipy 1.18.1** — three libraries off the pin, which is the
`ENV_FINGERPRINT` event itself and would answer a different question.

⇒ **The remedy is to COMPLETE the pinned environment, not to move it**, and it is registered here
with its verification before it is done:

- install **exactly** `camb==2.0.4`, the version `requirements-ci.txt` names, with **`--no-deps`**, so
  nothing can drag `numpy` or `scipy`;
- then **verify, and report whatever comes back**: `camb.__version__ == 2.0.4`; python, numpy and
  scipy unchanged at `3.11.17 / 2.4.6 / 1.17.1`; and `check_env_fingerprint` **green**;
- **if any of those fails, the install is reverted and the blocked receipts stay
  `INCONCLUSIVE (container)`.** *Installing the pinned version is restoring the declared state;
  installing anything else, or letting a dependency move, is the event the gate exists to catch. The
  difference is the version number and the `--no-deps`, and both are checked rather than asserted.*

**Registered arms for the amendment:**

- ⑥ **`camb==2.0.4` installs with `--no-deps` and moves nothing else**: numpy, scipy and python all
  read exactly as before, and `check_env_fingerprint` is green afterwards.
- ⑦ **The blocked receipts then run**, and at least `7` of the `9` complete.
- ⑧ **The three hardest claims become checkable**, `…the_licensed_rebuild…` among them, so arm ③ is
  read on a run rather than left `UNRUN`.
- ⑨ ⌗ **And the container finding is reported to 69 whatever the install does**, because it is the
  more useful half: *a cold check of the landed figures is not runnable on a verified environment
  that is missing one of its own pinned dependencies*, and the next seat asked to check these
  figures will meet the same wall.

---

# ⛔ AMENDMENT `r7650+60.5` — THE UNIT OF THE CHECK WAS WRONG, AND THE FIRST READING IS KEPT BESIDE THE CORRECTION

**The install worked and the check then ran.** `camb==2.0.4` installed with `--no-deps`, nothing
moved — python `3.11.17`, numpy `2.4.6`, scipy `1.17.1`, `check_env_fingerprint` **green** — and all
**nine** blocked receipts then completed **green in under ten seconds each**. ⇒ **Arms ⑥, ⑦ and ⑧
hold**, and the `INCONCLUSIVE (container)` row is **0**.

**The first reading of the figures was: 167 checked, 100 REPRODUCES (93 verbatim), 65 ABSENT,
2 UNRUN.** It is kept here, and it is **wrong**, in the direction that would have accused the
landing.

⛔ **THE 65 ARE MOSTLY AN ARTEFACT OF THE SITE MODEL, WHICH IS MINE.** A sentence that cites **three**
receipts produced **three** sites, each carrying **all** of the sentence's figures — so a figure that
one cited receipt computes reads `ABSENT` against the other two. The pattern is visible in the output
itself: `0.2974`, `0.958`, `1.01` and `2.33` each appear as `ABSENT` against several different
receipts of the same sentence. **A sentence citing several receipts is not mis-citing any of them;
each covers part of the claim.**

⇒ *An identification has to be checked on the loci the object itself distinguishes, and the locus
here is the SENTENCE WITH ITS WHOLE CITATION SET, not the pair I happened to enumerate.*

**The corrected rule, registered before the corrected number is produced:**

- ⅰ‴ The unit is the **sentence**. Its citation set is **every** `\rcpt{}` on it.
- ⅱ‴ A figure **REPRODUCES** when **any** receipt in that set produces it, by the rule already
  registered — verbatim, or within half a unit of its last printed digit.
- ⅲ‴ A figure is **ABSENT** only when **no** receipt in the set produces it **and every one of them
  ran**; if any is UNRUN the figure is **UNRUN**, never ABSENT.
- ⅳ‴ **MIS-CITATION** keeps its meaning and is now reported at sentence level: a sentence whose whole
  citation set ran and does not produce one of its figures.

**Registered arms for the correction:**

- ⑩ **The corrected ABSENT count is far below 65**, because the artefact dominates it. Band: **under
  25**.
- ⑪ **Arm ① is read on the corrected count**, and arm ④ with it: if the corrected ABSENT count is
  **zero**, the order's reachable negative is reached and arm ④ — this seat's prediction *against*
  that negative — **fires**, which is reported as a MISS and not smoothed.
- ⑫ ⌗ **And a routed observation, not a repair:** `check_figures_pinned` keys its own sites on
  `(population, paper, RECEIPT, figure)` and so has **the same property by design** — a multi-cited
  sentence's figures are flagged against every cited receipt that does not pin them. *That is a
  plausible part of why its baseline is as large as it is, and it is worth 69's attention rather than
  this seat's hands: the gate is not this seat's and the instruments are frozen.*

⌗ *Four rule conditions have now been withdrawn or corrected across `r7648` and `r7650`, every one
caught by a measurement rather than by a reading, and every one in the restrictive direction. That is
what the arms are for, and the count is reported rather than tidied.*

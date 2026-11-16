# r7805+cc66 — PREDICTION, registered before a line of the computation exists

**Order (69, r7805), two items.**
① **The r7669 discharge list against today's tree.** PO-87's register row says it is discharged when
every P15 figure resting on a spectrum off the leaf rate is re-derived on the refitted arm, or its
sentence is re-grounded on the configuration it is about. Re-run the `r7667` census on the current
tree; for each item report **re-derived**, **re-grounded**, or **still standing**, with the sentence.
If none stands, PO-87 can be struck on its own clause; if some do, they are the remaining work.
② **The control's point.** Which printed P15 figures depend on the control's *un-refitted* point
(the `0.918` comparison, the four-peak table, the fourth-feature differences, and anything else),
and by how much does each move at `omega_c = 0.1200` instead of the `0.120727` that
`(67.40, Omega_m 0.3150)` implies? Refitted comparisons should not move.

## A correction to the order's premise, before anything is measured

**The order says "your `LIST.md` has the 48 items". It does not: it has 30.** The census's own
header records the cuts — "Cut 5's own correction stands: it took the list from 48 to 30" — and
`r7675` split those 30 into **26 derived + 4 declared**, the four declared being carried in
`_JOINED_BY_READ` because they cannot be derived (their citing sentence prints no figure AND
`load_sites` records zero namesake sites, the arm being carried by a module-level *directory*).
`48` is the list *before* cut 5. So the census I am re-running is a 30-item list, and I will report
against 30 with the 48 named as the pre-cut-5 figure. **I am not re-deriving the 48-item version.**

## What the three verdicts mean, stated before measuring so they cannot be fitted afterwards

The census keys an item on two things at once: its receipt **reads** a namesake/superseded spectrum
(or every load site is undecidable), and a paper **body sentence citing it prints a figure**. So:
* **re-derived** — the receipt no longer reads a namesake/superseded spectrum: it was repointed to
  the arm-of-record/leaf-rate sibling. The item leaves the derived set by `prints_fig`'s own test.
* **re-grounded** — the receipt still reads the old spectrum, but the citing sentence is now
  explicitly *about* that configuration (it names the control, or says radiation-free, or states the
  arm), so the figure is no longer presented as the arm of record's. This is a judgement on the
  sentence and I will quote the sentence for each one I so classify.
* **still standing** — neither: the sentence still presents a figure from an off-leaf-rate spectrum
  as if it were the configuration the paper is about.

## PREDICTIONS

**① Most of the list has NOT moved, and PO-87 cannot be struck.** Reason, before measuring: the
census's membership test is what a receipt *reads*, and the five landings since `r7677` (`r7797`
through `r7805`) changed paper *sentences* and added *new* receipts; they did not repoint the old
receipts' `np.load` targets. Re-grounding is therefore the only mechanism that can have moved most
of these, and it moves them one sentence at a time.
* ①a **The derived set is between 20 and 28** (it was 26). **FALSIFIED** outside that band.
* ①b **At least one item still stands, so PO-87 cannot be struck on its own clause.** **FALSIFIED**
  if every one of the 30 is re-derived or re-grounded.
* ①c **The census's own pinned `_LIST_WAS = 30` no longer matches today's derived+declared total**,
  so the instrument reddens on its own pins and the ledgers want the departures named with the
  revision that moved each. **FALSIFIED** if it runs clean with no ledger edit.
* ①d **`the_low_multipole_depth_gap` (item 12) is the most likely departure**, because `r7677`
  item 3 ordered exactly that repoint once `70` banked `cc66_lowell_sweep_leafrec1.npz`, and `r7801`
  landed the one-rate depths into the sentences it cites. **FALSIFIED** if it is still in the derived
  set reading `cc66_lowell_sweep.npz`.
* ①e **The cheap set is at least 2** (it was 2 at `r7677`, and `r7797`–`r7805` banked more one-rate
  spectra, which can only add). **FALSIFIED** below 2.

**② The control's un-refitted point moves a short list, and the four-peak table is on it.**
* ②a **The list is non-empty and includes the `0.918` comparison and the four-peak table.**
  **FALSIFIED** if either turns out not to depend on the control's un-refitted point.
* ②b **Refitted comparisons do not move**, because a refit re-minimises and absorbs an `omega_c`
  shift into its own best fit. **FALSIFIED** if any refitted figure moves by more than its printed
  last digit.
* ②c **The moves are small compared with the differences the figures carry.** `omega_c` moves by
  `+0.000727`, 0.6 per cent of itself. On CAMB that was worth `+2.44 sigma` in `theta_*`, but
  `theta_*` is a ratio of two integrals over the whole history and is far more sensitive to it than
  a peak height or a spacing. So I predict **every un-refitted spectrum figure on the list moves by
  less than its own printed precision except where it is a ratio of two accumulated lengths**.
  **FALSIFIED** if any peak-height or peak-position figure moves by more than its printed last digit.
  *This is the prediction I hold least firmly: `omega_c` sets the matter-radiation ratio, which the
  driving and so the peak heights do depend on, and 0.6 per cent in it is not obviously negligible
  for the `0.918` height comparison.*

**③ A cross-cutting prediction, so the two items are not scored independently.** Item ② is a
*re-derivation* question about the control, and item ① counts re-derivations. **I predict the two
lists are disjoint**: none of the figures item ② names is one of the 30 census items, because the
census's items rest on spectra off the **leaf rate** while item ②'s rest on the **control's
background point**, which is a different defect. **FALSIFIED** if any receipt appears in both.

## How it is run

Item ① re-runs `r7667`'s own `census.py` on the current tree — the instrument is not rewritten, and
any ledger edit is additive and names the revision that moved the item. Item ② re-solves the named
figures at `omega_c = 0.1200` with the same machinery each already uses, changing only that one
number, and reports each figure's printed value beside the moved one.

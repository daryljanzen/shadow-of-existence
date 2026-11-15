# r7805+cc66 — RESULT: PO-87's list grew to 33, none of it is evidence, and re-pointing the control costs the arm half its margin

**Receipt:** `receipts/P15_CR_cosmology/P15_po87s_list_grew_to_33_and_not_one_arrival_is_evidence_and_repointing_the_control_to_plancks_omega_c_moves_the_0_918_to_0_957.py` — **11 gates, 0 fail.**
**Failability:** `failability.py` — **4 probes, all bite**; the unmutated receipt returns 11/11 from a temp path.

## A correction to the order's premise

The order says `LIST.md` has "the 48 items". **It has 30.** The census's own header records cut 5
taking the list 48 → 30, and `r7675` split those into **26 derived + 4 declared**. `48` is the
pre-cut-5 figure. Everything below is against 30.

## ① The census on today's tree: 33, up from 30 — and not one arrival is evidence

Re-run **unmodified**, the census reports **29 derived + 4 declared = 33**, and reddens on its own
pins. By set comparison against the banked list: **2 left, 5 joined** (30 − 2 + 5 = 33).

* **The departure that matters**: `the_low_multipole_depth_gap` — the repoint `r7677` item 3 ordered
  once 70 banked the sibling. That instrument did the job it was written for. *(Prediction ①d held.)*
* **The five arrivals, none of them a new defect**: three read **no namesake at all** (on the list
  only because every load site is undecidable); one reads the **control's own bank**, and only for
  its `arm` key — a provenance check I added deliberately, with no printed figure resting on it; one
  reads `r7749_leafgeom_refit_verify_cr.npz`, whose **own banked config says `LEAFGEOM: true,
  LEAFREC: true, LEAFSCALES: true`** and whose manifest reads *"arm of record + LEAFGEOM=1 (the
  projection distance on the leaf rate, radiation included)"*. **That is the one-rate build — the
  configuration PO-87 wants figures derived on — counted as a spectrum off the leaf rate**, because
  the classifier's suffix test looks for `_leafrec1` and the corpus's newer banks are named
  descriptively.
* **Three of the five arrivals are my own receipts** from r7797, r7801 and r7803.

### The classification the order asked for

| verdict | n | what it means |
|---|---|---|
| **STANDS (candidate)** | **7** | reads arm-side spectra that are not the one-rate build |
| **NOT A DEFECT (control)** | **5** | every spectrum it reads is the control's own |
| **RE-DERIVED** | **1** | its arm-side spectrum *is* the LEAFGEOM build |
| **UNDECIDED (needs a read)** | **16** | reads no namesake; every load site undecidable |

### ⛔ The answer to "can PO-87 be struck": not as the clause is written, and not for the reason expected

**7 stand, so it cannot be struck today.** But the clause cannot be discharged *ever* as written.
Five items read **nothing but the control's own spectra**, and **a ΛCDM control has no leaf rate** —
there is no such object as the control on the leaf rate, so a control spectrum is "off the leaf rate"
by construction and *every receipt that compares the arm against the control must read one*. PO-87's
clause, "every P15 figure resting on a spectrum off the leaf rate", therefore catches every control
comparison in the paper for ever. **It needs the control excluded from its scope, or it can never be
struck.** That is a wording decision, not a measurement.

⌗ **The 7 are candidates, not proven.** Their arm-side banks record **no `config` key at all**, so
the bank cannot say whether they are on the leaf rate — only that I cannot clear them. That is also
why 16 are undecidable, and it is a measured property of the older banks rather than a limit of
effort.

## ② Re-pointing the control to Planck's ω_c is not cosmetic

`ω_c = 0.1200` at the same `H₀` and `ω_b` means `Ωm = 0.313400`, so `ΔΩm = −0.001600` — **a tenth of
the refit grid's own step (0.0150)**, well inside the ±1-step stencil. So the move is priced from the
grid's banked two-sided steps (`lcdm_OMm`/`lcdm_OMp`) rather than by running a new spectrum, with the
refit receipts' own scoring.

| quantity | at the corpus's point | at ω_c = 0.1200 | move |
|---|---|---|---|
| control's no-fit χ², 185 lensed bins | 212.902 (grid) / 214.057 (published) | ×0.959103 | **−4.090 %** |
| **the published `0.918`** | 0.918 | **0.957** | **+0.039 — the third decimal moves** |
| the arm's margin over the control | 8.2 % | **4.3 %** | **about half the claim** |
| control's peak 1 | — | — | +0.118 multipoles |
| control's peak 2 | — | — | +0.363 |
| control's peak 3 | — | — | +0.695 |
| control's peak 4 | — | — | **+0.966** |

* **The `0.918` becomes `0.957`.** The whole move is the denominator's, since the arm does not move
  when the control's ω_c does. Applied as the *relative* factor the grid measures, not as an absolute
  χ² difference, because the grid base and the published control differ by −1.155.
* **The control's fourth peak moves +0.966 multipoles — more than every fourth-feature difference
  P15 prints** (0.00, 0.18, 0.21 in TT, EE, TE). So any arm-minus-control displacement at the fourth
  feature moves by that order. *(I priced the control's peak-4 position, which is the right order of
  magnitude but not the same statistic as the fourth-feature displacement; that would need the
  locator re-run on a re-pointed control, which is 69's call.)*
* **Refitted comparisons do not move.** The control's own 185-bin refit minimum sits at
  `Ωm = 0.309826`, already `−0.005174` from the corpus's point — **3.2× the re-pointing's own
  0.0016** — and a minimum found by search does not follow its starting point. *(Prediction ②b held.)*

⇒ **Re-pointing improves the control and costs the arm half of a headline comparison.** Whether to
take it is 69's ruling. **Nothing is re-pointed here and no paper sentence is edited.**

## Scoring the registered predictions, honestly — three of eight failed

| # | registered | measured | verdict |
|---|---|---|---|
| ①a | derived set 20–28 | **29** | ⛔ **FALSIFIED.** I reasoned that re-grounding cannot move items and forgot that **new** receipts join — three of the arrivals are my own. |
| ①b | at least one stands | 7 stand | ✅ HELD |
| ①c | the pinned `_LIST_WAS = 30` no longer matches | census reddens on its own pins, rc 1 | ✅ HELD |
| ①d | the depth-gap item is the likeliest departure | it left | ✅ HELD |
| ①e | cheap set ≥ 2 | **0** | ⛔ **FALSIFIED** — the second cheap item left the list by being repointed, which I should have seen. |
| ②a | list non-empty, includes the 0.918 and the four-peak table | both move | ✅ HELD |
| ②b | refitted comparisons do not move | unmoved | ✅ HELD |
| ②c | un-refitted peak figures move less than their printed last digit | peak 4 moves **+0.966**, the 0.918's third decimal moves | ⛔ **FALSIFIED, badly** — and I registered it as the one I held least firmly, for the right reason: ω_c sets the matter–radiation ratio the driving depends on. |
| ③ | the two items' lists are disjoint | disjoint: no receipt appears in both | ✅ HELD |

**Three of eight failed**, and all three are recorded in the receipt's own gate text (gates 7 and 10),
not only here.

## One thing the build taught

**Gates 9 and 10 originally trusted a subprocess's stdout**, so the receipt's own constants could
drift away from the script's and both gates would still pass. `failability.py`'s probe 1 found
exactly that: mutating `WC_PLANCK` in the receipt left them green. They now parse the instrument's
own reported point and assert it is the point the receipt names. *A gate that reads another
program's output has to check that program was asked the question this one is answering.*

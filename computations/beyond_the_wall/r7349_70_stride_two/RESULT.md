# `r7349+70.19` — RESULT: the second stride block closes whole. All 18 unbegun receipts are realised, and all 59 rows are out (58 repaired, 1 withdrawn with its case). 70's stride goes from 61 owed rows to 2, both held and routed. ⛔ The registration miscounted its own denominator (16 for 18), so T-a breaks HIGH on a count error, not a forecast. T-b and T-c are refuted low for the second block running

*Registered at `PREDICTION.md` (`aa24c6b5`, pushed 02:26:25 UTC, before the first receipt was opened). Repairs are
`.2`–`.5` and `.7`–`.17`; ledger commits are `.6` (`d685bece`) and `.18` (`9658532e`), both green on
`check_quote_pins`. **Nothing in the registration is revised.***

## ⛔ The registration's own error, stated first

- **PREDICTION said "16 unbegun receipts and 59 rows".** The rows were right and the receipts were not.
  - Its own table lists **18 receipts**: RP_34_gr and P03 each carry two.
  - I counted prefixes (16) and wrote them as receipts.
- **T-a was registered "realised receipts, of 16", band 10–16.** That is reported as written below: the band was
  bounded by a miscounted denominator.
- This is the same class as `r7339` ③'s stale-header charge: a count written without being re-derived from the list
  it names.

## The assignment and what was reached

| prefix | receipts | rows | repair commit |
|---|---|---|---|
| RP_34_gr | G2, G3 | 8 | `.2` |
| P03_SdS_slicing | A6, P03_w | 4 | `.3` |
| L247 | B1 | 8 | `.4` |
| L202_the_seam | T1 | 6 (one WITHDRAWN) | `.5` |
| L_probability, L246 | S1, W1 | 6 + 4 | `.7` |
| L272 | F1 | 4 | `.8` |
| L276 | R1 | 3 | `.9` |
| L560 | P1 | 3 | `.10` |
| L815 | S1 | 3 | `.11` |
| L248 | R1 | 2 | `.12` |
| L256 | B1 | 2 | `.13` |
| L280 | D1 | 2 | `.14` |
| L259 | D1 | 1 | `.15` |
| L556 | R1 | 2 | `.16` |
| P08 | P08_the_boundary | 1 | `.17` |
| **total** | **18** | **59** | |

**Every receipt in the block was reached.** None is left unattempted.

## ⑥'s quantities

- **EFFORT:** wall clock from opening a receipt to the commit carrying it. Prefixes with two receipts split their gap
  in half.
  - The 18 values run from 7 s to 216 s. **The median is 47 s, about 0.8 minutes.**
  - With the ledger and gate windows charged back: 02:26:31 to 03:04:45 is 38.2 minutes for 18 receipts, **2.1 minutes
    a receipt.**
- **REALISED: 18 receipts.**
- **The owed count beside the keys minted and adjudicated:**
  - **70's stride: 61 owed rows → 2.** The two are `P10_no_rescaling` (RC3) and W1's comment pin (RC4), both held and
    routed at `r7339+70`.
  - **Trunk REPAIR-OWED on this branch: 163 → 104** (59 rows).
  - **38 keys minted and adjudicated in the same push:**
    - 37 whole-clause keys are MEANING-HELD, each held at its own repair commit;
    - 1 code pin is DELIBERATE: `COV_TT[np.ix_(keep, keep)]`, the covariance read in S1.
  - **62 stale keys struck.**
  - **Four rows left by an instrument, not by a span, so they minted no key:**
    - L272's `return 1`: the survey is RUN with a missing ledger, then with an unfindable control, and each must fail.
    - L248's `bounded below`: the struck row's cells are COMPARED with its unstruck form at `aeeba47f~1`.
    - L556's `def is_data_row` and `index_rows`: the membership rule is EXERCISED on an em-dash row, and the import is
      asked of the AST.

## The predictions

| # | registered | measured | |
|---|---|---|---|
| T-a | realised 13 of "16" (10–16) | **18** | ⛔ **breaks HIGH, on the registration's miscount** (above) |
| T-b | median EFFORT 2.5 min (1.0–6) | **0.8** (2.1 with the windows charged) | ⛔ **REFUTED, low** |
| T-c | withdrawn 8% (3–20%) | **1 of 59 = 1.7%** | ⛔ **REFUTED, low** |
| T-d | rule cases 1 (0–3) | **0** | held |

- **T-b and T-c failed in the same direction as `r7339+70`'s S-b and S-c, on a block chosen to be harder.**
  - The registration said the source-heavy and instrument prefixes should move both quantities up. They did not.
  - L272, L276, L556 and L_probability/S1 took 25 s to 216 s each, which is the same range as the prose prefixes.
- ⇒ **What the two blocks support together:**
  - Once a ruling exists, repair is cheap: either 69's or 60's named repair in the reason column, or the rule's own
    "carry the claim, then stop".
  - Withdrawal is rare, because most fragments were cut from a true sentence.
  - **The cost sits in the ledger and the gate window**, about 10 minutes per batch, **not in the receipts.**
  - I do not carry a rate further than these 77 rows.

## The withdrawal, and the judgement calls

- **WITHDRAWN: L202_the_seam/T1's "the PO-12 row carries the debt but not the split".**
  - The row is struck as "THE DEBT IS DISCHARGED". Its r2623 block states the debt AS two steps.
  - So the claim is false on the live row, and the bare `debt` token kept it green. The case is written in the
    receipt.
- **Decided and said, not rule cases:**
  - **L560/P1's Lovelock clause:** "the same algebra" has its antecedent two sentences back. The claim pinned is that
    the sentence c54.202 added still stands, and the span carries that. This is 60's flagged border case, decided.
  - **L256/B1's "not yet reached the shared trunk"** was verdicted as an openness marker. It is the gate docstring's
    description of what the band measures, not outstanding work. Repaired as a clause.
  - **L247/B1's register check** is a **locus-scoped conjunction** of two rows, struck PO-14 and PO-21. No single span
    carries it, and the row reason says so (`r7341` ①).
- **Two spans crossing an `\emph{…}` brace** (T1's run clause and its envelope clause) were moved to the clause after
  the brace. A literal holding a closing brace of a wrapper it does not open counts 0 under `_unmark`.

## Checks run

- **`check_quote_pins`:** green at both ledger commits.
- **`check_deferrals`, `check_absence_claims`, `check_revision_collisions`, `check_provenance` and
  `check_paper_pins_not_comment_only`:** green.
- **All 18 touched receipts pass.**
- **The 40 ledger readers:** S19 and S20 are red as carried on main. **S36, S37 and S47 are reported in the reply**,
  read against `origin/main`.

## Not done

- The applier machinery stays stopped.
- No other seat's receipt was edited in this block except as reported in the reply.
- **No π_d.**

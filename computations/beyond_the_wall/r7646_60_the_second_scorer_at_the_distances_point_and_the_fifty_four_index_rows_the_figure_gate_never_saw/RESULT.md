# r7646 (60) — RESULT

**Both of `r7645`'s items are answered. All six of `70`'s printed figures reproduce on a second
scorer to the digits they print, worst |Δ| `0.0004`, so the figures 69 lands corpus-wide are not an
artefact of either instrument. And the row the figure gate could not see is one of fifty-four.**

Receipts: `second_scorer.py` (**15 checks, 0 FAIL**, 8 s) and `the_blind_rows.py` (**11 checks,
0 FAIL**, 2 s). Nine arms registered, **eight hold and one misses**; the miss is ⑦ and it is
reported with its discarded reading.

---

## ① PART 1 — the second scorer at the distances' point

`r7644`'s instrument, unchanged: this seat's own binning, marginalisation and closed-form amplitude
fit; **no import of `chi2_of_spectrum`**, which is the scorer `70`'s `measure.py` calls; `plik_lite`
TT, its weights and its covariance read as the data; and CAMB's **full** lensed/unlensed operator
read as the array `r7644` computed under the other interpreter and saved, so `camb` stays off the
pinned one. The operator is re-asserted at ℓ 1900 (`1.0666`, inside `[1.05, 1.08]`) rather than
assumed, and the interpreter is re-asserted as the pinned `3.11` / `numpy 2.4.6`.

| configuration | half | control | LEAFREC=0 | LEAFREC=1 | r0/c | r1/c | `70` prints |
|---|---|---|---|---|---|---|---|
| no-fit L2000 | unlensed | 696.0 | 1169.8 | 1129.8 | 1.681 | **1.623** | |
| no-fit L2000 | **LENSED** | 214.1 | 550.5 | **502.1** | **2.572** | **2.346** | 2.572 / 2.346 |
| grid base L8 | unlensed | 685.7 | 1155.5 | 1114.6 | 1.685 | **1.626** | |
| grid base L8 | **LENSED** | 212.9 | 545.8 | **496.5** | **2.564** | **2.332** | 2.564 / 2.332 |
| refit verify | unlensed | 592.8 | 910.1 | 924.2 | 1.535 | **1.559** | |
| refit verify | **LENSED** | 186.5 | 292.4 | **297.7** | **1.568** | **1.596** | 1.568 / 1.596 |

- **① ② ③ hold.** `2.346`, `2.332` and `1.596` all reproduce; worst |Δ| `0.0004`.
- **And the LEAFREC=0 rows reproduce with them** — `2.572`, `2.564`, `1.568` — so it is the **move**
  that is instrument-independent and not only the new endpoint.
- **④ holds.** The LEAFREC=1 arm is less unfavourable on **both** halves of both no-fit rows, so the
  8.8% the headline moves is the spectrum's and not the lensing operator's. *Had it held lensed and
  failed unlensed, the operator would have been doing the work.*
- **⑤ holds.** The unlensed no-fit ratio at the distances' point is `1.623`, inside the registered
  `[1.3, 1.68]` and below `r7644`'s `1.681`.
- **And the one row that moves the other way** is the refit: `1.568 → 1.596`, up where the no-fit
  rows go down, which is the direction `70` reports.
- ⛔ **The registered negative did not fire.** No row disagrees beyond the digits `70` prints.

⌗ *What this does not settle, from the registration: the two scorers share the data on purpose, so it
is an agreement about arithmetic on 185 bins and not about whether those bins are the right
confrontation. The claim is that the disagreement's **size** is instrument-independent.*

---

## ② PART 2 — the gate was not checking fifty-four rows, and `S60`'s was the last of them

`check_figures_pinned`'s `sites()` gated each `receipts/INDEX.md` row on
`c[4].startswith('`')` — so a row whose receipt-path cell was not in backticks became a **silent
non-site**, however many figures its claim cell printed, and the gate reported the same green either
way. cc66 found it on `INDEX.md:1210`. **The class is 54, against 1085 well-formed rows:** lines
`309`, `310`, `637`, and a contiguous `S10`…`S60` block from `1130` to `1210`.

**The repair, in three parts:**
1. **All 54 path cells backticked.** Verified against the parent revision cell by cell: 54 lines
   changed, each in cell 5 only, each change exactly the two backticks. No other cell, no pipe count.
2. **The one condition moved.** `startswith('`')` no longer *gates* the row; it *routes* it, into a
   module-level `MALFORMED`, and `main()` names each malformed row and returns non-zero **before**
   the baseline is read or written. ⇒ A malformed row is an error rather than an absence.
3. **Two seeds added**, so the new condition is tested in both directions on synthetic rows and not
   only on whichever tree happens to be checked out.

**What the 54 rows were hiding: 228 unpinned figures under 214 keys.**

- **⑥ holds exactly.** `S60`'s row alone brings **63** live — cc66's count, reproduced.
- ⌗ **And `S60` carries 28% of the class on its own, while 29 of the 54 rows print no unpinned figure
  at all.** The class is not 54 times one row.
- **⑧ holds.** Of the 214 new keys, **zero** were already in the baseline and **nothing went STALE**.
  A row the gate never read cannot have contributed a key.
- **⑨ holds, both ways.** On the repaired tree the router reports nothing malformed; with the
  backticks taken off those same 54 rows it sends every one of them to `MALFORMED`.
- **⑩ holds.** `make_all_appendices.py`, `gen_paper_html.py P15`, `regen_frontier.py` and
  `regen_grain_currency.py` all regenerate with **no output change at all** — the path cell's markup
  reaches the figure gate and nothing else, so no appendix moved and no PDF is owed.

### ⛔ ARM ⑦ IS A MISS

The registration predicted the class total **over 500**. It is **228**. The discarded reading is kept
beside the correction: the band was sized from `S60`'s 63 across 54 rows, which is the exact mistake
the finding itself names — *a class found through one member must not be sized from that member*.
29 of the 54 print nothing and one row carries 28%. The band was wrong in the direction that
matters, because 228 is affordable to read and 500 would not have been — and the disposal below was
argued from the structure, not from the size.

### The disposal, and it is not either of the two the order names

The 228 are **baselined**, not pinned and not trimmed.

- They are **not new claims**: nothing was pushed that printed them. That is exactly the population
  this gate's own docstring says is *"BASELINED, not repaired here — it is routed per paper"*, with
  the gate's work forward.
- **Nothing went STALE**, which is the structural fact the choice rests on: the red is 214 new keys
  and zero regressions.
- Pinning 228 pre-existing figures into receipts never written to hold them would be **building an
  instrument**, not repairing one; trimming the digits of `S60`'s 55 KB claim cell would be
  **rewriting another turn's landed record**. Both remain available and the baseline can only shrink.

⇒ Recorded as a fork this seat decided. **If 69 wants `S60`'s 63 pinned or trimmed instead, that is
one line of order and the baseline drops by 63.** The three rows outside this seat's own block
(`309`, `310`, `637`) had their **markup** normalised and nothing else; their claims and receipts are
untouched, and that is routed rather than assumed.

---

## Scope

No paper is edited, no figure moves, no parameter is pinned, no quote-pin key is minted, no new
instrument is added, and no receipt of `70`'s or cc66's is touched. One gate that was quietly not
checking now checks; `receipts/INDEX.md` changed only in the markup of 54 path cells;
`corpus/figure_pin_baseline.tsv` grew by the 228 figures that became visible, with the reason in its
own header.

## Files

- `PREDICTION.md` — the registration, its own commit, pushed before a score was read or a row edited.
- `second_scorer.py` — PART 1's receipt.
- `the_blind_rows.py` — PART 2's receipt.
- `repaired_rows.tsv` — the 54 rows, with each one's live figure count; the record of the repair.

# `r7727+cc66.1` — PRE-REGISTRATION: **the SEARCH** for P15's other printed multiples, fixed before it is run

⛔ The order's instruction is explicit: *"Register the sweep's search first, so the list is not chosen after
the results."* ⇒ **This file fixes the patterns, the scope, the inclusion test and the exclusions. It is
pushed before the search runs**, so the list cannot be tuned to what the test would do to it.

---

## 1. The scope, exactly

- **`corpus/CR_cosmology.tex`, lines `1`–`3040`** — the body, `3101` lines, down to its single `\input`.
- ⛔ **`appendix_receipts_P15.tex` is EXCLUDED, and here is why rather than by preference:** it is
  **generated** by `corpus/make_all_appendices.py` from the receipts. A figure there is a *transcription of
  a receipt's own output*, not a claim the paper prints on its own authority. ⇒ Sweeping it would count each
  claim twice and would attribute the receipt's text to the paper.
- Nothing outside P15 is in scope, whatever it says.

## 2. ⛭ THE PATTERNS — fixed now, run verbatim, and the regex's output IS the list

Over the body with whitespace flattened, case-insensitive:

| | pattern | catches |
|---|---|---|
| **Ⓐ** | a number within `80` characters **before** one of `scatter`, `spread`, `standard deviation`, `\bsd\b`, `sigma`, `\sigma` | *"`6.6` times its own scatter"*, *"`3.9` sd"* |
| **Ⓑ** | one of those words within `80` characters **before** a number | *"a scatter of which it is `12` times"* |
| **Ⓒ** | `times` or `multiple of` within `40` characters of one of those words | multiples whose number is spelled or deferred |

A "number" is `\d+(\.\d+)?`, with optional surrounding `$…$` or backticks stripped first.

⛭ **The union of Ⓐ, Ⓑ and Ⓒ is the candidate list. I do not get to add a site the patterns miss, and I do
not get to drop one they catch** — each is kept and classified in §3, with its classification stated.

## 3. The inclusion test, applied to every candidate and recorded for each

A candidate is **IN SCOPE for the calibrated test** only if all three hold:

1. it is **P15's own measurement**, not a figure quoted from the literature;
2. the denominator is an **empirical spread over correlated samples** — band centres, smoothing widths,
   or a band family — and not an independent-sample error or a quoted instrumental uncertainty;
3. it is used as **evidence** (a claim that something is or is not there), not as a **definition** or a
   tolerance (*"within one standard deviation"* as a criterion is not an evidential multiple).

**Each candidate is recorded with its verdict and the reason**, including the ones that fail.

## 4. ⛔ REGISTERED EXCLUSIONS — named now so they cannot be invented later

- ⒜ **The two sites already settled at `r7719`–`r7721`:** the located step's million-surrogate clause and
  the narrowed source-exclusion clause. They are the **precedent for this sweep, not new sites**, and
  re-reporting them as findings would be double-counting my own earlier work.
- ⒝ **The seven-band family.** As `r7719` established, `7! = 5040` admits a floor `p = 1.98e-4`, i.e.
  **`3.72` sd-equivalent**, so a printed multiple above that cannot be expressed by any resampling of it.
  ⇒ For those sites the registered answer is **"a ratio, not tested"**, which the order itself names as
  legitimate. ⛔ **That is an answer, not a failure, and it is not to be dressed as either a pass or a red.**
- ⒞ Figures that are **not** a quantity divided by a spread (percentages, bare ratios, counts).

## 5. What the calibrated test is, where it applies

`r7717`'s ruled construction, unchanged and not re-derived: **phase-randomised, step-free surrogates that
preserve the curve's own scatter and autocorrelation**, with the printed multiple read as a percentile
against them. ⛭ **Nothing about the test is redesigned here** — if a site needs a different test, that is
reported and not improvised.

## 6. ⛔ WHAT WOULD MAKE THIS SWEEP WRONG

- ⒜ the patterns return **zero** candidates beyond the excluded ones — in which case the honest report is
  that P15 prints no other multiple of this form, and the sweep's value is the **negative** result;
- ⒝ a candidate's receipt cannot be identified, so "with its receipt" cannot be answered — reported as
  **unsourced**, which would itself be a finding;
- ⒞ the test's own precedent does not transfer because the curve is a different object — the fault this
  seat has logged six times, and the reason §3's criterion 2 is about **what the denominator is of**.

## 7. The price

The sweep is a regex over `3040` lines: **seconds**. The calibrated test costs what `r7719` measured —
**~`1.3` µs per surrogate batched**, so `10⁶` draws per curve is about a minute. ⇒ Cheap; the cost is
proportional to how many sites survive §3, which is not yet known.

## 8. What this cannot do

It cannot change a P15 sentence. ⇒ Step 4 of the order is **drafts only**, *"only where the printed claim
does not survive"*, each with its new licence — and **whether a draft lands is 69's ruling.**

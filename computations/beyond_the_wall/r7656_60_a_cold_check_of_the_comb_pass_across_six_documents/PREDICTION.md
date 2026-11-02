# `r7656` (60) — REGISTER BEFORE CHECKING: the comb pass, read cold across six documents, with one locator on both sides

**The order (`r7655`, 69).** *"A part in four hundred"*, with the matched-locator peaks, comb, phase and
heights, landed in one pass across `P15` (abstract l.135, l.148, l.153, l.248, l.441, l.813,
l.882–886, l.945, l.2067–2075, l.2146, l.2768, l.2791, l.2990), `P7` (l.1812, l.1851, l.1863),
`P17` l.1722, `P18` l.1526 and l.1832, `P6` l.353, and the explainer l.241 and l.254. For each figure,
check that the receipt the sentence cites — or, for the five documents that are not `P15`, **the `P15`
receipt behind it** — computes it to the printed digits **by the same locator on both sides of the
comparison**. Then test the three claims most exposed to the change. **Register first. The reachable
negative is that every one reproduces.**

---

## ⓐ SCOPE, MEASURED AND DECLARED BEFORE ANYTHING IS RUN

Counted by the corpus's own figure extractor, `check_figures_pinned.figures`, on the named lines with
`\rcpt{}` and `\ldg{}` markers stripped:

| document | lines named | lines carrying text | figures | `\rcpt{}`-cited receipts ON those lines |
|---|---|---|---|---|
| `P15` `CR_cosmology.tex` | 25 (l.882–886 and l.2067–2075 as ranges) | **18** | **26** | **2** |
| `P7` `CR_framework.tex` | 3 | 3 | **23** | **0** |
| `P17` `geometric_core_paper.tex` | 1 | 1 | **1** | 0 |
| `P18` `CR_synthesis.tex` | 2 | 2 | **21** | 0 |
| `P6` `shadow_of_existence.tex` | 1 | 1 | **2** | 0 |
| the explainer `EXPLAINER.md` | 2 | 2 | **3** | 0 |
| **total** | | **27** | **76** | **2** |

⛔ **AND THE SHAPE OF THE PROBLEM IS IN THAT LAST COLUMN, SO IT IS DECLARED NOW.** Of the 27 named
lines, **two** carry a `\rcpt{}` marker at all. The other 25 reach a receipt the way the order says
they do — through the paper-level citation — so **this is not a citation lookup; it is a resolution
problem.** A check that simply read each line's own citation set would have **nothing to compare on 25
of 27 lines** and would report them green by vacuity. *An arm with no instance to score is not a pass,
and this seat has been caught by that before.*

⌗ **One declared blank:** the explainer's l.241 carries **no figure of two or more significant digits**
at all. It is reported as carrying none rather than as reproducing.

## ⓑ THE METHOD, FIXED HERE

- **ONE LOCATOR ON BOTH SIDES, which is the order's own condition.** The same function —
  `check_figures_pinned.figures` — extracts the figures from the paper's sentence **and** from the
  receipt's stdout. *The receipt's output is not grepped for a string: it is passed through the
  extractor the gate itself uses, so a figure that reproduces does so under one rule rather than two.*
- **THE RECEIPT SET IS BUILT, NOT GUESSED.** The candidates are every receipt cited anywhere in
  `P15`'s `sec:refit-bound` together with every receipt the named `P15` lines cite, each **run once**
  under a bounded budget taken from the repository's own `scripts/run_all_receipts.py` table, three at
  a time, one thread each. Nothing is re-run for reassurance.
- **THREE VERDICTS, as at `r7650`:** REPRODUCES, ABSENT, UNRUN — and a figure is ABSENT only when
  **every** candidate ran and none produced it. *If any candidate is unrun the figure is UNRUN, never
  absent.*
- **THE TOLERANCE IS THE PRINTED DIGIT:** the coarser of half a unit in the last printed digit and the
  gate's own 0.05% of |X|, which is `check_figures_pinned`'s allowance and not a window chosen here.

## THE ARMS

**① EVERY FIGURE RESOLVES TO A RECEIPT THAT COMPUTES IT.** All 76 return REPRODUCES, with none ABSENT
and none UNRUN. *This is the order's reachable negative and it is registered as the expected result.*

**② AND THE REGISTERED ARM AGAINST IT.** At least one of the 76 does **not** resolve — because 25 of
the 27 lines reach their receipt only through a paper-level citation, and a figure restated in a second
document can drift from the one its source computes without any gate noticing. *Registered against ①
before anything ran, exactly as `r7650`'s arm ④ was.*

**③ THE COMB ITSELF, WHICH IS THE PASS'S HEADLINE.** $299.1$ against $298.4$ reproduces, and the
"part in four hundred" is checked as arithmetic rather than accepted as prose: $|299.1-298.4|/298.4$
lies within half a unit in the last digit of $1/400$.

**④ "WITHIN THREE AND A QUARTER MULTIPOLES"** — the first of the three the order names. The receipt
behind it prints a worst per-peak offset over the first three peaks, and that offset is $\le 3.25$ to
the printed digit.

**⑤ "A THIRD OF A PER CENT HIGH" AT THE FOURTH PEAK** — located in `P7` l.1812 and **not** in `P15`,
which is declared here because the order's phrasing does not say where it sits. The fourth peak's
fractional offset reproduces at $0.33\%$ to half a unit in its last digit.

**⑥ "BETWEEN ONE AND THREE MULTIPOLES AT EACH PEAK"** — a *range* claim, so it is checked as one: every
per-peak offset the receipt prints lies in $[1, 3]$, and the check fails if any peak falls outside
rather than if the mean does. *A range claim verified on an average is not verified.*

**⑦ THE SAME FIGURE IS THE SAME EVERYWHERE IT IS RESTATED.** Where two documents print what should be
one quantity, they print the same digits — tested across the restatements the scope above found, and
reported per pair rather than as a count.

**⑧ AND THE ONE THING THIS CHECK CANNOT DO IS NAMED NOW.** A figure that reproduces establishes that
*some* receipt in the candidate set computes it. It does **not** establish that the sentence's own
citation points at that receipt, because on 25 of 27 lines there is no citation to point. ⇒ **Any
figure whose computing receipt is not among those its own document cites is reported as RESOLVED
ELSEWHERE, not as correctly cited** — and that distinction is the finding if arm ② fires.

---

## WHAT THIS DOES NOT CLAIM

- **It does not re-open the comb's physics.** It checks that the digits the six documents print are the
  digits the corpus's own receipts compute, under one locator.
- **It edits no paper.** Any drift found is routed, because a sentence in another seat's document is
  not this seat's to re-state.
- **It adds no gate, ledger or census**, and touches nothing of `70`'s or cc66's.
- ⚠ **And the budget is declared, not discovered:** each candidate gets **one** bounded run, every
  receipt that does not finish is reported UNRUN **with its budget** rather than dropped from the
  denominator, and the figures depending on it are UNRUN rather than absent. *A cold check that
  quietly dropped what it could not run would be measuring its own window — which this seat has now
  reported twice and will not report a third time as a result.*

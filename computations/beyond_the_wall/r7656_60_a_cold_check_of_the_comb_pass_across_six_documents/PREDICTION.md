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

---

# `r7656+60.1` — REGISTER THE CORRECTIONS: the order names the BLANK line before each paragraph, and my candidate set anchored on a comment

**Two method defects, both mine, both found by measurement before a single verdict was produced.**

## ⓘ THE NAMED LINES ARE THE BLANK LINES BEFORE THE PARAGRAPHS

Measured: `P15` l.135, l.148, l.153, l.441, l.2791 and l.2990 each have **length 1** — the newline
alone. The paragraph begins on the **next** line every time, and the "part in four hundred" the order
is about sits at l.136, l.149, l.154, l.442, l.2765, l.2788 and l.2987.

⇒ **So 69 is naming paragraph starts by the blank line that precedes them.** That is a consistent
convention, not a slip — but a check that read the named lines **literally** would find six blank
lines, extract nothing from them, and report them green. *That is the vacuity failure arm ② of this
registration was written against, and it would have fired on my own instrument rather than on the
corpus.*

**⑨ THE CORRECTED RULE, registered before the corrected scope exists:** a named line that is blank
resolves to the **next non-blank line**, and the receipt **prints the resolved line number beside the
named one** for every site, so the resolution is visible and not silent. A named line that is blank
and has no non-blank successor is reported UNRESOLVED, never skipped.

## ⓘ AND THE CANDIDATE SET WAS BUILT FROM THE WRONG ANCHOR

It returned **2** candidate receipts where `r7650` found **35** in the same section. The cause: the
builder anchored the segment on the first *mention* of `sec:refit-bound`, which is **line 34, inside a
comment block**, instead of on `\label{sec:refit-bound}` at **line 808**. So the "section" it scanned
was the abstract.

⇒ **⑩ THE CORRECTED RULE:** the segment is anchored on the **label's definition**, `\label{sec:...}`,
never on a mention; and the receipt **asserts the candidate count is above 20**, because a candidate
set of two could not resolve 33 distinct figures and a check that tried would report them absent for
want of a place to look. *A sweep that returns nothing has measured its own reach — the third time
this seat has had that lesson, and the first time it has been caught by an assertion written in
advance.*

⌗ *Both defects share one shape: **an instrument that silently returns less than it should looks
exactly like a corpus that is clean.** So both corrections are assertions about the instrument's own
reach, placed before the measurement rather than inferred from its result.*

**Running total of this seat's own rule conditions corrected by measurement rather than by reading,
across `r7648`, `r7650`, `r7652`, `r7654` and `r7656`: eighteen.**

---

# `r7656+60.3` — REGISTER BEFORE THE RESULT IS REPORTED: 95 of 95 is the shape of a guard that cannot fail, and the matcher's own reach must be measured first

**The pass returned REPRODUCES 95, ABSENT 0, UNRUN 0.** That is the order's reachable negative,
reached — and **it is not reportable yet**, because the instrument that produced it has a property I
can state before measuring it: *it searches **100** receipts' output for any number within half a unit
of the target.* For a two-significant-digit figure like `0.30` or `68.6` the chance that **some** number
in a hundred receipts' stdout falls inside that window is high **whatever the corpus says**.

⛔ **So a 95-of-95 is exactly what a matcher with no discriminating power returns**, and this seat has
reported that failure mode twice already — the sweep at 0.04% reach, and the arm with no instance to
score. *A guard that cannot fail on the data it is given is not a guard, and the way to find out is a
negative control, not a re-reading.*

## THE CONTROL, registered before it is run

**⑪ DECOYS.** For every one of the 95 real figures a **decoy** is built by moving it **well outside its
own tolerance** while keeping its magnitude and digit count — so the decoy is a figure the corpus should
**not** carry at that site, of exactly the shape of one it does. The decoys run through the **same**
matcher against the **same** 100 banked outputs.

**⑫ THE REGISTERED THRESHOLD, fixed now rather than after the number is seen.** If the decoy
reproduction rate is **above 20%**, the matcher is too permissive for 95-of-95 to mean anything, the
result is reported as **the instrument's reach and not the corpus's state**, and the matcher is
tightened before any verdict is published. Below 20%, the 95-of-95 stands and the decoy rate is
published beside it as the instrument's own false-positive floor.

**⑬ AND THE RATE IS PUBLISHED EITHER WAY**, with the decoys' own list, because a cold check that
reported its hit rate without its false-positive rate would be asking to be believed rather than
checked.

**⑭ A SECOND, SHARPER CONTROL.** The matcher is also run with the candidate pool **restricted to one
receipt at a time**: the number of distinct receipts that independently produce each figure is counted.
*A figure produced by exactly one receipt out of a hundred is a located figure; one "produced" by
forty is a coincidence of the window.* The median multiplicity is published.

⌗ **The reachable negative of this amendment is that the matcher is sound — decoys below 20% — and the
pass stands as measured.** It is registered against, because the arithmetic above says a hundred
outputs and a half-unit window is a wide net, and I would rather find that out here than have 69 find
it in the reply.

**Running total of this seat's own rule conditions corrected or controlled by measurement rather than
by reading, across `r7648`, `r7650`, `r7652`, `r7654` and `r7656`: twenty-one.**

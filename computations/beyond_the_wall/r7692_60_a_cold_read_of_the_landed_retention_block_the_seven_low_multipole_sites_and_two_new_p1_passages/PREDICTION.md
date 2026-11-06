# r7692 (60) — REGISTRATION: a cold read of the landed retention block, the seven low-ℓ sites, and two new P1 passages

**Registered before a line of any reading existed, in its own pushed commit.** The tree is named in
`runs/TREE.txt`. Every arm below is a COMPARISON with **no predicted verdict**; what is registered is
the shape of what a reading may return, and the reachable negatives, so that reaching one is a
result and not a silence.

Order: `r7689` (69), the topmost section of `FOR_60.md` on `origin/main` at registration. Three items.

---

## WHAT THE ORDER ASKS

1. **P15 `l.1772–1797`, the retention block,** against `the_cross_term…` and
   `the_phase_systematic…`, **in `r7684`'s form**. The order names two clauses as 69's own and not
   cc66's — the **carrier clause** ("rides on the envelopes") and **the injection's wording** — and
   says to read those hardest.
2. **The seven low-ℓ sites and the new scope sentence after `l.2816`,** against
   `the_low_multipole_depth_gap…`'s **distances-point block**.
3. **In P1:** part (i)'s new formal sentence (`td_cor_threefold_i`, `td_noClosed_of_temporal`,
   `td_noClosed_D`, in `ThreefoldDistinct.lean`), and **`cor:densities`' proof**, which now states
   the matter clauses machine-checked on the shell (`sm_*`, in `ShellMatter.lean`).

---

## `r7684`'s FORM, which item 1 is ordered into — restated so the reading cannot drift from it

`r7684` read a reported reversal and found it was **a ratio against a beat**. Its form is: for each
figure the prose states, (α) name the receipt the prose cites for it; (β) find whether that receipt
**computes** that figure, by reading the receipt's own source rather than its docstring or its
printed summary; (γ) if two receipts are cited for one figure, score each separately, because **two
citations on one figure are two claims and they can disagree**; (δ) where the figure is a ratio,
read its **denominator**, because a ratio is a claim about its denominator; (ε) where the prose names
*which* object a statistic is taken on, return **UNMEASURED** if the source does not distinguish
them.

## THE SIX GUARD FAMILIES, CARRIED FORWARD UNCHANGED

- **G1** every conjunct probed **through the same predicate**; never one conjunct by a looser matcher
  than its neighbour.
- **G2** three anchor forms only — a word boundary `\b`, an escaped control sequence, an escaped math
  delimiter. An **unanchored marker is REFUSED**; a boundary is never placed AFTER a delimiter.
- **G3** the flip family: every reading is run against a deliberately altered copy and must change
  its answer.
- **G4** classifier probes: each reading states which category it assigned and why.
- **G5** reader probes **with NEGATIVE probes**.
- **G6** every prose probe runs on a **whitespace-FLATTENED** copy.
- **Every verdict note is BUILT FROM its readings**, so it cannot contradict its own verdict.

## THE EIGHT STANDING NEGATIVE PROBES, CARRIED FORWARD

1. a figure in the `.tex` but absent from the cited receipt ⇒ **NOT SUPPORTED**;
2. a variable bound in a later binder group after a `:` must still parse **BOUND**;
3. a conjunct under `∃` must not be reported at TOP;
4. a reading naming *which* comb must return **UNMEASURED** if the source does not distinguish;
5. a reading scoring two figures said to be the same quantity must **FAIL** when handed two that differ;
6. a dependence reading must be able to answer "does not rest on it" and still **FAIL** on a sentence
   that does;
7. a hypothesis probe must separate "the hypothesis is stated" from "the hypothesis does the work",
   returning **STATED-BUT-UNUSED** for the first;
8. a reliance probe must be able to answer **NONE** and still fire on an injected site that relies.

## TWO NEW NEGATIVE PROBES THIS REVISION ADDS

9. **A carrier probe must distinguish "X is present in the computation" from "the quantity rides on
   X."** Handed a receipt that computes a quantity from a sum in which X appears as one term among
   several, with nothing selecting X, the reading must return **PRESENT-NOT-CARRIER**, never
   SUPPORTED. This is aimed directly at the clause the order says to read hardest.
10. **A site-count probe must be able to return a count OTHER than the one the prose states.** Handed
    a copy of the paper with one of the ordered sites removed, the enumeration must return `n-1` and
    say which is missing. A probe that can only confirm "seven" is a probe that answers about itself.

---

## ARM 1 — THE RETENTION BLOCK (P15 `l.1772–1797`)

Registered as a per-figure and per-clause comparison in `r7684`'s form. The clauses are fixed
*before* any figure is scored:

- **1a THE CARRIER CLAUSE, "rides on the envelopes."** 69's own clause, read hardest. Negative probe
  9 governs. Three distinguishable readings, each reachable and each a result: **SUPPORTED** (a cited
  receipt computes the quantity *from* the envelopes in a way that would change if they were
  replaced); **PRESENT-NOT-CARRIER** (the envelopes appear in the computation but nothing selects
  them as what the quantity rides on); **NOT SUPPORTED** (no cited receipt carries the object at all).
- **1b THE INJECTION'S WORDING.** 69's own clause, read hardest. What is injected, into what, and
  with what quantifier — and whether the receipt's own injection is the same operation under the same
  name. Reachable: **SUPPORTED** / **NOT SUPPORTED** / **TWO-TO-ONE** (one sentence carrying two
  claims about two different injections) / **UNMEASURED**.
- **1c EVERY REMAINING FIGURE OF THE BLOCK,** enumerated by the reading itself from `l.1772–1797`
  rather than from a list written here, each with the receipt(s) it cites, each scored at the
  receipt's **source**. Where two receipts are cited for one figure, each is scored separately and a
  disagreement is a finding, as at `r7686`.
- **1d WHICH RECEIPT COMPUTES WHAT.** `r7684` found an own-comb form for the step and **none** for
  the slope. The reading re-derives, from source, which of the two cited receipts computes each
  quantity the block states, and returns **UNMEASURED** for any quantity neither computes.

## ARM 2 — THE SEVEN LOW-ℓ SITES AND THE NEW SCOPE SENTENCE AFTER `l.2816`

- **2a THE ENUMERATION.** The reading enumerates the low-ℓ sites itself and reports the count it
  finds. Negative probe 10 governs: on a copy with one site removed it must return one fewer and name
  the missing one. **If the count is not seven, that is the result**, recorded as
  **COUNT-DISAGREES (`n` found against seven stated)** — not reconciled, not rounded to the stated
  number.
- **2b EACH SITE AGAINST THE DISTANCES-POINT BLOCK.** For each site, whether
  `the_low_multipole_depth_gap…`'s distances-point block computes the figure the site states, read at
  source. Reachable per site: **SUPPORTED** / **NOT SUPPORTED** / **MIS-CITED, SUPPORTED ELSEWHERE**
  / **UNMEASURED**.
- **2c THE NEW SCOPE SENTENCE.** A scope sentence is a claim about what the preceding figures *do and
  do not* cover. Registered as its own comparison, with the reachable negative that the scope stated
  is **wider than the block supports** (**SCOPE-OVERSTATED**) or **narrower** (**SCOPE-UNDERSTATED**,
  which is a result and not a safety).

## ARM 3a — PART (i)'s NEW FORMAL SENTENCE, AGAINST `ThreefoldDistinct.lean`

Three cited names, so at least three claims, scored against each theorem's **own statement text**:

- **3a-1** what `td_cor_threefold_i` states, and whether it is part (i) — `p ≠ q` — under the
  hypotheses the sentence names, no weaker and no stronger.
- **3a-2** `td_noClosed_of_temporal` and `td_noClosed_D`: what each supplies, and whether the
  sentence's account of where the causality condition comes from matches. ⚠ `r7690` established the
  condition is used by **(i) alone**; this arm checks the *formal* sentence, not that conclusion.
- **3a-3** the hypotheses actually carried, against the setting the sentence claims — including
  whether any is **stronger or weaker** than stated. **STRONGER-THAN-CLAIMED** is recorded and never
  silently upgraded to SUPPORTED, as at `r7690`.

⚠ Carried forward from `r7690`: **a quantity keeps its NAME outside the region where it measures
anything**, and **a hypothesis stated for a corollary need not be used by every part of it** — so
which part of the corollary each cited theorem serves is read, not inferred from where it sits.

## ARM 3b — `cor:densities`' PROOF'S MATTER CLAUSES, AGAINST `ShellMatter.lean`

The proof "now states the matter clauses machine-checked on the shell". Registered as: enumerate the
clauses the proof marks machine-checked; for each, the `sm_*` name it cites; and for each name, read
its statement at source and decide whether it carries that clause. Reachable per clause: **SUPPORTED**
/ **NOT SUPPORTED** / **TWO-TO-ONE** / **STRONGER-THAN-CLAIMED** / **MIS-CITED, SUPPORTED ELSEWHERE**
/ **UNMEASURED**. ⚠ "On the shell" is a locus claim and is read as one: a clause proved on the whole
model is not the same claim as one proved on the shell, and vice versa.

---

## WHAT WOULD MAKE THIS REVISION WRONG

- A carrier reading that returns SUPPORTED because the envelopes merely appear ⇒ negative probe 9.
- A site enumeration that can only return the stated count ⇒ negative probe 10.
- A figure scored from a receipt's docstring or printed summary instead of its source ⇒ `r7686`'s and
  `r7690`'s lesson, and `r7690` found exactly that defect in a probe's docstring.
- A verdict note that does not follow from its own readings ⇒ every note is BUILT from them.

## EXIT CODES REGISTERED IN ADVANCE

`0` every registered reading ran and its verdict is recorded (whatever the verdict).
`1` a reading could not be run, or a guard refused an anchor, or a negative probe failed to fire.
No other exit code is reachable; **no verdict is an exit code.**

## RECORDED NON-GOALS

- Nothing in `corpus/`, `receipts/`, `scripts/` or `computations/formalisation/` is edited. This is a
  READ. Every repair found is **routed** in `FOR_66_FROM_60.md`, never landed here.
- The receipts of item 1 and item 2 belong to **cc66** and **70**: a defect in one is routed with its
  patch and never edited.
- `sh_H_r`'s docstring defect from `r7690` is already routed to 71 and is **not** re-routed.

# r7164+70.1 — the 43 owed unread-figure sites: a read of each, plus a perturbation of each, pre-registered

*Pre-registered by node 70 against `origin/main` `0b71dad9`, before any of the 43 was read or perturbed. Order: `FOR_70.md` r7164 ⚑.
At `0b71dad9`, `check_unread_figure` reports owed **43**:
- **33** `UNADJUDICATED` (the per-site partition withdrew a file-level credit);
- **10** carried from `r7151+70.1` (4 `FIGURE`, 6 `FORMULA`).*

## The test: the read is backed by a perturbation, so a verdict does not rest on reading alone

For each owed site, in a throwaway `git worktree` of HEAD:
1. Take the figures the operator extracted for that site (`mutate_assertions --unread-figure`'s `figs`).
2. Find each figure's occurrences in the paper the label attributes it to. If the label names none, use every `corpus/*.tex` holding it.
3. Rewrite every such occurrence to a different value with the same number of digits.
4. Run the receipt from its own directory.

Outcomes:
- **RED-ON-MOVE:** the receipt fails. It *does* read the figure from the paper somewhere, so this is a **mis-classification by the per-site partition**, or a figure pinned by another check in the same file. Not a debt.
- **GREEN-ON-MOVE:** the receipt passes with the paper's figure moved. **The debt is real:** `FIGURE`, or `FORMULA` if the quantity is an expression.
- **NOT-IN-PAPER:** no attributed paper prints the figure, so nothing can be moved. These are read by hand:
  - `DRIFTED`: the paper used to print it and no longer does;
  - `NOT-A-PAPER-FIGURE`: the label attributes something else, or the number is the receipt's own arithmetic;
  - `FORMULA`: the expression is printed in a form the token match cannot find.
- **Every site is also read by hand.** The verdict, and what was read, is recorded per site in the baseline vocabulary. Where the hand read and the perturbation disagree, that disagreement is reported as a finding.

## Predictions

| id | prediction |
|---|---|
| F1 | Of the **33** withdrawn credits: genuine debts (`FIGURE` + `FORMULA`) **18–26**; mis-classified by the per-site predicate (RED-ON-MOVE) **3–10**; `NOT-A-PAPER-FIGURE` **3–8**. |
| F2 | The proportion of the 33 that are genuine debts is **55–80 %**. |
| F3 | The mis-classification class, if it exists, has **one dominant shape**: the paper's figure reaches the verdict through a name the taint fixpoint does not follow. My guesses are a dict or attribute lookup on a tainted object, a tuple-unpacked `re.search(...).groups()`, or a value checked by a *different* call that reads the paper while this site re-asserts the literal. |
| F4 | All **10** carried verdicts stand: GREEN-ON-MOVE, or NOT-IN-PAPER for the `FORMULA`s. A reversal of any of them is reported first. |
| F5 | The `60` `r7160` receipt's two sites are genuine debts, and are routed to `60`, not edited. |

*Misses will be reported as misses. No receipt is edited in this revision: this is a read, and repairs are routed by owner.*

# r7073 (70) — the confirmer on the current tree, and the class that nothing computes

*Pre-registered before any run. The order is `FOR_70.md` `r7073` Q1 and its second use.*

## What is run

`computations/beyond_the_wall/r7069_70_transposition_gate/confirm_transpositions.py --all` runs on the tree at this commit, against all 85 held baseline lines. For each line, it re-runs fresh the **own group** members and the **carrier** the gate named. It records three things:

- **own prints**: some own-group member's run output carries the number, at the paper's precision, by the r7043 matcher;
- **carrier prints**: the carrier's run output carries it;
- **carrier holds**: the carrier's source carries it (quote lines dropped). This is recorded, but it is **not** printing.

Each line is then reported in two lists.

1. **NOT CONFIRMED.** This covers lines whose verdict is "the own group prints it at run time" (40 of them) where no own member prints the number. The gate's 40 blind-spot entries are exactly these.
2. **NOTHING PRINTS.** This covers any line, whatever its verdict, where neither the own group's nor the carrier's fresh run prints the number. It is reported separately, with the line's verdict beside it.

## Scope, stated before the run

- "No cited receipt prints it" here means **the own group and the gate's carrier**. Those are the receipts the gate reads for that flag. It does **not** mean no receipt in the corpus computes it; `r7073`'s own correction on 7.06 Gyr is the reason for this line.
- Printing a number is **not** computing it, since a receipt may print a hard-coded literal. That distinction is reported where the source shows the number as a literal. It is not otherwise ruled.
- The four intentional lines are settled, and they are run only so the receipt fact is complete. They are not re-adjudicated.
- A NOTHING-PRINTS line whose verdict is external datum, configuration value or input is expected to be held rather than computed. It is listed, but it is not called a finding.

## Outcomes, the one that costs another seat most first

1. **A NOTHING-PRINTS line whose verdict is "own prints", "carrier restates", "coincidence" or intentional.** This would be a number the prose states that neither its own group nor the neighbouring carrier prints. It would be a (iii)-class candidate, which costs 66 a read and possibly a receipt build. **Predicted: none among the 40 "own prints" lines.** Those were disposed on saved run output, and the gate reports them not stale, so their groups are unchanged. For the 13 "carrier restates" lines, a restatement can be a literal, so **one to three are predicted to print nowhere**.
2. **NOT CONFIRMED among the 40.** This is possible only if a receipt's output changed since the saved runs, or the saved run was misread. **Predicted: 0.**
3. **Timeouts.** CAMB carriers are allowed 1800 s each. A timed-out run is reported as UNMEASURED and is never counted as "does not print".

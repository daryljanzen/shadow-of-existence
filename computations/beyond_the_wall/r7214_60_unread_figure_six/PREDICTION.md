# PRE-REGISTRATION — `r7214`, node 60: `PO-78`'s unread-figure backlog, this seat's six, and whether the class is what its name says

*Written and pushed BEFORE any computation. Nothing is ordered; `r7191` is answered by `r7210` and
`r7212` is landed. This is `PO-78`'s second standing backlog, the one neither `r7204` nor `r7208` nor
`r7212` touched: **`22` unread-figure sites owed against a ceiling of `22`**, `6` of them in receipts
this seat owns and therefore repairable here rather than routed.*

## WHAT THE CLASS IS CALLED, AND WHAT I SUSPECT IT ACTUALLY IS

*The gate's name says `unread figure`: a verdict that carries a paper's figure without reading it.*
⇒ **I suspect the name undersells it, and the thing I want to test is a structural claim rather than
a count.** *`70`'s own baseline notes on this seat's six read, in their own words,* ***"a paper's
number attributed in the label and hard-coded in the verdict, in a receipt that opens no `.tex`"***
*and* ***"hard-coded as the target, no pin of it in the file."***

⇒ *So the defect may not be a missing pin at all. It may be that* ***the LABEL makes a claim the
GATE never covers*** *— the label says a paper prints this, and nothing in the file reads the paper.*

**THE HYPOTHESIS, STATED BEFORE MEASURING SO IT CAN COME BACK WRONG:**

> ***`PO-78`'s two standing backlogs are the two sides of ONE failure — a gate and its label
> disagreeing about what is being asserted.*** *A quote-pin site is a GATE WITH NO CLAIM: it pins a
> form the argument does not need, so it breaks on a change that costs the argument nothing. An
> unread-figure site is a CLAIM WITH NO GATE: the label attributes a figure to a paper and no check
> covers the attribution, so it survives a change that should cost it everything.* **If that is
> right, the `2167` and the `22` are one class counted from opposite ends, and the repair rule is the
> same sentence read in two directions.**

## WHAT I ALREADY HOLD GOING IN

*The honest half of a pre-registration is what was already looked at.* I hold the gate's own
partition at the current head — `9` `NO-READ/FIGURE`, `13` `NO-READ/FORMULA`, `12`
`NOT-A-PAPER-FIGURE`, `13` `READ-ELSEWHERE`, `30` `READS-PAPER/REPORTED`, with `22` owed — and the
six baseline rows naming this seat's sites with `70`'s notes on each. I hold that
`mutate_assertions.py --prose` run on one of the six returns `0 site(s) in 0 receipt(s)`, which is
the instrument agreeing that the file makes no paper read. ⛭ *And I hold one measurement `70` already
made and I have not reproduced:* ***one of the six stays GREEN when the paper's figure is moved by a
factor of `1.37` in every paper.*** **I have read none of the six sources and repaired nothing.**

## THE OUTCOMES, TABLED, THE ROW-ENDING ONE FIRST

- ⓵ **THE HYPOTHESIS HOLDS AND THE TWO BACKLOGS ARE ONE CLASS.** *Then `PO-78` has one repair rule
  rather than three, stated as one sentence with two directions, and the row's shape changes rather
  than its count.*
- ⓶ **THE SIX REPAIR AND THE BACKLOG FALLS `22` → `16`, BUT THE UNIFICATION FAILS.** *Then the count
  moved and the structural claim did not, and I say so: a backlog that falls is worth less than a
  class that is understood, and reporting the fall as if it were the finding would be the error.*
- ⓷ **THE CLASS IS NOT WHAT THE NAME SAYS AND IS NOT WHAT I SUSPECT EITHER.** *Possible, and the most
  informative outcome: then reading all `22` tells me what it is, and the six repairs are incidental.*
- ⓸ **SOME OF THE SIX CANNOT BE REPAIRED FROM A RECEIPT.** *If an attributed figure is not actually
  printed in any paper, the repair is a paper-side act and not mine — it is routed, not forced, and
  the backlog falls by less than six.*

**THE LIKELIER BRANCH, NAMED BEFORE IT IS FOUND:** ⓶. *The unification is the thing I want and that
is exactly why it is the thing most likely to be read into the data. **The six repairs are
mechanical and near-certain; the structural claim is a claim and may well not survive the other
sixteen.** If it holds only on this seat's six it does not hold at all, and I will say that.*

## WHAT WOULD MAKE THE RESULT WRONG, AND IS CHECKED FOR

1. **A repair that satisfies the gate and not the argument.** *The whole lesson of `r7212`. Each
   repair is controlled TWO-SIDED on a shadow tree: unperturbed the gate is GREEN, and with the
   attributed figure perturbed in every paper it must go **RED**. ⛭ And the same perturbation against
   the PRE-repair source must leave it GREEN, which is `70`'s measurement reproduced rather than
   cited. A repair with no red side is not a repair.*
2. **Mutating the real corpus.** *Does not happen: the perturbation is built in a symlink shadow tree
   whose `corpus/` alone is rebuilt, the method `r7212` proved on a blanked corpus.*
3. **Keeping two objects apart.** *`r7210`'s lesson: where the paper's figure and this seat's
   computed one are different objects, the read asserts the paper's and the computation asserts
   mine, and the gate must not identify them.*
4. **A verdict moved rather than earned.** *No site leaves the owed count by reclassification. `70`'s
   baseline says it in terms — a record of adjudications, not a list of exemptions — so a site falls
   only by the file reading the paper.*

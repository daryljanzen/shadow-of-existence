# r7179+70.1 — is "the discrepancy a check exists to detect" recoverable from source?  A design note, measured

*Pre-registered before the operator exists.  Unordered: `FOR_70.md` r7179 asks for a design note if an operator
exists for "the tolerance exceeds the discrepancy the check exists to detect", and for a measured `cannot` if the
quantity is not recoverable from source.*

## The question split in two, before measuring

- **In general: NOT recoverable, by argument.**  The discrepancy a check must catch is the distance to the nearest
  WRONG value it should reject.  In `r7179`'s four, that wrong value was a second background configuration:
  `2.774` against `2.76`.  Nothing in a receipt's source names the competitor, so no static operator can know it.
  *This half is stated, not measured.*
- **A lower bound IS recoverable, for one shape.**  When a pin compares a computed value to a figure the PAPER
  PRINTS, the paper's own printed precision is a discrepancy the check must catch at the least.  A value off by
  more than half the printed last digit would print differently.  So **`T > half-ulp(printed L)`** means the pin
  accepts a value the paper would print differently.  Both `T` and the printed string are in the source.
  ⇒ *That is the operator: `abs(E - L) < T` with `L` and `T` numeric literals, `L` found printed in a paper the
  receipt names, the ulp taken from the paper's string.  It reports `T / half-ulp`.*

## Predictions

- **B1 RECALL.**  On the tree before `r7179`'s tightening (`adadc6a7^`), the operator flags the `0.03` stretch
  sites in **all four** receipts `r7179` names.  It also flags the `r0 +- 5.0` pins beside them (5051 is printed as
  an integer, half-ulp 0.5).
- **B2.**  At `HEAD` none of those four receipts' tightened sites is flagged.
- **B3 POPULATION** at `HEAD`:
  - **150-600** `abs(E - L) < T` sites with literal `L` and `T`.
  - **30-60%** of them anchored, meaning `L` is found printed in a named paper.
  - Of the anchored, **30-50%** flagged (`T > half-ulp`).
- **B4 PRECISION.**  In a hand-read sample of 20 flagged sites, **8-15** are genuine slack: the receipt gives no
  reason for the width and the paper's figure is a claim at its printed digits.  The rest are legitimate:
  - a coincidental match, where `L` is not the paper's figure;
  - an "approximately" figure whose receipt argues the width;
  - an exact rational pinned by a tolerance that is in fact tight.
- **B5 STATED LIMITS** (recall, unestimated):
  - a tolerance held in a variable or an expression;
  - `L` built at run time;
  - relative tolerances;
  - a pin against a computed reference;
  - the general case above.

*Misses reported as misses.  The operator is an instrument in `computations/`, not a gate.  No receipt is
edited: flagged sites are routed.*

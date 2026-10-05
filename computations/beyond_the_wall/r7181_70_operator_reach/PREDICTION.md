# r7181+70.1 — can `tol_vs_print`'s reach be widened cheaply?  Two widenings, predicted before either is run

*Unordered.  `FOR_70.md` r7181: "if the operator's reach can be widened cheaply ... that is worth a note".  The
r7179 operator anchors 145 of 1,060 literal sites.  722 name no paper, and 193 compare to a literal that no named
paper prints.*

## The two widenings, fixed before running

- **W1, ANY PAPER.**  For a receipt that names no paper, anchor `L` against every corpus paper.  This is cheap in
  code.  The cost is precision: a literal that some paper happens to print need not be that paper's figure.
- **W2, ONE IMPORT LEVEL.**  A receipt that names no paper itself, but imports a local module that does, takes that
  module's papers.  This is the same rule as r7177's `UNRUNNABLE` check.
- *"Cheap" means both of the following:*
  - *it adds at least 50 anchored sites;*
  - *its newly SLACK sites read COINCIDENTAL in at most 25% of a seeded hand-read sample of 20.  The r7179 sample
    read 10%, 2 of 20.*

## Predictions

- **C1.**  W1 raises anchored from 145 to **300-550**.
- **C2.**  Of W1's newly anchored sites, **30-50%** are SLACK.
- **C3.**  In a seeded sample of 20 of W1's newly SLACK sites, **>= 50%** are COINCIDENTAL.
  ⇒ *W1 is predicted NOT cheap: the reach it buys is mostly false.*
- **C4.**  W2 adds **20-80** anchored sites.
- **C5.**  W2's new SLACK sites, all of them if there are 20 or fewer, read COINCIDENTAL at **<= 25%**.
  ⇒ *W2 is predicted cheap, if C4 holds.*

*Misses reported as misses.  No receipt edited; the instrument stays in `computations/`.*

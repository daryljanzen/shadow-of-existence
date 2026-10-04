# r7161+70.1 — PRE-REGISTRATION: the lifecycle seed, on the scope selectors

*Committed before the apparatus exists.  Node 70.  Read at `origin/main` `fbb0f749`.  Offered at r7159 ("worth
having … registered as a report on the same ground as REGRID; your call whether it earns the turn").*

## What it is

r7157 found that "an instrument whose scope excludes the case it exists for" has no static signature: it is a
property of WHEN an instrument runs.  The measurable form is a **lifecycle seed**: plant one defect of a scoped
gate's own class at each stage the gate claims to cover, and ask whether the gate's SCOPE SELECTOR includes it.

**Apparatus:** `lifecycle_seed.py`, run in a throwaway `git worktree` of HEAD (the real tree is never touched).
It plants a receipt that pins a sentence of `corpus/CR_cosmology.tex`, then edits that sentence in the worktree's
paper, and asks each selector whether the planted receipt is in scope.  The stages are variants of the planted
receipt:

| seed | the receipt | stage it models |
|---|---|---|
| **S1** | names `CR_cosmology.tex`, opens it, pins the sentence; NOT in any baseline | written, not adjudicated (the r7149 window) |
| **S2** | the same pin, but reads the paper through `corpus/reach_baseline.py` (`RB.BODIES_TEX['P15']`) and names no `.tex` | the H1 read path found at r7159 |
| **S3** | as S1, and its literal recorded in `quote_pin_baseline.tsv` | adjudicated |
| **S4** | asserts the paper's figure in a LABEL only, reading nothing | the unread-figure class (a stated limit) |

**Selectors measured:** `scripts/_touched_pin_readers.py` (the scope of `run_touched_readers.sh`, the r7143 /
r7145 / r7151 gate) and `scripts/receipt_scope.py --scope suite` and `--scope reads`.

## Predictions

- **P1** `_touched_pin_readers` selects S1 (the r7151 third half fixed the adjudication window).
- **P2** `_touched_pin_readers` does **NOT** select S2: every half of it requires the receipt to NAME the changed
  file, and a `reach_baseline` reader names none.  *This would be a fourth member of the blindness shape, found by
  the seed rather than by a break.*
- **P3** `_touched_pin_readers` selects S3.
- **P4** `_touched_pin_readers` does not select S4 (its own docstring states this limit).
- **P5** `receipt_scope.py` selects none of S1–S4 for any scope, because a planted receipt is not registered in
  `INDEX.md` and the scope is over registered receipts.  *The planted receipt is therefore also run once
  REGISTERED (an INDEX row added in the worktree), and the predictions for that case are recorded from what the
  index says about unindexed receipts: P5′ — registered, S1 and S2 are selected by `--scope suite` via the
  "current source's names and imports" fallback.*

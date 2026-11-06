# `r7693` (cc66) — VERDICT

Against `PREDICTION.md`, registered and pushed before any computation.

## THE REGISTERED FIRST-FINDING CHECK PASSES WITH NOTHING TO REPORT

I registered that the order's depth row is **69's numbers, not mine**, and that any disagreement between
my own read of the bank and that row is this revision's first finding. **My read agrees at all seven
multipoles**, to rounding. *The check was worth keeping even though it found nothing: it is the
difference between reproducing a measurement and transcribing one.*

## THE ARMS

| arm | registered | outcome |
|---|---|---|
| ① which depths move by more than a printed digit | 4 move, 2 by one digit, ℓ = 8 not at all | **CONFIRMED** |
| ② the octopole's `+0.024` is the largest, upward | yes, and its penalty falls | **CONFIRMED** |
| ③ the likelihood's sign pattern survives | with ℓ = 4 unchanged at one place | **CONFIRMED on the pattern, ⛔ FALSIFIED on ℓ = 4** |
| ④ the one-clock cross-validation has no octopole exception | worst `2.9 %`, no exception | **CONFIRMED** |
| ⑤ the site list's completeness is the risk | a site absent from the order's ten is likelier | **CONFIRMED — four found** |

## ⛔⛔ ARM ③'s FALSIFIED LIMB IS THE `r7689` DEFECT A THIRD TIME, AND IT IS MINE

I registered that ℓ = 4's likelihood term would be **unchanged at one printed place**, then wrote a gate
calling it a rounding-boundary question for 69 to settle: *"`+2.050` exactly, so `+2.0` half-to-even and
`+2.1` half-up."*

**The term is `+2.05036`.** Strictly above the boundary, so it rounds to **`+2.1` under both
conventions**. There was no ambiguity and nothing for anyone to settle. ⇒ *** I read the TWO-DECIMAL
DISPLAY `+2.05` as if it were the value and reasoned about a boundary instead of looking at the next
digit. *** That is a derived conclusion computed from a rounded input: **the `r7689` `108.9` and the
`r7685` "factor of 75", a third time, by this seat, in three consecutive revisions — inside the
revision whose own receipt pins the repair for it.**

⌗ *Finding it in another seat's work, writing the rule down, routing it and gating against it has not
stopped me doing it. The gate now takes every rounding with `decimal` under BOTH conventions and returns
a **pair**, so a boundary cannot be read as a point.*
⇒ **So all four printed per-multipole terms change**, where my registration had three.

## ⚑ TWO PRINTED FIGURES THE ORDER DID NOT NAME, AND ONE CLAUSE THAT SURVIVES

- **The total: `+1.58 → +1.44`**, a move of `−0.149` against a printed precision of `0.01`. *So it is a
  SECOND figure the re-point changes and not one the depths carry along.* I had registered that the
  total was **not** licensed and that a move beyond the printed digit makes it a claim to re-measure
  rather than patch. It is.
- **The octopole-estimator range: `+0.2`–`+3.4` → `+0.2`–`+3.1`.**
- ✔ **But *"the same to the digit over `2 ≤ ℓ ≤ 10`"* SURVIVES**, because it claims the 8-vs-10
  agreement rather than the value — *gated as two separately computed sums rather than inferred from the
  total, which is the distinction the clause turns on.*

## ⚑ TWO FINDINGS AGAINST THE ORDER'S OWN FRAMING

- ✔ **The figure needs no regeneration.** The order lists *"the figure `fig:lowL-floor` with its plotted
  data"*. Its generator computes `D_C/r_0` and `sqrt(L(L+2))·ratio` and plots those plus a shaded band;
  **no depth appears in its plotted data at all.** The depths live only in the caption's prose.
- ⚑ **Four generated sites the list does not name** — the two appendix files, twice each. *Not
  hand-drafted; they regenerate. But listed, because a generated file carrying a stale figure is still a
  paper printing a wrong number, and what makes it right is a command rather than a draft.*
- ⌗ *Smaller: `l.134` prints ℓ = 4 at two places as `0.36`, and the new value also rounds to `0.36`, so
  that figure **survives** and editing it would introduce an error. And the "two-clock split's" clause
  the order places at `l.2600` is at `l.2608`.*

## FAILABILITY — 22 OF 22, AND IT TOOK A FIFTH LEG TO SAY SO

| leg | assertions broken |
|---|---|
| A arm-of-record depths scaled | **17** |
| B exact-transfer depths scaled | 4 |
| C one-clock bank replaced by the split | 1 — *exactly the cross-validation gate, and nothing else* |
| D the sky's quadrupole set to unity | 6 |
| **E1** exact transfer made equal to the arm of record | **the total-moves gate, targeted** |
| **E2** the ℓ = 8 depth moved far from unity | **the 8-vs-10 gate, targeted** |

⛔ **Legs A–D left TWO of the 22 unbroken, and reporting them as covered would have been false.** *The
total-moves claim is an inequality no leg was aimed at making coincide, and a one-per-cent scaling leaves
ℓ = 8 inside the tolerance the 8-vs-10 conjunct allows.* ⇒ Leg E was written for those two by name, and
**checks that its TARGET failed rather than that something failed** — which is the only version of this
check that means anything. Every leg verified the patch applied before running.

⌗ **And commitment ⑦ caught one assertion before any run:** the 8-vs-10 gate's first draft compared
`dm2lnL(_AOR, OBS)` against `_t8`, which **is that same call** — an assertion that could not fail,
inside the gate whose subject is a claim about two different sums.

## ⛔ TWO CI REDS, BOTH MINE, AND THE SECOND IS A PROCESS FAILURE I HAD JUST FIXED

`check_unread_figure` and `check_prose_pins`/`check_marker_transposition` went red on the runner. **Both
are in the heavy set the LEAN batch skips and only the push asks — the gap I identified at `r7691`, whose
standing change was to ask those gates locally when a revision touches a receipt's READS.** *I did not.
The rule I wrote down and routed lasted exactly one revision.*

- **`check_marker_transposition`: two STALE entries, not new transpositions.** `0.911` and `0.983`
  stopped being flagged once this file mentioned them — **but what made the own group carry them was a
  COMMENT of mine quoting the paper's row, and a comment is not a computation.** ⇒ The exact transfer's
  seven depths are now **pinned from the bank**, and the entries removed on that basis. *This closes, for
  the row still in print, the same hole `r7691` closed for the slope.*
- **`check_unread_figure`: one new key**, my sign-pattern gate, whose label attributed a *reading* to
  `sec:largescale` while every number in it is computed here. ⇒ Reworded to say what the receipt computed.

## ITEM 4 — THE DIP TEST, LANDED AND CHEAPER THAN I PRICED IT

All six figure pins and both licence gates green. ⌗ **And the price was wrong in the cheap direction:** the
24-phase scan already in that receipt had kept every band value the test needs, so the only new work is
two bank reads and an interpolation. *I quoted the cost of re-running a scan that was already paid for —
**an estimate of the wrong computation**, made without reading what the file already held.*

## GATES

Turn batch **`--full`: 133 of 133, `PASS=133 FAIL=0 UNRUN=0`** under `NODE=cc66` on `a3eaab2d8` with a
clean tree. CI green on the same head. *No corpus file is edited this revision: the drafts are routed.*

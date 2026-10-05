# r7177+70.1 — stated limits that announce their own lifting: a census of node 70's instruments, and the conversions it supports

*Pre-registered before the census is run.  Unordered work: `FOR_70.md` r7173 invites it ("if you see other stated
limits in your own instruments that could be made to announce their own lifting, that is worth a revision whenever
it is cheap"), and Daryl asked for it to start.*

## The shape being generalised

`P1`'s ⓷ (r7171): a limit stated as a fact about the TREE, and asserted, so that the edit that ends it fails the
instrument with the word LIFTED instead of passing silently.  A limit can be made to announce only if its truth is
decided by the tree and not by the instrument's own code.

## The classification, fixed before counting

Every stated limit in node 70's instruments goes in exactly one class:

- **CORPUS-STATE** -- a named site or a population that the tree decides (a paper, a receipt, a set of markers).  An
  edit OUTSIDE the instrument can end it or widen it.  ⇒ *These are the ones that can be made to announce.*
- **CAPABILITY** -- the instrument cannot see X by construction (a subprocess read, a run-time needle, untracked
  files).  It ends only by editing the instrument, so the instrument's own diff is the announcement already.
- **ENVIRONMENT / PROCESS** -- the machine, the runner, the history, the merge topology.  Not tree state at all.

## Instruments in scope (15)

The gates `corpus/check_{env_fingerprint,marker_transposition,unread_figure,revision_collisions,tilt_pins,
prose_pins,receipts_run}.py`; the scripts `scripts/{_touched_pin_readers,red_carry,sweep_vacuous_pins,
sweep_runner_reads,receipt_scope}.py`; the receipts `L_probability/C1_…`, `L_probability/S1_…`, `P01/P1_…`.

## What was known before this file, disclosed so it is not scored as a prediction

- **K1** -- `scripts/_touched_pin_readers.py` states as a remaining limit that
  `P15_the_exact_transmission_ratios…` "never names `CR_cosmology.tex` anywhere in its source".  That receipt has
  READ the paper since `r7153` (66).  ** A stated limit that lifted and stayed stated -- the inert kind. **
- **K2** -- `S1`'s (iii) limit (the +-0.0467 is carried as an INPUT by every script and computed by none) is already
  asserted, so it already announces.
- **K3** -- `C1`'s header: "the fifteen headline ones are read by hand, the rest are a STATED LIMIT".  The
  fifteen are fixed by name in the receipt; whether the corpus still has exactly those fifteen headline markers is
  NOT checked anywhere and has not been measured at `HEAD`.

## Predictions

- **A1** -- total distinct stated limits across the 15: **22-40**.  CAPABILITY is the majority (**>= 60%**);
  CORPUS-STATE **3-8**; the rest ENVIRONMENT/PROCESS.
- **A2** -- of the CORPUS-STATE limits, **1-3** already announce (K2 and `P1` ⓷ known).
- **A3** -- besides K1, **0-2** more CORPUS-STATE limits are found already lifted or moved, silently.
- **A4** -- `C1`'s headline set at `HEAD`, by r7043's own rule (abstract, or a section titled
  conclu|summary|verdict|outlook|closing): **unchanged** -- the same fifteen markers on the same thirteen receipts.
  *Moderate confidence; if it has changed, that is the limit having widened silently and it is reported first.*
- **A5** -- `C1` converted (my receipt, applied): the headline set asserted equal to the hand-read set, both ways.
  Seeds in a throwaway worktree: **S0** `HEAD` rc 0; **S1** a `\rcpt` marker added to an abstract → rc 1 naming it
  as WIDENED (a headline marker nobody read); **S2** a hand-read headline marker removed → rc 1 naming it as STALE.
- **A6** -- CORPUS-STATE limits in GATE code are **proposed as diffs, not applied** (gate code is 66's).  Each
  proposal is seed-tested in a worktree the same way.  K1 is proposed as a correction to the comment.
- **A7** -- each conversion adds **< 2 s** to its instrument's run.

*Misses will be reported as misses.  No paper prose and no other seat's receipt is touched.*

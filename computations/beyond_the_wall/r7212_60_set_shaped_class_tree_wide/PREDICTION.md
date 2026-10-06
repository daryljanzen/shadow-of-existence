# PRE-REGISTRATION — `r7212`, node 60: the set-shaped class, run over the WHOLE instrument tree and over the GATES

*Written and pushed BEFORE any computation. `r7208` measured this class over the `284` receipts this
seat owns and said out loud that the sweep was **bounded by authorship**, offering the tree-wide run
to the gate. Nothing has been ordered. **The bound was never a bound on MEASURING** — it is a bound
on REPAIRING, and those are two different acts. So the sweep runs tree-wide here and the repairs stay
inside this seat's own files, with anything found elsewhere routed as a patch and not an edit.*

## WHAT IS BEING RUN, AND WHY IT IS NOT THE SAME RUN AGAIN

`r7208`'s detector is an `ast` taint analysis: a name assigned from a SHARED registry is tainted,
taint propagates through assignment, and a site is flagged where an `==` against an integer literal
meets a `len`/`sum`/`count` of a tainted name. A second stage grounds each flagged site as
**FROZEN** *(the population is read at a pinned commit)*, **SELF** *(the set is the file's own
literal)*, **ROW-SCOPED** *(a single row, not a population)*, or **EXPOSED** *(live and growable)*.

`r7208`'s population was `284` files: one seat's receipts. **The population here is the pinned tree's
whole Python instrument layer — `997` receipts, `136` `scripts/`, `170` `corpus/`, `1,303` files —
and the two families that have never been swept at all are the GATES.** That is the point of the run
rather than an incidental widening:

> ***A gate on a SET is a gate on everyone who can add to that set.*** *Stated that way at `r7208`
> about receipts. A gate in `scripts/` or `corpus/` is a gate on everyone who can add to that set AND
> is itself the thing that decides whether anyone else's push lands. An exact count in a receipt goes
> red and costs its author a revision. **An exact count in a gate goes red and costs every seat the
> trunk.***

## WHAT I ALREADY HOLD GOING IN, SO IT IS NOT PRE-REGISTERED AS OPEN

*The honest half of a pre-registration is what was already looked at.* I hold, from `r7208`: that
over this seat's `284` receipts the detector flagged `25` sites in `9` files, that exactly **one** was
EXPOSED, and that the one was this revision's own predecessor — `r7198`'s receipt, **already red on
the trunk** and unseen because the receipts job had been `skipped` on every push between. I hold the
detector's code and both of its stages. **I have run it over nothing outside this seat's receipts,
and over no gate at all.** I do not know the tree-wide counts, the per-family rates, or whether a
single site outside this seat is EXPOSED.

## THE INSTRUMENT'S OWN BOUND, PRICED RATHER THAN ASSUMED

The detector's reach is a **hand-written list of `14` registry names**. A hand-list undercounts by
construction, and a sweep that reports a rate without pricing its own reach is reporting the
instrument and calling it the tree. So the run does what `70`'s `r7181+70.1` did to its operator:
measures with the `r7208` list *(so the number is comparable to `r7208`'s)*, then measures again with
a widened reach, and **states whether widening pays or buys coincidences.** If the widened reach adds
mostly false positives, the honest answer is to decline it in print, as `70` declined theirs.

## THE OUTCOMES, TABLED, THE ROW-ENDING ONE FIRST

- ⓵ **AN EXPOSED SITE IS LIVE IN A GATE.** *The most severe form of the class, in the layer where it
  costs every seat rather than one. Row-ending for the class: the `=` → `≤` repair stops being a
  receipt-hygiene rule and becomes a gate-layer requirement.*
- ⓶ **EXPOSED SITES EXIST IN OTHER SEATS' RECEIPTS, AND THE GATES ARE CLEAN.** *The tree-wide offer
  was worth taking; the class is a receipt-layer backlog, and `70` is owed a count that may only
  fall, in the shape `r7191` already ordered for the multi-site class.*
- ⓷ **NO EXPOSED SITE ANYWHERE OUTSIDE THIS SEAT'S OWN WORK.** *Then `r7208`'s one instance was the
  whole class and the tree-wide run returns a NEGATIVE — which is a result, reported as one, and the
  offer to the gate is withdrawn rather than left standing.*
- ⓸ **THE DETECTOR DOES NOT TRANSFER.** *Possible and must be said if it happens: the gates'
  idiom may be different enough that the taint rule flags nothing it should and everything it
  should not. Then the finding is about the instrument and the class stays unmeasured in that layer.*

**THE LIKELIER BRANCH, NAMED BEFORE IT IS FOUND, so that the other does not read as aimed at:** ⓷ for
the GATES and ⓶ for the receipts. The gates already have the ceiling idiom in them — the quote-pin
backlog is carried as `may only fall` and not as an equality — so I expect the gate layer to be the
*disciplined* one and the receipt layer to carry the class, because a receipt is written once and read
never while a gate is read on every push. **If that is what comes back, the result is the asymmetry
and not the count**, and the interesting sentence is *why* the layer under more pressure is cleaner.

## WHAT WOULD MAKE THE RESULT WRONG, AND IS CHECKED FOR

1. **A denominator that moves.** The population is read from `git ls-tree` at a pinned commit, never
   from a live glob — a sweep whose own denominator grows when this revision adds a receipt would be
   the defect it is about. *(`r7208`'s own precaution, kept.)*
2. **The detector matching itself.** This receipt will contain the forms it hunts, in its own code and
   in comments quoting what it repaired. Comment lines are stripped before any self-assertion, and
   tokens the detector must not match itself on are built programmatically. *(Both learned by falling
   into them.)*
3. **An EXPOSED verdict that is a false positive.** Every EXPOSED site is confirmed BY RUNNING IT, not
   by reading it — the claim "already red on the trunk" was earned at `r7208` by running on a pristine
   detached worktree and is earned the same way here or not made.
4. **A repair in a file this seat does not own.** Does not happen. Any site outside this seat's files
   is reported with a patch in the channel and left untouched.


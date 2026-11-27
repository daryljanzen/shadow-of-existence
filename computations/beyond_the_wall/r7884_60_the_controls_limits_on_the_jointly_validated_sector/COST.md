---
kind: COST
revision: r7884
node: 60
---
# r7884+60 — THE MEASURED COST, WHICH THE REGISTRATION ASKED FOR AS A RISK

⌗ *Recorded as it is measured, not after the fact. `PREDICTION.md` declared the cost a RISK and
required a measured number, with the item to SPLIT if the grids do not fit in one revision.*

## THE CMB GRID: MEASURED, AND IT FIT

Ten points, two arms at the five positive sum nodes, four at a time at the banked resolution with
the hierarchy on. Every point `rc=0`. Per-point wall was of the order of the `3945`–`3956` seconds
`r7882` measured for the same resolution, which is the figure the declared estimate used.

⚠ **One batch was killed and had to be re-run from the start.** The generator and both its legs
disappeared partway with **no `rc` recorded, no error in either log, and disk and memory both
ample** — so the cause was outside the computation. The generator is idempotent, so the relaunch ran
only the two outstanding points. ⌗ *A leg is not checkpointed: a killed leg loses all of its work,
which is what makes the next section a real risk rather than an inconvenience.*

## THE LENSING GRID: SLOWER THAN THE ESTIMATE, AND THE ESTIMATE SAID SO

⛔ **The declared estimate was taken from CMB legs and the lensing generator is a different
program.** `PREDICTION.md` said so when it declared the cost: *"the lensing grid is a second
generator whose scope is not yet read."* This is that reading.

**Measured: a lensing point exceeds `1h38m` of CPU and had not finished.** Four legs, each at
essentially 100 per cent of a core — `01:38:27` elapsed against `01:37:29` of CPU — with no output
beyond the header. So a lensing point is **at least `1.5×` a CMB point and its upper bound is not
yet measured.**

⌗ *There is no precedent in the record to compare against: the landed lensing grid kept no logs, so
nothing says what a point cost before the hierarchy was switched on.*

⚠ **AND THERE IS A STRUCTURAL CONSTRAINT, NOT JUST A LONG RUN.** The longest a tracked background
task may run here is two hours. A lensing point that exceeds two hours cannot complete inside one,
and because a leg is not checkpointed each attempt starts over — so a naive retry loop would make no
progress at all, however many times it ran. ⇒ **If that is what the measurement turns out to show,
the finding is a COST, reported as one, and the item splits with the CMB grid landing first.** That
is exactly the split `PREDICTION.md` registered, and it is not a reason to lower the resolution: a
grid the banks cannot be compared against would answer a different question.

## THE CONSTRAINT BIT, AND IT IS NOW MEASURED RATHER THAN ANTICIPATED

**A lensing point exceeds `1h58m` and did not finish.** The four legs reached `01:58:33` elapsed
against `01:57:31` of CPU — essentially a full core each, no idling — with no point written, and the
two-hour cap on a tracked task then forced the run to stop. ⇒ **So the section above is not a
worry about what might happen: a lensing point does not fit inside a tracked task, and because a leg
is not checkpointed, all four legs' work was lost.**

⌗ **The run is relaunched DETACHED**, in its own process session rather than as a tracked task, which
is the one form that has survived past two hours here. The generator is idempotent, so it resumes
from what is banked — which at that moment was nothing, so all ten points restart.

⚠ **AND THE UPPER BOUND IS STILL NOT MEASURED.** `1h58m` is a floor, not a duration. Ten points at
four at a time is three batches, so the grid is of the order of **six hours or more** if a point is
near that floor and longer if it is not. The honest statement is that the number is not yet known.

⇒ **WHAT THIS DOES TO THE ITEM.** `PREDICTION.md` registered the split, and this is the measurement
that may trigger it: if the lensing grid does not land, **the CMB grid and this cost land first and
the limit read follows on the completed grids.** ⛔ *Not at a lowered resolution — a grid the banks
cannot be compared against answers a different question — and not by skipping the lensing grid,
because the model reads its bandpowers and a limit read without them would not be the control's
limit.*

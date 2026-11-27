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

---

## ⛔ THE FIFTH DEATH, AND IT CHANGES THE CONCLUSION: THE LIMIT IS A REAP INTERVAL, NOT A BUDGET

Everything above reads the cost as a BUDGET — a point is expensive, ten points are more expensive
than one revision affords. **That reading is now superseded by a measurement, and the new one is
worse.** A fourth launch was made detached at `07:19:50` and a fifth death observed at `08:40`:

| | |
|---|---|
| launched | `07:19:50`, four legs, each its own process |
| last seen ALIVE | `08:21`, four legs at `48:47`, `48:43`, `48:40`, `48:39` of CPU |
| found GONE | `08:40`, no process, `0` of `10` points banked |
| in the logs | three lines per leg, all written at `07:19:51`; nothing after |
| exit status | none recorded — the generator's own log ends at its first line |
| OOM | none in `dmesg`; `15547` MB of `16087` free at the time of death |

⌗ **So the legs were not killed by anything they did.** No error, no traceback, no out-of-memory,
no disk pressure, and the one thing every death has in common is ELAPSED TIME: the `05:43` launch
was gone within about an hour and a half, and this one within about eighty minutes.

⇒ **THE OPERATIVE LIMIT IS NOT THE TWO-HOUR TRACKED-TASK CAP.** A detached process is reclaimed
here too, at a shorter interval than ONE lensing point needs. A point requires more than `1h58m` of
CPU and a leg is not checkpointed, so **a point can never reach its first write**, and every launch
loses everything. ⛔ *Relaunching a sixth time on an unchanged tree would not be perseverance; it
would be running a job already measured as unable to finish.*

### WHAT THIS MAKES THE NEXT STEP

The remedy is **not** a smaller grid and **not** more patience: it is that a leg must survive being
reclaimed. The expensive object is identified — `phi_shape(etaref)` in `phiphi.py` runs the
instrument over `NKP = 220` modes at about `176` state variables each with the hierarchy on, and
returns just two one-dimensional arrays, `kk` and `Phi`. That is a small checkpoint for a very
large computation, and the Limber loop over `36` multipoles that follows it is cheap by comparison.

⚠ **TWO THINGS ARE BEING MEASURED BEFORE ANY OF THAT IS BUILT, because the design turns on them
and neither is yet known:**

  ⓵ **How the solve's cost SPLITS between a fixed setup and a per-mode margin.** If the fixed cost
     dominates, then chunking the `k`-grid makes each resumed chunk pay that cost again and the
     chunked run could be slower than the unchunked one. The measurement is `evolve` at two mode
     counts, so the DIFFERENCE separates the fixed part from the marginal part — a single timing at
     one mode count cannot, and an early reading here showed over ten minutes of CPU for two modes,
     which is already evidence that the fixed part is not small.
  ⓶ **Whether the modes are INDEPENDENT**, so that solving a subset and concatenating is exact
     rather than approximately right. ⛔ *Not assumed from "a linear Boltzmann hierarchy separates
     in `k`": the solver batches the modes into one state vector, and whether anything couples them
     is a property of THIS code. The test is the same `k` values solved as one call and as two, with
     `Phi` compared — and until it passes, chunking is not licensed.*

⌗ *This section is the honest state: the cost is now understood well enough to say the grid cannot
be obtained here as the generator stands, and not yet well enough to say what replaces it.*

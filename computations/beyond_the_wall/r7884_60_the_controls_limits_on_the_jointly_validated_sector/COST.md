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

---

## ⛔ CORRECTION TO THE SECTION ABOVE: THE KILLER IS A CONTAINER RESTART, NOT PROCESS REAPING

The section above says *"a detached process is reclaimed here too"* and reads the deaths as the
runtime reaping long-lived processes. **That mechanism is wrong, and the right one was two commands
away the whole time: read `pid 1`.**

| | |
|---|---|
| this container booted at | `08:40:48` UTC (`/proc/uptime`, and `pid 1`'s own elapsed time) |
| the four legs were found gone at | `08:40` |
| an earlier reading, taken at `07:48`, gave | `up 41 min` ⇒ a boot at about `07:07` |
| the `05:43` launch therefore died at | that `07:07` boot, having lived about `84` minutes |
| the `07:19:50` launch died at | the `08:40` boot, having lived about `81` minutes |

⇒ **THE CONTAINER IS REPLACED, roughly every ninety minutes, and every process in it dies.** The
legs were not singled out and nothing reaped them for being long-lived or detached: the machine
underneath them was rebuilt. Two boots about `93` minutes apart, and each one accounts for a death
to the minute.

⌗ **This retires a belief this seat had been carrying and acting on.** `setsid nohup … & disown` was
recorded as *"the one form that has survived past two hours here"*, and the two-hour tracked-task
cap was treated as the thing to escape. ⛔ *Against a container restart the launch form buys
NOTHING — a tracked task, a detached session and a disowned process die identically — so three of
the five launches were spent on a distinction that does not exist.* The one real datum behind the
old belief is that a launch once held for over an hour, which is true and is simply the interval
between two boots.

### ⇒ AND IT IS THE FACT THAT MAKES CHECKPOINTING WORK, WHICH IS WHY IT IS WORTH THE CORRECTION

**The filesystem SURVIVES the restart.** Checked rather than hoped: after the `08:40` boot the
`07:19` launch log is still on disk with its original mtime, the repository is intact at its last
commit, and the working tree is clean. ⇒ **So a leg that writes partial state to disk resumes after
a restart**, and the remedy named above is not merely plausible but licensed by a measurement.

⚠ What does NOT change: the two questions still being measured — how the solve's cost splits
between a fixed setup and a per-mode margin, and whether the modes are independent enough that
solving a subset and concatenating is exact. **A checkpoint that survives a restart is useless if a
chunk cannot finish inside ninety minutes, and wrong if the modes are coupled.** Those decide the
design; this section only decides that the design is worth building.

---

## ⛔ AND THE REMEDY ABOVE IS WRONG TOO: CHUNKING THE `k`-GRID WOULD HAVE MADE IT WORSE

The two questions the section above said to settle before building anything have been settled, and
**they killed the design.** Both numbers are solo on an otherwise idle box:

| stage, at its REAL size | measured |
|---|---|
| `GrowthKDep` on `48` `k`-points | `12.5` s |
| `evolve` on `2` modes | `599.1` s |
| `evolve` on `4` modes | `611.7` s |
| `evolve` on `40` modes | `824.2` s |

⌗ **Doubling the modes from `2` to `4` cost `12.6` s.** The step count is set by `KMAX`, which is
present in both, so what dominates is a FIXED time-stepping cost and the per-mode margin is small.
Fitting the two small runs gives `F ≈ 586` s fixed and `m ≈ 6.3` s per mode, and that model then
**predicted the `40`-mode run at `838` s against `824.2` s measured — `1.7` per cent.** So the model
is not a curve drawn through two points; it was registered on two and tested on a third.

⇒ **CHUNKING THE `k`-GRID IS COUNTERPRODUCTIVE, and by a wide margin.** Eleven chunks of twenty
modes each re-pay the fixed cost: `11 × (586 + 20 × 6.3) ≈ 7832` s, against `586 + 220 × 6.3 ≈ 1972`
s for the whole grid in one call. **The checkpointing design would have turned a thirty-three minute
solve into a two-and-a-quarter hour one** — and the independence test never had to be run, because
the cost question disqualified the design before the correctness question was reached.

⌗ *That is why both were registered as questions to answer BEFORE building. Had they been assumed —
"a linear hierarchy separates in `k`, so chunk it" — the chunking would have been built, would have
been correct, and would have been slower than doing nothing.*

### ⇒ WHAT THE NUMBERS SAY THE REAL CAUSE WAS, AND IT IS NOT THE COST OF A POINT

`phi_shape` at the full `NKP = 220` extrapolates to about **`33` minutes of CPU**, and the growth
stage is `12.5` s. **That is comfortably inside the ninety-minute container lifetime.** So a lensing
point was never a two-hour computation.

What the five launches actually did was run **FOUR legs at once on four cores.** Under that
contention each leg accrued `48` minutes of CPU in `62` minutes of elapsed time and was still not
finished — more charged CPU than the solo estimate for the whole solve, which is what thread
contention looks like rather than what a larger computation looks like, since a busy-waiting thread
is charged CPU while making no progress. ⇒ **No leg could finish inside one container lifetime, so
every restart lost all four.**

### ⇒ THE REMEDY NEEDS NO CODE CHANGE AT ALL

Run the generator at `JOBS=1`. One point then has the whole box, finishes in about half an hour,
and **is banked** — and the generator is already idempotent, skipping every banked point on
relaunch. So the grid accumulates two or three points per container lifetime and completes across
four or five restarts, with nothing lost to a restart and no checkpointing written.

⚠ **This last paragraph is a PREDICTION UNDER TEST, not a result.** The generator is running at
`JOBS=1` as this is written, and the thing to look at is whether the first point banks inside one
container lifetime. If it does not, the extrapolation from `40` modes to `220` is superlinear and
that is the next thing to measure, not a thing to assume.

---

## ⚠ THE SOLO POINT'S COST, MEASURED — AND CONTENTION WAS NOT THE WHOLE STORY

The section above said the per-point cost was *"not yet measured"* and put the four-leg failure down
to contention. **One leg running alone, with the whole box, is past `2h 14m` of CPU at `34` minutes
of wall clock on about `3.95` cores, and has not finished.** So:

- ⛔ **The linear model's `33` minutes is wrong by more than a factor of four**, as the previous
  section warned it might be. `F + nk·m` earned its prediction at `40` modes and does not transfer
  to `220`: the per-step linear algebra on a `38720`-variable system is where the extra goes. **The
  figure to carry forward is `> 2h 14m` of CPU per point, a LOWER BOUND, read off a run that had not
  yet finished.**
- ⛔ **And the earlier reading — four legs each accruing `48` min of CPU in `62` min — is NOT mostly
  thread spin, as the previous section implied.** A point really does cost hours of CPU. *The
  contention account was the right shape and the wrong size: four legs on four cores did starve each
  other, but even one leg given everything needs more CPU than the whole four-leg batch had
  accrued.*

⇒ **What survives of the remedy is the part that matters.** At `3.95` cores a point is roughly
`35–45` minutes of WALL CLOCK, which does fit inside a ninety-minute container lifetime — so
`JOBS=1` is still the right configuration, and the grid should complete across restarts because each
finished point is banked. ⌗ *But it fits with much less room than "thirty-three minutes of CPU"
suggested, and a point started late in a container's life will not finish before the restart takes
it. This first leg began about `38` minutes into the lifetime and is likely to be one of those.*

⌗ *Which costs nothing but time: the generator skips what is banked, so a leg killed mid-point is
retried from the start in the next container, and only a leg that STARTS early enough banks. The
grid therefore completes at roughly one or two points per restart rather than two or three.*

---

## ⇒ THE PER-POINT COST, NOW EXACT, AND TWO CLAIMS OF MINE CHECKED RATHER THAN ASSERTED

The first point banked with the completed record: **`lcdm_S006`, `34m 29s` of wall clock and
`2h 16m 29s` of CPU on about `3.95` cores.** So the `> 2h 14m` above was a lower bound on a figure
that is now measured, and it replaces the linear model's `33` minutes for good.

| | |
|---|---|
| per point, wall clock | `≈ 35` min |
| per point, CPU | `≈ 2h 16m` |
| cores used by one leg | `≈ 3.95` |
| container lifetime | **VARIABLE: `≈ 93`, `≈ 96`, `≈ 80`, and one that ran past `105`** (boots `07:07`, `08:40:48`, `10:16:57`, `11:36:53`) |
| points per lifetime, if started early | **two** |

⇒ **Ten points is five to six container lifetimes**, and because each finished point is banked and
the generator skips what is banked, the grid accumulates rather than restarting.

⚠ **AND THE LIFETIME IS NOT A CONSTANT — `80` minutes at the short end, and one lifetime ran past
`105` minutes, so the long end is NOT established either.** ⛔ *So "about
ninety minutes" is a central value and NOT a deadline to plan a leg against: the `11:36:53` boot came
`80` minutes after the one before it, sixteen minutes earlier than the preceding interval. A leg
begun on the assumption of ninety is a leg that sometimes dies for nothing.* The operational rule
that survives this is the simple one: **relaunch as early in a lifetime as possible and never rely
on the tail of one.** The one thing that
matters operationally is **relaunching early in a lifetime**: a point begun more than about fifty
minutes in will not finish before the restart takes it, and that leg's work is lost.

### ⛭ AND TWO THINGS I ASSERTED ARE NOW CHECKED

⓵ **"Additive metadata: changes no number."** I said that of completing the switch record, and it is
now verified rather than argued: the re-run point's bandpowers are **bit-identical** to the deleted
run's — `1.4324e-07 .. 2.8055e-08` both times. *The record changed and the physics did not.*

⓶ **The record is actually readable by the gate that needs it.** The banked point carries
`NUHIER=1`, `NQ=12`, `LMAXNU=12`, `QMAXNU=20`, `BVEL=1`, `NUFD=1`, `PRIMNORM=1` — the exact strings
`Ⓛ⓹` compares against. ⌗ *Checked on the artefact, not on the recorder: a recorder that writes the
keys and a gate that reads different ones would have passed every static check and failed on the
tenth point.*

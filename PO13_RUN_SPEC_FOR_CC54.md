---
name: PO13_RUN_SPEC_FOR_CC54
description: PO-13's run specification for a node with compute — the one computation P15's acoustic section now names as open, with the flags, the convergence ladder, and what each run decides. Held outside the corpus beside PO13_WORKING_STATE.
status: WORKING DOCUMENT — deliberately not a paper
current: r4113
---

# PO-13 RUN SPEC — the CR arm at converged $k$ on the leaf congruence

***This supersedes the pre-`r3409` version of this file wholesale.*** *That version described
`LEAFPERT` as a default-off flag and said the instrument was byte-identical to its pre-`r3408` form
with the flags unset. **`LEAFPERT` has been the default since `r3409`** and the earlier text would
send a node to run the wrong configuration.*

## ⛭ WHAT THIS RUN IS FOR

*`P15 sec:refit-bound` was restated at `r4111` to report only what is in hand. It now names **one
computation** as the open item, and this is it. Until it is run, the peak spacing, the acoustic phase
and the peak heights are quantities the corpus does not report.*

**The instrument:** `computations/beyond_the_wall/ACOUSTIC_two_arm.py`.
**Both arms run on one set of equations**, so nothing measured between them is a difference of
machinery.

## ⛔ WHY THE EXISTING NUMBERS DO NOT ANSWER IT

*Two independent defects, and most of the retired figures carry both.*

**① The rate.** *The perturbations ran on the stacking rate until `r3409`. The rate rule assigns them
to the leaf — "a process running in the content — $\rs$, $r_D$, recombination, **the
perturbations** — takes the leaf's" — and **the leaf rate carries the radiation term.** Every P15
acoustic receipt is built at `r2376`–`r2512`, all below `r3409`.*

**② The $k$-integral.** *`r3870` found it truncated at the highest multipole **reported**, where
$\int P(k)\Delta_\ell(k)^2\,\dd k$ is not converged. **It was repaired on the control arm only**, and
`r3870` says so explicitly: "no CR number is produced or corrected. The CR arm is truncated by the
same mechanism." The control's height ratio moves $2.721 \to 2.393$ across the cutoff; a defect of
that size is a systematic, not a rounding.*

## ⛭ THE RUNS

*Ordered. Each is a gate on the next — **do not proceed past a failing convergence check**.*

### RUN 1 — the convergence ladder, both arms

```
for K in 1.5 2.0 3.0; do
  for A in lcdm cr; do
    KFAC=$K ARM=$A python3 computations/beyond_the_wall/ACOUSTIC_two_arm.py
  done
done
```

*`NK` is **derived** from `KFAC` and must not be pinned — the two guards pull against each other, and
reaching further in $k$ at fixed mode count coarsens $\dd k$ and breaks the sampling guard.*

⇒ **Decides:** whether the CR arm is converged, and at what cutoff. **The control is the calibrator**:
it must return $P_1/P_2 \approx 2.197$ and peaks near $220/540/812$ at the converged rung. *If the CR
arm's reported quantities still move between $2.0$ and $3.0$ by more than the control's own movement,
**it is not converged and nothing below is measured** — report that and stop.*

### RUN 2 — the datum freedoms as a range, at the converged `KFAC`

*The seam datum has **two** freedoms and the honest output is a **range**, not a value.*

| freedom | flag | readings |
|---|---|---|
| the common seam phase | `CRPHI` | a numeric grid over $[0,\pi)$, plus `entry` and `entryleaf` |
| what "flat in $k$" is read **at** | `CRAMP` | `flat`, `entry` |

```
KFAC=<converged> ARM=cr CRPHI=<phi> CRAMP=<amp> python3 .../ACOUSTIC_two_arm.py
```

⇒ **Decides:** the range of the first peak's position, the peak spacing, the acoustic phase intercept
and $P_1/P_2$ across the datum. **Report every reading, and the span.** *P15 already states the first
peak spans a factor of $2.26$ across the pre-repair readings; whether that survives convergence on the
leaf is exactly what this measures.*

⚠ ***The admissibility criterion is fixed here, before the numbers:*** *a reading enters the spacing
statistic only if it returns four peaks with the fourth at least a twentieth of the first. An interval
read off three features one of which is absent is not a spacing.*

### RUN 3 — the likelihood, both arms, identical settings

*Only if RUN 1 converged.* Score both arms on the same Planck binned $TT$ bins, at the converged
`KFAC`, with the control's own $\chi^2$ reported beside every CR figure.

⇒ **Decides:** whether there is an acoustic disagreement at all once the arm is converged on the rate
the framework assigns it — and, if so, its size against the control's floor.

⚠ ***Measure the floor as a model-to-model distance, not as a difference of two numbers each taken
against the sky.*** *The latter mixes how far the models are apart with where each sits relative to
one noise realisation, and it moved across three defensible reference $\Lambda$CDMs by an amount
comparable to the quantity being reported.*

## ⛔ WHAT NOT TO DO

- ***Do not set `STACKPERT=1`*** except to reproduce a retired figure for comparison. It recovers the
  pre-`r3409` behaviour, which is the configuration the framework does not assign.
- ***Do not pin `NK`.*** It is derived from `KFAC` for a reason recorded at the k-grid.
- ***Do not report a single first-peak position.*** It is a statement about a seam datum the
  construction does not fix. A range is the result; a value is a category error.
- ***Do not fit the shear coefficient.*** It is settled by derivation at $16/15$, and a coefficient
  chosen because it fits is a fitted parameter whatever it is called.
- ***Do not write any of this into a paper as narration.*** The corpus states one position. Findings
  land in `PO13_WORKING_STATE.md`; `P15 sec:refit-bound` is rewritten to the new state only once the
  runs are done, and it is rewritten rather than amended.

## ⛭ WHAT COMES BACK

*A single report into `PO13_WORKING_STATE.md` carrying: the convergence ladder for both arms; the
datum-freedom table with its span; the likelihood figures with the control beside them; and an
explicit statement of which of the retired figures the converged run reproduces and which it does
not. **If the diagnosis in the retired text — that the driving supplies the disagreement because a
geometrically fixed rate has no radiation-domination crossing — does not survive the leaf rate, that
is the most important thing the run can return**, since the leaf rate carries the radiation term and
the premise may not hold.*

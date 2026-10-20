# r7466 — NEITHER NAMED CANDIDATE CARRIES A RUNNING PHASE. THEY CARRY AN OFFSET, AND THE MODEL'S OWN PHASE RUN IS A STEP RATHER THAN A DRIFT

**THE QUESTION,** left open on purpose by the code seat: *"which quantity carries a running phase
at correct spacing, and you have already named the two candidates."*

**THE ANSWER. ⛔ NEITHER.** The driving moves the mean per-peak phase by `0.126` cycles — nearly
three times the whole drift — **at no cost in `ℓ_A` at all**, and it moves the phase's **run** by
`0.0029`, six per cent of the drift. The clean loading lever moves the mean by `0.016` and the run
by `0.0054`, twelve per cent. **Both are large phase effects with almost no run in them.** And the
drift is not hiding in the rest of the bank either: of the four parameter directions the largest
reaches four per cent of it.

**AND THE RUN AS REGISTERED IS ⛔ VOID.** Two of its three controls fired. That is the honest state
of it, `void_as_registered.txt` is kept, and **what the voided run measured is the result** — the
same shape as `r7454`, where the finding rested on reading once the instrument's own control had
spoken.

---

## ⌈ ① THE TARGET, DERIVED RATHER THAN ASSERTED

A series at period `P` against a comb of unit `ℓ_A` gives `ℓ_n = nP − c`, so
`φ_n = ℓ_n/ℓ_A − n = n(P/ℓ_A − 1) − c/ℓ_A` and

> **`s_required = P/ℓ_A − 1 = 311.79/298 − 1 = +0.04628` cycles per peak**

which fixes the **sign** as well as the size: the data's period is longer, so the run the model
would need goes **up** with `n`. ⌗ `PREDICTION.md` registered `0.0454`, converting `−96.6°` over
`104 ≤ ℓ ≤ 1886` at the banked base's `ℓ_A = 301.38`. **Two per cent apart, and the difference is
entirely which `ℓ_A` turns degrees into peaks.** Both are printed in the run.

---

## ⌈ ② THE BUDGET, WHICH IS WHAT MAKES THE NEGATIVE QUANTITATIVE

Every lever that moves the phase also moves `ℓ_A`, and **`ℓ_A` is already matched to `0.15` per
cent** — the whole budget is `0.452` in `301.380`. So the question is not whether a lever *can*
reach the drift but what reaching it **costs in the one number the sector already matches**:

| lever | `Δs` | `Δℓ_A` | cost of the whole drift |
|---|---|---|---|
| `H0`, plus-minus | `−0.00200` | `−8.778` | **`450` budgets** |
| `OM`, plus-minus | `−0.00121` | `−4.619` | **`391` budgets** |
| `WB`, plus-minus | `−0.00025` | `+2.077` | **`847` budgets** |
| loading, `RBFAC 0.5→1.5` | `+0.00589` | `+29.212` | **`507` budgets** |
| loading, `RBFAC 1.0→0.1` | `−0.01995` | `−28.961` | **`149` budgets** |
| `NS`, plus-minus | `−0.00017` | `0` | no `ℓ_A` cost; reaches `0.4` per cent |
| driving, fully removed | `−0.00289` | `0` | no `ℓ_A` cost; reaches `6.2` per cent |

⇒ **EVERY LEVER IS SPENT BEFORE IT ARRIVES.** The two that move `ℓ_A` would have to break the comb
by two to three orders of magnitude more than it is matched to; the two that cost nothing in `ℓ_A`
reach under seven per cent of the drift at **full throw** — the driving removed *entirely*, not
perturbed.

---

## ⌈ ③ AND THE PHYSICS THE VOIDED RUN STILL SETTLES: THE MODEL'S PHASE RUN IS A STEP

The residual's drift is a **line** in `ℓ` — that is the `PART F` identity, exactly. **The model's
own per-peak phase is not a line.** On the `CR` base it is

> `φ_n = −0.1516, −0.1477, −0.2527, −0.2170, −0.2372`

and a **step** between the second and third peaks fits it **`5.8` times better than a straight line
on the same two parameters**. Swept over the whole bank: **the step beats the line on `41` of `43`
configurations de-tilted and `41` of `43` raw, and the cut sits between peaks `2` and `3` in `39` of
`43`.** The step's height is stable at `−0.082` to `−0.099` across every parameter direction in both
grids and both arms — **the levers move the step's height by under ten per cent and never turn it
into a slope.**

⇒ ***A LEVER THAT MOVES A STEP CANNOT SUPPLY A LINE.*** And the step sits in the band the row itself
records as *tracking matter–radiation equality on both routes to it, and therefore fixed by the same
epoch the distance data fix* — so the one large feature in the model's phase run is pinned by data
the sector already matches, and it is the wrong shape for the residual besides.

⌗ **Which is where this meets the row's other half.** A linear run in `ℓ` needs a mechanism whose
effect **grows with `ℓ`**; the acoustic levers act through `ℓ_A`, a fixed unit, which is precisely
why they shift the phase without tilting it. `PO-87` step ① has already located the contrast excess
*"in the projection from wavenumber to multipole and not in the acoustic dynamics."* **Two halves of
the row, measured independently, point at the same side of the same boundary.** *Stated as a
direction with its evidence, not as a proof: nothing here computes a projection term.*

---

## ⌈ ④ THE CONTROLS, AND WHY THE SECOND ONE FIRING IS THE CRUX

**Ⓥ① INSTRUMENT IDENTITY — PASS.** The imported peak finder returns `cc66.156`'s printed `CR` base
mean phase `−0.20124`, alternation `+0.01511` and `ℓ_A = 301.380`, to every digit printed. **One copy
of the predicate, loaded from `r7201`'s own file by `ast` so that file's analysis does not run**
(`r7445`'s rule).

**⛔ Ⓥ② NOT BLIND TO THE DRIVING — FIRED, and the reason matters more than the firing.** Removing the
driving moves `s` by `−0.00289` against a `0.01441` error. **But both spectra are deterministic runs,
so that slope difference is exact — it is not a noisy measurement.** The error beside it is the
scatter of a **line** fitted to a **step**. ⇒ ***What kills this statistic is not measurement noise.
It is the misfit of a line to a step, and the misfit is five times the effect being hunted.***

**⛔ Ⓥ③ NO AMPLITUDE LEAK — FIRED.** `s` with the global de-tilt off is `−0.00461` against `−0.02405`
with it on: **the de-tilt, which has no phase in it, moves the statistic by `0.01944` — `42` per cent
of the target and more than any lever in the table.** The mechanism is not subtle and is worth
stating because it is general: **multiplying a curved peak by `ℓ^−tilt` shifts the location of its
maximum.** A de-tilt is phase-neutral on a Fourier period and is **not** phase-neutral on a peak
position, which is the quantity both statistics are built from.

**⌗ AND THE FIRST QUESTION AFTER A CONTROL FIRES IS WHAT ELSE STANDS ON WHAT IT CAUGHT.**
`cc66.156`'s mean per-peak phase is de-tilted too, and two banked receipts and `r7201`'s lever table
rest on it. **The leak reaches the absolute phase and very largely not the differences:**

| | de-tilted | raw | apart |
|---|---|---|---|
| absolute mean phase, `CR` base | `−0.20124` | `−0.26373` | `+0.06249` = `22.5°`, **`1.35×` the whole target** |
| loading `dφ/dlnRBFAC` | `+0.01642` | `+0.01373` | `16` per cent |
| driving `dφ`, `CR` | `+0.12589` | `+0.12992` | `3` per cent |
| driving `dφ`, control | `+0.12651` | `+0.13020` | `3` per cent |

⇒ **THOSE RECEIPTS ARE NOT HURT: they report differences, and the differences hold to three per cent
on the driving and sixteen on the loading.** What must not be read as a phase is the **absolute**
mean — and nothing reads it that way. *Reported because the control fired, not because anything was
found wanting.*

---

## ⌈ ⑤ THE SCORECARD, AND THE MISS THAT CHANGES THE PRESCRIPTION

| arm | predicted | measured | |
|---|---|---|---|
| `Ⓐ` the tilt control | tilt `<1/3` of `WB` | `0.00016` against `0.00034`, ratio `0.465` | **MISS** |
| `Ⓑ` the clean loading | non-zero, **negative**, order `0.01` | `+0.00537` | **MISS on the sign** |
| `Ⓒ` the driving | `3×` to `20×` the loading | `0.54×`, same sign both arms | **MISS** |
| `Ⓔ` the reach | no lever reaches it admissibly | best is `12` per cent; `149`–`847` budgets | **HIT** |
| `Ⓕ` the linearity | scatter `≥2×` the slope's error | `3.16×` | **HIT** |
| `Ⓖ` the resolution | `se(s)` of the same order as the target | `0.01116` against `0.04628`, ratio `0.24` | **MISS** |

**Ⓐ MISSES ITS CRITERION AND INVERTS ITS MEANING.** The tilt moves `s` by `0.4` per cent of the
target — the new statistic is *not* fooled by it, which is what was wanted — **but `ω_b` moves it by
`0.7` per cent, so the statistic is deaf to both.** The old statistic was fooled; this one is blind.

**Ⓒ MISSES BY INVERTING THE MEAN-PHASE ORDERING.** On the mean the driving is `7.7×` the loading; on
the run it is `0.54×`. ⇒ That inversion *is* the headline: **the driving sets the phase, not its
run.**

**⛔ AND Ⓖ IS THE MISS WORTH THE MOST, BECAUSE IT CHANGES WHAT IS OWED.** The prediction was that
five peaks could not resolve the drift and the cost of settling it would be **more peaks**. The
measurement says the opposite: `se(s) = 0.01116` against a target of `0.04628` makes the drift a
**`4.1σ`** effect on five peaks. **So the statistic is not resolution-limited.** What fails is the
**shape** — and the levers' own slope effects are six to twelve per cent of the drift whatever the
error bar. ⇒ ***The owed object is not more peaks. It is a different shape, and the earlier
receipt's "it needs a grid" is not what this measurement asks for.***

---

## ⌈ ⑥ WHAT IS SUPPLIED, AND WHAT IS NOT

⇒ **`PO-87` ② is answered in the negative with a reason and a budget**: the residual's drift is a
linear run at correct spacing, and neither the driving nor the baryon loading — nor `H0`, `Ω_m`,
`ω_b` or `n_s` — can source a run, because the model's own per-peak phase has a step in it and the
levers move the step's height rather than tilting it.

⇒ **AND THE OWED STATISTIC IS NOT THE ONE REGISTERED HERE.** It must be a phase observable with no
amplitude convention in it, since a de-tilt moves a peak position by `42` per cent of the drift; and
it must be able to express a run against a step, since a straight line is the wrong summary by a
factor of `5.8`.

**⌗ THE ROW IS THE REGISTER'S: supplied, not applied.** No paper edit is owed. **No new spectrum was
run and nothing was refitted** — everything is read off the bank. **`PO-87`'s fourth-peak half is
data-gated and is not touched**: nothing above is reported against the fourth-peak datum.

**THE PRICE:** `0.45`, `0.46`, `0.46` s over three runs on `43` banked configurations.

---

*`PREDICTION.md` registered `7dd49bd7` at `4d62831a`, before `phase_slope.py` existed. The seed is
pinned per `L-249`'s repair rule: the historical digest at the commit it stood at, the bank's present
readability asserted separately, and the live check directional.*

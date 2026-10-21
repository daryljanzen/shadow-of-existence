# r7480 — THE AMPLITUDE HALF IS CONVERGED, AND THE DISCHARGE RELOCATES `r7476`'s NINE PER CENT RATHER THAN DISSOLVING IT

**COMPUTES:** `NK`, the mode count of `ACOUSTIC_two_arm.py`'s projection k-grid, on the refit
minimum's own configuration. Nothing else is pinned.

**THE QUESTION.** `r7476` closed `r7474`'s coverage qualification on the projected statistic — it
moved `−0.00004`, `0.09` per cent of the `0.045` excess — but it closed **by a cancellation**: the
amplitude ratio rose `+0.00434` while the phase cosine fell `−0.00417`, in opposite directions, and
the statistic mixes the two by its own definition. That licensed the order's conclusion and did
**not** license a claim that the contrast is converged **component-wise**. This asks whether the
`4.0` points per Bessel period both of those numbers were read at is converged, by running the same
arm at `8.0`.

---

## ⌈ ① ⛔ FIRST, THE FOLLOW-UP I MYSELF ROUTED WAS WRONG, AND READING THE INSTRUMENT SHOWED IT BEFORE A RUN WAS SPENT

`r7476`'s reply proposed *"one more continuum run on the control arm"*. The instrument's k-grid is
built as

```
if ARM == 'cr' and os.environ.get('KCONT', '0') != '1':   # the discrete physical ladder
else:                                                      # linspace(12, KMAXL, NK*3)
```

⇒ **the ladder branch is guarded by `ARM == 'cr'`, so the control arm is ALREADY the continuum and
the continuum knob is a no-op on it.** That run would have measured nothing and returned a null that
looked like a result. *The knob that separates convergence from configuration is the mode count.*
**This is the second time in four revisions that a proposal of mine was repaired by reading the
object rather than by running it, and both repairs cost nothing because they were made first.**

---

## ⌈ ② THE RUN — one variable changed from `r7476`'s, which was itself one from the launcher's

`NK=1698` on `r7476`'s own invocation, everything else identical. The instrument's own log reports
**`5,094` modes at `8.0` points per Bessel period** — a density ratio of exactly `2.000` against
`r7476`'s `4.0`, so the new step is directly comparable with the one already measured. Wall cost
`62` minutes; the run and its log are banked beside this file.

---

## ⌈ ③ THE MEASUREMENT — ONE ARM AT THREE DENSITIES, AGAINST THE SAME CONTROL

| | projected | amplitude ratio | phase cosine | `ℓ_A` |
|---|---|---|---|---|
| **LADDER** `2.3` pts/period | `+1.04520` | `1.04552` | `+0.99969` | `301.799` |
| **CONTINUUM** `4.0` pts/period | `+1.04516` | `1.04986` | `+0.99552` | `301.799` |
| **CONTINUUM** `8.0` pts/period | `+1.04516` | `1.04986` | `+0.99552` | `301.799` |
| **step `2.3 → 4.0`** | `−0.00004` | **`+0.00434`** | **`−0.00417`** | — |
| **step `4.0 → 8.0`** | `+4.07e-09` | **`+1.24e-09`** | **`+2.70e-09`** | — |

> **The second step is zero to five decimals in all three quantities, and it is zero at the ninth.**

⇒ **`4.0` POINTS PER BESSEL PERIOD IS CONVERGED FOR BOTH COMPONENTS, and `r7476`'s component
qualification DISCHARGES: its two numbers are the resolved ones.**

---

## ⌈ ④ AND THE SAME READING RELOCATES THE NINE PER CENT RATHER THAN DISSOLVING IT

Read at the level of the spectrum rather than of the statistic, the two steps are not comparable
quantities at all:

| the spectrum itself | max rel | mean rel | worst at |
|---|---|---|---|
| ladder → `4.0` pts | **`6.46e-02`** | **`2.27e-02`** | `ℓ = 1852` |
| `4.0` pts → `8.0` pts | `6.43e-07` | `4.61e-08` | `ℓ = 1972` |

**Five orders of magnitude.** So the whole of the gap between the ladder and the continuum is the
gap between **two summand sets** — a discrete physical ladder and a continuum — and **not** a
numerical property of either. And the instrument's own note at the k-grid takes a position on which
set is the object:

> *"For CR the ladder `k_L = sqrt(L(L+2))/r_0` is **PHYSICAL** — the sum is the object, not an
> approximation to an integral — so its coarseness is not aliasing."*

⇒ **If that note stands, the ladder's `1.04552` is the arm's number and the continuum is the check,
which is exactly how `r7476` used it; and the `9.6` per cent is then the measured price of
discreteness — a modelling commitment of the row, not an error bar of the instrument.** *Which of
the two the row should carry is `PO-87`'s to rule. It is not decided here, and nothing is applied.*

⌗ **What this does NOT say.** It does not say the ladder is right. It says the alternative to the
ladder is converged, so the choice between them can no longer be deferred to numerics — which is
the only thing a convergence run can settle, and it settles it in the direction that makes the
remaining question a physical one.

---

## ⌈ ⑤ THE CONTROLS — four held, one was registered inapplicable and said so, one was added

**Ⓥ① THE SAME CONFIGURATION, FROM WHAT THE ARTEFACTS CARRY — PASS at zero.** `ℓ_A`, `D_M` and `r_s`
identical to **both** the `r7476` continuum and the banked ladder at `0.000e+00` relative
difference; the `ℓ` grid identical in length (`238`) and both endpoints (`100`, `1996`) against
both. *Checked against two references rather than one, because `r7474` withdrew an arm over exactly
this: two files sharing a stem that differed in reported reach.*

**Ⓥ② THE DENSER PATH ACTUALLY TAKEN, FROM THE INSTRUMENT'S OWN LOG — PASS.** `5,094` modes against
the registered `5,094`; `8.0` points per period against the registered `8.0`; the density ratio
`2.000`; and the line the instrument prints *only* when the knob is unset absent. *Read out of the
log, never out of the environment I set — `r7468`'s lesson.*

**Ⓥ③ THE SAME STATISTIC — PASS.** All four of `r7093`'s printed rows reproduced, worst difference
`2.97e-05` against the registered `1e-4`, the predicate imported by `ast` rather than copied.

**Ⓥ④ REGISTERED AND INAPPLICABLE, REPORTED THAT WAY RATHER THAN SCORED.** `PREDICTION.md` carried
`r7468`'s guard — *adjacent raw phase samples closer than π* — across out of habit. `r7093`'s
statistic takes no phase unwrap; it reads an oscillation about a running mean on the `ℓ` grid, so
there are **no raw phase samples** for a spacing to be checked on. ⇒ **NOT APPLICABLE**, and saying
so is the honest score. *A control carried from another instrument is not a control.*

**Ⓥ⑤ ADDED AFTER THE REGISTRATION, AND DECLARED AS ADDED — PASS.** The guard that **does** belong to
this instrument is the instrument's own: `UNDER-SAMPLED` and `k-TRUNCATED` both absent from **both**
continuum logs. *Its own verdict rather than a second one of mine.*

**Ⓥ⑥ ADDED AFTER THE REGISTRATION, AND DECLARED AS ADDED — PASS, and it is the one this result needs
most.** The components came back **equal to five decimals**, and `r7468` is the precedent for what
that can mean: an instrument agreeing with itself is not correctness. So the null is shown to be a
**measured** null before it is read as one — the two artefacts are **different files** (digests
`e688a10d…` and `27a74604…`), and their spectra **do** differ, by `6.43e-07` at worst. ⇒ **The zero
is a measurement, not a file read twice.**

---

## ⌈ ⑥ THE ARMS, AGAINST `PREDICTION.md` — digest `1cf54a82`, pinned `5190ba5f`, before the run existed

| arm | registered | measured | |
|---|---|---|---|
| **Ⓐ** projected | `\lvert Δ \rvert < 0.002` | `+4.07e-09` | **HIT** |
| **Ⓑ** amplitude step | `< 0.00217`, half the first | `1.24e-09` | **HIT** |
| **Ⓒ** phase step | `< 0.00209`, half the first | `2.70e-09` | **HIT** |
| **Ⓔ** opposite signs again | yes | **no second step exists** | **VACUOUS** |
| **Ⓕ** amplitude step keeps its sign | yes | **no second step exists** | **VACUOUS** |
| **Ⓖ** read price | reported | `4.4`/`4.3`/`4.6` ms | reported |

⛔ **Ⓔ AND Ⓕ ARE REPORTED AS VACUOUS AND NOT AS A HIT OR A MISS, AND THAT IS A POINT ABOUT
PRE-REGISTRATION RATHER THAN A CONCESSION.** Both were registered on the presumption that there
would *be* a second step to take the sign of. There is not. Scoring a sign test on a step of
`1.2e-09` would be reading a verdict out of an empty set — the same error as treating an identity as
an obstruction before establishing what it ranges over. **A registered arm whose domain the result
empties is a third outcome, and the register deserves to see it named rather than quietly counted as
a miss.**

⌗ Three hits, two vacuous, five controls held and one declared inapplicable. **The registered
outcome map's first branch — `Ⓑ` and `Ⓒ` both hit ⇒ `4.0` is converged and the qualification
discharges — is the one that obtained**, and it was written down before the run.

---

## ⌈ ⑦ ⛔ AND A DEFECT FOUND WHILE BANKING THIS ONE, WHICH WAS ALREADY TRUE OF `r7476`

`r7476`'s receipt says *"the run and its log are banked beside this file"*, and its `Ⓥ②` reads that
log. **The log was never banked.** The repository's `.gitignore` carries `*.log` at line `6`, so the
file sat on disk, was read by the control, and was excluded from every commit — which `git status`
reports by simply not mentioning it. ⇒ **A control that reads a file the repository does not carry
is not reproducible from the repository, and a receipt that says the file is banked is wrong about
its own contents.**

**The repair, and it is the smallest one:** both logs are renamed to `*_log.txt`, which the ignore
rule does not match, and this revision's reader points at those. *No gate is built and none is
touched — the instruments are frozen, and this is a receipt's own filename, not an instrument.*

⌗ **This is the third time in this line's recent revisions that the defect was in what an artefact
IS rather than in what it says** — `r7474` withdrew an arm over two files that shared a stem and
differed in reach, `r7480` ④ above turns on two summand sets that share a configuration, and here a
file that was read but never carried. **The pattern is worth the register's attention more than this
instance is: a thing named in a receipt has to be checked on the object, and "it is beside the
file" is a claim about the repository, not about the directory.**

---

**Nothing is applied to the register. Supplied, not applied.**

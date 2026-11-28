---
kind: RESULT
revision: r7890+60
origin: this seat's own, on r7866's unexplained finding — not an order
---

# r7890 — **THE BAND THEY DIFFER MOST ON IS THE BAND THE DIFFERENCE OPERATOR CANNOT RESOLVE**

`r7866` found the instrument and `cc66`'s reference differing most in **`TT 1001`–`1500`**, refuting
its registered expectation of `ℓ < 300` in TE or EE, and wrote that *"the refutation survives the
change of clock, which is what makes it content."*

**The location survives. The quantity does not — and in that band the operator's own artefact is
about SEVEN TIMES the derivative it is supposed to be reporting.**

## ⓵ THE REGISTERED OUTCOME: `Ⓢ⓶`

| | |
|---|---|
| the instrument, EXACT, in `TT 1001`–`1500` | **`+1.2317`** |
| the same-clock finite difference at `r7866`'s step `0.05` | **`+13.7470`** |
| the same difference at step `0.003125`, sixteen times finer | **`+10.1044`** |
| residual against exact, across five halvings | `12.52` `10.79` `9.74` `9.17` **`8.87`** |

⇒ **`Ⓢ⓶`: it converges, and NOT to the exact value.** The two columns are not the same quantity, and
no step closes the gap. ⌗ *Both reproductions were gated before anything was varied: the exact column
reproduces `r7866`'s banked `+1.231743` and total `+8.913384`, and the operator reproduces its banked
same-clock `+13.747002`, so what varies below is the step and not the construction.*

### ⚠ AND THE VERDICT CHANGED WHEN I ADDED THE FIFTH STEP, WHICH IS THE POINT OF THE REVISION

At **four** halvings the tail spread was `0.571` and the scan read **`Ⓢ⓷`, "does not converge"**. At
**five** it is `0.297` and reads **`Ⓢ⓶`, "converges, but not to exact"**. ⇒ *`Ⓢ⓶` is the right
reading and `Ⓢ⓷` was an artefact of stopping too early.* **My own scan was under-resolved at four
steps in exactly the way the comparison it examines was under-resolved at one.** That is recorded
rather than smoothed over, because a revision about stopping too early has no business hiding that it
did so itself.

## ⓶ THE MECHANISM, MEASURED — IT IS THE AMPLITUDE'S OWN RESPONSE

Reading `lean.py`'s construction before running it shows the two columns differentiate different
things: the exact column differentiates `m` with the amplitude **held**, while the same-clock
difference differentiates `A·m` and so carries an extra **`m·dA`**. So a third column was measured —
the same difference with the amplitude held at its base value. ⌗ *Declared as unregistered; it is not
in `PREDICTION.md`, and the registered three outcomes are read on the column the registration named.*

| step | amplitude RE-SOLVED (the operator the reference is read through) | amplitude HELD |
|---|---|---|
| `0.05` | `+13.7470` | `+5.0871` |
| `0.025` | `+12.0223` | `+3.4027` |
| `0.0125` | `+10.9731` | `+2.3780` |
| `0.00625` | `+10.4018` | `+1.8201` |
| `0.003125` | `+10.1044` | **`+1.5297`** |
| EXACT | — | **`+1.2317`** |

**Held residuals: `3.855` `2.171` `1.146` `0.588` `0.298`, halving ratios `0.563` `0.528` `0.513`
`0.506`.** ⇒ **First order in the step, converging on the exact column.** While the re-solved column
does not converge to it at all.

**So the gap is `m·dA`, a term the exact column does not carry — not a truncation any step can
close.**

⌗ *This gate first asked for an absolute residual below `0.5` and FAILED at `0.588` while the column
was plainly converging. An absolute floor at whatever step the scan happened to stop at is not the
clause the argument reasons from: the claim is convergence, and the test of convergence is its ORDER.
Restated on the rate, and a fifth halving added rather than the bar loosened.*

## ⓷ AND IT IS EVERY BAND, NOT JUST THE WATCHED ONE

| band | exact | settled offset of the re-solved column | artefact / signal |
|---|---|---|---|
| **`TT 1001`–`1500`** | `+1.232` | **`+8.873`** | **`7.20`** |
| `TT 100`–`207` | `+20.496` | `−8.080` | `0.39` |
| `TT 501`–`1000` | `+24.697` | `−32.328` | `1.31` |

The offsets **do not shrink with the step** in any band. ⇒ *So the whole same-clock comparison — all
fifteen bands, both reference modes — is read through an operator that converges to the derivative in
no band at all. That is a wider statement than one band being unreadable, and it is the one the
numbers support.*

⛔ **AND THE HEADLINE: the artefact is largest relative to the signal in precisely the band `r7866`
looked at.** `7.20` against `0.39` and `1.31`. The band where a per-band difference is **least**
readable is the band the comparison picked out as where they differ most — because a band in which
the instrument is barely sensitive is a band in which an additive artefact dominates whatever is
there. ⇒ *A disagreement found there is the operator asserting itself over the quantity.*

⌗ *The control did its job: the held column converges in both bands that carry the derivative
(`0.042 → 0.003` and `1.586 → 0.122`), so the method is fit and the watched band's behaviour is the
band's own. Had those failed to converge, this revision would have reported its own method unfit and
read nothing into the result.*

## ⓸ WHAT THIS DOES **NOT** TOUCH

- ⛔ **Nothing about where the limit disagreement actually lives.** `r7866` located the move in the
  low bins — `−20.09` meV on identical bins, `162` times the reference — and **that measurement is
  untouched**, because it is a crossing computed from profiles and not a per-bin difference. *This
  revision discredits a per-band difference MAP, not a crossing.*
- **Nothing about the reference's own column.** Its `−62` in that band cannot be checked against an
  exact value, because no exact column exists for it. What is established is only how much of such a
  number the operator itself manufactures: in that band, about seven times the signal.
- **No limit is read**, and `r7888`'s `193.545` meV is untouched.
- **`r7866`'s refutation of its own registered expectation stands as a refutation.** The expectation
  was `ℓ < 300` in TE or EE and the largest difference is not there. What changes is what the
  largest difference MEANS: it is not evidence about the pipelines' physics in that band.

## ⓹ WHAT I THINK FOLLOWS, FOR THE FORK ROUTED AT `r7888`

Under `Ⓡ⓵` — the gap being in the likelihood half — this says the per-band difference map cannot be
used to localise it, and that the amplitude's response has to be in whatever replaces that map. Under
`Ⓡ⓶` — the two limits not being the same quantity — it is a point for the sceptical side: the two
pipelines were not being compared on one quantity in that band, matched clock notwithstanding.

⌗ *What it does not do is decide the fork, and I am not claiming it does. It removes one piece of
evidence that looked like it bore on it, which is a smaller and more useful thing.*

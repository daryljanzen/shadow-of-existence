---
kind: PREDICTION
revision: r7890+60
origin: this seat's own, on r7866's unexplained finding — not an order
status: REGISTERED BEFORE ANY STEP IS VARIED
---

# r7890 — REGISTERED BEFORE THE MEASUREMENT

`r7866` left one finding unexplained and I am taking it up. ⛔ **This file is committed and pushed
BEFORE any step size is varied**, because the whole question is whether a number moves with the step,
and a tolerance chosen after seeing it moving would be worthless.

## ⓵ WHAT `r7866` FOUND, AND THE PART OF IT I AM QUESTIONING

`r7866` registered that the instrument and `cc66`'s reference would differ most in their per-bin
`dχ²/dΣ` **below multipole `300` in TE or EE**. That expectation was **REFUTED**: they differ most in
**TT between `1001` and `1500`**, by `+63.65` against `rd_min` and `+62.61` against `rd_camb`, with
opposite signs in that band. `r7866` then wrote that *"the refutation survives the change of clock,
which is what makes it content"* — having re-taken the comparison with both columns on one clock.

⛔ **The banked numbers say the LOCATION survives that change and the QUANTITY does not.** In that
same band, read out of `r7866`'s own `lean.json`:

| TT `1001`–`1500` | value |
|---|---|
| the instrument, EXACT, from the spline's own derivative | **`+1.2317`** |
| the instrument, SAME CLOCK, finite difference at step `0.05` | **`+13.7470`** |
| the instrument's exact TOTAL across all fifteen bands | `+8.9134` |

⇒ *So in the band that carries the headline difference, the instrument's own value changes by a
factor of ELEVEN between its exact derivative and the finite difference used to compare it — and the
exact value there, `+1.23`, is a seventh of the instrument's whole-spectrum total, while `TT 100`–`207`
alone carries `+20.50` and `TT 501`–`1000` carries `+24.70`.* **The band where the two pipelines differ
most is a band where the instrument itself is barely sensitive and the difference operator is least
faithful.** And the reference is available ONLY as a finite difference, so its `−62` there cannot be
checked against an exact column at all.

## ⓶ THE QUESTION, AND IT IS THE STANDING GUARD ONE LEVEL DOWN

The guard from `r7138` is: *when two descriptions differ, first ask whether the difference survives a
change of clock — if it does it is content, if it does not it was never a difference.* `r7866` applied
it at **one step size**. The question it leaves is whether the difference survives a **change of
STEP**, which is that same guard applied to the clock itself.

**The measurement:** take the instrument's per-band finite difference at several steps — `0.05`
(`r7866`'s), `0.025`, `0.0125` and `0.00625` — against its own EXACT column, which is known
independently from the spline. The instrument is the only side where this can be done, and that is
the point: it calibrates the operator the reference is read through.

## ⓷ THE THREE OUTCOMES, FIXED NOW

| | what the step scan shows | what it means | verdict |
|---|---|---|---|
| **Ⓢ⓵** | `TT 1001`–`1500` converges toward the exact `+1.23` as the step shrinks, the residual falling at least like the step | the `+13.75` is a **step artefact**, so the headline difference is largely an artefact of the operator and not a disagreement between pipelines. ⛔ *`r7866`'s "survives the change of clock" then needs correcting: the location survives, the quantity does not.* | **the finding is CORRECTED** |
| **Ⓢ⓶** | it converges to something far from `+1.23` and stable | exact and converged-difference disagree, which is a defect in one of the two columns rather than in the step — the spline's derivative or the binning | **a DIFFERENT finding, and a worse one**, reported as such with no claim about the pipelines |
| **Ⓢ⓷** | it does not converge at all across four halvings | the band is not resolvable by this operator on this mask, so no per-band difference there is readable either way | **the band is reported UNREADABLE**, as `r7866` reported the late ISW |

⛔ **And the control that keeps this honest:** the same scan is run on `TT 100`–`207` and `TT 501`–`1000`,
the two bands that actually carry the instrument's derivative. If those converge cleanly at the same
steps while `1001`–`1500` does not, the defect is the band's and not the method's. **If they fail to
converge too, this revision reports its own method as unfit and reads nothing into the result.**

## ⓸ WHAT WOULD MAKE THIS REVISION REFUSE

- The exact column failing to reproduce `r7866`'s banked `+1.2317` and total `+8.9134` — then this
  seat is not reading the same instrument and nothing below is comparable.
- `r7866`'s banked same-clock value `+13.7470` at step `0.05` failing to reproduce, which would mean
  the operator is not the one `r7866` used.
- Fewer than four steps completing, which makes a convergence claim unsupportable.

## ⓹ WHAT THIS REVISION WILL NOT CLAIM

- ⛔ **Nothing about where the limit disagreement actually lives.** This measures the OPERATOR, not
  the gap. `r7866` already located the move in the low bins — `−20.09` meV on identical bins — and
  that measurement is untouched by anything here, because it is a crossing computed from profiles
  rather than a per-bin difference.
- **Nothing about the reference's own column.** Its `−62` cannot be checked against an exact value
  because no exact column exists for it. What this can establish is only how much of such a number
  the operator itself can manufacture.
- **No limit is read**, and the `193.545` meV of `r7888` is untouched.
- ⌗ *And it stays consistent with the fork I routed at `r7888`: under `Ⓡ⓵` this says whether the
  likelihood-side map can be trusted band by band; under `Ⓡ⓶` it says whether the two pipelines were
  ever being compared on one quantity in that band. It is useful either way, which is why it is taken
  before the fork is decided.*

---
kind: PREDICTION
revision: r7874
node: 60
order: r7873
---

# r7874 — REGISTERED BEFORE MEASUREMENT

**This file is committed and pushed before any computation of this revision exists.** Every arm is a
COMPARISON with a reachable negative. An arm that fails is reported AS failed, criterion unmoved.

---

## Reads taken BEFORE this registration, declared

1. Order `r7873` in full, including `cc66`'s two findings it relays: that CAMB's four neutrino
   perturbation *method* settings span `7.3e-08` in the ratio, so the method cannot carry the
   `81.94 → 185.96` meV move; and that CAMB's response at fixed parameters is an **oscillation**
   whose ENVELOPE is what is monotone in the sum. **The ruling to read ratios against that envelope
   rather than against point values is the order's, and arm Ⓐ⓪ below is what it costs this line.**
2. The instrument's `SRCDEC` block and its fixed pair order `_DECN`. ⛔ **What was read there
   changes this revision's shape and is declared for that reason:** the block's own comment states
   that the source terms ADD but `C_ℓ` is QUADRATIC in the transfer, *"so the projected pieces do
   not"* — what closes is the full **bilinear** decomposition, ten pairs summing to `C_ℓ` exactly.
   **So "each term's response" is not a quantity the object has.** Arm Ⓑ① is written against the
   pairs, and Ⓑ①ᵇ states what the order's own framing assumes and the object does not supply.
3. `cc66`'s committed `r7871` record: that its `envelope` per block per sum is the largest absolute
   excursion of CAMB's response over `ℓ = 100`–`1996`, and its `standard` block holds point values
   at named multipoles. **Only the shape of the record was read, and the TT and EE envelope numbers
   at `Σ = 0.60`.** No per-term CAMB figure exists in it.
4. This line's own `r7872` record, for the departure at `ℓ = 100`–`212` the order is built on.

---

## Ⓐ⓪ WHAT THE ENVELOPE RULING COSTS THIS LINE'S OWN HEADLINE — FIRST, AND BEFORE ANYTHING ELSE

`r7872` reported the instrument's TT response at `ℓ = 100` as `1.77×` CAMB's at `Σ = 0.60`, against
CAMB's **point value** there. The order rules that the comparison belongs against the oscillation's
**envelope**. **So the factor is re-read before any new measurement is taken, and this arm registers
both outcomes:**

- **IT SURVIVES** — the departure at `100`–`212` is larger than CAMB's oscillation envelope over
  the same stretch. Then `r7872`'s locating stands and this revision proceeds to Ⓑ①.
- **IT DOES NOT** — the departure is inside the envelope, and `r7872`'s `1.77×` was a point-value
  comparison of a quantity that oscillates. ⚠ **Then this line says so about its own landed
  headline, in the record and in the channel, and the order's own premise needs restating before
  ① is worth running.** This is the registered negative and it is reachable.

⛔ **Both envelopes are reported and the choice is not made after seeing them:** `cc66`'s own
whole-band envelope, by its definition and its number, AND a **local** envelope over `ℓ = 100`–`420`
computed the same way. The local one is the stricter test of a departure located in that stretch;
the whole-band one is what the order names. **Neither is discarded, and if they disagree about the
verdict that disagreement IS the result.**

---

## Ⓑ① THE SUM RESPONSE BY SOURCE TERM

At the control, NUFD on, `Σ = 0.30` and `0.60`, over `ℓ = 100`–`420`.

### Ⓑ①ᵃ — the decomposition is read from the instrument, and it closes

Three runs with `SRCDEC` set — `Σ = 0`, `0.30`, `0.60` — each writing ten bilinear pair columns.
**The closure is checked before any response is read:** the ten columns must sum to the reported
`D_ℓ` to the relative tolerance the instrument prints. ⚠ If they do not, this arm reports **BLOCKED**
and no per-pair response is quoted.

### Ⓑ①ᵇ — ⛔ THE ORDER ASKS FOR A QUANTITY THE OBJECT DOES NOT HAVE, and that is stated, not worked around

The order says *"give each term's sum response"*. A term's projected contribution to `D_ℓ` **does not
exist**: `D_ℓ` is bilinear, so what exists is ten pair responses, of which four involve `isw`
(`sw*isw`, `dp*isw`, `isw*isw`, `isw*pol`). ⇒ **This revision reports the ten pairs, and answers
"which term carries it" through them**: a term is named as carrying the excess when the pairs it
appears in account for it and the pairs it does not appear in do not.

⚠ **Reachable negative, and it is a live case:** the excess may be carried by a pair whose two terms
are different — a CROSS term. Then **no single term carries it**, and that is reported as the
answer rather than resolved by assigning the cross term to one side or splitting it in half.

### Ⓑ①ᶜ — which pair or pairs carry the `100`–`212` excess, against CAMB's total

Each pair's share of the excess is measured as its contribution to the change in `D_ℓ` over that
stretch, as a fraction of the total change. Named by the largest contributor and by every
contributor above a tenth of the total, both reported.

⚠ **Registered negative:** the excess may be spread with no pair above that tenth. Then it is
reported as **not localised in the decomposition**, which would be a fact about the source split and
not a failure of the measurement.

---

## Ⓒ② THE ARM THAT DECIDES "ONE OBJECT"

The residual's measured size at `100`–`212` is put into the score as a correction to the
instrument's spectra at each sum, and the lean's limit move — `r7866`'s `−20.09` meV on the
thirty-six — is re-read. **The two outcomes are written down now, before the correction is built:**

- **THE RESIDUAL IS THE LEAN** — the corrected move falls to the reference's scale, order `0.1`–`1`
  meV, i.e. it loses at least ninety per cent of its size. Then they are one object.
- **THEY ARE TWO THINGS** — the corrected move keeps most of its size. ⇒ The low-ℓ residual and the
  lean are separate, and the order's working assumption that they are one object is retired by this
  measurement.

⛔ **The correction is a SUBTRACTION OF A MEASURED RESIDUAL AND NOTHING ELSE.** It is not fitted, not
tuned to make either outcome come out, and it is applied at the multipoles the residual was measured
at and nowhere else. ⚠ And its own failure mode is registered: if the correction's size is itself
inside CAMB's envelope there — Ⓐ⓪'s negative — then **this arm does not run**, because a correction
built from an unresolvable residual would decide "one object" on noise. It would be reported as not
runnable, with Ⓐ⓪'s verdict as the reason.

---

## Ⓓ③ THE EPOCH-DEPENDENT CLUSTERING FRACTION — CONDITIONAL, AND THE CONDITION IS NAMED NOW

The order gates this on ① naming the ISW. **So it runs only if Ⓑ①ᶜ names a pair involving `isw` as
the carrier, and not otherwise.** If it runs: the clustering matter loses `ω_ν` weighted by the
species' own non-relativistic fraction at each epoch — the same Fermi–Dirac weight the background
already carries — behind a switch, **default off, byte-identical off**, and the sum response is
checked against CAMB at `100`–`212` **before any limit is read through it**.

⚠ If Ⓑ①ᶜ does not name `isw`, this arm reports **NOT RUN, condition not met**, and the switch is not
written. An arm run anyway would be building the fix for a diagnosis the measurement declined.

---

## Ⓔ WHAT THIS REVISION DOES NOT DO

- **The two-start basin test is `cc66`'s**, as the order assigns and as this line routed it. Not
  duplicated here.
- **No limit is read except the one Ⓒ② re-reads**, and no envelope crossing appears in this record.
- **No CAMB per-term figure is quoted**, because none exists; the order asks `cc66` for it.
- **No other seat's receipt is edited.**

⌗ *This file is the registration. It is committed and pushed before the first number of this
revision is computed, and nothing in it is revised after a measurement is read.*

---

# ⚑ ADDENDUM, REGISTERED AFTER Ⓐ⓪'s VERDICT AND BEFORE THE ARM IT ADDS IS RUN

⛔ **This section was written after Ⓐ⓪ returned INSIDE and is committed and pushed before the arm
below is computed.** It is marked as an addendum rather than folded into the file above, because a
registration edited after a result is not a registration. **Nothing above is changed:** Ⓐ⓪'s
verdict stands exactly as measured, Ⓒ② stays not-runnable on it, and Ⓓ③'s condition is untouched.

## Why an arm is added at all, stated before its answer is known

The envelope test is a **proxy**, and now that it has decided something it is worth saying what it
is a proxy for. The envelope is the largest excursion of CAMB's own response over a stretch; the
departure is the largest pointwise difference between two responses over that stretch. **Those are
different quantities, and one being smaller than the other is not by itself a reason to call the
difference unreal.** What makes a pointwise difference between two oscillating curves spurious is
the two being MISREGISTERED in ℓ — a small peak-position difference, read pointwise, shows up as the
derivative times the offset.

⇒ **So the question the envelope test is standing in for is directly measurable:** does the
difference survive a change of ℓ-registration? That is this line's own standing guard — *when two
descriptions differ, first ask whether the difference survives a change of clock* — applied to the
clock that labels multipoles.

## Ⓕ④ THE SHIFT TEST, with its negatives

Over `ℓ = 100`–`420`, at `Σ = 0.30` and `0.60`, for TT and EE, fit the instrument's response to
CAMB's under exactly two parameters and nothing else:

    r_inst(ℓ)  ≈  A · r_camb(ℓ · (1 + ε))

`A` is the response's **amplitude** — how much the sum moves the spectrum. `ε` is a fractional
**ℓ-stretch** — how much the sum moves the peak positions. The two have separate physical meanings
and that is the point of using them rather than a free curve.

- **A REGISTRATION DIFFERENCE** — the residual after the best `(A, ε)` is small, `A` is near one,
  and the `ε` required is **no larger than the instrument's own acoustic-scale difference from
  CAMB**, which is a measured quantity read off the bank's recorded `l_A` and not a chosen bound.
  ⇒ The departure is a peak-registration difference, and `r7872`'s locating was wrong on a second
  count as well as the first.
- **AN AMPLITUDE DIFFERENCE** — the best fit needs `A` away from one, or the residual survives every
  `(A, ε)`. ⇒ **There is a real departure that the envelope test was too lenient to see**, and this
  line reports the order's envelope ruling as too lenient *for this purpose*, with this arm as the
  reason — routed, not asserted over the seat that ruled it.
- **NOT SEPARABLE** — `A` and `ε` trade off against each other across a wide range at comparable
  residual. ⇒ Reported as not separable on this stretch, with the range, and **no verdict is read
  through a degenerate fit.**

⚠ **The fit is over two parameters on a stretch holding dozens of multipoles, and the `ε` it needs
is checked against an independently measured number rather than eyeballed.** A fit with enough
freedom to absorb anything would decide nothing, which is why the model is two parameters and not a
spline.

⌗ *And whichever way it comes out, Ⓐ⓪'s verdict is not retracted: the departure is inside the
envelope, as measured. This arm says what being inside the envelope does and does not establish.*

# r7902 — REGISTER BEFORE THE PROFILE: does the solve's end cut a LIVE potential-decay source, or a dead one?

This seat's own item, continuing `r7900` — **not** an order. ⌗ *Committed and pushed before the profile
is run.*

`r7900` established that the instrument's line-of-sight source is integrated only to
`ETA_END = 1893.12`, which is `z = 53.545`, against `eta_0 = 14145.33` at `z = 0`, and it listed as
**not measured** where in conformal time the potential-decay term's weight actually sits. That gap
matters more than it looks:

- if the term's weight has **died** by `ETA_END`, the cut is a clean **limitation** — the instrument
  simply has no late ISW, which is what `r7900` reported;
- if the weight is **still live** there, the solve is **truncating a contribution mid-stream**, which
  is a different and worse thing: a defect in the instrument rather than a boundary of it.

`r7900` could not tell these apart, and said so. This measures it.

## ⒜ THE INSTRUMENT, WHICH ALREADY EXISTS

`SRCETA`, added at `r6959`. It writes the source's own weight across the window, band by band in `q`:

    w(eta, band) = sum_{k in band} P(k) S(eta, k)^2

with the `eta` grid saved beside it, and the same quantity per term — `w2sw`, `w2dp`, `w2isw`,
`w2pol` — so the potential-decay term's weight is read directly. ⌗ *Banding over `k` is what makes it
an envelope rather than an oscillation: at fixed `k` the source rings in `eta`, and neighbouring `k`
ring at different rates, so the band sum cancels the ringing. That is `r6959`'s construction and it is
not changed here.*

⚠ **AND THE ONE THING THIS QUANTITY IS NOT, STATED BEFORE IT IS READ.** `w2isw(eta)` is the **source's
own power** at each conformal time. It is **not** the eta-profile of what reaches multipoles
`100`–`207`, because the projection weights each `eta` through the Bessel kernel at
`x0 = eta_0 − eta`, and that weighting is not flat. ⇒ *So this revision can say whether the source is
still alive where the solve stops. It cannot say how much of the band's `D_l` comes from any stretch of
`eta`, and it will not be written as though it can.* By the standing guard, the two would be identified
by one label — "where the ISW comes from" — and the label is many-to-one on this object.

## ⒝ WHAT WILL BE MEASURED

One run of the control arm at Σ = `0`, with `SRCETA` and `SRCDEC` both on and every other environment
value exactly `r7900`'s. From the profile:

1. the ISW weight at `ETA_END` as a fraction of its own peak over the window;
2. where that peak sits, in `eta` and in redshift;
3. whether the weight is still **rising** at `ETA_END` — read as the sign of its slope over the last
   tenth of the window, not from a picture.

## ⒞ THE OUTCOMES, FIXED NOW

| | outcome | criterion |
|---|---|---|
| `Ⓨ⓵` | **THE CUT IS CLEAN** | the ISW weight at `ETA_END` is under `0.01` of its peak |
| `Ⓨ⓶` | **THE CUT TRUNCATES LIVE SOURCE** | it is at or above `0.01` of the peak |
| `Ⓨ⓷` | **AND THE SOURCE IS STILL RISING THERE** | in addition, the slope over the last tenth of the window is positive |

⚠ **`Ⓨ⓷` is not exclusive with `Ⓨ⓶` — it implies it.** Where both fire, `Ⓨ⓷` is the stronger statement
and is the headline, with `Ⓨ⓶` reported beside it. This is the same non-exclusivity discipline `r7892`,
`r7894` and `r7900` were registered under, and for the same reason: picking between them once the
numbers are visible is what registration excludes.

## ⒟ THE REGISTERED EXPECTATION

**`Ⓨ⓵`, the cut is clean.** The grounds: in matter domination the potential does not decay, so the ISW
source should fall away after the early epoch and be negligible long before `z = 53.5`. ⌗ *These are
the **same grounds** that produced `r7900`'s refuted expectation — the physics of a decaying potential
— and this is the second prediction I am making from them. If they fail again, the lesson is about the
grounds and not about this measurement, and I would rather have that on the record in advance than
discover it twice.*

⚠ **Its reachable negative:** the weight is substantial at the cut, in which case `r7900`'s "the
instrument has no late ISW" needs amending to "the instrument cuts its ISW off while it is still
contributing", and every banked spectrum in this programme inherits that.

## ⒠ THE CONTROL, AND IT GATES EVERYTHING

The instrument states that `SRCETA` and `SRCDEC` are read only inside guarded blocks and change no
reported quantity. **That claim is tested rather than taken:** this run's reported `D_l` must be
**bit-identical** to `r7900`'s banked `lcdm_S000` spectrum, which was produced with `SRCDEC` on and
`SRCETA` off.

⛔ **If the spectrum moves at all, the diagnostic is not inert, the profile describes a different run
than the one `r7900` measured, and no fraction is reported.**

## ⒡ WHAT THIS REVISION WILL NOT DO

- It will **not** extend `ETA_END`. That remains routed to `69` with a recommendation, and `r7900`'s
  refusal stands.
- It will **not** claim an eta-profile of the band's `D_l`, for the reason in ⒜.
- It will **not** re-run `r7900`'s eight points. One run at one sum answers the truncation question;
  the sum-dependence of the profile is a further question and is not opened here.
- It will **not** read a limit. `r7888`'s `193.545` meV is untouched.

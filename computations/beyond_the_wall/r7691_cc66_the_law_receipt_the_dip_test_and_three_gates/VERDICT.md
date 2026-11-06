# `r7691` (cc66) — VERDICT

Against `PREDICTION.md`, registered before any of this was computed.

## ⛔⛔ ARM ② IS FALSIFIED, AND IT IS THE FALSIFICATION THAT MATTERS

I registered, with *moderate* confidence, that the own-comb null's real-phase band response **does NOT
reproduce the `q ≈ 1.9` departure** — "that its band response has no feature there matching `+0.019`".

**It does.** At the pre-registered amplitude `0.5` the null's detrended band response carries `+0.0157`
at `q = 1.90`, **its own largest feature of the seven**, against the measurement's detrended `+0.0132`
there — `1.185` of it — and its shape correlates with the measurement's across all seven bands at
`+0.922`. At the banks' own amplitudes it is `+0.0098`, `0.741` of the measurement, correlation `+0.957`.

⌗ *The prediction was wrong in the direction that costs the most: I registered the outcome I wanted,
because a negative result licenses nothing and so cannot be misread, and the licence ceiling I fixed in
advance was the ceiling for the case I thought would not arrive.*

### AND THE NULL OF THE NULL IS THE CHECK THAT DECIDES WHAT IT IS WORTH

A shape match is worth nothing if any injection gives it, so the correlation was run at **all 24
phases**, not only the real one:

| | amplitude `0.5` | the banks' own amplitudes |
|---|---|---|
| correlation at the real phase | `+0.922` | `+0.957` |
| range across the 24 phases | `−0.971` … `+0.922` | `−0.917` … `+0.989` |
| rank of the real phase | **1 of 24** | **2 of 24** |
| fraction reproduced at `q = 1.9`, real phase | `+1.185` | `+0.741` |
| its range across the 24 phases | `−0.753` … `+1.185` | `−1.020` … `+0.857` |
| rank of the real phase | **1 of 24** | **2 of 24** |
| phases correlating above `+0.8` | 3 of 24 | 3 of 24 |

⇒ **The match is not a property of the band construction.** A randomly drawn injection phase does not
give it: the real phase is the best of the 24 at one amplitude and the second best at the other.

## ⚠ WHAT THIS LICENSES, AND THE CEILING HOLDS

The registered ceiling was **consistency IN SHAPE and never "the departure is the drift"**. The phase
scan earns one addition to it and nothing more:

> ⇒ **LICENSED:** the `q ≈ 1.9` departure is consistent in shape with the phase systematic's own
> real-phase band response, **and that consistency is specific to the measured phase rather than
> generic to the banding** — rank 1 of 24, with only 3 of 24 phases reaching it.

> ⛔ **NOT LICENSED: "the departure is the drift."** Three reasons, and the first two were registered
> before the answer was known:
> 1. **The amplitude is chosen.** The fraction reproduced at `q = 1.9` is `1.185` at the pre-registered
>    `0.5` and `0.741` at the banks' own amplitudes — a `1.6 ×` swing between two defensible choices of
>    a number I selected. **The size carries no information**; only the shape does.
> 2. **The drift was never turned off.** The scan varies the phase of an *injected* systematic. It does
>    not remove the real drift from the real spectra and watch the departure go. *That* is the
>    measurement that made the octopole's clock attribution legitimate an hour earlier in this same
>    revision, and it is a different measurement from the one ordered.
> 3. **The detrended shape is essentially one mode whose sign flips with phase** — the correlation
>    sweeps smoothly from `+0.92` to `−0.97` and back, and **ten** of the 24 phases align or
>    anti-align above `0.8` in absolute value at the pre-registered amplitude, **eight** at the banks'
>    own. *Counted in the script and not off its printed table.* It is the **sign and the maximum** that select the real
>    phase, not the existence of a matching shape. ⌗ *Stated because "rank 1 of 24" reads as stronger
>    than it is if the family it ranks within is not described.*

⛭ **AND THE MEASUREMENT THAT WOULD SETTLE IT IS NAMED RATHER THAN LEFT IMPLICIT:** a build with the
drift removed, read at the same bands. If the `q ≈ 1.9` departure goes with it, that is attribution by
the same route as the one-clock bank; if it stays, the shape match is a coincidence of one mode. ⇒ *A
bank request, not an analysis I can run — routed, not assumed.*

## ARM ① — THE ONE-CLOCK ATTRIBUTION: **CONFIRMED**

Registered: the ℓ = 3 residual swings from about `−1.0` per cent one-clock to about `+5` per cent
split-clock on both builds, the largest of the seven. Landed, with the old "cannot say" gate **replaced**
by the attribution rather than widened. Receipt: 0 FAILs, ALL CHECKS PASSED, 391s.

## ARM ③ — `_car_flat` GATED: **CONFIRMED**

`|−0.00003|` against `0.1 × |+0.00328|`. Passes by about a factor of ten, failable from both sides.
⇒ *LICENCES the landed clause's "leaving nothing" being checked.* ⛔ *Not that the envelope is
irrelevant: if flattening removes the null, the null NEEDS the envelopes — `r7689`'s correction of me,
and it stands.*

## ARM ④ — THE `> ℓ = 5` SPREAD: **CONFIRMED** at `0.63`, pinned two-sided.

## ARM ⑤ — THE HOST: **CONFIRMED**, and the price came in under the registered ceiling.

`P15_a_source_with_no_physics…` — cited at `l.2795`, so no new INDEX row, no appendix regeneration, no
PDF recompile. Registered ceiling `1.5 ×` its measured runtime; **measured 1s against a 1s baseline.**

## ⛔ ARM ⑥ IS FALSIFIED ON ONE OF ITS FOUR FIGURES, AND THE DEFECT IS MINE

Registered: `94.9` per cent, six of seven inside `0.0089`, slope ratio **`108.9`** per cent, spread
`0.00059`. Three reproduce exactly. **The slope ratio is `108.4`, not `108.9`.** My `r7689` figure
divided the law's slope by the *published rounded* `0.0103` instead of the measured `0.010344`:
`0.011215/0.0103 = 108.89` against `0.011215/0.010344 = 108.43`.

⌗ *This is the same defect class as the "factor of `75`" I caught in the band-RMS docstring at `r7685`
— **a derived digit computed from a rounded input** — arriving two revisions later in a figure of my
own, past my own commitment ⑦ check, and already quoted back to me in `r7691`'s order text. **It is
routed as a correction and not quietly repinned**, because 69 has it in prose.*

## FAILABILITY OF THE SIX ASSERTIONS ARM ⑤ ADDED — every one broken, each leg verified applied first

| perturbation | assertions that FAIL |
|---|---|
| the law's acceptance scaled by `1.01` | **4** of 6 |
| both arms put on one comb | **3** |
| the own-comb module path broken | **1** |
| the measured spectrum scaled by `1.01` | **0** |

⚠ The fourth leg's `0` is **informative and not a hole**: the statistic is a *relative* oscillation
ratio, so a constant rescaling cancels in numerator and denominator. *Same class as `r7687`'s
mis-aimed leg B — except that there the zero was a mis-aimed probe and here it is the statistic's own
invariance, which is why the distinction is stated rather than the leg dropped.* Each leg asserted the
patch had applied before running, and read the receipt's **own** failure token — the three false
negatives of `r7687`.

## THE DISTINCTION REGISTERED IN ADVANCE, AND IT HELD

`l.2795`'s existing clause is **PER-ARM** — `A_ℓ` against each arm's own measured comb amplitude, to
within ten per cent, worst `6.7`. **Everything above is an ARM/CONTROL RATIO** — the law's
`A_cr/A_lcdm` against the own-comb retention ratio. *Two claims about two different quantities. The
`94.9` per cent does not confirm "within ten per cent", and the drafted sentences say so in the paper
and not only here.* ⇒ It is stated in the receipt file itself, in the monotonicity gate's own text,
so the licence travels with the computation and not only with the route.

## PRICE OF HOSTING THE DIP TEST, IF 69 WANTS IT CITEABLE

The natural host is `P15_the_phase_systematic…` — it already builds these banks and imports the module.
Measured: the dip test is **37s** standalone; that receipt is **119s** against a **declared 900s**. So
`119 → ~156s`, **17 per cent of its own declaration and inside the global 600s cap**. ⌗ *Priced before
proposing it, per commitment ⑥, and not pushed: the order asked for the measurement, not the receipt.*

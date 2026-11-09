# `r7713+cc66` — THE DENSE READING, AGAINST THE RULE REGISTERED BEFORE IT

**All four combinations exist on every integer `l` with `q ∈ [0.80, 3.10]`** — `693` on the control
kernel, `697` on the arm's — and the reading was made by `analyse.py`, committed and pushed while one of
the four existed and the other three did not.

⇒ **The registered verdict is ⒜: the discriminant is NOT RESOLVED.** But three things in the way it fails
are worth more than the verdict, and one of them changes what the sparse reading meant.

---

## ⛭ ⓵ THE CONTROL HOLDS — the kernel swap is live on the dense grid

| source arm | median `|`move`|` | max |
|---|---|---|
| control | `6.0234` % | `17.5167` % |
| arm | `6.3223` % | `20.9049` % |

⇒ Swapping the kernel on a fixed source moves the pseudo-spectrum, so the cross readings below are
readings of something. *`r7703`'s leg-B case — an inert perturbation — does not apply.*

## ⛔⛔ ⓶ AND THE HEADLINE: **BOTH SINGLE-DIFFERENCE RATIOS REVERSED SIGN BETWEEN THE TWO SAMPLINGS**

`r7711` read the two differences on the bank's own `87` `l`. `r7713` reads them on all of them. **The signs
are opposite.**

| | at `87` `l` (`r7711`) | at `693`/`697` `l` (here, widest window) |
|---|---|---|
| own × own | `+0.0232` | `+0.0261` |
| **kernel alone** | **`+0.0482`** | **`−0.0286`** |
| **source alone** | **`−0.0277`** | **`+0.0481`** |

⛔ **The sparse pattern pointed at "the projection creates it". The dense pattern points, if anything, the
other way** — the source difference now carries the measured sign and is *larger* than own × own, while
the kernel difference opposes it.

⇒ **This is the finding, and it is a finding about the SPARSE READING: its sign was not stable under
sampling.** *Which is exactly what `r7713`'s registration said the thresholds were written in advance
for — "at low significance the pattern ALREADY looks like creates". It looked like it, and it was not it.*
⚠ **And neither sign is resolved, so the reversal licenses no verdict in the other direction either.**

## ⚠ ⓷ THE WELL-POSEDNESS TEST DID NOT REFUSE — BY `0.8` OF A PERCENTAGE POINT, AND THAT IS NOT A PASS

The registered refusal was: the interaction residual's own step is at least `2` sd **and** at least `50` %
of the own × own step.

| | |
|---|---|
| residual step | `0.014870` |
| its significance | `2.90` / `3.20` / `2.88` sd across the three widths — **over the `2` sd arm** |
| as a fraction of the own × own step | **`49.2` %** against a registered `50` % |

⛔ **So it passes on the letter of a threshold I set myself, by a margin of `0.8` of a percentage point.**
It is recorded here as *"not refused by this test"* and must not be read as *"well posed"*: the source and
kernel differences interact at essentially half the scale of the thing they would partition. ⌗ *In step
space, for comparability with `r7711`'s own quoted numbers, the gap runs `17.4`–`25.2` % of own × own
across the three widths; the registered test is the per-`l` log residual, and it is the one that decides.*

⇒ `analyse.py` also reports, correctly, that **own × own is itself unresolved, so the partition's status is
NOT ESTABLISHED rather than well posed** — there is no resolved step here to partition.

## ⛭ ⓸ THE AGREEMENT GATE PASSES ON ALL THREE

Same sign at every half-width, magnitudes within the registered factor of two, for all three ratios. ⇒
`r7711`'s first obstruction — a plateau that exists at one width and not another — **does not bite here.**

## ⚠ ⓹ AND THE REGISTERED GUARD FIRES: MY GRID ESTIMATE WAS WRONG

own × own reaches **`3.51` sd** at the widest registered window against a registered target of `5`.
`r7713+cc66.0` registered what to do about that in advance: *"If the dense grid does not take it there,
then my `1/√n` scaling was wrong and that is a finding about my estimate, not about the physics."*

⇒ **It was wrong.** `549` `l` was my estimate of what `5` sd needs; `693` of them deliver `3.51`. ⌗ *And
`r7713+cc66.10` says why `1/√n` was the wrong model: the slide's denominator is the variance WITHIN each
band group, and a gradient-shaped step traverses each group, so the effect enters its own error bar.
Measured there: cutting the scatter fivefold bought `0.36` sd. The significance does not scale with the
sample at all beyond a point — it saturates.*

## ⛔ WHAT THE VERDICT IS, AND THE ONE WORD IN IT I WILL NOT USE

**⒜ — the discriminant is not resolved.** Both single differences are under `2` sd (`1.47` and `1.92` at
the widest window), so neither row that names a mechanism can be claimed.

⚠ **But `⒜`'s registered wording says "exhausted rather than under-sampled", and I am not using
"exhausted".** Under-sampling is certainly dead — *every integer `l` in the band is in this reading, which
is precisely what this revision was ordered to do, and the sampling excuse is gone for good.* What has
replaced it is not exhaustion of the physics but **a ceiling in the statistic**: by `r7713+cc66.10`'s
measurement the estimator saturates near `4.2` sd for an effect of this shape, so a `5` sd bar may be
unreachable on this construction whatever the data says. ⇒ **Whether that ends the pseudo-spectrum route
or merely ends THIS estimator's use of it is `69`'s ruling, with four options and a recommendation already
routed, and it is not absorbed here.**

---

## WHAT IS NOT CLAIMED

- **No attribution.** No build removes a step the arms share; unchanged from the registration.
- **The acceptance kernel is not the exact transfer.** This settles something about the pseudo-spectrum
  built from the banked geometry, not about the full projection.
- **No significance is combined across the three ratios.** They share the denominator
  `Pseudo(lcdm,lcdm)`, so their scatters are correlated and consistent signs are not three
  confirmations. The run says so in its own output.
- **The sign reversal is not a measurement of the mechanism.** It is a measurement of the sparse
  reading's stability, and that is all it is offered as.

## PROVENANCE

| | |
|---|---|
| combination 1 | computed in this container, banked at `r7713+cc66.8` |
| combinations 2–4 | three CI runners, `r7715`'s ruling, matrix run `42522767544` |
| each runner's control | recomputed the banked combination's first block and required `≤1e-12`; **the one log read directly shows `0.000e+00`, byte-identical** |
| why all three controls passed | the ref-push step runs only `if: success()`, AFTER the control step, and all three refs exist — so a refused control could not have produced a ref |
| compute | `1609` s on the runner read, against about `1.05` h estimated per combination in the container; the runners were faster |
| the reading itself | `0.7` s |

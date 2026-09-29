# `r7017 → cc66.60` — PRE-REGISTRATION, WRITTEN BEFORE ANY OF IT WAS COMPUTED

⛔ **Nothing below has been measured.** *Committed as its own commit before `amplitude_or_phase.py` is run.
⓵'s table leads with **phase**, because that is the outcome that reframes the row rather than the one that
keeps it — the order says so and I agree.*

---

## ⓵ AMPLITUDE OR PHASE — AND THE ALGEBRA THAT SEPARATES THEM, NAMED BEFORE USE

*Write each arm's contrast as one oscillation at the comb period: $o_c = A_c\cos\psi$ and
$o_a = A_a\cos(\psi + \Delta)$, with $\psi$ the control's own phase, $r = A_a/A_c$ the **relative amplitude**
and $\Delta$ the **relative phase**. Then*

$$o_a - o_c = A_c\big[(r\cos\Delta - 1)\cos\psi - r\sin\Delta\,\sin\psi\big]
\quad\Longrightarrow\quad
\operatorname{std}(o_a-o_c) = \tfrac{A_c}{\sqrt2}\sqrt{\,r^2 - 2r\cos\Delta + 1\,}.$$

⇒ *** SO THE SURVIVING STATISTIC HAS EXACTLY TWO INPUTS AND THEY SEPARATE IN CLOSED FORM: ***

| limit | what it is | the quantity |
|---|---|---|
| $\Delta = 0$ | **amplitude only**, phase held fixed | $\dfrac{A_c}{\sqrt2}\,\lvert r-1\rvert$ |
| $r = 1$ | **phase only**, amplitude held fixed | $\dfrac{A_c}{\sqrt2}\,2\lvert\sin(\Delta/2)\rvert$ |

**HOW $r$ AND $\Delta$ ARE MEASURED.** *`cc66.53`'s held-period estimator, unchanged: a local fit of a
baseline polynomial plus one cos/sin pair at the comb period, giving an amplitude and a phase per arm at each
$q$; $r$ is their ratio and $\Delta$ their difference.*

**THE GATE THIS DECOMPOSITION MUST PASS BEFORE ANY OF IT IS READ.** *The closed form must reproduce the
**directly measured** $\operatorname{std}(o_a-o_c)$ band by band. ⛔ *If it does not, the two-input model is
wrong for this spectrum and nothing below is licensed* — that check comes first and is reported either way.*

**THE OUTCOMES, THE REFRAMING ONE FIRST.**

| outcome | what it means | what it does to the row |
|---|---|---|
| ⛭⛭ **PHASE** — the phase-only term carries the band-1 step and the amplitude-only term does not | **the first acoustic cycle is displaced, not weakened**, in this cosmology relative to the control | ***the row is reframed***: this is not a contrast finding at all, `P15` carries it somewhere else, and every sentence about "the contrast excess's step" is about the wrong object |
| ✔ **AMPLITUDE** — the amplitude-only term carries it and the phase-only term does not | the step is what the row has been calling it | the row continues, and the estimator is simply the clean way to read it |
| ⚠ **BOTH** — each carries a step of comparable size | two features at one scale, or one feature with two signatures | the row must say which it is before quoting either, and that is a further revision |
| ⛔ **INSEPARABLE** — the fit cannot resolve $r$ from $\Delta$ at band 1 | *an inseparability is a finding here, not a gap* | ⇒ **then this revision's job is to say exactly what would separate them**, and to say it in terms of a measurement that could be made |

⚠ ***NO PREDICTION IS OFFERED.*** *The phase row is tabled first because it costs the row most, not because I
expect it.*

---

## ⓶ RE-SCORING THE CANDIDATES WHERE THE CR-SPECIFIC TENTH ACTUALLY LIVES

*Every share in the row is measured on the ratio-of-contrasts route, where nine tenths of the feature enters
and cancels. ⇒ *So each channel is re-read as $\operatorname{std}(o_{\rm knob} - o_{\rm lcdm})$ — its **own**
differential against the same control — and its band-1 departure taken against its own bands 2–7 trend, on the
same four bases with none chosen.*

⌗ **The denominator changes and that is the point, so it is named before use:** *a channel's share is now its
departure over the **arm's differential** departure, not over the excess's. **The two fifths is not expected to
survive**, and a large move is the finding rather than a failure.*

| outcome | what it means |
|---|---|
| the shares move a long way | *a channel that accounts for two fifths of a mostly-shared quantity is not the channel that accounts for the CR-specific part* — and the row's candidate accounting has been scored against the wrong object |
| the shares are about the same | the ratio-of-contrasts route was not misleading after all, which is worth knowing and is **not** what I would bet on |
| a channel changes SIGN between the two routes | the strongest version of the first row: the channel opposes on the part that is CR's while helping on the part that is shared |

---

## ⓷ DOES THE STEP COMPOSE THE WAY THE CONTRAST DOES?

*`cc66.49` measured the composition of the window weighting and the term mix on the **contrast response** and
found it **multiplicative** — the product in 7 of 7 bands, the sum in 0 of 7. ⇒ *The question is whether the
**step** composes by that same rule.*

**NAMED BEFORE USE:** *the two singles' band-1 departures are combined under each of **product, sum and
quadrature**, and each prediction is compared with the **joint bank's own measured** departure — the pair
composed in one spectrum at the sizes their own profiles solve. No rule is assumed; all three are reported,
as the bases are.*

| outcome | what it means |
|---|---|
| **the same rule** | the pair's share stops being a measurement and becomes a **prediction**, and the remainder is then a statement about what is **missing** rather than about how two knobs add |
| ⛭ **a different rule** | ***a new property of the step, and worth more than the share*** — the step would compose unlike the contrast it is a feature of |
| ⚠ **no rule fits** | reported as that, with the three residuals, and not rounded to the nearest |

---

## ⓸ AND WHAT IS NOT DONE

⛔ *No envelope chosen, no trend basis chosen, no abscissa chosen. No new candidate. **No mechanism proposed** —
and that holds with particular force on ⓵: if the answer is phase, "the first acoustic cycle is displaced" is a
**signature**, not an explanation, and I will not say what displaces it. No corpus edits. Nothing on the quantum
sector or the reproducibility rows.*

⚠ **AND THE HAZARD ⓵ CARRIES, NAMED BEFORE IT IS MET.** *A local cos/sin fit returns amplitude and phase that
**trade off against each other** when the window is short or the baseline is curved — a small phase error
appears as an amplitude error and the reverse. ⇒ *So the separation is reported at more than one window
half-width, and if $r$ and $\Delta$ move together across widths in the way that trade-off predicts, **that is
the inseparable row and it will be called so** rather than read as a result.*

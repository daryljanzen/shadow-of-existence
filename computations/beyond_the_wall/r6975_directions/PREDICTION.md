# r6975 ⓷ — WHAT THE TERM-MIX SWAP IS PREDICTED TO DO, WRITTEN BEFORE IT RUNS

*Committed ahead of the runs, as `r6959`'s was. ⛭ **And written to 66's own correction of my `cc66.47`
pre-registration:** the tolerance is put on the quantity that would move, not on the quantity it is
derived from — a condition on $f$ cannot fire on a response in $f-1$.*

## THE OPERATION, AND WHY IT NEEDS NO NEW SWITCH

`cc66.47` measured the arm holding **more of its window's power in the monopole in every band** and
correspondingly less in the Doppler. The Doppler term is already a wired knob on the reporting path:
`DPSRC` scales $(1/k^{2})\,\partial_\eta[g\,\theta_b]$ and nothing else, wired to the hierarchy path at
`r6889+cc66.36`. Scaling it by $c$ scales its power by $c^{2}$, so the $c$ that gives the control the
arm's monopole fraction is fixed by the `SRCETA` profiles and by nothing else.

⛭⛭ **AND THE FIRST RESULT IS THAT ONE CONSTANT DOES IT.** Solved band by band from the measured
fractions:

| $q$ | $1.20$ | $1.90$ | $2.60$ | $3.30$ | $4.00$ | $4.70$ | $5.40$ |
|---|---|---|---|---|---|---|---|
| monopole fraction, control → arm | $0.1837\to0.2171$ | $0.3417\to0.4100$ | $0.3739\to0.4323$ | $0.4432\to0.5057$ | $0.5994\to0.6597$ | $0.5768\to0.6408$ | $0.5320\to0.5875$ |
| **`DPSRC` that matches it** | $0.8974$ | $0.8600$ | $0.8824$ | $0.8791$ | $0.8753$ | $0.8708$ | $0.8908$ |

⇒ ***The seven values span $0.860$ to $0.897$ — a two per cent spread about $0.879$.*** *So the arm's
term-mix difference is, to that precision, **a single scalar on the Doppler term** and not a
$q$-dependent reshaping. That is a measurement, not a modelling choice, and it is what makes the swap a
one-parameter operation.*

## THE RUNS

`DPSRC = 0.8794` on the control — the band-mean, the arm-matching value — and `DPSRC = 0.60` as the
second coefficient, so the response can be calibrated and inverted exactly as `cc66.47`'s taper response
was. Both at `LSTEP=1 LMAXL=2000`, `r6941_fine_*`'s own grid.

## WHAT IS PREDICTED, IN ADVANCE

* **P1 — SIGN.** Reducing the Doppler, which is a quarter period out of phase with the monopole, removes
  power that fills the oscillation in rather than deepening it. ⇒ **The control's contrast RISES.**
* **P2 — SHAPE, AND THIS IS THE ONE THAT MATTERS.** The matching $c$ is $q$-independent to two per cent.
  ⇒ ***So the response must be $q$-independent too, to within that:*** a straight-line fit of
  $\ln(\text{response})$ against $q^{2}$ must have an intercept that dominates its slope term across the
  band. **That is the opposite signature from the window channel**, whose response is a characteristic
  function and is identically $1$ at $q=0$ — and it is exactly the signature R1's non-zero offset of
  $1.0400$ needs.
* **P3 — SIZE.** Left to the two-coefficient inversion, because no closed form survives the $k$-sum: at a
  single $k$ the monopole and Doppler are exactly in quadrature and $|T|^{2}$'s oscillation amplitude
  equals its mean identically, so the contrast's dependence on the mix is entirely a property of the sum
  over $k$ and the kernel. ⌗ *Stating that here rather than inventing a bracket is the direct application
  of 66's correction: I do not have a quantity to put a tolerance on, so I do not pretend to one.*

## WHAT WOULD REFUTE IT — and the tolerances are on the quantities that move

* **T1 — SIGN.** The control's contrast falls, or does not move by more than the statistic's own
  resolution. Refuted outright.
* **T2 — SHAPE.** The fitted $q^{2}$ slope carries more of the response across the band than the
  intercept does — i.e. the response looks like a smearing after all. ⇒ *Then the term mix is not the
  source of the $q$-independent offset and ⓷ closes negatively.*
* **T3 — THE SYMMETRY, WHICH IS THE WHOLE POINT OF THE ROW NOW.** `cc66.46` measured the excess symmetric
  about the envelope; `cc66.47` measured the window channel peak-weighted $81$ against $14$ per cent.
  ⇒ ***If the term-mix swap is also peak-weighted by more than a factor of two, it cannot be the
  symmetric remainder either***, and the row's object narrows again rather than closing. **Refuted as the
  symmetric part if the height share exceeds twice the depth share.**
* **T4 — THE COMB.** Standing, from `r6959` ⓵ᶜ: if it closes contrast but moves the four peak positions
  past the sky's own locating widths ($1.00/1.20/1.60/2.36$), it is not a mechanism for this row.
* **T5 — THE NULL.** `DPSRC=1` is the default and must return the banked control bit-identically.

⌗ **Path provenance.** Every number is the **hierarchy** path (`LOS=1 HIER=1`). `DPSRC` reaches all three
paths but only the hierarchy one is read here. ⌗ **No detection language.**

---

# SUPPLEMENT — ⓵'s DECOMPOSITION SHARPENS T3, AND THIS IS STILL BEFORE THE RUNS LAND

*Written after the file above and **before any `DPSRC` slice finished**, which is checkable in the
history. ⓵ is analysis on banks already in hand and it changes what T3 should be looking for, so the
sharper target goes in now rather than being applied afterwards.*

**⓵'s result.** Dividing the measured excess by what the window channel actually delivers at the arm's
own size leaves a remainder which is $1.0184$ at $q=0$ — **$46$ per cent of the offset R1 fired on** —
and which carries $123$ per cent of the measured $q^{2}$ slope. ⇒ *So the remainder is where the growth
with wavenumber lives, and about half the long-wavelength offset.*

⛭⛭ **AND THE REMAINDER IS TROUGH-WEIGHTED, WHICH IS THE OPPOSITE OF THE CHANNEL IT WAS LEFT BY.**
On the anchored reading: the whole excess is $+5.66$ per cent on heights against $+2.58$ on depths
(ratio $2.20$); the window channel delivers $+4.59$ against $+0.37$ (ratio $12.44$); **the remainder is
$+1.07$ against $+2.21$ — a ratio of $0.49$.**

⇒ ***So T3's target is not "symmetric". It is trough-weighted by about two***, and the term-mix swap has
a two-sided bar rather than a one-sided one:

* **T3′ — THE REMAINDER'S OWN WEIGHTING.** If the `DPSRC` swap is to be the remainder, its anchored
  height-to-depth ratio must land near $0.5$ and on the trough side of $1$. ⛔ ***Refuted as the remainder
  if it comes out peak-weighted (ratio above $1$), and refuted equally if it is flat (ratio within ten
  per cent of $1$), because the remainder is not.***
* ⌗ **And there is a reason to expect the trough side, stated before the run:** the Doppler is a quarter
  period out of phase with the monopole, so it *fills* the oscillation rather than deepening it, and
  removing it should take more out of the troughs than it adds to the peaks. **If that is right the swap
  lands near $0.49$ by its own physics and not by fitting.**

⚠ **AND ONE THING ⓵ TURNED UP THAT IS NOT A PREDICTION BUT A CORRECTION OF FRAMING, RECORDED HERE SO IT
IS NOT MISTAKEN FOR A FINDING OF THE RUN.** *`cc66.46`'s "symmetric about the envelope" is the band
variance split's statement — $1.0668$ peak side against $1.0561$ trough side. On the **anchored** heights
and depths the same excess is peak-weighted $2.20$, because the control's depths are more than twice its
heights and equal percentage changes are not equal variance shares.* ⇒ **Two statistics, one of them
symmetric and one of them not, on the same excess** — the standing guard, firing again. *Everything in
`cc66.47` compared SHARES of the arm's own excess and so is unaffected; but the word "symmetric" belongs
to the variance split and I will say which statistic every weighting number is on.*

---

# SECOND SUPPLEMENT — ⓶'s ARITHMETIC RETRACTS THE FIRST SUPPLEMENT'S FRAMING, AND RESETS T3′'s REFERENCE

*⓶ is arithmetic on the control's own banked spectrum, done before any `DPSRC` slice finished. It changes
the number T3′ must be measured against, so it goes in now.*

**What a five per cent operation of each named class reads as, on the anchored statistic** — computed by
applying the operation to the control's own binned spectrum and re-running the same envelope and the same
anchored locator:

| class | operation on $D_\ell$ | heights | depths | **ratio** |
|---|---|---|---|---|
| **A amplitude** | the oscillation scaled about the envelope | $+7.53\%$ | $+3.84\%$ | **$1.95$** |
| **B envelope** | the smooth part scaled at fixed oscillation | $+7.93\%$ | $+4.05\%$ | **$1.96$** |
| **C loading** | a smooth positive component removed | $+2.21\%$ | $+3.51\%$ | **$0.60$–$0.67$** |
| **E smearing** | a Gaussian in $\ell$ of nine multipoles | $+5.55\%$ | $-1.05\%$ | **$-5.28$** |

⛔ ***So the baseline for a SYMMETRIC operation on this statistic is not $1$ — it is $1.95$***, stable
across operation sizes, because the running-mean envelope is recomputed and shifts $o$ upward by a
constant, which adds to the heights and subtracts from the deeper troughs.

⚠ **THAT RETRACTS THE FIRST SUPPLEMENT'S CLOSING NOTE.** *I wrote there that the anchored statistic and
the variance split disagree, the excess being "peak-weighted $2.20$" on one and symmetric on the other.
**They do not disagree**: $2.20$ against a symmetric baseline of $1.95$ is agreement to thirteen per cent,
so the anchored reading confirms `cc66.46`'s variance split rather than contradicting it.* ⇒ **The
statistic has a baseline and I compared to $1$ instead of computing it. The guard about keeping two
statistics apart was right; my application of it was not.**

**AND T3′'s REFERENCE MOVES WITH IT.** *Measured against $1.95$, not against $1$:*

* the **whole excess**, $2.20$ → within thirteen per cent of a pure amplitude change;
* the **window channel**, $12.44$ → strongly peak-weighted, on the smearing side;
* the **remainder**, $0.49$ → strongly trough-weighted, **and the only named class on that side of
  $1.95$ is the loading class at $0.60$–$0.67$.**

⇒ ***So ⓶'s answer is that the remainder is in the loading class — a smooth additive component removed —
and reducing the Doppler is exactly that operation.*** **T3′ restated: the `DPSRC` swap should read
between about $0.5$ and $0.7$, trough-weighted, well below the symmetric baseline of $1.95$.** ⛔ *Refuted
as the remainder if it reads at or above $1.95$ (symmetric or peak-weighted); refuted equally if it reads
far below $0.4$, which no named class produces.*

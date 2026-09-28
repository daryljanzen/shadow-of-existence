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

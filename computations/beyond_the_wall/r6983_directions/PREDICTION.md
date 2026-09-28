# r6983 — WHAT EACH COMPOSITION RULE PREDICTS, ON ALL THREE AXES, BEFORE THE JOINT RUN

*Committed before the joint run. ⛭ **Every reading below is against the anchored statistic's own symmetric
baseline of $1.95$**, per the order's ⚠, and the tolerances are on the quantities that would move.*

## THE OPERATION

Both knobs together at their own measured sizes, on the control: `SRCTAPER=1.100877765e-4
SRCTAPERS0=145.3465211 SRCTAPERNORM=1` (the window's spread matched to the arm's, weight-preserving)
**and** `DPSRC=0.8794` (the arm's monopole fraction imposed). `LSTEP=1 LMAXL=2000`, `r6941_fine_*`'s own
grid. *Both knobs are already wired and both individual responses are banked, so the joint run adds one
spectrum and no new machinery.*

## ⓵ WHAT THE THREE RULES PREDICT FOR THE SIZE

From the banked individual responses $R_w$ (`r6959_nswap_lcdm`) and $R_m$ (`r6975_mix_lcdm`):

| $q$ | $1.20$ | $1.90$ | $2.60$ | $3.30$ | $4.00$ | $4.70$ | $5.40$ |
|---|---|---|---|---|---|---|---|
| window $R_w$ | $1.0268$ | $1.0183$ | $1.0194$ | $1.0118$ | $1.0153$ | $1.0142$ | $1.0149$ |
| term mix $R_m$ | $1.0595$ | $1.1088$ | $1.0780$ | $1.0821$ | $1.0905$ | $1.0724$ | $1.0911$ |
| **product** | $1.0880$ | $1.1291$ | $1.0989$ | $1.0949$ | $1.1072$ | $1.0877$ | $1.1073$ |
| **sum** | $1.0864$ | $1.1271$ | $1.0974$ | $1.0939$ | $1.1058$ | $1.0866$ | $1.1059$ |
| **quadrature** | $1.0653$ | $1.1103$ | $1.0804$ | $1.0830$ | $1.0918$ | $1.0738$ | $1.0923$ |

⛔ **AND THE FIRST THING TO SAY IS WHAT THIS TEST CANNOT DO.** *The product and the sum differ only by the
cross term $(R_w-1)(R_m-1)$, which is at most $0.0016$ — a sixth of a per cent, far below what the band
statistic resolves.* ⇒ ***So this measurement can separate QUADRATURE from {product, sum} and it cannot
separate the product from the sum.*** *Saying so in advance is the point: a bar that cannot distinguish two
rules must be declared unable to, or the one that happens to be closer will be reported as the winner.*

* **T-SIZE.** The joint response lands within $0.005$ of the product/sum pair, or within $0.005$ of
  quadrature, in at least five of the seven bands. ⛔ *If it lands outside both, no named rule holds and
  the departure is the finding — to be reported as a shape in $q$, not as a shortfall in size.*

## ⓶ AND ON THE OTHER TWO AXES, WHICH IS WHERE THE LAST TWO REVISIONS EARNED THEIR RESULTS

* **T-WEIGHT.** The anchored height and depth *changes* add for small operations, so an additive or
  multiplicative composition predicts
  $$\text{ratio}_{\rm joint}=\frac{\Delta h_w+\Delta h_m}{\Delta t_w+\Delta t_m}
   =\frac{4.59+13.16}{0.37+5.90}=\mathbf{2.83},$$
  ***peak-weighted, well above the symmetric baseline of $1.95$***. ⛔ *Refuted as an additive/multiplicative
  composition if the joint reads below $2.2$ or above $3.6$ — a fifth either side. Quadrature makes no
  prediction on this axis at all, which is itself a discriminator: **a rule that cannot predict the
  weighting is weaker than one that can, even if it fits the size better.***
* **T-COMB.** The two channels move $\ell_1$ in *opposite* directions — the window $+2.83$ multipoles, the
  term mix $-1.04$ — so an additive composition predicts $+1.79$, inside the sky's own locating width of
  $1.00$... **it is not**: $1.79$ is outside it. ⇒ *Predicted $\ell_1$ shift $+1.79$, still outside the
  sky's width; refuted as additive if the joint moves $\ell_1$ by less than $+1.0$ or more than $+2.6$.*
  ⌗ *This axis is the cheapest sign that the channels interact, because a cancellation here is visible at a
  tenth of the size the contrast needs.*

## ⓷ THE $q$-INDEPENDENCE, WHICH HAS NO FREE CONSTANT IN IT

*The term mix's response is $q$-independent with intercept $1.0805$; the window's is $1.0213$ with a slope
of $-3\times10^{-4}$.* ⇒ ***So a multiplicative composition predicts a joint long-wavelength intercept of
$1.0213\times1.0805=1.1035$ exactly, with nothing fitted.*** The sum predicts $1.1019$ and quadrature
$1.0839$.

* **T-INTERCEPT.** The joint response's fitted intercept against $q^{2}$ lands within $0.005$ of $1.1035$
  (product), $1.1019$ (sum) or $1.0839$ (quadrature). ⌗ *And the number to report it beside is the
  **measured excess's own intercept, $1.0400$** — the offset R1 fired on. Whatever the rule, the joint
  intercept is about two and a half times that offset, which is the arithmetic that says the two channels
  at their measured sizes are too much and not too little.*

⌗ **Path provenance.** Hierarchy path (`LOS=1 HIER=1`) throughout; `_project` is where both knobs live.
⌗ **No detection language.** ⌗ **No third channel** — the order forbids one and none is added.

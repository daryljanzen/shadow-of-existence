---
name: PO13_WORKING_STATE
description: THE ACOUSTIC-PHASE OFFSET — the worked state of PO-13, held OUTSIDE the corpus. Not a paper, not a register row, not a route into either. Read before touching P15's acoustic sections.
status: WORKING DOCUMENT — deliberately not a paper
---

# THE ACOUSTIC-PHASE OFFSET — WORKING STATE

⛭ **WHY THIS IS NOT IN A PAPER.**  *The corpus's papers hold ONE state, and a question still being
worked is not a state.*  Writing this into `P15` while it moves is how a narrative mess is made: each
revision leaves a sediment of the last, and the paper stops saying one thing.  **This document is the
place the work moves; the papers are where it lands when it stops moving.**  Nothing here is routed
into a paper without a separate decision.

---

## THE QUESTION

`PO-13` asks: the construction reproduces the acoustic scale, the peak spacing, the damping physics and
the height pattern, and puts the first-peak phase intercept some way from the sky.  **Is that a defect
of the seam treatment, of the transfer, or of the geometry the transfer runs on?**

---

## THE ANSWER AS IT NOW STANDS

⇒⇒ ***NONE OF THE THREE.  The offset is a consequence of the radiation-free rate, and the mechanism
behind it is the construction's own, measured on the construction's own instrument.  Every handle that
could move it has been tried and none reaches the sky.***

*Stated as a claim about the programme rather than the instrument, which is why it is held here pending
a decision to state it at all.*

---

## WHAT IS MEASURED, AND WHERE

| finding | value | revision |
| --- | --- | --- |
| the driving implementation is SOUND | on ΛCDM it puts the first peak at $\ell=220$ against the sky's $220.6$, supplying $1.01$ of what is needed | r3335 |
| the first-peak mode is ALREADY SUB-HORIZON at the onset | $k/\mathcal H = 1.53$; its potential decays $46.5\%$ before recombination | r3351 |
| — and that is `P15`'s OWN stated hypothesis | *"modes begin already sub-horizon … so the potential does work on them at once"* | r3351 |
| the datum is imposed at a FITTED redshift | `Z_START` is solved so $\ell_A$ hits `LATARG`; the control's is fixed at $z=3\times10^7$ | r3361, r3365 |
| the first-peak deficit is NOT an artefact of the pin | across `LATARG` $260\to340$ — a $31\%$ swing — $\ell_1$ moves only $164\to176$ | r3365 |
| the pin sets the ASYMPTOTIC spacing and leaves the FIRST GAP alone | later gaps reach $264$ against the sky's $272$; the first stays $248$ against $317$ | r3365 |

### Eliminated by measurement, one computation each

* **the damping scale** — `DAMPX` $0.25$–$4$: $P_1/P_3$ matches the sky at $4$ while $P_1/P_2$ is still
  $45\%$ low, so no coefficient fixes both.  *That is the instrument's own criterion for "the residual
  is the SHAPE of the envelope, not its scale."*  (r3323)
* **the photon hierarchy** — `HIER=1` gives $P_1/P_2 = 0.889$, worse than $0.965$.  (r3323)
* **the polarisation source** — `PISRC=0` gives $0.903$: a $1.5\%$ effect on a $60\%$ error.  (r3323)
* **the baryon loading** — $R = 0.622$ at recombination, the standard value.  (r3323)
* **the expansion rate** — CR's $\mathcal H$ is $0.62$–$0.93$ of the control's, and $\mathcal H$ enters
  $Q$ LINEARLY, so a lower rate would UNDER-drive.  *It goes the wrong way.*  (r3337)
* **the closed-$S^3$ ladder** — reaching the first peak would need a transfer drawing power over a
  factor of eight in $k$.  (`L-274`, verified r3313)
* **the accumulated phase $\varphi(k)$** — spans $2.888\pi$, so $\cos\varphi$ flips sign twice inside
  the acoustic band and the second peak is DESTROYED rather than moved.  (r3369)
* **any COMMON phase** — the first two features sit at $172$–$188$ and $380$–$396$ and $\varphi$ hands
  leadership between them; **the sky's $221$ falls in a gap the construction does not populate**.
  (r3371)

---

## ⛭ THE TWO THINGS THAT CAME OUT BETTER THAN EXPECTED

⓵ **`P15`'s frozen-mode condition is SUPPORTED BY A SECOND, INDEPENDENT ARGUMENT.**  The paper derives
$\sin\varphi = 0$ from what crosses the branch point.  *The refutation of $\varphi(k)$ supplies the same
conclusion from the sky's own comb*: if modes arrived carrying individually accumulated phases the comb
would show polarity flips, and it does not.  **A common phase is required for a regular comb to exist at
all.**  (r3369)

⓶ **THE OFFSET AND THE HUBBLE RESOLUTION ARE ONE FACT.**  The standard driving shift is universal
*because* every mode crosses during radiation domination and acquires the same shift.  **A
radiation-free rate has no such crossing.**  So the same rate that dissolves the tension, carries the
BAO $\chi^2$ flat in $H_0$ and returns the abundances is the rate that puts the first peak where it is.
*The construction cannot keep the first while disowning the second.*

---

## ⛔ WHAT IS OPEN, AND WHAT IS NOT KNOWN

* **What the construction says the datum should be AT THE ONSET.**  Checked across all three source
  classes and **nothing settles it**: `P15` argues the condition at the branch point and applies it at
  the onset without stating what happens between; 638 receipts carry nothing on the placement; and
  **the thesis has no perturbation sector at all** — `perturbation` ×1, `initial condition` ×0.
  *Genuinely open rather than unconsulted.*  (r3363)
* **The gap is SPECIFIC.**  $221$ sits between $188$ and $380$.  This is not "the model is wrong
  everywhere" — it is one missing feature in a spectrum that otherwise reproduces the scale, the
  damping, the heights and the abundances.  *Whatever populates it, if anything does, will be a
  definite piece of physics and not a parameter.*

---

## ⌗ THINGS RETIRED ALONG THE WAY, RECORDED SO THEY ARE NOT REDISCOVERED

* **the factor of $2.02$** — pin-dependent: $2.02$ at `LATARG` $301.6$ and $1.57$ at $260$.  Both of its
  "independent" measurements were at the same pin.  *The mechanism stands; the number does not.*  (r3367)
* **the $0.72$–$0.79$ spacing** — a MEAN over a transient-dominated four-peak series.  The asymptotic
  spacing is $0.970$ against the control's $1.021$.  (r3183, verified r3309)
* **`PO-13` struck at r3307** — struck on numbers read out of the paper's prose with no computation
  behind them.  **Reverted.**  *A diagnosis assembled from a paper's own summary is not a diagnosis.*

---

## THE METHOD RULES THIS ARC BANKED

1. **Ask the receipts, not only the papers.**  What the corpus publishes and what it has already
   decided are different sets.  (`prior_art`, after r3339)
2. **And ask the sources.**  `p0` is authoritative for the ontology and the thesis carries the proofs;
   neither is reachable from the papers or the receipts.  (`source_texts`, after r3357)
3. **A receipt asserts what it establishes, never quotes what it found wrong.**  A check pinned to a
   defect fails the moment its own finding lands.  *Four instances.*
4. **State the prediction before the run.**  r3369's was wrong, and recording that is the point.
5. **Two pins or it is not a result.**  Any number measured at one configuration is a one-configuration
   number.  (r3367)

---

## ⌗ FROM THE HORIZON-TRANSIT LINE — r3397 WAS WRONG, RETRACTED AT r3398

⛔ **EVERYTHING r3397 APPENDED HERE IS WITHDRAWN.**  It rested on one error: I computed
`rs = integral from z_rec to INFINITY`.  **The plasma begins at the onset**, so the integral is
`rs = integral from z_rec to z_onset` — which `P15` states in the sentence I read past: *"the
standard radiation-governed rs is recovered only in the limit `z_onset -> infinity` that a
beginning at finite curvature forbids."*  With the correct limit:

| H0 | rs | D_M | theta_* |
|---|---|---|---|
| 67.4 | 147.01 | 14085 | **0.010437** |
| 70.0 | 141.55 | 13562 | **0.010437** |
| 73.0 | 135.73 | 13005 | **0.010437** |

**theta_* is exactly constant across H0 and equals 0.010437 against the observed 0.010411 —
0.25%.**  The mechanism works exactly as P15 describes: both `rs` and `D_M` carry the common
`1/H0`, the single parameter `z_onset` sets the scale, and it is met at the DIRECTLY measured
`H0`.  **There was no fork, no mis-assignment worth a factor 1.77, and no comb at 171.7.**  The
`257.72 Mpc` came from integrating through a region where there is no plasma.

⛔ **The `2/sqrt3` re-entry result is withdrawn too**, for the same reason: it used
`rs(z) -> 0` as `z -> infinity`, and `rs` does not extend above the onset.

---

## ⌗ WHAT SURVIVES, AND IT IS CR-NATIVE

**The acoustic modes re-enter the horizon BEFORE the plasma exists.**  On the rate, re-entry for
`k ~ pi/rs` is at `z ~ 2.5e4`; the onset is at `z_onset ~ 6797`.  So at the onset the modes are
inside the horizon and **frozen — there is no plasma for them to oscillate in yet.**  That is
what `prop:subhorizon` establishes, read forward.

**So the plasma turns on with every mode already sub-horizon and at rest, and they all begin
oscillating AT THE SAME MOMENT.**  The phase each carries at recombination is
`k * rs(z_rec)` with `rs` measured **from the onset** — a COMMON START TIME, not a common
`k rs = 0`.  **That is not the standard initial condition**, which has each mode's oscillation
matched at `k rs -> 0` in a radiation era this construction does not have.

**This is the interval's actual content, and it is where PO-13's question lives.**  What has NOT
been done: what a common-start-time initial condition does to the comb, worked from the
construction alone.  **Not to be estimated by importing a LambdaCDM peak-shift factor** — that
factor is the product of radiation driving and a potential decay this rate does not have.

---

## ⌗ AN INSTRUMENT MEASUREMENT (r3400) — THE CONSTRAINT FACTOR, AND WHY IT SETTLES NOTHING

**PRECONDITION: this is downstream of `OWED` (624), which is OPEN.**  Every peak position below
is a position of ONE OF TWO features, and which of them is the acoustic first peak is exactly
what (624) has not settled.  **Read no `l_1` here as an `l_1`.**

### What was changed, and why

`ACOUSTIC_two_arm.py` builds the CR arm's `Hc` from `rho_tot` WITHOUT radiation
(`RAD_IN_RATE=False`) while normalising the `Omega_i` in the `Phi` source to the full stack
(`_rt`, marked *"the STACK, both arms"*).  The `G^0_0` constraint is
`k^2 Phi + 3H(Phi' + H Psi) = -4 pi G a^2 drho`, and writing the source as
`(3/2) H^2 sum(Om_i d_i)` uses `H^2 = (8 pi G/3) a^2 rho_tot` — the FRIEDMANN CONSTRAINT, which
in CR is the **L2** leaf readout, *"the ordinary Friedmann readout with radiation gravitating
normally"* (`P15` `sec:properframe`).  **The two `rho_tot` are not the same one**, so the source
is short by `rho_tot(full)/rho_tot(free)` = **3.04 at the onset, 2.02 at equality, 1.33 at
recombination**.  Added env-gated as `GSRC=1`, identically 1 in the `lcdm` arm, both `Phi`
sites, **default OFF — the instrument is byte-identical to its committed form with the flag
unset.**

### What it measures

| | features below `l=500` | all maxima | `l_1/l_A` | `P1/P2` | `P1/P3` |
|---|---|---|---|---|---|
| baseline `GSRC=0` | **172, 396** | 172, 396, 628, 908, 1188 | 0.5703 | 0.965 | 0.823 |
| test `GSRC=1` | **196, 468** | 196, 468, 668, 940, 1204 | 0.6499 | **4.561** | 3.089 |
| undriven (r3323) | one, at 268 | — | — | 2.104 | — |
| sky | — | 220.6, 538.1, 809.8 | 0.7312 | 2.217 | 2.277 |

### What that means, and what it does not

**⑴ THE CONTINUUM GATE NOW PASSES, FOR BOTH ARMS.**  `KCONT=1` at 1200 modes — 5.8 points per
Bessel period against the discrete ladder's 2.3 — returns the SAME positions to the digit in
both configurations.  **Discreteness sets none of it**, which is the check the instrument has
been asking for in its own output and which was outstanding.

**⑵ IT DOES NOT REMOVE (624)'s EXTRA FEATURE.**  r3325 found that undriven, `DRC` alone and
`DRE=0.42` each give ONE maximum below `l=500` while both couplings together give TWO.  **`GSRC=1`
still gives two**, robust at every filter order.  It moves the pair (+24, +72) and WIDENS the gap
between them, 224 -> 272.  It is not a rigid shift and it is not undoing whatever creates the
second feature.

**⑶ IT IS NOT SIMPLY MORE DRIVING.**  Driving takes `P1/P2` DOWN from the undriven 2.104 to
0.965; this takes it UP to 4.561 — past undriven, opposite in sign to the driving axis.  So it is
a different knob, and its attribution is open.

**⑷ AND THE HEIGHT IS WORSE THAN IT WAS.**  56% low became 106% high.  By this row's own
criterion — *no coefficient fixes both* — that is a failure, not a partial success.

### The reading I will not make

⛔ *"`l_1` improved from 172 to 196 against the sky's 220.6."*  **That sentence needs 196 to be
the first peak, and (624) is open precisely on whether either 172 or 196 is.**  A two-feature
spectrum compared against a three-peak sky at the leftmost feature is a comparison of unlike
things until the feature identification is settled.  **(624) is the precondition, not a footnote
to this.**

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

## ⌗ FROM THE HORIZON-TRANSIT LINE (r3397) — THE INTERVAL, AND A MIS-ASSIGNMENT CLEARED

**The open item was:** *`P15` argues the condition at the branch point and applies it at the
onset without stating what happens between.*  What happens between is now stated.

**① EVERY ACOUSTIC MODE RE-ENTERS THE HORIZON INSIDE THAT INTERVAL.**  At the branch point
`aH -> infinity`, so every mode is outside and frozen; at the onset `k_hor ~ 0.010 /Mpc` against
`k_peak ~ 0.021 /Mpc`, so all are inside.  On P15's own rate the re-entries are at
`z ~ 2.5e4` (n=1) through `~3e6` (n=10) --- spread over two decades, all before the onset.
`k_hor(onset)` computes to `0.0103 /Mpc`, reproducing P15's quoted `~0.010`.

**② THE INTERVAL CANNOT IMPRINT ANYTHING k-DEPENDENT, AND THE REASON IS EXACT.**  On the
radiation-free rate at high z, `r_s(z) = (2c/sqrt3)/(H0 sqrt(Om) sqrt(1+z))` and
`k_hor(z) = H0 sqrt(Om) sqrt(1+z)/c`, so at a mode's OWN re-entry

        k r_s |_re-entry  =  2/sqrt3  =  1.154700538   EXACTLY

--- independent of `k`, `H0` and `Om`.  Oscillation onset (`k r_s ~ 1`) and horizon entry
(`k r_s = 2/sqrt3`) are the same event for every mode, always, so there is no separate entry a
mode could carry a phase memory of.  `r_s -> 0` at the branch point, so the solution is the
ordinary adiabatic `cos(k r_s)` measured from there, peaks at `n pi`.  **The offset is not in
the re-entry.  A tenth handle eliminated, and eliminated structurally rather than numerically.**

**③ A MIS-ASSIGNMENT FOUND AND CLEARED --- WHICH DOES NOT RESCUE THE PEAK.**  `P15`
`sec:properframe` listed *"a process running in the content---rs, r_D, recombination, the
perturbations---takes the leaf's [rate]"*, and `P7`'s figure caption said the same of the
plasma's sound horizon.  **That contradicts the decision rule stated four sentences earlier in
the same paragraph** --- *"a self-gravitating local excursion runs on L2, diffuse content riding
the global foliation on L1"* --- and contradicts the same paragraph's own warning that *"the
radiation-sourced L2 rate carried past the branch point radiation-pins rs and re-manufactures
the very tension this section dissolves."*  Our recombination-era plasma is diffuse content on
the global foliation, so `rs` is L1.  Both passages fixed at r3397.

**THE SIZE OF WHAT WAS AT STAKE, AND WHY IT IS NOT AN ESCAPE:**

| assignment | `rs` | `pi/theta_*` | `theta_*` across H0 67.4 -> 73 |
|---|---|---|---|
| leaf (the error) | 145.25 Mpc | 304.6 | 0.010312 -> 0.010729, **moves** |
| stacking (correct) | **257.72 Mpc** | **171.7** | 0.018297 -> 0.018297, **constant** |

The leaf assignment would have put the comb where the sky is and re-coupled `theta_*` to `H0`,
undoing the tension dissolution --- `Omega_r = omega_r/h^2` makes the radiation term
`H0`-independent, so it does not scale out.  **The framework's own rule forbids it.**  So `rs`
stays radiation-free, `pi/theta_*` stays at `171.7` --- inside this row's reported `172-188` ---
and **PO-13's central finding is confirmed from the outside**: the offset and the Hubble
resolution are one fact, and there is no bookkeeping error underneath it.

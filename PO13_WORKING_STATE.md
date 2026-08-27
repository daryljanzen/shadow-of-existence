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

---

## ⛭⛭⛭ THE LEAF-RATE CORRECTION AND WHAT IT LEAVES — the arc worked with node 58 (r3408+)

*58 (chat) found the defect and holds the framework; cc54 (compute) ran the instrument.  Nothing
below is routed into `P15` without a separate decision.  Read under `OWED` (624).*

### THE DEFECT, AND THE FIX THE FRAMEWORK SELECTS
The perturbation sector ran on the **L1 stacking rate**.  `P15` `sec:properframe` and `P7`'s
rate-rule assign a process running in the content --- `rs`, `r_D`, recombination, **the
perturbations** --- to the **L2 leaf rate** (radiation gravitating; `H_leaf` = the expansion scalar
of a self-gravitating congruence, so `eta_leaf` is a real conformal time).  The discrepancy is
`|Jac-1| = 0.128` at recombination, rising to `0.998` at `a = 1e-9` --- largest exactly where the
driving is set.  `LEAFPERT=1` (committed r3408) puts the perturbations on the leaf rate by the exact
chain rule `dY/deta_stack = (H_stack/H_leaf) F(Y, Hcal_leaf)`; `rs`, `D_M` and the projection keep
the stacking rate (L1, as `sec:tensions` assigns them).  The framework's call, in 58's words: the
perturbation sector is **L2 in full** --- equations, coefficients, and initial conditions.

### THE GATE (RUN 1): PASSES
`ARM=lcdm NK=900 LEAFPERT=1` returns `l_1 = 220`, identical to the flag-off control.  In the `lcdm`
arm `H_leaf == H_stack` character-for-character, so LEAFPERT is a provable no-op; confirmed
numerically at 2700 modes.  The implementation is sound; everything below inherits a validated gate.

### (624) DISSOLVES --- BUT NOT THE WAY FIRST CLAIMED, AND THE FIRST CLAIM WAS AN ARTEFACT
⚠ **Withdrawn (cc54, caught by 58): "the leaf rate removes the second feature (2 -> 1 below
`l=500`)."**  That was a **fixed-ceiling artefact** --- LEAFPERT's second feature moved `396 -> 516`
and crossed the fixed `l=500` line; nothing was removed.  r3325's own diagnostic shares the confound:
it counts maxima below a fixed `l=500` across combs of **different spacing**, and a tighter comb puts
more teeth under a fixed ceiling whether or not it has an extra one.  On the current instrument
`DRE=0.42` gives **two** below 500, not the one r3325 recorded.
⇒ **The scale-free replacement:** count no ceiling; read the **gap sequence**.  An extra feature is
one anomalously short gap in an otherwise regular comb.  **No configuration** --- undriven, DRC-alone,
`DRE=0.42`, baseline, LEAFPERT --- shows a short-gap intruder.  So **there was never an extra
feature**; the "two vs one below 500" was always spacing, and **every `l_1` read across this arc is a
real first peak.**  (624)'s premise is void.

### WHAT LEAFPERT FIXES: THE FIRST GAP
LEAFPERT's first gap is `l_2 - l_1 = 312`, against the control's `312` and the **sky's `317.5`** (1.7%).
The baseline's was `224`.  PO-13's standing residual --- *"the pin sets the asymptotic spacing and
leaves the first gap alone"* --- is **resolved by the leaf rate.**  The first peak is no longer the
problem.

### WHAT REMAINS: CR'S COMB IS UNIFORM WHERE THE SKY'S ALTERNATES
The observable is `g2/g1`, the ratio of the second to the first gap --- **scale-free**, so it isolates
the odd-even modulation from the overall `rs` shift.  The sky contracts the second gap
(`317.5, 271.7`, `g2/g1 = 0.856`); the control does too (`312, 280, 304`, `0.897`).  **CR does not:**
in **both** initial conditions the first two gaps are *exactly* equal --- default `312, 312`; the
leaf-clock accumulated-phase IC `280, 280` --- so `g2/g1 = 1.00` under two ICs that moved every peak.
This is **zero alternation**, robust, not a shortfall (to grid resolution `g2/g1 = 1.00 +/- 0.02`;
the gap to the sky is 5--7 sigma).

### THE INITIAL CONDITION IS NOT THE CAUSE (refuted)
`CRPHI=entryleaf` (committed) gives each mode the pre-onset acoustic phase it would carry on the leaf
clock (`phi(k)` up to `0.905 pi`).  It **shifts every peak** (`204,516,828 -> 196,476,756`) but leaves
`g2/g1 = 1.00`.  A k-dependent starting phase relocates the comb; it cannot manufacture a
compression/rarefaction asymmetry, which is dynamical (loading acting during the oscillation).  The
late-start hypothesis (58's, honestly proposed and honestly killed) is refuted.  *NB the framework
holds modes frozen before onset (no plasma), so `entryleaf`'s pre-onset acoustic history is a
diagnostic, not the framework's IC; the framework's IC is `CRPHI=0`, frozen at onset, which every
LEAFPERT run above used.*

### THE LOADING IS NOT THE CAUSE EITHER (gated, and decomposed)
`RBFAC` scales the baryon loading R consistently (sound speed and Euler inertia).
**Gate --- loading drives the alternation:** the control at `R=0` gives `g2/g1 = 1.065` (no
contraction) against `0.897` at the physical `R=0.6229`.  Removing the baryons removes the
contraction.  So the alternation *is* loading-driven --- the mechanism claim is earned, not assumed.
**But the CR shortfall is not the loading.**  Grid-matched (NK=700), the two arms have **nearly
identical loading response** (local slope `d(g2/g1)/dR`: CR `-0.292`, control `-0.270`) and **different
no-loading combs** (`R=0`: CR `1.182`, control `1.065`).  Decomposing the CR-minus-control gap at the
physical loading (`0.103`): the no-loading comb contributes `+0.117` and the loading response `-0.014`
--- i.e. the loading goes the *other* way (CR's is marginally the stronger).
⇒ **Counterfactual (linearity-free):** give CR the control's no-loading comb (`1.065`) with CR's own
loading and `g2/g1 = 0.883`, essentially the sky's `0.856`.  **The entire shortfall lives in the
no-loading comb.**

### SO THE RESIDUAL IS THE DRIVING, AND THE SIGN IS THIS WAY ROUND
The no-loading comb is the driving's fingerprint (no baryon asymmetry at `R=0`).  **The chain, stated
rather than concluded:** driving pulls the first peak inward, so `g1 = l_2 - l_1` grows, so `g2/g1`
falls; therefore a **higher** `g2/g1` means **less** first-peak pull, i.e. **weaker** driving.  CR's
`1.182` against the control's `1.065` therefore says **CR's driving is weaker.**  At `R=0` *both*
no-loading combs **widen** (neither alternates); CR widens **more**, and the physical loading --- CR's,
if anything marginally the stronger --- cannot overcome that larger head start.  This lands exactly
where PO-13's own record pointed: *the standard driving shift is universal because every mode crosses
during radiation domination, and a rate fixed by the geometry has no such crossing.*

### THE SIZE OF THE SHORTFALL --- NONLINEAR, DO NOT QUOTE A SINGLE FACTOR
The R-response is **curved**: successive local slopes are `-0.292, -0.218, -0.173` from `R=0`
outward.  So the global-fit extrapolation (which gave `R=1.40`, "2.25x") is **not valid** --- it
averages a curved response.  CR reaches the sky's `0.856` **somewhere near `R = 1.1`--`1.4`**
(local slope gives `1.12`, interpolating the outer points gives `1.29`), i.e. **of order twice** the
physical loading it has, with **no precise factor defined**.  The counterfactual above is the
clean statement; the R-shortfall is order-of-magnitude only.

### THE HEADLINE
Not that CR misplaces the first peak --- **the leaf rate fixed that.**  Not the loading --- **CR's
loading works.**  Not the initial condition --- **refuted.**  The residual is **the driving on a rate
fixed by the geometry**, which under-produces the compression/rarefaction alternation: CR's comb is
**uniform where the sky's alternates.**  Three independent routes converge on the one mechanism ---
PO-13's driving-crossing record, this gap-alternation decomposition, and 58's rigid-rescale parity
check.  *Method note: gap sequences not ceiling-counts; two configurations agree the alternation is
zero; the mechanism gate (loading) was run before the mechanism was claimed; the shortfall factor is
left as a nonlinear bracket rather than a fitted number.*

### ⛭⛭⛭ THE MECHANISM NAMED, AND WHY THE CLOSURE IS A FORK ON THE ONE FITTED NUMBER
The driving difference is now a statement about **two redshifts**, not a fingerprint.  Every acoustic
mode **re-enters the horizon before the plasma exists**: on the leaf rate `n=1` re-enters at
`z ~ 2.9e4`, `n=2` at `~1.2e5`, `n=3` at `~2.7e5`, and the onset is at `z=6797`.  So **no acoustic
mode crosses the horizon while there is a plasma to be driven** --- exactly the condition the standard
driving shift requires (58; and PO-13's own record: *"the standard shift is universal because every
mode crosses during radiation domination"*).

**The closing counterfactual (`ZSTART`):** push the onset UP past the re-entry redshifts so the modes
cross during the plasma era, and read `g2/g1` (scale-free, so it survives the acoustic-scale fit
breaking).  The scan --- CR LEAFPERT, physical loading --- is the **calibration curve**:

| `z_onset` | modes crossing during plasma | `g2/g1` |
| --- | --- | --- |
| 6797 (physical) | none | 1.000 |
| 1e4 | n=1 | 0.921 |
| 3e4, 1e5 | n=1 | 0.919 |
| 3e5, 1e6 | all three | **0.895** |

The alternation **appears exactly as `z_onset` passes the re-entry redshifts** and **saturates at the
control's value** (0.895 vs the control's 0.897) once all three modes cross.  **Compared to the
CONTROL, not the sky:** CR's deficit is `1.000 - 0.897 = 0.103` at the physical onset and
`0.895 - 0.897 = -0.002` --- exact agreement --- at saturation.  *The instrument misses the sky in
BOTH arms (control 0.897 vs sky 0.856); that residual `0.041` is the instrument's, common to both, and
is NOT charged to CR.*  ⇒ **The absence of the odd-even alternation is the absence of
crossing-during-plasma**, and forcing the crossing recovers the full control-level comb.  Closed on
the mechanism.

**⚠ WHAT THIS DOES NOT SAY, and the correction that keeps it honest (58).**  It does **NOT** say the
late onset is a consequence of the construction.  `z_onset` is **FITTED** --- `Z_START` is solved so
`l_A` hits `LATARG` --- so *"the plasma begins on the branch point's cooling leg"* is the **story**
about 6797, not its **provenance**.  Calling a fitted number a derived consequence is the move the
whole reframing pass exists to stop, and the mechanism's success must not smuggle it in.  *(An earlier
cc54 report and the `ZSTART` commit message carried that unearned claim; it is withdrawn here.)*

**⇒ THE REAL RESULT: a SECOND, INDEPENDENT HANDLE ON THE ONE FITTED NUMBER.**  The acoustic scale
fixes `z_onset` one way (6797).  The odd-even alternation constrains it another way (the calibration
curve wants `z_onset` **above 3e5**).  Two independent observables pull on one fitted parameter **in
different directions** --- which is precisely (624)'s neighbour, PO-13's open *"what the construction
says the datum should be at the onset,"* now with teeth.  **The closure is therefore a FORK:**
- **(A)** the construction genuinely places the onset above `3e5`, and the acoustic-scale fit is doing
  something else --- then both handles are met and the datum is over-determined in CR's favour.
- **(B)** the onset is `6797`, and CR then **predicts a uniform comb where the sky alternates** --- a
  clean, falsifiable disagreement, not a defect to be tuned away.
- **(C)** something other than crossing-during-plasma supplies the alternation and the
  saturation-at-the-control is coincidence --- least likely, and directly testable by the `Phi(eta)`
  envelope (does the potential decay with the k-dependent phase that produces alternation, or
  smoothly).  **Run next.**

Written closed on the mechanism, **fork open**, calibration curve recorded, with no claim about where
`6797` comes from.  Not routed into `P15` without Daryl's separate call.

**Branch (C) tested and disfavoured (the `Phi(eta)` envelope).**  Saving the potential per acoustic-peak
mode (`PHISAVE`, onset -> recombination) and asking 58's question --- does the potential decay with the
k-dependent phase that produces alternation, or smoothly --- the control's `Phi` carries **more
oscillatory turning points** (`1, 1, 3` across the first three peak modes) than CR's (`0, 0, 2`): the
control's potential **rebounds with the acoustic phase** (phase-coherent driving) while CR's decays
**more monotonically**.  That is the field-side image of the redshift-side mechanism --- at the physical
onset CR's modes are already sub-horizon and frozen, so there is no crossing to drive a phase-coherent
potential --- so the saturation-at-the-control is **not a coincidence**, and (C) is disfavoured.  The
effect is modest (one turning point per mode), not a knockout, but it points the same way.  **The fork
narrows to (A) vs (B)** --- both real outcomes, neither an artefact: either the construction places the
onset above `3e5` (over-determining the datum in CR's favour) or it says `6797` and CR carries a
falsifiable prediction of a uniform comb.  **That is a framework question --- 58's --- and it is PO-13's
own open datum, now held by two independent observables instead of one.**

### ⛭⛭⛭ THE FORK RESOLVES TO (B): A DERIVED, FALSIFIABLE PREDICTION (58, framework)
**(A) is closed.**  The apparent route to (A) was a suspected `P15`/`P16` contradiction: `P16`'s cooling
leg runs a standard BBN (helium-4 and deuterium at observed values), which needs a plasma at MeV
temperatures; if that plasma were on **our** expansion leg, it would exist at `z ~ 1e9`, the acoustic
modes would cross the horizon during it, and (A) would follow.  It is not on our leg.  `P16`
`fig:history` places the nucleosynthesis on the **transit's cooling leg** --- after turnaround, the
expansion cools the matter back through the nuclear window and deuterium freezes out **there, before the
branch point** --- and states that *"the observable expansion history begins only later, at the ~1.6 eV
onset ... the nucleosynthesis is complete below it."*  So the BBN plasma is the **progenitor's**, on the
far side of the branch point; **our** expansion-leg plasma begins at the onset.  `P15` and `P16` agree,
and the objection dissolves.  The onset genuinely sits at `z=6797`, below the acoustic re-entry
redshifts.

**So (B) stands, and it is a PREDICTION, not a deficit.**  On the radiation-free rate the plasma begins
at the onset, below every acoustic re-entry redshift (`n=1 ~2.9e4`, `n=2 ~1.2e5`, `n=3 ~2.7e5`), so **no
acoustic mode crosses the horizon while our plasma exists**, so the comb is **uniform**.  The sky's
comb **alternates**.  That is a **falsifiable disagreement with a derived cause** --- the odd-even
modulation is the standard driving shift, which requires crossing-during-plasma, which the
geometry-fixed rate does not have --- and it is the sharpest empirical statement the corpus carries.

**The counterfactual IS the calibration** (what makes the prediction testable rather than merely
stated): raise the onset past the re-entry redshifts and the alternation **appears and saturates at the
control** (`g2/g1`: 1.000 at 6797 -> 0.921 once `n=1` crosses -> 0.895 = the control's 0.897 once all
three do).  **Charge CR only with its own deficit:** `0.103` against the control at the physical onset;
the remaining `0.041` to the sky (control 0.897 vs sky 0.856) is the **instrument's**, common to both
arms, and is not CR's.

*The P7/P15 wording --- naming the mechanism and stating the prediction where the frontier text (r3409)
currently leaves a location --- is 58's to take.  P15 is held until then.  Nothing here is routed into a
paper by cc54.*

### ⛭⛭⛭ THE DRIVING SHIFT Q(k) DIRECTLY MEASURED --- 58's PREDICTION CONFIRMED (r3410+)
58 derived, on a Meszaros background, that the driving shift `Q(k)` (accumulated sound phase in
half-periods at the acoustic turnover) is **flat below 1 for the control and rises toward 1 for CR** ---
the normalisation-independent, falsifiable statement of *"the uniform comb IS the undriven comb."*  Run
on the full instrument by subtraction (`QSCAN`, undriven-calibrated to 1.000 on both arms):

| `k` [1/Mpc] | `Q_CR` (leaf) | `Q_control` |
| --- | --- | --- |
| 0.060 | **1.283** | 0.670 |
| 0.088 | 1.198 | 0.658 |
| 0.130 | 1.134 | 0.651 |
| 0.190 | 1.090 | 0.645 |
| 0.280 | **1.058** | 0.643 |

`Q_control` is **flat at 0.64--0.72** (58's control 0.66--0.72, the calibrated half --- exact match);
`Q_CR` **rises toward 1 from above** (58's 1.276 -> 1.008 --- same shape, near in magnitude).  **The
prediction is confirmed.**  And `Q_CR > 1` at low k --- the turnover is *later* than a free oscillator's,
58's novel signature --- appears in this **full-neutrino** instrument too, so it is not an artefact of
58's omitted 40%.

**Two instrument corrections were needed to see it, both real and both gated by the undriven column
(=1.000):** (i) under LEAFPERT `sound_phase` must reckon in `eta_leaf`, or the CR undriven calibration
comes out 1.33--1.57 (the stack/leaf ratio) not 1; (ii) the turnover must be the **first velocity
zero-crossing past the frozen-IC transient** (`QTURN=vel QMIN=0.5`) --- the CR driven mode's first
crossing is a transient at `Q~0.08`, the acoustic turnover the next at `Q~1.2`, subsequent crossings
spaced ~1 half-period.  Reading the transient gave `Q_CR -> 0` (spuriously "driven"), inconsistent with
the uniform comb; skipping it gives 58's rising curve.  *That is exactly the transient 58 named when
choosing the velocity zero-crossing over the temperature extremum; it just also bites the velocity
crossing on a mode already deep sub-horizon at onset.*  The comb (uniform) and the Q(k) (undriven,
rising to 1) now agree, and both confirm the mechanism the r3410 papers state.

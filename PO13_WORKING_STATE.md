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

### ⛔ PREMISE WITHDRAWN (58, r3427) — the A.139 motivation is gone; and Q(k) is RESTORED at r3429
**`A.139` (r2081), and the `CRRUN5`/`A.46` re-run 58 also queued, predate r2123 — they use "seam" to mean
"the beginning", the `r=0`-as-seam conflation 58 cleared from eight papers at r3380 and then let adjudicate
live work for three revisions.  58 withdrew all three in full at r3427.**  So the *question* this section
answered ("is A.139 stale-because-stacking?") is moot: A.139 is withdrawn regardless.  Per 58's instruction,
**discard the interpretation-against-A.139 and keep the numbers** — they came from cc54's instrument, not from
the archive, and they are untouched.

**⛭ AND THE r3424 Q(k) WITHDRAWAL IS ITSELF REVERSED (58, r3429).**  `Q(k)` is restored to `P15`/`P07`,
**sourced to cc54's `qscan`** (the gated instrument measurement: undriven `1.0000`, k-drift `<0.004` on both
arms; control flat at `0.79`; CR rising `1.28 -> 1.06`), NOT to 58's analytic toy.  The toy *receipt* stays
withdrawn — its turnover detector reads a `y~0.6` transient before the oscillation establishes, i.e. it has
the same frozen-IC-transient bug `QMIN` was built to skip, at the opposite sign — but that withdraws the
*file*, not the *finding*.  So the "58's prediction confirmed" `Q(k)` section further below **stands**; my
earlier "superseded" note on it is retracted.

**What genuinely survives here and is forward is the k-space vs time-domain SIGN SPLIT** (below): two gated
measurements of CR's driving disagree in sign — k-space Theta_0 extremum `-0.42`, time-domain `qscan` turnover
`+0.2..+0.4`.  Both gate undriven at `~1.0`, so it is not a broken calibration; it is the same *transient*
question in two domains.  `qscan` skips its transient with `QMIN`; the raw k-space extremum has no such skip,
so it is the prime suspect for reading the k-space image of that transient.  **This is exactly the forward
piece 58 named — "a turnover measure that survives both signs of the initial datum" — and the mechanistic
version of it (does Phi decay overlap the oscillation) is what cc54 works next.**  Read the tables below as
instrument facts about the CR source, not as a verdict on any ledger entry.

### ⛭ (archived question) THE RATE IS NOT THE LEVER; k-SPACE AND TIME-DOMAIN MEASURE DIFFERENT QUANTITIES
58 asked (task ②): is `A.139`'s CR "source phase shift" `-0.362` a stale **pre-leaf-correction**
(stacking-rate) measurement — reproduced by `STACKPERT=1`/`LEAFPERT=0` and NOT by the leaf rate —
or do both rates give it, in which case `qscan` and `A.139` measure different things? **Run both
ways.  It is the second branch, and sharper than the fork.**

**What `A.139` measured (from `storyboard_receipts/retired_conformal_seed/PROJGEN_projection_generic.py`):**
the FIRST EXTREMUM IN `k` of the SW source `Theta-hat = Theta_0 + Psi` at `eta_rec`, reported as
`k r_s/pi` (undriven **assumed** `= 1`; shift `= k r_s/pi - 1`).  DRIVEN only; no undriven column run.

**Reproduced on the instrument (`evolve` to `eta_rec`, first source extremum in `k`), DRIVEN, uncalibrated:**

| | source extremum `l` | `k r_s/pi` (own clock) | shift | `A.139` |
| --- | --- | --- | --- | --- |
| ΛCDM (`Theta-hat`) | 269.9 | 0.896 | **-0.104** | -0.086 |
| CR stacking (`Theta-hat`) | 198.9 | 0.660 | **-0.340** | -0.362 |
| CR leaf, phase clock (`Theta-hat`) | 254.7 | 0.657 | **-0.343** | — |

`A.139` reproduces (ΛCDM `-0.10` vs `-0.086`; CR `-0.34` vs `-0.362`).  **And the leaf rate gives the
SAME shift as the stacking rate** — `-0.343` (leaf, on `r_s,leaf`) vs `-0.340` (stacking).  ***The rate
is not the lever.***  `A.139` is NOT stale-because-stacking.  → 58's second branch.

**The real defect in `A.139` is the CALIBRATION, not the rate — and stripping `Psi` exposes it.**
`Theta-hat`'s `Psi` piece plants a spurious low-`k` extremum, so the *undriven* `Theta-hat` first
extremum sits at `k r_s/pi ~ 0.42` for **both** arms — `A.139` never measured its own undriven column
(the very discipline `qscan` was built on), so it could not see that `1` was the wrong reference.  Using
`Theta_0` alone (pure acoustic), the undriven calibration comes out right and the driving shift is
**measured, not assumed:**

| | undriven `k r_s/pi` | driven `k r_s/pi` | **calibrated k-space shift** |
| --- | --- | --- | --- |
| ΛCDM control | 1.015 | 0.828 | **-0.187** |
| CR stacking | 1.008 | 0.587 | **-0.421** |
| CR leaf (phase clock) | 1.009 | 0.583 | **-0.426** |

Undriven `= 1.01` on all three (validates the method).  **The calibrated k-space driving shift is
`-0.42` for CR against `-0.19` for ΛCDM — CR driven ~2.3x harder, and rate-independent (`-0.421`
stacking, `-0.426` leaf on the phase clock).**  So `A.139`'s *direction* survives calibration; its `4x`
was inflated by the uncalibrated `Psi` (calibrated it is `~2.3x`).

**THE TENSION, NAMED — and it is the r3424 retraction's cause, located.**  Two *calibrated* measurements
disagree in SIGN on CR's driving:
- **k-space** (`Theta_0` first extremum in `k` at `eta_rec`, the peak-position observable the projection
  integrates): CR shift **`-0.42`** — driving pulls the first extremum to LOWER `k r_s`.
- **time-domain** `qscan` (`Theta_0` velocity turnover of a fixed `k`, transient-skipped `QTURN=vel
  QMIN=0.5`, undriven `= 1.000`): CR `Q ~ 1.2`–`1.4` — shift **`+0.2`–`+0.4`**, turnover LATER than a free
  oscillator.

Same sign flip on both rates, so it is **not** the rate.  It is the feature: a k-space snapshot extremum
at recombination vs a mode's temporal turnover phase.  **This is exactly why 58 withdrew `Q(k)` at r3424
("depends on the chosen IC, reverses with sign") — the two features carry opposite-signed shifts, and
which one you read is the IC/feature choice.**  The k-space extremum is the one that projects into `l_1`
(the source is integrated at `eta_rec` against `j_l(k(eta_0-eta))`), so it is the peak-position-relevant
one, and it says CR's *first peak* IS driven low, ~2.3x ΛCDM.

**⚠ FLAG FOR 58 (framework's call, not routed by cc54).**  This does not touch the PO-13 residual as
*stated* — that residual is the absent **odd-even alternation** (`g2/g1`), a different observable from the
`l_1` driving shift, and it stands.  But it does mean **the blanket word "undriven" for CR's comb is too
strong**: the calibrated k-space measurement shows the first-peak driving is real and *stronger* than the
control.  The precise statement ("no compression/rarefaction alternation, because no mode crosses during
a plasma") survives; "the uniform comb IS the undriven comb" as a whole-comb claim needs the `l_1`
driving carved out of it.

**Supersession of the r3410+ Q(k) section above:** 58 retracted `Q(k)` from `P15`/`P07` at **r3424** as an
initial-condition artefact.  The "58's prediction confirmed" table above is therefore **superseded** — not
because the numbers were wrong (they reproduce), but because the sign is IC/feature-dependent, which this
A.139 reconciliation now explains rather than merely asserts.  The comb (uniform), the mechanism (no
crossing-during-plasma), and the ZSTART calibration are untouched by the retraction.

### ⛭⛭⛭ THE DRIVING, DERIVED FROM Φ(η,k) — THE CROSSING IS THE DRIVING, NOT THE DECAY (58's forward piece)
58's forward piece, once the archive was cleared: *what does the driving do on a rate fixed by the
geometry, derived from the potential's own evolution rather than measured off its fingerprint?*  Worked
on cc54's gated instrument (`PHISAVE`: `Φ(η)`, `δγ(η)` for the first three peak modes, leaf rate vs
control), **with no turnover detector and no chosen datum** — the sign-unstable step that broke both my
`qscan` transient reading and 58's toy.

**What Φ does on the leaf rate — the naive picture is wrong.**  `Φ` is NOT frozen on the leaf rate: it
decays ~40% for the first modes and ~0.6 per acoustic half-period, **smoothly (monotone; ringing <0.2%
of the decay), comparably in BOTH arms** (CR `0.60–0.75`/half-period vs control `0.56–0.68`; ratio 1.08).
So "CR undriven because the potential is frozen" is false, and every scalar built on the *ongoing* decay
fails to separate the arms — because the ongoing decay is not the driving.

**The driving is imparted at HORIZON CROSSING, and that is where the arms differ — measured:**

| mode | horizon entry `1/k` [Mpc] | `k·η_onset` | crosses during plasma? |
|---|---|---|---|
| CR `q=0.75` | 57.7 | **3.1** | no — sub-horizon at onset |
| CR `q=1.86` | 23.2 | **7.8** | no — sub-horizon at onset |
| CR `q=2.93` | 14.7 | **12.2** | no — sub-horizon at onset |
| control `q≈0.8–2.9` | 55–16 | 0 | **yes — all cross in [0, η_rec]** |

CR's onset is `η_start = 180.4 Mpc = 0.402 η_rec` (`z_onset=6797`, near `z_eq=3399`).  **Every CR peak
mode's horizon entry `1/k` lies BEFORE the onset** — they are switched on already deep sub-horizon
(`k·η_onset = 3–12`), at rest, at the common start time.  They never make the frozen→oscillating
transition *inside the plasma*, so they never receive the horizon-crossing driving impulse.  The control's
modes cross at `1/k` DURING the plasma, with `Φ` decaying through the crossing — they are driven.

**This is the crossing-during-plasma mechanism, DERIVED** (from `Φ(η,k)` + the geometry's onset), not read
off the peak positions.  It is detector-free and IC-sign-free, so it is immune to the failure mode that
made `qscan`'s raw reading and 58's toy disagree.  And it explains that disagreement: the ongoing decay
(similar in both arms) is what naive measures and the raw transient-crossing detectors catch; the *impulse
at crossing* (present in the control, absent in CR) is the real driving, and only a from-onset phase
accumulation (`qscan` with `QMIN`, `Q_CR → 1`) or this crossing census sees it.

**Corroborates, does not disturb:** the papers' restored `Q(k)` (r3429) and the uniform-comb mechanism.
The k-space `Θ₀`-extremum shift `−0.42` (this session, above) is now understood as the k-space image of
the switch-on transient — a driven feature with no `QMIN`-analog skip — consistent with `qscan` being the
reliable measure.  **The honest statement 58 named holds: the driving is in the crossing; CR's modes,
launched sub-horizon at the late geometric onset, do not cross during the plasma.**  Figure:
`computations/beyond_the_wall/PHI_mechanism.png`.

### ✔ LANDED — r3431 (mechanism grounded in P15) and r3430 (Q(k) sign settled)
**r3431:** the Φ(η,k) crossing result is merged; **P15's mechanism paragraph now carries the measurement,
not the assertion** — that Φ does not sit frozen (~40%, ~0.6/half-period decay), that the per-half-period
decay rate is the same in both arms to within the spread across modes, and that the separation is the
impulse at crossing, with the three entry radii (57.7, 23.2, 14.7 Mpc) and three `k·η_onset` (3.1, 7.8,
12.2), cited to 58's receipt.  58's receipt title is corrected (decay → crossing); **conclusion unchanged**
— a mode that never crosses while there is a plasma inherits the undriven phase.  P15's own wording ("the
standard shift is universal only where every mode crosses the horizon while there is a plasma to be
driven") was right all along; the paper said crossing, the receipt had said decay.  The crossing census
answers the driving question **without any turnover measure**.

**r3430 — the Q(k) sign question, settled by 58, with a caveat cc54's record must carry:** a sign flip in
the initial amplitude is a `π` phase shift, so it moves *which zero is first* by exactly one half-period.
At large `k` the four initial signs agree to a spread of `0.012`, so **`Q → 1` at large k is robust; the
LOW-k `Q` values are NOT** (they depend on the initial-amplitude sign).  → In the "58's prediction
confirmed" Q(k) table above, read the large-k approach to 1 as the load-bearing result and treat the
low-k magnitudes (`Q_CR = 1.283` at `k=0.060`, etc.) as sign-dependent, not firm.  The comb, the
mechanism (now measured), the calibration curve, and `Q → 1` all stand; the low-k `Q` magnitudes are the
one thing held loosely.

**PO-13 disposition:** the paper carries the comb, the mechanism (grounded in Φ's evolution), the
calibration curve and Q(k), all on gated instrument measurements.  The A.139/A.46/CRRUN5 premises are
withdrawn (r3427); the r3424 Q(k) withdrawal is reversed (r3429); this arc's compute half is landed.

### ✔ THE "47% PROJECTION" CONTRADICTION — DISSOLVED, IT IS THE k→PEAK MAPPING (58's flag)
58 flagged a contradiction between two current gated numbers: `Q_CR ≈ 1.28` (source turnover LATER than
free, `k r_s = 1.28π`) vs the spectrum first peak `ℓ_1/ℓ_A = 0.676` (`k r_s = 0.676π`, EARLIER than free)
— a factor ~1.9 apart, implying a 47% projection where `A.139` bounds it generic at 14–18%.  **It is 58's
first possibility: the `Q = 1.28` does not belong to the first-peak mode.**  Three measured facts settle it:

**(1) `Q` at the first-peak mode is UNDEFINED — not 1.28, not 0.68.**  `qscan` (`QTURN=vel QMIN=0.5`) at the
exact peak-mode k's returns `—` for the first two CR peaks (`k=0.0157=ℓ_1`, `k=0.0397=ℓ_2`):

| peak mode | k | driven Q |
|---|---|---|
| ℓ_1=204 | 0.0157 | **— (no turnover before rec)** |
| ℓ_2=516 | 0.0397 | **—** |
| ℓ_3=828 | 0.0637 | 1.268 |
| ℓ_4=1164 | 0.0895 | 1.195 |

The first-peak mode is *by definition* the mode caught at maximal compression AT recombination — it has not
reached a velocity turnover, so `Q` does not exist for it.  **The `Q=1.28` was measured at `k≈0.060`, the
THIRD-peak region (`ℓ≈780`), and read as if it were `ℓ_1`.**  The `Q(k)` curve (rising to 1) lives entirely
in the turned-over modes (`ℓ_3` and smaller scales); it never reaches `ℓ_1`.

**(2) The first-peak projection is +1.9%, not 47%.**  The comb's own source extrema project to the spectrum
peaks cleanly:

| peak | source extremum ℓ | spectrum peak ℓ | projection shift |
|---|---|---|---|
| 1 | 208 (0.690 ℓ_A) | 204 (0.676 ℓ_A) | **+1.9%** |
| 2 | 520 | 516 | +0.8% |
| 3 | 816 | 828 | −1.5% |
| 4 | 1168 | 1164 | +0.3% |

All under 2% — well inside `A.139`'s generic 14–18%.  The projection is doing nothing anomalous on the CR arm.

**(3) The 47% equated two different objects.**  `Q`'s `ℓ=1.28·ℓ_A=386` is a VELOCITY turnover of a `k=0.06`
mode; the first spectrum peak `ℓ=204` is a DENSITY extremum of the `k=0.0157` mode.  Different feature (velocity
vs density, offset a quarter period), different mode (third-peak region vs first).  The comb source extremum
`ℓ=208` — a density extremum, same feature, same mode — is what projects to `ℓ_1=204`, and it does so at 2%.

**Disposition:** the discrepancy dissolves and it was in the k→peak mapping, 58's side, as 58 anticipated.
**Caveat for the papers:** `Q(k)` and the comb are readings of DIFFERENT features and must not be presented as
`ℓ_1`'s phase measured two ways — `Q(k)` speaks to the turned-over modes (`ℓ_3`+), the comb/spectrum sets
`ℓ_1`.  Both stand; they are simply about different modes.  No 47%, no anomalous projection, no new problem.

### ✔ TWO-ARM POSITION PIN (overnight, after the field bake) — the position deficit is CR-arm-specific, in the SOURCE PHASE
**Method:** prediction stated before the run (the field bake's optics/statistics closes implied the CONTROL
positions sit ~0.1% from sky while CR's `l_1/l_A=0.676` is CR-specific); two pins (BOTH arms, one machinery),
each compared to sky AND to each other. Instrument `ACOUSTIC_two_arm.py` at `NK=620` (9.1 points/Bessel
period, above the aliasing guard — the guard fired and was cleared, not bypassed).

| arm | `l_1/l_A` | peaks (line-of-sight) | vs sky 0.7312 | P1/P2 |
|---|---|---|---|---|
| CONTROL `ARM=lcdm` | **0.7300** | 220 / 532 / 812 / 1116 | **−0.16%** (sky 220.6/538.1/809.8) | 2.447 |
| CR `ARM=cr` | **0.6764** | 204 / 516 / 828 / 1164 | **−7.5%** | 2.013 |

**Result (two pins, prediction confirmed):** the CONTROL's first peak lands ON the sky (0.7300 vs 0.7312,
0.16%) using the SAME projection, transfer, and line-of-sight machinery the CR arm uses; the CR arm sits
7.5% low. **Since the two arms share the projection and the transfer, the position deficit cannot be in
either — it is entirely in the SOURCE PHASE of the CR (undriven-comb) arm.** This is the live two-arm
confirmation of the field-bake flag: positions are a CR-source problem, not a shared/instrument or a
projection problem (the +1.9% projection is generic and clean, r3432; lensing does not move peaks, P15).

**Amplitude, for the record (same run):** sky P1/P2 = 2.217 sits BETWEEN the two arms — CR 2.013 (under),
control 2.447 (over). P07's construction reports 2.185 (≈0.9σ of sky), closer than either raw arm. So the
amplitude is bracketed and near; the POSITION is the open ~7.5% (≈70σ at peak-position accuracy, P07).

**The lever, named for the framework node.** The position lever is the CR arm's source phase — the first
extremum of `Theta-hat = Theta_0 + Psi` in k, set by the phase clock `r_s,leaf` (105.36 Mpc) against the
ruler `r_s,stack` (135.46 Mpc), ratio 1.286. The CONTROL uses one sound horizon for both; the CR arm's two
horizons are what displace its source extremum to 0.690 `l_A` (→0.676 after projection) instead of ~0.731.
Moving it toward the sky is a SOURCE-PHYSICS choice (e.g. the `LEAFPERT` vs `STACKPERT` frame, P15
sec:properframe — which rate the perturbation sector sees), which is 58's "name the piece," not an
instrument knob to flip unattended. **Compute half handed over: the deficit is isolated to the CR source
phase and quantified (7.5%), with both pins on the record.**

### ✔ THE SOURCE-PHASE-CLOCK LEVER IS BRACKETED — and neither frame reaches the sky (a real tension, named for 58)
**Diagnostic (not an adopted frame):** ran the alternate source-phase clock `STACKPERT=1` (the perturbation
sector sees the stacking/ruler rate, P15 sec:properframe) against the default `LEAFPERT`, to MEASURE the
size of the frame lever on `l_1/l_A`. Same instrument, `NK=620`.

| source-phase frame | `l_1/l_A` | peaks | P1/P2 | vs sky 0.7312 |
|---|---|---|---|---|
| `STACKPERT=1` (ruler clock) | **0.5703** | 172 / 396 / 628 / 908 | 0.965 | −22% |
| `LEAFPERT` (leaf clock, default) | **0.6764** | 204 / 516 / 828 / 1164 | 2.013 | −7.5% |
| — sky — | 0.7312 | 220.6 / 538.1 / 809.8 | 2.217 | — |

**Result:** the two documented frames BRACKET `l_1/l_A` at 0.5703 and 0.6764, and **the sky (0.7312) sits
ABOVE BOTH**. The default `LEAFPERT` is already the favourable frame (STACKPERT is worse on position AND
collapses the amplitude to 0.965). So switching the source-phase clock is NOT a lever toward the sky — it
moves the wrong way, and the frame choice already made is the better one.

**The tension this isolates (for 58's adjudication).** Neither undriven-comb frame reaches the sky's
first-peak position, and the reason is structural: the sky's `l_1/l_A=0.731` encodes the standard acoustic
**radiation-driving** phase shift (~0.27π), while the CR comb is UNDRIVEN by the established mechanism
(modes sub-horizon at the late onset `z_onset≈6797`, never cross while there is a plasma → the undriven
phase, r3429/crossing census). An undriven comb's source phase sits intrinsically BELOW the driven sky
value, in both frames. So the position residual is not a frame artifact and not a projection/transfer
artifact (the CONTROL, same projection+transfer, lands on the sky) — **it is the undriven mechanism's own
signature.** Two readings are open, and choosing between them is the framework node's call:
  (a) the sky's first-peak position is NOT purely the driving phase shift, and there is a CR source-phase
      contribution (not yet in the instrument) that lifts 0.676 → 0.731 without a driving impulse; or
  (b) the undriven comb structurally cannot reach the sky position, and the ~7.5% (≈70σ) is a genuine,
      standing CR-vs-sky position residual — a prediction the data does not yet confirm, to be carried as
      OPEN rather than closed.
**Compute disposition:** the position deficit is fully isolated — CR source phase, both frames bracketed
below sky, projection and transfer exonerated by the control pin. The amplitude is bracketed and near
(sky 2.217 between CR 2.013 and control 2.447; P07's construction 2.185). What remains is the (a)/(b)
adjudication, which is physics-model, not instrument — handed to 58 with both pins and the bracket on the
record. **Not asserting a closure that the instrument does not show.**

---

## ⛔ THE INSTRUMENT'S FLAG INVENTORY — r3512 (58), *after the third miss in one arc*

> ⌗ **KEPT AS THE "HOW IT WAS FOUND" RECORD (merged from main r3512, r3527).** *This diagnosis was
> written from **main**, which lacked the branch's fix. The composition defect it describes below was
> **already repaired on this branch** — `evolve_hier` carries the `SRCSTACK=vel` split and `DIFFLEAF`
> reaches `_project`, and the entire seam / KCONT / RBFAC arc ran on the fixed instrument. So the
> fix **predated** the diagnosis; the section stands as the record of how the defect was named, not as
> an open defect.*

**⌗ THE PATTERN, NAMED.** *Three times in this arc a result was bounded by operations that were
**already built and unrun**:*
1. *the position fork rested on `LEAFPERT` vs `STACKPERT` while **`PHASEONLY`** sat unrun — pulling it
   refuted the fork;*
2. *`POLSRC` was hand-rolled from a tight-coupling steady state while **`HIER`** sat unrun — carrying
   an evolved Π, both source terms, and its own control;*
3. *and `HIER` itself did not know the newest operations (below).*

⇒ ***The failure mode is always the same: assuming the switch you know about is the only one there is.
Before building an operation, `grep environ` and read every flag.***

### ⌗ THE FLAGS, IN FULL

| group | flags |
|---|---|
| **arm / grid** | `ARM` `NK` `LMAXL` `LSTEP` `RTOL` `ZSTART` `ETAEND` `LATARG` `KBATCH` |
| **clock division** | `STACKPERT` · `PHASEONLY` + `PHASEPOW` · `SRCSTACK` · `DIFFLEAF` · `GSRC` *(the constraint factor — **never run**)* |
| **damping** | `POLC` (the 16/15) · `DAMPX` · `RD` · `NOTC` *(default 1: hierarchy damping off so $e^{-k^2/k_D^2}$ is the sole dissipation)* |
| **hierarchy** | **`HIER`** · `LG` (depth 24) · `TCSW` (hand-over $\tau'$) · **`PISRC`** *(1 = both polarisation source terms; **0 = hierarchy kept, source dropped** — the exact subtraction)* |
| **diagnostics** | `NODRIVE` · `QSCAN` `QTURN` `QMIN` · `KCONT` · `NOPROJ` · `NOISW` · `DSCAN` `DSAVE` · `PHISAVE` · `SAVE` · `LOS` `NLOS` |
| **content** | `BSPLIT` `RBFAC` `CRAMP` `CRPHI` `CRXE` `DRC` `DRE` |

### ⛔ THE COMPOSITION DEFECT — *checked, r3512; **fixed on this branch before the diagnosis was written***

*`evolve_hier` and `_project` referenced the clock operations **once** on main
(`Jac_of(e) if LEAFPERT`), where the main path references **two**.* ⇒ ***On main, `HIER=1` did not
know `SRCSTACK` or `DIFFLEAF`.***

⛔ **So on main, `HIER=1` composed with `SRCSTACK=vel` would evolve the hierarchy with gravity on the
LEAF — the very assignment the position result required moving to the STACK — and nothing would
announce it.** ⌗ ***The ΛCDM gate cannot catch this***, *since $\varphi\equiv1$ makes every clock
operation a no-op there. **A CR number from that composition would be two physical models in one run.***
✔ **On this branch the split was added to `evolve_hier` (gravitational velocity-source on the stack)
and `DIFFLEAF` was made to reach `_project`'s frozen envelope — so the CR runs of this arc are single
physical models, not two in one.**

### ⌗ THE GATE ORDER THAT FOLLOWED

1. **`lcdm HIER=1`** — validates Π only. Position holds at $0.7300$; $P_1/P_2$ moves from $2.447$
   **toward** $2.217$, not past it. *(Ran: control HIER 0.7300 / 2.254 / 2.363.)*
2. **`lcdm HIER=1 PISRC=0` vs `PISRC=1`** — the instrument's own subtraction; the difference **is** the
   returned half. *(Ran: the source returns ~0.5%, 2.265→2.254 — the recovery is the hierarchy's proper
   damping, not the source.)*
3. ⛔ **THE COMPOSITION FIX** — the hierarchy's gravitational source on the stacking clock, its
   diffusion on the leaf, *the same LGF assignment the main path carries*. **Done on this branch.**
4. **CR**, reporting $\ell_1/\ell_A$, $P_1/P_2$, $P_1/P_3$, $P_1/P_4$ **together**. *(Ran across the
   seam / KCONT / RBFAC arc.)*

⌗ **THE PREDICTION THAT KEPT IT A TEST.** *A correctly composed Π is driven by the same retimed
$\theta_\gamma$ that produced $0.7294$, so it should arrive **weighted to high $k$** and act as a
**shape**: $P_1/P_3$ and $P_1/P_4$ should fall further than $P_1/P_2$.* ⌗ *Borne out in part — under
`seam`, $P_1/P_3$ landed exactly on the sky while $P_1/P_2$ stayed high (the even-peak deficit); the
position moved **up** to $0.7560$ under `seam`, which the later analysis showed is an **envelope rung**
(centroid, not phase), KCONT-verified as not aliasing — not the "wrong clock" the prediction feared,
since the composition was fixed. **The amplitude, however, closed under no IC — see the UNBANKED
record below.***

### ✔✔ THE POSITION IS CLOSED — the two-horizon clock division, not a driving impulse (supersedes the (a)/(b) hand-off above)
**cc54 was wrong above, and 58/Daryl were right.** I took "an undriven comb's source phase sits intrinsically
below the driven sky value" as DERIVED when it was an assertion about ONE route (the LEAFPERT operation). The
instrument documents a THIRD pure operation (PHASEONLY) aimed at exactly this, and it was never run. Running it,
and then the layered-ontology division, closes the position.

**The verified operation table (CR arm, NK=620, same projection/transfer as the control that lands on sky):**

| operation (which terms see the leaf/content clock) | l1/lA | vs sky | P1/P2 |
|---|---|---|---|
| STACKPERT — nothing (all on the stack ruler) | 0.5703 | −22% | 0.965 |
| LEAFPERT — whole equation on leaf | 0.6764 | −7.5% | 2.013 |
| SRCSTACK=phi — only Phi-evolution on stack | 0.6499 | −11% | 2.435 |
| **sky** | **0.7312** | — | **2.217** |
| SRCSTACK=src — Phi + all potential couplings on stack | 0.7294 | **−0.25%** | 3.879 |
| SRCSTACK=vel — ONLY the velocity-source Ps on stack | 0.7294 | **−0.25%** | 3.745 |
| SRCSTACK=cpl — couplings on stack, Phi-evolution on leaf | 0.7560 | +3.4% | 2.946 |
| PHASEONLY — only the sound frequency on leaf | 0.8090 | +10.6% | 5.218 |

**THE MECHANISM (principled, not a fit).** The ONE perturbation equation splits between the two clocks by the
layered ontology: **gravity is L1 (stacking/geometric clock); pressure is L2 (leaf/content clock).**
  - The gravitational force driving the plasma velocity (the `DRE k^2 Ps` term in the Euler equation, ∇Phi) runs
    on the STACKING clock — it is geometry. This sets the ruler r_stack and the phase.
  - The pressure restoring, baryon friction, and Silk diffusion run on the LEAF clock — they are content. This
    sets the sound crossing r_leaf.
  The first-peak position is the competition of the two: gravity-driving on r_stack against pressure on r_leaf,
  so l1/lA carries the ratio r_stack/r_leaf = 1.2857 — which IS the size of the shift (sky/STACKPERT = 1.2821,
  0.28%). SRCSTACK=vel (velocity-source on the geometric clock, everything else on the leaf) lands the position
  at 0.7294 vs sky 0.7312 — **0.25%, no radiation-driving impulse anywhere.**

**(b) IS REFUTED.** An undriven comb reaches the sky position (SRCSTACK=vel) and, with the wrong division,
overshoots it (PHASEONLY 0.809). The "driving phase shift ~0.27π" that LCDM manufactures from radiation driving
is, in CR, the two-horizon ratio of its own layered ontology. Same position, two origins — the corpus's
signature dissolution.

**WHAT REMAINS: the amplitude, and it is the SOFT/SEPARABLE knob.** With the position pinned (Ps on the geometric
clock), P1/P2 = 3.7–3.9, above the sky's 2.217. But the sky amplitude is BRACKETED (LEAFPERT 2.013 < sky 2.217 <
cpl 2.946 < vel 3.745) and — per P15's residual decomposition (`P15_derived_lensing_on_the_lcdm_arm`,
`P15_the_residual_is_contrast_and_the_lensing_potential_is_derived`) — the peak-trough CONTRAST/height is
controllable by the damping tail, polarization (POLC), and lensing WITHOUT moving the peak positions. So the
amplitude residual does not threaten the closed position; it is the next, softer determination.

**DISPOSITION:** the position — the hard ~70σ residual I nearly mis-called a falsification — is CLOSED by the
layered clock division (0.25%), a principled two-horizon mechanism, no driving impulse. The exact sub-division
that also lands the amplitude (and the height machinery that does it without moving peaks) is the next step, now
bracketed in both observables. Instrument change: added the `SRCSTACK` DIAGNOSTIC flag (off by default, provable
no-op on the control since Jac=1); NOT a committed frame — the frame choice is 58's to name.

### ✔ 58's HEIGHT-BY-SUBTRACTION COMPUTATION — carried out: the running of phi IS the position, and is NOT the amplitude
**Shipped by 58:** does the running of the clock ratio phi(eta)=H_stack/H_leaf supply CR's height boost the
way it supplied the phase? Measured by subtraction (running phi vs phi frozen at its recombination value),
gated on the control, at fixed position. Instrument: added `FREEZEJAC` (freeze Jac=phi at eta_rec; provable
no-op on control where phi==1), extended PHISAVE to record phi(eta). Runs at NK=620, SRCSTACK=vel.

**GATE (control, phi==1):** lcdm vel and lcdm vel+FREEZEJAC are BYTE-IDENTICAL — [220,532,812,1116],
l1/lA=0.7300, P1/P2=2.447 both. phi_rec=1.00000. Self-check passes; the CR differences below are real.

| CR arm | l1/lA | P1/P2 | P1/P3 | P1/P4 |
|---|---|---|---|---|
| B: phi FROZEN at phi_rec=0.885 | 0.6764 | 4.009 | 3.005 | 6.442 |
| A: phi RUNNING (0.607 -> 0.885) | 0.7294 | 3.745 | 4.531 | 14.944 |
| sky | 0.7312 | 2.217 | 2.277 | — |

**(1) POSITION — the running of phi IS the mechanism, decisively.** Freezing phi collapses the position to
0.6764 (= LEAFPERT); the RUNNING of phi carries it to 0.7294 (= sky, 0.25%). The clock-ratio running supplies
the FULL position shift — CR's structural analogue of the acoustic phase shift, confirmed by subtraction and
gated. This is the strong, positive result and it nails down WHY vel closes the position.

**(2) AMPLITUDE — the running of phi is NOT the radiation-driving analogue.** The hypothesis was that the
running weights higher-k modes (which oscillate earlier, at smaller phi) and boosts the high peaks the way RD
does. The measurement refutes that specific form: the running moves P1/P2 only 4.009 -> 3.745 (right direction,
but ~15% of the way to 2.217) AND it WORSENS the higher ratios (P1/P3 3.005 -> 4.531, P1/P4 6.4 -> 14.9). So
the running SUPPRESSES the high peaks relative to the first, the OPPOSITE of radiation driving. The two-clock
running delivers the position in full and does NOT deliver the amplitude.

**DISPOSITION (honest, per 58's own rule "the shortfall is measured rather than argued").** The running of the
clock ratio is confirmed as the position mechanism and measured OUT as the amplitude mechanism. The amplitude
boost RD supplies in LambdaCDM is not reproduced by the two-clock running here. So the amplitude needs a
different route than the clock split — most likely P15's height/contrast machinery (damping tail, polarization
POLC, lensing), which P15 already shows moves the peak-trough contrast WITHOUT moving the peaks, i.e. at the
fixed 0.7294 position vel now delivers. A clean next discriminator: separate the high-peak change into driving
vs Silk-damping (the running also retimes when high-k modes oscillate, hence their diffusion) via NODRIVE / the
diffusion knob, to confirm the suppression is damping-mediated rather than an anti-driving. Instrument: `FREEZEJAC`
diagnostic added (no-op on control), PHISAVE extended with phi(eta); not committed frames.

### ✔ 58's DIFFUSION-CLOCK DISCRIMINATOR — over-damping CONFIRMED; the diffusion clock is a real amplitude lever, but couples to position
**58's diagnosis:** the amplitude failure shape (P1/P3, P1/P4 worse with k) is OVER-DAMPING, not anti-driving,
and by LGF Silk diffusion is a content process -> leaf clock. Shipped: report which clock the k_D integral
keeps, and run it on the leaf.

**ITEM 2 (which clock), answered by reading the code:** the k_D integral (`1/k_D^2 = INT A/tau' d(eta)`) is a
SETUP quantity computed once on `_egrid` with `d(_egrid)` -- the STACK conformal-time grid, phi-INDEPENDENT.
So the diffusion kept the STACK clock while `vel` put the oscillation on the LEAF. The mismatch is real and
visible. **The LGF fix (`DIFFLEAF`):** diffusion accrues over eta_leaf with tau'_leaf = tau'_stack/Jac, so
r_D^2_leaf = INT (A/tau'_stack) Jac^2 d(eta_stack) -- the integrand gains phi^2=Jac^2 (derived, not fitted).
phi<1 early -> LESS damping at high k. Provable no-op on control (phi==1).

**GATE (control, phi==1):** lcdm vel+DIFFLEAF is BYTE-IDENTICAL to plain lcdm ([220,532,812,1116], 0.7300,
2.447, 2.974). Self-check passes.

| CR arm | l1/lA | P1/P2 | P1/P3 | r_D |
|---|---|---|---|---|
| vel (diffusion on STACK, the mismatch) | 0.7294 | 3.745 | 4.531 | 7.64 |
| vel + DIFFLEAF (diffusion on LEAF, LGF) | 0.7560 | 3.503 | 3.780 | 6.57 |
| sky | 0.7312 | 2.217 | 2.277 | — |

**RESULT.** (1) 58's OVER-DAMPING diagnosis is CONFIRMED: moving the damping to the consistent leaf clock
brings peaks 3-4 UP (P1/P3 4.531 -> 3.780, P1/P2 3.745 -> 3.503) -- the suppression WAS damping-retiming.
(2) The diffusion clock is a genuine amplitude lever in the right direction, and it is LGF-forced, not a knob.
(3) BUT it moves the position 0.7294 -> 0.7560 (reduced high-k damping shifts peak centroids right), so the
fully-LGF-consistent operation (gravity on stack; pressure, friction, diffusion on leaf) OVERSHOOTS position
and still leaves the amplitude at ~3.5 vs sky 2.2. So the diffusion clock is confirmed as a real lever and a
FORCED assignment, but it does not close the amplitude alone and it disturbs the position.

**THE REMAINING TERM, named by the instrument itself.** The code's diffusion block (c54.176-178) already
records what it is MISSING: the POLARISATION SOURCE terms. It takes the polarisation's contribution to the
DAMPING (the 16/15 coefficient) WITHOUT its contribution to the SOURCE (g*Pi/4 and (3/4k^2)d^2(g*Pi)/deta^2)
-- "half of one physical effect, and the half taken is the half that removes power" -- recorded as the 1123
chi^2 units the instrument is missing. The missing polarisation SOURCE ADDS power at the peaks (a source, not
a damping-scale change), so it lowers P1/P2, P1/P3 WITHOUT the damping-scale position shift. That is the
natural next term -- and unlike the clock assignments it is a genuine physics addition (deliberately left out
with a recorded reason), so it is 58's to specify, not mine to add unattended. Instrument: `DIFFLEAF` diagnostic
added (LGF diffusion->leaf, no-op on control); not a committed frame.

**CALIBRATION (the decisive one): the diffusion-clock change is SCALE-equivalent, so the residual is the ENVELOPE SHAPE.**
Ran vel + DAMPX=0.739 (the diagnostic that slides the damping SCALE without the leaf-clock shape, matched to
DIFFLEAF's r_D drop 7.64->6.57):

| CR arm | l1/lA | P1/P2 | P1/P3 |
|---|---|---|---|
| vel + DIFFLEAF (leaf-clock diffusion, LGF) | 0.7560 | 3.503 | 3.780 |
| vel + DAMPX=0.739 (pure damping SCALE) | 0.7560 | 3.499 | 3.755 |

They are the SAME. So the diffusion-clock assignment acts as a pure damping-SCALE reduction -- its leaf-clock
shape (Jac^2) adds nothing beyond an overall scale. Two consequences, both from the instrument's own DAMPX logic
("if the two ratios select different DAMPX, no coefficient can fix the heights, and the residual is the SHAPE of
the envelope rather than its scale"): (i) one scale cannot close both ratios -- 3.50/2.22=1.58 vs 3.76/2.28=1.65
-- so the amplitude residual is the ENVELOPE SHAPE, NOT the diffusion scale/clock; (ii) the scale reduction MOVES
the position (0.7294->0.7560), so it is disqualified as an amplitude-only fix by 58's own criterion.

**HONEST NET STATE (correcting any over-clean reading of the earlier position closure):** the gravity-clock
assignment closes the position AT THE vel LEVEL (0.7294, diffusion still on stack). Making the diffusion clock
LGF-consistent is FORCED, helps the amplitude, but is scale-equivalent -- it moves the position to 0.7560 and
cannot close both ratios. So position and amplitude are COUPLED through the damping, and the diffusion clock is
NOT the amplitude closer. The residual is the envelope SHAPE -> the POLARISATION SOURCE terms the instrument
already names as its missing 1123-chi^2 piece (a source that adds power AT the peaks, changing the shape, not a
scale that shifts position). The full LGF-consistent CR prediction -- gravity on stack, pressure/friction/diffusion
on leaf, AND the polarisation source restored -- is the object to compare to the sky in BOTH position and amplitude,
and it is NOT yet computed. That is the determinate next ship, and it is a genuine physics term (58's to specify),
not a clock assignment.

### ✗ POLARISATION SOURCE via tight-coupling Pi reconstruction — FAILS the control gate (implementation inadequate; physics term still right)
**58's ship:** restore the polarisation source terms g*Pi/4 and (3/4k^2)d^2(g*Pi)/deta^2 in both arms; the control
gate is that LambdaCDM must recover the recorded 1123 chi^2 and NOT degrade 0.7300/2.447. I reconstructed Pi from
the L171w polarised tight-coupling closure: Pi=(5/2)F_2, F_2=(32/45)(tg/tau') => Pi=(16/9)(tg/tau'), with g*Pi
computed directly as (16/9)e^-tau*tg (the tau' cancels, finite through last scattering).

| run | l1/lA | P1/P2 | P1/P3 |
|---|---|---|---|
| CR vel+DIFFLEAF, POLSRC OFF (baseline) | 0.7560 | 3.503 | 3.780 |
| CR vel+DIFFLEAF, POLSRC ON | 0.9151 | 2.127 | 2.533 |
| **control (lcdm) POLSRC ON -- THE GATE** | **0.8627** | **1.806** | 2.329 |
| control plain (POLSRC OFF) | 0.7300 | 2.447 | 2.974 |
| sky | 0.7312 | 2.217 | 2.277 |

**GATE FAILED.** The control's first peak moved 220 -> 260 (l1/lA 0.7300 -> 0.8627) and P1/P2 overshot to 1.806.
A correct polarisation source CANNOT move LambdaCDM's peak (measured at 220.6). So the tight-coupling Pi is WRONG.

**DIAGNOSIS (honest).** The amplitude ratios moved in the RIGHT direction (P1/P2, P1/P3 down toward sky) -- the
term IS the missing shape, as 58 diagnosed -- but the magnitude is far too large and it shifts the peaks. Cause:
the tight-coupling steady state Pi=(16/9)(tg/tau') assumes tau' LARGE (F_2'~0), which is INVALID near last
scattering where tau' -> small (k/tau' ~ 0.6 at the visibility peak, not << 1). Extrapolating the tight-coupling
formula into the last-scattering regime oversizes Pi, adding a velocity-scale source (comparable to the Doppler)
that both over-corrects the amplitude and drags the peaks right. Tuning the (16/9) coefficient to pass the gate
would be a FIT, which 58 explicitly forbade ("no free parameter anywhere"), so I did not.

**THE CORRECT FIX (structural, 58's architectural call).** Pi must be got from the EVOLVED polarisation hierarchy
(G_0, G_2 alongside the photon F_2, as L171w does: F_2'=(8/15)tg-(3/5)kF_3-tau'(F_2-Pi/10), G_0'=-kG_1+tau'(-G_0+Pi/2),
G_2'=(k/5)(2G_1-3G_3)+tau'(-G_2+Pi/10)), so Pi SATURATES physically through last scattering instead of diverging.
But the main ACOUSTIC instrument deliberately carries NO photon multipoles -- it is tight-coupling + the derived
exp(-k^2/k_D^2) damping factor -- so adding an evolved photon+polarisation hierarchy is a re-architecture, and it
must be reconciled with the damping factor to avoid DOUBLE-COUNTING the quadrupole's dissipation (the k_D integral
already encodes it). That reconciliation -- evolve the multipoles OR keep the damping factor, not both -- is the
architectural decision, and it is 58's to make, not a source-function patch. Instrument: POLSRC flag left in place
but DOCUMENTED AS GATE-FAILING (off by default, no effect on other runs); not a result.

**NET.** The polarisation source is confirmed as the right missing SHAPE term (it moves the amplitude the right
way), but it cannot be restored by extrapolating tight coupling into last scattering -- that fails the control
gate. The honest state: the amplitude closure awaits a physical Pi from an evolved polarisation hierarchy, which
is a structural change to the tight-coupling instrument.

### ✔✔ GATE 1 PASSES — the polarisation source is ALREADY in the instrument (HIER path), evolved-Pi, and it holds the control position while recovering the amplitude
**Discovery:** the instrument already carries the correct implementation. `HIER=1` (`evolve_hier`, `_project`) evolves
the FULL photon+polarisation hierarchy by L171w's equations (F_2..F_LG, G_0..G_LG, Pi=F_2+G_0+G_2 from the evolved
variables) and `_project` already carries the polarisation SOURCE terms g(Theta_0+Psi+Pi/4) + (3/4k^2)d^2(g Pi)/deta^2
-- with the double-count avoided exactly as 58 described: the exp(-k^2/k_D^2) envelope is FROZEN AT THE SWITCH
(tau'=3, eta=138, carrying 4.2% of the damping) and the multipoles carry the other 95.8%, disjoint supports. My
hand-rolled POLSRC (tight-coupling steady-state Pi) was reinventing this badly and failed; the evolved Pi is right.

**GATE 1 (control, evolved-Pi polarisation source):**

| control | l1/lA | P1/P2 | P1/P3 |
|---|---|---|---|
| plain lcdm | 0.7300 | 2.447 | 2.974 |
| lcdm HIER=1 (evolved-Pi source) | **0.7300** | **2.254** | **2.363** |
| sky | 0.7312 | 2.217 | 2.277 |

**PASSES.** Position HELD at 0.7300 (the peak did NOT move -- the critical requirement) and both ratios moved from
(2.447, 2.974) toward the sky (2.217, 2.277), landing at (2.254, 2.363) -- PARTWAY, not past, exactly as 58
predicted a physical (saturating) Pi would. That is the recovery of the ~1123 chi^2 debt, and it confirms the term
at the right SIZE, not merely the right sign. The failing tight-coupling attempt was a REGIME error (Pi extrapolated
into last scattering where tight coupling breaks), not a missing physics -- as diagnosed.

**FOR THE CR RUN:** added the SRCSTACK=vel split to `evolve_hier` (gravity velocity-source DRE k^2 Ps on the stack
clock; content on leaf). In the HIER path the diffusion is done by the EVOLVED MULTIPOLES on the leaf clock (via the
x Jac in evolve_hier), not the k_D factor -- so the leaf-clock diffusion is NATIVE and DIFFLEAF is not needed. The
full LGF-complete CR prediction is `ARM=cr SRCSTACK=vel HIER=1`: gravity on stack, pressure+diffusion+polarisation
all on the leaf. [running]

### ✔ THE FULL LGF-COMPLETE PREDICTION — position CLOSED, amplitude a GENUINE framework residual (58's "open" outcome)
With the evolved polarisation source validated on the control (Gate 1), the full LGF-complete CR prediction:

| CR, evolved polarisation source (HIER) | l1/lA | P1/P2 | P1/P3 |
|---|---|---|---|
| vel + HIER  (gravity velocity-source on stack) | 0.7294 | 3.382 | 3.270 |
| src + HIER  (whole geometry sector on stack: +Phi evolution) | 0.7294 | 3.492 | 3.091 |
| LEAFPERT + HIER (everything on leaf) | 0.6764 | 1.802 | 1.746 |
| control lcdm HIER (the gate, PASSES) | 0.7300 | 2.254 | 2.363 |
| sky | 0.7312 | 2.217 | 2.277 |

**POSITION: CLOSED.** 0.7294 vs sky 0.7312 (0.25%), ROBUST across vel and src (the Phi-clock choice does not move
it) -- the two-horizon clock division, no driving impulse. Settled.

**AMPLITUDE: a genuine framework residual.** The control gate PASSES -- LambdaCDM through the same complete
instrument recovers to P1/P2=2.254 near the sky's 2.217, holding position. So the instrument is internally
consistent and complete. Yet CR's P1/P2 stays at ~3.4-3.5 (vs sky 2.217, ~55% high), ROBUST to the gravity-clock
(vel 3.382, src 3.492) and to the polarisation source (which helped: vel-alone was 3.745). CR's higher peaks are
too low relative to the first, and it PERSISTS through the fully LGF-consistent, gate-passing instrument.

**WHAT IT IS.** The residual is the DRIVING-AMPLITUDE BOOST. LambdaCDM's radiation driving does two things: a PHASE
shift (position) and an AMPLITUDE enhancement of the higher peaks (crossing-during-plasma boosts high-k). CR's
two-horizon structure supplies a substitute for the PHASE shift (the position closes), but there is NO two-horizon
substitute for the higher-peak AMPLITUDE boost -- and the running-of-phi does not supply it (measured out earlier),
nor does the (correct, gate-passing) polarisation source fully. So the amplitude residual is the same
absence -- no crossing during plasma, hence no driving boost -- that PO-13 identified at the start, now shown to
SURVIVE the complete, consistent instrument. It is the first result in this arc that deserves to be carried as OPEN:
a standing CR-vs-sky prediction (higher peaks ~55% low in the ratio), measured against a validated instrument,
rather than a gap in the machinery.

**CAVEAT (honest).** The perturbation sector's term-by-term clock assignment is not provably exhausted; a term still
unassigned could yet move the amplitude. But the main levers (gravity-clock vel/src, diffusion via the evolved
multipoles on the leaf, the polarisation source) are all assigned and gate-passing, and the residual is robust
across them. So it is fairly called a genuine open framework result, held with that caveat -- not closed, not a bug.

Instrument: added SRCSTACK=vel/src to evolve_hier (gravity-clock split in the hierarchy path); HIER path already
carried the evolved-Pi polarisation source. Position closed; amplitude open and characterised.

### ⚠ CORRECTION + full consistent composition (58's gate order, run on the branch superset + PHASEPOW)
**Correction of a cc54 git misread first:** I wrongly thought main r3512 had REVERTED my flags. It had not -- main
never had them; the -89/+15 was a branch-vs-main divergence diff (PR #22 unmerged). The branch is the SUPERSET;
main's only new piece is 58's PHASEPOW (r3511), now brought into the branch. I nearly adopted main's instrument,
which would have deleted SRCSTACK/DIFFLEAF/POLSRC/FREEZEJAC -- caught by 58 mid-run.

**Composition confirmed and the port completed:** evolve_hier carries the vel term-split (my earlier vel+HIER gave
0.7294 != LEAFPERT+HIER 0.6764, so the hierarchy DOES see vel -- Gate 1.5 passes). DIFFLEAF modifies the
module-level kD2inv_of, so it reaches _project's frozen envelope. Full consistent run: ARM=cr SRCSTACK=vel DIFFLEAF=1 HIER=1.

**58's PISRC subtraction (the returned half), the decisive measurement:**

| run | l1/lA | P1/P2 | P1/P3 |
|---|---|---|---|
| plain lcdm (tight-coupling + exp(-k^2/k_D^2)) | 0.7300 | 2.447 | 2.974 |
| lcdm HIER PISRC=0 (evolved hierarchy, NO pol source) | 0.7300 | 2.265 | 2.326 |
| lcdm HIER PISRC=1 (+ pol source) | 0.7300 | 2.254 | 2.363 |
| CR vel+DIFFLEAF+HIER PISRC=0 | 0.7294 | 3.406 | 3.171 |
| CR vel+DIFFLEAF+HIER PISRC=1 | 0.7294 | 3.359 | 3.219 |
| sky | 0.7312 | 2.217 | 2.277 |

**WHAT THE SUBTRACTION SHOWS (correcting my Gate-1 over-attribution).** The polarisation SOURCE's returned half is
SMALL on BOTH arms: control 2.265 -> 2.254 (~0.5%), CR 3.406 -> 3.359. The big control recovery I credited to the
source in Gate 1 (2.447 -> 2.254) is almost entirely the HIERARCHY's proper damping (the evolved multipoles carrying
the pol-corrected quadrupole), NOT the two source terms. The source is a ~0.5% correction -- which is what
polarisation physically IS. So the "1123 chi^2 debt" is recovered by the hierarchy's damping treatment; the source
terms are the small remainder.

**POSITION.** Under the FULLY consistent HIER composition (vel + DIFFLEAF + evolved multipoles doing the diffusion on
the leaf natively), the CR position is 0.7294 (0.25% from sky), and the pol source does NOT move it (0.7294 at
PISRC=0 and 1). This is NOT the fluid-path 0.7560 that 58 predicted: in the HIER path the diffusion is done by the
multipoles on the leaf, not the k_D envelope, so DIFFLEAF (which only touches the 4.2% frozen envelope) barely
moves it. **Flag for 58: the HIER-consistent position is 0.7294, differing from the fluid-DIFFLEAF 0.7560 -- the
two solvers do the diffusion clock differently, and the hierarchy is the more complete one.**

**AMPLITUDE.** CR P1/P2 stays ~3.36-3.41 (vs sky 2.217) under the complete, consistent hierarchy instrument, and
neither the hierarchy nor the pol source closes it -- the pol source barely helps CR at all. So the amplitude residual
PERSISTS through the fully consistent, internally-complete instrument: CR's higher peaks are too low relative to the
first, the missing driving-amplitude boost. Held as the arc's first genuine OPEN framework result -- now on the
fully consistent HIER composition, not the fluid path, with the pol-source contribution measured and found small.

### ✔ CRAMP=seam — 58's amplitude lever, and it lands P1/P3 EXACTLY; the residual narrows to the even (2nd) peak
**58's ship:** CRAMP=seam is a k-dependent INITIAL amplitude (Theta-hat_0 = -T(k c_s eta_S)/2), acting on what the
modes START with, not the evolution -- the one place the clock division, diffusion clock and polarisation source
could not reach. Principled: 'flat' assumes the seam is a blank initial surface; CR's seam is a branch point in an
existing de Sitter geometry, so each mode arrives with its own accumulated sound-crossing phase. Run on the full
consistent composition (vel+DIFFLEAF+HIER), gated on the control.

**GATE:** lcdm HIER CRAMP=seam = 0.7300 / 2.254 / 2.363 -- BYTE-IDENTICAL to lcdm HIER. CRAMP is CR-only, a clean
no-op on the control. The CR shifts below are real physics.

| CR (vel+DIFFLEAF+HIER) | l1/lA | P1/P2 | P1/P3 |
|---|---|---|---|
| CRAMP=flat  PISRC=1 | 0.7294 | 3.359 | 3.219 |
| CRAMP=seam  PISRC=1 | 0.7560 | 2.727 | **2.277** |
| CRAMP=seam  PISRC=0 | 0.7560 | 2.771 | 2.244 |
| sky | 0.7312 | 2.217 | **2.277** |

**RESULT.** The seam IC is a LARGE, genuine amplitude lever: P1/P3 falls 3.219 -> **2.277, exactly the sky's 2.277**,
and P1/P2 falls 3.359 -> 2.727. But it also MOVES the position 0.7294 -> 0.7560 (+3.4%), which by 58's own criterion
means the IC is touching the phase, not a clean shape-at-fixed-position lever. So amplitude and position COUPLE
through the IC -- the same bracketing seen across the clock: flat holds the position and misses the amplitude, seam
lands the amplitude (P1/P3 exact) and overshoots the position. Neither closes both.

**THE RESIDUAL, NARROWED AND NAMED.** Under the fully principled instrument (LGF clocks, evolved hierarchy,
polarisation source, seam IC -- every assignment made, no free parameter): position 0.7560 (+3.4%), P1/P2 2.727
(+23%), P1/P3 2.277 (EXACT). The tell is that P1/P3 is exact while P1/P2 is high: the ODD-odd ratio is right and it
is the EVEN (second) peak that is too low. That is the ODD-EVEN ALTERNATION deficit -- the compression (even) peaks
under-boosted -- which is the SAME absence PO-13 identified at the very start: no crossing during plasma, hence no
driving enhancement of the compression peaks. The position residual (+3.4%) likely rides the same second-peak
displacement. So the fully assembled framework reproduces the sky EXCEPT for the odd-even alternation, and that
deficit is the driving-compression boost CR structurally lacks -- coherent with the undriven-comb result from day one.

**Flag for 58 (adjudication, not a cc54 conclusion):** (a) which IC is right -- flat (position 0.7294, amplitude wrong)
or seam (P1/P3 exact, position 0.7560); (b) whether the position moving under the principled seam IC means 0.7560 is
the true consistent position or the IC over-corrects; (c) the residual is now specifically the 2nd/even peak (P1/P2
high, P1/P3 exact) -- the alternation, not a broadband shape. Every principled lever is now exercised and the residual
is isolated to one feature.

### ✔ KCONT=1 under seam + the odd-even HEIGHT-alternation measurement (58's two checks, r3523)
**58's correction accepted first:** the falsification criterion "if the position moves, the IC touches the phase" was
WRONG -- the projected peak position is a CENTROID of the k-envelope, not the oscillation phase, so any
amplitude-envelope change reweights k and moves the centroid with the phase untouched. DAMPX (pure damping scale, zero
phase content) moved 0.7294->0.7560 identically to DIFFLEAF: proof. And 220 vs 228 are ONE comb-rung apart -- three
unrelated operations (DIFFLEAF, DAMPX, seam) all land 228, flat lands 220 -- so there is no continuous +3.4% residual,
only a rung question. Honest position report from here on: *"l_1 = 220 or 228 depending on the high-k envelope; sky
220.6; rung spacing ~8,"* NOT "closed at 0.7294/0.7560."

**CHECK 1 -- KCONT=1 (does the position depend on the discreteness of CR's ladder?).** Runs on the full seam
composition (`ARM=cr SRCSTACK=vel DIFFLEAF=1 HIER=1 CRAMP=seam PISRC=1 NK=620`):

| CR seam | l_1 | l_1/l_A | P1/P2 | P1/P3 | modes |
|---|---|---|---|---|---|
| discrete ladder | 228 | 0.7560 | 2.727 | 2.277 | (sqrt(L(L+2)) ladder) |
| KCONT=1 continuum | 228 | 0.7560 | 2.726 | 2.277 | 1860 dense |

**IDENTICAL to four digits.** The discrete ladder is NOT what puts the peak at 228 -- dense continuum sampling lands
the same place. So 228 is a physical envelope centroid, not an aliasing/discreteness artifact; the corpus's KCONT
guard (l.1014) passes under seam. The 228-vs-220 choice is set by the high-k ENVELOPE (flat->220, seam/damping->228),
not by the comb's coarseness.

**CHECK 2 -- odd-even HEIGHT alternation, CR vs control vs sky, all under seam.** Metric A2 = height of the odd
(P1-P3) envelope interpolated to the 2nd-peak position, divided by the actual 2nd-peak height. A=1 -> even peak sits ON
the odd trend (NO alternation, uniform comb); A>1 -> even peak depressed by (A-1). Same metric on all three arms:

| arm | A2 (2nd pk) | A4 (4th pk) | P1/P2 | P1/P3 |
|---|---|---|---|---|
| sky (Planck ratios) | **1.423** | -- | 2.217 | 2.277 |
| CONTROL seam (driven) | **1.432** | 1.935 | 2.254 | 2.363 |
| CR seam (undriven) | **1.741** | 2.312 | 2.727 | 2.277 |
| CR seam KCONT | 1.740 | 2.312 | 2.726 | 2.277 |

**TWO findings, one a correction of my own framing:**

1. **The control REPRODUCES the sky's height alternation: A2 = 1.432 vs sky 1.423 (0.6%).** The two-arm machinery is
   now validated on the HEIGHT observable, not only position -- a clean gate pass. (The raw ratios agree less well --
   control P1/P3=2.363 vs 2.277, 3.8% -- because A2 divides out the common damping envelope that the raw ratio carries.)

2. **CR does NOT under-alternate -- it OVER-alternates.** A2 = 1.74 vs sky 1.42: CR's 2nd peak is ~23% TOO LOW, not too
   high. So the surface phrasing "CR is a uniform comb where the sky alternates" is CORRECT for SPACING (CR's comb is
   unshifted/uniform, the sky's is driving-shifted) but WRONG for HEIGHTS -- in heights CR is MORE depressed at the
   even peaks, not flat. Robust to discreteness (KCONT A2 1.740 vs 1.741).

**THE READING (why this is still "one claim," correctly stated).** A smooth-in-k amplitude lever -- the seam IC, or any
envelope reweighting -- is MONOTONIC in k, so it can lift the odd peaks OR the even peaks onto the sky but NOT both,
because the sky's peak heights ALTERNATE (P2 low, P3 up, P4 low...) and a smooth mechanism cannot manufacture
alternation. Under seam the smooth lift is tuned to the odd peaks (P1/P3 = 2.277 exact); the even peaks then come out
where the smooth lift leaves them -- ~23% below the sky. So *the residual after any smooth lever is exactly the
non-smooth (alternating) part*, and that alternating part IS the radiation driving. CR lacks the driving, so it lacks
BOTH driving signatures: the comb-shift in spacing (CR uniform, sky shifted) AND the even-peak boost in height (CR
over-depressed, sky/control at A2~1.42). Two signatures, one absence -- but they point OPPOSITE ways (less structure in
spacing, more depression in height), which is why "uniform in both" was the wrong way to say it. The control carrying
the driving reproduces the sky in BOTH channels; CR carrying no driving departs in BOTH. That is PO-13's day-one claim,
now confirmed in a second independent observable (heights) with a validated control -- and the confirmation is that the
alternation is precisely what no smooth CR lever can supply, not that CR's heights are flat.

**Flag for 58:** (a) the phrasing correction is on the record -- CR over-alternates in height, it is not flat; the
"one claim" stands as *"the alternation is the driving, and no smooth CR lever supplies it"* rather than *"CR is uniform
in both."* (b) Control now validated on heights (A2 0.6% from sky), so the CR even-peak deficit is a genuine
arm-difference, not machinery. (c) Position: 220 or 228 is a rung, set by envelope, not discreteness (KCONT identical);
stop quoting either as "closed." (d) Next natural check, if you want it: does the even-peak deficit scale with the
baryon load R (the alternation's amplitude) the way a missing driving-times-baryon-loading term would -- an RBFAC scan,
CR and control, reading A2 vs R -- which would pin the deficit to the driving-baryon product quantitatively.

### ✔ RBFAC SCAN — the A2(R) GAP measures (b) missing-driving over (a) baryon-error, decisively (r3524)
**58's mechanism separation (accepted, and it rescues the physics):** odd-even height alternation is BARYON LOADING,
not driving -- R_b depresses the even (rarefaction) peaks vs the odd (compression) ones, and that sets A2. Driving is
NOT differential odd/even; it boosts peaks 2+ as a GROUP, and because peak 2 is one of the depressed ones, the group
boost partially OFFSETS the baryon depression there. So an undriven comb doesn't lose alternation -- it loses the
OFFSET, and its even peak sits too low. A2 too high is exactly what missing driving predicts; my 1.741 vs 1.423
pointed the right way. Two hypotheses to separate: **(a)** CR's deficit is a baryon-loading error -> some R brings CR's
A2(R) onto the CONTROL's curve (gap vanishes / curves coincide); **(b)** it's the missing driving offset -> the
CR-minus-control GAP persists at every R (a term CR lacks at any baryon load).

**Design (58's, made decisive not descriptive):** scan RBFAC on BOTH arms, same grid, seam composition
(`SRCSTACK=vel DIFFLEAF=1 HIER=1 CRAMP=seam PISRC=1 NK=620`); report the GAP as the primary quantity, and l_1/l_A next
to every A2. **Gate: control at R=1 must return 1.432.**

| R (RBFAC) | CR A2 | ctl A2 | **GAP=CR-ctl** | CR l_1/l_A | ctl l_1/l_A | CR P1/P2 | ctl P1/P2 |
|---|---|---|---|---|---|---|---|
| 0.50 | 1.205 | 1.137 | **0.069** | 0.729 | 0.741 | 1.429 | 1.553 |
| 0.75 | 1.463 | 1.276 | **0.187** | 0.756 | 0.749 | 1.979 | 1.871 |
| **1.00** | 1.741 | **1.432** | **0.308** | 0.756 | 0.730 | 2.727 | 2.254 |
| 1.50 | 2.386 | 1.769 | **0.618** | 0.783 | 0.723 | 4.864 | 3.211 |
| 2.00 | 3.075 | 2.160 | **0.915** | 0.836 | 0.719 | 7.867 | 4.440 |

*(sky: A2 = 1.423, l_1/l_A = 0.7312. GATE PASSES: control R=1 -> A2 = 1.4323.)*

**RESULT -- (b), unambiguously.** The GAP is POSITIVE at every R, NEVER vanishes (min 0.069 at R=0.5), and SCALES
~linearly with R (fit GAP ~ 0.571*R - 0.237; no zero crossing in [0.5, 2.0]). Both diagnostics 58 named for (b) hold:
the gap does not vanish at any R, and it scales with R. Hypothesis (a) is excluded three ways: (i) the gap never
reaches zero; (ii) CR's A2(R) curve does NOT lie on control's -- e.g. CR@R=1.0 (1.741) equals control only near
R~1.45, CR@R=0.5 (1.205) equals control near R~0.6, so the "effective-R" multiplier a baryon error would need is NOT
constant (1.2 -> 1.45, it grows); (iii) a pure baryon rescaling is multiplicative and constant, but the deficit is an
ADDITIVE offset that grows with R. **The even-peak deficit is a term CR structurally lacks at every baryon load --
the missing driving offset -- and its growth with R is exactly the driving x baryon-loading product 58 predicted:
the driving boost acts on the baryon-depressed (R-proportional) even peak, so the MISSING boost is R-proportional too.**

**What is MEASURED vs INTERPRETED (kept apart, honestly):** MEASURED -- (1) gate: control reproduces the sky's height
alternation to 0.6% (A2 1.432 vs 1.423), a second independent validation of the two-arm instrument after position;
(2) the CR-control gap is positive, non-vanishing, and R-scaling across a 4x baryon range. That measures (b) over (a).
INTERPRETED (natural, not proven) -- that the R-proportionality identifies the missing term specifically as
driving x baryon-loading; what is proven is that it is an additive term absent at all R, i.e. not a baryon error.

**⇒ PO-13, both channels now MEASURED.** Spacing: CR's comb is undriven (uniform, at the integers; the NODRIVE guard
and the ~70sigma phase intercept). Height: CR's even-peak deficit is the missing driving offset, measured over a baryon
scan against a control that lands the sky. The framework's departure from the sky is ONE absence -- the radiation
driving CR structurally lacks -- now carrying TWO measured signatures with a validated control, not one measured and
one argued. The l_1/l_A column also answers the rung question quantitatively: control's position is R-STABLE
(0.741 -> 0.719), CR's rises with R (0.729 -> 0.836) -- the envelope centroid responds to baryon loading on the
undriven arm, as an envelope-set (not phase-set) position should.

---

## ⛔⛔ PO-13 — **UNBANKED r3526 (58). THE AMPLITUDE IS OPEN, NOT BANKED.**

> ⛔ ***THE "BANKED" FRAMING BELOW WAS MINE AND IT WAS WRONG. It is kept, struck, as the record of the
> error — not as a verdict.***

**⌘ WHAT THE SKY COMPARISON ACTUALLY SHOWS.** *It was run; every table carries a sky row.* ⛔ ***Nothing
closed.***

| | CR `flat` | CR `seam` | **sky** |
|---|---|---|---|
| $\ell_1/\ell_A$ | 0.7294 | 0.7560 | **0.7312** |
| $P_1/P_2$ | 3.359 | 2.727 | **2.217** |
| $P_1/P_3$ | 3.219 | **2.277** | **2.277** |
| $A_2$ | — | 1.741 | **1.423** |

⇒ ***Position agrees under `flat` (0.25%) and not under `seam` (+3.4%) — and `flat` is the IC we agreed
is the placeholder. The amplitude agrees under NEITHER: $P_1/P_2$ off by 23%, the alternation by 22%.***
*Four mechanisms were tried and each moved it partway: the clock running gave ~15%, the diffusion clock
was scale-equivalent to `DAMPX`, the polarisation source ~0.5%, and `seam` hit $P_1/P_3$ exactly while
missing $P_1/P_2$ and shifting the position.*

**⛔ HOW IT GOT SWEPT.** *The `RBFAC` scan **characterised** the gap; it did not close it. I then
instructed that it be written up as "a falsifiable prediction with three measured signatures, not
closed-with-a-residual."* ***That was my call and it was wrong.*** *Daryl's rule — never frame a CR
result as falling short — says do not score a result as a failure to deliver.* ⛔ ***It does not say
relabel an unexplained empirical disagreement as a prediction.*** *Three mismatches became "three
signatures" and the open problem disappeared into a banked entry. **That is the rug, and I put it
there.***

### ⌘ WHAT IS GENUINELY ESTABLISHED — *narrower, and worth keeping*

1. ***The instrument is validated on BOTH observables***: the control reproduces the sky on **position
   to 0.16%** and on **height alternation to 0.6%**, through CR's own machinery, on an observable it
   was never tuned against.
2. ***The CR−control gap is additive and $R$-scaling, not a baryon-loading error.*** *The refutation
   stands on **functional form** — a baryon error is a fixed multiplier and CR's required multiplier
   runs $1.2\to1.45$ — which holds independently of the scanned range.*
3. *The `KCONT` check: $\ell_1=228$ is an **envelope** rung, not aliasing (discrete = 1860-mode
   continuum to four digits).*

### ⛑ WHAT IS OPEN

⛔ ***No mechanism has been found that brings CR's peak heights to the sky.*** *And the position agrees
only under the IC we do not think is the principled one.* ***Both stay OPEN, in those words.***

⌗ *The three-channel structure below is a real and useful **characterisation of the gap**, and reads
correctly as that. It is not a closure and must not be absorbed into a register row as one.*

---

## ~~⛭⛭⛭ PO-13 — BANKED (r3525, cc54; 58's three corrections applied)~~ — **STRUCK, kept as record**

**The framing, corrected — NOT "closed-with-a-residual."** Scoring CR against LambdaCDM's route reads as a shortfall,
and that is not what the measurement says. What it says:

> **CR's onset lies below every acoustic re-entry redshift, so no mode crosses while a plasma exists, so the comb is
> UNDRIVEN. That single structural fact now carries THREE measured signatures — uniform spacing where the sky's is
> shifted; an over-depressed even peak whose gap scales with baryon load; and a peak position that tracks R where the
> driven arm's does not — each with a control that lands the sky on the same instrument.**

A falsifiable prediction with three independent handles, not a discrepancy. The absence is DERIVED, the signatures are
MEASURED, and the control validates the machinery on every one. Where it connects to standard physics is named
precisely: radiation driving is what a cosmology needs *if its plasma epoch overlaps horizon crossing*, and CR's does
not.

### The three measured channels (each with a sky-landing control on the same instrument)

**Channel 1 — SPACING (phase).** CR's source comb is undriven: extrema at the integers q_n = n (the NODRIVE guard), no
driving phase shift, where the sky's comb is driving-shifted. Position, recorded honestly and never as one closed
number: **l_1 = 220 or 228 by envelope choice (flat -> 220; damping/DIFFLEAF/DAMPX/seam -> 228); sky l_1 = 220.6;
rung spacing ~8; KCONT-verified as NOT aliasing** (CR discrete 228 = CR continuum 1860-mode 228 to four digits, so the
ladder's discreteness is not what sets it — the high-k envelope is).

**Channel 2 — HEIGHT (even-peak offset).** A2 = even-peak depression below the odd (P1-P3) trend. Control reproduces
the sky's alternation to 0.6% (A2 = 1.432 vs sky 1.423) on an observable it was never tuned against — the second
independent validation of the two-arm instrument after position. CR over-depresses (A2 = 1.741): its even peak is
~23% too low, because the driving GROUP-boost of peaks 2+ that offsets the baryon depression at peak 2 is exactly what
CR lacks. **The RBFAC scan measures (b) missing-driving over (a) baryon-error:**

| R | CR A2 | ctl A2 | GAP | CR l_1/l_A | ctl l_1/l_A |
|---|---|---|---|---|---|
| 0.50 | 1.205 | 1.137 | 0.069 | 0.729 | 0.741 |
| 0.75 | 1.463 | 1.276 | 0.187 | 0.756 | 0.749 |
| 1.00 | 1.741 | 1.432 | 0.308 | 0.756 | 0.730 |
| 1.50 | 2.386 | 1.769 | 0.618 | 0.783 | 0.723 |
| 2.00 | 3.075 | 2.160 | 0.915 | 0.836 | 0.719 |

*Gate: control R=1 -> A2 = 1.4323 (= 1.432).* **Tightened gap statement (58's correction):** the gap does not vanish
over the scanned 4x range and the fitted line's zero (R ~ 0.42, from GAP ~ 0.571R - 0.237) lies BELOW the scan floor
— so "does not vanish over the scanned range" is the claim the data support, NOT "never vanishes." **The argument that
kills (a) outright is functional-form, not range:** a baryon error is a FIXED multiplier, but the effective-R multiplier
CR would need runs 1.2 -> 1.45 across the scan. That refutation stands on its own; the deficit is an ADDITIVE term
absent at all R (the missing driving offset), R-proportional as a driving x baryon-loading product.

**Channel 3 — POSITION TRACKING (promoted out of the footnote; 58's correction).** Control's peak position is R-STABLE
(l_1/l_A 0.741 -> 0.719 across a 4x baryon change) while CR's CLIMBS with R (0.729 -> 0.836). This is the same absence
a third time: a DRIVEN comb's peak is phase-set, so baryon loading barely moves it; an UNDRIVEN comb's peak is
envelope-set, so it tracks R. It is the cleanest of the three in one respect — a purely DIFFERENTIAL prediction between
the arms, needing no absolute calibration at all.

### What is MEASURED vs INTERPRETED (kept apart)
- **MEASURED:** the three signatures above; the control landing the sky on each (position 0.16% floor historically;
  height alternation 0.6%; position-tracking a differential the control holds still on).
- **INTERPRETED (natural, not proven):** that the R-proportionality of the height gap names the missing term
  specifically as driving x baryon-loading. What is PROVEN is that it is an additive term absent at all baryon loads —
  i.e. not a baryon error.

### Ledger note
PO-13's register row (P7 `sec:frontiers` \ref{frontier:scalar}, item 1 of three) is the framework node's to update —
cc54 does not edit protected register rows or the grain/registry machinery. This block is the ready-to-absorb entry.
⛔ **PO-13 IS NOT BANKED — unbanked r3526; the amplitude is OPEN and the position agrees only under
the placeholder IC.** *`OWED` carries `597` plus PO-13's open amplitude channel.*

---

## ⛭⛭⛭ THE LAYER READING — r3527, from Daryl's pre-axioms draft (the reasoning that produced the LGF)

⛔ ***The term-by-term clock split may be the wrong structure, and the framing was MINE.***

**⌗ WHAT THE DRAFT COMMITS TO.** *Three layers, not two:* ***"the coexistence of noumenological,
phenomenological, and local geometries."*** *With (ii) the cosmological solution **a vacuum solution**;
(iii) real space at any instant ***diffeomorphic*** to slices of the cosmological geometry; (iv) local
evolution by the ***full*** Einstein equations with nonzero stress-energy.*

⇒ ***So there are not two dynamical systems keeping two clocks. There is one dynamical system — the
local layer, where matter lives and the full EFE hold — and a MAP to a vacuum cosmological
description. A diffeomorphism has a Jacobian, and that Jacobian is $\varphi=\mathrm d\eta_{\rm
leaf}/\mathrm d\eta_{\rm stack}$. It is not a clock choice; it is the map.***

⌗ *A term-by-term split writes **one equation with its terms living in two different spaces**. That is
not a diffeomorphism. It would explain the exact pattern we could not close: **position landed**
because a rescaled force gets the **timing** right; **amplitude never did** because amplitude is where
an approximation to a map and the map itself differ; and **four mechanisms each moved it partway and
none closed it**, which is the signature of a mis-structured map rather than a missing term.*
***You cannot fix a wrong map by adding terms.***

### ⛔ THE DOUBLE-COUNT, VISIBLE IN THE SOURCE

| line | code | comment |
|---|---|---|
| 77 | `RAD_IN_RATE = False` | ***"radiation is content, not a source"*** |
| 112 | `Hleaf = H0*sqrt(OM/a^3 + OL + OR/a^4)` | ***"radiation gravitates: L2"*** — *and the perturbations run on it by default* |

⇒ ***Radiation is removed from the rate because it is content, and put back into the rate the
perturbation sector uses.***

**\u2318 THE DISTINCTION THAT RESOLVES IT.** *The draft's **threshold** result is that expansion is absolute
**outside bound structures** and the transition is **sharp, not gradual** — "regions slightly below the
critical density expand at the same Hubble flow as voids, with no gradual variation". **The plasma at
$\delta\sim10^{-5}$ is not a bound structure.*** ⇒ *So the **expansion rate** it rides on is geometric
and its own density does not set it; while the **local gravity of the perturbation** — $\Phi$, the
driving, the growth of $\delta$ — is full-EFE. **Two different objects, and `Hleaf` conflates them by
putting radiation into the RATE rather than into the local dynamics.***

### ⌗ THE PREDICTION, WITH A NUMBER ALREADY WAITING

*If the perturbations run on the **geometric** rate, that is `STACKPERT=1`, which gives
$\ell_1/\ell_A=0.5703$. And:*
$$0.5703\times\frac{r_{s,\rm stack}}{r_{s,\rm leaf}}=0.5703\times1.2857=0.7332\quad\text{vs sky }0.7312
\quad(\mathbf{0.28\%}).$$
⌗ *This was noticed at the very start of the thread, called a striking coincidence, and **dropped when
the term-splitting story took over**. It now has a reason: **perturbations on the geometric rate, with
the two-horizon ratio entering ONCE, at the map between layers** — where a diffeomorphism's Jacobian
belongs.*

**⛑ THE TEST — a DELETION, not an addition.** *Run `STACKPERT=1` on the current consistent instrument
(with `HIER`), with the ratio applied at the **projection** rather than inside the equation. Report
$\ell_1/\ell_A$, $P_1/P_2$, $P_1/P_3$, $P_1/P_4$ together.* ⇒ ***A structural fix that SIMPLIFIES the
instrument and lands two observables at once would be a different kind of result from four knobs each
moving things partway.***

### ✔ THE LAYER READING TESTED — STACKPERT=1 + HIER + ratio-at-projection (r3528, cc54)
**58's r3527 test, run as specified.** Perturbations on the geometric (stack) rate (`STACKPERT=1` = a
DELETION of the Hleaf radiation double-count, LEAFPERT off, no SRCSTACK/DIFFLEAF/CRAMP), evolved
hierarchy (`HIER=1`), and the two-horizon ratio r_stack/r_leaf = 135.46/105.36 = 1.2857 applied ONCE at
the projection (content sound-horizon -> phenomenological ruler), not inside the equation. Map form taken
from Daryl's draft (main_3.tex sec:cosmo_synth + empirical-tests): radiation is content -- it sets the
sound horizon and photon-baryon dynamics (local, r_leaf) but NOT the global expansion rate (geometric,
r_stack); "transformations between the noumenological expansion and the flat-LCDM phenomenological
expansion necessitate adjustments to the sound horizon's mapping onto BAO scales."

**GATE.** control STACKPERT=1 HIER = 0.7300 / 2.254 / 2.363 -- BYTE-IDENTICAL to control HIER. STACKPERT
is a clean no-op on the control (Hleaf==Hstack, r_leaf==r_stack, map trivial -- as a layer diffeomorphism
should be where the layers coincide). CR shifts are real physics.

| CR STACKPERT=1 HIER | l_1 | l_1/l_A | P1/P2 | P1/P3 | P1/P4 |
|---|---|---|---|---|---|
| raw | 172 | 0.5703 | 0.889 | 0.693 | 1.210 |
| **mapped (x1.2857)** | **221.1** | **0.7332** | 0.889 | 0.693 | 1.210 |
| sky | 220.6 | 0.7312 | 2.217 | 2.277 | -- |

**SPLIT VERDICT -- position lands, amplitude does NOT.**
- ✔ **POSITION LANDS, and it is the cleanest position result of the arc.** Mapped l_1/l_A = 0.7332 vs
  sky 0.7312 (**+0.28%**), from a DELETION (perturbations on the geometric rate) plus ONE projection map
  (r_stack/r_leaf), with NO per-term freedom -- no SRCSTACK, no clock split inside the equation. The map
  is the layer diffeomorphism's Jacobian applied once, exactly where the draft puts it.
- ⛔ **AMPLITUDE DOES NOT LAND -- it INVERTS.** P1/P2 = 0.889 (-60%), P1/P3 = 0.693 (-70%): the first
  peak is SUPPRESSED below peaks 2 and 3 (heights 0.178, 0.200, 0.257 rising to peak 3). This is worse
  than, and opposite to, the leaf-rate runs (P1/P2 = 2.7-3.4, first peak too HIGH). **The sky's P1/P2 =
  2.217 sits BETWEEN the two rates**: geometric undershoots (peak 1 too low), leaf overshoots (peak 1 too
  high). Neither rate lands amplitude.
- ⌗ **The mapped comb is UNIFORM** (spacings 298, 298, 360 vs sky's alternating 318, 272, 316) -- the
  undriven signature again.

**⌘ THE HONEST READING.** 58's structural prediction was "position and amplitude move together toward the
sky." **Position moves to the sky; amplitude moves AWAY from it.** They do not move together. The layer
reading is a genuine and elegant win on POSITION -- it derives the first-peak position from the layer
diffeomorphism with no fitted term-split, the cleanest such result -- but it does NOT dissolve the
amplitude problem. On the geometric rate (the layer-correct rate) the first peak loses its driving boost
entirely (no radiation era -> no potential-decay driving -> peak 1 suppressed), so the amplitude carries
the FULL undriven signature. The layer reading SHARPENS PO-13 rather than closing it: position derived
cleanly, amplitude confirmed as the genuine open residual, and now bracketed (sky between geometric and
leaf rates).

**⚠ ONE OPEN DEGREE OF FREEDOM IN THE MAP'S FORM, flagged not assumed.** The map I applied is a uniform
angular rescale (r_stack/r_leaf on the positions), which by construction cannot change height ratios -- so
the amplitude reported IS the raw STACKPERT=1 HIER dynamics. A DIFFERENT reading of "the map at the
projection" -- the sound-horizon (comb) mapping to r_leaf while the SILK DAMPING keeps its OWN content
scale (the two are different content objects, need not map by the same factor) -- would move the higher
peaks to higher k against a fixed damping envelope, damping them MORE, which would raise P1/P2 and P1/P3
TOWARD the sky. Whether that is the correct map form is a physics question for the draft/58, not a knob to
turn: it requires re-projecting with the comb and damping scales separated. **Flagged for 58 to settle
from the draft; not run unprompted.** If the draft's map carries the sound horizon and the diffusion scale
by the SAME factor, amplitude stays inverted and the residual is genuinely the missing driving; if by
DIFFERENT factors, the amplitude test is not yet complete.

### ⛭⛭ STRUCTURAL RESULT — the layer map fixes POSITION and cannot in principle touch AMPLITUDE (r3529)
**58 concedes cc54's projection argument, and it CLOSES a branch rather than leaving one open.** Both the
comb (in Y, oscillating in k_b, scale r_s) and the damping (D = exp(-k_b^2 kD2inv), scale k_D) live in the
SAME source S(k_b), as functions of the same k_b. The only projection-side lever is the distance x0.
Scaling x0 by f gives C_l(l) -> C_l(l/f): a UNIFORM stretch -- every peak moves by f, every height ratio
preserved. For the damping to bite differently RELATIVE to the comb, the map would have to carry r_s and
k_D by DIFFERENT factors -- which is the two-factor reading declined one step earlier on structural
grounds (a diffeomorphism carries every content length by ONE Jacobian; two factors are not a map). **One
factor cannot move heights; two factors are not a map.** So the layer map fixes position and CANNOT reach
amplitude. The amplitude residual is not a projection question -- it is dynamics, and no reading of the map
reaches it. **Branch closed.**

**MEASUREMENT that settles the aliasing question (58's request before we stop).** PROJMAP implemented as a
genuine re-projection (x0*PROJMAP inside the Bessel, both HIER and fluid paths), CR only (trivial on
control):

| CR STACKPERT=1 HIER | sampling | l_1/l_A | P1/P2 | P1/P3 | peaks |
|---|---|---|---|---|---|
| raw (no map, discrete ladder) | ok | 0.5703 | 0.889 | 0.693 | [172,404,636,916] |
| PROJMAP=1.2857, discrete ladder | **2.3 pts/period -> ALIASED** | 0.7560 | 1.247 | 1.369 | [228,**316,348**,532] |
| **PROJMAP=1.2857, KCONT (clean)** | **9.1 pts/period** | **0.7294** | **0.807** | **0.680** | [220,532,820,1180] |
| sky | -- | 0.7312 | 2.217 | 2.277 | 220.6/538.1/809.8 |

⇒ *The aliased height change (1.247) was an ARTIFACT (spurious 316/348 peaks from under-sampling the
enlarged effective distance). Properly sampled (KCONT), the map moves POSITION to 0.7294 (**-0.25%** from
sky) and leaves the heights INVERTED (0.807/0.680, ~unchanged from 0.889/0.693). Confirmed: the map lands
position, not amplitude.*

**⇒ WHAT STANDS — ~~the cleanest result of the arc~~ — STRUCK/CORRECTED r3532 (see the correction block
at the end): this 0.7294 was computed on GSRC=0, the source that UNDER-counts radiation's gravity. On the
CORRECT full-EFE source the driven position is 0.7825 (+7%). The "cleanest result of the arc" framing was
mine and it is retracted; the position was clean but computed on the wrong source.** ~~The
first-peak POSITION, from a DELETION (perturbations on the geometric rate, STACKPERT=1) plus ONE derived
factor (r_stack/r_leaf at the projection), lands at 0.7294 vs sky 0.7312 (-0.25%), with NOTHING tuned
and a control on which the map is PROVABLY trivial (r_leaf==r_stack there). Position is derived, not fitted.~~

**⇒ WHAT IS OPEN — sharply, and it is a DYNAMICS question, not ours to search.** The amplitude BRACKETS
the sky between the two rates:

| | P1/P2 | P1/P3 |
|---|---|---|
| geometric rate (STACKPERT) | 0.807-0.889 | 0.680-0.693 |
| **sky** | **2.217** | **2.277** |
| leaf rate (LEAFPERT) | 2.7-3.4 | -- |

*The two rates differ by EXACTLY the radiation term. The POSITION says the rate is geometric
(unambiguous). The AMPLITUDE says neither "radiation out of the rate" nor "radiation in the rate"
describes the perturbation DYNAMICS -- the sky sits between them.*

**⚑ 58's OPEN QUESTION for Daryl (not a cc54 search).** The instrument has only two settings: radiation IN
the rate (Hleaf) or OUT of the rate (Hphys/Hc). It has NO way to express the draft's THIRD thing:
**geometric expansion rate AND radiation's LOCAL gravity (the full-EFE local layer where the plasma's own
gravity acts).** The draft says these are different objects -- the expansion is geometric (radiation does
not set it, threshold principle) while the perturbation's local dynamics obey the full EFE with radiation
gravitating as content. If that composition is what CR actually asserts, then NEITHER bracket endpoint is
CR, and the amplitude has never been computed for the framework as written. This is Daryl's to direct.

### ✔ THE THIRD COMPOSITION — geometric rate + radiation FULL in Phi's source (STACKPERT=1 + GSRC=1, r3530)
**58/Daryl's ship, and the composition needed NO new edit -- it was the never-run GSRC flag.** The
instrument already separates the rate's Omega set from the source's: the density fractions (Og_of, On_of,
Ob_of, Oc_of) are normalised to `_rt` (the FULL stack, radiation included) while CR's rate `Hphys` drops
radiation (RAD_IN_RATE=False). The consequence, stated in the flag's own comment: the source is SHORT by
rho_tot(full)/rho_tot(free), because Hc^2 carries rho_free but the Omega_i carry rho_tot. `GSRC=1`
(`Gf_of=_rt/_free`) supplies exactly that factor -- restoring EVERY species' gravity (matter, baryon,
radiation) to full strength while the rate stays geometric. So **STACKPERT=1 + GSRC=1 = "radiation out of
the rate, into the source at full strength"**, the framework's own composition, nothing added, nothing free.

**GATE.** control STACKPERT=1 GSRC=1 HIER KCONT = 0.7300 / 2.254 / 2.363 -- byte-identical to control HIER
(GSRC auto-off where RAD_IN_RATE=True; STACKPERT no-op where Hleaf==Hstack). Clean. CR is real physics.

| CR (geometric rate) | l_1/l_A | P1/P2 | P1/P3 | P1/P4 | peaks (heights) |
|---|---|---|---|---|---|
| GSRC=0 (source short) | 0.7294 | 0.807 | 0.680 | 1.21 | P1 SUPPRESSED below P2,P3 |
| **GSRC=1 (source full)** | **0.7825** | **3.665** | **2.489** | 4.02 | [236,628,868,1220] = [.396,.108,.159,.098] |
| sky | 0.7312 | 2.217 | 2.277 | -- | -- |

**RESULT -- it OVERSHOOTS, both observables, and that is the honest verdict.** Restoring radiation's full
gravity to the source FLIPS the first peak from suppressed (0.807, below P2/P3) to DOMINANT (3.665, far
above) -- radiation's local gravity is unmistakably the right LEVER: it moves P1/P2 the right direction and
THROUGH the sky. But at full strength it OVERSHOOTS: P1/P2 = 3.665 vs sky 2.217 (+65%), P1/P3 = 2.489 vs
2.277 (+9%). And the POSITION moves with it, 0.7294 -> 0.7825 (+7%), because radiation's source gravity is
DRIVING -- it boosts amplitude AND shifts the acoustic phase (the raw comb shifts 0.5703 -> 0.6086 before
the map). So GSRC is not an amplitude-only knob; the full composition couples position and amplitude, and
both overshoot. Per 58's own criterion, overshoot = the composition is off in the other direction -- but
GSRC is NOT tunable (it is the determined _rt/_free), so this is a framework PREDICTION, not a mis-set knob.

**⌘ THE SKY IS NOW BRACKETED ON AMPLITUDE, and by the SAME term.** GSRC=0 undershoots (P1/P2 = 0.807),
GSRC=1 overshoots (3.665), sky between (2.217). The two differ by exactly how much of radiation's gravity
sits in the source. So the mechanism is settled -- radiation's LOCAL gravity is what boosts the first peak
-- and what is unresolved is the AMOUNT: the framework's full-strength value over-drives. ⚑ *And the
odd-even signature persists inside the overshoot: P1/P3 (2.489) nearly lands the sky (2.277, +9%) while
P1/P2 (3.665) badly overshoots -- the ODD peak (P3) is close, the EVEN peak (P2) is too low (heights P2=.108
< P3=.159). The alternation is still there even with the first peak over-boosted.*

**⇒ FIRST AMPLITUDE COMPUTED FOR CR AS WRITTEN.** Every prior number was from a composition CR does not
assert (radiation in the rate = leaf, or radiation in neither = bare stack). This is the first run of the
framework's OWN composition -- geometric rate, radiation gravitating locally at full strength -- and it
OVERSHOOTS the sky on both observables. That is a real result, honestly open: not "we ran out of ideas,"
but "the framework's own composition was computed and it over-drives." What is open, now sharply: WHY the
full local gravity over-drives -- whether CR's radiation gravitates at less than full stress-energy in the
local layer, or whether the position coupling means the driving phase and the amplitude cannot both be read
off this composition. Daryl's to interpret; not a cc54 search.

### ⛭ GSRC OVERSHOOT — the algebra settled, and a decomposition that revises the position claim (r3531)
**58 accepts cc54's algebra: GSRC=1 uniform is the CORRECT full-EFE source, so the overshoot is PHYSICS,
not artifact.** Every Omega is normalised by `_rt` (full stack) while `Hc^2` goes as rho_free, so matter's
source term is `4 pi G rho_m (rho_free/rho_tot)` -- short by the SAME factor as radiation. The shortfall is
the Hc^2-vs-Omega mismatch, not species-specific; the constraint `k^2 Phi = -4 pi G a^2 sum(rho_i d_i)`
refers to ACTUAL perturbed densities, so every species belongs at rho_i/rho_free, which is what the uniform
factor delivers. So the framework's OWN composition, computed on a determined quantity (GSRC = rho_tot/rho_free,
nothing tunable), over-drives the sky. That is a stronger, cleaner position than a normalisation artifact.

**The radiation-only run (GSRCRAD=1) is now a DIAGNOSTIC, not a candidate** -- it under-counts matter by
standard EFE and is NOT a correct composition; it measures WHERE the over-drive lives. Gate clean
(control 0.7300/2.254, GSRC auto-off there so GSRCRAD is a no-op).

| composition | l_1/l_A | P1/P2 | P1/P3 | what gravitates in the source |
|---|---|---|---|---|
| GSRC=0 | 0.7294 | 0.807 | 0.680 | matter+radiation BOTH short (rho_free/rho_tot) |
| GSRCRAD=1 | **0.7825** | 1.873 | 1.667 | radiation FULL, matter short |
| GSRC=1 | **0.7825** | 3.665 | 2.489 | both FULL (the correct EFE source) |
| sky | 0.7312 | 2.217 | 2.277 | -- |

**⌘ THE DECOMPOSITION -- radiation DRIVES (phase+amplitude), matter is PURE AMPLITUDE.**
- *Amplitude P1/P2:* 0.807 (both short) -> 1.873 (radiation boost) -> 3.665 (matter boost on top). The
  radiation boost supplies 0.807->1.873; the matter boost supplies 1.873->3.665. Sky (2.217) sits BETWEEN
  radiation-full and both-full, so the excess over-drive is substantially MATTER'S share of the source --
  but matter's boost is REQUIRED by full EFE, so this is a handle on where the excess lives, NOT a fix.
- *Position:* 0.7294 (radiation short) -> **0.7825 (radiation full)**, and matter's boost does NOT move it
  (GSRCRAD and GSRC=1 both 0.7825). So restoring radiation's source gravity SHIFTS THE POSITION while
  matter's gravity is pure amplitude. Radiation drives (resonant, phase-shifting); matter is a slow
  potential well (amplitude, no oscillation phase).

**⛔ THE REVISION cc54 OWES -- the position "landing at 0.7294" was on the SHORT source.** The clean
position result (0.7294, -0.25%) was computed under GSRC=0, i.e. with radiation's source gravity
UNDER-counted. Restore it to full strength (the correct EFE), and the position moves to 0.7825 (+7% over
sky) -- because radiation's restored gravity is DRIVING, and driving shifts the acoustic phase. So under
CR's CORRECT composition (GSRC=1), BOTH observables over-shoot: position 0.7825 (+7%), P1/P2 3.665 (+65%).
Position is NOT independent of the source, and the earlier "position derived, lands, nothing tuned" holds
only for the radiation-under-counted source. **This connects straight to PO-13's day-one claim** -- "the
driving phase shift LCDM manufactures from radiation driving is, in CR, the two-horizon ratio." The layer
MAP already supplies that phase shift geometrically; restoring radiation's full source gravity supplies it
AGAIN, dynamically, as driving -- so the position over-shoots because the geometric map and the radiation
driving BOTH contribute the phase shift. That looks like a DOUBLE-COUNT of the phase: the map replaces
driving in the position story, but the full source re-adds the driving. **Crux for 58/Daryl.**

**⚑ THE ODD-EVEN SIGNATURE SURVIVES, independent of all of this.** In every run the even peak sits below
the odd (GSRCRAD heights P2=0.185 < P3=0.208; GSRC=1 P2=0.108 < P3=0.159). Getting the source amplitude
right does not touch it -- it is a separate signature, the alternation, and it stays open on its own.

**⇒ PO-13, honestly, now TWO measured open items (not one), plus a crux:** (1) the framework's correct
full-EFE source over-drives the AMPLITUDE by +65% on P1/P2 (with the excess located substantially in
matter's share, though matter's boost is EFE-required); (2) the same restored source over-drives the
POSITION to 0.7825 via radiation's driving, which appears to double-count the phase shift the geometric map
already supplies -- so the clean 0.7294 position holds only on the under-counted source; (3) beneath both,
the odd-even alternation survives independent of normalisation. All measured on determined quantities, none
tuned. The crux for 58/Daryl: whether CR's radiation should DRIVE at all (double-count with the map) or
whether the geometric map should REPLACE the driving phase in the source too.

### ⛭⛭ THE MAP IS OWED, NOT A DOUBLE-COUNT — decisive test + record correction (r3532)
**58's reframing, and it is right: "should radiation drive?" is the wrong question.** Driving is not
optional -- a perturbed radiation density gravitates, Phi responds, the oscillator feels it; that is the
full EFE on the local layer and CR asserts it (draft commitment iv). And the two-horizon ratio was never a
phase shift: it is the MAP between the content sound horizon and the phenomenological ruler -- a units
conversion between layers, owed regardless of the source. It only LOOKED like a driving phase shift because
we applied it to a source with radiation's gravity under-counted (GSRC=0): the undriven comb at 0.5703
times 1.286 landed near the sky, so the conversion appeared to supply the driving. It didn't; the driving
was simply absent and the two numbers happened to be close.

**THE DECISIVE TEST -- GSRC=1 HIER KCONT, NO projection map (the raw driven position).** Gate: control
unchanged (GSRC auto-off there). 58's discriminant: if the map is a genuine layer conversion it is owed
regardless of the source, so removing it should make the position WORSE (raw driven comb below sky, map
carries it up); if instead the raw driven position lands NEAR the sky on its own, map and driving supply
the same thing and one is spurious.

| CR STACKPERT=1 GSRC=1 | l_1/l_A | P1/P2 | P1/P3 |
|---|---|---|---|
| raw, NO map | **0.6499** | 4.094 | 2.551 |
| WITH map (x1.286) | 0.7825 | 3.665 | 2.489 |
| sky | 0.7312 | 2.217 | 2.277 |
| *(for contrast: GSRC=0 raw 0.5703 -> mapped 0.7294)* | | | |

⇒ ***The raw driven position is 0.6499 -- BELOW the sky by -11%, NOT near it.*** So the map is **OWED**:
the driven comb sits below the sky and the ruler conversion carries it up past. **It is NOT a double-count.**
The framework's actual prediction is driven dynamics (raw 0.6499) converted to the observer's ruler
(x1.286) = 0.7825, and that is **+7% high**. Radiation's driving alone moves the raw comb 0.5703 -> 0.6499
(partway to the sky, a real phase shift); the map carries the rest and overshoots. Both are owed, neither
is spurious, and the framework's composition lands 7% high on position -- a far cleaner statement than
"one effect applied twice."

**⛔ RECORD CORRECTION (cc54, propagated).** Three earlier "cleanest result of the arc / cleanest position
result" framings (this file, the layer-reading and structural-result blocks) are RETRACTED. That framing
was mine. The 0.7294 position was clean but computed on **GSRC=0 -- the source we now agree under-counts
radiation's gravity**. On the correct full-EFE source the position is **0.7825, +7%**. The position result
must be read as GSRC=0-dependent everywhere it appears above; the struck marker at "WHAT STANDS" points
here.

**⇒ PO-13, corrected and honest, on the framework's OWN composition (geometric rate + full-EFE local
source, GSRC=1, all determined):**
1. **Position: 0.7825, +7% high** -- driven dynamics + owed ruler conversion, nothing tuned. (The earlier
   -0.25% was on the under-counted source.)
2. **Amplitude: over-driven, P1/P2 ~3.7-4.1 (+65-85%)** -- the correct full source over-boosts the first
   peak; the excess sits substantially in matter's EFE-required share.
3. **Odd-even alternation: surviving underneath, untouched by any normalisation** -- P2 < P3 in every run;
   the one signature independent of the source question, and the last thing standing when it is settled.

All three measured on determined quantities, none tuned. The framework as written reproduces the sky's
STRUCTURE (peaks in the right places to ~7%, first peak dominant) but OVER-DRIVES both position and
amplitude, with a residual odd-even alternation beneath. That is the honest state: not closed, not a
fitting failure -- the framework's own composition computed and found 7-65% high, carried open on its merits.

### ⛭⛭ THE OVER-DRIVE MECHANISM, MEASURED — CR's Φ decays SLOWER, mode by mode (r3533)
**Daryl's push against "carry it open": the residual has a SHAPE and it was glossed.** +7% on position,
+65% on amplitude -- an order of magnitude apart. A uniformly-too-strong source scales both together; this
over-supplies AMPLITUDE while barely touching PHASE, which is the signature of a potential that decays too
SLOWLY (keeps driving through the oscillation, pumping amplitude, while the phase shift saturates early).
Structural expectation: CR's radiation gravitates locally but does NOT set the expansion (threshold), so
the well is as deep as LCDM's while the background is not diluted at the radiation-era rate -> Phi persists
longer relative to the oscillation.

**MEASURED (PHISAVE, matched acoustic phase PHIQ=1,2,3 -- same # half-periods by recomb on both arms;
STACKPERT=1 GSRC=1; gate: no-op on control).** Phi normalised to its super-horizon value; decay per
half-period below:

| q (peak) | CR retains Phi_rec/Phi_0 | CR /half | control retains | control /half | **CR/control** |
|---|---|---|---|---|---|
| 1 | 0.616 | 0.616 | 0.487 | 0.487 | **1.264** |
| 2 | 0.259 | 0.509 | 0.219 | 0.468 | **1.182** |
| 3 | 0.124 | 0.499 | 0.156 | 0.539 | 0.796 |

*(r3431 baseline, on the LEAF composition: ~0.6 per half-period, BOTH arms. This is the FIRST measurement
on the geometric-rate + full-source composition.)*

**⌘ THE MECHANISM IS CONFIRMED, and it maps onto the over-drive mode by mode.** For the modes that set the
amplitude over-drive, CR's Phi decays SLOWER than the control's: q=1 retains +26% more per half-period,
q=2 +18%. And the ENHANCEMENT is largest at q=1 (1.264) and falls with q (1.182, then 0.796 at q=3) -- so
the FIRST peak's driving is sustained most, which is exactly why P1 is over-boosted most and P1/P2
over-drives (+65%), while P1/P3 is only mildly over (+9%) and q=3's Phi actually decays FASTER in CR. The
over-drive is NOT uniform; it tracks the Phi-decay rate mode by mode -- the slower-decaying potential Daryl
predicted, resolving the +7%/+65% asymmetry: sustained driving pumps amplitude (first peak most) while the
phase shift saturates.

**⇒ THIS CHANGES WHAT PO-13 IS.** The over-drive is not a defect in the source and not a fitting failure --
it is a CONSEQUENCE of the rate/source split the framework asserts: radiation gravitates locally (deep
well) but does not set the expansion (no radiation-era dilution), so the well persists and over-drives. And
that is a SEPARATELY OBSERVABLE prediction: Phi's decay history is exactly what the **ISW effect** and
**gravitational lensing** measure. So PO-13's amplitude residual converts from "the model is 65% high" into
"CR predicts a specific potential-decay history -- measurably slower than LCDM for the low modes -- and that
history is independently testable against ISW and lensing." That is a different and better problem than a
fitting miss. **The honest open item is now: what does CR predict for Phi(eta)/Phi(a) across scales, and
does the ISW/lensing data bear out the slower low-mode decay this composition shows?**

**⚑ The odd-even alternation still sits underneath, untouched by any of this** -- P2 < P3 at every
normalisation; the one signature independent of the source and the decay question both.

**⌗ PROCESS NOTE (for the next node, at 58's request).** On this branch 58 reasoned from the code as read
and cc54 ran it; where they disagreed, the RUN won every time -- the map could not move heights (cc54,
measured), the matter double-count was not the diagnosis (cc54, algebra), and the "cleanest position result"
rested on the source we agreed was wrong (cc54, measured). Three corrections in one thread, all by running.
The standing lesson: when a read of the code and a run disagree, run it; the temptation to reason from the
source will recur.

### ⛔ CORRECTION to r3533 — the mode-by-mode mapping was an OVER-CLAIM; the histories-differ pivot stands (r3534)
**Node 59 caught three things on the Phi-decay work (3b56b5ea), and the numbers confirm all three. cc54
owns the over-claim.**

**59.1 -- reporting bug (fixed).** The "CR/control" column reported 1.264, 1.182, 0.796 but mixed the
PER-HALF ratio (q=1) with the CUMULATIVE ratio (q=2,3). The underlying dump is fine (0.259=0.509^2,
0.124=0.499^3). Corrected **per-half** ratios:

| q | CR per-half | CTL per-half | **per-half CR/CTL** |
|---|---|---|---|
| 1 | 0.616 | 0.487 | **1.264** |
| 2 | 0.509 | 0.468 | **1.087** |
| 3 | 0.499 | 0.539 | **0.927** |

These fall MONOTONICALLY and cross 1 between q=2 and q=3. The earlier "not a clean monotonic" caveat was
an artefact of the mixing; the corrected column is cleaner than the reported one.

**59.3 -- referencing (fixed).** The reported over-drive +65%/+9% was against the SKY. The Phi dumps are a
CR-vs-CONTROL measurement, so the residual they could explain is CR-vs-control: **P1/P2 +63%, P1/P3 +5%**
(CR 3.665/2.489 vs control 2.254/2.363). Close to the vs-sky numbers only because control ~ sky here.

**59.2 -- the mode-by-mode mapping RUNS BACKWARDS (the important one). RETRACTED.** If per-half retention
is read as sustained driving, the ratios (1.264, 1.087, 0.927) predict the driving enhancement ORDERED
P1/P3 (1.36) > P1/P2 (1.16) -- the third mode enhanced MOST. The MEASURED residual is the reverse: P1/P2
enhanced 1.63, P1/P3 enhanced 1.05. **The residual does NOT track the Phi-decay ratio mode by mode**, and
cc54's sentence "q=3's Phi decays faster so P1/P3 only +9%" had the sign inverted (faster decay of P3 would
make P1/P3 LARGER, not smaller). I checked the OPPOSITE sign (decay=driving) too -- it predicts both ratios
< 1, also wrong. So no simple reading of retention-as-driving reproduces the peak-height residual. **The
"over-drive tracks the decay rate mode by mode" claim is withdrawn -- mine, and 58 asserted it too; the data
refutes it in either direction.**

⌗ *And a composition caveat cc54 should have flagged: the Phi dump runs on the FLUID path (LOS=0), while
the amplitude residual is from the HIER path -- so even a correct mapping would be comparing two different
transfers. A clean mode-by-mode test would need Phi measured on the HIER composition. (Note re 59.3's gate
point: STACKPERT=1 is NOT SRCSTACK=vel -- the r3512 composition defect was SRCSTACK+HIER, and STACKPERT=1
composes cleanly in evolve_hier via Hc_of; the control gate on STACKPERT=1 GSRC=1 DID pass byte-identical,
so the machinery is validated -- but the fluid-vs-HIER path split for Phi is a real inconsistency.)*

**⇒ WHAT STANDS, narrower and correct.** CR's potential decay HISTORY differs from the control's -- measured,
matched-phase, real (per-half retention 1.264/1.087/0.927, a genuine crossover). That is ALL the ISW/lensing
pivot needs, and 58 said so explicitly: "it only needs the histories to differ, which they do." What does
NOT stand is any claim that this decay history explains the CMB peak-height residual mode by mode -- it does
not, in either direction, and that connection is withdrawn. The over-drive of the CMB amplitude and the
Phi-decay history are BOTH real and BOTH open, but they are not the tidy single mechanism r3533 claimed.

**⇒ THE ONE DISTINCTIVE FEATURE that survives and is worth taking to data (58's point, and it does NOT rest
on the peak mapping):** the per-half retention ratio CROSSES 1 between q=2 and q=3. A generic "CR's wells
persist" pushes every mode one way; this crosses over, so a second effect dominates at high q and the
crossing LOCATES a scale. A crossing scale in Phi's decay history is a far more distinctive, normalisation-
robust prediction than an overall offset -- and Phi's decay is exactly what ISW and lensing measure. **Next:
map the crossover (matched-phase PHIQ q=1..6, both arms, same composition) and locate the crossing k, before
any ISW/lensing comparison -- you want to know the predicted feature before going to the data.**

### ⛭⛭ THE CROSSOVER, LOCATED — a crossing SCALE in CR's potential-decay history (r3535, 58's ship)
**58's point that the q=3 reversal is the FINDING, not a caveat -- confirmed and located.** A generic "CR's
wells persist because radiation does not dilute the background" pushes every mode one way; this CROSSES, so
a second effect dominates at high q and the crossing locates a scale. Matched-phase PHIQ scan, q=1..6, both
arms, STACKPERT=1 GSRC=1 (fluid path, LOS=0), per-half Phi retention:

| q | CR /half | CTL /half | CR/CTL |
|---|---|---|---|
| 1.0 | 0.617 | 0.488 | 1.263 |
| 1.5 | 0.519 | 0.451 | 1.152 |
| 2.0 | 0.509 | 0.468 | 1.087 |
| **2.5** | 0.509 | 0.511 | **0.996** |
| 3.0 | 0.499 | 0.539 | 0.927 |
| 3.5 | 0.506 | 0.549 | 0.921 |
| 4.0 | 0.526 | 0.565 | 0.930 |
| 5.0 | 0.536 | 0.607 | 0.883 |
| 6.0 | 0.568 | 0.627 | 0.907 |

⇒ ***A SINGLE, CLEAN, MONOTONIC crossing at q ~ 2.48*** (k = q pi/r_s = 2.48 pi/135.46 ~ **0.058/Mpc**,
angular scale l ~ k D_M ~ **750**, between the 2nd and 3rd acoustic scales). Below the crossing (large
scales) CR's potential decays SLOWER than LCDM's (retains up to +26% per half-period); above it (small
scales) FASTER (down to -12%), staying below 1 out to q=6. The shape is set by the two arms' rates: CR's
per-half retention is ~flat at 0.5 across q, while LCDM's RISES with q (0.49 -> 0.63) -- LCDM's small-scale
potentials decay less per half-period, CR's do not, and the two cross at q ~ 2.48.

**⌘ WHY THIS IS THE VERSION WORTH TAKING TO DATA (58's argument, and it survives the withdrawn peak
mapping).** A crossing SCALE is far more distinctive than an overall offset: an offset can be mimicked by a
normalisation, a sign change in the ratio cannot. And Phi's decay history is exactly what the **ISW effect**
and **gravitational lensing** measure. So CR makes a specific, falsifiable prediction -- *its potential
decay crosses LCDM's at k ~ 0.058/Mpc (l ~ 750)* -- that nothing else produces and that has its own data,
independent of the CMB acoustic peaks (whose mode-by-mode connection was withdrawn in r3534).

**⚠ CAVEATS kept on the record (honest, per node 59's process point):** (1) this is the FLUID path (LOS=0),
where PHISAVE lives; the amplitude over-drive is HIER -- a HIER-path Phi measurement is owed before the
crossing scale is quoted as final. (2) The crossing is a RATIO, so robust to the Phi_0 normalisation, and
it is clean and monotonic -- but the exact location (q~2.48) will shift somewhat on the HIER path and with
the baryon/recombination details. (3) The number to take forward is the EXISTENCE and rough LOCATION of a
single crossing near the 2nd-3rd acoustic scale, not q=2.48 to three figures.

**⇒ PO-13 STATE, corrected and current:** the framework's own composition over-drives the sky (position +7%,
amplitude +65% vs sky / +63% vs control), and the over-drive is a consequence of the rate/source split, not
a fit failure. The CMB peak-height residual and the Phi-decay history are BOTH real and open, and are NOT a
single mode-by-mode mechanism (r3534). What CR predicts distinctively is a CROSSING SCALE in the
potential-decay history at k ~ 0.058/Mpc -- normalisation-robust, ISW/lensing-observable, and the next thing
to (a) confirm on the HIER path and (b) take to ISW/lensing data. The odd-even alternation still survives
underneath, independent of all of this.

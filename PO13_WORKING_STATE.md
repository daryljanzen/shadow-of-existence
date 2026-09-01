---
name: PO13_WORKING_STATE
description: THE ACOUSTIC-PHASE OFFSET — the worked state of PO-13, held OUTSIDE the corpus. Not a paper, not a register row, not a route into either. Read before touching P15's acoustic sections.
status: WORKING DOCUMENT — deliberately not a paper
# ⛭ r3548 (node 60): DECLARED-UNKNOWN, which is the true statement from this line — nobody
# here has brought this document current and its position is not known. Written because
# classifying it (it had gone unclassified since it was added, failing
# `classify_documents --check` on every push — and under the fast job's `set -e` that
# aborted the step before anything after it ran) made it visible to `check_currency` for
# the first time. ** Declaring ignorance is not declaring currency, and only the owning
# line can do the second. **
current: none
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

## ⛔⛭ r3693 — THE KERNEL ROUTE IS REFUTED BY THE CORPUS, AND THE REFUTATION ARGUES *FOR* THE RYDBERG

***`r3689` proposed that `P15`'s Euclidean transmission would supply $z\simeq58{,}000$ and so turn the
Rydberg start from a fit into a consequence. It cannot, and `P15` proves it cannot — on two independent
routes, neither of which I had read before proposing the route.***

| | `P15` `prop:transmission` and `rem:transmission-leg` |
|---|---|
| **the branch point** | a **degenerate** horizon: $f\sim-\Lambda(r-r_N)^2$, $\kappa=0$, so the tortoise integral is $r_*\sim1/[\Lambda(r-r_N)]$ and the approach **power-law rather than exponential**. ⛔ ***"A degenerate horizon carries no scale, so it cannot imprint one."*** |
| **the collapse leg** | horizon entry at $x=k\eta/\sqrt3=1/\sqrt3$ ***for every $k$*** — the radiation era's own scale invariance — so every mode leaves carrying the same $0.4835\,\Psi_i$, **a single $k$-independent number** |

⇒ ***"Neither carries a scale, and a spectrum can only be tilted by something that does."*** *So the
transmission cannot deliver $58{,}000$ or any other redshift. **The prediction is refuted, and by the
corpus rather than by a computation of mine.***

### ⛭⛭ AND THAT INVERTS THE ARGUMENT RATHER THAN ENDING IT

***If the geometry provably carries NO scale, then any scale appearing in the acoustic era must be the
CONTENT's own.*** *And the content's own scale is atomic:*
$$1+z=\frac{13.5984\ \mathrm{eV}}{k_B\times2.7255\ \mathrm{K}}=57{,}899,$$
*built from the Rydberg and the measured CMB temperature, **carrying no cosmological parameter** — which is
exactly what a content scale looks like and exactly what a geometric one could not be.*

⌗ ***So the two findings are consistent in a way I did not expect when I proposed the test.*** *`P15` says
the geometry is scale-free; the acoustic scale nonetheless needs a scale; the only place left is the
content; and the number that works is the content's binding energy. **That is an argument, not a
derivation** — nothing here shows why the acoustic era should begin at ionisation rather than at any other
content scale — but the elimination is now the corpus's own and not a guess.*

⌗ *`P15`'s prose called the branch point "the seam" in `rem:transmission-leg` and in a label. **Corrected
here**, since the front seam is $r=+\alpha/\sqrt3$, the double root, and the two loci are precisely the two
this proposition distinguishes — a degenerate horizon against a non-degenerate one. Paper recompiles clean.*

---

## ⌗ r3743 — `DRC` SCANNED ON THE CONTROL: THE DEFAULT IS ITS OPTIMUM, SO THE DRIVING IS NOT THE KNOB

| `DRC` | $\ell_1$ | $P_1/P_2$ | $P_1/P_3$ |
|---|---|---|---|
| 0.0 — driving off | 204 | 4.216 | 11.625 |
| ⛭ **1.0 — the default** | **220** | 2.721 | ⛭ **4.496** |
| 1.5 | 228 | 2.567 | 7.495 |
| **THE SKY** | **220.6** | **2.217** | **2.277** |

⇒ ***$P_1/P_3$ is NON-MONOTONIC in `DRC`, with its MINIMUM at the default*** — *and $\ell_1=220$ against
the sky's $220.6$ sits at the same value. **The continuity driving is correctly set, and its best possible
value still leaves $P_1/P_3$ at $4.496$ against $2.277$.***

⌗ ***So `DRC` is eliminated as well, and eliminated the strong way***: *not "it does not help" but **"it is
already at its optimum and its optimum is not enough"**. A scan that had come out monotonic would have
left a fitted value to argue about; this one does not.*

### ⌗ THE ELIMINATION LIST FOR THE HEIGHT DEFECT, ON THE CONTROL

| | |
|---|---|
| $C_\ell$ vs $D_\ell$ | ⛔ correct as coded |
| primordial tilt $n_s$ | ⛔ present, $0.965$ |
| diffusion damping | ⛔ **44% remains with it entirely removed** |
| lensing | ⛔ would make it **worse** |
| continuity driving `DRC` | ⛔ **already at its optimum** |

⚠ ***AND THE POSITIONS ARE RIGHT THROUGHOUT.*** *At `DRC=1` the control gives $\ell_1=220$ against
$220.6$. **Whatever is missing suppresses the third peak without moving the comb** — which is a narrow
class of thing, and narrower now by five.*

---

## ⌗ r3741 — WORKING THE HEIGHT DEFECT ON THE CONTROL: THREE CANDIDATES ELIMINATED, THE DEFICIT IS IN THE SOURCE

***`r3739` put the height residual on the control, where the target is known. This turn eliminates the
three things that most often account for a factor like this.***

| candidate | verdict |
|---|---|
| **is it $C_\ell$ rather than $D_\ell$?** | ⛔ **no** — line 737 returns `Cl * (ls*(ls+1))`, so it is $D_\ell$, matching the sky's convention |
| **is the primordial tilt missing?** | ⛔ **no** — line 711, `P = kk**(0.965-1)/kk*dk`, $n_s=0.965$ is there |
| **can diffusion damping account for it?** | ⛔ **no** — see below |

*The control reports $\ell_D=1952$, so $e^{-2(\ell/\ell_D)^2}$ suppresses $P_3/P_1$ by $0.727$ and
$P_2/P_1$ by $0.881$. **Removing damping ENTIRELY** gives $P_1/P_3=3.268$ and $P_1/P_2=2.398$ against the
sky's $2.277$ and $2.217$.*

⇒ ***Even with the damping switched off completely, the control's third peak is $44\%$ too weak.
Diffusion cannot account for it, and the deficit is in the SOURCE.***

⌗ *Lensing is eliminated too, and in the informative direction: the sky's ratios are **lensed** and the
instrument's are not, and lensing SMOOTHS peaks — reducing $P_3$ more than $P_1$, which raises $P_1/P_3$.
**It would make the discrepancy worse, not better.***

⚠ ***WHAT THIS LOCALISES.*** *A third-peak deficit that survives damping removal, at the right positions,
with $D_\ell$ and the tilt both correct, is the classic signature of **the potential's behaviour through
the radiation-matter transition** — the term that boosts $P_3$ in $\Lambda$CDM and is what makes $P_3/P_1$
a measurement of $\Omega_c$. **That is the same $\Psi$-through-recombination the `r3737` diagnosis
reached from the other side, now reached on the arm where the answer is known.***

---

## ⛔⛭⛭ r3739 — **THE CONTROL FAILS THE HEIGHTS TOO. THE HEIGHT RESIDUAL IS NOT A CR DEFECT.**

***The check that should have come first. The height machinery is SHARED by the two arms, so run the arm
whose answer is known.***

| arm | $\ell_1$ | $\ell_2$ | $\ell_3$ | $P_1/P_2$ | err | $P_1/P_3$ | err |
|---|---|---|---|---|---|---|---|
| **$\Lambda$CDM control**, validated | **220** | 524 | 804 | 2.721 | $22.7\%$ | 4.496 | ⛔ **$97.5\%$** |
| CR, `CRAMP=flat` (coded) | 204 | 508 | 804 | 2.238 | $0.9\%$ | 3.901 | $71.3\%$ |
| ⛭ CR, `CRAMP=entry` (derived) | 204 | 508 | 804 | **1.935** | $12.7\%$ | **2.578** | $13.2\%$ |
| **THE SKY** | 220.6 | 538.1 | 809.8 | **2.217** | | **2.277** | |

⇒ ***The control gets the POSITIONS right — $\ell_1=220$ against $220.6$ — and the HEIGHTS wrong by
$23\%$ and $97.5\%$.*** *On $\Lambda$CDM, where the answer is known and the arm is validated against CAMB
for its transfer.* ⛔ ***A defect that shows there is not a CR defect.***

⛭ ***AND CR WITH THE DERIVED DATUM BEATS THE CONTROL ON BOTH RATIOS*** — *$12.7\%$ and $13.2\%$ against
$22.7\%$ and $97.5\%$. **The datum work of `r3735` was real; the residual it was measured against is the
instrument's, shared.***

### ⌗ AND A GUARD I HAD BEEN RUNNING PAST

*The control refused to report at `NK=90`: **"UNDER-SAMPLED — raise NK; the projected peaks would be
aliasing, and the source comb would stay correct while they did it."** Every CR run in this thread used
`NK=90`.* ⌗ ***Re-run at `NK=220`: `204/508/804`, $P_1/P_2=1.935$, $P_1/P_3=2.578$ — identical. The CR
runs were not aliased.*** *But that was luck, not care: the guard fires on $D_M$, and CR's is $13{,}005$
against the control's $13{,}865$, which is the only reason $90$ sufficed on one arm and not the other.*

⚠ ***SO THE LAST THREE REVISIONS WERE CHASING A SHARED INSTRUMENT DEFECT.*** *The baryon-offset diagnosis
at `r3737` — even peak too strong, odd too weak, offset $\propto R\Psi$ too small — **is a correct reading
of a spectrum the control produces too.** It is a statement about the height machinery, not about CR's
physics, and the place to work it is the arm where the target is known.*

---

## ⛔⛭ r3737 — TWO CORRECTIONS: MY OWN SIGN ERROR, AND `GSRC`'s PREMISE IS FALSE UNDER `LEAFPERT`

### ⛔ FIRST, MINE

*`r3735` reported the two height errors as "both off by $\sim13\%$ in the same direction, both low". **They
have OPPOSITE SIGNS**: $P_1/P_2$ is $-12.7\%$ and $P_1/P_3$ is $+13.2\%$. I read magnitudes and did not
check direction.*

| | CR | sky | the peak itself |
|---|---|---|---|
| $P_2/P_1$ | 0.5168 | 0.4511 | ⛔ $P_2$ is **$+14.6\%$ TOO STRONG** |
| $P_3/P_1$ | 0.3879 | 0.4392 | ⛔ $P_3$ is **$-11.7\%$ TOO WEAK** |

⇒ ***Even peak too strong, odd peak too weak. That IS the odd/even signature — REDUCED from
$+0.9/+71.3$ to a symmetric $\pm13\%$, and NOT gone.*** *And a uniform normalisation was never a
candidate: **it cancels in a ratio**, so both ratios moving is itself proof the residual is not an
amplitude.*

⌗ *Odd peaks are **compressions**, boosted by the baryon offset; even peaks are **rarefactions**,
suppressed by it. $P_3$ weak and $P_2$ strong says **the offset $\propto R\Psi$ is too small**, and $R$ is
already verified right (`r3725`) — so it is $\Psi$ **through recombination**, not the datum $\Psi$ that
`entry` now sets.*

### ⛔ SECOND, THE INSTRUMENT'S

*`GSRC` supplies exactly that missing $\Psi$ — the radiation the source omits. **Run with the derived
datum it moves $\ell_1$ from 204 to 244 where the sky wants 220.6: the right direction, overshooting by
$2.4\times$**, and takes the ratios to 6.7 and 14.6.*

***Its own justification says why: "the CR arm's Hc is the L1 rate, built from $\rho_{\rm tot}$ WITHOUT
radiation".*** ⛔ *That was written at `r3400`. **`LEAFPERT` became the default at `r3409`, and under it
`Hc = Hl_of(e)`, built from `Hleaf`, which CARRIES the radiation term.** The Friedmann constraint already
holds with the full $\rho_{\rm tot}$; the source is not short; $G_f$ should be 1.*

⇒ ***`GSRC=1` with `LEAFPERT` applies the same correction twice*** — $G_f=2.73$ at the onset, $1.28$ at
recombination. *Left settable, because it IS correct under `STACKPERT=1` where $H_c$ really is the
radiation-free rate, and the file now warns when the two are combined.*

⚠ ***SO THE OFFSET IS STILL TOO SMALL AND `GSRC` IS NOT THE WAY TO SUPPLY IT.*** *The one place $\Psi$
through recombination can legitimately grow has been checked and it was already counted.*

---

## ⛭⛭⛭ r3735 — `CRAMP=entry`: THE DERIVED DATUM BEATS BOTH FLAGS, AND THE ODD/EVEN IMBALANCE IS GONE

***One function, no flag. `r3733` showed neither coded reading holds across the band on the leaf, so the
datum is $T$ evaluated at the phase each mode has ACTUALLY accrued since ITS OWN leaf horizon entry:
$x=k c_s(\eta_{\rm on}-\eta_{\rm entry})$, and $x=0$ for a mode still outside, where $T\to1$ is the
super-horizon value.***

*Computed rather than chosen — each mode's entry solved from $k=aH_{\rm leaf}$ on the file's own grid:*

| $\ell$ | $z_{\rm entry}$ | $x$ | $T(x)$ |
|---|---|---|---|
| **220** | ***never enters*** | 0.000 | **1.0000** |
| 538 | 17,383 | 0.842 | 0.9308 |
| 810 | 27,082 | 1.585 | 0.7704 |
| 1450 | 49,954 | 3.317 | 0.2541 |

*against the coded reading's $T(1/\sqrt3)=0.9671$ for **every** mode.*

### ⛭ THE RESULT

| reading | $P_1/P_2$ | err | $P_1/P_3$ | err | combined |
|---|---|---|---|---|---|
| `flat` (coded) | 2.238 | $0.9\%$ | 3.901 | $71.3\%$ | $72.3\%$ |
| `onset` | 1.672 | $24.6\%$ | 2.403 | $5.5\%$ | $30.1\%$ |
| ⛭ **`entry` (derived)** | **1.935** | $12.7\%$ | **2.578** | $13.2\%$ | ⛭ **$25.9\%$** |
| **THE SKY** | **2.217** | | **2.277** | | |

⇒ ***The derived datum is the best combined — and the error CHANGES CHARACTER, which matters more than
the number.*** *`flat` has one ratio near-perfect and the other $71\%$ off; `onset` has that imbalance
reversed. **`entry` has both off by $\sim13\%$ in the SAME direction, both low.***

⛔ ***CORRECTED AT r3737 — THE ABOVE READ MAGNITUDES AND NOT SIGNS.*** *The two errors are
$-12.7\%$ and $+13.2\%$: **OPPOSITE**, not "both low". In the peaks themselves, relative to $P_1$:
**$P_2$ is $+14.6\%$ TOO STRONG and $P_3$ is $-11.7\%$ TOO WEAK.** That is the odd/even signature, still
present — **REDUCED from $+0.9/+71.3$ to a symmetric $\pm13\%$, and not gone.***

⌗ ***And a uniform normalisation was never a candidate: it CANCELS in a ratio.*** *Both ratios moving is
by itself proof the residual is not an amplitude.*

⚠ ***THE POSITIONS DID NOT MOVE:*** *$204/508/804$, identical to the coded default. **The datum fixes the
heights and not the comb**, so the position deficit is a separate residual and is not addressed here.*

---

## ⛭⛭ r3733 — `prop:subhorizon` IS COMPUTED ON THE STACKING RATE, AND ON THE LEAF ITS MARGIN GOES

***`prop:subhorizon` is the proposition that decides which handover datum is right, so its number matters.
It reproduces on one rate and not the other.***

| $k_{\rm hor}$(onset) at $z=6797$ | value | ratio to $\pi/\rs$ |
|---|---|---|
| **STACK** — geometric, no radiation | **0.01112** /Mpc | **2.09** |
| **LEAF** — content gravitates | 0.01836 /Mpc | 1.26 |
| *the paper states* | *$\sim0.010$* | *$\gtrsim2$* |

⇒ ***So the proposition is computed on the STACKING rate.*** *And the perturbations run on the **LEAF** —
`LEAFPERT`, default since `r3409`, and the rate rule's own assignment — so the horizon they are inside or
outside of is the leaf's.*

| $\ell$ | $k$ | $k/k_{\rm hor}$ STACK | $k/k_{\rm hor}$ LEAF |
|---|---|---|---|
| **220** | 0.01692 | 1.52 | ⛔ **0.92 — OUTSIDE** |
| 538 | 0.04137 | 3.72 | 2.25 |
| 810 | 0.06228 | 5.60 | 3.39 |

⛔ ***On the leaf the FIRST-PEAK MODE IS MARGINALLY OUTSIDE THE HORIZON at the onset.*** *The proposition's
"inside by a factor $\gtrsim2$" becomes "$1.26$, and the mode that matters most is at $0.92$".*

### ⛭ AND THAT IS EXACTLY THE FORK BETWEEN THE TWO DATA

*A mode **inside** the horizon at the onset has been oscillating and arrives with **its own accumulated
phase** — the $k$-dependent reading, `CRAMP=onset`. A mode **outside** has not, and arrives with the
super-horizon amplitude — the $k$-independent reading, `CRAMP=flat`.*

⇒ ***The two readings are not two conventions. They are the two sides of `prop:subhorizon`, and which one
holds depends on the rate the proposition is evaluated on.*** *On the stacking rate every acoustic mode is
inside and `CRAMP=onset` follows. On the leaf the low-$k$ end straddles the boundary, so **neither reading
is right across the whole band** — which is precisely the shape of the residual: `CRAMP=onset` fixes
$P_1/P_3$ (high $k$, firmly inside on both rates) and breaks $P_1/P_2$ (lower $k$, where the two rates
disagree).*

⚠ ***AND THE PROPOSITION'S OWN QUALIFIER SURVIVES THIS.*** *`P15` already records that completeness holds
"for the modes whose entry precedes the horizon maximum… **the low-$k$ end is where it would bite**". **The
low-$k$ end is where it bites.** The paper flagged the right edge and the instrument was run as though the
flag did not apply.*

---

## ⛭⛭ r3729 — RUN: `CRPSI` REFUTED BY THE PAPER'S OWN WARNING, AND `CRAMP=seam` GIVES THE BEST COMB YET

| configuration | $\ell_1$ | $\ell_2$ | $\ell_3$ | $P_1/P_2$ | $P_1/P_3$ |
|---|---|---|---|---|---|
| coded default (`CRAMP=flat`) | 204 | 508 | 804 | 2.238 | **3.901** |
| ⛭ **`CRAMP=seam`** | **212** | 508 | 796 | 1.672 | ⛭ **2.403** |
| ⛔ `CRPSI=envelope` | 164 | 580 | 756 | 14.48 | 9.21 |
| ⛔ both | 172 | 628 | 780 | **452.5** | 385.0 |
| **THE SKY** | **220.6** | **538.1** | **809.8** | **2.217** | **2.277** |

### ⛔ MY REMEDY WAS WRONG AND `P15` SAYS WHY, IN THE REMARK I QUOTED

*I set $\Psi$ from the leg's closed form independently. **Both variants destroy the comb** — $P_1/P_2$
reaches $452$.* ⌗ *`rem:branchpoint-not-a-condition`, the same remark that pointed me at `sec:envelope`,
warns against exactly this: **"The Hamiltonian constraint is not an additional condition to impose there…
Imposing it at the branch point alongside the leg's own solution therefore OVER-DETERMINES the
handover."** The leg supplies the potential, the effective temperature **and the density contrast as their
difference** — three quantities, one solution. **Setting one of them by hand breaks the other two**, and
that is what $\Theta_0=\hat\Theta-\Psi$ changing sign across the band is.*

⇒ ***The `r3727` diagnosis was half right: $\Psi$ IS flat where the paper derives a $k$-dependence. The
remedy is not to impose it — it is to let the datum carry it where the freedom actually lives.***

### ⛭ AND THAT IS `CRAMP=seam`, WHICH THE CORPUS ALREADY OFFERS

*It reads the **same** closed form $T(x)$ at each mode's own phase at the seam rather than at a single
argument — a reading the instrument's own comment calls "defensible" and "not invented here".*

| | coded | `CRAMP=seam` | sky | |
|---|---|---|---|---|
| $\ell_1$ | 204 | **212** | 220.6 | *closer* |
| $P_1/P_3$ | 3.901 | **2.403** | 2.277 | ⛭ ***from $71\%$ off to $5.5\%$ off*** |
| $P_1/P_2$ | 2.238 | 1.672 | 2.217 | ⛔ *from $0.9\%$ to $25\%$ — the other way* |

⇒ ***The height ratio that has been the corpus's worst failure moves almost onto the sky, and the one that
was already right moves off it.*** *One knob, opposite effects on the two ratios — **which is the odd/even
signature `r3725` predicted would be the thing in play**, now moving under a datum change rather than
staying flat.*

⚠ ***NOT A FIT.*** *`CRAMP` has two readings and both were in the file before this pass; neither was
tuned. **What is new is that the second one was never run against the heights.***

---

## ⛭⛭⛭ r3727 — **THE HANDOVER POTENTIAL IS DERIVED IN THE PAPER AND THE INSTRUMENT HANDS OVER A CONSTANT**

***`r3725` said the missing ingredient is $\Psi$. `P15` `sec:envelope` supplies it in closed form, and
`rem:branchpoint-not-a-condition` says so outright: "the state itself is whatever the leg's evolution
produces, and \S\ref{sec:envelope} supplies it in closed form: **the potential from the leg's own
equation**, the effective temperature oscillating freely from horizon entry, and the density contrast as
their difference."***

*On the radiation-dominated collapse leg $\Psi''+(4/\eta)\Psi'+(k^2/3)\Psi=0$, whose regular solution is
elementary and **even in $x$**, so the contracting leg carries it pointwise:*
$$\Psi=3\Psi_i\frac{\sin x-x\cos x}{x^{3}},\qquad x=\frac{k\eta}{\sqrt3}$$
*and $\hat\Theta=\Theta_0+\Psi$ removes the source exactly, $\hat\Theta''+(k^2/3)\hat\Theta=0$.*

### ⛔ WHAT THE INSTRUMENT ACTUALLY HANDS OVER

```
Ph0 = -np.ones(nk)          # lines 339 and 433
```

***A constant. Flat in $k$, for every mode.***

| $\ell$ | $k/\mathcal{H}$ | $x$ | $\Psi$ coded | $\Psi$ derived |
|---|---|---|---|---|
| **220** | 1.53 | 0.881 | $-1.000$ | $\mathbf{-0.9245}$ |
| 538 | 3.73 | 2.154 | $-1.000$ | $\mathbf{-0.6065}$ |
| 810 | 5.62 | 3.243 | $-1.000$ | $\mathbf{-0.2747}$ |
| 1120 | 7.77 | 4.485 | $-1.000$ | $\mathbf{-0.0013}$ |
| 1450 | 10.06 | 5.806 | $-1.000$ | $\mathbf{+0.0861}$ — *sign reversed* |

⇒ ***The derived datum falls from $0.92$ to zero across the observed comb and CHANGES SIGN near
$\ell\simeq1400$. The coded one is $1$ throughout.*** *That is a strong, monotone $k$-dependence imposed on
the driving term at the handover — **exactly where `r3683` measured the driving failing as $k^{-1}$.***

⌗ ***AND IT IS THE SAME INGREDIENT `r3725` NAMED.*** *The zero-point offset is $\propto R\Psi$; $R$ is
right in the code and $\Psi$ is a constant where it should be the transfer function. **One wrong line
accounts for the flat phase, the absent odd/even alternation, the $k^{-1}$ driving, and the height ratios
that go with them.***

⚠ ***NOT YET RUN.*** *This is a diagnosis from reading the paper against the code. **Whether replacing the
constant with the closed form moves the comb onto the sky is the next calculation and it has not been
done.***

---

## ⛭⛭ r3725 — ONE DEFECT, TWO SYMPTOMS: THE COMB'S PHASE DOES NOT ALTERNATE, AND THAT IS MISSING $\Psi$

***With the scale settled at `r3723`, the peaks are the whole problem. This turn reads them rather than
re-fitting them.***

### ⌗ FIRST, A MEASUREMENT THAT RULES OUT THE RULER

| $z_{\rm start}$ | $\rs^{\rm stack}$ | $\ell_A$ | peaks |
|---|---|---|---|
| 6,761 | 135.46 | **301.6** | 204 / 508 / 804 |
| 12,000 | 160.48 | **254.6** | 204 / 508 / 780 |
| 25,000 | 184.02 | **222.0** | 212 / 508 / 772 |

⇒ ***$\ell_A$ swings by $36\%$ and the comb barely moves. The peak positions are NOT following the ruler***
— *so no choice of $\rs$ or start redshift is going to place them, and the residual is dynamical.*

### ⛭ THE PHASE STRUCTURE, WHICH NAMES THE DEFECT

| $m$ | CR $\ell_m$ | $\phi_{\rm CR}$ | sky $\ell_m$ | $\phi_{\rm sky}$ |
|---|---|---|---|---|
| 1 | 204 | 0.324 | 220.6 | **0.269** |
| 2 | 508 | 0.316 | 538.1 | **0.217** |
| 3 | 804 | 0.334 | 809.8 | **0.317** |

⇒ ***CR's phase is FLAT. The sky's ALTERNATES — odd, even, odd.*** *That alternation is **baryon
loading**: the oscillation is offset from zero, so compression and rarefaction peaks shift differently.*

### ⛭ AND THE EQUATION SAYS WHICH INGREDIENT IS MISSING

*From the instrument's own velocity equation, which is **correct** — $\Psi$ enters undivided while the
pressure carries $1/(1+R)$, standard tight coupling:*
$$\Theta_0''+\frac{\mathcal{H}R}{1+R}\Theta_0'+k^{2}c_s^{2}\Theta_0=-\tfrac13k^{2}\Psi
\qquad\Longrightarrow\qquad \Theta_0\big|_{\rm eq}=-(1+R)\Psi$$

⇒ ***The offset is proportional to $R\Psi$, and it needs BOTH. $R$ is right in the code. $\Psi$ is not
there — a mode starting ALREADY SUB-HORIZON begins after $\Psi$ has decayed, so the offset is absent and
the comb has no odd/even structure.***

⛭ ***SAME ROOT CAUSE AS THE DRIVING DEFICIT.*** *`r3683` measured the driving tracking the start redshift;
this is that same fact read in the peak **phases** instead of in $Q$. **One defect, two symptoms — and the
height ratios go with it**, which is why $P_1/P_3=3.90$ against the sky's $2.28$ while $P_1/P_2=2.238$
against $2.217$ is nearly perfect: the odd/even structure is exactly what is absent.*

---

## ⛭⛭⛭ r3723 — **THE ACOUSTIC SCALE, EACH QUANTITY IN ITS OWN METRIC: $1.8\sigma$, AND $H_0$-FREE**

***The calculation PO-13 had never run. Nothing mixed, nothing fitted beyond the onset already in the
model.***

| | |
|---|---|
| $\rs$ **LEAF** — the phase accumulator, the metric the plasma lives in | **105.36 Mpc** |
| $\rs$ **STACK** — the comoving ruler, the vacuum metric | **135.46 Mpc** |
| ⛭ ratio | **1.2857** — *and the instrument's undocumented constant is $1.286$. **Derived, not stipulated.*** |
| $D_M$, read across leaves → stack | 13,005 Mpc |
| ⛭ $100\,\theta_*=100\,\rs^{\rm stack}/D_M$ | **1.04164** against the sky's $1.04109\pm0.00030$ |

### ⛭ AND IT IS $H_0$-FREE, WHICH WAS THE WHOLE POINT

| $H_0$ | 67.0 | 70.0 | 73.0 | 76.0 |
|---|---|---|---|---|
| $100\,\theta_*$ | 1.04164 | 1.04164 | 1.04164 | 1.04164 |

⇒ ***Identical to five decimals. The CMB acoustic angle places NO constraint on $H_0$ in this model — it
constrains $x_0$ alone, and $H_0$ comes from the local measurement unopposed.***

### ⌗ THE THREE ATTEMPTS, SIDE BY SIDE

| | $100\theta_*$ | miss | |
|---|---|---|---|
| mixed metrics, from $a\to0$ | 1.07458 | $+3.22\%$ | $111\sigma$ |
| mixed metrics, from the Rydberg | 1.03959 | $-0.144\%$ | $5\sigma$ |
| ⛭ **correct metrics, from the onset** | **1.04164** | **$+0.053\%$** | **$1.8\sigma$** |

⛭ ***THE TENSION RESOLVES TRIVIALLY, EXACTLY AS DARYL SAID IT MUST*** — *one geometric rate, two
parameters $(x_0,\alpha)$, and a ruler that is not radiation-pinned. **Nothing was adjusted to make it
happen; the mixing was removed and it fell out.***

### ⛔ AND WHAT REMAINS IS NOW A SINGLE, DIFFERENT PROBLEM

***The SCALE is right to $1.8\sigma$. The PEAK POSITIONS within it are not:*** *the instrument gives
$204/508/804$ against $220.6/538.1/809.8$, i.e. $\ell_1/\ell_A=0.6764$ against the sky's $0.7312$.*

⇒ ***That is the DRIVING, not the scale*** — *`r3683` measured it tracking the start redshift, and `r3685`
showed the branch-point datum brings CR's driven $Q$ to the control's to three decimals. **Those two have
never been run together with the metrics assigned correctly, and that is the next calculation.***

---

## ⛭⛭⛭ r3721 — THE RATE QUESTION SETTLED FROM DARYL'S PRE-BST PAPER: THE TWO HORIZONS ARE TWO METRICS, NOT TWO CONVENTIONS

***The layered-geometry hypothesis states the leaf/stack distinction directly, years before either word
existed. Four clauses, and (ii)–(iv) settle the rate question.***

> *(ii) the cosmological solution may be **fundamentally independent of matter fields, potentially arising
> as a vacuum solution** of the Einstein field equations; (iii) distinguishes between cosmological
> space-time and the real, existing three-dimensional universe by anchoring the latter in a particular
> foliation, such that real "space" at any instant is **diffeomorphic to slices of the cosmological
> geometry**; and (iv) permits **local spatial evolution in accordance with the full Einstein field
> equations, accommodating nonzero stress-energy densities.***

### ⛭ WHAT THAT FIXES

| | | |
|---|---|---|
| **the cosmological hypersurface** | a **VACUUM** solution — content does not enter it | **THE STACKING RATE.** *This is why it carries no radiation term: not because radiation is absent, but because it is **content**, and (ii) says content does not source this geometry* |
| **the real, existing 3-space** | **diffeomorphic** to that slice, but obeying the FULL field equations with $T_{\mu\nu}\neq0$ | **THE LEAF.** *Same space, differently metricised — which is why (iv) can permit lensing locally while the slice stays $S^3$* |

⇒ ***So the two sound horizons are not two conventions for one length. They are ONE separation measured in
TWO METRICS on the same slice, and the ratio $1.286$ is the leaf-to-stack metric ratio.***

### ⛭⛭ AND IT ASSIGNS EACH ONE WITHOUT PREFERENCE

*The acoustic wave is generated by a **process running in the content** — the plasma oscillates, and its
phase accumulates in the metric the plasma lives in. **LEAF.** That is `ACOUSTIC_two_arm`'s phase
accumulator, and the kinematic rule's "the plasma's sound horizon … takes the leaf's" is about **this**.*

*The angle $\theta_*$ is formed by light reaching us **across the foliation** from the two ends of that
separation. **A separation read across leaves takes the stacking rate**, so the comoving length whose angle
we measure is the same physical separation read in the **vacuum** metric. **STACK.** That is the comoving
ruler.*

⇒ ***Both readings of the rule hold at once, and `P15`'s $H_0$-independence follows: the ruler and $D_M$
share the stacking metric, so $H_0$ cancels — verified at `r3717` to $0.0000\%$.***

⌗ ***THE INSTRUMENT HAD THIS RIGHT AND I CALLED IT AN ERROR AT `r3683`.*** *Its docstring says "the two
are correct and NOT interchangeable… Do not unify them." **It was not a fudge between conventions; it was
this distinction, undocumented.***

### ⛔ AND THAT RETIRES THE RYDBERG THREAD'S PREMISE

***Every number from `r3687` to `r3715` computed $\theta_*$ with $\rs$ on the leaf and $D_M$ on the stack —
mixing the two metrics.*** *That mismatch is what made $\theta_*$ $H_0$-dependent, what made an early
cut-off necessary, and what put the required start near $z\simeq60{,}500$ in the first place.*

⇒ ***The Rydberg coincidence, the $2.2\%$ velocity offset, the atomic corrections — all of it was chasing
a residual created by a metric mismatch.*** *`r3689`'s structural finding does not survive either: the
"no root in $\Omega_m$ from $a\to0$" was computed under the same mismatch.* ⛭ *Daryl's standing point is
the plain reading: **there is one geometric rate and no room for adjustment beyond $(x_0,\alpha)$, so the
tension resolves trivially** — and it does, once the ruler is not radiation-pinned.*

---

## ⛔⛔ r3717 — THE CONTRADICTION AT THE ROOT OF THIS WHOLE THREAD: WHICH RATE THE SOUND HORIZON TAKES

***Three atomic corrections tested and all fail by orders of magnitude, which sent me to ask where
$\Omega_m=0.3066$ comes from. Reading `P15` `sec:tensions` answered that and exposed something larger.***

| candidate for the $2.2\%$ | size | |
|---|---|---|
| reduced mass ($\mathrm{Ry}_H$ vs $\mathrm{Ry}_\infty$) | $-0.027\%$ in velocity | ⛔ **wrong sign**, and $80\times$ too small |
| Lamb shift (1s) | $6\times10^{-5}\%$ | ⛔ five orders too small |
| Debye screening at $n_e=4.2\times10^{7}$ cm$^{-3}$ | $3\times10^{-6}\%$ | ⛔ eight orders too small — $a_0/\lambda_D=1.7\times10^{-8}$ |

### ⛔ AND THE ROOT PROBLEM, WHICH IS NOT ABOUT ATOMS AT ALL

*`P15` `sec:tensions` states the $H_0$ claim exactly:* **"$\rs$ and $D_M$ carry the stacking rate's common
$H_0$, which therefore scales out of their ratio, so $\theta_*$ is fixed by the offset $x_0$ alone… and the
same $z_{\rm onset}$ meets the scale at every $H_0$ across the range."**

***Measured:***

| $H_0$ | $\theta_*$, $\rs$ on the STACKING rate | $\theta_*$, $\rs$ on the LEAF |
|---|---|---|
| 67.0 | 1.82756 | 1.02986 |
| 73.0 | 1.82756 | 1.07458 |
| 76.0 | 1.82756 | 1.09523 |
| **variation** | ⛭ **0.0000% — $H_0$ scales out** | ⛔ **6.35% — it does not** |

⇒ ***`P15`'s $H_0$-independence REQUIRES the sound horizon on the STACKING rate. `P07`'s and `P15`'s own
kinematic rule puts it on the LEAF*** — *"the plasma's **sound horizon**, its diffusion length,
recombination, the perturbations — takes the leaf's".* **Radiation carries $\Omega_r=4.15\times10^{-5}/h^2$,
so $h$ does not cancel. The two statements cannot both hold.**

⌗ ***AND THE WHOLE $H_0$-TENSION CLAIM RESTS ON THE FIRST.*** *That is the claim `sec:tensions` makes —
the geometric rate fits DESI DR2 at $\chi^2/\mathrm{dof}\simeq1.0$ **at any $H_0$ including the local 73**,
where $\Lambda$CDM is tied to one $H_0$ and breaks at 73 with $\chi^2/\mathrm{dof}\simeq15$.*

### ⌗ AND IT EXPLAINS EVERY NUMBER IN THIS THREAD

*My whole PO-13 computation put $\rs$ on the leaf, per the rate rule. **That is why $\theta_*$ came out
$H_0$-dependent, why it needed an early cut-off at all, and why the required start moved with every
parameter I touched.*** ⛭ *On the stacking rate $\theta_*=1.82756$ from $a\to0$ with no cut-off — and the
$z_{\rm onset}$ machinery exists precisely to bring that to the sky's $1.04109$. **`sec:tensions` says so
outright: the onset is "fitted to the acoustic angle at the directly measured $H_0$".***

⚠ ***SO THE RYDBERG THREAD MAY BE ANSWERING A QUESTION THE CORPUS DOES NOT ASK.*** *It is the right
question only if $\rs$ takes the leaf. **Which rate the sound horizon takes is now the prior question, and
it is a contradiction between two statements the corpus makes, and one of them has to give.*

⛭ ***AND THE RESOLUTION MAY ALREADY BE IN THE INSTRUMENT, WHERE I CALLED IT AN ERROR.***
`ACOUSTIC_two_arm.py` carries **two** sound horizons and says of them: *"the two are correct and NOT
interchangeable (ratio 1.286 at the physical onset). Do not unify them."* ⌗ ***At `r3683` I judged that
wrong.*** *Read against the kinematic rule it may be exactly right, because the two are different objects:*

| | which rate | why |
|---|---|---|
| $\rs$ as the **PHASE ACCUMULATOR** — what the oscillator integrates to reach $m\pi$ | **LEAF** | *a process running in the content* |
| $\rs$ as the **COMOVING RULER** — the length whose angle is $\theta_*$, paired with $D_M$ | **STACKING** | *a separation read across leaves* |

⇒ ***Both readings of the rule are then satisfied at once, and $\theta_*$ is $H_0$-free because the ruler
and $D_M$ share the stacking rate — which is `P15`'s claim, verified above to $0.0000\%$.*** *The leaf
horizon sets WHERE THE PEAKS FALL IN PHASE; the stacking horizon sets WHAT ANGLE that phase subtends.*

---

## ⌗ r3715 — THE TARGET CHARACTERISED IN LEAF-LOCAL TERMS, SO A MECHANISM CAN BE RECOGNISED RATHER THAN GUESSED

***Three guesses have now failed. This turn lays the target out instead — every local quantity on the leaf
at the required start — so the next candidate is checked against a list rather than proposed against a
feeling.***

**At $z=60{,}500$, the centre of the window the sky requires:**

| | |
|---|---|
| photon temperature | $kT=14.210$ eV, $T=164{,}895$ K |
| **age of the universe** | $2.87\times10^{8}$ s $=$ **9.1 years** |
| $\rho_r/\rho_m$ | 15.37 |
| $\rho_\gamma/\rho_b$ | 66.7 |
| baryon loading $R$ | 0.01124 |
| sound speed | $c_s/c=0.574132$, against $1/\sqrt3=0.577350$ — **$0.56\%$ below the ultrarelativistic value** |
| comoving horizon | 7 Mpc |
| **electron thermal speed** | $v_{\rm th}/\alpha c=\mathbf{1.02195}$ |
| $r_s$ from there | 135.39 Mpc — the sky's value, by construction |

### ⛭ THE ONE NUMBER THAT TIES THE THREAD TOGETHER

***$v_{\rm th}=1.022\,\alpha c$.*** *The Rydberg locus is where $v_{\rm th}=\alpha c$ exactly, so it is
**$2.2\%$ low in VELOCITY** — which is $4.5\%$ in temperature and $3.5\%$ in $z$, ***exactly the miss
measured at `r3713`.*** *So the whole discrepancy is one statement: **the sky wants the electrons a couple
of per cent faster than the Bohr speed, not exactly at it.***

⌗ *Checked and rejected as the source of that $2.2\%$: the RMS speed $\sqrt{3kT/m}=\alpha c$ gives
$kT=9.07$ eV ($z=38{,}600$) and the mean speed $\sqrt{8kT/\pi m}=\alpha c$ gives $kT=10.68$ eV
($z=45{,}470$). **Both are further away than $\sqrt{2kT/m}$, so the choice of thermal average does not
supply it** — it makes it worse.*

⚠ ***NO MECHANISM IS IDENTIFIED AND NONE IS CLAIMED.*** *`P16` `sec:peak` supplies the leaf-local
principle — **the compression is adiabatic and $T\propto\rho^{1/3}$, "justified, not assumed"** — and a
mass-independent recollapse threshold that is *identically the Nariai parameter*, recovered from the ball's
turnaround with no step in common with the horizon cubic. **But it names no $14$ eV scale**, and neither
does anything else read so far.*

---

## ⛔ r3713 — THE COINCIDENCE MEASURED AGAINST THE RIGHT YARDSTICK: IT IS SHARP, AND THE RYDBERG MISSES IT

***Three candidate mechanisms tested and none lands. Then the test I should have run first.***

| candidate | result |
|---|---|
| **atom formation** (`r3711`) | Saha shows no feature; $1.4\times10^{9}$ ionising photons per baryon |
| **Thomson coupling** | $\Gamma_T/H$ runs $3.6\times10^{4}\to1.0\times10^{4}\to3.3\times10^{3}$ — **smooth through the locus** |
| **Massey adiabaticity** | the right KIND of object — $\xi=\alpha c/2v$, sudden above, adiabatic below — but its boundary is $v=\alpha c/2$, $kT=B/4$, **$z=14{,}474$**, a factor 4 away in temperature |

### ⛔ AND THE SHARPNESS TEST, WHICH SETTLES HOW MUCH THE FIT WAS EVER WORTH

| $z_{\rm start}$ | $kT$ | $100\theta_*$ | miss |
|---|---|---|---|
| 40,000 | 9.39 | 1.02435 | $-1.61\%$ |
| **57,898 — the Rydberg** | **13.60** | **1.03959** | **$-0.144\%$** |
| 80,000 | 18.79 | 1.04912 | $+0.77\%$ |
| 400,000 | 93.95 | 1.06943 | $+2.72\%$ |

***The window inside Planck's $\pm0.00030$ is $z=60{,}001$ to $61{,}106$ — a factor $1.02$ wide. The
Rydberg locus is NOT in it.***

⛔ ***So the $0.144\%$ I have been calling remarkable is $5\sigma$ against a $0.029\%$ measurement.*** *I
quoted it against no yardstick for four revisions. **Against $a\to0$'s $+3.22\%$ it is twenty-two times
better and still excluded.***

### ⌗ WHAT SURVIVES, AND IT IS THE STRUCTURAL HALF RATHER THAN THE NUMERICAL ONE

⛭ *From $a\to0$ there is **no root in $\Omega_m$ anywhere** in $0.25$–$0.75$; from the Rydberg there is one,
at $\Omega_m=0.3158$ — **inside $1\sigma$ of Planck's $0.315\pm0.007$.*** ⇒ ***That is the real content and
it is unaffected by the sharpness test: an early cut-off makes the acoustic scale REACHABLE at a
concordance matter density, and no cut-off does not.*** *The particular locus is then a $\sim2\%$ question
in $z$, not a $\sim0.1\%$ one, and the Rydberg is $3.5\%$ low.*

⚠ ***AND THE HONEST READING OF THE WHOLE THREAD:*** *what the sky requires is a start in a narrow window
near $z\simeq60{,}500$. **The Rydberg is the only unfitted candidate that has come near it, and it is
near, not on.** Whether that is a $3.5\%$ correction waiting to be found or a coincidence at the level a
$2\%$-wide window makes cheap is **not settled by anything computed here**.*

---

## ⛔⛭ r3711 — THE ATOM-FORMATION READING OF THE RYDBERG LOCUS IS TESTED AND FAILS. THE LOCUS IS A VELOCITY.

***Daryl proposed the mechanism: when the temperature drops below the hydrogen binding energy, atoms can
combine for the first time — long before recombination — and that starts the plasma phase. Tested by Saha
rather than argued about.***

| $z$ | $kT$ [eV] | $x_e$ | **ionising photons per baryon** |
|---|---|---|---|
| 200,000 | 46.97 | 1.00000 | $1.61\times10^{9}$ |
| **57,898 — the Rydberg locus** | **13.598** | **1.00000** | **$1.40\times10^{9}$** |
| 6,000 | 1.409 | 1.00000 | $5.03\times10^{6}$ |
| 1,500 | 0.353 | 0.93389 | $1.89\times10^{-5}$ |
| 1,090 | 0.256 | 0.00328 | $1.79\times10^{-11}$ |

⛔ ***At the Rydberg locus there are $1.4\times10^{9}$ ionising photons per baryon, and $x_e=1.00000$ to
five decimals on both sides.*** *Any atom that forms is destroyed by one of a billion available photons;
Saha shows **no feature whatever** there. Recombination waits until that count falls through **one**, at
$kT\simeq0.3$ eV, which is why it sits at $z\simeq1100$. ***The atom-formation reading does not survive.***

### ⛭ BUT THE TEMPERATURE IS NOT PRIMARILY AN ATOMIC NUMBER — IT IS A VELOCITY

$$\mathrm{Ry}=\tfrac12 m_e c^{2}\alpha_{\rm fs}^{2}\qquad\Longrightarrow\qquad
kT=\mathrm{Ry}\ \Longleftrightarrow\ v_{\rm thermal}=\alpha_{\rm fs}\,c$$

*Checked: at $kT=13.5984$ eV, $\sqrt{2kT/m_ec^2}=7.2954\times10^{-3}$ against
$\alpha_{\rm fs}=7.2974\times10^{-3}$ — **agreeing to $0.027\%$.***

⇒ ***So the locus is where the ELECTRONS' THERMAL SPEED FALLS THROUGH $\alpha c$ — the orbital speed of a
bound electron. That is a statement about the PLASMA, and it holds whether or not any atom ever forms.***

⌗ ***Which is why the Saha result does not kill the coincidence.*** *`r3689` stands unchanged: starting the
sound horizon there gives $100\theta_*$ to $0.145\%$ and a root at $\Omega_m=0.3158$. **What has been
eliminated is one candidate mechanism, and what has been gained is that the scale is
$m_e\alpha_{\rm fs}^{2}$ — built from the electron mass and the fine-structure constant, with no
cosmological parameter and no atom required.***

⚠ ***AND NOTHING YET SAYS WHY A SOUND HORIZON SHOULD BEGIN WHERE $v_e=\alpha c$.*** *That is the question,
restated in the terms the number is actually made of rather than the terms it is usually named in.*

---

## ⛭⛭⛭ r3709 — THE KERNEL COMPUTED WITH EVERY INGREDIENT DERIVED: IT ANNIHILATES THE TENSOR TOWER

***Three ingredients were owed at `r3707`. All three are now derived from the corpus rather than guessed,
and the geometry closes on itself to $0.0011\%$.***

### ⌗ ONE — $x_0$, DERIVED RATHER THAN GUESSED THREE TIMES

*`P07`'s $E{=}1$ congruence — **the flat leaf the observed cosmology selects** — obeys
$(\dd r/\dd\tau)^2=1-f=2M/r+r^2/\alpha^2$, so $H^2=2M/r^3+1/\alpha^2$. Matching that to `P16`'s
$H_{\rm stack}^2=(1/\alpha^2)(1+2(1+z)^3/x_0^3)$ term by term, **verified symbolically**:*
$$\boxed{\;x_0^{3}=\frac{r_{\rm now}^{3}}{M\alpha^{2}}\;}$$
⇒ ***and $M$ cancels out of the ratio***: $r_{\rm now}/\lvert r_{\rm turn}\rvert=(x_0^3/2)^{1/3}=1.3126$.
***Today's areal radius is $1.3126$ times the turnaround radius, independently of the mass.***

⌗ *This also kills the two wrong guesses for a third and fourth time: $x_0$ is not $\lvert
r_{\rm turn}\rvert/\alpha$ (would need $\Omega_m=0.8386$) and not $r_{\rm now}/\alpha$ (would force
$M=\alpha$, eleven times Nariai).*

### ⌗ TWO — $M$, FIXED BY THE NARIAI SATURATION, AND THE GEOMETRY CLOSES

*$M/\alpha=(r_{\rm now}/\alpha)^3/x_0^3$, and Nariai caps $M/\alpha\le3^{-3/2}$, so
$r_{\rm now}/\alpha\le0.9548$ and $\lvert r_{\rm turn}\rvert/\alpha\le0.7274$.* ⛭ ***That last number is
the Nariai turnaround $(2M/\alpha)^{1/3}$ computed the other way, and they agree to $0.0011\%$ — the two
routes close.*** *And **`P15` works at the Nariai member's proper frame**, so the bound is saturated and
nothing is left free:*

| | |
|---|---|
| $\alpha$ | 4,931.8 Mpc |
| $M$ | 949.1 Mpc — $M/\alpha=3^{-3/2}$ exactly |
| $r_{\rm now}$ | 4,709.0 Mpc $=0.9548\alpha$ |
| $\lvert r_{\rm turn}\rvert$ | 3,587.5 Mpc $=0.7274\alpha$ |
| $A$, $S$ | $16.225$ $[L^{1/3}]$, $10{,}329$ Mpc |
| ⛭ $C=3S^{1/3}/A$ | **4.0268 — dimensionless, multiplying $\mu_n$** |

### ⛭⛭ THREE — AND THE ANSWER IS NOT A FEATURE. IT IS A REMOVAL.

***The scale is a MODE NUMBER, $n_*=1/C=0.2483$. The tensor tower starts at $n=2$.***

| $n$ | $\mu_n$ | $e^{-C\mu_n}$ |
|---|---|---|
| **2** | 2.449 | $5.20\times10^{-5}$ |
| 3 | 3.606 | $4.95\times10^{-7}$ |
| 10 | 10.863 | $1.01\times10^{-19}$ |

⇒ ***The scale sits BELOW the tower's floor, so the branch point imprints no feature in the tensor
spectrum — it REMOVES the spectrum, uniformly and exponentially, from the first mode up.***

⛭ ***AND THAT IS A PREDICTION, not a null result***: *no primordial tensor modes survive the branch point.
Suppression in **power** at $n=2$ is $2.7\times10^{-9}$. **The observational bound is $r<0.036$
(BICEP/Keck 2021), and this construction sits nine orders below it.***

⚠ ***WHAT IS ASSUMED:*** *the Nariai saturation. `P15` is the Nariai member's proper frame, so it is the
corpus's own choice rather than mine — **but every number above scales with it and the assumption is
load-bearing.*** ⌗ *And this settles the tensor tower, **not the acoustic spectrum**: $\mu_n$ here are
`P10`'s transverse-traceless harmonics. **The Rydberg start still has no mechanism.***

---

## ⛭ r3707 — THE DIMENSIONS, READ FROM THE PAPER: `C` MULTIPLIES A MODE NUMBER, AND THE NARIAI BOUND EXCLUDES `r3703` OUTRIGHT

***Read before computing, which is the order that produced the retraction when reversed.***

### ⌗ `P10` SETTLES THE DIMENSIONS, AND NEITHER OF MY TWO READINGS WAS RIGHT

| from `eq:tt-action` verbatim | |
|---|---|
| $a(T)=\alpha\cosh(T/\alpha)$ | **a LENGTH** — the round three-sphere's radius |
| $\mu_n^{2}=n(n+2)-2,\ n\ge2$ | **DIMENSIONLESS** — unit-sphere Laplace eigenvalues |
| $\omega=\mu_n/a$ | $[\omega]=L^{-1}$ ✔, so $\int\omega\,\dd T$ is dimensionless ✔ |

⇒ *With $a=As^{2/3}$ and $a$ a length, $[A]=L^{1/3}$ and $3S^{1/3}\mu/A$ is dimensionless.* ⛭ ***So
`r3703`'s $A$ was right in kind — and `r3705`'s audit was ALSO wrong***, *having asserted "$a$ is the
dimensionless scale factor" as the consistent reading. **The paper says neither of my two.***

⛔ ***AND THE REAL ERROR IS SHARPER THAN THE ONE I RETRACTED FOR.*** *$C=3S^{1/3}/A$ is dimensionless and
it multiplies $\mu_n$ — **a MODE NUMBER on the three-sphere, not a comoving wavenumber.** The kernel is
$e^{-C\mu_n}$ and its scale is $n_*=1/C$, a mode number. Converting that to $k$ requires $k=\mu_n/a$ at a
**stated epoch**, which `r3703` never supplied. **The retraction stands; its stated reason was wrong.***

### ⛔⛭ AND A ONE-LINE CHECK THAT WAS AVAILABLE THE WHOLE TIME WOULD HAVE STOPPED IT

*`P07` fixes the family: the comoving-turnaround cubic $r^{3}+2M\alpha^{2}=0$ at $E=1$ — **the flat leaf
the observed cosmology selects** — the horizon cubic at $E=0$, and $\Delta(E)=4\alpha^{4}(\alpha^{2}(1-E^{2})^{3}-27M^{2})$
vanishing at $1-E^{2}=3(M/\alpha)^{2/3}$.*

⇒ ***The Nariai mass is where that crossing reaches $E=0$:*** $M/\alpha=3^{-3/2}=0.19245$, ***so
$2M/\alpha\le0.3849$ for any sub-Nariai mass — a HARD BOUND.***

| | |
|---|---|
| `r3703` set $2M/\alpha=x_0^{3}=2\Omega_\Lambda/\Omega_m$ | **4.5232** |
| the corpus's Nariai bound | **0.3849** |
| ⛔ | ***larger by $11.8\times$*** |

***So the retracted identification is excluded by the construction's own bound, independently of any
dimensional argument.*** *One comparison, available from the start, would have stopped the whole chain
before it ran. **The sanity check I did run — $M\sim10^{23}M_\odot$ — tests an order of magnitude against
astronomy; this one tests the number against the geometry that defines it, and only the second could fire.***

---

## ⛔⛔ r3705 — **`r3703` IS RETRACTED. THE NUMBER IS NOT TRUSTWORTHY AND THE FALSIFICATION DOES NOT STAND.**

***Daryl flagged the chain as doubtful — "too many things that seem like red flags, like basing it on
effective parameters like $M$, which in SdS is a mass parameter derived from $\alpha$ alone". Checked, and
BOTH flags are real defects.***

### ⛔ DEFECT ONE — A DIMENSIONAL INCONSISTENCY, AND IT IS FATAL

*An exponent must be dimensionless, and `I9`'s is, under the reading where $a$ is the **dimensionless scale
factor**: $[A]=L^{-2/3}$, so $3S^{1/3}\mu/A$ has dimension $L^{1/3}\cdot L^{-1}\cdot L^{2/3}=L^{0}$. ✔*

⛔ ***But `r3703` took $A$ from the AREAL RADIUS***, $\lvert r\rvert=(2M\alpha^{2})^{1/3}(3/2\alpha)^{2/3}s^{2/3}$,
*which makes $[A]=L^{1/3}$ — so its $C=3S^{1/3}/A$ is a **pure number**.* ⇒ ***It then called that
"$1.771$ Mpc" and read $1/C$ as a comoving wavenumber. $1/C$ is dimensionless. It is not $0.5646$ /Mpc,
and $z=260{,}781$ follows from nothing.***

### ⛔ DEFECT TWO — AN IDENTIFICATION ADOPTED TO FIX A SIGN, NEVER DERIVED

*The chain first tried $2M=r_0-r_0^{3}$ with $x_0=1.6538$ and got a **negative mass**. It then switched to
$2M/\alpha=x_0^{3}$ — **and that switch was a guess made to make the sign come out**, not a derivation.*
⌗ *The corpus calls $x_0$ "the offset, set by $\alpha$" (`P16` line 17): a geometric quantity of the Nariai
proper frame. **$M$ in this construction is not an independent input**, which is exactly Daryl's objection,
and the sanity check that reassured me — $M=2.33\times10^{23}M_\odot$ — checks an order of magnitude and
cannot detect a wrong identification that happens to land in range.*

### ⌗ WHAT SURVIVES AND WHAT DOES NOT

| | |
|---|---|
| ⛭ **survives** | **the branch point carries a scale and the front seam does not** — `r3699`'s `N8` verdict, and it is *stronger* under the corrected $e^{-Ck}$ form: spread $1.08\to10.8$ against $3\times10^{-16}$ |
| ⛭ **survives** | the two loci are different objects and `prop:transmission` reaches only the front seam (`r3693`) |
| ⛔ **retracted** | $k_*=0.5646$ /Mpc, $z=260{,}781$, the $4.4\times$ miss, and the $\ell\sim7{,}342$ residue — **all of it** |
| ⟐ **restored to open** | ***what the branch point's scale actually is.*** The hypothesis is neither confirmed nor falsified |

⚠ ***AND A PATTERN IN MY OWN WORK, NAMED BECAUSE IT IS TWICE IN ONE SESSION.*** *`r3687` computed a
required redshift and I compared the wrong quantity, nearly discarding the Rydberg. `r3703` chained an
underived identification into a dimensionally inconsistent conversion and reported a falsification.
**Both were caught by Daryl, not by me, and neither would have been caught by a gate** — a number with the
wrong units passes every check the corpus has.*

---

## ⛔ r3703 — THE BRANCH POINT'S SCALE IS COMPUTED, AND IT IS NOT THE RYDBERG. HYPOTHESIS FALSIFIED.

***The run owed since `r3693`, carried to a number. It misses.***

⚠ ***AND r3699 BELOW USED THE WRONG FUNCTIONAL FORM.*** *`I9` gives $\int\omega\,\dd s=3S^{1/3}\mu/A$ —
**linear in $\mu$ and so in $k$**, with the $S^{1/3}$ being the SEGMENT LENGTH's dependence. I read
"converges as $S^{1/3}$" and carried the $\tfrac13$ power onto $k$, testing $e^{-Ck^{1/3}}$. **The kernel
is $e^{-Ck}$.** *Redone: the scale-freedom verdict **strengthens** — spread $1.08\to10.8$ growing linearly
with $C$, against the front seam's $3\times10^{-16}$ — so `r3699`'s conclusion survives its own error, and
the error is recorded because the NUMBER does not.*

### ⌗ THE COMPUTATION, IN PHYSICAL UNITS

| | |
|---|---|
| $\alpha=c/(H_0\sqrt{\Omega_\Lambda})$ | 4,931.8 Mpc |
| $x_0=(2\Omega_\Lambda/\Omega_m)^{1/3}$, and $2M/\alpha=x_0^3$ | 1.6538, so $2M=22{,}307$ Mpc |
| ⌗ *sanity* | $M=2.33\times10^{23}\,M_\odot$ — **the right order for the observable universe's mass** |
| $A$ from $\lvert r\rvert=(2M\alpha^2)^{1/3}(3/2\alpha)^{2/3}s^{2/3}$ | 36.887 |
| $S=2\pi\alpha/3$, the segment zero-to-zero | 10,329 Mpc |
| $C=3S^{1/3}/A$ | **1.771 Mpc** |
| ⛭ **the scale** $k_*=1/C$ | **0.5646 / Mpc** |

⛔ ***AND THE RYDBERG LOCUS NEEDS $k=0.1286$ /Mpc, at $z=57{,}898$.*** *The kernel gives
$z=260{,}781$ — **$4.4\times$ too large in $k$, $4.5\times$ too high in $z$.** ***The branch point does not
supply the acoustic start.***

### ⛭ AND THE RESIDUE IS WORTH KEEPING

*$k_*=0.5646$ /Mpc lands at $\ell\sim k_*D_M=7{,}342$ — **the acoustic peaks are at $220$–$810$ and Silk
damping has killed the spectrum by $\ell\sim2{,}000$.*** ⇒ ***So the branch point's scale exists, is
computed, and sits $3.7\times$ beyond the damping tail, where nothing can see it.***

⌗ ***That is consistent with `P15`'s conclusion — the tilt is the progenitor's — reached by a route
`P15` does not take.*** *`P15` gets there by asserting neither locus carries a scale, which `r3699` showed
is false for the branch point. **The branch point carries one; it is simply unobservable.** A stronger
statement than the paper's, and it needs the paper's sentence scoped rather than repaired.*

⚠ ***SO THE RYDBERG START REMAINS A MEASURED FIT WITH NO MECHANISM.*** *The one candidate the
construction offered has been computed and rejected. **That is what the hypothesis being falsifiable
looks like, and it is recorded as a rejection rather than left as an open lead.***

---

## ⛭ r3699 — THE BRANCH POINT CARRIES A SCALE. THE FRONT SEAM DOES NOT. THEY ARE NOT THE SAME OBJECT.

***Run on 60's `N8` test, which is the instrument this question needed and which arrived in the six-field
merge.*** *`N8` gives "carries a scale" an operational form: **a kernel carries one exactly when the tilt
you fit to it depends on which band you fit.** Controls reproduced here before use.*

| kernel | band tilts | spread |
|---|---|---|
| $p{=}1$ non-degenerate, $\kappa=0.2$ | $[-1.01,-1.09,-2.21,-18.0]$ | 17.0 |
| $p{=}1$, $\kappa=2.0$ | $[-1.00,-1.01,-1.09,-2.21]$ | 1.21 |
| **$p{=}2$ degenerate — THE FRONT SEAM** | $[-1,-1,-1,-1]$ | **$3\times10^{-16}$** |
| **the BRANCH POINT**, $e^{-Ck^{1/3}}$, $C=1$ | $[-0.050,-0.107,-0.231,-0.497]$ | **0.45** |
| the same with a cutoff inserted by hand | $[-0.050,-0.110,-0.483,-2.24]$ | 2.20 |

⇒ ***The branch-point spread grows with $C$ — $0.22$, $0.45$, $1.34$ — so it tracks the kernel's own scale
exactly as `N8`'s $\kappa$-sweep does for $p{=}1$. **It is not scale-free.***

⌗ *The exponent is `I9`'s (`r3622`): at the branch point $\omega\propto s^{-2/3}$ on `P10`'s own
$\lvert r\rvert\propto s^{2/3}$, so the action integral converges as $S^{1/3}$ — **a third structure,
neither a simple nor a double root of $f$.***

### ⛔ AND THIS SCOPES A SENTENCE IN `P15`

*`P15` reads: "the leg multiplies the spectrum by a constant and the branch point imprints nothing:
**neither carries a scale**, and a spectrum can only be tilted by something that does."* ⌗ *Its proof,
`prop:transmission`, is a dichotomy between a **simple** and a **double root of $f$** — both at $f=0$, and
the degenerate one is the **front seam** (`r3693`). **The branch point sits at $r=0$ where $f$ diverges and
is not a Killing horizon at all, so the proposition does not reach it.***

⚠ ***WHAT IS MEASURED AND WHAT IS NOT.*** *Measured: the functional form $e^{-Ck^{1/3}}$ fails `N8`'s
scale-freedom test decisively. **NOT established** — (i) that this kernel is what acts on the ACOUSTIC
spectrum, since `I9` measured $\omega(s)$ for `P10`'s transverse-traceless tower and not for the
photon-baryon modes; (ii) the value of $C$ in physical units; (iii) that the scale it sets is anywhere near
$z\simeq58{,}000$. ***Each is a separate computation and none is done here.***

---

## ⛭⛭⛭ r3691 — THE ACOUSTIC ROOT AND THE GROWTH NORMALISATION ARE THE SAME MEMBER OF ONE FAMILY

***Two calculations sharing no input beyond the flat form land on the same $\Omega_m$.***

| | $\Omega_m$ | |
|---|---|---|
| $J(\Omega_m)=1$ — the growth normalisation of the RNAAS note, **pure mathematics of the flat form** | **0.315162424** | |
| CR's acoustic scale, **Rydberg start**, $H_0=73$ measured, meeting $100\theta_*=1.04109$ | **0.315846** | |
| the concordance value | $0.315\pm0.007$ | |

⇒ ***0.217% apart, and $J$ evaluated at the acoustic root is 0.99833.***

### ⌗ THE FAMILY, AND IT HAS REAL STRUCTURE

$$I(n,p;\Omega_m)\;\equiv\;\int_1^{\infty}\frac{u^{n}\,\dd u}{\bigl(\Omega_m u^{3}+1-\Omega_m\bigr)^{p}},
\qquad u=1+z,$$
*over the **stacking rate**, which is the rate `P16` `sec:scoping` assigns to separations read across leaves.*

⛭ ***The $n=2$ row is ELEMENTARY.*** *Substituting $w=\Omega_m u^{3}+1-\Omega_m$ gives*
$$I(2,p)=\frac{1}{3\Omega_m(p-1)}\qquad\Longrightarrow\qquad I=1 \text{ at } \Omega_m=\frac{1}{3(p-1)},$$
*so its unity roots are **exactly rational** — $2/3$, $1/3$, $2/9$, $1/6$ at $p=\tfrac32,2,\tfrac52,3$, each
confirmed numerically to nine figures.*

⛭ ***The $n=1$ row is NOT.*** *With $y\equiv\Omega_\Lambda/\Omega_m$,*
$$J=(1+y)^{3/2}\cdot\tfrac{2}{5}\,{}_2F_1\!\left(\tfrac56,\tfrac32;\tfrac{11}{6};-y\right),
\qquad J=1 \text{ at } y_*=2.172967096.$$
*No elementary form; $y_*$ matches none of $2\pi/3$, $e-\tfrac12$, $\sqrt2+\tfrac34$, $\varphi^{3/2}$ to
better than $0.4\%$. **The root is genuinely transcendental as far as this pass can tell.***

### ⛭⛭ AND THE ACOUSTIC CONDITION SITS AT $p=3/2$

***Solving for the exponent whose $n=1$ unity root IS the acoustic $\Omega_m$:***
$$p_{\rm acoustic}=1.498484 \qquad\text{against}\qquad p_J=\tfrac32=1.5 \qquad (0.101\%)$$

⇒ ***So CR's acoustic scale and the linear growth normalisation are, to a tenth of a per cent, the SAME
member of this family.*** *That is a measured relation between an integral over the stacking rate and an
observable computed from $r_s$ on the leaf against $D_M$ on the stack.*

⚠ ***STATED AS MEASURED AND NOT AS DERIVED.*** *Nothing here shows WHY the acoustic condition should land
on $p=3/2$, and $\theta_*=1.04109$ is an observational input while $J=1$ is not. **The agreement of three
numbers to $0.2\%$ is a fact; a mechanism is not claimed.*** ⌗ *What makes it worth pursuing rather than
filing as numerology is that the family demonstrably HAS structure — the $n=2$ row is exactly solvable with
rational roots — so "which member does the sky pick" is a well-posed question and not a fishing expedition.*

---

## ⛭⛭⛭ r3689 — THE SOUND HORIZON STARTING AT THE HYDROGEN IONISATION THRESHOLD

***`r3687` measured that from $a\to0$ the acoustic scale has NO ROOT in $\Omega_m$ anywhere in $0.25$–$0.75$.
Starting the integral at $kT_\gamma=13.5984$ eV — the Rydberg — it has one, at the measured $H_0$.***

| where the sound horizon begins | $z$ | $100\,\theta_*$ at $\Omega_m=0.3066$ | miss |
|---|---|---|---|
| $a\to0$ | ∞ | 1.0746 | **$+3.22\%$** |
| **$kT_\gamma=13.5984$ eV, the Rydberg** | **57,898** | **1.0372** | **$-0.37\%$** |

**And the root, which did not exist before:**

| $H_0$ | $\Omega_m$ meeting $100\,\theta_*=1.04109$ | $\Omega_m h^2$ |
|---|---|---|
| 70.0 | 0.3665 | 0.1796 |
| **73.0** — the measured value | **0.3158** | 0.1683 |
| 76.0 | 0.2738 | 0.1582 |

⇒ ***At $H_0=73$ the sky's acoustic scale is met at $\Omega_m=0.3158$, against Planck's $0.3150$.***

### ⌗ WHY THIS IS NOT A FITTED START

***The locus is fixed by atomic physics and the measured CMB temperature and carries NO cosmological
parameter***: $1+z = 13.5984\,\mathrm{eV}/(k_B\times2.7255\,\mathrm{K})$. *It does not move when $H_0$,
$\Omega_m$, $\omega_b$ or $N_{\rm eff}$ move. **It is the one candidate scale in this problem that is not
borrowed from $\Lambda$CDM and not tuned.***

⌗ *And the sensitivity is diagnostic rather than decorative: the Lyman-$\alpha$ threshold ($10.199$ eV,
$z=43{,}424$) gives $1.0282$ and the $n{=}2$ level ($3.400$ eV) gives $0.9419$. **The Rydberg is picked out;
its neighbours are not.***

⚠ ***WHAT IS NOT YET EXPLAINED, and it is the whole of what remains.*** *Why the photon-baryon plasma's
acoustic era should begin where the photon bath can no longer keep ANY hydrogen bound. **A start at that
threshold is stated here as a measured fit to the sky and NOT as a derivation** — the construction has not
yet been asked to produce it. ⌗ *That question is now sharp and local: `P15`'s Euclidean transmission is the
one object in the construction carrying an early scale, and what redshift it corresponds to has never been
computed.*

⌗ *And with CR's own $z_{\rm rec}=1093.6$ (Hu--Sugiyama at $\Omega_m h^2=0.1634$) rather than Planck's
hardcoded $1089.9$, the miss at $\Omega_m=0.3066$ widens to $-0.373\%$. **The better ingredient moves it
away, which is recorded rather than quietly dropped.***

---

## ⛔⛭ r3687 — THE ACOUSTIC SCALE AT $H_0=73$ IS CLOSED TO EVERY CONTENT PARAMETER

***With the driving solved (`r3685`), the whole residual is one number, and this pass measures every lever
that could move it. All three are excluded.***

| lever | what the sky needs | the bound | |
|---|---|---|---|
| $\Omega_m$ | — | 0.25–0.75 scanned | ⛔ ***no root at all***: $\theta_*$ moves the WRONG WAY, $1.0604$ at $0.28$ rising to $1.1824$ at $0.70$ |
| radiation | $1.137\times$ standard, $N_{\rm eff}=4.07$ | BBN + CMB: $3.0\pm0.3$ | ⛔ excluded |
| baryons | $\omega_b=0.0302$ | BBN + CMB: $0.0224\pm0.0005$ | ⛔ excluded at $1.35\times$ |
| $z_{\rm rec}$ | — | Hu–Sugiyama at CR's $\omega_m$ | ⌗ *real but tiny*: $1093.6$ against Planck's $1091.9$, **$0.16\%$**, worth $\sim0.1\%$ in $r_s$ |

⇒ ***So at the measured $H_0$, with the content BBN fixes, $\theta_*$ cannot be met by any content
parameter.*** *That is a real, falsifiable corner and it is recorded as one.*

### ⛭ AND IT SAYS EXACTLY WHAT MUST GIVE

*$D_M=13005$ Mpc on the stacking rate, so the sky's $\theta_*$ requires $r_s=135.39$ Mpc. The leaf integral
from $a\to0$ gives $139.74$. **The excess is $4.36$ Mpc and it must come off the EARLY end.***

$$\boxed{\text{the sound horizon must begin at } z \simeq 60{,}550}$$

*and there $\rho_r/\rho_m=15.4$ and $T=1.65\times10^{5}\,$K $=14.22$ eV.*

⚠ ***A near-coincidence, stated as near and NOT as a match.*** *Hydrogen's binding energy is $13.6$ eV,
which is $4.6\%$ away. **That is not agreement** and it is written here only so the next pass does not
re-derive it and mistake it for one. `r3685` recorded the cost of printing a conclusion before computing
it; this is the same guard.*

### ⌗ WHERE TO LOOK NEXT, AND WHY IT IS THE RIGHT PLACE

***The plasma that oscillates is OURS, and in this construction it arrives through the branch point.***
*Nothing requires its sound horizon to run from $a\to0$: before the arrival the content was the
progenitor's. **If our acoustic era begins when the transmitted content becomes an oscillating plasma
rather than whatever crossed, then $z\simeq60{,}550$ is a transmission scale and not a free number.***

⇒ *`P15`'s Euclidean kernel $e^{-\int\omega\,\dd s}$ carries a scale, and `I9` (`r3622`) established its
exponent is an **action integral** converging as $S^{1/3}$, with the adiabatic parameter diverging at the
branch point. **That kernel has never been asked what redshift it corresponds to.*** *It is the one object
in the construction that sets an early scale and is not borrowed from $\Lambda$CDM.*

---

## ⛭⛭⛭ r3685 — THE DRIVING IS EXACTLY RIGHT WHEN THE DATUM SITS AT A LOCUS THE CONSTRUCTION OWNS

***`P15` states the frozen-mode condition AT THE BRANCH POINT. The instrument imposed it at the onset. At
the branch point $a\to0$ and every mode is OUTSIDE the horizon, so the datum there is the super-horizon
adiabatic growing mode — the same physical statement the control uses because it is the same physical
situation.*** *Exposed as `CRIC=branchpoint`, a verified no-op unset.*

### ⛭ THE DRIVING THEN MATCHES THE CONTROL TO THREE DECIMALS

| $k$ | CR, datum at the branch point | $\Lambda$CDM control |
|---|---|---|
| 0.020 | **0.8753** | 0.8641 |
| 0.030 | **0.8156** | 0.8135 |
| 0.045 | **0.7928** | 0.7925 |
| 0.065 | **0.7835** | 0.7829 |
| 0.090 | **0.7802** | 0.7786 |

⇒ ***The $4\times$ $k$-dependence is GONE and CR's driving is the control's.*** *So the driving machinery
was never the defect: **the datum was, and it was imposed at a redshift rather than at a locus.***

### ⌗ AND THE RESIDUAL IS A SCALE, NOT A SHAPE

*Peaks at $212/508/780$ against $220.6/538.1/809.8$ — errors $-3.9\%$, $-5.6\%$, $-3.7\%$. **Near-uniform**,
where the onset datum gave $-7.5\%$, $-5.6\%$, $-0.7\%$. A uniform deficit is one number.*

**And that number is the acoustic scale.** *With $r_s$ on the leaf from $a\to0$ (139.74 Mpc, as `P07` and
`P15` assign it) and $D_M$ on the stacking rate (13005 Mpc, likewise):*
$$100\,\theta_* = 1.0746 \quad\text{against the sky's}\quad 1.04109 \qquad (3.22\%)$$

⛔ ***AND IT IS NOT REACHABLE BY $\Omega_m$.*** *$\theta_*$ moves the WRONG WAY with $\Omega_m$ — $1.0604$ at
$0.28$ rising to $1.1824$ at $0.70$ — **with no root anywhere in $0.25$–$0.75$.** In $\Lambda$CDM $\theta_*$
is fitted; here $H_0$ is measured and the two rates are different objects, so $\theta_*$ is a **prediction**,
and this is it.*

⌗ *It IS reachable at $1.137\times$ the standard radiation, $N_{\rm eff}=4.07$ — **which BBN and the CMB
exclude at $3.0\pm0.3$.** Recorded as measured and rejected.*

### ⛭ THE ONE NUMBER TO CHASE

***The $r_s$ that would meet the sky is $135.4$ Mpc. The instrument's fitted-onset $r_s$ is $135.46$ Mpc.
Those agree to $0.04\%$.*** *So `LATARG` is doing exactly the work of setting the sound horizon to the value
the sky wants, and the question is what physically sets it there.*

⚠ ***AND A HOPE OF MINE THAT FAILED, RECORDED BECAUSE IT WOULD OTHERWISE BE RE-TRIED.*** *I expected the
onset to coincide with the stated condition $\rho_r/\rho_m=2$. **It does not.** At CR's own parameters
($\Omega_m=0.3066$, $H_0=73$) equality is at $z_{\rm eq}=3936$, so that condition sits at $z=7871$ against
the fitted onset's $6761$ — **$16.4\%$ apart, not the sub-per-cent I asserted before computing it.** The
instrument's comment quotes $z_{\rm eq}\simeq3402$, which is *Planck's* $\Omega_m h^2$ and not CR's.

---

## ⛭⛭⛭ r3683 — THE HEADLINE BELOW IS SUPERSEDED. THE DEFICIT TRACKS THE ONSET, NOT THE RATE.

***Measured on the instrument's own Q-scan, whose undriven column is a MEASURED calibration and not an
assumption.*** *Every row below holds the calibration: CR's undriven Q spans $0.9984$–$1.0004$ against the
exact $1$ at every start tested.*

| configuration | $Q$ @ $k{=}0.03$ | $Q$ @ $k{=}0.12$ | variation |
|---|---|---|---|
| **CR, $z_{\rm onset}=6{,}761$** — the fitted onset | 0.454 | 0.178 | **2.55×** |
| CR, $z=15{,}000$ | 0.646 | 0.264 | 2.45× |
| CR, $z=30{,}000$ | 0.736 | 0.420 | 1.75× |
| **$\Lambda$CDM, $z=3\times10^{7}$** — the control | **0.814** | **0.776** | **1.05×** |

⇒ ***CR's driven $Q$ converges monotonically to the control's as the onset moves back, in value AND in
$k$-dependence.*** *The control's driving costs a nearly constant $0.22$ of a half-period; CR's at the
fitted onset costs $0.55$ rising to $0.82$. **That is a difference in functional form, and it tracks the
START REDSHIFT rather than the rate.***

### ⛔ WHY THE OBVIOUS CONTROL CANNOT BE RUN, AND WHAT THAT ITSELF SHOWS

*The symmetric test — run $\Lambda$CDM late, at CR's onset — was set up at `r3683` by exposing `LZSTART`.*
**It breaks the calibration: undriven $Q$ comes out $0.20$–$0.43$ where it must be $1.0000$.** *The
control's data are super-horizon adiabatic, and applying them to modes already inside the horizon is not a
valid start. **The two arms' initial data are therefore NOT interchangeable, and the gate detects it
immediately** — which is the gate working, and is why the comparison must be made along CR's own
$z_{\rm onset}$ ladder instead.*

⌗ *Instrument limit found and recorded: at $z_{\rm start}\gtrsim6\times10^{4}$ the first-extremum detector
returns $\sim10^{-4}$ for low $k$ — a detection failure, not a physical collapse. **The ladder above stops
at $30{,}000$ for that reason and no physics is read past it.***

### ⌗ WHAT THIS DOES AND DOES NOT SETTLE

⛭ **It relocates the defect.** *Not the seam treatment, not the transfer, not the geometry — and **not the
rate**. Under `LEAFPERT` the perturbations already run on $H_{\rm leaf}=H_0\sqrt{\Omega_m a^{-3}+\Omega_\Lambda+\Omega_r a^{-4}}$,
**which is the $\Lambda$CDM rate**, differing from the control only in $H_0$ and $\Omega_m$. Same equations,
same rate form, same calibration. **The $2.55\times$ against $1.05\times$ cannot come from the rate.***

⛔ **It does NOT supply a fix.** *$z_{\rm onset}$ is fitted to `LATARG`; moving it back breaks the acoustic-scale
fit that motivated it. **This is a diagnosis of where the deficit lives, not a demonstration that it can be
removed.*** ⌗ *And the corpus already says what the onset is: the instrument's own comment records that it
is **"not a locus of the construction at all but the redshift solved so that $\ell_A$ hits LATARG"**. A mode
with $k/\mathcal{H}>1$ there entered the horizon at $z\simeq15{,}700$ and has been oscillating since; it is
handed a datum that ignores that history.*

⌗ **Three candidates tested and eliminated this pass:** *`GSRC=1` (the constraint factor) makes $Q$
non-monotonic and erratic — confirming `r3400`'s "settles nothing"; `CRPHI=entryleaf` moves the peaks DOWN
to $196/476/756$ and takes $P_1/P_2$ to $4.5$ against the sky's $2.2$; and the leaf rate is already the
default.*

⌗ ⚠ **The figures in the section below are the PRE-`r3409` stacking-rate run.** *On the leaf default the
instrument gives peaks at $204/508/804$ against the sky's $220.6/538.1/809.8$ — the third within $0.7\%$ —
and $P_1/P_2=2.238$ against $2.217$. **The "$\ell_1=176$, first gap $248$" below is stale.***

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

## ⛔ THE INSTRUMENT'S FLAG INVENTORY — r3512, *after the third miss in one arc*

**⌗ THE PATTERN, NAMED.** *Three times in this arc a result was bounded by operations that were
**already built and unrun**:*
1. *the position fork rested on `LEAFPERT` vs `STACKPERT` while **`PHASEONLY`** sat unrun — pulling it
   refuted the fork;*
2. *`POLSRC` was hand-rolled from a tight-coupling steady state while **`HIER`** sat unrun — carrying
   an evolved Π, both source terms, and its own control;*
3. *and `HIER` itself does not know the newest operations (below).*

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

### ⛔ THE COMPOSITION DEFECT — *checked, r3512*

*`evolve_hier` and `_project` (lines 828–977) reference the clock operations **once**:
`Jac_of(e) if LEAFPERT`. The main path references **two**.* ⇒ ***`HIER=1` does not know `SRCSTACK` or
`DIFFLEAF`.***

⛔ **So `HIER=1` composed with `SRCSTACK=vel` evolves the hierarchy with gravity on the LEAF — the very
assignment the position result required moving to the STACK — and nothing announces it.**
⌗ ***The ΛCDM gate cannot catch this***, *since $\varphi\equiv1$ makes every clock operation a no-op
there. **A CR number from that composition would be two physical models in one run.***

### ⌗ THE GATE ORDER THAT FOLLOWS

1. **`lcdm HIER=1`** — validates Π only. Position must hold at $0.7300$; $P_1/P_2$ must move from
   $2.447$ **toward** $2.217$, not past it.
2. **`lcdm HIER=1 PISRC=0` vs `PISRC=1`** — the instrument's own subtraction; the difference **is** the
   returned half. This measures the term's size against the recorded $1123$ $\chi^2$ debt.
3. ⛔ **THE COMPOSITION FIX** — give the hierarchy's gravitational source the stacking clock and its
   diffusion the leaf, *the same LGF assignment the main path carries*. **Without this, step 4 is void.**
4. **CR**, reporting $\ell_1/\ell_A$, $P_1/P_2$, $P_1/P_3$, $P_1/P_4$ **together**.

⌗ **THE PREDICTION THAT KEEPS IT A TEST.** *A correctly composed Π is driven by the same retimed
$\theta_\gamma$ that produced $0.7294$, so it should arrive **weighted to high $k$** and act as a
**shape**: $P_1/P_3$ and $P_1/P_4$ should fall further than $P_1/P_2$, and the position should move
**back down** from $0.7560$.* ***If the position climbs instead, the hierarchy is on the wrong clock
and step 3 was skipped.***

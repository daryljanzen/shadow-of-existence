---
name: PO13_WORKING_STATE
description: THE ACOUSTIC-PHASE OFFSET — the worked state of PO-13, held OUTSIDE the corpus. Not a paper, not a register row, not a route into either. Read before touching P15's acoustic sections.
status: WORKING DOCUMENT — deliberately not a paper
# ⛔⛭ r3899 — **EVERY CR NUMBER IN THIS FILE IS SUSPENDED: `r3870` FOUND THE k-INTEGRAL TRUNCATED**

***60's `PO-24` step one established that the instrument's $k$-integral was cut off where it is not
converged, and that this — not the projector alone — was the larger half of the height defect.***

| $k_{\max}$ ($\ell$-equivalent) | 900 | 1300 | 1800 | 2400 |
|---|---|---|---|---|
| $P_1/P_2$ | **2.721** | 2.446 | 2.399 | **2.393** |
| $P_1/P_3$ | **4.497** | 2.974 | 2.791 | **2.768** |

⇒ ***Repaired, the control reproduces CAMB: peaks $220/540/812$ against the sky's $220.6/538.1/809.8$,
and $P_1/P_2=2.1969$ against CAMB's $2.200$ — $0.14\%$.***

⛔ ***AND `r3870` IS EXPLICIT THAT IT CORRECTED THE CONTROL ARM ONLY***: *"no CR number is produced or
corrected. **The CR arm is truncated by the same mechanism.**"*

⇒ ***So every CR height figure below — $1.935$, $2.578$, and the $12.7\%$ / $13.2\%$ that go with them —
was produced at the truncated $k_{\max}$ and is SUSPENDED pending a re-run at `KFAC` converged.*** *The
positions ($204/508/804$) are not affected by the same mechanism on the control's evidence, but that
should be confirmed rather than assumed.*

⚠ ***And one claim of mine falls with them.*** *I wrote at `r3869`, into `PO-24`'s register row and the
`PO-24` handoff, that **"CR with the derived datum beats the control on both ratios, $12.7\%$ and
$13.2\%$ against $22.7\%$ and $97.5\%$."* **That comparison was against a control number now known to be
a truncation artefact.** *It compared a truncated CR run to a truncated control run and read the
difference as physics. Withdrawn until both arms are converged.*


# ⛭ r3548 (node 60): DECLARED-UNKNOWN, which is the true statement from this line — nobody
# here has brought this document current and its position is not known. Written because
# classifying it (it had gone unclassified since it was added, failing
# `classify_documents --check` on every push — and under the fast job's `set -e` that
# aborted the step before anything after it ran) made it visible to `check_currency` for
# the first time. ** Declaring ignorance is not declaring currency, and only the owning
# line can do the second. **
current: r4400
---


# ⛭⛭⛭ r4400 — **THE ~20% SPACING DEFICIT DOES NOT SURVIVE. IT IS NOT A DEFICIT AT ALL.**

***Found while working `check_receipts`' nine orphaned `P15` receipts, which is not where I expected
a physics result.*** *Three of the nine rest on a "$\sim20$–$21\%$ spacing deficit", and one states
it sharply enough to be tested at source:* `P15_the_first_peak_is_the_seam_datum_and_the_spacing_is_not`
*claims* **"the peak spacing at $0.79\pm0.04$ of $\ell_A$ under every phase and NEVER $1.0$."**

**Measured across RUN 2's seventeen admissible readings, converged in $k$, on the leaf congruence:**

| spacing / $\ell_A$ | min | max | mean | readings at or above $1.0$ |
|---|---|---|---|---|
| converged, leaf | **0.915** | **1.095** | **1.018** | **12 of 17** |
| the retired claim | 0.75 | 0.83 | 0.79 | none, "never $1.0$" |

⇒ ***THERE IS NO SPACING DEFICIT.*** *At the coded default the spacing sits $8.2\%$ **above** $\ell_A$,
not $21\%$ below, and the mean across the datum is $1.018$ — the spacing straddles $\ell_A$ rather than
falling short of it.*

⛔ ***SO THE ROBUST DISAGREEMENT THAT ARC IDENTIFIED IS GONE, AND WHAT REPLACES IT IS THE ONE r4136
FOUND.*** *That arc's reading was: the first peak's position is a seam-datum statement, and what is
robust underneath it is a $\sim21\%$ spacing deficit.* **Converged and on the assigned rate, the
spacing is not in deficit and the heights are — $-20.7\%$ and $-29.2\%$ against the sky where the
control sits at $-0.9\%$ and $-3.8\%$.** ⇒ *The disagreement did not disappear; it moved from the
spacing to the heights, which is why `sec:refit-bound` reports what it now reports.*

⌗ ***AND THIS IS WHY SIX OF THE NINE ORPHANS CANNOT SIMPLY BE RE-CITED.*** *Discharging
`check_receipts` by adding `\rcpt{}` markers would put the $0.5703$ first peak, the $21\%$ spacing
deficit and the $0.62\pi$ phase offset back into a section rewritten specifically to stop reporting
them.* **The gate's only discharge is a citation, so the six are a de-registration decision and not a
citation one — and that is a call on `P15`'s own registration, not this node's to make alone.**

⌗ *The other three are not superseded and are separable:*
`P15_the_derived_diffusion_damping` *(the damping derived per arm, which `PO-24` still rests on)*,
`P15_the_driving_shift_by_subtraction` *(the undriven-reference method r4164's subtraction uses, and
its $k$-dependence)*, and `P15_the_control_entered_the_regime_and_the_arm_did_not_move` *(the
$\chi^2/\mathrm{dof}=1.18$ on 185 lensed bins, which is the better-converged likelihood RUN 3's 133
unlensed bins should be set BESIDE rather than replace).*



# ⛭⛭⛭ r4236 — **RUN 3, THE LIKELIHOOD: THE TWO MODELS ARE ELEVEN SIGMA PER BIN APART. AND RUN 4
CORRECTS A POSITION FIGURE THAT IS LIVE IN TWO PAPERS.**

## ⛔ RUN 3 — the likelihood, both arms, identical settings, on `plik_lite` TT

*Polarisation path, `KFAC=2.0`, `LSTEP=2`, both arms scored on the SAME bins by the same code.*

| | $\chi^2$ | bins | $\chi^2$/bin | fitted amplitude | $\ell$ range |
|---|---|---|---|---|---|
| control | **279.4** | 133 | **2.10** | 11108 | 100–1296 |
| this arm | **15752.0** | 133 | **118.44** | 14229 | 100–1296 |
| cut at $0.8\,\ell_{\max}$: control | 175.7 | 104 | 1.69 | 11142 | 100–1035 |
| cut at $0.8\,\ell_{\max}$: this arm | 8533.0 | 104 | 82.05 | 14459 | 100–1035 |

⇒ ***THE FLOOR, MEASURED AS THE SPEC REQUIRES — a distance between the two MODELS and not a
difference of two numbers each taken against the sky:***

$$\chi^2_{\rm sep} = (A_a m_a - A_c m_c)^{\mathsf T} F (A_a m_a - A_c m_c) = \mathbf{16260.5}
\ \text{over 133 bins} = \mathbf{122.3\ per\ bin} = \mathbf{11.06\sigma\ per\ bin}.$$

**The arms are not close.** *`P15_the_floor_is_a_distance_between_models_not_a_number_from_the_data`
measured the control's own separation from a reference $\Lambda$CDM at $0.11$ $\chi^2$ per bin; this is
$122$.* ⇒ ***Three orders of magnitude above the level at which this statistic cannot arbitrate.***

⚠ ***AND THE CONTROL IS NOT AT THE NOISE FLOOR IN THIS CONFIGURATION, WHICH MUST BE SAID.*** *Its
$\chi^2$/bin is $2.10$, not $1$: `LMAXL` $=1300$ cuts the damping tail and the spectrum is unlensed,
where `c54.186` reached $\chi^2/{\rm dof} = 1.18$ on 185 bins with a lensed spectrum to $\ell=1996$.*
**So the ABSOLUTE $\chi^2$ values are configuration-limited.** *What is not configuration-limited is the
RATIO: the separation between the arms is $58\times$ the control's own distance from the data on the
same bins, and $F_2$ and $\chi^2_{\rm sep}$ agree to within $5\%$ ($15473$ against $16261$), so the
verdict does not turn on which measure is used.* ⇒ **The disagreement is not marginal and is not a
truncation artefact — it is large at both cutoffs.**

## ⛔⛭ RUN 4 — the alternation resolves in favour of the reading, and a position figure does not

**The statistic works.** *On the arm whose answer is known the second gap CONTRACTS, as the sky's does.*

| `LSTEP=2`, fluid path | peaks | $\ell_1$ | gaps | ${\rm gap}_{23}/{\rm gap}_{12}$ |
|---|---|---|---|---|
| **control** | 220/530/812/1122 | 220 | 310/282/310 | **0.9097** |
| CR `phi0 flat` *(default)* | 206/518/828/1188 | 206 | 312/310/360 | 0.9936 |
| CR `phi0 entry` | 208/524/826/1178 | 208 | 316/302/352 | 0.9557 |
| CR `phi196 entry` | 218/482/744/1054 | 218 | 264/262/310 | 0.9924 |
| — sky — | 220.6/538.1/809.8 | 220.6 | 317.5/271.7 | **0.8557** |

⇒ ***So the caveat r4138 raised is discharged in the reading's favour: the uniform comb is REAL at four
times the resolution, not an artefact of the grid.*** *And the r4138 anti-correlation survives it — the
reading that lands the first peak nearest the sky (`phi196 entry`, $\ell_1=218$) is the one with
essentially NO contraction, $0.9924$.*

⛔ ***BUT THE ARM'S FIRST PEAK MOVES AND THE CONTROL'S DOES NOT.*** *`LSTEP` $8\to2$: the control holds
at $220$ on both paths; this arm goes $204 \to 206$.* **So it is not a common grid effect that cancels
in the comparison — it is specific to the arm.** *Confirmed on the polarisation path, which is where the
papers report:*

| polarisation path, `LSTEP=2` | peaks | $\ell_1/\ell_A$ | $P_1/P_2$ | $P_1/P_3$ |
|---|---|---|---|---|
| control | **220 / 536 / 814 / 1128** | 0.7300 | 2.195 | 2.191 |
| this arm | **206 / 528 / 832 / 1196** | **0.6830** | 1.759 | 1.612 |
| control, driving OFF | 276 / 564 / 860 / 1164 | 0.9158 | 1.716 | 2.679 |
| this arm, driving OFF | 340 / 716 / 1108 | 1.1273 | 2.042 | 4.170 |

⇒ ***WHAT CHANGES IN THE PAPERS:*** *$\ell_1/\ell_A = 0.6764 \to \mathbf{0.6830}$ and the position
deficit $7.5\% \to \mathbf{6.6\%}$; the arm's peaks $204/524/828/1196 \to \mathbf{206/528/832/1196}$;
the control's $220/540/812 \to \mathbf{220/536/814}$ with $P_1/P_2 = 2.196 \to 2.195$ ($0.23\%$ from a
standard code's $2.200$).*

⛭ ***AND WHAT DOES NOT CHANGE IS THE READING.*** *The driving subtraction on the polarisation path gives
the control $-0.1858$ and this arm $-0.4443$ in $\ell_1/\ell_A$ — **$2.39\times$**, against the fluid
path's $2.43\times$, and $134$ multipoles against the control's $56$. **The arm is driven $2.4$ times as
hard as the control and overshoots**, on both paths and at both grids.* **Every height ratio is
unchanged to the printed digit.**

⏸ ***THE PAPER CORRECTION IS HELD FOR ONE MORE RUN, DELIBERATELY.*** *`LSTEP` $8\to2$ moved this
quantity. Correcting a figure BECAUSE of grid dependence and not measuring the next step down would
repeat the pattern the correction is for.* **`LSTEP=1` on the arm is running; if $206$ holds, the
position is converged in the reported grid and the papers are corrected once with a measured number
rather than twice with a provisional one.**



# ⛭⛭⛭ r4164 — **THE DRIVING SUBTRACTION, BOTH ARMS: THE ARM IS DRIVEN 2.4 TIMES AS HARD AS THE
CONTROL, AND IT OVERSHOOTS RATHER THAN FALLING SHORT**

***The retired diagnosis said this arm has NO driving — "the acoustic modes re-enter above the onset,
so none of them" is driven. It has more driving than the control.***

| fluid path, `KFAC=2.0` | driving OFF | driving ON | shift in $\ell_1/\ell_A$ | in multipoles |
|---|---|---|---|---|
| control | 276, $\ell_1/\ell_A = 0.9158$ | 220, **0.7300** | $-0.1858$ | $-56$ |
| **this arm** | 340, $\ell_1/\ell_A = 1.1273$ | 204, **0.6764** | $\mathbf{-0.4509}$ | $\mathbf{-136}$ |
| — sky — | | 0.7312 | | |

⇒ ***THE ARM'S DRIVING SHIFT IS $2.43\times$ THE CONTROL'S***, *by the same factor in $\ell_1/\ell_A$
and in multipoles.* ⛔ **So the retired account is refuted in the direction opposite to the one it
claimed: not an absent driving, but a driving more than twice the control's.**

⛭ ***AND THE SEPARATION IS ALREADY THERE BEFORE THE DRIVING ACTS.*** *Undriven, this arm's first peak
sits at $1.1273$ against the control's $0.9158$ — $23.1\%$ higher, a gap of $+0.2115$. The driving then
carries it to $-0.0536$ BELOW the control's driven position.* ⇒ ***The arm overshoots.*** *It crosses
from above the control's undriven position to below its driven one, and past the sky: the control lands
$0.0012$ from $0.7312$ and this arm $0.0548$ below it.* **The $7.5\%$ position deficit is an
OVERCORRECTION, not a shortfall — which is the opposite sign of cause from the retired text's.**

⌗ ***AND THE DRIVING MOVES THE TWO ARMS' FIRST HEIGHT RATIO IN OPPOSITE DIRECTIONS.***

| | $P_1/P_2$ | | $P_1/P_3$ | |
|---|---|---|---|---|
| control | $1.901 \to 2.393$ | $\mathbf{+25.9\%}$ | $3.219 \to 2.766$ | $-14.1\%$ |
| this arm | $2.468 \to 1.759^{*}$ | | $5.839 \to 2.206$ | $-62.2\%$ |
| this arm (fluid) | $2.468 \to 1.975$ | $\mathbf{-20.0\%}$ | $5.839 \to 2.206$ | $-62.2\%$ |

*(\* the polarisation-path figure, listed for orientation only; the subtraction itself is fluid-path and
the row below it is the like-for-like one.)* ⇒ ***The driving RAISES the control's first-to-second ratio
by $25.9\%$ and LOWERS this arm's by $20.0\%$.*** *A second, independent way the two arms' driving is not
the same operation — and it is not the polarisation source, which pulls both arms the same way.*

⚠ ***STATED AS A FLUID-PATH MEASUREMENT, AND BEING REPEATED ON THE OTHER PATH.*** *All four runs above
are `los_spectrum` at `KFAC=2.0`, so the two arms are compared on ONE path and the comparison is
internally sound. But it is not the path `sec:refit-bound` reports its figures on, and quoting across
the two is the defect corrected at r4162.* **The polarisation-path subtraction is queued; until it
returns, the $2.43\times$ is a fluid-path number and is written that way in the paper.**

⇒ **`P15 sec:refit-bound` carries the two-sentence reading 61 held for me, with the path named.**



# ⛭⛭⛭ r4138 — **RUN 2: THE DATUM'S SPAN CONTAINS THE SKY ON ALL FOUR STATISTICS, AND NO SINGLE
READING REPRODUCES MORE THAN TWO OF THEM — POSITION AND ALTERNATION ARE ANTI-CORRELATED**

***Twenty readings of the seam datum's two freedoms at the converged rung `KFAC=2.0`, on the leaf
congruence, default projection path: `CRPHI` over $[0,\pi)$ in eight steps plus `entry` and
`entryleaf`, each with `CRAMP` $\in$ \{`flat`, `entry`\}. Spectra saved so the FOURTH peak can be
measured, because the instrument prints only $P_1/P_2$ and $P_1/P_3$ and the spec's admissibility
criterion is about the fourth.***

⚠ ***THE CRITERION WAS FIXED BEFORE THE NUMBERS, AS THE SPEC REQUIRES, AND IT REJECTS THREE.***
*"A reading enters the spacing statistic only if it returns four peaks with the fourth at least a
twentieth of the first."* — `phi2.7489_ampentry` returns **fewer than four peaks**; `phientryleaf`
returns $P_4/P_1 = 0.039$ and $0.049$, **below $1/20$ on both amplitude readings**. ⇒ **`entryleaf`
is excluded entirely by a criterion written before it was run.** *Seventeen admissible.*

## ⛭ THE FOUR STATISTICS, ACROSS THE SEVENTEEN

| statistic | span across the datum | sky | verdict |
|---|---|---|---|
| first peak $\ell_1$ | $148 \to 228$, **$1.541\times$** | 220.6 | **INSIDE** |
| spacing (fit to four peaks) | $276.0 \to 330.4$, $1.197\times$ | 294.6 | **INSIDE** |
| acoustic phase intercept $b/a$ | $-0.4044 \to -0.2161$ | $-0.2253$ | **INSIDE**, at the very edge |
| alternation $\mathrm{gap}_{23}/\mathrm{gap}_{12}$ | $0.475 \to 1.088$ | 0.856 | **INSIDE** |

⇒ ***`P15` `sec:coherence`'s CONCLUSION SURVIVES AND ITS NUMBER DOES NOT.*** *The paper says "across
the eighteen readings of the two freedoms together the first peak spans a factor of $2.26$", and its
own text gives that measurement's configuration away by naming "the peak near $172$" — the
stacking-clock family.* **At converged $k$ on the leaf congruence the span is $1.541\times$, and the
sky is still inside it, so "the first peak's position is not a statement of this construction" holds
with a different figure behind it.** *Across the fifteen NUMERIC-phase readings alone it is
$204 \to 228$, only $1.118\times$: most of the span is carried by the derived `entry` reading at 148.*

## ⛔⛭⛭ AND THE THING RUN 2 RETURNS THAT NOBODY ASKED FOR: THE TWO CANNOT BE HAD TOGETHER

***A span that contains the sky on each statistic SEPARATELY is a much weaker statement than a reading
that reproduces the sky. There is no such reading, and the reason is structural.***

| $\ell_1$ | alternation $\mathrm{gap}_{23}/\mathrm{gap}_{12}$ across the readings at that position |
|---|---|
| 148 | 0.475, 0.526 |
| 204 | 0.923, 0.946, 0.950, 1.000, 1.000, 1.000 |
| 212 | 0.971, 0.971, 1.057 |
| **220** | **1.000, 1.029, 1.057, 1.088** |
| **228** | **1.027, 1.051** |
| — sky — | 220.6 at **0.856** |

**Spearman $\rho = +0.782$, $p = 2.1\times10^{-4}$ over the seventeen.** *As the datum carries the
first peak UP toward the sky's position, the second gap goes from CONTRACTING to EXPANDING — away from
the sky's.* ⇒ ***Of the six readings that put the first peak within one grid step of $220.6$, NOT ONE
contracts. Every one expands.*** *And of the seven that do contract, every one sits at $\ell_1 \le 212$.*

*** => POSITION AND ALTERNATION ARE ANTI-CORRELATED ACROSS THE SEAM DATUM. THE DATUM CAN BUY EITHER
AND NOT BOTH. ***

⌗ ***This SHARPENS `P07` `sec:frontiers` rather than refuting it.*** *That section says the sky's
spacings alternate "and this comb does not: its first two gaps are equal to the resolution at which
they are read".* **At converged $k$ on the leaf that is exactly right where the position is right —
and wrong in general, because seven of the seventeen readings do alternate.** ⇒ *The uniform comb is
not a property of the construction; it is a property of the readings that land the first peak. The
statement that survives is the stronger one: **no reading buys the position without losing the
alternation.*** ⛔ *And `C61` has already removed the mechanism that section offers for it — on the
leaf rate the first peak's mode IS driven — so the correlation is measured and unexplained.*

⚠ ***ONE RESOLUTION CAVEAT, AND IT IS BEING MEASURED RATHER THAN ARGUED.*** *These gaps are read on an
$\ell$ grid with `LSTEP` $=8$, so a gap difference of $8$ is ONE BIN and cannot be told from zero. The
sky's contraction is $45.8$ in $\ell$, about six bins, so the FAILURE to contract at $\ell_1\simeq220$
is resolvable; the small contractions at $\ell_1=204\!-\!212$ (one to three bins) are not.* **RUN 4 is
re-running four readings at `LSTEP` $=2$ — the control, the coded default, the derived datum, and the
reading that lands the first peak on the sky — to settle it at a quarter of the bin.**

## ⌗ THE READINGS IN FULL

| reading | peaks | $\ell_1/\ell_A$ | $P_1/P_2$ | $P_1/P_3$ | $P_4/P_1$ | gap ratio | |
|---|---|---|---|---|---|---|---|
| `phi0.0` `flat` *(coded default)* | 204/516/828/1188 | 0.6764 | 1.975 | 2.206 | 0.235 | 1.000 | |
| `phi0.0` `entry` | 204/524/828/1180 | 0.6764 | 1.621 | 1.424 | 0.417 | 0.950 | |
| `phi0.3927` `flat` | 204/508/812/1172 | 0.6764 | 1.619 | 1.618 | 0.337 | 1.000 | |
| `phi0.3927` `entry` | 204/516/804/1148 | 0.6764 | 1.386 | 1.093 | 0.593 | 0.923 | |
| `phi0.7854` `flat` | 204/500/796/1156 | 0.6764 | 1.237 | 1.123 | 0.509 | 1.000 | |
| `phi0.7854` `entry` | 204/500/780/1124 | 0.6764 | 1.110 | 0.800 | 0.880 | 0.946 | |
| `phi1.1781` `flat` | 212/492/788/1148 | 0.7029 | 0.923 | 0.784 | 0.761 | 1.057 | |
| `phi1.1781` `entry` | 212/492/764/1100 | 0.7029 | 0.884 | 0.603 | 1.262 | 0.971 | |
| `phi1.5708` `flat` | 220/492/788/1140 | 0.7294 | 0.772 | 0.647 | 0.952 | 1.088 | |
| `phi1.5708` `entry` | 212/484/748/1076 | 0.7029 | 0.824 | 0.566 | 1.461 | 0.971 | |
| `phi1.9635` `flat` | 220/500/796/1148 | 0.7294 | 0.897 | 0.823 | 0.746 | 1.057 | |
| `phi1.9635` `entry` | 220/484/748/1052 | 0.7294 | 1.213 | 1.002 | 0.913 | 1.000 | |
| `phi2.3562` `flat` | 228/524/828/1180 | 0.7560 | 1.427 | 1.760 | 0.310 | 1.027 | |
| `phi2.3562` `entry` | 220/492/772/1052 | 0.7294 | 2.908 | 7.532 | 0.128 | 1.029 | |
| `phi2.7489` `flat` | 228/540/868/1220 | 0.7560 | 1.952 | 3.387 | 0.127 | 1.051 | |
| `phi2.7489` `entry` | 228/532/876 | 0.7560 | | | | | ⛔ **REJECTED**, fewer than four peaks |
| `phientry` `flat` | 148/604/844/1108 | 0.4907 | 1.155 | 1.406 | 0.159 | 0.526 | |
| `phientry` `entry` | 148/620/844/1076 | 0.4907 | 0.846 | 0.929 | 0.296 | 0.475 | |
| `phientryleaf` `flat` | 196/484/764/1268 | 0.6499 | 4.310 | 7.374 | **0.049** | 0.972 | ⛔ **REJECTED**, $P_4/P_1 < 1/20$ |
| `phientryleaf` `entry` | 196/476/724/1004 | 0.6499 | 4.121 | 5.929 | **0.039** | 0.886 | ⛔ **REJECTED**, $P_4/P_1 < 1/20$ |
| — **sky** — | 220.6/538.1/809.8 | **0.7312** | **2.217** | **2.277** | | **0.856** | |

⌗ *The retired `CRAMP=entry` row this file suspended — $204/508/804$, $P_1/P_2 = 1.935$,
$P_1/P_3 = 2.578$ — is now comparable like for like: at converged $k$ the same reading gives
$204/524/828$, $\mathbf{1.621}$, $\mathbf{1.424}$.* **The position's first peak reproduces; the second
and third do not; and both height ratios fall well below the retired figures.**



# ⛭⛭⛭ r4136 — **THE POLARISATION LEG: THE CONTROL MEETS THE SPEC'S CALIBRATOR AND THE CR ARM'S
NUMBER IS IN HAND. THE HEIGHT DEFICIT IS REAL AND IT IS LARGER THAN THE RETIRED FIGURES.**

***This is the number `PO-13` has owed since `r3899`: the CR arm at converged $k$, on the leaf
congruence the framework assigns the perturbations, on the projection path where the control
reproduces CAMB. All four runs converged; `KFAC` $2.0$ and $3.0$ agree to every printed digit.***

## ⛭ THE FOUR CORNERS, ONE INSTRUMENT, ONE SET OF EQUATIONS

| arm | path | peaks | $\ell_1/\ell_A$ | vs sky | $P_1/P_2$ | vs sky | $P_1/P_3$ | vs sky |
|---|---|---|---|---|---|---|---|---|
| control | `los_spectrum` | 220 / 532 / 812 / 1124 | 0.7300 | $-0.2\%$ | 2.393 | $+7.9\%$ | 2.766 | $+21.5\%$ |
| **control** | **`_project` (`HIER=1`)** | **220 / 540 / 812 / 1132** | **0.7300** | $\mathbf{-0.2\%}$ | **2.196** | $\mathbf{-0.9\%}$ | **2.191** | $\mathbf{-3.8\%}$ |
| CR | `los_spectrum` | 204 / 516 / 828 / 1188 | 0.6764 | $-7.5\%$ | 1.975 | $-10.9\%$ | 2.206 | $-3.1\%$ |
| ⛔ **CR** | **`_project` (`HIER=1`)** | **204 / 524 / 828 / 1196** | **0.6764** | $\mathbf{-7.5\%}$ | **1.759** | $\mathbf{-20.7\%}$ | **1.612** | $\mathbf{-29.2\%}$ |
| — sky — | | 220.6 / 538.1 / 809.8 | 0.7312 | | 2.217 $\pm3.4\%$ | | 2.277 $\pm3.2\%$ | |

⛭ ***THE SPEC'S CALIBRATOR IS MET.*** *`PO13_RUN_SPEC_FOR_CC54` requires "the control must return
$P_1/P_2 \approx 2.197$ and peaks near $220/540/812$".* **On the polarisation path the control returns
$P_1/P_2 = 2.196$ and peaks $220/540/812$** *— $0.18\%$ from CAMB's $2.200$ and $0.9\%$ from the sky,
inside the sky's own $1\sigma$. `C59` measured $2.1969$ at `LMAXL=900`, `NK=280`; this is
`LMAXL=1300` with `NK` derived from `KFAC`, and the two agree to the printed digit.* ⇒ ***The
instrument is calibrated in the configuration the CR number is taken in, which is the whole point of
running both arms.***

⛭ ***AND EVERY CORNER IS CONVERGED.*** *Between `KFAC` $2.0$ and $3.0$: the CR polarisation arm is
identical to every digit ($204/524/828/1196$, $0.6764$, $1.759$, $1.612$); the control moves
$0.00\%$ on $P_1/P_2$ and $0.046\%$ on $P_1/P_3$ with peaks unchanged.*

## ⛔⛭ THE RESULT, AND IT IS NOT THE ONE THE RETIRED TEXT REPORTS

*** On the configuration in which the control reproduces CAMB to $0.18\%$, the CR arm is $20.7\%$ and
$29.2\%$ low on the height ratios and $7.5\%$ low on the first peak's position. ***

⇒ ***THE HEIGHT DEFICIT IS REAL, IT IS NOT THE $k$-TRUNCATION, AND IT IS NOT THE PROJECTION PATH.***
*Those were `r3870`'s two instrument faults and both are removed here.* ⛔ **It is also considerably
LARGER than the $12.7\%$ / $13.2\%$ this file suspended at `r3899`** — *and larger than the fluid
path's $10.9\%$ / $3.1\%$. The suspension was right and the direction of the correction is against the
construction, not for it.*

⌗ ***THE POLARISATION SOURCE ACTS THE SAME WAY ON BOTH ARMS, AND THAT IS WHY THE COMPARISON FLIPS.***

| adding $g\Pi/4 + (3/4k^2)\dd^2_\eta[g\Pi]$ | $P_1/P_2$ | $P_1/P_3$ |
|---|---|---|
| control | $2.393 \to 2.196$ | $2.766 \to 2.191$ |
| | $-8.2\%$ | $-20.8\%$ |
| CR | $1.975 \to 1.759$ | $2.206 \to 1.612$ |
| | $-10.9\%$ | $-26.9\%$ |

⇒ *** It pulls both arms DOWN by comparable amounts. It lands the control ON the sky because the
control was ABOVE it, and it carries the CR arm further BELOW because the CR arm was already there. ***
*Nothing about the operation differs between the arms — which is what a shared instrument is for, and
what makes the residual attributable to the source rather than to the machinery.*

⌗ ***r3512's PREDICTION IS CONFIRMED AND DOES NOT DISCRIMINATE.*** *It predicted that a correctly
composed $\Pi$ "should arrive weighted to high $k$ and act as a shape: $P_1/P_3$ and $P_1/P_4$ should
fall further than $P_1/P_2$".* **They do — $-26.9\%$ against $-10.9\%$ on CR.** *But they do on the
CONTROL too, $-20.8\%$ against $-8.2\%$, where $\mathrm{Jac}\equiv1$ makes composition unable to be at
issue at all.* ⇒ ***So the prediction is a property of the polarisation source and not a test of the
composition*** *— which is consistent with `C60`, where the composition defect it was a test for turns
out not to exist.* ⛭ *And r3512's FAILURE test is not triggered: it said "if the position climbs
instead, the hierarchy is on the wrong clock and step 3 was skipped". The position does not climb. It
does not move at all — $0.6764$ on both paths, both rungs.*

⌗ ***ONE READING DECLINED FOR BEING AT THE GRID'S RESOLUTION.*** *The polarisation source moves the
SECOND and FOURTH peaks by $+8$ on both arms ($516\to524$, $1188\to1196$; $532\to540$, $1124\to1132$)
and the first and third not at all. **`LSTEP` is $8$, so $+8$ is exactly one grid point** — the
reported $\ell$ grid runs $100,108,116,\dots$ — so this is a one-bin shift read on a one-bin grid and
it is recorded rather than interpreted. A finer `LSTEP` would be needed to say whether the even peaks
really move and the odd ones really do not.*

## ⌗ WHAT THIS LEAVES

- **The deficit is now a single object with one number**: on the calibrated configuration, $-7.5\%$ in
  position and $-20.7\%$ / $-29.2\%$ in the two height ratios. ⛔ *It is not explained here.*
- ***And the account of WHY that the retired text gives is refuted separately*** *(r4124, `C61`): on
  the leaf rate the first peak's mode IS driven, so "the comb is undriven" cannot be the reason.*
  ⇒ ***So `PO-13` now has a measured deficit and NO mechanism for it, which is a worse position than
  the file recorded and an honest one.***
- **RUN 2** measures how much of the position is the seam datum's two freedoms rather than the
  construction — running now, twenty readings.
- **The driving subtraction** (`NODRIVE=1`, both arms) measures the driving's size directly, which is
  the next thing `C61`'s scope note names.



# ⛭⛭⛭ r4124 — **RUN 1: BOTH ARMS ARE CONVERGED IN $k$, AND THE DIAGNOSIS'S PREMISE IS FALSE ON THE
RATE THE FRAMEWORK ASSIGNS THE PERTURBATIONS**

***`PO13_RUN_SPEC_FOR_CC54`'s RUN 1, run as specified: `KFAC` $\in\{1.5,2.0,3.0\}$, both arms, `NK`
derived and not pinned, `STACKPERT` unset. The default (`los_spectrum`) path is complete; the
polarisation path, the `KCONT` check and the driving subtraction are in flight and are marked below.***

## ⛭ THE LADDER — default path, `LMAXL=1300`, `NK` derived

| `KFAC` | arm | modes | reach $k_{\max}D_M/\ell_{\max}$ | peaks | $\ell_1/\ell_A$ | $P_1/P_2$ | $P_1/P_3$ |
|---|---|---|---|---|---|---|---|
| 1.5 | lcdm | — | 1.50 | ⛔ **REFUSED** — k-TRUNCATED | | | |
| 1.5 | cr | — | 1.50 | ⛔ **REFUSED** — k-TRUNCATED | | | |
| **2.0** | lcdm | 1656 | 2.00 | 220 / 532 / 812 / 1124 | 0.7300 | **2.393** | **2.766** |
| **2.0** | cr | 943 | 2.00 | 204 / 516 / 828 / 1188 | **0.6764** | **1.975** | **2.206** |
| **3.0** | lcdm | 2484 | 3.00 | 220 / 532 / 812 / 1124 | 0.7300 | **2.392** | **2.765** |
| **3.0** | cr | 1416 | 3.00 | 204 / 516 / 828 / 1188 | **0.6764** | **1.975** | **2.205** |
| — sky — | | | | 220.6 / 538.1 / 809.8 | 0.7312 | 2.217 | 2.277 |

⌗ ***`KFAC=1.5` is not a missing row — it is the instrument refusing.*** *Its own guard fires at
reach $<1.9$: "⛔ k-TRUNCATED — the $C_\ell$ integral is not converged at this $k_{\max}$." **Data, not
an error**, and it is the r3870 guard doing exactly what it was added for.*

⛭ ***THE GATE THE SPEC SET, APPLIED.*** *"If the CR arm's reported quantities still move between $2.0$
and $3.0$ by more than the control's own movement, it is not converged and nothing below is measured."*

| | $\ell_1/\ell_A$ | $P_1/P_2$ | $P_1/P_3$ | peaks 1–4 |
|---|---|---|---|---|
| **control's own movement, 2.0 → 3.0** | $0.00\%$ | $0.042\%$ | $0.036\%$ | identical |
| **CR's movement, 2.0 → 3.0** | $0.00\%$ | $0.00\%$ | $0.045\%$ | identical |

⇒ ***BOTH ARMS ARE CONVERGED, and the CR arm moves by no more than the control does.*** *`KFAC=2.0` is
the converged rung and RUNs 2 and 3 are unblocked. The control validates independently at that rung:
$P_1/P_2 = 2.393$, $P_1/P_3=2.766$, peaks $220/532/812$ — `C59`'s separately measured
`los_spectrum` $k_{\max}=2400$ row is $2.3931$, $2.7676$, $220/532/812$.*

## ⛭ WHICH RETIRED FIGURES THE CONVERGED RUN REPRODUCES, AND WHICH IT DOES NOT

***The spec asks for this explicitly, so it is stated as a table and not as a summary.***

| retired figure, where it sits | converged run | verdict |
|---|---|---|
| control $2.3931$ / $2.7676$, peaks $220/532/812$ — `C59`'s `los_spectrum` $k_{\max}=2400$ row | $2.393$ / $2.766$, $220/532/812$ | ⛭ **REPRODUCED** |
| CR $\ell_1/\ell_A=\mathbf{0.6764}$ — the r3739 two-arm position pin, `NK=620`, leaf clock | $\mathbf{0.6764}$ | ⛭ **REPRODUCED to four digits** |
| CR peaks $204/516/828$ — same pin | $204/516/828$ | ⛭ **REPRODUCED exactly** |
| control $\ell_1/\ell_A=0.7300$, peaks $220/532/812$ — same pin | $0.7300$, $220/532/812$ | ⛭ **REPRODUCED** |
| CR $P_1/P_2=2.013$ — same pin, at the instrument's default $k_{\max}$ | **1.975** | ⛔ **NOT reproduced** — $1.9\%$ low |
| control $P_1/P_2=2.447$ — same pin, same default $k_{\max}$ | **2.393** | ⛔ **NOT reproduced** — $2.2\%$ low |
| CR fourth peak $1164$; control fourth peak $1116$ — same pin | **1188**; **1124** | ⛔ **NOT reproduced** |
| CR $204/508/804$, $P_1/P_2=1.935$, $P_1/P_3=2.578$ — the `CRAMP=entry` derived-datum row, `NK=220` | not comparable at this rung | ⚠ **DIFFERENT DATUM** — RUN 2 measures it |
| CR $204/508/804$, $2.238$ / $3.901$ — the `CRAMP=flat` coded row, `NK=220` | $204/516/828$, $1.975$ / $2.206$ | ⛔ **NOT reproduced** |

⇒ ***THE PATTERN IS CLEAN AND IT IS THE ONE r3899 SAID SHOULD BE CONFIRMED RATHER THAN ASSUMED.***
*r3899 wrote: "the positions are not affected by the same mechanism **on the control's evidence**, but
that should be confirmed rather than assumed."* **Confirmed on the CR arm's own evidence: the
$k$-truncation moves HEIGHTS and does not move the first three peak POSITIONS, on both arms.** *What it
does move is the FOURTH peak, on both arms — which is the peak nearest the truncation, and is the reason
the admissibility criterion RUN 2 fixes before its numbers is a criterion about the fourth peak.*

⌗ *The $508/804$ positions are **not** a truncation artefact and not a rate artefact: the r3739 pin at
`NK=620` on the same rate and the same default $k_{\max}$ already gives $516/828$. They come from runs
at `NK=220`, and this file already records at r3745 that "every CR run in this thread used `NK=90`" and
that the guard fires on $D_M$. **The remaining difference is mode count, in a quantity the sampling
guard is there to protect.***

## ⛔⛭⛭ AND THE ANSWER TO THE QUESTION THE SPEC CALLS THE MOST IMPORTANT ONE

***"If the diagnosis in the retired text — that the driving supplies the disagreement because a
geometrically fixed rate has no radiation-domination crossing — does not survive the leaf rate, that is
the most important thing the run can return."***

**It does not survive.**
`\rcpt{C61_the_undriven_premise_is_false_on_the_rate_the_framework_assigns_the_perturbations}`

*`P07` `sec:frontiers` states the premise, in the paragraph that opens "with the perturbations computed
on the leaf congruence the framework assigns them to":*

> *"the standard shift that carries it is universal only where every mode crosses the horizon while
> there is a plasma to be driven, and **on this rate the acoustic modes re-enter above the onset, so
> none of them does**."*

*and this file gives the same premise as the structural reason the arm cannot reach the sky: "modes
sub-horizon at the late onset $z_{\rm onset}\approx6797$, **never cross while there is a plasma** → the
undriven phase".*

⛭ ***THE CENSUS, ON BOTH RATES, FROM THE INSTRUMENT'S OWN BACKGROUND SPLINES.***

| | **leaf rate** (what `LEAFPERT` assigns the perturbations) | **stacking rate** (L1) |
|---|---|---|
| radiation in the rate | **YES** | no |
| equality | $z_{\rm eq}=\mathbf{3936}$, $\eta_{\rm eq}=236.4$ | ⛔ **NONE — there is no equality** |
| $aH/c$ at the onset | $0.01828$/Mpc | $0.01109$/Mpc |
| band entering AFTER the onset | $\ell < \mathbf{237.7}$ | $\ell < 144.2$ |
| of those, entering in radiation | $\mathbf{155.6 < \ell < 237.7}$ | ⛔ empty, necessarily |
| the reported first peak $\ell_1=204$ | $k/aH = \mathbf{0.858}$ — **SUPER-horizon at the onset**, enters at $z=\mathbf{5590}$ | $k/aH = 1.415$ — sub-horizon, already inside |

⇒ ***The onset ($z=6761$) PRECEDES the leaf's equality ($z=3936$), the first peak's mode is still
outside the horizon when the plasma starts, and it enters while radiation dominates.*** **It crosses
while there is a plasma to be driven, and so does every mode in $155.6<\ell<237.7$.**

⛭ ***AND THE OTHER RATE GIVES THE OPPOSITE ANSWER, WHICH IS THE POINT.*** *On the stacking rate the
sentence is not merely true but necessary: that background carries no radiation term, so it has no
equality and no mode can cross during radiation domination at any onset. **The diagnosis was stated on
the rate that carries the ruler and tested against a spectrum computed on the rate that carries the
content.***

⌗ ***AND THE REFUTATION WAS ALREADY IN THE RECORD AS A CAVEAT.*** *`r3733` measured that on the leaf the
$\ell=220$ mode sits at $k/k_{\rm hor}=0.92$ — outside the horizon at the onset. This run gets $0.926$.*
**That number is the premise's refutation and it was filed as a qualifier.**

⚠ ***WHAT THIS DOES NOT ESTABLISH, AND IT IS THE NEXT MEASUREMENT.*** *How large the driving those modes
receive actually is. **A premise refuted is not a mechanism measured.** The instrument's `NODRIVE=1`
guard runs the same equations with the driving removed, and the difference between the two runs is the
only honest answer; it is queued and is reported below when it lands.* ⛔ ***And the position deficit is
untouched by any of this: the converged arm reports $\ell_1/\ell_A=0.6764$ against the sky's $0.7312$
whichever way the premise falls.*** *What changes is the account of WHY, not the number.*

## ⛭ THE LADDER WAIVER, CHECKED — r4134, and it re-establishes `K1` at the assigned configuration

***The CR arm's projection samples at $2.3$ points per Bessel period against the guard's bar of $4.0$.
The guard does not fail it; it waives itself, and says why in the same breath:* "CR's ladder is DISCRETE
and physical, so this is not aliasing — but it is only not aliasing if the answer does not depend on it.
Run `KCONT=1` to check."** So the waiver is a conditional, and the conditional is measurable.**

| CR arm, converged | sampling | peaks | $\ell_1/\ell_A$ | $P_1/P_2$ | $P_1/P_3$ |
|---|---|---|---|---|---|
| `KFAC=2.0` discrete ladder | 2.3 / period | 204 / 516 / 828 / 1188 | 0.6764 | 1.975 | 2.206 |
| `KFAC=2.0` **`KCONT=1`** continuum | **4.0 / period** | 204 / 516 / 828 / 1188 | 0.6764 | 1.975 | 2.206 |
| `KFAC=3.0` discrete ladder | 2.3 / period | 204 / 516 / 828 / 1188 | 0.6764 | 1.975 | 2.205 |
| `KFAC=3.0` **`KCONT=1`** continuum | **4.0 / period** | 204 / 516 / 828 / 1188 | 0.6764 | 1.975 | 2.205 |

⇒ ***Identical to every printed digit, at both rungs.*** **The answer does not depend on the ladder
sampling, so the waiver holds — and it now holds by measurement at the configuration the framework
assigns, above the guard's own bar on the continuum side.**

⌗ ***AND THIS RE-ESTABLISHES A RECEIPT THAT HAD GONE ORPHANED.*** *`K1_the_ladder_waiver_is_checked_against_the_continuum` (`L-280`) ran exactly this
check and reached exactly this conclusion. **But it reads two BANKED spectra**, `c54.178_cr.npz` and
`c54.186_cr_KCONT.npz`, and those sit at a different perturbation configuration: their background is
identical to today's CR arm — $\ell_A = 301.6$, $D_M = 13004.6$, $r_s = 135.46$, the same numbers to the
digit — but their first peak is at $\mathbf{171.2}$ where this run gives $\mathbf{204}$.* ⇒ ***That
places them in the stacking-clock family and not the leaf:*** *r3739 measured the same background at
$172$ under `STACKPERT=1` and $204$ under `LEAFPERT`, and $204$ is what the live run returns.*

⇒ ** So `K1`'s VERDICT survives the rate correction and convergence in $k$, and `K1`'s NUMBERS do not. **
*The receipt currently carries zero `\rcpt{}` markers in any paper and is one of the five entries a full
appendix regeneration drops. **Its result is live and its data are not**, which makes it a candidate for
the `sec:refit-bound` rewrite: the finding can be re-banked against this run instead of retired with the
spectra it was measured on.*

## ⌗ STILL IN FLIGHT, AND NOT REPORTED UNTIL THEY LAND

- ⛭ **`KCONT=1` on the CR arm — DONE, at both rungs, and it is exact.** *See below.*
- **The polarisation (`HIER=1`) path, both arms, `KFAC` $2.0$ and $3.0$.** *Required because the spec's
  own calibrator, $P_1/P_2\approx2.197$, is that path's figure and not the default path's $2.393$ — see
  the r4122 section. **Opened by `C60`.***
- **`NODRIVE=1`, both arms, at the converged rung.** *The driving's size by the instrument's own
  subtraction.*
- **RUN 2**, the datum freedoms as a range: `CRPHI` over $[0,\pi)$ plus `entry` and `entryleaf`,
  `CRAMP` $\in$ {`flat`, `entry`}, twenty runs, spectra saved so the **fourth** peak's height can be
  measured against the admissibility criterion the spec fixes before the numbers.
- **RUN 3**, the likelihood, both arms, floor as a model-to-model distance.



# ⛭⛭⛭ r4122 — **THE DEFECT THAT GATED THE CR ARM IS NOT THERE, AND WAS NOT THERE WHEN IT WAS WRITTEN**

***`C59` closed `PO-24`'s control step and deferred the CR arm in one sentence: the clock operations are
no-ops on the control, "so r3512's `HIER` composition defect cannot touch this result — and stays LIVE
for the CR arm, **which is the first thing the next step must settle**." `THE_REGISTER`'s `PO-24` row,
`receipts/INDEX.md` and both receipt appendices carry that deferral. It is settled here, and it comes
out the other way.***

`\rcpt{C60_the_hier_composition_defect_names_two_flags_its_own_tree_never_had}` — three source facts
and one run.

⛔ ***THE REMEDY NAMES TWO FLAGS THAT ARE NOT IN THE TREE r3512 WAS WRITTEN AGAINST.*** *r3512's gate 3
is "give the hierarchy's gravitational source the stacking clock and its diffusion the leaf", i.e. teach
`HIER=1` about **`SRCSTACK`** and **`DIFFLEAF`** — and it says "without this, step 4 is void", step 4
being the CR run.* **Both occur ZERO times in `ACOUSTIC_two_arm.py` at `95559d53`, the commit r3512 IS.**
*Its forty-two `os.environ.get` flags are enumerated in the receipt and neither is among them.*

⌗ ***They were real, on a line that is not this one.*** *`6beeca84` carries `SRCSTACK` ×13 and
`DIFFLEAF` ×3, and `cb5ec460` — "full consistent `HIER` composition" — is r3512's gate 3 actually
**performed**, there. **`6beeca84` is not an ancestor of `95559d53`.*** *Two nodes held the same
instrument on two lines within four hours of each other; the flag inventory was compiled across both and
the defect was checked against one.*

⛔ ***AND THE ASYMMETRY IT COUNTED IS `sound_phase`, WHICH IS ON NEITHER SPECTRUM PATH.*** *"`evolve_hier`
and `_project` reference the clock operations **once**… the main path references **two**." The second
site on "the main path" is `sound_phase` — the leaf-clock phase accumulator — which is **called once in
the whole file, from inside `qscan()`**, the `QSCAN=1` diagnostic that computes no spectrum.*

| path | ODE right-hand sides carrying the clock | projection |
|---|---|---|
| `LOS` (default) | `evolve` — **1** | `los_spectrum` — **0** |
| `HIER` (polarisation) | `evolve` + `evolve_hier` — **1 + 1** | `_project` — **0** |

⇒ ***One and one.*** *Each segment of a two-segment integration applies the chain rule once, which is what
a change of independent variable requires; and neither projection applies it, which is also right — the
projection is the comoving ruler's, on the stacking clock, exactly as `sound_phase`'s own docstring says
when it warns against unifying the two horizons.* **This is true at HEAD and at `95559d53` alike**, so it
is not something a later repair fixed.

⛭ ***THE TWO RIGHT-HAND SIDES ARE THE SAME BYTES WHERE THE CLOCK ENTERS.*** *Not a count. Lines 576 and
959 are character-identical —* `return out.ravel() * (float(Jac_of(e)) if LEAFPERT else 1.0)` *— as are
the rate selections at 536 and 916, and every clock-or-source operation in `evolve` (`Jac_of`, `Hl_of`,
`Hc_of`, `Phi2_of`, `Gf_of`, the four density-fraction splines) is also in `evolve_hier`.* **And there is
no split assignment anywhere in the file for the hierarchy to be inconsistent with.**

⛭ ***AND IT MOVES.*** *Asserted by running it: on `ARM=cr`, where $\mathrm{Jac}$ runs $0.646 \to 0.959$
across $\eta = 200\!-\!800$, toggling `LEAFPERT` changes the state `evolve_hier` returns by $2.0$
relative. **The hierarchy is not ignoring the clock operation.*** *On the control the same toggle is
inert by construction rather than by measurement, since $\mathrm{Jac}\equiv1$ makes both branches of the
conditional the same number — which is why the control could never have caught a composition fault
either way. **That part of r3512 stands and is the reason this had to be checked at source.***

⇒ ***SO THE CR ARM IS NOT GATED ON A COMPOSITION FIX, AND THE POLARISATION PATH IS OPEN TO IT.*** *What
gates the CR arm is convergence in $k$, which is RUN 1 and is a different question. r3512's gate order 1,
2 and 4 — validate $\Pi$ on the control, the `PISRC` subtraction, the CR run — are untouched by this and
remain to be done.*

⚠ ***AND THIS MATTERS FOR THE SPEC, NOT ONLY FOR THE LEDGER.*** *`PO13_RUN_SPEC_FOR_CC54` sets the
calibrator as "the control must return $P_1/P_2 \approx 2.197$ and peaks near $220/540/812$", under a
command with no `HIER=1` in it.* **$2.197$ is the polarisation path's figure** *— the instrument says so
at its own line 64, "the converged value is 2.393 on that path and 2.197 on the polarisation path", and
`C59`'s 2×2 puts `los_spectrum` at converged $k_{\max}$ at $2.393$ and `_project` at $2.197$.* ⇒ ***So
RUN 1 as written could not reach its own calibrator, and the deferral this section discharges is why it
was written that way.*** *The ladder is therefore climbed on both paths.*

⌗ ***One thing found by needing it, reported and not repaired:*** *forty-one registered receipts call
`git show` on a named commit, and the `receipts` job in `.github/workflows/gates.yml` — the one that runs
every receipt — checks out **shallow**, while the fast `gates` job asks for `fetch-depth: 0`. `C60` exits
1 rather than passing when the commit it reads is absent, so it fails honestly there rather than
asserting over an empty string; the other forty-one have not been checked for that guard.* **Not repaired
from inside `C60`, which is one of the affected files: the verifier would be editing its own subject.**

⌗ *The receipt's appendix entries were **spliced** using the generator's own emit path rather than
produced by a full regeneration. `python3 corpus/make_all_appendices.py` on this tree gains `C60` and
**drops five** live entries from `appendix_receipts_P15.tex` — `BRANCHPT_transmission_character`,
`D1_the_diagnosis_is_the_driving_and_the_driving_is_the_rate`, `H1_the_low_multipole_deficit…`,
`K1_the_ladder_waiver_is_checked_against_the_continuum` and `P03_acceleration_is_slice_curvature`, three
of which `P15` still cites. That is a live generator-scoping defect, reported on PR #32 and not mine to
fix; regenerating to register one receipt would have broken three citations to fix a fourth.*


# ⛔⛭ r4107 — **AND P15 §`sec:refit-bound` IS STILL REPORTING THE SUSPENDED NUMBERS AS ITS LIVE STATE**

***The suspension above is honoured in this document and nowhere else.*** *P15's acoustic section — 539
lines, a third of the paper — reports the CR arm's figures as the construction's current position. Three
things are wrong with it and they compound:*

⛔ ***The numbers predate the rate correction.*** *Every P15 acoustic receipt is built at `r2376`–`r2512`.
`LEAFPERT` became the default at `r3409`, moving the perturbations onto the leaf congruence — which is what
the framework assigns them, and which **carries the radiation term**. So the section's figures were computed
on the assignment the framework does not make.*

⛔ ***The paper says this itself and then ignores it.*** *At `sec:refit-bound` it records that $0.570$ was
computed on the stacking rate, that the framework assigns the perturbations to the leaf, and that **on the
leaf the first peak's position is no longer in deficit** — spacing $312$ against the sky's $317.5$, and
$P_1/P_2$ moving to $2.01$ against $2.22$. **It then carries $0.5703$ as the live figure in six further
places**, including "the first peak still sits where §`sec:refit-bound` measures it, $23\%$ low."*

⛔ ***And the one post-correction figure has no receipt.*** *The leaf-rate numbers are cited to
`D1_the_diagnosis_is_the_driving_and_the_driving_is_the_rate`, which does not contain them — that receipt
carries the spacing, phase and coupling attribution, not a leaf-rate run.*

⇒ ***The consequence for the diagnosis is the part that matters.*** *PO-13's answer as the paper states it is
that the standard driving shift is universal because every mode crosses during radiation domination, and that
a geometrically fixed rate has no such crossing — so the two coupling channels that cancel in $\Lambda$CDM
instead add. **On the leaf rate radiation gravitates**, so that argument's premise is the pre-`r3409`
configuration. The single post-correction data point runs the other way. **Whether the diagnosis survives the
correction is not known and is not currently in hand.***

⇒ ***So P15's acoustic section is a narration of an arc whose numbers this document has suspended, and the
restructure it needs is not a de-narration but a re-statement to what is actually known.*** *What is known and
survives: the acoustic scale is an accommodation and it is spent; the first peak's position is fixed by the
initial datum, whose two freedoms move it by a factor of $2.26$, so it is not a statement of the construction;
the instrument, its guard and its control exist, and the control reproduces CAMB once the $k$-integral is
converged. **What is owed is the CR arm at converged $k$ on the leaf rate** — a long run, and the Code node's.*


# ⌗ r3853 — **A SPECULATION OF DARYL'S, AND THE ONE PIECE OF IT THAT IS ARITHMETIC**

***Recorded as speculation. Nothing rests on it and no receipt tests it.***

⇒ *That a **charge residual may be an inherited datum of the same class as $A_s$ and $n_s$**, and that
this may be why this item has been hard to land. And, at the same weight: that **the branch point may be
where $e$ is set**.*

⛭ ***What is checkable was checked.*** *`P03` has mass $R$-odd and charge $R$-even, so at the branch point
the odd term flips onto the conjugate branch while $Q^{2}/r^{2}$ **rides through unchanged** --- and that
term only dominates below $r_{\rm inner}=Q^{2}/2M$, which is where any obstruction can live.*

| reading of "a charge residual" | $Q$ | $r_{\rm inner}$ on the progenitor |
|---|---|---|
| **intensive** — a datum, order $e$ | $1\,e$ | $2.8\times10^{-99}$ m ⟶ ***$10^{-64}$ Planck lengths*** |
| **extensive** — per-baryon asymmetry $\times\,10^{80}$ | $10^{59}\,e$ | $2.8\times10^{19}$ m |

⇒ ***The two differ by 118 orders of magnitude, and which applies IS the question of whether a residual is
a datum or a sum.*** *On the datum reading the obstruction is an epsilon, as Daryl expected, and
`r3829`'s worry is conditional rather than standing.*

# ⛭⛭⛭ r3841 — **THE FLAT COMB IS EXPLAINED IN `P07`, AND HAS BEEN ALL ALONG**

***`r3725` measured that CR's peak phase is flat ($0.324,0.316,0.334$) where the sky's alternates
($0.269,0.217,0.317$), and four revisions were spent hunting the mechanism. `P07` `sec:frontiers` states
it.***

> *"That alternation is the compression--rarefaction asymmetry, and where it is fixed is the **driving
> history**: the standard shift that carries it is universal only where **every mode crosses the horizon
> while there is a plasma to be driven**, and on this rate the acoustic modes **re-enter above the
> onset**, so none of them does. The uniform comb follows from that ordering, and **the ordering is not
> adjustable** --- the nucleosynthesis plasma is the progenitor's, on the transit's cooling leg, complete
> before the branch point."*

⇒ ***And `r3733` measured the same fact from the other side without recognising it***: *on the leaf the
$\ell=220$ mode sits at $k/k_{\rm hor}=0.92$ --- **outside the horizon at the onset**. That is "the
acoustic modes re-enter above the onset", measured.*

⛭ ***So the alternation and the resolution of the Hubble tension are one fact***, *and it is a prediction
with its calibration attached: raising the onset past the re-entry redshifts restores the alternation and
saturates at the comparison's own value --- in two observables, since the same mechanism is read in the
accumulated sound phase at first turnover.*

⌗ ***`D1` states the verdict this document was hunting***: *"PO-13 is answered: NONE OF THE THREE LAYERS.
The offset is the geometric rate's own consequence." **The DIAGNOSIS is closed.** What remains is the
derivation --- the potential's own evolution on the EXPANDING leg, `P15` having derived it in closed form
on the collapse leg. `PO-13`'s register row is narrowed to that.*

⚠ ***AND THE LESSON.*** *Four revisions went to a mechanism the corpus already carried, because the hunt
ran inside the instrument and never returned to the frontier section that names the item.*


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

## ⛔ r3745 — `DRE` IS LOAD-BEARING, `LN` WAS UNDER-RESOLVED, AND RESOLVING IT MAKES THE DEFICIT **LARGER**

### ⌗ `DRE` — the other half of the driving, and it cannot be scanned

*`DRE=0` on the control destroys the comb outright: **two peaks, at 340 and 628**, where there should be
three. The $k^2\Psi$ in the Euler equations is load-bearing, not a knob.* ⇒ ***With `r3743`'s result that
`DRC`'s default is already its optimum, the driving is fully exonerated.***

### ⛔ `LN` — a hardcoded constant that had never been varied

*The free-streaming hierarchy truncates at $\ell_{\max}=LN-2=10$, and a mode is resolved only while
$k\eta$ stays below that. On the control at recombination:*

| peak | $\ell$ | $k\eta_{\rm rec}$ | vs truncation |
|---|---|---|---|
| $P_1$ | 220 | 4.5 | ⛭ resolved |
| $P_2$ | 538 | 10.9 | ⛔ **under-resolved** |
| $P_3$ | 810 | **16.4** | ⛔ **well above it** |

*A defect that grows with $\ell$ and does not move the comb — **exactly the shape of the residual**. So it
looked like the answer.*

| `LN` | $\ell_1$ | $\ell_3$ | $P_1/P_2$ | $P_1/P_3$ | |
|---|---|---|---|---|---|
| 12 (default) | 220 | 804 | 2.721 | 4.496 | *P2, P3 under-resolved* |
| ⛔ **r3870** | | | **does not reproduce** | **does not reproduce** | ***`LN`$\,=12$ and $25$ agree to $10^{-3}$*** |
| **25** | 220 | 772 | 2.901 | ⛔ **8.009** | *resolved past $P_3$* |
| **THE SKY** | 220.6 | 809.8 | **2.217** | **2.277** | |

⛔ ***Resolving the hierarchy makes $P_3$ WEAKER, not stronger. The truncation was UNDER-DAMPING the
high-$\ell$ modes and MASKING the deficit.***

⇒ ***So `LN` is eliminated — and the true deficit is a factor $3.5$, not the $2.0$ `r3739` measured
against an unconverged default.*** *Every height number in this thread was taken at `LN=12` and is
therefore optimistic. **That is an instrument finding in its own right, independent of the height
question: the high-$\ell$ output is not converged in the hierarchy depth, and the constant had no
override, so nobody had checked.***

⌗ *Exposed as `LN`, default `12`, verified a no-op.*

---

## ⌗ r3743 — `DRC` SCANNED ON THE CONTROL: THE DEFAULT IS ITS OPTIMUM, SO THE DRIVING IS NOT THE KNOB

| `DRC` | $\ell_1$ | $P_1/P_2$ | $P_1/P_3$ |
|---|---|---|---|
| 0.0 — driving off | 204 | 4.216 | 11.625 |
| ⛭ **1.0 — the default** | **220** | 2.721 | ⛭ **4.496** |
| ⚠ *every row above* | | *k-truncated* | *k-truncated — r3870* |
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
| ~~$\Lambda$CDM control, validated~~ | 220 | 524 | 804 | ~~2.721~~ | ~~$22.7\%$~~ | ~~4.496~~ | ~~$97.5\%$~~ |
| ⛭⛭ **$\Lambda$CDM control, CONVERGED — `r3870`** | **220** | **540** | **812** | **2.197** | ⛭ **$0.9\%$** | **2.192** | ⛭ **$3.7\%$** |
| CR, `CRAMP=flat` (coded) | 204 | 508 | 804 | 2.238 | $0.9\%$ | 3.901 | $71.3\%$ |
| ⛭ CR, `CRAMP=entry` (derived) | 204 | 508 | 804 | **1.935** | $12.7\%$ | **2.578** | $13.2\%$ |
| **THE SKY** | 220.6 | 538.1 | 809.8 | **2.217** | | **2.277** | |

⇒ ***The control gets the POSITIONS right — $\ell_1=220$ against $220.6$ — and the HEIGHTS wrong by
$23\%$ and $97.5\%$.*** *On $\Lambda$CDM, where the answer is known and the arm is validated against CAMB
for its transfer.* ⛔ ***A defect that shows there is not a CR defect.***

> ⛭⛭⛭ ***AND THE CONTROL'S HEIGHTS WERE NOT WRONG — `r3870`, running `PO-24`'s first step.***
> *Two instrument-configuration faults were compounding, and the larger one nobody had looked for.*
> · ⛔ ***The $k$-integral was truncated where it is not converged.*** *The $k$-grid was built from
>   `LMAXL`, the grid of multipoles to **print**, so choosing what to report chose where to stop
>   integrating. Reported $\ell$ grid held fixed, $k_{\max}$ alone moved:
>   $2.721\to2.446\to2.399\to2.393$.*
> · ⛭ ***`los_spectrum` omits the polarisation source*** *`_project` carries.*
> ⇒ ***Both fixed: $P_1/P_2=2.197$ against CAMB's $2.200$, peaks $220/540/812$ against
> $220.6/538.1/809.8$*** `\rcpt{C59_the_control_reproduces_camb_and_the_height_defect_was_k_truncation}`***.***
>
> ⚠ ***The CR rows are truncated by the same mechanism and are NOT re-measured, so the comparison
> below is withdrawn pending that run rather than reversed.***

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

⌗ ***ON $\rho_r/\rho_m$ AT THE ONSET — corrected r3793: `P15` ALREADY STATES THIS, and states it more
precisely than my note did.*** *I recorded it as a failed expectation of mine, that the onset would sit at
$\rho_r/\rho_m=2$ and does not. **The paper says the same thing and says what follows from it**: at the
fitted $\Omega_m$ with $H_0\simeq68$ the condition holds and $1+z_{\rm eq}=3399$ is exactly half the onset,
while ***"read at the directly measured $H_0$ instead, the same $z_{\rm onset}$ gives
$\rho_r/\rho_m=1.71$, so the datum is an order-unity band and not a determined number."*** *Both numbers
reproduce here exactly — $1.718$ at $H_0=73$ and $1.979$ at $H_0=68$.*

⇒ ***So this is not a discrepancy to chase. It is a stated property of the datum***, and `P07` says where a
derivation would have to come from instead: *"the filter argument binds the primordial amplitude and tilt
— $A_s$ and $n_s$ are of the frozen class — and **does not bind the composition**: $\rho_r/\rho_m$ is a
background ratio, not a mode … **a derivation of the composition must be sought on other grounds.**"*

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


# ⛭⛭⛭ r4540 — **63's CHECK, ANSWERED: THE EXPANDING LEG STARTS WITH THE PRIMORDIAL POTENTIAL — AND THE HANDOVER'S TWO HALVES ARE READ AT DIFFERENT POINTS OF THE COLLAPSE LEG**

***63 asked which potential the arm's transfer starts the expanding leg with, the transmitted one or
the primordial one, because the two readings decide whether the over-driving is a prediction or a
calculation fault. It is the PRIMORDIAL one, and the reason is sharper than either branch.***

## ⓵ WHAT THE INSTRUMENT DOES, read at source and then run

`ACOUSTIC_two_arm.py` does **not integrate the collapse leg**. It integrates the expanding leg only,
from `ETA_ON`, and the collapse leg enters entirely through the handover datum — three numbers per
mode: the photon amplitude $\hat\Theta$, the potential $\Phi_0$, and the phase $\phi$.

| the datum's half | what the code sets | is the collapse leg's transfer applied? |
|---|---|---|
| photon amplitude | `That = -_T(xe)/2`, $x_e = 1/\sqrt3$ | ⛭ **YES** |
| potential | `Ph0 = -np.ones(nk)` (`CRPSI=flat`, the default) | ⛔ **NO** |

⛔ ***AND `_T` IS LITERALLY THE SAME FUNCTION IN BOTH PLACES.*** *`sec:envelope` derives the collapse
leg's potential in closed form — $\Psi''+(4/\eta)\Psi'+(k^2/3)\Psi=0$, regular solution
$\Psi=\Psi_i\,T(x)$ — and `_T` is that solution, already coded in this file. **The code applies it to
the amplitude and not to the potential.*** 59 wrote exactly that at `r3729` when it added the
`CRPSI=envelope` branch: *"The amplitude was given the transfer function and the potential was not."*
⌗ **That branch had never been run. No receipt, computation or paper mentions `CRPSI`; this is its
first measurement.**

⇒ ***So 63's second reading is the one the instrument supports: the expanding-leg driving is
re-applied from an UNDECAYED potential, onto an amplitude that has already been decayed.***

## ⓶ AND THE CONSEQUENCE IS NOT WHAT EITHER BRANCH PREDICTED

*Fluid path, `KFAC=2.0`, the same driving subtraction as `r4164`. The first two rows are `r4164`'s and
the driving-ON cell of row two was re-run here and reproduces to four decimals.*

| | driving OFF | driving ON | shift in $\ell_1/\ell_A$ | $\times$ control |
|---|---|---|---|---|
| control | $0.9158$ | $0.7300$ | $-0.1858$ | $1.00$ |
| arm, $\Phi$ **primordial** (as coded) | $1.1273$ | $0.6764$ | $-0.4509$ | $2.43$ |
| arm, $\Phi$ **transmitted** (`CRPSI=envelope`) | $1.4987$ | $\mathbf{0.5438}$ | $\mathbf{-0.9549}$ | $\mathbf{5.14}$ |

⛔ ***Carrying the decay across does not halve the driving. It doubles it again*** — $2.43\times \to
5.14\times$ — *and the first peak moves from $0.6764$ to $0.5438$, **further** from the sky's $0.7312$,
not back toward the structural claim.*

## ⓷ ⚠ AND THE CAVEAT THAT STOPS THAT NUMBER TRAVELLING

*What sources the expanding leg is the DIFFERENCE $\hat\Theta-\Phi$, not either half alone, and the
three codings of it disagree qualitatively rather than in size:*

| $\ell$ | $\Phi$ (envelope) | $\delta_\gamma^{(0)}$, $\Phi$ primordial | $\delta_\gamma^{(0)}$, $\Phi$ transmitted |
|---|---|---|---|
| $220$ | $-0.920$ | $+2.066$ | $+1.746$ |
| $540$ | $-0.584$ | $+2.066$ | $+0.402$ |
| $810$ | $-0.247$ | $+2.066$ | $\mathbf{-0.945}$ |
| $1120$ | $+0.017$ | $+2.066$ | $-2.004$ |

⇒ ***The initial photon perturbation CHANGES SIGN across the band under the transmitted reading and is
constant under the coded one.*** *So the envelope run reshapes the envelope rather than rescaling it,
and the undriven cell returns $P_1/P_2 = 0.804$ — **the "first peak" lower than the second**, which
means the peak-finder is not identifying the same feature in the two rows.* ⛔ **The $5.14\times$ is the
subtraction as defined and is NOT yet a like-for-like comparison of driving. It should not be carried
into a paper as one.**

⌗ ***AND THE THIRD READING IS DEGENERATE, WHICH IS THE POINT.*** *Making the handover self-consistent
the other way — `CRAMP=onset CRPSI=envelope`, both halves evaluated at the same $x=k c_s\eta_{\rm ON}$
— gives $\hat\Theta-\Phi = T(x)/2$, so the source vanishes with the transfer: measured
$\ell_1/\ell_A=0.5703$ with $P_1/P_2 = \mathbf{427}$. **The comb above the first peak is gone.***

## ⇒ HOW PO-13's MECHANISM READS, ON THIS EVIDENCE

⛔ ***Neither branch of the dichotomy as posed.*** *It is not a clean two-dose prediction, because the
second dose is applied from a potential the first dose already spent. And it is not simply one decay
counted twice, because carrying the decay across makes the over-driving **larger**, not smaller.*

⇒ ***WHAT IS ACTUALLY WRONG IS THAT THE HANDOVER DATUM'S TWO HALVES ARE READ AT DIFFERENT POINTS OF
THE COLLAPSE LEG, and the instrument has never specified both at the same point.*** *All three
codings of $\hat\Theta-\Phi$ that exist are defensible readings of "one datum per mode" and they give
$2.43\times$, $5.14\times$ and a dead comb. **The factor of $2.4$ is a property of that choice and not
yet a property of the construction.***

⚠ **NOT CLAIMED.** *That the two-dose mechanism is wrong — it may well be right, and it is the only
account so far that gives the direction, the ordering with peak number and the overshoot together.
What is claimed is that the instrument cannot presently be used to weigh it, because the quantity the
weighing depends on is unspecified at the handover.*

⌗ **THE RUN THAT WOULD DECIDE IT** is not another spectrum: it is a statement, from `sec:envelope` or
from the branch-point join `C19` computes ($\Phi_{\rm exp}=\tfrac9{10}\Phi_{\rm coll}$, exactly), of
what $\hat\Theta$ and $\Phi$ BOTH are at the same locus. *`C19`'s $9/10$ is a relation between the two
legs' potentials and is the closest thing the corpus has to that statement; nothing in the instrument
uses it.*


# ⛭⛭⛭ r4546 — **THE 23% UNDRIVEN SPLIT IS NOT THE HANDOVER: THE OSCILLATOR IS IDENTICAL ON BOTH ARMS AND EVERY DATUM CHANGE MOVES THE ARM THE WRONG WAY**

***62 asked whether the handover asymmetry that gives three codings of the driving also sets where the
undriven peak lands — one defect for both halves of the row, or two objects. **It is two objects.***

## ⓵ ⛭⛭ THE OSCILLATOR IS EXCLUDED, MEASURED WITHOUT THE PEAK-FINDER

*`qscan` reports $Q = k\!\int\!c_s\,\mathrm{d}\eta/\pi$ at the first extremum of $\Theta_0$ — the
turnover in the mode's **own sound phase**, with no projection and no peak identification in it.*

| undriven, 8 modes $k = 0.012$–$0.160$ /Mpc | $Q$ |
|---|---|
| control | $0.9989$–$1.0009$ |
| this arm, coded handover | $0.9989$–$1.0001$ |

⇒ ***Both arms turn over at exactly one half-period, to a part in a thousand.*** **So the $23\%$ split
is not in the acoustic phase, not in the sound-horizon bookkeeping, and not in the initial data's
phase.** *This is the instrument's own calibration and it holds on both arms: whatever the split is,
the undriven oscillator is not it.*

⌗ **AND THE DRIVEN COLUMNS ARE THE ROW'S OTHER HALF, IN PHASE RATHER THAN IN POSITION.**

| driven | $Q$ span | ratio | slope |
|---|---|---|---|
| control | $0.7744$–$0.8641$ | $1.12\times$ | $k^{-0.05}$ |
| this arm, coded handover | $0.1539$–$0.6427$ | $\mathbf{4.18\times}$ | $\mathbf{k^{-0.69}}$ |

*The control's driving is nearly flat in $k$; this arm's runs as $k^{-0.69}$ across a factor of four.
**That is the deepening-with-peak-number, measured in the mode's own phase rather than read off peak
positions** — and it is coding-dependent in the way `r4540` established.*

## ⓶ ⛔ AND EVERY CHANGE TO THE HANDOVER MOVES THE ARM AWAY FROM THE CONTROL, NOT TOWARD IT

*Undriven, fluid path, `KFAC=2.0`. **Each row names the coding it is read on**, per 62's caution.*

| undriven cell | $\ell_A$ | $\ell_1/\ell_A$ | |
|---|---|---|---|
| control, as coded (`LZSTART=3e7`) | $301.6$ | $\mathbf{0.9158}$ | `r4164` |
| arm, coded handover (`CRAMP=flat CRPSI=flat CRPHI=0`) | $301.6$ | $\mathbf{1.1273}$ | `r4164` |
| arm, `CRAMP=onset` (amplitude $k$-dependent) | $301.6$ | $1.2069$ | here |
| arm, `CRPSI=envelope` (potential transmitted) | $301.6$ | $1.4987$ ⚠ | `r4540` |
| arm, `CRIC=branchpoint` (the control's datum) | $301.6$ | peaks $[532, 916]$ only ⚠ | here |
| arm, `CRIC=branchpoint ZSTART=3e7` (datum **and** start) | $172.8$ | $1.5506$ | here |

⇒ ***Three independent ways of changing the handover datum — its amplitude envelope, its potential,
and replacing it wholesale with the control's — move the arm's undriven position UP or scatter it.
None moves it toward $0.9158$.*** ⛔ **So the split does not follow the handover. 62's first outcome is
not supported and the second is: the row has two objects.**

⚠ *The two marked cells are the ones 62 warned about: `CRPSI=envelope` returns $P_1/P_2 = 0.804$ and
`CRIC=branchpoint` finds only two peaks, so in both the peak-finder is not identifying the same
feature. **They are reported as scatter and no weight is put on their values** — the argument rests on
`CRAMP=onset`, which keeps three clean peaks and still moves the wrong way.*

⌗ **THE LAST ROW IS NOT A DEFECT AND IS WORTH SAYING SO.** *With the arm's sound horizon integrated
from $a\to0$ the way the control's is, $\ell_A$ comes out $172.8$ rather than $301.6$ — a factor of
$1.75$. **That is correct, not broken: on this construction there is no plasma before the onset, so a
sound horizon from $a\to0$ is not a quantity the arm has.** It confirms that $R_S$ must be integrated
from the onset, which is what the instrument does.*

## ⇒ WHERE THE SPLIT ACTUALLY LIVES

*The oscillator is excluded by ⓵ and the datum by ⓶, and $\ell_1/\ell_A$ would be $1$ on both arms if
the projected peak sat at the source's turnover. It does not: the control lands $8.4\%$ **below** it
and this arm $12.7\%$ **above**.* ⇒ ***So the split is in the PROJECTION — the map from a mode's
turnover to a multipole — and specifically in what rides with $\Theta_0$ into the source: the
$\Psi$ term, the integrated term, and the Doppler term, which the two arms do not carry alike.***

⚠ **NOT CLAIMED**: *which of those three it is. That is one subtraction away — the source has separable
terms and the instrument already switches them individually (`PISRC`, `NOISW`, `DRC`/`DRE`) — and it is
the next run rather than a conclusion here.*

⌗ **AND IT IS A THIRD OBJECT, NAMED.** *PO-13 now carries: the mechanism half, whose weighing waits on
the locus statement (`r4519`); this split, which is in the projection; and the phase offset the
transfer exposed. **The first two are independent, which is what this revision establishes.***

---

# ⛭ r6760+cc66.2 — THE CLOCK ADJUDICATED, THE RULER PRICED, AND THE EQUALITY FOUND TO BE THE RESIDUAL

*Node 66 (code seat), on node 66 (chat seat)'s work order. **This section is the code seat's; the
papers, `ONTOLOGY_FOUNDATION_INDEX.md`, `THE_PLAN.md` and the ledgers are the chat seat's and are
not touched here.** Lead-ID band `L-6600`–`L-6649`, revisions suffixed `+cc66.N`, per the split
agreed in band `r6760`.*

## ⓵ ⚑ THE DAMPING-TO-COMB RATIO PICKS ONE CONFIGURATION OUT OF FOUR, AND IT IS THE ONE BOTH
## SEATS ARRIVED AT SEPARATELY

*$\theta_D/\theta_* = r_D/r_s$ — $D_M$ cancels exactly, which matters, because the arm's $D_M$ is
$13005$ Mpc against the control's $13865$ and a comparison of $\theta_D$ alone would be reporting
that instead of the damping.*

| handover locus | clock | $r_s$ | $r_D$ | $r_D/r_s$ | vs control |
|---|---|---|---|---|---|
| control ($\Lambda$CDM, one rate) | — | $144.52$ | $6.567$ | $0.04544$ | $1.0000$ |
| **onset** | **stacking** — *the corpus as it stands* | $135.46$ | $6.986$ | $0.05157$ | $1.135$ |
| onset | leaf | $105.36$ | $6.479$ | $0.06149$ | $1.353$ |
| crossing | stacking | $236.37$ | $7.005$ | $0.02963$ | $0.652$ |
| **crossing** | **leaf** | $139.74$ | $6.490$ | $0.04644$ | $\mathbf{1.022}$ |

⇒ ***The crossing on the leaf clock is 2.2% from the control; the other three are 13.5%, 35.3% and
34.8%.*** **And neither choice was made to fix this quantity** — the crossing was adopted because
that is where $aH$ diverges, the leaf clock because the chat seat ruled one object for $r_s$ and
$r_D$ both. *A 2.2% agreement from a quantity nobody consulted is evidence.*

⌗ **AND THE TWO CHOICES ARE NOT SEPARABLE.** *The crossing on the wrong clock is worse than the
onset on the wrong clock, and the leaf clock at the wrong locus is the worst row of the four.*
⇒ ***So this is one configuration, not two improvements landing together, and the corpus's current
pair is the second-best of four rather than the reasonable default it reads as.***

⚠ **NOT CLAIMED**: *that the spectrum agrees. The crossing arm is still rejected at $35.5$ per bin
against the control's $2.10$. Getting this ratio right is **necessary and not sufficient**.*
⌗ *`receipts/P15_CR_cosmology/P15_the_damping_to_comb_ratio_picks_the_crossing_and_the_leaf_clock_out_of_four.py`*

## ⓶ ⚑ WHAT THE LEAF CLOCK COSTS THE DESI RESULT: OUTCOME (a), WITH A PRICE

*The chat seat named three outcomes. **It is (a): the dissolution survives with a different
derivation.***

| ruler | $H_0$ | $\Omega_m$ fit | $z_{\rm onset}$ | $\rho_r/\rho_m$ there | $\chi^2/12$ dof |
|---|---|---|---|---|---|
| stacking | $63$–$80$, every value | $0.3066$ | $6764$ | $2.31$–$1.43$ | $\mathbf{1.00}$, spread $0.0000$ |
| leaf, **no** onset | $68.50$ | $0.293$ | — | — | $0.88$ |
| leaf, **no** onset | $73$ | $0.330$ | — | — | $\mathbf{10.70}$ ⛔ |
| leaf, onset retained | $70$ | $0.2968$ | $178785$ | $51.0$ | $0.88$ |
| leaf, onset retained | $73$ | $0.2975$ | $61157$ | $16.0$ | $0.88$ |
| leaf, onset retained | $80$ | $0.2989$ | $26860$ | $5.8$ | $0.88$ |

**⛭ ON THE STACKING RULER $H_0$ CANCELS ALGEBRAICALLY** — *the rate is radiation-free, so $H_0$
leaves $D_M$, $D_H$ and $r_d$ together and the BAO ratios cannot see it. The measured $\chi^2$
spread across $H_0=63$–$80$ is **exactly zero**.*
**⛔ ON THE LEAF RULER IT DOES NOT.** *It enters through $\omega_r/h^2$. The fit holds across
$70$–$80$ anyway, at $0.88$ per dof, **because the onset moves to keep $\theta_*$ fixed.***
⇒ ***That is a compensation, not a cancellation, and the two are not the same claim.***

**⌗ THE PRICE, AS A NUMBER.** *The corpus's onset is "where radiation stops mattering". On the
stacking ruler it is **one** redshift, $6764$, at every $H_0$. On the leaf ruler the **locus**
moves: $z_{\rm onset}$ runs $1.8\times10^5\to2.7\times10^4$ across $H_0=70$–$80$ and
$\rho_r/\rho_m$ with it, $51.0\to5.8$.* ⇒ ***A locus sitting at $\rho_r/\rho_m=51$ at one $H_0$ and
$5.8$ at another is not "where radiation stops mattering"; it is a fitted redshift, and the
flatness is bought with it.***

**⌗ AND A SECOND, INDEPENDENT DETERMINATION AGREES.** *$\theta_*$ on the onset-free leaf ruler hits
the observed $0.0104085$ at $H_0=68.55$; BAO on the same ruler prefers $68.50$. **Two different
datasets, 0.05 apart in $H_0$.***

⇒ ***AND THE TWO LEAF BRANCHES NEED TWO DIFFERENT SENTENCES*** — *the chat seat's correction to
my own wording, which gave them one:*

*· **leaf ruler, onset retained**: `sec:tensions` keeps its CONCLUSION and not its ARGUMENT. The fit
does hold across $H_0=70$–$80$, so $H_0$ is not FORCED by BAO; but it holds by the onset moving
rather than by $H_0$ cancelling, so "$H_0$ is ABSENT from it" no longer follows.*

*· **leaf ruler, no onset**: **`sec:tensions` keeps NEITHER.** This branch re-pins $H_0$ to $68.50$
and breaks at $73$ at $10.70$ per dof. There is no dissolution on it at all — BAO forces a low
$H_0$ exactly as $\Lambda$CDM's does, and the acoustic angle independently agrees.*

⚠ ***And the branch that produces the arm's best acoustic comb (⓵ of `r6760+cc66.7`) is the second
one — the branch on which the dissolution does not survive.*** *That is the trade, and it is the
chat seat's to price.*
⌗ *`receipts/P15_CR_cosmology/P15_the_desi_dissolution_survives_the_leaf_ruler_but_only_by_moving_the_onset.py`*

## ⓷ ⚑ THE EQUALITY IS THE RESIDUAL, AND THE ARM'S OWN $z_{\rm eq}$ IS 14% TOO EARLY

*`ORFAC` scales $\Omega_r$ and therefore the leaf equality, at the crossing handover, everything
else untouched. **$r_s$ and $D_M$ do not move at all across these rows** — $236.37$ and $13004.6$
in every one — because the stacking rate carries no radiation term, so what moves is the DRIVING
and nothing else.*

| $z_{\rm eq}$ | peaks | $P_1/P_2$ | $P_1/P_3$ | fitted $\ell_A$ | $\phi/\pi$ | $\chi^2$ /133 | 700–1000 /bin |
|---|---|---|---|---|---|---|---|
| $3936$ *(the arm's own)* | $216/522/788/1094$ | $2.250$ | $2.150$ | $286.0$ | $-0.2214$ | $4723.2$ | $85.9$ |
| $\mathbf{3447}$ *($\Lambda$CDM's)* | $\mathbf{220/536/816/1132}$ | $\mathbf{2.278}$ | $\mathbf{2.299}$ | $\mathbf{298.0}$ | $\mathbf{-0.2416}$ | $\mathbf{645.8}$ | $\mathbf{6.4}$ |
| $3000$ | $226/554/846/1174$ | $2.315$ | $2.474$ | $310.0$ | $-0.2516$ | $6256.2$ | $68.4$ |
| *sky* | $220.4/537.7/817.3/1123.9$ | $2.217$ | $2.277$ | $298.4$ | $-0.2405$ | — | — |
| *control* | $220/536/814/1128$ | $2.195$ | $2.191$ | $297.0$ | $-0.2379$ | $279.4$ | $2.6$ |

⇒ ***At $z_{\rm eq}=3447$ the crossing arm's four peaks land on the sky's four peaks, its fitted
comb is $298.0$ against the sky's $298.4$, and its acoustic phase is $-0.2416\pi$ against the sky's
$-0.2405\pi$ — the corpus's own headline number, recovered on an arm that spends no fitted
parameter on it.*** **$\chi^2$ falls $4723.2\to645.8$ and the 700–1000 band, which the crossing
handover did NOT fix, falls $85.9\to6.4$ per bin.**

⛔ **AND THAT IS A DIAGNOSIS, NOT A FIT.** *$z_{\rm eq}=3447$ is $\Lambda$CDM's value, not a
freedom this arm has: `ORFAC` $=1.1418$ means **14.2% more radiation than the arm's parameters
give**. What the row establishes is where the residual lives, and the answer is **the equality**.
The arm at $3447$ is still $4.86$ per bin against the control's $2.10$ — a factor $2.3$, where the
coded arm was a factor $56$.*

⚠ **AND THE SCAN IS NOT MONOTONE**, *which is the point: $3936\to3447\to3000$ gives $4723\to646\to
6256$. **The sky sits at a minimum inside the scanned range**, so this is a measurement of where
the arm's equality should be and not a direction to push it.*

### ⚑ AND THE SECOND ROUTE SETTLES IT: $P_1/P_3$ TRACKS $z_{\rm eq}$ ON BOTH, SO THE ROUTE IS IRRELEVANT

*`ORFAC` moves $z_{\rm eq}$ through the radiation at fixed matter — at fixed $T_{\rm CMB}$ that is a
$\Delta N_{\rm eff}$, and it is **not** how this arm's equality arises. $z_{\rm eq}=3936$ here IS
$\omega_m=0.1634$ ($H_0=73$ at $\Omega_m=0.3066$) against $\Lambda$CDM's $0.1431$. **`CROM` reaches
the same two points through $\Omega_m$ at fixed $h$.***

| $z_{\rm eq}$ | route | $\Omega_m$ | peaks | $P_1/P_2$ | $\mathbf{P_1/P_3}$ | $\chi^2$ /133 | 700–1000 /bin |
|---|---|---|---|---|---|---|---|
| $3936$ | — *(as coded)* | $0.3066$ | $216/522/788/1094$ | $2.250$ | $\mathbf{2.150}$ | $4723.2$ | $85.9$ |
| $3447$ | radiation (`ORFAC`) | $0.3066$ | $220/536/816/1132$ | $2.278$ | $\mathbf{2.299}$ | $645.8$ | $6.4$ |
| $3447$ | **matter** (`CROM`) | $0.2685$ | $218/530/804/1116$ | $2.269$ | $\mathbf{2.294}$ | $1309.9$ | $24.0$ |
| $3000$ | radiation (`ORFAC`) | $0.3066$ | $226/554/846/1174$ | $2.315$ | $\mathbf{2.474}$ | $6256.2$ | $68.4$ |
| $3000$ | **matter** (`CROM`) | $0.2337$ | $222/540/824/1140$ | $2.292$ | $\mathbf{2.460}$ | $1233.2$ | $8.3$ |

⇒ ***$P_1/P_3$ agrees between the two routes to $0.2\%$ at $z_{\rm eq}=3447$ and $0.6\%$ at $3000$,
across a $12\%$ change in $\Omega_m$ and therefore in $D_M$ and the whole projection.*** **So the
third-peak deficit is RADIATION DRIVING and the route by which the equality is reached is
irrelevant to it** — which is the first of the two outcomes the chat seat named for this scan.

⛔ **BUT THE POSITIONS AND THE BAND $\chi^2$ DO NOT AGREE BETWEEN THE ROUTES, AND THAT IS THE
CONFOUND BEING VISIBLE RATHER THAN A CONTRADICTION.** *$\Omega_m$ cannot move without
$\Omega_\Lambda=1-\Omega_m$ and therefore $D_M$ moving: the matter route's comb slides the other
way, so at $3447$ its peaks sit $218/530/804$ against the radiation route's $220/536/816$, and the
$700$–$1000$ band's minimum lands at a **different** $z_{\rm eq}$ on the two routes ($6.4$ per bin
at $3447$ on radiation, $8.3$ at $3000$ on matter).* ⇒ ***The band is sensitive to the projection
as well as to the equality, so it is $P_1/P_3$ — a ratio at fixed $\ell$, blind to $D_M$ — that
carries the verdict, and it is unambiguous.***

⚠ **NOT CLAIMED**: *that either $\Omega_m$ is admissible. $0.2685$ and $0.2337$ are diagnostic
settings, and the arm's $\Omega_m$ is fixed at $0.3066$ by the DESI fit in ⓶.*

## ⓸ ⛔ THE BBN TABLE IS SILENT ON THIS ARM'S EQUALITY — NEITHER A COST NOR SUPPORT

**This is the chat seat's amendment and it is stated in its own words because it is right.**

*`computations/p16_bbn/bbn_network.py` reproduces: $Y_p=0.2432$, D/H $=2.567\times10^{-5}$,
$^3$He/H $=1.044\times10^{-5}$, $^7$Li/H $=4.461\times10^{-10}$.* **Its free inputs are
$\eta_{10}$ and a temperature range.** *The background is $H=\sqrt{8\pi G\rho_{\rm rad}(T)/3}$ with
$g_*(T)$ hardcoding three neutrino species. **$\omega_m$ does not appear in it. $z_{\rm eq}$ does
not appear in it. $\Omega_\Lambda$ does not appear in it.***

⇒ ***So the route by which this arm's equality actually differs — $\omega_m$, the matter density —
is INVISIBLE to the network. Every abundance is bit-identical across it.***

**⌗ AND THE PRICED ROUTE IS THE OTHER ONE.** *Reaching $z_{\rm eq}=3447$ and $3000$ through the
radiation instead is a $\Delta N_{\rm eff}$, and that the network does see: $Y_p$ goes
$0.2432\to0.2577\to0.2726$ and D/H $\to2.269\to2.002\times10^{-5}$.* ⚠ ***Those numbers price a
route this arm does not take.***

⇒ ***The abundances are SILENT on the arm's equality — neither a cost nor support — and the table
must be read that way. A `sec:tensions` rewritten around $\rho_r/\rho_m\sim17$ may not cite the
abundances either for it or against it.***

⌗ **THE STRUCTURAL FINDING GETS ITS OWN RECEIPT**, *per the amendment, because "the network cannot
see this parameter" is a claim about the network and belongs in a file that would fail if it
became untrue.*

## ⓹ ⛔ THE PIN AND THE CROSSING CANNOT BOTH BE HAD, AND THE PIN'S EFFECT IS THE START

*Run 1 as specified — crossing handover, `LEAFSCALES=1`, the onset retained and pinned on the leaf
ruler at $H_0=73$ — solves $z_{\rm onset}=61{,}580$.*

| configuration | $\ell_A$ rep | peaks | $\ell_1/\ell_A$ | $P_1/P_2$ | $P_1/P_3$ | $\chi^2$ /133 |
|---|---|---|---|---|---|---|
| run 1 (`LEAFSCALES=1`, $z_{\rm on}=61580$) | $301.6$ | $214/520/784/1092$ | $0.7095$ | $2.603$ | $2.539$ | $7157.8$ |
| **same start, STACKING clock** | $200.8$ | $\mathbf{214/520/784/1092}$ | $1.0659$ | $2.612$ | $2.561$ | $7427.8$ |

⇒ ***The peaks are identical to the multipole and the ratios move under 1%. `LEAFSCALES` is
bookkeeping in the transfer and nothing else — it relabels $\ell_A$ and moves no photon.*** *So
run 1's spectrum is entirely a START effect: the plasma begins at $z=61{,}580$.*

**⛔ AND THAT START IS AN ORDER OF MAGNITUDE BELOW WHERE THE CROSSING CONVERGED.** *The crossing
arm's `ZSTART` scan converged over $3\times10^6$–$3\times10^8$. $61{,}580$ is not in it.* ⇒ ***The
pin fixes the comb — the $\ell_1$ deficit goes 6.6% → 3.0% — and overshoots the heights by +17.4%
and +11.5%, because at $z=61{,}580$ the first-peak mode has already entered the horizon and the
handover datum is being applied mid-oscillation. The pin and the crossing are two different
handovers and the arm cannot have both.***

⚠ *This is the configuration the chat seat asked the P15 numbers to be landed from. **It is
reported as measured rather than as asked for**, and the choice between the pin and the crossing is
the chat seat's, since the papers are.*

### ⛭ AND THE INCOMPATIBILITY IS AN **ORDERING CONSTRAINT**, NOT A NUMERICAL COINCIDENCE

**This is node 66 (chat)'s framing and it is recorded here because it outlives the exchange that
produced it.**

*The two numbers above — $z_{\rm onset}=61{,}580$ from the pin, $z\gtrsim3\times10^6$ from the
crossing's own convergence — do not fail to agree by accident, and no refinement of either will
bring them together.* ⇒ ***The handover cannot precede the onset. "Pinned" puts the handover AT a
solved redshift; "at the crossing" puts it at the branch point, which is before every onset there
is. The two name DISJOINT configurations, and a configuration cannot be in both.***

⚠ ***So any later run that reports a pin and a crossing together is INTERMEDIATE and must be read
as one.*** *It is not a third branch and it is not a compromise between two; it is a run whose
handover locus has not been decided. Run 1 is exactly such a run, which is why its spectrum turns
out to be the START's and not the clock's — the start is the only handover statement in it.*

## ⓺ ⌗ THE BRACKET FAMILY, SWEPT

*27 live acoustic-onset `brentq` solvers in the tree and 46 retired; **18 of the live ones carry a
ceiling below the leaf ruler's root of $61{,}583$**. All 18 integrate $r_s$ on the stacking clock,
where the root is $6{,}761$, so they are **latent and not broken** — recorded rather than
pre-emptively widened, because churn in files whose numbers the papers quote is worse than churn.*
**Six files were widened: the instrument, three in `hubble_build/`, and two receipt mirrors that
had drifted from the `hubble_build/` scripts they declare as their ORIGIN.**
⌗ *`receipts/P15_CR_cosmology/P15_the_onset_bracket_family_is_latent_everywhere_and_was_live_in_one_place.py`*


---

# ⚑⚑ r6760+cc66.7 — AT ITS OWN RULER'S $H_0$ THE CROSSING ARM PREDICTS THE COMB, AND THE
# 700–1000 BAND FINALLY GOES

*Node 66 (code seat), at node 66 (chat seat)'s work order: "the crossing arm, no pin, at
$H_0=68.6$ — on that branch the comb should land on the sky's 298.4 as an OUTPUT, not a fit."*
**It lands.**

## ⓵ THE CONFIGURATION, AND THE THREE CHOICES WERE MADE SEPARATELY

*Handover at the **crossing** (⓵ of `r6760+cc66.1`: where $aH$ diverges and every mode is
super-horizon). **One clock, the leaf clock** (the chat seat's adjudication, $r_s$ and $r_D$
together). $(H_0,\Omega_m)=(68.60,\,0.2973)$ — **what the leaf ruler's own DESI DR2 fit returns**,
with $\theta_*$ alone returning $68.55$ independently (⓶ of `r6760+cc66.2`).*
⇒ ***Three choices, three places, three unrelated reasons. That they land together is the result.***

## ⓶ THE NUMBERS, POLARISATION PATH

| configuration | $\ell_A$ rep | peaks | **fitted comb** | $\phi/\pi$ | $P_1/P_2$ | $P_1/P_3$ | $g_2/g_1$ | $g_3/g_2$ | $\chi^2$/bin |
|---|---|---|---|---|---|---|---|---|---|
| control $\Lambda$CDM | $301.4$ | $220/536/814/1128$ | $297.0$ | $-0.2379$ | $2.195$ | $2.191$ | $0.8797$ | $1.1295$ | $\mathbf{2.10}$ |
| the arm as coded, $H_0=73$ | $301.6$ | $206/528/832/1196$ | $313.0$ | $-0.3323$ | $1.759$ | $1.612$ | $0.9441$ | $1.1974$ | $118.44$ |
| crossing, $H_0=73$ | $172.8$ | $216/522/788/1094$ | $286.0$ | $-0.2214$ | $2.250$ | $2.150$ | $0.8693$ | $1.1504$ | $35.51$ |
| **crossing, $H_0=68.6$** | $\mathbf{302.9}$ | $\mathbf{222/538/818/1134}$ | $\mathbf{298.0}$ | $\mathbf{-0.2349}$ | $\mathbf{2.264}$ | $\mathbf{2.298}$ | $\mathbf{0.8861}$ | $\mathbf{1.1286}$ | $\mathbf{4.19}$ |
| run 1, the pin | $301.6$ | $214/520/784/1092$ | $285.0$ | $-0.2246$ | $2.603$ | $2.539$ | $0.8627$ | $1.1667$ | $53.82$ |
| **the sky** | $301.7$ | $220.4/537.7/817.3/1123.9$ | $\mathbf{298.4}$ | $\mathbf{-0.2405}$ | $\mathbf{2.217}$ | $\mathbf{2.277}$ | $\mathbf{0.8812}$ | $\mathbf{1.0966}$ | — |

⇒ ***Comb $0.15\%$. $P_1/P_2$ $+2.1\%$. $P_1/P_3$ $+0.9\%$. $g_2/g_1$ $+0.6\%$, $g_3/g_2$
$+2.9\%$.***

**⌗ AND THE RULER AND THE SPECTRUM NOW AGREE.** *Reported $\ell_A = 302.9$ against a fitted comb of
$298.0$ — $1.6\%$. **At $H_0=73$ the same two were $172.8$ and $286.0$**, so this is not bookkeeping
agreeing with itself.*

## ⓷ THE BANDS, AND THE ONE THAT SURVIVED EVERYTHING

| | 100–400 | 400–700 | **700–1000** | 1000–1300 |
|---|---|---|---|---|
| control $\Lambda$CDM | $0.77$ | $1.44$ | $2.62$ | $3.73$ |
| the arm as coded | $144.82$ | $22.50$ | $77.89$ | $248.50$ |
| crossing, $H_0=73$ | $7.01$ | $8.11$ | $\mathbf{85.89}$ | $47.79$ |
| **crossing, $H_0=68.6$** | $\mathbf{1.70}$ | $\mathbf{2.22}$ | $\mathbf{4.23}$ | $\mathbf{9.29}$ |

⇒ ***Every band within a factor $2.5$ of the control.*** **The 700–1000 band — which the crossing
handover did not fix, which the equality scan reached only by putting in radiation the arm does not
have, and which the pin made worse — goes $85.89\to4.23$ per bin here, on a configuration that
fits nothing.**

## ⓸ WHAT IS NOT FITTED

*$z_{\rm onset}$: **not solved** — the handover is at the crossing, so `brentq` never runs and
`LATARG` is never reached. **The corpus calls $z_{\rm onset}$ "the one fitted number" and this
configuration does not spend it.** $\ell_A$: **not pinned** — reported as $\pi D_M/r_s$ and
independent of the comb. $A_s$: one amplitude in closed form, as for every row including the
control.*
⚠ ***$(H_0,\Omega_m)$ ARE fitted*** — *to DESI BAO and $\theta_*$, not to $TT$. So the cosmology is
not parameter-free; what is out-of-sample is the **spectrum** against the data that set it.*

## ⓹ ⛔ AND IT IS STILL REJECTED, WHICH IS THE RESULT AND NOT A CAVEAT ON IT

*$4.19$ per bin against the control's $2.10$ — **a factor $2.0$**. What changed is the size: the
coded arm is a factor $56$ and the same crossing arm at $H_0=73$ is a factor $17$.*

**⌗ THE PHASE IS NOW THE ONLY THING LEFT IN THE POSITIONS.** *$-0.2349\pi$ against the sky's
$-0.2405\pi$, $2.3\%$, where the comb is $0.15\%$. `sec:refit-bound`'s standing finding — the
spacing is right and the acoustic phase is the disagreement — **survives this configuration and is
sharpened by it**.*

**⌗ BOTH PATHS.** *The comb is $298.0$ on both. The heights are $2.264/2.298$ on the polarisation
path and $2.448/2.934$ on the fluid path — and the fluid path already overshot at $H_0=73$
($2.496/2.982$), so moving $H_0$ neither caused that nor can cure it.* ⇒ ***The comb result is
path-proof; the height result is polarisation-path specific and is reported as such.***

⚠ **AND THE CONFIGURATION IS THE 133-BIN UNLENSED ONE AT `LMAXL=1300`.** *The corpus's 185-bin
full-range lensed comparison needs $\ell\sim2000$ and is not run. A number scored on one may not be
quoted against the other.*

## ⇒ WHAT THIS IS, STATED FOR THE CHAT SEAT TO DECIDE ON

***On the chat seat's own criterion this is the first branch: a complete, pin-free configuration
that reproduces the sky's acoustic comb to $0.15\%$ and its heights to $\sim2\%$ with no fitted
number in the spectrum, and it predicts $H_0\approx68.6$.*** **That is a different Hubble statement
from the corpus's and has to be written as its own rather than as a repair of the existing one** —
*because the corpus's $H_0=73$ is exactly what it replaces, and at $73$ this same configuration is
rejected seventeen times harder.*
⌗ *`receipts/P15_CR_cosmology/P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_with_no_fitted_number.py`*


---

# ⛔ r6760+cc66.12 — THE FULL-RANGE LENSED COMPARISON IS THE UNFAVOURABLE ONE, AND IT IS THE ONE
# THE PAPER MUST QUOTE

*The configuration the corpus's own $\chi^2$ values are quoted on: `LMAXL=2000`, polarisation path,
the $(68.60,\,0.2973)$ arm and a control run at the same reach. **The range really is 185 bins**,
$\ell=100$–$1996$, asserted rather than taken on the name.*

| | bins | unlensed | /bin | lensed | /bin | $\Delta\chi^2$ |
|---|---|---|---|---|---|---|
| control $\Lambda$CDM | $185$ | $696.0$ | $3.76$ | $214.1$ | $\mathbf{1.16}$ | $-481.9$ |
| arm, crossing at $68.60$ | $185$ | $1169.8$ | $6.32$ | $550.5$ | $\mathbf{2.98}$ | $-619.3$ |

| comparison | arm/control |
|---|---|
| 133-bin, unlensed (⓹ of `r6760+cc66.7`) | $1.98\times$ |
| 185-bin full range, unlensed | $1.68\times$ |
| **185-bin full range, LENSED** | $\mathbf{2.57\times}$ |

⇒ ***$2.57\times$ is what `sec:SR-15` must quote.*** *A number scored on one configuration may not
be quoted against the other, and the corpus's own values are on the full-range lensed one.* **Both
are recorded so neither can be picked for being the kinder.**

**⌗ WHY IT MOVES, and it is the two residuals ⓹ already named, seen from the likelihood's side.**
*Lensing is worth proportionally more to the control — a factor $3.25$ against the arm's $2.13$ —
so the gap widens. **A smoothing operator helps a spectrum whose peaks are already in the right
place more than one whose fourth peak is $0.9\%$ out and whose acoustic phase is $2.3\%$ out.***

**⌗ AND AT `LMAXL=2000` THE ARM'S PEAKS AND HEIGHTS ARE UNCHANGED** — *$222/538/818/1134$,
$2.264$, $2.297$, identical to `LMAXL=1300`.* ⇒ ***The $k$-truncation was never touching the first
four peaks; the comb table of ⓶ stands.***

## ✔ AND THE CAVEAT RAISED IN ADVANCE IS WITHDRAWN RATHER THAN RELIED ON

*`r6760+cc66.9` flagged, before these numbers existed, that the control might carry $\sim700$ of
transfer inaccuracy — citing `P15_derived_lensing_on_the_lcdm_arm`'s $1320$ unlensed for the
`c54.178` control against CAMB's $615$.* **This control comes in at $696.0$ unlensed and $214.1$
lensed against CAMB's $615$ and $186$ — within $13\%$ and $15\%$, where `c54.178`'s was
$2.1\times$.**
⇒ ***So the ratio is a statement about the arm and not about the instrument, and the hedge is
withdrawn.*** *Recorded rather than deleted: a caveat raised before the measurement and dropped in
silence is indistinguishable from one that was never raised.*
⌗ *`receipts/P15_CR_cosmology/P15_the_full_range_lensed_comparison_is_the_unfavourable_one_and_the_control_is_nearly_camb.py`*


---

# ⚑ r6760+cc66.15 — THE ANOMALOUS DRIVING BELONGED TO THE PIN

*`sec:refit-bound`'s driving-subtraction paragraph carried the PINNED arm at $2.4\times$ the
control's shift. That configuration was retired at `r6760+cc66.7` — the pin and the crossing are
disjoint by ordering — so the paragraph pointed at a measurement the corpus did not have.*

| configuration | $\ell_A$ rep | $\ell_1$ driven | undriven | $\ell_1/\ell_A$ driven | undriven | $\Delta$ |
|---|---|---|---|---|---|---|
| control $\Lambda$CDM, POL | $301.4$ | $220$ | $274$ | $0.7300$ | $0.9092$ | $\mathbf{0.1792}$ |
| **CR arm $68.60$, POL** | $302.9$ | $222$ | $274$ | $0.7329$ | $0.9046$ | $\mathbf{0.1717}$ |
| **CR arm $68.60$, FLUID** | $302.9$ | $220$ | $272$ | $0.7263$ | $0.8980$ | $\mathbf{0.1717}$ |
| the PINNED arm | $301.6$ | $206$ | $340$ | $0.6830$ | $1.1273$ | $0.4443$ |

⇒ ***Adjudicated arm $0.96\times$ the control; pinned arm $2.48\times$.*** **The potential's grip on
the oscillator is within $4\%$ of the control's and slightly WEAKER rather than stronger.**

**⌗ PATH-PROOF.** *$0.1717$ on both paths, agreeing to $0.0000$ — **unlike the heights**, which have
had to be reported as polarisation-path specific throughout.*

**⌗ THE CONVENTION.** *$\ell_1/\ell_A$ on the **reported** $\ell_A$, not the fitted comb; on this arm
$302.9$ against $298.0$, giving $0.7329$ against $0.7450$ for the same run. The chat seat's control
figure reproduces on the first and not the second.*

⚠ **NOT CLAIMED**: *that a smaller driving shift makes the arm right. It removes a discrepancy
rather than adding a confirmation, and the $2.3\%$ phase residual is untouched.*
⌗ *`receipts/P15_CR_cosmology/P15_the_anomalous_driving_belonged_to_the_pin_and_not_to_the_construction.py`*

## ⛔ AND THE REFIT'S FIRST RESULT NEEDS NO RUN: $\tau$ IS NOT A FREE DIRECTION

*No reionisation is modelled, so on $\ell\ge100$ $e^{-2\tau}$ is a constant and only $A_se^{-2\tau}$
is seen. $\chi^2 = 1169.818285$ at $\tau = 0.000,\,0.030,\,0.054,\,0.090,\,0.150$ — identical to one
part in $10^6$.* ⇒ ***The six-parameter fit has at most FIVE directions, and the abstract's "five
free parameters" already counted one that cannot move the likelihood here.*** *It does not bias the
comparison, both arms losing it equally, but the count is wrong and any per-dof figure resting on it
is wrong with it.*


---

# ⚑⚑ r6788+cc66.18 — THE PARAMETER REFIT: THE BACKGROUND STAYS PUT, THE PHASE DOES NOT CLOSE

*132 bins, $\ell=100$–$1287$, per the chat seat's `r6788` ruling. Both arms refitted like-for-like
on the same bins in $H_0$, $\Omega_m$, $\omega_b$ and $n_s$, with the amplitude closed-form.*

| arm | $H_0$ | $\Omega_m$ | $\omega_b$ | $n_s$ | $\chi^2$ | /bin |
|---|---|---|---|---|---|---|
| control, start | $67.4000$ | $0.3150$ | $0.0224$ | $0.9650$ | $134.8$ | $1.02$ |
| control, refitted | $67.4054$ | $0.3095$ | $0.0220$ | $0.9559$ | $\mathbf{118.3}$ | $\mathbf{0.90}$ |
| **CR, start** | $68.6000$ | $0.2973$ | $0.0224$ | $0.9650$ | $299.0$ | $2.26$ |
| **CR, refitted** | $\mathbf{68.6077}$ | $\mathbf{0.2967}$ | $0.0217$ | $\mathbf{0.9949}$ | $\mathbf{171.1}$ | $\mathbf{1.30}$ |

⇒ ***$H_0$ moves by $0.011\%$ and $\Omega_m$ by $0.20\%$.*** **$(68.60,\,0.2973)$ came from DESI BAO
and $\theta_*$ with no spectrum involved; the spectrum, free to go anywhere, stays there.**

**⌗ AT A SHARP MINIMUM, NOT UNCONSTRAINED.** *One-step excursions cost $\Delta\chi^2$ of $1186$
($H_0$), $354$ ($\Omega_m$), $84$ ($\omega_b$), $23$ ($n_s$) — all four constrained on both arms.*

**⌗ AND THE MINIMUM IS VERIFIED.** *Predicted $118.2$ and $170.6$; real runs at the best-fit
parameters give $118.3$ and $171.1$ — $+0.1$ and $+0.5$.*

## ⛔ NEITHER RESIDUAL IS A BACKGROUND CHOICE

| | before | after | |
|---|---|---|---|
| acoustic phase, % out | $2.3$ | $\mathbf{4.5}$ | **worse** |
| fourth peak, % out | $0.9$ | $0.7$ | unchanged |

⇒ ***Freedom does not remove them — the phase gets worse, the fit trading it for likelihood
elsewhere. So both are properties of the CONSTRUCTION.*** *Ratio at the verified minimum
$\mathbf{1.45\times}$ against $2.22\times$ as-computed: freedom closes about a third of the gap and
leaves the rest.*

## ⚠ AND THE KNOB THIS RUN FOUND DEAD

*`NS`, exposed and "verified" at `cc66.14`, was **shadowed** — the literal $0.965$ exists three times
and the verification was run on the one path where the knob worked. **The flatness test caught it**
($\Delta\chi^2 = 0.00$ for $n_s$ on both arms); fixed at `cc66.17`; the CR arm's refitted $\chi^2$
moved $223.3\to170.6$ once the tilt was real.*
⌗ *`receipts/P15_CR_cosmology/P15_the_refit_leaves_the_background_where_the_distances_put_it_and_does_not_close_the_phase.py`*

---

# ⚑⚑ r6788+cc66.19 — `PO-24`: THE SIGNATURE COLLAPSES AT THE ADJUDICATED RATIO, AND THE ENDPOINT
# SETS ITS SIGN

*The joint amplitude-and-tilt fit against the arm's own $185$-bin spectrum at $(68.60,\,0.2973)$,
crossing handover, leaf clock. Window $\ell=100$–$1996$, pivot $\ell=1000$.*

| endpoint | $r=\theta_D/\theta_*$ | $r^2-1$ | $\ell_D$ | amplitude alone | + tilt | $\sigma$/bin | $\delta n_s$ | $\Delta\chi^2$ |
|---|---|---|---|---|---|---|---|---|
| to recombination | $1.02313$ | $+0.04679$ | $2133.5$ | $12.575$ ($0.0680$/bin) | $3.744$ ($0.0202$/bin) | $0.142$ | $-0.00926 \pm 0.00313$ | $8.83$ |
| to the visibility peak | $0.99179$ | $-0.01636$ | $2093.3$ | $1.698$ ($0.0092$/bin) | $0.514$ ($0.0028$/bin) | $0.053$ | $+0.00335 \pm 0.00307$ | $1.18$ |
| *`C62`, at $1.082$* | *$1.08200$* | *$+0.17072$* | *$2133.5$* | *$159.935$ ($0.864$/bin)* | *$46.18$ ($0.250$/bin)* | *$0.500$* | *$-0.03414$* | *$113.76$* |

⇒ ***A $13$-fold collapse to recombination and a $100$-fold one to the visibility peak, and it is the
configuration that moved rather than the fit.*** *An amplitude ALONE now absorbs the signature to
under a tenth of a $\chi^2$ per bin on either endpoint.*

⛔ ***AND THE SIGN IS THE ENDPOINT'S.*** *To recombination the arm damps MORE than the control and the
absorbing tilt is negative; to the visibility peak it damps LESS and the tilt is positive. The two
stopping points are $0.4\%$ apart in redshift.* **Which one the corpus reads $r_D$ to is the papers'
question; the chat seat settles it. Both reported, neither chosen.**

⌗ **THE TILT RUNS WITH ITS WINDOW BY A FACTOR $5.8$** *($-0.00751$ on $\ell=100$–$1300$ to $-0.04354$
on $1300$–$1996$), against $5.54$ from the ratio of their central $\ell$ squared — `C62`'s
$(\ell_{\max}/\ell_{\min})^2$ result confirmed as arithmetic. **So the displacement cannot be quoted
bare.***

⌗ **AND THE $r^2-1$ PRICING THE CHAT SEAT USED IS CORRECT**: *the tilt is linear in $r^2-1$ to better
than $2\%$ and the $\chi^2$ as its square to $8\%$, checked at one fixed $\ell_D$. The base
(CR spectrum against `plik_lite`'s own, $1.5\%$) and lensing ($5\%$) each move nothing.*

⌗ *`receipts/P15_CR_cosmology/P15_the_signature_collapses_at_the_adjudicated_ratio_and_the_endpoint_sets_its_sign.py`*

---

# ⚑ r6797+cc66.20 — THE ENDPOINT SETTLED: BOTH LENGTHS TO THE VISIBILITY PEAK

*The chat seat ruled at `r6797` that $r_s$ and $r_D$ both terminate at the visibility peak, and asked
for the common-endpoint number if it is not exactly $0.991$.*

| $r_s$ to | $r_D$ to | ratio vs control | | |
|---|---|---|---|---|
| recombination | recombination | $1.02313$ | $+2.31\%$ | **COMMON — the corpus's $+2.2\%$** |
| recombination | vis. peak | $0.98680$ | $-1.32\%$ | *mixed* |
| vis. peak | recombination | $1.02830$ | $+2.83\%$ | *mixed* |
| **vis. peak** | **vis. peak** | $\mathbf{0.99179}$ | $\mathbf{-0.82\%}$ | **COMMON — the ruled reading** |

⇒ **The ruled number is $0.99179$, $-0.82\%$, at the adjudicated background** *($0.99113$, $-0.89\%$,
at the $H_0=73.00$ one the ruling's $-0.9\%$ came from).*

⌗ **THE INSTRUMENT NEEDED NO SURGERY.** *`machinery()`'s $r_s(a_{\rm hi})$ and $r_D(a_{\rm hi})$ take
one upper limit, so every row already terminated both integrals at one epoch. **The ruled
configuration is the `PO-24` row labelled "to the visibility peak", unchanged:** amplitude alone
$1.698$ over $185$ bins ($0.0092$/bin), $+$tilt $0.514$ ($0.053\,\sigma$/bin),
$\delta n_s = +0.00335 \pm 0.00307$, $\Delta\chi^2 = 1.18$.*

⛔ **AND THE RULING'S ACCOUNT OF THE OLD NUMBER IS NOT WHAT THE CODE DID.** *`r6797` calls the
$+2.2\%$ a mixed reading — the sound horizon at the observed angle against a diffusion length to a
recombination cut. **The standalone integration took BOTH to recombination.** The mixed quantity the
sentence describes measures $1.02830$, $+2.83\%$.* ⇒ *The choice is between two COMMON epochs; the
ruling's own argument carries it without that support, and the paper's sentence should be corrected.*

⌗ *`receipts/P15_CR_cosmology/P15_the_signature_collapses_at_the_adjudicated_ratio_and_the_endpoint_sets_its_sign.py`, `PART 1b`*

---

# ⚑ r6801+cc66.22 — THE LOW-MULTIPOLE FLOOR ON THE ADJUDICATED BACKGROUND

*Order ② (a): the depth at $\ell=2$–$8$, both Boltzmann arms, one number for the disagreement.*

| $\ell$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| arm A (CAMB exact $\Delta_\ell$) | $0.4874$ | $0.4348$ | $0.3590$ | $0.6663$ | $0.9113$ | $0.9831$ | $0.9981$ |
| arm B (photon hierarchy) | $0.4905$ | $0.2511$ | $0.1779$ | $0.5998$ | $0.8959$ | $0.9813$ | $0.9967$ |
| A/B | $0.994$ | $1.731$ | $\mathbf{2.018}$ | $1.111$ | $1.017$ | $1.002$ | $1.001$ |

⇒ **The number is $2.02$ at $\ell=4$ and it WIDENED** *(control $1.84$)*. **The geometry does not
move**: $r_0 = 5064.75 \to 5051.49$ Mpc ($-0.26\%$), $\ell_2 = 7.74 \to 7.81$, so this is a depth
measurement and not a geometry one. *The shape still cross-validates — minimum at $\ell=4$, recovery
by $\ell=8$, on both arms and both backgrounds.*

⛔ **THE CAUSE IS THE LATE ISW.** *Not the geometry — $1\%$ in $r_0$ buys $3.5\%$ at $\ell=4$ against
a $102\%$ gap. Arm B's line-of-sight cut is `ETAEND` $=20\,a_{\rm rec}$, $z=53.5$; pushing it to
$z=15$ moves $\ell=3$ and $\ell=4$ **towards** arm A ($12\%$ of the way), which is the direction the
diagnosis predicts. **And the hierarchy goes non-finite past $z\simeq10$** under the defaults and
under `NS3=4000` and `NS3=12000, HKCAP=0.02` — not a step-size failure.*

⇒ ***So (b)'s condition — "if the two paths can be brought together" — is not met, and (b) is not
run.*** *What would earn it: carry the post-recombination source with the photon hierarchy
**decoupled**, since $\Phi'+\Psi'$ needs the metric and matter sector only. An instrument build, not
a knob, and not made unbidden.*

⌗ **TWO CHANGES MADE TO ASK THE QUESTION.** *`H0_L` exposed on the hierarchy's control branch
(default byte-identical; the literal $67.40$ in `Or_content` replaced by `H0`, which is the
correction away from the default). And both arms given ONE $r_0$ — the banked run's $2.75/D_M$ ladder
implied $5042$ Mpc against the formula's $5065$; re-run separately it reproduces the banked quartet
to $2\%$, so the $4.8\%$ that correction costs is measured.*

⌗ *`receipts/P15_CR_cosmology/P15_the_low_multipole_floor_moves_with_no_background_and_the_factor_two_is_the_late_isw.py`*

---

# ⚑⚑ r6825+cc66.25/.26 — THE 185-BIN REFIT, THE FLOOR CLOSED, AND TWO WITHDRAWALS

## ⛔ THE WITHDRAWALS, FIRST

1. **`cc66.22`: the blocker past $z\simeq10$ is NOT the $L_G=12$ truncation.** *It is the opacity
   grid: `_ea = linspace(eg[1], eta_end, 20000)` is a fixed point count over a growing range, so
   raising the cut coarsens $\tau'$ by $7.5\times$, the cubic spline overshoots negative, and
   $1/\tau'$ overflows in the tight-coupling viscosity. **With the resolution held fixed the
   undecoupled hierarchy runs to $a=1$ finite.** The three refinements I offered as evidence were
   `NS3` and `HKCAP` — neither touches the grid I was blaming.*
2. **`cc66.18`: the acoustic phase of $4.5\%$ is quantisation.** *Read with `argrelextrema` on the
   `LSTEP=8` grid, so peaks were quantised to $8$ in $\ell$. **The control returns the same
   $4.5\%$.** Refined (validated against `LSTEP=1` first: raw locator errs $3.1$ in $\ell$,
   refinement $0.13$): the arm is at $3.4\%$ on $185$ bins, $3.1\%$ on $132$, against the control's
   $1.6\%$.*

## ⓵ THE 185-BIN REFIT — VERIFIED

| arm | $H_0$ | $\Omega_m$ | $\omega_b$ | $n_s$ | $\chi^2$ predicted | measured | /bin |
|---|---|---|---|---|---|---|---|
| control | $67.4103$ | $0.3098$ | $0.02197$ | $0.9542$ | $185.1$ | $186.5$ | $1.01$ |
| CR, crossing | $68.5811$ | $0.2972$ | $0.02152$ | $0.9980$ | $292.5$ | $292.4$ | $1.58$ |

⇒ **$H_0$ moves $0.028\%$, $\Omega_m$ $0.031\%$** *(against $0.011\%$ and $0.20\%$ on $132$ bins —
$\Omega_m$ six times tighter, $H_0$ twice as loose, both inside a thirtieth of a per cent).*
**Ratio at the verified minimum $1.57\times$**, against $2.56\times$ as-computed. *Flatness
(control/CR): $1774$/$2527$, $473$/$740$, $98$/$141$, $32$/$31$ — all constrained, every one costing
more than on $132$ bins.*

## ⓶ THE LOW-MULTIPOLE FLOOR — THE GAP CLOSES

| $\ell$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| arm A (CAMB), adjudicated | $0.4874$ | $0.4348$ | $0.3590$ | $0.6663$ | $0.9113$ | $0.9831$ | $0.9981$ |
| arm B decoupled, adjudicated | $0.4774$ | $0.4300$ | $0.3485$ | $0.6587$ | $0.9091$ | $0.9820$ | $0.9975$ |
| A/B | $1.021$ | $1.011$ | $1.030$ | $1.012$ | $1.002$ | $1.001$ | $1.001$ |

⇒ ***$3\%$ where the corpus carries $2.02\times$.*** **And the factor of two was TWO defects
opposing**: a line-of-sight cut at $z=53.5$ (no late ISW, biasing down) and a continuum truncated at
$0.5\,k_2$ (biasing up). *Fixing the continuum alone widens the gap to $4.02\times$.*

**(b), now that its condition is met:** $\Delta(-2\ln L) = +1.58$ central ($+0.22$ to $+3.40$ across
the octopole estimators), against the landed $+1.80$. ***The verdict does not move — the sector is
settled as a wash rather than left as one.***

⌗ *`receipts/P15_CR_cosmology/P15_the_full_range_refit_holds_the_background_and_the_phase_residual_was_quantised.py`
and `.../P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py`*

---

# ⚑⚑ r6835+cc66.28 — THERE IS NO PHASE RESIDUAL, AND THE FOURTH PEAK IS NOT THE ENVELOPE

*One locator — bin to `plik_lite`'s bins, convert to $D_l$, spline, parabola over $\pm W$ — applied
identically to the sky and both arms' verified $185$-bin spectra, $W$ swept over seven values so the
locator's own spread is the uncertainty carried.*

| | peaks | $\varphi/\pi$(1–3) | $\varphi/\pi$(1–4) |
|---|---|---|---|
| sky | $221.0/533.8/814.8/1121.9$ | $-0.2378 \pm 0.0099$ | $-0.2448 \pm 0.0074$ |
| control | $220.2/537.0/811.7/1124.5$ | $-0.2318 \pm 0.0018$ | $-0.2464 \pm 0.0022$ |
| CR crossing | $221.8/536.8/812.9/1126.5$ | $-0.2278 \pm 0.0017$ | $-0.2445 \pm 0.0019$ |

⇒ **CR against the sky: $+1.0\sigma$ (1–3), $+0.0\sigma$ (1–4). CR against the control:
$+1.6\sigma$, $+0.6\sigma$.**

⚠ **AND THE MECHANISM IS THE SIGMA, NOT THE SIZE.** *Priced one mismatch at a time the offset goes
$3.4\% \to 3.8\% \to 5.3\% \to 4.2\%$ — **it does not shrink**. What dissolves it is that the sky's own
$\varphi/\pi$ cannot be pinned tighter than $\pm0.0099$. The number was never small; it was never
measured against anything.*

**② THE DAMPING ENVELOPE IS RULED OUT.** *Forcing the arm's damping to the control's
($\exp[(r^2-1)(\ell/\ell_D)^2]$, $r=0.99179$, $\ell_D=2094.2$, $-0.47\%$ at $\ell=1127$) moves the
fourth peak $-0.13$ against an offset of $+1.95$ — $7\%$. The inverse test on the control gives
$+0.14$, equal and opposite.*

**WHAT IS LEFT:** *offsets $+1.60/-0.24/+1.25/+1.95$; the arm's comb is $+0.085\%$ wider, predicting
$+0.19/+0.46/+0.69/+0.95$; leftovers $+1.41/-0.70/+0.56/+0.99$ — same sign and order, **not a clean
constant**.*

⛔ **③ NOT RUN** — *conditional on a uniform phase offset surviving ①, and none does.*

⌗ *`receipts/P15_CR_cosmology/P15_there_is_no_phase_residual_and_the_fourth_peak_is_not_the_damping_envelope.py`*

---

# ⚑⚑ r6841+cc66.29 — `PO-25`'S CRITERION IS TWO LENGTHS THE CORPUS ALREADY CARRIES

*`P16` `sec:interior`'s exact closed dust-plus-radiation ball, put through `P03` `sec:charge`'s
sharpened condition. The algebra is exact and is re-derived rather than quoted; the conclusion it
points at is not the one the row currently holds.*

**⌗ THE CRITERION, REDUCED.** *Along a comoving shell $Rm(R)\to B\sin^{4}\chi/2$, so $p=1$ and the
marginal coefficient is $2k=B\sin^{4}\chi$. `P16` determines $a_{\rm eq}=A\rho^{2}/4=B/A=1.49$ Mpc, and
$2M(\chi)=A\sin^{3}\chi$, so $B\sin^{4}\chi=2M(\chi)a_{\rm eq}\sin\chi$ and*

$$\text{the obstruction survives}\iff r_{\rm inner}=\frac{Q^{2}}{2M}>a_{\rm eq}\sin\chi .$$

| $M$ | $(Q/M)_{\rm crit}=\sqrt{2a_{\rm eq}/M}$ | reading | $r_{\rm inner}$ | $r_{\rm inner}/a_{\rm eq}$ | shortfall in $Q^{2}$ |
|---|---|---|---|---|---|
| $2.33\times10^{23}M_\odot$ | $1.63\times10^{-2}$ | extensive | $2.77\times10^{19}$ m | $6.0\times10^{-4}$ | $\mathbf{1.7\times10^{3}}$ |
| | | intensive | $2.77\times10^{-99}$ m | $6.0\times10^{-122}$ | $1.7\times10^{121}$ |
| $4.3\times10^{52}$ kg | $5.37\times10^{-2}$ | extensive | $2.99\times10^{20}$ m | $6.5\times10^{-3}$ | $1.5\times10^{2}$ |
| | | intensive | $2.99\times10^{-98}$ m | $6.5\times10^{-121}$ | $1.5\times10^{120}$ |

⇒ ***Destroyed on every mass-and-reading pair the corpus carries***, *so the verdict does not turn on
the datum fork. $a_{\rm eq}=4.598\times10^{22}$ m throughout; the $2.8\times10^{19}$ m and
$2.8\times10^{-99}$ m published at `r3827`/`r3853` are reproduced to $5\%$.*

**⌗ THE TWO LIMITS, WHICH ARE NOT THE SAME QUESTION.**

| limit | $m$ | $p$ | what it is |
|---|---|---|---|
| fixed time, $\chi\to0$ | $R^{3}(Aa+B)/2a^{4}$ | $-3$ | centre regularity, coefficient $\tfrac{4\pi}{3}\rho$ |
| fixed shell, $R\to0$ | $B\sin^{4}\chi/2R$ | $1$ | **the one the criterion needs** |

**⌗ THE CENTRAL DEGENERACY — $Q(\chi)^{2}/(B\sin^{4}\chi)=\tfrac{q_c^{2}}{9B}\chi^{2}+O(\chi^{4})$.**

| $Q_{\rm tot}^{2}/B$ | $\chi_*$ | unobstructed core, fraction of the dust |
|---|---|---|
| $2$ | $1.2913$ | $0.888$ |
| $10$ | $0.6967$ | $0.264$ |
| $100$ | $0.2339$ | $0.0125$ |
| $10^{4}$ | $0.02356$ | $1.31\times10^{-5}$ |
| $10^{8}$ | $2.36\times10^{-4}$ | $1.31\times10^{-11}$ |

*$\chi_*\propto Q_{\rm tot}^{-1/2}$ to four figures, which is the $\chi^{2}$ degeneracy and not a scale
in the problem.* ⇒ ***The obstruction is never total, for any charge.***

**⌗ THE TURNING POINTS — THREE REGIMES, $\beta=B\sin^{4}\chi-Q^{2}$ in
$\dot R^{2}=-\sin^{2}\chi+A\sin^{3}\chi/R+\beta/R^{2}$.**

| | roots | the shell |
|---|---|---|
| $\beta>0$ | one positive | reaches $R=0$ |
| $0<-\beta<A^{2}\sin^{4}\chi/4$ | two positive | bounces at finite $R$ — **the obstruction** |
| $-\beta>A^{2}\sin^{4}\chi/4$ | none | does not exist with that energy (over-extremality, $Q>M$ at the edge) |

⛔ **NOT ESTABLISHED:** *that a spacelike $r=0$ forms — the clause `r6405` left. The charged ball is not
exactly `P16`'s homogeneous interior (a radial field makes the stress anisotropic), so every statement
is **per-shell**; $\rho_r\propto R^{-4}$ at fixed shell is the top-hat's behaviour; and a supercritical
charge's differential bounce makes shell crossings the probe does not follow.*

⌗ *`receipts/P03_SdS_slicing/P03_the_interior_mass_function_is_p_equals_one_along_the_shell_and_the_charge_falls_short_of_the_equality_radius.py`*

---

# ⚑⚑ r6849+cc66.30 — `PO-43`'s CHECK: THE TWO HELICITY TOWERS ARE POPULATED ALIKE

*`P10` `sec:lock`'s fibre-by-fibre Hartle–Hawking condition, tested for helicity-blindness at the level
of the mode functions. The condition's whole dependence on the tower is
$\hat\Gamma=\gamma+c\sum_n\hat\pi_n^{2}$, with $\nu=\sqrt{\hat\Gamma+\tfrac14}$ and the regular branch
$x^{1/2+\nu}$ on $\hat\Gamma<\tfrac34$.*

**⌗ THE COMMUTATORS WITH THE HELICITY SWAP $P$** *(truncated Fock space, two levels × two helicities,
3 states per mode):*

| object | $\lVert[\,\cdot\,,P]\rVert_\infty$ |
|---|---|
| $\hat\Gamma$ | $1.78\times10^{-15}$ |
| $\nu(\hat\Gamma)$ | $4.44\times10^{-16}$ |
| $\Pi_{\hat\Gamma<3/4}$ | $1.67\times10^{-16}$ |
| *CONTROL: helicity-weighted $\hat\Gamma$* | *$3.633$* |

*And $\kappa=\tfrac12\lvert f'(\alpha)\rvert=1/\alpha$, $\beta=2\pi\alpha$, derived off
$f=1-r^{2}/\alpha^{2}$ — free symbols $\{\alpha\}$, **no mode index**.*

**⌗ THE TOWER'S BOOKKEEPING, AGAINST `P10`'s OWN DEGENERACY AND EIGENVALUE.**
*$(j_L,j_R)=\big(\tfrac{m+1}{2},\tfrac{m-3}{2}\big)$ and its swap, $m=n+1$; $\mu^{2}=2(C_L+C_R)-6$.*

| $n$ | $(j_L,j_R)$ | dim each | total | `P10`'s $2(n-1)(n+3)$ | $\mu_n^{2}$ | `P10`'s $n(n+2)-2$ |
|---|---|---|---|---|---|---|
| **2** | $(2,0)$ | $5$ | $10$ | $10$ | $6$ | $6$ |
| 3 | $(5/2,1/2)$ | $12$ | $24$ | $24$ | $13$ | $13$ |
| 4 | $(3,1)$ | $21$ | $42$ | $42$ | $22$ | $22$ |
| 5 | $(7/2,3/2)$ | $32$ | $64$ | $64$ | $33$ | $33$ |
| 6 | $(4,2)$ | $45$ | $90$ | $90$ | $46$ | $46$ |
| 7 | $(9/2,5/2)$ | $60$ | $120$ | $120$ | $61$ | $61$ |
| 8 | $(5,3)$ | $77$ | $154$ | $154$ | $78$ | $78$ |

**⌗ THE ISOMETRY THAT FORCES IT.** *$\sigma:g\mapsto g^{-1}=\mathrm{diag}(1,-1,-1,-1)$ on the embedding
$\mathbb{R}^{4}$: $\sigma^{\mathsf T}\sigma=I$, $\det\sigma=-1$, and $\sigma(gq)=\sigma(q)\sigma(g)$ to
$1.1\times10^{-16}$ over $200$ random unit-quaternion pairs.* ⇒ *exchanges the $\mathrm{SU}(2)$ factors,
commutes with the Laplacian, anti-commutes with the curl.*

**⌗ THE PARITY-ODD EXPECTATION, AND WHAT CARRIES THE ZERO.**

| state | $\langle X\rangle$ |
|---|---|
| Hartle–Hawking at the common $\beta$ (Fock) | $-1.7\times10^{-18}$ |
| closed form, $\sum_n[d_n^{+}-d_n^{-}]\,n_B(\beta\mu_n)$, $n=2$–$8$ | $0$ exactly |
| *CONTROL: unequal degeneracies* | *$0.1366$* |
| *CONTROL: frequencies split $10\%$* | *$0.3767$* |

**⌗ THE ROTATING CONTROL — what an actual break looks like.** *Chemical potential $\beta\Omega$ on the
helicity charge:*

| $\Omega$ | $0$ | $0.05$ | $0.10$ | $0.20$ | $0.50$ |
|---|---|---|---|---|---|
| $\langle X\rangle$ | $0$ | $+0.12486$ | $+0.25013$ | $+0.50356$ | $+1.31840$ |

*Ratio $\langle X\rangle(0.10)/\langle X\rangle(0.05)=2.0033$ against $2$ — linear, so the break is a
genuine parity-breaking potential.* ⇒ ***The de Sitter cosmological horizon has $\Omega=0$.***

⛔ **BOUND:** *not that the tower is achiral (`r4547` stands); nothing about the interacting tower's
ultraviolet definition; the anomaly step is a reading of the corpus's index obstruction and not computed
here; the declined $S=A/4$ question untouched; the floor-as-subtraction-point candidate not built.*

⌗ *`receipts/P10_canonical_time/P10_the_thermal_condition_is_helicity_blind_at_the_mode_functions_and_the_parity_odd_entry_is_not_owed.py`*

---

# ⚑⚑ r6863+cc66.31 — `PO-51`: THE FLOOR IS FORCED AS A MODE, NOT AS A SUBTRACTION POINT

*The free transverse-traceless tower of `P10` `sec:lock`: $d(m)=2(m^{2}-4)$, $\mu(m)=\sqrt{m^{2}-3}$,
$m=n+1\ge3$. Nothing below uses the coupled tower — `PO-23` is fenced and is not reached.*

**⌗ THE FLOOR, FORCED.**

| | $m=2$ | $m=3$ (the floor) | $m=4$ |
|---|---|---|---|
| $j_R=(m-3)/2$ | $-1/2$ — no representation | $\mathbf{0}$ | $1/2$ |
| $d(m)=2(m^{2}-4)$ | $0$ | $\mathbf{10}$ | $24$ |
| $\mu(m)$ | — | $\mathbf{\sqrt6=2.449490}$ | $3.605551$ |

*Gapped, no zero mode, no soft region.* ⇒ *the infrared is regulated by the geometry.*
**CONTROL:** *a floor at $10^{-6}$ gives an infrared-weighted sum of $1.0\times10^{12}$ against this
tower's $0.122$.*

**⌗ THE LOG, AS AN ANALYTIC STRUCTURE.** *$d\mu=2m^{3}-11m+\tfrac{39}{4m}+\tfrac{45}{8m^{3}}+\cdots$;
$Z(s)=\sum_{m\ge3}d(m)\mu(m)m^{-s}$:*

| pole | measured residue | exact |
|---|---|---|
| $s=4$ | $1.9999737$ | $2$ |
| $s=2$ | $-10.999952$ | $-11$ |
| $\mathbf{s=0}$ | $\mathbf{9.750007418}$ | $\mathbf{39/4}$ |

⇒ *a pole at $s=0$ is scheme-independent, so no regularisation returns a unique finite part.*

**⌗ THE SUBTRACTION POINT MOVES THE CONSTANT AND NOT THE COEFFICIENT.**

| cut $M_1/M_2$ | $L$ (identical at $m_0=3,5,10,50$) | spread across $m_0$ | $\lvert L-39/4\rvert$ |
|---|---|---|---|
| $400/800$ | $9.7500189817039$ | $2.56\times10^{-30}$ | $1.90\times10^{-5}$ |
| $4000/8000$ | $9.7500001901607$ | $2.33\times10^{-26}$ | $1.90\times10^{-7}$ |
| $40000/80000$ | $9.7500000019020$ | $4.96\times10^{-22}$ | $1.90\times10^{-9}$ |

*The $m_0$-spread is the summation's own rounding, $25$ orders below the truncation error.*
**CONTROL:** *a mass shift $\mu^{2}\to m^{2}-3+\delta$ MOVES $L$ — $\delta=1\Rightarrow7$,
$\delta=3\Rightarrow0$ — so the invariance is a fact and not a tautology.*
**CONTROL:** *at $\mu^{2}=m^{2}$ the product is the polynomial $2m^{3}-8m$, $L=0$, and the $1/m$ term
does not exist — no pole, no subtraction point, no question.*

**⌗ THE FINITE PART, AND WHAT IT COSTS TO MOVE IT.**

| subtraction at | constant |
|---|---|
| $m_0=3$ (**the floor**) | $\mathbf{-8.51485690643\ldots}$ |
| $m_0=5$ | $C+4.980549831718$ |
| $m_0=10$ | $C+11.73873484218$ |
| $m_0=50$ | $C+27.43075448841$ |

*Shift $=\tfrac{39}{4}\ln(m_0'/m_0)$ exactly, verified to $10^{-12}$ against the direct sum.*

**⌗ WHY NOTHING MEASURES IT.** *Derived here rather than quoted: the closed synchronous slicing
$a(T)=\alpha\cosh(T/\alpha)$ has $R=12/\alpha^{2}$, **constant** — exactly de Sitter — so `sec:lock`'s
one-dimensional counterterm basis holds on the tower's own background, the log's counterterm is
degenerate with the cosmological term, and `P17` absorbs a constant vacuum energy into the one observed
curvature with no bare-versus-vacuum split.*

⇒ ***FORCED AS A MODE, CONVENIENT AS A SUBTRACTION POINT.*** *The one-scale claim rules out a second
LENGTH and a mode number is dimensionless, so it protects every choice equally.*

⛔ **BOUND:** *not that the one-scale claim fails — the opposite for the part that matters; nothing
about `PO-23`'s ultraviolet definition; the Weyl-squared entry off the admitted family is named and not
claimed; $39/4$ is not discharged (`r6436` stands).*

⌗ *`receipts/P10_canonical_time/P10_the_floor_is_forced_as_a_mode_but_the_subtraction_point_is_a_convention_and_the_residue_is_the_absorbed_constant.py`*

---

# ⚑⚑ r6875+cc66.32 — `PO-47`: THE SKY'S OWN FOURTH PEAK, WITH THE COVARIANCE CARRIED

⚠ ***A CORRECTION TO `cc66.28`'s YARDSTICK.*** *That receipt quoted the sky's fourth peak as
$1121.9\pm0.87$ and used the $0.87$ throughout. **It is a procedure spread** — the window sweep on one
realisation — not the sky's uncertainty.*

**⌗ THE SKY'S FOURTH PEAK, WITH `plik_lite`'s BANDPOWER COVARIANCE PROPAGATED THROUGH THE SAME PARABOLA.**

| | value |
|---|---|
| central | $1121.9$ |
| statistical (COV_TT, $600$ realisations, $W=55$) | $\pm2.03$ |
| procedure (seven-window sweep) | $\pm0.87$ |
| **combined** | $\mathbf{\pm2.21}$ ($\pm1.57$ at $W=80$) |

**⌗ THE WINDOW, CHOSEN ON THE BIAS–VARIANCE TRADE.**

| $W$ | kept | $\sigma_1$ | $\sigma_2$ | $\sigma_3$ | $\sigma_4$ | bias$_4$ | |
|---|---|---|---|---|---|---|---|
| $40$ | $529/600$ | $4.38$ | $13.83$ | $2.72$ | $122.32$ | $+0.05$ | ⛔ |
| $55$ | $600/600$ | $2.39$ | $2.61$ | $1.92$ | $\mathbf{2.03}$ | $+0.63$ | ✔ |
| $80$ | $600/600$ | $1.33$ | $1.34$ | $1.09$ | $\mathbf{1.31}$ | $-0.37$ | ✔ |
| $110$ | $600/600$ | $0.80$ | $0.83$ | $0.69$ | $0.96$ | $\mathbf{-6.38}$ | ⛔ |

*Seed-independent to $2\%$ ($2.07$ against $2.03$).*

**⌗ THE THREE PAIRINGS AT THE FOURTH PEAK.**

| pairing | offset | $\sigma$ at $W=55$ | $\sigma$ at $W=80$ |
|---|---|---|---|
| **CR arm − control** | $+2.00$ | $\mathbf{+0.90}$ | $\mathbf{+1.27}$ |
| control − sky | $+2.65$ | $+1.20$ | $+1.69$ |
| CR arm − sky | $+4.65$ | $+2.10$ | $+2.96$ |

⇒ ***The construction's own displacement does not reach significance at either admissible window.***
*$57\%$ of the arm-minus-sky offset is the control's — a **shared** offset, not this construction's.*

**⌗ CONTROL — the machinery can see a displacement.**

| planted | recovered |
|---|---|
| $4.0$ | $+4.56$ |
| $10.0$ | $+11.71$ |

⛔ **⌗ AND THE INSTRUMENT TRAP.** *`cc66.28`'s free-extremum locator under the covariance:*

| peak | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| free search | $221.7\pm3.3$ | $526.2\pm54.7$ | $754.7\pm117.3$ | $\mathbf{1050.7\pm131.5}$ |

***Seventy multipoles off. Error propagation through that locator must anchor the window.***

⛔ **BOUND:** *`COV_TT` is the shipped bandpower covariance with foregrounds and calibration
marginalised — no beam or theory-side term; the central value is the locator's on `plik_lite`'s binning
(`sec:intro`'s own $1123.9$ is two multipoles away, inside); **none of the three candidates is run**;
nothing re-opens the phase intercept, the damping envelope, the driving or the refit.*

⌗ *`receipts/P15_CR_cosmology/P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart_and_the_displacement_is_shared_with_the_control.py`*

---

# ⚑⚑ r6879+cc66.33 — THE ACOUSTIC FIGURE, AND THE RESIDUAL IS MOSTLY THE CONTROL'S

⛔ *** HEADING PARTLY WITHDRAWN at `r6881+cc66.34`. *** *The shared fraction is right and "mostly the control's" does not follow from it — see that entry. The measurements below stand; the reading of the first table does not.*

*Both arms at their verified $185$-bin refit minima, through P15's derived lensing operator, binned,
amplitude on the **full** bandpower covariance. Pipeline checked first: $186.51$ and $292.42$ over
$185$ bins, reproducing the refit's own to $0.05$.*

**⌗ THE SHARED FRACTION — the deciding number.**

| | |
|---|---|
| $\cos(w_{\rm CR}, w_{\rm ctl})$ | $+0.8549$ |
| shared fraction of the arm's $\chi^{2}$ | $\mathbf{73.1\%}$ |
| residue after projecting the control's direction out | $76.2$ of $283.0$ |
| bin cuts $100$–$1996$ / $100$–$1500$ / $200$–$1900$ | $73.7\%$ / $72.5\%$ / $73.6\%$ |

**⌗ ONE FURTHER PARAMETER AT A TIME (179 bins, $\ell\le1900$).**

| | best | $\Delta\chi^{2}$ arm | $\Delta\chi^{2}$ control |
|---|---|---|---|
| peak-position rescale $\varepsilon$ | $-7.5\times10^{-4}$ | $\mathbf{+4.68}$ | $+0.00$ |
| damping-shape | $+1.69\times10^{-2}$ | $+1.36$ | $+0.30$ |
| tilt $\delta n_s$ | $-1.25\times10^{-3}$ | $+0.09$ | $+0.00$ |

*$\delta n_s=+0.01$ **costs** $+11.2$ — the refit spent the tilt. $\varepsilon$ is $0.8$ in $\ell$ at
the fourth peak; $4.7/283 = 1.7\%$ of the misfit.*

**⌗ BAND MEANS IN SIXTHS, $\ell=100$–$1300$.**

| | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| CR, covariance amplitude, diagonal $\sigma$ | $-0.61$ | $-0.07$ | $+0.33$ | $+0.54$ | $-1.06$ | $-0.36$ |
| CR, whitened | $-0.63$ | $-0.08$ | $+0.35$ | $+0.55$ | $-0.99$ | $+0.02$ |
| CR, **diagonal** amplitude | $-0.34$ | $+0.31$ | $+0.79$ | $+1.08$ | $-0.51$ | $+0.19$ |
| control, covariance amplitude | $-0.18$ | $-0.03$ | $+0.16$ | $+0.12$ | $-0.32$ | $-0.04$ |
| *r6879's quick render (CR)* | *$-0.22$* | *$-0.07$* | *$+0.42$* | *$+1.46$* | *$-1.86$* | *$-0.06$* |

*Band rms $0.78 \to 1.39$ across the range. $A_{\rm diag}/A_{\rm cov} = 1.00833$ (arm), $1.00255$
(control).*

⛔ **BOUND:** *no mechanism for the bulk of the misfit — four directions excluded as the whole of it
and none offered; "the transfer's" is the order's phrase for **not construction-specific**, not a claim
about the implementation; the refit minima are `r6825+cc66.25`'s, used as banked; the low-multipole
floor's score is `r6831`'s, untouched; whitening mixes bins, so a whitened band mean is over a rotated
basis and is reported beside the diagonal one.*

⌗ *`corpus/make_fig_acoustic_two_arm.py` → `corpus/fig_acoustic_two_arm.pdf`;
`spectra/cc66_fig_acoustic_numbers.npz`;
`receipts/P15_CR_cosmology/P15_three_quarters_of_the_arms_residual_is_the_controls_and_what_is_left_is_position_not_amplitude.py`*


# ⚑⚑ r6881+cc66.34 — ⛔ THE SHARED FRACTION DOES NOT MEAN WHAT I SAID, AND THREE OF FOUR DIAGNOSTICS ARE THE ARM'S

**⌗ THE ALGEBRA, WHICH IS WHY.** *Both arms fitted to the same data:*
$r_{\rm CR}=r_{\rm ctl}+(m_{\rm CR}-m_{\rm ctl})$ *exactly — $\max\lvert\cdot\rvert = 8.9\times10^{-16}$ on the
fitted vectors. **The shared $-d$ term makes a "shared fraction" a similarity of MODELS.***

**⌗ THE CONTROL THAT BREAKS IT — a model nobody believes.**

| flat $\Lambda$CDM, tilted | $\chi^2$ | shared with the control |
|---|---|---|
| $\delta n_s=+0.02$ | $214.6$ | $\mathbf{82.2\%}$ |
| $\delta n_s=+0.05$ | $408.8$ | $42.5\%$ |
| $\delta n_s=+0.10$ | $1083.8$ | $15.6\%$ |
| $\delta n_s=-0.05$ | $428.4$ | $42.2\%$ |
| **CR arm** | $283.0$ | $73.1\%$ |

**⌗ THE DECOMPOSITION THAT REPLACES IT (179 bins, $\ell\le1900$).**

| | |
|---|---|
| control | $177.88 = \mathbf{0.994}$/bin |
| CR arm | $282.96 = 1.581$/bin |
| excess | $\mathbf{+105.08}$ |
| $\lvert m_{\rm CR}-m_{\rm ctl}\rvert^2$ | $\mathbf{77.3}$ |
| $2\,r_{\rm ctl}\!\cdot\!\Delta$ | $+27.8$ |
| $\lvert r_{\rm ctl}\rvert,\ \lvert\Delta\rvert,\ \lvert r_{\rm CR}\rvert$ | $13.34,\ 8.79,\ 16.82$ |

**⌗ `r6881`'s FOUR, BOTH METRICS, WITH THE ROUTED VALUE BESIDE EACH.**

| | routed (diag) | diagonal amplitude | whitened |
|---|---|---|---|
| (1) control peaks / troughs | $+0.57$ / $-0.67$ | $\mathbf{+0.03}$ / $\mathbf{-0.06}$ | $+0.03$ / $-0.07$ |
| (1) arm peaks / troughs | $+0.93$ / $-1.11$ | $+0.36$ / $-0.51$ | $+0.42$ / $-0.52$ |
| (2) correlation | $0.96$ | $0.837$ | $0.855$ |
| (2) slope | $1.28$ | $1.137$ | $1.078$ |
| (2) **rms ratio** | $1.34$ | $\mathbf{1.357}$ | $1.261$ |
| (3) control thirds | $0.66/0.96/1.46$ | $0.67/0.77/\mathbf{0.88}$ | $0.66/0.74/0.89$ |
| (3) arm thirds | $0.69/1.39/2.09$ | $0.68/1.12/1.00$ | $0.72/0.91/1.09$ |
| (4) control, $\ell\,950$–$1080$ ($n=15$) | $-1.56$ | $\mathbf{+0.06}$ | $-0.07$ |
| (4) arm, $\ell\,950$–$1080$ | $-2.66$ | $-0.64$ | $-1.09$ |

*Peaks/troughs sorted by the sign of the **control's** binned $\mathcal{D}_\ell$ curvature for both arms
($93$ / $86$), so the two share one partition.*

⛔ **BOUND:** *withdrawing "it is the transfer's" is **not** exonerating the transfer — no statistic here
separates a transfer defect from a cosmology difference and none is offered; no mechanism is added;
`cc66.33`'s band means, single-parameter scans and figure are untouched; the diagnostics are on this tree's
$179$ scored bins at $\ell\le1900$, the figure's own cut and not the order's; each arm's own curvature for
the split is not run.*

⌗ *`receipts/P15_CR_cosmology/P15_the_shared_fraction_does_not_mean_what_i_said_and_the_peak_trough_pattern_is_the_arms_alone.py`
— 14 gates, four controls. Phrase registered in `corpus/check_withdrawn.py`.*


# ⚑⚑ r6885+cc66.35 — THE MODEL DIFFERENCE IS AN ACOUSTIC **CONTRAST** DIFFERENCE, AND THE REJECTION IS NOT ONE SKY'S LUCK

**⌗ THE DECOMPOSITION (179 bins, $\ell\le1900$, both arms at their own 185-bin minima).**

| | |
|---|---|
| $\chi^2_{\rm ctl}$ | $177.88$ |
| $2\langle r_{\rm ctl},\Delta\rangle$ | $+27.82$ |
| $\lVert\Delta\rVert^2$ | $\mathbf{77.26}$ |
| $\chi^2_{\rm arm}$ (sum, exact) | $282.96$ |
| $\lVert\Delta\rVert^2$ as a share of the $+105.08$ excess | $\mathbf{73.5\%}$ |
| cross term against its sky-random null $2\lVert\Delta\rVert=17.58$ | $\mathbf{+1.58\sigma}$ |
| $E[\chi^2_{\rm arm}]$ on a typical sky $= n+\lVert\Delta\rVert^2$ | $256.3 = \mathbf{1.43}$/bin |

**⌗ THE COEFFICIENT, AND IT IS THE CROSS TERM.**

| | whitened | diagonal |
|---|---|---|
| cosine / correlation | $+0.8549$ | $+0.8373$ |
| norm / rms ratio | $1.2612$ | $1.3569$ |
| **coefficient** | $\mathbf{1.0782}$ | $1.1367$ |

*`r6885`'s $1.15 = 0.855\times1.34$ multiplies the WHITENED cosine by the DIAGONAL rms ratio.*
⛭ $b-1 = \langle\Delta,r_{\rm ctl}\rangle/\lVert r_{\rm ctl}\rVert^{2}$ **identically** (to $3\times10^{-16}$),
so $sd(b)=\lVert\Delta\rVert/\lVert r_{\rm ctl}\rVert^{2}=0.0494$ and $b=1.078\pm0.049$, $+1.58\sigma$.
Bin cuts $100$–$1996$ / $100$–$1500$ / $200$–$1900$ / $100$–$1900$: $b = 1.075/1.057/1.073/1.078$ at
$+1.58/+1.07/+1.48/+1.58\sigma$, with $\lVert\Delta\rVert^2$ above the cross term at every one.

**⌗ $\Delta$'s SHAPE.**

| | |
|---|---|
| $\Delta/\sigma$ at peaks / troughs | $+0.011$ / $\mathbf{-0.760}$ |
| $\mathcal{D}_\ell$ ratio arm/control at peaks / troughs | $0.9985$ / $0.9856$ |
| oscillatory part of $\lVert\Delta\rVert^2$ (envelope poly deg $3/5/7$) | $74.9$ / $67.1$ / $66.4$ of $77.26$ |
| the oscillatory part's own peak / trough means | $+0.389$ / $-0.420$ |
| **arm's oscillation about its own envelope, as a fraction of the control's** | $\mathbf{1.0401}$ (window $0.75$–$1.5$ periods: $1.041/1.040/1.036/1.028$) |
| $\lVert\Delta\rVert^2$ in $\ell\,900$–$1500$ | $52.4\%$ |

**⌗ WHAT $\Delta$ IS ORTHOGONAL TO (amplitude marginalised).**

| direction | cos with $\Delta$ | share of $\lVert\Delta\rVert^2$ |
|---|---|---|
| amplitude (the fitted $A$) | $-0.0027$ | $0.00\%$ |
| position (peak rescale) | $+0.0990$ | $0.98\%$ |
| tilt $\delta n_s$ | $+0.0444$ | $0.20\%$ |
| damping shape | $-0.0776$ | $0.60\%$ |
| **CONTRAST (built from the control alone)** | $\mathbf{+0.7151}$ | $\mathbf{51.13\%}$ |
| span of position+tilt+damping | | $5.73\%$ |
| **span with the contrast direction** | | $\mathbf{66.84\%}$ |

*Contrast direction across its one window: $51.3/51.1/50.2/46.2\%$.*

**⌗ THE SHORT LIST, each knob off BOTH arms.**

| candidate | $\lVert\Delta_{\rm off}\rVert^2$ | of base | cos with $\Delta$ | contrast |
|---|---|---|---|---|
| $LN\,12\to24$ (neutrino depth) | $72.37$ | $93.7\%$ | $+0.999$ | $1.0393$ |
| `NOISW=1` (early ISW) | $71.70$ | $92.8\%$ | $+0.974$ | $1.0438$ |
| `DRE=0` (driving, Euler half) | $52.74$ | $68.3\%$ | $\mathbf{-0.163}$ | $1.0395$ |
| `DRC=0` (driving, continuity half) | $67.65$ | $87.6\%$ | $+0.978$ | $1.0384$ |
| **base** | $77.26$ | $100\%$ | $+1.000$ | $\mathbf{1.0401}$ |

*The handover amplitude $0.4835\to0.5$ is excluded EXACTLY without a run: $\hat\Theta$ is set
$k$-independently, so $\chi^2$ moves by $8.5\times10^{-13}$ and the residual by $3.7\times10^{-14}$.*
⚠ *`DRE=0` rotates $\Delta$ to cos $-0.16$ while shrinking its norm by a third — $\Delta$ **replaced**,
not reduced — so the $32\%$ is a norm and not a share; and every row is a large excursion, not a
derivative.*

**⌗ ⛔ AND A KNOB SHADOW, WITH ITS CALIBRATION.**

*`_SWSRC` and `_DPSRC` are read ONLY inside `los_spectrum`; `HIER=1` takes the other path, which
carries `_ISW` and not these two. `DPSRC=0` at the refit configuration returns a **bit-identical**
spectrum on both arms ($0.0$ exactly), and the same knob on the LOS path moves $\mathcal{D}_\ell$ by
$62\%$ — the pair is what makes it a shadow rather than a null.*

**⌗ THE FIFTH CANDIDATE, ON THE PATH WHERE THE KNOB REACHES.**

| | ‖Δ_LOS‖² | contrast (arm/ctl) | cos with the CONTRAST direction |
|---|---|---|---|
| LOS base | $128.43$ | $1.0325$ | — (cos with $\Delta_{\rm HIER}$ $+0.757$) |
| `DPSRC=0` | $261.62$ | $1.0352$ | ctl $+0.877$, arm $\mathbf{+0.893}$; each arm's own oscillation $\to1.85$ |
| `SWSRC=0` | $134.05$ | — | arm $\mathbf{-0.791}$; its own oscillation $\to\mathbf{-0.300}$ (**inverts**) |

⇒ ⚑ **The two halves of the source bracket the contrast with opposite signs: the contrast direction IS
the monopole-to-dipole balance.**

**⌗ AND `r6887`'s SHARPENED ASK — $\Delta$ AGAINST THE THREE FEATURES `cc66.34` SHOWED ARE THE ARM'S.**
*Both arms' residuals on the same covariance-fitted amplitude, so arm $-$ control $=\Delta$ exactly.*

| feature | control | arm | $\Delta$ |
|---|---|---|---|
| (1) at the peaks | $-0.104$ | $-0.093$ | $+0.011$ |
| (1) at the troughs | $-0.200$ | $-0.960$ | $\mathbf{-0.760}$ |
| (4) $\ell\,950$–$1080$ ($n=15$) | $-0.103$ | $-1.177$ | $\mathbf{-1.074}$ — $91\%$ of the arm's deficit, $23.4\%$ of $\lVert\Delta\rVert^2$ |
| (3) $\lvert\cdot\rvert$, third 1 | $0.668$ | $0.718$ | $0.332$ |
| (3) $\lvert\cdot\rvert$, third 2 | $0.746$ | $0.899$ | $0.550$ |
| (3) $\lvert\cdot\rvert$, third 3 | $0.871$ | $1.140$ | $0.681$ |

⇒ ***All three are $\Delta$'s.*** *And $\Delta$ grows **monotonically** where the residuals do not — a
residual is $\Delta$ plus a noise floor of order one, and the floor flattens the growth.*

⛔ **BOUND:** *naming the shape is not naming the mechanism; the channel is identified and the cause is
NOT measured — deleting the Doppler term is all-or-nothing, it leaves the arms' contrast RATIO where it
was and DOUBLES $\lVert\Delta\rVert^2$, so the arms differ in HOW MUCH the channel supplies and not in
whether it is there, and measuring that wants the term SCALED and wired into the hierarchy path first;
$33\%$ of $\lVert\Delta\rVert^2$ is unnamed by any direction here; $LN$ is a direction and not a
convergence test; the LOS path's $\chi^2$ is not comparable with the hierarchy path's; and nothing here
bears on transfer-versus-cosmology, which `r6881+cc66.34` withdrew the statistic for.*

⌗ *`receipts/P15_CR_cosmology/P15_the_model_difference_is_an_acoustic_contrast_difference_and_it_is_not_one_skys_luck.py`
— five parts, **38 gates**. Seven banked pairs at `spectra/r6885_*` with their commands in
`spectra/README.md`; launchers at `/tmp/n66/r6885/launch{,2}.sh`, idempotent.*


# ⛭⛭ r6889+cc66.36 — THE KNOB SHADOW CLOSED WITH ITS DEFAULT PROVED AT EXACTLY ZERO, AND THE NEUTRINOS GET A KNOB

**⌗ THE REPAIR.** *`_SWSRC` and `_DPSRC` now reach all three source constructions — `los_spectrum`,
the hierarchy path (`los_hier`) and the low-multipole path (`main`) — where they reached one. The
monopole bracket is **split** so the switch multiplies $g(\Theta_0+\Psi)$ and not the polarisation
term that shares it and already has `PISRC`.*

| | max $\lvert\Delta\mathcal{D}_\ell\rvert$ against the banked base |
|---|---|
| `r6889_noop_lcdm` | $\mathbf{0.0}$ |
| `r6889_noop_cr` | $\mathbf{0.0}$ |

⚠ *And that took a second attempt, recorded rather than tidied away: written
`_SWSRC * g_ * (\Theta_0+\Psi) + g_ * \ldots` the default sums in a different **order**, which cost
$1.1\times10^{-16}$ — immaterial physically and still not zero. Keeping the factor INSIDE the bracket
makes it exact, because $x\times1.0$ is.*

**⌗ THE CALIBRATION, each newly wired switch on the path it was newly wired into.**

| knob | control | arm |
|---|---|---|
| `DPSRC=0` | $62.3\%$ | $61.3\%$ |
| `SWSRC=0` | (see below) | (see below) |
| `NUFS=0` | $36.3\%$ | $37.3\%$ |

⛭ ***`DPSRC=0` moved the reporting path by exactly $0.0$ before the repair and $62\%$ after — that
pair is what makes the shadow a proof rather than a story.***

**⌗ THE TWO BRACKETING TESTS, ON THE REPORTING PATH (r6885's LOS values in brackets).**

| test | $\lVert\Delta_{\rm off}\rVert^2$ | of base | contrast ratio | arm's own oscillation | cos with CONTRAST |
|---|---|---|---|---|---|
| `DPSRC=0` | $149.30$ | $193.3\%$ | $1.0376$ | $+1.828$ [$+1.855$] | $\mathbf{+0.798}$ [$+0.893$] |
| `SWSRC=0` | $229.69$ | $297.3\%$ | $1.0818$ | $\mathbf{-0.399}$ [$-0.300$] | $\mathbf{-0.765}$ [$-0.791$] |
| base | $77.26$ | $100\%$ | $\mathbf{1.0401}$ | — | — |

⇒ ***The same opposite-sign bracket on both paths, so the contrast direction IS the monopole-to-dipole
balance and that reading was not the path's.*** ⌗ *The two deletions are not equally inert on the
ratio: the dipole moves it $-0.0025$, the monopole $+0.042$, and neither collapses it toward $1.000$.*

**⌗ ⚑ `NUFS` — THE FREE-STREAMING KNOB, FOUR LINES.**

*$\sigma_\nu = F_2/2$ at two dynamical sites (the Euler equation and $\Psi$'s shear term), so `NUFS`
multiplies $\sigma_\nu$ and the $F_2$ source on both solver paths. **The quadrupole's IC is exactly
zero** — `y0 = np.zeros((nk, NV))` with no assignment to index 7 anywhere — so at `NUFS=0` it is never
sourced, the whole $\ell\ge2$ ladder stays zero, and the sector is a perfect fluid at the SAME
background density (`FNU`, `Onv`, `Ogv` untouched).*

| peaks | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| control, free-streaming | $221$ | $536$ | $815$ | $1130$ | $1418$ | $1733$ |
| control, perfect fluid | $230$ | $545$ | $824$ | $1139$ | $1436$ | $1750$ |
| arm, free-streaming | $221$ | $536$ | $815$ | $1130$ | $1427$ | $1733$ |
| arm, perfect fluid | $230$ | $545$ | $824$ | $1139$ | $1436$ | $1750$ |

⇒ ***Every shift POSITIVE on both arms, $+9.00$ uniformly across the first four*** — the sign the
Bashinsky–Seljak pull has, and the shape a **phase** shift has rather than a rescaling of the acoustic
scale. ⚠ *Exactly one binned grid step ($8.9999$), so the SIGN and order of magnitude are established
and the VALUE is not; and the DRAG half, $36$–$37\%$ in $\mathcal{D}_\ell$, is the large effect and is
not the same number.*
  ⚠ ** THE UNIFORMITY IS CORRECTED AT r6893+cc66.37: sub-bin, on both arms and on two independent locators, the shift RISES with multipole -- about $+3$ near the first peak and about $+12$ by $\ell\sim1500$.  The peak positions compared here were quantised to the $\ell$ grid, so the uniformity was the grid.  The SIGN stands. **

⛭ **AND ONE CORRECTION TO THE ORDER.** *`r6889` says of the source decomposition and the phase shift
that "the two are the same part of the source". **They are two layers.** `SWSRC`/`DPSRC` switch which
line-of-sight terms are projected; the phase shift is in the dynamics that set the dipole before last
scattering. Deleting the Doppler term removes the dipole's contribution; `NUFS` changes what the
dipole IS. Pointing the first at the second would have measured nothing, which is why it is two knobs.*

⛔ **BOUND:** *no mechanism for the contrast imbalance — `r6889` said that boundary is right; no value
for the phase shift as a result about this construction, its size being grid-limited and pointing the
knob at the question being the next order's; the low-multipole path is wired for consistency and NOT
exercised here; and no other knob is audited — three shadows found by three routes says nothing about
a fourth.*

⌗ *`receipts/P15_CR_cosmology/P15_the_source_decomposition_is_reachable_on_the_reporting_path_and_the_neutrinos_have_a_knob.py`
— five parts, **22 gates**. Four pairs banked at `spectra/r6889_*`; launcher at
`computations/beyond_the_wall/r6889_directions/`, idempotent.*



# ⛭⛭ r6893+cc66.37 — THE SWITCH SWEEP IS EXHAUSTIVE, AND THE FREE-STREAMING SHIFT IS MEASURED AND RULED OUT

*`r6891`, two parts. **① Point `NUFS` at the question on a grid that can resolve it** — "a locator on
a finer $\ell$ grid, both arms, so the shift is measured rather than bracketed at one bin step — and
the two arms' shifts compared, since a phase shift common to both is not a candidate for $\Delta$ and
one that differs between them is", with the drag half reported separately and not folded in. **②
Sweep the switches; the rate is the finding** — every environment switch enumerated, each tagged from
the SOURCE TEXT with which of the three source constructions and which of the two solver paths reads
it, and every switch reachable on the reporting path measured. The order's own bound: **the output is
the table, not a repair campaign.***

## ⚑⚑ THE SWEEP, AND WHY ITS FORM IS THE RESULT

**Three knob shadows had been found by three different routes** — `cc66.17`'s tilt literal, the baryon
density, `cc66.35`'s source switches — ***and three by three routes is a rate, not a count***, which
is why a fourth find would not have closed it and an accounting would.

⇒ **Sixty environment switches**, read through `ast` and not from memory. The reporting path is
declared from the dispatch's own three lines — `main:1296` `QSCAN`, `main:1352` `LOS`, `main:1364`
`HIER`, and the `return 0` at `main:1379` that kills the rest of `main` — and branches are pruned
ONLY where an environment comparison settles the test, so **the live set OVER-counts what runs, which
is the safe direction: it can under-report a shadow and never invent one.**

⌗ ** A BINDING IS NOT A USE, and that distinction is the whole of the static half.** A first pass
keyed to binding sites reported fifty-five of sixty live on the reporting path, because
`_DAMPX = float(os.environ.get('DAMPX', 1.0))` sits at module level and executes on every path the
instrument can take. *It proves nothing about whether the value is ever read.*

| | |
|---|---|
| switches read | **60** |
| with a live use site on the reporting path | **51** |
| without one | **9** — `DAMPX`, `DSAVE`, `DSCAN`, `NOPROJ`, `PHISAVE`, `QK`, `QMIN`, `QTURN`, `RD` |
| measured, both arms, one switch at a time | **55** |
| bit-identical runs | **41**, and every one of them accounted for |

⇒ ⚑ **The nine are not taken on the static argument**: all eighteen runs come back at
$\max\lvert\Delta\mathcal{D}_\ell\rvert = 0.0$ **exactly**, `RD` at two different off-default values,
and again at **full $\ell$ reach** — which is where a null could have hidden, `DAMPX` and `RD` both
acting on the damping tail that $\ell\le500$ barely sees.

⇒ ***AND THE ACCOUNTING IS A SET EQUALITY.*** The runs that came back bit-identical are **exactly**
the set four readings predict, with no unexplained null and nothing explained away that in fact moved:

- **OFF-PATH** — the nine, each confined to a declared alternative mode (`qscan`, the line-of-sight
  projection diagnostics, the low-multipole analytic block that `LOS=0` selects).
- **RATE-IDENTITY on the control** — `GSRC`, `LEAFSCALES`, `PHASEONLY`, `PHASEPOW`, `STACKPERT` are
  bit-identically inert on the control and **every one of them moves the arm**, because there `Hphys`
  and `Hleaf` are the same expression, the Jacobian is $1$, and $x\times1.0$ is exact. *The control
  arm being a control — and the same floating-point fact `cc66.36`'s reassociation episode turned on.*
- **ARM-BRANCH** — fourteen switches the arm dispatch reads in the other arm's branch; twelve of them
  move on the arm that does read them.
- **GATED** — `PHASEPOW` is inert at `PHASEONLY=0` on both arms and moves the arm by $176\%$ once
  `PHASEONLY=1`, which is `r4558`'s rule discharged by a run rather than by an argument.

## ⛭ TWO THINGS THE SWEEP DID TURN UP, AND NEITHER IS OF THE `r6476` CLASS

**(i) `LRSFROM` moves the instrument's REPORTED acoustic scale by a quarter and its spectrum by
EXACTLY ZERO.** At `LZSTART=6761` the header's $r_s$ goes $145.38\to110.49$ Mpc and
$\ell_A=\pi D_M/r_s$ goes $301.5\to396.8$ — ***and $\mathcal{D}_\ell$ is bit-identical, at reduced
reach and at full.*** ⌗ *Why, from the source: on all three paths $R_S$ and $\ell_A$ reach a `print`
and the `SAVE` metadata and nothing else, and `hier_run(kk, EE, L_A_, D_M_, R_S_)` **accepts the
acoustic scale, the distance and the sound horizon and loads none of the three.***

⚠ **AND `r6476`'s OWN NOTE IN THE FILE IS WHAT THIS CORRECTS.** It records the switch as
"reachability-checked before use", on the ground that $R_S$ "feeds $\ell_A$ ... AND the header line
... so the knob is visible in the instrument's own report and was seen to move it". ***The print is
not the reported number.*** ⇒ So nothing needs rewiring and no number moves: **what was wrong is the
certification, and it was a certification of the wrong quantity.**

⇒ ⛭ **AND THE CONSEQUENCE POINTS THE USEFUL WAY.** Because no transfer function reads $\ell_A$, the
agreement the instrument prints — $\ell_1/\ell_A = 0.7312$ against the sky's $220.6/301.7 = 0.7312$ —
is between **two independently computed quantities** and not a value fed in. *A reader could have
taken the acoustic scale for an input to the transfer. It is not one.*

**(ii) `LATARG` — which the file calls "the corpus's one fitted number" — has NO ROOT at the CR arm's
adjudicated background.** With `ZSTART` unset the onset solve raises: $f(a)$ and $f(b)$ carry the same
sign across the whole bracket that `r6760+cc66.1` widened to $5\times10^{6}$ for exactly this solve.
*Which is why the refit command supplies `ZSTART=3e7` and every reported number already comes from
that — so nothing moves, but the register had not said the switch is unreachable at the arm's own
minimum.* ⌗ *It is still CONNECTED, which `r4558`'s rule requires before the inertness counts: at
`LATARG=310` the root exists and the spectrum moves.*

## ⚑⚑ AND THE FREE-STREAMING SHIFT, MEASURED — WITH ⚠ A CORRECTION TO `r6889`

Two independent locators, so neither carries the claim alone: **(A)** the parabola vertex at each
acoustic extremum, and **(B)** a sub-bin cross-correlation of the **envelope-normalised** oscillation,
so the amplitude change cannot leak into the position. Run band by band, in bands one acoustic period
wide:

| band | control | arm | difference |
|---|---|---|---|
| $\ell\sim301$ | $+2.91$ | $+3.08$ | $+0.17$ |
| $\ell\sim602$ | $+5.57$ | $+5.67$ | $+0.11$ |
| $\ell\sim904$ | $+9.36$ | $+9.25$ | $-0.11$ |
| $\ell\sim1205$ | $+10.89$ | $+10.86$ | $-0.03$ |
| $\ell\sim1507$ | $+12.60$ | $+12.47$ | $-0.14$ |

⚠ ***IT IS NOT UNIFORM, AND THAT CORRECTS `r6889+cc66.36`.*** That receipt gated the shift as "UNIFORM
across the first four peaks on both arms, which is what a PHASE shift looks like as against a
rescaling of the acoustic scale" — on peak positions quantised to the $\ell$ grid, with a tolerance of
$0.05$ on integers that could only differ by a whole bin. **The uniformity was the resolution.** ⌗
*That is the second time in three revisions that a gate passed because the resolution and not the
physics set the number — `cc66.36`'s reassociation episode was the first — and both are recorded
rather than tidied away.* ⚠ *A pure rescaling does not fit it either: the straight line through the
per-extremum shifts has an intercept of three multipoles, so separating the Bashinsky–Seljak constant
from the $k$-dependent change in the potentials' decay that `NUFS=0` also causes is NOT attempted.*

⇒ ***AND IT IS COMMON TO THE TWO ARMS.*** Largest band-by-band difference **$0.17$ of a multipole**;
in units of each arm's own $\ell_A$ the extremum-averaged shift agrees to $1.7\times10^{-4}$. ⇒ **On
`r6891`'s own criterion — "a phase shift common to both is not a candidate for $\Delta$ and one that
differs between them is" — the free-streaming phase shift is NOT a candidate.**

⇒ ⚑ **AND THE DRAG HALF, KEPT APART FROM THE PHASE AND SPLIT IN TWO, BECAUSE IT IS TWO THINGS.**
Removing free-streaming raises the **envelope** by $25.7\%$ and changes the peak-to-trough
**contrast** by $-1.3\%$ — on both arms, agreeing to $0.0004$ and $0.0006$. ***$\Delta$ is a CONTRAST
difference (`cc66.35`), so this knob's large effect is in the wrong quantity and its arm-difference in
the right quantity is six parts in ten thousand.*** *A second reason, independent of the first.*

⌗ *In $\Delta$'s own space: the two arms' `NUFS` directions sit at a whitened cosine of $0.99918$;
their difference, freely rescaled, could reach $8.7\%$ of $\lVert\Delta\rVert^{2}$ at a **negative**
coefficient — and there is no such freedom, because both arms carry the same neutrino sector.*

⌗ *And the answer is not the grid's: the four spectra were recomputed at `LSTEP=2`, four times the
multipole sampling at the same reach, and the band-by-band locator reproduces the `LSTEP=8` answer to
better than half a multipole on both arms.*

⛔ **BOUND:** *no mechanism for the contrast imbalance — `r6891` says that boundary has not moved and
this does not move it; no attribution of the shift's growth with $\ell$ to the Bashinsky–Seljak term;
and the sweep is of ENVIRONMENT switches, so a hard-coded literal that ought to be a switch is a
different search — `cc66.17`'s `NS` literal is the reminder. The screen runs at `LMAXL=500` and only
the NULLS are re-run at full reach.*

⌗ *`receipts/P15_CR_cosmology/P15_the_free_streaming_knob_is_common_to_both_arms_and_the_switch_sweep_finds_no_further_shadow.py`
— five parts, **46 gates (34 at `r6893+cc66.37`; the twelve added at `r6895+cc66.38` are the finer grids' own and the slicing check's)**. The screen banked at `spectra/r6893_switch_screen_{lcdm,cr}.npz`, the fine
grid at `spectra/r6893_fine_grid_{lcdm,cr}.npz`, the full-reach nulls at
`spectra/r6893_full_reach_nulls_lcdm.npz`. The instrument gains COMMENTS ONLY, and even that is
measured: both arms' bases re-run against the annotated file at exactly $0.0$.*


# ⛭ r6895+cc66.38 — THE SPLIT CLOSED: THE RECEIPT REPRODUCES FROM THE TREE, AND THE FINER GRID IS MEASURED

*`r6895` gated the sweep with one split — the confirmation banks were not in the push, so on `main`
the receipt read thirty-two passed and three failed on bank absence, which is `r4549`'s shape: a
result stated in a message whose receipt does not reproduce from the tree. **The order was one line.
Four banks are pushed and the receipt runs to `GATES: ALL PASS` at forty-six gates.***

## ⚠ THE FINER GRID TOOK TWO ATTEMPTS, AND THE FIRST IS WHY THE SECOND IS BUILT AS IT IS

The first attempt ran each spectrum whole at `LSTEP=2 LMAXL=2000`, about a hundred minutes.
**A container restart destroyed all four at eighty**, because this instrument writes its `npz` only at
the end. ⇒ ***A run longer than its node's own lifetime is not a long run; it is a run that does not
finish.***

| | construction | what it buys |
|---|---|---|
| **A** | `LSTEP=2 LMAXL=900`, whole | **four times** the banked sampling over the first three acoustic bands; cheap because the cost is (number of $\ell$) × (number of $k$) and $k_{\max}$ tracks `LMAXL` |
| **B** | `LSTEP=4 LMAXL=2000`, in eleven (six on the arm) `KSLICE` pieces of 250 modes | **twice** the sampling over all five bands, resumable at slice granularity |

## ⚑ AND THE ANSWER IS NOT THE GRID'S

| | banked, step 8 | A, step 2 | B, step 4 |
|---|---|---|---|
| control, per extremum | $+5.66\,+1.99\,+6.22\,+8.84\,+9.49\ldots$ | $+5.62\,+2.12\,+6.27\,+8.89\,+9.38$ | $+5.63\,+2.10\,+6.28\,+8.85\,+9.48\ldots$ |
| largest disagreement with step 8 | — | $0.135$ | $0.188$ |
| arm, largest disagreement | — | $0.179$ | $0.228$ |

⇒ **Better than a quarter of a multipole on both arms and on both grids — and A does it with $k_{\max}$
cut to $\ell=900$, so the agreement is not a shared truncation.** Band by band on B:
$+2.98/+5.56/+9.36/+10.88/+12.61$ on the control against $+3.15/+5.67/+9.25/+10.85/+12.47$ on the arm.
**The rise stands; the arms' agreement stands at $0.17$ of a multipole; the drag stays an envelope
rescale of $1.2573$ against $1.2577$ with a contrast ratio of $0.9875$ against $0.9869$.**

⚠ *A's `LMAXL` cut takes $k_{\max}$ with it, and the envelope ratio is the quantity that cut moves —
the two arms differ by $0.0048$ there against $0.0004$ at full reach. **So A is the phase check and the
envelope comparison is B's**, stated rather than averaged over.*

## ⛭⛭ AND ONE THING WORTH MORE THAN THE CONFIRMATION, FOUND WHILE TESTING THE SLICING

`r6794` built `KSLICE` for exactly this restart problem, and recorded a caveat: **slices add exactly
only on a uniform $k$ grid**, because `_project` takes $dk=$ `np.gradient(kb)` from the batch it is
handed, and the CR arm's ladder is not uniform.

⇒ ***Measured. Sliced at $k$-index $130$, both arms pay $8\times10^{-9}$. Sliced at multiples of $250$,
which is `KBATCH`, both arms are exact to $10^{-16}$.***

⇒ **So the caveat is AVOIDED rather than tolerated: put the slice boundaries on `KBATCH` and the whole
run and the pieces use the same batches, the same measure inside each, and a non-uniform ladder cannot
enter — because no batch's own $dk$ changes.** *A run too long for its node is exactly divisible on
this instrument, on either arm.*

⚠ *And one gate of mine was the vacuous shape `r6895` had just finished naming: the first version
asserted the caveat DOES bite on the arm and passed on `cr > lcdm`, $8.55\times10^{-9}$ against
$7.41\times10^{-9}$. **Two numbers of the same size satisfy that by luck.** Replaced, and the episode
written into the gate's own text.*

⛔ **BOUND:** *the shape of the rise is NOT pushed as a paper result — `r6895` held it and this does not
move it; no mechanism for the contrast imbalance; and no claim that the rise is the Bashinsky–Seljak
term.*

⌗ *Launchers: `computations/beyond_the_wall/r6893_directions/` — nine idempotent scripts and both
bankers, with a README saying what each is for and why it runs at the grid it does.*


# ⛭⛭ r6897+cc66.39 — THE MONOPOLE'S ZERO POINT IS NOT THE CHANNEL, AND THE TWO RESIDUALS POINT OPPOSITE WAYS

*`r6897`'s order, and it is a measurement and not a mechanism. **(a)** the value $\Theta_0+\Psi$ swings
ABOUT at last scattering, in units of that arm's own $\Psi$. **(b)** what each arm's own
$R=3\rho_b/4\rho_\gamma$ at its own visibility peak accounts for. **(c)** from each residual alone, the
effective displacement that would produce it — *do the two agree?*  Plus the visibility FWHM in the
header, which had been printed only inside `los_spectrum`.*

## ⌗ WHAT THE INSTRUMENT GAINED

`ZPSAVE` saves $\Theta_0$, $\Psi$, $\Phi$ and $\theta_b$ at the visibility peak, wired into `hier_run`
— **the reporting path**. ⌗ *`PHISAVE` already saves fields and is one of the nine switches
`r6893+cc66.37` measured as OFF the reporting path, so using it would have measured the low-multipole
construction and called it the reporting one.* It saves the **undamped** monopole on purpose: the
envelope multiplies the whole of $\Theta_0$, its offset included. **Default gated bit-identical on both
arms before any number is read.**

And the header now carries the visibility peak, its redshift, its FWHM and $R$ there, on every path:

| | $\eta_{\rm LS}$ | $z_*$ | FWHM | $R$ | $1+R$ | $\omega_b$ |
|---|---|---|---|---|---|---|
| control | $281.75$ | $1090.3$ | $\mathbf{38.04}$ Mpc | $0.61063$ | $1.61063$ | $0.021966$ |
| arm | $485.99$ | $1087.9$ | $\mathbf{43.59}$ Mpc | $0.59969$ | $1.59969$ | $0.021524$ |

*The arm's last-scattering surface is $1.146$ times as wide in conformal time — side by side on the
reporting path for the first time.*

## ⚑⚑ (a)/(b) THE ZERO POINT, AND THE CALIBRATION THAT MAKES IT A MEASUREMENT

On both arms the offset approaches the tight-coupling equilibrium $-R\Psi$ **from below**, reaching
$0.78$ of it on the control and $0.76$ on the arm. ⇒ *So (b)'s absolute question answers **no** on both
arms and by nearly the same amount, which is a fact about the approach to equilibrium and not about
either arm: $\Psi$ decays inside the horizon and $R$ grows, so the instantaneous
$-R(\eta_*)\Psi(\eta_*)$ is not the offset.*

⚑ **AND `r4558`'s RULE IS APPLIED TO A MEASUREMENT RATHER THAN TO A KNOB.** *A number that has not been
shown to move when the thing it measures moves is not a measurement.* The control is re-run with
$\omega_b$ displaced $\pm8$ per cent and the estimator **tracks $77$ per cent of a known $\Delta R$** —
and that measured response, not the raw $-R$, is what converts an offset difference into an effective
displacement.

| | value |
|---|---|
| arm $-$ control, measured $\mathrm d(\text{offset})$ | $+0.02381$ |
| what their own $\omega_b$ accounts for | $+0.00968$ |
| **unaccounted** | $\mathbf{+0.01413}$ |
| ⇒ **effective $\mathrm d\omega_b$** | $\mathbf{-2.94\%}$ of the control's |

⇒ ***THE ARM'S OFFSET FALLS SHORT OF WHAT ITS OWN LOADING ACCOUNTS FOR*** — on top of the $-2.0$ per
cent its fitted $\omega_b$ already is, and of the same sign in every third of the wavenumber range.
**Too much loading is what deepens troughs and raises alternation. This arm's monopole behaves as
though it had too little, and its troughs are deeper anyway.** ⌗ *On `r6897`'s own branching this is a
**third** outcome, and it refutes the loading reading **by sign** rather than leaving it undetermined.*

## ⚑⚑⚑ (c) AND THE TWO RESIDUALS DIFFER BY A FACTOR OF SIXTEEN AND IN SIGN

| $\omega_b$ | of control | contrast | alternation |
|---|---|---|---|
| $0.02020872$ | $-8\%$ | $0.97939$ | $+0.028888$ |
| $0.02108736$ | $-4\%$ | $0.99130$ | $+0.030256$ |
| $0.02196600$ | $0$ | $1.00000$ | $+0.032311$ |
| $0.02284464$ | $+4\%$ | $1.00538$ | $+0.034066$ |
| $0.02372328$ | $+8\%$ | $1.00736$ | $+0.035098$ |

Both responses are **positive** — more loading gives more of both, which is what the reading requires,
so neither residual is converted through a response that is not there.

| residual | value | implied effective $\mathrm d\omega_b$ |
|---|---|---|
| contrast | $+0.04015$ | $\mathbf{+22.9\%}$ |
| alternation | $-0.000569$ | $\mathbf{-1.40\%}$ |
| monopole offset (a) | $+0.01413$ | $\mathbf{-2.94\%}$ |

⇒ ***NOT ONE NUMBER. The contrast asks for more loading, the alternation and the monopole offset for
less.*** ⇒ ⚑⚑ **AND THE $+22.9$ IS A LOWER BOUND, BECAUSE THE CONTRAST RESPONSE SATURATES**: over the
whole range the contrast spans only $0.028$ and its increments fall monotonically
($+0.0119, +0.0087, +0.0054, +0.0020$), so a straight line **overstates** what $\omega_b$ can deliver.
***A four per cent contrast excess is beyond what the baryon density reaches in this construction at
any value, not merely at an implausible one.***

⌗ *And two independent measurements of the loading displacement — the monopole offset and the
alternation — agree at $-2.9$ and $-1.4$ per cent. **It is the contrast that stands apart.***

## ⚠ AND PART OF THAT IS A CORRECTION TO THE ORDER'S PREMISE

`r6897` pairs an alternation excess read against the **sky** ($P_1/P_2 = 2.264$ against $2.217$) with a
contrast excess read against the **control** ($1.040$).

| | peaks | heights | $P_1/P_2$ | $P_1/P_3$ |
|---|---|---|---|---|
| control | $220,537,814$ | $0.5339, 0.2437, 0.2406$ | $2.1912$ | $2.2188$ |
| arm | $222,536,815$ | $0.4423, 0.2066, 0.2036$ | $\mathbf{2.1411}$ | $2.1724$ |

⇒ **Against the control — the reference $\Delta$ is built on — the arm's $P_1/P_2$ is LOWER.** *The two
residuals were never pointing the same way; the appearance that they were is the two references.*

## ⛭ ONE POSITIVE LOCALISATION, AND ITS SIGN PROBLEM STATED

The same bank carries $\theta_b$, so this is a measurement and not a further run. **The arm's
dipole-to-monopole amplitude ratio at the visibility peak is $+1.76$ per cent and GROWS with
wavenumber** — $+0.46$, $+1.72$, $+2.79$ per cent in thirds of the range.

⚠ *But the Doppler term is a quarter period out of phase and **fills** troughs — `cc66.36` measured
`DPSRC=0` taking the arm's own oscillation from $1.040$ to $1.828$ — so a larger dipole fraction makes
troughs **shallower**, and this arm's is larger while its troughs are deeper.* ⇒ **It works AGAINST the
contrast excess, which leaves a source larger than four per cent and partly cancelled.** *That is a
statement about size, not a mechanism, and it is as far as this order's measurements reach.*

## ⌗ TWO METHOD NOTES, BECAUSE BOTH COULD HAVE GONE WRONG QUIETLY

**The offset estimator had three biased predecessors, each recorded with the bias it carried.** A
midpoint of successive extrema carries half the amplitude change between them and came out alternating
by a factor of three; the quarter-half-quarter combination of three extrema cancels a **linear**
amplitude variation and left $\pm15$ per cent of curvature; and a one-period fitting window is
ill-conditioned, the constant being nearly collinear with the $\mathrm dq$-weighted oscillation terms.
⇒ *Four periods with a quadratic amplitude gives a $q$-to-$q$ scatter of $0.027$ on an offset of
$-0.477$, and the verdict is unchanged across five settings.*

**And the alternation statistic is not a second difference.** That vanishes only on a **linear** trend
and the envelope's decline is strongly curved, so a second-difference statistic comes out dominated by
the first triple and is mostly curvature. ⇒ *The trend and the alternation are **fitted together**,
$o(p_n) = c_0 + c_1 n + c_2 n^2 + a(-1)^n$, and the sign is shown independent of the trend's degree.*

⛔ **BOUND:** *no mechanism for the contrast imbalance — `r6897` says none is asked for and none is
claimed; no claim that the dipole excess produces the contrast excess, its sign being wrong for it; no
claim that the offset's shortfall against $-R$ is a defect of either arm, it being the same shortfall on
both; and the width story `r6897` withdrew before sending is not reinstated.*

⌗ *`receipts/P15_CR_cosmology/P15_the_monopole_zero_point_is_not_the_channel_and_the_two_residuals_point_opposite_ways.py`
— six parts, **22 gates**. Four banks at `spectra/r6897_*`; launchers at
`computations/beyond_the_wall/r6897_directions/`. **Every long run sliced on `KBATCH`**, which
`r6895+cc66.38` measured as exact to $10^{-16}$ — made one revision ago while testing something else,
and this is the first order it paid for.*

# ⛭⛭ r6911+cc66.40 — THE CONTRAST IS NOT IN THE SOURCE: IT IS MANUFACTURED BETWEEN $k$ AND $\ell$

***`r6911`'s order: take the contrast statistic already in hand and apply it BEFORE the projection as
well as after. Three outcomes named in advance — $\approx1.04$ = made in the dynamics; $\approx1.00$ =
manufactured between $k$ and $\ell$; or a split, and the split is the measurement.***

⚑ **The answer is the second, and it is clean.**

| rung | what it is | ratio arm/control |
|---|---|---|
| 1 | the source at last scattering, $S(k,\eta_{\rm LS})^{2}$ | $0.9960$ |
| 1m | monopole $+$ Doppler only (what the order names) | $0.9937$ |
| 1s | monopole alone | $0.9923$ |
| 2 | the source $\eta$-integrated, $(\int S\,\mathrm d\eta)^{2}$ — the transfer with the kernel taken out | $0.9923$ |
| 3 | the raw $D_\ell$ from the same run | $1.0452$ |
| 4 | lensed, binned, amplitude-fitted — `cc66.35`'s own object | $1.0468$ |

*Over four envelope windows, both envelope definitions, three term subsets, four $q$ sub-windows and
with or without the $k$-measure, **the source rungs span $0.971$–$1.005$ and the $\ell$ rung
$1.042$–$1.052$.*** The statistic's floor is $0.6$ per cent, set by its own bias on a **known injected**
contrast; the step is $5.3$.

## ⛔ SO THE FOUR-FOR-FOUR DISSOLVES RATHER THAN BEING SOLVED

*`r6909`'s sharpest observation was that four channels which each **shallow** the troughs are all larger
on this arm, so something upstream had to be big enough to overcome all four — and therefore the effect
to explain was **bigger** than four per cent.* ⇒ ***Upstream the arm's oscillation is $0.996$ of the
control's — very slightly SHALLOWER, which is exactly the direction all four point.*** **Nothing
overcomes them because nothing had to.** *The effect is not bigger than four per cent; it is not upstream
at all, and the search has been in the wrong half of the chain.*

## ⛔ THE NAMED ROUTE IS OUT TWICE OVER — FIRST A PREMISE CORRECTION, THEN A MEASUREMENT

*`r6911`'s route: the arms' distances differ by six per cent while their acoustic angles agree, so the
same $\ell$ samples a different wavenumber on each and the Bessel kernel has a different width in $k$.*

⚠ ***The pair $13005$ against $13865$~Mpc is the SUPERSEDED configuration's*** ($r_s=135.46/144.53$),
where the arm's was the smaller. At the adjudicated minima:

| arm | $D_M$/Mpc | $r_s$/Mpc | $\ell_A$ |
|---|---|---|---|
| control | $13954.354$ | $145.382$ | $301.543$ |
| arm | $14017.039$ | $145.911$ | $301.799$ |

⇒ **$+0.449$ per cent, and the ARM'S IS THE LARGER** — wrong in size and wrong in sign. *The
cancellation the route relies on is real, $\ell_A$ agreeing to $0.085$ per cent, so it is the six per
cent and not the reasoning that fails.*

⇒ **And the route is eliminated by measurement anyway.** *`SRCXS` projects one arm's own source through
the **other's** comoving distance, one arm at a time, so the geometry is the only thing that moves: the
control's contrast falls $0.63$ per cent, the arm's rises $0.59$, and **removing the difference
altogether takes the arm/control ratio UP, $1.045\to1.051$.***

## ⌗ WHERE IN THE PROJECTION, AND NO FURTHER

*The arm's projection **retains $1.054$ times as much** of its own source oscillation as the control's
does — rms $0.689\to0.166$ against $0.684\to0.174$, suppression $0.2413$ against $0.2543$. That is the
whole finding as one number per arm.* And four things it is **not**:

- not the **visibility width** acting before the kernel: rung 1 → rung 2, where an $\eta$-average acts
  with no kernel, moves the ratio by $-0.4$ per cent. *The arm's visibility is $15$ per cent wider,
  which shallows contrast — a bound on one route, not the identification of another.*
- not the **lensing or the binning**: $1.045\to1.047$.
- not the **$k$ grid**. `KCONT=1` replaces the arm's physical ladder with the uniform continuum
  sampling at the control's own $2547$ modes, physics untouched: the $\ell$ rung is unchanged at
  $1.0452$ and the source rungs move to $1.0041$ and $0.9992$. *That switch is shown non-null, so this
  is a null from a connected knob and not `r4558`'s unwired one.*
- not the **distance**, per above.

*And the excess **rises** with wavenumber — $1.031$ below $q=3$ to $1.065$ above — where the source
ratio is flat, $0.992\to0.992$.*

## ⛔ THE GUARD CHANGED THE DEFINITION, AND THAT IS PART OF THE MEASUREMENT

*`r6885+cc66.35`'s envelope is a running **geometric** mean, which needs a strictly positive quantity.
$D_\ell$ is; **the source power is not** — it comes within a part in $10^{8}$ of its own median at the
troughs, where a log-mean is dominated by near-zeros and $(P-e)/e$ diverges.* ⇒ **The envelope is a
running arithmetic mean at EVERY rung**, both definitions are reported side by side, and they differ by
$0.003$ on the $\ell$ rung against the $0.05$ step being measured. *`cc66.35`'s $1.0401$ is reproduced
exactly under its own definition and is not superseded.*

⌗ **And the abscissa was measured rather than assumed.** $q=kr_s/\pi$ in $k$ and $q=\ell/\ell_A$ in
$\ell$ are the same variable under the sharp-visibility map $\ell=kD_M$, because $\ell_A=\pi D_M/r_s$ —
*so the two arms' acoustic period in $q$ was measured: $1.0000$ against $0.9978$ at the source and
$1.0347$ against $1.0338$ in $\ell$, agreeing to $0.22$ and $0.09$ per cent, with best-fit lags of
$+0.005$ and $-0.001$.* **A regression of two oscillations at a frequency mismatch reads as a contrast
deficit, and that is the one way this measurement could have come out low for no reason.**

⛔ **BOUND:** *no mechanism within the projection — the order asks for none and none is offered; no
claim that the projection is the wrong projection, nothing here touching `prop:flat`; no claim that the
visibility width is its route; and no claim that the source is identical on the two arms — it is
$0.992$, a real deficit of about the statistic's own floor, and that sign is the four channels' own.*

⌗ *`receipts/P15_CR_cosmology/P15_the_acoustic_contrast_is_not_in_the_source_and_the_projection_makes_it_without_the_distance.py`
— seven parts, **45 gates**. Four banks at `spectra/r6911_*`; launchers at
`computations/beyond_the_wall/r6911_directions/`. The instrument gained `SRCSAVE` and `SRCXS`, both
bit-identical when unset on both arms — **and `SRCXS=1.5` with `SRCSAVE` unset is bit-identical too**,
which is what makes the swap an output of the save rather than a knob on the physics. The sliced runs
reproduce the banked $185$-bin refit spectra to $4.9\times10^{-15}$ relative, **which is what makes the
$k$ end and the $\ell$ end one run rather than two.***

# ⛭⛭ r6915+cc66.41 — THE CROSS TERM IS NOT THE CHANNEL: EVERY PROJECTED TERM CARRIES THE EXCESS

***`r6915`'s order: `cc66.40` located the stage, so which TERM carries it after projection? The
monopole–Doppler pair named first, because $j_\ell$ and $j_\ell'$ are a quarter period out of phase
and the projection rotates their relative phase by an amount depending on their relative weight.***

## ⛔ THE CLOSURE GATE THE ORDER FORCED HAD TO BE CORRECTED BEFORE IT COULD BE PASSED

*The order: "the projection is linear in the source, so the separately projected pieces must sum to
the full spectrum. **Gate that first, and read nothing below it if it fails.**"*

⇒ ***The TRANSFER is linear in the source and the pieces add there. $C_\ell$ is QUADRATIC in the
transfer, so the projected SPECTRA cannot add.*** *The four diagonal pieces alone fall short of
$D_\ell$ by up to $46$ per cent — gated as a measurement, not argued.* ⌗ **This is not the order's
third outcome**: its *first* outcome presupposes a cross term, so the two clauses are in tension and
the first is the coherent one.

⇒ **What closes is the full bilinear decomposition.** With $\Delta^a_\ell(k)=\int\text{term}_a
j_\ell\,\mathrm d\eta$ one transfer per source term,
$C_\ell=\sum_{a\le b}w_{ab}\sum_k P\,\Delta^a\Delta^b$ with $w=1$ on the diagonal and $2$ off it —
**ten numbers per multipole, closing on $D_\ell$ to $1.1$ and $1.3\times10^{-15}$ relative.**

## ⛔ ⓵ AND THE CROSS TERM IS NOT THE CHANNEL

| piece | ratio arm/control | rms ctl | rms arm |
|---|---|---|---|
| `sw*sw`  the monopole alone | $1.0343$ | $0.3054$ | $0.3161$ |
| `dp*dp`  the Doppler alone | $1.0988$ | $0.1159$ | $0.1275$ |
| `isw*isw`  the ISW alone | $0.9889$ | $0.2193$ | $0.2170$ |
| `pol*pol`  the polarisation alone | $1.0578$ | $0.3957$ | $0.4189$ |
| the two squares, **no** cross | $1.0484$ | $0.2175$ | $0.2281$ |
| **full minus the `sw*dp` cross** | $\mathbf{1.0451}$ | $0.2192$ | $0.2293$ |
| **FULL (all ten)** | $\mathbf{1.0452}$ | $0.1664$ | $0.1740$ |

*Deleting the cross moves the ratio by one part in ten thousand; over four envelope windows its carry
runs $-0.0013$ to $+0.0008$ of the $+0.045$.* ⇒ ***The interference between $j_\ell$ and $j_\ell'$ is
bounded at about a part in a thousand and is excluded.***

## ⚑⚑ BECAUSE EVERY PROJECTED PIECE ALREADY CARRIES IT — NEITHER OUTCOME THE ORDER NAMED

| term | source ($k$) | projected | change |
|---|---|---|---|
| monopole $g(\Theta_0+\Psi)$ | $0.9920$ | $1.0343$ | $+0.042$ |
| Doppler $\partial_\eta[g\theta_b]/k^2$ | $0.9726$ | $1.0988$ | $+0.126$ |
| ISW | $0.9723$ | $0.9889$ | $+0.017$ |
| polarisation | $0.9904$ | $1.0578$ | $+0.067$ |
| the whole source | $0.9923$ | $1.0452$ | $+0.053$ |

***Every term's source ratio is at or below $0.992$ and every term's projected ratio is higher.*** *So
it is not a term and not a pair of terms: the projection raises this arm's contrast on nearly
everything it projects. `cc66.40` found that for the source as a whole; term by term is why no single
term can be the channel.*

## ⌗ WEIGHT AGAINST RESPONSE — ABOUT $40/60$, THE RESPONSE THE LARGER

*The weight **does** differ, which is the half of the order's reasoning that survives: the arm's
`sw*sw` share is $0.5225$ against $0.5092$ and its `dp*dp` $0.1753$ against $0.1840$.*

- the arm as it is: $1.0452$
- the **arm's** pieces at the **control's** shares: $1.0267$ — the weights carry $+0.0185$
- the **control's** pieces at the **arm's** shares: $1.0254$ — the weights carry $+0.0198$

⇒ *Two crude reweightings run in opposite directions agreeing to $0.001$ is what makes this a **split**
rather than a number. Neither alone is clean: rescaling a piece by its mean share also moves the
envelope, which is why both are reported.*

## ⚑ ⓶ THE RETAINED FRACTION AS A FUNCTION OF $q$ — NOT FLAT

| $q$ band | retain ctl | retain arm | ratio |
|---|---|---|---|
| $0.85$–$1.55$ | $0.3459$ | $0.3561$ | $1.0296$ |
| $1.55$–$2.25$ | $0.1830$ | $0.1950$ | $1.0657$ |
| $2.25$–$2.95$ | $0.2240$ | $0.2381$ | $1.0628$ |
| $2.95$–$3.65$ | $0.2252$ | $0.2430$ | $1.0789$ |
| $3.65$–$4.35$ | $0.1983$ | $0.2130$ | $1.0738$ |
| $4.35$–$5.05$ | $0.1747$ | $0.1898$ | $1.0863$ |
| $5.05$–$5.75$ | $0.2049$ | $0.2231$ | $1.0885$ |

*Over twelve settings — four envelope windows $\times$ three band counts — the slope is
$\mathbf{+0.0139\pm0.0021}$ per unit $q$ and is **never once negative**.* ⇒ **So the order's branch
that would have killed the reading — flat, the $q$ split reading the envelope — is excluded.** ⌗ *The
intercept is $1.017\pm0.010$ and **straddles one**: the rise is established and a constant offset is
not, and $q=0$ is an extrapolation from a lowest band centre of $q=1.20$.*

⛔ **BOUND:** *no mechanism. The order's own words — "naming which two terms interfere is still not a
statement about why their weights differ" — and nothing here names two terms, because it is not two
terms. No claim that the cross term is zero: it is $26$ per cent of $D_\ell$ and its oscillation is
$59$ per cent of the full's; what is bounded is its contribution to the **difference**. No claim that
the Doppler's $1.099$ is as well determined as the monopole's $1.034$ — its piece's relative
oscillation is $0.116$ against $0.305$. And nothing here touches `prop:flat`.*

⌗ *`receipts/P15_CR_cosmology/P15_the_cross_term_is_not_the_channel_and_every_projected_term_carries_the_excess.py`
— six parts, **26 gates**. Three banks at `spectra/r6915_*`; launchers at
`computations/beyond_the_wall/r6915_directions/`. `SRCDEC` is wired into `_project`'s own multipole
loop so the Bessel evaluation is **shared** with the reported spectrum — four trapezoids per
multipole, not a second projection — and it is bit-identical when unset on both arms. **This run's
$D_\ell$ is gated identical to `r6911+cc66.40`'s to $10^{-13}$ relative**, which is what lets a source
rung and a projected rung sit in one ladder.*

# ⛭⛭⛭ r6919+cc66.42 — A SOURCE WITH NO PHYSICS REPRODUCES IT, AND THE TWO CLOCKS PART COMPANY

***`r6919`'s order: ⓵ project an analytic oscillating source — no transfer, no terms, no weights —
through both arms' own machinery and measure the retained fraction against $q$; ⓶ then swap the
visibility and $\chi(\eta)$ one at a time.***

## ⚑⚑ ⓵ THE SOURCE IS IRRELEVANT TO IT

$S = g(\eta)\cos(k r_s(\eta)+\phi)\,k^{(1-n_s)/2}$ — the last factor makes the smooth part of $PS^2$
exactly $\mathrm dk/k$ on **both** arms, so the injection is identical in $q$ and the tilts cannot
enter.

| configuration | ratio | slope / unit $q$ | intercept |
|---|---|---|---|
| sweep, each arm's own clock | $\mathbf{1.0659}$ | $\mathbf{+0.02260}$ | $1.0085$ |
| …and at $\phi=\pi/2$ | $1.0661$ | $+0.02250$ | $1.0090$ |
| fixed phase, no advance across the visibility | $1.0587$ | $+0.01189$ | $1.0204$ |
| **the REAL source (`cc66.41`)** | $1.054$ | $+0.01167$ | $1.0308$ |

⇒ ***The projection's geometry accounts for the whole of the measured effect and over-delivers.*** *The
injection's phase does not matter, and a **standing** oscillation already carries most of it — so the
effect is not only the source's phase sweep; the kernel's own window does part of it.*

## ⛔ THE ORDER'S NAMED CANDIDATE IS IN THE INSTRUMENT, RELOCATED

*The order: $\chi(\eta)$ is "this arm's own conformal-distance-to-time relation", read on the other
clock from the source.* ⇒ ⚠ ***`x0 = eta_0 - EE` on both arms, so $\chi(\eta)=\eta_0-\eta$ and
$\mathrm d\chi/\mathrm d\eta\equiv1$ identically on each, with no `Jac`, `Hleaf` or `Hphys` touching
`x0` on any path. There is nothing there to exchange.***

⇒ ***The two clocks sit between $r_s$ and $\eta$.*** *`eg` — conformal time, and so `x0` — is built
from `Hphys`, the **stacking** rate; the acoustic phase accumulates on the **leaf** rate.*

| arm | `LEAFSCALES` | $\mathrm d\eta_{\rm leaf}/\mathrm d\eta_{\rm stack}$ across $\pm3$ FWHM |
|---|---|---|
| control | False | $1.000000$ — flat, by the rate identity |
| arm | True | $\mathbf{0.789313}$ to $\mathbf{0.912601}$ |

## ⚑⚑⚑ AND THAT IS WHERE THEY PART COMPANY

| arm | FWHM($\eta$) | $\mathrm d r_s$ (own clock) | $\mathrm d r_s$ (stacking) | $\mathrm d\chi$ | $\mathrm d r_s/\mathrm d\chi$ |
|---|---|---|---|---|---|
| control | $38.042$ | $17.3074$ | $17.3074$ | $38.042$ | $0.454950$ |
| arm | $43.591$ | $17.2941$ | $19.8989$ | $43.591$ | $0.396733$ |

***The sound horizon accumulated across the visibility agrees to $0.08$ per cent; the comoving distance
across it differs by $14.6$.*** *The leaf clock makes $r_s$ accumulate more slowly per unit $\eta$, so a
fifteen per cent wider window covers the **same** acoustic phase — and the kernel, which reads $\chi$,
sees the wider window.*

⇒ ***THE JOINT OBJECT IS $\mathrm d r_s/\mathrm d\chi$ ACROSS THE VISIBILITY — the sound speed the
kernel sees — $0.4550$ on the control against $0.3967$ on the arm, $12.8$ per cent lower.***
**Term-independent, growing with wavenumber, and vanishing for a window under one acoustic period: the
three properties `cc66.41` measured.**

## ⛔ ⓶ AND NEITHER SWAP CLOSES IT ALONE

**(a) The clock swap is ILL POSED as an isolation, and the statistic says so rather than returning a
null.** *Forcing both arms' phase onto the stacking clock gives $0.078$ overall — and band by band it
**alternates in sign**: $+0.368 / -0.524 / +0.425 / -0.566 / +0.392 / -0.420 / +0.332$.* ⇒ *Changing the
clock moves $r_s(\eta_{\rm LS})$ and so moves the **comb**; a regression of two oscillations out of
phase reads their mismatch, not their contrast.* ⌗ ***`cc66.40`'s guard was built for exactly this shape
and it fires here.*** *And it is itself evidence the leaf assignment is what the arm's reported peak
positions need — a consistency statement about `LEAFSCALES=1`, not a defect.*

**(b) The visibility-width swap IS well posed, and it overshoots by eight.** *Each arm given the other's
FWHM about its own peak: ratio $1.0565$ but slope $\mathbf{+0.09313}$ — band by band $0.985\to1.380$.*
⇒ *So the width sets the $q$-dependence and not the level, and swapping it **amplifies** the difference
rather than neutralising it.*

⇒ ***They close only together, and what they close on is $\mathrm d r_s/\mathrm d\chi$.*** *That is the
outcome the order named third and asked to have said if it came out this way.*

⛔ **BOUND:** *no mechanism, and the order does not ask for one yet. **Naming $\mathrm d r_s/\mathrm
d\chi$ is not an account of why this construction assigns the scales the plasma accumulates and the
distances the kernel reads to different rates** — that is `P15` §`sec:tensions`' own question and is not
reopened here. No claim that the injection **is** the source: over-delivery is sufficiency, not
identity, and the excess over $1.054$ is not interpreted. No claim that the visibility width is ruled
out — its swap overshoots, which makes it inseparable from the clock, not absent. No claim that
`LEAFSCALES=1` is wrong. And **no `SRCINJ` run is a spectrum of this model**: each is the projection's
transfer of a known input.*

⌗ *`receipts/P15_CR_cosmology/P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_clocks_part_company_at_the_visibility.py`
— four parts, **24 gates**. Four banks at `spectra/r6919_*`; launchers at
`computations/beyond_the_wall/r6919_directions/`. Four new names, bit-identical when unset on both arms
in one result that covers both guards. **The solver is skipped on the injected path**, because the
analytic source replaces `S` entirely — seconds of setup plus the projection, rather than a full run to
build an array nothing reads.*

# ⛭⛭ r6925+cc66.43 — THE RATE RULE'S GAP IS ALREADY OPEN IN THE CODE, AND THE GEOMETRY IS INVARIANT

***`r6925`'s order: which clock is $g=\tau'e^{-\tau}$ a density in, and does the rule determine it? ⓵
audit every rate the visibility and the optical depth touch, recompute $\mathrm dr_s/\mathrm d\chi$
under the other assignment, and report the comb beside the contrast. ⓶ where the source's partial
cancellation sits.***

## ⛔ THE AUDIT: TWO PLASMA-ACCUMULATED OBJECTS ON OPPOSITE CLOCKS

| site | clock |
|---|---|
| the recombination history's expansion rate, `xe_history(lambda z: Hphys(...))` | **stacking** |
| $\tau' = n_e\sigma_T a$, `taup_of` on `eg`'s conformal time | **stacking** |
| the $\tau$ integration's measure, over `_egrid` | **stacking** |
| the visibility, its peak and its FWHM, off `_egrid` | **stacking** |
| $1/k_D^2$'s measure — **Jac-weighted under `LEAFSCALES`** | **LEAF** |

⇒ ***The diffusion length takes the leaf clock and the optical depth the stacking clock, and nothing
in the instrument or the corpus states the choice.*** *So `VISLEAF=1` is not an invention: it applies
to $\tau$ exactly the weighting $1/k_D^2$ already applies to itself.*

## ⚑⚑ ⓵ ON THE GEOMETRY THE TWO ASSIGNMENTS AGREE

| `VISLEAF` | arm $\eta_{\rm LS}$ | arm FWHM | arm $r_D$ | $\mathrm dr_s/\mathrm d\chi$ ctl | arm | ratio |
|---|---|---|---|---|---|---|
| 0 | $485.99$ | $43.591$ | $7.473$ | $0.454950$ | $0.396733$ | $0.8720$ |
| 1 | $483.83$ | $43.952$ | $7.168$ | $0.454950$ | $0.396957$ | $0.8725$ |

***$12.80$ per cent lower becomes $12.75$.*** *And structurally: $\mathrm dr_s/\mathrm d\chi$ is a
**ratio** of two accumulations across the **same** window, so re-weighting the measure re-weights
both.* ⇒ **The visibility is not where the freedom is; the $12.8$ per cent is forced by the rule as
stated.** ⌗ *The switch is not inert on the arm — $\eta_{\rm LS}$, the FWHM and $r_D$ all move — so the
near-null is a connected knob's.*

## ⛔ BUT THE CONTRAST AND THE COMB DISAGREE

**The contrast** — the injection's retained ratio, band by band:

| $q$ | 1.20 | 1.90 | 2.60 | 3.30 | 4.00 | 4.70 | 5.40 | mean | slope |
|---|---|---|---|---|---|---|---|---|---|
| `VISLEAF=0` | 1.029 | 1.055 | 1.070 | 1.088 | 1.107 | 1.100 | 1.146 | $1.0850$ | $+0.02424$ |
| `VISLEAF=1` | 1.039 | 1.011 | 1.073 | 1.109 | 1.048 | 1.190 | 1.015 | $1.0695$ | $+0.01332$ |
| the real source | | | | | | | | $1.0694$ | $+0.01167$ |

*Read alone that is the order's first branch.* ⚠ **But the `VISLEAF=1` bands are non-monotonic scatter
with a fitted residual nine times the current assignment's** — *moving $\eta_{\rm LS}$ moves
$r_s(\eta_{\rm LS})$ and so moves the comb, and a band ratio of two oscillations no longer aligned in
$q$ reads their phase mismatch. `cc66.40`'s guard, firing a third time.*

**The comb:**

| arm | `VISLEAF` | first four peaks | $\ell_1/\ell_A$ | $P_1/P_2$ |
|---|---|---|---|---|
| control | 0 | $220, 540, 812, 1132$ | $0.7296$ | $2.192$ |
| control | 1 | $220, 540, 812, 1132$ | $0.7296$ | $2.192$ |
| arm | 0 | $220, 540, 812, 1132$ | $0.7290$ | $2.142$ |
| arm | 1 | $228, 540, 820, 1140$ | $\mathbf{0.7555}$ | $2.017$ |

*The sky: $\ell_1/\ell_A = 0.7312$.* ⇒ ***The comb moves AWAY from the sky on the arm and not at all on
the control.*** ⇒ ***The geometry says forced, the contrast says improvable, the comb says no — and the
comb is the only one of the three with an external referent. Neither is picked.***

## ⚑ ⓶ THE SOURCE'S CANCELLATION IS HALF THE LEVEL AND NONE OF THE SLOPE

| | mean | slope |
|---|---|---|
| the injection | $1.0850$ | $+0.02424$ |
| $\times$ the source deficit | $1.0766$ | $+0.02296$ |
| the real source | $1.0694$ | $+0.01167$ |
| the source deficit itself | $0.9922$ | $-0.00106$ (**flat**) |

⇒ ***$54$ per cent of the level gap and $10$ per cent of the slope gap.*** *So the four trough-filling
channels account for about half the level difference and essentially none of the slope: **the order's
conditional is half satisfied and the sector does not close into one account**. What flattens the slope
is the real source's own $\eta$-dependence across the visibility — exactly what the injection
replaced — and that is named, not measured here.*

⛔ **BOUND:** *nothing here settles whether the two-rate assignment is right, which is the row's
question now. No claim that `VISLEAF=1` is wrong as physics — what is measured is that it moves the
comb away from the sky while moving the contrast toward the real source, and that its contrast
improvement is partly a phase artefact. No claim that the $0.06$ per cent invariance settles the row:
it says the visibility is not where the freedom is, and the freedom is in the rule's assignment of
$r_s$ itself.*

⌗ *`receipts/P15_CR_cosmology/P15_the_visibilitys_clock_is_the_one_the_kernel_reads_and_the_comb_votes_against_the_alternative.py`
— four parts, **31 gates**. Four banks at `spectra/r6925_*`; launchers at
`computations/beyond_the_wall/r6925_directions/`.* ⚠ **And the launcher's own episode is in its
README:** *the first version dropped its extra environment through a positional-argument bug and
thirty-six slices ran as plain `VISLEAF=0` spectra — reporting nothing wrong and reproducing the
banked spectra, which is the shape that gets banked as an answer. The fix is a smoke test that greps
the log for the marker the switch must print before the set goes out.*


# ⛭⛭⛭ r6929+cc66.44 — THE COMB'S RESOLUTION IS FOUR MULTIPOLES, AND THE SKY IS OUTSIDE THE FAMILY

***`r6929`'s order: the comb has been promoted to arbiter, so measure what it can actually decide.
Scan the assignment continuously — `VISLEAF` as a fraction — and report $\ell_1/\ell_A$ against the
sky's $0.7312$, the retained fraction and its $q$-slope, and $\mathrm dr_s/\mathrm d\chi$ against that
parameter; and say whether the comb's motion is the visibility peak relocating or the acoustic phase
changing.***

## ⛭⛭ EVERY READING IS LINEAR IN THE PARAMETER, AND THE WHOLE FAMILY IS FOUR MULTIPOLES WIDE

| $f$ | $\ell_1$ (sub-bin) | $\ell_1/\ell_A$ | $P_1/P_2$ | contrast | its $q$-slope | its s.e. | band residual |
|---|---|---|---|---|---|---|---|
| 0 | 221.953 | 0.73543 | 2.141 | 1.0584 | $+0.01042$ | 0.00284 | 0.0089 |
| 0.1 | 222.356 | 0.73677 | 2.128 | 1.0567 | $+0.00913$ | 0.00275 | 0.0086 |
| 0.25 | 222.968 | 0.73880 | 2.109 | 1.0541 | $+0.00727$ | 0.00392 | 0.0123 |
| 0.5 | 224.008 | 0.74224 | 2.078 | 1.0501 | $+0.00436$ | 0.00713 | 0.0223 |
| 0.75 | 225.073 | 0.74577 | 2.048 | 1.0463 | $+0.00178$ | 0.01063 | 0.0333 |
| 1 | 226.163 | 0.74938 | 2.017 | 1.0429 | $-0.00039$ | 0.01410 | 0.0441 |

*The sky: $\ell_1/\ell_A = 0.7312$, $P_1/P_2 = 2.217$.*

$\ell_1 = 221.93 + 4.21f$ to **three hundredths of a multipole**, so the family holds one number and the
scan is not hiding structure between its points. Its whole span is $0.01395$ in $\ell_1/\ell_A$ — **$4.2$
of the sky's one-multipole locating widths and $2.1$ of its two-multipole ones**.

⇒ ***The comb pins $f$ to about $\pm0.24$. It separates the family's ends and comes nowhere near fixing
the clock — which is the resolution the order asked to have stated before the arbiter decides anything.***

## ⛔ THE ORDER'S FIRST BRANCH IS HALF RIGHT, AND THE HALF THAT FAILS IS THE INTERESTING ONE

The order's first branch was *steep comb, shallow contrast*. The contrast's **level** is shallow as it
guessed — $1.75\sigma$ of its own band scatter across the family, against the comb's $4.21$ — but its
**$q$-slope is not**: $+0.01042 \to -0.00039$ is $3.80\sigma$ of its own fit error, the comb's
statistical equal.

⇒ ⛭ ***What separates them is not steepness but that the contrast's error GROWS with the parameter and
the comb's does not.*** The band residual runs $0.0089 \to 0.0441$ and the slope's standard error
$0.00284 \to 0.01410$, a factor five each, because moving `ETA_LS` moves $r_s(\mathrm{ETA\_LS})$ and a
band ratio of two oscillations no longer aligned in $q$ reads their phase mismatch — **`cc66.40`'s guard
firing a fourth time**, and the injection carries the same degradation, so it is the statistic's response
to the comb moving and not something in the plasma. *The comb's locating width is the same at both ends.*

## ⛭⛭⛭ AND THE DECIDING RESULT IS NOT ABOUT THE CHOICE: THE SKY'S VALUE IS NOT IN THE FAMILY

$0.7312$ sits at **$f = -0.304$** on the family's own straight line — on the far side of the stacking
clock, outside the two admissible assignments.

⇒ ***No interior fraction fits the comb better than the endpoint the instrument already uses***, so the
order's third branch does not arise and there is no fitted clock to declare (the corpus's
no-early-parameter claim is not asked to answer for one). The best point in the family is $f=0$. And
⇒ ***the residual first-peak disagreement cannot be absorbed by the clock assignment, because the
direction it would need is not admissible.***

⚑ And $P_1/P_2$, a **second** external referent, says the same thing independently: $2.141 \to 2.017$
against the sky's $2.217$, so both referents are best at $f=0$ and neither is being traded against the
other.

## ⚑ THE GUARD, ANSWERED AND SEPARATED THREE WAYS

The injection is a $\cos(k r_s)$ source with **no plasma dynamics in it**, which is what makes the
separation possible rather than a matter of assertion:

| the share of the comb's motion | $\mathrm d\ell_1/\ell_1$ | multipoles | share |
|---|---|---|---|
| the relocation through $r_s(\mathrm{ETA\_LS})$, $146.099 \to 145.241$ | $+0.591\%$ | $+1.311$ | **31%** |
| the visibility's re-weighting of the kernel (the injection, above that) | $+0.175\%$ | $+0.388$ | **9%** |
| the plasma's own acoustic phase (the real spectrum, above the injection) | $+1.131\%$ | $+2.510$ | **60%** |

⇒ ***So the comb's motion is NOT mostly the peak relocating: three fifths of it is the plasma responding
to the re-weighted optical depth.***

## ⚠ AND TWO OF `cc66.43`'s OWN NUMBERS WERE GRID-LIMITED

Read on the raw `LSTEP=8` grid the arm's first peak went $220 \to 228$ and $\ell_1/\ell_A$
$0.7290 \to 0.7555$. Those are **one bin step and its consequence**. Sub-bin — with the locator validated
first against the banked `LSTEP=1` spectrum, where it recovers the fine-grid $\ell_1$ to $0.004$ of a
multipole — the motion is $221.95 \to 226.16$ and $0.73543 \to 0.74938$: *the direction survives, the
magnitude was overstated $1.9\times$, and the **sign** of the arm's offset from the sky at $f=0$ flips —
from $0.7290$ (below) to $0.73543$ ($1.28$ multipoles above).*

⌗ The same caveat takes the FWHM with it: the width is a threshold crossing on the same $\eta$ grid,
$43.591 \to 43.952$ is exactly **one step** of it, and the value jitters non-monotonically across the
family — so the width's motion is not resolved, while `ETA_LS`'s (six steps, monotone) and $r_D$'s
($-4.1\%$, smooth) are. And $\mathrm dr_s/\mathrm d\chi$ reproduces `r6925`'s endpoints exactly
($0.396733 \to 0.396957$, $12.80\%$ lower becoming $12.75\%$) with $\ell_A$ not moving at all.

## ⛭ THE SWITCH GUARD IS NOW STANDING, WHICH 66 ASKED FOR RATHER THAN THE ONE-OFF

*Any switch whose effect is a bit-difference should print a marker and its launcher should fail if the
marker is absent.* The instrument prints a `__SWITCHES__` line naming every switch in its environment,
and **the inventory is read off its own source** rather than hand-maintained — `r3512`'s flag inventory
was wider than the code, and a list derived from the `os.environ` reads cannot drift from them, so
`VISLEAFF=1` is *absent* from the marker and fails the guard instead of running silently.
`switch_smoke.sh` asserts every assignment arrives (one import, no solver); the launcher smoke-tests every
distinct environment **before** the set goes out and checks **every slice's own log** after.

⚠ *What it cannot catch is stated where it is built: it proves the environment ARRIVED and that the name
is one the instrument reads. It does not prove the value reached the physics — that is the knob shadow
(`r4558`, `cc66.36`) and it takes a differential, not a print.*

⚑ **Receipt**: `P15_the_combs_resolution_is_four_multipoles_and_the_skys_own_value_lies_outside_the_family.py`
— six parts, **42 gates**, `GATES: ALL PASS`. Banks at `spectra/r6929_*`; launchers at
`computations/beyond_the_wall/r6929_directions/`. ⚠ **NOT CLAIMED**: a verdict on the two-rate
assignment — the row's question is whether it is right, and how well the comb constrains it is evidence
toward that, not the answer; that $f<0$ is admissible; a re-derivation of the sky's locating width, which
is P15's own; that the injected runs are spectra of this model; any mechanism beyond `cc66.42`'s; nothing
touches `prop:flat` and there is no refit.


# ⛭⛭⛭ r6941+cc66.45 — THE LOCATOR IS GOOD TO THREE HUNDREDTHS, AND THE FOURTH PEAK IS THE CONTROL'S TOO

***`r6941`'s order (headed `r6939`): the fourth peak is the only one of the four out of sample, so ⓶
establish the locator's own precision at each of the four peaks BEFORE reading any residual off them —
the stopping rule being that a locator worse than ten multipoles at $\ell_4$ means the residual is not
measured and the order ends there. ⓷ Then the three-way separation at every peak index. And the guard:
one systematic or two, and do not pick.***

## ⛭⛭ ⓶a THE STOPPING RULE DOES NOT FIRE, AND IT MISSES BY A FACTOR OF FOUR HUNDRED

The reported configuration re-run at `LSTEP=1 LMAXL=2000` — $1900$ multipoles against the reported $238$,
on both arms, 35 `KSLICE` slices — gives the reference the reported grid's locator is measured against:

| | $\ell_1$ | $\ell_2$ | $\ell_3$ | $\ell_4$ |
|---|---|---|---|---|
| control, fine | 220.351 | 536.291 | 814.331 | 1129.224 |
| control, `LSTEP=8` | 220.350 | 536.303 | 814.303 | 1129.206 |
| **error** | **0.0007** | **0.0126** | **0.0283** | **0.0176** |
| arm, fine | 221.956 | 536.105 | 815.398 | 1130.531 |
| arm, `LSTEP=8` | 221.953 | 536.114 | 815.381 | 1130.508 |
| **error** | **0.0035** | **0.0089** | **0.0167** | **0.0229** |

⇒ ***Two hundredths of a multipole at $\ell_4$ against a bar of ten.*** *And the extremum search is
insensitive to its own width — order $3$ through $40$ on the fine grid returns the same four peaks to
every printed digit — so the damping's flattening costs neither the search nor the refinement.*

## ⛔ ⓶b WHAT IS IMPRECISE IS THE PARABOLA'S WINDOW, AND IT IS A BIAS RATHER THAN A NOISE

Swept over `PO-47`'s admissible $W=15\ldots110$ the located peak moves $0.08/2.77/4.73/5.82$ on the arm
and $0.11/2.98/4.97/6.49$ on the control — **growing steeply with peak index**, because a wider fit on an
increasingly asymmetric, damping-suppressed hump pulls its apex down the envelope's slope.

⇒ *So at $\ell_4$ the window's bias is comparable to the residual being read there* — **but it displaces
the sky and both models the same way, which is exactly what the corpus's matched-procedure differencing
is for** and not a convenience. At the tight window $W=25$ the anchored parabola and the three-point
locator agree to $0.2$ of a multipole at every peak.

## ⛭⛭⛭ AND THE ORDER'S PATTERN IS TWO ARTEFACTS, NEITHER OF THEM PHYSICS

**First the quartet's provenance.** $222/538/818/1134$ is `sec:refit-bound`'s **line-of-sight** path;
every bank in this campaign is the **hierarchy** path, whose raw grid reading is $220/540/812/1132$. ⌗
*And at $\ell_3$ the two bracketing `LSTEP=8` bins differ by **four parts in ten thousand**, so which one
is called the peak is a coin flip: the paper quotes $820$ on this path, this run's locator picks $812$,
the sub-bin apex is $815.40$, and the fine grid's own maximum is at $815$.*

**Second, the differencing.**

| $n$ | arm | control | sky | arm − sky | control − sky | **arm − control** |
|---|---|---|---|---|---|---|
| 1 | 221.956 | 220.351 | 220.4 | $+1.556$ | $-0.049$ | **$+1.605$** |
| 2 | 536.105 | 536.291 | 537.7 | $-1.595$ | $-1.409$ | **$-0.186$** |
| 3 | 815.398 | 814.331 | 817.3 | $-1.902$ | $-2.969$ | **$+1.067$** |
| 4 | 1130.531 | 1129.224 | 1123.9 | $+6.631$ | $+5.324$ | **$+1.308$** |

⇒ ***Sub-bin, peaks two and three were never "on" — they are each about $1.7$ LOW — and peak four is
$6.6$ out rather than $10.1$.*** And ⇒ ***the CONTROL produces four fifths of the fourth peak's residual
($+5.32$ of $+6.63$), so what belongs to this construction is $+1.61/-0.19/+1.07/+1.31$: a near-constant
ONE multipole at all four peaks.***

**That is a constant $\Delta\ell$ — the FIRST of the order's three shapes** — fitting half again better
than the ruler's constant $\Delta\ell/\ell$ (rms $0.68$ against $1.02$, the ruler needing
$0.52/1.25/1.91/2.65$) and nothing like a driving error growing with $\ell$. ⇒ **So the pattern needs ONE
systematic and not two, and the "one-off, two-and-three-on, four-off" shape that fitted none of the three
candidates was the raw grid plus an undifferenced sky comparison.**

⌗ *And the sky cannot tell that one multipole from zero: `PO-47` measured its fourth peak at
$1121.9\pm2.36$ and put the arm-minus-control displacement at $0.83\sigma$ — every one of the four is
inside that spread, which is why this is reported as a shape and not as a disagreement.*

## ⚑ ⓷ THE SEPARATION AT EVERY PEAK INDEX, AND $\ell_1$ IS THE OUTLIER

| $n$ | total motion | relocation | visibility | plasma |
|---|---|---|---|---|
| 1 | $+1.893\%$ | $31.2\%$ | $9.2\%$ | $59.6\%$ |
| 2 | $+0.628\%$ | $94.1\%$ | $26.4\%$ | $-20.5\%$ |
| 3 | $+0.709\%$ | $83.4\%$ | $22.7\%$ | $-6.0\%$ |
| 4 | $+0.662\%$ | $89.3\%$ | $23.5\%$ | $-12.8\%$ |

***At $\ell_2$ through $\ell_4$ the motion is almost entirely geometric and the plasma's phase partially
CANCELS it, where at $\ell_1$ the plasma dominates and adds.*** By the order's reading, fixed in advance:
the plasma's share does not grow with $n$, so the residual is not in the driving; the relocation share
does grow, which points at the ruler. ⚠ **But the third reading is the one that applies: the shares are
not flat and the residual is not reached** — the family's motion is $+0.6$ to $+0.7$ per cent with one
sign at every peak while the sky residual alternates, *so the decomposition does not cover the four-peak
pattern, which is a statement about the guard's coverage and not a failure of the run.*

⌗ *The motions are resolved: fine against coarse they agree to $0.02$ of a multipole at every peak, so
the shares are the spectra's and not the grid's.*

⚑ **Receipt**: `P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks_residual_is_the_controls_too.py`
— four parts, **24 gates**, `GATES: ALL PASS`. Banks at `spectra/r6941_*`; launchers at
`computations/beyond_the_wall/r6941_directions/`. ⌗ **No corpus edits, as the order directs** — the
paper-side consequences go to 66 in `FOR_66.md`. ⚠ **NOT CLAIMED**: a mechanism for the one-multipole
offset; a re-derivation of the sky's locating spread, which is `PO-47`'s; that the window convention is
an error rather than a convention; that peak four is uninteresting — it is the largest of the four and
four fifths of it is the control's; no verdict on the two-rate assignment; no refit; nothing touches
`prop:flat` or the clock family.


# ⛭⛭⛭ r6955+cc66.46 — THE EXCESS IS SYMMETRIC, AND THE TROUGHS ARE WHERE THE SKY MEASURES IT BEST

***`r6955`'s order: four routes are eliminated, so what is left is the $\chi^2$ — trough-dominated in the
whitened residual. 66's reading, stated as its own: the trough depths mix the two clocks in a way
$\theta_D/\theta_*$ does not. ⓶ᵃ Locate the excess first (if it is in the peaks, stop); ⓶ᵇ then the clock
sensitivity of whichever carries it; ⓶ᶜ and the sky's own spread on it, the way `PO-47` did.***

⌗ **Path provenance, in the receipt's header as the order now requires.** Every model number is the
**hierarchy** path — `cc66_r185_verify_*`, the `LSTEP=1` references `r6941_fine_*`, and the `VISLEAF`
family `r6929_scan_cr` / `r6941_fine_cr_visleaf`. `sec:refit-bound`'s quartet is the **line-of-sight**
path's and is not read at all — searched for by grepping the receipt for each of the four values and for
every line-of-sight bank name, none of which occurs in its code. The sky is `plik_lite` TT through the likelihood's own
binning, with the models binned identically before any comparison.

## ⛭⛭ ⓶ᵃ THE EXCESS IS SYMMETRIC ABOUT THE ENVELOPE

Splitting the band variance of the envelope-normalised oscillation at its own zero — a decomposition, the
two parts adding to the whole to machine precision:

| | mean over the seven bands |
|---|---|
| total contrast | $1.0546$ |
| **peak side** | **$1.0668$** |
| **trough side** | **$1.0561$** |

And at the literal extrema (six of each, fine grid) the arm exceeds the control by **$5.7$ per cent at
the maxima against $5.3$ at the minima**.

⇒ ***It is an AMPLITUDE excess, carried equally by peak heights and trough depths.*** *So $\Delta$'s
trough dominance is a statement about the whitened residual and does not transfer to the contrast's own
decomposition — which the order explicitly declined to assume, and the answer is that they disagree.* ⚠
*The stop condition does not fire either: the excess is not in the peaks, so the row is not pushed back
onto the driving.*

## ⛔ ⓶ᵇ THE DEPTHS ARE THREE TIMES THE MORE CLOCK-RESPONSIVE — AND THE DISCRIMINANT MOVES MORE STILL

| across the `VISLEAF` family | $f=0$ | $f=1$ | change |
|---|---|---|---|
| mean peak height | $0.25070$ | $0.24878$ | $-0.77\%$ |
| mean trough depth | $0.25733$ | $0.25070$ | $\mathbf{-2.58\%}$ |
| $\theta_D/\theta_* = r_D/r_s$ | $0.051216$ | $0.049127$ | $\mathbf{-4.08\%}$ |

⇒ *The depths are $3.4\times$ the more responsive of the two observables — **that half of the reading
holds**. But $\theta_D/\theta_*$ moves more than either, because $r_D$ is itself `Jac`-weighted under
`LEAFSCALES` and the $\tau$ re-weighting moves it directly.* ⇒ ***The paper's discriminant of principle
is the MOST sensitive of the three, not the insensitive one, and by the order's own rule — both move
together — the depths are not a new handle on the clock.*** *The endpoints reproduce on the `LSTEP=1`
grid, so the response is the spectra's and not the grid's.*

## ⛭⛭⛭ ⓶ᶜ AND YET THE TROUGHS ARE WHERE IT BECOMES OBSERVABLE: THE SKY MEASURES DEPTHS TWICE AS WELL

Same data, same likelihood binning, same anchored locator, `COV_TT` propagated by Monte Carlo (two seeds,
$600$ realisations each, stable to $5\times10^{-4}$):

| | control | arm | sky | arm − control | the sky's spread | in sigma |
|---|---|---|---|---|---|---|
| **trough depth** | $0.28007$ | $0.29071$ | $0.28038$ | $+0.01064$ | $\mathbf{0.00588}$ | **$+1.81$** |
| **peak height** | $0.27715$ | $0.28743$ | $0.28382$ | $+0.01029$ | $\mathbf{0.01135}$ | **$+0.91$** |

⇒ ***The excess is the same SIZE in both, and reads twice as significantly in the depths, because the sky
measures depths twice as precisely.*** And ⇒ ***the control lands on the sky's trough depths at
$-0.05\sigma$ while the arm sits $+1.76$ above: the first statistic in this sector whose residual is NOT
shared with the control*** — against the fourth peak, where arm-minus-control was $0.83\sigma$ and both
models sat high of the sky.

⇒ **So the order's conclusion stands and its argument does not.** *The troughs are where the assignment
becomes observable because of how well the sky measures them, not because of how they mix the clocks.*

## ⚑ THE GUARDS THE ORDER ASKED FOR

* ***The window bias does not exist for this statistic.*** The anchored depth is identical over
  $W=20\ldots70$ on the sky and on both arms, because it reads a **value** at a located extremum rather
  than the **location** of one — where `cc66.45`'s parabola apex drifted six multipoles at $\ell_4$.
* ⚠ ***But `PO-47`'s trap reproduces exactly, on depths instead of positions***: a free extremum search
  under noise returns $0.0369$ against the anchored $0.00588$, six times worse, because it latches onto
  noise minima. **The anchoring is necessary and not a convenience**, and that is gated.
* ⌗ *The one real systematic is the envelope's abscissa: the sky's depth runs $0.2790\to0.2830$ as the
  $\ell_A$ that sets it goes $298\to305$, about a third of a sigma, reported rather than minimised.*

⚑ **Receipt**: `P15_the_contrast_excess_is_symmetric_about_the_envelope_and_the_troughs_are_where_the_sky_measures_it_best.py`
— four parts, **21 gates**, `GATES: ALL PASS`. ⚑ *And this revision cost no solver time: it is analysis
on the banks `cc66.44` and `cc66.45` already built, which is why all three parts and all three guards fit
in one revision.* ⚠ **NOT CLAIMED**: that $1.8\sigma$ is a detection; a mechanism for the amplitude
excess; a re-derivation of `PO-47`'s spreads; that the depths discriminate the clock — they do not; no
verdict on the two-rate assignment; no refit; nothing touches `prop:flat`; no corpus edits.

## `cc66.47` (`r6959`) — THE NORMALISATION ACROSS THE VISIBILITY: A THIRD OF THE EXCESS, AND PEAK-WEIGHTED

*Path: **hierarchy** (`LOS=1 HIER=1`) throughout — `_project`, where `SRCETA` and `SRCTAPER` live, is
reached from `hier_run` and nowhere else. Banks `spectra/r6959_*`; receipt
`P15_the_windows_phase_spread_is_nearly_equal_because_the_visibility_widens_as_the_leaf_clock_slows.py`,
45 gates.*

**⓵ᵃ THE FUNCTION.** The source's weight across the window, band by band in $q$, with $r_{s,\rm leaf}$ as
its abscissa. Spread in the phase variable: $0.06523$ of $r_s$ on the control, $0.06424$ on the arm — the
arm narrower by $1.5$ per cent, $1.1$–$2.0$ per cent by band.

| | control | arm |
|---|---|---|
| visibility FWHM in $\eta$ | $38.04$ | $\mathbf{43.59}$ ($+14.6\%$) |
| $\mathrm d r_{s,\rm leaf}/\mathrm d\eta$ over $\pm3$ FWHM | $0.45572$ | $\mathbf{0.39334}$ ($-13.7\%$) |
| `Jac` across the window | $1.0000$ | $0.789$–$0.913$ |
| product, which is what a smearing reads | $1$ | $\mathbf{0.9890}$ |

⇒ **The two-rate structure reaches the window and then very nearly cancels inside it**, because the
visibility widens by almost the factor the leaf clock slows by.

**⓵ᵇ THE PREDICTION, PRE-REGISTERED, AND WHAT THE RUNS DID TO IT.** The exact characteristic function of
the phase under the measured weight gives $\mathcal D_{\rm cr}/\mathcal D_{\rm lcdm}=1.00078\to1.01654$
against a measured excess of $1.0215\to1.0762$. R5 (sign) survives; R2 (size) fires at $0.223$ of the
$[\tfrac12,2]$ bar; R1 (shape) fires because the measured excess extrapolates to $1.0400$ at $q=0$ where
a characteristic function is identically $1$.

⚠ **And R3's bracket was wrong in direction, which is mine.** `PREDICTION.md` argued the contrast responds
*between* $f$ and $f^2$; measured it responds $2.3$ to $26$ times **more**, at both coefficients and in
every band, and the condition passed only because its tolerance was written multiplicatively on $f$
instead of on $f-1$.

**THREE WIRINGS, THE FIRST TWO NOT THE OPERATION.** (1) The taper on the whole source cuts the ISW's
$\eta$-integral to $0.656$ and $0.238$ of itself and moves $\ell_1$ by $7.7$ and $27.3$ multipoles.
(2) Tapering only the visibility-carried source fixes that, and still outran the prediction by three.
(3) Holding the window's total weight fixed lands on (2) to parts in ten thousand — **so that second
diagnosis of mine was wrong too**, and the over-response is the contrast statistic's own sensitivity to
the window's spread.

**THE SIZE, FROM THE INSTRUMENT'S OWN RESPONSE.** Two coefficients fix $\ln R=c_1\alpha+c_2\alpha^2$ per
band; inverted:

| $q$ | $1.20$ | $1.90$ | $2.60$ | $3.30$ | $4.00$ | $4.70$ | $5.40$ |
|---|---|---|---|---|---|---|---|
| arm's own narrowing | $1.09\%$ | $1.53\%$ | $1.51\%$ | $1.89\%$ | $1.81\%$ | $1.97\%$ | $1.95\%$ |
| narrowing for ALL of it | $1.24\%$ | $5.58\%$ | $3.59\%$ | $5.05\%$ | $7.16\%$ | $4.90\%$ | $4.01\%$ |
| **share the arm's narrowing delivers** | $(88\%)$ | $\mathbf{25\%}$ | $\mathbf{40\%}$ | $\mathbf{36\%}$ | $\mathbf{23\%}$ | $\mathbf{37\%}$ | $\mathbf{44\%}$ |
| **the direct swap closes** | $(124\%)$ | $\mathbf{33\%}$ | $\mathbf{38\%}$ | $\mathbf{20\%}$ | $\mathbf{22\%}$ | $\mathbf{23\%}$ | $\mathbf{21\%}$ |

⇒ **Two independent routes agree on about a third above $q=1.9$**, and the narrowing for all of it is
$4.5$ per cent against the arm's $1.7$ — a factor $2.7$. *The lowest band is where the inversion cannot
be trusted and the swap overshoots, taking the excess below unity; that is reported rather than averaged
away.*

**⓵ᶜ R4, AND THE REFUTATION FROM `cc66.46`.** The arm-sized swap delivers $81$ per cent of the arm's
peak-height excess and $14$ per cent of its trough-depth excess — a $5.7$-fold asymmetry — where
`cc66.46` measured the excess **symmetric** about the envelope. ⇒ **A peak-weighted channel cannot carry
a symmetric excess alone, whatever its size**, and that argument uses no size estimate at all. The taper
that would deliver the whole excess moves $\ell_1$ by $18.5$ multipoles and the heights by $45$ per cent;
the arm-sized one overshoots $\ell_1$ past the arm's own value ($+2.83$ against $+1.61$) while $\ell_2$,
$\ell_3$ and $\ell_4$ stay inside the sky's locating widths.

**THE TERM MIX, REPORTED AND NOT SWAPPED.** The same profiles show the arm holding more of its window's
power in the monopole in every band ($0.1837\to0.2171$ at $q=1.2$, $0.5320\to0.5875$ at $q=5.4$) and
correspondingly less in the Doppler, with the ISW under half a per cent of the window's power on both
arms. *That is a normalisation difference which is not a smearing and is not required to vanish at long
wavelength — where R1's $q$-independent offset could come from. Measured here, tested nowhere.*

## `cc66.48` (`r6975`) — THE TERM MIX HAS THE OFFSET'S SHAPE AND OVER-DELIVERS ITS SIZE; THE CHANNELS DO NOT ADD

*Path: **hierarchy** throughout. Banks `spectra/r6975_mix{,b}_lcdm.npz` plus `r6959_*`; receipt
`P15_the_term_mix_has_the_shape_the_offset_needs_and_over_delivers_its_size.py`, 28 gates.*

**⓵ THE REMAINDER.** Measured excess ÷ what the window channel delivers at the arm's size: $1.0184$ at
$q=0$ (**46 % of R1's offset**), $123$ % of the measured $q^{2}$ slope, anchored ratio $0.49$ against the
window channel's $12.44$.

**⓶ THE CLASS ARITHMETIC — AND THE STATISTIC'S OWN BASELINE.** Each class applied to the control's
spectrum and re-read with the same envelope and locator:

| class | heights | depths | ratio |
|---|---|---|---|
| amplitude (oscillation scaled about the envelope) | $+7.53\%$ | $+3.84\%$ | $\mathbf{1.96}$ |
| envelope (smooth part scaled at fixed oscillation) | $+7.93\%$ | $+4.05\%$ | $1.96$ |
| loading (a smooth positive component removed) | $+2.21\%$ | $+3.51\%$ | $0.63$ |
| smearing (Gaussian in $\ell$, nine multipoles) | $+5.55\%$ | $-1.05\%$ | $-5.28$ |

⇒ **A symmetric operation reads $1.95$ here, not $1$** — stable across a fivefold range of sizes, because
the running-mean envelope is recomputed and shifts the oscillation upward by a constant. ⛭ *So the
anchored reading **confirms** `cc66.46`'s variance split: $2.20$ against $1.96$ is twelve per cent. My
own note that the two statistics disagreed is retracted, in the pre-registration, before the runs landed.*

**⓷ THE TERM-MIX SWAP.** `DPSRC` was already wired to the hierarchy path (`r6889+cc66.36`), and the
coefficient giving the control the arm's monopole fraction is solved from the profiles: $0.860$–$0.897$
across the seven bands — **one constant to two per cent**.

| $q$ | $1.20$ | $1.90$ | $2.60$ | $3.30$ | $4.00$ | $4.70$ | $5.40$ |
|---|---|---|---|---|---|---|---|
| `DPSRC=0.8794` | $1.0595$ | $1.1088$ | $1.0780$ | $1.0821$ | $1.0905$ | $1.0724$ | $1.0911$ |
| `DPSRC=0.60` | $1.2078$ | $1.4010$ | $1.2759$ | $1.2995$ | $1.3331$ | $1.2658$ | $1.3394$ |
| measured excess | $1.0215$ | $1.0574$ | $1.0519$ | $1.0606$ | $1.0748$ | $1.0659$ | $1.0762$ |
| **over-delivery** | $2.77\times$ | $1.90\times$ | $1.50\times$ | $1.35\times$ | $1.21\times$ | $1.10\times$ | $1.20\times$ |

* ✔ **T1 sign** — the contrast rises in every band.
* ⛭⛭ **T2 shape — the finding.** The response is **$q$-independent**: intercept $1.0805$ at $q=0$, slope
  worth three per cent of it. ***The first channel measured with the signature the offset needs***, where
  a smearing's characteristic function is identically one.
* ⛔ **T3′ weighting fires** — $2.23$ and $2.21$, peak-weighted at the symmetric baseline, where the
  remainder it was to be is $0.49$. **The term mix is not the remainder.**
* ⛔ **T4 comb fires, wrong way** — $\ell_1$ $-1.04$, $\ell_2$ $-1.79$, both outside the sky's widths,
  where the arm sits at $+1.61$.

⛔⛭⛭ **THE CONSEQUENCE.** Window channel $1.72\%$ band-mean, term mix $8.32\%$, measured $5.84\%$ ⇒
**their sum is $1.72\times$ what is measured**, so the two cannot both be present at their measured sizes
and simply compose. ***And ⓵'s remainder is a ratio of two responses, so it is a construct of that
composition rule and not a residual channel*** — which is why its $0.49$ and the swap's $2.23$ are not in
conflict.

⚠ **AND MY ⓶ IDENTIFICATION IS REFUTED BY ⓷.** I argued the Doppler fills the oscillation and that
removing it should read as the loading class near $0.6$; it reads $2.23$. The profiles say why: the
Doppler's band-to-band power tracks the monopole's at correlation $0.95$, so it is an **oscillating** term
in quadrature, not a smooth additive one, and removing it is nearly a pure amplitude change.

## `cc66.49` (`r6983`) — THE COMPOSITION RULE IS MEASURED: MULTIPLICATIVE, NOT QUADRATURE, AND THE PAIR IS FLAT WHERE THE EXCESS GROWS

*Path: **hierarchy** throughout. Bank `spectra/r6983_joint_lcdm.npz` plus `r6959_nswap_*`, `r6975_mix_*`
and `r6941_fine_*`; receipt
`P15_the_two_channels_compose_multiplicatively_and_the_pair_is_flat_where_the_excess_grows.py`,
**22 gates**. Both knobs on ONE spectrum at the sizes their own revisions solved; **neither re-chosen**.*

**⓵ T-SIZE.** Joint within the pre-registered $0.005$ of the product in **7 of 7** bands, of the sum in
**7 of 7**, of **quadrature in 0 of 7** (worst miss $0.018$, three and a half times the bar). *Product
and sum were declared inseparable here in advance — they differ by at most $0.0016$ — and they are not
separated.* ⛭ The pair is slightly **sub**-multiplicative and consistently so: $0.971$ of the product,
$0.985$ of the sum, below both in every band and above quadrature in every band.

**⓶ T-WEIGHT**, the sharpest of the four. Predicted $2.83$ from the two channels' separate height and
depth changes, bracket $[2.2, 3.6]$; the joint reads **$2.80$** — one per cent from a number computed
before the run, on an axis where quadrature predicts nothing at all.

**⓷ T-COMB.** $\ell_1$ predicted $+1.79$, bracket $[+1.0, +2.6]$, measured **$+1.41$** — below the
additive centre, the same mild sub-additivity the sizes show.

**⓸ T-INTERCEPT.** Joint intercept against $q^{2}$ = **$1.0993$**, against a multiplicative $1.1035$
with nothing fitted ($0.0042$ away), a sum's $1.1019$ ($0.0026$), quadrature's $1.0839$ ($0.0154$,
outside). ⛭⛭ And the joint response is **the flattest thing this sector has measured**: $0.004$ of its
intercept, against the term mix's $0.031$ and the measured excess's $0.442$.

⛔⛭⛭ **THE CONSEQUENCE, IN THREE PARTS, ONE OF THEM AGAINST MY OWN PREVIOUS REVISION.**
* ✔ **Confirmed, by direct measurement rather than by adding two numbers.** `cc66.48` put the pair at
  $1.72$ times the measured excess from the two channels separately; composing them in one spectrum
  reads **$1.70$**. *The arithmetic was right to one per cent.*
* ⛔ **RETRACTED: `cc66.48`'s inference.** That revision argued the shares sum to more than the excess,
  therefore the channels do not compose as assumed, therefore a remainder got by DIVIDING one response
  into the excess is an artefact of a wrong rule. ***The rule is now measured and it IS the assumed
  one.*** Dividing is the right operation, so the remainder is a well-defined object and not an
  artefact. *The over-delivery was evidence about the SIZES, not about the RULE — and reading it as
  evidence about the rule is the error.*
* ⛭⛭ **And the obstruction that survives is a SHAPE, which no coefficient on either knob can remove.**
  The pair over-delivers $3.87$ times in the longest-wavelength band and $1.38$ in the shortest, because
  it is flat in $q$ where the measured excess grows. ⇒ *Scale it to the offset at $q=0$ and it is short
  at high $q$; scale it to high $q$ and it is an order too large at low $q$.* **That is a stronger
  negative than `cc66.48`'s, and it is available only because the rule was measured rather than
  assumed.**

⌗ **An operational note that is part of the provenance.** The joint spectrum is a sum of **35 disjoint
mode slices**. This container is reclaimed faster than a large slice completes, so slices above mode
index $750$ restarted from zero at every churn and would never have landed; the run was re-sliced twice
midway, finally at $50$ modes, and the launcher became gap-driven. ⇒ **The bank's check moved with it:
it reconstructs each slice's span from its filename and asserts the spans tile $[0, 2547)$ with no gap
and no overlap, rather than asserting a fixed step — a check on the SUM instead of on the bookkeeping
convention, which is what makes re-slicing midway verifiable rather than trusted.**

## `cc66.50` (`r6993`) — THE EXCESS DECELERATES, AND THE FIRST POSITIVE SEARCH RETURNS EMPTY

*Path: **hierarchy** throughout. Banks `r6941_fine_*`, `r6959_eta_*`, `r6959_nswap_*`, `r6975_mix_*`,
`r6983_joint_*`; receipt
`P15_the_excess_decelerates_and_nothing_measured_in_this_arm_carries_its_wavenumber_dependence.py`,
**22 gates**. ⛔ Nothing is RUN: every number is read from banks on disk, which is the order's ⓸.*

**⓷ FIRST, AND THE INVERSION IS THE METHOD.** ⓷ asks whether the statistic's $q$-dependence belongs to
the effect or the anchoring — a question about the INSTRUMENT, whose answer is what ⓵'s pre-registration
must write its tolerances on. ✔ Six injected forms, two with a **scale** in them, recover to $1.3$ per
cent. ⚠ But the per-band bias swings about one per cent and the six forms agree on it seven times more
closely, so it is fixed: ***a constant contrast reads as a wobble***, and band ordering at the per-cent
level is the instrument. ⛔ **The median envelope is excluded with its mechanism** — it reads $1.49$
against the mean's $0.44$ and would have been the headline, but it does not move with its own window,
because at high $q$ the running median collapses onto the curve itself ($3.6$ per cent from it against
the mean's $14$). ✔ The rise survives the mean envelope at $0.44/0.44/0.40$. ⇒ **The rise is real; the
wobble is not.**

**⓵ AND THE SHAPE EXCLUDES THE PARAMETRISATION THIS SECTOR QUOTES.** At the pre-registered
$\sigma = 0.013$: ⛔ **a rise linear in $q^{2}$ is EXCLUDED** at $\chi^{2}/\nu = 4.66$, the only one of
six — ***and it is the form `cc66.47`, `cc66.48` and `cc66.49` all quote their variation statistic in***.
The excess **decelerates**. The concave family all fit and **none is preferred** ($\Delta\chi^{2}=0.43$
against a bar of $4$); both pre-registered non-separations held; **no scale is resolved**, and the rule as
written caught this seat's own code, which had asked only that the central value be inside. ⚠ And the rise
is a **preference, not an exclusion of flatness** — $\Delta\chi^{2}=6.0$–$10.4$ over a constant whose own
$\chi^{2}/\nu=2.03$ is under the exclusion bar.

**⓶ AND THE FILTER'S FIRST APPLICATION RETURNS EMPTY.** The target's departure grows by $G=3.55$ with
negative curvature. Every candidate already measured fails the growth tooth: six source terms
($0.54$–$1.00$), the dipole-to-monopole ratio ($1.08$), and all three channels — window $0.55$, term mix
$1.53$, the pair $1.27$. ⚠ And the order's named candidate **disagrees with the register**: recorded as
two per cent above the control and rising, it reads fourteen per cent **below** and flat on the hierarchy
path. *Which quantity the register measured is owed before that candidate is closed.*

⇒ ***The useful form of the empty result: the carrier is not among the things this sector has already
measured.*** *That is a statement about the list searched, and the list is now written down with a number
beside each entry, which is what makes the next one cheap.*

## `cc66.51` (`r6997`) — TWO QUANTITIES, NOT A CONTRADICTION; AND THE PROJECTION'S UNMEASURED WIDTH

*Path: **hierarchy** throughout. Banks `r6897_fields`, `r6959_eta_*`, `r6941_fine_*`; receipt
`P15_the_two_readings_are_different_quantities_and_the_projection_width_is_the_unmeasured_one.py`,
**15 gates**. ⛔ Nothing RUN — the order's ⓸.*

**⓵ THE SIGN IS NOT THE RANGE, IT IS THE QUANTITY.** The register's reading is reproduced from its own
bank and estimator at $+2.06$ per cent over its own range, and is still $+0.95$ over the part of
`cc66.50`'s range it reaches — where `cc66.50`'s reads $-11.58$. They differ in **what is ratioed** (the
oscillation amplitude of each source field against the integrated band power, which keeps the smooth
part), **which fields**, and **over what range**. ⛔ **And which one is needed is the register's, which
makes `cc66.50`'s filter row this seat's own error**: what fills a trough is an oscillating amplitude,
and so is what the contrast statistic measures.

**⓶ SO THE SECOND TOOTH IS USED.** On the range where the right quantity can be measured the candidate's
departure runs $-0.0006 \to +0.0166$ and **decelerates**, curvature $-0.0037$ against the target's
$-0.0029$. ***It passes both teeth where it can be tested, reversing `cc66.50` on this seat's error
rather than on new data.*** ⚠ The growth statistic is **undefined** there, not large — the departure
crosses zero, and the arithmetic's $-26$ would have read as a spectacular pass.

⛔ **AND THE FILTER STILL CANNOT CLOSE IT.** The right quantity bottoms out at $q = 2.0$ — stable to a
tenth of a per cent across four window widths, so sound and simply not reaching — while the target grows
$3.55$-fold over the full range and only $1.47$-fold over the shared one. ⇒ ***The target's growth is
concentrated exactly where the only quantity that could carry it cannot be measured.*** What would close
it is a different estimator below $q=2$, not a longer run of this one.

**⓷ AND THE ENUMERATION OF THE UNMEASURED.** ⛭ A whole class is settled by **structure**: every two-rate
clock quantity — leaf clock, ruler, Jacobian, visibility, optical depth — is stored against conformal
time alone, and a function of $\eta$ has the same value at every wavenumber, so it **cannot carry it**,
no run needed. ⛭⛭⛭ **And the projection holds a width nobody has imposed**: the acoustic phase varies
across the window by $k\times$ the width in the **leaf** clock — what `cc66.47` acted on — while the
projection smears by $k\times$ the width in **conformal time**, the Bessel argument being
$k(\eta_0-\eta)$. One object in a one-rate cosmology; two here. ⇒ ***The arm's window is $6.5$ per cent
wider in conformal time and $0.8$ per cent narrower in the leaf horizon — a ratio $7.3$ per cent
different from the control's, and the projection width has never been imposed.***

## `cc66.52` (`r6999`) — THE TWO WIDTHS DIFFER BY THE JACOBIAN ALONE, WHICH MAKES THE DIFFERENCE A CR PREDICTION; AND THE CHANNEL IT OPENS IS A QUARTER OF THE EXCESS

*Path: **hierarchy** throughout. Banks `r6959_eta_*`, `r6941_fine_*`; receipt
`P15_the_two_projection_widths_differ_by_the_jacobian_alone_and_the_channel_that_opens_is_a_quarter_of_the_excess.py`,
**17 gates**; pre-registration `r6999_directions/PREDICTION.md`. ⛔ Nothing SOLVED — the projection
kernel is evaluated directly with `scipy.special.spherical_jn` at the instrument's own $\ell$, $k$,
$\eta_0$.*

**⛭⛭⛭ ⓷ FORCED, AND FORCED BY ONE OBJECT — reported first because the order says it is worth more than
the contrast result.** The instrument keeps two sound horizons on one integrand and two rates, so
$d(r_{s,\rm leaf})/d(r_{s,\rm stack}) = \mathrm{Jac}$ pointwise — checked across the window to **one part
in a million** on the arm and exactly on the control, where $\mathrm{Jac}\equiv 1$ by the rate identity.

- **ⓐ On the RULER clock the two arms are the same instrument.** The window's conformal width against
  its width in $r_{s,\rm stack}$ agrees between the arms to $0.3$ per cent on both core width
  definitions. *The visibility is laid down in $\eta$ by Thomson scattering on the physical background,
  which is the same physics on both arms.*
- **ⓑ On the LEAF clock it is $+14.5$ per cent, and the whole of that is $\mathrm{Jac}$** — Jac share
  $1.1484$ against a leaf ratio $1.1446$; the arm's own leaf-to-ruler width ratio equals
  $\langle\mathrm{Jac}\rangle = 0.8744$ to $0.4$ per cent.
- **ⓒ $\mathrm{Jac} = H_{\rm phys}/H_{\rm leaf}$ is not a knob** — fixed by the background solution once
  the arm is specified, no free coefficient, identically $1$ on any one-rate cosmology. ⇒ ***The two
  widths standing in a different ratio is a prediction of the two-rate assignment and not an artefact of
  how this instrument builds its window. The ruler clock is what proves it.***

⚠ **AND THE SIZE IS DEFINITION-DEPENDENT WHILE THE ATTRIBUTION IS NOT.** Under one measure — the
visibility as a density over $\eta$ — RMS gives $+7.3$ per cent (`cc66.51`'s figure) while FWHM and the
characteristic function's half-fall give $+14.5$ and agree with each other to better than a hundredth of
a per cent. *The window has long tails; RMS weights them; neither the projection nor the phase sweep
responds to them.* ⇒ **Quote the prediction on a core width, with the definition named.**

**⛭⛭ ⓶ THE FILTER, APPLIED IN THE INSTRUMENT'S OWN KERNEL.** The order's operation done analytically on
the control's own projection: hold the source phase $\cos(k r_{s,\rm leaf})$ and stretch only the Bessel
argument by the measured $s = 1.135$.

⛔ **And it corrects its own first pass, by a factor of fifteen and in sign.** That pass used the
plane-wave proxy $\lvert\int g\,e^{-ik\eta}\rvert$, on the reading that the Bessel argument advances at
rate $k$. **It does not**: $j_\ell(x)$ near its turning point $x\sim\ell$ — *where the entire window
sits, $kD_M\sim\ell$ being what the projection IS* — oscillates at local rate $\sqrt{1-\ell^2/x^2}$,
which vanishes there. The proxy gives $-29.7$ per cent at the top band; the kernel gives $+1.96$.

⚠ **And the sign is not determined on paper, because a stretch needs a fixed point.** Mean-anchored the
departure runs $+0.0034 \to +0.0196$; peak-anchored $-0.0034 \to +0.0016$, crossing zero, where $G$ is
**undefined**. *A stretch about the wrong point is a stretch plus a displacement, and a displacement of
the window moves the comb rather than the contrast.*

⛔ **THE VERDICT.** Curvature $+0.00016$ (mean) and $+0.00037$ (peak) against the target's $-0.00327$:
**it accelerates where the target decelerates, so it fails the committed second tooth under both
anchorings** — and at the top band it delivers $+1.96$ per cent against the $+7.62$ the measurement
needs. ⇒ ***Not the carrier. Not excluded as a contributor.***

⚠ **AND THE FILTER ITSELF NEEDED A THIRD TOOTH.** The superseded plane-wave numbers run
$-0.033 \to -0.297$: $G = 8.93$, curvature $-0.0014$ — ***passing both pre-registered teeth while moving
the contrast the wrong way in every band.*** $G$ is a ratio of a departure to a departure and is blind to
their common sign. ⇒ **SIGN is now the first tooth, and $G$ is read only after it.** *Second revision
running in which this statistic returned a number outside its domain.*

**⛔ ⓵ THE RUN IS NOT CONSTRUCTIBLE, WHICH FOLLOWS FROM ⓷ AND NOT FROM EFFORT.** *"Give the control arm
this arm's conformal width at the same leaf width"* is, by ⓐ–ⓒ, exactly *"give the control arm this
arm's $\mathrm{Jac}$"* — and a control with $\mathrm{Jac}\neq1$ is not a control. **There is no knob for
the projection width and the instrument is right not to have one.** *Reported rather than substituted
for.* ⌗ The pre-registration is written anyway and carries all four outcomes including the null, and
states which teeth were committed at `r6993` before the measurement and which two are added now.

**⌗ ⓸ THE SUB-PERIOD ESTIMATOR, SAID AND NOT BUILT.** The acoustic period in $q$ is **known** and equal
to $2$, so a fit of $A\cos(\pi q + \varphi)$ with the period **held** has two free parameters per $q$
rather than an amplitude read off a window, and needs only a fraction of a period of support — which is
what would reach below $q=2$. ⚠ **Its cost is that the held period must be right**: an error of a few
per cent leaks into $A$ as a slow drift, which is exactly the $q$-dependence being measured. ⇒ *It would
have to be validated against the window estimator on $[2.6,\,5.4]$, where both work, before anything it
says below $q=2$ is read.*

## `cc66.53` (`r7001`) — THE BELOW-FLOOR ESTIMATOR REACHES A BAND NOTHING HAS REACHED, AND THE TOOTH THAT WOULD DECIDE CANNOT BE APPLIED

*Path: **hierarchy** throughout. Banks `r6897_fields`, `r6941_fine_*`, `r6959_eta_*`; receipt
`P15_the_held_period_estimator_reaches_below_the_floor_and_the_tooth_that_would_decide_cannot_be_applied.py`,
**23 gates**; pre-registration `r7001_directions/PREDICTION.md`, both nulls tabled. ⛔ Nothing SOLVED.*

**⛭⛭ ⓵ THE ESTIMATOR, AND THE FIRST THING IT FOUND IS THAT THE PERIOD IS NOT THE PERIOD.** The acoustic
period in $q = k r_s/\pi$ is $2$ **by construction**, and it is not $2$ in the fields. Read off the drift
of the recovered phase and iterated to self-consistency: **monopole $1.9636$, dipole $1.9909$** on the
control; $1.9585$ and $1.9896$ on the arm. ⇒ ***A two per cent error, and a different one for the two
fields*** — exactly the failure the order asked to be measured rather than noted. **So the held period is
measured per field and per arm**, its own uncertainty taken from disjoint sub-ranges: $1.3$ per cent.

**⛔ VALIDATION FIRST, WHICH WAS THE ORDER AND IS THE STANDING GUARD MADE PROCEDURAL.** Against the
window estimator on the same quantity and the same fields, the **means agree** — $1.4987$ (window at
`half` $=2$, where it is sound) against $1.4911$ (held at `half` $=0.5$), $0.5$ per cent apart.

⚠ **And the window estimator does not survive its own width while the held one does.** Its ripple runs
$0.7 \to 11.6$ per cent as it narrows from `half` $=2$ to `half` $=0.5$ — ***the width `cc66.51` read the
candidate at*** — while the held estimator sits near $2.5$ per cent at **every** width and reaches
$q = 0.39$, against the window estimator's hard floor of $1.5 + \mathrm{half} \ge 2.00$.

**⛭ AND THE LEAK IS MEASURED, NOT NOTED, AND IT IS HALF A PER CENT.** Perturbing the held period at the
$1.3$ per cent it is known to moves the candidate's span across the bands by $0.00005$ against a span of
$0.0097$. ⌗ *The reason is a mechanism: the fit re-fits the **phase** in every window, so a wrong held
period is absorbed there and costs only a common amplitude factor — which cancels in a ratio of ratios.*
⇒ ***The estimator can answer the question.***

**⛭⛭ ⓶ IT REACHES $q = 1.90$, AND STOPS AT $q = 1.20$ FOR A MECHANISM.**

| $q$ | 1.20 | 1.90 | 2.60 | 3.30 | 4.00 | 4.70 | 5.40 |
|---|---|---|---|---|---|---|---|
| departure | $-0.0003$ | $+0.0048$ | $+0.0049$ | $+0.0051$ | $+0.0090$ | $+0.0124$ | $+0.0144$ |
| spread over 8 settings | $0.0210$ | $0.0030$ | $0.0050$ | $0.0052$ | $0.0011$ | $0.0021$ | $0.0010$ |

⛔ **Band 1 is still not measurable** — its spread exceeds its value — *because its window straddles the
first acoustic excursion, where there is no oscillation amplitude to estimate.* **A floor of mechanism,
not of width**, and the pre-registration's second null.

**⛭ THE TEETH, SIGN FIRST.** On $q = 1.90$–$5.40$ the candidate's departure is **positive in every band**
as the target's is, and runs $+0.0048 \to +0.0144$: $G = 2.99$ against the target's $1.33$, the same
direction. ⇒ ***It passes SIGN and it passes GROWTH, on the range this estimator unlocked.***

**⛔⛔ AND THE CURVATURE TOOTH CANNOT BE APPLIED — THE FIRST NULL, AND THE REASON IS EXACT RATHER THAN
STATISTICAL.** On the full seven-band range the target's curvature is $-0.0033$ as pre-registered at
`r6993`. **Dropping band 1 alone flips it to $+0.0003$; dropping any other single band leaves it in
$[-0.0053,\,-0.0028]$.** ⇒ ***The target's deceleration is carried entirely by the one band no estimator
of the candidate can reach.*** *The filter is out of teeth rather than the candidate out of chances, and
that is a statement about the filter.*

**⚠⚠ AND `cc66.51`'s CURVATURE PASS DOES NOT SURVIVE — a correction to this seat's own landed result.**
Read with the window estimator on its own range and its own recipe, the candidate's curvature runs
$-0.0093$ at `half` $=0.5$, $-0.0005$ at $1.0$, $+0.0012$ at $2.0$. ⛔ **`cc66.51`'s stability check
certified the MEAN over a sub-range; the curvature was never the quantity that was checked** — the
"say which quantity" guard biting the seat that wrote it. ⌗ *The mean is reproduced and stands; only the
curvature read off it does not.*

**⛭⛭⛭ ⓷ THE PREDICTION IS AN INDEPENDENT READING OF THE JACOBIAN, AND IT IS NOT OBSERVABLE.**

- **The comb reads the CUMULATIVE ratio** $r_{s,\rm leaf}/r_{s,\rm stack}$ at last scattering $= 0.5665$:
  $\pi D_M/r_{s,\rm leaf} = 301.41$ against the banked $l_A = 301.80$, while
  $\pi D_M/r_{s,\rm stack} = 170.76$ is not close.
- **The widths read the WINDOW-LOCAL average** $\langle\mathrm{Jac}\rangle = 0.8744$.
- ⇒ ***A third apart. Both are $1$ on one rate and neither carries a free coefficient, so a construction
  tuned to the comb must still produce the right LOCAL Jacobian to match the widths.*** **The width ratio
  is not a restatement of the comb.**

⛔ **But no measurement reaches the ratio.** The **phase** width, which the window's Landau damping reads,
differs between the arms by $0.84$ per cent; the **conformal** width, which the projection reads, differs
by $13.5$ — and `cc66.52` bounded the projection's contrast effect at $2$ per cent with its sign
undetermined. ⇒ ***NO, not observable in its own right*** — said in the order's own terms. ⌗ *The
independence finding above is named as a separate thing and is not offered as an observability argument;
where the passage lives is the chat seat's call.*

**⛔ ⓸ NOTHING ELSE.** No new channels. *The polarisation note in `r7001_directions/independent.py` is a
statement about what this instrument does not carry — it banks polarisation only as its contribution to
the temperature decomposition, not as an E-mode spectrum — and is not a proposal.*

## `cc66.54` (`r7003`) — THE LOWEST BAND IS CLOSED BY THE FIELDS AT AN EXACT FLOOR; THE DECELERATION IS CARRIED BY THAT BAND ALONE AND BY THIS ENVELOPE; AND THE FILTER'S THIRD CONDITION IS UNAVAILABLE EXACTLY WHERE IT IS NEEDED

*Path: **hierarchy** throughout. Banks `r6897_fields`, `r6941_fine_*`, `r6959_eta_cr`; receipt
`P15_the_lowest_band_is_closed_by_the_fields_and_the_excess_deceleration_is_carried_by_it_alone.py`,
**19 gates**; pre-registration `r7003_directions/PREDICTION.md`, **failure modes tabled ahead of
outcomes**. ⛔ Nothing SOLVED.*

**⛭⛭⛭ ⓵ THE BAND IS CLOSED BY THE FIELDS, AND THE FLOOR IS EXACT.** The criterion is named before use and
is a necessary condition from identifiability, not a chosen threshold: *an oscillation amplitude at $q_0$
is identified only if the fitting window holds a **turning point** of the field on each side of $q_0$* —
because over a span carrying no turning point the held-period $\cos/\sin$ pair is monotone in $q$, and a
monotone function over a short span is what the baseline polynomial already spans.

- The monopole's turning points are $q = 0.996,\,1.915,\,2.912,\dots$ with **none below the first**: the
  first excursion is one-sided. ⇒ floor $= 1.4553$ (control), $1.4533$ (arm).
- The dipole's floor is $0.9618$, so **the monopole binds** — the reach of a *ratio* of the two
  amplitudes is set by the field whose first excursion starts later.
- ⇒ ***Band 1, $q \in [0.85,\,1.55]$, lies $86.5$ per cent below the floor. Bands 2–7 lie entirely above
  it.***

**⌷ AND IT IS NOT THE WINDOW, SHOWN THREE WAYS.** *Width*: the same eight window widths at identical
conditioning spread $0.0039$ at $q_0 = 1.90$ and $0.0164$ at $q_0 = 1.20$, with a sign change.
*Placement*: sweeping the left edge with the right held, the departure is **negative for every window
that opens past the monopole's first turning point and positive for every one that stays above it** —
what lies below is the field's rise from its initial condition, which is not an acoustic oscillation.
*Prediction*: **every centre below the floor spreads by more than every centre above it** ($0.0164$
against $0.0126$), which the floor was not fitted to.

⇒ *** NO ESTIMATOR OF AN OSCILLATION AMPLITUDE CAN REACH INSIDE THE FIRST EXCURSION. An acoustic
oscillation has a first extremum and there is no amplitude before it because there is no oscillation
before it. ***

**⛭⛭ ⓶ THE TARGET'S OWN CURVATURE, IN THREE PARTS — AND THE THIRD GOES AGAINST THIS SEAT'S RESULT.**

- **(a) Robust within the statistic as defined.** Moving the envelope width ($0.8$–$1.2$), the band edges
  ($\pm0.05$) and the sampling: the curvature is **negative in all six variants**, $-0.00377$ to
  $-0.00291$, with band 1 stable at $+0.0201$ to $+0.0240$. *"The excess decelerates" is not a fragile
  number.*
- **(b) And carried by band 1 alone.** With band 1 dropped the curvature runs $-0.00121$ to $+0.00031$:
  **its sign is not determined.** ⇒ ***The deceleration is the lowest band being low, not the upper bands
  bending*** — and that band is the one ⓵ closes.
- **(c) ⚠⚠ And NOT robust to the envelope's DEFINITION.** A running **median** envelope — same window,
  same bands, everything else unchanged — ***reverses the curvature to $+0.00504$***. That is a different
  statistic, and the difference is measured (its envelope absorbs about half the top band's oscillation
  on both arms, $0.0962 \to 0.0441$ control and $0.1035 \to 0.0525$ arm, so its ratios are formed on a
  much smaller residual). ⛔ **But it is not obviously the worse envelope** — it leaves a departure with
  zero mean, which the arithmetic one does not — *so the honest reading is that the sign belongs to the
  statistic rather than to the excess.*

⇒ **`P15` may say the excess decelerates and owes two qualifications in the same breath: that the
deceleration is carried by the lowest band, and that it is a property of this envelope.** ⌗ *What was
landed too strongly is not the claim but its **independence** — of any one band, and of the envelope's
definition — which nothing in the paper says and a reader would assume.*

**⛔⛔ ⓷ AND THE THIRD CONDITION IS NOT UNAVAILABLE IN GENERAL, WHICH IS WORSE THAN IF IT WERE.** It needs
a band-1 value. Band 1 is closed to *oscillation-amplitude* estimators — **not** to a candidate computed
from the kernel: `cc66.52`'s projection-width channel had a band-1 value ($+0.00343$) and the filter
**excluded it on curvature**. ⇒ *** THE FILTER'S FULL STRENGTH IS AVAILABLE EXACTLY FOR THE CLASS THAT
CANNOT CARRY THE EXCESS, AND ITS THIRD CONDITION IS PERMANENTLY UNAVAILABLE EXACTLY FOR THE CLASS THAT
CAN *** — since `cc66.51` settled on physics that what fills a trough is an oscillation amplitude.

**⌗ AND IS A TWO-CONDITION FILTER A FILTER? SEPARATELY, BECAUSE THE ANSWERS DIFFER.**

- **As an exclusion device, yes, and it has lost nothing.** Sign and growth are each necessary on a
  carrier, and the exclusions already made were made on growth alone.
- **As a confirmation device, no — and it never was one, not with three either.** All three conditions
  are conditions on the *shape* of a departure in $q$, and a shape match does not fix a size: **measured
  here, the candidate matches the target in sign and in direction of growth while being $5.3$ times
  smaller at the top band.**
- ⇒ *So the candidate's passing two is worth exactly what passing three would have been — it is **not
  excluded** — and the row's remaining question is the **coupling**: how much band contrast a
  dipole-to-monopole amplitude ratio of a given size actually produces. That is quantitative, lives on
  $q \ge 1.90$ where the candidate **is** measured, and needs band 1 not at all.* ⛔ **Named as the
  question, not proposed as a channel: the order's ⓸ closes the list.**

## `cc66.55` (`r7005`) — THE COUPLING IS MEASURED AND NEGATIVE AND FIXED BY THE CONSTRUCTION; THE CONTRIBUTION IS UNDETERMINED BECAUSE ITS INPUT IS

*Path: **hierarchy** throughout. Banks `r6941_fine_*`, `r6975_mix_lcdm` and `r6975_mixb_lcdm` (the two
banked `DPSRC` points), `r6959_eta_*`; receipt
`P15_the_coupling_is_measured_and_negative_and_the_contribution_is_undetermined_because_its_input_is.py`,
**14 gates**; pre-registration `r7005_directions/PREDICTION.md`, **five failure modes ahead of five
outcomes**. ⛔ Nothing SOLVED — the three `DPSRC` spectra were already on disk.*

**⛭⛭ THE COUPLING IS MEASURED, NOT MODELLED.** `DPSRC` scales the Doppler source term, so the banked
control spectra at `DPSRC` $=1,\,0.8794,\,0.6$ give $d\ln C/d\ln s$ per band as a finite difference —
***three points, so the linearity is checked rather than assumed***, and it steepens towards $s=1$ at all
seven bands, so the local slope there is both the applicable one and the one measured over the shortest
step. Near $s=1$ on the arithmetic envelope it runs $-0.45$ to $-0.80$ with **no trend in $q$**.

⇒ *** NEGATIVE AT EVERY BAND, ON BOTH ENVELOPES, OVER EVERY INTERVAL — forty-two measurements of the sign
and not one positive. *** *More Doppler fills more trough and lowers the contrast: `cc66.51`'s own
trough-filling physics read forwards.*

**⛭ ⓶ AND THE CONSTRUCTION FIXES IT, SHOWN BY WHAT DOES NOT CHANGE IT.** The control's own
Doppler-to-monopole band-power share runs $4.30$ down to $0.65$ — **a factor of $6.6$ across the bands —
and the coupling's sign is the same at every one.** ⇒ *A quantity whose sign is invariant across a factor
of six in the very ratio it depends on is not set by a knob*: `DPSRC` is the **probe**, not the setter.
***So the size is a prediction and not a fit.*** ⚠ *All three `DPSRC` banks are the control, so the arm's
coupling is assumed to be the control's; its share differs by about a fifth against the factor of six
across which the sign does not move, so the assumption cannot reach the sign and is not asked to.*

**⛔⛔ ⓵ AND THE CONTRIBUTION IS NOT DETERMINED — NOT BECAUSE OF THE COUPLING BUT BECAUSE OF ITS INPUT.**
The criterion was named before use: *the coupling multiplies a fractional change in the Doppler's
oscillation amplitude relative to the monopole's.* Two measured quantities claim to be it:

| reading | the arm against the control | contribution | fraction of the excess |
|---|---|---|---|
| **FIELD** (`cc66.51`'s held-period estimator, at last scattering) | **higher** by $+0.5$ to $+1.4$ % | $-0.004$ to $-0.010$ | **$-7$ to $-13$ %, the WRONG sign** |
| **PROJECTED** (`cc66.50`'s quantity, $\sqrt{}$ of the banked `w2dp/w2sw` share — *what `DPSRC` actually scales*) | **lower** by $10$ to $13$ % | $+0.066$ to $+0.108$ | **$+188$ down to $+94$ %, the RIGHT sign** |

⇒ *** THE COUPLING TURNS A DISAGREEMENT ABOUT A QUANTITY INTO A DISAGREEMENT ABOUT WHETHER THE CANDIDATE
HELPS AT ALL — a factor of seven in magnitude even at their closest. This is the third revision in which
these two readings decide the answer between them and the first in which they decide its SIGN. ***

**⌗ AND THE ORDER'S SECOND HALF — CONSTANT SHORTFALL OR GROWING? GROWING, ON BOTH READINGS, IN OPPOSITE
DIRECTIONS.** The field reading's fraction grows in magnitude from $-7$ to $-13$ %; the projected
reading's falls from $+188$ to $+94$. ⇒ ***A shape mismatch and not a coupling deficit, on either
reading, and the fourth this sector has found.*** *The coupling is flat, so the $q$-dependence belongs to
the input.*

**⛭ ⓷ AND THE ENVELOPE QUESTION HAS THE GOOD ANSWER.** The coupling's sign survives both envelopes at
every band, so **the contribution does not reverse with the statistic and the coupling question does not
inherit the envelope ambiguity.** *Its magnitude does — the median envelope's coupling reaches $2.2\times$
the arithmetic one's at the top band — so a quoted **fraction** inherits the ambiguity while the **sign**
does not, and that is said before any fraction is quoted.* ⛔ *The envelope question is not revisited to
settle it: the order forbids that, both are carried, and no conclusion rests on choosing one.*

**⌗ AND WHAT WOULD SETTLE THE INPUT, NAMED AND NOT BUILT.** Neither banked quantity is the right one: the
field reading is an amplitude but **at last scattering** rather than in the projected source, and the
projected reading is in the projected source but is a **band power**, which keeps the smooth part
`cc66.51` showed fills no trough. ⇒ **The quantity the coupling multiplies is the OSCILLATION AMPLITUDE OF
THE PROJECTED DOPPLER CONTRIBUTION, per band, and the instrument banks neither it nor the $\eta$-resolved
fields a derivative of it would need.** *One bank, not a channel: the order's ⓸ closes the list.*

## `cc66.56` (`r7007`) — THE BANK ALREADY EXISTED; THE DOPPLER CARRIES A GROWING MINORITY; AND THE FOUR SHAPE MISMATCHES SHARE A REASON ABOUT THE EXCESS

*Path: **hierarchy** throughout. Banks `r6915_pairs_{lcdm,cr}` (the `SRCDEC` bilinear decomposition),
`r6941_fine_*`, `r6959_eta_cr`; receipt
`P15_the_bank_already_existed_and_the_doppler_carries_a_growing_minority_of_the_excess.py`, **13 gates**;
pre-registration `r7007_directions/PREDICTION.md`, five failure modes ahead of five outcomes with
"settles nothing" tabled first. ⛔ Nothing SOLVED and nothing RUN.*

**⛭⛭ ⓵ THE INSTRUMENT ALREADY EMITS THE RIGHT QUANTITY AND BOTH ARMS' BANKS ARE ON DISK.** `SRCDEC`,
added at `r6915+cc66.41`, writes the full bilinear decomposition — $C_\ell = \sum_{a\le b} w_{ab}\sum_k
P\,\Delta^a\Delta^b$, **ten $\ell$-resolved terms per multipole summing to $C_\ell$ exactly** (verified to
$1.2\times10^{-15}$). ⇒ **No run, no instrument change, and the order's escape hatch is not needed.**
⌗ *The grid is $238$ multipoles against the fine banks' $1900$: it reads the contrast $1.9$ per cent low
and the deficit agrees between the arms to $3\times10^{-4}$, so it cancels in the ratio — the only thing
read from it.*

**⛭ AND THE BANK DISCHARGES A CAVEAT `cc66.55` COULD ONLY STATE.** The $s$-scaling of every pair is exact
— $s^2$ on `dp*dp`, $s$ on the three `dp` crosses — so $dD_\ell/d\ln s = (\texttt{sw*dp} +
\texttt{dp*isw} + \texttt{dp*pol}) + 2\,\texttt{dp*dp}$ per multipole and the coupling follows
**analytically for the arm as well as the control**: $-0.48$ to $-0.86$ on each, **equal between the arms
to $4$ per cent**, agreeing with `cc66.55`'s three-point finite difference to $7$.

**⚠ AND THE FIRST CONSTRUCTION IS REPORTED AS FAILED RATHER THAN DROPPED.** The obvious reading,
$\sqrt{\mathrm{osc}(\texttt{dp*dp})/\mathrm{osc}(\texttt{sw*sw})}$ per band, is small on the arithmetic
envelope ($|\delta| \le 0.010$) and reaches $+134$ per cent under a median one — *because the oscillation
of a weak, smooth term about a median envelope is not well conditioned.* ⇒ **That definition inherits
the envelope ambiguity through its own conditioning, so it is not used**, and the failure is dated in the
pre-registration.

**⛭⛭ WHAT IS USED NEEDS NO EQUIVALENT-$s$ STEP: A ONE-AT-A-TIME SWAP.** On the arm's own $q$ grid,
replace the arm's four Doppler-containing pairs by the control's, envelope-scaled, and recompute the
contrast; the share is $(C_{\rm arm}-C_{\rm swapped})/(C_{\rm arm}-C_{\rm control})$. *Same shape of
operation as `SRCINJRS`'s one-at-a-time clock swap, which the instrument already sanctions.*

**⛔ ⓶ AND THE CONTRIBUTION IS A MINORITY SHARE THAT GROWS AND IS SIGN-INDEFINITE AT THE BOTTOM.**

| $q$ | 1.20 | 1.90 | 2.60 | 3.30 | 4.00 | 4.70 | 5.40 |
|---|---|---|---|---|---|---|---|
| share, arithmetic envelope | $+1\%$ | $-12\%$ | $+5\%$ | $+12\%$ | $+11\%$ | $+26\%$ | $+17\%$ |
| share, median envelope | $+12\%$ | $-20\%$ | $-13\%$ | $+32\%$ | $+33\%$ | $+34\%$ | $+48\%$ |

⇒ ***The candidate is not the carrier.*** **It lands between the two wrong readings — which said $-13$
and $+188$ per cent — and it does not settle nothing: it settles that the candidate is a real but
MINORITY contributor, which neither wrong reading said.** ⌗ *`cc66.55`'s split is confirmed rather than
assumed: the coupling's sign is the same on both envelopes while the fraction moves by $2.7\times$.*
⛔ *No envelope is chosen — the order's refusal held for a second revision.*

**⛭⛭⛭ ⓷ AND THE FOUR MISMATCHES DO SHARE A REASON, AND IT IS ABOUT THE EXCESS.** The excess has **one**
dominant feature: ***band 1 is $0.33$ of the mean of the rest and sits $4.9$ scatters below it***, while
above band 1 a constant already fits (scatter $0.0088$ on a mean of $0.0645$) and a line only halves the
residual.

⇒ *** THE EXCESS'S $q$-STRUCTURE IS A STEP AT THE LOWEST BAND, NOT A TREND — AND ALL FOUR CANDIDATES WERE
JUDGED ON A TREND ACROSS BANDS 2–7, WHERE THE EXCESS IS VERY NEARLY FEATURELESS. ***

- A **flat** candidate — the window weighting (`cc66.47`), the term mix (`cc66.48/49`), the band-power
  reading (`cc66.50`) — matches the flat part and misses the step.
- A **rising** one — the projection width (`cc66.52`), the field reading (`cc66.53`) — matches the mild
  rise and misses the step.
- **On bands 2–7 the two are barely distinguishable, because there is almost nothing there to
  distinguish them with.**

⇒ **So the sector has been spending its discriminating power on the part of the excess carrying least
structure, because the part carrying the structure is the band `cc66.54` showed it cannot measure a
candidate in.** ⌗ *That is `cc66.54`'s own finding seen from the candidate side, and it is why four
mismatches look like four failures rather than one.*

## `cc66.57` (`r7009`) — THE STEP IS THE EXCESS'S OWN, IT SITS AT THE SECOND ACOUSTIC PEAK, AND NONE OF THE FOUR CANDIDATES PRODUCES IT

*Path: **hierarchy** throughout. Banks `r6941_fine_*`, `r6915_pairs_*`, `r6897_fields`, `r6959_eta_cr`;
receipt `P15_the_step_is_the_excesss_own_and_it_sits_at_the_second_acoustic_peak_and_none_of_the_four_produces_it.py`,
**12 gates**; pre-registration `r7009_directions/PREDICTION.md`, **written before any of ⓵ was computed**,
on the order's explicit sequencing. ⛔ Nothing SOLVED, nothing RUN.*

**⛭⛭ THE SEQUENCING WAS HONOURED, AND IT IS CHECKED RATHER THAN CLAIMED.** The pre-registration says in
terms that nothing in ⓵ had been computed when it was written, names the step's definition before use —
*band 1's excess over the mean of bands 2–7* — and **tables first the outcome that withdraws `cc66.56`'s
⓷**, which `r7009` had already landed in two sections. ⌗ *The three previous revisions each had to record
that their outcome tables followed their measurements; this one does not.*

**⛭⛭⛭ ⓵ THE STEP IS THE EXCESS'S AND NOT THE ESTIMATOR'S.**

| reading | band 1 | step ratio |
|---|---|---|
| running arithmetic mean | $+0.0215$ | $0.333$ |
| running median | $+0.0407$ | $0.391$ |
| local quadratic (Savitzky–Golay) — *a third envelope, different in kind* | $+0.0405$ | $0.633$ |
| **peak-to-trough depth per cycle — no envelope at all** | $-0.0017$ | $-0.025$ |

⇒ **Never near one on any of them.** *And the envelope-free reading is the sharpest: band 1's excess is
indistinguishable from zero against a bands 2–7 mean of $+0.0654$; it carries only one acoustic cycle per
band, so it is coarse, and that is stated.*

**⌷ AND THE EDGE HAZARD IS RULED OUT THE RIGHT WAY ROUND, which is what makes it ruled out.** Band 1's
envelope comes within $0.018$ in $q$ — about five multipoles — of truncating. But moving the band's lower
edge **up**, away from the hazard, makes it read $+0.0215 \to +0.0239 \to +0.0282 \to +0.0361$:
**higher, where a truncation artefact would have to make it read lower.**

⚠ *Its **size** is reading-dependent, so the step is quoted as **"band 1 between none and two thirds of the
rest"**, not as a number.* ⛔ *No envelope is chosen — a third was added, which is what the order asked.*

**⛭⛭⛭ ⓶ AND IT SITS AT THE SECOND ACOUSTIC PEAK.** The half-rise point of the excess, in sliding windows
at three widths, is $q = 1.789,\,1.788,\,1.805$ — **$1.794 \pm 0.008$** — against the second acoustic peak
at $q = 1.7775$ (control) and $1.7760$ (arm): ***a match to $0.9$ per cent***, where the nearest other
scale the construction fixes — the monopole's second turning point at $1.915$ — is **seven** per cent away
and $q=2$ is twelve. ⌗ The plateaux are $0.026$ below and $0.053$ above on all three widths: **a factor of
$2.0$, reached within about a tenth of a comb period — sharper than the narrowest window that found it.**

⇒ *** THE EXCESS IS ONE SIZE IN THE FIRST ACOUSTIC CYCLE AND TWICE THAT IN EVERY CYCLE ABOVE IT. ***
⛔ **Not claimed: that this is a mechanism.** *A step at a scale is a signature to be explained — which is
what the pre-registration said would not be claimed.* ⌗ *And the peaks sit at fixed $q$ on both arms, so
what the step says is that the **first acoustic cycle** differs, not that an arm-specific scale sits there.*

**⛔⛔ ⓷ AND ALL FOUR CANDIDATES CAN BE SCORED ON THE STEP, AND NONE OF THEM PRODUCES IT.**

- the **window weighting** (`cc66.47`) and the **term mix** (`cc66.48/49`): both measured **flat in $q$** —
  and a flat candidate's step ratio is exactly one, *by construction and without a new number*;
- the **projection width** (`cc66.52`), kernel-class and reachable at band 1: fitted by a **straight line
  in $q$ to $2.6$ per cent of its own range** — linear, so no step;
- the **Doppler**, by the swap route that reaches band 1 (`cc66.56`): $-0.0016$ to $+0.0014$ in sliding
  half-period windows, with means $-0.0001$ below the step and $-0.0002$ above — **noise at the step's
  resolution and no transition at all.**

⇒ *** NOT the identifiability floor closing over the list — every one of the four WAS evaluable — but the
list EXHAUSTED against the right feature, for the first time. *** ⌗ *So the row's question is now: **what
turns on at the second acoustic peak?** Narrower than the question this sector has asked for six
revisions, and not a channel.*

## ⛭⛭⛭ `cc66.58` — `r7011` FILLED: THE WINDOW-FREE READING CANNOT RESOLVE THE FIRST CYCLE, THE FLATNESS WAS A **TREND**, AND NINE TENTHS OF THE STEP IS **COMMON TO BOTH ARMS**

**Receipt** `receipts/P15_CR_cosmology/P15_the_window_free_reading_cannot_resolve_the_first_cycle_the_flatness_was_a_trend_and_nine_tenths_of_the_step_is_common_to_both_arms.py` — **34 gates, `GATES: ALL PASS`**, 1.1 s. Pre-registration `computations/beyond_the_wall/r7011_directions/PREDICTION.md` committed *before* the working script `the_first_cycle.py` was run, in separate commits. Nothing solved, nothing run, no corpus edits.

### ⓵ THE WINDOW-FREE FAMILY HAS ONE DATUM BELOW THE STEP, SO IT CANNOT ANSWER — AND THAT IS THE ANSWER

Its band 1 rests on **exactly one half-cycle transition**, because the first locatable extremum pair sits at $q = 1.363$ and the step is at $1.794$. So $-0.0008$ is $0.02\sigma$ from **zero** *and* $1.60\sigma$ from the bands 2–7 mean: consistent with both, informative about neither. The uncertainty is not asserted — it is the per-transition scatter $0.0456$ over the ten data in bands 2–7.

No finer member escapes it. The **extremal envelope** — successive maxima and successive minima interpolated separately, no running window anywhere — covers only $27\%$ of band 1, rests on the same single extremum, and interpolates *across* the step, so its $+0.0245$ is biased **toward** the above-step value. Three settings of the extremum finder give the same below/above ratio $0.338$ to six decimals.

⇒ **The answer comes from the statistics that do resolve band 1, and there the excess is $+0.0215$** over the full band $q = 0.85$–$1.55$, including the $73\%$ of it the window-free family cannot reach. **"Small but non-zero" is the supported row; the step stays a step rather than becoming an onset.**

⛔ **`cc66.57`'s "the sharpest of the four" is WITHDRAWN — it was the coarsest**, by one datum against four hundred. Its "none" endpoint goes with it, **as unresolved rather than as a reading**, which *tightens* the size: $0.333$, $0.391$, $0.633$ windowed and $0.338$ on the extremal envelope — band 1 between a third and two thirds of the rest.

### ⓶ THE RANGE WAS FULL; THE STATISTIC WAS A TREND; AND NEITHER CHANNEL IS FLAT

**(a)** `cc66.49`'s fit abscissa is `Q2 = QC ** 2` over the centres of **all seven bands** — read off that receipt's own file and gated on it. So band 1 *is* in the flatness measurement and **the disposal is not circular on range**; the order's first reading of the hazard does not fire.

**(b) But the statistic is a trend, and that is the half this seat owns.** $\lvert\text{slope}\times\langle q^2\rangle\rvert/\lvert\text{intercept}\rvert$ cannot exclude a step, which lives in the **residual** — the JOINT reads $0.004$ on that statistic while leaving $61\%$ of its own range unexplained by that line.

**(c) Re-scored on band 1's departure from its own bands 2–7 trend, across four trend bases with none chosen:**

| channel | $v\sim q$ | $v\sim q^2$ | $\ln v\sim q$ | $\ln v\sim q^2$ | verdict |
|---|---|---|---|---|---|
| window | $+0.449$ | $+0.531$ | $+0.468$ | $+0.560$ | **steps UP** — wrong sign |
| term mix | $-0.385$ | $-0.358$ | $-0.378$ | $-0.350$ | **steps DOWN**, $63\%$ of the excess's |
| JOINT (realised pair) | $-0.266$ | $-0.233$ | $-0.259$ | $-0.225$ | down, $42\%$, $2\sigma$ on three bases |
| measured excess | $-0.566$ | $-0.598$ | $-0.575$ | $-0.601$ | the step itself |
| projection width | $+0.282$ | $-0.346$ | $-0.295$ | $-0.446$ | **flips sign** ⇒ no step |

⇒ ***`cc66.57`'s ⓷ is withdrawn in part and THE LIST IS NOT EXHAUSTED.*** Its sentence *"a flat candidate's step ratio is exactly one, by construction and without a new number"* was never earned. The step has a **partial account** — a minority share, as the Doppler turned out to be — rather than none.

⌗ **The projection width's disposal stands, and the basis table is what shows why**: that channel is linear in $q$ to $2.6\%$ of its range, so a log basis *manufactures* a step for it and it flips sign across the family. `cc66.57` scored that one on a residual from a straight line in $q$ — the sound one of the four.

### ⓷ BOTH ARMS STEP, NEARLY EQUALLY, AND THE EXCESS'S STEP IS THE PART THAT FAILS TO CANCEL

On **every** one of the four bases and on **both** the windowed and the window-free contrast: the control departs from its own bands 2–7 trend by $+30$ to $+44$ per cent at band 1, the arm by $+27$ to $+39$, **the arm always the shallower — by some eleven per cent of the step and no more**.

⇒ ***So of a step worth tens of per cent in each spectrum, about nine tenths is COMMON to the two arms and cancels in the ratio; the excess's step is the tenth that does not.*** That is the pre-registration's "both arms" row: the step belongs to the acoustic physics the two share, and it explains — without a new number — why `cc66.57` found the location at fixed $q$ on **both** arms.

⚠ **And the caution is this seat's, not the order's:** a small residual of two large common features is exactly where a *nearly*-common systematic would sit. That does not make the step an artefact. It does mean **the next reading of it should be differential by construction** rather than a difference of two large numbers.

### THE DISCIPLINE THIS REVISION ADDS

⚠ ***A TREND STATISTIC CANNOT EXCLUDE A STEP.*** A small slope says nothing about a residual, and two of `cc66.57`'s four disposals rested on exactly that non-sequitur.
⚠ ***A RESIDUAL-AGAINST-TREND STATISTIC NEEDS A BASIS, AND THE BASIS IS A CHOICE — SO DO NOT CHOOSE IT.*** The projection width is linear in $q$; a log basis manufactures a step for it. Four bases are reported; a departure counts only if it survives all four. *Fourth revision running on "do not choose — name the family".*
⚠ ***COUNT THE DATA BEFORE CALLING A READING SHARP.*** "Envelope-free" is a statement about bias, not about resolution, and the reading with the least bias here had one datum where it mattered.

## ⛭⛭⛭ `cc66.59` — `r7015` FILLED: THE STEP **SURVIVES** THE DIFFERENTIAL ESTIMATOR; **NO SINGLE BILINEAR TERM** CARRIES THE SHARED STEP; AND THE $42\%$ IS $42\%$ OF THE **EXCESS'S** STEP

**Receipt** `receipts/P15_CR_cosmology/P15_the_step_survives_a_differential_estimator_and_no_single_bilinear_term_carries_the_shared_step_though_the_doppler_leads_it.py` — **28 gates, `GATES: ALL PASS`**, 0.3 s. Pre-registration `computations/beyond_the_wall/r7015_directions/PREDICTION.md` is its own commit ahead of the working script `the_differential.py`. Nothing solved, nothing run, no corpus edits.

### ⓵ THE STEP SURVIVES AN ESTIMATOR IN WHICH THE TWO LARGE COMMON STEPS ARE NEVER FORMED

Writing each arm as $\mathcal D = E(1+o)$: the present route forms $\operatorname{std}(o_a)$ and $\operatorname{std}(o_c)$ and divides; the ordered route forms $R = \mathcal D_a/\mathcal D_c \approx (E_a/E_c)(1+o_a-o_c)$ and takes the contrast of **that**, so it reads $\operatorname{std}(o_a-o_c)$ — **the common oscillation divides out before any width is taken.**

| reading | band-1 departure, four bases | significance |
|---|---|---|
| per common $\ell$ | $-0.374$ … $-0.387$ | $3.5$–$3.6\sigma$ |
| per common $q$ | $-0.382$ … $-0.383$ | $3.2$–$3.3\sigma$ |
| *(present route, for scale)* | $-0.566$ … $-0.601$ | $7.2$–$7.7\sigma$ |

⇒ ***Same sign on all four trend bases and both abscissas, at about $65\%$ of the present route's fractional size. SO THE TENTH THAT FAILED TO CANCEL IS NOT THE RESIDUAL OF TWO LARGE NUMBERS.*** The costliest pre-registered outcome does not fire, and the estimator is the one the row should be built on.

⌷ The conditioning hazard named in the pre-registration does not fire either — the control never falls below $0.67$ of its band median, the first acoustic trough inside band 1 included. And the **smoothed-divisor control** turns the departure *positive*, back toward the arms' own $+0.3$: **it is the differencing, not the division, that produces the negative step.**

⚠ **What the new estimator is not**, named in the pre-registration rather than after: $\operatorname{std}(o_a-o_c)$ is sensitive to a **phase** difference as well as an amplitude one. A null on it would have been strong; a signal on it does not by itself say "amplitude", and its absolute size carries no expectation — only the step is compared.

### ⓶ NO SINGLE TERM CARRIES THE SHARED STEP — IT IS A PROPERTY OF THE SUM

The licence check comes first, as pre-registered: the 238-multipole `SRCDEC` total reproduces the 1900-multipole step to better than $0.006$ in departure on **both** arms. Then removing each term in turn, **the fractional losses sum to $182\%$** — far more than one, so the step is not additive across terms. **That is the pre-registered null on the naming.**

⛭⛭ **But the leverage is not flat**, and that is what the null leaves standing:

| term | share of the step | share of the oscillation | leverage |
|---|---|---|---|
| `sw*dp` | $+29.1\%$ | $5.2\%$ | $\mathbf{5.59\times}$ |
| `dp*dp` | $+46.2\%$ | $12.2\%$ | $\mathbf{3.80\times}$ |
| `sw*isw` | $+39.3\%$ | $31.8\%$ | $1.23\times$ |
| `sw*sw` | $+63.4\%$ | $88.1\%$ | $0.72\times$ |
| `dp*isw` | $-12.1\%$ | $13.3\%$ | $-0.91\times$ |
| `isw*isw` | $-9.6\%$ | $4.6\%$ | $-2.07\times$ |

⇒ **A step-weighted reading of the bilinear decomposition is led by the Doppler where an amplitude-weighted one is led by the monopole.**

⚠ `dp*isw` is the named exception — a Doppler-bearing term with *negative* leverage — and `isw*isw` sits lower still, so the ordering is **not** Doppler-versus-not, and the claim is "the two highest-leverage terms are Doppler", not "every Doppler term leads". **And leverage is not authorship**: the non-additivity is the reason it is not.

### ⓷ THE $42\%$ IS $42\%$ OF THE EXCESS'S STEP

`cc66.58`'s share function divided every channel's departure by the departure of `MEAS - 1.0` — the **excess's own response** — which is read off that file and gated on it. That is the only comparison a channel admits: a channel response and the excess are both ratios to the *same* control. ⇒ **So it is the large reading: the pair accounts for two fifths of the step the excess actually has, not of the shared step most of which cancels.**

⌗ And the two normalisations are **one departure under two denominators**, $-0.0323$ in excess units:

* $-0.601$ of the excess's own extrapolated size — *what the $42\%$ is against*;
* $-0.100$ of the control's contrast departure — *where the "nine tenths" comes from*.

Provable rather than asserted: the arms' own log-departures differ by $-0.0308$, which is that same number to $4.6$ per cent.

### THE DISCIPLINE THIS REVISION ADDS

⚠ ***A DIFFERENTIAL ESTIMATOR IS A DIFFERENT QUANTITY, NOT A CLEANER VERSION OF THE SAME ONE.*** $\operatorname{std}(o_a-o_c)$ and $\operatorname{std}(o_a)/\operatorname{std}(o_c)$ differ in what they are blind to; only the step may be compared between them, and the absolute sizes may not.
⚠ ***A SHARE NEEDS A DENOMINATOR NAMED IN THE SAME BREATH.*** ⓷ exists because `cc66.58` quoted $42\%$ without one, and the two available denominators differ by an order of magnitude on the same departure.
⚠ ***LEVERAGE IS NOT AUTHORSHIP.*** When removal losses sum to $182\%$, no term "carries" the feature, and a per-term ranking may be reported only as a ranking.

## ⛭⛭⛭ `cc66.60` — `r7017` FILLED: THE SURVIVING STEP IS **AMPLITUDE**, THE CANDIDATE SHARES **DO NOT SURVIVE** THE CHANGE OF DENOMINATOR, AND THE STEP **DOES NOT COMPOSE** THE WAY THE CONTRAST DOES

**Receipt** `receipts/P15_CR_cosmology/P15_the_surviving_step_is_amplitude_and_not_phase_and_the_candidate_shares_do_not_survive_the_change_of_denominator.py` — **23 gates, `GATES: ALL PASS`**, 0.5 s. Pre-registration `computations/beyond_the_wall/r7017_directions/PREDICTION.md` is its own commit ahead of the working script `amplitude_or_phase.py`. Nothing solved, nothing run, no corpus edits.

### ⓵ AMPLITUDE, NOT PHASE — SO THE ROW IS NOT REFRAMED

With $o_c = A_c\cos\psi$, $o_a = A_a\cos(\psi+\Delta)$ and $r = A_a/A_c$:
$$\operatorname{std}(o_a-o_c) = \tfrac{A_c}{\sqrt2}\sqrt{r^2 - 2r\cos\Delta + 1},$$
amplitude-only $\tfrac{A_c}{\sqrt2}\lvert r-1\rvert$, phase-only $\tfrac{A_c}{\sqrt2}2\lvert\sin(\Delta/2)\rvert$. **The closed form reproduces the difference's own measured comb amplitude to $0.00\%$ pointwise** — the decomposition is an *identity*, so the licence gate passes exactly.

| quantity | band-1 departure, four bases | verdict |
|---|---|---|
| BOTH (the surviving step) | $-0.204$ … $-0.236$ | **STEP** |
| **AMPLITUDE only** | $-0.227$ … $-0.260$ | **STEP** |
| PHASE only | $+0.570$ … $+0.796$ | step, *opposite sign* |
| raw band std (`cc66.59`) | $-0.450$ … $-0.454$ | **STEP** |

At band 1 the amplitude limit supplies $0.958$ of the statistic against phase's $0.284$. ⇒ ***The surviving step is a WEAKENING of the first acoustic cycle, not a DISPLACEMENT of it.***

⚠ **But the phase channel is unresolved, not merely small — the pre-registered trade-off fires.** Its departure runs $+3.54$, $+0.66$, $-0.46$ across window half-widths $0.55/0.75/0.95$ and **changes sign**, where the amplitude term's sign does not move. The reason is size: the relative phase is $0.0068$ rad ($0.39°$) against a relative amplitude of $0.0554$. ⇒ **Amplitude on the sign, inseparable on the share** — and what would separate them is a phase read against the comb itself over a longer lever arm in $q$, not a local fit in a window one period wide.

⚠⚠ **A CORRECTION TO `cc66.59` THAT THIS FORCED.** A band spans $0.70$ in $q$ against a comb period of $1.00$, so **a raw band `std` samples less than one full cycle and is phase-dependent by construction**. The step is $-0.45$ on that route and $-0.22$ on the phase-insensitive held-period one. **Both carried, neither chosen; the step survives on both**, and `cc66.59`'s size is the larger of the two.

### ⓶ THE SHARES DO NOT SURVIVE THE CHANGE OF DENOMINATOR

Each knob read as its own $\operatorname{std}(o_{\rm knob}-o_{\rm lcdm})$, against the arm's:

| channel | on the ratio-of-contrasts | on the DIFFERENTIAL | sign vs the arm |
|---|---|---|---|
| window weighting | wrong sign | $+1.05$ … $+1.32$ | **OPPOSITE** |
| term mix | $63\%$ | **no longer a step** | same |
| JOINT (realised pair) | $42\%$ | **zero within its scatter**, sign flips | — |

⇒ ***A channel that accounts for two fifths of a mostly-shared quantity accounts for nothing of the part that is this cosmology's. The row's candidate accounting was scored against the wrong object.***

### ⓷ THE STEP DOES NOT COMPOSE THE WAY THE CONTRAST DOES

`cc66.49` measured the **contrast** composing multiplicatively — product 7 of 7, sum 0 of 7. On the **step**:

| rule | predicts | residual |
|---|---|---|
| product $(1+d_w)(1+d_m)-1$ | $+0.843$ | $6.1\times$ the joint's scatter |
| sum $d_w + d_m$ | $+1.028$ | $7.4\times$ |
| quadrature | $+1.195$ | $8.6\times$ |

against a **measured** $-0.014$. ⇒ **No rule fits.** All three predict a large positive departure where the realised pair measures zero. ***The two knobs very nearly cancel on the step where they multiply on the contrast*** — a new property of the step.

⌗ Residuals are in departure units against the joint's own scatter, **not** as a percentage: its departure is consistent with zero, and a percentage of a near-zero measurement would be meaningless — this line's own denominator guard turned on itself.

### THE DISCIPLINE THIS REVISION ADDS

⚠ ***A BAND NARROWER THAN THE PERIOD IT MEASURES MAKES ITS OWN STATISTIC PHASE-DEPENDENT.*** Bands are $0.70$ of a comb period, so a band `std` samples an incomplete cycle; the held-period amplitude does not.
⚠ ***AN IDENTITY IS NOT A FIT, AND SAYING WHICH ONE YOU HAVE IS THE GATE.*** The decomposition reproduces the measured quantity to $0.00\%$ because it is algebra, and that is why the separation is exact rather than modelled.
⚠ ***A PERCENTAGE OF A NEAR-ZERO MEASUREMENT IS NOT A SHARE.*** When the denominator is consistent with zero, quote the residual in the measured units against the scatter.

## ⛭⛭⛭ `cc66.61` — `r7019` FILLED: **NO STATISTIC THIS CONSTRUCTION CAN BUILD** RESOLVES THE TWO CHANNELS; THE PHASE STEP **DIES ON A MATCHED-WIDTH CONTROL**; AND THE CANCELLATION IS **AGGREGATION-DEPENDENT**

**Receipt** `receipts/P15_CR_cosmology/P15_no_statistic_this_construction_can_build_resolves_the_two_channels_and_the_phase_step_dies_on_a_matched_width_control.py` — **22 gates, `GATES: ALL PASS`**, 0.7 s. Pre-registration is its own commit ahead of the working script `resolving_power.py`. Nothing solved, nothing run, no corpus edits.

### ⓵ THE FLOOR DOES NOT MOVE — AND THAT IS `PO-56`'s TERMINAL CONDITION

The **minimum resolvable share** $f_{\min} = 2\sigma/\lvert d_{\rm arm}\rvert$ is the smallest fraction of the step a channel could carry and still be decided.

| route | $\lvert d_{\rm arm}\rvert$ | $\sigma$ | $f_{\min}$ |
|---|---|---|---|
| raw, 7 bands, per common $q$ | 0.4525 | 0.1473 | 0.65 |
| held, 7 bands, per common $q$ | 0.2201 | 0.0696 | **0.63** |
| raw / held, per common $\ell$ | 0.4522 / 0.2199 | 0.1473 / 0.0695 | 0.65 / 0.63 |
| raw / held, 8 bands to $q = 6.45$ | 0.4404 / 0.2440 | 0.1369 / 0.0724 | 0.62 / **0.59** |
| raw / held, 12 finer bands | — / 0.2224 | — / 0.0835 | — / 0.75 |

⇒ ***The term mix carries $0.35$ of the step and the realised pair $0.03$, against a floor of $0.59$. They cannot be resolved by any statistic this construction can build.***

⌗ **And the reason is what the pre-registration did not expect.** The held-period aggregation lowers $\sigma$ by $2.12\times$ *exactly as predicted* — **and lowers the signal by $2.06\times$ at the same time**. $f_{\min}$ moves only $0.65 \to 0.63$. *The candidate named in advance as the one expected to help most does not help.*

⛔ **And the pre-registered abuse hazard fires before any power claim can be made:** the term mix and the realised pair **change sign** between the two aggregations, so their departures are not established at all. Only the window channel keeps its sign on all eight readings.

### ⓶ THE PHASE IS RESOLVED WHERE IT IS NOT NEEDED AND NOT WHERE IT IS

| | value |
|---|---|
| upper range, 4 full-period stretches | $+0.007368 \pm 0.000974$ rad ($+0.42°$, $7.6\sigma$) |
| whole upper range as one stretch | $+0.007541$ rad |
| band 1 ($0.70$ of a period) | $-0.002440$ rad |
| matched-width control, 6 stretches of $0.70$ | mean $+0.008575$, scatter $0.007264$ — **$3.7\times$ larger** |

On the full-period yardstick band 1 is $5.03$ scatters out. ⛔ **But that yardstick is wrong**: a projection over a *non-integer* number of periods leaks the baseline into $C$ and $S$, so a narrow stretch is both noisier *and* biased.

⇒ ***Band 1 sits $1.52$ scatters out, not $5.03$. The phase step is NOT resolved, and `cc66.60`'s amplitude verdict stands as the complete one rather than the sign-only one.***

⌗ The method reaches a $13\%$ measurement over five periods and cannot bring it to the one band that needs it — **the same structural limit in a third disguise**, after `cc66.58`'s window-free family and `cc66.60`'s trade-off.

### ⓷ THE CANCELLATION IS AGGREGATION-DEPENDENT

The joint's departure over its own scatter, four bases each: **raw** $0.24$–$0.54\sigma$ (consistent with zero on all four); **held** $4.16$–$4.98\sigma$ (on none). ⇒ **So ⓷ inherits ⓵'s answer rather than choosing a word** — the third possibility the pre-registration named — and constraint-versus-coincidence cannot be settled here. What it would be cancelling between is large either way: the two singles sum to $+0.895$ (raw) and $+1.149$ (held).

### THE DISCIPLINE THIS REVISION ADDS

⚠ ***A REDUCTION IN SCATTER IS ONLY A GAIN IF THE SIGNAL DOES NOT FALL WITH IT.*** The held-period aggregation halves both; $f_{\min}$ is the invariant and it does not move.
⚠ ***A NARROW-WINDOW MEASUREMENT NEEDS A MATCHED-WIDTH CONTROL, NOT THE WIDE-WINDOW ERROR BAR.*** It turned $5.03\sigma$ into $1.52\sigma$ here, and the difference is the whole finding.
⚠ ***"UNRESOLVABLE" IS A STATEMENT ABOUT THE INSTRUMENT AND MUST BE PROVED OVER ITS WHOLE REACH*** — every route banked, not the one to hand.

## ⛭⛭⛭ `cc66.62` — `r7021` FILLED: THE LIKELIHOOD **SEES THE STEP AND SEPARATES THE TWO CHANNELS**, SO THE DEMONSTRATION DOES NOT COVER IT AND `PO-56`'s AMENDED CLAUSE IS **NOT MET**

**Receipt** `receipts/P15_CR_cosmology/P15_the_likelihood_sees_the_step_and_separates_the_two_channels_so_the_demonstration_does_not_cover_it.py` — **19 gates, `GATES: ALL PASS`**, 0.5 s. Pre-registration is its own commit ahead of the working script `does_the_likelihood_see_it.py`. Nothing solved, nothing run, no corpus edits.

### ⓵ⓐ THE LIKELIHOOD IS NOT A BANDED STATISTIC IN DISGUISE

`plik_lite` TT bins at a median $0.0298$ in $q$ — **one thirty-fourth of a comb period** — with **24 bins inside band 1**, and its bin-to-bin correlation is a flat $\approx 0.15$ floor rather than a coupling that grows over a period. *It bins; it does not **band**, in the sense that defeats every statistic in the demonstration.*

⌗ That structure was inspected **before** the pre-registration was written — bin edges, widths and covariance are properties of the instrument fixed on disk regardless of any spectrum — and the pre-registration says so and declares the branch settled rather than tabling it as if open.

### ⓵ⓑ THE STEP IS A LOCALISED CONTRIBUTION TO ITS EXCESS

| band | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| σ of arm-vs-control from that band alone | **36.4** | 42.8 | 49.8 | 44.6 | 35.1 | 24.6 | 14.2 |

Whole covered range together: $98.9\sigma$. Band 1 against its own bands 2–7 trend: $-0.311$ … $-0.489$ across the four bases, at $2.5$–$3.2\sigma$ of its own residual. The trend predicts $53$–$71\sigma$ at band 1 where the likelihood delivers $36.4$.

⇒ **The same sign as every other instrument in this row — and the first per-band number in it that carries the instrument's own noise rather than an empirical scatter across a noiseless theory spectrum.**

### ⓵ⓒ AND IT SEPARATES THE TWO CHANNELS AT BAND 1

| | σ at band 1 |
|---|---|
| window vs control | 6.61 |
| term mix vs control | 18.64 |
| JOINT vs control | 12.82 |
| the ARM vs control (the target) | 36.37 |
| **window vs term mix** | **25.11** |

⇒ ***So `cc66.61`'s demonstration covers the statistic family and not the instrument the paper runs beside it. `PO-56`'s amended clause is NOT met, and the row has a measurement to make rather than an exit to take.***

⚠ **The two floors are in different units**, which the pre-registration required be said before the numbers were in hand: the likelihood's smallest detectable share at band 1 is $0.055$ of the band-1 **difference** under *real instrument noise*; `cc66.61`'s $0.59$ is a share of the **step** under an *empirical scatter of a noiseless spectrum*. **Neither bounds the other.** The legitimate comparison is the one the order asked for: the statistic family cannot separate the channels at band 1; the likelihood separates them at 25σ.

### ⓶ THE SCOPE STATEMENT THE CLAUSE NEEDS

Of the **eleven** instruments this row has ever made a claim on, **eight band** at $0.70$ of a comb period — the contrast statistic, the held-period amplitude, the window-free depth, the extremal envelope, the differential estimator, the bilinear decomposition read through the band statistic, the comb-phase projection, and the projection-width kernel. **Three do not:**

* the **anchored peak/trough locator** (`cc66.45/46`) — does not band, but makes **no amplitude claim at band 1**: it locates peaks;
* **`plik_lite` TT**, the likelihood;
* the **refit $\chi^2$ and its derivative grid**, which use the same bins.

⇒ **So the likelihood and its refit are the only instruments in this row that both avoid the band-width limit *and* make an amplitude claim at band 1** — which is why ⓵ was the right question, and why there is no third instrument outside the demonstration.

### THE DISCIPLINE THIS REVISION ADDS

⚠ ***AN INSTRUMENT THAT BINS IS NOT NECESSARILY AN INSTRUMENT THAT BANDS.*** The limit is the ratio of the averaging width to the period, not the presence of bins.
⚠ ***SAY WHICH FACTS WERE IN HAND BEFORE THE PRE-REGISTRATION WAS WRITTEN.*** Instrument structure is fixed on disk and looking at it is legitimate; presenting a settled branch as open is not.
⚠ ***A FLOOR UNDER NOISELESS STRUCTURE AND A FLOOR UNDER INSTRUMENT NOISE ARE NOT ONE NUMBER.*** Compare the verdicts, never the figures.

## ⛭⛭⛭ `cc66.63` — `r7023` FILLED: BAND 1 CARRIES **UNDER ONE PER CENT** OF THE LIKELIHOOD'S EXCESS AND ITS CONTRIBUTION **CHANGES SIGN**; `cc66.62`'s LABEL IS **CORRECTED**; AND IN THE METRIC THE STEP DOES LIVE IN, **ALL THREE CHANNELS DEPART THE ARM'S WAY**

**Receipt** `receipts/P15_CR_cosmology/P15_the_band_one_departure_is_not_in_the_likelihoods_excess_and_all_three_channels_match_it_in_separating_power.py` — **21 gates, `GATES: ALL PASS`**, 0.5 s. Pre-registration is its own commit ahead of the working script `score_in_the_metric.py`. Nothing solved, nothing run, no corpus edits.

**The order's distinction is this revision's vocabulary, not an acknowledgement:** *separating power* is the instrument's ability to tell two candidate spectra apart at a band; *significance* is the size of a departure against its own trend. **No quantity below divides one by the other**; every share is a ratio of two significances.

### ⓶ RUN FIRST, BECAUSE IT DECIDES WHAT ⓵ MEANS — AND THE ANSWER IS NEITHER OUTCOME TABLED

| $n$ (free coefficients in $\ln\ell$) | total excess | b1 | b2 | b3 | b4 | b5 | b6 | b7 |
|---|---|---|---|---|---|---|---|---|
| 1 *(the single amplitude)* | 322.0 | **+2.6** | 12.3 | 26.0 | 67.5 | 77.7 | 61.2 | 39.8 |
| 2 | 317.6 | **−0.5** | 16.4 | 22.8 | 75.2 | 79.0 | 64.1 | 41.5 |
| 3 | 327.4 | **+0.3** | 16.2 | 20.7 | 72.9 | 74.3 | 66.4 | 38.8 |
| 4 | 314.8 | **+6.6** | 12.4 | 25.1 | 69.4 | 81.4 | 63.6 | 41.7 |

Band 1 contributes **2.6 of the 287** the seven bands sum to — **0.9%** — against a total excess of 322 over all covered bins. **It changes sign** as smooth global shape is absorbed, where bands 2–7 hold to within a few per cent.

⇒ ***So band 1's departure is not a distinct feature of the residual, and it is not the shape rejection read locally either — the shape rejection is barely present there at all.*** It lives at bands 4–7, which carry **86%** of the per-band excess.

### ⛔⛔ AND THAT FORCES A CORRECTION TO `cc66.62`, WHICH IS THIS SEAT'S

`cc66.62` ⓵ⓑ was headed *"THE STEP IS A LOCALISED CONTRIBUTION TO ITS EXCESS"* and then reported band 1's **separating power** — 36.4σ against a trend predicting 53–71.

**The number was right and the label was wrong.** The likelihood *does* see a band-1 departure, in its power to tell models apart; it does *not* carry a band-1 excess. Those are different sentences and `cc66.62` ran them together — one revision after 66 drew the distinction, and one before it bit.

### ⓵ IN THE METRIC THE STEP ACTUALLY LIVES IN, ALL THREE CHANNELS DEPART THE ARM'S WAY

| channel | four bases | share of the arm's | significance |
|---|---|---|---|
| **window** | $-0.493$, $-0.448$, $-0.584$, $-0.514$ | **1.31** | 2.7–3.6σ |
| **term mix** | $-0.325$, $-0.244$, $-0.459$, $-0.336$ | 0.86 | 2.2–2.4σ |
| **JOINT** | $-0.206$, $-0.100$, $-0.343$, $-0.184$ | 0.51 | 0.6–1.9σ |
| *the ARM* | $-0.373$, $-0.311$, $-0.489$, $-0.394$ | 1.00 | 2.5–3.2σ |

⇒ ***The first time this row has had candidates that depart the same way as the arm on an instrument that can carry the question.***

⚠ **And the window channel, which went the *wrong* way on the differential estimator, goes the right way here and over-delivers** — a different verdict on a different instrument, reported as that rather than smoothed.

**The cancellation is measured rather than read off** the 12.82-against-18.64 the order flagged: product predicts $-0.677$, sum $-0.851$, quadrature $-0.613$, against a measured $-0.208$. **No rule fits** — the realised pair delivers **34%** of the closest, 2.4 of its own residual away. The two knobs partly cancel here as they did on the differential estimator.

### ⚠⚠ AND WHAT ⓶ DOES TO ⓵ — THE WHOLE REASON IT WAS RUN FIRST

These are shares of a **separating-power** departure. A channel matching the arm there is matching a feature that carries **one per cent of the likelihood's excess**. ⇒ **So this is not yet "a candidate produces the step" in the sense `PO-56`'s strong clause needs**: a real match in a real metric, and the wrong metric for the clause.

### THE DISCIPLINE THIS REVISION ADDS

⚠ ***A LABEL IS A CLAIM.*** `cc66.62`'s number was right and its heading named a different quantity; that is a correction, not a rewording.
⚠ ***WHEN ONE ITEM DECIDES WHAT ANOTHER MEANS, RUN IT FIRST AND SAY SO IN THE FILE'S STRUCTURE.***
⚠ ***A DEPARTURE THAT CHANGES SIGN AS NUISANCE FREEDOM IS ADDED IS NOT A FEATURE OF THE RESIDUAL*** — and the control is the rate against the other bands, since more freedom always shrinks a residual.

## cc66.64 — the cost at bands 4–7: what accounts for it, and has it any structure

**Order `r7025`, two items.** *Pre-registration its own commit ahead of the working script.*

### The estimator, corrected first

`cc66.63` read per-band excess by inverting each band's covariance block alone; its contributions
summed to **287 against a total of 322**. Since $r_a = r_c - d$,

$$\chi^{2}(a)-\chi^{2}(c) \;=\; d^{T}Fd \;-\; 2\,d^{T}Fr_c$$

whose per-bin terms sum to the excess **identically** — reproduced to $1.7\times10^{-13}$.

⌗ *The split is not bookkeeping. The first term is the separating power; the second is the only
part that knows where the data sits. **`cc66.63`'s finding is that algebra.***

| | bands 4–7 share of the banded excess |
|---|---|
| exact decomposition | **87%** |
| `cc66.63` block-inverted | 86% |

⇒ ***The location holds. This corrects the instrument, not the result.***

### ⓶ — featureless and combed at once

82 bins across bands 4–7, median spacing 0.0298 in $q$ against a comb period of 1.00.

| tested against | scatter explained |
|---|---|
| a constant | **+0.0%** |
| a trend in $\ln q$ | +1.6% |
| a quadratic in $\ln q$ | +2.8% |

*`cc66.58`'s verdict survives every smooth shape at the finer scale.* **But the acoustic-comb
projection gives 7.30 against a null of 2.53 built from 110 wrong periods — not one of which
returns more — and the scan's own maximum sits at period 1.01.**

⇒ ***So `cc66.58`'s "featureless" was a property of the BANDING.*** *Seven numbers cannot see a
modulation at the period they are 0.70 wide against; 82 bins at a thirty-fourth of it can.*

⛔ **And the control that makes it a result.** *$d$ is itself a comb, so a comb in the excess could
be an artefact of the model difference.* Split: **6.24 in $-2d^{T}Fr_c$ against 1.08 in $d^{T}Fd$**
— five sixths from the term that knows where the data sits. ⇒ ***A fact about the data.***

⚠ *And the prediction that the quadratic term would enter at period 1/2 did **not** hold cleanly —
0.57 there against 1.08 at 1.00. $d$ is not a pure sinusoid and its envelope varies. Reported as it
measured.*

### ⓵ — the shares, and the control they were uninterpretable without

| channel | share 4–7 | across $n=1..4$ | corr with arm | regression | left over |
|---|---|---|---|---|---|
| window | 0.14 | 0.13–0.18 | **−0.70** | −0.12 | — |
| term mix | **1.36** | 1.28–1.42 | **+0.70** | 0.74 | **45%** |
| JOINT | 1.53 | 1.47–1.63 | +0.46 | 0.62 | 59% |

⛔ *Any spectrum that is not the control costs something, so a share above one may mean only "also
rejected" and not "rejected the same way." **The per-bin pattern is what decides.***

* **The window is ANTI-correlated with the arm.** *Its 0.14 is not a small share of the arm's cost
  — it is a different cost.*
* **The term mix is the first channel this row has produced that costs something where the
  likelihood actually rejects the arm** — 1.41, 1.07, 0.76 across bands 4, 5, 7.
* **The JOINT matches worse than the term mix alone.** *Adding the window raises the total and
  degrades the pattern — the sharpest statement available that a total is not a match.*

⇒ ***THE AMENDED CLAUSE IS NEITHER MET NOR DISCHARGED, AND IS NOT ROUNDED EITHER WAY.*** *A channel
producing 136% of the cost at $r=+0.70$ is not "no quantity"; a channel misplacing 45% of its cost
is not "the carrier identified."*

### ⚠⚠ And the cancellation is absent, which goes against this row's story

*Twice elsewhere the pair delivered a fraction of its singles, and it was called beginning to look
like a property.* **On the excess: singles sum to 1.4965, the realised pair gives 1.5305 — 102%.**

⇒ ***THE KNOBS ADD HERE. CANCELLATION IS A PROPERTY OF THE METRIC, NOT OF THE PAIR.***

⚠ *Band 6 is where the arm is cheapest (14.6 against 80, 80, 123), so every channel's share there
has a small denominator and it is never quoted alone.*

## cc66.65 — the measurement that joins cc66.64's two findings

**Order `r7029`, one item plus a small one.** *Pre-registration its own commit ahead of the working script.*

### The gap, and why ⓑ could not answer it

`cc66.64` measured the **correlation on per-band shares** and the **modulation on per-bin structure**. Those
were not yet statements about the same object: a channel can carry the cost in exactly the right four bands
and be smooth inside every one of them.

⛔ **And `ⓑ` cannot close it, which the pre-registration stated before the run.** A one-coefficient
regression's fitted part is a scalar multiple of one of its inputs, in either orientation:

| orientation | fitted part | predicted amp | measured |
|---|---|---|---|
| A — channel on arm (`cc66.64`'s) | $\beta\,e_{\rm arm}$ | $0.7435 \times 7.304 = 5.4304$ | **5.4304** |
| B — arm on channel | $\gamma\,e_{k}$ | $0.8033 \times 4.238 = 3.4044$ | **3.4044** |

⇒ ***Both exact to the digit, so `ⓑ` carries nothing its input did not — and since `ⓑ` is $\gamma \times$
`ⓐ`, the order's fork collapses to one question: is the term mix's own cost combed?***

### ⓶ — it is not, and the modulation survives where no channel accounts for it

| quantity | amp | null μ | null max | # of 110 over | phase − arm |
|---|---|---|---|---|---|
| the ARM excess (reference) | 7.304 | 2.528 | 5.561 | 0 | +0.00 |
| **ⓐ term mix own cost** | **4.238** | 2.030 | 4.297 | **1** | — |
| ⓒ A: the 45% it misplaces | 1.482 | 2.793 | 3.188 | **110** | — |
| **ⓒ B: what it does NOT explain** | **4.005** | 3.034 | 3.889 | **0** | **−0.16** |

⇒ *** `ⓒ` COMBED AND `ⓑ` NOT — `PO-56`'s TERMINATING ROW. ***

⚠ **The one reading that says DISCHARGES is orientation A taken literally** — its `ⓑ` is $\beta \times$ the
arm's own 7.30 and its `ⓒ` is a different object. *That exit rests entirely on the amplitude gated as
arithmetic in advance. Strip it and both orientations say the same thing.*

⛔ **Not decisive and not reported as decisive.** *`ⓐ` fails by one period of 110; `ⓒ` clears by a comparable
margin; the bar is a null **maximum** over correlated periods and is deliberately conservative.*

### The self-similarity artefact, killed again for the channel

| | amp | null max | clears |
|---|---|---|---|
| arm $d^{T}Fd$ | 1.083 | 0.856 | yes |
| arm $-2d^{T}Fr_c$ | 6.241 | 4.791 | yes |
| term mix $d^{T}Fd$ | 0.851 | 0.907 | **no** |
| term mix $-2d^{T}Fr_c$ | 3.399 | 3.728 | **no** |

*The channel is combed in neither term, so there is no "channel looking at itself" to discount.*

### ⓷ — the window is combed in antiphase, but not one structure with two signs

**Own cost 2.010 against a null max of 1.711, none of 110 above, at +3.12 rad from the arm's — π to within
0.02.** *So not a smooth offset: a modulation at the same period, opposed.*

⛔ **The blunt test of "one structure, two signs" fails:** $\alpha = -0.0587$ with the residual keeping 98% of
the window's power; the amplitudes that follow miss by a factor of five.

⌗ *But that is the **wrong instrument** — a ratio over whole vectors asks whether the window **is** the arm
scaled, where the question is about each one's **modulated part**. `cc66.60`'s aggregation error had exactly
this shape.* ⇒ Like-for-like, projecting the two spectrum differences:

| | amp | null max | # over | phase − arm |
|---|---|---|---|---|
| $d_{\rm arm}$ | 5.491e−05 | 4.542e−05 | 0 | +0.00 |
| $d_{\rm window}$ | 1.448e−05 | 1.221e−05 | 0 | **+0.27** |

**In phase, at a ratio of 0.264 — and $0.264 \times 6.241 = 1.646$ against a measured 1.893.**

⇒ *** THE MAGNITUDE COMPOSES AND THE SIGN DOES NOT. The reversal appears only after the likelihood's own
weighting. *** ⌗ *That locates the sign flip. It does not explain it, and naming why would be a mechanism.*

## cc66.66 — the same three projections against the null 70 validated

**Order `r7033`, one re-run plus a routed finding.** *Pre-registration its own commit ahead of the working
script. The measurement is unchanged; only the bar changed, and the bar was mine.*

### What 70's audit established

| | |
|---|---|
| bins across bands 4–7 | 82, spanning $T = 2.78$ in $q$ |
| independent frequencies the range holds | **≈ 3.6** |
| $N_{\rm eff}$ of the 110-period ensemble | **3.07** |
| of the 110, correlating with the comb above 0.5 | 6 (max 0.64) |

⇒ ***"None of 110" was worth roughly one in four.*** ⌗ *I flagged the margin as thin and asked for this
audit. I did not work out that 82 bins over $T = 2.78$ can only hold about 3.6 independent frequencies —
and that, not the arithmetic gate I was pleased with, was the weak part of `cc66.65`.*

### The gate: is this 70's instrument?

| | this seat | 70 |
|---|---|---|
| arm's comb amplitude | 7.3038 | 7.304 |
| draws of 2,000 reaching it | **0** | **0** |
| null maximum | 2.34 | 2.54 (another seed) |

### ⓵ — all three clear

| quantity | amp | null med | null max | # ≥ amp | $p$ | margin |
|---|---|---|---|---|---|---|
| **ⓐ term mix own cost** | 4.238 | 0.839 | 1.874 | **0** | ≤0.0005 | 2.26× |
| **ⓑ arm excess it does NOT explain** | 4.005 | 0.681 | 1.416 | **0** | ≤0.0005 | 2.83× |
| **ⓒ the 45% it misplaces** | 1.482 | 0.451 | 1.029 | **0** | ≤0.0005 | **1.44×** |

⇒ *** `ⓐ` CLEARS, SO `cc66.65`'s CENTRAL READING — "the term mix's own cost is NOT combed" — IS WRONG. ***
*It failed the old bar by **one period of 110**, and the pre-registration said in advance that a bar worth one
in four failing something by one unit is equally capable of passing it.*

**And `ⓐ`'s clearance is not the noise-free term talking.** Under this null $d$ is fixed and only $r_c$ moves:

| ⓐ's term | amp | null | reading |
|---|---|---|---|
| $d^{T}Fd$ | 0.851 | $0.794 \pm 0.006$ | **noise-free — no evidence** |
| $-2d^{T}Fr_c$ | 3.399 | median 0.354, **0 of 2,000** | **a real test, and it passes** |

*The held-coefficient variant agrees on both fitted quantities, so none of the clearance is the regression
chasing noise.*

⇒ **The measured row is "both"** — `ⓐ` clearing reads as DISCHARGES and `ⓑ` clears too. *At this bar the
projections no longer separate and the fork as posed does not discriminate. Reported, not chosen between.*

⚠ **And the old bar was not merely weak, it was inflated.** *Its maxima ran 3.2–4.3 where this one's run
1.0–1.9: the wrong-period amplitudes were carrying the signal itself, leaked.* ⇒ ***A null built from the same
data at neighbouring frequencies is not independent of the feature it is scoring.***

### ⓶ — `cc66.62`'s scope claim, amended

Band 1 is $q \in [0.85, 1.55)$.

| anchor | $q$ | inside band 1? |
|---|---|---|
| peaks 1–4 | 0.736, 1.778, 2.703, 3.751 | **none** |
| **trough 1** | **1.360** | **yes** |

*`C17_the_instrument_already_carries_both` states the instrument carries "acoustic peak **and trough**
positions", so the peak-only reading would have been a dodge.* ⇒ ***70's factual claim is correct.***

**The qualifier:** `anchored()` returns $-c_1/2c_0$, a vertex **position**, never a height. *So the claim
survives in substance but was carrying an implication it had not earned — that the instrument does not reach
band 1 at all.* ⇒ ***It LOCATES inside band 1 and MEASURES no height there.***

## cc66.67 — the accounting: it closes, and it cannot attribute

**Order `r7035`.** *`r7033`'s fork withdrawn by 66 as its own defect — a detection test asked of an authorship
question. Pre-registration its own commit ahead of the working script.*

### Gate — `cc66.65`'s window numbers reproduce to the digit

| | measured now | `cc66.65` |
|---|---|---|
| phase offset | +0.270 rad | +0.27 |
| amplitude ratio | 0.2638 | 0.264 |
| prediction vs measured | 1.646 vs 1.893 | 1.646 vs 1.893 |

### ⓐ and ⓑ — the ratio, and the hinge

| channel | spectrum-level phase − arm | ratio | predicted | measured | error |
|---|---|---|---|---|---|
| window | +0.27 | 0.264 | 1.646 | 1.893 | **13%** |
| **term mix** | **+0.383** | **1.176** | **7.341** | **3.399** | **116%** |

⇒ ***The scale `r7035`'s template was built on does not carry over to this channel.***

### ⓒ — the accounting closes, on both scales

| scale | $k$ | contribution | residue | share | closes? |
|---|---|---|---|---|---|
| spectrum-level ratio | 1.176 | 4.985 | 2.570 | **68.3%** | exact |
| least-squares projection | 1.694 | 7.181 | 1.335 | **98.3%** | exact |

*Naive amplitude ratio 58.0% at a phase offset of +0.18 rad — the gap between naive and vector is the phase
doing work, and it is reported rather than hidden.*

### ⛔ And the second scale is an identity

In a two-dimensional $(\cos,\sin)$ plane, $k = (v_a\!\cdot\!v)/(v\!\cdot\!v)$ gives
$|kv| = |v_a\!\cdot\!v|/|v| = |v_a|\,|\cos\Delta|$, so

$$\textbf{share} = |\cos\Delta| \quad \textbf{exactly}$$

| channel | $\Delta$ | $\lvert\cos\Delta\rvert$ | measured share | $k$ |
|---|---|---|---|---|
| term mix | +0.184 | 0.9832 | **0.9832** | +1.694 |
| **window** | **+3.121** | **0.9998** | **0.9998** | **−3.633** |

⇒ ***It depends only on the phase offset and not at all on the channel's amplitude.*** ⇒ ***And the window is
the proof: in antiphase it scores 100.0% of the authorship, at a negative scale that turns its cost upside
down to get there.***

**So both scales are out, each for its own reason and neither failure the other's:** the spectrum-level ratio
by **measurement** (ⓑ, a factor of two), the least-squares projection by **algebra**.

⚠ *Two channels together span the plane and reconstruct the arm exactly, residue 0.000 — arithmetic, not
attribution, and printed to be discounted.*

### ⇒ The third row

***`PO-56` TERMINATES on the stated ground that no instrument this construction has can attribute the
modulation.*** *`r7035` calls that the terminal state itself and also a result. No fourth row was reached for.*

## cc66.70 — the acceptance: what moves it, what cannot move it, and how far it moves

*Measurements only. The law itself is `cc66.70`'s first receipt; this is the convergence side of it, taken up
because `r7049` observed that $A_\ell$ is a sharper probe than the height ratios **and** that it had become
free — `GRIDSAVE` writes the background $A_\ell$ needs in $1.45$ s per configuration without computing a
spectrum at all. Receipt:
`P15_CR_cosmology/P15_the_acceptance_does_not_move_under_refinement_and_three_of_the_twelve_axes_could_not_have_moved_it.py`,
`GATES: ALL PASS`, $347$ s.*

### ⛭ WHAT MOVES $A_\ell$, AND BY HOW MUCH — WORST SINGLE MULTIPOLE, NOT THE MEAN

*Nine of the twelve axis-arm pairs move at least one input $A_\ell$ is built from. Against `r6911`'s
$0.6\%$ floor, measured on a known injected contrast:*

| axis | arm `cr` | control `lcdm` | points |
|---|---|---|---|
| $k_{\max}$ via `KFAC` ($2.0\to4.0$) | $0.00001\%$ — $41163\times$ inside | $0.00007\%$ — $8343\times$ | four |
| the mode count `NK` | ⛔ **inert by construction** | $0.00000\%$ — $3083418\times$ | three |
| the $\eta$ resolution `NLOS` ($560\to2240$) | $0.00076\%$ — $786\times$ | $0.00137\%$ — $437\times$ | three |
| the $\eta$ half-width `NLOSW` ($6\to12$) | $0.00081\%$ — $739\times$ | $0.00147\%$ — $409\times$ | three |
| the $\eta$ split `NLOSF` | $0.00454\%$ — $132\times$ | $0.00817\%$ — $73\times$ | **two** |
| the reported $\ell$ grid `LSTEP` | ⛔ **inert by construction** | ⛔ **inert by construction** | two |

⇒ ***The largest excursion anywhere among the nine is $0.00817\%$, inside the floor by $73\times$.*** *The
**worst single multipole** is quoted throughout and not the mean over the range, because a mean can hide a
moving tail; the mean is $0.0000\%$ to four places on every axis and would have been the weaker claim.*
  ⚠ *`NLOSF` is a **two-point** axis and is not reported as converged: a two-point axis cannot turn over.
  The three-point and four-point axes are monotone at the $10^{-7}$ level, so the pre-registered verdict
  printed beside each of them is "inside the floor but the sequence has NOT turned over" — carried unaltered,
  and not loosened after the numbers were in.*

### ⛔ WHAT CANNOT MOVE IT — THREE OF TWELVE, AND THEY ARE TWO DIFFERENT THINGS

*`A_\ell` is built from the background alone — $\mathrm{vis}(\eta)$, $x_0(\eta)$, $k$, $\mathrm dk$,
$r_s^{*}$. An axis leaving all of those byte-identical cannot move it.*

**① `NK` on the arm.** *The arm's ladder is $\sqrt{L(L+2)}\,$stretch out to `KMAXL` and `NK` is only a
decimation cap never reached:* $1452$ modes at `base`, `nk15` and `nk20` alike, with `k`, `dk`, `eta`, `x0`
and `vis` equal under `np.array_equal` and under sha256. **Confirmed at the spectrum, not only at the grid:**
`real_cr_nk15_k0` and `real_cr_nk20_k0` against `real_cr_base_k0` at $\max|D_\ell| = 0.000\mathrm{e}{+}00$
with an identical $\ell$ list, and both injection forms equal on every array.
  ⛭ *And **the control moves** — $2547 \to 3822 \to 5094$ modes, $\max|D_\ell(\texttt{nk15}) -
  D_\ell(\texttt{nk20})| = 1.71\times10^{-1}$ — which is what makes the arm's silence a reading rather than
  a broken test.*

**② `LSTEP` on both arms.** *$A_\ell$ is read at the **same multipoles at every setting** by construction, so
the reported $\ell$ grid cannot enter it at all.* ⌗ *This one is a property of the **question**, not of the
arm — and it is the half that shows the test had to be general: a list of known-inert knobs would not have
contained it.*

### ⛭ THE NARROWING, AT EVERY SETTING, AGAINST AN INDEPENDENT ROUTE

| | |
|---|---|
| acceptance span, control | $5.1353$ ($5.1353$–$5.1360$ across twelve settings) |
| acceptance span, arm | $4.4663$ ($4.4663$–$4.4670$) |
| **arm narrower by** | $\mathbf{13.03\%}$ at **all twelve**, spread $0.0048$ percentage points |
| `r6919`'s independent $\mathrm dr_s/\mathrm d\chi$ reading | $12.8\%$ — $0.23$ pp apart |

⇒ *`r6919` reached $12.8\%$ by a route that computes no acceptance at all. The quantity the law's absolute
prediction rides on is therefore **stable across every numerical setting in the sweep** and agrees with an
independent measurement of the same physical narrowing.*

### ⛔ WHAT THIS IS NOT

***It is not `r7041`'s sweep and does not substitute for it.*** *The sweep asks what the **retention** and the
peak heights do, measured on spectra; this asks what the kernel's $k$-acceptance does, computed from the
background. **A converged acceptance with an unconverged retention would itself be a finding**, which is why
the two are reported apart — as this seat's own pre-registration required before either was read.* ⛔ *Nine
of twelve inside the floor is **not the row's convergence verdict**. And nothing here says which cosmology
is right.*

## cc66.72 — the sweep at full coverage: nothing moves it, and eleven of twelve readings are still not converged

**`r7041`'s convergence sweep finished at 10:53 on 2026-10-01: $158{,}885$ of $158{,}885$ modes, $66$ of $72$
configurations folding to a complete spectrum.** Two injection schemes (`fixed`, `sweepown`) $\times$ two arms
(`cr`, `lcdm`) $\times$ twelve settings $= 48$ runs, every one read.

| | |
|---|---|
| `fixed` band-RMS ratio | $1.0587$ at **every** setting of **every** axis |
| `sweepown` band-RMS ratio | $1.0659$–$1.0660$ |
| worst last step, all twelve readings | $\mathbf{0.008\%}$ against the pre-registered floor of $0.6\%$ — a factor of $73$ inside |
| `r6919`'s banked base points | $1.0587/{+}0.01189$ and $1.0659/{+}0.02260$ — **reproduced exactly** |
| readings reportable as **converged** | $\mathbf{1 \text{ of } 12}$ — `sweepown`/`NLOSW` only |
| the other eleven | seven *not turned over*, four *two points only* |

⛔ **STABILITY IS NOT CONVERGENCE AND ONLY THE FIRST IS CLAIMED.** The pre-registration: *a sequence that has not
turned over is not converged whatever its last step*, and monotonicity is undefined on two points. `sweepown`'s
`NLOSW` is the only sequence that reverses — $1.0659425 \to 1.0659377 \to 1.0659385$ — so it alone can be read as
having turned over. *A small last step is the cheapest way to look converged without being it.*

### ⛭ five axes on the arm, six on the control — and the run log is the evidence

`NK` is inert on the arm **by construction** (ladder $\sqrt{L(L+2)}\,$stretch to `KMAXL`, `NK` a decimation cap
never reached; byte-identical $k$ and $\eta$, $\max|D_\ell| = 0$), so its six arm configurations read
`inert: = _cr_base  NOT QUEUED` and never started; on the control it carries $2547 \to 3822 \to 5094$ modes.
`LSTEP` is the mirror: **real** for the sweep ($238 \to 475$ reported $\ell$) and **inert for the acceptance** on
both arms, as `cc66.70` ② recorded.
  ⌗ *The last two configurations in the sweep to finish were `real_lcdm_nk15` and `real_lcdm_nk20` — `NK` on the
  **control**. The asymmetry the verdict is gated against is in what the launcher queued.*

⚠ **The terminal state is $66$ of $72$, never $72$ of $72$** — $66$ queued plus the six inert. *A completion test
of "$72$ of $72$" cannot be met by this apparatus; coverage per cent is the clean criterion, since an inert row
carries no mode count and enters neither side of the sum.*

### ⛔ three instruments that answered with less state than their question needed

① **`report_c.py` opened whole-run `.npz` only.** Five configurations finished unsliced; sixty-one are tiled on
`KSLICE`. At **full** coverage the reader therefore called $39$ of $48$ runs *"not on disk yet"* and read two
points of one axis — a partial read of a complete sweep. It now loads through `fold.load`, the one authority on
both forms.
② **The receipt's fallback table, banked at $4$ dp, reported eight of twelve converged against the live path's
one** — the rule tests the **signs** of the steps, and points identical to $4$ dp round to differences of zero,
which read as a turn. Banked at full precision instead.
③ **The completion test itself** — see above. *Three in one revision, all the same shape.*

### ⌗ what it cost, and the apparatus findings

The container was reclaimed at essentially **every cycle for $\sim 11$ hours**, each reclaim killing **four
in-flight slices** redone from nothing; only the launcher's idempotence preserved what was banked. Slice width was
cut to **$100$ modes** so a slice can finish inside a container window. **This box has four cores**, so
`run_fast_job.sh` must never run while four solvers are live: its child gets $0$ s of CPU and fails on its own
$420$ s clock rather than on its content. *The three fold defects at `82de6bd9` are the standing record.*

### ⛔ WHAT THIS IS NOT

***Nothing here is a spectrum of the model*** — every run is the projection's transfer of a **known** analytic
oscillation (`SRCINJ`), comparable with neither a banked spectrum nor the sky. ***And the quantity is the
BAND-RMS RATIO, not "the retention"*** (`r7057`/`r7059`/`r7061`): about a **third** of the reported $+0.0139$ per
acoustic period is a phase drift between the two arms' *source* combs, which a band root-mean-square reads as
retention — *the rise survives; two thirds of its size does.* ***It is not `cc66.70`'s acceptance row*** — that
computes the kernel's $k$-acceptance from the background, this measures spectra. ⛭ *Node 70 audits first where
the verdict is read off a banded statistic, which this is. And nothing here says which cosmology is right.*

## cc66.73 — the projection read recombination 72 per cent away from the plasma's clock; one clock removes it and the swing survives

**`r7091`'s order, on Daryl's standing frame: when the model does not match the measured spectrum the
default hypothesis is that the MODEL does not faithfully implement what CR requires.** The defect is
real, it is large, and it is measurable from the backgrounds alone.

### ⛔ the defect, in closed form and with no spectrum

The instrument built its conformal-time grid from the **stacking** rate `Hphys`, and with it `a(eta)`,
$\eta_{\rm rec}$, $\eta_0$, $D_M$, `ETA_ON`, `ETA_END`, every spline's abscissa — and **the projection
kernel's own argument $x_0=\eta_0-\eta$** — while the acoustic phase (`sound_phase`), the perturbations
(`LEAFPERT`) and, under `LEAFSCALES=1`, the sound horizon all accumulate on the **leaf** rate.
  ⇒ *So $\Delta_\ell=\int S(k,\eta)\,j_\ell(k(\eta_0-\eta))\,\mathrm d\eta$ carried $S$ in one
  parametrisation of the history and $j_\ell$'s argument in another.*

| at the arm's refit best fit | stacking clock | leaf clock |
|---|---|---|
| $\eta_{\rm rec}$ | $485.5$ Mpc | $282.3$ Mpc |
| gap | | $\mathbf{41.8\%}$ |
| against the **control's** own $\eta_{\rm rec}=281.8$ Mpc | $\mathbf{72.3\%}$ out | $0.18\%$ out |
| $D_M=\eta_0-\eta_{\rm rec}$ | $14017$ Mpc | $13947$ Mpc ($-0.50\%$) |
| visibility peak, $\eta$ | $485.99$ | $282.34$ |
| visibility FWHM | $43.59$ Mpc | $38.38$ Mpc |
| hierarchy handover, $\eta$ | $307.1$ | $136.8$ |

⌗ **$D_M$ is what hid it.** $\eta_0$ moves with $\eta_{\rm rec}$ because radiation is negligible late,
so the clocks agree there and the difference cancels in $D_M$: **the gap is $84\times$ the move in
$D_M$.** *A reader watching $D_M$ calls a $42$ per cent inconsistency a half-per-cent effect.*

### ⛭ `LEAFGEOM=1` — the one clock assignment that had no knob

`LEAFPERT` moved the perturbation dynamics, `LEAFSCALES` the two scales, `PHASEONLY` the oscillator's
phase; **the time variable itself was reachable by nothing.** `LEAFGEOM=1` builds the grid on `Hleaf`,
so with `LEAFSCALES=1` and `LEAFPERT` every clock assignment is on the leaf. **The three consequences
are asserted at run time and the run refuses a spectrum otherwise:** `max|Jac-1| = 0` exactly,
`max|Phi2-1| = 0`, the two sound-horizon accumulators identical to $0$ Mpc.
  ⌗ Default off and **byte-identical**; the arm's default output is bit-identical, and on the **control**
  it is a provable no-op (`Hleaf` and `Hphys` character-identical there) **checked bit-level on the
  reporting path** rather than from reading the source.
  ⌗ *It does not collapse the arm onto the control: the arms differ three ways and this touches one —
  the arm keeps the handover initial data and the discrete $k$ ladder.*

### ⛭ the comb as an output and not a pinned input, onset held

$\ell_1/\ell_A$: $0.7290 \to 0.7326$ against the sky's $0.7312$ — **from $0.0022$ out to $0.0014$ out, a
factor $1.6$ closer, with nothing fitted to it** ($\ell_A$ $301.8\to300.3$; peaks $220,540,812,1132 \to
220,532,812,1124$ against $220.6,538.1,809.8$). ⛔ *And the heights move away:* P1/P2 $2.142\to2.080$ and
P1/P3 $2.173\to2.094$ against $2.217$ and $2.277$.

### ⛔⛔ the residual's shape — scored by the order's rule, and it does not flatten

| $\ell\le1040$, 104 bins | before | after |
|---|---|---|
| $\chi^2$, amplitude only | $266.7$ | $274.8$ ($+3.0\%$) |
| longest run of one sign | $16$ bins | $35$ bins |
| $\chi^2$, **+ a tilt** | $265.5$ | $\mathbf{215.0}$ ($\mathbf{-19.0\%}$) |
| worst excursion | $6.10\sigma$ | $4.12\sigma$ |
| rms residual | $1.59\sigma$ | $1.42\sigma$ |
| crossings | $36$ | $30$ |
| longest run | $16$ bins | $18$ bins |

**The fixed-parameter comparison is a tilt artefact**: at the old parameters the residual runs positive
unbroken from $\ell=100$ to $414$ and $\chi^2$ worsens, but the geometry moves $D_M$ and the visibility
width, so the best-fit parameters move with it — allow an amplitude and a power-law tilt and $\chi^2$
falls $19$ per cent. *The $35$-bin run was $n_s$ and not shape; the tilt the after wants is $-0.0324$
against the before's $-0.0046$, a prediction for the refit.*
  ⇒ ***And the swing still does not flatten: crossings $36\to30$, longest run $16\to18$ — the wrong
  direction on both. By the order's own rule this is not the fix.*** **The clocks are not the swing.**

⚠ **Not claimed:** the parameters are not refitted under the new geometry, so $-19$ per cent is a
two-direction marginalisation ($n_s$ is not a pure tilt in $\ell$). A real refit on the one-clock
geometry is a grid of runs and is not ordered.
⚠ **Found in passing and not this revision's doing:** the refit's own verified minimum `verify_cr.npz`
is no longer reproducible from the tree, $\max|\Delta D_\ell| = 7.14\times10^{-3}$; **the pre-patch code
differs from it by the same amount to every digit**, so the drift predates this build. Both sides of
every comparison above are same-revision runs.

## cc66.78 — `r7095` Q3: the licensed configuration moves neither statistic, and the swing was read above where it converges

**Receipt** `receipts/P15_CR_cosmology/P15_the_licensed_configuration_moves_neither_statistic_and_the_swing_was_read_above_where_it_converges.py` — 22 checks, all pass. Grids banked in-tree: `computations/beyond_the_wall/r7095_directions/grid_licensed` (nine arm runs at `ARM=cr HIER=1 LEAFREC=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 ZSTART=3e7`, control's nine copied from `refit_grid185`), `r7093_directions/grid_oneclock`, and `r7095_directions/lmaxl1300` (the pair `cc66.73` measured).

### The three configurations, same ell sampling, same control files

| | contrast `c` (arm) | crossings | longest run | mean abs extremum | chi2/bin | sum abs height dev |
|---|---|---|---|---|---|---|
| banked `refit_grid185` | −0.0636 ± 0.0085 (−7.5σ) | 30 | 18 | 1.353 σ | 3.05 | 0.068 |
| licensed `LEAFREC=1` | −0.0642 ± 0.0084 (−7.7σ) | 36 | 22 | 1.217 σ | 3.20 | 0.100 |
| forbidden `LEAFGEOM=1` | −0.0069 ± 0.0083 (−0.8σ) | 44 | 12 | 1.039 σ | 1.47 | 0.081 |

Shape statistics at `--lmax 1040 --tilt` through `r7091_directions/shape.py`; `c` through `r7093_directions/contrast_on.py`, which reproduces 70's published −0.0636 (arm) and −0.0075 (control) on the banked grid before any comparison. The control's `c` is identical across all three grids — its nine runs are the same nine files.

- **Licensed moves `c` by −0.08σ and |c| RISES 1%.** Longest run 18 → 22, chi2/bin 3.05 → 3.20, heights the worst of the three. It moves neither statistic.
- **Forbidden moves `c` by +6.70σ, |c| falling 89% onto the control's value**, with crossings 30 → 44 and the longest run 18 → 12.

### The convergence finding, which corrects cc66.73's inference

`cc66.73` reported crossings 36 → 30 and longest run 16 → 18 under the forbidden repair — the wrong way on both. That reproduces exactly on its own `LMAXL=1300` pair, so it was measured correctly. Read to ell ≤ 1040 it is 80% of that run's own reported ceiling against 52% of the `LMAXL=2000` run's; both hold `k_max = 2 l_max / D_M`.

Longest run of one sign against the read ceiling:

| | ell ≤ 700 | ell ≤ 800 | ell ≤ 900 | ell ≤ 1040 |
|---|---|---|---|---|
| banked | 8 | 8 | 15 | 18 |
| licensed | 9 | 9 | 13 | 22 |
| forbidden | 9 | 9 | 9 | 12 |

Below ell ≈ 800 all three are indistinguishable, so a reading taken there decides nothing. The discriminating feature lives above ell ≈ 850, where the banked default's longest run grows with the ceiling and the licensed configuration's grows faster while the forbidden repair's stays flat. **The correction is the ceiling, not the arithmetic**, and convergence is localised rather than reached — the scan stops at the grids' own `LMAXL=2000`.

### Two by-products of `LEAFREC`

- `LEAFREC=1` moved the spectrum (max rel 6.5%) and left `l_A`, `D_M` and `r_s` **bit-identical** to the banked run — `r6893+cc66.37`'s diagnostics finding confirmed again on a switch built after it.
- Its default being ON put three instrument-running receipts in conflict with numbers banked before the split. `C62`, `C63` and `P15_the_one_fitted_number_moves_the_scale_and_not_the_peak` now pin `LEAFREC=0` for the leg whose target predates it, with the reason in each file. `C62` measures the move rather than discarding it: recombination on its own rate takes the arm's diffusion scale from +7.55% to +8.37%, and the control's `r_D` is asserted bit-identical across the switch. Lifting those pins means re-measuring numbers `P15` quotes — routed to the gate, not done here.

## cc66.79 — `r7097` Q3: the licensed rebuild leaves all three rigidity numbers where they were; the forbidden one reaches the control's floor

**Receipt** `receipts/P15_CR_cosmology/P15_the_licensed_rebuild_leaves_all_three_rigidity_numbers_where_they_were_and_the_forbidden_one_puts_the_arm_on_the_controls_own_floor.py` — 13 checks, all pass. Measured through 70's own `rigidity.py` definitions (`build`, `W`, `STEP`, `stats`, `bestfit`), not re-implemented.

`r7097` named the three figures before the grid existed. On the banked grid they return exactly: unreachable chi2 278.8 on the arm against the control's 186.0 at n−5=180, crossings 54 against noise's 88±10.

| grid | arm | unreachable chi2 | crossings | longest run |
|---|---|---|---|---|
| all three | lcdm | 186.006575 | 87 | 8 |
| banked `refit_grid185` | cr | 278.795150 | 54 | 33 |
| **licensed** `LEAFREC=1`, `LEAFGEOM=0` | cr | **278.788424** | **54** | **33** |
| forbidden `LEAFGEOM=1` | cr | **184.988550** | **91** | **8** |

- **The licensed rebuild closes 0.007% of the 92.8 chi2 gap** and moves neither the crossings nor the longest run at all — on a rebuild that changed the spectrum by 6.5%.
- **The forbidden one closes all of it**: chi2 below the control's own 186.01, crossings 91 against the control's 87, longest run 8 — exactly the control's.
- The control's three numbers are identical across all three grids (its nine runs are the same nine files), which is the no-op saying what moved is the arm.

**60's falsifier fires**, and it was written unprompted and before the run: a rebuild consistent on all four assignments supplies no contrast correction of the named sign and size, which it said in advance means the rate assignments are not where the contrast comes from. But the one assignment the rule *forbids* supplies all of it, so the conclusion is sharper than the falsifier's wording: **the contrast comes from the clock the geometry is read on — the one object `P07` pins to the stacking rate by name.**

### The refit and the tilt prediction

Four-parameter refit (Nelder-Mead, closed-form amplitude), arm rows: banked `NS +0.0288` (chi2 301.2), licensed `NS +0.0422` (297.9), forbidden `NS −0.0035` (186.7, matching the control's 186.3).

The two-direction tilt `shape.py` fits and the refit's own `n_s` shift agree to better than 0.004 on all three grids at matched resolution, which is what licenses reading one as the other — checked rather than assumed. On that reading **`cc66.73`'s −0.0324 does not survive the resolution change**: it is that pair's own `LMAXL=1300` value, and the one-clock rebuild needs essentially no tilt. The banked default and the licensed configuration both want +0.03 to +0.04, so the tilt the fit reaches for is a property of the two-clock geometry rather than of the rebuild.

### Q4 — both locator validations re-pointed onto a re-derivable substrate

`cc66_cr_x_lstep1.npz` has no command anywhere in the repository and its comb is the superseded stacking ruler's (`l_A` 172.841). Both receipts now read `r6941_fine_cr.npz` — a launcher exists, `l_A` 301.799, ell 100–1999 at spacing 1 — and the check is **stricter** there, reproducing 70's measurement exactly:

- `P15_the_full_range_refit_holds_the_background_and_the_phase_residual_was_quantised`: raw 3.90, refined 0.023 (was raw 3.06, refined 0.133).
- `P15_the_combs_resolution_is_four_multipoles_and_the_skys_own_value_lies_outside_the_family`: `l_1` to 0.0035, worst of four 0.023 (was 0.0043 and 0.133).

Thresholds unchanged; the INDEX row naming the old substrate is re-pointed too.

### One flag

`--grid DIR` was added to `rigidity.py`, which is 70's file, in its own existing `--mc` style. Unset it is the banked grid and the behaviour is byte-identical, so none of that driver's findings move. Additive only — no definition, baseline, step or statistic touched. Flagged rather than assumed.

## cc66.80 — an absolute container path in `shape.py` made a passing receipt red in CI

`cc66.78`'s receipt passed here (22/22) and failed in CI in 0 s with `shape.py gave no statistics`. `computations/beyond_the_wall/r7091_directions/shape.py` line 32 read:

```python
sys.path.insert(0, '/home/user/shadow-of-existence/computations/planck_tt_likelihood')
```

On a runner the checkout is at `/home/runner/work/...`, so `import chi2_of_spectrum` failed, the subprocess died before printing, and the receipt's assertion reported only the absence of statistics. Now derived from `__file__`. Verified by running the receipt from a relocated copy of the tree and confirming `chi2_of_spectrum` resolves inside that copy.

Two findings beyond the one file:

- **The pattern is systemic but latent.** Roughly forty drivers and launchers under `computations/beyond_the_wall/` hold the same absolute root, including `refit_grid185/fit.py`, `PO13_score_likelihood.py`, `r6893_directions/bank.py` and most `launch.sh` / `pass*.sh`. Nothing registered reads them, so CI never runs them — the failure appears the moment a receipt invokes one. Fixed here only; the class is routed to the gate, where a lint for an absolute container path in a tracked file would close it once.
- **The assertion was its own defect.** An assertion about a subprocess that does not carry that subprocess's stderr turns a one-line ImportError into a mystery. It now reports exit code, stderr and stdout.

## cc66.81 — the banked logs were never in the repository, and the scope gate that claimed otherwise now asks git

The `shape.py` path fix (`cc66.80`) carried `cc66.78`'s receipt through three sections in CI and then it died again. Second cause, hidden behind the first: **`.gitignore` line 6 is `*.log`**, so the `.log` files copied beside the banked `.npz` grids were never committed. The receipt read two of them for each run's reported truncation ceiling — present here, absent in CI.

- The four `projection reach:` lines are now banked verbatim in `computations/beyond_the_wall/r7095_directions/truncation_reach.txt`, a `.txt` and so not ignored — the corpus's own idiom for a banked log. The `.npz` grids were tracked all along and keep their `__SWITCHES__` stamps.
- **And the receipt's own scope claim was false while it passed.** It asserted every number came from a file tracked in the repository without asking git: true of the spectra, false of those two logs. That gate now runs `git ls-files --error-unmatch` over all nine inputs and fails if any is untracked. Outside a checkout there is no tracking to ask about, so it falls back to existence and says which question it answered rather than failing or pretending.

Verified by materialising the git index alone into a separate root (`git checkout-index --prefix`) and running both new receipts from the receipt's own directory — which is exactly what CI gives them. `cc66.78` 23/23, `cc66.79` 13/13.

⌗ Three defects of one shape in a row, each hiding the next: an absolute path to this container; files excluded by `.gitignore`; and a provenance claim that did not consult the thing deciding provenance. The lesson worth keeping is the test, not the three fixes — **a receipt is only verified when it is run from a tree built from the index alone.**

## cc66.82 — `r7099` Q2: the DAMPX pair re-measured at `LEAFREC=1`, all three pins lifted, two of them tolerance defects

**New pair banked and tracked:** `computations/beyond_the_wall/spectra/r7099_lcdm_LEAFREC1_DAMPX1.000.npz` and `..._1.174.npz`, carrying the `r4494` pair's provenance keys plus `LEAFREC=1`.

### The number

`DAMPX` 1.156766 → **1.174306** = 1.08365410². The arm's diffusion scale at the visibility peak goes `r_D` 7.639814 → 7.697505 Mpc, i.e. +7.553% on the stacking rate against **+8.365%** on the leaf — back toward the `~9%` the row originally carried. The control's `r_D` is **bit-identical** across `LEAFREC` (the provable no-op), asserted in `C62`.

### The configuration proof, and a gate of mine restated

I required the `DAMPX=1.0` leg to come back **bit-identical** to banked `r4494_lcdm_DAMPX1.000`. Measured: `ls`, `l_A`, `D_M`, `r_s` bit-identical; `Dl` to **6.4e-15 relative** (~29× machine epsilon). That is reduction order, not physics — a different configuration moves a scalar or the abscissa by orders more. The banked file was built by node 60 at `r4502` under a different BLAS thread count. "Bit-identical" was too strict for a cross-machine comparison; recorded rather than passed over.

### Two pins were tolerance defects, not stale figures

`C62` lifted cleanly (re-measures the ratio live; its pair was the thing re-run). The other two failed because a check demanded **exact** equality of a peak located on a coarse ℓ grid:

| receipt | moved | grid | one bin? |
|---|---|---|---|
| `C63` `cr SWSRC=0` | 444 → 436 at `LMAXL=520` | `LSTEP=8` | 8 = yes |
| one-fitted-number | `l_1` 206 → 204 at the pin | `LSTEP=2` | 2 = yes |

`C63`'s was settled by measurement: the same leg at `LMAXL=1300`, `LEAFREC=1` returns **444** — unchanged — so 444 is not clock-sensitive and the 436 is the 520 locator one bin short. Seven of eight legs reproduce exactly on both clocks. Both checks now tolerate exactly one `LSTEP` and name in their output which legs are exact; the exact matches are still asserted exact.

Third instance this round of a gate surviving on a coincidence, after `C41b`'s literal `8.2\%` and `R1`'s `likelihood` count — the shape is a check asserting a resolution finer than the measurement it reads.

### Routed, not decided

At the faithful configuration the arm's first peak is **`l_1` = 204** where `P15` quotes 206. The paper is unchanged and nothing is blocked (the one-bin tolerance passes). If `P15` should carry the faithful value, 206 → 204 and its derived figures move — a paper change, which is the boundary `r7099` drew for itself over the diffusion figures.

### Environment finding

**This container is reclaimed when the session goes idle, not on a wall clock.** The `DSCAN` pair died twice, once at ~50 min of CPU, because `DSCAN` writes nothing until the whole solve completes. Split into two independently-saving legs (more total work, monotone progress) and landed by holding the session active ~2.5 h; each leg is ~70 min CPU. Worth knowing before ordering a run of this size: the cost is the session staying awake, not the CPU.

## cc66.83 — `r7109` ⓸ and ⓵: the DAMPX pair re-banked through the writer, and the config now carries the instrument's source hash

**⓸ The blocker, cleared as ordered — a re-bank, not a backfill.** Both legs re-run through the `config`-at-save-time writer, saving directly into `spectra/`. Nothing written into the existing `.npz` after the fact: a reconstruction entered as a record is the `COMMAND`/`FINGERPRINT` distinction the manifest itself draws.

- **The re-run is bit-identical to the first run of the same leg**, which confirms the 6.4e-15 against `r4494` is cross-machine rather than run-to-run — the reduction-order reading is measured, not assumed. Proof gate unchanged: `ls`, `l_A`, `D_M`, `r_s` bit-identical.
- **Leg 1 was re-run a second time** because it finished minutes before the writer was corrected and its `config` carried an extra `DAMPX` key leg 2's did not. A pair whose halves label themselves differently is a provenance defect, and the artefact would not have been byte-reproducible from the committed instrument. Both configs are now character-identical.
- Bank-time keys (`dampx`, `DAMPX`, `LMAXL`, `KFAC`, `LSTEP`, `path`, `built`) added with `config` preserved verbatim — provenance belongs to the banking step, not to a switch read the instrument does not need.

**⓵ The source hash — asked and answered: it did NOT record one.** Added `instrument_blob`, the git blob hash of the instrument file's own bytes, verified equal to `git hash-object`. Read from `__file__` at import rather than from git, so it records what RAN even on a dirty tree. This closes the one thing 70's three-grid audit could not show from the artefacts: "same instrument but for the switch" was inferred from shared log lines, never recorded. The pair banked here predates the hash by one commit; the next pair will carry it.

**A stale pin found before the push.** `r7109` moved `P15`'s band 206–210 → 204–208 and updated the one-fitted-number receipt's seven sites; `P15_the_fitted_onset_...` quotes the same band from a different receipt and went red. Re-pointed. Found by `run_instrument_receipts` on this tree — which is what that runner exists for.

Verified: `check_banked_config` green, `run_instrument_receipts` **102 pass / 0 fail**, fast job green (10 generators, 111 gates, the lint), `C62` green reading the re-banked pair.

Still open, not started: `r7109` ⓶ (a control base log at the grids' settings) and ⓷ (`r7101`'s 2.10-per-bin assertion and the two load-bearing unplaceables).

## cc66.84 — `r7109` ⓶: the control's base log banked beside the grids, and the peak-height cell filled

**The cell is a CONCORDANT sign.** The control's base reads `P1/P2 = 2.196`, `P1/P3 = 2.190` against the arm's banked logs' 2.283/2.311 (licensed) and 2.199/2.213 (forbidden). As a 2-dof distance in the data's own units, against the control: **forbidden 0.18, licensed 2.83.** So the forbidden configuration's heights are the control's own — a fourth statistic agreeing with χ², the crossings and the longest run — and the reading that they looked *better* was the collapse, not an improvement. The geometry says it first: the forbidden arm's `l_A` is the control's to 1.6e-5 where the licensed one's is 1.51 away.

**And the cell could never have held a contrary sign.** Against the sky on two degrees of freedom: banked 0.85, licensed 1.05, forbidden 0.44, control 0.59 — all inside 1.1, and the two ratios do not agree on an ordering. The heights concur in direction and abstain in significance; both halves are reported.

**Why the apparent disagreement looked real, and it is an instrument defect rather than a reading error.** The instrument carries **two sky references in one file**: the non-`DSCAN` print's bare `P1/P2 = 2.217, P1/P3 = 2.277` (the line the audit read) and the `DSCAN` print's `2.256 +-3.4%` / `2.280 +-3.2%`. The sky's own ratios, propagated from the published covariance's 3×3 block, are **2.2564 ± 0.0772** and **2.2800 ± 0.0737** — so the 0.084 between 2.199 and 2.283 is a fifth of the bar. The bare pair is not wrong (inside 1σ, asserted here and at `c54.176`); it is bare. **Routed, not swept:** about a dozen registered receipts carry 2.217 as `SKY` and the protocol is the paper's.

**Why the control had no log, which was not an oversight.** Both grid launchers *copy* the control's nine spectra from `refit_grid185/` rather than re-running them — `LEAFGEOM` and `LEAFREC` are provable no-ops there. A copy carries the `.npz` and not the stdout, and the peak table is printed to stdout. What is banked is therefore the **original** stdout of the run whose `.npz` IS the banked file (one file in three places, md5 `5df16bcd401dcd2a624fb230313c97f7`), under a declared `.gitignore` exception. The order's one run is spent as the independent check instead — the current instrument at the control's own settings returning the banked arrays, which also measures the `LEAFREC` no-op live since the default flipped after the bank was built.

### Method, stated rather than assumed

Reading the model on its own 2-multipole grid against a sky read on 185 coarse bins is not "the same units" — the fourth instance of that shape this round. The cell is computed the sky's own way: the models through CAMB's non-perturbative lensed/unlensed operator, binned by the likelihood's own binning, the same peak finder, the same 185-bin window, one 2-dof number per arm from the joint covariance of both ratios (correlation +0.73 — they share P1). **Not claimed as the corpus's settled protocol.** The instrument's own fine-grid unlensed route is carried beside it as a control that fires: 0.046σ against 1.124σ, same sign, so the result is not the binning's or the operator's.

Still open from `r7109`: ⓷ (`r7101`'s 2.10-per-bin assertion on 133 bins, and the two load-bearing unplaceables `cc66_lowell_sweep` and `c54.182_clpp`).

### PART 5's run, which landed after the entry above was written

The control run finished rc=0 and prints the banked log's pair exactly (`peaks at l = [220, 540, 812, 1132]`, `l_1/l_A = 0.7300`, `P1/P2 = 2.196`, `P1/P3 = 2.190`). Against the banked arrays: `ls`, `l_A`, `D_M`, `r_s` **bit-identical**; `Dl` to **6.8e-15** (136 of 238 elements differ at that level) — the same cross-machine reduction order the DAMPX pair showed against `r4494` (6.4e-15), and reported as relaxed rather than asserted as bit-identical. The bank was built at r6801 on another machine. **So the `LEAFREC` no-op on the control is now measured on the reporting path at production settings rather than inherited** — `LEAFREC` defaults to 1 since r7095+cc66.75 and the bank predates the flip.

## cc66.85 — `r7109` ⓷ first half: the 133-bin figures computed and asserted, and the hardcoded one is the wrong run's

| | χ² | bins | per bin | |
|---|---|---|---|---|
| control `cc66_lcdm` | 279.4200 | 133 | **2.100902** | the corpus's 2.10 |
| arm H0=68.60 `cc66_cr_x_h686_pol` | 556.6858 | 133 | **4.185607** | cc66.7's own 4.19 |
| arm H0=68.62 `cc66_cr_x_h6862_pol` | 552.9992 | 133 | **4.157889** | the 4.16 that is hardcoded |

The arm's χ² is asserted against the 556.7 `FOR_66` recorded for cc66.7, so the file is identified by a check rather than by recollection.

**Two sites.** `P15_the_full_range_lensed_comparison_...` line 129 prints `{4.16 / 2.10:.2f}x` labelled `(r6760+cc66.7)` — but 4.16 is the 68.62 run and the two rows computed live beneath it load the 68.60 arm, so three rows of a like-for-like table carry two H0 values. **And it propagated into `P15`:** the paper writes "over 133 bins giving 279.4 against 556.7, a factor 1.98" where 556.6858/279.4200 = 1.9923, i.e. **1.99** — the 68.60 pair's χ² values with the 68.62 run's ratio. One digit, nothing turns on it, routed to the gate seat as a paper figure; the receipt asserts both ratios so either is backed.

**Citations only in `P15`, no prose.** Three `\rcpt{}` markers for cc66.85 and one for cc66.84, added because `check_receipts` requires a registered receipt to reach a paper and `check_marker_transposition` named the sentence. The transposition gate then **discharged seven of 70's baseline adjudications**: they read "not a transposition — configuration value" on the grounds the numbers are restated as the configuration, which was right exactly while no receipt computed them. Removed with the reason recorded. Two of 70's `1.58` rows are **re-keyed, not re-adjudicated** — adding a carrier changes the group's key; verdict and reading are 70's verbatim.

**Tooling, the same lesson a third time.** `make_receipt_appendix` refused both appendices on `ⓐⓑⓒ`: the circled LETTERS (U+24D0–U+24E9, U+24B6–U+24CF) were absent entirely. Generated now with the digits' own import-time partiality guard. L-262 covered one glyph, r3144 the circled digits, r7091 their zeros — "cover the family" was read as "cover the family that broke" three times running.

### The two unplaceables — established, not closed

**`cc66_lowell_sweep` is smaller than it looks.** Eight configurations × seven multipoles. `P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling` recomputes the FROZEN variant live through `armB`, and three banked keys are exactly configurations it already computes — `FROZEN_control_KLO_0_1` = `KSCAN[0.1]` (used as `_both` at line 234), `FROZEN_control_KLO_0_02` = `KSCAN[0.02]`, `FROZEN_adjudicated_KLO_0_1` = `B_frozen[ADJ]`. **The same configuration, live and banked, in the same file, never compared** — a free exact reproduction check sitting unused. Two more FROZEN keys need one run each; only the three DECOUPLED keys are genuinely producerless (~9 min each, commands already in that receipt's PART 5). **The checks are not added yet because the tolerance must be measured before it is asserted, and measuring it means running that receipt while a solver and the fast job held the cores.**

**`c54.182_clpp`: the repository's lensing-potential producer is not this artefact's.** `L171x_lensing_potential.py` was built at **c54.184 — after** the c54.182 artefact — and writes `ls, cl, k, Phi` only, where the banked file also carries `cl_exact`, `cl_limber`, `l_exact`. So 70's "no producer" is right and the fix is not a pointer. **And re-deriving through `L171x` on the current background answers 70's open question to 60 by construction rather than waiting on it** — a potential built now on the current background is admissible by construction, where re-deriving the c54.182 object would inherit the question. That is 70's second option (re-point PART B onto a re-derivable source); not taken unilaterally, because re-pointing a registered receipt's PART B turns on an adjudication that is 60's.

## cc66.86 — `r7109` ⓷: `cc66_lowell_sweep` closed, producer written in and all eight configurations re-derived

All 56 values across all 8 banked configurations reproduce the bank **exactly** at its own 4-decimal storage: `round(live, 4)` equals the banked value identically, worst raw difference 4.9e-5 = half the last stored digit. Timings: the five FROZEN configurations ~80 s each, the three DECOUPLED ones 424–770 s.

**The engine is not a second copy.** `r7109_directions/rederive_lowell_sweep.py` parses `P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling` and exec's only its arm-B definitions (`_RUN`, `armB`, `r0_of`, the two backgrounds). That receipt's PART 5 already printed the two command lines — the specification existed and only its executable form was missing. The receipt asserts the converse too: it fails if the harness's program text appears in the producer, and fails if the receipt stops defining the names the producer's reader depends on. The `CASES` table is asserted set-equal to the banked key set, not counted.

One configuration is re-derived live on every run (~80 s) so the producer is exercised; the full eight come from the producer's tracked record, each checked against the bank rather than trusted. The bank's stored precision is derived from the bank itself rather than assumed.

**Not closed:** `c54.182_clpp`, and the receipt says so in its closing line.

**A pattern worth a ruling.** Every `\rcpt{}` citation added to an existing group silently un-keys that group's baseline adjudications, because the baseline keys on group membership. Three groups touched this round, fourteen of 70's rows re-keyed (verdicts and readings preserved verbatim, with the reason recorded in the file each time). The gate catches it every time, so it is safe — but keying on something stabler than group membership would be a change to 70's gate.

## cc66.87 — `r7109` ⓷: `c54.182_clpp` placed, bit-identically, and the era question answered by measurement

`spectra/c54.182_clpp.npz` re-derives **bit-identically** from `computations/beyond_the_wall/L171x_lensing_potential.py` at its own defaults on the current background — zero relative difference on all four keys that producer writes (`Phi`, `k`, `ls`, and the Limber `cl` PART B's figure is built from).

**Why 70's audit missed the producer, which is not a defect in the audit.** `L171x` **postdates** the artefact — `c54.184` against `c54.182` — and writes four of its seven keys. A producer search keyed on the artefact's era cannot find a producer written two revisions later under a different name. So "no producer" is literally true of the file and false of the object.

**The era question is answered by measurement, not adjudication.** 66 asked 60 whether a c54-era lensing potential is admissible on the current background at all. The current background returns the identical arrays, so `LEAFSCALES` does not move this object — the reason being in the producer's docstring (Φ(k,a) = Φ(k,a_ref)·g(a)/g(a_ref) with g a background quadrature, no transfer function imported), which the receipt measures rather than quotes. So PART B was standing on an unreproducible object, not a superseded one, and now on neither.

**What does not re-derive:** `cl_exact`, `cl_limber`, `l_exact` — the Limber-against-exact cross-check at eight multipoles — because `L171x` computes the Limber integral only. The Limber side *is* re-derived; the exact projection it is compared against has no producer. Not built: that is new machinery in c54's instrument, and the cross-check stays on the provenance list in the receipt's own closing line. PART B not re-pointed: it is c54.184's receipt, and with the object re-deriving bit-identically there is nothing to re-point it onto that it is not already reading.

**One self-correction inside the receipt.** I sized the residual gap by what each key feeds; the receipt also prints how often PART B reads each, and the count goes the other way — three reads of the unproduced keys against two of the re-derived. The count contradicts the sizing, so the receipt reports it *before* its conclusion and declines to rest on it, asserting instead on the figure line quoted from source (`P = (ls*(ls+1))**2 * cl / (2*np.pi) * AMP`). A read count is the wrong measure of load-bearing and I had it standing as a proxy for one.

**Cost, measured.** The full run is ~9 min (220 modes carried to η=4000); a reduced `NKP=12 LMAXPHI=40` run still exceeds two minutes, because the cost is the mode integration and not the mode count. So no live re-derivation fits a receipt's budget; the record is banked beside the producer and compared against the bank rather than trusted.

Both of `r7109` ⓷'s unplaceables are now answered. What remains of `r7109` is explicitly the gate seat's: the paper digit 1.98 → 1.99, and the orphaned open-ledger row `b1b3f917f5`.

### The two CI reds resolve into one cause: `Q1`'s runtime is at the 600 s wall

At `d236b3ce` the plain suite reported **294 pass, 1 fail, 1 over timeout** — the first `over timeout` on any head — and named it: `receipts/L_numerics/Q1_a_stated_tolerance_is_a_request_and_the_corpus_answers_it.py` exceeded 600 s. **That is the same receipt the tolerance ledger marks `⚠ CONTRADICTED`, carried 50 / cleared 49.** `Q1` re-runs forty other receipts' ODE solves at 100× tighter tolerance; the log catches it partway through VERDICT 3. So the red/green alternation and the timeout are one phenomenon: its runtime sits at the wall and the runner's speed decides the verdict.

**The remedy is the corpus's own.** `scripts/run_all_receipts.py`'s `LONG` table declares budgets for six receipts and names this class in its own commentary — "a budget that holds today and reports SLOW on the first slower runner", "a receipt that close to the wall reports SLOW sooner or later — and SLOW is not a pass" — with the rule: worst measured × 1.7 for contention, to the next 300 s step (C59 → 2100 s, C63 → 900 s). **`Q1` is not in that table.** A one-line entry would clear roughly half the CONTRADICTED history and changes nothing about what `Q1` measures. Not made here: `receipts/L_numerics/` is not this seat's and is not in the diff.

**Counter-hypothesis checked.** My four new receipts entered this suite and one runs an ~80 s subprocess, so added contention is the obvious way this could be mine. Against it: wall time on the timing-out head was *lower* (1612 s vs 2275 s on `6e8eb758`, where Q1 did not time out), and `C59` alone varied 1012 → 1607 s across these heads — a 1.6× spread with no change to C59, right at the 1.7× the LONG rule absorbs. So the variance is the runner's; but the load is real and if 70 reads the timing otherwise, mine get declared.

And on `cb0b7c88` — a commit touching only `FOR_66.md` — the two scoped checks scoped **3** and **2** receipts and each still returned its red. A prose-only commit cannot move a numerical tolerance or a ledger WARN, which is the cleanest demonstration that neither red tracks this branch's content.

## cc66.88 — `r7113`: `Q1` declared at 900 s, and measuring it refuted the contention diagnosis outright

`r7113` ordered one item: add `L_numerics/Q1_a_stated_tolerance_is_a_request_and_the_corpus_answers_it.py` to `run_all_receipts.py`'s `LONG` table with its measured runtime.

**Measured on this container:** 54.8 s standalone cold, 37.1 s warm, and **37.1 s with three competing full-CPU loads — no slowdown at all.** r4564's existing note records 35 s standalone and 45–47 s in-suite. So contention is refuted as the mechanism, by measurement, alongside the threading and memory r4564 already refuted and the build variant and CPU dispatch r7025 refuted.

**And the mechanism was already established in the file I was diagnosing.** `r7025+70.1`, from Q1's own source: *"exited 1 BECAUSE of a timeout — this receipt's own `timeout=600` on the tightened `P16_the_scalar_monodromy` … A timeout inside a receipt is invisible to every timeout outside it."* And four lines below: *"Do not re-run this until it passes, and do not read its carry count as a diagnosis."* I read the carry count as a diagnosis twice on the PR. I re-derived a known finding the slow way and had the cause wrong en route.

**Why the number is argued, not computed.** The table's 1.7× contention rule gives ~93 s → a 300 s step, which is *below* the 600 s this file has hit twice; a rule-conformant declaration would make the red more frequent. The budget is therefore set against the structural bound: `INNER = 600` s on one tightened child plus Q1's own ~55 s of other work ≈ 655 s, so **900 s** is the next 300 s step — the same step P14 took, and for the same reason (its own worst case, not C63's spread). Verified: the runner prints `DECLARED LONG: Q1 … runs on 900s` and it passes in 35 s.

**The repair is named and is not this seat's.** `check_receipts_run` offers "with its MEASURED cost beside it, **or repair it**". `INNER = 600` equals the outer cap, so Q1's inner guard can never fire before the outer runner kills it — guaranteed invisible, which is what r7025 found the hard way. Lowering `INNER` below the declared budget would let it fire and name the pathological child. Routed to 70; Q1's source untouched.

Noted, no change: the runner prints "named, with its measured cost in the source" for every `LONG` entry, and Q1's source does not name its cost — the measurement sits beside the entry in the table, which is what `check_receipts_run` asks for.

**Named, not started** (answering r7113's closing invitation): the `DAMPX` pair still predates `instrument_blob` by one commit — it carries `config` but not the source hash, so the pair that motivated the hash is the one pair that cannot use it. A third re-run (two legs, ~70 min each) would make it like-for-like by construction. Provenance tidy, not a result.

## cc66.89 — `r7117`: nothing ordered to this seat; `line/66` recorded as dead as an order source, and the Q1 declaration's scope limit stated

`r7117` routes to 60 and to 70. `FOR_CC66.md` is byte-unchanged from `r7113`, so this seat's queue is clear and this entry carries no result. It exists because two things had been stated only in the code window, and Daryl works in the chat window only — anything not committed there is lost.

**`line/66` is no longer an order source, measured rather than inferred.** `origin/line/66` is **0 commits ahead** of `main` and **988 behind**; its `HEAD` is `c54e4f03` = `r6772+66.42`; its `FOR_CC66.md` differs from `main`'s only by being older. So the standing cycle's premise — "66 works on `line/66` and it reaches `main` later" — no longer holds, and has not for some time. `main` is the live order source.

It has never mis-fed an order: `line/66` is a strict ancestor of `main`, so its copy of the order file is always a prefix of `main`'s and never a contradiction of it. The exposure was always "miss a new order", never "act on a wrong one". The cycle still reads both — it costs one `git show`, and a divergence would be worth knowing — but `main` decides. `FOR_66.md`'s header had been asserting the stale premise (and citing PR #59, 164 pull requests stale); both are corrected there, since the header is what the whole file is read through.

**What the Q1 declaration does not cover.** The 900 s budget governs runs that read the *new* `LONG` table and nothing else. Any run on a tree predating `a07a9b7b` — a re-run of an older head, an already-queued workflow, a cached scope — still enforces the global 600 s cap and can still report Q1 over timeout. **Such an event is not evidence the declaration failed.** The discriminator is one line of the runner's own output: a run honouring the declaration prints `DECLARED LONG: Q1 … runs on 900s`; no such line means the old table, the old cap, and an event that says nothing about the fix.

Worth writing down only because the entire history of this item is seats reading a recurrence as a diagnosis — 70 said so in Q1's own source, and this seat then did it twice anyway. A recurrence under the old cap is the cheapest available way to make that mistake a third time.

The limit is a limit and not a hedge: on a tree that *does* carry the entry, Q1 over timeout would be a real failure of the declaration and should be routed as one. The structural bound the budget was argued from (`INNER = 600` s plus ~55 s) would then be wrong, and the `INNER` repair routed to 70 becomes load-bearing rather than tidy.

## cc66.90 — `r7119`: `C63`'s check ⓶ asserted a one-point window on a quantity whose resolution is 3.7 points; repaired by deriving the window from the abscissa, and two unflagged sites in the same file with it

`r7119` routed one item: `C63`'s check ⓶, found by 70's `REGRID` mutation operator rather than by hand.

**The defect, measured.** ⓶ was `0.225 < splits['all three terms'] - 1 < 0.235` — a **one-point** window. The split is a ratio of two *integer* peaks located on an `LSTEP=8` abscissa, so one bin moves it several points:

|  | peaks CR/ctrl | split | one bin moves it | × resolution |
|---|---|---|---|---|
| all three terms | 340/276 | 23.1% | 3.7 pts | 6.3× |
| integrated removed | 316/244 | 29.4% | 4.4 pts | 6.7× |
| Doppler removed | 332/268 | 23.8% | 3.8 pts | 6.3× |
| monopole removed | 444/348 | 27.5% | 3.0 pts | 9.2× |

**All eight** neighbouring grid configurations fall outside the window: one bin on the control reads 19.6% or 26.8%, one bin on the arm 20.2% or 26.0%. The check held on which bin the locator happened to land in.

**And it is the same class already repaired in this file.** At `cc66.83` the ⓵ pins here were widened to one `LSTEP` for exactly this reason. ⓶ reads the same peaks and was not touched — the repair reached the sites that were *red* and not the site that was merely *lucky*. That is 66's reading and the measurement confirms it.

**Two more sites, not flagged, repaired with it.** ⓶ᵇ's `0.22` bound sat 1.1 points under the achieved value against a 3.7-point quantum and **fails on 4 of the 18 re-gridded trees**; ⓶ᵈ's cleared its own quantum by only 1.8×. 70's operator flagged neither — it tests the two-sided window and these are one-sided bounds. Repairing the flagged site and leaving these would repeat the mistake that produced the finding. ⓶ᶜ is an *ordering*, not a window, and needed nothing.

**The form: derived, not re-pinned to wider digits.** 66's order was explicit that a re-pin to new digits must not happen, and 60's standing point two revisions ago is that a gate pinned to the digits of a measurement asserts a spelling. So `split_quantum()` **computes** the tolerance from the abscissa the peaks sit on — it moves on its own if `LSTEP` moves — and ⓶'s two conflated claims are separated:

- **⓶ — the split is REAL and not a gridding artefact**: positive, and 6.3× its own one-bin quantum. Grid-free, and the strong half. This is what the check was *for*.
- **⓶ᵃ — it is the 23% the ROW carries**, to ±that quantum. The row carries one significant figure and one is all this grid can support.

66 offered the two forms as alternatives — widen to the quantum, or assert sign and size class — and said to take the second if the surrounding checks already carry the magnitude. **Both are needed here, and the measurement is why.** The undriven split's 23.1% is pinned *nowhere else in the corpus* (the other "23%" figures — `B4`, `c54.188`, `P15_two_arm_control_and_guard` — are the spacing deficit, a different quantity), so form 2 alone would drop the only pin on the row's figure. And form 1 alone asserts a window without ever saying the split is larger than the grid it is measured on, which is the actual content of "the split is real". The split/quantum ratio of 6.3 is the number that settles it.

**Verified both ways.** All five of PART 2's checks pass on every one of the 18 trees reachable by moving any one leg by one bin, and on both the `LMAXL=1300` peak set and the live `LMAXL=520` one (which reads the `cr SWSRC=0` leg one bin low at 436 — the leg `cc66.83` widened ⓵ to tolerate — making that row 25.2% at 8.6×). Live run green, 397 s against its declared 900 s. Fast job green: 10 generators, 112 gates, the hollow-assertion lint.

**And 70's own operator returns clean on it**, which is the verification that counts. The banked log's run on the current blobs reported `REGRID: 1 site(s) in 1 receipt(s)` naming `C63:244:10`; the re-run here against the repaired file reports **`REGRID: 0 site(s) in 0 receipt(s)`** — 14 min, exit 0. **And the `LSTEP`-up direction is clean too** — `REGRID: 0 site(s) in 0 receipt(s)`, run on `e9679c21` — so both directions 66's order named are closed (the up run was relaunched once after this seat killed a healthy run in error; nothing landed on the lost run). The other receipt on 70's regrid list, `P15_the_one_fitted_number_moves_the_scale_and_not_the_peak`, is clean here and in the banked current-blob runs — its historical up-direction flag at `257:10` was the `PAPER_L1` pin that `r7109` and `cc66.83` between them already repaired.

**CI red on #227 at `2523c250`, and it is not this PR's.** `scoped — the runner-read sweep` failed on `P15_the_progenitor_spectrum_is_defined_before_the_lift_...` — not in my diff (which is C63 plus two record files), byte-identical to main's copy, reproducing here at `15 of 17` with the same two gates, and the `PO-68` ledger at the run reads it carried on **4 lines including `main`**. That is the one legitimate "not mine" case.

A fix existed, so it is ported rather than waited on: **`r7118+60.1`** on 60's line. Two of that receipt's gates were pinned to `sec:scope`'s verbatim wording (`'carried across unaltered'`); `r7117` changed that sentence *in answer to this very row*, and both gates went red because the thing they asked for was granted. 60 withdraws the clause and asserts the paper's load-bearing premise instead (`'the crossing accumulates no divergent phase'`, present either way) plus the receipt's own computed locus. Ported into #227 and run here: **17 of 17, exit 0**. It no-ops once main carries it.

And it is the same class as the item 66 ordered this round. 60's own words: *"a gate pinned to the spelling of a sentence another seat owns asserts a spelling and not a finding — this line's own rule, turned on itself"*, counted as the fifth instance in this sector. Mine is a window finer than its abscissa; theirs is a quotation finer than the sentence's lifetime — same disease, two units. 60 repaired theirs by *removing* the pin, which is the form 60 and 66 both named as right two revisions ago, and is the form taken here for ⓶ᵃ by pinning to the row's one significant figure rather than to any measured digit.

**The port cleared its target, and a second red arrived with the merge.** `red_carry` at `e9679c21`: `- cleared: P15_the_progenitor_spectrum_...`, `+ carried: P15_the_constant_r_foliation_carries_the_sphere_across_the_lap_...` (`22 of 24`). The new one was introduced by `b4461633` = `r7118`, reaches this branch only via the main merge, is byte-identical to main's copy, reproduces here, and the `PO-68` ledger reads it carried **on 1 line: main**. No fix exists on any line (`…6awafl` has no diff on it; `…wgcmvt` predates the file). No re-run spent: both failing conditions are `in b15` string matches against the paper, so they are deterministic.

**It is `r7118+60.1`'s mechanism again, one revision later.** Both gates pin verbatim paper strings, and `r7121` discharged and struck `PO-74` in answer to this very receipt. Against the current `CR_cosmology.tex`: `'the cosmic layers are the surfaces of constant areal radius'` present; `'as a conjecture and do not claim it as a theorem'` **gone**; `'work this paper does not carry'` **gone** — replaced by *"which is shown rather than assumed, and the demonstration is one pure number"*. The gates went red because the thing they asked for was granted. The receipt's physics passes untouched (`max(near) < 1e-12`, `worst < 1e-12`).

Three instances this round across three seats, each a different unit too fine: C63 ⓶ a window finer than its abscissa; `r7118+60.1` a quotation finer than the sentence's lifetime; this one the same with the sentence struck rather than reworded.

**The patch is written and posted on #227, not pushed.** Two lines, in 60's own `r7118+60.1` form, both replacement strings verified present. Not pushed because 66's `r7109` rule is that the exception is whoever's edit broke it — 60's `r7121` paper edit broke 60's `r7118` receipt — because P15 prose and other seats' receipts are not this seat's, and because which paper clause is load-bearing for 60's claim is 60's judgement; picking it wrong would assert a spelling again, the exact error. Cost: #227 stays red on a receipt that is not this seat's. Routed to 66 for a ruling.

**A method defect of this seat's, which cost a run and impeaches the standing cycle's own probe.** I reported the first `LSTEP`-up REGRID run as dead and killed it; it was healthy. Two broken probes: `pgrep -f "mutate_assertions…"` matched its own shell wrapper, so the real process was never inspected; and `/proc/*/environ` for `ACOUSTIC_two_arm` returned 0 with nine solvers running. **The second is the cycle's own prescribed probe and it does not work** — verified against live solver pid 3247, whose environ carries `ARM=cr`, `LMAXL=520`, `LSTEP=2`, the switches and not the instrument's name. The working probe is `/proc/*/cmdline`. The cycle's step 2 should read cmdline, not environ; that line is 66's and is untouched. Cost ~35 min of compute and one wrong report, now corrected; nothing landed on it. Same shape as the fast-job replica and the inflated run counts: a probe trusted without being checked against what it actually matches — this time carried by the corpus's own instruction.
**And 70's own operator returns clean on it**, which is the verification that counts. The banked log's run on the current blobs reported `REGRID: 1 site(s) in 1 receipt(s)` naming `C63:244:10`; the re-run here against the repaired file reports **`REGRID: 0 site(s) in 0 receipt(s)`** — 14 min, exit 0. The `LSTEP`-up run is in flight, since 66's order records the check as failing re-gridded in both directions. The other receipt on 70's regrid list, `P15_the_one_fitted_number_moves_the_scale_and_not_the_peak`, is clean here and in the banked current-blob runs — its historical up-direction flag at `257:10` was the `PAPER_L1` pin that `r7109` and `cc66.83` between them already repaired.

## cc66.92 — `r7123`: `B4`/`B5`'s residual pins were windows finer than their abscissa; repaired on the derived form, a third unflagged site with them, and the repair exposed a limit of the TILT operator

`r7123` routed two sites found by 70's `TILT` operator: `abs(r_c[i] - v) < 6` in `B4` and `B5`, pinning residuals of integer peak positions to ±6 on a step-8 grid.

**The defect, measured, and worse than the routing said.** CR first-three residuals are +142.4, +80.0, +17.6; one bin on **any** peak moves them by **9.6, 8.0, 8.0** — the ±6 window sat below all three. One bin on the pinned peak moves its own residual by 8; one bin on a *fitted* peak (4–8) moves every residual, which is where the 9.6 comes from. The old window fails **11 of 43** re-gridded trees.

**A third site, unflagged, in the same two files.** `max(abs(r_l[:3])) < 20` has 4 points of headroom against the 9.6 quantum and **fails 5 of the same 43 trees**. TILT could not see it: the operator reports a literal float pin whose operands do not move, and this is a one-sided bound — the same blind spot REGRID had on C63's ⓶ᵇ, now the second time the margin case hid from the instrument that caught the window case. Repaired with it, on `r7123`'s own principle that a repair stopping at what was flagged leaves the file half-right.

**The form.** `grid_step()` reads the banked grid and refuses a non-uniform one; `resid_quantum()` measures how far one bin on any peak moves each residual. Five assertions, all verified over the 43 trees reachable by moving any one peak of either arm one bin: the shape (first three positive and strictly decreasing, the first 14.8× its own quantum); the tail (`max|r_4..8|` = 3.2, inside two bins, where r₁ is 18 bins off the line); the figures (the record's +142, +80, +18 recovered to ±2 bins — off by 0.4, 0.0, 0.4); and the control (no decaying transient, the arm's first residual beating the control's largest by 126 = 13.2× what one bin could explain).

`2 × step` is derived and not chosen: one bin on the pinned peak plus the fit's own one-bin response, measured maximum 9.6, bounded by two bins. `≤ q[i]` itself fails 3 of the 43 at the boundary — measured rather than guessed.

Both forms again, as for C63, and for the same reason: the figures are **not** descriptive here. `C56`, `P15_the_spacing_is_right_and_the_acoustic_phase_is_wrong` and the P15 appendix all quote "+142, +80, +18", and the appendix quotes the control's "within 16". The shape assertion passes under a one-bin move by design, so with the figure pin dropped nothing in either file would notice the record's digits drifting.

**And the repair made TILT flag the new figure pin.** Re-running the ratchet: the two old rows go STALE (repaired, removed as r7069 requires) and `abs(r_c[i] - v) <= 2 * step_c` comes back as a NEW DETACHED site in both files. It is detached **by the nature of the quantity**: the operand is an integer peak position from `argrelextrema` on a step-8 grid, so a smooth 5 per cent tilt is below its quantum by construction and cannot move it. That is the sibling of the `CONSTANT` class 70 added — the one case where TILT cannot resolve below the measurement's own resolution.

So a verdict was recorded rather than an exemption taken, with a new label, `QUANTISED`. The ratchet's own remedy is "READ IT AND RECORD A VERDICT"; the row states in full why the pin is kept and that **70 should rule on the label** — accept it beside `CONSTANT`, or say the figure pin should go and the shape carry it alone. Retiring a guard on three citations of the record was not this seat's call to make alone, and inventing an exemption class in 70's baseline without saying so would have been worse.

Result: `OWED: 0` — bucket empty, no new unadjudicated site, no stale entry, ratchet green.

**One line changed in 70's gate, stated rather than left to be found: `CEILING` 2 → 0.** With both owed sites discharged, a ceiling of 2 is a standing permission for two new owed ones — the same "silent permission to regress" the baseline warns of for a stale entry. A ceiling can only *tighten* a gate, which is why this seat was willing to touch another seat's file here having just declined to touch 60's receipt; it reverses in one line and the comment says so.

Verified: B4 green, B5 green, tilt ratchet green at `OWED: 0`, fast job green (10 generators, 112 gates, the hollow-assertion lint). Appendices regenerated with no diff, since they index from INDEX.md and no row changed.

## cc66.93 — three readings out of `red_carry`'s own output: the Q1 declaration is confirmed, 60's stale quote was failing three gates, and a force-push cost the ledger four comparisons

No new order, nothing of this seat's red, main not moved. These are read out of the ledgers across #227's heads.

**1. The Q1 declaration is confirmed by the gate's own ledger.** At `105be29d` the tolerance record reads `ran 233, 1 named red` with `- cleared: receipts/L_numerics/Q1_a_stated_tolerance_is_a_request_and_the_corpus_answers_it.py`. So the 900 s declaration did what it was for, stated by the gate rather than by this seat. This discharges the caveat written at cc66.89 from the other side: the limit (the declaration governs only trees carrying the new `LONG` table) stands as written, but it is no longer the only evidence available — on a tree that does carry it, the gate cleared the receipt.

`P15_the_harmonic_expansion_...` is in the same cleared list — the receipt this seat mis-routed twice. Its carry history closed by a green with nothing owed by anyone, which is what the PO-68 ledger said would happen and what should have been read the first time.

**2. 60's progenitor receipt was red in a third gate.** The `r7118+60.1` port was made to clear `scoped — the runner-read sweep`; the tolerance record shows the same receipt carried there too (`carried 2, cleared 2, on 2 line(s): …wgcmvt, main`). So one stale quotation was failing three separate gates on two lines and the port closes all of them. Worth stating because it sizes the class: a quoted sentence going stale is not one red, it is one red per gate that runs the receipt.

Unchanged and already commented on #227: the two still-red receipts are 60's `constant_r_foliation` (ledger: 1 line, main) and `layer_is_R_times_S2` (carried 4, cleared 0, on 4 lines including main). Both carried on main, both with patches posted, neither pushed, no second comment owed.

**3. A cost of this seat's own branch restart.** The tolerance record prints `4 pair(s) UNCHECKABLE: a pushed tree is no longer fetchable`. That is this seat's: #223 merged at an earlier head, so the branch was restarted from main and force-pushed over `105be29d`, and four of the ledger's before/after comparisons can no longer be made because the tree they referenced is gone. Nothing was asserted wrongly and nothing is owed, but it is a real cost of a force-push on a watched branch that had not been counted — the PO-68 ledger's evidence is pairs of trees and a force-push deletes the earlier half. If the merged-PR restart becomes routine the cost recurs; the cheap mitigation is to restart with an ordinary commit rather than a force-push wherever the branch carries no merged history to drop.

**`r7123` verified in CI, and #227's three reds are one cause.** At `1e4e925a` the plain suite ran 65 receipts: `63 pass, 2 fail, 0 over timeout, in 540s wall` — **B4 and B5 are among the 63**, so the ordered repair passes in the suite that gates it and not only on this container. All three red checks at that head (plain suite, runner-read sweep, tolerance perturbation) fail on 60's two receipts and nothing else: `constant_r_foliation` carried 3 on 3 lines including main, `layer_is_R_times_S2` carried 4 on 4 lines including main.

The tolerance sweep's own wording matters because it is not a tolerance finding: *"NOT A SWEEP -- nothing flagged, but a receipt was not measured on both builds"*. A red receipt in scope costs the sweep its verdict even when no tolerance site moves. So one struck sentence is demonstrably costing four gates, not three — strengthening the sizing recorded in cc66.93.

Both are already commented on #227 with patches; the blocker holds unchanged, so no second comment is owed and none was posted. #227 cannot reach green on anything this seat is willing to do unilaterally, and waits on 66's ruling.

The Q1 declaration is live in the runner's banner at this head: `DECLARED LONG: Q1_a_stated_tolerance_is_a_request_and_the_corpus_answers_it.py runs on 900s, not 600s`.

## cc66.94 — 60's fix for `constant_r_foliation` is ported and is better than this seat's patch; 60 has named the pattern, and it generalises both of this seat's items this round

**Ported `r7118+60.2`.** 60's branch moved and carries the repair for `constant_r_foliation`; ported here, runs 24 of 24.

**And it is a better repair than the patch this seat posted.** The proposal here was to swap the struck clause for the foliation sentence — a string swap. 60 asserts the foliation sentence *and a disjunction*: that `sec:largescale` is in exactly one of its two legitimate states — still a conjecture **with** the demonstration owed, or carrying the demonstration **and** citing this receipt. Mine fails on none of: a revert to the conjecture, the paper having neither state, the paper having both. Theirs fails on all three, the last two being paper states worth stopping on. 60's line: *"that is a real test and not a tautology."* Recorded because this seat had the weaker form and called it adequate.

**60 has named the pattern**, from the receipt: *"A GATE THAT ASSERTS THE STATUS OF A PAPER SENTENCE THIS RECEIPT IS ASKING TO CHANGE IS A GATE THAT FAILS ON ITS OWN SUCCESS. Assert the paper's LOAD-BEARING CLAUSE — the thing the argument reasons FROM — and never its STATUS."*

That is the general form of what `C63` ⓶ and `B4`/`B5` were, and this seat had only the special case. Mine: do not assert finer than the abscissa the quantity sits on. Theirs: do not assert the status your own success removes. Both are one rule — **do not pin a gate to something the work it gates is trying to move** — reached from the paper side by 60 and from the grid side here. Worth carrying as one named class rather than two. 60 counts theirs the sixth instance in this sector and routes a seventh at `r7122+60.1`, in 70's receipt and not this seat's; noted, not actioned.

**Still red: one receipt, no fix anywhere.** `layer_is_R_times_S2`, gate ⓸. Checked rather than assumed: `…6awafl` and `…wgcmvt` show zero diff on it, and the six branches that do show a diff (`line/54`, `line/56`, `line/64`, `line/66`, `spinup-checkin-diff`, `cosmological-relativity-c54-sn2msi`) do not contain the file at all, so their 297 lines is a deletion and not a repair — verified with `git cat-file` rather than read off the line count.

And this is the one where 60's own rule says the repair is not a swap: gate ⓸ asserts the non-claim *"is marked as a conjecture in the paper's own words"*, which is a STATUS assertion of exactly the kind 60 just named, and `r7121` removed the status. The repair needs the receipt's non-claim restated, which is 60's judgement and not a clause this seat can substitute. Patch still posted on #227, still not pushed; 60's naming of the pattern is now the argument for why it is theirs.

## cc66.95 — the port took three of the four gates green; a correction to this seat's own "four gates" sizing; and this seat repeated the probe defect it had just recorded

Measured at `eb9d55de`, the head carrying the `r7118+60.2` port: `fast` success, **`scoped — the runner-read sweep` success** (red on four consecutive heads before), **`scoped — the tolerance perturbation` success**, and `scoped — the plain suite` red on one receipt instead of two. The ledger states it: `ran 22, 1 named red; 1 cleared by a green, 1 still red`, with `- cleared: constant_r_foliation` and `= still red: layer_is_R_times_S2` (carried 4, cleared 0, on 4 lines including main).

**The correction.** At cc66.93b this seat wrote that one struck sentence is "demonstrably costing four gates, not three". That figure was for the two receipts **together** at that head, and it reads as "each stale quote costs four gates" — which the next head refutes. Measured properly: repairing *one* of the two took three of the four gates green, so `constant_r_foliation` was the receipt in the runner-read sweep's and the tolerance sweep's scope, and `layer_is_R_times_S2` costs exactly one gate, the plain suite.

The sizing claim stands for the pair and not per sentence. A gate count is a property of what is in each gate's scope, not of the defect — which this seat had collapsed.

What remains: one check, one receipt, no fix on any line, and a status assertion of exactly the kind 60 has just named. Patch posted on #227, not pushed; 60's own rule (assert the load-bearing clause and never the status) is the argument for why the restatement is theirs. Nothing else on #227 is red and everything red on it has been reported.

**And this seat repeated the probe defect recorded one entry earlier, in the same turn.** Clearing a background waiter, it ran `pkill -f "seq 1 55"`, which matched its own shell wrapper and killed the command issuing it — taking the FOR_66 and PO13 edits with it (re-applied since). That is the same self-match recorded at cc66.93 against `pgrep -f`, committed again within minutes of writing it up. Writing a defect down is not the same as having changed the habit. The form that is actually safe is the one already recorded: match on `/proc/*/cmdline` with a prefix test, never `-f` against a pattern the issuing command line itself contains. Cost: one re-run of two file edits; nothing landed wrong.

## cc66.96 — #227's last red cleared itself at `r7125`, and this seat's cc66.94 comparison praised the exact property that turned out to be the defect

#227 is merged, all thirteen commits on main, nothing ahead. `r7125` orders to 60 and 70; `FOR_CC66.md` byte-unchanged, so nothing is ordered to this seat. Two corrections, no new work.

**1. The receipt this seat refused to guess at is green, untouched.** `layer_is_R_times_S2` now exits 0. `r7125` reverted `sec:largescale`: the conjecture sentence is back (count 1), "work this paper does not carry" is back (count 1), "the demonstration is one pure number" is gone (count 0) — and gate ⓸, which asserts the conjecture wording, passes again on its own.

So the right action on it was to wait, and waiting cleared it. Not to be over-read: a stale quotation reverting is luck, not a method. The gate is still pinned to a paper's *status* and will break again the next time PO-74 is discharged. What was right was declining to guess the restatement; the restatement is still owed and still 60's. The red being gone does not make the defect gone.

**2. The correction that matters: this seat called the defect a virtue.** At cc66.94 the comparison table scored 60's form better than this seat's patch on three rows, one of which was *"fails if the paper has both — a paper state worth stopping on"*. **That row is wrong, and it is the row `r7125` had to repair.** From 66's note in the receipt: *"the disjunction was right in kind and wrong in connective, and the case that broke it is the interesting one"* — 70's PO-74 adversarial pass at `r7123+70.1` produced a third state, and it is the honest one: the demonstration *posits* the round S³ rather than obtaining it, so the continuation reverts to a conjecture **while the receipt stays cited for the parts that do stand** (the seam at r_N, the sign-blindness through r², the invariant's discriminating power on a Berger sphere). So `conjecture` and `cited` are true at once, the exclusive or forbade it, and `r7125` made it inclusive.

The error was not preferring 60's form — that was right, and 66's note says so ("the anti-fragile instinct that wrote the disjunction was correct"). The error is *how* it was judged: the gate was scored against the claims in its own docstring instead of asking whether those claims were true. "Fails if the paper has both" read as strength because the docstring presented it as one. A gate that forbids a state the corpus permits is not strict, it is wrong — and this seat had just spent two entries saying exactly that about windows finer than their abscissa, which is the same error in the connective instead of the tolerance.

66's own statement of the lesson, which this seat would not have reached: *"a defence against a paper state changing has to admit the state the result itself may produce."* That is the third form of this round's one rule, after this seat's (do not assert finer than the abscissa) and 60's (do not assert the status your success removes). This one: **do not enumerate the states your own result can reach.**

No code change: `r7125`'s connective is on main and this seat has nothing to add. Both receipts verified green on the merged trunk — `constant_r_foliation` 24 of 24 with all three legs printing True, and `layer_is_R_times_S2` exit 0.

## cc66.97 — `r7125`'s L204 order: the 42 is the key-collapse artefact the order itself warns about, and P10's vacuous pin concealed a dead finding

Order read, main merged, verdict pass started on `receipts/L204_physics_reach`. Two corrections to the order's premises, established before doing the work.

**1. It is 31 sites, not 42, so the ceiling goes 149 → 118 and not 107.** Measured both ways: the PROSE-PIN operator reports **42 raw sites** for L204, but the baseline and the ceiling count **distinct `(receipt, expression)` keys**, of which there are **31**. That is the same `(receipt, expression)` artefact the order names in its own closing paragraph — the 149-against-170 slack that printed "21 already read" when nothing had been read. Lowering by 42 would invent 11 of headroom: eleven sites marked read that nobody read, because identical expressions inside one receipt collapse to one adjudication (`check_prose_pins` prints that rule in its header: "reading it once settles it"). The ceiling will be lowered by 31 and nothing else.

**2. P10's `n >= 0` is not merely vacuous — it concealed the death of the receipt's own finding.** P10's docstring states its central measurement as `N_{\rm eff} 0 · N_\mathrm{eff} 0 · Neff 0 · 3.046 0 · "effective number of" 0`, and its headline is "names it in no paper", "stated nowhere". Measured on this tree: `N_{\rm eff}` 1x, `N_\mathrm{eff}` 0x, `Neff` 1x, **`3.046` 3x**, `"effective number of"` 0x — and **`N_{\mathrm{eff}}`, the spelling the paper actually uses and which the receipt's list does not contain, 5x**. `cosmogenesis_paper.tex` reads *"the effective number $N_{\mathrm{eff}}=3.046$~\cite{Mangano2005}"*. The receipt looks for `N_\mathrm{eff}` where the paper writes `N_{\mathrm{eff}}` — it misses it on a pair of braces.

And the corpus already knows: **P11, in the same family, asserts the opposite of P10's docstring about the same string** — *"and `3.046` is NO LONGER at zero — the absence ENDED at c54.205 (`L-527`) ... this check is now the REGRESSION GUARD on that filling"*, asserting `len(re.findall('3.046', allp)) > 0`. P11 is right and P10's docstring is stale. The commit that closed the absence is `9fd40454` = `c54.205`, *"CR makes no N_eff prediction because it fixes a place and not a coupling"* — the name of P11 itself. The supersession is in the git log and in the filename.

This is the class at full strength and a stronger instance than the four it was built on: those were counts that held while the thing counted moved. Here the count was never read, and what moved was the receipt's headline.

**The pass.** All 31 read against their labels rather than their tier. ~15 DELIBERATE (explicit regression guards on absences that ended, their labels saying so in terms, plus `counts['stress tensor'] == 1` with its file list); a few PRESENCE-CONTROL (bare incidental vocabulary presence); and **12 DEFECT** — 11 round-number vocabulary controls (`> 50`, `> 20`, `> 5`, `>= 5`, `>= 10`, `>= 3` across P2, P3, P7, P9, P11, which is the order's class ⓵) plus P10's `n >= 0`. Roughly two thirds legitimate, which matches the order's expectation and is explained by the survey character: a receipt whose claim is that the corpus never mentions X must count mentions of X.

In flight: the verdicts and the eleven control repairs. The ceiling moves by 31 when they land, in one visible edit, and not before.

## cc66.98 — `r7125` delivered: all 31 L204 sites verdicted, 14 defects repaired, ceiling 149 → 118, and the order's "42" traced to duplicate rows in the baseline file itself

`check_prose_pins` on this tree: `UNADJUDICATED: 118`, `PRESENCE-CONTROL: 15`, `DELIBERATE: 16`, **no new site, no stale entry**, `the ratchet holds: 118 against a ceiling of 118; 31 site(s) read and verdicted`. All thirteen L204 receipts exit 0; fast job green (10 generators, 112 gates, the hollow-assertion lint).

**Where the 42 came from, and it is worse than a miscount.** Writing the rows printed it: `removed 42 old L204 row(s), wrote 31 verdicted row(s)`. The baseline **file** held 42 L204 lines for 31 distinct keys; `read_baseline()` dicts on `(receipt, expression)` and collapses them silently. The file overstates and the gate does not — 66 counted the file, the ceiling counts the dict. Measured: baseline file rows **159**, distinct keys **149**, 10 duplicate rows across 10 keys. And it is not only L204: `L165` (8 rows / 5 keys), `L203` (7/4), `L175`, `L221`, `L557`, `L803_station9_neff` — six families where counting lines overstates the work, by 10 rows in total. Anyone sizing a block from the file's line count will over-lower the ceiling, which is the 170-against-149 failure in this gate's own history. The fix is one de-duplicating pass that changes no key and no verdict; **not done here**, because those six families are blocks this seat has not read. The 31 rows written carry no duplicate.

**14 defects, not 2.** The eleven round-number controls (order class ⓵) and P10's `n >= 0` (class ⓶) were routed. Three were not, and all three are **labels contradicting their own conditions**:
- P10's `'⇒⇒ SO THE STANDARD N_eff SETUP IS ADOPTED IN CODE AND STATED IN NO PAPER'` asserting `len(re.findall('Neff', allp)) > 0` — that it IS present.
- P10's `'the unnamed adoption is what hides it'` asserting the name is present, for a question P11 has since answered.
- P4's `'✔ NOW while "Higgs" still appears ZERO times, so the identification is invisible to search'` asserting `> 0`. Measured 4.

These could survive for the same reason as `n >= 0`: nobody read the label and the condition together. **A new sub-class worth naming: a check whose LABEL and CONDITION assert opposite things.** TILT and PROSE-PIN both key on the expression and neither reads the label, so no instrument can see it — it took a per-site human-style read, which is what the order asked for.

**The repair form: derived liveness.** Every one of those controls guards an *absence* claim, so if the glob found nothing or a regex broke, every count would be 0 and the absences would pass trivially — the one thing the control must rule out, and `> 20` was a declared proxy for it. Each receipt now carries its own check: *"the search reached live text, derived and not declared: 37 paper file(s) and 2,724,419 characters — every corpus/*.tex less the generated appendices, counted from the filesystem"*, asserted as `len(P) == len(papers())`, a fact about the filesystem and not a chosen number. The vocabulary checks now assert what their labels always said — presence — with every count printed so a move stays visible. The derived liveness checks are not reported by the instrument at all, which is the right outcome: the repair moved the claim out of the class instead of exempting it inside it.

**The substantive one: P10's headline is superseded and the receipt now says so.** The papers name the parameter — `N_{\mathrm{eff}}` 5x, `3.046` 3x — against a docstring claiming all five spellings at ZERO and a headline of "names it in no paper". The ⓵ block is rewritten as the regression guard on an absence that ended at `c54.205`, which is this family's own idiom (P1, P2, P3, P5, P8, P9 all carry it), with P11 named as the receipt holding the finding now. ⓶, the code commitment, is untouched and is what P10 still carries on its own. The spelling list now includes the live spelling it had missed on a pair of braces.

**Noted and not done:** P3's dict is still named `zero` — the terms it held when they were all zero — so `zero['Higgs'] > 0` reads against itself; a rename is cosmetic and would re-key the row, so it is recorded in the row instead. And the six families' duplicate rows, above.

PO-76 now stands at 118 unadjudicated, 31 adjudicated, every verdict carrying what was read.

## cc66.99 — `r7129`: the de-duplicating pass, and LABEL-PIN pre-registered, built, measured, and judged NOT gate-grade

**Item 1, the de-duplicating pass.** `corpus/prose_pin_baseline.tsv` went 159 data rows → 149, exactly the ten duplicates across L165 (3), L203 (3), L175, L221, L557, L803_station9_neff. Every removed row was verified byte-identical to the row that stays, under an assert that refuses the whole pass otherwise; `r7129` said a disagreeing pair must be reported rather than merged, and none disagreed. File rows now equal distinct keys (149 = 149), so the trap that sized the r7125 order is gone. Gate unchanged and green: UNADJUDICATED 118, PRESENCE-CONTROL 15, DELIBERATE 16, no new site, no stale entry.

**Item 2, LABEL-PIN.** Pre-registered at `computations/beyond_the_wall/r7129_cc66_label_pin/PREDICTION.md` and committed at `8195034a` **before** the operator touched the tree. Recall **4 of 4** on the parent blobs (`7b40925e`, before the r7125+cc66.98 repair): three OPPOSED, one VACUOUS, nothing else in those two files. The class is real and mechanically findable.

**The prediction against the measurement:** receptacles with an absence-word label 263 against a predicted 120–220 (over); stage-1 naive flags 94 against 150–400 (in range); stage-2 survivors **112 against a predicted 12–40** (3× the top); true contradictions outside L204 **0 of the first 10 read** against a predicted 0–3 (right).

**Wrong in two places named and one not.** The pre-registration said stage 2 would be the weak point; it was **stage 1** — the first run returned 453 OPPOSED of which 389 came from the bare words `no` and `not` ("is not a dichotomy", "does not use", "the check is not vacuous"). Dropping them cost recall 4/4 → 3/4 because "STATED IN NO PAPER" is a genuine absence claim; restoring `no` as a phrase (`in no <noun>`, `no paper`) put recall back at 4/4 and 66 OPPOSED.

And then a third mechanism not predicted at all, which is the actual limit: all ten OPPOSED read outside L204 are false positives of one shape — **the absence word and the condition are about different quantities in the same label**. U2's "none hedges it" asserts `len(occ) >= 1 and hedged == []`, which asserts exactly that; A1's "the word kernel … times" asserts `_kernel_then == 0`; C1's "HAS NEVER EXITED ZERO" tests board text, not exit codes. A corpus label routinely says "A is present (N times) and B is absent", and resolving which subject the absence attaches to is semantic co-reference that no static scan settles.

**Verdict: reports, not enforced**, on the pre-registration's own terms ("real, hand-found, and not mechanizable at useful precision — which is a result and is reported as one"). All three true instances are in L204, the survey family, exactly as the load-bearing prediction said. So it earns no ratchet row beside `check_prose_pins` and `check_quote_pins` — the same call 70 made for REGRID. What it is worth: `label_pin.py --files <block>` on a family about to be read by hand cuts the label-and-condition reads from all of them to a few; a reading aid for a per-site pass, which is how all three were found.

One self-inflicted finding: five narrow survivors are this seat's own repair labels from last round — "with the counts printed so a move is visible and **asserted nowhere**" contains `nowhere`. A repair written in one round became a false positive for an operator built in the next; the guard is in the source.

One block named and not adjudicated: `VACUOUS` is a separate and much cleaner signal — a condition that asserts nothing of its own — standing at **46 sites** on the tree, of which P10's `n >= 0` was one. Not read here: r7129 asked for the label-versus-condition class, and 46 sites is a block, not a footnote. The obvious next order.

## cc66.100 — `r7131`: all 12 L221 sites verdicted, 10 repaired, ceiling 118 → 106; and testing an "ALL" claim found that the corpus writes one invariant two ways

`check_prose_pins`: 147 keys / 147 baseline rows, UNADJUDICATED 106, PRESENCE-CONTROL 23, DELIBERATE 17, NOT-A-COUNT 1, no new site, no stale entry, "the ratchet holds: 106 against a ceiling of 106; 41 site(s) read and verdicted". Every L221 receipt exits 0; fast job green at 113 gates.

On the arithmetic: **12 sites were read**; the repairs collapsed two keys, so the live total fell 149 → 147 and the unadjudicated count 118 → 106. The ceiling tracks what is unread, so it moves by the 12 read and not by the 10 rows written — recorded in the gate's comment beside the number. The order's "13 → 105" was the pre-de-dup file count, from cc66.98's own measurement, and cc66.99 removed that duplicate row.

**The third sub-class paid off immediately.** Flagged in flight: a condition *weaker* than its label rather than opposite to it — invisible to `label_pin` (nothing points the wrong way) and to PROSE-PIN (which sees only the count). Two instances, both labels claiming "ALL":

- **B33**: *"P15's 6 uses are ALL inside ratios — never standing alone as a physical length"*, asserting `n_uses > 0 and len(ratios.findall(...)) > 0` — true of a paper where one use is in a ratio and five stand alone. Repaired by testing the claim: strike the ratio contexts out and count the bare uses left. **Left = 0 of 6.** The label was right and nothing had checked it.
- **B3**: *`"K^2"` appears 6 times — ALL of them the extrinsic curvature in the Hamiltonian constraint*, asserting `n_k2 > 0` plus one string appearing somewhere. **Testing the ALL found why nobody had: the corpus writes the invariant both ways.** Five occurrences are `K^{2}-K_{ij}K^{ij}`; the sixth is `K_{ij}K^{ij}-K^{2}`, the same invariant transposed with the sign flipped, in BH_causality's Bianchi line. So "ALL of them" is 6 of 6 — but only once both orderings are allowed.

That second case is what makes the sub-class worth having: a one-string test reports the claim unverifiable, and a careless repair weakens the *label* to match the string, losing a true statement. The only route to the right answer was to test what the label said and let it fail first.

**The verdict split, and 66's scope note was right.** L204 (survey): 16 DELIBERATE of 31, 14 repaired. L221 (not): 1 DELIBERATE + 1 NOT-A-COUNT of 12, **10 repaired**. The reason is as 66 said — L204's majority was the survey idiom (regression guards on ended absences), while L221 has one of those (B28's filled vocabulary gap) and eleven ordinary controls.

B41's `dims.count(2) == 2` is the one NOT-A-COUNT: not a text count at all — `dims` is D₆'s irrep dimension list from a group-theory computation, with the character-table identity `sum(d*d) == 12` asserted beside it. The static trace reached a list length and read it as a count of matches. The exact figure is the claim and a change would be a different group; nothing owed.

**And these repairs took 70's new QUOTE-PIN gate red, which is fixed and stated.** The fast job went red on `check_quote_pins` after the B3 repair: one STALE entry, the literal `"K^{2}-K_{ij}K^{ij}"`, because the two-ordering regex retired the bare-string site that row described. Removed per the same r7069 rule the tilt baseline carries — a fixed site left in a baseline is a silent permission to regress there. It was UNADJUDICATED, so nothing adjudicated was lost. Gate green: 2297 keys / 2297 rows, no new key, no stale entry.

**70's ceiling was NOT lowered, and that is a change from cc66.92 worth recording.** There this seat lowered `CEILING 2 → 0` on the reasoning that a ceiling can only tighten. Here the fall is incidental — a site retired as a side effect of a repair, not a site this seat adjudicated — and 70 is mid-pass on a live 2,286 backlog; tightening their ceiling by one while they work could make their next legitimate state red for a reason that is not theirs. A ceiling this seat lowers should be one it earned by reading, not one that moved under someone else's feet. It reads `2286 against a ceiling of 2287`, and that slack is 70's to close.

## cc66.101 — a CI red on a superseded ancestor, and the find is in the carry layer: a red from an ancestor outlived the green that cleared it

`scoped — the tolerance perturbation` went red on `112ad14f`, an ancestor of PR #236's head, with **exit code 2** — a verdict the workflow names in words, not a crash: `NOT A SWEEP -- nothing flagged, a receipt unmeasured`. **Nothing was flagged.** The unmeasured receipt is `receipts/L_numerics/Q1_a_stated_tolerance_is_a_request_and_the_corpus_answers_it.py`.

**It is not this PR's, on four independent readings.**

1. **The diff does not reach it.** No `L_numerics` file is in `origin/main...HEAD`, and none of Q1's four children is either — `P16_the_mixing_is_two_pi_over_rho`, `P15_the_continuation_is_diagonal`, `P16_the_scalar_monodromy_is_four_pi_over_rho`, `P15_the_crossing_exists_and_is_empty`. Q1 enters the tolerance scope **only** through its `READ_INDEX` dep `receipts/**/*.py`, which any receipt edit anywhere satisfies.
2. **It measures inside its budget here.** Q1 runs in **33 s**, exit 0, every verdict passing (`READ_INDEX` records `s: 47.9`). The runner filed it unmeasured against `2 * max(900, 600) = 1800 s`, and under the `r7007+70.1` rule that is **two** timeouts — the parallel pass and then the re-run alone. 33 s against 1800 s is a factor of **54**.
3. **A same-commit control exists, because the repo runs two workflows per head.** On `112ad14f` the `pull_request`-event run `37073925456` ran the identical check and **passed in 41 s**; the `push`-event run `37073897369` ran **50 minutes** and failed. Same tree, same gate, opposite outcomes — the scopes differed because the ranges did (`receipt_scope.py --range 56628e4b..112ad14f --scope tolerance` is **n=0**: that commit is prose only).
4. **The live head measured Q1 green.** `receipt_scope.py --range 112ad14f..dfce672f --scope tolerance` gives **n=24, Q1 among them**, and both of `dfce672f`'s runs passed (4 min and 7 min). Q1 was covered on the current head, in the same scope class that had just failed on its parent.

**⚑ The find is why the red is still on the branch, and it is in the carry layer rather than in Q1.** `refs/ci/carry` was last written at **23:32:34** — by the *failing* run, **after** both green runs on `dfce672f` had finished (23:09:24 and 23:12:34). `red_carry.py`'s own conflict rule is that a refused push "re-reads the ledger and re-applies ITS OWN delta", so a slow run on the **ancestor** re-added Q1 on top of the descendant's clear. `carry.json` now reads `claude/shadow-of-existence-setup-5tjf0b -> tolerance -> L_numerics/Q1`, `since: 112ad14f`.

⇒ **A red carried from an ancestor can outlive the green that cleared it, whenever a slow run finishes after a faster run on a later commit of the same branch.** Each run's delta is correct for itself and wrong for the branch: the last writer wins, and "last" is wall clock, not ancestry. The ledger already reasons about forks and about which branch may clear which entry; it does not reason about **two live commits of one branch**. This is node 70's layer (PO-65/67/68), so it is named here and not changed — the same posture as the ruling I am still owed on repairing another seat's gate.

**The honest limit is the module's own, quoted rather than paraphrased** (`red_carry.py` ll. 58–60): *"that a timeout's clear is a repair. Every other clear is a run that covered the receipt … a quieter machine clears it exactly as a fix would, and nothing here tells the two apart."* So the 33 s here and the green on `dfce672f` do **not** show Q1 repaired. They show it measures inside budget on two machines, and that nothing in this PR moved it. Q1 already carries this shape: `r7025+70.1` judged an earlier `>600 s` on the runner "an event, not a cost".

**Action.** One re-run of the failed job (attempt 2 of run `37073897369`) — the single re-run the posture allows for confirming a not-this-PR's failure, and the same mechanism that clears the carry, since a green records Q1 as covered. **No fix pushed: there is nothing in this diff to fix.** PR #236's head `dfce672f` is green on all four running checks and `mergeable_state: clean`.

**⛔ And one against myself, the third occurrence of a shape I have already routed twice.** The `/proc/*/cmdline` probe I routed as the repair for the `pgrep`/`pkill` self-match **matched this shell's own command line** — because the pattern being searched for appears in the searching command. The probe was only half the repair: **the matcher must exclude its own PID.** I killed by PID instead, and the correction belongs on the cycle instruction I have already asked 66 to change. Twice recorded is still not changed.

## cc66.102 — `r7135`: both blocks closed, ceiling 106 → 97; and the predictor 66 asked me to test FAILS AND INVERTS, with a better one measured in its place

`check_prose_pins`: **147 keys / 147 baseline rows**, `UNADJUDICATED 97`, `PRESENCE-CONTROL 31`, `DELIBERATE 18`, `NOT-A-COUNT 1`, **no new site**, **no stale entry**, *"the ratchet holds: 97 unadjudicated against a ceiling of 97; 50 site(s) read and verdicted"*. All four receipts exit 0; fast job green at 113 gates; `check_quote_pins` green at 2300 keys / 2300 rows.

**The order's sizing was right this time** — 5 and 4, file rows equal to distinct keys in both families, because the `cc66.99` de-dup pass had already closed that gap everywhere. Ceiling 106 − 9 = 97, which is the order's "roughly 97".

**The arithmetic, since it keeps moving:** 9 rows written for 9 sites read, no key collapsed and none retired, so here the ceiling's fall equals the rows written *as well as* the sites read. That is a coincidence of this block and not the rule — at `r7131` it was 12 read against 10 written. The ceiling still tracks what is unread.

### The reading aid: two more blocks, and it flags nothing on either

`label_pin.py --files` on `L165_defining_the_sum`: **36 distinct keys → 0 flags**, stage 1 itself 0. On `L203_reach_stations`: **53 keys → 0 flags**, stage 1 0. Two receipts in the first and three in the second carry absence-word labels; none is paired with a presence condition.

⌗ **Said plainly, as the order asked: a reading aid that saves no reads on a real block is a different verdict from one that was never tried.** On `L221` it cut 422 keys to 4 and two of those four were real finds. Here it contributes one fact and no leads — that these two families contain no `OPPOSED` and no `VACUOUS` site. **That is worth having and it is not what the aid was sold as.** The nine prose-pin sites still had to be read one at a time, because `label_pin` and `PROSE-PIN` see different things: the aid reduces the *label-versus-condition* reads, never the verdict reads.

### The verdict split, and 66's predictor goes the wrong way

| family | n | DELIBERATE | reach family? |
|---|---|---|---|
| `L204_physics_reach` | 31 | 16 (52%) | yes |
| `L221_the_bridge` | 10 | 1 (10%) | no |
| `L165_defining_the_sum` | 4 | 1 (25%) | no |
| `L203_reach_stations` | 4 | **0 (0%)** | **yes** |

**`L203_reach_stations` is the reach family and it scored lowest of the four. `L165_defining_the_sum` is not one and scored higher.** So family type is not the predictor, and this is not a weak result in the predictor's favour — it is the wrong sign.

### ⚑ And the real predictor was sitting in L204's own verdict notes

Reading them back: **14 of the 18 `DELIBERATE` sites tree-wide are regression guards on an absence that was filled** — "at ZERO when this receipt was written, supplied at `c54.202`", "the absence ENDED at `c54.205`", "is in print now", "the debt is DISCHARGED". Per family: **L204 12 of 16, L221 1 of 1, L165 1 of 1, L203 0 of 0.** The three small families are exact.

⇒ **The predictor is not what KIND of family it is. It is whether that family's own receipts caused the papers to change.** `L204_physics_reach` drove a documented burst of revisions (`c54.202`, `.204`, `.205`, `.207`) and every filled absence legitimately left a `> 0` guard behind. **L204 was not unusual as a reach family; it was unusual as the family that moved the corpus.** `L203`'s four sites are liveness controls sitting on top of three real sentence-level checks that already run above them — it changed nothing, so it banked no guards.

**Back-tested on the 49 sites already read**, from the label alone: **recall 0.76** (13 of 17), **precision 0.87** (13 of 15), 1 label unmatched.

**Pre-registered forward, before the next block is read:** over the remaining 97, the predictor matches 76 labels and says **8 `DELIBERATE` and 68 `PRESENCE-CONTROL`** — about 11% against L204's 52% — naming where: `P15_CR_cosmology` 2 of 27, `L221_quark_lepton` 2 of 2, `L218_reader_package` 1 of 8, `L803_station9_neff` 1 of 6, `L175_dimensional_descent` 1 of 3. **21 sites are unmatched because they sit in bare `assert`s, which `label_pin` does not read — a known limit of the instrument, stated here rather than hidden in the 76.**

### The nine sites

**Eight were round-number controls** and repaired to presence with counts printed: `n_th > 20` → `> 0` and `n_alg > 20` → `> 0` in `S1` (**each in two places**, the condition and the closing conclusion, which share one key); `branched bead >= 2` → `> 0` in `M2`, where the label's claim is that "P14 USES THAT PHRASE"; and `n_alg >= 4`, `n_anc >= 8`, `n_con >= 2` → `> 0` in `M3`, **each in two places**, where the label *prints* all three counts and claims nothing about 4, 8 or 2. One site — `S1`'s `deficiency ind > 0` — was **not repaired because it was already the minimal form**; only the count (6) was added to its label. `S50`'s `_now > 0` is `DELIBERATE` untouched: the receipt's own gate comment says the point of the revision is the counterterm count moving off zero. `S1`'s docstring also carried a stale "(45 occurrences)" for a count now at 49, corrected in the same pass.

### ⚑ The one real defect, and it is the kind that passes for the wrong reason

**`S1`'s C6 asserted `len(re.findall('fibre', allp, re.I)) > 5`, and it could not fail for C6's reason.** 'fibre' stands at **28** occurrences across 7 papers and only **7** sit within 140 characters of any closure or boundary-condition language; the rest are the Hopf submersion's fibre, the covering maps' fibres and the radial operator's sub-threshold fibres. ⇒ **21 unrelated hits clear a floor of 5 on their own: every per-fibre closure sentence could be deleted from the corpus and the check would still pass.**

**And the claim IS in the papers — written "fibre by fibre", not "per fibre".** That is why a word count was reached for in the first place, and why a search for C6's own phrase returns nothing: `per[- ]fibre` is at **zero** in the papers. `canonical_time` carries the fibre-wise phrasing three times, once with the deriving receipt cited on the sentence (`D1_the_boundary_is_per_fibre_and_the_UV_is_over_fibres`). ⌗ And the label's own words are "cannot be broken by the **number** of fibres", so a pin on a number of occurrences was asserting the one thing C6 disclaims.

**⛔ My first repair was wrong and the gate caught it.** I asserted the paper's sentence as a literal — which retired the prose-pin key and put **two new keys into 70's `quote_pin_baseline.tsv`**. That moves the claim into another seat's class instead of settling it, and it pins a gate to wording the papers are actively being revised to change: **this round's own rule, turned on me.** Withdrawn and measured rather than adjudicated. What is asserted now is the grid-free shape — a fibre-wise phrase standing in closure language — which is reword-tolerant across two vocabularies and three phrasings. Measured: **3 of 3 fibre-wise phrases near closure language, 0 of the other 25 'fibre' hits**, so the discriminator is exact. `check_quote_pins` is back to no new key.

## cc66.103 — correcting cc66.101: the Q1 red is STRUCTURAL, not contention, and the defect is a budget that counts one child where there are eight

**The re-run came back failure on attempt 2** (exit 2 again, 46 minutes). So `cc66.101`'s reading — a timeout anomaly plus a run-ordering artefact — **is withdrawn on its second half.** What it measured was right (33 s here, green on `dfce672f`, the same-commit 41 s control, the `n=0` range); what it *invited* was wrong, and the line's practice is to record that rather than quietly restate it.

**The arithmetic, which settles it.** Q1 runs its sample as child subprocesses: **4 receipts × 2 passes** (as written, then at 100× tighter tolerance) **= 8 children**, each capped by Q1's own `INNER = 600`. Worst case **4800 s**. The sweep allows `2 * max(900, budget(Q1, 600))`, and Q1 is declared in `run_all_receipts.LONG` at **900**, so the outer budget is **1800 s**.

- **Three children at their cap (1800 s) exhausts the outer budget.**
- **Two children (1200 s) already exceeds the 900 s declaration.**
- ⚑ **And the declaration states its own assumption in writing:** *"900s covers its own `INNER=600` bound"* — it budgets for **one** child at the cap, and there are **eight**.

**Long-standing, and already in the record from the other side:** `r7019+70.1` notes *"`Q1`'s ten suite timeouts (09-28/09-29)"*. ⇒ So the condition has materialised repeatedly and the budget line has never been revisited against the child count.

**Still not this PR's**, and that part of `cc66.101` stands unchanged: the diff touches neither Q1 nor any of its four children, and Q1 enters the tolerance scope through its `READ_INDEX` dep `receipts/**/*.py` — and now through the carried red as well, which re-enters it on every push to this branch until some run measures it green.

**Proposed and NOT pushed, because Q1 and `sweep_tolerances` are node 70's.** Make the child cap a share of a **total** deadline rather than a per-child one, so `n_children × cap` fits inside the declared budget, keeping the `r7025+70.1` behaviour where a child past the cap is recorded as a named verdict rather than raising. A slow child then *reports* instead of blowing the outer budget, which is what that machinery was built for. ⌗ **Raising the `LONG` entry to cover 4800 s would be wrong by that table's own standard** — the `C59` and `C63` entries both argue at length that a declaration records a cost the receipt *has*, and Q1's measured cost is 33 s with all eight children fast. A 4800 s budget would describe a cost it does not have in order to hide one it does.

⇒ **Two items for 70's layer are now outstanding from this one failure** — this budget, and the carry's last-writer-wins across two live commits of one branch (`cc66.101`). Both named, neither touched, and the ruling on repairing another seat's gate is the thing that decides what happens next.

## cc66.104 — the Q1 red is on `main` and on a sibling branch too, and the SUITE red confirms the arithmetic: it is Q1's child budget, not the tolerance probe

**My branch's carry cleared** — `80c8158d`'s push run measured Q1 in the tolerance scope (`n=23`, Q1 among them) and **passed in 5 minutes**, so the entry `cc66.101` found is gone. ⌗ *I had read the ledger before that run's record step wrote; the reading, not the layer, was early. The `cc66.101` ordering finding stands as stated — a red from an ancestor DID outlive a later commit's green — but it resolved on the next covering green rather than sticking.*

**And the ledger now shows the failure is everywhere:**

| branch | class | run | red |
|---|---|---|---|
| `main` | tolerance | `37079174045`, head `8a997cad`, **73 min** | `L_numerics/Q1` |
| `…6awafl` (another seat) | **suite** | `37080526986`, head `f0faf273`, **43 min** | `L_numerics/Q1` |
| `…5tjf0b` (mine) | tolerance | cleared by `80c8158d` | — |

⇒ **The base branch carries the same red**, which is the one case the drive-to-green posture calls legitimately not this PR's — and it is not silent: it is commented on #236, proposed on #240 and routed here.

### ⚑ The SUITE red is the one that settles the cause

**`…6awafl`'s failure is in `scoped — the plain suite`, not in the tolerance probe.** The probe was never the cause, and that rules out the composition story anyone would reach for first (Q1 tightens its children 100×, the probe perturbs builds). **In the plain suite the budget IS the `LONG` declaration — 900 s — and Q1 runs 8 children each capped at its own `INNER = 600`.** Two children at their cap is 1200 s and the receipt is killed.

⇒ **That is the `cc66.103` arithmetic reproducing in a second class on a third branch, and it is the strongest form of the claim available**: the defect is Q1's own per-child budget against its declared total, and nothing about the instrument that happened to surface it. **The declaration's own words — "900s covers its own `INNER=600` bound" — budget for one child where the code runs eight.**

⌗ *So the proposed patch does not change: make the child cap a share of a TOTAL deadline, keeping the `r7025+70.1` behaviour that records a child past the cap as a named verdict. **It now fixes a red on `main` rather than a red on one PR.*** Still not pushed — `Q1` is node 70's receipt and the ruling I am owed covers exactly this.

## cc66.105 — `r7137`: the carry-layer audit. 62 of 425 writes are out of order, 54 reds were actually lost, 21 were never re-recorded, and 20 of those are one event on `main` — but the defect is the MIRROR of the one I reported, and it cannot touch a verdict

### ⛔ First, against myself: the case I reported at `cc66.101` is the layer working as designed

`red_carry.py`'s own concurrency note states the intended rule: *"Two jobs disagreeing about one receipt: **red wins**."* The Q1 event I found — a failing run on an ancestor re-adding a red after a descendant's green had cleared it — **is that rule being honoured.** I called it a defect; it is the specification.

⇒ **The real defect is the mirror case, which I did not report and which the rule does not survive:** an ancestor's run that *passes* on a receipt writes `del cur[rec]` (`apply()`, the `elif rec in cur` branch), and on a refused push the module re-applies *its own* delta — "add these reds, **clear these greens**". So when the ancestor writes last, **its clear removes a red a descendant had recorded, and green wins.** `red wins` holds in one of the two orderings and not the other.

### The measurement, over the whole ledger

425 ledger commits, all parsed, no missing shas.

| | |
|---|---|
| **out-of-order writes** (a run on an ancestor wrote after a run on a descendant, same branch and class) | **62** (14.6% of all writes) |
| of those, writes that cleared something — the direction that can lose a red | 35 |
| of those, writes that only re-added — the `cc66.101` shape, intended | 27 |
| **reds actually lost** (an ancestor's clear removed a receipt a descendant had marked red) | **54** |
| of those, later re-recorded on the same branch | 33 |
| **never re-recorded afterwards** | **21** |

By branch, of the 54: `…6awafl` 28, **`main` 21**, `…wgcmvt` 3, **mine (`…5tjf0b`) 2**. Both of mine were `L_numerics/Q1` and **both were later re-found**, so none of my branch's losses is in the never-recorded 21.

### ⚑ 20 of the 21 are a single event on `main`, and its shape matters

Ancestor `5d85e6e4` (`r7083`) wrote `tolerance @ main: +0 -22 =1` at `01:38:53`, **1166 s after** descendant `97636d38` (`r7085`) had written `+23 -0 =1`. 22 of the 23 were cleared and 20 were never recorded again.

⌗ **And the honest reading is narrower than "a green overrode a red".** The descendant's run `36802241087` was **cancelled**, not failed — so its 23 tolerance and 64 suite reds were not measurements but the module's deliberate blanket carry for a job whose failure cannot be attributed. The ancestor's run `36800853571` **did** measure, and failed, and its clears are real passes — *on an older tree*. ⇒ So what actually happened is **a measurement on an ancestor overriding an UNKNOWN on a descendant.** That is still a loss the layer promised not to allow, and still wrong substantively — a pass on the parent establishes nothing about the child — but it is not the crisp story, and the crisp story would be the wrong one to put in the register.

⌗ **A second limit, stated because the ledger cannot settle it:** "never re-recorded" does not distinguish *passed when next covered* from *never covered again*. The ledger records deltas, not coverage. So 20 is the count of reds the layer stopped chasing, not of defects that went unseen.

### ⇒ The answer to what `r7137` actually asked

**No — the greens in `FOR_66` are not worth "exactly as much as the carry layer's ordering", and the reason is the direction of the dependency.** The carry decides **scope only**: which receipts the next run re-tests. It cannot retract a check-run conclusion, and nothing it does feeds the fast job or a PR's own checks, which is where every green I have reported comes from. ⇒ **What the ordering can cost is not a verdict but the layer's own guarantee**, stated in its docstring: *"no push that misses it can silence it: it is re-run until it finishes."* **That is the sentence this defect falsifies, and it is the only one.**

### ⇒ And it is an ordering change, not a ratchet

The information needed is already in the ledger. Record, per `(branch, class)`, the newest head sha written; on a write whose own head sha is an **ancestor** of that, **apply its adds and drop its clears.** That preserves `red wins` in *both* orderings, needs no new file and no new gate, and is a few lines in `apply()`/`do_record`. ⌗ A ratchet would be the wrong instrument here: there is no backlog to hold down, only a rule that is already written and is enforced in one direction out of two.

**Not pushed.** `red_carry.py` is node 70's, and this is now the fifth item this round turning on the ruling I am owed about repairing another seat's apparatus.

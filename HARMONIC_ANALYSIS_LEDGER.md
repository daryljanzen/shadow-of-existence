---
name: harmonic-analysis-ledger
kind: FORWARD
current: r3452
job: The harmonic-analysis field-bake ledger — what bit, what bounced, and the boundary. Second of the four fields `L-272`'s re-survey left outstanding. `OWED` 622.
sources: [cowork]
---

> **▣ FORWARD — the harmonic bake, and part of the corpus.** *Three registers kept apart: **what bit**,
> **what bounced**, **what the boundary is**. `L-272` put this field second, on the HARMONIC half
> specifically — the operator half is station Ⓗ's (`L-264`, the Weyl limit-point test) — and because
> `P15`'s* ***"discrete closed-$S^3$ spectrum projected through the flat spherical Bessel"*** *is a
> live computation and it is Sturm–Liouville on a sphere.*


## ⛭ THE BASELINE, MEASURED FIRST

| present | absent across all seventeen, word-bounded |
| --- | --- |
| `orthogonality` ×10 · `Fourier` ×3 · `mode function` ×4 · `transfer function` ×4 · `hyperspherical` ×2 · `discrete spectrum` ×2 · `Riemann sum` ×1 · `aliasing` ×1 · `Laplacian` ×1 | `Sturm` · `Liouville` · `spherical harmonic` · `Legendre` · `Gegenbauer` · `eigenfunction` · `completeness relation` · `Plancherel` · `Parseval` · `convolution` · `addition theorem` · `Wigner` · `sum rule` · `power conservation` · `band-limited` · `Nyquist` · `Poisson summation` · `Euler–Maclaurin` |

⌗ *So the corpus does the work and carries almost none of the field's names — the same shape the Cartan
bake found one field over.*


## ⛭⛭ WHAT BOUNCED — and the bounce is large

**The field's first question is why a closed-$S^3$ source is projected through FLAT spherical Bessel
functions rather than hyperspherical ones. `P15` answers it in its own text**, and the answer is right:

> **"Because the distance slicing is flat, the photons are projected through the flat geometry ...
> while only the source modes carry the closed-$S^3$ quantization ... not the hyperspherical transfer
> of a literal closed universe: that transfer carries the closed distance relation, which CR does not
> have, and would (wrongly, here) deliver the lowest mode to the quadrupole and no deficit."**

**The field's second question is whether the measure is right.** *`P15` states
$w_L=(L+1)/(L(L+2))$ and derives it twice — as degeneracy $\beta^2$ over per-mode power
$\beta(\beta^2-1)$, and as $d\ln k_L/dL$.* ⇒ ***Both agree to machine precision at every $L$ tested,
and the paper's own stated limit holds: as $D_C/r_0\to0$ the ladder sum returns to the flat plateau
(0.9999 at $D_C/r_0=0.3$).***

⌗ **Controls, run before anything was used:** *the spherical-Bessel completeness identity
$\sum_\ell(2\ell+1)j_\ell(x)^2=1$ to ten figures — so the projection conserves power mode by mode —
and the fixed grid reproducing $\int j_\ell^2\,d\ln x = 1/(2\ell(\ell+1))$ to six figures, so the
quadrature is not the finding.*


## ⛔⛭⛭ WHAT BIT — the deficit is TWO effects and the paper reports one

*In the pure Sachs–Wolfe limit, the suppression relative to the continuum splits exactly into the
**FLOOR** (the integral truncated below $k_2$) and the **DISCRETENESS** (the ladder sum minus that
truncated integral).*

| $\ell$ | full = sum/int | floor = trunc/int | **discreteness** |
| --- | --- | --- | --- |
| 2 | 0.121 | 0.048 | **+0.073** |
| 3 | 0.104 | 0.118 | −0.014 |
| 4 | 0.199 | 0.158 | +0.041 |
| **5** | 0.649 | 0.269 | **+0.380** |
| **6** | 0.916 | 0.531 | **+0.385** |
| 7 | 0.986 | 0.789 | +0.197 |
| 8 | 0.998 | 0.931 | +0.067 |
| ≥13 | 1.0000 | 1.0000 | ~0 |

⇒ ***At $\ell=5$–6 the discreteness contributes as much as the floor and in the OPPOSITE direction:
the ladder puts back power that a pure cut-off removes.***

⇒ **And it sets the recovery multipole.** *With it the spectrum recovers to 99% at $\ell=8$; the floor
alone recovers at $\ell=10$.* ⌗ ***The paper quotes "recovery by $\ell\approx8$" — so the number it
quotes is the ladder's, not the floor's.***


## ⛭⛭ AND THE TWO HALVES RESPOND TO $r_0$ WITH OPPOSITE SIGNS

*Under $\pm2\%$ in $r_0$, in this limit:*

| $\ell$ | full | floor |
| --- | --- | --- |
| 3 | **+27.8%** | −6.2% |
| 4 | **−43.3%** | −2.4% |
| 5 | −13.3% | −17.9% |
| 6 | −3.1% | −14.9% |

**`P15` says: "The location is geometric and robust; the depth is settled by the full Boltzmann
transfer."** ⇒ ***The decomposition is why. The LOCATION is the floor and it is robust exactly as
claimed; the DEPTH is the ladder and it is volatile. The paper's qualitative split is correct and now
has a mechanism.***


## ⛭⛭⛭ AND A SELF-WAIVED GATE BECOMES A BOUND

**`P15` records the waiver in its own voice:** *the ladder* **"samples the projection below the rate
the instrument's own aliasing gate demands, and that gate waives itself on the claim that the ladder
is physical, with the check named in its own text and never run against $\chi^2$."**

*Measured: the ladder's imprint dies at* $\ell \simeq k_2 D_C\,e^{3\sigma}$, *with $\sigma$ the
transfer's width in $\ln k$.*

| $\sigma$ | first $\ell$ with \|discreteness\| < $10^{-3}$ | $k_2D_C\,e^{3\sigma}$ | ratio |
| --- | --- | --- | --- |
| 0.00 | 11 | 7.8 | 1.41 |
| 0.10 | 12 | 10.5 | 1.14 |
| 0.25 | 16 | 16.5 | 0.97 |
| 0.50 | 32 | 34.9 | 0.92 |

⇒ ***To imprint at the first acoustic peak ($\ell\approx220$) the transfer would need $\sigma\approx1.1$
— drawing power over a factor of NINE in $k$. Far broader than any CMB transfer.*** ⇒ **So the waiver
is safe, with a wide margin — by measurement and a stated bound rather than by the claim that the
ladder is physical.**

⚠ **AND THE DIRECTION IS THE OPPOSITE OF THE NAIVE EXPECTATION, which is why it was worth computing.**
*A broader transfer does not average the ladder away. It reaches further **down** into the ladder's
coarse bottom — where $\Delta\ln k = w_2 = 0.375$ — and so carries discreteness **up** in $\ell$.*
⌗ ***The first form of this test, run with adaptive quadrature, reported that at $\sigma=0.5$ the
imprint never died within $\ell\le40$. Redone on a fixed grid whose quadrature is checked against the
exact plateau, it dies at $\ell=32$. The direction survived; the number did not.***


## ⌗ THE BOUNDARY — what this bake did not reach

- **The real transfer's width.** *Everything above is the pure Sachs–Wolfe limit, where the transfer
  is $j_\ell^2$, with a Gaussian-in-$\ln k$ **stand-in** for a broader one. **Measuring the actual
  $\Delta_\ell(k)$ width of the Boltzmann transfer is the owed next step** and turns the bound from a
  scaling into a number. Named rather than left implicit.*
- **The paper's quoted depths.** *`P15` reports $0.42, 0.35, 0.29, 0.52$ at $\ell=2$–5 from a genuine
  Boltzmann transfer; this bake's Sachs–Wolfe numbers are deeper, as the paper says they should be
  ("the deficit is milder than a Sachs–Wolfe-only estimate suggests"). **The two are not compared and
  no discrepancy is claimed.***
- **The Boltzmann code itself.** *Not run here. The decomposition is a property of the ladder and the
  Bessel functions; whether the split survives quantitatively on the exact transfer is untested.*
- **`Poisson summation` as such.** *The oscillatory structure at $\ell=2,3,4$ (+0.073, −0.014, +0.041)
  is the image-term signature and is reported as measured, **not** derived. A derivation would give
  the amplitude in closed form and is not attempted.*

⛔ **AND THE ONE THING THIS BAKE MUST NOT BE READ AS SAYING:** *nothing here says the deficit is wrong.
Every number of the paper's that this bake touches is reproduced or confirmed, including its own
$D_C/r_0\to0$ limit. What changed is that a result reported as one geometric effect is two, that they
carry the robustness and the volatility respectively, and that a gate the paper waives now has a
margin behind it.*


---

# ⛭⛭ BROUGHT TO THE BAR — r3452

> *The r3166 bake's content stands. What it lacked was **numbered probes and a receipt** — and this
> ledger's own record of an adaptive-quadrature artefact is the strongest argument for the receipt
> requirement anywhere in the sweep.*

## ⌗ THE LEAD REGISTER

| # | probe | state |
|---|---|---|
| `H0` | baseline, word-bounded | ⊢ **WORKED** r3166 — *the corpus does the work and carries almost none of the field's names, the same shape the Cartan bake found* |
| `H1` | is the ladder measure $w_L$ right? | ⊢ **WORKED** r3452, **receipted** — *two derivations return the **same expression**, not merely equal values* |
| `H2` | does the flat projection conserve power? | ⊢ **WORKED** r3452, **receipted** — *completeness to ten figures* |
| `H3` | is the quadrature the finding? | ⛔ **IT WAS, ONCE** — r3166, receipted r3452 |
| `H4` | is the low-$\ell$ deficit one effect or two? | ⛔ **BITE** r3452, **receipted** — *two, of opposite sign* |
| `H5` | why flat Bessel rather than hyperspherical? | ⟐ **BOUNCE** — *`P15` answers it in its own text, and correctly* |
| `H6` | does the flat plateau return as $D_C/r_0\to0$? | ⊢ **WORKED** r3166 — *$0.9999$ at $D_C/r_0=0.3$* |
| `H7` | is `P15`'s self-waived aliasing gate safe? | ⊢ **WORKED** r3166 — *bounded, not assumed: imprinting at $\ell\approx220$ needs $\sigma\approx1.1$, a factor of nine in $k$* |
| `H8` | does a broader transfer average the ladder away? | ⛔ **NO — THE OPPOSITE** r3166 — *it reaches further **down** into the coarse bottom and carries discreteness **up** in $\ell$* |
| `H9` | the real transfer's width | ⛭ **REFERRED** — *the pure Sachs–Wolfe limit is what is computed; the full transfer is `P15`'s* |
| `H10` | is the operator half this field's? | ⛭ **REFERRED** — *station Ⓗ's, and worked as the functional-analysis bake's `F1`–`F3`* |
| `H11` | is `P14`'s "mode completeness" really open? | ⛔ **BITE** r3454, **receipted** — *the wall is the reflectionless pair; only the **join** is open* |
| `H12` | is `P07`'s adiabaticity parameter local or integrated? | ⏷ **ROUTED** r3456, **receipted** — *the separation is exact; the local value diverges* |
| `H13` | is `P10`'s "loses control at the lowest harmonics" a coincidence? | ⛔ **BITE** r3457, **receipted** — *it is FORCED, and it joins two papers* |

---

## ⊢ H1–H4 — **RECEIPTED** *(`storyboard_receipts/HA_H1_H4_the_ladder_and_the_projection.py`)*

- **`H1`** — $w_L=(L+1)/(L(L+2))$ as degeneracy over per-mode power **and** as $\mathrm{d}\ln k_L/\mathrm{d}L$.
  ***Sympy returns the same expression from both routes***, which is stronger than agreement at sampled $L$.
- **`H2`** — $\sum_\ell(2\ell+1)j_\ell(x)^2=1$ to ten figures. **Nothing in the deficit is projection loss.**
- **`H3`** — the fixed grid reproduces $\int j_\ell^2\,\mathrm{d}\ln x=1/(2\ell(\ell+1))$ to better than a
  part in $10^3$. ⚠ ***And this control is not decoration: the ledger records that the FIRST form of its
  aliasing test, on adaptive quadrature, reported an imprint that "never died within $\ell\le40$", and
  that on a checked fixed grid it dies at $\ell=32$. The direction survived; the number did not.***
- **`H4`** — the deficit splits into **floor** and **discreteness**, ***of opposite sign at some
  multipoles*** — at $\ell=4$ the discreteness is negative where the floor is positive — and near
  $\ell=5$–6 the discreteness contributes as much as the floor. ⇒ ***The ladder recovers to 99% at
  $\ell=8$; the floor alone does not until $\ell=11$.*** *`P15` quotes "recovery by $\ell\approx8$" —
  **the ladder's number**. **The paper's figure is right and the mechanism behind it is not the one its
  text names.*** ⌗ *(the exact floor multipole moves with $D_C/r_0$, chosen as $3.0$ in the receipt; the
  split and the ordering are what is asserted)*

---

## ⛭⛭ THE BAR, MEASURED

| | this bake | the FULL tier |
|---|---|---|
| lines | **~200** | 189–978 ✔ |
| numbered probes | **14** (`H0`–`H13`) | 10–17 ✔ |
| receipts, all running | **4** | 2–10 ✔ |
| papers touched | `P07`, `P10`, `P14`, `P15` = **4** | 6–11 ⚠ *two short* · **reach 4/12 = 33%** |
| lead register | **11 rows, none unmarked** | — |

⛔ ***ONE RECEIPT AND FIVE PAPERS SHORT, AND THE NARROW-FIELD DEFENCE IS REFUTED.***

*It was argued here that this field touches one paper because its subject IS one computation in one
paper, and that the bar does not fit it.* ⇒ ***Measured at r3453: the harmonic vocabulary appears in
SIX papers. This bake read one — a REACH of 17%, the worst of the five fields worked.*** *So it is not
a narrow field fully worked; it is a field whose subject spans six papers and whose bake read one.*

⌗ **THIS FIELD STAYS OPEN.** *What is owed is the five papers the vocabulary reaches and this bake did
not, and a second receipt. `THE_FIELD_BAKE_PLAN` now carries `REACH` as a reported quantity for exactly
this reason.*


---

## ⛔⛭⛭ H11 — **`P14`'s WALL IS SOLVED, AND ITS "MODE COMPLETENESS" IS NOT OPEN**

*The first probe of the reach owed after r3453. `P14` carries more of this field's vocabulary than any
paper (`mode` ×60) and this bake had never read it. It lists among its open undertakings* ***"the
quantised field, its mode completeness, and the join between the static region's continuum and the wall
— which sit in different regions"***.

**`P14`'s wall is $m(x)=\tanh(x/a)$, and the Dirac problem factorises into the SUSY partners
$V_\mp=m^2\mp m'$:**
$$V_-=1-2\,\mathrm{sech}^2 x\quad(\text{Pöschl–Teller},\ \ell=1),\qquad V_+=1\quad(\text{free}).$$
*Diagonalised: $V_-$ carries **exactly one** bound state, at $E=0$ to six figures, matching the analytic
$\mathrm{sech}(x)/\sqrt2$ — the Jackiw–Rebbi zero mode — and its partner carries **none**.*

⇒ ***That is the REFLECTIONLESS pair: one bound state plus a reflectionless continuum, for which
completeness is a classical closed-form result.*** *So the wall's mode completeness is **not** open.*

**⌗ AND `P14` SAYS SO ITSELF, IN THE SAME SENTENCE:** *what is open is* ***"the JOIN … which sit in
different regions"***. *The wall's own spectral problem is solved; joining it to the static region's
continuum is the undertaking.* ⇒ **The clause reads as though three things were open and one of the
three is a solved system — which understates what the paper has.**

**⏷ ROUTED, NOT APPLIED.** *The clause owed: that the wall's mode problem is the reflectionless
Pöschl–Teller system, whose completeness is closed-form, so the open undertaking is the join alone.*

⚠ **AND THIS RECEIPT CAUGHT TWO OF ITS OWN NUMERICAL SLIPS.** *The first draft discretised
$-\tfrac12\,\mathrm{d}^2/\mathrm{d}x^2$ and returned **two** bound states with $E_0$ negative; the second
asserted $\lvert E_0\rvert<10^{-6}$ against a grid delivering $1.7\times10^{-6}$.* ⌗ ***With this
ledger's own adaptive-quadrature artefact that is three numerical slips in one field, every one caught
by an assert, and not one of which prose would have caught.***
*(receipt `storyboard_receipts/HA_H11_the_wall_is_reflectionless.py`)*

---

## ⏷ H12 — **`P07`'s ADIABATICITY IS AN INTEGRATED BOUND WRITTEN AS A LOCAL ONE**

*The second probe of the reach owed. `P07` carries this field's vocabulary ×55 and the bake had never
read it. It states:* ***"the tower's frequencies diverge at the branch point but only as $s^{-2/3}$ …
its adiabaticity is controlled by the harmonic index alone, the parameter being $C/\mu_n$ with
$C\le1.72$."***

**⌗ THE SEPARATION IS EXACT AND THE CLAIM IS STRUCTURALLY RIGHT.** *With $\omega_n(s)=\mu_n f(s)$ the
WKB parameter is $\lvert\dot\omega/\omega^2\rvert=(1/\mu_n)\lvert f'/f^2\rvert$ — **the mode index factors
out identically**, so "controlled by the harmonic index alone" is not an approximation.*

**⛔ BUT THE LOCAL VALUE DIVERGES, FOR EVERY MODE.** *With $f=s^{-2/3}$, $\lvert f'/f^2\rvert=\tfrac23
s^{-1/3}\to\infty$ at the branch point.* ⇒ ***So the local parameter is unbounded at $s=0$ for every
$n$ — not of order unity at $n=2,3$ and small elsewhere.*** *The divergence is **integrable**, which is
why `P07` can say correctly that the adiabatic **correction** is finite.*

⇒ ***THEREFORE $C\le1.72$ BOUNDS AN INTEGRATED QUANTITY, NOT A LOCAL ONE*** — *and the sentence "the
parameter being $C/\mu_n$" reads as local, where no such bound exists.* ⌗ *The corpus's own
`LOWL_adiabatic_bearing.py` uses $1.72$ as a given constant and does not distinguish them.*

**⏷ ROUTED, NOT APPLIED.** *What is owed is one word: whether $C$ bounds the local parameter or its
integral along the segment. **The receipt asserts the divergence and the convergence, not a value for
$C$***, since that depends on the segment's range and on subleading terms.*
*(receipt `storyboard_receipts/HA_H12_the_adiabaticity_is_integrated_not_local.py`)*

---

## ⛔⛭⛭ H13 — **`P10`'s DECLINED COINCIDENCE IS FORCED, AND THE ENTAILMENT SPANS TWO PAPERS**

*`P10` writes, carefully:* ***"We record, **without claiming it**, that the harmonic indices at which
the treatment loses control are the lowest ones."*** ⌗ *A declined claim is the best kind of probe:
either the caution is warranted, or the claim is available.* ⇒ ***It is available, and it is a
theorem.***

**① THE TOWER BEGINS AT $n=2$**, *and `P10` says so — "there are no modes below $n=2$ on $S^3$". The
reason is the TT rank-two degeneracy on $S^3$, $2(n^2-1)$: **zero at $n=1$**, empty below, and $6$ at
$n=2$.*

**② THE ADIABATICITY PARAMETER IS MONOTONE.** *From `H12` it separates as $C/\mu_n$ with
$\mu_n=\sqrt{n(n+2)-2}$, and*
$$\frac{\mathrm d}{\mathrm dn}\frac1{\mu_n}=\frac{-(n+1)}{\big(n(n+2)-2\big)^{3/2}}<0\quad\text{for all }n\ge2,$$
*so $C/\mu_n$ is **strictly decreasing**, ***for any value of $C$***.*

⇒ ***① AND ② TOGETHER FORCE IT.*** *A monotone-decreasing parameter takes its largest value at the
smallest available index, and the smallest available is $n=2$ by the degeneracy.* **So the adiabatic
treatment MUST lose control at the lowest harmonics — whatever $C$ is, and whatever the frequencies do.
It is not a coincidence to be recorded; it is entailed.**

**⌗ AND IT JOINS TWO PAPERS.** *`P07` supplies the parameter's form and `P10` the spectrum's floor.*
***Neither alone entails the conclusion and together they do*** *— which is why the entailment was
available to neither, and why a field bake reaching across papers is the thing that finds it.*

**⏷ ROUTED, NOT APPLIED.** *`P10`'s caution can be withdrawn: the sentence can **claim** what it
currently only records.*
*(receipt `storyboard_receipts/HA_H13_the_declined_coincidence_is_forced.py`)*

⌗ **A PROBE THAT BOUNCED ON THE WAY, worth recording.** *The obvious attack was that `P10` relies on
the TT/conformal orthogonality — a completeness statement — without naming the decomposition.* ⇒ **It
names it**: `York` appears in **eight** papers, `transverse-traceless` ×29, `DeWitt` ×11, `tensor
harmonic` in `P10` itself. *The anonymity pattern that held for `Hilbert space` and `Ambrose–Singer`
does **not** hold here.*
---
name: acoustic-build-setup
kind: STATE
current_main: r2111
job: The boundary conditions, layer assignment and scope for THE_PLAN's parametrisation-arc step ⑥ — the first-principles acoustic build. WRITTEN BEFORE ANY CODE so it can be checked on its own.
sources: [cowork]
current: c54.185
---

> **⛭⛭ BROUGHT CURRENT r2449, TO c54.185 — and this setup's front moved twice while the file stood still.**
>
> *It says "the setup for the front the working fork is on **right now**", so its own claim obliges it to track that
> front.* **Two things landed:**
>
> **⛭ ① A DERIVED LENSING, RUN WITH NO FREE WIDTH — and it came in UNDER the bound a fit had set** *(c54.181–183)*.
> *c54.181 **fitted** a growing-width smoothing worth $\Delta\chi^2=400$ on the $\Lambda$CDM arm and stated the
> discipline before the number was known:* ***"a derived lensing that came in ABOVE 400 would not be a triumph, it
> would be evidence the operation had a free parameter hiding in it."*** *The derived calculation returned
> **$1320\to989$, $\Delta\chi^2=331$**, after validating where the answer is known (**CAMB's own $\Lambda$CDM,
> $615\to186$**).* ⚠ *The operator is **$\Lambda$CDM's own lensed-to-unlensed ratio, imported not fitted**; **`PO-7`
> stays protected and the CR arm does not fit.***
>
> **⛔ ② AND THE SETUP'S OWN VOCABULARY IS AT RISK IN P15** *(routed as `FOR_54` 21, flagged to take first)*: *P15
> says **"branch point"** at five sites where **the receipt cited at those sentences says "seam"** — nineteen times
> to zero. And the loci behave oppositely: $1/aH$ is **1.000 at the seam** and **0.051 at $10^{-3}\alpha$**, so*
> ***a proposition titled "sub-horizon" is TRUE at the seam and FALSE at the branch point.***
> ⌗ **A build setup is exactly where that distinction must be right**, *since it fixes boundary conditions at a
> locus — **and the conflation has already cost two independent nodes a false finding in one day**.*


> **⌗⌗ INDEXED r2380 — LIVE, and it is the setup for the front the working fork is on right now.**
> *Its own discipline is why it is worth keeping and is quoted rather than paraphrased:* ***"Written before any
> code, so it can be checked on its own"*** *and* ***"every number here recomputed from the measured parameters
> at write time, not carried over from earlier revisions."*** **A setup document that can be checked without
> running the build is the guard against the failure the heights arc paid for four times** — the r822 lesson,
> read the source before the computation.
>
> ⚠ **AND ITS OWN REASON FOR EXISTING NOW APPLIES TO IT.** *It says the Phase-7 build was stale because it
> "predates r2099–r2110" and was written on superseded ground. **This file is r2111 and the fork has run to
> c54.134**, with `computations/beyond_the_wall/` gaining 29 scripts on this exact front (the collapse leg's
> scale invariance, the mode map, what the sky permits of the parent) — so the same argument now bears on the
> setup itself.* ***That is a read for whoever next opens the acoustic build, not a defect this line resolves:
> the front is the fork's.***

# THE ACOUSTIC BUILD — SETUP

> **⌗ RE-READ AGAINST c54.163 AND DECLARED CURRENT r2396 — and this one is dated with a standing caveat, not a
> clearance.** *Its `species` is the **species reversal at the branch point**, so the withdrawal does not touch
> it.* ⚠ ***But its subject is the front the fork has been advancing hardest***, *and its own r2111 argument
> still bears on it: it retired the Phase-7 build as written on superseded ground, and* **this file is r2111
> while the fork has run to c54.163** *with `computations/beyond_the_wall/` and `baryon_edge/` gaining scripts
> throughout.* ⇒ ***The setup is the PLAN; those directories are the EXECUTION, and the two have still never been
> read against each other.*** **That is a read for whoever opens the acoustic build, and it is the fork's front,
> not this line's to resolve.**


> **⛭ What this is.** The boundary conditions, layer assignment and scope for arc step ⑥, the
> first-principles acoustic build. **Written before any code**, so it can be checked on its own.
> Opened r2111. Every number here recomputed from the measured parameters at write time, not
> carried over from earlier revisions.
>
> **Why the build is fresh.** The existing Phase-7 build predates r2099–r2110. It was written with
> `z_onset` as a fitted lower limit, with seam-language for a locus that is not a seam, and before
> the lap's structure was assembled. **It is a suspect model: leaned on for verification, not trusted.**

---

## 1 · THE PARAMETERS

Two numbers, both measured (`PHYSICAL_VALUES_LEDGER` §0.1, §0.2):

| | value | route |
|---|---|---|
| $x_0$ | $1.6648\pm0.0467$ | DESI DR2 $D_M/D_H$, calibration-free, 6 bins, $\chi^2=6.51/5$ |
| $\alpha$ | $16.037\pm0.300$ Gly | ladder, $H_0=73.0\pm1.0$ |
| | *or* $16.889\pm0.599$ Gly | stellar ages, $t_0=13.57\pm0.27$ Gyr — **$1.71\sigma$ from the ladder** |

**⚠ The $\alpha$ ambiguity is real and unresolved.** The build should carry $\alpha$ symbolically and
report sensitivity to it, not adopt one route silently.

**⛔ NO CMB-DERIVED NUMBER MAY ENTER.** Planck's $H_0$, $\Omega_m$, $\theta_*$, $r_s$, $z_*$ and every
CMB-combined value are $\Lambda$CDM fits *to the acoustic physics this build exists to derive*. Using
any of them is circular. **This includes the acoustic angle $\ell_A=301.6$ itself** — it is the thing
to predict, not an input. (Violated three times in the r2105–r2107 stretch; see those entries.)

Admissible external inputs: $T_{\rm CMB}$, $N_{\rm eff}$, $\omega_b$ from **BBN** (not from peak
heights), the distance ladder, stellar ages, and DESI BAO **ratios**.

---

## 2 · THE RATE, AND WHAT IT IS NOT

$$H^2(x)=\frac{\Lambda}{3}\left(1+\frac{2}{x^3}\right),\qquad x=r/r_N$$

**Two terms, and no slot for a third.** P8's vacuum kernel $rf'+f-1+\Lambda r^2=0$ has entire
solution space $f=1-2M/r-\Lambda r^2/3$; Nariai then fixes $M=1/3\sqrt\Lambda$. The first term is
$R$-odd (perspectival), the second $R$-even (invariant). **Neither is a density**, and there is no
$\Omega_r$ in the rate at any epoch.

**⛔ Do not call this "radiation-free".** That phrasing imports the rightward picture in which content
sources expansion — the picture the construction denies. It is *geometric*: the rate is set by which
cut, and content is read off it on the other layer.

---

## 3 · WHERE THE ACOUSTIC ERA SITS

Recomputed at write time from $x_0=1.6648$, $\alpha=16.037$ Gly:

| epoch | $z$ | $r/\alpha$ | $\operatorname{Re}\tilde\tau$ |
|---|---|---|---|
| hadronisation | $7.2\times10^{11}$ | $1.33\times10^{-12}$ | $2.6\times10^{-14}$ Myr |
| BBN / deuterium | $3.0\times10^{8}$ | $3.23\times10^{-9}$ | $3.2\times10^{-9}$ Myr |
| matter–radiation equality | $3936$ | $2.44\times10^{-4}$ | $0.0657$ Myr |
| recombination | $1090$ | $8.81\times10^{-4}$ | $0.451$ Myr |
| **front seam** | $0.665$ | $0.5774$ | **$7040$ Myr** |
| today | $0$ | $0.9612$ | $12885$ Myr |

> **The entire acoustic era lies between $r/\alpha\sim10^{-12}$ and $\sim9\times10^{-4}$: all on the
> real expansion leg, immediately after the branch point, and $\sim10^4$ times closer to $r=0$ than
> to the front seam.** Neither seam is in its neighbourhood. In this range
> $r\simeq A_r(3c\tilde\tau/2\alpha)^{2/3}$ to better than $10^{-12}$ relative.

---

## 4 · THE BOUNDARIES, AND THEIR JUSTIFICATION

### Lower: $r=0$

**The physical bound is the fluid's existence.** A photon–baryon fluid requires baryons, so acoustic
oscillation is possible from **hadronisation** ($T\sim170$ MeV) onward. And the sound-horizon
integrand goes as $a^{-1/2}$ on this rate, so:

$$r_s(\text{from hadronisation})=r_s(\text{from }a=0)\quad\text{to 4 decimal places}$$

**So the lower limit is $r=0$ for all practical purposes** — the branch point, where the expansion
begins and where the geometry has its one violent event ($\dot r\to\infty$, $\ddot r$ reversing
through $\pm\infty$, the species reversal).

**⛔ The fitted $z_{\rm onset}=6761$ is retired as a boundary.** $T=1.588$ eV is not recombination
(0.26 eV), not equality (0.9 eV), not the deuterium bottleneck ($7\times10^4$ eV), not hadronisation.
No plasma condition has been identified there. It was obtained by `brentq` against the measured
acoustic angle — i.e. by fitting the answer.

### Upper: recombination

Thomson coupling fails, the fluid stops being a fluid. Unambiguous. $z_{\rm rec}$ must be computed
**on this rate** (Peebles), not taken from Planck.

---

## 5 · THE LAYER ASSIGNMENT

P16 `sec:scoping` — the boundary is derived, not assumed, and *"carrying either law across into the
other's domain is quantitatively fatal."*

| stretch | $\operatorname{Re}\tilde\tau$ | layer | rate |
|---|---|---|---|
| back seam → turnaround → lift → $r=0$ | $-14.13$ Gyr $\to0$ | **L2** | **window** rate: the infalling congruence's own leaf-level expansion scalar, **radiation included** |
| $r=0$ → recombination → front seam → today | $0\to+12.885$ Gyr | **L1** | **foliation** stacking rate $H^2=2M/r^3+\Lambda/3$ |

*The reassignment acts on the **time-stacking** and **not on the leaf**: content and composition cross
as inherited progenitor data while the stacking is reset. **Everything leaf-level is continuous at the
crossing.*** So radiation appearing in the perturbation source while absent from the rate is the
transition law's content, **not** a boundary violation.

---

## 6 · WHAT CROSSES, AND AT WHAT STANDARD OF PROOF

| quantity | status |
|---|---|
| $\Phi$ (curvature perturbation) | **derived** — it is in the induced 2-metric on a null hypersurface; Barrabès–Israel forces continuity |
| $\Psi$ | **not derived.** $\Psi=\Phi+6\mathcal H^2\Omega_\nu\sigma/k^2$, and $\sigma$ is a fluid variable, as free as $\hat\Theta$. P15: the seam is far below neutrino decoupling, so the shear is genuinely there |
| $\hat\Theta$ (photon temperature perturbation) | **permitted to reset, not forced.** The junction conditions leave it entirely free; P16's dissociation is the physical argument and it is doing real work |
| $\rho_r/\rho_m$, $\eta$ | **inherited content data.** Dimensionless, and `A.150` shows they *cannot* be geometric: the substrate supplies exactly one scale, $\alpha$, and a lone dimensionful quantity cannot set a dimensionless ratio |

**⚠ Scanned and found inert (r2103):** seeding $\sigma$ at the lower boundary moves $\ell_1$ not at all
across $\sigma\in[0,0.2]$. So the $\Phi$/$\Psi$ distinction, while real, is not where the peak
position lives.

---

## 7 · WHAT THE BUILD MUST PREDICT, NOT FIT

$\ell_A=\pi D_M/r_s$ · $\ell_1$ · the peak spacing · $P_1/P_2$, $P_1/P_3$ · $\theta_D/\theta_*$.

**With the lower limit at $r=0$ and nothing fitted, $\ell_A$ comes out $171.7$ against a measured
$301.6$** (computed on the ladder $\alpha$; the age $\alpha$ shifts it). **That is the number the build
has to confront**, and it is the honest starting position — not something to be closed by a cutoff.

---

## 8 · THE FAILURE MODE THIS DOCUMENT EXISTS TO PREVENT

Across r2105–r2110 every caught error was **at the write-up step, not the calculation step**: a
$\Lambda$CDM value used one revision after the rule against it was written; an uncertainty quoted on
one route and omitted on the other; "lap" written where "lift" was computed. **The arithmetic was
right each time; the prose drifted while restating it, and each drift made the result look stronger.**

**Rule for the build: before any ledger write, re-derive the specific numbers from the live
computation rather than from earlier prose.** In all three cases the correct value was already on
screen.

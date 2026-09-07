---
name: PO38_WORKING_NOTE
description: PO-38's computation as run — the growth root on the leaf rate, the judgement that the moment-balance form does not survive, and the three roots side by side. Held outside the corpus.
status: WORKING DOCUMENT — deliberately not a paper
current: r4394
---

# PO-38 — **THE MOMENT BALANCE DOES NOT SURVIVE, THE ROOT BARELY MOVES, AND THE CONTINUED
INTEGRAL POINTS THE WRONG WAY**

*Everything below is asserted by
`\rcpt{P15_the_growth_root_on_the_leaf_rate_is_not_a_moment_balance_and_the_gap_stands}`, which runs
in about twenty seconds.*

## ⛔ THE JUDGEMENT, MADE BEFORE THE ARITHMETIC

***`PO-38` asked for this decided first, and it is decidable symbolically rather than numerically.***

*The derivation's Step 2 is one sentence —* "the decaying mode IS the rate." *Apply the growth
operator to $D=H$ with radiation present, using only the flat Friedmann/Raychaudhuri pair
$\dot H = -4\pi G(\rho+p)$ and the two continuity equations:*

$$\mathcal{L}[H] \;=\; \ddot H + 2H\dot H - 4\pi G\rho_m H \;=\; \tfrac{32}{3}\pi G\,H\,\rho_r$$

⇒ ***THE DECAYING MODE STOPS BEING THE RATE THE INSTANT RADIATION GRAVITATES.*** *With it go the
reduction of order that gives $D_+ = \coth u\,F(u)$, the identity $G'/F' = \tfrac92\Omega_m - 2$, and
the moment balance itself.* **The balance is a matter-and-$\Lambda$ theorem, not a growth theorem.**

⌗ ***AND $\alpha$ STILL CANCELS.*** *Radiation enters the rate as a dimensionless function of the
clock, so the equation stays scale-free — it simply acquires $\Omega_r$, which the geometry does not
fix.* **The loss is parameter-freedom, not scale-freedom: a parameter-free equation becomes a
one-parameter family.**

⌗ *Corroborated downstream rather than left as an argument: $\Omega_m = \mathrm{sech}^2 u$ fails on
the leaf rate by $9.3\times10^{-4}$ at $v=0.2$, and the balance integral returns $-1.71\times10^{-4}$
at the leaf root where the stacking one vanishes to $10^{-13}$.*

## ⛭ WHAT REPLACED IT

*The growth ODE integrated directly in $x=\ln a$,
$D_{xx} + [2 + \dd\ln E/\dd x]D_x - \tfrac32\Omega_m(a)D = 0$, on the leaf rate with flatness kept.*
**Two calibrations, each against an independently known answer, before either is used:**

- *the Mészáros growing mode $D = 1 + \tfrac32 y$ is checked **exact** for matter+radiation to
  $1.6\times10^{-12}$, so the normalising attractor is analytic and no window is fitted;*
- *with radiation off, the ODE under the published $D\to\tfrac25 a/\Omega_m$ convention reproduces
  the closed form $\int_0^1 \dd a/(a^3E^3)$ to $2\times10^{-12}$.*

## ⛭⛭ THE RESULT — **OUTCOME 3, WITH A SIGN**

| | $\Omega^\star$ | $u_0$ | $x_0$ | vs $1.6648$ |
|---|---|---|---|---|
| stacking (the published root) | 0.315162424 | 1.180309372 | 1.631903 | $-0.704\sigma$ |
| **leaf, growing mode SOLVED** | **0.315303543** | **1.180038880** | **1.631480** | $\mathbf{-0.713\sigma}$ |
| leaf, published integral CONTINUED | 0.314917676 | 1.180778715 | 1.632453 | $-0.693\sigma$ |
| — corpus measured — | | 1.2052 | $1.6648\pm0.0467$ | |

***The root moves by $\dd u_0 = -2.70\times10^{-4}$ — $1.1\%$ of the $0.0249$ gap — taking the
offset from $0.704$ to $0.713\sigma$.*** **The $2\%$ is not an artefact of the rate. The gap stands
and wants a mechanism.** *And the shift goes **further** from the measurement, not closer.*

⛔ ***AND THE CONTINUED INTEGRAL GETS THE DIRECTION BACKWARDS, WHICH IS THE SHARPER FINDING.***
*Continuing the published closed form onto the leaf rate — the route behind the recorded $0.99934$ —
moves the root **toward** the measurement where solving the equation moves it **away**, and by
$1.7\times$ the size in $u_0$.* ⇒ **$0.99934$ does not measure how far the root moves. It measures a
closed form failing on a rate it does not solve, and reading it as a direction gives the wrong one.**

## ⌗ THE PIVOT DOES NOT MOVE — IT SPLITS

| | $u$ | $r/r_N$ |
|---|---|---|
| stacking: $\Omega_m = 2/3$ | 0.658478948 | **1.000000000** |
| leaf: $\Omega_m = 2/3$ | 0.658260700 | 0.999747989 |
| leaf: $q=0$, the turnover | 0.658768578 | 1.000334436 |

*$\Omega_m = 2/3$ is the acceleration turnover only when matter and $\Lambda$ are the whole content.
Radiation decelerates too, so $q=0$ requires $\Omega_m + 2\Omega_r = 2\Omega_\Lambda$.* ⇒ ***On the
leaf rate the pivot and the turnover are two epochs, separated by $\dd u = 5.08\times10^{-4}$, and
the Nariai radius sits BETWEEN them.*** **Which is the correct status for an L1 identification read
on L2 — exact on the stacking rate, approximate on the leaf one.**

## ⌗ ONE INCIDENTAL DEFECT, REPORTED BECAUSE IT IS THE SIZE OF THE EFFECT

*The existing scope-(b) check's leaf integrand carries $\Omega_\Lambda = 1-\Omega$ rather than
$1-\Omega-\Omega_r$, so the three fractions sum to $1+\Omega_r$. Kept flat its own figure reads
$0.99940$ rather than $0.99934$, and* **the slip alone accounts for $10.4\%$ of the shift that figure
is quoted for.**

## ⌗ WHAT IS NOT CLAIMED

*That the leaf rate is the right rate for this object — the corpus's rule assigns it and this
computes the consequence. That $\Omega_r$ is anything but an inherited datum: it is held fixed at
$8.5\times10^{-5}$ and **nothing here is tuned**. And no mechanism for the residual $2\%$ is offered:
the row asked whether the rate explains it, and the answer is that it does not.*

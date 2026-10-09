---
name: r7236-prediction
kind: PREDICTION
job: the expected sign and order of magnitude of the kernel's phase difference between the arms, in ONE form, BEFORE the evaluation
revision: r7236
seat: 60
order: r7223
---

# ⛭ r7236 — PRE-REGISTRATION

`r7223` ordered this and added one thing to the burden that `r7234` earned: ***give the prediction in
ONE form.*** *I offered `r7234`'s size in two forms as restatements and they were not equivalent.*
**The form here is the one the order names: the kernel's phase difference between the two arms, in
degrees, across `$104\le\ell\le1886$`, against the residual's `$-96.6^{\circ}$`.** This file is
committed before any evaluation is run.

## ⌗ WHAT IS BEING EVALUATED, AS AN IDENTITY FIRST

`r7234` derived the `$\ell$`-space comb's shape as the centroid shift of the kernel's own asymptotic
window. Writing `$x=kD_M$`, that window is

    W(x; l) ∝ x^{n_s-2} · exp(-2 (x r_D/D_M)^2) / ( x · sqrt(x^2 - l^2) )

and the oscillation it weights is `$\cos(2xr_s/D_M)$`. ⇒ **So the kernel's phase at multipole
`$\ell$` is**

    ΔΦ(l) = 2 ( x̄(l) - l ) · r_s/D_M ,     x̄ = the window's centroid

***and it depends on exactly two dimensionless numbers: `$r_D/D_M$`, which sets the window's shape,
and `$r_s/D_M$`, which converts the centroid shift into a phase.*** *The phase the order wants is the
RUNNING part — `$\Delta\Phi(1886)-\Delta\Phi(104)$` — because the intercept is already a fitted
parameter and only the slope is the residual's `$-96.6^{\circ}$`.*

## ⛭⛭ THE TWO ARMS' OWN INPUTS, READ OFF THE BANKS BEFORE ANY COMPUTATION

| | `$r_s$` | `$D_M$` | `$r_D$` | `$r_s/D_M$` | `$r_D/D_M$` |
|---|---|---|---|---|---|
| arm | `$145.3281$` | `$13941.629$` | `$7.12$` | `$0.01042404$` | `$5.1070\times10^{-4}$` |
| control | `$144.5281$` | `$13864.663$` | `$7.10$` | `$0.01042420$` | `$5.1210\times10^{-4}$` |
| difference | `$+0.55\%$` | `$+0.55\%$` | `$+0.28\%$` | `$-1.5\times10^{-5}$` | `$-0.27\%$` |

⌗ ***The first two columns differ by half a per cent and the first dimensionless number by fifteen
parts in a million*** — *which is `$\theta_*$`, matched by construction, and that is the whole reason
this is a small number rather than a half-per-cent one.* **The only input that differs at the
per-cent level is `$r_D/D_M$`, at `$0.27$` per cent.**

## ⛭⛭⛭ THE PREDICTION, IN ONE FORM

> ***`$\Delta\Phi_{\text{arm}} - \Delta\Phi_{\text{control}} = +0.06^{\circ}$` across
> `$104\le\ell\le1886$`, of order `$0.1^{\circ}$`, which is THREE ORDERS OF MAGNITUDE below the
> residual's `$-96.6^{\circ}$`.***

*The band I am claiming is `$0.01^{\circ}$` to `$0.3^{\circ}$` in magnitude, and POSITIVE in sign.*

**Where the number comes from, so it can be checked against rather than admired.** *`r7234`'s own
closed-form table gives the kernel's running phase at three values of `$r_D$`: at `$5.00$` Mpc the
peak offsets `$q-n$` run `$-0.0789\to-0.1393$`, a running `$-10.9^{\circ}$`; at `$7.12$` Mpc
`$-0.0566\to-0.1507$`, a running `$-16.9^{\circ}$`; at `$10.88$` Mpc `$-0.0089\to-0.1701$`, a running
`$-29.0^{\circ}$`.* ⇒ *So `$\mathrm{d}\ln|\Delta\Phi|/\mathrm{d}\ln r_D \simeq 1.4$` near the live
value, and `$1.4\times0.27\%\times16.9^{\circ}=0.064^{\circ}$`.* **Sign: the arm's `$r_D/D_M$` is the
SMALLER of the two, a smaller `$r_D$` gives a smaller running phase in magnitude, both are negative,
so arm minus control is POSITIVE.** ⌗ *The `$r_s/D_M$` difference contributes
`$1.5\times10^{-5}\times16.9^{\circ}=0.0003^{\circ}$` and is negligible — which is the structural
point and not an aside.*

## ⇒ SO THE ANSWER I EXPECT IS THE ORDER'S NEGATIVE BRANCH, IN ITS OWN WORDS

**`the kernel is not a carrier, the candidate list stays at the driving, the loading and the clock,
and the projection is cleared`.** *I expect that, and `r7223` is right that it is worth having in
print as a cleared candidate rather than an unexamined one.*

## ⛔ WHAT WOULD REFUTE ME, NAMED IN ADVANCE

1. **The difference is `$\ge10^{\circ}$`** — a tenth of the residual or more. The kernel is a real
   fourth candidate, my prediction is refuted by two orders, and the row has the different kind of
   cycle `r7223` describes.
2. **The difference is `$\ge1^{\circ}$`** — an order above my band. Refuted on size even if the
   `cleared` conclusion survives, and I will say which of the two it is.
3. **The sign is NEGATIVE** — the arm's kernel phase more negative than the control's. Refuted on
   sign, and it would mean my reading of the `$r_D$` sensitivity off `r7234`'s own table is backwards.
4. **The sensitivity is not carried by `$r_D/D_M$`** — e.g. the `$r_s/D_M$` term turns out to
   dominate. That refutes the two-number decomposition the identity above rests on, which is a
   bigger failure than the number.
5. **The kernel's own running phase is not of order `$-17^{\circ}$`** at the live `$r_D$`. That is
   read off `r7234`'s printed table rather than recomputed here, so it is the one input I am taking
   on trust from my own previous revision, and the evaluation must reproduce it independently.

## ⌈ AND THE THIRD OUTCOME, PRE-REGISTERED BECAUSE NEITHER BRANCH OF THE ORDER NAMES IT

`r7223` frames two branches: the kernel is a carrier, or it is cleared. **There is a third and I
expect it to hold alongside the second:** *the DIFFERENCE is three orders down and the kernel is
cleared as a carrier of the residual — and yet the kernel's own ABSOLUTE running phase is of order
`$-17^{\circ}$`, which is a sixth of the residual's `$-96.6^{\circ}$` and is present in ANY spectrum
this instrument projects, the control's included.* ⇒ **So `a running phase at correct spacing` is not
a phase-clean observable: a sixth of the scale the row reads its candidates against is manufactured by
the projection and cancels only because both arms carry it.** *If that is what the evaluation gives I
will say it in those words, because `cleared` and `the observable has a common-mode floor` are
different statements and only the first is what was asked.*

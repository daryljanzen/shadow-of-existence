# `r7614` — REGISTERED BEFORE MEASURING

**The order, `r7613`.** *"Redo steps (i) to (v) of `P15` §properframe on a cut with $m'(r)\neq0$: the
radiation bend `P15` and the slicing-operator paper (`P8`) describe, **not a model of your choosing**.
Then: **(1)** does $r(\tau,\chi)=r(\tau+\chi)$ survive, and with it $\partial_\chi r=\partial_\tau r$?
**(2)** What does a length accumulated along the photon family come to on that cut? Compare it to the
stacking distance (`14011.456` Mpc) and the leaf distance (`13941.629` Mpc). Register the arms before
computing, including a control that returns your `r7612` figure when $m'=0$."* And the clause it set:
*whether the photon family still crosses the leaves at unit cosmic-time rate on the cut as radiation
bends it.*

## The bend is read out of the two papers, not chosen

* `P8` §bend, `prop:bend`: $f(r)=1-2m(r)/r-\Lambda r^{2}/3$ with $m(r)$ a **mass function**, and
  $\rho(r)=m'(r)/4\pi r^{2}$ — *a straight cut has $m'\equiv0$; the bend is $m'\neq0$.*
* `P15` §tensions: radiation's own scaling is $\Omega_r(1+z)^4$, and `P15` §properframe fixes
  $1+z=r(\tilde\tau_0)/r(\tilde\tau_e)$, so **as a radial profile** radiation is
  $\rho_r(r)=\rho_{r,0}(r_0/r)^4$.
* Those two **fix $m(r)$ up to one integration constant**, and the constant is fixed by the bend being a
  *departure* from the straight cut: $m(r_0)=M$. ⌗ **That is the one convention here, and arm Ⓕ measures
  how much the answer depends on it** by fixing it at recombination instead.

## What is derived analytically here, before any number is run

Written out so the measurement cannot be said to have suggested it.

1. **Step (i)–(iii) survive for *every* mass function, and the reason is autonomy.** At $E=1$ the radial
   equation is $(\mathrm{d}r/\mathrm{d}\tau)^2=2m(r)/r+r^2/\alpha^2$, whose right-hand side depends on
   $r$ **alone**. An autonomous first-order equation has solutions that are time-translates of one
   another, so $r=F(\tau+\text{const})$; labelling the congruence by that constant is step (iv), and it
   gives $r(\tau,\chi)=r(\tau+\chi)$ with $\partial_\chi r=\partial_\tau r$ **whatever $m(r)$ is**. Step
   (v)'s $g_{\chi\tau}=0$ then forces the integration function to be $\chi$ itself exactly as before, so
   `eq:proper-frame` keeps its form with $g_{\chi\chi}=(\partial_\chi r)^2=2m(r)/r+r^2/\alpha^2$.
2. **So the answer to (1) is expected to be YES, and the unit cosmic-time rate with it** — which would
   mean the clause `r7613` set answers in the affirmative and the derivation is not confined to the
   vacuum chart.
3. **And then the rate the bent chart carries can be written down.** With
   $m(r)-M=\int_{r_0}^{r}4\pi s^2\rho_r(s)\,\mathrm{d}s=4\pi\rho_{r,0}r_0^3\,(1-r_0/r)$, the extra term
   in $H^2=2Gm(r)/c^2r^3+c^2/\alpha^2$ is $-3H_0^2\Omega_r\,z(1+z)^3$. **So the bend does NOT restore the
   leaf's $+H_0^2\Omega_r(1+z)^4$: it subtracts a term of the same high-$z$ scaling and three times the
   size.** At large $z$, $z(1+z)^3\to(1+z)^4$, so the bent rate is the stacking rate *minus* three times
   the leaf's radiation term.
4. **Which has a consequence sharp enough to be a test:** $H_{\rm bent}^2$ vanishes where
   $\Omega_m(1+z)^3+\Omega_\Lambda=3\Omega_r z(1+z)^3$, i.e. near $1+z\simeq\Omega_m/3\Omega_r$, a few
   hundred above recombination. **Beyond that redshift the bent cut has no real rate at all.**

This is a derivation, not a measurement. Whether it survives the checks below is what the run decides.

## The arms, scored HIT / MISS

**Ⓐ The bend is the papers', located.** `P8`'s mass-function line and `prop:bend`'s
$\rho=m'(r)/4\pi r^2$, and `P15`'s *radiation … requiring $m'(r)\neq0$, a bend of the cut*. ⇒ HIT if all
three are located by containment.

**Ⓑ (1): $r(\tau+\chi)$ and $\partial_\chi r=\partial_\tau r$ survive the bend.** Integrate the bent
radial equation from two different initial radii and check that the two solutions are translates: that
$F(\tau+\chi)$ reproduces both, and that the two partial derivatives agree. ⇒ HIT if the translate test
holds to $10^{-8}$ relative over the sampled range and the derivatives agree to the differencing floor.
**MISS if the bent solutions are not translates**, which would mean the bend breaks step (iv) and the
derivation is confined to the vacuum chart — the outcome that would close `r7612`'s derivation off.

**Ⓒ The unit cosmic-time rate survives.** $\partial_\chi\tilde\tau=\partial_\tau\tilde\tau=1$ with
$\tilde\tau=\tau+\chi$, checked symbolically, and $\partial_\chi r=\partial_\tau r$ measured on the bent
chart. ⇒ HIT if both hold. **This is the clause `r7613` set, and this arm is its whole content.**

**Ⓓ The bend's rate term, measured against the registered derivation.** ⇒ HIT if the measured
$H_{\rm bent}^2-H_{\rm stack}^2$ matches $-3H_0^2\Omega_r z(1+z)^3$ to $10^{-10}$ relative at every
sampled redshift, **and** the ratio of that term to the leaf's $+H_0^2\Omega_r(1+z)^4$ tends to $-3$ at
high $z$. MISS if the measured term is $+H_0^2\Omega_r(1+z)^4$ — in which case the bend *does* restore
the leaf rate, and the sky's preferred distance is what the bent cut computes, which is the strongest
outcome available and the one the order's second branch names.

**Ⓔ (2): the length along the photon family on the bent cut.** $r_0\int\mathrm{d}\tilde\tau/r$ over the
bent chart, reported against `14011.456` (stacking) and `13941.629` (leaf). **Registered prediction: it
is LONGER than the stacking distance, because the bend lowers the rate**, and it is **not** between the
two. ⇒ HIT if longer than `14011.456`; MISS if it lands in `[13941.629, 14011.456]`; **VOID if the bent
rate vanishes below $z_{\rm rec}$**, in which case the integral does not exist and *that* is the result.

**Ⓕ How much the one convention carries.** Refix $m(r_{\rm rec})=M$ instead of $m(r_0)=M$ and report
both. ⇒ HIT if the two differ by less than the gap between the stacking and leaf distances; MISS if the
convention moves the answer by more than that gap, in which case the comparison the order asks for is
convention-limited and the reply says so rather than quoting a number.

**Ⓖ The control the order names.** Set $m'=0$ and the whole chart must return `r7612`'s figures: the
layer-time integral at `14011.456` Mpc and the photon family's accumulation equal to it. ⇒ HIT if both
return to $10^{-8}$ relative. **MISS voids every other arm**, since a chart that does not reproduce the
unbent case cannot be trusted on the bent one.

**Ⓗ The zero-crossing, which the registered derivation predicts and which the papers do not mention.**
⇒ HIT if $H_{\rm bent}^2$ has a real zero and it lies above $z_{\rm rec}=1089.9$; MISS if it has none
below $z=10^4$; **and if the zero lies BELOW $z_{\rm rec}$ this arm carries Ⓔ's VOID with it.**

## What each outcome means for the row

* **Ⓑ Ⓒ HIT with Ⓓ Ⓔ as registered.** The clause `r7613` set answers **yes** — the photon family still
  crosses the leaves at unit cosmic-time rate once radiation bends the cut, so `r7612`'s derivation is
  not an artefact of the vacuum chart — **and the bend does not deliver the leaf-rate distance**: it
  moves the distance the *other* way. Then the sky's preference for the leaf rate is **not** what putting
  radiation into the cut gives, and the row's first branch is the one that holds: the deficit stands as
  the derived spectrum confronted with the sky.
* **Ⓓ MISS.** The bend restores the leaf's term, the bent cut computes the distance the sky prefers, and
  the row's second branch holds — the strongest outcome for the cosmology and the one to report loudest.
* **Ⓑ MISS.** The bend breaks step (iv); `r7612`'s derivation holds only on the vacuum chart, and the
  clause answers **no**, which reopens what `r7612` closed. **Registered so that it can.**
* **Ⓖ MISS.** Nothing here is reportable and the reply says only that.

**No instrument is added**, per `r7471` and `r7577`: no gate, ledger, census or receipt-about-receipts.
No parameter is pinned, so no `COMPUTES:` header is owed. The background and the unbent chart are read
from `r7580`'s script by path, which reads its own background out of the prior `P15` receipt by `ast` —
one instrument, not three. **And if a result here moves a sentence about what is open, `r7577`'s standing
rule applies and the reply says so.**

⌗ **One correction this revision also carries, and it is mine.** `r7612`'s write-up mistyped two rows of
its own metric-component table — the `z = 1` row, which `69` caught at `r7613`, and the `z = 3×10⁷` row,
which is the same slip one row down. Both are corrected from the captured run, in the receipt and in the
register index. No arm, verdict or other figure moves.

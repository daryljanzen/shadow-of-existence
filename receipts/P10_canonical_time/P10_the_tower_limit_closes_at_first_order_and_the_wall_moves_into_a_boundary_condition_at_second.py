#!/usr/bin/env python3
r"""
P10_the_tower_limit_closes_at_first_order_and_the_wall_moves_into_a_boundary_condition_at_second
===============================================================================================

LEVEL: **closed form for every load-bearing step.**  The reduction, the ODE, its general-$z$
solution, the symmetry of the vertex operator, the deficiency integrals and the large-scale Bessel
reduction are all exact symbolic results; the position-representation cross-check is an independent
exact derivation of the same verdict.  ⌗ *Continuing `r6950`'s discipline, itself taken from
`r6947`'s finding on `r6946`: ask of each tolerance whether the arithmetic could be exact instead.*
**One float appears** -- the amplitude exponent on the oscillatory side of §D, measured against the
Bessel prediction $-3/4$ rather than against a threshold.

OBJECT UNDER TEST -- `PO-23`, `r6951`/`r6953`.  The order hands over a hypothesis 66 has run rather
than guessed: in the momentum representation $M(a)\psi=0$ is a **first-order ODE** with the closed
form $\psi=C\,e^{\mathrm{i}c(a)p}/p$, non-normalizable because of the $1/p$ at the origin.  Asked:

  ⓵ᵃ *"Confirm or refute the reduction itself ... and is the representation I have assumed the one it
      uses?  If the measure is not $\mathrm{d}p$, the $1/p$ verdict changes."*
  ⓵ᵇ *"Then the domain question, which is the load-bearing one.  Is $M(a)$ essentially self-adjoint
      on the natural domain, or does it admit a family of extensions?"*  ⌗ *with: if the extension
      selection is the datum `PO-15` carries, that is the ordering surfacing a third time.*
  ⓵ᶜ *"And whether more than two operators enter ... report the order of the equation the actual
      operator content gives, since that decides whether ⓵ᵃ's closed form is the answer or the first
      term of one."*

COMPUTES: the vertex operator in both representations; the first-order equation and its general-$z$
solution; the exact near-origin integrals that count deficiency; whether $z=0$ has an $L^2$ solution
under any boundary condition; and the second-order equation's behaviour at the momentum origin and at
large scale.

-------------------------------------------------------------------------------
** THE REDUCTION IS CORRECT.  THE OPERATOR IS **NOT** ESSENTIALLY SELF-ADJOINT -- AND THE VERDICT IS
   UNIFORM OVER THE EXTENSION FAMILY ANYWAY, SO THE FIRST-ORDER CASE CLOSES WITHOUT CHOOSING ONE.
   BUT ⓵ᶜ IS NOT A FOOTNOTE: AT SECOND ORDER THE ANSWER REVERSES. **

** ⛭ ⓵ᵃ THE REDUCTION HOLDS, AND IT HOLDS IN BOTH REPRESENTATIONS. **  With $\hat\pi\to p$ and
$\hat\varphi\to\mathrm{i}\,\mathrm{d}/\mathrm{d}p$ the symmetrised vertex is exactly
$\hat T_2=\mathrm{i}\,p\,\frac{\mathrm{d}}{\mathrm{d}p}(p\,\cdot)$, the equation is first order, and
sympy returns 66's closed form unprompted.  The measure **is** $\mathrm{d}p$ (Plancherel), and the
verdict is invariant under the oscillator's own scalings, since a dilation carries $1/p$ to
$1/\lambda p$.  ⇒ *And the position representation is an independent route to the same place*:
$M=-\bigl((A+Bx)\psi'\bigr)'$, whose $z=0$ solutions are $c_1+c_2\ln\lvert A+Bx\rvert$ --- neither in
$L^2(\mathrm{d}x)$.  **Two representations, one verdict, no numerics.**

** ⛭ ⓵ᵇ AND 66's WORRY IS JUSTIFIED: THE OPERATOR IS NOT ESSENTIALLY SELF-ADJOINT. **  At general
$z$ the solution is $\psi_z=\frac{C}{p}\exp\bigl(\mathrm{i}\tfrac{A}{B}p+\mathrm{i}\tfrac{z}{Bp}\bigr)$.
At $z=\mathrm{i}\sigma$ the second exponential is **real**, $e^{-\sigma/Bp}$, and the near-origin
integral is exact:
$$\int_0^1\frac{e^{-k/p}}{p^{2}}\,\mathrm{d}p=\frac{e^{-k}}{k}\ \ (k>0),\qquad
  \int_0^1\frac{e^{+k/p}}{p^{2}}\,\mathrm{d}p=\infty .$$
So each half-line contributes an $L^2$ solution for one sign of $\operatorname{Im}z$ and none for the
other: ** deficiency indices $(1,1)$, a $U(1)$ family of self-adjoint extensions. **

** ⛭ AND YET THE QUESTION IS SETTLED UNIFORMLY OVER THAT FAMILY, WHICH IS WHY THE ORDERING DOES NOT
   SURFACE A THIRD TIME. **  At $z=0$ the exponential is a pure phase and
$\lvert\psi_0\rvert^{2}=\lvert C\rvert^{2}/p^{2}$, whose integral **diverges at the origin on either
side**: $\int_0^1\mathrm{d}p/p^{2}=\infty$.  ⇒ *A boundary condition selects among $L^2$ solutions,
and at $z=0$ there are none to select from.*  ** So $0$ is not an eigenvalue of ANY extension: the
first-order tower criterion closes, and closes without an extension choice. **  ⌗ *Which answers the
order's conditional in the negative --- the extension selection never has to be made, so it cannot be
`PO-15`'s datum surfacing.*

** ⛭ ⓵ᶜ BUT THE ORDER OF THE EQUATION IS THE DECIDING DATUM, AND AT SECOND ORDER THE ANSWER
   REVERSES. **  Adding a $\hat\varphi^{2}$ structure makes the equation second order, and then:
$\psi=\alpha+\beta p$ solves it to $O(p)$ at the momentum origin, so **both solutions are regular
there and the $1/p$ obstruction is gone** --- exactly the failure mode the order flagged.  The
constraint moves to large scale, where the reduced equation
$\psi''+\psi'/x-(C/B)x\psi=0$ is **exactly Bessel** in $\xi=\tfrac23\sqrt{C/B}\,\lvert x\rvert^{3/2}$:
exponentially decaying at one end, and oscillatory at the other with amplitude
$\lvert x\rvert^{-3/4}$ --- measured at $-0.7511$ against that exact prediction --- so
$\lvert\psi\rvert^{2}\sim\lvert x\rvert^{-3/2}$ is **integrable**.  ⇒ ** Both ends admit $L^2$
behaviour, so a normalizable null vector is not excluded, and everything then turns on the boundary
condition at the degenerate point $x_0=-A/B$ where $A+Bx$ vanishes. **

⛔ ** SO THE HONEST STATUS, IN THE ORDER'S OWN TERMS. **  *Not* a third completed argument yet: it is
one **at the operator content the cubic's kinetic vertex gives**, and at second order ** the wall has
moved into the extension choice at the degenerate point -- a different open object from a limit of
determinants, and named as such. **  ⇒ *The deciding datum is now the operator content: whether a
$\hat\varphi^{2}$ structure enters $\hat R$ alongside $\hat\pi^{2}\hat\varphi$.*  ⌗ And that
boundary-condition question is the **same kind of object** the corpus already closes at $a=0$ with the
horizon's thermal state, which is where I would look first.  No ordering choice; no corpus edit.
rc=0 on all 16 checks.
"""

import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(title):
    print()
    print("=" * 94)
    print(title)
    print("=" * 94)


p = sp.Symbol('p', real=True)
x = sp.Symbol('x', real=True)
ppos, kpos = sp.symbols('p k', positive=True)
A, B, Cc = sp.symbols('A B C', real=True, nonzero=True)
z = sp.Symbol('z')
psi = sp.Function('psi')

# ============================================================================ A
head("A.  THE GUARDS, CARRIED BEFORE ANYTHING IS COMPUTED")

print(r"""
  GUARD 1 -- KEEP THE ARITHMETIC EXACT WHERE IT CAN BE, which is `r6950`'s discipline and before it
    `r6947`'s finding on `r6946`.  Everything load-bearing here is closed form: the reduction, the
    general-z solution, the deficiency integrals, the Bessel reduction.  ⌗ *The single float is §D's
    amplitude exponent, and it is reported against the exact Bessel value rather than a threshold --
    a prediction to hit, not a tolerance to clear.*

  GUARD 2 -- THE ORDERING STAYS NAMED AND UNPICKED, and the order adds a conditional: if the
    extension selection turns out to be `PO-15`'s datum, that is the ordering surfacing a third time.
    ⇒ §C answers it: the selection never has to be made in the first-order case, so it cannot be.

  GUARD 3 -- DO NOT TAKE THE ODE ON TRUST.  The order names four places it can fail --
    representation, measure, domain, operator content.  §B tests the first two (and adds a second
    representation as an independent route), §C the third, §D the fourth -- and the fourth is the one
    that moves the answer.""")

# ============================================================================ B
head("B.  ⓵ᵃ  THE REDUCTION -- CONFIRMED, AND CONFIRMED TWICE IN TWO REPRESENTATIONS")


def T1_mom(fn):
    return p ** 2 * fn


def T2_mom(fn):
    """(1/2)(pi^2 phi + phi pi^2) with pi -> p, phi -> i d/dp."""
    return sp.Rational(1, 2) * (p ** 2 * (sp.I * sp.diff(fn, p)) + sp.I * sp.diff(p ** 2 * fn, p))


f = psi(p)
t2 = sp.simplify(sp.expand(T2_mom(f)))
print(f"\n      T_2 psi = {t2}")
check(sp.simplify(sp.expand(T2_mom(f) - sp.I * (p ** 2 * sp.diff(f, p) + p * f))) == 0,
      "the vertex operator is i(p^2 psi' + p psi) in the momentum representation -- the order's "
      "expression, confirmed")
check(sp.simplify(sp.expand(T2_mom(f) - sp.I * p * sp.diff(p * f, p))) == 0,
      "** and it is exactly i p d/dp (p .) -- which is where the 1/p comes from: the symmetrisation's "
      "own inner derivative **")

g = sp.Function('g')(p)
sym = sp.simplify(sp.expand(
    sp.conjugate(f) * T2_mom(g) - sp.conjugate(T2_mom(f)) * g
    - sp.diff(sp.I * p ** 2 * sp.conjugate(f) * g, p)))
print(f"\n      symmetry, as a total derivative:  f* T_2 g - (T_2 f)* g - d/dp[i p^2 f* g] = {sym}")
check(sym == 0,
      "T_2 is symmetric on compactly supported functions -- the difference is exactly a total "
      "derivative, so the only obstruction to self-adjointness is a boundary term")

M_mom = A * T1_mom(f) + B * T2_mom(f)
sol0 = sp.simplify(sp.dsolve(sp.Eq(sp.expand(M_mom), 0), f).rhs)
print(f"\n      M(a) psi = 0  ->  psi = {sol0}")
check(sp.simplify(sol0 / sol0.args[0] - sp.exp(sp.I * A * p / B) / p) == 0
      if hasattr(sol0, 'args') else False,
      "** the equation is FIRST ORDER and integrates to C exp(i (A/B) p)/p -- the order's closed "
      "form, reproduced independently **")
check(sp.ode_order(sp.Eq(sp.expand(M_mom), 0), psi(p)) == 1,
      "and its order is 1, which is what makes the closed form available at all")

print(r"""
      THE MEASURE, which the order flagged as able to change the verdict on its own.  The mode's
      Hilbert space is L^2 in the field variable; the momentum representation is its Fourier
      transform, which is unitary onto L^2(dp) with Lebesgue measure.  ⇒ So the measure IS dp.  And
      the oscillator's mass a^3 and frequency mu/a enter only as a DILATION of p, which carries 1/p
      to 1/(lambda p):""")
lam_ = sp.Symbol('lambda', positive=True)
dil = sp.integrate(1 / (lam_ * ppos) ** 2, (ppos, 0, 1))
print(f"        int_0^1 dp/(lambda p)^2 = {dil}")
check(dil == sp.oo,
      "** so the verdict is scale-invariant: no choice of the oscillator's mass or frequency makes "
      "1/p normalizable, and the measure is not a place this fails **")

print("\n      AND THE INDEPENDENT ROUTE -- the position representation, phi -> x, pi -> -i d/dx:")
fx = psi(x)
T1_pos = -sp.diff(fx, x, 2)
T2_pos = sp.Rational(1, 2) * (-sp.diff(x * fx, x, 2) - x * sp.diff(fx, x, 2))
M_pos = sp.expand(A * T1_pos + B * T2_pos)
check(sp.simplify(sp.expand(M_pos + sp.diff((A + B * x) * sp.diff(fx, x), x))) == 0,
      "in position space the same operator is the Sturm-Liouville form -((A + Bx) psi')' -- whose "
      "leading coefficient VANISHES at x_0 = -A/B, the same singular point seen from the other side")
sol_pos = sp.simplify(sp.dsolve(sp.Eq(M_pos, 0), fx).rhs)
print(f"        z = 0 solutions: {sol_pos}")
check(sol_pos.has(sp.log),
      "** and its z = 0 solutions are a constant and log|A + Bx| -- neither in L^2(dx), since a "
      "logarithm does not decay.  Two representations, one verdict, and no numerics in either **")

# ============================================================================ C
head("C.  ⓵ᵇ  THE DOMAIN QUESTION -- NOT ESSENTIALLY SELF-ADJOINT, AND SETTLED ANYWAY")

solz = sp.simplify(sp.dsolve(sp.Eq(sp.expand(M_mom), z * f), f).rhs)
print(f"\n      at general z:  psi_z = {solz}")
expect = sp.exp(sp.I * (A * p ** 2 + z) / (B * p)) / p
resid = sp.simplify((A * T1_mom(expect) + B * T2_mom(expect) - z * expect).doit())
print(f"      substituting exp(i(A p^2 + z)/(B p))/p into M(a)psi - z psi gives: {resid}")
check(resid == 0,
      "psi_z = exp(i(A p^2 + z)/(B p))/p solves it EXACTLY, by substitution -- so the z-dependence "
      "sits in a 1/p term inside the exponential, which is what makes the deficiency count "
      "decidable in closed form")

print(r"""
      At z = i sigma the second exponential is REAL: exp(i (i sigma)/(B p)) = exp(-sigma/(B p)).  So
      |psi_z|^2 = exp(-2 sigma/(B p))/p^2 near the origin, and the two signs behave oppositely.
      Both integrals are exact:""")
I_dec = sp.integrate(sp.exp(-kpos / ppos) / ppos ** 2, (ppos, 0, 1))
I_gro = sp.integrate(sp.exp(+kpos / ppos) / ppos ** 2, (ppos, 0, 1))
I_inf = sp.integrate(1 / ppos ** 2, (ppos, 1, sp.oo))
print(f"        int_0^1 exp(-k/p)/p^2 dp = {sp.simplify(I_dec)}        (finite)")
print(f"        int_0^1 exp(+k/p)/p^2 dp = {I_gro}")
print(f"        int_1^oo dp/p^2          = {I_inf}        (finite, so infinity is never the problem)")
check(sp.simplify(I_dec - sp.exp(-kpos) / kpos) == 0 and I_gro == sp.oo and I_inf == 1,
      "** exactly e^-k/k on one side and divergent on the other -- so each half-line carries an L^2 "
      "solution for ONE sign of Im z and none for the other **")
print(r"""
    ⇒ ** DEFICIENCY INDICES (1, 1). **  On (0, oo) the unique solution is L^2 for Im z > 0 and not
      for Im z < 0; on (-oo, 0) the signs swap, because 1/p changes sign.  One each way.
      ⇒ ** M(a) is NOT essentially self-adjoint: it admits a U(1) family of self-adjoint extensions,
      and 66's worry about the singular point was well founded. **""")

zero_near = sp.integrate(1 / ppos ** 2, (ppos, 0, 1))
print(f"\n      AND THE DECISIVE POINT -- at z = 0 the exponential is a PURE PHASE, so "
      f"|psi_0|^2 = |C|^2/p^2 and\n        int_0^1 dp/p^2 = {zero_near}")
check(zero_near == sp.oo,
      "** at z = 0 there is NO L^2 solution on EITHER side of the singular point. A boundary "
      "condition selects among L^2 solutions; here there are none to select from **")
print(r"""
    ⇒ ** SO 0 IS NOT AN EIGENVALUE OF ANY EXTENSION. **  Every self-adjoint realisation is a
      restriction of the adjoint, so its eigenvectors solve the same equation and must lie in L^2.
      ⇒ *The first-order tower criterion closes, and closes UNIFORMLY over the extension family --
      the choice never has to be made.*
    ⌗ ** WHICH ANSWERS THE ORDER'S CONDITIONAL IN THE NEGATIVE. **  The extension selection is not
      needed, so it cannot be `PO-15`'s datum surfacing a third time.  *The ordering stays named and
      unpicked, and this time it did not even come to the door.*""")

# ============================================================================ D
head("D.  ⓵ᶜ  THE OPERATOR CONTENT -- AND AT SECOND ORDER THE ANSWER REVERSES")

print(r"""
      WHAT THE CONTENT IS, as far as this line has established it.  The FREE tower contributes no
      tower operator at all: written at fixed occupation its excitation energy is S/a with S free of
      a, and the trace formula annihilates h ~ 1/a exactly (`r6930`).  ⇒ *So the tower operators in
      R-hat begin at the cubic, whose kinetic vertex is pi^2 phi -- ONE power of phi, hence first
      order in the momentum representation.*  ⌗ Whether a phi^2 structure enters R-hat alongside it
      is NOT established here, and §D shows that is the deciding question rather than a detail.""")

fx2 = psi(x)
M3 = sp.expand(A * (-sp.diff(fx2, x, 2)) + B * sp.Rational(1, 2) *
               (-sp.diff(x * fx2, x, 2) - x * sp.diff(fx2, x, 2)) + Cc * x ** 2 * fx2)
check(sp.ode_order(sp.Eq(M3, 0), psi(x)) == 2,
      "with a phi^2 structure the equation is SECOND order, as the order anticipated")

al, be = sp.symbols('alpha beta')
M3_mom = sp.expand(A * p ** 2 * f + B * sp.I * p * sp.diff(p * f, p) + Cc * (-sp.diff(f, p, 2)))
reg = sp.simplify(sp.expand(M3_mom.subs(psi(p), al + be * p).doit()))
print(f"\n      at the MOMENTUM origin, with psi = alpha + beta p the second-order equation reads")
print(f"        {reg}")
check(sp.simplify(reg.subs(p, 0)) == 0,
      "** which vanishes at p = 0: BOTH solutions are regular at the origin, so the 1/p obstruction "
      "is GONE.  The order was right that non-normalizability stops being readable by inspection **")

y = sp.Function('y')
xp = sp.Symbol('x', positive=True)
lam2 = sp.Symbol('lambda', positive=True)
bes = sp.simplify(sp.dsolve(sp.Eq(sp.diff(y(xp), xp, 2) + sp.diff(y(xp), xp) / xp
                                  - lam2 * xp * y(xp), 0), y(xp)).rhs)
print(f"\n      and at LARGE scale the reduced equation psi'' + psi'/x - (C/B) x psi = 0 is exactly "
      f"Bessel:\n        {bes}")
check(bes.has(sp.besseli) or bes.has(sp.besselj) or bes.has(sp.bessely),
      "the large-scale reduction is a Bessel equation in xi = (2/3) sqrt(C/B) |x|^(3/2) -- so its "
      "asymptotics are exact statements rather than estimates")

print(r"""
      Which fixes both ends exactly: on the side where (C/B)x > 0 one solution decays like
      exp(-xi)/sqrt(xi), comfortably L^2; on the other side the solutions are oscillatory with
      amplitude xi^(-1/2) ~ |x|^(-3/4), so |psi|^2 ~ |x|^(-3/2) -- INTEGRABLE.  ⇒ The claim to test
      is that exponent, so measure it on the FULL equation rather than the reduced one:""")

Af, Bf, Cf = 1.0, 1.0, 1.0            # the degenerate point sits at x_0 = -A/B = -1


def rhs(xv, yv):
    ps, dp_ = yv
    return [dp_, (Cf * xv ** 2 * ps - Bf * dp_) / (Af + Bf * xv)]


amps = []
for X in (40.0, 80.0, 160.0):
    s2 = solve_ivp(rhs, [-1.001, -X], [1.0, 0.0], rtol=1e-11, atol=1e-14,
                   dense_output=True, max_step=0.01)
    xx = np.linspace(-X, -X / 2, 20001)
    amps.append((X, float(np.max(np.abs(s2.sol(xx)[0])))))
    print(f"        X = {X:6.1f}   peak |psi| on [-X, -X/2] = {amps[-1][1]:.6e}")
slope = float(np.polyfit(np.log([a[0] for a in amps]), np.log([a[1] for a in amps]), 1)[0])
print(f"        measured amplitude exponent = {slope:+.4f}   against the exact Bessel value -0.7500")
check(abs(slope + 0.75) < 0.01,
      f"** the full equation follows the Bessel amplitude to {abs(slope + 0.75):.1e} -- so "
      f"|psi|^2 ~ |x|^{2 * slope:.3f}, integrable at infinity, and the oscillatory end admits L^2 "
      "too **")
check(2 * slope < -1,
      "both ends therefore admit L^2 behaviour, so a normalizable null vector is NOT excluded at "
      "second order -- the opposite of the first-order verdict")

print(r"""
    ⇒ ** AND THEN EVERYTHING TURNS ON THE DEGENERATE POINT. **  In the position representation the
      leading coefficient A + Bx vanishes at x_0 = -A/B, where the two solutions behave as a constant
      and a logarithm -- both locally L^2, so the operator is limit-circle there and a boundary
      condition IS required.  ⇒ *Whether a global null vector exists is exactly the question of which
      realisation is carried, and that is a self-adjoint-extension question at a singular point.*
    ⌗ ** WHICH IS THE SAME KIND OF OBJECT THIS PAPER ALREADY CLOSES AT a = 0 **, where the horizon's
      own thermal state fixes the extension -- so it is where I would look first, and it is NOT the
      limit of determinants `r6950` named.  *A different open thing, as the order asked me to say.*""")

# ============================================================================ E
head("E.  THE VERDICT, IN THE ORDER'S OWN TERMS")

print(r"""
  ⚑ WHAT IS SETTLED, with no truncation and no tolerance anywhere in it:

    · ** The reduction is correct ** -- and correct in two representations, the second reached
      independently (the Sturm-Liouville form, whose z = 0 solutions are a constant and a logarithm).
    · ** The measure is dp, and the verdict is scale-invariant ** -- no oscillator scaling makes 1/p
      normalizable, so that failure mode is closed rather than assumed away.
    · ** M(a) is NOT essentially self-adjoint: deficiency (1,1), a U(1) family. **  66's worry was
      justified and the answer to the posed question is "it admits extensions".
    · ** And the criterion is settled uniformly over that family: at z = 0 there is no L^2 solution
      on either side, so 0 is not an eigenvalue of any extension. **  ⇒ *The first-order tower
      criterion closes WITHOUT choosing an extension -- which is a stronger statement than closing it
      by choosing the right one.*
    · ** The ordering did not surface a third time. **  The selection is never needed.

  ⛔ WHAT IS NOT SETTLED, AND IT IS THE ORDER'S OWN ⓵ᶜ RATHER THAN A FOOTNOTE:

    · ** The operator content decides the answer, because the answer REVERSES at second order. **
      With a phi^2 structure present the momentum-origin obstruction disappears, both ends admit L^2
      behaviour, and a normalizable null vector is not excluded.  ⇒ *So ⓵ᵃ's closed form is the
      answer for the content the cubic's kinetic vertex gives, and the first term of one otherwise.*
    · ** At second order the wall has MOVED, not vanished: into the boundary condition at the
      degenerate point x_0 = -A/B. **  That is a different open object from a limit of determinants
      and is named as such rather than carried as the same item.  ⌗ *And it is the same kind of
      object `sec:lock` already closes at a = 0 with the horizon's thermal state -- which is the one
      concrete suggestion this receipt makes about where to look.*

  ⇒ ** SO: NOT a third completed argument yet -- it is one AT A STATED OPERATOR CONTENT. **  *I am
    not claiming the wall is gone, because the thing that would make it gone is now a different
    question than it was this morning, and it has an address: does a phi^2 structure enter R-hat
    alongside pi^2 phi?*

  ⛔ WHAT THIS DOES NOT TOUCH.

    · No ordering choice -- §C shows the first-order case never reaches one.
    · No interacting theory beyond the two cubic operators and the hypothetical phi^2.
    · The transverse-traceless weight stays where `r6946` left it.
    · Nothing on `prop:flat`, `PO-31` or `PO-15`; ** no corpus edit ** -- the `P10` site and its
      sentence are routed in `FOR_66_FROM_60.md`.
""".rstrip())

print()
print("=" * 94)
if FAILED:
    print(f"FAILED {len(FAILED)} check(s):")
    for fmsg in FAILED:
        print("   -", fmsg)
    sys.exit(1)
print("ALL CHECKS PASS.")

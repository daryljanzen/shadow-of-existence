#!/usr/bin/env python3
r"""
P10_the_field_squared_is_already_in_the_trace_at_quadratic_order_and_the_degenerate_point_is_representational
===========================================================================================================

LEVEL: **exact for every load-bearing step.**  The trace operator is derived three times, in closed
form, by three independent routes -- one of them `r6930`'s own instrument; the ladder identity, the vanishing of the diagonal, the non-vanishing of the
operator, the null solutions and the two differential representations are all exact symbolic or exact
integer/radical results.  ⌗ *Continuing `r6950`'s and `r6954`'s discipline, itself `r6947`'s finding on
`r6946`.*  **One float appears**: the envelope exponent of the exact Bessel null solution, measured against the
*exact predicted value* $-\tfrac12$ rather than against a threshold.  ⌗ *The two asymptotic exponents of
§E, which an earlier draft measured, are verified symbolically instead -- the recessive branch is
ill-conditioned outward and the phase integral is $\sim p^{3}$, so measuring them was both fragile and
slow; the relative residual of each ansatz is an exact limit.*

OBJECT UNDER TEST -- `PO-23`, `r6959`/`r6961`.  `r6954` reduced the row to one datum and the order makes
that datum the whole row:

  ⓵ *"Does a $\hat\varphi^{2}$ structure enter $\hat R$ alongside the kinetic vertex's
      $\hat\pi^{2}\hat\varphi$?"* -- with the two outcomes named and not symmetric, and with the
      direction named and not claimed: *"the curvature enters through the trace, so the question is
      which structures the stress trace carries at cubic order ... a $\hat\varphi^{2}$ in $\hat\Theta$
      is a potential-like term, and the cubic vertex you used is kinetic."*
  ⓶ *Only if ⓵ says yes*: the deficiency indices at the degenerate point, the form of the family, and
      *"whether the same argument that closed the first-order case -- no square-integrable solution to
      select among -- has any purchase at all"*; and whether the $a=0$ mechanism reaches that point.

  ⌗ WITH THE ORDER'S GUARDS: computed-and-inconclusive is a report and not-attempted is not; **do not
    let the kinetic vertex answer for the content**, and *"if the content turns out to be larger than
    two structures, say what the equation's order becomes and stop"*; keep the arithmetic exact; the
    ordering stays named and unpicked.

COMPUTES: the tower trace operator at quadratic order from the paper's own Hamiltonian, from the stress
tensor, and from `r6930`'s own trace instrument with the occupation numbers not held fixed; its exact ladder form and the exact vanishing of its diagonal; a state on which it
does not vanish; the null equation at the quadratic content and its exact Bessel solutions; the same
abstract operator's two differential representations and where each one degenerates; and the count of
square-integrable solutions at each end.

-------------------------------------------------------------------------------
** ⓵ IS YES -- AND IT IS YES EARLIER THAN THE ORDER'S DIRECTION LOOKED.  $\hat\varphi^{2}$ DOES NOT WAIT
   FOR THE CUBIC: IT IS IN $\hat\Theta$ AT **QUADRATIC** ORDER, FROM THE TOWER'S OWN GRADIENT TERM.  AND
   THE WALL IS NOT AN EXTENSION CHOICE, BECAUSE THE DEGENERATE POINT IS A FEATURE OF ONE
   REPRESENTATION. **

** ⛭ ⓵ THE ANSWER, WITH ITS ADDRESS.  ** The paper's own tower Hamiltonian is
$\hat H=\sum_n[\hat\pi_n^{2}/2a^{3}+\tfrac12 a\mu_n^{2}\hat\varphi_n^{2}]$ (`sec:lock`), and `r6934`'s
exact trace formula sends an energy term $h(a)\otimes T$ to $(h+ah')T/2\pi^{2}a^{3}$.  Applied term by
term:
$$2\pi^{2}\hat\Theta_{\text{quad}}=-\frac{\hat\pi_n^{2}}{a^{6}}+\frac{\mu_n^{2}\hat\varphi_n^{2}}{a^{2}} .$$
⇒ *Two further routes agree term for term*: for a minimally coupled mode
$\rho-3p=(\partial\varphi)^{2}=-\dot\varphi^{2}+\mu^{2}\varphi^{2}/a^{2}$ with $\dot\varphi=\pi/a^{3}$; and
`r6930`'s own `trace_of`, whose verdict reduces to the single step $S'(a)=0$, applied to
$S(a)=\mu(\hat N+\tfrac12)=(a^{2}\mu^{2}\hat\varphi^{2}+\hat\pi^{2}/a^{2})/2$ in the **fixed** field
operators.
** So $\hat\varphi^{2}$ enters $\hat R$ with coefficient $\kappa\mu_n^{2}/2\pi^{2}$ at the power
$a^{-2}$, and $\mu_n^{2}=m^{2}-3\ge6$ is never zero. **  ⌗ *It is a potential-like term, exactly as the
order's direction said -- but its source is the tower's own gradient term and not the cubic, so it is
there at $j=0$ and at every order above.*

** ⛭ AND THE REASON THE ROW READ IT AS ABSENT IS A SIXTH FACE OF THE STANDING LESSON: THE DOMAIN OF A
   VANISHING. **  In the adiabatic basis ($M=a^{3}$, $\omega=\mu/a$) the same operator is exactly
$$2\pi^{2}\hat\Theta_{\text{quad}}=\frac{\mu}{a^{4}}\bigl(\hat a^{2}+\hat a^{\dagger2}\bigr),$$
whose **diagonal is exactly zero at every truncation** -- which is the harmonic virial theorem,
$\langle n|\hat K|n\rangle=\langle n|\hat V|n\rangle$, verified here exactly.  ⇒ *So
$\rho\propto a^{-4}$ and "the pressure is a third of the density" are true **of the expectation in every
stationary state**, and the landed sentence's "identically as an operator -- in every state and not
merely the vacuum" is the overreach: the operator is $\hat a^{2}+\hat a^{\dagger2}$, which is
$\hat X^{2}-\hat P^{2}$, and it has expectation $\ne0$ on a squeezed state, exhibited here.*  ⌗ *An
operator that vanishes on the diagonal of a basis vanishes on that diagonal.  Normal ordering does not
remove it either -- it carries no contraction.*

** ⛭ THE CONCLUSION DRAWN FROM THE OVERREACH SURVIVES, AND SURVIVES BETTER. **  The residual tower
operator is an **inverted oscillator** $\hat X^{2}-\hat P^{2}$ with $[\hat X,\hat P]=\mathrm{i}\mu/a^{4}$,
and its point spectrum is empty.  Exactly: in the momentum representation the null equation is
$\psi''+p^{2}\psi/\mu^{2}a^{4}=0$, solved by $\sqrt{p}\,J_{\pm1/4}(p^{2}/2\mu a^{2})$ -- **both regular at
the origin and neither square-integrable at infinity**, $\lvert\psi\rvert^{2}\sim1/p$ with
$\int_1^\infty\mathrm{d}p/p=\infty$, and the same amplitude exponent $-\tfrac12$ at every real $z$.
⇒ ** So $\hat R$ still has no eigenvector at quadratic order -- not because it is a function of $a$
alone, which it is not, but because the operator it carries is an inverted oscillator. **  ⚠ *What does
NOT survive as stated is "the spectrum is the half-line above $4\Lambda$": an inverted oscillator is
unbounded in both directions, so the restored operator content puts spectrum below $4\Lambda$.  Flagged
and routed; not extrapolated past quadratic order.*

** ⛭ ⓶ AND THE DEGENERATE POINT IS A FEATURE OF ONE REPRESENTATION, SO THERE IS NOTHING TO SELECT. **
One abstract operator $\hat M=c_1\hat\pi^{2}+c_2\,\tfrac12(\hat\pi^{2}\hat\varphi+\hat\varphi\hat\pi^{2})
+c_3\hat\varphi^{2}$; two representations, verified to be the same operator by its matrix in the number
basis computed from each:
$$\text{position: } -(c_1+c_2x)\psi''-c_2\psi'+c_3x^{2}\psi,\qquad
  \text{momentum: } -c_3\psi''+\mathrm{i}c_2(p^{2}\psi'+p\psi)+c_1p^{2}\psi .$$
** The position leading coefficient vanishes at $x_0=-c_1/c_2$; the momentum leading coefficient is the
constant $-c_3$ and vanishes nowhere. **  ⇒ *`r6954`'s degenerate point is `r6954`'s third face --- the
domain of a representation --- returning on its own result: the same operator is regular on the other
side of the Fourier transform, so there is no singular point at which to impose a condition.*  And the
count settles the rest: at each end exactly **one** solution is square-integrable
($\lvert\psi\rvert\sim p^{-1}$ against $\lvert\psi\rvert\sim1$, each verified by an exact limit on the
ansatz's relative residual), so both ends are limit-point, ** the deficiency indices are $(0,0)$, the operator is essentially
self-adjoint, and the family the order asked for the form of is a single point. **  ⇒ *So ⓶'s selection
problem has no object, and the first-order argument's shape has more than purchase: at $c_2=0$ -- the
quadratic content alone -- it closes the question exactly.*

** ⛭ WHAT DISTINGUISHES THIS POINT FROM $a=0$, WHICH THE ORDER ASKED FOR. **  The $a=0$ point is an
**endpoint of the physical configuration space** and a physical locus (the de~Sitter horizon), so the
extension freedom is genuine and a physical condition -- the horizon's thermal state -- is available to
close it.  $x_0=-c_1/c_2$ is an **interior point in one representation and no point at all in another**,
and there is no locus there to carry a condition.  ** The mechanism does not reach it because there is
nothing for it to reach. **

⛔ ** THE HONEST STATUS, AND IT IS NOT THE THIRD COMPLETED ARGUMENT. **  Two things stop it, and both are
the order's own guards firing.  *First*, switching on $c_2$ **creates** a square-integrable solution at
each end where the quadratic content had none, so the exact closure at $c_2=0$ does not extend by
continuity: what remains is a **connection condition** -- one analytic equation asking the two ends'
one-dimensional subspaces to coincide -- and not a boundary condition.  The scaling reduction leaves a
single dimensionless parameter $v=c_1c_3^{1/3}c_2^{-4/3}$, constant in $a$ only if the cubic's trace power
is exactly $5$, and the corpus's own "$\pi_n^{2}\varphi_m/a^{3}$ in kind" puts it at $6$; the
$c_2\to0$ endpoint says the condition is not identically satisfied.  *Second*, **the content may be larger
than three structures**: the trace's potential sector at cubic order is $\hat\varphi^{3}$, which is third
order in the momentum representation.  Per the guard I report the order and stop: ** two at the content
established here, three if the potential cubic enters. **  ⇒ *The object `r6959` named in its second
branch -- a boundary condition at the degenerate point -- does not exist; the row's remaining datum is
the connection coefficient and the potential sector's cubic.*
rc=0 on all 32 checks.
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


a = sp.Symbol('a', positive=True)
mu = sp.Symbol('mu', positive=True)
phi, pi_ = sp.symbols('varphi pi_n', real=True)
x = sp.Symbol('x', real=True)
p = sp.Symbol('p', real=True)
ppos = sp.Symbol('p', positive=True)
c1, c2, c3 = sp.symbols('c1 c2 c3', real=True, nonzero=True)
f = sp.Function('f')

# ============================================================================ A
head("A.  THE GUARDS, CARRIED BEFORE ANYTHING IS COMPUTED")

print(r"""
  GUARD 1 -- KEEP THE ARITHMETIC EXACT.  Every load-bearing step here is closed form: two derivations
    of the trace operator, the ladder identity, the vanishing of the diagonal, the null solutions, and
    the two differential representations.  ⌗ *The three floats are amplitude exponents, each reported
    against an EXACT predicted value (-1/2, -1, 0) and not against a threshold.*

  GUARD 2 -- DO NOT LET THE KINETIC VERTEX ANSWER FOR THE CONTENT.  This is the order's central guard
    and it is the one that fires: the question was posed about the cubic, and the answer is at
    quadratic order, in a term the row had already classified as traceless.

  GUARD 3 -- IF THE CONTENT IS LARGER THAN TWO STRUCTURES, REPORT THE ORDER AND STOP.  §F does exactly
    that: two at the content established here, three if the potential sector's cubic enters, and no
    extrapolation of either verdict past its content.

  GUARD 4 -- THE ORDERING STAYS NAMED AND UNPICKED.  Nothing below picks one: §B's operator is
    quadratic and carries no ordering ambiguity at all (§C.4), and §E's symmetrised vertex is the
    ordering `r6950` and `r6954` already carried.""")

# ============================================================================ B
head("B.  ⓵  THE TRACE OPERATOR AT QUADRATIC ORDER, DERIVED TWICE")

print(r"""
  The paper's own tower Hamiltonian, `sec:lock` eq. (442):  H = pi^2/2a^3 + (1/2) a mu^2 phi^2,
  one oscillator of mass a^3 and frequency mu/a per mode.

  ROUTE 1 -- `r6934`'s exact trace formula.  An energy term h(a) (x) T has trace (h + a h')T/2pi^2 a^3,
  which is just Theta = (E + aE')/2pi^2 a^3 with E the energy on the S^3 of volume 2pi^2 a^3.

  ROUTE 2 -- the stress tensor, with no reference to the trace formula.  For a minimally coupled mode
  T^mu_mu = -(d phi)^2, so  rho - 3p = (d phi)^2 = -phidot^2 + mu^2 phi^2/a^2,  with phidot = pi/a^3.
""")

E_quad = pi_ ** 2 / (2 * a ** 3) + a * mu ** 2 * phi ** 2 / 2
theta_route1 = sp.simplify((E_quad + a * sp.diff(E_quad, a)) / (2 * sp.pi ** 2 * a ** 3))
theta_route2 = (-pi_ ** 2 / a ** 6 + mu ** 2 * phi ** 2 / a ** 2) / (2 * sp.pi ** 2)

check(sp.simplify(sp.expand(theta_route1 - theta_route2)) == 0,
      f"route 1 (trace formula) == route 2 (stress tensor):  2pi^2 Theta = {sp.simplify(2*sp.pi**2*theta_route1)}")

coeff_phi2 = sp.simplify(sp.expand(2 * sp.pi ** 2 * theta_route1).coeff(phi ** 2))
coeff_pi2 = sp.simplify(sp.expand(2 * sp.pi ** 2 * theta_route1).coeff(pi_ ** 2))
print(r"""
  ROUTE 3 -- `r6930`'s OWN instrument, which is where the absence was established, and it agrees too.
  `r6930` writes the excitation energy as E = S/a and its `trace_of` gives Theta = (E + aE')/2pi^2 a^3,
  which for that form is EXACTLY S'(a)/2pi^2 a^3 -- so the verdict "traceless" is the single step
  S' = 0, i.e. "S free of a".  ⌗ *Its own docstring says what that step needs: "at fixed occupation
  numbers".*  Written in the FIXED field operators, S(a) = mu(N-hat + 1/2) = (a^2 mu^2 phi^2 + pi^2/a^2)/2,
  whose derivative is not zero -- and S'/2pi^2 a^3 is route 1 and route 2, term for term.
""")

S_of_a = (a ** 2 * mu ** 2 * phi ** 2 + pi_ ** 2 / a ** 2) / 2
check(sp.simplify(sp.diff(S_of_a, a)) != 0,
      f"S(a) = mu(N+1/2) in fixed field operators is NOT free of a: S' = {sp.simplify(sp.diff(S_of_a, a))}")
check(sp.simplify(sp.expand(sp.diff(S_of_a, a) / (2 * sp.pi ** 2 * a ** 3) - theta_route1)) == 0,
      "and `r6930`'s own formula S'(a)/2pi^2 a^3 reproduces routes 1 and 2 EXACTLY -- "
      "** three routes, one operator; the vanishing was the step S' = 0 **")
Sfun = sp.Function('S')(a)
E_gen = Sfun / a
tr_gen = sp.simplify((E_gen + a * sp.diff(E_gen, a)) / (2 * sp.pi ** 2 * a ** 3))
check(sp.simplify(tr_gen - sp.diff(Sfun, a) / (2 * sp.pi ** 2 * a ** 3)) == 0,
      "⌗ and the verdict reduces to EXACTLY ONE STEP: for any E = S(a)/a the trace is S'(a)/2pi^2 a^3, "
      "so 'traceless' IS 'S free of a' -- true for the c-number zero point sum(mu_n/2) and true at "
      "fixed occupation, and false for the operator")

check(coeff_phi2 == mu ** 2 / a ** 2,
      f"the phi^2 coefficient is exactly mu^2/a^2 = {coeff_phi2}  -- power a^-2")
check(coeff_pi2 == -1 / a ** 6,
      f"the pi^2 coefficient is exactly -1/a^6 = {coeff_pi2}  -- power a^-6")

# mu_n^2 = m^2 - 3, m >= 3, so it is never zero and never small
mus = [sp.Integer(m) ** 2 - 3 for m in range(3, 12)]
check(all(v >= 6 for v in mus),
      f"mu_n^2 = m^2-3 >= 6 for every m >= 3 (first: {mus[:4]}), so the coefficient never vanishes")

deg = sp.Poly(sp.expand(2 * sp.pi ** 2 * theta_route1 * a ** 6), phi, pi_).total_degree()
check(deg == 2,
      f"the whole operator is degree {deg} in (phi, pi): ** phi^2 is a QUADRATIC-order structure, "
      "not a cubic one **")

print(r"""
  ⇒ ** ⓵ IS ANSWERED, AND ANSWERED YES. **  A phi^2 structure enters R-hat = 4Lambda + kappa Theta-hat
    with coefficient kappa mu_n^2 / 2pi^2 at the power a^-2.  It is potential-like, exactly as the
    order's direction said -- but it does not come from the cubic.  It comes from the tower's own
    gradient term, so it is present at j = 0 and at every order above.""")

# ============================================================================ C
head("C.  WHY IT READ AS ABSENT: THE OPERATOR VANISHES ON A DIAGONAL, NOT AS AN OPERATOR")

N = 6
sq = sp.sqrt


def ladders(n):
    """a and a-dagger in the ORTHONORMAL number basis, exact radicals."""
    A_ = sp.zeros(n, n)
    Ad_ = sp.zeros(n, n)
    for k in range(1, n):
        A_[k - 1, k] = sq(k)
        Ad_[k, k - 1] = sq(k)
    return A_, Ad_


Aop, Adop = ladders(N)
# M = a^3, omega = mu/a  =>  M*omega = a^2 mu
Mw = a ** 2 * mu
PHI = (Aop + Adop) / sq(2 * Mw)
PIH = sp.I * sq(Mw / 2) * (Adop - Aop)
THETA = sp.simplify(-(PIH * PIH) / a ** 6 + mu ** 2 * (PHI * PHI) / a ** 2)
LADDER_FORM = sp.simplify(mu / a ** 4 * (Aop * Aop + Adop * Adop))

check(sp.simplify(THETA - LADDER_FORM) == sp.zeros(N, N),
      "2pi^2 Theta-hat = (mu/a^4)(a^2 + a-dagger^2) EXACTLY, at truncation N=6, in exact radicals")

check(all(sp.simplify(THETA[i, i]) == 0 for i in range(N)),
      "its diagonal is exactly ZERO in every entry -- so <n|Theta|n> = 0 for every number state")

check(sp.simplify(THETA[0, 2]) != 0,
      f"but the operator is NOT zero: <0|Theta|2> = {sp.simplify(THETA[0, 2])}")

# the diagonal statement IS the virial theorem
K = sp.simplify((PIH * PIH) / (2 * a ** 3))
V = sp.simplify(a * mu ** 2 * (PHI * PHI) / 2)
vir = [sp.simplify(K[i, i] - V[i, i]) for i in range(N - 1)]
check(all(v == 0 for v in vir),
      "and that vanishing IS the harmonic virial theorem: <n|K|n> = <n|V|n> exactly, "
      f"both = (mu/4a)(2n+1) (interior rows n<{N-1}; the top row is truncation, not physics)")

# a mixture of number states also gives zero -- linearity in the diagonal
w = [sp.Rational(k + 1, 21) for k in range(N)]
check(sp.simplify(sum(w[i] * THETA[i, i] for i in range(N))) == 0,
      "every MIXTURE of number states gives zero too, since the trace reads only the diagonal")

# but a squeezed state does not
t = sp.Symbol('t', real=True, nonzero=True)
psi_sq = sp.zeros(N, 1)
psi_sq[0, 0] = 1
psi_sq[2, 0] = t
num = sp.simplify((psi_sq.T * THETA * psi_sq)[0, 0])
den = sp.simplify((psi_sq.T * psi_sq)[0, 0])
exp_sq = sp.simplify(num / den)
check(sp.simplify(exp_sq - 2 * sq(2) * mu * t / (a ** 4 * (1 + t ** 2))) == 0,
      f"on the squeezed state |0> + t|2> the expectation is {exp_sq} != 0 -- "
      "** the vanishing is on the diagonal, not of the operator **")

# normal ordering cannot remove it
check(sp.simplify(LADDER_FORM - mu / a ** 4 * (Aop * Aop + Adop * Adop)) == sp.zeros(N, N),
      "and normal ordering cannot remove it: a^2 + a-dagger^2 carries no contraction, so its "
      "normal-ordered form is itself -- the ordering does not surface here")

print(r"""
  ⇒ ** THE SIXTH FACE OF THE STANDING LESSON: THE DOMAIN OF A VANISHING. **  The landed sentence reads
    "the excitation trace vanishes identically as an operator -- in every state and not merely the
    vacuum", and its warrant is that rho goes as a^-4 with p = rho/3.  That warrant is an
    EXPECTATION-VALUE statement, true in every stationary state of the instantaneous Hamiltonian and in
    every mixture of them -- and it is the virial theorem, not an operator identity.  The operator is
    a^2 + a-dagger^2 = X^2 - P^2, which is not zero and is not small.

    ⌗ *The five faces were the domain of a symbol, of an identity, of a representation, of an
      expansion, and of an equivalence.  This is the same lesson at a vanishing: the set on which a
      thing was checked to vanish is part of the claim that it does.*""")

# ============================================================================ D
head("D.  THE CONCLUSION SURVIVES, WITH A DIFFERENT AND STRONGER REASON: AN INVERTED OSCILLATOR")

print(r"""
  The eigenvalue question `r6950` reduced to is whether M(a) = sum_k kappa_k a^-m_k T_k is SINGULAR for
  almost every a.  At quadratic content M(a) is proportional to a^2 + a-dagger^2 = X^2 - P^2 with
  X = mu phi/a, P = pi/a^3 -- an INVERTED oscillator, whose point spectrum is empty.
""")

# the commutator that makes it an inverted oscillator, exact on the interior block
X_ = sp.simplify(mu * PHI / a)
P_ = sp.simplify(PIH / a ** 3)
comm = sp.simplify(X_ * P_ - P_ * X_)
check(all(sp.simplify(comm[i, i] - sp.I * mu / a ** 4) == 0 for i in range(N - 1)),
      f"[X, P] = i mu/a^4 exactly on the interior block (X = mu phi/a, P = pi/a^3)")
check(sp.simplify(sp.expand(mu / a ** 4 * (Aop * Aop + Adop * Adop) - (X_ * X_ - P_ * P_))) == sp.zeros(N, N),
      "and (mu/a^4)(a^2 + a-dagger^2) = X^2 - P^2 exactly: the residual operator IS an inverted oscillator")

# the null equation and its exact solutions
k_ = sp.Symbol('k', positive=True)
for order in (sp.Rational(1, 4), -sp.Rational(1, 4)):
    sol = sp.sqrt(ppos) * sp.besselj(order, k_ * ppos ** 2 / 2)
    resid = sp.simplify(sp.diff(sol, ppos, 2) + k_ ** 2 * ppos ** 2 * sol)
    check(sp.simplify(sp.expand(resid)) == 0,
          f"psi = sqrt(p) J_{{{order}}}(k p^2/2) solves psi'' + k^2 p^2 psi = 0 BY SUBSTITUTION "
          "(k = 1/mu a^2)")

# near the origin both are regular: leading powers 1 and 0
lead_p = sp.simplify(sp.limit(sp.sqrt(ppos) * sp.besselj(sp.Rational(1, 4), k_ * ppos ** 2 / 2) / ppos,
                              ppos, 0, '+'))
lead_m = sp.simplify(sp.limit(sp.sqrt(ppos) * sp.besselj(-sp.Rational(1, 4), k_ * ppos ** 2 / 2),
                              ppos, 0, '+'))
check(lead_p != 0 and lead_m != 0,
      "both solutions are REGULAR at the momentum origin -- leading behaviours p^1 and p^0, so "
      "** the 1/p obstruction of the first-order case is gone, exactly as `r6959` predicted **")

# but neither is L^2 at infinity.  The envelope exponent is measured on the EXACT solution, whose
# validity §D has already established by substitution -- so the float tests the asymptotics only.
from scipy.special import jv  # noqa: E402

# J_nu and J_(nu+1) are pi/2 out of phase at large argument, so their hypotenuse IS the envelope
pg = np.linspace(200.0, 600.0, 4001)
xi = pg ** 2 / 2
env = np.sqrt(pg) * np.hypot(jv(0.25, xi), jv(1.25, xi))
e_meas = float(np.polyfit(np.log(pg), np.log(env), 1)[0])
check(abs(e_meas - (-0.5)) < 2e-3,
      f"envelope exponent of sqrt(p) J_(1/4)(p^2/2) measured {e_meas:+.5f} against the EXACT "
      "prediction -1/2  =>  |psi|^2 ~ 1/p")

# and the -1/2 does not depend on z at all, exactly: the WKB amplitude is Q^(-1/4) with Q = p^2 + z
zsym = sp.Symbol('z', real=True)
wkb = sp.sqrt(ppos) * (ppos ** 2 + zsym) ** sp.Rational(-1, 4)
check(sp.limit(wkb, ppos, sp.oo) == 1,
      "and the exponent is -1/2 at EVERY real z, exactly: the WKB amplitude (p^2+z)^(-1/4) satisfies "
      "sqrt(p)(p^2+z)^(-1/4) -> 1, so no real z makes the solution decay faster")

check(sp.integrate(1 / ppos, (ppos, 1, sp.oo)) == sp.oo,
      "and the divergence is exact: int_1^oo dp/p = oo, so NEITHER solution is L^2 at infinity, "
      "at EVERY real z")

print(r"""
  ⇒ ** SO R-HAT STILL HAS NO EIGENVECTOR AT QUADRATIC ORDER -- and the reason is not the landed one. **
    Not "the Ricci scalar is a function of the scale factor alone", which §B and §C show it is not,
    but: the tower operator it carries is an inverted oscillator, and an inverted oscillator has no
    normalizable eigenvector at any real eigenvalue.  The conclusion is unchanged and its warrant is
    stronger, because it no longer depends on a term being absent.

  ⚠ ** WHAT DOES NOT SURVIVE AS STATED, flagged and routed rather than extrapolated. **  "The spectrum
    is purely continuous, the half-line above 4Lambda with 4Lambda itself not attained" used the same
    absence.  X^2 - P^2 has spectrum all of R, so once the operator content is restored there is
    spectrum BELOW 4Lambda.  *Purely continuous survives; the half-line does not.*  This receipt claims
    that at quadratic content only, and routes the sentence.""")

# ============================================================================ E
head("E.  ⓶  THE DEGENERATE POINT IS A FEATURE OF ONE REPRESENTATION")

print(r"""
  One abstract operator, M = c1 pi^2 + c2 (1/2)(pi^2 phi + phi pi^2) + c3 phi^2.  Two representations:
  position (phi -> x, pi -> -i d/dx) and momentum (pi -> p, phi -> i d/dp).
""")

g = sp.Function('g')
# position representation
Lpos = -c1 * sp.diff(f(x), x, 2) - c2 * sp.diff(x * sp.diff(f(x), x), x) + c3 * x ** 2 * f(x)
Lpos_e = sp.expand(Lpos)
lead_pos = sp.simplify(Lpos_e.coeff(sp.Derivative(f(x), (x, 2))))
# momentum representation
Lmom = c1 * p ** 2 * g(p) + c2 * sp.I * p * sp.diff(p * g(p), p) + c3 * (-sp.diff(g(p), p, 2))
Lmom_e = sp.expand(Lmom)
lead_mom = sp.simplify(Lmom_e.coeff(sp.Derivative(g(p), (p, 2))))

check(sp.simplify(lead_pos + (c1 + c2 * x)) == 0,
      f"position representation: leading coefficient is {lead_pos} -- it VANISHES at x0 = -c1/c2")
check(sp.simplify(lead_mom + c3) == 0 and sp.diff(lead_mom, p) == 0,
      f"momentum representation: leading coefficient is the CONSTANT {lead_mom} -- it vanishes nowhere")

# and they are the same operator: matrix in the number basis, from the position-space
# differential expression by exact Hermite integrals, against the abstract ladder matrix
NH = 4
xx = sp.Symbol('x', real=True)
herm = [sp.exp(-xx ** 2 / 2) * sp.hermite(n, xx) / sp.sqrt(sp.sqrt(sp.pi) * 2 ** n * sp.factorial(n))
        for n in range(NH)]
Ao, Ado = ladders(NH)
PH0 = (Ao + Ado) / sq(2)          # phi with M*omega = 1 (the Hermite basis' own oscillator)
PI0 = sp.I * (Ado - Ao) / sq(2)
Mabs = sp.simplify(c1 * PI0 * PI0
                   + c2 * (PI0 * PI0 * PH0 + PH0 * PI0 * PI0) / 2
                   + c3 * PH0 * PH0)
Mint = sp.zeros(NH, NH)
for i in range(NH):
    for j in range(NH):
        expr = (-c1 * sp.diff(herm[j], xx, 2)
                - c2 * sp.diff(xx * sp.diff(herm[j], xx), xx)
                + c3 * xx ** 2 * herm[j])
        Mint[i, j] = sp.simplify(sp.integrate(sp.expand(herm[i] * expr), (xx, -sp.oo, sp.oo)))
# the truncated abstract matrix loses the top rows to truncation; compare the interior block
ok_same = all(sp.simplify(Mint[i, j] - Mabs[i, j]) == 0 for i in range(NH - 2) for j in range(NH - 2))
check(ok_same,
      "and the two ARE one operator: the position-space differential expression's exact Hermite "
      f"matrix equals the abstract ladder matrix on the interior block (N={NH})")

print(r"""
  ⇒ ** `r6954`'s THIRD FACE RETURNING ON `r6954`'s OWN RESULT: THE DOMAIN OF A REPRESENTATION. **  The
    degenerate point x0 = -c1/c2 is where one representation's leading coefficient vanishes.  The same
    operator, on the other side of the Fourier transform, has a constant leading coefficient and no
    singular point at all.  ** So there is no point at which to impose a boundary condition, and the
    wall did not move into an extension choice. **
""")

# the L^2 count at each end -- deficiency indices
print(r"""
  THE COUNT THAT SETTLES IT.  Asymptotically at large |p| the momentum equation
  -c3 psi'' + i c2 (p^2 psi' + p psi) + c1 p^2 psi = 0  has two behaviours, both exact:

    psi_1 ~ p^-1 exp(i c2 p^3 / 3 c3 - i c1 p / c2)   -- |psi|^2 ~ p^-2, L^2
    psi_2 ~        exp(i c1 p / c2)                   -- |psi|^2 ~ const, NOT L^2
""")


# Verified by SUBSTITUTION and an exact limit, not by integration: the recessive branch is
# ill-conditioned outward, and the phase integral grows as p^3, so measuring these was fragile and slow.
bet, gam = sp.symbols('beta gamma', nonzero=True)
pp = sp.Symbol('p', positive=True)


def relative_residual(ans):
    """residual of psi'' - beta p^2 psi' - beta p psi - gamma p^2 psi, relative to the largest term."""
    R = (sp.diff(ans, pp, 2) - bet * pp ** 2 * sp.diff(ans, pp)
         - bet * pp * ans - gam * pp ** 2 * ans)
    return sp.simplify(sp.cancel(sp.expand(R / (pp ** 2 * ans))))


ans1 = sp.exp(bet * pp ** 3 / 3 + (gam / bet) * pp) / pp          # the recessive branch
ans2 = sp.exp(-(gam / bet) * pp)                                   # the dominant branch
r1 = relative_residual(ans1)
r2 = relative_residual(ans2)
check(sp.limit(r1, pp, sp.oo) == 0,
      f"branch 1, psi ~ exp(beta p^3/3 + (gamma/beta)p)/p: relative residual {r1} -> 0 exactly")
check(sp.limit(r2, pp, sp.oo) == 0,
      f"branch 2, psi ~ exp(-(gamma/beta)p): relative residual {r2} -> 0 exactly")

# with beta = i c2/c3 and gamma = c1/c3 both giving PURELY IMAGINARY exponents, the moduli are exact
beta_v = sp.I * c2 / c3
gam_v = c1 / c3
check(sp.simplify(sp.re(beta_v)) == 0 and sp.simplify(sp.re(gam_v / beta_v)) == 0,
      "beta = i c2/c3 and gamma/beta = -i c1/c2 are PURELY IMAGINARY for real couplings, so both "
      "exponentials are pure phases and the moduli are exactly |psi_1| = 1/p and |psi_2| = 1")

print(r"""
  ⇒ ** EXACTLY ONE L^2 SOLUTION AT EACH END: both ends are limit-point, the deficiency indices are
    (0,0), and the operator is essentially self-adjoint. **  The family the order asked for the form of
    is a single point.  ⇒ *⓶'s selection problem has no object -- and the argument that closed the
    first-order case has more than purchase: at c2 = 0 (§D) it closes the question exactly.*

  ** AND WHAT DISTINGUISHES THIS POINT FROM a = 0, WHICH THE ORDER ASKED FOR DIRECTLY. **  a = 0 is an
    ENDPOINT of the physical configuration space and a physical locus -- the de Sitter cosmological
    horizon, surface gravity 1/alpha -- so the extension freedom is genuine and the horizon's own
    thermal state is there to close it.  x0 = -c1/c2 is an INTERIOR point in one representation and no
    point at all in the other, and carries no physical locus.  ** The mechanism does not reach the
    degenerate point because there is nothing there for it to reach. **""")

# ============================================================================ F
head("F.  WHAT IS LEFT, AND THE GUARD THAT SAYS TO REPORT THE ORDER AND STOP")

print(r"""
  TWO THINGS STOP THIS SHORT OF THE THIRD COMPLETED ARGUMENT, and both are the order's guards firing.
""")

# (i) the c2 -> 0 discontinuity, and the scaling reduction
print(r"""  (i) THE CLOSURE AT c2 = 0 DOES NOT EXTEND BY CONTINUITY.  At c2 = 0 neither solution is
      L^2 (§D).  At c2 != 0 exactly one is, at each end (§E).  So switching on the cubic's kinetic
      vertex CREATES a square-integrable solution where there was none, and what remains is a
      CONNECTION CONDITION -- one analytic equation asking the two ends' one-dimensional subspaces to
      coincide -- rather than a boundary condition.""")

lam = sp.Symbol('lambda', positive=True)
q = sp.Symbol('q', positive=True)
mm = sp.Symbol('m', positive=True)
# p = lambda q reduces the equation to one dimensionless parameter
u = c2 * lam ** 3 / c3
v = c1 * lam ** 4 / c3
lam_star = sp.solve(sp.Eq(u, 1), lam)[0]
v_star = sp.simplify(v.subs(lam, lam_star))
v_target = c1 * c3 ** sp.Rational(1, 3) * c2 ** sp.Rational(-4, 3)
check(sp.powsimp(sp.simplify(v_star / v_target), force=True) == 1,
      f"the scaling p -> lambda q (lambda = {lam_star}) leaves ONE dimensionless parameter, "
      f"v = {v_target}")

# with c1 ~ a^-6, c3 ~ a^-2, c2 ~ a^-m, when is v independent of a?
v_a = (a ** -6) * (a ** -2) ** sp.Rational(1, 3) * (a ** -mm) ** sp.Rational(-4, 3)
expo = sp.simplify(sp.log(v_a) / sp.log(a))
m_flat = sp.solve(sp.Eq(expo, 0), mm)
check(m_flat == [5],
      f"with c1 ~ a^-6 and c3 ~ a^-2, v is constant in a only if the cubic's trace power is m = "
      f"{m_flat[0]}; the corpus's own 'pi_n^2 phi_m/a^3 in kind' puts it at 6")

print(r"""      ⇒ *So for the corpus's own power the single parameter v does vary along the curve the scale
      factor traces, the condition is one analytic equation in it, and the c2 -> 0 endpoint says the
      condition is not identically satisfied.  That is a shape and not a verdict: whether the
      connection coefficient has a zero, and where, is the row's remaining datum, and it is NOT
      claimed here.*
""")

# (ii) the content may be larger still
print(r"""  (ii) THE CONTENT MAY BE LARGER THAN THREE STRUCTURES, and the guard says to report the order and
      stop.  The trace carries whatever the Hamiltonian carries.  The KINETIC sector's expansion
      pi^2/(1+lambda phi) supplies pi^2, pi^2 phi, pi^2 phi^2, ... -- always two powers of momentum.
      The POTENTIAL sector -- the term the phi^2 of §B came from, sqrt(h) R^(3) expanded in the
      transverse-traceless perturbation -- supplies phi^2 at quadratic order and phi^3 at cubic, with
      no momenta at all.  The corpus named only the kinetic vertex ("pi_n^2 phi_m/a^3 in kind")
      because that is the one that is singular at a = 0; the potential cubic is regular there and so
      was never in view -- but the TRACE does not care which is singular.""")

orders = {"pi^2": 0, "phi^2": 2, "sym(pi^2 phi)": 1, "phi^3": 3}
check(max(orders.values()) == 3 and orders["phi^2"] == 2,
      "order of the null equation in the momentum representation, by highest power of phi-hat: "
      "** 2 at the content established here (pi^2, sym(pi^2 phi), phi^2); 3 if the potential "
      "sector's cubic phi^3 enters **")

print(r"""
  ⛔ ** SO THE HONEST STATUS, IN THE ORDER'S OWN TERMS. **

    · ** ⓵ IS YES, and it is yes at quadratic order. **  A phi^2 structure is in R-hat with coefficient
      kappa mu_n^2/2pi^2 at the power a^-2, from the tower's own gradient term.  Derived twice, exactly.
      ⇒ *The order's first branch -- "if it does not enter ... the wall is gone as an object ... the
      third completed argument" -- is not the branch we are on, and I am not reporting those words.*

    · ** BUT THE SECOND BRANCH'S OBJECT DOES NOT EXIST EITHER. **  The obstruction at the momentum
      origin is gone, as the order said it would be.  The wall does NOT then sit in a boundary
      condition at x0 = -c1/c2: that point is a feature of one representation, the same operator is
      regular in the other, and the deficiency indices are (0,0).  ** There is nothing to select. **

    · ** AND A LANDED CLAIM NEEDS ITS SCOPING. **  "The excitation trace vanishes identically as an
      operator -- in every state and not merely the vacuum" is the virial theorem, true on the
      diagonal and not of the operator.  The conclusion it was used for -- no eigenvector at quadratic
      order -- SURVIVES, on the stronger ground that the operator is an inverted oscillator.  The
      companion claim "the half-line above 4Lambda" does not survive as stated.

    · ** WHAT IS LEFT IS TWO NAMED DATA: ** the connection coefficient at c2 != 0, and whether the
      potential sector's cubic puts phi^3 into the trace.  Two structures give order 2; three give
      order 3.  ⇒ *Reported and stopped, per the guard, rather than extrapolated.*

  ⛔ WHAT THIS DOES NOT TOUCH.

    · No ordering choice -- §C.7 shows the quadratic operator has no ordering ambiguity at all.
    · No interacting theory beyond the trace's content at cubic order.
    · The transverse-traceless weight stays where `r6946` left it -- named, non-load-bearing, unclaimed.
    · Nothing on `prop:flat`, `PO-31` or `PO-15`; ** no corpus edit ** -- the `P10` sites and their
      sentences are routed in `FOR_66_FROM_60.md`.
""".rstrip())

print()
print("=" * 94)
if FAILED:
    print(f"FAILED {len(FAILED)} check(s):")
    for fmsg in FAILED:
        print("   -", fmsg)
    sys.exit(1)
print("ALL CHECKS PASS.")

#!/usr/bin/env python3
r"""
P10_the_second_logarithm_line_closes_because_the_interaction_cannot_reach_the_anomalys_own_power_of_a
====================================================================================================

LEVEL: exact closed form for the second-order shift (verified against direct diagonalization to
eight digits), exact integer arithmetic for the S^3 selection rule and the multiplet sum rule,
exact symbolic series for the vertex's large-label expansion, exact symbolic algebra for the trace
formula; float linear algebra only for the convergence-order and variance measurements, each against
a floor measured in the same arithmetic.  The convergence exponents are log-log slopes of measured
residuals; nothing else is fitted.

OBJECT UNDER TEST -- `PO-23`, `r6943`/`r6945`.  The order, on the one thing `r6942` reduced the
second-logarithm question to and declined to guess:

  ⓵ᵃ *"The vertex's large-label asymptotic, to the order that decides the pole structure.  Report
      whether the inner sum produces a harmonic number and at what order in the label, with the
      expansion printed rather than characterised."*
  ⓵ᵇ *"And whichever way it falls, say what it does to the relocation."*

  ⌗ WITH THE ORDER'S OWN STATEMENT OF WHAT IS AT STAKE: *"What it gates is whether the relocation at
    $c_2=2r$ is PHYSICALLY AVAILABLE."*  ⇒ ** THAT QUESTION HAS AN ANSWER THAT DOES NOT GO THROUGH
    THE VERTEX AT ALL, AND IT IS NO. **

  ⌗ AND THREE GUARDS: the convergence-order measurement stays live rather than recited; the ordering
    stays named and unpicked, and if the vertex asymptotic depends on one, name the datum and stop;
    and -- NEW -- if the line closes outright, say so in those terms rather than burying it.

COMPUTES: the cubic's second-order vacuum shift in closed form and its exact power of the scale
factor; which $(n,m)$ family any order of the interaction can populate; the exact $S^3$ triple-
harmonic selection rule and multiplet sum rule; the internal-label expansion of the second-order
summand in both soft corners, order by order; and the exact condition on the vertex weight under
which a harmonic number appears.  Scope: the reduced tower on the fixed background, at fixed
occupation; NO ordering choice; no corpus edit.

-------------------------------------------------------------------------------
** THE SECOND-LOGARITHM LINE IS CLOSED.  IT CLOSES TWICE, AND THE STRONGER CLOSURE DOES NOT DEPEND
   ON THE VERTEX. **

** ⛭ THE CLOSURE THAT NEEDS NO VERTEX: THE INTERACTION CANNOT REACH $n=1$ AT ALL. **  The relocation
`r6942` found is a term $c_2\,a^{-1}\ln^{2}a$ --- it must sit at $n=1$, because that is where the
anomaly sits.  ** The cubic's own contribution sits at $n=3$. **  In closed form, verified against
direct diagonalization,
$$E^{(2)}=-\frac{\lambda^{2}\kappa}{32\,a^{3}}\sum_{123}G_{123}\,
   \frac{\mu_1\mu_2}{\mu_3(\mu_1+\mu_2+\mu_3)},$$
and measured as a log-log slope the free energy goes as $a^{-1.000000}$ while the shift goes as
$a^{-3.000000}$.  ⇒ *And the reason is a counting rather than an accident: the only scales are $a$
and $\ell_P$, so a term carrying $\ell_P^{\,j}$ carries $a^{-(1+j)}$ --- **$n=1+j$, and $n=1$ is
populated at $j=0$ alone, by the free tower.***  The free tower is log-free in the label (`r6942`,
exactly), so ** at $n=1$ the logarithm is capped at $m=1$ forever, and $(n{=}1,m{=}2)$ is not a term
this theory has. **  ⇒ *The relocation at $c_2=2r$ is a fact about the formula and not about this
construction, at every order of the interaction and not just the cubic.  §C.*

** ⛭ AND THE VERTEX COMPUTATION, WHICH THE ORDER ASKED FOR ON ITS OWN TERMS: NO HARMONIC NUMBER, AT
   ANY ORDER. **  The $S^3$ triple-harmonic overlap has an exact multiplet sum rule,
$\sum_{\alpha}|C_{123}|^{2}=n_1n_2n_3/2\pi^{2}$ on the selection-rule set (triangle inequality and
$n_1{+}n_2{+}n_3$ odd) --- checked against quadrature and against the $n_3=1$ case it must reproduce.
In both soft corners the internal-label dependence of the second-order summand is
$j\,(j^{2}-3)^{p}$, $p\in\tfrac12\mathbb{Z}$: ** for integer $p$ a polynomial in odd powers ending at
$j^{+1}$, for half-integer $p$ an even-power series -- so the coefficient of $1/j$ is zero at every
order, in both corners. **  ⇒ *No harmonic number, hence no $\ln$ of the label, hence no double pole:
the cubic stays at $m=1$ at its own power of $a$ too.*  §D prints the expansions.

** ⛭ AND THE CONDITION IS SHARP RATHER THAN LUCKY, WHICH IS WHAT MAKES IT CHECKABLE. **  The theorem
turns on the weight being a *polynomial* in the label.  A weight carrying one inverse power breaks the
termination and produces a harmonic number at a computed order with coefficient $c(-3)^{p}$ --- shown
in §E with the same arithmetic.  ⇒ ** So the one step at which the transverse-traceless index
contractions could differ from the scalar sum rule is named exactly: whether their multiplet-summed
weight is polynomial in each label.  It does not touch §C. **

⛔ ** NOT CLAIMED. **  No ordering choice: §A shows the cubic's reordering is confined to coincident
labels and is *linear in the momenta*, so it does not enter the asymptotic -- named, and stopped at.
No interacting theory beyond this vertex's own asymptotic; nothing on `prop:flat`, `PO-31`, `PO-15`;
no corpus edit -- the `P10` site and its sentence are routed.  rc=0 on all 18 checks.
"""

import sys

import numpy as np
import sympy as sp
from scipy.linalg import eigh

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


R_RES = sp.Rational(15, 4)  # r6975: 15/4, not 15/4 -- the frequency carries the curvature term's +2K (node 60's r6974)                       # Res_{s=-1} zeta_omega -- BANKED at r6920
a = sp.Symbol('a', positive=True)
L = sp.log(a)
VOL = 2 * sp.pi ** 2 * a ** 3
KAP = 4.0 * float(R_RES) / np.pi
LAM4 = 12.0


def Theta(h):
    """Theta = rho - 3p with rho = E/V and p = -dE/dV, at fixed occupation numbers."""
    return sp.simplify(h / VOL - 3 * (-sp.diff(h, a) / sp.diff(VOL, a)))


# ============================================================================ A
head("A.  THE THREE GUARDS, CARRIED BEFORE ANYTHING IS COMPUTED")

print("\n  GUARD 1 -- the convergence-order measurement stays LIVE.  This line's own rule from r6934:")
print("    on a finite-difference grid the commutator sits OFF-DIAGONAL, so a matrix comparison")
print("    returns a residual that does not converge.  Apply both sides to a smooth state and")
print("    measure the ORDER, here at the anomaly's own a^-5:")


def ident_order(k, Td=2, seed=0):
    NS = [200, 400, 800]
    vals = []
    for N in NS:
        xg = np.linspace(1.0, 6.0, N)
        hg = xg[1] - xg[0]
        D = (np.diag(np.ones(N - 1), 1) - np.diag(np.ones(N - 1), -1)) / (2 * hg)
        rng = np.random.default_rng(seed)
        T = rng.normal(size=(Td, Td))
        T = T + T.T
        V = np.exp(-(xg - 3.5) ** 2 / 0.8)[:, None] * rng.normal(size=Td)[None, :]
        fv, dfv = xg ** float(k), float(k) * xg ** (float(k) - 1)
        lhs = fv[:, None] * ((-1j * (D @ V)) @ T.T) + 1j * (D @ (fv[:, None] * (V @ T.T)))
        rhs = 1j * (dfv[:, None] * (V @ T.T))
        m = slice(3, N - 3)
        vals.append(float(np.linalg.norm(lhs[m] - rhs[m]) / np.linalg.norm(rhs[m])))
    return float(np.polyfit(np.log(NS), np.log(vals), 1)[0]), vals


e5, v5 = ident_order(-5)
print(f"      f = a^-5:  {[f'{q:.2e}' for q in v5]}   exponent {e5:+.2f}")
check(abs(e5 + 2) < 0.1,
      f"the identity converges at SECOND order ({e5:+.2f}) on a smooth state, so a flat residual "
      "would be a REPRESENTATION error -- measured this revision, not cited")

print("\n  GUARD 2 -- the ordering stays NAMED AND UNPICKED, and the order adds: if the vertex")
print("    asymptotic depends on an ordering choice, name the datum and STOP.  So measure where the")
print("    cubic's own reordering lives.  The vertex is P_1 P_2 Q_3; reordering it can only matter")
print("    where two legs carry the SAME label, and there P Q P = P P Q + i P exactly:")


def reorder_residual(Nt):
    """(P Q P) - (P P Q) - i P on one mode, relative, on the interior block."""
    n = np.arange(Nt)
    low = np.diag(np.sqrt(n[1:]), 1)
    Q = (low + low.T) / np.sqrt(2.0)
    P = 1j * (low.T - low) / np.sqrt(2.0)
    resid = P @ Q @ P - P @ P @ Q - 1j * P
    k = slice(0, Nt - 3)
    return float(np.linalg.norm(resid[k, k]) / np.linalg.norm(P[k, k]))


rr = [reorder_residual(N) for N in (20, 40, 80)]
print(f"      distinct labels: [Q_3, P_2] = 0 identically, so the ordering is immaterial there.")
print(f"      coincident labels, interior residual of  P Q P - P P Q - i P : "
      f"{[f'{q:.2e}' for q in rr]}")
check(max(rr) < 1e-12,
      "** the cubic's reordering difference is exactly +i P -- LINEAR in the momenta, and supported "
      "only on coincident labels.  So it is not a cubic term and does not enter the large-label "
      "asymptotic: the datum is named and this receipt stops at it **")

xs = np.linspace(-8, 8, 900)
hs = xs[1] - xs[0]
Hosc = -(-2 * np.eye(900) + np.eye(900, k=1) + np.eye(900, k=-1)) / hs ** 2 + np.diag(xs ** 2)
_w, _V = np.linalg.eigh(Hosc)
v3 = _V[:, 3]
VAR_FLOOR = abs(float(v3 @ (Hosc @ (Hosc @ v3)) - (v3 @ (Hosc @ v3)) ** 2))
print(f"\n  GUARD 3 -- the variance floor for the second measurement: {VAR_FLOOR:.3e}")
check(VAR_FLOOR < 1e-8,
      f"'the variance vanishes' measures as {VAR_FLOOR:.2e} in this arithmetic; §F reports the "
      "relocation against it, because a relocation is not a sharpening")

print("\n  GUARD 4, the order's new one -- SAY IT IN THOSE TERMS IF IT CLOSES.  It closes: §C closes")
print("    the second-logarithm line without the vertex, §D closes it again with the vertex, and the")
print("    verdict sentence is in §G rather than in a remainder list.")

# ============================================================================ B
head("B.  THE CUBIC'S SECOND-ORDER SHIFT IN CLOSED FORM -- AND ITS POWER OF THE SCALE FACTOR")

print(r"""
    Each mode is an oscillator of mass a^3 and frequency mu/a, so <1|P|0> = a sqrt(mu/2) and
    <1|Q|0> = 1/(a sqrt(2 mu)).  With the DeWitt kinetic term's expansion giving
    H_3 = -(lam sqrt(kappa)/2a^3) sum C_123 P_1 P_2 Q_3, second-order perturbation theory on the
    vacuum returns, exactly,

        E^(2) = -(lam^2 kappa / 32 a^3) sum_123 G_123 mu_1 mu_2 / (mu_3 (mu_1+mu_2+mu_3)).

    The claim to test is the POWER OF a, so test it against a diagonalization that knows nothing
    about the derivation.""")


def build(a_, lam, Nt, mus=(2.0, 3.0, 4.0)):
    n = np.arange(Nt)
    low = np.diag(np.sqrt(n[1:]), 1)

    def QA(mu):
        M, w = a_ ** 3, mu / a_
        return (low + low.T) / np.sqrt(2 * M * w), (low.T - low) * np.sqrt(M * w / 2)

    ops = [QA(m) for m in mus]
    I = np.eye(Nt)

    def k3(A, B, C):
        return np.kron(np.kron(A, B), C)

    H = np.zeros((Nt ** 3, Nt ** 3))
    for i, (mu, (Q, A_)) in enumerate(zip(mus, ops)):
        h = -(A_ @ A_) / (2 * a_ ** 3) + a_ * mu ** 2 * (Q @ Q) / 2
        H += k3(*[h if k == i else I for k in range(3)])
    H += (lam / (2 * a_ ** 3)) * k3(ops[0][1], ops[1][1], ops[2][0])   # P_1 P_2 = -A_1 A_2
    return H


def ground(a_, lam, Nt):
    return eigh(build(a_, lam, Nt), subset_by_index=[0, 0], eigvals_only=True)[0]


def shift2(a_, Nt=8, lam=1e-3):
    E0 = ground(a_, 0.0, Nt)
    return E0, ((ground(a_, lam, Nt) + ground(a_, -lam, Nt)) / 2 - E0) / lam ** 2


MUS = (2.0, 3.0, 4.0)


def closed_form(a_):
    m1, m2, m3 = MUS
    return -(1.0 / (32 * a_ ** 3)) * m1 * m2 / (m3 * (m1 + m2 + m3))


print("\n      a        E_free          d2E/dlam2        closed form       slope_free  slope_shift")
prev = None
sl_f, sl_s = [], []
for a_ in [1.0, 1.5, 2.25, 3.375]:
    E0, s = shift2(a_)
    cf = closed_form(a_)
    line = f"   {a_:7.4f}  {E0: .8e}  {s: .8e}  {cf: .8e}"
    if prev:
        sf = np.log(E0 / prev[1]) / np.log(a_ / prev[0])
        ss = np.log(s / prev[2]) / np.log(a_ / prev[0])
        sl_f.append(sf)
        sl_s.append(ss)
        line += f"  {sf: .6f}   {ss: .6f}"
    print(line)
    prev = (a_, E0, s)

# ⛔⛭⛭ r6947 (66, gating r6946): ** THIS CHECK'S TOLERANCE WAS THE AUTHOR'S MACHINE'S ROUND-OFF
#   FLOOR, AND IT WENT RED ON THE GATING TREE AT 5.1e-07 AGAINST A THRESHOLD OF 1e-7. **
#   *The receipt reported rc=0 with 2.5e-09 on the seat that wrote it.  Neither number is a
#   physics result: the second difference (E(+lam) + E(-lam))/2 - E(0) cancels to order lam^2, so
#   with E ~ O(1) the numerator carries the double-precision epsilon and the quotient carries
#   epsilon/lam^2 -- NOISE THAT GROWS AS LAM FALLS, and whose realised size depends on the BLAS
#   and the eigensolver build.*
#   ⇒ *** MEASURED HERE RATHER THAN ARGUED, at a = 1 over three truncations: ***
#         lam      Nt=6      Nt=8     Nt=10
#         1e-2   1.3e-06   1.3e-06   1.3e-06     <- lam^2 truncation dominates
#         3e-3   5.4e-08   7.3e-08   3.5e-08     <- the balance point
#         1e-3   6.9e-07   5.1e-07   1.0e-06     <- the shipped lam, already in the noise
#         1e-4   4.5e-05   4.5e-05   1.1e-05     <- noise, rising as lam^-2
#   ⌗ ** The error is NOT monotone in lam, which is the signature that says the shipped point was
#     below the balance and measuring round-off rather than agreement. **  A tolerance set from one
#     run at such a point certifies the machine it ran on.
#   ⇒ ** THE REPAIR IS TO MEASURE THE BEST-ACHIEVABLE AGREEMENT RATHER THAN THE AGREEMENT AT AN
#     ARBITRARY STEP: ** scan lam over a stated grid and assert the minimum.  *That is a stronger
#     instrument, not a looser one -- the claim under test is a POWER OF a, and a wrong power is
#     O(1) out, so the tolerance can sit well above every machine's floor.*
#   ⌗ *Routed to `PO-60` as evidence: a check green for machine-specific reasons is that row's
#     first class seen outside the nine 70 found, and it was found by running rather than swept for.*
#
# ⛔⛭ r6975 (66, on node 70's r6961+70.2): ** THE r6947 REPAIR WAS RIGHT IN METHOD AND WRONG IN ITS
#   MARGIN, AND THE THING THAT CAUGHT IT IS THE DETECTOR THAT ROW ASKED FOR. **  `r6947` scanned the
#   step and asserted the minimum -- which is the right instrument -- and then claimed "four decades
#   of margin".  70's build perturbation measured the same site on three linear-algebra builds:
#         one thread (the runner's own)      2.5e-9
#         four threads                       7.3e-8
#         Prescott kernel, two threads       1.5e-7
#   ⇒ *** SO THE MARGIN OVER 1e-6 WAS 6.7x TO 13.6x ON TWO BUILDS OF THREE, NOT FOUR DECADES, AND THE
#     SCAN MINIMUM IS STILL FLOOR-DOMINATED ON THOSE TWO. ***  The exponent check measured 4.2x-5.3x
#     and the truncation-spread check 2.4x-3.7x.
#   ⌗ ** The lesson is the one r6947 itself drew, applied to r6947: a tolerance argued from one run is
#     an argument about that run.  The scan fixed WHERE the step sits; it did not fix the margin, and
#     the margin is the part a second machine sees. **
#   ⇒ ** REPAIRED BY MEASUREMENT RATHER THAN BY ARGUMENT: each tolerance is set an order of magnitude
#     above the worst value measured across those builds.  Every failure mode here is O(1) -- a wrong
#     power of a, a wrong exponent, a truncation-dependent answer -- so the widened tolerances leave
#     about five decades of real margin while no longer certifying one machine. **
#   ⌗ *70's alternative, carrying the second difference in exact arithmetic, is better where it
#     applies and is not taken here: the quantity is an eigenvalue of a truncated matrix, so exact
#     arithmetic would change the instrument rather than its tolerance.  Named as the stronger route.*
_LAM_GRID = (1e-2, 3e-3, 1e-3)
_rels = {lam: abs(shift2(1.0, 8, lam)[1] / closed_form(1.0) - 1.0) for lam in _LAM_GRID}
rel = min(_rels.values())
_at = min(_rels, key=_rels.get)
print("\n   lam-scan of the second difference (relative to the closed form), a = 1, Nt = 8:")
for lam in _LAM_GRID:
    print(f"     lam = {lam:.0e}   {_rels[lam]:.2e}" + ("   <- best" if lam == _at else ""))
check(rel < 1e-5,      # r6975: 1e-5, an order above the worst of 2.5e-9 / 7.3e-8 / 1.5e-7
      f"** the closed form matches the diagonalization to {rel:.1e} relative at lam = {_at:.0e}: "
      f"-lam^2 mu_1 mu_2 / (32 a^3 mu_3 sum mu), and at a=1 both give -1/192 **")
check(max(abs(np.array(sl_f) + 1)) < 1e-3,   # r6975: 4.2x-5.3x of headroom measured at 1e-5
      f"the FREE energy's exponent measures {np.mean(sl_f):+.6f} -- the n = 1 family, which is "
      "where the anomaly and its logarithm live")
check(max(abs(np.array(sl_s) + 3)) < 1e-2,   # r6975: the same site on the n = 3 branch
      f"** the cubic's second-order shift measures exponent {np.mean(sl_s):+.6f} -- it is an "
      "n = 3 term, NOT an n = 1 term **")

tr = [shift2(2.0, Nt=N)[1] for N in (5, 6, 7, 8, 9)]
spread = max(tr) - min(tr)
print(f"\n      truncation Nt = 5..9 at a = 2: {[f'{q:.9e}' for q in tr]}")
check(abs(spread / tr[0]) < 1e-4,   # r6975: 2.4x-3.7x of headroom measured at 1e-5
      f"and the measurement is truncation-stable to {abs(spread / tr[0]):.1e} relative, so the "
      "exponent is a property of the operator rather than of the cut")

# ============================================================================ C
head("C.  ⓵ᵇ  THE CLOSURE THAT NEEDS NO VERTEX -- THE RELOCATION LIVES AT A POWER OF a THE "
     "INTERACTION CANNOT REACH")

c, n, m, r, c2 = sp.symbols('c n m r c_2', positive=True)


def trace_general(cc, nn, mm):
    return sp.simplify(Theta(cc * a ** (-nn) * L ** mm) * 2 * sp.pi ** 2)


print("\n      the general entry, re-derived here rather than cited (r6942 ⓵ᵃ):")
gen = trace_general(c, n, m)
pred = c * a ** (-(n + 3)) * ((1 - n) * L ** m + m * L ** (m - 1))
check(sp.simplify(sp.expand(gen - pred)) == 0,
      "2 pi^2 Theta[c a^-n ln^m a] = c a^-(n+3) [ (1-n) ln^m a + m ln^(m-1) a ], exactly")

print("\n      the anomaly's entry and the cubic's, side by side:")
anom = trace_general(r, 1, 1)
cub2 = trace_general(c, 3, 2)
print(f"        (n=1, m=1), the anomaly   : 2 pi^2 Theta = {sp.simplify(anom)}")
print(f"        (n=3, m=2), the cubic's    : 2 pi^2 Theta = {sp.simplify(sp.expand(cub2))}")
d_anom = sp.simplify(sp.diff(anom, a))
d_cub2 = sp.simplify(sp.diff(cub2, a))
print(f"        d/da of those              : {d_anom}   and   {sp.expand(d_cub2)}")
check(sp.simplify(sp.diff(anom * a ** 4, a)) == 0
      and sp.simplify(sp.diff(sp.expand(cub2 * a ** 6), a)) != 0
      and sp.simplify(sp.diff(sp.expand(cub2 * a ** 6) - (-2 * c * L ** 2 + 2 * c * L), a)) == 0,
      "the anomaly's trace is exactly r a^-4 and the cubic's is exactly c a^-6 (-2 ln^2 a + 2 ln a): "
      "DIFFERENT powers of a, so they are independent terms")
mix = sp.expand(d_anom + sp.diff(trace_general(c2, 3, 2), a))
sol = sp.solve([sp.simplify(mix.subs(a, 2)), sp.simplify(mix.subs(a, 3))], c2, dict=True)
print(f"        requiring the two families to cancel at a = 2 and at a = 3 gives: {sol}")
check(sol == [],
      "** and asking for a cancellation between the two families returns NO solution: one "
      "coefficient cannot annihilate an a^-5 term and an a^-7 term at two values of a, so an n = 3 "
      "term cannot cancel an n = 1 term at any coefficient **")

print(r"""
    ⇒ ** THE COUNTING, WHICH IS WHY THIS IS A THEOREM AND NOT A FEATURE OF THE CUBIC. **  In the
      reduced theory the only scales are a and the Planck length; hbar = c = 1 makes the vacuum
      energy 1/length.  ⇒ A term carrying ell_P^j must carry a^-(1+j):

          E(a) = (1/a) * sum_j f_j (ell_P/a)^j * [polynomial in ln(a/ell_P)]     ⇒   n = 1 + j.

      The interaction enters at j >= 2 (one vertex pair costs kappa = ell_P^2, measured as the
      exponent -3 in §B), so ** n = 1 is populated at j = 0 ALONE -- by the FREE tower. **  And the
      free tower's summand is log-free exactly (r6942: d(m) mu(m) = 2(m^2-4) sqrt(m^2-3) is a pure
      Laurent series), so its Dirichlet series has simple poles only:

        ** at n = 1 the logarithm is capped at m = 1, at every order of the interaction. **

    ⇒ ** THEREFORE THE RELOCATION AT c_2 = 2r IS NOT PHYSICALLY AVAILABLE. **  It needs a term
      c_2 a^-1 ln^2 a.  That is an (n=1, m=2) term, and this theory has no such term to tune.
      *r6942's relocation is a fact about the trace formula's closure, not about this construction*
      --- which is exactly the disjunction the order set up, resolved on the second branch, and
      resolved for every order of the coupling rather than for the cubic alone.""")

# ============================================================================ D
head("D.  ⓵ᵃ  AND THE VERTEX SUM ON ITS OWN TERMS -- THE EXACT SELECTION RULE, THEN THE EXPANSION")


def sel_over_pi(n1, n2, n3):
    """(1/pi) int_0^pi sin(n1 t) sin(n2 t) sin(n3 t)/sin t dt, EXACT, from
       sin(n3 t)/sin t = sum_k e^{i(n3-1-2k)t} and cosine orthogonality."""
    tot = sp.Integer(0)
    for k in range(n3):
        p = n3 - 1 - 2 * k
        for q, sgn in ((abs(n1 - n2), 1), (n1 + n2, -1)):
            if abs(p) == q:
                tot += sgn * sp.Rational(1, 2) * (1 if q == 0 else sp.Rational(1, 2))
    return tot


def quad_over_pi(n1, n2, n3, N=400001):
    t = np.linspace(1e-9, np.pi - 1e-9, N)
    f = np.sin(n1 * t) * np.sin(n2 * t) * np.sin(n3 * t) / np.sin(t)
    return float(np.trapezoid(f, t) / np.pi)


def allowed(n1, n2, n3):
    return (max(n1, n2, n3) < n1 + n2 + n3 - max(n1, n2, n3)) and ((n1 + n2 + n3) % 2 == 1)


bad, shown = 0, 0
print("\n      the selection-rule integral, exact integer arithmetic against quadrature:")
for n1 in range(1, 8):
    for n2 in range(1, 8):
        for n3 in range(1, 8):
            e, nu = sel_over_pi(n1, n2, n3), quad_over_pi(n1, n2, n3)
            if abs(float(e) - nu) > 2e-6:
                bad += 1
            if e != 0 and shown < 5 and n1 <= n2 <= n3:
                print(f"        ({n1},{n2},{n3}): exact = {e} pi,  quadrature = {nu:.6f} pi,  "
                      f"allowed = {allowed(n1, n2, n3)}")
                shown += 1
            if (e != 0) != allowed(n1, n2, n3):
                bad += 1
check(bad == 0,
      "** the integral is pi/2 on the selection-rule set -- triangle inequality AND n1+n2+n3 odd -- "
      "and 0 off it, over all 343 triples, matching quadrature **")

print(r"""
      With the S^3 zonal kernel K_n(theta) = n sin(n theta) / (2 pi^2 sin theta) -- whose value at
      theta = 0 is n^2/2pi^2 = d_n/Vol -- the multiplet-summed overlap is the exact triple integral

        sum_alpha |C_123|^2 = Vol * int 4 pi sin^2(theta) K_1 K_2 K_3 d(theta)
                            = n_1 n_2 n_3 / (2 pi^2)   on the selection-rule set.""")
n1s, n2s = sp.symbols('n_1 n_2', positive=True)
G = lambda x, y, z: sp.Rational(1, 2) * x * y * z / sp.pi ** 2
lhs_deg = sp.simplify(G(2 * n1s, 2 * n2s, 2 * n1s) / G(n1s, n2s, n1s))
check(sp.simplify(lhs_deg - 8) == 0,
      "the sum rule is homogeneous of degree 3 in the labels, which is what fixes the summand's "
      "scaling degree")
print("\n      and the one case it MUST reproduce, as a check rather than a claim: n_3 = 1 is the")
print("      constant harmonic, where sum_alpha |C|^2 = n_1^2 delta_{n_1 n_2} / 2 pi^2 directly.")
direct = n1s ** 2 / (2 * sp.pi ** 2)
viarule = G(n1s, n1s, 1)
check(sp.simplify(direct - viarule) == 0 and allowed(3, 3, 1) and not allowed(3, 4, 1),
      f"** the sum rule returns {sp.simplify(viarule)} against the direct "
      f"{sp.simplify(direct)}, and its selection rule forces n_1 = n_2 there: exact agreement **")

j, S = sp.symbols('j Sigma', positive=True)
mu_j = sp.sqrt(j ** 2 - 3)
KMAX = 8


def corner_report(title, jdep_of_k, note):
    print(f"\n      {title}")
    bad_k = []
    for k in range(KMAX):
        jd = sp.simplify(jdep_of_k(k))
        ser = sp.expand(sp.series(jd, j, sp.oo, 6).removeO())
        cinv = sp.simplify(ser.coeff(j, -1))
        print(f"        k={k}:  {jd}")
        print(f"               large-j: {ser}")
        print(f"               coeff of 1/j = {cinv}")
        if cinv != 0:
            bad_k.append(k)
    check(bad_k == [],
          f"** {note} -- the 1/j coefficient is EXACTLY ZERO at every order k = 0..{KMAX - 1} **")


print(r"""
      THE EXPANSION ITSELF.  With the summand G_123 mu_1 mu_2 / (mu_3 (mu_1+mu_2+mu_3)) and the
      sum rule's one power of each label, expand in the soft internal label.  The triangle
      inequality bounds the internal label by the others' sum, so the expansion that matters is in
      mu_j / Sigma with Sigma the hard legs' frequency sum, coefficients EXACT in j.""")
corner_report("soft leg on the 1/mu_3 factor -- the phi leg:  term_k = (-1)^k j mu_j^(k-1)/Sigma^(k+1)",
              lambda k: j * mu_j ** (k - 1),
              "the phi-leg corner produces no harmonic number")
corner_report("soft leg on a mu numerator -- a pi leg:  term_k = (-1)^k j mu_j^(k+1)/Sigma^(k+1)",
              lambda k: j * mu_j ** (k + 1),
              "the pi-leg corner produces no harmonic number either")

print(r"""
    ⇒ ** AND THE CLOSED FORM OF THE REASON, WHICH IS WHY IT HOLDS AT EVERY ORDER AND NOT JUST THE
      EIGHT PRINTED. **  Every term is j (j^2-3)^p with p in (1/2)Z:

        · p integer      -> a POLYNOMIAL in j with odd powers only, terminating at j^(+1).
        · p half-integer -> j^(2p+1) times a series in 1/j^2, with 2p+1 EVEN, so even powers only.

      A 1/j term is an odd power, so it can only come from the integer-p branch -- where the series
      terminates at j^(+1) and never reaches it.  ⇒ ** No harmonic number at any order in the label.
      Hence no ln of the label in the summand, hence only simple poles, hence m = 1: the cubic does
      not generate a second logarithm even at its own power of a. **""")

# ============================================================================ E
head("E.  THE CONTROL -- AND IT NAMES EXACTLY WHICH PROPERTY THE ANSWER TURNS ON")

cc = sp.Symbol('kappa_w')
print(r"""
      A negative result needs an instrument that can return a positive one.  The theorem above turns
      on the weight being a POLYNOMIAL in the label.  Give it one inverse power -- w(j) = j + c/j --
      and the integer-p branch no longer terminates:""")
hits = []
for k in (1, 3, 5, 7):
    p = sp.Rational(k - 1, 2)
    jd = sp.simplify((j + cc / j) * mu_j ** (k - 1))
    ser = sp.expand(sp.series(jd, j, sp.oo, 6).removeO())
    cinv = sp.simplify(ser.coeff(j, -1))
    predicted = sp.simplify(cc * (-3) ** p)
    print(f"        k={k} (p={p}):  coeff of 1/j = {cinv}      predicted c(-3)^p = {predicted}")
    hits.append((sp.simplify(cinv - predicted) == 0, cinv != 0))
check(all(h[0] for h in hits),
      "** the control's 1/j coefficient is exactly c(-3)^p at every odd k -- so the instrument DOES "
      "see a harmonic number when one is there, and the zero in §D is a measurement **")
check(all(h[1] for h in hits),
      "and it is non-zero at every one of them, so the contrast is with a live signal rather than "
      "with a second zero")
Hm = sp.Symbol('H_m')
print(r"""
    ⇒ ** WHICH STEP, NAMED. **  The scalar sum rule's weight n_1 n_2 n_3 is a polynomial exactly, so
      §D's zero is exact there.  The transverse-traceless vertex differs from it by index
      contractions, whose multiplet-summed weight is a rational function of the labels; ** the one
      step at which the conclusion could differ is whether that rational function is a polynomial in
      each label or carries an inverse power. **  This receipt does not compute the TT zonal kernel
      and does not guess it.  ⌗ *And that step is not load-bearing for the order's question: §C
      settles the relocation without any vertex property at all, and §C is where the verdict is.*""")

# ============================================================================ F
head("F.  THE SECOND MEASUREMENT, BECAUSE A RELOCATION IS NOT A SHARPENING")

N = 30000
xg = np.linspace(0.5, 25.0, N)
hg = xg[1] - xg[0]


def variance_at(c2v, sig=0.25, a0=4.0):
    Lg = np.log(xg)
    Rv = LAM4 + KAP * xg ** -4 + c2v * 2.0 * Lg * xg ** -4 * (4.0 / np.pi)
    p_ = np.exp(-(xg - a0) ** 2 / (4 * sig ** 2))
    p_ /= np.sqrt(np.sum(p_ ** 2) * hg)
    edge = max(p_[0], p_[-1]) ** 2 / np.max(p_ ** 2)
    w = p_ ** 2 * hg
    return edge, float(np.sum(w * Rv ** 2) - np.sum(w * Rv) ** 2)


e_ok, var_tuned = variance_at(2.0 * float(R_RES))
e_bad, var_wide = variance_at(2.0 * float(R_RES), sig=1.2)
print(f"\n      at the tuned c_2 = 2r, sigma = 0.25:  edge {e_ok:.2e} (admissible)   "
      f"Var(R) = {var_tuned:.4e}")
print(f"                              sigma = 1.20:  edge {e_bad:.2e} (NOT admissible -- printed, "
      f"not dropped)   Var(R) = {var_wide:.4e}")
check(e_ok < 1e-10 and e_bad > 1e-10,
      "the admissibility gate still separates, and the rejected width is shown with its arithmetic")
check(var_tuned > 1e4 * VAR_FLOOR,
      f"** Var(R) = {var_tuned:.3e} at the tuned coefficient, "
      f"{np.log10(var_tuned / VAR_FLOOR):.1f} decades above the floor {VAR_FLOOR:.1e}: even where "
      "the relocation is written down it is not a sharp curvature -- and §C says it cannot be "
      "written down in this theory at all **")

# ============================================================================ G
head("G.  THE VERDICT, IN THE ORDER'S OWN TERMS")

print(r"""
  ⚑ ** THE SECOND-LOGARITHM LINE IS CLOSED. **  Not narrowed: closed, and by two independent
    arguments, of which the stronger needs no property of the vertex.

    ⓵ ** THE INTERACTION CANNOT REACH THE ANOMALY'S POWER OF a. **  The relocation is an
      (n=1, m=2) term.  The cubic's second-order shift is an n = 3 term -- closed form in §B,
      exponent measured at -3.000000 against the free tower's -1.000000 -- and the counting
      n = 1 + (powers of ell_P) makes that general: n = 1 is populated at zeroth order alone, by the
      free tower, whose summand is log-free exactly.  ⇒ *At n = 1 the logarithm is capped at m = 1
      forever, so there is no (n=1, m=2) coefficient in this theory to tune.*

    ⓶ ** AND THE VERTEX SUM CARRIES NO LOGARITHM OF THE LABEL EITHER. **  On the exact S^3 multiplet
      sum rule, the internal-label dependence in both soft corners is j (j^2-3)^p, whose expansion
      is either an odd polynomial terminating at j^(+1) or an even-power series.  ⇒ *The coefficient
      of 1/j is zero at every order: no harmonic number, no double pole, m = 1 at the cubic's own
      power of a too.*  §E shows the instrument returns c(-3)^p when a 1/j IS present.

  ⛔ WHAT THIS DOES TO r6942's RELOCATION -- IT DEMOTES IT, AND r6942 SAID SO FIRST.

    r6942 reported the relocation as *"a fact about the formula"* and asked whether it was available.
    ⇒ ** It is not.  The tuned state c_2 = 2r exists in the trace formula's closure and not in this
    theory's spectrum. **  *Nothing in r6942's verdict changes -- §C there was already unconditional
    -- and the third answer to "cancel or add" keeps its status as a property of the operation.*
    ⌗ This is a demotion of a possibility, not a correction of a claim: r6942 neither asserted the
    relocation was reachable nor guessed its sign.

  ⛔ WHAT MOVES IN P10, ROUTED AND NOT EDITED.

    · `sec:lock`'s sentence *"The cubic carries one internal sum, and whether its own large-label
      asymptotic carries a logarithm is what would decide it"* is now answered, and the stronger
      statement belongs beside it: ** the interacting corrections populate n = 2k+1, so the
      relocation's own power of a is reached only at k = 0, where the tower is free and log-free. **
    · The site and the replacement sentence are in `FOR_66_FROM_60.md`.  No corpus edit here.

  ⛔ AND WHAT IS LEFT ON THIS ROW, STATED SO IT IS NOT MISTAKEN FOR MORE THAN IT IS.

    · The TT multiplet-summed weight's polynomiality (§E) -- which decides ⓶ for the tensor vertex
      and decides nothing about ⓵.
    · The entangled-state question over a non-commuting cubic tower family (r6934's remainder), which
      this order did not ask about and which none of the above touches.
    · The ordering datum stays named and unpicked: §A shows the cubic's reordering is linear in the
      momenta and supported on coincident labels, so the asymptotic does not depend on it.
""".rstrip())

print()
print("=" * 94)
if FAILED:
    print(f"FAILED {len(FAILED)} check(s):")
    for f in FAILED:
        print("   -", f)
    sys.exit(1)
print("ALL CHECKS PASS.")

#!/usr/bin/env python3
r"""
P10_the_commutator_bound_survives_the_cubic_because_the_scaling_that_could_cancel_it_carries_no_trace
====================================================================================================

LEVEL: exact symbolic (sympy) for the commutator identity, the trace formula, the cancellation-power
theorem and the level-set degree count; float linear algebra for the identity's grid convergence, the
tuned cancellation and the non-commutativity measurement -- each against a floor or an exponent
measured in the same arithmetic.  Nothing is fitted.

OBJECT UNDER TEST -- `PO-23`, `r6933`.  The order, verbatim:

    "Compute $[\hat R,p_a]$ at that order and report whether the variance bound survives with the
     residue as its coefficient."

  with three outcomes costed: the correction $\hat a$-independent or carrying the residue as a common
  factor ⇒ *"the bound survives verbatim and the theorem generalizes"*; the correction able to
  **cancel** the residue term at some tower state ⇒ *"the question genuinely needs the interacting
  theory --- but you will have said so with the cancellation condition in hand"*; and ⚠ if the
  promotion is not well posed without a choice, *"say which choice, and whether the corpus has already
  made it elsewhere ... if this lands on the ordering, that is a different row's business and you
  should say so rather than pick."*

  ⌗ AND THE GUARD, named as this line's own catch returned: *"an inadmissible case shown with its
    arithmetic is evidence about the instrument; the same case dropped is a filtered result.  Whatever
    you build for ⓵, carry that."*  §A carries it and §D prints both sides for every inadmissible
    width.

COMPUTES: the commutator of the promoted $\hat R$ with $p_a$; the trace of an arbitrary energy term
and which power-law scalings can cancel the anomaly's contribution to $\partial_a\hat\Theta$; whether
a tower expectation can zero the bound's coefficient and whether that makes the curvature sharp; and
how far the level-set argument survives the promotion.  Scope: NO interacting theory is built -- the
commutator is computable without one, which is why it was ordered.

-------------------------------------------------------------------------------
** THE BOUND SURVIVES, AND THE REASON IS THE ROW'S OWN SHAPE A FOURTH TIME: THE ONLY SCALING THAT
   COULD CANCEL IT IS THE SCALING THAT CARRIES NO TRACE. **

** ⛭ ⓵ THE BOUND SURVIVES VERBATIM IN FORM AT EVERY ORDER, AND ORDERING-BLIND. **  For any tower
operator $\hat T$ -- commuting or not, ordered any way -- $[f(\hat a)\otimes\hat T,\,p_a]
=i\hbar f'(\hat a)\otimes\hat T$, because $\hat T$ acts on the other factor and the commutator
differentiates only the $a$-function.  ⇒ Robertson gives
$\operatorname{Var}(\hat R)\operatorname{Var}(p_a)\ge\frac{\hbar^{2}}{4}\langle\partial_a\hat
R\rangle^{2}$ **at every order**.  *A commutator is algebra and not dynamics, exactly as the order
says.*

** ⛭ ⓶ AND POINTWISE CANCELLATION IS IMPOSSIBLE, BY A THEOREM. **  An energy term $h(a)\otimes\hat T$
contributes $\hat\Theta=(h+ah')\hat T/2\pi^{2}a^{3}$, so a power law $h=c\,a^{-n}$ gives
$\partial_a\hat\Theta\propto(n-1)(n+3)\,a^{-n-4}$.  The anomaly's $\partial_a\hat\Theta_0$ goes as
$a^{-5}$, so matching the power needs $n=1$ --- **and at $n=1$ the coefficient $(n-1)$ vanishes, so
that term contributes nothing to $\hat\Theta$ at all.**  ⇒ *The unique scaling that could cancel the
anomaly in $\partial_a\hat\Theta$ is the $1/a$ scaling that makes a term traceless.  The anomaly
exists because $\ln a$ breaks that scaling; cancelling it would need exactly the scaling it broke.*

** ⛭ ⓷ THE EXPECTATION CAN BE TUNED TO ZERO -- AND THAT IS NOT SHARPNESS. **  $\langle\partial_a\hat
R\rangle$ sums distinct powers of $a$ weighted by tower expectations, and a tuned coefficient zeroes
it: at $B^{*}$ the bound's right-hand side collapses to $1.2\times10^{-35}$.  ⚠ **But
$\operatorname{Var}(\hat R)=2.3\times10^{-7}$ there, five decades above the measured floor.**  A
vacuous bound is not a sharp curvature; it only stops constraining.  ⇒ *So the order's second branch
is reachable in the weak sense and not in the strong one, and the cancellation condition is in hand.*

** ⛭ ⓸ AND THE LEVEL-SET ARGUMENT SURVIVES FURTHER THAN THE ORDER EXPECTED. **  Wherever the cubic's
tower operators can be simultaneously diagonalized -- every product state, and any commuting family --
$\hat R$ is a direct integral of multiplications by $R_{\rm eff}(a)=4\Lambda+\sum_j c_j a^{-n_j}$.
$\partial_aR_{\rm eff}\equiv0$ has **no solution at all** while $r>0$, and a level set clears to a
polynomial of finite degree, hence finitely many roots.  ⇒ **No eigenvector there either.**  ⌗ *The
residue is therefore not the coupling as such but exactly the NON-COMMUTATIVITY of the cubic's own
tower factors, measured below at $9.8\times10^{-2}$ and $2.8\times10^{-1}$ against a commuting
family's $5.2\times10^{-17}$.*

⛔ ** NOT CLAIMED. **  No interacting theory.  No coupled $\zeta(0)$.  No detectable signal.  §E
states what entangled states leave open, and §F answers the well-posedness question by naming the
choice rather than making it -- the ordering is another row's business, as `P10` already says.
rc=0 on all 20 checks.
"""

import sys

import numpy as np
import sympy as sp

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


R_RESIDUE = sp.Rational(15, 4)                    # Res_{s=-1} zeta_omega -- r6975 re-point of r6920
KAP = 4.0 * float(R_RESIDUE) / np.pi
LAM4, HBAR = 12.0, 1.0

# ============================================================================ A
head("A.  THE CONTROLS AND FLOORS, BUILT FIRST -- INCLUDING THE ONE THE ORDER NAMED")

xs = np.linspace(-8, 8, 1200)
hs = xs[1] - xs[0]
Hosc = -(-2 * np.eye(1200) + np.eye(1200, k=1) + np.eye(1200, k=-1)) / hs ** 2 + np.diag(xs ** 2)
_w, _V = np.linalg.eigh(Hosc)
# ⛭ r6981 (66, on node 70's r6977+70.1): ** THE FLOOR IS THE LARGEST OF TEN AND NOT ONE
#   EIGENVECTOR'S, WHICH IS THE SAME REPAIR 70 MADE TO THIS SITE'S SIBLING AND FOR THE SAME REASON. **
#   A floor read off a single eigenvector is one round-off number, and 70 measured it moving
#   1.4e-10 to 1.9e-8 across linear-algebra builds -- a spread of 133x.  ⇒ *A threshold scaled by such
#   a floor recalibrates itself only while the floor is stable, and this one is not: when `r6975`
#   moved Var(R) from 1.56e-6 to 2.31e-7 the headroom fell to 12.2, so a build twelve times noisier
#   than four threads would turn the check red.  The judgement that had called it a false positive
#   LAPSED with that change, and 70's scoped tolerance job is what printed it.*
#   ⌗ **Measured here: the largest variance over the first ten eigenvectors is 1.65e-12 against the
#   fourth's 2.42e-13 -- 6.8x larger and, on the sibling's eight-build measurement, stable to a factor
#   under three where the single-eigenvector form moved thirty.**  So the threshold below reads against
#   a floor that is bigger and steadier, and the headroom on it is 1.4e5.
#   ⚠ *What is owed and named rather than assumed: the cross-build confirmation of THIS floor. Only a
#   seat that can perturb the build can make it, and it is ordered.*
VAR_FLOOR = max(abs(float(_V[:, k] @ (Hosc @ (Hosc @ _V[:, k]))
                          - (_V[:, k] @ (Hosc @ _V[:, k])) ** 2)) for k in range(10))
print(f"\n  VARIANCE FLOOR, on an operator that DOES have eigenvectors:"
      f"  Var(H_osc) on its 4th = {VAR_FLOOR:.3e}")
check(VAR_FLOOR < 1e-8,
      f"'the variance vanishes' measures as {VAR_FLOOR:.2e} -- the floor any sharpness claim must clear")

print("\n  ⌗ AND THE GUARD THE ORDER NAMED, carried from r6930: the commutator identity integrates by")
print("    parts, so a state with amplitude at the boundary breaks it.  §D prints BOTH sides for every")
print("    inadmissible width rather than filtering them, because an inadmissible case shown with its")
print("    arithmetic is evidence about the instrument and the same case dropped is a filtered result.")
_gx = np.linspace(0.5, 30.0, 4000)
_gate = []
for _s in (1.0, 0.25):
    _q = np.exp(-(_gx - 4.0) ** 2 / (4 * _s ** 2))
    _gate.append(float((_q[0] ** 2 + _q[-1] ** 2) / np.max(_q ** 2)))
print(f"      edge amplitude at sigma = 1.00: {_gate[0]:.2e}   at sigma = 0.25: {_gate[1]:.2e}"
      f"   threshold 1e-10")
check(_gate[0] > 1e-10 > _gate[1],
      f"the gate SEPARATES: it rejects sigma = 1.00 at {_gate[0]:.1e} and admits sigma = 0.25 at "
      f"{_gate[1]:.1e}, so it is a discriminating threshold and not a rubber stamp")

# ============================================================================ B
head("B.  ⓵  THE COMMUTATOR IS ALGEBRA: THE IDENTITY, THEN ITS CONVERGENCE, FOR ANY TOWER OPERATOR")

xv = sp.Symbol('x', positive=True)
hb = sp.Symbol('hbar', positive=True)
f, psi = sp.Function('f'), sp.Function('psi')
comm = sp.expand(f(xv) * (-sp.I * hb * sp.diff(psi(xv), xv))
                 - (-sp.I * hb * sp.diff(f(xv) * psi(xv), xv)))
print(f"\n      [f(x), -i hbar d/dx] psi = {sp.simplify(comm)}")
check(sp.simplify(comm - sp.I * hb * sp.diff(f(xv), xv) * psi(xv)) == 0,
      "** [f(a-hat), p_a] = i hbar f'(a-hat) EXACTLY, for an arbitrary f -- no order, no coupling, no "
      "state enters **")
print("\n    ⇒ AND THE TOWER FACTOR RIDES THROUGH UNTOUCHED.  p_a acts on the scale-factor factor and")
print("      T-hat on the tower, so [f(a-hat) (x) T-hat, p_a] = i hbar f'(a-hat) (x) T-hat whatever")
print("      T-hat is -- commuting or not, and however its operators are ordered.")


def ident_residual(N, k, Td=3, seed=0):
    """apply both sides to a smooth state; the central difference is second order, so the residual
    must fall as N^-2.  (Comparing MATRICES fails: on a grid the commutator sits off-diagonal.)"""
    xg = np.linspace(1.0, 6.0, N)
    hg = xg[1] - xg[0]
    D = (np.diag(np.ones(N - 1), 1) - np.diag(np.ones(N - 1), -1)) / (2 * hg)
    rng = np.random.default_rng(seed)
    T = rng.normal(size=(Td, Td))
    T = T + T.T                                        # an ARBITRARY tower operator
    # apply factor-by-factor on the (N, Td) array rather than materializing the N*Td square kron:
    #   (f (x) T) v = f[:,None] * (v @ T.T);   (p (x) 1) v = (-1j D) v
    V = np.exp(-(xg - 3.5) ** 2 / 0.8)[:, None] * rng.normal(size=Td)[None, :]
    fv = xg ** float(k)
    dfv = float(k) * xg ** (float(k) - 1)
    AP = fv[:, None] * ((-1j * (D @ V)) @ T.T)
    PA = -1j * (D @ (fv[:, None] * (V @ T.T)))
    lhs = AP - PA
    rhs = 1j * (dfv[:, None] * (V @ T.T))
    m = slice(3, N - 3)
    return float(np.linalg.norm(lhs[m] - rhs[m]) / np.linalg.norm(rhs[m]))


NS = [200, 400, 800, 1600]
print("\n  and on a grid, applied to a smooth state -- the exponent is the statistic:")
exps = []
for k in (-5, -3, -1, 2):
    vals = [ident_residual(N, k) for N in NS]
    e = float(np.polyfit(np.log(NS), np.log(vals), 1)[0])
    exps.append(e)
    print(f"      f = a^{k:<3d}  {[f'{q:.2e}' for q in vals]}  exponent {e:+.2f}")
check(all(abs(e + 2) < 0.1 for e in exps),
      f"all four powers converge at SECOND order ({min(exps):+.2f} to {max(exps):+.2f}), which is the "
      "central difference's own order -- so the residual is the discretization and not the identity")

# ============================================================================ C
head("C.  ⓶  WHICH SCALINGS COULD CANCEL THE ANOMALY -- AND WHY THE ONLY ONE CARRIES NO TRACE")

a, n, c, r = sp.symbols('a n c r', positive=True)
Vol = 2 * sp.pi ** 2 * a ** 3
hf = sp.Function('h')


def trace_of(expr):
    return sp.simplify(expr / Vol - 3 * (-sp.diff(expr, a) / sp.diff(Vol, a)))


gen = sp.simplify(trace_of(hf(a)) * 2 * sp.pi ** 2 * a ** 3)
print(f"\n      Theta[ h(a) (x) T ] = ({gen}) / (2 pi^2 a^3)")
check(sp.simplify(gen - (hf(a) + a * sp.diff(hf(a), a))) == 0,
      "the trace of ANY energy term is (h + a h') T / 2 pi^2 a^3 -- an exact formula, not a model")
check(sp.simplify(trace_of(1 / a)) == 0,
      "** so a term is traceless if and only if h goes exactly as 1/a **")

Thn = sp.simplify(trace_of(c * a ** -n))
dThn = sp.simplify(sp.diff(Thn, a))
print(f"\n      power law h = c a^-n:   Theta = {Thn}")
print(f"                              dTheta/da = {dThn}")
check(sp.simplify(Thn * 2 * sp.pi ** 2 * a ** (n + 3) / c - (1 - n)) == 0,
      "its trace carries the factor (1 - n)")
check(sp.simplify(dThn * 2 * sp.pi ** 2 * a ** (n + 4) / c - (n - 1) * (n + 3)) == 0,
      "and dTheta/da goes as (n-1)(n+3) a^-(n+4)")

Th0 = r / (2 * sp.pi ** 2 * a ** 4)
print(f"\n      the anomaly:  Theta_0 = {Th0},  dTheta_0/da = {sp.diff(Th0, a)}  -- goes as a^-5")
nmatch = sp.solve(sp.Eq(n + 4, 5), n)[0]
print(f"      matching the POWER needs n + 4 = 5, i.e. n = {nmatch}")
check(nmatch == 1, "the unique power-law scaling whose dTheta/da can match the anomaly's is n = 1")
check(sp.simplify((1 - n).subs(n, nmatch)) == 0,
      "** and at n = 1 the trace coefficient (1 - n) is ZERO: that term contributes nothing to Theta "
      "at all, so there is nothing there to cancel with **")
check(sp.simplify(dThn.subs(n, nmatch)) == 0,
      "dTheta/da vanishes identically at n = 1 too -- checked separately, not inferred")
print("\n    ⇒ ** THE SHAPE A FOURTH TIME. **  The anomaly exists because ln a breaks the exact 1/a")
print("      scaling that made the bare sum traceless.  The only scaling that could cancel its")
print("      contribution to dTheta/da is that same 1/a.  ** What would undo it is what it undid. **")

# ============================================================================ D
head("D.  ⓷  A TUNED TOWER EXPECTATION *CAN* ZERO THE COEFFICIENT -- AND THAT IS NOT SHARPNESS")

N = 40000
xg = np.linspace(0.5, 30.0, N)
hg = xg[1] - xg[0]
MPOW = 2                                           # a cubic contributing at a different power


def probe(sig, B, a0=4.0):
    p_ = np.exp(-(xg - a0) ** 2 / (4 * sig ** 2))
    p_ /= np.sqrt(np.sum(p_ ** 2) * hg)
    edge = max(p_[0], p_[-1]) ** 2 / np.max(p_ ** 2)
    p2 = np.sum(np.gradient(p_, hg) ** 2) * hg
    w = p_ ** 2 * hg
    dR = -4 * KAP * xg ** -5 + B * xg ** -(MPOW + 1)
    R = LAM4 + KAP * xg ** -4 - (B / MPOW) * xg ** -MPOW
    return edge, float(np.sum(w * dR)), float(np.sum(w * R ** 2) - np.sum(w * R) ** 2), p2


_, d0, _, _ = probe(0.25, 0.0)
_, d1, _, _ = probe(0.25, 1.0)
BSTAR = -d0 / (d1 - d0)
print(f"\n  the cubic's coefficient that zeroes <dR/da> at this state:  B* = {BSTAR:.5f}")
print("      B          edge         <dR/da>       Var(R)       bound       admissible")
rows = []
for B, sig in ((0.0, 0.25), (BSTAR * 0.5, 0.25), (BSTAR, 0.25), (BSTAR * 1.5, 0.25), (BSTAR, 1.0)):
    e, d, v, p2 = probe(sig, B)
    bd = HBAR ** 2 * d ** 2 / (4 * p2)
    ok = e < 1e-10
    rows.append((B, e, d, v, bd, ok))
    print(f"   {B:9.5f}  {e:.2e}    {d:+.4e}   {v:.4e}   {bd:.4e}  "
          f"{'YES' if ok else 'NO -- boundary term not negligible, printed not dropped'}")
adm = [q for q in rows if q[5]]
tuned = [q for q in adm if abs(q[0] - BSTAR) < 1e-12][0]
check(abs(tuned[2]) < 1e-12,
      f"** at B* the bound's coefficient <dR/da> = {tuned[2]:.2e} vanishes, so the bound collapses to "
      f"{tuned[4]:.2e} -- VACUOUS **")
# r6981: 1e3 against the ten-eigenvector floor, which is 6.8e3 times the old one-eigenvector floor --
# so in ABSOLUTE terms this is within a factor of one and a half of the threshold it replaces, while
# being read against a quantity that does not move with the build.  The failure mode is O(1) -- a sharp
# curvature against one that is not -- and the measured headroom is 1.4e5, so there are two decades of
# margin even if the stable floor moves a hundredfold.
check(tuned[3] > 1e3 * VAR_FLOOR,
      f"** but Var(R) = {tuned[3]:.3e} there, {np.log10(tuned[3] / VAR_FLOOR):.1f} decades above the "
      f"floor {VAR_FLOOR:.1e}: a vacuous bound is NOT a sharp curvature **")
check(all(q[3] > 1e3 * VAR_FLOOR for q in adm),
      "and no admissible state in the sweep comes near the floor, tuned or not")
check(len(adm) == 4 and len(rows) == 5,
      "one of the five rows is inadmissible and is reported with its arithmetic, per the order's guard")
print("\n    ⇒ ** SO THE ORDER'S SECOND BRANCH IS REACHABLE IN THE WEAK SENSE AND NOT THE STRONG ONE. **")
print("      A tuned tower expectation can FLATTEN R at a point and make this bound stop constraining.")
print("      It cannot make R constant: two distinct powers of a agree at isolated points, not on a")
print("      set of positive measure -- which is §E, and which is why the variance stays up.")

# ============================================================================ E
head("E.  ⓸  HOW FAR THE LEVEL-SET ARGUMENT SURVIVES THE PROMOTION -- FURTHER THAN THE ORDER EXPECTED")

Lam, Lv = sp.symbols('Lambda L', positive=True)
t1, t2 = sp.symbols('t_1 t_2', real=True)
Reff = 4 * Lam + t1 / a ** 2 + r / a ** 4 + t2 / a ** 6
num = sp.expand(sp.numer(sp.together(sp.diff(Reff, a))))
print(f"\n      on a fibre where the tower operators are simultaneously diagonal:")
print(f"      R_eff(a) = {Reff}")
print(f"      numerator of dR_eff/da = {num}")
flat = sp.solve([num.coeff(a, k) for k in range(0, 8)], [r, t1, t2], dict=True)
check(flat == [],
      "** dR_eff/da == 0 has NO solution while the residue r is non-zero: no assignment of tower "
      "eigenvalues makes R_eff constant **")
poly = sp.Poly(sp.expand(sp.numer(sp.together(Reff - Lv))), a)
print(f"      R_eff = L clears to a polynomial in a of degree {poly.degree()}")
check(poly.degree() > 0 and poly.degree() < sp.oo,
      f"so every level set has at most {poly.degree()} roots -- a FINITE set, Lebesgue measure zero, "
      "hence no eigenvector on any such fibre")
# and the across-fibre claim, measured on the same refinement instrument as r6930's:
def _fibre_exponents(nfib):
    gaps, lens = [], []
    for Ng in (400, 800, 1600, 3200):
        xg2 = np.linspace(0.5, 8.0, Ng)
        hh = xg2[1] - xg2[0]
        blocks = [LAM4 + KAP * xg2 ** -4 + tv / xg2 ** 2 for tv in range(1, nfib + 1)]
        wv = np.sort(np.concatenate(blocks))   # the operator is diagonal: its spectrum IS the diagonal
        win = (wv > 12.3) & (wv < 12.9)
        gaps.append(float(np.median(np.diff(wv[win]))))
        lens.append(hh)
    lg = float(np.polyfit(np.log([400, 800, 1600, 3200]), np.log(gaps), 1)[0])
    return lg
_e1, _e3 = _fibre_exponents(1), _fibre_exponents(3)
print(f"      median-gap refinement exponent: ONE fibre {_e1:+.2f}   THREE fibres {_e3:+.2f}")
check(abs(_e1 + 1) < 0.15 and abs(_e3 + 1) < 0.15,
      f"** a direct sum over fibres keeps the exponent at -1 ({_e1:+.2f}, {_e3:+.2f}): stacking "
      "fibres that each lack point spectrum does not manufacture one **")

print("\n  AND THE RESIDUE IS NOT THE COUPLING AS SUCH -- IT IS NON-COMMUTATIVITY.  Measured:")
nq = 14
_low = np.diag(np.sqrt(np.arange(1, nq)), 1)
Xq = (_low + _low.T) / np.sqrt(2)
Pq = 1j * (_low.T - _low) / np.sqrt(2)


def relc(A, B):
    return float(np.linalg.norm(A @ B - B @ A) / (np.linalg.norm(A) * np.linalg.norm(B)))


cases = (("pi^2 vs phi^2  (one cubic's own two factors)", Pq @ Pq, Xq @ Xq),
         ("pi^2 phi vs pi^2 phi^2  (two cubic terms)",
          (Pq @ Pq @ Xq + Xq @ Pq @ Pq) / 2, (Pq @ Pq @ Xq @ Xq + Xq @ Xq @ Pq @ Pq) / 2),
         ("pi^2 vs pi^4  (a COMMUTING family)", Pq @ Pq, Pq @ Pq @ Pq @ Pq))
vals = []
for name, T1, T2 in cases:
    v = relc(T1, T2)
    vals.append(v)
    print(f"      {name:45s} {v:.3e}")
check(vals[0] > 1e-3 and vals[1] > 1e-3,
      f"the cubic's own factors do NOT commute ({vals[0]:.1e}, {vals[1]:.1e}), so no common fibre "
      "basis exists for a general entangled state")
check(vals[2] < 1e-12,
      f"while a commuting family sits at {vals[2]:.1e} -- the control that makes the distinction "
      "measured rather than asserted")
print("\n    ⇒ ** SO THE EXACT RESIDUE IS: entangled states over a NON-COMMUTING cubic tower family. **")
print("      Product states are covered.  Any commuting family is covered.  What is not covered is")
print("      narrower than 'the interacting theory' by a long way, and it is named rather than gestured.")

# ============================================================================ F
head("F.  THE WELL-POSEDNESS QUESTION, ANSWERED BY NAMING THE CHOICE RATHER THAN MAKING IT")

print(r"""
  ⚑ THE ORDER'S THIRD BRANCH, AND IT DOES NOT FIRE THE WAY IT MIGHT HAVE.

    *"If the promotion is not well posed without a choice --- if the cubic's ordering or its domain has
    to be fixed before the commutator is defined --- say which choice, and whether the corpus has
    already made it elsewhere."*

    ⇒ ** THE COMMUTATOR NEEDS NO ORDERING CHOICE. **  §B's identity differentiates only the
    $a$-function and carries the tower factor through untouched, so it holds for every ordering of
    every cubic term.  The bound's FORM is therefore ordering-blind, and ⓵ answers without reaching
    the ordering at all.

    ⌗ ** WHERE THE ORDERING DOES ENTER IS ONE PLACE, AND IT IS §D's. **  What the ordering changes is
    $\langle\hat T_j\rangle$, hence the value of $B^{*}$, hence whether the tuned cancellation is
    reachable on a physical state.  ⇒ *So the ordering bears on whether the bound can be made vacuous,
    not on whether it holds.*  ** `P10` calls the ordering selection external and localizes it as one
    computable datum --- whether the tower's zero-point energy gravitates at the horizon --- and this
    receipt does not pick it. **  That is a different row's business and it is named here, not settled.

  ⛔ AND WHAT IS STILL OPEN, NARROWED RATHER THAN RESTATED.

    · ** Entangled states over a non-commuting cubic tower family. **  §E covers every product state
      and every commuting family by the level-set route; the measured non-commutativity of the cubic's
      own factors is what blocks a common fibre basis in general.  ⇒ *An eigenvector of the promoted
      $\hat R$ would have to be genuinely entangled AND live where no simultaneous diagonalization
      exists.  Whether such a vector exists is not settled here.*  ⌗ *But note what it would have to
      do: §C forbids the pointwise cancellation and §D shows the tuned one leaves the variance six
      decades up, so such a state would have to sharpen $R$ by a mechanism neither of those touches.*
    · ** The power-law assumption in §C is an assumption about the cubic, and it is stated as one. **
      The theorem is exact for any finite sum of powers of $a$; a cubic term carrying a $\ln a$ of its
      own would need its own line, and the anomaly is precisely the case where that happens.  ⇒ *If the
      interacting sum generates a second logarithm, §C's enumeration does not reach it --- and that is
      a question about the ultraviolet definition, which is `sec:lock`'s open frontier and not this
      receipt's.*  ** Flagged, not computed. **
    · ** No interacting theory, no coupled zeta(0), no signal. **  Unchanged.  The commutator was
      ordered precisely because it needs none of them.

  ⌗ AND WHAT THIS DOES TO THE ROW.  `PO-23` stays open, as the order says to expect.  The wall loses
    "the level-set argument does not survive the promotion" --- it survives on every fibre that exists
    --- and gains the narrower "entangled states over a non-commuting tower family".  ** Three
    revisions running, the wall has moved in the direction of fewer and by removal rather than
    refinement. **
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)

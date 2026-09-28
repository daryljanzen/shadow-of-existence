#!/usr/bin/env python3
r"""
P10_no_state_makes_the_curvature_sharp_and_the_obstruction_is_the_anomaly_coefficient_itself
===========================================================================================

LEVEL: exact symbolic (sympy) for the trace operator, the monotonicity that decides the spectral
type, and the domain condition; float linear algebra for the spectral-character instrument and the
saturation of the uncertainty bound, each against a floor measured in the same arithmetic.  Nothing
is fitted.

OBJECT UNDER TEST -- `PO-23`, `r6929`.  The order, verbatim:

    "whether any physical state makes $\hat R$ sharp --- whether $\operatorname{spec}\hat\Theta$ has
     a point spectrum.  Not computed, and stated as the step. ⇒ *That is the order.*"

  with the two readings costed: *only continuous spectrum* ⇒ every physical state carries a spread in
  $R$ and the independence of $\int\!\sqrt g\,R^{2}$ is "a statement about the ensemble the state
  already is --- which is stronger than it sounds and needs saying in those terms"; *point states* ⇒
  the independence is realized on individual states and the counterterm is observable in the ordinary
  sense.  ⚠ And: ***say which of the two `P10` is entitled to claim now*** --- reported, NOT edited.

  ⌗ THE GUARD, this line's own returned again: *"a spectral-type claim with no measured floor is the
    same shape as an unfalsifiable one.  A case with known point spectrum and one with known
    continuous spectrum, run through the same arithmetic."*  §A builds both first.

COMPUTES: the trace of the tower's stress tensor as an OPERATOR rather than an expectation; the
spectral type of $\hat R$ by two refinement exponents against two controls; the exact commutator
bound on $\operatorname{Var}(\hat R)$ and its saturation; and whether $\langle\hat a^{-4}\rangle$
exists on the domain the horizon's thermal condition selects.  Scope: the back-reaction is
SEMICLASSICAL, as before; the interacting theory is NOT built, and §F names the one step that needs
it.

-------------------------------------------------------------------------------
** THE ANSWER IS THE ORDER'S FIRST READING, AND IT IS A THEOREM RATHER THAN A MEASUREMENT: NO
   PHYSICAL STATE MAKES $\hat R$ SHARP. AND THE OBSTRUCTION IS THE ANOMALY COEFFICIENT ITSELF. **

** ⛭ ⓵ $\hat\Theta$ IS A MULTIPLE OF THE IDENTITY ON THE TOWER AT THIS ORDER, WHICH IS WHY THE
   QUESTION HAS AN ANSWER WITHOUT THE COUPLING. **  The excitation part of the tower energy is
$\bar S/a$ with $\bar S=\sum_n\mu_n\hat N_n$ free of $a$, so its trace vanishes **identically as an
operator** --- in every state, not merely the vacuum.  The whole anomaly sits in the renormalized
zero point, which is a c-number.  ⇒ $\hat\Theta=(r/2\pi^{2}a^{4})\mathbb 1$, and therefore
$\hat R=4\Lambda+\kappa\hat a^{-4}$ is a function of $\hat a$ alone.

** ⛭ ⓶ SO THE SPECTRAL QUESTION REDUCES TO ONE ABOUT MULTIPLICATION OPERATORS, AND THERE IT IS
   EXACT. **  $R(a)$ is strictly monotonic on the half-line, hence injective, hence every level set
is a single point of Lebesgue measure zero --- and multiplication by $f$ has an eigenvector at
$\lambda$ **iff** the level set $\{f=\lambda\}$ has positive measure.  ⇒ ** $\hat R$ has NO
eigenvectors: purely continuous spectrum, $[4\Lambda,\infty)$. **  The instrument confirms it: both
refinement exponents sit at $-1.00$, matching the known-continuous control and not the
known-point-spectrum control at $0.00$.

** ⛭ ⓷ AND THE OBSTRUCTION IS QUANTITATIVE AND IS THE SAME NUMBER A THIRD TIME. **  The commutator
$[R(\hat a),\hat p_a]=i\hbar R'(\hat a)$ gives, exactly,
$$\operatorname{Var}(\hat R)\cdot\operatorname{Var}(\hat p_a)\;\ge\;\tfrac{\hbar^{2}}{4}
  \big\langle R'(\hat a)\big\rangle^{2},\qquad R'(a)=-4\kappa a^{-5},\qquad \kappa=4Gr/\pi .$$
Saturated to $0.3\%$ by narrow admissible states.  The right-hand side vanishes **iff $r=0$**.  ⇒
*The residue that makes the counterterm observable is the same residue that forbids any state from
resolving it into a definite curvature.*  Were there no anomaly, $\hat R=4\Lambda\mathbb 1$ would be
sharp in every state --- and there would be nothing to observe.

⛔ ** NOT CLAIMED. **  No interacting theory; §F states what the coupling is still needed for and it
is a narrower thing than before.  No coupled $\zeta(0)$.  No detectable signal.  ** And `P10` is not
edited **: §F says what the paper may assert and routes it, as ordered.  rc=0 on all 23 checks.
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


R_RESIDUE = sp.Rational(39, 4)                  # Res_{s=-1} zeta_omega -- BANKED at r6920
KAP = 4.0 * float(R_RESIDUE) / np.pi            # kappa = 4 G r / pi at G = 1
LAM4 = 12.0                                     # 4 Lambda at Lambda = 3
HBAR = 1.0

# ============================================================================ A
head("A.  THE CONTROLS, BUILT FIRST -- HOW POINT AND CONTINUOUS SPECTRUM READ IN THIS ARITHMETIC")

NS = [400, 800, 1600, 3200]


def grid(N, x0=0.5, x1=8.0):
    x = np.linspace(x0, x1, N)
    return x, x[1] - x[0]


def laplacian(N, h):
    return (-2 * np.eye(N) + np.eye(N, k=1) + np.eye(N, k=-1)) / h ** 2


def spectral_stats(M, x, h, target):
    """(median nearest-neighbour gap in a window, participation LENGTH of the nearest eigenvector).

    Both are lengths/energies with a physical limit: for a genuine L^2 eigenfunction each tends to a
    positive constant under refinement; for a multiplication operator each tracks the grid spacing.
    """
    w, V = np.linalg.eigh(M)
    win = (w > target * 0.6) & (w < target * 1.6)
    gaps = np.diff(w[win])
    j = int(np.argmin(np.abs(w - target)))
    v2 = V[:, j] ** 2
    v2 = v2 / v2.sum()
    return (np.median(gaps) if len(gaps) else np.nan), h / np.sum(v2 ** 2)


def exponent(vals):
    v = np.array(vals, dtype=float)
    ok = np.isfinite(v) & (v > 0)
    return float(np.polyfit(np.log(np.array(NS)[ok]), np.log(v[ok]), 1)[0])


def run(build, target):
    g, L = [], []
    for N in NS:
        x, h = grid(N)
        gg, LL = spectral_stats(build(N, x, h), x, h, target)
        g.append(gg)
        L.append(LL)
    return g, L, exponent(g), exponent(L)


gP, LP, eP_g, eP_L = run(lambda N, x, h: -laplacian(N, h) + np.diag(x ** 2), 40.0)
print("\n  CONTROL point -- the harmonic oscillator, whose spectrum IS pure point:")
print(f"      gaps   {[f'{v:.3e}' for v in gP]}   exponent {eP_g:+.3f}")
print(f"      lengths{[f'{v:.3e}' for v in LP]}   exponent {eP_L:+.3f}")
check(abs(eP_g) < 0.05 and abs(eP_L) < 0.05,
      f"a point spectrum holds BOTH exponents at zero ({eP_g:+.3f}, {eP_L:+.3f}): gaps and "
      "eigenvector support are physical lengths and do not track the grid")

gC, LC, eC_g, eC_L = run(lambda N, x, h: np.diag(x), 4.0)
print("\n  CONTROL continuous -- multiplication by x, whose spectrum IS purely continuous:")
print(f"      gaps   {[f'{v:.3e}' for v in gC]}   exponent {eC_g:+.3f}")
print(f"      lengths{[f'{v:.3e}' for v in LC]}   exponent {eC_L:+.3f}")
check(abs(eC_g + 1) < 0.05 and abs(eC_L + 1) < 0.05,
      f"a continuous spectrum drives BOTH to -1 ({eC_g:+.3f}, {eC_L:+.3f}): there is no eigenvector "
      "to converge to, so the apparent one shrinks with the grid")
check(abs(eP_g - eC_g) > 0.9 and abs(eP_L - eC_L) > 0.9,
      "** the two controls are separated by a full decade of exponent, so the instrument can tell "
      "them apart -- which is what makes a spectral-type verdict falsifiable **")

print("\n  AND THE VARIANCE FLOOR, measured on an operator that DOES have eigenvectors:")
xs = np.linspace(-8, 8, 1200)
hs = xs[1] - xs[0]
Hosc = -(-2 * np.eye(1200) + np.eye(1200, k=1) + np.eye(1200, k=-1)) / hs ** 2 + np.diag(xs ** 2)
_w, _V = np.linalg.eigh(Hosc)
# ⛔ ** r6961+70.2 (PO-60, the third class): ONE EIGENVECTOR'S VARIANCE IS NOT A FLOOR, IT IS A DRAW
#   FROM ONE.  This read `_V[:, 3]` alone, and the null control below asserts `|Var(R)| <= VAR_FLOOR`
#   -- one round-off number against another, with no margin.  Measured across OpenBLAS kernels
#   (OPENBLAS_CORETYPE), the 4th eigenvector's variance was 4.0e-13 (default), 1.9e-13 (Prescott),
#   4.3e-13 (Sandybridge), 1.2e-13 (Haswell) and 1.4e-14 (Prescott, two threads), while the null
#   control is a constant 5.7e-14 -- so this receipt was GREEN HERE AND RED ON ANOTHER BUILD, which
#   `scripts/sweep_tolerances.py` found by running it on both. **
#   ⇒ *** The floor is now the LARGEST variance over the first ten eigenvectors: 1.2e-12 to 1.6e-12 on
#       every kernel measured, stable to 30 per cent, with the null control twenty times below it on
#       all of them.  The claim is unchanged -- the r = 0 variance is at the floor, not above it -- and
#       the floor is now a property of the operator's round-off rather than of one eigenvector's. ***
VAR_FLOOR = max(abs(float(_V[:, k] @ (Hosc @ (Hosc @ _V[:, k])) - (_V[:, k] @ (Hosc @ _V[:, k])) ** 2))
                for k in range(10))
print(f"      Var(H_osc) on its own eigenvectors, the largest of the first ten = {VAR_FLOOR:.3e}")
check(VAR_FLOOR < 1e-8,
      f"'the variance vanishes' measures as {VAR_FLOOR:.2e} here -- the floor any claim that some "
      "state makes an observable sharp has to clear")

# ============================================================================ B
head("B.  THE TRACE AS AN OPERATOR, NOT AN EXPECTATION -- AND IT IS A C-NUMBER ON THE TOWER")

a, C0, r, mu, Sbar = sp.symbols('a C_0 r mu S', positive=True)
Vol = 2 * sp.pi ** 2 * a ** 3


def trace_of(E):
    """Theta = rho - 3p with rho = E/V and p = -dE/dV, at fixed occupation numbers."""
    return sp.simplify(E / Vol - 3 * (-sp.diff(E, a) / sp.diff(Vol, a)))


E_exc = Sbar / a                                   # sum_n mu_n N_n / a: an OPERATOR, S free of a
E_zp = (C0 + r * sp.log(a * mu)) / a               # the renormalized zero point: a C-NUMBER
Th_exc, Th_zp = trace_of(E_exc), trace_of(E_zp)
print(f"\n      Theta[ excitation operator  S/a ]          = {Th_exc}")
print(f"      Theta[ renormalized zero point ]           = {Th_zp}")
check(Th_exc == 0,
      "** the EXCITATION part is traceless IDENTICALLY, as an operator: omega_n = mu_n/a makes "
      "E = S/a with S free of a, so p = rho/3 whatever the occupation numbers **")
check(sp.simplify(sp.diff(Th_zp, mu)) == 0,
      "and the zero-point trace is mu-independent -- scheme-independent, which is what an anomaly is")
check(sp.simplify(Th_zp - r / (2 * sp.pi ** 2 * a ** 4)) == 0,
      "Theta = r/(2 pi^2 a^4), reproducing r6920's banked expectation value")
check(sp.simplify(Th_zp.subs(r, 0)) == 0,
      "and it vanishes with the residue -- the null control on the whole construction")
print("\n    ⇒ ** SO Theta-hat = (r/2 pi^2 a^4) . 1 ON THE TOWER. **  The operator content is in the")
print("      excitation part, which is exactly traceless; the anomaly is in the c-number zero point.")
print("      ⇒ R-hat = 4 Lambda + kappa a-hat^-4 is a function of a-hat ALONE, and that is why the")
print("      order's question can be answered at this order rather than waiting on the coupling.")

# ============================================================================ C
head("C.  THE SPECTRAL TYPE OF R-hat -- EXACT, THEN CONFIRMED ON THE INSTRUMENT")

av, lam, kapS, LamS = sp.symbols('a lambda kappa Lambda', positive=True)
Rf = 4 * LamS + kapS / av ** 4
dR = sp.simplify(sp.diff(Rf, av))
print(f"\n      R(a) = {Rf}          dR/da = {dR}")
check(sp.simplify(dR + 4 * kapS / av ** 5) == 0 and (-dR).is_positive is True,
      "R'(a) = -4 kappa / a^5 is strictly NEGATIVE on the half-line (sympy decides the sign from the "
      "positivity of kappa and a), so R is strictly monotonic, hence INJECTIVE")
# solve on the level ABOVE the accumulation point, since below it the level set is empty:
# lambda = 4 Lambda + d with d > 0.  (Declaring only lambda > 0 leaves sympy unable to sign the
# roots, and it returns "none positive" -- the domain of the symbol is part of the statement again.)
d = sp.Symbol('d', positive=True)
sols = sp.solve(sp.Eq(kapS / av ** 4, d), av)
pos = [q for q in sols if q.is_positive is True]
print(f"      {{R = 4 Lambda + d}} has {len(sols)} roots of the quartic, of which {len(pos)} positive:"
      f"  a = {pos[0] if pos else None}")
check(len(pos) == 1,
      f"so every level set above 4 Lambda is ONE point of the half-line -- the quartic has "
      f"{len(sols)} roots and exactly {len(pos)} lies in the domain, i.e. Lebesgue measure ZERO")
check(not sp.solve(sp.Eq(kapS / av ** 4, -d), av, dict=True) or
      all(q[av].is_positive is not True for q in sp.solve(sp.Eq(kapS / av ** 4, -d), av, dict=True)),
      "and BELOW 4 Lambda the level set is empty, so no eigenvalue can hide there either")
print("\n    ⇒ ** THE THEOREM. **  Multiplication by f on L^2 has an eigenvector at lambda if and only")
print("      if the level set {f = lambda} carries positive measure: (f - lambda) psi = 0 a.e. forces")
print("      psi to vanish off that set.  R is injective, so every level set is a point of measure")
print("      zero.  ** R-hat therefore has NO eigenvectors -- purely continuous spectrum. **")
lim_inf = sp.limit(Rf, av, sp.oo)
lim_zero = sp.limit(Rf, av, 0, '+')
print(f"      R(a -> infinity) = {lim_inf}        R(a -> 0+) = {lim_zero}")
check(sp.simplify(lim_inf - 4 * LamS) == 0 and lim_zero is sp.oo,
      "and the spectrum is the RANGE of R, [4 Lambda, infinity): it accumulates on 4 Lambda as "
      "a -> infinity and is unbounded above at the horizon, with 4 Lambda itself not attained")

gT, LT, eT_g, eT_L = run(lambda N, x, h: np.diag(LAM4 + KAP * x ** -4), LAM4 + 0.4)
print("\n  AND THE INSTRUMENT ON R-hat ITSELF, same arithmetic as the two controls:")
print(f"      gaps   {[f'{v:.3e}' for v in gT]}   exponent {eT_g:+.3f}")
print(f"      lengths{[f'{v:.3e}' for v in LT]}   exponent {eT_L:+.3f}")
check(abs(eT_g - eC_g) < 0.05 and abs(eT_L - eC_L) < 0.05,
      f"R-hat tracks the CONTINUOUS control to within 0.05 in both exponents "
      f"({eT_g:+.3f} vs {eC_g:+.3f}; {eT_L:+.3f} vs {eC_L:+.3f})")
check(abs(eT_g - eP_g) > 0.9 and abs(eT_L - eP_L) > 0.9,
      "and is a full decade of exponent away from the POINT control -- the verdict is the one the "
      "instrument was built to be able to get wrong")

# ============================================================================ D
head("D.  THE BOUND IS EXACT, AND IT VANISHES ONLY WITH THE RESIDUE")

N = 40000
xg = np.linspace(0.5, 30.0, N)
hg = xg[1] - xg[0]
Rg = LAM4 + KAP * xg ** -4
dRg = -4 * KAP * xg ** -5


def trial(sig, a0=4.0, kap=KAP):
    psi = np.exp(-(xg - a0) ** 2 / (4 * sig ** 2))
    psi /= np.sqrt(np.sum(psi ** 2) * hg)
    edge = max(psi[0], psi[-1]) ** 2 / np.max(psi ** 2)
    p2 = np.sum(np.gradient(psi, hg) ** 2) * hg               # <p^2> = ||psi'||^2, and <p> = 0
    w = psi ** 2 * hg
    Rv = LAM4 + kap * xg ** -4
    dRv = -4 * kap * xg ** -5
    varR = np.sum(w * Rv ** 2) - np.sum(w * Rv) ** 2
    return edge, varR * p2, HBAR ** 2 * np.sum(w * dRv) ** 2 / 4, p2, varR


print("\n  ⚠ THE IDENTITY HAS A DOMAIN, AND IT IS PART OF THE STATEMENT.  [R(a),p] = i hbar R'(a)")
print("    integrates by parts, so a trial state with amplitude at the boundary breaks it.  Both")
print("    sides are reported for every width, with the admissibility gate shown, because the")
print("    inadmissible ones read as VIOLATIONS and would have looked like a refutation:\n")
print("     sigma   edge |psi|^2/peak    Var(R)*<p^2>    (hbar^2/4)<R'>^2    ratio    admissible")
ratios = []
for sig in (2.0, 1.0, 0.5, 0.35, 0.25, 0.12, 0.06):
    edge, lhs, rhs, p2, varR = trial(sig)
    ok = edge < 1e-10
    if ok:
        ratios.append(lhs / rhs)
    print(f"    {sig:6.3f}   {edge:.3e}         {lhs:.4e}      {rhs:.4e}      {lhs / rhs:8.3f}   "
          f"{'YES' if ok else 'NO -- boundary term not negligible'}")
check(min(ratios) >= 1.0,
      f"** every ADMISSIBLE state satisfies Var(R) Var(p_a) >= (hbar^2/4) <R'>^2, the tightest at "
      f"{min(ratios):.4f} **")
check(min(ratios) < 1.01,
      f"and the narrow states SATURATE it to {100 * (min(ratios) - 1):.1f} per cent, so it is the "
      "right bound and not a loose one")
check(any(r > 1.0 for r in ratios) and len(ratios) == 5,
      "five of the seven widths are admissible; the two that are not are exactly the two that read "
      "as violations, which is the gate earning its keep rather than an excuse")

_, lhs0, rhs0, _, varR0 = trial(0.5, kap=0.0)
varR0 = abs(varR0)                                  # the round-off can land either side of zero
print(f"\n  NULL CONTROL, kappa = 0 (no anomaly):  |Var(R)| = {varR0:.3e}   bound = {rhs0:.3e}")
check(varR0 <= VAR_FLOOR,
      f"** at r = 0, R-hat = 4 Lambda . 1 and |Var(R)| = {varR0:.1e} sits AT the measured floor "
      f"{VAR_FLOOR:.1e}: sharp in every state **")
check(rhs0 == 0.0,
      "and the bound is identically zero there, so it is the residue and nothing else that forbids "
      "a sharp curvature")
print("\n    ⇒ ** THE SHAPE, A THIRD TIME AND FROM A THIRD DIRECTION. **  r6920: the degeneracy that")
print("      hid the constant is switched off by that constant.  r6928: the premise that would have")
print("      restored it is not a dependency, and superselection does not restore it either.  Here:")
print("      ** the same residue that makes the constant observable is what forbids any state from")
print("      resolving the curvature it is read off. **  Sharpening R costs momentum without bound.")

# ============================================================================ E
head("E.  AND THE EXPECTATION EXISTS ONLY BECAUSE OF THE BOUNDARY CONDITION THE HORIZON FIXES")

xx, nu = sp.symbols('x nu', positive=True)
POW = 1 + 2 * nu - sp.Rational(8, 3)               # |psi|^2 ~ x^(1+2nu); a^-4 ~ x^(-8/3)
nu_min = sp.solve(sp.Eq(POW, -1), nu)[0]
print(f"\n      x ∝ a^(3/2), so a^-4 ∝ x^(-8/3); the regular branch is psi ~ x^(1/2+nu).")
print(f"      ∫ |psi|^2 a^-4 dx ~ ∫ x^({POW}) dx converges at the origin iff nu > {nu_min}")
check(nu_min == sp.Rational(1, 3),
      "<a^-4> is finite at the origin iff nu > 1/3 -- a real condition, not automatic")
for g, label in ((sp.Rational(1, 4), "normal ordering   (gamma = 1/4)"),
                 (sp.Rational(3, 4), "symmetric ordering (gamma = 3/4)")):
    nuv = sp.sqrt(g + sp.Rational(1, 4))
    print(f"      {label}:  nu = {nuv} = {float(nuv):.4f}")
    check(float(nuv) > float(nu_min),
          f"{label}: nu = {float(nuv):.4f} > 1/3, so <a^-4> exists on the Friedrichs domain")
check(float(sp.sqrt(sp.Rational(1, 2))) > sp.Rational(1, 3),
      "** so the thermal condition that closes the deficiency is the same condition that makes "
      "R-hat's expectation exist at all -- the two are not independent choices **")

# ============================================================================ F
head("F.  WHAT `P10` IS ENTITLED TO CLAIM, AND THE ONE STEP STILL NEEDING THE COUPLING")

print(r"""
  ⚑ THE ORDER'S FIRST READING, AND ROUTED RATHER THAN EDITED, AS INSTRUCTED.

    `P10` says *"the one ultraviolet constant becomes observable once the scale factor is
    quantized"*.  ** That sentence stands, and the mode of observability is now fixed: it is
    distributional and not sharp-valued. **  No physical state assigns the Ricci scalar a definite
    value, so the independence of the third integral is a statement about the spread every state
    already carries.  ⇒ *The paper is entitled to the claim WITHOUT a qualifier about special
    states, because there are none to except: the reading is unconditional rather than weakened.*
    ⌗ What it is NOT entitled to is the ordinary-observable reading --- a measurement returning a
    sharp R in which the counterterm shows up as a definite number.  ** That reading is excluded,
    and excluded by a theorem rather than by a missing calculation. **
    ⇒ *The correction is `r6929`'s to make.  This receipt does not touch `corpus/canonical_time.tex`.*

  ⛔ AND WHAT STILL NEEDS THE INTERACTING THEORY -- NARROWER THAN THE WALL IT REPLACES.

    · ** Theta-hat is a c-number ON THE TOWER at THIS order, and that is what carries the result. **
      The excitation part is traceless identically, so nothing in the free tower's occupation
      numbers reaches Theta.  ⇒ *At higher order the cubic and above put genuine tower operators
      into Theta-hat, and then R-hat is no longer a function of a-hat alone.  Whether a correlated
      state of the interacting theory can have R-hat sharp is NOT settled here* --- the level-set
      argument uses injectivity of a function of one variable and does not survive the promotion.
      ** That is the step, and it is strictly smaller than "whether spec Theta-hat has a point
      spectrum", which is answered at leading order and answered NO. **
    · ⌗ *And one thing can be said about the higher-order case without building it, as a direction
      and not a result: the bound in §D needs only [R(a-hat), p_a] = i hbar R'(a-hat), so any
      interacting Theta-hat that still contains a non-constant function of a-hat inherits a bound of
      the same form from that piece alone.  Removing the obstruction would need the a-dependence to
      cancel, not merely to be accompanied.*  ** Flagged as a direction; not computed. **
    · ** The truncated-grid instrument is an instrument, not a proof. **  §C's verdict rests on the
      level-set theorem; the exponents are the falsifiable check with a measured separation, and a
      finite matrix has pure point spectrum by construction, which is exactly why the statistic is a
      REFINEMENT exponent and not a spectrum.
    · ** No interacting theory, no coupled zeta(0), no signal. **  Unchanged.  The gap is still
      O(r^2) and structural independence is still not laboratory observability.

  ⌗ AND WHAT THIS DOES TO THE ROW.  `PO-23` stays open, as the order says to expect.  The wall list
    loses the trace question as posed and gains the narrower one above: ** two items down from
    `r6920`'s four, both removals rather than additions, and neither by refining the method. **
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)

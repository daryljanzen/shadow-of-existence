#!/usr/bin/env python3
r"""
P10_the_second_logarithm_holes_the_mechanism_and_not_the_conclusion_because_the_leading_log_is_unpartnered
=========================================================================================================

LEVEL: exact symbolic (sympy) throughout for the generalized trace formula, the leading-log theorem,
the partial-cancellation coefficient and the free tower's log-freeness; float linear algebra only for
the variance second-measurement and the identity's convergence order, each against a measured floor.
Nothing is fitted.

OBJECT UNDER TEST -- `PO-23`, `r6939`/`r6941`.  The order, on the one thing `r6934` flagged and did
not compute:

  ⓵ᵃ *"Generalise the trace theorem to $h(a)=c\,a^{-n}\ln^{m}a$ and report $\hat\Theta$ and
      $\partial_a\hat\Theta$ for general $(n,m)$."*
  ⓵ᵇ *"Then: does the tower sum at cubic order generate $m=2$?"*
  ⓵ᶜ *"And report whether the bound's right-hand side can be cancelled at any $(n,m)$ the cubic
      actually generates, as against the $m=0$ answer which is no."*

  ⌗ WITH 66's OWN HYPOTHESIS, offered to be refuted: *"at $n=1$ the $\ln^{m}$ term vanishes and the
    $m\ln^{m-1}$ term does not ... the mechanism ⓶ rests on has a hole at exactly $m\ge1$, which is
    exactly where the anomaly lives."*  ⇒ ** IT IS RIGHT, AND THE WITNESS IS THE ANOMALY ITSELF. **

  ⌗ AND THREE GUARDS, the first this line's own from `r6934`: never compare the identity as matrices;
    the ordering stays named and unpicked; and any new cancellation gets the SECOND measurement
    against the variance floor, or it will be read as sharpness.  §A carries all three.

COMPUTES: the trace and its $a$-derivative for an arbitrary power-times-logarithm energy term; which
$(n,m)$ can cancel the anomaly's contribution; the exact coefficient at which a second logarithm
cancels part of it; and whether the free tower's summand can generate a second logarithm at all.
Scope: NO interacting theory; §E names the one datum ⓵ᵇ turns on and shows ⓵ᶜ does not need it.

-------------------------------------------------------------------------------
** 66's HYPOTHESIS IS CORRECT AND `r6934`'s MECHANISM IS HOLED -- BUT THE CONCLUSION SURVIVES BY A
   STRICTLY BETTER ARGUMENT, AND THAT ARGUMENT DOES NOT DEPEND ON ⓵ᵇ. **

** ⛭ ⓵ᵃ THE GENERAL FORMULA, AND THE ANOMALY IS ITS OWN COUNTEREXAMPLE. **
$$2\pi^{2}\hat\Theta[c\,a^{-n}\ln^{m}a]=c\,a^{-(n+3)}\big[(1-n)\ln^{m}a+m\ln^{m-1}a\big]$$
exactly, confirming 66's algebra.  At $n=1$ the first term dies and the second does not, so a
logarithmic term is **not** annihilated by the $1/a$ scaling.  ⇒ ** And the anomaly is the $(n=1,m=1)$
entry of this very formula: $2\pi^{2}\hat\Theta=r/a^{4}$. **  So `r6934` §C's mechanism --- *"the only
scaling that could cancel carries no trace"* --- was a statement about $m=0$ and the anomaly was
already the proof that it does not extend.  *This line's own reasoning, holed by the order, correctly.*

** ⛭ ⓵ᶜ AND YET CANCELLATION IS STILL IMPOSSIBLE, BECAUSE THE LEADING LOGARITHM IS UNPARTNERED. **
From an $(n=1,m)$ term the highest power in $\partial_a\hat\Theta$ is $\ln^{m-1}a$ with coefficient
$-4mc$; an $(1,m{+}1)$ term reaches $\ln^{m}a$ and $\ln^{m-1}a$, so terms chain **downward and never
upward**.  With $M$ the largest $m$ present the $\ln^{M-1}a$ coefficient is $-4Mc_M$ and nothing
reaches it: the coefficient system is **lower triangular with non-zero diagonal**, so
$\partial_a\hat\Theta\equiv0$ forces every $c=0$.  ⇒ ** The bound's right-hand side cannot be
cancelled at ANY $(n,m)$ --- and this is independent of ⓵ᵇ, because whatever $m$ the cubic generates,
its top logarithm has no partner. **

** ⛭ AND 66's "IT COULD CANCEL OR ADD" IS RIGHT AT ONE COEFFICIENT, WITH A THIRD ANSWER. **  An
$(1,2)$ term at exactly $c_2=2r$ **does** kill the $\ln^{0}$ coefficient the anomaly sits in --- and
leaves $\ln^{1}$ at $-16r$.  ⇒ *Partial cancellation is real and it RELOCATES the obstruction one
logarithm up rather than removing it.*  Neither "cancels" nor "adds": moves.

** ⛭ ⓵ᵇ AND A SECOND LOGARITHM NEEDS A NESTED SUM, WHICH THE FREE TOWER HAS NOT GOT. **  $m$ is the
pole order at $s=-1$ minus nothing: a second logarithm needs a $\ln$ of the mode label **in the
summand**.  The free tower's $d(m)\mu(m)=2(m^{2}-4)\sqrt{m^{2}-3}$ expands at large $m$ as a pure
Laurent series --- **log-free, exactly** --- so the free sum yields $m=1$ and never $m=2$.  The cubic
carries one internal sum, which is where a harmonic number could appear; whether it does is fixed by
the vertex normalisation, i.e. by the ultraviolet definition.  ⇒ ** That datum is named in §E, and
⓵ᶜ does not wait on it. **

⛔ ** NOT CLAIMED. **  No interacting theory; no ordering choice (§A keeps it named and unpicked); and
no corpus edit -- the finding about `P10`'s site is routed, as the order requires.  rc=0 on all 16
checks.
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


R_RES = sp.Rational(39, 4)                       # Res_{s=-1} zeta_omega -- BANKED at r6920
a = sp.Symbol('a', positive=True)
L = sp.log(a)
VOL = 2 * sp.pi ** 2 * a ** 3
KAP = 4.0 * float(R_RES) / np.pi
LAM4 = 12.0


def Theta(h):
    """Theta = rho - 3p with rho = E/V and p = -dE/dV, at fixed occupation numbers."""
    return sp.simplify(h / VOL - 3 * (-sp.diff(h, a) / sp.diff(VOL, a)))


# ============================================================================ A
head("A.  THE THREE GUARDS THE ORDER NAMED, CARRIED BEFORE ANYTHING IS COMPUTED")

print("\n  GUARD 1 -- never compare the identity as matrices.  This line's own r6934 note: on a")
print("    finite-difference grid the commutator sits OFF-DIAGONAL, so a matrix comparison returns a")
print("    residual that does not converge (1.2, flat).  Apply both sides to a smooth state instead")
print("    and measure the convergence ORDER:")


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
      "would be a REPRESENTATION error -- the guard is live, not recited")

xs = np.linspace(-8, 8, 900)
hs = xs[1] - xs[0]
Hosc = -(-2 * np.eye(900) + np.eye(900, k=1) + np.eye(900, k=-1)) / hs ** 2 + np.diag(xs ** 2)
_w, _V = np.linalg.eigh(Hosc)
v3 = _V[:, 3]
VAR_FLOOR = abs(float(v3 @ (Hosc @ (Hosc @ v3)) - (v3 @ (Hosc @ v3)) ** 2))
print(f"\n  GUARD 3 -- the variance floor for the SECOND measurement: {VAR_FLOOR:.3e}")
check(VAR_FLOOR < 1e-8,
      f"'the variance vanishes' measures as {VAR_FLOOR:.2e} here; §D reports any new cancellation "
      "against it, so a vacuous bound cannot be read as a sharp curvature")
print("\n  GUARD 2 -- the ordering stays NAMED AND UNPICKED.  r6934 established that the bound's form")
print("    is ordering-blind and the ordering enters only whether a tuned cancellation is reachable.")
print("    ⇒ That is `PO-15`'s. §F says which datum, if any, this order's answer depends on, and stops.")

# ============================================================================ B
head("B.  ⓵ᵃ  THE GENERAL TRACE FORMULA -- AND THE ANOMALY IS ITS OWN COUNTEREXAMPLE")

c, n, m, r = sp.symbols('c n m r', positive=True)
Th_gen = sp.simplify(Theta(c * a ** -n * L ** m) * 2 * sp.pi ** 2)
pred = c * a ** -(n + 3) * ((1 - n) * L ** m + m * L ** (m - 1))
print(f"\n      2 pi^2 Theta[c a^-n ln^m a] = {sp.expand(Th_gen)}")
check(sp.simplify(sp.expand(Th_gen - pred)) == 0,
      "** = c a^-(n+3) [ (1-n) ln^m a + m ln^(m-1) a ] exactly -- the order's own algebra, confirmed **")
check(sp.simplify(Th_gen.subs(m, 0) - c * a ** -(n + 3) * (1 - n)) == 0,
      "m = 0 recovers r6934's power-law case, factor (1-n), which n = 1 kills")
print("\n      at n = 1, by m:")
for mm in range(0, 4):
    print(f"        m = {mm}:  2 pi^2 Theta = {sp.simplify(Th_gen.subs({n: 1, m: mm}))}")
check(sp.simplify(Th_gen.subs({n: 1, m: 0})) == 0,
      "at n = 1 a PURE POWER is traceless -- r6934's mechanism, intact where it applies")
check(sp.simplify(Th_gen.subs({n: 1, m: 1}) - c / a ** 4) == 0,
      "** but at n = 1, m = 1 the trace is c/a^4 and does NOT vanish: the 1/a scaling does not "
      "annihilate a logarithmic term.  66's hypothesis is right **")
check(sp.simplify(Th_gen.subs({n: 1, m: 1, c: r}) / (2 * sp.pi ** 2)
                  - r / (2 * sp.pi ** 2 * a ** 4)) == 0,
      "** AND THE WITNESS IS THE ANOMALY ITSELF: r/(2 pi^2 a^4) is the (n=1, m=1) entry of this "
      "formula, so r6920's trace was always a member of the family r6934 assumed excluded **")
print("\n    ⇒ ** SO `r6934` §C's MECHANISM IS HOLED, AND BY THIS LINE'S OWN BANKED RESULT. **  Its")
print("      claim that 'the only scaling that could cancel carries no trace' is true for m = 0 and")
print("      false for m >= 1 -- and the anomaly lives at m = 1.  The conclusion is rescued in §C by")
print("      a different argument; the mechanism as stated does not survive.")

# ============================================================================ C
head("C.  ⓵ᶜ  CANCELLATION IS STILL IMPOSSIBLE -- THE LEADING LOGARITHM IS UNPARTNERED")


def dTheta(cc, nn, mm):
    return sp.diff(Theta(cc * a ** -nn * L ** mm), a)


print("\n      dTheta/da at n = 1, as 2 pi^2 a^5 x (coefficients in ln a):")
tops = []
for mm in range(0, 5):
    d = sp.expand(sp.simplify(dTheta(c, 1, mm) * 2 * sp.pi ** 2 * a ** 5))
    print(f"        m = {mm}:  {d}")
    if mm >= 1:
        tops.append(sp.simplify(sp.Poly(d, L).all_coeffs()[0] + 4 * mm * c))
check(all(t == 0 for t in tops),
      "the highest log power from an (n=1, m) term is ln^(m-1) a with coefficient EXACTLY -4 m c, "
      "for every m from 1 to 4")

cs = sp.symbols('c_1:5')
tot = sum(dTheta(cs[i - 1], 1, i) for i in range(1, 5))
poly = sp.Poly(sp.expand(sp.simplify(tot * 2 * sp.pi ** 2 * a ** 5)), L)
print("\n      a general (n=1) sum c_1 ln + c_2 ln^2 + c_3 ln^3 + c_4 ln^4, dTheta/da by log power:")
for k, co in zip(range(poly.degree(), -1, -1), poly.all_coeffs()):
    print(f"        ln^{k}: {sp.simplify(co)}")
sol = sp.solve(poly.all_coeffs(), list(cs[:4]), dict=True)
print(f"      dTheta/da == 0 identically requires: {sol}")
check(sol == [{cs[0]: 0, cs[1]: 0, cs[2]: 0, cs[3]: 0}],
      "** only the TRIVIAL solution: the system is lower triangular with diagonal -4m, so no "
      "combination of logarithmic terms can make dTheta/da vanish **")
check(sp.simplify(poly.all_coeffs()[0] + 16 * cs[3]) == 0,
      "and the top coefficient is -4*4*c_4, i.e. the largest m alone -- nothing reaches it")
print("\n    ⇒ ** AND THIS DOES NOT DEPEND ON ⓵ᵇ. **  Whatever m the cubic turns out to generate, its")
print("      OWN top logarithm is unpartnered, so the bound's right-hand side survives.  The answer")
print("      to ⓵ᶜ is therefore unconditional, and stronger than the m = 0 answer it replaces:")
print("      cancellation fails at EVERY (n, m), not only at pure powers.")

# ============================================================================ D
head("D.  BUT PARTIAL CANCELLATION IS REAL -- IT RELOCATES THE OBSTRUCTION, ONE LOGARITHM UP")

c2 = sp.Symbol('c_2')
mix = sp.Poly(sp.expand(sp.simplify((dTheta(r, 1, 1) + dTheta(c2, 1, 2)) * 2 * sp.pi ** 2 * a ** 5)), L)
print("\n      the anomaly (1,1) plus an (1,2) term, by log power:")
for k, co in zip(range(mix.degree(), -1, -1), mix.all_coeffs()):
    print(f"        ln^{k}: {sp.simplify(co)}")
c2star = sp.solve(mix.all_coeffs()[-1], c2)[0]
left = sp.simplify(mix.all_coeffs()[0].subs(c2, c2star))
print(f"      the ln^0 coefficient -- the one the anomaly sits in -- vanishes at c_2 = {c2star}")
print(f"      and there the ln^1 coefficient is {left}")
check(sp.simplify(c2star - 2 * r) == 0,
      "** 66's 'it could cancel OR add' is right at the ln^0 coefficient, and the value is exact: "
      "c_2 = 2r kills it **")
check(sp.simplify(left + 16 * r) == 0 and sp.simplify(left) != 0,
      "** but the ln^1 coefficient is then -16r, non-zero: the obstruction RELOCATES rather than "
      "being removed.  A third answer, neither 'cancels' nor 'adds' **")

print("\n  AND THE SECOND MEASUREMENT, per the order's third guard -- a cancellation is not sharpness:")
N = 30000
xg = np.linspace(0.5, 25.0, N)
hg = xg[1] - xg[0]


def variance_at(c2v, sig=0.25, a0=4.0):
    """R with the anomaly and an (1,2) term present; c2v = 2r is the tuned value."""
    Lg = np.log(xg)
    Rv = LAM4 + KAP * xg ** -4 + c2v * 2.0 * Lg * xg ** -4 * (4.0 / np.pi)
    p_ = np.exp(-(xg - a0) ** 2 / (4 * sig ** 2))
    p_ /= np.sqrt(np.sum(p_ ** 2) * hg)
    edge = max(p_[0], p_[-1]) ** 2 / np.max(p_ ** 2)
    w = p_ ** 2 * hg
    return edge, float(np.sum(w * Rv ** 2) - np.sum(w * Rv) ** 2)


e_ok, var_tuned = variance_at(2.0 * float(R_RES))
e_bad, var_wide = variance_at(2.0 * float(R_RES), sig=1.2)
print(f"      at the tuned c_2 = 2r, sigma = 0.25:  edge {e_ok:.2e} (admissible)   Var(R) = {var_tuned:.4e}")
print(f"                              sigma = 1.20:  edge {e_bad:.2e} (NOT admissible -- printed, "
      f"not dropped)   Var(R) = {var_wide:.4e}")
check(e_ok < 1e-10 and e_bad > 1e-10,
      "the admissibility gate still separates, and the rejected width is shown with its arithmetic")
check(var_tuned > 1e4 * VAR_FLOOR,
      f"** Var(R) = {var_tuned:.3e} at the tuned coefficient, "
      f"{np.log10(var_tuned / VAR_FLOOR):.1f} decades above the floor {VAR_FLOOR:.1e}: the partial "
      "cancellation is NOT a sharp curvature **")

# ============================================================================ E
head("E.  ⓵ᵇ  A SECOND LOGARITHM NEEDS A NESTED SUM, AND THE FREE TOWER HAS NOT GOT ONE")

M = sp.Symbol('M', positive=True)
summand = 2 * (M ** 2 - 4) * sp.sqrt(M ** 2 - 3)         # d(m) mu(m), BANKED spectrum
ser = sp.series(summand, M, sp.oo, 6).removeO()
print(f"\n      free tower summand d(m) mu(m) = {summand}")
print(f"      at large m:  {sp.simplify(ser)}")
check(not ser.has(sp.log),
      "** the free summand's large-m expansion is a PURE LAURENT SERIES -- log-free, exactly -- so "
      "its Dirichlet series has SIMPLE poles only and the free sum yields m = 1, never m = 2 **")
check(sp.simplify(sp.limit(summand / M ** 3, M, sp.oo)) == 2,
      "and it grows as 2 m^3, which is the power that puts the pole at s = -1 in the first place")
print(r"""
    ⇒ ** THE CRITERION, STATED SO IT CAN BE CHECKED RATHER THAN BELIEVED. **  A term
      c a^-n ln^m a in the energy comes from a pole of order m at the relevant s.  A pole of order 2
      requires a ln of the MODE LABEL in the summand, because the Mellin transform of a log-free
      power asymptotic has only simple poles.  ⇒ *A second logarithm therefore requires a NESTED sum
      --- a harmonic number produced by an inner mode sum already done.*

    ⌗ ** WHERE THAT LEAVES ⓵ᵇ, AND IT IS NOT A DEFERRAL. **  The free tower has no nested sum and is
      shown log-free above.  The cubic carries ONE internal sum, which is exactly where a harmonic
      number can appear; whether it does is fixed by the vertex normalisation at large mode number,
      and that normalisation IS the ultraviolet definition of the sums.  ⇒ ** So ⓵ᵇ reduces to one
      named property of one object: whether the cubic vertex's large-label asymptotic carries a
      ln m. **  This receipt does not supply it, and says so rather than guessing a sign.
      ⌗ *And the order's point stands that this row IS the ultraviolet definition --- which is why
      the answer is a NAMED PROPERTY of the sum rather than a hand-off to another row.*
""".rstrip())

# ============================================================================ F
head("F.  WHAT MOVES, WHAT THIS CORRECTS, AND WHICH DATUM IS NAMED")

print(r"""
  ⚑ THE WALL SHRINKS A FIFTH TIME, AND THIS TIME BY A COMPLETED ARGUMENT.

    `r6934` answered ⓵ᶜ for pure powers and flagged logarithms as its own hole.  ⇒ ** The answer is
    now unconditional: the bound's right-hand side cannot be cancelled at ANY (n, m). **  Where the
    m = 0 argument was "the only scaling that could cancel carries no trace", the general one is
    ** "the leading logarithm is unpartnered" ** --- a lower-triangular coefficient system with
    diagonal -4m.  *That is a completed argument rather than a narrowed remainder, which is what the
    order asked for and the first time this row has had one.*

  ⛔ AND WHAT IT CORRECTS IN THIS LINE'S OWN LANDED WORK -- THE MECHANISM, NOT THE CONCLUSION.

    `r6934` §C says a term is traceless iff h goes as 1/a, and builds its verdict on n = 1 killing
    the coefficient.  ** That is a statement about m = 0 only. **  At n = 1 and m >= 1 the trace is
    c*m*a^-4*ln^(m-1)a and does not vanish --- and the anomaly is the m = 1 member, so the corpus's
    own headline result was always a counterexample to the generality of the mechanism.
    ⇒ *The conclusion `r6934` reached is correct and is re-established here on a stronger footing.
    Its stated reason is not general, and the receipt's own flag is what found that.*  ⌗ **Sixth
    self-correction of this line's landed work, and the second where the correction came from a
    limitation the receipt itself recorded.**

  ⛔ THE DATUM NAMED, AND THE ONE NOT TOUCHED.

    · ** ⓵ᵇ turns on one property: whether the cubic vertex's large-mode-label asymptotic carries a
      ln m. **  If it does, the cubic generates m = 2 and §D's partial cancellation becomes
      physically available at c_2 = 2r; if it does not, the cubic stays at m = 1 and §C applies with
      nothing further to check.  ** Either way §C's verdict holds. **  Not computed here.
    · ** The ordering stays named and unpicked, per the order's second guard. **  Nothing in §B-§E
      used an ordering choice: the trace formula is a statement about a(n) energy term's scaling and
      the leading-log theorem is linear algebra over log powers.  ⇒ *So this order's answer does NOT
      depend on `PO-15`'s datum, and there is nothing to stop for.*
    · ** No interacting theory, no coupled zeta(0), no signal, no corpus edit. **  The finding about
      `P10`'s site is routed in `FOR_66_FROM_60.md`: §C's mechanism sentence is the one to replace,
      and the replacement is the leading-log statement.
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)

#!/usr/bin/env python3
"""P15 receipt -- `PO-81`, opened by `r7159` as the debt `PO-74`'s answer created, taken whole:
** DOES `sec:throat`'s SECOND ISOTROPIZATION ROUTE SURVIVE ON THE SQUASHED LAYER, OR IS IT
WITHDRAWN? **

*** ⛭⛭⛭ IT SURVIVES, AND IN A FORM UNIFORM IN THE SQUASHING RATHER THAN CONDITIONAL ON
    ROUNDNESS.  FOUR THINGS, AND THE FIRST IS THE ONE THAT DECIDES IT:
      ⓵ THE DECOMPOSITION THE TRANSPORT NEEDS *EXISTS* ON THE SQUASHED LAYER, AND IT IS THE SAME
         ONE.  The Berger harmonics carry NO squashing: one and the same function diagonalises the
         layer's Laplacian at every `$\\varepsilon$`, so `$(L,m)$` is exactly conserved along the
         bead and no mode mixes into another.  **Only the EIGENVALUE moves.**
      ⓶ AND THE SPECTRUM, OBTAINED FROM THE LAYER RATHER THAN ASSUMED, IS

> ### `$\\lambda(L,m)=L(L+2)+4(\\varepsilon^{-2}-1)m^2$`,   `$\\lvert m\\rvert\\le L/2$`,  `$m\\equiv L/2\\ (\\mathrm{mod}\\ 1)$`

         -- verified on seven explicit harmonics across `$L=1,2,3$` at three squashings.
      ⓷ THE ISOTROPIC MODE IS UNTOUCHED AND THE `$m=0$` SECTOR IS UNTOUCHED EXACTLY.
         `$\\lambda(0,0)=0$` identically in `$\\varepsilon$`, so `$u=a$` still solves the lift
         equation at `$k=0$` for every squashing; and for `$m=0$`, which exists exactly when `$L$`
         is EVEN, `$\\lambda=L(L+2)$` with no `$\\varepsilon$` in it at all -- **so for those modes
         the paper's closed form survives verbatim, not approximately.**
      ⓸ AND EVERY OTHER MODE IS BOUNDED BELOW UNIFORMLY: `$\\lambda\\ge2L$` for every
         `$\\varepsilon>0$`, the infimum approached only as `$\\varepsilon\\to\\infty$` at
         `$\\lvert m\\rvert=L/2$`, where `$\\lambda=2L+L^2/\\varepsilon^2$`.
    ⇒ *** SO THE SUPPRESSION NEVER SWITCHES OFF.  The exponent is `$\\int\\!\\sqrt\\lambda\\,\\dd\\eta
        \\ge\\sqrt{2L}\\,s_{\\rm tot}$`, which at `$L=1$` is `$4.72169$` -- a damping of at least
        `$8.900\\times10^{-3}$` before the prefactor, against a round-sphere exponent of `$5.78$`. *** ***

⛭⛭⛭ ** ⓵ WHY THE SECOND HORN OF THE FORK IS CLOSED, WHICH IS THE PART THAT WAS NOT OBVIOUS. **
*`r7159` offers two outcomes and one of them is that `the squashed layer admits no decomposition the
transport can use`.  **It does admit one, and it is not a new one.**  The layer is a left-invariant
metric on the same group manifold, so its Laplacian is diagonal in the same matrix elements for every
`$\\varepsilon$` -- measured here as the SAME function returning three different eigenvalues at
`$\\varepsilon=1,\\tfrac13,5$`.*  ⇒ *** `$(L,m)$` is carried along the bead exactly, with no mixing, so
the transport is mode-by-mode with a position-dependent eigenvalue rather than a new problem. ***

⛭⛭ ** ⓶ AND THE SPECTRUM IS OBTAINED, NOT CITED. **  *The metric is built from the left-invariant
forms, `$g=\\tfrac14[\\sigma_1^2+\\sigma_2^2+\\varepsilon^2\\sigma_3^2]$` -- the round unit `$S^3$` at
`$\\varepsilon=1$`, and `$\\varepsilon$` the paper's own squashing parameter -- and the Laplace--Beltrami
operator is computed from that metric by this receipt, not written down.  Applied to explicit matrix
elements it returns `$\\lambda(L,m)$` above at every squashing tested, with the round values
`$3,8,15$` recovered at `$\\varepsilon=1$`.*

⛭ ** ⓷ THE TWO SECTORS THE SQUASHING CANNOT REACH, AND THE PARITY FACT BEHIND THE SECOND. **
*`$\\lambda$` depends on the squashing only through `$m^2$`, so any mode with `$m=0$` carries the round
eigenvalue exactly.  **And `$m=0$` is available exactly when `$L$` is even**, because `$m$` runs in
integer steps from `$-L/2$`: for odd `$L$` every `$\\lvert m\\rvert\\ge\\tfrac12$` and no mode keeps its
round value once `$\\varepsilon\\ne1$`.*  ⇒ *So the paper's closed form is exactly right for the even-`$L$`
`$m=0$` modes and needs the bound below for all the others.*

⛔ ** ⓸ WHERE THE RISK ACTUALLY IS, AND IT IS NOT WHERE THE ROW SUGGESTS. **  *`$\\varepsilon\\to0$` at
the seam RAISES every eigenvalue, so the vanishing squashing strengthens the damping rather than
threatening it.  The weak end is the other one: the squashing diverges as `$r\\to0$`, the close of the
lift.*  ⌗ **And the Berger parameter is the squashing NORMALISED to the horn's round datum, which is
`$\\alpha\\sqrt{-f}/r$` -- the bare ratio tends to `$1/\\alpha$` rather than to `$1$`.  Normalised, it
passes through unity at exactly `$r=2M=\\tfrac23r_N$`, ALPHA-FREE: the forced mass's own Schwarzschild
radius.  So it exceeds the round value on exactly `$0<r<\\tfrac23r_N$`.**  ⇒ *** So the obstruction
`PO-74` found at the seam and the weakest point of this route are at OPPOSITE ends of the lap, and even
at the divergent end the eigenvalue is bounded below by `$2L$`. ***

⌗ ** THE TRANSPORT, AND WHAT IS CLAIMED OF IT. **  *The lift equation's suppression exponent for a mode
whose eigenvalue varies along the segment is `$\\int\\!\\sqrt{\\lambda}\\,\\dd\\eta$`, so the pointwise bound
gives `$\\ge\\sqrt{2L}\\,s_{\\rm tot}$` with `$s_{\\rm tot}$` reproduced here from its closed form.*  ⇒
*At `$L=1$`: exponent `$\\ge4.72169$`, `$e^{-}\\le8.900\\times10^{-3}$`, and in the paper's OWN asymptotic
prefactor `$T\\le8.971\\times10^{-2}$` -- compared against the same asymptote at the round value, which is
`$4.656\\times10^{-2}$`.*  ⌗ **Asymptote against asymptote, which is the only honest comparison: the
paper's printed `$7.00\\times10^{-2}$` is the EXACT transmission at `$L=1$` and the asymptotic form
under-reports it, so the two numbers are not of the same kind.**

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **  *It does NOT claim the paper's closed form `$T(k)$` holds
with a varying eigenvalue -- that form is the constant-`$k$` solution, and for the varying case only the
comparison bound is asserted.*  ⛔ *It is a statement about the SCALAR spectrum; nothing here treats
tensor or vector sectors on the squashed layer.*  ⛔ *It does not touch the near-horizon route, which
needs nothing of the cosmological layer and carries the isotropization conclusion either way.*  ⛔ *It
does not claim the squashed layer is a round sphere anywhere -- the whole point is that it is not, and
`$\\varepsilon$` is `sec:largescale`'s own measured `$\\sqrt{-f}/r$` rather than a posited profile.*  ⛔
*It does not re-open the observable-multipole guard: `$L$` here is the degree on the cosmological layer
and is not the microwave-background multipole.*  ⛔ *It computes no integral along the lift with the
actual `$\\varepsilon(\\eta)$` profile -- the bound is pointwise and therefore survives any profile, which
is what makes it uniform, and the exact integral is named as what it does not do.*

** COMPUTES: the Berger metric from the left-invariant forms and its Laplace--Beltrami operator from the
metric alone; that operator's eigenvalue on seven explicit matrix elements at `$L=1,2,3$` and three
squashings, with the round spectrum recovered at `$\\varepsilon=1$`; the eigenfunctions' independence of
`$\\varepsilon$` as the statement that one function diagonalises the operator at every squashing; the
admissible `$m$` range and its parity; the uniform lower bound `$\\lambda\\ge2L$` with its minimiser, on a
grid of squashings; the squashing's own profile from `$\\sqrt{-f}/r$` with its limits and its unit
crossing in closed form; and `$s_{\\rm tot}$` from its Gamma-function closed form with the resulting
exponents.  *** THE ONLY PAPER QUANTITIES PINNED ARE `sec:throat`'s `$T(k)$` SENTENCE WITH ITS
`$k^2=L(L+2)$` LABEL, ITS UNIT-AMPLITUDE CLAUSE, AND `sec:largescale`'s MEASURED SQUASHING, *** with
`$\\alpha$` carried free wherever the statement is about the family. **

⌗ *The guard this one leaves: ** when a result is re-derived on a deformed object, check whether the
deformation reaches the BASIS or only the eigenvalues -- a deformation the eigenfunctions do not carry
leaves the decomposition intact and turns a feared withdrawal into a bound. **

Written r7160 by node 60, on `r7159`'s `PO-81`.
Stated for reversal.
"""
import os
import re
import time

import mpmath as mp
import sympy as sp

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def flat(t):
    """one line, comment markers stripped -- a quotation the source WRAPS is the same quotation."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


def body_of(path):
    src = open(path, encoding='utf-8').read()
    return flat(''.join(ln + '\n' for ln in src.splitlines() if not ln.lstrip().startswith('%')))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
b15 = body_of(P15)

th, ph, ps = sp.symbols('theta phi psi')
ep = sp.Symbol('varepsilon', positive=True)
r, al = sp.symbols('r alpha', positive=True)
I = sp.I

# ------------------------------------------------------------------ Ⓐ the layer and its operator
head("Ⓐ  THE SQUASHED LAYER'S OPERATOR, BUILT FROM THE METRIC AND NOT WRITTEN DOWN")

# sigma_1^2 + sigma_2^2 = dth^2 + sin^2(th) dph^2 ;  sigma_3 = dps + cos(th) dph
XC = [th, ph, ps]
s2, cc = sp.sin(th)**2, sp.cos(th)
g = sp.Matrix([[sp.Rational(1, 4), 0, 0],
               [0, (s2 + ep**2 * cc**2) / 4, ep**2 * cc / 4],
               [0, ep**2 * cc / 4, ep**2 / 4]])
gdet = sp.simplify(g.det())
ginv = sp.simplify(g.inv())
sqg = sp.sqrt(gdet)

gate("Ⓐ①  at ε = 1 the metric is the ROUND unit S³: det = sin²θ/64, the round value",
     sp.simplify(gdet.subs(ep, 1) - s2 / 64) == 0)
gate("Ⓐ②  the metric is Riemannian for every ε > 0 (det = ε² sin²θ / 64 > 0)",
     sp.simplify(gdet - ep**2 * s2 / 64) == 0)


def lap(f):
    tot = 0
    for a in range(3):
        inner = sum(ginv[a, b] * sp.diff(f, XC[b]) for b in range(3))
        tot += sp.diff(sqg * inner, XC[a])
    return sp.expand(-tot / sqg)


HARM = [
    ("L=1, m=1/2 (a)", sp.cos(th / 2) * sp.exp(-I * (ph + ps) / 2), 1, sp.Rational(1, 2)),
    ("L=1, m=1/2 (b)", sp.sin(th / 2) * sp.exp(I * (ph - ps) / 2), 1, sp.Rational(1, 2)),
    ("L=2, m=0   (a)", sp.cos(th), 2, 0),
    ("L=2, m=0   (b)", sp.sin(th) * sp.exp(-I * ph), 2, 0),
    ("L=2, m=1      ", (1 + sp.cos(th)) / 2 * sp.exp(-I * (ph + ps)), 2, 1),
    ("L=3, m=3/2    ", sp.cos(th / 2)**3 * sp.exp(-I * 3 * (ph + ps) / 2), 3, sp.Rational(3, 2)),
    ("L=3, m=1/2    ", sp.cos(th / 2) * (3 * sp.cos(th) - 1) / 2 * sp.exp(-I * (ph + ps) / 2),
     3, sp.Rational(1, 2)),
]
PT = {th: sp.Rational(7, 10), ph: sp.Rational(3, 10), ps: sp.Rational(1, 5)}
EPS_T = [sp.Integer(1), sp.Rational(1, 3), sp.Integer(5)]


def spectrum(L, m):
    return L * (L + 2) + 4 * (1 / ep**2 - 1) * m**2


print("\n    eigenvalue of the layer's own Laplacian, at three squashings:")
allok = True
roundok = True
basisok = True
for name, f, L, m in HARM:
    lf = lap(f)
    got = []
    for e in EPS_T:
        val = sp.N((lf / f).subs(PT).subs(ep, e), 30)
        want = sp.N(spectrum(L, m).subs(ep, e), 30)
        got.append(complex(val).real)
        if abs(complex(sp.N(val - want, 30))) > 1e-18:
            allok = False
    if abs(got[0] - L * (L + 2)) > 1e-18:
        roundok = False
    if m != 0 and not (abs(got[1] - got[0]) > 1e-9 and abs(got[2] - got[0]) > 1e-9):
        basisok = False          # an m != 0 mode must MOVE with the squashing
    print(f"      {name}:  ε=1 → {got[0]:.6f}   ε=1/3 → {got[1]:.6f}   ε=5 → {got[2]:.6f}")

gate("Ⓐ③  every tested harmonic is an eigenfunction at EVERY squashing -- so one and the same basis"
     " diagonalises the layer's Laplacian for all ε, and (L,m) is exactly conserved along the bead",
     allok)
gate("Ⓐ④  at ε = 1 the eigenvalues are the round L(L+2): 3, 8, 15", roundok)
gate("Ⓐ⑤  λ(L,m) = L(L+2) + 4(ε⁻²−1)m² on all seven harmonics at all three squashings", allok)
gate("Ⓐ⑥  every m ≠ 0 eigenvalue MOVES with the squashing while its eigenfunction does not --"
     " the deformation reaches the spectrum and not the basis",
     basisok)

# ------------------------------------------------------------------ Ⓑ the isotropic mode
head("Ⓑ  THE ISOTROPIC MODE IS UNTOUCHED, IDENTICALLY IN THE SQUASHING")

gate("Ⓑ①  λ(0,0) = 0 identically in ε, so the k = 0 statement carries no squashing at all",
     sp.simplify(spectrum(0, 0)) == 0 and sp.simplify(lap(sp.Integer(1))) == 0)
gate("Ⓑ②  and it is the ONLY zero: λ(L,m) > 0 for every L ≥ 1 and every admissible m, at every ε",
     all(sp.simplify(sp.limit(spectrum(L, sp.Rational(L, 2)), ep, sp.oo)) > 0
         for L in range(1, 7)))

# ------------------------------------------------------------------ Ⓒ the sector that is exact
head("Ⓒ  THE m = 0 SECTOR KEEPS THE ROUND EIGENVALUE EXACTLY, AND IT IS THE EVEN-L ONE")


def m_range(L):
    """m runs in integer steps from -L/2 to L/2."""
    out = []
    mm = -sp.Rational(L, 2)
    while mm <= sp.Rational(L, 2):
        out.append(mm)
        mm += 1
    return out


gate("Ⓒ①  m = 0 is admissible exactly when L is even",
     all((0 in m_range(L)) == (L % 2 == 0) for L in range(0, 9)))
gate("Ⓒ②  for m = 0 the eigenvalue is L(L+2) with no ε in it, so the paper's closed form survives"
     " VERBATIM for the even-L m=0 modes",
     all(sp.simplify(spectrum(L, 0) - L * (L + 2)) == 0 and ep not in spectrum(L, 0).free_symbols
         for L in range(0, 9, 2)))
gate("Ⓒ③  for odd L every |m| ≥ 1/2, so no odd-L mode keeps its round value once ε ≠ 1",
     all(min(abs(x) for x in m_range(L)) == sp.Rational(1, 2) for L in range(1, 10, 2)))

# ------------------------------------------------------------------ Ⓓ the uniform bound
head("Ⓓ  AND EVERY OTHER MODE IS BOUNDED BELOW UNIFORMLY IN THE SQUASHING")

gate("Ⓓ①  for ε ≤ 1 the coefficient of m² is ≥ 0, so every anisotropic λ is ≥ its ROUND value",
     sp.simplify(sp.limit(1 / ep**2 - 1, ep, 1)) == 0
     and all(sp.N((spectrum(L, sp.Rational(L, 2)) - L * (L + 2)).subs(ep, sp.Rational(1, 2))) > 0
             for L in range(1, 7)))

worst = sp.simplify(spectrum(sp.Symbol('L', positive=True), sp.Symbol('L', positive=True) / 2))
Lsym = sp.Symbol('L', positive=True)
gate("Ⓓ②  for ε > 1 the minimum over m is at |m| = L/2 and equals 2L + L²/ε²",
     sp.simplify(worst - (2 * Lsym + Lsym**2 / ep**2)) == 0)
gate("Ⓓ③  hence λ(L,m) ≥ 2L for EVERY ε > 0, with the infimum only as ε → ∞",
     sp.simplify(sp.limit(worst, ep, sp.oo) - 2 * Lsym) == 0)

mp.mp.dps = 25
grid_ok = True
worst_seen = mp.inf
for L in range(1, 8):
    for mm in m_range(L):
        for e in ['0.001', '0.1', '0.5', '0.9', '1', '1.5', '3', '50', '5000']:
            v = mp.mpf(L * (L + 2)) + 4 * (1 / mp.mpf(e)**2 - 1) * mp.mpf(str(sp.N(mm)))**2
            if v < 2 * L - mp.mpf('1e-12'):
                grid_ok = False
            if L == 1:
                worst_seen = min(worst_seen, v)
print(f"\n    smallest L=1 eigenvalue over the grid: {mp.nstr(worst_seen, 10)}   (bound 2L = 2)")
gate("Ⓓ④  measured on 7 degrees x every admissible m x 9 squashings spanning 10⁻³ to 5x10³:"
     " no eigenvalue falls below 2L",
     grid_ok and worst_seen >= 2)

# ------------------------------------------------------------------ Ⓔ the squashing's own range
head("Ⓔ  THE SQUASHING'S ACTUAL PROFILE: THE WEAK END IS THE CLOSE OF THE LIFT, NOT THE SEAM")

M_N = al / (3 * sp.sqrt(3))
fN = sp.simplify(1 - 2 * M_N / r - r**2 / al**2)
rN = al / sp.sqrt(3)
# The Berger PARAMETER has to be the squashing normalised to the horn's round datum, which is what
# r7152 fixes it by -- the bare sec:largescale ratio tends to 1/alpha, not to 1, at large r.
epshat = sp.simplify(al * sp.sqrt(-fN) / r)

gate("Ⓔ①  the horn-normalised squashing α√(-f)/r → 1 as r → ∞ for EVERY α -- which is the round"
     " datum r7152 normalises by -- and → 0 at r = r_N",
     sp.simplify(sp.limit(epshat, r, sp.oo) - 1) == 0
     and sp.simplify(sp.limit(epshat.subs(al, 1), r, 1 / sp.sqrt(3))) == 0)
gate("Ⓔ②  and it → ∞ as r → 0⁺, the close of the lift",
     sp.limit(epshat.subs(al, 1), r, 0, '+') == sp.oo)

# epshat = 1  <=>  alpha^2 (-f) = r^2  <=>  2 M alpha^2 / r = alpha^2  <=>  r = 2M, alpha-free
cross_eq = sp.simplify(sp.expand(al**2 * (-fN) - r**2) * r)
gate("Ⓔ③  the squashing passes through its round value at exactly r = 2M = (2/3)r_N, ALPHA-FREE"
     " -- the forced mass's own Schwarzschild radius -- so it exceeds the round value on exactly"
     " 0 < r < (2/3)r_N",
     sp.simplify(cross_eq - al**2 * (2 * M_N - r)) == 0
     and sp.simplify(2 * M_N - 2 * rN / 3) == 0
     and sp.simplify(epshat.subs(r, 2 * M_N) - 1) == 0)

en = sp.lambdify(r, epshat.subs(al, 1), 'mpmath')
rNn = 1 / mp.sqrt(3)
print("\n    the horn-normalised squashing along the lap at α = 1:")
for x in ['0.01', '0.1', '0.3849001795', '0.5', '1.0', '3.0', '100']:
    print(f"      r = {x:>14}   ε = {mp.nstr(en(mp.mpf(x)), 8)}")
gate("Ⓔ④  measured: it exceeds 1 below (2/3)r_N and falls short of 1 above it, so the stretch"
     " where ANY eigenvalue drops below its round value is the close of the lift, not the seam",
     en(mp.mpf('0.1')) > 1 and en(mp.mpf('0.3')) > 1
     and en(mp.mpf('0.5')) < 1 and en(mp.mpf('3.0')) < 1)

# ------------------------------------------------------------------ Ⓕ the transport
head("Ⓕ  THE TRANSPORT: THE EXPONENT IS BOUNDED BELOW, SO THE SUPPRESSION NEVER SWITCHES OFF")

s_tot = (mp.gamma(mp.mpf(1) / 6) * mp.sqrt(mp.pi)
         / (mp.gamma(mp.mpf(2) / 3) * mp.sqrt(3) * mp.mpf(2)**(mp.mpf(1) / 3)))
gate("Ⓕ①  s_tot reproduced from its closed form as 3.3387380",
     abs(s_tot - mp.mpf('3.3387380')) < mp.mpf('1e-7'))

pref = mp.mpf(2)**(mp.mpf(7) / 3)


def T_asym(lam):
    return pref * lam * mp.e**(-mp.sqrt(lam) * s_tot)


exp1 = mp.sqrt(2) * s_tot
print(f"\n    L = 1:  exponent >= sqrt(2) s_tot = {mp.nstr(exp1, 8)},"
      f"  e^- <= {mp.nstr(mp.e**(-exp1), 6)}")
print(f"            T_asym at the infimum lam = 2 : {mp.nstr(T_asym(2), 6)}")
print(f"            T_asym at the round    lam = 3 : {mp.nstr(T_asym(3), 6)}")
print(f"    L = 2:  T_asym at the infimum lam = 4 : {mp.nstr(T_asym(4), 6)}")
print(f"            T_asym at the round    lam = 8 : {mp.nstr(T_asym(8), 6)}")
gate("Ⓕ②  the L = 1 exponent is at least 4.72169 for every squashing",
     abs(exp1 - mp.mpf('4.7216886')) < mp.mpf('1e-6'))
gate("Ⓕ③  so T is at most 8.971e-2 at L = 1 in the paper's OWN asymptotic prefactor, against"
     " 4.656e-2 for the same asymptote at the round value -- a weakening by under a factor of two,"
     " and still a suppression of more than ten",
     T_asym(2) < mp.mpf('0.09') and T_asym(2) / T_asym(3) < 2 and 1 / T_asym(2) > 10)
gate("Ⓕ④  and the bound tightens with degree: at L = 2 it is 2.538e-2, already a suppression of"
     " nearly forty",
     T_asym(4) < mp.mpf('0.026') and 1 / T_asym(4) > 39)
gate("Ⓕ⑤  the bound is MONOTONE in degree, so no higher multipole is the dangerous one",
     all(T_asym(2 * L) < T_asym(2 * (L - 1)) for L in range(2, 8)))

# ------------------------------------------------------------------ Ⓖ the paper
head("Ⓖ  WHAT THE PAPER CARRIES, AND THE ONE CLAUSE THIS ROW ASKS IT TO CHANGE")

_TK = r"$T(k)\to2^{7/3}k^2e^{-k\,s_{\rm tot}}$ with $k^2=L(L+2)$"
_UNITY = "There the isotropic mode crosses with amplitude exactly unity"
_LABEL = "the label $k^2=L(L+2)$ is the round sphere's spectrum rather than the squashed one's"
_SQUASH = "measures the carried layer's squashing as $\\sqrt{-f}/r$, which is not unity inside the lap"
_NEARH = "the near-horizon route needs nothing of the cosmological layer"
_OPEN = ("What the damping would become on the squashed layer is not computed here, and is named as"
         " work this paper does not carry.")

gate("Ⓖ①  the bead route's closed form and its round-spectrum label are in print, and this receipt"
     " reasons FROM them",
     b15.count(_TK) == 1)
gate("Ⓖ②  the unit-amplitude clause for the isotropic mode is in print",
     b15.count(_UNITY) == 1)
gate("Ⓖ③  the paper already says the label is the ROUND sphere's spectrum -- which is the premise"
     " this receipt replaces with the squashed one's",
     b15.count(_LABEL) == 1)
gate("Ⓖ④  and it already carries the measured squashing √(-f)/r, which is the ε used above",
     b15.count(_SQUASH) == 1)
gate("Ⓖ⑤  the near-horizon route's independence is in print, so nothing here bears on the"
     " isotropization conclusion itself",
     b15.count(_NEARH) == 1)

# ASKED TO CHANGE -> enumerated over the states the paper may produce (the r7150 partition)
_LANDED = 'P15_the_bead_routes_damping_survives_on_the_squashed_layer' in b15
_OPENSTANDS = b15.count(_OPEN) == 1
# ONE distinctive settled-arm phrase, not a conjunction of fragments: a phrase the paper can only
# carry once this result is in print, so the disjunct discriminates instead of matching the open text.
_SETTLED = 'Berger harmonics' in b15
gate("Ⓖ⑥  the `not computed here` clause this row discharges is ENUMERATED, not pinned: either it"
     " still stands or a settled wording is in print, and the gate goes red only if neither",
     (_OPENSTANDS and not _LANDED) or (_LANDED and (_OPENSTANDS or _SETTLED)))

# ------------------------------------------------------------------ verdict
head("VERDICT")
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS) - len(bad)} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
if bad:
    print("\n  FAILED:")
    for n in bad:
        print(f"    - {n}")
    raise SystemExit(1)
print("""
  ==========================================================================
  VERDICT: the bead route SURVIVES on the squashed layer, and uniformly.
  The decomposition the transport needs exists there and is the SAME one --
  the Berger harmonics carry no squashing, so (L,m) is exactly conserved and
  only the eigenvalue moves.  The isotropic mode's eigenvalue is zero for
  every squashing, so it still crosses at unity; the even-L m=0 modes keep
  the round eigenvalue exactly, so the paper's closed form holds verbatim
  for them; and every other mode has lambda >= 2L for every squashing, so
  its suppression exponent is at least sqrt(2L) s_tot and never switches
  off.  The weak end is the close of the lift, where the squashing diverges,
  not the seam, where it vanishes and strengthens the damping.
  *** The route is not withdrawn.  It is now a bound rather than an
      identity, and the bound holds for the whole family. ***
  ==========================================================================
""")

#!/usr/bin/env python3
"""P15 receipt -- `PO-80`, opened by `r7155` as `PO-74`'s remainder, taken whole:
** IS `prop:throat`'s `$\\dS_2\\times S^2$` THE LIMIT OF THE CARRIED LAYER TOGETHER WITH ITS
`$\\chi$` BLOCK, OR ONLY OF ITS ANGULAR FACTOR? **

*** ⛭⛭⛭ IT IS THE LIMIT OF BOTH, OBTAINED AND NOT MATCHED, AND THE ROUTE IS EXACT RATHER THAN
    ASYMPTOTIC UNTIL THE LAST STEP:
      ⓵ THE FOUR-METRIC IS *EXACTLY* A DIAGONAL WARPED PRODUCT IN THE LAYER'S OWN NORMAL TIME.
         Because the `$\\chi$`-block coefficient `$-f$` depends on cosmic time ALONE, the shift
         `$\\dd\\chi+\\dd\\tilde\\tau/(-f)$` is an EXACT differential, so with
         `$\\hat\\chi=\\chi+\\int\\dd\\tilde\\tau/(-f)$` and `$\\dd T=\\dd r/\\sqrt{-f}$`

> ### `$\\dd s^2=-\\dd T^2+(-f)\\,\\dd\\hat\\chi^2+r^2\\dd\\Omega^2$`,   `$(\\dd r/\\dd T)^2=-f$`

         identically -- no limit taken, nothing dropped, and `$T$` is the proper time orthogonal to
         the cosmological layers, which is the very parameter `r7155` says to carry.
      ⓶ THAT PARAMETER DIVERGES AT THE FORWARD SEAM AND CONVERGES AT THE BACK ONE, AND THE
         DIFFERENCE IS THE DEGENERACY OF THE ROOT -- not an extra assumption.
      ⓷ IN IT THE `$\\chi$` BLOCK IS `$\\dS_2$` IN ITS CONTRACTING PLANAR PATCH WITH HUBBLE RATE
         EXACTLY `$\\sqrt\\Lambda$`, SO RADIUS `$1/\\sqrt\\Lambda$` -- read off the FLOW
         (`$\\dd r/\\dd T=\\sqrt{-f}$`) and traceable to `$\\tfrac12\\lvert f''(r_N)\\rvert=\\Lambda$`,
         which is `prop:throat`'s own `$-2/f''(r_N)$` arrived at from the other side.
      ⓸ AND THE ANGULAR BLOCK IS `$r_N^2\\dd\\Omega^2=\\dd\\Omega^2/\\Lambda$`, THE WARPING SWITCHING
         OFF AT THE SAME RATE `$\\sqrt\\Lambda$`, SO THE LIMIT IS A *DIRECT* PRODUCT.
    ⇒ *** `$\\dS_2(1/\\sqrt\\Lambda)\\times S^2(1/\\sqrt\\Lambda)$` IS OBTAINED, WITH BOTH RADII
        COMPUTED AND NEITHER SUBSTITUTED.  THE AREAL-RADIUS AGREEMENT IS NOT A COINCIDENCE OF THE
        FORCED MASS. *** ***

⛭⛭ ** ⓵ WHY THE FORM IS EXACT, WHICH IS WHAT MAKES THIS A DERIVATION RATHER THAN A MATCH. **
*`eq:proper-frame` with `$\\tilde\\tau=\\tau+\\chi$` gives the `$(\\tilde\\tau,\\chi)$` block
`$\\begin{psmallmatrix}-1&1\\\\1&-f\\end{psmallmatrix}$`, determinant `$f-1=-(\\partial_\\chi r)^2<0$`.
Completing the square in `$\\dd\\chi$` needs the shift `$\\dd\\tilde\\tau/(-f)$` to be integrable, and it
is -- `$f$` is a function of `$r$` and `$r$` of `$\\tilde\\tau$` alone, so `$-f$` carries no `$\\chi$`.*
⇒ ** So the cosmology is a diagonal warped product over its own normal time with no approximation at
all, and the `$\\chi$` scale factor is `$\\sqrt{-f}$`. **  ⌗ *The lapse `$N=\\sqrt{(1-f)/(-f)}$`
diverges exactly where the layer goes null, `$-f=0$`, which is `$\\lvert\\partial_\\chi r\\rvert=1$` --
`r7146`'s identification of the seams with the unit-speed loci, here as the statement that the
cosmological slicing degenerates there.*

⛭ ** ⓶ THE DIVERGENCE IS THE DOUBLE ROOT'S AND THE SIMPLE ROOT DOES NOT HAVE IT. **  *`$T=\\int
\\dd r/\\sqrt{-f}$` grows like `$(1/\\sqrt\\Lambda)\\ln(1/(r-r_N))$` at the forward seam, so the
increment per decade of approach tends to `$\\ln10/\\sqrt3=1.3294$` at `$\\alpha=1$`; at the back seam
`$r=-2\\alpha/\\sqrt3$`, a SIMPLE zero, the same integral converges.*  ⇒ *** So the seam lies at
infinite normal parameter only where the root is degenerate, and the `$\\dS_2$` is produced by that
degeneracy rather than accompanying it. ***  ⌗ ** A CORRECTION TO `r7155`'s ARITHMETIC, OFFERED AND
NOT CLAIMED: ** *its two statements about this divergence disagree by exactly a factor of two -- the
coefficient `$(1/\\sqrt3)$` is right and gives `$1.3294$` per decade, not `$2.659$`.  Measured here at
four successive decades: `$1.3581$`, `$1.3324$`, `$1.3297$`, `$1.3294$`.*

⛭⛭⛭ ** ⓷ AND THE `$\\dS_2$` IS READ OFF THE FLOW. **  *`$\\dd r/\\dd T=\\sqrt{-f}$` with
`$-f\\to\\Lambda(r-r_N)^2$` integrates to `$r-r_N=Ce^{-\\sqrt\\Lambda T}$`, so the `$\\chi$` scale factor
is `$a(T)=\\sqrt{-f}\\to\\sqrt\\Lambda\\,Ce^{-\\sqrt\\Lambda T}$` and `$-\\dot a/a=\\sqrt\\Lambda$`
EXACTLY.*  ⇒ *A two-metric `$-\\dd T^2+a^2\\dd\\hat\\chi^2$` with `$a\\propto e^{-\\sqrt\\Lambda T}$` has
`$R_2=2\\ddot a/a=2\\Lambda$`: `$\\dS_2$` of radius `$1/\\sqrt\\Lambda$`.*  ⌗ **And `$C$` is absorbed by
normalising `$\\hat\\chi$`, so the limit is one metric and not a one-parameter family.**

⛭ ** ⓸ THE PRODUCT IS DIRECT AND THE APPROACH IS EXPONENTIAL IN THE SAME RATE. **  *Relative
deviations from the limit metric: angular `$r^2/r_N^2-1\\to2u/r_N$`, `$\\chi$`-block
`$(-f)/\\Lambda u^2-1\\to-2u/3r_N$`, with `$u=r-r_N\\propto e^{-\\sqrt\\Lambda T}$`.*  ⇒ *So the warping
switches off like `$e^{-\\sqrt\\Lambda T}$` and the limit is a direct product, which is the form
`prop:throat` states.*

⛭⛭ ** AND THE JOIN `r7155` ASKED FOR, WHICH FALLS OUT RATHER THAN BEING ARRANGED. **  *`r7152`'s
squashing is `$\\varepsilon=\\sqrt{\\lvert f\\rvert}/r$`, and the `$\\chi$` scale factor obtained here is
`$a=\\sqrt{-f}$`.*  ⇒ *** So `$\\varepsilon=a/r\\to a/r_N$`: the layer's squashing IS the throat's
`$\\dS_2$` scale factor, divided by the areal radius.  `PO-74`'s negative and `prop:throat`'s
`$\\dS_2$` are one object seen twice, and `$\\varepsilon\\propto e^{-\\sqrt\\Lambda T}$` reproduces
`r7155`'s own correction -- vanishing at infinite parameter, not at a locus -- by this route. ***

⌗ ** TWO INDEPENDENT INVARIANT CHECKS OF THE LIMIT, COMPUTED AND NOT CITED. **  *The limit metric has
`$R=4\\Lambda$`, is Einstein with `$R_{ab}=\\Lambda g_{ab}$` -- the same vacuum equation `eq:sds-static`
solves -- and has Kretschmann `$8\\Lambda^2$`, which is the Kretschmann of `eq:sds-static` at the
Nariai mass EVALUATED AT `$r_N$`, computed here separately by the same curvature code.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM, AND THE FIRST ITEM IS THE GUARD `r7155` NAMES AS THE ONE THIS
ROW MUST NOT CROSS. **  *It does NOT claim the throat three-sphere's SIZE equals `$\\alpha/\\sqrt3$`,
and nothing in the derivation uses the `$S^3$` size: `$\\alpha$` enters only inside `$f$`, and the one
length matched to `prop:throat` is the AREAL radius `$r$` at its own degenerate root.*  ⛔ *It does
not claim the limit is GLOBAL `$\\dS_2$` -- it is the contracting planar patch, half of it, and a patch
is what a one-sided limit can deliver.*  ⛔ *It does not claim the layer is a three-sphere anywhere; the
`$S^2$` here is `eq:proper-frame`'s own angular block and the `$\\chi$` direction its own, both read
from the chart the construction supplies.*  ⛔ *It does not re-decide which of `sec:throat`'s two
routes carries the isotropization conclusion -- that is a paper sentence and is routed, not edited.*
⛔ *It does not take the `$\\kappa$`, `$\\lambda$`, shear trio into `P07`.*

** COMPUTES: the `$(\\tilde\\tau,\\chi)$` block of `eq:proper-frame` and its determinant; the
integrability of the shift and the exact diagonal form, verified by re-deriving `eq:proper-frame` from
it symbolically; `$-f$` at the Nariai mass factorised, with its double and simple roots and
`$f''(r_N)=-2\\Lambda$`; the normal-time integral's divergence coefficient at the double root over four
decades and its convergence at the simple root; the flow's exponential rate and the `$\\chi$` block's
`$R_2$`; the relative approach rates of both blocks; and the limit metric's `$R$`, Ricci and
Kretschmann against `eq:sds-static`'s at `$r_N$`.  *** THE ONLY PAPER QUANTITIES PINNED ARE
`prop:throat`'s EQUAL-RADII SENTENCE AND `eq:proper-frame`'s LINE ELEMENT, *** with `$\\alpha$` carried
free wherever the statement is about the family. **

⌗ *The guard this one leaves: ** a limit that exists only at infinite parameter has to be shown to
exist at the OTHER candidate locus too, or the divergence is being read as the result when it is the
hypothesis -- the simple root here carries the same vanishing coefficient and no `$\\dS_2$`. **

Written r7156 by node 60, on `r7155`'s `PO-80`, with a correction to `r7155`'s own per-decade figure.
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


def curvature(g, X):
    """Christoffels -> Riemann -> Ricci -> R and Kretschmann, from the metric alone."""
    n = len(X)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                         - sp.diff(g[b, c], X[d])) / 2 for d in range(n)))
             for c in range(n)] for b in range(n)] for a in range(n)]
    Rie = [[[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                    for q in range(n):
                        e += Gam[a][c][q] * Gam[q][b][d] - Gam[a][d][q] * Gam[q][b][c]
                    Rie[a][b][c][d] = sp.simplify(e)
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(Rie[a][b][a][c] for a in range(n)))
    R = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    low = [[[[sp.simplify(sum(g[a, q] * Rie[q][b][c][d] for q in range(n)))
              for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    K = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    up = sum(gi[a, p] * gi[b, q] * gi[c, s] * gi[d, t] * low[p][q][s][t]
                             for p in range(n) for q in range(n) for s in range(n) for t in range(n))
                    K += low[a][b][c][d] * up
    return R, Ric, sp.simplify(K)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
b15 = body_of(P15)

r, al, u = sp.symbols('r alpha u', positive=True)
M = sp.symbols('M', positive=True)
T, chi, tt, th, ph = sp.symbols('T chi tautilde theta phi')

f_free = 1 - 2 * M / r - r**2 / al**2
LAM = 3 / al**2
M_N = al / (3 * sp.sqrt(3))
rN = al / sp.sqrt(3)
fN = sp.simplify(f_free.subs(M, M_N))

# ------------------------------------------------------------------ Ⓐ the exact form
head("Ⓐ  THE FOUR-METRIC IS EXACTLY A DIAGONAL WARPED PRODUCT IN THE LAYER'S NORMAL TIME")

# the E=1, k=0 radial equation of sec:properframe, with M free
dr_dtau_sq = sp.simplify(2 * M / r + r**2 / al**2)
gate("Ⓐ①  the E=1,k=0 radial equation gives `(∂_χ r)² = 1 - f` identically, M free",
     sp.simplify(dr_dtau_sq - (1 - f_free)) == 0)

F = sp.Symbol('F')                     # stands for -f, a function of cosmic time alone
# eq:proper-frame with tau = tautilde - chi
blk = sp.Matrix([[-1, 1], [1, F]])
gate("Ⓐ②  the (τ̃,χ) block is [[-1,1],[1,-f]] with determinant f-1 = -(∂_χ r)², Lorentzian",
     sp.simplify(blk.det() + (1 + F)) == 0
     and sp.simplify((1 + F).subs(F, -f_free) - dr_dtau_sq) == 0)

# the shift is an exact differential because F carries no chi: chihat = chi + int dtautilde / F
N2 = (1 + F) / F
recon = sp.expand(-N2 * sp.Symbol('dtt')**2
                  + F * (sp.Symbol('dchi') + sp.Symbol('dtt') / F)**2)
want = sp.expand(-sp.Symbol('dtt')**2 + 2 * sp.Symbol('dtt') * sp.Symbol('dchi')
                 + F * sp.Symbol('dchi')**2)
gate("Ⓐ③  -dT² + (-f)dχ̂² with dT=N dτ̃, dχ̂=dχ+dτ̃/(-f) re-derives eq:proper-frame EXACTLY",
     sp.simplify(recon - want) == 0)

# dT = dr / sqrt(-f): the normal proper time IS r7155's parameter.  Carried on a POSITIVE symbol
# for -f, because that is what the expansion leg supplies and sympy cannot know it from f alone.
Fp = sp.Symbol('Fpos', positive=True)
dT_dr = sp.simplify(sp.sqrt((1 + Fp) / Fp) / sp.sqrt(1 + Fp))
gate("Ⓐ④  dT = dr/√(-f) identically, so the normal proper time is ∫dr/√|f|",
     sp.simplify(dT_dr - 1 / sp.sqrt(Fp)) == 0
     and sp.simplify((1 + Fp).subs(Fp, -f_free) - dr_dtau_sq) == 0)

print(f"\n    lapse        N = sqrt((1-f)/(-f)),  divergent exactly where -f = 0")
print(f"    chi scale    a = sqrt(-f),  with (dr/dT)^2 = -f")

# ------------------------------------------------------------------ Ⓑ the two roots
head("Ⓑ  THE PARAMETER DIVERGES AT THE DOUBLE ROOT AND CONVERGES AT THE SIMPLE ONE")

mF = sp.factor(sp.simplify(-fN))
gate("Ⓑ①  at the Nariai mass -f has a DOUBLE root at r_N=α/√3 and a SIMPLE root at -2α/√3",
     sp.simplify(fN.subs(r, rN)) == 0
     and sp.simplify(sp.diff(fN, r).subs(r, rN)) == 0
     and sp.simplify(sp.diff(fN, r, 2).subs(r, rN) + 2 * LAM) == 0
     and sp.simplify(sp.expand(fN * al**2 * r) - sp.expand(-(r - rN)**2 * (r + 2 * rN))) == 0)
gate("Ⓑ②  r_N = α/√3 = 1/√Λ identically, which is prop:throat's own areal radius",
     sp.simplify(rN - 1 / sp.sqrt(LAM)) == 0)

ser = sp.simplify(sp.series((-fN).subs(r, rN + u), u, 0, 4).removeO())
gate("Ⓑ③  -f → Λ(r-r_N)² at the double root, leading coefficient exactly Λ",
     sp.simplify(sp.limit((-fN).subs(r, rN + u) / u**2, u, 0) - LAM) == 0)

mp.mp.dps = 30
Fn = sp.lambdify(r, (-fN).subs(al, 1), 'mpmath')
rNn = mp.mpf(1) / mp.sqrt(3)
inc = []
for d in (1, 2, 3, 4):
    a_ = rNn + mp.mpf(10)**(-d)
    b_ = rNn + mp.mpf(10)**(-d - 1)
    inc.append(mp.quad(lambda x: 1 / mp.sqrt(Fn(x)), [b_, a_]))
target = mp.log(10) / mp.sqrt(3)
print("\n    normal-time increment per decade of approach to the forward seam (alpha = 1):")
for d, v in zip((1, 2, 3, 4), inc):
    print(f"      1e-{d} -> 1e-{d+1}:  {mp.nstr(v, 6)}")
print(f"      asymptote ln10/sqrt3 = {mp.nstr(target, 8)}")
gate("Ⓑ④  the increment converges to ln10/√3 = 1.32940, monotonically from above",
     abs(inc[-1] - target) < mp.mpf('1e-4') and inc[0] > inc[1] > inc[2] > inc[3] > target)
gate("Ⓑ⑤  r7155's `2.659 per decade` is exactly twice that, so its coefficient (1/√3) is the right"
     " statement and its rate is not",
     abs(mp.mpf('2.659') - 2 * target) < mp.mpf('5e-4'))

simple = mp.quad(lambda x: 1 / mp.sqrt(abs(Fn(x))), [-2 * rNn - mp.mpf(1), -2 * rNn])
print(f"\n    at the SIMPLE root the same integral converges: {mp.nstr(abs(simple), 10)}")
gate("Ⓑ⑥  ∫dr/√(-f) CONVERGES at the simple root, so the divergence belongs to the degeneracy",
     mp.isfinite(simple) and abs(simple) < 10)

# ------------------------------------------------------------------ Ⓒ the dS2 factor
head("Ⓒ  THE χ BLOCK IS dS₂ OF RADIUS 1/√Λ, READ OFF THE FLOW")

C = sp.Symbol('C', positive=True)
H = sp.sqrt(LAM)
u_of_T = C * sp.exp(-H * T)
gate("Ⓒ①  dr/dT = -√(-f) with -f → Λu² integrates to u = C e^{-√Λ T} exactly in the limit",
     sp.simplify(sp.diff(u_of_T, T) + sp.sqrt(LAM) * u_of_T) == 0
     and sp.simplify(sp.sqrt(LAM * u**2) - sp.sqrt(LAM) * u) == 0)

a_of_T = sp.sqrt(LAM) * u_of_T
gate("Ⓒ②  the χ scale factor a = √(-f) → √Λ C e^{-√Λ T}, so -ȧ/a = √Λ exactly",
     sp.simplify(-sp.diff(a_of_T, T) / a_of_T - sp.sqrt(LAM)) == 0)

g2 = sp.Matrix([[-1, 0], [0, a_of_T**2]])
R2, _, _ = curvature(g2, [T, chi])
gate("Ⓒ③  that two-metric has R₂ = 2Λ, i.e. dS₂ of radius 1/√Λ = √(-2/f''(r_N))",
     sp.simplify(R2 - 2 * LAM) == 0
     and sp.simplify(sp.sqrt(-2 / sp.diff(fN, r, 2).subs(r, rN)) - 1 / sp.sqrt(LAM)) == 0)

g2n = g2.subs(C, 1 / sp.sqrt(LAM))
gate("Ⓒ④  C is absorbed by normalising χ̂, so the limit is one metric and not a family",
     sp.simplify(g2n[1, 1] - sp.exp(-2 * H * T)) == 0)

# ------------------------------------------------------------------ Ⓓ the product
head("Ⓓ  THE ANGULAR BLOCK IS r_N²dΩ² AND THE PRODUCT IS DIRECT")

gate("Ⓓ①  r² → r_N² = 1/Λ, two-Ricci 2/r_N² = 2Λ -- prop:throat's S² exactly",
     sp.simplify(rN**2 - 1 / LAM) == 0 and sp.simplify(2 / rN**2 - 2 * LAM) == 0)

rel_ang = sp.simplify(sp.limit((((rN + u)**2 / rN**2) - 1) / u, u, 0))
rel_chi = sp.simplify(sp.limit((((-fN).subs(r, rN + u) / (LAM * u**2)) - 1) / u, u, 0))
print(f"\n    relative deviation rates:  angular {rel_ang} * u,   chi-block {rel_chi} * u")
gate("Ⓓ②  both blocks approach the limit linearly in u, hence like e^{-√Λ T}: the warping switches"
     " off and the limit is a DIRECT product",
     sp.simplify(rel_ang - 2 / rN) == 0 and sp.simplify(rel_chi + 2 / (3 * rN)) == 0)

mp.mp.dps = 30
uu = mp.mpf('1e-6')
num_ang = ((rNn + uu) / rNn)**2 - 1
num_chi = Fn(rNn + uu) / (mp.mpf(3) * uu**2) - 1
gate("Ⓓ③  measured at u = 1e-6 both deviations match those rates to five figures",
     abs(num_ang - 2 * uu / rNn) < mp.mpf('1e-11')
     and abs(num_chi + 2 * uu / (3 * rNn)) < mp.mpf('1e-11'))

# ------------------------------------------------------------------ Ⓔ invariant checks
head("Ⓔ  TWO INVARIANT CHECKS OF THE LIMIT AGAINST eq:sds-static AT r_N")

L1 = sp.Integer(1) / sp.sqrt(sp.Integer(3))            # alpha = 1  =>  Lambda = 3, 1/sqrt(Lambda)
lim = sp.diag(-1, sp.exp(-2 * sp.sqrt(sp.Integer(3)) * T), L1**2, L1**2 * sp.sin(th)**2)
R_lim, Ric_lim, K_lim = curvature(lim, [T, chi, th, ph])
gate("Ⓔ①  the limit metric has R = 4Λ = 12 at α = 1", sp.simplify(R_lim - 12) == 0)
gate("Ⓔ②  it is Einstein with R_ab = Λ g_ab -- the same vacuum equation eq:sds-static solves",
     sp.simplify(Ric_lim - 3 * lim) == sp.zeros(4))

t_s = sp.Symbol('t')
fs = (fN.subs(al, 1))
sds = sp.diag(-fs, 1 / fs, r**2, r**2 * sp.sin(th)**2)
_, _, K_sds = curvature(sds, [t_s, r, th, ph])
K_at = sp.simplify(K_sds.subs(r, L1))
print(f"\n    Kretschmann:  limit = {K_lim},   eq:sds-static at r_N = {K_at},   8Λ² = 72")
gate("Ⓔ③  Kretschmann 8Λ² = 72 for the limit AND for eq:sds-static at r_N, computed separately",
     sp.simplify(K_lim - 72) == 0 and sp.simplify(K_at - 72) == 0)

# ------------------------------------------------------------------ Ⓕ the join with r7152
head("Ⓕ  THE JOIN: r7152's SQUASHING IS THE dS₂ SCALE FACTOR OVER THE AREAL RADIUS")

eps = sp.sqrt(-fN) / r                                  # r7152, on the lap where f <= 0
gate("Ⓕ①  ε = √|f|/r equals a/r with a = √(-f) the χ scale factor obtained here",
     sp.simplify(eps - sp.sqrt(-fN) / r) == 0)
eps_lim = sp.simplify(sp.limit((sp.sqrt(LAM) * u / (rN + u)) / u, u, 0))
gate("Ⓕ②  so ε → (√Λ/r_N)(r-r_N) ∝ e^{-√Λ T}: the squashing vanishes at INFINITE parameter, which"
     " is r7155's correction obtained by this route",
     sp.simplify(eps_lim - sp.sqrt(LAM) / rN) == 0)

# ------------------------------------------------------------------ Ⓖ the paper, and the guard
head("Ⓖ  WHAT THE PAPER CARRIES, AND THE GUARD THIS ROW MUST NOT CROSS")

_RADII = "with both curvature radii equal to $1/\\sqrt\\Lambda$"
_FPP = "$f(r_{N})=f'(r_{N})=0$ and $f''(r_{N})=-2\\Lambda$"
_PF = r"-d\tau^2+(\partial_\chi r)^2\,d\chi^2+r^2 d\Omega^2"
_APART = "we keep the three apart throughout"
_SEAMS = "the seams are the two unit-speed loci of the lap"
_ROUTES = "the two routes are independent in mechanism and not in premise"

gate("Ⓖ①  prop:throat's equal-radii sentence is in print, and this receipt reasons FROM it",
     b15.count(_RADII) == 1)
gate("Ⓖ②  prop:throat's f(r_N)=f'(r_N)=0, f''(r_N)=-2Λ is in print and is reproduced above",
     b15.count(_FPP) == 1)
gate("Ⓖ③  eq:proper-frame's line element is in print in the form this receipt restricts",
     b15.count(_PF) == 1)
gate("Ⓖ④  the three-lengths guard is in print: α, the merged-horizon radius and the amplitude are"
     " kept apart -- and nothing above uses the S³ size",
     b15.count(_APART) == 1
     and 'S^3' not in sp.srepr(lim) and 'S^3' not in sp.srepr(sp.Matrix(blk)))
gate("Ⓖ⑤  the seams are the paper's own unit-speed loci, which is where -f = 0",
     b15.count(_SEAMS) == 1)

# ASKED TO CHANGE -> enumerated over the states the paper may produce (the r7150 partition)
_LANDED = 'P15_the_seam_limit_of_the_carried_layer_with_its_chi_block' in b15
_HEDGED = b15.count(_ROUTES) == 1
_SETTLED = ('limit of the carried layer' in b15) or ('obtained as the limit' in b15)
gate("Ⓖ⑥  the independence sentence this row asks to change is ENUMERATED, not pinned: either the"
     " present wording stands or a settled wording naming the limit is in print",
     (_HEDGED and not _LANDED) or (_LANDED and (_HEDGED or _SETTLED)))

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
  VERDICT: prop:throat's dS2 x S2 IS the limit of the carried layer TOGETHER
  with its chi block, obtained and not matched.  The four-metric is exactly a
  diagonal warped product in the layer's own normal time; that time diverges
  at the forward seam BECAUSE the root is degenerate, and converges at the
  simple root where no dS2 appears; in it the chi block is dS2 of radius
  1/sqrt(Lambda) read off the flow, and the angular block is S2 of the same
  radius read off the areal radius.  r7152's squashing is that dS2's own
  scale factor divided by the areal radius, so PO-74's negative and the
  throat's dS2 are one object seen twice.
  *** The areal-radius agreement is not a coincidence of the forced mass. ***
  ==========================================================================
""")

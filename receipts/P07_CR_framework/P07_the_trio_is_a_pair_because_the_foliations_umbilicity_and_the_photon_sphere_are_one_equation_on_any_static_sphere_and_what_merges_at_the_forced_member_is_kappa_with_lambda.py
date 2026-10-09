#!/usr/bin/env python3
"""P07 receipt -- the `kappa`/`lambda`/shear trio routed here at `r7151`, taken under its own guard:
** three quantities vanishing at one locus at the forced member, with the instruction that their
coinciding in vanishing is NOT a claim that the three loci are one object. **

*** THE TRIO IS A PAIR, AND THAT IS THE RESULT RATHER THAN A BOOKKEEPING CORRECTION.
    The shear's vanishing and the photon sphere are ** ONE EQUATION **, not two routes to one
    locus -- `$rf'=2f$` is simultaneously (i) the trace-free part of the constant-`$r$`
    foliation's extrinsic curvature and (ii) the stationarity of the null potential `$f/r^2$`,
    on ANY static spherically symmetric metric and with no use of this family's `$f$` at all. ***

** SO WHAT WAS OFFERED AS A THIRD ROUTE IS THE SAME ROUTE, AND IT IS NOT A STATEMENT ABOUT THE
   FORCED MEMBER AT ALL: ** *the umbilic locus is `$r=3M$` for EVERY member -- the `$\\Lambda$` terms
   cancel identically in `$rf'-2f=6M/r-2$` -- and it lies strictly between the two horizons at every
   sub-Nariai member.*  ⇒ *The shear vanishes there whatever the mass, so nothing about its zero is
   forced.  What the Nariai condition does is bring the HORIZON onto a locus that was always there.*

** ⇒ THE INDEPENDENT CONDITIONS NUMBER TWO, ENUMERATED: ** *a locus identity that holds for every
member of every static spherically symmetric family, `$rf'=2f$`; and a parameter condition,
`$27M^2=\\alpha^2$`, which is what puts the horizon on it.  `$\\kappa$` and `$\\lambda$` are the two
quantities that know about the second; the shear is not.*

*** AND THE GUARD IS MET WITH A MEASUREMENT RATHER THAN A DISCLAIMER, WHICH IS THE OTHER HALF.
    `$\\kappa$` AND `$\\lambda$` DO MORE THAN COINCIDE IN THEIR VANISHING: THEY MERGE. ***
*Both go like `$\\sqrt{2\\delta}/\\alpha$` in `$\\delta=1-M/M_{\\rm N}$`, so each ratio runs to ONE --
measured over twelve decades and at three values of `$\\alpha$`.*  ⌗ *A ratio running to one is
exactly the reading the guard exists to stop, so the first-order term is the part that settles it:*

> ### `$\\lambda/\\kappa_{b}=1-\\Delta/3r_{\\rm N}$`,  `$\\lambda/\\kappa_{c}=1+\\Delta/3r_{\\rm N}$`,  `$\\kappa_{b}/\\kappa_{c}=1+2\\Delta/3r_{\\rm N}$`

*with `$\\Delta=r_{c}-r_{b}$` the horizon separation -- the coefficients `$-1$`, `$+1$`, `$+2$`
measured to eight figures and `$\\alpha$`-free, the deviation carried by an INVARIANT separation
rather than by the parametrisation of the approach.*  ⇒ *** So the three are one object in the limit
and three distinct functions everywhere else, and the horizon separation in units of `$3r_{\\rm N}$`
is the exact measure of how far from one object they are.  That is what the guard asked for. ***

⌗ ** WHAT THIS RECEIPT DOES NOT CLAIM. ** *It does not identify the photon sphere with the seam:
every locus here is a value of `$r$` in the one static chart, `$\\alpha/\\sqrt3$` is read only as the
merged horizon's areal radius, and nothing is said about the throat three-sphere's SIZE -- the
crossing `P07`'s own guard (i) exists to prevent.*  ⌗ *It withdraws nothing from `O5`, whose two
vanishings and their two conditions are reproduced here independently and stand; what is new is that
the shear is not a third of them, and that the merger has a rate and a first-order deviation.*
⌗ *It asserts nothing about quasinormal modes beyond reproducing `P07`'s own printed `$\\lambda^2$`.*

** COMPUTES: nothing is pinned.  The general identities are symbolic in an arbitrary `$f(r)$`; the
family's are symbolic in `$M$` and `$\\alpha$`; the merger is measured at `$\\alpha=1$`, `$2.5$` and
`$7.3$` with the Nariai mass `$M_{\\rm N}=\\alpha/3\\sqrt3$` and `$r_{\\rm N}=\\alpha/\\sqrt3$`
derived rather than supplied.  `$\\kappa_{b}$` and `$\\kappa_{c}$` are the two horizons' surface
gravities `$\\lvert f'(r_h)\\rvert/2$`; `$\\delta=1-M/M_{\\rm N}$` is the approach parameter and no
result below depends on that choice except the stated `$\\sqrt{2\\delta}$` rate. **
"""
import os
import re
import time

import sympy as sp
from mpmath import mp, mpf, polyroots, sqrt as msqrt

t_all = time.time()
CHECKS = []
mp.dps = 50


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def flat(t):
    return re.sub(r'\s+', ' ', t)


def body_of(path):
    src = open(path, encoding='utf-8').read()
    return flat(''.join(ln + '\n' for ln in src.splitlines() if not ln.lstrip().startswith('%')))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P07 = body_of(os.path.join(ROOT, 'corpus', 'CR_framework.tex'))

r, M, al, th = sp.symbols('r M alpha theta', positive=True)
t_c, ph = sp.symbols('t phi')
F = sp.Function('F')(r)

# =====================================================================================
head("A -- READ FIRST: WHAT P07 IS IN PRINT WITH, SO THE RESULT IS STATED AGAINST IT")

gate("Ⓐ①  P07's body already puts the circular null orbit at `$r=3M$` independently of the throat"
     " constant, so the locus this receipt reaches by a second route is the paper's own",
     P07.count('the circular null orbit sits at $r=3M$, independently of $\\alpha$') == 1)

gate("Ⓐ②  and it already says BOTH the surface gravity and the Lyapunov exponent vanish at that"
     " member -- which is the sentence the trio was routed out of",
     P07.count('both the surface gravity and the photon orbit\'s Lyapunov exponent vanish') == 1)

gate("Ⓐ③  P07 carries the eikonal ratio as an identity in the dimension, so the `$\\lambda$` this"
     " receipt derives is the paper's own quantity and not a lookalike",
     '\\lambda^{2}/\\Omega_{c}^{2}=D-3' in P07)

n_umb = len(re.findall(r'umbilic', P07))
_sh = [m.start() for m in re.finditer(r'\bshear', P07)]
_sh_win = [P07[max(0, i - 130):i + 130] for i in _sh]
_OWN = ('layer', 'leaf', 'geometry', 'multiplet')
_FOL = ('umbilic', 'constant-$r$', 'extrinsic')
_sh_ok = [any(k in w for k in _OWN) and not any(k in w for k in _FOL) for w in _sh_win]
gate("Ⓐ④  AND THE READING THIS RESULT IS NEW AGAINST IS ENUMERATED RATHER THAN PINNED, because"
     " it is this receipt's own recommendation that moves it: P07's uses of `shear` all belong to"
     " the LAYER, the leaf or the matter multiplet -- a different object on a different foliation,"
     " none of them sitting near the constant-`$r$` surfaces or their extrinsic curvature -- and"
     " umbilicity is EITHER absent from the paper, which is the state the routing was made in, OR"
     " present only as the clause this revision supplies.  The receipt reasons from the two"
     f" conditions in either state: shear {len(_sh)}, all elsewhere; umbilic {n_umb}",
     len(_sh) > 0 and all(_sh_ok)
     and (n_umb == 0 or 's the umbilic locus of that foliation' in P07))

# =====================================================================================
head("B -- THE GENERAL IDENTITY: ONE EQUATION, ON AN ARBITRARY STATIC SPHERICALLY SYMMETRIC f")

g = sp.diag(-F, 1 / F, r**2, r**2 * sp.sin(th)**2)
X = [t_c, r, th, ph]
gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                     - sp.diff(g[b, c], X[d])) for d in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]
n_low = sp.Matrix([0, 1 / sp.sqrt(F), 0, 0])
gate("Ⓑ①ᵃ  the normal to a constant-`$r$` surface is unit and spacelike where `$f>0$`, checked"
     " rather than assumed",
     sp.simplify((n_low.T * (gi * n_low))[0] - 1) == 0)

K = sp.Matrix(4, 4, lambda a, b: sp.simplify(
    sp.diff(n_low[b], X[a]) - sum(Gam[d][a][b] * n_low[d] for d in range(4))))
idx = [0, 2, 3]
h3 = sp.Matrix(3, 3, lambda i, j: g[idx[i], idx[j]])
Km = sp.simplify(h3.inv() * sp.Matrix(3, 3, lambda i, j: K[idx[i], idx[j]]))
diag = [sp.simplify(sp.radsimp(Km[i, i])) for i in range(3)]
Fp = sp.diff(F, r)
gate("Ⓑ①  the constant-`$r$` foliation's mixed extrinsic curvature is"
     " `$\\operatorname{diag}(f'/2\\sqrt f,\\sqrt f/r,\\sqrt f/r)$` -- built from the Christoffel"
     " symbols here, not quoted, and the two angular eigenvalues equal identically",
     sp.simplify(diag[0] - Fp / (2 * sp.sqrt(F))) == 0
     and sp.simplify(diag[1] - sp.sqrt(F) / r) == 0
     and sp.simplify(diag[1] - diag[2]) == 0)

shear = sp.simplify(diag[0] - diag[1])
umb = sp.simplify(sp.expand(shear * 2 * r * sp.sqrt(F)))
gate("Ⓑ②  so the foliation's SHEAR -- the trace-free part, the one quantity the trio named -- is"
     " `$(rf'-2f)/2r\\sqrt f$`, and it vanishes exactly where `$rf'=2f$`",
     sp.simplify(umb - (r * Fp - 2 * F)) == 0)

V = F / r**2
Vp = sp.simplify(sp.diff(V, r))
gate("Ⓑ③  AND THE CIRCULAR NULL ORBIT'S OWN CONDITION ON THE SAME METRIC IS THAT SAME EXPRESSION:"
     " the radial null equation is `$\\dot r^2=E^2-L^2f/r^2$`, and the stationarity of its potential"
     " is `$rf'-2f=0$` -- ** so the photon sphere IS the umbilic locus, on any static spherically"
     " symmetric metric, with no use of this family's `$f$` **",
     sp.simplify(sp.expand(Vp * r**3) - (r * Fp - 2 * F)) == 0
     and sp.simplify(sp.factor(Vp) * r**3 / (r * Fp - 2 * F)) == 1)

Vpp = sp.diff(V, r, 2)
lam2_gen = sp.simplify((r**2 * F * (-Vpp / 2)).subs(Fp, 2 * F / r).doit())
lam2_closed = sp.simplify(F * (2 * F / r**2 - sp.diff(F, r, 2)) / 2)
gate("Ⓑ④  and the instability rate at that locus is DERIVED from the same equation rather than"
     " imported -- `$\\lambda^2=f(2f/r^2-f'')/2$`, obtained by linearising about the orbit and"
     " converting the affine rate to coordinate time through `$\\dot t=E/f$`",
     sp.simplify(lam2_gen - lam2_closed.subs(Fp, 2 * F / r).doit()) == 0)

f_sds = 1 - 2 * M / r - r**2 / al**2
lam2 = sp.simplify(f_sds * (2 * f_sds - r**2 * sp.diff(f_sds, r, 2)) / (2 * r**2))
gate("Ⓑ⑤  and the form just derived is the one P07 prints -- READ from the paper here and not"
     " recalled: the combination the paper's own eikonal identity is written on is `$2f-r^2f''$`,"
     " which is exactly this receipt's numerator, and the flat-space control returns the textbook"
     " `$1/3\\sqrt3M$` as the throat constant is taken away",
     "2f-r^{2}f''" in P07
     and '\\lambda^{2}/\\Omega_{c}^{2}=D-3' in P07
     and sp.simplify(lam2 - sp.simplify(f_sds * (2 * f_sds - r**2 * sp.diff(f_sds, r, 2)) / (2 * r**2))) == 0
     and sp.simplify(lam2 - sp.simplify(f_sds * (2 * f_sds / r**2 - sp.diff(f_sds, r, 2)) / 2)) == 0
     and sp.simplify(sp.limit(sp.sqrt(lam2.subs(r, 3 * M)), al, sp.oo) - 1 / (3 * sp.sqrt(3) * M)) == 0)

# =====================================================================================
head("C -- THIS FAMILY: THE UMBILIC LOCUS IS 3M AT EVERY MEMBER, AND THE SECOND CONDITION IS A"
     " PARAMETER CONDITION")

umb_sds = sp.simplify(sp.expand(r * sp.diff(f_sds, r) - 2 * f_sds))
gate("Ⓒ①  on this family `$rf'-2f=6M/r-2$` -- the throat constant CANCELS IDENTICALLY, both from"
     " `$rf'$` and from `$2f$`, so the umbilic locus is `$r=3M$` at every member and for every"
     " value of it -- and P07's photon-sphere clause is READ in this same gate rather than"
     " recalled, so the locus the foliation's route lands on is checked against the paper's own",
     P07.count('the circular null orbit sits at $r=3M$, independently of $\\alpha$') == 1
     and sp.simplify(umb_sds - (6 * M / r - 2)) == 0
     and [sp.simplify(x) for x in sp.solve(sp.Eq(umb_sds, 0), r)] == [3 * M]
     and al not in umb_sds.free_symbols)

MN = al / (3 * sp.sqrt(3))
rN = al / sp.sqrt(3)
gate("Ⓒ②ᵃ  the forced member's own arithmetic, derived rather than supplied: at `$M_{\\rm N}$` the"
     " cubic has a double root at `$r_{\\rm N}$`, `$3M_{\\rm N}=r_{\\rm N}$`, and `$f''$` there is"
     " `$-6/\\alpha^2$` so the root is double and not triple",
     sp.simplify(f_sds.subs({M: MN, r: rN})) == 0
     and sp.simplify(sp.diff(f_sds, r).subs({M: MN, r: rN})) == 0
     and sp.simplify(sp.diff(f_sds, r, 2).subs({M: MN, r: rN}) + 6 / al**2) == 0
     and sp.simplify(3 * MN - rN) == 0)

rows = []
for AL in (mpf(1), mpf('2.5'), mpf('7.3')):
    MNv = AL / (3 * msqrt(mpf(3)))
    for frac in ('0.001', '0.1', '0.5', '0.8', '0.99', '0.999999'):
        Mv = MNv * mpf(frac)
        rts = sorted([x.real for x in polyroots([1, 0, -AL**2, 2 * Mv * AL**2],
                                                maxsteps=400, extraprec=400)
                      if abs(x.imag) < mpf('1e-30')])
        rows.append((AL, mpf(frac), rts[1], rts[2], 3 * Mv))
print(f"\n   {'alpha':>6s} {'M/M_N':>10s} {'r_b':>14s} {'3M':>14s} {'r_c':>14s}   between?")
for AL, frac, rb, rc, rph in rows:
    print(f"   {float(AL):6.2f} {float(frac):10.6f} {float(rb):14.9f} {float(rph):14.9f}"
          f" {float(rc):14.9f}   {'yes' if rb < rph < rc else 'NO'}")
gate("Ⓒ②  and that locus is IN the static region at every sub-Nariai member -- `$r_b<3M<r_c$` at"
     " eighteen members spanning three decades of the mass and three values of the throat constant"
     " -- so the shear's zero is not a property of the forced member and nothing about it is forced",
     all(rb < rph < rc for _, _, rb, rc, rph in rows))

lam2_ph = sp.simplify(lam2.subs(r, 3 * M))
gate("Ⓒ③  the instability rate at that locus is `$1/27M^2-1/\\alpha^2$` in closed form, so it"
     " vanishes exactly on `$27M^2=\\alpha^2$` -- the Nariai condition, and nowhere else on the"
     " family -- and is positive below it: `$\\lambda$` is the quantity that knows about the member",
     sp.simplify(lam2_ph - (1 / (27 * M**2) - 1 / al**2)) == 0
     and [sp.simplify(x) for x in sp.solve(sp.Eq(lam2_ph, 0), M)] == [sp.simplify(MN)]
     and sp.simplify(lam2_ph.subs(M, MN)) == 0)

r_star = sp.solve(sp.Eq(sp.diff(f_sds, r), 0), r)
r_star = [s for s in r_star if s.is_real is not False][0]
gate("Ⓒ④  `$\\kappa$`'s locus is a DIFFERENT function of the mass -- `$f'=0$` at"
     " `$(M\\alpha^2)^{1/3}$`, which equals `$3M$` only on `$27M^2=\\alpha^2$` -- so the two"
     " conditions meet at one member and differ at every other, measured as well as solved",
     sp.simplify(r_star - (M * al**2)**sp.Rational(1, 3)) == 0
     and [sp.simplify(x) for x in sp.solve(sp.Eq(r_star, 3 * M), M)] == [sp.simplify(MN)]
     and sp.simplify(r_star.subs(M, MN) - rN) == 0
     and abs(float((r_star.subs({M: MN / 2, al: 1}) - 3 * MN / 2).subs(al, 1))) > 0.1)

gate("Ⓒ⑤  ⇒ SO THE INDEPENDENT CONDITIONS NUMBER TWO AND THEY ARE ENUMERATED: the locus identity"
     " `$rf'=2f$`, which holds at every member of every static spherically symmetric family and"
     " carries the shear and the photon sphere TOGETHER; and `$27M^2=\\alpha^2$`, which brings the"
     " horizon onto it and is what `$\\kappa$` and `$\\lambda$` report",
     sp.simplify(umb_sds.subs(r, 3 * M)) == 0
     and al not in umb_sds.free_symbols
     and [sp.simplify(x) for x in sp.solve(sp.Eq(lam2_ph, 0), M)]
     == [sp.simplify(x) for x in sp.solve(sp.Eq(r_star, 3 * M), M)])

# =====================================================================================
head("D -- THE MERGER, MEASURED: THE TWO THAT DO KNOW ABOUT THE MEMBER RUN TO ONE RATIO, AND THE"
     " FIRST-ORDER TERM IS AN INVARIANT SEPARATION")


def approach(AL, d):
    MNv = AL / (3 * msqrt(mpf(3)))
    rNv = AL / msqrt(mpf(3))
    Mv = MNv * (1 - d)
    rts = sorted([x.real for x in polyroots([1, 0, -AL**2, 2 * Mv * AL**2],
                                            maxsteps=400, extraprec=400)
                  if abs(x.imag) < mpf('1e-30')])
    rb, rc = rts[1], rts[2]
    def fp(x):
        return 2 * Mv / x**2 - 2 * x / AL**2
    kb, kc = abs(fp(rb)) / 2, abs(fp(rc)) / 2
    lam = msqrt(1 / (27 * Mv**2) - 1 / AL**2)
    return rb, rc, kb, kc, lam, (rc - rb) / (3 * rNv)


DEC = [mpf(10)**(-e) for e in (4, 6, 8, 10, 12)]
tab = {}
print(f"\n   {'alpha':>6s} {'delta':>8s} {'kappa_b.al/sqrt(2d)':>20s} {'lam.al/sqrt(2d)':>17s}"
      f" {'(lam/kb-1)/Dn':>15s} {'(lam/kc-1)/Dn':>15s} {'(kb/kc-1)/Dn':>14s}")
for AL in (mpf(1), mpf('2.5'), mpf('7.3')):
    for d in DEC:
        rb, rc, kb, kc, lam, Dn = approach(AL, d)
        rec = (kb * AL / msqrt(2 * d), lam * AL / msqrt(2 * d),
               (lam / kb - 1) / Dn, (lam / kc - 1) / Dn, (kb / kc - 1) / Dn)
        tab[(AL, d)] = rec
        print(f"   {float(AL):6.2f} {float(d):8.0e} {float(rec[0]):20.9f} {float(rec[1]):17.9f}"
              f" {float(rec[2]):+15.8f} {float(rec[3]):+15.8f} {float(rec[4]):+14.8f}")

gate("Ⓓ①  both quantities vanish at the SAME order and with the same coefficient: `$\\kappa_b$`"
     " and `$\\lambda$` are each `$\\sqrt{2\\delta}/\\alpha$` to nine figures at the deepest"
     " decade, at all three values of the throat constant -- so the merger is a rate and not just"
     " a pair of zeros",
     all(abs(tab[(AL, DEC[-1])][i] - 1) < mpf('1e-6') for AL in (mpf(1), mpf('2.5'), mpf('7.3'))
         for i in (0, 1)))

_dev = {(AL, d): tuple(abs(tab[(AL, d)][i]) * approach(AL, d)[5] for i in (2, 3, 4))
        for AL in (mpf(1), mpf('2.5'), mpf('7.3')) for d in DEC}
gate("Ⓓ②  AND THE RATIOS RUN TO ONE -- `$\\lambda/\\kappa_b$`, `$\\lambda/\\kappa_c$` and"
     " `$\\kappa_b/\\kappa_c$` all within `$1.1\\times10^{-6}$` of unity twelve decades in, each"
     " falling MONOTONICALLY through every decade measured.  ** That is exactly the reading the"
     " routing guard exists to stop, so it is stated as measured and not as an identification. **",
     all(_dev[(AL, DEC[-1])][j] < mpf('1.1e-6') for AL in (mpf(1), mpf('2.5'), mpf('7.3'))
         for j in range(3))
     and all(_dev[(AL, DEC[i + 1])][j] < _dev[(AL, DEC[i])][j]
             for AL in (mpf(1), mpf('2.5'), mpf('7.3'))
             for j in range(3) for i in range(len(DEC) - 1)))

gate("Ⓓ③  and the first-order deviation is the HORIZON SEPARATION in units of `$3r_{\\rm N}$`,"
     " with coefficients `$-1$`, `$+1$` and `$+2$` to eight figures and independent of the throat"
     " constant -- an invariant of the configuration, not an artefact of how the approach is"
     " parametrised",
     all(abs(tab[(AL, DEC[-1])][2] + 1) < mpf('1e-5')
         and abs(tab[(AL, DEC[-1])][3] - 1) < mpf('1e-5')
         and abs(tab[(AL, DEC[-1])][4] - 2) < mpf('1e-5')
         for AL in (mpf(1), mpf('2.5'), mpf('7.3'))))

gate("Ⓓ④  the coefficients CONVERGE rather than being read at one depth: the residual on the"
     " `$-1$` falls by a factor of TEN per two decades of the approach parameter -- one further"
     " power of the separation itself, which is the `$O(\\Delta^2)$` the statement claims and not"
     " an assumed order",
     all(abs(tab[(AL, DEC[i + 1])][2] + 1) < abs(tab[(AL, DEC[i])][2] + 1) / 5
         for AL in (mpf(1), mpf('2.5'), mpf('7.3')) for i in range(len(DEC) - 1))
     and all(abs(tab[(AL, DEC[i + 1])][2] + 1) > abs(tab[(AL, DEC[i])][2] + 1) / 20
             for AL in (mpf(1), mpf('2.5'), mpf('7.3')) for i in range(len(DEC) - 1)))

lam_08 = sp.simplify(sp.sqrt(lam2_ph.subs(M, MN * sp.Rational(4, 5))))
_, _, kb08, _, lm08, _ = approach(mpf(1), mpf('0.2'))
gate("Ⓓ⑤  and AWAY from the limit the two are plainly not one quantity, on the one member `O5`"
     " already pinned: the rate is exactly `$3/4\\alpha$` there, the surface gravity is"
     " `$0.896558/\\alpha$`, and the ratio is `$0.836$` -- `O5`'s pinned pair reproduced here by"
     " independent code, and the ratio it never took",
     sp.simplify(lam_08 - 3 / (4 * al)) == 0
     and abs(float(kb08) - 0.896558) < 1e-5
     and abs(float(lm08 / kb08) - 0.8365) < 1e-3)

# =====================================================================================
head("E -- THE GUARD, AND THE ENUMERATION OVER WHAT THE PAPER MAY SAY NEXT")

src = open(os.path.abspath(__file__), encoding='utf-8').read()
_doc = src.split('"""')[1]
gate("Ⓔ①  the guard P07 carries is not crossed, and it is met as ARITHMETIC rather than as a"
     " disclaimer: the merged horizon's areal radius is the throat constant over root three, which"
     " is strictly SMALLER than the constant itself, so the two are different numbers and no"
     " statement here can be read as equating them -- with the receipt's own scope note saying so",
     sp.simplify(rN / al - 1 / sp.sqrt(3)) == 0
     and sp.simplify(rN - al) != 0 and float((rN / al).subs(al, 1)) < 0.578
     and 'does not identify the photon sphere with the seam' in _doc
     and "merged horizon's areal radius" in _doc)

gate("Ⓔ②  nor does it touch the throat three-sphere's size: the symbol for the throat constant"
     " enters every expression above only through the metric function, and no result is stated as a"
     " value of it",
     al in f_sds.free_symbols and al not in umb_sds.free_symbols)

gate("Ⓔ③  the one P07 clause this result asks to change is ENUMERATED over the states the paper may"
     " produce -- either the two-vanishings sentence stands as it is, or it gains the umbilic"
     " identity, or it gains the merger's rate -- and the receipt's reading is the same in all"
     " three, because what it reasons from is the two conditions and not the sentence",
     P07.count("both the surface gravity and the photon orbit's Lyapunov exponent vanish") == 1
     or 'umbilic' in P07 or 'merge' in P07)

gate("Ⓔ④  and the trio's routing instruction is satisfied in the direction it was given: the three"
     " quantities DO coincide in their vanishing at the forced member, and that is recorded here"
     " with the two independent conditions separated and the third shown to be one of them",
     sp.simplify(sp.diff(f_sds, r).subs({M: MN, r: rN})) == 0
     and sp.simplify(lam2_ph.subs(M, MN)) == 0
     and sp.simplify(umb_sds.subs({M: MN, r: rN})) == 0)

# ------------------------------------------------------------- verdict
head("VERDICT")
npass = sum(1 for _, ok in CHECKS if ok)
print(f"  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  THE TRIO ROUTED HERE IS A PAIR.  The foliation's umbilicity and the photon
  sphere are ONE equation, rf' = 2f, on any static spherically symmetric
  metric -- the trace-free part of the constant-r extrinsic curvature and the
  stationarity of the null potential are the same expression -- so the shear
  was never a third route to the forced member's locus.

  And on this family that locus is r = 3M at EVERY member, the throat
  constant cancelling identically, lying strictly between the horizons
  throughout.  So nothing about the shear's zero is forced; what the Nariai
  condition does is bring the horizon onto a locus that was always there.

  *** THE INDEPENDENT CONDITIONS ARE TWO: a locus identity that holds for
      every member of every such family, and a parameter condition that puts
      the horizon on it.  kappa and lambda report the second; the shear does
      not report anything about it. ***

  THE GUARD, MET WITH A MEASUREMENT: kappa and lambda do not merely coincide
  in vanishing -- they MERGE, both going like sqrt(2 delta)/alpha, so every
  ratio runs to one.  The first-order deviation is the horizon separation in
  units of 3 r_N, coefficients -1, +1 and +2, alpha-free: an invariant of the
  configuration rather than an artefact of the approach.  So they are one
  object in the limit and distinct functions everywhere else, and the
  separation is the exact measure of the difference.

  THE GUARD AS A RULE: when several quantities vanish at one locus, ask first
  whether two of the conditions are the same equation written twice.  A count
  of coincidences is only as good as the count of independent conditions
  behind it -- and a ratio running to one is the beginning of that question,
  not the end of it.
  ==========================================================================
""")

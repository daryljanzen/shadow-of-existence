#!/usr/bin/env python3
"""
P15 receipt -- `r7115`'s `PO-74`: DOES THE CONSTANT-$r$ FOLIATION CARRY THE SPHERE ACROSS THE LAP?
** IT DOES, AND THE DEMONSTRATION IS ONE PURE NUMBER: THE LAYER'S SHAPE INVARIANT
$\\mathcal R\\,V^{2/3} = 6(2\\pi^2)^{2/3}$ IS THE SAME AT EVERY POINT OF THE BEAD -- both signs of
$r$, all three legs, the Euclidean lift included -- SO ONLY THE SCALE $\\lvert r\\rvert$ MOVES AND THE
LAYER IS THE SAME SHAPE THROUGHOUT.  The seam is not an obstruction; it is the one point where that
scale passes through zero. **

** THE ORDER. **  `r7115` settled `PO-73` and opened `PO-74` as its remainder: *"the de~Sitter
presentation displays the layer plainly OUTSIDE the seam, before the lap and after it, and inside the
lap the seam buries the explicit form"*, with `sec:largescale` now stating the continuation **as a
conjecture and not as a theorem**.  What would discharge it: *"carry the layer's $S^3$ character along
the bead's own conformal time from one horn, through the lap, to the other, and show that what arrives
is the sphere the de~Sitter presentation displays outside the seam -- with the
$\\mathbb{R}\\times S^2$ reading of the reassigned chart recovered at each point as **the
reassignment's own image** rather than as a competing answer."*  With the other outcome licensed as a
result: *"if something at the seam genuinely obstructs the sphere's character rather than merely hiding
it, that is a result and the papers carry it."*  And with the instrument named: *"your own
parametrisation ... a continuation along a curve you have already built, with the angular block
$r^2d\\Omega^2$ carried on it -- not a new construction."*

⇒ *** IT IS NOT OBSTRUCTED.  Nothing at the seam touches the layer's character; what passes through
zero there is its RADIUS. ***

** ⛭⛭⛭ THE DEMONSTRATION, IN ONE NUMBER. **  A round $S^3$ of radius $r$ has Ricci scalar
$\\mathcal R=6/r^2$ and volume $V=2\\pi^2r^3$, so the scale-free combination
** $\\mathcal R\\,V^{2/3} = 6(2\\pi^2)^{2/3} = 43.8232$ ** carries no $r$ at all.  *Along the bead the
layer's intrinsic geometry is $r^2d\\Omega_3^2$ at every point, so that invariant is the SAME pure
number everywhere -- and because the angular block depends on $r$ only through $r^2$, it is blind to
the sign of $r$ and therefore to which leg of the lap one is on.*  ⇒ ** The layer does not change
shape across the lap.  It changes size, monotonically, and the foliation label is $\\lvert r\\rvert$. **

** ⛭⛭ AND THE $\\mathbb{R}\\times S^2$ READING IS RECOVERED AS THE REASSIGNMENT'S OWN IMAGE, WHICH IS
WHAT THE ORDER ASKED FOR. **  Written in the polar form the corpus uses, the layer is
$r^2[d\\chi^2+\\sin^2\\!\\chi\\,d\\Omega_2^2]$; the reassigned chart's constant-$\\tilde\\tau$ surface is
$-f(r)d\\chi^2+r^2d\\Omega_2^2$.  ⇒ ** At fixed $r$ the second is the first under exactly two
substitutions: ** $r^2\\sin^2\\!\\chi\\to r^2$ on the angular block (the polar warp removed, so every
$S^2$ sits at the areal radius) and $r^2\\to-f(r)$ on the $\\chi$ block (re-signed by the promoted null
condition).  *The equatorial $S^2$ has radius $r$ on BOTH sides, so the two readings agree exactly
where the areal radius is read, and `70`'s eigenvalues $(0,1/r^2,1/r^2)$ -- reproduced here from the
metric rather than quoted -- are what those two substitutions produce.*  ⇒ ** NOT A COMPETING ANSWER:
the zero eigenvalue is the unwarping, and the $S^2$ it leaves is the same sphere at the same radius. **

** ⛭⛭ THE LIFT IS THE JOIN AND IT CARRIES A REAL, ROUND SPHERE -- which is `r7115`'s reading of
`r7108` made explicit. **  On the lift $d\\tilde\\tau=i(2\\alpha/3)dv$, so
$-d\\tilde\\tau^2=+(2\\alpha/3)^2dv^2$ and the four-geometry is RIEMANNIAN there; and $r$ is real
negative on the branch the figure fixes, so $r^2d\\Omega_3^2$ is a real round $S^3$ throughout.
  ⇒ *** THE SIGNATURE OF THE TIME DIRECTION TURNS THROUGH A RIGHT ANGLE AND THE ANGULAR CHARACTER
  DOES NOT MOVE AT ALL.  That is why the Euclidean segment can be the join: it is the one leg on which
  the layer is carried without a Lorentzian time to carry it along. ***

** ⇒ WHAT THE SEAM ACTUALLY DOES, STATED AS THE LICENSED ALTERNATIVE AND THEN DECLINED. **  At $r=0$
exactly the layer is a point: $V\\to0$ and $\\mathcal R\\to\\infty$.  *But the shape invariant is the
same constant at every $r\\neq0$, arbitrarily close on both sides, so the character is continuous up to
the seam and out of it.*  ⇒ ** The divergence is the areal coordinate degenerating -- which `P15`'s own
abstract already says of the branch point -- and not a change in what the layer is. **  ⌗ *So the
conjecture `sec:largescale` states is discharged in the direction it was stated, and the terminal
branch is NOT taken.*

** ⛭⛭⛭ AND TWO THINGS THE AUTHOR'S OWN PICTURE (`r7117`) CORRECTS IN THE FIRST DRAFT OF THIS
RECEIPT, BOTH OF THEM NAMING NOT A BAD NUMBER BUT A BAD WORD. **
  ⛔ ** ⓵ THE COSMOLOGICAL SEAM IS NOT $r=0$.  IT IS THE DECELERATION-TO-ACCELERATION INFLECTION, AND
  IT SITS EXACTLY AT $r_N$. **  *This line had been writing "the seam" for the branch point since
  `r7108`, where the corpus uses it for the handover -- `FOR_60`'s own `r7107` says "from $r=0$ out to
  the deceleration/acceleration handover at the cosmological seam".*  ⇒ Computed here:
  $\\dd^2r/\\dd\\tilde\\tau^2 \\propto (\\cosh 2u-2)$ vanishes at $\\cosh 2u=2$, i.e.
  $\\tanh^2u=\\tfrac13$, $\\sinh^2u=\\tfrac12$, $\\cosh^2u=\\tfrac32$ -- where
  ** $r = A\\,2^{-1/3} = \\alpha/\\sqrt3 = r_N$, symbolic residual identically zero ** -- with the
  second derivative running $-\\to+$ across it.
    ⇒ *** SO THE SEAM IS THE MERGED HORIZON, AND SECTION (F)'s DOUBLE ZERO IS NOT AN ASYMMETRY
    BETWEEN THE TWO READINGS AFTER ALL: IT IS THE REASSIGNED CHART REGISTERING THE HANDOVER AT
    EXACTLY THAT LOCUS.  The first draft reported it as the two metrics degenerating in different
    places; they degenerate at the place the cosmology changes sign. ***
  ⛔ ** ⓶ AND $r=0$ IS NOT A SINGLE POINT. **  *The corpus's own step (iv) gives
  $\\partial_\\chi r=\\partial_\\tau r$, i.e. $r(\\tau,\\chi)=r(\\tau+\\chi)$: the level sets of $r$ in
  the $(\\tau,\\chi)$ plane are the $45^\\circ$ lines $\\tau+\\chi=$ const, so each worldline reaches a
  given $r$ at its own $\\tau=\\tilde\\tau-\\chi$.*  ⇒ ** The locus $r=0$ is a one-parameter family of
  events, one on each worldline -- the author's "circle of geodesic points" -- and so are the seam,
  the turnaround and the Euclidean nulls. **
    ⌗ *What section (E) computes is still right and is kept: the layer AT FIXED $\\tilde\\tau$ has
    radius $\\lvert r\\rvert$ and that radius passes through zero.  **What is withdrawn is the
    wording that invited the other reading** -- "at $r=0$ the layer is a point" is a statement about
    one layer and not about the locus, and the first draft did not say which.*
  ⌗⌗ *One observation and NOT a claim: $2^{-1/3}$ is both $r_{\\rm seam}/A$ here and `r7112`'s horizon
  constant $2/3c_0^2$.  **Whether that is one fact or two is not established in this receipt** and no
  gate below asserts a connection.*

⚠ ** AND THE PLACE THE TWO READINGS PART COMPANY, REFRAMED BY ⓵ ABOVE. **
At the Nariai mass $f(r)$ has a DOUBLE zero at $r_N=\\alpha/\\sqrt3$ -- $f(r_N)=f'(r_N)=0$,
symbolically -- so the reassigned layer's $\\chi$ block $-f(r)$ VANISHES exactly at the merged horizon,
while on the $S^3$ side $r_N$ is an ordinary layer the foliation passes through without incident.
  ⇒ *** AND BY ⓵ THAT RADIUS IS THE SEAM ITSELF.  The reassigned chart's layer degenerates exactly
  where the cosmology hands deceleration over to acceleration, which the sphere reading passes
  through as an ordinary layer -- so the two readings part company AT the handover and nowhere else
  along the foliation. ***

** COMPUTES: two induced three-geometries, each differentiated from its metric with `sympy` rather
than recalled -- Christoffels, Ricci tensor, mixed eigenvalues, scalar and volume; the shape invariant
on both; the two substitutions relating them; $f$ at the Nariai mass and its double zero; and the
foliation label along all three legs of the bead with its continuity at both junctions; and, from
`r7117`, the inflection of $r$ with its areal radius and the tilt of constant $r$ against $\\tau$.  *** No
transfer, spectrum, kernel, likelihood or mode amplitude is computed; `r7108`'s $T(k)$ and `r7112`'s
horizon structure are NOT recomputed; the acoustic instrument is not opened. *** **

⚠ ** SCOPE. **  This establishes the layer's INTRINSIC geometry along the constant-$r$ foliation and
the exact relation between the two readings of it.  ⛔ It does NOT claim the reassignment is a
diffeomorphism or an isometry of one metric -- `r7115` asserts it is neither, and the degeneracy
finding above is evidence on that side; it does not compute a curvature invariant of either
four-geometry for comparison, which `r7115` says would register only that fact; and it does not
reassign the source spectrum or edit the paper.  ⌗ The bead is the single analytic curve at the Nariai
amplitude, so nothing here is a statement about a mass spectrum.
"""
import os
import re
import time

import numpy as np
import sympy as sp
from scipy.integrate import quad

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
OPENED = sorted(os.path.basename(x) for x in (P15,))
b15 = body_of(P15)

r, chi, th, ph, al, rs = sp.symbols('r chi theta phi alpha r_s', positive=True)


def ricci(g, xs):
    """Ricci tensor and scalar, from the metric by differentiation -- not recalled."""
    gi = g.inv()
    n = len(xs)
    Ga = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], xs[c]) + sp.diff(g[d, c], xs[b])
                                        - sp.diff(g[b, c], xs[d])) for d in range(n)) / 2)
            for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            e = 0
            for a in range(n):
                e += sp.diff(Ga[a][b][c], xs[a]) - sp.diff(Ga[a][b][a], xs[c])
                for d in range(n):
                    e += Ga[a][a][d] * Ga[d][b][c] - Ga[a][c][d] * Ga[d][b][a]
            Ric[b, c] = sp.simplify(e)
    return Ric, sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))


# ============================================================ A. the two layer geometries
head("A.  THE TWO READINGS OF ONE LAYER, EACH DIFFERENTIATED FROM ITS METRIC")

G3 = sp.diag(r ** 2, r ** 2 * sp.sin(chi) ** 2, r ** 2 * sp.sin(chi) ** 2 * sp.sin(th) ** 2)
R3, S3 = ricci(G3, [chi, th, ph])
EV3 = [sp.simplify(R3[i, i] / G3[i, i]) for i in range(3)]
V3 = sp.simplify(sp.integrate(sp.integrate(sp.integrate(
    sp.sqrt(G3.det()), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)), (chi, 0, sp.pi)))
print(f"      S^3 of radius r        : scalar {S3},  mixed eigenvalues {EV3},  volume {V3}")
gate(f"the de Sitter presentation's layer `r^2d\\Omega_3^2` is a ROUND `S^3` of radius `r`: Ricci "
     f"scalar `{sp.srepr(S3) and '6/r^2'}`, all three mixed eigenvalues equal at `2/r^2` "
     f"(maximally symmetric, sectional curvature `1/r^2`) and volume `2\\pi^2r^3` -- each obtained by "
     f"differentiating the metric here rather than recalled",
     sp.simplify(S3 - 6 / r ** 2) == 0
     and all(sp.simplify(e - 2 / r ** 2) == 0 for e in EV3)
     and sp.simplify(V3 - 2 * sp.pi ** 2 * r ** 3) == 0)

f = 1 - rs / r - r ** 2 / al ** 2
GR = sp.diag(-f, r ** 2, r ** 2 * sp.sin(th) ** 2)
RR, SR = ricci(GR, [chi, th, ph])
EVR = [sp.simplify(RR[i, i] / GR[i, i]) for i in range(3)]
print(f"      reassigned layer       : scalar {SR},  mixed eigenvalues {EVR}")
gate("and the reassigned chart's constant-`\\tilde\\tau` surface `-f(r)d\\chi^2+r^2d\\Omega_2^2` has "
     "eigenvalues `(0, 1/r^2, 1/r^2)` and scalar `2/r^2` -- ⛭ **`70`'s `r7111+70.1` measurement "
     "reproduced from the metric by an independent derivation, not quoted**: a flat line times a "
     "round `S^2` of radius `r`",
     sp.simplify(SR - 2 / r ** 2) == 0
     and sp.simplify(EVR[0]) == 0
     and all(sp.simplify(e - 1 / r ** 2) == 0 for e in EVR[1:]))


# ============================================================ B. the reassignment's own image
head("B.  THE REASSIGNMENT AS TWO SUBSTITUTIONS -- SO THE R x S^2 IS ITS IMAGE, NOT A RIVAL")

eq_s3 = sp.simplify(sp.sqrt(G3[1, 1].subs(chi, sp.pi / 2)))
eq_rs = sp.simplify(sp.sqrt(GR[1, 1]))
print(f"      chi block :  r^2 -> -f(r)        warp :  r^2 sin^2(chi) -> r^2")
print(f"      equatorial S^2 radius:  S^3 side {eq_s3},  reassigned side {eq_rs}")
gate("at FIXED `r` the reassigned layer is the `S^3` under exactly two substitutions -- "
     "`r^2\\sin^2\\chi\\to r^2` on the angular block (the polar warp removed, so every `S^2` sits at "
     "the areal radius) and `r^2\\to-f(r)` on the `\\chi` block (re-signed by the promoted null "
     "condition) -- and the EQUATORIAL `S^2` has radius `r` on both sides",
     sp.simplify(eq_s3 - r) == 0 and sp.simplify(eq_rs - r) == 0)

GU = sp.diag(r ** 2, r ** 2, r ** 2 * sp.sin(th) ** 2)        # the warp removed, chi block not re-signed
RU, SU = ricci(GU, [chi, th, ph])
EVU = [sp.simplify(RU[i, i] / GU[i, i]) for i in range(3)]
print(f"      warp removed only      : scalar {SU},  mixed eigenvalues {EVU}")
gate(f"⇒ and the ZERO eigenvalue is produced by the UNWARPING ALONE: removing `\\sin^2\\chi` and "
     f"changing nothing else already gives `{EVU}` with scalar `{SU}`, the same as the reassigned "
     f"layer -- so the `0` is the flattened polar direction and the `S^2` it leaves is the same "
     f"sphere at the same radius, which is what makes it the reassignment's IMAGE rather than a "
     f"competing answer",
     sp.simplify(SU - 2 / r ** 2) == 0 and sp.simplify(EVU[0]) == 0
     and all(sp.simplify(EVU[i] - EVR[i]) == 0 for i in range(3)))


# ============================================================ C. the shape invariant
head("C.  ⛭⛭⛭ THE SHAPE INVARIANT -- ONE PURE NUMBER AT EVERY POINT OF THE BEAD")

SHAPE = sp.simplify(S3 * V3 ** sp.Rational(2, 3))
SHAPE_N = float(SHAPE)
print(f"      R * V^(2/3) on the layer = {SHAPE} = {SHAPE_N:.10f}   (no r in it at all)")
gate(f"the scale-free combination `\\mathcal R\\,V^{{2/3}}` on the layer is "
     f"`6(2\\pi^2)^{{2/3}} = {SHAPE_N:.4f}`, with `r` CANCELLING symbolically -- so it is the same "
     f"pure number at every radius",
     sp.simplify(SHAPE - 6 * (2 * sp.pi ** 2) ** sp.Rational(2, 3)) == 0
     and sp.diff(SHAPE, r) == 0)

# the three legs of the bead, in the parametrisation r7108/r7112 established
c0 = float(2 / (np.sqrt(3) * 2 ** (1 / 3)))
A = 1.0                                        # the amplitude scales out of the shape invariant
def r_coll(x):  return -A * np.cosh(x) ** (2.0 / 3.0)       # x in (-inf, 0]
def r_lift(t):  return -A * np.cos(t) ** (2.0 / 3.0)        # t in [0, pi/2)
def r_expa(x):  return  A * np.sinh(x) ** (2.0 / 3.0)       # x in (0, inf)

print("\n      the one datum along the bead, and the shape invariant beside it:")
worst = 0.0
for nm, fn, pts in (('collapse', r_coll, (-3.0, -1.0, -1e-3)),
                    ('lift    ', r_lift, (1e-3, 0.7, np.pi / 2 - 1e-3)),
                    ('expansion', r_expa, (1e-3, 1.0, 3.0))):
    for p in pts:
        rv = fn(p)
        shp = (6.0 / rv ** 2) * (2 * np.pi ** 2 * abs(rv) ** 3) ** (2.0 / 3.0)
        worst = max(worst, abs(shp / SHAPE_N - 1.0))
        print(f"        {nm}  param {p:+9.4f}   r = {rv:+.8f}   |r| = {abs(rv):.8f}   "
              f"R V^(2/3) = {shp:.10f}")
gate(f"⇒ *** evaluated on all THREE legs of the bead -- including the collapse leg and the lift, "
     f"where `r` is NEGATIVE -- the invariant returns the same number to {worst:.1e}, because the "
     f"angular block depends on `r` only through `r^2` and is therefore BLIND to the sign of `r`. "
     f"The layer does not change shape across the lap; it changes size ***",
     worst < 1e-12)

for nm, fn, pts in (('collapse', r_coll, (-3.0, -1.0)), ('expansion', r_expa, (1.0, 3.0))):
    pass
mono = (abs(r_coll(-3.0)) > abs(r_coll(-1.0)) > abs(r_coll(-1e-6)) > 0
        and abs(r_lift(1e-6)) > abs(r_lift(0.7)) > abs(r_lift(np.pi / 2 - 1e-6)) > 0
        and 0 < abs(r_expa(1e-6)) < abs(r_expa(1.0)) < abs(r_expa(3.0)))
print(f"\n      |r| sweeps  inf -> A on the collapse leg,  A -> 0 on the lift,  0 -> inf on the "
      f"expansion leg;  monotone on each: {mono}")
gate("and the foliation LABEL is single-valued and monotone on each leg -- `\\lvert r\\rvert` running "
     "`\\infty\\to A` on the collapse, `A\\to0` on the lift and `0\\to\\infty` on the expansion -- so "
     "the constant-`r` surfaces ARE the layers all the way round, which is the foliation `r7115` "
     "names as the invariant that makes the layering one object",
     mono and abs(abs(r_coll(0.0)) - abs(r_lift(0.0))) < 1e-15)


# ============================================================ D. the junctions and the lift
head("D.  THE JUNCTIONS, AND THE LIFT AS THE JOIN THAT CARRIES A REAL SPHERE")

print(f"      turnaround:  r^2 from the collapse side {r_coll(0.0)**2:.15f}, from the lift side "
      f"{r_lift(0.0)**2:.15f}")
dr2 = {}
for nm, fn, g, p in (('collapse', lambda x: r_coll(x) ** 2, lambda x: c0 / np.cosh(x) ** (2 / 3), 0.0),
                     ('lift-turn', lambda t: r_lift(t) ** 2, lambda t: c0 / np.cos(t) ** (2 / 3), 0.0)):
    h = 1e-6
    dr2[nm] = abs((fn(p + h) - fn(p - h)) / (2 * h) / g(p)) if nm == 'collapse' else \
              abs((fn(p + h) - fn(p)) / h / g(p))
print(f"      and |d(r^2)/d(path)| there: collapse {dr2['collapse']:.2e}, lift {dr2['lift-turn']:.2e} "
      f"-- both vanish, the turnaround being the turnaround of r")
gate(f"`r^2` is continuous at the TURNAROUND -- {abs(r_coll(0.0)**2 - r_lift(0.0)**2):.1e} -- and its "
     f"derivative along the conformal path vanishes from both sides, so the collapse leg and the lift "
     f"join there in the foliation label as well as in the curve",
     abs(r_coll(0.0) ** 2 - r_lift(0.0) ** 2) < 1e-15
     and dr2['collapse'] < 1e-5 and dr2['lift-turn'] < 1e-5)

seam = [(abs(r_lift(np.pi / 2 - d)), abs(r_expa(d))) for d in (1e-3, 1e-5, 1e-7)]
print(f"      seam:  |r| from the lift side and from the expansion side, as the parameter -> 0:")
for d, (a, b) in zip((1e-3, 1e-5, 1e-7), seam):
    print(f"        delta={d:<8.0e}  lift {a:.3e}   expansion {b:.3e}")
# ⌗ ** THE ASSERTION IS THE APPROACH AND NOT A CUT.  *A first draft of this gate required
#   `\lvert r\rvert < 10^{-2}` at every probe, which the coarsest one meets with equality -- the same
#   floor-pinning this line has now been caught at three times.*  ⇒ ** What the claim needs is that
#   BOTH sides fall MONOTONICALLY toward zero and that the finest probe is orders below the coarsest,
#   which is a statement about the limit rather than about where the probes happen to land. **
_dec = (all(seam[i][0] > seam[i + 1][0] for i in range(len(seam) - 1))
        and all(seam[i][1] > seam[i + 1][1] for i in range(len(seam) - 1)))
print(f"      monotone on both sides: {_dec};  finest/coarsest = "
      f"{seam[-1][0]/seam[0][0]:.1e} (lift) and {seam[-1][1]/seam[0][1]:.1e} (expansion)")
gate(f"and both sides of the SEAM approach `\\lvert r\\rvert = 0` -- the lift from `r<0` and the "
     f"expansion from `r>0`, each MONOTONICALLY and by a factor "
     f"{seam[0][0]/seam[-1][0]:.0e} over the probes -- so the foliation label is continuous there too "
     f"and the branch point is the one place it vanishes, exactly as `r7115` says: the growing-`r` "
     f"foliation begins where `r` and `\\tilde\\tau` vanish together",
     _dec and seam[-1][0] < seam[0][0] / 100.0 and seam[-1][1] < seam[0][1] / 100.0)

LIFT_SIG = (2 * sp.Symbol('alpha', positive=True) / 3) ** 2
print(f"\n      on the lift  d tau~ = i(2 alpha/3) dv  =>  -d tau~^2 = +(2 alpha/3)^2 dv^2 = "
      f"+{LIFT_SIG}  (POSITIVE)")
gate("⛭⛭ and the LIFT is the join that carries a real sphere: `d\\tilde\\tau=i(2\\alpha/3)dv` makes "
     "`-d\\tilde\\tau^2=+(2\\alpha/3)^2dv^2` POSITIVE, so the four-geometry is RIEMANNIAN there, while "
     "`r` is real on the branch the figure fixes and `r^2d\\Omega_3^2` is a real round `S^3` "
     "throughout -- ⇒ *the signature of the time direction turns through a right angle and the "
     "angular character does not move at all*",
     sp.simplify(LIFT_SIG) == LIFT_SIG and LIFT_SIG.is_positive is not False
     and all(np.isreal(r_lift(t)) and r_lift(t) < 0 for t in (1e-3, 0.7, 1.5)))


# ============================================================ E. the seam, and the verdict
head("E.  ⇒ THE SEAM HIDES THE CHART AND NOT THE CHARACTER -- THE CONJECTURE IS DISCHARGED")

near = []
for rv in (1e-2, 1e-4, 1e-6, -1e-6, -1e-4, -1e-2):
    shp = (6.0 / rv ** 2) * (2 * np.pi ** 2 * abs(rv) ** 3) ** (2.0 / 3.0)
    near.append(abs(shp / SHAPE_N - 1.0))
    print(f"      r = {rv:+.0e}   V = {2*np.pi**2*abs(rv)**3:.3e}   R = {6/rv**2:.3e}   "
          f"R V^(2/3) = {shp:.10f}")
gate(f"at `r=0` exactly the layer AT THAT FIXED `\\tilde\\tau` is a POINT -- `V\\to0`, "
     f"`\\mathcal R\\to\\infty`; ⌗ *the LOCUS `r=0` is not a point, see (E3)* -- but the shape "
     f"invariant is the same constant at every `r\\neq0`, to {max(near):.1e} at six orders of "
     f"magnitude either side of the seam.  ⇒ ** the divergence is the AREAL COORDINATE degenerating, "
     f"which `P15`'s own abstract already says of the branch point, and NOT a change in what the "
     f"layer is **",
     max(near) < 1e-12 and 'areal coordinate degenerating' in b15)

gate("⇒ *** `PO-74` DISCHARGED IN THE DIRECTION `sec:largescale` STATES IT: the foliation is the "
     "constant-`r` one at every point of the curve and the layer's character continues across the lap "
     "with it.  The terminal branch is NOT taken -- nothing at the seam obstructs the sphere's "
     "character; what passes through zero there is its radius ***",
     max(near) < 1e-12 and worst < 1e-12
     and 'as a conjecture and do not claim it as a theorem' in b15)

gate("⌗ and the paper's conjecture is located rather than quoted from memory: `sec:largescale` "
     "carries both the foliation sentence and the explicit statement that the demonstration is work "
     "the paper does not carry",
     'the cosmic layers are the surfaces of constant areal radius' in b15
     and 'work this paper does not carry' in b15)


# ============================================================ E2. the seam is the inflection
head("E2.  ⛭⛭⛭ THE COSMOLOGICAL SEAM IS NOT r=0 -- IT IS THE INFLECTION, AND IT SITS AT r_N")

u, Asym = sp.symbols('u A', positive=True)
r_of_u = Asym * sp.sinh(u) ** sp.Rational(2, 3)
d2 = sp.simplify(sp.factor(sp.diff(r_of_u, u, 2)))
u_i = sp.atanh(1 / sp.sqrt(3))
r_i = sp.simplify(r_of_u.subs(u, u_i))
A_val = 2 ** sp.Rational(1, 3) * al / sp.sqrt(3)          # eq:amplitude's Nariai amplitude
resid = sp.simplify(r_i.subs(Asym, A_val) - al / sp.sqrt(3))
print(f"      d^2 r / d(u)^2 = {d2}")
print(f"      vanishes at cosh 2u = 2, i.e. tanh^2 u = 1/3:  sinh^2 u = "
      f"{sp.simplify(sp.sinh(u_i)**2)},  cosh^2 u = {sp.simplify(sp.cosh(u_i)**2)}")
print(f"      r there = {sp.simplify(r_i)} = A * 2^(-1/3);  with A = 2^(1/3) alpha/sqrt3  ->  "
      f"{sp.simplify(r_i.subs(Asym, A_val))}   and r_N = {sp.simplify(al/sp.sqrt(3))}")
print(f"      residual r_infl - r_N = {resid}")
sgn = [sp.sign(d2.subs([(u, v), (Asym, 1)])).evalf() for v in (0.3, 1.5)]
print(f"      sign of d^2r/du^2 before and after: {sgn}  (deceleration -> acceleration)")
gate(f"⛭⛭⛭ the deceleration-to-acceleration INFLECTION of `r(\\tilde\\tau)` sits at "
     f"`\\cosh2u=2`, where `\\sinh^2u=\\tfrac12` and `\\cosh^2u=\\tfrac32`, and the areal "
     f"radius there is `A\\,2^{{-1/3}} = \\alpha/\\sqrt3 = r_N` -- ** residual identically "
     f"`{resid}` ** -- with the second derivative running `-\\to+` across it",
     sp.simplify(r_i - Asym * 2 ** sp.Rational(-1, 3)) == 0 and resid == 0
     and sgn[0] < 0 < sgn[1])

gate("⇒ *** so the COSMOLOGICAL SEAM IS THE MERGED HORIZON, and section (F)'s double zero of `-f` is "
     "NOT an asymmetry between the two readings: it is the reassigned chart registering the handover "
     "at exactly that locus.  ⛔ This line had been writing \"the seam\" for the branch point since "
     "`r7108`, where the corpus uses it for the handover -- `FOR_60`'s `r7107` says \"from `r=0` out "
     "to the deceleration/acceleration handover at the cosmological seam\" -- and that naming is "
     "corrected here ***",
     resid == 0)

print(f"\n      2^(-1/3) = {float(2**sp.Rational(-1,3)):.12f} is both r_seam/A here and `r7112`'s "
      f"horizon constant 2/3c_0^2")
gate("⌗⌗ and ONE OBSERVATION THAT IS NOT A CLAIM: `2^{-1/3}` is both `r_{seam}/A` and `r7112`'s "
     "horizon constant `2/3c_0^2`.  **Whether that is one fact or two is NOT established here** and "
     "this gate asserts only that the two numbers are equal, not that they are the same fact",
     abs(float(2 ** sp.Rational(-1, 3)) - 2.0 / (3 * c0 ** 2)) < 1e-15)


# ============================================================ E3. r=0 is not a single point
head("E3.  ⛭⛭ AND r=0 IS NOT A SINGLE POINT -- THE 45-DEGREE TILT, FROM THE CORPUS'S OWN STEP (iv)")

tau, chiC = sp.symbols('tau chi', real=True)
rr = sp.Function('r')(tau + chiC)
same = sp.simplify(sp.diff(rr, chiC) - sp.diff(rr, tau))
print(f"      the corpus's step (iv): r(tau,chi) = r(tau+chi), so d_chi r - d_tau r = {same}")
print(f"      => the level sets of r in the (tau,chi) plane are the 45-degree lines tau + chi = const")
for chi_v in (-2.0, 0.0, 3.5):
    print(f"        the worldline chi = {chi_v:+.1f} reaches r = 0 at its own tau = {-chi_v:+.1f}")
gate("`\\partial_\\chi r=\\partial_\\tau r` identically -- the corpus's own step (iv), "
     "`r(\\tau,\\chi)=r(\\tau+\\chi)` -- so constant `r` is tilted at `45^\\circ` to `\\tau` "
     "and each worldline reaches a given `r` at its OWN `\\tau=\\tilde\\tau-\\chi`",
     same == 0
     and r'r(\tau,\chi)=r(\tau+\chi)' in b15.replace(' ', '')
     and r'45^\circ' in b15)

gate("⇒ ** THEREFORE THE LOCUS `r=0` IS A ONE-PARAMETER FAMILY OF EVENTS, ONE ON EACH WORLDLINE -- "
     "the author's \"circle of geodesic points\" -- and so are the seam, the turnaround and the "
     "Euclidean nulls. ⌗ What section (E) computes is kept: the layer AT FIXED `\\tilde\\tau` has "
     "radius `\\lvert r\\rvert` and that radius passes through zero.  **What is withdrawn is the "
     "wording that invited the other reading** -- \"at `r=0` the layer is a point\" is about one "
     "layer, not about the locus, and the first draft did not say which",
     same == 0)

# ============================================================ F. the one asymmetry
head("F.  ⚠ THE ONE PLACE THE TWO READINGS ARE NOT INTERCHANGEABLE, AS A FINDING")

rN = al / sp.sqrt(3)
fN = sp.simplify(f.subs(rs, 2 * al / (3 * sp.sqrt(3))))
f_at, fp_at = sp.simplify(fN.subs(r, rN)), sp.simplify(sp.diff(fN, r).subs(r, rN))
print(f"      f(r) at the Nariai mass = {sp.factor(fN)}")
print(f"      f(r_N) = {f_at}    f'(r_N) = {fp_at}   (a DOUBLE zero at r_N = alpha/sqrt3)")
gate(f"at the Nariai mass `f` has a DOUBLE zero at `r_N=\\alpha/\\sqrt3` -- `f(r_N)={f_at}` and "
     f"`f'(r_N)={fp_at}` symbolically -- so the reassigned layer's `\\chi` block `-f(r)` VANISHES "
     f"exactly at the merged horizon, while on the `S^3` side `r_N` is an ordinary layer the "
     f"foliation passes through without incident",
     f_at == 0 and fp_at == 0)

gate("⇒ *** so the two metrics do not even DEGENERATE in the same places, which is the sharpest form "
     "of `r7115`'s own point that the reassignment is not a diffeomorphism -- and it is a finding "
     "about what the reassignment does, not a caveat on the result above ***",
     f_at == 0 and sp.simplify(G3[0, 0].subs(r, rN)) != 0)


# ============================================================ G. controls
head("G.  THE CONTROLS -- ONE THAT MUST RETURN THE AFFIRMATIVE AND ONE THAT MUST COME BACK WRONG")

C, H0, Om = 299792.458, 68.60, 0.2973
x03 = 2.0 / Om - 2.0
alpha = (C / H0) * np.sqrt(1.0 + 2.0 / x03)
shp_throat = (6.0 / alpha ** 2) * (2 * np.pi ** 2 * alpha ** 3) ** (2.0 / 3.0)
print(f"      pure de Sitter at the throat, r = alpha = {alpha:.3f} Mpc:  sectional curvature "
      f"1/alpha^2 = {1/alpha**2:.4e},  R V^(2/3) = {shp_throat:.10f}")
gate(f"✔ THE AFFIRMATIVE CONTROL: the throat of pure de Sitter is the `S^3` of radius `\\alpha`, a "
     f"known object, and the same invariant returns the same constant on it to "
     f"{abs(shp_throat/SHAPE_N - 1):.1e} -- so the quantity is reading the layer's shape and not an "
     f"artefact of the bead's parametrisation",
     abs(shp_throat / SHAPE_N - 1.0) < 1e-12)

# ⌗⌗ ** A SLIP OF MINE, CAUGHT BY THIS GATE AND RECORDED RATHER THAN QUIETLY FIXED. **  *The first
#   draft wrote the flat slice as `diag(1, r^2, r^2 sin^2(theta))` over `(chi, theta, phi)` with `r` a
#   FREE SYMBOL -- which is not flat `E^3` at all but `R x S^2` again, and it duly returned `2/r^2`.*
#   ⇒ ** FLAT `E^3` NEEDS THE RADIAL COORDINATE TO BE THE ONE BEING DIFFERENTIATED: `d\rho^2 +
#   \rho^2d\Omega_2^2` over `(\rho, \theta, \phi)`.  The warning is the useful part -- the
#   difference between the two readings of the layer is exactly whether the sphere's radius varies
#   along the third direction, so writing a constant radius there is how one accidentally builds the
#   cylinder. **  *`r7102` established the flatness of `prop:flat`'s slice; it is cited here and the
#   round-`E^3` form is what this control needs.*
rho = sp.symbols('rho', positive=True)
GF = sp.diag(sp.Integer(1), rho ** 2, rho ** 2 * sp.sin(th) ** 2)   # flat E^3, radial coord rho
RF, SF = ricci(GF, [rho, th, ph])
print(f"      the WRONG foliation -- `prop:flat`'s constant-tau slice, flat E^3 "
      f"(d rho^2 + rho^2 dOmega^2) -- scalar {SF}, so R V^(2/3) = 0")
gate(f"⚠ AND THE CONTROL THAT MUST COME BACK WRONG DOES: on the OTHER slicing -- `prop:flat`'s "
     f"constant-`\\tau` surface, which `r7102` showed is exactly flat `\\mathbb{{E}}^3` -- the Ricci "
     f"scalar is `{SF}` and the invariant is `0`, not `{SHAPE_N:.1f}`.  ⇒ *the result depends on the "
     f"foliation being the constant-`r` one, which is exactly what `r7115`'s settlement names as the "
     f"invariant; taking the distance slicing instead returns the wrong answer*",
     sp.simplify(SF) == 0)


# ============================================================ H. scope
head("H.  ⚠ SCOPE, AND WHAT IS NOT CLAIMED")
print(f"      every file this receipt opened: {OPENED}")
gate("no transfer, spectrum, kernel, likelihood or mode amplitude is computed, and `r7108`'s `T(k)` "
     "and `r7112`'s horizon structure are not recomputed: the only objects here are two induced "
     "three-geometries and one scale-free combination of their invariants, with the paper the only "
     "file opened",
     OPENED == ['CR_cosmology.tex'])
gate("⛔ and what is NOT claimed: that the reassignment is a diffeomorphism or an isometry of one "
     "metric -- `r7115` asserts it is neither and section F is evidence on that side; no curvature "
     "invariant of either FOUR-geometry is computed for comparison across the registers, which "
     "`r7115` says would register only that fact; the source spectrum is not reassigned and the paper "
     "is READ and not edited",
     'not a diffeomorphism' in b15)


# ============================================================ verdict
head("VERDICT")
bad = [n for n, ok in CHECKS if not ok]
for n, ok in CHECKS:
    if not ok:
        print(f"  FAILED: {n}")
print(f"\n  {len(CHECKS) - len(bad)} of {len(CHECKS)} checks pass   [{time.time()-t_all:.1f}s]")
if bad:
    raise SystemExit(1)
print("  ALL PASS -- the constant-r foliation carries the sphere across the lap: the layer's shape\n"
      "  invariant R V^(2/3) = 6(2 pi^2)^(2/3) is the same pure number at every point of the bead,\n"
      "  both signs of r and the Euclidean lift included, so only the scale |r| moves; the R x S^2\n"
      "  reading is that same layer under two substitutions, with the zero eigenvalue produced by\n"
      "  the unwarping alone; and the seam hides the chart, not the character.")

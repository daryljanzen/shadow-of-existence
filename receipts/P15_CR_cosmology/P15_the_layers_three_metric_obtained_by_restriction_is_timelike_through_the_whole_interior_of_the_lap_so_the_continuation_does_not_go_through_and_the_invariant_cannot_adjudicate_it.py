#!/usr/bin/env python3
"""P15 receipt -- `PO-74`, the amended discharge, taken on the three clauses it names:
** the layer's three-metric inside the lap OBTAINED rather than written, `eq:shape-invariant`
MEASURED on it rather than evaluated on an input already round, and the `$\\chi$`-block coefficient
`$-f$` PRODUCED by applying the reassignment rather than selected to match. **

*** ⛭⛭⛭ ALL THREE ARE DONE, AND THE ANSWER IS THAT THE CONTINUATION DOES NOT GO THROUGH -- WHICH
    `PO-74`'s OWN TERMINATION CONDITION CALLS EQUALLY A RESULT:
      ⓵ THE THREE-METRIC IS OBTAINED BY RESTRICTING `eq:proper-frame` TO A CONSTANT-`$\\tilde\\tau$`
         SURFACE.  Nothing is posited: `$h=[(\\partial_\\chi r)^2-1]\\dd\\chi^2+r^2\\dd\\Omega^2$`.
      ⓶ `$-f$` IS PRODUCED, NOT MATCHED: the `$E=1$`, `$k=0$` radial equation gives
         `$(\\partial_\\chi r)^2=1-f$` IDENTICALLY, so the `$\\chi$` block IS `$-f$` by substitution.
      ⓷ AND THE MEASUREMENT IS DECISIVE AGAINST THE CONJECTURE, IN TWO INDEPENDENT WAYS. ***

** ⇒ FIRST: `eq:shape-invariant` IS NOT AN INVARIANT ON THE OBJECT THE FLOW DELIVERS. **
*Computed from the metric by this receipt's own curvature code -- validated first on a round `$S^3$`,
where it returns `$6\\cdot2^{2/3}\\pi^{4/3}=43.8232327$` with the radius CANCELLING -- the obtained layer
gives `$\\mathcal R=2/r^2$` and*

> ### `$\\mathcal R V^{2/3}=4\\cdot2^{1/3}\\pi^{2/3}L^{2/3}(-f)^{1/3}r^{-2/3}$`

*which carries the layer's SIZE as `$r^{-2/3}$` and, worse, carries the arbitrary coordinate extent
`$L$` of the `$\\chi$` line.*  ⇒ *** The quantity the paper offers as the test has no value on the
layer at all without choosing `$L$`, and is not scale-free once chosen.  Its defining property --
*"carries no `$r$` at all---it cancels symbolically"* -- holds on the `$S^3$` it was built for and
fails on the object a flow along the bead produces. ***

⛔ ** AND THERE IS A STRONGER REASON IN THE SAME EXPRESSION, WHICH IS THE ONE THAT SETTLES IT. **
*The volume carries `$\\sqrt{-f}$`, so the invariant needs `$-f>0$` -- and `$-f=-1$` at the turnaround.*
⇒ *** So `eq:shape-invariant` does not merely fail to be invariant inside the lap: it has no real value
there at all, because the layer has no Riemannian volume.  THAT is why the test cannot adjudicate the
continuation in either direction, and it is why the row could not have been settled by running it. ***

⌗ ** ONE PROPERTY OF THE INSTRUMENT, MEASURED BECAUSE A FIRST DRAFT OF THIS RECEIPT GOT IT WRONG AND
   THE GATE CAUGHT IT: ** *the first version asserted a non-zero slope at `$\\varepsilon=1$` and went
red.  **The round point is STATIONARY** -- `$g'(1)=0$` with `$g''(1)=-77.908<0$`, and `$\\varepsilon=1$`
is the only solution of `$g=43.8232$`.*  ⇒ *So the test is a strict MAXIMUM at roundness and its
sensitivity is SECOND order in the squashing, not first: sharp enough to be a test, and not as sharp as
a reader would assume.  `P15` does not say this and it bears on how much a near-miss would mean.*

⌗ ** AND THE CONTROL IS `70`'s OWN POINT, REPRODUCED AS A CHECK RATHER THAN CITED: ** *the layer's
Ricci diagonal comes back `$(0,1,\\sin^2\\theta)$` -- eigenvalues `$(0,1/r^2,1/r^2)$` -- with the
`$\\chi$`-block carried as a FREE SYMBOL that does not appear in the answer.  **So matching those
eigenvalues could never have discriminated anything**, and that is measured here rather than accepted.*

** ⇒ SECOND, AND THIS IS THE RESULT: THE LAYER IS **TIMELIKE** THROUGH THE WHOLE OF THE LAP'S
   INTERIOR, SO THERE IS NO SPATIAL THREE-METRIC THERE TO BE A SPHERE. **
*The cubic factorises exactly at the Nariai member:*

> ### `$-f=(r-\\alpha/\\sqrt3)^2(r+2\\alpha/\\sqrt3)/\\alpha^2r$`

*-- a DOUBLE root at `$+\\alpha/\\sqrt3$` and a simple root at `$-2\\alpha/\\sqrt3$`, and **those are the
lap's two unit-speed loci**, necessarily so: `$-f=(\\partial_\\chi r)^2-1$` makes `$-f=0$` and
`$\\lvert\\partial_\\chi r\\rvert=1$` the SAME condition.  ⇒ *So the sign of `$-f$` is the sign of
`$(r+2\\alpha/\\sqrt3)/r$`, and it is NEGATIVE on the whole stretch `$-2\\alpha/\\sqrt3<r<0$`* --

| where | `$-f$` | the layer |
|---|---|---|
| far collapse leg, `$\\lvert r\\rvert=3\\alpha$` | `$+7.8717$` | spacelike |
| **the back seam, `$r=-2\\alpha/\\sqrt3$`** | `$0$` | **null** |
| the turnaround, `$r=-A$` | **`$-1$` exactly** | **timelike** |
| mid-lift, `$r=-A/2$` | `$-1.9260$` | **timelike** |
| **the front seam, `$r=+\\alpha/\\sqrt3$`** | `$0$` | **null** |
| expansion leg, `$r=+A$` | `$+0.0583$` | spacelike |

⇒ *** AND THE ENTIRE LIFT LIES INSIDE THAT STRETCH: `$A=0.7274\\alpha$` against `$2/\\sqrt3=1.1547\\alpha$`.
    So the layer is Lorentzian from the back seam to the branch point -- across the turnaround and the
    whole Euclidean segment -- and a flow carrying a round `$S^3$` from a horn cannot deliver one
    there, because what it delivers is not a Riemannian three-metric. ***

⌗ ** THE TURNAROUND VALUE IS `$-1$` EXACTLY AND IT IS STRUCTURAL, NOT A COINCIDENCE: ** *`$-f=
(\\partial_\\chi r)^2-1$` and the turnaround is where `$\\partial_\\chi r=0$`, so the layer there is
exactly a UNIT-timelike line times `$S^2(A)$`.  **A Lorentzian product, computed rather than argued.***

** ⇒ AND THE PAPER'S OWN CLAUSE IS RIGHT ABOUT THE SUBSTRATE AND WRONG ABOUT THE CHART, WHICH IS THE
   SAME DISTINCTION THIS ARC HAS MADE THREE TIMES. **  *`sec:largescale` says the `$\\chi$` block
*"vanishes there with them, so that layer is null at the handover and nowhere else"*.  **It vanishes
TWICE on the signed chart**, at both seams -- and `r7134`'s translation makes those one substrate
point, `$-2\\alpha/\\sqrt3+\\sqrt3\\alpha=+\\alpha/\\sqrt3$` exactly.*  ⇒ *So *"nowhere else"* is a true
statement about the substrate and a false one about the chart, and the clause needs the lap's closure
to be read correctly.*

⚑ ** AND `r7134` IS CONFIRMED FROM A NEW DIRECTION, BY THE METRIC ITSELF. **  *`sec:largescale` says
*"Because the angular block enters only through `$r^2$` it is blind to the sign of `$r$`"*, which is
true of that block.  **But `$-f$` carries `$2M/r$`, which is ODD in `$r$`** -- so the two chart values
of equal `$\\lvert r\\rvert$` carry `$S^2$` factors of equal size and `$\\chi$` blocks that differ, at
`$\\lvert r\\rvert=A$` by `$-1$` against `$+0.0583$`: **opposite in SIGN.**  ⇒ *Equal `$\\lvert r\\rvert$`
is not the same layer, and now that is a statement about the three-metric rather than about a label.*

⌗ ** THE FLOW SATISFIES `r7134`'s CONSTRAINT, WHICH IS WHY IT IS THE RIGHT FLOW TO HAVE USED. **
*It is the `$\\tilde\\tau$` flow -- equivalently the SIGNED-`$r$` flow, since `$r(\\tilde\\tau)$` is
monotone across the whole lap -- so it does NOT fold the lap at `$r=0$` and does carry the layer along
the substrate.  Checked here on a dense sweep rather than assumed.*

** ⇒ SO `PO-74` TERMINATES ON ITS OWN STATED CONDITION. **  *The row reads: `TERMINATES IF the
continuation is shown not to go through, which is equally a result the papers would carry.`*  ⇒ *** It
does not go through, and the reason is not a failure of analytic continuation: the layer's causal
character changes at the back seam, so there is no spatial layer inside the lap for the sphere to
continue INTO.  `eq:shape-invariant` cannot adjudicate it either way, because it is not an invariant
there. ***

⛔ ** WHAT THIS RECEIPT DOES NOT DO. **  *It does not recompute `70`'s Berger measurement, which is
`70`'s and is CITED: the paper's own expression is located and checked to reduce to the round value at
`$\\varepsilon=1$` and to vary otherwise, and nothing more.  It does not claim the two presentations
are one metric -- the paper denies that and this receipt uses the denial.  It proposes no edit: the
`"nowhere else"` clause and the sign-blindness clause both want amending and that is the gate's.  It
says nothing about `PO-75`, and it computes no spectrum.*  ⌗ *It also does not claim the de~Sitter
presentation's `$S^3$` is wrong anywhere it is displayed -- outside the seam it stands untouched.*

** COMPUTES: the layer's three-metric by restricting `eq:proper-frame` to constant `$\\tilde\\tau$`; the
`$\\chi$` block from the `$E=1$`, `$k=0$` radial equation; the Ricci tensor and scalar of the result
from Christoffel symbols written here, validated first on a round `$S^3$` of free radius; the
shape-invariant combination on both and its derivatives in `$r$` and in the coordinate extent; the
cubic's factorisation and its two roots symbolically; `$-f$` at seven loci spanning the lap; and the
flow's monotonicity on a dense sweep.  *** THE ONLY NUMBERS PINNED ARE THE PAPER'S OWN `$43.8232$` and
its Berger expression, *** in the Nariai gauge the paper fixes (`$2M=2\\alpha/3\\sqrt3$`). **

⌗ *The guard this one leaves: ** a test's discriminating power has to be measured on the object the
test will be APPLIED to, not on the object it was designed for -- a quantity that is scale-free on one
and carries two scales on the other is not the same quantity twice. **

Written r7146 by node 60, on `r7145`'s queue, taking `PO-74` first as ordered.
Stated for reversal.
"""
import os
import re
import time

import numpy as np
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

r, al, chi, th, ph = sp.symbols('r alpha chi theta phi', real=True)
R0, eps = sp.symbols('R varepsilon', positive=True)
_M2 = 2 * al / (3 * sp.sqrt(3))                       # 2M at the Nariai member, the paper's gauge
f = 1 - _M2 / r - r ** 2 / al ** 2
_rN = al / sp.sqrt(3)
_rB = -2 * al / sp.sqrt(3)
_A = 2 ** sp.Rational(1, 3) * al / sp.sqrt(3)


def curvature(g, x):
    """Ricci tensor and scalar from Christoffel symbols written here, not imported."""
    n = len(x)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[l, s] * (sp.diff(g[s, i], x[j]) + sp.diff(g[s, j], x[i])
                                         - sp.diff(g[i, j], x[s])) / 2 for s in range(n)))
             for j in range(n)] for i in range(n)] for l in range(n)]
    Ric = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            Ric[i, j] = sp.simplify(
                sum(sp.diff(Gam[l][i][j], x[l]) for l in range(n))
                - sum(sp.diff(Gam[l][i][l], x[j]) for l in range(n))
                + sum(Gam[l][l][s] * Gam[s][i][j] for l in range(n) for s in range(n))
                - sum(Gam[l][j][s] * Gam[s][i][l] for l in range(n) for s in range(n)))
    return Ric, sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))


# ============================================ A. the clauses the discharge names
head("A.  THE CLAUSES THE DISCHARGE NAMES -- LOCATED IN `P15`, NOT RECALLED")

_PFRAME = r"ds^2=-d\tau^2+(\partial_\chi r)^2\,d\chi^2+r^2 d\Omega^2,"
_SUM = r"$r(\tau,\chi)=r(\tau+\chi)$, with $\partial_\chi r=\partial_\tau r$"
print(f"      `eq:proper-frame`: {b15.count(_PFRAME)}x;   the sum-dependence: {b15.count(_SUM)}x")
gate("Ⓐ① THE LINE ELEMENT THE LAYER IS RESTRICTED FROM IS LOCATED, WITH ITS SUM-DEPENDENCE -- "
     "`eq:proper-frame` and *\"`$r(\\tau,\\chi)=r(\\tau+\\chi)$`, with `$\\partial_\\chi r=\\partial_\\tau "
     "r$`\"*.  ⇒ *So the layer below is obtained from the paper's own metric*",
     b15.count(_PFRAME) == 1 and b15.count(_SUM) == 1)

_INV = r"\mathcal R\,V^{2/3}=6(2\pi^2)^{2/3}=43.8232\ldots"
_BERGER = (r"on a Berger sphere of squashing $\varepsilon$ the same combination is "
           r"$2\cdot2^{2/3}\pi^{4/3}\varepsilon^{2/3}(4-\varepsilon^2)$, which varies with the "
           r"squashing and takes the round value only at $\varepsilon=1$")
_OWED = (r"the three-metric of the layer inside the lap carried from the sphere the de~Sitter "
         r"presentation displays at a horn, rather than posited at each point of the bead")
print(f"      the invariant: {b15.count(_INV)}x;   the Berger discriminant: {b15.count(_BERGER)}x;   "
      f"what is owed: {b15.count(_OWED)}x")
gate("Ⓐ② THE TEST, ITS MEASURED DISCRIMINANT AND THE THING OWED ARE ALL LOCATED -- `$43.8232$`, the "
     "Berger expression, and *\"the three-metric of the layer inside the lap carried from the sphere "
     "the de~Sitter presentation displays at a horn, rather than posited\"*",
     b15.count(_INV) == 1 and b15.count(_BERGER) == 1 and b15.count(_OWED) == 1)

_EIG = (r"whose intrinsic Ricci eigenvalues are $(0,1/r^2,1/r^2)$---a flat line times a round $S^2$ "
        r"of radius $r(\tilde\tau)$, not a three-sphere")
_NULL = (r"the reassigned layer's $\chi$ block $-f=(\partial_\chi r)^2-1$ vanishes there with them, "
         r"so that layer is null at the handover and nowhere else")
_CONJ = r"We state the continuation as a conjecture and do not claim it as a theorem"
_BLIND = r"Because the angular block enters only through $r^2$ it is blind to the sign of $r$"
#: ⛭ AMENDED r7150 (60), AND IT IS THE SECOND INSTANCE OF THE SAME DEFECT IN THIS SEAT'S OWN FILES.
#: As first written this gate PINNED all four clauses at `count == 1` -- and two of the four are the
#: ones THIS ROW ASKED THE GATE TO CHANGE.  `r7147` changed them (the `nowhere else` clause corrected,
#: the sign-blindness clause replaced, both carrying this receipt's own results), so the gate went RED
#: ON THE SUCCESS OF ITS OWN WORK.  ⇒ That is exactly the break `r7140` had and `r7142` repaired, and
#: writing the repair into one receipt did not stop the next one reintroducing it: the lesson is the
#: PARTITION, not the pattern.  A clause this receipt reasons FROM may be pinned; a clause this
#: receipt asks to CHANGE must be enumerated over the states the paper may produce -- the fourth guard.
_STABLE = b15.count(_EIG) == 1 and b15.count(_CONJ) == 1       # reasoned FROM: pinned
_LANDED = 'P15_the_layers_three_metric_obtained_by_restriction_is_timelike' in b15
_ASKED = b15.count(_NULL) == 1 and b15.count(_BLIND) == 1      # asked to CHANGE: enumerated
_STATES = (_ASKED and not _LANDED) or _LANDED
print(f"      eigenvalues: {b15.count(_EIG)}x;   the `$-f$` clause: {b15.count(_NULL)}x;   "
      f"the conjecture: {b15.count(_CONJ)}x;   sign-blindness: {b15.count(_BLIND)}x;   "
      f"this row landed in `P15`: {_LANDED};   enumeration holds: {_STATES}")
gate("Ⓐ③ THE FOUR CLAUSES SECTIONS `D` TO `F` MEASURE AGAINST, **PARTITIONED BY WHAT THIS ROW DOES TO "
     "THEM**: the eigenvalues and the conjecture are reasoned FROM and are pinned; the *\"null at the "
     "handover and nowhere else\"* clause and *\"blind to the sign of `$r$`\"* are what this row ASKS "
     "TO CHANGE, so they are gated as an **ENUMERATION** -- before this row lands they stand as "
     "written; after it lands they are the gate's to set.  ** Red only where the sentences this "
     "receipt reasons from would not be the sentences it read **",
     _STABLE and _STATES)


# ============================================ B. the flow, and the metric obtained from it
head("B.  THE FLOW STATED, AND THE THREE-METRIC **OBTAINED** BY RESTRICTION -- NOTHING POSITED")

#: the flow is the tau~ flow along the bead.  On a constant-tau~ surface tau~ = tau + chi is fixed,
#: so d(tau) = -d(chi); substituting that into eq:proper-frame IS the restriction.
dchi_r = sp.Symbol('u', real=True)                       # stands for d_chi r, carried free
h_block = sp.simplify(-1 + dchi_r ** 2)                  # from -d(tau)^2 + (d_chi r)^2 d(chi)^2
print(f"      restricting `eq:proper-frame` to constant `$\\tilde\\tau$` (so `$\\dd\\tau=-\\dd\\chi$`) "
      f"gives the `$\\chi$` block {h_block}")
gate("Ⓑ① THE LAYER'S THREE-METRIC IS **OBTAINED**: on a constant-`$\\tilde\\tau$` surface "
     "`$\\dd\\tau=-\\dd\\chi$`, so `eq:proper-frame` restricts to "
     "`$h=[(\\partial_\\chi r)^2-1]\\dd\\chi^2+r^2\\dd\\Omega^2$`.  ⇒ ** No metric is written down at any "
     "point of the bead; the layer is what the paper's own line element leaves on the surface **",
     sp.simplify(h_block - (dchi_r ** 2 - 1)) == 0)

# the E = 1, k = 0 radial equation:  (dr/dtau~)^2 = 2M/r + r^2/alpha^2 = 1 - f
rad = _M2 / r + r ** 2 / al ** 2
print(f"      the `$E=1$`, `$k=0$` radial equation gives `$(\\partial_\\chi r)^2$` = {sp.simplify(rad)}"
      f" ;  `$1-f$` = {sp.simplify(1 - f)}")
gate("Ⓑ② AND `$-f$` IS **PRODUCED, NOT MATCHED**: the `$E=1$`, `$k=0$` radial equation gives "
     "`$(\\partial_\\chi r)^2=2M/r+r^2/\\alpha^2=1-f$` IDENTICALLY, so the `$\\chi$` block is "
     "`$(1-f)-1=-f$` by substitution.  ⇒ *** The coefficient the row required to be derived is derived "
     "from the congruence's own equation of motion, with no reference to any target eigenvalue. ***",
     sp.simplify(rad - (1 - f)) == 0)

#: r7134's constraint: the flow must not fold the lap at r = 0.  r(tau~) is monotone across the lap,
#: so the tau~ flow IS the signed-r flow -- checked on a dense sweep rather than asserted.
_tt = np.linspace(-6.0, 6.0, 400001)
_rr = (2 ** (1 / 3) / np.sqrt(3)) * np.cbrt(np.sinh(1.5 * _tt)) ** 2 * np.sign(np.sinh(1.5 * _tt))
_mono = bool(np.all(np.diff(_rr) > -1e-15))
print(f"      signed `$r(\\tilde\\tau)$` monotone over {_tt.size} samples spanning both legs: {_mono}")
gate("Ⓑ③ ** AND THE FLOW SATISFIES `r7134`'s CONSTRAINT, CHECKED RATHER THAN ASSUMED: ** signed "
     "`$r(\\tilde\\tau)$` is monotone across the whole lap, so the `$\\tilde\\tau$` flow IS the signed-"
     "`$r$` flow and does **not** fold the lap at `$r=0$`.  ⇒ *It carries the layer along the "
     "substrate, which is what the amended discharge requires of it*",
     _mono)


# ============================================ C. the instrument, validated before it is applied
head("C.  THE CURVATURE CODE VALIDATED ON A ROUND `$S^3$` BEFORE IT IS POINTED AT THE LAYER")

g3 = sp.diag(R0 ** 2, R0 ** 2 * sp.sin(chi) ** 2,
             R0 ** 2 * sp.sin(chi) ** 2 * sp.sin(th) ** 2)
_, Rs3 = curvature(g3, [chi, th, ph])
V3 = sp.integrate(sp.integrate(sp.integrate(sp.sqrt(g3.det()), (ph, 0, 2 * sp.pi)),
                               (th, 0, sp.pi)), (chi, 0, sp.pi))
INV3 = sp.simplify(Rs3 * V3 ** sp.Rational(2, 3))
print(f"      round `$S^3(R)$`: `$\\mathcal R$` = {Rs3};  `$V$` = {sp.simplify(V3)};  "
      f"`$\\mathcal R V^{{2/3}}$` = {INV3} = {float(INV3):.7f}")
gate(f"Ⓒ① THE CODE RETURNS `$\\mathcal R=6/R^2$`, `$V=2\\pi^2R^3$` AND "
     f"`$\\mathcal R V^{{2/3}}={float(INV3):.4f}$` WITH THE RADIUS **CANCELLING SYMBOLICALLY** -- the "
     f"paper's own `$43.8232$`.  ⇒ ** So the instrument is checked on the object the invariant was "
     f"built for, before being applied to the one it was not **",
     sp.simplify(sp.diff(INV3, R0)) == 0
     and sp.simplify(INV3 - 6 * (2 * sp.pi ** 2) ** sp.Rational(2, 3)) == 0
     and abs(float(INV3) - 43.8232327) < 1e-6)

_BER = 2 * 2 ** sp.Rational(2, 3) * sp.pi ** sp.Rational(4, 3) * eps ** sp.Rational(2, 3) * (4 - eps ** 2)
#: ⛭ A FIRST DRAFT OF THIS GATE ASSERTED A NON-ZERO SLOPE AT `$\\varepsilon=1$` AND WENT RED, which
#: is the gate catching the receipt: the round point is STATIONARY.  That is a property of the
#: instrument the paper does not state and it is worth stating, because it says how sharp the test is.
_rnd = 6 * (2 * sp.pi ** 2) ** sp.Rational(2, 3)
_g1 = sp.simplify(_BER.subs(eps, 1) - _rnd)
_dg1 = sp.simplify(sp.diff(_BER, eps).subs(eps, 1))
_ddg1 = sp.simplify(sp.diff(_BER, eps, 2).subs(eps, 1))
_only = sp.solve(sp.Eq(_BER, _rnd), eps)
print(f"      Berger at `$\\varepsilon=1$` minus the round value: {_g1};   first derivative: {_dg1};   "
      f"second: {_ddg1} = {float(_ddg1):.4f};   solutions of `$g=\\mathrm{{round}}$`: {_only}")
gate(f"Ⓒ② AND `70`'s BERGER MEASUREMENT IS **CITED, NOT RECOMPUTED** -- but the one thing this receipt "
     f"needs from it is measured and it CORRECTS this receipt's own first draft: the round point is "
     f"**STATIONARY**, `$g'(1)=0$` with `$g''(1)={float(_ddg1):.3f}<0$`, and `$\\varepsilon=1$` is the "
     f"ONLY solution of `$g=43.8232$`.  ⇒ *** So the test is a strict MAXIMUM at roundness and its "
     f"sensitivity is SECOND order in the squashing, not first -- sharp enough to be a test, and not as "
     f"sharp as a reader would assume. ***",
     _g1 == 0 and _dg1 == 0 and float(_ddg1) < 0 and _only == [1] and b15.count(_BERGER) == 1)


# ============================================ D. the measurement, and the test's failure on it
head("D.  `eq:shape-invariant` MEASURED ON THE OBTAINED LAYER -- AND IT IS NOT AN INVARIANT THERE")

w, Lc = sp.symbols('w L', positive=True)                 # w stands for the chi block, carried FREE
hl = sp.diag(w, r ** 2, r ** 2 * sp.sin(th) ** 2)
Ricl, Rl = curvature(hl, [chi, th, ph])
diag = [sp.simplify(Ricl[i, i]) for i in range(3)]
print(f"      obtained layer: Ricci diagonal = {diag};  `$\\mathcal R$` = {Rl}")
gate("Ⓓ① ** THE CONTROL `70` ASKED FOR, RUN RATHER THAN CITED: ** the layer's Ricci diagonal comes "
     "back `$(0,1,\\sin^2\\theta)$` -- eigenvalues `$(0,1/r^2,1/r^2)$` -- with the `$\\chi$` block a "
     "**free symbol that does not appear in the answer**.  ⇒ *** So reproducing those eigenvalues could "
     "never have discriminated anything about the `$\\chi$` block, which is `70`'s finding ⓶ measured "
     "from the inside. ***",
     diag[0] == 0 and sp.simplify(diag[1] - 1) == 0
     and sp.simplify(diag[2] - sp.sin(th) ** 2) == 0 and sp.simplify(Rl - 2 / r ** 2) == 0
     and sp.simplify(sp.diff(Rl, w)) == 0 and b15.count(_EIG) == 1)

#: `$r$` is carried SIGNED here, as it is on the lap, so sympy returns `$\\lvert r\\rvert^{4/3}/r^2$`
#: rather than `$r^{-2/3}$` -- the same thing for `$r>0$` and the honest form for the collapse leg.
rp = sp.Symbol('rho', positive=True)
Vl = sp.sqrt(w) * Lc * 4 * sp.pi * rp ** 2
INVl = sp.simplify(Rl.subs(r, rp) * Vl ** sp.Rational(2, 3))
dr = sp.simplify(sp.diff(INVl, rp))
dL = sp.simplify(sp.diff(INVl, Lc))
_shape = sp.simplify(INVl * rp ** sp.Rational(2, 3)
                     / (Lc ** sp.Rational(2, 3) * w ** sp.Rational(1, 3)))
print(f"      `$V$` = {sp.simplify(Vl)} ;  `$\\mathcal R V^{{2/3}}$` = {INVl}")
print(f"      stripped of `$L^{{2/3}}w^{{1/3}}r^{{-2/3}}$`: {_shape}")
print(f"      `$\\partial_r$` = {dr}  (zero: {dr == 0}) ;  `$\\partial_L$` = {dL}  (zero: {dL == 0})")
gate("Ⓓ② *** AND THE TEST FAILS ITS OWN DEFINING PROPERTY ON THE OBJECT THE FLOW DELIVERS: "
     "`$\\mathcal R V^{2/3}=4\\cdot2^{1/3}\\pi^{2/3}L^{2/3}w^{1/3}r^{-2/3}$` CARRIES THE LAYER'S SIZE AND "
     "THE ARBITRARY COORDINATE EXTENT `$L$` OF THE `$\\chi$` LINE, both derivatives non-zero. ***  ⇒ "
     "** The paper's *\"carries no `$r$` at all---it cancels symbolically\"* holds on the `$S^3$` and "
     "fails here **",
     dr != 0 and dL != 0
     and sp.simplify(_shape - 4 * 2 ** sp.Rational(1, 3) * sp.pi ** sp.Rational(2, 3)) == 0)

#: and the stronger reason, which falls out of the same expression: the volume form needs `$w>0$`.
_w_lift = sp.simplify(-f.subs(r, -_A))
gate(f"Ⓓ③ *** AND THERE IS A STRONGER REASON IN THE SAME EXPRESSION: `$V$` CARRIES `$\\sqrt w$`, SO THE "
     f"INVARIANT NEEDS `$w=-f>0$` -- AND `$w=-1$` AT THE TURNAROUND BY `Ⓔ⑤`. ***  ⇒ ** So "
     f"`eq:shape-invariant` is not merely non-invariant on the layer inside the lap: it has no real "
     f"value there at all, because the layer has no Riemannian volume. *That is why the test cannot "
     f"adjudicate the continuation in either direction.* **",
     sp.simplify(_w_lift + 1) == 0 and float(_w_lift.subs(al, 1)) < 0
     and sp.simplify(sp.diff(Vl, w)) != 0)


# ============================================ E. the obstruction, located exactly
head("E.  THE OBSTRUCTION: THE LAYER IS **TIMELIKE** THROUGH THE WHOLE INTERIOR OF THE LAP")

cubic = sp.factor(sp.expand(sp.simplify(-f * al ** 2 * r)))
print(f"      `$-f\\,\\alpha^2r$` factorises as {cubic}")
gate("Ⓔ① THE CUBIC FACTORISES EXACTLY AT THE NARIAI MEMBER: `$-f=(r-\\alpha/\\sqrt3)^2"
     "(r+2\\alpha/\\sqrt3)/\\alpha^2r$` -- a **double** root at the front seam and a **simple** root at "
     "`$-2\\alpha/\\sqrt3$`.  ⇒ *Two zeros on the signed chart, not one*",
     sp.simplify(cubic - (r - _rN) ** 2 * (r - _rB) / al ** 2 * al ** 2 / al ** 2) == 0
     or sp.simplify(sp.expand(-f * al ** 2 * r) - sp.expand((r - _rN) ** 2 * (r - _rB))) == 0)

gate("Ⓔ② AND THOSE TWO ZEROS ARE THE LAP'S TWO **UNIT-SPEED** LOCI NECESSARILY, NOT COINCIDENTALLY: "
     "`$-f=(\\partial_\\chi r)^2-1$` by `Ⓑ②`, so `$-f=0$` and `$\\lvert\\partial_\\chi r\\rvert=1$` are "
     "the SAME condition.  ⌗ *The seams were defined by unit speed at `r7132`; the layer's nullity is "
     "that definition rewritten*",
     sp.simplify(f.subs(r, _rN)) == 0 and sp.simplify(sp.diff(f, r).subs(r, _rN)) == 0
     and sp.simplify(f.subs(r, _rB)) == 0 and sp.simplify(rad.subs(r, _rN) - 1) == 0
     and sp.simplify(rad.subs(r, _rB) - 1) == 0)

LOCI = [("far collapse leg, |r|=3a", -3 * al), ("THE BACK SEAM", _rB), ("the turnaround, r=-A", -_A),
        ("mid-lift, r=-A/2", -_A / 2), ("THE FRONT SEAM", _rN), ("expansion leg, r=+A", _A),
        ("expansion leg, r=+3a", 3 * al)]
vals = []
for lab, v in LOCI:
    mf = sp.simplify(-f.subs(r, v))
    vals.append((lab, mf, float(mf.subs(al, 1))))
    print(f"      -f at {lab:26s} = {float(mf.subs(al, 1)):+.6f}   "
          f"{'NULL' if abs(float(mf.subs(al, 1))) < 1e-14 else ('timelike' if float(mf.subs(al, 1)) < 0 else 'spacelike')}")
gate("Ⓔ③ *** AND THE SIGN OF `$-f$` IS THE SIGN OF `$(r+2\\alpha/\\sqrt3)/r$`, SO THE LAYER IS "
     "**TIMELIKE** ON THE WHOLE STRETCH `$-2\\alpha/\\sqrt3<r<0$` -- `$-1$` exactly at the turnaround "
     "and `$-1.9260$` at mid-lift, against `$+7.87$` on the far collapse leg and `$+0.0583$` on the "
     "expansion leg. ***",
     abs(vals[0][2] - 7.8717) < 1e-3 and abs(vals[1][2]) < 1e-14
     and sp.simplify(vals[2][1] + 1) == 0 and abs(vals[3][2] + 1.925984) < 1e-5
     and abs(vals[4][2]) < 1e-14 and abs(vals[5][2] - 0.058267) < 1e-5 and vals[6][2] > 8)

gate(f"Ⓔ④ ** AND THE ENTIRE LIFT LIES INSIDE THAT STRETCH: `$A={float(_A.subs(al, 1)):.6f}\\alpha$` "
     f"against `$2/\\sqrt3={float(-_rB.subs(al, 1)):.6f}\\alpha$`. **  ⇒ *** So the layer is Lorentzian "
     f"from the back seam through the turnaround and the whole Euclidean segment to the branch point, "
     f"and no flow can deliver a round `$S^3$` there because what it delivers is not a Riemannian "
     f"three-metric at all. ***",
     float(_A.subs(al, 1)) < float(-_rB.subs(al, 1))
     and sp.simplify(-f.subs(r, -_A) + 1) == 0)

gate("Ⓔ⑤ ⌗ AND THE TURNAROUND VALUE IS `$-1$` **EXACTLY** AND STRUCTURAL: `$-f=(\\partial_\\chi r)^2-1$` "
     "and the turnaround is where `$\\partial_\\chi r=0$`, so the layer there is exactly a UNIT-timelike "
     "line times `$S^2(A)$` -- *a Lorentzian product, computed rather than argued*",
     sp.simplify(rad.subs(r, -_A)) == 0 and sp.simplify(-f.subs(r, -_A) + 1) == 0)


# ============================================ F. the two clauses this amends, and r7134 confirmed
head("F.  WHAT THE PAPER SAYS, READ AGAINST THE CHART AND AGAINST THE SUBSTRATE")

LAP = sp.sqrt(3) * al
gate("Ⓕ① *** THE *\"null at the handover and nowhere else\"* CLAUSE IS TRUE OF THE **SUBSTRATE** AND "
     "FALSE OF THE **CHART**: `$-f$` vanishes at BOTH seams, and `r7134`'s translation makes those one "
     "substrate point -- `$-2\\alpha/\\sqrt3+\\sqrt3\\alpha=+\\alpha/\\sqrt3$` exactly. ***  ⇒ *The same "
     "distinction this arc has made three times, now on the layer's own metric*",
     sp.simplify(_rB + LAP - _rN) == 0 and sp.simplify(f.subs(r, _rB)) == 0
     and sp.simplify(f.subs(r, _rN)) == 0 and _STATES)

_odd = sp.simplify(f.subs(r, -r) - f)
print(f"      `$f(-r)-f(r)$` = {_odd}  -- non-zero, so `$-f$` is NOT even in `$r$`")
gate("Ⓕ② ⚑ AND `r7134` IS CONFIRMED BY THE METRIC ITSELF, FROM A NEW DIRECTION: the angular block is "
     "even in `$r$` as the paper says, **but `$-f$` carries `$2M/r$`, which is ODD**, so the two chart "
     "values of equal `$\\lvert r\\rvert$` carry `$S^2$` factors of equal size and `$\\chi$` blocks of "
     "**opposite sign** at `$\\lvert r\\rvert=A$`, `$-1$` against `$+0.0583$`.  ⇒ ** Equal "
     "`$\\lvert r\\rvert$` is not the same layer, and that is now a statement about the three-metric "
     "rather than about a label **",
     _odd != 0 and sp.simplify(f.subs(r, _A) + f.subs(r, -_A) - 2 * (1 - _A ** 2 / al ** 2)) == 0
     and float((-f.subs(r, -_A)).subs(al, 1)) < 0 < float((-f.subs(r, _A)).subs(al, 1))
     and _STATES)

gate("Ⓕ③ ⬭ SO `PO-74` TERMINATES ON ITS OWN STATED CONDITION -- *the continuation is shown not to go "
     "through* -- and the paper's hedge is the right one to have carried: *\"We state the continuation "
     "as a conjecture and do not claim it as a theorem\"*.  ⌗ ** The reason is not a failure of "
     "analytic continuation but a change of causal character at the back seam, so there is no spatial "
     "layer inside the lap for a sphere to continue INTO **",
     b15.count(_CONJ) == 1 and float((-f.subs(r, -_A)).subs(al, 1)) < 0
     and dr != 0 and sp.simplify(sp.diff(INV3, R0)) == 0)


# ============================================ verdict
head("VERDICT")
_ok = sum(1 for _, v in CHECKS if v)
print(f"\n  {_ok} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
for nm, v in CHECKS:
    if not v:
        print(f"    FAILED: {nm}")
print()
raise SystemExit(0 if _ok == len(CHECKS) else 1)

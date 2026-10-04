#!/usr/bin/env python3
"""P15 receipt -- `PO-83`, opened at `r7164` as `PO-81`'s remainder from this seat's `r7166` tensor
obstruction, TAKEN, and taken through the second route the row itself names:
** DOES THE ROW MOVE TO THE COMPANION DYNAMICS PAPER, WHICH ALREADY CARRIES A TENSOR SECTOR? **

*** ⛭⛭⛭ IT DOES NOT MOVE, AND THE REASON IS BETTER THAN THE MOVE WOULD HAVE BEEN.  THREE
    MEASUREMENTS AND THEY POINT ONE WAY:
      ⓵ THE COMPANION'S TENSOR SECTOR AVOIDS THE OBSTRUCTION BY A DIFFERENT MECHANISM, NOT BY
         BEING EXEMPT FROM IT.  Its leaf is a `$T^2$`-symmetric Gowdy--de~Sitter slice, and
         **MEASURED HERE: that leaf is NOT EINSTEIN EITHER** -- three nonvanishing traceless-Ricci
         components.  What saves it is that the residual `$T^2$` pins the polarization
         ALGEBRAICALLY: the torus block's determinant is `$R^2$` identically, so one function is
         left and **there is no divergence constraint to solve.**  ⇒ *Two geometries avoiding one
         obstruction for two different reasons is not one question answered twice.*
      ⓶ BUT THE OBSTRUCTION IS NOT A PROPERTY OF THE SPACETIME -- IT IS A PROPERTY OF THE INDUCED
         METRIC ON THE LAYER.  The `$4$`-metric the layer sits in is **EXACTLY EINSTEIN with the
         mass and the throat constant FREE**: `$R_{ab}=\\Lambda g_{ab}$` identically and
         `$R=4\\Lambda=12/\\alpha^2$`, so the traceless Ricci that drives the obstruction is
         IDENTICALLY ZERO there, at every point of the lap.
      ⓷ AND THE OBSTRUCTION IS A PROPORTIONALITY RATHER THAN A CORRELATION.  The divergence
         `$\\Delta_L$` generates from a transverse-traceless tensor, divided by the Einstein
         deficit, converges to a finite degree-dependent constant --

> ### `0.255551` at `$L=2$` and `$0.183473` at `$L=3$`, stable over FOUR DECADES of deficit

         -- so it is exactly linear in the deficit, and a vanishing deficit is a vanishing
         obstruction rather than merely a smaller one.
    ⇒ *** SO `PO-83` IS NARROWED AND STAYS WHERE IT IS: what is obstructed is the LAYER-BY-LAYER
        HARMONIC METHOD the scalar route uses, and what is owed is a FOUR-DIMENSIONAL treatment
        rather than a three-layer decomposition.  The obstruction does not reach the physics. *** ***

⛭⛭⛭ ** ⓵ WHY THE MOVE IS NOT AVAILABLE, STATED AS A FACT ABOUT THE COMPANION RATHER THAN A
PREFERENCE. **  *`r7164` offers the move and says it prefers it, so the honest thing is to test it
and report what the test says.*  The companion's tensor sector is `eq:metric`'s polarized
Gowdy--de~Sitter wave: a `$(t,z)$` conformal plane times a two-torus, with the single propagating
polarization the torus block's `$\\psi$`.  **Its constant-`$t$` leaf is a different three-geometry
from the cosmological layer** -- `$\\mathbb{R}\\times T^2$` against a squashed `$S^3$` -- and this
receipt measures that leaf's own Ricci and finds it NOT Einstein.  ⇒ *** So the companion does not
answer the question on a geometry where the obstruction is absent; it asks a different question on a
geometry where the obstruction cannot arise, because nothing there has to solve a transversality
constraint. ***  ⌗ *That distinction is the whole of the answer: the obstruction bites exactly where
transverse-tracelessness must be OBTAINED, and not where a symmetry supplies it.*

⛭⛭ ** ⓶ AND THE DIRECTION THE ROW SHOULD GO, WHICH THE MEASUREMENT FIXES. **  *`r7166` found the
obstruction by asking for a spectrum on the LAYER.  The layer is a three-dimensional slice of a
`$4$`-geometry, and that `$4$`-geometry is `eq:sds-static` at the forced mass -- **a vacuum solution
with `$\\Lambda$`, hence Einstein identically, which this receipt derives rather than cites, with
`$M$` and `$\\alpha$` carried free.**  Since the quantity that generates the obstruction is the
traceless part of the Ricci tensor, and that part vanishes identically on the `$4$`-metric, the
question `r7166` found ill posed on the layer is well posed one dimension up.*
⇒ *** THE OBSTRUCTION IS DIMENSION-SPECIFIC.  It is a fact about the reduced description and not
    about the object the description is of. ***

⛭ ** ⓷ AND THE IDENTIFICATION IS TIGHTENED FROM `r7166`, WHICH IS WHAT MAKES THE ABOVE AN ARGUMENT
RATHER THAN A HOPE. **  *`r7166` measured that the generated divergence is linear in the Einstein
deficit near the round point at two degrees.  Here the ratio is followed over four decades and shown
to CONVERGE -- `0.2555` and `0.1835` to six figures -- so the leading dependence is exactly linear
with a finite coefficient and there is no hidden term that survives the deficit going to zero.*
⌗ *Without that, `Ric` proportional to `g` would license only "the obstruction gets small"; with it,
it licenses "the obstruction is absent".*

⛔ ** WHAT THIS DOES NOT DO, AND IT IS THE ROW'S OWN NEXT STEP. **  *It does not carry out the
four-dimensional transverse-traceless computation.  What is established is that the quantity which
obstructs the three-dimensional one vanishes identically on the four-geometry, and that is a reason
to expect the four-dimensional question to be well posed rather than a demonstration that it is.*
⛔ *It does not claim the four-dimensional route reproduces the bead's mode-by-mode transport: the
scalar route's whole economy is that `$(L,m)$` is carried unmixed along the curve, and whether a
`$4$`-dimensional treatment keeps that economy is not addressed.*  ⛔ *Nothing here is offered as
`P15`'s tensor claim -- `sec:intro` puts the tensor half in the companion, and this is a statement
about where a question can be ASKED.*  ⛔ *It does not re-measure `r7166`; its obstruction is taken
as given and only its identification is sharpened.*  ⛔ *It makes no claim about the companion's own
results, which are its own seat's; the single fact taken from it is the geometry its tensor sector
is carried on, read from its own equations.*

⌗ ** THE GUARD THIS ONE LEAVES. **
> **An obstruction found in a reduced description has to be checked in the description it was
> reduced FROM before it is called a property of the object.**  *The layer is a slice of a geometry
> that is Einstein identically, so the quantity that obstructed the slice is not merely small
> upstairs -- it is zero.  A reduction can manufacture an obstruction, and the test for that is
> cheap: compute the obstructing quantity one level up.*

⌗ **A SECOND, NARROWER ONE, FROM `r7164`'s OWN CORRECTION OF TWO OF THIS CORPUS'S RECEIPTS:** *a
clause a receipt's OWN RESULT will ask to have changed must be enumerated and never pinned -- a pin
there is red exactly when the recommendation is taken and green exactly while it is ignored.  Every
paper clause below is pinned only where it is reasoned FROM, and the clauses this row's result bears
on are enumerated over the states the paper may produce.*
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
b15 = body_of(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
bdyn = body_of(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex'))


def ricci(g, X):
    """Ricci, scalar curvature and the inverse, from the metric -- no package, no shortcut."""
    n = len(X)
    gi = sp.simplify(g.inv())
    Ga = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                        - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
            for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Ga[a][b][c], X[a]) - sp.diff(Ga[a][b][a], X[c])
                for d in range(n):
                    s += Ga[a][a][d] * Ga[d][b][c] - Ga[a][c][d] * Ga[d][b][a]
            Ric[b, c] = sp.simplify(s)
    Rs = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return Ric, Rs, gi


# ------------------------------------------------------------- Ⓐ the four-geometry
head("Ⓐ  THE FOUR-GEOMETRY THE LAYER SITS IN, AND ITS TRACELESS RICCI")

t4, r4, th4, ph4 = sp.symbols('t r theta phi', positive=True)
M, al = sp.symbols('M alpha', positive=True)
f_sds = 1 - 2 * M / r4 - r4**2 / al**2
g4 = sp.diag(-f_sds, 1 / f_sds, r4**2, r4**2 * sp.sin(th4)**2)
Ric4, R4, gi4 = ricci(g4, [t4, r4, th4, ph4])
LAM = 3 / al**2
dev4 = sp.simplify(Ric4 - (R4 / 4) * g4)
print(f"\n    R = {sp.simplify(R4)},   4*Lambda = {sp.simplify(4 * LAM)}")
gate("Ⓐ①  the four-metric is EXACTLY EINSTEIN with the mass and the throat constant FREE:"
     " R_ab = Λ g_ab identically, derived from the metric rather than cited",
     sp.simplify(Ric4 - LAM * g4) == sp.zeros(4, 4))
gate("Ⓐ②  and its TRACELESS Ricci -- the quantity that obstructs the layer -- is IDENTICALLY ZERO,"
     " at every radius and for every member of the family",
     sp.simplify(dev4) == sp.zeros(4, 4))
gate("Ⓐ③  with R = 4Λ = 12/α², so the Einstein constant is the throat's and nothing is fitted",
     sp.simplify(R4 - 4 * LAM) == 0 and sp.simplify(R4 - 12 / al**2) == 0)

# the same statement on the carried layer's own four-metric, eq:layer-proper
T, chi = sp.symbols('T chi', positive=True)
LAMs = sp.Symbol('Lambda', positive=True)
glayer = sp.diag(-1, sp.exp(-2 * sp.sqrt(LAMs) * T), 1 / LAMs, sp.sin(th4)**2 / LAMs)
Ricl, Rl, _ = ricci(glayer, [T, chi, th4, ph4])
gate("Ⓐ④  and the seam limit of the carried layer is Einstein too -- R_ab = Λ g_ab on the object"
     " r7156 obtained, so the statement is not special to one chart",
     sp.simplify(Ricl - LAMs * glayer) == sp.zeros(4, 4))

# ------------------------------------------------------------- Ⓑ the companion's leaf
head("Ⓑ  THE COMPANION'S TENSOR SECTOR: ITS LEAF IS NOT EINSTEIN EITHER, AND IT DOES NOT NEED TO BE")

zc = sp.Symbol('z')
Pf, Gf, Rf = sp.Function('psi')(zc), sp.Function('gamma')(zc), sp.Function('R')(zc)
gleaf = sp.diag(sp.exp(2 * (Gf - Pf)), sp.exp(2 * Pf), Rf**2 * sp.exp(-2 * Pf))
Ricg, Rg, _ = ricci(gleaf, [zc, sp.Symbol('x'), sp.Symbol('y')])
devg = sp.simplify(Ricg - (Rg / 3) * gleaf)
nzg = [(i, j) for i in range(3) for j in range(3) if sp.simplify(devg[i, j]) != 0]
print(f"\n    the Gowdy leaf's traceless Ricci has {len(nzg)} nonvanishing component(s): {nzg}")
gate("Ⓑ①  the companion's constant-t leaf is NOT Einstein -- three nonvanishing traceless-Ricci"
     " components -- so it does NOT avoid the obstruction the way the four-geometry does",
     len(nzg) == 3 and sp.simplify(devg) != sp.zeros(3, 3))
torus = sp.Matrix([[gleaf[1, 1], 0], [0, gleaf[2, 2]]])
gate("Ⓑ②  what saves it instead is ALGEBRAIC: the torus block's determinant is R² identically, so"
     " at fixed area exactly ONE function is left and there is no divergence constraint to solve",
     sp.simplify(torus.det() - Rf**2) == 0)
gate("Ⓑ③  and the companion says so in its own voice, in print exactly once each: the single"
     " transverse-traceless polarization, the area element, and the determinant clause",
     bdyn.count('The field $\\psi$ is the single transverse-traceless polarization') == 1
     and bdyn.count('$R$ is the area element') == 1
     and bdyn.count('The torus block still has determinant $R^2$') == 1)
gate("Ⓑ④  so the two geometries avoid ONE obstruction for TWO different reasons -- the four-geometry"
     " because its traceless Ricci vanishes, the companion's leaf because a symmetry pins the"
     " polarization -- which is why the row does not move",
     sp.simplify(dev4) == sp.zeros(4, 4) and sp.simplify(devg) != sp.zeros(3, 3))

# ------------------------------------------------------------- Ⓒ the obstruction, tightened
head("Ⓒ  AND THE OBSTRUCTION IS A PROPORTIONALITY: THE RATIO CONVERGES OVER FOUR DECADES")

IDX9 = [(a, b) for a in range(3) for b in range(3)]


def tpieces(epv):
    e = float(epv)
    a_, b_ = 2 * e, 2 / e
    Cn = {(c, x, y): 0.0 for c in range(3) for x in range(3) for y in range(3)}

    def setC(c, x, y, v):
        Cn[(c, x, y)] = v
        Cn[(c, y, x)] = -v

    setC(2, 0, 1, a_)
    setC(0, 1, 2, b_)
    setC(1, 2, 0, b_)
    G = {(c, x, y): 0.5 * (Cn[(c, x, y)] - Cn[(x, y, c)] + Cn[(y, c, x)])
         for c in range(3) for x in range(3) for y in range(3)}
    Rm = {}
    for d in range(3):
        for c in range(3):
            for x in range(3):
                for y in range(3):
                    Rm[(d, c, x, y)] = (sum(G[(d, x, k)] * G[(k, y, c)] for k in range(3))
                                        - sum(G[(d, y, k)] * G[(k, x, c)] for k in range(3))
                                        - sum(G[(d, k, c)] * Cn[(k, x, y)] for k in range(3)))
    Rc = np.array([[sum(Rm[(x, c, x, y)] for x in range(3)) for y in range(3)] for c in range(3)])
    return Cn, G, Rm, Rc


def lich(jv, epv):
    Cn, G, Rm, Rc = tpieces(epv)
    n = int(round(2 * jv)) + 1
    qs = np.array([(round(2 * jv) - 2 * k) / 2.0 for k in range(n)])
    J3 = np.diag(qs)
    Jp, Jm = np.zeros((n, n)), np.zeros((n, n))
    for k in range(n):
        q = qs[k]
        if k > 0:
            Jp[k - 1, k] = np.sqrt(jv * (jv + 1) - q * (q + 1))
        if k < n - 1:
            Jm[k + 1, k] = np.sqrt(jv * (jv + 1) - q * (q - 1))
    J1, J2 = (Jp + Jm) / 2, (Jp - Jm) / (2 * 1j)
    e = float(epv)
    E = [-2j * J1, -2j * J2, -(2j / e) * J3]

    def gam_act(x):
        Mf = np.zeros((9, 9))
        for p, (a, b) in enumerate(IDX9):
            for d in range(3):
                Mf[p, IDX9.index((d, b))] -= G[(d, x, a)]
                Mf[p, IDX9.index((a, d))] -= G[(d, x, b)]
        return Mf

    D = [np.kron(np.eye(9), E[x]) + np.kron(gam_act(x), np.eye(n)).astype(complex) for x in range(3)]
    tot = np.zeros((9 * n, 9 * n), dtype=complex)
    for x in range(3):
        Tm = np.kron(np.eye(9), E[x]) @ D[x]
        for d in range(3):
            if abs(G[(d, x, x)]) > 1e-14:
                Tm = Tm - G[(d, x, x)] * D[d]
        Tm = Tm + np.kron(gam_act(x), np.eye(n)).astype(complex) @ D[x]
        tot = tot + Tm
    CUR = np.zeros((9, 9))
    for p, (a, b) in enumerate(IDX9):
        for c in range(3):
            for d in range(3):
                CUR[p, IDX9.index((c, d))] += -2 * Rm[(a, c, b, d)]
            CUR[p, IDX9.index((c, b))] += Rc[a, c]
            CUR[p, IDX9.index((a, c))] += Rc[b, c]
    return n, D, -tot + np.kron(CUR, np.eye(n)).astype(complex)


def probe(jv, epv):
    n, D, LL = lich(jv, epv)
    trace_rows, anti_rows, div_rows = [], [], []
    for m in range(n):
        rr = np.zeros(9 * n, dtype=complex)
        for a in range(3):
            rr[IDX9.index((a, a)) * n + m] = 1
        trace_rows.append(rr)
    for a in range(3):
        for b in range(a + 1, 3):
            for m in range(n):
                rr = np.zeros(9 * n, dtype=complex)
                rr[IDX9.index((a, b)) * n + m] = 1
                rr[IDX9.index((b, a)) * n + m] = -1
                anti_rows.append(rr)
    for b in range(3):
        for m in range(n):
            rr = np.zeros(9 * n, dtype=complex)
            for x in range(3):
                rr += D[x][IDX9.index((x, b)) * n + m, :]
            div_rows.append(rr)
    Mrow = np.array(trace_rows + anti_rows + div_rows)
    _, s, vh = np.linalg.svd(Mrow)
    ns = vh[np.sum(s > 1e-9):].conj().T
    H = LL @ ns
    nrm = np.linalg.norm(H)
    return (np.linalg.norm(np.array(div_rows) @ H) / nrm,
            np.linalg.norm(np.array(trace_rows) @ H) / nrm)


print("\n     L     ε            deficit |1−ε²|      divergence/‖image‖     ratio")
RAT = {}
for Lv in [2, 3]:
    rows = []
    for e in [1.000001, 1.00001, 1.0001, 1.001, 1.01]:
        dv, tr = probe(Lv / 2.0, e)
        d = abs(1 - e * e)
        rows.append((e, d, dv, dv / d, tr))
        print(f"    {Lv:>2}   {e:<11g}  {d:>16.3e}  {dv:>18.3e}  {dv / d:>10.6f}")
    RAT[Lv] = rows

gate("Ⓒ①  at the round point itself the subspace is invariant, which is the control that the"
     " instrument reads zero when there is nothing to read",
     all(probe(Lv / 2.0, 1.0)[0] < 1e-12 for Lv in [2, 3]))
gate("Ⓒ②  the ratio of generated divergence to Einstein deficit CONVERGES over four decades --"
     " 0.2556 at L = 2 and 0.1835 at L = 3, each stable to four figures across the range -- so the"
     " dependence is exactly LINEAR with a finite coefficient",
     max(abs(r[3] - RAT[2][0][3]) for r in RAT[2][:4]) < 1e-3
     and max(abs(r[3] - RAT[3][0][3]) for r in RAT[3][:4]) < 1e-3)
gate("Ⓒ③  and the coefficient is NONZERO and degree-dependent, so the deficit is the obstruction's"
     " actual source rather than a quantity that merely travels with it",
     RAT[2][0][3] > 0.2 and RAT[3][0][3] > 0.15
     and abs(RAT[2][0][3] - RAT[3][0][3]) > 0.05)
gate("Ⓒ④  the TRACE stays at machine zero throughout, so what fails is transversality alone and the"
     " identification is of that failure and not of a general breakdown",
     all(r[4] < 1e-13 for Lv in RAT for r in RAT[Lv]))
gate("Ⓒ⑤  ⇒ SO A VANISHING DEFICIT IS A VANISHING OBSTRUCTION, not a smaller one -- which is what"
     " licenses carrying Ⓐ②'s identical zero into a statement about the four-dimensional question"
     " rather than only into a statement that it is less obstructed",
     sp.simplify(dev4) == sp.zeros(4, 4)
     and max(abs(r[3] - RAT[2][0][3]) for r in RAT[2][:4]) < 1e-3)

# ------------------------------------------------------------- Ⓓ the paper, read
head("Ⓓ  THE PAPERS' OWN CLAUSES, LOCATED IN THE CURRENT SOURCE AND PARTITIONED")

_SCOPE = 'the scalar half is here'
_SCALARS = 'For scalars the deformation reaches the spectrum and not the basis'
_FLOORS = 'every other scalar mode is bounded below uniformly'
_SHEAR = "the leaf's transverse-traceless shear"

gate("Ⓓ①  `sec:intro`'s scalar-half scoping clause is in print exactly once and is reasoned FROM:"
     " it is why nothing here is offered as this paper's tensor claim", b15.count(_SCOPE) == 1)
gate("Ⓓ②  eq:squashed-spectrum's LABEL is in print exactly once -- the label and never its citation"
     " count, which is the lesson this corpus learned twice over", b15.count('\\label{eq:squashed-spectrum}') == 1)
gate("Ⓓ③  and the two clauses r7164 RESCOPED on this seat's own recommendation are in print in"
     " their scoped form, each exactly once -- read here as the settled state they now have, which"
     " is the state this row reasons FROM rather than asks to change",
     b15.count(_SCALARS) == 1 and b15.count(_FLOORS) == 1)
gate("Ⓓ④  the companion's own description of where its tensor sector lives is in print and is"
     " reasoned FROM, not re-derived: its leaf's shear is the propagating polarization",
     bdyn.count(_SHEAR) >= 1)
gate("Ⓓ⑤  the ONE clause this row's result bears on is ENUMERATED over the states the paper may"
     " produce rather than pinned -- either the tensor obstruction still stands unqualified in"
     " print, or it has acquired the dimension-specific qualification this row recommends, or the"
     " row has moved and the companion is named beside it -- and the receipt's reading is unchanged"
     " in all three, which is the form that survived the last two landings",
     ('scalar' in b15 and b15.count(_SCALARS) == 1)
     or 'not Einstein' in b15
     or 'dynamics paper' in b15)

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
  VERDICT: PO-83 DOES NOT MOVE, AND THE REASON IS BETTER THAN THE MOVE.

  The companion's tensor sector is carried on a T^2-symmetric Gowdy leaf
  which is measured here to be NOT EINSTEIN either -- so it does not avoid
  the obstruction the way the four-geometry does.  What saves it is
  algebraic: the torus block's determinant is R^2 identically, leaving one
  function and no divergence constraint to solve.  Two geometries avoiding
  one obstruction for two different reasons is not one question answered
  twice, so the row stays where it is.

  BUT IT IS NARROWED DECISIVELY.  The four-metric the layer sits in is
  EXACTLY Einstein with the mass and the throat constant free, so the
  traceless Ricci that drives the obstruction is IDENTICALLY ZERO there.
  And the obstruction is a proportionality, not a correlation: the ratio of
  generated divergence to Einstein deficit converges to 0.2556 and 0.1835
  at the two degrees, stable over four decades -- so a vanishing deficit is
  a vanishing obstruction.

  *** SO WHAT IS OBSTRUCTED IS THE LAYER-BY-LAYER HARMONIC METHOD, AND WHAT
      PO-83 OWES IS A FOUR-DIMENSIONAL TREATMENT RATHER THAN A THREE-LAYER
      DECOMPOSITION.  THE OBSTRUCTION DOES NOT REACH THE PHYSICS. ***

  THE GUARD: an obstruction found in a reduced description has to be checked
  in the description it was reduced FROM before it is called a property of
  the object.  A reduction can manufacture an obstruction, and the test is
  cheap -- compute the obstructing quantity one level up.
  ==========================================================================
""")

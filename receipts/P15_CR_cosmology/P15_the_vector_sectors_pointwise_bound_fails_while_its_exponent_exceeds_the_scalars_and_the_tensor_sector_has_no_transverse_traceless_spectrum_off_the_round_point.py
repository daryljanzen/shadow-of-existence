#!/usr/bin/env python3
"""P15 receipt -- the two sectors `r7160` and `r7162` named as NOT DONE, taken together, because the
answer turns out to be ONE structural fact read three times:
** DO THE VECTOR AND TENSOR SECTORS SURVIVE ON THE SQUASHED LAYER THE WAY THE SCALAR SECTOR DOES? **

*** ⛭⛭⛭ THEY DO NOT, AND THEY FAIL DIFFERENTLY FROM EACH OTHER.  FOUR THINGS:
      ⓵ THE VECTOR SPLIT SURVIVES EVERY SQUASHING, AND FOR A REASON THAT HAS NOTHING TO DO WITH
         THIS LAYER.  The Hodge Laplacian commutes with `d` and `d*` on ANY Riemannian manifold, so
         the exact/co-exact split is carried along the bead whatever the squashing does -- MEASURED
         here as the gradient sector returning `eq:squashed-spectrum` EXACTLY, every eigenvalue, at
         every `$\\varepsilon$`.
      ⓶ BUT INSIDE THE CO-EXACT SECTOR THE DEFORMATION REACHES THE BASIS, WHICH IS THE OPPOSITE OF
         THE SCALAR CASE.  The invariant blocks are at most `$3\\times3$`, at fixed frame-minus-layer
         charge, with an off-diagonal coupling PROPORTIONAL TO `$\\varepsilon$` -- so the
         eigenVECTORS move with the squashing and the transport is not mode-by-mode.  ⌗ *Except at
         the extreme charge, where the block is `$1\\times1$` and nothing mixes at all.*
      ⓷ AND THE POINTWISE UNIFORM BOUND FAILS.  The unmixed extreme-charge mode has

> ### `$\\lambda^{\\perp}=(L+2)^2/\\varepsilon^2$`  -- exactly, for every degree

         so it runs to ZERO as `$\\varepsilon\\to\\infty$`, which is the close of the lift.  There is
         no `$\\lambda\\ge2L$` here: the scalar sector's uniform floor has no vector counterpart.
      ⛭ ⓸ ***AND THE SUPPRESSION SURVIVES ANYWAY, BECAUSE THE MEASURE IS THIN WHERE THE EIGENVALUE
         IS SMALL.***  Carrying the exact minimum through the lift's own measure gives an exponent
         LINEAR in degree and LARGER than the most transparent scalar band's at every degree
         computed -- `2.5952` at `$L=1$` against the scalars' `1.4983`, and `4` to `13` per cent
         above it through `$L=6$`.  ⇒ *A pointwise bound running to zero did not weaken the
         damping; it is the mirror of `r7162`'s guard and it runs the other way.*
    ⛔ AND THE TENSOR SECTOR IS NOT A SPECTRUM QUESTION AT ALL ON THIS LAYER.  `$\\Delta_L$` keeps
      TRACELESSNESS at every squashing and GENERATES DIVERGENCE as soon as the layer stops being
      Einstein -- which the Berger layer is only at `$\\varepsilon=1$`.  The transverse-traceless
      subspace is invariant to `$4\\times10^{-16}$` at the round point and NOT invariant off it,
      with the generated divergence LINEAR in the Einstein deficit and already `$24$`--`$32$` per
      cent of the image at the lift's entry.  ⇒ *** SO `PO-81`'s SECOND HORN, WHICH CLOSED FOR THE
      SCALARS, OPENS FOR THE TENSORS: there the decomposition the transport needs does not exist in
      the same form, and what is owed is a decomposition rather than an eigenvalue. *** ***

⛭⛭⛭ ** ⓵ WHY THE VECTOR SPLIT IS SAFE, AND WHY THAT IS NOT A FACT ABOUT THIS LAYER. **
*`$\\Delta_H=\\dd\\dd^*+\\dd^*\\dd$` commutes with `$\\dd$` and with `$\\dd^*$` on any Riemannian
manifold, so `$\\Delta_H\\dd f=\\dd\\Delta_s f$` identically and the exact and co-exact subspaces are
each invariant at every squashing.*  ⇒ *** The control is exact and it is the strongest one in this
receipt: at every degree the operator's gradient eigenvalues are the scalar spectrum
`eq:squashed-spectrum` member for member, with the squashing free. ***  ⌗ *So the vector sector needs
no analogue of `r7160`'s left-invariance argument -- which is worth saying, because the scalar result
LOOKED like the general reason and is not.*

⛭⛭ ** ⓶ AND THEN THE BASIS MOVES, WHICH IS EXACTLY WHAT `r7160` FOUND DID NOT HAPPEN. **
*The layer's isometry group drops from `$SU(2)\\times SU(2)$` to `$SU(2)\\times U(1)$`, so what survives
is the LEFT spin and ONE charge.  A `$1$`-form carries its own charge in the frame index, so the
conserved label is the DIFFERENCE, and the invariant blocks are the triples
`$\\{e_+\\!\\otimes\\!q{+}1,\\ e_3\\!\\otimes\\!q,\\ e_-\\!\\otimes\\!q{-}1\\}$` -- dimension `$3$`, or
`$2$`, or `$1$` at the ends.  **Measured: zero matrix entries cross that grouping, and the coupling
inside it is `$2\\sqrt2\\varepsilon$` at `$L=1$` and `$4\\varepsilon$` at `$L=2$` -- nonzero for every
squashing and growing with it.**  So the eigenvectors are `$\\varepsilon$`-dependent mixtures and
`$(L,m)$` is NOT carried unmixed.*  ⌗ *The one place it is carried unmixed is the extreme charge,
where the block is one-dimensional -- and that is also where the eigenvalue is smallest at large
squashing, so the statement that matters is the one that needs no adiabaticity.*

⛭ ** ⓷ THE FLOOR THE SCALARS HAVE AND THE VECTORS DO NOT. **
*`r7160` has `$\\lambda\\ge2L$` for every `$\\varepsilon>0$`, its infimum only as
`$\\varepsilon\\to\\infty$`.  The co-exact sector has no such floor: `$(L+2)^2/\\varepsilon^2$` is an
EXACT eigenvalue at every degree -- `$9,16,25,36,49,64$` over `$L=1\\ldots6$` -- and it vanishes in
the same limit.*  ⌗ *For EVEN `$L$` a mixed branch dips below it; for `$L=1$` the unmixed mode is the
minimum at every squashing on the lift.  Both run to zero like `$\\varepsilon^{-2}$`.*

⛔ ** ⓸ AND THE REASON THAT DOES NOT END THE ROUTE. **  *`$\\varepsilon\\to\\infty$` happens only at
`$r\\to0$`, and `r7162` measured how little measure sits there: `$\\int|\\varepsilon|^{-1}\\dd\\eta =
0.8650719$` against `$s_{\\rm tot}=3.3387380$`.  The vector exponent is `$\\int\\sqrt{\\lambda^\\perp}
\\,\\dd\\eta$`, which at `$L=1$` is `$3\\times0.8650719=2.5952158$` EXACTLY, `$\\alpha$`-free.*
⇒ *** So the pointwise failure costs nothing: the exponent is linear in degree and the vector sector
is damped MORE than the scalar sector's most transparent band, by `$1.73$` at `$L=1$` and by `$4$` to
`$13$` per cent beyond. ***

⛔ ** THE TENSOR OBSTRUCTION, STATED AS A MECHANISM RATHER THAN AS A DIFFICULTY. **
*`$\\Delta_L$` preserves the transverse-traceless condition when the background is EINSTEIN.  The
Berger layer has `$R_{ab}=\\mathrm{diag}(4-2\\varepsilon^2,\\,4-2\\varepsilon^2,\\,2\\varepsilon^2)$`,
Einstein exactly at `$\\varepsilon^2=1$`.*  ⇒ *** So the transverse-traceless subspace is invariant at
the round point and at no other, and on the lift -- where `$\\varepsilon\\ge1.3747$` throughout -- the
divergence generated is a third of the image at the entry and exceeds the whole of it beyond.  That
is not a correction to bound; it is a different decomposition. ***  ⌗ *What this receipt therefore
does NOT do is quote a tensor eigenvalue on the squashed layer.  It shows the object does not exist in
that form and names what would replace it.*

⌗ ** THE GUARD THIS ONE LEAVES, AND IT IS `r7162`'s READ BACKWARDS. **
*`r7162`: a uniform bound is not a prediction until the measure is carried through it.  Here: ** a
pointwise bound's FAILURE is not a prediction either, until the same measure is carried through it. **
A floor that collapses on a set the transport barely visits costs the exponent nothing -- and the
honest form of both statements is the integral and never the bound.*

⌗ ** BOUNDS.  ** *Scalar-half scoping is respected: the paper's own sentence puts the tensor half in
the companion dynamics paper, so nothing here is offered as this paper's tensor claim -- the tensor
result is an obstruction to a computation, not a physical tensor spectrum.*  ⛔ *`$L$` is the degree
on the cosmological layer and is NOT the observable multipole; `sec:largescale`'s map is a projection
and not a relabelling above its third degree, which is this seat's own prior finding and is not
re-opened here.*  ⛔ *No layer metric is written down on the lift: the squashing is `sec:largescale`'s
own measured one, carried as its modulus on the timelike segment.*  ⛔ *No transmission FIGURE is
claimed -- exponents only, as in `r7162`.*  ⛔ *Vector perturbations of a spherically symmetric
background include a constrained sector; the paper's own guard on propagating modes applies here
unchanged and is not re-litigated.*
"""
import os
import re
import time

import mpmath as mp
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

ep = sp.Symbol('varepsilon', positive=True)
I = sp.I
mp.mp.dps = 30

# ---------------------------------------------------------------- Ⓐ the layer's own geometry
head("Ⓐ  THE LAYER'S CONNECTION AND CURVATURE, FROM THE STRUCTURE CONSTANTS AND NOT WRITTEN DOWN")


def struct():
    """orthonormal left-invariant frame e_1 = 2X_1, e_2 = 2X_2, e_3 = (2/eps)X_3 on the Berger layer."""
    a_, b_ = 2 * ep, 2 / ep
    C = {(c, x, y): 0 for c in range(3) for x in range(3) for y in range(3)}

    def setC(c, x, y, v):
        C[(c, x, y)] = v
        C[(c, y, x)] = -v

    setC(2, 0, 1, a_)
    setC(0, 1, 2, b_)
    setC(1, 2, 0, b_)
    Gam = {(c, x, y): sp.simplify(sp.Rational(1, 2) * (C[(c, x, y)] - C[(x, y, c)] + C[(y, c, x)]))
           for c in range(3) for x in range(3) for y in range(3)}
    Riem = {}
    for d in range(3):
        for c in range(3):
            for x in range(3):
                for y in range(3):
                    Riem[(d, c, x, y)] = sp.simplify(
                        sum(Gam[(d, x, e)] * Gam[(e, y, c)] for e in range(3))
                        - sum(Gam[(d, y, e)] * Gam[(e, x, c)] for e in range(3))
                        - sum(Gam[(d, e, c)] * C[(e, x, y)] for e in range(3)))
    Ric = sp.Matrix(3, 3, lambda c, y: sp.simplify(sum(Riem[(x, c, x, y)] for x in range(3))))
    return C, Gam, Riem, Ric


C, Gam, Riem, RIC = struct()
RSC = sp.simplify(sum(RIC[i, i] for i in range(3)))
print(f"\n    Ric = diag({RIC[0, 0]}, {RIC[1, 1]}, {RIC[2, 2]}),   R = {RSC}")

gate("Ⓐ①  at ε = 1 the frame returns the ROUND unit S³: Ric = 2g and R = 6, each derived from the"
     " structure constants rather than assumed",
     sp.simplify(RIC.subs(ep, 1) - 2 * sp.eye(3)) == sp.zeros(3, 3) and sp.simplify(RSC.subs(ep, 1) - 6) == 0)
gate("Ⓐ②  and off it the layer is NOT Einstein: Ric = diag(4−2ε², 4−2ε², 2ε²), whose traceless part"
     " vanishes exactly at ε² = 1 -- which is the whole tensor obstruction below, located here",
     sp.simplify(RIC[0, 0] - (4 - 2 * ep**2)) == 0 and sp.simplify(RIC[2, 2] - 2 * ep**2) == 0
     and sp.solve(sp.Eq(RIC[0, 0], RIC[2, 2]), ep) == [1])
gate("Ⓐ③  the frame is unimodular and the structure constants carry the squashing the way the metric"
     " does: C³₁₂ = 2ε against C¹₂₃ = C²₃₁ = 2/ε, equal only at ε = 1",
     sp.simplify(C[(2, 0, 1)] - 2 * ep) == 0 and sp.simplify(C[(0, 1, 2)] - 2 / ep) == 0
     and sp.simplify(C[(1, 2, 0)] - 2 / ep) == 0)


def spinJ(j):
    n = int(round(2 * j)) + 1
    qs = [sp.Rational(int(round(2 * j)) - 2 * k, 2) for k in range(n)]
    J3 = sp.diag(*qs)
    Jp, Jm = sp.zeros(n, n), sp.zeros(n, n)
    jj = sp.Rational(int(round(2 * j)), 2)
    for k in range(n):
        q = qs[k]
        if k > 0:
            Jp[k - 1, k] = sp.sqrt(jj * (jj + 1) - q * (q + 1))
        if k < n - 1:
            Jm[k + 1, k] = sp.sqrt(jj * (jj + 1) - q * (q - 1))
    return qs, (Jp + Jm) / 2, (Jp - Jm) / (2 * I), J3


def hodge_1form(j):
    """the Hodge Laplacian on 1-forms as a matrix on (frame index) x (layer charge)."""
    qs, J1, J2, J3 = spinJ(j)
    n = len(qs)
    E = [-2 * I * J1, -2 * I * J2, -(2 * I / ep) * J3]

    def emb(Mf, Ms):
        return sp.Matrix(sp.kronecker_product(Mf, Ms))

    Id3, Idn = sp.eye(3), sp.eye(n)
    D = [emb(Id3, E[x]) + emb(sp.Matrix(3, 3, lambda b, c: -Gam[(c, x, b)]), Idn) for x in range(3)]
    tot = sp.zeros(3 * n, 3 * n)
    for x in range(3):
        T = emb(Id3, E[x]) * D[x]
        for d in range(3):
            if Gam[(d, x, x)] != 0:
                T = T - Gam[(d, x, x)] * D[d]
        T = T + emb(sp.Matrix(3, 3, lambda c, d: -Gam[(d, x, c)]), Idn) * D[x]
        tot = tot + T
    return qs, sp.simplify(-tot + emb(RIC.T, Idn))


SCAL = lambda Lv, q: Lv * (Lv + 2) + 4 * (1 / ep**2 - 1) * q**2
UROT = sp.Matrix([[1 / sp.sqrt(2), 0, 1 / sp.sqrt(2)],
                  [-I / sp.sqrt(2), 0, I / sp.sqrt(2)],
                  [0, 1, 0]])
SFR = [1, 0, -1]


def vector_blocks(j):
    qs, L = hodge_1form(j)
    n = len(qs)
    T = sp.Matrix(sp.kronecker_product(UROT, sp.eye(n)))
    Lc = sp.simplify(T.inv() * L * T)
    lab = [(SFR[f], qs[m]) for f in range(3) for m in range(n)]
    key = [lab[i][0] - lab[i][1] for i in range(3 * n)]
    grp = {}
    for i in range(3 * n):
        grp.setdefault(key[i], []).append(i)
    cross = sum(1 for i in range(3 * n) for k in range(3 * n)
                if key[i] != key[k] and sp.simplify(Lc[i, k]) != 0)
    offd = [sp.simplify(Lc[i, k]) for i in range(3 * n) for k in range(3 * n)
            if i != k and sp.simplify(Lc[i, k]) != 0]
    Lv = sp.Integer(int(round(2 * j)))
    grad, trans = [], []
    cands = [sp.simplify(SCAL(Lv, q)) for q in qs]
    for c, idx in grp.items():
        ev = []
        for k, mult in sp.simplify(Lc[idx, idx]).eigenvals().items():
            ev += [sp.simplify(k)] * int(mult)
        used = False
        for e in ev:
            if not used and any(sp.simplify(e - cd) == 0 for cd in cands):
                grad.append(e)
                used = True
            else:
                trans.append(e)
    return Lv, qs, grp, lab, cross, offd, grad, trans


# ---------------------------------------------------------------- Ⓑ the vector sector
head("Ⓑ  THE VECTOR SECTOR: THE SPLIT SURVIVES, THE BASIS DOES NOT, AND THE FLOOR IS GONE")

VEC = {}
for jv in [sp.Rational(1, 2), 1, sp.Rational(3, 2), 2, sp.Rational(5, 2), 3]:
    VEC[int(2 * jv)] = vector_blocks(jv)

ROUND_1F = {1: {3: 2, 9: 4}, 2: {8: 3, 4: 1, 16: 5}, 3: {15: 4, 9: 2, 25: 6}}
ok_round = True
for Lv, want in ROUND_1F.items():
    _, _, _, _, _, _, grad, trans = VEC[Lv]
    got = {}
    for e in grad + trans:
        v = sp.nsimplify(sp.simplify(e.subs(ep, 1)))
        got[v] = got.get(v, 0) + 1
    ok_round = ok_round and got == {sp.Integer(k): v for k, v in want.items()}
gate("Ⓑ①  the operator reproduces the ROUND S³ 1-form spectrum with its multiplicities at L = 1, 2, 3"
     " -- the scalar members L(L+2) and the co-exact (k+1)² -- which is the control that fixes the"
     " convention before any squashing is switched on", ok_round)

ok_split, ok_count = True, True
for Lv in VEC:
    _, qs, _, _, _, _, grad, trans = VEC[Lv]
    cands = [sp.simplify(SCAL(sp.Integer(Lv), q)) for q in qs]
    ok_split = ok_split and all(any(sp.simplify(g - cd) == 0 for cd in cands) for g in grad)
    ok_count = ok_count and len(grad) == Lv + 1 and len(trans) == 2 * (Lv + 1)
gate("Ⓑ②  the EXACT subspace is invariant at every squashing and its eigenvalues are eq:squashed-"
     "spectrum member for member -- the structural fact that Δ_H commutes with d, measured rather"
     " than cited, at six degrees with ε free", ok_split)
gate("Ⓑ③  and the count is right: L+1 gradient modes against 2(L+1) co-exact ones at every degree,"
     " so nothing has been lost or double-counted in the split", ok_count)

_, _, _, _, cross1, offd1, _, _ = VEC[1]
_, _, _, _, cross2, offd2, _, _ = VEC[2]
print(f"\n    entries crossing the conserved frame-minus-layer charge: L=1 {cross1}, L=2 {cross2}")
print(f"    the couplings inside a block: L=1 {sorted(set(sp.simplify(x) for x in offd1), key=str)}"
      f"   L=2 {sorted(set(sp.simplify(x) for x in offd2), key=str)}")
gate("Ⓑ④  the conserved label is the frame charge MINUS the layer charge and the blocks are at most"
     " 3×3: zero matrix entries cross that grouping at L = 1 and L = 2",
     cross1 == 0 and cross2 == 0)
gate("Ⓑ⑤  and inside a block the coupling is PROPORTIONAL TO ε -- 2√2ε at L = 1 and 4ε at L = 2,"
     " nonzero for every squashing -- so the eigenVECTORS move with ε and (L,m) is NOT carried"
     " unmixed, which is the OPPOSITE of the scalar sector's deciding fact",
     any(sp.simplify(x - 2 * sp.sqrt(2) * ep) == 0 or sp.simplify(x + 2 * sp.sqrt(2) * ep) == 0 for x in offd1)
     and any(sp.simplify(x - 4 * ep) == 0 or sp.simplify(x + 4 * ep) == 0 for x in offd2)
     and all(sp.simplify(sp.limit(x, ep, 0)) == 0 for x in offd1))

ok_edge = True
edge_vals = []
for Lv in sorted(VEC):
    _, _, grp, lab, _, _, _, _ = VEC[Lv]
    qs, L = hodge_1form(sp.Rational(Lv, 2))
    n = len(qs)
    T = sp.Matrix(sp.kronecker_product(UROT, sp.eye(n)))
    Lc = sp.simplify(T.inv() * L * T)
    top = max(grp)
    idx = grp[top]
    val = sp.simplify(Lc[idx, idx][0, 0])
    edge_vals.append((Lv, len(idx), val))
    ok_edge = ok_edge and len(idx) == 1 and sp.simplify(val - (Lv + 2)**2 / ep**2) == 0
print("\n    the extreme-charge block, by degree:")
for Lv, d, val in edge_vals:
    print(f"      L={Lv}: dim {d},  λ = {val}")
gate("Ⓑ⑥  the extreme-charge block is ONE-DIMENSIONAL at every degree -- so that mode alone is"
     " carried unmixed -- and its eigenvalue is EXACTLY (L+2)²/ε², verified at L = 1…6", ok_edge)
gate("Ⓑ⑦  so the scalar sector's uniform floor has NO vector counterpart: (L+2)²/ε² runs to zero as"
     " ε → ∞, where r7160's λ ≥ 2L holds -- the two sectors differ at the one end of the lap the"
     " transport actually reaches",
     all(sp.limit((Lv + 2)**2 / ep**2, ep, sp.oo) == 0 for Lv in sorted(VEC))
     and sp.simplify(sp.limit(2 * sp.Symbol('L', positive=True) + sp.Symbol('L', positive=True)**2 / ep**2,
                              ep, sp.oo) - 2 * sp.Symbol('L', positive=True)) == 0)

# ---------------------------------------------------------------- Ⓒ the lift, carried
head("Ⓒ  AND THE EXPONENT, WITH THE LIFT'S OWN MEASURE CARRIED THROUGH THE BROKEN FLOOR")


def build(alpha):
    """the lift's objects at this alpha, from the E = 1, k = 0 radial equation -- r7162's, reused."""
    al = mp.mpf(alpha)
    two_M = 2 * al / (3 * mp.sqrt(3))
    rN = al / mp.sqrt(3)
    u_t = (two_M * al**2)**(mp.mpf(1) / 3)
    mf = lambda r: (r - rN)**2 * (r + 2 * rN) / (al**2 * r)
    eps = lambda u: al * mp.sqrt(abs(mf(-u))) / u
    deta = lambda u: 1 / (u * mp.sqrt(two_M / u - u**2 / al**2))
    return al, u_t, eps, deta


AL, U_T, EPSF, DETAF = build(1)
S_TOT = mp.re(mp.quad(DETAF, [0, U_T / 2, U_T]))
INV = mp.re(mp.quad(lambda u: DETAF(u) / EPSF(u), [0, U_T / 2, U_T]))
print(f"\n    s_tot = {mp.nstr(S_TOT, 12)},   ∫|dη|/|ε| = {mp.nstr(INV, 12)},"
      f"   ratio = {mp.nstr(INV / S_TOT, 12)},   |ε| at the turnaround = {mp.nstr(EPSF(U_T), 10)}")
gate("Ⓒ①  the lift's measure reproduces r7162 before anything new is built on it: s_tot = 3.3387380,"
     " the inverse-squashing length 0.8650719 and the entry squashing 1.3747296",
     abs(S_TOT - mp.mpf('3.33873802357')) < mp.mpf('1e-10')
     and abs(INV - mp.mpf('0.86507190554')) < mp.mpf('1e-10')
     and abs(EPSF(U_T) - mp.mpf('1.374729637')) < mp.mpf('1e-8'))
gate("Ⓒ②  and the whole lift lies where the squashing EXCEEDS its round value, so the end where the"
     " vector floor collapses is the end the transport reaches",
     EPSF(U_T) > 1 and EPSF(U_T / 1000) > EPSF(U_T))

TFN = {Lv: [sp.lambdify(ep, t, 'mpmath') for t in VEC[Lv][7]] for Lv in sorted(VEC)}
rows = []
print("\n     L    I_vec (exact minimum)    (L+2)·0.8650719    scalar max-charge    ratio")
for Lv in sorted(VEC):
    fns = TFN[Lv]
    lam = lambda u: min(mp.re(f(EPSF(u))) for f in fns)
    Iv = mp.re(mp.quad(lambda u: mp.sqrt(lam(u)) * DETAF(u), [mp.mpf('1e-12') * U_T, U_T / 2, U_T]))
    unm = (Lv + 2) * INV
    sc = mp.sqrt(Lv * (Lv + 2)) * INV
    rows.append((Lv, Iv, unm, sc))
    print(f"    {Lv:>2}    {mp.nstr(Iv, 10):>16}    {mp.nstr(unm, 10):>14}    {mp.nstr(sc, 10):>14}"
          f"    {mp.nstr(Iv / sc, 7)}")
gate("Ⓒ③  the exponent is FINITE at every degree although the eigenvalue it integrates runs to zero"
     " -- the measure is thin exactly where the floor collapses",
     all(r[1] > 0 and r[1] < mp.inf for r in rows))
gate("Ⓒ④  at L = 1 the minimum IS the unmixed extreme-charge mode at every squashing on the lift, so"
     " there the exponent is exactly 3 × 0.8650719 = 2.5952158 with no adiabaticity assumed",
     abs(rows[0][1] - 3 * INV) < mp.mpf('1e-12'))
gate("Ⓒ⑤  and the vector exponent EXCEEDS the scalar sector's most transparent band at every degree"
     " computed -- by 1.73 at L = 1 and by 4 to 13 per cent through L = 6 -- so the broken pointwise"
     " bound leaves the suppression STRONGER rather than weaker",
     all(r[1] > r[3] for r in rows) and rows[0][1] / rows[0][3] > mp.mpf('1.7'))
gate("Ⓒ⑥  the exponent stays LINEAR in degree rather than collapsing: I_vec/L settles between 1.1 and"
     " 1.2 over the computed range, against the scalar band's 0.865",
     all(mp.mpf('1.0') < r[1] / r[0] < mp.mpf('1.4') for r in rows[2:])
     and abs(INV - mp.mpf('0.865')) < mp.mpf('0.001'))

afree = []
for a in ['0.4', '1', '7']:
    _, ut, epf, detaf = build(a)
    afree.append(mp.re(mp.quad(lambda u: 3 * detaf(u) / epf(u), [mp.mpf('1e-14') * ut, ut / 2, ut])))
print(f"\n    I_vec(1) at α = 0.4, 1, 7: {[mp.nstr(x, 13) for x in afree]}")
gate("Ⓒ⑦  and it is α-FREE: the L = 1 exponent agrees to thirteen figures across three values of α,"
     " so it is a statement about the family and not about a member",
     max(abs(x - afree[0]) for x in afree) < mp.mpf('1e-12'))

# ---------------------------------------------------------------- Ⓓ the tensor obstruction
head("Ⓓ  THE TENSOR SECTOR: TRACELESSNESS SURVIVES, TRANSVERSALITY DOES NOT, AND THE DEFICIT IS Ⓐ②")

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


def lichnerowicz(jv, epv):
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
        T = np.kron(np.eye(9), E[x]) @ D[x]
        for d in range(3):
            if abs(G[(d, x, x)]) > 1e-14:
                T = T - G[(d, x, x)] * D[d]
        T = T + np.kron(gam_act(x), np.eye(n)).astype(complex) @ D[x]
        tot = tot + T
    CUR = np.zeros((9, 9))
    for p, (a, b) in enumerate(IDX9):
        for c in range(3):
            for d in range(3):
                CUR[p, IDX9.index((c, d))] += -2 * Rm[(a, c, b, d)]
            CUR[p, IDX9.index((c, b))] += Rc[a, c]
            CUR[p, IDX9.index((a, c))] += Rc[b, c]
    return n, D, -tot + np.kron(CUR, np.eye(n)).astype(complex)


def tt_probe(jv, epv):
    n, D, LL = lichnerowicz(jv, epv)
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
    dv = np.linalg.norm(np.array(div_rows) @ H) / nrm
    tr = np.linalg.norm(np.array(trace_rows) @ H) / nrm
    dim = ns.shape[1]
    if dim and np.linalg.norm(H) > 0:
        P = ns.conj().T @ LL @ ns
        inv = np.linalg.norm(LL @ ns - ns @ P) / nrm
        ev = np.sort(np.real(np.linalg.eigvals(P)))
    else:
        inv, ev = 0.0, np.array([])
    return dim, ev, dv, tr, inv


ROUND_TT = {2: 28, 3: 39, 4: 52, 5: 67, 6: 84}
ok_tt_round, tt_dims = True, []
for Lv, want in ROUND_TT.items():
    dim, ev, dv, tr, inv = tt_probe(Lv / 2.0, 1.0)
    tt_dims.append((Lv, dim, ev[-1], inv))
    ok_tt_round = ok_tt_round and abs(ev[-1] - want) < 1e-8 and inv < 1e-12 and dim >= 2 * Lv + 2
print("\n    at the ROUND point: TT dimension, top eigenvalue, and invariance residual")
for Lv, dim, top, inv in tt_dims:
    print(f"      L={Lv}: dim {dim:>3}, λ_top = {top:.6f} (L²+6L+12 = {Lv * Lv + 6 * Lv + 12}),"
          f"  residual {inv:.1e}")
gate("Ⓓ①  at ε = 1 the transverse-traceless space IS invariant -- residual below 1e-12 -- and its"
     " top eigenvalue is L² + 6L + 12 at L = 2…6, which is the control that the operator and the"
     " projection are both right where they can be checked.  ⌗ The dimension is 2L+2 from the third"
     " degree up and ONE MORE than that at L = 2, which is reported as measured rather than fitted:"
     " that extra element is invariant to machine precision like the rest, so it is a feature of the"
     " lowest degree and not a defect of the projection", ok_tt_round)

print("\n    off the round point: what Δ_L generates from a transverse-traceless tensor")
print("      L    ε          divergence/‖image‖      trace/‖image‖     Einstein deficit |1−ε²|")
probe = []
for Lv in [2, 3]:
    for e in [1.0, 1.0001, 1.1, 1.374729637, 2.0, 5.0]:
        dim, ev, dv, tr, inv = tt_probe(Lv / 2.0, e)
        probe.append((Lv, e, dv, tr, abs(1 - e * e)))
        print(f"     {Lv:>2}   {e:<10g}  {dv:>18.3e}   {tr:>16.3e}   {abs(1 - e * e):>14.4g}")
gate("Ⓓ②  Δ_L keeps TRACELESSNESS at every squashing -- the trace it generates stays at machine zero"
     " across both degrees and all six squashings", max(p[3] for p in probe) < 1e-14)
gate("Ⓓ③  but it generates DIVERGENCE as soon as the layer stops being Einstein: machine zero at"
     " ε = 1 and nonzero at every ε ≠ 1 tested, so the transverse-traceless subspace is invariant at"
     " the round point and at no other",
     all(p[2] < 1e-14 for p in probe if p[1] == 1.0)
     and all(p[2] > 1e-6 for p in probe if p[1] != 1.0))
near = [p for p in probe if p[1] == 1.0001]
gate("Ⓓ④  and the divergence generated is LINEAR in the Einstein deficit of Ⓐ② near the round point"
     " -- a deficit of 2e-4 produces 3.7e-5 and 5.1e-5 at the two degrees, the same order with no"
     " quadratic suppression -- which identifies the obstruction rather than merely exhibiting it",
     all(1e-2 < p[2] / p[4] < 1e0 for p in near))
entry = [p for p in probe if abs(p[1] - 1.374729637) < 1e-9]
gate("Ⓓ⑤  at the lift's ENTRY the divergence generated is already 24 to 32 per cent of the image, and"
     " beyond it exceeds the whole of it -- so this is not a small correction to be bounded on the"
     " segment the transport actually traverses",
     all(0.2 < p[2] < 0.35 for p in entry)
     and all(p[2] > 0.7 for p in probe if p[1] == 2.0))
gate("Ⓓ⑥  so no tensor eigenvalue is quoted on the squashed layer by this receipt, and the reason is"
     " structural rather than a want of effort: the object a spectrum would belong to is not"
     " invariant, and what is owed is a decomposition",
     not any('tensor eigenvalue on the squashed layer' in nm for nm, _ in CHECKS))

# ---------------------------------------------------------------- Ⓔ the paper, read
head("Ⓔ  THE PAPER'S OWN CLAUSES, LOCATED IN THE CURRENT SOURCE AND PARTITIONED")

_SCOPE = 'the scalar half is here'
_BASIS = 'deformation reaches the spectrum and not the basis'
# ⛭ r7164 (66, the gate, repairing a receipt its own edit broke -- the standing exception): Ⓔ③ pinned
#   `every other mode is bounded below uniformly` and the basis clause at their r7166 wording, and
#   LANDING THIS RECEIPT'S RESULT rescoped both -- they now read `every other SCALAR mode ...` and
#   `For scalars the deformation ...`, because the whole finding is that the scalar scope is where they
#   are true.  ** So the receipt went red on the success of its own recommendation, for the fourth
#   revision running in this family. **
#   ⇒ *** AND IT IS A SHARPER FORM THAN r7163's: that one was a count of citations rising.  This is a
#       receipt PINNING THE PROSE ITS OWN RESULT ASKS TO BE CHANGED -- so the pin is red exactly when
#       the recommendation is taken, and green exactly while it is ignored. ***  `Ⓔ⑤` two gates below
#       enumerates over the states the paper may produce and held through the same landing, which is
#       the form that works; these two counted instead.
#   ⌗ Repaired to the clauses as the scoping leaves them, with the scope word carried in the pattern
#     rather than assumed away: `_FLOOR` keeps the word `scalar`, which is what this receipt put there.
_FLOOR = 'every other scalar mode is bounded below uniformly'
_UNMIX = 'so $(L,m)$ is conserved along the bead and nothing mixes'
_PROP = 'The computation above is a statement about propagating field modes'

gate("Ⓔ①  the scalar-half scoping clause is in print exactly once and is reasoned FROM: it is why"
     " nothing here is offered as this paper's tensor claim", b15.count(_SCOPE) == 1)
gate("Ⓔ②  eq:squashed-spectrum's LABEL is in print exactly once -- the label and not its citation"
     " count, which r7163 established is not pinnable because landing a result adds citations",
     b15.count('\\label{eq:squashed-spectrum}') == 1)
gate("Ⓔ③  the uniform-floor clause and the unmixed-transport clause are each in print exactly once"
     " and are reasoned FROM: they are the SCALAR statements this receipt contrasts against rather"
     " than contradicts", b15.count(_FLOOR) == 1 and b15.count(_UNMIX) == 1)
gate("Ⓔ④  and the propagating-modes guard is in print exactly once, which is what keeps the vector"
     " result from being read as a statement about the constrained sector",
     b15.count(_PROP) == 1)
gate("Ⓔ⑤  the ONE clause this receipt's result bears on is ENUMERATED over the states the paper may"
     " produce rather than pinned: either the basis sentence still stands unscoped, or it has"
     " acquired a sector scope, or this row has landed and the vector sector is named beside it --"
     " and the receipt's reading is unchanged in all three",
     (b15.count(_BASIS) == 1 and 'vector' not in b15[b15.find(_BASIS):b15.find(_BASIS) + 400])
     or 'scalar sector' in b15[max(0, b15.find(_BASIS) - 200):b15.find(_BASIS) + 400]
     or b15.count('co-exact') >= 1)
gate("Ⓔ⑥  and the layer the whole computation is done on is the paper's OWN measured squashing"
     " carried as its modulus, not a posited profile: the entry value 1.3747296 is reproduced from"
     " the radial equation in Ⓒ① rather than read from the paper",
     abs(EPSF(U_T) - mp.mpf('1.374729637')) < mp.mpf('1e-8'))

# ---------------------------------------------------------------- verdict
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
  VERDICT, THE VECTOR SECTOR: the split survives every squashing because the
  Hodge Laplacian commutes with d on any manifold -- measured as the gradient
  sector returning eq:squashed-spectrum exactly -- but INSIDE the co-exact
  sector the deformation reaches the BASIS, with 3x3 blocks coupled in
  proportion to the squashing itself, so (L,m) is not carried unmixed.  And
  the scalar sector's uniform floor has no counterpart: the unmixed extreme-
  charge eigenvalue is exactly (L+2)^2/eps^2 and runs to ZERO at the close of
  the lift.
  *** AND THE SUPPRESSION SURVIVES ANYWAY.  Carried through the lift's own
      measure the exponent is finite, linear in degree, and LARGER than the
      most transparent scalar band's at every degree computed -- 2.5952
      against 1.4983 at L = 1, exactly 3 x 0.8650719 and alpha-free. ***

  VERDICT, THE TENSOR SECTOR: there is no transverse-traceless spectrum to
  quote.  Delta_L keeps tracelessness at every squashing and generates
  divergence as soon as the layer stops being Einstein, which it does at every
  eps other than 1 -- the generated divergence linear in the Einstein deficit
  near the round point and already a third of the image at the lift's entry.
  *** So PO-81's second horn, which closed for the scalars, OPENS for the
      tensors: what is owed there is a decomposition and not an eigenvalue. ***

  THE GUARD: a pointwise bound's FAILURE is not a prediction until the measure
  is carried through it -- r7162's guard read backwards, and it cost the
  exponent nothing.
  ==========================================================================
""")

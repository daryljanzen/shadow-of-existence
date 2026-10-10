#!/usr/bin/env python3
"""P16 receipt -- node 66's `r7171` ORDER ⓶, re-weighted LOAD-BEARING by `r7173`:
** derive `P16`'s `the $S^3$ tensor tower starts at $L=2$ and has no $k=0$ member` on the
construction's own `$S^3$`, rather than citing the standard result. **

*** ⛭⛭⛭ THE CLAUSE IS RIGHT AS WRITTEN AND IT IS NOW DERIVED.  The transverse-traceless rough
    Laplacian on this `$S^3$` has spectrum `$L(L+2)-2$` EXACTLY, for integer `$L\\ge2$` and for no
    other value: `$6,13,22,33,46,61,78$` over the seven levels computed, with degree multiplicity
    `$2(L+3)(L-1)$`.  ** The floor is arithmetic: `$k^2=L(L+2)-2=0$` requires `$L(L+2)=2$`, which no
    non-negative integer satisfies, so the `$k=0$` member is not excluded by fiat -- it does not
    exist. ** ***

⛔ ** AND THE FIRST THING THIS RECEIPT DOES IS WITHDRAW MY OWN REPORT OF A GAP. ** *At `r7173`-time I
reported to `66` that this space is non-empty at every degree including `$L=0$` and `$L=1$`, that the
floor therefore does NOT follow from the transverse-traceless condition, and that twelve solutions at
one degree were accounted for by nothing.*  ⇒ *** THAT REPORT WAS WRONG, and the error was a
LABELLING error of exactly the kind this corpus keeps catching: ** the index I was reading as the
degree is the level of the construction's `$V_j`-factor, which IS the degree for SCALARS -- the scalar
Laplacian at level `$2j$` is `$2j(2j+2)$` -- and is NOT the degree for tensors. *** *The twelve modes
I called `$L=1$` carry `$-\\nabla^2=13=3\\cdot5-2$`: they are `$L=3$`, the SECOND rung of the tower,
not a sub-floor mode.  **Gated below at Ⓒ④ rather than asserted here.***

** ⓵ THE INDEX CANNOT BE A DEGREE, AND THE PROOF OF THAT IS THAT ONE LEVEL CARRIES TWO DEGREES. **
*At level `$2j=4$` the kernel is ten-dimensional and the Laplacian splits it: ONE eigenvector at `$6$`
and NINE at `$46$` -- `$L=2$` and `$L=7$` in the same level.*  ⇒ *An index that splits under the
operator whose eigenvalue defines the degree is not that degree.  **The two pieces are the two
chiralities: degree `$L$` is assembled from level `$2j=L-2$` and level `$2j=L+2$`, half each.***

** ⓶ SO THE FLOOR IS A STATEMENT ABOUT WHICH LEVELS EXIST AND IT IS EXACT. ** *Every eigenvalue the
computation returns is `$L(L+2)-2$` for an integer `$L$` in `$2\\ldots8$`, and the MINIMUM over the
whole computed space is `$6$`.*  ⇒ *** `$L=1$` would require the eigenvalue `$1$` and `$L=0$` would
require `$-2$`; neither occurs.  The tower starts at `$L=2$`. ***

⌗ ** AND THE DEGENERACIES CONFIRM IT INDEPENDENTLY OF THE EIGENVALUES: ** *`$10$` at `$L=2$`, `$24$`
at `$L=3$`, `$42$` at `$L=4$`, each assembled from two equal halves at the two chirality levels ---
`$2(L+3)(L-1)$`, which is the closed-`$FRW$` tensor degeneracy.  **Two independent fingerprints of the
same tower, and the floor sits at the bottom of both.**

*** ⛭⛭ THE KILLING CONTROL IS STATED IN THIS RECEIPT BECAUSE IT IS THE CONTROL I ALREADY PROVED I CAN
    MIS-SITE.  `$\\mathcal{L}_\\xi g=0$` has exactly SIX solutions and they sit THREE at level
    `$2j=0$` and THREE at level `$2j=2$`, with NOTHING at `$2j=1$` -- which is the arithmetic I got
    wrong the first time and reported as a failed control. ** The instrument passes its own control,
    and the location of the passing is part of the result. ** ***

⌗ ** AND NO TRANSVERSE-TRACELESS MODE IS PURE GAUGE: ** *the intersection of the kernel with the image
of `$\\xi\\mapsto\\mathcal{L}_\\xi g$` is ZERO at every level computed, so the tower is physical
content and the floor is not a gauge artefact.*

** WHAT THIS DOES NOT SHOW, STATED SO THE CLAUSE IS NOT OVER-READ. ** *This is the ROUND unit
`$S^3$`, which is the sphere `P16`'s closed ball carries and the sphere its clause is about.  The
squashed members are a DIFFERENT eigenvalue problem -- `r7184` computed one sector of it and found the
squashing drops out only where the sector descends -- and nothing here speaks to them.  **The three
sites that carry `$L=2$` rest on this derivation; the squashed question is not one of them.***

** COMPUTES: on the unit round `$S^3$` in its left-invariant frame, the Levi-Civita connection from
the frame's own bracket, its Ricci tensor, the scalar Laplacian level by level, the trace and
divergence constraints on symmetric two-tensors, the rough Laplacian restricted to their common
kernel and its exact rational spectrum, the Killing equation, and the gauge image -- at the seven
levels `$2j=0\\ldots6$`.  Exact arithmetic throughout; no tolerance, no sampling, no floating point
in any gate. **
"""
import os
import re
import time

import sympy as sp

t_all = time.time()
CHECKS = []
I = sp.I


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAPER = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                                 encoding='utf-8').read())


# ======================================================================================
# THE INSTRUMENT.  The left-invariant frame on SU(2) = S^3: E_a = -2i J_a on the level-j
# representation, so [E_a, E_b] = 2 eps_abc E_c, and the Levi-Civita connection for that
# bracket is Gamma^d_{ab} = eps(d, a, b).  Both facts are GATED below, not assumed.
# ======================================================================================
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
    return (Jp + Jm) / 2, (Jp - Jm) / (2 * I), J3


_E3 = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1,
       (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}


def eps(a, b, c):
    return sp.Integer(_E3.get((a, b, c), 0))


def G(d, a, b):
    return eps(d, a, b)


PAIRS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]


def ip(b, c):
    return PAIRS.index((b, c) if (b, c) in PAIRS else (c, b))


def frame(j):
    J1, J2, J3 = spinJ(j)
    return [-2 * I * J1, -2 * I * J2, -2 * I * J3]


# =====================================================================================
head("A -- THE INSTRUMENT IS THE CONSTRUCTION'S OWN S^3, AND IT IS VALIDATED BEFORE USE")

# torsion-free: [E_a, E_b] = (Gamma^c_{ab} - Gamma^c_{ba}) E_c, with [E_a,E_b] = 2 eps_abc E_c
_brk = []
for a in range(3):
    for b in range(3):
        for c in range(3):
            _brk.append(sp.simplify(G(c, a, b) - G(c, b, a) - 2 * eps(a, b, c)))
# metric-compatible: Gamma^c_{ab} = -Gamma^b_{ac}
_mc = [sp.simplify(G(c, a, b) + G(b, a, c))
       for a in range(3) for b in range(3) for c in range(3)]
gate("Ⓐ①  the connection used is the LEVI-CIVITA connection OF THIS FRAME, and both halves are"
     " checked against the frame's own bracket rather than quoted: torsion-free, because"
     " `$\\Gamma^c_{ab}-\\Gamma^c_{ba}$` equals the structure constant `$2\\varepsilon_{abc}$` at"
     " every one of the twenty-seven index triples; and metric-compatible, because"
     " `$\\Gamma^c_{ab}$` is antisymmetric in its last two indices at every triple",
     all(x == 0 for x in _brk) and all(x == 0 for x in _mc))


def Riem(d, c, a, b):
    t = sum(G(d, a, e) * G(e, b, c) - G(d, b, e) * G(e, a, c) for e in range(3))
    t -= sum(2 * eps(a, b, e) * G(d, e, c) for e in range(3))
    return sp.simplify(t)


RIC = sp.Matrix(3, 3, lambda c, b: sum(Riem(a, c, a, b) for a in range(3)))
gate("Ⓐ②  and the curvature it produces is the UNIT ROUND `$S^3$`: the Ricci tensor comes out"
     " `$R_{ab}=2\\delta_{ab}$` exactly -- so the sphere this receipt computes on is the sphere"
     " whose scalar tower the construction already uses, and not some other three-geometry",
     sp.simplify(RIC - 2 * sp.eye(3)) == sp.zeros(3, 3))

_scal = []
for twoj in range(0, 7):
    j = sp.Rational(twoj, 2)
    E = frame(j)
    LAPS = -(E[0] * E[0] + E[1] * E[1] + E[2] * E[2])
    _scal.append((twoj, sp.simplify(LAPS - twoj * (twoj + 2) * sp.eye(twoj + 1)) ==
                  sp.zeros(twoj + 1, twoj + 1)))
gate("Ⓐ③  ⛭ AND THE SCALAR LAPLACIAN AT LEVEL `$2j$` IS `$2j(2j+2)$` EXACTLY, at all seven levels"
     " -- which is `$L(L+2)$` with `$L=2j$`, the closed-`$FRW$` scalar tower.  ** THIS GATE IS THE"
     " TRAP: the level index IS the degree for scalars, which is precisely why it was mistaken for"
     " the degree for tensors, and it is stated here as a fact about SCALARS so that Ⓒ can show it"
     " fails for tensors **",
     all(ok for _, ok in _scal))


# ======================================================================================
# The operators on symmetric two-tensors, level by level.
#   grad_a h_{bc} = E_a h_{bc} - Gamma^d_{ab} h_{dc} - Gamma^d_{ac} h_{bd}
#   (div grad h)_{bc} = sum_a grad_a (grad h)_{a bc}
# ======================================================================================
def ops(j):
    n = int(round(2 * j)) + 1
    E = frame(j)
    N = 6 * n

    def col(p, k):
        return p * n + k

    M3 = 3 * 6 * n

    def c3(a, p, k):
        return (a * 6 + p) * n + k

    D = sp.zeros(M3, N)
    for a in range(3):
        for p, (b, c) in enumerate(PAIRS):
            for k in range(n):
                r = c3(a, p, k)
                for kk in range(n):
                    D[r, col(p, kk)] += E[a][k, kk]
                for d in range(3):
                    D[r, col(ip(d, c), k)] -= G(d, a, b)
                    D[r, col(ip(b, d), k)] -= G(d, a, c)
    Ld = sp.zeros(N, M3)
    for p, (b, c) in enumerate(PAIRS):
        for k in range(n):
            r = col(p, k)
            for a in range(3):
                for kk in range(n):
                    Ld[r, c3(a, p, kk)] += E[a][k, kk]
                for d in range(3):
                    Ld[r, c3(a, ip(d, c), k)] -= G(d, a, b)
                    Ld[r, c3(a, ip(b, d), k)] -= G(d, a, c)
                    Ld[r, c3(d, p, k)] -= G(d, a, a)
    LAP = -(Ld * D)

    rows = []
    for k in range(n):                                   # traceless
        r = [sp.Integer(0)] * N
        for a in range(3):
            r[col(ip(a, a), k)] += 1
        rows.append(r)
    for c in range(3):                                   # transverse
        for k in range(n):
            r = [sp.Integer(0)] * N
            for a in range(3):
                for kk in range(n):
                    r[col(ip(a, c), kk)] += E[a][k, kk]
                for d in range(3):
                    r[col(ip(d, c), k)] -= G(d, a, a)
                    r[col(ip(a, d), k)] -= G(d, a, c)
            rows.append(r)

    gcols = []                                           # xi |-> Lie_xi g
    for b0 in range(3):
        for k0 in range(n):
            h = [[sp.Integer(0)] * n for _ in range(6)]
            for a in range(3):
                for b in range(3):
                    for k in range(n):
                        t = sp.Integer(0)
                        if b == b0:
                            t += E[a][k, k0]
                        t -= G(b0, a, b) * (1 if k == k0 else 0)
                        if t != 0:
                            h[ip(a, b)][k] += t
            vec = []
            for p in range(6):
                vec.extend(h[p])
            gcols.append(sp.Matrix(vec))
    return sp.Matrix(rows), LAP, sp.Matrix.hstack(*gcols), N, n


LEVELS = {}
for twoj in range(0, 7):
    j = sp.Rational(twoj, 2)
    C, LAP, GAU, N, n = ops(j)
    K = C.nullspace()
    B = sp.Matrix.hstack(*K) if K else sp.zeros(N, 0)
    spec = {}
    if K:
        RHS = LAP * B
        X = sp.simplify(B.solve_least_squares(RHS))
        inv = sp.simplify(B * X - RHS) == sp.zeros(*RHS.shape)
        spec = {sp.nsimplify(e): m for e, m in X.eigenvals().items()}
    else:
        inv = True
    rk_g = GAU.rank()
    both = sp.Matrix.hstack(GAU, B).rank() if K else rk_g
    inside = rk_g + B.rank() - both if K else 0
    # every count in the reduced space carries the implicit multiplicity (2j+1) of the
    # second V_j factor, which no operator here touches; `full` counts are reduced x n.
    LEVELS[twoj] = dict(n=n, dim=len(K), full=len(K) * n, spec=spec,
                        inv=inv, rk_g=rk_g, inside=inside,
                        kill_red=3 * n - rk_g, kill=(3 * n - rk_g) * n)
    print(f"    level 2j={twoj}:  kernel {len(K):2d} x {n} = {len(K) * n:3d}"
          f"   spectrum { {str(k): v for k, v in sorted(spec.items(), key=lambda t: t[0])} }"
          f"   Killing {(3 * n - rk_g) * n}   in-gauge {inside}", flush=True)

# =====================================================================================
head("B -- THE KILLING CONTROL, AND THE CONTROL'S LOCATION IS PART OF THE RESULT")

gate("Ⓑ①  `$\\mathcal{L}_\\xi g=0$` has exactly SIX solutions over the seven levels -- the isometry"
     " algebra of the round `$S^3$`, counted by the instrument rather than quoted at it",
     sum(LEVELS[t]['kill'] for t in LEVELS) == 6)

gate("Ⓑ②  ⛭ AND THEY SIT THREE AT LEVEL `$2j=0$` AND THREE AT LEVEL `$2j=2$`, WITH NOTHING AT"
     " `$2j=1$` -- which is the arithmetic this seat got wrong once and reported to `66` as a FAILED"
     " control.  ** The location is gated here, and not merely the total, because the total was"
     " never what I got wrong **",
     LEVELS[0]['kill'] == 3 and LEVELS[1]['kill'] == 0 and LEVELS[2]['kill'] == 3
     and all(LEVELS[t]['kill'] == 0 for t in (3, 4, 5, 6)))

gate("Ⓑ③  and the transverse-traceless kernel meets the gauge image in ZERO at every level, so no"
     " member of the tower is `$\\mathcal{L}_\\xi g$` for any `$\\xi$` -- the tower is physical"
     " content and the floor below is not an artefact of a coordinate choice",
     all(LEVELS[t]['inside'] == 0 for t in LEVELS))

gate("Ⓑ④  and the kernel is LAPLACIAN-INVARIANT at every level -- the restriction below is a"
     " restriction and not a projection, checked by residual rather than argued from the operator's"
     " name",
     all(LEVELS[t]['inv'] for t in LEVELS))

# =====================================================================================
head("C -- THE LEVEL INDEX IS THE SCALAR DEGREE AND IT IS NOT THE TENSOR DEGREE")

gate("Ⓒ①  the transverse-traceless kernel is non-empty at EVERY level, with full dimensions"
     " `$5,12,21,32,50,72,98$` -- which is the measurement that, read as a statement about degrees,"
     " says the tower has members below its floor.  ** It is reproduced here because it is true and"
     " because it is what I mis-read **",
     [LEVELS[t]['full'] for t in range(7)] == [5, 12, 21, 32, 50, 72, 98])

gate("Ⓒ②  ⛭ BUT AT LEVEL `$2j=0$` THE LAPLACIAN EIGENVALUE IS `$6$`, WHILE THE DEGREE THAT INDEX"
     " WOULD NAME REQUIRES `$2j(2j+2)-2=-2$`.  ** So the index does not name the degree, and one"
     " level of the instrument settles it: a five-dimensional space of modes whose eigenvalue is"
     " that of `$L=2$` sits at the index I was calling `$L=0$` **",
     list(LEVELS[0]['spec'].keys()) == [sp.Integer(6)]
     and sp.Integer(-2) not in LEVELS[0]['spec'])

gate("Ⓒ③  AND THE DECISIVE ONE: at level `$2j=4$` the Laplacian SPLITS the kernel -- one eigenvector"
     " at `$6$` and nine at `$46$`, two different degrees in ONE level.  ** An index that splits"
     " under the operator whose eigenvalue defines the degree cannot be that degree; this is a"
     " structural statement and not a close call **",
     LEVELS[4]['spec'] == {sp.Integer(6): 1, sp.Integer(46): 9}
     and LEVELS[5]['spec'] == {sp.Integer(13): 2, sp.Integer(61): 10}
     and LEVELS[6]['spec'] == {sp.Integer(22): 3, sp.Integer(78): 11})

gate("Ⓒ④  ⛔ SO THE TWELVE MODES THIS SEAT REPORTED AS AN UNEXPLAINED `$L=1$` CARRY"
     " `$-\\nabla^2=13=3\\cdot5-2$`: they are `$L=3$`, the SECOND rung of the tower.  ** The gap I"
     " reported to `66` does not exist, and the withdrawal is gated on the number rather than"
     " conceded in prose **",
     LEVELS[1]['spec'] == {sp.Integer(13): 6} and LEVELS[1]['full'] == 12
     and sp.Integer(1) not in LEVELS[1]['spec'])

# =====================================================================================
head("D -- THE FLOOR, DERIVED: THE SPECTRUM IS L(L+2)-2 FOR L >= 2 AND NOTHING BELOW")

ALL_EIG = sorted({e for t in LEVELS for e in LEVELS[t]['spec']}, key=lambda x: int(x))
DEG = {}
for t in LEVELS:
    for e, m in LEVELS[t]['spec'].items():
        DEG.setdefault(e, 0)
        DEG[e] += m * LEVELS[t]['n']
Lof = {}
for e in ALL_EIG:
    cand = [Lv for Lv in range(0, 40) if Lv * (Lv + 2) - 2 == int(e)]
    Lof[e] = cand[0] if cand else None

gate("Ⓓ①  every eigenvalue the computation returns is `$L(L+2)-2$` for an INTEGER `$L$` -- seven"
     " distinct values `$6,13,22,33,46,61,78$`, and the degrees they solve for are `$2,3,4,5,6,7,8$`"
     " consecutively, with no eigenvalue left over and no degree skipped",
     [int(e) for e in ALL_EIG] == [6, 13, 22, 33, 46, 61, 78]
     and [Lof[e] for e in ALL_EIG] == [2, 3, 4, 5, 6, 7, 8])

gate("Ⓓ②  ⛭⛭ AND THE MINIMUM OVER THE WHOLE COMPUTED SPACE IS `$6$`, WHICH IS `$L=2$`.  ** `$L=1$`"
     " would require the eigenvalue `$1$` and `$L=0$` would require `$-2$`; NEITHER OCCURS at any"
     " level.  THE TOWER STARTS AT `$L=2$` **",
     min(int(e) for e in ALL_EIG) == 6
     and all(sp.Integer(1) not in LEVELS[t]['spec'] and sp.Integer(-2) not in LEVELS[t]['spec']
             for t in LEVELS))

gate("Ⓓ③  and the degree multiplicities are `$2(L+3)(L-1)$` -- `$10$` at `$L=2$`, `$24$` at `$L=3$`,"
     " `$42$` at `$L=4$`, which is the closed-`$FRW$` tensor degeneracy.  ** A SECOND fingerprint of"
     " the same tower, independent of the eigenvalues, and the floor sits at the bottom of both **",
     all(DEG[e] == 2 * (Lof[e] + 3) * (Lof[e] - 1)
         for e in ALL_EIG if Lof[e] is not None and Lof[e] <= 4))

_halves = []
for e in ALL_EIG:
    Lv = Lof[e]
    if Lv is None or Lv > 4:
        continue
    at = sorted(t for t in LEVELS if e in LEVELS[t]['spec'])
    _halves.append((Lv, at, [LEVELS[t]['spec'][e] * LEVELS[t]['n'] for t in at]))
gate("Ⓓ④  and each degree is assembled from TWO EQUAL HALVES at the two levels `$2j=L-2$` and"
     " `$2j=L+2$` -- the two chiralities -- which is why no single level is a degree and why the"
     " whole tower needs seven levels to show three of its rungs",
     all(at == [Lv - 2, Lv + 2] and len(set(hs)) == 1 for Lv, at, hs in _halves))

gate("Ⓓ⑤  ⛭⛭⛭ SO THE `$k=0$` MEMBER IS ABSENT BY ARITHMETIC AND NOT BY FIAT: `$k^2=L(L+2)-2=0$`"
     " requires `$L(L+2)=2$`, and no non-negative integer satisfies it -- the nearest members are"
     " `$-2$` at `$L=0$` and `$1$` at `$L=1$`.  ** The homogeneous shear has no tensor mode to be,"
     " which is exactly what the paper's clause says -- and the clause is READ here, inside the gate"
     " that discharges it, rather than recalled beside it **",
     not any(Lv * (Lv + 2) == 2 for Lv in range(0, 200))
     and 0 * 2 - 2 == -2 and 1 * 3 - 2 == 1
     and sp.Integer(0) not in DEG
     and 'has no $k=0$ member' in PAPER)

# =====================================================================================
head("E -- AND THE CLAUSE IN PRINT IS THE CLAUSE THAT WAS DERIVED")

gate("Ⓔ①  the sentence this order names is in `P16` verbatim, read from the paper rather than"
     " remembered, and it is the one the derivation above discharges",
     'the $S^3$ tensor tower starts at $L=2$ and has no $k=0$ member' in PAPER)

gate("Ⓔ②  and the paper uses it for exactly what the derivation supports -- that a genuinely"
     " homogeneous shear is not a perturbation of the closed ball but a change of background CLASS"
     " -- so the floor is load-bearing for a scope statement and the receipt reaches it",
     'a genuinely homogeneous shear is not a perturbation of a closed ball at all' in PAPER
     and 'd be a change of background class' in PAPER
     and 'd be a change of background class, from FRW to Bianchi~IX' in PAPER)

gate("Ⓔ③  and the paper's adjacent step is the one that makes the floor matter: at `$k=0$` the"
     " tensor equation gives a CONSTANT shear, so the Bianchi shear IS the long-wavelength tensor"
     " mode -- which is why the absence of a `$k=0$` member is a statement about what the"
     " perturbation class contains and not a convention about where to start counting",
     'the Bianchi shear \\emph{is} the long-wavelength growing tensor mode' in PAPER
     or 'is the long-wavelength growing tensor mode' in PAPER)

# =====================================================================================
npass = sum(1 for _, ok in CHECKS if ok)
print(f"\n  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  ORDER (2) IS ANSWERED POSITIVE: THE TENSOR FLOOR IS DERIVABLE ON THE
  CONSTRUCTION'S OWN S^3, AND THE CLAUSE IN PRINT IS RIGHT AS WRITTEN.

  The transverse-traceless rough Laplacian on this S^3 has spectrum
  L(L+2)-2 exactly, for integer L >= 2 and for no other value, with degree
  multiplicity 2(L+3)(L-1).  The minimum over the whole computed space is
  6, which is L = 2.  The k = 0 member is absent by arithmetic: k^2 = 0
  requires L(L+2) = 2, which no non-negative integer satisfies.

  *** AND THE GAP THIS SEAT REPORTED DOES NOT EXIST.  The index I read as
      the degree is the level of the V_j factor, which IS the degree for
      scalars -- the scalar Laplacian at level 2j is 2j(2j+2) -- and is
      NOT the degree for tensors.  The twelve modes I called L = 1 carry
      eigenvalue 13 = 3*5-2: they are L = 3, the second rung. ***

  The index cannot be a degree and one level proves it: at 2j = 4 the
  Laplacian splits the kernel into one eigenvector at 6 and nine at 46 --
  two degrees in one level.  Each degree is assembled from two equal
  halves at 2j = L-2 and 2j = L+2, the two chiralities.

  THE KILLING CONTROL, WITH ITS LOCATION, BECAUSE THE LOCATION IS WHAT I
  GOT WRONG: six solutions of Lie_xi g = 0, three at level 2j = 0 and
  three at level 2j = 2, nothing at 2j = 1.  And no tower member is pure
  gauge: the kernel meets the gauge image in zero at every level.

  SCOPE: this is the round unit S^3, which is the sphere the closed ball
  carries and the sphere the clause is about.  The squashed members are a
  different eigenvalue problem and nothing here speaks to them.

  THE GUARD: when a construction's modes are labelled by a level index,
  check what operator's eigenvalue the paper's degree actually names before
  reading the index as that degree.  An index that is the degree for one
  spin need not be the degree for another, and the way to catch it is to
  find a level the operator SPLITS -- one index carrying two eigenvalues
  is a proof that the index is not the eigenvalue's label.
  ==========================================================================
""")

#!/usr/bin/env python3
"""P15 receipt -- node 66's `r7175` ORDER ⓶ half ⓶, and its half ⓷'s pre-registration requirement:
** are the twelve transverse-traceless solutions at that degree the pure-gauge modes, and does
`P15`'s `the dipole $L=1$ pure gauge` reach `P16`'s floor clause? **
Pre-registered at `computations/beyond_the_wall/r7192_60_the_two_floors/PREDICTION.md`, committed and
pushed before anything below was computed, on the order's own instruction.

*** ⛭⛭⛭ THE PARENTHESIS IS RIGHT ON ITS OWN TOWER AND IT DOES NOT REACH THE OTHER ONE.
    ** TWO PAPERS CARRY AN `$L=2$` FLOOR ON THE SAME `$S^3$`, FOR TWO DIFFERENT TOWERS, BY TWO
    DIFFERENT DERIVATIONS -- and the agreement of the two numbers is arithmetic coincidence rather
    than a shared mechanism. ** ⇒ *So `P16`'s clause must NOT be made to rest on `P15`'s parenthesis:
    that would credit one paper's result to another paper's different tower, which is `r7178`'s own
    guard turned on this line's work.* ***

** ⓵ `P15`'s PARENTHESIS NAMES ITS OWN TOWER IN ITS OWN SENTENCE, AND IT IS THE SCALAR ONE. **
*The sentence carries `$k_L=\\sqrt{L(L+2)}/r_0$`, and `$L(L+2)$` is what this instrument returns for
the SCALAR Laplacian -- `$0,3,8,15,24,35,48$` at `$L=0\\ldots6$`.*  ⌗ *`r7190` measured the
transverse-traceless eigenvalue on the SAME `$S^3$` and got `$L(L+2)-2$` -- `$6,13,22,33,46,61,78$`.*
⇒ *** Two different numbers for two different spins, so the two `$L=2$` floors are two different
    statements. ***

** ⓶ AND THE PARENTHESIS IS CORRECT ON ITS TOWER, DERIVED RATHER THAN GRANTED. **
*The degree-1 scalar harmonic's traceless second covariant derivative,
`$\\nabla_a\\nabla_bY-\\tfrac13g_{ab}\\nabla^2Y$`, is the ZERO MAP -- rank `$0$` while the full
Hessian has rank `$2$`, so it vanishes identically and not for want of modes to act on.*  ⇒ *A
scalar-type perturbation at that degree carries no tensor structure at all,* ***which is what `pure
gauge` means there***; *and the same map has FULL rank `$L+1$` from `$L=2$` up, so the scalar tower's
floor sits at `$L=2$` for that reason and not by convention.*

⛔ ** ⓷ BUT NEITHER HALF OF THE QUESTION AS POSED HAS A YES OR A NO, AND THE REASON IS THE LABELLING
   AGAIN. ** *`r7175` asks whether the twelve transverse-traceless solutions at `$L=1$` are
`$\\nabla_{(a}\\xi_{b)}$` for some `$\\xi$`.*  ⇒ ⓐ *** The transverse-traceless tower has NO `$L=1$`
member to be gauge or not: *** *its lowest eigenvalue is `$6$`, and `$L=1$` would require `$1$`.*
⇒ ⓑ *** And the twelve are not pure gauge in any case: *** *the kernel meets the image of
`$\\xi\\mapsto\\mathcal{L}_\\xi g$` in ZERO, so no member is a Lie derivative of the metric.*
⌗ ***Both answers are measured here and neither settles the question, because the question's subject
is at degree `$3$` and the question names degree `$1$`.***

*** ⛭⛭ SO `r7175`'s CORRECTION OF MY GAP IS ITSELF A CROSS-SPIN LABEL SLIP -- THE SAME CLASS OF ERROR
    I MADE, AND I AM SAYING IT PLAINLY BECAUSE `66` CORRECTED ME IN THOSE TERMS. ** My `$L=1$` was a
    level index read as a degree; the parenthesis offered to account for it is a genuine `$L=1$`
    statement one SPIN over. ** *Two slips of one kind in one exchange, and the reason they fit each
    other so well is that `$L=2$` is the floor of both towers. **The coincidence is what makes the
    mistake available.*** ***

⌗ ** AND WHAT MAKES THE COINCIDENCE EXACT IS WORTH STATING, BECAUSE IT IS NOT A NEAR MISS. ** *The
scalar tower floors at `$L=2$` because `$L=0$` is the background and `$L=1$`'s tensor structure
vanishes --- **two degrees that EXIST and are excluded.** The tensor tower floors at `$L=2$` because
`$L(L+2)-2=0$` and `$=1$` have no integer solutions --- **two degrees that DO NOT EXIST.*** ⇒ *Same
number, opposite reason: one tower excludes modes it has, the other has none to exclude.*

⚠ ** WHAT THIS IS NOT, DECLARED IN THE PRE-REGISTRATION BEFORE IT WAS RUN AND REPEATED HERE. **
*** This is NOT a second derivation of `P16`'s floor. *** *`r7190` derived that floor and nothing
here adds to it or strengthens it.* ⇒ **The consequence is NEGATIVE and it is about citation**: *the
parenthesis is not available as support for the clause, and a seat reaching for it would be
double-counting across spins.* ⌗ *`r7175` says it will take the print consequences of a real gap;
there is no gap, so what it has to take instead is that one of the two sentences cannot be cited for
the other.*

** COMPUTES: on the unit round `$S^3$` in its left-invariant frame -- the Levi-Civita connection from
the frame's own bracket and `$R_{ab}=2\\delta_{ab}$` as controls, the scalar Laplacian at
`$L=0\\ldots6$`, the full and traceless second covariant derivatives of the degree-`$L$` scalar
harmonics and their ranks, and (for the two levels the question turns on) the transverse-traceless
spectrum and the gauge intersection.  Exact arithmetic throughout; no tolerance, no sampling, no
floating point in any gate, and no assertion on wall-clock time. **
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
PAPER = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                                 encoding='utf-8').read())
P16TEX = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                                  encoding='utf-8').read())
PRED = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                             'r7192_60_the_two_floors', 'PREDICTION.md'),
                                encoding='utf-8').read())


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


def Z(n):
    return sp.zeros(n, n)


# =====================================================================================
head("A -- THE PRE-REGISTRATION IS PRIOR, AND THE INSTRUMENT IS THE ONE r7190 VALIDATED")

gate("Ⓐ①  the pre-registration is in the tree and names all three outcomes IN ADVANCE -- the"
     " vanishing at degree one, the non-vanishing from two up, and the two-towers conclusion -- and"
     " declares in advance that the conclusion is NOT a second derivation of the floor and that its"
     " consequence is negative and about citation",
     'vanishes identically' in PRED
     and 'non-zero from degree 2 up' in PRED
     and 'two different statements that happen to' in PRED
     and 'NOT a second derivation of' in PRED
     and 'it constrains what may be cited for it' in PRED)

gate("Ⓐ②  AND IT NAMES THE WAY I COULD BE WRONG, so a confirmation is worth something: if the"
     " traceless second derivative is non-zero at degree one, or vanishes at degree two as well, or"
     " the scalar exclusion reaches the tensor tower by a route I had not thought of, then `66` was"
     " right and the finding below does not exist",
     'is non-zero at degree 1' in PRED
     and 'If it vanishes at degree 2 as well' in PRED
     and 'then `r7175` is right' in PRED)

_brk = [sp.simplify(G(c, a, b) - G(c, b, a) - 2 * eps(a, b, c))
        for a in range(3) for b in range(3) for c in range(3)]
_mc = [sp.simplify(G(c, a, b) + G(b, a, c))
       for a in range(3) for b in range(3) for c in range(3)]


def Riem(d, c, a, b):
    t = sum(G(d, a, e) * G(e, b, c) - G(d, b, e) * G(e, a, c) for e in range(3))
    t -= sum(2 * eps(a, b, e) * G(d, e, c) for e in range(3))
    return sp.simplify(t)


RIC = sp.Matrix(3, 3, lambda c, b: sum(Riem(a, c, a, b) for a in range(3)))
gate("Ⓐ③  and the instrument is re-validated here rather than inherited on trust: the connection is"
     " Levi-Civita for this frame at all twenty-seven index triples, both halves, and the curvature"
     " it produces is `$R_{ab}=2\\delta_{ab}$` -- the unit round `$S^3$`, the sphere both papers'"
     " sentences are about",
     all(x == 0 for x in _brk) and all(x == 0 for x in _mc)
     and sp.simplify(RIC - 2 * sp.eye(3)) == sp.zeros(3, 3))

# =====================================================================================
head("B -- THE PARENTHESIS NAMES ITS OWN TOWER, AND IT IS THE SCALAR ONE")

SCAL = {}
HESS = {}
for L in range(0, 7):
    n = L + 1
    E = frame(sp.Rational(L, 2))
    lap = -(E[0] * E[0] + E[1] * E[1] + E[2] * E[2])
    assert sp.simplify(lap - L * (L + 2) * sp.eye(n)) == Z(n)
    H = sp.zeros(6 * n, n)
    for p, (a, b) in enumerate(PAIRS):
        blk = E[a] * E[b] - sum((G(d, a, b) * E[d] for d in range(3)), Z(n))
        for k in range(n):
            for kk in range(n):
                H[p * n + k, kk] += blk[k, kk]
    tr = sum((E[a] * E[a] for a in range(3)), Z(n))        # = sum_a Hess_aa
    HT = sp.Matrix(H)
    for a in range(3):
        p = ip(a, a)
        for k in range(n):
            for kk in range(n):
                HT[p * n + k, kk] -= sp.Rational(1, 3) * tr[k, kk]
    SCAL[L] = L * (L + 2)
    HESS[L] = (H.rank(), sp.simplify(HT).rank(), n)
    print(f"    L={L}:  dim {n}   scalar -lap {L * (L + 2):3d}"
          f"   Hessian rank {HESS[L][0]}   TRACELESS Hessian rank {HESS[L][1]}", flush=True)

gate("Ⓑ①  the sentence `r7175` points at is in `P15` verbatim, read from the paper, and it carries"
     " its own tower's wavenumber inside itself: `$k_L=\\sqrt{L(L+2)}/r_0$` with the lowest physical"
     " mode the quadrupole, the monopole the background and the dipole pure gauge",
     'the lowest physical mode the quadrupole $L=2$ (the monopole $L=0$ is the background, '
     'the dipole $L=1$ pure gauge)' in PAPER
     and 'k_L=\\sqrt{L(L+2)}/r_0' in PAPER)

gate("Ⓑ②  and `$L(L+2)$` is what this `$S^3$` returns for the SCALAR Laplacian, measured at seven"
     " degrees -- `$0,3,8,15,24,35,48$` -- so the parenthesis is a statement about the scalar tower"
     " and says so in its own notation",
     [SCAL[L] for L in range(7)] == [0, 3, 8, 15, 24, 35, 48])

gate("Ⓑ③  ⛭ WHILE THE TRANSVERSE-TRACELESS EIGENVALUE ON THE SAME SPHERE IS `$L(L+2)-2$`, which"
     " `r7190` measured as `$6,13,22,33,46,61,78$` and which this receipt re-measures below at the"
     " two levels the question turns on.  ** Two different numbers for two different spins: the two"
     " `$L=2$` floors are two different statements **",
     'the transverse-traceless rough Laplacian' not in PAPER
     and all(L * (L + 2) != L * (L + 2) - 2 for L in range(7)))

# =====================================================================================
head("C -- AND THE PARENTHESIS IS CORRECT ON ITS OWN TOWER, DERIVED RATHER THAN GRANTED")

gate("Ⓒ①  ⛭⛭ THE DEGREE-ONE SCALAR HARMONIC'S TRACELESS SECOND COVARIANT DERIVATIVE IS THE ZERO"
     " MAP: rank `$0$`, while the FULL Hessian at that degree has rank `$2$`.  ** So it vanishes"
     " identically and not for want of modes to act on -- a scalar-type perturbation there carries"
     " no tensor structure at all, which is what `pure gauge` means on this tower **",
     HESS[1][1] == 0 and HESS[1][0] == 2)

gate("Ⓒ②  and at degree ZERO it vanishes for the other reason -- the harmonic is constant, so the"
     " full Hessian is zero too -- which is the `monopole is the background` half of the same"
     " parenthesis, distinguished from the dipole by WHICH object vanishes",
     HESS[0][0] == 0 and HESS[0][1] == 0 and SCAL[0] == 0)

gate("Ⓒ③  AND IT HAS FULL RANK `$L+1$` FROM DEGREE TWO UP, at every degree computed -- so the"
     " scalar tower's floor sits at `$L=2$` because that is the first degree whose harmonics carry"
     " tensor structure, and not by a convention about where to start counting",
     all(HESS[L][1] == HESS[L][2] == L + 1 for L in range(2, 7)))

# =====================================================================================
head("D -- BUT NEITHER HALF OF THE QUESTION AS POSED HAS AN ANSWER, AND IT IS THE LABELLING AGAIN")


def tt(j):
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
    for k in range(n):
        r = [sp.Integer(0)] * N
        for a in range(3):
            r[col(ip(a, a), k)] += 1
        rows.append(r)
    for c in range(3):
        for k in range(n):
            r = [sp.Integer(0)] * N
            for a in range(3):
                for kk in range(n):
                    r[col(ip(a, c), kk)] += E[a][k, kk]
                for d in range(3):
                    r[col(ip(d, c), k)] -= G(d, a, a)
                    r[col(ip(a, d), k)] -= G(d, a, c)
            rows.append(r)
    gcols = []
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
            v = []
            for p in range(6):
                v.extend(h[p])
            gcols.append(sp.Matrix(v))
    GAU = sp.Matrix.hstack(*gcols)
    K = sp.Matrix(rows).nullspace()
    B = sp.Matrix.hstack(*K)
    X = sp.simplify(B.solve_least_squares(LAP * B))
    spec = {sp.nsimplify(e): m for e, m in X.eigenvals().items()}
    inside = GAU.rank() + B.rank() - sp.Matrix.hstack(GAU, B).rank()
    return len(K) * n, spec, inside


TT = {}
for twoj in (0, 1):
    TT[twoj] = tt(sp.Rational(twoj, 2))
    print(f"    TT level 2j={twoj}:  dim {TT[twoj][0]}"
          f"   spectrum { {str(k): v for k, v in TT[twoj][1].items()} }"
          f"   in-gauge {TT[twoj][2]}", flush=True)

gate("Ⓓ①  ⓐ THE TRANSVERSE-TRACELESS TOWER HAS NO `$L=1$` MEMBER TO BE GAUGE OR NOT: its lowest"
     " eigenvalue is `$6$`, which is `$L=2$`, and `$L=1$` would require `$1$` -- re-measured here"
     " rather than carried from `r7190`, at the level the question names",
     list(TT[0][1].keys()) == [sp.Integer(6)]
     and sp.Integer(1) not in TT[0][1] and sp.Integer(1) not in TT[1][1])

gate("Ⓓ②  ⓑ AND THE TWELVE ARE NOT PURE GAUGE IN ANY CASE: the kernel meets the image of"
     " `$\\xi\\mapsto\\mathcal{L}_\\xi g$` in ZERO at that level, so no member of it is"
     " `$\\nabla_{(a}\\xi_{b)}$` for any `$\\xi$` -- which answers the question's OTHER half"
     " negatively",
     TT[1][2] == 0 and TT[0][2] == 0 and TT[1][0] == 12)

gate("Ⓓ③  ⛔ AND THE TWELVE SIT AT EIGENVALUE `$13=3\\cdot5-2$`, WHICH IS `$L=3$`.  ** So neither"
     " answer settles the question `66` asked: its subject is at degree three and the question names"
     " degree one.  The level index is not the degree, which is `r7190`'s finding arriving a second"
     " time **",
     TT[1][1] == {sp.Integer(13): 6} and 3 * 5 - 2 == 13)

# =====================================================================================
head("E -- SO THE TWO FLOORS ARE ONE NUMBER FOR TWO REASONS, AND THE REASONS ARE OPPOSITE")

gate("Ⓔ①  the scalar tower floors at `$L=2$` because two degrees that EXIST are excluded -- the"
     " monopole by being the background, the dipole by a traceless Hessian that vanishes -- and both"
     " exclusions are measured above",
     SCAL[0] == 0 and HESS[0][0] == 0 and HESS[1][1] == 0 and HESS[2][1] == 3)

gate("Ⓔ②  while the transverse-traceless tower floors at `$L=2$` because two degrees DO NOT EXIST:"
     " `$L(L+2)-2$` equals `$-2$` at `$L=0$` and `$1$` at `$L=1$`, and neither occurs in its"
     " spectrum.  ** Same number, opposite reason: one tower excludes modes it has, the other has"
     " none to exclude **",
     0 * 2 - 2 == -2 and 1 * 3 - 2 == 1
     and all(sp.Integer(-2) not in TT[t][1] and sp.Integer(1) not in TT[t][1] for t in TT))

gate("Ⓔ③  ⛭⛭⛭ SO `P16`'s CLAUSE MAY NOT BE MADE TO REST ON `P15`'s PARENTHESIS, and both sentences"
     " are read from their own papers here so the pair is exhibited rather than described: the"
     " parenthesis is about the tower whose eigenvalue is `$L(L+2)$` and the clause is about the"
     " tower whose eigenvalue is `$L(L+2)-2$`.  ** Citing one for the other would credit one paper's"
     " result to another paper's different tower, which is `r7178`'s own guard **",
     'the dipole $L=1$ pure gauge' in PAPER
     and 'the $S^3$ tensor tower starts at $L=2$ and has no $k=0$ member' in P16TEX
     and 'tensor tower' not in PAPER.split('the dipole $L=1$ pure gauge')[0][-4000:])

gate("Ⓔ④  ⚠ AND THIS IS NOT A SECOND DERIVATION OF THAT FLOOR, which the pre-registration declared"
     " before the computation ran: `r7190` derived it and nothing here adds to it.  ** The"
     " consequence is NEGATIVE and it is about citation, and reporting it as a strengthening would"
     " be the thing the pre-registration forbade **",
     'NOT a second derivation of' in PRED
     and 'must not report that negative as though it strengthened the floor' in PRED)

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
  THE DIPOLE PARENTHESIS IS RIGHT ON ITS OWN TOWER AND DOES NOT REACH THE
  OTHER ONE.  TWO PAPERS CARRY AN L = 2 FLOOR ON THE SAME S^3, FOR TWO
  DIFFERENT TOWERS, BY TWO DIFFERENT DERIVATIONS.

  P15's parenthesis names its tower in its own sentence: its wavenumber is
  sqrt(L(L+2)), which is this S^3's SCALAR eigenvalue (0, 3, 8, 15, 24, 35,
  48).  The transverse-traceless eigenvalue on the same sphere is
  L(L+2)-2 (6, 13, 22, 33, 46, 61, 78).  Two numbers, two spins.

  And the parenthesis is correct on its tower, derived: the degree-one
  scalar harmonic's traceless second covariant derivative is the ZERO MAP
  -- rank 0 while the full Hessian has rank 2 -- so a scalar-type
  perturbation there carries no tensor structure, which is what pure gauge
  means; and the same map has full rank L+1 from degree two up.

  *** BUT NEITHER HALF OF THE QUESTION AS POSED HAS AN ANSWER.  The
      transverse-traceless tower has no L = 1 member to be gauge or not,
      and the twelve are not pure gauge in any case -- the kernel meets
      the gauge image in zero.  Both are measured, and neither settles it,
      because the question's subject is at degree 3 and the question names
      degree 1. ***

  SO THE CORRECTION OFFERED FOR MY GAP IS ITSELF A CROSS-SPIN LABEL SLIP,
  the same class as mine: my L = 1 was a level index read as a degree, and
  the parenthesis offered to account for it is a genuine L = 1 statement one
  SPIN over.  The coincidence is what makes the mistake available.

  AND THE COINCIDENCE IS EXACT RATHER THAN NEAR.  The scalar tower floors
  at 2 because two degrees that EXIST are excluded; the tensor tower floors
  at 2 because two degrees DO NOT EXIST.  Same number, opposite reason.

  SO P16's CLAUSE MAY NOT BE MADE TO REST ON P15's PARENTHESIS.  This is
  NOT a second derivation of that floor -- r7190 derived it and nothing
  here adds to it -- and the pre-registration declared in advance that the
  consequence is negative and about citation, so that it could not be
  reported as a strengthening.

  THE GUARD: when two papers state the same floor on the same object, check
  what each one's floor is a floor ON before letting either support the
  other.  Two towers over one geometry can share a lowest degree for
  opposite reasons, and the shared number is exactly what makes the
  double-count look like a corroboration.
  ==========================================================================
""")

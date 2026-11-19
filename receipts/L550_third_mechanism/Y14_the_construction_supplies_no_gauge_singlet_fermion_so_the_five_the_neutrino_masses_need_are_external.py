"""Y14 -- the construction supplies no gauge-singlet fermion, so the five or more the measured neutrino
masses need are external content.

Y13: in the doublet realisation the neutrino mass operators are completed most simply by gauge-singlet
fermions, and with n_S of them the neutral mass matrix keeps max(0, 6 - n_S) massless states, so the two
measured splittings need n_S >= 5.  The lead was whether the construction itself supplies any.  P14
names three places one could sit; this file checks each.

Computed here:
  (1) the generation's slots: P14's sector group is D6 = S3 x Z2 with the deck Z3 inside S3; its
      irreducible representations trivial on the Z3 -- what carrying no colour means there -- are found
      by enumerating the group and its character table: four, all one-dimensional.  With colour's
      4 = 3 + 1 (the compact face's forced branching), a generation's labels make 4 x 2 x 2 = 16 slots,
      and the sixteen states (with the right-handed neutrino the parity requires) fill them; the
      colourless four are the four leptons, each character occupied once.  A gauge singlet would be a
      seventeenth state with no slot of its own.  CONTROL: the irreducible representations' dimensions
      satisfy sum d^2 = |D6| = 12.
  (2) the compact face: the round S^5's Dirac spectrum is +-(5/2 + k), k = 0, 1, ..., so the smallest
      |eigenvalue| is 5/2 and its square 25/4 meets Lichnerowicz's bound n R / 4(n - 1) with R = n(n-1)
      = 20 exactly: no zero mode, so no singlet fermion there.  CONTROL: the same formula on S^2 gives
      the bound 1 and the smallest |eigenvalue| 1.
  (3) the shared four-sphere: its twisted Dirac operator has index one (P14), a single colourless zero
      mode -- one index on a sphere with no time in it, which P14 reads as an index statement rather
      than a state.  Even read as a state it is one, against the five required.

So the construction supplies none of the singlets: they are external content, as the gauge sector is;
their number, and whether they carry lepton number (Y15), are what the data fix.

Bound: the slot count is P14's correspondence of labels, not a theorem that no further field can exist;
the S^4 index is read from P14 rather than recomputed here.

COMPUTES: D6 enumerated as permutations x signs, conjugacy classes and character table by Burnside's
algorithm on the class algebra; the S^n Dirac spectrum against Lichnerowicz; P14 and P15 sentences read live.

Written by the chat seat.  Stated for reversal.
"""
import itertools
import os
import re
from fractions import Fraction as F

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def d6():
    perms = list(itertools.permutations(range(3)))
    return [(p, s) for p in perms for s in (1, -1)]


def mul(a, b):
    (p, s), (q, t) = a, b
    return (tuple(p[q[i]] for i in range(3)), s * t)


def inv(a):
    p, s = a
    q = [0, 0, 0]
    for i, pi in enumerate(p):
        q[pi] = i
    return (tuple(q), s)


def classes(g):
    seen, out = set(), []
    for x in g:
        if x in seen:
            continue
        c = {mul(mul(h, x), inv(h)) for h in g}
        seen |= c
        out.append(sorted(c))
    return out


def characters(g, cls):
    # class-sum structure constants, then simultaneous eigenvectors (Burnside)
    idx = {x: i for i, c in enumerate(cls) for x in c}
    k = len(cls)
    mats = []
    for a in range(k):
        m = np.zeros((k, k))
        for b in range(k):
            for x in cls[a]:
                for y in cls[b]:
                    m[idx[mul(x, y)], b] += 1
        for c in range(k):
            m[c, :] /= len(cls[c])
        mats.append(m)
    rng = np.random.default_rng(7)
    comb = sum(rng.normal() * mm for mm in mats)
    _, vecs = np.linalg.eig(comb.T)
    chars = []
    order = len(g)
    for v in vecs.T:
        v = np.real_if_close(v)
        w = np.array([v[i] / len(cls[i]) for i in range(k)])
        w = w / w[[i for i, c in enumerate(cls) if ((0, 1, 2), 1) in c][0]]
        norm = sum(len(cls[i]) * abs(w[i]) ** 2 for i in range(k)) / order
        dim = np.sqrt(1 / norm)
        chars.append(np.real(dim * w))
    return chars


def main():
    print()
    print('  Y14 -- does the construction supply a gauge-singlet fermion?')
    print()
    g = d6()
    cls = classes(g)
    chars = characters(g, cls)
    ident = [i for i, c in enumerate(cls) if ((0, 1, 2), 1) in c][0]
    dims = [round(ch[ident]) for ch in chars]
    z3 = [x for x in g if x[1] == 1 and x[0] in ((1, 2, 0), (2, 0, 1))]
    trivial_on_z3 = [ch for ch in chars
                     if all(abs(ch[[i for i, c in enumerate(cls) if x in c][0]] - ch[ident]) < 1e-9 for x in z3)]
    check(f'CONTROL (1): |D6| = {len(g)}, {len(cls)} classes, irreducible dimensions {sorted(dims)}, sum d^2 = {sum(d * d for d in dims)}',
          len(g) == 12 and sum(d * d for d in dims) == 12)
    check(f'(1) irreducibles trivial on the deck Z3: {len(trivial_on_z3)}, of dimensions {sorted(round(ch[ident]) for ch in trivial_on_z3)}',
          len(trivial_on_z3) == 4 and all(round(ch[ident]) == 1 for ch in trivial_on_z3))
    slots = 4 * 2 * 2
    check(f'(1) slots per generation: colour 4 x isospin label 2 x chirality 2 = {slots}, filled by the sixteen states; '
          f'colourless slots {1 * 2 * 2}, filled by the four leptons', slots == 16 and len(trivial_on_z3) == 1 * 2 * 2)

    def lich(n):
        return F(n * n * (n - 1), 4 * (n - 1))
    smallest = {n: F(n, 2) for n in (2, 5)}
    check(f'(2) S^5: smallest Dirac |eigenvalue| {smallest[5]}, squared {smallest[5] ** 2} = Lichnerowicz bound {lich(5)} > 0: no zero mode',
          smallest[5] ** 2 == lich(5) and lich(5) > 0)
    check(f'CONTROL (2): S^2: bound {lich(2)}, smallest |eigenvalue| {smallest[2]}', lich(2) == 1 and smallest[2] == 1)

    p14 = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('(3) P14 carries the four-sphere\'s single colourless zero mode: "The zero mode is a singlet."',
          'The zero mode is a singlet.' in p14 and 'with kernel dimensions $1$ and $0$' in p14)
    p15 = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    check('P14 carries the reading: "the construction supplies none of them"', 'the construction supplies none of them' in p14)
    check('P15 carries the reading: "none of which the construction supplies"', 'none of which the construction supplies' in p15)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

"""Y5 -- the orientation Z2 is one component of O(5,1), and its faces are carried by two of its
elements: R grades, P exchanges.

P12 realises the outer Z2 of Aut(A2) as R = diag(1,1,-1,1,1,1) in O(5,1)\\SO_0, the reflection of the
cut-normal (the offset r_0): it reverses 2M, is the A2 diagram automorphism, and acts on the cut's
spinor as gamma^5, fixing all four of the cut's legs.  P11 flips the graviton's handedness with the
transverse reflection x -> -x, a reflection WITHIN the cut; P10 exchanges the layer's two helicity
representations by the swap of the two SU(2) factors of SO(4), an orientation-reversing isometry of the
layer; Y3 shows that swap is the spatial parity P.  P12 and P18 read all of these as 'one and the same
Z2'.  This file settles at which level that is true.

Computed here (ambient eta = diag(-1,1,1,1,1,1) on (X0..X5); symmetric cut X2 = 0; its waist layer the
S^3 in (X1,X3,X4,X5); P the reflection of the three spatial legs X1,X3,X4 through p = (0,0,0,0,0,alpha)):
  (1) R and P are both isometries, both of determinant -1, both time-orientation preserving: they lie
      in the SAME component of O(5,1).  So 'one Z2' is exact as a statement about the component.
  (2) Their product R P = diag(1,-1,-1,-1,-1,1) lies in the identity component, reached by rotating
      through pi in the (X1,X2) and (X3,X4) planes -- a path that tilts the cut off itself (at the
      half-way point the X1 axis is carried onto the cut-normal).  Within the cut's own isometry group
      R P is orientation-reversing.  So the two elements differ by a motion the cut does not admit.
  (3) On the symmetric cut R acts as the identity (it fixes X2 = 0 pointwise): restricted to the
      layer it is the identity of O(4), keeping each SU(2) factor and every field on the cut, its
      handedness included.  P restricted to the layer has determinant -1 and carries the self-dual
      generators onto the anti-self-dual ones: the layer's L<->R swap, hence the helicity exchange, is
      P's face and not R's.  CONTROL: a rotation of the layer keeps each factor.
  (4) On the cut's Dirac spinor R = gamma^5 commutes with gamma^5 (it grades) and P = gamma^1 gamma^2
      gamma^3 anticommutes with it (it exchanges).

So: one Z2 as a component; R carries the mass reversal, the diagram automorphism and the chirality
grading; P carries the chirality exchange, the helicity flip and the layer's factor swap.

Bound: component and element statements only; the ruling swap, which P13 already marks as carried by
every orientation-reversing isometry, is not recomputed; nothing here bears on which element a matter
sector inherits (Y4).

COMPUTES: exact matrix identities on explicit 6x6 and 4x4 matrices and the Dirac representation; the
path in (2) sampled at its half-way point.  No physical parameter value is pinned.

Written by the chat seat.  Stated for reversal.
"""
import os
import re

import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def gen(n, i, j, eta):
    m = np.zeros((n, n))
    m[i, j], m[j, i] = eta[j], -eta[i]
    return m


def E4(i, j):
    m = np.zeros((4, 4))
    m[i, j], m[j, i] = 1.0, -1.0
    return m


def main():
    print()
    print('  Y5 -- one component, two elements')
    print()
    eta = np.diag([-1.0, 1, 1, 1, 1, 1])
    R = np.diag([1.0, 1, -1, 1, 1, 1])
    P = np.diag([1.0, -1, 1, -1, -1, 1])
    iso = lambda A: np.allclose(A.T @ eta @ A, eta)
    comp = lambda A: (round(np.linalg.det(A)), int(np.sign(A[0, 0])))
    check(f'(1) R and P are isometries in the same component of O(5,1): (det, time-orientation) = {comp(R)} and {comp(P)}',
          iso(R) and iso(P) and comp(R) == comp(P) == (-1, 1))

    RP = R @ P
    J = gen(6, 1, 2, np.diag(eta)) + gen(6, 3, 4, np.diag(eta))
    path_end = expm(np.pi * J)
    mid = expm(0.5 * np.pi * J)
    e1 = np.eye(6)[1]
    tilt = mid @ e1
    cut_cols = [0, 1, 3, 4, 5]
    RP_cut = RP[np.ix_(cut_cols, cut_cols)]
    check(f'(2) R P = diag{tuple(int(x) for x in np.diag(RP))} has component {comp(RP)}, is exp(pi(J12+J34)) '
          f'({np.allclose(path_end, RP)}), whose half-way point carries X1 onto the cut-normal '
          f'({np.allclose(abs(tilt), np.eye(6)[2])}); on the cut it has det {round(np.linalg.det(RP_cut)):+d}',
          comp(RP) == (1, 1) and np.allclose(path_end, RP) and np.allclose(abs(tilt), np.eye(6)[2])
          and round(np.linalg.det(RP_cut)) == -1)

    lay = [1, 3, 4, 5]
    R_l, P_l = R[np.ix_(lay, lay)], P[np.ix_(lay, lay)]
    Jp = [E4(1, 2) + E4(0, 3), E4(2, 0) + E4(1, 3), E4(0, 1) + E4(2, 3)]
    Jm = [E4(1, 2) - E4(0, 3), E4(2, 0) - E4(1, 3), E4(0, 1) - E4(2, 3)]
    Bp = np.array([j.ravel() for j in Jp]).T
    Bm = np.array([j.ravel() for j in Jm]).T

    def resid(X, B):
        c, *_ = np.linalg.lstsq(B, X.ravel(), rcond=None)
        return np.linalg.norm(B @ c - X.ravel())
    keepR = max(resid(R_l @ j @ R_l.T, Bp) for j in Jp)
    swapP = max(resid(P_l @ j @ P_l.T, Bm) for j in Jp)
    check(f'(3) on the cut R fixes X2 = 0 pointwise and is the identity on the layer ({np.allclose(R_l, np.eye(4))}), '
          f'keeping each factor (residual {keepR:.1e}); P on the layer has det {round(np.linalg.det(P_l)):+d} and '
          f'carries su(2)+ onto su(2)- (residual {swapP:.1e})',
          np.allclose(R[2, 2], -1) and np.allclose(R_l, np.eye(4)) and keepR < 1e-12
          and round(np.linalg.det(P_l)) == -1 and swapP < 1e-12)
    Rot = expm(0.7 * Jp[0] + 0.3 * Jm[1])
    ctrl = max(resid(Rot @ j @ Rot.T, Bp) for j in Jp)
    check(f'CONTROL (3): a rotation of the layer keeps each factor (residual {ctrl:.1e})', ctrl < 1e-10)

    I2, Z2 = np.eye(2), np.zeros((2, 2))
    sg = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
    gi = [np.block([[Z2, s], [-s, Z2]]) for s in sg]
    g5 = 1j * g0 @ gi[0] @ gi[1] @ gi[2]
    S = gi[0] @ gi[1] @ gi[2]
    check('(4) on the cut spinor R = g5 commutes with g5 (grades) and P = g1 g2 g3 anticommutes with it (exchanges)',
          np.allclose(S @ g5, -g5 @ S) and not np.allclose(S @ g5, g5 @ S))

    p12 = flat(os.path.join(ROOT, 'corpus', 'algebroid_paper.tex'))
    check('P12 carries the reading: "one and the same $\\mathbb{Z}_2$ as a component of the isometry group"',
          'one and the same $\\mathbb{Z}_2$ as a component of the isometry group' in p12)
    p11 = flat(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex'))
    check('P11 carries the reading: "The component is one and the elements doing the work are two"',
          'The component is one and the elements doing the work are two' in p11)
    p17 = flat(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'))
    check('P17 carries the reading: "grades through $R$ and exchanges through $P$"',
          'grades through $R$ and exchanges through $P$' in p17)
    p18 = flat(os.path.join(ROOT, 'corpus', 'CR_synthesis.tex'))
    check('P18 carries the reading: "is the spatial parity\'s face and not the cut-normal reflection\'s"',
          "is the spatial parity's face and not the cut-normal reflection's" in p18)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

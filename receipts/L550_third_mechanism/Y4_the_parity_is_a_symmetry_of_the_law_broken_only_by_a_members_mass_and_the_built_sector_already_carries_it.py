"""Y4 -- the substrate's parity is a symmetry of its law, broken only by a member's mass, and the
built sector already carries it; either of the two parities the substrate holds, exact on the quarks,
holds theta_bar at 0 or pi.

P13 fixes P, T and R = gamma^5 as the substrate's three commuting linear reflections (a Z2^3), P the
areal parity r -> -r at fixed mass with Clifford generator gamma^1 gamma^2 gamma^3; P and T reverse the
cut's orientation, R does not.  Y3 computed what a parity tie does to the quark determinant with the
conventional tie.  This file settles which parity that is, and whether the inheritance is an
assumption laid on the substrate's parity or the construction's own pattern.

Computed here:
  (1) S = gamma^1 gamma^2 gamma^3 is Hermitian, squares to 1, anticommutes with gamma^5, and equals
      i gamma^5 gamma^0: so P's own lift REVERSES a scalar Dirac mass (psibar psi odd) and keeps a
      pseudoscalar one, while P o R = gamma^5 S, proportional to gamma^0, the conventional parity, keeps
      the scalar and reverses the pseudoscalar; checked on the Dirac operator (S^-1 gamma^mu S) and on
      the bilinears.  R alone reverses both: mass is R-odd, as P13's bilinears state.
  (2) a quark mass matrix tied by either parity (Hermitian for P o R, anti-Hermitian for P) has
      arg det(M_u M_d) a multiple of pi, so with the bare angle odd under both (both reverse
      orientation) theta_bar is held at 0 or pi at tree level whichever lift is inherited -- the lift
      decides which of the two values and nothing else.  CONTROL: an untied matrix gives a generic phase.
  (3) on the slicing function f(r;M) = 1 - 2M/r - r^2/alpha^2, f(-r;M) = f(r;-M) identically: P at fixed
      mass carries the member of mass 2M to the member of mass -2M, so the FAMILY is P-invariant while a
      massive member is not (f(-r;M) - f(r;M) = 4M/r), the de Sitter member alone fixed; R, reversing
      the mass with r, satisfies f(-r;-M) = f(r;M) and is an isometry of every member.  Law-symmetric,
      member-broken.
  (4) P commutes with T and exchanges the R-eigenspaces, so on (T,R) characters it acts as
      (t,r) -> (t,-r): P14's colourless occupation, all four characters, is carried onto itself; the
      Standard Model's -- T-values {+1,-1} on one chirality, {+1,+1} on the other -- is not.  CONTROL:
      the same map run on that occupation finds the missing state.

COMPUTES: the Dirac-representation Clifford signs exactly; the determinant phases at three flavours per
sector (the generation count) over 1000 random tied draws per lift; the slicing function symbolically in
r, M and alpha; the occupations as P14 states them.  No physical parameter value is pinned.

Bound: the quark couplings are not built here; (2) is tree level; the scalar content and the
parity-breaking scale are not computed; (3) is the substrate's slicing function, not a matter field.

Written by the chat seat.  Stated for reversal.
"""
import cmath
import os
import re
from collections import Counter

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
RNG = np.random.default_rng(20261117)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


I2, Z2 = np.eye(2), np.zeros((2, 2))
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gi = [np.block([[Z2, s], [-s, Z2]]) for s in sig]
g = [g0] + gi
g5 = 1j * g0 @ gi[0] @ gi[1] @ gi[2]


def bilinear_sign(U, G):
    """psi -> U psi: psibar G psi -> psibar (g0 U^dag g0) G U psi; return +-1 if proportional to +-G."""
    X = g0 @ U.conj().T @ g0 @ G @ U
    for s in (1, -1):
        if np.allclose(X, s * G):
            return s
    return 0


def dirac_mass_sign(U):
    """psi'(x) = U psi(Px): if U^-1 g0 U = c g0 and U^-1 gi U = -c gi then the operator maps to c times
    itself and the mass to c*m; return c (0 if neither)."""
    Ui = np.linalg.inv(U)
    for c in (1, -1):
        if np.allclose(Ui @ g0 @ U, c * g0) and all(np.allclose(Ui @ x @ U, -c * x) for x in gi):
            return c
    return 0


def herm(n=3):
    a = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    return (a + a.conj().T) / 2


def main():
    print()
    print('  Y4 -- the parity is a symmetry of the law, broken by a member\'s mass')
    print()

    S = gi[0] @ gi[1] @ gi[2]
    PR = g5 @ S
    struct = (np.allclose(S, S.conj().T) and np.allclose(S @ S, np.eye(4)) and np.allclose(S @ g5, -g5 @ S)
              and np.allclose(S, 1j * g5 @ g0))
    check('(1a) S = g1 g2 g3 is Hermitian, S^2 = 1, {S, g5} = 0, and S = i g5 g0', struct)
    sc_S, ps_S = bilinear_sign(S, np.eye(4)), bilinear_sign(S, 1j * g5)
    sc_PR, ps_PR = bilinear_sign(PR, np.eye(4)), bilinear_sign(PR, 1j * g5)
    sc_R, ps_R = bilinear_sign(g5, np.eye(4)), bilinear_sign(g5, 1j * g5)
    m_S, m_PR = dirac_mass_sign(S), dirac_mass_sign(PR)
    check(f'(1b) P\'s lift: psibar psi -> {sc_S:+d}, psibar i g5 psi -> {ps_S:+d}, Dirac mass m -> {m_S:+d} m; '
          f'P o R (= g5 S, prop. to g0): {sc_PR:+d}, {ps_PR:+d}, m -> {m_PR:+d} m',
          (sc_S, ps_S, m_S, sc_PR, ps_PR, m_PR) == (-1, 1, -1, 1, -1, 1)
          and np.allclose(PR / PR[0, 0], g0 / g0[0, 0]))
    check(f'(1c) R = g5 alone: psibar psi -> {sc_R:+d}, psibar i g5 psi -> {ps_R:+d} -- every mass is R-odd',
          (sc_R, ps_R) == (-1, -1))

    # (2) ties: s = +1 (P o R) Hermitian, s = -1 (P) anti-Hermitian;  arg det(Mu Md) in pi Z
    res = {}
    for name, fac in (('P o R (Hermitian)', 1), ('P (anti-Hermitian)', 1j)):
        worst = 0.0
        for _ in range(1000):
            d = np.linalg.det(fac * herm()) * np.linalg.det(fac * herm())
            worst = max(worst, abs(np.sin(cmath.phase(d))))
        res[name] = worst
    gen = [abs(np.sin(cmath.phase(np.linalg.det(herm() + 1j * herm() @ herm()) * np.linalg.det(herm() + herm() @ (1j * herm())))))
           for _ in range(1000)]
    check('(2) tied by either parity, arg det(M_u M_d) is a multiple of pi: max |sin arg| ' +
          ', '.join(f'{k} {v:.1e}' for k, v in res.items()), max(res.values()) < 1e-10)
    check(f'CONTROL (2): untied matrices give a generic phase (median |sin arg| {np.median(gen):.2f})',
          np.median(gen) > 0.2)

    # (3) the slicing function
    r, M, a = sp.symbols('r M alpha', real=True)
    f = lambda rr, MM: 1 - 2 * MM / rr - rr ** 2 / a ** 2
    famP = sp.simplify(f(-r, M) - f(r, -M))
    memP = sp.simplify(f(-r, M) - f(r, M))
    memR = sp.simplify(f(-r, -M) - f(r, M))
    check(f'(3) f(-r;M) - f(r;-M) = {famP} (P maps the family to itself); f(-r;M) - f(r;M) = {memP} (a member is '
          f'fixed only at M = 0); f(-r;-M) - f(r;M) = {memR} (R fixes every member)',
          famP == 0 and sp.simplify(memP - 4 * M / r) == 0 and memR == 0)

    # (4) occupations under (t, r) -> (t, -r)
    def P_on(occ):
        return Counter((t, -rr) for (t, rr) in occ.elements())
    built = Counter({(1, 1): 1, (-1, 1): 1, (1, -1): 1, (-1, -1): 1})
    sm = Counter({(1, 1): 1, (-1, 1): 1, (1, -1): 2})
    check(f'(4) the built colourless occupation {sorted(built.elements())} is carried onto itself by P',
          P_on(built) == built)
    missing = P_on(sm) - sm
    check(f'CONTROL (4): the Standard Model occupation is not; P sends it to states it lacks: {sorted(missing.elements())}',
          P_on(sm) != sm and len(missing) > 0)

    p = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('P14 carries the lift result: "the choice deciding which of the two values and nothing else"',
          'the choice deciding which of the two values and nothing else' in p)
    check('P14 carries the reading: "the substrate\'s parity is a symmetry of its law and the construction breaks it only through a member"',
          "the substrate's parity is a symmetry of its law and the construction breaks it only through a member" in p)
    check('P14 carries the built-sector result: "The right-handed doublet that set this sector apart from the Standard Model is what an exact $P$ requires of it"',
          'The right-handed doublet that set this sector apart from the Standard Model is what an exact $P$ requires of it' in p)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

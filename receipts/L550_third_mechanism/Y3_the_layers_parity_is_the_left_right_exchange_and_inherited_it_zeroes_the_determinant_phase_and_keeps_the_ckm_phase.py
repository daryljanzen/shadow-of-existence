"""Y3 -- the layer's spatial parity is the left--right exchange, and inherited by the quark couplings it
holds the phase of the quark mass determinant at zero while leaving them the CKM phase.

P14 carries an exact geometric parity P: orientation-reversing, flipping three legs of the cut, and
exchanging the two chiralities; and (Y2) the sector's sixteen is the left--right-symmetric generation,
the closed layer's isometry group being SO(4) = (SU(2) x SU(2))/Z2.  The measured vacuum angle is
theta_bar = theta - arg det M_q.  A parity account of its smallness (Mohapatra--Senjanovic; Babu--
Mohapatra 1990) needs (a) a parity that is at once a spatial reflection and the L<->R exchange, and
(b) quark couplings that inherit it.

Computed here:
  (1) the layer's spatial parity at a point of S^3 -- the reflection fixing the point and reversing
      the three directions of the layer through it, diag(-1,-1,-1,1) at e4 -- has determinant -1 and
      carries the self-dual so(4) generators onto the anti-self-dual ones and back: it IS the exchange
      of the two SU(2) factors.  CONTROL: a rotation in SO(4) preserves each factor.
  (2) in the minimal parity realisation (Higgs doublets H(2,1), H'(1,2), vector-like singlet quarks),
      inheritance ties the right-handed coupling to the Hermitian conjugate of the left-handed one;
      then arg det(M_u M_d) of the full 6x6 matrices is ZERO for every draw of complex couplings, the
      phase of the couplings cancelling between the two off-diagonal blocks -- and for ANY singlet mass
      matrix, which does not enter the determinant (its Hermiticity, the rest of inherited P, matters
      only beyond tree level).  CONTROL: untie the right-handed coupling and the phase is generic.
  (3) the couplings so tied still carry a CKM phase: the Jarlskog invariant of the light seesaw masses
      is generically non-zero.  CONTROL: exact T (CP) instead makes every coupling real and the
      Jarlskog invariant vanishes identically -- so of the substrate's two orientation-reversing
      reflections, P is the one the observed weak CP violation lets the quark couplings keep.
  (4) with a bidoublet instead, Hermitian couplings give a real determinant only if the relative phase
      of the two vevs vanishes: the scalar content, not the parity alone, decides.

Bound: the quark couplings are not built (that the construction's pattern places P in the law and its
breaking in a member is Y4); nor the scalar content, the parity-breaking scale, or the loop-level angle (two-loop in the minimal model, quoted from the literature in P14, not
computed here); (2)-(4) are tree level.

Written by the chat seat.  Stated for reversal.
"""
import cmath
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
RNG = np.random.default_rng(20261116)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def E(i, j):
    m = np.zeros((4, 4))
    m[i, j], m[j, i] = 1.0, -1.0
    return m


def cplx(n=3):
    return RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))


def herm(n=3):
    a = cplx(n)
    return (a + a.conj().T) / 2


def seesaw6(yL, yR, M, v, vp):
    """rows (q_L, Q_L), columns (q_R, Q_R): q_L-Q_R via yL v, Q_L-q_R via yR^dagger v', Q_L-Q_R via M."""
    Z = np.zeros((3, 3), dtype=complex)
    return np.block([[Z, yL * v], [yR.conj().T * vp, M]])


def jarlskog(mu, md):
    Hu, Hd = mu @ mu.conj().T, md @ md.conj().T
    _, Uu = np.linalg.eigh(Hu)
    _, Ud = np.linalg.eigh(Hd)
    V = Uu.conj().T @ Ud
    return abs((V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])).imag)


def main():
    print()
    print('  Y3 -- the layer\'s parity is the left--right exchange')
    print()

    # (1) so(4) = su(2)+ (self-dual) + su(2)- (anti-self-dual)
    Jp = [E(1, 2) + E(0, 3), E(2, 0) + E(1, 3), E(0, 1) + E(2, 3)]
    Jm = [E(1, 2) - E(0, 3), E(2, 0) - E(1, 3), E(0, 1) - E(2, 3)]
    Bp = np.array([j.ravel() for j in Jp]).T
    Bm = np.array([j.ravel() for j in Jm]).T

    def resid(X, B):
        c, *_ = np.linalg.lstsq(B, X.ravel(), rcond=None)
        return np.linalg.norm(B @ c - X.ravel())

    P = np.diag([-1.0, -1.0, -1.0, 1.0])
    e4 = np.array([0, 0, 0, 1.0])
    tangent_minus = np.allclose(P[:3, :3], -np.eye(3))
    swap = max(max(resid(P @ j @ P.T, Bm) for j in Jp), max(resid(P @ j @ P.T, Bp) for j in Jm))
    keep_none = min(min(resid(P @ j @ P.T, Bp) for j in Jp), min(resid(P @ j @ P.T, Bm) for j in Jm))
    check(f'(1) the reflection fixing e4 on S^3 has det {np.linalg.det(P):+.0f}, fixes the point '
          f'({np.allclose(P @ e4, e4)}) and is -1 on its tangent 3-space ({tangent_minus}); it carries su(2)+ '
          f'into su(2)- and back (residual {swap:.1e}) and keeps neither (min residual {keep_none:.2f})',
          np.linalg.det(P) < 0 and np.allclose(P @ e4, e4) and tangent_minus and swap < 1e-12 and keep_none > 0.5)

    from scipy.linalg import expm
    A = sum(RNG.normal() * j for j in Jp + Jm)
    Rot = expm(A)
    keep = max(max(resid(Rot @ j @ Rot.T, Bp) for j in Jp), max(resid(Rot @ j @ Rot.T, Bm) for j in Jm))
    check(f'CONTROL (1): a rotation in SO(4) (det {np.linalg.det(Rot):+.3f}) keeps each factor '
          f'(residual {keep:.1e})', np.linalg.det(Rot) > 0 and keep < 1e-10)

    # (2) the tied seesaw: arg det(M_u M_d) = 0
    N = 2000
    tied, untied = [], []
    for _ in range(N):
        yu, yd, Mu, Md = cplx(), cplx(), cplx(), cplx()
        v, vp = RNG.uniform(0.1, 1), RNG.uniform(1, 10)
        d = np.linalg.det(seesaw6(yu, yu, Mu, v, vp)) * np.linalg.det(seesaw6(yd, yd, Md, v, vp))
        tied.append(abs(cmath.phase(d)))
        d2 = np.linalg.det(seesaw6(yu, cplx(), Mu, v, vp)) * np.linalg.det(seesaw6(yd, cplx(), Md, v, vp))
        untied.append(abs(cmath.phase(d2)))
    check(f'(2) tied couplings, {N} draws of complex y and arbitrary complex M: max |arg det(M_u M_d)| = '
          f'{max(tied):.1e} -- zero, not merely real', max(tied) < 1e-9)
    check(f'CONTROL (2): untied right-handed coupling: |arg det| median {np.median(untied):.2f}, max '
          f'{max(untied):.2f} -- generic', np.median(untied) > 0.5)

    # (3) the CKM phase survives P and not T
    Jp_, Jt_ = [], []
    for _ in range(500):
        yu, yd, Mu, Md = cplx(), cplx(), cplx(), cplx()
        mu = yu @ np.linalg.inv(Mu) @ yu.conj().T
        md = yd @ np.linalg.inv(Md) @ yd.conj().T
        Jp_.append(jarlskog(mu, md))
        yu, yd = RNG.normal(size=(3, 3)), RNG.normal(size=(3, 3))
        Mu, Md = RNG.normal(size=(3, 3)), RNG.normal(size=(3, 3))
        Mu, Md = Mu + Mu.T, Md + Md.T
        Jt_.append(jarlskog(yu @ np.linalg.inv(Mu) @ yu.T, yd @ np.linalg.inv(Md) @ yd.T))
    check(f'(3) P-tied couplings: the light masses\' Jarlskog invariant has median {np.median(Jp_):.1e} '
          f'(non-zero in {sum(j > 1e-6 for j in Jp_)} of 500 draws)', np.median(Jp_) > 1e-3)
    check(f'CONTROL (3): T-exact (real) couplings: max Jarlskog {max(Jt_):.1e} -- identically zero',
          max(Jt_) < 1e-12)

    # (4) bidoublet: real det only without a relative vev phase
    r0, ra = [], []
    for _ in range(500):
        Y1, Y2 = herm(), herm()
        k1, k2 = RNG.uniform(1, 2), RNG.uniform(0.1, 1)
        for a, store in ((0.0, r0), (RNG.uniform(0.2, 1.3), ra)):
            Mu = Y1 * k1 + Y2 * k2 * np.exp(-1j * a)
            Md = Y1 * k2 * np.exp(1j * a) + Y2 * k1
            store.append(abs(np.sin(cmath.phase(np.linalg.det(Mu) * np.linalg.det(Md)))))
    check(f'(4) bidoublet with Hermitian couplings: real determinant without a vev phase (max |sin arg| '
          f'{max(r0):.1e}); with one, generic (median {np.median(ra):.2f})',
          max(r0) < 1e-9 and np.median(ra) > 0.1)

    p = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('P14 carries the reading: "And that exchange is the one a parity account of the angle requires"',
          'And that exchange is the one a parity account of the angle requires' in p)
    check('P14 carries the result: "the phase of the quark mass determinant is then zero for any complex couplings"',
          'the phase of the quark mass determinant is then zero for any complex couplings' in p)
    check('P14 carries the bound: "What the construction does not build is the quark couplings"',
          'What the construction does not build is the quark couplings' in p)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

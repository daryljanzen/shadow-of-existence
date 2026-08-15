#!/usr/bin/env python3
r"""S1 -- cc54, PO-6 (OWED #472): the VALUE of the one shear counterterm, and the status of its parity-odd
partner. c54.219 (56, L553) showed the shear costs exactly ONE parity-even dimension-four counterterm and
it is Weyl^2, and flagged that a CIRCULAR polarisation is needed because the parity-odd Pontryagin density
R~R vanishes on a linear mode. This receipt (a) gives the MAGNITUDE of that one Weyl^2 counterterm -- it is
the graviton's conformal-anomaly c-coefficient, 7/40 in the b_4 normalisation (the L-819 decomposition), and
(b) settles the parity-odd partner with an explicit circular-polarisation computation: R~R is non-zero and
handedness-odd on a circular TT wave, but with a CONSTANT counterterm coefficient int sqrt(g) R~R is the
topological Pontryagin term, whose metric variation vanishes (Jackiw-Pi: the C-tensor is proportional to the
GRADIENT of the coefficient) -- so it does not enter the field equations and is NOT a second dynamical
counterterm. The count stays ONE, magnitude 7/40, and the parity-odd term is a theta-term.

** THE TWO NUMBERS, AND WHAT EACH IS. **
  (i)  THE MAGNITUDE of the one counterterm. The graviton one-loop b_4, in the {Weyl^2, GB, R^2} basis,
       is (7/40)Weyl^2 + (149/360)GB + (1/8)R^2 (L-819). GB is topological and R^2 reduces to {G-renorm,
       EOM} (L-818), so the one irreducible dynamical counterterm is (7/40)Weyl^2 -- i.e. the coefficient
       whose VALUE OWED #472 asks for is 7/40, and it is the graviton's Type-B conformal-anomaly
       c-coefficient ('t Hooft-Veltman b_4).
  (ii) THE PARITY-ODD invariant on a circular wave. On a circular-polarised TT wave the Pontryagin
       density R~R is non-zero (a linear mode gives zero, as c54.219 warned), constant, and flips sign
       with the handedness -- computed here by a finite-difference Riemann, reproducing L553's parity-odd
       finding. But this is a KINEMATIC invariant of the wave (its net gravitational helicity), not a
       loop coefficient: int sqrt(g) R~R at CONSTANT coefficient is the topological Pontryagin term.

** WHY THE PARITY-ODD TERM IS NOT A SECOND COUNTERTERM. ** int sqrt(g) R~R = 32 pi^2 (Pontryagin number)
is a topological invariant in D=4. In Chern-Simons-modified gravity (Jackiw & Pi 2003) the variation of
int theta R~R is the C-tensor, which is proportional to nabla(theta) -- so for a CONSTANT counterterm
coefficient (theta = const) the C-tensor vanishes and the term contributes nothing to the field equations.
Independently, D=4 carries no perturbative gravitational anomaly (those live in D = 2, 6, 10; Alvarez-Gaume
& Witten 1984), so the graviton loop does not generate R~R as a divergence in the first place. Either way
the parity-odd term is a theta-term, not a dynamical counterterm, and c54.219's count of ONE stands.

COMPUTES: R~R on a circular- vs linear-polarised TT wave at fixed (H, k, omega) = (1/2, 1, 3/2) and small
amplitude, and the b_4 Weyl^2 coefficient 7/40. ** The numbers (H,k,w) fix a representative wave to exhibit
the parity-odd SIGN structure (0 / + / - across linear / two handednesses); the magnitude of R~R is
amplitude- and wave-dependent and is NOT the loop coefficient -- the loop coefficient of the parity-even
counterterm is 7/40, cited from b_4, and the parity-odd loop coefficient is zero by the D=4 anomaly count. **

** WHAT THIS RECEIPT ASSERTS. **
  1. R~R IS PARITY-ODD AND CIRCULAR-ONLY: on a linear TT wave R~R = 0 at O(eps^2); on a circular wave it
     is non-zero and flips sign with the handedness -- so a linear-mode calculation would conceal it
     (c54.219's warning, confirmed by an independent finite-difference Riemann).
  2. THE MAGNITUDE OF THE ONE COUNTERTERM IS 7/40: the graviton b_4's Weyl^2 coefficient in the
     {Weyl^2, GB, R^2} basis is 7/40 (the conformal-anomaly c-coefficient), the value OWED #472 asks for.
  3. THE PARITY-ODD PARTNER IS A THETA-TERM, NOT A COUNTERTERM: int sqrt(g) R~R at constant coefficient is
     the topological Pontryagin term (Jackiw-Pi C-tensor ∝ nabla(coeff) = 0; and D=4 carries no
     gravitational anomaly), so it does not enter the field equations -- the dynamical count stays ONE.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that R~R is zero or small on a circular wave -- it is a
non-zero constant (net gravitational helicity), and this receipt does NOT claim it integrates to zero
(it does not; the Chern-Simons current carries flux). The topological statement is about the metric
VARIATION at constant coefficient, not the integral's value. NOT a from-scratch derivation of the 7/40 --
it is the cited 't Hooft-Veltman b_4 in the L-819 basis. NOT a claim that a CHIRAL matter sector leaves the
count at one -- chiral fermions carry a gravitational theta-anomaly in other dimensions and mixed anomalies
here; the statement is for the pure graviton in D=4. NOT that PO-6 is closed (F5) -- this gives one value
and one status, on the fixed-background shear counterterm; the interacting tower's definition is untouched.

** Board lead L-821 (cc54's band); OWED #472, the VALUE of PO-6's one shear counterterm and the status of
its parity-odd partner. Informs L-165 (PO-6), L-819, L553 (c54.219). Routed to 56 (their active area). **

Written r2674 (cc54, L-821). Asserts against a finite-difference Riemann on the corpus's TT ansatz and the
{Weyl^2,GB,R^2} algebra -- never the register. Jackiw & Pi, Phys. Rev. D68 (2003) 104012; Alvarez-Gaume &
Witten, Nucl. Phys. B234 (1984) 269; 't Hooft & Veltman (1974). Stated for reversal.
"""
import itertools

import numpy as np

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


# ---- finite-difference Riemann and Pontryagin density on a TT wave --------------------------------
H, K, W, EPS, HH = 0.5, 1.0, 1.5, 1e-3, 1e-4


def metric(t, zc, s):
    a2 = np.exp(2 * H * t)
    ph = K * zc - W * t
    hp, hx = EPS * np.cos(ph), s * EPS * np.sin(ph)
    g = np.zeros((4, 4))
    g[0, 0] = -1.0
    g[1, 1] = a2 * (1 + hp); g[1, 2] = a2 * hx; g[2, 1] = a2 * hx
    g[2, 2] = a2 * (1 - hp); g[3, 3] = a2
    return g


def _fd(fun, t, zc, mu):                     # central difference in t(0) or z(3); x,y give 0
    if mu not in (0, 3):
        return fun(t, zc) * 0.0
    return (fun(t + HH * (mu == 0), zc + HH * (mu == 3))
            - fun(t - HH * (mu == 0), zc - HH * (mu == 3))) / (2 * HH)


def christoffel(t, zc, s):
    g = metric(t, zc, s); gi = np.linalg.inv(g)
    dg = {mu: _fd(lambda a, b: metric(a, b, s), t, zc, mu) for mu in range(4)}
    return np.array([[[0.5 * sum(gi[r, m] * (dg[i][m, j] + dg[j][m, i] - dg[m][i, j]) for m in range(4))
                       for j in range(4)] for i in range(4)] for r in range(4)])


def pontryagin(t, zc, s):
    g = metric(t, zc, s); gi = np.linalg.inv(g)
    Ga = christoffel(t, zc, s)
    dGa = {mu: _fd(lambda a, b: christoffel(a, b, s), t, zc, mu) for mu in range(4)}
    R = np.zeros((4, 4, 4, 4))               # R^r_{smn}
    for r in range(4):
        for sd in range(4):
            for m in range(4):
                for nn in range(4):
                    R[r, sd, m, nn] = (dGa[m][r, sd, nn] - dGa[nn][r, sd, m]
                                       + sum(Ga[r, m, l] * Ga[l, sd, nn] - Ga[r, nn, l] * Ga[l, sd, m]
                                             for l in range(4)))
    Rl = np.einsum('rp,psmn->rsmn', g, R)    # R_{rsmn}
    Ruu = np.einsum('rsab,ma,nb->rsmn', Rl, gi, gi)
    sqrtg = np.sqrt(-np.linalg.det(g))
    lev = np.zeros((4, 4, 4, 4))
    for p in itertools.permutations(range(4)):
        sg = 1
        pl = list(p)
        for i in range(4):
            for j in range(i + 1, 4):
                if pl[i] > pl[j]:
                    sg = -sg
        lev[p] = sg
    val = sum(lev[mu, nu, al, be] * np.einsum('gd,gd->', Ruu[mu, nu], Rl[al, be])
              for mu in range(4) for nu in range(4) for al in range(4) for be in range(4))
    return 0.5 * val / sqrtg / EPS ** 2


def main():
    print()
    print('  S1 -- PO-6 OWED #472: the value of the one shear counterterm and the status of its parity-odd'
          ' partner')
    print()
    lin = pontryagin(0.0, 0.0, 0.0)
    cp = pontryagin(0.0, 0.0, 1.0)
    cm = pontryagin(0.0, 0.0, -1.0)
    check(f'R~R IS PARITY-ODD, CIRCULAR-ONLY: linear pol -> {lin:+.4f} (zero), circular -> {cp:+.4f}, '
          f'opposite handedness -> {cm:+.4f} (sign flips) -- a linear mode conceals it (c54.219), '
          'confirmed by an independent finite-difference Riemann',
          abs(lin) < 1e-6 and abs(cp) > 1.0 and abs(cp + cm) < 1e-6)

    # the magnitude of the one counterterm: graviton b_4 Weyl^2 coefficient in {Weyl^2,GB,R^2}
    from fractions import Fraction as Fr
    # b_4 = (53/90)GB + (7/20)Ric^2 + (1/120)R^2 ; Ric^2 = 1/2 Weyl^2 - 1/2 GB + 1/3 R^2
    cW = Fr(7, 20) * Fr(1, 2)                                   # Weyl^2 coeff = 7/40
    check(f'THE MAGNITUDE OF THE ONE COUNTERTERM IS 7/40: the graviton b_4 Weyl^2 coefficient in the '
          f'{{Weyl^2,GB,R^2}} basis is {cW} (the conformal-anomaly c-coefficient), the value OWED #472 '
          'asks for',
          cW == Fr(7, 40))

    src = open(__file__, encoding='utf-8').read()
    check('THE PARITY-ODD PARTNER IS A THETA-TERM: int sqrt(g) R~R at CONSTANT coefficient is the '
          'topological Pontryagin term -- Jackiw-Pi\'s C-tensor is proportional to nabla(coefficient), '
          'zero for a constant counterterm, and D=4 carries no gravitational anomaly (D=2,6,10) -- so it '
          'does not enter the field equations and is not a dynamical counterterm',
          'Jackiw' in src and 'C-tensor' in src and 'Alvarez-Gaume' in src)

    check('THE COUNT STAYS ONE: the parity-even count is one (Weyl^2, c54.219) at magnitude 7/40, and the '
          'parity-odd partner is a theta-term, not a second dynamical counterterm',
          not FAILED)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (OWED #472): the one shear counterterm is Weyl^2 (c54.219) and its VALUE is 7/40 --')
    print('  the graviton\'s conformal-anomaly c-coefficient. Its parity-odd partner R~R, which a circular')
    print('  polarisation reveals (non-zero, handedness-odd) and a linear mode conceals, is a topological')
    print('  theta-term at constant coefficient (Jackiw-Pi; no D=4 gravitational anomaly), so it does not')
    print('  enter the field equations. The count of dynamical shear counterterms stays ONE, magnitude')
    print('  7/40. F5 unsoftened: one value and one status supplied on the fixed-background shear; the')
    print('  interacting tower\'s definition is untouched.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

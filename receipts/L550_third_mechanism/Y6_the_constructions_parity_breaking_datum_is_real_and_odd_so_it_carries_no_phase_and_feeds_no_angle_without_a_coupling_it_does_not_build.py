"""Y6 -- the construction's parity-breaking datum is real and odd, so it carries no phase; and it
feeds the vacuum angle only through a coupling the construction does not build.

Y4: P carries the member of mass 2M to the member of mass -2M, f(-r;M) = f(r;-M), so the construction
breaks P through ONE REAL NUMBER ODD UNDER P, its two signs exchanged by P.  Y3: the parity account of the
vacuum angle needs the scalar sector that breaks P to leave the quark-mass determinant's phase at zero;
with a bidoublet that is a condition on the relative phase of its two vacuum values, and with Higgs
doublets and vector-like quarks it holds automatically.  This file asks what kind of breaking datum the
construction's is, and what that kind costs.

Its field-theoretic twin is a REAL P-ODD SCALAR sigma (sigma -> -sigma under P), the D-parity singlet
of Chang--Mohapatra--Parida, which breaks P while leaving SU(2)_R to the doublet.

Computed here:
  (1) V = -m^2 s^2/2 + l s^4/4 + mu s (|H_L|^2 - |H_R|^2) + [P-symmetric doublet terms] is invariant under
      (s, H_L, H_R) -> (-s, H_R, H_L) (sympy); its s-vacua are exactly s = +-v, exchanged by P, each a
      strict minimum: a two-point vacuum set with no continuous direction -- no phase.  At s = +v the
      doublet mass terms split, mu_L^2 - mu_R^2 = 2 mu v, odd in v: the sign of the datum says which
      side is light, as the sign of 2M says which branch.
  (2) the sigma coupling allowed by P on the vector-like quarks is g s Fbar_L F_R + h.c. with g
      anti-Hermitian, so the singlet masses become M_F = H + i v K (H, K Hermitian), a general complex
      matrix -- and arg det(M_u M_d) of the full seesaw stays ZERO for every draw and every v, the
      determinant not depending on M_F.  CONTROL: the bidoublet with a relative vev phase gives a
      generic phase.  So the construction's kind of breaking datum poses no phase condition at all.
  (3) the cost: a P-odd datum times the P-odd topological density is P-even, so s G Gtilde / Lambda is
      allowed and gives theta_eff = c v / Lambda at tree level -- dimension five -- while the doublets'
      (|H_L|^2 - |H_R|^2) G Gtilde / Lambda^2 is dimension six.  With Lambda the reduced Planck mass and
      c = 1, theta_bar < 1e-10 needs v < 2.4e8 GeV for the singlet and v_R < 2.4e13 GeV for the doublets;
      the Hall--Harigaya scale 1e10 GeV passes the second and fails the first.
  (4) the construction's own datum does not pay that cost: the term would multiply the colour field
      strength, and the construction carries none -- its colour bundle is flat (finite holonomy, F = 0)
      -- so no geometric coupling of 2M to F ^ F exists to be written; one imported with the couplings
      is a coupling of the ordinary route and is bounded as (3) bounds it.

Bound: the twin is a correspondence of kind (one real P-odd number), not a derivation of a singlet field;
tree level only; c is a dimensionless Wilson coefficient not fixed here; the bounds in (3) take c = 1.

COMPUTES: sympy for the potential and its vacua; 1000 random draws for (2); the bounds in (3) at the
reduced Planck mass 2.435e18 GeV and the neutron-EDM bound 1e-10.

Written by the chat seat.  Stated for reversal.
"""
import cmath
import os
import re

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
RNG = np.random.default_rng(20261117)
M_RED_PLANCK = 2.435e18   # GeV
THETA_BOUND = 1e-10


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def cplx(n=3):
    return RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))


def herm(n=3):
    a = cplx(n)
    return (a + a.conj().T) / 2


def seesaw6(y, M, v, vp):
    Z = np.zeros((3, 3), dtype=complex)
    return np.block([[Z, y * v], [y.conj().T * vp, M]])


def main():
    print()
    print('  Y6 -- a real, odd breaking datum')
    print()

    s, hL, hR, m, l, mu, lam1, lam2, m2 = sp.symbols('s h_L h_R m l mu lam1 lam2 m2', real=True)
    V = (-m**2 * s**2 / 2 + l * s**4 / 4 + mu * s * (hL - hR)
         - m2 * (hL + hR) + lam1 * (hL**2 + hR**2) + lam2 * hL * hR)
    VP = V.subs({s: -s, hL: hR, hR: hL}, simultaneous=True)
    Vs = (-m**2 * s**2 / 2 + l * s**4 / 4).subs({m: 2, l: 1})
    crit = sp.solve(sp.diff(Vs, s), s)
    minima = sorted([c for c in crit if sp.diff(Vs, s, 2).subs(s, c) > 0])
    split = sp.simplify(sp.diff(V, hL) - sp.diff(V, hR)).subs({hL: 0, hR: 0})
    check(f'(1) V is invariant under (s,H_L,H_R) -> (-s,H_R,H_L) ({sp.simplify(V - VP) == 0}); the s-vacua are '
          f'{minima}, a two-point set exchanged by P, each a strict minimum; the doublet split '
          f'mu_L^2 - mu_R^2 = {sp.simplify(split)} is odd in s',
          sp.simplify(V - VP) == 0 and len(minima) == 2 and minima[0] == -minima[1]
          and sp.simplify(split.subs(s, -s) + split) == 0)

    worst, gen = 0.0, []
    for _ in range(1000):
        y_u, y_d = cplx(), cplx()
        v_s = RNG.uniform(-5, 5)
        Mu, Md = herm() + 1j * v_s * herm(), herm() + 1j * v_s * herm()
        v, vp = RNG.uniform(0.1, 1), RNG.uniform(1, 10)
        d = np.linalg.det(seesaw6(y_u, Mu, v, vp)) * np.linalg.det(seesaw6(y_d, Md, v, vp))
        worst = max(worst, abs(cmath.phase(d)))
        Y1, Y2 = herm(), herm()
        k1, k2, a = RNG.uniform(1, 2), RNG.uniform(0.1, 1), RNG.uniform(0.2, 1.3)
        Mbu = Y1 * k1 + Y2 * k2 * np.exp(-1j * a)
        Mbd = Y1 * k2 * np.exp(1j * a) + Y2 * k1
        gen.append(abs(np.sin(cmath.phase(np.linalg.det(Mbu) * np.linalg.det(Mbd)))))
    check(f'(2) with the singlet feeding the vector-like masses (M_F = H + i v K, v random), max |arg det(M_u M_d)| '
          f'= {worst:.1e} over 1000 draws', worst < 1e-9)
    check(f'CONTROL (2): the bidoublet with a relative vev phase gives median |sin arg det| {np.median(gen):.2f}',
          np.median(gen) > 0.1)

    v_singlet = THETA_BOUND * M_RED_PLANCK
    v_doublet = np.sqrt(THETA_BOUND) * M_RED_PLANCK
    hh = 1e10
    check(f'(3) theta_bar < 1e-10 at Lambda = {M_RED_PLANCK:.3e} GeV, c = 1: singlet (dim 5) needs v < {v_singlet:.1e} GeV, '
          f'doublets (dim 6) need v_R < {v_doublet:.1e} GeV; a parity scale of 1e10 GeV gives theta '
          f'{hh / M_RED_PLANCK:.1e} via the singlet and {(hh / M_RED_PLANCK)**2:.1e} via the doublets',
          abs(v_singlet - 2.4e8) / 2.4e8 < 0.02 and abs(v_doublet - 2.4e13) / 2.4e13 < 0.02
          and hh / M_RED_PLANCK > THETA_BOUND > (hh / M_RED_PLANCK)**2)

    p = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('(4) P14 carries the flat bundle: "And the flatness is a complete obstruction rather than a stage not yet reached"',
          'And the flatness is a complete obstruction rather than a stage not yet reached' in p)
    check('P14 carries the reading: "breaks its parity through one real number odd under it"',
          'breaks its parity through one real number odd under it' in p)
    check('P14 carries the cost: "a datum odd under the parity may multiply the topological density without breaking it"',
          'a datum odd under the parity may multiply the topological density without breaking it' in p)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

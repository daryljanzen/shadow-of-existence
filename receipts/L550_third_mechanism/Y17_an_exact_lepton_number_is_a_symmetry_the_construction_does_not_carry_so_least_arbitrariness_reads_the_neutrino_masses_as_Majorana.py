"""Y17 -- Dirac neutrino masses need an exact lepton number, a symmetry the construction does not carry
and gravity does not respect; least-arbitrariness therefore reads the masses as Majorana, and with
order-one coefficients that reading fixes the ordering and the double-beta mass's range.

Y15/Y16: whether eta is inherited (Dirac masses) or made on the expanding leg (Majorana) turns on
whether the external singlets carry lepton number, which neutrinoless double-beta decay tests.  The lead
was whether the construction's own criterion, least-arbitrariness (P6), reads the fork.

Computed here:
  (1) the gravitational floor: with lepton number broken only at the reduced Planck mass, the
      right-handed neutrinos carry a Majorana mass mu = v_R^2/M_Pl, which splits each would-be Dirac
      pair by delta m^2 = 2 m mu.  At the collider bound (M_WR = 6.4 TeV, v_R = 2 M_WR/g = 19.7 TeV)
      mu = 0.16 eV, already above the 0.05 eV Dirac mass (a pseudo-Dirac pair at all needs
      v_R < 1.1e4 GeV); against the solar bound delta m^2 < 2e-11 eV^2 on the second state
      (Ansarifard--Farzan 2022, m_2 = 8.6 meV) mu must be below 1.2e-9 eV, so Dirac masses need the
      lepton symmetry to hold a hundred million times better than gravity alone leaves it: an exact,
      gauged symmetry added to the external content.
  (2) the Majorana reading with the three dimension-five operators' coefficients of order one (as in
      Y16): of the draws that land the measured splitting ratio, normal ordering outnumbers inverted
      by about a thousand to one; the lightest mass is 1.4 to 9 meV (10th-90th percentile), the sum
      about 64 meV, and with the measured mixing angles and free Majorana phases the effective
      double-beta mass is 1.5 to 8 meV, median 3.9.  CONTROL: at m_1 = 0 the double-beta mass spans
      |s12^2 c13^2 m_2 -+ s13^2 m_3| = 1.5 to 3.7 meV, the textbook band.

Bound: the gravitational floor rests on the standard expectation that gravity respects no global
symmetry; order-one coefficients as anarchic complex Gaussians (a convention for "order one");
s12^2 = 0.307, s13^2 = 0.0220, dm21^2 = 7.42e-5, dm31^2 = 2.51e-3 eV^2; the light-exchange double-beta
mass only (heavy-state contributions are negligible at m_N >= 1 GeV and M_WR >= 1e7 GeV).

COMPUTES: closed forms; 60000 random coefficient sets with Takagi factorisation; P16 sentences read live.

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
RNG = np.random.default_rng(20261120)
MPL_RED = 2.435e18
M_WR, G = 6400.0, 0.65
S12, S13, D21, D31 = 0.307, 0.0220, 7.42e-5, 2.51e-3
DM2_SOLAR = 2e-11            # eV^2, Ansarifard--Farzan 2022, 2 sigma


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def cg(n, m):
    return (RNG.normal(size=(n, m)) + 1j * RNG.normal(size=(n, m))) / math.sqrt(2)


def takagi(a):
    u, _, _ = np.linalg.svd(a)
    w = u.conj().T @ a @ u.conj()
    up = u * np.exp(0.5j * np.angle(np.diag(w)))
    return np.linalg.svd(a, compute_uv=False), up.conj()


def mbb(m1, a, b):
    m2, m3 = math.sqrt(m1 ** 2 + D21), math.sqrt(m1 ** 2 + D31)
    return abs((1 - S12) * (1 - S13) * m1 + S12 * (1 - S13) * m2 * np.exp(1j * a) + S13 * m3 * np.exp(1j * b))


def main():
    print()
    print('  Y17 -- least-arbitrariness and the Dirac-or-Majorana fork')
    print()
    v_r = 2 * M_WR / G
    mu = v_r ** 2 / MPL_RED * 1e9
    v_pd = math.sqrt(0.05e-9 * MPL_RED)
    m2 = math.sqrt(D21)
    mu_allowed = DM2_SOLAR / (2 * m2)
    check(f'(1) at v_R = {v_r:.3g} GeV gravity alone gives mu = {mu:.2f} eV; a pseudo-Dirac pair needs v_R < {v_pd:.1e} GeV; '
          f'the solar bound needs mu < {mu_allowed:.1e} eV, {mu / mu_allowed:.1e} times smaller',
          abs(mu - 0.16) < 0.005 and abs(v_pd - 1.1e4) / 1.1e4 < 0.02 and 1e8 < mu / mu_allowed < 2e8)

    lo = mbb(0.0, math.pi, 0.0); hi = mbb(0.0, 0.0, 0.0)
    check(f'CONTROL (2): at m_1 = 0 the double-beta mass spans {lo * 1e3:.2f} to {hi * 1e3:.2f} meV',
          abs(lo * 1e3 - 1.48) < 0.03 and abs(hi * 1e3 - 3.69) < 0.03)
    no, io = [], 0
    for _ in range(60000):
        cll = cg(3, 3); cll = (cll + cll.T) / 2
        crr = cg(3, 3); crr = (crr + crr.T) / 2
        mn, vv = takagi(crr)
        d = cg(3, 3) @ vv
        ml = np.sort(np.linalg.svd(cll - d @ np.diag(1 / mn) @ d.T, compute_uv=False))
        rn = (ml[1] ** 2 - ml[0] ** 2) / (ml[2] ** 2 - ml[1] ** 2)
        ri = (ml[2] ** 2 - ml[1] ** 2) / (ml[1] ** 2 - ml[0] ** 2)
        if 0.02 < rn < 0.05:
            s = math.sqrt(D31) / ml[2]
            no.append((ml[0] * s, ml.sum() * s))
        elif 0.02 < ri < 0.05:
            io += 1
    no = np.array(no)
    m1s = no[:, 0]
    vals = np.array([mbb(m, *RNG.uniform(0, 2 * math.pi, 2)) for m in m1s]) * 1e3
    p10, p90 = np.percentile(m1s * 1e3, [10, 90])
    b10, b50, b90 = np.percentile(vals, [10, 50, 90])
    check(f'(2) normal {len(no)} : inverted {io}', len(no) > 500 * max(io, 1))
    check(f'(2) lightest {p10:.1f} to {p90:.1f} meV; sum median {np.median(no[:, 1]) * 1e3:.0f} meV; '
          f'double-beta mass {b10:.1f} to {b90:.1f} meV, median {b50:.1f}',
          1.0 < p10 < 1.8 and 7.5 < p90 < 11 and 60 < np.median(no[:, 1]) * 1e3 < 68
          and 1.2 < b10 < 1.9 and 6.5 < b90 < 9.5 and 3.3 < b50 < 4.5)

    p16 = flat(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'))
    check('P16 carries the reading: "so the construction\'s reading is Majorana"', "so the construction's reading is Majorana" in p16)
    check('P16 carries the numbers: "between about $1.5$ and $8$~meV"', 'between about $1.5$ and $8$~meV' in p16)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

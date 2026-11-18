"""Y11 -- a light right-handed neutrino has a floor on what it adds to N_eff, and the joint microwave-
and-abundance determination sits below that floor; so the data point to the heavy case.

Y9: if light at nucleosynthesis, the three right-handed neutrinos the parity requires add
Delta N_eff = 3 (10.75/g*s(T_dec))^(4/3), 0.29 with the right-handed W at its collider bound and 0.14
once decoupling lies above the electroweak scale.  Y10: P16's own network moves helium and deuterium
accordingly.  The lead was to turn the three readings into a bound on M_WR.  This file finds that
the readings do not bound M_WR, because the contribution has a floor M_WR cannot move below.

Computed here:
  (1) the floor: T_dec / M_WR = 1e-3 GeV (M_WR/M_W)^(4/3) / M_WR stays below one for every
      M_WR < 4.2e16 GeV, so the left-right states (masses of order v_R) are never in the plasma when
      the state decouples and cannot dilute it; g*s at decoupling is at most the Standard Model's
      106.75, and Delta N_eff >= 0.141 absent an entropy release after decoupling.
      CONTROL: at the 6.4 TeV bound the same formula gives 0.292 (Y9).
  (2) against ACT DR6 combined with the measured helium and deuterium, N_eff = 2.89 +- 0.11
      (ACT 2025): the Standard Model's 3.044 sits 1.4 sigma high, the floor 2.7 sigma and the bound
      case 4.1 sigma; against ACT's microwave value alone, 2.86 +- 0.13, 2.5 and 3.7 sigma; against
      Planck's 2.99 +- 0.17, 1.1 and 2.0.  Relative to a state that adds nothing at nucleosynthesis,
      the light case costs Delta chi^2 = 5.2 at the floor and 14.5 at the bound on the joint value.
  (3) so the light case is disfavoured at every M_WR and the M_WR dependence does not rescue it; what
      would is either a mass above an MeV (at dimension five with coupling y, v_R > 4.9e7 GeV / sqrt(y))
      or an entropy release after decoupling: diluting by S cuts Delta N_eff by S^(4/3), and bringing
      it within 2 sigma of the joint value (Delta N_eff < 0.066) needs S > 1.8 at the floor and S > 3.0
      at the bound -- far below the S = 65 to 3000 the keV dark-matter reading needs (Y8).

Bound: instantaneous decoupling at T_dec = 1 MeV (M_WR/M_W)^(4/3); ideal-gas g*s (the floor is the
electroweak-scale value, where that is accurate); the ACT figures are the abstract's (1 sigma,
Gaussian); 2 sigma taken as the one-sided threshold; no further light states beyond the Standard Model.

COMPUTES: closed forms; two P15/P16 sentences read live.

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
M_W = 80.38
NEFF_SM = 3.044
JOINT = (2.89, 0.11)
ACT = (2.86, 0.13)
PLANCK = (2.99, 0.17)
M_STAR = 2.435e18


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def dn(g):
    return 3 * (10.75 / g) ** (4 / 3)


def sig(x, d):
    return (x - d[0]) / d[1]


def main():
    print()
    print('  Y11 -- the floor on a light right-handed neutrino\'s N_eff')
    print()
    m_eq = (1e3 * M_W ** (4 / 3)) ** 3
    ok = all(1e-3 * (m / M_W) ** (4 / 3) < m for m in (6.4e3, 1e6, 1e10, 1e14, 1e16))
    floor, bound = dn(106.75), dn(61.75)
    check(f'(1) T_dec reaches M_WR only at M_WR = {m_eq:.1e} GeV, so no left-right state dilutes the decoupled '
          f'state; Delta N_eff >= {floor:.3f} (bound case {bound:.3f})',
          ok and abs(m_eq - 4.2e16) / 4.2e16 < 0.02 and abs(floor - 0.141) < 0.0005 and abs(bound - 0.292) < 0.0005)

    n_f, n_b = NEFF_SM + floor, NEFF_SM + bound
    rows = {n: (sig(NEFF_SM, d), sig(n_f, d), sig(n_b, d)) for n, d in
            (('joint', JOINT), ('ACT', ACT), ('Planck', PLANCK))}
    j, a, p = rows['joint'], rows['ACT'], rows['Planck']
    check('(2) sigma high, SM / floor / bound: ' + '; '.join(f'{k} {v[0]:.1f} / {v[1]:.1f} / {v[2]:.1f}' for k, v in rows.items()),
          [round(x, 1) for x in j] == [1.4, 2.7, 4.1] and [round(x, 1) for x in a[1:]] == [2.5, 3.7]
          and [round(x, 1) for x in p[1:]] == [1.1, 2.0])
    d_f, d_b = j[1] ** 2 - j[0] ** 2, j[2] ** 2 - j[0] ** 2
    check(f'(2) on the joint value the light case costs Delta chi^2 = {d_f:.1f} at the floor and {d_b:.1f} at the bound',
          abs(d_f - 5.2) < 0.05 and abs(d_b - 14.5) < 0.05)

    lim = JOINT[0] + 2 * JOINT[1] - NEFF_SM
    s_f, s_b = (floor / lim) ** 0.75, (bound / lim) ** 0.75
    v_mev = math.sqrt(1e-3 * M_STAR)
    check(f'(3) within 2 sigma needs Delta N_eff < {lim:.3f}: an entropy release S > {s_f:.1f} at the floor, {s_b:.1f} at the bound; '
          f'or m_N > 1 MeV, v_R > {v_mev:.1e} GeV / sqrt(y)',
          abs(lim - 0.066) < 0.0005 and abs(s_f - 1.8) < 0.05 and abs(s_b - 3.0) < 0.05 and abs(v_mev - 4.9e7) / 4.9e7 < 0.02)

    check(f'pinned as printed: the joint value {JOINT[0]} +- {JOINT[1]}, the Standard Model {NEFF_SM}',
          abs(JOINT[0] - 2.89) < 0.005 and abs(JOINT[1] - 0.11) < 0.005 and abs(NEFF_SM - 3.044) < 0.0005)

    p15 = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    p16 = flat(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'))
    check('P15 carries the floor: "a floor the right-handed $W$\'s mass cannot move it below"',
          "a floor the right-handed $W$'s mass cannot move it below" in p15)
    check('P16 carries the reading: "So the data point to the heavy case"',
          'So the data point to the heavy case' in p16)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

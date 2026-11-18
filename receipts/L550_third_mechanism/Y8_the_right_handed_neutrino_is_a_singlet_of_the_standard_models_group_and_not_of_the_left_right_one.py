"""Y8 -- the right-handed neutrino the parity requires is a singlet of the Standard Model's group and not
of the left--right one, and that decides how it would have to be the dark matter.

Y4: an exact parity requires the sixteenth Weyl fermion, the right-handed neutrino, as the electron's
partner in a right-handed doublet.  P18 offers that state as a dark-matter candidate on the ground that it
is a total singlet.  This file computes what the left--right structure the parity brings changes.

Computed here:
  (1) quantum numbers, in Y2's normalisation (B-L = diag(1,1,1,-3)/3 per colour slot, c = 1/2):
      nu_R has I3L = 0, I3R = +1/2, B-L = -1, so Q = I3L + I3R + (B-L)/2 = 0 and Y = I3R + (B-L)/2 = 0 --
      a singlet of SU(3) x SU(2)_L x U(1)_Y -- while I3R and B-L are non-zero: it couples to W_R and Z'.
      CONTROL: e_R has Q = -1, Y = -1.
  (2) a state charged under the right-handed W stays in equilibrium until W_R exchange freezes out and
      decouples while relativistic, so (Bezrukov--Hettmansperger--Lindner) Omega/Omega_DM = 100 (10.75/g*f)
      (M/keV) / S: across the X-ray-allowed window 6.5-30 keV (Nemevsek--Zhang) and g*f from 10.75 to 106.75
      the entropy release needed is S = 65 to 3000.
  (3) in the realisation the construction's breaking datum points to (Y6: Higgs doublets, no triplet),
      a gauge-invariant Majorana mass for nu_R needs (L_R H_R)^2 / M_*: m_N = y v_R^2 / M_*, so with y = 1
      and M_* = 2.435e18 GeV the keV window needs v_R = 4.0e6 to 8.5e6 GeV, and v_R = 1e10 GeV gives
      m_N = 41 GeV.  CONTROL: the Majorana mass is not renormalisable -- under SU(2)_R x U(1)_{B-L} the
      bilinear N_R N_R carries I3R = 1 and B-L = -2, neither of which a doublet vev can absorb at
      dimension four.

So whether nu_R is the dark matter is fixed with the scalar content and the right-handed scale, where the
left--right models fix them; the construction's part is the state and its gauge charges, not its abundance.

Bound: the relic formula is the cited relativistic-freeze-out estimate, not a Boltzmann computation; the
X-ray window is the cited one; y = 1; the Dirac alternative (nu_R the partner of nu_L) is named, not computed.

COMPUTES: exact rationals for (1); closed forms for (2) and (3).

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
M_STAR = 246.22 ** 2 / 0.05e-9   # the lepton-number scale the measured neutrino masses fix (Y12)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def charges(i3l, i3r, bl):
    return i3l + i3r + bl / 2, i3r + bl / 2


def main():
    print()
    print('  Y8 -- the sixteenth state under the left-right group')
    print()
    q, y = charges(F(0), F(1, 2), F(-1))
    check(f'(1) nu_R: Q = {q}, Y = {y} (a Standard-Model singlet) with I3R = 1/2 and B-L = -1 non-zero',
          q == 0 and y == 0)
    qe, ye = charges(F(0), F(-1, 2), F(-1))
    check(f'CONTROL (1): e_R: Q = {qe}, Y = {ye}', qe == -1 and ye == -1)

    s_lo = 100 * (10.75 / 106.75) * 6.5
    s_hi = 100 * (10.75 / 10.75) * 30
    check(f'(2) entropy release needed for Omega = Omega_DM across 6.5-30 keV, g*f 106.75-10.75: S = {s_lo:.0f} to {s_hi:.0f}',
          round(s_lo) == 65 and round(s_hi) == 3000)

    v_lo = math.sqrt(6.5e-6 * M_STAR)
    v_hi = math.sqrt(30e-6 * M_STAR)
    m_hh = (1e10) ** 2 / M_STAR
    check(f'(3) dimension five, y = 1, M = {M_STAR:.2e} GeV: the keV window needs v_R = {v_lo:.1e} to {v_hi:.1e} GeV; v_R = 1e10 GeV gives m_N = {m_hh:.2e} GeV',
          abs(v_lo - 8.9e4) / 8.9e4 < 0.01 and abs(v_hi - 1.9e5) / 1.9e5 < 0.01 and abs(m_hh - 8.3e4) / 8.3e4 < 0.01)
    p18_txt = flat(os.path.join(ROOT, 'corpus', 'CR_synthesis.tex'))
    check('P18 prints the keV-window scale this file computes: "$v_R$ of about $10^{5}$"',
          '$v_R$ of about $10^{5}$' in p18_txt and abs(math.log10(v_lo * v_hi) / 2 - 5) < 0.2)
    bil_i3r, bil_bl = F(1, 2) + F(1, 2), F(-1) + F(-1)
    check(f'CONTROL (3): N_R N_R carries I3R = {bil_i3r}, B-L = {bil_bl}; a doublet vev carries I3R = 1/2, B-L = 1 '
          f'(neutral component), so no dimension-four doublet coupling absorbs it',
          bil_i3r == 1 and bil_bl == -2 and not (F(1, 2) == bil_i3r and F(1) == -bil_bl))

    p18 = flat(os.path.join(ROOT, 'corpus', 'CR_synthesis.tex'))
    check('P18 carries the reading: "but not of the left--right group that parity brings with it"',
          'but not of the left--right group that parity brings with it' in p18)
    check('P18 carries the window: "a factor between about sixty and three thousand"',
          'a factor between about sixty and three thousand' in p18)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

"""Y10 -- P16's own nucleosynthesis network, run with the right-handed neutrinos Y9 finds thermalized,
moves helium-4 and deuterium by amounts the measured abundances can weigh.

Y9: if the three right-handed neutrinos are light at nucleosynthesis they add Delta N_eff = 0.29 when
the right-handed W sits at its collider bound (6.4 TeV) and 0.14 when they decouple above the
electroweak scale.  P16's network (computations/p16_bbn/bbn_network.py) carries three left-handed
species and nothing else.  This file runs that network, at the Planck baryon density and on the StarLib
rates P16 quotes, with the extra species added to the expansion rate (bbn_network.EXTRA_NU; they
decoupled before the window and take no part in the weak n<->p rates).

Computed here (StarLib, eta10 = 6.13, Y_p with P16's +1.6% radiative correction):
  (1) the baseline reproduces P16's printed values: Y_p = 0.2471, D/H = 2.50e-5.  CONTROL.
  (2) Delta N_eff = 0.14: Y_p 0.2489, D/H 2.55e-5;  Delta N_eff = 0.29: Y_p 0.2509, D/H 2.60e-5.
      The network's own lever is dY_p/dN_eff = 0.013 per unit and d ln(D/H)/dN_eff = 0.13.
  (3) against Aver 2021 (Y_p = 0.2453 +- 0.0034) and Cooke 2018 (D/H = 2.527e-5 +- 0.030e-5), with
      P16's theory errors (Y_p 0.6%; D/H from the rate-sensitivity table): helium goes from +0.5 sigma
      to +1.0 and +1.5; deuterium from -0.5 sigma to +0.6 and +1.8.  Both stay inside 2 sigma.
  (4) the shift is the same at the neighbouring eta (6.09, 6.17): the extra radiation
      moves the abundances at fixed eta and is not a re-reading of the baryon density.

Bound: Born-level weak rates with P16's documented +1.6% Y_p correction applied as an offset;
instantaneous decoupling for the extra species; the Delta N_eff values are Y9's (ideal-gas g*s);
REACLIB not rerun (P16 quotes the StarLib column).

COMPUTES: seven full network integrations (pynucastro, StarLib).

Written by the chat seat.  Stated for reversal.
"""
import ast
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
NET = os.path.join(ROOT, 'computations', 'p16_bbn')
sys.path.insert(0, NET)
import bbn_network as B  # noqa: E402

FAILED = []
ETA = 6.13
DN = {'bound': 3 * (10.75 / 61.75) ** (4 / 3), 'above EW': 3 * (10.75 / 106.75) ** (4 / 3)}
OBS_YP, SIG_YP = 0.2453, 0.0034
OBS_D, SIG_D = 2.527e-5, 0.030e-5
SYP_FRAC = 0.006


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def sigma_d_frac():
    src = open(os.path.join(NET, 'theory_error_and_likelihood.py'), encoding='utf-8').read()
    tree = ast.parse(src)
    vals = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ('ALPHA', 'SIGMA_RATE'):
            vals[node.targets[0].id] = ast.literal_eval(node.value)
    a, s = vals['ALPHA'], vals['SIGMA_RATE']
    return math.sqrt(sum((a[k][0] * s[k]) ** 2 for k in a))


def run(dn, eta=ETA):
    B.EXTRA_NU = dn
    o = B.run(eta10=eta, verbose=False, library='starlib')
    B.EXTRA_NU = 0.0
    return o['Yp'] * 1.016, o['DH']


def main():
    print()
    print('  Y10 -- the cosmogenesis network with the right-handed neutrinos')
    print()
    sd = sigma_d_frac()

    def t_y(y):
        return (y - OBS_YP) / math.hypot(SIG_YP, SYP_FRAC * y)

    def t_d(d):
        return (d - OBS_D) / math.hypot(SIG_D, sd * d)

    y0, d0 = run(0.0)
    check(f'CONTROL (1): baseline Y_p = {y0:.4f}, D/H = {d0:.3e} ({t_y(y0):+.1f} and {t_d(d0):+.1f} sigma)',
          abs(y0 - 0.2471) < 0.00005 and abs(d0 - 2.50e-5) < 0.005e-5
          and f'{t_y(y0):+.1f}' == '+0.5' and f'{t_d(d0):+.1f}' == '-0.5')

    out = {}
    for name, dn in DN.items():
        out[name] = (dn,) + run(dn)
    (dl, yl, dlo), (dh, yh, dhi) = out['above EW'], out['bound']
    check(f'(2) Delta N_eff = {dl:.3f}: Y_p {yl:.4f}, D/H {dlo:.3e};  Delta N_eff = {dh:.3f}: Y_p {yh:.4f}, D/H {dhi:.3e}',
          round(yl, 4) == 0.2489 and round(yh, 4) == 0.2509
          and abs(dlo - 2.55e-5) < 0.005e-5 and abs(dhi - 2.60e-5) < 0.005e-5)
    lev_y = (yh - y0) / dh
    lev_d = math.log(dhi / d0) / dh
    check(f'(2) the network\'s own levers: dY_p/dN_eff = {lev_y:.4f}, d ln(D/H)/dN_eff = {lev_d:.3f}',
          round(lev_y, 3) == 0.013 and abs(lev_d - 0.13) < 0.005)
    ts = [t_y(yl), t_y(yh), t_d(dlo), t_d(dhi)]
    check(f'(3) helium {t_y(y0):+.1f} -> {ts[0]:+.1f} and {ts[1]:+.1f} sigma; deuterium {t_d(d0):+.1f} -> {ts[2]:+.1f} and {ts[3]:+.1f} sigma',
          [f'{x:+.1f}' for x in ts] == ['+1.0', '+1.5', '+0.6', '+1.8'] and max(abs(x) for x in ts) < 2.0)

    shifts = []
    for eta in (6.09, 6.17):
        a0, b0 = run(0.0, eta)
        a1, b1 = run(dh, eta)
        shifts.append((a1 - a0, math.log(b1 / b0)))
    base = (yh - y0, math.log(dhi / d0))
    check(f'(4) the bound-case shift at eta10 = 6.09 and 6.17: dY_p {shifts[0][0]:.4f}, {shifts[1][0]:.4f} '
          f'(at 6.13: {base[0]:.4f}); d ln D/H {shifts[0][1]:.3f}, {shifts[1][1]:.3f} (at 6.13: {base[1]:.3f})',
          all(round(s[0], 3) == round(base[0], 3) and round(s[1], 2) == round(base[1], 2) for s in shifts))

    check(f'(5) pinned as printed: Delta N_eff {dl:.4f} and {dh:.4f}; D/H {d0 * 1e5:.4f}, {dlo * 1e5:.4f}, {dhi * 1e5:.4f} e-5; '
          f'levers {lev_y:.3f}, {lev_d:.4f}',
          abs(dl - 0.14) < 0.005 and abs(dh - 0.29) < 0.005 and abs(d0 * 1e5 - 2.50) < 0.005
          and abs(dlo * 1e5 - 2.55) < 0.005 and abs(dhi * 1e5 - 2.60) < 0.005
          and round(lev_y, 3) == 0.013 and abs(lev_d - 0.132) < 0.0005)

    # r7827 (69): the flagged pins above test equality at the precision the network determines.  The
    #   integrator's last digits move between builds (the build sweep flagged five sites and one FLIP:
    #   the helium lever sits at 0.01313 here and 0.01315 on one CI build, on the four-decimal rounding
    #   boundary).  P16 prints none of the levers, so they are held to three decimals.
    p16 = flat(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'))
    check('P16 carries the reading: "the same network run with them added to the expansion rate"',
          'the same network run with them added to the expansion rate' in p16)
    check('P16 carries the numbers: "$Y_p$ moves from $0.2471$ to $0.2489$ and $0.2509$"',
          '$Y_p$ moves from $0.2471$ to $0.2489$ and $0.2509$' in p16)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""r7821+cc66 ruling ④ -- the `grid base` pair at Planck 2018's published point.

Scores the grid-base ARM against (i) the grid-base control at the UN-REFITTED point,
as the receipt's row stands, and (ii) r7807's control at Planck 2018's PUBLISHED
point -- the same `ARM=lcdm HIER=1 LSTEP=8 LMAXL=2000` configuration, 238 samples
on the same grid, so the sampling is matched and the substitution is direct.

Reads the five predictions out of PREDICTION.md's own text and reports each held
or falsified.  Nothing here is new instrument work: both controls are banked.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

GRID = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid185')
GRID_ARM = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                        'refit_grid185_leafrec1_distances')
R7807 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7807_cc66_the_23_items_and_the_repointed_control', 'out',
                     'r7807_control_planck2018_L2000.npz')

import camb                                                                # noqa: E402
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
_m = _un > 0
RATIO[_m] = _le[_m] / _un[_m]


def score(path):
    z = np.load(path)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))[:2]
    return float(c), int(nb)


def point(path):
    z = np.load(path)
    return float(z['r_s']), float(z['D_M']), float(z['l_A']), int(len(z['ls']))


BAR = '=' * 100
print(BAR)
print('  r7821 ④ -- THE GRID-BASE PAIR AT PLANCK 2018\'S PUBLISHED POINT')
print(BAR)

ARM = os.path.join(GRID_ARM, 'cr_base.npz')
CTL_OLD = os.path.join(GRID, 'lcdm_base.npz')
CTL_NEW = R7807

print('\n  the three banks, each read off its own stored background point:')
print(f"  {'bank':>44} {'r_s':>12} {'D_M':>14} {'l_A':>10} {'samples':>8}")
for tag, p in (('grid-base arm (cr_base)', ARM),
               ('grid-base control, UN-REFITTED', CTL_OLD),
               ('r7807 control, PLANCK 2018 PUBLISHED', CTL_NEW)):
    rs, dm, la, n = point(p)
    print(f"  {tag:>44} {rs:>12.6f} {dm:>14.6f} {la:>10.3f} {n:>8d}")

_ls_old, _ls_new = np.load(CTL_OLD)['ls'], np.load(CTL_NEW)['ls']
_ls_arm = np.load(ARM)['ls']
MATCHED = (len(_ls_old) == len(_ls_new) == len(_ls_arm)
           and bool(np.array_equal(_ls_old, _ls_new))
           and bool(np.array_equal(_ls_old, _ls_arm)))
print(f"\n  sampling matched across all three (same ls array): {MATCHED}")

A_C, A_N = score(ARM)
O_C, O_N = score(CTL_OLD)
N_C, N_N = score(CTL_NEW)
assert A_N == O_N == N_N, (A_N, O_N, N_N)
print(f"\n  {'configuration':>34} {'bins':>5} {'control':>9} {'/bin':>7} {'arm':>9} {'/bin':>7} "
      f"{'arm/control':>12}")
for tag, c in (('grid base, un-refitted control', O_C), ('grid base, PLANCK point control', N_C)):
    print(f"  {tag:>34} {O_N:>5d} {c:>9.1f} {c / O_N:>7.2f} {A_C:>9.1f} {A_C / A_N:>7.2f} "
          f"{A_C / c:>11.2f}x")

FALL = (O_C - N_C) / O_C
print(f"\n  the control's chi^2 moves {O_C:.3f} -> {N_C:.3f}, a fall of {100 * FALL:+.2f} per cent")
print(f"  the ratio moves {A_C / O_C:.4f} -> {A_C / N_C:.4f}, "
      f"rounding {A_C / O_C:.2f} -> {A_C / N_C:.2f}")
print(f"  the arm does not move: {A_C:.3f} on {A_N} bins, {A_C / A_N:.4f} per bin")

# ---------------------------------------------------------------- the predictions, read as text
print('\n' + BAR)
print('  THE FIVE REGISTERED PREDICTIONS, EACH HELD OR FALSIFIED')
print(BAR)
PRED = open(os.path.join(HERE, 'PREDICTION.md'), encoding='utf-8').read()
for need in ('The control\'s chi^2 FALLS', 'between 1 and 8 per cent',
             'MOVES AT ITS PRINTED PRECISION', 'The arm leg does not move at all',
             'between 2.36 and 2.50'):
    assert need in PRED, need
print('  (all five read out of PREDICTION.md\'s own text, not restated here)')

V = [('① the control\'s chi^2 FALLS below 212.9', N_C < O_C),
     ('② it falls by between 1 and 8 per cent (195.9 <= chi2 <= 210.8)', 195.9 <= N_C <= 210.8),
     ('③ the ratio rises past 2.33 at its printed precision', round(A_C / N_C, 2) != 2.33
      and A_C / N_C > A_C / O_C),
     ('④ the arm leg does not move (|chi2 - 496.5| <= 0.05)', abs(A_C - 496.5) <= 0.05),
     ('⑤ the ratio lands in [2.36, 2.50]', 2.36 <= A_C / N_C <= 2.50)]
for lab, ok in V:
    print(f"    {'HELD     ' if ok else 'FALSIFIED'}  {lab}")

OUT = dict(arm_chi2=A_C, arm_per_bin=A_C / A_N, nbins=A_N,
           ctl_unrefitted=O_C, ctl_unrefitted_per_bin=O_C / O_N, ratio_unrefitted=A_C / O_C,
           ctl_planck=N_C, ctl_planck_per_bin=N_C / N_N, ratio_planck=A_C / N_C,
           sampling_matched=MATCHED,
           predictions_held=[lab for lab, ok in V if ok],
           predictions_falsified=[lab for lab, ok in V if not ok])
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r7821_grid_base_at_plancks_point.json'), 'w',
          encoding='utf-8') as f:
    json.dump(OUT, f, indent=2, sort_keys=True)
print(f"\n  wrote out/r7821_grid_base_at_plancks_point.json")
print(BAR)

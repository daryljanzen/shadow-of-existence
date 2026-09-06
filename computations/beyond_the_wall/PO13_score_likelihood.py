#!/usr/bin/env python3
"""RUN 3 -- the likelihood, both arms, identical settings, with the floor as a MODEL-TO-MODEL
distance rather than a difference of two numbers each taken against the sky.

The spec's instruction, and `P15_the_floor_is_a_distance_between_models_not_a_number_from_the_data`
established why: F2 = chi2(arm) - chi2(CAMB) mixes how far the two models are apart with where each
sits relative to ONE noise realisation, and it moved across three defensible reference LambdaCDMs by
an amount comparable to the quantity being reported.

  chi2_sep = (A_a m_a - A_c m_c)^T F (A_a m_a - A_c m_c)   over the bins BOTH arms cover.
"""
import os
import sys

import numpy as np
import scipy.linalg

ROOT = '/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

S = sys.argv[1] if len(sys.argv) > 1 else '.'
BAR = '=' * 78


def load(p):
    d = np.load(p)
    return np.asarray(d['ls'], float), np.asarray(d['Dl'], float)


arms = {}
for tag, f in (('control', 'lcdm.npz'), ('CR', 'cr.npz')):
    arms[tag] = load(os.path.join(S, f))

print(BAR)
print('  RUN 3 -- the likelihood on plik_lite TT, both arms, identical settings')
print(BAR)
LMAXL = 1300.0
for cut, label in ((None, 'every bin both arms cover'),
                   (0.8 * LMAXL, f'cut at 0.8*LMAXL = {0.8*LMAXL:.0f}')):
    print(f'\n  --- {label} ---')
    print(f"    {'arm':>8} {'chi2':>10} {'bins':>6} {'chi2/bin':>9} {'amplitude':>10} {'range':>14}")
    res = {}
    for tag, (ls, Dl) in arms.items():
        c, n, A, lo, hi = CS.chi2_of(ls, Dl, lmax=cut)
        res[tag] = (c, n, A)
        print(f'    {tag:>8} {c:>10.1f} {n:>6d} {c/n:>9.3f} {A:>10.4f} {lo:>6d}-{hi:<7d}')
    d = res['CR'][0] - res['control'][0]
    print(f"    {'F2':>8} {d:>10.1f}   ** CR minus control, the measure the floor receipt warns "
          f"about **")

# ── the floor, as a distance between the two models
mb, keep = {}, None
for tag, (ls, Dl) in arms.items():
    b = CS.bin_spectrum(ls, Dl)
    mb[tag] = b
    k = np.isfinite(b)
    keep = k if keep is None else (keep & k)
cov = CS.COV_TT[np.ix_(keep, keep)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(keep.sum())))
F = 0.5 * (F + F.T)
A = {t: CS.chi2_of(*arms[t])[2] for t in arms}
dv = A['CR'] * mb['CR'][keep] - A['control'] * mb['control'][keep]
sep = float(dv @ F @ dv)
n = int(keep.sum())
print(f'\n  --- the floor, measured WITHOUT the data ---')
print(f'    chi2_sep between the two models over the {n} shared bins: {sep:.1f}')
print(f'    per bin: {sep/n:.3f}   ({np.sqrt(sep/n):.2f} sigma per bin)')
print(BAR)

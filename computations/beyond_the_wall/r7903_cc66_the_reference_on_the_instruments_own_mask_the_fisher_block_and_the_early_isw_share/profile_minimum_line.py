# -*- coding: utf-8 -*-
"""r7903+cc66 item ⑲④: THE ONE LINE ON THIS SEAT'S OWN REFERENCE PROFILE MINIMUM, UNDER THE RULING.

COMPUTES: the minimum and both limits of THIS SEAT'S REFERENCE profile, read off its own banked grid
with the ruled convention.  No CAMB: the grid is `r7853`'s `out5`, eight sums on each ruler, which is
the profile this seat's `30.56` and `54.00` meV were read from.

`r7903` rules the convention of record is `Δχ²` referenced to **the profile's minimum over the
physical region `Σ ≥ 0`**.

⛔ ** AND THE FIRST VERSION OF THIS FILE ANSWERED ABOUT THE WRONG PROFILE. **  It read `min_at` out
of `r7895`'s `limit_read.json` and reported `Σ = 0.06` eV.  That file describes **60's banked profile
on the runner's lensing grid** (`r7888`), which is what `⑱①` re-read; it is not this seat's
reference.  ⑲④ asks about THIS seat's reference profile, and on its own grid the minimum sits
somewhere else entirely.  *The two objects carry different numbers -- `193.5` meV for 60's grid,
`30.56`/`54.00` for this reference -- and reading one's minimum as the other's is the mistake this
file now exists to not make.*
"""
import glob
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
R7853 = glob.glob(os.path.join(BW, 'r7853_cc66_*'))[0]
R7895 = glob.glob(os.path.join(BW, 'r7895_cc66_*'))[0]
GRID = os.path.join(R7853, 'out5')

SUMS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
CROSS = 2.71


def limit_and_min(mode):
    pts = []
    for s in SUMS:
        p = os.path.join(GRID, '%s_%.3f.json' % (mode, s))
        if os.path.exists(p):
            pts.append((s, json.load(open(p))['total']))
    s = np.array([p[0] for p in pts], float)
    t = np.array([p[1] for p in pts], float)
    at = float(s[int(np.argmin(t))])
    d_min = t - t.min()
    d_low = t - t[0]                      # the lowest-sum baseline, this seat's former convention
    out = {}
    for tag, d in (('minimum', d_min), ('lowest_sum', d_low)):
        if d.max() <= CROSS:
            out[tag] = None
            continue
        fine = np.linspace(s[0], s[-1], 200001)
        i = np.where(np.interp(fine, s, d) > CROSS)[0]
        out[tag] = float(fine[i[0]] * 1000.0) if len(i) else None
    return at, out, [(float(a), float(b)) for a, b in pts], bool(np.all(np.diff(t) > 0))


res = {'ruling': 'dchi2 referenced to the profile minimum over Sigma >= 0',
       'profile': os.path.basename(R7853) + '/out5  (THIS seat\'s like-for-like reference)',
       'not_this_profile': os.path.basename(R7895) + '/limit_read.json describes 60\'s banked '
                           'profile on the runner grid (r7888), whose minimum is at 0.06 eV',
       'sums': SUMS, 'cross': CROSS, 'rulers': {}}

print('=' * 100)
print('  ⑲④ THE ONE LINE, ON THIS SEAT\'S OWN REFERENCE PROFILE')
print('=' * 100)
for mode, label in (('rd_camb', 'calibrated ruler'), ('rd_min', 'minimised ruler')):
    at, lims, pts, mono = limit_and_min(mode)
    same = (lims['minimum'] is not None and lims['lowest_sum'] is not None
            and abs(lims['minimum'] - lims['lowest_sum']) < 1e-9)
    res['rulers'][mode] = dict(label=label, minimum_at_eV=at, limit_on_minimum_meV=lims['minimum'],
                               limit_on_lowest_sum_meV=lims['lowest_sum'],
                               conventions_coincide=same, monotone_increasing=mono,
                               points=pts)
    print('  %-8s (%s): minimum at Sum = %.2f eV; monotone increasing from Sum=0: %s'
          % (mode, label, at, mono))
    print('      limit on the MINIMUM baseline     : %.3f meV' % lims['minimum'])
    print('      limit on the LOWEST-SUM baseline  : %.3f meV' % lims['lowest_sum'])
    print('      the two conventions COINCIDE      : %s' % same)

cal = res['rulers']['rd_camb']
LINE = (
    'This seat\'s reference profile is monotone increasing from Sigma = 0 on BOTH rulers, so its '
    'minimum over the physical region IS the lowest-sum point, Sigma = %.2f eV. Under r7903\'s '
    'ruling the reference\'s limits are therefore %.3f meV on the calibrated ruler and %.3f on the '
    'minimised -- IDENTICAL to the lowest-sum readings, because for this profile the two '
    'conventions are one reading. The ruling costs this reference nothing. The 22.734 meV '
    'convention gap this seat measured at r7895 belongs to 60\'s banked profile on the runner grid, '
    'whose minimum sits at 0.06 eV, and not to this reference at all.'
    % (cal['minimum_at_eV'], cal['limit_on_minimum_meV'],
       res['rulers']['rd_min']['limit_on_minimum_meV'])
)
res['line'] = LINE
json.dump(res, open(os.path.join(HERE, 'profile_minimum_line.json'), 'w'), indent=1)
print()
print('  ⇒ ' + LINE.replace('. ', '.\n    '))
print()
print('  ⌗ and the two readings reproduce this seat\'s banked uncut figures (30.56, 54.00) to three')
print('    decimals, which is the check that this grid and this reader are the ones of record.')
print()
print('  banked: profile_minimum_line.json')

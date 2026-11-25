# -*- coding: utf-8 -*-
"""Ⓑ②+ THE SAME BARRIER, LOOKED FOR ON EACH RUNG -- AN ADDITIONAL READING, NOT A REGISTERED ARM.

⚠ ** THIS FILE IS NOT IN `PREDICTION.md` AND IS LABELLED SO. **  It was written after `Ⓑ②ᵃ` named
the direction, because the order's own sentence -- *"a second basin in the instrument alone is an
instrument property"* -- turns on whether the barrier is a property of the instrument or of the
background setting the basins were found on.  It is reported as a reading, with no criterion
registered in advance, and nothing in this revision's registered verdicts rests on it.

** WHAT IT DOES. **  `r7870` found the two vectors on the `+0.044` rung.  This file asks the SAME
question of the SAME two vectors on whichever rung it is pointed at: is the straight segment
between them still barriered when the chi^2 is built on a different background?

  RUNG=nufd_dneff044 | nufd_only       NODE=60 python3 basin_across_rungs.py
"""
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
R7864 = os.path.join(_BTW, 'r7864_60_the_massive_neutrino_background_given_its_fermi_dirac_'
                           'density_and_both_limits_re_read')
R7870 = os.path.join(_BTW, 'r7870_60_the_separating_grid_the_corrected_control_and_the_cache_'
                           'that_relabelled_a_column')
RUNG = os.environ.get('RUNG', 'nufd_dneff044')
POL = {'nufd_dneff044': ('pol_grid_bvel1_nufd_dneff044',
                         'phiphi_grid_eta4000_bvel1_primnorm1_nufd_dneff044'),
       'nufd_only': ('pol_grid_bvel1_nufd_only',
                     'phiphi_grid_eta4000_bvel1_primnorm1_nufd_only')}
if RUNG not in POL:
    raise SystemExit('RUNG must be one of: %s' % ', '.join(sorted(POL)))

sys.path.insert(0, R7864)
import limits as _L7864                                                    # noqa: E402,F401

os.environ['POL_DIR'] = os.path.join(BANK, POL[RUNG][0])
os.environ['PPGRID'] = os.path.join(BANK, POL[RUNG][1])
for k, v in (('POL_DIR', POL[RUNG][0]), ('PPGRID', POL[RUNG][1])):
    if not os.path.isdir(os.environ[k]):
        raise SystemExit('%s is not on disk: %s' % (k, v))

import model6 as M6                                                        # noqa: E402

NODE = 0.400
_at = json.load(open(os.path.join(R7870, 'second_basin.json')))['at_0400']
X_LO = [float(v) for v in _at['x_lower']]
X_HI = [float(v) for v in _at['x_higher']]

mod = M6.Model6('lcdm')
raw = mod.amp_cmb
mod.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0


def chi2_at(v5):
    return float(mod.chi2(list(v5[:4]) + [NODE, float(v5[4])]))


ts = np.linspace(0.0, 1.0, 81)
seg = [chi2_at([X_LO[i] + t * (X_HI[i] - X_LO[i]) for i in range(5)]) for t in ts]
c_lo, c_hi = seg[0], seg[-1]
interior = seg[1:-1]
top = float(max(interior))
t_top = float(ts[1 + int(np.argmax(interior))])
barrier = bool(top > max(c_lo, c_hi) + 1e-6)

out = dict(rung=RUNG, pol_dir=POL[RUNG][0], node=NODE,
           chi2_at_lower_vector=c_lo, chi2_at_higher_vector=c_hi,
           interior_max=top, interior_max_at_t=t_top,
           height_over_higher_end=float(top - max(c_lo, c_hi)),
           barrier=barrier, segment_chi2=[float(c) for c in seg],
           registered=False,
           note='an additional reading, written after Ⓑ②ᵃ named the direction; no criterion was '
                'registered for it in advance and no registered verdict rests on it')
p = os.path.join(_HERE, 'basin_across_rungs_%s.json' % RUNG)
json.dump(out, open(p, 'w'), indent=1, sort_keys=True)
print('  rung %-14s ends %.4f and %.4f; interior max %.4f at t=%.4f, %.4f over the higher end'
      % (RUNG, c_lo, c_hi, top, t_top, top - max(c_lo, c_hi)))
print('  ⇒ %s' % ('A BARRIER on this rung too' if barrier else 'NO BARRIER on this rung'))
print('  wrote %s' % p)

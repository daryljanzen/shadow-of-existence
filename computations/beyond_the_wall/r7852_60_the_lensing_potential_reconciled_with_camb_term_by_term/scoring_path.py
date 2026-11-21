#!/usr/bin/env python3
"""** THE NINE BANDPOWERS ON THE LANDED SCORING PATH, at both handovers, banked as a record. **

`handover_optimum.py` scores thirteen handovers through the growth this line used BEFORE the
predecessor's initial-condition repair, because that is the growth whose surface can be rebuilt from
a banked solve in a second.  ** The limit is read through the other one. **  `phiphi_point_ics.py` is
the worker the control's grid is actually built with, and its growth takes its initial conditions
from the instrument's own solve, so the figure that belongs beside a limit is the one from THAT path.

This file scores the control point of each banked grid and writes both, so the receipt pins a record
rather than recomputing a number inside its own assertion.

⌗ The two paths disagree by `0.31` per dof at the repaired handover, which is the predecessor's
initial-condition repair costing something where the source split had already measured the growth to
be right to two per cent before it was touched.

Run: python3 scoring_path.py            (writes scoring_path.json)
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
R7850 = os.path.join(_BTW, 'r7850_60_phi_carried_through_the_radiation_era')
sys.path.insert(0, R7846)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

import lensing_like as LL                                                    # noqa: E402

GRIDS = (
    ('eta400_instrument_ics', os.path.join(_HERE, 'grid_ics_eta400', 'lcdm_S000.json')),
    ('eta400_kdep', os.path.join(_HERE, 'grid_kdep_eta400', 'lcdm_S000.json')),
    ('eta4000_instrument_ics', os.path.join(R7850, 'grid_ics_eta4000', 'lcdm_S000.json')),
)


def main():
    out = {}
    print('\n  the control point of each banked grid, one amplitude fitted\n')
    print('    which                      etaref     chi^2      per dof    amplitude')
    for tag, path in GRIDS:
        if not os.path.exists(path):
            out[tag] = None
            print('    %-26s  (not present)' % tag)
            continue
        d = json.load(io.open(path, encoding='utf-8'))
        b = np.array(d['bandpowers'], float)
        a = float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b))
        r = LL.DATA - a * b
        c2 = float(r @ LL.FISHER @ r)
        out[tag] = dict(etaref=d['etaref'], chi2=c2, per_dof=c2 / 8.0, amplitude=a,
                        growth=d.get('growth', ''), n_modes=d.get('n_modes'),
                        bandpowers=[float(v) for v in b])
        print('    %-26s %7.0f  %9.4f  %9.6f  %.6e' % (tag, d['etaref'], c2, c2 / 8.0, a))
    a4, a0 = out.get('eta400_instrument_ics'), out.get('eta4000_instrument_ics')
    if a4 and a0:
        out['ics_improvement_factor'] = a0['chi2'] / a4['chi2']
        print('\n    ⇒ on the landed scoring path the repaired handover improves the nine '
              'bandpowers by a factor %.4f' % out['ics_improvement_factor'])
    k4 = out.get('eta400_kdep')
    if a4 and k4:
        out['ics_costs_per_dof_at_eta400'] = a4['per_dof'] - k4['per_dof']
        print('    ⇒ and the initial-condition growth costs %.6f per dof against the growth '
              'before it, at the same handover' % out['ics_costs_per_dof_at_eta400'])
    out['camb_per_dof_exactly_binned'] = 1.0668
    with io.open(os.path.join(_HERE, 'scoring_path.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote scoring_path.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

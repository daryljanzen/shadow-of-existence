"""Ⓙ⑩: what the instrument's own solve COSTS, recorded with the configuration it was measured under.

`r7848` left a cost record -- `r7846_60_.../phiphi_cost.json` -- whose `phi` entry says `40.38` s for
`phi_shape`.  ** That file does not record which `ETAREF` it was measured at, and `phiphi_cost.py`
takes `ETAREF` from the environment with no default. **  This seat's own five-wavenumber timing at
`e_end = 1000` came out at `40.4` s and at `e_end = 4000` at `493.3` s, so a `40` s figure cannot
describe the `eta_ref = 4000` carry the revision actually landed on.

⌗ **This is the same defect as the two figures `r7848` had to correct, in a third place: a number
recorded under one configuration and later read as if it applied to another.**  The normalisation
read `1.3` per cent instead of `9.0` for want of a factor; the two Fisher matrices read `1.000e+00`
instead of `1.9e-17` for want of a denominator; this reads `40` s instead of whatever it is for want
of the `ETAREF` it was taken at.

So this file measures the production call -- `phi_shape(etaref)` at the production `NKP` -- at both
candidate carries, prints the configuration beside every number, and writes a record that carries
its own switches.  Nothing here is inferred from the earlier file; it is re-measured.

Run: NKP=220 python3 cost_table.py          (writes cost_table.json)
"""
import io
import json
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)
sys.path.insert(0, _BTW)
import phiphi as PP                                                        # noqa: E402
A = PP.A

CARRIES = [float(v) for v in os.environ.get('CARRIES', '914,4000').split(',')]


def main():
    out = dict(switches=dict(NKP=PP.NKP, KMIN=PP.KMIN, KMAX=PP.KMAX, NK=os.environ.get('NK'),
                             NOPROJ=os.environ.get('NOPROJ'), RTOL=A.RTOL,
                             ETA_ON=float(A.ETA_ON), ETA_END=float(A.ETA_END),
                             eta_0=float(A.eta_0)),
               five_mode_probe=dict(
                   note='five wavenumbers 2e-4..1.0, measured before this revision registered',
                   seconds={'500': 12.2, '1000': 40.4, '1893': 123.4, '4000': 493.3,
                            '6000': 1095.7},
                   killed_at='eta = 9000, at the 30-minute limit, so eta_0 = 14145 is unmeasured '
                             'and is NOT extrapolated into a claim'),
               carries={})
    print('\n  the instrument\'s own solve, with the configuration beside every number\n')
    print('  NKP = %d over k = %.1e..%.1e; NK = %s; NOPROJ = %s; RTOL = %.1e'
          % (PP.NKP, PP.KMIN, PP.KMAX, os.environ.get('NK'), os.environ.get('NOPROJ'), A.RTOL))
    print('  ETA_ON = %.4f, ETA_END = %.1f, eta_0 = %.1f\n'
          % (A.ETA_ON, A.ETA_END, A.eta_0))
    for etaref in CARRIES:
        a_ref = float(A.a_of_eta(min(etaref, A.eta_0)))
        z = 1.0 / a_ref - 1.0
        t0 = time.time()
        kkp, Phi = PP.phi_shape(etaref)
        dt = time.time() - t0
        out['carries'][('%g' % etaref)] = dict(
            etaref=etaref, a_ref=a_ref, z_ref=z, seconds=dt, n_modes=int(len(kkp)),
            phi_at_k_min=float(Phi[0]), phi_at_k_max=float(Phi[-1]))
        print('  ETAREF = %-6g (a = %.6e, z = %8.2f): phi_shape over %d modes took %8.1f s'
              % (etaref, a_ref, z, len(kkp), dt), flush=True)
        print('     Phi at k = %.1e is %+.6e; at k = %.1e is %+.6e'
              % (kkp[0], Phi[0], kkp[-1], Phi[-1]), flush=True)

    rec = os.path.join(R7846, 'phiphi_cost.json')
    if os.path.exists(rec):
        old = json.load(io.open(rec, encoding='utf-8'))
        out['r7848_record'] = dict(phi_seconds=old['seconds']['phi'],
                                   records_its_etaref=('etaref' in json.dumps(old)))
        near = min(out['carries'].values(), key=lambda v: abs(v['seconds']
                                                              - old['seconds']['phi']))
        out['r7848_record']['nearest_measured_carry'] = near['etaref']
        out['r7848_record']['nearest_ratio'] = near['seconds'] / old['seconds']['phi']
        print('\n  r7848 recorded phi = %.2f s and did NOT record its ETAREF (%s).'
              % (old['seconds']['phi'], 'confirmed' if not
                 out['r7848_record']['records_its_etaref'] else 'it did'))
        print('     Of the carries measured here the closest is ETAREF = %g, a factor %.3f away.'
              % (near['etaref'], out['r7848_record']['nearest_ratio']))
    with io.open(os.path.join(_HERE, 'cost_table.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote cost_table.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

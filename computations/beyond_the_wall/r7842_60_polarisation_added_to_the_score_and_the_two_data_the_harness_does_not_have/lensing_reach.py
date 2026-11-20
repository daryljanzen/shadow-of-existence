#!/usr/bin/env python3
"""** THE LENSING DATA IS HERE; THE INSTRUMENT CANNOT WEIGH NEUTRINOS WITH IT, AND THE REASON IS
EXACT RATHER THAN APPROXIMATE. **

Order `r7841` ② asked for the lensing-reconstruction spectrum with its covariance.  `r7842`
registered it as data the harness does not have -- and the Planck 2018 conservative bandpowers,
their covariance and their nine windows have been in
`computations/beyond_the_wall/r7471_70_PO24_tilt_off_the_tail/lensing/` since node `70` banked them,
scored there as `613 bins + 9 lensing`.  ** SO THE REGISTERED ARM IS FALSIFIED AND THE ORDER IS NOT
BLOCKED ON DATA. **  What it is blocked on is measured here.

`L171x_lensing_potential.py` builds `C_L^phiphi` as `Phi(k, a) = Phi(k, a_ref) * g(a)/g(a_ref)` with
`g = D/a` a BACKGROUND quadrature over `A.Hphys`, the `k`-dependence frozen at `eta_ref = 4000`
(`z = 12.8`).  The two things that decides are measured, not argued:

  ① ** AT FIXED TOTAL `Omega_m` THIS INSTRUMENT'S BACKGROUND RATE IS EXACTLY INDEPENDENT OF THE
    SUM. **  Not nearly: `0` to every bit, across four decades of scale factor, with the comoving
    distance to last scattering identical to all printed digits.  `ACOUSTIC_two_arm` holds `OM` as
    the TOTAL by design -- that is what "the dust term's total carries their late mass" means -- so
    `_rt` never moves and neither does `Hphys`.  ⇒ *A growth factor built from `Hphys` carries
    exactly ZERO neutrino effect.*  The lensing kernel peaks at `chi_*/2`, around `z ~ 3.3`, and
    every bit of that range is downstream of `eta_ref`.

  ② ** THE ONE CHANNEL THAT DOES RESPOND IS SCALE-INDEPENDENT AND FROZEN AT `z = 12.8`. **  The sum
    enters `OCDM` and the Poisson source, lowering the clustering fraction by exactly `f_nu` --
    flat in `k`, identical at every late time.  The physical suppression is neither: it is
    scale-dependent, switching on above the free-streaming scale, and it ACCUMULATES to `z = 0`.

So the gap is not a missing measurement, it is a missing scale-dependent growth: an instrument
extension, not a data request.  ** THIS SCRIPT DOES NOT ESTIMATE HOW BIG THE MISSING PART IS. **
Writing `-8 f_nu` here would be quoting a textbook asymptote as though this harness had produced it,
and it has not; what is pinned is the structure and the two exact numbers.  Writes
`lensing_reach.json`.
"""
import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
LENS = os.path.join(BTW, 'r7471_70_PO24_tilt_off_the_tail', 'lensing')

PROBE = r'''
import os, sys, json
import numpy as np
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '1')
os.environ['MNU'] = sys.argv[1]
os.environ['LH0'] = '67.40'; os.environ['LOM'] = '0.3150'
os.environ['WBH2'] = '0.02237'; os.environ['NS'] = '0.965'
sys.path.insert(0, sys.argv[2])
import ACOUSTIC_two_arm as A
ag = np.logspace(-4, 0, 41)
et = np.linspace(A.eta_0 * 0.2, A.eta_0, 9)
print('@@' + json.dumps(dict(
    mnu=float(sys.argv[1]), ONU=float(A.ONU), OCDM=float(A.OCDM), OM=float(A.OM),
    D_M=float(A.D_M), eta_0=float(A.eta_0),
    H=[float(A.Hphys(float(a))) for a in ag],
    Om_of=[float(A.Om_of(float(e))) for e in et])))
'''


def probe(mnu):
    """the instrument's background and clustering matter at this sum, in a fresh process

    A fresh process per sum because the switches are read at IMPORT: setting `MNU` and re-importing
    in one process would measure the first value twice.
    """
    p = os.path.join(HERE, '_reach_probe.py')
    with open(p, 'w') as fh:
        fh.write(PROBE)
    try:
        r = subprocess.run([sys.executable, p, str(mnu), BTW], capture_output=True, text=True,
                           timeout=1800)
        for line in r.stdout.splitlines():
            if line.startswith('@@'):
                return json.loads(line[2:])
        raise RuntimeError(f'the probe printed no result at MNU={mnu}:\n{r.stdout[-2000:]}'
                           f'\n{r.stderr[-2000:]}')
    finally:
        if os.path.exists(p):
            os.remove(p)


def main():
    # ③ the data itself, read rather than described
    lb = np.loadtxt(os.path.join(LENS, 'x_bandpowers.dat'))
    cov = np.loadtxt(os.path.join(LENS, 'x_cov.dat'))
    wins = [np.loadtxt(os.path.join(LENS, 'win', f'window{i}.dat')) for i in range(1, 10)]
    err = np.sqrt(np.diag(cov))
    data = dict(bandpowers=int(lb.shape[0]), L_min=float(lb[0, 1]), L_max=float(lb[-1, 2]),
                L_av=[float(v) for v in lb[:, 3]], PP=[float(v) for v in lb[:, 4]],
                cov_shape=list(cov.shape),
                cov_symmetric_to=float(np.max(np.abs(cov - cov.T))),
                cov_min_eigenvalue=float(np.min(np.linalg.eigvalsh(cov))),
                fractional_error=[float(e / p) for e, p in zip(err, lb[:, 4])],
                windows=len(wins), window_rows=[int(w.shape[0]) for w in wins],
                window_weight_sums=[float(np.sum(w[:, 1])) for w in wins],
                path=os.path.relpath(LENS, os.path.dirname(BTW)))
    print('  ③ the banked data: %d bandpowers, L = %g to %g, %dx%d covariance'
          % (data['bandpowers'], data['L_min'], data['L_max'], *data['cov_shape']), flush=True)
    print('     fractional errors run %.1f to %.1f per cent; smallest eigenvalue %.3e'
          % (100 * min(data['fractional_error']), 100 * max(data['fractional_error']),
             data['cov_min_eigenvalue']), flush=True)

    a, b = probe(0.0), probe(0.30)
    H1, H2 = np.asarray(a['H'], float), np.asarray(b['H'], float)
    m1, m2 = np.asarray(a['Om_of'], float), np.asarray(b['Om_of'], float)
    dH = float(np.max(np.abs(H2 / H1 - 1.0)))
    dDM = float(abs(b['D_M'] / a['D_M'] - 1.0))
    ratio = m2 / m1
    f_nu = float(b['ONU'] / b['OM'])
    out = dict(
        data=data,
        background=dict(sum_ev=0.30, max_rel_dH=dH, rel_dDM=dDM,
                        D_M=[a['D_M'], b['D_M']], eta_0=[a['eta_0'], b['eta_0']],
                        exactly_independent=bool(dH == 0.0 and dDM == 0.0)),
        clustering=dict(ONU=b['ONU'], OCDM=[a['OCDM'], b['OCDM']], OM=b['OM'], f_nu=f_nu,
                        source_ratio=[float(v) for v in ratio],
                        source_drop=float(1.0 - np.mean(ratio)),
                        scale_independent_to=float(np.max(ratio) - np.min(ratio)),
                        matches_f_nu_to=float(abs((1.0 - np.mean(ratio)) - f_nu))),
        verdict=dict(
            background_carries_nothing=bool(dH == 0.0 and dDM == 0.0),
            only_channel_is_frozen_at_z=12.8,
            missing_piece='a scale-dependent growth below the free-streaming scale, accumulated '
                          'from z = 12.8 to z = 0, where the lensing kernel does its work',
            blocked_on='an instrument extension, not a measurement'))
    print('  ① the background rate across Sum = 0 -> 0.30 eV: max |dH/H| = %.3e, '
          'comoving distance rel %.3e' % (dH, dDM), flush=True)
    print('     exactly independent of the sum: %s' % out['background']['exactly_independent'],
          flush=True)
    print('  ② the clustering source drops %.6f per cent, flat in k to %.3e, '
          'against f_nu = %.6f per cent'
          % (100 * out['clustering']['source_drop'],
             out['clustering']['scale_independent_to'], 100 * f_nu), flush=True)
    with open(os.path.join(HERE, 'lensing_reach.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote lensing_reach.json', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())

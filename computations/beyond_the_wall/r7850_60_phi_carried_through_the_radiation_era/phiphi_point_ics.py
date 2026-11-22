#!/usr/bin/env python3
"""one grid point of the lensing bandpowers, with the growth's ICs read off the instrument

`r7846`'s `phiphi_point.py` with ONE line changed in substance: the growth is
`GrowthFromInstrument` rather than `GrowthKDep`, so its initial conditions at `eta_ref` come from
the instrument's own perturbation solve instead of from the matter + Λ closed form.

** AND ONE SOLVE SERVES BOTH, WHICH IS WHAT MAKES THE GRID AFFORDABLE. **  The Limber integral needs
`Phi(k)` at `eta_ref` and the growth needs `delta_cb` and its `N`-derivative there; those are three
output times of the SAME solve.  This revision measured that the solve's cost is set by its end
time and not by its mode count, so one `220`-mode solve with three output times costs what one
needed anyway -- about `667` s -- instead of twice that.

Writes `$PPOUT/<arm>_<tag>.json`, in the same shape `phiphi_point.py` writes, plus the keys that
say which growth produced it.  ⌗ *A record that does not carry the configuration it was measured
under cannot be read later, which this revision learned from `r7848`'s cost table the hard way.*

Environment: PPARM, PPTAG, PPOUT, MNU, ETAREF, and the instrument's own switches.
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
os.environ.setdefault('ETAREF', '4000')
sys.path.insert(0, R7846)
sys.path.insert(0, _HERE)
sys.path.insert(0, _BTW)
import phiphi as PP                                                        # noqa: E402
from growth_from_instrument import GrowthFromInstrument                     # noqa: E402

A = PP.A
DELTA = float(os.environ.get('DELTA', '8.0'))


def main():
    arm, tag = os.environ['PPARM'], os.environ['PPTAG']
    out_dir = os.environ.get('PPOUT', '/tmp/claude-0/phiphi_grid_ics')
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, f'{arm}_{tag}.json')
    if os.path.exists(dest):
        print('  [have] %s %s' % (arm, tag), flush=True)
        return 0
    mnu = float(os.environ.get('MNU', '0.0'))
    etaref = float(os.environ['ETAREF'])
    a_ref = float(A.a_of_eta(etaref))

    lb, cov, wins = PP.bandpowers()
    Lg = np.unique(np.concatenate([L for L, _ in wins]))
    ls = np.unique(np.round(np.logspace(np.log10(max(2, Lg.min())),
                                        np.log10(Lg.max()), 36)).astype(int))

    # ** ONE solve, three output times, on the shape's own mode grid. **
    kk = np.logspace(np.log10(PP.KMIN), np.log10(PP.KMAX), PP.NKP)
    te = np.array([etaref - DELTA, etaref, etaref + DELTA], float)
    sol, nk, NV = A.evolve(kk, t_eval=te, e_end=float(te[-1]))
    assert sol.status == 0, f'the instrument solve did not finish: {sol.message}'
    Y = sol.y.T.reshape(len(te), nk, NV)
    wc = float(A.OCDM) / (float(A.OCDM) + float(A.OB))
    wb = 1.0 - wc
    # ⚠ asked for, not derived: under `BVEL=1` (r7854) `NV - 1` is the baryon VELOCITY.
    d = wc * Y[:, :, 0] + wb * Y[:, :, A.I_DB_F]
    N = np.log(np.array([float(A.a_of_eta(t)) for t in te]))
    phi_at_ref = Y[1, :, 6]

    # the shape the Limber integral needs, served from that same solve
    PP.phi_shape = lambda _e, _kk=kk, _p=phi_at_ref: (_kk, _p)

    g = GrowthFromInstrument(mnu, kk=kk, etaref=etaref,
                             ic_from=(d[1], (d[2] - d[0]) / (N[2] - N[0]),
                                      dict(weights=dict(cdm=wc, baryon=wb),
                                           eta_outputs=[float(t) for t in te])))
    cl = PP.clpp(ls, mnu, etaref=etaref, growth=g)
    b = PP.bin_through(ls, cl, wins)
    rec = dict(arm=arm, tag=tag, mnu=mnu, etaref=etaref, a_ref=a_ref,
               z_start=1.0 / a_ref - 1.0, f_nu=g.f_nu,
               ls=[int(v) for v in ls], cl=[float(v) for v in cl],
               bandpowers=[float(v) for v in b],
               growth='GrowthFromInstrument: initial conditions read off the instrument at eta_ref',
               n_modes=int(len(kk)), delta_eta=DELTA,
               switches={k: os.environ[k] for k in
                         ('ARM', 'CRH0', 'CROM', 'HIER', 'LEAFGEOM', 'LEAFSCALES', 'LMAXL',
                          'LSTEP', 'MNU', 'ETAREF', 'NK', 'NOPROJ')
                         if k in os.environ})
    with io.open(dest, 'w', encoding='utf-8') as fh:
        json.dump(rec, fh, indent=1, sort_keys=True)
    print('  [done] %s %s  bandpowers %.4e .. %.4e' % (arm, tag, b[0], b[-1]), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())

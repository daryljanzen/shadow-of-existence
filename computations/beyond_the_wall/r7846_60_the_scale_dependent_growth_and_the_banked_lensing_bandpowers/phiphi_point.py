#!/usr/bin/env python3
"""one grid point of the lensing bandpowers: C_L^phiphi binned through the nine windows

Reads the instrument's switches from the environment, exactly as `gen_pol.sh` sets them for the CMB
spectra, so the two datasets refer to ONE cosmology per point and not to two.  Writes
`$PPOUT/<arm>_<tag>.json`.

** THE CARRY STARTS AT `ETAREF`, AND `r7846` SETTLED THAT AT `z = 188` RATHER THAN THE ORDERED
`z = 12.8`, FOR TWO MEASURED REASONS: **  the ordered interval carries only `44.4` per cent of the
post-non-relativistic neutrino suppression, and it leaves the shape at `chi^2/dof = 2.05` against
these nine bandpowers where the earlier carry gives `1.07`.
"""
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
os.environ.setdefault('ETAREF', '914')

import phiphi as PP                                                      # noqa: E402
import growth_kdep as GK                                                 # noqa: E402
A = GK.A


def main():
    arm, tag = os.environ['PPARM'], os.environ['PPTAG']
    out_dir = os.environ.get('PPOUT', '/tmp/claude-0/phiphi_grid')
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f'{arm}_{tag}.json')
    if os.path.exists(path) and os.path.getsize(path) > 0:
        print(f'  [have] {arm} {tag}')
        return 0

    mnu = float(os.environ.get('MNU', '0.0'))
    etaref = float(os.environ['ETAREF'])
    a_ref = float(A.a_of_eta(etaref))

    lb, cov, wins = PP.bandpowers()
    Lg = np.unique(np.concatenate([L for L, _ in wins]))
    ls = np.unique(np.round(np.logspace(np.log10(max(2, Lg.min())),
                                        np.log10(Lg.max()), 36)).astype(int))
    kk = np.logspace(np.log10(PP.KMIN), np.log10(PP.KMAX), 48)
    g = GK.GrowthKDep(mnu, kk=kk, a_start=a_ref)
    cl = PP.clpp(ls, mnu, etaref=etaref, growth=g)
    bp = PP.bin_through(ls, cl, wins)

    rec = dict(arm=arm, tag=tag, mnu=mnu, etaref=etaref, z_start=float(1.0 / a_ref - 1.0),
               ls=[int(v) for v in ls], cl=[float(v) for v in cl],
               bandpowers=[float(v) for v in bp], f_nu=float(g.f_nu),
               switches={k: os.environ[k] for k in
                         ('ARM', 'CRH0', 'CROM', 'LH0', 'LOM', 'WBH2', 'NS', 'MNU', 'HIER',
                          'LMAXL', 'LSTEP', 'LEAFGEOM', 'LEAFSCALES', 'ZSTART')
                         if k in os.environ})
    with open(path, 'w') as fh:
        json.dump(rec, fh, indent=1, sort_keys=True)
    print(f'  [done] {arm} {tag}  bandpowers {bp[0]:.4e} .. {bp[-1]:.4e}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

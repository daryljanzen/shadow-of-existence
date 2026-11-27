#!/usr/bin/env python3
"""one grid point of the lensing bandpowers: C_L^phiphi binned through the nine windows

Reads the instrument's switches from the environment, exactly as `gen_pol.sh` sets them for the CMB
spectra, so the two datasets refer to ONE cosmology per point and not to two.  Writes
`$PPOUT/<arm>_<tag>.json`.

** THE CARRY STARTS AT `ETAREF = 4000`, THE ORDERED `z = 12.8`. **  `r7846` first settled on
`z = 188` for two measured reasons -- the ordered interval carries only `44.4` per cent of the
post-non-relativistic neutrino suppression, and it leaves the shape at `chi^2/dof = 2.05` where the
earlier carry gives `1.07` -- and then `carry_validity.py` reversed that decision: at `z = 188` the
growth equation is outside its own range and the better `chi^2` was two errors cancelling.  Both of
those deficits are still real and neither is fixed by moving the start.
"""
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
# ** THE ORDERED CARRY, z = 12.8, AND THIS DEFAULT WAS 914 UNTIL carry_validity.py REVERSED IT. **
#   The earlier start looked better on the lensing shape and on how much neutrino suppression it
#   carried, and both of those readings stood until the closed test: Phi taken DIRECTLY from the
#   instrument at z = 12.8 against Phi at z = 188 carried forward by the growth.  The ratio came
#   out k-dependent, 0.96 at the largest scales and 0.74 at small ones -- sub-horizon Phi decay
#   through the residual radiation era, which a matter-only growth equation does not carry.  At
#   z = 188 radiation is still 5 per cent of matter.  ⇒ The growth was being used outside its own
#   range, so the better chi^2 was two errors cancelling and not a better model.
os.environ.setdefault('ETAREF', '4000')

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
               #: ⛭ r7884+60: the seven on the second line were NOT recorded, so a banked lensing
               #: point could not show which object it was.  The CMB side records its switches in
               #: the spectrum's own `config` and `r7884`'s gates Ⓛ⓵/Ⓛ⓶ read them there; the
               #: lensing side had no such record at all, so nothing could verify that these
               #: bandpowers are the hierarchy's at the gated grid.  ⛔ *The whole discipline is to
               #: read a leg's settings off the LEG and not off the generator that was meant to set
               #: them, and on this side that was impossible rather than merely unused.*  Additive
               #: metadata: every reader of a banked `switches` record parses it by name, so adding
               #: keys changes no number and no existing read.
               switches={k: os.environ[k] for k in
                         ('ARM', 'CRH0', 'CROM', 'LH0', 'LOM', 'WBH2', 'NS', 'MNU', 'HIER',
                          'BVEL', 'NUFD', 'PRIMNORM', 'NUHIER', 'NQ', 'LMAXNU', 'QMAXNU',
                          'LMAXL', 'LSTEP', 'LEAFGEOM', 'LEAFSCALES', 'ZSTART')
                         if k in os.environ})
    with open(path, 'w') as fh:
        json.dump(rec, fh, indent=1, sort_keys=True)
    print(f'  [done] {arm} {tag}  bandpowers {bp[0]:.4e} .. {bp[-1]:.4e}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

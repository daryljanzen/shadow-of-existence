"""fold r6959's runs into the banks the receipt reads -- r6959+cc66.47.

  * `r6959_eta_{lcdm,cr}.npz` -- ⓵ᵃ's measurement: the source's own weight across the visibility
    window, band by band in q, for the whole source, for the monopole-plus-Doppler combination and for
    each of the four terms separately, with the phase abscissa `r_s,leaf(eta)`, the visibility, e^-tau
    and `Jac`.  ** Copied unaltered from the instrument's own `SRCETA` output -- one run per arm, no
    slicing, so nothing is summed. **
  * `r6959_swap_lcdm.npz` -- ⓵ᵇ's swap: the control with the ARM's spread in r_s,leaf/r_s imposed,
    `LSTEP=1 LMAXL=2000`, the coefficient solved from the measurement above and read from
    `prediction.json` rather than chosen here.
  * `r6959_big_lcdm.npz` -- the taper that WOULD deliver the observed excess at the top band.  *It
    answers what the candidate needs rather than what it has.*
  * `r6959_{swap,big}all_lcdm.npz` -- ** the same two coefficients with the taper on the WHOLE source,
    which is what the first pair of runs did before the wiring was corrected. **  A Gaussian in
    r_s,leaf over the whole eta grid also crushes the ISW, whose support runs to eta_0: the ISW's own
    eta-integral comes back at 0.656 of itself at the small coefficient and 0.238 at the large one.
    *Kept and read, because it is how the ISW's share of the low-q contrast is measured -- and because a
    knob whose first wiring was wrong should leave the wrong version banked rather than deleted.*
"""
import json
import os
import re
import shutil

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = '/tmp/n66/r6959'
STEP = 250
NK = 2547                                    # the control's mode count at LMAXL=2000


def fold(tag, sub='swap', nk=NK):
    fs = sorted((int(re.search(r'_k(\d+)$', x[:-4]).group(1)), x)
                for x in os.listdir(f'{D}/{sub}')
                if x.startswith(f'{tag}_k') and x.endswith('.npz'))
    assert [i for i, _ in fs] == list(range(0, nk, STEP)), f'{tag}: slices {[i for i, _ in fs]}'
    ds = [np.load(os.path.join(D, sub, x)) for _, x in fs]
    ls = ds[0]['ls']
    for d in ds:
        assert np.array_equal(d['ls'], ls), f'{tag}: slices differ on the multipoles'
    return dict(ls=ls, Dl=sum(d['Dl'] for d in ds), l_A=ds[0]['l_A'], D_M=ds[0]['D_M'],
                r_s=ds[0]['r_s'], arm=ds[0]['arm'])


PR = json.load(open(os.path.join(D, 'eta', 'prediction.json')))
for arm in ('lcdm', 'cr'):
    shutil.copyfile(os.path.join(D, 'eta', f'eta_{arm}.npz'),
                    os.path.join(SP, f'r6959_eta_{arm}.npz'))
    print(f'  {arm}: the eta-profile -> spectra/r6959_eta_{arm}.npz')
for tag, al, sub, allt in (('swap_lcdm', PR['alpha'], 'swap', 0),
                           ('big_lcdm', PR['alpha_big'], 'swap', 0),
                           ('swapall_lcdm', PR['alpha'], 'swapall', 1),
                           ('bigall_lcdm', PR['alpha_big'], 'swapall', 1)):
    src = 'swap_lcdm' if tag.startswith('swap') else 'big_lcdm'
    out = fold(src, sub)
    out['taper'] = float(al)
    out['taper_s0'] = float(PR['s0'])
    out['taper_all'] = int(allt)
    np.savez(os.path.join(SP, f'r6959_{tag}.npz'), **out)
    print(f'  {tag}: {len(out["ls"])} multipoles at LSTEP=1, SRCTAPER={al:.10g}'
          f'{" SRCTAPERALL=1" if allt else ""} -> spectra/r6959_{tag}.npz')

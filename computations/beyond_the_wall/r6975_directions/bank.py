"""fold r6975's term-mix runs into the banks the receipt reads -- r6975+cc66.48.

  * `r6975_mix_lcdm.npz` -- the control with the ARM's monopole fraction imposed, `DPSRC=0.8794`.  The
    coefficient is solved from `r6959`'s `SRCETA` profiles and from nothing else: scaling the Doppler by
    c scales its power by c^2, and the c that matches the arm's fraction comes out between 0.860 and
    0.897 in all seven bands -- ** one constant to two per cent **, which is what makes the arm's
    term-mix difference a one-parameter operation rather than a reshaping.
  * `r6975_mixb_lcdm.npz` -- the same operation at `DPSRC=0.60`, the second coefficient, so the response
    can be calibrated and inverted the way `cc66.47`'s taper response was.

⌗ `DPSRC` needed no wiring: it scales (1/k^2) d/deta [g theta_b] and nothing else, and it was wired to
  the hierarchy path at `r6889+cc66.36`.  Both runs are `LSTEP=1 LMAXL=2000`, `r6941_fine_*`'s own grid.
"""
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = '/tmp/n66/r6975'
STEP = 250
NK = 2547                                    # the control's mode count at LMAXL=2000


def fold(tag, nk=NK):
    fs = sorted((int(re.search(r'_k(\d+)$', x[:-4]).group(1)), x)
                for x in os.listdir(f'{D}/mix')
                if x.startswith(f'{tag}_k') and x.endswith('.npz'))
    assert [i for i, _ in fs] == list(range(0, nk, STEP)), f'{tag}: slices {[i for i, _ in fs]}'
    ds = [np.load(os.path.join(D, 'mix', x)) for _, x in fs]
    ls = ds[0]['ls']
    for d in ds:
        assert np.array_equal(d['ls'], ls), f'{tag}: slices differ on the multipoles'
    return dict(ls=ls, Dl=sum(d['Dl'] for d in ds), l_A=ds[0]['l_A'], D_M=ds[0]['D_M'],
                r_s=ds[0]['r_s'], arm=ds[0]['arm'])


for tag, dp in (('mix_lcdm', 0.8794), ('mixb_lcdm', 0.60)):
    out = fold(tag)
    out['dpsrc'] = float(dp)
    np.savez(os.path.join(SP, f'r6975_{tag}.npz'), **out)
    print(f'  {tag}: {len(out["ls"])} multipoles at LSTEP=1, DPSRC={dp:g} '
          f'-> spectra/r6975_{tag}.npz')

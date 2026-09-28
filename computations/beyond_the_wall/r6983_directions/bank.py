"""fold r6983's JOINT run into the bank the receipt reads -- r6983+cc66.49.

  * `r6983_joint_lcdm.npz` -- the control carrying BOTH channels at once, each at the size its own
    revision measured and neither coefficient re-chosen here:
      · the window's phase spread matched to the arm's and weight-preserving --
        `SRCTAPER=0.0001100877765 SRCTAPERS0=145.3465211 SRCTAPERNORM=1`, solved at `r6959+cc66.47`;
      · the arm's monopole fraction imposed on the term mix --
        `DPSRC=0.8794`, solved from `r6959`'s `SRCETA` profiles at `r6975+cc66.48`.

*** WHAT THE BANK IS FOR, AND IT IS ONE NUMBER. ***  `cc66.48` measured the two channels at 1.14 and
1.58 times the excess and observed that they do not add -- but "do not add" was read off a COMPOSITION
RULE nobody had measured, and three rules disagree about what the pair should give: multiplicative
1.1035, sum 1.1019, quadrature 1.0839, against the measured excess's own 1.0400.  This run is the
arbiter: it applies both operations to one spectrum and reads the joint intercept off it, so the rule
is measured rather than assumed.  ⛔ *Nothing in the prediction is fitted to it -- all four numbers are
pre-registered in `PREDICTION.md`, which is committed ahead of this file.*

⌗ `LSTEP=1 LMAXL=2000` is `r6941_fine_*`'s own grid, so the joint response is read against the same
  baselines with the same anchored locator as each channel alone -- and against the SYMMETRIC BASELINE
  1.95 rather than 1, which `cc66.48` established and which every reading here uses.

⚠ ** THE SLICING IS VERIFIED, NOT ASSUMED, AND THE REASON IS OPERATIONAL. **  `KSLICE=lo:hi` is a plain
index slice of the mode list, so any tiling of `[0, 2547)` into disjoint contiguous spans sums to the
same spectrum.  This seat's container is reclaimed every ten to twenty minutes and a 250-mode slice above
index 750 takes longer than that, so those slices restarted at every churn and never landed while the
three below 750 landed first time.  ⇒ *The run was re-sliced at 100 modes above 750 (`launch_fine.sh`),
which changes the unit of work and nothing about the operation.*  ** So this file reconstructs each
slice's SPAN from its filename and asserts that the spans tile `[0, 2547)` exactly -- no gap, no overlap,
nothing counted twice -- rather than asserting a fixed step, which would have been a check on the
bookkeeping convention instead of on the sum. **
"""
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = '/tmp/n66/r6983'
STEP = 250
NK = 2547                                    # the control's mode count at LMAXL=2000


def span_of(name):
    """the mode span a slice file covers -- `_s<lo>_<hi>` carries it, `_k<lo>` implies `STEP`"""
    m = re.search(r'_s(\d+)_(\d+)$', name)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = re.search(r'_k(\d+)$', name)
    if m:
        return int(m.group(1)), int(m.group(1)) + STEP
    raise AssertionError(f'{name}: the filename carries no mode span')


def fold(tag, nk=NK):
    fs = sorted((span_of(x[:-4]), x) for x in os.listdir(f'{D}/joint')
                if x.startswith(f'{tag}_') and x.endswith('.npz'))
    lo = 0
    for (a, b), x in fs:
        assert a == lo, f'{tag}: the slices do not tile -- {x} starts at {a}, expected {lo}'
        assert b > a, f'{tag}: {x} has an empty span'
        lo = b
    assert lo >= nk, f'{tag}: the slices reach {lo} of {nk} modes'
    assert fs[-1][0][0] < nk, f'{tag}: a slice starts past the last mode'
    ds = [np.load(os.path.join(D, 'joint', x)) for _, x in fs]
    ls = ds[0]['ls']
    for d in ds:
        assert np.array_equal(d['ls'], ls), f'{tag}: slices differ on the multipoles'
    print(f'  {tag}: {len(fs)} slice(s) tiling [0, {nk}) with no gap and no overlap')
    return dict(ls=ls, Dl=sum(d['Dl'] for d in ds), l_A=ds[0]['l_A'], D_M=ds[0]['D_M'],
                r_s=ds[0]['r_s'], arm=ds[0]['arm'])


for tag, srct, s0, dp in (('joint_lcdm', 0.0001100877765, 145.3465211, 0.8794),):
    out = fold(tag)
    out['srctaper'] = float(srct)
    out['srctapers0'] = float(s0)
    out['srctapernorm'] = 1
    out['dpsrc'] = float(dp)
    np.savez(os.path.join(SP, f'r6983_{tag}.npz'), **out)
    print(f'  {tag}: {len(out["ls"])} multipoles at LSTEP=1, '
          f'SRCTAPER={srct:g} SRCTAPERNORM=1 DPSRC={dp:g} -> spectra/r6983_{tag}.npz')

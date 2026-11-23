# -*- coding: utf-8 -*-
"""r7860 (60) Ⓐ① -- THE POLARISATION BLOCKS WIRED UNDER `FOURPI`, MEASURED ON THREE LEGS.

⛭ `r7857` (69) ruled ① that the polarisation blocks take the SAME TWO FACTORS as TT, both being
definitions rather than fits.  This wires `_FP_ACC` onto the EE and TE accumulations and `_FP_DL`
onto the line that writes their `D_l`, and then MEASURES the result on three legs of one
configuration rather than asserting it:

  * leg `main` -- the merged head's own instrument, `FOURPI` unset;
  * leg `tree` -- this revision's instrument, `FOURPI` unset;
  * leg `on`   -- this revision's instrument, `FOURPI=1`.

⛔ The criterion registered BEFORE this ran: `main` and `tree` BITWISE identical on `ls`, `Dl`,
`Dl_EE` and `Dl_TE`; and `on` exactly twice `tree` on EACH of the three blocks, worst
`|ratio - 2| < 1e-12`.  A block that moves by something other than two REFUTES the ruling's premise
for that block and is reported as that.

⌗ The temporary instrument copies live in the instrument's OWN directory, because it imports
siblings by name -- the failure `r7858` hit when it put them elsewhere.  They are removed again.

    python3 wire.py        # rc=0 when the arm holds
"""
import io
import json
import os
import subprocess
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
#: ⛔ FOUR dirnames: this file sits three directories below the repository root.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
INST = os.path.join(BW, 'ACOUSTIC_two_arm.py')

#: the bank point's own switches, copied from cc66's committed `regen_control_point.sh`, with the
#: multipole reach cut so the three legs cost minutes: the arm is a RATIO between legs of ONE
#: configuration, and a ratio does not need the bank's full reach to be exact.
BASE = dict(ARM='lcdm', LH0='67.40', LOM='0.3150', WBH2='0.0224', NS='0.965', MNU='0.00',
            HIER='1', LMAXL='400', LSTEP='8')


def leg(tag, src, fourpi):
    """run one leg and return its saved polarisation bank"""
    tmp = os.path.join(BW, '_r7860_ctrl_%s.py' % tag)
    out = os.path.join(_HERE, '_leg_%s.npz' % tag)
    with io.open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(src)
    env = dict(os.environ)
    env.update(BASE)
    env['POLSAVE'] = out
    env['SAVE'] = os.path.join(_HERE, '_leg_%s_tt.npz' % tag)
    env.pop('FOURPI', None)
    if fourpi:
        env['FOURPI'] = '1'
    try:
        r = subprocess.run([sys.executable, os.path.basename(tmp)], cwd=BW, env=env,
                           capture_output=True)
        if not os.path.exists(out):
            sys.stderr.write(r.stdout.decode()[-3000:] + r.stderr.decode()[-3000:])
            raise SystemExit('  ⛔ leg %s produced no bank' % tag)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    return dict(np.load(out, allow_pickle=True))


MAIN_SRC = subprocess.run(['git', 'show', 'HEAD:computations/beyond_the_wall/ACOUSTIC_two_arm.py'],
                          cwd=ROOT, capture_output=True).stdout.decode()
TREE_SRC = io.open(INST, encoding='utf-8').read()
assert MAIN_SRC and TREE_SRC != MAIN_SRC, 'nothing to measure: the trees agree'

print(__doc__)
print('=' * 100)
print('\n  running three legs at LMAXL=%s, LSTEP=%s ...' % (BASE['LMAXL'], BASE['LSTEP']),
      flush=True)
M = leg('main', MAIN_SRC, False)
T = leg('tree', TREE_SRC, False)
N = leg('on', TREE_SRC, True)

KEYS = ('ls', 'Dl', 'Dl_EE', 'Dl_TE')
off = {}
for k in KEYS:
    a, b = np.asarray(M[k], float), np.asarray(T[k], float)
    off[k] = dict(n=int(a.size), bitwise_identical=bool(np.array_equal(a, b)),
                  worst_abs=float(np.max(np.abs(a - b))) if a.size else 0.0)
byte_identical = all(v['bitwise_identical'] for v in off.values())

BLOCKS = (('TT', 'Dl'), ('EE', 'Dl_EE'), ('TE', 'Dl_TE'))
on = {}
for name, k in BLOCKS:
    a, b = np.asarray(T[k], float), np.asarray(N[k], float)
    m = np.abs(a) > 0
    r = b[m] / a[m]
    on[name] = dict(n=int(m.sum()), mean=float(np.mean(r)),
                    worst_distance_from_two=float(np.max(np.abs(r - 2.0))),
                    exactly_two=bool(np.max(np.abs(r - 2.0)) < 1e-12))

print('\n  Ⓐ① THE OFF LEG, AGAINST THE MERGED HEAD\'S OWN INSTRUMENT')
print('  ' + '-' * 98)
for k in KEYS:
    print('    %-7s  n=%-4d  bitwise identical: %-5s  worst |diff| %.3e'
          % (k, off[k]['n'], off[k]['bitwise_identical'], off[k]['worst_abs']))
print('\n  Ⓐ① THE ON LEG, BLOCK BY BLOCK')
print('  ' + '-' * 98)
for name, _ in BLOCKS:
    d = on[name]
    print('    %-3s  n=%-4d  ratio mean %.12f   worst |ratio-2| %.3e   exactly two: %s'
          % (name, d['n'], d['mean'], d['worst_distance_from_two'], d['exactly_two']))

holds = byte_identical and all(on[n]['exactly_two'] for n, _ in BLOCKS)
rec = dict(holds=bool(holds), config=BASE, off=dict(arrays=off, byte_identical=byte_identical,
                                                    n_multipoles=int(np.asarray(M['ls']).size)),
           on=on)
with io.open(os.path.join(_HERE, 'wire.json'), 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(rec, indent=1, sort_keys=True))
for f in os.listdir(_HERE):
    if f.startswith('_leg_'):
        os.remove(os.path.join(_HERE, f))
print('\n  %s Ⓐ① %s' % ('✔' if holds else '⛔', 'holds' if holds else 'FAILS'))
sys.exit(0 if holds else 1)

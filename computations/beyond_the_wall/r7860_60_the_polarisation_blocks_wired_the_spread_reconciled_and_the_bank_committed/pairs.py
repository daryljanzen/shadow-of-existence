# -*- coding: utf-8 -*-
"""r7860 (60) Ⓖ⑦ -- `FOURPI` REACHES THE BILINEAR PAIRS TOO, AT `r7859`'s ORDER.

⛭ `69` ordered this after `cc66` READ THE SOURCE and found what this seat's own two revisions on
the switch had missed: the bilinear decomposition is accumulated BESIDE `out[j]`, so it never saw
the accumulation factor, and the save wrote `Dl_pairs` without the `D_l` factor the `Dl` beside it
carries.  ⇒ **With the switch on, the ten pairs would have stopped summing to the `D_l` saved next
to them by exactly a factor two, and the instrument's own closure print — which four receipts and
seven arms read — would have contradicted itself while still printing a number.**

⛔ **THIS ARM IS NOT THIS SEAT'S FINDING AND SAYS SO.**  It is the measurement that the ordered
repair does what the order says, on three legs of one configuration:

  * the switch unset, against the base's own instrument: BITWISE identical on `ls`, `Dl` and
    `Dl_pairs`;
  * the switch set: `Dl` and `Dl_pairs` BOTH multiplied by exactly two, so the closure is unmoved;
  * and the closure itself, read off the instrument's own print on both legs.

⌗ And the un-repaired state is measured too, by running the base's instrument with the switch ON:
that is the `0.5` the order predicts, reproduced here rather than taken on trust.

    python3 pairs.py        # rc=0 when the arm holds
"""
import io
import json
import os
import re
import subprocess
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
#: ⛔ FOUR dirnames: this file sits three directories below the repository root.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
INST = os.path.join(BW, 'ACOUSTIC_two_arm.py')
BASE = dict(ARM='lcdm', LH0='67.40', LOM='0.3150', WBH2='0.0224', NS='0.965', MNU='0.00',
            HIER='1', LMAXL='400', LSTEP='8')


def leg(tag, src, fourpi):
    tmp = os.path.join(BW, '_r7860_pairs_%s.py' % tag)
    out = os.path.join(_HERE, '_pairs_%s.npz' % tag)
    with io.open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(src)
    env = dict(os.environ)
    env.update(BASE)
    env['SRCDEC'] = out
    env['SAVE'] = os.path.join(_HERE, '_pairs_%s_tt.npz' % tag)
    env.pop('FOURPI', None)
    if fourpi:
        env['FOURPI'] = '1'
    try:
        r = subprocess.run([sys.executable, os.path.basename(tmp)], cwd=BW, env=env,
                           capture_output=True)
        txt = r.stdout.decode()
        if not os.path.exists(out):
            sys.stderr.write(txt[-3000:] + r.stderr.decode()[-3000:])
            raise SystemExit('  ⛔ leg %s produced no decomposition' % tag)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    m = re.search(r'the pairs close on D_l to ([0-9.eE+-]+) relative', txt)
    return dict(np.load(out, allow_pickle=True)), (float(m.group(1)) if m else None)


BASE_SRC = subprocess.run(['git', 'show', 'HEAD:computations/beyond_the_wall/ACOUSTIC_two_arm.py'],
                          cwd=ROOT, capture_output=True).stdout.decode()
TREE_SRC = io.open(INST, encoding='utf-8').read()
assert BASE_SRC and TREE_SRC != BASE_SRC, 'nothing to measure: the trees agree'

print(__doc__)
print('=' * 100)
print('\n  running four legs at LMAXL=%s ...' % BASE['LMAXL'], flush=True)
BO, BO_cl = leg('base_off', BASE_SRC, False)
BN, BN_cl = leg('base_on', BASE_SRC, True)
TO, TO_cl = leg('tree_off', TREE_SRC, False)
TN, TN_cl = leg('tree_on', TREE_SRC, True)

KEYS = ('ls', 'Dl', 'Dl_pairs')
off = {}
for k in KEYS:
    a, b = np.asarray(BO[k], float), np.asarray(TO[k], float)
    off[k] = dict(bitwise_identical=bool(np.array_equal(a, b)),
                  worst_abs=float(np.max(np.abs(a - b))))
byte_identical = all(v['bitwise_identical'] for v in off.values())


def ratio(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    m = a != 0
    r = b[m] / a[m]
    return float(np.mean(r)), float(np.max(np.abs(r - 2.0)))


dl_mean, dl_worst = ratio(TO['Dl'], TN['Dl'])
pr_mean, pr_worst = ratio(TO['Dl_pairs'].sum(axis=1), TN['Dl_pairs'].sum(axis=1))


def closure(z):
    d = np.asarray(z['Dl_pairs'], float).sum(axis=1)
    dl = np.asarray(z['Dl'], float)
    return float(np.max(np.abs(d - dl) / np.abs(dl)))


print('\n  Ⓖ⑦ THE OFF LEG, AGAINST THE BASE\'S OWN INSTRUMENT')
print('  ' + '-' * 98)
for k in KEYS:
    print('    %-9s bitwise identical: %-5s  worst |diff| %.3e'
          % (k, off[k]['bitwise_identical'], off[k]['worst_abs']))
print('\n  Ⓖ⑦ THE ON LEG -- `Dl` AND THE PAIRS MUST MOVE TOGETHER')
print('  ' + '-' * 98)
print('    Dl        ratio %.12f   worst |ratio-2| %.3e' % (dl_mean, dl_worst))
print('    the pairs ratio %.12f   worst |ratio-2| %.3e' % (pr_mean, pr_worst))
print('\n  Ⓖ⑦ THE CLOSURE, read off the instrument\'s own print and recomputed from the arrays')
print('  ' + '-' * 98)
print('    base, switch off : print %.3e   arrays %.3e' % (BO_cl, closure(BO)))
print('    base, switch ON  : print %.3e   arrays %.3e   ⇐ the un-repaired state'
      % (BN_cl, closure(BN)))
print('    tree, switch off : print %.3e   arrays %.3e' % (TO_cl, closure(TO)))
print('    tree, switch ON  : print %.3e   arrays %.3e' % (TN_cl, closure(TN)))
base_on_ratio = float(np.mean(np.asarray(BN['Dl_pairs'], float).sum(axis=1)
                              / np.asarray(BN['Dl'], float)))
print('\n    ⇒ un-repaired with the switch on, the pairs sum to %.6f of the `Dl` beside them -- the'
      % base_on_ratio)
print('      factor the order predicts, reproduced here rather than taken on trust.')

holds = bool(byte_identical and dl_worst < 1e-12 and pr_worst < 1e-12
             and closure(TN) < 1e-6 and abs(base_on_ratio - 0.5) < 1e-6)
rec = dict(holds=holds, off=dict(arrays=off, byte_identical=byte_identical),
           on=dict(dl_mean=dl_mean, dl_worst=dl_worst, pairs_mean=pr_mean, pairs_worst=pr_worst),
           closure=dict(base_off=closure(BO), base_on=closure(BN), tree_off=closure(TO),
                        tree_on=closure(TN), printed_tree_on=TN_cl),
           unrepaired_pairs_over_dl=base_on_ratio, found_by='cc66, read off the source at r7859')
with io.open(os.path.join(_HERE, 'pairs.json'), 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(rec, indent=1, sort_keys=True))
for f in os.listdir(_HERE):
    if f.startswith('_pairs_'):
        os.remove(os.path.join(_HERE, f))
print('\n  %s Ⓖ⑦ %s\n' % ('✔' if holds else '⛔', 'holds' if holds else 'FAILS'))
sys.exit(0 if holds else 1)

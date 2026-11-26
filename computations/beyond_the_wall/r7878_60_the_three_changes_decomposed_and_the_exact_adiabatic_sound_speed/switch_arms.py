# -*- coding: utf-8 -*-
"""r7878+60 — THE SWITCH'S OWN ARMS, before any component is read.

Three claims, each measured on OUTPUT rather than asserted:

  ① **OFF IS STILL BYTE-IDENTICAL.** `origin/main`'s instrument against the patched one, with
     `NUPERT` absent and with `NUPERT=0`, every array compared element for element.
  ② **ON WITH THE DEFAULTS IS STILL `r7876`'s RUN.** `origin/main`'s instrument at `NUPERT=1`
     against the patched one at `NUPERT=1` with no component switch set -- bit-identical, which is
     a stronger statement than "the four amplitudes come back the same" and costs one pair of runs
     instead of a refit.
  ③ **IT REFUSES WHAT IT CANNOT RUN:** the background switch missing, a zero sum, a letter that is
     not one of `WCE`, an empty set, and the exact sound speed asked for without the Euler change.

⌗ *Cheap on purpose: `LMAXL=300 LSTEP=60`.  Identity is identity, and a coarse grid exercises every
  line the switches touch -- both right-hand sides, the four source paths and the weight -- in about
  twenty seconds a leg.*

    NODE=60 python3 switch_arms.py
"""
import io
import json
import os
import subprocess
import sys
import tempfile

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_REPO = os.path.dirname(os.path.dirname(_BTW))
REL = 'computations/beyond_the_wall/ACOUSTIC_two_arm.py'
PRE = os.path.join(_BTW, '_prepatch_ACOUSTIC_two_arm.py')      # same depth: the file reads __file__
BASE = dict(BVEL='1', NUFD='1', ARM='lcdm', LH0='67.40', LOM='0.3150', WBH2='0.0224',
            NS='0.965', MNU='0.30', HIER='1', LMAXL='300', LSTEP='60')


def one(script, out, extra=None):
    env = dict(os.environ)
    env.update(BASE)
    env['SAVE'] = out + '_tt.npz'
    env['POLSAVE'] = out + '_pol.npz'
    for k in ('NUPERT', 'NUSHOFF', 'NUPARTS', 'NUCA'):
        env.pop(k, None)
    env.update(extra or {})
    p = subprocess.run([sys.executable, script], cwd=_BTW, env=env,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.returncode, p.stdout.decode('utf-8', 'replace')


def same(a_pfx, b_pfx, tmp):
    """every array of both saves, element for element; `config` reported apart"""
    rows, ok = {}, True
    for which in ('tt', 'pol'):
        a = np.load(os.path.join(tmp, '%s_%s.npz' % (a_pfx, which)), allow_pickle=True)
        b = np.load(os.path.join(tmp, '%s_%s.npz' % (b_pfx, which)), allow_pickle=True)
        ka, kb = sorted(a.files), sorted(b.files)
        keys = [k for k in ka if k != 'config']
        eq = (ka == kb and all(a[k].dtype == b[k].dtype and a[k].shape == b[k].shape
                               and a[k].tobytes() == b[k].tobytes() for k in keys))
        rows[which] = dict(arrays_identical=bool(eq), n_arrays=len(keys),
                           config_same=bool(str(a['config']) == str(b['config'])))
        ok = ok and eq
    return ok, rows


def main():
    print(__doc__)
    print('=' * 100)
    src = subprocess.run(['git', 'show', 'origin/main:' + REL], cwd=_REPO,
                         stdout=subprocess.PIPE, check=True).stdout
    io.open(PRE, 'wb').write(src)
    tmp = tempfile.mkdtemp(prefix='r7878_arms_')
    rec = {}
    try:
        legs = {
            'landed_off': (PRE, None),
            'patched_absent': (os.path.join(_BTW, 'ACOUSTIC_two_arm.py'), None),
            'patched_zero': (os.path.join(_BTW, 'ACOUSTIC_two_arm.py'), {'NUPERT': '0'}),
            'landed_on': (PRE, {'NUPERT': '1'}),
            'patched_on': (os.path.join(_BTW, 'ACOUSTIC_two_arm.py'), {'NUPERT': '1'}),
        }
        rcs = {}
        for name, (script, extra) in legs.items():
            rcs[name], _ = one(script, os.path.join(tmp, name), extra)
        print('\n  return codes: %s' % rcs)
        assert all(v == 0 for v in rcs.values()), '  ⛔ a leg did not run'

        print('\n  ① OFF IS BYTE-IDENTICAL')
        ok1, r1 = same('landed_off', 'patched_absent', tmp)
        ok2, r2 = same('landed_off', 'patched_zero', tmp)
        for lbl, (o, r) in (('absent', (ok1, r1)), ('NUPERT=0', (ok2, r2))):
            for which, v in sorted(r.items()):
                print('     %-4s landed vs %-9s : %2d array(s) %s ; config %s'
                      % (which, lbl, v['n_arrays'],
                         'IDENTICAL' if v['arrays_identical'] else '** DIFFER **',
                         'same' if v['config_same'] else 'differs -- the blob hash, and must'))
        rec['off_identical'] = bool(ok1 and ok2)
        rec['off_rows'] = {'absent': r1, 'zero': r2}

        print('\n  ② ON WITH THE DEFAULTS IS STILL THE PREVIOUS REVISION\'S RUN')
        ok3, r3 = same('landed_on', 'patched_on', tmp)
        for which, v in sorted(r3.items()):
            print('     %-4s landed-on vs patched-on : %2d array(s) %s ; config %s'
                  % (which, v['n_arrays'],
                     'IDENTICAL' if v['arrays_identical'] else '** DIFFER **',
                     'same' if v['config_same'] else 'differs -- it now records the two new keys'))
        rec['on_identical'] = bool(ok3)
        rec['on_rows'] = r3

        print('\n  ③ AND IT REFUSES WHAT IT CANNOT RUN')
        REF = [('no NUFD', {'NUPERT': '1', 'NUFD': '0'}, 'NUPERT=1 needs NUFD=1'),
               ('zero sum', {'NUPERT': '1', 'MNU': '0.0'}, 'NUPERT=1 needs NUFD=1'),
               ('a bad letter', {'NUPERT': '1', 'NUPARTS': 'WX'}, 'the letters are W'),
               ('an empty set', {'NUPERT': '1', 'NUPARTS': ''}, 'the letters are W'),
               ('NUCA without E', {'NUPERT': '1', 'NUPARTS': 'WC', 'NUCA': '1'},
                'NUCA=1 needs E in NUPARTS')]
        rec['refusals'] = {}
        for name, extra, needle in REF:
            rc, out = one(os.path.join(_BTW, 'ACOUSTIC_two_arm.py'),
                          os.path.join(tmp, 'ref'), extra=extra)
            hit = [l for l in out.splitlines() if needle in l]
            good = rc != 0 and bool(hit)
            rec['refusals'][name] = dict(rc=rc, refused=bool(good),
                                         message=hit[0].strip() if hit else None)
            print('     %-16s rc=%d  %s' % (name, rc, 'REFUSES' if good else '** RAN **'))

        rec['all_pass'] = bool(rec['off_identical'] and rec['on_identical']
                               and all(v['refused'] for v in rec['refusals'].values()))
    finally:
        if os.path.exists(PRE):
            os.remove(PRE)
    print('\n  ⇒ %s' % ('all three arms pass' if rec.get('all_pass')
                        else '** AN ARM DOES NOT PASS **'))
    json.dump(rec, io.open(os.path.join(_HERE, 'switch_arms.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote switch_arms.json')
    return 0 if rec.get('all_pass') else 1


if __name__ == '__main__':
    sys.exit(main())

# -*- coding: utf-8 -*-
"""r7876+60 item ③'s FIRST ARM — `NUPERT` off is byte-identical, and on it refuses to run half.

The order requires the switch `"default off, byte-identical off"`.  That is a claim about OUTPUT, so
it is measured on output: the LANDED instrument -- `origin/main`'s copy of the file -- and the
patched one are each run at the same control point, and every array of both saves is compared
element for element as raw bytes.

⌗ *The comparison is run twice: with `NUPERT` ABSENT and with `NUPERT=0`, because "default off" and
  "off" are two claims.*
⌗ *The `config` provenance string is EXPECTED to differ, and the reason is worth stating exactly
  rather than waved at: it carries `instrument_blob`, the git blob hash of the file's own bytes,
  which necessarily changes when the file changes -- and it now also carries the two keys this
  revision adds for the reason `r7864` established.  So a config string that AGREED here would mean
  the patch had not been applied.  It is reported separately rather than excluded silently.*

⌗ *Cheap on purpose: `LMAXL=300 LSTEP=60`.  Identity is identity, and a coarse grid exercises every
  line the switch touches -- both right-hand sides, the four source paths and the shear -- in about
  twenty seconds a leg instead of twenty minutes.*

⌗ *And the two REFUSALS: `NUPERT=1` without `NUFD=1`, and with a zero sum.  The repair IS the
  species' own Fermi-Dirac weight, so neither is a configuration it may silently run.*

    NODE=60 python3 byte_identical.py
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
    env.update(extra or {})
    env.pop('NUPERT', None) if extra is None else None
    p = subprocess.run([sys.executable, script], cwd=_BTW, env=env,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.returncode, p.stdout.decode('utf-8', 'replace')


def main():
    print(__doc__)
    rec = {}
    src = subprocess.run(['git', 'show', 'origin/main:' + REL], cwd=_REPO,
                         stdout=subprocess.PIPE, check=True).stdout
    io.open(PRE, 'wb').write(src)
    tmp = tempfile.mkdtemp(prefix='r7876_bid_')
    try:
        legs = {}
        rc, _ = one(PRE, os.path.join(tmp, 'landed'))
        legs['landed'] = rc
        rc, _ = one(os.path.join(_BTW, 'ACOUSTIC_two_arm.py'), os.path.join(tmp, 'absent'))
        legs['absent'] = rc
        rc, _ = one(os.path.join(_BTW, 'ACOUSTIC_two_arm.py'), os.path.join(tmp, 'zero'),
                    extra={'NUPERT': '0'})
        legs['zero'] = rc
        print('\n  return codes: %s' % legs)
        assert all(v == 0 for v in legs.values()), '  ⛔ a leg did not run'

        ok = True
        rec['compare'] = {}
        for which in ('tt', 'pol'):
            a = np.load(os.path.join(tmp, 'landed_%s.npz' % which), allow_pickle=True)
            for other in ('absent', 'zero'):
                b = np.load(os.path.join(tmp, '%s_%s.npz' % (other, which)), allow_pickle=True)
                ka, kb = sorted(a.files), sorted(b.files)
                keys = [k for k in ka if k != 'config']
                same = (ka == kb and all(a[k].dtype == b[k].dtype and a[k].shape == b[k].shape
                                         and a[k].tobytes() == b[k].tobytes() for k in keys))
                cfg_same = str(a['config']) == str(b['config'])
                rec['compare']['%s|%s' % (which, other)] = dict(
                    arrays_identical=bool(same), n_arrays=len(keys), config_same=bool(cfg_same))
                print('  %-4s landed vs %-7s : %2d array(s) %s ; config string %s'
                      % (which, other, len(keys),
                         'IDENTICAL' if same else '** DIFFER **',
                         'same' if cfg_same else 'differs -- the blob hash, and must'))
                ok = ok and same
        rec['byte_identical'] = bool(ok)
        print('\n  ⇒ BYTE-IDENTICAL OFF: %s' % ('PASSES' if ok else '** FAILS **'))

        print('\n  the two refusals:')
        rec['refusals'] = {}
        for name, extra in (('no NUFD', {'NUPERT': '1', 'NUFD': '0'}),
                            ('zero sum', {'NUPERT': '1', 'MNU': '0.0'})):
            rc, out = one(os.path.join(_BTW, 'ACOUSTIC_two_arm.py'),
                          os.path.join(tmp, 'ref'), extra=extra)
            msg = [l for l in out.splitlines() if 'NUPERT=1 needs' in l]
            good = rc != 0 and bool(msg)
            rec['refusals'][name] = dict(rc=rc, refused=bool(good),
                                         message=msg[0].strip() if msg else None)
            print('    %-9s rc=%d  %s' % (name, rc, 'REFUSES' if good else '** RAN **'))
            ok = ok and good
        rec['all_pass'] = bool(ok)
    finally:
        if os.path.exists(PRE):
            os.remove(PRE)
    json.dump(rec, io.open(os.path.join(_HERE, 'byte_identical.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('\n  wrote byte_identical.json')
    return 0 if rec.get('all_pass') else 1


if __name__ == '__main__':
    sys.exit(main())

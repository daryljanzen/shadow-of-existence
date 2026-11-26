# -*- coding: utf-8 -*-
"""r7878+60 — ** THE CLOCK CORRECTION, MEASURED ON OUTPUT BOTH WAYS. **

`clock.py` measured the FACTOR (`Jac`) the uncorrected term carried.  This measures the
CONSEQUENCE, on the instrument's own output, with the exact sound speed switched on:

  ① **ON `lcdm` THE CORRECTION IS A BIT-LEVEL NO-OP** -- the uncorrected file and the corrected one
     produce identical arrays, element for element, at `NUCA=1`.  That is what licenses leaving
     this revision's ten banks alone and restating none of its numbers.
  ② **ON `cr` IT IS NOT** -- the same pair differs, which is the positive control: a correction
     that changed nothing anywhere would be decoration, and this one bites exactly where `Jac != 1`.

⌗ NOT RETYPED.  The leg runner and the array comparison are `switch_arms.py`'s own `one` and
  `same`, IMPORTED rather than copied, so both files measure identity the same way.
⌗ The uncorrected file is not kept in the tree: it is materialised from `git show HEAD:<path>`,
  which is the committed state before this correction, and deleted afterwards.

    NODE=60 python3 clock_arms.py
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from switch_arms import REL, _BTW, _REPO, one, same          # noqa: E402

PRE = os.path.join(_BTW, '_preclock_ACOUSTIC_two_arm.py')
CUR = os.path.join(_BTW, 'ACOUSTIC_two_arm.py')
ON = dict(NUPERT='1', NUPARTS='WCE', NUCA='1')


def main():
    print(__doc__)
    print('=' * 100)
    src = subprocess.run(['git', 'show', 'HEAD:' + REL], cwd=_REPO,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if src.returncode != 0:
        raise SystemExit('  ⛔ could not read the committed instrument: %s'
                         % src.stdout.decode('utf-8', 'replace')[:400])
    pre = src.stdout
    cur = io.open(CUR, 'rb').read()
    #: ⛔ *the whole arm is vacuous if the two files are the same file, so that is gated first --
    #:   the control the `S55` class exists for.*
    if pre == cur:
        raise SystemExit('  ⛔ the committed instrument and the one on disk are IDENTICAL: there is '
                         'no correction to measure, and an arm that passes on nothing is worse '
                         'than no arm.')
    io.open(PRE, 'wb').write(pre)
    rec = {'differ_in_source': True,
           'uncorrected_has_leaf_rate': pre.count(b'3.0 * Hc * (1.0 + _w)') == 2,
           'corrected_has_grid_rate': cur.count(b'3.0 * float(Hc_of(e)) * (1.0 + _w)') == 2}
    print('  the two files differ, the uncorrected one divides by the leaf rate at both sites: %s'
          % rec['uncorrected_has_leaf_rate'])
    print('  and the corrected one divides by the grid rate at both sites: %s'
          % rec['corrected_has_grid_rate'])
    try:
        tmp = tempfile.mkdtemp(prefix='r7878_clock_')
        try:
            for arm in ('lcdm', 'cr'):
                for tag, script in (('pre', PRE), ('post', CUR)):
                    pfx = '%s_%s' % (arm, tag)
                    rc, out = one(script, os.path.join(tmp, pfx), dict(ON, ARM=arm))
                    if rc != 0:
                        raise SystemExit('  ⛔ %s leg failed rc=%d:\n%s' % (pfx, rc, out[-1500:]))
                    print('    ran %-10s rc=0' % pfx)
                ok, rows = same('%s_pre' % arm, '%s_post' % arm, tmp)
                rec[arm] = {'arrays_identical': bool(ok), 'rows': rows}
                print('  %-5s the corrected output is %s the uncorrected one'
                      % (arm, 'IDENTICAL to' if ok else '** NOT ** identical to'))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    finally:
        if os.path.exists(PRE):
            os.remove(PRE)
    rec['all_pass'] = bool(rec['uncorrected_has_leaf_rate'] and rec['corrected_has_grid_rate']
                           and rec['lcdm']['arrays_identical']
                           and not rec['cr']['arrays_identical'])
    print('\n  ⇒ %s' % ('the correction is a BIT-LEVEL NO-OP on `lcdm` and BITES on `cr`, which is '
                        'both halves of what was claimed'
                        if rec['all_pass'] else
                        '** NOT WHAT WAS CLAIMED -- do not restate the numbers on this **'))
    json.dump(rec, io.open(os.path.join(_HERE, 'clock_arms.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote clock_arms.json')
    return 0 if rec['all_pass'] else 1


if __name__ == '__main__':
    sys.exit(main())

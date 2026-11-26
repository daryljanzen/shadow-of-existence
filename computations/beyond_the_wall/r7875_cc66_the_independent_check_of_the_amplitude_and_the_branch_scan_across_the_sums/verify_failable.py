# -*- coding: utf-8 -*-
"""r7875+cc66 -- ARE THIS REVISION'S PINS FAILABLE?

The standing cycle requires it in those words: verify the pin is FAILABLE by perturbing the
computation and watching the receipt go red.  A two-sided comparison against a number that is never
perturbed is indistinguishable from a comparison against itself.

This perturbs the RECORD, not the receipt -- a receipt edited to fail proves nothing about the
receipt that ships.  One pinned value per trial, moved by one part in a thousand, with the SHIPPED
receipt run as a subprocess and a non-zero exit required.  Records are restored in a `finally`, and
the run ends by re-running the untouched receipt and requiring it GREEN, so a trial that failed to
restore cannot pass unnoticed.

    NODE=cc66 python3 verify_failable.py
"""
import copy
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(_BTW))
RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                       'P15_the_amplitude_is_confirmed_independently_and_is_not_bought_with_a_'
                       'shift_and_the_branch_is_one_across_the_range.py')
OUT = os.path.join(_HERE, 'verify_failable.json')

TRIALS = [
    ('amplitude_check.json', ['fits', 'TT|0.30', 'A_free'], "TT's 1.1516214 -- the item's answer"),
    ('amplitude_check.json', ['fits', 'TT|0.60', 'A_free'], "TT's 1.2959211 at 0.60"),
    ('amplitude_check.json', ['fits', 'EE|0.30', 'A_free'], "EE's 1.0140592"),
    ('amplitude_check.json', ['fits', 'TT|0.30', 'abs_diff_from_60'],
     "the 3.538034e-06 that separates my A from 60's"),
    ('amplitude_check.json', ['allowance', '0.30', 'allowed'],
     "the theta*-derived allowance 2.563377e-04"),
    ('amplitude_check.json', ['fits', 'TT|0.30', 'A_eps_zero'],
     "A at eps = 0, which refutes my own H8"),
    ('amplitude_check.json', ['fits', 'TT|0.30', 'A_all_321'],
     'the 321-multipole A that makes the set load-bearing'),
    ('amplitude_check.json', ['fits', 'EE|0.30', 'lensing_moves_A'],
     "EE's 0.036161 lensing move"),
    ('amplitude_check.json', ['fits', 'TT|0.30', 'interp_sensitivity'],
     'the interpolation sensitivity'),
    ('branch_scan.json', ['scan', 'rd_camb|0.20', 'midpoint_minus_worse'],
     'the widest midpoint margin, 0.036365 below'),
    ('branch_scan.json', ['scan', 'rd_camb|0.60', 'midpoint_minus_worse'],
     "the +0.000394 ridge the unscaled test would have called two basins"),
    ('branch_scan.json', ['scan', 'rd_min|0.30', 'excess_over_fatol'],
     "that ridge's 0.0831 of fatol"),
]


def _get(d, p):
    for k in p:
        d = d[k]
    return d


def _set(d, p, v):
    for k in p[:-1]:
        d = d[k]
    d[p[-1]] = v


def run():
    r = subprocess.run([sys.executable, '-W', 'ignore', RECEIPT],
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       env=dict(os.environ, NODE='cc66'))
    return r.returncode, r.stdout.decode('utf-8', 'replace')


def main():
    print(__doc__)
    print('=' * 100)
    assert os.path.exists(RECEIPT), RECEIPT
    rc, _ = run()
    print('\n  the SHIPPED receipt, untouched: exit %d  %s'
          % (rc, 'GREEN' if rc == 0 else '⛔ ALREADY RED'))
    if rc != 0:
        sys.exit('FATAL: red before any perturbation.')
    res, caught, bak = [], 0, {}
    try:
        for rec in sorted({t[0] for t in TRIALS}):
            src = os.path.join(_HERE, rec)
            assert os.path.exists(src), src
            fd, b = tempfile.mkstemp(suffix='.bak.json')
            os.close(fd)
            shutil.copy2(src, b)
            bak[src] = b
        for i, (rec, path, what) in enumerate(TRIALS, 1):
            src = os.path.join(_HERE, rec)
            real = json.load(io.open(bak[src], encoding='utf-8'))
            was = _get(real, path)
            moved = copy.deepcopy(real)
            new = was * 1.001 if was else 1e-6
            if new == was:
                new = was + 1e-6
            _set(moved, path, new)
            io.open(src, 'w', encoding='utf-8').write(json.dumps(moved, indent=1, sort_keys=True))
            rc, out = run()
            shutil.copy2(bak[src], src)
            nf = sum(1 for ln in out.split('\n') if ln.strip().startswith('[FAIL]'))
            ok = rc != 0
            caught += 1 if ok else 0
            print('\n  trial %2d  %s' % (i, '.'.join(map(str, path))))
            print('            %s' % what)
            print('            %r -> %r   exit %d, %d arm(s) FAIL   ⇒ %s'
                  % (was, new, rc, nf, 'CAUGHT' if ok else '⛔ NOT CAUGHT -- VACUOUS PIN'))
            res.append(dict(record=rec, path=list(map(str, path)), claim=what, was=was,
                            moved=new, exit=rc, failed_arms=nf, caught=ok))
    finally:
        for src, b in bak.items():
            shutil.copy2(b, src)
            os.unlink(b)
    rc, _ = run()
    print('\n  records restored, receipt again: exit %d  %s'
          % (rc, 'GREEN' if rc == 0 else '⛔ RESTORE FAILED'))
    print('\n' + '=' * 100)
    print('  %d of %d CAUGHT; restore %s' % (caught, len(TRIALS), 'GREEN' if rc == 0 else 'RED'))
    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(
        dict(trials=res, caught=caught, total=len(TRIALS), restored_green=bool(rc == 0)),
        indent=1, sort_keys=True))
    sys.exit(0 if (caught == len(TRIALS) and rc == 0) else 1)


if __name__ == '__main__':
    main()

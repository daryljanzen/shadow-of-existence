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
                       'P15_the_repair_legs_amplitudes_are_confirmed_on_a_second_fitter_and_the_'
                       'repair_trades_TT_for_EE.py')
OUT = os.path.join(_HERE, 'verify_failable.json')

TRIALS = [
    ('refit_legs.json', ['fits', 'shear_on|TT|0.30', 'A'], "shear_on TT's 0.8640022 -- the item"),
    ('refit_legs.json', ['fits', 'shear_off|TT|0.60', 'A'], "shear_off TT's 0.8110362"),
    ('refit_legs.json', ['fits', 'shear_on|EE|0.30', 'A'], "shear_on EE's 0.9447322"),
    ('refit_legs.json', ['fits', 'shear_off|EE|0.60', 'A'], "shear_off EE's 0.9112188"),
    ('refit_legs.json', ['fits', 'shear_off|TT|0.60', 'diff_from_60'],
     'the worst distance from 60, 8.818003e-06'),
    ('refit_legs.json', ['regression', 'TT|0.30', 'A'],
     "the regression control's re-derivation of r7875's 1.1516214"),
    ('refit_legs.json', ['ee_vs_band', 'shear_on|EE|0.30', 'dist'],
     "EE's 0.055268 against its 0.05 band"),
    ('refit_legs.json', ['direction', 'shear_on|TT|0.30', 'repaired_dist'],
     "TT's repaired distance 0.135998 -- the trade"),
    ('refit_legs.json', ['direction', 'shear_on|EE|0.30', 'repaired_dist'],
     "EE's repaired distance 0.055268 -- the other half of the trade"),
    ('refit_legs.json', ['separation', 'EE|0.30', 'mine'],
     "EE's unresolvable 6.422709e-07 separation"),
    ('refit_legs.json', ['separation', 'EE|0.30', 'my_floor'],
     "my own EE interpolation floor 5.307333e-05"),
    ('refit_legs.json', ['separation', 'TT|0.30', 'mine'],
     "TT's resolvable 0.003753 separation"),
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

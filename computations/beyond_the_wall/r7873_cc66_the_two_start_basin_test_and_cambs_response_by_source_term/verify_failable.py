# -*- coding: utf-8 -*-
"""r7873+cc66 -- ARE THIS REVISION'S PINS ACTUALLY FAILABLE?

The standing cycle requires it in those words: *"verify the pin is FAILABLE by perturbing the
computation and watching the receipt go red."*  A two-sided comparison against a number that is
never perturbed is indistinguishable from a comparison against itself.

⛔ WHAT THIS DOES NOT DO.  It does not perturb the receipt -- a receipt edited to fail proves
nothing about the receipt that ships.  It perturbs the RECORD the receipt reads, one pinned value
per trial, runs the SHIPPED receipt as a subprocess, and requires a NON-ZERO exit.  The real
records are restored in a `finally`, and the run ends by re-running the untouched receipt and
requiring it GREEN, so a trial that failed to restore cannot pass unnoticed.

Each trial moves one value by about one part in a thousand -- far smaller than any claim in the
receipt turns on, and far larger than the tolerances the pins carry.

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
                       'P15_the_two_start_scan_finds_one_basin_at_0_400_only_and_cambs_sum_'
                       'response_is_carried_by_the_early_isw_at_twice_its_weight.py')
OUT = os.path.join(_HERE, 'verify_failable.json')

# (record, path into it, what the receipt claims on it)
TRIALS = [
    ('source_terms.json', ['path_control', 'rel'],
     "the registered path control's own 1.976630e-03"),
    ('source_terms.json', ['closure', '0', 'sixteen_vs_own'],
     'the sixteen-pair closure residual that must EQUAL the path residual'),
    ('source_terms.json', ['closure', '0', 'autos_median_shortfall'],
     "the registered arithmetic's 26.683487 per cent shortfall"),
    ('source_terms.json', ['ratio_control', '0.6', 'frac_of_signal'],
     'the ratio control at 5.858855e-04 of signal'),
    ('source_terms.json', ['answer', '0.6', 'ISW', 'signed_share_of_response'],
     "ISW's 0.291812 share of the response"),
    ('source_terms.json', ['answer', '0.6', 'ISW', 'share_of_spectrum'],
     "ISW's 0.136091 weight -- the pin check_figures_pinned found ABSENT"),
    ('source_terms.json', ['interference', 'mono_x_isw'],
     'the monopole x ISW interference at 0.209044'),
    ('source_terms.json', ['isw_window', 'halves', '0.6', 'early',
                           'signed_share_of_ISW_response'],
     "the EARLY ISW's 0.945356 of the ISW response"),
    ('source_terms.json', ['isw_window', 'rel_to_undivided_isw'],
     "the window's closure at 1.049911e-14"),
    ('two_start.json', ['modes', 'rd_camb', 'dchi2'],
     "rd_camb's 0.08595087 chi2 separation"),
    ('two_start.json', ['modes', 'rd_min', 'dchi2'],
     "rd_min's 0.00000658 -- the pin whose tolerance was SLACK at 1e-7"),
    ('two_start.json', ['criterion', 'same_dh0'],
     "the registered criterion's own 0.5 bound, read from the record"),
    ('basin_detail.json', ['modes', 'rd_camb', 'midpoint_minus_worse'],
     "the midpoint's -0.05522985 below the worse endpoint"),
    ('basin_detail.json', ['modes', 'rd_min', 'excess_over_fatol'],
     "rd_min's 0.009668 of fatol -- the scale my first test lacked"),
    ('basin_detail.json', ['modes', 'rd_camb', 'separations', 'tau'],
     "the tau separation 0.00146063 the chi2 gap lives in"),
]


def _get(d, path):
    for k in path:
        d = d[k]
    return d


def _set(d, path, v):
    for k in path[:-1]:
        d = d[k]
    d[path[-1]] = v


def run_receipt():
    p = subprocess.run([sys.executable, '-W', 'ignore', RECEIPT],
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       env=dict(os.environ, NODE='cc66'))
    return p.returncode, p.stdout.decode('utf-8', 'replace')


def main():
    print(__doc__)
    print('=' * 100)
    assert os.path.exists(RECEIPT), RECEIPT
    rc, _ = run_receipt()
    print('\n  the SHIPPED receipt, untouched: exit %d  %s'
          % (rc, 'GREEN' if rc == 0 else '⛔ ALREADY RED -- nothing below means anything'))
    if rc != 0:
        sys.exit('FATAL: the receipt is red before any perturbation.')

    results, caught = [], 0
    backups = {}
    try:
        for rec in sorted({t[0] for t in TRIALS}):
            src = os.path.join(_HERE, rec)
            assert os.path.exists(src), src
            fd, bak = tempfile.mkstemp(suffix='.bak.json')
            os.close(fd)
            shutil.copy2(src, bak)
            backups[src] = bak

        for i, (rec, path, what) in enumerate(TRIALS, 1):
            src = os.path.join(_HERE, rec)
            real = json.load(io.open(backups[src], encoding='utf-8'))
            was = _get(real, path)
            moved = copy.deepcopy(real)
            # one part in a thousand, and never to zero
            new = was * 1.001 if was else 1e-6
            if new == was:
                new = was + 1e-6
            _set(moved, path, new)
            io.open(src, 'w', encoding='utf-8').write(json.dumps(moved, indent=1,
                                                                 sort_keys=True))
            rc, out = run_receipt()
            shutil.copy2(backups[src], src)
            nfail = 0
            for ln in out.split('\n'):
                if ln.strip().startswith('[FAIL]'):
                    nfail += 1
            ok = rc != 0
            caught += 1 if ok else 0
            print('\n  trial %2d  %s -> %s' % (i, '.'.join(map(str, path)), rec))
            print('            %s' % what)
            print('            moved %r -> %r   receipt exit %d, %d arm(s) FAIL   ⇒ %s'
                  % (was, new, rc, nfail, 'CAUGHT' if ok else '⛔ NOT CAUGHT -- the pin is VACUOUS'))
            results.append(dict(record=rec, path=list(map(str, path)), claim=what,
                                was=was, moved=new, exit=rc, failed_arms=nfail, caught=ok))
    finally:
        for src, bak in backups.items():
            shutil.copy2(bak, src)
            os.unlink(bak)

    rc, _ = run_receipt()
    print('\n  the records restored, the SHIPPED receipt again: exit %d  %s'
          % (rc, 'GREEN' if rc == 0 else '⛔ RESTORE FAILED'))
    print('\n' + '=' * 100)
    print('  %d of %d perturbation(s) CAUGHT; restore verified %s'
          % (caught, len(TRIALS), 'GREEN' if rc == 0 else 'RED'))
    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(
        dict(trials=results, caught=caught, total=len(TRIALS),
             restored_green=bool(rc == 0)), indent=1, sort_keys=True))
    print('  written %s' % os.path.relpath(OUT, ROOT))
    sys.exit(0 if (caught == len(TRIALS) and rc == 0) else 1)


if __name__ == '__main__':
    main()

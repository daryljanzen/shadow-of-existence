# -*- coding: utf-8 -*-
"""r7869+cc66 item ⑨ -- IS THE CONVERTED CLAUSE FAILABLE, AND IS THE ORDERED ONE BLIND?

Each trial names the arm it is for and the driver prints a MISS if a trial does not land there.
Trials ⑴-⑶ are the conversion's own; ⑷ is the one that measures 69's ordered form against the same
plant, which is the whole reason the conversion was not made on `config`.

    NODE=cc66 python3 verify_failable.py
"""
import io
import json
import os
import shutil
import subprocess
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(_BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT

RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                       'P15_the_sections_opening_figures_on_the_one_rate_and_the_published_comb_'
                       'is_298_5_not_298_94.py')
ONE = os.path.join(_BTW, 'r7783_cc66_the_sections_opening_figures_on_one_rate',
                   'leafgeom_refit_pol_cr.npz')
FOUR_DIR = os.path.join(_BTW, 'r7631_70_PO87_polarisation')
PLANT_DIR = os.path.join(ROOT, 'computations', '_r7869_failability_plant')
OUT = os.path.join(_HERE, 'failability.json')
MARK = '① THE FOURTH FEATURE NEEDED A RUN'


def run_receipt():
    """returns (census arm verdict, overall failure count) read from the receipt's OWN output"""
    p = subprocess.run([sys.executable, RECEIPT], cwd=ROOT,
                       env=dict(os.environ, NODE='cc66'),
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=1800)
    txt = p.stdout.decode('utf-8', 'replace')
    arm = None
    for line in txt.splitlines():
        if MARK in line:
            arm = 'PASS' if '[PASS]' in line else ('FAIL' if '[FAIL]' in line else '?')
            break
    fails = None
    for line in txt.splitlines():
        if 'failure(s)' in line:
            try:
                fails = int(line.split('gates;')[1].split('failure')[0].strip())
            except Exception:
                pass
    return arm, fails, txt


def plant_one_rate(with_config, leafgeom=None, shift_ns=0.0):
    """a bank planted the way a real one would arrive -- through POLSAVE, which writes NO config"""
    os.makedirs(PLANT_DIR, exist_ok=True)
    z = np.load(ONE, allow_pickle=True)
    d = {k: z[k] for k in z.files}
    if shift_ns:
        d['ns'] = np.asarray(float(np.asarray(z['ns']).ravel()[0]) + shift_ns)
    if with_config:
        d['config'] = np.asarray(json.dumps({'ARM': 'cr', 'LEAFGEOM': bool(leafgeom),
                                             'LEAFREC': True, 'LMAXL': 2000.0}))
    np.savez(os.path.join(PLANT_DIR, 'planted_pol.npz'), **d)


def clear():
    shutil.rmtree(PLANT_DIR, ignore_errors=True)


def ordered_form_verdict():
    """69's ORDERED clause, implemented faithfully: 'on the one rate' read off `config` ALONE.

    Returns the number of banks it would flag.  This is the measurement of Ⓗ⑧: run against the same
    plant the converted clause reddens on.
    """
    import glob
    flagged = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'computations', '**', '*.npz'), recursive=True)):
        try:
            z = np.load(f, allow_pickle=True)
        except Exception:
            continue
        if not ('Dl_EE' in z.files or 'Dl_TE' in z.files):
            continue
        if 'config' not in z.files:
            continue                       # ⛔ exactly the blindness: no config, no verdict
        c = z['config']
        try:
            c = c.item()
        except Exception:
            pass
        try:
            d = json.loads(str(c))
        except Exception:
            continue
        if not d.get('LEAFGEOM'):
            continue
        # "on the one rate", read off config -- there is NO rate field, so this can never be decided
        if any(k in d for k in ('CRH0', 'CROM', 'NS', 'WBH2', 'H0', 'OM')):
            flagged.append(os.path.relpath(f, ROOT))
    return flagged


TRIALS = (
    ('⑴ the live tree, nothing planted', 'Ⓚ⑪', None, 'PASS'),
    ('⑵ a one-rate bank planted through POLSAVE, carrying NO config', 'Ⓙ⑩',
     dict(with_config=False), 'FAIL'),
    ('⑶ a bank planted on ANOTHER rate, declaring LEAFGEOM=1 in config', 'Ⓚ⑪',
     dict(with_config=True, leafgeom=True, shift_ns=0.01), 'PASS'),
    ('⑷ one of r7783\'s own four renamed away', 'Ⓛ⑫', 'rename', 'FAIL'),
)


def main():
    print(__doc__)
    print('=' * 100)
    clear()
    res = []
    moved = None
    try:
        for name, band, plant, want in TRIALS:
            clear()
            if plant == 'rename':
                src = os.path.join(FOUR_DIR, 'pol_cr_leafrec1.npz')
                moved = src + '.r7869_moved'
                os.rename(src, moved)
            elif isinstance(plant, dict):
                plant_one_rate(**plant)
            arm, fails, _ = run_receipt()
            if plant == 'rename' and moved and os.path.exists(moved):
                os.rename(moved, os.path.join(FOUR_DIR, 'pol_cr_leafrec1.npz'))
                moved = None
            hit = (arm == want)
            print('  %-66s %-6s want %-4s got %-4s  %s'
                  % (name, band, want, arm, 'as intended' if hit else '⛔ MISS'))
            res.append(dict(trial=name, band=band, want=want, got=arm, failures=fails, hit=hit))
    finally:
        clear()
        if moved and os.path.exists(moved):
            os.rename(moved, os.path.join(FOUR_DIR, 'pol_cr_leafrec1.npz'))

    # Ⓗ⑧ the ordered form, against the same plant the converted clause reddens on
    print('\n  Ⓗ⑧ 69\'s ORDERED config-keyed form, run against trial ⑵\'s plant:')
    try:
        plant_one_rate(with_config=False)
        flagged = ordered_form_verdict()
        print('      banks it can even decide "on the one rate" for: %d' % len(flagged))
        print('      ⇒ the planted one-rate bank carries no config, so the ordered form NEVER SEES '
              'IT: it stays GREEN on the exact case the arm must redden on.')
        ordered = dict(flagged=flagged, n_flagged=len(flagged), blind_to_the_plant=True)
    finally:
        clear()

    n_hit = sum(1 for r in res if r['hit'])
    print('\n  %d of %d trial(s) landed at the arm each was written for' % (n_hit, len(res)))
    io.open(OUT, 'w', encoding='utf-8').write(
        json.dumps(dict(trials=res, n_hit=n_hit, n_total=len(res), ordered_form=ordered),
                   indent=1, sort_keys=True))
    print('  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()

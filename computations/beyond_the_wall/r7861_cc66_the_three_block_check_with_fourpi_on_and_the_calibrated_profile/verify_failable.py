#!/usr/bin/env python3
r"""r7861+cc66.8 -- ** ARE THIS RECEIPT'S PINS FAILABLE?  PERTURB WHAT IT READS AND SEE. **

Seven perturbations, each applied IN PLACE to the record or the bank array the receipt actually
reads, each restored from a byte copy this script makes itself -- never from a version-control
checkout, which is the `r7855` defect where the committed copy predated a field the receipt read.
The baseline is run green BEFORE the first edit and AFTER the last restore, and every file's
sha256 is compared, because a loop that crashes prints no failures and looks like a receipt with no
failable pins.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), f'ROOT is wrong: {ROOT}'
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_with_fourpi_on_all_three_blocks_read_one_and_tes_correlation_is_four_nines'
                    '_where_its_ratio_is_unusable.py')
BK = os.path.join(HERE, '_bk')
T = {k: os.path.join(HERE, k) for k in ('compare_fourpi_vs_camb.json', 'rdrag_grid.json',
                                        'calibrated_profile.json')}
T['bank'] = os.path.join(HERE, 'bank_fourpi', 'lcdm_S000.npz')
T['pairs'] = os.path.join(HERE, 'pairs_fourpi', 'lcdm_S000_fourpi1.npz')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def run():
    p = subprocess.run([sys.executable, RCPT], cwd=ROOT, capture_output=True, text=True,
                       errors='replace')
    red = [ln.strip()[6:24] for ln in (p.stdout + p.stderr).splitlines()
           if ln.strip().startswith('FAIL  ')]
    return p.returncode, red


def jset(path, fn):
    d = json.load(open(path))
    fn(d)
    json.dump(d, open(path, 'w'), indent=1)


def nset(path, key, factor):
    z = dict(np.load(path, allow_pickle=True))
    z[key] = np.asarray(z[key], float) * factor
    np.savez(path, **z)


def main():
    os.makedirs(BK, exist_ok=True)
    before = {}
    for k, p in T.items():
        shutil.copy2(p, os.path.join(BK, k.replace('/', '_') + os.path.basename(p)))
        before[k] = sha(p)
    rc0, red0 = run()
    print(f"  baseline before any edit: rc={rc0}, {len(red0)} red")
    if rc0 != 0 or red0:
        print('  ⛔ REFUSED: the baseline is not green, so nothing below would mean anything.')
        return 2

    def restore(k):
        shutil.copy2(os.path.join(BK, k.replace('/', '_') + os.path.basename(T[k])), T[k])
        assert sha(T[k]) == before[k], f'{k} did not restore'

    res = {}

    def trial(name, k, mutate):
        mutate()
        rc, red = run()
        restore(k)
        res[name] = (rc, red)
        print(f"  {name:36s} rc={rc}  reddened {len(red)}: {red}")

    trial("TT's mean moved 0.01", 'compare_fourpi_vs_camb.json',
          lambda: jset(T['compare_fourpi_vs_camb.json'],
                       lambda d: d['blocks'].__setitem__(
                           0, {**d['blocks'][0], 'abs_mean': d['blocks'][0]['abs_mean'] + 0.01})))
    trial("TE's correlation made to move", 'compare_fourpi_vs_camb.json',
          lambda: jset(T['compare_fourpi_vs_camb.json'],
                       lambda d: d['te_correlation'].__setitem__('abs_difference', 1e-6)))
    trial("the ruler's range halved", 'rdrag_grid.json',
          lambda: jset(T['rdrag_grid.json'],
                       lambda d: d['ends'].__setitem__('range_mpc', 1.2)))
    trial("rdrag at the control moved", 'rdrag_grid.json',
          lambda: jset(T['rdrag_grid.json'],
                       lambda d: d['rdrag']['lcdm control'].__setitem__('rdrag', 147.4)))
    trial("the calibrated ruler unpinned", 'calibrated_profile.json',
          lambda: jset(T['calibrated_profile.json'],
                       lambda d: d['profile']['rd_camb'][0].__setitem__('rd_used', 1.0)))
    trial("the bank point scaled 1.5 not 2", 'bank', lambda: nset(T['bank'], 'Dl', 0.75))
    trial("the pairs' closure broken", 'pairs', lambda: nset(T['pairs'], 'Dl_pairs', 1.01))

    rc1, red1 = run()
    print(f"  baseline re-read after every restore: rc={rc1}, {len(red1)} red")
    ok = (rc1 == 0 and not red1 and all(sha(p) == before[k] for k, p in T.items())
          and all(v[0] != 0 and v[1] for v in res.values()))
    json.dump({n: dict(rc=v[0], reddened=v[1]) for n, v in res.items()},
              open(os.path.join(HERE, 'verify_failable.json'), 'w'), indent=1)
    shutil.rmtree(BK)
    print(f"\n  ⇒ {sum(1 for v in res.values() if v[1])} of {len(res)} perturbations reddened the "
          f"receipt, every file restored byte-for-byte, baseline green before and after: "
          f"{'OK' if ok else '⛔ NOT OK'}")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())

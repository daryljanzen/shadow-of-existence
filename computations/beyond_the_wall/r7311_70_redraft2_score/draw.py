#!/usr/bin/env python3
"""r7311+70: draw the held set for 69's SECOND redraft (r7303's draw.py, with the first held set added to the exclusions), as PREDICTION.md fixes it -- printing no verdict.

    python3 draw.py SALT        # SALT = the full sha of the commit that landed the redraft

Eligible: ledger keys (at SALT) verdicted REPAIR-OWED, DELIBERATE, MEANING-HELD or ENCODING-OK, excluding every key of
any batch the pooler globs (pooled or pending), the 47 of r7299_70_two_scores/KEYS_BLIND.tsv and the 21 calibration
keys.  Sorted by sha256("SALT|receipt|literal") with the literal JSON-decoded; the first 69 are taken.  Writes
KEYS_BLIND.tsv (receipt, literal) beside this file."""
import glob
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()
ELIGIBLE = {'REPAIR-OWED', 'DELIBERATE', 'MEANING-HELD', 'ENCODING-OK'}
N = 69


def keys_of(path):
    out = set()
    for ln in open(path, encoding='utf-8'):
        c = ln.rstrip('\n').split('\t')
        if ln.startswith('#') or len(c) < 2 or not ln.strip():
            continue
        try:
            out.add((c[0].strip(), json.loads(c[1])))
        except ValueError:
            pass
    return out


def main():
    salt = sys.argv[1]
    led = subprocess.run(['git', '-C', ROOT, 'show', f'{salt}:corpus/quote_pin_baseline.tsv'], capture_output=True,
                         text=True, check=True).stdout
    elig = set()
    for ln in led.split('\n'):
        c = ln.split('\t')
        if len(c) >= 6 and not ln.startswith('#') and c[5].strip() in ELIGIBLE:
            elig.add((c[0], json.loads(c[1])))
    excl = set()
    for pat in ('DOUBLE_READ*.tsv', 'BLIND_READ*.tsv'):
        for p in glob.glob(os.path.join(ROOT, 'computations', '**', pat), recursive=True):
            excl |= keys_of(p)
    excl |= keys_of(os.path.join(ROOT, 'computations/beyond_the_wall/r7299_70_two_scores/KEYS_BLIND.tsv'))
    excl |= keys_of(os.path.join(ROOT, 'computations/beyond_the_wall/r7297_70_convergence_score/CALIBRATION_21.tsv'))
    excl |= keys_of(os.path.join(ROOT, 'computations/beyond_the_wall/r7303_70_redraft_score/KEYS_BLIND.tsv'))   # the first held set
    pool = elig - excl
    h = lambda k: hashlib.sha256(f'{salt}|{k[0]}|{k[1]}'.encode()).hexdigest()
    take = sorted(pool, key=h)[:N]
    with open(os.path.join(HERE, 'KEYS_BLIND.tsv'), 'w', encoding='utf-8') as f:
        f.write(f'# r7311+70: the held set for 69\'s second redraft, drawn by draw.py with salt {salt} (the redraft\'s commit).\n')
        f.write(f'# {len(elig)} eligible, {len(excl & elig)} excluded, {len(pool)} in the pool, first {N} by hash.  No verdict column.\n')
        f.write('# receipt\tliteral\n')
        for k in take:
            f.write(f'{k[0]}\t{json.dumps(k[1], ensure_ascii=False)}\n')
    print(f'  {len(elig)} eligible, {len(excl & elig)} excluded, pool {len(pool)}, drew {len(take)} '
          f'over {len({k[0] for k in take})} receipts')


if __name__ == '__main__':
    main()

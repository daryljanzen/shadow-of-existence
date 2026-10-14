#!/usr/bin/env python3
"""r7315+70: draw the held set and the crossover keys for 69's THIRD redraft, as r7311_70_redraft2_score/PREDICTION.md and
r7315_70_widens_reregistered/PREDICTION.md fix them -- printing no verdict.

    python3 draw.py SALT        # SALT = the full sha of the commit that landed the redraft

The pool is r7311's (ledger keys at SALT verdicted REPAIR-OWED, DELIBERATE, MEANING-HELD or ENCODING-OK, less every
batch the pooler globs, the 47, the 21 calibration keys), less BOTH earlier held sets.  KEYS_BLIND.tsv: the first 69 by
sha256("SALT|receipt|literal").  CROSSOVER_KEYS_BLIND.tsv: from what is left, the first 40 by
sha256("SALT|crossover|receipt|literal").  Disjoint by construction."""
import glob
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()
sys.path.insert(0, os.path.join(HERE, '..', 'r7311_70_redraft2_score'))
from draw import keys_of, ELIGIBLE  # noqa: E402

N, NX = 69, 40
BW = os.path.join(ROOT, 'computations/beyond_the_wall')


def write(path, head, take):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(head)
        f.write('# receipt\tliteral\n')
        for k in take:
            f.write(f'{k[0]}\t{json.dumps(k[1], ensure_ascii=False)}\n')


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
    for rel in ('r7299_70_two_scores/KEYS_BLIND.tsv', 'r7297_70_convergence_score/CALIBRATION_21.tsv',
                'r7303_70_redraft_score/KEYS_BLIND.tsv', 'r7311_70_redraft2_score/KEYS_BLIND.tsv'):
        excl |= keys_of(os.path.join(BW, rel))
    pool = elig - excl
    take = sorted(pool, key=lambda k: hashlib.sha256(f'{salt}|{k[0]}|{k[1]}'.encode()).hexdigest())[:N]
    rest = pool - set(take)
    cross = sorted(rest, key=lambda k: hashlib.sha256(f'{salt}|crossover|{k[0]}|{k[1]}'.encode()).hexdigest())[:NX]
    assert not set(take) & set(cross)
    stats = f'# {len(elig)} eligible, {len(excl & elig)} excluded, {len(pool)} in the pool.  No verdict column.\n'
    write(os.path.join(HERE, 'KEYS_BLIND.tsv'),
          f'# r7315+70: the held set for 69\'s third redraft, drawn by draw.py with salt {salt} (the redraft\'s commit), '
          f'first {N} by hash.\n' + stats, take)
    write(os.path.join(HERE, 'CROSSOVER_KEYS_BLIND.tsv'),
          f'# r7315+70: the crossover keys, to be applied under the PREVIOUS text (6bef6fd5) FIRST, salt {salt}|crossover, '
          f'first {NX} of the pool less the held set.\n' + stats, cross)
    print(f'  {len(elig)} eligible, {len(excl & elig)} excluded, pool {len(pool)}; held {len(take)} over '
          f'{len({k[0] for k in take})} receipts; crossover {len(cross)} over {len({k[0] for k in cross})} receipts')


if __name__ == '__main__':
    main()

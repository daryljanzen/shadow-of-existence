#!/usr/bin/env python3
"""The draw and the hash split, deterministic and auditable.

The frame is every DISTINCT KEY this seat read in the pooled cells at
`computations/beyond_the_wall/r7299_66_the_fourth_conflict/CELLS_pooled.tsv` -- 78 of them, from
122 cells.  All 78 are taken, for the reason registered in PREREGISTRATION.md §1.

The split is by SHA-256 of `<salt>\\x00<receipt>\\x00<literal>`, salt = the text's own commit
`1a3c13a6`, assigned by the low bit.  Nothing about the key's content or this seat's verdict
enters the assignment, and re-running reproduces it exactly.
"""
import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CELLS = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7299_66_the_fourth_conflict',
                     'CELLS_pooled.tsv')
SALT = '1a3c13a6'          # the text both halves are read against
HERE = os.path.dirname(os.path.abspath(__file__))


def frame():
    """Every distinct key this seat read, with the verdict it gave -- held back from the readers."""
    seen = {}
    for ln in open(CELLS, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        f = ln.rstrip('\n').split('\t')
        if len(f) < 6:
            continue
        pair = f[2].split('|')
        if 'cc66' not in pair:
            continue
        key = (f[0], json.loads(f[1]))
        seen.setdefault(key, f[3 + pair.index('cc66')])
    return seen


def half_of(receipt, literal):
    h = hashlib.sha256(f'{SALT}\x00{receipt}\x00{literal}'.encode()).digest()
    return 'A' if h[0] & 1 == 0 else 'B'


def main():
    seen = frame()
    keys = sorted(seen)
    print(f'  frame: {len(keys)} distinct keys from the pooled cells (this seat as a reader)')
    halves = {'A': [], 'B': []}
    for r, l in keys:
        halves[half_of(r, l)].append((r, l))
    for h in ('A', 'B'):
        print(f'    half {h}: {len(halves[h])} keys')
        out = os.path.join(HERE, f'KEYS_half_{h}.tsv')
        with open(out, 'w', encoding='utf-8') as fh:
            fh.write(f'# half {h} of this seat\'s within-seat spread frame, r7321+cc66.\n')
            fh.write(f'# Read against THE_RULE.md at {SALT} and NOTHING ELSE.\n')
            fh.write('# receipt and literal ONLY -- no verdict here and the baseline is withheld,\n')
            fh.write('# because its reason field carries this seat\'s verdict and its reasoning.\n')
            fh.write('# columns: receipt, literal\n')
            for r, l in halves[h]:
                fh.write(f'{r}\t{json.dumps(l)}\n')
        print(f'      -> {os.path.relpath(out, ROOT)}')

    # The held-back answers, written so the scoring can run later without re-deriving them.
    out = os.path.join(HERE, 'HELD_BACK_cc66_verdicts.tsv')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('# THIS SEAT\'S OWN verdicts on the frame. NOT GIVEN TO EITHER READER.\n')
        fh.write('# Kept so the spread can be scored against this seat\'s recorded reading later.\n')
        fh.write('# columns: half, receipt, literal, cc66 verdict\n')
        for r, l in keys:
            fh.write(f'{half_of(r, l)}\t{r}\t{json.dumps(l)}\t{seen[(r, l)]}\n')
    print(f'    held back: {os.path.relpath(out, ROOT)}')

    if len(keys) != 78:
        print(f'  FAILED: frame is {len(keys)} keys, registered as 78')
        return 1
    if abs(len(halves['A']) - len(halves['B'])) > 8:
        print(f'  FAILED: halves badly unbalanced: {len(halves["A"])} / {len(halves["B"])}')
        return 1
    print()
    print('  The two halves are the read lists.  Each goes to ONE fresh reader that has not')
    print('  opened the baseline, and the two reads are never pooled.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

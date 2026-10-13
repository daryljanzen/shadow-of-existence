#!/usr/bin/env python3
"""r7295+70: build the four-column BLIND_READ batch from 70's blind verdicts (VERDICTS_70_blind.tsv, committed first)
and the first reader's verdicts as they stand in the ledger at REV -- and refuse while any of them is still open.

    python3 join.py [REV]     # REV defaults to origin/main; writes BLIND_READ_L262_70.tsv only when every key is landed

No verdict is adjusted in either direction: the join copies two strings per key and nothing else."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()
OPEN = {'UNADJUDICATED', 'UNADJUDICATED-PINNED', ''}


def main():
    rev = sys.argv[1] if len(sys.argv) > 1 else 'origin/main'
    mine = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'VERDICTS_70_blind.tsv'), encoding='utf-8')
            if l.strip() and not l.startswith('#')]
    led = subprocess.run(['git', '-C', ROOT, 'show', f'{rev}:corpus/quote_pin_baseline.tsv'], capture_output=True,
                         text=True, check=True).stdout
    first = {}
    for l in led.split('\n'):
        c = l.split('\t')
        if len(c) >= 6 and not l.startswith('#'):
            first[(c[0], json.loads(c[1]))] = c[5].strip()
    rows, waiting = [], []
    for r, lit, v, _ in mine:
        f = first.get((r, json.loads(lit)), '')
        (waiting if f in OPEN else rows).append((r, lit, f, v))
    if waiting:
        print(f'  waiting: {len(waiting)} of {len(mine)} key(s) still open in the ledger at {rev} -- nothing written')
        return 1
    out = os.path.join(HERE, 'BLIND_READ_L262_70.tsv')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(f'# blind read of L262_half_a_family -- first reader 69 (ledger at {rev}), second reader 70 (blind, r7295+70.2)\n')
        for r in rows:
            fh.write('\t'.join(r) + '\n')
    print(f'  written: {os.path.relpath(out, ROOT)} ({len(rows)} keys, {sum(a == b for *_, a, b in rows)} agree)')
    return 0


if __name__ == '__main__':
    sys.exit(main())

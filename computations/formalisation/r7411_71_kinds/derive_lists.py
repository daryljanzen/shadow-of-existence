#!/usr/bin/env python3
"""derive_lists.py -- r7411+71 (r7411's rule: a copied list is a claim; this one is derived).

THE SELECTOR, committed with the measurement (cc66): from r7325_71_inventory/ROWS.tsv at HEAD, every row whose status
is exactly `NO-CONNECTION, NOT DONE` (the 32) or `REAL OBSTRUCTION` (the 4); each joined by index to its receipt path
in r7285_71_restate/READINGS.tsv. Prints one line per row: status, index, class, path, stand-in. Nothing else.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
rows = [l.split('\t') for l in open(os.path.join(ROOT, 'r7325_71_inventory', 'ROWS.tsv'), encoding='utf-8').read().split('\n')[1:]]
paths = {l.split('\t')[0]: l.split('\t')[1] for l in open(os.path.join(ROOT, 'r7285_71_restate', 'READINGS.tsv'), encoding='utf-8').read().split('\n')[1:] if '\t' in l}
for want in ('NO-CONNECTION, NOT DONE', 'REAL OBSTRUCTION'):
    sel = [r for r in rows if len(r) >= 5 and r[2] == want]
    print(f'## {want}: {len(sel)}')
    for r in sel:
        print('\t'.join([r[0], r[1], paths.get(r[0], 'NO PATH'), r[4]]))

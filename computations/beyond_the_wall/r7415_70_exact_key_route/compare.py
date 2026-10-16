#!/usr/bin/env python3
"""r7415+70 ④ K-a: the new route against the old, row by row, within each target in ledger order."""
import sys
from collections import defaultdict
D = sys.argv[1]


def load(paths):
    by = defaultdict(list)
    for p in paths:
        for ln in open(p, encoding='utf-8'):
            if ln.startswith('#'):
                continue
            i, tg, v, rc, lit = ln.rstrip('\n').split('\t', 4)
            by[tg].append((rc, lit, int(v)))
    return by


old = load([f'{D}/OLD_PAPER.tsv', f'{D}/OLD_SOURCE.tsv'])
new = load([f'{D}/NEW_ALL.tsv'])
tot = diff = 0
for tg in sorted(old):
    o, n = old[tg], new[tg]
    k = len(o)
    assert [x[:2] for x in o] == [x[:2] for x in n[:k]], f'{tg}: row keys out of step'
    d = [(a, b) for a, b in zip(o, n[:k]) if a[2] != b[2]]
    tot += k; diff += len(d)
    print(f'{tg:7} compared {k} of {len(n)}: {len(d)} differ; absent old {sum(1 for x in o if not x[2])}, '
          f'absent new {sum(1 for x in n[:k] if not x[2])}')
    for a, b in d:
        print(f'   DIFF old={a[2]} new={b[2]} {a[0]}  {a[1][:90]}')
print(f'K-a: {diff} of {tot} compared rows differ')

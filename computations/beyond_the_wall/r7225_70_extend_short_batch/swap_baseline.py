#!/usr/bin/env python3
"""Swap the baseline rows for the ledger's accepted keys, all at once, and check the counts against PREDICTION.md's
advance statement: UNADJUDICATED falls by N_U, EXTENDED rises by N, PINNED/LIST/MULTI unchanged, total unchanged."""
import collections, json, os, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import mutate_assertions as M
BL = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')
norm = lambda s: ' '.join(s.split())

ledger = json.load(open(os.path.join(HERE, 'ledger.json')))
ok = [x for x in ledger if x['outcome'] == 'OK']
lines = open(BL, encoding='utf-8').read().split('\n')
idx = {}
for i, ln in enumerate(lines):
    if ln.strip() and not ln.startswith('#'):
        f = ln.split('\t'); idx[(f[0], json.loads(f[1]))] = i
before = collections.Counter(lines[i].split('\t')[5] for i in idx.values())
live = {}
for rec in {x['receipt'] for x in ok}:
    for r in M.quote(ROOT, [os.path.join(ROOT, rec)]):
        live.setdefault((r['receipt'], r['lit']), r)
drop, add, NU = set(), [], 0
for x in ok:
    old = (x['receipt'], norm(x['lit'])); new = (x['receipt'], norm(x['new']))
    i = idx[old]; f = lines[i].split('\t'); NU += f[5] == 'UNADJUDICATED'
    r = live[new]
    drop.add(i)
    add.append('\t'.join([new[0], json.dumps(new[1], ensure_ascii=False), r['target'], r['tier'], r['flags'], 'EXTENDED',
                          f"r7225+70.1: extended from {json.dumps(old[1], ensure_ascii=False)} by D={x['D']} so every "
                          f"declared reversal of its clause breaks it; prior verdict {f[5]}"]))
out = [ln for i, ln in enumerate(lines) if i not in drop]
while out and out[-1] == '':
    out.pop()
out.append("# ⛭ r7225+70.1 (66's r7225 order): the EXTEND-SHORT batch -- each key below replaced a REVERSAL key by its "
           "minimal verbatim extension, the receipt edited at the same site and run green.  Verdict EXTENDED; the "
           "prior verdict is in the last column.")
out += add
open(BL, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
after = collections.Counter(ln.split('\t')[5] for ln in out if ln.strip() and not ln.startswith('#'))
N = len(ok)
print(f'  N = {N} accepted, N_U = {NU} of them UNADJUDICATED')
print('  before:', dict(before)); print('  after: ', dict(after))
assert sum(before.values()) == sum(after.values()), 'total key count moved'
assert after['UNADJUDICATED'] == before['UNADJUDICATED'] - NU
assert after['EXTENDED'] == before.get('EXTENDED', 0) + N
for v in ('UNADJUDICATED-PINNED', 'UNADJUDICATED-LIST'):
    assert after[v] == before[v], v
print('  counts reconcile with the advance statement')

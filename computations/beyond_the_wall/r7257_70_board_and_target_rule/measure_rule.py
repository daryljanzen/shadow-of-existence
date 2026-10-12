#!/usr/bin/env python3
"""r7257+70.1: R* against the baseline's hand-corrected target column and against the current rule, over every live
key.  A key's kinds are the union over its sites of the file kinds its WIDE trace names."""
import collections, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import mutate_assertions as M
rows = M.quote(ROOT)
kinds, cur = collections.defaultdict(set), collections.defaultdict(set)
for r in rows:
    k = (r['receipt'], r['lit']); kinds[k] |= set(r['_kinds']); cur[k].add(r['target'])
base = {}
for l in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8'):
    q = l.rstrip('\n').split('\t')
    if len(q) == 7 and not l.startswith('#'):
        base[(q[0], ' '.join(json.loads(q[1]).split()))] = q[2]
def rstar(ks):
    if ks == {'tex'}: return 'PAPER'
    if 'tex' not in ks: return 'SOURCE'
    return 'UNDECIDED'
c = collections.Counter(); out = []
for k in kinds:
    b = base.get(k); r = rstar(kinds[k]); now = 'PAPER' if 'PAPER' in cur[k] else 'SOURCE'
    c['live'] += 1; c['in_baseline'] += b is not None
    c['R*=' + r] += 1
    if b and r != 'UNDECIDED' and r != b: c[f'R* {r} vs baseline {b}'] += 1; out.append((k[0], k[1], b, r, ','.join(sorted(kinds[k]))))
    if b and now != b: c[f'current {now} vs baseline {b}'] += 1
    if r == 'UNDECIDED': c['UNDECIDED, baseline ' + str(b)] += 1
for k_, v in sorted(c.items()): print(f'  {k_:45s} {v}')
with open(os.path.join(os.path.dirname(__file__), 'disagreements.tsv'), 'w') as f:
    f.write('# receipt\tliteral\tbaseline\tR*\tkinds\n')
    for x in sorted(out): f.write('\t'.join(x) + '\n')

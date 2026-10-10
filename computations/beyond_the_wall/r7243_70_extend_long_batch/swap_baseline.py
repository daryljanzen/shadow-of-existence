#!/usr/bin/env python3
"""r7243+70.1 -- swap the baseline rows for the ledger's accepted keys, once, and check the counts against
PREDICTION.md: each prior verdict falls by its own N_v, EXTENDED rises by N - K, PINNED and MULTI do not move, and the
total falls by exactly K.  K counts CONVERGENCE (r7227's E2 lesson): an accepted key whose new literal is already a key
in its receipt -- another accepted key's, or a row the baseline already holds -- becomes ONE row recording both."""
import collections, json, os, sys
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
rows = lambda ls: [ln for ln in ls if ln.strip() and not ln.startswith('#')]
before = collections.Counter(ln.split('\t')[5] for ln in rows(lines))
multi_before = sum('MULTI' in ln.split('\t')[4] for ln in rows(lines))
live = {}
for rec in {x['receipt'] for x in ok}:
    for r in M.quote(ROOT, [os.path.join(ROOT, rec)]):
        live.setdefault((r['receipt'], r['lit']), r)
drop, new_rows, prior = set(), {}, collections.Counter()
K, notes = 0, []
for x in ok:
    old = (x['receipt'], norm(x['lit'])); new = (x['receipt'], norm(x['new']))
    i = idx[old]; f = lines[i].split('\t'); prior[f[5]] += 1
    drop.add(i)
    why = f"extended from {json.dumps(old[1], ensure_ascii=False)} by D={x['D']} (prior verdict {f[5]})"
    if new in new_rows:
        K += 1; new_rows[new][1].append(why); notes.append(('two accepted keys', new))
    elif new in idx and idx[new] not in drop:
        K += 1; j = idx[new]; g = lines[j].split('\t')
        g[6] = g[6] + f'; r7243+70.1 CONVERGED: {why}'; lines[j] = '\t'.join(g); notes.append(('an existing row', new))
    else:
        new_rows[new] = (live[new], [why])
out = [ln for i, ln in enumerate(lines) if i not in drop]
while out and out[-1] == '':
    out.pop()
out.append("# ⛭ r7243+70.1 (66's r7243 order): the EXTEND-LONG batch -- each key below replaced a REVERSAL key by its "
           "minimal verbatim extension (26 <= D <= 100), the receipt edited at the same site and run green, and every "
           "declared reversal checked to break the extension before the edit.  Verdict EXTENDED; prior verdict last.")
for (rec, lit), (r, whys) in new_rows.items():
    tag = 'r7243+70.1: ' + ('; CONVERGED -- '.join(whys)) + ' -- so every declared reversal of its clause breaks it'
    out.append('\t'.join([rec, json.dumps(lit, ensure_ascii=False), r['target'], r['tier'], r['flags'], 'EXTENDED', tag]))
open(BL, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
after = collections.Counter(ln.split('\t')[5] for ln in rows(out))
multi_after = sum('MULTI' in ln.split('\t')[4] for ln in rows(out))
N = len(ok)
print(f'  N = {N} accepted; by prior verdict {dict(prior)}; converged K = {K} {notes}')
print('  before:', dict(before)); print('  after: ', dict(after)); print(f'  MULTI {multi_before} -> {multi_after}')
assert sum(after.values()) == sum(before.values()) - K, 'total key count moved by other than K'
for v, n in prior.items():
    if v != 'EXTENDED':
        assert after[v] == before[v] - n, v
assert after['EXTENDED'] == before['EXTENDED'] + N - K - prior.get('EXTENDED', 0)
assert after['UNADJUDICATED-PINNED'] == before['UNADJUDICATED-PINNED']
print('  counts reconcile with the advance statement' + ('' if multi_after == multi_before else '  (MULTI MOVED -- reported)'))

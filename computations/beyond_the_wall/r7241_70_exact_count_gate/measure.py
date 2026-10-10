"""r7241+70.1 -- the lifted detector over every receipt in the working tree: claim-sites by partition, every
EXPOSED site listed, and the standing 29 in S3/S4/S6 read on their own."""
import os, sys, collections, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_exact_counts as E
found, totals = E.sweep()
pop = E.population()
print('receipts', len(pop), ' claim-sites by partition', dict(sorted(totals.items())), ' total', sum(totals.values()))
exp = {k: v for k, v in found.items() if v[0] == 'EXPOSED'}
print('distinct EXPOSED keys', len(exp))
in60 = lambda r: r.startswith('receipts/P15_CR_cosmology/') or r.startswith('receipts/L_probability/S')
print('EXPOSED in 60\'s two directories', sum(1 for r, _ in exp if in60(r)), ' outside', sum(1 for r, _ in exp if not in60(r)))
s346 = [p for p in pop if os.path.basename(p)[:3] in ('S3_', 'S4_', 'S6_') and '/L_probability/' in p]
c = collections.Counter(); n = 0
for rel in s346:
    for seg, part, line in E.sites_of(open(os.path.join(ROOT, rel), encoding='utf-8').read()):
        c[part] += 1; n += 1
print('S3/S4/S6 claim-sites', n, dict(c))
json.dump(sorted([[r, s, p, l] for (r, s), (p, l) in exp.items()]), open(os.path.join(os.path.dirname(__file__), 'exposed.json'), 'w'), indent=0, ensure_ascii=False)
for (r, s), (p, l) in sorted(exp.items()):
    print(f'  {r[9:70]:62s} L{l:<5d} {s[:70]}')

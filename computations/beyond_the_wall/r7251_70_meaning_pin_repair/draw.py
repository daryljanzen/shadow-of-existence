#!/usr/bin/env python3
"""r7251+70.2: the seeded draw pre-registered in PREDICTION.md -- 3 of 60's 162 PAPER/SENTENCE REPAIR-OWED keys."""
import json, os, random, statistics
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8')
        if not l.startswith('#')]
pop = sorted((r[0], r[1]) for r in rows if len(r) == 7 and '/L221_the_bridge/' in r[0] and r[5] == 'REPAIR-OWED'
             and r[6].startswith('r7252 (60)') and r[2] == 'PAPER' and r[3] == 'SENTENCE')
assert len(pop) == 162, len(pop)
rng = random.Random(0x3bf0ac52)
picks = rng.sample(pop, 3)
words = sorted(len(json.loads(l).split()) for _, l in pop)
q = statistics.quantiles(words, n=4)
quart = lambda w: sum(w > x for x in q) + 1
share = {}
for f, _ in pop: share[f] = share.get(f, 0) + 1
print(f'population 162; literal word-count quartile cuts {q}')
qs = []
for f, l in picks:
    w = len(json.loads(l).split()); qs.append(quart(w))
    print(f'  {os.path.basename(f)[:70]}\n    {l}\n    {w} words (Q{quart(w)}); its receipt holds {share[f]} of the 162')
if len(set(qs)) == 1:
    extra = rng.sample([p for p in pop if p not in picks], 1)[0]
    print('  ALL THREE IN ONE QUARTILE -- fourth draw:', extra)

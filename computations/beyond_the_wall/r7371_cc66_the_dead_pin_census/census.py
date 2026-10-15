#!/usr/bin/env python3
"""r7371+cc66 ③ -- THE DEAD-PIN CENSUS over the whole live key set, priced.

`r7371` ③: *"a key whose literal is absent from what it reads while its receipt is GREEN is a dead
pin.  `_present_at` already computes the first half, and the green-receipt set is the second."*

⛔ THE BAND IS REGISTERED IN `REGISTRATION.md`, PUSHED BEFORE THIS RAN: central `8`, band `1`-`40`,
refuted by `0` or by `> 40`, with the informative half being WHICH verdicts the hits carry.  The
binding faithfulness check is also there and has a known answer: with the `r7367` mint ON this must
flag `S17`'s `'already the product of a repair'`.

⛭ EVERY FIELD COMES FROM THE INSTRUMENT THAT OWNS IT -- `r7367` ④'s remedy, third use.  The key,
target and verdict are read from `corpus/quote_pin_baseline.tsv` the way the GATE keys it (the
literal column is JSON, never raw text: keying it raw reports 2628 stale on an exactly-green ledger,
which is `r7365+cc66.38` ⒢'s recorded error).  `H3` is `check_quote_pins`' own `_present_at`, called
and not reimplemented.

    python3 -I census.py [--limit N] [--target PAPER|SOURCE]
"""
import argparse, importlib.util, json, os, sys, time

AP = argparse.ArgumentParser()
AP.add_argument('--limit', type=int, default=0, help='first N rows only, for pricing a sample')
AP.add_argument('--target', default='', help='restrict to one target, to price the two halves apart')
A = AP.parse_args()

spec = importlib.util.spec_from_file_location('g', 'corpus/check_quote_pins.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

rows = []
for ln in open('corpus/quote_pin_baseline.tsv', encoding='utf-8').read().split('\n'):
    if '\t' not in ln or ln.startswith('#'):
        continue
    c = ln.split('\t')
    if len(c) < 6:
        continue
    try:
        lit = json.loads(c[1])
    except ValueError:
        continue
    rows.append((c[0], lit, c[2], c[3], c[5]))      # receipt, lit, target, tier, verdict

if A.target:
    rows = [r for r in rows if r[2] == A.target]
if A.limit:
    rows = rows[:A.limit]

head = g._git('rev-parse', 'HEAD').stdout.strip()
print(f'# census over {len(rows)} live row(s) at {head[:12]}'
      + (f', target={A.target}' if A.target else '') + (f', limit={A.limit}' if A.limit else ''))

t0 = time.time()
dead, per = [], {}
for i, (receipt, lit, target, tier, verdict) in enumerate(rows, 1):
    t = time.time()
    present = g._present_at(head, lit, target, receipt)
    per.setdefault(target, []).append(time.time() - t)
    if not present:
        dead.append((receipt, lit, target, tier, verdict))
    if i % 200 == 0:
        print(f'#   {i}/{len(rows)} in {time.time() - t0:7.1f}s, {len(dead)} absent so far',
              file=sys.stderr, flush=True)
wall = time.time() - t0

print(f'# WALL {wall:.1f}s on this container for {len(rows)} row(s) '
      f'= {wall / max(1, len(rows)):.3f}s a row')
for tg, xs in sorted(per.items()):
    print(f'#   {tg:7} {len(xs):5d} row(s)  {sum(xs):8.1f}s  mean {sum(xs)/len(xs):.4f}s')
print(f'# ABSENT FROM WHAT THE KEY READS: {len(dead)}')
from collections import Counter
print('# by verdict :', dict(Counter(d[4] for d in dead)))
print('# by target  :', dict(Counter(d[2] for d in dead)))
print('# ⌗ ABSENT is the first half only.  A receipt that is RED is excluded by r7371 ③ -- the green')
print('#   half is a separate list and is NOT applied here; these rows are candidates, not verdicts.')
for d in sorted(dead):
    print('\t'.join((d[0], json.dumps(d[1], ensure_ascii=False), d[2], d[3], d[4])))

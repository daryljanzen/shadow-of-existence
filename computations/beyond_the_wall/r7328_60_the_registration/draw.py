#!/usr/bin/env python3
r"""draw.py -- the r7328 draw, exactly as PREDICTION.md ③ and ④ registered it before this ran.

A receipt ROTATION over the 128 keys r7320 left: within each receipt its keys in hash order, the
receipts themselves in hash order, then one key from each receipt in turn, round and round, until 80
are taken.  The rotation is what buys the design effect of 1.566 priced in ②; the first 80 by hash
alone would have drawn in proportion to receipt size, which is the concentrated draw r7320 made.

The first 52 of the drawn order are the reader arm (④), a subset and not an addition.

No key is READ here and there is no verdict column: the re-read is a later revision, and r7321
forbids reading one this cycle.
"""
import collections
import hashlib
import io
import json
import os
import re
import sys

SALT = '1a3c13a61759c6cea88ac5f3a11182254a012e57'   # the third redraft's own commit
PREV_SALT = '6bef6fd5acf0692299f306c96e2ee630542dac14'  # r7320's, to reproduce the 40 it read
SIZE = 80
READER = 52
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))


def seat(w):
    for s in ('+60', '+69', '+70', 'cc66', '+66', '+71'):
        if s in (w or ''):
            return s.lstrip('+')
    return '?'


def rev(w):
    m = re.match(r'r(\d{4})', w or '')
    return int(m.group(1)) if m else None


def h(*parts):
    return hashlib.sha256(''.join(parts).encode('utf-8')).hexdigest()


rows = []
for l in io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if len(c) >= 7 and c[0].startswith('receipts/'):
        rows.append(c)

pop = [c for c in rows
       if c[5] == 'DELIBERATE' and seat(c[6]) == '60' and (rev(c[6]) or 99999) < 7260]
assert len(pop) == 168, f'the registered frame was 168, this tree has {len(pop)}'

read40 = {(c[0], c[1]) for c in
          sorted(pop, key=lambda c: h(PREV_SALT, c[0], '\t', c[1]))[:40]}
rest = [c for c in pop if (c[0], c[1]) not in read40]
assert len(rest) == 128, f'the registered population was 128, this tree has {len(rest)}'

by_receipt = collections.defaultdict(list)
for c in rest:
    by_receipt[c[0]].append(c)
for r in by_receipt:
    by_receipt[r].sort(key=lambda c: h(SALT, c[0], '\t', c[1]))
order = sorted(by_receipt, key=lambda r: h(SALT, r))
assert len(order) == 29, f'the registered population lay in 29 receipts, this tree has {len(order)}'

drawn, cursor = [], {r: 0 for r in order}
while len(drawn) < SIZE:
    took = False
    for r in order:
        if len(drawn) == SIZE:
            break
        if cursor[r] < len(by_receipt[r]):
            drawn.append(by_receipt[r][cursor[r]])
            cursor[r] += 1
            took = True
    if not took:
        break
assert len(drawn) == SIZE, f'the rotation took {len(drawn)} of {SIZE}'

out = io.open(os.path.join(HERE, 'SAMPLE_80.tsv'), 'w', encoding='utf-8')
out.write(f'# r7328 the draw: a receipt ROTATION over the 128 keys r7320 left, SALT={SALT}\n')
out.write('# The population, the size, the rotation and both bands were registered in '
          'PREDICTION.md before this ran.\n')
out.write(f'# arm: the first {READER} rows are the READER arm as well (both reads), a subset of the '
          'sampling arm.  No verdict column: no key is read this revision.\n')
out.write('# n\treceipt\tliteral\ttarget\ttier\tverdicted_at\tarm\n')
for i, c in enumerate(drawn, 1):
    at = re.match(r'r\d{4}', c[6])
    out.write('\t'.join([str(i), c[0], c[1], c[2], c[3], at.group(0) if at else '?',
                         'both' if i <= READER else 'sampling']) + '\n')
out.close()

alloc = collections.Counter(c[0] for c in drawn)
n, k = len(drawn), len(alloc)
m0 = (n - sum(v * v for v in alloc.values()) / n) / (k - 1)
print(f'population {len(rest)} in {len(order)} receipts;  drawn {n} over {k} receipts')
print(f'  allocation {dict(sorted(collections.Counter(alloc.values()).items()))} '
      '(keys per receipt: how many receipts)')
print(f'  m0 {m0:.2f}   deff {1 + (m0 - 1) * 0.327:.3f}   (registered: m0 2.73, deff 1.566)')
print(f'  reader arm: the first {READER}, over '
      f'{len(set(c[0] for c in drawn[:READER]))} receipts')
print(f'  tier   {({t: sum(1 for c in drawn if c[3] == t) for t in sorted({c[3] for c in drawn})})}')
print(f'  target {({t: sum(1 for c in drawn if c[2] == t) for t in sorted({c[2] for c in drawn})})}')
print(f'  prefixes {len({c[0].split("/")[1] for c in drawn})}')

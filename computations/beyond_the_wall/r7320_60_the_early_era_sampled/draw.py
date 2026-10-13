#!/usr/bin/env python3
r"""draw.py -- the r7320 draw, exactly as PREDICTION.md ③ registered it before this ran.

SIZE 40 of the 168; the first 40 by sha256(SALT + receipt + "\t" + literal_as_JSON), ascending hex,
with SALT the second redraft's own commit.  Deterministic from a salt published before the draw, so it
cannot be steered and anyone can reproduce it.
"""
import hashlib
import io
import json
import os
import re
import sys

SALT = '6bef6fd5acf0692299f306c96e2ee630542dac14'
SIZE = 40
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))


def seat(w):
    for s in ('+60', '+69', '+70', 'cc66', '+66', '+71'):
        if s in (w or ''):
            return s.lstrip('+')
    return '?'


def rev(w):
    m = re.match(r'r(\d{4})', w or '')
    return int(m.group(1)) if m else None


rows = []
for l in io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if len(c) >= 7 and c[0].startswith('receipts/'):
        rows.append(c)

pop = [c for c in rows
       if c[5] == 'DELIBERATE' and seat(c[6]) == '60' and (rev(c[6]) or 99999) < 7260]
assert len(pop) == 168, f'the registered population was 168, this tree has {len(pop)}'

keyed = sorted(pop, key=lambda c: hashlib.sha256(
    (SALT + c[0] + '\t' + c[1]).encode('utf-8')).hexdigest())
drawn = keyed[:SIZE]

out = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SAMPLE_40.tsv'), 'w',
              encoding='utf-8')
out.write('# r7320 the draw: the first 40 of 168 by sha256(SALT + receipt + TAB + literal), '
          f'SALT={SALT}\n')
out.write('# the population and the size were registered in PREDICTION.md before this ran.  '
          'No verdict column: the re-read is the next commit.\n')
out.write('# receipt\tliteral\ttarget\ttier\tflags\tverdicted_at\n')
for c in drawn:
    out.write('\t'.join([c[0], c[1], c[2], c[3], c[4], (re.match(r'r\d{4}', c[6]) or [''])[0]
                         if re.match(r'r\d{4}', c[6]) else '?']) + '\n')
out.close()
print(f'population {len(pop)};  drawn {len(drawn)}')
print(f'  tier   {({t: sum(1 for c in drawn if c[3] == t) for t in sorted({c[3] for c in drawn})})}')
print(f'  target {({t: sum(1 for c in drawn if c[2] == t) for t in sorted({c[2] for c in drawn})})}')
print(f'  prefixes {len({c[0].split("/")[1] for c in drawn})}')

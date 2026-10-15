#!/usr/bin/env python3
"""r7345+cc66 ruling (b): score candidate forms of "the container reads another receipt's SOURCE
line by line" against the HAND-JUDGED 14, on the narrow trace."""
import importlib.util, json, re, sys
S = sys.argv[1]
spec = importlib.util.spec_from_file_location('m', S + '/mutate_assertions.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

hand = {tuple(x.split('\t')) for x in open(S + '/want14.txt').read().split('\n') if '\t' in x}
hand = {(a, json.loads(b)) for a, b in hand}
new = set()
for ln in open(S + '/k_new2.keys'):
    q = ln.rstrip('\n').split('\t')
    if len(q) == 2:
        new.add((q[0], json.loads(q[1])))

LINEWISE = re.compile(r"\.splitlines\(|\.split\('\\n'\)|\.split\(\"\\n\"\)|\.readlines\(")
BLOB = re.compile(r"cat-file|git\('show'|git\('grep'|'show',")

rules = {
    'A  narrow kinds == {py}': lambda k, t: k == {'py'},
    'B  {py} AND linewise': lambda k, t: k == {'py'} and bool(LINEWISE.search(t)),
    'C  {py} AND (linewise OR blob)': lambda k, t: k == {'py'} and bool(LINEWISE.search(t) or BLOB.search(t)),
    'D  (py in kinds) AND linewise': lambda k, t: 'py' in k and bool(LINEWISE.search(t)),
    'E  ({py} OR no kind) AND (linewise OR blob)':
        lambda k, t: (k == {'py'} or not k) and bool(LINEWISE.search(t) or BLOB.search(t)),
}
got = {name: set() for name in rules}
for r in m.quote('/home/user/shadow-of-existence'):
    key = (r['receipt'], r['lit'])
    if key not in new:
        continue
    t = r.get('_trace') or ''
    kinds = set(m._EXT.findall(t))
    for name, f in rules.items():
        if f(kinds, t):
            got[name].add(key)
print(f'hand-judged class: {len(hand)} keys;  hop population: {len(new)}')
for name in rules:
    g = got[name]
    tp, fp, fn = len(g & hand), len(g - hand), len(hand - g)
    print(f'{name:46} caught={len(g):3d}  hit={tp:2d}  over={fp:2d}  missed={fn:2d}')
best = got['C  {py} AND (linewise OR blob)']
print('\n--- rule C over-catches ---')
for k in sorted(best - hand):
    print('  ', k[0].split('/')[-1][:44], '|', k[1][:46])
print('--- rule C misses ---')
for k in sorted(hand - best):
    print('  ', k[0].split('/')[-1][:44], '|', k[1][:46])

#!/usr/bin/env python3
"""r7435+70 ④ positive control for measure.py's zero: can it see an ambiguous bare basename at all?
python3 control.py WORKTREE_AT_r7287+70.2"""
import os, sys, tempfile
sys.argv = [sys.argv[0], sys.argv[1]]
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'measure.py'), encoding='utf-8').read().split("\nns['_orig_named'] = ", 1)[0]
g = {'__name__': 'm'}; exec(compile(src, 'measure.py', 'exec'), g)
BYBASE = g['BYBASE']; N = g['N']
amb = sorted((len(v), k) for k, v in BYBASE.items() if len(v) >= 2 and '.' in k)[::-1]
print(f'tracked files {len(g["TRACKED"])}; basenames shared by >= 2 tracked files: {sum(1 for v in BYBASE.values() if len(v) >= 2)}')
print('  most shared:', ', '.join(f'{k}({n})' for n, k in amb[:6]))
probe = os.path.join(N.ROOT, 'receipts', '_r7435_probe_.py')
open(probe, 'w').write(f"A = '{amb[0][1]}'\nB = '{amb[1][1]}'\nC = 'no_such_basename_r7435.txt'\n")
try:
    got = g['bare'](os.path.relpath(probe, N.ROOT))
finally:
    os.remove(probe)
print(f'  seeded receipt constants -> {got}')
ok = got.get(amb[0][1], 0) >= 2 and got.get(amb[1][1], 0) >= 2 and got.get('no_such_basename_r7435.txt') == 0
print('CONTROL', 'PASSES: an ambiguous bare basename is seen as ambiguous, an absent one as absent' if ok else 'FAILS')
sys.exit(0 if ok else 1)

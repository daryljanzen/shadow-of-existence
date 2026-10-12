#!/usr/bin/env python3
"""r7265+70.1 ①: L251/N1 ⓹ᵇ, OLD (60's half, whoever runs it) against NEW (the running node's half), on built repos."""
import os, shutil, subprocess, sys, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
os.environ['NODE'] = '60'
import check_revision_collisions as C

def build(revs):
    d = tempfile.mkdtemp(prefix='r7265.')
    g = lambda *a: subprocess.run(['git', '-C', d] + list(a), capture_output=True, text=True)
    g('init', '-q', '-b', 'main'); g('config', 'user.email', 's@l'); g('config', 'user.name', 's')
    open(os.path.join(d, 'f'), 'w').write('0\n'); g('add', '-A'); g('commit', '-q', '-m', 'base')
    g('branch', '-f', 'origin/main')
    for r in revs:
        open(os.path.join(d, 'f'), 'a').write(r + '\n'); g('add', '-A'); g('commit', '-q', '-m', f'{r} — seeded')
    return d

def at(parity, d):
    keep = C.PARITY
    try:
        C.PARITY = parity
        return C.band_violations(root=d)
    finally:
        C.PARITY = keep

SEEDS = [('N-a', '66', ['r4001', 'r4003']), ('N-b', '60', ['r4000', 'r4002']),
         ('N-c', '66', ['r4000', 'r4002', 'r4003']), ('N-d', 'ci', ['r4001', 'r4003'])]
want = {'N-a': (2, 0), 'N-b': (0, 0), 'N-c': (2, 2), 'N-d': (2, None)}
ok = True
for name, runner, revs in SEEDS:
    d = build(revs)
    try:
        o = at(0, d)
        p = C._PARITY_BY_NODE.get(runner)
        n = None if p is None else at(p, d)
    finally:
        shutil.rmtree(d, ignore_errors=True)
    got = (len(o), None if n is None else len(n))
    ok &= got == want[name]
    fmt = lambda v: 'None' if v is None else f'{len(v)} {[x[1] for x in v]}'
    print(f'{name}  NODE={runner:<3} commits={revs}  OLD {fmt(o)}  NEW {fmt(n)}  as predicted: {got == want[name]}')
print(f'all four seeds as pre-registered: {ok}')
sys.exit(0 if ok else 1)

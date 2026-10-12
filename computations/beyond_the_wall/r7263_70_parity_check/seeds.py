#!/usr/bin/env python3
"""r7263+70.1: B1 ⓸ᵇ, OLD against NEW, on six repositories this script builds (PREDICTION.md P1-P6).
OLD: the parity flipped to 66's half, whoever runs it.  NEW: the half of the node RUNNING it; no half -> None."""
import os, shutil, subprocess, sys, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
os.environ['NODE'] = '60'
import check_revision_collisions as C

def build(revs):
    d = tempfile.mkdtemp(prefix='r7263.')
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

def old(runner, d):
    return at(C._PARITY_BY_NODE['66'], d)

def new(runner, d):
    p = C._PARITY_BY_NODE.get(runner)
    return None if p is None else at(p, d)

SEEDS = [('P1', '60', []), ('P2', '60', ['r4000']), ('P3', '60', ['r4000', 'r4002', 'r4004']),
         ('P4', '60', ['r4000', 'r4002', 'r4003']), ('P5', '66', ['r4001', 'r4003']), ('P6', 'ci', ['r4000', 'r4002'])]
res = {}
for name, runner, revs in SEEDS:
    d = build(revs)
    try:
        o, n = old(runner, d), new(runner, d)
    finally:
        shutil.rmtree(d, ignore_errors=True)
    fmt = lambda v: 'None' if v is None else f'{len(v)} {[x[1] for x in v]}'
    res[name] = (revs, o, n)
    print(f'{name}  NODE={runner:<3} commits={revs}  OLD {fmt(o)}  NEW {fmt(n)}')
even = lambda revs: sum(int(r[1:]) % 2 == 0 for r in revs)
a = all(len(res[k][1]) == even(res[k][0]) for k in res)
b = all(res[k][2] == [] for k in ('P1', 'P2', 'P3', 'P5'))
c = [x[1] for x in res['P4'][2]] == ['r4003'] and res['P6'][2] is None
print(f'OLD count == even commits on every seed: {a}')
print(f'NEW count 0 on every in-band seed: {b}')
print(f'NEW fires on P4\'s odd commit only, and reports None for a runner with no half: {c}')
sys.exit(0 if a and b and c else 1)

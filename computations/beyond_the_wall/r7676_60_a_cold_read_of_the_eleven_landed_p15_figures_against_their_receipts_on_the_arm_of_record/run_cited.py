#!/usr/bin/env python3
"""r7676 (60) -- RUN each receipt the order's sites cite, once, bounded, and bank its output.

One bounded run each, nothing re-run for reassurance, every receipt that does not complete recorded
UNRUN with its timeout rather than dropped from the denominator.  Three at a time, one thread each,
because the comparison is `does this receipt print this figure under this label` and not a tolerance
reading.
"""
import ast
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT = os.path.join(HERE, 'runs')
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                           # noqa: E402

RECEIPTS = json.load(open(os.path.join(HERE, 'sites.json')))['receipts']
LONGSET = {}
try:
    for n in ast.walk(ast.parse(open(os.path.join(ROOT, 'scripts', 'run_all_receipts.py'),
                                     encoding='utf-8').read())):
        if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'LONG':
            LONGSET = {k.value: v.value for k, v in zip(n.value.keys, n.value.values)}
except Exception as e:                                                     # noqa: BLE001
    print(f"  (could not read LONG: {e})")


def one(name):
    path = G.FILES[name]
    budget = int(LONGSET.get(os.path.basename(path), 420))
    env = dict(os.environ, NODE='60')
    for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
        env[k] = '1'
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, path], cwd=os.path.dirname(path) or ROOT,
                           capture_output=True, text=True, timeout=budget, env=env)
        txt, rc, state = (r.stdout or '') + (r.stderr or ''), r.returncode, 'RAN'
    except subprocess.TimeoutExpired as e:
        raw = e.stdout
        txt = raw.decode('utf-8', 'replace') if isinstance(raw, bytes) else (raw or '')
        rc, state = None, 'UNRUN'
    dt = time.time() - t0
    open(os.path.join(OUT, name[:120] + '.txt'), 'w', encoding='utf-8').write(txt)
    print(f"  {state:<5} rc={str(rc):<5} {dt:>7.1f}s  budget {budget:>4}s  {name[:66]}", flush=True)
    return dict(receipt=name, state=state, rc=rc, seconds=round(dt, 1), budget=budget,
                chars=len(txt))


print(f"running {len(RECEIPTS)} receipt(s), 3 at a time, one thread each")
with ThreadPoolExecutor(max_workers=3) as ex:
    res = list(ex.map(one, RECEIPTS))
json.dump(res, open(os.path.join(HERE, 'runs.json'), 'w'), indent=1)
ran = sum(1 for r in res if r['state'] == 'RAN')
print(f"\n  RAN {ran} / {len(res)};  UNRUN {len(res) - ran}")

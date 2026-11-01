#!/usr/bin/env python3
"""r7650+60.1 -- re-run the receipts that died on the missing pinned dependency, now that
`camb==2.0.4` -- the version `requirements-ci.txt` pins -- is installed with `--no-deps` on the
pinned interpreter, verified to have moved nothing: python 3.11.17, numpy 2.4.6, scipy 1.17.1
unchanged and `check_env_fingerprint` green.
"""
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT = os.path.join(HERE, 'runs')
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                           # noqa: E402

PREV = {r['receipt']: r for r in json.load(open(os.path.join(HERE, 'runs.json')))}
BLOCK = []
for name in PREV:
    p = os.path.join(OUT, name[:120] + '.txt')
    if os.path.exists(p) and "No module named 'camb'" in open(p, encoding='utf-8',
                                                              errors='replace').read():
        BLOCK.append(name)
print(f"re-running {len(BLOCK)} receipt(s) blocked on the missing pin, 2 at a time")


def one(name):
    path = G.FILES[name]
    env = dict(os.environ, NODE='60')
    for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
        env[k] = '1'
    t0 = time.time()
    budget = 1500
    try:
        r = subprocess.run([sys.executable, path], cwd=os.path.dirname(path) or ROOT,
                           capture_output=True, text=True, timeout=budget, env=env)
        txt, rc, state = (r.stdout or '') + (r.stderr or ''), r.returncode, 'RAN'
    except subprocess.TimeoutExpired as e:
        txt = (e.stdout or b'').decode('utf-8', 'replace') if isinstance(e.stdout, bytes) else (e.stdout or '')
        rc, state = None, 'UNRUN'
    dt = time.time() - t0
    open(os.path.join(OUT, name[:120] + '.txt'), 'w', encoding='utf-8').write(txt)
    still = "No module named 'camb'" in txt
    print(f"  {state:<5} rc={str(rc):<5} {dt:>7.1f}s  camb-blocked still: {still}  {name[:62]}",
          flush=True)
    return dict(receipt=name, state=state, rc=rc, seconds=round(dt, 1), budget=budget,
                chars=len(txt), was_blocked=True, still_blocked=still)


with ThreadPoolExecutor(max_workers=2) as ex:
    res = list(ex.map(one, BLOCK))
merged = dict(PREV)
for r in res:
    merged[r['receipt']] = r
json.dump(list(merged.values()), open(os.path.join(HERE, 'runs.json'), 'w'), indent=1)
json.dump(res, open(os.path.join(HERE, 'rerun.json'), 'w'), indent=1)
ok = sum(1 for r in res if r['state'] == 'RAN' and not r['still_blocked'])
print(f"\n  {ok} of {len(res)} now complete without the dependency error")

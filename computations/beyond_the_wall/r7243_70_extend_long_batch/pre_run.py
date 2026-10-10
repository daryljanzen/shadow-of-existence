"""run each receipt that holds a candidate key once, before any edit: 'rc seconds path' per line"""
import json, os, subprocess, sys, time, concurrent.futures as cf
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
ext = json.load(open(os.path.join(HERE, 'extensions.json')))
recs = sorted({o['receipt'] for o in ext if not o['divergent'] and o['b_verdict'] == 'DISCRIMINATING'})
def one(r):
    t = time.time()
    try:
        rc = subprocess.run([sys.executable, r], cwd=ROOT, capture_output=True, timeout=900).returncode
    except subprocess.TimeoutExpired:
        rc = 'TIMEOUT'
    return f'{rc} {time.time() - t:.0f} {r}'
with cf.ThreadPoolExecutor(4) as ex, open(os.path.join(HERE, 'pre_run_log.txt'), 'w') as f:
    for line in ex.map(one, recs):
        f.write(line + '\n'); f.flush()
    f.write('DONE\n')

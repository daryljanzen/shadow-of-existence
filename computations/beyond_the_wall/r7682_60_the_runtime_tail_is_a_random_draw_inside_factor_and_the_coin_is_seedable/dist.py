"""The DISTRIBUTION the r7188 entry asked a later seat for: N fresh processes, the three ell steps
timed in each, nothing else changed."""
import json, os, re, subprocess, sys, time
R = sys.argv[1]
N = int(sys.argv[2])
env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1',
           NUMEXPR_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1', PYTHONUNBUFFERED='1')
env.pop('NODE', None)
rows = []
for i in range(N):
    t0 = time.time()
    marks = {}
    p = subprocess.Popen([sys.executable, R], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, env=env, bufsize=1)
    for ln in p.stdout:
        m = re.match(r'\s*ell=(\d+):', ln)
        if m:
            marks[f'ell{m.group(1)}'] = round(time.time() - t0, 2)
    p.wait()
    tot = round(time.time() - t0, 2)
    rows.append(dict(run=i, rc=p.returncode, total=tot, **marks))
    print(f"  run {i:>2}  rc={p.returncode}  ell1={marks.get('ell1')}  ell2={marks.get('ell2')}  "
          f"ell3={marks.get('ell3')}  total={tot}", flush=True)
json.dump(rows, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist.json'), 'w'),
          indent=1)
tot = sorted(r['total'] for r in rows)
d2 = sorted(round(r['ell2'] - r['ell1'], 2) for r in rows if 'ell1' in r and 'ell2' in r)
print(f"\n  N={len(rows)}  total: min {tot[0]}  median {tot[len(tot)//2]}  max {tot[-1]}  "
      f"spread {tot[-1]/tot[0]:.2f}x")
print(f"  the ell=2 STEP alone: min {d2[0]}  median {d2[len(d2)//2]}  max {d2[-1]}  "
      f"spread {d2[-1]/d2[0]:.2f}x")

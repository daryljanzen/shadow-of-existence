#!/usr/bin/env python3
"""r7695+70: HIER's SPLITCLOCK=L is byte-identical where it is not set (G1), and when set moves only the dynamics (G2).

G1. Pre-edit HIER (from git, BASE_REV = r7695+70.0, before the SPLITCLOCK=L edit) and the edited file are each imported
    in a fresh process and 19 quantities hashed: the background (ag, eg, Hc_of and every content fraction on eg,
    eta_rec/eta_0, DM, rs, eta_onset), the ionisation history (_zg, _xeg) and a short `evolve()` on five modes.
    Compared bitwise at: the default; the adjudicated environment; SPLITCLOCK=1 there; SPLITCLOCK=1 + SPLITIC=cr there.
G2. The edited file with SPLITCLOCK=L against SPLITCLOCK=1 at the adjudicated environment: every background and
    ionisation hash is equal (the same grid, projection and recombination), and only evolve()'s output moves.
Writes gate_leafpert.json; exit 0 only if G1 and G2 hold.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SB = os.path.join(ROOT, 'storyboard_receipts')
BASE = os.environ.get('BASE_REV', 'b1f2613cd')          # r7695+70.0: the tree before the SPLITCLOCK=L edit

PROBE = r'''
import os, sys, io, contextlib, hashlib, json
import numpy as np
sys.path.insert(0, os.environ['HDIR']); sys.path.insert(1, os.environ['SBDIR'])
with contextlib.redirect_stdout(io.StringIO()):
    import HIER_photon_hierarchy as H
def h(a): return hashlib.sha256(np.ascontiguousarray(np.asarray(a, dtype=float)).tobytes()).hexdigest()
out = {}
for n in ('ag', 'eg', '_zg', '_xeg'):
    out[n] = h(getattr(H, n))
for n in ('Hc_of', 'Og_of', 'On_of', 'Oc_of', 'Rb_of', 'Ob_of', 'Ocdm_of'):
    out[n] = h(getattr(H, n)(H.eg))
for n in ('eta_rec', 'eta_0', 'DM', 'rs', 'eta_onset'):
    out[n] = repr(float(getattr(H, n)))
kk = np.array([0.0005, 0.002, 0.008, 0.02, 0.05])
with contextlib.redirect_stdout(io.StringIO()):
    E, Y, e_sw = H.evolve(kk)
out['evolve_E'] = h(E); out['evolve_Y'] = h(Y); out['evolve_esw'] = repr(float(e_sw))
print('__J__' + json.dumps(out))
'''


def probe(hdir, env):
    e = {**os.environ, **env, 'HDIR': hdir, 'SBDIR': SB, 'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1'}
    e.pop('SPLITCLOCK', None)
    e.update({k: v for k, v in env.items()})
    r = subprocess.run([sys.executable, '-c', PROBE], env=e, capture_output=True, text=True, cwd=SB)
    ln = [x for x in r.stdout.splitlines() if x.startswith('__J__')]
    if not ln:
        sys.exit(f'probe failed ({hdir}, {env}):\n{r.stderr[-1500:]}')
    return json.loads(ln[0][5:])


old_dir = tempfile.mkdtemp(prefix='hier_pre_')
src = subprocess.run(['git', 'show', f'{BASE}:storyboard_receipts/HIER_photon_hierarchy.py'], cwd=ROOT,
                     capture_output=True, text=True, check=True).stdout
open(os.path.join(old_dir, 'HIER_photon_hierarchy.py'), 'w').write(src)
new_dir = tempfile.mkdtemp(prefix='hier_new_')
os.symlink(os.path.join(SB, 'HIER_photon_hierarchy.py'), os.path.join(new_dir, 'HIER_photon_hierarchy.py'))

ADJ = {'H0_L': '68.6000000000', 'OMF': '%.12f' % (0.2973 / 0.3150), 'KMAXL': '700'}
ENVS = {'default': {}, 'adjudicated': ADJ, 'split': {**ADJ, 'SPLITCLOCK': '1'},
        'split_splitic': {**ADJ, 'SPLITCLOCK': '1', 'SPLITIC': 'cr'}}
res = {'base_rev': BASE, 'G1': {}, 'G2': {}}
ok = True
for name, env in ENVS.items():
    a, b = probe(old_dir, env), probe(new_dir, env)
    diff = sorted(k for k in a if a[k] != b.get(k))
    res['G1'][name] = {'keys': len(a), 'differ': diff}
    ok &= not diff
u = probe(new_dir, ENVS['split'])
s = probe(new_dir, {**ADJ, 'SPLITCLOCK': 'L'})
same = sorted(k for k in u if u[k] == s.get(k))
moved = sorted(k for k in u if u[k] != s.get(k))
res['G2'] = {'equal_when_L': same, 'moved_when_L': moved}
g2 = set(moved) <= {'evolve_Y', 'evolve_E', 'evolve_esw'} and 'evolve_Y' in moved
ok &= g2
res['G1_holds'], res['G2_holds'] = all(not v['differ'] for v in res['G1'].values()), g2
json.dump(res, open(os.path.join(HERE, 'gate_leafpert.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
sys.exit(0 if ok else 1)

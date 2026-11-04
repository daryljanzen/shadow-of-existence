#!/usr/bin/env python3
"""r7673+70 item 1: fold `launch.sh` into `spectra/r7041_accept_cr_leafrec1.npz`.

The chain is the namesake's own, lifted rather than copied:
  * `r7039_directions/bank.py`'s transfer loop (the module-level `for arm in ...` over `TTAGS`), pointed at this
    build's slices and run on the CR arm only -> a scratch `r7039_transfer_cr.npz` (15 MB-class, untracked as there);
  * `r7041_directions/bank_thin.py`'s `main()`, pointed at that scratch directory, on the CR arm only.
Both are taken from their source by `ast`. Only the loop's arm tuple and the directories are replaced.

Recipe check first: lr0 (recorded point, LEAFREC=0) against `spectra/r7041_accept_cr.npz`, key by key. lr1 (refit
licensed point, LEAFREC=1) is banked only if lr0 reproduces exactly, with `config` and `manifest`. Writes `item1.json`.
"""
import ast
import json
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
SP = os.path.join(BW, 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/r7673')
AR = 'ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066 LEAFREC=1'


class CrOnly(ast.NodeTransformer):
    """('lcdm', 'cr') -> ('cr',) in a `for` header"""
    def visit_For(self, node):
        self.generic_visit(node)
        it = node.iter
        if isinstance(it, ast.Tuple) and [getattr(e, 'value', None) for e in it.elts] == ['lcdm', 'cr']:
            node.iter = ast.Tuple(elts=[ast.Constant('cr')], ctx=ast.Load())
        return node


def lift_transfer_fold():
    src = open(os.path.join(BW, 'r7039_directions', 'bank.py')).read()
    tree = ast.parse(src)
    keep = []
    for n in tree.body:
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
            keep.append(n)
        elif isinstance(n, ast.Assign) and any(getattr(t, 'id', '') in ('NK', 'QTAGS', 'TTAGS') for t in n.targets):
            keep.append(n)
        elif isinstance(n, ast.For) and 'TTAGS' in ast.unparse(n):
            keep.append(n)
    assert sum(isinstance(n, ast.For) for n in keep) == 1, 'expected exactly one transfer loop in r7039 bank.py'
    mod = ast.fix_missing_locations(CrOnly().visit(ast.Module(body=keep, type_ignores=[])))
    return compile(mod, 'r7039_directions/bank.py[transfer loop, cr]', 'exec')


def lift_thin():
    src = open(os.path.join(BW, 'r7041_directions', 'bank_thin.py')).read()
    tree = ast.parse(src)
    keep = [n for n in tree.body if not isinstance(n, ast.If)]          # drop only the `if __name__` block
    mod = ast.fix_missing_locations(CrOnly().visit(ast.Module(body=keep, type_ignores=[])))
    return compile(mod, 'r7041_directions/bank_thin.py[main, cr]', 'exec')


def build(lr):
    base = f'{D}/lr{lr}'
    sp = f'{base}/sp'
    os.makedirs(sp, exist_ok=True)
    for f in os.listdir(f'{base}/dlk'):
        if f.endswith('.log'):
            t = open(f'{base}/dlk/{f}').read()
            assert '__DONE__ rc=0' in t, f'lr{lr} {f}: not rc=0'
    g = {'__name__': 'fold', 'D': base, 'SP': sp}
    code = lift_transfer_fold()
    exec(code, g)                                   # defines NK/TTAGS/slices, then runs the cr transfer loop
    t = {'__name__': 'thin', '__file__': os.path.join(BW, 'r7041_directions', 'bank_thin.py')}
    exec(lift_thin(), t)
    t['SP'] = sp
    assert t['main']() == 0
    return np.load(os.path.join(sp, 'r7041_accept_cr.npz'), allow_pickle=True)


def compare(a, b):
    out = {}
    for k in b.files:
        if k not in a.files:
            out[k] = 'MISSING'
            continue
        x, y = a[k], b[k]
        if y.dtype.kind in 'USO':
            out[k] = 0.0 if str(x) == str(y) else 1.0
        elif x.shape != y.shape:
            out[k] = f'shape {x.shape} vs {y.shape}'
        else:
            out[k] = 0.0 if np.array_equal(x, y, equal_nan=True) else float(
                np.nanmax(np.abs(x - y)) / max(np.nanmax(np.abs(y)), 1e-300))
    return out


def walls(lr):
    w = []
    for f in sorted(os.listdir(f'{D}/lr{lr}/dlk')):
        if f.endswith('.log'):
            m = re.search(r'wall=(\d+)s', open(f'{D}/lr{lr}/dlk/{f}').read())
            w.append(int(m.group(1)) if m else None)
    return w


ns = np.load(os.path.join(SP, 'r7041_accept_cr.npz'), allow_pickle=True)
b0, b1 = build(0), build(1)
c0, c1 = compare(b0, ns), compare(b1, ns)
off0 = sorted(k for k, v in c0.items() if v != 0.0)
res = dict(recipe_check_lr0=dict(keys_off=off0, n_keys=len(c0)),
           lr1_keys_moved=sorted(k for k, v in c1.items() if v != 0.0),
           lr1_keys_unmoved=sorted(k for k, v in c1.items() if v == 0.0),
           A_mean=dict(namesake=float(np.nanmean(ns['A'])), lr1=float(np.nanmean(b1['A']))),
           scalars={q: dict(namesake=float(ns[f'{q}__fixed']), lr1=float(b1[f'{q}__fixed']))
                    for q in ('l_A', 'D_M', 'r_s', 'eta_ls', 'eta_ls_w')},
           wall_s=dict(lr0=walls(0), lr1=walls(1)))
res['A_mean']['rel'] = res['A_mean']['lr1'] / res['A_mean']['namesake'] - 1
if not off0:
    r = subprocess.run([sys.executable, '-c', 'import ACOUSTIC_two_arm as M; print("__C__" + str(M._resolved_config()))'],
                       cwd=BW, capture_output=True, text=True,
                       env={**os.environ, **dict(x.split('=') for x in AR.split()), 'OMP_NUM_THREADS': '1'})
    cfg = next(l[5:] for l in r.stdout.splitlines() if l.startswith('__C__'))
    assert json.loads(cfg).get('LEAFREC') is True
    out = {k: b1[k] for k in b1.files}
    out['config'] = np.array(cfg)
    out['manifest'] = np.array(json.dumps(dict(
        stem='r7041_accept_cr_leafrec1', namesake='r7041_accept_cr', LEAFREC=1,
        point=dict(CRH0=68.57073, CROM=0.291246, WBH2=0.021643, NS=1.015066, LEAFREC=1, ZSTART=3e7, LEAFSCALES=1),
        switches=f'{AR} HIER=1 LSTEP=8 LMAXL=2000 + SRCINJ=fixed | SRCINJ=sweep SRCINJRS=own, DLKSAVE',
        held='r7039_directions/launch.sh transfer runs (cr), six KSLICE pieces of 250; folded by r7039 bank.py\'s '
             'transfer loop and thinned by r7041 bank_thin.main(), both lifted; only the point and LEAFREC moved',
        note_r7673='the LEAFREC=0 rebuild through the same chain reproduces every namesake key exactly '
                   '(r7673_70_three_builds/item1.json)')))
    np.savez(os.path.join(SP, 'r7041_accept_cr_leafrec1.npz'), **out)
    res['banked'] = 'spectra/r7041_accept_cr_leafrec1.npz'
json.dump(res, open(os.path.join(HERE, 'item1.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != 'lr1_keys_unmoved'}, indent=1))
sys.exit(0 if not off0 else 1)

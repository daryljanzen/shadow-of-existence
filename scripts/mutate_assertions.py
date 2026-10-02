#!/usr/bin/env python3
"""mutate_assertions.py -- ** A CHECK THAT DOES NOT FLIP WHEN ITS MEASUREMENT IS DISPLACED IS ASSERTING SOMETHING ELSE. **

Built r7113+70.1 by node 70, on node 66's r7113 order; pre-registered at
computations/beyond_the_wall/r7113_70_mutation_instrument/PREDICTION.md.

** THE CLASS (r7111). **  Five assertions this round passed on something other than what they were filed
against: `C41b` on a literal `8.2\\%` still in the paper for an unrelated sentence; `R1` on a word count in
another lane's prose; `C63` and `P15_the_one_fitted_number_...` on a peak landing in the same grid bin as
before (exact equality on an abscissa of step 8 and 2); and `60`'s 404 sites, and the gate's own `1e-30`, on
the numerical floor.  `sweep_tolerances.py`'s BUILD PERTURBATION catches the floor class and cannot catch the
other three, because a literal, a count and a bin are build-stable.

** WHY THE MUTATION IS UPSTREAM OF THE CHECK. **  Displacing the operand AT the comparison always flips it --
`abs(X + 2T - V) < T` is false whatever X was -- so that mutation measures nothing.  What the class shares is
a check that does not READ the quantity it is filed against.  So each operator displaces the quantity where
it is MADE and lets the receipt carry the displacement to its checks:

  --tilt LIST OUT   TILT.  Every float array or number the receipt reads as data in-process (`np.load`,
                    `np.loadtxt`, `np.genfromtxt`, `json.load`) is multiplied by 1 + DELTA*u, u in [-1, 1]
                    along the last axis (a smooth tilt, so a continuous locator moves and a grid-quantised
                    one need not), DELTA = 0.05.  Integer arrays -- grids, indices, counts -- are untouched.
                    The receipt is run instrumented clean and tilted, and every ASSERTING comparison is
                    compared between the two (sweep_tolerances' probe, unchanged).
                      DETACHED  a float PREDICTION / EXACT pin -- or an integer one fed by an argmax-class
                                locator -- whose operands are bit-identical under the tilt and which passes on
                                both, in a receipt where the tilt demonstrably reached the computation (some
                                other site's operands moved).  It asserts something other than its data.
                      WIDE      operands moved and it still passes: a tolerance of 5% or more.  Reported.
                      NOT REACHED  the receipt read no tiltable data, or nothing moved: no verdict.
  --regrid LIST OUT REGRID.  Every subprocess call the receipt makes to `ACOUSTIC_two_arm.py` has its
                    `LSTEP` moved by one unit (8 -> 7; 1 -> 2), so a located peak moves by LESS than one
                    original step.  A site that passes clean and FAILS re-gridded claims a resolution finer
                    than its own abscissa: SUBQUANTUM.  Expensive (a full re-run of every instrument call),
                    so it runs on a named list only.
  --prose           PROSE-PIN, static.  An asserting comparison against a NON-ZERO number whose measured
                    operand traces in the file (names -> assignments -> called helpers, three levels) to a
                    count of pattern matches (`findall`, `finditer`, `.count(`) in a file that reads
                    `corpus/*.tex`.  An ABSENCE claim (`== 0`, `< 1`, `<= 0`) is exempt: it does not go
                    stale when another lane rewords.
  --seed            the planted both-ways set for all three operators; exit 0 iff exactly the planted
                    defects are flagged.

** WHAT IT CANNOT SEE, STATED BEFORE IT IS RUN. **  TILT reaches data read in-process through the four
loaders and nothing else: a receipt that computes from a subprocess's stdout, a CSV parsed by hand or a
hard-coded array is NOT REACHED, and is reported as that, never as clean.  REGRID knows one instrument and one
abscissa.  PROSE-PIN is a static trace three levels deep and misses a count laundered through a data
structure it does not follow.  And a check can read its data and still be wrong in a way none of these move.
"""
import argparse
import ast
import glob
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.abspath(__file__)
ROOT = os.path.dirname(os.path.dirname(HERE))
DELTA = 0.05
_JSON_LOAD = json.load          # the instrument's own I/O must never go through the tilt it installs
_spec = importlib.util.spec_from_file_location('sweep_tolerances', os.path.join(os.path.dirname(HERE),
                                                                                'sweep_tolerances.py'))
ST = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ST)
LOCATOR = re.compile(r'\b(argmax|argmin|nanargmax|nanargmin|argsort|searchsorted|find_peaks|argrelextrema|'
                     r'argrelmax|argrelmin)\b')


# ===================================================================================== the mutations
def _tilt_array(a, tag=''):
    import numpy as np
    if not isinstance(a, np.ndarray) or a.dtype.kind not in 'fc' or a.size == 0:
        return a
    if a.ndim == 0:
        # ⛭ a SCALAR gets its own factor, keyed on where it came from: a uniform 1+DELTA cancels in every ratio
        #   of two banked scalars (r7113+70.1's first run flagged `max(RS)/min(RS)` DETACHED for exactly that)
        import zlib
        u = (zlib.crc32(tag.encode()) % 2001) / 1000.0 - 1.0
        return a * (1 + DELTA * u)
    u = np.linspace(-1.0, 1.0, a.shape[-1]) if a.shape[-1] > 1 else np.ones(1)
    return a * (1 + DELTA * u)


class _Npz:
    """np.load's lazy archive, with every float member tilted on access"""
    def __init__(self, z, path=''):
        self._z = z
        self.files = z.files
        self._p = str(path)

    def __getitem__(self, k):
        return _tilt_array(self._z[k], f'{self._p}::{k}')

    def __contains__(self, k):
        return k in self._z.files

    def __iter__(self):
        return iter(self._z.files)

    def keys(self):
        return list(self._z.files)

    def items(self):
        return [(k, self[k]) for k in self._z.files]

    def values(self):
        return [self[k] for k in self._z.files]

    def get(self, k, d=None):
        return self[k] if k in self._z.files else d

    def __len__(self):
        return len(self._z.files)

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self._z.close()
        return False

    def close(self):
        self._z.close()

    def __getattr__(self, n):
        return getattr(self._z, n)


def _tilt_json(o):
    if isinstance(o, float):
        return o * (1 + DELTA)
    if isinstance(o, list):
        return [_tilt_json(x) for x in o]
    if isinstance(o, dict):
        return {k: _tilt_json(v) for k, v in o.items()}
    return o


def install_tilt():
    import numpy as np
    MUT = {'reads': 0}
    _load, _loadtxt, _genfromtxt = np.load, np.loadtxt, np.genfromtxt

    def load(*a, **k):
        r = _load(*a, **k)
        MUT['reads'] += 1
        if isinstance(r, np.ndarray):
            return _tilt_array(r, str(a[0]) if a else '')
        if hasattr(r, 'files'):
            return _Npz(r, a[0] if a else '')
        return r

    np.load = load
    np.loadtxt = lambda *a, **k: (MUT.__setitem__('reads', MUT['reads'] + 1), _tilt_array(_loadtxt(*a, **k)))[1]
    np.genfromtxt = lambda *a, **k: (MUT.__setitem__('reads', MUT['reads'] + 1),
                                     _tilt_array(_genfromtxt(*a, **k)))[1]
    _jl = json.load

    def jload(fp, *a, **k):
        r = _jl(fp, *a, **k)
        MUT['reads'] += 1
        return _tilt_json(r)
    json.load = jload
    return MUT


def install_regrid():
    MUT = {'calls': 0}
    _run, _co, _popen = subprocess.run, subprocess.check_output, subprocess.Popen

    def fix(args, kw):
        argv = args[0] if args else kw.get('args')
        s = ' '.join(map(str, argv)) if isinstance(argv, (list, tuple)) else str(argv)
        if 'ACOUSTIC_two_arm' not in s:
            return kw
        env = dict(kw.get('env') or os.environ)
        step = int(env.get('LSTEP', '8'))
        # ⛭ DIRECTION.  A pinned grid value v stays on the moved grid only if (v - 100) divides by the new step,
        #   so either direction alone can miss: r7113+70.1's first recall run took P15_the_one_fitted_number's
        #   l_1 = 206 from step 2 to 1 and 206 stayed on the grid.  `--regrid-dir up` takes step + 1.
        up = os.environ.get('MUTATE_REGRID_DIR') == 'up' or step == 1
        env['LSTEP'] = str(step + 1 if up else step - 1)
        MUT['calls'] += 1
        return dict(kw, env=env)

    subprocess.run = lambda *a, **k: _run(*a, **fix(a, k))
    subprocess.check_output = lambda *a, **k: _co(*a, **fix(a, k))

    class P(_popen):
        def __init__(self, *a, **k):
            super().__init__(*a, **fix(a, k))
    subprocess.Popen = P
    return MUT


def mutant_one(log, target, mode):
    """run ONE receipt instrumented (sweep_tolerances' probe, unchanged) under one mutation"""
    MUT = install_tilt() if mode == 'tilt' else install_regrid()
    import atexit
    atexit.register(lambda: _note(log, MUT))     # registered first, so it runs AFTER the probe's own dump
    ST.probe_one(log, target)


def _note(log, mut):
    try:
        d = _JSON_LOAD(open(log))       # ⛔ not json.load: in the child it is the TILTED loader, and reading
        d['mutation'] = mut             #   the probe's own log through it scaled every recorded value by 1+DELTA
        json.dump(d, open(log, 'w'))
    except Exception:
        pass


# ===================================================================================== running
def _child(rel, root, out, mode, budget):
    key = rel.replace('/', '_') + '.json'
    log = os.path.join(out, key)
    if os.path.exists(log):
        return
    d, f = os.path.split(os.path.join(root, rel))
    env = dict(os.environ, NODE='ci', PYTHONUNBUFFERED='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    cmd = ([sys.executable, os.path.join(os.path.dirname(HERE), 'sweep_tolerances.py'), '--probe-one', log, f]
           if mode == 'clean' else [sys.executable, HERE, '--mutant-one', log, f, mode])
    t0 = time.time()
    try:
        subprocess.run(cmd, cwd=d, env=env, capture_output=True, text=True, errors='replace', timeout=budget)
    except subprocess.TimeoutExpired:
        pass
    if not os.path.exists(log):
        json.dump({'receipt': rel, 'rc': None, 'sites': {}, 'timeout': True}, open(log, 'w'))
    ST._annotate(log, wall=round(time.time() - t0, 1))


def run_pair(rels, root, out, mode, jobs, budget):
    for sub in ('clean', mode):
        os.makedirs(os.path.join(out, sub), exist_ok=True)
    tasks = [(r, sub) for r in rels for sub in ('clean', mode)]
    with ThreadPoolExecutor(max_workers=jobs) as ex:
        list(ex.map(lambda t: _child(t[0], root, os.path.join(out, t[1]), t[1], budget), tasks))


def asserting(root, rel):
    """{site: (class, ctx, node)} for every asserting comparison, by sweep_tolerances' own classifier"""
    src = open(os.path.join(root, rel), encoding='utf-8', errors='replace').read()
    tree = ast.parse(src)
    out = {}
    for n, ctx in ST.contexts(tree):
        if isinstance(n, ast.Compare):
            k = ST.classify(n)
            if k:
                out[f'{n.lineno}:{n.col_offset}'] = (k, ctx, n)
    return out, src, tree


def _vals_equal(a, b):
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x[0] != y[0] or x[1] != y[1]:
            return False
    return True


def _floaty(s):
    return any(t.startswith(('float', 'nd:f', 'sympy_float', 'mpmath')) for t in s.get('types', []))


def _fed_by_locator(node, tree, src):
    """does the comparison's operand trace (names -> assignments, two levels) to an argmax-class locator?"""
    seg = ast.get_source_segment(src, node) or ''
    if LOCATOR.search(seg):
        return True
    names = {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}
    for _ in range(2):
        more = set()
        for a in ast.walk(tree):
            if isinstance(a, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                tg = a.targets if isinstance(a, ast.Assign) else [a.target]
                if any(isinstance(t, ast.Name) and t.id in names for t in tg):
                    s = ast.get_source_segment(src, a) or ''
                    if LOCATOR.search(s):
                        return True
                    more |= {n.id for n in ast.walk(a.value) if isinstance(n, ast.Name)} if a.value else set()
        names |= more
    return False


def judge(root, out, mode):
    rows, unreached = [], []
    for pc in sorted(glob.glob(os.path.join(out, 'clean', '*.json'))):
        pm = os.path.join(out, mode, os.path.basename(pc))
        C = json.load(open(pc))
        M = json.load(open(pm)) if os.path.exists(pm) else {'rc': 'missing', 'sites': {}}
        rel = C['receipt'] if not os.path.isabs(C['receipt']) else os.path.relpath(C['receipt'], root)
        if C.get('rc') != 0:
            unreached.append((rel, f'clean rc={C.get("rc")}'))
            continue
        try:
            sites, src, tree = asserting(root, rel)
        except (OSError, SyntaxError) as e:
            unreached.append((rel, f'unreadable: {e}'))
            continue
        cs, ms = C.get('sites', {}), M.get('sites', {})
        if mode == 'tilt':
            moved = [s for s in cs if s in ms and not _vals_equal(cs[s]['vals'], ms[s]['vals'])]
            if not (M.get('mutation') or {}).get('reads') or not moved:
                unreached.append((rel, 'NOT REACHED -- ' + ('no tiltable data read' if not
                                  (M.get('mutation') or {}).get('reads') else 'the tilt moved no comparison')))
                continue
            for sid, (k, ctx, node) in sites.items():
                if k not in ('PREDICTION', 'EXACT') or sid not in cs or sid not in ms:
                    continue
                a, b = cs[sid], ms[sid]
                if not a['vals'] or a['pass'] != a['n'] or b['pass'] != b['n']:
                    continue
                lit = all(isinstance(x, ast.Constant) for x in [node.left] + list(node.comparators))
                seg = ast.get_source_segment(src, node) or ''
                if _vals_equal(a['vals'], b['vals']):
                    if lit:
                        continue                      # a literal against a literal is the static class
                    # ⛭ INVARIANT BY DESIGN, read off the first population run (r7113+70.1: 14 of 31 DETACHED):
                    #   an exactness check (`== 0.0`, or a tolerance at or below 1e-8 -- an identity or a no-op
                    #   that two paths agree) and a sign agreement are SUPPOSED not to move.  Counted, not flagged.
                    tol = a['vals'][0][1] if a['op'] in ('Lt', 'LtE') else None
                    zero = any(ST.num(x) == 0.0 for x in [node.left] + list(node.comparators))
                    if re.search(r'\bsign\s*\(', seg) or zero or (tol is not None and abs(tol) <= 1e-8):
                        rows.append(dict(receipt=rel, site=sid, kind='INVARIANT', cls=k, text=seg[:140]))
                        continue
                    if _floaty(a) or _fed_by_locator(node, tree, src):
                        rows.append(dict(receipt=rel, site=sid, kind='DETACHED', cls=k, text=seg[:140]))
                elif _floaty(a):
                    rows.append(dict(receipt=rel, site=sid, kind='WIDE', cls=k,
                                     text=(ast.get_source_segment(src, node) or '')[:140]))
        else:
            if M.get('rc') is None or not (M.get('mutation') or {}).get('calls'):
                unreached.append((rel, 'NOT REACHED -- ' + ('no instrument call' if M.get('rc') is not None
                                                            else 'the re-gridded run did not finish')))
                continue
            for sid, (k, ctx, node) in sites.items():
                a, b = cs.get(sid), ms.get(sid)
                if not a or not b or a['pass'] != a['n']:
                    continue
                if b['pass'] < b['n']:
                    rows.append(dict(receipt=rel, site=sid, kind='SUBQUANTUM', cls=k,
                                     text=(ast.get_source_segment(src, node) or '')[:140]))
    return rows, unreached


# ===================================================================================== PROSE-PIN
_COUNT = re.compile(r'\b(findall|finditer)\s*\(|\.count\s*\(')
_TEX = re.compile(r"(corpus|\.tex\b|CR_[A-Za-z_]+\b)")


def _defs(tree):
    asg, fns = {}, {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                for nm in (x for x in ast.walk(t) if isinstance(x, ast.Name)):
                    asg.setdefault(nm.id, []).append(n.value)
        elif isinstance(n, (ast.AugAssign, ast.AnnAssign)) and isinstance(n.target, ast.Name) and n.value:
            asg.setdefault(n.target.id, []).append(n.value)
        elif isinstance(n, ast.FunctionDef):
            fns[n.name] = n
    return asg, fns


def _counts(expr, asg, fns, src, depth=3, seen=None):
    seen = seen if seen is not None else set()
    seg = ast.get_source_segment(src, expr) or ''
    if _COUNT.search(seg):
        return True
    if depth == 0:
        return False
    for n in ast.walk(expr):
        if isinstance(n, ast.Name) and n.id not in seen:
            seen.add(n.id)
            for v in asg.get(n.id, []):
                if _counts(v, asg, fns, src, depth - 1, seen):
                    return True
            if n.id in fns and _COUNT.search(ast.get_source_segment(src, fns[n.id]) or ''):
                return True
    return False


def prose(root, files=None):
    out = []
    files = files or sorted(glob.glob(os.path.join(root, 'receipts', '**', '*.py'), recursive=True))
    for f in files:
        try:
            src = open(f, encoding='utf-8', errors='replace').read()
            tree = ast.parse(src)
        except SyntaxError:
            continue
        if not re.search(r"\.tex['\"]|CR_cosmology|corpus", src):
            continue
        asg, fns = _defs(tree)
        pairs = []
        for n, ctx in ST.contexts(tree):
            if isinstance(n, ast.Compare) and len(n.ops) == 1:
                pairs.append((n, type(n.ops[0]).__name__, n.left, n.comparators[0]))
        # ⛭ the corpus's other check idiom, check(label, got, want): the comparison is inside the helper, so
        #   there is no Compare node at the site at all -- R1's `likelihood` pin is written this way and the
        #   first pass missed it (r7113+70.1, found by the recall run on R1's own history)
        for n in ast.walk(tree):
            if isinstance(n, ast.Call) and ST._CHECKY.search(ST.fname(n) or '') and len(n.args) >= 3:
                pairs.append((n, 'Eq', n.args[1], n.args[2]))
        for n, op, a, b in pairs:
            va, vb = ST.num(a), ST.num(b)
            if (va is None) == (vb is None):
                continue
            meas, lit = (b, va) if va is not None else (a, vb)
            lit_left = va is not None
            # absence claims are exempt: == 0, < 1, <= 0 (and their mirror images)
            eff = {'Lt': 'Gt', 'LtE': 'GtE', 'Gt': 'Lt', 'GtE': 'LtE'}.get(op, op) if lit_left else op
            if (eff == 'Eq' and lit == 0) or (eff == 'Lt' and lit <= 1) or (eff == 'LtE' and lit <= 0):
                continue
            if eff in ('NotEq',):
                continue
            if _counts(meas, asg, fns, src):
                # PRESENCE (> 0, >= 1) goes stale only when the last occurrence goes; PIN (== N, >= N > 1)
                # goes stale whenever the count moves -- C41b's was a PRESENCE pin and R1's a PIN
                tier = 'PRESENCE' if (eff == 'Gt' and lit < 1) or (eff == 'GtE' and lit <= 1) else 'PIN'
                out.append(dict(receipt=os.path.relpath(f, root), site=f'{n.lineno}:{n.col_offset}',
                                kind='PROSE-PIN', tier=tier, text=(ast.get_source_segment(src, n) or '')[:140]))
    return out


# ===================================================================================== seeds
_SEED_TILT = r'''
import numpy as np
z = np.load("data.npz")
ls, y = z["ls"], z["y"]
mean = float(np.mean(y))
expected = float(np.mean(0.1 + np.exp(-((ls - 300.4) / 40.0) ** 2)))
assert abs(mean / expected - 1) < 0.02                # READS its data: must NOT flag
quoted = 0.277
assert abs(quoted - 0.277) < 0.01                     # PLANTED: a literal beside a data computation -- DETACHED
i = int(np.argmax(y))
peak = int(ls[i])
assert peak == 300                                    # PLANTED: an argmax on the grid, exact -- DETACHED
j = int(np.argmax(y))
a, b, c = y[j - 1], y[j], y[j + 1]
peak_c = ls[j] + 0.5 * (a - c) / (a - 2 * b + c) * (ls[1] - ls[0])
assert abs(peak_c - 300.4) < 5.0                      # an interpolated (continuous) locator: must NOT flag
'''
_SEED_DATA = 'import numpy as np\nls = np.arange(100, 500, 8)\ny = 0.1 + np.exp(-((ls-300.4)/40.0)**2)\n' \
             'np.savez("data.npz", ls=ls, y=y)\n'
_SEED_INST = r'''
import os
step = int(os.environ.get("LSTEP", "8"))
true = 443.7
grid = list(range(100, 1000, step))
print("peaks at l = [%d]" % min(grid, key=lambda g: abs(g - true)))
'''
_SEED_REGRID = r'''
import os, re, subprocess, sys
INST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ACOUSTIC_two_arm.py")
out = subprocess.run([sys.executable, INST], capture_output=True, text=True,
                     env=dict(os.environ, LSTEP="8")).stdout
l1 = int(re.search(r"peaks at l = \[(\d+)", out).group(1))
assert l1 == 444                                      # PLANTED: exact on a step-8 grid -- SUBQUANTUM
assert abs(l1 - 444) <= 8                             # tolerates one step: must NOT flag
'''
_SEED_PROSE = r'''
import re
p15 = open("corpus/CR_cosmology.tex").read()
n = len(re.findall(r"8\.2\\%", p15))
assert n >= 1                                         # PLANTED: a presence pin on another lane's prose
assert len(re.findall(r"\\sim8", p15)) == 0           # an absence claim: must NOT flag
def wcount(w):
    return len(re.findall(w, p15))
lik = wcount("likelihood")
assert lik == 2                                       # PLANTED: a word count pinned
total = 3 + 4
assert total == 7                                     # not a count of prose: must NOT flag
'''


def seed():
    tmp = tempfile.mkdtemp(prefix='mut_seed_')
    ok = True
    try:
        d = os.path.join(tmp, 'receipts', 'SEED')
        os.makedirs(d)
        os.makedirs(os.path.join(d, 'corpus'))
        subprocess.run([sys.executable, '-c', _SEED_DATA], cwd=d, check=True)
        for name, body in (('T1_tilt.py', _SEED_TILT), ('G1_regrid.py', _SEED_REGRID),
                           ('ACOUSTIC_two_arm.py', _SEED_INST), ('P1_prose.py', _SEED_PROSE)):
            open(os.path.join(d, name), 'w').write(body)
        open(os.path.join(d, 'corpus', 'CR_cosmology.tex'), 'w').write('a 8.2\\% b likelihood c likelihood')

        def lines_of(rows, kind):
            return sorted(int(r['site'].split(':')[0]) for r in rows if r['kind'] == kind)

        def planted(body, tag):
            return sorted(i + 1 for i, l in enumerate(body.split('\n')) if tag in l and 'PLANTED' in l)

        out = os.path.join(tmp, 'tilt')
        run_pair(['receipts/SEED/T1_tilt.py'], tmp, out, 'tilt', 2, 120)
        rows, un = judge(tmp, out, 'tilt')
        got, want = lines_of(rows, 'DETACHED'), planted(_SEED_TILT, 'DETACHED')
        print(f'  TILT    flagged DETACHED at lines {got}; planted {want}   {"OK" if got == want else "MISS"}'
              + (f'   unreached: {un}' if un else ''))
        ok &= got == want
        out = os.path.join(tmp, 'regrid')
        run_pair(['receipts/SEED/G1_regrid.py'], tmp, out, 'regrid', 2, 120)
        rows, un = judge(tmp, out, 'regrid')
        got, want = lines_of(rows, 'SUBQUANTUM'), planted(_SEED_REGRID, 'SUBQUANTUM')
        print(f'  REGRID  flagged SUBQUANTUM at lines {got}; planted {want}   {"OK" if got == want else "MISS"}'
              + (f'   unreached: {un}' if un else ''))
        ok &= got == want
        rows = prose(tmp, [os.path.join(d, 'P1_prose.py')])
        got, want = lines_of(rows, 'PROSE-PIN'), planted(_SEED_PROSE, 'pin')
        print(f'  PROSE   flagged PROSE-PIN at lines {got}; planted {want}   {"OK" if got == want else "MISS"}')
        ok &= got == want
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


# ===================================================================================== main
def _list(path):
    return [l.strip() for l in open(path) if l.strip() and not l.startswith('#')]


def report(rows, unreached, title):
    print(f'\n  {title}: {len(rows)} site(s) in {len({r["receipt"] for r in rows})} receipt(s)')
    for r in rows:
        print(f'    [{r["kind"]:10s}]{"[" + r["tier"] + "]" if r.get("tier") else ""} {r["receipt"]}:{r["site"]}  '
              f'{r["text"]}')
    for rel, why in unreached:
        print(f'    [UNMEASURED] {rel}: {why}')


def main():
    if len(sys.argv) == 5 and sys.argv[1] == '--mutant-one':
        mutant_one(sys.argv[2], sys.argv[3], sys.argv[4])
        return 0
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    ap.add_argument('--tilt', nargs=2, metavar=('LIST', 'OUT'))
    ap.add_argument('--regrid', nargs=2, metavar=('LIST', 'OUT'))
    ap.add_argument('--prose', action='store_true')
    ap.add_argument('--files', nargs='*', help='with --prose: only these receipt files')
    ap.add_argument('--regrid-dir', choices=('down', 'up'), default='down',
                    help='move LSTEP down by one (default) or up by one')
    ap.add_argument('--jobs', type=int, default=4)
    ap.add_argument('--budget', type=int, default=1800)
    ap.add_argument('--seed', action='store_true')
    a = ap.parse_args()
    if a.seed:
        print('\n  mutate_assertions --seed: does each operator flag exactly its planted defects?\n')
        return seed()
    rc = 0
    os.environ['MUTATE_REGRID_DIR'] = a.regrid_dir      # read by the mutated child, which inherits it
    if a.prose:
        rows = prose(a.root, [os.path.abspath(f) for f in a.files] if a.files else None)
        report(rows, [], 'PROSE-PIN')
        rc |= bool(rows)
    for mode, arg in (('tilt', a.tilt), ('regrid', a.regrid)):
        if arg:
            run_pair(_list(arg[0]), a.root, os.path.abspath(arg[1]), mode, a.jobs, a.budget)
            rows, un = judge(a.root, os.path.abspath(arg[1]), mode)
            flagged = [r for r in rows if r['kind'] in ('DETACHED', 'SUBQUANTUM')]
            report(rows, un, mode.upper())
            rc |= bool(flagged)
    return int(rc)


if __name__ == '__main__':
    sys.exit(main())

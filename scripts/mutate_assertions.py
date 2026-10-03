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
  --quote           QUOTE-PIN, static (r7125+70.1).  An asserting test of a string literal's PRESENCE (`in`,
                    `re.search/match`, `find() >= 0`, `index`) in text traced to a FILE READ the receipt does
                    not own -- not its own `__file__`, not json/npz/csv data.  Reported per site with
                    target PAPER (`*.tex`) or SOURCE, tier SENTENCE (>= 3 words) or TOKEN, and flags ALT
                    (one arm of a disjunction of states), XOR (an exclusive one, the form that broke at
                    r7125) and OPEN (an openness marker in the literal).  Absence claims are exempt.  This
                    is `L-249`'s class (r3105), which was left ungated because a pin is not mechanically
                    separable from a check; the ratchet answers that the way PROSE-PIN does, by counting
                    and adjudicating rather than separating.
  --seed            the planted both-ways set for all four operators; exit 0 iff exactly the planted
                    defects are flagged.

** WHAT IT CANNOT SEE, STATED BEFORE IT IS RUN. **  TILT reaches data read in-process through the four
loaders and nothing else: a receipt that computes from a subprocess's stdout, a CSV parsed by hand or a
hard-coded array is NOT REACHED, and is reported as that, never as clean.  REGRID knows one instrument and one
abscissa.  PROSE-PIN is a static trace three levels deep and misses a count laundered through a data
structure it does not follow.  And a check can read its data and still be wrong in a way none of these move.
"""
import argparse
import ast
import functools
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
    _install_import_tilt(MUT)
    return MUT


# ⛭ r7119+70.1 (r7119 Q1): THE IMPORT ROUTE.  r7113's TILT reached data only through the four loaders, so a
#   receipt that takes its measurement by EXECUTING an instrument (C62's `_m._rD`, read off ACOUSTIC_two_arm
#   imported with importlib) was filed DETACHED although it reads its data -- by a route the tilt did not
#   perturb.  Every module executed from an instrument directory now has its float and float-array attributes
#   tilted after execution, each by its own factor keyed on module file and name.
def _instrument_dirs():
    env = os.environ.get('MUTATE_INSTRUMENT_DIRS')
    if env:
        return [os.path.abspath(d) for d in env.split(os.pathsep) if d]
    return [os.path.join(ROOT, 'computations'), os.path.join(ROOT, 'storyboard_receipts')]


def _tilt_module(mod, origin, MUT):
    import numpy as np
    n = 0
    for k, v in list(vars(mod).items()):
        if k.startswith('__'):
            continue
        tag = f'{origin}::{k}'
        if isinstance(v, float) and not isinstance(v, bool):
            setattr(mod, k, float(_tilt_array(np.array(v), tag)))
            n += 1
        elif isinstance(v, np.ndarray) and v.dtype.kind in 'fc' and v.size:
            setattr(mod, k, _tilt_array(v, tag))
            n += 1
    MUT['imports'] = MUT.get('imports', 0) + 1
    MUT['reads'] += 1 if n else 0


def _wrap_spec(spec, MUT):
    origin = os.path.abspath(getattr(spec, 'origin', '') or '')
    if not spec or not spec.loader or not any(origin.startswith(d + os.sep) for d in _instrument_dirs()):
        return spec
    ex = spec.loader.exec_module
    if getattr(ex, '_tilted', False):
        return spec

    def exec_module(mod):
        ex(mod)
        _tilt_module(mod, origin, MUT)
    exec_module._tilted = True
    try:
        spec.loader.exec_module = exec_module
    except Exception:
        pass
    return spec


def _install_import_tilt(MUT):
    import importlib.machinery
    import importlib.util
    _sffl = importlib.util.spec_from_file_location
    importlib.util.spec_from_file_location = lambda *a, **k: _wrap_spec(_sffl(*a, **k), MUT)

    class _Finder:
        @staticmethod
        def find_spec(name, path=None, target=None):
            spec = importlib.machinery.PathFinder.find_spec(name, path, target)
            return _wrap_spec(spec, MUT) if spec else None
    sys.meta_path.insert(0, _Finder)


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


_DATA = re.compile(r"np\.load|loadtxt|genfromtxt|json\.|open\(|import|exec_module|subprocess|environ|\.npz|"
                   r"\bz\[|\bglob\b|read\(")
_MATH = {'abs', 'float', 'int', 'round', 'min', 'max', 'sum', 'len', 'range', 'np', 'math', 'pi', 'log', 'exp',
         'sqrt', 'True', 'False', 'None'}


def _fn_reads(name, fns, src, seen=None):
    """does local function `name`, or any local function it calls (transitively), touch data?  r7119+70.1's first
    run filed B7's `npk0 == 8` CONSTANT because `b4_index` reads its spectrum through a second helper, `peaks`"""
    seen = seen if seen is not None else set()
    if name in seen:
        return False
    seen.add(name)
    body = ast.get_source_segment(src, fns[name]) or ''
    if _DATA.search(body):
        return True
    return any(_fn_reads(c.func.id, fns, src, seen) for c in ast.walk(fns[name])
               if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id in fns)


def _constant(node, tree, src, depth=4):
    """CONSTANT (r7119+70.1): does the comparison's operand trace only to literals and arithmetic -- local
    functions included -- with no loader, file, import or environment in the trace?  Such a pin checks a quoted
    figure by arithmetic and has no data to be detached from.  Unresolved names count as data (conservative)."""
    asg, fns = _defs(tree)
    seen, todo = set(), [node]
    computes = [False]          # ⛭ a bare literal COPIED and compared with itself checks nothing: it stays DETACHED.
    #                             CONSTANT needs the trace to compute something (an operator or a call)
    for _ in range(depth):
        nxt = []
        for e in todo:
            seg = ast.get_source_segment(src, e) or ''
            if _DATA.search(seg):
                return False
            if e is not node and any(isinstance(x, (ast.BinOp, ast.Call)) for x in ast.walk(e)):
                computes[0] = True
            for n in ast.walk(e):
                if isinstance(n, ast.Name) and n.id not in seen:
                    seen.add(n.id)
                    if n.id in _MATH or n.id in dir(__builtins__):
                        continue
                    if n.id in fns:
                        if _fn_reads(n.id, fns, src):
                            return False
                        computes[0] = True
                        continue
                    if n.id in asg:
                        nxt += asg[n.id]
                        continue
                    if any(isinstance(a, ast.arg) and a.arg == n.id for a in ast.walk(tree)):
                        continue                          # a function's own parameter: its caller's literal
                    return False
        if not nxt:
            return computes[0]
        todo = nxt
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
                        kind = 'CONSTANT' if _constant(node, tree, src) else 'DETACHED'
                        rows.append(dict(receipt=rel, site=sid, kind=kind, cls=k, text=seg[:140]))
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


# ===================================================================================== QUOTE-PIN (r7125+70.1)
# ⛭ the class `r7125` named off this seat's own routing line: an asserting test of a string literal's PRESENCE in
#   text the receipt READS from a file it does not own.  Seven instances were repaired by hand (00b81f9c,
#   555cd9f8, 0ecde732, 78f20759, 323f2522), each a gate that failed on another seat's rewording -- and twice on
#   the SUCCESS of the work it watched, when a sentence saying something was open was retired.
_READ = re.compile(r'\b(io\.)?open\s*\(|\.read_text\s*\(|\.read\s*\(\s*\)|\bbody_of\s*\(|\bread_\w*\s*\(|'
                   r'\bslurp\w*\s*\(|\bload_tex\w*\s*\(')
_OPEN_WORDS = re.compile(r'(?i)\b(conjectur\w*|open|owed|does not carry|not yet|remains?|unresolved|pending|'
                         r'not claim\w*|not shown|outstanding)\b')
_SELF = re.compile(r'open\(\s*(os\.path\.(abspath|realpath)\()?\s*__file__\s*\)?\s*[,)]')
_STRUCT = re.compile(r'\b(json|yaml|pickle|tomllib|np|numpy)\.(load|loads|safe_load)\s*\(|\bcsv\.(reader|DictReader)\b')


@functools.lru_cache(maxsize=4)
def _lines(src):
    return src.splitlines(keepends=True)


def _seg(src, n):
    """ast.get_source_segment without its per-call re-split of the whole file, which was 93 % of a 58 s run"""
    if getattr(n, 'end_lineno', None) is None:
        return ''
    L = _lines(src)
    a, b = n.lineno - 1, n.end_lineno - 1
    if a == b:
        return L[a].encode()[n.col_offset:n.end_col_offset].decode(errors='replace')
    return ''.join([L[a].encode()[n.col_offset:].decode(errors='replace')] + L[a + 1:b]
                   + [L[b].encode()[:n.end_col_offset].decode(errors='replace')])


def _strlit(n, asg, depth=2):
    """a string literal at n, through a module constant (`_AGR = "..."`) and simple `+` -- else None"""
    if isinstance(n, ast.Constant) and isinstance(n.value, str):
        return n.value
    if isinstance(n, ast.JoinedStr):
        parts = [v.value if isinstance(v, ast.Constant) else '{}' for v in n.values]
        s = ''.join(parts)
        return s if s.replace('{}', '').strip() else None
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
        a, b = _strlit(n.left, asg, depth), _strlit(n.right, asg, depth)
        return a + b if a is not None and b is not None else None
    if isinstance(n, ast.Name) and depth > 0:
        vals = asg.get(n.id, [])
        if len(vals) == 1:
            return _strlit(vals[0], asg, depth - 1)
    return None


def _reads(expr, asg, fns, src, depth=3, seen=None):
    """the text of every expression the container's trace visits, if the trace reaches a FILE READ -- else None.
    Follows names -> assignments, arguments, called helpers and `.lower()`-class methods, three levels (PROSE's)"""
    seen = seen if seen is not None else set()
    seg = _seg(src, expr) or ''
    acc, hit = [seg], bool(_READ.search(seg))
    for n in ast.walk(expr):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in fns and n.func.id not in seen:
            seen.add(n.func.id)
            body = _seg(src, fns[n.func.id]) or ''
            if _READ.search(body):
                hit = True
                acc.append(body)
        if depth and isinstance(n, ast.Name) and n.id not in seen:
            seen.add(n.id)
            for v in asg.get(n.id, []):
                r = _reads(v, asg, fns, src, depth - 1, seen)
                if r is not None:
                    hit = True
                    acc.append(r)
                else:
                    acc.append(_seg(src, v) or '')
    return '\n'.join(acc) if hit else None


_VERDICT = re.compile(r"PASS|FAIL|\bassert\b|\braise\b|CHECKS|RESULTS|\.append\(\(")


def _assert_roots(tree, fns, src):
    # ⛭ a check helper is recognised by NAME (sweep_tolerances' `check`-family) OR by BODY: the corpus's `gate(name,
    #   ok)` records a verdict and matches no name rule -- the first recall run returned 0 of 5 for exactly that
    checky = {k for k, f in fns.items() if _VERDICT.search(_seg(src, f) or '')}
    roots = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Assert):
            roots.append(n.test)
        elif isinstance(n, ast.Call) and (ST._CHECKY.search(ST.fname(n) or '') or
                                          (isinstance(n.func, ast.Name) and n.func.id in checky)):
            # a check's LABEL is not its verdict: an f-string label interpolating `{_OWED}` is a report, and
            #   reading it as an assertion un-flags the ALT form the verdict argument actually has (r7125+70.1)
            roots.extend(a for a in list(n.args) + [k.value for k in n.keywords]
                         if not isinstance(a, (ast.JoinedStr, ast.Constant)))
        elif isinstance(n, ast.If):
            body = ast.dump(ast.Module(body=n.body, type_ignores=[]))
            if re.search(r"(?i)'[^']*(fail|bad)[^']*'", body) or any(isinstance(b, ast.Raise) for b in n.body):
                roots.append(n.test)
    return roots


def _quote_site(n, neg, asg, fns, src):
    """(literal, container, present) if n is a literal-presence test against a traced container, else None"""
    def _re(call):
        if (isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute)
                and call.func.attr in ('search', 'match', 'fullmatch') and len(call.args) >= 2
                and isinstance(call.func.value, ast.Name) and call.func.value.id == 're'):
            return _strlit(call.args[0], asg), call.args[1]
        return None, None

    def _find(call):
        if (isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute)
                and call.func.attr in ('find', 'index', 'rfind', 'rindex') and call.args):
            return _strlit(call.args[0], asg), call.func.value
        return None, None

    if isinstance(n, ast.Compare) and len(n.ops) == 1:
        op, rhs = n.ops[0], n.comparators[0]
        if isinstance(op, (ast.In, ast.NotIn)):
            lit = _strlit(n.left, asg)
            if lit is not None:
                return lit, rhs, isinstance(op, ast.In) != neg
        lit, cont = _re(n.left)
        if lit is not None and isinstance(rhs, ast.Constant) and rhs.value is None:
            return lit, cont, isinstance(op, ast.IsNot) != neg
        lit, cont = _find(n.left)
        v = ST.num(rhs)
        if lit is not None and v is not None:
            name = type(op).__name__
            # find() is -1 when absent: `>= 0`, `> -1`, `!= -1` (or a position bound) need the literal present
            present = (name in ('GtE', 'Gt') and v >= -1) or (name == 'NotEq' and v == -1)
            absent = (name == 'Eq' and v == -1) or (name == 'Lt' and v <= 0) or (name == 'LtE' and v < 0)
            if present or absent:
                return lit, cont, present != neg
    if isinstance(n, ast.Call):
        lit, cont = _re(n)
        if lit is not None:
            return lit, cont, not neg
        lit, cont = _find(n)
        if lit is not None and n.func.attr in ('index', 'rindex'):
            return lit, cont, True
    return None


_ALT_RANK = {False: 0, 'XOR': 1, True: 2}


def quote(root, files=None):
    out = []
    files = files or sorted(glob.glob(os.path.join(root, 'receipts', '**', '*.py'), recursive=True))
    for f in files:
        try:
            src = open(f, encoding='utf-8', errors='replace').read()
            tree = ast.parse(src)
        except SyntaxError:
            continue
        if not _READ.search(src):
            continue
        asg, fns = _defs(tree)
        best = {}       # id(node) -> (node, literal, container, alt)

        def visit(n, neg, alt, hops, seen):
            if isinstance(n, (ast.Lambda, ast.FunctionDef)):
                return
            s = _quote_site(n, neg, asg, fns, src)
            if s is not None:
                lit, cont, present = s
                if present:
                    # reached by several routes, the strictest reading wins: bare < XOR < ALT
                    prev = best.get(id(n))
                    if prev is None or _ALT_RANK[alt] < _ALT_RANK[prev[3]]:
                        best[id(n)] = (n, lit, cont, alt)
            if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.Not):
                visit(n.operand, not neg, alt, hops, seen)
                return
            if isinstance(n, ast.BoolOp):
                for v in n.values:
                    visit(v, neg, alt or (isinstance(n.op, ast.Or) and len(n.values) > 1), hops, seen)
                return
            if (isinstance(n, ast.Compare) and len(n.ops) == 1 and isinstance(n.ops[0], (ast.Eq, ast.NotEq))
                    and s is None and ST.num(n.comparators[0]) is None and ST.num(n.left) is None):
                # `(A and B) != C`: a test of two STATES, and EXCLUSIVE -- the form that went red at r7125 when the
                #   pass produced a third state with both true, so it is flagged XOR beside ALT and not let pass as it
                for v in (n.left, n.comparators[0]):
                    visit(v, neg, 'XOR', hops, seen)
                return
            if isinstance(n, ast.Name) and hops and n.id not in seen:
                for v in asg.get(n.id, []):
                    visit(v, neg, alt, hops - 1, seen | {n.id})
                return
            for c in ast.iter_child_nodes(n):
                visit(c, neg, alt, hops, seen)

        for r in _assert_roots(tree, fns, src):
            visit(r, False, False, 2, frozenset())
        for n, lit, cont, alt in best.values():
            trace = _reads(cont, asg, fns, src)
            if trace is None:
                continue
            # not text another seat owns: the receipt's OWN source (`open(__file__)`, a self-pin, found in the
            #   r7125+70.1 precision sample), or structured data whose `in` is key membership, not a quotation
            if _SELF.search(trace) or _STRUCT.search(trace):
                continue
            target = 'PAPER' if re.search(r'\.tex\b', trace) else 'SOURCE'
            # SENTENCE: three or more whitespace-separated words -- wording another seat owns.  TOKEN: a label,
            #   a receipt name, a macro, a figure -- a cross-reference rather than prose
            tier = 'SENTENCE' if len(lit.split()) >= 3 else 'TOKEN'
            flags = ','.join(x for x, on in (('ALT', alt), ('XOR', alt == 'XOR'),
                                             ('OPEN', bool(_OPEN_WORDS.search(lit)))) if on)
            out.append(dict(receipt=os.path.relpath(f, root), site=f'{n.lineno}:{n.col_offset}', kind='QUOTE-PIN',
                            target=target, tier=tier, flags=flags, lit=' '.join(lit.split())))
    # `re.search(...) is not None` reaches the same site as its Compare and as its Call: one site, ALT only if
    #   every route to it is ALT
    uniq = {}
    for r in out:
        k = (r['receipt'], r['site'], r['lit'])
        if k in uniq and 'ALT' not in r['flags']:
            uniq[k] = r
        uniq.setdefault(k, r)
    out = sorted(uniq.values(), key=lambda r: (r['receipt'], tuple(int(x) for x in r['site'].split(':'))))
    return out


# ===================================================================================== CANNOT-FAIL (r7139+70.1)
# ⛭ an assertion, or an `or`-arm that dominates it, which is true WHATEVER the measured text or value is.  The
#   object behind cc66's `n >= 0`, B14's `... else True`, and r7137's vacuous arms.  Per assertion, static.
#   ⚠ NOT a DEAD arm (one that can never fire): that needs the container's contents and is out of static reach.
_NONNEG = ('len', 'abs', 'sum', 'count', 'sqrt', 'exp')


def _verdicts(tree, fns, src):
    """the VERDICT expression of every asserting context -- an assert's test, a check's second argument (the
    first being its label), an `if` that guards a failure"""
    checky = {k for k, f in fns.items() if _VERDICT.search(_seg(src, f))}
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Assert):
            out.append(n.test)
        elif isinstance(n, ast.Call) and (ST._CHECKY.search(ST.fname(n) or '') or
                                          (isinstance(n.func, ast.Name) and n.func.id in checky)):
            # the LABEL is the string argument and the verdict the other: the corpus writes both `check(label, ok)`
            #   and `check(ok, label)` -- the first full run read 600 labels as literal verdicts (r7139+70.1)
            if len(n.args) >= 2:
                lab = lambda x: isinstance(x, ast.JoinedStr) or (isinstance(x, ast.Constant) and isinstance(x.value, str))
                if lab(n.args[0]) and not lab(n.args[1]):
                    out.append(n.args[1])
                elif lab(n.args[1]) and not lab(n.args[0]):
                    out.append(n.args[0])
                elif not lab(n.args[0]) and not lab(n.args[1]):
                    out.append(n.args[1])
        elif isinstance(n, ast.If):
            body = ast.dump(ast.Module(body=n.body, type_ignores=[]))
            if re.search(r"(?i)'[^']*(fail|bad)[^']*'", body) or any(isinstance(b, ast.Raise) for b in n.body):
                out.append(n.test)
    return out


def _pure_literal(e):
    return not any(isinstance(m, (ast.Name, ast.Call, ast.Attribute, ast.Subscript, ast.JoinedStr, ast.Starred,
                                  ast.Lambda, ast.comprehension)) for m in ast.walk(e))


@functools.lru_cache(maxsize=2)
def _corpus_texts(root):
    tex = [open(f, encoding='utf-8', errors='replace').read() for f in glob.glob(os.path.join(root, 'corpus', '*.tex'))]
    rec = [open(f, encoding='utf-8', errors='replace').read()
           for f in glob.glob(os.path.join(root, 'receipts', '**', '*.py'), recursive=True)]
    return tex, rec


def _ubiquity(root, lit, target, lower):
    tex, rec = _corpus_texts(root)
    pool = tex if target == 'PAPER' else rec
    if not pool:
        return 0.0
    if lower:
        lit = lit.lower()
        return sum(lit in t.lower() for t in pool) / len(pool)
    return sum(lit in t for t in pool) / len(pool)


def cannot_fail(root, files=None, ubiq_root=None, thresh=0.5):
    out = []
    ubiq_root = ubiq_root or root
    files = files or sorted(glob.glob(os.path.join(root, 'receipts', '**', '*.py'), recursive=True))
    for f in files:
        try:
            src = open(f, encoding='utf-8', errors='replace').read()
            tree = ast.parse(src)
        except SyntaxError:
            continue
        asg, fns = _defs(tree)
        imported = {a.name.split('.')[0] for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))
                    for a in getattr(n, 'names', [])} | {n.module.split('.')[0] for n in ast.walk(tree)
                                                          if isinstance(n, ast.ImportFrom) and n.module}
        seen = set()

        def hit(n, cls):
            if (id(n), cls) in seen:
                return
            seen.add((id(n), cls))
            out.append(dict(receipt=os.path.relpath(f, root), site=f'{n.lineno}:{n.col_offset}', cls=cls,
                            text=' '.join(_seg(src, n).split())[:150]))

        for v in _verdicts(tree, fns, src):
            # T2: the verdict itself is a literal
            if _pure_literal(v):
                # only a BOOLEAN-shaped literal is a verdict: `expect(x, 27)` passes an expected value, not a verdict.
                #   `True` is T2; arithmetic on literals is the CONSTANT class (r7119), cannot fail by construction
                #   and counted apart, because the gate rules it a deliberate check of a quoted figure.
                if isinstance(v, ast.Constant) and v.value is True:
                    hit(v, 'T2 LITERAL-TRUE')
                elif isinstance(v, (ast.Compare, ast.BoolOp, ast.UnaryOp)):
                    try:
                        if eval(compile(ast.Expression(v), '<v>', 'eval'), {'__builtins__': {}}):
                            hit(v, 'T2c LITERAL-ARITHMETIC')
                    except Exception:
                        pass
                continue
            for n in ast.walk(v):
                if isinstance(n, ast.Compare) and len(n.ops) == 1:
                    op, a, b = n.ops[0], n.left, n.comparators[0]
                    # T1: identical sides, or a non-negative quantity against 0 / -1
                    if (isinstance(op, (ast.Eq, ast.LtE, ast.GtE, ast.Is)) and not _pure_literal(a)
                            and ast.dump(a) == ast.dump(b)):
                        hit(n, 'T1 TAUTOLOGY')
                    for x, y, o in ((a, b, op), (b, a, {ast.LtE: ast.GtE(), ast.Lt: ast.Gt()}.get(type(op), op))):
                        nn = (isinstance(x, ast.Call) and ST.fname(x) in _NONNEG) or (
                            isinstance(x, ast.Name) and asg.get(x.id) and all(
                                isinstance(w, ast.Call) and ST.fname(w) in _NONNEG for w in asg[x.id]))
                        v0 = ST.num(y)
                        if nn and v0 is not None and ((isinstance(o, ast.GtE) and v0 <= 0) or
                                                      (isinstance(o, ast.Gt) and v0 < 0)):
                            hit(n, 'T1 TAUTOLOGY')
                    # T3: a module the file imports, tested for presence in sys.modules
                    if (isinstance(op, ast.In) and isinstance(a, ast.Constant) and isinstance(a.value, str)
                            and isinstance(b, ast.Attribute) and b.attr == 'modules'
                            and a.value.split('.')[0] in imported):
                        hit(n, 'T3 TRIVIAL-ENV')
                if (isinstance(n, ast.Call) and ST.fname(n) == 'exists' and n.args
                        and '__file__' in _seg(src, n.args[0]) and 'join' not in _seg(src, n.args[0])):
                    hit(n, 'T3 TRIVIAL-ENV')
                if isinstance(n, ast.BoolOp) and isinstance(n.op, ast.Or):
                    if any(isinstance(x, ast.Constant) and x.value is True for x in n.values):
                        hit(n, 'T1 TAUTOLOGY')
                    # T5: an arm whose literal is in most files of its haystack's kind dominates the disjunction
                    if len(n.values) > 1:
                        for x in n.values:
                            s = _quote_site(x, False, asg, fns, src)
                            if s is None or not s[2]:
                                continue
                            lit, cont, _ = s
                            trace = _reads(cont, asg, fns, src)
                            if trace is None:
                                continue
                            target = 'PAPER' if re.search(r'\.tex\b', trace) else 'SOURCE'
                            lower = '.lower()' in _seg(src, cont) or '.lower()' in trace
                            u = _ubiquity(ubiq_root, lit, target, lower)
                            if u >= thresh:
                                hit(x, f'T5 UBIQUITOUS-ARM ({100 * u:.0f}% of {target.lower()} files)')
                # T4: a guard whose other branch is literally True
                if isinstance(n, ast.IfExp) and any(isinstance(x, ast.Constant) and x.value is True
                                                    for x in (n.body, n.orelse)):
                    hit(n, 'T4 GUARDED-TRUE')
    out.sort(key=lambda r: (r['receipt'], tuple(int(x) for x in r['site'].split(':'))))
    return out


def report_cannot_fail(rows):
    from collections import Counter
    c = Counter(r['cls'].split(' (')[0] for r in rows)
    print(f'\n  CANNOT-FAIL: {len(rows)} site(s) in {len({r["receipt"] for r in rows})} receipt(s)   {dict(sorted(c.items()))}')
    for r in rows:
        print(f'    [CANNOT-FAIL][{r["cls"]}] {r["receipt"]}:{r["site"]}  {r["text"]}')


# ================================================================ UNREAD-FIGURE (r7147+70.1)
# ⛭ THE FIFTH CLASS: A RECEIPT THAT ASSERTS A PAPER'S FIGURE IT NEVER READS.  The routed instance
#   (`P15_the_exact_transmission_ratios...`, before r7145): `check(f"... rounds to the paragraph's 3.32 ...",
#   round(Deta, 2) == 3.32)` in a file that opens no .tex.  Its subject is the paper and its measurement is
#   its own arithmetic, so no file-scoped gate reaches it -- there is nothing to scope on.
#   A SITE = a check whose LABEL attributes a figure to a text AND whose VERDICT carries that figure (a
#   numeric literal also written in the label, or a name the label interpolates that resolves to literals).
#   Partitioned by READ (NO-READ is the class proper) and WHERE (the figure in the home paper, another
#   .tex, or none -- IN-NO-TEX is the drifted sub-class: the paper no longer prints what is attributed to it).
_ATTRIB = re.compile(r"(?i)\bthe (paper|paragraph|passage|sentence|section|table|caption|abstract|row|text|"
                     r"corollary|theorem|proposition|remark|footnote|appendix)['’]s\b|"
                     r"\bas (printed|stated|quoted|written)\b|\bP\d\d?['’]s\b|\\\\?(eq)?ref\b|\b(sec|eq|tab):")
_TEXREAD = re.compile(r"\.tex\b")
PAPER_OF_DIR = {'P1': 'BH_causality_v2', 'P2': 'janzen_circle_v3', 'P3': 'SdS-slicing-curve_v2',
                'P4': 'modern_parallax', 'P5': 'groupoid_paper', 'P6': 'shadow_of_existence',
                'P7': 'CR_framework', 'P8': 'slicing_operator', 'P9': 'range_paper', 'P10': 'canonical_time',
                'P11': 'dynamics_paper', 'P12': 'algebroid_paper', 'P13': 'boundary_paper',
                'P14': 'matter_sector_paper', 'P15': 'CR_cosmology', 'P16': 'cosmogenesis_paper',
                'P17': 'geometric_core_paper', 'p0': 'geometric_core_paper', 'P18': 'CR_synthesis'}


def _num_lits(node, src):
    """the source text of every numeric literal under node (bool excluded; a leading unary minus kept)"""
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
            out.append((_seg(src, n) or repr(n.value)).replace('_', ''))
    return out


def _for_bindings(tree, src):
    """name -> numeric-literal texts it takes in a `for` over a literal tuple/list (by position)"""
    out = {}
    for n in ast.walk(tree):
        if isinstance(n, (ast.For, ast.comprehension)) and isinstance(n.iter, (ast.Tuple, ast.List)):
            tgt = n.target
            for el in n.iter.elts:
                if isinstance(tgt, ast.Name):
                    out.setdefault(tgt.id, []).extend(_num_lits(el, src) if isinstance(el, ast.Constant) else [])
                elif isinstance(tgt, ast.Tuple) and isinstance(el, (ast.Tuple, ast.List)) and len(el.elts) == len(tgt.elts):
                    for t, v in zip(tgt.elts, el.elts):
                        if isinstance(t, ast.Name) and isinstance(v, ast.Constant):
                            out.setdefault(t.id, []).extend(_num_lits(v, src))
    return out


def _resolves_to_lits(name, asg, forb, src):
    lits = list(forb.get(name, []))
    for v in asg.get(name, []):
        if isinstance(v, (ast.Constant, ast.UnaryOp, ast.Dict, ast.Tuple, ast.List)) and _pure_literal(v):
            # a dict's KEYS are indices (`PAPER = {15: 0.926}`), not figures: its values only
            for e in (v.values if isinstance(v, ast.Dict) else [v]):
                lits.extend(_num_lits(e, src))
    return lits


def _label_names(lab):
    return {n.id for n in ast.walk(lab) if isinstance(n, ast.Name)} if isinstance(lab, ast.JoinedStr) else set()


def _label_text(lab, src):
    if isinstance(lab, ast.Constant):
        return lab.value
    return ''.join(v.value if isinstance(v, ast.Constant) else '{}' for v in lab.values)


@functools.lru_cache(maxsize=2)
def _tex_texts(root):
    """paper -> the set of numeric tokens it prints"""
    return {os.path.basename(f)[:-4]: set(re.findall(r'(?<![\d.])\d+(?:\.\d+)?',
                                                      open(f, encoding='utf-8', errors='replace').read()))
            for f in glob.glob(os.path.join(root, 'corpus', '*.tex'))}


def _in_tex(lit, toks):
    """does the paper print this figure -- AT THE PAPER'S OWN PRECISION?  `3.3387380236` in a receipt is the
    paper's `3.33874`: a printed token t matches when it has no more decimals than the literal and the literal
    rounds to it (the first draft matched exact text and filed the r7145 repair as IN-OTHER-TEX)"""
    lit = lit.lstrip('+')
    if lit in toks:
        return True
    try:
        v = float(lit)
    except ValueError:
        return False
    d = len(lit.split('.')[1]) if '.' in lit else 0
    for t in toks:
        td = len(t.split('.')[1]) if '.' in t else 0
        if 1 <= td < d and t.split('.')[0] == lit.split('.')[0] and abs(float(t) - v) <= 0.5 * 10 ** -td + 1e-12:
            return True
    return False


def unread_figure(root, files=None, tex_root=None):
    out = []
    tex = _tex_texts(tex_root or root)
    files = files or sorted(glob.glob(os.path.join(root, 'receipts', '**', '*.py'), recursive=True))
    for f in files:
        try:
            src = open(f, encoding='utf-8', errors='replace').read()
            tree = ast.parse(src)
        except SyntaxError:
            continue
        asg, fns = _defs(tree)
        forb = _for_bindings(tree, src)
        checky = {k for k, fn in fns.items() if _VERDICT.search(_seg(src, fn) or '')}
        reads = 'READS-PAPER' if (_TEXREAD.search(src) and _READ.search(src)) else 'NO-READ'
        m = re.match(r'(P\d+|p0)_', os.path.basename(os.path.dirname(f)))
        home = PAPER_OF_DIR.get(re.sub(r'^P0', 'P', m.group(1))) if m else None
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and len(n.args) >= 2 and (ST._CHECKY.search(ST.fname(n) or '') or
                                                                     (isinstance(n.func, ast.Name) and n.func.id in checky))):
                continue
            lab = lambda x: isinstance(x, ast.JoinedStr) or (isinstance(x, ast.Constant) and isinstance(x.value, str))
            if lab(n.args[0]) and not lab(n.args[1]):
                label, verdict = n.args[0], n.args[1]
            elif lab(n.args[1]) and not lab(n.args[0]):
                label, verdict = n.args[1], n.args[0]
            else:
                continue
            ltext = _label_text(label, src)
            if not _ATTRIB.search(ltext):
                continue
            # written IN the label as a token of its own: `2` is not in "3.32" (the first draft matched substrings)
            figs = [x for x in _num_lits(verdict, src)
                    if re.search(r'(?<![\d.])' + re.escape(x.lstrip('-')) + r'(?![\d]|\.\d)', ltext)]
            lnames = _label_names(label)
            # a name used only as a SUBSCRIPT in the verdict (`PAPER[l]`) is an index, not a figure
            idx = [x.slice.id for x in ast.walk(verdict) if isinstance(x, ast.Subscript) and isinstance(x.slice, ast.Name)]
            vnames = [x.id for x in ast.walk(verdict) if isinstance(x, ast.Name)]
            for nm in {v for v in vnames if vnames.count(v) > idx.count(v)} & lnames:
                figs.extend(_resolves_to_lits(nm, asg, forb, src))
            figs = sorted({x.lstrip('-') for x in figs if x.lstrip('-') not in ('0', '1')})
            if not figs:
                continue
            if home and home in tex and all(_in_tex(x, tex[home]) for x in figs):
                where = 'IN-PAPER'
            elif all(any(_in_tex(x, t) for t in tex.values()) for x in figs):
                where = 'IN-OTHER-TEX' if home else 'IN-SOME-TEX'
            elif any(any(_in_tex(x, t) for t in tex.values()) for x in figs):
                where = 'PARTLY-IN-TEX'
            else:
                where = 'IN-NO-TEX'
            out.append(dict(receipt=os.path.relpath(f, root), site=f'{n.lineno}:{n.col_offset}', read=reads,
                            where=where, figs=figs, label=' '.join(ltext.split())[:110]))
    out.sort(key=lambda r: (r['receipt'], tuple(int(x) for x in r['site'].split(':'))))
    return out


def report_unread_figure(rows):
    from collections import Counter
    c = Counter((r['read'], r['where']) for r in rows)
    print(f'\n  UNREAD-FIGURE: {len(rows)} site(s) in {len({r["receipt"] for r in rows})} receipt(s)   '
          f'{dict(sorted((f"{a}/{b}", v) for (a, b), v in c.items()))}')
    for r in rows:
        print(f'    [UNREAD-FIGURE][{r["read"]}][{r["where"]}] {r["receipt"]}:{r["site"]}  '
              f'{{{",".join(r["figs"][:6])}}}  {json.dumps(r["label"], ensure_ascii=False)}')


# ================================================================ ROUNDING-BOUNDARY (r7153+70.1)
# ⛭ A VERDICT DECIDED BY A ROUNDING BOUNDARY RATHER THAN BY THE QUANTITY (66, r7153 ⌗): `round(x, n) == L`, or
#   `abs(x - L) < T` with T half a unit in the n-th decimal.  Such a check CAN fail -- and whether it does is a coin
#   flip on the last bit when x sits at the midpoint (P15's ell = 2 ratio straddled 0.9255 by 6e-7: it passed on one
#   quadrature grid and failed on the other while the ratio moved by 8e-7).  The STATIC half is here; where x sits
#   needs the receipt RUN, and `computations/beyond_the_wall/r7153_70_rounding_boundary/` does that on the receipts
#   this selects.
def _half_unit(t):
    """n if t is half a unit in the n-th decimal (5e-(n+1)), else None"""
    import math
    try:
        t = float(t)
    except (TypeError, ValueError):
        return None
    if t <= 0:
        return None
    n = math.log10(2 * t)
    k = round(n)
    return -k if abs(n - k) < 1e-9 and k <= 0 else None


def rounding_boundary(root, files=None):
    out = []
    files = files or sorted(glob.glob(os.path.join(root, 'receipts', '**', '*.py'), recursive=True))
    for f in files:
        try:
            src = open(f, encoding='utf-8', errors='replace').read()
            tree = ast.parse(src)
        except SyntaxError:
            continue
        _asg, fns = _defs(tree)
        seen = set()
        for v in _verdicts(tree, fns, src):
            for n in ast.walk(v):
                if not (isinstance(n, ast.Compare) and len(n.ops) == 1) or id(n) in seen:
                    continue
                seen.add(id(n))
                a, b, op = n.left, n.comparators[0], n.ops[0]
                site = dict(receipt=os.path.relpath(f, root), site=f'{n.lineno}:{n.col_offset}',
                            text=' '.join((_seg(src, n) or '').split())[:140])
                if isinstance(op, ast.Eq):
                    for x in (a, b):
                        if (isinstance(x, ast.Call) and isinstance(x.func, ast.Name) and x.func.id == 'round'
                                and len(x.args) == 2):
                            out.append(dict(site, form='ROUND', n=_seg(src, x.args[1])))
                            break
                elif isinstance(op, (ast.Lt, ast.LtE)):
                    if (isinstance(a, ast.Call) and ST.fname(a) == 'abs' and len(a.args) == 1
                            and isinstance(a.args[0], ast.BinOp) and isinstance(a.args[0].op, ast.Sub)):
                        try:
                            t = eval(compile(ast.Expression(b), '<t>', 'eval'), {'__builtins__': {}})
                        except Exception:
                            continue
                        k = _half_unit(t)
                        # ⛭ T must be half a unit in the LITERAL's own last printed digit -- `abs(x - 0.926) < 5e-4`
                        #   is the rounding check `round(x, 3) == 0.926`; `abs(x - 924.28) < 0.5` is a tolerance that
                        #   merely happens to be a half (the first draft took both: 200 sites, most of them the second)
                        lits = []
                        for y in (a.args[0].left, a.args[0].right):
                            z = y.operand if isinstance(y, ast.UnaryOp) and isinstance(y.op, ast.USub) else y
                            if isinstance(z, ast.Constant) and isinstance(z.value, float):
                                txt = (_seg(src, z) or '').lower()
                                if 'e' not in txt:
                                    lits.append(len(txt.split('.')[1]) if '.' in txt else 0)
                        if k is not None and k in lits:
                            out.append(dict(site, form='HALF-UNIT', n=str(k)))
    out.sort(key=lambda r: (r['receipt'], tuple(int(x) for x in r['site'].split(':'))))
    return out


def report_rounding_boundary(rows):
    from collections import Counter
    c = Counter(r['form'] for r in rows)
    print(f'\n  ROUNDING-BOUNDARY: {len(rows)} site(s) in {len({r["receipt"] for r in rows})} receipt(s)   {dict(c)}')
    for r in rows:
        print(f'    [ROUNDING-BOUNDARY][{r["form"]}][n={r["n"]}] {r["receipt"]}:{r["site"]}  {r["text"]}')


def report_quote(rows):
    print(f'\n  QUOTE-PIN: {len(rows)} site(s) in {len({r["receipt"] for r in rows})} receipt(s)')
    for r in rows:
        print(f'    [QUOTE-PIN][{r["target"]}][{r["tier"]}][{r["flags"]}] {r["receipt"]}:{r["site"]}  '
              f'{json.dumps(r["lit"], ensure_ascii=False)}')


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
import importlib.util, os
_sp = importlib.util.spec_from_file_location("inst", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                             "computations", "inst_mod.py"))
_m = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(_m)
assert abs(_m.RD / 7.5 - 1) < 0.2                     # read through an IMPORTED instrument: must NOT flag
ppp = 2 * np.pi * (3 * 260 - 1) / (2000 - 12)
assert abs(ppp - 2.4621) < 0.01                       # arithmetic on constants, CONSTANT: must NOT flag
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

_SEED_QUOTE = r'''
import os, re
P15 = os.path.join("corpus", "CR_cosmology.tex")
def body_of(path):
    return open(path, encoding="utf-8").read()
b15 = body_of(P15)
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, ok))
    print("PASS" if ok else "FAIL", name)
gate("label", "as a conjecture and do not claim it" in b15)          # PLANTED pin: a paper sentence
_STATE = "the demonstration is owed here"
gate(f"label {_STATE in b15}", _STATE in b15)                        # PLANTED pin: through a named literal
assert "carried across unaltered" in b15.lower()                     # PLANTED pin: through .lower()
assert b15.find("one boundary-condition supplier") >= 0              # PLANTED pin: find() >= 0
_A = "stated as open" in b15                                         # PLANTED pin, ALT: one of two states
_B = "eq:shape-invariant" in b15                                     # PLANTED pin, ALT: the other, still pinned
gate("either state", _A or _B)                                       # (the site is the test, not the call)
assert "withdrawn sentence about the seam" not in b15                # absence: must NOT flag
D = {"a key in a dict": 1}
assert "a key in a dict" in D                                        # not a file read: must NOT flag
out = "computed here " + str(3)
assert "computed here 3" in out                                      # the receipt's own string: must NOT flag
SRC = open(os.path.abspath(__file__)).read()
assert "planted pin" in SRC.lower()                                  # its own source, a self-pin: must NOT flag
'''


def seed():
    tmp = tempfile.mkdtemp(prefix='mut_seed_')
    ok = True
    try:
        d = os.path.join(tmp, 'receipts', 'SEED')
        os.makedirs(d)
        os.makedirs(os.path.join(d, 'corpus'))
        subprocess.run([sys.executable, '-c', _SEED_DATA], cwd=d, check=True)
        os.makedirs(os.path.join(d, 'computations'))
        open(os.path.join(d, 'computations', 'inst_mod.py'), 'w').write('import math\nRD = 7.5 * math.cos(0.0)\n')
        os.environ['MUTATE_INSTRUMENT_DIRS'] = os.path.join(d, 'computations')
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
        open(os.path.join(d, 'Q1_quote.py'), 'w').write(_SEED_QUOTE)
        rows = quote(d, [os.path.join(d, 'Q1_quote.py')])
        got = sorted(int(r['site'].split(':')[0]) for r in rows)
        want = sorted(i + 1 for i, l in enumerate(_SEED_QUOTE.split('\n')) if 'PLANTED pin' in l)
        alt = sorted(int(r['site'].split(':')[0]) for r in rows if 'ALT' in r['flags'])
        want_alt = [i + 1 for i, l in enumerate(_SEED_QUOTE.split('\n')) if 'PLANTED pin, ALT' in l]
        print(f'  QUOTE   flagged QUOTE-PIN at lines {got}; planted {want}; ALT at {alt}   '
              f'{"OK" if got == want and alt == want_alt else "MISS"}')
        ok &= got == want and alt == want_alt
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
    ap.add_argument('--quote', action='store_true')
    ap.add_argument('--cannot-fail', action='store_true')
    ap.add_argument('--unread-figure', action='store_true')
    ap.add_argument('--rounding-boundary', action='store_true')
    ap.add_argument('--files', nargs='*', help='with --prose / --quote: only these receipt files')
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
    if a.cannot_fail:
        rows = cannot_fail(a.root, [os.path.abspath(f) for f in a.files] if a.files else None, ubiq_root=ROOT)
        report_cannot_fail(rows)
        rc |= bool(rows)
    if a.rounding_boundary:
        rows = rounding_boundary(a.root, [os.path.abspath(f) for f in a.files] if a.files else None)
        report_rounding_boundary(rows)
        rc |= bool(rows)
    if a.unread_figure:
        rows = unread_figure(a.root, [os.path.abspath(f) for f in a.files] if a.files else None, tex_root=ROOT)
        report_unread_figure(rows)
        rc |= bool(rows)
    if a.quote:
        rows = quote(a.root, [os.path.abspath(f) for f in a.files] if a.files else None)
        report_quote(rows)
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

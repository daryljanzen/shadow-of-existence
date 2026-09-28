#!/usr/bin/env python3
"""sweep_tolerances.py -- ** PO-60's THIRD CLASS: A TOLERANCE CALIBRATED ON ONE MACHINE CERTIFIES THAT MACHINE. **

Built r6961+70.2 by node 70, on node 66's r6959 order.  WIRED r6977+70.1: per push on the receipts
`receipt_scope.py --scope tolerance` names (`--from`), and whole in the monthly backstop.

** r6977+70.1, FOR THE WIRING. **  `--from LIST` probes only the listed receipts.  `--compare` passes a
FLAG (never a FLIP) at a site recorded in receipts/TOLERANCE_JUDGED.json ONLY while the receipt's git blob
is the one it was judged on -- a judgement lapses the moment the receipt changes.  ⛔ And a relative
`--probe` directory silently recorded nothing: the child runs from the receipt's own directory, so its log
landed there and every receipt was filed `rc=None, 0 sites` -- a sweep of nothing that reads as clean.  The
directory is made absolute now.  *(The r6961 sweep used absolute paths; its numbers stand.)*

** THE CLASS (r6947). **  A check compared a closed form against a diagonalization and read 2.5e-9 on
the seat that wrote it and 5.1e-7 on the seat that gated it, against a threshold of 1e-7.  Neither was
physics: the second difference carried epsilon/lam^2, noise whose size is set by the linear-algebra
build.  It is invisible to reading and to the red count until a different build runs it.

** TWO PASSES, THE CHEAP ONE FIRST. **
  --static     (seconds)  every numeric comparison in an ASSERTION CONTEXT, classified from source:
                 EXACT       `==` / `!=` -- exact if its operands are
                 PREDICTION  a float against a stated value: abs(X - V) < T, isclose(X, V)
                 THRESHOLD   a float against a bare small number: abs(X) < T, max|..| < T, X < 1e-3
                 RANGE       an order or bracket on a quantity
               It bounds the class from ABOVE and names the population the perturbation must cover.
  --probe OUT  (a suite run) every registered receipt run as the runner runs it, with EVERY comparison
               instrumented: operand TYPES and values recorded per site.  Types settle what source
               cannot -- whether an `==` compared integers, rationals, sympy objects or floats.
  --compare A B  the perturbation: two probe runs of the same tree on DIFFERENT LINEAR-ALGEBRA BUILDS
               (thread count and OPENBLAS_CORETYPE -- numpy's OpenBLAS is DYNAMIC_ARCH, so both change
               round-off without touching a receipt; see WHICH BUILDS below).  For every passing float check
               `err < tol`, it measures how far err MOVED between builds and how much HEADROOM tol
               leaves over the larger of the two:
                 FLAGGED   err moved by more than 10% (it is reading round-off, not convergence)
                           AND headroom < 1e3 (a build-to-build swing of that size can cross it --
                           r6947's swing was 200x); or the check PASSED on one build and FAILED on
                           the other
                 not flagged: err identical across builds (converged or truncation-dominated -- a
                           genuinely approximate claim is entitled to thin headroom); or it moves
                           with headroom >= 1e3 (round-off with real margin is not a defect)

** WHICH BUILDS, MEASURED ON THE REAL INSTANCE RATHER THAN CHOSEN. **  r6946's receipt, run here on
every OpenBLAS kernel at one and at four threads: the THREAD COUNT reproduces the whole historical
spread -- 3.4e-7 at one thread (red, as on the gating seat) and 2.5e-9 at four (the authoring seat's
exact number) -- while switching the kernel at one thread moves it by nothing.  The runner pins ONE
thread and an interactive author runs on all cores, which is how the instance happened.  So the
perturbation is run against TWO builds: four threads (the author's side) and the Prescott kernel at two
threads (a different machine's kernels), each compared with the runner's single-thread default.

** WHY THE PERTURBATION IS THE BUILD AND NOT A PARAMETER. **  The order names the hard part: the step,
truncation or seed is a LOCAL variable, not declared.  Moving the BLAS kernel needs no parameter at
all, reaches EVERY receipt, and is the perturbation r6947 actually suffered.  It detects a floor; it
does not measure MONOTONICITY in a step, which needs the parameter -- see FOR_66_FROM_70.md for the
fraction of flagged sites where that parameter could be located and what it showed.

** THE MEASUREMENT (r6961+70.2, 868 registered, three instrumented suite runs). **
  * --static: 8,220 numeric assertions in 796 receipts.  The probe types them: 3,237 compare FLOATS,
    4,079 are exact or symbolic, 681 are not numeric, 220 sit on unexecuted branches.  All 868 pass
    instrumented, so the instrumentation changes nothing.
  * --compare, on the pre-repair tree, over both builds: 7 sites flagged in 4 receipts, EVERY ONE READ.
      TRUE 5  -- P10_no_state... FLIPPED (green at one thread, red on Prescott/two threads: a round-off
                 number against a round-off "floor");  P16_freezeout_trev_toy's endpoint pin (the
                 fourth digit was the solver's step sequence);  P10_the_second_logarithm... x3
                 (headroom 2.4-13.6 over a floor-dominated error)
      FALSE 2 -- P10_the_commutator_bound... x2: the threshold is a floor measured on the RUNNING
                 machine, so a larger floor makes the check stricter.  Structurally indistinguishable.
    ** Precision 5/7 by site, 3/4 by receipt. **  Seven more sites sat below 1e-13 -- each read, each
    an identity in floating point with bounded cancellation -- and are counted, not flagged.
  * RECALL on the real instance: r6946's shipped receipt reads 3.4e-7 at one thread and 2.5e-9 at four
    -- a pass/fail flip across its 1e-7, caught.  The seed is caught.  Nothing wider is claimed.
  ⚠ WHAT IT CANNOT SEE: a machine difference outside thread count and CPU kernel (another LAPACK,
    another compiler); a floor-reader whose error happens not to move between these builds; and any
    threshold that is itself a measured floor, which it flags whether or not it is a defect.

  --from LIST  (with --probe) only the receipts listed, one per line
  --judged F   the judged-sites file (default receipts/TOLERANCE_JUDGED.json)
  --seed       the both-ways seeding: a second difference at a step far below its balance (planted),
               a converged eigenvalue with 1e5 headroom and a truncation-dominated finite difference
               with thin headroom (both legitimate).  Exit 0 iff exactly the planted one is flagged.
"""
import argparse
import ast
import atexit
import collections
import glob
import json
import math
import operator
import os
import re
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction

HERE = os.path.abspath(__file__)
MOVED, HEADROOM, EPS_LEVEL = 0.10, 1e3, 1e-13


_CHECKY = re.compile(r'(^|_)(check|chk|ok|expect|verify|require|claim|record|test|assert\w*|must|ensure)$',
                     re.I)


def num(n):
    """a numeric literal (incl. unary minus, 1e-7, 10**-7, a/b of literals) -> float, else None"""
    try:
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
            return float(n.value)
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.USub, ast.UAdd)):
            v = num(n.operand)
            return None if v is None else (-v if isinstance(n.op, ast.USub) else v)
        if isinstance(n, ast.BinOp) and isinstance(n.op, (ast.Pow, ast.Mult, ast.Div)):
            a, b = num(n.left), num(n.right)
            if a is None or b is None:
                return None
            return a ** b if isinstance(n.op, ast.Pow) else (a * b if isinstance(n.op, ast.Mult) else a / b)
    except Exception:
        return None
    return None


def fname(call):
    f = call.func
    return f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else '')


def is_abs(n):
    return isinstance(n, ast.Call) and fname(n) in ('abs', 'fabs', 'absolute')


def residual_like(n):
    """abs(X) with X not a difference, or max/norm/amax of something"""
    if is_abs(n) and n.args:
        a = n.args[0]
        return not (isinstance(a, ast.BinOp) and isinstance(a.op, ast.Sub))
    if isinstance(n, ast.Call) and fname(n) in ('max', 'amax', 'norm', 'nanmax'):
        return True
    return False


def diff_against(n):
    """abs(X - V) or abs(X/V - 1): return V's node, else None"""
    if is_abs(n) and n.args:
        a = n.args[0]
        if isinstance(a, ast.BinOp) and isinstance(a.op, ast.Sub):
            return a.right
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div) and is_abs(n.left):
        return diff_against(n.left)
    return None


def classify(cmp):
    ops = [type(o).__name__ for o in cmp.ops]
    operands = [cmp.left] + list(cmp.comparators)
    if all(o in ('Eq', 'NotEq') for o in ops):
        return 'EXACT'
    if not any(o in ('Lt', 'LtE', 'Gt', 'GtE') for o in ops):
        return None
    if len(operands) == 3:
        return 'RANGE'
    x, t = (operands[0], operands[1]) if ops[0] in ('Lt', 'LtE') else (operands[1], operands[0])
    tv = num(t)
    v = diff_against(x)
    if v is not None:
        vv = num(v)
        if vv == 0.0:
            return 'THRESHOLD'
        return 'PREDICTION'
    if residual_like(x):
        return 'THRESHOLD'
    if tv is not None and 0 < tv <= 1e-3:
        return 'THRESHOLD'
    return 'RANGE'


def contexts(tree):
    """yield (node, context) for every Compare / isclose call in an assertion context"""
    out = []
    seen = set()

    def take(root, ctx):
        for n in ast.walk(root):
            if id(n) in seen:
                continue
            if isinstance(n, ast.Compare):
                seen.add(id(n))
                out.append((n, ctx))
            elif isinstance(n, ast.Call) and fname(n) in ('isclose', 'allclose', 'assert_allclose',
                                                          'assert_almost_equal'):
                seen.add(id(n))
                out.append((n, ctx))

    for n in ast.walk(tree):
        if isinstance(n, ast.Assert):
            take(n.test, 'assert')
        elif isinstance(n, ast.Call) and _CHECKY.search(fname(n) or ''):
            for a in list(n.args) + [k.value for k in n.keywords]:
                take(a, 'check')
        elif isinstance(n, ast.If):
            body = ast.dump(ast.Module(body=n.body, type_ignores=[]))
            if re.search(r"(?i)'[^']*(fail|bad)[^']*'", body):
                take(n.test, 'if-fail')
    return out


def iscl(call):
    args = call.args
    v = args[1] if len(args) > 1 else None
    if v is not None and num(v) == 0.0:
        return 'THRESHOLD'
    return 'PREDICTION'


def scan(root):
    rows = []
    for f in sorted(glob.glob(os.path.join(root, 'receipts', '**', '*.py'), recursive=True)):
        try:
            src = open(f, encoding='utf-8', errors='replace').read()
            tree = ast.parse(src)
        except SyntaxError:
            continue
        rel = os.path.relpath(f, root)
        for n, ctx in contexts(tree):
            k = iscl(n) if isinstance(n, ast.Call) else classify(n)
            if k is None:
                continue
            rows.append({'file': rel, 'site': f'{n.lineno}:{n.col_offset}', 'ctx': ctx, 'class': k})
    return rows


_OPS = {'Lt': operator.lt, 'LtE': operator.le, 'Gt': operator.gt, 'GtE': operator.ge,
        'Eq': operator.eq, 'NotEq': operator.ne}
SITES = {}


def _kind(v):
    t = type(v)
    mod = t.__module__ or ''
    if isinstance(v, bool):
        return 'bool', None
    if isinstance(v, int):
        return 'int', float(v) if abs(v) < 1e300 else None
    if isinstance(v, Fraction):
        return 'fraction', float(v)
    if isinstance(v, float):
        return 'float', v
    if mod.startswith('numpy'):
        try:
            import numpy as np
            if isinstance(v, np.ndarray):
                if v.size == 1:
                    return f'nd:{v.dtype.kind}', float(v.reshape(-1)[0]) if v.dtype.kind in 'fiu' else None
                return f'nd:{v.dtype.kind}[{v.size}]', None
            if isinstance(v, np.bool_):
                return 'bool', None
            if isinstance(v, np.integer):
                return 'int', float(v)
            if isinstance(v, np.floating):
                return 'float', float(v)
            if isinstance(v, np.complexfloating):
                return 'complex', None
        except Exception:
            return 'numpy?', None
    if mod.startswith('sympy'):
        try:
            if getattr(v, 'is_Float', False):
                return 'sympy_float', float(v)
            if getattr(v, 'is_Number', False):
                return 'sympy_exact', float(v)
            return 'sympy_expr', None
        except Exception:
            return 'sympy_expr', None
    if mod.startswith('mpmath'):
        try:
            return 'mpmath', float(v)
        except Exception:
            return 'mpmath', None
    if isinstance(v, complex):
        return 'complex', None
    if isinstance(v, str):
        return 'str', None
    return t.__name__, None


def __po60_cmp(site, first, ops, rest):
    left = first
    res = True
    for op, th in zip(ops, rest):
        right = th()
        res = _OPS[op](left, right)
        try:
            s = SITES.get(site)
            if s is None:
                s = SITES[site] = {'n': 0, 'pass': 0, 'types': [], 'op': op, 'vals': []}
            s['n'] += 1
            kl, vl = _kind(left)
            kr, vr = _kind(right)
            tk = f'{kl}{op}{kr}'
            if tk not in s['types'] and len(s['types']) < 6:
                s['types'].append(tk)
            try:
                ok = bool(res)
            except Exception:
                ok = None
            if ok:
                s['pass'] += 1
            if vl is not None and vr is not None and len(s['vals']) < 40:
                s['vals'].append([vl, vr, ok])
        except Exception:
            pass
        try:
            if not res:
                return res
        except Exception:
            return res
        left = right
    return res


class _T(ast.NodeTransformer):
    def visit_Compare(self, node):
        self.generic_visit(node)
        names = [type(o).__name__ for o in node.ops]
        if not all(n in _OPS for n in names):
            return node
        rest = [ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[],
                                              kw_defaults=[], kwarg=None, defaults=[]), body=c)
                for c in node.comparators]
        call = ast.Call(func=ast.Name(id='__po60_cmp', ctx=ast.Load()),
                        args=[ast.Constant(f'{node.lineno}:{node.col_offset}'), node.left,
                              ast.List(elts=[ast.Constant(n) for n in names], ctx=ast.Load()),
                              ast.List(elts=rest, ctx=ast.Load())], keywords=[])
        return ast.copy_location(call, node)

    def visit_ClassDef(self, node):
        return node        # a lambda in a class body cannot see class-level names: leave classes alone


def probe_one(LOG, TARGET):
    """Run ONE receipt in this process, from the cwd, with every comparison instrumented."""
    def _dump():
        with open(LOG, 'w') as fh:
            json.dump({'receipt': os.path.abspath(TARGET), 'rc': _RC[0], 'sites': SITES}, fh)
    _RC = [None]
    atexit.register(_dump)
    src = open(TARGET, encoding='utf-8').read()
    tree = _T().visit(ast.parse(src, filename=os.path.abspath(TARGET)))
    ast.fix_missing_locations(tree)
    code = compile(tree, os.path.abspath(TARGET), 'exec')
    sys.argv = [TARGET]
    sys.path.insert(0, os.path.dirname(os.path.abspath(TARGET)))
    g = {'__name__': '__main__', '__file__': os.path.abspath(TARGET), '__builtins__': __builtins__,
         '__po60_cmp': __po60_cmp}
    try:
        exec(code, g)
        _RC[0] = 0
    except SystemExit as e:
        _RC[0] = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
        raise
    except BaseException:
        _RC[0] = 1
        raise


# ------------------------------------------------------------------------------ the perturbation
def _err_tol(site, v):
    """(err, tol) for a float check err < tol, else None"""
    l, r, ok = v
    op = site['op']
    if op in ('Lt', 'LtE'):
        err, tol = l, r
    elif op in ('Gt', 'GtE'):
        err, tol = r, l
    else:
        return None
    if not any(t.startswith(('float', 'nd:f', 'sympy_float', 'mpmath')) for t in site['types']):
        return None
    if tol is None or err is None or not (tol > 0) or err < 0 or not math.isfinite(err):
        return None
    return err, tol


def compare(a_dir, b_dir):
    out = []
    for pa in sorted(glob.glob(os.path.join(a_dir, '*.json'))):
        pb = os.path.join(b_dir, os.path.basename(pa))
        if not os.path.exists(pb):
            continue
        A, B = json.load(open(pa)), json.load(open(pb))
        for sid, sa in A.get('sites', {}).items():
            sb = B.get('sites', {}).get(sid)
            if sb is None:
                continue
            worst = None
            for va, vb in zip(sa['vals'], sb['vals']):
                ea, eb = _err_tol(sa, va), _err_tol(sb, vb)
                if ea is None or eb is None:
                    continue
                # ** a check that PASSES on one build and FAILS on the other is the class at its
                #    sharpest, whether or not its threshold is a constant -- a threshold that is itself
                #    a measured round-off floor moves too (r6930's VAR_FLOOR). **
                if va[2] is not None and vb[2] is not None and bool(va[2]) != bool(vb[2]):
                    worst = ('FLIP', ea, eb, min(ea[1], eb[1]) / max(ea[0], eb[0], 1e-300), 1.0)
                    break
                if ea[1] != eb[1]:
                    continue
                m = max(ea[0], eb[0])
                if m == 0:
                    continue
                # ** an error at the precision floor itself -- below 1e-13, a few hundred epsilon --
                #    moves between builds by construction and cannot grow by the factor it would need
                #    without an amplifying step.  Read at r6961+70.2: all seven such sites were
                #    identities evaluated in floating point with bounded cancellation.  Counted
                #    separately, not flagged. **
                if m < EPS_LEVEL:
                    mv, hd = abs(ea[0] - eb[0]) / m, ea[1] / m
                    if mv > MOVED and hd < HEADROOM and (worst is None or
                                                        worst[0] == 'EPS' and hd < worst[3]):
                        worst = ('EPS', ea, eb, hd, mv)
                    continue
                moved = abs(ea[0] - eb[0]) / m
                head = ea[1] / m
                if moved > MOVED and head < HEADROOM:
                    if worst is None or worst[0] == 'EPS' or head < worst[3]:
                        worst = ('FLAG', ea, eb, head, moved)
            if worst:
                out.append({'receipt': os.path.basename(pa)[:-5], 'site': sid, 'kind': worst[0],
                            'err_a': worst[1][0], 'err_b': worst[2][0], 'tol': worst[1][1],
                            'headroom': round(worst[3], 1), 'moved': round(worst[4], 2)})
    return out


def not_swept(a_dir, b_dir):
    """⛔ r6977+70.1: every receipt whose probe did not run to exit 0 on BOTH builds.  The first backstop
    dispatch ran without numpy (its install had failed), every receipt died on import, and `compare` --
    which only looks at sites that were recorded -- read "0 flagged" off 871 empty probes.  A comparison of
    nothing is not a clean result, so this is reported and the exit code is 2."""
    out = []
    for pa in sorted(glob.glob(os.path.join(a_dir, '*.json'))):
        pb = os.path.join(b_dir, os.path.basename(pa))
        A = json.load(open(pa))
        B = json.load(open(pb)) if os.path.exists(pb) else {'rc': 'missing'}
        bad = [f'{n} rc={d.get("rc")}' + (' timeout' if d.get('timeout') else '')
               for n, d in (('A', A), ('B', B)) if d.get('rc') != 0]
        if bad:
            out.append((os.path.basename(pa)[:-5], ', '.join(bad)))
    return out


def _run(root, rel, budget, out, env_extra):
    key = rel.replace('/', '_')
    log = os.path.join(out, key + '.json')
    if os.path.exists(log):
        return
    d, f = os.path.split(os.path.join(root, rel))
    env = dict(os.environ, NODE='ci', **env_extra)
    try:
        subprocess.run([sys.executable, HERE, '--probe-one', log, f], cwd=d, env=env,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=budget)
    except subprocess.TimeoutExpired:
        pass
    if not os.path.exists(log):
        with open(log, 'w') as fh:
            json.dump({'receipt': rel, 'rc': None, 'sites': {}, 'timeout': True}, fh)


def probe_all(root, out, jobs, env_extra, only=None):
    import importlib.util
    from concurrent.futures import ThreadPoolExecutor
    spec = importlib.util.spec_from_file_location('rar', os.path.join(root, 'scripts',
                                                                      'run_all_receipts.py'))
    m = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, ['x']
    spec.loader.exec_module(m)
    sys.argv = argv
    files, _ = m.registered()
    if only is not None:                  # a scoped run: the receipts `receipt_scope` named, nothing else
        files = [f for f in files if os.path.relpath(f, root) in only]
    out = os.path.abspath(out)            # the child runs from the receipt's directory: a relative log lands there
    os.makedirs(out, exist_ok=True)
    with ThreadPoolExecutor(max_workers=jobs) as ex:
        list(ex.map(lambda f: _run(root, os.path.relpath(f, root), 2 * max(900, m.budget(f, 600)),
                                   out, env_extra), files))
    return len(files)


# ------------------------------------------------------------------------------ judged sites
# ⛭ r6977+70.1, for the SCOPED job.  Two sites were read at r6961+70.2 and judged FALSE (a threshold that
#   is a floor measured on the running machine, which recalibrates itself).  Wired per push, they would
#   fail every push that scopes their receipt, and a gate that is red for a known reason is a gate that
#   gets ignored.  ** So a judgement is recorded -- and it is bound to the receipt's git BLOB: the moment the
#   receipt changes, the judgement LAPSES and the flag counts again until someone reads it. **  A FLIP is
#   never judged away: a check that passes on one build and fails on another is the class itself.
JUDGED = os.path.join('receipts', 'TOLERANCE_JUDGED.json')


def split_judged(flags, path, root):
    try:
        J = json.load(open(path))['sites']
    except (OSError, ValueError, KeyError):
        return [], []
    blob = {}
    for l in subprocess.run(['git', 'ls-files', '-s', 'receipts'], cwd=root, capture_output=True,
                            text=True).stdout.split('\n'):
        if '\t' in l:
            blob[l.split('\t', 1)[1].replace('/', '_')] = l.split()[1]
    judged, lapsed = [], set()
    for r in flags:
        key = r['receipt'] + ('' if r['receipt'].endswith('.py') else '.py')
        for rec, j in J.items():
            if rec.replace('/', '_') != key:
                continue
            if not blob.get(key, '').startswith(j['sha']):
                lapsed.add((rec, f"judged on blob {j['sha']}, now {blob.get(key, 'absent')[:12]}"))
            elif r['kind'] == 'FLAG' and r['site'] in j['sites']:
                judged.append(r)
    return judged, sorted(lapsed)


# ------------------------------------------------------------------------------ seeding
_SEED = r'''
import numpy as np
rng = np.random.default_rng(7)
A = rng.standard_normal((120, 120)); A = A + A.T
B = rng.standard_normal((120, 120)); B = B + B.T
def e0(lam): return np.linalg.eigvalsh(A + lam * B)[0]
# PLANTED: a second difference at a step far below the balance -- reads round-off
lam = 3e-7
d2 = (e0(lam) + e0(-lam) - 2 * e0(0.0)) / lam**2
d2_ref = (e0(1e-2) + e0(-1e-2) - 2 * e0(0.0)) / 1e-4
err_floor = abs(d2 / d2_ref - 1)
# LEGIT 1: converged, with real headroom
Q, _ = np.linalg.qr(rng.standard_normal((50, 50)))
w = np.linalg.eigvalsh(Q @ np.diag(np.arange(1.0, 51.0)) @ Q.T)
err_conv = abs(w[0] - 1.0)
# LEGIT 2: genuinely approximate -- truncation-dominated, deterministic, thin headroom
h = 1e-2
fd = (np.sin(1 + h) - np.sin(1 - h)) / (2 * h)
err_trunc = abs(fd - np.cos(1.0))
print(err_floor, err_conv, err_trunc)
assert err_floor < 0.5
assert err_conv < 1e-8
assert err_trunc < 3e-5
'''


def seed():
    tmp = tempfile.mkdtemp(prefix='po60c_seed_')
    src = _SEED.split('\n')
    try:
        os.makedirs(os.path.join(tmp, 'receipts', 'SEED'))
        with open(os.path.join(tmp, 'receipts', 'SEED', 'S1_seed.py'), 'w') as fh:
            fh.write(_SEED)
        a, b = os.path.join(tmp, 'a'), os.path.join(tmp, 'b')
        os.makedirs(a)
        os.makedirs(b)
        rel = os.path.join('receipts', 'SEED', 'S1_seed.py')
        one = {'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'}
        _run(tmp, rel, 120, a, one)
        _run(tmp, rel, 120, b, dict(one, OPENBLAS_CORETYPE='Prescott'))
        flags = compare(a, b)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    lines = {int(r['site'].split(':')[0]) for r in flags if r['kind'] in ('FLAG', 'FLIP')}
    planted = next(i + 1 for i, l in enumerate(src) if l.startswith('assert err_floor'))
    legit = {i + 1 for i, l in enumerate(src) if l.startswith(('assert err_conv', 'assert err_trunc'))}
    for r in flags:
        print('    flagged', r)
    ok_p = planted in lines
    ok_l = not (lines & legit)
    print(f'  planted floor-reader flagged              : {ok_p}')
    print(f'  converged and truncation-dominated passed : {ok_l}')
    return 0 if ok_p and ok_l else 1


def main():
    if len(sys.argv) == 4 and sys.argv[1] == '--probe-one':
        probe_one(sys.argv[2], sys.argv[3])
        return 0
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(HERE)))
    ap.add_argument('--static', action='store_true')
    ap.add_argument('--probe')
    ap.add_argument('--coretype')
    ap.add_argument('--threads', default='1')
    ap.add_argument('--jobs', type=int, default=4)
    ap.add_argument('--compare', nargs=2)
    ap.add_argument('--from', dest='frm', help='probe only the receipts listed in this file, one per line')
    ap.add_argument('--judged', default=os.path.join(os.path.dirname(os.path.dirname(HERE)), JUDGED),
                    help='sites read and judged FALSE, each bound to the receipt blob it was judged on')
    ap.add_argument('--seed', action='store_true')
    a = ap.parse_args()
    if a.seed:
        print('\n  sweep_tolerances --seed: does a build perturbation flag a floor and pass a convergence?\n')
        return seed()
    if a.static:
        rows = scan(a.root)
        c = collections.Counter(r['class'] for r in rows)
        print(f'\n  NUMERIC ASSERTIONS -- {len(rows)} in {len({r["file"] for r in rows})} receipt(s)')
        for k in ('EXACT', 'PREDICTION', 'THRESHOLD', 'RANGE'):
            print(f'    {k:10} {c.get(k, 0)}')
        return 0
    if a.probe:
        env = {'OPENBLAS_NUM_THREADS': a.threads, 'OMP_NUM_THREADS': a.threads,
               'MKL_NUM_THREADS': a.threads}
        if a.coretype:
            env['OPENBLAS_CORETYPE'] = a.coretype
        only = {l.strip() for l in open(a.frm) if l.strip()} if a.frm else None
        n = probe_all(os.path.abspath(a.root), a.probe, a.jobs, env, only)
        print(f'  probed {n} registered receipt(s) into {a.probe}')
        return 0
    if a.compare:
        rows = compare(*a.compare)
        unswept = not_swept(*a.compare)
        flags = [r for r in rows if r['kind'] in ('FLAG', 'FLIP')]
        judged, lapsed = split_judged(flags, a.judged, os.path.abspath(a.root))
        flags = [r for r in flags if r not in judged]
        eps = [r for r in rows if r['kind'] == 'EPS']
        print(f'\n  BUILD PERTURBATION -- {len(flags)} flagged site(s); {len(eps)} at the precision '
              f'floor (< {EPS_LEVEL:g}), counted and not flagged')
        for r in flags:
            print('  ⛔', json.dumps(r))
        for r in eps:
            print('  ⌗', json.dumps(r))
        for r in judged:
            print('  ⌗ JUDGED FALSE, receipt unchanged since:', json.dumps(r))
        for rec, why in lapsed:
            print(f'  ⚠ judgement LAPSED for {rec}: {why} -- its flags above count until it is read again')
        if unswept:
            print(f'\n  ⛔ NOT A SWEEP OF {len(unswept)} RECEIPT(S): they did not run to exit 0 on both builds, so '
                  f'none of their comparisons was measured -- "0 flagged" says nothing about them.')
            for rec, why in unswept[:12]:
                print(f'      {why:28} {rec}')
            if len(unswept) > 12:
                print(f'      ... and {len(unswept) - 12} more')
            return 2
        return 1 if flags else 0
    ap.print_help()
    return 2


if __name__ == '__main__':
    raise SystemExit(main())

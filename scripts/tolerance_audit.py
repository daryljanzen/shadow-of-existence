#!/usr/bin/env python3
r"""tolerance_audit.py -- ** THE MUTATION HARNESS `Q5` SPECIFIED AND THE v1 PASS DECLINED TO BUILD. **

`NUMERICAL_ANALYSIS_LEDGER.md`, `Q5`, left open at r3616:

  > *"whether 688 `abs(...) < tol` assertions carry meaningful tolerances.  **That needs a mutation
  > harness, not a reading**, and building one is a larger instrument than a field bake should ship.
  > Recorded with the shape of the check it wants: mutate the asserted quantity by the tolerance and
  > require the assertion to fail."*

** WHAT IT DOES.  Two AST rewrites of every `abs(E) < T` site in a receipt, each run from the
receipt's OWN directory in a subprocess, exactly as `run_all_receipts.py` does: **

  * ** MARGIN ** -- `abs(E) < T`  ->  `_tolprobe(id, abs(E), T) < T`.  *Semantically identical; it
    records the ratio $\lvert E\rvert/T$ at every site the run actually reaches.*  ⇒ **This is the
    only way to learn which sites EXECUTE and how much room each one has.**
  * ** MUTATE-UP ** -- `abs(E) < T`  ->  `abs(E + K*T) < T` with `K=3`.  *Since $\lvert E\rvert<T$
    on a passing site, $\lvert E+3T\rvert \ge 2T > T$ at every one of them, so the comparison flips
    to False.*  ⇒ ** Catches the ASSERT shape: `assert abs(E) < T` / `check(..., abs(E) < T)`. **
  * ** MUTATE-DOWN ** -- `abs(E) < T`  ->  `abs(E) * 0 < T`, which flips the comparison to True.
    ⇒ ** Catches the GUARD shape: `if abs(E) < T: fail.append(...)`, where the FAILURE lives on the
    `<` branch and an upward kick can only silence it. **

⛔⛭⛭ *** THE SECOND DIRECTION EXISTS BECAUSE THE FIRST PASS REPORTED FOUR "DEFECTS" AND ALL FOUR
     WERE THE HARNESS'S OWN BLIND SPOTS. ***  *Up-mutation alone left four files exiting 0.  Read
     one at a time rather than counted: `L265`'s `abs(lv) < 3/4` is a THRESHOLD PREDICATE on an
     integer parameter, `P14_lambda_spectrum`'s `abs(lv) <= 4` is a DISPLAY FILTER choosing which
     rows to print, and `P15_which_coupling`'s two are GUARDS whose failure branch is the `<` side.*
  ** A one-sided mutation cannot test a two-sided guard, and `abs(E) < T` is not always a tolerance.
  Reporting the four as corpus defects would have been the instrument reporting its own limits as
  the corpus's. **

⛔ ** AND THAT IS A DIFFERENT QUESTION FROM THE ONE `Q5` ASKED, WHICH IS WHY BOTH RUNS ARE HERE. **
  *`Q5` asked whether the tolerances are "loose enough to pass anything".  The mutation cannot ask
  that -- it fires on every executed, enforced site by arithmetic, exact identities included.*
  ** What it CAN ask is whether the comparison is enforced at all, which is the receipt-layer form
  of the hollow assertion. **  *The margin run answers the looseness question instead, per site, by
  measurement.*  ⇒ *** Two instruments, two questions, and saying which is which is the whole of
  not overselling this. ***

⌗ ** A ratio of exactly 0.0 is an EXACT identity evaluated in floating point.  It is not a defect
and this harness must not report it as one **  -- `NUMERICAL_ANALYSIS_LEDGER.md` Pass A rows 4, 8,
9, 12 and 14 name that class in advance, before the harness existed.

Usage:
    python3 scripts/tolerance_audit.py --mode margin  [--only SUBSTR] [--timeout 120] [--jobs 4]
    python3 scripts/tolerance_audit.py --mode mutate  [...]
    python3 scripts/tolerance_audit.py --selftest      # the two controls, and nothing else
"""
import argparse
import ast
import json
import os
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:] = [p for p in sys.path if os.path.abspath(p or '.') != HERE]
ROOT = os.path.dirname(HERE)

KICK = 3.0          # multiples of the tolerance the mutation adds

PREAMBLE = '''
import os as _os, json as _json, atexit as _atexit
_TOLREC = []
def _tolmag(v):
    try:
        return float(abs(v))
    except Exception:
        pass
    try:
        import numpy as _np
        return float(_np.max(_np.abs(_np.asarray(v, dtype=float))))
    except Exception:
        return None
def _tolprobe(_sid, _v, _t):
    _TOLREC.append((_sid, _tolmag(_v), _tolmag(_t)))
    return _v
def _tolflush():
    _p = _os.environ.get('TOLAUDIT_OUT')
    if _p:
        with open(_p, 'a') as _f:
            _f.write(_json.dumps(_TOLREC) + chr(10))
_atexit.register(_tolflush)
'''


class Rewriter(ast.NodeTransformer):
    """rewrite every `abs(E) < T` / `abs(E) <= T`; `sites` records (lineno, col) in order"""

    def __init__(self, mode, path):
        self.mode, self.path, self.sites = mode, path, []

    def visit_Compare(self, node):
        self.generic_visit(node)
        if len(node.ops) != 1 or not isinstance(node.ops[0], (ast.Lt, ast.LtE)):
            return node
        L = node.left
        if not (isinstance(L, ast.Call) and getattr(L.func, 'id', '') == 'abs' and len(L.args) == 1):
            return node
        tol = node.comparators[0]
        sid = f'{os.path.relpath(self.path, ROOT)}:{node.lineno}'
        self.sites.append(sid)
        if self.mode == 'margin':
            node.left = ast.Call(func=ast.Name(id='_tolprobe', ctx=ast.Load()),
                                 args=[ast.Constant(value=sid), L, tol], keywords=[])
        elif self.mode == 'mutate':
            # abs(E)  ->  abs(E + KICK*T)     the comparison goes False
            L.args[0] = ast.BinOp(
                left=L.args[0], op=ast.Add(),
                right=ast.BinOp(left=ast.Constant(value=KICK), op=ast.Mult(), right=tol))
        else:
            # abs(E)  ->  abs(E) * 0          the comparison goes True
            node.left = ast.BinOp(left=L, op=ast.Mult(), right=ast.Constant(value=0))
        return node


def transform(path, mode):
    src = open(path, encoding='utf-8', errors='replace').read()
    tree = ast.parse(src)
    rw = Rewriter(mode, path)
    tree = rw.visit(tree)
    ast.fix_missing_locations(tree)
    if not rw.sites:
        return None, []
    if mode == 'margin':
        # ⛔ THE FIRST VERSION PREPENDED `PREAMBLE` AS TEXT, WHICH DISPLACED EACH MODULE'S
        # DOCSTRING AND SET `__doc__` TO None -- and eleven receipts that `print(__doc__)` and
        # then split it died with AttributeError.  ** The harness broke the files it was
        # measuring, and reported the breakage as their result. **  The preamble now goes in
        # AFTER the docstring, as AST nodes.
        pre = ast.parse(PREAMBLE).body
        i = 1 if (tree.body and isinstance(tree.body[0], ast.Expr)
                  and isinstance(tree.body[0].value, ast.Constant)
                  and isinstance(tree.body[0].value.value, str)) else 0
        tree.body[i:i] = pre
        ast.fix_missing_locations(tree)
    return ast.unparse(tree), rw.sites


def run_one(path, mode, timeout, outfile):
    """write the rewritten file NEXT TO the original -- imports and relative paths are its own

    ** `baseline` runs the file UNTRANSFORMED, because a verdict about a mutated run is worth
    nothing without the un-mutated one beside it: a receipt that already exits non-zero (a missing
    `camb`, say) would otherwise be read as a mutation firing. **
    """
    if mode == 'baseline':
        code, sites = open(path, encoding='utf-8', errors='replace').read(), transform(path, 'mutate')[1]
    else:
        code, sites = transform(path, mode)
    if code is None:
        return dict(path=path, verdict='NO-SITES', sites=[], secs=0.0)
    d = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(prefix='_tolaudit_', suffix='.py', dir=d)
    t0 = time.time()
    try:
        with os.fdopen(fd, 'w') as f:
            f.write(code)
        env = dict(os.environ, TOLAUDIT_OUT=outfile, MPLBACKEND='Agg')
        try:
            r = subprocess.run([sys.executable, os.path.basename(tmp)], cwd=d, env=env,
                               capture_output=True, text=True, timeout=timeout)
            rc, note = r.returncode, (r.stderr or '').strip().split('\n')[-1][:160]
        except subprocess.TimeoutExpired:
            rc, note = None, f'timeout {timeout}s'
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass
    return dict(path=path, verdict=('TIMEOUT' if rc is None else ('EXIT0' if rc == 0 else 'NONZERO')),
                rc=rc, note=note, sites=sites, secs=time.time() - t0)


def sweep_debris(verbose=True):
    r"""⛔ ** A HARNESS THAT WRITES INTO THE TREE LEAVES DEBRIS WHEN IT IS KILLED. **

    *The rewritten file must sit NEXT TO the original -- a receipt that imports a sibling module
    needs its own directory on `sys.path` -- so `run_one` writes `_tolaudit_*.py` into
    `receipts/<dir>/` and removes it in a `finally`.*  ** A `finally` does not run through SIGKILL,
    and the first long mutation pass was killed by a wall-clock timeout, leaving twenty-odd stray
    files inside `receipts/`, which is exactly where a gate would find them. **
      => *Cleanup is therefore not left to the `finally` alone: this sweeps before every run and
        is exposed as `--clean`.*
    """
    n = 0
    for dp, _, fns in os.walk(os.path.join(ROOT, 'receipts')):
        for fn in fns:
            if fn.startswith('_tolaudit_') and fn.endswith('.py'):
                os.remove(os.path.join(dp, fn))
                n += 1
    if verbose and n:
        print(f'  swept {n} stray _tolaudit_*.py file(s) from receipts/')
    return n


def registered_receipts(only=None):
    out = []
    for dp, _, fns in os.walk(os.path.join(ROOT, 'receipts')):
        for fn in sorted(fns):
            if fn.endswith('.py') and not fn.startswith('_tolaudit_'):
                p = os.path.join(dp, fn)
                if only and only not in p:
                    continue
                try:
                    if transform(p, 'mutate')[1]:
                        out.append(p)
                except SyntaxError:
                    pass
    return sorted(out)


# ------------------------------------------------------------------ the two controls (R2)
CTRL_SENSITIVE = '''
x = 1.0 + 1e-12
assert abs(x - 1.0) < 1e-9, "the tight one"
print("control: sensitive, ALL PASS")
'''
CTRL_UNENFORCED = '''
x = 1.0 + 1e-12
ok = abs(x - 1.0) < 1e-9
print("control: computed but never asserted ->", ok)
'''
CTRL_GUARD = '''
import sys
x = 1.0 + 1e-12
fail = []
if abs(x - 1.0) < 1e-9:
    fail.append("the guard shape: the FAILURE lives on the `<` branch")
print("control: guard, fail =", fail)
sys.exit(1 if fail else 0)
'''

CTRL_ULP = '''
import math
lhs = math.sqrt(2.0) ** 2
rhs = 2.0
assert abs(lhs - rhs) < 1e-9, "an identity that is exact in R and 4.4e-16 in floating point"
print("control: ulp-level, ALL PASS")
'''

CTRL_ZERO = '''
lhs = 3 * 5
rhs = 15
assert abs(lhs - rhs) < 1e-9, "exact integer arithmetic -- the residual really is zero"
print("control: exactly zero, ALL PASS")
'''


def selftest(timeout=60):
    print('  ' + '=' * 88)
    print('  THE HARNESS\'S OWN CONTROLS -- R2 predicted it would need both, before it existed')
    print('  ' + '=' * 88)
    tmpd = tempfile.mkdtemp(prefix='tolaudit_selftest_')
    outf = os.path.join(tmpd, 'margins.jsonl')
    fails = []
    # ⛔ THE FIRST VERSION OF THIS TABLE WANTED margin == 0.0 FOR THE "EXACT" CONTROL AND THE
    # CONTROL FAILED.  It was right to: `sqrt(2)**2 - 2` is 4.4e-16, not 0, so against a 1e-9
    # tolerance the ratio is 4.4e-7.  ** An "exact identity" in a receipt almost never has margin
    # zero -- it has margin at ULP SCALE -- and a harness testing for 0.0 tests for something that
    # hardly ever happens. **  Both cases are now controls: ulp-level and genuinely zero.
    for name, body, want_up, want_dn, band in [
            ('SENSITIVE   (tight assert)', CTRL_SENSITIVE, 'NONZERO', 'EXIT0', (1e-6, 1.0)),
            ('GUARD       (failure on the < branch)', CTRL_GUARD, 'EXIT0', 'NONZERO', (1e-6, 1.0)),
            ('UNENFORCED  (computed, never asserted)', CTRL_UNENFORCED, 'EXIT0', 'EXIT0', (1e-6, 1.0)),
            ('ULP-LEVEL   (exact in R, 4.4e-16 in floats)', CTRL_ULP, 'NONZERO', 'EXIT0', (0.0, 1e-6)),
            ('ZERO        (exact integer arithmetic)', CTRL_ZERO, 'NONZERO', 'EXIT0', (0.0, 0.0))]:
        p = os.path.join(tmpd, name.split()[0].lower() + '.py')
        open(p, 'w').write(body)
        mut = run_one(p, 'mutate', timeout, outf)
        dwn = run_one(p, 'mutate-down', timeout, outf)
        open(outf, 'w').close()
        mar = run_one(p, 'margin', timeout, outf)
        rec = [json.loads(l) for l in open(outf) if l.strip()]
        ratios = [(v / t) for blk in rec for _, v, t in blk if v is not None and t]
        got_r = max(ratios) if ratios else None
        lo, hi = band
        ok_up = mut['verdict'] == want_up
        ok_dn = dwn['verdict'] == want_dn
        ok_mar = got_r is not None and lo <= got_r <= hi
        print(f'    {name:<40} up={mut["verdict"]:<8}(want {want_up:<8}) '
              f'down={dwn["verdict"]:<8}(want {want_dn:<8}) margin={got_r:<11.3e}'
              f'(want [{lo:g}, {hi:g}])')
        if not ok_up:
            fails.append(name + ' [mutate-up]')
        if not ok_dn:
            fails.append(name + ' [mutate-down]')
        if not ok_mar:
            fails.append(name + ' [margin]')
        open(outf, 'w').close()
    print()
    if fails:
        print('  CONTROLS FAILED: ' + '; '.join(fails))
        return 1
    print('  ALL FIVE CONTROLS BEHAVE.  The ASSERT shape is caught by the upward kick and the')
    print('  GUARD shape only by the downward one -- so a one-sided harness would have reported')
    print('  the guard as unenforced.  An unenforced comparison is flagged by neither, which is')
    print('  the verdict that means something; an exact identity is not called a defect; and the')
    print('  margin probe separates ulp-level headroom from a tight tolerance BY MEASUREMENT.')
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', choices=['baseline', 'margin', 'mutate', 'mutate-down'],
                    default='margin')
    ap.add_argument('--only')
    ap.add_argument('--timeout', type=int, default=120)
    ap.add_argument('--jobs', type=int, default=4)
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--out', default=os.path.join(tempfile.gettempdir(), 'tolerance_audit.json'),
                    help='run artefacts; NOT under receipts/ -- a .json there is not a receipt')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--clean', action='store_true', help='sweep stray _tolaudit_*.py and exit')
    a = ap.parse_args(argv)
    if a.clean:
        print(f'  swept {sweep_debris(verbose=False)} file(s)')
        return 0
    if a.selftest:
        return selftest()
    sweep_debris()

    files = registered_receipts(a.only)
    if a.limit:
        files = files[:a.limit]
    marg = a.out + '.margins.jsonl'
    open(marg, 'w').close()
    print(f'  tolerance audit [{a.mode}] over {len(files)} receipt file(s), '
          f'{a.jobs} at a time, {a.timeout}s each')
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        res = list(ex.map(lambda p: run_one(p, a.mode, a.timeout, marg), files))
    tally = {}
    for r in res:
        tally[r['verdict']] = tally.get(r['verdict'], 0) + 1
    print(f'  {time.time()-t0:.0f}s   ' + '  '.join(f'{k}={v}' for k, v in sorted(tally.items())))
    with open(a.out.replace('.json', f'.{a.mode}.json'), 'w') as f:
        json.dump([{k: v for k, v in r.items() if k != 'sites'} | {'nsites': len(r['sites'])}
                   for r in res], f, indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

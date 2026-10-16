#!/usr/bin/env python3
"""r7408 (60) -- ONE COMPARISON, ONE HOP.  The narrower form `r7405` ① ordered, with its four arms
registered in `PREDICTION.md` at `FRAME` before this ran.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THIS RAN: ⒜ exact 1 (sensitivity on the
known instance, pre-repair), ⒝ exact 0 (precision over the 88 carve-out clauses), ⒞ 0 (band 0-4) at HEAD,
⒟ 20 s (band 5-300 s).

** THE RULE. **  *An asserting clause may not compare a pinned operand against an instrument run's output
in the same comparison.*

** THE UNIT, and it is the whole reason this one can work. **  ONE `Compare` expression and its operands,
each name resolved ONE HOP to the statement that binds it, inside the scope that binds it.  No transitive
closure -- so no path root (`r7406`'s `__file__`), no name-level collision across a file, and no loop
sibling: there is nowhere for a walk to wander because there is no walk.

⌗ ⛭ TWO DECISIONS STATED RATHER THAN BURIED:
  ⓵ ** THE UNIT IS EVERY COMPARISON IN THE RECEIPT, not only one inside an asserting call. **  `Ⓑ②`'s
    condition was `_pairs >= 10`, whose operands carry no provenance; the offending comparison was inside
    the loop that BUILT the counter.  Whether a comparison's result reaches an assertion is a dataflow
    question, and the bound `r7405` ① set forbids asking it -- so the comparison is read where the two
    provenances meet, and the precision arm is what shows the widening is safe.
  ⓶ ** A PIN WINS OVER AN INSTRUMENT MARKER on the same binding. **  `git show <sha>:corpus/check_X.py`
    names an instrument AND reads it at a pin: that is a historical read, not an instrument run, and
    treating it as a run is exactly the false positive that killed the previous forms.

⌗ The one figure worth quoting from the refuted family, per `r7405` ①, is the scope-aware bare count:
** `24` against `93` **.  The rest are superseded and are not repeated here.

    python3 -I cost.py
"""
import argparse
import ast
import importlib.util
import os
import re
import subprocess
import sys
import time

FRAME = '0ba253b5'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))

S37 = ('receipts/L_probability/S37_the_ground_disqualified_seventeen_of_its_authors_own_calls_and_'
       'sixteen_of_them_are_repairs.py')
# the commit before r7402's repair, where the defect stood -- taken from the repair's own commit
REPAIR_SUBJECT = 'r7402 — the gate that counted'
ASSERTERS = {'gate': 1, 'check': 1, 'assert_': 1}
_SHA = re.compile(r'\b[0-9a-f]{8,40}\b')
_PINNED = re.compile(r"""['"]show['"]|git\s+show\b""")
_RUN = re.compile(r'mutate_assertions|--quote|--prose|--cannot-fail|\balt_runs\s*\(|\bsweep_\w+|'
                  r'\bcheck_\w+\.py')
_DIRECTIONAL = (ast.Lt, ast.Gt, ast.LtE, ast.GtE)


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def seat_receipts(sha=None):
    """(path, source) for every receipt carrying a `+60` revision stamp, live or at a commit"""
    out = []
    names = (git('ls-tree', '-r', '--name-only', sha) if sha else git('ls-files', 'receipts'))
    for f in names.split('\n'):
        if not f.startswith('receipts/') or not f.endswith('.py'):
            continue
        src = git('show', f'{sha}:{f}') if sha else None
        if src is None:
            p = os.path.join(ROOT, f)
            if not os.path.exists(p):
                continue
            src = open(p, encoding='utf-8', errors='replace').read()
        if re.search(r'r\d{4}\+60\b', src):
            out.append((f, src))
    return out


# ============================================================ the scope map, and ONE HOP inside it
def scopes_of(tree):
    out = [(tree, None)]

    def rec(node, parent):
        for n in ast.iter_child_nodes(node):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                out.append((n, parent))
                rec(n, n)
            else:
                rec(n, parent)
    rec(tree, tree)
    return out


def own_statements(scope):
    acc = []

    def rec(node):
        for n in ast.iter_child_nodes(node):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                continue
            acc.append(n)
            rec(n)
    rec(scope)
    return acc


def targets(n):
    tg = []
    if isinstance(n, ast.Assign):
        tg = n.targets
    elif isinstance(n, (ast.AnnAssign, ast.AugAssign)):
        tg = [n.target]
    elif isinstance(n, (ast.For, ast.comprehension)):
        tg = [n.target]
    return [x.id for t in tg for x in ast.walk(t) if isinstance(x, ast.Name)]


def mark(seg):
    """PINNED / RUN / '' for ONE binding's own source segment.  A pin WINS: reading an instrument's
    source at a sha is a historical read and not a run of it."""
    if _PINNED.search(seg) or _SHA.search(seg):
        return 'PINNED'
    if _RUN.search(seg):
        return 'RUN'
    return ''


def bindings_of(scope, src):
    """name -> {mark} for the bindings THIS scope makes, one statement deep.  A `for`'s name takes the
    mark of its ITERABLE, which is the single hop `Ⓑ②` needs: `for b in _grp` makes `b` carry `_grp`'s."""
    out = {}
    for n in own_statements(scope):
        if isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign)) and n.value is not None:
            m = mark(ast.get_source_segment(src, n.value) or '')
            for nm in targets(n):
                out.setdefault(nm, set()).add(m)
        elif isinstance(n, ast.For):
            m = mark(ast.get_source_segment(src, n.iter) or '')
            for nm in targets(n):
                out.setdefault(nm, set()).add(m)
        for c in ast.walk(n):
            if isinstance(c, ast.comprehension):
                m = mark(ast.get_source_segment(src, c.iter) or '')
                for nm in targets(c):
                    out.setdefault(nm, set()).add(m)
    return out


def scan(src, path):
    """every comparison whose operands carry BOTH marks, one hop, scope-aware.
    Returns [(line, marks, the comparison's own text, the enclosing asserting call's line or None)]"""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    scopes = scopes_of(tree)
    binds = {id(sc): bindings_of(sc, src) for sc, _ in scopes}
    parent = {id(sc): p for sc, p in scopes}
    owner = {}
    for sc, _ in scopes:
        for n in own_statements(sc):
            owner[id(n)] = sc
    # which asserting call, if any, each node sits inside
    inside = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ASSERTERS:
            for a in n.args[ASSERTERS[n.func.id]:]:
                for q in ast.walk(a):
                    inside[id(q)] = n.lineno

    def resolve(nm, sc):
        seen = set()
        while sc is not None and id(sc) not in seen:
            seen.add(id(sc))
            if nm in binds[id(sc)]:
                return binds[id(sc)][nm]
            sc = parent.get(id(sc))
        return set()

    def operand_marks(expr, sc):
        got = set()
        for x in ast.walk(expr):
            if isinstance(x, ast.Name):
                got |= resolve(x.id, sc)
        return got

    hits = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Compare):
            continue
        sc = owner.get(id(n))
        if sc is None:
            for s2, _ in scopes:
                if any(id(q) == id(n) for st in own_statements(s2) for q in ast.walk(st)):
                    sc = s2
                    break
        sc = sc or tree
        sides = [operand_marks(n.left, sc)] + [operand_marks(c, sc) for c in n.comparators]
        has_pin = any('PINNED' in s for s in sides)
        has_run = any('RUN' in s for s in sides)
        if not (has_pin and has_run):
            continue
        # the two marks must be on DIFFERENT sides of the same comparison -- one operand carrying both
        # is a quantity already built from both, which is the ratchet r7405 ruled NOT BUILT
        if not any('PINNED' in a and 'RUN' not in a for a in sides):
            continue
        if not any('RUN' in b and 'PINNED' not in b for b in sides):
            continue
        hits.append((n.lineno, sorted({m for s in sides for m in s if m}),
                     (ast.get_source_segment(src, n) or '')[:110].replace('\n', ' '),
                     inside.get(id(n))))
    return hits


def main():
    argparse.ArgumentParser().parse_args()
    print(f'# r7408 (60) -- one comparison, one hop, at FRAME {FRAME}')
    print('# ⌗ the one figure quoted from the refuted family, per r7405 ①: the scope-aware bare count,')
    print('#   24 against 93.  The others are superseded and are not repeated.')

    # ── ⒜ sensitivity, at the commit before the repair ────────────────────────────────────────────
    pre = git('log', '--format=%H %s', '-20', '--', S37).split('\n')
    repair = next((l.split()[0] for l in pre if REPAIR_SUBJECT in l), '')
    before = git('rev-parse', f'{repair}~1').strip() if repair else ''
    print()
    print(f'# ⒜ SENSITIVITY, at the commit before the repair ({before[:12]})   (point prediction 1)')
    s37_pre = git('show', f'{before}:{S37}') if before else ''
    hits_pre = scan(s37_pre, S37) if s37_pre else []
    print(f'#    {len(hits_pre)} hit(s) in S37 pre-repair:')
    for h in hits_pre:
        print(f'#      line {h[0]}  {",".join(h[1])}  inside the asserting call at {h[3]}')
        print(f'#        {h[2]}')
    print(f'#    and at HEAD, after the repair: {len(scan(open(os.path.join(ROOT, S37), encoding="utf-8").read(), S37))} hit(s)')

    # ── ⒝ precision over the carve-out clauses ────────────────────────────────────────────────────
    # ⛭ THE POPULATION IS `r7406`'s OWN, IMPORTED AND NOT RE-COLLECTED: the arm was registered over
    #   "the 88 carve-out clauses r7406 counted", so re-deriving them here with a looser condition
    #   would score the arm against a different population than the one it names.  r7367 ④'s remedy.
    t0 = time.time()
    live = seat_receipts()
    hits_by_file = {f: {h[0] for h in scan(src, f)} for f, src in live}
    _r7406 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                          'r7406_60_the_signature_of_the_defect_is_the_signature_of_the_repair',
                          'cost.py')
    _spec = importlib.util.spec_from_file_location('r7406_cost', _r7406)
    _R = importlib.util.module_from_spec(_spec)
    sys.modules['r7406_cost'] = _R
    _spec.loader.exec_module(_R)
    carve = _R.carve_population()
    srcs = dict(live)
    charged = []
    for f, line in carve:
        if f not in srcs:
            continue
        try:
            tree = ast.parse(srcs[f])
        except SyntaxError:
            continue
        for n in ast.walk(tree):
            if (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id in ASSERTERS and n.lineno == line):
                lines = {q.lineno for a in n.args[ASSERTERS[n.func.id]:]
                         for q in ast.walk(a) if hasattr(q, 'lineno')}
                if hits_by_file.get(f, set()) & lines:
                    charged.append((f, line))
    t_scan = time.time() - t0
    print()
    print(f'# ⒝ PRECISION against the prescribed repair: {len(charged)} of {len(carve)} carve-out '
          f'clause(s) charged -- the population imported from r7406   (point prediction 0)')
    for c in charged[:10]:
        print(f'#      ⛔ {c[0].split("/")[-1][:58]}:{c[1]}')

    # ── ⒞ the corpus count at HEAD ────────────────────────────────────────────────────────────────
    allhits = [(f, h) for f, src in live for h in scan(src, f)]
    print()
    print(f'# ⒞ THE CORPUS COUNT at HEAD: {len(allhits)} hit(s) over {len(live)} receipt(s)   '
          f'(band 0-4, central 0)')
    for f, h in sorted(allhits):
        print(f'#      {f.split("/")[-1][:58]}:{h[0]}  {",".join(h[1])}  '
              f'{"inside an asserting call at " + str(h[3]) if h[3] else "outside any asserting call"}')
        print(f'#        {h[2]}')

    print()
    print(f'# ⒟ THE PRICE on this container: {t_scan:.1f}s over {len(live)} receipt(s)   '
          f'(band 5-300 s, central 20 s)')
    print('#    no subprocess, no closure, one pass: the price is a property of the bound.')


if __name__ == '__main__':
    main()

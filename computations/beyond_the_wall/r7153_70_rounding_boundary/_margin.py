"""_margin.py -- run ONE receipt and record, at each rounding-boundary site, how far the measured value sits from the
boundary that decides the verdict (r7153+70.1, node 70).

  python3 _margin.py <receipt.py> <out.json> <line:col> ...

The receipt runs from its own directory, as `run_all_receipts` runs it.  The one edit is an AST rewrite at each named
Compare: the measured operand is wrapped in `__rb(value, sid, n)`, which records the MARGIN and returns the value
unchanged.  The margin is the distance to the flipping boundary in units of 10^-n:
  ROUND      `round(x, n) == L`       -> | frac(x * 10^n) - 1/2 |
  HALF-UNIT  `abs(d) < 5*10^-(n+1)`   -> | 1/2 - |d| * 10^n |
An array operand records its smallest element margin.  Nothing else in the receipt changes.
"""
import ast
import atexit
import json
import math
import os
import sys

path, out = os.path.abspath(sys.argv[1]), sys.argv[2]
want = {tuple(int(x) for x in s.split(':')) for s in sys.argv[3:]}
src = open(path, encoding='utf-8').read()
tree = ast.parse(src, path)
REC = {}


def _scalars(v):
    try:
        return [float(v)]
    except (TypeError, ValueError):
        try:
            import numpy as np
            return [float(x) for x in np.asarray(v, dtype=float).ravel()]
        except Exception:
            return []


def __rb(v, sid, kind, n):
    try:
        n = int(n)
        ms = []
        for x in _scalars(v):
            if not math.isfinite(x):
                continue
            if kind == 'ROUND':
                y = x * 10 ** n
                ms.append(abs((y - math.floor(y)) - 0.5))
            else:
                ms.append(abs(0.5 - abs(x) * 10 ** n))
        if ms:
            REC.setdefault(sid, []).append(min(ms))
    except Exception:
        pass
    return v


def _wrap(node, sid, kind, n):
    return ast.Call(func=ast.Name('__rb', ast.Load()),
                    args=[node, ast.Constant(sid), ast.Constant(kind), n], keywords=[])


class Rw(ast.NodeTransformer):
    def visit_Compare(self, node):
        self.generic_visit(node)
        key = (node.lineno, node.col_offset)
        if key not in want or len(node.ops) != 1:
            return node
        sid = f'{key[0]}:{key[1]}'
        a, b = node.left, node.comparators[0]
        if isinstance(node.ops[0], ast.Eq):
            for side in ('left', 'right'):
                x = node.left if side == 'left' else node.comparators[0]
                if isinstance(x, ast.Call) and isinstance(x.func, ast.Name) and x.func.id == 'round' and len(x.args) == 2:
                    x.args[0] = _wrap(x.args[0], sid, 'ROUND', x.args[1])
                    break
        elif isinstance(a, ast.Call) and len(a.args) == 1:
            # abs(d) < T: n is read from T = 5*10^-(n+1) at run time inside the wrapper's caller
            t = b
            n = ast.Call(func=ast.Name('__rb_n', ast.Load()), args=[t], keywords=[])
            a.args[0] = _wrap(a.args[0], sid, 'HALF-UNIT', n)
        elif isinstance(a, ast.Name):
            # r7155+70.1 HALF-UNIT-LABELLED: `_d < T` with `_d = abs(E - C)` -- the name IS the distance |d|
            n = ast.Call(func=ast.Name('__rb_n', ast.Load()), args=[b], keywords=[])
            node.left = _wrap(a, sid, 'HALF-UNIT', n)
        return node


def __rb_n(t):
    return -round(math.log10(2 * float(t)))


tree = ast.fix_missing_locations(Rw().visit(tree))
atexit.register(lambda: json.dump(REC, open(out, 'w')))
os.chdir(os.path.dirname(path))
sys.path.insert(0, os.path.dirname(path))
sys.argv = [path]
g = {'__name__': '__main__', '__file__': path, '__builtins__': __builtins__, '__rb': __rb, '__rb_n': __rb_n}
exec(compile(tree, path, 'exec'), g)

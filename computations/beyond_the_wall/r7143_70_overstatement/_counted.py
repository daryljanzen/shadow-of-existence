"""_counted.py -- run ONE receipt with every check helper rebound to a counting wrapper (r7143+70.1, node 70).

  python3 _counted.py <receipt.py> <out.json> [line:end_line ...]

The receipt runs from its own directory, as `run_all_receipts` runs it, and is otherwise unchanged: the one edit
is an AST insertion `name = __cf_wrap(name)` after each check-helper definition.  A helper is a function the
receipt CALLS with a string label beside a non-label argument -- the `check(label, ok)` / `check(ok, label)`
family the instrument's `_verdicts` reads -- so a function that merely contains an `assert` is not counted.
Only the OUTERMOST helper call counts: a `gate` that calls `check` is one verdict.
The spans on the command line are the owed cannot-fail sites' enclosing helper calls; each call whose caller
line lies in a span is counted against it.
"""
import ast
import atexit
import json
import os
import sys

path, out = os.path.abspath(sys.argv[1]), sys.argv[2]
spans = [tuple(int(x) for x in s.split(':')) for s in sys.argv[3:]]
src = open(path, encoding='utf-8').read()
tree = ast.parse(src, path)

LAB = lambda x: isinstance(x, ast.JoinedStr) or (isinstance(x, ast.Constant) and isinstance(x.value, str))
labelled = set()
for n in ast.walk(tree):
    if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and len(n.args) >= 2:
        if LAB(n.args[0]) != LAB(n.args[1]):
            labelled.add(n.func.id)
helpers = set()


class Ins(ast.NodeTransformer):
    def _body(self, body):
        new = []
        for s in body:
            new.append(self.visit(s))
            if isinstance(s, ast.FunctionDef) and s.name in labelled and len(s.args.args) >= 2:
                helpers.add(s.name)
                new.append(ast.parse(f'{s.name} = __cf_wrap({s.name})').body[0])
        return new

    def generic_visit(self, node):
        for f in ('body', 'orelse', 'finalbody'):
            if isinstance(getattr(node, f, None), list) and not isinstance(node, ast.ClassDef):
                setattr(node, f, self._body(getattr(node, f)))
        for f, v in ast.iter_fields(node):
            if f in ('body', 'orelse', 'finalbody'):
                continue
            if isinstance(v, list):
                setattr(node, f, [self.visit(x) if isinstance(x, ast.AST) else x for x in v])
            elif isinstance(v, ast.AST):
                setattr(node, f, self.visit(v))
        return node


tree = ast.fix_missing_locations(Ins().visit(tree))
STATE = {'depth': 0, 'N': 0, 'span': [0] * len(spans), 'off_file': 0}


def __cf_wrap(fn):
    def w(*a, **k):
        if STATE['depth'] == 0:
            fr = sys._getframe(1)
            if fr.f_code.co_filename == path:
                STATE['N'] += 1
                for i, (lo, hi) in enumerate(spans):
                    if lo <= fr.f_lineno <= hi:
                        STATE['span'][i] += 1
            else:
                STATE['off_file'] += 1
        STATE['depth'] += 1
        try:
            return fn(*a, **k)
        finally:
            STATE['depth'] -= 1
    w.__wrapped__ = fn
    return w


def dump():
    json.dump(dict(helpers=sorted(helpers), **STATE), open(out, 'w'))


atexit.register(dump)
os.chdir(os.path.dirname(path))
sys.path.insert(0, os.path.dirname(path))
sys.argv = [path]
g = {'__name__': '__main__', '__file__': path, '__builtins__': __builtins__, '__cf_wrap': __cf_wrap}
exec(compile(tree, path, 'exec'), g)

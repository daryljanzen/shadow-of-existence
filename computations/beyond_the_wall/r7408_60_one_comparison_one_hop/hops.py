#!/usr/bin/env python3
"""r7408 (60) -- HOW MANY HOPS THE PROVENANCE ACTUALLY SITS FROM THE COMPARISON.  ⛔ Not a registered
arm: `⒜` is refuted and this measures WHY, so the next seat knows what a dataflow build would have to
reach rather than guessing a hop count.  Reported, never banded after the fact.

    python3 -I hops.py
"""
import ast
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r7408_cost', os.path.join(HERE, 'cost.py'))
C = importlib.util.module_from_spec(spec)
sys.modules['r7408_cost'] = C
spec.loader.exec_module(C)

before = C.git('rev-parse', '1977dddd~1').strip()
src = C.git('show', f'{before}:{C.S37}')
tree = ast.parse(src)
scopes = C.scopes_of(tree)
binds, inputs = {}, {}
for sc, _ in scopes:
    for n in C.own_statements(sc):
        val = n.value if isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign)) else (
            n.iter if isinstance(n, ast.For) else None)
        if val is None:
            continue
        seg = ast.get_source_segment(src, val) or ''
        m = C.mark(seg)
        for nm in C.targets(n):
            binds.setdefault(nm, set()).add(m)
            inputs.setdefault(nm, set()).update(
                {x.id for x in ast.walk(val) if isinstance(x, ast.Name)} - {nm})
    for n in ast.walk(sc):
        if isinstance(n, ast.comprehension):
            seg = ast.get_source_segment(src, n.iter) or ''
            m = C.mark(seg)
            for nm in C.targets(n):
                binds.setdefault(nm, set()).add(m)
                inputs.setdefault(nm, set()).update(
                    {x.id for x in ast.walk(n.iter) if isinstance(x, ast.Name)} - {nm})


def nearest(nm, want, cap=8):
    """the fewest hops from `nm` to a binding marked `want`, or None within `cap`"""
    front, seen = {nm}, set()
    for d in range(cap + 1):
        nxt = set()
        for x in front:
            if x in seen:
                continue
            seen.add(x)
            if want in binds.get(x, set()):
                return d
            nxt |= inputs.get(x, set())
        front = nxt - seen
        if not front:
            return None
    return None


print(f'# r7408 (60) -- the hop distance in S37 at {before[:12]}, the commit before the repair')
print('# the offending comparison is `norm(_a) in norm(b)`, inside `any(... for b in _grp)`')
for nm, want in (('_a', 'PINNED'), ('_c', 'PINNED'), ('_mine', 'PINNED'), ('_now', 'PINNED'),
                 ('b', 'RUN'), ('_grp', 'RUN'), ('_runs', 'RUN'), ('_alt', 'RUN')):
    print(f'#   {nm:7} -> nearest {want:7} binding: {nearest(nm, want)} hop(s); '
          f'own mark {sorted(binds.get(nm, set()))}')
print('# ⇒ ONE HOP reaches neither side.  The rule r7405 ① bounded to one expression and one hop')
print('#   therefore cannot see the one instance in this corpus, and widening the hop count IS the')
print('#   closure walk that four earlier forms died on.')

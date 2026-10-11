#!/usr/bin/env python3
"""r7255+70.1: 60's OWN alignment test (S18's `_occ`, lifted by name, not re-typed) run on the 46 re-cuts -- a span
is CLIPPED if EVERY occurrence in the non-appendix papers is clipped, as S18 requires."""
import ast, glob, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
S18 = glob.glob(os.path.join(ROOT, 'receipts', 'L_probability', 'S18_*.py'))[0]
ns = {'re': re, 'os': os, 'ROOT': ROOT, '__import__': __import__}
for node in ast.parse(open(S18, encoding='utf-8').read()).body:
    if (isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in ('_PAPERS', '_NORM', '_W') for t in node.targets)) \
            or (isinstance(node, ast.FunctionDef) and node.name == '_occ'):
        exec(compile(ast.Module([node], []), S18, 'exec'), ns)
L = [x for x in json.load(open(os.path.join(HERE, 'ledger.json'))) if x['outcome'] == 'APPLIED']
res = {'ALIGNED': 0, 'CLIPPED': 0, 'NOT-IN-PAPERS': 0}
for x in L:
    o = ns['_occ'](x['recut'])
    res['NOT-IN-PAPERS' if not o else 'CLIPPED' if all(o) else 'ALIGNED'] += 1
before = {'CLIPPED': 0}
for x in L:
    o = ns['_occ'](x['lit']); before['CLIPPED'] += bool(o) and all(o)
print(f"60's test on the {len(L)} spans: before the re-cut {before['CLIPPED']} CLIPPED;  after: {res}")

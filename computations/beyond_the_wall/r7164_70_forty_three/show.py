"""show.py N [N..] -- print an owed site's check call and the bindings of every name in its verdict (read aid)."""
import ast, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(HERE, 'sites.json')))
for a in sys.argv[1:]:
    s = S[int(a)]
    src = open(s['receipt'], encoding='utf-8').read()
    tree = ast.parse(src)
    l, c = map(int, s['site'].split(':'))
    call = next(n for n in ast.walk(tree) if isinstance(n, ast.Call) and n.lineno == l and n.col_offset == c)
    print(f'=== {a} {s["verdict"]} {s["receipt"]}:{l}\n' + (ast.get_source_segment(src, call) or '')[:900])
    names = {x.id for x in ast.walk(call) if isinstance(x, ast.Name)}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in names for t in ast.walk(n) if isinstance(t, ast.Name) and t in [z for tt in n.targets for z in ast.walk(tt)]):
            seg = ast.get_source_segment(src, n) or ''
            print(f'   L{n.lineno}: {seg[:300]}')
    print()

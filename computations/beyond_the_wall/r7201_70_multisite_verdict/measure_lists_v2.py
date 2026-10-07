"""E3 v2 -- the pre-registered definition (v1, measure_lists.py) missed S2's ABSENT list, which is passed WHOLE to a
paper-surveying helper (`RB.survey(ABSENT + ...)`) and asserted on the result.  v2 counts a module-level string
collection as pin-like if, in a receipt that reads the papers, it is
  (a) iterated, with the loop variable used in any comparison (not only `in`), or
  (b) passed, alone or concatenated, as an argument to any call.
Kept beside v1, not in place of it."""
import ast, glob, json, os, re, sys
from collections import Counter
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
READS_PAPERS = re.compile(r"\.tex\b|reach_baseline|corpus['\"/]")
def strs(v):
    if isinstance(v, (ast.List, ast.Tuple, ast.Set)):
        out = []
        for e in v.elts:
            if isinstance(e, ast.Constant) and isinstance(e.value, str): out.append(e.value)
            elif isinstance(e, (ast.Tuple, ast.List)) and e.elts and isinstance(e.elts[0], ast.Constant) and isinstance(e.elts[0].value, str): out.append(e.elts[0].value)
            else: return None
        return out
    if isinstance(v, ast.Dict):
        ks = [k.value for k in v.keys if isinstance(k, ast.Constant) and isinstance(k.value, str)]
        return ks if ks and len(ks) == len(v.keys) else None
    return None
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
    src = open(f, encoding='utf-8', errors='replace').read()
    if not READS_PAPERS.search(src): continue
    try: tree = ast.parse(src)
    except SyntaxError: continue
    coll = {}
    for n in tree.body:
        if isinstance(n, (ast.Assign, ast.AnnAssign)):
            tg = n.targets[0] if isinstance(n, ast.Assign) else n.target
            if isinstance(tg, ast.Name) and n.value is not None:
                s = strs(n.value)
                if s and all(len(x.strip()) >= 3 for x in s): coll[tg.id] = s
    if not coll: continue
    how = {}
    for node in ast.walk(tree):
        gens = []
        if isinstance(node, ast.For): gens = [(node.target, node.iter, node.body)]
        elif isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)):
            gens = [(g.target, g.iter, [node]) for g in node.generators]
        for tgt, it, body in gens:
            base = it.func.value if isinstance(it, ast.Call) and isinstance(it.func, ast.Attribute) and it.func.attr in ('items','keys','values') else it
            if isinstance(base, ast.Name) and base.id in coll:
                tn = {x.id for x in ast.walk(tgt) if isinstance(x, ast.Name)}
                if any(isinstance(c, ast.Compare) and any(isinstance(x, ast.Name) and x.id in tn for x in ast.walk(c)) for b in body for c in ast.walk(b)):
                    how.setdefault(base.id, set()).add('ITERATED')
        if isinstance(node, ast.Call):
            for a in list(node.args) + [k.value for k in node.keywords]:
                for x in ast.walk(a):
                    if isinstance(x, ast.Name) and x.id in coll and not (isinstance(node.func, ast.Name) and node.func.id in ('len', 'print', 'sorted', 'list', 'set', 'enumerate', 'zip', 'range', 'str', 'repr')):
                        how.setdefault(x.id, set()).add('PASSED')
    for name, h in how.items():
        rows.append((os.path.relpath(f, ROOT), name, '+'.join(sorted(h)), coll[name]))
print(f'v2 collections {len(rows)} in {len({r[0] for r in rows})} receipts; strings {sum(len(r[3]) for r in rows)}')
print('  by route:', dict(Counter(r[2] for r in rows)))
print('  S2 ABSENT found:', any('S2_the_systematics' in r[0] and r[1] == 'ABSENT' for r in rows))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lists_v2.tsv'), 'w') as o:
    o.write('receipt\tcollection\troute\tn_strings\tstrings\n')
    for r in sorted(rows): o.write('\t'.join([r[0], r[1], r[2], str(len(r[3])), json.dumps(r[3])]) + '\n')

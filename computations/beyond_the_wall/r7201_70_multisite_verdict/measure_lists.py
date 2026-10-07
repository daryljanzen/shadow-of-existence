"""E3/E4: pin-like COLLECTIONS -- a module-level list/tuple/set/dict of string constants that a loop or comprehension
iterates (itself, .keys(), .values(), .items()) and whose loop variable is tested with `in`/`not in` against a container."""
import ast, glob, json, os, re, sys
from collections import Counter
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
sys.path.insert(0, os.path.join(ROOT, 'scripts')); sys.argv = sys.argv[:1]
import mutate_assertions as MA
TEX = {}
def tex(name):
    if name not in TEX:
        p = os.path.join(ROOT, 'corpus', name)
        TEX[name] = open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else None
    return TEX[name]
def strs(v):
    if isinstance(v, (ast.List, ast.Tuple, ast.Set)):
        out = []
        for e in v.elts:
            if isinstance(e, ast.Constant) and isinstance(e.value, str): out.append(e.value)
            elif isinstance(e, (ast.Tuple, ast.List)) and e.elts and isinstance(e.elts[0], ast.Constant) and isinstance(e.elts[0].value, str):
                out.append(e.elts[0].value)   # (phrase, note) pairs: the phrase is the pin
            else: return None
        return out
    if isinstance(v, ast.Dict):
        ks = [k.value for k in v.keys if isinstance(k, ast.Constant) and isinstance(k.value, str)]
        vs = [x.value for x in v.values if isinstance(x, ast.Constant) and isinstance(x.value, str)]
        return (ks if len(ks) == len(v.keys) else []) + vs if (ks or vs) else None
    return None
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
    src = open(f, encoding='utf-8', errors='replace').read()
    try: tree = ast.parse(src)
    except SyntaxError: continue
    asg, fns = MA._defs(tree)
    coll = {}
    for n in tree.body:
        if isinstance(n, (ast.Assign, ast.AnnAssign)):
            tg = n.targets[0] if isinstance(n, ast.Assign) else n.target
            if isinstance(tg, ast.Name) and n.value is not None:
                s = strs(n.value)
                if s and len(s) >= 1 and all(len(x.strip()) >= 3 for x in s):
                    coll[tg.id] = s
    if not coll: continue
    for node in ast.walk(tree):
        gens = []
        if isinstance(node, ast.For): gens = [(node.target, node.iter, node.body)]
        elif isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)):
            gens = [(g.target, g.iter, [node]) for g in node.generators]
        for tgt, it, body in gens:
            base = it.func.value if isinstance(it, ast.Call) and isinstance(it.func, ast.Attribute) and it.func.attr in ('items', 'keys', 'values') else it
            if not (isinstance(base, ast.Name) and base.id in coll): continue
            tnames = {x.id for x in ast.walk(tgt) if isinstance(x, ast.Name)}
            for b in body:
                for c in ast.walk(b):
                    if (isinstance(c, ast.Compare) and len(c.ops) == 1 and isinstance(c.ops[0], (ast.In, ast.NotIn))
                            and isinstance(c.left, ast.Name) and c.left.id in tnames):
                        pol = 'ABSENT' if isinstance(c.ops[0], ast.NotIn) else 'PRESENT'
                        trace = MA._reads(c.comparators[0], asg, fns, src) or ''
                        papers = sorted(set(re.findall(r'(\w[\w\-]*\.tex)\b', trace)))
                        rows.append((os.path.relpath(f, ROOT), base.id, c.lineno, pol, ','.join(papers), coll[base.id]))
# one row per (receipt, collection, polarity)
seen = {}
for r in rows: seen.setdefault((r[0], r[1], r[3]), r)
rows = list(seen.values())
paper_rows = [r for r in rows if r[4]]
def occ(lit, t): return max(t.count(lit), ' '.join(t.split()).count(' '.join(lit.split())))
strings = sum(len(r[5]) for r in rows)
pres = [(r, s) for r in paper_rows if r[3] == 'PRESENT' for s in r[5]]
mult = 0; absn = 0
for r, s in pres:
    n = max((occ(s, tex(p)) for p in r[4].split(',') if tex(p) is not None), default=-1)
    mult += n >= 2; absn += n == 0
print(f'collections {len(rows)} in {len({r[0] for r in rows})} receipts; strings {strings}; reaching a paper: {len(paper_rows)} collections')
print('  by polarity:', dict(Counter(r[3] for r in rows)), '| paper-reaching by polarity:', dict(Counter(r[3] for r in paper_rows)))
print(f'  presence strings on a paper {len(pres)}: MULTI-SITE {mult} ({100*mult/max(1,len(pres)):.1f}%), ABSENT {absn}')
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lists.tsv'), 'w') as o:
    o.write('receipt\tcollection\tline\tpolarity\tpapers\tn_strings\tstrings\n')
    for r in sorted(rows): o.write('\t'.join([r[0], r[1], str(r[2]), r[3], r[4], str(len(r[5])), json.dumps(r[5])]) + '\n')

"""r7183+70.1 -- literal pins that occur more than once in their file: pins on a file, not a claim.

  python3 multi_site.py [ROOT] [--tsv OUT]
Receipt pins: `'<lit>' in <name>` (len(lit) >= 8) in a receipt naming exactly one corpus paper.
Explainer pins: `in <file>: "<lit>"` clauses in EXPLAINER.md watch markers.
Counts are non-overlapping occurrences in whitespace-collapsed, comment-stripped text.
"""
import ast, glob, os, re, sys
ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else os.getcwd()
OUT = sys.argv[sys.argv.index('--tsv') + 1] if '--tsv' in sys.argv else None
MIN = 8
PAPERS = {os.path.basename(p): p for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
          if not os.path.basename(p).startswith('appendix_')}
_T = {}
def text(path):
    if path not in _T:
        t = open(path, encoding='utf-8', errors='replace').read()
        if path.endswith('.tex'):
            t = re.sub(r'(?<!\\)%[^\n]*', '', t)
        _T[path] = ' '.join(t.split())
    return _T[path]
def count(lit, path):
    return text(path).count(' '.join(lit.split()))

rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
    src = open(f, encoding='utf-8', errors='replace').read()
    named = [n for n in PAPERS if n in src]
    if len(named) != 1:
        continue
    try:
        tree = ast.parse(src)
    except SyntaxError:
        continue
    for node in ast.walk(tree):
        if (isinstance(node, ast.Compare) and len(node.ops) == 1 and isinstance(node.ops[0], ast.In)
                and isinstance(node.left, ast.Constant) and isinstance(node.left.value, str)
                and len(node.left.value.strip()) >= MIN and isinstance(node.comparators[0], (ast.Name, ast.Attribute, ast.Call))):
            n = count(node.left.value, PAPERS[named[0]])
            rows.append(('receipt', os.path.relpath(f, ROOT), node.lineno, named[0], n, node.left.value))
ex = os.path.join(ROOT, 'EXPLAINER.md')
if os.path.exists(ex):
    for i, ln in enumerate(open(ex, encoding='utf-8'), 1):
        if ln.startswith('<!-- watch:'):
            for fn, lit in re.findall(r'in ([^\s:]+): "((?:[^"\\]|\\.)*)"', ln):
                p = os.path.join(ROOT, fn)
                n = count(lit, p) if os.path.exists(p) else -1
                rows.append(('explainer', 'EXPLAINER.md', i, fn, n, lit))

for kind in ('receipt', 'explainer'):
    r = [x for x in rows if x[0] == kind]
    present = [x for x in r if x[4] >= 1]
    multi = [x for x in r if x[4] >= 2]
    print(f'{kind}: pins {len(r)}; present {len(present)}; absent {sum(1 for x in r if x[4] == 0)}; '
          f'MULTI-SITE {len(multi)} ({100 * len(multi) / max(1, len(present)):.1f}% of present)')
if OUT:
    with open(OUT, 'w') as o:
        o.write('kind\tfile\tline\tpaper\toccurrences\tliteral\n')
        for x in rows:
            o.write('\t'.join(map(str, x[:5])) + '\t' + x[5].replace('\t', ' ').replace('\n', ' ') + '\n')

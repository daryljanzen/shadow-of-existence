"""r7179+70.1 -- a tolerance against the precision of the paper figure it pins.

For every `abs(E - L) < T` (or `abs(L - E)`, `<=`) in a receipt, where L and T are numeric literals: find L PRINTED
in a corpus paper the receipt names (`<name>.tex` in its source), take the printed precision from the paper's own
string (the coarsest printing, so the flag is conservative), and report T / half-ulp.  T > half-ulp means the pin
accepts a value the paper would print differently.

  python3 tol_vs_print.py [ROOT] [--tsv OUT]
"""
import ast, glob, os, re, sys

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else os.getcwd()
OUT = sys.argv[sys.argv.index('--tsv') + 1] if '--tsv' in sys.argv else None

NUM = re.compile(r'(?<![\w.])(\d+(?:\.\d+)?)(?:\s*\\times\s*10\^\{?(-?\d+)\}?)?(?![\w])')


def num(n):
    if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
        return float(n.value)
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
        v = num(n.operand)
        return -v if v is not None else None
    return None


def printings(tex):
    """value -> list of ulps at which the paper prints it"""
    t = re.sub(r'(?<!\\)%[^\n]*', '', tex).replace('{,}', '').replace('\\,', '')
    out = {}
    for m in NUM.finditer(t):
        mant, ex = m.group(1), m.group(2)
        dec = len(mant.split('.')[1]) if '.' in mant else 0
        e = int(ex) if ex else 0
        v = float(mant) * 10 ** e
        out.setdefault(round(v, 12), []).append(10.0 ** (e - dec))
    return out


PAPERS = {os.path.basename(p): p for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
          if not os.path.basename(p).startswith('appendix_')}
_PR = {}


def pr(name):
    if name not in _PR:
        _PR[name] = printings(open(PAPERS[name], encoding='utf-8', errors='replace').read())
    return _PR[name]


rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
    src = open(f, encoding='utf-8', errors='replace').read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        continue
    named = sorted(n for n in PAPERS if n in src)
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Compare) and len(node.ops) == 1 and isinstance(node.ops[0], (ast.Lt, ast.LtE))):
            continue
        a = node.left
        if not (isinstance(a, ast.Call) and getattr(a.func, 'id', None) == 'abs' and len(a.args) == 1
                and isinstance(a.args[0], ast.BinOp) and isinstance(a.args[0].op, ast.Sub)):
            continue
        T = num(node.comparators[0])
        if T is None or T <= 0:
            continue
        b = a.args[0]
        L = num(b.right) if num(b.right) is not None else num(b.left)
        if L is None or L == 0:
            continue
        rel = os.path.relpath(f, ROOT)
        hit = []
        for p in named:
            for v, ulps in pr(p).items():
                if abs(v - abs(L)) <= 1e-9 * max(1.0, abs(L)):
                    hit += [(u, p) for u in ulps]
        if not hit:
            rows.append((rel, node.lineno, L, T, '', '', 'UNANCHORED' if named else 'NO-PAPER-NAMED'))
            continue
        u, p = max(hit)
        ratio = T / (u / 2)
        rows.append((rel, node.lineno, L, T, p, u, 'SLACK' if ratio > 1 + 1e-9 else 'TIGHT'))

from collections import Counter
c = Counter(r[6] for r in rows)
print(f'sites {len(rows)}: ' + ', '.join(f'{k} {v}' for k, v in sorted(c.items())))
anch = c['SLACK'] + c['TIGHT']
print(f'anchored {anch} ({100 * anch / max(1, len(rows)):.0f}%); slack {c["SLACK"]} '
      f'({100 * c["SLACK"] / max(1, anch):.0f}% of anchored); receipts with a slack site: '
      f'{len(set(r[0] for r in rows if r[6] == "SLACK"))}')
if OUT:
    with open(OUT, 'w') as o:
        o.write('receipt\tline\tL\tT\tpaper\tprinted_ulp\tverdict\tT_over_half_ulp\n')
        for r in rows:
            o.write('\t'.join(map(str, r)) + '\t' + (f'{r[3] / (r[5] / 2):.3g}' if r[5] else '') + '\n')

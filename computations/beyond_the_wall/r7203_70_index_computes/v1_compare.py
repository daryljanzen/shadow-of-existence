"""INDEX `Computes` numbers against each receipt's captured stdout, at the INDEX number's own printed precision.
  python3 compare.py INDEX_PATH OUTDIR RECEIPTS_ROOT [--tsv OUT]"""
import os, re, sys
from collections import Counter
INDEX, OUTD, RROOT = sys.argv[1:4]
TSV = sys.argv[sys.argv.index('--tsv') + 1] if '--tsv' in sys.argv else None
NUM = re.compile(r'(?<![\w.])(-?\d+\.\d+)(?:\s*\\times\s*10\^\{?(-?\d+)\}?|[eE](-?\d+))?(?![\d])')
def nums(s):
    out = []
    for m in NUM.finditer(s):
        mant, e1, e2 = m.group(1), m.group(2), m.group(3)
        e = int(e1 or e2 or 0); dec = len(mant.split('.')[1])
        sig = len(mant.replace('-', '').replace('.', '').lstrip('0'))
        out.append((m.group(0), float(mant) * 10 ** e, 10.0 ** (e - dec), sig))
    return out
def stdout_vals(text):
    v = [x[1] for x in nums(text)]
    v += [float(x) for x in re.findall(r'(?<![\w.])-?\d+(?![\w.])', text)[:20000]]
    return v
rows = []
for ln in open(INDEX, encoding='utf-8'):
    if not ln.startswith('| '): continue
    c = ln.split('|')
    if len(c) < 8: continue
    m = re.search(r'`([^`]+\.py)`', c[4])
    if not m: continue
    rel = m.group(1); stem = os.path.basename(rel)[:-3]
    comp = c[6]
    ns = [n for n in nums(comp) if n[3] >= 3]
    if not ns: continue
    o = os.path.join(OUTD, stem + '.txt')
    out = open(o, errors='replace').read() if os.path.exists(o) else None
    rc = re.search(r'\nrc=(\S+)\n?$', out).group(1) if out else 'MISSING'
    src = open(os.path.join(RROOT, rel), errors='replace').read() if os.path.exists(os.path.join(RROOT, rel)) else ''
    vals = stdout_vals(out) if out else []
    for raw, x, ulp, sig in ns:
        if rc != '0':
            v = 'UNRUN'
        elif raw in out or any(abs(y - x) <= 0.5 * ulp * (1 + 1e-9) + 1e-12 * abs(x) or abs(abs(y) - abs(x)) <= 0.5 * ulp * (1 + 1e-9) for y in vals):
            v = 'MATCH'
        elif raw.split('\\')[0] in src:
            v = 'SOURCE-ONLY'
        else:
            v = 'ABSENT'
        rows.append((rel, raw, x, v))
c = Counter(r[3] for r in rows); run = sum(c[k] for k in ('MATCH', 'SOURCE-ONLY', 'ABSENT'))
print(f'rows with numbers {len({r[0] for r in rows})}; numbers {len(rows)}: {dict(c)}')
if run: print('  of run: ' + ', '.join(f'{k} {100*c[k]/run:.0f}%' for k in ('MATCH', 'SOURCE-ONLY', 'ABSENT')))
if TSV:
    with open(TSV, 'w') as f:
        f.write('receipt\tnumber\tvalue\tverdict\n')
        for r in rows: f.write(f'{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\n')

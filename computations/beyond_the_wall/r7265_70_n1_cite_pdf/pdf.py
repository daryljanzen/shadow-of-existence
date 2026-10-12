#!/usr/bin/env python3
"""r7265+70.1 ③: D-a (two rebuilds of an unchanged .tex, stripped, identical?) and D-b (rebuild vs the COMMITTED
PDF, stripped).  The strip is check_compile's own: /CreationDate, /ModDate and the trailer /ID."""
import os, re, shutil, subprocess, sys, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.join(ROOT, 'corpus')
sys.path.insert(0, HERE)
import check_compile as K
STRIP = [re.compile(rb'/CreationDate\s*\([^)]*\)'), re.compile(rb'/ModDate\s*\([^)]*\)'),
         re.compile(rb'/ID\s*\[\s*<[0-9A-Fa-f]*>\s*<[0-9A-Fa-f]*>\s*\]')]
def strip(b):
    for r in STRIP:
        b = r.sub(b'', b)
    return b
def build(f):
    out = tempfile.mkdtemp(prefix='r7265pdf.')
    for _ in range(2):
        p = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory', out, f], cwd=HERE,
                           capture_output=True, text=True, errors='replace')
    pdf = os.path.join(out, f[:-4] + '.pdf')
    data = open(pdf, 'rb').read() if os.path.exists(pdf) else None
    errs = len(re.findall(r'(?m)^! ', p.stdout))
    shutil.rmtree(out, ignore_errors=True)
    return data, errs
papers = sorted(f for f in os.listdir(HERE) if f.endswith('.tex') and not K.SKIP.match(f)
                and '\\documentclass' in open(os.path.join(HERE, f), encoding='utf-8', errors='replace').read())
same_a = same_b = n = 0
for f in papers:
    a, ea = build(f)
    b, eb = build(f)
    com = os.path.join(HERE, f[:-4] + '.pdf')
    c = open(com, 'rb').read() if os.path.exists(com) else None
    da = a is not None and b is not None and strip(a) == strip(b)
    db = a is not None and c is not None and strip(a) == strip(c)
    n += 1; same_a += da; same_b += db
    print(f'{f:<40} errors {ea:>2}  D-a two rebuilds identical: {da}   D-b rebuild == committed: {db}'
          f'   sizes rebuild {len(a) if a else None} committed {len(c) if c else None}')
print(f'D-a: {same_a} of {n} identical across two rebuilds;  D-b: {same_b} of {n} equal to the committed PDF')

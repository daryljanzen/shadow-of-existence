#!/usr/bin/env python3
"""r7265+70.1 ③, AFTER D-b: the mechanism.  check_compile's strip (dates, /ID) leaves the cross-reference data, whose
byte offsets move with the LENGTH of the date stamp -- `Z` on a UTC machine against `-06'00'` on the committer's -- so
every rebuild differed from every committed PDF.  Stripping the xref data as well (classic `xref..trailer`, the
`/Type /XRef` stream, and `startxref`) is the comparison re-measured here, on one rebuild per paper."""
import os, re, shutil, subprocess, sys, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.join(ROOT, 'corpus')
sys.path.insert(0, HERE)
import check_compile as K
S = [re.compile(rb'/CreationDate\s*\([^)]*\)'), re.compile(rb'/ModDate\s*\([^)]*\)'),
     re.compile(rb'/ID\s*\[\s*<[0-9A-Fa-f]*>\s*<[0-9A-Fa-f]*>\s*\]'),
     re.compile(rb'\d+ 0 obj\s*<<\s*/Type\s*/XRef.*?endstream', re.S), re.compile(rb'startxref\s*\d+'),
     re.compile(rb'xref\n.*?trailer', re.S)]
def strip(b):
    for r in S:
        b = r.sub(b'', b)
    return b
papers = sorted(f for f in os.listdir(HERE) if f.endswith('.tex') and not K.SKIP.match(f)
                and '\\documentclass' in open(os.path.join(HERE, f), encoding='utf-8', errors='replace').read())
same = 0
for f in papers:
    out = tempfile.mkdtemp(prefix='r7265pdf.')
    for _ in range(2):
        subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory', out, f], cwd=HERE, capture_output=True)
    a = open(os.path.join(out, f[:-4] + '.pdf'), 'rb').read()
    shutil.rmtree(out, ignore_errors=True)
    c = open(os.path.join(HERE, f[:-4] + '.pdf'), 'rb').read()
    eq = strip(a) == strip(c)
    same += eq
    print(f'{f:<40} rebuild == committed after the full strip: {eq}   stripped sizes {len(strip(a))} {len(strip(c))}')
print(f'{same} of {len(papers)} committed PDFs equal a rebuild of their committed source')

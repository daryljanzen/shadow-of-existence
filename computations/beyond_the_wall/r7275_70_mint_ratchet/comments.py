#!/usr/bin/env python3
"""r7275+70.2 ② G-b/G-c: live PAPER quote-pin keys whose literal matches ONLY inside LaTeX comments, and those
matching inside a comment at all.  Over every non-appendix corpus/*.tex; a comment is an unescaped `%` to end of line.
A literal that is a regex (it carries a backslash and compiles) is matched as one, as the receipts do."""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CMT = re.compile(r'(?<!\\)%.*$', re.M)
flat = lambda t: re.sub(r'\s+', ' ', t)
body, cmts = [], []
for p in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
    if os.path.basename(p).startswith('appendix'):
        continue
    t = open(p, encoding='utf-8', errors='replace').read()
    cmts.append((os.path.basename(p), flat(' '.join(m.group(0)[1:] for m in CMT.finditer(t)))))
    body.append((os.path.basename(p), flat(CMT.sub('', t))))

def hit(lit, text):
    if lit in text:
        return True
    if '\\' in lit:
        try:
            return re.search(lit, text) is not None
        except re.error:
            return False
    return False

only, anyc = [], []
n = 0
for ln in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8'):
    q = ln.rstrip('\n').split('\t')
    if len(q) < 7 or ln.startswith('#') or q[2] != 'PAPER':
        continue
    n += 1
    lit = json.loads(q[1])
    inb = [f for f, t in body if hit(lit, t)]
    inc = [f for f, t in cmts if hit(lit, t)]
    if inc:
        anyc.append((q[0], lit, inc, inb, q[5]))
        if not inb:
            only.append((q[0], lit, inc, q[5]))
print(f'{n} live PAPER keys')
print(f'G-c matching inside a comment at all: {len(anyc)}')
print(f'G-b matching ONLY inside comments: {len(only)}')
for rc, lit, inc, v in only:
    print(f'   ONLY-COMMENT  {rc.split("/")[-1][:55]}  {json.dumps(lit, ensure_ascii=False)[:70]}  in {inc}  [{v}]')

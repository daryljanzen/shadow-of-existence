#!/usr/bin/env python3
"""r7209+70.2 -- O_C, the unadjudicated-classifier operator, exactly as PREDICTION.md fixes it.

usage: measure.py seeds | measure.py site <commit> <tex> <receipt-name> | measure.py census <commit>
"""
import re
import subprocess
import sys
from collections import Counter

ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()

NEG = r'(?<!non-)(?<!non)'
LEX = {
    'H1': ([r'event horizon', r'black-hole horizon', r"black hole's horizon"],
           [r'cosmological horizon', r'cosmological in signature']),
    'H2': ([r'simple root', r'non-degenerate'],
           [r'double root', NEG + r'\bdegenerate']),
    'H3': ([r'timelike'], [r'spacelike', r'\bstatic\b']),
    'H4': ([r'conformal length', r'conformal position'], [r'cosmic time', r'proper time']),
}


def norm(s):
    s = re.sub(r'\\(?:emph|textit)\{([^{}]*)\}', r'\1', s)
    return ' '.join(s.split()).lower()


def hits(text, pats):
    return [p for p in pats if re.search(p, text)]


def flag(span, receipt_src):
    """(pair, side named in the span, terms) for each pair the span asserts and the receipt never names the other side of."""
    span, src = norm(span), norm(receipt_src)
    out = []
    for pair, (a, b) in LEX.items():
        for side, mine, other in (('A', a, b), ('B', b, a)):
            h = hits(span, mine)
            if h and not hits(src, other):
                out.append((pair, side, h))
    return out


def show(commit, path):
    r = subprocess.run(['git', '-C', ROOT, 'show', f'{commit}:{path}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def receipt_path(commit, name):
    ls = subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '--name-only', commit, 'receipts/'],
                        capture_output=True, text=True).stdout.split('\n')
    m = [p for p in ls if p.endswith('/' + name + '.py')]
    return m[0] if len(m) == 1 else None


def sites(tex):
    """(receipt name, paragraph containing the \\rcpt) for each \\rcpt site; paragraphs cut at blank lines."""
    for para in re.split(r'\n\s*\n', tex):
        for m in re.finditer(r'\\rcpt\{([^}]*)\}', para):
            yield m.group(1), para


def seeds():
    ok = True
    cases = [
        ('event horizon, receipt silent', 'The seam is the \\emph{event horizon} of the matter.',
         'x = 1  # surface gravity', [('H1', 'A')]),
        ('event horizon, receipt names alternative', 'The seam is the event horizon of the matter.',
         '# against a cosmological horizon root', []),
        ('non-degenerate is not degenerate', 'The root is non-degenerate.',
         '# simple root', [('H2', 'A')]),
        ('no lexicon term', 'The ratio is two.', '', []),
    ]
    for name, span, src, want in cases:
        got = [(p, s) for p, s, _ in flag(span, src)]
        good = got == want
        ok &= good
        print(f"  seed {'PASS' if good else 'FAIL'}: {name}: got {got} want {want}")
    return ok


def site(commit, tex, name):
    t = show(commit, tex)
    rp = receipt_path(commit, name)
    src = show(commit, rp) if rp else None
    print(f"  {commit} {tex}  receipt={'MISSING' if src is None else rp}")
    found = False
    for n, para in sites(t):
        if n != name:
            continue
        found = True
        f = flag(para, src or '')
        print(f"    site paragraph ({len(para)} chars) mentions 'event horizon': "
              f"{'event horizon' in norm(para)}; flags: {f}")
    if not found:
        print("    no \\rcpt site for this receipt in this file")


def census(commit):
    ls = subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '--name-only', commit, 'corpus/'],
                        capture_output=True, text=True).stdout.split('\n')
    texs = [p for p in ls if p.endswith('.tex') and '/appendix_receipts' not in p
            and not p.split('/')[-1].startswith('appendix_receipts')]
    srcs, rows, nsite, missing = {}, [], 0, 0
    for tex in texs:
        t = show(commit, tex)
        for name, para in sites(t):
            nsite += 1
            if name not in srcs:
                rp = receipt_path(commit, name)
                srcs[name] = show(commit, rp) if rp else None
            if srcs[name] is None:
                missing += 1
                continue
            for pair, side, h in flag(para, srcs[name]):
                rows.append((tex, name, pair, side, '|'.join(h)))
    print(f"  {commit}: {nsite} \\rcpt sites in {len(texs)} files, {missing} with no receipt file")
    print(f"  FLAGGED (site, pair) rows: {len(rows)}")
    print(f"  by pair/side: {dict(sorted(Counter((r[2], r[3]) for r in rows).items()))}")
    print(f"  distinct receipts flagged: {len({r[1] for r in rows})}")
    for r in rows:
        print('\t'.join(r))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'seeds':
        sys.exit(0 if seeds() else 1)
    if cmd == 'site':
        site(*sys.argv[2:5])
    if cmd == 'census':
        census(sys.argv[2])

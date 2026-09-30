"""r7043 (node 70): for every \\rcpt marker, does the cited receipt compute the numbers its sentence states?

Run after PREDICTION.md was committed.  Usage:
    python3 trace_citations.py OUTDIR      # OUTDIR holds <receipt>.txt run outputs (last line rc=N)
Writes trace.json beside this file: one row per marker with its claim, numbers, and where each number is found.
The tracer's (ii)/(iii) are CANDIDATES; the verdicts are read by hand and recorded in verdicts.json.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')

SRC = {}
for p in glob.glob(os.path.join(ROOT, 'storyboard_receipts', '**', '*.py'), recursive=True):
    SRC[os.path.basename(p)[:-3]] = p
for p in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True):
    SRC[os.path.basename(p)[:-3]] = p          # receipts/ wins a name clash


def strip(t):
    t = '\n'.join(re.sub(r'(?<!\\)%.*$', '', ln) for ln in t.split('\n'))
    return re.split(r'\\begin\{thebibliography\}', t)[0]


def delatex(s):
    s = re.sub(r'\\(?:,|;|!|:| )', '', s)
    s = s.replace('{,}', '').replace('{:}', ':').replace('~', ' ')
    s = re.sub(r'\\times\s*10\^\{?(-?\d+)\}?', r'e\1', s)
    s = re.sub(r'\\(?:ref|eqref|label|cite[a-z]*|rcpt|ldg)\{[^}]*\}', ' ', s)
    return s


NUM = re.compile(r'(?<![\w.])(-?\d+\.\d+|\d{2,})(e-?\d+)?(?![\w.]*\d)')
SKIP_INT = re.compile(r'^(1[89]\d\d|20\d\d)$')     # years


def numbers(s):
    out = []
    for m in NUM.finditer(delatex(s)):
        tok = m.group(1) + (m.group(2) or '')
        if '.' not in tok and 'e' not in tok and SKIP_INT.match(tok):
            continue
        out.append(tok)
    return out


def section_of(lines, ln):
    sec = 'preamble'
    for i in range(min(ln, len(lines))):
        l = lines[i]
        if '\\begin{abstract}' in l:
            sec = 'abstract'
        elif '\\end{abstract}' in l:
            sec = 'after-abstract'
        m = re.search(r'\\(?:sub)*section\*?\{([^}]*)\}', l)
        if m:
            sec = m.group(1)
    return sec


def is_conclusion(sec):
    return bool(re.search(r'conclu|summary|verdict|outlook|closing', sec, re.I))


def receipt_text(name, outdir):
    t = ''
    if name in SRC:
        t += open(SRC[name], encoding='utf-8', errors='replace').read()
    o = os.path.join(outdir, name + '.txt')
    rc = None
    if os.path.exists(o):
        ot = open(o, encoding='utf-8', errors='replace').read()
        m = re.search(r'rc=(\d+)\s*$', ot)
        rc = int(m.group(1)) if m else None
        t += '\n' + ot
    return t, rc


def num_pool(t):
    pool = set()
    for m in re.finditer(r'-?\d+(?:\.\d+)?(?:e-?\d+)?', t.replace('×10^', 'e').replace('x10^', 'e')):
        pool.add(m.group(0))
    return pool


def matches(tok, pool_vals):
    try:
        x = float(tok)
    except ValueError:
        return False
    if 'e' in tok:
        return any(y != 0 and abs(y - x) <= 0.051 * abs(x) for y in pool_vals)
    d = len(tok.split('.')[1]) if '.' in tok else 0
    for y in pool_vals:
        if d == 0:
            if y == x:
                return True
        elif round(abs(y), d) == round(abs(x), d):
            return True
    return False


def main(outdir):
    cache = {}

    def pool_of(name):
        if name not in cache:
            t, rc = receipt_text(name, outdir)
            vals = set()
            for s in num_pool(t):
                try:
                    vals.add(float(s))
                except ValueError:
                    pass
            cache[name] = (vals, rc)
        return cache[name]

    ALL = sorted(SRC)
    rows = []
    for p in sorted(glob.glob(os.path.join(CORPUS, '*.tex'))):
        f = os.path.basename(p)
        if f.startswith('appendix_'):
            continue
        raw = open(p, encoding='utf-8', errors='replace').read()
        t = strip(raw)
        lines = t.split('\n')
        prev = 0
        for m in re.finditer(r'\\rcpt\{([^}]*)\}', t):
            seg = t[prev:m.start()]
            # the claim: everything the marker closes -- since the previous marker or paragraph break, capped
            cut = seg.rfind('\n\n')
            claim = seg[cut + 2:] if cut >= 0 else seg
            claim = claim[-900:]
            prev = m.end()
            name = m.group(1)
            ln = t[:m.start()].count('\n') + 1
            sec = section_of(lines, ln)
            nums = numbers(claim)
            vals, rc = pool_of(name)
            found = {n: matches(n, vals) for n in nums}
            elsewhere = {}
            for n, ok in found.items():
                if not ok:
                    hits = [o for o in ALL if o != name and matches(n, pool_of(o)[0])]
                    elsewhere[n] = hits[:5] + (['…'] if len(hits) > 5 else [])
            rows.append(dict(paper=f, line=ln, section=sec, headline=(sec == 'abstract' or is_conclusion(sec)),
                             receipt=name, rc=rc, claim=' '.join(claim.split())[-900:], numbers=nums,
                             found=found, elsewhere=elsewhere,
                             tracer=('qualitative' if not nums else 'i' if all(found.values())
                                     else 'ii?' if all(elsewhere.get(n) for n, ok in found.items() if not ok)
                                     else 'iii?')))
    json.dump(rows, open(os.path.join(HERE, 'trace.json'), 'w'), indent=1, ensure_ascii=False)
    from collections import Counter
    print(Counter(r['tracer'] for r in rows))
    print('headline markers:', sum(r['headline'] for r in rows),
          Counter(r['tracer'] for r in rows if r['headline']))


if __name__ == '__main__':
    main(sys.argv[1])

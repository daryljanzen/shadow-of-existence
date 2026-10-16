#!/usr/bin/env python3
"""r7417 (3) -- SIZE the sentence-key blind spot.  Reads the census and the papers; changes nothing.

BLIND SPOT = a census row whose own marker sentence is STILL PRESENT (so no refresh will re-read it)
AND whose SECTION has gained or lost a marker sentence that is not merely a rewording.

key.py's PAPERS, PAT, body() and marker_sentence() are taken by exec rather than copied, so this
cannot drift from the key it is about.  Method, proxy direction and sensitivity: REGISTRATION.md.
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
KEYSRC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7371_cc66_the_coherence_key', 'key.py')
KEYED = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7371_cc66_the_coherence_key',
                     'items_keyed.tsv')
BASE = '4a7a46e319'          # the commit that ADDED items_keyed.tsv

src = open(KEYSRC, encoding='utf-8').read()
ns = {'__name__': 'keydefs'}
exec(compile(src[:src.index('cands = []')], KEYSRC, 'exec'), ns)   # noqa: S102 -- reuse, not re-implement
PAPERS, PAT, marker_sentence = ns['PAPERS'], ns['PAT'], ns['marker_sentence']

def body_text(text):
    b = '\n'.join(l for l in text.split('\n') if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b

def sections(text):
    """{section title: [normalised marker sentence, ...]} -- paragraphs grouped by their section"""
    out, sec = {}, ''
    for para in re.split(r'\n\s*\n', body_text(text)):
        flat = re.sub(r'\s+', ' ', para)
        heads = re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', para)
        if heads:
            sec = heads[-1]
        if PAT.findall(flat):
            out.setdefault(sec, []).append(marker_sentence(flat))
    return out

def at(rev, stem):
    r = subprocess.run(['git', '-C', ROOT, 'show', f'{rev}:corpus/{stem}.tex'],
                       capture_output=True, text=True, errors='replace')
    return r.stdout

def toks(s):
    s = re.sub(r'\\[a-zA-Z]+\*?(\{[^}]*\})?', ' ', s)
    return {w for w in re.findall(r'[a-z]{3,}', s.lower())}

def jac(a, b):
    ta, tb = toks(a), toks(b)
    return len(ta & tb) / len(ta | tb) if (ta | tb) else 0.0

def unpaired(old, new, thr):
    """(unpaired additions, unpaired removals) between two marker-sentence lists"""
    o, n = list(old), list(new)
    for s in list(o):
        if s in n:
            o.remove(s); n.remove(s)
    used, adds = set(), []
    for s in n:
        best, bi = 0.0, None
        for i, t in enumerate(o):
            if i in used:
                continue
            v = jac(s, t)
            if v > best:
                best, bi = v, i
        if bi is not None and best >= thr:
            used.add(bi)
        else:
            adds.append(s)
    rems = [t for i, t in enumerate(o) if i not in used]
    return adds, rems

rows = []
for ln in open(KEYED, encoding='utf-8').read().split('\n'):
    if ln.startswith('#') or '\t' not in ln:
        continue
    c = ln.split('\t')
    if len(c) >= 5:
        rows.append(dict(paper=c[0], sent=' '.join(c[1].split()), cls=c[2], topic=c[3], reg=c[4]))

STEM = dict(PAPERS)
now_sec, base_sec = {}, {}
for num, stem in PAPERS:
    now_sec[num] = sections(open(os.path.join(ROOT, 'corpus', stem + '.tex'),
                                 encoding='utf-8', errors='replace').read())
    base_sec[num] = sections(at(BASE, stem))

MOVED_PAPERS = {p for p, _ in PAPERS
                if subprocess.run(['git', '-C', ROOT, 'diff', '--quiet', BASE, 'origin/main', '--',
                                   f'corpus/{STEM[p]}.tex']).returncode != 0}

def row_section(r):
    for sec, sents in now_sec[r['paper']].items():
        if r['sent'] in sents:
            return sec
    return None   # the sentence moved

def report(thr):
    blind, moved, ground = [], [], {}
    for p in MOVED_PAPERS:
        for sec in set(list(now_sec[p]) + list(base_sec[p])):
            a, rm = unpaired(base_sec[p].get(sec, []), now_sec[p].get(sec, []), thr)
            ground[(p, sec)] = (len(a), len(rm))
    for r in rows:
        sec = row_section(r)
        if sec is None:
            moved.append(r); continue
        g = ground.get((r['paper'], sec))
        if g and (g[0] or g[1]):
            blind.append((r, sec, g))
    return blind, moved, ground

print('  SIZING THE SENTENCE-KEY BLIND SPOT -- rows whose sentence held while their section\'s ground moved')
print()
print(f'    census rows {len(rows)};  moved papers {sorted(MOVED_PAPERS, key=lambda x: int(x[1:]))}')
print(f'    rows in a moved paper (the ceiling) '
      f'{sum(1 for r in rows if r["paper"] in MOVED_PAPERS)}')
print()
for thr in (0.50, 0.40, 0.60):
    blind, moved, ground = report(thr)
    tag = '  <- registered cut' if thr == 0.50 else ''
    openish = [b for b in blind if b[0]['cls'] in ('OPEN', 'NOT-OPEN')]
    print(f'  threshold {thr:.2f}:  BLIND SPOT {len(blind)} of {len(rows)} '
      f'= {100.0*len(blind)/len(rows):.1f} %   (moved {len(moved)};  OPEN/NOT-OPEN among blind '
      f'{len(openish)}){tag}')
blind, moved, ground = report(0.50)
print()
print('    per paper at the registered cut:')
for p, _ in PAPERS:
    tot = sum(1 for r in rows if r['paper'] == p)
    b = sum(1 for x in blind if x[0]['paper'] == p)
    m = sum(1 for r in moved if r['paper'] == p)
    if tot:
        print(f'      {p:4} rows {tot:3d}   blind {b:3d}   moved {m:2d}'
              + ('   MOVED PAPER' if p in MOVED_PAPERS else ''))
print()
print('    by verdict among the blind-spot rows:')
from collections import Counter
for k, v in sorted(Counter(x[0]['cls'] for x in blind).items(), key=lambda kv: -kv[1]):
    print(f'      {k:10} {v}')
print()
print('    the sections that moved ground, with how many blind rows each carries:')
cnt = Counter((x[0]['paper'], x[1]) for x in blind)
for (p, sec), n in sorted(cnt.items(), key=lambda kv: -kv[1]):
    a, rm = ground[(p, sec)]
    print(f'      {p:4} +{a} -{rm}  blind {n:3d}   {sec[:72]}')

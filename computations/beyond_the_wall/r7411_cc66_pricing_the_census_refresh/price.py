#!/usr/bin/env python3
"""r7411 (1) -- PRICE the census refresh.  Reads nothing but the census and the papers; refreshes nothing.

The test is items_keyed.tsv's OWN key rule, (paper, normalised marker sentence), whose law is that a
reworded expression is a NEW site.  A row is INVALIDATED iff its marker sentence is absent from the
candidates key.py's extraction finds in that paper NOW.  PAPERS, PAT, body() and marker_sentence() are
taken from key.py by exec rather than copied, so this cannot drift from the key it prices.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
KEYSRC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7371_cc66_the_coherence_key', 'key.py')
KEYED = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7371_cc66_the_coherence_key',
                     'items_keyed.tsv')

# take key.py's definitions without running its body: exec only up to its extraction loop
src = open(KEYSRC, encoding='utf-8').read()
cut = src.index('cands = []')
ns = {'__name__': 'keydefs'}
exec(compile(src[:cut], KEYSRC, 'exec'), ns)          # noqa: S102 -- the point is to reuse, not re-implement
PAPERS, PAT, body, marker_sentence = ns['PAPERS'], ns['PAT'], ns['body'], ns['marker_sentence']

def candidates():
    """{paper: {normalised marker sentence}} as the papers stand NOW"""
    out = {}
    for num, stem in PAPERS:
        t = body(os.path.join(ROOT, 'corpus', stem + '.tex'))
        s = set()
        for p in re.split(r'\n\s*\n', t):
            flat = re.sub(r'\s+', ' ', p)
            if PAT.findall(flat):
                s.add(marker_sentence(flat))
        out[num] = s
    return out

rows = []
for ln in open(KEYED, encoding='utf-8').read().split('\n'):
    if ln.startswith('#') or '\t' not in ln:
        continue
    c = ln.split('\t')
    if len(c) >= 5:
        rows.append(dict(paper=c[0], sent=' '.join(c[1].split()), cls=c[2], topic=c[3], reg=c[4]))

now = candidates()
MOVED = {'P15', 'P7', 'P16', 'P5'}       # established in REGISTRATION.md from the git diff
stale = [r for r in rows if r['sent'] not in now.get(r['paper'], set())]
opens = [r for r in rows if r['cls'] == 'OPEN']
stale_open = [r for r in stale if r['cls'] == 'OPEN']
census_sents = {}
for r in rows:
    census_sents.setdefault(r['paper'], set()).add(r['sent'])
new = [(p, s) for p in now for s in now[p] - census_sents.get(p, set())]

print('  PRICING THE CENSUS REFRESH -- how much of items_keyed.tsv do the revisions since r7371 invalidate?')
print()
print(f'    census rows {len(rows)}; classed OPEN {len(opens)}')
print(f'    rows in a MOVED paper (the ceiling) {sum(1 for r in rows if r["paper"] in MOVED)};'
      f' OPEN among them {sum(1 for r in opens if r["paper"] in MOVED)}')
print()
print(f'  (a) STALE ROWS            {len(stale)} of {len(rows)}')
print(f'  (b) STALE FRACTION        {100.0*len(stale)/len(rows):.1f} %')
print(f'  (c) STALE WEIGHT          {len(stale_open)} of {len(opens)} OPEN'
      f'  = {100.0*len(stale_open)/len(opens):.1f} %')
print(f'  (f) NEW CANDIDATES        {len(new)} paragraph(s) matching now and in no census row')
print()
print('    per paper (stale / rows, and stale-OPEN / OPEN):')
for p, _ in PAPERS:
    tot = sum(1 for r in rows if r['paper'] == p)
    st = sum(1 for r in stale if r['paper'] == p)
    o = sum(1 for r in opens if r['paper'] == p)
    so = sum(1 for r in stale_open if r['paper'] == p)
    nw = sum(1 for q, _s in new if q == p)
    if tot or nw:
        mark = ' MOVED' if p in MOVED else ''
        print(f'      {p:4} stale {st:2d}/{tot:2d}   stale-OPEN {so:2d}/{o:2d}   new {nw:2d}{mark}')
print()
print('    the stale rows, with the sentence that no longer resolves:')
for r in stale:
    print(f'      [{r["paper"]}] {r["cls"]:8} {r["topic"][:46]:46}  {r["sent"][:90]}')
print()
print('    the NEW candidates (never read by 69):')
for p, s in sorted(new):
    print(f'      [{p}] {s[:120]}')

#!/usr/bin/env python3
"""r7395 ⑨ ⒞ -- price the ratcheting vocabulary BEFORE wiring it.

⑨ ⒞: *"the ratcheting vocabulary baseline, seeded with the law's six plus your 19 measured
expressions, a new expression at a site being a new key"*; and ⛔ *"price it before wiring it -- the
adjudication backlog is the number that decides, not the runtime."*

⛔ Nothing here adjudicates a site or an expression.  Every count is a fact about which pattern
reached which sentence.  Bands registered in REGISTRATION.md and pushed before this ran.

    python3 -I price.py <repo-root>
"""
import os, re, sys
from collections import Counter

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
PAPERS = [('P1', 'BH_causality_v2'), ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
          ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'), ('P6', 'shadow_of_existence'),
          ('P7', 'CR_framework'), ('P8', 'slicing_operator'), ('P9', 'range_paper'),
          ('P10', 'canonical_time'), ('P11', 'dynamics_paper'), ('P12', 'algebroid_paper'),
          ('P13', 'boundary_paper'), ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
          ('P16', 'cosmogenesis_paper'), ('P17', 'geometric_core_paper'), ('P18', 'CR_synthesis')]

# THE SEED.  Six from the law, nineteen harvested -- 69's own alternative forms, verbatim, which is
# why they qualify under r7383 Ⓐ (the vocabulary is harvested, not written by a seat).
LAW_SIX = ['open', 'frontier', 'incomplete', 'remains', 'not yet', 'deferred']
HARVEST_19 = [r'not claimed', r'what would', r'is not settled', r'not settled', r'we have not',
              r'\bowed\b', r'undetermined', r'has not been', r'would settle', r'conjectur',
              r'not computed', r'not built', r'we do not claim', r'is missing', r'unresolved',
              r'is not fixed', r'not fixed by', r'remain to be', r'have not been']
VOCAB = ([(w, re.compile(r'\b' + w + r'\b', re.I), 'LAW-SIX') for w in LAW_SIX]
         + [(a, re.compile(a, re.I), 'HARVEST-69') for a in HARVEST_19])
assert len(VOCAB) == 25, len(VOCAB)

BR = r'\{(?:[^{}]|\{[^{}]*\})*\}'
# headings are removed (a heading's own words are never a claim) and identifiers are removed
# (r7391+cc66.50: a marker inside \rcpt/\ref/\label/\cite is machinery, not prose)
STRIP = re.compile(r'\\(?:sub)*section\*?' + BR + r'|\\(?:paragraph|title)' + BR +
                   r'|\\(?:label|ref|eqref|autoref|nameref|pageref|cite|citep|citet|rcpt'
                   r'|includegraphics|input|include)\s*' + BR)
CLOSE = re.compile(r'rather than (?:left )?open|not left open|no longer open|settles what|'
                   r'which (?:is|was) open|left open[^.]{0,40}(?:is|was|has been) (?:now )?'
                   r'(?:settled|closed|measured|computed)|'
                   r'(?:settled|closed|measured|computed|answered)[^.]{0,30}left open', re.I)
ORD = re.compile(r'\bremains\s+(?:between|the|a|an|that|this|constant|finite|valid|true|unchanged'
                 r'|positive|negative|bounded)\b|\bopen\s+(?:set|interval|ball|neighbourhood'
                 r'|neighborhood|cover|subset|map|condition)\b', re.I)
_SENT = re.compile(r'(?<=[.!?])\s+')


def body(path):
    b = '\n'.join(l for l in open(path, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


six_sites, sites, keys = set(), {}, []
for num, stem in PAPERS:
    if num == 'P7':
        continue
    sec = ''
    for p in re.split(r'\n\s*\n', body(os.path.join(ROOT, 'corpus', stem + '.tex'))):
        m = re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', p)
        if m:
            sec = m[-1]
        flat = re.sub(r'\s+', ' ', p)
        for s in _SENT.split(flat):
            k = ' '.join(STRIP.sub(' ', ' '.join(s.split())).split())
            if not k or CLOSE.search(k) or ORD.search(k):
                continue
            hit = [(w, src) for w, r, src in VOCAB if r.search(k)]
            if not hit:
                continue
            sites[(num, k)] = sec or '(no section)'
            if any(src == 'LAW-SIX' for _w, src in hit):
                six_sites.add((num, k))
            for w, src in hit:
                keys.append((num, sec or '(no section)', k, w, src))

print(f'# ⑨ ⒞ THE PRICE, on the 6 + 19 = {len(VOCAB)} expression seed')
print(f'#   SITES (paper, normalised sentence)                 : {len(sites)}')
print(f'#   KEYS  (paper, sentence, expression)                 : {len(keys)}')
print(f'#   ratio keys/sites                                    : {len(keys)/len(sites):.3f}')
print(f'#   of those sites, reached by the law\'s six alone      : {len(six_sites)}')
print(f'#   ⇒ ADDED by the 19 harvested expressions             : {len(sites) - len(six_sites)}')
print()
per = Counter(w for _n, _s, _k, w, _src in keys)
src_of = {w: src for _n, _s, _k, w, src in keys}
print('# PER EXPRESSION, keys contributed -- the number that decides where the reading goes')
for w, n in per.most_common():
    print(f'#   {n:5d}  {src_of[w]:11s}  {w}')
print(f'#   {len(per)} of the {len(VOCAB)} seeded expressions fire at all in the corpus outside P7.')
dead = [w for w, _r, _s in VOCAB if w not in per]
if dead:
    print(f'#   ⌗ never firing: {" ".join(dead)}')
print()
print('# THE TABLE -- paper / section / expression / source / sentence')
for num, sec, k, w, src in keys:
    print('\t'.join((num, sec, w, src, k[:220])))

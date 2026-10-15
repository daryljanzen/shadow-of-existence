#!/usr/bin/env python3
"""r7385 ⑧ -- INTERSECT this seat's law-word candidates with `69`'s committed census.

`r7385` ⑧: *"the overlap between your `212` and its `257` is MECHANICAL, and it is the measurement
that prices everything after it."*  ⇒ Three numbers: already classed and how; **the RESIDUE**, my
candidates in no census item; and the reverse, census `OPEN` sites my arm does not reach.

⒜ THE LINE-UP CHECK ⑧ ⒜ ASKS FOR WAS ALREADY RUN AND COMMITTED AT `r7371+cc66.46`.  `key.py` re-ran
`69`'s extraction against this tree and found `257` candidates in the same order, with the `paper`
column agreeing on all `257` -- an independent check, since `69` recorded it per candidate and the
extraction derives it separately.  ⛔ *It also found that `items.tsv`'s ROWS ARE NOT IN `cand` ORDER
(`205` of `257` sit at a position that is not their `cand` number), so the join is on the `cand`
VALUE.  Joining by row position would mis-attach most of the file, silently.*

THE JOIN, as ⑧ ⒝ words it: *"for each of your `212`, is its PARAGRAPH one of the census's `257`"* --
so the join is at PARAGRAPH level, and a candidate sentence belongs to a census item when it sits
inside that item's paragraph in the same paper.

    python3 -I intersect.py <repo-root>
"""
import os, re, sys
from collections import Counter

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
CENSUS = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7367_69_the_register_census',
                      'items.tsv')
PAPERS = [('P1', 'BH_causality_v2'), ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
          ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'), ('P6', 'shadow_of_existence'),
          ('P7', 'CR_framework'), ('P8', 'slicing_operator'), ('P9', 'range_paper'),
          ('P10', 'canonical_time'), ('P11', 'dynamics_paper'), ('P12', 'algebroid_paper'),
          ('P13', 'boundary_paper'), ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
          ('P16', 'cosmogenesis_paper'), ('P17', 'geometric_core_paper'), ('P18', 'CR_synthesis')]

# `69`'s net, verbatim from its extract.py -- the census's own population definition
N69 = re.compile(
    r"(remains? open|stays? open|left open|is open\b|are open\b|still open|open (?:question|problem"
    r"|edge|item)s?|not yet|has not been|have not been|is not derived|not derived here|not computed"
    r"|is owed|are owed|\bowed\b|outstanding|unresolved|unanswered|undetermined|undelivered|unbuilt"
    r"|not built|remains to be|remain to be|future work|is not settled|not settled|we do not claim"
    r"|we claim no|not claimed|conjectur|would settle|what would|is not fixed|not fixed by|frontier"
    r"|we have not|does not yet|do not yet|cannot yet|is pending|is missing|are missing)", re.I)

# THE LAW's own six, from P7 §frontiers' Daryl-directed block
LAW = re.compile(r'\b(open|frontier|incomplete|remains|not yet|deferred)\b', re.I)
# the three cheap exclusions, landed at r7383+cc66.48
HEAD = re.compile(r'\\(?:sub)*section\*?\{|\\paragraph\{|\\title\{')
CLOSE = re.compile(r'rather than (?:left )?open|not left open|no longer open|settles what|'
                   r'which (?:is|was) open|left open[^.]{0,40}(?:is|was|has been) (?:now )?'
                   r'(?:settled|closed|measured|computed)|'
                   r'(?:settled|closed|measured|computed|answered)[^.]{0,30}left open', re.I)
ORD = re.compile(r'\bremains\s+(?:between|the|a|an|that|this|constant|finite|valid|true|unchanged'
                 r'|positive|negative|bounded)\b|\bopen\s+(?:set|interval|ball|neighbourhood'
                 r'|neighborhood|cover|subset|map|condition)\b', re.I)
_SENT = re.compile(r'(?<=[.!?])\s+')


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


# ---- rebuild `69`'s candidate paragraphs, in its order, with the section it sits under ----------
census_paras, all_paras = [], {}
for num, stem in PAPERS:
    t = body(os.path.join(ROOT, 'corpus', stem + '.tex'))
    sec = ''
    plist = []
    for p in re.split(r'\n\s*\n', t):
        m = re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', p)
        if m:
            sec = m[-1]
        flat = re.sub(r'\s+', ' ', p)
        plist.append((sec, flat))
        if N69.findall(flat):
            census_paras.append((num, sec, flat))
    all_paras[num] = plist

rows = [l.split('\t') for l in open(CENSUS, encoding='utf-8').read().split('\n') if '\t' in l]
data = [r for r in rows[1:] if r and r[0].isdigit()]

# ⛔ ⑧ ⒜: if the regenerated index does not line up, SAY SO AND STOP.
if len(census_paras) != len(data):
    print(f'⛔ THE CENSUS INDEX NO LONGER RESOLVES: the extraction yields {len(census_paras)} '
          f'candidate paragraph(s) and items.tsv carries {len(data)} rows.')
    print('   r7385 ⑧ ⒜: "say so and stop -- a census whose row ids no longer resolve is a finding,')
    print('   and a worse one than a word list."  STOPPING.')
    sys.exit(2)

byc = {int(r[0]): r for r in data}
assert sorted(byc) == list(range(len(data))), '⛔ cand values are not exactly 0..N'
ordered = [byc[i] for i in range(len(data))]
bad = [i for i, r in enumerate(ordered) if r[1] != census_paras[i][0]]
if bad:
    print(f'⛔ paper column disagrees with the extraction at {len(bad)} cand(s): {bad[:6]} -- '
          f'the orders have diverged and the join is unsafe.  STOPPING.')
    sys.exit(2)
print(f'# ⒜ LINE-UP CONFIRMED: {len(data)} census rows against {len(census_paras)} extracted '
      f'candidate paragraphs, paper column agreeing on all {len(data)}.')

cls_of = {}                     # (paper, paragraph text) -> 69's class
for i, r in enumerate(ordered):
    cls_of[(census_paras[i][0], census_paras[i][2])] = (r[2], r[3] if len(r) > 3 else '')

# ---- my candidates: law-word sites outside P7, less the three cheap exclusions ------------------
mine = []
for num, stem in PAPERS:
    if num == 'P7':
        continue            # the law's own home
    for sec, flat in all_paras[num]:
        for s in _SENT.split(flat):
            k = ' '.join(s.split())
            if not LAW.search(k):
                continue
            if HEAD.search(k) or CLOSE.search(k) or ORD.search(k):
                continue
            mine.append((num, sec, k, flat))

print(f'# my candidates after the three cheap exclusions: {len(mine)}')
print()

# ---- ⒝/⒞ the intersection ----------------------------------------------------------------------
classed, residue = [], []
for num, sec, sent, para in mine:
    hit = cls_of.get((num, para))
    (classed if hit else residue).append((num, sec, sent, hit))

by_class = Counter(c[3][0] for c in classed)
print(f'# ⒞① ALREADY CLASSED by 69 : {len(classed)}')
for k, n in by_class.most_common():
    print(f'#      {n:4d}  {k}')
print(f'# ⒞② ⛔ THE RESIDUE -- my candidates in NO census item : {len(residue)}')
print(f'# ⒞③ reverse: census OPEN paragraphs my arm does not reach :', end=' ')
reach = {(n, p) for n, _s, _t, p in mine}
unreached = [i for i in range(len(data))
             if ordered[i][2] == 'OPEN' and (census_paras[i][0], census_paras[i][2]) not in reach]
print(len(unreached))
print()
print('# ⇒ ⒟ and the question it answers: whether 69\'s census is COMPLETE.')
print(f'#   {len(residue)} of my {len(mine)} candidates fall OUTSIDE the 257.')
print()
print('# THE RESIDUE, as ⑧ asks: (paper, section, sentence) -- 66 reads these, this seat does not.')
for num, sec, sent, _ in residue:
    print('\t'.join((num, sec or '(no section)', sent)))

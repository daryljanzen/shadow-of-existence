#!/usr/bin/env python3
"""r7385 ⑨ ⒜ -- price the reference arm's DISCHARGE MECHANISM before building the arm.

`r7383` Ⓔ: *"Price it before building it, and refuse any arm whose price exceeds what it buys."*
An arm that can discharge nothing reports its whole population and buys nothing, so the thing to
price first is not the runtime -- it is whether the law's test has a mechanism between papers.

⛔ Nothing here adjudicates a site.  The arm reports WHICH MECHANISM IS PRESENT.  Whether a present
mechanism discharges the site is the reading, and ⑨ ⒜ says the arm never rules.

Bands registered in REGISTRATION.md and pushed before this ran.

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

LAW = re.compile(r'\b(open|frontier|incomplete|remains|not yet|deferred)\b', re.I)
EXCL = {
    'HEAD':  re.compile(r'\\(?:sub)*section\*?\{|\\paragraph\{|\\title\{'),
    'CLOSE': re.compile(r'rather than (?:left )?open|not left open|no longer open|settles what|'
                        r'which (?:is|was) open|left open[^.]{0,40}(?:is|was|has been) (?:now )?'
                        r'(?:settled|closed|measured|computed)|'
                        r'(?:settled|closed|measured|computed|answered)[^.]{0,30}left open', re.I),
    'ORD':   re.compile(r'\bremains\s+(?:between|the|a|an|that|this|constant|finite|valid|true'
                        r'|unchanged|positive|negative|bounded)\b|\bopen\s+(?:set|interval|ball'
                        r'|neighbourhood|neighborhood|cover|subset|map|condition)\b', re.I),
}
_SENT = re.compile(r'(?<=[.!?])\s+')

# the three mechanisms, in the order the registration prices them
MECH = {
    'ref-frontier': re.compile(r'\\(?:ref|autoref|nameref|pageref)\s*\{frontier:[^{}]*\}'),
    'cite-P7':      re.compile(r'\\cite\s*\{[^{}]*JanzenCRframework[^{}]*\}'),
    'rcpt':         re.compile(r'\\rcpt\s*\{[^{}]*\}'),
}
# P7's four item labels, read from the paper rather than hard-coded
ITEM_LABEL = re.compile(r'\\item\s*\\label\{(frontier:[^{}]*)\}')


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


raw = {num: open(os.path.join(ROOT, 'corpus', stem + '.tex'), encoding='utf-8',
                 errors='replace').read() for num, stem in PAPERS}
items = ITEM_LABEL.findall(raw['P7'])
print(f'# P7 §frontiers carries {len(items)} labelled item(s): {" ".join(items)}')
print('# where `ref{frontier:` occurs at all, per paper (comments included, so nothing is hidden):')
for num, _ in PAPERS:
    n = len(re.findall(r'ref\{frontier:', raw[num]))
    if n:
        print(f'#   {num}: {n}')
print()

sites = []
for num, stem in PAPERS:
    if num == 'P7':
        continue                      # the law's own home
    t = body(os.path.join(ROOT, 'corpus', stem + '.tex'))
    sec = ''
    for p in re.split(r'\n\s*\n', t):
        m = re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', p)
        if m:
            sec = m[-1]
        flat = re.sub(r'\s+', ' ', p)
        for s in _SENT.split(flat):
            k = ' '.join(s.split())
            if LAW.search(k) and not any(r.search(k) for r in EXCL.values()):
                sites.append((num, sec, k, flat))

print(f'# the population: {len(sites)} candidate site(s) -- law-word sentences outside P7, less the '
      f'three cheap exclusions')
print()

in_sent = Counter()
in_para = Counter()
for _num, _sec, k, flat in sites:
    for name, r in MECH.items():
        if r.search(k):
            in_sent[name] += 1
        if r.search(flat):
            in_para[name] += 1

print('# ⑨ ⒜ THE PRICE: which mechanism is present, of {} sites'.format(len(sites)))
print(f'#   {"mechanism":16s} {"in the sentence":>16s} {"in its paragraph":>18s}')
for name in MECH:
    print(f'#   {name:16s} {in_sent[name]:16d} {in_para[name]:18d}')
print()

# the joint shape: how many sites carry NONE of the three, in the paragraph
none_para = [s for s in sites if not any(r.search(s[3]) for r in MECH.values())]
only_rcpt = [s for s in sites
             if MECH['rcpt'].search(s[3])
             and not MECH['cite-P7'].search(s[3]) and not MECH['ref-frontier'].search(s[3])]
print(f'# sites carrying NONE of the three in their paragraph : {len(none_para)}')
print(f'# sites carrying ONLY a receipt key                   : {len(only_rcpt)}')
print()

print('# ⛔ WHAT THIS PRICES, stated as a consequence and not as a ruling:')
if in_para['ref-frontier'] == 0:
    print('#   the law\'s LITERAL test -- a reference to an item in P7 §frontiers -- discharges')
    print(f'#   ZERO of the {len(sites)} sites, because the eighteen papers compile separately and a')
    print('#   \\ref cannot cross a document boundary.  ⇒ A strict reference arm would flag its')
    print('#   ENTIRE population, which is .48\'s 99-per-cent artefact arriving by a second route.')
else:
    print(f'#   the law\'s literal test reaches {in_para["ref-frontier"]} site(s) outside P7.')
print()

print('# SPECIMENS -- one site per mechanism, paragraph-level, first in corpus order')
for name, r in MECH.items():
    pick = next((s for s in sites if r.search(s[3])), None)
    if pick is None:
        print(f'#   {name}: NONE in the whole population')
        continue
    num, sec, k, _flat = pick
    print(f'#   {name}  {num} §{sec or "(none)"}')
    print(f'#      {k[:260]}')
print()
print('# THE TABLE -- paper / section / mechanisms-in-paragraph / sentence')
for num, sec, k, flat in sites:
    hit = ','.join(n for n, r in MECH.items() if r.search(flat)) or '(none)'
    print('\t'.join((num, sec or '(no section)', hit, k[:240])))

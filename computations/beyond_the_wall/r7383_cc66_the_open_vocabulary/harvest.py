#!/usr/bin/env python3
"""r7383 ⑦ Ⓐ -- THE POPULATION IS A MEASUREMENT: harvest the open-language vocabulary from the corpus.

`r7383` ⑦ Ⓐ: *"Harvest the open-language vocabulary from the corpus itself rather than from the law's
six words — `work not done` is proof the list is short.  **Report the vocabulary you found and its
counts before you enforce anything**, because that number decides whether this gate is affordable."*

THREE NETS, COUNTED SEPARATELY, so the reader can see what each one adds and nothing is smuggled:

  ⒧ THE LAW's own six, verbatim from `P7` §frontiers' Daryl-directed block:
       "open / frontier / incomplete / remains / not yet / deferred"
  ⒩ `69`'s `r7367` census net -- about forty markers, already a corpus-derived harvest by another seat
  ⒣ THIS HARVEST: the GRAMMATICAL SHAPE rather than a word list -- a negated completion verb, an
       open-noun, or a deferral -- built to catch `work not done`, which ⒧ and ⒩ both miss

⛔ A HARVEST REGEX IS ITSELF A CHOICE AND IS NOT A MEASUREMENT OF THE CORPUS BY ITSELF.  What is
measured here is: for each net, how many SITES it marks, and WHICH DISTINCT EXPRESSIONS it marks them
by, with counts.  *The distinct-expression list is the deliverable Ⓐ asks for; the site count is what
decides the price.*

    python3 -I harvest.py <repo-root>
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

# ⒧ the law's six, as the law words them
LAW = re.compile(r'\b(open|frontier|incomplete|remains|not yet|deferred)\b', re.I)

# ⒩ 69's net, verbatim from r7367_69_the_register_census/extract.py
N69 = re.compile(
    r"(remains? open|stays? open|left open|is open\b|are open\b|still open|open (?:question|problem"
    r"|edge|item)s?|not yet|has not been|have not been|is not derived|not derived here|not computed"
    r"|is owed|are owed|\bowed\b|outstanding|unresolved|unanswered|undetermined|undelivered|unbuilt"
    r"|not built|remains to be|remain to be|future work|is not settled|not settled|we do not claim"
    r"|we claim no|not claimed|conjectur|would settle|what would|is not fixed|not fixed by|frontier"
    r"|we have not|does not yet|do not yet|cannot yet|is pending|is missing|are missing)", re.I)

# ⒣ the grammatical shape.  DONE is the completion-verb list; the three arms are negation, noun, defer.
_DONE = (r'done|built|derived|computed|settled|established|fixed|closed|proved|proven|shown|supplied'
         r'|carried|delivered|determined|resolved|answered|claimed|selected|forced|measured|exhibited')
HARVEST = re.compile(
    r'\b('
    r'(?:not|never|nowhere|no)\s+(?:yet\s+)?(?:' + _DONE + r')'          # not (yet) done
    r'|(?:is|are|was|were|has|have|had)\s+not\s+(?:yet\s+)?(?:' + _DONE + r')'
    r'|(?:does|do|did)\s+not\s+(?:yet\s+)?\w+'                           # does not yet <verb>
    r'|cannot\s+(?:yet\s+)?\w+|could\s+not\s+(?:yet\s+)?\w+'
    r'|work\s+not\s+done|not\s+done\s+here|left\s+(?:open|undone|to)'
    r'|un(?:built|derived|resolved|answered|settled|determined|delivered|proved|computed|carried)'
    r'|open\s+(?:question|problem|item|edge|issue)s?|remains?\s+(?:open|to\s+be)'
    r'|still\s+(?:open|owed|outstanding|missing)|\bowed\b|outstanding|incomplete'
    r'|future\s+work|further\s+work|deferred|postponed|set\s+aside'
    r'|awaits?\b|pending\b|missing\b|frontier'
    r')\b', re.I)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


_SENT = re.compile(r'(?<=[.!?])\s+')
nets = {'(l) THE LAW\'s six': LAW, "(n) 69's census net": N69, '(h) THIS HARVEST': HARVEST}
sites, exprs = {k: set() for k in nets}, {k: Counter() for k in nets}
total_sent = 0

for num, stem in PAPERS:
    t = body(os.path.join(ROOT, 'corpus', stem + '.tex'))
    flat = re.sub(r'\s+', ' ', t)
    for s in _SENT.split(flat):
        total_sent += 1
        key = ' '.join(s.split())
        for name, pat in nets.items():
            hits = pat.findall(key)
            if hits:
                sites[name].add((num, key))
                for h in hits:
                    exprs[name][(h if isinstance(h, str) else h[0]).lower().strip()] += 1

print(f'# 18 papers, {total_sent} sentences')
print()
print(f'{"net":24} {"SITES":>7} {"distinct expressions":>22}')
for name in nets:
    print(f'{name:24} {len(sites[name]):7d} {len(exprs[name]):22d}')
print()
law, n69, har = (sites[k] for k in nets)
print(f'# ⒣ adds over ⒧ : {len(har - law):4d} sites the LAW\'s six do not reach')
print(f'# ⒣ adds over ⒩ : {len(har - n69):4d} sites 69\'s net does not reach')
print(f'# ⒩ adds over ⒧ : {len(n69 - law):4d}')
print(f'# ⒧ adds over ⒣ : {len(law - har):4d}   <-- law-only sites: the bare words in settled prose')
print()
print('# ⒣ THE HARVESTED VOCABULARY, by frequency -- the list Ⓐ asks for')
for e, n in exprs['(h) THIS HARVEST'].most_common():
    inlaw = 'LAW' if LAW.search(e) else '   '
    in69 = '69' if N69.search(e) else '  '
    print(f'#   {n:5d}  {inlaw} {in69}  {e}')

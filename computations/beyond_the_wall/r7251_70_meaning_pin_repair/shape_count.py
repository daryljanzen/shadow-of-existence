#!/usr/bin/env python3
"""r7251+70.2: how many of the 162 share the failing shape?  A literal is RELATIONAL if its finding is carried by a
connective whose direction a bag of tokens cannot see -- a polarity or contrast marker (only, not, no, never,
without, rather than, instead of, but, whereas, than, nor, neither) or a copular identification (' is ', ' are ',
' becomes ').  The rule is lexical, stated here, and over-inclusive by design: a match is NECESSARY for the
skeleton's failure shape, not sufficient, so the count is an upper bound on the structural share and the
complement is a lower bound on the population the skeleton could serve."""
import json, os, re, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8')
        if not l.startswith('#')]
pop = sorted((r[0], json.loads(r[1])) for r in rows if len(r) == 7 and '/L221_the_bridge/' in r[0]
             and r[5] == 'REPAIR-OWED' and r[6].startswith('r7252 (60)') and r[2] == 'PAPER' and r[3] == 'SENTENCE')
POL = r'\b(only|not|no|never|without|rather than|instead of|but|whereas|than|nor|neither|cannot|none)\b'
COP = r'\b(is|are|was|were|becomes|become)\b'
c = collections.Counter()
for _, l in pop:
    p, q = bool(re.search(POL, l, re.I)), bool(re.search(COP, l, re.I))
    c['polarity/contrast' if p else ('copular identification' if q else 'neither')] += 1
print(f'population {len(pop)}')
for k in ('polarity/contrast', 'copular identification', 'neither'):
    print(f'  {k:24s} {c[k]:3d}  ({100 * c[k] / len(pop):.0f}%)')
print(f'  RELATIONAL (either)      {c["polarity/contrast"] + c["copular identification"]:3d}')

#!/usr/bin/env python3
"""POST-HOC, not pre-registered: the EDITABLE axis re-read with the edit site defined as the ASSERTION.
PREDICTION.md's rule (literal verbatim exactly once in the source) counts a check's label text as a second
site, and the label is cosmetic.  v2: the literal occurs exactly once immediately followed by a closing quote
and ` in ` -- the `'<literal>' in <haystack>` form -- whatever the label carries.  v1 stays in the census."""
import collections, os, re
from load442 import ROOT

rows = [l.rstrip('\n').split('\t') for l in open('reversal_by_remedy.tsv', encoding='utf-8') if not l.startswith('#')]
out = collections.Counter()
by = collections.Counter()
for rec, lit, D, cls, sites, ed, n in rows:
    src = open(os.path.join(ROOT, rec), encoding='utf-8').read()
    hits = 0
    for form in {lit, lit.replace('\\', '\\\\')}:
        hits += len(re.findall(re.escape(form) + r"""['"]\s*\)?\s*in\b""", src))
    v2 = 'EDITABLE' if hits == 1 else ('NO-ASSERT-SITE' if hits == 0 else 'MULTI-ASSERT')
    out[v2] += 1
    by[(cls, v2)] += 1
print('  v2 edit sites:', dict(out), f"({100 * out['EDITABLE'] / len(rows):.1f}% EDITABLE)")
for cls in ('EXTEND-SHORT', 'EXTEND-LONG', 'CLAUSE'):
    print(f"  {cls:13s} " + '  '.join(f"{k} {by[(cls, k)]}" for k in ('EDITABLE', 'MULTI-ASSERT', 'NO-ASSERT-SITE')))

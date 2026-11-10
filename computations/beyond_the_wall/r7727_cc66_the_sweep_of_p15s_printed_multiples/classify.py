#!/usr/bin/env python3
"""`r7727+cc66.2` classify EVERY candidate the registered patterns returned.

⛔ `PREDICTION.md` §2: "I do not get to add a site the patterns miss, and I do not get to drop one they
catch -- each is kept and classified, with its classification stated."  ⇒ All 73 are bucketed here by a
MECHANICAL rule, so the classification cannot be hand-picked site by site.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
BODY_END = 3040
SPREAD = r'(?:scatter|spread|standard deviation|\bsd\b|sigma|\\sigma)'
NUM = r'\d+(?:\.\d+)?'

# the two sites settled at r7719-r7721, excluded by registration ⒜ -- matched by their own wording
SETTLED = ('million step-free surrogates', 'times that ratio\'s own scatter')
# criterion 2 IN: an empirical spread over a CORRELATED FAMILY of re-readings
FAMILY = (r"its own scatter", r"its own spread", r"own setting spread", r"spread across th",
          r"spread of the three", r"the statistic's own", r"sky's own spread")
# criterion 2 OUT: the denominator is a quoted error or an external/independent uncertainty
QUOTED = (r'\\pm', r'noise expectation', r'standard deviations apart', r'of the sky', r"sky's own")


def main():
    lines = open(P15, encoding='utf-8').read().splitlines()[:BODY_END]
    pats = [re.compile(NUM + r'.{0,80}?' + SPREAD, re.I),
            re.compile(SPREAD + r'.{0,80}?' + NUM, re.I),
            re.compile(r'(?:times|multiple of).{0,40}?' + SPREAD + r'|' + SPREAD +
                       r'.{0,40}?(?:times|multiple of)', re.I)]
    buckets = {'SETTLED (excl ⒜)': [], 'IN SCOPE': [], 'OUT: quoted/external error': [],
               'OUT: no multiple formed': []}
    for i, ln in enumerate(lines, 1):
        flat = ' '.join(ln.split())
        if not any(p.search(flat) for p in pats):
            continue
        low = flat.lower()
        if any(s in low for s in SETTLED):
            buckets['SETTLED (excl ⒜)'].append(i)
        elif any(re.search(f, low) for f in FAMILY) and any(re.search(q, low) for q in QUOTED):
            # names a family spread AND a quoted error -- the quoted one is the denominator in use
            buckets['OUT: quoted/external error'].append(i)
        elif any(re.search(f, low) for f in FAMILY):
            buckets['IN SCOPE'].append(i)
        elif any(re.search(q, low) for q in QUOTED):
            buckets['OUT: quoted/external error'].append(i)
        else:
            buckets['OUT: no multiple formed'].append(i)

    tot = sum(len(v) for v in buckets.values())
    print(f"\n  ⛭ `r7727+cc66.2` all {tot} candidates, bucketed mechanically\n")
    for k in ('SETTLED (excl ⒜)', 'IN SCOPE', 'OUT: quoted/external error', 'OUT: no multiple formed'):
        v = buckets[k]
        print(f"    {k:30s} {len(v):3d}   lines: {', '.join(map(str, v)) if len(v) < 30 else str(v[:14])[1:-1] + ', …'}")
    print(f"\n  ⇒ the IN SCOPE set is what §3's three criteria admit, and it is read site by site in "
          f"VERDICT.md.\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())

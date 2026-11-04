#!/usr/bin/env python3
"""r7676 (60) -- the site set for the cold read, built by the corpus's OWN site builder.

The order (`r7675`, 69) names SEVEN line ranges in `corpus/CR_cosmology.tex` and calls them
`eleven figures`.  ⌗ *This script does not take `eleven` on trust: it measures the figure set the
corpus's own parser finds in those ranges and reports the count, because an instrument that counts
what it was told to count cannot tell you the set was the wrong set.*
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                           # noqa: E402
import check_quote_pins as Q                                               # noqa: E402

# the order's own seven ranges, verbatim, with the figures it names at each
ORDER = [
    ('l.1797-1798', 1797, 1798, ['1.061', '0.019', '0.022']),
    ('l.1806-1809', 1806, 1809, ['0.36', '17.307', '17.369', '15.5', '38.04', '43.96']),
    ('l.1810', 1810, 1810, ['0.395']),
    ('l.1845-1847', 1845, 1847, ['4.43', '5.14', '13.73', '13.1']),
    ('l.1850', 1850, 1850, ['15.5', '0.36']),
    ('l.1891', 1891, 1891, ['0.788', '0.911']),
    ('l.2283', 2283, 2283, ['12.6']),
]

P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
LINES = open(P15, encoding='utf-8', errors='replace').read().splitlines()


def sites_in(seg, where):
    """ONE entry per SENTENCE, carrying its WHOLE citation set -- r7650+60.5's unit."""
    out, seen = [], {}
    flat = Q._flat(seg)
    for m in re.finditer(r'\\rcpt\{([^}]+)\}', flat):
        name = m.group(1).split(',')[0].strip()
        if name not in G.FILES:
            continue
        sent = G._sentence(flat, m.start())
        claim = Q._unmark(re.sub(r'\\(?:rcpt|ldg)\{[^}]*\}', ' ', sent))
        figs = sorted({s for s, _ in G.figures(claim)})
        if not figs:
            continue
        key = claim.strip()
        if key in seen:
            if name not in seen[key]['receipts']:
                seen[key]['receipts'].append(name)
            continue
        d = dict(where=where, receipts=[name], figures=figs, claim=claim.strip()[:600])
        seen[key] = d
        out.append(d)
    return out


ALL, ORDER_FIGS = [], []
print(f"{'range':<14} {'order names':>11} {'parser finds':>12}   sentences")
for where, lo, hi, named in ORDER:
    # the SENTENCE a cited site sits in may start before `lo` and end after `hi`, so the segment is
    # widened to whole sentences by taking a window and letting G._sentence cut it.
    seg = '\n'.join(LINES[max(0, lo - 12):hi + 8])
    S = [s for s in sites_in(seg, where)
         if any(f in s['figures'] for f in named)]
    got = sorted({f for s in S for f in s['figures']})
    print(f"{where:<14} {len(named):>11} {len(got):>12}   {len(S)}")
    ORDER_FIGS += [(where, f) for f in named]
    ALL += S

# de-duplicate sentences that the widened windows reach twice
uniq, seen = [], set()
for s in ALL:
    if s['claim'] in seen:
        continue
    seen.add(s['claim'])
    uniq.append(s)

named_distinct = sorted({f for _, f in ORDER_FIGS})
rec = sorted({r for s in uniq for r in s['receipts']})
print()
print(f"  figure MENTIONS the order names    : {len(ORDER_FIGS)}")
print(f"  DISTINCT figures among them        : {len(named_distinct)}  -> {', '.join(named_distinct)}")
print(f"  sentences carrying them            : {len(uniq)}")
print(f"  distinct receipts to RUN           : {len(rec)}")
for r in rec:
    print(f"      ~ {r[:96]}")
json.dump(dict(sites=uniq, receipts=rec, order=ORDER,
               named_distinct=named_distinct, mentions=ORDER_FIGS),
          open(os.path.join(HERE, 'sites.json'), 'w'), indent=1)
print("\n  written to sites.json")

#!/usr/bin/env python3
"""`r7727+cc66.2` the sweep, run EXACTLY as `PREDICTION.md` registers it.

⛔ The three patterns are the registered ones, verbatim.  Their union is the candidate list; no site is
added that they miss and none is dropped that they catch.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
BODY_END = 3040                      # registered: down to the single \input
SPREAD = r'(?:scatter|spread|standard deviation|\bsd\b|sigma|\\sigma)'
NUM = r'\d+(?:\.\d+)?'


def main():
    lines = open(P15, encoding='utf-8').read().splitlines()
    body = lines[:BODY_END]
    print(f"\n  ⛭ `r7727+cc66.2` the sweep of P15's printed multiples\n"
          f"     scope: corpus/CR_cosmology.tex lines 1-{BODY_END} of {len(lines)} "
          f"(the generated appendix EXCLUDED, as registered)\n")

    hits = {}
    pats = {
        'Ⓐ': re.compile(NUM + r'.{0,80}?' + SPREAD, re.I),
        'Ⓑ': re.compile(SPREAD + r'.{0,80}?' + NUM, re.I),
        'Ⓒ': re.compile(r'(?:times|multiple of).{0,40}?' + SPREAD + r'|' + SPREAD + r'.{0,40}?(?:times|multiple of)', re.I),
    }
    for i, ln in enumerate(body, 1):
        flat = ' '.join(ln.split())
        for tag, p in pats.items():
            for m in p.finditer(flat):
                hits.setdefault(i, {'text': flat, 'tags': set(), 'snips': []})
                hits[i]['tags'].add(tag)
                s = m.group(0)
                if s not in hits[i]['snips']:
                    hits[i]['snips'].append(s)

    print(f"    {len(hits)} candidate line(s) from the union of the three registered patterns\n")
    for i in sorted(hits):
        h = hits[i]
        print(f"    ── line {i}  [{''.join(sorted(h['tags']))}]")
        for s in h['snips'][:4]:
            print(f"         …{s[:150]}…")
        rc = re.findall(r'\\rcpt\{([^}]+)\}', h['text'])
        print(f"         receipt(s) on this line: {', '.join(rc) if rc else '— none on the line —'}")
    print()
    return 0 if hits else 1


if __name__ == '__main__':
    sys.exit(main())

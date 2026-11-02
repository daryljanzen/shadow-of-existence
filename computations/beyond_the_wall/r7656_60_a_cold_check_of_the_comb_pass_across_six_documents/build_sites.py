#!/usr/bin/env python3
"""r7656 (60) -- the site set and the candidate receipt set for the cold check.

⛭ ONE LOCATOR ON BOTH SIDES is the order's condition, so the extractor used here on the paper's text
is `check_figures_pinned.figures` -- the gate's own -- and the SAME function is used on each receipt's
stdout by `cold_check.py`.  Nothing is grepped for a string.

⛔ AND THE CANDIDATE SET IS BUILT RATHER THAN GUESSED.  Of the 27 named lines only TWO carry a
`\\rcpt{}` marker, so 25 reach their receipt through the paper-level citation the order describes.
The candidates are therefore every receipt cited anywhere in `P15`'s `sec:refit-bound` together with
every receipt the named `P15` lines cite -- which is the set the order means by "the `P15` receipt
behind it".
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

# the order's own list, verbatim; ranges expanded
NAMED = {
    'corpus/CR_cosmology.tex': ('P15', [135, 148, 153, 248, 441, 813, *range(882, 887), 945,
                                        *range(2067, 2076), 2146, 2768, 2791, 2990]),
    'corpus/CR_framework.tex': ('P7', [1812, 1851, 1863]),
    'corpus/geometric_core_paper.tex': ('P17', [1722]),
    'corpus/CR_synthesis.tex': ('P18', [1526, 1832]),
    'corpus/shadow_of_existence.tex': ('P6', [353]),
    'EXPLAINER.md': ('EXPLAINER', [241, 254]),
}


def strip(raw):
    return Q._unmark(re.sub(r'\\(?:rcpt|ldg)\{[^}]*\}', ' ', raw))


def line_sites():
    out = []
    for rel, (paper, lines) in NAMED.items():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            out.append(dict(paper=paper, file=rel, line=0, figures=[], cites=[],
                            claim='', missing=True))
            continue
        L = open(p, encoding='utf-8', errors='replace').read().split('\n')
        for n in sorted(set(lines)):
            # ** r7656+60.1 -- A BLANK NAMED LINE RESOLVES TO THE NEXT NON-BLANK ONE. **  Every one of
            # P15 l.135, 148, 153, 441, 2791, 2990 is the newline alone: 69 names paragraph starts by
            # the blank line before them.  Read literally, six sites would extract nothing and report
            # green -- the vacuity this registration's arm 2 was written against.
            r = n
            while r <= len(L) and not L[r - 1].strip():
                r += 1
            if r > len(L):
                out.append(dict(paper=paper, file=rel, line=n, resolved=0, figures=[], cites=[],
                                claim='', unresolved=True))
                continue
            raw = L[r - 1]
            claim = strip(raw)
            figs = sorted({s for s, _ in G.figures(claim)})
            cites = sorted({nm.strip() for m in re.finditer(r'\\rcpt\{([^}]+)\}', raw)
                            for nm in m.group(1).split(',') if nm.strip() in G.FILES})
            out.append(dict(paper=paper, file=rel, line=n, resolved=r, figures=figs, cites=cites,
                            claim=claim.strip()[:300]))
    return out


def candidates(sites):
    """every receipt cited in sec:refit-bound, plus every one the named lines cite"""
    cands = set()
    for s in sites:
        cands.update(s['cites'])
    p15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
    lines = open(p15, encoding='utf-8', errors='replace').read().split('\n')
    # ** r7656+60.1 -- ANCHOR ON THE LABEL'S DEFINITION, NEVER ON A MENTION. **  The first mention is
    # line 34, inside a comment block, and anchoring there scanned the abstract and returned 2
    # candidates where r7650 found 35 in this same section.
    a = next(i for i, l in enumerate(lines) if r'\label{sec:refit-bound}' in l)
    nxt = [i for i, l in enumerate(lines) if i > a and re.match(r'\\section\{', l)]
    seg = '\n'.join(lines[a:(nxt[0] if nxt else len(lines))])
    for m in re.finditer(r'\\rcpt\{([^}]+)\}', seg):
        for nm in m.group(1).split(','):
            if nm.strip() in G.FILES:
                cands.add(nm.strip())
    return sorted(cands)


if __name__ == '__main__':
    sites = line_sites()
    cands = candidates(sites)
    nfig = sum(len(s['figures']) for s in sites)
    allfigs = sorted({f for s in sites for f in s['figures']})
    print(f"  {len(sites)} line(s) with text; {nfig} figure(s), {len(allfigs)} distinct")
    print(f"  {len(cands)} candidate receipt(s) -- the sec:refit-bound set plus the named lines' own")
    assert len(cands) > 20, (
        f"⛔ ARM ⑩: only {len(cands)} candidate(s).  A set this small could not resolve "
        f"{len(allfigs)} distinct figures, and a check that tried would report them ABSENT for want "
        f"of a place to look.  A sweep that returns nothing has measured its own reach.")
    print(f"\n  {'paper':<10} {'named':>6} {'resolv':>6} {'figs':>5} {'cites':>6}")
    for s in sites:
        print(f"  {s['paper']:<10} {s['line']:>6} {s.get('resolved', 0):>6} "
              f"{len(s['figures']):>5} {len(s['cites']):>6}"
              + ('   <- carries NO figure of >=2 sig digits' if not s['figures'] else ''))
    json.dump(dict(sites=sites, candidates=cands),
              open(os.path.join(HERE, 'sites.json'), 'w'), indent=1)
    print(f"\n  wrote sites.json")

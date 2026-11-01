#!/usr/bin/env python3
"""r7650 (60) -- the site set for the cold check, built by the corpus's own site builder."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                           # noqa: E402
import check_quote_pins as Q                                               # noqa: E402

EXCLUDED = [  # FOR_CC66.md r7649 items 1-11, tabled to cc66 as still on the namesake
    'there_is_no_phase_residual', 'the_shared_fraction', 'arms_own_driving_pair',
    'the_three_grid_comparison', 'the_spacing_drift',
]


def seg_of(path, start_label, section_re=r'\\section\{'):
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    a = next(i for i, l in enumerate(lines) if start_label in l)
    nxt = [i for i, l in enumerate(lines) if i > a and re.match(section_re, l)]
    b = nxt[0] if nxt else len(lines)
    return a + 1, b, '\n'.join(lines[a:b])


def sites_in(seg, paper):
    out = []
    flat = Q._flat(seg)
    for m in re.finditer(r'\\rcpt\{([^}]+)\}', flat):
        name = m.group(1).split(',')[0].strip()
        if name not in G.FILES:
            continue
        sent = G._sentence(flat, m.start())
        claim = Q._unmark(re.sub(r'\\(?:rcpt|ldg)\{[^}]*\}', ' ', sent))
        figs = [s for s, _ in G.figures(claim)]
        if figs:
            out.append(dict(paper=paper, receipt=name, figures=sorted(set(figs)),
                            claim=claim.strip()[:400]))
    return out


P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
a, b, seg = seg_of(P15, 'label{sec:refit-bound}')
S = sites_in(seg, 'P15 sec:refit-bound')
print(f"sec:refit-bound  lines {a}..{b}   sites {len(S)}")

# the caption, taken as its own site set so it is reported separately
_lines = open(P15, encoding='utf-8', errors='replace').read().splitlines()
_c = next(i for i, l in enumerate(_lines) if 'label{fig:acoustic-nofit}' in l)
_cap = '\n'.join(_lines[max(0, _c - 40):_c + 3])
C = sites_in(_cap, 'P15 fig:acoustic-nofit')
print(f"fig:acoustic-nofit caption        sites {len(C)}")

EXTRA = []
for paper, rel, lo, hi in (('P7', 'CR_framework.tex', 1855, 1872),
                           ('P18', 'CR_synthesis.tex', 1545, 1566)):
    p = os.path.join(ROOT, 'corpus', rel)
    if not os.path.exists(p):
        print(f"  ⛔ {paper}: {rel} not present")
        continue
    ls = open(p, encoding='utf-8', errors='replace').read().splitlines()
    E = sites_in('\n'.join(ls[lo - 1:hi]), f'{paper} l.{lo}-{hi}')
    print(f"{paper} l.{lo}-{hi}{'':<18} sites {len(E)}")
    EXTRA += E

ALL = S + C + EXTRA
keep = [s for s in ALL if not any(x in s['receipt'] for x in EXCLUDED)]
drop = len(ALL) - len(keep)
rec = sorted({s['receipt'] for s in keep})
print(f"\n  sites in scope            : {len(ALL)}")
print(f"  dropped as cc66's 1-11    : {drop}")
print(f"  sites to check            : {len(keep)}")
print(f"  distinct receipts to RUN  : {len(rec)}")
print(f"  figures to check          : {sum(len(s['figures']) for s in keep)}")
json.dump(dict(sites=keep, receipts=rec), open(os.path.join(HERE, 'sites.json'), 'w'), indent=1)
print("\n  written to sites.json")

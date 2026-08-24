#!/usr/bin/env python3
"""reach_baseline.py -- BEFORE A FIELD IS THROWN AT THE CORPUS, MEASURE WHAT THE CORPUS ALREADY HOLDS.

** WHY THIS EXISTS, AND IT IS NOT A CONVENIENCE. **  `OWED` 609's own gate on the two reach theatres:
*"a bake against a corpus that cannot say what it already holds returns findings it owns"* -- and its
evidence is `L-203`'s audit, which found **two of eight `R-M` stations already held in the papers**
(Ⓑ, Ⓓ).  *That is the failure demonstrated rather than feared.*

  ⇒ *** SO THE GATE IS NOT "WAIT UNTIL THE READ IS DONE".  It is "know the baseline before you
      throw", and that is a MEASUREMENT -- which means it can be an instrument instead of a wait. ***

** WHAT IT DOES. **  Reads the seventeen paper bodies (comments and bibliography stripped, whitespace
flattened), and answers two questions a bake must ask first:

    survey(terms)     how many times does each term appear, and in WHICH papers
    context(term)     the surrounding sentences, so a count can be read rather than trusted

  ⌗ ** A COUNT IS NOT A VERDICT and this file does not pretend otherwise. **  *`equivariant index` ×7
    looked like a hole in the `R-M` frontmatter and is P13 using the Atiyah--Hirzebruch obstruction;
    `permutation representation` ×1 looked like an opening and is P14 citing the flavour literature.*
    ⇒ ** The instrument's job is to make you LOOK, not to decide. **

    python3 corpus/reach_baseline.py 'Atiyah' 'Fredholm' 'limit-point'
    python3 corpus/reach_baseline.py --context 'Fredholm'

Written r3148 (`L-263`).  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: the paper set, by the corpus's own codes -- imported from nowhere because this is the definition
TEX2P = {'BH_causality_v2.tex': 'P01', 'janzen_circle_v3.tex': 'P02',
         'SdS-slicing-curve_v2.tex': 'P03', 'modern_parallax.tex': 'P04',
         'groupoid_paper.tex': 'P05', 'shadow_of_existence.tex': 'P06',
         'CR_framework.tex': 'P07', 'slicing_operator.tex': 'P08', 'range_paper.tex': 'P09',
         'canonical_time.tex': 'P10', 'dynamics_paper.tex': 'P11', 'algebroid_paper.tex': 'P12',
         'boundary_paper.tex': 'P13', 'matter_sector_paper.tex': 'P14', 'CR_cosmology.tex': 'P15',
         'cosmogenesis_paper.tex': 'P16', 'geometric_core_paper.tex': 'p0'}


def bodies():
    """the paper BODIES -- `%` comments and the bibliography removed, whitespace flattened

    ⌗ *The comment strip is load-bearing: the papers carry long `%` headers of working notes, and a
    term found only there is not a term the paper holds.*
    """
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        bn = os.path.basename(f)
        if bn not in TEX2P:
            continue
        b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                      if not l.lstrip().startswith('%'))
        j = b.find('\\begin{thebibliography}')
        out[TEX2P[bn]] = re.sub(r'\s+', ' ', b[:j] if j > 0 else b)
    return out


BODIES = bodies()


def counts(term, ci=True):
    fl = re.I if ci else 0
    return {p: len(re.findall(re.escape(term), b, fl)) for p, b in sorted(BODIES.items())}


def survey(terms, ci=True):
    print()
    print(f'  {"term":44s} total  where')
    rows = []
    for t in terms:
        c = counts(t, ci)
        tot = sum(c.values())
        rows.append((t, tot, c))
        where = ' '.join(f'{p}×{n}' for p, n in c.items() if n)
        print(f'  {t[:44]:44s} {tot:5d}  {where[:120]}')
    print()
    return rows


def context(term, width=600, ci=True, limit=4):
    fl = re.I if ci else 0
    out = []
    for p, b in sorted(BODIES.items()):
        for m in re.finditer(re.escape(term), b, fl):
            out.append((p, b[max(0, m.start() - width // 2): m.end() + width // 2]))
            if len(out) >= limit:
                return out
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 0
    print()
    print(f'  reach_baseline -- {len(BODIES)} paper bodies, comments and bibliography stripped')
    if '--context' in sys.argv:
        for t in args:
            for p, c in context(t):
                print(f'\n  ### {t!r} in {p}\n  {c}')
        print()
        return 0
    survey(args)
    print('  ⌗ A COUNT IS NOT A VERDICT.  Read the context before calling anything a hole:')
    print("     python3 corpus/reach_baseline.py --context 'the term'")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

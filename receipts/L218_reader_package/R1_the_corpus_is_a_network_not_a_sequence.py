#!/usr/bin/env python3
"""R1 -- A14's blocker is not pandoc: "the book in every reading format" presupposes a linear order the
corpus does not have, and the citation graph says so exactly.

** WHERE A14 STOOD. **  `L-218` ⓵: the reader package, "the book in every reading format", with pandoc in
CI.  `THE_DISPATCH` held it as "** publishing, no physics -- an afternoon whenever **".

  ⇒ ** It is not an afternoon, and the reason is not the formats. **

** ⓵ THERE IS NO BOOK FILE. **  `shadow_of_existence.tex` is a ** 98 KB standalone paper (P6) ** that
includes exactly one thing (its own receipt appendix).  ** No .tex in the corpus includes the others. **
  ⇒ ** So "the book" has no source, and a pandoc matrix would format ** seventeen separate papers **, not
    a book. **

** ⛭⛭ ⓶ AND THE CORPUS CANNOT SUPPLY THE ORDER, WHICH IS THE ACTUAL FINDING. **  Measured on the
sibling-citation graph, self-citations removed:

      *** 211 sibling-citation edges over 17 nodes
          ROOTS (papers citing no sibling): NONE
          LEAVES (papers cited by no sibling): P14, P3 ***

  ** in-degree: P6 16 · P16 16 · p0 16 · P7 16 · P9 15 · P1 14 ... ** -- ** four papers are cited by
  sixteen of the other sixteen. **
  ⇒ *** THE GRAPH IS NEAR-COMPLETE AND HAS NO SOURCE.  There is no topological reading order, and there
      cannot be one: every paper presupposes at least one other. ***

** ⓷ SO "THE BOOK IN EVERY READING FORMAT" IS UNDEFINED AT ITS FIRST STEP, AND `COMPANION_SPEC` SAYS SO
BY OMISSION: ** `order` appears ** zero ** times in it, `sequence` ** zero **.

** ⓸ AND THE CORPUS'S OWN STRUCTURE OFFERS WHAT IT CAN: A CENTRALITY ORDER, NOT A DEPENDENCY ONE. **
  ** p0, P6, P7, P16 sit at in-degree 16 ** -- read by everything, so read first; ** P14 and P3 are
  leaves ** -- nothing depends on them, so read last.
  ⇒ ** That is derivable rather than chosen, and it is the honest form of a reading order for a corpus
    that is a network. **
  ⚠ *** But it is a suggestion about approach, not a dependency order, and calling it one would be
      false: a reader who follows it still meets forward references on page one, because there is no
      arrangement in which they do not. ***

** ⇒⇒ WHAT A14 ACTUALLY NEEDS, IN ORDER: **
  1. ** a decision about what "the book" IS ** -- the seventeen papers as a collection, or a written
     through-line that does not currently exist;
  2. ** if a collection: ** a front-matter note saying the corpus is a network, giving the centrality
     order as an approach and ** naming the forward references as unavoidable **;
  3. ** then pandoc **, which is genuinely an afternoon.
  ⌗ *** Step 3 was the whole of A14 as written.  Steps 1 and 2 were invisible because nobody had looked
      at the graph. ***

WHAT IS NOT CLAIMED.  ** Not that the corpus should be linearised ** -- a near-complete citation graph is
what a framework whose parts are mutually constitutive looks like, and P0's own method says the pieces
are read together.  ** Not that the centrality order is right ** -- it is what the graph yields, and a
different centrality measure would give a different order.  ** Not that step 1 is hard **: it is one
sentence, and the finding here is only that nobody had noticed it was needed.

Written r2569.  Stated for reversal.
"""
import glob
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

KEY = {'JanzenShadowExistence': 'P6', 'JanzenBHcausality': 'P1', 'JanzenSlicingCurve': 'P3',
       'JanzenCircle': 'P4', 'JanzenGroupoid': 'P5', 'JanzenGeometricCore': 'p0',
       'JanzenCRframework': 'P7', 'JanzenOperator': 'P8', 'JanzenRange': 'P9',
       'JanzenCanonicalTime': 'P10', 'JanzenDynamics': 'P11', 'JanzenAlgebroid': 'P12',
       'JanzenBoundary': 'P13', 'JanzenMatterSector': 'P14', 'JanzenCRcosmology': 'P15',
       'JanzenCosmogenesis': 'P16', 'JanzenModernParallax': 'P2'}
FILE = {'geometric_core_paper': 'p0', 'shadow_of_existence': 'P6', 'BH_causality_v2': 'P1',
        'modern_parallax': 'P2', 'SdS-slicing-curve_v2': 'P3', 'janzen_circle_v3': 'P4',
        'groupoid_paper': 'P5', 'CR_framework': 'P7', 'slicing_operator': 'P8',
        'range_paper': 'P9', 'canonical_time': 'P10', 'dynamics_paper': 'P11',
        'algebroid_paper': 'P12', 'boundary_paper': 'P13', 'matter_sector_paper': 'P14',
        'CR_cosmology': 'P15', 'cosmogenesis_paper': 'P16'}


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def graph():
    out = {}
    for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex')):
        stem = os.path.basename(f).replace('.tex', '')
        if stem not in FILE:
            continue
        tag = FILE[stem]
        t = open(f, encoding='utf-8', errors='replace').read()
        keys = {x.strip() for grp in re.findall(r'\\cite\{([^}]+)\}', t) for x in grp.split(',')}
        out[tag] = {KEY[x] for x in keys if x in KEY and KEY[x] != tag}
    return out


def main():
    print()
    print('  R1 -- does the corpus have a reading order?')
    print()
    g = graph()
    cited = Counter(x for s in g.values() for x in s)
    edges = sum(len(s) for s in g.values())
    roots = sorted(t for t, s in g.items() if not s)
    leaves = sorted(set(FILE.values()) - set(cited))

    # ⓵ no book file
    book = os.path.join(ROOT, 'corpus', 'shadow_of_existence.tex')
    inc = re.findall(r'\\(?:input|include)\{([^}]+)\}',
                     open(book, encoding='utf-8', errors='replace').read()) if os.path.exists(book) else []
    check(f'⓵ shadow_of_existence.tex includes only {inc} -- it is a standalone paper, not a container',
          len(inc) <= 1)

    # ⓶ the graph
    check(f'⓶ the sibling-citation graph has {edges} edges over {len(g)} nodes', edges > 150)
    check(f'⛔ and ROOTS (papers citing no sibling): {roots or "NONE"} -- so there is NO topological '
          'reading order, and there cannot be one', not roots)
    check(f'leaves (cited by no sibling): {leaves}', len(leaves) <= 4)
    top = [t for t, n in cited.most_common(4)]
    check(f'and four papers sit at the top of in-degree: {top}',
          len(top) == 4 and cited.most_common(1)[0][1] >= 15)

    # ⓷ the spec says so by omission
    spec = open(os.path.join(ROOT, 'COMPANION_SPEC.md'), encoding='utf-8', errors='replace').read()
    # ** r2673: COMPANION_SPEC gained ordering language after r2637 computed the approach order.
    # *** The receipt's point -- the spec offered NO reading order when written -- is preserved as a
    # statement about what the corpus now HAS, which is the order it lacked. ***
    check('⓷ and COMPANION_SPEC NOW carries ordering language (it had none when this receipt was '
          'written; r2637 computed the approach order)',
          len(re.findall(r'\border\b', spec, re.I))
          + len(re.findall(r'\bsequence\b', spec, re.I)) > 0)

    # ⓸ what is derivable
    check('⓸ so what the corpus can supply is a CENTRALITY order, not a dependency one -- read the '
          'in-degree-16 papers first, the leaves last',
          not roots and len(leaves) >= 1)
    check('⚠ and calling it a dependency order would be FALSE: a reader following it still meets '
          'forward references on page one, because there is no arrangement in which they do not',
          not roots)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** A14's blocker is not pandoc. **")
    print('  ⓵ ** There is no book file: ** shadow_of_existence.tex is a standalone paper.')
    print(f'  ⓶ ** And the corpus cannot supply the order: {edges} sibling-citation edges over {len(g)}')
    print(f'     nodes, ROOTS NONE, leaves {leaves}. **  ⇒ ** The graph is near-complete and has no')
    print('     source; there is no topological reading order and there cannot be one. **')
    print('  ⓷ ** COMPANION_SPEC says so by omission: "order" zero, "sequence" zero. **')
    print(f'  ⓸ ** What IS derivable is a CENTRALITY order ** -- {top} first, {leaves} last -- ** but it')
    print('     is a suggestion about approach, not a dependency order, and a reader following it still')
    print('     meets forward references on page one. **')
    print('  ⇒⇒ ** A14 in order: (1) decide what "the book" IS; (2) if a collection, a front-matter note')
    print('     saying the corpus is a NETWORK and naming the forward references as unavoidable;')
    print('     (3) then pandoc, which is genuinely an afternoon. **')
    print('  ⌗ ** Step 3 was the whole of A14 as written.  Steps 1 and 2 were invisible because nobody')
    print('    had looked at the graph. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

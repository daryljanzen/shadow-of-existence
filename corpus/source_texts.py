#!/usr/bin/env python3
"""source_texts.py -- THE THIRD SOURCE CLASS.  The papers CITE, the receipts DECIDE, and `resources/`
is where the proofs actually live.

** ⛔⛭⛭ WHY, AND IT IS THE SAME FAILURE A THIRD TIME. **

  * *`reach_baseline` reads the seventeen PAPER bodies.*
  * *`prior_art` (`L-281`) reads the 638 RECEIPT heads, built after two bakes walked into a question
    the receipts had settled.*
  * *Neither reads* `resources/` *-- and `resources/PhD_thesis/` is where `p0`'s* `prop:unique`
    *sends the reader: "\\cite{JanzenThesis} \\S sec\\_RPT".*
  ⇒ *** SO A CLAIM COULD BE STATED IN A PAPER, CITED TO A PROOF, AND CHECKED BY NEITHER INSTRUMENT --
      which is exactly how `L-280` produced a counterexample the thesis refutes on its own page. ***

** ⌗ WHAT THE THESIS SAYS, AND IT SETTLES IT (ch. 3, the classification at the `sec_RPT` reduction). **
*The real spheres $x\\cdot x=\\alpha^2$ of real $\\mathbb{M}^5$:*

    alpha^2 > 0   de Sitter -- the maximally symmetric TIMELIKE hypersurface     LORENTZIAN
    alpha^2 < 0   the maximally symmetric SPACELIKE hypersurface, and the thesis
                  says outright it "has four positive-definite eigenvalues"      RIEMANNIAN
    alpha^2 = 0   the null cone

  ⇒ ** In THIS family there is no Lorentzian alternative to de Sitter. **  *The anti-de Sitter that
    is Lorentzian embeds in a different ambient with a second timelike direction -- not a real sphere
    of real $\\mathbb{M}^5$ at all.*
  ⇒ *** So `p0`'s "real" is load-bearing, and a counterexample drawn from outside the family is not
      a counterexample to the proposition. ***

** ⌗ WHAT IT DOES. **  Searches `resources/` -- the thesis chapters, the earlier papers, the reading
notes -- and reports file, line and match.  *Use it for any claim a paper CITES rather than proves.*

  ⚠ ** WHAT IT CANNOT DO. **  *It matches words, like the other two, and `resources/` is not the
    corpus: a thesis chapter is a SOURCE, not a live document, and may be superseded by the papers.
    It says what was proved, not what is currently claimed.*
  ⌷ ** THE THREE TOGETHER, and none of them substitutes for another: ** *`reach_baseline` -- what the
    corpus PUBLISHES.  `prior_art` -- what it has already DECIDED.  `source_texts` -- what it PROVED,
    and where.*

    python3 corpus/source_texts.py 'maximally symmetric' 'positive-definite'
    python3 corpus/source_texts.py --files

Written r3184 (`L-283`).  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
RESOURCES = os.path.join(ROOT, 'resources')


def source_files():
    """every readable source text under resources/"""
    out = []
    for ext in ('*.tex', '*.md', '*.bib'):
        out += glob.glob(os.path.join(RESOURCES, '**', ext), recursive=True)
    return sorted(out)


def search(terms, files=None):
    """[(relpath, lineno, term, line)] over the source texts"""
    files = files if files is not None else source_files()
    hits = []
    for f in files:
        try:
            lines = open(f, encoding='utf-8', errors='replace').read().split('\n')
        except OSError:
            continue
        rel = os.path.relpath(f, ROOT)
        for n, line in enumerate(lines, 1):
            for t in terms:
                if re.search(re.escape(t), line, re.I):
                    hits.append((rel, n, t, line.strip()))
                    break
    return hits


def main():
    files = source_files()
    print()
    print('  source_texts -- what the corpus PROVED, and where')
    print()
    print(f'    source texts under resources/: {len(files)}')
    if not files:
        print('    ⛔ [FAIL] resources/ is unreachable — an empty search is not a clean sheet.')
        print()
        return 1
    if '--files' in sys.argv:
        for f in files:
            print(f'      {os.path.relpath(f, ROOT)}')
        print()
        return 0
    terms = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not terms:
        print('    give one or more terms.  The papers CITE; the receipts DECIDE;')
        print('    resources/ is where the proofs live.')
        print()
        return 0
    hits = search(terms, files)
    print(f'    lines matching {terms}: {len(hits)}')
    print()
    for rel, n, t, line in hits[:40]:
        print(f'    {rel}:{n}  «{t}»')
        print(f'       {line[:190]}')
    if not hits:
        print('    nothing found — a statement about these WORDS, not about the sources.')
    print()
    print('    ⌗ resources/ is a SOURCE, not the live corpus: it says what was PROVED, not what is')
    print('      currently claimed, and a paper may have moved past it.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""prior_art.py -- HAS THE CORPUS ALREADY ADJUDICATED THIS?  The receipts are searched, not the papers.

** ⛔⛭⛭ WHY THIS EXISTS, AND IT IS A FAILURE OF MINE MADE INTO AN INSTRUMENT. **

  *`reach_baseline` was built at `L-263` on `OWED` 609's own gate --* **"a bake against a corpus that
  cannot say what it already holds returns findings it owns"** *-- and it reads THE SEVENTEEN PAPER
  BODIES.*
  ⇒ ** But the corpus does not hold its adjudications only in the papers. **  *It holds them in six
    hundred receipts, and a receipt is where a question gets SETTLED before a paper ever carries it.*
  ⇒ *** SO THE BASELINE HAD A HOLE THE WHOLE TIME: a bake could survey every paper, find a clean
      sheet, and walk straight into a question the corpus decided two hundred revisions ago. ***

** ⌗ WHAT MADE IT VISIBLE (r3180, `L-281`). **  *The branch-point index was reduced four separate
ways across the fork, and `L-829` `S3` settled it at r2819 jointly with 56 -- naming all four wrong
reductions and giving a substitution test that kills them in one line.*  ⇒ ** Two later bakes touched
that exact operator without consulting it. **  *Station Ⓗ inherited the right pairing and `L-275`
inherited it from Ⓗ, so both came out right -- **by inheritance, not by method**.  Nothing in either
procedure would have caught a drift, and one did drift.*

** ⌗ WHAT IT DOES. **  Searches every registered receipt's DOCSTRING -- where a receipt states what it
settled and what it refuses to claim -- for a term, and reports the receipt, its id and the matching
line.  *Docstrings, not bodies: a receipt's head is its finding, and its code is how.*

  ⚠ ** WHAT IT CANNOT DO. **  *It matches words.  A prior adjudication phrased differently is invisible
    to it, which is `field_survey`'s blind spot in a second place -- and the answer is the same one:
    it bounds the reading and the reading decides.*
  ⌷ ** USE IT BEFORE A BAKE ASSERTS ANYTHING, alongside `reach_baseline`. **  *The papers say what the
    corpus PUBLISHES; the receipts say what it has already DECIDED, and those are different sets.*

    python3 corpus/prior_art.py 'branch point' 'limit-point'
    python3 corpus/prior_art.py --wide 'superpotential'

Written r3180 (`L-281`).  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def receipt_heads():
    """{path: docstring} for every receipt file that has one"""
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        try:
            src = open(f, encoding='utf-8', errors='replace').read(24000)
        except OSError:
            continue
        m = re.search(r'"""(.*?)"""', src, re.S)
        if m:
            out[os.path.relpath(f, ROOT)] = m.group(1)
    return out


def search(terms, wide=False, heads=None):
    """[(path, term, line)] -- every receipt head mentioning any term"""
    heads = heads if heads is not None else receipt_heads()
    hits = []
    for path, doc in heads.items():
        body = doc if not wide else doc
        for t in terms:
            for line in body.split('\n'):
                if re.search(re.escape(t), line, re.I):
                    hits.append((path, t, line.strip()))
                    break
    return hits


def main():
    wide = '--wide' in sys.argv
    terms = [a for a in sys.argv[1:] if not a.startswith('--')]
    heads = receipt_heads()
    print()
    print('  prior_art -- has the corpus already adjudicated this?')
    print()
    print(f'    receipt heads searched: {len(heads)}')
    if not heads:
        print('    ⛔ [FAIL] no receipt docstrings found — an empty search is not a clean sheet.')
        print()
        return 1
    if not terms:
        print('    give one or more terms.  The papers say what the corpus PUBLISHES;')
        print('    the receipts say what it has already DECIDED.')
        print()
        return 0
    hits = search(terms, wide, heads)
    print(f'    receipts mentioning {terms}: {len({h[0] for h in hits})}')
    print()
    for path, t, line in hits[:60]:
        rid = path.split('/')[1] if '/' in path else path
        print(f'    [{rid}]  «{t}»')
        print(f'       {line[:150]}')
    if not hits:
        print('    nothing found — which is a statement about these WORDS, not about the corpus.')
    print()
    print('    ⌗ A MATCH IS NOT A VERDICT and an absence is not a clean sheet: this bounds the')
    print('      reading.  Read the receipt before a bake asserts anything against it.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

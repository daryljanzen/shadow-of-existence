#!/usr/bin/env python3
"""unmet.py -- WHICH OPEN ROWS DO NOT KNOW THE CORPUS ALREADY HOLDS SOMETHING FOR THEM?

** WHY.  r2715, Daryl: ** "*** the six items are still full of stable things that we previously worked
out but the problems that need them don't know they exist. ***"  ** He is right, and it is the dominant
class: eight instances in about a hundred revisions, all one shape. **

      *** PO-11   needed "a different object"      -> B3 held the superpotential         r2714
          PO-10   needed a comparison rule         -> AIC/BIC, standard                  r2709
          L-543   asked about a RUNNING background -> r2691 had shown it de Sitter        r2713
          PO-12   last piece "unrun"               -> P15: no integrand at w=0            r2701
          PO-2    "three separated levels"         -> the taxonomy named them             r2683
          PO-3/9  rows read OPEN                   -> answered 50 revisions earlier       r2695
          triality P14 "does not yet do so"        -> r2679 supplied the ingredient       r2705
          PO-6    "three of its four halves"       -> the row declares TWO                r2695 ***

  ⇒ *** Every one: the row states a NEED, the corpus already HOLDS what meets it, and nothing connects
      the two.  Each was found by a human reading -- which does not scale and did not happen for
      fifty revisions at a time. ***

** WHAT THIS DOES. **  For each open `PO-` row it extracts the distinctive content words of its stated
NEED, and reports receipts whose INDEX summary shares those words but which the row DOES NOT CITE.

  ⚠ ** It surfaces candidates and does not verdict ** -- *** the same floor as `unbanked.py` (r2699):
      word overlap catches a shared vocabulary, not a shared object.  `PO-11`'s case would have been
      caught (both say "spinor", "radial"); `PO-10`'s would NOT, because AIC/BIC is absent from the
      corpus entirely.  ** A tool cannot find what the corpus has never named. ** ***
  ⌗ ** So this addresses the INTERNAL half of the class ** -- results the corpus holds -- and the
    external half (standard tools the corpus lacks a word for) stays a reading problem.

    python3 scripts/unmet.py            # default: 3 shared words
    python3 scripts/unmet.py 4

Written r2715.  Stated for reversal.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

STOP = set("""the and for with that this from what which where when whether about into over under
open still stated named computed receipt receipts corpus paper papers papers's line row rows
because there their they them then than only also does done make made take taken given gives
first second third half halves both each other another between within against before after""".split())


def words(s):
    s = re.sub(r'\\[a-zA-Z]+|[^a-z ]', ' ', s.lower())
    return {w for w in s.split() if len(w) > 5 and w not in STOP}


def main():
    need = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    print()
    print(f'  unmet -- receipts an open row does not cite, sharing >={need} content words')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    idx = open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8', errors='replace').read()

    # ** the INDEX rows: stem -> summary **
    rec = {}
    for l in idx.split('\n'):
        m = re.search(r'`([A-Za-z0-9_]+/)?([A-Za-z0-9_]+)\.py`', l)
        if m:
            rec.setdefault(m.group(2), set()).update(words(l))

    n = 0
    for l in raw.split('\n'):
        m = re.match(r'\|\s*\*\*(PO-\d+)\*\*', l)
        if not m or l.startswith('| ~~'):
            continue
        tag = m.group(1)
        cells = l.split(' | ')
        if 'ANSWERED' in cells[-1][:40]:
            continue
        # ** the NEED is the row's object plus the tail of its state field. **
        need_words = words(cells[2] if len(cells) > 2 else '') | words(cells[-1][-700:])
        hits = []
        for stem, w in rec.items():
            # ** r2715: the citation test must match the way rows actually cite -- by receipt
            # STEM or by any distinctive fragment of it.  *** A bare `stem in l` missed
            # `P14_colour_is_vector_like_on_singlets`, which PO-5 cites in a shortened form,
            # and reported a row's own citation as a gap. ***
            frag = stem.split('_')
            if stem in l or (len(frag) > 3 and '_'.join(frag[:4]) in l):
                continue                      # already cited
            shared = need_words & w
            if len(shared) >= need:
                hits.append((len(shared), stem, sorted(shared)[:4]))
        hits.sort(reverse=True)
        if hits:
            n += 1
            print(f'  {tag} -- {len(hits)} uncited receipt(s) sharing vocabulary:')
            for c, stem, sh in hits[:4]:
                print(f'      {c}  {stem[:52]:<54}{sh}')
            print()

    print(f'  {n} open row(s) have uncited receipts in their own vocabulary')
    print('  ⚠ CANDIDATES, not findings -- word overlap is not a shared object.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

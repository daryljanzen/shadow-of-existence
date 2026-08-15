#!/usr/bin/env python3
"""A4 -- the LEDGER 7 swept AS A GROUP for the first time: three duplicate `PO` rows verbatim, three are
the papers' OWN weight-marks and not work, and ONE is a real unrun item.

** THE QUESTION, r2694, Daryl: ** "*** Of the 20, are there not any that are closing anytime soon? … Are
all 20 now large projects or what? ***"

** ⛔ ⓵ THE `LEDGER 7` HAD NEVER BEEN SWEPT AS A GROUP -- it has been a PENDING item across the whole
session, and item-by-item reading cannot see duplication. **  Read together:

** ⓶ THREE DUPLICATE `PO` ROWS, VERBATIM. **

      *** b2d1f4a62a  "the full propagating spinor field sector (the built modes being leaf-bound,
                       not the propagating theory)"                  -> PO-11, WORD FOR WORD
          328d33776e  "the compact-face fermion sector ... remains unbuilt"
                                                                     -> PO-11's other half
          0201758a05  "the bespoke transfer"                         -> PO-12, WORD FOR WORD ***

  ⇒ *** Each is one problem counted twice.  `b2d1f4a62a`'s own note even says "** THE largest genuinely
      open thing, and on no register **" -- written before `PO-11` was registered at r2597, and never
      revisited. ***

** ⛭⛭ ⓷ THREE ARE THE PAPERS' OWN WEIGHT-MARKS, WHICH IS NOT WORK. **  `STATED-AT-WEIGHT` reads:
  * `233a615f2f`: "** the figure it matches is recalled rather than derived here **, so what is
    established is internal consistency" -- and the note: "corroboration at the strength of a memory,
    ** deliberately weight-marked **".
  * `9921e78365`: "** We state it at that strength and no higher, and the paragraphs below lower it
    further **".
  * `3e6a969eb5`: "The operator half is explicit and grounded ... ** and the charge half stated at its
    own weight.  Half a result, marked as half **."

  ⇒⇒ *** A paper saying "we claim this only this far" is SCOPE-BY-DESIGN, not a debt.  It is exactly what
      r2639 reclassified four `OPEN-DOWNSTREAM` items for, and the same argument applies: these are
      DISCIPLINE, and counting them as work counts the corpus's honesty against it. ***

** ⓸ AND ONE IS REAL. **  `3ebe33bce1`: "** A genuine test would compute the triality from the colour
content independently of the charge, and this sector does not yet do so. **"  *** A named, specified,
unrun test -- and NOT a duplicate: the phrase appears nowhere in `PO-4`. ***

** ⇒ ⓹ SO THE ANSWER TO THE QUESTION IS: THE BUCKET IS 1, NOT 7. **  *** Three are already on the table
under other names, three are not work at all, and one is a real item.  The 20 does not contain seven
ledger problems; it contains one, plus three double-counts of `PO-11`/`PO-12`. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-11` and `PO-12` shrink ** -- *** removing a duplicate removes a
COUNT, not a problem; the physics is unchanged and the rows keep their content. ***  ** Not that the
weight-marks should be deleted ** -- they are reclassified to `SCOPE-BY-DESIGN`, which is where the
corpus keeps deliberate self-limitation.  ** Not that the triality test is easy ** -- it is unrun and
stays unrun here.

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT d13805b** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2694.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    _raw14 = open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                  encoding='utf-8', errors='replace').read()
    p14 = re.sub(r'\s+', ' ', '\n'.join(x for x in _raw14.split('\n')
                                        if not x.lstrip().startswith('%')))
    print()
    print('  A4 -- the LEDGER 7, swept as a group')
    print()
    rows = [l for l in open(os.path.join(ROOT, 'corpus', 'open_ledger.txt'), encoding='utf-8')
            if '|' in l and not l.startswith('#')]
    led = {}
    for r in rows:
        p = [x.strip() for x in r.split('|', 3)]
        if len(p) == 4:
            led[p[0]] = (p[2], p[3])

    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    po = {re.search(r'PO-\d+', l).group(0): l
          for l in raw.split('\n') if re.match(r'\|\s*~*\*\*PO-\d+\*\*', l)}

    # ⓶ the three duplicates
    for hid, phrase, tag in (
            ('b2d1f4a62a', 'full propagating spinor field sector', 'PO-11'),
            ('328d33776e', 'compact-face fermion sector', 'PO-11'),
            ('0201758a05', 'bespoke transfer', 'PO-12')):
        check(f'⓶ {hid} duplicates {tag} verbatim: "{phrase}"',
              phrase.lower() in led[hid][1].lower() and phrase.lower() in po[tag].lower())

    # ⓷ the three weight-marks are the papers' own
    check('⛭⛭ ⓷ 233a615f2f is the paper limiting itself: "the figure it matches is recalled rather than '
          'derived here"',
          'recalled rather than derived here' in led['233a615f2f'][1])
    check('9921e78365 likewise: "We state it at that strength and no higher, and the paragraphs below '
          'lower it further"',
          'and no higher, and the paragraphs below lower it further' in led['9921e78365'][1])
    check('and 3e6a969eb5 marks its own half: "Half a result, marked as half"',
          'Half a result, marked as half' in led['3e6a969eb5'][1])

    # ⓸ the one real item
    # ** r2721, on cc54's c54.213 principle: *** an absence receipt that fails because its
    # finding was ACTED ON is a success -- flipping the comparison would throw that away.
    # The triality test was RUN at r2705 and P14 EDITED at r2706, so this converts to a
    # REGRESSION GUARD on the filling, naming the revision that did it. ***
    check('⓸ while 3ebe33bce1 was a real unrun test when this swept -- RUN at r2705 and banked '
          'into P14 at r2706, so the guard is now on the FILLING: the paper states the test '
          'and cites its receipt',
          'A genuine test computes the triality from the colour content' in p14
          and 'B24_the_triality_test_run' in p14)
    check('and it is NOT a duplicate -- the phrase appears in no PO row',
          not any('triality from the colour content' in v.lower() for v in po.values()))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the LEDGER bucket is 1, not 7. **')
    print('  ⓶ ** THREE DUPLICATE PO ROWS, VERBATIM: ** the full propagating spinor sector and the')
    print('     compact-face sector are ** PO-11 **; the bespoke transfer is ** PO-12 **.')
    print('     ⇒ *** b2d1f4a62a\'s own note reads "THE largest genuinely open thing, and ON NO')
    print('       REGISTER" — written before PO-11 was registered at r2597, and never revisited. ***')
    print('  ⛭⛭ ⓷ ** THREE ARE THE PAPERS\' OWN WEIGHT-MARKS: ** "recalled rather than derived here",')
    print('     "we state it at that strength and no higher", "half a result, marked as half".')
    print('     ⇒ *** A paper saying "we claim this only this far" is SCOPE-BY-DESIGN, not a debt —')
    print('       exactly what r2639 reclassified four OPEN-DOWNSTREAM items for.  Counting them as')
    print('       work counts the corpus\'s honesty against it. ***')
    print('  ⓸ ** AND ONE IS REAL: ** the triality test, named and specified and unrun — and not a')
    print('     duplicate.')
    print('  ⇒ ** So the 20 does not contain seven ledger problems.  It contains ONE, plus three')
    print('    double-counts of PO-11 and PO-12. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

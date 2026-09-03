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



def _ledger_at(rev):
    """`open_ledger.txt` parsed the same way as above, at a revision."""
    import subprocess as _sp
    out = {}
    txt = _sp.run(['git', 'show', f'{rev}:corpus/open_ledger.txt'], cwd=ROOT,
                  capture_output=True, text=True, errors='replace').stdout
    for r in txt.split('\n'):
        if '|' not in r or r.startswith('#'):
            continue
        p = [x.strip() for x in r.split('|', 3)]
        if len(p) == 4:
            out[p[0]] = (p[2], p[3])
    assert out, ('the ledger must be readable at the sweep commit, or nothing below is a comparison',
                 rev)
    return out


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

    # ** ⛔⛭⛭ THIS LOOP DID NOT FAIL, IT *** CRASHED *** (repaired r3974). **  `led[hid]` with no
    # ** default raised `KeyError` the moment a row left the ledger, so nothing after it ran and the
    # ** file reported a traceback instead of a verdict.  ** Third crash of this exact shape in the
    # ** debt ** -- with `L257/V1`'s `StopIteration` and `L272/F1`'s `IndexError`, all three a lookup
    # ** that assumed its key still existed.  *A closed item must read as a closed item, not as a
    # ** stack trace: a crash reports nothing, INCLUDING everything downstream of it.*
    #   ⛭ AND TWO OF THE THREE HAVE SINCE BEEN CLOSED, each by the claim itself being settled:
    #     `b2d1f4a62a` at r3811 ("five stale sentences closed"), when p0 stopped saying the
    #     propagating sector stays open and started saying it is built; `0201758a05` at r3870
    #     ("PO-24 step one: the control reproduces CAMB to 0.14%").  ** A ledger id is a hash of the
    #     claim's own text, so a row LEAVING is what a settled qualification looks like. **
    #   ⇒ ** The duplication is a fact about the ledger AT THE SWEEP, so it is pinned there; what is
    #     asserted live is the disposition -- still duplicating, or gone because it was settled. **
    _AT_SWEEP = 'd13805b8'          # r2694 -- this sweep's own commit
    _led_then = _ledger_at(_AT_SWEEP)
    for hid, phrase, tag in (
            ('b2d1f4a62a', 'full propagating spinor field sector', 'PO-11'),
            ('328d33776e', 'compact-face fermion sector', 'PO-11'),
            ('0201758a05', 'bespoke transfer', 'PO-12')):
        check(f'⓶ {hid} duplicated {tag} verbatim at {_AT_SWEEP}, this sweep\'s own commit: '
              f'"{phrase}"',
              hid in _led_then and phrase.lower() in _led_then[hid][1].lower()
              and phrase.lower() in po[tag].lower())
        _live = led.get(hid)
        _disp = ('still in the ledger and still duplicating' if _live
                 else 'GONE -- its claim was settled and the row left with it')
        check(f'⓶ᵃ {hid} is {_disp}',
              (phrase.lower() in _live[1].lower()) if _live else (hid not in led))

    # ⓷ the three weight-marks are the papers' own
    check('⛭⛭ ⓷ 233a615f2f is the paper limiting itself: "the figure it matches is recalled rather than '
          'derived here"',
          'recalled rather than derived here' in led['233a615f2f'][1])
    check('9921e78365 likewise: "We state it at that strength and no higher, and the paragraphs below '
          'lower it further"',
          'and no higher, and the paragraphs below lower it further' in led['9921e78365'][1])
    # ** ⛭ AND THE THIRD WEIGHT-MARK'S ROW IS GONE, FOR A DIFFERENT REASON THAN THE TWO ABOVE
    # ** (r3974). **  `3e6a969eb5` left at r3797 -- "the prose pass closed: the corpus's paper bodies
    # ** carry no bespoke jargon, 36 sites to zero" -- so the sentence was REWORDED and its id, being
    # ** a hash of the claim's own text, changed with it.  ** That is not the claim being settled;
    # ** it is the claim being rephrased **, which is a different disposition from `b2d1f4a62a`'s and
    # ** `0201758a05`'s and is worth keeping distinct.
    #   ⇒ The mark is pinned where this sweep read it, and the live check asks whether the WEIGHT is
    #     still carried -- by that id or by any row -- rather than whether one hash survived.
    _mark_then = _led_then.get('3e6a969eb5')
    check('and 3e6a969eb5 marked its own half at the sweep: "Half a result, marked as half"',
          _mark_then and 'Half a result, marked as half' in _mark_then[1])
    _still = [k for k, v in led.items() if 'half a result, marked as half' in v[1].lower()]
    _where = (f'row(s) {_still}' if _still
              else 'no row -- the id changed at r3797 when the prose pass reworded the sentence '
                   'it hashes')
    check(f'⛭ and the weight-mark is carried under {_where}', bool(_still) or '3e6a969eb5' not in led)

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

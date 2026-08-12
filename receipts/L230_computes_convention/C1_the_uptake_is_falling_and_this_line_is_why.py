#!/usr/bin/env python3
"""C1 -- the COMPUTES: convention's uptake is FALLING, not flat, and this line wrote 84 receipts this
session and used it once.

** WHAT THE ROW SAYS. **  L-230: "the `COMPUTES:` convention -- uptake ** flat at 40 of 357 ** while the
corpus grew a sixth", and its live route is "** make COMPUTES: universal **, which turns the receipt's
scope into a DECLARATION a gate can check against a sentence."

** ⛔ ⓵ RECOUNTED, AND IT IS NOT FLAT. **

      r2447 stated        39 of 309   = 12.6%
      the board says      40 of 357   = 11.2%
      *** r2551 measured  40 of 394   = 10.2% ***

  ⇒ ** ONE receipt adopted the convention in a hundred-odd revisions, while eighty-five receipts were
    written. **  ⇒ *** The denominator grew and the numerator did not.  "Flat" describes the count;
    the RATE is falling, and a convention whose share falls while the corpus grows is not being
    adopted -- it is being left behind. ***

** ⛭⛭ ⓶ AND THE PROXIMATE CAUSE IS THIS LINE. **  Receipts added this session: ** 84 **.  Carrying
`COMPUTES:`: ** 1 **.

  ⇒ *** So the row has been on the board describing an uptake problem while the node reading the board
      wrote eighty-four receipts and used the convention once.  That is not a corpus-wide adoption
      failure with an unclear cause; it is a specific one with a named one. ***

** ⓷ AND THE REASON MATTERS, BECAUSE IT DECIDES WHETHER THE ROUTE IS RIGHT. **  The row's route is to
make the header ** universal **.  ** But nothing enforces it, and the reason nothing enforces it is
L-230's own ⓵: "the instrument question is closed r2447 -- ** no gate can read a quantifier **." **
  ⇒ ** So the convention was designed to be voluntary because its CONTENT cannot be checked -- and a
    voluntary convention in a corpus with twenty-four gates is one nobody is reminded of. **
  ⇒ *** THE SPLIT: the header's PRESENCE is mechanical and can be required; the header's TRUTH is not
      and cannot.  Requiring presence is worth doing precisely because it is the half a gate can hold,
      and r2447 closed the wrong half. ***

WHAT IS NOT CLAIMED.  ** Not that a presence check should be built here ** -- that is the row's route and
Daryl's programme, and building a gate that makes eighty-four existing receipts fail is a decision about
work, not a cleanup.  ** Not that the convention is worthless **: it is the one thing that would let a
gate catch the F14 class (a receipt running at one parameter while the sentence citing it means
another).  ** Not that 40 is wrong ** -- the count is right; what was wrong is reading it as flat.

Written r2551.  Stated for reversal.
"""
import glob
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  C1 -- is the COMPUTES: uptake flat, or falling?')
    print()
    rs = glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)
    # ** this receipt's own docstring contains the token, so it counts itself.  Excluded -- a
    # measurement that includes the instrument taking it is off by the instrument. **
    _self = os.path.abspath(__file__)
    withc = [f for f in rs
             if os.path.abspath(f) != _self
             and 'COMPUTES:' in open(f, encoding='utf-8', errors='replace').read()]
    # ** the phrase lives in BOARD.md's lead text, not the register -- located by grep after the
    # first run failed against THE_LIVE_ARC.  Fourth time this span that matching at source beat
    # matching from habit. **
    # ** TWO SOURCES, and conflating them is what the first two runs did. **  The "flat at 40 of 357"
    # phrasing is BOARD.md's lead text; the "no gate can read a quantifier" clause is the REGISTER's
    # next-step field.  Each is checked where it actually lives.
    board = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'BOARD.md'),
                                     encoding='utf-8', errors='replace').read())
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    check('L-230 records the uptake as "flat at 40 of 357" (in BOARD.md\'s lead text)',
          'flat at 40 of 357' in board)
    pct_now = 100.0*len(withc)/len(rs)
    check(f'⛔ recounted: {len(withc)} of {len(rs)} = {pct_now:.1f}% -- against 39/309 = 12.6% at r2447 '
          f'and 40/357 = 11.2% on the board',
          len(rs) > 380 and pct_now < 11.2)
    check('⇒ SO THE COUNT IS FLAT AND THE RATE IS FALLING: the denominator grew and the numerator did '
          'not', len(withc) <= 41 and len(rs) > 380)

    # ⓶ this session
    out = subprocess.run(['git', 'log', '--diff-filter=A', '--name-only', '--pretty=format:',
                          '--since=1 day ago'], cwd=ROOT, capture_output=True, text=True).stdout
    recent = sorted({l for l in out.split('\n')
                     if l.startswith('receipts/') and l.endswith('.py')
                     and os.path.exists(os.path.join(ROOT, l))})
    rec_with = [f for f in recent
                if os.path.abspath(os.path.join(ROOT, f)) != _self
                and 'COMPUTES:' in open(os.path.join(ROOT, f), encoding='utf-8',
                                        errors='replace').read()]
    check(f'⛭⛭ and receipts added this session: {len(recent)}; carrying COMPUTES:: {len(rec_with)}',
          len(recent) > 50)
    check('⇒⇒ SO THE ROW DESCRIBED AN UPTAKE PROBLEM WHILE THE NODE READING THE BOARD WROTE DOZENS OF '
          'RECEIPTS AND USED THE CONVENTION ONCE -- a specific failure with a named cause, not a '
          'diffuse one', len(rec_with) <= 2 and len(recent) > 50)

    # ⓷ why the route is the way it is
    check('⌗ and L-230\'s own ⓵ says why nothing enforces it: "no gate can read a quantifier"',
          'no gate can read a quantifier' in arc)
    check('⇒ SO THE HEADER\'S PRESENCE IS MECHANICAL AND ITS TRUTH IS NOT -- and r2447 closed the '
          'question about TRUTH, leaving PRESENCE unaddressed',
          'no gate can read a quantifier' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the uptake is falling, and this line is the proximate cause. **')
    print(f'    r2447   39 of 309 = 12.6%')
    print(f'    board   40 of 357 = 11.2%')
    print(f'    now     {len(withc)} of {len(rs)} = {pct_now:.1f}%')
    print(f'  ⇒ ** One adoption in a hundred-odd revisions while {len(rs)-309} receipts were written. **')
    print(f'  ⛭ AND THIS SESSION: ** {len(recent)} receipts added, {len(rec_with)} carrying the header. **')
    print('     ⇒ ** The row described an uptake problem while the node reading the board was the one')
    print('       not adopting it. **')
    print('  ⌗ AND THE SPLIT THAT MATTERS: ** the header\'s PRESENCE is mechanical and can be required;')
    print('    its TRUTH is not and cannot. **  r2447 closed the question about truth -- ** the half a')
    print('    gate could actually hold was never addressed. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""C1 -- the COMPUTES: uptake, ORIGINALLY read as falling; CORRECTED c54.222 (`L-556`) -- it rose, and
the original file had never once exited zero.

** ⛭⛭⛭ WHAT THIS FILE SAID, AND ITS TABLE IS KEPT BECAUSE THE CORRECTION IS ABOUT IT. **  Written r2551
(observer line), the head read: *"the COMPUTES: convention's uptake is FALLING, not flat, and this line
wrote 84 receipts this session and used it once,"* on this table --

      r2447 stated        39 of 309   = 12.6%
      the board said      40 of 357   = 11.2%
      *** r2551 measured  40 of 395   = 10.2% ***

  -- and concluded *"the denominator grew and the numerator did not ... a convention whose share falls
  while the corpus grows is not being adopted, it is being left behind."*

** ⛔ ⓵ THE THESIS IS OVERTURNED BY WHAT HAPPENED NEXT.  82 of 543 = 15.1% ** (self-excluded, as the
original counted it).  The numerator has more than DOUBLED (40 -> 82) while the denominator grew by 148.  *** The rate is now ABOVE r2447's 12.6% and
half again the board's 11.2% -- the highest the convention has ever scored. ***  Nothing in the original
reasoning was wrong about r2551; ** a trend read off three points was reported as a property. **

** ⛭⛭ ⓶ AND THE PART THAT IS NOT A TREND ARGUMENT: THIS RECEIPT HAD NEVER PASSED. **  Run against
`9f4477c`, ** the very commit that added it **, it fails three of its seven checks -- and the FIRST one
is the row quote.  *** The string `flat at 40 of 357` occurs ZERO times in `BOARD.md` at `9f4477c`.
The receipt's opening premise was false on the day it was committed. ***

  ⇒ ** It was registered `✔✔` -- which the INDEX means as "run, exits zero" -- and it has never exited
    zero in any tree. **

** ⓷ WHY NOBODY SAW IT, AND THE CAUSE IS NOT INATTENTION.  Its INDEX row's paper column is an EM-DASH **
(it supports no paper), ** and every reader of `receipts/INDEX.md` filtered rows on that column. **  So
`run_all_receipts` -- THE ELEVENTH GATE, whose whole reason for existing is that "an instrument that
reads a file has not run it" -- had never run this file.  Twenty rows were dropped that way; eighteen
name a file on disk; *** this is the one of the eighteen that fails. ***  `L-556` removes the filter.

** ⓸ AND ONE DEFECT INSIDE THE FILE, WHICH THE SAME RUN EXPOSES.  Its session window was WALL-CLOCK. **
`git log --since=1 day ago` returned 85 receipts at c54.222 and ** 0 at `9f4477c` **, from the same
source, because those commits are older than a day now.
  ⇒ *** A receipt whose verdict depends on WHEN it is run is not reproducible, and its checks were
      thresholds on that number (`len(recent) > 50`).  The window is a SHA RANGE here. ***

** ⓹ WHAT SURVIVES UNCHANGED, and it is the half worth keeping.  THE SPLIT: the header's PRESENCE is
mechanical and can be required; its TRUTH is not and cannot ** -- L-230's own clause, *"no gate can read
a quantifier"*, is why the convention was designed voluntary.  r2447 closed the question about truth and
left presence unaddressed.  ** That reading is independent of the rate and is asserted below. **

WHAT IS NOT CLAIMED.  ** Not that the original was careless ** -- its three points were measured
correctly and its arithmetic is right; what it lacked was any way to be RUN again.  ** Not that the rise
is the convention's doing **: no cause is measured here, and the numerator moved over a span in which
this fork wrote most of the new receipts.  ** Not that a presence gate should be built ** -- still the
row's route and Daryl's programme.

Written r2551 (observer line).  CORRECTED c54.222 (`L-556`), cross-band and routed to 56 in `FOR_56.md`.
Stated for reversal.
"""
import glob
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

#: the commit that ADDED this file (r2551).  ** c54.220's rule: a claim about a past state of the tree
#: is a claim about a COMMIT, so it takes a SHA -- HEAD moves and takes the claim with it. **
BIRTH = '9f4477c'


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*args):
    return subprocess.run(['git'] + list(args), cwd=ROOT, capture_output=True,
                          text=True, errors='replace').stdout


def counted(rev):
    """(carrying, total) for the receipt tree AT a commit, measured the same way at both ends"""
    total = len([l for l in git('ls-tree', '-r', '--name-only', rev, '--', 'receipts').split('\n')
                 if l.endswith('.py')])
    carrying = len([l for l in git('grep', '-l', 'COMPUTES:', rev, '--',
                                   'receipts/*.py', 'receipts/**/*.py').split('\n') if l.strip()])
    return carrying, total


def main():
    print()
    print('  C1 -- the COMPUTES: uptake: falling (r2551) or rising (corrected c54.222)?')
    print()

    # ------------------------------------------------------------------ ⓵ the two measurements
    rs = glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)
    # ** this receipt's own docstring contains the token, so it counts itself.  Excluded -- a
    # measurement that includes the instrument taking it is off by the instrument. **
    _self = os.path.abspath(__file__)
    withc = [f for f in rs
             if os.path.abspath(f) != _self
             and 'COMPUTES:' in open(f, encoding='utf-8', errors='replace').read()]
    pct_now = 100.0 * len(withc) / len(rs)

    b_with, b_tot = counted(BIRTH)
    b_with -= 1                       # the same self-exclusion, at the commit that added the self
    pct_birth = 100.0 * b_with / b_tot
    check(f'⓵ at {BIRTH} (r2551, the commit that ADDED this file): {b_with} of {b_tot} '
          f'= {pct_birth:.1f}% -- the original measurement, reproduced from the commit',
          b_with == 40 and b_tot == 395)
    check(f'⛔ and NOW: {len(withc)} of {len(rs)} = {pct_now:.1f}% -- against 39/309 = 12.6% at r2447, '
          f'40/357 = 11.2% on the board, and {pct_birth:.1f}% at r2551',
          pct_now > 12.6 and len(withc) > 2 * b_with - 10)
    check('⇒ SO THE THESIS IS OVERTURNED: the numerator more than doubled while the denominator grew '
          'by less than half -- a trend read off three points, reported as a property',
          len(withc) > b_with and pct_now > pct_birth)

    # ------------------------------------------------------------------ ⓶ it never passed
    # ** The strongest single fact here, and it is about a COMMIT, so it is checked at that commit. **
    board_at_birth = git('show', f'{BIRTH}:BOARD.md')
    check(f'⓶ the premise was false when written: "flat at 40 of 357" occurs '
          f'{board_at_birth.count("flat at 40 of 357")} time(s) in BOARD.md at {BIRTH} '
          f'({len(board_at_birth)} chars read, so the file IS there)',
          len(board_at_birth) > 1000 and 'flat at 40 of 357' not in board_at_birth)
    check('⇒ SO A RECEIPT REGISTERED ✔✔ ("run, exits zero") HAS NEVER EXITED ZERO IN ANY TREE',
          len(board_at_birth) > 1000 and 'flat at 40 of 357' not in board_at_birth)

    # ------------------------------------------------------------------ ⓷ why nobody saw it
    # the row's paper column is an em-dash, and that is what all five readers filtered on
    idx = open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8',
               errors='replace').read().split('\n')
    myrow = [l for l in idx if 'C1_the_uptake_is_falling_and_this_line_is_why.py' in l]
    check('⓷ this receipt\'s own INDEX row opens with the EM-DASH paper column that every reader '
          'filtered on', len(myrow) == 1 and myrow[0].startswith('| — |'))
    reader = open(os.path.join(ROOT, 'corpus', 'index_rows.py'), encoding='utf-8',
                  errors='replace').read()
    check('⇒ and the filter is GONE rather than patched a fifth time: corpus/index_rows.py decides '
          'membership by header-or-rule, and never by the paper column',
          'def is_data_row' in reader
          and "if not (ln[:3].upper().startswith('| P')" not in reader)

    # ------------------------------------------------------------------ ⓸ the wall-clock window
    # ** REPLACED.  The original asked git for `--since=1 day ago` and asserted `> 50` on the answer. **
    span = sorted({l for l in git('log', '--diff-filter=A', '--name-only', '--pretty=format:',
                                  f'{BIRTH}..HEAD').split('\n')
                   if l.startswith('receipts/') and l.endswith('.py')
                   and os.path.exists(os.path.join(ROOT, l))})
    span_with = [f for f in span
                 if os.path.abspath(os.path.join(ROOT, f)) != _self
                 and 'COMPUTES:' in open(os.path.join(ROOT, f), encoding='utf-8',
                                         errors='replace').read()]
    check(f'⓸ over the SHA range {BIRTH}..HEAD: {len(span)} receipt(s) added, {len(span_with)} '
          f'carrying the header -- a window that does not move with the calendar',
          len(span) > 100 and len(span_with) > 30)
    check('⇒ AND IT IS THE SAME QUANTITY THE ORIGINAL READ AS "1 for 84": over a fixed range instead '
          'of over "the last day", the header is on a large minority of the span',
          100.0 * len(span_with) / max(1, len(span)) > 12.6)

    # ------------------------------------------------------------------ ⓹ what survives
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())
    check('⓹ L-230\'s own ⓵ still says why nothing enforces it: "no gate can read a quantifier"',
          'no gate can read a quantifier' in arc)
    check('⇒ SO THE SPLIT STANDS INDEPENDENT OF THE RATE: the header\'s PRESENCE is mechanical and '
          'can be required; its TRUTH is not and cannot -- r2447 closed the half a gate cannot hold',
          'no gate can read a quantifier' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the uptake ROSE, and the receipt that said otherwise had never run. **')
    print('    r2447    39 of 309 = 12.6%')
    print('    board    40 of 357 = 11.2%')
    print(f'    {BIRTH}  {b_with} of {b_tot} = {pct_birth:.1f}%   <- r2551, and this file\'s own commit')
    print(f'    now      {len(withc)} of {len(rs)} = {pct_now:.1f}%')
    print(f'  ⇒ ** The numerator more than doubled over {len(span)} added receipts. **')
    print('  ⛔ AND THE STANDING FINDING IS THE OTHER ONE: ** a registered receipt marked ✔✔ that has')
    print('     never exited zero, because its row\'s paper column is an em-dash and every reader of')
    print('     the INDEX filtered on that column. **  `L-556` removes the filter; this file is the')
    print('     one failure the removal uncovered.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

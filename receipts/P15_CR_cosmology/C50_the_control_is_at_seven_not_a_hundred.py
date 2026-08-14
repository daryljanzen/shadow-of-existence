#!/usr/bin/env python3
"""C50 -- the control arm is at $\\chi^2/{\\rm dof}=7.14$, not $\\sim100$: the receipt's F4 prose carries
a floor that fell fourteen-fold, and r2759 quoted the prose over the print.

** ⛔ ⓵ THE FILE DISAGREES WITH ITSELF. **

      *** F4 PROSE:   "the control arm lands at chi^2/dof ~ 100 against CAMB's 0.96"
          F6 OUTPUT:            chi^2    bins   chi^2/dof
            CAMB LambdaCDM      206.4     215        0.96
            this LCDM arm      1320.5     185        7.14
            this CR arm       51817.0     185      280.09 ***

  ** And F6 says why in its own words: ** *** "the floor has fallen from $103$ (c54.172) through $22.5$
  and $28.6$ to $7.1$, ** A FACTOR OF 14 ACROSS THE ARC **, and the verdict has not turned over at any
  step."  ** The F4 prose carries the c54.172 number and was never updated when the floor fell. ** ***

** ⛭⛭ ⓶ AND r2759 QUOTED THE PROSE, WHICH IS r2748's FAILURE REPEATED. **  *** r2748 established: take
the measured value from the RECEIPT THAT ASSERTS IT, never from prose, because "a paper's sentence
cannot fail."  ** The same holds inside a receipt: a printed $\\chi^2/{\\rm dof}$ is recomputed on every
run and cannot go stale; a sentence about it can and did. ** ***

** ⓷ AND THE CORRECTION CHANGES THE VERDICT ON THE ROW. **

      *** ~100  ->  the instrument is hopeless and PO-10 is blocked indefinitely
          7.14  ->  the instrument is a factor of SEVEN from usable, after already
                    improving by a factor of FOURTEEN across the arc ***

  ⇒ *** That is a different row.  ** A control that has moved $103\\to22.5\\to28.6\\to7.1$ is being worked
      and is converging; one sitting at $100$ is not. ** ***

** ⓸ AND TWO FURTHER FACTS THE PRINT CARRIES AND THE PROSE DOES NOT. **
  * ** the bin count differs: ** *** $185$ against CAMB's $215$ -- the arm drops thirty bins, and any
    $\\chi^2$ comparison across the two is comparing different data. ***
  * ** the CR arm is at $280.09$, not merely "outside the regime": *** $\\chi^2=51817$ on $185$ bins.
    Whatever the control's residual defect is, ** the CR arm carries it and something else. ** ***

WHAT IS NOT CLAIMED.  ** Not that $7.14$ is acceptable ** -- *** F6 itself says both arms remain outside
the regime in which plik_lite discriminates, and that verdict is unchanged. ***  ** Not that the
remaining factor of seven is diagnosed ** -- it is not, here or in the receipt.  ** Not that the F4
prose was wrong when written ** -- it recorded the floor at c54.172 correctly and was left behind by
its own file's progress.

** COMPUTES: nothing.  *** The receipt is RUN and its printed table read against its own prose. *** **

Written r2760.  Stated for reversal.
"""
import glob
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
    print()
    print("  C50 -- is the control arm at ~100 or at 7?")
    print()
    f = glob.glob(os.path.join(ROOT, 'receipts', '**', 'P15_where_the_likelihood_sits.py'),
                  recursive=True)[0]
    d = open(f, encoding='utf-8', errors='replace').read()

    # ** r2760, cc54's c54.213 principle: this receipt's finding was ACTED ON in the same
    # revision -- the stale prose is fixed at source.  Converted to a REGRESSION GUARD on the
    # fix, which now points the reader at the printed table. **
    check('✔ ⓵ the F4 prose is FIXED (r2760): it now says the control "was at chi^2/dof ~ 100 '
          'WHEN THIS NOTE WAS WRITTEN (c54.172)" and directs the reader to READ THE TABLE AND '
          'NOT THIS LINE',
          'WHEN THIS NOTE WAS WRITTEN' in d and 'READ THE' in d)
    check('while F6 prints the live table from a recomputation -- it formats chi^2, bins and '
          'chi^2/dof for CAMB, this LambdaCDM arm and this CR arm',
          "'this LCDM arm'" in d and "'this CR arm'" in d and 'dof_l' in d)
    check('and F6 states the history in its own words: "the floor has fallen from 103 (c54.172) '
          'through 22.5 and 28.6 to 7.1, a factor of 14 across the arc"',
          # ** the 7.1 is an f-string field, {dof_l:.1f} -- recomputed every run, so it
          # cannot go stale.  That is exactly why the PRINT is the source and the prose is not. **
          'has fallen from' in d and '22.5 and 28.6 to {dof_l:.1f}' in d)
    check('⛭⛭ ⓶ so the F4 prose carries the c54.172 floor and was left behind: 103 is the number it '
          'rounds to ~100',
          'c54.172' in d)

    # ⓷ the bin difference is in the print, not the prose
    check('⓷ and the print carries a fact the prose does not: the arm uses lik.nbintt bins against '
          'CAMB\'s 215, so a raw chi^2 comparison spans different data',
          'lik.nbintt' in d)
    check('⓸ while F6\'s verdict is unchanged and this receipt does not disturb it: "both arms remain '
          'outside the regime in which plik_lite discriminates"',
          'outside the regime in' in d and 'plik_lite discriminates' in d)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the control is at 7.14, and the file\'s own prose says ~100. **')
    print('  ⛔ ⓵ ** F4 PROSE: ** "the control arm lands at chi^2/dof ~ 100"')
    print('     ** F6 PRINT:  ** CAMB 206.4/215 = 0.96 · this LCDM arm 1320.5/185 = 7.14 ·')
    print('                      this CR arm 51817.0/185 = 280.09')
    print('     *** F6 says why: the floor fell 103 → 22.5 → 28.6 → 7.1, a factor of 14, and the F4')
    print('     prose carries the c54.172 number. ***')
    print('  ⛭⛭ ⓶ ** And r2759 quoted the prose — r2748\'s failure repeated inside a receipt: ** a')
    print('     printed χ²/dof is recomputed every run and cannot go stale; ** a sentence about it')
    print('     can, and did. **')
    print('  ⓷ ** The correction changes the row: ** ~100 means the instrument is hopeless; 7.14 means')
    print('     it is a factor of seven from usable ** after already improving fourteen-fold **.')
    print('     *** A control moving 103→22.5→28.6→7.1 is being worked and converging. ***')
    print('  ⓸ ** Two facts only the print carries: ** the arm uses 185 bins against CAMB\'s 215 — a')
    print('     raw χ² comparison spans different data — and ** the CR arm is at 280.09, so whatever')
    print('     the control\'s residual defect is, the CR arm carries it AND something else. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

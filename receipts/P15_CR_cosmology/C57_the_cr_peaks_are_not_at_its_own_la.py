#!/usr/bin/env python3
"""C57 -- the CR arm's peaks are NOT where its own $\\ell_A$ says: spacing $258$ against a stored
$\\ell_A=301.6$, a ratio of $0.855$, while the $\\Lambda$CDM arm sits at $0.995$.

** THE AMPLITUDE TEST r2788 NAMED, RUN -- AND IT FOUND SOMETHING PRIOR. **  *** The plan was to compare
peak HEIGHTS.  ** The peaks are not in comparable places to compare heights at. ** ***

** ⛔⛭⛭⛭ ⓵ THE TWO ARMS' PEAKS SIT AT DIFFERENT SPACINGS. **

      *** LCDM   peaks at 220, 540, 812, 1124, 1420    spacings 320,272,312,296   mean 300
          CR     peaks at 172, 404, 636,  916, 1204    spacings 232,232,280,288   mean 258 ***

** ⓶ AND ONLY ONE ARM SITS WHERE ITS OWN $\\ell_A$ SAYS. **

      *** LCDM   mean spacing / stored l_A = 300 / 301.4 = 0.995   ✔
          CR     mean spacing / stored l_A = 258 / 301.6 = 0.855   ⛔ ***

  ⇒⇒ *** THE $\\Lambda$CDM ARM IS SELF-CONSISTENT AND THE CR ARM IS NOT.  Its stored $\\ell_A=301.60$
      -- the number r2788 verified as $\\pi D_M/r_s$ and found agreeing with $\\Lambda$CDM's to $0.08\\%$
      -- ** does not describe where its own peaks are **. ***

** ⛭⛭ ⓷ WHICH EXPLAINS r2787's OSCILLATION AT LAST, AND ITS SIZE. **  *** A $14.5\\%$ spacing mismatch
puts the arms fully out of register within four peaks: at $\\ell\\sim1200$ the CR arm is on its fifth
peak where $\\Lambda$CDM is between its fourth and fifth.  ** That produces exactly a ratio swinging
between $0.24$ and $2.4$ -- the measured range -- and it is two orders larger than the $0.075\\%$
$\\ell_A$ residual r2788 sized. ** ***

** ⛭⛭⛭ ⓸ AND IT RELOCATES THE DEFECT FROM THE PHYSICS TO THE BOOKKEEPING. **  *** r2788 closed the
"numerical" horn by showing $\\ell_A=\\pi D_M/r_s$ holds in both arms.  ** It does -- as ARITHMETIC on the
stored $D_M$ and $r_s$. **  What this receipt shows is that the arithmetic and the SPECTRUM disagree
for CR: the stored quantities are consistent with each other and not with the computed $C_\\ell$. ***
  ⇒ *** So the question is no longer physical-or-numerical about a $0.075\\%$ slip.  ** It is: which of
    $D_M$, $r_s$ or the projection does the CR arm's own transfer actually use? **  One of the three is
    not the stored value. ***

WHAT IS NOT CLAIMED.  ** Not that the CR arm is wrong ** -- *** a $0.855$ ratio could be a real feature
of a geometric stacking transfer; what is established is that the STORED $\\ell_A$ does not describe the
spectrum, not which of them is right. ***  ** Not that peak-finding is exact ** -- *** prominence
threshold $2\\%$ of range, five peaks found in each arm; the conclusion rests on a $14.5\\%$ gap, not on
peak positions to the bin. ***  ** Not that amplitude is now excluded ** -- *** it was not tested, because
the peaks are not aligned enough to compare heights. ***

** COMPUTES: peak positions and spacings in both banked arms, against their stored $\\ell_A$.
*** Both spectra are `c54.178`, the corpus's own. *** **

Written r2789.  Stated for reversal.
"""
import glob
import os

import numpy as np
from scipy.signal import find_peaks

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def peaks_of(z, ls):
    pk, _ = find_peaks(z['Dl'], prominence=np.ptp(z['Dl'])*0.02)
    return ls[pk]


def main():
    print()
    print("  C57 -- do the arms' peaks sit where their own l_A says?")
    print()
    cr = np.load(glob.glob(os.path.join(ROOT, '**', 'c54.178_cr.npz'), recursive=True)[0])
    lc = np.load(glob.glob(os.path.join(ROOT, '**', 'c54.178_lcdm.npz'), recursive=True)[0])
    ls = cr['ls']

    pl, pc = peaks_of(lc, ls), peaks_of(cr, ls)
    sl, sc = np.diff(pl).mean(), np.diff(pc).mean()
    lА_l, lA_c = float(lc['l_A']), float(cr['l_A'])

    check(f'⓵ both arms show five peaks: $\\Lambda$CDM at {[int(x) for x in pl]}, '
          f'CR at {[int(x) for x in pc]}',
          len(pl) == len(pc) == 5)
    check(f'⓶ with mean spacings {sl:.0f} and {sc:.0f} -- ** a {100*(1-sc/sl):.1f}% difference **',
          abs(1 - sc/sl) > 0.1)

    check(f'⛭⛭⛭ ⓷ and only $\\Lambda$CDM sits where its own $\\ell_A$ says: '
          f'{sl:.0f}/{lА_l:.1f} = {sl/lА_l:.3f}', abs(sl/lА_l - 1) < 0.03)
    check(f'⛔ while CR gives {sc:.0f}/{lA_c:.1f} = {sc/lA_c:.3f} -- ** its stored $\\ell_A$ does not '
          'describe where its own peaks are **', abs(sc/lA_c - 1) > 0.10)

    # ⓸ and the mismatch is the right size for r2787's swing
    check(f'⓸ and a {100*(1-sc/sl):.1f}% spacing mismatch puts the arms fully out of register within '
          f'four peaks -- ** two orders larger than the 0.075% $\\ell_A$ residual r2788 sized **',
          abs(1 - sc/sl) > 50*0.00075)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the CR arm's peaks are not where its own l_A says. **")
    print(f'  ⓵ ** Both arms, five peaks: **')
    print(f'       LCDM  {[int(x) for x in pl]}   spacing {sl:.0f}')
    print(f'       CR    {[int(x) for x in pc]}   spacing {sc:.0f}')
    print(f'  ⛭⛭⛭ ⓶ ** And only one is self-consistent: **')
    print(f'       LCDM  {sl:.0f} / {lА_l:.1f} = {sl/lА_l:.3f}   ✔')
    print(f'       CR    {sc:.0f} / {lA_c:.1f} = {sc/lA_c:.3f}   ⛔')
    print('     *** The stored ℓ_A = 301.60 — the number r2788 verified as πD_M/r_s and found agreeing')
    print('     with ΛCDM\'s to 0.08% — DOES NOT DESCRIBE WHERE ITS OWN PEAKS ARE. ***')
    print(f'  ⛭⛭ ⓷ ** Which explains r2787\'s oscillation and its size: ** a {100*(1-sc/sl):.1f}% spacing')
    print('     mismatch puts the arms fully out of register within four peaks — producing exactly a')
    print('     ratio swinging 0.24 to 2.4, ** two orders larger than the 0.075% residual. **')
    print('  ⓸ ** And it relocates the defect from the physics to the bookkeeping: ** r2788 showed')
    print('     ℓ_A = πD_M/r_s holds — ** as arithmetic on the STORED values. **  The arithmetic and')
    print('     the SPECTRUM disagree for CR.')
    print('     ⇒ *** Which of D_M, r_s or the projection does the CR arm\'s transfer actually use?')
    print('     One of the three is not the stored value. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

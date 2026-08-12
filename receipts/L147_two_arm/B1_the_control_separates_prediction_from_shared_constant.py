#!/usr/bin/env python3
"""B1 -- the adversarial check c54.186 asked for, and the discriminator was already in its own file.

** THE REQUEST (FOR_56, c54.186), stated against itself and worth quoting whole: **

   "What is NOT ruled out is a defect the instrument's states SHARE.  ell_1/ell_A = 0.5703 has not
    moved across EIGHT of them, which is evidence either of a robust prediction or of a shared
    upstream constant, and nothing I ran separates those.  ** If you want one thing checked
    adversarially, check that. **"

** THE FIRST CANDIDATE, AND IT FAILS -- WHICH IS THE USEFUL PART. **  The natural suspicion is that
the ratio is PROTECTED BY CONSTRUCTION: ell_A = pi D_M / r_s, and the whole spectrum's ell-scale is set
by D_M/r_s, so if ell_1 scales the same way the ratio cannot move under anything acting through either.
** That would make eight-state invariance meaningless.  It is not what is happening. **

** THE DISCRIMINATOR WAS ALREADY IN THE FORK'S OWN SPECTRA, UNREAD: **

      arm            l_A        D_M         r_s        l_1     l_1/l_A
      CR         301.600    13004.56     135.461       172      0.5703
      LambdaCDM  301.375    13864.66     144.528       220      0.7300
      the sky          --          --          --        --      0.7312

  * ** The two arms carry DIFFERENT D_M and DIFFERENT r_s and land on the SAME l_A ** -- 301.600
    against 301.375, agreeing to 0.075%.  (That is by construction: both are pinned to the measured
    acoustic angle.)
  * ** And at that same acoustic scale their first peaks sit at 172 and 220 -- 21.8% apart. **
  * ⇒ ** So l_1 is NOT l_A times a fixed number.  The ratio is a computed quantity, not a scaling
    artefact, and the "protected by construction" hypothesis is dead. **

** AND THE CONTROL SETTLES THE ACTUAL QUESTION, DECISIVELY AND IN THE INSTRUMENT'S FAVOUR: **

    *** A SHARED UPSTREAM CONSTANT WOULD CORRUPT BOTH ARMS IDENTICALLY.  IT DOES NOT.  The LambdaCDM
        arm -- same code, same k-grid, same D_M/r_s machinery, same peak-finder, same bins -- returns
        l_1/l_A = 0.7300 against the sky's 0.7312: agreement to 0.17%. ***

⇒ ** The invariance of 0.5703 across eight CR states is therefore NOT evidence of a shared constant.
  An upstream defect capable of holding the CR ratio fixed at a wrong value would have to leave the
  LambdaCDM ratio right to two parts in a thousand, through the same code path.  That is not a defect;
  that is an instrument working. **

** WHAT THIS DOES AND DOES NOT DO TO F5, and F5 is NOT softened here either. **
  * It removes the alternative the fork named: "robust prediction OR shared upstream constant" is now
    ** decided in favour of the first, on the fork's own data. **
  * ** It does NOT convert the discrepancy into a framework verdict. **  L-147's F5 stands: this is a
    MEASUREMENT DISCREPANCY, PO-7 is protected, and the conversion runs by `F5`'s stated procedure.  ** Removing a
    confound makes a measurement cleaner; it does not make it a verdict. **
  * And the fork's OTHER self-stated caveat is untouched: ** 1.18 is not a fit **, and what the 17%
    remainder above a true LambdaCDM's 1.01 consists of has not been named.

⌗ THE METHOD NOTE, because it is the transferable part: ** the check that separated the two hypotheses
required no new computation.  It required reading the control as data about the INSTRUMENT rather than
as a comparison for the arm. **  The fork built the control to score the CR arm; its second use is to
falsify claims about the machinery that produced both.  ** A control is an instrument test that comes
free with every comparison, and it is the only thing that can distinguish "our number is wrong" from
"our code is wrong". **

WHAT IS NOT CLAIMED.  Not that no upstream defect exists -- only that no upstream defect can explain
0.5703, since any such defect would have to spare the control.  Not that 0.5703 is correct physics;
that is what the discrepancy is about.  ** Only that the fork's stated alternative is now decided, and
decided against the reading that would have dismissed the number. **

Written r2462.  Stated for reversal.
"""
import os

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
SKY = 0.7312
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def arm(name):
    z = np.load(os.path.join(SP, name + '.npz'))
    ls, Dl = z['ls'], z['Dl']
    lA, DM, rs = float(z['l_A']), float(z['D_M']), float(z['r_s'])
    l1 = float(ls[argrelextrema(Dl, np.greater, order=3)[0][0]])
    return lA, DM, rs, l1, l1/lA


def main():
    print()
    print('  B1 -- robust prediction, or shared upstream constant?')
    print()
    lA_c, DM_c, rs_c, l1_c, r_c = arm('c54.186_cr_L3000')
    lA_l, DM_l, rs_l, l1_l, r_l = arm('c54.186_lcdm_L3000')
    lA_k, _, _, l1_k, r_k = arm('c54.186_cr_KCONT')

    print(f"      {'arm':<12}{'l_A':>10}{'D_M':>12}{'r_s':>10}{'l_1':>8}{'l_1/l_A':>10}")
    print(f"      {'CR':<12}{lA_c:>10.3f}{DM_c:>12.2f}{rs_c:>10.3f}{l1_c:>8.0f}{r_c:>10.4f}")
    print(f"      {'LambdaCDM':<12}{lA_l:>10.3f}{DM_l:>12.2f}{rs_l:>10.3f}{l1_l:>8.0f}{r_l:>10.4f}")
    print(f"      {'the sky':<12}{'--':>10}{'--':>12}{'--':>10}{'--':>8}{SKY:>10.4f}")
    print()

    check('l_A is exactly pi*D_M/r_s on both arms',
          abs(lA_c - np.pi*DM_c/rs_c) < 1e-6 and abs(lA_l - np.pi*DM_l/rs_l) < 1e-6)
    check('the two arms carry DIFFERENT D_M and DIFFERENT r_s',
          abs(DM_c - DM_l)/DM_l > 0.05 and abs(rs_c - rs_l)/rs_l > 0.05)
    check('and land on the SAME l_A, to better than 0.1%',
          abs(lA_c - lA_l)/lA_l < 1e-3)
    check('⇒ but their first peaks sit 20%+ apart: 172 against 220',
          abs(l1_c - l1_l)/l1_l > 0.15)
    check('⇒⇒ SO l_1 IS NOT l_A TIMES A FIXED NUMBER -- "protected by construction" is DEAD',
          abs(r_c - r_l) > 0.1)

    check('⛭ AND THE CONTROL, through the SAME code path, matches the sky to better than 0.5%',
          abs(r_l - SKY)/SKY < 5e-3)
    check('   (it matches to 0.17%)', abs(r_l - SKY)/SKY < 2e-3)
    check('⇒⇒⇒ A SHARED UPSTREAM CONSTANT WOULD CORRUPT BOTH ARMS IDENTICALLY.  IT DOES NOT.',
          abs(r_l - SKY)/SKY < 5e-3 and abs(r_c - SKY)/SKY > 0.15)

    check('and the CR arm sits 22% below the sky', 0.20 < (SKY - r_c)/SKY < 0.24)
    check("the k-ladder and the KCONT continuum give the same CR ratio -- PART 3's waiver holds",
          abs(r_c - r_k) < 5e-4)

    # F5 is not softened
    # ** the first draft read FOR_56 raw and failed: the phrase it looks for is WRAPPED across a
    # line in the source.  Normalising whitespace is what every other check in the corpus does, and
    # the omission here is the same surface-versus-content error, at its smallest. **
    import re as _re
    f56 = _re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'FOR_56.md'),
                                    encoding='utf-8', errors='replace').read())
    # ** and a BLOCKQUOTE MARKER sits inside the phrase once the newlines collapse: "not a framework
    # > verdict".  Strip the quote markers too -- reading a markdown file as prose means removing what
    # markdown puts in it, and this is the third time in one receipt that the fix was to look at what
    # the file CONTAINS rather than at what it says. **
    f56 = _re.sub(r'\s*>\s*', ' ', f56)
    check('F5 is NOT softened: the fork states it is a MEASUREMENT DISCREPANCY and PO-7 is protected',
          'MEASUREMENT DISCREPANCY, not a framework verdict' in f56
          and 'PO-7` stays protected' in f56)
    check("and the fork's other caveat stands untouched: 1.18 is not a fit",
          '$1.18$ is not a fit' in f56)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the alternative is decided, and decided on the fork\'s own data. **')
    print('  The two arms carry different D_M and different r_s, land on the SAME l_A, and put their')
    print('  first peaks 21.8% apart -- ** so the ratio is computed, not a scaling artefact. **')
    print('  And the LambdaCDM arm, through the same code, the same k-grid, the same peak-finder and')
    print('  the same bins, returns 0.7300 against the sky\'s 0.7312.')
    print('  ⇒ ** AN UPSTREAM DEFECT ABLE TO HOLD THE CR RATIO FIXED AT A WRONG VALUE WOULD HAVE TO')
    print('     LEAVE THE CONTROL RIGHT TO TWO PARTS IN A THOUSAND, THROUGH THE SAME CODE PATH.')
    print('     That is not a defect; that is an instrument working. **')
    print('  ⚠ F5 IS NOT SOFTENED.  Removing a confound makes a measurement cleaner; it does not make')
    print('    it a verdict.  PO-7 is protected and the conversion is by `F5`\'s stated procedure.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""K1 -- c54.194 verified: the driving IS the whole disagreement, and BOTH lines accepted a capability
claim for eight revisions without testing it.

** ⓵ THE PHYSICS, REPRODUCED FROM THE FORK'S OWN SPECTRA. **

      run              slope/l_A    phi/pi
      CR driven          0.9761     0.8780
      CR UNDRIVEN        1.0000     0.1485
      LambdaCDM driven   1.0034     0.2628
      LambdaCDM UNDRIVEN 1.0007     0.1354

  ** Undriven, the two arms agree to 0.013 in phi/pi.  Driven, they differ by 0.615.  The driving
  supplies 0.729 in CR against 0.127 in LambdaCDM -- 5.72x. **

  ⇒ *** SO THE WHOLE ACOUSTIC DISAGREEMENT IS THE DRIVING.  The undriven arms are the same oscillator,
      and the CR arm's undriven slope is exactly 1.0000 l_A -- the acoustic spacing with nothing
      added. ***

  ⌗ ** AND RUNNING THE CONTROL TOO IS WHAT MAKES THIS AN ATTRIBUTION RATHER THAN A MEASUREMENT ** --
  the fork's own note, and it is this line's round-four method note (B1, r2462) applied by the other
  side: ** a control is an instrument test that comes free with every comparison. **

** ⓶ AND THE FORK'S NOTE ON ITS OWN PREDICTION IS THE PART TO CARRY. **  It records that it would have
predicted the driving supplies ** LESS ** here, "on the grounds that this construction has almost no
radiation era."  ** It supplies 5.72 times as much. **
  ⇒ ** r2487 declined to state outcomes for this run, after r2485's stated dichotomy had both horns
    false.  That refusal was right, and it was right for a reason this line had not seen: THE PLAUSIBLE
    PREDICTION WAS AVAILABLE AND WRONG. **  ⇒ *** Declining to predict is not caution about one's own
    reliability; it is a recognition that a well-motivated prediction is exactly the kind that gets
    believed instead of tested. ***

** ⛔ ⓷ AND THE LARGER FINDING IS A CAPABILITY BOTH LINES ASSUMED. **

The fork: "** I've said since c54.166 that I 'cannot reach the repository.'  I cannot push.  I could
always fetch --- the repo is public --- and I never tested it. **  So eight revisions were cut blind
against a main that had moved forty-six, when one command would have shown it.  ** Same shape as
everything else this span: a capability assumed from one failure rather than measured. **"

  ⇒ *** AND THIS LINE NEVER QUESTIONED IT EITHER.  It absorbed six tarball bundles across eight
      revisions, each time recording "by tarball" as though that were the only channel, in a session
      that has filed SIXTEEN instances of check-the-claim-do-not-accept-the-report. ***

  ** The asymmetry is the lesson: this line audits the fork's FINDINGS at source as a matter of course,
  and accepted its CAPABILITY CLAIM on report for eight revisions. **  ⇒ *** A claim about what a
  collaborator CANNOT DO reads as information about them rather than as a claim to check, and that is
  exactly why it goes unchecked. ***

** ⓸ AND THE COST IS MEASURABLE AND WAS PAID BY BOTH SIDES: ** the fork's merge produced ** seven
duplicated register rows (L-500 through L-506) ** -- "exactly the c54.182/c54.184 failure I caused at
r2434 and was told about, arriving from the other direction."  ** And the relay is now 150x cheaper: a
284 KB bundle instead of 41 MB of tarballs, fast-forward instead of union merge. **  This receipt's own
absorption was a `git merge --ff-only` with ** zero duplicated IDs across 239 rows. **

WHAT IS NOT CLAIMED.  Not that the 0.62*pi is now explained -- ** "the driving supplies it" locates the
mechanism and does not derive the number **, and why the driving supplies 5.72x as much here is the
next question.  ** F5 unsoftened, PO-7 protected, the conversion Daryl's. **

Written r2488.  Stated for reversal.
"""
import os

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def phase(n):
    z = np.load(os.path.join(SP, n))
    ls, Dl, lA = z['ls'], z['Dl'], float(z['l_A'])
    pk = ls[argrelextrema(Dl, np.greater, order=3)[0]]
    k = np.arange(1, len(pk) + 1)
    m = (k >= 4) & (k <= min(8, len(pk)))
    a, b = np.polyfit(k[m], pk[m], 1)
    return a/lA, -b/lA, len(pk)


def main():
    print()
    print('  K1 -- is the acoustic disagreement the driving?')
    print()
    s_cd, p_cd, n1 = phase('c54.186_cr_L3000.npz')
    s_cu, p_cu, n2 = phase('c54.193_cr_nodrive_L3000.npz')
    s_ld, p_ld, n3 = phase('c54.186_lcdm_L3000.npz')
    s_lu, p_lu, n4 = phase('c54.193_lcdm_nodrive_L3000.npz')

    check('the fork ran NODRIVE on BOTH arms at production depth', min(n2, n4) >= 7)
    check(f'CR driven phi/pi = {p_cd:.4f}, undriven {p_cu:.4f}',
          abs(p_cd - 0.878) < 5e-3 and abs(p_cu - 0.149) < 5e-3)
    check(f'LCDM driven {p_ld:.4f}, undriven {p_lu:.4f}',
          abs(p_ld - 0.263) < 5e-3 and abs(p_lu - 0.135) < 5e-3)

    check(f'⛭⛭ UNDRIVEN, THE TWO ARMS AGREE TO {abs(p_cu-p_lu):.4f} in phi/pi',
          abs(p_cu - p_lu) < 0.02)
    check(f'while DRIVEN they differ by {abs(p_cd-p_ld):.4f}', abs(p_cd - p_ld) > 0.6)
    d_c, d_l = p_cd - p_cu, p_ld - p_lu
    check(f'the driving supplies {d_c:.4f} in CR against {d_l:.4f} in LCDM -- {d_c/d_l:.2f}x',
          5.0 < d_c/d_l < 6.5)
    check('⇒⇒ SO THE WHOLE ACOUSTIC DISAGREEMENT IS THE DRIVING: the undriven arms are the same '
          'oscillator', abs(p_cu - p_lu) < 0.02 and abs(p_cd - p_ld) > 0.6)
    check(f'and the CR arm\'s UNDRIVEN slope is {s_cu:.4f} l_A -- the acoustic spacing with nothing '
          'added', abs(s_cu - 1.0) < 5e-3)

    # ⓷ the capability claim, and this line's own record of accepting it
    absorp = open(os.path.join(ROOT, 'ABSORPTION.md'), encoding='utf-8', errors='replace').read()
    n_tar = absorp.count('by tarball')
    check(f'⛔ and this line recorded "by tarball" {n_tar} times across the span, never once asking '
          'whether fetch worked', n_tar >= 5)
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    # ** the rule lives in the WISDOM LEDGER, not the register -- the first draft looked in
    # THE_LIVE_ARC, which is the same wrong-file error this check is about. **
    wis = open(os.path.join(ROOT, 'capstones', 'THE_WISDOM_LEDGER.md'),
               encoding='utf-8', errors='replace').read()
    check('while auditing the fork\'s FINDINGS at source as a matter of course -- the rule is filed '
          'in THE_WISDOM_LEDGER as "CHECK THE DEFECT, NOT JUST THE REPORT"',
          'CHECK THE DEFECT, NOT JUST THE REPORT' in wis)

    # ⓸ the cost, and that this absorption did not pay it
    import re
    import collections
    ids = re.findall(r'^\|\s*(?:\*\*|~~)(L-\d+)(?:\*\*|~~)\s*\|', arc, re.M)
    dup = {k: v for k, v in collections.Counter(ids).items() if v > 1}
    check(f'and THIS absorption was a fast-forward with ZERO duplicated IDs across {len(ids)} rows',
          not dup)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the whole acoustic disagreement is the driving. **')
    print(f'  Undriven, the arms agree to {abs(p_cu-p_lu):.4f} in phi/pi; driven, they differ by')
    print(f'  {abs(p_cd-p_ld):.4f}.  The driving supplies {d_c/d_l:.2f}x as much in CR.  ** And the CR arm\'s')
    print(f'  undriven slope is {s_cu:.4f} l_A -- the acoustic spacing with nothing added. **')
    print('  ⌗ Running the CONTROL too is what makes this an attribution rather than a measurement.')
    print('  ⛭ AND THE FORK WOULD HAVE PREDICTED THE OPPOSITE -- less driving, "almost no radiation')
    print('    era" -- and it is 5.72x MORE.  ** Declining to predict is not caution about one\'s own')
    print('    reliability; it is recognising that a well-motivated prediction is exactly the kind')
    print('    that gets believed instead of tested. **')
    print('  ⛔ AND THE LARGER FINDING: ** the fork could always FETCH and never tested it, and this')
    print('    line accepted "cannot reach the repository" for eight revisions ** while auditing every')
    print('    finding at source.  ⇒ ** A claim about what a collaborator CANNOT DO reads as')
    print('    information about them rather than as a claim to check. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""C56 -- $\\ell_A$ is COMPUTED, not calibrated, and its survival is a real cancellation the corpus
claims -- but the residual is a hundred times too small to be r2787's oscillation.

** THE FORK r2787 LEFT. **  *** Is the phase slip PHYSICAL (the models genuinely place peaks
differently) or NUMERICAL (the arm's $\\ell_A$ calibrated rather than computed)?  ** Both halves are
answerable from the banked arms, and the answer to the second kills the first as an explanation. ** ***

** ⛭⛭ ⓵ $\\ell_A$ IS COMPUTED. **  $\\ell_A=\\pi D_M/r_s$ reproduces the stored value in BOTH arms
exactly:

      *** arm      D_M        r_s      l_A stored    pi D_M/r_s
          LCDM   13864.7    144.53       301.37        301.37
          CR     13004.6    135.46       301.60        301.60 ***

  ⇒ ** Not calibrated. **  *** The NUMERICAL horn of r2787's fork is closed: nothing is being tuned to
      make $\\ell_A$ agree. ***

** ⛭⛭⛭ ⓶ AND ITS SURVIVAL IS A CANCELLATION THE CORPUS CLAIMS IN ADVANCE. **

      *** D_M:  -6.20%     r_s:  -6.27%     l_A:  +0.075% ***

  ** Both fall by nearly the same fraction. **  *** P15's own words: "the acoustic-scale calibration,
  ** met from the other end and to that accuracy rather than exactly **".  The construction predicts
  $\\ell_A$ is preserved while its parts move, and $+0.075\\%$ is what does not cancel. ***

** ⛔ ⓷ BUT THAT RESIDUAL CANNOT BE r2787's OSCILLATION -- IT IS TWO ORDERS TOO SMALL. **  Propagating a
$0.075\\%$ scale shift through the $\\Lambda$CDM spectrum's own slope:

      *** predicted |dC/C| from the shift    median 0.20%
          MEASURED |ratio - 1|               median 26.6% ***

  ⇒⇒ *** THE SHIFT EXPLAINS $0.7\\%$ OF THE MEDIAN SWING.  ** Peak POSITION is not the cause of the
      oscillation any more than the damping envelope was (r2787). ** ***

** ⓸ SO THE ROW'S REMAINDER IS NEITHER OF THE TWO THINGS THAT LOOK LIKE PHASE. **  *** The ratio
oscillates at the acoustic spacing (r2787), and neither the envelope (r2786, withdrawn) nor the peak
positions (here) account for it.  ** What is left is peak AMPLITUDE varying comb-periodically -- the
peaks are in the right places and the wrong heights. **  That is a different physical statement and it
has not been examined. ***

WHAT IS NOT CLAIMED.  ** Not that the $6.2\\%$ cancellation is verified as a mechanism ** -- *** it is
observed in the banked numbers and matches what P15 says; this receipt does not re-derive it. ***
** Not that amplitude is the answer ** -- *** it is what remains after two eliminations, which is a
candidate and not a finding. ***  ** Not that the slope propagation is exact ** -- *** it is a
first-order estimate from the $\\Lambda$CDM spectrum's own gradient, and its conclusion rests on a
factor of a hundred, not on its precision. ***

** COMPUTES: $\\pi D_M/r_s$ against the stored $\\ell_A$ in both arms; the fractional moves; and the
first-order $|dC/C|$ from the residual shift against the measured swing.  *** All inputs are the banked
`c54.178` arms. *** **

Written r2788.  Stated for reversal.
"""
# ** SCOPE NOTE (r2931). **
# *** The shift propagated here is the ASYMPTOTIC l_A residual, +0.075%. The TRANSIENT position offset (+142, +80, +18 off the CR arm own line, B4) is ~860x larger and is NOT propagated. So "peak positions are not the cause" holds at the asymptotic scale and is untested for the transient. ***
# ⌗ The receipt's own computation is unaffected; this records WHAT IT MEASURES.
import glob
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  C56 -- is l_A computed or calibrated, and does its residual explain the swing?")
    print()
    cr = np.load(glob.glob(os.path.join(ROOT, '**', 'c54.178_cr.npz'), recursive=True)[0])
    lc = np.load(glob.glob(os.path.join(ROOT, '**', 'c54.178_lcdm.npz'), recursive=True)[0])

    # ⓵ computed, not calibrated
    for nm, z in (('LCDM', lc), ('CR', cr)):
        D, rs, lA = float(z['D_M']), float(z['r_s']), float(z['l_A'])
        check(f'⛭⛭ ⓵ {nm}: $\\pi D_M/r_s = {np.pi*D/rs:.2f}$ reproduces the stored $\\ell_A={lA:.2f}$ '
              '-- ** computed, not calibrated **',
              abs(np.pi*D/rs - lA) < 0.5)

    # ⓶ the cancellation
    D1, r1 = float(lc['D_M']), float(lc['r_s'])
    D2, r2 = float(cr['D_M']), float(cr['r_s'])
    dD, dr = (D2-D1)/D1, (r2-r1)/r1
    resid = (1+dD)/(1+dr) - 1
    check(f'⛭⛭⛭ ⓶ and both parts fall together: $D_M$ {100*dD:+.2f}%, $r_s$ {100*dr:+.2f}%, '
          f'leaving $\\ell_A$ at {100*resid:+.3f}%',
          abs(dD) > 0.05 and abs(dr) > 0.05 and abs(resid) < 0.002)

    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))
    check('and P15 claims exactly that in advance: "the acoustic-scale calibration, met from the '
          'other end and to that accuracy rather than exactly"',
          'met from the other end and to that accuracy rather than exactly' in p15)

    # ⓷ but it is far too small
    ls = lc['ls']
    Dl = lc['Dl']
    frac = np.abs(np.gradient(Dl, ls)*(ls*abs(resid))/Dl)
    meas = np.abs(cr['Dl']/lc['Dl'] - 1)
    check(f'⛔ ⓷ but propagating that shift gives median $|dC/C|={100*np.median(frac):.2f}\\%$ against '
          f'a measured median swing of {100*np.median(meas):.1f}% -- ** two orders too small **',
          np.median(frac) < np.median(meas)/50)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** l_A is computed and its residual is not the oscillation. **")
    print('  ⛭⛭ ⓵ ** Computed, not calibrated ** — πD_M/r_s reproduces the stored ℓ_A in both arms.')
    print("     *** The NUMERICAL horn of r2787's fork is closed. ***")
    print(f'  ⛭⛭⛭ ⓶ ** And its survival is a real cancellation: ** D_M {100*dD:+.2f}%, r_s {100*dr:+.2f}%,')
    print(f'     ℓ_A {100*resid:+.3f}%.  ** P15 claims it in advance: ** "the acoustic-scale')
    print('     calibration, met from the other end and to that accuracy rather than exactly."')
    print(f'  ⛔ ⓷ ** But the residual is two orders too small: ** median |dC/C| = {100*np.median(frac):.2f}%')
    print(f'     against a measured {100*np.median(meas):.1f}%.  ** It explains under 1% of the swing. **')
    print('  ⓸ *** SO NEITHER OF THE TWO THINGS THAT LOOK LIKE PHASE ACCOUNTS FOR IT: not the envelope')
    print('     (r2786, withdrawn), not the peak positions (here).  What remains is peak AMPLITUDE')
    print('     varying comb-periodically — the peaks in the right places and the wrong heights. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""B6 -- c54.191 verified here: the acoustics work at 98% of the required rate, and the experiment this
line named at r2485 answered a question this line had posed as a false dichotomy.

** ⓵ THE POSITIVE RESULT, REPRODUCED FROM THE FORK'S OWN SPECTRA. **

Moving the one fitted parameter so the sound horizon falls, and asking whether the peak spacing responds
at the rate ordinary acoustics requires (spacing ~ 1/r_s):

      run                r_s        slope      intercept/l_A
      as coded        135.461      294.400        -0.8780
      pin moved       120.162      331.200        -0.8988

      r_s changes by  -11.29%
      acoustics requires  +12.73%
      the spacing does    +12.50%
      ⇒ *** 98.2% OF THE ACOUSTIC RATE ***

** THE PEAKS IN THIS CONSTRUCTION ARE SET BY ITS OWN SOUND HORIZON.  That is not a fit -- it is a
RESPONSE to a moved parameter, in the direction and magnitude acoustics demands. **

** ⓶ AND THE PHASE TABLE REPRODUCES: ** control -0.263, CR as coded -0.878, pin moved -0.899, opposite
seam phase -0.671.  ⇒ ** the fitted parameter moves the phase by 3% of the discrepancy; the seam datum's
phase freedom closes 34% and stops. **

** ⛔ ⓷ AND THAT ANSWERS A QUESTION THIS LINE POSED AS A FALSE DICHOTOMY AT r2485. **

r2485 named the experiment and stated its outcomes: "** if it does not move, the 0.62*pi is structural
and the corrected claim is far stronger than it is today.  If it does, the disagreement is a datum
statement after all. **"

  ⇒ *** THE ANSWER IS NEITHER.  IT MOVES, AND IT STOPS AT 34%. ***

  ** And that is a BETTER result than either horn: a datum freedom that MOVES the phase confirms the
  diagnosis is a PHASE diagnosis -- exactly what a phase diagnosis predicts -- while one that CANNOT
  CLOSE the gap leaves the remainder structural. **

⌗ ** SEVENTEENTH INSTANCE, AND THE SECOND IN SIXTEEN REVISIONS OF THE SAME SHAPE. **  B3 (r2470)
recorded the rule after this line read the fork's candid "either/or" as a partition: ** "a dichotomy
someone stated in passing is not a proof of exhaustiveness." **  ⇒ *** r2485 wrote one of its own, and
the rule it had filed fifteen revisions earlier is the rule that catches it. ***
⇒ ** THE SHARPER FORM: when you name an experiment and state its outcomes, the outcomes are a
PREDICTION about the answer space and carry the same burden as any other prediction.  "If X then A,
else B" asserts that A and B exhaust it, and that assertion is almost never checked. **

** ⓸ AND THE SECOND RETRACTION IS CORRECT TOO. **  c54.189's "the peaks track their own sound horizon
at 24% of the rate acoustics requires" was measured ** on the first peak -- inside the transient c54.190
found. **  Over this pin range the first peak moves at 37% against the series' 98%.  ** Do not carry "a
quarter of the acoustic rate". **

WHAT IS NOT CLAIMED.  ** Not that a 0.62*pi phase discrepancy is a verdict ** -- F5 unsoftened, PO-7
protected, the conversion Daryl's.  Not that "why 0.62*pi" is answered: ** only that an acoustic phase
shift is a computable consequence of the driving, so the question now has an ADDRESS, which the
four-item list it replaces did not. **

Written r2486.  Stated for reversal.
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


def read(n):
    z = np.load(os.path.join(SP, n))
    ls, Dl = z['ls'], z['Dl']
    pk = ls[argrelextrema(Dl, np.greater, order=3)[0]]
    return pk, float(z['l_A']), float(z['r_s'])


def fit(pk, lA):
    n = np.arange(1, len(pk) + 1)
    m = (n >= 4) & (n <= min(8, len(pk)))
    a, b = np.polyfit(n[m], pk[m], 1)
    return a, b/lA


def main():
    print()
    print('  B6 -- do the acoustics work, and was the r2485 dichotomy exhaustive?')
    print()
    pk0, lA0, rs0 = read('c54.186_cr_L3000.npz')
    pk1, lA1, rs1 = read('c54.191_cr_lA340_L3000.npz')
    pkp, lAp, _ = read('c54.191_cr_phipi_L3000.npz')
    pkl, lAl, _ = read('c54.186_lcdm_L3000.npz')

    a0, i0 = fit(pk0, lA0)
    a1, i1 = fit(pk1, lA1)
    ap, ip = fit(pkp, lAp)
    al, il = fit(pkl, lAl)

    # ⓵ the acoustic response
    drs = (rs1 - rs0)/rs0
    req = 1/(1 + drs) - 1
    got = (a1 - a0)/a0
    check(f'moving the pin drops r_s by {drs:.2%}', -0.13 < drs < -0.10)
    check(f'ordinary acoustics (spacing ~ 1/r_s) requires {req:+.2%}', 0.11 < req < 0.14)
    check(f'and the fitted spacing changes by {got:+.2%}', 0.11 < got < 0.14)
    check(f'⛭⛭ ⇒ {got/req:.1%} OF THE ACOUSTIC RATE -- the peaks are set by its own sound horizon',
          0.93 < got/req < 1.03)

    # ⓶ the phase table
    check(f'control intercept {il:+.4f}, CR as coded {i0:+.4f}', abs(il + 0.263) < 5e-3
          and abs(i0 + 0.878) < 5e-3)
    check(f'pin moved {i1:+.4f} -- the fitted parameter moves the phase by '
          f'{abs(i1-i0)/abs(i0-il):.1%} of the discrepancy', abs(i1 - i0)/abs(i0 - il) < 0.06)
    check(f'opposite seam phase {ip:+.4f} -- the datum freedom closes '
          f'{abs(ip-i0)/abs(i0-il):.0%} of it and stops',
          0.28 < abs(ip - i0)/abs(i0 - il) < 0.42)

    # ⓷ the dichotomy
    moved = abs(ip - i0) > 0.05
    closed = abs(ip - il) < 0.05
    check('⛔ r2485 said "if it does not move, structural; if it does, a datum statement"',
          True is not False and moved)
    check('⇒ IT MOVES (so the first horn is false)', moved)
    check('⇒ AND IT DOES NOT CLOSE (so the second horn is false too)', not closed)
    check('⇒⇒ THE DICHOTOMY WAS NOT EXHAUSTIVE, and the actual answer is better than either horn: '
          'a freedom that MOVES the phase confirms it is a PHASE, and one that CANNOT CLOSE leaves '
          'the remainder structural', moved and not closed)

    # ⓸ the second retraction
    d1 = (pk1[0] - pk0[0])/pk0[0]
    check(f'and the first peak moves only {d1:.1%} over this pin range, against the series\' '
          f'{got:.1%} -- so c54.189\'s "24% of the acoustic rate" was the TRANSIENT',
          d1 < got)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the acoustics work, and my r2485 dichotomy was false. **')
    print(f'  r_s falls {drs:.2%}; acoustics requires {req:+.2%}; the spacing does {got:+.2%} --')
    print(f'  ** {got/req:.1%} of the acoustic rate.  The peaks are set by this construction\'s own sound')
    print('     horizon, as a RESPONSE to a moved parameter rather than as a fit. **')
    print('  ⛔ AND r2485 posed "structural OR datum" as exhaustive.  ** It moves, and it stops at 34%. **')
    print('     ⇒ Neither horn -- and the truth is better than either: ** a freedom that MOVES the phase')
    print('       confirms the diagnosis is a phase diagnosis; one that CANNOT CLOSE leaves the')
    print('       remainder structural. **')
    print('  ⌗ Seventeenth instance, and B3 filed the rule fifteen revisions ago: ** a dichotomy someone')
    print('    stated in passing is not a proof of exhaustiveness -- including one you state yourself. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

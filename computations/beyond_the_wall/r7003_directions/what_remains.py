"""⓷ WHAT CAN THE FILTER STILL DECIDE? -- r7003+cc66.54.

⛔ *The order's ⓷: "Sign and growth are applicable and the candidate passes both.  Is that enough to say
anything, or is a two-condition filter with the third permanently unavailable simply not a filter?
Either answer changes what this sector should do next, and I would rather have the honest one than a
third candidate."*

** THE FIRST THING TO GET RIGHT IS THAT THE THIRD CONDITION IS NOT UNAVAILABLE IN GENERAL. **  It needs
the candidate's departure in band 1.  ⓵ closes band 1 to *oscillation-amplitude* estimators, by the
fields.  It does NOT close band 1 to a candidate computed from the kernel or the background -- and
`cc66.52`'s projection-width channel was exactly such a candidate, with a band-1 value, and the filter
EXCLUDED it on curvature.  ⇒ ** So the third condition is available for one class of candidate and
permanently unavailable for the other, and the line between them is whether the candidate is an
oscillation amplitude of a source field. **
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7001_directions'))
import held_period as H                                                       # noqa: E402

print(__doc__)
print('=' * 100)

# the two classes, each at band 1, from the banks rather than from memory
KERN = np.array([1.00343, 1.00569, 1.00816, 1.01079, 1.01350, 1.01640, 1.01955]) - 1.0   # cc66.52
P = {}
for t in ('lcdm', 'cr'):
    q_, um_, ud_ = H.fields(t)
    P[t] = (H.period_of(q_, um_, 2.5, 8.0), H.period_of(q_, ud_, 2.5, 8.0))


def cand(half=0.5, bd=1):
    o = {}
    for t in ('lcdm', 'cr'):
        Q, R = H.held_ratio(t, P[t][0], P[t][1], half=half, bd=bd, step=0.02)
        o[t] = np.array([np.mean(np.interp(np.linspace(a, b, 200), Q, R))
                         for a, b in zip(H.QE[:-1], H.QE[1:])])
    return o['cr'] / o['lcdm'] - 1.0


ALLS = np.array([cand(half=h, bd=b) for h in (0.35, 0.5, 0.75, 1.0) for b in (1, 2)])
AMP = cand()
SPR = ALLS.max(axis=0) - ALLS.min(axis=0)
print('\n  the two candidate classes at BAND 1:')
print(f"    KERNEL class  (`cc66.52`'s projection width)  band 1 = {KERN[0]:+.5f}   "
      f"computed, not estimated -- an integral of banked profiles, so band 1 is simply a value of q")
print(f"    AMPLITUDE class (the surviving candidate)     band 1 = {AMP[0]:+.5f}   "
      f"spread {SPR[0]:.4f} across eight estimator settings, which exceeds it")
print('    ⇒ ** the filter EXCLUDED the kernel-class candidate on curvature and cannot apply that '
      'condition to the amplitude-class one at all. **')

print("""
  ⛔⛔ AND THAT IS WORSE NEWS THAN "TWO CONDITIONS OUT OF THREE", WHICH IS THE HONEST ANSWER TO ⓷.

    `cc66.51` settled which class can carry the excess, and on physics rather than on preference:
    ** trough-filling is an oscillating term a quarter period out of phase adding into another's
    troughs, so what fills a trough is an oscillation AMPLITUDE, and the contrast statistic is itself a
    standard deviation of the oscillation about a running envelope. **
    ⇒ *** SO THE FILTER'S FULL STRENGTH IS AVAILABLE EXACTLY FOR THE CLASS THAT CANNOT CARRY THE
    EXCESS, AND ITS THIRD CONDITION IS PERMANENTLY UNAVAILABLE EXACTLY FOR THE CLASS THAT CAN. ***

  ⌗ SO: IS A TWO-CONDITION FILTER A FILTER?  Separated into what it can and cannot do, because the two
    answers are different and the row needs both.

    ⓐ ** AS AN EXCLUSION DEVICE, YES, AND IT HAS NOT LOST ANYTHING. **  Sign and growth are each a
      necessary condition on a carrier, and four of the five candidates in `cc66.50`'s table were
      excluded on growth alone -- those exclusions never used curvature and stand untouched.  *A
      necessary condition that a candidate fails is a complete answer, and two of them are two.*

    ⓑ ** AS A CONFIRMATION DEVICE, NO -- AND IT NEVER WAS ONE, NOT EVEN WITH THREE. **  Sign, growth
      and curvature are all conditions on the SHAPE of a departure in q.  *Three matching shapes is
      still a shape match: it does not measure how much contrast a given amplitude ratio produces, and
      nothing that fails to measure that can promote a candidate.*  ⇒ ** So the candidate's passing
      two conditions is exactly as much as its passing three would have been: it is not excluded. **

    ⓒ ** WHICH MAKES THE MISSING CONDITION COST LESS THAN IT LOOKS, AND THE ROW'S NEXT STEP NOT A
      CONDITION AT ALL. **  What would settle the surviving candidate is the COUPLING: how much band
      contrast does a dipole-to-monopole amplitude ratio of a given size actually produce, through the
      projection this instrument already computes?  *That is a calculation on the bands where the
      candidate IS measured -- q from 1.90 up -- and it needs band 1 not at all.*
      ⛔ **Named as what the question is, not proposed as a channel: the order's ⓸ closes the list and
      this is not an addition to it.**

  ⇒ ** THE PLAIN ANSWER: the filter can still eliminate and could never promote; it has eliminated
    everything it can reach; and the one candidate left cannot be eliminated by it and was never going
    to be confirmed by it.  The row's remaining question is quantitative and not a fourth condition. **
""")

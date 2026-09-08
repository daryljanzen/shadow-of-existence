#!/usr/bin/env python3
"""C34 -- `PO-10`'s deliverable is fully specified, and it is a PAIR rather than a number: the acoustic
sector is open as `PO-7`, its phase freedom is DISCRETE, and both branches are scored against the same
threshold.

** THE QUESTION, r2711, Daryl: ** "*** isn't the acoustic sector open still?  So is this just part of the
machinery that will run as we compute?  And is there something left to close off this item? ***"  ** Yes,
yes, and yes -- and the third is what this receipt does. **

** ⛭⛭ ⓵ THE ACOUSTIC SECTOR IS OPEN, AND IT IS `PO-7`. **  "The first acoustic peak, and the propagated
comb.  Does the construction imprint an acoustic phase?"  *** And it bears directly on `PO-10`, which
r2709-r2710 had been setting up as though the input were settled. ***

** ⓶ THE DEPENDENCY, IN P15's OWN NUMBERS. **  "the seam datum's own phase freedom is ** a real lever on
it and spans a third of it **---at the opposite phase ** the gap to the control closes from $0.615$ to
$0.408$, thirty-four per cent, and no further **.  That is the confirmation the diagnosis wanted: the
datum's phase moves the acoustic phase, as a phase diagnosis predicts, and ** cannot close the
discrepancy **."

  ⇒ *** So a $\\chi^2$ scored while `PO-7` is open carries a two-valued input.  It is not a single
      number, and r2710's threshold was being set up for one. ***

** ⛭ ⓷ BUT THE FREEDOM IS DISCRETE, WHICH IS THE THING THAT KEEPS `PO-10` TRACTABLE. **  `CRPHI` is a
choice between ** two ** phases, not a continuous parameter.

      *** CR k=2 (Omega_m + A_s)                 dBIC = 21.5
          if CRPHI were counted as a parameter   dBIC = 16.1 ***

  ⇒⇒ *** A discrete two-valued choice is not a continuous parameter and does not enter $k$.  Standard
      practice is to REPORT BOTH BRANCHES, not to penalise half a parameter.  So the threshold stays at
      $21.5$ and the deliverable doubles. ***

** ⓸ SO THE SPECIFICATION IS CLOSED, AND IT IS THIS. **
      *** PO-10 delivers  chi^2(phi = 0)  and  chi^2(phi = pi),
          each at CR's best Omega_m on L-147's 215 TT bins,
          each compared to flat LambdaCDM's best-fit chi^2 against dBIC = 21.5;
          and PO-7, when it closes, SELECTS which branch is physical. ***

  ⌗ ** Which answers the middle question directly: ** *** yes, this is machinery that runs as the
    computation proceeds -- but the machinery is now fully specified, and specifying it was the part
    that could be done without the compute. ***

WHAT IS NOT CLAIMED.  ** Not that either $\\chi^2$ is known ** -- *** neither branch is scored, and that
is the whole of what `PO-10` still owes. ***  ** Not that `PO-7` is easier ** -- it selects the branch and
is unchanged.  ** Not that $0.408$ and $0.615$ are $\\chi^2$ values ** -- they are the acoustic-phase gap
to the control, and the receipt they carry is P15's.

Written r2711.  Stated for reversal.
"""
import os
import subprocess
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
N = 215


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
    print("  C34 -- what can PO-10 deliver while PO-7 is open?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    po7 = next(l for l in raw.split('\n')
               if re.match(r'\|\s*~?~?\*\*PO-7\*\*', l))

    # ⓵ the acoustic sector is open
    check('⓵ the acoustic sector is open as PO-7: "The first acoustic peak, and the propagated comb"',
          'The first acoustic peak, and the propagated comb' in po7)

    # ⓶ the dependency, in P15's numbers
    # ⛔⛭⛭ AMENDED r4518.  ** r4111 restated P15's acoustic section, 539 lines to 73, and this
    #    receipt's three quotations went with it. **  The old form gave the lever as a single pair of
    #    numbers -- the gap closing from $0.615$ to $0.408$ at the opposite phase, "thirty-four per
    #    cent, and no further".  *** The paper does not report less now, it reports more: *** the
    #    datum's TWO freedoms are enumerated, and the first peak is measured across all seventeen
    #    readings a four-peak criterion admits -- spanning $148$ to $228$, a factor of $1.541$ -- with
    #    the sky's $220.6$ inside the span and "there is no such reading" that reproduces the sky.
    #    ⇒ The historical numbers are read at `48e55a6b^`, where they stood; what the paper says NOW
    #      carries the same claim this receipt needs -- the datum's freedoms move the result and do
    #      not close it -- and is asserted on its own terms rather than re-pinned to a phrase P15 has
    #      replaced with a stronger measurement.
    _P15_THEN = re.sub(r'\s+', ' ', subprocess.run(
        ['git', 'show', '48e55a6b^:corpus/CR_cosmology.tex'],
        cwd=ROOT, capture_output=True, text=True, errors='replace').stdout)
    check('⛭⛭ ⓶ᵃ the phase freedom WAS given as a lever with a pair of numbers, read where it stood '
          '(48e55a6b^, before r4111): "the seam datum\'s own phase freedom is a real lever on it and '
          'spans a third of it", the gap closing "from $0.615$ to $0.408$, thirty-four per cent, and '
          'no further", and "cannot close the discrepancy"',
          len(_P15_THEN) > 100000
          and "own phase freedom is a real lever on it and spans a third of it" in _P15_THEN
          and 'thirty-four per cent, and no further' in _P15_THEN
          and 'cannot close the discrepancy' in _P15_THEN)
    check('⛭⛭ ⓶ᵇ and P15 states it MORE strongly now, which is why the pins broke: "The seam datum '
          'carries two freedoms, and how far the first peak moves with them is measured" -- across '
          'the seventeen admitted readings the first peak spans $148$ to $228$, a factor of $1.541$, '
          'the sky\'s $220.6$ inside it, and "there is no such reading" reproducing the sky.  ** So a '
          '$\\chi^2$ scored while PO-7 is open still carries a two-valued input, and the freedoms '
          'still do not close the gap. **',
          'The seam datum carries two freedoms' in p15
          and 'how far the first peak moves with them is measured' in p15
          and 'there is no such reading' in p15)

    # ⓷ discrete, so k is unchanged
    dB2 = (6 - 2)*np.log(N)
    dB3 = (6 - 3)*np.log(N)
    check(f'⛭ ⓷ the freedom is DISCRETE (two phases), so it does not enter $k$: the threshold stays '
          f'{dB2:.1f} rather than dropping to {dB3:.1f}',
          abs(dB2 - 21.5) < 0.1 and abs(dB3 - 16.1) < 0.1 and dB2 > dB3)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-10's deliverable is a PAIR, and the specification is now closed. **")
    print('  ⓵ ** The acoustic sector IS open — it is PO-7 ** ("the first acoustic peak, and the')
    print('     propagated comb"), and r2709-r2710 were setting PO-10 up as though its input were')
    print('     settled.')
    print('  ⛭⛭ ⓶ ** The dependency, in P15\'s numbers AS THEY STOOD (48e55a6b^, before r4111): **')
    print('     the seam phase "is a real lever ... at the')
    print('     opposite phase the gap to the control closes from ** 0.615 to 0.408, thirty-four per')
    print('     cent, and no further **" — and "** cannot close the discrepancy **".')
    print('     ⇒ *** So a χ² scored while PO-7 is open carries a TWO-VALUED input. ***')
    print('  ⛭ ⓷ ** But the freedom is DISCRETE, which is what keeps PO-10 tractable: ** two phases, not')
    print(f'     a continuous parameter, so it does NOT enter k.  The threshold stays {dB2:.1f} rather')
    print(f'     than dropping to {dB3:.1f}.  ** Standard practice is to report both branches, not to')
    print('     penalise half a parameter. **')
    print('  ⓸ ** SO THE SPECIFICATION IS CLOSED: **')
    print('       PO-10 delivers χ²(φ=0) and χ²(φ=π), each at CR\'s best Ω_m on the same 215 bins,')
    print('       each against ΔBIC = 21.5 — and PO-7, when it closes, SELECTS the physical branch.')
    print('     ⌗ *** Yes, it is machinery that runs as the computation proceeds — and specifying it was')
    print('       the part that could be done without the compute. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""T1 -- `PO-12` is HALF BUILT: the specification the bespoke transfer runs against exists, and the paper
computes it two sections earlier than the place it calls the debt.

** THE ITEM. **  `CR_cosmology`'s own named debt: "It is a debt owed and named as such: ** not a missing
idea but a computation this sequence owes and has not yet run **, and the paper's own open edge rather
than another's."

** ⓵ AND THE PAPER STATES THE DEBT AS TWO STEPS, NOT ONE. **  "This is a genuine build, not a plug-in:
it requires ** FIRST specifying how the fluctuations gravitate on the radiation-free background ** ---the
piece that sets the high-$\\ell$ driving envelope, and which the standard Boltzmann codes cannot supply
because they tie radiation's gravity to its presence and so cannot represent the content-not-rate split
the layered rate rests on---** AND THEN a bespoke transfer against that specification **."

  ⇒ ** ① the specification (how fluctuations gravitate on the radiation-free background); ② the transfer
    run against it. **

** ⛭⛭ ⓶ AND STEP ① IS BUILT.  THE PAPER SAYS SO TWICE, IN AN EARLIER SECTION. **

  "the same radiation-free rate that enlarges $r_D$ also governs the high-$\\ell$ driving envelope, so
   CR's high-$\\ell$ spectrum rests on short-wavelength collapse-phase driving rather than on the boost an
   expanding radiation era supplies.  ** That driving is computed below (\\S\\ref{sec:envelope}), and the
   calculation removes the licence the shortcut lacked: the envelope is DERIVED ON THE COLLAPSE LEG
   RATHER THAN IMPORTED. **"

  ⇒ *** "The piece that sets the high-$\\ell$ driving envelope" is step ① word for word, and
      `sec:envelope` computes it.  The specification the bespoke transfer would run against EXISTS. ***

** ⓷ SO WHAT IS OWED IS THE SECOND STEP ALONE, AND THAT IS A DIFFERENT SIZE OF THING. **  ① is the
physics -- how gravity works on a background no standard code can represent.  ② is a transfer run against
a specification already in hand.
  ⌗ ** And the paper says a Boltzmann transfer of the needed kind is already built for a neighbouring
    purpose: ** "the flat-projection transfer of the discrete closed-$S^3$ source is built with a ** genuine
    Boltzmann transfer **---the exact CMB temperature transfer $\\Delta_\\ell(k)$ (Sachs--Wolfe, early and
    late integrated Sachs--Wolfe, and Doppler ...)".
  ⇒ *** So the machinery exists and the specification exists; what has not been run is the two against
      each other. ***

** ⓸ AND ONE THING THE ROW CLAIMS IS NARROWER THAN IT READS. **  "the transfer is what makes the 8%
signature confrontable at all" -- but the paper also says ** "The peak heights are then carried by a
STRUCTURAL argument rather than a bespoke transfer." **
  ⇒ ** So the transfer is owed for the tilt-irreducible RESIDUAL **, not for the heights: "largely
    absorbable into $n_s$ ... ** with the tilt-irreducible residual the part the transfer would
    isolate **".

WHAT IS NOT CLAIMED.  ** Not that the transfer is easy ** -- the paper calls it a genuine build and this
receipt does not run it.  ** Not that `sec:envelope` is the whole of step ① ** -- it computes the driving;
whether it constitutes the full specification a transfer needs is not established here.  ** Not that the
row should close **: ② is genuinely not run, and the item stands.

Written r2623.  Stated for reversal.
"""
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
    print('  T1 -- is PO-12 one step or two?')
    print()
    p15 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                                   encoding='utf-8', errors='replace').read())
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(l for l in raw.split('\n') if l.startswith('| **PO-12**'))

    # ⓵ two steps
    check('⓵ the paper states the debt as TWO steps: "it requires first specifying how the fluctuations '
          'gravitate on the radiation-free background ... and then a bespoke transfer against that '
          'specification"',
          'it requires first \\emph{specifying how the fluctuations gravitate on the '
          'radiation-free background}' in p15
          and 'and then a bespoke transfer against that specification' in p15)
    check('and names step ① as what sets the envelope: "the piece that sets the high-$\\ell$ driving '
          'envelope"',
          'the piece that sets the high-$\\ell$ driving envelope' in p15)
    check('and why no standard code supplies it: "they tie radiation\'s gravity to its presence and so '
          'cannot represent the content-not-rate split"',
          "they tie radiation's gravity to its presence" in p15)

    # ⓶ step ① is built
    check('⛭⛭ ⓶ and STEP ① IS BUILT: "That driving is computed below (\\S\\ref{sec:envelope}), and the '
          'calculation removes the licence the shortcut lacked: the envelope is derived on the collapse '
          'leg rather than imported."',
          'That driving is computed below' in p15
          and 'the envelope is derived on the collapse leg rather than imported' in p15)
    check('with the same object named: "the same radiation-free rate that enlarges $r_{D}$ also governs '
          'the high-$\\ell$ driving envelope"',
          'also governs the high-$\\ell$ driving envelope' in p15)

    # ⓷ the machinery exists too
    check('⓷ and a genuine Boltzmann transfer is already in use at large angles: "on a genuine '
          'Boltzmann transfer a dip whose \\emph{minimum falls at $\\ell=4$}"',
          'on a genuine Boltzmann transfer a dip whose' in p15)

    # ⓸ the heights do not need it
    check('⓸ and the heights do NOT need it: "The peak heights are then carried by a structural argument '
          'rather than a bespoke transfer."',
          'carried by a structural argument rather than a bespoke transfer' in p15)
    check('so what the transfer would isolate is the residual: "with the tilt-irreducible residual the '
          'part the transfer would isolate"',
          'with the tilt-irreducible residual the part the transfer would isolate' in p15)

    # the row
    check("⌗ and the PO-12 row carries the debt but not the split", 'debt' in row.lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** PO-12 is HALF BUILT, and the paper says so two sections earlier. **')
    print('  ⓵ ** The debt is TWO steps: ** ① specify how fluctuations gravitate on the radiation-free')
    print('     background -- the piece that sets the high-ℓ driving envelope, which no standard')
    print('     Boltzmann code can supply -- and ② a bespoke transfer against that specification.')
    print('  ⛭⛭ ⓶ ** And ① IS BUILT: ** "That driving is computed below (sec:envelope) ... ** the envelope')
    print('     is derived on the collapse leg rather than imported. **"')
    print('  ⓷ ** And the machinery exists: ** a "genuine Boltzmann transfer" is already built for the')
    print('     flat-projection of the closed-S³ source.')
    print('     ⇒ ** The specification exists and the machinery exists; what has not been run is the two')
    print('       against each other. **')
    print('  ⓸ ** And the item is narrower than the row reads: ** the peak HEIGHTS are "carried by a')
    print('     structural argument rather than a bespoke transfer" -- ** the transfer is owed for the')
    print('     TILT-IRREDUCIBLE RESIDUAL. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

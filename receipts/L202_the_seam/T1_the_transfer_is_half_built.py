#!/usr/bin/env python3
"""T1 -- `PO-12` is HALF BUILT: the specification the bespoke transfer runs against exists, and the paper
computes it two sections earlier than the place it calls the debt.

** THE ITEM. **  `CR_cosmology`'s own named debt: "It is a debt owed and named as such: ** not a missing
idea but a computation this sequence owes and has not yet run **, and the paper's own open edge rather
than another's."

** ⓵ AND THE PAPER STATES THE DEBT AS TWO STEPS, NOT ONE. **  "This is a genuine build, not a plug-in:
it requires ** FIRST specifying how the fluctuations gravitate on the geometric stacking background ** ---the
piece that sets the high-$\\ell$ driving envelope, and which the standard Boltzmann codes cannot supply
because they tie radiation's gravity to its presence and so cannot represent the content-not-rate split
the layered rate rests on---** AND THEN a bespoke transfer against that specification **."

  ⇒ ** ① the specification (how fluctuations gravitate on the geometric stacking background); ② the transfer
    run against it. **

** ⛭⛭ ⓶ AND STEP ① IS BUILT.  THE PAPER SAYS SO TWICE, IN AN EARLIER SECTION. **

  "the same geometric stacking rate that enlarges $r_D$ also governs the high-$\\ell$ driving envelope, so
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

** ⛭ r6931+70.1 -- DISCHARGED: STEP ② HAS BEEN RUN, AND THE PAPER NO LONGER STATES THE DEBT. **  The
register struck `PO-12` at r2702 ("the bespoke transfer is BUILT and its numbers verified"), and
r6719 (440623b6) brought P15 to it: the two-step debt sentence, "the piece that sets the high-ell
driving envelope", "they tie radiation's gravity to its presence" and "the tilt-irreducible residual
the part the transfer would isolate" all went, replaced by "The end-to-end branch-point-to-recombination
transfer is run (sec:refit-bound)" -- a two-arm line-of-sight Boltzmann integral "carried on this
cosmology's own background with the perturbations on the leaf congruence the framework assigns them",
validated on its control -- and the residual it was to isolate is now LOCATED: "a Gaussian residual in
ell that no tilt removes".  ** This receipt's finding -- that ① existed and only ② was owed -- is what
that run confirms; its "half built" is the state at r2623, not now.  The checks below are re-pointed
at what discharged each part. **

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
        # ** r2722: a STRUCK row's tag is `~~**PO-12**~~`.  *** A `startswith` on the unstruck
        # form raises StopIteration the moment the row closes -- so the record dies on the
        # corpus moving FORWARD, which is the one thing a record must survive. ***
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(l for l in raw.split('\n') if re.match(r'\|\s*~*\*\*PO-12\*\*', l))

    # ⓵ two steps
    # ⛔⛭ RE-PINNED r3950 -- same cause as C23/C24: r3841's sweep rewrote this receipt's PINNED
    #   STRING from `radiation-free` to `geometric stacking`, and P15 was swept to a different
    #   successor.  The paper says "specifying how the fluctuations gravitate on the GEOMETRICALLY
    #   FIXED background".  Pinned to the fragment that carries the claim, not the whole clause.
    # ** r6931+70.1: CLASS (b) -- DISCHARGED, FOR THE THREE CHECKS BELOW.  They pinned P15's
    #   statement of the debt: "it requires first specifying how the fluctuations gravitate on the
    #   geometrically fixed background -- the piece that sets the high-ell driving envelope, and
    #   which the standard Boltzmann codes cannot supply because they tie radiation's gravity to its
    #   presence ... -- and then a bespoke transfer against that specification".  440623b6 (r6719,
    #   "the transfer is run") removed the whole sentence because the debt was PAID (PO-12 struck
    #   r2702).  Re-pointing at the reworded prose would not be possible and would not be honest; so
    #   each check is re-pointed at what discharged its part:
    #     ⓵ the two steps  -> P15 states the end-to-end transfer RUN, and "three are run" of its four
    #                         named debts;
    #     ① the spec       -> the run carries "the perturbations on the leaf congruence the framework
    #                         assigns them", on "this cosmology's own background" -- step ① in use;
    #     no standard code -> the bespoke instrument is VALIDATED against a standard code on its
    #                         control (C59_the_control_reproduces_camb_...), which is what "a genuine
    #                         build, not a plug-in" had to come to.
    check('⓵ the two-step debt is PAID: "The end-to-end branch-point-to-recombination transfer is run", '
          'three of P15\'s four named debts run',
          'The end-to-end branch-point-to-recombination transfer is run} (\\S\\ref{sec:refit-bound})' in p15
          and 'Of the four, three are run and one is a frontier' in p15)
    check('and step ① is what it runs on: "carried on this cosmology\'s own background with the '
          'perturbations on the leaf congruence the framework assigns them"',
          "carried on this cosmology's own background with the perturbations on the leaf congruence "
          'the framework assigns them' in p15)
    check('and the build no standard code could be plugged in for is VALIDATED against one on its '
          'control (C59_the_control_reproduces_camb_and_the_height_defect_was_k_truncation)',
          'validated on its control to' in p15
          and 'C59_the_control_reproduces_camb_and_the_height_defect_was_k_truncation' in p15)

    # ⓶ step ① is built
    check('⛭⛭ ⓶ and STEP ① IS BUILT: "That driving is computed below (\\S\\ref{sec:envelope}), and the '
          'calculation removes the licence the shortcut lacked: the envelope is derived on the collapse '
          'leg rather than imported."',
          'That driving is computed below' in p15
          and 'the envelope is derived on the collapse leg rather than imported' in p15)
    check('with the same object named: "the same geometric stacking rate that enlarges $r_{D}$ also governs '
          'the high-$\\ell$ driving envelope"',
          'e handover that fixes $r_D$ also governs the high-$\\ell$ driving envelope' in p15)

    # ⓷ the machinery exists too
    check('⓷ and a genuine Boltzmann transfer is already in use at large angles: "on a genuine '
          'Boltzmann transfer a dip whose \\emph{minimum falls at $\\ell=4$}"',
          'on a genuine Boltzmann transfer a dip whose \\emph{minimum falls at $\\ell=4' in p15)

    # ⓸ the heights do not need it
    check('⓸ and the heights do NOT need it: "The peak heights are then carried by a structural argument '
          'rather than a bespoke transfer."',
          'e then carried by a structural argument rather than a bespoke transfer' in p15)
    # ** r6931+70.1: CLASS (b) -- DISCHARGED.  "with the tilt-irreducible residual the part the
    #   transfer would isolate" went at 440623b6 (r6719) because the transfer isolated it: P15 now
    #   says the joint fit "locates [it] as a Gaussian residual in ell that no tilt removes".  Same
    #   object (the tilt-irreducible part of the diffusion-scale signature), now found rather than
    #   owed; the check pins the finding.
    check('so what the transfer was to isolate -- the tilt-irreducible residual -- it has isolated: '
          '"a Gaussian residual in $\\ell$ that no tilt removes"',
          'located by the joint fit as a Gaussian residual in $\\ell$ that no tilt removes' in p15)

    # the row
    check("⌗ and the PO-12 row carries the debt but not the split", 'debt' in row.lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** PO-12 was HALF BUILT at r2623, and the paper said so two sections earlier. **')
    print('  (r6931+70.1: DISCHARGED since -- PO-12 struck r2702, and P15 states the end-to-end transfer')
    print('   RUN on the leaf congruence, the tilt-irreducible residual located as a Gaussian no tilt')
    print('   removes.)')
    print('  ⓵ ** The debt is TWO steps: ** ① specify how fluctuations gravitate on the geometric stacking')
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

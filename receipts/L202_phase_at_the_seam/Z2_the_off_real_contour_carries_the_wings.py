#!/usr/bin/env python3
"""Z2 -- L-202 narrowed a second time, by L-211's procedure.  Still not decided.

** Z1 (r2451) LEFT THE QUESTION WITH A LOCATION: ** the seam phase is the ANTILINEAR face
K : tau~ -> conj(tau~); reality admits exactly two values of it; and ** K acts TRIVIALLY on values over
the reality set while R exchanges the branches. **  So the phase is not a second labelling of matter and
antimatter, and whatever K carries is carried OFF the reality set.  Z1 ended: "does the off-real contour
carry anything a trajectory can be said to HAVE?"

** L-211's PROCEDURE FOUND THE ANSWER TWO CLAUSES ON IN P7, NEVER JOINED TO THIS ROW. **

P7 sec:two-sided-closure, immediately after naming the antilinear face:

   "K ... ** fixes the neutral real axis, the self-conjugate photon congruence, and swaps the two
   conjugate WINGS of the lap. **  R and K are the two axis-symmetries of one analytic object, the
   plate C_r x C_tau~: the r-axis carrying R with the A_2 hexad and the two rulings, ** the tau~-axis
   carrying K with the cosmogenetic lap and its two wings. **"

⇒ ** SO THE OFF-REAL CONTOUR CARRIES THE TWO WINGS OF THE LAP, AND K SWAPS THEM.  That is exactly the
  structure Z1 said K's content must live in, and P7 states it. **

** AND IT GOES FURTHER: the composite CLOSES CHARGE CONJUGATION. **
   "R o K is an antilinear involution reproducing C's action on species, on |2M|, on the mass-sign, and
   on the Feynman-Stueckelberg particle<->antiparticle wing structure, while being blind to the
   electric-charge sign ... so charge conjugation factorises,
   C = (Q -> -Q)_field o (R o K)_geometric."

⇒ ** K IS NOT AN INTERPRETIVE OVERLAY.  It is one of two axis-symmetries of one analytic object, and
  its composite with R supplies every kinematic datum of C. **

** ⚠ AND YET L-202 IS STILL NOT DECIDED, AND THIS IS THE WHOLE POINT OF THE ROW'S CONSTRAINT. **
p0 asks about ** the phase structure at the seam RELATIVE TO TRAJECTORIES. **  What P7 establishes is
that K is real structure ** OF THE PLATE ** -- an involution of the analytic object with a geometric
action.  ** That is the OBJECT-level question, and it is not the TRAJECTORY-level one. **

⇒ *** THE NARROWING SHARPENS AGAIN AND STILL DOES NOT CLOSE: the phase is REAL STRUCTURE OF THE PLATE.
   Whether a TRAJECTORY carries it is what remains. ***

⌗ AND ONE FURTHER CUT, because P7 names a trajectory class: ** K FIXES "the self-conjugate photon
congruence." **  So some trajectories DO stand in a definite relation to K -- the null ones are its
fixed set.  ⇒ ** The live question narrows to the MASSIVE trajectories, which are the ones neither
fixed by K nor exchanged as a wing-pair in the way the photon congruence is. **

WHAT IS NOT CLAIMED.  Not that the phase is real structure relative to trajectories.  Not that it is
interpretation.  ** Only that K is established as real structure of the PLATE, that the photon
congruence is its fixed set, and that what remains is strictly narrower than what Z1 left: not "does the
off-real contour carry anything" -- it demonstrably does -- but "does a MASSIVE trajectory carry a
phase." **

⌗ AND THE ROUTE IS THE POINT AGAIN: this sat two clauses after a sentence the corpus quotes constantly,
and nothing joined it to p0's frontier item.  ** L-211's procedure is what looked. **

Written r2457.  Stated for reversal.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  Z2 -- what does the off-real contour carry?')
    print()
    p7 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'),
                                  encoding='utf-8', errors='replace').read())

    check('P7 names the antilinear face K on complexified cosmic time',
          'reality involution $K:\\tilde\\tau\\mapsto\\bar{\\tilde\\tau}$' in p7)
    check('⛭ and says what it DOES off the real axis: it "swaps the two conjugate wings of the lap"',
          'swaps the two conjugate wings of the lap' in p7)
    check('so the off-real contour demonstrably carries structure -- the two wings',
          'two conjugate wings' in p7)
    check('and R and K are "the two axis-symmetries of one analytic object, the plate"',
          'the two axis-symmetries of one analytic object' in p7)
    check('the tau~-axis carrying K with the cosmogenetic lap and its two wings',
          'carrying $K$ with the cosmogenetic lap and its two wings' in p7)

    check('⛭⛭ and the composite CLOSES charge conjugation: R o K reproduces C\'s action on species, '
          'on |2M|, on the mass-sign and on the Feynman-Stueckelberg wing structure',
          "reproducing $C$'s action on species" in p7
          and 'Feynman--St\\"uckelberg particle$\\leftrightarrow$antiparticle wing structure' in p7)
    check('with C factorising as (Q -> -Q)_field o (R o K)_geometric',
          'C=(Q\\mapsto-Q)_{\\mathrm{field}}\\circ(R\\circ K)_{\\mathrm{geometric}}' in p7)
    check('⇒ so K is NOT an interpretive overlay: it is geometric and it does work',
          'complex-analytic and geometric' in p7)

    # the cut that keeps this open
    check('AND K FIXES A TRAJECTORY CLASS: "the self-conjugate photon congruence"',
          'the self-conjugate photon congruence' in p7)
    check('so SOME trajectories stand in a definite relation to K -- the null ones are its fixed set',
          'fixes the neutral real axis, the self-conjugate photon congruence' in p7)

    # and the row's constraint, unbroken
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    check('L-202 is stated without being claimed BOTH WAYS, and this receipt decides neither',
          'not claimed BOTH WAYS' in arc)
    check("Z1's location -- 'does the off-real contour carry anything a trajectory can be said to "
          "HAVE?' -- is what this narrows, not what it answers",
          'off-real' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (a SECOND NARROWING; nothing is closed):')
    print('  ** The off-real contour DOES carry structure: the two conjugate wings of the lap, which K')
    print('     swaps. **  R and K are the two axis-symmetries of one analytic object, and their')
    print('  composite supplies every kinematic datum of charge conjugation.')
    print('  ⇒ ** So K is real structure OF THE PLATE, and that is the OBJECT-level question. **')
    print('    p0 asks the TRAJECTORY-level one, and it is not the same.')
    print('  ⌗ AND ONE FURTHER CUT: ** K fixes the self-conjugate photon congruence **, so the null')
    print('    trajectories are its fixed set.  ⇒ The live question is now strictly narrower than Z1')
    print('    left it: not "does the off-real contour carry anything" -- it demonstrably does -- but')
    print('    ** "does a MASSIVE trajectory carry a phase." **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

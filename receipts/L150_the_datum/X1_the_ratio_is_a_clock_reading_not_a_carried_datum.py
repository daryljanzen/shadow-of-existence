#!/usr/bin/env python3
"""X1_the_ratio_is_a_clock_reading_not_a_carried_datum.py -- L-150 section 1.

** THE QUESTION, sharpened by section 0. **  p0's frontier item 1 asks that rho_r/rho_m be the sole
tunable datum and that its derivation from the progenitor collapse be owed.  Section 0 found the
derivation ALREADY MADE -- but one universe back: THE_ASSUMPTIONS_RETREATED_UPWARD carries "the
progenitor's composition, derived", (rho_r/rho_m)_max ~ 7.3e-4, about 2.5x the observable leg's
present value, with turnaround at z ~ 1.5 and a mass of 4.3e52 kg.

    ** So: is the composition at OUR seam fixed by the progenitor's plus the crossing? **

THE ANSWER IS NO, AND THE REASON IS NOT THE CROSSING.  ** It is that rho_r/rho_m is not the kind of
quantity a crossing can carry, because it is not a constant of the evolution on either side. **

  (1) ** THE RATIO SCALES.  **  Radiation dilutes as a^-4 and matter as a^-3 in any FRW-like leaf, so
      rho_r/rho_m goes as 1/a.  ** A quantity that changes along the leg has no single value for a
      handover to transmit. **  Whatever the progenitor's ratio is at ITS maximum is not what the
      leaf carries to a later epoch; it is a reading taken at one point on a curve.

  (2) ** AND THE CROSSING IS MULTIPLICATIVE, WHICH MAKES IT WORSE, NOT BETTER, FOR THIS QUANTITY. **
      The corpus's own result: "hbar is multiplicative, and that is the whole asymmetry ... it
      survives in an amplitude and cancels in every logarithmic derivative", and the crossing
      "determines how much a perturbation is multiplied, and does not determine the perturbation".
      ⇒ A crossing that multiplies BOTH components by the same factor leaves the ratio UNCHANGED --
        lambda cancels -- so it transmits nothing about it.  A crossing that multiplied them
        DIFFERENTLY would rescale the ratio by lambda_r/lambda_m -- but ** the corpus states the
        reassignment carries the leaf's content across as INHERITED, one operation on the leaf, not
        a species-resolved one. **
      ⇒ ** Either way the crossing does not FIX the ratio: it is silent by cancellation, or it would
        need a species-selection rule the corpus has already withdrawn (P7's c54.162 withdrawal:
        "the exponent has nothing to act on; the crossing is lossless for every species"). **

  (3) ** AND THE CORPUS ALREADY TREATS IT AS A READING RATHER THAN A TRANSMITTED CONSTANT. **  P15
      calls rho_r/rho_m a "single inherited datum" and "a one-parameter accommodation, the structural
      analogue of the baryon-to-photon ratio", and P16 distinguishes it from eta explicitly: ** "eta
      fixes the abundances and the CMB peak HEIGHTS, rho_r/rho_m the peak SPACING" ** -- two data of
      the same handover, not one derived from the other.  And the observable rate is read LEFTWARD:
      "radiation and matter are inherited content read off the clock, never terms that source the
      rate".

** ⇒ THE VERDICT: THE DATUM HALF OF p0'S FRONTIER ITEM 1 DOES NOT CLOSE BY DERIVATION FROM THE
   PROGENITOR, AND THE OBSTRUCTION IS STRUCTURAL RATHER THAN OUTSTANDING WORK. **  rho_r/rho_m at our
seam is where the observable leg's clock is read, and the clock's zero is not something the previous
universe hands over -- it is fixed by WHEN, on our own leg, the reading is taken.

** ⇒ WHICH IS THE ONE-CONSTANT THEOREM'S SECOND FACE, ARRIVED AT FROM THE MATTER SIDE. **  L-200
showed the construction spends no free dimensionless constant because "a dimensionless magnitude
needs two invariants and the substrate has one".  ** rho_r/rho_m IS a dimensionless magnitude. **  So
the geometry cannot force it for exactly the reason it forces no other -- and the capstone's line,
"either the deepest thing the corpus knows about itself, or the sign that the question has been posed
at the wrong level", resolves here toward the first.

WHAT THIS DOES NOT CLAIM, and the distinction matters for the fork's interface:
  * It does NOT claim the progenitor derivation is worthless -- it fixes the progenitor's own
    composition, its turnaround redshift and its mass, and those stand.
  * It does NOT claim z_onset is undetermined; z_onset is a different quantity, fixed on the
    observable leg, and NOTHING here bears on it.  ** The fork's instrument keeps pinning z_onset
    from the measured acoustic angle, and that must be said rather than claimed past. **
  * It does NOT close p0's item; ** it converts the datum half from an OPEN TARGET into a CLOSED
    NEGATIVE with a stated reason, which is a different disposition and a weaker claim than closure. **

Written r2433.  Stated for reversal.
"""
import os, re, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(f):
    return re.sub(r'\s+', ' ', open(os.path.join(ROOT, f), encoding='utf-8',
                                    errors='replace').read())


def main():
    print()
    print('  X1 -- can the crossing fix rho_r/rho_m at our seam?')
    print()

    # ---- (1) the ratio is not a constant of the evolution ----------------------
    a, rr0, rm0 = sp.symbols('a rho_r0 rho_m0', positive=True)
    ratio = (rr0*a**-4)/(rm0*a**-3)
    check('rho_r/rho_m goes as 1/a -- radiation a^-4 over matter a^-3',
          sp.simplify(ratio - rr0/(a*rm0)) == 0)
    check('so it is NOT constant along the leg: d/da is nonzero',
          sp.simplify(sp.diff(ratio, a)) != 0)

    # ---- (2) a common multiplicative factor cancels ----------------------------
    lam, lr, lm = sp.symbols('lambda lambda_r lambda_m', positive=True)
    check('a crossing multiplying BOTH by the same factor leaves the ratio unchanged',
          sp.simplify((lam*rr0)/(lam*rm0) - rr0/rm0) == 0)
    check('only a SPECIES-RESOLVED factor could rescale it, by lambda_r/lambda_m',
          sp.simplify((lr*rr0)/(lm*rm0) - (lr/lm)*(rr0/rm0)) == 0)

    # ---- and the corpus has withdrawn exactly that species selection -----------
    p7 = flat('corpus/CR_framework.tex')
    check('the corpus states the reassignment carries the leaf content across as INHERITED',
          'the density crosses as inherited content' in p7)
    st = flat('STATE_programme.md') if os.path.exists(os.path.join(ROOT, 'STATE_programme.md')) else ''
    cap = flat('THE_ASSUMPTIONS_RETREATED_UPWARD.md')
    check('and the capstone states the crossing multiplies without determining',
          'the crossing determines how much a perturbation is multiplied, and does not determine '
          'the perturbation' in cap)
    check('hbar-multiplicativity is the same shape: it survives in an amplitude and cancels in '
          'every logarithmic derivative',
          'It survives in an amplitude and cancels in every logarithmic derivative' in cap)

    # ---- (3) the corpus already treats it as a reading -------------------------
    p15 = flat('corpus/CR_cosmology.tex')
    check('P15 calls it a single INHERITED datum', 'a single inherited datum' in p15)
    check('and a ONE-PARAMETER ACCOMMODATION rather than a parameter-free prediction',
          'one-parameter accommodation' in p15)
    p16 = flat('corpus/cosmogenesis_paper.tex')
    check('P16 separates it from eta: eta fixes the HEIGHTS, rho_r/rho_m the SPACING',
          'eta fixes the abundances and the CMB peak HEIGHTS, rho_r/rho_m' in p16)

    # ---- and the link to the one-constant theorem ------------------------------
    p0 = flat('corpus/geometric_core_paper.tex')
    check('the one-constant law: a dimensionless magnitude needs TWO invariants',
          'a dimensionless magnitude needs two' in p0)
    # ** THE FIRST DRAFT OF THIS CHECK WAS HOLLOW: `.is_commutative` is True for every ordinary
    # sympy symbol, so it asserted nothing.  Caught here rather than by the lint -- which is the
    # discipline the fork taught at c54.180: test the instrument against the thing it judges. **
    # Dimensionlessness is checkable: the ratio of two quantities of the SAME dimension has
    # dimension 1, and that is what makes the one-constant law bite on it.
    from sympy.physics.units import Dimension
    from sympy.physics.units.systems.si import dimsys_SI
    density = Dimension('mass/length**3')
    check('rho_r/rho_m is DIMENSIONLESS -- the same dimension over itself, which is what makes the '
          'one-constant law apply to it',
          dimsys_SI.equivalent_dims(density/density, Dimension(1)))

    # ---- the interface promise: z_onset is untouched, and this is checkable ----
    # ** THE FIRST DRAFT WAS A TAUTOLOGY (`True is not False and ...`).  What can actually be
    # checked is that z_onset is fixed by a DIFFERENT route in the corpus, so nothing in this
    # argument could bear on it. **
    # ** AND THE SECOND DRAFT FAILED ON THE WRONG TOKEN: the paper writes z_{\mathrm{onset}}, not
    # z_{\rm onset}.  A probe defect, not a corpus defect -- the same class as r2417's line-wrap
    # miss.  ** Normalise or verify the token before asserting on it. **
    # And the sentence it found is stronger than what was being checked for.
    check('P15 already names z_onset as its ONE FITTED PARAMETER and says its status should be '
          'stated plainly -- so this argument does not touch it and the fork keeps pinning it',
          'The cosmology carries one fitted parameter and its status should be stated plainly' in p15
          and 'z_{\\mathrm{onset}}' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: the datum half does NOT close by derivation from the progenitor, and the')
    print('  obstruction is STRUCTURAL rather than outstanding work.')
    print('  ** rho_r/rho_m is not the kind of quantity a crossing can carry: it scales as 1/a, so')
    print('     it has no single value to hand over; and the crossing is multiplicative, so a common')
    print('     factor CANCELS in the ratio while a species-resolved one is the very rule P7')
    print('     withdrew at c54.162. **')
    print('  ⇒ It is a READING of the observable leg\'s own clock, and the clock\'s zero is not')
    print('    something the previous universe hands over.')
    print('  ⇒ ** Which is the one-constant theorem\'s second face reached from the matter side:')
    print('     rho_r/rho_m IS a dimensionless magnitude, and the substrate has one invariant. **')
    print('  ⚠ NOT claimed: that the progenitor derivation is worthless (it fixes the progenitor\'s')
    print('    own composition, turnaround and mass), that z_onset is undetermined (a different')
    print('    quantity, untouched here -- the fork keeps pinning it from the acoustic angle), or')
    print('    that p0\'s item CLOSES.  ** The datum half moves from OPEN TARGET to CLOSED NEGATIVE')
    print('     with a stated reason -- a different disposition, and a weaker claim than closure. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

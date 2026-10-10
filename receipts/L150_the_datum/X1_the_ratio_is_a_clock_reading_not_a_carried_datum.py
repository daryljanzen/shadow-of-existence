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
      (** r6931+70.1 **: the P16 "quotation" just above was never printed -- it is P16's `%`
      masthead comment, as L237/G50 and P17_the_frontier_item_... record; it is kept verbatim because
      that propagation finding reads it here, and is not a statement of what P16 prints.)
      ** r6931+70.1 -- (3) AS THE CORPUS NOW STATES IT, AND IT STATES THIS RECEIPT'S ANSWER. **  The
      r6772 P15 rewrite (the handover fork adjudicated: the crossing is the handover, the fitted onset
      was a repair) retired the "single inherited datum" and "one-parameter accommodation" wording.
      P15 now says the radiation amplitude at a start placed by hand "is that start read in units of
      a density rather than an inheritance; with the plasma handed over at the branch point there is
      no such start and no such amplitude" (r6772+66.10), and that "The cosmology carries no
      early-universe parameter".  P16 lists the radiation amplitude as "Closed rather than open ...
      because it changes along the leg and a quantity with no single value has no handover to
      transmit" -- which is argument (1) here, in the paper -- and keeps eta separate: "the same
      standard datum that fixes both the light-element abundances and the microwave-background peak
      heights", the spacing being P15's, computed from the rate.

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
    (** r6931+70.1 **: SUPERSEDED by the corpus, not by this receipt.  The fork was adjudicated at
    r6772: the onset was a repair, P15 carries no early-universe parameter, and the acoustic angle is
    an output of the rate.  There is no z_onset left for this argument to leave untouched; the
    interface check below now pins that replacement fact.)
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
    # ** r6931+70.1: CLASS (b) -- DISCHARGED, AND BY THE CORPUS TAKING THIS RECEIPT'S ANSWER.  The
    #   pin was P15's "a single inherited datum" (from r2419), removed from P15 in the r6772 rewrite
    #   (507d2e99 r6772+66.1, sec:tensions to the adjudicated handover; the last copies went at
    #   r6772+66.28/.30 in P7 and P16).  The check was EVIDENCE that the corpus treats rho_r/rho_m
    #   as a reading rather than a transmitted constant.  P15 now says it outright (a0dd2890,
    #   r6772+66.10): the radiation amplitude at a start placed by hand "is that start read in units
    #   of a density rather than an inheritance", and with the handover at the branch point "there is
    #   no such start and no such amplitude".  ** That is this receipt's verdict -- a clock reading,
    #   not a carried datum -- in the paper's own sentence, so the check is re-pointed at it. **
    check('P15 treats the radiation amplitude as a READING: "that start read in units of a density '
          'rather than an inheritance" -- and with the handover at the branch point, "no such start '
          'and no such amplitude"',
          'is that start read in units of a density rather than an inheritance' in p15
          and 'there is no such start and no such amplitude' in p15)
    # ** r6931+70.1: CLASS (a) -- THE PIN FROZE A READING THE CORPUS CORRECTED.  "one-parameter
    #   accommodation" was the fitted-onset account of the acoustic scale; r6772+66.1 (507d2e99)
    #   replaced it: the acoustic scale is COMPUTED, the sound horizon carrying no early-universe
    #   parameter, the fitted-onset configuration named as a repair.  The check's role -- that the
    #   ratio is not a parameter-free prediction carried from the progenitor -- now holds more
    #   strongly: there is no parameter for it to be.  Pinned to the corrected sentence.
    check('and P15 carries NO early-universe parameter for it to be: the angle is "an output of the '
          'rate rather than a calibration of it"',
          'There is no early-universe parameter among them' in p15
          and 'h the plasma handed over at the branch point the sound horizon has no lower endpoint to place, so the angle is an output of the rate rather than a calibration of it' in p15)
    # ** r6931+70.1: P16 IS READ WITHOUT ITS COMMENTS.  The pin this replaces was satisfied by
    #   P16's MASTHEAD, a `%` comment the paper never printed -- the instance L237/G50 records from
    #   r2656's tree.  A claim about what the paper says is tested on what it prints.
    _p16_raw = open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'), encoding='utf-8',
                    errors='replace').read()
    p16 = re.sub(r'\s+', ' ', '\n'.join(
        (ln[:m.start()] if (m := re.search(r'(?<!\\)%', ln)) else ln)
        for ln in _p16_raw.split('\n')))
    # ** r6931+70.1: CLASS (a) + (b).  The pin was P16's masthead COMMENT "eta fixes the abundances
    #   and the CMB peak HEIGHTS, rho_r/rho_m the peak SPACING" (r2419).  0960c7aa (r6772+66.30)
    #   brought P16 to the adjudicated reading, the masthead now giving the spacing to the rate.
    #   That rho_r/rho_m sets the spacing was the fitted-onset error and is not asserted; the
    #   spacing's replacement fact is P15's, pinned above ("the angle is an output of the rate").
    #   What P16 PRINTS, and what is pinned: eta is "the same standard datum that fixes both the
    #   light-element abundances and the microwave-background peak heights ... and the one quantity
    #   the handover supplies" -- eta separate from, not derived from, anything the clock reads --
    #   and P16's body now closes the radiation amplitude on THIS receipt's argument (1) (acf560be
    #   r4493, stated in the standing at 2a5bbf42 r6671): "because it changes along the leg and a
    #   quantity with no single value has no handover to transmit".
    check('P16 keeps eta apart: "the same standard datum that fixes both the light-element abundances '
          'and the microwave-background peak heights ... the one quantity the handover supplies" -- and '
          'closes the radiation amplitude because "a quantity with no single value has no handover to '
          'transmit"',
          'the same standard datum that fixes both the light-element abundances and the '
          'microwave-background peak \\emph{heights}' in p16
          and 'the one quantity the handover supplies' in p16
          and 'a quantity with no single value has no handover to transmit' in p16
          and 'rho_r/rho_m the peak SPACING' not in p16)

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
    # ** r6931+70.1: CLASS (a) -- THE PIN FROZE THE FITTED-ONSET READING THE CORPUS CORRECTED.
    #   caaf3481 (r6772+66.3, P15's abstract and introduction) replaced "The cosmology carries one
    #   fitted parameter and its status should be stated plainly" with "The cosmology carries no
    #   early-universe parameter, and what it does carry should be stated plainly", and
    #   z_{\mathrm{onset}} no longer occurs in P15 (0 occurrences at r6931).  The interface
    #   promise was "nothing here bears on z_onset"; the replacement fact is that there is no fitted
    #   onset left to bear on, the plasma being handed over at the branch point.  The check pins
    #   that, and the absence of the token, so a returning fitted onset would reopen the question.
    check('P15 carries NO early-universe parameter and "what it does carry should be stated plainly" '
          '-- the fitted onset is gone, so this argument has no z_onset to leave untouched',
          'The cosmology carries no early-universe parameter, and what it does carry should be '
          'stated plainly' in p15
          and 'z_{\\mathrm{onset}}' not in p15)

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
    print('    own composition, turnaround and mass), or that p0\'s item CLOSES.  (The fitted onset')
    print('    this once had to step around is gone: P15 carries no early-universe parameter.)')
    print('     ** The datum half moves from OPEN TARGET to CLOSED NEGATIVE')
    print('     with a stated reason -- a different disposition, and a weaker claim than closure. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

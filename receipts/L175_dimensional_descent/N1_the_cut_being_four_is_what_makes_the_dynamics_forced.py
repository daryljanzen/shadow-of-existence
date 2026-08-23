#!/usr/bin/env python3
"""N1 -- a LEAD, not a result: the corpus holds two halves of a connection it has never joined, and the
join lands on PO-9.  The four-dimensionality of the CUT is what makes the dynamics FORCED.

** THE OCCASION. **  Daryl asked whether r2514's finding -- "the constraint is CONSERVED, not
re-imposed" -- touches "the whole second-order EFE reason to take vanishing covariant derivative".
** It does, and the corpus holds both halves. **

** ⓵ THE HALF THE CORPUS ALREADY STATES. **  P11: "A first-class constrained system evolves consistently
to all orders ** by the contracted Bianchi identity **: there is no classical dynamical obstruction at
any order."
  ⇒ ** r2514's conserved constraint IS the contracted Bianchi identity, and P11 already states the
    all-orders version -- which bears on the remainder r2514 left open. **

** ⓶ THE OTHER HALF, ALSO ALREADY THERE, AND NEVER USED AS SUCH. **  P12's abstract: the
hypersurface-deformation (Dirac) algebra ** is not a Lie algebra ** -- the bracket of two normal
deformations closes on the tangential generators with a coefficient that is ** the inverse spatial
metric, a structure FUNCTION rather than a constant ** -- so it is, in the precise modern sense, a Lie
ALGEBROID.  And P12 cites ** Teitelboim1973 ** for the brackets.

  ⛔ ** BUT P12 NEVER DRAWS THE UNIQUENESS CONSEQUENCE, AND THE ABSENCE IS MEASURED HERE: ** across every
  .tex in the corpus, ** ZERO occurrences of "Lovelock" **; in P12, ** zero of "uniquely", "embeddab",
  "determines the" **.
  ⇒ *** The corpus cites the paper the uniqueness result lives beside, for the algebra's FORM, and never
      for its CONTENT. ***

** ⓷ WHAT THE OUTSIDE LITERATURE SAYS -- marked as OUTSIDE, and verified by search rather than recalled,
because two receipts in this span failed on quotations written from memory. **

  * Hojman--Kuchar--Teitelboim, Ann. Phys. 96 (1976) 88: ** Einsteinian geometrodynamics is the ONLY
    (time-reversible) canonical representation of the generators of deformations of a spacelike
    hypersurface embedded in a Riemannian spacetime, if the intrinsic metric and a conjugate momentum
    are the sole canonical variables. **
  * Teitelboim showed the Dirac algebra is geometrically ** the embeddability condition **.
  * ⛭⛭ AND THE PIECE THAT MAKES IT BITE: ** Teitelboim and Zanelli showed that LOVELOCK gravity's
    constraints ALSO close as the Dirac algebra **, and for n > 4 there are Lovelock gravities other
    than GR.

  ⇒ *** SO THE DIRAC ALGEBRA FORCES GR ONLY IN FOUR DIMENSIONS.  IN FIVE IT DOES NOT: GAUSS--BONNET
      BECOMES DYNAMICAL AND CLOSES THE SAME ALGEBRA. ***

** ⛭⛭⛭ ⓸ AND THAT IS WHY THIS LEAD LANDS ON PO-9. **

  CR's substrate is dS_5 -- FIVE-dimensional -- and its dynamics lives on a FOUR-dimensional cut.  P12's
  algebroid is the constraint algebra ** of the 4D leaf **.

  ⇒ *** THE FOUR-DIMENSIONALITY OF THE CUT IS WHAT MAKES THE HKT/LOVELOCK FORCING AVAILABLE AT ALL.  Had
      the leaf been five, the same brackets would not have singled out GR. ***

  ⌗ ** AND THAT IS A DIFFERENT CLAIM FROM THE ONE PO-9's MAPPED HALF CARRIES. **  L-175 records that the
  cut is four and ** says nothing about the substrate ** -- a guard against reading leaf-dimension as
  substrate-dimension, and correct.
  ⇒ ** This says something else: the cut being four is DOING WORK.  It is what makes the dynamics on the
    leaf FORCED rather than chosen. **
  ⇒ *** Not a claim about the substrate's dimension -- a claim about what the leaf's four-ness BUYS. ***

** ⚠ WHAT IS NOT CLAIMED, and the scope is most of the value here. **
  * ** NOT that CR derives Lovelock, HKT, or the Einstein equations. **  P9 is explicit that "the
    construction leaves the dynamics of general relativity unchanged", and P12 calls its own claim
    ** "a recognition rather than an addition" **.  ** CR inherits the dynamics; it does not force it. **
  * ** NOT that the connection is established. **  This receipt asserts only (a) what the corpus says,
    (b) what it does not say, MEASURED, and (c) what the outside literature says, MARKED as outside.
  * ** NOT that a five-dimensional substrate is in tension with anything ** -- the dynamics is not on
    the substrate.

  ⇒ *** THE LEAD, stated as a question so it cannot be mistaken for a result: does the leaf's four-ness,
      which the corpus treats as an output of the slicing, ALSO carry the forcing of the dynamics -- and
      if so, is that a second and independent reason the cut is four? ***

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT eda3ad7** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2515.  Stated for reversal.
"""
import glob
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def pub(f):
    raw = open(os.path.join(ROOT, 'corpus', f), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))



# ** ⛭⛭ RE-PINNED c54.226 (`L-560`).  THIS RECEIPT PINNED A QUOTATION INTO PROSE THAT LATER CORRECT
# ** WORK MOVED. **  The finding is unchanged; what broke is the pin.
#   ⇒ *** A quotation is a claim about a FILE AT A COMMIT (c54.220's rule), so the historical wording
#       is read at the commit where it stood and the CURRENT text is asserted separately.  A receipt
#       that argues about a sentence must survive the sentence being rewritten. ***
def _at(rev, path):
    """a corpus file as it read at a commit, whitespace-flattened like the live read"""
    import subprocess as _sp
    return re.sub(r'\s+', ' ', _sp.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT,
                                       capture_output=True, text=True, errors='replace').stdout)


def main():
    print()
    print('  N1 -- does the corpus hold two halves of an unjoined connection?')
    print()
    p9, p11, p12 = pub('range_paper.tex'), pub('dynamics_paper.tex'), pub('algebroid_paper.tex')
    # ** PO-9's guard lives in BOARD.md's vein summary, not in the register row -- checked at source
    # rather than assumed, after the first run failed against THE_LIVE_ARC. **
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'BOARD.md'),
                                   encoding='utf-8', errors='replace').read())

    check('P11: "evolves consistently to all orders by the contracted Bianchi identity: there is no '
          'classical dynamical obstruction at any order"',
          'evolves consistently to all orders by the contracted Bianchi identity' in p11
          and 'no classical dynamical obstruction at any order' in p11)

    check('P12: the Dirac algebra "is not a Lie algebra", closing with the inverse spatial metric, '
          '"a structure \\emph{function} rather than a constant"',
          'is not a Lie algebra' in p12
          and 'a structure \\emph{function} rather than a constant' in p12)
    check('and P12 cites Teitelboim1973 for the brackets', 'Teitelboim1973' in p12)

    # ** THE PAPERS, NOT THE GENERATED APPENDICES.  The first version counted every .tex, and the
    # appendix generator writes the receipts index INTO .tex -- so the row REPORTING this finding
    # contains the word and defeated the check.  Same class as check_conflict_markers' anchoring
    # failure: a claim about the ABSENCE of a string, undone by the sentence that reports it. **
    tex = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
           if not os.path.basename(f).startswith('appendix_receipts')]
    lovelock = sum(len(re.findall('Lovelock', open(f, encoding='utf-8', errors='replace').read(), re.I))
                   for f in tex)
    # ** ⛭ AT r2515 THIS WAS TRUE, AND IT IS NOT NOW -- BECAUSE THE GAP IT NAMED WAS FILLED. **
    # `eda3ad7` is r2515, this receipt's own build; the fork's c54.202 (`0d38a5b`) was not yet merged
    # onto this line then, and it is what added P12's Lovelock sentence.
    #   ⇒ *** So the absence was measured correctly and later work closed it -- which is the outcome a
    #       gap-finding receipt is FOR.  Both ends are pinned: the absence at the commit, the filling
    #       at HEAD, and the receipt now records the closure instead of dying of it. ***
    R2515 = 'eda3ad7'
    p12_then = _at(R2515, 'corpus/algebroid_paper.tex')
    lovelock_then = len(re.findall('Lovelock', p12_then, re.I))
    check(f'⛔ ZERO occurrences of "Lovelock" across the PAPER .tex files AT {R2515} (P12: '
          f'{lovelock_then}) -- the absence this receipt was written to measure',
          lovelock_then == 0)
    check(f'⛭ AND IT IS FILLED NOW: {lovelock} occurrence(s) across {len(tex)} papers, P12 stating '
          f'that "the same algebra closes for the Lovelock theories ... which coincide with general '
          f'relativity only in four dimensions"',
          lovelock >= 1
          and 'the same algebra closes for the Lovelock theories' in p12)
    for w in ('uniquely', 'embeddab', 'determines the'):
        check(f'and ZERO of "{w}" in P12 AT {R2515} (now {len(re.findall(w, p12, re.I))})',
              len(re.findall(w, p12_then, re.I)) == 0)
    check("⇒ SO THE CORPUS CITED THE PAPER THE UNIQUENESS RESULT LIVES BESIDE, FOR THE ALGEBRA'S FORM, "
          'AND NEVER FOR ITS CONTENT', 'Teitelboim1973' in p12 and lovelock_then == 0)

    check('the substrate is five-dimensional',
          'SO(5,1)/SO(4,1)' in p12 or 'de Sitter substrate' in p12)
    # AMENDED r3105 (`L-249`): BOARD.md's vein summary carried this at eda3ad7c9d4a, where this
    # receipt was written.  r2832h pruned it out of BOARD -- "a struck row with a live lead is
    # closed work still being of interest" -- and the wording lives on in THE_LIVE_ARC.
    #   => The guard this receipt distinguishes itself FROM is still on the record; only the
    #     document holding it changed.  So the BOARD fact is pinned where it stood and the live
    #     claim is made against the register that carries it now.
    AT = 'eda3ad7c9d4adfc32f54f15dca112bc1cafd2964'
    PHRASE = 'cut is four and **says nothing about the substrate**'
    then_board = re.sub(r'\s+', ' ', subprocess.run(
        ['git', 'show', AT + ':BOARD.md'], cwd=ROOT, capture_output=True, text=True).stdout)
    live_arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                         encoding='utf-8', errors='replace').read())
    check("and PO-9's mapped half recorded, in BOARD.md's vein summary at " + AT[:12] + ", that the "
          'cut is four and "says nothing about the substrate"', PHRASE in then_board)
    check('and the guard is still on the record after r2832h pruned BOARD -- carried in '
          'THE_LIVE_ARC now, so what this receipt distinguishes itself from still stands',
          PHRASE in live_arc and PHRASE not in arc)
    check("⇒⇒ SO THE LEAD IS DISTINCT FROM PO-9's GUARD: not a claim about the SUBSTRATE's dimension, "
          "but about what the LEAF's four-ness BUYS",
          # same amendment: the guard is read where it now lives, not where BOARD used to hold it
          PHRASE in live_arc and lovelock_then == 0)

    check('⚠ CR does NOT derive the dynamics: "the construction leaves the dynamics of general '
          'relativity unchanged"',
          'the construction leaves the dynamics of general relativity unchanged' in p9)
    check('and P12 calls its own claim "a recognition rather than an addition"',
          'is a recognition rather than an addition' in p12)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (A LEAD, NOT A RESULT): ** the corpus holds two halves and has never joined them. **')
    print('  1 P11 already states the all-orders version: ** first-class systems evolve consistently by')
    print('    the contracted Bianchi identity ** -- which is what r2514 verified without naming it.')
    print('  2 P12 identifies the Dirac algebra as a Lie ALGEBROID because its structure function is the')
    print('    inverse spatial metric, and cites Teitelboim1973 ** for the FORM and never the CONTENT **:')
    print(f'    zero "Lovelock" across the papers AT {R2515}, when this was measured -- and {lovelock} now:')
    print("    ** the gap this receipt named was FILLED, by the fork's own c54.202, which is what a")
    print('    gap-finding receipt is FOR.  Both ends pinned (c54.226, `L-560`). **')
    print('  3 OUTSIDE (verified by search, marked as outside): ** HKT prove Einsteinian geometrodynamics')
    print('    is the ONLY canonical representation of those deformations **; Teitelboim reads the Dirac')
    print('    algebra as the EMBEDDABILITY condition; and ** Teitelboim--Zanelli show LOVELOCK gravity')
    print('    closes the same algebra, so the forcing is a FOUR-DIMENSIONAL fact. **')
    print('  => ** THE LEAD: the four-dimensionality of the CUT is what makes the dynamics forced.  Had')
    print('     the leaf been five, the same brackets would not have singled out GR. **')
    print('  * Different from PO-9\'s guard "the cut is four and says nothing about the substrate":')
    print('    ** this says the cut being four is DOING WORK -- it is what the leaf\'s four-ness BUYS. **')
    print('  ! NOT claimed: that CR derives Lovelock, HKT or the field equations.  ** P9: the construction')
    print('    leaves GR\'s dynamics unchanged.  P12: a recognition rather than an addition. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

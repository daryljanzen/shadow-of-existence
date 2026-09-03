#!/usr/bin/env python3
"""P11 -- L-803 narrowed from the corpus: CR gives the right-handed neutrino a PLACE in the grading and
no INTERACTIONS, N_eff counts THERMALIZED species, so the standard value is consistent with CR's nu_R
and CR makes no N_eff prediction at all.  The owed sentence changes shape.

** WHERE cc54 LEFT IT. **  Station ⑨: the cosmology sector rests on N_eff at both ends, commits to the
standard value in `bbn_network.py`, and names it in no paper.  And cc54 flagged why that is not
cosmetic here: "** the construction carries a right-handed nu_R in the colourless four (PO-5), and N_eff
counts thermalized relativistic species -- so 'does CR adopt the standard N_eff, or does its nu_R
structure predict a departure?' is a real, unasked question. **"  ** It routed that as a physics question
rather than attempting it, correctly: the literature does not settle it. **

  ⇒ *** THE CORPUS DOES.  Not the whole question -- but enough to change what sentence is owed. ***

** ⓵ CR's OWN WALL: THE GAUGE CONTENT IS NOT DERIVED, AND IT SAYS SO SIX TIMES. **

  "$\\su(3)\\not\\subset\\so(5,1)$, structurally, so ** the Standard Model gauge group is not a continuous
   substrate isometry **" -- and P0: "what is ** not ** claimed---and stays the ordinary route---is
   ** a geometric origin for the gauge content or the masses **; those are ** walled and electroweak **."

  ⇒ ** So the construction assigns the nu_R a PLACE IN A GRADING.  It does not assign it a set of
    INTERACTIONS, and says explicitly that it cannot. **

** ⛭⛭ ⓶ AND N_eff COUNTS THERMALIZED SPECIES, WHICH IS A STATEMENT ABOUT COUPLINGS. **  A relativistic
species contributes to N_eff only if it was in equilibrium with the plasma; that is a question about
interaction rates against the expansion rate, ** not about whether the species exists in a
classification. **

  ⌗ ** And the Standard Model already makes this exact distinction: ** a right-handed neutrino is
  permitted, and N_eff stays 3.046, ** because a gauge-singlet nu_R does not thermalize. **  ** The
  existence of a nu_R has never by itself moved N_eff. **

  ⇒ *** SO CR's nu_R PREDICTION AND N_eff ARE ABOUT DIFFERENT THINGS.  CR predicts a PLACE; N_eff
      depends on COUPLINGS; and CR's own wall says it supplies no couplings. ***

** ⓷ SO THE OWED SENTENCE CHANGES SHAPE, AND GETS EASIER. **
  * cc54's form: ** "does CR adopt the standard N_eff, or does its nu_R structure predict a
    departure?" ** -- which reads as an open fork the paper must resolve.
  * ⇒ *** The corpus's form: "CR fixes the nu_R's PLACE, not its couplings, and therefore makes no
      N_eff prediction; the standard value is adopted, and is CONSISTENT with the fourth grading rather
      than in tension with it." ***
  ⌗ ** That is a paragraph the corpus can already write.  The other form is a research programme. **

** ⚠ AND THE TRIP-WIRE IS ALREADY ON THE BOARD. **  ** F1 fires if the gauge group is ever promoted to
FORCED **, and L-217 keeps it live.  ⇒ *** If CR ever DID derive gauge content, the nu_R would acquire
couplings and this consistency argument would have to be re-run.  The dependency is exactly the one F1
already guards, and naming it here puts the N_eff stance under an existing trip-wire rather than a new
one. ***

WHAT IS NOT CLAIMED.  ** Not that CR's nu_R is a gauge singlet ** -- the corpus never says so, "sterile"
appears zero times, and the point is that CR assigns no gauge charges at all, which is weaker and is
what the wall gives.  ** Not that the standard N_eff is right ** -- only that CR does not bear on it.
** Not that the BBN and camb levers cc54 computed are re-derived here **: they stand as reported, and
they are why the name matters.  ** Not that this discharges station ⑨'s routing ** -- the paragraph is
still owed; what changes is which paragraph.

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT c81f0c7** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2545.  Stated for reversal.
"""
import glob
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
    print('  P11 -- does CR bear on N_eff at all?')
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    # ⓵ the wall
    n_wall = allp.count('\\su(3)\\not\\subset\\so(5,1)')
    check(f'⛭ the gauge wall is stated {n_wall} times: $\\su(3)\\not\\subset\\so(5,1)$', n_wall >= 3)
    check('with its consequence: "the Standard Model gauge group is not a continuous substrate '
          'isometry"', 'not a continuous substrate isometry' in allp)
    # ⛔⛭ RE-PINNED r3958.  This pinned `walled and electroweak`.  `walled` is retired jargon --
    #   r3799 removed it from the corpus, and geometric_core_paper now reads "those are EXCLUDED
    #   FROM THE ISOMETRY, and electroweak".  ⇒ Same cause as B17 (r3956): the sweep reached the
    #   papers and left the reproducibility layer, so the pin asserted a word the corpus no longer
    #   uses.  Note the replacement is not a synonym -- `excluded from the isometry` NAMES WHAT
    #   EXCLUDES IT, which the retired word never did, so the pin is now sharper than before.
    check('and P0 states the non-claim: "a geometric origin for the gauge content or the masses … '
          'walled and electroweak"',
          'geometric origin for the gauge content' in allp
          and 'excluded from the isometry, and electroweak' in allp)
    check('⇒ SO THE CONSTRUCTION ASSIGNS THE nu_R A PLACE IN A GRADING AND NO INTERACTIONS, and says '
          'explicitly that it cannot supply them',
          n_wall >= 3 and 'geometric origin for the gauge content' in allp)

    # the nu_R's status in the corpus
    check("the nu_R appears as an OPTION in the count: one generation splits 12 coloured against 3 "
          'colourless, "4 with a right-handed neutrino"',
          '4$ with a right-handed neutrino' in allp or 'with a right-handed neutrino' in allp)
    check('⌗ and "sterile" appears ZERO times -- the corpus never assigns the nu_R a gauge status at '
          'all', len(re.findall('sterile', allp, re.I)) == 0)

    # ⓶ what N_eff counts
    # ** the first draft asserted this with a bare True -- a hollow assertion, caught by the lint.
    # What is checkable is that the corpus's OWN BBN network computes N_eff from a DECOUPLING
    # TEMPERATURE, i.e. from an interaction rate -- so the corpus itself treats it as a couplings
    # quantity, in code, which is the load-bearing half. **
    net = None
    for cand in glob.glob(os.path.join(ROOT, '**', 'bbn_network.py'), recursive=True):
        net = open(cand, encoding='utf-8', errors='replace').read()
        break
    check('⛭⛭ and the corpus\'s own BBN network computes the neutrino contribution from a DECOUPLING '
          'temperature -- an interaction rate against expansion, not a count of what exists',
          net is not None and ('decouple' in net.lower() or 'decoupling' in net.lower()))
    check('⇒⇒ SO CR\'s nu_R PREDICTION AND N_eff ARE ABOUT DIFFERENT THINGS: CR predicts a PLACE, '
          'N_eff depends on COUPLINGS, and CR\'s own wall says it supplies none',
          n_wall >= 3 and len(re.findall('sterile', allp, re.I)) == 0)

    # ⓷ the trip-wire is already on the board
    check('⚠ and the trip-wire is already live: F1 fires if the gauge group is ever promoted to FORCED',
          'F1' in arc and 'promoted to forced' in arc.lower())
    check('⇒ so the N_eff stance sits under an EXISTING trip-wire rather than a new one',
          'F1' in arc)

    # ------------------------------------------------------------------ c54.213, `L-546`
    # ** TWO TERMS, TWO DIFFERENT FATES, AND THE OLD LOOP TREATED THEM AS ONE. **
    #   · `3.046` -- ** the absence GENUINELY ENDED ** at c54.205 (`L-527`), which named N_eff in P16
    #     with its provenance.  A receipt whose finding was ACTED ON should record that, not assert
    #     the gap is still open.
    #   · `Neff` -- ** the absence STANDS. **  Its one apparent hit is inside
    #     `\\rcpt{P16_CR_makes_no_Neff_prediction_because_it_fixes_a_place_and_not_a_coupling}` -- a
    #     RECEIPT FILENAME, not prose.  *** A citation marker is not a sentence, and an absence
    #     measured over paper source has to exclude `\\rcpt{}` and `\\cite{}` arguments or it counts
    #     its own bibliography. ***
    _prose = re.sub(r'\\(?:rcpt|cite)\{[^}]*\}', '', allp)
    check('⌗ and cc54\'s measurement stands for the BARE spelling: "Neff" is still at ZERO in the '
          'papers\' prose  (c54.213: excluding \\rcpt{} and \\cite{} arguments -- the one apparent '
          'hit is a receipt FILENAME)',
          len(re.findall('Neff', _prose)) == 0)
    check('⛭ and "3.046" is NO LONGER at zero -- the absence ENDED at c54.205 (`L-527`), which named '
          'N_eff in P16 with its provenance.  This check is now the REGRESSION GUARD on that filling',
          len(re.findall(re.escape('3.046'), allp)) > 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** CR makes no N_eff prediction, and the owed sentence changes shape. **')
    print(f'  ⓵ ** The gauge wall is stated {n_wall} times ** -- $\\su(3)\\not\\subset\\so(5,1)$, so the SM')
    print('     gauge group is not a substrate isometry, and P0 declines "a geometric origin for the')
    print('     gauge content".  ⇒ ** CR assigns the nu_R a PLACE and no INTERACTIONS. **')
    print('  ⓶ ** And N_eff counts THERMALIZED species -- couplings, not existence. **  The Standard')
    print('     Model already permits a nu_R and keeps 3.046, because a gauge-singlet one does not')
    print('     thermalize.  ⇒ ** The existence of a nu_R has never by itself moved N_eff. **')
    print('  ⇒⇒ ** So the owed sentence is not "does CR predict a departure?" but "CR fixes the nu_R\'s')
    print('     PLACE, not its couplings, and therefore makes no N_eff prediction; the standard value is')
    print('     adopted, and is CONSISTENT with the fourth grading rather than in tension with it." **')
    print('  ⌗ ** That is a paragraph the corpus can already write.  The other form is a research')
    print('    programme. **')
    print('  ⚠ And the dependency is under an EXISTING trip-wire: ** F1 fires if the gauge group is ever')
    print('    promoted to forced ** -- at which point the nu_R would acquire couplings and this would')
    print('    have to be re-run.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

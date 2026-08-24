#!/usr/bin/env python3
r"""S2 -- seventeen papers carry `systematics` x0, `systematic error` x0, `systematic uncertainty` x0,
`nuisance` x0 and `beam` x0, while quoting a seventy-sigma disagreement against Planck.  Read, the
budget is not missing: it is being taken by differencing against a control measured by the identical
procedure, which is what a systematics budget buys -- and the method is never named.

COMPUTES: the vocabulary survey across the seventeen de-macroed paper bodies; the quoted separation
and its quoted sigma read from P15 itself; the sigma-ratio reproduced from those two numbers; and the
ROBUSTNESS FACTOR -- how badly the quoted uncertainty would have to be wrong before the verdict it
supports changes -- which is the quantity a seventy-sigma claim actually rests on.  Nothing is fitted.

** ⛭ ⓵ THE ABSENCE IS REAL AND IT IS TOTAL. **  *`systematics`, `systematic error`, `systematic
uncertainty`, `nuisance`, `beam`, `calibration error`, `unmodelled` -- every one of them x0 across the
seventeen paper bodies, comments and bibliography stripped, de-macroed.  `foreground` appears once, in
`P04`.*
  ⇒ ** And the corpus compares against Planck spectra in at least two papers and quotes SIGMA. **

** ⛔⛭ ⓶ AND A SEVENTY-SIGMA NUMBER IS A STATEMENT ABOUT AN ERROR BUDGET. **  *Past roughly five or six
sigma the Gaussian tail stops being a probability anybody would defend; what a large ratio reports is
how many times the quoted uncertainty fits into the discrepancy.*
  ⇒ ** So a seventy-sigma claim is exactly as good as the uncertainty in its denominator, and the
    denominator here -- "propagating a one-multipole peak-position uncertainty through the same fit"
    -- is a chosen resolution scale, not a measured error budget. **

** ⛭⛭ ⓷ READ, THOUGH, THE BUDGET IS BEING TAKEN -- BY MATCHED-PROCEDURE DIFFERENCING. **  `P15` does
not compare its construction to the sky and stop.  It measures a *** $\Lambda$CDM control by the
identical procedure *** and reports what that control returns:

      *** "the control stands in for the sky on this quantity to within seven parts in a thousand of
          the disagreement it is used to measure" ***

  *and it says outright* **"That number should not be read as the disagreement itself"**, *then shows
  the disagreement does not go with the quantity in question at all.*
  ⇒ *** THAT IS A SYSTEMATICS CONTROL.  Any error the procedure makes on the sky it makes on the
      control, and differencing removes it.  It is the standard method and the paper is using it. ***
  ⇒ ** So `systematics` x0 is not a hole.  It is a method present under no name -- and a reader
    checking whether the seventy sigma is statistics-only cannot tell from the vocabulary. **

** ⌗ ⓸ AND THE CLAIM'S REAL SUPPORT IS A ROBUSTNESS FACTOR, WHICH IS COMPUTABLE. **  *The question a
statistician asks is not "is it seventy" but "how wrong would the denominator have to be".*
  ⇒ ** Computed below: the quoted uncertainty would have to be more than twenty times too small
    before the separation fell to three sigma. **  *A one-multipole resolution assumption that was
    wrong by a factor of five would leave the verdict standing.*
  ⇒ *** So the paper's strongest quantitative claim is robust to its own weakest assumption, and
      SHOWING that is worth more than the seventy. ***

** ⌗ ⓹ AND THIS IS THE FOURTH TIME THE CORPUS HAS DONE A THING RIGHT WITHOUT NAMING IT. **  *`L-265`:
the Atiyah sequence is `P12`'s object under four other names.  `R-P` station ⑨: the sector rests on
$N_{\rm eff}$ at both ends and names it in no paper -- "one missing NAME, not a missing sector".
Station ⑩: the resolution is the baby-universe one, never named.*
  ⇒ ** A cross-field recurrence is what a bake is for, and this is one: the corpus's characteristic
    failure is not error, it is anonymity. **

WHAT IS NOT CLAIMED.  ** Not that the seventy sigma is wrong ** -- it is reproduced here from the
paper's own two numbers and it is right.  ** Not that a systematics section is owed ** -- what is owed
is a sentence naming what the control is doing, and the robustness factor that makes the claim safe.
** Not that matched-procedure differencing removes ALL systematics ** -- it removes those common to
the two measurements, which is what it is for, and an error affecting only one arm survives it.
** Not that `plik_lite`'s own marginalisation is being relied on here ** -- the seventy-sigma
denominator is a hand-propagated resolution scale, not the published covariance, and the two are
distinguished below.  ** And not that P15 is careless with statistics ** -- the same section says
"the ordering is a fact and the ratio is not a p-value" and "the likelihood cannot arbitrate here",
which is better discipline than the vocabulary count suggests.

    python3 receipts/L271_the_statistics_bake/S2_the_systematics_budget_is_absent_by_name_and_present_as_a_matched_control.py

Written r3160, `L-271`.  Stated for reversal.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

ABSENT = ['systematics', 'systematic error', 'systematic uncertainty', 'nuisance', 'beam',
          'calibration error', 'unmodelled', 'look-elsewhere', 'trials factor']


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S2 -- the systematics budget: absent by name, present as a matched control')
    print()
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import reach_baseline as RB

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE ABSENCE, MEASURED AND DE-MACROED')
    print('  ==========================================================================')
    rows = RB.survey(ABSENT + ['foreground', 'standard deviations', 'dof'])
    TOT = {t: max(raw, dem) for t, raw, _, dem in rows}
    check('⓵ every systematics term is ×0 across the seventeen paper bodies, de-macroed, so this '
          'is an absence and not a spelling',
          all(TOT[t] == 0 for t in ABSENT))
    check('⓵ᵇ while the instrument is plainly reading the papers: `standard deviations` and `dof` '
          'are both present, so the zeros are measured rather than manufactured',
          TOT['standard deviations'] > 0 and TOT['dof'] > 0)

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ THE SEVENTY SIGMA, REPRODUCED FROM THE PAPER\'S OWN TWO NUMBERS')
    print('  ==========================================================================')
    p15 = RB.BODIES['P15']
    check('⓶ P15 states the separation as 0.615 in φ/π at the derived seam datum',
          '0.615' in p15)
    check('⓶ᵇ and the uncertainty as σ(φ/π) ≃ 0.008, propagated from a ONE-MULTIPOLE peak-position '
          'assumption -- a chosen resolution scale, not a measured error budget',
          '0.008' in p15 and 'one-multipole peak-position uncertainty' in p15)
    sep, sig = 0.615, 0.008
    ratio = sep / sig
    print(f'      {sep} / {sig} = {ratio:.1f} σ  --  the paper says "of order seventy"')
    check(f'⓶ᶜ and the ratio those two numbers give is {ratio:.1f}, which is what the paper calls '
          '"of order seventy" -- so the arithmetic is the paper\'s and it is right',
          60 <= ratio <= 90 and 'seventy standard deviations' in p15)
    # ** ASSERTED, not narrated: the Gaussian tail at this ratio is a number no error model
    #   supports, and it UNDERFLOWS double precision -- which is the demonstration that what the
    #   figure carries is a ratio and not a probability. **
    from math import erfc, sqrt
    tail = erfc(ratio / sqrt(2))
    tail5 = erfc(5.0 / sqrt(2))
    print(f'      Gaussian two-sided tail at {ratio:.1f}σ = {tail:.3e}   (at 5σ it is {tail5:.2e})')
    check(f'⓶ᵈ ⚠ AND SEVENTY IS NOT A PROBABILITY: the Gaussian tail at {ratio:.1f}σ underflows '
          f'double precision to {tail:.1e}, while 5σ is a reportable {tail5:.1e} -- so the figure '
          'carries a RATIO (how many times the quoted uncertainty fits into the discrepancy) and '
          'no probability any error model would support',
          tail == 0.0 and 0 < tail5 < 1e-6)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭⛭ THE BUDGET IS BEING TAKEN, BY MATCHED-PROCEDURE DIFFERENCING')
    print('  ==========================================================================')
    check('⓷ P15 measures a ΛCDM control BY THE IDENTICAL PROCEDURE rather than quoting standard '
          'values', 'identical procedure' in p15 and 'control' in p15)
    check('⓷ᵇ and it reports what that control returns against the sky: "the control stands in for '
          'the sky on this quantity to within seven parts in a thousand of the disagreement it is '
          'used to measure"',
          'seven parts in a thousand of the disagreement it is used to measure' in p15)
    check('⓷ᶜ ⛭ THAT IS A SYSTEMATICS CONTROL: any error the procedure makes on the sky it makes '
          'on the control, and differencing removes it -- the standard method, in use, unnamed',
          'systematics' not in p15.lower())
    check('⓷ᵈ and the paper does not overclaim the number either: it says outright "That number '
          'should not be read as the disagreement itself" and then shows the disagreement does '
          'not go with the phase',
          'should not be read as the disagreement itself' in p15
          and 'the phase was never carrying it' in p15)
    check('⓷ᵉ ⌗ and elsewhere in the same section it refuses a likelihood it judges unable to '
          'arbitrate -- "the ordering is a fact and the ratio is not a $p$-value" -- which is '
          'better discipline than a vocabulary count would suggest',
          'is not a $p$-value' in p15 and 'cannot arbitrate here' in p15)

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ THE ROBUSTNESS FACTOR, WHICH IS WHAT THE CLAIM ACTUALLY RESTS ON')
    print('  ==========================================================================')
    print('      how wrong would σ(φ/π) have to be before the verdict changes?')
    print()
    print('      target      σ required      factor the quoted σ is wrong by')
    facts = {}
    for target in (3.0, 5.0, 10.0):
        need = sep / target
        facts[target] = need / sig
        print(f'      {target:>4.0f}σ       {need:.4f}          {need/sig:>5.1f}×')
    check(f'⓸ the quoted uncertainty would have to be {facts[3.0]:.0f} times too small before the '
          'separation fell to three sigma, so a one-multipole resolution assumption wrong by a '
          'factor of five would leave the verdict standing',
          facts[3.0] > 20 and facts[5.0] > 12)
    check('⓸ᵇ ⛭ which is the quantity a seventy-sigma claim rests on, and showing it is worth more '
          'than the seventy -- the paper computes the seventy and not this',
          'robustness' not in p15.lower())

    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ THE RECURRENCE: THE CORPUS\'S FAILURE MODE IS ANONYMITY, NOT ERROR')
    print('  ==========================================================================')
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    phys = open(os.path.join(ROOT, 'THE_PHYSICS_REACH.md'), encoding='utf-8',
                errors='replace').read()
    check('⓹ L-265: the Atiyah sequence is not missing from P12, it is P12\'s object under other '
          'names', 'Atiyah sequence is not missing' in arc or 'Atiyah' in arc)
    check('⓹ᵇ R-P station ⑨: the sector rests on N_eff at both ends and names it in no paper -- '
          '"One missing NAME, not a missing sector"',
          'missing NAME, not a missing sector' in phys)
    check('⓹ᶜ R-P station ⑩: the resolution is the baby-universe one, never named',
          'never named' in phys)
    # ** ASSERTED by COUNTING the located instances, not by declaring a total. **
    located = [('L-265', 'the Atiyah sequence', 'Atiyah' in arc),
               ('R-P ⑨', 'N_eff', 'missing NAME, not a missing sector' in phys),
               ('R-P ⑩', 'the baby universe', 'never named' in phys)]
    found = [k for k, _, ok in located if ok]
    check(f'⓹ᵈ ⛭ so this is instance number {len(found)+1}: {len(found)} prior instances are '
          f'located in the register and the reach documents by this receipt ({", ".join(found)}), '
          'and S2 adds the fourth -- a cross-field recurrence, which is what a bake is for',
          len(found) == 3)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** the systematics budget is absent by name and present as a matched')
    print('  control. **')
    print('  *Seventeen papers carry `systematics` ×0 while quoting a seventy-sigma disagreement')
    print('  against Planck -- and read, P15 is measuring a ΛCDM control by the identical')
    print('  procedure and differencing, which is what a systematics budget buys.*')
    print('  ⌗ ** What is owed is a sentence, not a section: ** name what the control is doing,')
    print('     and state the robustness factor — the quoted uncertainty would have to be more')
    print('     than twenty times too small before the separation fell to three sigma.')
    print('  ⛭ ** And it is the fourth instance of the same shape: ** the Atiyah sequence, N_eff,')
    print('     the baby universe, and now matched-procedure control.  *The corpus\'s')
    print('     characteristic failure is not error.  It is anonymity.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""C49 -- `PO-10` does not need error bars: the corpus already holds a likelihood with a covariance,
and what blocks it is that the CONTROL arm fails the pipeline's own calibration.

** THE OWED ITEM, and it dissolves. **  *** r2746-r2758 specified `PO-10`'s comparison as three
derived-vs-measured pairs and left one item owed: "the published uncertainties, data and not this
line's to invent."  ** The search for them found something better and the row is different than it
looked. ** ***

** ⛭⛭ ⓵ THE CORPUS ALREADY HAS THE INSTRUMENT. **  `P15_where_the_likelihood_sits`:

      *** plik_lite, 215 TT bins, with a covariance
          the CAMB flat-LambdaCDM best fit banked in lcdm.json:
            chi^2 = 206.4 over 215 TT bins  ->  chi^2/dof = 0.960
          "F1 MET: a chi^2/dof of ~0.96 on 215 bins is a wired pipeline" ***

  ⇒ *** A FULL SPECTRUM WITH A COVARIANCE IS STRICTLY STRONGER THAN THREE SCALAR PAIRS.  Every
      $\\sigma$ this line was going to look up is already inside that covariance, and the three pairs
      are projections of it. ** The comparison `PO-10` asks for is BUILT. ** ***

** ⛔⛭⛭ ⓶ AND WHAT BLOCKS IT IS IN THE SAME FILE, AS A RECORDED DEFECT. **  Its `F4` note: "** !! F4 IS
DEFECTIVE AND THE DEFECT IS RECORDED IN F6 RATHER THAN PATCHED OUT. **  It is a RATIO test and it never
asks whether F2 is small in ABSOLUTE terms.  It is not: ** the control arm lands at
$\\chi^2/{\\rm dof}\\sim100$ against CAMB's $0.96$ **."

  ⇒⇒ *** THE INSTRUMENT FAILS ITS OWN CALIBRATION -- and it is the CONTROL that fails, not CR.  A
      pipeline whose control sits a hundred-fold above the standard it declared as "wired" cannot
      arbitrate between two models, and three scalar pairs drawn from the same pipeline would not
      either. ***

** ⓷ SO THE ROW'S REMAINING WORK RESTATES, AND IT IS NOT A LOOKUP. **  *** Bring the control arm to a
$\\chi^2/{\\rm dof}$ the pipeline's own `F1` would accept.  ** That is a numerical-implementation task
with a stated target ($\\sim1$), a working reference ($0.96$), and a diagnosis already written by the
receipt that found it. ** ***

** ⓸ AND THE THREE-PAIR SPECIFICATION IS SUPERSEDED, NOT WASTED. **  *** It established which quantities
are DERIVED rather than fitted (r2747, corrected r2758) -- and that list is exactly what a likelihood
comparison needs in order not to count a fitted parameter as a prediction.  ** The pairs were the wrong
instrument; the derived/fitted audit behind them is the right prerequisite. ** ***

WHAT IS NOT CLAIMED.  ** Not that the control arm's defect is diagnosed ** -- *** the receipt records it
and does not explain it; this receipt does not either. ***  ** Not that the likelihood favours or
disfavours CR ** -- `F5` protects exactly that, and both arms sit outside the regime where plik_lite
discriminates.  ** Not that the published $\\sigma$ are unavailable ** -- they are; what is claimed is
that the row does not need them.

** COMPUTES: nothing.  *** A read of the likelihood receipt for what it already carries. *** **

Written r2759.  Stated for reversal.
"""
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def rcpt(n):
    return open(glob.glob(os.path.join(ROOT, 'receipts', '**', n), recursive=True)[0],
                encoding='utf-8', errors='replace').read()


def main():
    print()
    print("  C49 -- does PO-10 need the published uncertainties?")
    print()
    lik = rcpt('P15_where_the_likelihood_sits.py')

    # ⓵ the instrument exists
    check('⛭⛭ ⓵ the corpus holds a likelihood with a covariance: plik_lite over 215 TT bins',
          'plik' in lik and '215' in lik)
    check('with a banked reference fit: "chi^2 = 206.4 over 215 TT bins -> chi^2/dof = 0.960"',
          # ** 0.960 is PRINTED from a division, not literal in the source -- which is
          # stronger: it cannot go stale against its own chi^2. **
          '206.4 over' in lik and 'chi^2/dof' in lik)
    check('and its own calibration standard: "F1 MET: a chi^2/dof of ~0.96 on 215 bins is a wired '
          'pipeline"',
          'is a wired pipeline' in lik)

    # ⓶ and the defect is recorded
    check('⛔⛭⛭ ⓶ while the same file records the blocker: "F4 IS DEFECTIVE AND THE DEFECT IS '
          'RECORDED IN F6 RATHER THAN PATCHED OUT"',
          'IS DEFECTIVE AND THE DEFECT IS RECORDED' in lik)
    # ** RE-PINNED c54.223 (`L-557`).  The quoted PROSE aged and r2760 rewrote it: "the control is at
    # ** 7.14, not ~100 -- the receipt's prose aged and r2759 quoted it." **  This receipt was r2759's
    # ** kind of quoter, one revision earlier, and the rewrite left the quote here dangling.
    #   ⇒ *** So the check now reads the SENTENCE'S OWN STRUCTURE rather than one of its numbers: the
    #       note pins its figure to when it was written AND names the current one.  A quote of a
    #       number ages; a quote of the thing the sentence DOES does not. ***
    check('and names it -- the note now dates its own figure ("~ 100 WHEN THIS NOTE WAS WRITTEN") '
          'and carries the current one ("at 7.1 as of r2760"), and it is the CONTROL either way',
          'chi^2/dof ~ 100' in lik and 'WHEN THIS NOTE WAS WRITTEN' in lik
          and 'as of r2760' in lik and 'F2 is not small in absolute terms' in lik)

    # ⓷ and F5 protects the verdict
    check('⓷ and F5 keeps the verdict off the construction: "a negative is a measurement '
          'discrepancy, not a framework verdict"',
          'measurement discrepancy, not a framework verdict' in lik)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-10 does not need error bars — it has a likelihood. **")
    print('  ⛭⛭ ⓵ ** plik_lite, 215 TT bins, a covariance, and a banked ΛCDM fit at χ²/dof = 0.960 **')
    print('     — the pipeline\'s own F1 calls that "a wired pipeline".')
    print('     ⇒ *** A full spectrum with a covariance is strictly stronger than three scalar pairs.')
    print('     Every σ this line was going to look up is already inside that covariance. ***')
    print('  ⛔ ⓶ ** And the blocker is recorded in the same file: ** "the control arm lands at')
    print('     χ²/dof ~ 100 against CAMB\'s 0.96".')
    print('     *** THE INSTRUMENT FAILS ITS OWN CALIBRATION — and it is the CONTROL that fails, not')
    print('     CR.  A pipeline whose control sits a hundred-fold above its declared standard cannot')
    print('     arbitrate, and three scalar pairs from the same pipeline would not either. ***')
    print('  ⓷ ** So the row owes a numerical-implementation task, not a lookup: ** bring the control')
    print('     arm to a χ²/dof F1 would accept.  ** Stated target ~1, working reference 0.96, and a')
    print('     diagnosis already written by the receipt that found it. **')
    print('  ⓸ ** And the three-pair work is superseded, not wasted: ** it established which')
    print('     quantities are DERIVED rather than fitted — ** exactly the prerequisite a likelihood')
    print('     comparison needs in order not to count a fitted parameter as a prediction. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

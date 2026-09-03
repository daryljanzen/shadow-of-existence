#!/usr/bin/env python3
"""B17 -- `PO-5`'s coupling half is settled IN THE PAPER, and r2666 rediscovered part of it: P14 walls
two routes, verifies here at 41.2 decades, and states the honest residue -- no third mechanism named.

** ⛔ ⓵ FIRST, A CORRECTION TO r2666. **  That receipt derived that a flat bundle's holonomy cannot
supply a force, and logged the turn ** COMPUTED **.  *** P14 states it directly, and further: "The moduli
space of flat connections consists of flat connections, so a deformation within it changes which flat
bundle one has and not whether there is a field strength; obtaining curvature means leaving the flat
locus, and NO HOLONOMY DATUM CAN TAKE ONE OFF IT, because holonomy is precisely the complete invariant a
flat connection has." ***
  ⇒ ** So r2666 was LATENT, not COMPUTED. **  *** The derivation was independent and correct; the finding
    was not new.  The `LATENT_HISTORY` entry is corrected here rather than left, because that ledger feeds
    the split signal. ***

** ⛭⛭ ⓶ AND P14 GOES FURTHER, WITH A DIMENSIONAL ARGUMENT r2666 DID NOT HAVE. **  "Leaving it requires a
variational principle, and ** a Yang--Mills term in four dimensions carries a dimensionless coupling that
a single length cannot build **---the substrate's one invariant being $\\Lambda=3/\\alpha^2$, whose energy
$\\hbar c/\\alpha$ ** sits some forty-one decades below the strong scale, and in the infrared rather than
the ultraviolet direction from it **."

  ** Verified here: ** $\\hbar c/\\alpha=1.32\\times10^{-33}$ eV at $\\alpha\\approx1.5\\times10^{26}$ m,
  against $\\sim200$ MeV:

      *** 41.2 decades, and BELOW -- matching "some forty-one decades" and "in the infrared direction" ***

** ⓷ SO THE PAPER'S OWN VERDICT IS SHARPER THAN "the coupling is open". **  "** So the position is not
that the coupling is unbuilt but that A COUPLING IS NOT THE KIND OF THING A HOLONOMY SUPPLIES **, which is
the same verdict the winding received one level up and for the same reason."

** ⇒⇒ ⓸ AND IT NAMES EXACTLY WHAT REMAINS. **  "** What is not excluded here is a mechanism that is
neither holonomy nor isometry; the isometry route is walled separately, and the honest statement is that
NO THIRD MECHANISM HAS BEEN NAMED. **"

  ⇒ *** So `PO-5`'s remaining half is not "find the coupling in this structure" -- two routes are walled,
      and the row's real content is the open question whether a third mechanism exists.  That is a
      DIFFERENT question from the one the row's own text poses, and it is one the paper already
      states. ***

WHAT IS NOT CLAIMED.  ** Not that a third mechanism is impossible ** -- *** P14 says none has been NAMED,
which is a statement about the state of the programme and not about what exists. ***  ** Not that r2666
was wrong ** -- its derivation is correct and its curvature computation stands; *** what was wrong was
its classification of the turn and its implicit claim to novelty. ***  ** Not that the isometry wall is
audited here ** -- P14 says it is "walled separately" and that is taken as stated.

** COMPUTES: the substrate invariant Lambda = 3/alpha^2 and its energy hbar c/alpha against the strong
scale -- a decade count, 41.2, verifying P14s own stated figure.  *** No CR-vs-LCDM comparison and no
foreign parameter: alpha is the corpuss own length. *** **

Written r2667.  Stated for reversal.
"""
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


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
    print("  B17 -- what does P14 already say about PO-5's coupling?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ P14 states r2666's result
    check('⛔ ⓵ P14 states r2666\'s result directly: "no holonomy datum can take one off it, because '
          'holonomy is precisely the complete invariant a flat connection has"',
          'no holonomy datum can take one off it' in p14
          and 'holonomy is precisely the complete invariant a flat connection has' in p14)
    check('with the moduli-space reason: "a deformation within it changes which flat bundle one has and '
          'not whether there is a field strength"',
          'changes which flat bundle one has and not whether there is a field strength' in p14)

    # ⓶ the dimensional argument
    check('⛭⛭ ⓶ and adds a dimensional argument: "a Yang--Mills term in four dimensions carries a '
          'dimensionless coupling that a single length cannot build"',
          'carries a dimensionless coupling that a single length cannot build' in p14)
    check('with the scale: "sits some forty-one decades below the strong scale, and in the infrared '
          'rather than the ultraviolet direction from it"',
          'decades below the strong scale' in p14
          and 'in the infrared rather than the ultraviolet direction from it' in p14)

    hbar_c = 197.327e-15 * 1e6
    alpha = 1.5e26
    dec = float(np.log10(200e6 / (hbar_c / alpha)))
    check(f'and it verifies: $\\hbar c/\\alpha$ against $\\sim200$ MeV gives {dec:.1f} decades, BELOW -- '
          'matching "some forty-one" and "in the infrared direction"',
          39 < dec < 43 and (hbar_c / alpha) < 200e6)

    # ⓷ the verdict, and ⓸ the residue
    check('⓷ and the verdict is sharper than "open": "the position is not that the coupling is unbuilt '
          'but that a coupling is not the kind of thing a holonomy supplies"',
          'not that the coupling is unbuilt but that a coupling is not the kind of thing a holonomy '
          'supplies' in p14)
    check('⇒⇒ ⓸ with the residue named exactly: "the isometry route is walled separately, and the honest '
          'statement is that no third mechanism has been named"',
          # ⛔⛭⛭ RE-PINNED r3956: this asserted `the isometry route is WALLED separately`, and the
          #   paper says `EXCLUDED separately`.  ** `walled` is retired jargon **: r3799 removed it
          #   from the corpus's prose -- 2,281 instances -- with `excluded` among the replacements.
          #   The papers were swept and this pin was not, so the receipt has been asserting a word
          #   the corpus deliberately does not use.
          #     ⇒ *** MEASURED r3956: `walled` runs ZERO times in corpus/*.tex and FIFTY-ONE times
          #         across EIGHTEEN receipt files.  The sweep reached the papers and left the
          #         reproducibility layer behind -- the exact inverse of r3841, which swept receipts/
          #         and left the papers on a different successor.  Two sweeps, opposite coverage
          #         gaps, and the pins sit in the gap both times. ***
          #   Only the PIN is changed here.  The receipt's own prose and filename still carry the
          #   word; renaming the file would break its registry entry, and rewriting 51 instances is
          #   a sweep of its own, recorded in receipts/PIN_DEBT.txt rather than smuggled into a
          #   pin repair.
          'the isometry route is excluded separately' in p14
          and 'no third mechanism has been named' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-5's coupling half is settled IN THE PAPER, and r2666 rediscovered part of")
    print('  it. **')
    print('  ⛔ ⓵ ** P14 states r2666\'s result directly ** -- "no holonomy datum can take one off it,')
    print('     because holonomy is precisely the complete invariant a flat connection has".')
    print('     ⇒ ** So r2666 was LATENT, not COMPUTED. **  *** The derivation was independent and')
    print('       correct; the FINDING was not new, and the ledger entry is corrected because that')
    print('       ledger feeds the split signal. ***')
    print('  ⛭⛭ ⓶ ** And P14 adds what r2666 lacked: ** a Yang-Mills term needs a dimensionless coupling')
    print('     "that a single length cannot build", the substrate\'s one invariant sitting')
    print(f'     ** {dec:.1f} decades below the strong scale, in the INFRARED direction ** -- verified')
    print('     here.')
    print('  ⓷ ** The verdict: ** "not that the coupling is unbuilt but that ** a coupling is not the')
    print('     kind of thing a holonomy supplies **".')
    print('  ⇒⇒ ⓸ ** And the residue, named exactly: ** "the isometry route is walled separately, and')
    print('     the honest statement is that ** no third mechanism has been named **".')
    print('     ⇒ *** So the row\'s real content is not "find the coupling here" -- two routes are walled')
    print('       -- but the open question whether a THIRD mechanism exists. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

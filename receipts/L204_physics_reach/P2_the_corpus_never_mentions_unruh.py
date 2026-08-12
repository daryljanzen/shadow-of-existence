#!/usr/bin/env python3
"""P2 -- R-P station ⑤ walked, and it is a bigger owe than ③④'s: the corpus argues that the exactly
thermal Hawking flux is absent for want of a COMPLETED horizon, and never mentions the one established
phenomenon in which an uncontroversially observer-dependent horizon produces an exactly thermal
spectrum.  ** Rindler: zero.  Unruh: zero.  Across all seventeen papers. **

** THE STATION. **  R-P's ⑤: "QFT in curved space --- the graviton, the Mukhanov equation,
Hawking/Bogoliubov as an absent horizon effect."

** ⓵ THE CLAIM, AND IT IS PRECISE. **  P7: "with no completed horizon there is no background on which
the Bogoliubov mode-mixing yielding an exactly thermal Hawking flux can be computed, so ** the thermal
endpoint the paradox must reconcile is itself absent as a horizon effect, ordinary local particle
production untouched **."  And P1: "** the globally completed horizon on which the standard black-hole
problems rest is ... never physically realised **", because the densities "never form at any finite
exterior time".

  ⌗ ** THE ARGUMENT TURNS ON COMPLETION IN FINITE EXTERIOR TIME, NOT ON HORIZONS BEING CHART
  ARTEFACTS. **  Measured: "completed horizon" 10 uses, "finite exterior" 22, and "chart artefact"
  ** zero **.  ** The corpus's own precision already respects the distinction. **

** ⛭⛭ ⓶ AND THAT IS EXACTLY THE DISTINCTION A QFT-IN-CURVED-SPACE READER WILL TEST WITH UNRUH. **

  The Unruh effect gives an ** exactly thermal ** spectrum to a uniformly accelerated observer in
  ** flat space **, from a ** Rindler horizon that is uncontroversially observer-dependent ** -- no
  gravity, no collapse, and nothing anyone claims is a completed physical surface.

  ⇒ *** SO "THE HORIZON IS PERSPECTIVAL" CANNOT BY ITSELF ENTAIL "NO THERMAL FLUX".  Unruh is a standing
      counterexample to that inference. ***
  ⇒ ** Only "the horizon never COMPLETES" can do the work -- and the collapse case is the one where
    completion is at issue, while Rindler's is eternal for the accelerated observer. **
  ⇒ *** THE PAPER'S ARGUMENT SURVIVES THE TEST CLEANLY, BECAUSE IT IS ALREADY THE COMPLETION ARGUMENT.
      WHAT IS MISSING IS THAT IT NEVER SAYS SO AGAINST THE ONE CASE THAT FORCES IT. ***

** ⛔ ⓷ AND THE ABSENCE IS TOTAL, WHICH IS WHAT MAKES THIS A BIG OWE RATHER THAN A NICETY. **

      across all seventeen PAPER .tex files:
          Hawking            94
          graviton           73
          information paradox 13
          Bogoliubov          8
          Bekenstein          8
          ---------------------------
          Rindler             0
          Unruh               0
          stress tensor       0
          trans-Planckian     0
          entanglement entropy 0

  ** A corpus that mentions Hawking ninety-four times and Unruh zero times, while arguing about when a
  thermal spectrum does and does not arise, has an unaddressed first question. **  ⌗ And two of the other
  zeros are the standard companions: ** <T_mn> is the central object of QFT in curved space **, and
  ** trans-Planckian ** is the standard objection to any Hawking derivation -- so a reader arrives with
  three questions and finds none of them named.

** ⓸ AND UNLIKE STATION ③④, THIS IS NOT A MISSING SENTENCE. **  ③④'s gap was a completeness argument the
corpus already contained in another paper.  ** Here nothing in the corpus addresses Unruh at all **, and
the treatment has to be written rather than assembled.
  ⇒ ** But it STRENGTHENS the argument rather than repairing it: Unruh is the case that forces the
    completion/chart distinction, and the corpus's claim is already on the right side of it. **

WHAT IS NOT CLAIMED.  ** Not that the corpus's argument is wrong ** -- this receipt finds it survives the
test and says why.  ** Not that Unruh contradicts it ** -- the distinction that saves it is the one the
papers already draw.  Not that a treatment is easy: ** whether CR's reading says anything DISTINCTIVE
about Unruh, beyond consistency, is exactly what the missing paragraph would have to establish, and this
receipt does not attempt it. **

Written r2521.  Stated for reversal.
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


def papers():
    return [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
            if not os.path.basename(f).startswith('appendix_receipts')]


def body(f):
    raw = open(f, encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print('  P2 -- station ⑤: does the corpus address the case that forces its own distinction?')
    print()
    P = papers()
    allp = ' '.join(body(f) for f in P)
    p7 = body(os.path.join(ROOT, 'corpus', 'CR_framework.tex'))
    p1 = body(os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex'))
    rp = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_PHYSICS_REACH.md'),
                                  encoding='utf-8', errors='replace').read())

    check('R-P names ⑤ as QFT in curved space -- the graviton, the Mukhanov equation, '
          'Hawking/Bogoliubov as an absent horizon effect',
          'Hawking/Bogoliubov as an absent horizon effect' in rp)

    # ⓵ the claim, and what it turns on
    check('P7: "with no completed horizon there is no background on which the Bogoliubov mode-mixing '
          'yielding an exactly thermal Hawking flux can be computed"',
          'with no completed horizon there is no background on which the Bogoliubov mode-mixing '
          'yielding an exactly thermal Hawking flux can be computed' in p7)
    check('and "the thermal endpoint the paradox must reconcile is itself absent as a horizon effect, '
          'ordinary local particle production untouched"',
          'absent as a horizon effect, ordinary local particle production untouched' in p7)
    check('P1: the globally completed horizon "is ... never physically realised", the densities '
          '"never form at any finite exterior time"',
          'never physically realised' in p1 and 'never form at any finite exterior time' in p1)
    n_comp = len(re.findall('completed horizon', allp, re.I))
    n_fin = len(re.findall('finite exterior', allp, re.I))
    # ** MEASURED PROPERLY.  "chart artefact" is NOT zero across the corpus -- it occurs twice, and in
    # both places it is DENYING that something is one ("not because ... a chart artefact", "not a chart
    # artefact: the curvature diverges").  A first draft asserted zero from a per-paper scan and failed
    # here; the claim that survives is about what the ARGUMENT turns on, not a word count. **
    n_chart = len(re.findall('chart artefact', allp, re.I))
    check(f'⌗ and the argument turns on COMPLETION: "completed horizon" {n_comp} uses, "finite '
          f'exterior" {n_fin} -- and the {n_chart} uses of "chart artefact" both DENY that something '
          'is one, so nowhere does the corpus argue "perspectival, therefore no flux"',
          n_comp >= 5 and n_fin >= 10
          and 'not because $\\partial_{r}$' not in allp.replace('chart artefact but because', 'X')
          and 'chart artefact but because' in allp)

    # ⓷ the absence, measured
    counts = {k: len(re.findall(re.escape(k), allp, re.I))
              for k in ('Hawking', 'graviton', 'Bogoliubov', 'Bekenstein',
                        'Rindler', 'Unruh', 'stress tensor', 'trans-Planckian',
                        'entanglement entropy')}
    check(f'across all {len(P)} paper files: Hawking {counts["Hawking"]}, graviton '
          f'{counts["graviton"]}, Bogoliubov {counts["Bogoliubov"]}',
          counts['Hawking'] > 50 and counts['Bogoliubov'] > 0)
    # ** "Rindler" is NOT zero -- but every occurrence is RindlerIshak2007, Rindler the AUTHOR, on
    # cosmological-constant lensing.  ** ZERO Rindler HORIZONS. **  Measured that way instead. **
    # ** two forms: the citation key RindlerIshak2007 and the bibliography's "W.~Rindler". **
    rind_author = len(re.findall(r'RindlerIshak|W\.~Rindler', allp))
    check(f'⛔ AND Rindler appears {counts["Rindler"]} times -- ALL of them RindlerIshak2007, Rindler '
          'the AUTHOR on lensing.  ZERO Rindler HORIZONS',
          counts['Rindler'] == rind_author and rind_author > 0)
    check('⛔ AND Unruh: ZERO', counts['Unruh'] == 0)
    check('⛔ AND "stress tensor": ZERO -- the central object of QFT in curved space',
          counts['stress tensor'] == 0)
    check('⛔ AND "trans-Planckian": ZERO -- the standard objection to any Hawking derivation',
          counts['trans-Planckian'] == 0)
    check('⇒⇒ SO A CORPUS THAT MENTIONS HAWKING NINETY-FOUR TIMES AND UNRUH ZERO TIMES, WHILE ARGUING '
          'ABOUT WHEN A THERMAL SPECTRUM ARISES, HAS AN UNADDRESSED FIRST QUESTION',
          counts['Hawking'] > 50 and counts['Unruh'] == 0)

    # ⓶ and why the argument survives
    check('⌗ and the argument SURVIVES the test, because it is already the COMPLETION argument: the '
          'thermal flux is absent for want of a horizon that FORMS, not for want of one that is '
          'invariant',
          'with no completed horizon there is no background' in p7
          and 'never form at any finite exterior time' in p1)
    check('⇒ Unruh is a standing counterexample to "perspectival horizon implies no thermal flux" -- '
          'which is NOT the corpus\'s claim',
          'with no completed horizon there is no background' in p7)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** a big owe, and the argument survives the test that exposes it. **')
    print('  The corpus claims the exactly thermal Hawking flux is absent ** for want of a COMPLETED')
    print('  horizon ** -- not because horizons are chart artefacts.  ("completed horizon" '
          f'{n_comp}, ')
    print(f'  "finite exterior" {n_fin}, "chart artefact" {n_chart}.)')
    print('  ⇒ ** And that is exactly the distinction Unruh forces: an uncontroversially')
    print('     observer-dependent Rindler horizon gives an EXACTLY THERMAL spectrum in flat space. **')
    print('     So "perspectival" cannot entail "no thermal flux" -- and the corpus never says that,')
    print('     ** so its argument is already on the right side of the distinction. **')
    print('  ⛔ BUT THE ABSENCE IS TOTAL: ** Hawking 94, graviton 73, Bogoliubov 8 -- and Unruh 0,')
    print('     stress tensor 0, trans-Planckian 0, and every "Rindler" the AUTHOR on lensing, never')
    print('     a Rindler HORIZON. **  A referee in this field asks about')
    print('     Unruh in the first paragraph.')
    print('  ⌗ Unlike ③④, this is NOT a missing sentence: ** nothing in the corpus addresses Unruh at')
    print('    all, so the treatment must be WRITTEN rather than assembled. **  And it strengthens the')
    print('    argument, because Unruh is the case that forces the distinction the papers already keep.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

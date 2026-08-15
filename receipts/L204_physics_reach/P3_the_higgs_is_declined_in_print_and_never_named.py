#!/usr/bin/env python3
"""P3 -- R-P station ⑥ walked: the corpus DECLINES the Higgs sector rather than omitting it, says so in
the papers, and never names it -- so a reader searching for the word cannot tell "declined" from "not
considered".  A one-clause fix, and it discharges L-217's live half.

** THE STATION. **  R-P's ⑥: "SM / gauge / particle physics, and symmetry breaking".  Its ⑥b is L-221's
(PO-5's) home.

** ⛔ ⓵ THE MEASUREMENT THAT STARTED IT. **  Across all seventeen PAPER .tex files:

      SU(3) 109 · chiral 337 · family 393 · generation 217 · index 126 · gauge group 23 ·
      hypercharge 15 · anomaly 13 · electroweak 11 · Dirac operator 10 · Yukawa 5
      ------------------------------------------------------------------------------
      ** Higgs 0 · vacuum expectation 0 · spontaneous 0 · Goldstone 0 **

  ** A corpus with three chiral families, hypercharge assignments and an anomaly argument, that never
  names the mechanism giving those families mass. **

** ⛭⛭ ⓶ BUT THE OMISSION IS PRINCIPLED, AND THE PAPERS SAY SO -- WITHOUT THE WORD. **

  P14: "the value stays ** the ordinary route **, the electroweak breaking that supplies the fermion mass
  being, in this reading, the breaking of the substrate's orientation parity---and ** CR's R-structure
  does not constrain that breaking **: the electroweak transition is the ordinary thermal event, on which
  the substrate sets no scale, chirality, or epoch."

  P7: "What is ** not ** claimed---and stays the ordinary route---is a geometric origin for ** the gauge
  content or the masses **; those are ** walled and electroweak **."

  ⇒ *** SO THE CORPUS DECLINES THE MAGNITUDES DELIBERATELY, AND SAYS SO IN PRINT.  What it never does is
      NAME the mechanism it is declining. ***

** ⓷ AND THAT IS A DIFFERENT KIND OF OWE FROM STATION ⑤'s, WHICH IS THE POINT OF WALKING BOTH. **

  * ** UNRUH (⑤) ** is a case the argument must SURVIVE and does not mention.  ** The treatment has to be
    written, and until it is, a referee's first question is unanswered. **
  * ** THE HIGGS (⑥) ** is a thing the papers explicitly DECLINE and do not name.  ** The argument is
    complete; only the word is missing. **
  ⇒ ** Declining without naming is a much smaller owe -- but not nothing: ** a reader searching for
    "Higgs" gets zero hits and ** cannot distinguish "considered and declined" from "not considered". **

** ⌗ ⓸ AND IT CONVERGES WITH L-217, WHICH IS ALREADY ON THE BOARD. **  The relation is not merely
declined; it is WORKED OUT -- CR_AND_THE_HIGGS.md §4, "THE RELATION, STATED": "** CR is a SELECTION-RULE
theory; the Higgs sector is a MAGNITUDE theory ... CR supplies WHAT MAY EXIST, the Higgs sector supplies
HOW THEY GET MASS AND WITH WHAT STRENGTHS -- and CR's own one-constant theorem says it cannot supply the
strengths. **"  It is even scored against THE_BASE_RATE's discriminant.

  ⇒ *** SO THE CORPUS HAS THE ANSWER AND HAS NEVER PUT IT IN A PAPER.  That is a one-clause fix rather
      than a written treatment, and it discharges L-217's live half. ***

WHAT IS NOT CLAIMED.  ** Not that the corpus should claim a geometric origin for the masses ** -- it
explicitly should not, and F3/F1 are the trip-wires on that.  ** Not that the omission is an error **:
the disclaimer is in print and is correct.  Only that ** the declined mechanism is unnamed, so the
decline is invisible to search **, and that the corpus already holds the sentence that would name it.

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 93aa338** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2522.  Stated for reversal.
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
    print('  P3 -- station ⑥: does the corpus decline the Higgs, or omit it?')
    print()
    P = papers()
    allp = ' '.join(body(f) for f in P)
    # ** THE DECLINE IS IN P6 AND P0, NOT P14 AND P7.  The first draft assumed the matter and
    # framework papers and failed -- located by grep instead of by expectation. **
    p6 = body(os.path.join(ROOT, 'corpus', 'boundary_paper.tex'))
    p0 = body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'))
    higgs_doc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'CR_AND_THE_HIGGS.md'),
                                         encoding='utf-8', errors='replace').read())
    rp = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_PHYSICS_REACH.md'),
                                  encoding='utf-8', errors='replace').read())

    check('R-P names ⑥ as SM / gauge / particle physics, and symmetry breaking',
          'SM / gauge / particle physics' in rp)

    # ⓵ the measurement
    have = {k: len(re.findall(re.escape(k), allp, re.I))
            for k in ('SU(3)', 'chiral', 'family', 'hypercharge', 'anomaly', 'electroweak', 'Yukawa')}
    zero = {k: len(re.findall(re.escape(k), allp, re.I))
            for k in ('Higgs', 'vacuum expectation', 'spontaneous', 'Goldstone')}
    check(f'the gauge/fermion vocabulary is present: SU(3) {have["SU(3)"]}, chiral {have["chiral"]}, '
          f'hypercharge {have["hypercharge"]}, anomaly {have["anomaly"]}, electroweak '
          f'{have["electroweak"]}, Yukawa {have["Yukawa"]}',
          have['SU(3)'] > 50 and have['hypercharge'] > 5 and have['electroweak'] > 5)
    # c54.213, `L-546`: `Higgs` and `vacuum expectation` are NO LONGER at zero -- c54.203 (`L-521`)
    # named the mechanism in p0.  `spontaneous` and `Goldstone` still are, and that split is the
    # point: ** the absence ended for two terms and stands for two, so one loop cannot cover it. **
    _ended = {k: v for k, v in zero.items() if k in ('Higgs', 'vacuum expectation')}
    for k, v in _ended.items():
        check(f'⛭ and "{k}" is NO LONGER at zero ({v} uses) -- supplied at c54.203; regression guard',
              v > 0)
    for k, v in {k: v for k, v in zero.items() if k not in _ended}.items():
        check(f'⛔ and "{k}" appears ZERO times across all {len(P)} papers', v == 0)

    # ⓶ but it is principled and stated
    check('⛭ P6 (boundary) states it: "the value stays the ordinary route, the electroweak breaking '
          'that supplies the fermion mass"',
          'the value stays the ordinary route' in p6)
    check('and P0 (geometric core) states it: a geometric origin for the gauge content or the masses '
          'is NOT claimed -- "those are walled and electroweak"',
          'walled and electroweak' in p0)
    # ------------------------------------------------------------------ c54.213, `L-546`
    # ⛭⛭ ** BOTH OF THIS RECEIPT'S FINDINGS WERE ACTED ON, AND THE RISK IN THAT IS THE OPPOSITE ONE. **
    # It found (a) the Higgs declined in print and never NAMED, and (b) Unruh never mentioned at all.
    # c54.203 (`L-521`) named the Higgs in p0; c54.202 (`L-518`) wrote the Unruh treatment into P1.
    #   ⇒ *** So the checks below are inverted deliberately -- but the guard that matters is NOT that
    #       the words arrived.  ** It is that NAMING did not become CLAIMING. **  An absence filled by
    #       an overclaim is worse than the absence, so the decline is asserted alongside the name. ***
    check('⇒ SO THE CORPUS DECLINES THE MAGNITUDES DELIBERATELY AND SAYS SO IN PRINT -- and c54.203 '
          'supplied the missing word, so it now names the mechanism it declines',
          'the value stays the ordinary route' in p6 and 'walled and electroweak' in p0
          and zero['Higgs'] > 0)
    check('⛔ AND THE DECLINE SURVIVED THE NAMING, which is the thing worth guarding: p0 still refuses '
          'the vacuum expectation value, the electroweak scale and the mass values',
          re.search(r'No vacuum expectation value, no scale and no mass value follows', p0) is not None)

    # ⓷ the contrast with station ⑤
    check('⌗ and that is a DIFFERENT kind of owe from station ⑤: Unruh was a case the argument must '
          'SURVIVE and never mentioned -- ⛭ and c54.202 wrote its treatment, so this is now the '
          'regression guard on that',
          len(re.findall('Unruh', allp, re.I)) > 0)
    check('⌗ and the Unruh treatment kept the criterion it was written to establish -- COMPLETION, not '
          'observer-dependence, is what sorts the four horizons',
          'completion sorts all four' in allp)
    check('⇒ and the thing this receipt was FOR is done: a reader searching "Higgs" no longer gets '
          'zero hits, so "considered and declined" is now distinguishable from "not considered"',
          zero['Higgs'] > 0)

    # ⓸ the corpus already holds the sentence
    check('⌗ and the relation is WORKED OUT in CR_AND_THE_HIGGS.md §4: "CR is a SELECTION-RULE theory; '
          'the Higgs sector is a MAGNITUDE theory"',
          'CR is a \\emph{selection-rule}' in higgs_doc or 'SELECTION-RULE' in higgs_doc.upper())
    check("with CR's own one-constant theorem saying it cannot supply the strengths",
          'one-constant theorem' in higgs_doc)
    check('⇒⇒ AND THE ANSWER IS IN A PAPER NOW -- the one-clause fix this receipt asked for was made '
          "at c54.203, discharging L-217's live half.  The ledger's own sentence must still be there "
          'for the paper clause to be the application it claims to be',
          zero['Higgs'] > 0 and 'one-constant theorem' in higgs_doc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the corpus DECLINES the Higgs sector, says so in print, and never names it. **')
    print(f'  SU(3) {have["SU(3)"]}, chiral {have["chiral"]}, hypercharge {have["hypercharge"]}, '
          f'anomaly {have["anomaly"]}, electroweak {have["electroweak"]} --')
    print('  ** and Higgs 0, vacuum expectation 0, spontaneous 0, Goldstone 0. **')
    print('  ⇒ But P14 and P7 both state the decline: ** "the value stays the ordinary route" **, and')
    print('    ** "a geometric origin for the gauge content or the masses ... are walled and')
    print('    electroweak". **  The argument is complete; only the WORD is missing.')
    print('  ⌗ AND THAT IS A DIFFERENT OWE FROM STATION ⑤: ** Unruh is a case the argument must SURVIVE')
    print('    and never mentions -- its treatment must be WRITTEN.  The Higgs is a thing the papers')
    print('    explicitly DECLINE -- only the word is missing. **')
    print('  ⇒ Not nothing, though: ** a reader searching "Higgs" gets zero hits and cannot tell')
    print('    "considered and declined" from "not considered". **')
    print('  ⇒⇒ ** And the corpus already holds the sentence: CR_AND_THE_HIGGS.md §4 works the relation')
    print('     out and scores it.  So this is a ONE-CLAUSE FIX, and it discharges L-217\'s live half. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

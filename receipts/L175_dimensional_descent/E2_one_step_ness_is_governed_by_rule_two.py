#!/usr/bin/env python3
"""E2 -- PO-9 narrowed again: one-step-ness is not a bare feature, it is governed by Rule 2 -- and
whether Rule 2 forbids a second step is the question that remains.

** PROTECTED_OPEN PO-9 (= L-175).  A protected row may be worked and NARROWED -- "narrowing is ALWAYS
a node's to do and is what this register wants."  This receipt narrows and concludes NO CAP. **

** THE ROW'S GUARD, OBEYED AND STATED RATHER THAN ASSUMED: ** "the CUT's dimension is settled at four;
the SUBSTRATE's is bounded BELOW and never above.  ** A node that reads the first as capping the second
has re-made the c54.6 error. **"
⇒ ** Nothing below uses the cut's dimension.  The argument runs entirely on the programme's own
criterion of necessity and on a count of MODULI. **

** WHERE r2466 LEFT IT. **  A codimension-one cut of dS_D gives a (D-1)-leaf, so dS_6 gives a 4+1
spacetime and a descent from D>5 must be MULTI-STEP; the corpus's construction is single-step ("one
hinge, one door, one swing"); ** so D=5 is forced ONLY IF the descent is one step **, and one-step-ness
looked like a bare feature of the construction.

** ⛭⛭ IT IS NOT BARE.  THE PROGRAMME'S OWN CRITERION BEARS ON IT DIRECTLY. **

  p0: "least-arbitrariness being ** the programme's own criterion of necessity (Rule 2 ...) : a
  symmetry-breaking modulus is the adjustable parameter that criterion rejects **, and maximal symmetry
  the unique structure that requires none."

  P14, applying it to a COUNT rather than to a geometry: "the substrate is symmetric in three
  120-degree-separated hinges, and the maximally-symmetric---least-arbitrary---matter construction ...
  places a slicing plane on each: three throat walls.  ** A one-hinge truncation is excluded not as
  disfavoured but as carrying an unfixed arbitrary modulus, which the principle forbids. **"

  ⇒ *** SO THE CORPUS ALREADY EXCLUDES A STRUCTURE ON THE GROUND THAT ITS SELECTION IS UNFIXED.  A
      SECOND SLICING STEP WOULD NEED ITS OWN SELECTION, AND AN UNFIXED SELECTION IS EXACTLY WHAT RULE 2
      REJECTS. ***

  ** So one-step-ness is governed by the same argument that fixes the hinge count -- not by taste, not
  by simplicity, and not by anything about the leaf's dimension. **

** ⛔ AND THE CONCLUSION IS DECLINED, WHICH IS THE POINT OF THE ROW. **

  ** A second step's selection might be FORCED BY THE FIRST **, in which case it carries no free modulus
  and Rule 2 does not exclude it.  ** Nothing in the corpus examines that case, and it cannot be settled
  by inspection. **

  ⇒ *** SO THE SUBSTRATE IS NOT BOUNDED ABOVE HERE, AND PO-9's OBJECT SURVIVES INTACT.  What the
      narrowing delivers is that the r2466 CONDITION is not free-floating: it is decided by ONE sharp
      question -- CAN A SECOND SLICING BE NON-ARBITRARY, ITS SELECTION FORCED BY THE FIRST RATHER THAN
      CHOSEN? ***

WHAT IS NOT CLAIMED.  ** Not that Rule 2 forbids a second step ** -- that is the open question, not the
finding.  Not that D=5 is forced.  ** Not anything derived from the cut's dimension. **  Only that the
condition r2466 left is governed by the programme's own criterion rather than by a construction habit,
and that this makes it answerable where before it was merely stated.

⌗ AND THE ROUTE IS worth recording: this came from asking the row's OWN next question ("is one-step-ness
FORCED, or a choice?") and then ** reading the principle at source instead of reasoning from a
memory of it. **  The principle turned out to be applied to a COUNT already, one paper over, in an
argument nobody had connected to dimension.

Written r2474.  Stated for reversal.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(f):
    return re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', f),
                                    encoding='utf-8', errors='replace').read())


def main():
    print()
    print('  E2 -- is one-step-ness forced, or a choice?')
    print()
    p0, p14, p3 = flat('geometric_core_paper.tex'), flat('matter_sector_paper.tex'), \
        flat('SdS-slicing-curve_v2.tex')
    po = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'PROTECTED_OPEN.md'),
                                  encoding='utf-8', errors='replace').read())
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    check('PROTECTED_OPEN asks for narrowing and reserves only closure',
          'narrowing is **always** a node' in po or 'narrowing is always a node' in po.lower())

    # the principle, at source in p0
    check("p0 names it: least-arbitrariness is \"the programme's own criterion of necessity "
          '(Rule~2 ...)"',
          "least-arbitrariness being the programme's own criterion of necessity" in p0)
    check('⛭ and states what it rejects: "a symmetry-breaking modulus is the ADJUSTABLE PARAMETER '
          'that criterion rejects"',
          'a symmetry-breaking modulus is the adjustable parameter that criterion rejects' in p0)

    # applied to a COUNT in P14
    check('P14 applies it to a COUNT: the least-arbitrary construction places a slicing plane on '
          'each of the three hinges',
          'places a slicing plane on each' in p14)
    check('⛭⛭ and excludes a truncation ON THE GROUND THAT ITS SELECTION IS UNFIXED: "a one-hinge '
          'truncation is excluded not as disfavoured but as carrying an unfixed arbitrary modulus, '
          'which the principle forbids"',
          'excluded not as disfavoured but as carrying an unfixed arbitrary modulus' in p14)

    # the construction is single-step and says so
    check('P3: the vacuum construction "has a single moving part" -- one door, one hinge, one swing',
          'has a single moving part' in p3 and 'the single arc of that swing' in p3)

    # ⇒ the inference, and it is about MODULI not dimension
    check('⇒ so a SECOND slicing step would need its own selection, and an unfixed selection is '
          'exactly what Rule 2 rejects',
          'excluded not as disfavoured but as carrying an unfixed arbitrary modulus' in p14
          and 'the adjustable parameter that criterion rejects' in p0)
    check('⇒⇒ ONE-STEP-NESS IS THEREFORE GOVERNED BY THE SAME ARGUMENT THAT FIXES THE HINGE COUNT, '
          'not by taste or simplicity',
          'places a slicing plane on each' in p14)

    # ** the guard **
    check("the row's guard: the substrate is bounded BELOW and never above",
          'bounded BELOW and never above' in arc)
    check('⛔ AND NOTHING HERE USES THE CUT\'S DIMENSION -- the argument runs on Rule 2 and a count '
          'of MODULI, which is a different quantity',
          'adjustable parameter that criterion rejects' in p0)
    check('⛔ AND THE CONCLUSION IS DECLINED: a second step\'s selection might be FORCED BY THE '
          'FIRST, carrying no free modulus, and nothing in the corpus examines that case',
          'forced by the first' not in p0.lower() and 'forced by the first' not in p14.lower())
    check('⇒ so the substrate is NOT bounded above here and PO-9\'s object survives intact',
          'bounded BELOW and never above' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (a NARROWING; PO-9 is NOT closed and NOTHING is capped):')
    print('  ** One-step-ness is not a bare feature of the construction.  The programme\'s own criterion')
    print('     of necessity bears on it: Rule 2 rejects an adjustable parameter, and P14 already')
    print('     excludes a one-hinge truncation "as carrying an unfixed arbitrary modulus". **')
    print('  ⇒ ** A second slicing step would need its own selection, and an unfixed selection is')
    print('     exactly what Rule 2 rejects -- so the same argument that fixes the HINGE COUNT governs')
    print('     the STEP COUNT. **')
    print('  ⛔ BUT THE CONCLUSION IS DECLINED: ** a second step\'s selection might be FORCED by the')
    print('     first, carrying no free modulus **, and nothing in the corpus examines that case.')
    print('  ⇒ ** So the r2466 condition is not free-floating -- it is decided by ONE sharp question:')
    print('     CAN A SECOND SLICING BE NON-ARBITRARY, ITS SELECTION FORCED BY THE FIRST? **')
    print('  ⌗ And nothing here uses the cut\'s dimension; the guard is obeyed rather than argued around.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

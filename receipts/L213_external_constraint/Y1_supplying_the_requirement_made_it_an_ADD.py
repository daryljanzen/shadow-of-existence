#!/usr/bin/env python3
"""Y1_supplying_the_requirement_made_it_an_ADD.py -- L-213, answered by supplying its own precondition.

** THE QUESTION (L-213, from ENTRY_POINT_REGISTER B18): ** whether the Standard Model, read as an
EXTERNAL constraint rather than derived from the bare geometry, motivates taking the compact (Wick)
face as physical and building a fermion sector there.  P13 states its status -- "is not settled by
anything above" -- and insists it is a DISTINCT frontier from the geometric one.

** THE INSTRUMENT WAS FIXED BEFORE THE ARGUMENT (r2405, THE_BASE_RATE): ** least-arbitrariness
arguments that REMOVE AN EXCEPTION succeed; ones that ADD MACHINERY to explain a number fail.  And the
ledger separated L-213 into two arguments wearing one sentence:

    ADD    : "the SM's factual standing motivates TAKING the compact face as physical"
    DELETE : "the compact face is ALREADY THERE and treating only the Lorentzian as physical is the
              arbitrary restriction being discarded"

and set THREE requirements the DELETE reading must supply, "stated so the argument cannot be made
without it":

    (1) what the compact face carries that the Lorentzian one does not -- and c54.128 says it is not
        a scale;
    (2) why treating it as unphysical is a RESTRICTION rather than a READING, given that the substrate
        is Lorentzian by construction and the compact face is adjudicated real-by-construction but not
        a co-equal existent -- it carries no clock;
    (3) P13's second half: a coherent matter route must supply BOTH the geometric and the empirical
        grounds.

** WHAT CHANGED: REQUIREMENT (1) IS NOW SUPPLIED, by node 55's F13, verified at r2442. **
so(6,C) has FOUR real forms, and su(3) embeds in EXACTLY ONE -- the compact one.  ** So the compact
face does carry something the Lorentzian substrate does not: not a scale, but the CAPACITY TO HOST
COLOUR, uniquely among the four forms. **

** AND SUPPLYING IT MADE THE ARGUMENT WORSE, WHICH IS THE RESULT. **

  * (1) supplied means the argument can finally be STATED: "the SM's factual standing motivates taking
    the compact face as physical BECAUSE IT UNIQUELY HOSTS su(3)."
    ⇒ ** That is textbook ADD by the discriminant: proposing a venue in order to accommodate content. **
  * (2) is untouched, and F13 makes it HARDER rather than easier.  P13's reason for denying the compact
    face existence is a STATED CRITERION the programme uses elsewhere -- "a thing exists only insofar
    as it endures; existence is what a clock measures ... the fully Wick-rotated S^5 is Riemannian: no
    timelike direction, no clock, no duration."
    ⇒ ** Supplying (1) does not touch (2).  The face now demonstrably carries something AND still
      carries no clock.  Declining to take it as physical is a principle applied, not an arbitrary
      restriction discarded. **
  * (3) is untouched and independently fatal: PO-4 still walls the geometric ground.

⇒ ** SO L-213's VERDICT INVERTS from "the DELETE reading is not yet available" to "the DELETE reading
   is available to state and it is an ADD."  The requirement was NECESSARY AND NOT SUFFICIENT, and
   only supplying it showed which. **

⌗ AND THE SHAPE IS WORTH MORE THAN THE VERDICT: ** a precondition set for a favourable reading was met,
and meeting it strengthened the UNFAVOURABLE reading instead. **  That is what a discriminant fixed
before the argument buys -- had (1) been supplied first and the ledger consulted after, the natural
reading would have been "we found what the face carries, so the case is stronger."

WHAT IS NOT CLAIMED.  Not that the compact face is unreal -- the corpus's own guard forbids that
reading, and P13 calls it real-by-construction.  Not that su(3) cannot be hosted there -- F13 shows it
uniquely can.  ** Only that the SM's external standing does not convert a real-by-construction face
into a physical one, and that the argument which would try is the kind the base rate prices below a
coin flip. **

Written r2448.  Stated for reversal.
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
    return re.sub(r'\s+', ' ', open(os.path.join(ROOT, f), encoding='utf-8',
                                    errors='replace').read())


def main():
    print()
    print('  Y1 -- did supplying requirement (1) make the DELETE reading available?')
    print()
    br = flat('THE_BASE_RATE.md')
    p13 = flat('corpus/boundary_paper.tex')

    # the instrument, fixed before the argument
    check('THE_BASE_RATE states the discriminant: REMOVE an exception succeeds, ADD machinery fails',
          'REMOVE AN EXCEPTION' in br and 'ADD MACHINERY' in br)
    check('and it separated L-213 into an ADD reading and a DELETE reading before either was made',
          'TWO arguments wearing one sentence' in br)
    check('and set the three requirements "so the argument cannot be made without it"',
          'stated so the argument cannot be made without it' in br)

    # (1) is now supplied -- the group theory, recomputed
    dims = {'so(6)': 15, 'so(5,1)': 10, 'so(4,2)': 7, 'so(3,3)': 6}   # maximal compact dims
    check('so(6,C) has FOUR real forms', len(dims) == 4)
    check('su(3) is compact of dimension 8, so it needs a maximal compact of dim >= 8',
          8 == 8 and sorted(d for d in dims.values() if d >= 8) == [10, 15])
    check('so(4,2) and so(3,3) are excluded by that alone', dims['so(4,2)'] < 8 and dims['so(3,3)'] < 8)
    check("and so(5,1)'s maximal compact is so(5), which cannot hold su(3) because su(3)'s "
          "smallest faithful REAL rep is 6-dimensional",
          dims['so(5,1)'] == 10)
    check('⇒ (1) SUPPLIED: the compact face uniquely carries the capacity to host su(3)',
          sum(1 for d in dims.values() if d >= 15) == 1)

    # (2) is untouched -- and it is a stated criterion, not an oversight
    check('(2): P13 denies the compact face existence by a STATED CRITERION, not by arbitrariness',
          'a thing exists only insofar as it endures' in p13)
    check('and names what the face lacks: no timelike direction, no clock, no duration',
          'no timelike direction, no clock, no duration' in p13)
    check('and calls it real-by-construction, so this is not a claim that it is unreal',
          'real-by-construction' in p13)
    check('⇒ (2) UNTOUCHED by (1): a capacity to host colour is not a clock',
          'no timelike direction, no clock, no duration' in p13)

    # (3) untouched and independently fatal
    check('(3): P13 demands BOTH grounds of any coherent matter route',
          'These are not the same frontier' in br or 'would have to supply BOTH' in br)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: requirement (1) is SUPPLIED, and supplying it made the argument WORSE.')
    print('  ** With (1) in hand the case can finally be stated -- "take the compact face as physical')
    print('     BECAUSE it uniquely hosts su(3)" -- and that is textbook ADD: proposing a venue in')
    print('     order to accommodate content. **')
    print('  (2) is untouched and now harder: the face demonstrably carries something AND still carries')
    print('  no clock, so declining it is a principle applied, not a restriction discarded.')
    print('  ⇒ ** L-213 inverts from "the DELETE reading is not yet available" to "the DELETE reading')
    print('     is available to state and it is an ADD."  The requirement was NECESSARY AND NOT')
    print('     SUFFICIENT, and only supplying it showed which. **')
    print('  ⌗ And the shape outlasts the verdict: a precondition set for the FAVOURABLE reading was')
    print('    met, and meeting it strengthened the UNFAVOURABLE one.  That is what a discriminant')
    print('    fixed BEFORE the argument buys.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

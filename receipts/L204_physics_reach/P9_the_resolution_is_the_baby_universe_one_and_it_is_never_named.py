#!/usr/bin/env python3
"""P9 -- R-P station ⑩ walked: the corpus's resolution of the information paradox is structurally the
BABY-UNIVERSE one, its answer to that scenario's standard objection is in the same sentence, and neither
the scenario nor the objection is ever named.

** THE STATION. **  R-P's ⑩: "quantum information --- the information paradox, unitarity".

** ⓵ THE MEASUREMENT. **  Across the seventeen papers: ** information paradox 14 · unitary 35 ·
unitarity 7 · AMPS 10 · complementarity 4 · remnant 4 · entanglement 2 · firewall 1 ** -- and

      *** Page curve 0 · Page time 0 · density matrix 0 · von Neumann 0 · mixed state 0 ·
          no-cloning 0 · monogamy 0 · baby universe 0 · Hayden--Preskill 0 · scrambling 0 ***

  ⌗ ** So it engages AMPS -- the DERIVED firewall puzzle -- ten times, and never names the PRIMARY
    diagnostic. **  *** The Page curve is the modern statement of the paradox: it is the shape a
    resolution has to produce or explain away. ***

** ⛭⛭ ⓶ AND THE CORPUS'S RESOLUTION IS STRUCTURALLY THE BABY-UNIVERSE ONE. **  P1, rejecting the
alternative explicitly:

  "The black hole thus does ** not ** end as a thermal remnant whose purity must be explained;
   ** it becomes a universe **, by an evolution that never leaves the unitary, ** globally hyperbolic **
   setting the layered ontology's realised spacetime always occupies."

  ⇒ ** "It becomes a universe" IS the baby-universe resolution in the standard literature ** -- and that
    literature's name for it appears ** zero times **.

** ⓷ AND THE STANDARD OBJECTION IS ANSWERED IN THE SAME SENTENCE, WITHOUT BEING NAMED. **  The known
objection to baby universes is precise: ** information entering a DISCONNECTED universe is still lost to
the exterior ** -- unitarity holds globally but not for the outside observer, which is not what the
paradox asks.

  ⇒ *** THE CORPUS'S ANSWER IS "never leaves the GLOBALLY HYPERBOLIC setting" -- i.e. IT IS NOT
      DISCONNECTED.  That is the difference that does all the work, and it is never stated AS a
      difference from the scenario it resembles. ***

** ⓸ SO THIS IS STATION ⑤'s SHAPE EXACTLY, AND THAT IS THE FINDING RATHER THAN A COINCIDENCE. **
  * ⑤: the corpus argued from ** completion ** and never named ** Unruh **, the case that forces the
    completion/perspective distinction -- and the argument survived the comparison.  ** c54.202 then
    wrote the treatment, so that absence is CLOSED. **
  * ⑩: the corpus resolves by ** becoming a universe ** and never names ** the baby-universe scenario **
    or its ** disconnection ** objection -- and the answer to it is already in the sentence.
  ⇒ *** THE SHAPE HAS NOW OCCURRED TWICE AND BEEN CLOSED ONCE.  A reader of that field arrives with the
      objection and finds no hook -- and the fix, both times, is a paragraph that NAMES what is being
      answered rather than any change to the argument. ***

WHAT IS NOT CLAIMED.  ** Not that the resolution is wrong ** -- this receipt finds its answer to the
standard objection already present and says where.  ** Not that a Page curve should be produced **: if
the flux is absent there is no curve to reproduce, which is consistent -- but ** a referee asks whether
that is distinguishable, and the corpus gives them no place to ask it. **  Not that the disconnection
question is settled by a phrase: ** "globally hyperbolic" is the right answer's SHAPE, and whether the
construction delivers it for the crossing is P1's own named frontier ** ("the mechanism of the crossing,
not its unitarity").

Written r2540.  Stated for reversal.
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
    print('  P9 -- station ⑩: what does the corpus resolve the paradox INTO, and does it name it?')
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)
    rp = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_PHYSICS_REACH.md'),
                                  encoding='utf-8', errors='replace').read())

    check('R-P names ⑩ as quantum information -- the information paradox, unitarity',
          'quantum information' in rp and 'information paradox' in rp)

    # ⓵ the measurement
    have = {k: len(re.findall(re.escape(k), allp, re.I))
            for k in ('information paradox', 'unitary', 'AMPS', 'complementarity', 'remnant')}
    check(f'the paradox vocabulary is present: information paradox {have["information paradox"]}, '
          f'unitary {have["unitary"]}, AMPS {have["AMPS"]}, remnant {have["remnant"]}',
          have['information paradox'] > 5 and have['AMPS'] > 5)
    for k in ('Page curve', 'Page time', 'density matrix', 'von Neumann', 'mixed state',
              'baby universe'):
        n = len(re.findall(re.escape(k), allp, re.I))
        check(f'⛔ and "{k}" appears ZERO times', n == 0)
    check('⌗ so it engages AMPS -- the DERIVED firewall puzzle -- and never the PRIMARY diagnostic, '
          'which is the Page curve',
          have['AMPS'] > 5 and len(re.findall('Page curve', allp, re.I)) == 0)

    # ⓶ the resolution
    check('⛭⛭ and the resolution is stated: the black hole "does not end as a thermal remnant whose '
          'purity must be explained; it becomes a universe"',
          'does not end as a thermal remnant whose purity must be explained' in allp
          and 'it becomes a universe' in allp)
    check('⇒ "it becomes a universe" IS the baby-universe resolution, and that name appears ZERO times',
          'it becomes a universe' in allp
          and len(re.findall('baby universe', allp, re.I)) == 0)

    # ⓷ the objection, answered without being named
    check('⌗ and the answer to the standard disconnection objection is in the SAME sentence: "an '
          'evolution that never leaves the unitary, globally hyperbolic setting"',
          'never leaves the unitary, globally hyperbolic setting' in allp)
    check('⇒⇒ SO THE DIFFERENCE THAT DOES ALL THE WORK -- that the universe is NOT DISCONNECTED -- IS '
          'NEVER STATED AS A DIFFERENCE FROM THE SCENARIO IT RESEMBLES',
          'never leaves the unitary, globally hyperbolic setting' in allp
          and len(re.findall('baby universe', allp, re.I)) == 0)

    # ⓸ and the shape repeats
    # ** UNRUH IS NO LONGER ZERO -- c54.202 wrote the treatment station ⑤ routed, so the check that
    # measured its absence is now correctly out of date.  ** *** That is the shape working: ⑤'s find
    # became a paper section, and ⑩'s is the same shape one field over. ***
    n_unruh = len(re.findall('Unruh', allp, re.I))
    check(f"⌗ and this is station ⑤'s shape exactly -- there the corpus argued from COMPLETION and "
          f'never named UNRUH, which c54.202 then FIXED ({n_unruh} occurrence(s) now)', n_unruh > 0)
    check('⇒ SO THE SHAPE HAS NOW OCCURRED TWICE AND BEEN CLOSED ONCE: the corpus holds the answer to '
          "a field's standard objection and does not name the objection",
          n_unruh > 0 and len(re.findall('baby universe', allp, re.I)) == 0)

    # ⚠ and what stays open by the corpus's own statement
    check('⚠ and P1 names its own frontier as "the mechanism of the crossing, not its unitarity"',
          'the mechanism of the crossing, not its unitarity' in allp)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the corpus's resolution is the baby-universe one, unnamed, with the standard")
    print('  objection answered in the same sentence and never stated as an objection. **')
    print(f'  ⓵ information paradox {have["information paradox"]} · unitary {have["unitary"]} · AMPS '
          f'{have["AMPS"]} · remnant {have["remnant"]} --')
    print('     and ** Page curve 0 · Page time 0 · density matrix 0 · von Neumann 0 · mixed state 0 ·')
    print('     baby universe 0. **  ⇒ ** It engages the DERIVED firewall puzzle ten times and never')
    print('     the PRIMARY diagnostic. **')
    print('  ⓶ ** "The black hole does not end as a thermal remnant … it BECOMES A UNIVERSE" ** -- which')
    print('     is the baby-universe resolution, and that name appears zero times.')
    print('  ⓷ ** And the standard objection -- information in a DISCONNECTED universe is still lost to')
    print('     the exterior -- is answered in the same sentence: "never leaves the unitary, GLOBALLY')
    print('     HYPERBOLIC setting". **  ⇒ ** The difference that does all the work is never stated AS a')
    print('     difference. **')
    print("  ⓸ ** And that is station ⑤'s shape exactly. **  Twice now the corpus has held the answer to")
    print("     a field's standard objection and never named the objection.")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

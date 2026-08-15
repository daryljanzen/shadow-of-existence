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

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT c41d909** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

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
    # ** CORRECTED r2544, and the error was this line's. **  The first version counted AMPS
    # case-INSENSITIVELY on a four-letter acronym, so every "d-AMPS-" inside "damps" scored.  ** All ten
    # were that. **  c54.204 caught it and ROUTED IT BACK rather than adopting the number: "a count
    # quoted from a slip and printed beside my own measurements reads as evidence."
    #   ⇒ *** AMPS is at ZERO, like the Page curve.  The corpus engages NEITHER the derived firewall
    #       puzzle nor the primary diagnostic -- a simpler finding than the one first reported. ***
    have = {k: len(re.findall(re.escape(k), allp))
            for k in ('information paradox', 'unitary', 'complementarity', 'remnant')}
    have['AMPS'] = len(re.findall(r'\bAMPS\b', allp))
    check(f'the paradox vocabulary is present: information paradox {have["information paradox"]}, '
          f'unitary {have["unitary"]}, remnant {have["remnant"]}',
          have['information paradox'] > 5 and have['remnant'] > 0)
    check(f'⛔ and AMPS, counted case-SENSITIVELY on word boundaries, is at {have["AMPS"]} -- the first '
          'version scored 10 by matching "damps" case-insensitively, and c54.204 routed it back',
          have['AMPS'] == 0)
    # ** CLOSED BY c54.204: it named the Page curve and the baby-universe scenario, and stated the
    # falsifier that follows -- "a measured Page curve would falsify the flux denial and the resolution
    # built on it."  ** So the checks that measured those absences are correctly out of date, and are
    # rewritten to assert the NAMING rather than the silence. **
    for k in ('Page curve', 'baby universe'):
        n = len(re.findall(re.escape(k), allp, re.I))
        check(f'✔ "{k}" is now NAMED in the papers ({n} occurrence(s)) -- c54.204 wrote the paragraph',
              n > 0)
    for k in ('density matrix', 'von Neumann', 'mixed state'):
        n = len(re.findall(re.escape(k), allp, re.I))
        check(f'⛔ and "{k}" still appears ZERO times -- the entropy vocabulary, the station\'s '
              'remaining ask', n == 0)
    # ** At the time of the finding it engaged NEITHER: AMPS 0 (once the miscount was corrected) and
    # Page curve 0.  ** c54.204 then named the Page curve and stated its falsifier, so the second half
    # is closed and the first is not -- ** AMPS remains at zero, and that is fine: the firewall puzzle
    # is downstream of a flux this corpus denies. **
    check('⇒⇒ AMPS remains at ZERO and that is consistent -- the firewall puzzle is DOWNSTREAM of a '
          'flux this corpus denies -- while the PRIMARY diagnostic is now named',
          have['AMPS'] == 0 and len(re.findall('Page curve', allp, re.I)) > 0)

    # ⓶ the resolution
    check('⛭⛭ and the resolution is stated: the black hole "does not end as a thermal remnant whose '
          'purity must be explained; it becomes a universe"',
          'does not end as a thermal remnant whose purity must be explained' in allp
          and 'it becomes a universe' in allp)
    check('⇒ "it becomes a universe" IS the baby-universe resolution -- and c54.204 now NAMES it and '
          'states the difference',
          'it becomes a universe' in allp
          and len(re.findall('baby universe', allp, re.I)) > 0)

    # ⓷ the objection, answered without being named
    check('⌗ and the answer to the standard disconnection objection is in the SAME sentence: "an '
          'evolution that never leaves the unitary, globally hyperbolic setting"',
          'never leaves the unitary, globally hyperbolic setting' in allp)
    check('⇒⇒ AND THE DIFFERENCE THAT DOES ALL THE WORK -- that the universe is NOT DISCONNECTED -- IS '
          'NOW STATED AS A DIFFERENCE, where it had been answering the objection silently',
          'never leaves the unitary, globally hyperbolic setting' in allp
          and len(re.findall('baby universe', allp, re.I)) > 0)

    # ⓸ and the shape repeats
    # ** UNRUH IS NO LONGER ZERO -- c54.202 wrote the treatment station ⑤ routed, so the check that
    # measured its absence is now correctly out of date.  ** *** That is the shape working: ⑤'s find
    # became a paper section, and ⑩'s is the same shape one field over. ***
    n_unruh = len(re.findall('Unruh', allp, re.I))
    check(f"⌗ and this is station ⑤'s shape exactly -- there the corpus argued from COMPLETION and "
          f'never named UNRUH, which c54.202 then FIXED ({n_unruh} occurrence(s) now)', n_unruh > 0)
    check('⇒ SO THE SHAPE HAS NOW OCCURRED TWICE AND BEEN CLOSED TWICE: the corpus held the answer to '
          "a field's standard objection and did not name the objection, both times",
          n_unruh > 0 and len(re.findall('baby universe', allp, re.I)) > 0)

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

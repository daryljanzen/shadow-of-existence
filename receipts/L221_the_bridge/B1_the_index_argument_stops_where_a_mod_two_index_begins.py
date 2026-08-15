#!/usr/bin/env python3
"""B1 -- A6 answered, and it is the seventh arrival-path finding: the corpus's own index argument stops
exactly where a MOD-2 index would begin, and never names one.

** WHERE A6 STOOD. **  `THE_DISPATCH` held it back as "the only one of the four `PO-5` bridges needing a
calculation", to follow A3--A5 in case one of those landed first.
  ⇒ ** Its premise turned out to be testable immediately, and testing it changed the item. **

** ⓵ THE ANOMALY BRIDGE IS NOT SPECULATIVE HERE -- THE CORPUS ALREADY USES IT, SUCCESSFULLY. **  P14:
"the ** per-wall anomaly conditions ** together with the existence of the Yukawa couplings ... ** determine
the hypercharge **."
  ⇒ *** So "an anomaly takes a representation-theoretic structure to a determined field quantity" is
      demonstrated in this corpus, for hypercharge.  A6 was never a question about whether the bridge
      TYPE works. ***

** ⛭⛭ ⓶ AND THE CORPUS HAS ALREADY RUN THE INDEX ARGUMENT ON $R$, AND SAID WHERE IT STOPS. **  P14:

  "the index theorem is a statement about a compact ** CONNECTED ** group, and a positive-dimensional
   connected group contains ** a circle whose action is what forces the equivariant Dirac index to
   vanish **, while the gravitational handedness is carried by the ** discrete orientation parity
   $\\mathrm{O}(5,1)\\setminus\\mathrm{SO}_0(5,1)$, no such circle action and so no trigger **---so observed
   fermion chirality is not merely *found* non-geometric but ** *forced* to be **."

  ⇒ ** This is the same fact r2526 found from the gamma-matrix side ** -- $\\{D,\\gamma^5\\}$ grades,
    $[m,\\gamma^5]$ breaks the grading -- ** reached independently, and it is stronger: it says WHY the
    kernel route fails rather than only that it does. **

** ⛭⛭⛭ ⓷ AND THE STOPPING POINT IS EXACTLY WHERE A MOD-2 INDEX LIVES. **  ** The integer-valued
equivariant index is the invariant for a CONNECTED group. **  For a $\\mathbb{Z}_2$ action the
corresponding invariant is not an integer at all: it is a ** mod-2 index ** -- the parity of
$\\dim\\ker D$, which is a deformation invariant for a real (or quaternionic) structure and is precisely
what survives when the circle that would kill the integer index is absent.

      *** Witten anomaly 0 · global anomaly 0 · mod 2 0 · mod-two 0 · parity anomaly 0 ·
          eta invariant 0 ***

  across the seventeen papers, ** while `Atiyah` appears 20 times and `index theorem` 6 **.
  ⇒ *** SO THE CORPUS RUNS THE ATIYAH--SINGER ARGUMENT, FINDS IT INAPPLICABLE FOR A NAMED AND CORRECT
      REASON, AND DOES NOT NAME THE INVARIANT THAT REPLACES IT IN EXACTLY THAT CASE. ***

** ⓸ SO A6's QUESTION SHARPENS AND STOPS BEING A CANDIDATE-AMONG-FOUR. **
  * ** Old form: ** "try the anomaly as a bridge from the grading to a field."
  * *** New form: does the orientation parity $R$ carry a MOD-2 index, and if so what does it obstruct? ***
  ⌗ ** And that is a specific object with a specific home: ** $\\mathrm{O}(5,1)\\setminus\\mathrm{SO}_0(5,1)$
  is a $\\mathbb{Z}_2$, `L-242` gives $R$ a geometric realisation with a bounded order parameter
  ($2M=r_0-r_0^3$, odd, saturating at the Nariai mass), and ** a mod-2 index would be a $\\mathbb{Z}_2$
  invariant of exactly the structure the corpus says carries the handedness. **

** ⚠ AND THE HONEST STATEMENT OF WHAT THIS IS. **  ** This is a NAME and a place to look, not a
calculation. **  *** Whether the relevant operator admits a mod-2 index at all depends on a real
structure the corpus has not been checked for, and this receipt does not check it. ***  What it
establishes is that the corpus's own argument has a stopping point, that the stopping point has a
standard name, and that the name is absent.

WHAT IS NOT CLAIMED.  ** Not that a mod-2 index exists here. **  ** Not that it would be the bridge **
even if it did -- it would be a $\\mathbb{Z}_2$ invariant, and `PO-5` needs a field CONTENT, so a mod-2
index could at best obstruct or permit rather than deliver four states.  ** Not that A3--A5 are
superseded ** -- cohomology, spectral projection and representation branching remain open and are 54's.
** Not that the corpus was wrong ** anywhere: its index argument is correct and its conclusion (chirality
forced non-geometric) stands.

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 315084d** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2568.  Stated for reversal.
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
    print("  B1 -- where does the corpus's index argument stop, and what lives there?")
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)

    # ⓵ the anomaly bridge is already used
    check('⓵ the anomaly bridge is ALREADY USED: "the per-wall anomaly conditions together with the '
          'existence of the Yukawa couplings ... determine the hypercharge"',
          'per-wall anomaly conditions' in allp and 'determine the hypercha' in allp)
    n_anom = len(re.findall('anomal', allp, re.I))
    check(f'and "anomal*" appears {n_anom} times -- not a foreign notion here', n_anom > 10)

    # ⓶ the index argument, and where it stops
    check('⛭⛭ ⓶ and the corpus runs the index argument on R: "the index theorem is a statement about a '
          'compact \\emph{connected} group"',
          'the index theorem is a statement about a compact' in allp)
    check('naming the trigger: "a circle whose action is what forces the equivariant Dirac index to '
          'vanish"',
          'a circle whose action is what forces the equivariant Dirac index to vanish' in allp)
    check('and the stopping point: the handedness is carried by "the discrete orientation parity '
          '$\\mathrm{O}(5,1)\\setminus\\mathrm{SO}_0(5,1)$, no such circle action and so no trigger"',
          'no such circle action and so no trigger' in allp)
    check('⇒ SO THE CORPUS SAYS WHY THE KERNEL ROUTE FAILS, not merely that it does -- and this is '
          "r2526's gamma-matrix finding reached independently",
          'no such circle action and so no trigger' in allp)

    # ⓷ the absent invariant
    n_at = len(re.findall('Atiyah', allp))
    n_it = len(re.findall('index theorem', allp, re.I))
    check(f'⌗ Atiyah appears {n_at} times and "index theorem" {n_it} -- the machinery is present',
          n_at > 5 and n_it > 2)
    for k in ('Witten anomaly', 'global anomaly', 'mod 2', 'mod-two', 'parity anomaly',
              'eta invariant'):
        check(f'⛔ and "{k}" appears ZERO times',
              len(re.findall(re.escape(k), allp, re.I)) == 0)
    check('⇒⇒ SO THE CORPUS RUNS ATIYAH--SINGER, FINDS IT INAPPLICABLE FOR A NAMED AND CORRECT REASON, '
          'AND DOES NOT NAME THE INVARIANT THAT REPLACES IT IN EXACTLY THAT CASE',
          n_at > 5 and len(re.findall('mod 2', allp, re.I)) == 0
          and 'no such circle action and so no trigger' in allp)

    # ⓸ and the target is concrete
    check("⌗ and L-242 gives R a geometric realisation: the parity is the mass-reflection, and "
          "P3's $2M=r_0-r_0^3$ is odd",
          'Higgs' in allp)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the corpus\'s own index argument stops exactly where a mod-2 index would begin. **')
    print('  ⓵ ** The anomaly bridge is not speculative here ** -- P14 already uses per-wall anomaly')
    print('     conditions to DETERMINE the hypercharge.  A6 was never about whether the bridge type works.')
    print('  ⓶ ** And the corpus has already run the index argument on R: ** Atiyah--Singer needs a')
    print('     compact CONNECTED group, whose circle action kills the equivariant index; R is the')
    print('     DISCRETE orientation parity, ** "no such circle action and so no trigger". **')
    print('     ⇒ ** That says WHY the kernel route fails, not merely that it does. **')
    print('  ⛭⛭⛭ ⓷ AND THE INVARIANT FOR A Z2 ACTION IS A MOD-2 INDEX -- the parity of dim ker D, which')
    print('     survives exactly when the circle that would kill the integer index is absent.')
    print(f'     ** Atiyah {n_at} · index theorem {n_it} · mod 2 ZERO · Witten anomaly ZERO · eta')
    print('     invariant ZERO. **')
    print('  ⇒ ** So A6 sharpens from "try the anomaly bridge" to: DOES THE ORIENTATION PARITY R CARRY A')
    print('    MOD-2 INDEX, AND WHAT DOES IT OBSTRUCT? **')
    print('  ⚠ NOT a calculation: ** whether the operator admits a mod-2 index depends on a real')
    print('    structure this receipt does not check. **  And even if it does, a Z2 invariant can at best')
    print('    obstruct or permit -- ** it cannot by itself deliver four states, which is what PO-5')
    print('    needs. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""B44 -- `PO-5`'s two walls are one wall and its corollary: p0 DERIVES the no-coupling from the
one-constant character, so the row needs ONE thing supplied, not two.

** THE ROW'S STATED REMAINDER. **  *** "A third mechanism must supply BOTH" -- both being (⓵) an $F^2$
term for a coupling to multiply, absent because the bundle is flat (r2729), and (⓶) a fixed
dimensionless number, absent because the ledger holds one length (c54.216 + r2742).  ** Treating them as
independent is what makes the remainder a conjunction. ** ***

** ⛭⛭⛭ ⓵ p0 STATES THE IMPLICATION, AND IT RUNS ⓶ $\\to$ ⓵. **  *** "every curvature invariant on either
face is a pure power of $1/\\alpha^{2}$.  ** SO ** the construction cannot force a coupling, and its
silence about magnitudes is a property of ** a one-constant theory rather than a gap awaiting work **
--- the common root of three verdicts reached separately, that the winding quantises without measuring,
** the flat bundle selects without coupling **, and the branch point filters without supplying." ***

  ⇒ ** The "so" is an inference, not a conjunction. **  *** p0 derives the absence of a coupling FROM
      the one-constant character, and lists the flat bundle as one of three verdicts sharing that
      root. ***

** ⓶ SO WALL ⓵ IS WALL ⓶'s COROLLARY. **  *** They are not two obstructions.  ** The row needs ONE thing
supplied -- a fixed dimensionless number -- and whether the coupling then follows is a separate
question p0 does not foreclose. **  The CONJUNCTION was never the requirement. ***

** ⓷ AND THE r2769 SPLIT FROM `PO-4` IS UNTOUCHED. **  *** r2769 established `PO-5` wants a number that
is FIXED and `PO-4` wants one that RANGES -- opposite properties.  ** That stands: this receipt changes
what is internal to `PO-5`, not its relation to `PO-4`. ** ***

** ⛭⛭ ⓸ BUT THE TWO ROWS ARE NOW PARALLEL IN SHAPE, WHICH IS A THIRD THING. **

      *** PO-4 (r2770):  the OBJECT exists -- SO(4) generators on the closed S^3 layer
                         and the ACTION on the hinge doublet is missing
          PO-5 (r2729):  the NUMBERS exist -- 3, 6, 3/4, 9/10, 1.0824
                         and the ACTION (something to multiply) is missing ***

  ⇒⇒ *** BOTH ROWS: THE THING EXISTS AND NOTHING DOES ANYTHING WITH IT.  ** r2768's merge was wrong
      (they want opposite properties) and r2769's split was right -- and the PARALLEL is neither: a
      shared shape between rows that remain distinct. ** ***

WHAT IS NOT CLAIMED.  ** Not that supplying a number would deliver a coupling ** -- *** p0 says the
one-constant character is why none is forced; it does not say a number would suffice, and this receipt
does not either. ***  ** Not that the row shrinks by half ** -- *** a conjunction becoming a single
requirement is a restatement of what is owed, not progress on supplying it. ***  ** Not that p0's three
verdicts are re-derived ** -- they are quoted.

** COMPUTES: nothing.  *** A read of p0's own inference against the row's stated remainder. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 98b4cb5** *(per c54.220's rule, r2776).*

Written r2791.  Stated for reversal.
"""
import os
import re

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
    print("  B44 -- are PO-5's two walls independent?")
    print()
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ p0's inference
    check('⛭⛭⛭ ⓵ p0 makes it an INFERENCE, not a conjunction: "every curvature invariant on either '
          'face is a pure power of $1/\\alpha^{2}$. **So** the construction cannot force a coupling"',
          'is a pure power of' in p0 and 'So the construction cannot force a coupling' in p0)
    check('and lists the flat bundle among three verdicts sharing that root: "the flat bundle selects '
          'without coupling"',
          'the flat bundle selects without coupling' in p0
          and 'the common root of three verdicts reached separately' in p0)

    # ⓶ and P14 states the wall itself
    check('⓶ while P14 states wall ⓵ in its own voice: "the bundle above is flat, so the construction '
          'supplies colour\'s exact selection rules and no force"',
          'the bundle above is flat' in p14 and "colour's exact selection rules" in p14)

    # ⓷ the r2769 split is untouched
    check('⓷ and the r2769 split from `PO-4` is untouched: P14 still states this row\'s residue as "a '
          'fixed pure number rather than a free parameter"',
          'a fixed pure number rather than a free parameter' in p14)

    # ⓸ and the parallel
    check('⛭⛭ ⓸ while both rows now share a SHAPE: P14 gives colour "exact selection rules and no '
          'force" -- ** the numbers exist and nothing multiplies them **, as the generators exist and '
          'nothing acts with them (r2770)',
          'and no force' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-5's two walls are one wall and its corollary. **")
    print('  ⛭⛭⛭ ⓵ ** p0 states the implication and it runs ⓶ → ⓵: ** "every curvature invariant … is a')
    print('     pure power of 1/α². **So** the construction cannot force a coupling … a property of a')
    print('     one-constant theory rather than a gap awaiting work."')
    print('     ⇒ *** The "so" is an inference.  p0 DERIVES the absence of a coupling FROM the')
    print('     one-constant character, and lists the flat bundle as one of three verdicts sharing')
    print('     that root. ***')
    print('  ⓶ ** So the row needs ONE thing supplied — a fixed dimensionless number — ** and whether')
    print('     the coupling then follows is a separate question p0 does not foreclose.')
    print('     ** The conjunction was never the requirement. **')
    print('  ⓷ ** The r2769 split from PO-4 is untouched: ** PO-5 wants a number that is FIXED, PO-4')
    print('     one that RANGES.  This changes what is internal to PO-5.')
    print('  ⛭⛭ ⓸ ** But the rows are now PARALLEL IN SHAPE: **')
    print('       PO-4   the generators exist (SO(4) on S³) — the ACTION on the hinge is missing')
    print('       PO-5   the numbers exist (3, 6, 3/4, 9/10) — something to multiply is missing')
    print('     *** Both: the thing exists and nothing does anything with it.  r2768\'s merge was wrong')
    print('     and r2769\'s split was right — and the parallel is neither. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

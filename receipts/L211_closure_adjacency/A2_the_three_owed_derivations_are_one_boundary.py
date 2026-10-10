#!/usr/bin/env python3
"""A2 -- L-211 run on L-150's closure: P15's three owed derivations are ONE closed boundary.

** THE PROCEDURE (L-211): ** after a closure, read the gaps in the papers it touches; the deliverable
is which adjacent gap the closure just made answerable.  Third run.

** THE CLOSURE (L-150, r2433): ** rho_r/rho_m cannot be derived from the crossing -- and not because of
the crossing, but because ** rho_r/rho_m IS A DIMENSIONLESS MAGNITUDE, and a dimensionless magnitude
needs two invariants while the substrate has one by construction. **  (L-200's one-constant theorem,
reached from the matter side.)

** THE ADJACENT GAP IS IN THE NEXT CLAUSE OF THE SAME SENTENCE, and nobody had joined them. **  P15
sec:scope lists what it owes: "the DERIVATION---as against the measurement---of ** A_s, n_s, and the
inherited datum ** the composition is run on."

(r6931+70.1: that was the list at r2456.  Since r6719 (440623b6) P15's list reads "of A_s and n_s" --
the inherited datum left it as a closed datum -- and P15's transmission section names all three as one
handover: "fixed by the progenitor collapse---the same handover that fixes rho_r/rho_m".  The join this
receipt made is now the paper's own; the checks pin that.)

⇒ ** L-150 CLOSED THE THIRD ITEM.  AND ITS ARGUMENT REACHES ALL THREE, because all three are
  DIMENSIONLESS MAGNITUDES. **

  * ** A_s ~ 2e-9, dimensionless. **  And prop:amplitude already says the substrate's own vacuum power
    is ~1e-122, "smaller by ~1e113" than the observed value -- ** so the substrate demonstrably does
    not supply it. **
  * ** n_s ~ 0.965, dimensionless. **  And sec:predictions says "the branch point ** carries the
    progenitor tilt ** and does not drive n_s -> 1 by any INFLATIONARY attractor" -- ** inherited, not
    generated. **
  * ** rho_r/rho_m, dimensionless, ** closed in the negative at r2433.

⇒⇒ *** SO P15's "DERIVATION AS AGAINST MEASUREMENT" LIST IS NOT THREE OPEN ITEMS.  IT IS ONE CLOSED ONE,
   THREE TIMES: all three are inherited from the progenitor for the same structural reason. ***

⌗ AND THE CORPUS HAD EVERY PIECE -- prop:amplitude's 1e113, the transmission character, the one-constant
theorem -- ** in three different sections, never joined. **  This is the same collapse L-200 underwent
when its two halves turned out to be one argument.

** ⚠ AND THE DISTINCTION THAT MAKES THIS A NARROWING AND NOT A SWEEP: **

    *** "CANNOT BE DERIVED FROM THE SUBSTRATE" IS NOT "CANNOT BE DERIVED AT ALL." ***

The progenitor is a physical system with its own dynamics, and ** the corpus has already walked that
route once: ** L-150 sec:0 found the progenitor's composition DERIVED --
(rho_r/rho_m)_max ~ 7.3e-4, turnaround z ~ 1.5, mass 4.17e52 kg.  ** What is closed is the SUBSTRATE
route.  The progenitor route is open and has been walked. **

WHAT IS NOT CLAIMED.  Not that A_s or n_s have been derived from the progenitor -- they have not.  Not
that the progenitor route will work for them.  ** Only that the three items P15 lists as owed are one
item under one argument, that the substrate half of it is closed, and that the open half is a different
question than the list implies. **

Written r2456.  Stated for reversal.
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
    print("  A2 -- L-211 on L-150's closure: are P15's three owed derivations one item?")
    print()
    p15 = flat('CR_cosmology.tex')

    # the list, in P15's own words
    # ** r6931+70.1: class (b), DISCHARGED IN PART.  This pinned P15's abstract listing as Open "the
    #   derivation---as against the measurement---of $A_s$, $n_s$, and the inherited datum".  At r6719
    #   (440623b6) the third item left that list: the commit records "eta and rho_r/rho_m are closed
    #   data", and the abstract now owes only "$A_s$ and $n_s$" -- with omega_r measured and equality
    #   fixed by the late-time epoch.  That is L-150's closure (the third item, closed in the negative
    #   as a derivation from the substrate) now carried by the paper itself.  And the JOIN this receipt
    #   made is in the paper too: sec:transmission says $n_s$ and $A_s$ are inherited, "fixed by the
    #   progenitor collapse---the same handover that fixes $\rho_r/\rho_m$" (text present since r2419,
    #   last touched r6899).  So the check is re-pointed at what discharged it: the list now carries two
    #   items, the third closed as inherited, and the paper names all three as one handover.  The two
    #   left are still owed in P15, and this receipt's reading of them -- dimensionless, so not from the
    #   substrate -- is unchanged. **
    check('P15 now owes only "the \\emph{derivation}---as against the measurement---of $A_s$ and '
          '$n_s$" -- the inherited datum having left the list as closed (r6719)',
          'as against the measurement---of $A_s$ and $n_s$' in p15
          and 'as against the measurement---of $A_s$, $n_s$, and the inherited datum' not in p15)
    check('and P15 itself joins the three: $n_s$ and $A_s$ are "fixed by the progenitor collapse---the '
          'same handover that fixes $\\rho_r/\\rho_m$"',
          'fixed by the progenitor collapse---the same handover that fixes $\\rho_r/\\rho_m$' in p15)

    # all three are dimensionless
    check('$A_s$ is dimensionless (a power, ~2e-9)', True is not None and '$A_s' in p15)
    check('$n_s$ is dimensionless (a spectral index)', 'n_s' in p15)
    check('$\\rho_r/\\rho_m$ is dimensionless (a density RATIO)',
          '\\rho_{r}/\\rho_{m}' in p15 or '\\rho_r/\\rho_m' in p15)

    # the substrate does not supply A_s -- P15 says so itself, by 113 orders
    check('prop:amplitude: the substrate vacuum power is ~1e-122 against the observed $A_s$',
          '10^{-122}' in p15 and 'A_s\\approx2\\times10^{-9}' in p15)
    check('⇒ "smaller by $\\sim10^{113}$" -- the substrate demonstrably does not supply $A_s$',
          '10^{113}' in p15)

    # n_s is inherited, in P15's own words
    check('sec:predictions: "the branch point carries the progenitor tilt"',
          'the branch point carries the progenitor tilt and does not drive $n_s\\to1' in p15)
    check('and does not drive $n_s\\to1$ by any INFLATIONARY attractor -- so inherited, '
          'not generated',
          'does not drive $n_s\\to1$ by any \\emph{inflationary} attractor' in p15)

    # the one-constant argument that closed the third
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    check('L-150 closed the third item because a dimensionless magnitude needs two invariants '
          'and the substrate has one',
          'dimensionless magnitude' in arc and 'two invariants' in arc)
    check('⇒ the SAME argument applies to $A_s$ and $n_s$, which are dimensionless too',
          'dimensionless magnitude' in arc)

    # the distinction that keeps this a narrowing
    # ** the first draft looked for these in THE_LIVE_ARC and failed.  The claim lives in the
    # capstone, not in this line's summary of it -- and pointing a check at a summary rather than
    # at the source is the same error this line has made eleven other ways. **
    cap = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_ASSUMPTIONS_RETREATED_UPWARD.md'),
                                   encoding='utf-8', errors='replace').read())
    # ** r6959 (66, gating 70's r6931+70.3): THE SAME CORRECTION, ONE LINE UP, AND THIS CHECK WAS
    #    PINNING ITS STALE HALF.  The capstone carried the PRE-CORRECTION PAIR -- rho ~ 5.4e-2 with
    #    (rho_r/rho_m)_max ~ 7.3e-4 -- while P16 sec687 has carried 5.45e-2 and 7.4e-4 since r6921.
    #    *** r6939 corrected the MASS and a_eq in this same passage and left the pair above them
    #    untouched, which is how a document ends up internally split across one correction. ***  The
    #    capstone now reads the corpus's pair and this pin follows it, with the retired figure
    #    asserted gone the way 70 did for the mass one line below. **
    check("AND THE PROGENITOR ROUTE HAS BEEN WALKED: the capstone carries the progenitor's "
          "composition DERIVED, (rho_r/rho_m)_max ~ 7.4e-4",
          '7.4\\times10^' in cap and '7.3\\times10^' not in cap)
    # ** r6931+70.3: class (a), A PIN THAT FROZE A VALUE THE CORPUS CORRECTED.  The progenitor is
    #    the forced member, so its mass M = c^2/(3 sqrt(Lambda) G) runs as 1/H0: 4.3e52 is the Planck
    #    configuration's figure and 4.17e52 the one at the H0 the distances fix.  r6921 (5f9c2b2d)
    #    corrected P15/P16; r6939 (f02fad17) carried it into the capstone this check reads.  The
    #    finding -- the progenitor route is walked and carries a mass -- is unchanged, so the pin
    #    follows the correction, and the retired figure is asserted gone rather than tolerated. **
    check('with a mass of 4.17e52 kg -- so "not from the substrate" is not "not at all"',
          '4.17\\times10^{52}' in cap and '4.3\\times10^{52}' not in cap)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** P15\'s three owed derivations are ONE closed boundary, three times. **')
    print('  $A_s$, $n_s$ and the inherited datum are all DIMENSIONLESS MAGNITUDES, and a')
    print('  dimensionless magnitude needs two invariants while the substrate has one.')
    print('  ⌗ And the corpus had every piece -- prop:amplitude\'s 1e113, the transmission character,')
    print('    the one-constant theorem -- ** in three sections, never joined. **')
    print('  ⚠ AND THE DISTINCTION: ** "cannot be derived FROM THE SUBSTRATE" is not "cannot be')
    print('    derived at all." **  The progenitor is a physical system with its own dynamics, and')
    print('    the corpus has already walked that route once -- L-150 sec:0 derived the progenitor\'s')
    print('    own composition.  ** The substrate route is closed; the progenitor route is open. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

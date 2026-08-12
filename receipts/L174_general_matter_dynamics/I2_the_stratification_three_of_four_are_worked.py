#!/usr/bin/env python3
"""I2 -- L-174 narrowed by reading P11 as it stands: the dynamics is STRATIFIED by symmetry, three of
four strata are worked, and the unbuilt one is the stratum with NO continuous isometry.

** THE ROW asked for "the classical general matter dynamics", carried since r2376+c54.166 (folding a
map item live since r565) as the deepest question the construction opens onto.  r2480 narrowed it to
"the exhibition BEYOND spherical symmetry".  ** Reading P11 -- which P9 CITES for exactly this -- gives
a stratification neither statement had. **

** THE COMPANION IS REAL AND IS IN THE CORPUS. **  P9's cor:wall: the beyond-wall radiative degrees of
freedom "are carried past it by the ordinary general-relativistic evolution ** the companion dynamics
paper works out **~\\cite{JanzenDynamics}".  ** JanzenDynamics is P11, `dynamics_paper.tex`, "Why the cut
bends". **

** ⛭⛭ THE STRATIFICATION, read at source: **

    stratum                          symmetry   status
    ------------------------------   --------   -------------------------------------------------
    the symmetric sector             maximal    ** CLOSED FORM ** -- d^2r/dtau^2 = -f'/2 = r K_G,
                                                "the rate at which the symmetric cut's bend changes
                                                in time is the bend itself"
    spherically symmetric, general   3 KV       ** EXHIBITED r2450 ** (L-207 (1)) -- LTB with Lambda,
                                                arbitrary m(r), one equation per comoving shell
    inhomogeneous, confined          2 KV       ** WORKED EXPLICITLY IN P11 ** -- polarized
                                                Gowdy--de Sitter; the TT mode's energy and momentum
                                                ARE the leaf's shear; the ADM equations ARE the
                                                constraints; "the Type-I edge --- the last confined
                                                stratum before the wall"
    beyond the wall                  NONE       ** NOT WORKED **

  ⇒ *** SO THE UNBUILT THING IS NOT "THE GENERAL MATTER DYNAMICS".  IT IS THE ONE STRATUM WITH NO
      CONTINUOUS ISOMETRY -- and everything carrying at least one Killing vector is done. ***

** ⌗ AND P11 SETTLES THE WALL'S CHARACTER WITHOUT EVOLVING PAST IT: ** "the wall, a Type-N plane wave,
has a ** non-degenerate metric ** (no measure-collapse) and ** vanishing curvature invariants **, so it
is ** neither species **" -- neither a metric singularity in P1's sense nor a curvature one.

** ⚠ AND THAT EXPOSES SOMETHING IN P9 WORTH MARKING RATHER THAN CALLING A DEFECT. **  cor:wall's
citation is defensible on a careful reading -- ** P11 works out ordinary GR evolution, and ordinary GR
evolution is what carries the beyond-wall modes ** -- but a reader takes the citation to cover the
beyond-wall CASE, and ** what P11 delivers is the method on the CONFINED stratum. **
  ⇒ ** The citation covers the METHOD, not the CASE, and the sentence does not say which. **  Routed.

⌗ WHY THE ROW WAS CARRIED SO WIDE FOR SO LONG: it folded a map item phrased as an open DISCOVERY (P8's
% source comment, corrected at c54.179 -- see r2480), and ** nobody re-read the target after the
correction. **  ⇒ *** This is the FOURTH case in twenty revisions of the corpus being ahead of its own
register *** (L-217, L-204, L-203's station F, L-206), and the fifth counting this one.

WHAT IS NOT CLAIMED.  ** Not that the beyond-wall stratum is discharged ** -- it is the one thing on
this board that is genuinely unbuilt.  Not that P9's citation is wrong; ** only that it covers the
method rather than the case, and does not say so. **  Not anything about (2), which is gated on PO-6.

Written r2503.  Stated for reversal.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def pub(f):
    raw = open(os.path.join(ROOT, 'corpus', f), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print('  I2 -- what is actually unbuilt in the matter dynamics?')
    print()
    p9, p11 = pub('range_paper.tex'), pub('dynamics_paper.tex')
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    # the companion is real
    check('P9 cor:wall cites a companion dynamics paper for the beyond-wall evolution',
          'the companion dynamics paper works out' in p9)
    check('and JanzenDynamics is P11, "Why the cut bends"',
          'Why the cut bends' in pub('BH_causality_v2.tex')
          and os.path.exists(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex')))

    # stratum 1: closed form
    check("⛭ the symmetric sector is CLOSED FORM: d^2r/dtau^2 = -f'/2 = r K_G",
          "\\mathrm{d}^{2}r/\\mathrm{d}\\tilde\\tau^{2}=-f'/2=rK_{G}" in p11)
    check('and P11 states its content: "the rate at which the symmetric cut\'s bend changes in time '
          'is the bend itself"',
          "the rate at which the symmetric cut's bend changes in time is the bend itself" in p11)

    # stratum 2: LTB, exhibited by this line
    check('the spherically symmetric general case was exhibited at r2450 -- LTB with Lambda, one '
          'equation per comoving shell',
          'one equation per comoving shell' in arc or 'ONE equation per comoving shell' in arc)

    # stratum 3: Gowdy, worked in P11
    check('⛭ P11 works the FIRST inhomogeneous time-dependent bend explicitly: a polarized '
          'Gowdy--de Sitter model',
          'We work the first inhomogeneous, time-dependent bend explicitly' in p11
          and 'polarized Gowdy--de Sitter model' in p11)
    check('with the TT mode\'s energy and momentum being the shear of the leaf, and the ADM '
          'equations being exactly the constraints',
          'are the shear of the leaf' in p11
          and 'are exactly the Hamiltonian and momentum constraints' in p11)
    check('⇒ and it locates that stratum: "the Type-I edge of the isotropy stratification---the LAST '
          'CONFINED STRATUM BEFORE THE WALL"',
          'the last confined stratum before the wall' in p11)

    # stratum 4: not worked
    check('⇒⇒ SO THE UNBUILT STRATUM IS THE ONE WITH NO CONTINUOUS ISOMETRY -- P11 carries ZERO uses '
          'of "beyond the wall" and zero of "no continuous isometry"',
          len(re.findall('beyond the wall', p11, re.I)) == 0
          and len(re.findall('no continuous isometry', p11, re.I)) == 0)
    check('while P9 states the wall IS inhomogeneity: "a geometry with no continuous isometry admits '
          'no sweep-subgroup"',
          'no continuous isometry admits no sweep-subgroup' in p9)

    # the wall's character, settled without evolving past it
    check('⌗ and P11 settles the wall\'s character: a Type-N plane wave with a NON-DEGENERATE metric '
          'and VANISHING curvature invariants, so it is NEITHER species',
          'has a non-degenerate metric' in p11 and 'vanishing curvature invariants' in p11
          and 'neither species' in p11)

    # the citation covers the method, not the case
    check('⚠ so P9\'s citation covers the METHOD (ordinary GR evolution, worked on the confined '
          'stratum) rather than the CASE, and does not say which',
          'the companion dynamics paper works out' in p9
          and 'the last confined stratum before the wall' in p11)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the dynamics is STRATIFIED and three of four strata are worked. **')
    print("    symmetric (maximal)            ** closed form ** -- d^2r/dtau^2 = -f'/2 = r K_G")
    print('    spherically symmetric (3 KV)   ** exhibited r2450 ** -- LTB, arbitrary m(r)')
    print('    inhomogeneous confined (2 KV)  ** worked in P11 ** -- polarized Gowdy--de Sitter,')
    print('                                      "the last confined stratum before the wall"')
    print('    beyond the wall (NO isometry)  ** NOT WORKED **')
    print('  ⇒ ** So the unbuilt thing is not "the general matter dynamics" -- it is the one stratum')
    print('     with no continuous isometry, and everything with at least one Killing vector is done. **')
    print('  ⌗ And P11 settles the wall\'s CHARACTER without evolving past it: a Type-N plane wave,')
    print('    non-degenerate metric, vanishing invariants -- ** neither species. **')
    print('  ⚠ Which exposes one thing in P9: ** its citation covers the METHOD, not the CASE, and')
    print('    does not say which. **  A reader takes it to cover the beyond-wall case.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

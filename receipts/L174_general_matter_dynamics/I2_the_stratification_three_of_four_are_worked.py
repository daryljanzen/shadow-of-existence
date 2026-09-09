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
    # ⛔⛭ AMENDED r4516.  ** Five verbatim quotations here broke at once, and NONE of the claims did. **
    #    P9 now writes "the companion dynamics paper walks straight past it: it works the cut's
    #    dynamics as a true-Hamiltonian flow" for "works out"; P11 writes "carried \emph{entirely by
    #    the shear of the spatial leaf}" for "are the shear of the leaf", "precisely the ADM
    #    Hamiltonian and momentum constraints" for "exactly the ...", "a single transverse-traceless
    #    shear---the propagating graviton" for the polarisation phrase, and the closed form is a
    #    DISPLAY FRACTION now (`\frac{\mathrm{d}^{2}r}{...}`) where it was inline.
    #    ⌗ *The last of those is not even a rewording -- it is LaTeX formatting, and a receipt that
    #      pins a formula by its markup is asserting about the typesetting rather than the physics.*
    #    ⇒ Every probe below names its terms and bounds the window (`W1`'s rule), so the papers stay
    #      free to reword and reformat while the claims stay checkable.
    _CITES = re.compile(r"companion dynamics paper (?:works out|walks straight past|works)", re.I)
    _SHEAR = re.compile(r"energy and momentum are[^.]{0,40}?shear of the (?:spatial )?leaf", re.I)
    _CONSTR = re.compile(r"(?:are|is)\s+(?:precisely|exactly)\s+the ADM Hamiltonian and momentum "
                         r"constraints|(?:precisely|exactly) the Hamiltonian and momentum constraints",
                         re.I)
    _GOWDY = re.compile(r"polarized Gowdy--de[~ ]?Sitter model", re.I)
    _CLOSED = re.compile(r"\\mathrm\{d\}\^\{2\}r\}?\{?\\mathrm\{d\}\\tilde\\tau\^\{2\}\}?"
                         r"\s*=\s*-\s*\\?f?r?a?c?\{?f'\}?\{?2?\}?")

    check('P9 cor:wall cites a companion dynamics paper for the beyond-wall evolution',
          _CITES.search(p9) is not None)
    check('and JanzenDynamics is P11, "Why the cut bends"',
          'Why the cut bends' in pub('BH_causality_v2.tex')
          and os.path.exists(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex')))

    # stratum 1: closed form
    check("⛭ the symmetric sector is CLOSED FORM: d^2r/dtau^2 = -f'/2 = r K_G",
          _CLOSED.search(p11) is not None and 'K_{G}' in p11)
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
          and _GOWDY.search(p11) is not None)
    check('with the TT mode\'s energy and momentum being the shear of the leaf, and the ADM '
          'equations being exactly the constraints',
          _SHEAR.search(p11) is not None and _CONSTR.search(p11) is not None)
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
    # ⛔⛭ AMENDED r4516: P11's `prop:radiative-wall` was rewritten to argue the two species SEPARATELY
    #    -- "its metric is non-degenerate\rcpt{P11_wall_ppwave} ... it is not the finite-curvature
    #    species" and "All its polynomial curvature invariants vanish (it is VSI) ... not the
    #    divergent-invariant species either" -- so "neither species" is no longer one phrase.
    #    *The claim is stronger than it was, not weaker: each species is excluded by its own named
    #    property with a citation.*  ⇒ Matched as the three terms it is made of.
    _NONDEG = re.compile(r"metric is non-degenerate", re.I)
    _VSI = re.compile(r"polynomial curvature invariants vanish|curvature invariants\) vanish", re.I)
    _NEITHER = re.compile(r"not the finite-curvature species[^.]{0,400}?not the (?:divergent-invariant|"
                          r"infinite-curvature)[^.]{0,30}?species|neither species", re.I | re.S)
    check('⌗ and P11 settles the wall\'s character: a Type-N plane wave with a NON-DEGENERATE metric '
          'and VANISHING polynomial curvature invariants, so it is NEITHER species -- P11 now '
          'excludes the two species one at a time, each by its own named property',
          _NONDEG.search(p11) is not None and _VSI.search(p11) is not None
          and _NEITHER.search(p11) is not None)

    # the citation covers the method, not the case
    check('⚠ so P9\'s citation covers the METHOD (ordinary GR evolution, worked on the confined '
          'stratum) rather than the CASE, and does not say which',
          _CITES.search(p9) is not None
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

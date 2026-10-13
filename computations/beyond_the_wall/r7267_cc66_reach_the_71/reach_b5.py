#!/usr/bin/env python3
"""
`r7283` RULING ③ BATCH FIVE — **THE FIVE HELD ROWS, READ AT THEIR OWN LOCI AND ALL FIVE TAKEN.
⚠ AND TWO THINGS THE RULING DID NOT EXPECT: THE LOCI ARE IN FOUR PAPERS, AND NOT ONE OF THE FOUR
`lie_g` ROWS IS A METRIC CLAIM AT ALL.**

`r7283` ruling ③: *"do not CHOOSE one. READ which one the paper states at the row's own locus...
And if the paper states NO metric at that locus, the blocker is a GAP IN THE PAPER."*

  ⓵ `P11` -> `matter_sector_paper.tex`:   `su(3)` is not a subalgebra of `so(5,1)`
  ⓶ `B1`, `B42` -> `boundary_paper.tex`:  the parity is in the DISCRETE coset `O(5,1)\\SO_0(5,1)`
  ⓷ `B39` -> `geometric_core_paper.tex`:  the absolute fixes the group; the polar cut is `dS_4`
  ⓸ `B11` -> `janzen_circle_v3.tex`:      the three loci are `f = 0, 1, 2`

⚠ ⛭⛭⛭ ** THE RULING ASKED WHICH METRIC THE PAPER STATES, AND THE ANSWER IS THAT FOUR OF THE FIVE
   ROWS DO NOT WANT ONE. **  *Three are statements about which GROUPS exist -- a subalgebra
containment, a component of an orthogonal group, the stabiliser of a quadric -- and `lie_g` tests
whether a VECTOR FIELD is Killing for a METRIC.*  *** A change of inputs cannot repair a change
of kind, so no input to `lie_g` could ever have reached them and the `INPUTS` classification is
refuted for all four. ***
  ⇒ My hold code `GEOMETRY-NOT-RECORDED` is **WITHDRAWN** and replaced by
  `FUNCTION-IS-THE-WRONG-KIND`.  ** That is a reclassification of the BACKLOG and not a hold on
  the row: all five rows are COMPUTED here, exactly, which is what backs it. **

⌗ ** AND THE GAP BRANCH DOES NOT FIRE ANYWHERE. **  *Every one of the five loci states what its
row needs, in one sentence, in the paper where the literal is pinned.  The defect was mine and
the backlog's, never the papers'.*

⌗ *`B11` is the one that lands as an ordinary `INPUTS` row: `character(s2)` is exactly the right
kind, and `character(1-f)` at the paper's own `f = 0, 1, 2` returns three DISTINCT characters.
Its code `OBJECTS-NOT-RECORDED` was right -- the objects were recorded, in a different paper
from the one I looked in.*

WHAT IS NOT CLAIMED.  ** Not that `janzen_circle_v3`'s two triples are one structure ** -- the
paper declines that in its own voice and nothing here supplies a derivation.  ** Not the paper's
index ordering for the polar signature ** -- it writes `(1,4)`, this computes four positive and
one negative eigenvalue, and the count is reported as computed.  ** Not that `su(3)` fails on
dimension ** -- `so(5)` has `10` and `su(3)` has `8`, so the obstruction computed is the ROOT
SYSTEM and not a count.  ** Not that any pin moves. **

Run: python3 reach_b5.py            (writes REACHED_B5.tsv)
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import groups_and_characters as GC                                 # noqa: E402

OUT = os.path.join(HERE, 'REACHED_B5.tsv')

B_ = 'receipts/L221_the_bridge/'
R_ = 'receipts/L204_physics_reach/'
A2M = 'beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py'
L104 = 'baryon_edge/L104w_the_excentre_trichotomy.py'

BOUNDARY = 'corpus/boundary_paper.tex'
MATTER = 'corpus/matter_sector_paper.tex'
CORE = 'corpus/geometric_core_paper.tex'
CIRCLE = 'corpus/janzen_circle_v3.tex'

WRONG_KIND = 'FUNCTION-IS-THE-WRONG-KIND'


def _su3_detail():
    return (f'su(3) is compact so any embedding lands in a maximal compact subalgebra of '
            f'so(5,1), which is so(5) of dimension {GC.so_dimension((1,)*5)}; so(5) is B2, '
            f'whose {len(GC.roots("B2"))} roots fall into TWO length classes of four, and an A2 '
            f'needs SIX roots of one length -- contains_A2(B2) is '
            f'{GC.contains_A2("B2")}. One dimension up so(6) is D3, '
            f'{len(GC.roots("D3"))} roots all of one length, and contains_A2(D3) is '
            f'{GC.contains_A2("D3")}')


def _circle_detail():
    return (f'the orientation parity preserves eta with det -1, while all '
            f'{len(GC.so_generators((-1,1,1,1,1,1)))} generators of so(5,1) are TRACELESS, so '
            f'det exp(tX) = exp(t tr X) = 1 for every t and no element of the det = -1 coset '
            f'lies on a one-parameter subgroup; the (x4,x5) rotation generator exponentiates '
            f'to a genuine circle of period 2 pi inside the identity component')


def _absolute_detail():
    pos, neg, norm = GC.polar_signature(GC.substrate_point())
    cpos, cneg, cnorm = GC.polar_signature(GC.inside_the_cone())
    return (f'the stabiliser of the absolute eta(X,X) = 0 has dimension '
            f'{GC.isometry_dimension_of_the_absolute()}; a substrate point with eta(P,P) = '
            f'{norm} has polar signature ({pos},{neg}), Lorentzian, whose isometry algebra has '
            f'dimension {GC.so_dimension((-1,1,1,1,1))}; a point inside the cone with '
            f'eta(P,P) = {cnorm} has polar signature ({cpos},{cneg}), Riemannian, and is no '
            f'dS_4 at all')


def _character_detail():
    a = GC.characters_at(GC.THREE_LOCI)
    b = GC.characters_at(GC.EQUALLY_SPACED_CONVERSE)
    return (f'character(1-f) at the paper\'s own f = 0, 1, 2 returns {a}, three DISTINCT '
            f'characters; at three equally spaced f = 0, 1/2, 1 it returns {b}, only '
            f'{len(set(b))} distinct, so `the three critical loci are the three causal '
            f'characters` is a fact about those three values of f')


ROWS = [
    (R_ + 'P11_CR_fixes_the_place_not_the_couplings.py',
     'not a continuous substrate isometry', A2M, 'lie_g', WRONG_KIND, MATTER,
     'su(3) is not a subalgebra of so(5,1), structurally -- so the Standard Model gauge group '
     'is not a continuous substrate isometry',
     GC.su3_is_not_in_so51,
     'ask the same containment ONE DIMENSION UP, in so(6), which is a change of the form and '
     'nothing else',
     GC.su3_containment_under_the_dimension_edit, _su3_detail),

    (B_ + 'B1_the_index_argument_stops_where_a_mod_two_index_begins.py',
     'no such circle action and so no trigger', A2M, 'lie_g', WRONG_KIND, BOUNDARY,
     'the gravitational handedness is carried by the discrete orientation parity '
     'O(5,1) minus SO_0(5,1), and a circle action needs a positive-dimensional CONNECTED group',
     GC.every_one_parameter_subgroup_has_determinant_one,
     'ask the same of a positive-dimensional CONNECTED subgroup -- the (x4,x5) rotation -- '
     'which is where the boundary paper says the trigger does live',
     GC.no_circle_under_the_connected_edit, _circle_detail),

    (B_ + 'B42_the_route_was_taken_and_p14_is_the_work.py',
     'no such circle action and so no trigger', A2M, 'lie_g', WRONG_KIND, BOUNDARY,
     'the gravitational handedness is carried by the discrete orientation parity '
     'O(5,1) minus SO_0(5,1), and a circle action needs a positive-dimensional CONNECTED group',
     GC.every_one_parameter_subgroup_has_determinant_one,
     'ask the same of a positive-dimensional CONNECTED subgroup -- the (x4,x5) rotation -- '
     'which is where the boundary paper says the trigger does live',
     GC.no_circle_under_the_connected_edit, _circle_detail),

    (B_ + 'B39_the_substrate_does_carry_compact_su2.py',
     'isometry group being fixed by the absolute', A2M, 'lie_g', WRONG_KIND, CORE,
     'the absolute is the quadric eta(X,X) = 0, and a substrate point\'s polar hyperplane cuts '
     'a totally geodesic dS_4 of isometry SO(4,1), a sweep-subgroup of the substrate\'s SO(5,1)',
     GC.polar_cut_is_dS4,
     'take a point INSIDE the cone instead of on the substrate, so its polar hyperplane is '
     'Riemannian and the cut is not a dS_4',
     GC.polar_cut_is_dS4_inside_the_cone, _absolute_detail),

    (B_ + 'B11_three_triples_two_identifications.py',
     'the three critical loci are the three causal characters', L104, 'character', 'INPUTS',
     CIRCLE,
     'the three critical loci sit at f = 0 (the seam), f = 1 (the turnaround) and f = 2 (the '
     'interior Euclidean null), where 1-f takes the values +1, 0, -1',
     GC.three_loci_are_three_characters,
     'ask the same of three EQUALLY SPACED values of f that are not the paper\'s -- 0, 1/2, 1 '
     '-- so the three loci no longer carry three distinct characters',
     GC.three_characters_at_equally_spaced, _character_detail),
]


# ⚠ ** NO PREDICATE SLOT IS A LAMBDA, and that is not style. **  The first draft of this file
#   wrote a converse as `lambda: not GC.<fn>` WITHOUT the call, which evaluates `not <function>`
#   -> always `False`, and `False` is exactly what a converse must return -- so the row passed
#   for the wrong reason.  *** A named function makes a missing call a `TypeError`. ***
for _r in ROWS:
    for _slot in (_r[7], _r[9]):
        assert getattr(_slot, '__name__', '<lambda>') != '<lambda>', _r[0]
        assert isinstance(_slot(), bool), _r[0]


def main():
    print()
    print('  r7283 ruling (3) batch five -- 5 held rows read at their own loci, 5 taken')
    print()
    bad, lines = [], [
        '# r7283 RULING (3) BATCH FIVE -- the five rows held at r7275/r7281 for want of a',
        '# geometry, read at their OWN loci in FOUR different papers and all five taken.  Per',
        '# row: the paper, what it states at the locus, the predicate, and the reachable',
        '# converse.  `code` is the classification AFTER the read: four of the five are',
        '# FUNCTION-IS-THE-WRONG-KIND, because `lie_g` is a metric Killing test and those four',
        '# claims are about which GROUPS exist -- which no change of inputs can repair.',
        '\t'.join(('stem', 'literal', 'module', 'function', 'code', 'paper', 'paper_states',
                   'claim', 'converse_edit', 'converse', 'computed'))]
    for (stem, lit, mod, fn, code, paper, states, claim, cedit, conv, detail) in ROWS:
        c, v = bool(claim()), bool(conv())
        d = detail()
        ok = c and not v
        if not ok:
            bad.append(stem)
        print(f"    {'OK  ' if ok else 'FAIL'}  {os.path.basename(stem)[:34]:<34} "
              f"{code:<27} claim={c} converse={v}")
        print(f"            {paper.split('/')[-1]}: {states[:96]}")
        print(f"            {d[:150]}")
        lines.append('\t'.join((stem, lit, mod, fn, code, paper, states,
                                'TRUE' if c else 'FALSE', cedit,
                                'TRUE' if v else 'FALSE', d)))
    body = '\n'.join(lines) + '\n'
    open(OUT, 'w', encoding='utf-8').write(body)
    print()
    print(f'    REACHED_B5.tsv  {len(ROWS)} rows   '
          f'digest {hashlib.sha1(body.encode()).hexdigest()[:16]}')
    if bad:
        print(f'    {len(bad)} row(s) NOT reached')
        return 1
    print(f'    ** {len(ROWS)} taken, every predicate TRUE on the claim and FALSE on its '
          f'recorded converse. **')
    print('    ** AND THE RULING ASKED WHICH METRIC THE PAPER STATES: four of the five rows do')
    print('       not want one.  Three are statements about which GROUPS exist and `lie_g` is a')
    print('       metric Killing test, so a change of inputs could never have reached them --')
    print('       a change of INPUTS cannot repair a change of KIND.  GEOMETRY-NOT-RECORDED is')
    print('       withdrawn for all four in favour of FUNCTION-IS-THE-WRONG-KIND, which is a')
    print('       reclassification of the backlog backed by the five computations above. **')
    print('    ** AND THE LOCI ARE IN FOUR PAPERS, NOT ONE: the geometric core carries exactly')
    print('       one of the five.  The gap branch of the ruling fires nowhere. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

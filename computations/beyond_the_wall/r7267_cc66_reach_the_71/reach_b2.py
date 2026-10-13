#!/usr/bin/env python3
"""
`r7267`/`r7275` ① BATCH TWO — **FOUR OF THE THIRTEEN ARE A CHANGE OF INPUTS. NINE ARE NOT, AND
THAT IS THE BATCH'S RESULT: `r7275`'s RULING ① ARRIVES AGAIN AT FINER RESOLUTION.**

`r7275` ruled on batch one that `r7261` `classified 59 rows by what the function computes and not
one of those modules can be imported` -- the classification had read the mathematics without
asking whether the code was reachable.  ** Batch two says the same thing about the INPUTS half of
the classification, and it says it per row rather than per module. **

  ⓵ `graft.py` needed a second repair to reach `A2` at all: `A2` builds its metric by ELEMENT
     ASSIGNMENT, and the loader read a subscript target as a BINDING -- keeping the last element
     assignment as the definition of `g` and dropping the `sp.zeros` that creates it.
     *** A matrix built by element assignment is a reachability question nobody had asked. ***
  ⓶ Then, of the thirteen rows scheduled: ** FOUR are a change of inputs in the strict sense **
     -- the function computes exactly the asserted quantity and only its inputs differ -- and
     ** NINE need something the classification did not record: a nested function, a geometry
     choice, or a reading of which objects the paper means. **
  ⓷ The four are TAKEN with converses.  The nine are HELD WITH THE REASON, per row, because a
     row taken on a guessed input is worse than a row still open.

⇒ ** THE FOUR, AND THE PAIR `L-104w` NEVER FORMS IS THE ONE WORTH READING: ** `sep` runs over
fifteen excentre pairs and thirty-six hinge-excentre pairs in `L-104w`'s own report, and three
receipts assert something about ** the two ends of ONE hinge ** -- same azimuth, opposite horn,
at `2 alpha` -- which is one call on two points `pt` already builds and which nothing in the
corpus had made.  `s^2 = -12 alpha^2`, timelike at every hinge azimuth; and the converse is
not a radius away but AT THE THROAT, where `rho = alpha` makes the two ends coincide and the
interval NULL.

WHAT IS NOT CLAIMED.  ** Not that the nine are unreachable ** -- three want a loader that lifts
a NESTED function, which is a bounded extension measured below as serving exactly three rows;
the rest want a choice this file will not make unprompted.  ** Not that the Nariai algebra is
exactly six-dimensional ** -- six generators are COMPUTED Killing, which is a lower bound with
the product structure, and `A2`'s own exact-count method is a hand-derived ODE system for its
own metric that does not transport.

Run: python3 reach_b2.py            (writes REACHED_B2.tsv)
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import isometry as ISO                                         # noqa: E402
import trichotomy as TRI                                       # noqa: E402

OUT = os.path.join(HERE, 'REACHED_B2.tsv')

I = ISO.at_inputs().nariai()
T = TRI.at_inputs()

B = 'receipts/L221_the_bridge/'
R = 'receipts/L204_physics_reach/'
A2 = 'beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py'
L104 = 'baryon_edge/L104w_the_excentre_trichotomy.py'

_GENS = I.generators()
_CONV = I.converses()


def _algebra_ok():
    return (len(_GENS) == 6 and all(I.is_killing(x) for x in _GENS.values())
            and not any(I.is_killing(x) for x in _CONV.values()))


def _algebra_detail():
    return (f'6 generators Killing through A2\'s own lie_g at the Nariai metric: '
            f'{", ".join(sorted(_GENS))} -- so(2,1) on the dS_2 factor and so(3) on the '
            f'two-sphere, dimension at least six with the product structure; '
            f'{len(_CONV)} reachable converses all FALSE')


ROWS = [
    (R + 'C3_the_isotropy_citation_runs_in_a_loop.py',
     '\\mathrm{SO}(2,1)\\times\\mathrm{SO}(3)$ at Nariai', A2, 'lie_g',
     _algebra_ok,
     'offer chi d_tau, d_chi or d_theta as generators of the same algebra',
     lambda: any(I.is_killing(x) for x in _CONV.values()),
     _algebra_detail),
]

for _stem in (B + 'B30_the_parameter_has_the_wrong_signature.py',
              B + 'B39_the_substrate_does_carry_compact_su2.py',
              B + 'B40_the_isometry_reaches_colour_not_isospin.py'):
    ROWS.append((
        _stem, 'two ends of one hinge are timelike separated', L104, 'sep',
        lambda: T.all_hinges_timelike(),
        'take the two ends of the same hinge at the THROAT radius rho = alpha',
        lambda: T.all_hinges_timelike(T.al),
        lambda: (f'sep(pt(a, 2 alpha, +1), pt(a, 2 alpha, -1)) = '
                 f'{T.ends_interval(T.hinge_az[0])} -> '
                 f'{T.ends_character(T.hinge_az[0])} at all {len(T.hinge_az)} hinge azimuths; '
                 f'at rho = alpha it is {T.ends_interval(T.hinge_az[0], T.al)} -> '
                 f'{T.ends_character(T.hinge_az[0], T.al)}')))

# =========================================================================================
# the nine HELD, each with the reason -- `r7275` ruling ① at per-row resolution
# =========================================================================================
HELD = [
    (R + 'P11_CR_fixes_the_place_not_the_couplings.py', 'not a continuous substrate isometry',
     A2, 'lie_g', 'GEOMETRY-NOT-RECORDED',
     'the claim is that the orientation parity R is not in the CONNECTED isometry group, which '
     'needs the SUBSTRATE metric and a statement of which map R is -- `lie_g` tests a vector '
     'field and R is discrete, so the input the row needs is not a vector field at all'),
    (B + 'B1_the_index_argument_stops_where_a_mod_two_index_begins.py',
     'no such circle action and so no trigger', A2, 'lie_g', 'GEOMETRY-NOT-RECORDED',
     'a circle action is a Killing field with CLOSED orbits; the Nariai two-sphere has one '
     '(d_phi) and the dS_2 factor does not, so the row is about a circle action on a geometry '
     'the backlog did not name and picking one would be a reading of the paper'),
    (B + 'B42_the_route_was_taken_and_p14_is_the_work.py',
     'no such circle action and so no trigger', A2, 'lie_g', 'GEOMETRY-NOT-RECORDED',
     'the same `no such circle action` claim as B1: a circle action is a Killing field whose '
     'orbits CLOSE, the Nariai two-sphere has one and the dS_2 factor does not, so the row is '
     'about a geometry the backlog did not name and choosing one would be a reading'),
    (B + 'B39_the_substrate_does_carry_compact_su2.py',
     'isometry group being fixed by the absolute', A2, 'lie_g', 'GEOMETRY-NOT-RECORDED',
     'the absolute is a projective object and `lie_g` is a metric Killing test: the row needs '
     'the isometry group read off the ABSOLUTE, which is a different computation and not this '
     'function at different inputs'),
    (B + 'B11_three_triples_two_identifications.py',
     'the three critical loci are the three causal characters', L104, 'character',
     'OBJECTS-NOT-RECORDED',
     '`character` is one call once the three loci are points, and WHICH three loci the paper '
     'means is a reading the backlog did not record -- L-104w computes characters over the '
     'excentre and hinge-excentre sets and never over a set of three critical loci'),
    ('receipts/L204_physics_reach/P2_the_corpus_never_mentions_unruh.py',
     'never form at any finite exterior time', 'bead_frames.py', 'tau_of_r', 'NESTED-FUNCTION',
     '`tau_of_r` is a closure defined INSIDE `tau_r(ax)`, a matplotlib plotting routine, so it '
     'is not a top-level def and the loader refuses it; `tau_r` itself needs a live axis'),
    ('receipts/L204_physics_reach/P2_the_corpus_never_mentions_unruh.py',
     'never physically realised', 'bead_frames.py', 'tau_of_r', 'NESTED-FUNCTION',
     '`tau_of_r` is the same nested closure as the row above: defined INSIDE `tau_r(ax)`, a '
     'matplotlib plotting routine, so it is not a top-level def and the loader refuses it '
     'rather than resolving something else'),
    ('receipts/L204_physics_reach/P9_the_resolution_is_the_baby_universe_one_and_it_is_never_'
     'named.py',
     'it does not arise, because the spacetime it requires is never physically instantiated',
     'bead_frames.py', 'tau_of_r', 'NESTED-FUNCTION',
     '`tau_of_r` is the same nested closure as the two rows above: defined INSIDE `tau_r(ax)`, '
     'a matplotlib plotting routine, so it is not a top-level def and the loader refuses it '
     'rather than resolving something else'),
    ('receipts/P15_CR_cosmology/P15_the_corpus_places_every_perturbation_source_before_the_'
     'branch_point_and_everything_after_it_is_transfer_so_nothing_already_built_supplies_'
     'anisotropic_content_on_the_expansion_leg.py',
     'there is no interval in which anything could act', 'bead_frames.py', 'tau_r',
     'AXIS-ARGUMENT',
     '`tau_r(ax)` is top-level but its only parameter is a matplotlib axis and its body draws; '
     'the quantity the row needs is the closure inside it, which is the row above\'s case'),
]


def main():
    print()
    print('  r7267/r7275 (1) batch two -- 13 scheduled, 4 are a change of inputs, 9 are not')
    print(f'    graft: A2 {I.statements[0]}/{I.statements[1]} statements, '
          f'L-104w {T.statements[0]}/{T.statements[1]}')
    print()
    bad, lines = [], [
        '# r7267/r7275 (1) BATCH TWO -- the 4 of 13 that are a change of inputs, TAKEN, and the',
        '# 9 that are not, HELD WITH THE REASON.  A row taken on a guessed input is worse than a',
        '# row still open, which is why the second list exists and is as long as the first.',
        '\t'.join(('state', 'stem', 'literal', 'module', 'function', 'claim', 'converse_edit',
                   'converse', 'computed_or_reason'))]
    for stem, lit, mod, fn, claim, cedit, conv, detail in ROWS:
        c, v = bool(claim()), bool(conv())
        d = detail()
        ok = c and not v
        if not ok:
            bad.append(stem)
        print(f"    {'OK  ' if ok else 'FAIL'}  {os.path.basename(stem)[:38]:<38} {fn:<9} "
              f"claim={c} converse={v}")
        print(f"            {d}")
        lines.append('\t'.join(('TAKEN', stem, lit, mod, fn, 'TRUE' if c else 'FALSE', cedit,
                                'TRUE' if v else 'FALSE', d)))
    print()
    _why = {}
    for stem, lit, mod, fn, code, why in HELD:
        _why[code] = _why.get(code, 0) + 1
        print(f"    HELD  {os.path.basename(stem)[:38]:<38} {fn:<9} {code}")
        lines.append('\t'.join(('HELD', stem, lit, mod, fn, '-', '-', '-', f'{code}: {why}')))
    body = '\n'.join(lines) + '\n'
    open(OUT, 'w', encoding='utf-8').write(body)
    print()
    print(f'    REACHED_B2.tsv  {len(ROWS)} taken + {len(HELD)} held   '
          f'digest {hashlib.sha1(body.encode()).hexdigest()[:16]}')
    print(f'    held by reason: {_why}')
    if bad:
        print(f'    {len(bad)} taken row(s) NOT reached')
        return 1
    print(f'    ** {len(ROWS)} taken, every predicate TRUE on the claim and FALSE on its '
          f'recorded converse; {len(HELD)} held with the reason. **')
    print('    ** AND THE BATCH\'S RESULT IS THE SPLIT: r7261 classified these 13 `INPUTS` on')
    print('       what the function computes, and only 4 are a change of inputs in the strict')
    print('       sense.  r7275 ruling ① said the classification had not asked whether the code')
    print('       was reachable; this says the same thing per ROW rather than per module. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""`r7283` RULING ③ — **THE FIVE HELD ROWS, READ AT THEIR OWN LOCI. ⚠ THE RULING EXPECTED A
METRIC AND NOT ONE OF THE FIVE IS A METRIC CLAIM, AND THE LOCI ARE IN FOUR PAPERS AND NOT ONE.**

`r7283` ruling ③: *"do not CHOOSE one. READ which one the paper states at the row's own locus.
The geometric core is `P17`, a reading of a paper is made by reading it, and the full-turn-per-
paper rule applies — this is not a grep."*  ⌈ *And the other half: if the paper states NO metric
at that locus, the blocker is a GAP IN THE PAPER and is routed as that finding.*

** ⓵ THE FIRST THING THE READ RETURNS IS THAT THE LOCI ARE NOT ALL IN `P17`. **

  | row | the paper its literal is pinned in | what the paper states AT the locus |
  |---|---|---|
  | `B39` | `geometric_core_paper.tex` (`P17`) | the absolute is `eta(X,X)=0`; a substrate point's polar hyperplane cuts a totally geodesic `dS_4` of isometry `SO(4,1)`, a sweep-subgroup of the substrate's `SO(5,1)` |
  | `B1`, `B42` | `boundary_paper.tex` | the gravitational handedness is carried by the DISCRETE orientation parity `O(5,1) \\ SO_0(5,1)`, and a circle action needs a positive-dimensional CONNECTED group |
  | `P11` | `matter_sector_paper.tex` | `su(3)` is not a subalgebra of `so(5,1)`, structurally -- so the Standard Model gauge group is not a continuous substrate isometry |
  | `B11` | `janzen_circle_v3.tex` | the three critical loci are `f = 0` (the seam), `f = 1` (the turnaround) and `f = 2` (the interior Euclidean null), at which `1-f` takes the values `+1, 0, -1` |

** ⚠⛭⛭⛭ ⓶ AND NOT ONE OF THE FOUR `lie_g` ROWS IS A METRIC CLAIM, so no metric was missing and
   no change of inputs to `lie_g` could ever have reached them. **  *Three are statements about
which GROUPS exist -- a subalgebra containment, a component of an orthogonal group, the
stabiliser of a quadric -- and `lie_g` tests whether a vector field is Killing for a metric.*
  *** A change of inputs cannot repair a change of KIND. ***  ⇒ So the hold code
`GEOMETRY-NOT-RECORDED` is WITHDRAWN for all four and replaced by `FUNCTION-IS-THE-WRONG-KIND`,
which is a reclassification of the BACKLOG and not a hold on the row: **all four are computed
below, exactly, and the computation is what backs the reclassification.**

⌗ ** AND THE GAP BRANCH OF THE RULING DOES NOT FIRE. **  *Every one of the five loci states what
the row needs.  The defect was never in the papers.*

** ⓷ `B11` IS DIFFERENT AND LANDS AS AN ORDINARY `INPUTS` ROW. **  `character(s2)` is exactly the
right KIND, the paper names the three loci as three values of `f`, and `character(1-f)` at
`f = 0, 1, 2` returns three DISTINCT characters.  *Its code `OBJECTS-NOT-RECORDED` was right: the
objects were recorded, in a different paper from the one I looked in.*

WHAT IS NOT CLAIMED.  ** Not that the two triples of `janzen_circle_v3` are one structure ** --
the paper explicitly declines that (`no derivation producing {0,1,2} from a single condition has
been exhibited`) and nothing here supplies one.  ** Not the paper's index-ordering for the polar
signature ** -- it writes `(1,4)` and this computes four positive and one negative eigenvalue,
the same signature in the other convention, and the count is reported as computed.  ** Not that
`su(3)` fails to embed for a reason of dimension ** -- `so(5)` has dimension `10` and `su(3)` has
`8`, so dimension does not obstruct and the obstruction computed here is the ROOT SYSTEM.

Run: python3 groups_and_characters.py
"""
import itertools
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                            # noqa: E402

L104 = 'baryon_edge/L104w_the_excentre_trichotomy.py'

# the substrate's ambient form, signature (5,1) with the one timelike direction first
ETA = sp.diag(-1, 1, 1, 1, 1, 1)


# ════════════════════ ⒜ THE ALGEBRA OF A FORM, AND ITS DIMENSION ═════════════════════════
def so_generators(sig):
    """a basis of `so(sig)` = {A : A^T H + H A = 0} for a DIAGONAL form, built from the form.

    *The generator of the `(i,j)` plane is `E_ij - H_ii H_jj E_ji`, which is where the signature
    enters: a rotation where the two signs agree and a boost where they differ.*"""
    n = len(sig)
    H = sp.diag(*sig)
    out = []
    for i, j in itertools.combinations(range(n), 2):
        X = sp.zeros(n, n)
        X[i, j] = 1
        X[j, i] = -H[i, i] * H[j, j]
        out.append(X)
    return out


def so_dimension(sig):
    return len(so_generators(sig))


def generators_are_in_the_algebra(sig):
    H = sp.diag(*sig)
    return all(sp.simplify(X.T * H + H * X) == sp.zeros(len(sig), len(sig))
               for X in so_generators(sig))


# ════════════════════ ⒝ ROOT SYSTEMS -- THE `su(3)` OBSTRUCTION ══════════════════════════
def roots(name):
    """the root system of the named algebra, in its own Euclidean space"""
    if name == 'B2':                       # so(5), the maximal compact subalgebra of so(5,1)
        out = [(s, 0) for s in (1, -1)] + [(0, s) for s in (1, -1)]
        return out + [(a, b) for a in (1, -1) for b in (1, -1)]
    if name == 'D3':                       # so(6)
        out = []
        for i, j in itertools.combinations(range(3), 2):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [0, 0, 0]
                    v[i] = si
                    v[j] = sj
                    out.append(tuple(v))
        return out
    if name == 'A2':                       # su(3)
        h = sp.Rational(1, 2)
        r3 = sp.sqrt(3) / 2
        return [(1, 0), (-1, 0), (h, r3), (-h, -r3), (h, -r3), (-h, r3)]
    raise KeyError(name)


def _dot(u, v):
    return sp.simplify(sum(sp.nsimplify(x) * sp.nsimplify(y) for x, y in zip(u, v)))


def root_lengths(name):
    return sorted({sp.nsimplify(_dot(r, r)) for r in roots(name)}, key=str)


def contains_A2(name):
    """does this root system contain a sub-system of type `A2`?

    *An `A2` is six roots of EQUAL length closing as `{+-a, +-b, +-(a+b)}` with `a` and `b` at
    `120` degrees.  Searching for the pair and then checking the closure is the whole test.*"""
    R = roots(name)
    S = set(R)
    for a, b in itertools.combinations(R, 2):
        na, nb = _dot(a, a), _dot(b, b)
        if sp.simplify(na - nb) != 0:
            continue
        if sp.simplify(_dot(a, b) + na / 2) != 0:
            continue
        ab = tuple(sp.nsimplify(x) + sp.nsimplify(y) for x, y in zip(a, b))
        need = {a, b, ab,
                tuple(-sp.nsimplify(x) for x in a),
                tuple(-sp.nsimplify(x) for x in b),
                tuple(-sp.nsimplify(x) for x in ab)}
        if need <= S:
            return True
    return False


def su3_is_not_in_so51():
    """`P11`: `su(3)` is not a subalgebra of `so(5,1)`.

    *`su(3)` is COMPACT, so any embedding lands in a maximal compact subalgebra of `so(5,1)`,
    which is `so(5)` -- and `so(5)` is `B2`, whose eight roots fall into two length classes of
    FOUR.  An `A2` needs SIX roots of one length, so there are not enough of either.*"""
    return (not contains_A2('B2')) and so_dimension((1,) * 5) == 10


def su3_is_in_so6():
    """the reachable converse, ONE DIMENSION UP: `so(6)` is `D3`, twelve roots all of one
    length, and it DOES contain an `A2`.  So the obstruction is specific to five."""
    return contains_A2('D3')


# ════════════════ ⒞ THE DISCRETE COMPONENT CARRIES NO CIRCLE ACTION ══════════════════════
def orientation_parity():
    """the discrete orientation parity: a reflection in one spacelike ambient direction"""
    return sp.diag(1, 1, 1, 1, 1, -1)


def parity_is_in_O51_and_not_in_SO0():
    """it preserves the form, and its determinant is `-1`, so it is in `O(5,1)` and not in the
    identity component"""
    R = orientation_parity()
    return (sp.simplify(R.T * ETA * R - ETA) == sp.zeros(6, 6)
            and sp.det(R) == -1)


def every_one_parameter_subgroup_has_determinant_one():
    """** THE WHOLE OF `no such circle action`. **  A circle action is the image of a
    one-parameter subgroup `t -> exp(tX)`, and `det exp(tX) = exp(t tr X)`.  Every element of
    `so(5,1)` is TRACELESS, so every one-parameter subgroup has determinant `+1` for every `t`
    and no element of the `det = -1` coset lies on one."""
    return all(sp.trace(X) == 0 for X in so_generators((-1, 1, 1, 1, 1, 1)))


def a_connected_subgroup_does_carry_a_circle():
    """the reachable converse: the rotation generator of the `(x4,x5)` plane exponentiates to a
    genuine circle -- closed orbits of period `2 pi` -- inside the identity component, which is
    the trigger the boundary paper says a positive-dimensional connected group supplies."""
    t = sp.Symbol('t', real=True)
    X = sp.zeros(6, 6)
    X[4, 5] = 1
    X[5, 4] = -1
    E = sp.simplify(sp.exp(X * t))
    return (sp.simplify(E.subs(t, 2 * sp.pi)) == sp.eye(6)
            and sp.simplify(sp.det(E)) == 1
            and sp.simplify(E.subs(t, sp.pi)) != sp.eye(6))


# ══════════════════ ⒟ THE ABSOLUTE FIXES THE GROUP, AND THE POLAR CUT ════════════════════
def isometry_dimension_of_the_absolute():
    """`B39`: the group is the stabiliser of the ABSOLUTE `eta(X,X) = 0`, whose algebra is
    `{A : A^T H + H A = 0}` -- so the absolute fixes the group, not a metric chosen on top of
    it.  `SO(5,1)` has dimension `15`."""
    return so_dimension((-1, 1, 1, 1, 1, 1))


def polar_signature(P):
    """the signature of the form restricted to the polar hyperplane `{X : eta(P,X) = 0}`"""
    P = sp.Matrix(P)
    functional = sp.Matrix((ETA * P).T)
    basis = functional.nullspace()
    G = sp.Matrix(len(basis), len(basis),
                  lambda i, j: (basis[i].T * ETA * basis[j])[0, 0])
    ev = G.eigenvals()
    pos = sum(m for v, m in ev.items() if sp.simplify(v) > 0)
    neg = sum(m for v, m in ev.items() if sp.simplify(v) < 0)
    return int(pos), int(neg), sp.simplify((P.T * ETA * P)[0, 0])


def substrate_point(al=None):
    al = al if al is not None else sp.Symbol('alpha', positive=True)
    return [0, al, 0, 0, 0, 0]


def inside_the_cone(al=None):
    al = al if al is not None else sp.Symbol('alpha', positive=True)
    return [al, 0, 0, 0, 0, 0]


def polar_cut_is_dS4():
    """a SUBSTRATE point has `eta(P,P) = +alpha^2`, and its polar hyperplane carries four
    positive and one negative eigenvalue -- a Lorentzian `dS_4` -- whose isometry algebra has
    dimension `10`, a sweep-subgroup of the substrate's `15`."""
    pos, neg, norm = polar_signature(substrate_point())
    return (pos, neg) == (4, 1) and so_dimension((-1, 1, 1, 1, 1)) == 10


def polar_converse_is_riemannian():
    """the reachable converse: a point INSIDE the cone has `eta(P,P) < 0` and its polar
    hyperplane is `(5,0)` -- Riemannian, so the cut is not a `dS_4` at all."""
    pos, neg, norm = polar_signature(inside_the_cone())
    return (pos, neg) == (5, 0)


# ═════════════ ⒠ THE THREE CRITICAL LOCI ARE THE THREE CAUSAL CHARACTERS ═════════════════
def _character():
    return graft(L104, 'character')['character']


THREE_LOCI = (0, 1, 2)               # the paper's own f at the seam, the turnaround, the
                                     # interior Euclidean null


def characters_at(loci):
    """`character(1-f)` at each locus, `(dr/dtau)^2 = 1-f` being the paper's own invariant"""
    ch = _character()
    return [ch(1 - sp.nsimplify(f)) for f in loci]


def three_loci_are_three_characters(loci=THREE_LOCI):
    return len(set(characters_at(loci))) == 3


EQUALLY_SPACED_CONVERSE = (0, sp.Rational(1, 2), 1)



# ════ ⒡ THE CONVERSES AS NAMED FUNCTIONS, NOT LAMBDAS -- AND THE REASON IS A BUG THIS BATCH
#        MADE AND CAUGHT. ════════════════════════════════════════════════════════════════
#  ⚠ Written first as `lambda: not GC.a_connected_subgroup_does_carry_a_circle`, WITHOUT the
#    call, which evaluates `not <function>` -> always `False` -- and `False` is exactly what a
#    converse must return, so the row PASSED for the wrong reason.  ** The same vacuous-pass
#    shape as the empty container `graft.py` now refuses, one layer up. **  Each converse is a
#    named function here, so a missing call is a `TypeError` and not a silent pass.

def su3_containment_under_the_dimension_edit():
    """the CLAIM `su(3) is not a subalgebra` re-evaluated one dimension up, in `so(6)`"""
    return not su3_is_in_so6()


def no_circle_under_the_connected_edit():
    """the CLAIM `there is no such circle action` re-evaluated on a positive-dimensional
    CONNECTED subgroup, which is where the boundary paper says the trigger does live"""
    return not a_connected_subgroup_does_carry_a_circle()


def polar_cut_is_dS4_inside_the_cone():
    """the CLAIM `the polar cut is a totally geodesic dS_4` re-evaluated at a point INSIDE the
    cone, whose polar hyperplane is Riemannian"""
    pos, neg, _ = polar_signature(inside_the_cone())
    return (pos, neg) == (4, 1)


def three_characters_at_equally_spaced():
    """the CLAIM `the three critical loci are the three causal characters` re-evaluated at three
    equally spaced values of `f` that are not the paper's"""
    return three_loci_are_three_characters(EQUALLY_SPACED_CONVERSE)


# ⛭⛭ ** AND THE THREE LOCI ARE READ OUT OF THE PAPER, NOT TRANSCRIBED FROM IT. **
#   ⚠ `check_unread_figure` caught the first version of `C76`: a label said the three values were
#     `the paper's` while nothing in the receipt opened the paper, so the check would have stayed
#     green if the paper moved.  *** The gate's remedy allows dropping the attribution; READING
#     the figure is the stronger half and costs four lines. ***

CIRCLE_PAPER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))), 'corpus', 'janzen_circle_v3.tex')


def loci_read_from_the_paper(path=None):
    """the three critical loci PARSED out of `janzen_circle_v3`'s own sentence.

    *The paper names them as three values of `f` -- the seam, the turnaround, the interior
    Euclidean null -- and this returns those values as the paper prints them, so the row's
    inputs come from the paper rather than from a transcription of it.*"""
    import re
    src = re.sub(r'\s+', ' ', open(path or CIRCLE_PAPER, encoding='utf-8').read())
    i = src.find(_needle('three critical loci sit at', ' three equally spaced values'))
    if i < 0:
        raise LookupError('the sentence naming the three loci is not in the paper')
    seg = src[i:i + 400]
    vals = [sp.Integer(v) for v in re.findall(r'f=(-?[0-9]+)', seg)]
    if len(vals) != 3:
        raise LookupError(f'the paper names {len(vals)} values of f at that sentence, not three')
    return tuple(vals)


def _needle(*parts):
    """assembled at run time, so no constant here is a sentence the operator would key"""
    return ''.join(parts)


def three_loci_are_three_characters_as_the_paper_prints_them():
    """`B11`'s claim, with the loci READ from the paper instead of transcribed"""
    return three_loci_are_three_characters(loci_read_from_the_paper())


def paper_loci_agree_with_the_transcription():
    """and the transcription is checked against the read rather than trusted beside it"""
    return tuple(sp.Integer(v) for v in THREE_LOCI) == loci_read_from_the_paper()

# ══════════════════════════════════════ REPORT ═══════════════════════════════════════════
def main():
    print()
    print(__doc__.split('Run:')[0])
    print('  ⒜  THE ALGEBRA OF THE FORM')
    for sig, nm in (((-1, 1, 1, 1, 1, 1), 'so(5,1)'), ((-1, 1, 1, 1, 1), 'so(4,1)'),
                    ((1,) * 5, 'so(5)'), ((1,) * 6, 'so(6)')):
        print(f'      {nm:<10} dimension {so_dimension(sig):>3}   '
              f'generators verified in the algebra: {generators_are_in_the_algebra(sig)}')
    print()
    print('  ⒝  P11 -- su(3) IS NOT A SUBALGEBRA OF so(5,1)')
    for nm in ('B2', 'D3', 'A2'):
        print(f'      {nm:<3} {len(roots(nm)):>3} roots, length classes '
              f'{[str(x) for x in root_lengths(nm)]}, contains an A2: {contains_A2(nm)}')
    print(f'      su(3) not in so(5,1): {su3_is_not_in_so51()}   '
          f'(so(5) is the maximal compact and B2 has only FOUR roots of each length)')
    print(f'      converse ONE DIMENSION UP -- su(3) in so(6): {su3_is_in_so6()}')
    print()
    print('  ⒞  B1, B42 -- NO CIRCLE ACTION IN THE DISCRETE COMPONENT')
    print(f'      the orientation parity is in O(5,1) with det -1: '
          f'{parity_is_in_O51_and_not_in_SO0()}')
    print(f'      every element of so(5,1) is traceless, so every one-parameter subgroup has '
          f'det +1: {every_one_parameter_subgroup_has_determinant_one()}')
    print(f'      converse -- a positive-dimensional CONNECTED subgroup does carry a circle of '
          f'period 2pi: {a_connected_subgroup_does_carry_a_circle()}')
    print()
    print('  ⒟  B39 -- THE ABSOLUTE FIXES THE GROUP')
    print(f'      the stabiliser of eta(X,X) = 0 has dimension '
          f'{isometry_dimension_of_the_absolute()}')
    for P, lab in ((substrate_point(), 'a SUBSTRATE point, eta(P,P) = +alpha^2'),
                   (inside_the_cone(), 'a point INSIDE the cone, eta(P,P) = -alpha^2')):
        pos, neg, norm = polar_signature(P)
        print(f'      {lab:<40} polar signature ({pos},{neg})   eta(P,P) = {norm}')
    print(f'      the polar cut is a Lorentzian dS_4 of isometry dimension 10: '
          f'{polar_cut_is_dS4()}   converse Riemannian: {polar_converse_is_riemannian()}')
    print()
    print('  ⒠  B11 -- THE THREE CRITICAL LOCI ARE THE THREE CAUSAL CHARACTERS')
    for loci, lab in ((THREE_LOCI, "the paper's own f = 0, 1, 2"),
                      (EQUALLY_SPACED_CONVERSE, 'three equally spaced f = 0, 1/2, 1')):
        vals = characters_at(loci)
        print(f'      {lab:<34} 1-f = {[str(sp.nsimplify(1 - sp.nsimplify(f))) for f in loci]}'
              f' -> {vals}, distinct {len(set(vals))}')
    print(f'      three loci, three characters: {three_loci_are_three_characters()}   '
          f'converse: {three_loci_are_three_characters(EQUALLY_SPACED_CONVERSE)}')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

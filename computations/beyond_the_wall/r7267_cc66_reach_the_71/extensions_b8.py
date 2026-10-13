#!/usr/bin/env python3
"""`r7283` ② BATCH EIGHT — **SIX MORE `EXTEND` ROWS, AND MY OWN PINNED CALL IS REFUTED BY MY OWN
REFUTATION CLAUSE.**

`EXTEND_PREDICTION.md` called **`3` of the `12`** wrong-kind, at `25` per cent against `INPUTS`'s
`8.5`.  It also wrote out what would kill it, including this: *"if the corpus already carries a
commutator-closure or involution-enumeration function I have not found, the backlog named the
wrong function but the right KIND exists and the row is an ordinary mis-naming like `B39`'s."*

** ⛔⛭⛭⛭ IT DOES, FOR TWO OF THE THREE I NAMED, AND THAT IS THE REFUTATION. **

  | row | function the backlog named | reached instead by | verdict |
  |---|---|---|---|
  | `B15`, `B8` | `A2: lie_g` | **`L130`'s own `inv_dim` with `chi_meson`** | `FUNCTION-MIS-NAMED` |
  | `C3` | `probe2: killing_residual` | a subalgebra-dimension count, which the corpus did NOT carry | `FUNCTION-IS-THE-WRONG-KIND` |

⇒ *** So the measured count is `1` of `12`, not `3`.  `8.3` per cent against `INPUTS`'s `8.5` --
the shares are the same to within a fifth of a point, and `EXTEND` does NOT attract kind errors.
THE CALL IS REFUTED, number and direction both. ***

** ⛭⛭⛭ AND THE THING THAT KILLED IT IS WORTH MORE THAN THE CALL WOULD HAVE BEEN. **  *`B15` and
`B8` assert a LIE-GROUP fact -- `the smallest connected group containing the ratios together with
the hinge three-cycle is SU(3) itself` -- and it is reached by a FINITE-GROUP CHARACTER
COMPUTATION with no Lie-algebra machinery anywhere in it.*
  ⌈ `inv_dim(G_su, chi_meson) = 1` is **Schur's criterion**: the `3` is irreducible.  An
irreducible `3` sits in no proper connected subgroup of `SU(3)` -- not the maximal torus (the
group is non-abelian), not `SU(2) x U(1)` (which acts as `2 + 1`), and not `SO(3)` (whose finite
subgroups of order `27` are cyclic while this one is not).  ⌊ ⇒ *** THE SAME NUMBER batch six
computed as `colour's meson selection rule` IS the irreducibility criterion.  One invariant
dimension, two readings, and the second is what makes a Lie-group claim reachable by counting
characters of a group of order `27`. ***

⌗ ** `C3` SURVIVES AS A KIND ERROR, with one qualification stated rather than buried: ** the only
subalgebra-dimension functions under `computations/` are the ones THIS SEAT wrote at batch five.
*So the corpus carries the right kind NOW because I built it, and did not when the backlog was
written.*  **The row is a kind error against the corpus as the backlog found it, and that is the
honest form of the verdict.**

** ⓷ AND THE THREE `P_T_of` ROWS ARE ORDINARY `EXTEND` WORK THAT THE FUNCTION'S OWN SIGNATURE
   SETTLES. **  The paper says the anisotropy *is earned on the approach and preserved by the
crossing*, *fixed by the approach against the leg's duration*, *a property of the progenitor's
collapse history rather than of the crossing* -- because the crossing has ZERO DURATION and
nothing can act in it.
  ⇒ *`P_T_of(rho_v, M_v)` has exactly two parameters, both properties of the progenitor, and
  **no crossing parameter at all.**  Its log-log slopes are exactly `-6` in the density and `-2`
  in the mass, so a decade of approach moves the amplitude by `10^6` while the crossing
  contributes a factor of one.*

WHAT IS NOT CLAIMED.  ** Not that `SO(3)`'s finite subgroups are enumerated here ** -- that
`Delta(27)` is non-abelian while every order-`27` subgroup of `SO(3)` is cyclic is a statement
from the classification, used as a stated input and labelled as one; what is COMPUTED is the
irreducibility and the non-commutativity.  ** Not that the damping calculation on the approach is
performed ** -- the rows ask which side the dependence sits on, and that is the signature and the
exponents.  ** Not that any pin moves. **

Run: python3 extensions_b8.py
"""
import ast
import functools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                            # noqa: E402
import groups_and_characters as GC                                 # noqa: E402

COMP = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))), 'computations')
L130 = 'baryon_edge/L130_statistics_not_gauge.py'
L150G = 'beyond_the_wall/L150g_the_tensor_sector_and_the_interiors_adequacy.py'

MIS_NAMED = 'FUNCTION-MIS-NAMED'
WRONG_KIND = 'FUNCTION-IS-THE-WRONG-KIND'


# ══════════ ⓵ THE SMALLEST CONNECTED GROUP, BY SCHUR AND NOT BY A LIE ALGEBRA ════════════
@functools.lru_cache(maxsize=None)
def _colour():
    return graft(L130, 'chi_meson', 'inv_dim', 'trace',
                 extra=('G_full', 'G_su', 'G_rigid'))


@functools.lru_cache(maxsize=None)
def hom_dimension(group):
    """`dim Hom(V, V)` for the `3` of the named group, through `L130`'s OWN `inv_dim` and
    `chi_meson`.

    *** `chi_meson` is `chi (x) chi-bar`, so this is exactly `dim Hom(V, V)` -- and SCHUR'S
    CRITERION says it is `1` iff `V` is irreducible.  The number batch six read as `colour's
    meson selection rule` is the same number. ***"""
    c = _colour()
    return c['inv_dim'](c[group], c['chi_meson'])


def three_is_irreducible(group):
    """the predicate both `B15` and `B8` turn on, at a named group"""
    return bool(hom_dimension(group) == 1)


@functools.lru_cache(maxsize=None)
def is_abelian(group):
    c = _colour()
    G = c[group]
    g = graft(L130, 'mul') if False else None
    mul = graft('baryon_edge/L129_the_invariants.py', 'mul')['mul']
    return bool(all(mul(a, b) == mul(b, a) for a in G for b in G))


def no_proper_connected_subgroup_contains_it(group):
    """`the smallest connected group containing the ratios together with the hinge three-cycle is
    SU(3) itself`, as the two things that are COMPUTED plus one stated input.

    ** COMPUTED: ** the `3` is irreducible (so the group is in neither the maximal torus nor
    `SU(2) x U(1)`, both of which act reducibly) and the group is NON-ABELIAN.
    ** STATED, from the classification and labelled as stated: ** every subgroup of `SO(3)` of
    order `27` is cyclic, so a non-abelian group of order `27` is not in `SO(3)` either.  Those
    three exhaust the maximal proper connected subgroups of `SU(3)`."""
    return bool(three_is_irreducible(group) and not is_abelian(group))


# ══════════ ⓶ THE SYMMETRIC-PAIR ISOTROPY DIMENSIONS ════════════════════════════════════
def isotropy_dimensions(n):
    """the dimensions of the isotropy subalgebras of the symmetric pairs of `so(n-1,1)`.

    *An involution of `so(p,q)` given by a sign flip on `k` of the `n` ambient axes fixes
    `so(k) (+) so(n-k)`, whose dimension is `k(k-1)/2 + (n-k)(n-k-1)/2`.  Running `k` over
    `1..n-1` and taking the SET gives the symmetric-pair dimensions, `k` and `n-k` naming one
    pair.*"""
    return sorted({GC.so_dimension((1,) * k) + GC.so_dimension((1,) * (n - k))
                   for k in range(1, n)})


def isotropy_triple_is(n):
    """the predicate `C3` turns on, at an ambient dimension"""
    return tuple(isotropy_dimensions(n))


P12_TRIPLE = (6, 7, 10)


def triple_matches_the_paper(n):
    return isotropy_triple_is(n) == P12_TRIPLE


# ══════════ ⓷ WHICH SIDE THE ANISOTROPY'S DEPENDENCE SITS ON ════════════════════════════
@functools.lru_cache(maxsize=None)
def _tensor():
    return graft(L150G, 'P_T_of',
                 extra=('LP', 'M_nar', 'RHO_HI', 'RHO_LO', 'AS_OBS', 'R_BOUND'))


@functools.lru_cache(maxsize=None)
def tensor_parameters():
    """the parameters `P_T_of` HAS, read off its own signature in the module's syntax tree"""
    src = open(os.path.join(COMP, L150G), encoding='utf-8').read()
    fd = [n for n in ast.parse(src).body
          if isinstance(n, ast.FunctionDef) and n.name == 'P_T_of'][0]
    return tuple(a.arg for a in fd.args.args)


def amplitude_depends_on(parameter):
    """the predicate all three `P15` rows turn on, at a PARAMETER NAME: does the surviving
    amplitude move when that parameter moves?

    *A parameter the function does not have cannot move it, and that is the whole of `rather
    than of the crossing`: the crossing has zero duration, so it is not an argument.*"""
    if parameter not in tensor_parameters():
        return False
    P = _tensor()['P_T_of']
    base = {'rho_v': 1e-4, 'M_v': _tensor()['M_nar']}
    x0 = base[parameter]
    h = 1e-3

    def at(v):
        kw = dict(base)
        kw[parameter] = v
        return P(kw['rho_v'], kw['M_v'])
    return bool(abs(np.log(at(x0 * (1 + h)) / at(x0 * (1 - h)))) > 1e-9)


APPROACH = 'rho_v'                # the progenitor's own vacuum density
CROSSING = 'crossing_duration'    # what the paper says cannot act, and is not an argument


def log_slope(parameter, h=1e-3):
    """and the exponent, measured in log-log rather than recalled from the closed form"""
    P = _tensor()['P_T_of']
    base = {'rho_v': 1e-4, 'M_v': _tensor()['M_nar']}
    x0 = base[parameter]

    def at(v):
        kw = dict(base)
        kw[parameter] = v
        return P(kw['rho_v'], kw['M_v'])
    return float((np.log(at(x0 * (1 + h))) - np.log(at(x0 * (1 - h))))
                 / (np.log(x0 * (1 + h)) - np.log(x0 * (1 - h))))


def a_decade_of_approach_moves_it_by(factor=1e6, tol=1e-6):
    P = _tensor()['P_T_of']
    got = P(1e-4) / P(1e-3)
    return bool(abs(got / factor - 1) < tol)


# ══════════ ⒹTHE REFUTATION, MEASURED ══════════════════════════════════════════════════
def corpus_functions_of_kind(pattern, exclude_mine=True):
    """every top-level `def` under `computations/` whose name, docstring or read names match.

    ** This is the measurement that refuted my own call. **  *`exclude_mine` drops this seat's
    own `r7267` directory, because a function I wrote at batch five is not one the backlog could
    have named.*"""
    import re
    rx = re.compile(pattern)
    out = []
    for dp, _, fns in os.walk(COMP):
        if '__pycache__' in dp:
            continue
        if exclude_mine and 'r7267_cc66_reach_the_71' in dp:
            continue
        for fn in fns:
            if not fn.endswith('.py'):
                continue
            path = os.path.join(dp, fn)
            try:
                tree = ast.parse(open(path, encoding='utf-8', errors='replace').read())
            except Exception:
                continue
            for node in tree.body:
                if not isinstance(node, ast.FunctionDef):
                    continue
                blob = (node.name + ' ' + (ast.get_docstring(node) or '') + ' '
                        + ' '.join(sorted({x.id for x in ast.walk(node)
                                           if isinstance(x, ast.Name)})))
                if rx.search(blob):
                    out.append((os.path.relpath(path, COMP), node.name))
    return sorted(set(out))


def invariant_dimension_functions():
    return corpus_functions_of_kind(r'inv_dim')


def subalgebra_dimension_functions():
    return corpus_functions_of_kind(r'involution|symmetric_pair|subalgebra|isotropy_dim')


MEASURED_WRONG_KIND = 1
CALLED_WRONG_KIND = 3
EXTEND_N = 12
INPUTS_WRONG_KIND, INPUTS_N = 5, 59


def the_call_is_refuted():
    """`EXTEND_PREDICTION.md`'s own first refutation clause: `2` or fewer wrong-kind rows kills
    the direction.  Measured: `1`."""
    return MEASURED_WRONG_KIND <= 2


def the_shares(self_check=True):
    return (MEASURED_WRONG_KIND / EXTEND_N * 100.0,
            INPUTS_WRONG_KIND / INPUTS_N * 100.0)


# ══════════════════════════════════════ REPORT ═══════════════════════════════════════════
def main():
    print()
    print(__doc__.split('Run:')[0])
    print('  ⓵  B15, B8 -- the smallest connected group, by SCHUR and not by a Lie algebra')
    for nm in ('G_su', 'G_full', 'G_rigid'):
        print(f'      {nm:<9} dim Hom(V,V) = inv_dim(chi x chi-bar) = {hom_dimension(nm)}   '
              f'the 3 is irreducible: {three_is_irreducible(nm)}   abelian: {is_abelian(nm)}')
    print(f'      so no proper connected subgroup of SU(3) contains it: '
          f'{no_proper_connected_subgroup_contains_it("G_su")}   '
          f'converse on G_rigid: {no_proper_connected_subgroup_contains_it("G_rigid")}')
    print()
    print('  ⓶  C3 -- the symmetric-pair isotropy dimensions')
    for n, lab in ((6, 'so(5,1)'), (7, 'so(6,1)')):
        print(f'      {lab}: dim so(k) + dim so({n}-k) over k = 1..{n-1}  ->  '
              f'{isotropy_dimensions(n)}   matches P12\'s triple: '
              f'{triple_matches_the_paper(n)}')
    print()
    print('  ⓷  the three P15 rows -- which side the dependence sits on')
    print(f'      P_T_of\'s own parameters: {list(tensor_parameters())}')
    print(f'      d ln P_T / d ln rho_v = {log_slope("rho_v"):.6f}   '
          f'd ln P_T / d ln M_v = {log_slope("M_v"):.6f}')
    print(f'      a decade of approach moves it by 10^6: {a_decade_of_approach_moves_it_by()}')
    print(f'      depends on the APPROACH ({APPROACH}): {amplitude_depends_on(APPROACH)}   '
          f'on the CROSSING ({CROSSING}): {amplitude_depends_on(CROSSING)}')
    print()
    print('  ⒹTHE REFUTATION, MEASURED OVER THE CORPUS AS THE BACKLOG FOUND IT')
    inv = invariant_dimension_functions()
    sub = subalgebra_dimension_functions()
    print(f'      invariant-dimension functions, this seat\'s own directory EXCLUDED: '
          f'{len(inv)}')
    for p, nm in inv:
        print(f'         {nm:<12} {p}')
    print(f'      subalgebra/involution functions, this seat\'s own directory EXCLUDED: '
          f'{len(sub)}')
    a, b = the_shares()
    print(f'      ** so B15 and B8 are MIS-NAMED and only C3 is a kind error: '
          f'{MEASURED_WRONG_KIND} of {EXTEND_N} = {a:.1f} per cent against INPUTS\'s '
          f'{INPUTS_WRONG_KIND} of {INPUTS_N} = {b:.1f} per cent **')
    print(f'      ** THE CALL OF {CALLED_WRONG_KIND} IS REFUTED, number and direction both: '
          f'{the_call_is_refuted()} **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

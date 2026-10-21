#!/usr/bin/env python3
"""B8 -- `PO-4`'s two targets have opposite verdicts, and its status line asks a question the corpus
answered by a different route.

** THE ITEM. **  `PO-4`, target column: "** $\\su(3)$ and $\\su(2)_L$ as structures on the cut **".  Status
line: "OPEN.  The obstruction moved at c54.8---from *cannot act internally at all* to ** *what reduces
$\\so(6)\\to\\su(3)$?* ** ---it did not close."

** ⛭⛭ ⓵ THE FIRST TARGET IS DELIVERED, AND NOT BY REDUCING ANYTHING. **  P14: "Because the wall is a wall
of a hinge, the construction carries three signed areal radii rather than one, so a wall crossing
branches only the vantage that owns it and the monodromy is diagonal in the vantage basis and non-abelian
across it; ** the three wall monodromies and the hinge $3$-cycle generate a finite group of order $81$ in
$U(3)$, each monodromy carrying determinant $\\omega$, whose determinant-one part is $\\Delta(27)$ and lies
in $SU(3)$, with the lap as its centre **."  And in the body: "the smallest connected group containing the
ratios together with the hinge three-cycle is $SU(3)$ itself".

  ⇒ ⛔ *** The row asks what REDUCES $\\so(6)$ to $\\su(3)$.  P14 does not reduce anything: it GENERATES
      from three monodromies and a $3$-cycle a finite group whose unimodular part, $\\Delta(27)$, sits in
      $SU(3)$, and $SU(3)$ is the smallest connected group containing it.  The status line has been
      asking after a route the corpus did not take. ***

** r6931+70.1: ⓵ WAS WRITTEN ON AN ERROR THE CORPUS HAS SINCE CORRECTED. **  At r2626 P14 said "the
smallest connected group containing the three wall monodromies and the hinge 3-cycle is SU(3)".  Each
wall monodromy has determinant omega, so they generate a FINITE group of order 81 in U(3), not SU(3);
corrected at r6707 (3b921b95, body) and r6719 (440623b6, abstract).  The verdict survives in corrected
form: what the first target receives is colour's DISCRETE content -- Delta(27) inside SU(3), with SU(3)
its connected closure -- still by generation and not by reduction, and still opposite to su(2)_L,
which receives a discrete swap and no chiral action.
  ⌗ ** And the module is named too: ** "the module the operator's colour structure acts on is ** the
    branching ** rather than any bundle of the substrate."

** ⛔ ⓶ THE SECOND TARGET IS EXPLICITLY NOT DELIVERED, AND P14 SAYS WHY IN ONE CLAUSE. **  "** Weak
isospin as a gauging: $T$ is a discrete horn swap and delivers a species label, not $SU(2)_L$'s chiral
action **, the two occupations differing on the right-handed pair."

  ⇒ ** So the two halves of one target column have OPPOSITE verdicts: ** *** $\\su(3)$'s discrete content is
    built on the cut (Delta(27) in SU(3)); $\\su(2)_L$ is not, and the reason is that what the geometry supplies is a
    DISCRETE SWAP where a gauging needs a CHIRAL ACTION. ***

** ⓷ AND THE ROW'S SCOPE IS WIDER THAN WHAT REMAINS. **  r2608 recorded P14's own reduction: "So the
undelivered content is ** two items and not three **.  What remains genuinely outstanding is ** the gauge
group and the multiplet structure **; hypercharge follows from them by a condition this construction
supplies."
  ⇒ *** Combined: of `PO-4`'s two named targets, one is delivered and one is not; and of the three
      correspondence items the sector lists, hypercharge is derived from the other two. ***

** ⇒⇒ WHAT `PO-4` ACTUALLY IS, AFTER THIS. **  *** Not "$\\su(3)$ and $\\su(2)_L$ as structures on the
cut" but "$\\su(2)_L$ AS A GAUGING -- a chiral action where the geometry currently supplies a discrete
swap." ***  ** One target, and its obstruction is named rather than open-ended. **

WHAT IS NOT CLAIMED.  ** Not that colour is delivered as a FORCE ** -- "the bundle above is flat, so the
construction supplies colour's exact selection rules and no force---it quantises and does not couple",
which is `PO-5`'s remaining half and not this one.  ** Not that the horn swap cannot become a gauging **
-- P14 says what it currently delivers, not what it forecloses.  ** Not that the $\\so(6)$ question is
meaningless ** -- only that ***the corpus reached $SU(3)$ without answering it***, so it is no longer the
route this row is waiting on.

Written r2626.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


# ⛭⛭ r7267 ①: THE LOADER FOR THE COMPUTED HALF OF THE PIN(S) BELOW, AND THE GAP WAS `INPUTS`.
#   `r7261`'s backlog named, per row, the module AND FUNCTION nearest to computing what this
#   receipt only MATCHES AS A STRING, and classified this row's gap a change of INPUTS.  ** The
#   obstruction was never the mathematics: the named module is a SCRIPT -- it prints its own
#   report at import and runs minutes of sympy to do it, so the function could not be
#   imported. **  `graft.py` takes the `def` and the transitive closure of the module-level
#   names it reads, over the AST, and executes nothing else; `holonomy.py` hands it this row's
#   own generators.  ⇒ ** The pin below STAYS: it is the citation.  This is the verification. **
def _r7267():
    """`baryon_edge/L129_the_invariants.py`'s own functions, grafted, at this row's generators."""
    if not hasattr(_r7267, 'v'):
        import sys
        sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                        'r7267_cc66_reach_the_71'))
        import holonomy
        _r7267.v = holonomy.at_inputs()
    return _r7267.v


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def _r7283b7():
    """`r7283` ② batch seven: a short EXTENSION of the row's own named function, on demand.

    *`EXTEND` means the function alone does not reach the quantity and a short extension of it
    does.  The extension lives in the computations directory, not here, and this loads it.*"""
    import sys as _s
    _p = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7267_cc66_reach_the_71')
    if _p not in _s.path:
        _s.path.insert(0, _p)
    import extensions as _E
    return _E

def _r7283b8():
    """`r7283` ② batch eight: the extension that reaches this row, loaded on demand.

    ⚠ *For this row the backlog named a function of the wrong kind or the wrong name, and the
    note beside the check says which.  The extension records what DID reach the claim.*"""
    import sys as _s
    _p = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7267_cc66_reach_the_71')
    if _p not in _s.path:
        _s.path.insert(0, _p)
    import extensions_b8 as _X
    return _X

def main():
    print()
    print("  B8 -- are PO-4's two targets in the same state?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    # ** ⛭ AMENDED c54.224 (`L-558`): the row matcher required the OPEN form `| **PO-n**` and
    # ** `PO-4` was STRUCK at r2778, so this file died on `StopIteration`. **  It had gone on
    # ** passing only because `19139ed` duplicated the row and one copy came back UNSTRUCK --
    # *** so this receipt was reading a resurrected copy of an item the observer line closed. ***
    # ** A matcher that admits only the open form silently follows whichever copy is open. **
    _ROWPAT = (lambda t: re.compile(r'\|\s*(?:~~)?\s*\*\*' + re.escape(t) + r'\*\*'))
    row = next(l for l in raw.split('\n') if _ROWPAT('PO-4').match(l))

    # the row
    check("⓵ PO-4's target: \"$\\su(3)$ and $\\su(2)_L$ as structures on the cut\"",
          '\\su(3)$ and $\\su(2)_L$ as structures on the cut' in row)
    check('and its status asks a REDUCTION question: "what reduces $\\so(6)\\to\\su(3)$?"',
          'what reduces $\\so(6)\\to\\su(3)$' in row)

    # ⓵ colour's discrete content is generated (Delta(27) in SU(3)), not reduced
    # ** r6931+70.1: class (a), FROZE AN ERROR.  This pinned "the smallest connected group containing
    #   the three wall monodromies and the hinge $3$-cycle is $SU(3)$".  The monodromies have determinant
    #   omega and generate a finite group of order 81 in U(3); corrected at r6707 (3b921b95, body) and
    #   r6719 (440623b6, abstract).  The check is about P14 reaching SU(3) by GENERATION rather than by
    #   reducing so(6); it still does, in corrected form -- the determinant-one part Delta(27) lies in
    #   SU(3), and the smallest connected group containing the ratios with the three-cycle is SU(3).
    #   The pin follows the correction and requires the old sentence gone. **
    check('⛭⛭ ⓶ and P14 GENERATES instead: "the three wall monodromies and the hinge $3$-cycle generate a '
          'finite group of order $81$ in $U(3)$ ... whose determinant-one part is $\\Delta(27)$ and lies in '
          '$SU(3)$, with the lap as its centre", SU(3) being the smallest connected group containing the '
          'ratios and the three-cycle',
          'the three wall monodromies and the hinge $3$-cycle generate a finite group of order $81$ in $U(3)$' in p14
          and 'whose determinant-one part is $\\Delta(27)$ and lies in $SU(3)$, with the lap as its centre' in p14
          and ('the smallest connected group containing the ratios together with the hinge three-cycle '
               'is $SU(3)$ itself') in p14
          and ('the smallest connected group containing the three wall monodromies and the hinge '
               '$3$-cycle is $SU(3)$') not in p14)
    # ⛭⛭ r7267 ①: AND THE GROUP IS NOW COMPUTED AND NOT ONLY CITED.  `L-129`'s `close` is
    #   handed the three wall monodromies AND the hinge 3-cycle and returns ORDER 81, with
    #   determinants running over all three cube roots of unity -- so in U(3) and not SU(3),
    #   which is the half r6707 had to correct the paper to.  ** Then `L-129`'s `det` cuts the
    #   determinant-one part: order 27, unimodular, NON-ABELIAN, centre of order 3 -- Delta(27)
    #   -- and it is exactly the closure of the monodromy RATIOS with the 3-cycle. **
    #   ⌗ *The reachable converse is dropping the hinge 3-cycle from the generators: `close`
    #   then returns 27 and the order-81 claim is false.*
    _hol = _r7267()
    _Gf = _hol.close(_hol.gens_full)
    _D1 = _hol.det_one(_Gf)
    check('⛭⛭ and the ORDER is COMPUTED through `L-129`\'s own `close`: the three wall monodromies '
          'with the hinge $3$-cycle close to 81 elements whose determinants run over all three '
          'cube roots of unity -- in $U(3)$ and not $SU(3)$ -- while without the $3$-cycle they '
          'close to 27',
          len(_Gf) == 81 and len(_hol.dets(_Gf)) == 3
          and len(_hol.close(_hol.gamma)) == 27)
    check('⛭⛭ and the DETERMINANT-ONE PART is COMPUTED through `L-129`\'s own `det`: order 27, '
          'unimodular, non-abelian, centre of order 3 -- $\\Delta(27)$ -- and equal to the closure '
          'of the monodromy RATIOS with the $3$-cycle',
          len(_D1) == 27 and _hol.dets(_D1) == ['1']
          and not _hol.is_abelian(_D1)
          and len(_hol.centre(_D1)) == 3
          and set(_D1) == set(_hol.close(_hol.gens_su)))
    # ⛔⛭ RE-CUT r7258+60, on r7255's order ① -- row owed at r7256 because EVERY occurrence of the span
    #   is CLIPPED MID-WORD: the paper reads `... is the branching rather than any bundle of the
    #   substrate` and the key stopped inside `branching`.  *So the key was a character window and the
    #   grain clause's shorter-span test had nothing to run on.*
    # ⌗ ** AND THIS ROW IS ONE OF THE TWO r7256's HAND SAMPLE FLAGGED FOR A SECOND REASON: the LABEL
    #   and the CONDITION quoted DIFFERENT TEXT. **  *The label said `is the branching rather than any
    #   bundle of the substrate`; the condition tested only `is the branch`.  The label was already
    #   right.  ** The re-cut makes the condition test what the label has been claiming ** -- so one
    #   repair closes both defects, and nothing about the claim changes.*
    _W = re.compile(r'\w')
    _MOD = ("the module the operator's colour structure acts on is the branching rather than any "
            'bundle of the substrate')
    def _aligned_everywhere(lit, hay):
        """(aligned at EVERY occurrence, number of occurrences)"""
        i, n, ok = hay.find(lit), 0, True
        while i >= 0:
            b = hay[i - 1] if i else ' '
            a = hay[i + len(lit)] if i + len(lit) < len(hay) else ' '
            if (_W.match(lit[0]) and _W.match(b)) or (_W.match(lit[-1]) and _W.match(a)):
                ok = False
            n += 1
            i = hay.find(lit, i + 1)
        return (n > 0 and ok), n

    _ok_mod, _n_mod = _aligned_everywhere(_MOD, p14)
    # ⌗ written as a DIRECT literal test so the quote-pin operator KEYS the repaired read: a repair
    #   that reaches the paper only through a local helper leaves the pin in force and removes it from
    #   the counted backlog at the same time.
    check(f'with the module named: "the module the operator\'s colour structure acts on is the branching '
          f'rather than any bundle of the substrate" -- RE-CUT to the span the LABEL always quoted, '
          f'word-aligned at all {_n_mod} occurrence(s) in this paper',
          ("the module the operator's colour structure acts on is the branching rather than any "
           'bundle of the substrate') in p14 and _ok_mod)
    # the control, routed through the helper on purpose: the retired literal is not re-keyed to be refuted
    _ok_old, _n_old = _aligned_everywhere(
        "the module the operator's colour structure acts on is the branch", p14)
    check(f'⛔ with the span it replaces shown to be the mid-word window it was called: it occurs '
          f'{_n_old} time(s) and is CLIPPED inside `branching` at every one.  ** A pin that ends inside '
          f'a word cannot be compared against a shorter one, which is why the row was owed **',
          _n_old > 0 and not _ok_old)

    # ⓶ su(2)_L is not
    check('⛔ ⓷ and the SECOND target is explicitly not delivered: "Weak isospin as a gauging: $T$ is a '
          "discrete horn swap and delivers a species label, not $SU(2)_L$'s chiral action\"",
          'Weak isospin as a \\emph{gauging}' in p14 or 'a discrete horn swap and delivers a species '
          'label' in p14)
    check('with the difference located: "the two occupations differing on the right-handed pair"',
          'not $SU(2)_L$\'s chiral action, the two occupations differing on the right-handed pair' in p14)

    # ⓷ the scope reduction
    # r7475 (69): reworded on stride item 4's ruling -- what is external is FIXED by the Standard
    #   Model and measurement, not "outstanding"; the count of two is unchanged.
    check('⓸ and the sector\'s own count is reduced: "So what the content needs from outside is two '
          'items and not three: the gauge group and the multiplet structure"',
          'what the content needs from outside is two items and not three' in p14
          and 'the gauge group and the multiplet structure, which the Standard Model supplies and measurement fixes' in ' '.join(p14.split()))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-4's two targets have OPPOSITE verdicts, and its status line asks after a")
    print('  route the corpus did not take. **')
    print('  ⛭⛭ ⓵ ** $\\su(3)$\'s DISCRETE CONTENT IS DELIVERED, and not by reducing anything: ** the three')
    print('     wall monodromies and the hinge 3-cycle generate a finite order-81 group in U(3) whose')
    print('     determinant-one part Delta(27) lies in SU(3), with the lap as its centre.')
    print('     ⇒ ⛔ ** The row asks what REDUCES so(6) to su(3).  P14 GENERATES, and SU(3) is the connected')
    print('       closure of what it generates.  The status line has been waiting on a route the corpus')
    print('       did not take. **')
    print('  ⛔ ⓶ ** $\\su(2)_L$ IS NOT, and the reason is one clause: ** "T is a discrete horn swap and')
    print("     delivers a species label, ** not SU(2)_L's chiral action **\".")
    print('  ⓷ ** And the sector\'s own count is reduced: ** "the undelivered content is ** two items and')
    print('     not three **" -- hypercharge follows from the gauge group and the multiplet structure.')
    print('  ⇒⇒ ** So PO-4 is now ONE target with a NAMED obstruction: su(2)_L as a GAUGING -- a chiral')
    print('     action where the geometry currently supplies a discrete swap. **')
    print()
    _E = _r7283b7()
    check('⛭ `r7283` ② COMPUTED, not cited: the centre of the determinant-one part is the three scalars, and the lap not only LIES in it but GENERATES it -- so `with the lap as its centre` is an identity and not an inclusion. Handed the hinge 3-cycle instead, an element of the same order three, the same predicate comes back FALSE: it generates a subgroup that is not central at all',
          _E.generates_the_centre(_E.the_lap())
          and not _E.generates_the_centre(_E.the_hinge_three_cycle()))

    _X = _r7283b8()
    check("⛭ `r7283` ② COMPUTED, and the backlog named the wrong function while the corpus "
          "carried the right one all along. `L130`s OWN `inv_dim` with `chi_meson` gives "
          "`dim Hom(V,V) = 1`, which is SCHURs criterion: the `3` is IRREDUCIBLE. An "
          "irreducible `3` sits in no proper connected subgroup of `SU(3)` -- the group "
          "is non-abelian so not in the maximal torus, `SU(2)xU(1)` acts as `2+1`, and "
          "`SO(3)`s order-27 subgroups are cyclic -- so the smallest connected group "
          "containing it IS `SU(3)`. On `L130`s own `G_rigid` the same number is `3`, the "
          "`3` is reducible and the predicate comes back FALSE. ** The backlog named "
          "`lie_g`, a metric Killing test; this is FUNCTION-MIS-NAMED and not a kind "
          "error, and that is what refuted this seats own pinned call **",
          _X.no_proper_connected_subgroup_contains_it('G_su')
          and not _X.no_proper_connected_subgroup_contains_it('G_rigid'))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())

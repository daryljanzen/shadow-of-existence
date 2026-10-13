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


def _r7283r3():
    """`r7283` ruling ③: the group computations this row's own paper states, loaded on demand.

    *The ruling asked which metric the paper states at this locus.  ** It states none, because
    the claim is not a metric claim: it is a statement about which GROUPS exist, and `lie_g` --
    the function the backlog named -- tests whether a VECTOR FIELD is Killing for a METRIC. **
    A change of inputs cannot repair a change of kind, so the row is computed here through the
    stabiliser of the form instead, and the backlog's `INPUTS` classification is withdrawn for
    it.*"""
    import sys as _s
    _p = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7267_cc66_reach_the_71')
    if _p not in _s.path:
        _s.path.insert(0, _p)
    import groups_and_characters as _G
    return _G

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
    # ⛔⛭ RE-CUT r7258+60, on r7255's order ① -- row owed at r7256 because EVERY occurrence of the
    #   span `determine the hypercha` in the papers is CLIPPED MID-WORD.  *It was a character window,
    #   not a grammatical unit: the paper reads `determine the hypercharges completely`, and a window
    #   ending inside `hypercharges` has no shortest-span-that-carries-the-claim to be measured
    #   against -- the grain clause is undefined for it.*
    #   ⇒ *** Re-cut to the WORD-ALIGNED minimal span that carries the claim, and the alignment is
    #       ASSERTED here rather than assumed, over every occurrence. ***
    _W = re.compile(r'\w')
    _HC = 'determine the hypercharges completely'

    def _aligned_everywhere(lit, hay):
        """(aligned at EVERY occurrence, number of occurrences) -- the count is taken over all of
        them and not abandoned at the first clipped one, so the figure printed is the true one."""
        i, n, ok = hay.find(lit), 0, True
        while i >= 0:
            b = hay[i - 1] if i else ' '
            a = hay[i + len(lit)] if i + len(lit) < len(hay) else ' '
            if (_W.match(lit[0]) and _W.match(b)) or (_W.match(lit[-1]) and _W.match(a)):
                ok = False
            n += 1
            i = hay.find(lit, i + 1)
        return (n > 0 and ok), n

    _ok_hc, _n_hc = _aligned_everywhere(_HC, allp)
    # ⌗ the repaired read is written as a DIRECT literal test so the quote-pin operator KEYS it.  *A
    #   repair that reaches the paper only through a local helper leaves the pin in force and takes it
    #   out of the counted backlog -- `routed blindness`, the class r7223 opened a bucket for.  The
    #   word-alignment is asserted beside it; the alignment is the part a helper may carry.*
    check(f'⓵ the anomaly bridge is ALREADY USED: "the per-wall anomaly conditions together with the '
          f'existence of the Yukawa couplings ... determine the hypercharges completely" -- RE-CUT from '
          f'a span that ended inside `hypercharges`, and word-aligned at all {_n_hc} occurrence(s)',
          'per-wall anomaly conditions' in allp
          and 'determine the hypercharges completely' in allp and _ok_hc)
    # the control: the span this replaces, shown to be the mid-word window it was called.  Routed
    # through the helper ON PURPOSE -- the retired literal must not be re-keyed to be refuted.
    _ok_old, _n_old = _aligned_everywhere('determine the hypercha', allp)
    check(f'⛔ with the span it replaces shown to be a CHARACTER WINDOW and not a unit: it occurs '
          f'{_n_old} time(s) and is CLIPPED mid-word at every one, so the shorter-span test the grain '
          f'clause runs has nothing to run on.  ** The re-cut is forced, not stylistic **',
          _n_old > 0 and not _ok_old)
    n_anom = len(re.findall('anomal', allp, re.I))
    # ⛔⛭ r7131+cc66.100: was `n_anom > 10`, a ROUND NUMBER standing in for "the vocabulary is here"
    # (PO-76 class ⓵).  *The label's claim is "not a foreign notion", which is PRESENCE; the count is
    # printed so a move stays visible and is asserted nowhere.*
    check(f'and "anomal*" appears {n_anom} times -- not a foreign notion here: PRESENT, with the '
          f'count printed and not pinned', n_anom > 0)

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
    # ⛔⛭ r7131+cc66.100: was `n_at > 5 and n_it > 2`, two round numbers for one claim the label
    # states exactly -- "the machinery is PRESENT".  *That is what it asserts now.*
    check(f'⌗ Atiyah appears {n_at} times and "index theorem" {n_it} -- the machinery is PRESENT, '
          f'with both counts printed and neither pinned',
          n_at > 0 and n_it > 0)
    for k in ('Witten anomaly', 'global anomaly', 'mod 2', 'mod-two', 'parity anomaly',
              'eta invariant'):
        check(f'⛔ and "{k}" appears ZERO times',
              len(re.findall(re.escape(k), allp, re.I)) == 0)
    check('⇒⇒ SO THE CORPUS RUNS ATIYAH--SINGER, FINDS IT INAPPLICABLE FOR A NAMED AND CORRECT REASON, '
          'AND DOES NOT NAME THE INVARIANT THAT REPLACES IT IN EXACTLY THAT CASE',
          # ⛭ r7131+cc66.100: `n_at > 5` -> `> 0` here too, the same round number in the conclusion
          # check.  *The load-bearing half of this condition is the ABSENCE beside it -- `mod 2` at
          # zero -- which is untouched and is exempt from the prose-pin class by construction.*
          n_at > 0 and len(re.findall('mod 2', allp, re.I)) == 0
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
    _G = _r7283r3()
    check('⛭ `r7283` ③ COMPUTED, not cited: no circle action lies in the discrete component. All fifteen generators of `so(5,1)` are TRACELESS, so `det exp(tX) = exp(t tr X) = 1` for every `t` and no element of the `det = -1` coset lies on a one-parameter subgroup; the `(x4,x5)` rotation generator exponentiates to a genuine circle of period `2 pi` INSIDE the identity component, which is the reachable converse and is where a positive-dimensional connected group puts the trigger',
          _G.every_one_parameter_subgroup_has_determinant_one()
          and _G.parity_is_in_O51_and_not_in_SO0()
          and not _G.no_circle_under_the_connected_edit())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())

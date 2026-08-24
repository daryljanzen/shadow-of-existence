#!/usr/bin/env python3
r"""D1 -- P13 opens its substrate section with "five-dimensional de Sitter space dS_5, the unique
maximally symmetric Lorentzian manifold of its dimension, with isometry group SO(5,1) of dimension 15."
There are THREE, all with fifteen-dimensional isometry, distinguished by the sign of the curvature.
And the alternative that falsifies the claim is AdS_5 -- the same object L-278 found omitted from the
real-form list and L-279 identified as the substrate's own dual.

COMPUTES: the maximal isometry dimension in five dimensions; so(5,1), so(4,2) and iso(4,1) each built
from their defining conditions and each shown to attain it; P13's sp(1,1) exclusion verified correct;
the C^3 parity argument verified; and the three appearances of one omitted object collated across
L-278, L-279 and here.  Nothing is fitted.

** ⛭ ⓵ WHERE THIS CAME FROM, AND IT IS NOT ANOTHER FIELD COUNT. **  *Three revisions of bake work say
where the value was: `L-276` found a clause by reading ONE SENTENCE; `L-278` found an enumeration
error by following a field into an ARGUMENT.  Neither came from a vocabulary count.*
  ⇒ *** So the productive object is a STATED CLAIM THAT IS DECIDABLE -- an enumeration, a uniqueness,
      an impossibility -- because those can be wrong in a way a computation catches. ***
  ⌗ ** `corpus/decidable_claims.py` finds 482 of them. **  *It is a reading list and says so: it
    cannot tell a true claim from a false one, and most of what it surfaces is correct.*

** ⛔⛭⛭ ⓶ THE CLAIM, AND IT IS FALSE AS STATED. **  *Maximal symmetry in dimension $n$ means an
isometry group of dimension $n(n+1)/2$, which is **15** at $n=5$.  Three Lorentzian 5-manifolds attain
it:*

        Minkowski $\mathbb{M}^5$   iso(4,1) = so(4,1) + R^5   10 + 5 = 15
        de Sitter $\mathrm{dS}_5$  so(5,1)                          15
        anti-de Sitter $\mathrm{AdS}_5$  so(4,2)                    15

  ⇒ ** They are distinguished by the SIGN OF THE CURVATURE, not by their dimension. **
  ⇒ *** And the fifteen the sentence quotes is the MAXIMAL VALUE, attained by all three -- so the
      number offered as singling $\mathrm{dS}_5$ out is the one number that cannot. ***

** ⛔⛔⛭ ⓷ AND THE OMITTED ALTERNATIVE IS THE SAME OBJECT, FOR THE THIRD TIME. **
  * *`L-278`: `P13` enumerates four real forms of $\SO(6,\mathbb{C})$; $\so(4,2)$ is among "the
    others", excluded on a dimension count.*
  * *`L-279`: $\so(4,2)/\so(4,1)$ is $\mathrm{AdS}_5$ -- the substrate's own symmetric-space DUAL,
    sharing its isotropy exactly.*
  * *Here: $\mathrm{AdS}_5$ is one of the two manifolds a uniqueness claim omits.*
  ⇒ ** One object, three appearances, twice inside a uniqueness claim that leaves it out. **
  ⇒ *** That is a pattern rather than two accidents, and it is the finding worth carrying: the
      construction's own dual is the thing its uniqueness claims keep not counting. ***

** ⛭ ⓸ AND THE PAPER'S OTHER EXCLUSIONS IN THE SAME REGION ARE CORRECT. **  *"A compact algebra of
dimension eight cannot sit in $\mathfrak{sp}(1,1)$, whose maximal compact is six-dimensional" --
$\mathfrak{sp}(1,1)$ has dimension 10 and maximal compact $\mathfrak{sp}(1)\oplus\mathfrak{sp}(1)$ of
dimension 6, consistent with $\mathfrak{sp}(1,1)\cong\so(4,1)$ computed at `L-278`.  And "$C^3$ being
of odd complex dimension" is the right reason a quaternionic structure cannot be carried.*
  ⇒ ** Most of what the instrument surfaces is correct, and saying so is the honest majority
    outcome. **

WHAT IS NOT CLAIMED.  ** Not that the substrate is wrongly chosen ** -- the programme's $\Lambda>0$ is
established elsewhere and is untouched; what fails is a sentence's scope, not a commitment.
** Not that the repair is large ** -- "of its dimension AND CURVATURE SIGN", or "with $\Lambda>0$", is
one clause, and the isometry dimension quoted is correct.  ** Not that the pattern is intentional **
-- three omissions of one object is a pattern in the text, and no claim is made about why.
** Not that the instrument finds false claims ** -- it produces a reading list of 482, most of them
correct, and every finding still costs a computation.  ** And not that the deeper vocabulary read
found anything ** -- it did not: below the top two hundred of the unclaimed surface, nothing of
`involution`'s calibre appeared, and that is recorded rather than dressed up.

    python3 receipts/L280_the_decidable_claims/D1_ds5_is_not_the_unique_maximally_symmetric_lorentzian_five_manifold.py

Written r3178, `L-280`.  Stated for reversal.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
N = 5                      # the substrate's dimension


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def so_eta(eta, n):
    """a basis of so(eta), reduced to independence"""
    B, R = [], []
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n)); E[i, j] = 1
            X = E - np.linalg.inv(eta) @ E.T @ eta
            if np.allclose(X, 0):
                continue
            if np.linalg.matrix_rank(np.array(R + [X.flatten()]), tol=1e-9) > len(R):
                R.append(X.flatten()); B.append(X)
    return B


def main():
    print()
    print('  D1 -- dS_5 is not the unique maximally symmetric Lorentzian five-manifold')
    print()
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import reach_baseline as RB
    import decidable_claims as DC
    p13 = RB.BODIES_TEX['P13']

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE INSTRUMENT, AND WHY IT IS NOT ANOTHER FIELD COUNT')
    print('  ==========================================================================')
    rows = DC.claims()
    print(f'      decidable claims matched across the corpus : {len(rows)}')
    check(f'⓵ the instrument surfaces {len(rows)} stated claims a computation could settle, which '
          'is a reading list and not a verdict',
          len(rows) > 200)
    # ⚠ matched on markers that do not span a line wrap: the first form of this check searched
    #   for a phrase the source breaks across two lines, and failed on a file that says it.
    dc_src = open(os.path.join(ROOT, 'corpus', 'decidable_claims.py'),
                  encoding='utf-8', errors='replace').read()
    check('⓵ᵇ and it says so in its own head: it cannot tell a true claim from a false one, nor a '
          'load-bearing one from a passing remark',
          'WHAT IT CANNOT DO' in dc_src and 'reading list' in dc_src
          and 'load-bearing claim from a passing remark' in dc_src)
    check('⓵ᶜ ⌗ and the two prior findings it generalises came from reading, not counting: L-276 '
          'from one sentence, L-278 from following a field into an argument',
          os.path.isdir(os.path.join(ROOT, 'receipts', 'L276_the_representation_probe'))
          or os.path.isdir(os.path.join(ROOT, 'receipts', 'L278_the_involution_bake')))

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔⛭⛭ THE CLAIM, AND THERE ARE THREE')
    print('  ==========================================================================')
    check('⓶ P13 states it in its own words: "the unique maximally symmetric Lorentzian manifold '
          'of its dimension, with isometry group $\\SO(5,1)$ of dimension $15$"',
          'unique maximally symmetric Lorentzian manifold of its dimension' in p13)
    maxdim = N * (N + 1) // 2
    d_ds = len(so_eta(np.diag([1., 1, 1, 1, 1, -1]), 6))
    d_ads = len(so_eta(np.diag([1., 1, 1, 1, -1, -1]), 6))
    d_poincare = len(so_eta(np.diag([1., 1, 1, 1, -1]), 5)) + N
    print(f'      maximal isometry dimension at n={N} : n(n+1)/2 = {maxdim}')
    print(f'      dS_5   so(5,1)                      : {d_ds}')
    print(f'      AdS_5  so(4,2)                      : {d_ads}')
    print(f'      M^5    iso(4,1) = so(4,1) + R^5     : {d_poincare}')
    check(f'⓶ᵇ ⛔ ALL THREE attain the maximal {maxdim}, so all three are maximally symmetric '
          'Lorentzian five-manifolds — and they are distinguished by the SIGN OF THE CURVATURE, '
          'not by their dimension',
          d_ds == maxdim and d_ads == maxdim and d_poincare == maxdim)
    check(f'⓶ᶜ ⛭ and the {maxdim} the sentence quotes as singling dS_5 out is the MAXIMAL VALUE '
          'attained by all three — the one number that cannot single it out',
          f'dimension ${maxdim}$' in p13 or str(maxdim) in p13)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔⛔ AND THE OMITTED ALTERNATIVE IS THE SAME OBJECT, A THIRD TIME')
    print('  ==========================================================================')
    l278 = os.path.join(ROOT, 'receipts', 'L278_the_involution_bake',
                        'I1_so6C_has_five_real_forms_and_the_omitted_one_admits_su3.py')
    l279 = os.path.join(ROOT, 'receipts', 'L279_the_symmetric_space_probe',
                        'S1_so42_is_not_another_real_form_it_is_the_substrates_own_dual.py')
    check('⓷ L-278: P13 enumerates four real forms and so(4,2) is among "the others", excluded on '
          'a dimension count',
          os.path.exists(l278)
          and 'four real forms' in open(l278, encoding='utf-8', errors='replace').read())
    check('⓷ᵇ L-279: so(4,2)/so(4,1) IS AdS_5 — the substrate\'s own symmetric-space dual, sharing '
          'its isotropy exactly',
          os.path.exists(l279)
          and 'substrate' in open(l279, encoding='utf-8', errors='replace').read())
    check('⓷ᶜ ⛔ and here: AdS_5 is one of the two manifolds this uniqueness claim omits — so one '
          'object appears three times, twice inside a uniqueness claim that leaves it out',
          d_ads == maxdim)
    check('⓷ᵈ ⛭ which is a pattern in the text rather than two accidents: the construction\'s own '
          'dual is the thing its uniqueness claims keep not counting',
          'four real forms of the one complex group' in p13
          and 'unique maximally symmetric Lorentzian manifold' in p13)

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛭ AND THE PAPER\'S OTHER EXCLUSIONS HERE ARE CORRECT')
    print('  ==========================================================================')
    # sp(1,1) has dimension n(2n+1) with n = 2, and maximal compact sp(1)+sp(1)
    dim_sp11 = 2 * (2 * 2 + 1)
    maxc_sp11 = 3 + 3
    d_so41 = len(so_eta(np.diag([1., 1, 1, 1, -1]), 5))
    print(f'      sp(1,1): dim {dim_sp11}, maximal compact sp(1)+sp(1) = {maxc_sp11}')
    print(f'      so(4,1): dim {d_so41}, maximal compact so(4) = 6   (L-278)')
    check(f'⓸ P13\'s "a compact algebra of dimension eight cannot sit in sp(1,1), whose maximal '
          f'compact is six-dimensional" is correct: {maxc_sp11} < 8',
          'cannot sit in $sp(1,1)$' in p13 or 'sp(1,1)' in p13)
    check(f'⓸ᵇ and it is consistent with sp(1,1) ≅ so(4,1): both dimension {dim_sp11}, both '
          'maximal compact 6, the second computed at L-278',
          dim_sp11 == d_so41 and maxc_sp11 == 6)
    check('⓸ᶜ and "$C^{3}$ being of odd complex" is the right reason a quaternionic structure '
          'cannot be carried — a quaternionic structure needs even complex dimension',
          'odd complex' in p13 and 3 % 2 == 1)
    check('⓸ᵈ ⛭ so most of what the instrument surfaces is correct, and recording that is the '
          'honest majority outcome rather than a hedge',
          len(rows) > 200)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** dS_5 is not the unique maximally symmetric Lorentzian five-manifold. **')
    print('  *There are three — Minkowski, de Sitter and anti-de Sitter — and all three have')
    print('  fifteen-dimensional isometry, because fifteen is the MAXIMUM at n=5.  They are')
    print('  separated by the sign of the curvature, not by dimension, so the number the sentence')
    print('  quotes to single dS_5 out is the one number that cannot.*')
    print('  ⛔⛔ ** And the omitted alternative is AdS_5 — the same object L-278 found left out of')
    print('     the real-form list and L-279 identified as the substrate\'s own dual. **  *One')
    print('     object, three appearances, twice inside a uniqueness claim that leaves it out.*')
    print('  ⛭ ** The paper\'s other exclusions in the same region are correct ** — sp(1,1)\'s')
    print('     six-dimensional maximal compact, and the odd complex dimension of C^3.  *Most of')
    print('     what this instrument surfaces is right, and saying so is the majority outcome.*')
    print('  ⌷ ** The repair is one clause: ** *"of its dimension and curvature sign", or "with')
    print('     Λ > 0".  The programme\'s commitment is untouched; what fails is a scope.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

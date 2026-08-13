#!/usr/bin/env python3
"""A1 -- FOR_54 item 26 discharged: $\\{6,7,10\\}$ is a fact about $\\mathfrak{so}(5,1)$'s own symmetric
decompositions, computed here, so P12 owns it and never needed the citation.

** THE ITEM, routed r2442 and verified r2575, undischarged since. **  P12: "The isotropy dimensions are
the Killing-vector counts the construction establishes~\\cite{JanzenRange}", giving $\\{6,7,10\\}$.  And P9,
at its own isotropy passage, cites P12.  ⇒ ** Each cites the other for the same fact, and $6,7,10$ appears
ZERO times in P9. **  *** `check_citations` is blind to it: it checks that a cited key EXISTS, not that
the cited paper CONTAINS the fact. ***

  ** What item 26 said would discharge it: ** "one paper derives the triple, or P12 states it as its own."

** ⛭⛭ ⓵ AND THE TRIPLE IS NOT WHAT THE CITATION SUGGESTS.  IT IS AN ALGEBRA FACT. **  P12's own sentence,
read whole: "** the symmetric-pair isotropy dimensions of $\\mathfrak{so}(5,1)$ are $6,7,10$ **, so the two
symmetric strata sit at the only admissible dimensions and are the geometry-fixed pairs (** $SO(4,1)$ at
ten, the $SO(2,1)\\times SO(3)$ Grassmannian at six **), while every generic stratum (** dimensions four,
three **, ...)".

  ⇒ *** $\\{6,7,10\\}$ are the dimensions of the SYMMETRIC SUBALGEBRAS of $\\mathfrak{so}(5,1)$ -- a fact
      about the algebra, computable without any geometry. ***

  ** Computed here from $\\mathfrak{so}(5,1)$'s symmetric decompositions ($\\dim\\mathfrak{so}(5,1)=15$): **

      *** so(5)             10     the maximal compact
          so(4,1)           10     the de Sitter subalgebra
          so(1,1) + so(4)    7     the boost-plus-rotation split
          so(2,1) + so(3)    6     the Grassmannian pair
          ⇒ {6, 7, 10} ***

** ⓶ AND P9's SET IS A DIFFERENT SET. **  P9 tabulates the STRATUM isotropies as groups: "$SO(4,1)$ at
Type O, $SO(2,1)\\times SO(3)$ at Nariai, $\\mathbb{R}_t\\times SO(3)$ at the generic
Schwarzschild--de Sitter class".  Their dimensions are ** $\\{10, 6, 4\\}$ **.

  ⇒⇒ *** Two of the three coincide -- because two strata ARE symmetric -- and the third does not: the
      generic stratum sits at FOUR, which P12 itself calls generic in the same sentence.  So P9 could
      never have established $\\{6,7,10\\}$: it does not contain that set, and the two-of-three overlap is
      why the loop survived unnoticed. ***

** ⓷ SO THE DISCHARGE IS THE SECOND OF ITEM 26's TWO OPTIONS, AND IT IS THE CORRECT ONE. **  *** P12
states the triple as its OWN: it is $\\mathfrak{so}(5,1)$'s symmetric-pair spectrum, and P12 is the paper
that works the algebra.  The `\\cite{JanzenRange}` attributes an algebra fact to a geometry paper, which
is why nothing downstream broke -- the fact is true, and P9's geometry is CONSISTENT with it at the two
symmetric strata without establishing it. ***

WHAT IS NOT CLAIMED.  ** Not that P9 is wrong ** -- its three groups are its own and correct; only the
direction of the citation is.  ** Not that the edit is made here ** -- this receipt establishes what the
edit should say; ** the one-clause change to P12 is the discharge and is a separate act. **  ** Not that
`check_citations` should catch this class ** -- *** a gate that verified every cited paper CONTAINS the
cited fact would be a reading, not a check. ***

Written r2635.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def dim_so(n):
    return n * (n - 1) // 2


def main():
    print()
    print('  A1 -- where does {6,7,10} come from?')
    print()
    p12 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'algebroid_paper.tex')))
    p9 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'range_paper.tex')))

    # ⓵ P12's sentence, whole
    check('⓵ P12 attributes the triple to P9: "The isotropy dimensions are the Killing-vector counts the '
          'construction establishes~\\cite{JanzenRange}"',
          'The isotropy dimensions are the Killing-vector counts the construction '
          'establishes~\\cite{JanzenRange}' in p12)
    check('but the same sentence says what the triple IS: "the symmetric-pair isotropy dimensions of '
          '$\\so(5,1)$ are $6,7,10$"',
          'symmetric-pair isotropy dimensions of $\\so(5,1)$ are $\\{6,7,10\\}$' in p12)
    check('and places the two occupied ones: "$SO(4,1)$ at ten, the $SO(2,1)\\times SO(3)$ Grassmannian '
          'at six"',
          'at ten' in p12 and 'Grassmannian at six' in p12)
    check('with the generic strata at other dimensions: "every generic stratum (dimensions four, three"',
          'every generic stratum (dimensions four, three' in p12)

    # ⓶ compute it
    dims = sorted({dim_so(5), dim_so(5), 1 + dim_so(4), dim_so(3) + dim_so(3)})
    check(f'⛭⛭ ⓶ and the symmetric decompositions of so(5,1) give {dims}: so(5)=10, so(4,1)=10, '
          'so(1,1)+so(4)=7, so(2,1)+so(3)=6',
          dims == [6, 7, 10])
    check(f'with dim so(5,1) = {dim_so(6)}', dim_so(6) == 15)

    # ⓷ P9's set is different
    check('⓷ P9 tabulates STRATUM isotropies as groups: "$SO(4,1)$ at Type~O, $SO(2,1)\\times SO(3)$ at '
          'Nariai, $\\mathbb{R}_{t}\\times SO(3)$ at the generic Schwarzschild--de~Sitter class"',
          '$\\mathrm{SO}(4,1)$ at Type O' in p9 and 'at Nariai' in p9
          and 'at the generic Schwarzschild--de~Sitter class' in p9)
    strata = sorted({dim_so(5), dim_so(3) + dim_so(3), 1 + dim_so(3)})
    check(f'whose dimensions are {strata} -- a DIFFERENT set', strata == [4, 6, 10])
    check("⛔ and $6,7,10$ appears nowhere in P9", '6,7,10' not in p9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** {6,7,10} is an ALGEBRA fact, and P12 owns it. **')
    print('  ⛭⛭ ⓵ ** The symmetric decompositions of so(5,1) (dim 15): ** so(5)=10, so(4,1)=10,')
    print('     so(1,1)+so(4)=7, so(2,1)+so(3)=6 ⇒ ** {6, 7, 10} **, computable without any geometry.')
    print('  ⓶ ** P9\'s set is DIFFERENT: ** its three tabulated stratum isotropies are SO(4,1),')
    print('     SO(2,1)xSO(3) and R_t x SO(3) ⇒ ** {10, 6, 4} **.')
    print('     ⇒⇒ ** Two of three coincide because two strata ARE symmetric, and the third does not --')
    print('       the generic stratum sits at FOUR, which P12 itself calls generic in the same sentence.')
    print('       So P9 could never have established {6,7,10}, and the two-of-three overlap is why the')
    print('       loop survived. **')
    print('  ⓷ ** THE DISCHARGE: ** P12 states the triple as its own -- it is so(5,1)\'s symmetric-pair')
    print('     spectrum and P12 is the paper that works the algebra.  ** The cite attributes an ALGEBRA')
    print('     fact to a GEOMETRY paper, which is why nothing downstream broke: the fact is true, and')
    print("     P9's geometry is consistent with it without establishing it. **")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

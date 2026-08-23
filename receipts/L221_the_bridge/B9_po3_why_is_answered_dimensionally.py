#!/usr/bin/env python3
"""B9 -- `PO-3`'s "why" is answered, dimensionally: the parity doubling exists because the mass function
is odd in the signed offset exactly when $D$ is even.

** THE ITEM, never worked (0 dated moves before this). **  `PO-3`: "The $a_2$-meaning drill-site --- ** why
does the SdS geometry produce a zero-sum triple with a $\\mathbf3/\\bar{\\mathbf3}$ parity doubling **, and
does that reason ...", targeting "** the $A_2$ skeleton and the parity doubling **".

** ⛭⛭ ⓵ THE $A_2$ SKELETON IS IDENTIFIED, AND IT IS THE OFFSET-TO-MASS CUBIC. **  P13: "the offset-to-mass
map is no mere labelling: it is a cubic, $2M=((r_0/\\alpha)-(r_0/\\alpha)^3)$, ** whose three zero-sum roots
are the $A_2$ weights that $S_3$ permutes **---mass-tied, moving with $2M$---so ** the geometry does carry
a genuine three-fold $R$-odd mass structure **".

  ⇒ ** So "the zero-sum triple" is the cubic's roots and "the $A_2$ skeleton" is what they form. **  *** Not
    a resemblance: the roots ARE the weights, and $S_3$ permutes them. ***

** ⛭⛭⛭ ⓶ AND THE "WHY" OF THE PARITY DOUBLING IS ANSWERED, IN P14, AS A DIMENSIONAL FACT. **  The
$D$-selection argument runs on two conditions, and the SECOND is exactly this row's question:

  "The second condition is ** the parity **, and it separates those two.  ** The mass function is odd in
   the signed offset exactly when $D$ is even **, so ** at $D=5$ the orientation parity $r_0\\to-r_0$ fixes
   each geometry rather than exchanging it with its conjugate: there is no mass-reflection
   $\\mathbb{Z}_2$, hence no $\\mathbf3\\oplus\\bar{\\mathbf3}$ Nariai hexad, no outer factor of
   $\\mathrm{Aut}(A_2)=S_3\\rtimes\\mathbb{Z}_2$, and no $\\gamma^5$ **"

  ⇒⇒ *** THE ANSWER, read forward: the doubling exists at $D=4$ BECAUSE the mass function is odd in the
      signed offset there, so the orientation parity EXCHANGES each geometry with its conjugate rather
      than fixing it.  That exchange IS the $\\mathbf3/\\bar{\\mathbf3}$ doubling, and it is what supplies
      the outer $\\mathbb{Z}_2$ of $\\mathrm{Aut}(A_2)$ and $\\gamma^5$ with it. ***

** ⓷ AND THE ROW'S SECOND CLAUSE -- "does that reason ..." -- HAS ITS ANSWER TOO. **  The same passage
uses the parity as ** a $D$-selection condition **: it rules out $D=5$, where the first condition (the
harmonic collapse, "at $D=5$ the collapse does occur, at scale $1$, and returns a four-fold") would
otherwise have admitted it.
  ⇒ *** So the reason for the doubling is not a local curiosity: it is one of the two conditions that
      select $D=4$, and P14 uses it as such. ***  ** That is the third $D=4$ argument rehomed at r2582,
      seen from the other end. **

WHAT IS NOT CLAIMED.  ** Not that `PO-3` closes ** -- `F5` reserves that, and the row's own status text
carries corrections from the colour arc that are not audited here.  ** Not that the mass VALUES realise
the three-fold splitting ** -- P13 marks that separately: "whether their masses realise its three-fold
splitting---a ph[ysical question]".  ** Not that this is new physics ** -- *** every clause quoted is in
the papers; what was missing was the connection between the row's question and the passage that answers
it. ***

Written r2627.  Stated for reversal.
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


def main():
    print()
    print("  B9 -- is PO-3's 'why' answered anywhere?")
    print()
    p13 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'boundary_paper.tex')))
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(l for l in raw.split('\n')
               if re.match(r'\|\s*~?~?\*\*PO-3\*\*', l))

    # the question
    check("⓵ PO-3 asks why the geometry produces \"a zero-sum triple with a "
          '$\\mathbf3/\\bar{\\mathbf3}$ parity doubling"',
          'parity doubling' in row and 'zero-sum triple' in row)
    check('targeting "the $A_2$ skeleton and the parity doubling"',
          'the $A_2$ skeleton and the parity doubling' in row)

    # ⓵ the A2 skeleton is the cubic's roots
    check('⛭⛭ ⓶ P13 identifies the skeleton: the offset-to-mass map "is a cubic ... whose three zero-sum '
          'roots are the $A_2$ weights that $S_3$ permutes"',
          'whose three zero-sum roots are the $A_{2}$ weights that $S_{3}$ permutes' in p13
          or 'whose three zero-sum roots are the $A_2$ weights that $S_3$ permutes' in p13)

    # ⓶ the why, dimensionally
    check('⛭⛭⛭ ⓷ and P14 answers the WHY: "The mass function is odd in the signed offset exactly when '
          '$D$ is even"',
          'The mass function is odd in the signed offset exactly when $D$ is even' in p14)
    check('with the consequence at $D=5$ spelled out: "the orientation parity $r_{0}\\to-r_{0}$ fixes '
          'each geometry rather than exchanging it with its conjugate"',
          '\\emph{fixes} each geometry rather than exchanging it with its conjugate' in p14)
    check('and what is then absent: "there is no mass-reflection $\\mathbb{Z}_{2}$, hence no '
          '$\\mathbf3\\oplus\\bar{\\mathbf3}$ Nariai hexad, no outer factor of '
          '$\\mathrm{Aut}(A_{2})=S_{3}\\rtimes\\mathbb{Z}_{2}$, and no $\\gamma^{5}$"',
          'there is no mass-reflection' in p14 and 'Nariai hexad' in p14
          and 'no outer factor of' in p14)

    # ⓷ it is a D-selection condition
    check('⓸ and P14 uses it as a $D$-selection condition: "The second condition is the parity, and it '
          'separates those two"',
          'The second condition is the parity, and it separates those two' in p14)
    check('against the first, which alone would admit $D=5$: "At $D=5$ the collapse does occur, at scale '
          '$1$, and returns a four-fold"',
          'the collapse does occur, at scale' in p14 and 'returns a four-fold' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-3's 'why' is answered, dimensionally, and the row never knew. **")
    print('  ⛭⛭ ⓵ ** The $A_2$ skeleton IS the offset-to-mass cubic: ** its "three zero-sum roots are the')
    print('     $A_2$ weights that $S_3$ permutes" -- not a resemblance, an identity.')
    print('  ⛭⛭⛭ ⓶ ** And the WHY is a dimensional fact: ** "The mass function is odd in the signed')
    print('     offset ** exactly when D is even **".')
    print('     ⇒ ** Read forward: at D=4 the orientation parity EXCHANGES each geometry with its')
    print('       conjugate rather than fixing it -- and that exchange IS the 3/3̄ doubling, supplying')
    print('       the outer Z2 of Aut(A_2) and γ⁵ with it. **')
    print('  ⓷ ** And P14 uses the parity as a D-SELECTION condition: ** it rules out D=5, where the')
    print('     harmonic collapse alone "returns a four-fold".')
    print('     ⇒ ** So the reason is not a local curiosity: it is one of the two conditions that select')
    print('       D=4 -- the third D=4 argument, seen from the other end. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

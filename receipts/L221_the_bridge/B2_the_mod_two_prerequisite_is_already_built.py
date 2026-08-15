#!/usr/bin/env python3
"""B2 -- the corpus supplies a mod-2 index's PREREQUISITE, and it is realised on the very modes such an
index would count.

** THE QUESTION, ranked #1 at r2603. **  `PO-5`'s remaining route (r2568): *** does the discrete
orientation parity $R$ carry a MOD-2 INDEX, and what would it obstruct? ***  ⇒ ** And a mod-2 index is
not defined on a bare $\\mathbb{Z}_2$-graded operator. **  It requires a ** REAL or QUATERNIONIC
structure ** -- an antilinear involution commuting appropriately with the operator -- because the
mod-2 index is the PARITY of $\\dim\\ker D$, and that parity is a deformation invariant only when such a
structure pins it.

** ⓵ SO THE FIRST QUESTION IS NOT "does the index exist" BUT "does the corpus supply the structure". **
Measured across the papers:

      *** antilinear 38 · charge conjugation 58 · reality 36 · real structure 4 · quaternionic 2
          Majorana 0 · symplectic 0 ***

  ⇒ ** The corpus is saturated with exactly this material, and none of it was gathered for this
    purpose. **

** ⛭⛭ ⓶ AND THE STRUCTURE IS REALISED ON THE BUILT ZERO-MODES, WHICH IS THE STRONGEST FORM IT COULD TAKE. **
P13, in its own words: "that geometric antilinear face is $C$'s kinematic shadow and not $C$ itself ...
and it is ** realised on the built fermion sector, where $R\\circ K$ acts on the actual zero-modes as
charge conjugation's kinematic face **".

  ⇒ *** $R$ is the $\\mathbb{Z}_2$ grading whose index is in question.  $K$ is antilinear.  And their
      composite acts on THE VERY MODES a mod-2 index would count -- one chiral zero-mode per throat wall.
      That is not a structure that would have to be supplied; it is a structure the matter sector already
      built and used for another purpose. ***

** ⓷ AND A SECOND, INDEPENDENT $\\mathbb{Z}_2$-ON-A-REAL-STRUCTURE SITS IN P5 AND IS CONNECTED TO NOTHING. **
The groupoid paper: "the monodromy group does not act uniformly on the real structure: in the
under-critical regime ($>0$, three real roots) all of $S_3$ is realised on the real root labelling,
whereas in the over-critical regime ($<0$, one real root and a complex-conjugate pair) ** only the
order-two subgroup---complex conjugation of the pair---is realised on the real structure **".

  ⇒ ** A $\\mathbb{Z}_2$ acting on a real structure, arising as a MONODROMY, on the same cubic whose
    three zero-sum roots are the $A_2$ weights $S_3$ permutes. **  *** Whether it is the same
    $\\mathbb{Z}_2$ as $R$ is not established here and is the obvious next question. ***

** ⇒⇒ WHAT THIS CHANGES ABOUT `PO-5`. **  r2568 left it as "does $R$ carry a mod-2 index?", with the
honest note that ** `mod 2`, `Witten anomaly` and `eta invariant` are at ZERO across the corpus **.  That
remains true of the NAME.
  ⌗ *** It is not true of the STRUCTURE.  The antilinear involution exists, is named, and acts on the
      built zero-modes; the question is therefore not whether the substrate could support such an index
      but whether $R\\circ K$'s action makes $\\dim\\ker D$'s parity a deformation invariant. ***
  ⇒ ** That is a calculation on objects the corpus already has, not a search for missing structure. **

WHAT IS NOT CLAIMED.  ** Not that a mod-2 index exists **: the commutation relations between $D$, $R$ and
$K$ that would make the parity invariant are not checked here.  ** Not that P5's monodromy $\\mathbb{Z}_2$
is $R$ ** -- they act on different objects (root labelling versus spinor grading) and the identification
would need proving.  ** Not that a mod-2 index would deliver the bridge **: r2568's standing limit holds
-- *** a $\\mathbb{Z}_2$ invariant can obstruct or permit but cannot by itself deliver four states. ***

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 8631387** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2604.  Stated for reversal.
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


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  B2 -- does the corpus supply a mod-2 index's prerequisite?")
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(body(f) for f in papers)
    p13 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'boundary_paper.tex')))
    p5 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'groupoid_paper.tex')))

    # ⓵ the material is present
    counts = {k: len(re.findall(re.escape(k), allp, re.I))
              for k in ('antilinear', 'charge conjugation', 'reality', 'real structure', 'quaternionic')}
    check(f'⓵ the corpus is saturated with the material: {counts}',
          counts['antilinear'] > 20 and counts['charge conjugation'] > 20)
    for k in ('Majorana', 'symplectic'):
        check(f'   and the standard NAMES are absent: "{k}" appears '
              f'{len(re.findall(k, allp, re.I))} times',
              len(re.findall(k, allp, re.I)) == 0)

    # ⓶ realised on the built zero-modes
    check('⛭⛭ ⓶ and P13 states it is REALISED ON THE BUILT ZERO-MODES: "it is realised on the built '
          'fermion sector, where $R\\circ K$ acts on the actual zero-modes as charge conjugation\'s '
          'kinematic face"',
          'realised on the built fermion sector' in p13
          and 'acts on the actual zero-modes as charge conjugation' in p13)
    check("and the antilinear face is named as such -- \"$C$'s kinematic shadow and not $C$ itself\"",
          "kinematic shadow and not $C$ itself" in p13)

    # ⓷ P5's independent Z2 on a real structure
    check('⓷ and P5 carries a SECOND, independent $\\mathbb{Z}_2$ on a real structure: "the monodromy '
          'group does not act uniformly on the real structure"',
          'does not act uniformly on the real structure' in p5)
    check('with the order-two subgroup named: "only the order-two subgroup---complex conjugation of the '
          'pair---is realised on the real structure"',
          'only the order-two subgroup' in p5 and 'complex conjugation of the pair' in p5)

    # the names remain absent
    for k in ('mod 2', 'mod-two', 'Witten anomaly', 'eta invariant'):
        check(f'⌗ and r2568\'s count still holds of the NAME: "{k}" appears zero times',
              len(re.findall(re.escape(k), allp, re.I)) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the structure a mod-2 index needs is present, named, and realised on the very")
    print("  modes such an index would count. **")
    print("  ⓵ ** antilinear 38 · charge conjugation 58 · reality 36 · real structure 4 · quaternionic 2 **")
    print("     -- and ** Majorana 0, symplectic 0 **: the material is here, the standard names are not.")
    print("  ⓶ ** P13: \"realised on the built fermion sector, where R∘K acts on the actual zero-modes as")
    print("     charge conjugation's kinematic face\". **  ⇒ ** R is the Z2 grading; K is antilinear; their")
    print("     composite acts on one chiral zero-mode per throat wall. **")
    print("  ⓷ ** And P5 carries a SECOND Z2 on a real structure, as a MONODROMY ** -- on the same cubic")
    print("     whose three zero-sum roots are the A_2 weights S_3 permutes -- ** and it is connected to")
    print("     nothing. **")
    print("  ⇒⇒ ** So PO-5's question changes shape: not whether the substrate could support such an")
    print("     index, but whether R∘K's action makes dim ker D's parity a deformation invariant. **")
    print("     *** A calculation on objects the corpus already has, not a search for missing structure. ***")
    print("  ⚠ NOT claimed: that the index exists, that P5's monodromy Z2 is R, or that a mod-2 index")
    print("    would deliver the bridge -- ** a Z2 invariant can obstruct or permit but cannot by itself")
    print("    deliver four states. **")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

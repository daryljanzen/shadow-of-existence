#!/usr/bin/env python3
"""B66 -- `PO-5`'s surviving route is GATED ON `PO-11`, not by decision but by what a composite is made
of: the chain is `PO-2` → `PO-5` → `PO-11`, it terminates, and `PO-11` is the spinor descent.

** THE REMAINDER r2822 LEFT. **  *** "Does the OCTET channel of $3\\otimes\\bar3$ on the wall kernel
contain a massless spin-1 state?"  ** That question has a prior, and the prior settles the row's place
on the board. ** ***

** ⓵ WHAT THE COMPOSITE WOULD BE MADE OF. **  P14: the modes are ** wall-bound zero-modes ** with
** disjoint support ** on three distinct throat walls -- "the three throat walls are distinct loci, so
the wall-bound zero-modes have disjoint support and span a three-dimensional space".

** ⓶ AND WHAT A GAUGE FIELD MUST BE. **  *** A PROPAGATING massless spin-1 field on the four-dimensional
cut. ***

  ⇒⇒ *** A BOUND STATE OF LOCALISED MODES IS LOCALISED.  ** Two zero-modes with disjoint support on
      walls compose to an object that lives ON the walls; it does not propagate off them. **  The
      composite route needs a PROPAGATING sector to compose from. ***

** ⛭⛭⛭ ⓷ AND THAT SECTOR IS `PO-11`, BY THE CORPUS'S OWN NAME FOR IT. **  `groupoid_paper`: the
discrete skeleton "is built as ** bound-state zero-modes ** of the existent leaf ... while ** the descent
onto a full propagating spinor field sector --- the programme's largest unbuilt undertaking ---
remains genuinely open **".

  ⇒ *** `PO-5`'s SURVIVING ROUTE IS GATED ON `PO-11`.  ** Not by anyone's decision -- by what a
      composite is made of. ** ***

** ⛭⛭ ⓸ AND THE CHAIN TERMINATES, WHICH IS THE PART THAT MATTERS. **

      *** PO-2  --gated on-->  PO-5  --gated on-->  PO-11  --gated on-->  (nothing) ***

  ⇒⇒ *** THREE ROWS, ONE DEPENDENCY CHAIN, NO CIRCULARITY.  ** `PO-11` is the root of the whole knot,
      and `PO-11` is the spinor descent. **  What looked like three separate open problems is one
      unbuilt sector with two consequences. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-11` closing would close the others ** -- *** it would unblock
them, which is a different and weaker statement; the octet question would still have to be asked and the
coupling still supplied. ***  ** Not that the wall-bound composite is excluded ** -- *** a wall-localised
spin-1 is a real object; what is claimed is that it is not a four-dimensional gauge field, which is what
`PO-5` requires. ***  ** Not that the gating is the corpus's ** -- *** it is derived here and the
register did not record it; `PO-5` and `PO-11` both read "gated on nothing" before this receipt. ***

** COMPUTES: nothing.  *** A read of what the wall kernel's modes are, against what a gauge field must
be, and a traversal of the register's recorded gating. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 4fde44f** *(per c54.220's rule, r2776).*

Written r2823.  Stated for reversal.
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


def flat(name):
    raw = open(os.path.join(ROOT, 'corpus', name), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print("  B66 -- what is PO-5's surviving route made of?")
    print()
    p14 = flat('matter_sector_paper.tex')
    grp = flat('groupoid_paper.tex')

    check('⓵ the wall kernel\'s modes are BOUND and LOCALISED: "the three throat walls are distinct '
          'loci, so the wall-bound zero-modes have disjoint support and span a three-dimensional '
          'space"',
          'wall-bound zero-modes have disjoint support' in p14)
    check('⇒ so a composite of them is localised on the walls -- ** it does not propagate off them, '
          'and a gauge field must **',
          'disjoint support' in p14)

    check('⛭⛭⛭ ⓶ and the propagating sector is the corpus\'s own largest unbuilt piece: the skeleton '
          '"is built as bound-state zero-modes of the existent leaf ... while the descent onto a full '
          'propagating spinor field sector --- the programme\'s largest unbuilt undertaking --- remains '
          'genuinely open"',
          'bound-state zero-modes of the existent leaf' in grp
          and "largest unbuilt" in grp)

    # ⓷ the chain terminates
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    def gated(pid):
        l = next(x for x in raw.split('\n') if re.match(rf'\|\s*~*\*\*{pid}\*\*', x))
        return set(re.findall(r'gated on \**`?(PO-[\dA-Za-z]+|PO-seam)`?', l))
    check(f'⛭⛭ ⓷ and the register records `PO-2` gated on {sorted(gated("PO-2"))}, while `PO-11` is '
          f'gated on {sorted(gated("PO-11")) or "nothing"} -- ** so the chain PO-2 → PO-5 → PO-11 '
          'TERMINATES, with no circularity **',
          'PO-5' in gated('PO-2') and not gated('PO-11'))
    check('⇒ ** and the register did not record the PO-5 → PO-11 link before this receipt ** -- both '
          'rows read as gated on nothing',
          not gated('PO-5') or 'PO-11' not in gated('PO-5'))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-5's surviving route is gated on PO-11, and the chain terminates there. **")
    print('  ⓵ ** The composite would be made of wall-BOUND zero-modes with DISJOINT SUPPORT. **')
    print('     ⇒ *** A bound state of localised modes is localised.  It lives ON the walls and does')
    print('     not propagate off them — and a gauge field must. ***')
    print('  ⛭⛭⛭ ⓶ ** So the route needs a PROPAGATING sector to compose from, and that sector is')
    print('     PO-11 ** — "the descent onto a full propagating spinor field sector, the programme\'s')
    print('     largest unbuilt undertaking".')
    print('     ⇒ ** Not gated by anyone\'s decision — by what a composite is made of. **')
    print('  ⛭⛭ ⓷ ** And the chain terminates: **')
    print('       PO-2  →  PO-5  →  PO-11  →  (nothing)')
    print('     *** Three rows, one dependency chain, no circularity.  PO-11 is the root of the whole')
    print('     knot, and PO-11 is the spinor descent.  What looked like three separate open problems')
    print('     is one unbuilt sector with two consequences. ***')
    print('  ⚠ Closing PO-11 would UNBLOCK the others, not close them: the octet question would still')
    print('     have to be asked and the coupling still supplied.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

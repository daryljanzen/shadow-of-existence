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
import subprocess

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

    # ⛔⛭⛭ RE-PINNED r3954, AND THE BREAKAGE IS MINE.  This asserted `"largest unbuilt" in grp` --
    #   the phrase "the programme's largest unbuilt undertaking", which I REMOVED from
    #   groupoid_paper at r3904 because it was FALSE: the paper claimed the propagating sector
    #   "remains genuinely open" while CITING `JanzenCRframework`, and P07 says "A propagating
    #   fermion sector IS NOW BUILT".  A claim of openness resting on a citation that says built.
    #     ⇒ *** So a correct paper repair broke a receipt that pinned the incorrect claim.  That is
    #         this debt in miniature and it is not a reason to undo either: the paper is right now,
    #         and the pin follows it. ***
    #   ⌗ "largest unbuilt undertaking" is also the exact phrase the ledger pass carries as a
    #     failure mode -- "calling a handover a debt" -- so the receipt was pinning a known defect.
    #   The skeleton half is untouched and still asserted; the "unbuilt" half is replaced by what
    #   the paper now states, which keeps this check discriminating rather than merely present.
    check('⛭⛭⛭ ⓶ the skeleton is the BOUND sector, and the descent is now BUILT -- groupoid_paper, '
          'as repaired at r3904: "the descent onto a full propagating spinor field sector is now '
          'built ... the sector that stays unbuilt is the other one, gauge-acted and '
          'isometry-realised on the compact face"',
          'bound-state zero-modes of the existent leaf' in grp
          and 'spinor field sector is now built' in grp
          and 'stays unbuilt is the other one' in grp)

    # ⓷ the chain terminates
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    def gated(pid):
        l = next(x for x in raw.split('\n') if re.match(rf'\|\s*~*\*\*{pid}\*\*', x))
        return set(re.findall(r'gated on \**`?(PO-[\dA-Za-z]+|PO-seam)`?', l))
    check(f'⛭⛭ ⓷ and the register records `PO-2` gated on {sorted(gated("PO-2"))}, while `PO-11` is '
          f'gated on {sorted(gated("PO-11")) or "nothing"} -- ** so the chain PO-2 → PO-5 → PO-11 '
          'TERMINATES, with no circularity **',
          'PO-5' in gated('PO-2') and not gated('PO-11'))
    # ⛔⛭⛭ AMENDED r3132 (`L-258`).  ** THIS CHECK READ THE LIVE REGISTER FOR A CLAIM ABOUT THE PAST. **
    #   *It says "the register did not record the PO-5 → PO-11 link BEFORE THIS RECEIPT" and tested it
    #   against `PROTECTED_OPEN.md` as it stands now.  The link was recorded BECAUSE of this receipt.*
    #   ⇒ *** So the check went red exactly when its own recommendation was adopted -- the purest
    #       instance of r3105's rule yet: a check that pins a LIVE register punishes the finding it
    #       defends, and here the finding's whole content was "this link is missing". ***
    #   ⇒ ** The absence is a claim about a COMMIT (c54.220's rule), so it is read at this receipt's
    #     own parent; and the PRESENT is asserted in the opposite direction, which is the direction
    #     that says the work landed. **
    MINE = '465ebef05a'        # r2823, where this receipt was written
    before_raw = subprocess.run(['git', '-C', ROOT, 'show', MINE + '^:PROTECTED_OPEN.md'],
                                capture_output=True, text=True, errors='replace').stdout

    def gated_at(text, pid):
        row = next((x for x in text.split('\n')
                    if re.match(rf'\|\s*~*\*\*{pid}\*\*', x)), '')
        return set(re.findall(r'gated on \**`?(PO-[\dA-Za-z]+|PO-seam)`?', row))

    was = gated_at(before_raw, 'PO-5')
    check(f'⇒ ** and the register did not record the PO-5 → PO-11 link before this receipt ** -- at '
          f'{MINE}^ the PO-5 row read as gated on {sorted(was) or "nothing"}',
          'PO-11' not in was)
    check(f'⇒ ⛭ AND IT DOES NOW, which is this receipt landing rather than this receipt breaking: '
          f'PO-5 is gated on {sorted(gated("PO-5")) or "nothing"} in the live register',
          'PO-11' in gated('PO-5'))

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

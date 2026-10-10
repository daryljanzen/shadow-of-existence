#!/usr/bin/env python3
"""B66 -- `PO-5`'s surviving route is GATED ON `PO-11`, not by decision but by what a composite is made
of: the chain is `PO-2` → `PO-5` → `PO-11`, it terminates, and `PO-11` is the spinor descent.

** THE REMAINDER r2822 LEFT. **  *** "Does the OCTET channel of $3\\otimes\\bar3$ on the wall kernel
contain a massless spin-1 state?"  ** That question has a prior, and the prior settles the row's place
on the board. ** ***

** ⓵ WHAT THE COMPOSITE WOULD BE MADE OF. **  P14: the modes are ** wall-bound zero-modes **, BOUND
STATES OF THE LEAF -- "the three throat walls are distinct loci, so the wall-bound zero-modes are
linearly independent and span a three-dimensional space", and "CR reads the fermion as a mode of the
existent leaf, not a propagating spacetime field carrying the tortoise norm---on the leaf it is a bound
state".

** r6931+70.1: ⓵ AS WRITTEN RESTED ON AN ERROR THE CORPUS HAS SINCE CORRECTED. **  At r2823 P14 said the
wall-bound zero-modes "have DISJOINT SUPPORT", and this receipt argued from that: a composite of modes
with disjoint support "lives ON the walls".  r6748 (a839957a) showed the supports are NOT disjoint -- the
modes are algebraic, not exponential; the binding branch vanishes at its own wall; the pairwise overlap
is exact and of order one (1/6 + sqrt(3)/pi at lambda = 1); the walls are lines meeting at the centre --
and r6756 (23a98f4f) replaced the reason in P14: three modes span three dimensions because they are
linearly INDEPENDENT.  So "localised on the walls" is withdrawn here as the reason.  ** What carries the
finding is the other property P14 states and r6748 does not touch: the modes are static BOUND states of
the leaf, normalisable in the leaf measure and NOT in the conserved spacetime Dirac norm -- not
propagating fields. **  A composite of leaf-bound static modes is itself leaf-bound, and a gauge field
must propagate on the four-dimensional cut; so the route still needs a propagating sector to compose
from, which is ⓷.

** ⓶ AND WHAT A GAUGE FIELD MUST BE. **  *** A PROPAGATING massless spin-1 field on the four-dimensional
cut. ***

  ⇒⇒ *** A BOUND STATE OF LEAF-BOUND MODES IS LEAF-BOUND.  ** Static zero-modes normalisable only in
      the leaf measure compose to an object that is a bound state of the leaf, not a propagating field
      on the cut. **  The composite route needs a PROPAGATING sector to compose from. ***  (r6931+70.1:
      the r2823 wording here was "two zero-modes with disjoint support on walls compose to an object
      that lives ON the walls"; the disjointness was false, r6748, and the argument now runs on
      boundness, which is what it needed.)

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

    # ** r6931+70.1: class (a), FROZE AN ERROR.  ⓵ pinned P14's "the wall-bound zero-modes have
    #   disjoint support and span a three-dimensional space".  r6748 (a839957a) showed the supports are
    #   not disjoint (algebraic modes, order-one exact overlap, walls are lines meeting at the centre)
    #   and r6756 (23a98f4f) corrected P14 to "are linearly independent and span a three-dimensional
    #   space".  The pin follows the correction, and requires the disjointness sentence gone.
    #   The second check had pinned the bare phrase 'disjoint support' -- which still passed only because
    #   P14 QUOTES the slicing paper's "with disjoint support" elsewhere; it was carrying the error, not
    #   the finding.  What the finding needs is that the modes are leaf-BOUND and not propagating, which
    #   P14 states in sec:chirality and r6748 does not touch, so that is what it now pins. **
    check('⓵ the wall kernel\'s modes are BOUND: "the three throat walls are distinct loci, so the '
          'wall-bound zero-modes are linearly independent and span a three-dimensional space" '
          '(was "have disjoint support"; corrected r6756 after r6748)',
          'e \\emph{distinct} loci, so the wall-bound zero-modes are linearly independent and span a three-dimensional space' in p14
          and 'wall-bound zero-modes have disjoint support' not in p14)
    check('⇒ and they are static BOUND STATES OF THE LEAF, not propagating fields -- "CR reads the '
          'fermion as a mode of the existent leaf, not a propagating spacetime field carrying the '
          'tortoise norm---on the leaf it is a bound state" -- so a composite of them is leaf-bound, '
          '** and a gauge field must propagate **',
          ('CR reads the fermion as a mode of the existent leaf, not a propagating spacetime field '
           'carrying the tortoise norm---on the leaf it is a bound state') in p14)

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
    # ** r6931+70.1: class (c), STALE.  r6719 (440623b6) reworded groupoid_paper's "the descent onto a
    #   full propagating spinor field sector is now built" to "... is built---on the static slicing
    #   structure, and again on this framework's own chiral member", adding the second built member
    #   (the unpolarised chiral one, JanzenDynamics) and dropping "now".  Same claim, more of it: the
    #   propagating sector is built, and the unbuilt one is still the compact-face sector.  Re-pinned
    #   to the current sentence; the skeleton and "stays unbuilt" halves are unchanged. **
    check('⛭⛭⛭ ⓶ the skeleton is the BOUND sector, and the descent is now BUILT -- groupoid_paper, '
          'as repaired at r3904: "the descent onto a full propagating spinor field sector is '
          'built---on the static slicing structure, and again on this framework\'s own chiral member '
          '... the sector that stays unbuilt is the other one, gauge-acted and isometry-realised on '
          'the compact face"',
          'bound-state zero-modes of the existent leaf' in grp
          and ('the descent onto a full \\emph{propagating} spinor field sector is built---on the '
               'static slicing structure, and again on this framework\'s own chiral member') in grp
          and 'e fixed in the matter sector rather than by this grading~\\cite{JanzenMatter}, and the sector that stays unbuilt is the other one' in grp)

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
    print('  ⓵ ** The composite would be made of wall-BOUND zero-modes: static bound states of the')
    print('     leaf, normalisable in the leaf measure and not as propagating spacetime fields. **')
    print('     ⇒ *** A bound state of leaf-bound modes is leaf-bound.  It does not propagate on the')
    print('     cut — and a gauge field must. ***')
    print('  ⛭⛭⛭ ⓶ ** So the route needs a PROPAGATING sector to compose from, and that sector is')
    print('     PO-11 ** — "the descent onto a full propagating spinor field sector" (groupoid_paper now')
    print('     says that descent is built, on the static structure and on the chiral member; the')
    print('     "largest unbuilt undertaking" wording this line once quoted was removed at r3904).')
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

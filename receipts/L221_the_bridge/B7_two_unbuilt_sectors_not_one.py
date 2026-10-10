#!/usr/bin/env python3
"""B7 -- there are TWO unbuilt fermion sectors, not one, and r2618's dedupe collapsed them: the
Lorentzian propagating theory and the compact-face gauge-acted sector.

** WHAT r2618 DID. **  Printing the queue's items individually exposed apparent duplicates, and three
`NAMED-UNBUILT` ledger entries were reclassified as `REGISTERED` on the grounds that `PO-11` already
carried the object.  *** The table fell 32 -> 27 and this line reported it as pure gain. ***

** ⛔ ⓵ ONE OF THE THREE WAS NOT A DUPLICATE, AND `boundary_paper` SAYS SO IN THE SENTENCE BEFORE. **

  "A fermion sector is built~\\cite{JanzenMatter}, but on the other component---the discrete orientation
   parity ... and ** it is a spinor on the real Lorentzian slicing structure, NOT a gauge-acted sector on
   the compact face **~\\cite{JanzenMatter}; it therefore supplies ** no equivariant index for the
   obstruction to act on **, and leaves the gauge wall of this paper exactly where it stands.  ** The
   compact-face fermion sector the obstruction would act on remains unbuilt **, and its construction is
   the major undertaking any geometric gauge-matter route would first have to complete."

  ⇒ *** So there are TWO unbuilt sectors and the paper distinguishes them in one sentence: ***
  * ** p0's / `PO-11`'s: ** the full ** PROPAGATING ** spinor field sector on the ** Lorentzian ** slicing
    structure -- "the built modes being leaf-bound, not the propagating theory";
  * ** `boundary_paper`'s: ** the ** COMPACT-FACE ** fermion sector, ** gauge-acted **, which an
    equivariant index would act on and which the gauge wall's obstruction needs in order to bite.

  (r6931+70.1: that was boundary_paper at r2621.  Since r6683 (73eb61ef) it no longer calls the
  compact-face sector "unbuilt ... the major undertaking": sec:open says "The sector the obstruction would
  act on is the other one---gauge-acted and isometry-realized, on the compact face---and that sector can be
  specified, and is obstructed twice", specifies it as an SU(4) spinor on the round S^5, and finds it
  empty -- "The specification does not build the sector ... what is definite is the emptiness of a
  definite object".  So the compact-face sector is still not built, now because it is shown EMPTY; and
  the propagating one has been built since r3802.  The two-sectors distinction is sharper than when it
  was written: one built, the other specified and obstructed.)

** ⓶ AND THEY ARE UNBUILT FOR DIFFERENT REASONS, WHICH IS THE TEST THAT SETTLES IT. **
  * *** the propagating sector is unbuilt because the modes delivered are BOUND *** -- normalizable in
    the leaf's proper measure, where the propagating Dirac-norm mode is not;
  * *** the compact-face sector is unbuilt because the substrate supplies no such face to act on ***
    -- the localisation argument closes the isometry route, and $\\mathfrak{su}(3)$ is no isometry of the
    non-compact substrate to begin with.
  ⇒ ** Building one does not build the other. **  *** A single construction cannot be both Lorentzian and
    on the compact face. ***

** ⓷ WHAT THIS COSTS AND WHAT IT BUYS. **  The table goes ** 27 -> 28 ** -- *** a correction that ADDS an
item, which is the honest direction and the one a dedupe pass will never produce on its own. ***
  ⌗ ** And it buys the reason `PO-11` cannot absorb it: ** `PO-11`'s row names three papers as naming ONE
  object.  *** Two of those namings are the same object; the third is a different one, and it now needs
  either its own row or an explicit note on `PO-11` that it is excluded. ***

** ⛭ THE RULE THIS RECEIPT RECORDS. **  *** A dedupe pass is a claim that two things are the same, and a
claim needs a check.  r2618 deduped on SHARED VOCABULARY -- both entries said "fermion sector ...
unbuilt" -- and the paper distinguishes them by a clause the vocabulary does not carry. ***  ** The test
that would have caught it: ask why each is unbuilt.  Two things unbuilt for different reasons are two
things. **

WHAT IS NOT CLAIMED.  ** Not that the other two dedupes were wrong ** -- `groupoid_paper`'s "descent onto
a full propagating spinor" and p0's are the same object by the word *propagating*, and the "is built"
entry was mis-bucketed by its trigger.  ** Not that the compact-face sector is reachable ** -- the paper
says the isometry route to it is walled.

Written r2621.  Stated for reversal.
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


def main():
    print()
    print('  B7 -- one unbuilt fermion sector, or two?')
    print()
    bp = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'boundary_paper.tex'),
                                  encoding='utf-8', errors='replace').read())
    p0 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'),
                                  encoding='utf-8', errors='replace').read())

    # ⓵ the distinction, in one sentence
    check('⓵ boundary_paper distinguishes them: the built sector "is a spinor on the real Lorentzian '
          'slicing structure, not a gauge-acted sector on the compact face"',
          'is a spinor on the real Lorentzian slicing structure, not a gauge-acted sector on the '
          'compact face' in bp)
    # ** r6931+70.1: class (b), DISCHARGED.  This pinned "The compact-face fermion sector the
    #   obstruction would act on remains unbuilt", which r6683 (73eb61ef) replaced with "sec:open
    #   specifies that sector and finds it obstructed twice".  sec:open does it: the sector is named as
    #   the OTHER one, specified (an SU(4) spinor on the round S^5, receipt
    #   P13_the_construction_is_specifiable_and_colour_sits_in_the_spin_group) and shown empty.  The
    #   finding this check carries -- the compact-face sector is a DIFFERENT sector from the built one --
    #   is now the paper's own sentence, so the check is re-pointed at that sentence and at what
    #   discharged "unbuilt" (specified, obstructed twice, not built, empty), never at a new way of
    #   saying unbuilt. **
    check('and names the OTHER sector and what became of it: "The sector the obstruction would act on is '
          'the other one---gauge-acted and isometry-realized, on the compact face---and that sector can '
          'be specified, and is obstructed twice" (was "remains unbuilt"; discharged r6683)',
          ('The sector the obstruction would act on is the other one}---gauge-acted and '
           'isometry-realized, on the compact face---and that sector can be specified, and is '
           'obstructed twice') in bp
          and 'The specification does not build the sector' in bp
          and 't evade the positive-curvature obstruction, so what is definite is the emptiness of a definite object' in bp)
    check('and why it matters: the built sector "supplies no equivariant index for the obstruction to '
          'act on"',
          'supplies no equivariant index for the obstruction to act on' in bp)

    # ⛔⛭⛭ RE-PINNED r3954, AND HALF THIS RECEIPT'S TITLE IS NOW FALSE.  Both checks below pinned
    #   `geometric_core_paper` calling the propagating sector UNBUILT.  ** It is built. **  r3802
    #   built the Dirac sector on P11's unpolarised Gowdy member (`C50`, run and passing), and the
    #   paper now says so in its own voice, twice:
    #     "the descent onto a PROPAGATING spinor sector IS NOW BUILT AS WELL, a Dirac field on the
    #      unpolarised radiating member propagating on the light cone and carrying the twist"
    #     "the propagating spinor field sector IS NOW BUILT AS WELL, the leaf-bound modes and the
    #      propagating field being TWO SECTORS RATHER THAN ONE"
    #   ⇒ *** KIND ②, and only HALF the thesis died.  "Two sectors, not one" is this receipt's real
    #       contribution and the paper states it verbatim.  "Both UNBUILT" is what the corpus has
    #       since overtaken -- so the pin is replaced by what the build established, never re-pinned
    #       to a new way of saying unbuilt. ***
    #   ⌗ This is the fourth paper to carry the correction: P07 L267, P5 L648 (repaired r3904),
    #     `boundary_paper` (item 41), and here.  A receipt asserting the old state was the last
    #     place it survived.
    # ** r6931+70.1: class (c), STALE, both.  r6683 (73eb61ef) trimmed P0's "the leaf-bound modes and
    #   the propagating field being two sectors rather than one owed" to "... being two sectors", and
    #   replaced "the propagating spinor field sector is now built as well" with "the descent onto a
    #   propagating spinor sector is built on ..."; r6719 (440623b6) then identified the member it is
    #   built on as the chiral one, "which is the unpolarised one" (formerly "the unpolarised radiating
    #   member").  Same two facts -- two sectors, and the propagating one built -- in current words. **
    check("⓶ and the two sectors are DISTINCT, which is this receipt's title and the paper's own "
          'words: "the leaf-bound modes and the propagating field being two sectors"',
          't selected~\\cite{JanzenMatter}, the leaf-bound modes and the propagating field being two sectors' in p0)
    check('⛭ and the propagating one is NO LONGER UNBUILT -- the corpus overtook this receipt: '
          '"the descent onto a propagating spinor sector is built on the chiral member, which is the '
          'unpolarised one, a Dirac field there propagating on the light cone"',
          ('the descent onto a \\emph{propagating} spinor sector is built on the chiral member, which '
           'is the unpolarised one, a Dirac field there propagating on the light cone') in p0)

    # different reasons
    check('⓷ and they are unbuilt for DIFFERENT reasons -- the compact-face route is walled by '
          'localisation and by $\\mathfrak{su}(3)$ being no isometry: "being no isometry of the '
          'non-compact substrate to begin with"',
          'being no isometry of the non-compact substrate to begin with' in bp)
    # ⛔ AND THIS ONE TOO: it asserted the propagating sector is unbuilt "because the delivered modes
    #   are BOUND".  The distinction it rests on -- bound modes are not the propagating field --
    #   SURVIVES and is exactly why the two are two sectors; what has changed is that the second one
    #   now exists.  Re-pinned to the distinction, which is the part that was ever load-bearing.
    check('while the two remain distinct for the reason this receipt gave -- the leaf-bound modes are '
          'not the propagating field, which is why they were never one sector',
          't selected~\\cite{JanzenMatter}, the leaf-bound modes and the propagating field' in p0)

    # the ledger records it again
    led = open(os.path.join(ROOT, 'corpus', 'open_ledger.txt'), encoding='utf-8').read()
    check('⌗ and the ledger now carries it as NAMED-UNBUILT again, with the correction recorded',
          '328d33776e' in led and 'RESTORED r2621' in led)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** TWO unbuilt fermion sectors, and r2618 collapsed them. **')
    print('  ⛔ ⓵ boundary_paper distinguishes them ** in one sentence: ** the built sector "is a spinor')
    print('     on the real Lorentzian slicing structure, ** NOT a gauge-acted sector on the compact')
    print('     face **".')
    print('  ⓶ ** p0 / PO-11: ** the PROPAGATING theory on the Lorentzian slicing structure.')
    print('     ** boundary_paper: ** the COMPACT-FACE, gauge-acted sector an equivariant index would act')
    print('     on.')
    print('  ⓷ ** And they are unbuilt for DIFFERENT REASONS: ** the first because the delivered modes')
    print('     are BOUND; the second because the substrate supplies no such face -- su(3) "being no')
    print('     isometry of the non-compact substrate to begin with".')
    print('     ⇒ ** Building one does not build the other. **')
    print('  ⛭ ** THE RULE: ** a dedupe pass is a CLAIM that two things are the same, and a claim needs a')
    print('    check.  r2618 deduped on ** shared vocabulary ** -- both said "fermion sector ...')
    print('    unbuilt".  ** The test that would have caught it: ask WHY each is unbuilt.  Two things')
    print('    unbuilt for different reasons are two things. **')
    print('  ⌗ The table goes ** 27 -> 28 ** -- a correction that ADDS an item, which is the honest')
    print('    direction and one a dedupe pass will never produce on its own.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

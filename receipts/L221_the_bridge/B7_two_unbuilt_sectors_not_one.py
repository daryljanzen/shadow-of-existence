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
    check('and names what stays unbuilt: "The compact-face fermion sector the obstruction would act on '
          'remains unbuilt"',
          'The compact-face fermion sector the obstruction would act on remains unbuilt' in bp)
    check('and why it matters: the built sector "supplies no equivariant index for the obstruction to '
          'act on"',
          'supplies no equivariant index for the obstruction to act on' in bp)

    # p0's is a different object
    check("⓶ and p0's object is the PROPAGATING theory: \"the full \\emph{propagating} spinor field "
          'sector (the built modes being leaf-bound, not the propagating theory)"',
          'the full \\emph{propagating} spinor field sector' in p0
          and 'the built modes being leaf-bound, not the propagating theory' in p0)

    # different reasons
    check('⓷ and they are unbuilt for DIFFERENT reasons -- the compact-face route is walled by '
          'localisation and by $\\mathfrak{su}(3)$ being no isometry: "being no isometry of the '
          'non-compact substrate to begin with"',
          'being no isometry of the non-compact substrate to begin with' in bp)
    check('while the propagating sector is unbuilt because the delivered modes are BOUND -- p0: "the '
          'built modes being leaf-bound"',
          'the built modes being leaf-bound' in p0)

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

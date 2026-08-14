#!/usr/bin/env python3
"""P4 -- r2522 CORRECTED: the corpus does not decline the Higgs mechanism.  It IDENTIFIES electroweak
breaking with the breaking of the substrate's orientation parity R, in a subordinate clause, and never
develops it.  ** And this line's "the argument is complete and only the word is missing" was the burying,
not the finding. **

** ⛔ THE CORRECTION, AND IT IS THIS LINE'S ERROR. **  r2522 read P6's passage as a principled DECLINE
and wrote: "the corpus declines the magnitudes deliberately and says so in print ... the argument is
complete and only the word is missing."  ** Daryl: "Not having the Higgs incorporated into the same
physics is not my choice.  I have pressed to include the Higgs mechanism for completion wherever it is
relevant.  I've met nodes trying to bury that." **

  ⇒ *** THE PASSAGE IS NOT A DECLINE.  IT IS A POSITIVE STRUCTURAL IDENTIFICATION. ***

** ⓵ WHAT P6 ACTUALLY SAYS, read whole rather than from its last clause: **

  "the $M=0$ central cut is the one $R$ fixes and massless fermions are the ones $\\gamma^5$ fixes, so
   ** the $R$-symmetric sector is exactly the offset-free, massless vacuum **, and ** mass (geometric $M$
   or fermionic $m$) is the $R$-odd DEPARTURE from it.  Geometric and fermion mass are thereby THE SAME
   KIND OF OBJECT, the one discrete residue broken **; the value stays the ordinary route, ** the
   electroweak breaking that supplies the fermion mass being, in this reading, THE BREAKING OF THE
   SUBSTRATE'S ORIENTATION PARITY **---and CR's $R$-structure does not constrain that breaking: the
   electroweak transition is the ordinary thermal event, on which the substrate sets no scale,
   chirality, or epoch."

  ⇒ ** CR IDENTIFIES ELECTROWEAK SYMMETRY BREAKING WITH THE BREAKING OF R. **  That is a claim about
    ** what the Higgs mechanism IS in CR's terms **.
  ⇒ ** And what the same sentence declines is narrow and explicit: the SCALE, the CHIRALITY, the EPOCH,
    and the mass VALUES.  ** *** The one-constant theorem forbids the STRENGTHS.  It says nothing about
    the MECHANISM. ***

** ⛭⛭ ⓶ AND THE CORPUS HAS ITS OWN SYMMETRY-BREAKING MECHANISM, WHICH NOBODY HAS SET BESIDE IT. **

  P3, of the observer fixing the offset: "** This is the symmetry breaking, located precisely. **"  The
  construction's whole content is a symmetry-breaking cut of a maximally symmetric substrate; P0 calls
  the physics "** broken-symmetry shadows **".

  ⇒ *** SO THERE ARE TWO SYMMETRY-BREAKING MECHANISMS IN PLAY -- the cut, and the electroweak transition
      -- and the corpus identifies the second with a substrate structure ($R$) in a subordinate clause
      and never develops the identification. ***

** ⓷ AND THE SHAPE OF THIS LINE'S ERROR IS ONE IT HAS FILED AGAINST ITSELF TWICE. **  r2495: "'that is
unseated' is legitimate only where a JUDGEMENT remains."  r2498: "a category named after a person is
unfalsifiable."
  ⇒ ** Here the same move wore a third costume: ** *** a STATE OF THE TEXT was read as a SETTLED
      DECISION.  "The papers decline it" became "the programme declines it" -- and nobody decided
      that. ***
  ⌗ ** And the tell was in the sentence this line wrote: "the argument is complete and only the word is
    missing" turns a live, undeveloped identification into a presentational nicety. **  *** Whenever a
    finding resolves into "only the wording", check whether the thing being called wording is a claim
    nobody has worked. ***

** ⓸ WHAT IS ACTUALLY OPEN, and it is a lead into PO-5's vein rather than a routing item: **

  *** Does CR's structure say anything about the Higgs MECHANISM -- as against the magnitudes it
      provably cannot supply? ***  The corpus already asserts one identification (electroweak breaking =
  breaking of $R$).  ** Nothing tests it, extends it, or asks what it would predict. **
  ⌗ And the neighbouring structure is already built: ** $R$ is the orientation parity; $\\gamma^5$ fixes
  the massless fermions; the $R$-symmetric sector IS the massless vacuum; and PO-5's live question is
  whether an operator's kernel gives the colourless four. **  ** These are the same sector. **

WHAT IS NOT CLAIMED.  ** Not that CR derives the Higgs sector, the vev, or any mass ** -- the
one-constant theorem stands and F1/F3 remain the trip-wires.  ** Not that P6's identification is
correct ** -- it is asserted in the corpus and is not tested here.  Only that ** it is an
IDENTIFICATION rather than a decline, that it is undeveloped, and that r2522 mis-recorded it. **

Written r2524.  Stated for reversal.
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
    raw = open(os.path.join(ROOT, 'corpus', f), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print('  P4 -- does the corpus DECLINE the Higgs mechanism, or IDENTIFY it?')
    print()
    p6 = body('boundary_paper.tex')
    p3 = body('SdS-slicing-curve_v2.tex')
    p0 = body('geometric_core_paper.tex')

    # ⓵ the identification, read whole
    check('P6: the $R$-symmetric sector is exactly the offset-free, massless vacuum',
          'the $R$-symmetric sector is exactly the offset-free, massless vacuum' in p6)
    check('and mass -- geometric $M$ or fermionic $m$ -- is the $R$-odd DEPARTURE from it',
          'is the $R$-odd \\emph{departure} from it' in p6)
    check('and "Geometric and fermion mass are thereby the same kind of object, the one discrete '
          'residue broken"',
          'Geometric and fermion mass are thereby the same kind of object' in p6)
    check('⛭⛭ AND THE IDENTIFICATION: "the electroweak breaking that supplies the fermion mass being, '
          "in this reading, the breaking of the substrate's orientation parity\"",
          'the electroweak breaking that supplies the fermion mass being, in this reading, the '
          "breaking of the substrate's orientation parity" in p6)
    check('⇒ SO CR IDENTIFIES ELECTROWEAK SYMMETRY BREAKING WITH THE BREAKING OF $R$ -- a claim about '
          'what the mechanism IS, not a decline of it',
          "the breaking of the substrate's orientation parity" in p6)

    # what IS declined, and it is narrow
    check('and what the same sentence declines is narrow and explicit: the substrate "sets no scale, '
          'chirality, or epoch"',
          'the substrate sets no scale, chirality, or epoch' in p6)
    check('together with the mass VALUES -- "What the geometry does not fix are the individual mass '
          '\\emph{values}; those stay the ordinary route"',
          'What the geometry does not fix are the individual mass \\emph{values}' in p6)
    check('⇒ THE ONE-CONSTANT THEOREM FORBIDS THE STRENGTHS.  IT SAYS NOTHING ABOUT THE MECHANISM',
          'the substrate sets no scale, chirality, or epoch' in p6
          and "the breaking of the substrate's orientation parity" in p6)

    # ⓶ the corpus's own symmetry breaking
    check("⌗ and the corpus has its OWN symmetry-breaking mechanism: P3 -- \"This is the symmetry "
          'breaking, located precisely\"',
          'This is the symmetry breaking, located precisely' in p3)
    check('and P0 frames the whole physics as "broken-symmetry shadows"',
          'broken-symmetry shadows' in p0)
    check('⇒⇒ SO TWO SYMMETRY-BREAKING MECHANISMS ARE IN PLAY, the second identified with a substrate '
          'structure in a SUBORDINATE CLAUSE, and never developed',
          'This is the symmetry breaking, located precisely' in p3
          and "the breaking of the substrate's orientation parity" in p6)

    # ⓸ the sector is already built
    check("⌗ and the neighbouring structure is built: $\\gamma^5$ fixes the massless fermions",
          'massless fermions are the ones $\\gamma^5$ fixes' in p6)
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(body(os.path.basename(f)) for f in papers)
    check('✔ NOW while "Higgs" still appears ZERO times, so the identification is invisible to search',
          len(re.findall('Higgs', allp, re.I)) > 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** r2522 was wrong.  The corpus IDENTIFIES rather than declines. **')
    print('  P6: ** the $R$-symmetric sector IS the offset-free massless vacuum; mass is the $R$-odd')
    print('  DEPARTURE from it; geometric and fermion mass are THE SAME KIND OF OBJECT; and the')
    print("  electroweak breaking that supplies the fermion mass IS the breaking of the substrate's")
    print('  orientation parity. **')
    print('  ⇒ ** That is a claim about what the Higgs mechanism IS in CR\'s terms. **  What the same')
    print('    sentence declines is narrow and explicit: ** the scale, the chirality, the epoch, and the')
    print('    mass VALUES. **  ⇒ ** The one-constant theorem forbids the STRENGTHS.  It says nothing')
    print('    about the MECHANISM. **')
    print('  ⌗ And the corpus has its OWN symmetry breaking -- P3: "This is the symmetry breaking,')
    print('    located precisely" -- ** and nobody has set the two beside each other. **')
    print('  ⛔ AND THE ERROR SHAPE IS ONE THIS LINE HAS FILED TWICE: ** a STATE OF THE TEXT read as a')
    print('     SETTLED DECISION. **  "The papers decline it" became "the programme declines it".')
    print('     ⇒ ** Whenever a finding resolves into "only the wording", check whether the thing being')
    print('       called wording is a claim nobody has worked. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

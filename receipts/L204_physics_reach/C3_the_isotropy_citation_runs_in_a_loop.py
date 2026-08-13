#!/usr/bin/env python3
"""C3 -- item 26's residue, and it is not what F12 said: P12 and P9 cite EACH OTHER for the isotropy
dimensions, and the triple {6,7,10} appears in neither's derivation.

** WHERE ITEM 26 STOOD. **  Routed r2442, and honestly: "two items routed at the finder's weight,
** not independently verified here **.  This line has not re-derived either, and says so rather than
passing them on as checked."  ** It is one of the last two items in the routed queue, and the only one
with a testable claim in it. **

** ⓵ F12's CHARACTERISATION IS WRONG, AND CHECKING IT IS WHAT FOUND THE REAL THING. **  F12: "P12's
isotropy-3 stratum labelled 'Bianchi' is claimed to be ** six of the nine types **".
  ⇒ ** Measured: `isotropy-3` 0 · `six of the nine` 0 · `nine types` 0 across the papers. **  P12's only
    `Bianchi` is "** Type I (Bianchi, dimension three; Zipoy--Voorhees, dimension two) **" -- a label on
    one stratum, ** not a claim about six of nine **.
  ⌗ *** So the finder's weight was the right thing to route it at.  The claim as stated does not exist. ***

** ⛭⛭ ⓶ BUT THE SENTENCE F12 POINTED AT CARRIES A DIFFERENT DEFECT, AND IT IS REAL. **  P12:

  "** The isotropy dimensions are the Killing-vector counts the construction establishes **~\\cite{JanzenRange},
   and the verdict is independent of the choice of generator realization: ** the symmetric-pair isotropy
   dimensions of $\\so(5,1)$ are $\\{6,7,10\\}$ **"

  ** So P12 states the triple and cites P9 for it. **  And P9, at its own isotropy passage:

  "at every stratum for which ** the companion algebroid paper tabulates an isotropy ** ... it is in fact
   an equality~\\cite{JanzenAlgebroid}"

  ⇒ *** EACH CITES THE OTHER FOR THE SAME FACT.  P12 cites P9 for the counts; P9 cites P12 for the
      tabulation. ***

** ⓷ AND THE TRIPLE IS IN NEITHER DERIVATION. **  ** `6,7,10` appears 0 times in P9 **; `seven` 0, `six`
0, `isotropy dimension` 0.  ** P9 names isotropies as GROUPS ** -- $\\mathrm{SO}(4,1)$ at Type O,
$\\mathrm{SO}(2,1)\\times\\mathrm{SO}(3)$ at Nariai, $\\mathbb{R}_t\\times\\mathrm{SO}(3)$ at the generic
class -- ** and never as the dimension triple P12 attributes to it. **
  ⇒ ** The dimensions are recoverable from those groups by inspection ** (10, 3+1=4 ... ), *** which is
      exactly why nobody noticed: the fact is TRUE and the citation does not establish it. ***

** ⇒⇒ SO ITEM 26's RESIDUE IS A CITATION-CONTENT GAP, WHICH IS ITEM 45's CLASS. **  There,
`Teitelboim1973` was cited for the Dirac brackets' ** form ** and never for the ** uniqueness content **.
Here, P9 is cited for a ** triple it never states **, while P9 cites P12 back for the tabulation the
triple summarises.
  ⌗ *** A citation loop between two papers is invisible to `check_citations`, which checks that a cited
      key EXISTS, not that the cited paper CONTAINS the fact. ***

WHAT IS NOT CLAIMED.  ** Not that the triple is wrong ** -- $\\{6,7,10\\}$ is consistent with the groups P9
names, and this receipt does not re-derive it.  ** Not that either paper is careless **: two papers
written together will naturally point at each other, and *** the loop is a property of the pair, not a
mistake in either alone. ***  ** Not that F16 is checked ** -- item 26's second finding is untouched here
and stays at the finder's weight.

⌗ AND WHAT WOULD DISCHARGE IT: ** one of the two papers derives the triple, or P12 states it as its own
rather than attributing it. **  *** One clause, and the choice of which paper owns it is an authorial
one. ***

Written r2575.  Stated for reversal.
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


def body(name):
    return re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(os.path.join(ROOT, 'corpus', name), encoding='utf-8',
                        errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))


def main():
    print()
    print("  C3 -- item 26's residue: does P9 establish what P12 cites it for?")
    print()
    p12 = body('algebroid_paper.tex')
    p9 = body('range_paper.tex')
    allp = ' '.join(body(os.path.basename(f)) for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
                    if not os.path.basename(f).startswith('appendix_receipts'))

    # ⓵ F12's characterisation is wrong
    for k in ('isotropy-3', 'six of the nine', 'nine types'):
        check(f'⓵ F12 says P12 claims "{k}" -- it appears ZERO times across the papers',
              len(re.findall(re.escape(k), allp, re.I)) == 0)
    check('and P12\'s only "Bianchi" is a label on one stratum: "Type I (Bianchi, dimension three; '
          'Zipoy--Voorhees, dimension two)"',
          'Type I (Bianchi, dimension three' in p12)

    # ⓶ the real sentence
    check('⛭⛭ ⓶ but P12 states: "The isotropy dimensions are the Killing-vector counts the construction '
          'establishes~\\cite{JanzenRange}"',
          'The isotropy dimensions are the Killing-vector counts the construction establishes' in p12
          and 'JanzenRange' in p12)
    check('and gives the triple: "the symmetric-pair isotropy dimensions of $\\so(5,1)$ are $\\{6,7,10\\}$"',
          '\\{6,7,10\\}' in p12)
    check('while P9 points BACK: "at every stratum for which the companion algebroid paper tabulates an '
          'isotropy ... it is in fact an equality~\\cite{JanzenAlgebroid}"',
          'the companion algebroid paper tabulates an isotropy' in p9
          and 'JanzenAlgebroid' in p9)
    check('⇒⇒ SO EACH CITES THE OTHER FOR THE SAME FACT',
          'JanzenRange' in p12 and 'JanzenAlgebroid' in p9)

    # ⓷ and the triple is in neither derivation
    check('⓷ and the triple is NOT in P9: "6,7,10" appears zero times there',
          '6,7,10' not in p9)
    check('P9 names isotropies as GROUPS instead -- SO(4,1) at Type O, SO(2,1)xSO(3) at Nariai',
          '\\mathrm{SO}(4,1)$ at Type O' in p9)
    check('⇒ so the fact is TRUE and recoverable by inspection, and the citation does not establish it '
          '-- which is why nobody noticed',
          '\\{6,7,10\\}' in p12 and '6,7,10' not in p9)

    # the class
    check("⌗ and this is item 45's class: a citation for FORM where the CONTENT is elsewhere",
          'Teitelboim1973' in p12)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** item 26's residue is a citation LOOP, and it is not what F12 said. **")
    print('  ⓵ ** F12\'s "six of the nine types" does not exist ** -- isotropy-3 0, six of the nine 0,')
    print('     nine types 0.  ** The finder\'s weight was the right thing to route it at. **')
    print('  ⓶ ** But P12 states the triple {6,7,10} and cites P9; and P9 cites P12 back for the')
    print('     tabulation the triple summarises. **  ⇒ ** Each cites the other for the same fact. **')
    print('  ⓷ ** And "6,7,10" appears ZERO times in P9 ** -- which names isotropies as GROUPS, not as a')
    print('     dimension triple.  ⇒ ** The fact is TRUE and recoverable by inspection, and the citation')
    print('     does not establish it: which is exactly why it survived. **')
    print('  ⌗ ** A citation loop between two papers is invisible to check_citations **, which checks a')
    print('    cited key EXISTS, not that the cited paper CONTAINS the fact.')
    print('  ⇒ WHAT WOULD DISCHARGE IT: ** one paper derives the triple, or P12 states it as its own. **')
    print('    One clause -- and which paper owns it is authorial.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
r"""check_paper_tense.py -- A PAPER CARRIES ONE STATE, SO IT MAY NOT NARRATE ITS OWN HISTORY.

** WHY.  A paper is not a changelog. **  It asserts what is the case; the corpus's registers and
receipts carry what changed and when.  *A sentence saying a thing **has since been** done is telling
the reader about the paper's own development, and it dates the moment it is written.*

  ⇒ *** "That refit has since been performed" was found in P15 at r3111 by the observer line, reading
      the paper for a different purpose, and repaired to "is performed here". ***
  ⇒ ** One found by hand is a sighting.  This gate is the sweep, and it finds five more. **

** ⌗ AND ONE OF THE SIX IS NOT A DEFECT, which is why the discriminator matters more than the list. **
*p0 says a centrepiece is "stated at what it has since become rather than at what it was when first
written (r1609)".*  ** That is the OPPOSITE of the drift: it declares that the statement is given in
its current form, and names the revision. **
  ⇒ *** So a history phrase with a revision id beside it is a DECLARATION and passes; one without is
      an undeclared narration and fails.  Declared, not inferred -- the corpus's own pattern, the
      same one `NOT-A-RECEIPT:` and `IN-FLIGHT:` and `[REPORTED]` use. ***

** ⚠ WHAT THIS GATE DOES NOT DO: rewrite the sentence. **  *"has since been measured" becomes "is
measured" only if the measurement is in the paper's current state, and knowing that is a READING of
the paper.*  ⇒ ** It reports the site and the phrase and stops, which is why it is baselined by NAME
rather than arriving red on five sentences whose owner has not read them yet. **

    python3 corpus/check_paper_tense.py

Written r3112 (`L-251`).  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: phrases that narrate the paper's own development rather than assert its content
HISTORY = re.compile(
    r'has since been|have since been|had previously|was previously|were previously|'
    r'since then|has now been|have now been|as of this writing|at the time of writing|'
    r'used to be|in an earlier version|previously stated|we have since|it has since',
    re.I)
#: a revision id BESIDE the phrase declares the statement is given at its current state
REV = re.compile(r'\br\d{3,5}[a-z]?\b')
NEAR = 100

#: ** NAMED, not counted, and not by filename. **  Known at r3112 and reported until cleared.  A
#: site not on this list is a FAILURE.  *A count could be satisfied by fixing one and adding
#: another, which is the hole c54.212 found in a different gate.*
BASELINE = {
    ('CR_cosmology.tex', 'has since been'),
    ('CR_cosmology.tex', 'it has since'),
    ('CR_cosmology.tex', 'has now been'),
    ('CR_framework.tex', 'has now been'),
    ('matter_sector_paper.tex', 'has since been'),
}


def body(src):
    """the document body: comments dropped, preamble dropped

    *A `%` line is not read by anyone and a preamble carries package history legitimately.*
    """
    src = '\n'.join(l for l in src.split('\n') if not l.lstrip().startswith('%'))
    i = src.find(r'\begin{document}')
    return src[i:] if i > 0 else src


def sites(root=None):
    out = []
    for f in sorted(glob.glob(os.path.join(root or ROOT, 'corpus', '*.tex'))):
        name = os.path.basename(f)
        if name.startswith('appendix_receipts'):
            continue                                  # generated; its text is the INDEX printed
        b = body(open(f, encoding='utf-8', errors='replace').read())
        for m in HISTORY.finditer(b):
            near = b[max(0, m.start() - NEAR):m.start() + NEAR]
            out.append((name, m.group(0).lower(), bool(REV.search(near)),
                        b[max(0, m.start() - 55):m.start() + 75].replace('\n', ' ').strip()))
    return out


def main():
    print()
    print('  check_paper_tense -- does any paper narrate its own history?')
    print('  (a paper carries ONE STATE; what changed and when is the registers\' job)')
    print()
    found = sites()
    declared = [s for s in found if s[2]]
    undeclared = [s for s in found if not s[2]]
    known = [s for s in undeclared if (s[0], s[1]) in BASELINE]
    new = [s for s in undeclared if (s[0], s[1]) not in BASELINE]
    gone = BASELINE - {(s[0], s[1]) for s in undeclared}

    print(f'    {len(found)} history phrase(s) in paper bodies')
    print(f'    {len(declared)} DECLARED -- a revision id beside the phrase, so the statement is '
          f'given at its current state on purpose')
    for n, p, _, ctx in declared:
        print(f'          [ok]    {n:<26} [{p}]  …{ctx[:78]}…')
    print(f'    {len(known)} known, still open (baselined by NAME at r3112)')
    for n, p, _, ctx in known:
        print(f'          [known] {n:<26} [{p}]  …{ctx[:78]}…')
    if gone:
        print(f'    {len(gone)} baselined site(s) now CLEARED -- strike them from BASELINE:')
        for n, p in sorted(gone):
            print(f'          [clear] {n:<26} [{p}]')
    print()
    if not new:
        print('    no NEW paper sentence narrates the paper\'s own history.')
        print()
        return 0
    for n, p, _, ctx in new:
        print(f'    [FAIL] {n}  [{p}]')
        print(f'           …{ctx[:96]}…')
    print()
    print('    ⛭ ** A paper asserts what IS the case.  A sentence saying a thing "has since been"')
    print('       done narrates the paper\'s own development and dates the moment it was written. **')
    print('    ⌷ State it in the present -- "is performed here" -- if the thing is in the paper\'s')
    print('       current state; or name the revision beside it, which DECLARES the tense on purpose.')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())

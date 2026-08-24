#!/usr/bin/env python3
"""check_one_state.py -- A PAPER MAY NOT NARRATE ITS OWN CONSTRUCTION.

** WHY THIS GATE EXISTS, AND WHY IT IS MECHANICAL. **

*** A paper presents ONE state.  One set of results, one model, one fit.  Not fifty attempts and
then the right one.  The corpus has said this for hundreds of revisions and it kept recurring --
r3157, r3159, r3161, r3175, r3183, r3185, r3189, r3195 all cut the same class out of ONE paper. ***

  ⛔ ** AND THE REASON IT RECURRED IS NOT CARELESSNESS.  A node reading "the rule's own defect is
     recorded rather than quietly repaired" scores it as RIGOUR -- because in a RECEIPT it is.  A
     receipt is a process artifact and SHOULD carry how a result was got; a paper is not and MUST
     NOT.  A node that judges case by case will approve it again, having re-derived the wrong
     conclusion from a principle it correctly holds. **

  ⇒ *** SO THE TEST IS MECHANICAL AND TAKES NO JUDGEMENT: in a PAPER, the paper, its instrument, its
      rule or its programme may not be the subject of a verb about its own making.  Not "was
      rebuilt", not "had to be removed", not "prompted the check", not "we now met that twice".
      What the instrument IS, what it measures, what a rule FORBIDS -- all fine.  How it came to be
      that way -- never. ***

** WHAT IS NOT FLAGGED. **  Receipts, ledgers, plans, THE_REGISTER, commit messages: process
artifacts, where this record is required.  This gate reads corpus/*.tex only, and only between
\\begin{document} and the bibliography.

    python3 corpus/check_one_state.py

Written r3197.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: ** NAMED BY CLASS, not by spelling. **  Each entry is a way a paper can narrate its own making.
PATTERNS = [
    ('a prior state of the paper',
     r'\b(?:was|were|had been)\s+(?:withdrawn|revised|corrected|wrong|too (?:wide|strong|weak))\b'
     r'|\bis (?:withdrawn|here revised|accordingly withdrawn|withdrawn (?:here|to the))\b'
     r'|\ban earlier (?:reading|pass|version|form|formulation|statement)\b'
     r'|\bas earlier stated\b|\bas (?:previously|formerly) stated\b'
     r'|\bthis (?:paper|section) (?:stated|claimed|read|carried|previously)\b'
     r'|\bbefore the \w+ was run\b|\bthe older \w+[- ]analytic\b'
     r'|\bthat (?:reading|statement|figure) (?:is|was) (?:withdrawn|wrong)\b'
     r'|\bwe withdraw\b|\bwithdraw it in those terms\b|\bare withdrawn\b'
     r'|\ban earlier statement\b|\bneither is reproduced\b'
     r'|\bwe record the \w+ against ourselves\b'
     r'|\bthe paragraph (?:after next|below) corrects\b'
     r'|\bwhat they were taken to mean\b|\bunder another name\b'),
    ('a repair or its occasion',
     r'\bhad to be (?:removed|corrected|added|restored)\b'
     r'|\bprompted the check\b|\bfor it to work\b'
     r'|\bmade the (?:control|arm|fit) worse\b'
     r'|\bobjection is now gone\b|\bthe mistake .{0,30}exists to avoid\b'),
    ('a count of attempts',
     r'\brebuilt (?:twice|three times|four times|\w+ times)\b'
     r'|\bin consecutive revisions\b|\bhas now met that\b'
     r'|\b(?:second|third) lesson\b|\barrived in the same shape\b'
     r'|\bfor two revisions\b|\bonly now measured\b|\basserted here for\b'),
    ('a revision stamp in the prose',
     r'(?<![A-Za-z])r\d{3,4}(?![\d])|c54\.\d+'),
]


def body(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    t = re.sub(r'(?m)^%.*$', '', t)                 # whole-line comments
    t = re.sub(r'(?<!\\)%.*$', '', t, flags=re.M)   # trailing comments
    i = t.find('\\begin{document}')
    j = t.find('\\begin{thebibliography}')
    if i < 0:
        return ''
    return t[i:j if j > i else len(t)]


def main():
    print()
    print('  check_one_state -- a paper may not narrate its own construction')
    print()
    bad = 0
    for path in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        name = os.path.basename(path)
        if 'appendix' in name:
            continue
        b = body(path)
        if not b:
            continue
        for label, pat in PATTERNS:
            for m in re.finditer(pat, b, re.I):
                ctx = re.sub(r'\s+', ' ', b[max(0, m.start() - 60):m.end() + 60])
                print(f'    [FAIL] {name}: {label}')
                print(f'           ...{ctx.strip()[:130]}...')
                bad += 1
    print()
    if bad:
        print(f'    {bad} site(s).  ** A PAPER PRESENTS ONE STATE. **  State what the thing IS, what it')
        print('    measures, what a rule forbids.  Not how it came to be that way -- that belongs in')
        print('    the receipt, which is where a reader who wants the history should find it.')
        print()
        return 1
    print('    No paper narrates its own construction.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

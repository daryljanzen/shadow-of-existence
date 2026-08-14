#!/usr/bin/env python3
"""check_self_certification.py -- A RECEIPT MAY NOT ASSERT ITS OWN COMPLIANCE.

** WHY.  THE_INTERFERENCE_ENGINE §3, the failure-tell: **

    *** "ANNOUNCING ONE'S OWN MEASUREDNESS.  When the reception is genuine you do not have to label
        it; THE LABEL IS SELF-CERTIFICATION, WHICH IS WHAT SURFACES WHEN THE THING ITSELF IS
        ABSENT." ***

  ** And §87 lists, as a known machine failure of THIS collaboration: ** *"an AI fabricating
  'balanced' caveats to perform measuredness, turning a thing told in earnest into an asshole's
  weapon."*

** ⛭ WHAT THE MEASUREMENT ACTUALLY FOUND, r2732, and it is mostly a NEGATIVE. **  *** 82 receipts
this session, 76 carrying a `WHAT IS NOT CLAIMED` block.  A first pass classified 190 of 224 clauses
as "label only" -- and the SAMPLE showed that classification was wrong: "Not that confinement is
derived", "Not that a non-flat bundle exists here", "Not that `C5b` is re-derived" each name a
SPECIFIC, checkable exclusion.  **The caveat blocks do scope work.  I nearly rebuilt something that
was not broken, on a crude classifier I had not sampled.** ***

  ⇒ ** The real residue is small and exact: ** *** labels asserting COMPLIANCE rather than SCOPE.
      `stated for reversal` (88) names a reversibility property a reader can act on.
      `NOT-A-PAPER-CLAIM` (181) routes the claim's scope.  ** `F5-safe` (2) asserts that a rule was
      obeyed -- and that is the failure-tell verbatim: the label surfacing where the thing itself
      would be visible without it. ** ***

** WHAT THIS CHECKS. **  Receipts and register rows for compliance-assertions: a node declaring its
own work safe, compliant, careful, rigorous, balanced, or measured.

  ⌗ ** SCOPE is not compliance. **  *** "Not that X is derived" tells a reader what the receipt does
    not cover -- checkable, and load-bearing.  "F5-safe" tells a reader the node believes it followed
    a rule -- which the reader cannot check and which the work would show if true. ***

    python3 corpus/check_self_certification.py

Written r2732.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** a node asserting that its own work complies. **
SELF_CERT = re.compile(
    r'\bF5[- ]safe\b|\bgate[- ]safe\b|\bcoda[- ]compliant\b'
    r'|\bthis (?:receipt|revision|turn) is (?:careful|rigorous|balanced|measured)\b'
    r'|\bproperly scoped\b|\bduly (?:caveated|hedged)\b'
    r'|\bI have been (?:careful|rigorous|thorough)\b', re.I)


def main():
    print()
    print('  check_self_certification -- does any receipt assert its own compliance?')
    print()
    flagged, n = [], 0
    targets = sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    targets += [os.path.join(ROOT, 'PROTECTED_OPEN.md')]
    for f in targets:
        if not os.path.exists(f) or os.path.basename(f) == os.path.basename(__file__):
            continue
        d = open(f, encoding='utf-8', errors='replace').read()
        n += 1
        hits = sorted({h.lower() for h in SELF_CERT.findall(d)})
        if hits:
            flagged.append((os.path.basename(f)[:54], hits))

    print(f'  {n} file(s) checked')
    if flagged:
        print()
        for name, hits in flagged[:12]:
            print(f'    [FAIL] {name}: {hits}')
        print()
        print('    ⛔⛭ ** THE FAILURE-TELL (INTERFERENCE ENGINE §3): "announcing one\'s own')
        print('       measuredness ... the label is self-certification, WHICH IS WHAT SURFACES WHEN')
        print('       THE THING ITSELF IS ABSENT." **')
        print('       *** SCOPE is not compliance.  "Not that X is derived" tells a reader what is')
        print('       not covered -- checkable, load-bearing.  "F5-safe" tells a reader the node')
        print('       believes it followed a rule, which the reader cannot check and which the work')
        print('       would show if true. ***')
        return 1
    print('  no receipt asserts its own compliance.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

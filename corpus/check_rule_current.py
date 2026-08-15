#!/usr/bin/env python3
"""check_rule_current.py -- A RULE CHANGE MUST REACH EVERY DOCUMENT THAT STATES THE RULE.

** WHY.  r2834. **  *** r2830 replaced the register's closure rule -- "Closures on protected items are
Daryl's", "a node may not strike a protected row" -- with a physics one: ** a row is struck when its
OBJECT is answered and the answer is receipted. **  The change was made in `PROTECTED_OPEN`.  ** The old
rule survived, verbatim and unmarked, in 33 places across 14 documents ** -- including `README`,
`THE_HUB`, `THE_OPERATING_MANUAL` and `THE_WISDOM_LEDGER`. ***

  ⇒ *** This is the withdrawal-propagation failure applied to a RULE rather than a finding -- and it is
      worse, because ** a stale finding misleads about one result while a stale rule misgoverns every
      future one. **  A node reading `THE_HUB` would have inherited the person-gate whole. ***

** WHAT THIS CHECKS. **  *** Every statement of a superseded rule must sit within 240 characters of a
mark naming its replacement. ***

  ⌗ ** The rule text is KEPT, not deleted ** -- *** it is the record of what the programme used to
    require, and `THE_CODA`'s negatives-are-the-map applies to rules as much as to branches.  What is
    required is that it announce itself as past. ***

    python3 corpus/check_rule_current.py

Written r2834.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** superseded rule statements, and the revision that replaced each **
SUPERSEDED = [
    (re.compile(r'may not CLOSE|may NOT close|may not close|a node may not strike|'
                r'[Cc]losures on protected items are'), 'r2830'),
]
MARKED = re.compile(r'r283[0-9]|PRE-r2830|old rule|replaced|person-gate', re.I)


def main():
    print()
    print('  check_rule_current -- has every superseded rule statement been marked?')
    print()
    files = sorted(glob.glob(os.path.join(ROOT, '*.md'))
                   + glob.glob(os.path.join(ROOT, 'capstones', '*.md')))

    bad, found = [], 0
    for f in files:
        t = open(f, encoding='utf-8', errors='replace').read()
        for pat, by in SUPERSEDED:
            for m in pat.finditer(t):
                found += 1
                window = t[max(0, m.start()-160):m.end()+240]
                if not MARKED.search(window):
                    bad.append((os.path.relpath(f, ROOT), m.group(0)[:40], by))

    print(f'  {len(files)} document(s); {found} statement(s) of a superseded rule')
    if bad:
        print()
        for rel, txt, by in bad[:12]:
            print(f'    [FAIL] {rel}: "{txt}" is superseded by {by} and unmarked')
        print()
        print('    ⛭ ** A stale FINDING misleads about one result; a stale RULE misgoverns every')
        print('       future one. ***  Keep the text — it is the record of what was required —')
        print('       and mark it as past. ***')
        return 1

    print('  every superseded rule statement names its replacement.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

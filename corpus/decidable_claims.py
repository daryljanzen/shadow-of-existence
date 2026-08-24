#!/usr/bin/env python3
"""decidable_claims.py -- THE CORPUS'S STATED CLAIMS THAT A MATHEMATICIAN CAN SETTLE.

** ⛭⛭ WHY THIS, AND NOT ANOTHER FIELD SURVEY. **  *Three revisions of field-bake work say where the
value actually came from, and it was not the field counts:*

  * *`L-276` -- `P14`'s clause "no character count on a finite group can produce three" drops the
    premise its own sentence sets.  Found by reading ONE SENTENCE.*
  * *`L-278` -- `P13`'s "four real forms of $\\SO(6,\\mathbb{C})$" is five, and "the unique real form
    that admits $\\su(3)$" is false.  Found by following a field into the paper's ARGUMENT.*
  * *`L-280` -- `P13`'s "the unique maximally symmetric Lorentzian manifold of its dimension".  Found
    by this instrument.*

  ⇒ *** THE PRODUCTIVE OBJECT IS NOT AN UNCLAIMED FIELD.  It is a STATED CLAIM THAT IS DECIDABLE --
      an enumeration, a uniqueness, an impossibility, a bound -- because those are exactly the claims
      that can be wrong in a way a computation catches. ***
  ⌗ ** And the corpus makes a great many of them: 784 by this instrument's pattern. **

** ⌗ WHAT IT DOES. **  Splits the de-macroed bodies into sentences and keeps those that BOTH match a
claim pattern (`the four ...`, `exactly three`, `the unique`, `at most two`, `cannot sit`, `there are
only`, ...) AND carry mathematical furniture (an algebra name, `dim`, `rank`, `subalgebra`,
`representation`, `generator`, `invariant`, ...).

  ⚠ ** WHAT IT CANNOT DO, AND THIS IS THE WHOLE DISCIPLINE. **  *It cannot tell a TRUE claim from a
    false one, and it cannot tell a load-bearing claim from a passing remark.  It produces a reading
    list.*  ⇒ ** Every finding still costs a computation, and `L-280`'s three bounces are what that
    looks like: most claims it surfaces are correct, and saying so is the honest majority outcome. **
  ⚠ *A claim stated only in symbols, or spread across two sentences, is invisible to it.*

    python3 corpus/decidable_claims.py
    python3 corpus/decidable_claims.py --paper P13

Written r3178 (`L-280`).  Stated for reversal.
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
import reach_baseline as RB                                                # noqa: E402

#: the shapes a decidable claim takes.  STATED IN FULL so the pattern can be argued with.
CLAIM = re.compile(
    r'\b(the (?:two|three|four|five|six|seven|eight|nine|ten) [a-z][a-z\- ]{2,30}s?\b'
    r'|exactly (?:one|two|three|four|five|six|seven|eight|nine|ten)\b'
    r'|the unique\b|is unique\b|the only\b'
    r'|at most (?:one|two|three|four|five|six)\b'
    r'|no [a-z][a-z\- ]{2,30} can\b'
    r'|cannot (?:be|sit|produce|carry|reach|hold|embed)\b'
    r'|there are (?:no|exactly|only)\b'
    r'|precisely (?:one|two|three|four|five)\b)', re.I)

#: mathematical furniture -- without one of these the match is prose, not a claim about mathematics
MATH = re.compile(r'(su\(|so\(|sl\(|sp\(|mathfrak|dim\b|rank\b|subalgebra|algebra|group|root|'
                  r'representation|generator|eigen|invariant|involution|isometry|symmetr|'
                  r'manifold|form\b|class\b|order\b)', re.I)

MIN_LEN, MAX_LEN = 40, 700


def sentences(b):
    b = re.sub(r'\\(?:label|ref|eqref|cite|rcpt)\{[^{}]*\}', ' ', b)
    return re.split(r'(?<=[.!?])\s+', b)


def claims(paper=None):
    """[(paper, matched-phrase, sentence)] over the de-macroed bodies"""
    out, seen = [], set()
    for p, b in sorted(RB.BODIES_TEX.items()):
        if paper and p != paper:
            continue
        for s in sentences(b):
            if not (MIN_LEN < len(s) < MAX_LEN):
                continue
            m = CLAIM.search(s)
            if not m or not MATH.search(s):
                continue
            key = (p, s[:70])
            if key in seen:
                continue
            seen.add(key)
            out.append((p, m.group(1).strip(), s.strip()))
    return out


def main():
    paper = sys.argv[sys.argv.index('--paper') + 1] if '--paper' in sys.argv else None
    rows = claims(paper)
    print()
    print('  decidable_claims -- stated claims a computation could settle')
    print()
    print(f'    claims matched: {len(rows)}')
    if not rows:
        print('    ⛔ [FAIL] the pattern matched nothing — an empty reading list is not a clean tree.')
        print()
        return 1
    by = collections.Counter(p for p, _, _ in rows)
    print(f'    by paper: {dict(by.most_common())}')
    print()
    print('    ⌗ THIS IS A READING LIST.  It cannot tell a true claim from a false one, nor a')
    print('      load-bearing one from a passing remark.  Every finding still costs a computation.')
    print()
    if paper:
        for p, kind, s in rows:
            print(f'    [{p}] «{kind[:34]}»\n       {s[:420]}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""check_landing_rows_trace.py -- DOES EVERY LANDING-TABLE ROW TRACE TO A WORKED REGISTER?

** WHY.  Routed by 59 at r3567, and its own words are the case for it: ** *"at r3524 I invented a
register ... It survived eleven revisions and was caught only because landing it meant reading its
worked statement and finding none."*

** ⌗ THE PROPERTY THIS GUARDS, and it is one level past the gates that read a report as the thing
reported. **  A landing table DESCRIBES the ledger it sits in.  ⇒ *** Once a document describes the
corpus in the corpus's own voice, a row with nothing behind it reads exactly like a row with a proof
behind it -- and the danger is not only that a CHECKER confuses the two, but that a WRITER does. ***
*A fabricated row is not a lie; it is a summary that outran its source, which is what summarising
does when nothing checks it.*

WHAT IT DOES.  For each ledger carrying a landing table, every register id named in the table's
first column must appear somewhere in that ledger OUTSIDE the table.  A register worked in the body
resolves; a register that exists only in the row that describes it does not.

** ⚠ TWO FALSE-POSITIVE CLASSES, BOTH NAMED BY 59 FROM BUILDING THE AD-HOC VERSION. **
  (1) ** THE TURNSTILE'S SPACE. **  Bodies write `⊢ 56`, tables write `⊢56`.  59's first pass
      reported seven false positives on that alone.  *Both sides are normalised here.*
      ⛔ *And this is not a cosmetic caution: the ONE case that motivated this gate is an instance
      of it.  See the note at the foot of this file.*
  (2) ** THE WARNING SIGIL IS A SECOND LEGITIMATE FORM. **  Some registers are carried as `⚠ ⊢45`
      rather than as a proved turnstile.  *A register held under a warning is still a register; the
      gate asks whether the id is WORKED SOMEWHERE, not which sigil it carries.*
⌗ AND PAPER CODES ARE NOT REGISTERS.  `P07`, `p0`, `L-533` name a destination or an arc row, not a
  probe, and a landing table's first cell carries them freely.  They are excluded by shape.

Written r3568 (node 60), to 59's r3567 routing.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

HEAD = re.compile(r'^#+.*THE LANDING TABLE.*$', re.M)
TURNSTILE = re.compile(r'⊢\s*(\d+)')
CODE = re.compile(r'`([A-Z]{1,3}\d{1,3}[′\'`a-z]?)`')
PAPER = re.compile(r'^[Pp]\d{1,2}$')


def norm(t):
    """collapse `⊢ 56` and `⊢56` to one token -- 59's first false-positive class"""
    return TURNSTILE.sub(lambda m: '⊢' + m.group(1), t)


def table_span(t):
    m = HEAD.search(t)
    if not m:
        return None
    rest = t[m.end():]
    e = re.search(r'\n---\s*\n', rest)
    return m.end(), (m.end() + e.start() if e else len(t))


def main():
    print()
    print('  check_landing_rows_trace -- does every landing-table row trace to a worked register?')
    print()
    orphans, checked, tables = [], 0, 0
    for f in sorted(glob.glob(os.path.join(ROOT, '*_LEDGER.md'))):
        t = norm(open(f, encoding='utf-8', errors='replace').read())
        span = table_span(t)
        if not span:
            continue
        tables += 1
        a, b = span
        tbl, body = t[a:b], t[:a] + t[b:]
        ids = set()
        for row in re.findall(r'^\|.*$', tbl, re.M):
            cells = row.split('|')
            if len(cells) < 3:
                continue
            first = cells[1]
            ids |= {'⊢' + n for n in TURNSTILE.findall(first)}
            ids |= {c for c in CODE.findall(first) if not PAPER.match(c)}
        for i in sorted(ids):
            checked += 1
            if i not in body:
                orphans.append((os.path.basename(f), i))

    print(f'    {tables} landing table(s); {checked} register id(s) traced')
    if orphans:
        print()
        for fn, i in orphans:
            print(f'    [FAIL] {fn}: `{i}` is named in the landing table and WORKED NOWHERE in the ledger')
        print()
        print('    ⛔ ** A ROW WITH NOTHING BEHIND IT READS EXACTLY LIKE A ROW WITH A PROOF BEHIND IT. **')
        print('       *That is what a summary in the corpus\'s own voice costs when nothing checks it.*')
        print('       ⇒ Work the register, or strike the row and say the id was never a register.')
        print()
        return 1
    print('    every landing-table row traces to a register worked in its own ledger.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

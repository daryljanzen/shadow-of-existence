#!/usr/bin/env python3
"""check_frontier_current.py -- THE FRONTIER'S RUNWAY MUST NOT LAG ITS ROW.

** WHAT THIS CATCHES, AND IT HAD DRIFTED ON EVERY LIVE ROW AT ONCE. **  `THE_FRONTIER.md`
reads as a generated view of `THE_REGISTER.md`, and for which rows are LIVE it is one --
struck rows drop out correctly.  ** But the per-row content -- title, counts, and the
runway prose a node actually reads to decide what to work -- is a hardcoded table inside
`scripts/regen_frontier.py`. **  Nothing updated it when a register row moved.

At r6473 every one of the eight live rows was behind its row by between 1898 and 2578
revisions, and the same text was being served to the public site through
`BOOK_INTRO_cosmiCave/frontier.html`.  *** A document that looks generated and is not is
worse than one that looks hand-written: nobody thinks to check it. ***

** WHY A STAMP CHECK AND NOT GENERATION. **  The runway is an editorial DIGEST of a
register row that runs to tens of thousands of characters; it cannot be mechanically
derived, and pretending otherwise is what would produce a generated-looking lie again.
** What CAN be checked mechanically is its currency: ** the newest revision a runway
cites must be at least the newest its register row cites.  A row that moves without its
runway moving fails here.

⌗ The remedy for a failure is to WRITE the runway forward, not to bump a number -- and
the gate says so, because a stamp bumped without prose is the same defect wearing the
check's own clothes.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, '..', 'scripts', 'regen_frontier.py')
REG = os.path.join(HERE, '..', 'THE_REGISTER.md')


def newest_revision(text):
    n = [int(x) for x in re.findall(r'r(\d{3,5})', text)]
    return max(n) if n else None


def runway_blocks(gen):
    out = {}
    for m in re.finditer(r"'(PO-\d+)':\s*\(.*?\n(?=\s*'PO-|\s*\}\n)", gen, re.S):
        out[m.group(1)] = m.group(0)
    return out


def register_rows(reg):
    out = {}
    for pid in re.findall(r'\| \*\*(PO-\d+)\*\*', reg):
        i = reg.index(f'| **{pid}**')
        row = reg[i:]
        row = row[:row.index(' |\n')] if ' |\n' in row[:60000] else row[:60000]
        out[pid] = row
    return out


def main():
    if not (os.path.exists(GEN) and os.path.exists(REG)):
        print('  [FAIL] generator or register missing')
        return 1
    gen = open(GEN, encoding='utf-8', errors='replace').read()
    reg = open(REG, encoding='utf-8', errors='replace').read()
    blocks, rows = runway_blocks(gen), register_rows(reg)

    print()
    print('  FRONTIER CURRENCY -- each live row\'s runway against its register row')
    print()
    stale, missing = [], []
    for pid, row in rows.items():
        if pid not in blocks:
            missing.append(pid)
            continue
        v, r = newest_revision(blocks[pid]), newest_revision(row)
        if v is None or r is None:
            continue
        mark = 'current' if v >= r else f'STALE by {r - v}'
        print(f'    {pid:<8} runway r{v:<6} row r{r:<6}  {mark}')
        if v < r:
            stale.append((pid, r - v))
    print()
    if missing:
        print(f'  ⛔ {len(missing)} live row(s) with NO runway: {", ".join(missing)}')
    if stale:
        print(f'  ⛔ {len(stale)} STALE RUNWAY(S) -- the row moved and the view did not:')
        for pid, gap in stale:
            print(f'    [FAIL] {pid} lags its register row by {gap} revision(s)')
        print('     ⌗ WRITE THE RUNWAY FORWARD.  Do not bump the stamp: a stamp moved')
        print('       without the prose is this same defect wearing the gate\'s clothes.')
        print()
        return 1
    if missing:
        return 1
    print(f'  {len(rows)} live row(s); every runway is at or ahead of its row.')
    print('  ⌗ Currency is what is checkable here.  The runway is a DIGEST and cannot be')
    print('    generated -- which is why it drifted for ~2000 revisions unnoticed.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

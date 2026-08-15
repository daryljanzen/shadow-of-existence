#!/usr/bin/env python3
"""check_superseded_marked.py -- AN OVERTURNED BLOCK MUST SAY SO WHERE IT SITS.

** WHY.  r2831. **  *** The register is append-only: every finding is written as a new block on the end
of a row's status cell.  ** When a later block WITHDRAWS, CORRECTS, REVERSES or RETRACTS an earlier one,
the earlier one stays exactly as written and still reads as current. **  Measured: twenty-one such pairs
across the register and ** not one earlier block carried any mark **. ***

  ⇒ *** A reader -- including the next instance -- meets the withdrawn claim first, in the same voice as
      the live ones, and has no way to know it was overturned unless they read to the end of a cell that
      runs to fifty thousand characters. ***

** ⛭⛭ AND THE SAME APPEND HABIT PRODUCED EXACT DUPLICATES. **  *** 29,263 bytes of byte-identical blocks
sat in three rows -- `PO-5` carried ten, `PO-6` nine -- because a merge re-appended what was already
there and nothing compared blocks. ***

** WHAT THIS CHECKS. **
  * *** every earlier block named as WITHDRAWN/CORRECTED/REVERSED/RETRACTED by a later one must carry an
    `⟨OVERTURNED by ...⟩` mark at its head; ***
  * *** and no status cell may contain the same block twice. ***

  ⌗ ** It does not check that the mark is right ** -- *** only that the overturned block announces
    itself.  A wrong mark is a different failure; what this stops is a dead claim reading as live. ***

    python3 corpus/check_superseded_marked.py

Written r2831.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

ROW = re.compile(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*')
OVERTURN = re.compile(r'(WITHDRAW[SN]?|CORRECTS|REVERSES|RETRACT\w*)\s+(r\d{4}|c54\.\d+)', re.I)
SPLIT = r'(?=⛭⛭⛭|⛔⛭⛭|⛔⛔)'
MARK = '⟨OVERTURNED'


def main():
    print()
    print('  check_superseded_marked -- does every overturned block say so?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()

    unmarked, dupes, rows = [], [], 0
    for l in raw.split('\n'):
        m = ROW.match(l)
        if not m:
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', l)[1:-1]]
        if len(cells) < 5:
            continue
        rows += 1
        s = cells[4]

        # ⓵ every named victim's block carries the mark
        for mm in OVERTURN.finditer(s):
            victim = mm.group(2)
            # ** r2831b: a dead block may be REPLACED by its surviving content rather than
            # marked in place (r2831's compression).  *** Then the block head is gone and only
            # the ⟨OVERTURNED by {victim}...⟩ note remains -- which is the stronger outcome, not
            # a miss.  Treat a victim named inside an OVERTURNED note as handled. ***
            if re.search(r'⟨OVERTURNED by ' + re.escape(victim), s):
                continue
            # ** r2831c: the victim may be named ONLY inside the block that overturns it --
            # "AND r2810 WITHDRAWS r2804's LABEL" -- in which case there is no victim block in
            # this cell to mark, and flagging it is a false positive.  *** Require a block HEAD
            # for the victim; without one there is nothing here to mark. ***
            if re.search(r'⟨OVERTURNED by ' + re.escape(victim), s):
                continue
            j = s.find(f'AND {victim} ')
            if j < 0:
                continue
            # ** r2831a: a +/-60-character window is an arbitrary scope and rejected a mark
            # sitting a few characters further into the block.  *** The honest test is that the
            # BLOCK carries the mark -- so bound the search by the next block delimiter. ***
            # ** r2832: the j-90 LOOKBACK was the same arbitrary-window flaw as the forward
            # one -- a long mark's opener sits further back than 90 characters.  *** Bound the
            # lookback by the PREVIOUS block delimiter, so the search is the block, both ways. ***
            prev = [mo.end() for mo in re.finditer(SPLIT, s[:j])]
            start = prev[-1] if prev else 0
            nxt = re.search(SPLIT, s[j+1:])
            block = s[start:j + 1 + (nxt.start() if nxt else len(s))]
            if MARK not in block:
                unmarked.append((m.group(2), victim, mm.group(1).upper()))

        # ⓶ no block appears twice
        seen = set()
        for b in re.split(SPLIT, s):
            k = b.strip()
            if len(k) < 200:
                continue
            if k in seen:
                dupes.append((m.group(2), len(b), k[:56]))
            seen.add(k)

    print(f'  {rows} row(s) checked')
    if unmarked or dupes:
        print()
        for pid, victim, verb in unmarked[:12]:
            print(f'    [FAIL] {pid}: {victim} is {verb} by a later block and carries no mark')
        for pid, n, head in dupes[:8]:
            print(f'    [FAIL] {pid}: a {n}-byte block appears twice -- "{head}..."')
        print()
        print('    ⛭ ** An append-only register carries its dead claims in the same voice as its live')
        print('       ones. *** Mark the overturned block where it sits, and never append what is')
        print('       already there. ***')
        return 1

    print('  every overturned block is marked, and no block appears twice.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

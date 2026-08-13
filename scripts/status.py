#!/usr/bin/env python3
"""status.py -- THE NUMBERS, COMPUTED.

** WHY.  r2612, Daryl: ** "You're not reporting numbers properly at all and it looks like you're
accomplishing nothing by your own reporting ... you're using all these codes like C1-7, but those codes
don't appear in any of your enumeration at all and it looks like sideways progress the whole way along."

  ⇒ ⛔ *** Correct.  The state table reported gates, ledger and board -- none of which move when a
      PROTECTED_OPEN item is worked -- while the turn's actual content was narrated in codes (C1-C7,
      routes, candidates) that appear in no count. ***
  ⇒ ** So work on the thing that matters was invisible in the reporting of it. **

** WHAT THIS PRINTS: ** every quantity that MOVES when work is done, and nothing that does not.  Each PO
item with its ranking axes and a one-line state; the conditions list with its current length; the ledger;
the gates.  *** If a turn changes nothing here, the turn changed nothing. ***

    python3 scripts/status.py

Written r2612.  Stated for reversal.
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def po_rows():
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    # ** struck rows are `| ~~PO-N~~ |` and are excluded: a closed item is not open work. **
    return {re.search(r'PO-\d+', l).group(0): l
            for l in raw.split('\n') if re.match(r'\|\s*\*\*PO-\d+\*\*', l)}


def conditions():
    """The necessary-conditions list on the measure: how many are still CONDITIONS."""
    p = os.path.join(ROOT, 'receipts', 'L165_defining_the_sum',
                     'S1_seven_necessary_conditions_on_the_measure.py')
    if not os.path.exists(p):
        return None, []
    body = open(p, encoding='utf-8', errors='replace').read()
    named = sorted(set(re.findall(r'\*\* (C\d) ', body)))
    # removals recorded by later receipts in the same folder
    removed = {}
    for f in glob.glob(os.path.join(ROOT, 'receipts', 'L165_defining_the_sum', 'S*.py')):
        t = open(f, encoding='utf-8', errors='replace').read()
        if 'C1 AND C2 ARE ONE' in t.upper():
            removed['C2'] = 'merged into C1 (one sentence in P10)'
        if 'C6 IS NOT A CONDITION' in t.upper() or 'C6 IS A THEOREM' in t.upper():
            removed['C6'] = 'derived, not required (direct integral)'
    return named, removed


def ledger():
    p = os.path.join(ROOT, 'corpus', 'open_ledger.txt')
    if not os.path.exists(p):
        return 0, 0
    rows = [l for l in open(p, encoding='utf-8') if '|' in l and not l.startswith('#')]
    unv = sum(1 for r in rows if '| UNVERDICTED |' in r)
    return len(rows), unv


def main():
    print()
    print('  ' + '=' * 76)
    print('  THE NUMBERS')
    print('  ' + '=' * 76)
    print()

    rows = po_rows()
    kills = {os.path.basename(f)[:-3] for f in glob.glob(os.path.join(ROOT, 'kills', '*.md'))}
    print(f'  PROTECTED_OPEN: {len(rows)} items, {len(kills)} with kill receipts')
    print()
    print(f"    {'item':<7} {'kill':>4} {'row chars':>10}   what moved most recently")
    for tag in sorted(rows, key=lambda x: int(x[3:])):
        l = rows[tag]
        marks = re.findall(r'\br(2\d{3})\b', l)
        last = max(marks) if marks else '—'
        print(f'    {tag:<7} {("yes" if tag in kills else "-"):>4} {len(l):>10}   last dated move: r{last}')
    print()

    # ** ---- THE PROGRESS NUMBER, added r2613 ---- **
    # ** Daryl: "which numbers am I actually supposed to see moving?" **  ⇒ *** Most of these should
    # NOT move.  GATES and RECEIPTS grow with instrument-building and can grow forever without the
    # physics advancing.  The LEDGER is saturated at 111/0 and only moves when a paper changes.  The
    # PO COUNT goes UP when work finds something (PO-10, 11, 12 were added by finding them), so a
    # rising count is discovery wearing the costume of regress. ***
    #   ⇒ ** The number that measures the programme closing is DARK HALVES ANSWERED: each vein has a
    #     MAPPED half and a DARK half, and the dark half is the physics that is not yet known. **
    board = open(os.path.join(ROOT, 'BOARD.md'), encoding='utf-8', errors='replace').read()
    veins, answered = [], []
    for m in re.finditer(r'## `(L-\d+)`', board):
        seg = board[m.start():m.start() + 3000]
        d = seg.find('DARK')
        if d < 0:
            continue
        veins.append(m.group(1))
        if re.search(r'\u2714 \*\*ANSWERED', re.sub(r'\s+', ' ', seg[d:d + 4000])):
            answered.append(m.group(1))
    print(f'  ⛭ DARK HALVES ANSWERED: {len(answered)} of {len(veins)}   '
          f'{"  ".join(sorted(answered)) if answered else "(none)"}')
    print()
    # ** ---- NARROWING, added r2614 ---- **
    # ** Daryl: "I want all gaps that narrow as you work reported." **  ⇒ *** ANSWERED is binary and
    # most turns do not flip it.  What a turn usually does is NARROW a dark half -- and a report that
    # shows only the flip makes six turns of narrowing look like nothing. ***
    #   ⌗ ** A narrowing is dated in the vein text.  The LAST date on a dark half is when it last
    #   moved; the count of dates is how many times. **
    print('    each dark half, with when it last narrowed:')
    for v in sorted(veins, key=lambda x: int(x[2:])):
        m = re.search(r'## `' + v + r'`', board)
        seg = board[m.start():m.start() + 3000]
        d = seg.find('DARK')
        # ** the DARK section runs to the next bullet or the section end -- a fixed window silently
        # truncated it and reported r2570 for a vein narrowed twice since. **
        end = seg.find('\n- ', d)
        win = re.sub(r'\s+', ' ', seg[d:end if end > d else d + 4000])
        dates = sorted(set(re.findall(r'\br(2\d{3})\b', win)))
        mark = '✔' if v in answered else '⛔'
        print(f'      {mark} {v:<7} narrowed {len(dates):>2}x, last r{dates[-1] if dates else "—"}')
    print()
    print('    ⌗ ** This is the number that measures the programme closing.  The others measure how')
    print('      well it is being kept. **')
    print()

    named, removed = conditions()
    if named is not None:
        live = [c for c in named if c not in removed]
        print(f'  THE MEASURE\'S NECESSARY CONDITIONS (PO-6): {len(live)} live, from {len(named)} as first written')
        for c in named:
            if c in removed:
                print(f'    {c}  ⛔ REMOVED -- {removed[c]}')
            else:
                print(f'    {c}  live')
        print()

    n, unv = ledger()
    print(f'  OPEN LEDGER: {n} qualifications, {unv} unverdicted')

    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    # ** a RANGE HEADER (`| **L-176**--**L-199** |`) is not a row: require the cell to CLOSE after
    # one id.  ⇒ *** Counting the header as live is what put a phantom row in every status this
    # session and made the board and the register disagree by one. ***
    live = len(re.findall(r'^\|\s*\*\*L-\d+\*\*\s*\|', arc, re.M))
    struck = len(re.findall(r'^\|\s*~~L-\d+~~', arc, re.M))
    print(f'  REGISTER: {live} live rows, {struck} struck')
    # ** the wired suite, not every check_*.py on disk -- the workflow is the authority. **
    wf = open(os.path.join(ROOT, '.github', 'workflows', 'gates.yml'),
              encoding='utf-8', errors='replace').read()
    # ** the wired list spans lines; count the check_ tokens on the `for g in` line itself. **
    # ** the list spans CONTINUATION lines; a single-line count reported 4 of 30 for the whole
    # session.  ⇒ *** Walk the continuations to the `do`. *** **
    L = wf.split('\n')
    i = next((k for k, l in enumerate(L) if 'for g in' in l), None)
    names = set()
    if i is not None:
        k = i
        while True:
            names |= {w.rstrip(';') for w in L[k].split()
                      if w.startswith('check_') and w.rstrip(';').isidentifier()}
            if not L[k].rstrip().endswith('\\'):
                break
            k += 1
    # ** r2650: two wired gates have NO failure path (check_arcpins, check_citations) -- they run,
    # print, and return 0.  ⇒ *** Reporting them in the gate count is a green tick nobody earned, so
    # the number reported is the one that can FAIL. *** **
    import re as _re
    _F = _re.compile(r'return 1|exit\(1\)|sys\.exit\(1\)')
    can = {n for n in names
           if os.path.exists(os.path.join(ROOT, 'corpus', n + '.py'))
           and _F.search(open(os.path.join(ROOT, 'corpus', n + '.py'),
                              encoding='utf-8', errors='replace').read())}
    gates = len(can)
    reports = len(names) - len(can)
    rcpts = len(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    print(f'  GATES: {gates} that can fail (+{reports} report-only)   RECEIPTS: {rcpts}')
    print()
    # ** ---- WHAT GOT BUILT, added r2614 ---- **
    # ** Daryl: "along with what gets built." **  ⇒ *** The receipts count alone says nothing -- 423
    # is a number that only rises.  What is informative is what was built RECENTLY and against which
    # item, because that is the trace of a turn on the physics rather than on the bookkeeping. ***
    import subprocess as _sp
    out = _sp.run(['git', 'log', '--since=40.hours', '--diff-filter=A', '--name-only',
                   '--pretty=format:'], cwd=ROOT, capture_output=True, text=True).stdout
    built = sorted({l for l in out.split('\n')
                    if l.startswith('receipts/') and l.endswith('.py')})
    kills_new = sorted({l for l in out.split('\n') if l.startswith('kills/')})
    gates_new = sorted({l for l in out.split('\n')
                        if l.startswith('corpus/check_') and l.endswith('.py')})
    print(f'  BUILT RECENTLY: {len(built)} receipts, {len(gates_new)} gates, {len(kills_new)} kill receipts')
    for b in built[-8:]:
        item = b.split('/')[1] if '/' in b else '?'
        print(f'    {item:<26} {os.path.basename(b)[:52]}')
    for g in gates_new:
        print(f'    {"[GATE]":<26} {os.path.basename(g)}')
    print()
    print('  ⌗ ** If a turn changes nothing above, the turn changed nothing. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""regen_work_edge.py -- the work orders' "what is live" block, GENERATED from the register.

** WHY THIS EXISTS, and it is a defect this line committed and this session had already named twice. **

`CLAUDE_CODE_WORK_ORDER.md` §III⓹ named FOUR rows as "the edge": L-165, L-175, L-221, L-210.
** Within eight revisions all four had been worked ** (r2464-r2479), each carrying a fresh narrowing and
a restated next step.  ⇒ ** An unattended session reading that list finds every item freshly handled and
concludes there is no work left. **

** THE DIAGNOSIS IS ARC 17's, and it applies to instruction documents exactly as it did to THE_PLAN and
THE_EVOLUTION_MAP: ** a document whose content is "what the work is" is made of sentences that are
true-for-now, ** so it goes stale by construction and the staleness is invisible from inside it. **

⇒ *** THE FIX IS r2469's: THE REGISTER IS MACHINE-READABLE, SO "WHICH ROWS ARE LIVE AND CARRY A STATED
    NEXT STEP" IS A COMPUTATION RATHER THAN A LIST SOMEBODY WRITES. ***

** AND THE SPLIT IS THE SAME ONE, because it is the same rule (r2447): **
  * ** GENERATED: which rows are live, and what each says to do next. **  Always current, machine-checked.
  * ** HAND-WRITTEN and preserved verbatim: the PROCEDURE ** -- L-211, how to find edge work when the
    list runs out -- ** because that is a judgement and a gate can check a declaration, not a
    judgement. **

⌗ AND THE ORDERING IS DELIBERATE: the generated block puts ** rows never worked, or worked longest ago,
FIRST **, so a reader taking them in order does not re-tread what was landed an hour before.

    python3 scripts/regen_work_edge.py           # rewrite the blocks
    python3 scripts/regen_work_edge.py --check   # verify they match the register

Written r2479.  Stated for reversal.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
REGISTER = os.path.join(ROOT, 'THE_LIVE_ARC.md')
TARGETS = ['CLAUDE_CODE_WORK_ORDER.md', 'NEXT.md']

BEGIN = '<!-- WORK-EDGE:BEGIN -->'
END = '<!-- WORK-EDGE:END -->'
PROSE = '<!-- WORK-EDGE:PROCEDURE -->'

# rows that are structure or bookkeeping rather than research work
SKIP = re.compile(r'CONSOLIDATE §|see the arc|see §13')


def live_rows():
    """(id, last-worked revision or 0, next-step text) for live rows with a real next step"""
    out = []
    for line in open(REGISTER, encoding='utf-8', errors='replace').read().split('\n'):
        m = re.match(r'^\|\s*\*\*(L-\d+)\*\*\s*\|', line)
        if not m:
            continue
        cells = line.split(' | ')
        if len(cells) < 5:
            continue
        nxt = cells[3].strip()
        if not nxt or nxt in ('—', '-') or SKIP.search(nxt):
            continue
        revs = [int(r) for r in re.findall(r'\br(2\d{3})\b', cells[1])]
        out.append((m.group(1), max(revs) if revs else 0, nxt))
    # never-worked first, then longest-ago first
    return sorted(out, key=lambda x: x[1])


def block(procedure):
    rows = live_rows()
    L = [BEGIN, '']
    L.append('### ⛭⛭ THE LIVE EDGE — **GENERATED** by `scripts/regen_work_edge.py` from '
             '`THE_LIVE_ARC.md`')
    L.append('')
    L.append('> ⚠ **THIS BLOCK IS REGENERATED, NOT WRITTEN — because a hand-written list of live work '
             'goes stale by construction.** *An earlier draft of this file named four rows as "the '
             'edge"; **within eight revisions all four had been worked**, and a session reading that '
             'list would conclude there was no work left.*')
    L.append('>')
    L.append('> ⌗ ***Ordered with the LONGEST-UNWORKED FIRST, so taking them in order does not '
             're-tread what landed an hour ago.***')
    L.append('')
    L.append(f'| row | last worked | what its own row says to do next |')
    L.append('|---|---|---|')
    for rid, rev, nxt in rows[:14]:
        n = re.sub(r'\s+', ' ', nxt)[:150]
        L.append(f'| **`{rid}`** | {("r"+str(rev)) if rev else "*never*"} | {n} |')
    L.append('')
    L.append(f'*{len(rows)} live rows carry a stated next step; the {min(14, len(rows))} '
             f'longest-unworked are shown.*')
    L.append('')
    L.append(PROSE)
    L.append(procedure.strip() if procedure.strip() else
             '> *(no procedure written — how to find edge work when the list runs out is unstated)*')
    L.append('')
    L.append(END)
    return '\n'.join(L)


def main():
    checking = '--check' in sys.argv
    bad = []
    for g in TARGETS:
        p = os.path.join(ROOT, g)
        if not os.path.exists(p):
            continue
        t = open(p, encoding='utf-8', errors='replace').read()
        if BEGIN not in t or END not in t:
            continue
        proc = t.split(PROSE, 1)[1].split(END, 1)[0] if PROSE in t else ''
        head, rest = t.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
        out = head + block(proc) + tail
        if checking:
            if out != t:
                bad.append(g)
        else:
            open(p, 'w', encoding='utf-8').write(out)
            print(f'  {g:<32} {len(live_rows())} live rows with a next step')
    if checking:
        if bad:
            print(f'  [FAIL] work-edge block is stale in: {", ".join(bad)}')
            print('     Run: python3 scripts/regen_work_edge.py')
            return 1
        print('  work-edge blocks match the register')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

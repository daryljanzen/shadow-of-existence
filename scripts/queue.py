#!/usr/bin/env python3
"""queue.py -- THE WORK ON THE TABLE, ENUMERATED.

** WHY.  r2615, Daryl: ** "Every turn you are pulling from some fucking list! ... There is a finite
number of them that we think might advance the programme.  It's not infinite.  You ranked it.  I want to
see it."

  ⇒ ⛔ *** Correct, and the list existed only in this line's head.  Every turn pulled an item from an
      implicit queue assembled by reading five documents, and reported the RESULT without ever showing
      the queue it came from or what the queue did. ***

** WHAT THIS IS. **  Every actionable item the programme currently holds, gathered from its five sources
and printed as ONE numbered list, ordered by `THE_PRIORITY`'s axes.  *** Nothing here is invented: each
line is a row that exists in PROTECTED_OPEN, the board's dark halves, the open ledger's work buckets, the
routed queue, or the dispatch. ***

  ⌗ ** The number that matters is the TOTAL and its movement. **  A turn either takes one off, adds one,
  or leaves it -- and *** all three are informative, because finding a new item is work and hiding that
  it was found is not. ***

    python3 scripts/queue.py

Written r2615.  Stated for reversal.
"""
import glob
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def dark_halves():
    """The veins' dark halves -- the physics not yet known.  OPEN unless marked ANSWERED."""
    board = open(os.path.join(ROOT, 'BOARD.md'), encoding='utf-8', errors='replace').read()
    out = []
    for m in re.finditer(r'## `(L-\d+)`', board):
        seg = board[m.start():m.start() + 9000]
        d = seg.find('DARK')
        if d < 0:
            continue
        end = seg.find('\n- ', d)
        win = re.sub(r'\s+', ' ', seg[d:end if end > d else d + 4000])
        dates = sorted(set(re.findall(r'\br(2\d{3})\b', win)))
        # the first sentence after DARK, trimmed of markup, is what the half asks
        txt = re.sub(r'[*`⛭⛔✔⚠⇒⌗·—]', '', win[4:]).strip(' —-')
        out.append({'id': m.group(1), 'kind': 'DARK HALF',
                    'open': not re.search(r'\u2714 \*\*ANSWERED', win),
                    'narrowed': len(dates), 'last': dates[-1] if dates else None,
                    'what': txt[:78]})
    return out


def po_items():
    po = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    kills = {os.path.basename(f)[:-3] for f in glob.glob(os.path.join(ROOT, 'kills', '*.md'))}
    out = []
    for l in po.split('\n'):
        if not re.match(r'\|\s*\*\*PO-\d+\*\*', l):
            continue
        tag = re.search(r'PO-\d+', l).group(0)
        cells = l.split(' | ')
        what = re.sub(r'[*`⌗]', '', cells[1] if len(cells) > 1 else '').strip()
        dates = sorted(set(re.findall(r'\br(2\d{3})\b', l)))
        out.append({'id': tag, 'kind': 'PROTECTED OPEN', 'open': True,
                    'kill': tag in kills, 'narrowed': len(dates),
                    'last': dates[-1] if dates else None, 'what': what[:78]})
    return out


def ledger_work():
    """The open ledger's buckets that mean WORK -- the others are scope, method or already answered."""
    p = os.path.join(ROOT, 'corpus', 'open_ledger.txt')
    rows = [l for l in open(p, encoding='utf-8') if '|' in l and not l.startswith('#')]
    WORK = ('NAMED-UNBUILT', 'DISCOVERABLE-PROOF', 'STATED-AT-WEIGHT',
            'OPEN-DOWNSTREAM', 'PRECISION')
    out = []
    for r in rows:
        parts = [x.strip() for x in r.split('|', 3)]
        if len(parts) == 4 and parts[2] in WORK:
            out.append({'id': parts[0], 'kind': parts[2], 'open': True,
                        'paper': parts[1], 'what': parts[3].split('##')[0].strip()[:70]})
    return out


def routed():
    t = open(os.path.join(ROOT, 'FOR_54.md'), encoding='utf-8', errors='replace').read()
    out = []
    for l in t.split('\n'):
        if l.startswith('## ') and re.search(r'(?<!\d)\d+\s*·', l) and '✔' not in l:
            n = re.search(r'(?<!\d)(\d+)\s*·', l).group(1)
            out.append({'id': f'item {n}', 'kind': 'ROUTED', 'open': True,
                        'what': re.sub(r'[*#`]', '', l).split('·', 1)[-1].strip()[:70]})
    return out


def dispatch():
    d = open(os.path.join(ROOT, 'THE_DISPATCH.md'), encoding='utf-8', errors='replace').read()
    return [{'id': a, 'kind': 'DISPATCH', 'open': True, 'what': ''}
            for a in re.findall(r'\| \*\*(A\d+)\*\* \|', d)]


def main():
    dh = dark_halves()
    everything = dh + po_items() + ledger_work() + routed() + dispatch()
    live = [x for x in everything if x['open']]

    print()
    print('  ' + '=' * 76)
    print(f'  THE WORK ON THE TABLE: {len(live)} items')
    print('  ' + '=' * 76)
    print()

    print(f'  ⛭ DARK HALVES -- the physics not yet known ({sum(1 for x in dh if x["open"])} of {len(dh)} open)')
    for x in dh:
        mark = '⛔' if x['open'] else '✔'
        print(f'     {mark} {x["id"]:<7} narrowed {x["narrowed"]}x, last r{x["last"] or "—"}   {x["what"][:52]}')
    print()

    po = po_items()
    print(f'  PROTECTED OPEN -- {len(po)} items, {sum(1 for x in po if x["kill"])} with kill receipts')
    for x in po:
        print(f'     {x["id"]:<7} {"kill" if x["kill"] else "    ":<5} '
              f'{x["narrowed"]:>2}x last r{x["last"] or "—"}   {x["what"][:48]}')
    print()

    lw = ledger_work()
    print(f'  LEDGER WORK -- {len(lw)} qualifications that mean work')
    for k, n in Counter(x['kind'] for x in lw).most_common():
        who = ', '.join(sorted({x['paper'] for x in lw if x['kind'] == k}))
        print(f'     {k:<20} {n:>2}   {who[:46]}')
    print()

    rt, dp = routed(), dispatch()
    print(f'  ROUTED -- {len(rt)}')
    for x in rt:
        print(f'     {x["id"]:<8} {x["what"][:60]}')
    print(f'  DISPATCH -- {len(dp)}: {" ".join(x["id"] for x in dp)}')
    print()
    print(f'  ⇒⇒ TOTAL ON THE TABLE: {len(live)}')
    print('     ** A turn takes one off, adds one, or leaves it.  All three are informative --')
    print('       finding a new item IS work, and hiding that it was found is not. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

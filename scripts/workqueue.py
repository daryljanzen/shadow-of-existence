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

    python3 scripts/workqueue.py

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


def dark_halves_distinct():
    """Live dark halves that are NOT a PO row under another name.

    ** r2696: both live halves were duplicates. **  `PO-5`'s row states "register alias:
    `L-221`" in print, and the board's vein header reads "`L-165` · PO-6".  *** The stamp read
    DARK and PO from different files and added them, so one problem counted twice, twice. ***
      ⌗ ** A vein is a working space and is not deleted ** -- what is removed is its
        contribution to the COUNT.
    """
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    board = open(os.path.join(ROOT, 'BOARD.md'), encoding='utf-8', errors='replace').read()
    out = []
    for d in dark_halves():
        if not d['open']:
            continue
        tag = d['id']
        aliased = (tag in raw) or re.search(re.escape(tag) + r'`?\s*·\s*PO-\d+', board)
        if not aliased:
            out.append(d)
    return out


def po_items():
    po = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    kills = {os.path.basename(f)[:-3] for f in glob.glob(os.path.join(ROOT, 'kills', '*.md'))}
    out = []
    for l in po.split('\n'):
        # ** a STRUCK row (`| ~~PO-8~~ |`) is closed and must not be counted as work on the table. **
        if not re.match(r'\|\s*\*\*PO-\d+\*\*', l):
            continue
        tag = re.search(r'PO-\d+', l).group(0)
        # ** an item whose question is ANSWERED and whose checks all pass is a RECORD awaiting a
        # procedural strike, not open work.  r2644: PO-9's object is a two-branch question and the
        # second branch is the answer -- counting it as open overstates what is left. **
        answered = 'THE QUESTION IS ANSWERED' in l or 'QUESTION IS ANSWERED' in l
        cells = l.split(' | ')
        what = re.sub(r'[*`⌗]', '', cells[1] if len(cells) > 1 else '').strip()
        dates = sorted(set(re.findall(r'\br(2\d{3})\b', l)))
        out.append({'id': tag, 'kind': 'PROTECTED OPEN', 'open': not answered,
                    'answered': answered,
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
        # ** r2695: '✔' alone is not the only way an item closes.  *** Item 59 carried
        # "⛔⛔ AND ANSWERED AT c54.212" IN ITS OWN HEADER and was still counted live, because
        # the reader tested for one glyph.  A queue whose CLOSE marker is a single character
        # will count every other way of closing as open. ***
        DONE = ('✔', 'ANSWERED', 'WITHDRAWN', 'DISCHARGED', 'CLOSED', 'RETIRED')
        if (l.startswith('## ') and re.search(r'(?<!\d)\d+\s*·', l)
                and not any(d in l for d in DONE)):
            n = re.search(r'(?<!\d)(\d+)\s*·', l).group(1)
            out.append({'id': f'item {n}', 'kind': 'ROUTED', 'open': True,
                        'what': re.sub(r'[*#`]', '', l).split('·', 1)[-1].strip()[:70]})
    return out


def dispatch():
    """** PARKED items are listed and NOT counted.  r2640, Daryl: ** "Preparing a book stays at the very
    bottom of this list.  No interest till it's earned."  ⇒ *** An item nobody is waiting on is not work
    on the table -- the total should say what is WORKABLE, and a parked item inflates it while looking
    like progress when it is finally struck. ***"""
    d = open(os.path.join(ROOT, 'THE_DISPATCH.md'), encoding='utf-8', errors='replace').read()
    out = []
    for a in re.findall(r'\| \*\*(A\d+)\*\* \|', d):
        m = re.search(r'\| \*\*' + a + r'\*\* \|(.{0,400})', d, re.S)
        parked = bool(m and 'DEPRIORITISED' in m.group(1))
        out.append({'id': a, 'kind': 'DISPATCH', 'open': not parked,
                    'parked': parked, 'what': ''})
    return out


def main():
    dh = dark_halves()
    # ** the TOTAL counts only what is still open: an ANSWERED dark half and a STRUCK PO row are
    # closed, and counting them inflates the table by items nobody can pick up.  ⇒ *** PO-8 sat in the
    # OPEN register for 238 revisions after its own kill receipt recorded the authorisation, and every
    # count of "what is left" carried it. *** **
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

    # ** r2617: EVERY ITEM, not a bucket count.  Daryl: "That's five separate lists you just pulled
    # from and you're withholding from me every one of those lists."  ⇒ *** A summary line is a list
    # withheld.  If a thing is on the table it gets a line, because the choice of what to attack next
    # is only legible against everything that was not chosen. ***
    lw = ledger_work()
    print(f'  LEDGER WORK -- {len(lw)} qualifications that mean work')
    for x in sorted(lw, key=lambda y: (y['kind'], y['paper'])):
        txt = re.sub(r'\\[a-zA-Z]+|[{}$~\\]', '', x['what'])
        print(f'     {x["kind"]:<19} {x["paper"][:16]:<16} {txt[:52]}')
    print()

    rt, dp = routed(), dispatch()
    print(f'  ROUTED -- {len(rt)}')
    for x in rt:
        print(f'     {x["id"]:<9} {x["what"][:64]}')
    print()
    d = open(os.path.join(ROOT, 'THE_DISPATCH.md'), encoding='utf-8', errors='replace').read()
    live_dp = [x for x in dp if x['open']]
    print(f'  DISPATCH -- {len(live_dp)} live, {len(dp) - len(live_dp)} parked')
    for x in dp:
        m = re.search(r'\| \*\*' + x['id'] + r'\*\* \|(.{0,240})', d, re.S)
        txt = re.sub(r'\s+', ' ', re.sub(r'[*`|]', '', m.group(1))) if m else ''
        print(f'     {x["id"]:<9} {txt[:64]}')
    print()
    print(f'  ⇒⇒ TOTAL ON THE TABLE: {len(live)}')
    print('     ** A turn takes one off, adds one, or leaves it.  All three are informative --')
    print('       finding a new item IS work, and hiding that it was found is not. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

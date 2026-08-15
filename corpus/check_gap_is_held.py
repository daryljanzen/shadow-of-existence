#!/usr/bin/env python3
"""check_gap_is_held.py -- THE MAP MUST CARRY EVERY OPEN ROW'S OWN OBJECT.

** WHY.  r2829. **  *** `OPEN_PROBLEMS_MAP.md` carried five of six open rows' objects and ** not
`PO-5`'s **.  It said "coupling" fifteen times and "multiplet" ** zero **.  The coupling is the ROUTE;
`PO-5`'s object is "the quark/lepton split ... the five multiplets, and which carries the colour 3", and
r2609 had already recorded that the route and the object came apart. ** The map kept the route. ** ***

  ⇒ ** So a node reading the map to learn the gap learned a reconstruction, not the gap. **  *** And
      that is exactly how a session spends a day on the wrong object while every gate stays green:
      nothing checked that the held state matched the rows. ***

** ⛭⛭ WHAT MAKES THIS DETECTABLE. **  *** A row states its own object in its object cell.  ** If the map
that is supposed to hold the gap does not contain that object's distinctive words, the map is holding
something else. **  A string check is enough, because the failure is not subtlety -- it is absence. ***

** WHAT THIS CHECKS. **  For every open `PROTECTED_OPEN` row, a distinctive phrase from its ** own object
cell ** must appear in `OPEN_PROBLEMS_MAP.md`.

  ⌗ ** It does not check that the map is RIGHT about the object ** -- *** only that the object is
    present.  A map that carries the words and misdescribes them is a different failure and this gate
    does not see it.  What it stops is the gap silently becoming a different gap. ***

    python3 corpus/check_gap_is_held.py

Written r2829.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

ROW = re.compile(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*')
MAP = 'OPEN_PROBLEMS_MAP.md'

# ** words too common to discriminate -- a hit on these proves nothing **
STOP = {'the', 'and', 'a', 'an', 'of', 'in', 'on', 'at', 'is', 'it', 'its', 'to', 'for',
        'what', 'which', 'that', 'this', 'as', 'against', 'with', 'from', 'not', 'but',
        'sector', 'paper', 'stated', 'own', 'full', 'built', 'open', 'level', 'whether'}


# ** r2829a: an object cell may OPEN with a register alias -- "⌗ register alias: L-221
# (renumbered from L-174 at r2426...)".  *** The seed test did not fire because the keys came
# from that bookkeeping ("register" appears 95 times in the map) instead of from the object.
# Strip any leading ⌗-marked aside before extracting. *** **
ALIAS = re.compile(r'^\s*⌗[^.]*\.\s*')


def distinctive(text, k=3):
    """The k rarest substantial words in the object cell, after any leading alias aside."""
    text = ALIAS.sub('', text)
    words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z/\-]{4,}", text)]
    seen, out = set(), []
    for w in words:
        if w in STOP or w in seen:
            continue
        seen.add(w)
        out.append(w)
    return out[:k]


def main():
    print()
    print('  check_gap_is_held -- does the map carry every open row\'s own object?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    mp = open(os.path.join(ROOT, MAP), encoding='utf-8', errors='replace').read().lower()

    missing, checked = [], 0
    for l in raw.split('\n'):
        m = ROW.match(l)
        if not m or m.group(1) or l.lstrip('|').lstrip().startswith('~~'):
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', l)[1:-1]]
        if len(cells) < 2:
            continue
        obj = re.sub(r'[*`$\\]', '', cells[1])
        keys = distinctive(obj)
        if not keys:
            continue
        checked += 1
        # ** r2829b: `any` passed the seed because 'baryon' is shared with PO-2's object.
        # *** A key that another row also uses cannot show THIS row is held.  Keep only the
        # keys no other open row's object uses -- the discriminating ones -- and require
        # one of THOSE. ***
        others = set()
        for l2 in raw.split('\n'):
            m2 = ROW.match(l2)
            if not m2 or m2.group(2) == m.group(2):
                continue
            c2 = [c.strip() for c in re.split(r'(?<!\\)\|', l2)[1:-1]]
            if len(c2) > 1:
                others |= set(distinctive(re.sub(r'[*`$\\\\]', '', c2[1]), k=8))
        disc = [k for k in keys if k not in others] or keys
        # ** r2829c: `any` over discriminating keys STILL passed the seed -- 'split' (26)
        # and 'baryon' (17) occur in the map for unrelated reasons.  *** One word of an
        # object is not the object.  Require ALL of them: if the map holds this row's
        # object it carries the object's phrase, not a word borrowed from elsewhere. ***
        absent = [k for k in disc if k not in mp]
        if absent:
            missing.append((m.group(2), absent, obj[:64]))

    print(f'  {checked} open row(s) checked against {MAP}')
    if missing:
        print()
        for pid, keys, obj in missing:
            print(f'    [FAIL] {pid}: none of {keys} appears in the map')
            print(f'           object: "{obj}"')
        print()
        print('    ⛭ ** The map is holding something other than this row\'s object. **')
        print('       *** Most often it is holding the ROUTE the row was last worked along —')
        print('       which is how a session spends a day on the wrong object with every gate')
        print('       green. Put the row\'s own object in the map. ***')
        return 1

    print('  every open row\'s object is present in the map.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

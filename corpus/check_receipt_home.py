#!/usr/bin/env python3
"""check_receipt_home.py -- ONE PAPER, ONE RECEIPT HOME.

** WHY THIS EXISTS. **  Several papers carry a second receipt directory and one carried a
third, and nothing declared which was the home.  A node adding a receipt then GUESSES.
Node 64 guessed wrong twice in a single session -- `P8_slicing_operator` beside the
existing `P08_slicing_operator` at r6403, and a stray `P17_geometric_core` beside
`P17_geometric_core_paper` at r6437 -- and ** neither was visible to `check_receipts`,
because a row naming a real path resolves. **  The defect is invisible to every instrument
that checks resolution, which is why it needed one that checks PLACEMENT.

** WHAT IT DOES AND DOES NOT DO. **  It fails on a receipt in a directory that is neither
the paper's declared home nor one of its grandfathered legacy directories -- i.e. on a NEW
stray.  ** It does not ask anything in the tree to move. **  That is deliberate and it is
not laziness: `check_receipt_prefixes` faced the same shape in the filename namespace and
chose the same remedy in its own words --

    "the bands apply going forward and existing allocations are grandfathered.  Nothing in
     the tree needs to move for this gate to be green; what it stops is the NEXT collision."

Relocating hundreds of files would break every path in `INDEX.md`, every appendix generated
from it, and every quotation of a path in a receipt's own prose, ** to fix a defect whose
whole cost is that the next node guesses. **  Declaring the home removes that cost outright.

⌗ THE HOMES ARE DATA, in `corpus/receipt_home.txt`, alongside `node_roster.txt`.  A paper
gaining a directory is a one-line edit there, in the same commit as the receipt.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HOMES = os.path.join(HERE, 'receipt_home.txt')
RECEIPTS = os.path.join(HERE, '..', 'receipts')


def declared():
    """paper -> (home, {legacy...})"""
    out = {}
    if not os.path.exists(HOMES):
        return out
    for ln in open(HOMES, encoding='utf-8'):
        ln = ln.strip()
        if not ln or ln.startswith('#'):
            continue
        f = ln.split()
        out[f[0]] = (f[1], set(f[2:]))
    return out


def paper_of(dirname):
    """P08_slicing_operator -> P8 ; p0_geometric_core -> P17 (the deprecated tag folds)"""
    m = re.match(r'^(p0|P\d{1,2})_', dirname)
    if not m:
        return None
    t = m.group(1)
    return 'P17' if t == 'p0' else 'P' + str(int(t[1:]))


def main():
    homes = declared()
    if not homes:
        print('  [FAIL] corpus/receipt_home.txt is absent -- the homes are data and must exist')
        return 1
    print()
    print('  RECEIPT HOMES -- one paper, one home; legacy directories grandfathered')
    print()
    strays, known = [], 0
    for d in sorted(os.listdir(RECEIPTS)):
        if not os.path.isdir(os.path.join(RECEIPTS, d)):
            continue
        p = paper_of(d)
        if p is None:
            continue                       # lead-scoped directories are not this gate's
        if p not in homes:
            strays.append((d, p, 'the paper is not declared in receipt_home.txt'))
            continue
        home, legacy = homes[p]
        if d == home or d in legacy:
            known += 1
            continue
        strays.append((d, p, f"neither {p}'s home ({home}) nor grandfathered"))

    for p, (home, legacy) in sorted(homes.items()):
        n = len(os.listdir(os.path.join(RECEIPTS, home))) if os.path.isdir(os.path.join(RECEIPTS, home)) else 0
        mark = f"   (+{len(legacy)} legacy)" if legacy else ''
        print(f'    {p:<5} {home:<30} {n:>4} file(s){mark}')
    print()
    if strays:
        print(f'  ⛔ {len(strays)} STRAY RECEIPT DIRECTOR(Y/IES):')
        for d, p, why in strays:
            print(f'    [FAIL] receipts/{d} -- {why}')
        print('     Move the file to the paper\'s declared home, or -- if the directory is')
        print('     genuinely wanted -- add it to corpus/receipt_home.txt in the same commit.')
        print()
        return 1
    print(f'  {known} paper receipt director(y/ies) placed; no strays.')
    print('  ⌗ This gate checks PLACEMENT.  check_receipts checks RESOLUTION, and a stray')
    print('    resolves perfectly -- which is why it was invisible until now.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

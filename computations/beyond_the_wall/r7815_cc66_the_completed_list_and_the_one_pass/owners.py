#!/usr/bin/env python3
"""r7815 (cc66) -- for a named receipt, WHICH control banks does it load and at
WHAT POINT is each?

`cross.py` answers that for a sentence that CITES a receipt.  69's ruling is that
the figures the swap-log list missed are in sentences that cite none, so each of
those is hand-read to the quantity it prints and the receipt that owns that
quantity is named by hand.  This file is the second half of that read: it takes
the named owner and says what the owner's own banks are, so "this figure moves"
is a statement about a bank's stored background and not about my recollection.

Usage: python3 owners.py <receipt-name-fragment> [...]
"""
import os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cross                                             # noqa: E402
ROOT = cross.ROOT

def main():
    frags = sys.argv[1:]
    if not frags:
        print(__doc__)
        return 2
    for frag in frags:
        hits = sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', f'*{frag}*.py'),
                                recursive=True))
        if not hits:
            print(f'\n{frag}: NO RECEIPT MATCHES')
            continue
        for h in hits:
            banks = cross.banks_of(h)
            lcdm = sorted((cross.BANKS[b][1], b) for b in banks
                          if cross.BANKS[b][0] in ('lcdm', '?'))
            other = sorted(b for b in banks if cross.BANKS[b][0] not in ('lcdm', '?'))
            print(f'\n== {os.path.relpath(h, ROOT)}')
            if not banks:
                print('   names no bank in a string literal (built at runtime, or no bank at all)')
            for cls, b in lcdm:
                print(f'   {cls:9s} {b}')
            if other:
                print(f'   (non-lcdm arms: {len(other)} bank(s))')
    return 0

if __name__ == '__main__':
    sys.exit(main())

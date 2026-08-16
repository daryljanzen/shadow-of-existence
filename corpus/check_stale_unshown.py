#!/usr/bin/env python3
"""check_stale_unshown.py -- ONE RECEIPT'S "NOT SHOWN" MUST NOT OUTLIVE ANOTHER'S "SHOWN".

** WHY.  r2885-r2887. **  *** r2885 read `P03_thirds_from_closure`'s ** "it does not show the antecedent
-- that is `L-74` and it is now the gate" ** and recorded `PO-1c` as gated on it.  ** r2886 found
`P14_route_or_point` had closed `L-74` **: "with `L-72` AND `L-74` BOTH CLOSED, the winding sector's
premises are COMPUTED".  A whole revision spent on a gate that did not exist. ***

  ⇒ ** This is the withdrawal-propagation failure BETWEEN RECEIPTS ** -- *** the gates built at r2832
      cover rows, reports, leads and routing, and nothing covered receipt-to-receipt. ***

** AND THE MEASUREMENT MATTERS AS MUCH AS THE DEFECT.  ***  Swept: ** exactly three instances **
(`L-74`, `L-88`, `L-89`).  *** The hypothesis that the register's picture of what is open is inflated
ACROSS THE BOARD is WRONG -- the corpus is more coherent than that.  ** A small number is the finding,
and it is stated because a large one would have been reported. ** ***

** WHAT THIS CHECKS. **  *** Any lead named "not shown / is now the gate / not established" in one
receipt while another names it "CLOSED / answered / discharged" must carry a mark in the first. ***

    python3 corpus/check_stale_unshown.py

Written r2887.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

OPEN_A = re.compile(r'(not shown|does not show|is now the gate|unshown|NOT established|'
                    r'stays alive as)[^.\n]{0,120}?\b(L-\d+)\b', re.I)
OPEN_B = re.compile(r'\b(L-\d+)\b[^.\n]{0,120}?(not shown|does not show|is now the gate|unshown)', re.I)
CLOSE_A = re.compile(r'\b(L-\d+)\b[^.\n]{0,80}?(CLOSED|is the answer to|answered|discharged|cleared)', re.I)
CLOSE_B = re.compile(r'(CLOSED|discharged|cleared|answered)[^.\n]{0,80}?\b(L-\d+)\b', re.I)
MARKED = re.compile(r'r28[89]\d|SINCE CLOSED|since closed|superseded', re.I)


def main():
    print()
    print('  check_stale_unshown -- does any receipt call open what another has closed?')
    print()
    opens, closes = {}, {}
    files = sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    for f in files:
        b = os.path.basename(f)[:-3]
        t = open(f, encoding='utf-8', errors='replace').read()
        for m in OPEN_A.finditer(t):
            opens.setdefault(m.group(2), []).append((b, f))
        for m in OPEN_B.finditer(t):
            opens.setdefault(m.group(1), []).append((b, f))
        for m in CLOSE_A.finditer(t):
            closes.setdefault(m.group(1), set()).add(b)
        for m in CLOSE_B.finditer(t):
            closes.setdefault(m.group(2), set()).add(b)

    bad = []
    for lead, sites in opens.items():
        if lead not in closes:
            continue
        for b, f in sites:
            if b in closes[lead]:
                continue
            t = open(f, encoding='utf-8', errors='replace').read()
            i = t.find(lead)
            if MARKED.search(t[max(0, i-400):i+400]):
                continue
            bad.append((lead, b, sorted(closes[lead])[0]))

    print(f'  {len(files)} receipt(s); {len(opens)} lead(s) named open, {len(closes)} named closed')
    if bad:
        print()
        for lead, opener, closer in bad[:10]:
            print(f'    [FAIL] {opener}')
            print(f'           calls {lead} open; {closer} has closed it')
        print()
        print('    ⛭ ** One receipt\'s "not shown" outliving another\'s "shown" costs a whole')
        print('       revision. ***  r2885 was spent on a gate that did not exist. ***')
        return 1

    print('  no receipt calls open what another has closed.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

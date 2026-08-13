#!/usr/bin/env python3
"""check_killrefs.py -- A KILL RECEIPT'S VERDICT AND THE ROWS THAT POINT AT IT MUST AGREE.

** WHY.  r2599 corrected `kills/PO-7.md` -- check ② does not clear -- and corrected the `PROTECTED_OPEN`
row in the same turn.  ** ⇒ ⛔ *** And `L-171`'s next-step still read "all four now pass" and "the next
step is the register's own: and Daryl authorises" for three revisions after. ***

  ⌗ ** The same failure one register out: ** a correction reached the instrument and the register and not
  the LEAD that points at them.  *** That is `check_depmatrix`'s two-place lesson at a third place, and it
  is the reason the r2570/r2559 contradiction survived inside one file for twenty-nine revisions. ***

** WHAT IT CHECKS. **  For every receipt under `kills/`, whether it reports a check that ** does not
clear **.  If it does, no register row or lead may say the item is ** awaiting authorisation ** or that
** all four checks pass **.
  ⇒ *** A receipt that does not clear is not waiting on anyone.  Saying it is manufactures a decision, and
      a manufactured decision left in a register is one somebody may act on. ***

** ⚠ WHAT IT DOES NOT CHECK. **  Whether the receipt's own verdict is right -- that is a reading.  ** And
it does not fire on a receipt whose checks DO all clear: those legitimately await authorisation. **

    python3 corpus/check_killrefs.py

Written r2602.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

NOT_CLEAR = re.compile(r"(does not clear|DOES NOT CLEAR|fails? on route|\u26d4 \u2461|\u26d4 \u2463)")
AWAITING = re.compile(r"(awaiting authorisation|awaits authorisation|all four (?:checks )?(?:now )?pass"
                      r"|the next step is the register's own|and Daryl authorises)", re.I)
# ** THE ONE NAMED EXCLUSION. **  The exit procedure's own text -- "② Its object is named, all four
# checks are written into a kill receipt under `kills/`, and Daryl authorises" -- is QUOTED in places
# that then say the quotation no longer applies.  ⇒ *** A quotation of the rule is not a claim that the
# rule has been reached; the tell is a supersession marker within the same clause. ***
SUPERSEDED = re.compile(r"(the old reading|superseded|corrected r\d{4}|was never reached|it was not)", re.I)
WATCHED = ('THE_LIVE_ARC.md', 'PROTECTED_OPEN.md', 'BOARD.md', 'THE_STATE.md',
           'THE_CLOSURE_PLAN.md', 'THE_RESIDUAL.md', 'THE_FRONT_EDGE.md')


def main():
    print()
    print("  check_killrefs -- do the rows agree with their kill receipt's verdict?")
    print()
    bad = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'kills', '*.md'))):
        tag = os.path.basename(f).replace('.md', '')
        body = re.sub(r'\s+', ' ', open(f, encoding='utf-8', errors='replace').read())
        if not NOT_CLEAR.search(body):
            continue                      # all checks clear: legitimately awaiting authorisation
        print(f'  {tag}: reports a check that DOES NOT CLEAR')
        for w in WATCHED:
            p = os.path.join(ROOT, w)
            if not os.path.exists(p):
                continue
            for line in open(p, encoding='utf-8', errors='replace'):
                if tag not in line and tag.replace('PO-', 'PO-') not in line:
                    continue
                flat = re.sub(r'\s+', ' ', line)
                m = AWAITING.search(flat)
                if m and not SUPERSEDED.search(flat[max(0, m.start()-200):m.end()+200]):
                    bad.append((tag, w, m.group(0)))
    print()
    if bad:
        for tag, w, phrase in bad:
            print(f'    [FAIL] {w} says "{phrase}" of {tag}')
        print()
        print('    ⛔ A RECEIPT THAT DOES NOT CLEAR IS NOT WAITING ON ANYONE.  ** Saying it is')
        print('       manufactures a decision, and a manufactured decision left in a register is one')
        print('       somebody may act on. **')
        return 1
    print('  no row claims authorisation is pending on a receipt that does not clear.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

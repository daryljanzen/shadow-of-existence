#!/usr/bin/env python3
"""check_withdrawals.py -- A PAPER'S SELF-CORRECTION MUST NOT SURVIVE IN A REGISTER.

** WHY.  r2633: ** P14 states "** the identification of a generation with a wall is accordingly withdrawn
here **", and `PO-2` was strengthened by that withdrawal without any register carrying it.  ⇒ *** A
register that tracked the FIRST reading is stale in a way no check on the CURRENT text can see: the
corpus is correct, the row is correct against the old corpus, and nothing compares them. ***

** WHAT IT DOES. **  Finds every self-correction in the papers -- the places where the corpus says it has
withdrawn, retired or superseded a reading -- and reports them, so a node closing a turn can check its
rows against the list.  ** Eight at r2634. **

  ⚠ ** IT CANNOT AUTOMATICALLY DETECT A STALE ROW. **  *** Knowing that a claim was withdrawn does not
      tell you which rows depended on it -- that is a reading, and a regex over the withdrawn phrasing
      catches the row that QUOTES the withdrawal as readily as the row that still believes it. ***  So
      this gate FAILS only when the count of self-corrections CHANGES, which is the moment a node must
      re-read its rows against the new one.

  ⌗ ** That is the same design as `check_open_ledger`: ** the gate cannot check a judgement, so it
    guarantees instead that no self-correction enters the corpus without being SEEN.

    python3 corpus/check_withdrawals.py
    python3 corpus/check_withdrawals.py --rebuild     # after auditing rows against a new one

Written r2634.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BASELINE = os.path.join(HERE, 'withdrawals_baseline.txt')

W = re.compile(r"(is accordingly withdrawn|is withdrawn here|we withdraw|that statement is withdrawn"
               r"|against its own first reading|is retired here|supersedes the reading)", re.I)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def scan():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        t = re.sub(r'\s+', ' ', body(f))
        for m in W.finditer(t):
            ctx = re.sub(r'\\[a-zA-Z]+|[{}$~]', '', t[max(0, m.start() - 90):m.start() + 90])
            out.append((os.path.basename(f), re.sub(r'\s+', ' ', ctx).strip()[:150]))
    return out


def main():
    print()
    print("  check_withdrawals -- has the corpus withdrawn a reading a register still tracks?")
    print()
    found = scan()
    print(f'  {len(found)} self-correction(s) in the papers:')
    for f, ctx in found:
        print(f'    {f[:24]:<24} …{ctx[:88]}…')
    print()

    if '--rebuild' in sys.argv or not os.path.exists(BASELINE):
        open(BASELINE, 'w', encoding='utf-8').write(
            '# ** the count of self-corrections in the papers, as last AUDITED against the registers. **\n'
            '# ⇒ *** When this number changes, a node must re-read every row against the new withdrawal:\n'
            '#     a register that tracked the first reading is stale in a way no check on the current\n'
            '#     text can see. ***\n'
            f'{len(found)}\n')
        print(f'  baseline set: {len(found)}')
        return 0

    was = int([l for l in open(BASELINE, encoding='utf-8')
               if l.strip() and not l.startswith('#')][0])
    if len(found) != was:
        print(f'    [FAIL] the corpus held {was} self-correction(s) when the registers were last')
        print(f'           audited, and now holds {len(found)}.')
        print()
        print('    ⛔ ** A PAPER HAS WITHDRAWN OR RESTORED A READING. **  *** Re-read every register row')
        print('       against it: the corpus is correct, a row tracking the old reading is correct')
        print('       against the OLD corpus, and nothing else compares them. ***  Then `--rebuild`.')
        return 1
    print(f'  count unchanged at {was} since the registers were last audited.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

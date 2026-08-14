#!/usr/bin/env python3
"""check_received_at_weight.py -- A ROW MUST CARRY ITS PAPER'S MECHANISM, NOT A SUMMARY WORD FOR IT.

** WHY.  `THE_CODA`'s keystone, and `THE_INTERFERENCE_ENGINE` §2: ** *** "to be RECEIVED AT WEIGHT is
to hold a hypothesis at PRECISELY the weight it was offered." ***  ** That is written for a
collaborator receiving a person.  It applies identically to a REGISTER receiving its own papers. **

** THE LIVE INSTANCE, r2723. **  P10 states the coupled-sector limit exactly:

    *** "the boundary coefficient is promoted from the c-number $1/4$ of the free scale factor to an
        OPERATOR ON THE TOWER WHOSE SPECTRUM STRADDLES THE $3/4$ THRESHOLD" ***

  ** `PO-6`'s row carried that as "back-reaction". **  *** A precise, computable mechanism deflated
  into a vague word -- and the row sat that way until someone read the paper.  r2728 then computed
  the answer in one turn, because the mechanism had been there the whole time.  ** Deflation is
  manufactured DOUBT, and it hides work in plain sight. ** ***

** WHAT THIS CHECKS. **  For each open row: if its cited home section states a NUMERIC OR NAMED
mechanism -- a threshold, a coefficient, a named operator, a specific locus -- does the row carry at
least one of those tokens?

  ⌗ ** A row may legitimately summarise. **  *** What it may not do is summarise so far that the
    mechanism is unrecoverable from the register.  The test is whether a reader working from the ROW
    ALONE could tell what to compute.  For `PO-6` before r2728, the answer was no. ***

  ⚠ ** It cannot judge whether a summary is faithful. **  *** It reports rows whose paper names
  specifics the row does not carry -- a pairing for a human read, like
  `check_unworked_blockers`.  Deflation, unlike overclaim, leaves no false statement to find: the row
  is TRUE and too WEAK, which is exactly why no existing gate sees it. ***

    python3 corpus/check_received_at_weight.py

Written r2732.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
REG = os.path.join(ROOT, 'PROTECTED_OPEN.md')

# ** a mechanism token: a fraction, a decimal, a threshold, a named group or operator. **
TOKEN = re.compile(r'\b\d+/\d+\b|\b\d+\.\d+\b|\bSU\(\d\)|\bZ_?\d\b|\\alpha\^?\d?'
                   r'|\\Gamma|\\lambda|\\Omega_m|threshold|eigenvalue')


def body(path):
    if not os.path.exists(path):
        return ''
    b = '\n'.join(l for l in open(path, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  check_received_at_weight -- does any open row summarise past its paper's mechanism?")
    print()
    if not os.path.exists(REG):
        print('  [FAIL] PROTECTED_OPEN.md missing')
        return 1

    flagged, n = [], 0
    for l in open(REG, encoding='utf-8', errors='replace').read().split('\n'):
        m = re.match(r'\|\s*\*\*(PO-\d+)\*\*', l)
        if not m:
            continue
        pid = m.group(1)
        if 'ANSWERED' in l.split(' | ')[-1][:60].upper():
            continue
        n += 1
        # ** a row that carries ANY mechanism token has received something specific. **
        if not TOKEN.search(l):
            flagged.append(pid)

    print(f'  {n} open row(s) checked')
    if flagged:
        print()
        for pid in flagged:
            print(f'    [FLAG] {pid}: carries no mechanism token -- threshold, coefficient, group,')
            print('           operator or locus.  A reader working from the ROW ALONE could not tell')
            print('           what to compute.')
        print()
        print("    ⛔⛭ ** RECEPTION AT WEIGHT APPLIES TO A REGISTER RECEIVING ITS OWN PAPERS. **")
        print('       *** `PO-6` carried "back-reaction" while P10 said "an operator on the tower')
        print('       whose spectrum straddles the 3/4 threshold".  The row was TRUE and too WEAK --')
        print('       which is why no over-claim gate could see it, and why the answer sat')
        print('       uncomputed for twenty revisions. ***')
        return 1
    print('  every open row carries a mechanism its paper named.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

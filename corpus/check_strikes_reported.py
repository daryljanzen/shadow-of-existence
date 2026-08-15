#!/usr/bin/env python3
"""check_strikes_reported.py -- A STRUCK ROW MUST BE RECORDED AS STRUCK WHEREVER IT IS REPORTED.

** WHY.  r2832. **  *** Two rows were struck this revision.  `OPEN_PROBLEMS_MAP` -- the document a node
reads to learn the gap -- still carried them as ** "ANSWERED ... rows had read OPEN" **, which was
accurate when written and stale the moment the strike landed. ***

  ⇒ ** This is the withdrawal-propagation failure one level up. **  *** There, a correction reached one
      ROW and not another.  Here, a strike reaches the REGISTER and not the documents that report it --
      and a reader taking the state from a reporting document gets a row that no longer exists as
      open. ***

** WHAT THIS CHECKS. **  *** For every struck row: any reporting document that names it must also name
its strike -- the word STRUCK, or the revision that struck it -- somewhere in the same paragraph. ***

  ⌗ ** A historical line is not a violation ** -- *** "PO-3 read OPEN for fifty revisions" is a true
    statement about the past.  What the check requires is that the CURRENT status be recoverable, so a
    paragraph naming the row must also carry the strike. ***

    python3 corpus/check_strikes_reported.py

Written r2832.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

ROW = re.compile(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*')
DOCS = ['BOARD.md', 'THE_PLAN.md', 'OPEN_PROBLEMS_MAP.md',
        'THE_OPEN_PROBLEMS_LEDGER.md', 'THE_REMAINING_WORK.md']


def main():
    print()
    print('  check_strikes_reported -- is every struck row recorded as struck where it is reported?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()

    struck, rev = set(), {}
    for l in raw.split('\n'):
        m = ROW.match(l)
        if m and (m.group(1) or l.lstrip('|').lstrip().startswith('~~')):
            struck.add(m.group(2))
            r = re.search(r'STRUCK\s+(r\d{4})', l)
            if r:
                rev[m.group(2)] = r.group(1)

    print(f'  {len(struck)} struck row(s): {sorted(struck)}')

    bad = []
    for d in DOCS:
        f = os.path.join(ROOT, d)
        if not os.path.exists(f):
            continue
        t = open(f, encoding='utf-8', errors='replace').read()
        # ** r2832a: paragraph-splitting flagged table rows and prose that merely NAME a row
        # in passing -- too crude.  *** Check HEADERS and list items, where a document presents
        # a row as live work; a passing mention in a sentence is not a status claim. ***
        # ** r2832b: checking the header LINE alone missed a mark written on the line
        # BELOW it, which is where a note about a section naturally goes.  *** Carry each
        # header together with the two lines following it. ***
        # ** r2832c: I tuned this window four times and it kept producing false positives
        # from list items and prose that merely NAME a row.  *** Anchor on HEADERS ONLY --
        # a section header is the one place a document unambiguously PRESENTS a row as its
        # subject, and it is checkable without judging prose. ***
        # ⌗ ** What this therefore does NOT catch: a struck row discussed as live inside
        # running prose. **  Stated rather than tuned around.
        _ls = t.split('\n')
        # ** r2832d: the +4-line window pulled a row's id in from BELOW an unrelated header
        # and reported it as that header's subject.  *** The row must be named in the HEADER
        # LINE itself; the following lines are searched only for the MARK. ***
        paras = []
        for i, l in enumerate(_ls):
            if re.match(r'\s*#+\s', l):
                paras.append((l, ' '.join(_ls[i:i+4])))
        for para in paras:
            head, window = para
            for pid in struck:
                if not re.search(rf'\b{re.escape(pid)}\b', head):
                    continue
                if re.search(r'STRUCK|struck|~~', window) or rev.get(pid, '@@') in window:
                    continue
                bad.append((d, pid, re.sub(r'\s+', ' ', head)[:64]))

    if bad:
        print()
        for d, pid, head in bad[:10]:
            print(f'    [FAIL] {d}: a paragraph names {pid} without its strike')
            print(f'           "{head}..."')
        print()
        print('    ⛭ ** A strike that reaches the register and not the documents reporting it is a')
        print('       row that no longer exists as open, still being read as open. ***')
        return 1

    print('  every struck row carries its strike where it is reported.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

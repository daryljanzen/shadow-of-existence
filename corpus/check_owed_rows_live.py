#!/usr/bin/env python3
"""check_owed_rows_live.py -- AN OPEN OWED ITEM'S ROW MUST STILL BE OPEN, AND ITS CITED RECEIPT MUST EXIST.

** WHY.  r2834. **  *** The per-document sweep is finished; every state document has been read.  ** What
remains ungated is not documents but RELATIONS between them. **  This gates two: `OWED`→register, and
row→receipt. ***

  ⇒ ** And the generic cross-document checker was tried and rejected. **  *** Testing the register's
      claims against every document that repeats them produced overwhelming false positives, because a
      document legitimately states counts historically -- "the register stood at 20 open when the colour
      arc closed" is true, and no generic checker can tell it from a stale current claim.  ** The pass
      that works is relation-specific: name the two documents and the one thing that must hold. ** ***

** WHAT THIS CHECKS. **
  * *** every OPEN item in `OWED.md` names a row that is still OPEN -- work owed on a closed question is
    work nobody should do; ***
  * *** every receipt filename cited in a register row exists under `receipts/`. ***

  ⌗ ** Both were clean when built ** -- *** stated so the next reader knows the gate was not built
    around a defect it then reported fixing. ***

    python3 corpus/check_owed_rows_live.py

Written r2834.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def main():
    print()
    print('  check_owed_rows_live -- is every owed item on a live row, and every cited receipt real?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    struck = set()
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if m and (m.group(1) or line.lstrip('|').lstrip().startswith('~~')):
            struck.add(m.group(2))

    bad = []

    # ⓵ OWED -> register
    owed = open(os.path.join(ROOT, 'OWED.md'), encoding='utf-8', errors='replace').read()
    n_owed = 0
    for line in owed.split('\n'):
        if not line.startswith('- [ ]'):
            continue
        n_owed += 1
        for pid in re.findall(r'\bPO-\d+[a-z]?\b', line):
            if pid in struck:
                bad.append(('OWED', f'an open item names {pid}, which is STRUCK'))

    # ⓶ rows -> receipts
    have = {os.path.basename(p) for p in
            glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)}
    have |= {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, 'scripts', '*.py'))}
    have |= {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, 'corpus', '*.py'))}
    n_cited = 0
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if not m:
            continue
        # ** r2834: this matched only citations written WITH the .py suffix, and the rows
        # cite receipts by STEM.  *** That is how `C41_a_tilde_on_a_settled_value_is_a_stale_
        # hedge` sat in `PO-10` for 36 revisions after r2798 renamed it to `C41b` -- the row
        # pointed at a receipt that does not exist and nothing looked. ***
        stems = {os.path.splitext(h)[0] for h in have}
        for r in sorted(set(re.findall(r'`([A-Za-z0-9_]+(?:\.py)?)`', line))):
            if not re.match(r'^[A-Z]\d+[a-z]?_|^L\d+_|^S\d+_|^B\d+_|^D\d+_|^M\d+_|\.py$', r):
                continue
            n_cited += 1
            if r in have or os.path.splitext(r)[0] in stems:
                continue
            if any(st.startswith(os.path.splitext(r)[0]) for st in stems):
                continue
            bad.append((m.group(2), f'cites `{r}`, which does not exist'))

    print(f'  {n_owed} open owed item(s); {n_cited} receipt citation(s) in rows')
    if bad:
        print()
        for who, why in bad[:12]:
            print(f'    [FAIL] {who}: {why}')
        print()
        print('    ⛭ ** Work owed on a closed question is work nobody should do, and a row citing')
        print('       a receipt that does not exist is a row whose evidence cannot be checked. ***')
        return 1

    print('  every owed item is on a live row; every cited receipt exists.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

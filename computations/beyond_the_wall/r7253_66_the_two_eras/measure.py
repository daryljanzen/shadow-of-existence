#!/usr/bin/env python3
"""`r7253` (node 66, the gate) -- THE CONTESTED CELL IS A MIXTURE OF TWO INSTRUMENTS, AND THE MIXTURE
IS TEMPORAL RATHER THAN BETWEEN SEATS.  THIS ALSO CORRECTS `r7251`'s OWN HEADLINE FIGURE.

** WHAT `r7251` SAID AND WHAT WAS WRONG WITH IT. **  *That revision reported `60` giving `REPAIR-OWED`
to `164` of `235` `PAPER`/`SENTENCE` keys and `cc66` giving it to `0` of `161`, and called the
disagreement complete.*  ** The `235` is reproducible and `cc66` reproduced it independently.  The
`161` is not `cc66`'s reading. **  *It is every verdicted key of that cell in `receipts/P15_CR_cosmology`
whatever revision stamped it: `17` carry `cc66`'s reading, `72` carry `60`'s own from `r7198`, `r7202`
and `r7206`, and the rest were stamped by this gate seat and by `70`.*  ⇒ *** So the figure attributed
to one seat a column that four seats wrote, including the seat it was being contrasted with. ***

** AND THE CORRECTED MEASUREMENT IS STRONGER THAN THE ONE IT REPLACES. **  *Bucketing the cell by the
revision that stamped each row:* *** the `357` `PAPER`/`SENTENCE` verdicts entered between `r7198`
and `r7247`, across at least seven revisions and four seats, carry `REPAIR-OWED` on `9` -- `2.5` per
cent -- while `60`'s single `r7252` reading gives it to `162` of `176`, `92` per cent.  A factor of
thirty-seven in one cell of one ledger. ***  ** So the old ground was not one seat's; it was the
column's, for fifty revisions. **

⇒ *Live, after `cc66`'s re-statement and `70`'s `L204` re-read: `344` rows still carry a
pre-settlement reading at `2.6` per cent `REPAIR-OWED`, against `235` re-read at `93.6` -- a thirty-six
fold gap in one cell of one ledger.*  ** That is what a mixture of two instruments looks like, and it
is a mixture across the settlement rather than across the seats. **

** WHY THE TWO CROSS-READS DISAGREED. **  *`cc66` read `40` of `60`'s keys and agreed on `33`;  `60`
read `40` of `cc66`'s and agreed on `6` of the `27` comparable.*  ⇒ *** `60` compared against `cc66`'s
rows as they stood BEFORE `cc66` re-stated them, so it measured the ERA gap;  `cc66` compared against
`60`'s post-settlement reading, so it measured the SEAT gap.  Against `cc66`'s re-stated rows the same
forty verdicts agree on `17` of `27`. ***  *Both seats measured correctly and neither measured the
same contrast.*

⌗ *A MEASUREMENT and not a gated receipt: it computes over committed files and asserts nothing about
any paper.  It exists so the figures written into `THE_REGISTER.md` at `r7253` -- and the correction to
`r7251`'s -- can be reproduced.*  **Run it from the repository root.**
"""
import collections
import csv
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))
BASE = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')
MIRROR = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                      'r7254_60_mirror_cross_read', 'VERDICTS.tsv')

# *The tree `r7251` measured, and the first revision whose readings are post-settlement.*
AT_R7251 = '3bf0ac52'
SETTLED_FROM = 7251
CELL = ('PAPER', 'SENTENCE')
P15 = 'receipts/P15_CR_cosmology/'
VERDICTS = {'DELIBERATE', 'REPAIR-OWED', 'ALT-OK', 'NOT-A-PIN', 'ENCODING-OK', 'EXTENDED',
            'MEANING-HELD'}
UNREAD = ('UNADJUDICATED', 'UNADJUDICATED-LIST', 'UNADJUDICATED-PINNED')
REV = re.compile(r'r(\d{4})')
HEAD_REV = re.compile(r'^(r\d+)(\+\S+?)?[:,]')


def git(*a):
    return subprocess.run(('git',) + a, cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def parse(txt):
    return [r for r in csv.reader(io.StringIO(txt), delimiter='\t')
            if r and not r[0].startswith('#')]


def newest_stamp(r):
    xs = [int(x) for x in REV.findall(r[6])] if len(r) >= 7 else []
    return max(xs) if xs else 0


def main():
    at = parse(git('show', f'{AT_R7251}:corpus/quote_pin_baseline.tsv'))
    live = parse(io.open(BASE, encoding='utf-8').read())

    # ---- (1) what r7251's 161 actually counted
    p15 = [r for r in at if r[0].startswith(P15) and r[5] in VERDICTS]
    cell = [r for r in p15 if (r[2], r[3]) == CELL]
    print(f'  r7251: {P15} carried {len(p15)} verdicted key(s), {len(cell)} in {CELL[0]}/{CELL[1]}')
    who = collections.Counter()
    for r in cell:
        m = HEAD_REV.match(r[6].strip())
        who[m.group(0).rstrip(':,') if m else 'unstamped'] += 1
    print('    the stamp at the head of each row\'s note:')
    for k, v in who.most_common(8):
        print(f'      {v:4d}  {k}')
    print('    ⇒ the 161 is the whole prefix\'s history, not one seat\'s reading.')

    # ---- (2) the two eras, on the tree r7251 measured
    allcell = [r for r in at if (r[2], r[3]) == CELL and r[5] in VERDICTS and len(r) >= 7]
    old = [r for r in allcell if 0 < newest_stamp(r) < 7252]
    print(f'\n  r7251, the cell by era:')
    new = [r for r in allcell if newest_stamp(r) >= 7252]
    for nm, g in (('stamped r7198-r7247', old), ("60's r7252 reading", new)):
        ro = sum(1 for r in g if r[5] == 'REPAIR-OWED')
        print(f'    {nm:22s}: n={len(g):4d}  REPAIR-OWED {ro:4d} '
              f'({100 * ro / max(len(g), 1):.1f}%)')
    # ⌗ *The first draft of this script asserted NOT ONE of the old era was `REPAIR-OWED`, which is
    #   what a bucketing by each row's HEAD stamp shows.  Bucketing by the NEWEST stamp anywhere in
    #   the note finds `9`.  The assertion is kept in the measured form, because a claim of zero that
    #   depends on which stamp is read is the kind of figure this row exists to catch.*
    old_ro = sum(1 for r in old if r[5] == 'REPAIR-OWED')
    new_ro = sum(1 for r in new if r[5] == 'REPAIR-OWED')
    assert old and old_ro * 10 < len(old), (old_ro, len(old))
    assert new and new_ro * 10 > len(new) * 8, (new_ro, len(new))
    print(f'    ⇒ {100 * old_ro / len(old):.1f} per cent against '
          f'{100 * new_ro / len(new):.1f}, a factor of '
          f'{(new_ro / len(new)) / (old_ro / len(old)):.0f} in one cell of one ledger.')

    # ---- (3) the live gap, after the re-statements
    lc = [r for r in live if (r[2], r[3]) == CELL and r[5] in VERDICTS]
    pre = [r for r in lc if newest_stamp(r) < SETTLED_FROM]
    post = [r for r in lc if newest_stamp(r) >= SETTLED_FROM]
    print(f'\n  live, the same cell:')
    for nm, g in (('still carrying a pre-settlement reading', pre),
                  ('re-read at r7251 or later', post)):
        ro = sum(1 for r in g if r[5] == 'REPAIR-OWED')
        print(f'    {nm}: n={len(g):4d}  REPAIR-OWED {ro:4d} '
              f'({100 * ro / max(len(g), 1):.1f}%)')
    print('    the re-statement owed, by prefix:')
    for k, v in collections.Counter(r[0].split('/')[1] for r in pre).most_common(6):
        print(f'      {k:32s} {v:4d}')

    # ---- (4) why the two cross-reads disagreed
    if os.path.exists(MIRROR):
        pre_m = {(r[0], r[1]): r[5] for r in at if len(r) >= 7}
        post_m = {(r[0], r[1]): r[5] for r in live if len(r) >= 7}
        a_pre = n_pre = a_post = n_post = 0
        for r in parse(io.open(MIRROR, encoding='utf-8').read()):
            rec, lit, v60 = r[1], r[2], r[6]
            try:
                k = (rec, json.dumps(json.loads(lit), ensure_ascii=False))
            except Exception:
                k = (rec, lit)
            if k not in post_m:
                k = next((kk for kk in post_m if kk[0] == rec and kk[1] == lit), None)
            if k is None:
                continue
            if pre_m.get(k) and pre_m[k] not in UNREAD:
                n_pre += 1; a_pre += (pre_m[k] == v60)
            if post_m.get(k) and post_m[k] not in UNREAD:
                n_post += 1; a_post += (post_m[k] == v60)
        print(f'\n  60\'s forty verdicts against the other seat\'s rows:')
        print(f'    as 60 saw them, PRE-settlement : {a_pre}/{n_pre} = '
              f'{100 * a_pre / max(n_pre, 1):.1f}% agree')
        print(f'    after that seat re-stated them : {a_post}/{n_post} = '
              f'{100 * a_post / max(n_post, 1):.1f}% agree')
        print('    ⇒ 60 measured the ERA gap; cc66 measured the SEAT gap.  Both are right about '
              'what they measured.')
    else:
        print(f'\n  ⌗ {MIRROR} not on this tree; the reconciliation is not computed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

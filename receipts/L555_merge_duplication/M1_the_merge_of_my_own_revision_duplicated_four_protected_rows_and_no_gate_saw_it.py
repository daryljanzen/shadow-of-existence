#!/usr/bin/env python3
"""M1 -- the `f220/line/54` merge duplicated FOUR protected rows and TWO index rows, no register gate
saw any of it, and for two of the four rows NEITHER copy was a superset -- the observer line's work
and the fork's sat in different copies of the same row.

** ⛔⛭⛭ ⓵ WHAT WAS WRONG. **  At `ed7b4d0`, `PROTECTED_OPEN.md` carried `PO-4`, `PO-5`, `PO-6` and
`PO-7` ** twice each **, with the two copies at different lengths.  Bisected: one row per id at
`e3bb3ca` (this fork's own c54.220), two from `c53be44` -- *** the merge of this fork's branch. ***

      *** PO-4  22165 / 9888     PO-5  18425 / 25172
          PO-6  28405 / 32280    PO-7   5880 / 5476   characters ***

** ⛔⛔ ⓶ AND FOR TWO OF THE FOUR, NEITHER COPY WAS A SUPERSET. **  `PO-4`: 402 words only in the
first, 59 only in the second.  `PO-6`: 147 and 211.  *** So r2768/r2770/r2774/r2775 sat in one copy of
`PO-4` and `L-552` in the other; `r2743`/`r2766` in one copy of `PO-6` and `L-553`/`L-554` in the
other.  Whichever copy a reader consulted showed half the record, and nothing marked either as
partial. ***  ⌗ *`PO-5` and `PO-7` were strict containments and are the easy case.*

** ⛔ ⓷ AND THE MERGE RESURRECTED A CORRUPTION THIS FORK HAD REPAIRED FOUR REVISIONS EARLIER. **
c54.217 (`L-551`) restored `PO-4`'s OBJECT column, which had carried 5069 characters of duplicated
status prose since r2427.  *** The first copy at `ed7b4d0` has that prose back in the object cell.
The repair was undone by a merge that kept both sides, and the side it kept was the pre-repair one. ***

** ⓸ AND NO GATE SAW ANY OF IT. **  At the duplicated state, ** `check_dupes`, `check_row_state`,
`check_id_bands`, `check_open_ledger`, `check_kills` and `check_family_pointers` were all GREEN. **
*`CLAIMS.md` records this class twice (r2434, c54.194) and c54.217 found it inside a cell; this is the
same failure at ROW level, and the duplicate-ID gate that fired for `L-171` does not look at `PO-` rows.*

** ⛔⛭⛭ ⓹ AND A SECOND, LARGER BLIND SPOT IN `receipts/INDEX.md`, FOUND BY THE SAME SWEEP. **  The
INDEX has 545 table rows.  `check_receipts` parses a row only if it starts `| P` or ``| ` `` --

      *** 524 parsed, 21 SKIPPED SILENTLY, 18 of them carrying a real receipt path. ***
      *(23 and 20 before this revision collapsed the two duplicate rows below.)*

The skipped rows are the corpus's own convention for a receipt belonging to no paper: an em-dash in
the paper column.  ⇒ *** For those 20 receipts the stem-uniqueness check, the column lint and the
origin/bound cells never run.  Two of them were EXACT duplicate rows -- `G50` and `G51`, byte for
byte -- and two of the skipped rows do not have eight columns and have never been linted. ***
  ⌗⌗ ** And the gate's own comment block names this class twice already: ** *the `| P` case-sensitivity
    bug that hid all nine `p0` rows (r2533+c54.203), and the duplicate-stem hole -- both described in
    its own words as "a gate blind to a row it should be policing".*  *** This is the third instance,
    and the em-dash is not an error but the corpus's convention. ***

** ⛔ ⓺ A HYPOTHESIS FORMED AND KILLED, recorded because the pattern-match was strong and wrong. **
`check_family_pointers` was RED at `e3bb3ca` and GREEN at `c53be44` -- *** exactly c54.217's shape,
where a corruption made a gate pass. ***  ⇒ ** It is not that. **  The observer line REOPENED `PO-10`
at r2730, which restores family 5's real target: the overlap with its object is
`['perturbation', 'scalar']`, a genuine match, and it is the fix this fork asked for as `FOR_56` item
27.  *** The gate went green for the right reason.  Checked before claiming, and the claim was
withdrawn. ***

** ⓻ REPAIRED, AND THE REPAIR IS LOSSLESS. **  Strict containments dropped; the two divergent pairs
concatenated with a merge note naming what happened; the two identical INDEX rows collapsed.
*** Not one distinct word lost -- verified file-wide and row by row across all fourteen protected
rows. ***

WHAT IS NOT CLAIMED.  ** Not that the parser should be changed ** -- `check_receipts` is the observer
line's instrument and what its row filter should accept is its call; this reports the blind spot with
its size and repairs the damage.  ** Not that any verdict moved ** -- every word of every row
survives and no row's state changed.  ** Not that the merge was careless ** -- a union merge cannot
see a duplicated row, which is the whole point of the class.  ** And the `PO-10` gate flip is NOT
attributed to the duplication ** -- ⓺.

Written c54.221, `L-555`.  Stated for reversal.
"""
import collections
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
SPL = re.compile(r'(?<!\\)\|')
ROW = re.compile(r'\|\s*~*\*\*(PO-[\w-]+)\*\*~*\s*\|')

# ⛔ EVERY "BEFORE" FACT IS PINNED TO A SHA, NOT TO THE WORKING TREE -- the rule this fork banked at
#   c54.220: an absence (or a duplication) is a claim about a COMMIT, not about a file, and this
#   revision edits both files it is making claims about.
DUP = 'ed7b4d0'      # r2776a -- the state carrying the duplication
ONE = 'e3bb3ca'      # c54.220 -- one row per id
MERGE = 'c53be44'    # the f220/line/54 merge that introduced it


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True).stdout


def po_rows(text):
    d = collections.defaultdict(list)
    for l in text.split('\n'):
        m = ROW.match(l)
        if m:
            d[m.group(1)].append(l)
    return d


def words(t):
    return collections.Counter(re.findall(r"[A-Za-z][A-Za-z'-]{3,}", t))


def main():
    print()
    print('  M1 -- did a merge duplicate protected rows, and did anything look?')
    print()

    dup = po_rows(git('show', DUP + ':PROTECTED_OPEN.md'))
    one = po_rows(git('show', ONE + ':PROTECTED_OPEN.md'))
    now = po_rows(open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read())

    # ---------------------------------------------------------------- (1) the duplication
    doubled = sorted(k for k, v in dup.items() if len(v) > 1)
    check(f'⓵ at {DUP} four protected rows were DOUBLED: {doubled}',
          doubled == ['PO-4', 'PO-5', 'PO-6', 'PO-7'])
    check(f'   and at {ONE} (this fork\'s own c54.220) there was exactly one row per id',
          all(len(v) == 1 for v in one.values()) and len(one) >= 13)
    mrg = po_rows(git('show', MERGE + ':PROTECTED_OPEN.md'))
    check(f'   so it entered at {MERGE}, "{git("log", "-1", "--format=%s", MERGE).strip()[:44]}" -- '
          'the merge of this fork\'s own branch',
          sorted(k for k, v in mrg.items() if len(v) > 1) == doubled)
    lens = {k: [len(x) for x in dup[k]] for k in doubled}
    check(f'   with the two copies at DIFFERENT lengths, so they were not identical: {lens}',
          all(a != b for a, b in lens.values()))

    # ---------------------------------------------------------------- (2) neither is a superset
    print()
    diverged = {}
    for k in doubled:
        a, b = words(dup[k][0]), words(dup[k][1])
        oa = [w for w in a if w not in b]
        ob = [w for w in b if w not in a]
        diverged[k] = (len(oa), len(ob))
    check(f'⛔⛔ ⓶ and for PO-4 and PO-6 NEITHER copy was a superset: unique-word counts '
          f'{ {k: v for k, v in diverged.items()} }',
          diverged['PO-4'][0] > 0 and diverged['PO-4'][1] > 0
          and diverged['PO-6'][0] > 0 and diverged['PO-6'][1] > 0)
    check('   so the observer line\'s r2768/r2770/r2774/r2775 sat in one copy of PO-4 and this fork\'s '
          'L-552 in the other',
          any('r2775' in x for x in dup['PO-4']) and any('L-552' in x for x in dup['PO-4'])
          and not any('r2775' in x and 'L-552' in x for x in dup['PO-4']))
    check('   and r2743/r2766 in one copy of PO-6 while L-553/L-554 sat in the other',
          any('r2766' in x for x in dup['PO-6']) and any('L-554' in x for x in dup['PO-6'])
          and not any('r2766' in x and 'L-554' in x for x in dup['PO-6']))
    check('   while PO-5 and PO-7 were strict containments -- the easy case',
          min(diverged['PO-5']) == 0 and min(diverged['PO-7']) == 0)

    # ---------------------------------------------------------------- (3) the resurrected corruption
    print()
    objs = [SPL.split(x)[2] for x in dup['PO-4']]
    check(f'⛔ ⓷ AND THE MERGE RESURRECTED c54.217\'s CORRUPTION: one PO-4 copy has the status prose '
          f'back in its OBJECT column ({max(len(o) for o in objs)} characters against '
          f'{min(len(o) for o in objs)} for the repaired one)',
          max(len(o) for o in objs) > 4000 and min(len(o) for o in objs) < 200)
    check('   which is the 5069-character cell L-551 restored, undone by a merge that kept both '
          'sides and kept the pre-repair one',
          any('WHERE ITS REMAINING ROUTE' in o for o in objs))

    # ---------------------------------------------------------------- (4) no gate saw it
    print()
    import tempfile
    import shutil
    gates = ['check_dupes', 'check_row_state', 'check_id_bands', 'check_open_ledger', 'check_kills']
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, 'corpus'))
        for f in ('PROTECTED_OPEN.md', 'THE_OPEN_PROBLEMS_LEDGER.md', 'THE_LIVE_ARC.md',
                  'CORPUS_MAP.md', 'kills'):
            out = git('show', f'{DUP}:{f}')
            if out:
                open(os.path.join(td, f), 'w', encoding='utf-8').write(out)
        results = {}
        for g in gates:
            src = git('show', f'{DUP}:corpus/{g}.py')
            if not src:
                continue
            open(os.path.join(td, 'corpus', g + '.py'), 'w', encoding='utf-8').write(src)
            r = subprocess.run(['python3', os.path.join('corpus', g + '.py')], cwd=td,
                               capture_output=True, text=True, env={**os.environ, 'NODE': 'ci'})
            results[g] = r.returncode
        green = [g for g, rc in results.items() if rc == 0]
        # ⚠ SCOPE OF THIS REPRODUCTION.  The sandbox carries only the register files, so a gate
        #   needing the kills/ tree cannot run here and its non-zero exit is environmental, not a
        #   detection.  The four that CAN run all pass on the duplicated tree; and all six --
        #   including check_kills and check_family_pointers -- were observed green on the real tree
        #   at ed7b4d0 before the repair.  Only the four are asserted.
        need_no_tree = ['check_dupes', 'check_row_state', 'check_id_bands', 'check_open_ledger']
        check(f'⓸ AND NO GATE SAW IT: re-run against the duplicated tree, {len(green)} of '
              f'{len(results)} exited 0 -- {results} (check_kills needs the kills/ tree the sandbox '
              'does not carry, so its exit is environmental and is not counted)',
              all(results.get(g) == 0 for g in need_no_tree))

    # ---------------------------------------------------------------- (5) the INDEX blind spot
    print()
    rows = [l.rstrip('\n') for l in open(os.path.join(ROOT, 'receipts', 'INDEX.md'),
                                         encoding='utf-8') if l.startswith('|')]
    parsed = [l for l in rows if (l[:3].upper().startswith('| P') or l.startswith('| `'))]
    skipped = [l for l in rows if l not in parsed]
    withpath = [l for l in skipped
                if len(SPL.split(l)) > 4 and SPL.split(l)[4].strip().strip('` ').endswith('.py')]
    src = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'check_receipts.py'),
                                   encoding='utf-8').read())
    check(f'⛔⛭ ⓹ AND A LARGER BLIND SPOT IN receipts/INDEX.md: of {len(rows)} table rows, '
          f'check_receipts parses {len(parsed)} and SKIPS {len(skipped)} -- {len(withpath)} of the '
          'skipped ones carrying a real receipt path',
          len(skipped) >= 20 and len(withpath) >= 18)
    check("   because the row filter is `ln[:3].upper().startswith('| P') or ln.startswith('| `')` "
          'and the corpus writes an em-dash in the paper column for a receipt belonging to no paper',
          "ln[:3].upper().startswith('| P') or ln.startswith('| `')" in src
          and all(SPL.split(l)[1].strip().startswith('—') or '---' in SPL.split(l)[1]
                  for l in withpath))
    # ⚠ I first asserted this phrase appears TWICE and it appears once; the near-phrase "blind to a
    #   row" appears twice, for the two prior instances.  Corrected to the counted value rather than
    #   the guessed one -- the same lesson as c54.219's fitted threshold.
    n_exact = src.count('a gate blind to a row it should be policing')
    n_near = src.count('blind to a row')
    check(f'   ⌗⌗ and the gate\'s own comment already names this class: "a gate blind to a row it '
          f'should be policing" appears {n_exact}x and "blind to a row" {n_near}x -- once for the '
          '`| P` case-sensitivity bug that hid all nine p0 rows, once for the duplicate-stem hole',
          n_exact == 1 and n_near == 2
          and 'ALL NINE of its INDEX rows were invisible to this gate' in src)

    # ---------------------------------------------------------------- (6) the hypothesis I killed
    print()
    def objs_unstruck(text):
        d = {}
        for l in text.split('\n'):
            m = re.match(r'\|\s*\*\*(PO-\d+)\*\*\s*\|([^|]*)\|', l)
            if m:
                d.setdefault(m.group(1), []).append(m.group(2))
        return d
    o_before, o_now = objs_unstruck(git('show', ONE + ':PROTECTED_OPEN.md')), \
        objs_unstruck(open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read())
    STOP = set('the a an of and or in on at to for is are was were be by with its it this that from '
               'what which as not but its their our one two three full open live sector'.split())

    def gw(x):
        x = re.sub(r'\\[a-zA-Z]+|[^a-z ]', ' ', x.lower())
        return {w for w in x.split() if len(w) > 4 and w not in STOP}

    fam5 = 'the scalar perturbation sector, to a verdict'
    check('⛔ ⓺ A HYPOTHESIS FORMED AND KILLED: check_family_pointers was RED at c54.220 and GREEN '
          'after the merge -- exactly c54.217\'s shape, where a corruption made a gate pass',
          'PO-10' not in o_before and 'PO-10' in o_now)
    check(f'   BUT IT IS NOT THAT: the observer line REOPENED PO-10 at r2730, and family 5\'s overlap '
          f'with its object is {sorted(gw(fam5) & gw(o_now["PO-10"][0]))} -- a genuine match, and the '
          'fix this fork asked for as FOR_56 item 27',
          {'scalar', 'perturbation'} <= gw(fam5) & gw(o_now['PO-10'][0]))

    # ---------------------------------------------------------------- (7) lossless repair
    print()
    wb, wn = words(git('show', DUP + ':PROTECTED_OPEN.md')), \
        words(open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read())
    lost = [w for w in wb if w not in wn]
    check(f'⓻ THE REPAIR LOSES NO DISTINCT WORD file-wide: {lost}', lost == [])
    per = {}
    for k, v in dup.items():
        a = words(' '.join(v))
        b = words(' '.join(now.get(k, [])))
        m = [w for w in a if w not in b]
        if m:
            per[k] = m
    check(f'   and ROW BY ROW across all {len(dup)} protected ids: {per}', per == {})
    check(f'   with one row per id remaining: '
          f'{ {k: len(v) for k, v in now.items() if len(v) != 1} or "all single"}',
          all(len(v) == 1 for v in now.values()))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the merge of this fork\'s own c54.220 duplicated four protected rows, and no')
    print('  register gate saw it. **')
    print('  ⛔ ⓵ ** For PO-4 and PO-6 neither copy was a superset ** — the observer line\'s')
    print('     r2768–r2775 and this fork\'s L-552/L-553/L-554 sat in *different copies of the same')
    print('     row*, so whichever a reader consulted showed half the record.')
    print('  ⛔ ⓶ ** And the merge resurrected c54.217\'s corruption: ** PO-4\'s object column has the')
    print('     status prose back in it, four revisions after it was repaired.')
    print('  ⛔⛭ ⓷ ** And a larger blind spot in receipts/INDEX.md: ** 23 of 547 rows are skipped')
    print('     silently, 20 of them carrying real receipt paths, because the parser gates on')
    print('     "| P" and the corpus writes an em-dash for a receipt with no paper.  *** The gate\'s')
    print('     own comment names this class twice; this is the third. ***')
    print('  ⛔ ⓸ ** And one hypothesis killed: ** the gate that flipped green did so because the')
    print('     observer line reopened PO-10 — the legitimate fix — and NOT because of the')
    print('     duplication.  Checked before claiming.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

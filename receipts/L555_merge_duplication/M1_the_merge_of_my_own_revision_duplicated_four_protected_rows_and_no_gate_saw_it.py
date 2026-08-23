#!/usr/bin/env python3
# RERUNNABLE: NO — POINT-IN-TIME
# *** This receipt verified a REPAIR at its own revision.  Its checks compare the tree
# against a state that later legitimate edits change, so it CANNOT be re-run green and
# a red result here is not a defect.  Added r2902; the corpus had no convention for
# this and three receipts were permanently red with nothing saying why. ***
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
INDEX has 546 table rows.  `check_receipts` parses a row only if it starts `| P` or ``| ` `` --

      *** 525 parsed, 21 SKIPPED SILENTLY, 18 of them carrying a real receipt path. ***
      *(547 / 524 / 23 / 20 at `ed7b4d0`, before this revision collapsed the two duplicate rows.)*
  ⚠ ** CORRECTED r3125 (`L-253`) BY PINNING THE MEASUREMENT THIS LINE REPORTS. **  *It read "545
    rows, 524 parsed".  524 is the PRE-repair parsed count: the row total was decremented for the
    collapsed rows and the parsed count beside it was carried over unchanged, so the pair printed
    here was never a state the file was in.*  ⇒ ** The load-bearing pair -- 21 skipped, 18 carrying
    a path -- was right, and both states are now MEASURED at their SHAs instead of transcribed. **

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
# ** r2901: this receipt's FAILING check is a POINT-IN-TIME. **
# *** same shape as R1 — a merge-repair verification, not an invariant. ***
# ⌗ The receipt is correct about what it did; the check cannot be re-run green.
import collections
import ast
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
# ⛭⛭ ADDED r3125 (`L-253`).  ** THE "AFTER" WAS NOT PINNED, AND THE "AFTER" IS THE REPAIR. **
#   *This receipt verifies a repair, and it read the repaired state from the WORKING TREE -- so
#   every later legitimate edit to a protected row moved the thing it was verifying.*
#   ⇒ *** The rule ⓹ already carries, applied to the two checks ⓹ did not touch: a finding is a
#       claim about a COMMIT.  The repair landed HERE, so the repair is read HERE, and the
#       PRESENT is asserted separately and MONOTONELY. ***
REPAIRED = 'e33c34c73d7037a04b85bd46fd5261c6c5d3f0b7'   # c54.221 -- this receipt's own revision


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
    now = po_rows(git('show', REPAIRED + ':PROTECTED_OPEN.md'))      # the repaired state, PINNED
    liv = po_rows(open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read())

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
    _BLIND = 'e33c34c'          # the tree this receipt was written against, before `L-556`
    # ⛭⛭ r3125 (`L-253`): ** THE THIRD SITE OF THE SAME DEFECT, IN THE FILE THAT DIAGNOSED IT. **
    #   *This block measured the blind spot in the LIVE `receipts/INDEX.md` while dating the finding to
    #   `_BLIND`.  The index has grown from 547 rows to 613 since, so the numbers the receipt PRINTS
    #   were never the numbers it FOUND -- and the verdict below still narrated the original pair.*
    #   ⇒ *** A pinned claim measured against a live file is not half-pinned; it is unpinned with a
    #       SHA written next to it. ***  The finding is read at `_BLIND`; the live index is reported
    #       beside it, unasserted, because what the deleted filter WOULD skip today is not a defect.
    rows = [l for l in git('show', f'{_BLIND}:receipts/INDEX.md').split('\n') if l.startswith('|')]
    _live_rows = [l.rstrip('\n') for l in open(os.path.join(ROOT, 'receipts', 'INDEX.md'),
                                               encoding='utf-8') if l.startswith('|')]
    parsed = [l for l in rows if (l[:3].upper().startswith('| P') or l.startswith('| `'))]
    skipped = [l for l in rows if l not in parsed]
    withpath = [l for l in skipped
                if len(SPL.split(l)) > 4 and SPL.split(l)[4].strip().strip('` ').endswith('.py')]
    # ** CORRECTED c54.222 (`L-556`): THIS BLOCK WAS A PRESENT-TENSE CLAIM ABOUT A FILE, AND THE FILE
    # ** WAS FIXED BECAUSE OF THIS RECEIPT. **  It read `corpus/check_receipts.py` from the WORKING TREE
    # ** and asserted the filter string was in it; c54.222 deleted the filter, and this check went red --
    # ** the sixth instance of "my own edit breaks my own receipt" (items 28/30/32/40's class).
    #   ⇒ *** The finding is about the tree AS IT WAS, so it is pinned to a SHA (c54.220's rule), and the
    #       repair is asserted SEPARATELY.  A receipt about a defect must survive the defect's repair. ***
    src = re.sub(r'\s+', ' ', subprocess.run(
        ['git', 'show', f'{_BLIND}:corpus/check_receipts.py'], cwd=ROOT,
        capture_output=True, text=True, errors='replace').stdout)
    live = open(os.path.join(ROOT, 'corpus', 'check_receipts.py'), encoding='utf-8').read()
    # ** AND BOTH STATES ARE NOW MEASURED, not one measured and one narrated. **  *The docstring gave
    #   the post-repair pair and the verdict gave the pre-repair pair, and neither said which was which.*
    _dup = [l for l in git('show', f'{DUP}:receipts/INDEX.md').split('\n') if l.startswith('|')]
    _dupsk = [l for l in _dup if not (l[:3].upper().startswith('| P') or l.startswith('| `'))]
    _dupwp = [l for l in _dupsk
              if len(SPL.split(l)) > 4 and SPL.split(l)[4].strip().strip('` ').endswith('.py')]
    check(f'⛔⛭ ⓹ AND A LARGER BLIND SPOT IN receipts/INDEX.md, MEASURED AT BOTH PINS: at {DUP} '
          f'{len(_dup)} table rows, {len(_dupsk)} SKIPPED SILENTLY, {len(_dupwp)} carrying a real '
          f'receipt path; at {_BLIND}, after this revision collapsed the two duplicate rows, '
          f'{len(rows)}/{len(skipped)}/{len(withpath)}.  *The live index now has {len(_live_rows)} '
          f'rows; reported, not asserted -- the filter is gone.*',
          (len(_dup), len(_dupsk), len(_dupwp)) == (547, 23, 20)
          and (len(rows), len(skipped), len(withpath)) == (546, 21, 18))
    # ⚠ ** AND ONE OF THIS RECEIPT'S OWN PRINTED NUMBERS WAS WRONG BY ONE, found by pinning it. **
    #   *The head said "545 table rows ... 524 parsed" for the post-repair state; the post-repair state
    #   is 546 and 525.  524 is the PRE-repair parsed count -- the row total was decremented for the two
    #   collapsed rows and the parsed count was carried over unchanged.*  ⇒ ** Corrected in the head.
    #   The load-bearing pair (21 skipped, 18 with a path) was right, and is now asserted. **
    # ** ⓹ᵇ AND THE ONE-ROW DIFFERENCE IS ACCOUNTED FOR, not asserted away. **  *Two byte-identical
    #   rows collapse (-2) and this revision registers itself (+1), which is why the total falls by
    #   ONE while the skipped count falls by TWO.  Both duplicated rows are `| — |` rows -- the very
    #   class the filter could not see, which is why nothing caught them.*
    _dupdup = [l for l, n in collections.Counter(_dup).items() if n > 1]
    check(f'   ⓹ᵇ and the arithmetic closes: exactly {len(_dupdup)} rows were byte-identical '
          f'duplicates at {DUP} (G50 `L-541` and G51 `L-545`, both `| — |` rows) and none is at '
          f'{_BLIND}; rows {len(_dup)} -> {len(rows)} is -2 for the collapse and +1 for this '
          "revision's own registration, and skipped falls by exactly the 2 that collapsed",
          len(_dupdup) == 2
          and all('L-541' in l or 'L-545' in l for l in _dupdup)
          and all(l.startswith('| —') for l in _dupdup)
          and not [l for l, n in collections.Counter(rows).items() if n > 1]
          and len(_dup) - len(rows) == 1 and len(_dupsk) - len(skipped) == 2
          and sum(1 for l in rows if 'L-555' in l) == 1)
    check(f"   because the row filter WAS `ln[:3].upper().startswith('| P') or ln.startswith('| `')` "
          f'at {_BLIND}, and the corpus writes an em-dash in the paper column for a receipt belonging '
          f'to no paper',
          "ln[:3].upper().startswith('| P') or ln.startswith('| `')" in src
          and all(SPL.split(l)[1].strip().startswith('—') or '---' in SPL.split(l)[1]
                  for l in withpath))
    check('   ⛭ AND IT IS GONE: c54.222 (`L-556`) deleted the predicate rather than patching it a fifth '
          'time, so check_receipts now reads corpus/index_rows.py and carries no copy of its own',
          'index_rows' in live
          and "ln[:3].upper().startswith('| P') or ln.startswith('| `')) : continue"
          not in re.sub(r'\s+', ' ', live)
          and not [n for n in ast.walk(ast.parse(live))
                   if isinstance(n, ast.Constant) and n.value in ('| P', '| `')])
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
        objs_unstruck(git('show', REPAIRED + ':PROTECTED_OPEN.md'))
    o_live = objs_unstruck(open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read())
    STOP = set('the a an of and or in on at to for is are was were be by with its it this that from '
               'what which as not but its their our one two three full open live sector'.split())

    def gw(x):
        x = re.sub(r'\\[a-zA-Z]+|[^a-z ]', ' ', x.lower())
        return {w for w in x.split() if len(w) > 4 and w not in STOP}

    fam5 = 'the scalar perturbation sector, to a verdict'
    check('⛔ ⓺ A HYPOTHESIS FORMED AND KILLED: check_family_pointers was RED at c54.220 and GREEN '
          'after the merge -- exactly c54.217\'s shape, where a corruption made a gate pass',
          'PO-10' not in o_before and 'PO-10' in o_now)
    # ⛭⛭ r3125 (`L-253`): ** AND THIS CHECK WAS THE ONE THAT BROKE, FOR THE REASON ⓹ ALREADY NAMED. **
    #   *`o_now` was the WORKING TREE.  `PO-10` was reopened at r2730, verified here, and later STRUCK --
    #   so the matcher (which reads only the unstruck spelling `| **PO-n** |`) stopped seeing it and the
    #   check went red.*  ⇒ *** The check punished the settlement it had asked for: a check that pins a
    #   LIVE register punishes the finding it defends.  The reopening is a fact about a COMMIT; the
    #   present is a separate, MONOTONE claim -- the row still exists, and its object still matches. ***
    _p10_live = liv.get('PO-10', [''])[0]
    check('   ⓺ᵇ AND THE PRESENT, ASSERTED SEPARATELY AND MONOTONELY: PO-10 still has exactly one row '
          f'live and it is now STRUCK ({"struck" if _p10_live.lstrip("| ").startswith("~~") else "OPEN"}) '
          '-- the reopening this check verified was carried to a verdict, which is the outcome it '
          'called for and NOT a break in it',
          len(liv.get('PO-10', [])) == 1 and 'PO-10' not in o_live)
    check('   ⓺ᶜ and the OBJECT survives the strike: family 5\'s overlap with PO-10\'s object cell is '
          'unchanged in the live file, so what ⓺ established about the gate flip is still readable',
          {'scalar', 'perturbation'} <= gw(fam5) & gw(SPL.split(_p10_live)[2] if _p10_live else ''))
    check(f'   BUT IT IS NOT THAT: the observer line REOPENED PO-10 at r2730, and family 5\'s overlap '
          f'with its object is {sorted(gw(fam5) & gw(o_now["PO-10"][0]))} -- a genuine match, and the '
          'fix this fork asked for as FOR_56 item 27',
          {'scalar', 'perturbation'} <= gw(fam5) & gw(o_now['PO-10'][0]))

    # ---------------------------------------------------------------- (7) lossless repair
    print()
    # ⛭ r3125 (`L-253`): pinned for the same reason as ⓺.  ** THE REPAIR IS LOSSLESS AGAINST THE
    #   STATE IT PRODUCED, and against nothing else. **  *Losslessness cannot be a live claim: a later
    #   revision is ENTITLED to delete a word, and asserting otherwise would make every subsequent
    #   editor answerable to this receipt.*
    wb, wn = words(git('show', DUP + ':PROTECTED_OPEN.md')), \
        words(git('show', REPAIRED + ':PROTECTED_OPEN.md'))
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
    # ** ⓻ᵇ THE LIVE CLAIM, AND IT IS THE ONLY ONE THAT CAN BE MADE LIVE. **  *Not "no word was lost"
    #   -- that is the repair's property, above.  What must hold forever is the DEFECT'S ABSENCE:
    #   no protected id has come back doubled, and none of the fourteen has gone missing.*
    _multi = {k: len(v) for k, v in liv.items() if len(v) != 1}
    check(f'⓻ᵇ AND THE DEFECT HAS NOT RECURRED, live: {len(liv)} protected ids, '
          f'{_multi or "one row each"}, and none of the {len(now)} present at the repair has been lost'
          f'{" -- missing: " + str(sorted(set(now) - set(liv))) if set(now) - set(liv) else ""}',
          not _multi and not (set(now) - set(liv)))

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
    print(f'  ⛔⛭ ⓷ ** And a larger blind spot in receipts/INDEX.md: ** {len(_dupsk)} of '
          f'{len(_dup)} rows were skipped silently at {DUP}')
    print(f'     ({len(skipped)} of {len(rows)} after this revision), {len(_dupwp)} of them carrying '
          'real receipt paths, because the')
    print('     parser gates on "| P" and the corpus writes an em-dash for a receipt with no paper.')
    print('     *** The gate\'s own comment names this class twice; this is the third. ***')
    print('  ⛔ ⓸ ** And one hypothesis killed: ** the gate that flipped green did so because the')
    print('     observer line reopened PO-10 — the legitimate fix — and NOT because of the')
    print('     duplication.  Checked before claiming.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

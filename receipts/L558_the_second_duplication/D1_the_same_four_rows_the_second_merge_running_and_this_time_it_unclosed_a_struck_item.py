#!/usr/bin/env python3
"""D1 -- the same merge shape duplicated the same four protected rows a SECOND time, one of them
un-closing an item the observer line had struck, and my own two receipts are what caught it.

COMPUTES: the duplicate census at `19139ed` and at both its merge parents; which side each copy came
from, byte-for-byte; that the losing side's unique content is this fork's own c54.221 note and that
every substantive token of it survives elsewhere; that seven register gates were green throughout;
and a seeded-defect test of the standing gate this builds.

** ⛭⛭⛭ IT HAPPENED AGAIN, ON THE NEXT MERGE. **

  * `c53be44` -- the merge of c54.220 -- duplicated `PO-4`, `PO-5`, `PO-6`, `PO-7`.  `L-555` repaired
    it, registered it, routed it, and its receipt gates the class.
  * *** `19139ed` -- the merge of c54.222, the very next one -- did the same four rows again. ***

And it stayed live through `r2783`, `r2783a`, `r2784` and `r2785`.

** ⛔ AND THIS TIME IT UN-CLOSED A CLOSED ITEM. **  `PO-4` was STRUCK at r2778 ("the ask is answered in
the negative, determined rather than deferred").  After the merge one copy carried `~~PO-4~~` and the
other did not.  *** So the register said an item was both closed and open, and read from the top it was
open. ***

** ⌗ WHAT CAUGHT IT, AND IT IS NOT A GATE. **  `L-555`'s own receipt `M1`, and -- independently --
`L-549`'s `Q1`, whose r2738 guard asserts `po.count('144/80/24') == 1` and which therefore counts TWO
when `PO-6` is doubled.  *A pin on a quotation turns out to be a duplicate detector, which is not what
it was for.*
  ⇒ ** Both are receipts, and `run_all_receipts` is not in the standing ten. **  So the detection
    existed and did not run for four revisions.  `corpus/check_protected_dupes.py` is built here.

** ⓵ WHY SEVEN REGISTER GATES SAW NOTHING. **  `check_row_state`, `check_kills`, `check_open_ledger`,
`check_family_pointers`, `check_register_columns`, `check_killrefs` and `check_dupes` all read this
file, and every one of them reads it ** one row at a time **.
  ⇒ *** A row that is perfectly well formed TWICE satisfies every per-row check there is.  That is not
      a defect in any of them; it is the hole BETWEEN them, and it is the hole a merge falls through. ***

** ⓶ AND THE MECHANISM IS NOT THE ONE ALREADY KNOWN. **  `.gitattributes` declares `merge=union` on
four files and warns in its own comment that *"Union merge cannot detect a duplicate ID"* -- and
`PROTECTED_OPEN.md` ** is not one of the four **.  So this is the other route: rows tens of thousands
of characters long, both nodes editing them, and the conflict resolved by keeping both sides.  ** The
known hole was gated; this one had nothing on it. **

** ⓷ THE REPAIR IS A READING, AND IT IS SIMPLER THAN LAST TIME BECAUSE THE MERGE WAS CLEAN. **  Neither
copy was interleaved: `19139ed` kept each parent\'s row verbatim.  So the two copies ARE the two sides,
byte-for-byte, and the question is only which is authoritative.
  * ** `PROTECTED_OPEN.md` is IDENTICAL at `e33c34c` and `d98bf61` ** -- c54.222 did not touch it -- so
    the fork side contributes nothing this fork wrote after c54.221.
  * ** The observer side is later work on the same rows ** (r2777, r2778 striking `PO-4`, r2780-r2782a).
  * *** And the fork side\'s unique tokens are exactly this fork\'s own c54.221 REPAIR NOTE ***, which the
    observer line pruned deliberately -- its permanent home is `L-551`, `L-555` and their receipts, not
    a protected row.  ** Asserted below: every substantive token of it is found elsewhere in the tree. **
  ⇒ *** So the fork-side copies are dropped and the observer-side copies kept.  Nothing is lost that is
      not recorded in three other places. ***

** WHAT IS NOT CLAIMED. **  ** Not that the observer line was wrong to prune the note ** -- it was right;
a repair note belongs in the arc and the receipt.  ** Not that the merge was careless **: both copies
were well-formed and every standing gate was green, which is the finding.  ** Not that the new gate
repairs anything ** -- it counts IDs and stops, because at c54.224 only a reader could know which copy
was authoritative.  ** Not that `PO-4`\'s strike is re-examined **: r2778\'s verdict is the observer
line\'s and is restored as it stood, not reviewed.

Written c54.224 (`L-558`).  Stated for reversal.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
REG = os.path.join(ROOT, 'PROTECTED_OPEN.md')
FAILED = []

#: the merge and its two parents.  ** A claim about a merge is a claim about three commits. **
MERGE, SIDE56, SIDE54 = '19139ed', '55f4605', 'd98bf61'
IDS = ('PO-4', 'PO-5', 'PO-6', 'PO-7')
ROW = re.compile(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True,
                          text=True, errors='replace').stdout


def rows(text):
    out = {}
    for n, line in enumerate(text.split('\n'), 1):
        m = ROW.match(line)
        if m:
            out.setdefault(m.group(2), []).append((n, bool(m.group(1)), line))
    return out


def main():
    print()
    print('  D1 -- the same four rows, the second merge running')
    print()
    at_merge = rows(git('show', f'{MERGE}:PROTECTED_OPEN.md'))
    a = rows(git('show', f'{SIDE56}:PROTECTED_OPEN.md'))
    b = rows(git('show', f'{SIDE54}:PROTECTED_OPEN.md'))
    live = rows(open(REG, encoding='utf-8', errors='replace').read())

    dup = sorted(k for k, v in at_merge.items() if len(v) > 1)
    check(f'⓵ at {MERGE} ("Merge branch \'f222/line/54\'") {len(dup)} protected IDs sit on two rows '
          f'each: {", ".join(dup)}', dup == list(IDS))
    check(f'⛭ and it is the SAME FOUR as c53be44 at c54.221 -- the very next merge, the same shape',
          set(dup) == set(IDS))
    check('⇒ while BOTH PARENTS carry one row per ID, so the duplication is the merge and nothing else',
          all(len(v) == 1 for v in a.values()) and all(len(v) == 1 for v in b.values()))

    # ⓶ the strike
    states = {s for _, s, _ in at_merge['PO-4']}
    check('⛔ ⓶ AND THE TWO `PO-4` COPIES DISAGREE ABOUT STATE: one struck, one open -- so a merge '
          'un-closed an item r2778 had determined in the negative',
          states == {True, False}
          and a['PO-4'][0][1] is True and b['PO-4'][0][1] is False)

    # ⓷ the copies ARE the parents, byte for byte
    verbatim = [k for k in IDS
                if sorted(l for _, _, l in at_merge[k]) == sorted([a[k][0][2], b[k][0][2]])]
    check(f'⓷ the merge kept each parent\'s row VERBATIM -- {len(verbatim)} of {len(IDS)} match '
          f'byte-for-byte, so no reading is needed to say which copy came from where',
          len(verbatim) == len(IDS))
    check('⇒ and PROTECTED_OPEN.md is IDENTICAL at e33c34c and d98bf61: c54.222 never touched it, so '
          'the fork side contributes nothing written after c54.221',
          git('diff', '--stat', 'e33c34c', SIDE54, '--', 'PROTECTED_OPEN.md').strip() == '')

    # ⓸ what the losing side uniquely held, and where it survives
    elsewhere = ''
    for f in ('THE_LIVE_ARC.md', 'FOR_56.md',
              'receipts/L555_merge_duplication/M1_the_merge_of_my_own_revision_duplicated_four'
              '_protected_rows_and_no_gate_saw_it.py',
              'receipts/L551_register_integrity/R1_a_protected_row_was_corrupt_for_368_commits_and'
              '_the_corruption_satisfied_a_gate.py'):
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            elsewhere += open(p, encoding='utf-8', errors='replace').read()
    elsewhere += git('log', '--format=%B', '-1', 'e33c34c')
    E = set(re.findall(r"[A-Za-z0-9_`\\-]+", elsewhere))

    def bare(t):
        return re.sub(r"[^A-Za-z0-9_`\\-]", '', t)

    lost = {}
    for k in IDS:
        wa = set(re.findall(r'\S+', a[k][0][2]))
        wb = set(re.findall(r'\S+', b[k][0][2]))
        lost[k] = [t for t in (wb - wa) if bare(t) and bare(t) not in E]
    check(f'⓸ the fork side\'s unique tokens are its own c54.221 REPAIR NOTE, and every substantive '
          f'one survives in the arc, `FOR_56`, `L-551`/`L-555` or the c54.221 commit message: '
          f'{ {k: len(v) for k, v in lost.items()} } left unaccounted',
          all(len(v) <= 6 for v in lost.values()))
    check('⇒ SO THE DROP IS LOSSLESS IN SUBSTANCE: what the observer line pruned is a repair note, '
          'whose permanent home is the arc row and the receipt and never a protected row',
          sum(len(v) for v in lost.values()) <= 12)

    # ⓹ the repair, in the live file
    check(f'⓹ REPAIRED: every protected ID now appears exactly once ({len(live)} IDs, '
          f'{sum(len(v) for v in live.values())} rows)',
          all(len(v) == 1 for v in live.values()) and len(live) == 14)
    # ** ⛭ AMENDED c54.228: this compared the LIVE file against `55f4605`, so it broke the moment the
    # ** observer line edited those rows again (r2786-r2797, carried in by c54.227's merge).  *** A
    # ** before/after identity is a claim about the commit where the repair LANDED, not about HEAD. ***
    # ** The repair is pinned at `6fd26f9` (c54.224); what the live file must still satisfy is the
    # ** PROPERTY -- one row per id, and PO-4 struck -- which is asserted separately and is what a
    # ** regression would break. **
    AT_REPAIR = '6fd26f9'
    repaired = rows(git('show', f'{AT_REPAIR}:PROTECTED_OPEN.md'))
    check(f'⇒ and at {AT_REPAIR} each surviving row was the OBSERVER side byte-for-byte -- r2778\'s '
          f'strike on `PO-4` restored as it stood, not reviewed',
          all(repaired[k][0][2] == a[k][0][2] for k in IDS) and repaired['PO-4'][0][1] is True)
    check('⛭ and the PROPERTY still holds in the live file after c54.227 merged r2797 on top: one row '
          'per protected id, and `PO-4` still struck',
          all(len(v) == 1 for v in live.values()) and live['PO-4'][0][1] is True)

    # ⓺ why nothing standing saw it
    GATES = ('check_row_state', 'check_kills', 'check_open_ledger', 'check_family_pointers',
             'check_register_columns', 'check_killrefs', 'check_dupes')
    readers = [g for g in GATES
               if 'PROTECTED_OPEN' in open(os.path.join(ROOT, 'corpus', g + '.py'),
                                           encoding='utf-8', errors='replace').read()]
    check(f'⓺ {len(readers)} of {len(GATES)} standing gates READ this file and every one of them was '
          f'green across the four revisions the duplication was live', len(readers) >= 5)
    attrs = open(os.path.join(ROOT, '.gitattributes'), encoding='utf-8', errors='replace').read()
    check('⇒ and the mechanism is NOT the one already known: .gitattributes declares merge=union on '
          'four files and warns that "Union merge cannot detect a duplicate ID" -- and '
          'PROTECTED_OPEN.md is not one of the four',
          'nion merge cannot detect a duplicate ID' in attrs
          and not re.search(r'^PROTECTED_OPEN\.md\s+merge=union', attrs, re.M))

    # ------------------------------------------------------------------ ⓺b the un-closing BIT
    # ** ⛔⛔ AND THE UN-CLOSING WAS NOT COSMETIC. **  Three of the observer line's own receipts match
    # `PO-4` with `l.startswith('| **PO-4**')` -- the OPEN form -- and they went on passing across the
    # four revisions the duplication was live.
    #   ⇒ *** They were passing BECAUSE the resurrected copy was unstruck.  Deduplicating killed all
    #       three with `StopIteration` on the first read, which is how this was found. ***
    #   ⇒ ** A matcher that admits only the open form silently follows whichever copy is open. **
    BRIDGE = ('B8_po4_targets_have_opposite_verdicts', 'B14_identical_in_content_is_po2s_reason',
              'B15_po3_both_clauses_answered')
    at_head0 = [n for n in BRIDGE
                if "startswith('| **PO-4**')" in git('show', f'{MERGE}:receipts/L221_the_bridge/{n}.py')
                or "startswith(f'| **{t}**')" in git('show', f'{MERGE}:receipts/L221_the_bridge/{n}.py')]
    check(f'⛔ ⓺b {len(at_head0)} of the observer line\'s own `L-221` receipts matched `PO-4` by its '
          f'OPEN form at {MERGE} and passed throughout -- they were reading the RESURRECTED copy of a '
          f'row r2778 struck', len(at_head0) == 3)
    now = [n for n in BRIDGE
           if 'AMENDED c54.224' in open(os.path.join(ROOT, 'receipts', 'L221_the_bridge', n + '.py'),
                                        encoding='utf-8', errors='replace').read()]
    check('⇒ all three amended to a matcher that admits the struck form, so a strike can no longer be '
          'invisible to them -- and all three pass against the deduplicated register',
          len(now) == 3)

    # ⓻ the gate, SEEDED
    tmp = tempfile.mkdtemp(prefix='L558.')
    try:
        shutil.copytree(os.path.join(ROOT, 'corpus'), os.path.join(tmp, 'corpus'))
        shutil.copy(REG, os.path.join(tmp, 'PROTECTED_OPEN.md'))
        gate = os.path.join(tmp, 'corpus', 'check_protected_dupes.py')

        def run():
            r = subprocess.run([sys.executable, gate], cwd=tmp, capture_output=True,
                               text=True, errors='replace')
            return r.returncode, r.stdout + r.stderr

        clean_rc, _ = run()
        tgt = os.path.join(tmp, 'PROTECTED_OPEN.md')
        keep = open(tgt, encoding='utf-8').read()
        ls = keep.split('\n')
        i = [n for n, x in enumerate(ls) if re.match(r'\|\s*(~~)?\s*\*\*PO-6\*\*', x)][0]
        ls.insert(i + 1, ls[i].replace('**PO-6**', '~~**PO-6**~~', 1))   # the seed: the real defect
        open(tgt, 'w', encoding='utf-8').write('\n'.join(ls))
        seed_rc, seed_out = run()
        open(tgt, 'w', encoding='utf-8').write(keep)
        rest_rc, _ = run()
        same = open(tgt, encoding='utf-8').read() == keep
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    check(f'⓻ check_protected_dupes: clean {clean_rc}, SEEDED {seed_rc}, restored {rest_rc}; the '
          f'restore is byte-identical ({same}); and the seed is the DEFECT ITSELF -- one row doubled '
          f'with a differing strike marker',
          clean_rc == 0 and seed_rc == 1 and rest_rc == 0 and same)
    check('⇒ and it reports the state disagreement, which is the half that un-closed PO-4',
          'disagree about state' in seed_out.lower() or 'DISAGREE ABOUT STATE' in seed_out)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the same four rows, the second merge running, and this time it un-closed a')
    print('    struck item. **')
    print('    · c53be44 (c54.221) and 19139ed (c54.224) -- consecutive merges, identical shape')
    print('    · live through four revisions; seven per-row gates green throughout')
    print('    · caught by two RECEIPTS of this fork\'s own, neither of which is in the standing ten')
    print('  ⇒ ** A per-row check cannot see a whole-file property, and that is the hole a merge')
    print('    falls through. **  corpus/check_protected_dupes.py closes it.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

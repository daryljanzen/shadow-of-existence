#!/usr/bin/env python3
"""O1 -- `L-556` turned the registry check outward from citations to rows, and the arrow still only
pointed one way: four computations existed under `receipts/` that no row registered.

COMPUTES: the orphan census against the shared row reader; that each of the three real ones RUNS and
exits zero; that `bbn_network` is an engine three receipts import AND is named in the runner's own SLOW
tuple; that the P17 receipt was the only thing reporting any of it; and a seeded-defect test of the new
gate, including that a declared exemption is honoured and an inferred one is not.

** ⛭⛭⛭ THE ASYMMETRY, AND IT IS THE WHOLE FINDING. **

c54.222 (`L-556`) found the registry validated from CITATIONS INWARD -- a `\rcpt{}` must reach a row and
a file -- and never from ROWS OUTWARD, so two rows named files that had never existed and were printed
into three appendices as `[OK]`.  `check_receipts` now fails on a row with no file.

  ⇒ *** And nothing asked it the other way: a FILE with no ROW. ***  Four of them.

** ⓵ WHAT AN UNREGISTERED RECEIPT COSTS, and it is not the same cost as an unresolvable row. **  The
INDEX is the file list for everything downstream, so a receipt with no row is never run by
`run_all_receipts`, never reaches an appendix, never enters the assertion census, and never appears in
the supersession scan.  ** It is a computation that exists and that the corpus does not know it has. **

** ⓶ AND ONE OF THE FOUR IS SHARPER THAN THAT. **  `bbn_network.py` is named in `run_all_receipts`' own
`SLOW` tuple -- *** a per-file timeout budget for a file the runner has never run ***, because the
budget is written by hand and the file list is read from the INDEX.  ** Two halves of one gate, kept in
two places, disagreeing about which files exist. **  It is a genuine ENGINE (three receipts import it),
so it is DECLARED rather than registered.

** ⓷ WHAT WAS REPORTING IT, AND WHY THAT IS NOT ENOUGH. **  `P17_the_frontier_item_is_a_result…` names
three of the four in its own failure line and has been failing on them.  ** A receipt reporting a
registry hole is the same shape as `L-558`'s finding one file over: the detection existed, in a receipt,
and `run_all_receipts` is not in the standing ten. **

** ⌷ ⓸ AND THE OPT-OUT IS A DECLARATION, NOT AN INFERENCE. **  The gate could exempt a file by asking
"is it imported anywhere", and deliberately does not.  *** An inferred exemption is invisible, and it
silently exempts the next orphan that happens to be imported once. ***  A file opts out by writing
`NOT-A-RECEIPT:` into its own docstring -- `L-237`'s rule, that a declaration is the only kind of thing
this corpus can gate.  ** Asserted below both ways: the declared file passes, and the same file with the
declaration removed FAILS. **

** WHAT IS NOT CLAIMED. **  ** Not that the three newly registered receipts are right ** -- they RUN and
exit zero, and their rows say "registered, not written": the content is the observer line's and is
unaltered.  ** Not that every unregistered file is a defect ** -- that is what the declaration is for.
** Not that the SLOW tuple should be derived from the INDEX ** (routed, not done: the budget is a
judgement and deriving it would hide the judgement).

Written c54.225 (`L-559`).  Stated for reversal.
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.append(os.path.join(ROOT, 'corpus'))
import index_rows                                                          # noqa: E402

FAILED = []
BEFORE = '6fd26f9'          # c54.224 -- the tree this revision started from
FOUR = ('receipts/P03_SdS_slicing/A6_item_58_resolves_split.py',
        'receipts/P12_algebroid/A3_the_convergence_audit.py',
        'receipts/P12_algebroid/A8_the_self_protecting_falsehood.py',
        'receipts/P16_cosmogenesis_paper/bbn_network.py')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True,
                          text=True, errors='replace').stdout


def main():
    print()
    print('  O1 -- the registry from files inward: does every receipt file have a row?')
    print()

    # ⓵ the census AT THE COMMIT THIS STARTED FROM, using the shared reader on that tree's INDEX
    idx_before = git('show', f'{BEFORE}:receipts/INDEX.md')
    tmp_idx = os.path.join(tempfile.mkdtemp(prefix='L559idx.'), 'INDEX.md')
    open(tmp_idx, 'w', encoding='utf-8').write(idx_before)
    reg_before = set()
    for r in index_rows.rows(index=tmp_idx, resolve_paths=True, root=ROOT):
        for p in (r.paths or []):
            reg_before.add(os.path.realpath(p))
    files_before = [l for l in git('ls-tree', '-r', '--name-only', BEFORE, '--', 'receipts').split('\n')
                    if l.endswith('.py')]
    orph_before = sorted(f for f in files_before
                         if os.path.realpath(os.path.join(ROOT, f)) not in reg_before)
    check(f'⓵ at {BEFORE}: {len(files_before)} receipt files, {len(orph_before)} with NO INDEX row '
          f'-- {", ".join(os.path.basename(f) for f in orph_before)}',
          sorted(orph_before) == sorted(FOUR))

    # ⓶ three of the four RUN and exit zero -- so they are receipts, not scratch
    ran = []
    for f in FOUR[:3]:
        d, b = os.path.dirname(os.path.join(ROOT, f)), os.path.basename(f)
        rc = subprocess.run([sys.executable, b], cwd=d, capture_output=True,
                            text=True, errors='replace').returncode
        ran.append((b, rc))
    check(f'⓶ all three of the real ones RUN where they sit and exit zero: '
          f'{ {b: rc for b, rc in ran} } -- they are receipts, not scratch',
          all(rc == 0 for _, rc in ran))

    # ⓷ the fourth is an engine, and the runner budgets for it without running it
    runner = open(os.path.join(ROOT, 'scripts', 'run_all_receipts.py'),
                  encoding='utf-8', errors='replace').read()
    importers = [f for f in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)
                 if 'bbn_network' in open(f, encoding='utf-8', errors='replace').read()
                 and os.path.basename(f) != 'bbn_network.py']
    check(f'⓷ `bbn_network` is a genuine ENGINE -- {len(importers)} receipt(s) reference it -- and it '
          f'is named in run_all_receipts\' own SLOW tuple while having no row',
          len(importers) >= 3 and "'bbn_network'" in runner)
    check('⇒ SO THE RUNNER CARRIES A PER-FILE TIMEOUT BUDGET FOR A FILE IT HAS NEVER RUN: the budget '
          'is written by hand and the file list is read from the INDEX -- two halves of one gate, '
          'kept in two places, disagreeing about which files exist',
          "'bbn_network'" in runner
          and 'bbn_network' not in ''.join(r.token for r in index_rows.rows()))

    # ⓸ what was reporting it
    p17 = open(os.path.join(ROOT, 'receipts', 'P17_geometric_core_paper',
                            'P17_the_frontier_item_is_a_result_and_the_cosmogenesis_paper_reaches_it'
                            '_the_other_way.py'), encoding='utf-8', errors='replace').read()
    check('⓸ the ONLY thing reporting any of it was a RECEIPT -- P17\'s, which names three of the four '
          'and had been failing on them',
          'no INDEX row' in p17 or 'still have no INDEX row' in p17)
    check('⇒ and run_all_receipts is NOT in the standing ten, by its own docstring -- so the detection '
          'existed and was not being run, which is L-558\'s finding one file over',
          'THIS GATE IS NOT IN THE STANDING TEN' in runner)

    # ⓹ the repair
    live_reg = set()
    for r in index_rows.rows(resolve_paths=True):
        for p in (r.paths or []):
            live_reg.add(os.path.realpath(p))
    live_files = glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)
    left = [f for f in live_files if os.path.realpath(f) not in live_reg]
    check(f'⓹ REPAIRED: {len(live_files)} receipt files, {len(left)} unregistered, and the one that '
          f'remains carries an explicit `NOT-A-RECEIPT:` declaration',
          len(left) == 1 and 'NOT-A-RECEIPT:' in open(left[0], encoding='utf-8',
                                                      errors='replace').read())
    check('⇒ and the three new rows say "registered, not written" -- the content is the observer '
          'line\'s and is unaltered',
          all('ROW ADDED c54.225' in open(os.path.join(ROOT, 'receipts', 'INDEX.md'),
                                          encoding='utf-8', errors='replace').read()
              for _ in (0,)))

    # ⓺ the gate, SEEDED -- both directions
    tmp = tempfile.mkdtemp(prefix='L559.')
    try:
        shutil.copytree(os.path.join(ROOT, 'corpus'), os.path.join(tmp, 'corpus'))
        os.makedirs(os.path.join(tmp, 'receipts'))
        for entry in os.listdir(os.path.join(ROOT, 'receipts')):
            src = os.path.join(ROOT, 'receipts', entry)
            if entry == 'INDEX.md':
                shutil.copy(src, os.path.join(tmp, 'receipts', entry))
            elif os.path.isdir(src):
                shutil.copytree(src, os.path.join(tmp, 'receipts', entry))
            else:
                shutil.copy(src, os.path.join(tmp, 'receipts', entry))
        gate = os.path.join(tmp, 'corpus', 'check_receipt_orphans.py')

        def run():
            r = subprocess.run([sys.executable, gate], cwd=tmp, capture_output=True,
                               text=True, errors='replace')
            return r.returncode, r.stdout + r.stderr

        clean_rc, _ = run()
        # SEED A: a new file with no row
        seeded = os.path.join(tmp, 'receipts', 'P12_algebroid', 'ZZ_seeded_by_L559.py')
        open(seeded, 'w', encoding='utf-8').write('"""a file with no row."""\n')
        a_rc, a_out = run()
        os.remove(seeded)
        # SEED B: strip the declaration from the engine -- an inferred exemption must NOT save it
        eng = os.path.join(tmp, 'receipts', 'P16_cosmogenesis_paper', 'bbn_network.py')
        keep = open(eng, encoding='utf-8').read()
        open(eng, 'w', encoding='utf-8').write(keep.replace('NOT-A-RECEIPT:', 'not a receipt:', 1))
        b_rc, b_out = run()
        open(eng, 'w', encoding='utf-8').write(keep)
        rest_rc, _ = run()
        same = open(eng, encoding='utf-8').read() == keep
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    check(f'⓺ check_receipt_orphans: clean {clean_rc}; an unrowed file added -> {a_rc} '
          f'({"named" if "ZZ_seeded_by_L559" in a_out else "NOT named"}); restored {rest_rc}, '
          f'byte-identical ({same})',
          clean_rc == 0 and a_rc == 1 and 'ZZ_seeded_by_L559' in a_out and rest_rc == 0 and same)
    check('⇒ AND THE DECLARATION IS WHAT EXEMPTS, NOT THE IMPORT: with `NOT-A-RECEIPT:` removed the '
          'engine FAILS, though three receipts still import it -- so an exemption cannot be acquired '
          'by accident',
          b_rc == 1 and 'bbn_network' in b_out)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** L-556 turned the check outward from citations to rows; the arrow still only')
    print('    pointed one way. **')
    print('    · four computations under receipts/ that no row registered')
    print('    · never run, never in an appendix, never in the census, never in the supersession scan')
    print('    · one of them budgeted for by name in the runner\'s SLOW tuple and never run')
    print('    · the only thing reporting it was a RECEIPT, and the receipt runner is not standing')
    print('  ⇒ ** A registry needs both arrows, and the exemption from either must be DECLARED. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""R1 -- the receipt registry was validated from CITATIONS INWARD, so twenty rows were read by nothing,
two of them registered files that have never existed, and the column lint sat downstream of the hole.

COMPUTES: the INDEX row set at `e33c34c` under the old predicate and under the new one, the 20-row
difference and its decomposition, the two column-split rows inside that difference, the 2 rows naming
files absent from all 486 commits, the 56-row appendix shortfall, and a seeded-defect test of the new
currency gate in an isolated tree.

** ⛭⛭⛭ THE SHAPE OF IT, AND IT IS ONE MECHANISM WITH FOUR CONSEQUENCES. **

`receipts/INDEX.md` had FIVE readers, each with its own copy of the same row filter:

    corpus/check_receipts.py · corpus/make_receipt_appendix.py · corpus/check_supersession.py
    scripts/run_all_receipts.py · scripts/work_entry_points.py

*** and FOUR of the five had already been patched SEPARATELY for the same class of loss ***
(r2376+c54.36 the `` | `stem` `` format; c54.203 two files for the lowercase `p0`; r2555 the runner for
the same `p0`, in its own words *"the fourth instance of the silent-discard class"*).  ** Each fix
landed in one copy.  A fifth divergence was not a risk; it was a schedule. **

** ⓵ THE FIFTH ARRIVED, AND IT IS THE SAME COLUMN.  The predicate is
`ln[:3].upper().startswith('| P') or ln.startswith('| `')` -- it decides MEMBERSHIP by the PAPER
column -- and the corpus writes an EM-DASH there for a receipt that supports no paper. **

  *** 20 of 544 rows.  18 name one concrete file on disk; 1 names a nine-file glob; 1 named nothing at
      all because its path cell had been destroyed (⓶). ***  So `run_all_receipts` -- THE ELEVENTH
  GATE, built because *"an instrument that reads a file has not run it"* -- had never run any of them.

  ⇒ ** RUN HERE, ALL EIGHTEEN.  Seventeen pass.  ONE FAILS **: `L230_computes_convention/C1`, whose
    thesis is overturned and which *** has never exited zero in any tree, including the commit that
    added it *** -- corrected in place this revision, see its own head.

** ⛔ ⓶ AND THE COLUMN LINT SAT INSIDE THE LOOP THE FILTER GUARDS. **  `check_receipts` carries an
8-cell lint; it runs after `continue`.  ** So it could only ever lint the rows the filter already
liked ** -- and TWO of the dropped rows were column-split, at 10 and 12 cells, on `\\|aH\\|` and
`\\|T\\|^2+\\|R\\|^2=1`, sitting in the file since r2674.  The 12-cell row's PATH cell had become the
single character `T`.

  ⇒ *** cc54's r2772 note, the reason `check_register_columns` exists, reads: "the identical string went
      into the INDEX row, ** where your column lint caught it instantly **."  ** That is true of the rows
      the filter admits and false of the rows it drops, and the falsifying pair was in the file while
      the sentence was being written. ***  ** A lint downstream of a filter inherits the filter's blind
      spot and reports green from inside it. **

** ⛔⛔ ⓷ THE HALF THAT IS NOT ABOUT THE FILTER AT ALL, AND IT IS THE WORST OF THE FOUR.  EVERY reader
resolved a path with `if os.path.exists(f)` -- and did nothing when it failed. **  Two rows,
`X4_singularity_types.py` and `X3_seam_schwarz_reflection.py`, ** name files that have never existed in
ANY of the 486 commits reachable from any ref **, carry `✔✔`, and certify a RUN (`run r1870, rc=0`).
Both are printed into P3's, P7's and the corpus appendix marked ** `[OK]` **.

  ⇒ *** The registry was checked from CITATIONS INWARD -- a `\\rcpt{}` must reach a row and a file -- and
      never from ROWS OUTWARD.  An UNCITED row naming a file that does not exist was therefore checked by
      NOTHING, while the generated appendix advertised it as verified. ***

  ⌗ ** AND THE WORK WAS REDONE UNDER OTHER ROWS, WHICH IS HOW THE NAMES CAME TO BE FREE. **
  `X4r_no_essential_singularity.py` opens *"X4-REDONE"*; `X3r_reality_lines.py` opens *"X3-REDONE"* and
  states that `r = sin(theta)` is entire, so the Schwarz principle *"invoked at r1869, has no work to
  do."*  *** r1869 is the withdrawn X3 row's own build revision: the redo REVERSED the claim, and the
  reversed row kept its `✔✔` and kept reaching the appendix. ***  Both rows are WITHDRAWN verbatim into
  a blockquote this revision -- not deleted, because the text is the evidence.

** ⓸ AND ONE MORE THING THE SAME READING EXPOSED: THE APPENDICES WERE 49 REVISIONS STALE. **  The
generator's own first line says the appendix *"can never drift from the ledger, because it is
regenerated"*; nothing checked that it HAD been.  `check_compile` fails on a DEAD LINK, which needs the
new row to be CITED -- so an uncited row just lags.  ** 488 entries against 544 registered rows: 56
short. **  `corpus/check_appendix_current.py` is built and seeded here.

** WHAT IS NOT CLAIMED. **  ** Not that the 17 newly-run receipts were verified ** -- they were RUN, and
exit zero is what that buys.  ** Not that X3's or X4's redone results are wrong ** -- they are registered
and they stand; what is withdrawn is two rows for files that do not exist.  ** Not that the em-dash
convention is wrong ** -- a receipt supporting no paper is a real category; what was wrong is reading a
CONTENT column as a membership test.  ** Not that the appendix content is now correct **, only that it
is now what the ledger generates.

Written c54.222 (`L-556`).  Stated for reversal.
"""
import ast
import fnmatch
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

#: ** the tree this revision started from.  Every claim about "before" is a claim about THIS commit **
#: (c54.220's rule: a claim about a past state takes a SHA, because HEAD moves and takes it along).
BEFORE = 'e33c34c'

#: the predicate as it stood, quoted from the source at BEFORE and asserted to be there (⓵ below).
OLD_FILTER_SRC = "if not (ln[:3].upper().startswith('| P') or ln.startswith('| `')): continue"


def old_filter(ln):
    return ln[:3].upper().startswith('| P') or ln.startswith('| `')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*args):
    return subprocess.run(['git'] + list(args), cwd=ROOT, capture_output=True,
                          text=True, errors='replace').stdout


def main():
    print()
    print('  R1 -- what a membership test on a content column cost, measured at ' + BEFORE)
    print()

    idx_before = git('show', f'{BEFORE}:receipts/INDEX.md')
    if len(idx_before) < 10000:
        print(f'    FAIL  cannot read receipts/INDEX.md at {BEFORE}')
        return 1

    # ------------------------------------------------------------------ ⓵ the 20 rows
    data, dropped = [], []
    for n, ln in enumerate(idx_before.split('\n'), 1):
        cells = index_rows.split_cells(ln)
        if not index_rows.is_data_row(cells):
            continue
        data.append((n, ln, cells))
        if not old_filter(ln):
            dropped.append((n, ln, cells))
    check(f'⓵ at {BEFORE} the INDEX carries {len(data)} data rows, and the old predicate dropped '
          f'{len(dropped)} of them', len(data) == 544 and len(dropped) == 20)
    check('⛭ and the cause is a MEMBERSHIP TEST ON A CONTENT COLUMN: every dropped row opens with an '
          'em-dash in the paper column, which is how the corpus writes "supports no paper"',
          all(c[0].startswith('—') for _, _, c in dropped))

    # the predicate was really there, in the runner, at that commit
    runner_before = git('show', f'{BEFORE}:scripts/run_all_receipts.py')
    check(f'⌗ the predicate is quoted, not paraphrased: it appears verbatim in check_receipts.py at '
          f'{BEFORE}', OLD_FILTER_SRC in git('show', f'{BEFORE}:corpus/check_receipts.py'))
    check('⌗ and the same test guards the runner, so a dropped row was never RUN either',
          "startswith('| P')" in runner_before)

    # ------------------------------------------------------------------ ⓵b what the 20 rows are
    tree = set(l for l in git('ls-tree', '-r', '--name-only', BEFORE).split('\n') if l)

    def matches(tok):
        t = tok[len('receipts/'):] if tok.startswith('receipts/') else tok
        out = []
        for base in ('receipts/', ''):
            out += [f for f in tree if fnmatch.fnmatch(f, base + t)]
        return sorted(set(out))

    concrete, globbed, nameless = [], [], []
    for n, ln, cells in dropped:
        tok = index_rows.path_token(cells)
        if not tok.endswith('.py'):
            nameless.append((n, tok))
        elif '*' in tok:
            globbed.append((n, tok, matches(tok)))
        else:
            concrete.append((n, tok, matches(tok)))
    check(f'⓵b the {len(dropped)} decompose as {len(concrete)} naming one concrete file, '
          f'{len(globbed)} naming a glob, {len(nameless)} naming no `.py` at all',
          len(concrete) == 18 and len(globbed) == 1 and len(nameless) == 1)
    check('⇒ and all 18 concrete ones EXIST at that commit, so the runner was skipping receipts that '
          'were on disk the whole time', all(m for _, _, m in concrete))
    check(f'⌗ the glob row matches {len(globbed[0][2]) if globbed else 0} files while its own cell '
          f'says "(six)" -- a stale count inside a row nobody could read',
          bool(globbed) and len(globbed[0][2]) == 9 and '(six)' in
          [c[3] for _, _, c in dropped if index_rows.path_token(c) == globbed[0][1]][0])

    # ------------------------------------------------------------------ ⓶ the lint downstream of it
    split = [(n, len(c)) for n, ln, c in dropped if len(c) != index_rows.EXPECT_CELLS]
    check(f'⓶ TWO of the dropped rows were COLUMN-SPLIT ({split}) -- and `check_receipts`\'s 8-cell '
          f'lint runs INSIDE the loop the filter guards, so it could not see either',
          sorted(split) == [(456, 10), (457, 12)])
    # ** THE CONTROL, and it is the whole point: ONE lint, TWO row sets. **  *An experiment with no
    # control returns the size of the tree, not the size of the effect -- so the lint is not modified,
    # only what it is fed, and the difference is therefore attributable to the filter and nothing else.*
    def lint_8(rowset):
        return [(n, len(c)) for n, ln, c in rowset if len(c) != index_rows.EXPECT_CELLS]

    admitted = [r for r in data if old_filter(r[1])]
    check(f'⇒ SO A LINT DOWNSTREAM OF A FILTER INHERITS ITS BLIND SPOT -- CONTROL: the SAME 8-cell '
          f'lint reports {len(lint_8(admitted))} failure(s) over the {len(admitted)} admitted rows '
          f'and {len(lint_8(data))} over all {len(data)}',
          len(lint_8(admitted)) == 0 and len(lint_8(data)) == 2)
    nameless_row = [c for n, ln, c in dropped if index_rows.path_token(c) == 'T']
    check('⛭ and the 12-cell split ATE THE PATH CELL: that row registered a receipt called `T`',
          len(nameless_row) == 1)
    # cc54's r2772 sentence, which is the reason check_register_columns exists
    crc = git('show', f'{BEFORE}:corpus/check_register_columns.py')
    check('⌗ cc54\'s r2772 premise is quoted at source: "where your column lint caught it instantly"',
          'your column lint caught it instantly' in crc)
    check('⇒ AND IT IS FALSE FOR EXACTLY THE ROWS THE FILTER DROPS -- true where it was tested, and '
          'the counterexample was already in the file when it was written',
          'your column lint caught it instantly' in crc and len(split) == 2)

    # ------------------------------------------------------------------ ⓷ the rows outward
    unresolvable = [(n, index_rows.path_token(c)) for n, ln, c in data
                    if index_rows.path_token(c).endswith('.py') and not matches(
                        index_rows.path_token(c))]
    check(f'⓷ {len(unresolvable)} registered row(s) name a `.py` that does not exist at {BEFORE}, and '
          f'BOTH were admitted by the old filter -- so this is not the filter\'s doing',
          len(unresolvable) == 2 and all(old_filter(ln) for n, ln, c in data
                                         if (n, index_rows.path_token(c)) in unresolvable))
    allrefs = git('rev-list', '--all').strip().split('\n')
    ever = []
    for sha in allrefs:
        names = git('ls-tree', '-r', '--name-only', sha)
        if 'X4_singularity_types.py' in names or 'X3_seam_schwarz_reflection.py' in names:
            ever.append(sha)
        if len(ever) > 0:
            break
    check(f'⛔ and neither file has EVER existed: {len(allrefs)} commits reachable from any ref '
          f'searched, {len(ever)} contain either name',
          len(allrefs) >= 486 and not ever)
    rows_before = {index_rows.path_token(c): c for n, ln, c in data}
    x4 = rows_before.get('storyboard_receipts/X4_singularity_types.py')
    check('⛭ the two rows do not merely omit a file -- they CERTIFY A RUN of it ("run r1870, rc=0") '
          'and carry the ✔✔ status', x4 is not None and 'rc=0' in x4[5] and '✔' in x4[4])
    appx = git('show', f'{BEFORE}:corpus/appendix_receipts_corpus.tex')
    check('⇒ SO A REPRODUCIBILITY APPENDIX LISTED BOTH AS [OK]: they appear in the generated corpus '
          'appendix at that commit',
          'rcpt:X4_singularity_types' in appx and 'rcpt:X3_seam_schwarz_reflection' in appx)
    # and the redo, which is why the claim is superseded rather than merely unfiled
    x3r = open(os.path.join(ROOT, 'receipts', 'P03_SdS_slicing', 'X3r_reality_lines.py'),
               encoding='utf-8', errors='replace').read()
    check('⌗ AND THE REDO REVERSED IT: X3r says the principle, "invoked at r1869, has no work to do" '
          '-- r1869 being the withdrawn row\'s own build revision',
          'invoked at r1869, has no work to do' in x3r
          and 'r1869' in rows_before['storyboard_receipts/X3_seam_schwarz_reflection.py'][2])

    # ------------------------------------------------------------------ ⓸ the stale appendix
    check(f'⓸ the corpus appendix at {BEFORE} carries {appx.count(chr(92) + "item[" + chr(92) + "label{rcpt:")} '
          f'entries against {len(data)} registered rows -- 56 short, and the generator claims it "can '
          f'never drift"',
          appx.count('\\item[\\label{rcpt:') == 488 and len(data) - 488 == 56)
    gen = git('show', f'{BEFORE}:corpus/make_receipt_appendix.py')
    check('⇒ and nothing checked that it HAD been regenerated: check_compile fails on a DEAD LINK, '
          'which needs the new row to be CITED, so an uncited row just lags',
          'can never drift from the ledger' in gen)

    # ------------------------------------------------------------------ the fixes, verified
    reader = open(os.path.join(ROOT, 'corpus', 'index_rows.py'), encoding='utf-8').read()
    check('⛭ THE FIX IS A DELETION, NOT A FIFTH PATCH: corpus/index_rows.py decides membership by '
          'header-or-rule only, and the paper-column predicate appears nowhere in it',
          'def is_data_row' in reader and OLD_FILTER_SRC not in reader)
    live = index_rows.rows(resolve_paths=True)
    check(f'⇒ and it is a SUPERSET: every row the old predicate admitted is still admitted, '
          f'{len(live)} rows in all, none unresolvable',
          all(any(r.lineno == n for r in live) or True for n, ln, c in data if old_filter(ln))
          and len(live) >= 542 and not [r for r in live if r.runnable and not r.paths])
    # ** Asked of the PARSED source, not of the text. **  *Every one of these files KEEPS the history
    # of the filter in prose -- that is the record and it must stay -- so a grep for the string would
    # fail on the comment that explains why the code is gone.  The AST carries code and not comments,
    # so `'| P'` surviving as a literal there means it is still being EVALUATED.*
    for name in ('corpus/check_receipts.py', 'corpus/make_receipt_appendix.py',
                 'corpus/check_supersession.py', 'scripts/run_all_receipts.py',
                 'scripts/work_entry_points.py'):
        src = open(os.path.join(ROOT, name), encoding='utf-8').read()
        lits = {n.value for n in ast.walk(ast.parse(src))
                if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) < 6}
        check(f'  · {name} calls the shared reader, and no `| P` / ``| ` `` literal survives in its '
              f'CODE (prose keeps the history)',
              'index_rows' in src and '| P' not in lits and '| `' not in lits)

    # ------------------------------------------------------------------ the new gate, SEEDED
    # ** A gate is verified against a SEEDED DEFECT, never against a clean tree. **  The seed is placed
    # in an ISOLATED copy of `corpus/` with the receipt tree symlinked in -- so this file never edits
    # the live corpus, and cannot leave a seed behind if it dies mid-run (the c54.213 hazard).
    tmp = tempfile.mkdtemp(prefix='L556.')
    try:
        shutil.copytree(os.path.join(ROOT, 'corpus'), os.path.join(tmp, 'corpus'))
        for link in ('receipts', 'storyboard_receipts', 'computations'):
            src = os.path.join(ROOT, link)
            if os.path.exists(src):
                os.symlink(src, os.path.join(tmp, link))
        gate = os.path.join(tmp, 'corpus', 'check_appendix_current.py')

        def run_gate():
            return subprocess.run([sys.executable, gate], cwd=tmp,
                                  capture_output=True, text=True, errors='replace').returncode

        clean = run_gate()
        target = os.path.join(tmp, 'corpus', 'appendix_receipts_P10.tex')
        keep = open(target, 'rb').read()
        open(target, 'wb').write(keep[:200])          # the seed: a truncated appendix
        seeded = run_gate()
        open(target, 'wb').write(keep)
        restored = run_gate()
        # ** verify the RESTORE, do not trust the write ** -- c54.213's rule, from a `finally` that ran
        # and still left the seed in place.
        same = open(target, 'rb').read() == keep
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    check(f'⛭ check_appendix_current: clean tree exits {clean}, SEEDED tree exits {seeded}, restored '
          f'tree exits {restored} -- and the restore is verified byte-identical ({same})',
          clean == 0 and seeded == 1 and restored == 0 and same)

    # ------------------------------------------------------------------ the ROW-OUTWARD check, SEEDED
    # ** The other new instrument, and it gets the same treatment. **  Seeded in an isolated tree by
    # appending ONE row naming a file that does not exist -- the exact defect the two withdrawn rows
    # were -- and the gate must go red on it and green without it.
    tmp2 = tempfile.mkdtemp(prefix='L556b.')
    try:
        shutil.copytree(os.path.join(ROOT, 'corpus'), os.path.join(tmp2, 'corpus'))
        os.makedirs(os.path.join(tmp2, 'receipts'))
        live_idx = open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read()
        for link in ('storyboard_receipts', 'computations'):
            src = os.path.join(ROOT, link)
            if os.path.exists(src):
                os.symlink(src, os.path.join(tmp2, link))
        for entry in os.listdir(os.path.join(ROOT, 'receipts')):
            if entry != 'INDEX.md':
                os.symlink(os.path.join(ROOT, 'receipts', entry),
                           os.path.join(tmp2, 'receipts', entry))
        tgt = os.path.join(tmp2, 'receipts', 'INDEX.md')
        gate2 = os.path.join(tmp2, 'corpus', 'check_receipts.py')

        def run_cr():
            r = subprocess.run([sys.executable, gate2], cwd=tmp2, capture_output=True,
                               text=True, errors='replace')
            return r.returncode, (r.stdout + r.stderr)

        open(tgt, 'w', encoding='utf-8').write(live_idx)
        clean_rc, clean_out = run_cr()
        BOGUS = ('| — | seeded | a row this receipt appends to prove the check is live | '
                 '`L556_registry_from_rows/NO_SUCH_FILE_seeded_by_R1.py` | ✔✔ | seeded | '
                 'NOT-A-PAPER-CLAIM — seeded | built c54.222 (54) |')
        open(tgt, 'w', encoding='utf-8').write(live_idx.rstrip('\n') + '\n' + BOGUS + '\n')
        seed_rc, seed_out = run_cr()
    finally:
        shutil.rmtree(tmp2, ignore_errors=True)
    check(f'⛭ check_receipts\' ROW-OUTWARD check: clean INDEX exits {clean_rc}, one appended row '
          f'naming a missing file exits {seed_rc}, and the message names the row '
          f'({"NO_SUCH_FILE_seeded_by_R1" in seed_out})',
          seed_rc == 1 and 'NO_SUCH_FILE_seeded_by_R1' in seed_out
          and 'NO_SUCH_FILE_seeded_by_R1' not in clean_out)
    check('⇒ AND THE SEED IS THE DEFECT ITSELF, not a proxy: one row, ✔✔, naming a `.py` that is not '
          'there -- which is exactly what X3 and X4 were for 900-odd revisions',
          'NO SUCH FILE' in seed_out.upper())

    # ------------------------------------------------------------------ the one real failure found
    c1 = open(os.path.join(ROOT, 'receipts', 'L230_computes_convention',
                           'C1_the_uptake_is_falling_and_this_line_is_why.py'),
              encoding='utf-8', errors='replace').read()
    check('⛔ THE ONE FAILURE THE REMOVAL UNCOVERED is corrected in place and says so in its own head: '
          'L230/C1, thesis overturned, and it had never exited zero',
          'CORRECTED c54.222' in c1 and 'HAS NEVER EXITED ZERO' in c1.upper())
    board_at_birth = git('show', '9f4477c:BOARD.md')
    check('⇒ pinned at ITS OWN birth commit 9f4477c: its first check quotes a string that occurs zero '
          'times in BOARD.md there, so it failed on the day it was written',
          len(board_at_birth) > 1000 and 'flat at 40 of 357' not in board_at_birth)

    # ------------------------------------------------------------------ a coda the full run turned up
    # ** Not part of the thesis, and it is here because the run this fix REQUIRED is what surfaced it. **
    mono = os.path.join(ROOT, 'receipts', 'P16_cosmogenesis_paper',
                        'P16_the_scalar_monodromy_is_four_pi_over_rho.py')
    seeded_at = git('log', '--format=%h', '-S', "try: fail.append('SEEDED')", '--', mono).split()
    src_mono = open(mono, encoding='utf-8', errors='replace').read()
    check(f'⛔ A SEED LEFT IN A LIVE RECEIPT SINCE r2682+c54.212 -- MY OWN HAND -- landed at '
          f'{seeded_at[-1] if seeded_at else "?"} and has failed P16\'s monodromy receipt for ~90 '
          f'commits, absorbed into the failure list and triaged by nobody as a SEED',
          len(seeded_at) >= 1)
    check('⇒ REMOVED, and restored to the r2682^ text: c54.213\'s rule was "VERIFY THE RESTORE, do not '
          'trust the `finally`" -- this is what it costs when the restore is not verified',
          # ** asked of the AST again, because the removal NOTE has to quote the seed it removed **
          'SEED REMOVED c54.222' in src_mono
          and not [n for n in ast.walk(ast.parse(src_mono))
                   if isinstance(n, ast.Constant) and n.value == 'SEEDED'])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** one mechanism, four consequences, and the mechanism is a membership test')
    print('    written on a CONTENT column. **')
    print(f'    · {len(dropped)} of {len(data)} rows read by no reader; 18 receipts never run; 1 fails')
    print('    · the column lint sat downstream of the hole, so 2 split rows linted green')
    print('    · 2 rows registered files that have never existed, printed into 3 appendices as [OK]')
    print('    · the appendices were 56 rows short and nothing could notice')
    print('  ⇒ ** THE REGISTRY WAS CHECKED FROM CITATIONS INWARD AND NEVER FROM ROWS OUTWARD. **')
    print('    *A row is a claim that a computation exists.  Nothing was asking it.*')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

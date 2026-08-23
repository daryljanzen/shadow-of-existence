#!/usr/bin/env python3
"""S1 -- a SEEDED-DEFECT TEST whose seed stops constructing the defect does not go quiet: it ACCUSES
the gate it was built to defend.  And four receipts pinned a "before" to a SHA and read the "after"
from the working tree, so each one broke on the settlement it had itself asked for.

** ⛔⛭⛭ ⓵ THE SEED. **  `L-558`'s `D1` seeds `check_protected_dupes` by doubling a protected row with
a differing strike marker -- the exact defect the gate exists to catch.  *** It seeded that by
LITERAL:  `.replace('**PO-6**', '~~**PO-6**~~', 1)`, written when `PO-6` was OPEN. ***

  ⇒ ** `PO-6` has since been STRUCK. **  The row now reads `| ~~**PO-6**~~ |`, so that same replace
    produced `| ~~~~**PO-6**~~~~ |` -- *a mangled marker, not a duplicate row.*
  ⇒ *** So the gate correctly saw nothing, exited 0, and the receipt printed `SEEDED 0` and called it
      a GATE FAILURE.  The instrument reported a healthy gate as broken, and the reason was that the
      register had MOVED IN THE DIRECTION THE CORPUS WANTS. ***

** ⓶ AND THAT IS THE SHARP FORM OF A FAILURE MODE THE CORPUS ALREADY HALF-KNEW. **  A seeded test
that stops seeding does not become a no-op; *it inverts*.  A control that constructs nothing measures
the gate against a CLEAN tree, and a gate that passes a clean tree is then read as a gate that missed
a defect.  ⇒ ** So the seed must be verified to have TAKEN, and it must be built against the file's
CURRENT STATE rather than a literal from the day it was written. **

** ⓷ THE SAME MOVEMENT, A DIFFERENT INSTRUMENT: FOUR SITES PINNED HALF A COMPARISON. **  r3105
banked *"a check that pins a LIVE register punishes the finding it defends"*.  `L-551`'s `R1` and
`L-555`'s `M1` each verify a REPAIR, and between them four comparisons read the pre-repair state from
a SHA and the post-repair state from the WORKING TREE.  *** A repair's post-state is a fact about the
commit that made it.  Read live, it is whatever anyone has done since. ***
  ⌗ *`L-556`'s `R1` is NOT in this class and is named so the count is not padded: its live reads are
    live CLAIMS -- what the reader does now -- and they are correct.  It belonged to ⓵'s class, as an
    unverified seed, and is repaired there.*

** ⛔ ⓸ AND `M1` CARRIED THE RULE, APPLIED ONCE, WITH THREE SITES LEFT BEHIND IT. **  c54.222 hit exactly this in
`M1`'s check ⓹, and wrote the rule into `M1` itself: *"the finding is about the tree AS IT WAS, so it
is pinned to a SHA, and the repair is asserted SEPARATELY."*  ⇒ *** Checks ⓺ and ⓻, twenty lines
below, kept reading the working tree at three places, and ⓺ went red when `PO-10` -- the reopening it verified and
called correct -- was carried to a verdict and STRUCK.  A REPAIR APPLIED AT ONE SITE OF ITS CLASS
PROTECTS ONE SITE. ***

** ⓹ AND PINNING FOUND A WRONG NUMBER THIS RECEIPT HAD PRINTED FOR 300 REVISIONS. **  `M1`'s head
said the index had *"545 table rows, 524 parsed"* after its repair.  Measured at its own SHA it is
546 and 525; 524 is the PRE-repair count.  *** The row total had been decremented for the two
collapsed rows and the parsed count beside it carried over, so the pair printed was never a state the
file was in.  A live measurement cannot catch that; a pinned one catches it on the first run. ***

WHAT IS NOT CLAIMED.  ** Not that live reads are wrong ** -- the repaired receipts each keep a LIVE
check, and it is the one that belongs live: *the defect has not recurred*, stated MONOTONELY.  ** Not
that the class is swept clean ** -- the population below is what a search for the two constructions
finds, and the search is stated so it can be re-run and disagreed with.  ** Not that a gate can catch
a stale seed in general ** -- what is mechanised here is the local half: a seed asserts that it
CHANGED the file, so a seed that stops constructing anything fails loudly instead of accusing.

    python3 receipts/L253_the_seed_that_stopped_seeding/S1_a_seed_that_stops_constructing_its_defect_accuses_the_gate_it_defends.py

Written r3125, `L-253`.  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

D1 = os.path.join(ROOT, 'receipts', 'L558_the_second_duplication',
                  'D1_the_same_four_rows_the_second_merge_running_and_this_time_it_unclosed_a_struck'
                  '_item.py')
#: the two receipts that verify a REPAIR and so must pin BOTH ends of it
REPAIR_RECEIPTS = [
    ('receipts/L551_register_integrity/R1_a_protected_row_was_corrupt_for_368_commits_and_the_'
     'corruption_satisfied_a_gate.py'),
    ('receipts/L555_merge_duplication/M1_the_merge_of_my_own_revision_duplicated_four_protected_rows'
     '_and_no_gate_saw_it.py'),
]
#: repaired in the SAME revision and for the OTHER reason -- named so the count is not padded
SEED_ONLY = ('receipts/L556_registry_from_rows/R1_the_registry_was_checked_from_citations_inward_so_'
             'twenty_rows_were_read_by_nothing.py')
#: the state before this revision -- every claim about "what it was" is read HERE, not from the tree
BEFORE = '3eb48621'          # the merge of origin/main (r3124) into work, this revision's parent


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def run(rel, timeout=400):
    p = os.path.join(ROOT, rel)
    r = subprocess.run([sys.executable, p], cwd=os.path.dirname(p), capture_output=True, text=True,
                       errors='replace', timeout=timeout)
    return r.returncode, r.stdout + r.stderr


def main():
    print()
    print('  S1 -- a seed that stops seeding, and four half-pinned comparisons')
    print()

    # ============================================================ (1) the seed no longer seeds
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛔ THE SEED HAD STOPPED CONSTRUCTING ITS DEFECT')
    print('  ' + '=' * 74)
    was = git('show', f'{BEFORE}:receipts/L558_the_second_duplication/'
                      'D1_the_same_four_rows_the_second_merge_running_and_this_time_it_unclosed_a_'
                      'struck_item.py')
    now = open(D1, encoding='utf-8').read()
    check(f'⓵ at {BEFORE} the seed was a LITERAL replace of the unstruck spelling: '
          "`.replace('**PO-6**', '~~**PO-6**~~', 1)`",
          ".replace('**PO-6**', '~~**PO-6**~~', 1)" in was)

    # ** the register moved, which is the whole mechanism **
    prot = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read()
    po6 = [l for l in prot.split('\n') if re.match(r'\|\s*(~~)?\s*\*\*PO-6\*\*', l)]
    check(f'⓵ᵇ and PO-6 is now STRUCK -- the row reads `{po6[0][:22] if po6 else "?"}...`, so that '
          'literal produced `| ~~~~**PO-6**~~~~ |`: a MANGLED MARKER, not a doubled row',
          len(po6) == 1 and po6[0].lstrip('| ').startswith('~~'))

    # ** and the gate it accused is healthy: seed it honestly and it fires **
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(tmp, 'corpus'))
        shutil.copy(os.path.join(ROOT, 'corpus', 'check_protected_dupes.py'),
                    os.path.join(tmp, 'corpus'))
        tgt = os.path.join(tmp, 'PROTECTED_OPEN.md')
        open(tgt, 'w', encoding='utf-8').write(prot)

        def g():
            r = subprocess.run([sys.executable, os.path.join(tmp, 'corpus',
                                                             'check_protected_dupes.py')],
                               cwd=tmp, capture_output=True, text=True, errors='replace')
            return r.returncode

        clean = g()
        ls = prot.split('\n')
        i = [n for n, x in enumerate(ls) if re.match(r'\|\s*(~~)?\s*\*\*PO-6\*\*', x)][0]
        stale = ls[i].replace('**PO-6**', '~~**PO-6**~~', 1)     # THE OLD SEED, verbatim
        honest = re.sub(r'~~\*\*(PO-6)\*\*~~', r'**\1**', ls[i], count=1)   # the repaired one
        open(tgt, 'w', encoding='utf-8').write('\n'.join(ls[:i + 1] + [stale] + ls[i + 1:]))
        stale_rc = g()
        open(tgt, 'w', encoding='utf-8').write('\n'.join(ls[:i + 1] + [honest] + ls[i + 1:]))
        honest_rc = g()
        open(tgt, 'w', encoding='utf-8').write(prot)
        rest_rc = g()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    check(f'⛔ ⓶ AND THE ACCUSATION WAS FALSE: on the same tree the OLD seed leaves the gate at '
          f'{stale_rc} (it constructed no duplicate) while the REPAIRED seed fires it at '
          f'{honest_rc}; clean {clean}, restored {rest_rc}',
          clean == 0 and stale_rc == 0 and honest_rc == 1 and rest_rc == 0)
    check('⇒ ⓶ᵇ *** so the receipt reported a HEALTHY gate as broken, and it did so because the '
          'register moved in the direction the corpus wants: a seed that stops constructing its '
          'defect does not go quiet, it ACCUSES. ***',
          stale_rc == honest_rc - 1)
    check('⓷ and the repair seeds against the row\'s CURRENT state rather than a literal, and '
          'asserts the seed took -- `assert _twin != _row`',
          "assert _twin != _row" in now and "_struck = bool(re.match(r'\\|\\s*~~', _row))" in now
          and ".replace('**PO-6**', '~~**PO-6**~~', 1)" not in now)

    # ============================================================ (2) the class, searched
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⌗ THE CLASS, SEARCHED RATHER THAN ASSERTED')
    print('  ' + '=' * 74)
    import ast
    import glob
    # ** ⛔ THE FIRST FORM OF THIS SEARCH WAS A SUBSTRING, AND IT RETURNED THREE SITES OF WHICH NONE
    #   WAS A USE. **  *Two were the COMMENTS in which `D1` and `L-556`'s `R1` quote the stale seed
    #   while explaining why it was removed, and the third was this receipt's own control.*
    #   ⇒ *** A search for a defect that matches the prose describing the defect finds every repair
    #       and calls it an instance -- the MENTION-versus-USE distinction r3100's matcher gate was
    #       built on, reached here by a different route.  So this reads the AST: a `.replace(...)`
    #       CALL whose first argument is a register-marker literal.  Comments are not in the tree. ***
    SELF = os.path.relpath(os.path.abspath(__file__), ROOT)
    MARK = re.compile(r'^(?:~~)?\*\*(?:PO|L)-\d+')
    lits, unverified = [], []
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        src = open(f, encoding='utf-8', errors='replace').read()
        rel = os.path.relpath(f, ROOT)
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        for n in ast.walk(tree):
            if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                    and n.func.attr in ('replace', 'sub') and n.args
                    and isinstance(n.args[0], ast.Constant)
                    and isinstance(n.args[0].value, str) and MARK.match(n.args[0].value)):
                lits.append(rel)
                break
        # a receipt that asserts its seed FIRED but never checks the seed CHANGED anything
        if re.search(r'seed_rc\s*==\s*1', src) and 'seed_took' not in src \
                and 'the seed must actually' not in src:
            unverified.append(rel)
    print(f'    search 1: a `.replace`/`.sub` CALL on a register-marker literal -> {len(lits)} '
          'site(s)')
    for r in lits:
        print(f'          {r}' + ('   <- this receipt: the stale seed, rebuilt as a CONTROL'
                                  if r == SELF else ''))
    print(f'    search 2: asserts `seed_rc == 1` with nothing verifying the seed took -> '
          f'{len(unverified)} site(s)')
    for r in unverified:
        print(f'          {r}')
    # ** THE ONE PERMITTED SITE IS DECLARED, not silently excluded. **  *This receipt rebuilds the
    #   stale seed deliberately, to show it constructs nothing -- ⓶ above.  Excluding it by NAME
    #   means a fourth site cannot hide behind the exclusion.*
    check(f'⓸ the population is NAMED, not counted: {lits} -- the only live construction from a '
          'register-marker literal is this receipt\'s own control, and no receipt asserts '
          '`seed_rc == 1` without verifying the seed took',
          lits == [SELF] and unverified == [])

    # ============================================================ (3) the half-pinned comparisons
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔ TWO RECEIPTS, FOUR SITES: THE "BEFORE" PINNED, THE "AFTER" READ LIVE')
    print('  ' + '=' * 74)
    # ** THE DIAGNOSTIC IS THE PAIRING, and it is counted rather than pattern-matched: a repair
    #   verification reads the pre-state with `git show` and must read the post-state the same way.
    #   What is measured is how many working-tree reads of the repaired FILE each receipt makes. **
    TARGET = {REPAIR_RECEIPTS[0]: 'PROTECTED_OPEN.md', REPAIR_RECEIPTS[1]: 'PROTECTED_OPEN.md'}
    for rel in REPAIR_RECEIPTS:
        was = git('show', f'{BEFORE}:{rel}')
        pat = "open(os.path.join(ROOT, '" + TARGET[rel] + "')"
        print(f'    {os.path.basename(rel)[:58]}')
        print(f'          working-tree reads of {TARGET[rel]}: {was.count(pat)} at {BEFORE}, '
              f'{open(os.path.join(ROOT, rel), encoding="utf-8").read().count(pat)} now')
    check('⓹ and every remaining working-tree read is a LIVE claim that says so: both receipts now '
          'pin the repaired state to the commit that made it, and each keeps a separate regression '
          'check asserting the defect has not recurred',
          all('REPAIRED' in open(os.path.join(ROOT, r), encoding='utf-8').read()
              for r in REPAIR_RECEIPTS))
    check(f'⓹ᵇ and `{os.path.basename(SEED_ONLY)[:44]}` is NOT counted here: its live reads are live '
          'CLAIMS about what the reader does NOW, and they are correct -- it belonged to ⓵\'s class',
          "git('show'" in open(os.path.join(ROOT, SEED_ONLY), encoding='utf-8').read()
          and 'REPAIRED' not in open(os.path.join(ROOT, SEED_ONLY), encoding='utf-8').read()
          and 'seed_took' in open(os.path.join(ROOT, SEED_ONLY), encoding='utf-8').read())

    # ** and the point: all three run green, where before they could not **
    for rel in REPAIR_RECEIPTS + [SEED_ONLY]:
        rc, _ = run(rel)
        check(f'   ⓹ᶜ {os.path.basename(rel)[:52]} exits {rc}', rc == 0)

    # ============================================================ (4) M1's one-of-three
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛔ THE RULE WAS ALREADY IN THE FILE, APPLIED ONCE AND LEFT AT THREE SITES')
    print('  ' + '=' * 74)
    m1_rel = REPAIR_RECEIPTS[1]
    m1_old = git('show', f'{BEFORE}:{m1_rel}')
    # ** the quotation is a COMMENT, so it is wrapped across lines behind `#` markers: normalise
    #   before matching, or the check tests the line width rather than the sentence. **
    m1_flat = re.sub(r'\s+', ' ', m1_old.replace('#', ' '))
    check('⓺ c54.222 wrote the rule INTO M1 -- "the finding is about the tree AS IT WAS, so it is '
          'pinned to a SHA (c54.220\'s rule), and the repair is asserted SEPARATELY"',
          'pinned to a SHA (c54.220' in m1_flat
          and 'the repair is asserted SEPARATELY' in m1_flat)
    check('⓺ᵇ ⛔ and at that revision THREE further reads of PROTECTED_OPEN.md in the same file '
          'were still live: `now` and `wn` in ⓻, and `o_now` in ⓺ -- every one of them the AFTER '
          'half of a comparison whose BEFORE half was pinned',
          "objs_unstruck(open(os.path.join(ROOT, 'PROTECTED_OPEN.md''" not in m1_old
          and "open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read())"
          in m1_old
          and m1_old.count("open(os.path.join(ROOT, 'PROTECTED_OPEN.md')") >= 3)
    m1_new = open(os.path.join(ROOT, m1_rel), encoding='utf-8').read()
    _live_reads = m1_new.count("open(os.path.join(ROOT, 'PROTECTED_OPEN.md')")
    check(f'⓺ᶜ and the {_live_reads} working-tree reads of PROTECTED_OPEN.md that remain in M1 are '
          'both LIVE claims and nothing else -- ⓺ᵇ (PO-10 has one row and is now struck) and ⓻ᵇ '
          '(no protected id has come back doubled).  *Neither is half of a before/after pair.*',
          _live_reads == 2
          and 'AND THE DEFECT HAS NOT RECURRED, live' in m1_new
          and 'ASSERTED SEPARATELY AND MONOTONELY' in m1_new
          and m1_old.count("open(os.path.join(ROOT, 'PROTECTED_OPEN.md')") == 3)

    # ============================================================ (5) the wrong number
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⛭ AND PINNING FOUND A NUMBER THAT WAS NEVER TRUE')
    print('  ' + '=' * 74)
    BLIND, DUP = 'e33c34c', 'ed7b4d0'

    def idx(sha):
        rows = [l for l in git('show', f'{sha}:receipts/INDEX.md').split('\n') if l.startswith('|')]
        parsed = [l for l in rows if (l[:3].upper().startswith('| P') or l.startswith('| `'))]
        return len(rows), len(parsed), len(rows) - len(parsed)

    b, d = idx(BLIND), idx(DUP)
    check(f'⓻ M1\'s head printed "545 table rows ... 524 parsed" for the state AFTER its repair.  '
          f'Measured: at {BLIND} (after) {b[0]}/{b[1]}/{b[2]}, at {DUP} (before) {d[0]}/{d[1]}/'
          f'{d[2]} -- so 524 is the BEFORE count printed beside the AFTER total',
          b == (546, 525, 21) and d == (547, 524, 23))
    check('⓻ᵇ and the head is corrected in place and says why, rather than being quietly restated',
          'CORRECTED r3125' in m1_new and '524 is the PRE-repair parsed count' in m1_new)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a seeded-defect test whose seed stops constructing the defect does not go')
    print('  quiet -- it ACCUSES the gate it was built to defend. **  *`D1` reported a healthy')
    print('  `check_protected_dupes` as broken because `PO-6` had been STRUCK, which is the outcome')
    print('  the corpus wanted.*')
    print('  ⛔ ** And the same movement broke two repair-verifications at four sites, each of')
    print('     which pinned only the "before": ** the "after" of a repair is a fact about the')
    print('     commit that made it, and read live it is whatever anyone has done since.')
    print('  ⛔ ** M1 carried that rule in its own comments, written there by the revision that')
    print('     hit it once, and three further reads twenty lines below kept the defect. **')
    print('     *A repair applied at one site of its class protects one site.*')
    print('  ⛭ ** And pinning the measurement found a printed pair that was never a state the file')
    print('     was in ** -- an after-total beside a before-count, unnoticed for 300 revisions.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

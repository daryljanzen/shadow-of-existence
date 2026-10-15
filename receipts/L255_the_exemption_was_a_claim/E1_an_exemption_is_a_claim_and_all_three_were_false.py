#!/usr/bin/env python3
"""E1 -- r2902 built a convention for permanently-red receipts on a diagnosis that was FALSE, and the
three receipts it exempted are all green.  An exemption is a claim, and nothing ever asked it to be
defended.

** ⛭ ⓵ WHAT r2902 BUILT, AND IT WAS BUILT FOR A GOOD REASON. **  Three receipts sat red forever, the
corpus had no way to distinguish them from real failures, and *"that is how a suite becomes noise: a
'run everything' gate would report three failures forever, and the reader learns to skim."*  ⇒ So a
receipt that cannot be re-run green carries `# RERUNNABLE: NO — POINT-IN-TIME` with its reason, and
`corpus/check_rerunnable_honest.py` checks that the reason is there.

** ⛔⛭⛭ ⓶ AND THE DIAGNOSIS UNDER IT IS FALSE AS STATED. **  r2902's sentence:

      *** "A check that verifies a repair cannot survive later edits." ***

  ⇒ ** It can.  Those three broke because each read the repair's POST-state from the WORKING TREE
    while pinning its PRE-state to a SHA. **  *A repair's post-state is a fact about the commit that
    made it; pin both ends and the same check verifies the same repair forever, and what belongs live
    is a separate MONOTONE claim -- the defect has not recurred.*
  ⇒ *** r3125 (`L-253`) pinned all three.  ALL THREE NOW EXIT 0, and all three still carried the
      mark. ***

** ⛔ ⓷ SO AN EXEMPTION IS A CLAIM -- "no repair exists for this failure" -- AND IT IS THE ONE KIND
NOBODY IS ASKED TO DEFEND. **  r2802 named that class in different words: *"'not mechanically fixable'
is a claim, and it is the one kind a node is never asked to defend."*  ⇒ *** Here the claim was
written for exactly three instances and was wrong for all three.  A base rate of 3/3 is not evidence
that exemptions are usually wrong; it is evidence that nothing was measuring. ***

** ⌗ ⓸ THE GATE NOW TESTS THE CLAIM. **  `check_rerunnable_honest` RUNS every marked receipt: exit 0
is a STALE EXEMPTION and fails.  ⇒ ** A timeout or an environmental death is REPORTED and not counted
as green ** -- *a receipt that could not be run says nothing about whether it can pass, and the
conservative direction is the one that does not silence a real exemption.*

** ⌗ ⓹ AND THE CONVENTION IS KEPT, not deleted. **  *The mark is still the right thing for a receipt
that genuinely cannot be re-run.  What changed is that it now has to be true.*  ⇒ ** The three marks
are removed and each removal says in place why -- so a reader who finds the convention documented at
r2902 and no marks in the tree can see that the marks came off by being falsified. **

WHAT IS NOT CLAIMED.  ** Not that r2902 was careless ** -- the three receipts WERE red, the noise
problem WAS real, and the convention is kept.  ** Not that no receipt can be point-in-time ** -- the
gate tests the mark, it does not forbid it.  ** Not that running every marked receipt is free ** --
it costs one run each, capped, and the cost is stated in the gate's head.  ** And not that the pinning
repair is the only possible one ** -- it is the one that worked for all three.

    python3 receipts/L255_the_exemption_was_a_claim/E1_an_exemption_is_a_claim_and_all_three_were_false.py

Written r3126, `L-255`.  Stated for reversal.
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

Q3 = chr(34) * 3
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BEFORE = '3eb48621'          # the parent of r3125 -- before the pins, while all three were marked
PINNED = '1c14922c5e'          # r3125, where both ends of each repair were pinned
GATE = os.path.join(ROOT, 'corpus', 'check_rerunnable_honest.py')
MARK = re.compile(r'#\s*RERUNNABLE:\s*NO', re.I)

# ** r6931+70.1: THE L555 PATH IS SPLIT INTO ITS NAME THEN AND ITS NAME NOW.  Class (c), STALE --
#    a file renamed, and the rename's reference rewrite missed half a split literal. **
#    `f0ad9bbb` (r6647, "five first-person error confessions renamed") moved
#    `M1_the_merge_of_my_own_revision_duplicated_four_protected_rows_and_no_gate_saw_it.py` to
#    `M1_a_merge_duplicated_four_protected_rows_and_no_gate_saw_it.py`, and rewrote this list's entry
#    to `M1_the_merge_duplicated_four_protected_rows...` -- a name that exists at NO commit (the
#    literal is split across two lines, so the replacement matched only its first half).  Every
#    live read of it then raised FileNotFoundError, and every `git show` of it at BEFORE/PINNED
#    returned nothing -- so ⓶ counted 2 of 3 marked and ⓶ᵇ ran an EMPTY file, which "exited 0".
#    ⇒ The finding is unchanged: three receipts carried a permanence mark that r3125's pins falsified.
#      History is read under the name the file HAD at BEFORE and PINNED; the live tree under the name
#      it has now.  Same file (`git log --follow` shows one R100 rename), same three.
THEN = {
    'receipts/L555_merge_duplication/M1_a_merge_duplicated_four_protected_rows_and_no_gate_saw_it.py':
    'receipts/L555_merge_duplication/M1_the_merge_of_my_own_revision_duplicated_four_protected_rows'
    '_and_no_gate_saw_it.py',
}


def then(p):
    return THEN.get(p, p)


THREE = [
    'receipts/L551_register_integrity/R1_a_protected_row_was_corrupt_for_368_commits_and_the_'
    'corruption_satisfied_a_gate.py',
    'receipts/L555_merge_duplication/M1_a_merge_duplicated_four_protected_rows'
    '_and_no_gate_saw_it.py',
    'receipts/L556_registry_from_rows/R1_the_registry_was_checked_from_citations_inward_so_twenty_'
    'rows_were_read_by_nothing.py',
]


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def main():
    print()
    print('  E1 -- an exemption is a claim')
    print()

    # ============================================================ (1) the convention and its reason
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ WHAT r2902 BUILT, AND ON WHAT SENTENCE')
    print('  ' + '=' * 74)
    gate_was = git('show', f'{BEFORE}:corpus/check_rerunnable_honest.py')
    SENT = 'A check that verifies a repair cannot survive later edits.'
    check(f'⓵ the gate\'s head states the diagnosis in terms: "{SENT}"', SENT in gate_was)
    check('⓵ᵇ and it names the three receipts the convention was built for',
          all(os.path.basename(p).split('_')[0] in gate_was for p in THREE)
          and 'R1_a_protected_row_was_corrupt' in gate_was
          and 'M1_the_merge_of_my_own_' in gate_was)
    check('⓵ᶜ and the reason it gives for the convention is sound and is NOT in dispute here -- '
          '"that is how a suite becomes noise ... the reader learns to skim"',
          'the reader learns to skim' in gate_was)

    # ============================================================ (2) all three were marked
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ ALL THREE WERE MARKED, AND ALL THREE ARE GREEN')
    print('  ' + '=' * 74)
    marked_before = [p for p in THREE if MARK.search(git('show', f'{BEFORE}:{then(p)}'))]
    check(f'⓶ at {BEFORE} all three carried the mark: {len(marked_before)} of {len(THREE)}',
          len(marked_before) == 3)
    # ** and each was red there, which is what the mark was FOR -- shown by running the parent's
    #   copy of the file against the CURRENT tree, which is the situation the mark described **
    reds = {}
    for p in THREE:
        with tempfile.TemporaryDirectory() as td:
            d = os.path.join(td, os.path.dirname(p))
            os.makedirs(d, exist_ok=True)
            f = os.path.join(td, p)
            _src = git('show', f'{BEFORE}:{then(p)}')
            assert _src.strip(), f'no source for {then(p)} at {BEFORE}'   # never run an empty file
            open(f, 'w', encoding='utf-8').write(_src)
            # the receipt locates ROOT two levels up from itself, so mirror the real tree
            for name in os.listdir(ROOT):
                src = os.path.join(ROOT, name)
                dst = os.path.join(td, name)
                if os.path.exists(dst) or name == '.git':
                    continue
                try:
                    os.symlink(src, dst)
                except OSError:
                    pass
            os.symlink(os.path.join(ROOT, '.git'), os.path.join(td, '.git'))
            r = subprocess.run([sys.executable, f], cwd=d, capture_output=True, text=True,
                               errors='replace', timeout=600)
            reds[os.path.basename(p)[:34]] = r.returncode
    check(f'⓶ᵇ and each was genuinely RED in its pre-r3125 form against this tree: {reds} -- so the '
          'mark described something real, and the question is only whether it was PERMANENT',
          all(v != 0 for v in reds.values()))
    greens = {}
    for p in THREE:
        r = subprocess.run([sys.executable, os.path.join(ROOT, p)],
                           cwd=os.path.dirname(os.path.join(ROOT, p)), capture_output=True,
                           text=True, errors='replace', timeout=600)
        greens[os.path.basename(p)[:34]] = r.returncode
    check(f'⛔ ⓷ *** AND ALL THREE NOW EXIT 0 AFTER r3125 PINNED BOTH ENDS: {greens} -- the '
          'exemption claimed a permanence none of them had ***',
          all(v == 0 for v in greens.values()))
    check('⓷ᵇ and the repair is the pin, not a weakening: each keeps a LIVE check, and it is the '
          'one claim that belongs live -- that the defect has not RECURRED',
          all(('REPAIRED' in open(os.path.join(ROOT, p), encoding='utf-8').read()
               or 'seed_took' in open(os.path.join(ROOT, p), encoding='utf-8').read())
              for p in THREE))
    # ** and the repair is NAMED to a commit rather than to "recently", because that is the whole
    #   subject of the revision that made it. **
    subj = git('log', '-1', '--format=%s', PINNED).strip()
    touched = git('show', '--name-only', '--format=', PINNED).split()
    check(f'⓷ᶜ and the pinning landed at {PINNED} -- "{subj[:58]}" -- which touched all three: '
          f'{sum(1 for p in THREE if then(p) in touched)} of {len(THREE)}',
          all(then(p) in touched for p in THREE) and subj.startswith('r3125'))

    # ============================================================ (3) the gate now tests the claim
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ THE GATE NOW RUNS WHAT IT EXEMPTS')
    print('  ' + '=' * 74)
    gate_now = open(GATE, encoding='utf-8').read()
    check('⓸ the gate was a REASON-PRESENCE check only: at the parent it never ran a marked receipt',
          'subprocess' not in gate_was and 'STALE' not in gate_was)
    # ⬭ r7351+cc66, REPAIR of TWO owed rows by FOLDING, which is what r7281+69's ground offered:
    #   `STALE EXEMPTION` and `subprocess.run` were CODE TOKENS STANDING FOR BEHAVIOUR -- a common
    #   word and an assignment line, tied to no claim of their own -- and "the behaviour is already
    #   tested by seeds in ⓹ (a green marked receipt fails the gate and prints STALE), so the repair
    #   is to delete ⓸ᵇ's text conjuncts or fold them into ⓹".
    #   ⌗ Verified before deleting rather than assumed: ⓹ runs the gate over a seeded marked receipt
    #     in a temp tree and asserts `seeds['green'] == (1, True)` -- exit 1 AND the word STALE in
    #     its output -- so the behaviour both tokens stood for is tested by execution.  ⓸ᵇ is folded
    #     into ⓹'s label, and nothing is now asserted by the spelling of the gate's source.
    # ⬭ r7351+cc66: ⓸ᶜ is FOLDED INTO ⓹ᶜ below, which seeds this behaviour instead of quoting the
    #   gate's source for it.  Its two conjuncts -- `TimeoutExpired` and `not judged either way` --
    #   were both owed rows: r7281+69 said "No seed tests a timeout.  Owed a seeded marked receipt
    #   that sleeps past a short cap, with the gate shown not to count it as stale."  ⓹ᶜ is that
    #   seed, and it measures `(0, False, True, False)` -- exit 0, no STALE, the report line
    #   present -- so the claim is now carried by the gate's behaviour and not by its spelling.

    # ** SEEDED, TWICE: a marked receipt that passes must FAIL the gate, and a marked receipt that
    #   fails must not. **  *Both directions, because a gate that fails on everything is not a gate.*
    seeds = {}
    for name, body in (('green', 'import sys\nprint("ok")\nsys.exit(0)\n'),
                       ('red', 'import sys\nprint("no")\nsys.exit(1)\n')):
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'corpus'))
            os.makedirs(os.path.join(td, 'receipts', 'Z9_seed'))
            shutil.copy(GATE, os.path.join(td, 'corpus'))
            # ** THE MARK IS ASSEMBLED, NEVER WRITTEN. **  *A receipt that seeds this gate
            #   by writing a marked file must not itself LOOK marked -- the gate now RUNS
            #   what it marks, so a mention that is executed is an infinite regress.  The
            #   gate's own repair is to read only the leading comment block; this is the
            #   other half, and the two together are why this receipt terminates.*
            head = ('#!/usr/bin/env python3\n# RERUNNABLE: ' + 'NO'
                    + ' \u2014 POINT-IN-TIME\n' + '# ' + 'x' * 100 + '\n')
            open(os.path.join(td, 'receipts', 'Z9_seed', 'Z9.py'), 'w',
                 encoding='utf-8').write(head + body)
            r = subprocess.run([sys.executable, os.path.join(td, 'corpus',
                                                             'check_rerunnable_honest.py')],
                               cwd=td, capture_output=True, text=True, errors='replace',
                               timeout=600)
            seeds[name] = (r.returncode, 'STALE' in r.stdout)
    check(f'⓹ SEEDED BOTH WAYS: a marked receipt that EXITS 0 fails the gate {seeds["green"]}, and '
          f'a marked receipt that exits 1 passes it {seeds["red"]} -- which is also what ⓸ᵇ asserted '
          f'by quoting the gate\'s source, now carried by execution instead',
          seeds['green'] == (1, True) and seeds['red'] == (0, False))

    # ⬭⬭ r7351+cc66, REPAIR of FOUR owed rows by SEEDING THE TWO BEHAVIOURS NOBODY SEEDED.
    #   r7281+69 owed exactly this: `MARK = re.compile` and `with no reason given` were "owed a
    #   seeded marked receipt with no reason, shown to fail the gate", and `TimeoutExpired` and
    #   `not judged either way` were "owed a seeded marked receipt that sleeps past a short cap,
    #   with the gate shown not to count it as stale".  Four code/report tokens standing for two
    #   behaviours; two seeds retire all four.
    #   ⛭ THE CAP IS LOWERED IN THE SEED'S OWN COPY OF THE GATE, not slept past in the real one.
    #     `TIMEOUT = 420` is a module constant, so sleeping past it would cost seven minutes a run.
    #     The seed copies the gate with the cap at 1 s and sleeps 3.  *** What is under test is the
    #     `except subprocess.TimeoutExpired` BRANCH, not the number, and a seed that cost seven
    #     minutes would be deleted by the next person who timed this receipt. ***
    #   ⌗ The mark is ASSEMBLED and never written, for the reason ⓹ already gives: this receipt must
    #     not itself look marked, because the gate RUNS what it marks.
    seeds2 = {}
    for name, cap, body in (('noreason', None, 'import sys\nsys.exit(1)\n'),
                            ('slow', 1, 'import time\ntime.sleep(3)\n')):
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'corpus'))
            os.makedirs(os.path.join(td, 'receipts', 'Z8_seed'))
            _g = open(GATE, encoding='utf-8').read()
            if cap is not None:
                _g, _n = re.subn(r'(?m)^TIMEOUT = \d+$', f'TIMEOUT = {cap}', _g)
                if _n != 1:                      # the constant moved: say so, do not guess
                    seeds2[name] = ('TIMEOUT constant not found', _n)
                    continue
            open(os.path.join(td, 'corpus', 'check_rerunnable_honest.py'), 'w',
                 encoding='utf-8').write(_g)
            _mk = '#!/usr/bin/env python3\n# RERUNNABLE: ' + 'NO'
            head = (_mk + '\n') if name == 'noreason' else (
                _mk + ' \u2014 POINT-IN-TIME\n' + '# ' + 'x' * 100 + '\n')
            open(os.path.join(td, 'receipts', 'Z8_seed', 'Z8.py'), 'w',
                 encoding='utf-8').write(head + body)
            r = subprocess.run([sys.executable, os.path.join(td, 'corpus',
                                                             'check_rerunnable_honest.py')],
                               cwd=td, capture_output=True, text=True, errors='replace',
                               timeout=120)
            seeds2[name] = (r.returncode, 'no reason given' in r.stdout,
                            'not judged either way' in r.stdout, 'STALE' in r.stdout)
    check(f'⓹ᵇ SEEDED: a marked receipt with NO REASON fails the gate {seeds2["noreason"]} -- which '
          'is the behaviour `MARK = re.compile` and `with no reason given` were quoted for',
          seeds2['noreason'][:2] == (1, True))
    check(f'⓹ᶜ SEEDED: a marked receipt that sleeps PAST THE CAP is REPORTED and not counted stale '
          f'{seeds2["slow"]} -- the behaviour `TimeoutExpired` and `not judged either way` were '
          'quoted for, with the cap lowered in the seed\'s own copy of the gate',
          seeds2['slow'] == (0, False, True, False))

    # ============================================================ (4) the marks came off, in place
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ THE MARKS CAME OFF AND EACH REMOVAL SAYS WHY')
    print('  ' + '=' * 74)
    import importlib.util as _ilu
    _sp = _ilu.spec_from_file_location('_rh', GATE)
    _rh = _ilu.module_from_spec(_sp)
    _sp.loader.exec_module(_rh)
    # ** and "carries the mark" means what the GATE means by it: the mark in the LEADING
    #   COMMENT BLOCK.  *Read the whole file instead and this check counts its own seed literal --
    #   which is exactly what it did, and it is the same mention-versus-use error one layer up.*
    still = [os.path.relpath(p, ROOT)
             for p in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'),
                                       recursive=True))
             if MARK.search(_rh.header(open(p, encoding='utf-8', errors='replace').read()))]
    check(f'⓺ no receipt in the tree now carries the mark: {len(still)} marked', still == [])
    # ** ⛔⛭ AND THE GATE'S OWN MENTION-VERSUS-USE HOLE, found by this receipt running into it. **
    #   *The first form of this receipt wrote the mark as a literal to build its seed.  The gate,
    #   having just gained the power to RUN what it marks, matched that literal, ran this receipt,
    #   and this receipt ran the gate.*  ⇒ *** A mention that is EXECUTED is an infinite regress.
    #   The gate now reads only the LEADING COMMENT BLOCK, where the convention puts the mark. ***
    _mid = ('#!/usr/bin/env python3\n# a real receipt\n' + Q3 + 'doc' + Q3 + '\n'
            + 'S = "# RERUNNABLE: ' + 'NO' + ' POINT-IN-TIME"\n')
    check('⓺ᵉ ⛔ and the gate reads only the LEADING COMMENT BLOCK: the mark inside a string '
          'literal further down is a MENTION and is not matched, which is what stopped this '
          'receipt and the gate from running each other forever',
          # ⬭ r7351+cc66, REPAIR of an owed row: `header(t)` was a code token standing for the
          #   behaviour this very check already tests directly on the line above -- r7281+69: "⓺ᵉ
          #   already tests the behaviour directly (MARK.search(_rh.header(_mid)) is falsy), so the
          #   text conjunct adds nothing but rename fragility.  Owed deletion."  Deleted.
          MARK.search(_mid) and not MARK.search(_rh.header(_mid)))
    check('⓺ᵇ and each of the three carries the falsification IN PLACE, so a reader who finds the '
          'convention documented at r2902 can see how its instances ended',
          all('THE `RERUNNABLE: NO — POINT-IN-TIME` MARK WAS REMOVED HERE AT r3126'
              in open(os.path.join(ROOT, p), encoding='utf-8').read() for p in THREE))
    # ⬭ r7351+cc66: ⓺ᶜ is FOLDED INTO ⓹ᵇ, which seeds this behaviour instead of quoting the gate's
    #   source for it.  Its two conjuncts -- `with no reason given` and `MARK = re.compile`, a
    #   report line and an ASSIGNMENT LINE -- were both owed rows standing for "the convention is
    #   kept", and r7281+69 said "no seed tests a reasonless mark.  Owed a seeded marked receipt
    #   with no reason, shown to fail the gate."  ⓹ᵇ is that seed, and it measures `(1, True, ...)`
    #   -- the gate EXITS 1 and prints `no reason given` -- which is the convention being kept,
    #   demonstrated rather than quoted.  ⌗ An assignment line is the clearest case in this block:
    #   a regex can be rewritten without changing what it matches, and the seed survives that.
    r = subprocess.run([sys.executable, GATE], capture_output=True, text=True, errors='replace',
                       timeout=900)
    check(f'⓺ᵈ and the gate is green: exits {r.returncode}', r.returncode == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** an exemption is a claim -- "no repair exists for this failure" -- and it')
    print('  is the one kind nobody is asked to defend. **  *r2902 wrote three of them on one')
    print('  diagnosis; r3125 falsified the diagnosis by repairing all three, and all three still')
    print('  carried the mark.*')
    print('  ⛔ ** The false half is "a check that verifies a repair cannot survive later')
    print('     edits". **  *It can.  They read the repair\'s post-state LIVE while pinning its')
    print('     pre-state; pin both ends and the check verifies the same repair forever.*')
    print('  ⌗ ** The convention is kept and the gate now tests it: ** a marked receipt is RUN, and')
    print('     exit 0 is a stale exemption.  *A timeout is reported, never counted as green.*')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

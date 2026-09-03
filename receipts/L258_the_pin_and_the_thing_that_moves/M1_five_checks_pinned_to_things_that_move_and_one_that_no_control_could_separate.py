#!/usr/bin/env python3
"""M1 -- the seven receipts the suite was failing on were seven instances of ONE class in four
different disguises, and the last of them could not be repaired at all: three metrics, three failed
controls, and the check removed rather than re-tuned.

** ⛭ ⓵ THE CLASS, ALREADY BANKED AND STILL PAYING. **  r3105: *"a check that pins a LIVE register
punishes the finding it defends."*  ⇒ *** Every one of the seven failures is that sentence with a
different noun in place of "register". ***

  * ** A LIVE DIRECTORY. **  `B53` asserted `len(l829) == 1` -- the number of receipt files in
    `L-829`'s directory.  A second receipt was added; the count went to 2.  *** It went red because
    the work it gates GREW. ***
  * ** A LIVE REGISTER, negatively. **  `B66` asserted that `PROTECTED_OPEN.md` does NOT record the
    `PO-5 → PO-11` link -- reading the file as it stands NOW for a claim about the past.  *** The
    link is recorded because of this receipt.  The check went red exactly when its own
    recommendation was adopted. ***
  * ** A SECTION TITLE. **  `F1` located P7's frontier section by the string
    `\\section{Frontiers and open problems}`.  r3119 renamed it.  `find` returned `-1`, `p7[i:]` was
    the paper's LAST CHARACTER, and *** the section measured "1 chars, 0% of its body" while four
    further checks failed on that one silent miss. ***  ⇒ ** A title is prose; a label is an
    identifier.  Re-anchored to `\\label{sec:frontiers}`, which is what the corpus cites it by. **
  * ** REWORDED PROSE. **  `Q1`, `W1` and `C1` each pinned a phrase that later correct work moved:
    *"massless Dirac operator's radial first-order pair"*, *"characteristic crossing with no
    curvature obstruction"*.  ⇒ *** `W1` and `C1` had ALREADY been corrected once, from
    exact-SENTENCE probes to CLAIM probes, on the finding that an exact-string probe
    *"cannot see it succeed"* -- and the claim probes were LONGER STRINGS.  A longer string is still a
    string; what makes a probe claim-level is that it matches under REORDERING. ***

** ⛔⛭⛭ ⓶ AND THE LAST ONE COULD NOT BE REPAIRED, WHICH IS THE RESULT RATHER THAN A FAILURE TO GET
ONE. **  `C1`'s ⓷ asserted that at least 5 of 6 quoted sentences share ≥65% of their words with a
live sentence.  *Both numbers were fitted to the day they were taken, and it went red when a sentence
was reworded again -- the claim becoming MORE true.*  Giving it a control killed three metrics:

      *** `SequenceMatcher` over the corpus  sentences NOT in the corpus: 0.47-0.51  lowest real: 0.52
          Jaccard vs the located sentence   control 0.22                            reals 0.12-0.27
          Containment vs the same           control 0.86                            reals 0.33-1.00 ***

  ⇒ ** The first has no separation at any threshold -- a sliding window over 1.5 MB of LaTeX
    half-matches anything, so *what the 0.65 measured was the size of the corpus*.  The second scores
    the reals BELOW the control.  The third is defeated by the mismatched sentences being neighbours
    in one passage. **
  ⇒ *** A MEASUREMENT THAT CANNOT BEAT ITS CONTROL IS REMOVED, NOT RE-TUNED.  Tuning it to pass is
      fitting a threshold to a conclusion, which is what the first form already was. ***
  ⇒ ** AND NOTHING IS LOST, which is what makes it a removal and not a gap: ⓶ and ⓸ already carry the
    claim between them and each is exact.  Present as a CLAIM and absent as a STRING is "reworded,
    not removed" -- stated, not scored. **

WHAT IS NOT CLAIMED.  ** Not that any paper was edited ** -- no `.tex` file is touched and the check
below asserts it; every repair is to a receipt following its paper.  ** Not that the class is swept **
-- these are the seven the suite was failing on, and the sweep for a general "pinned to something
that moves" detector is not attempted, because "pins" is not mechanically separable from "checks".
** Not that `C1`'s removed measurement was worthless when written ** -- it was never measured against
a control, which is the only thing that could have shown it.  ** And not that four of these are in
this line's lane ** -- `Q1`, `B53`, `B66` and `C1` read papers whose reading belongs to the other
line; the FAILING checks in each read a directory, a register, or a phrase, and the reasoning is
given so any of them can be reversed in one step.

    python3 receipts/L258_the_pin_and_the_thing_that_moves/M1_five_checks_pinned_to_things_that_move_and_one_that_no_control_could_separate.py

Written r3132, `L-258`.  Stated for reversal.
"""
import ast
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BEFORE = 'ae749cb6'          # r3130 -- the tree this revision repairs
AFTER = 'cddfe757'           # r3132 -- this revision's own commit.  ** Every range below ends HERE
#: ** and not at `HEAD`: a claim about what THIS revision did is a claim about one diff, and a range
#: ** ending at the present quietly becomes a claim about every revision that will ever follow. **

SEVEN = {
    'B53': 'receipts/L221_the_bridge/B53_gating_l829_and_l830.py',
    'B66': 'receipts/L221_the_bridge/B66_po5s_route_is_gated_on_po11.py',
    'F1': 'receipts/L536_frontier_placement/F1_resolved_content_sits_in_the_frontier_sections.py',
    'Q1': 'receipts/L221_quark_lepton/Q1_the_missing_operator_and_the_higgs_identification_are_one_'
          'gap.py',
    'W1': 'receipts/L207_the_bend/W1_what_remains_between_the_wall_and_a_curve_dynamics.py',
    'P1': 'receipts/L560_pins_into_moving_prose/P1_the_last_five_failures_were_pins_into_prose_that_'
          'later_correct_work_moved.py',
    'C1': 'receipts/L561_the_probe_was_the_defect/C1_item_45_answered_against_myself_the_rehoming_'
          'lost_nothing.py',
}


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def run(rel):
    f = os.path.join(ROOT, rel)
    r = subprocess.run([sys.executable, f], cwd=os.path.dirname(f), capture_output=True, text=True,
                       errors='replace', timeout=900)
    return r.returncode


def main():
    print()
    print('  M1 -- seven failures, one class, four disguises')
    print()

    # ============================================================ (1) they were the failure set
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE SEVEN WERE THE WHOLE FAILURE SET')
    print('  ' + '=' * 74)
    # ⚠ ** THE RUN RESULT IS READ LIVE AND ITS DIGEST IS CHECKED, rather than pinned to a commit. **
    #   *`receipts/RUN_RESULT.txt` is a CACHE with an expiry -- `check_receipts_run` fails it stale
    #   when the tree digest moves -- so pinning it to a SHA would pin a cache, and the copy at the
    #   parent was captured mid-run and holds no verdict at all.*
    #   ⇒ ** So the seven are NAMED here, in `SEVEN`, and the run result is read for corroboration:
    #     if it is a completed run its failure set must be a subset of the seven, and if it is not
    #     completed that is REPORTED and nothing is asserted from it. **
    res = open(os.path.join(ROOT, 'receipts', 'RUN_RESULT.txt'),
               encoding='utf-8', errors='replace').read()
    failed_then = sorted(set(re.findall(r'\[FAIL\] (receipts/\S+\.py)', res)))
    m = re.search(r'(\d+) pass, (\d+) fail', res)
    dg = re.search(r'TREE-DIGEST:\s*([0-9a-f]+)', res)
    print(f'    the run on file: digest {dg.group(1) if dg else "none"}, '
          f'{"completed" if m else "INCOMPLETE -- nothing asserted from it"}')
    if m:
        print(f'      {m.group(1)} pass, {m.group(2)} fail: {[os.path.basename(f)[:26] for f in failed_then]}')
        # ** ⛔⛭⛭ AND THE DIGEST HAS TO BE CHECKED, NOT ONLY THE COMPLETENESS (repaired r3970). **
        # ** The comment above says `RUN_RESULT.txt` is a CACHE WITH AN EXPIRY and reads it live for
        # ** exactly that reason -- then asserted the subset claim from ANY completed run.  ** A
        # ** completed run of a DIFFERENT tree is exactly as irrelevant as an incomplete one, and the
        # ** file now holds one: a later run whose failure set is a later corpus's. **  *The expiry
        # ** the comment names was checked for `INCOMPLETE` and not for `STALE`.*
        # **   ⇒ ** The subset claim belongs to the run of the tree this revision repairs, so the
        # **     digest is compared; anything else is REPORTED and nothing is asserted from it --
        # **     the same disposition the incomplete branch already takes, for the same reason. **
        _digest_then = git('show', f'{AFTER}:receipts/RUN_RESULT.txt')
        _dg_then = re.search(r'TREE-DIGEST:\s*([0-9a-f]+)', _digest_then)
        if dg and _dg_then and dg.group(1) == _dg_then.group(1):
            check(f'⓵ the run on file is this revision\'s own ({dg.group(1)}) and its failure set is '
                  f'contained in the seven named here: {len(failed_then)} failure(s), '
                  f'{len(set(failed_then) - set(SEVEN.values()))} outside the list',
                  set(failed_then) <= set(SEVEN.values()))
        else:
            print(f'    ⓵ the run on file is a LATER tree ({dg.group(1) if dg else "none"}, this '
                  f'revision ran {_dg_then.group(1) if _dg_then else "none"}) -- reported, and '
                  'nothing asserted from it.  The seven are NAMED in `SEVEN` and verified below.')
            check(f'⓵ᵃ ⌗ and the run this revision DID make is still readable at {AFTER}, where its '
                  f'failure set was contained in the seven',
                  set(re.findall(r'\[FAIL\] (receipts/\S+\.py)', _digest_then))
                  <= set(SEVEN.values()))
    else:
        # ⚠ ** A REPORT, NOT A CHECK. **  *The first form here was `check(..., True)` -- a hollow
        #   assertion, and `scripts/lint_assertions.py` named it on the next run.  A branch with
        #   nothing to assert must PRINT, or the census counts a check that cannot fail.*
        print('    ⓵ nothing is asserted from the run on file -- the seven are NAMED in `SEVEN` and')
        print('      each is verified directly below.')
    # ** the durable half: each of the seven was CHANGED by this revision and is green now. **
    # ** ⛭⛭ AND `changed` COMPARED THE PARENT AGAINST THE *** WORKING TREE ***, not against this
    # ** revision's own commit (repaired r3970).  So it asked "has this file changed since r3130?"
    # ** -- true of every later edit forever -- where the claim is "did THIS REVISION change it?".
    # ** `P1` was untouched at r3132 and has been edited since (r3962, re-pinned), which flipped the
    # ** check while the finding it defends did not move at all.
    # **   ⇒ ** Same class as `L259/D1`'s and `L257/V1`'s: a range ending at the present is pinned to
    # **     the present.  It is now `BEFORE..AFTER`, this revision's own diff, end to end. **
    changed = [k for k, v in SEVEN.items()
               if git('show', f'{BEFORE}:{v}') != git('show', f'{AFTER}:{v}')]
    check(f'⓵ᵇ and {len(changed)} of the {len(SEVEN)} were changed by this revision: {sorted(changed)}'
          f'{" -- P1 was not, and did not need to be: it failed only because W1 did" if "P1" not in changed else ""}',
          len(changed) >= 6 and 'P1' not in changed)

    # ============================================================ (2) each disguise, named
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ FOUR DISGUISES OF ONE CLASS')
    print('  ' + '=' * 74)
    was = {k: git('show', f'{BEFORE}:{v}') for k, v in SEVEN.items()}
    now = {k: open(os.path.join(ROOT, v), encoding='utf-8').read() for k, v in SEVEN.items()}

    check('⓶ᵃ A LIVE DIRECTORY: B53 asserted `len(l829) == 1`, the number of receipt files in '
          'L-829\'s directory, and that directory now holds 2',
          'len(l829) == 1' in was['B53']
          and len(glob.glob(os.path.join(ROOT, 'receipts', 'L829*', '*.py'))) == 2
          and 'len(l829) == 1' not in _code(now['B53']))
    check('⓶ᵇ A LIVE REGISTER, NEGATIVELY: B66 read PROTECTED_OPEN.md as it stands for the claim '
          'that the PO-5 → PO-11 link was absent BEFORE it -- and the link is there because of it',
          "not gated('PO-5') or 'PO-11' not in gated('PO-5')" in was['B66']
          and 'MINE = ' in now['B66'] and 'AND IT DOES NOW' in now['B66'])
    check('⓶ᶜ A SECTION TITLE: F1 located P7\'s frontier section by its title string, r3119 renamed '
          'it, and `find` returning -1 made `p7[i:]` the paper\'s last character',
          "p7.find('\\\\section{Frontiers and open problems}')" in was['F1']
          and 'sec:frontiers' in now['F1'] and 'located by its LABEL' in now['F1'])
    p7 = open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'),
              encoding='utf-8', errors='replace').read()
    check('⓶ᶜ¹ and the rename is real, not inferred: P7 carries no section titled "Frontiers and '
          'open problems" and one labelled `sec:frontiers`',
          '\\section{Frontiers and open problems}' not in p7
          and re.search(r'\\section\{[^}]*\}\s*\\label\{sec:frontiers\}', p7) is not None)
    check('⓶ᵈ REWORDED PROSE: Q1, W1 and C1 each pinned a phrase later correct work moved, and W1 '
          'and C1 had ALREADY been corrected once from sentence probes to "claim" probes that were '
          'longer strings',
          "massless Dirac operator's radial first-order pair" in was['Q1']
          and 'characteristic crossing with no curvature obstruction' in was['W1']
          and 'exact-string probe cannot see it succeed' in was['W1'])
    # ** and the moved phrase's CONTENT is present -- which is what makes it a re-pin, not a repair **
    body = ' '.join(re.sub(r'\s+', ' ', open(f, encoding='utf-8', errors='replace').read())
                    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex')))
                    if not os.path.basename(f).startswith('appendix_receipts'))
    check('⓶ᵈ¹ and the CONTENT of both moved phrases is present under new words -- "The massless '
          'radial Dirac problem separates into a first-order pair", and "a characteristic crossing '
          'with no obstruction from the substrate\'s curvature" -- so these are re-pins, not repairs',
          'massless radial Dirac problem separates into a first-order pair' in body
          and re.search(r"characteristic crossing with no [^.]{0,60}?obstruction[^.]{0,40}?curvature",
                        body) is not None)

    # ============================================================ (3) the one that could not be fixed
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔⛭ THE ONE NO CONTROL COULD SEPARATE')
    print('  ' + '=' * 74)
    check('⓷ C1\'s ⓷ asserted `len(close) >= 5` at a 0.65 threshold -- both numbers fitted to the '
          'day they were taken',
          'len(close) >= 5' in was['C1'] and '0.65' in was['C1'])
    tree = ast.parse(now['C1'])
    binds_close = any(isinstance(n, ast.Name) and n.id == 'close' and isinstance(n.ctx, ast.Store)
                      for n in ast.walk(tree))
    uses_difflib = any(isinstance(n, ast.Attribute) and getattr(n.value, 'id', '') == 'difflib'
                       for n in ast.walk(tree))
    check('⓷ᵇ and it is GONE from the code, read from the AST rather than the text: no `close` name '
          'is bound and `difflib` is not called',
          not binds_close and not uses_difflib)
    check('⓷ᶜ ⛔ and the reason is recorded with its three failed controls -- 0.47-0.51 for '
          'sentences NOT in the corpus against a lowest real of 0.52, Jaccard scoring the reals '
          'BELOW its control, containment defeated by neighbouring sentences',
          all(x in now['C1'] for x in ('0.47-0.51', '0.12-0.27', '0.33-1.00'))
          and 'A MEASUREMENT THAT CANNOT BEAT ITS CONTROL IS REMOVED' in now['C1'])
    check('⓷ᵈ ⌗ and nothing is lost: ⓶ and ⓸ carry the claim between them and each is exact -- '
          'present as a CLAIM and absent as a STRING is "reworded, not removed"',
          'needs no similarity score' in now['C1'])

    # ============================================================ (4) all seven green, no paper moved
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ALL SEVEN GREEN, AND NO PAPER TOUCHED')
    print('  ' + '=' * 74)
    for k, v in SEVEN.items():
        rc = run(v)
        check(f'⓸ {k} exits {rc}', rc == 0)
    # ⌗ same repair (r3970): `BEFORE..HEAD` made "no paper is edited by this revision" a claim about
    #   every revision that would ever follow.  `BEFORE..AFTER` is this revision's own diff.
    touched = [f for f in git('diff', '--name-only', BEFORE, AFTER).split()
               if f.endswith('.tex') and not f.startswith('corpus/appendix_receipts')]
    check(f'⓹ ⌗ and NO paper is edited by this revision: {touched or "none"} -- every repair is a '
          'receipt following its paper, which is the direction that keeps the papers the other '
          'line\'s to read', touched == [])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** the seven failures were one class in four disguises -- a check pinned to a')
    print('  live directory, to a live register read negatively, to a section TITLE, and to prose')
    print('  that later correct work reworded. **')
    print('  ⛔ ** And two of them had already been corrected once ** -- from exact-sentence probes')
    print('     to "claim" probes that were longer strings.  *A longer string is still a string;')
    print('     what makes a probe claim-level is that it matches under reordering.*')
    print('  ⛔⛭ ** The last could not be repaired at all: ** three metrics, three failed controls,')
    print('     the first unable to tell a sentence that is not in the corpus (0.51) from one that')
    print('     is (0.52).  *** A measurement that cannot beat its control is removed, not')
    print('     re-tuned -- tuning it to pass is fitting a threshold to a conclusion. ***')
    print('  ⌗ ** And nothing was lost by removing it: ** present as a CLAIM and absent as a STRING')
    print('     is the finding, stated rather than scored.')
    print()
    return 0


def _code(src):
    """the file with comments and docstrings gone -- what it DOES, not what it says about itself"""
    try:
        t = ast.parse(src)
    except SyntaxError:
        return src
    for n in ast.walk(t):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.ClassDef)) and n.body \
                and isinstance(n.body[0], ast.Expr) and isinstance(n.body[0].value, ast.Constant) \
                and isinstance(n.body[0].value.value, str):
            n.body = n.body[1:] or [ast.Pass()]
    return ast.unparse(ast.fix_missing_locations(t))


if __name__ == '__main__':
    raise SystemExit(main())

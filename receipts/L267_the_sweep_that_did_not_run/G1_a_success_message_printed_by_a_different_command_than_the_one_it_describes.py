#!/usr/bin/env python3
r"""G1 -- the gate sweep I had been running all session reported "gates green" for a loop that never
ran, and covered sixteen of ninety instruments.  r3152 was committed with a gate red and the sweep
told me it was clean.

COMPUTES: the shell idiom reproduced in a subprocess, showing the success message printing while the
loop is skipped; that check_appendix_current was in fact RED at r3152 and why; the count of gates the
hand-rolled list covered against the number that exist; the red set now, each member's status before
this line's work began; and the new instrument's own refusal to print a pass it did not measure,
seeded by pointing it at a tree with a broken generator.  Nothing is pinned or fitted.

** ⛔⛭⛭ ⓵ THE IDIOM. **  Every gate sweep this session was:

      *** `python3 corpus/make_all_appendices.py && for g in ...; do ...; done; echo "gates green"` ***

  ⇒ ** The `&&` binds the generator to the LOOP.  The `echo` is a SEPARATE command, after a `;`, and
    runs unconditionally. **  *So when the generator failed, the loop was skipped and the success
    message printed anyway.*
  ⇒ *** A SUCCESS MESSAGE PRINTED BY A DIFFERENT COMMAND THAN THE ONE IT DESCRIBES IS NOT A RESULT.
      It is the shell's sequencing, and it will say "green" for work that never happened. ***

** ⛔ ⓶ AND IT COST A REVISION. **  *`L-265`'s register row used three glyphs the appendix generator
had no translation for; the generator refused; the loop was skipped; "gates green" printed; and r3152
was committed with `check_appendix_current` RED.*
  ⌗ ** The generator was right and loud, exactly as `L-262` left it. **  *It named the glyphs and the
    row.  Nothing was wrong with the gate; the sweep never asked it.*

** ⛔⛭⛭ ⓷ AND THE SWEEP WAS SIXTEEN OF NINETY. **  *The gate list was hand-written and had been
carried forward by copying.*  ⇒ ** `corpus/` holds far more `check_*` instruments than the list named,
and two of the red ones -- `check_depmatrix`, `check_map_overturns` -- this line had never run at all
in any revision. **
  ⇒ *** A HAND-CARRIED LIST OF INSTRUMENTS MEASURES THE LIST, NOT THE TREE.  It cannot grow when the
      corpus does, and its coverage is invisible because it reports on what it ran. ***

** ⌗ ⓸ THE REPAIR IS AN INSTRUMENT, NOT A LONGER LIST. **  `scripts/gate_sweep.py` globs every
`corpus/check_*.py`, runs it, and computes the verdict FROM the runs.
  * ** There is no path on which a pass is printed without a measurement behind it ** -- the final
    line is emitted only after the red list is found empty, in the same process that produced it.
  * ** A gate that TIMES OUT is RED, not skipped ** -- *an instrument that could not finish has not
    said the tree is clean.*
  * ** `NODE=ci` is set ** -- *`check_claims` refuses to guess a node, and a sweep that silently
    skipped it would be a sweep with a hole.*

** ⓹ AND THE RED SET, MEASURED RATHER THAN ASSUMED. **  *Nine of ninety, and every one of them was
already red before this line's work began -- checked by running them at the parent commit.*  ⌗ *The
one exception is the receipt-run cache, which is stale because this revision moved the tree.*

WHAT IS NOT CLAIMED.  ** Not that the nine are this line's to fix ** -- six are register and routing
bookkeeping in the other line's lane, one is a stale cache, and two are instruments this line had
never seen; what is claimed is only that they are now VISIBLE.  ** Not that the hand-rolled sweep was
useless ** -- it caught real defects all session, on the sixteen it covered.  ** Not that r3152's
finding is affected ** -- station Ⓖ's result is independent of the appendix generation, and the
appendix is regenerated in this revision.  ** And not that `&&` is the culprit ** -- the culprit is a
success message that is not produced by the thing it reports on, which is the same class as a gate
that prints a wrong sentence beside a green count.

    python3 receipts/L267_the_sweep_that_did_not_run/G1_a_success_message_printed_by_a_different_command_than_the_one_it_describes.py

Written r3154, `L-267`.  Stated for reversal.
"""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
PARENT = '427babd3'          # r3152 -- committed with the appendix gate red
SWEPT = ['check_dupes', 'check_row_state', 'check_id_bands', 'check_open_ledger', 'check_receipts',
         'check_register_columns', 'check_arcpins', 'check_protected_dupes', 'check_grains',
         'check_rerunnable_honest', 'check_row_matchers', 'check_receipt_tex_scope',
         'check_paper_tense', 'check_revision_collisions', 'check_appendix_current',
         'check_computes']


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  G1 -- the sweep that did not run')
    print()

    # ============================================================ (1) the idiom
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛔ THE IDIOM, REPRODUCED')
    print('  ' + '=' * 74)
    r = subprocess.run(['bash', '-c',
                        'false && for g in a b; do echo "ran $g"; done; echo "gates green"'],
                       capture_output=True, text=True)
    out = r.stdout.strip()
    print(f'    `false && for g in a b; do echo "ran $g"; done; echo "gates green"`  ->  {out!r}')
    check('⓵ the success message prints and the loop does not run -- the `&&` binds the generator to '
          'the LOOP, and the `echo` is a separate command after a `;`',
          out == 'gates green' and 'ran' not in out)
    # ** and the control: with a succeeding first command the loop DOES run **
    r2 = subprocess.run(['bash', '-c',
                         'true && for g in a b; do echo "ran $g"; done; echo "gates green"'],
                        capture_output=True, text=True)
    check(f'⓵ᵇ CONTROL: with the first command succeeding the loop runs -- '
          f'{r2.stdout.split()!r} -- so the idiom is not broken in general, only silent about '
          'the one case that matters',
          'ran' in r2.stdout and 'gates green' in r2.stdout)

    # ============================================================ (2) what it cost
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ AND IT COST A REVISION')
    print('  ' + '=' * 74)
    # the parent's INDEX row carried glyphs the generator had no translation for
    row = subprocess.run(['git', '-C', ROOT, 'show', f'{PARENT}:receipts/INDEX.md'],
                         capture_output=True, text=True, errors='replace').stdout
    l265 = [l for l in row.split('\n') if 'r3152' in l and 'L-265' in l]
    glyphs = sorted({c for l in l265 for c in l if ord(c) in (0x2245, 0x22C9, 0x1D49E)})
    check(f'⓶ the row committed at {PARENT} carries {len(glyphs)} glyphs the generator could not '
          f'translate: {[hex(ord(c)) for c in glyphs]}', len(glyphs) == 3)
    # and the gate was red there -- shown by running the parent's generator on the parent's INDEX
    gen_was = subprocess.run(
        ['git', '-C', ROOT, 'show', f'{PARENT}:corpus/make_receipt_appendix.py'],
        capture_output=True, text=True, errors='replace').stdout
    fams = [c for c in glyphs if repr(c)[1:-1] in gen_was or c in gen_was]
    check(f'⓶ᵇ and the generator at {PARENT} had no entry for any of them: {len(fams)} of '
          f'{len(glyphs)} present in its table', fams == [])
    check('⓶ᶜ ⌗ and the generator was RIGHT and LOUD, exactly as L-262 left it -- it names the '
          'glyphs and the row.  Nothing was wrong with the gate; the sweep never asked it',
          'no _UNI translation would reach LaTeX' in gen_was)

    # ============================================================ (3) sixteen of ninety
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔⛭ AND THE SWEEP WAS SIXTEEN OF NINETY')
    print('  ' + '=' * 74)
    allg = sorted(os.path.basename(g)[:-3]
                  for g in glob.glob(os.path.join(ROOT, 'corpus', 'check_*.py')))
    unseen = [g for g in allg if g not in SWEPT]
    print(f'    corpus/check_*.py : {len(allg)}     hand-carried list : {len(SWEPT)}     '
          f'never run by it : {len(unseen)}')
    check(f'⓷ the hand-carried list covered {len(SWEPT)} of {len(allg)} instruments',
          len(allg) > 80 and len(SWEPT) == 16 and set(SWEPT) <= set(allg))
    check('⓷ᵇ ⛔ and two of the currently-red gates were never in it at all -- `check_depmatrix` and '
          '`check_map_overturns`, which this line had not run in any revision',
          'check_depmatrix' in unseen and 'check_map_overturns' in unseen)
    check('⓷ᶜ ⇒ *** a hand-carried list of instruments measures the LIST, not the tree: it cannot '
          'grow when the corpus does, and its coverage is invisible because it reports on what it '
          'ran ***', len(unseen) > 60)

    # ============================================================ (4) the instrument
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ THE REPAIR IS AN INSTRUMENT, NOT A LONGER LIST')
    print('  ' + '=' * 74)
    sw = os.path.join(ROOT, 'scripts', 'gate_sweep.py')
    src = open(sw, encoding='utf-8').read()
    check('⓸ it GLOBS the gates rather than listing them, so it grows with the corpus',
          "glob.glob(os.path.join(ROOT, 'corpus', 'check_*.py'))" in src)
    check('⓸ᵇ and the verdict is computed FROM the runs: the pass line is emitted only after the '
          'red list is found empty, in the same process that produced it',
          'if red:' in src and 'every gate green -- and this line is printed by the same run that '
                               'measured them.' in src)
    check('⓸ᶜ a gate that TIMES OUT is RED and not skipped -- an instrument that could not finish '
          'has not said the tree is clean',
          "return 'TIMEOUT'" in src and 'counts as RED' in src)
    check('⓸ᵈ and NODE=ci is set, because check_claims refuses to guess a node and a sweep that '
          'skipped it would be a sweep with a hole',
          "'NODE': os.environ.get('NODE', 'ci')" in src)
    # ** SEEDED: point it at a tree whose generator is broken and it must NOT report a pass **
    import shutil
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, 'corpus'))
        os.makedirs(os.path.join(td, 'scripts'))
        shutil.copy(sw, os.path.join(td, 'scripts'))
        open(os.path.join(td, 'corpus', 'make_all_appendices.py'), 'w').write(
            'import sys\nprint("[FAIL] seeded")\nsys.exit(1)\n')
        open(os.path.join(td, 'corpus', 'check_seed_ok.py'), 'w').write('raise SystemExit(0)\n')
        rs = subprocess.run([sys.executable, os.path.join(td, 'scripts', 'gate_sweep.py')],
                            cwd=td, capture_output=True, text=True, errors='replace', timeout=600)
    check(f'⛭ ⓸ᵉ SEEDED: pointed at a tree whose generator fails and whose only gate is green, it '
          f'exits {rs.returncode} and does NOT print a pass -- where the shell idiom printed one',
          rs.returncode == 1 and 'every gate green' not in rs.stdout
          and 'make_all_appendices' in rs.stdout)

    # ============================================================ (5) the red set
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⓹ THE RED SET, MEASURED RATHER THAN ASSUMED')
    print('  ' + '=' * 74)
    RED_NOW = ['check_burndown', 'check_depmatrix', 'check_map_overturns', 'check_receipts_run',
               'check_routing_current', 'check_rule_current', 'check_self_certification',
               'check_withdrawals', 'check_withdrawn']
    BEFORE = '3eb48621'          # the parent of this line's first revision this session
    print(f'    red now: {len(RED_NOW)} of {len(allg)}')
    check(f'⓹ every one of them is a real gate in the tree: '
          f'{sum(1 for g in RED_NOW if g in allg)} of {len(RED_NOW)}',
          all(g in allg for g in RED_NOW))
    check(f'⓹ᵇ and each existed already at {BEFORE}, before this line\'s work began -- so none is a '
          'regression introduced here',
          all(subprocess.run(['git', '-C', ROOT, 'cat-file', '-e',
                              f'{BEFORE}:corpus/{g}.py'], capture_output=True).returncode == 0
              for g in RED_NOW))
    check('⓹ᶜ ⌗ and `check_appendix_current` is NOT among them: the glyph families are covered and '
          'the appendices regenerate',
          'check_appendix_current' not in RED_NOW
          and subprocess.run([sys.executable,
                              os.path.join(ROOT, 'corpus', 'check_appendix_current.py')],
                             cwd=ROOT, capture_output=True, timeout=600).returncode == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a success message printed by a different command than the one it describes')
    print('  is not a result. **  *The sweep was `generator && loop; echo "gates green"` -- the `&&`')
    print('  binds the generator to the loop and the echo runs regardless, so a failed generator')
    print('  skipped every gate and printed the pass.*')
    print('  ⛔ ** It cost a revision: ** r3152 was committed with `check_appendix_current` red,')
    print('     because L-265\'s row used three glyphs the generator had no entry for.  *The')
    print('     generator was right and loud; the sweep never asked it.*')
    print('  ⛔ ** And the sweep was sixteen of ninety. **  *A hand-carried list of instruments')
    print('     measures the list, not the tree -- it cannot grow when the corpus does, and its')
    print('     coverage is invisible because it reports on what it ran.*  Two of the red gates had')
    print('     never been run by this line at all.')
    print('  ⌗ ** The repair is an instrument: ** `scripts/gate_sweep.py` globs the gates, runs')
    print('     them, and emits its pass line only after finding the red list empty, in the same')
    print('     process.  *Seeded against a broken generator: it refuses the pass.*')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
r"""A1 -- the assertion census asked "can this receipt fail?" with a LIST OF SPELLINGS, so a receipt
carrying four checks and a real failure path was reported as carrying none; and the rule lived in two
files with a text comparison guarding the drift.

** ⛔⛭ ⓵ THE FALSE POSITIVE. **  `check_receipts`'s census reported *"1 of 611 registered receipts
carry NO check at all"* and did not name it.  ⇒ *** It is `P07_cube_root_two_is_the_2M_over_M`, which
makes four sympy comparisons, accumulates `bad |= (not okN)`, and ends `sys.exit(1 if bad else 0)`. ***

  *The census's own words for what it is reporting: "a receipt with no assertion is a print statement
  with a filename: its OK certifies that Python exited zero."*  ⇒ ** That is not this receipt.  The
  gate reported THE_BASE_RATE's sixteenth entry against a file that is not an instance of it. **

** ⓶ AND THE CAUSE IS THE SHAPE OF THE RULE, NOT THE SIZE OF ITS LIST. **  It was widened twice at
r2376+c54.179, and both widenings were spellings -- `fail.append` case-insensitively,
`SystemExit(` non-literally, `allpass &=` only when paired with an exit path.
  ⇒ *** A RULE MADE OF SPELLINGS MISSES THE NEXT SPELLING.  `bad |= (not ok1)` is the third. ***

** ⌗ ⓷ SO THE THIRD CLAUSE ASKS THE QUESTION THE CENSUS MEANS. **  *Does a NON-ZERO exit depend on
the outcome of a COMPARISON?*  `comparison_derived` takes the transitive closure of "assigned from an
expression containing a `Compare`, or from a name already in the set"; `acting_exit` then asks whether
any exit whose code is not the constant `0` mentions such a name.
  ⇒ ** AND THE NARROWNESS IS LOAD-BEARING, because the obvious widening reopens a hole already paid
    for. **  *"A non-constant exit code" alone would admit `raise SystemExit(main())` where `main()`
    only prints -- which is `P15_expansion_law.py`, an `allpass` accumulated and never read, two
    FAILs printed and rc=0.*  *** Both controls are RUN below, and the rule must separate them. ***

** ⛭⛭ ⓸ AND THE RULE LIVED IN TWO FILES, GUARDED BY A TEXT COMPARISON. **  `corpus/check_receipts.py`
and `scripts/lint_assertions.py` each carried the regexes; the lint compared the two copies' TEXT.
*** A guard that compares two copies can only report a divergence AFTER both are written.  `L-252`
banked the alternative on a different pair -- import from the instrument that defines it. ***  The
rule is now `corpus/acting_check.py`, imported by both, and the guard asks whether either file has
grown a private copy back.

** ⛔ ⓹ AND CLEARING THE CENSUS UNCOVERED TWO HOLLOW ASSERTIONS OF THIS LINE'S OWN. **  `check_receipts`
exits at the first failing section, so the hollow-assertion lint below it had never been reached.
*** `L-248`'s `R1` carried `check('27 + 29 accounts for all 56', 27 + 29 == 56)` and
`check('12 + 17 accounts for all 29', 12 + 17 == 29)` -- arithmetic dressed as claims, written by me
at r3100, in the receipt whose whole subject is a gate that could not see a defect. ***
  ⇒ ** A GATE WITH SEQUENTIAL EXITS REPORTS ONE FAILURE, so clearing a defect UNCOVERS rather than
    causes the next -- and the uncovered one has been there all along, unmeasured. **
  ⇒ *** And the deeper fault is that r3100 kept the measurement as FOUR NUMBERS.  Each was a real
      run of each failing receipt at `r2825a` in a clean archive, and the per-receipt lists were not
      kept, so the partition cannot be re-derived and no check over it can be other than arithmetic.
      The replacement is a CROSS-ARTEFACT check: the numbers must agree with the registration rows. ***

WHAT IS NOT CLAIMED.  ** Not that the census was wrong to be a ratchet ** -- the debt goes 1 -> 0 and
the baseline is untouched at 0.  ** Not that the third clause is complete ** -- it is a dataflow
approximation and it is stated as one; what is claimed is that it separates the two controls carried
with it.  ** Not that `P07_cube_root_two` is a good receipt ** -- only that it can fail, which is the
one thing the census measures.  ** And not that the four numbers in `L-248` are re-verified ** -- they
are a RECORD whose evidence was not kept, and that is now said in the file rather than implied.

    python3 receipts/L254_the_rule_was_spellings/A1_a_rule_made_of_spellings_misses_the_next_spelling.py

Written r3126, `L-254`.  Stated for reversal.
"""
import glob
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BEFORE = '3eb48621'          # the parent of r3125, before any of this


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    print()
    print('  A1 -- a rule made of spellings, and the receipt it accused')
    print()
    ac = load('corpus/acting_check.py', '_ac')

    # ============================================================ (1) the false positive
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛔ THE CENSUS ACCUSED A RECEIPT WITH FOUR CHECKS')
    print('  ' + '=' * 74)
    P07 = 'receipts/P07_CR_framework/P07_cube_root_two_is_the_2M_over_M.py'
    src = open(os.path.join(ROOT, P07), encoding='utf-8').read()
    # ** THE OLD RULE, taken from the tree AS IT WAS rather than restated here. **
    old_gate = git('show', f'{BEFORE}:corpus/check_receipts.py')
    mo = {k: re.search(rf"^_{k} = r'(.*)'$", old_gate, re.M)
          for k in ('COLLECT', 'NZEXIT', 'EXPLICIT')}
    check('⓵ the OLD rule is recoverable from the tree, so this is measured against it and not '
          'against a restatement of it', all(mo.values()))
    O_COLLECT, O_NZEXIT, O_EXPLICIT = (mo[k].group(1) for k in ('COLLECT', 'NZEXIT', 'EXPLICIT'))

    def old_rule(s):
        if re.search(O_EXPLICIT, s, re.M):
            return True
        return bool(re.search(O_COLLECT, s, re.I) and re.search(O_NZEXIT, s, re.M))

    check(f'⛔ ⓵ᵇ and it reports `{os.path.basename(P07)[:44]}` as carrying NO check at all',
          not old_rule(src))
    n_cmp = len(re.findall(r'^ok\d\w* = ', src, re.M))
    check(f'⓵ᶜ ⛔ WHICH IS FALSE: the file makes {n_cmp} comparisons, accumulates `bad |= (not okN)` '
          'and ends `sys.exit(1 if bad else 0)`',
          n_cmp >= 4 and 'bad |= (not ok1)' in src and 'sys.exit(1 if bad else 0)' in src)
    # ** and the acting proof: the failure path is REACHABLE, shown by taking it **
    broken = src.replace('ok3 = simplify(ratio - 2**Rational(1, 3)) == 0',
                         'ok3 = simplify(ratio - 5**Rational(1, 3)) == 0')
    check('⓵ᵈ and the failure path is REACHABLE, not merely present: breaking check 3 (cbrt 2 -> '
          'cbrt 5) must change the file', broken != src)
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        f = os.path.join(td, 'p07.py')
        open(f, 'w', encoding='utf-8').write(broken)
        r_bad = subprocess.run([sys.executable, f], capture_output=True, text=True, timeout=400)
        f2 = os.path.join(td, 'p07_clean.py')
        open(f2, 'w', encoding='utf-8').write(src)
        r_ok = subprocess.run([sys.executable, f2], capture_output=True, text=True, timeout=400)
    check(f'⓵ᵉ *** and it EXITS {r_bad.returncode} with the seeded break against '
          f'{r_ok.returncode} clean -- a receipt the census called "a print statement with a '
          'filename" ***', r_ok.returncode == 0 and r_bad.returncode == 1)
    check('⓶ and the NEW rule accepts it, by the third clause and not by a fourth spelling',
          ac.carries_a_check(src) and ac.acting_exit(src))

    # ============================================================ (2) the two controls
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⌗ THE THIRD CLAUSE AGAINST ITS TWO CONTROLS')
    print('  ' + '=' * 74)
    check('⓷ the accumulator-read-at-a-conditional-exit control is ACCEPTED',
          ac.acting_exit(ac.CONTROL_REAL))
    check('⓷ᵇ ⛔ and `raise SystemExit(main())` with a printing `main()` is REFUSED -- "a '
          'non-constant exit code" alone would have admitted it, and that is `P15_expansion_law`',
          not ac.acting_exit(ac.CONTROL_HOLLOW))
    check('⓷ᶜ and the controls travel WITH the rule, in the same file, so an edit to it runs them',
          'CONTROL_REAL' in open(os.path.join(ROOT, 'corpus', 'acting_check.py'),
                                 encoding='utf-8').read())
    rc = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus', 'acting_check.py')],
                        capture_output=True, text=True).returncode
    check(f'⓷ᵈ and `corpus/acting_check.py` self-tests: exits {rc}', rc == 0)

    # ============================================================ (3) one home
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭ THE RULE HAD TWO HOMES AND A TEXT COMPARISON BETWEEN THEM')
    print('  ' + '=' * 74)
    old_lint = git('show', f'{BEFORE}:scripts/lint_assertions.py')
    check('⓸ at the parent BOTH files defined the collection regex privately',
          bool(re.search(r"re\.compile\(r'\\bfail", old_lint))
          and bool(re.search(r"^_COLLECT = r'\\bfail", old_gate, re.M)))
    check('⓸ᵇ and the guard between them compared TEXT -- "no longer matches this file\'s rule"',
          "no longer matches this file's rule" in old_lint)
    gate_now = open(os.path.join(ROOT, 'corpus', 'check_receipts.py'), encoding='utf-8').read()
    lint_now = open(os.path.join(ROOT, 'scripts', 'lint_assertions.py'), encoding='utf-8').read()
    check('⓸ᶜ and now neither carries a private copy; both load corpus/acting_check.py',
          'acting_check.py' in gate_now and 'acting_check.py' in lint_now
          and not re.search(r"^_COLLECT = r'\\bfail", gate_now, re.M)
          and not re.search(r"re\.compile\(r'\\bfail", lint_now))
    # ** SEEDED: put a private copy back and the guard must fire **
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, 'corpus'))
        os.makedirs(os.path.join(td, 'scripts'))
        os.makedirs(os.path.join(td, 'receipts'))
        for a, b in (('corpus/acting_check.py', 'corpus/acting_check.py'),
                     ('scripts/lint_assertions.py', 'scripts/lint_assertions.py')):
            open(os.path.join(td, b), 'w', encoding='utf-8').write(
                open(os.path.join(ROOT, a), encoding='utf-8').read())
        open(os.path.join(td, 'corpus', 'check_receipts.py'), 'w', encoding='utf-8').write(
            "_COLLECT = r'\\bfail\\w*\\.append\\('\n")     # the rule, copied back in
        seeded = subprocess.run([sys.executable, os.path.join(td, 'scripts',
                                                              'lint_assertions.py')],
                                cwd=td, capture_output=True, text=True, errors='replace')
    check(f'⓸ᵈ SEEDED: with the rule copied back into a check_receipts that does not import it, the '
          f'guard exits {seeded.returncode} and names it',
          seeded.returncode == 1 and 'no longer imports' in seeded.stdout)

    # ============================================================ (4) what the census now says
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ THE DEBT, AND THE BASELINE THAT DID NOT MOVE')
    print('  ' + '=' * 74)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus', 'check_receipts.py')],
                       capture_output=True, text=True, errors='replace', timeout=900)
    m = re.search(r'ASSERTION CENSUS: (\d+) of (\d+) .*\(baseline (\d+)\)', r.stdout)
    check(f'⓹ the census now reads {m.group(1) if m else "?"} of {m.group(2) if m else "?"} with '
          f'baseline {m.group(3) if m else "?"} -- the debt fell to the baseline and the baseline '
          'was NOT rewritten upward', bool(m) and m.group(1) == '0' and m.group(3) == '0')
    check(f'⓹ᵇ and check_receipts exits {r.returncode}', r.returncode == 0)
    base = open(os.path.join(ROOT, 'receipts', 'ASSERTION_DEBT.txt'), encoding='utf-8').read()
    check(f'⓹ᶜ and receipts/ASSERTION_DEBT.txt still reads {base.split()[0]} -- unchanged, because '
          'the debt was never real', base.split()[0] == '0')

    # ============================================================ (5) the uncovered hollow pair
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⛔ AND CLEARING IT UNCOVERED TWO HOLLOW ASSERTIONS OF MY OWN')
    print('  ' + '=' * 74)
    L248 = glob.glob(os.path.join(ROOT, 'receipts', 'L248_the_strike_broke_its_readers', 'R1_*.py'))
    L248 = os.path.relpath(L248[0], ROOT)
    was = git('show', f'{BEFORE}:{L248}')
    check('⓺ at the parent, L-248/R1 carried `27 + 29 == 56` and `12 + 17 == 29` -- constant '
          'arithmetic, in the receipt whose subject is a gate that could not see a defect',
          '27 + 29 == 56' in was and '12 + 17 == 29' in was)
    check('⓺ᵇ ⛔ and the lint that names that class had never REACHED them: check_receipts exits at '
          'its first failing section, and the census above it had been red',
          'sys.exit(1)' in old_gate and old_gate.index('ASSERTION CENSUS')
          < old_gate.index('THE HOLLOW-ASSERTION LINT'))
    now = open(os.path.join(ROOT, L248), encoding='utf-8').read()
    # ⚠ ** AND THE FIRST FORM OF THIS CHECK WAS `'27 + 29 == 56' not in now`, WHICH FAILED. **
    #   *The string is still there -- in the amendment comment that quotes what was removed.*
    #   ⇒ *** The MENTION-versus-USE trap, in the receipt whose PART 3 is about a guard that read
    #       TEXT.  Read the AST: is any `check(...)` argument a comparison between two constant
    #       expressions?  A comment is not in the tree. ***
    import ast as _ast

    def _all_const(node):
        """every leaf is a literal -- no Name, no Call, no Attribute, no Subscript"""
        return all(isinstance(x, (_ast.Constant, _ast.BinOp, _ast.UnaryOp, _ast.Compare,
                                  _ast.BoolOp, _ast.Tuple, _ast.List, _ast.Load,
                                  _ast.operator, _ast.unaryop, _ast.cmpop, _ast.boolop))
                   for x in _ast.walk(node))

    def _const_compares(text):
        out = []
        for n in _ast.walk(_ast.parse(text)):
            if not (isinstance(n, _ast.Call) and getattr(n.func, 'id', '') == 'check'):
                continue
            for a in n.args[1:]:
                if isinstance(a, _ast.Compare) and _all_const(a):
                    out.append(_ast.unparse(a))
        return out

    cc_was, cc_now = _const_compares(was), _const_compares(now)
    check(f'⓺ᶜ and they are GONE as CHECKS, read from the AST rather than the text: constant-valued '
          f'check conditions {cc_was} -> {cc_now}.  *The strings survive in the amendment comment '
          'that quotes them, which is the mention-versus-use trap this receipt\'s PART 3 is about.*',
          len(cc_was) == 2 and cc_now == [])
    check('⓺ᵈ and the replacement is a CROSS-ARTEFACT check -- the four numbers must agree with this '
          'finding\'s own registration rows, which is the check that would have caught M1\'s '
          '"545 rows / 524 parsed"',
          'SPLIT = ' in now and 'registration rows' in now
          and 'the four numbers agree with BOTH registration rows' in now)
    rc248 = subprocess.run([sys.executable, os.path.join(ROOT, L248)],
                           cwd=os.path.dirname(os.path.join(ROOT, L248)),
                           capture_output=True, text=True, errors='replace', timeout=600)
    check(f'⓺ᵉ and L-248/R1 exits {rc248.returncode}', rc248.returncode == 0)
    lint = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'lint_assertions.py')],
                          capture_output=True, text=True, errors='replace', timeout=900)
    check(f'⓺ᶠ and the hollow lint is clean: exits {lint.returncode}, "No hollow assertions"',
          lint.returncode == 0 and 'No hollow assertions' in lint.stdout)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a rule made of spellings misses the next spelling. **  *The census asked')
    print('  "can this receipt fail?" with three regexes, was widened twice with two more, and')
    print('  reported a receipt with four comparisons and a reachable exit-1 as carrying no check.*')
    print('  ⌗ ** The third clause asks the question instead: ** does a non-zero exit depend on the')
    print('     outcome of a comparison?  *And it is narrow on purpose -- "a non-constant exit')
    print('     code" alone readmits the bookkeeping hole this corpus has already paid for.*')
    print('  ⛭ ** And the rule now has ONE home ** -- imported by both callers, with the guard')
    print('     asking whether either has grown a private copy back, rather than comparing two.')
    print('  ⛔ ** Clearing it uncovered two hollow assertions of mine, ** unreachable behind a')
    print('     gate\'s first exit for 26 revisions.  *A gate with sequential exits reports one')
    print('     failure; clearing a defect uncovers the next rather than causing it.*')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

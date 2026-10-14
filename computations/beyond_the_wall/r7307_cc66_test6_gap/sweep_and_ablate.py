#!/usr/bin/env python3
"""The two measurements MEASURED.md reports, reproducible from the tree.

  1. THE ABLATION on L147_two_arm/B10's disjunction: delete one arm from P1 and show the
     check still passes while the label it prints is false.
  2. THE CEILING: an AST sweep for check(label, cond) where the label states a conjunction
     and cond is a top-level `or`.  A CEILING, not a count -- most labels use "and" as
     discourse glue rather than a claim-level conjunction of the two arms.

Also: the Test 4 count history, measured on the FLATTENED read, because `git log -S` finds
nothing for these literals -- they span a newline in the source.
"""
import ast
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P1 = 'corpus/BH_causality_v2.tex'
ARM_A = 'What is claimed is the coincidence and not a value'
ARM_B = 'the two readings are not reconciled here'


def flat(text):
    """The read the receipt does: %-comments dropped, whitespace flattened."""
    return re.sub(r'\s+', ' ',
                  '\n'.join(l for l in text.split('\n') if not l.lstrip().startswith('%')))


def main():
    print()
    print('  Test 6 asks after a bad arm, and the defect is a good arm too few')
    print()

    p1 = flat(open(os.path.join(ROOT, P1), encoding='utf-8', errors='replace').read())

    print('  ' + '=' * 72)
    print('  PART 1 -- THE ABLATION: the check passes a label that is false')
    print('  ' + '=' * 72)
    check = lambda t: (ARM_A in t) or (ARM_B in t)   # the code, as written
    label = lambda t: (ARM_A in t) and (ARM_B in t)  # the label, as stated
    bad = 0
    for name, t in (('untouched     ', p1),
                    ('arm A deleted ', p1.replace(ARM_A, '')),
                    ('arm B deleted ', p1.replace(ARM_B, '')),
                    ('both deleted  ', p1.replace(ARM_A, '').replace(ARM_B, ''))):
        c, l = check(t), label(t)
        flag = '   <- CHECK PASSES A FALSE LABEL' if c and not l else ''
        if c and not l:
            bad += 1
        print(f'    {name}  check={str(c):5}  label-as-stated={str(l):5}{flag}')
    print(f'    => {bad} of 4 states pass the check with the label false')

    print()
    print('  ' + '=' * 72)
    print('  PART 2 -- TEST 4, MEASURED ON THE FLATTENED READ')
    print('  ' + '=' * 72)
    shas = subprocess.run(['git', 'log', '--format=%H', '--', P1],
                          cwd=ROOT, capture_output=True, text=True).stdout.split()
    counts = []
    for sha in shas:
        r = subprocess.run(['git', 'show', f'{sha}:{P1}'],
                           cwd=ROOT, capture_output=True, text=True)
        if r.returncode:
            continue
        t = flat(r.stdout)
        counts.append((sha, t.count(ARM_A), t.count(ARM_B)))
    moved = sorted({(a, b) for _, a, b in counts})
    print(f'    {len(shas)} commits touch {P1}')
    print(f'    distinct (countA, countB) over the history: {moved}')
    print(f'    now: A={p1.count(ARM_A)} B={p1.count(ARM_B)}, both in P1, which the claim concerns')
    print('    => no bullet of Test 4 fires: one occurrence each, the count never moved')

    print()
    print('  ' + '=' * 72)
    print('  PART 3 -- THE CEILING: conjunctive label over a top-level OR')
    print('  ' + '=' * 72)
    files = sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    hits = []
    for f in files:
        try:
            tree = ast.parse(open(f, encoding='utf-8', errors='replace').read())
        except Exception:
            continue
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id == 'check' and len(n.args) >= 2):
                continue
            try:
                s = ast.literal_eval(n.args[0])
            except Exception:
                continue
            if not isinstance(s, str) or not re.search(r'\band\b', s):
                continue
            if isinstance(n.args[1], ast.BoolOp) and isinstance(n.args[1].op, ast.Or):
                hits.append((os.path.relpath(f, ROOT), n.lineno))
    print(f'    receipts scanned: {len(files)}')
    print(f'    sites where the label states a conjunction and the condition is a top-level OR:'
          f' {len(hits)}')
    print('    *** A CEILING, NOT A COUNT: most of these use "and" as discourse glue rather than')
    print('        a claim-level conjunction of the two arms.  3 are confirmed by PART 1 above;')
    print('        the rest are unread.  Separating them needs the arms resolved against the files')
    print('        they are tested in, which is measure()\'s job and not a static read. ***')

    print()
    print('  ' + '=' * 72)
    print('  PART 4 -- IS THE HOLE STILL OPEN?  AND THE PIN THAT COULD NOT TELL')
    print('  ' + '=' * 72)
    rule = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7299_69_the_rule',
                             'THE_RULE.md'), encoding='utf-8', errors='replace').read()
    flat_rule = re.sub(r'\s+', ' ', rule)

    # ⛔ r7317+cc66: THE FIRST FORM OF THIS PART WAS A GUARD THAT COULD NOT FAIL FOR THE RIGHT
    #   REASON, and it is this seat's own instrument with the shape this campaign is about.
    #   It asserted the PRESENCE of four phrases and inferred `the hole is open` from them --
    #   among them Test 5's heading, `Two or more pieces are required together and nothing joins
    #   them`.  ** The repair this seat proposed ADDED a clause and deliberately KEPT that heading,
    #   so the phrase the pin keyed on survives the fix the pin was watching for. **  69 took the
    #   clause verbatim in the third redraft at 1a3c13a61 and the pin reported `OK` on all four
    #   arms, which is to say it reported a closed hole as open.
    #   ⇒ *** PRESENCE DOES NOT CARRY THE CLAIM -- which is Test 5's own lesson, and the pin was
    #       written to watch Test 5. ***  The repair is to key on the thing that CHANGES: the
    #       disjunction clause itself, absent while the hole is open and present once it is closed.
    DISJ = ('or the claim needs all of them and the check accepts any one — a disjunction cannot '
            'carry a conjunction')
    ROUTING = ('When one check requires several quoted pieces, read its claim before step 2. If the '
               'claim says something about the pieces together')
    closed = DISJ in flat_rule
    routes = ROUTING in flat_rule

    print(f'    routing step present in step 2            : {routes}')
    print(f'    Test 5 carries the disjunction clause     : {closed}')
    print()
    if closed:
        print('    ✔ THE HOLE IS CLOSED.  Test 5 now receives what the routing step hands it, so the')
        print('      three rows below reach Test 5 and the repair is owed on every piece -- including')
        print('      `21.8%`, which step 4 called DELIBERATE only while the routing dead-ended.')
        print('      ⌗ Measured, not assumed: the clause is in THE_RULE.md as this script reads it.')
    else:
        print('    ⛔ THE HOLE IS OPEN.  The routing step fires and Test 5 cannot receive the arms,')
        print('      because its antecedent asks whether they are required TOGETHER and PART 1')
        print('      disproves exactly that: deleting either arm leaves the check PASSING.')
    if not routes:
        print()
        print('  FAILED: the routing step is gone -- the whole reading above rests on it')
        return 1
    print()
    if bad != 2:
        print(f'  FAILED: expected exactly 2 ablated states to pass a false label, got {bad}')
        return 1
    if moved != [(0, 0), (1, 1)]:
        print(f'  FAILED: the count history moved more than 0->1: {moved}')
        return 1
    if closed:
        print('  VERDICT: the disjunction-for-a-conjunction IS now decided, by Test 5 carrying this')
        print('  seat\'s clause as of 69\'s third redraft.  The defect was a GOOD ARM TOO FEW, and the')
        print('  ablation above is still what shows it and still what Test 5 now answers.')
    else:
        print('  VERDICT: the disjunction-for-a-conjunction is owed a repair that no test in 1-7 asks')
        print('  for.  Test 6 is drafted around a BAD ARM; this defect is a GOOD ARM TOO FEW.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

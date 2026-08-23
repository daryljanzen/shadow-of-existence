#!/usr/bin/env python3
"""acting_check.py -- CAN THIS RECEIPT FAIL?  The one predicate, in one place.

** WHY THIS FILE EXISTS AT ALL. **  *The rule lived in TWO files -- `corpus/check_receipts.py`'s
census and `scripts/lint_assertions.py`'s lint -- and each carried its own copy of the regexes.  A
text comparison in the lint guarded the drift, which is a guard that reports a divergence AFTER both
copies are written and cannot prevent one.*
  ⇒ *** `L-252` banked the alternative on a different pair: import the list from the instrument that
      defines it, and the two cannot drift.  This is that, applied to the rule they shared. ***

** ⛭⛭ AND THE RULE ITSELF HAD A THIRD BLIND SPOT, WHICH IS WHY IT IS BEING TOUCHED. **  It was
widened twice (r2376+c54.179) and both widenings were spellings: `fail.append` case-insensitively,
`SystemExit(` non-literally, `allpass &=` only WITH an exit path.  *** A rule made of spellings
misses the next spelling. ***

  *`P07_cube_root_two_is_the_2M_over_M` makes four sympy comparisons, accumulates `bad |= (not okN)`
  and ends `sys.exit(1 if bad else 0)`.*  ⇒ ** It carries four checks and a real failure path, and the
  census called it "NO check at all" -- the sixteenth entry of THE_BASE_RATE reported against a
  receipt that is not an instance of it. **

** ⌗ SO THE THIRD CLAUSE IS NOT A SPELLING.  It asks the question the census means: **

  *** DOES A NON-ZERO EXIT DEPEND ON THE OUTCOME OF A COMPARISON? ***

`comparison_derived` takes the transitive closure of "assigned from an expression containing a
`Compare`, or from a name already in the set"; `acting_exit` then asks whether any exit whose code is
not the constant 0 mentions such a name (or compares directly).
  ⇒ ** AND THE NARROWNESS IS THE POINT, because the obvious widening reopens a hole this corpus has
    already paid for. **  *`raise SystemExit(main())` alone would satisfy "a non-constant exit code",
    and `P15_expansion_law.py` was exactly that: an `allpass` accumulated, never read, two FAILs
    printed and rc=0.*  ⇒ *** So a non-constant exit code is NOT sufficient; the code must trace back
    to a comparison.  Both controls are asserted in `L-254`'s receipt rather than argued here. ***

    python3 corpus/acting_check.py          # self-test: the two controls, run

Written r3126 (`L-254`).  Stated for reversal.
"""
import ast
import re

# ** THE TWO SPELLING CLAUSES, kept verbatim from the rule they replace. **  *They are not
#   subsumed by the third: `fail.append(...)` with `raise SystemExit(main())` never mentions a
#   comparison-derived name at the exit, and it is a real check.*
COLLECT = r'\bfail\w*\.append\(|allpass\s*&=|\bok\s*=\s*False\b'
NZEXIT = r'raise\s+SystemExit\(|^\s*sys\.exit\(|^\s*return\s+1\b'
EXPLICIT = r'^\s*assert\b|^\s*sys\.exit\(1\)|raise\s+SystemExit\(1\)'


def comparison_derived(tree):
    """every name whose value derives, transitively, from a COMPARISON -- that is, from a check"""
    assigns = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            assigns += [(t.id, n.value) for t in n.targets if isinstance(t, ast.Name)]
        elif isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name):
            assigns.append((n.target.id, n.value))
    derived, changed = set(), True
    while changed:                       # a fixpoint, because `bad |= (not ok1)` is two steps
        changed = False
        for name, val in assigns:
            if name in derived:
                continue
            for sub in ast.walk(val):
                if isinstance(sub, ast.Compare) or (isinstance(sub, ast.Name)
                                                    and sub.id in derived):
                    derived.add(name)
                    changed = True
                    break
    return derived


def acting_exit(src):
    """*** does a NON-ZERO exit depend on the outcome of a comparison? ***"""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return False
    derived = comparison_derived(tree)
    for n in ast.walk(tree):
        arg = None
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'exit':
            arg = n.args[0] if n.args else None
        elif isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call) \
                and getattr(n.exc.func, 'id', '') == 'SystemExit':
            arg = n.exc.args[0] if n.exc.args else None
        if arg is None or (isinstance(arg, ast.Constant) and arg.value in (0, None)):
            continue
        for sub in ast.walk(arg):
            if isinstance(sub, ast.Compare) or (isinstance(sub, ast.Name) and sub.id in derived):
                return True
    return False


def carries_a_check(src):
    """** the whole rule: an explicit assert, OR collection-with-an-exit, OR an acting exit. **"""
    if re.search(EXPLICIT, src, re.M):
        return True
    if re.search(COLLECT, src, re.I) and re.search(NZEXIT, src, re.M):
        return True
    return acting_exit(src)


#: ** THE TWO CONTROLS, carried WITH the rule so a future edit runs them. **  *The first must be
#: accepted and the second must be REFUSED; a rule that takes both is the hole, not the fix.*
CONTROL_REAL = '''
import sys
bad = 0
ok1 = 2 + 2 == 4
bad |= (not ok1)
print('done')
sys.exit(1 if bad else 0)
'''
CONTROL_HOLLOW = '''
import sys
allpass = True
def main():
    print('a receipt that only prints')
    return 0
raise SystemExit(main())
'''


def main():
    print()
    print('  acting_check -- the two controls the third clause must separate')
    print()
    a, b = acting_exit(CONTROL_REAL), acting_exit(CONTROL_HOLLOW)
    print(f'    accumulator read at a conditional exit   -> acting_exit {a}   (must be True)')
    print(f'    `raise SystemExit(main())`, main() prints -> acting_exit {b}  (must be False)')
    print()
    if a and not b:
        print('    the clause separates them: a non-constant exit code is NOT enough; the code')
        print('    must trace back to a comparison.')
        print()
        return 0
    print('    [FAIL] the third clause does not separate its two controls.')
    print()
    return 1


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""lint_assertions.py -- ** THE HOLLOW-ASSERTION LINT. **

Built r2376+c54.158, at the start of the assertion sweep, and BEFORE any of it was written.

** WHY IT EXISTS. **  The census at c54.154 found 188 of 276 receipts with no check at all, and
c54.157 closed the last audit batch with the debt at 172.  The sweep that clears it is mechanical
enough to dispatch -- and that is exactly the danger.  A worker asked to make a file "able to
fail" can satisfy the count with a check that cannot fail: `assert True`, `assert x == x`, or the
subtler and far more common form

        y = <expression>
        assert abs(y - <the same expression>) < tol

which re-derives the value it is testing and therefore tests the interpreter.  ** A hollow
assertion is worse than none: it converts a known gap into an unknown one, and it makes the debt
number lie. **

So the sweep's own instrument comes first.  This lint reads every assertion in a receipt and
classifies it:

  HOLLOW    -- provably cannot fail: a literal truthy constant, or both sides syntactically equal,
               or a comparison of a name against the expression it was just assigned.
  UNPINNED  -- can fail in principle, but tests no external quantity: every operand traces back to
               values computed in the same file, with no literal to anchor it.  ** Legitimate for
               a structural identity (det = 1, a symbolic difference = 0) and NOT legitimate as a
               receipt's only check, because it cannot notice that the PAPER has drifted. **
  PINNED    -- compares a computed value against a numeric or exact literal.  This is the form
               THE_BASE_RATE's eighteenth entry asks for: assert abs(value - <the figure the
               paper prints>) < tol.

A receipt passes the lint when it has at least one assertion and NONE of them is HOLLOW.
It is REPORTED (not failed) when all of its assertions are UNPINNED, because a purely structural
receipt legitimately has nothing to pin.

Usage:  python3 scripts/lint_assertions.py [path ...]      (default: all of receipts/)
Exit 1 if any HOLLOW assertion is found.
"""
import ast
import os
import sys
import glob
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

TRUTHY_CONST = (True, 1, -1, 'x')


def _src(node, lines):
    try:
        return ast.get_source_segment('\n'.join(lines), node) or ''
    except Exception:
        return ''


class Visitor(ast.NodeVisitor):
    def __init__(self, lines):
        self.lines = lines
        self.assigns = {}          # name -> source text of its last assignment
        self.findings = []         # (lineno, verdict, text)

    def visit_Assign(self, node):
        txt = _src(node.value, self.lines)
        for t in node.targets:
            if isinstance(t, ast.Name):
                self.assigns[t.id] = txt
        self.generic_visit(node)

    # --- the classifier ------------------------------------------------------------------
    def _has_literal(self, node):
        """does the expression contain a numeric/string literal that is not 0, 1 or a tolerance?"""
        for n in ast.walk(node):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
                v = abs(n.value)
                if v not in (0, 1, 2) and not (0 < v < 1e-3):
                    return True
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3:
                return True
        return False

    def _sides(self, node):
        """for a comparison, return the two source texts being compared"""
        # abs(a - b) < tol FIRST -- it is also a Compare, and the generic branch below would
        # otherwise swallow it and return ('abs(a - b)', 'tol'), which never matches.
        if (isinstance(node, ast.Compare) and isinstance(node.left, ast.Call)
                and getattr(node.left.func, 'id', '') == 'abs' and node.left.args):
            inner = node.left.args[0]
            if isinstance(inner, ast.BinOp) and isinstance(inner.op, ast.Sub):
                return _src(inner.left, self.lines), _src(inner.right, self.lines)
        # (a - b) == 0, or (a - b) < tol -- the difference form.  Added r2376+c54.159 after the
        # P03 sweep found `sqrt(Rv**2-1) - sqrt(Rv**2-1) == 0` printing PASS at every dimension.
        if (isinstance(node, ast.Compare) and len(node.ops) == 1
                and isinstance(node.left, ast.BinOp) and isinstance(node.left.op, ast.Sub)):
            return _src(node.left.left, self.lines), _src(node.left.right, self.lines)
        if isinstance(node, ast.Compare) and len(node.ops) == 1:
            return _src(node.left, self.lines), _src(node.comparators[0], self.lines)
        return None, None

    # ** THE check() FORM, added r2376+c54.159. **  The P03 sweep found three tautologies wearing
    # a `check(label, condition)` helper that PRINTS PASS/FAIL -- `sqrt(Rv**2-1) - sqrt(Rv**2-1)
    # == 0`, a hardcoded `True`, and a loop recomputing its answer without the variable it claims
    # to vary.  ** Those are invisible to a lint that reads only `assert`, and invisible to the
    # census too, since the file may carry real assertions elsewhere. **  A check that cannot fail
    # is a hollow assertion wearing a different hat, so it is classified the same way.
    CHECKISH = ('check', 'chk', 'ok_', 'verify', 'assert_')

    def visit_Call(self, node):
        fn = getattr(node.func, 'id', '') or getattr(node.func, 'attr', '')
        if fn and any(fn == c or fn.startswith(c) for c in self.CHECKISH) and len(node.args) >= 2:
            cond = node.args[-1]
            txt = (_src(node, self.lines) or '').strip().replace('\n', ' ')[:150]
            if isinstance(cond, ast.Constant) and cond.value in TRUTHY_CONST:
                self.findings.append((node.lineno, 'HOLLOW', txt))
                return
            if isinstance(cond, ast.Compare) and not any(
                    isinstance(n, (ast.Name, ast.Attribute, ast.Call)) for n in ast.walk(cond)):
                self.findings.append((node.lineno, 'HOLLOW', txt))
                return
            a, b = self._sides(cond)
            _m = lambda t: t.strip().strip('()').replace(' ', '')
            if a is not None and a and b and _m(a) == _m(b):
                self.findings.append((node.lineno, 'HOLLOW', txt))
                return
        self.generic_visit(node)

    def visit_Assert(self, node):
        t = node.test
        txt = (_src(node, self.lines) or '').strip().replace('\n', ' ')[:150]
        # 1. a bare truthy constant
        if isinstance(t, ast.Constant) and t.value in TRUTHY_CONST:
            self.findings.append((node.lineno, 'HOLLOW', txt)); return
        # 2. abs(a - b) < tol, or a == b, with both sides syntactically identical
        a, b = self._sides(t)
        _n = lambda t: t.strip().strip('()').replace(' ', '')
        if a is not None and a and b and _n(a) == _n(b):
            self.findings.append((node.lineno, 'HOLLOW', txt)); return
        # 3. a name compared against the very expression it was assigned
        if a is not None and a and b:
            for lhs, rhs in ((a, b), (b, a)):
                nm = lhs.strip()
                if nm in self.assigns and _n(self.assigns[nm]) == _n(rhs):
                    self.findings.append((node.lineno, 'HOLLOW', txt)); return
        # 4. a condition built entirely of literals -- (1-1) == 0, 2 <= 3, 0 == 0.  Added
        #    r2376+c54.161 after the P08/P09 sweep found `check("eq:Ek verified", (1-1)==0)` and a
        #    "CONTROL" whose condition was `2 <= 3`.  ** Constant-folded, so it cannot fail. **
        if isinstance(t, ast.Compare) and not any(isinstance(n, (ast.Name, ast.Attribute, ast.Call))
                                                  for n in ast.walk(t)):
            self.findings.append((node.lineno, 'HOLLOW', txt)); return
        # 5. does it pin anything external?
        self.findings.append(
            (node.lineno, 'PINNED' if self._has_literal(t) else 'UNPINNED', txt))
        self.generic_visit(node)


def lint(path):
    src = open(path, encoding='utf-8', errors='replace').read()
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [(0, 'SYNTAX', str(e))]
    v = Visitor(src.split('\n'))
    v.visit(tree)
    return v.findings


# ** THE THIRD FORM, ADDED r2376+c54.179 AFTER THIS INSTRUMENT REPORTED A DEFECT THAT WAS NOT THERE. **
#
# The old test was  `fail\.append|allpass\s*&=|^\s*sys\.exit\(1\)|raise SystemExit\(1\)`  and it missed
# a whole idiom: a `check(label, cond)` helper appending to an UPPERCASE failure list, with the script
# ending `raise SystemExit(main())` where main returns 1 if the list is non-empty.  ** Case-sensitive on
# `fail`, literal on `SystemExit(1)`. **  Thirteen receipts were reported as carrying "no check of any
# kind" on that basis; node 56 broke a claim inside one of them and it returned rc=1, which is the
# evidence that settles it.  *An instrument that reports a defect that is not there costs exactly what a
# missed defect costs -- a reading of the whole namespace to disprove -- and this one did it while I was
# routing a finding built on its output.*
#
# ** THE RULE IS DELIBERATELY TWO-PART, so this does not over-correct into counting things that cannot
# fail. **  A failure-collection idiom ALONE is not a check: nothing acts on the list.  What makes it a
# check is a collection idiom AND a non-zero exit path.  An explicit `sys.exit(1)` / `SystemExit(1)`
# still counts on its own, since it IS the acting.
_FAIL_COLLECT = re.compile(r'\bfail\w*\.append\(|allpass\s*&=|\bok\s*=\s*False\b', re.I)
_NONZERO_EXIT = re.compile(r'raise\s+SystemExit\(|^\s*sys\.exit\(|^\s*return\s+1\b', re.M)
_EXPLICIT_ONE = re.compile(r'^\s*sys\.exit\(1\)|raise\s+SystemExit\(1\)', re.M)


def _carries_other_check(src):
    """a check in a form other than `assert` -- see the note above for why it is two-part"""
    if _EXPLICIT_ONE.search(src):
        return True
    return bool(_FAIL_COLLECT.search(src) and _NONZERO_EXIT.search(src))


def _rule_has_not_drifted():
    """** THE SAME RULE LIVES IN corpus/check_receipts.py AND A RULE IN TWO PLACES DRIFTS. **

    That gate decides the ratchet; this one decides the lint.  When they disagreed -- and they did,
    both carrying `fail\.append` case-sensitively and `allpass &=` with no exit path -- a registered
    receipt that could not fail passed both.  So the two are compared HERE, by reading that file's
    text: no import, since importing a gate runs it, and no shared module, since these are two
    directories with different owners.  *If either rule is edited alone, this fails and names it.*
    """
    g = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     'corpus', 'check_receipts.py')
    try:
        txt = open(g, encoding='utf-8').read()
    except OSError:
        return ["corpus/check_receipts.py is unreadable -- the two-part rule cannot be compared"]
    want = {'_COLLECT': r"\bfail\w*\.append\(|allpass\s*&=|\bok\s*=\s*False\b",
            '_NZEXIT': r"raise\s+SystemExit\(|^\s*sys\.exit\(|^\s*return\s+1\b"}
    out = []
    for nm, pat in want.items():
        if pat not in txt:
            out.append(f"check_receipts.py's {nm} no longer matches this file's rule")
    return out


def main(argv):
    targets = argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'receipts', '*', '*.py')))
    hollow, unpinned_only, none_at_all, ok = [], [], [], 0
    other_form = []
    for f in targets:
        fs = lint(f)
        if any(v == 'SYNTAX' for _, v, _ in fs):
            hollow.append((f, 0, 'unparseable')); continue
        if not fs:
            # ** the census in check_receipts also counts fail.append / allpass &= / a non-zero
            #    exit as checks; a file may carry those and no `assert` at all.  Reported here
            #    as a SEPARATE line so the two instruments' numbers can be reconciled instead of
            #    silently disagreeing -- which they did until r2376+c54.161. **
            _src_txt = open(f, encoding='utf-8', errors='replace').read()
            if _carries_other_check(_src_txt):
                other_form.append(f)
            else:
                none_at_all.append(f)
            continue
        h = [(ln, t) for ln, v, t in fs if v == 'HOLLOW']
        if h:
            for ln, t in h:
                hollow.append((f, ln, t))
        elif all(v == 'UNPINNED' for _, v, _ in fs):
            unpinned_only.append(f)
            ok += 1
        else:
            ok += 1
    _drift = _rule_has_not_drifted()
    print()
    print(f"  HOLLOW-ASSERTION LINT -- {len(targets)} receipt(s)")
    print(f"    {ok:>4} carry at least one assertion and none of them hollow")
    print(f"    {len(other_form):>4} carry no `assert` but DO carry a check in another form "
          f"(fail.append / allpass / exit 1)")
    print(f"    {len(none_at_all):>4} carry no check of any kind -- THE ASSERTION DEBT "
          f"(receipts/ASSERTION_DEBT.txt)")
    print(f"    {len(unpinned_only):>4} of the {ok} are UNPINNED-only -- structural checks with no "
          f"external literal.")
    print(f"         *Legitimate for a symbolic identity; it cannot notice that the PAPER moved.*")
    if hollow:
        print()
        print(f"  ⛔ {len(hollow)} HOLLOW ASSERTION(S) -- provably cannot fail:")
        for f, ln, t in hollow[:40]:
            print(f"     {os.path.relpath(f, ROOT)}:{ln}")
            print(f"        {t}")
        print()
        print("  A hollow assertion is worse than none: it converts a known gap into an unknown")
        print("  one, and it makes the debt number lie.")
        return 1
    print()
    if _drift:
        for _m in _drift:
            print(f"  [FAIL] {_m}")
        print("  ** The two-part check rule lives in this file AND in corpus/check_receipts.py, and")
        print("  when they last disagreed a registered receipt that could not fail passed both. **")
        return 1
    print("  the two-part check rule agrees with corpus/check_receipts.py's")
    print("  No hollow assertions.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

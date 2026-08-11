#!/usr/bin/env python3
"""propagate_to_origin.py -- keep a receipts/ copy and its ORIGIN identical in CODE.

Built r2376+c54.158, during the assertion sweep, because the sweep creates exactly the drift the
ORIGIN guard exists to catch.

** THE SITUATION. **  Most receipts carry a line `ORIGIN: <path> -- edit the origin, not this
copy`, and `check_receipts.py` compares the two files' CODE (docstrings may differ; the receipts
copy carries the registration header).  The assertion sweep adds checks to the receipts copy, so
every swept file with an origin diverges.  The guard reported that immediately and correctly:
24 unexplained before the sweep began, 35 after the first two batches.

** WHAT THIS DOES. **  Rewrites each named ORIGIN so that its code is the receipts copy's code,
while KEEPING THE ORIGIN'S OWN DOCSTRING.  The pair then agrees in code and differs only where it
is supposed to.  It refuses to touch a pair whose code already agrees, and refuses to run on a
file with no ORIGIN line, so it cannot quietly overwrite something it was not pointed at.

Usage:  python3 scripts/propagate_to_origin.py <receipts/…/file.py> [more …]
        python3 scripts/propagate_to_origin.py --all-diverging
"""
import ast
import os
import re
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
ORIGIN_RE = re.compile(r'ORIGIN:\s*([^\s]+\.py)')


def code_of(path):
    """the file's source with its module docstring removed -- what the guard compares"""
    src = open(path, encoding='utf-8', errors='replace').read()
    try:
        t = ast.parse(src)
    except SyntaxError:
        return None
    if (t.body and isinstance(t.body[0], ast.Expr)
            and isinstance(t.body[0].value, ast.Constant)
            and isinstance(t.body[0].value.value, str)):
        end = t.body[0].end_lineno
        return '\n'.join(src.split('\n')[end:])
    return src


def docstring_block(path):
    """the leading docstring of a file, verbatim, including its quotes and any shebang above it"""
    src = open(path, encoding='utf-8', errors='replace').read()
    t = ast.parse(src)
    if (t.body and isinstance(t.body[0], ast.Expr)
            and isinstance(t.body[0].value, ast.Constant)
            and isinstance(t.body[0].value.value, str)):
        end = t.body[0].end_lineno
        return '\n'.join(src.split('\n')[:end])
    return ''


def propagate(rel):
    p = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
    src = open(p, encoding='utf-8', errors='replace').read()
    m = ORIGIN_RE.search(src)
    if not m:
        return f"  [skip] {os.path.relpath(p, ROOT)}: no ORIGIN line"
    o = os.path.join(ROOT, m.group(1))
    if not os.path.exists(o):
        return f"  [skip] {os.path.relpath(p, ROOT)}: origin {m.group(1)} not on disk"
    if code_of(p) == code_of(o):
        return f"  [ok]   {os.path.relpath(p, ROOT)}: already agrees"
    head = docstring_block(o)
    body = code_of(p)
    if body is None:
        return f"  [FAIL] {os.path.relpath(p, ROOT)}: unparseable"
    open(o, 'w', encoding='utf-8').write(head + '\n' + body)
    return f"  [prop] {os.path.relpath(o, ROOT)} <- {os.path.relpath(p, ROOT)}"


def main(argv):
    args = argv[1:]
    if args == ['--all-diverging']:
        args = []
        for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '*', '*.py'))):
            s = open(f, encoding='utf-8', errors='replace').read()
            m = ORIGIN_RE.search(s)
            if not m:
                continue
            o = os.path.join(ROOT, m.group(1))
            if os.path.exists(o) and code_of(f) != code_of(o):
                args.append(f)
    if not args:
        print("  nothing to propagate")
        return 0
    print()
    for a in args:
        print(propagate(a))
    print()
    print("  Now re-run corpus/check_receipts.py -- the ORIGIN drift guard should be quiet on these.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

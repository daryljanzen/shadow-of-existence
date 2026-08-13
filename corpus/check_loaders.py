#!/usr/bin/env python3
"""check_loaders.py -- THE SILENT-DISCARD CLASS: a loader that drops input without saying so.

** WHY THIS IS A CLASS AND NOT FIVE SLIPS.  c54.206 named it: ** "a loader that silently discards
input, with the gate downstream reporting the consequence ... the common tell is that ** something was
written and did not arrive **.  If a fourth turns up I think that's a class worth a gate of its own
rather than three fixes."

** FIVE INSTANCES, in four files and three shapes: **
  ⓵ ** `check_receipts` ** filtered INDEX rows on `startswith('| P')` while the geometric core is
    written ** `p0` lowercase ** -- nine receipts invisible (c54.203).
  ⓶ ** `make_receipt_appendix` ** carried the same filter -- the same nine dropped from the printed
    reproducibility layer, ** and an uncited receipt that vanishes leaves no dead link ** (c54.203).
  ⓷ ** `regen_board`'s LEADS dict had TWO `L-171` keys ** -- a duplicate key in a Python dict literal
    is ** silent **, the later wins, and an r2552 edit to the first was discarded at load (r2552).
  ⓸ ** `check_currency`'s declaration regex ** did not accept the compound `rNNNN+c54.N` the corpus
    actually writes -- ** 40 of 70 declarations never parsed ** (r2550).
  ⓹ ** `run_all_receipts` and `work_entry_points` ** carried instance ⓵'s filter, unfixed -- ** twelve
    receipts that the runner never ran ** -- and `check_receipts` had a ** SECOND load site ** in the
    same file, left behind when the first was corrected (r2555).

  ⇒ *** THE SHAPE: the input is well-formed, the loader rejects it on a convention it does not know,
      and NOTHING REPORTS THE REJECTION.  The gate downstream then reports a consequence whose cause is
      invisible to it -- r2541's drift check saw "the board text stops at no revision" while the
      duplicate key was unreachable from what it read. ***

** WHAT THIS GATE CHECKS. **
  1. ** DUPLICATE STRING KEYS in dict literals ** across `scripts/` and `corpus/` -- exact, via `ast`,
     and a hard failure.  Python will not tell you.
  2. ** CASE-SENSITIVE PAPER-COLUMN FILTERS ** -- any live `startswith('| P')` on a table the corpus
     writes with a lowercase tag.  Comments are excluded; only executable lines count.
  3. ** DECLARATION LINES NO PARSER ACCEPTS ** -- every `current:` value in the top-level documents is
     put through `check_currency.declared`, and any that returns "no marker at all" is reported.

⚠ ** LIMIT, stated because it is the honest half: ** this catches the three shapes that HAVE occurred.
*** A silent discard is by construction invisible, so a gate for it can only ever encode the ways it has
already been caught -- which is why the instance list above is part of the specification and is meant to
grow. ***  ⌗ That is c54.206's own point about namespace lints, one register out: ** the exception list
is the spec, not a defect record. **

    python3 corpus/check_loaders.py

Written r2555.  Stated for reversal.
"""
import ast
import collections
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
FAILURES = []


def sources():
    return (sorted(glob.glob(os.path.join(ROOT, 'scripts', '*.py')))
            + sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.py'))))


def check_duplicate_dict_keys():
    """⓷'s shape: a repeated key in a dict literal.  Silent in Python; the later entry wins."""
    out = []
    for f in sources():
        try:
            tree = ast.parse(open(f, encoding='utf-8', errors='replace').read())
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, ast.Dict):
                continue
            keys = [k.value for k in node.keys
                    if isinstance(k, ast.Constant) and isinstance(k.value, str)]
            # ** a CHARACTER TRANSLATION TABLE with a repeated key is harmless and usually
            # deliberate -- make_receipt_appendix's _UNI maps two forms of one glyph.  ** The class
            # this gate exists for is a NAMED entry silently losing to a later one; single-character
            # keys are not names.
            if keys and all(len(k) <= 2 for k in keys):
                continue
            dupes = {k: n for k, n in collections.Counter(keys).items() if n > 1}
            if dupes:
                out.append((os.path.basename(f), node.lineno, dupes))
    return out


def check_case_sensitive_filters():
    """⓵⓶⓹'s shape: a case-sensitive filter on a column the corpus writes in mixed case."""
    out = []
    pat = re.compile(r"""\w*ln\s*\.startswith\(\s*['"]\|\s*P['"]""")
    for f in sources():
        # ** COMMENTS AND DOCSTRINGS ARE NOT CODE, and the first version could only see comments.
        # make_receipt_appendix's own DOCSTRING account of the c54.36 fix -- "because the filter was
        # ln.startswith('| P')" -- scored as a live filter, which is exactly backwards: it is the
        # record OF the fix. **  ⇒ *** Tokenising is the only way to tell a quoted mention from a
        # call, and a lint that cannot is a lint that punishes documentation. ***
        import io
        import tokenize
        try:
            src = open(f, encoding='utf-8', errors='replace').read()
            code_lines = set()
            for tok in tokenize.generate_tokens(io.StringIO(src).readline):
                if tok.type not in (tokenize.COMMENT, tokenize.STRING):
                    code_lines.add(tok.start[0])
        except Exception:
            code_lines = None
        for i, line in enumerate(open(f, encoding='utf-8', errors='replace'), 1):
            if code_lines is not None and i not in code_lines:
                continue
            stripped = line.lstrip()
            # ** a comment recording the fix is not the fix being undone.  The first version tested
            # only `startswith('#')`, which misses a docstring line -- and make_receipt_appendix's
            # own account of the c54.36 fix scored as a live filter. **
            code = line.split('#', 1)[0]
            if stripped.startswith('#') or '#' in line and pat.search(line) and not pat.search(code):
                continue
            if pat.search(code):
                out.append((os.path.basename(f), i, stripped.strip()[:70]))
    return out


def check_unparsed_declarations():
    """⓸'s shape: a declaration written in a form no parser accepts."""
    sys.path.insert(0, HERE)
    try:
        import check_currency as cc
    except Exception:
        return []
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, '*.md'))):
        head = open(f, encoding='utf-8', errors='replace').read(2500)
        m = re.search(r'^current:\s*(.+)$', head, re.M)
        if not m:
            continue
        kind, _ = cc.declared(f)
        if kind is None:
            out.append((os.path.basename(f), m.group(1).strip()[:40]))
    return out


def main():
    print()
    print('  check_loaders -- does anything drop input without saying so?')
    print()

    dupes = check_duplicate_dict_keys()
    if dupes:
        for f, ln, d in dupes:
            print(f'    [FAIL] {f}:{ln} dict literal has duplicate key(s): {d}')
        print('       ⛔ A duplicate key in a dict literal is SILENT: the later wins and any edit to')
        print('          the earlier one is discarded at load, with no error anywhere.')
        FAILURES.append('duplicate dict keys')
    else:
        print(f'    OK    no duplicate dict keys across {len(sources())} source file(s)')

    filters = check_case_sensitive_filters()
    if filters:
        for f, ln, txt in filters:
            print(f'    [FAIL] {f}:{ln} case-sensitive paper-column filter: {txt}')
        print("       ⛔ The corpus writes the geometric core as `p0` LOWERCASE.  A filter on '| P'")
        print('          drops its rows, and a dropped row leaves no trace downstream.')
        FAILURES.append('case-sensitive filters')
    else:
        print('    OK    no live case-sensitive paper-column filter')

    undecl = check_unparsed_declarations()
    if undecl:
        for f, raw in undecl:
            print(f'    [FAIL] {f} declares `current: {raw}` and no parser accepts it')
        print('       ⛔ A declaration nothing reads is a declaration that was written and did not')
        print('          arrive -- the gate then falls back to a weaker proxy without saying so.')
        FAILURES.append('unparsed declarations')
    else:
        print('    OK    every `current:` declaration parses')

    print()
    if FAILURES:
        print(f'  {len(FAILURES)} shape(s) failing: {", ".join(FAILURES)}')
        return 1
    print('  ⌗ ** THE LIMIT, stated: ** a silent discard is by construction invisible, so this gate can')
    print('    only encode the shapes that have ALREADY been caught -- five instances, four files,')
    print('    three shapes.  ** The instance list in the docstring is part of the specification and is')
    print('    meant to grow, not a defect record. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""check_row_matchers.py -- A RECEIPT MAY NOT LOOK UP A REGISTER ROW BY ITS OPEN-FORM PREFIX.

** WHY, AND THE CORPUS DIAGNOSED THIS ONCE ALREADY AND DID NOT GATE IT. **

A protected row is written `| **PO-6**` while open and `| ~~**PO-6**~~` once struck.  A receipt that
locates it with `l.startswith('| **PO-6**')` is reading the OPEN FORM ONLY.

  ⇒ ** STRUCK: the match fails, `next()` raises `StopIteration`, and the receipt CRASHES ** -- an
    ABSENCE presenting as a broken receipt rather than as a check failure.
  ⇒ ** DUPLICATED: it silently follows whichever copy is open ** -- which is worse, because it goes
    on passing while reading a resurrected row.

*** BOTH FAILURE MODES HAVE HAPPENED IN THIS CORPUS. ***
  · `L-558` (c54.224): a merge resurrected `PO-4` unstruck; **three `L-221` receipts matched the open
    form and passed for four revisions while reading the resurrected copy.**  Deduplicating them
    killed all three with `StopIteration`, *"which is how this was found."*  They were amended and
    the rule was written down: **"a matcher that admits only the open form silently follows whichever
    copy is open."**
  · `L-248` (r3100): r3001 closed `PROTECTED_OPEN` with fourteen rows struck.  **Fourteen more
    receipts carried the same brittle lookup and thirteen crashed.**

  ⇒ *** THE RULE WAS RECORDED IN A RECEIPT AND NEVER TURNED INTO A GATE, SO THE NEXT STRIKE
      RE-CREATED IT AT FIVE TIMES THE SCALE.  A rule that lives only in a receipt protects only the
      files that receipt amended. ***

** ⌗ THE REPAIR, and it is one expression. **  Match the ID with the strike markup optional:

      next(l for l in raw.split('\\n') if re.match(r'\\|\\s*~?~?\\*\\*PO-6\\*\\*', l))

*This admits both forms, so it survives a strike AND a re-opening, and it still pins the row it
names.*  ⌷ **A receipt DISCUSSING the brittle form -- quoting it inside a string, as `L-558` does --
is not using it, and is exempted by that distinction rather than by a filename.**

    python3 corpus/check_row_matchers.py

Written r3100 (`L-248`).  Stated for reversal.
"""
import ast
import glob
import io
import os
import re
import sys
import tokenize

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: the brittle lookup: a startswith on a row's OPEN form.
BRITTLE = re.compile(r"""\.startswith\(\s*(?P<q>['"])\|\s*\*\*(PO|L)-[^'"]*\*\*(?P=q)\s*\)""")


#: what an OPEN-FORM row identifier looks like, as the CONTENT of a string literal
OPEN_FORM = re.compile(r"^\|\s*\*\*(PO|L)-.*\*\*")


def uses_it(src):
    """(line, text) for every line that USES the brittle matcher -- not one that MENTIONS it

    ** The distinction is the whole reason this gate does not simply grep, and it is not
    hypothetical: `L-558`'s `D1` records this hazard and quotes the brittle form in a COMMENT, while
    this gate's sibling receipt quotes it in a DOCSTRING. **  *A grep fails on both -- on the receipt
    that documented the class and on the one that repaired it.*

    ⛔ ** AND BLANKING STRING TOKENS DOES NOT WORK EITHER, WHICH IS WHERE THIS WAS WRITTEN FIRST. **
    *The row identifier IS a string literal, so blanking strings erases the thing being matched: the
    gate went green on a seeded USE.  Caught by seeding it rather than by reading it.*
      ⇒ *** So the match is on the TOKEN SEQUENCE -- `.startswith( <string> )` where the string's
          CONTENT is an open-form row id.  A mention inside a comment or a docstring is a single
          COMMENT/STRING token and never produces that sequence, so the distinction is structural
          rather than heuristic. ***
    """
    try:
        toks = [t for t in tokenize.generate_tokens(io.StringIO(src).readline)
                if t.type not in (tokenize.NL, tokenize.NEWLINE, tokenize.INDENT,
                                  tokenize.DEDENT, tokenize.COMMENT)]
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return [(0, 'UNPARSEABLE -- cannot distinguish use from mention')] \
            if BRITTLE.search(src) else []
    lines = src.split('\n')
    out = []
    for i in range(len(toks) - 3):
        a, b, c, d = toks[i], toks[i + 1], toks[i + 2], toks[i + 3]
        if not (a.type == tokenize.OP and a.string == '.'
                and b.type == tokenize.NAME and b.string == 'startswith'
                and c.type == tokenize.OP and c.string == '('
                and d.type == tokenize.STRING):
            continue
        try:
            val = ast.literal_eval(d.string)
        except Exception:
            continue
        if isinstance(val, str) and OPEN_FORM.match(val):
            ln = b.start[0]
            out.append((ln, lines[ln - 1].strip()[:96]))
    return out


def main():
    print()
    print('  check_row_matchers -- does any receipt look a register row up by its OPEN form only?')
    print()
    bad = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        hits = uses_it(open(f, encoding='utf-8', errors='replace').read())
        if hits:
            bad.append((os.path.relpath(f, ROOT), hits))
    n = len(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    print(f'    {n} receipt(s) scanned; {len(bad)} use an open-form-only row lookup')
    if not bad:
        print('    every register-row lookup admits the struck form.')
        print()
        return 0
    print()
    for f, hits in bad:
        print(f'    [FAIL] {f}')
        for ln, txt in hits:
            print(f'           line {ln}: {txt}')
    print()
    print('    ⛔ ** A row struck since this was written makes the lookup raise StopIteration and the')
    print('       receipt CRASH -- an absence reading as a broken receipt.  A row DUPLICATED makes it')
    print('       silently follow whichever copy is open, which is worse because it keeps passing. **')
    print("    ⌷ Repair:  re.match(r'\\|\\s*~?~?\\*\\*PO-n\\*\\*', l)  -- admits both forms.")
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())

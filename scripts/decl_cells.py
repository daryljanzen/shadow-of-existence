#!/usr/bin/env python3
"""THE GRAMMAR OF `ROWS.tsv`'s `receipt` AND `decl` CELLS -- stated once, in one place, because the
absence of a stated grammar is what made the first join gate red on good data.

** WHY THIS FILE EXISTS, and the defect is in an ORDER of node 66's rather than in either instrument. **
`r7419` ① asked `71` for a `decl` column carrying *"the fully qualified Lean name or names AND THE FILE"*
-- names plural, file singular.  `71` reasonably generalised: a row's proof is often spread over several
files, so it wrote SEVERAL GROUPS, each a file with its own name list.  `60` reasonably implemented the
singular reading: `_split_decl` took the FIRST `.lean` path in the cell and the LONGEST dotted token
anywhere in it, and paired them.

On a one-group cell those agree.  On a multi-group cell they do not, and at `r7423` the consequence was
measured:

  * the data held **258** `(file, name)` pairs over **87** rows in **106** groups, **15** rows carrying
    more than one group;
  * the gate checked **one pair per row -- 87 of 258, 34 per cent**;
  * and it reported **7 dangling references, every one of them its own mispairing** -- a name from a
    later group against the first group's file.  Spot-checked against the tree: `euler_tt_transverse` is
    declared in `probes/NonDiag.lean` exactly as `71`'s cell says, and the gate asserted `S3Frame.lean`.

** SO NEITHER SEAT ERRED AND THE ORDER DID. **  A format with no stated grammar is a key with no declared
`K`: two instruments each implement a reading, both reasonable, and the disagreement surfaces as a red on
correct data.  ⇒ The remedy is not to patch two parsers.  It is to state the grammar once and have both
read it here, which is what this module is for.

** AND ONE LESSON TRAVELS WITH IT. **  `71` wrote, of its own syntactic check, *"that is a syntactic
check; `60`'s gate is the verdict"* -- and the gate was wrong while the syntactic check was right.  A gate
is the verdict only on the question it ACTUALLY IMPLEMENTS, so deference to an instrument is itself a
claim that wants checking.  (`r7417` ② ruled that agreement with an instrument is not correctness; this is
the same rule for disagreement.)

-------------------------------------------------------------------------------------------------------
THE GRAMMAR
-------------------------------------------------------------------------------------------------------
A `decl` cell is a `|`-separated list of GROUPS.  A group is

    <path to a .lean file> : <name> [, <name>]*

with surrounding whitespace insignificant.  A name is a Lean identifier, usually fully qualified
(`ShadowProbe.foo`).  Every name in a group is a claim that THAT name is declared in THAT file; a name
carries no claim about any other group's file.  An empty cell, or `-`, is no claim at all -- which is the
state for `ROW: A DIFFERENT KIND`, `LIBRARY GAP` and `GENERIC-METRIC IDENTITY` rows by `71`'s own rule,
since a cell there could otherwise name a theorem that does not carry the row.

A `receipt` cell is a `|`-separated list of receipt paths, no names.

** A CELL THAT DOES NOT PARSE IS AN ERROR AND NOT AN EMPTY RESULT. **  `parse_decl` raises on a group
that has no `.lean` path or no name, rather than returning fewer pairs, because a parser that silently
drops what it cannot read is the silence-versus-verdict defect of `PO-78`'s fifteenth face: a caller
cannot tell "this row claims nothing" from "I could not read this row".

Usage:
    from decl_cells import parse_decl, parse_receipt, DeclCellError
    for path, name in parse_decl(row['decl']):   # EVERY pair, not one
        ...
    python3 scripts/decl_cells.py --selftest     # the grammar's own cases
    python3 scripts/decl_cells.py --audit        # parse every cell in ROWS.tsv and report the shape
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROWS = os.path.join(ROOT, 'computations', 'formalisation', 'r7325_71_inventory', 'ROWS.tsv')

_LEAN = re.compile(r'^([\w./\-]+\.lean)$')
_NAME = re.compile(r"^[A-Za-z_][\w.']*$")


class DeclCellError(ValueError):
    """A cell that does not parse.  Raised rather than returning a short list."""


def _empty(cell):
    return cell is None or cell.strip() in ('', '-')


def parse_decl(cell):
    """[(lean_path, name), ...] -- EVERY pair the cell claims, in cell order.

    Raises DeclCellError on a group with no `.lean` path or no names.  Returns [] only for an
    empty cell, so [] means "claims nothing" and never "could not read"."""
    if _empty(cell):
        return []
    out = []
    for i, grp in enumerate(cell.split('|')):
        g = grp.strip()
        if not g:
            continue
        path, sep, names = g.partition(':')
        path = path.strip()
        if not sep or not _LEAN.match(path):
            raise DeclCellError(
                f'group {i + 1} has no `<path>.lean :` prefix: {g[:80]!r}')
        got = [n.strip() for n in names.split(',') if n.strip()]
        if not got:
            raise DeclCellError(f'group {i + 1} ({path}) names nothing')
        for n in got:
            if not _NAME.match(n):
                raise DeclCellError(f'group {i + 1} ({path}) has a non-identifier name: {n!r}')
            out.append((path, n))
    if not out:
        raise DeclCellError(f'no group parsed from a non-empty cell: {cell[:80]!r}')
    return out


def parse_receipt(cell):
    """[receipt_path, ...] -- every path the cell names, in cell order."""
    if _empty(cell):
        return []
    return [p.strip() for p in cell.split('|') if p.strip()]


def read_rows(path=ROWS):
    lines = [l for l in open(path, encoding='utf-8').read().split('\n') if l.strip()]
    head = lines[0].split('\t')
    return head, [dict(zip(head, l.split('\t'))) for l in lines[1:] if l.count('\t') >= len(head) - 1]


# --------------------------------------------------------------------------------------------------
# The grammar's own cases.  Each is a statement about the grammar and not about the inventory.
_CASES = [
    ('a/B.lean: N.x', [('a/B.lean', 'N.x')]),
    ('a/B.lean: N.x, N.y', [('a/B.lean', 'N.x'), ('a/B.lean', 'N.y')]),
    # ** THE CASE THE FIRST GATE GOT WRONG: a later group's name against the first group's file. **
    ('a/B.lean: N.x | c/D.lean: N.yyyyyyyy',
     [('a/B.lean', 'N.x'), ('c/D.lean', 'N.yyyyyyyy')]),
    ('  a/B.lean : N.x ,N.y |c/D.lean:N.z  ',
     [('a/B.lean', 'N.x'), ('a/B.lean', 'N.y'), ('c/D.lean', 'N.z')]),
    ('', []),
    ('-', []),
    (None, []),
]
_RAISES = ['N.x', 'a/B.lean', 'a/B.lean:', 'a/B.txt: N.x', 'a/B.lean: 9bad']


def selftest():
    bad = 0
    for cell, want in _CASES:
        got = parse_decl(cell)
        if got != want:
            print(f'  [FAIL] {cell!r}\n         want {want}\n          got {got}')
            bad += 1
    for cell in _RAISES:
        try:
            parse_decl(cell)
        except DeclCellError:
            continue
        print(f'  [FAIL] {cell!r} parsed but should have raised')
        bad += 1
    # ** THE SEED: the grammar must distinguish the two readings on a real multi-group cell, or this
    #   module is not doing the thing it exists for.  r7421's rule -- a check whose population can be
    #   empty must prove in its own run that it could have fired -- applied to a parser.
    multi = 'x/A.lean: N.short | y/B.lean: N.the_longest_token_here'
    pairs = parse_decl(multi)
    first_path = pairs[0][0]
    longest = max((n for _, n in pairs), key=len)
    if (first_path, longest) in pairs:
        print('  [FAIL] SEED: the mispairing the old parser made is not distinguishable here')
        bad += 1
    print(f'  decl_cells selftest: {len(_CASES) + len(_RAISES) + 1} case(s), '
          f'{"ALL PASS" if not bad else str(bad) + " FAILED"}')
    return 1 if bad else 0


def audit():
    head, rows = read_rows()
    if 'decl' not in head:
        print('  ROWS.tsv carries no `decl` column'); return 1
    pairs = groups = withdecl = multi = 0
    errs = []
    for r in rows:
        try:
            p = parse_decl(r.get('decl'))
        except DeclCellError as e:
            errs.append((r.get('index'), str(e))); continue
        if not p:
            continue
        withdecl += 1
        pairs += len(p)
        ng = len({f for f, _ in p})
        groups += ng
        if ng > 1:
            multi += 1
    print(f'  rows                       : {len(rows)}')
    print(f'  rows with a decl claim     : {withdecl}')
    print(f'  (file, name) pairs claimed : {pairs}')
    print(f'  file groups                : {groups}')
    print(f'  rows with >1 group         : {multi}  '
          f'<- a one-pair-per-row reader mispairs here')
    print(f'  ⇒ a one-pair-per-row reader covers {withdecl} of {pairs} pairs '
          f'({100 * withdecl // max(pairs, 1)} %)')
    for idx, e in errs:
        print(f'  [FAIL] row {idx}: {e}')
    return 1 if errs else 0


if __name__ == '__main__':
    if '--audit' in sys.argv:
        sys.exit(audit())
    sys.exit(selftest())

#!/usr/bin/env python3
"""index_rows.py -- ONE READER FOR `receipts/INDEX.md`, BECAUSE THERE WERE FIVE AND THEY DISAGREED.

** WHY THIS FILE EXISTS, and it is a count rather than an argument. **  Five scripts each carried
their OWN copy of the same row filter:

    corpus/check_receipts.py          line 22
    corpus/make_receipt_appendix.py   line 29
    corpus/check_supersession.py      line 104   (narrower still -- no '| `' branch at all)
    scripts/run_all_receipts.py       line 83
    scripts/work_entry_points.py      line 141

*** and FOUR of them had already been patched SEPARATELY for the same class of loss ***: r2376+c54.36
added the `` | `stem` `` format; c54.203 fixed `check_receipts` and `make_receipt_appendix` for the
lowercase `p0`; r2555 fixed the runner for the same `p0` a second time, in its own words "the fourth
instance of the silent-discard class".  ** Each fix landed in one copy.  A fifth divergence was not a
risk, it was a schedule. **

** ⛭⛭ AND THE FIFTH ARRIVED.  The filter was `ln[:3].upper().startswith('| P') or ln.startswith('| `')`
-- it decides membership by the PAPER column -- and the corpus writes an EM-DASH in that column for a
receipt that supports no paper.  ** Twenty rows.  Eighteen of them name a receipt that exists on disk,
so the runner had never run any of the eighteen, and a green run said nothing about them. **

  ⇒ *** ONE OF THE EIGHTEEN FAILS. ***  `L230_computes_convention/C1` -- see its own corrected head.

** ⌗ AND THE PART THAT IS NOT JUST ANOTHER INSTANCE.  `check_receipts` carries a COLUMN LINT, and that
lint sits INSIDE the loop the filter guards. **  So the lint never saw an em-dash row -- and TWO
em-dash rows were column-split (10 cells and 12, on `\\|aH\\|` and `\\|T\\|^2+\\|R\\|^2=1`), sitting in
the file since r2674.
  ⇒ *** cc54's r2772 note, which is why `check_register_columns` was built, reads: "the identical string
      went into the INDEX row, ** where your column lint caught it instantly **."  That is true of the
      rows the filter admits and false of the rows it drops -- and the falsifying pair was in the file
      as the sentence was written.  ** A lint downstream of a filter inherits the filter's blind spot,
      and reports green from inside it. ***

** ⛔ THE OTHER HALF: RESOLUTION WAS SILENT TOO. **  Every copy did `if os.path.exists(f)` and moved on
when it did not.  Six path cells do not resolve, and the reasons are not the same:
  * four name `storyboard_receipts/...` at the repository ROOT while the readers prepend `receipts/`;
  * `X4_singularity_types.py` and `X3_seam_schwarz_reflection.py` ** have never existed in any of the
    486 commits reachable from any ref **, and both are emitted into P3's, P7's and the corpus
    appendix marked `[OK]`.
  ⇒ *** So the registry was validated from CITATIONS INWARD -- `\\rcpt{stem}` must resolve to a row and a
      file -- and never from ROWS OUTWARD.  An UNCITED row naming a file that does not exist is invisible
      to every gate and visible to every reader of the appendix. ***

** WHAT THIS MODULE DOES AND DOES NOT DECIDE. **  It parses; it does not judge.  `resolve=` is off by
default so a caller that only wants cells pays nothing.  ** It does not skip an unresolvable row --
it returns it with `paths == []` and lets the caller fail. **  *A reader that drops what it cannot
resolve is the defect this file exists to remove; a reader that dropped it QUIETLY would be the same
defect wearing a new name.*

Written c54.222 (`L-556`).  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
INDEX = os.path.join(ROOT, 'receipts', 'INDEX.md')

#: the header's cell count.  A row with any other count has an unescaped `|` in a cell.
EXPECT_CELLS = 8

_RAW_PIPE = re.compile(r'(?<!\\)\|')
_BACKTICKED = re.compile(r'`([^`]+)`')


def split_cells(line):
    """the row's cells, unescaping `\\|` INSIDE a cell -- or None if the line is not a table row"""
    if not line.startswith('|'):
        return None
    parts = _RAW_PIPE.split(line.rstrip('\n'))
    if len(parts) < 3:
        return None
    return [p.replace('\\|', '|').strip() for p in parts[1:-1]]


def is_data_row(cells):
    """the header and the `|---|` separator are the only two non-data rows the file has.

    ** The old filter asked what the PAPER column CONTAINS.  This one asks only whether the row is
    the header or the rule. **  *A membership test that reads a content column excludes content.*
    """
    if cells is None or len(cells) < 4:
        return False
    c0 = cells[0]
    if c0 == 'paper':
        return False
    if c0 and set(c0) <= set('-: '):      # the markdown alignment rule
        return False
    return True


def path_token(cells):
    """the path cell's backticked token -- `` `a/b.py` (six) `` is a PATH plus a parenthetical.

    ** Falls back to a bare strip so a row written without backticks still resolves. **
    """
    cell = cells[3]
    m = _BACKTICKED.search(cell)
    return (m.group(1) if m else cell).strip()


def resolve(token, root=ROOT):
    """absolute path(s) for a path token, globbed, searched BOTH under `receipts/` and from ROOT.

    ** Both, because four registered rows name `storyboard_receipts/...` at the repository root and
    every previous reader prepended `receipts/` unconditionally and then dropped the miss. **
    Returns `[]` when nothing matches -- which is a FINDING for the caller, not a skip.
    """
    tok = token[len('receipts/'):] if token.startswith('receipts/') else token
    out = []
    for base in (os.path.join(root, 'receipts'), root):
        out += sorted(glob.glob(os.path.join(base, tok)))
    seen, uniq = set(), []
    for p in out:
        rp = os.path.realpath(p)
        if rp not in seen and os.path.isfile(p):
            seen.add(rp)
            uniq.append(p)
    return uniq


class Row(object):
    """one INDEX row.  `cells` is raw; the named fields are the header's meaning of each cell."""

    __slots__ = ('lineno', 'cells', 'token', 'paths')

    def __init__(self, lineno, cells, resolve_paths, root):
        self.lineno = lineno
        self.cells = cells
        self.token = path_token(cells)
        self.paths = resolve(self.token, root) if resolve_paths else None

    paper = property(lambda s: s.cells[0])
    label = property(lambda s: s.cells[1])
    claim = property(lambda s: s.cells[2])
    path = property(lambda s: s.token)
    status = property(lambda s: s.cells[4] if len(s.cells) > 4 else '')
    computes = property(lambda s: s.cells[5] if len(s.cells) > 5 else '')
    bound = property(lambda s: s.cells[6] if len(s.cells) > 6 else '')
    origin = property(lambda s: s.cells[7] if len(s.cells) > 7 else '')
    stem = property(lambda s: os.path.splitext(os.path.basename(s.token))[0])
    #: a row may register a `.md` kill record; that is registered and not runnable.
    runnable = property(lambda s: s.token.endswith('.py'))
    well_formed = property(lambda s: len(s.cells) == EXPECT_CELLS)

    def __repr__(self):
        return '<Row %d %s %r>' % (self.lineno, self.paper, self.token)


def rows(index=INDEX, resolve_paths=False, root=ROOT):
    """every data row of the INDEX, in file order, header and rule excluded and nothing else."""
    out = []
    with open(index, encoding='utf-8', errors='replace') as fh:
        for n, line in enumerate(fh, 1):
            cells = split_cells(line)
            if not is_data_row(cells):
                continue
            out.append(Row(n, cells, resolve_paths, root))
    return out


def main():
    """a census, so the module is runnable and its own numbers are printable"""
    rs = rows(resolve_paths=True)
    bad = [r for r in rs if not r.well_formed]
    unres = [r for r in rs if r.runnable and not r.paths]
    print()
    print('  index_rows -- the census this module exists to make possible')
    print()
    print(f'    {len(rs)} data row(s)')
    print(f'    {len(bad)} with a cell count other than {EXPECT_CELLS}')
    for r in bad:
        print(f'      line {r.lineno}: {len(r.cells)} cells')
    print(f'    {len(unres)} runnable row(s) whose path does not resolve')
    for r in unres:
        print(f'      line {r.lineno}: {r.token}')
    print()
    return 1 if (bad or unres) else 0


if __name__ == '__main__':
    raise SystemExit(main())

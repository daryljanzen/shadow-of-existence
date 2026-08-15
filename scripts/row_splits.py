#!/usr/bin/env python3
"""row_splits.py -- PARTITION A REGISTER'S OFF-COUNT ROWS INTO "blind-fixable" AND "not".

** WHY.  `check_arcpins`/`check_register_columns` report `THE_LIVE_ARC.md`'s column breaks with a
baseline and call the backlog "not blind-fixable". **  *That is true of the backlog as a whole and it
is not true of every row in it, and the difference is measurable rather than arguable.*

** ⛭ THE TWO CAUSES LOOK IDENTICAL IN A COUNT AND ARE NOT ALIKE AT ALL. **

  * ** A SPLIT ** -- a raw `|` inside `$...$` or `` `...` `` -- adds cells.  Markdown reads it as a cell
    boundary; the author meant an absolute value, a norm, a restriction bar, or a quoted table row.
    *** Escaping it is mechanical, and it is VERIFIABLE: the only edit is inserting backslashes before
    pipes, so `new.replace('\\|','|') == old` must hold exactly, and the row must land on the modal
    cell count.  Both together leave no room for a wrong repair. ***
  * ** A MISSING OR EXTRA CELL ** -- the row is short or long as WRITTEN.  *** Repairing that means
    supplying content, which is a reading and not a repair. ***

⇒ ** A row can be BOTH, and c54.229 called those unfixable.  THAT WAS WRONG, and r2802 is why: **
  *"escaping does not need to know which cell a stray bar belonged to -- a raw bar written as an escaped
  one stays content in the cell it is already in."*  *** The two defects are INDEPENDENT.  Escaping a
  both-row leaves it short, which it already was, and no longer split. ***  The tool escapes it, reports
  that it is still off the mode, and leaves the SHAPE to a reader.

** WHAT IT DOES. **  Dry-run by default: it reports, per row, the count before, the count after
escaping in-span pipes, and which of the three classes the row falls in.  With `--apply` it writes
ONLY the rows that both verify losslessly and land on the modal count.

    python3 scripts/row_splits.py                          # THE_LIVE_ARC.md, dry run
    python3 scripts/row_splits.py --file PROTECTED_OPEN.md
    python3 scripts/row_splits.py --apply --band 500-799   # only rows in one node's ID band

** ⌷ AND THE BAND FILTER IS NOT A CONVENIENCE. **  `CLAIMS.md`: *"never edit a row in another node's
band; route instead."*  A tool that could repair every row in a shared register is a tool that will,
so the band is an argument and there is no default that spans them.

Written c54.229 (`L-562`).  Stated for reversal.
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
RAW = re.compile(r'(?<!\\)\|')
ROWID = re.compile(r'\|\s*(?:~~)?\s*\*?\*?(?:PO-|L-)(\d+)')


def cells(line):
    return len(RAW.split(line)) - 2


def raw_in_span(line):
    """positions of every UNESCAPED `|` that lies inside a `$...$` or `` `...` `` span

    ** ⛔ THIS IS THE INVARIANT c54.229 AND r2802 BOTH MISSED, AND IT IS SHARPER THAN THE CELL COUNT. **
    A row can carry the modal number of cells and have its BOUNDARIES IN THE WRONG PLACES: escape three
    structural bars and leave three content bars raw and the count is unchanged while the columns have
    moved.  *** `L-551` came out of the two sweeps in exactly that state on one line and correctly on
    the other, and both copies passed a count check. ***
      ⇒ ** A register row is well formed when every RAW bar is structural -- not when there are the
        right number of them. **
    """
    out, i, n, inmath, incode = [], 0, len(line), False, False
    while i < n:
        ch = line[i]
        if ch == '\\' and i + 1 < n:
            i += 2
            continue
        if ch == '`':
            incode = not incode
        elif ch == '$' and not incode:
            inmath = not inmath
        elif ch == '|' and (inmath or incode):
            out.append(i)
        i += 1
    return out


def escape_in_spans(line):
    """escape every unescaped `|` inside a `$...$` math span or a `` `...` `` code span

    ** The scanner is a state machine over the line, not a regex. **  *A regex for "inside a span"
    cannot be written correctly for nested and adjacent delimiters, and the failure mode is silent --
    it escapes a STRUCTURAL pipe and the row loses a cell.  The caller's losslessness check would
    catch it; not needing to rely on that is better.*
    """
    out, i, n, inmath, incode = [], 0, len(line), False, False
    while i < n:
        ch = line[i]
        if ch == '\\' and i + 1 < n:                     # an already-escaped character, taken whole
            out.append(line[i:i + 2])
            i += 2
            continue
        if ch == '`':
            incode = not incode
        elif ch == '$' and not incode:
            inmath = not inmath
        elif ch == '|' and (inmath or incode):
            out.append('\\|')
            i += 1
            continue
        out.append(ch)
        i += 1
    return ''.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--file', default='THE_LIVE_ARC.md')
    ap.add_argument('--band', default='', help='ID range to touch, e.g. 500-799')
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()

    path = os.path.join(ROOT, a.file)
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    idx = [i for i, l in enumerate(lines) if ROWID.match(l)]
    if not idx:
        print(f'  [FAIL] no register rows found in {a.file} -- the reader is broken, not the file')
        return 1
    modal = collections.Counter(cells(lines[i]) for i in idx).most_common(1)[0][0]

    lo, hi = (0, 10 ** 9)
    if a.band:
        lo, hi = (int(x) for x in a.band.split('-'))

    fixable, both, shape, skipped = [], [], [], 0   # `both` = escapable, still off the mode
    for i in idx:
        c = cells(lines[i])
        if c == modal:
            continue
        rid = int(ROWID.match(lines[i]).group(1))
        if not (lo <= rid <= hi):
            skipped += 1
            continue
        new = escape_in_spans(lines[i])
        # ** the complete verification: the ONLY edit permitted is inserting `\` before a `|`. **
        if new.replace('\\|', '|') != lines[i].replace('\\|', '|'):
            shape.append((i + 1, rid, c, None, 'REFUSED -- the escape was not lossless'))
            continue
        c2 = cells(new)
        # ** ⛭⛭ CORRECTED c54.230, against this tool's own first reading.  IT REQUIRED THE ROW TO LAND
        # ** ON THE MODAL COUNT, and that conflated two independent defects. **  The observer line's
        # ** r2802: *"escaping does not need to know which cell a stray bar belonged to -- a raw bar
        # ** written as an escaped one stays content in the cell it is already in."*
        #   ⇒ *** So a row that is BOTH split and short is still safely escapable: it comes out short,
        #       which it already was, and no longer split.  The two conditions that make the escape safe
        #       are LOSSLESSNESS and that the bar was in a span -- not the resulting count. ***
        # ** The count is still reported, because a row that does not reach the modal count after
        # escaping still needs a reader.  What is corrected is calling it unfixable. **
        if c2 != c:
            (fixable if c2 == modal else both).append((i + 1, rid, c, c2, new))
        else:
            shape.append((i + 1, rid, c, c2, 'shape only -- supplying a cell is a reading'))

    print()
    print(f'  row_splits -- {a.file}: {len(idx)} rows, modal cell count {modal}'
          + (f', band {a.band}' if a.band else ''))
    print()
    print(f'    {len(fixable):3d} BLIND-FIXABLE   a split only; escaping lands it on {modal}')
    for ln, rid, c, c2, _ in fixable:
        print(f'          line {ln:5d}  id {rid:<5d} {c} -> {c2}')
    print(f'    {len(both):3d} SPLIT AND SHORT the escape is still safe; the row stays off the mode')
    for ln, rid, c, c2, _ in both:
        print(f'          line {ln:5d}  id {rid:<5d} {c} -> {c2} after escaping, still not {modal}')
    print(f'    {len(shape):3d} SHAPE ONLY      no in-span pipe; the row is short or long as written')
    # ** and the sharper property, which a cell count cannot see (see `raw_in_span`) **
    misplaced = [(i + 1, int(ROWID.match(lines[i]).group(1)), len(raw_in_span(lines[i])))
                 for i in idx if raw_in_span(lines[i])
                 and lo <= int(ROWID.match(lines[i]).group(1)) <= hi]
    print()
    print(f'    {len(misplaced):3d} MIS-BOUNDED     a RAW bar still inside a span -- the row may carry the')
    print(f'                        modal count with its columns in the WRONG PLACES')
    for ln, rid, k in misplaced[:12]:
        print(f'          line {ln:5d}  id {rid:<5d} {k} raw bar(s) inside a span')
    if len(misplaced) > 12:
        print(f'          ... and {len(misplaced)-12} more')
    if misplaced:
        print()
        print('       ⌗ ** REPORTED AND NOT WRITTEN, deliberately. **  *Escaping a mis-bounded row that')
        print('         already carries the modal count makes its cell count WORSE by the count metric')
        print('         and RIGHT by the boundary one -- one of these rows goes 5 -> 3.*')
        print('       ⇒ *** So the metric a gate baselines on is the thing in question, and moving rows')
        print('           under a baseline while disputing the baseline is not a repair. ***')
    if skipped:
        print(f'    {skipped:3d} outside the band, untouched')
    print()

    if not a.apply:
        print('    ⌗ dry run.  `--apply` writes ONLY the blind-fixable rows, and only inside a band.')
        print()
        return 0
    if not a.band:
        print('    ⛔ REFUSING TO APPLY WITHOUT --band.  A register is shared; `CLAIMS.md` says a node')
        print('       never edits a row in another node\'s band.  Name the band you own.')
        print()
        return 1
    for ln, rid, c, c2, new in fixable + both:
        lines[ln - 1] = new
    open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    print(f'    wrote {len(fixable) + len(both)} row(s) (escapes only).  {len(shape)} shape-only '
          f'rows left for a reader, and {len(both)} of the written ones are still off the mode.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

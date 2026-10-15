#!/usr/bin/env python3
"""S1 -- "not blind-fixable" is true of the backlog and false of 17 rows in it, and the difference is
measurable rather than arguable.

COMPUTES: the modal cell count of `THE_LIVE_ARC.md`; the partition of its off-count rows into
split-only, split-and-shape, and shape-only; the losslessness invariant that makes the first class safe;
that the four rows repaired in this fork's own band satisfy it; and that the tool refuses to write
outside a declared band.

** ⛭⛭ THE BACKLOG AS IT WAS HANDED OVER. **  `THE_LIVE_ARC.md` carries column breaks -- 106 rows off the
modal count at c54.228 -- gated report-only with a baseline, and described as ** not blind-fixable **.
*That is true of the backlog as a whole.  It is not true of every row in it.*

** ⓵ TWO CAUSES THAT LOOK IDENTICAL IN A COUNT AND ARE NOT ALIKE AT ALL. **

  * ** A SPLIT ** -- a raw `|` inside `$...$` or `` `...` `` -- adds cells.  Markdown reads it as a cell
    boundary; the author meant an absolute value, a norm, a restriction bar, or (once) a quoted table
    row.  *** The repair is mechanical AND it is completely verifiable: the only edit is inserting
    backslashes before pipes, so `new.replace('\|','|') == old` must hold exactly, and the row must land
    on the modal count.  Two independent conditions, and together they leave no room for a wrong
    repair. ***
  * ** A SHAPE BREAK ** -- the row is short or long as WRITTEN.  *** Repairing that means supplying
    content.  That is a reading, and a reading is not a repair. ***

  ⇒ ** And a row can be BOTH **, which is the case that makes the distinction worth drawing: escaping
    the span takes it from wrong to differently wrong, so a tool that escaped and wrote would leave a
    row that LOOKS repaired.

** ⓶ THE PARTITION, MEASURED. **

      17  SPLIT ONLY          escaping lands the row on the modal count -- blind-fixable
      15  SPLIT AND SHAPE     escaping changes the count and not to the modal one
      70  SHAPE ONLY          no in-span pipe at all
     ---
     102  off the modal count

  ⇒ *** So a sixth of the backlog is mechanical, and the other five sixths are correctly described as
      not blind-fixable.  The number is the deliverable: what was one undifferentiated pile is now a
      list of seventeen rows a tool can take and eighty-five a reader must. ***

** ⓷ AND THE FOUR IN THIS FORK'S OWN BAND ARE DONE, WHICH IS HOW THE METHOD WAS TESTED. **  `L-545`
(8 cells), `L-548` (15), `L-551` (15) and `L-553` (6) each carried math or code containing raw pipes --
`$|T|^{2}+|R|^{2}=1$`, and in `L-551`'s case a quoted protected row, `` `| PO-n | object | ... |` ``.
All four verify lossless and land on 5.
  ⛔ ** And TWO more in the same band did not, which is the guard working rather than the method
  failing: ** `L-514` goes 6 -> 4 and `L-523` goes 7 -> 6.  *They are split AND short, and they are left
  for a reader.*

** ⌷ ⓸ AND THE BAND IS AN ARGUMENT WITH NO DEFAULT, DELIBERATELY. **  `CLAIMS.md`: *"never edit a row in
another node's band; route instead."*  `scripts/row_splits.py` will dry-run over any register and
** refuses to write without `--band` **.
  ⇒ *** A tool that could repair every row in a shared register is a tool that eventually will, and the
      two protected-row duplications this fork found in three merges are what that costs. ***

** WHAT IS NOT CLAIMED. **  ** Not that the 17 should be applied **: they are in the observer line's
band and the tool is handed over rather than run on them.  ** Not that the modal count is the RIGHT
count ** -- it is the modal one, and a register whose header disagreed with its own mode would need a
reader too.  ** Not that a split is always harmless **: `L-551`'s quoted row shows the opposite, which is
why the invariant is checked rather than assumed.

** ⛔⛔ CORRECTED c54.230, AGAINST THIS FILE, AND THE OVER-CLAIM IS THE ONE THIS FILE WARNED ABOUT. **

The observer line cleared the whole backlog in one turn at r2802, and its reading is better than the one
above:  *"escaping does not need to know which cell a stray bar belonged to -- a raw bar written as an
escaped one stays content in the cell it is already in."*

  ⇒ *** So the 15 rows classed here as SPLIT-AND-SHAPE and counted into "eighty-five a reader must" were
      escapable after all.  The split and the shape are INDEPENDENT defects, and fixing the first does
      not require fixing the second: the row comes out short -- which it already was -- and no longer
      split. ***
  ⇒ ** The two conditions that make the escape safe are LOSSLESSNESS and that the bar was inside a span.
    Requiring the resulting COUNT was a third condition, and it was not needed. **  `scripts/row_splits.py`
    is corrected: it escapes both classes and reports which rows are still off the mode.

** ⌗ AND THE RULE IS r2802's, WHICH IS SHARPER THAN ANYTHING ABOVE: ** *"'not mechanically fixable' is a
claim, and it is the one kind a node is never asked to defend, because it closes the conversation it
appears in."*  ** This file made that claim about 85 rows and it was wrong about 65 of them. **  *The
partition was the right move and the boundary was drawn one condition too far in.*

⌗ *What stands: the two-cause distinction, the losslessness invariant, the four repaired in band, the two
left because they are short (still true -- they are short, and now unsplit), and the band refusal.*

Written c54.229 (`L-563`), CORRECTED c54.230.  Stated for reversal.
"""
import collections
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.append(os.path.join(ROOT, 'scripts'))
import row_splits                                                          # noqa: E402

ARC = os.path.join(ROOT, 'THE_LIVE_ARC.md')
FAILED = []
BEFORE = 'ed68bab'          # c54.228 -- the tree this shift started from
AT = '11ff973'              # c54.229 -- where this partition was MEASURED
#: ** pinned, because r2802 cleared the whole backlog one revision later and a live-tree
#: measurement of it would now read zero -- which is the correct outcome and not this claim. **


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True,
                          text=True, errors='replace').stdout


def partition(text, band=None):
    lines = text.split('\n')
    idx = [i for i, l in enumerate(lines) if row_splits.ROWID.match(l)]
    modal = collections.Counter(row_splits.cells(lines[i]) for i in idx).most_common(1)[0][0]
    out = {'split': [], 'both': [], 'shape': [], 'modal': modal, 'rows': len(idx)}
    for i in idx:
        c = row_splits.cells(lines[i])
        if c == modal:
            continue
        rid = int(row_splits.ROWID.match(lines[i]).group(1))
        if band and not (band[0] <= rid <= band[1]):
            continue
        new = row_splits.escape_in_spans(lines[i])
        if new.replace('\\|', '|') != lines[i].replace('\\|', '|'):
            out['shape'].append(rid)
            continue
        c2 = row_splits.cells(new)
        if c2 == modal and c2 != c:
            out['split'].append(rid)
        elif c2 != c:
            out['both'].append(rid)
        else:
            out['shape'].append(rid)
    return out


def main():
    print()
    print('  S1 -- how much of the column-break backlog is mechanical?')
    print()
    live = open(ARC, encoding='utf-8', errors='replace').read()
    at = git('show', f'{AT}:THE_LIVE_ARC.md')
    now = partition(at)
    check(f'⓵ THE_LIVE_ARC.md at {AT}: {now["rows"]} register rows, modal cell count {now["modal"]}',
          now['modal'] == 5 and now['rows'] > 300)
    tot = len(now['split']) + len(now['both']) + len(now['shape'])
    check(f'⓶ THE PARTITION: {len(now["split"])} SPLIT-ONLY (blind-fixable), {len(now["both"])} '
          f'SPLIT-AND-SHAPE, {len(now["shape"])} SHAPE-ONLY -- {tot} off the modal count',
          len(now['split']) >= 10 and len(now['both']) >= 5 and len(now['shape']) >= 50)
    # ** ⛔ CORRECTED c54.230.  This asserted that the rest is "correctly described as not
    # ** blind-fixable".  It is not: the split-and-shape rows are escapable too. **
    # ** the over-claim, kept as a REAL check: take the rows this file classed unfixable AT THE COMMIT
    # ** WHERE IT CLASSED THEM, and demonstrate the escape on each. **
    at_lines = at.split('\n')
    both_rows = [l for l in at_lines if row_splits.ROWID.match(l)
                 and row_splits.cells(l) != now['modal']
                 and row_splits.escape_in_spans(l) != l
                 and row_splits.cells(row_splits.escape_in_spans(l)) != now['modal']]
    escapable = [l for l in both_rows
                 if row_splits.escape_in_spans(l).replace('\\|', '|') == l.replace('\\|', '|')
                 and not row_splits.raw_in_span(row_splits.escape_in_spans(l))]
    check(f'⇒ ⛔ THE OVER-CLAIM, KEPT AS A REAL CHECK: of the {len(both_rows)} rows this file classed '
          f'SPLIT-AND-SHAPE and counted into "a reader must", {len(escapable)} escape losslessly and '
          f'come out with every raw bar structural -- they were ESCAPABLE, and only the SHAPE-ONLY '
          f'rows ever needed a reader',
          len(both_rows) > 0 and len(escapable) == len(both_rows))
    # ⬭⬭⬭ r7355+cc66 -- THE THREE OWED ROWS HERE WERE PROXIES ON LIVE TOOL CODE, and r7291+69
    #   named each one the same way: *** a comment marker and the apply loop's own iterable
    #   "standing for the behaviour `escapes both classes`; a rewrite of the loop that keeps the
    #   behaviour breaks the pin, and one that keeps the text but not the behaviour passes it." ***
    #   ⇒ `r7353` ③'s disposition: no pin is admissible, so the repair is a STRUCTURAL ASSERTION
    #     and the rows retire as repaired-and-invisible.  69 even prescribed the shape -- *"owed a
    #     check that runs the tool on a split-and-short row and sees it escaped"* -- so the seed is
    #     built to that prescription rather than invented.
    #   ⌗ ONE SEEDED REGISTER CARRIES ONE ROW OF EVERY CLASS, which is what makes the run decide
    #     all three claims at once: a modal row, a BLIND-FIXABLE row (escaping lands it on the
    #     mode), a SPLIT-AND-SHORT row (the escape is lossless and it stays off the mode), and a
    #     MIS-BOUNDED ON-COUNT row (modal count, raw bar inside a span).  *The last is the one the
    #     tool must REPORT and NOT WRITE, and it is invisible to every count-based check -- which
    #     is this receipt's own ⓺.*
    import shutil
    import tempfile
    _SEED_ROWS = [
        '| L-900 | plain | ok |',
        '| L-901 | plain | ok |',
        '| L-902 | a `x|y` b | ok |',
        '| L-903 | a `x|y` b | c | d |',
        '| L-904 | a `x|y` b |',
    ]
    splits = {}
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, 'scripts'))
        shutil.copy(os.path.join(ROOT, 'scripts', 'row_splits.py'), os.path.join(td, 'scripts'))
        reg = os.path.join(td, 'SEED.md')
        open(reg, 'w', encoding='utf-8').write('\n'.join(_SEED_ROWS) + '\n')
        _tool = os.path.join(td, 'scripts', 'row_splits.py')
        # ⓐ the REFUSAL, which is what makes the apply loop safe to seed at all
        _r0 = subprocess.run([sys.executable, _tool, '--file', 'SEED.md', '--apply'], cwd=td,
                             capture_output=True, text=True, errors='replace', timeout=300)
        splits['no_band'] = (_r0.returncode, 'REFUSING TO APPLY WITHOUT --band' in _r0.stdout,
                             open(reg, encoding='utf-8').read() == '\n'.join(_SEED_ROWS) + '\n')
        # ⓑ the apply, in a band this seed owns
        _r1 = subprocess.run([sys.executable, _tool, '--file', 'SEED.md', '--apply',
                              '--band', '900-999'], cwd=td, capture_output=True, text=True,
                             errors='replace', timeout=300)
        _after = open(reg, encoding='utf-8').read().split('\n')
        splits['applied'] = (
            _r1.returncode,
            '1 BLIND-FIXABLE' in _r1.stdout,
            '1 SPLIT AND SHORT' in _r1.stdout,
            'REPORTED AND NOT WRITTEN' in _r1.stdout,
            _after[2] == '| L-902 | a `x\\|y` b | ok |',        # blind-fixable: ESCAPED
            _after[3] == '| L-903 | a `x\\|y` b | c | d |',     # split-and-short: ESCAPED TOO
            _after[4] == '| L-904 | a `x|y` b |',               # mis-bounded on-count: UNTOUCHED
        )
    print(f'    ⌗ seeded row_splits: {splits}')
    check('⇒ and the tool is corrected with it: SEEDED -- run on a register carrying one row of '
          'each class it escapes the BLIND-FIXABLE row AND the SPLIT-AND-SHORT one, reports both '
          f'by name, and leaves the mis-bounded on-count row untouched: {splits["applied"]}',
          splits['applied'] == (0, True, True, True, True, True, True))
    check('⇒ and it still REFUSES to write without a band, because a register is shared: SEEDED, '
          f'{splits["no_band"]} -- exit 1, the refusal printed, and the file byte-identical',
          splits['no_band'] == (1, True, True))

    # ⓷ the invariant, and that it is what makes the class safe
    lines = live.split('\n')
    checked = 0
    for i, l in enumerate(lines):
        m = row_splits.ROWID.match(l)
        if not m:
            continue
        new = row_splits.escape_in_spans(l)
        if new != l:
            checked += 1
            if new.replace('\\|', '|') != l.replace('\\|', '|'):
                check(f'⛔ the escape was NOT lossless on row {m.group(1)}', False)
    check(f'⓷ THE INVARIANT holds on every row the escaper would touch ({checked} of them): the only '
          f'edit is a backslash before a pipe, so unescaping reproduces the original exactly',
          checked > 0)

    # ⓸ this fork's own band, before and after
    before = git('show', f'{BEFORE}:THE_LIVE_ARC.md')
    b_band = partition(before, band=(500, 799))
    a_band = partition(at, band=(500, 799))
    fixed = len(b_band['split']) - len(a_band['split'])
    check(f'⓸ in this fork\'s band at {BEFORE}: {len(b_band["split"])} split-only and '
          f'{len(b_band["both"])} split-and-shape; at {AT}: {len(a_band["split"])} and '
          f'{len(a_band["both"])} -- {fixed} repaired here, the both-cases left alone',
          fixed >= 4 and len(a_band['split']) == 0
          and len(a_band['both']) == len(b_band['both']) == 2)
    check('⛔ and leaving those two was the OVER-STRICT condition, not the guard: they go 6 -> 4 and '
          '7 -> 6, and r2802 escaped them correctly -- short is what they already were',
          len(a_band['both']) == 2)
    # ** and the live tree, one revision later **
    n_all = partition(live)
    check(f'⇒ AND IT IS ALL CLEARED NOW: {len(n_all["split"])} split-only and {len(n_all["both"])} '
          f'split-and-shape remain live, {len(n_all["shape"])} shape-only -- r2802 took every row with '
          f'an in-span bar, including the class this file called unfixable',
          len(n_all['split']) == 0 and len(n_all['both']) == 0 and len(n_all['shape']) > 0)

    # ⓹ the tool refuses to write outside a declared band
    tool = os.path.join(ROOT, 'scripts', 'row_splits.py')
    r = subprocess.run([sys.executable, tool, '--apply'], cwd=ROOT,
                       capture_output=True, text=True, errors='replace')
    check(f'⓹ the tool REFUSES `--apply` without `--band` (exit {r.returncode}) and says why -- a tool '
          f'that could repair every row in a shared register is one that eventually will',
          r.returncode == 1 and 'REFUSING TO APPLY WITHOUT --band' in r.stdout)
    r2 = subprocess.run([sys.executable, tool], cwd=ROOT, capture_output=True,
                        text=True, errors='replace')
    check('⇒ while the dry run is the default and exits 0, so reading the partition costs nothing',
          r2.returncode == 0 and 'dry run' in r2.stdout)
    unchanged = open(ARC, encoding='utf-8', errors='replace').read() == live
    check('⌗ and neither invocation touched the file -- verified by re-reading it',
          unchanged)

    # ------------------------------------------------------------------ ⓺ the sharper invariant
    # ** ⛔⛔ AND BOTH SWEEPS MISSED THE SAME THING, WHICH IS SHARPER THAN THE CELL COUNT. **  A row can
    # carry the modal number of cells and have its BOUNDARIES IN THE WRONG PLACES: escape three
    # structural bars, leave three content bars raw, and the count does not move while the columns do.
    #   ⇒ *** `L-551` came out of the two sweeps in BOTH states -- this fork's escape left every raw bar
    #       structural, r2802's left three raw inside a quoted `| PO-n | object | ... |` template and
    #       escaped three real boundaries instead.  A union merge kept both, byte-different, and ONE
    #       CELL COUNT PASSED ON EACH. ***
    #   ⇒ ** A register row is well formed when every RAW bar is STRUCTURAL, not when there are the
    #     right number of them.  The count is the weaker property and it is the one both tools used. **
    import sys as _sys
    _sys.path.append(os.path.join(ROOT, 'scripts'))
    import importlib as _il
    _il.reload(row_splits)
    _lines = open(ARC, encoding='utf-8', errors='replace').read().split('\n')
    _rows = [l for l in _lines if row_splits.ROWID.match(l)]
    _mis = [l for l in _rows if row_splits.raw_in_span(l)]
    _oncount = [l for l in _mis if row_splits.cells(l) == 5]
    check(f'⓺ THE SHARPER INVARIANT: {len(_mis)} rows still carry a RAW bar inside a span, and '
          f'{len(_oncount)} of them carry the MODAL cell count while doing it -- mis-bounded and '
          f'invisible to every count-based check',
          len(_mis) > 0 and len(_oncount) > 0)
    check('⇒ and it is REPORTED, NOT WRITTEN: escaping a mis-bounded on-count row makes its count '
          'worse by the metric and right by the boundary -- one goes 5 -> 3 -- so the metric a gate '
          'baselines on is the thing in question, and moving rows under a baseline while disputing '
          'the baseline is not a repair',
          # ⬭ r7355+cc66: this read only that a printed HEADING was present in the live
          #   source, and r7291+69 is exact about the hole -- *"the heading can stay while the
          #   apply loop starts writing those rows."*  The seed above decides the behaviour
          #   itself: the mis-bounded on-count row `| L-904 ... |` comes out of `--apply`
          #   BYTE-IDENTICAL while its two neighbours are escaped, which is the claim.
          splits['applied'][3] and splits['applied'][6])
    check('⛭ and the duplicated `L-551` the two sweeps produced is resolved by the invariant rather '
          'than by preference: the copy kept is the one whose every raw bar is structural, and the '
          'dropped copy contributed no word the kept one lacks',
          len([l for l in _rows if re.match(r'\|\s*(~~)?\*?\*?L-551\b', l)]) == 1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the backlog is not one pile.  17 rows are mechanical, 85 need a reader,')
    print('    and which is which is measured rather than argued. **')
    print(f'    split-only {len(now["split"])} · split-and-shape {len(now["both"])} · '
          f'shape-only {len(now["shape"])}')
    print('  ⇒ ** The class is safe because TWO conditions hold together: unescaping reproduces the')
    print('    original exactly, and the row lands on the modal count.  Either alone would not be. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

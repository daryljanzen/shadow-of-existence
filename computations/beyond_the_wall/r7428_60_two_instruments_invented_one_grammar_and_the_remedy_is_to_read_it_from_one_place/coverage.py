#!/usr/bin/env python3
"""r7428 -- the coverage figures of arms ⒝ and Ⓠ, re-derived from the data rather than quoted.

`r7417` ②'s lesson applied to a count: a figure carried forward instead of re-measured is the defect.
So this re-derives, from `ROWS.tsv` and the Lean tree:

  * how many `(file, name)` pairs the inventory claims, and over how many rows and groups;
  * how many of those a ONE-PAIR-PER-ROW reader reaches -- the coverage `_split_decl` had;
  * which pairs that reader MISPAIRS, and whether each mispairing is a red on correct data;
  * how many cleared pairs clear on the fully qualified name and how many only on its last component,
    which is `Ⓠ`'s measurement of the shared reader's `end` handling.

    python3 computations/beyond_the_wall/r7428_60_*/coverage.py
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import decl_cells as dc                                    # noqa: E402
import check_formalisation_join as fj                       # noqa: E402


def old_split(cell):
    """`_split_decl` as it stood at `r7426`: the FIRST `.lean` path, the LONGEST dotted token anywhere."""
    m = re.search(r'([\w./\-]+\.lean)', cell or '')
    if not m:
        return None, (cell or '').strip()
    path = m.group(1)
    rest = ((cell[:m.start()] + ' ' + cell[m.end():]).replace(',', ' ').replace(':', ' '))
    toks = [t for t in rest.split() if re.fullmatch(r"[A-Za-z_][\w.']*", t or '')]
    return path, (max(toks, key=len) if toks else '')


def main():
    head, rows = dc.read_rows()
    claim = [r for r in rows if not dc._empty(r.get('decl'))]
    pairs = [(r.get('index'), p, n) for r in claim for p, n in dc.parse_decl(r.get('decl'))]
    groups = sum(len({p for p, _ in dc.parse_decl(r.get('decl'))}) for r in claim)
    multi = sum(1 for r in claim if len({p for p, _ in dc.parse_decl(r.get('decl'))}) > 1)

    print('  THE POPULATION')
    print(f'      rows in the inventory                      : {len(rows)}')
    print(f'      rows carrying a `decl` claim               : {len(claim)}')
    print(f'      `(file, name)` pairs claimed               : {len(pairs)}')
    print(f'      file groups                                : {groups}')
    print(f'      rows carrying MORE THAN ONE group          : {multi}')

    print('\n  WHAT A ONE-PAIR-PER-ROW READER REACHED')
    seen, wrong = [], []
    for r in claim:
        got = dc.parse_decl(r.get('decl'))
        p, n = old_split(r.get('decl'))
        seen.append((r.get('index'), p, n))
        if (p, n) not in got:
            wrong.append((r.get('index'), p, n))
    print(f'      pairs it asserted                          : {len(seen)} of {len(pairs)} '
          f'({100 * len(seen) // len(pairs)} %)')
    print(f'      of those, pairs THE DATA DOES NOT CLAIM    : {len(wrong)}  <- its own mispairings')
    for idx, p, n in wrong:
        ds = dc.declared_names(p)
        real = [q for i, q, m in pairs if i == idx and m == n]
        print(f'        row {idx}: asserted `{n}` in {os.path.basename(p)}; the data claims it in '
              f'{", ".join(os.path.basename(x) for x in real) or "(nowhere)"} '
              f'-- {"DECLARED there" if ds is not None and n in (ds or ()) else "a red on correct data"}')

    print('\n  Ⓠ WHAT THE SHARED CHECK ACTUALLY CHECKS')
    strict = fb = conf = 0
    for _idx, p, n in pairs:
        ds = dc.declared_names(p)
        if ds is None:
            continue
        if n in ds:
            strict += 1
        elif n.split('.')[-1] in ds:
            fb += 1
            a = dc.lean_path(p)
            ctl = fj.declarations(a) if a else None
            conf += 1 if (ctl and n in ctl) else 0
    print(f'      cleared on the FULLY QUALIFIED name        : {strict}')
    print(f'      cleared ONLY on the last component         : {fb}')
    print(f'      of those, qualified under a MATCHING-`end` reader: {conf} of {fb}')
    print(f'      ⇒ {"the data is right on the strict reading; the fallback masks the reader" if conf == fb else "SOME pairs no reader confirms -- a question for the column"}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

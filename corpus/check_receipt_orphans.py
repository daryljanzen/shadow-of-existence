#!/usr/bin/env python3
"""check_receipt_orphans.py -- EVERY `receipts/**/*.py` MUST HAVE AN INDEX ROW, OR DECLARE WHY NOT.

** WHY.  This is the SYMMETRIC HALF of `L-556`, and the asymmetry is the whole point. **

c54.222 found that the registry was validated from CITATIONS INWARD -- a `\\rcpt{}` must reach a row and
a file -- and never from ROWS OUTWARD, so two rows named files that had never existed and were printed
into three appendices as `[OK]`.  ** `check_receipts` now fails on a row whose file is missing. **

  ⇒ *** And nothing asks the question the other way round: a FILE with no ROW. ***

** ⛭⛭ FOUR OF THEM, FOUND AT c54.225 BY A RECEIPT RATHER THAN A GATE. **  `P17`'s own receipt names
three -- `A3_the_convergence_audit`, `A6_item_58_resolves_split`, `A8_the_self_protecting_falsehood` --
and has been *failing on them*, which is where they surface.  The fourth, `bbn_network.py`, nothing
named at all.

  ** An unregistered receipt is invisible in a specific way, and it is not the same way as an
  unresolvable row. **  It is never run by `run_all_receipts` (which reads the INDEX), never reaches an
  appendix, never enters the assertion census, and never appears in the supersession scan.  *** It is a
  computation that exists and that the corpus does not know it has. ***

  ⌗ AND `bbn_network.py` IS SHARPER THAN THAT: it is named in `run_all_receipts`' own `SLOW` tuple.  **
  The runner carries a per-file timeout budget for a file it has never run **, because the budget is
  written by hand and the file list is read from the INDEX.

** ⌷ THE OPT-OUT IS A DECLARATION, NOT AN INFERENCE. **  Some files under `receipts/` are ENGINES --
libraries a receipt imports -- and they are correctly unregistered.  *This gate could infer that from
"is it imported anywhere", and deliberately does not:* ** an inference makes the exemption invisible and
silently exempts the next orphan that happens to be imported once. **  A file opts out by saying so in
its own docstring:

    NOT-A-RECEIPT: <one line on what it is instead>

*The corpus's own rule, `L-237`: a declaration is the only kind of thing this can gate.*

    python3 corpus/check_receipt_orphans.py

Written c54.225 (`L-559`).  Stated for reversal.
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.append(HERE)
import index_rows                                                          # noqa: E402

#: the declaration a non-receipt must carry, in its own docstring, to be exempt.
OPT_OUT = 'NOT-A-RECEIPT:'


def main():
    print()
    print('  check_receipt_orphans -- does every receipt file have a row that registers it?')
    print()
    registered = set()
    for r in index_rows.rows(resolve_paths=True):
        for p in (r.paths or []):
            registered.add(os.path.realpath(p))

    files = sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    orphans, declared = [], []
    for f in files:
        if os.path.realpath(f) in registered:
            continue
        head = ''
        try:
            head = open(f, encoding='utf-8', errors='replace').read(4000)
        except OSError:
            pass
        (declared if OPT_OUT in head else orphans).append(f)

    print(f'    {len(files)} receipt file(s) · {len(files) - len(orphans) - len(declared)} registered '
          f'· {len(declared)} declared {OPT_OUT[:-1]}')
    for f in declared:
        print(f'      [ok]   {os.path.relpath(f, ROOT)} -- declared, not inferred')
    if not orphans:
        print('    every receipt file is registered or declares why it is not.')
        print()
        return 0
    print()
    for f in orphans:
        print(f'    [FAIL] {os.path.relpath(f, ROOT)} -- on disk, in NO INDEX row')
    print()
    print('    ⛭ ** An unregistered receipt is never run by `run_all_receipts`, never reaches an')
    print('       appendix, never enters the assertion census and never appears in the supersession')
    print('       scan. **  *** It is a computation that exists and that the corpus does not know it')
    print('       has -- which is `L-556`\'s finding with the arrow reversed. ***')
    print('    ⌷ Register it in `receipts/INDEX.md`, or -- if it is an ENGINE a receipt imports --')
    print(f'       write `{OPT_OUT} <what it is instead>` into its docstring.  **Declared, not')
    print('       inferred: an inferred exemption is invisible and grows.**')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""check_receipt_tex_scope.py -- A RECEIPT THAT GREPS `corpus/*.tex` MUST NOT GREP THE GENERATED ONES.

** WHY.  `corpus/appendix_receipts_*.tex` are GENERATED FROM `receipts/INDEX.md`. **  Every receipt's
own `claim` and `computes` text is printed into them.

  ⇒ *** So a receipt that globs `corpus/*.tex` looking for a term it NAMES IN ITS OWN INDEX ROW will
      find ITSELF, and will report its own registration as evidence about the papers. ***
  ⇒ ** And the failure is DELAYED: it appears not when the receipt is written but the first time the
     appendices are regenerated after it is registered. **  *So it lands on whoever regenerates, which
     is not whoever wrote it.*

⛭ *Found c54.232 when `B59_the_routes_are_enumerable_and_one_is_absent` went red on a full run: it
checks that the SPECTRAL-TRIPLE route is "absent from the corpus entirely", and it was reading
`appendix_receipts_corpus.tex`, which carries its own row saying "spectral-triple".*
  ⇒ ** This is r2800's defect -- a finding written into the row it measures -- reached by a different
     route: the receipt did not write into the appendix, the GENERATOR did, from the row. **

** ⌗ WHAT IT CHECKS, AND WHY IT IS BASELINED RATHER THAN ABSOLUTE. **  35 receipts glob `corpus`
`.tex` with a wildcard.  ** THIRTY of them already exclude the generated appendices ** -- the
convention exists and is nearly universal, which is what makes the five exceptions a defect and not a
style.  *A gate that failed on all five would be a gate that arrives red, so the five are named as a
baseline: a NEW one fails, and the named ones are reported until they are cleared.*
  ⇒ *** The baseline NAMES the files rather than counting them.  A count can be satisfied by fixing
      one and breaking another, which is the hole c54.212 found in a different gate. ***

    python3 corpus/check_receipt_tex_scope.py

⛔⛭⛭ ** RE-LANDED r3105 (`L-249`), AND THE RE-LANDING IS ITSELF THE EVIDENCE. **  *This gate and the
`B59` repair were built at c54.232 in a span that was never absorbed — the fork line was declared
closed over it.  **So the repair left the tree, and `B59` found itself again**, this time in TWO
generated appendices rather than one, because a second receipt's row now names the term too.*
  ⇒ *** A FIX THAT IS NOT IN THE TREE IS NOT A FIX.  The population is unchanged across the whole
      span — 35 receipts glob corpus `.tex`, 30 exclude the generated appendices, 5 do not — which
      is what makes this a recurrence rather than a new instance. ***

Written c54.232 (`L-567`), re-landed r3105 (`L-249`).  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: a wildcard glob of corpus .tex -- the only pattern that can sweep a generated appendix in
_GLOB = re.compile(r"""glob[^\n]*['"]([^'"]*\*[^'"]*\.tex)['"]""")
#: the generated files, by the one prefix `make_all_appendices.py` writes
_GEN = 'appendix_receipts'

#: ** NAMED, not counted. **  Known at c54.232 and reported until cleared; a file not on this list
#: that globs corpus tex without excluding the generated appendices is a FAILURE.
BASELINE = {
    'receipts/L218_reader_package/R1_the_corpus_is_a_network_not_a_sequence.py',
    'receipts/L220_arrival_paths/V2_the_arrival_path_admits_no_metric.py',
    'receipts/L221_the_bridge/B33_the_ledger_branch_is_settled.py',
    'receipts/L221_the_bridge/B35_the_continuation_is_cited_wrong.py',
}


def main():
    print()
    print('  check_receipt_tex_scope -- does any receipt grep the GENERATED appendices as if they')
    print('  were papers?  (they are `receipts/INDEX.md` printed, so a receipt finds its own row)')
    print()
    globbers, offenders = [], []
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        src = open(f, encoding='utf-8', errors='replace').read()
        if not _GLOB.search(src):
            continue
        rel = os.path.relpath(f, ROOT)
        globbers.append(rel)
        if _GEN not in src:
            offenders.append(rel)

    new = sorted(set(offenders) - BASELINE)
    known = sorted(set(offenders) & BASELINE)
    gone = sorted(BASELINE - set(offenders))

    print(f'    {len(globbers)} receipt(s) glob corpus .tex with a wildcard')
    print(f'    {len(globbers) - len(offenders)} of them exclude `{_GEN}*` -- the convention')
    print(f'    {len(known)} known, still open (baselined by NAME at c54.232)')
    for r in known:
        print(f'          [known] {r}')
    if gone:
        print(f'    {len(gone)} baselined file(s) now CLEARED -- strike them from BASELINE:')
        for r in gone:
            print(f'          [clear] {r}')
    print()
    if not new:
        print('    no NEW receipt greps the generated appendices as prose.')
        print()
        return 0
    for r in new:
        print(f'    [FAIL] {r}')
        print(f'           globs corpus/*.tex and does not exclude `{_GEN}*`')
    print()
    print('    ⛭ ** The generated appendices carry every receipt\'s own claim and computes text. **')
    print('       *So an ABSENCE check over `corpus/*.tex` measures the INDEX as well as the papers,')
    print('       and a receipt that names a term in its row will report that term as present.*')
    print('    ⌷ Skip any basename starting `appendix_receipts`, as 30 receipts already do.')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())

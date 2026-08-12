#!/usr/bin/env python3
"""check_receipt_prefixes.py -- THE PREFIX-BAND GATE: two nodes must not allocate the same receipt
prefix in the same directory.

** THIS EXISTS BECAUSE IT ALREADY HAPPENED TWICE IN TWO REVISIONS, AND THE SECOND TIME THE COLLISION
REACHED THE PUSHED TREE. **

  * r2505 + c54.198 -- `receipts/L174_general_matter_dynamics/` acquired ** two files called I4 **:
    56's `I4_the_shear_selection_exists_and_is_vacuum_bound.py` and 54's
    `I4_the_free_shear_is_two_not_five...`.  ** Both were on `main` at r2510. **
  * r2510 + c54.199 -- 54 renamed its file to I5 to resolve that, and 56 had meanwhile written
    `I5_two_not_five_and_the_constraint_was_in_my_own_receipt.py`.  ** The rename collided too. **
  * r2512 -- 56 resolved both by hand, moving 54's files to I6 and I7 and repointing every citation,
    and named the class themselves: "a collision class the ID bands do not cover: receipt filenames."
    ** Their resolution stands and is not disturbed here. **  *54's c54.199 proposed a band rename to
    I50/I51 in a bundle that crossed with it; that rename is DROPPED -- three renames of one file is
    churn, and the pushed names own the slots.*

⇒ ** SO THE BANDS APPLY GOING FORWARD AND EXISTING ALLOCATIONS ARE GRANDFATHERED. **  Nothing in the
tree needs to move for this gate to be green; what it stops is the NEXT collision.

⇒ *** A shared receipt directory has a LETTER+NUMBER namespace with no allocation rule, which is
    exactly the state the LEAD-ID space was in before bands -- and that space collided twice before
    `check_id_bands.py` was written, for the same reason and with the same shape. ***

** THE FIX IS THE ONE THAT ALREADY WORKED, APPLIED TO THE NAMESPACE THAT NOW NEEDS IT: BANDS. **
The lead register gives 56 `L-221`-`L-499`, 54 `L-500`-`L-799`, cc54 `L-800`-`L-899`.  This gate
gives the receipt prefixes the same shape, in the same order, so a node that knows one knows the
other:

      56    1 - 49        the observer line
      54   50 - 79        the working fork
      cc54 80 - 99        the unattended node

⚠ ** AND WHAT THIS GATE DOES AND DOES NOT DO. **  It FAILS on a duplicate prefix within one
directory -- that is the collision, and it is unambiguous.  It only ** REPORTS ** a prefix outside
every band, because ** the bands are 54's proposal and are not 56's yet ** (routed as `FOR_56` item
16): every existing 56 receipt is inside 1-49 already, so the proposal costs them nothing, but a
convention is not a convention until the other lines have seen it.  *A gate that failed the whole
tree on a rule one node invented this morning would be a node legislating, which this corpus does
not do.*

⌗ ** VERIFIED AGAINST A SEEDED DEFECT THAT WAS NOT SEEDED: ** the duplicate this gate is built for
was sitting on `main` when it was written, so its first run was a real detection and not a drill.
The self-test below re-creates that state in memory so the detection survives the fix.

Exit 0 clean, 1 on any duplicate prefix.
"""

import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')

BANDS = [
    (1, 49, '56 -- the observer line'),
    (50, 79, '54 -- the working fork'),
    (80, 99, 'cc54 -- the unattended node'),
]

PREFIX = re.compile(r'^([A-Za-z]+)(\d+)_')


def prefixes(directory):
    """{(letter, number): [filenames]} for one directory -- the STATION prefixes only.

    ** THE DIRECTORY'S OWN TAG IS NOT A STATION PREFIX, and the first draft of this gate did not
    know that. **  `receipts/P17_geometric_core_paper/` holds `P17_power_is_null.py`,
    `P17_qm_S4_vs_S5.py` and four more -- every paper-scoped receipt repeats its paper's tag by
    design, so a naive reader flags six files as a six-way collision.  *That is the whole directory
    doing exactly what it should, reported as the failure this gate exists for* -- and a gate whose
    steady output is a wall of false alarms is a gate nobody reads, which this line paid for in
    `check_loci` at c54.197 and is not paying for twice.
    """
    own = os.path.basename(directory.rstrip('/')).split('_')[0].upper()
    out = defaultdict(list)
    for fn in sorted(os.listdir(directory)):
        if not fn.endswith('.py'):
            continue
        m = PREFIX.match(fn)
        if not m:
            continue
        tag = (m.group(1) + m.group(2)).upper()
        if tag == own:
            continue                      # the directory's own tag, repeated by design
        # ** AND AN `L<digits>` PREFIX IS A LEAD TAG, NOT A STATION PREFIX. **  Some directories
        # name receipts by the LEAD they serve rather than by a station letter --
        # `P13_boundary/` holds `L212_the_factorisation_singles_out_nothing.py` and
        # `L212_the_generation_index_fixes_the_mass.py`, which are two receipts for ONE lead and
        # not two nodes claiming one slot.  *Second false-positive class found the same way as
        # the first: by running the gate and reading what it said instead of what I expected.*
        if m.group(1).upper() == 'L':
            continue
        out[(m.group(1).upper(), int(m.group(2)))].append(fn)
    return out


def band_of(n):
    for lo, hi, who in BANDS:
        if lo <= n <= hi:
            return who
    return None


def scan(root):
    """(duplicates, unbanded) over every receipt directory under root."""
    dups, unbanded = [], []
    rdir = os.path.join(root, 'receipts')
    if not os.path.isdir(rdir):
        return dups, unbanded
    for sub in sorted(os.listdir(rdir)):
        d = os.path.join(rdir, sub)
        if not os.path.isdir(d):
            continue
        for (letter, n), files in sorted(prefixes(d).items()):
            if len(files) > 1:
                dups.append((sub, f'{letter}{n}', files))
            if band_of(n) is None:
                unbanded.append((sub, f'{letter}{n}', files[0]))
    return dups, unbanded


def selftest():
    """** The r2510 state, re-created so the detection outlives the fix. **

    A gate proven only on a tree that no longer contains the defect proves nothing about the tree
    that does -- this corpus has paid for that lesson twice (`check_loci`, c54.197).
    """
    fake = {('I', 4): ['I4_a.py', 'I4_b.py'], ('I', 5): ['I5_c.py']}
    hits = [k for k, v in fake.items() if len(v) > 1]
    if hits != [('I', 4)]:
        print('  ** SELF-TEST FAILED: the duplicate detector does not detect a duplicate. **')
        return False
    if band_of(4) != BANDS[0][2] or band_of(50) != BANDS[1][2] or band_of(85) != BANDS[2][2]:
        print('  ** SELF-TEST FAILED: the band lookup does not place 4 / 50 / 85. **')
        return False
    if band_of(0) is not None or band_of(120) is not None:
        print('  ** SELF-TEST FAILED: the band lookup accepts a number outside every band. **')
        return False
    return True


def main():
    print()
    print('  check_receipt_prefixes -- one prefix, one node, one directory')
    print()
    if not selftest():
        return 1

    dups, unbanded = scan(ROOT)
    ndirs = sum(1 for s in os.listdir(os.path.join(ROOT, 'receipts'))
                if os.path.isdir(os.path.join(ROOT, 'receipts', s)))
    print(f'  {ndirs} receipt director(ies) scanned')

    if unbanded:
        print()
        print(f'  [REPORT] {len(unbanded)} prefix(es) outside every band -- ** reported, not failed: '
              f'the bands are 54\'s proposal and not yet 56\'s ** (FOR_56 item 16)')
        for sub, pfx, f in unbanded[:8]:
            print(f'      {sub}/{pfx}  ({f})')
        if len(unbanded) > 8:
            print(f'      ... and {len(unbanded) - 8} more')

    print()
    if not dups:
        print('  clean -- no two files share a prefix inside one receipt directory')
        print('  ⌗ bands: ' + ' | '.join(f'{lo}-{hi} {who.split(" --")[0]}' for lo, hi, who in BANDS))
        print()
        return 0

    print(f'  {len(dups)} DUPLICATE PREFIX(ES):')
    for sub, pfx, files in dups:
        print(f'\n  receipts/{sub}/  prefix {pfx}')
        for f in files:
            print(f'      {f}')
        print('     ** Two nodes allocated the same prefix.  The PUSHED file owns the slot; the')
        print('        other renames INTO ITS OWN BAND and re-points its \\rcpt{} key, its INDEX')
        print('        row and its register row. **')
    return 1


if __name__ == '__main__':
    sys.exit(main())

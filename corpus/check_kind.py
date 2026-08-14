#!/usr/bin/env python3
"""check_kind.py -- A TURN MARKED `COMPUTED` MUST HAVE COMPUTED SOMETHING.

** WHY.  `THE_HANDOFF` (r2654) named this as the one failure no gate catches: ** *** "a 54 marking its own
turns will mark a reading as a computation, because from inside a turn they feel identical." ***  ⇒ ** And
r2656 ran the check by hand against this line's own log and found it twice. **

  * ** `r2635` ** -- marked `COMPUTED`; its receipt derives $\\{6,7,10\\}$ from $\\mathfrak{so}(5,1)$'s
    symmetric decompositions using a two-line `dim_so(n)` helper.  *** Arithmetic, and real -- but the
    turn's finding was that a CITATION was circular, which is a reading. ***
  * ** `r2637` and `r2649` ** -- marked `COMPUTED` with ** no receipt at all **.  r2637 reduced a matrix
    already on disk; r2649 fixed a script.  *** Both are instrument work wearing a computation's label. ***

** WHY IT MATTERS MORE THAN IT LOOKS. **  *** The `LATENT`/`COMPUTED` ratio is the SPLIT SIGNAL.  Marking a
reading as a computation moves the number in the direction that licenses splitting -- and r2649 found that
every instrument error this session ran the same way, LOW on what remains and HIGH on what has been done.
A node grading its own turns will drift the same way, and nothing else looks. ***

** WHAT THIS CHECKS. **  Every `LATENT_HISTORY` row marked `COMPUTED` must have a receipt written at that
revision which imports `numpy` or `sympy`, or calls one of them.  ** Not a proof that real work happened
-- a proof that SOMETHING was computed. **

  ⚠ ** It cannot catch the converse ** -- a genuine computation logged as `LATENT` -- *** and that is the
      safe direction, so it is left uncaught deliberately. ***
  ⌗ ** GRANDFATHERED: ** the three rows above are recorded here rather than rewritten, because *** the log
    is a record of what was believed at the time and editing it would destroy the only evidence that this
    drift happens. ***

⚠ ** A BLIND SPOT, NAMED r2667 AND DELIBERATELY NOT GATED r2668. **  This gate verifies that a `COMPUTED`
turn COMPUTED something.  *** It cannot verify the computation was NEEDED. ***  r2666 derived, correctly
and independently, a result P14 states directly -- and passed here, because the receipt does compute.

  ** r2668 tried to gate it and stopped. **  The tell tried was "the receipt quotes the paper stating its
  own conclusion", and it fires on five receipts of which the two inspected are ** legitimate **:
  `P03_locus_sweep` establishes identities P3 states only CONDITIONALLY, and
  `P14_no_choice_of_group_works` exposes a silent modelling assumption.

  ⇒ *** The distinguishing feature of a rediscovery is not what the receipt quotes but whether the
      SEARCH covered the section the conclusion lands in -- which is a fact about the reading, not about
      the artefact, and nothing on disk records it. ***
  ⌗ ** So this is a DISCIPLINE and not a gate, and it has a rule (r2667): ** *** before deriving, read
    forward from the sentence that raised the question. ***  Building a mechanism for it would repeat
    r2657's error -- a protocol around something a line in a file already handles.

    python3 corpus/check_kind.py

Written r2656.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

GRANDFATHERED = {'r2635', 'r2637', 'r2649'}
# ** r2751: the test did not know CAMB or scipy exist, so a receipt that runs a Boltzmann
# code five times read as computing nothing.  *** The gate was measuring which LIBRARY was
# imported, not whether anything was computed -- and numpy/sympy happened to be the two this
# corpus reached for first.  A whitelist of tools is a proxy for the property, and it goes
# stale the moment a receipt reaches for a tool nobody had used yet. ***
NUMERIC = re.compile(r'import numpy|import sympy|import camb|import scipy|from scipy'
                     r'|np\.\w|sp\.\w|camb\.\w|quad\(|solve_ivp\(|brentq\(')


def main():
    print()
    print('  check_kind -- did every COMPUTED turn compute something?')
    print()
    rows = [l.split(None, 2) for l in
            open(os.path.join(ROOT, 'LATENT_HISTORY.txt'), encoding='utf-8', errors='replace')
            if l.startswith('r')]

    seen, dupes = set(), []
    for r in rows:
        if r[0] in seen:
            dupes.append(r[0])
        seen.add(r[0])

    receipts = {f: open(f, encoding='utf-8', errors='replace').read()
                for f in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)}

    bad = []
    for r in rows:
        if len(r) < 2 or r[1] != 'COMPUTED' or r[0] in GRANDFATHERED:
            continue
        hits = [d for d in receipts.values() if re.search(rf'(Written|built) {r[0]}\b', d)]
        if not hits:
            bad.append((r[0], 'no receipt at that revision'))
        elif not any(NUMERIC.search(d) for d in hits):
            bad.append((r[0], 'receipt computes nothing'))

    if dupes:
        print(f'    [FAIL] LATENT_HISTORY has duplicate revision row(s): {sorted(set(dupes))}')
        print('    ⛔ ** A duplicated row double-counts its kind and skews the split signal. **')
        return 1
    if bad:
        for rev, why in bad:
            print(f'    [FAIL] {rev} marked COMPUTED -- {why}')
        print()
        print('    ⛔ ** A TURN MARKED `COMPUTED` MUST HAVE COMPUTED SOMETHING. **  *** From inside a turn')
        print('       a reading and a computation feel identical, and the ratio they feed is the split')
        print('       signal.  Re-mark the turn, or write the receipt. ***')
        return 1
    n = sum(1 for r in rows if len(r) > 1 and r[1] == 'COMPUTED')
    print(f'  {n} COMPUTED turns, {len(GRANDFATHERED)} grandfathered, the rest carry a computing receipt.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

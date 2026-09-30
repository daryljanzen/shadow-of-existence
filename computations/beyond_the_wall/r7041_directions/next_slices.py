"""The slices a configuration still needs, at a width chosen for THIS configuration's cost.

** WHY A HELPER AND NOT A LOOP IN THE LAUNCHER. **  The launcher used to compute its slice list as
`range(0, n, 250)` in bash, which is a second definition of the tiling living beside `fold.py`'s.  *Two
definitions of "which slices does this configuration need" is the copied-snippet defect the fold module
exists to prevent* -- so the launcher asks, and the answer comes from `fold.py`'s own range reading.

⛭ ** THE WIDTH IS PER CONFIGURATION, AND IT IS READ FROM THE GRID RATHER THAN DERIVED FROM THE KNOBS. **
A slice of width `W` costs about `W x (eta points)`, because the k-slice bounds the modes and every mode is
integrated over the whole visibility.  So a configuration with four times the eta points needs a quarter the
width to cost the same wall time.  *`GRIDSAVE` measured `nlos` for all 24 configurations, so this reads it;
re-deriving it from `NLOS`/`NLOSW`/`NLOSF` would be a claim about the instrument instead of a reading of it.*

⛔ ** AND THE REASON IT IS WORTH DOING AT ALL IS MEASURED. **  `nlos2240` slices at width 250 took 237, 271,
298 and 405 s.  When this container's restarts tightened to a few minutes, a unit of work that long stopped
completing at all -- ONE slice landed in twenty-six minutes, which over the 498 still to run is about 216
hours.  *A killed slice loses all of its work, so the unit has to fit inside the window.*
"""
import os
import sys

import numpy as np

import fold

# ⛭ THE WIDTH POLICY MOVED INTO `fold` this revision, so the launcher and the count read ONE definition
#   instead of two that can drift.  ** MEASURED, and why it narrowed from 250 to 100: the container is
#   reclaimed shortly after this seat goes idle, and a slice that does not finish inside that window is
#   killed and redone from nothing. **  Between 14:48 and 15:14, with this seat working continuously, 14
#   slices landed; in the 16 quiet minutes after, 2 did.  With `SRCINJ` injected the solver is SKIPPED, so a
#   slice costs the projection integral alone -- linear in (modes) x (reported l count) over a few seconds of
#   setup -- so narrowing it shortens it very nearly proportionally.
#   ⛔ And the equal-cost claim was only half true: it divided by `nlos` alone, but `LSTEP=4` reports 475
#   multipoles where the base 8 reports 238, so an `lstep4` slice cost twice what the same width cost
#   elsewhere.  That is corrected in `fold.width_for`.
#   ⌷ Nothing banked is discarded: `fold` reads each slice's OWN declared `__SLICE__ lo:hi` and `covered_to`
#   walks abutting ranges, so narrow slices abut the wide ones already there and the tiling gate still
#   verifies the union.
width_for = fold.width_for


def main():
    # ⌗ `--width ARM TAG` answers phase 1, which opens a configuration BEFORE its mode count is known.
    # *The width depends only on the eta count, which `GRIDSAVE` already measured, so phase 1 can open at
    # the cheap width instead of paying one 250-wide slice per expensive configuration just to read a
    # header.*
    if sys.argv[1] == '--width':
        print(width_for(sys.argv[2], sys.argv[3]))
        return 0
    outdir, tag, arm, cfgtag = sys.argv[1:5]
    n = fold.modes_from_log(os.path.join(outdir, f'{tag}_k0.log'))
    if n is None:
        return 1                                   # slice 0 never reported: the launcher warns, not here
    w = width_for(arm, cfgtag)
    lo = fold.covered_to(outdir, tag)
    while lo < n:
        print(f'{lo}:{lo + w}')
        lo += w
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

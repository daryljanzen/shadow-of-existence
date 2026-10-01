#!/usr/bin/env python3
"""r7093 -- the contrast coefficient c on a NAMED grid, through `70`'s own instrument and not a new one.

** WHY A DRIVER AND NOT A COPY. **  `r7093` names the number the one-clock rebuild has to move: the
coefficient c on the contrast template once the five declared directions are fitted -- `70` measured
c = -0.0636 +- 0.0085 on the arm against -0.0075 +- 0.0083 on the control, i.e. *the data ask THIS arm's
acoustic contrast to be 6.4 +- 0.9 per cent lower and ask the control for nothing.*
  ⇒ ** The definition must stay `70`'s. **  So this imports `r7091_70_fit_rigidity/rigidity.py` and
  `contrast_size.py`'s own least-squares, and changes exactly ONE thing: the directory the grid is read
  from.  *Re-deriving the template here would make a disagreement unattributable -- it could be the
  geometry or it could be my arithmetic, and the whole point is to tell those apart.*

⛔ ** AND IT PROVES ITSELF ON THE BANKED GRID FIRST. **  Run with no argument it reads
`refit_grid185/` and must reproduce `70`'s published c to the digits they published.  *A tool that
cannot reproduce the number it is about to move is not evidence that the number moved.*

⌗ Usage:  python3 contrast_on.py [GRID_DIR ...]      (default: the banked refit_grid185)
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SEV = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7091_70_fit_rigidity')
PUBLISHED = {'cr': (-0.0636, 0.0085), 'lcdm': (-0.0075, 0.0083)}      # 70's, at r7093


def c_on(grid):
    """(c, sigma) per arm, with `70`'s build and `contrast_size`'s own design matrix"""
    import io
    import contextlib
    sys.path.insert(0, SEV)
    for m in ('rigidity',):
        sys.modules.pop(m, None)
    argv = sys.argv
    sys.argv = [argv[0], '--mc', '1']            # the Monte Carlo is not used here; keep it to one draw
    with contextlib.redirect_stdout(io.StringIO()):
        import rigidity as R
    sys.argv = argv
    R.GRID = grid                                # ⇐ THE ONE CHANGE
    out = {}
    for arm in ('lcdm', 'cr'):
        B = R.build(arm)
        cols = [B['m0'] * 0.02] + [B['g'][k] * R.STEP[k] for k in R.STEP] + [B['contrast']]
        Jw = np.column_stack([R.W(B, c) for c in cols])
        y = R.W(B, B['d'] - B['m0'])
        x, *_ = np.linalg.lstsq(Jw, y, rcond=None)
        err = np.sqrt(np.diag(np.linalg.inv(Jw.T @ Jw)))
        # the configuration the bank itself records, where it records one -- r7093 asked for this
        z = np.load(os.path.join(grid, f'{arm}_base.npz'))
        sw = str(z['switches']) if 'switches' in z.files else '(the bank records no configuration)'
        out[arm] = (float(x[-1]), float(err[-1]), sw)
    return out


# ⛔ ** FIXED AT `cc66.77`: THE SELF-PROOF WAS BOUND TO "THE FIRST GRID IN THE LIST" RATHER THAN TO
# ** THE BANK, so naming a rebuilt grid made the rebuilt grid the thing that had to reproduce `70`'s
# ** published c -- and a rebuilt grid disagreeing with it is the measurement, not a driver fault. **
# *The driver refused to read `grid_licensed` for exactly the reason it exists to report.  The bank is
# now PREPENDED unconditionally: the proof always runs where it means something, and every named grid
# gets its `WHAT MOVED` baseline for free instead of depending on argument order.*
BANK = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid185')


def main(argv):
    grids = [BANK] + [g for g in argv if os.path.abspath(g.rstrip('/')) != os.path.abspath(BANK)]
    print(__doc__.split('⌗ Usage')[0])
    print('=' * 100)
    first = None
    for g in grids:
        r = c_on(g)
        print(f"  {os.path.basename(g.rstrip('/'))}")
        for arm in ('lcdm', 'cr'):
            c, s, sw = r[arm]
            line = f"    {arm:5s}  c = {c:+.4f} +- {s:.4f}  ({c/s:+.1f} sigma)"
            if arm in PUBLISHED and first is None:
                pc, ps = PUBLISHED[arm]
                agree = abs(c - pc) < 5e-4 and abs(s - ps) < 5e-4
                line += f"   vs 70's published {pc:+.4f} +- {ps:.4f}  {'REPRODUCED' if agree else '⛔ DISAGREES'}"
            print(line)
            if sw:
                print(f"           configuration recorded in the bank: {sw[:110]}")
        if first is None:
            first = r
            # ⛔ the self-proof: refuse to go on if 70's own number is not reproduced ON THE BANK --
            #    which is now always the first grid read, by construction above
            for arm, (pc, ps) in PUBLISHED.items():
                c, s, _ = r[arm]
                assert abs(c - pc) < 5e-4, (f"{arm}: c = {c:+.6f} does not reproduce 70's {pc:+.4f} -- "
                                            f"fix the driver before reading any rebuilt grid")
            print("  ⇒ 70's published coefficients are REPRODUCED on the banked grid, both arms.")
        else:
            print("  WHAT MOVED, against the banked grid:")
            for arm in ('lcdm', 'cr'):
                c0, s0, _ = first[arm]
                c1, s1, _ = r[arm]
                d = c1 - c0
                print(f"    {arm:5s}  c {c0:+.4f} -> {c1:+.4f}   change {d:+.4f} "
                      f"({d/s0:+.1f} of the banked sigma)   |c| {'FELL' if abs(c1) < abs(c0) else 'ROSE'}"
                      f" by {100*abs(abs(c1)-abs(c0))/abs(c0):.0f}%")
            print("  ⌗ r7093: the data ask the arm's contrast to be 6.4 +- 0.9 per cent LOWER, so a")
            print("    rebuild that works drives the arm's |c| toward the control's, and one that does")
            print("    not is a real negative result reported the same way.")


if __name__ == '__main__':
    main(sys.argv[1:])

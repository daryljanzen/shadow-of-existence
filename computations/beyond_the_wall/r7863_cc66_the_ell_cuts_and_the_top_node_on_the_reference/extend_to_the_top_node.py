"""r7863+cc66 item ②: EXTEND THE LIKE-FOR-LIKE PROFILE TO 0.60 eV AND ASK WHETHER IT IS ONE BRANCH.

Order r7863 (69) item ②, and 60's own item ④ asks the same question of this seat.  60's profile on
this reference jumps to a second branch at Sum = 0.60 eV, H0 65.74 against 69.17 at the node below.
Bands registered at `r7863+cc66.1` BEFORE this file existed.

** THE HARNESS IS r7853's AND IS IMPORTED, NOT COPIED. **  `profile_likeforlike.py` is imported as a
module and its `profile`, `score`, `X0` and `BOX` are used as they stand, so this extension cannot
drift from the arm of record.  The only thing added is four more sums and a cold-start control.

** WARM STARTS, AND THE CHECK THAT THEY DID NOT DECIDE THE ANSWER. **  Each sum starts from the
previous sum's solution, beginning at the BANKED 0.40 eV point of each arm -- which is what makes a
basin jump invisible if the warm path simply follows the basin it is in.  So every extended point is
ALSO run COLD from the control start, and the two are compared: a cold start that lands LOWER is a
warm path stuck in the basin it came from, and that is the second branch rather than evidence
against one.  ⌗ *This is the one way a one-branch answer could be an artefact of the method, so the
cold leg is not a spot check here -- it is run at every extended point.*

** IDEMPOTENT: one JSON per (mode, leg, sum) under out/, an existing file skipped. **

Run: python3 -I extend_to_the_top_node.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(HERE)
R7853 = os.path.join(_BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference')
assert os.path.isdir(R7853), R7853          # r7861: three dirnames, asserted, not counted
sys.path.insert(0, R7853)
import profile_likeforlike as PL                                             # noqa: E402

NEW_SUMS = [0.45, 0.50, 0.55, 0.60]
OUT = os.path.join(HERE, 'out')
BANKED = os.path.join(R7853, 'out5')


def banked(mode, s):
    p = os.path.join(BANKED, '%s_%.3f.json' % (mode, s))
    return json.load(open(p)) if os.path.exists(p) else None


def start_of(d):
    return (d['H0'], d['Om'], d['ombh2'], d['ns'], d['tau'])


def run(mode, leg, s, start):
    path = os.path.join(OUT, '%s_%s_%.3f.json' % (mode, leg, s))
    if os.path.exists(path):
        d = json.load(open(path))
        print('  skip (already done): %s' % os.path.basename(path), flush=True)
        return d
    det = PL.profile(s, mode, start)
    det['leg'] = leg
    det['interior'] = all(lo + 1e-9 < v < hi - 1e-9 for v, (lo, hi)
                          in zip((det['H0'], det['Om'], det['ombh2'], det['ns'], det['tau']),
                                 PL.BOX))
    json.dump(det, open(path, 'w'), indent=1)
    print('  %-8s %-4s Sum=%.3f: total %10.3f  H0 %7.3f  Om %.4f  wb %.5f  ns %.4f  tau %.4f  '
          'rd %7.3f  interior %s  nfev %d'
          % (mode, leg, s, det['total'], det['H0'], det['Om'], det['ombh2'], det['ns'],
             det['tau'], det['rd_used'], det['interior'], det['nfev']), flush=True)
    return det


def main():
    os.makedirs(OUT, exist_ok=True)
    for mode in PL.MODES:
        anchor = banked(mode, 0.40)
        if anchor is None:
            print('  ⛔ no banked 0.40 point for %s -- cannot warm-start' % mode)
            return 1
        warm = start_of(anchor)
        for s in NEW_SUMS:
            warm = start_of(run(mode, 'warm', s, warm))
        for s in NEW_SUMS:
            run(mode, 'cold', s, PL.X0)
    print('\n  done: %d files under %s' % (len(os.listdir(OUT)), OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())

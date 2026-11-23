"""r7863+cc66 item ①: RE-SCORE BOTH ARMS WITH 60's TWO ELL CUTS AND THEIR INFORMATION-LOSS CONTROL.

Order r7863 (69) item ①.  60 measured, on their own pipeline, that thirty-six bandpowers removed
from the top of the spectrum cost 0.28 meV and the same thirty-six from the bottom cost 46.53.  This
runs the same two cuts through THIS seat's like-for-like reference so the tail's share becomes a
difference of two pipelines rather than one number from one.  Bands registered at `r7863+cc66.1`
BEFORE this file existed.

** THE ARM OF RECORD IS NOT REIMPLEMENTED, IT IS PATCHED AT ONE FUNCTION. **  `profile_likeforlike`
and `score_ttteee` are both 60's and this seat's committed modules and NEITHER IS EDITED.  Instead
`SC.chi2_of` is replaced, for the duration of a run, by a wrapper that applies the ell mask and then
does exactly what the original does -- restrict the COVARIANCE to the kept bins and re-invert it
(choice 1), fit ONE amplitude in closed form (choice 2), interpolate before binning (choice 3, which
happens upstream in `bin_three` and is untouched).  ⇒ So the cut profiles run through the SAME
minimiser, the same CAMB build and the same BAO and lensing terms as the landed limits, and the one
difference is the mask.

** AND THE PATCH IS VERIFIED BEFORE IT IS TRUSTED. **  With `cut = None` the wrapper must reproduce
`r7853`'s banked totals; the driver checks that at every banked sum of both arms and REFUSES to run
the cut legs if any total moves by more than 1e-6.  A patch that silently changed the uncut answer
would make every number below meaningless.

** THE CUT IS A CHOICE AND IS SPELLED OUT. **  A bin is ABOVE the cut when its LOW edge is, so a bin
straddling the cut is KEPT.  The count removed is taken from the bins the model COVERS, not from all
613, and the low-end control removes the SAME NUMBER of covered bins from the bottom.  ⌗ *That count
is not 60's thirty-six and is not meant to be: their covered set and bin convention are their own.*

** IDEMPOTENT: one JSON per (mode, cut, sum) under cuts/, an existing file skipped.  Each leg stops
one point past the 2.71 crossing, because a limit needs the crossing bracketed and nothing beyond. **

Run: python3 -I cut_rescore.py
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(HERE)
R7853 = os.path.join(_BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference')
assert os.path.isdir(R7853), R7853          # r7861: three dirnames, asserted, not counted
sys.path.insert(0, R7853)
import profile_likeforlike as PL                                             # noqa: E402
import score_ttteee as SC                                                    # noqa: E402

_ORIG = SC.chi2_of
SUMS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
#: (label, ell cut, which end the bins come off)
LEGS = [('top1800', 1800, 'top'), ('bot1800', 1800, 'bot'),
        ('top1500', 1500, 'top'), ('bot1500', 1500, 'bot')]
OUT = os.path.join(HERE, 'cuts')
BANKED = os.path.join(R7853, 'out5')
CROSS = 2.71
_REMOVED = {}


def _masked(cut, side):
    """the replacement for SC.chi2_of: the original's three choices, with an ell mask added"""
    def chi2_of(ls, Dtt, Dte, Dee, amplitude=None, blocks=(0, 1, 2)):
        mb = SC.bin_three(ls, Dtt, Dte, Dee)
        covered = np.isfinite(mb) & np.isin(SC.BLOCK, list(blocks))
        above = covered & (SC.BIN_LO > cut)
        n_cut = int(above.sum())
        if side == 'top':
            drop = above
        else:
            idx = np.where(covered)[0]
            order = idx[np.argsort(SC.BIN_LO[idx], kind='stable')][:n_cut]
            drop = np.zeros_like(covered)
            drop[order] = True
        keep = covered & ~drop
        _REMOVED[(cut, side)] = (n_cut, int(covered.sum()), int(keep.sum()))
        if keep.sum() < 10:
            raise ValueError('only %d bins left -- too short to score' % keep.sum())
        F = SC.fisher_for(keep)
        m, d = mb[keep], SC.X_DATA[keep]
        A = float((m @ F @ d) / (m @ F @ m)) if amplitude is None else float(amplitude)
        r = d - A * m
        n = {b: int(((SC.BLOCK == b) & keep).sum()) for b in (0, 1, 2)}
        return float(r @ F @ r), int(keep.sum()), A, n
    return chi2_of


def _identity():
    """cut = None: the mask keeps everything, so this MUST reproduce the banked totals"""
    def chi2_of(ls, Dtt, Dte, Dee, amplitude=None, blocks=(0, 1, 2)):
        return _ORIG(ls, Dtt, Dte, Dee, amplitude=amplitude, blocks=blocks)
    return chi2_of


def banked(mode, s):
    p = os.path.join(BANKED, '%s_%.3f.json' % (mode, s))
    return json.load(open(p)) if os.path.exists(p) else None


def start_of(d):
    return (d['H0'], d['Om'], d['ombh2'], d['ns'], d['tau'])


def verify_patch():
    """the uncut wrapper against every banked point of both arms, before any cut leg runs"""
    SC.chi2_of = _identity()
    worst = 0.0
    for mode in PL.MODES:
        for s in PL.SUMS:
            d = banked(mode, s)
            if d is None:
                continue
            tot, _ = PL.score(s, *start_of(d), mode)
            worst = max(worst, abs(tot - d['total']))
    SC.chi2_of = _ORIG
    print('  patch verification: worst |total - banked| = %.3e over the banked grid' % worst,
          flush=True)
    return worst


def main():
    os.makedirs(OUT, exist_ok=True)
    worst = verify_patch()
    json.dump(dict(worst_uncut_departure=worst), open(os.path.join(HERE, 'patch_check.json'), 'w'),
              indent=1)
    if worst > 1e-6:
        print('  ⛔ REFUSING to run the cut legs: the uncut wrapper does not reproduce the banked '
              'totals (worst %.3e).  Every cut number would be meaningless.' % worst)
        return 1
    for label, cut, side in LEGS:
        for mode in PL.MODES:
            SC.chi2_of = _masked(cut, side)
            base = None
            warm = start_of(banked(mode, 0.0))
            for s in SUMS:
                path = os.path.join(OUT, '%s_%s_%.3f.json' % (mode, label, s))
                if os.path.exists(path):
                    det = json.load(open(path))
                    print('  skip (already done): %s' % os.path.basename(path), flush=True)
                else:
                    b = banked(mode, s)
                    det = PL.profile(s, mode, start_of(b) if b else warm)
                    det['leg'], det['ell_cut'], det['side'] = label, cut, side
                    det['removed'] = _REMOVED.get((cut, side))
                    det['interior'] = all(lo + 1e-9 < v < hi - 1e-9 for v, (lo, hi)
                                          in zip((det['H0'], det['Om'], det['ombh2'],
                                                  det['ns'], det['tau']), PL.BOX))
                    json.dump(det, open(path, 'w'), indent=1)
                    print('  %-8s %-8s Sum=%.3f: total %10.3f  removed %s  H0 %7.3f  Om %.4f  '
                          'rd %7.3f  interior %s  nfev %d'
                          % (mode, label, s, det['total'], det['removed'], det['H0'], det['Om'],
                             det['rd_used'], det['interior'], det['nfev']), flush=True)
                warm = start_of(det)
                base = det['total'] if base is None else base
                if det['total'] - base > CROSS:
                    print('    crossing bracketed at Sum=%.3f (dchi2 %.3f) -- leg stops here'
                          % (s, det['total'] - base), flush=True)
                    break
            SC.chi2_of = _ORIG
    print('\n  done: %d files under %s' % (len(os.listdir(OUT)), OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())

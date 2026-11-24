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

** AND THE PATCH IS VERIFIED BEFORE IT IS TRUSTED -- ON THE TERM THE MASK CAN TOUCH, WHICH IS NOT
THE TOTAL. **  The first cut of this check compared the TOTAL against `r7853`'s banked value and
REFUSED, at a worst departure of 6.185e-03.  The wrapper could not be the cause -- at `cut = None` it
calls the original with the same arguments and returns its result unchanged -- so the check was
measuring something else, and `reproduce_the_banked_score.py` found what: the departure is confined
ENTIRELY to `chi2_bao` on the `rd_min` arm, `rd_camb` reproducing bit-exactly on every term at every
sum.  `bao_min`'s memo is keyed on ROUNDED parameters (`round(h0, 4)`, `round(om, 5)`), so a fresh
process computes `r_d` at the recorded parameters where the banked run was served the first trial
point that rounded to the same key -- 1.026e-03 Mpc at worst.  `rd_camb` never calls it.

⇒ ** SO THE GUARD IS NOW ON `chi2_cmb`, WHICH IS THE ONLY TERM AN ELL MASK CAN CHANGE AT ALL. **  The
lensing, tau and BAO terms do not see the mask, so putting them inside the tolerance made the check
LOOSER where it matters and impossible to pass where it does not.  The driver now refuses unless
`chi2_cmb` reproduces EXACTLY on both arms and the whole total reproduces EXACTLY on `rd_camb`, with
the `rd_min` residue required to be `chi2_bao`-only and under a bound this measurement justifies.
⌗ *That is the check tightened where it bites, not loosened to let the run proceed.*

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


#: the residue `bao_min`'s rounded memo leaves on the minimised arm, measured at
#: `reproduce_the_banked_score.json` -- 6.185e-03 worst, so this bound is that figure doubled
BAO_MEMO_BOUND = 1.3e-2


def verify_patch():
    """the uncut wrapper against every banked point, on the term the mask can actually change

    Returns a dict of the three quantities the refusal is decided on, so the receipt pins what was
    checked rather than a single number that hides which term moved.
    """
    SC.chi2_of = _identity()
    out = dict(worst_cmb_either_arm=0.0, worst_total_rd_camb=0.0, worst_total_rd_min=0.0,
               worst_non_bao_rd_min=0.0, points=0)
    for mode in PL.MODES:
        for s in PL.SUMS:
            d = banked(mode, s)
            if d is None:
                continue
            tot, det = PL.score(s, *start_of(d), mode)
            out['points'] += 1
            out['worst_cmb_either_arm'] = max(out['worst_cmb_either_arm'],
                                              abs(det['chi2_cmb'] - d['chi2_cmb']))
            out['worst_total_%s' % mode] = max(out['worst_total_%s' % mode],
                                               abs(tot - d['total']))
            if mode == 'rd_min':
                non_bao = sum(abs(det[k] - d[k]) for k in ('chi2_cmb', 'chi2_lens', 'chi2_tau'))
                out['worst_non_bao_rd_min'] = max(out['worst_non_bao_rd_min'], non_bao)
    SC.chi2_of = _ORIG
    out['ok'] = (out['worst_cmb_either_arm'] == 0.0 and out['worst_total_rd_camb'] == 0.0
                 and out['worst_non_bao_rd_min'] == 0.0
                 and out['worst_total_rd_min'] < BAO_MEMO_BOUND)
    print('  patch verification over %d banked points:' % out['points'])
    print('    chi2_cmb, either arm         %.3e   (must be EXACTLY 0 -- the mask touches this)'
          % out['worst_cmb_either_arm'])
    print('    total, rd_camb               %.3e   (must be EXACTLY 0)'
          % out['worst_total_rd_camb'])
    print('    non-bao terms, rd_min        %.3e   (must be EXACTLY 0)'
          % out['worst_non_bao_rd_min'])
    print('    total, rd_min                %.3e   (bao-memo residue, bound %.1e)'
          % (out['worst_total_rd_min'], BAO_MEMO_BOUND), flush=True)
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    chk = verify_patch()
    json.dump(chk, open(os.path.join(HERE, 'patch_check.json'), 'w'), indent=1)
    if not chk['ok']:
        print('  ⛔ REFUSING to run the cut legs: the uncut wrapper does not reproduce the banked '
              'score on a term the mask can change.  Every cut number would be meaningless.')
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

# -*- coding: utf-8 -*-
"""r7903+cc66 item ⑲①: THE REFERENCE RE-SCORED ON THE INSTRUMENT'S OWN 555-BIN MASK.

Order `r7903` (69) item ⑲①.  Bands registered in `PREDICTION.md` at `b7ade4b6d`, pushed BEFORE this
file existed.

** THE ORDER'S PREMISE IS OFF BY SIXTEEN BINS, AND THIS FILE RUNS BOTH READINGS. **  ⑲① says to set
the model to `NaN` below `ℓ = 100` "so that `score_ttteee` keeps exactly the instrument's 555 bins".
Measured on `SC.BIN_LO`/`BIN_HI`/`BLOCK`, that keeps **571**: `BIN_LO < 100` removes 42 (14 from each
block) and the remaining 16 of the 58 are `BIN_HI > 1996`, every one `TT`, because `TT` runs to
`BIN_LO 2476` while `TE` and `EE` stop at `1980`.  ⇒ The instrument's mask is `ℓ ≥ 100` AND
`ℓ ≤ 1996`, which keeps **185 from each block**.  This file runs the `555` mask as the answer and the
literal `571` beside it, so the difference is visible rather than resolved silently.

** NEITHER `profile_likeforlike` NOR `score_ttteee` IS EDITED. **  `SC.chi2_of` is replaced for the
duration of a leg by a wrapper that applies the mask and then calls the original's own three choices,
exactly as `r7863` did it.  ⌗ *And `r7863`'s stopping rule is NOT copied: it breaks on
`total - base` with `base` the FIRST point, which is the lowest-sum convention `r7903` has now ruled
against.  This scans the whole grid and reads the crossing from the profile MINIMUM.*

** TWO CONTROLS, BOTH REFUSING. **  ⒜ the uncut wrapper must reproduce every banked `chi2_cmb`
EXACTLY -- `r7863`'s own control, carried forward, and the run refuses the legs if it fails, because
a mask number scored against a different likelihood is meaningless.  ⒝ the `555` mask must keep
exactly `555` bins at `185/185/185`, asserted before a limit is read.

    python3 <this file>            # idempotent: one JSON per (mask, mode, sum), existing skipped
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
R7853 = [d for d in os.listdir(BW) if d.startswith('r7853_cc66_')][0]
R7863 = [d for d in os.listdir(BW) if d.startswith('r7863_cc66_')][0]
sys.path.insert(0, os.path.join(BW, R7853))

import profile_likeforlike as PL                                             # noqa: E402
import score_ttteee as SC                                                    # noqa: E402

_ORIG = SC.chi2_of
OUT = os.path.join(HERE, 'mask_out')
#: ⒜'s control bank: r7863's 16 cold/warm points, the ones its own patch check used
CTRL = os.path.join(BW, R7863, 'out')
#: the PROFILE GRID this seat's own 613-bin reading was read on -- r7853's out5, both modes at
#  eight sums.  ** The masked limit is read on the SAME grid as the unmasked one, so the move is a
#  difference of two readings of one sampling and not a difference of two samplings. **
GRID = os.path.join(BW, R7853, 'out5')

SUMS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
CROSS = 2.71

#: ⑲①'s two readings.  LOW is the order's literal words; INSTR is what it intends.
#: ⒞ `top597` exists ONLY to score the additivity claim registered at Ⓐ②: with low-only and
#   full measured, the top part alone is the third leg the claim needs.  A registered claim with no
#   leg that can score it is not registered, it is decorative.
MASKS = {'instr555': dict(lo=100, hi=1996),
         'low571': dict(lo=100, hi=None),
         'top597': dict(lo=-1, hi=1996)}

_KEPT = {}


def _masked(lo, hi):
    """SC.chi2_of with an ell mask, built from the module's OWN bin edges"""
    def chi2_of(ls, Dtt, Dte, Dee, amplitude=None, blocks=(0, 1, 2)):
        mb = SC.bin_three(ls, Dtt, Dte, Dee)
        covered = np.isfinite(mb) & np.isin(SC.BLOCK, list(blocks))
        keep = covered & (SC.BIN_LO >= lo)
        if hi is not None:
            keep = keep & (SC.BIN_HI <= hi)
        _KEPT[(lo, hi)] = (int(keep.sum()),
                           {b: int(((SC.BLOCK == b) & keep).sum()) for b in (0, 1, 2)})
        if keep.sum() < 10:
            raise ValueError('only %d bins left' % keep.sum())
        F = SC.fisher_for(keep)
        m, d = mb[keep], SC.X_DATA[keep]
        A = float((m @ F @ d) / (m @ F @ m)) if amplitude is None else float(amplitude)
        r = d - A * m
        return float(r @ F @ r), int(keep.sum()), A, None
    return chi2_of


def _uncut():
    """the mask that keeps everything -- this MUST reproduce the banked chi2_cmb exactly"""
    return _masked(-1, None)


def banked(mode, sum_ev):
    """this seat's own 613-bin profile point at (mode, sum), from r7853's out5"""
    p = os.path.join(GRID, '%s_%.3f.json' % (mode, sum_ev))
    return json.load(open(p)) if os.path.exists(p) else None


def ctrl_points():
    """r7863's 16 cold/warm points -- the bank ⒜ checks the uncut wrapper against"""
    out = []
    for f in sorted(os.listdir(CTRL)):
        if f.endswith('.json') and ('_cold_' in f or '_warm_' in f):
            out.append(json.load(open(os.path.join(CTRL, f))))
    return out


def unmasked_limit(mode):
    """the 613-bin limit on THIS grid, read with the same profile-minimum convention"""
    pts = []
    for s in SUMS:
        b = banked(mode, s)
        if b:
            pts.append((s, b['total']))
    lim, at = limit95_from_min(pts) if len(pts) >= 3 else (None, None)
    return lim, at, pts


def start_of(d):
    return [d['H0'], d['Om'], d['ombh2'], d['ns'], d['tau']]


def patch_check():
    """⒜ the uncut control, over every banked point this seat has"""
    SC.chi2_of = _uncut()
    worst, n = 0.0, 0
    try:
        for b in ctrl_points():
            det = PL.score(b['sum'], b['H0'], b['Om'], b['ombh2'], b['ns'], b['tau'], b['mode'])[1]
            if not det:
                continue
            worst = max(worst, abs(det['chi2_cmb'] - b['chi2_cmb']))
            n += 1
    finally:
        SC.chi2_of = _ORIG
    return worst, n


def limit95_from_min(points):
    """the crossing of 2.71 above the profile MINIMUM -- r7903's ruled convention, in meV"""
    pts = sorted(points)
    s = np.array([p[0] for p in pts], float)
    t = np.array([p[1] for p in pts], float)
    d = t - t.min()
    if d.max() <= CROSS:
        return None, float(s[int(np.argmin(t))])
    fine = np.linspace(s[0], s[-1], 200001)
    i = np.where(np.interp(fine, s, d) > CROSS)[0]
    return (float(fine[i[0]] * 1000.0) if len(i) else None), float(s[int(np.argmin(t))])


def main():
    os.makedirs(OUT, exist_ok=True)
    print('=' * 100)
    print('  ⑲① THE REFERENCE ON THE INSTRUMENT\'S OWN MASK')
    print('=' * 100)

    worst, n = patch_check()
    print('  ⒜ uncut control over %d banked point(s): worst |Δchi2_cmb| = %.3e  (must be EXACTLY 0)'
          % (n, worst))
    if not (n > 0 and worst == 0.0):
        print('  ⛔ REFUSING the mask legs: the uncut wrapper does not reproduce the banked '
              'chi2_cmb. Every masked number would be scored against a different likelihood.')
        return 1

    counts = {}
    for name, m in MASKS.items():
        SC.chi2_of = _masked(m['lo'], m['hi'])
        b0 = banked('rd_camb', 0.0)
        PL.score(0.0, b0['H0'], b0['Om'], b0['ombh2'], b0['ns'], b0['tau'], 'rd_camb')
        SC.chi2_of = _ORIG
        counts[name] = _KEPT[(m['lo'], m['hi'])]
        print('  ⒝ mask %-9s keeps %d bins  %s' % (name, counts[name][0], counts[name][1]))
    if counts['instr555'][0] != 555 or sorted(counts['instr555'][1].values()) != [185, 185, 185]:
        print('  ⛔ REFUSING: the instrument mask does not keep 555 at 185/185/185.')
        return 1
    print('  ⇒ and the ORDER\'S LITERAL reading keeps %d, not 555 -- the sixteen-bin gap is the '
          'top cut.' % counts['low571'][0])
    print()

    res = {'masks': {k: dict(lo=v['lo'], hi=v['hi'], kept=counts[k][0],
                            per_block=counts[k][1]) for k, v in MASKS.items()},
           'uncut_control_worst': worst, 'uncut_control_points': n,
           'cross': CROSS, 'sums': SUMS, 'baseline': 'profile minimum over Sigma >= 0 (r7903 ruling)',
           'legs': {}}

    for name, m in MASKS.items():
        for mode in PL.MODES:
            SC.chi2_of = _masked(m['lo'], m['hi'])
            warm = start_of(banked(mode, 0.0))
            pts = []
            try:
                for s in SUMS:
                    path = os.path.join(OUT, '%s_%s_%.3f.json' % (name, mode, s))
                    if os.path.exists(path):
                        det = json.load(open(path))
                        print('  skip %s' % os.path.basename(path), flush=True)
                    else:
                        b = banked(mode, s)
                        det = PL.profile(s, mode, start_of(b) if b else warm)
                        det['mask'], det['kept'] = name, counts[name][0]
                        det['interior'] = all(lo + 1e-9 < v < hi - 1e-9 for v, (lo, hi)
                                              in zip((det['H0'], det['Om'], det['ombh2'],
                                                      det['ns'], det['tau']), PL.BOX))
                        json.dump(det, open(path, 'w'), indent=1)
                        print('  %-9s %-8s Sum=%.3f  total %10.3f  H0 %7.3f  Om %.4f  '
                              'interior %s  nfev %d'
                              % (name, mode, s, det['total'], det['H0'], det['Om'],
                                 det['interior'], det['nfev']), flush=True)
                    warm = start_of(det)
                    pts.append((s, det['total']))
                    d = [p[1] for p in pts]
                    if len(pts) >= 3 and (max(d) - min(d)) > CROSS and d[-1] == max(d):
                        print('    crossing bracketed above the MINIMUM at Sum=%.3f '
                              '(dchi2 %.3f) -- leg stops here' % (s, max(d) - min(d)), flush=True)
                        break
            finally:
                SC.chi2_of = _ORIG
            lim, at = limit95_from_min(pts)
            u_lim, u_at, u_pts = unmasked_limit(mode)
            move = (lim - u_lim) if (lim is not None and u_lim is not None) else None
            res['legs']['%s|%s' % (name, mode)] = dict(
                mask=name, mode=mode, limit95_meV=lim, min_at=at,
                unmasked613_meV=u_lim, unmasked_min_at=u_at,
                move_meV=move, kept=counts[name][0],
                sums=[p[0] for p in pts], totals=[p[1] for p in pts])
            print('  ⇒ %-9s %-8s limit95 = %s meV  (min at Sum=%.3f);  613-bin = %s meV '
                  '(min at %s);  MOVE = %s meV\n'
                  % (name, mode, ('%.3f' % lim) if lim else None, at,
                     ('%.3f' % u_lim) if u_lim else None, u_at,
                     ('%+.3f' % move) if move is not None else None), flush=True)

    print('=' * 100)
    print('  Ⓐ② ADDITIVITY: does low-only plus top-only make the full 555 move?')
    print('=' * 100)
    res['additivity'] = {}
    for mode in PL.MODES:
        f = res['legs'].get('instr555|%s' % mode, {}).get('move_meV')
        lo_ = res['legs'].get('low571|%s' % mode, {}).get('move_meV')
        tp = res['legs'].get('top597|%s' % mode, {}).get('move_meV')
        if None in (f, lo_, tp):
            print('  %-8s incomplete legs -- not scored' % mode)
            continue
        ssum = lo_ + tp
        resid = ssum - f
        frac = abs(resid) / abs(f) if f else None
        held = (frac is not None and frac <= 0.20)
        res['additivity'][mode] = dict(full=f, low_only=lo_, top_only=tp, sum_of_parts=ssum,
                                       residual=resid, residual_fraction=frac,
                                       within_20pc=bool(held))
        print('  %-8s full %+7.3f ;  low %+7.3f + top %+7.3f = %+7.3f ;  residual %+7.3f '
              '= %6.1f%% of the full move  -> registered bar (20%%) %s'
              % (mode, f, lo_, tp, ssum, resid, 100.0 * frac, 'HOLDS' if held else 'REFUTED'))
    print()
    json.dump(res, open(os.path.join(HERE, 'mask_limits.json'), 'w'), indent=1)
    print('  banked: mask_limits.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())

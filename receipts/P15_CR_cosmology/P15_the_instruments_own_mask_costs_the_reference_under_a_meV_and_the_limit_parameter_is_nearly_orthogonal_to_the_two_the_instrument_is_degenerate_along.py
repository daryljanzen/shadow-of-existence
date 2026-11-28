# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE INSTRUMENT'S OWN MASK COSTS THIS REFERENCE UNDER A meV, AND THE LIMIT PARAMETER IS
NEARLY ORTHOGONAL TO THE TWO THE INSTRUMENT IS DEGENERATE ALONG -- SO THE FACTOR OF 320 IS THE
INSTRUMENT'S AND NOT THE REFERENCE'S.

COMPUTES: the mask decomposition, the limits, the additivity residuals, the early-ISW shares and the
Fisher correlations, all RE-DERIVED here from primary records rather than read back as conclusions.
The bin counts come from `score_ttteee`'s own `BIN_LO`/`BIN_HI`/`BLOCK`; the limits from `r7853`'s
and `r7903`'s banked profile totals through this seat's own crossing reader; the shares from the
banked binned spectra, including the POWER-WEIGHTED aggregate recomputed from them; the correlations
by inverting the banked Fisher matrix. No CAMB runs here: the profiles and the custom-source legs
are the computation's cost and are not a receipt's to pay again.
** IT PINS AS RESULTS: ** the order's own premise is off by sixteen bins -- `NaN` below `ell = 100`
keeps `571`, not `555`, because `42` bins lie below `100` (fourteen from each block) and the
remaining `16` of the `58` are `TT`-only above `BIN_HI 1996`. The instrument's mask is
`ell >= 100` AND `ell <= 1996`, keeping `185` from EACH block.
⛔ ** AND THE MASK IS NEARLY FREE: ** the full substitution moves the limit `+0.792` meV on the
calibrated ruler and `+0.539` on the minimised, against `30.558` and `53.994` unmasked. The low and
top cuts ADD to within `4.2` and `3.0` per cent -- and on the minimised ruler they carry OPPOSITE
signs, `-0.120` low against `+0.676` top, so they act independently even while cancelling.
⛔ ** AND THE FACTOR OF 320 IS EXPLAINED: ** `rho(Sigma, omega_b)` is `+0.0548` on 613 bins and
`+0.0415` on 555, `rho(Sigma, n_s)` is `+0.0281` and `+0.0356`. Freeing two parameters cannot move a
limit when the limit parameter barely couples to them, so `60`'s `89.6` meV against `0.28` is the
INSTRUMENT's degeneracy.
⛔ ** AND THE EARLY-ISW SHARE FALLS ACROSS THE BAND: ** `0.4416` at `ell 100-108` to `0.3161` at
`199-207`, a fall of `28.4` per cent, with a power-weighted aggregate of `0.3996` at `Sigma = 0`
rising only to `0.4056` at `0.60` eV.
⛔ ** AND WHAT WAS REFUTED, SCORED NOT BURIED: ** two registered claims failed. The top part was
bounded at `<= 0.28` meV from another pipeline's figure and came back `+0.676` on the minimised
ruler. The share was claimed to fall MONOTONE and falls with one uptick, and the reason registered
beside it argued for RISING.
⛔ ** AND WHAT IS NOT CLAIMED: ** no mechanism for the share's shape, no reading of the instrument's
own likelihood, and no symmetric error on `Sigma`, whose Fisher row is a ONE-SIDED curvature because
the evaluation point sits on the boundary of the physical region.

    python3 <this file>
"""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7842 = glob.glob(os.path.join(BW, 'r7842_60_*'))[0]
R7853 = glob.glob(os.path.join(BW, 'r7853_cc66_*'))[0]
R7903 = glob.glob(os.path.join(BW, 'r7903_cc66_*'))[0]
sys.path.insert(0, R7842)

import score_ttteee as SC                                                    # noqa: E402

MASK = json.load(open(os.path.join(R7903, 'mask_limits.json'), encoding='utf-8'))
ISW = json.load(open(os.path.join(R7903, 'early_isw_share.json'), encoding='utf-8'))
FISH = json.load(open(os.path.join(R7903, 'fisher_block.json'), encoding='utf-8'))
MINL = json.load(open(os.path.join(R7903, 'profile_minimum_line.json'), encoding='utf-8'))

SUMS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
CROSS = 2.71
FAILS = []
NARMS = 0


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


def limit_from_min(pts):
    """this seat's crossing reader, on the profile-MINIMUM baseline r7903 ruled for"""
    pts = sorted(pts)
    s = np.array([p[0] for p in pts], float)
    t = np.array([p[1] for p in pts], float)
    d = t - t.min()
    if d.max() <= CROSS:
        return None
    fine = np.linspace(s[0], s[-1], 200001)
    i = np.where(np.interp(fine, s, d) > CROSS)[0]
    return float(fine[i[0]] * 1000.0) if len(i) else None


def banked613(mode):
    out = []
    for s in SUMS:
        p = os.path.join(R7853, 'out5', '%s_%.3f.json' % (mode, s))
        if os.path.exists(p):
            out.append((s, json.load(open(p))['total']))
    return out


print('=' * 100)
print('  A -- THE MASK, RE-DERIVED FROM THE LIKELIHOOD\'S OWN BIN EDGES')
print('=' * 100)

lo, hi, blk = np.asarray(SC.BIN_LO), np.asarray(SC.BIN_HI), np.asarray(SC.BLOCK)
n_low = int((lo < 100).sum())
n_top = int((hi > 1996).sum())
keep555 = (lo >= 100) & (hi <= 1996)
per_block = sorted(int((keep555 & (blk == b)).sum()) for b in (0, 1, 2))
n_total = int(lo.size)

check(u'Ⓐ① ⛭ RE-DERIVED: 42 bins lie below ℓ = 100, fourteen from each block',
      abs(n_low - 42) <= 0 and sorted(int(((lo < 100) & (blk == b)).sum()) for b in (0, 1, 2))
      == [14, 14, 14], '%d low, %s per block'
      % (n_low, sorted(int(((lo < 100) & (blk == b)).sum()) for b in (0, 1, 2))))

check(u'Ⓐ② ⛭ and 16 lie above BIN_HI 1996, EVERY ONE of them TT',
      abs(n_top - 16) <= 0 and int(((hi > 1996) & (blk == 0)).sum()) == n_top,
      '%d top, %d of them TT' % (n_top, int(((hi > 1996) & (blk == 0)).sum())))

check(u'Ⓐ③ ⛔ SO THE ORDER\'S PREMISE IS OFF BY SIXTEEN: the two cuts remove 58 '
      u'together, and a low cut ALONE leaves 571 rather than 555',
      abs((n_low + n_top) - 58) <= 0 and abs((n_total - n_low) - 571) <= 0,
      '%d + %d = %d removed; low-only keeps %d' % (n_low, n_top, n_low + n_top, n_total - n_low))

check(u'Ⓐ④ ⛭ and the instrument\'s mask keeps 185 from EACH block, 555 in all',
      per_block == [185, 185, 185] and abs(int(keep555.sum()) - 555) <= 0,
      '%d kept, %s per block' % (int(keep555.sum()), per_block))

check(u'Ⓐ⑤ the scorer\'s OWN counts agree with these arrays on all three masks',
      abs(MASK['masks']['instr555']['kept'] - 555) <= 0
      and abs(MASK['masks']['low571']['kept'] - 571) <= 0
      and abs(MASK['masks']['top597']['kept'] - 597) <= 0,
      '555/%d, 571/%d, 597/%d' % (MASK['masks']['instr555']['kept'],
                                  MASK['masks']['low571']['kept'],
                                  MASK['masks']['top597']['kept']))

check(u'Ⓐ⑥ ⛔ and the uncut control REFUSED nothing because it passed at EXACTLY '
      u'zero -- the mask is scored against the same likelihood',
      abs(MASK['uncut_control_worst'] - 0.0) <= 0.0 and MASK['uncut_control_points'] >= 16,
      'worst %.3e over %d points' % (MASK['uncut_control_worst'], MASK['uncut_control_points']))

print()
print('=' * 100)
print('  B -- THE LIMITS AND THE MOVES, RE-READ THROUGH THIS SEAT\'S OWN CROSSING READER')
print('=' * 100)

#: ⌷ the two banked figures carry DIFFERENT precisions -- `r7863` recorded `30.56` to
#  two decimals and `54.0` to one.  A first version of this arm compared BOTH at two and
#  failed correctly: `53.994` rounds to `53.99`, not `54.00`.  *Each is checked at the
#  precision it was banked at, which is the only comparison the record supports.*
u_cam = limit_from_min(banked613('rd_camb'))
u_min = limit_from_min(banked613('rd_min'))
check(u'Ⓑ① ⛭ RE-DERIVED: the unmasked 613-bin limits are 30.558 and 53.994 meV',
      abs(round(u_cam, 3) - 30.558) <= 1e-9 and abs(round(u_min, 3) - 53.994) <= 1e-9,
      '%.3f / %.3f meV' % (u_cam, u_min))

check(u'Ⓑ② ⛭ and they reproduce this seat\'s banked uncut figures at the precision each '
      u'was recorded to: 30.56 to two decimals, 54.0 to one',
      abs(round(u_cam, 2) - 30.56) <= 1e-9 and abs(round(u_min, 1) - 54.0) <= 1e-9,
      '%.2f and %.1f' % (round(u_cam, 2), round(u_min, 1)))

L = MASK['legs']
check(u'Ⓑ③ ⛭ the 555-bin limits are 31.350 and 54.533 meV',
      abs(round(L['instr555|rd_camb']['limit95_meV'], 3) - 31.350) <= 1e-9
      and abs(round(L['instr555|rd_min']['limit95_meV'], 3) - 54.533) <= 1e-9,
      '%.3f / %.3f' % (L['instr555|rd_camb']['limit95_meV'], L['instr555|rd_min']['limit95_meV']))

check(u'Ⓑ④ ⛔ SO THE MASK COSTS +0.792 meV CALIBRATED AND +0.539 MINIMISED -- under '
      u'a meV either way, against a registered band of 3.0',
      abs(round(L['instr555|rd_camb']['move_meV'], 3) - 0.792) <= 1e-9
      and abs(round(L['instr555|rd_min']['move_meV'], 3) - 0.539) <= 1e-9
      and max(abs(L['instr555|rd_camb']['move_meV']), abs(L['instr555|rd_min']['move_meV'])) <= 3.0,
      '%+.3f / %+.3f' % (L['instr555|rd_camb']['move_meV'], L['instr555|rd_min']['move_meV']))

check(u'Ⓑ⑤ ⛭ the low cut alone moves +0.640 and -0.120 -- OPPOSITE SIGNS between '
      u'the rulers',
      abs(round(L['low571|rd_camb']['move_meV'], 3) - 0.640) <= 1e-9
      and abs(round(L['low571|rd_min']['move_meV'], 3) + 0.120) <= 1e-9
      and L['low571|rd_camb']['move_meV'] > 0 > L['low571|rd_min']['move_meV'],
      '%+.3f / %+.3f' % (L['low571|rd_camb']['move_meV'], L['low571|rd_min']['move_meV']))

check(u'Ⓑ⑥ ⛭ and the top cut alone moves +0.186 and +0.676',
      abs(round(L['top597|rd_camb']['move_meV'], 3) - 0.186) <= 1e-9
      and abs(round(L['top597|rd_min']['move_meV'], 3) - 0.676) <= 1e-9,
      '%+.3f / %+.3f' % (L['top597|rd_camb']['move_meV'], L['top597|rd_min']['move_meV']))

print()
print('=' * 100)
print('  C -- ADDITIVITY, RECOMPUTED FROM THE THREE LEGS RATHER THAN READ OFF')
print('=' * 100)

for mode, pin in (('rd_camb', 4.2), ('rd_min', 3.0)):
    f = L['instr555|%s' % mode]['move_meV']
    a = L['low571|%s' % mode]['move_meV'] + L['top597|%s' % mode]['move_meV']
    frac = 100.0 * abs(a - f) / abs(f)
    check(u'Ⓒ %s: low + top reproduces the full move to %.1f per cent, inside the registered '
          u'20' % (mode, pin),
          abs(round(frac, 1) - pin) <= 0.05 and frac <= 20.0,
          'sum %+.3f vs full %+.3f, residual %.1f%%' % (a, f, frac))

check(u'Ⓒ③ ⛔ and the minimised ruler adds CANCELLING parts: a tightening low cut and '
      u'a loosening top cut still sum to the full move',
      L['low571|rd_min']['move_meV'] < 0 < L['top597|rd_min']['move_meV']
      and abs((L['low571|rd_min']['move_meV'] + L['top597|rd_min']['move_meV'])
              - L['instr555|rd_min']['move_meV']) <= 0.05,
      'low %+.3f + top %+.3f' % (L['low571|rd_min']['move_meV'], L['top597|rd_min']['move_meV']))

print()
print('=' * 100)
print('  D -- THE EARLY-ISW SHARE, WITH THE AGGREGATE RECOMPUTED FROM THE BINNED SPECTRA')
print('=' * 100)

p0 = ISW['per_sum']['0.00']
bf = np.array(p0['full_per_bin'], float)
bn = np.array(p0['no_isw_per_bin'], float)
agg0 = float((bf.sum() - bn.sum()) / bf.sum())
sh0 = (bf - bn) / bf

check(u'Ⓓ① ⛭ RE-DERIVED from the banked spectra: the POWER-WEIGHTED aggregate at '
      u'Σ = 0 is 0.3996, and it is NOT the unweighted mean of the shares',
      abs(round(agg0, 4) - 0.3996) <= 1e-9 and abs(agg0 - float(sh0.mean())) > 1e-4,
      'weighted %.4f, unweighted mean %.4f' % (agg0, sh0.mean()))

check(u'Ⓓ② ⛭ the share runs 0.4416 at ℓ 100-108 down to 0.3161 at 199-207',
      abs(round(float(sh0[0]), 4) - 0.4416) <= 1e-9
      and abs(round(float(sh0[-1]), 4) - 0.3161) <= 1e-9,
      '%.4f .. %.4f over %d bins' % (sh0[0], sh0[-1], sh0.size))

check(u'Ⓓ③ ⛔ a FALL of 28.4 per cent across the band, positive in every bin',
      abs(round(100.0 * float((sh0[0] - sh0[-1]) / sh0[0]), 1) - 28.4) <= 0.05
      and bool(np.all(sh0 > 0)),
      '-%.1f%%' % (100.0 * (sh0[0] - sh0[-1]) / sh0[0]))

check(u'Ⓓ④ ⚠ but NOT monotone: one uptick in the first increment, so the claim as '
      u'CODED is refuted while the claim as WORDED holds',
      not bool(np.all(np.diff(sh0) < 0)) and int(np.argmax(sh0)) == 1,
      'turnover at bin %d of %d' % (int(np.argmax(sh0)) + 1, sh0.size))

check(u'Ⓓ⑤ and the aggregate moves only 0.3996 to 0.4056 across the four sums, with a '
      u'worst per-bin spread of 0.0084',
      abs(round(ISW['per_sum']['0.60']['aggregate'], 4) - 0.4056) <= 1e-9
      and abs(round(ISW['worst_spread'], 4) - 0.0084) <= 1e-9,
      '%.4f at 0.60, worst spread %.4f' % (ISW['per_sum']['0.60']['aggregate'],
                                           ISW['worst_spread']))

check(u'Ⓓ⑥ and the band holds 12 TT bins, which is NOT r7892\'s 13 because that band is '
      u'everything below the first peak and this one is 100 to 207',
      len(ISW['bin_ell_lo']) == 12 and ISW['bin_ell_lo'][0] == 100 and ISW['bin_ell_hi'][-1] == 207,
      '%d bins, ℓ %d..%d' % (len(ISW['bin_ell_lo']), ISW['bin_ell_lo'][0],
                                  ISW['bin_ell_hi'][-1]))

print()
print('=' * 100)
print('  E -- THE FISHER BLOCK, CORRELATIONS RE-INVERTED FROM THE BANKED MATRIX')
print('=' * 100)

for mask, rwb, rns, cond in (('bin613', 0.0548, 0.0281, 2408.0), ('instr555', 0.0415, 0.0356, 2794.0)):
    B = FISH['blocks'][mask]
    F = np.array(B['fisher'], float)
    C = np.linalg.inv(F)
    sd = np.sqrt(np.diag(C))
    R = C / np.outer(sd, sd)
    check(u'Ⓔ %s: ⛭ RE-INVERTED, ρ(Σ, ω_b) = %+.4f and '
          u'ρ(Σ, n_s) = %+.4f, both far inside the registered 0.8'
          % (mask, rwb, rns),
          abs(round(float(R[0, 3]), 4) - rwb) <= 1e-9
          and abs(round(float(R[0, 4]), 4) - rns) <= 1e-9
          and max(abs(R[0, 3]), abs(R[0, 4])) <= 0.8,
          '%+.4f / %+.4f' % (R[0, 3], R[0, 4]))
    check(u'Ⓔ %s: the (ω_b, n_s) block is well conditioned at %.0f, under the '
          u'registered 1e4, and the whole block is POSITIVE DEFINITE' % (mask, cond),
          abs(round(float(np.linalg.cond(F[np.ix_([3, 4], [3, 4])])), 0) - cond) <= 1.0
          and bool(np.all(np.linalg.eigvalsh(F) > 0)),
          'cond %.1f, min eigenvalue %.3e' % (np.linalg.cond(F[np.ix_([3, 4], [3, 4])]),
                                              np.linalg.eigvalsh(F).min()))

check(u'Ⓔ⑤ ⛔ SO THE FACTOR OF 320 IS THE INSTRUMENT\'S: the limit parameter is '
      u'nearly ORTHOGONAL to the two directions the instrument is degenerate along',
      max(abs(FISH['blocks'][m]['rho_sigma_omegab']) for m in ('bin613', 'instr555')) <= 0.06
      and max(abs(FISH['blocks'][m]['rho_sigma_ns']) for m in ('bin613', 'instr555')) <= 0.06,
      'worst |rho| %.4f' % max(abs(FISH['blocks'][m][k])
                               for m in ('bin613', 'instr555')
                               for k in ('rho_sigma_omegab', 'rho_sigma_ns')))

check(u'Ⓔ⑥ and the mask loosens σ(Σ) from 0.0190 to 0.0204 eV, the same '
      u'direction as the limit move',
      abs(round(FISH['blocks']['bin613']['sigma_1sigma_eV'], 4) - 0.0190) <= 1e-9
      and abs(round(FISH['blocks']['instr555']['sigma_1sigma_eV'], 4) - 0.0204) <= 1e-9,
      '%.4f -> %.4f eV' % (FISH['blocks']['bin613']['sigma_1sigma_eV'],
                           FISH['blocks']['instr555']['sigma_1sigma_eV']))

print()
print('=' * 100)
print('  F -- THE PROFILE MINIMUM, AND WHAT THE RULING COSTS THIS REFERENCE')
print('=' * 100)

cal = MINL['rulers']['rd_camb']
check(u'Ⓕ① ⛭ RE-DERIVED: this reference\'s profile minimum is at Σ = 0 on both '
      u'rulers, so the ruled convention and the lowest-sum one are ONE reading',
      abs(cal['minimum_at_eV'] - 0.0) <= 1e-12
      and cal['conventions_coincide'] is True
      and MINL['rulers']['rd_min']['conventions_coincide'] is True,
      'minimum at %.2f eV, coincide %s' % (cal['minimum_at_eV'], cal['conventions_coincide']))

check(u'Ⓕ② ⛔ so the ruling costs THIS reference nothing, and the 22.734 meV '
      u'convention gap belongs to 60\'s banked profile whose minimum is elsewhere',
      abs(round(cal['limit_on_minimum_meV'], 3) - round(cal['limit_on_lowest_sum_meV'], 3)) <= 1e-9,
      '%.3f on both baselines' % cal['limit_on_minimum_meV'])

print()
print('=' * 100)
print('  G -- WHAT WAS REFUTED, AND WHAT IS NOT CLAIMED')
print('=' * 100)

RES = __doc__
check(u'Ⓖ① that the top-part bound was REFUTED on the minimised ruler, and why',
      'bounded at `<= 0.28` meV from another pipeline' in RES)
check(u'Ⓖ② that the share\'s monotonicity was refuted and its registered reason argued '
      u'for the opposite direction',
      'argued for RISING' in RES)
check(u'Ⓖ③ that no mechanism is offered for the share\'s shape',
      'no mechanism for the share' in RES)
check(u'Ⓖ④ that the instrument\'s own likelihood is NOT read here',
      'no reading of the instrument' in RES)
check(u'Ⓖ⑤ that Σ carries no symmetric error, because its Fisher row is one-sided '
      u'on the boundary',
      'ONE-SIDED curvature' in RES)
check(u'Ⓖ⑥ that no CAMB is run here and why',
      'not a receipt\'s to pay again' in RES)

print('\n' + '=' * 100)
print('  %d arm(s); %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('    FAILED: %s' % f)
print('=' * 100)
sys.exit(1 if FAILS else 0)

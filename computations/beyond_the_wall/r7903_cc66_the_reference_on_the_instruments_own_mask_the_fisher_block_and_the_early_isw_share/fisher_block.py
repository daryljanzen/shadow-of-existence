# -*- coding: utf-8 -*-
"""r7903+cc66 item ⑲②: THE 5x5 FISHER BLOCK IN (Sigma, H0, Om, omega_b, n_s), ON 555 AND ON 613.

Order `r7903` (69) item ⑲②.  Registered at `b7ade4b6d` before this file existed: the reference is
STIFF along `omega_b` and `n_s` -- `|rho|` with `Sigma` at most `0.8` on both masks and the
`(omega_b, n_s)` 2x2 condition number under `1e4` -- which would make 60's factor of `320` the
INSTRUMENT's degeneracy rather than anything unusual on the reference's side.

** THE CURVATURE IS THIS SEAT'S FITTER'S OWN OBJECTIVE. **  `F_ij = 1/2 d^2 chi2 / dtheta_i
dtheta_j`, where `chi2` is `profile_likeforlike.score`'s total: the plik_lite CMB term through
`score_ttteee`, plus lensing, plus the tau prior, plus BAO.  `tau` is HELD at the evaluation point,
because the order names five parameters and `tau` is not among them.

⛔ ** SIGMA SITS ON THE BOUNDARY AND THE FILE SAYS SO RATHER THAN HIDING IT. **  `Sigma >= 0` is the
physical region, the evaluation point is `Sigma = 0`, so `Sigma`'s derivatives are ONE-SIDED
(forward).  A symmetric error ellipse through a boundary is not a confidence statement, and this was
registered in advance rather than offered afterwards if the number looked awkward.  The `Sigma` row
and column are therefore a one-sided curvature and are labelled as such in the output.

** THE EVALUATION POINT IS EACH MASK'S OWN `Sigma = 0` BEST FIT **, not one point shared between
them: the mask changes the fit, so the curvature of the 555-bin likelihood belongs at the 555-bin
minimum.  ⌗ *A judgement call, stated: the alternative is to evaluate both at the 613 fit, which
would mix one likelihood's curvature with another's location.*

** ONE REFUSING CONTROL: ** the block must be POSITIVE DEFINITE.  At a minimum it has to be, so a
non-positive eigenvalue means the point is not a minimum or the steps are wrong, and either way the
correlations would be meaningless.

    python3 <this file>
"""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
R7853 = glob.glob(os.path.join(BW, 'r7853_cc66_*'))[0]
sys.path.insert(0, R7853)

import profile_likeforlike as PL                                             # noqa: E402
import score_ttteee as SC                                                    # noqa: E402

_spec = __import__('importlib.util', fromlist=['util']).spec_from_file_location(
    'cc66_r7903_mask', os.path.join(HERE, 'mask_rescore.py'))
_mr = __import__('importlib.util', fromlist=['util']).module_from_spec(_spec)
_spec.loader.exec_module(_mr)

NAMES = ('Sigma', 'H0', 'Om', 'omega_b', 'n_s')
#: steps: large enough to beat differencing cancellation, small enough to be curvature
STEP = (0.01, 0.20, 0.0020, 0.00010, 0.0040)
MODE = 'rd_camb'                      #: the calibrated ruler, the one the limit question rests on
MASKS = ('bin613', 'instr555')


def point_for(mask):
    """each mask's own Sigma = 0 best fit -- the location where its curvature belongs"""
    if mask == 'bin613':
        d = json.load(open(os.path.join(R7853, 'out5', '%s_0.000.json' % MODE)))
    else:
        d = json.load(open(os.path.join(HERE, 'mask_out', '%s_%s_0.000.json' % (mask, MODE))))
    return [0.0, d['H0'], d['Om'], d['ombh2'], d['ns']], d['tau'], d['total']


def chi2_at(x, tau):
    return float(PL.score(x[0], x[1], x[2], x[3], x[4], tau, MODE)[0])


def fisher(x0, tau):
    """1/2 d^2 chi2, central in the four free directions and FORWARD in Sigma (the boundary)"""
    n = len(x0)
    H = np.zeros((n, n))
    cache = {}

    def f(d):
        k = tuple(round(v, 12) for v in d)
        if k not in cache:
            cache[k] = chi2_at([x0[i] + d[i] for i in range(n)], tau)
        return cache[k]

    z = [0.0] * n
    f0 = f(z)
    for i in range(n):
        h = STEP[i]
        a, b = [0.0] * n, [0.0] * n
        if i == 0:                                   # Sigma: forward second difference
            a[i], b[i] = h, 2.0 * h
            H[i, i] = (f(b) - 2.0 * f(a) + f0) / (h * h)
        else:
            a[i], b[i] = h, -h
            H[i, i] = (f(a) - 2.0 * f0 + f(b)) / (h * h)
    for i in range(n):
        for j in range(i + 1, n):
            hi, hj = STEP[i], STEP[j]
            if i == 0:                               # one-sided in Sigma, central in the other
                pp, pm = [0.0] * n, [0.0] * n
                zp, zm = [0.0] * n, [0.0] * n
                pp[i], pp[j] = hi, hj
                pm[i], pm[j] = hi, -hj
                zp[j], zm[j] = hj, -hj
                H[i, j] = (f(pp) - f(pm) - f(zp) + f(zm)) / (2.0 * hi * hj)
            else:
                pp, pm, mp, mm = [0.0] * n, [0.0] * n, [0.0] * n, [0.0] * n
                pp[i], pp[j] = hi, hj
                pm[i], pm[j] = hi, -hj
                mp[i], mp[j] = -hi, hj
                mm[i], mm[j] = -hi, -hj
                H[i, j] = (f(pp) - f(pm) - f(mp) + f(mm)) / (4.0 * hi * hj)
            H[j, i] = H[i, j]
    return 0.5 * H, len(cache)


def main():
    out = {'names': list(NAMES), 'steps': list(STEP), 'mode': MODE,
           'objective': 'profile_likeforlike.score total: plik_lite CMB + lensing + tau prior + BAO',
           'tau': 'HELD at the evaluation point; the order names five parameters and tau is not one',
           'sigma_note': 'Sigma >= 0 is the physical region and the point is Sigma = 0, so the '
                         'Sigma row/column are a ONE-SIDED (forward) curvature, not a symmetric one',
           'evaluation_point': 'each mask\'s OWN Sigma = 0 best fit', 'blocks': {}}
    print('=' * 100)
    print('  ⑲② THE 5x5 FISHER BLOCK, ON 555 AND ON 613')
    print('=' * 100)
    print('  parameters: %s' % ', '.join(NAMES))
    print('  ⛔ Sigma is on the boundary: its row/column are ONE-SIDED, registered in advance')
    print()
    ok = True
    for mask in MASKS:
        x0, tau, tot = point_for(mask)
        if mask == 'bin613':
            SC.chi2_of = _mr._ORIG
        else:
            m = _mr.MASKS[mask]
            SC.chi2_of = _mr._masked(m['lo'], m['hi'])
        try:
            F, nev = fisher(x0, tau)
        finally:
            SC.chi2_of = _mr._ORIG
        w = np.linalg.eigvalsh(F)
        pd = bool(np.all(w > 0))
        C = np.linalg.inv(F)
        sd = np.sqrt(np.diag(C))
        R = C / np.outer(sd, sd)
        sub = F[np.ix_([3, 4], [3, 4])]
        cond = float(np.linalg.cond(sub))
        out['blocks'][mask] = dict(
            point=dict(zip(NAMES, [float(v) for v in x0])), tau=float(tau), total=float(tot),
            evaluations=nev, fisher=[[float(v) for v in r] for r in F],
            eigenvalues=[float(v) for v in w], positive_definite=pd,
            correlation=[[float(v) for v in r] for r in R],
            rho_sigma_omegab=float(R[0, 3]), rho_sigma_ns=float(R[0, 4]),
            cond_omegab_ns=cond, sigma_1sigma_eV=float(sd[0]))
        print('  %-9s point H0 %.3f Om %.4f wb %.5f ns %.4f tau %.4f   (%d evaluations)'
              % (mask, x0[1], x0[2], x0[3], x0[4], tau, nev))
        print('      positive definite: %-5s   eigenvalues %s'
              % (pd, ' '.join('%.3e' % v for v in w)))
        print('      rho(Sigma, omega_b) = %+.4f    rho(Sigma, n_s) = %+.4f'
              % (R[0, 3], R[0, 4]))
        print('      cond[(omega_b, n_s)] = %.3e      sigma(Sigma) = %.4f eV' % (cond, sd[0]))
        if not pd:
            ok = False
            print('      ⛔ NOT POSITIVE DEFINITE -- the correlations below are not reported as '
                  'meaningful')
        print()
    if not ok:
        print('  ⛔ REFUSING to score the registered claims: a block that is not positive definite '
              'is not a curvature at a minimum.')
        json.dump(out, open(os.path.join(HERE, 'fisher_block.json'), 'w'), indent=1)
        return 1

    print('  ' + '-' * 96)
    print('  THE REGISTERED CLAIMS, SCORED')
    print('  ' + '-' * 96)
    b1 = all(abs(out['blocks'][m]['rho_sigma_omegab']) <= 0.8
             and abs(out['blocks'][m]['rho_sigma_ns']) <= 0.8 for m in MASKS)
    b2 = all(out['blocks'][m]['cond_omegab_ns'] < 1e4 for m in MASKS)
    out['claims'] = {'Ⓑ①_rho_at_most_0.8_both_masks': bool(b1),
                     'Ⓑ①_cond_under_1e4_both_masks': bool(b2),
                     'Ⓑ②_320_is_the_instruments_degeneracy': bool(b1 and b2)}
    print('  Ⓑ① |rho| <= 0.8 along omega_b and n_s, both masks : %s' % ('HOLDS' if b1 else 'REFUTED'))
    print('  Ⓑ① cond[(omega_b, n_s)] < 1e4, both masks         : %s' % ('HOLDS' if b2 else 'REFUTED'))
    print('  Ⓑ② so 60\'s factor of 320 is the INSTRUMENT\'s      : %s'
          % ('SUPPORTED' if (b1 and b2) else 'NOT SUPPORTED'))
    print()
    json.dump(out, open(os.path.join(HERE, 'fisher_block.json'), 'w'), indent=1)
    print('  banked: fisher_block.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())

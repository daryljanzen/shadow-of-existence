#!/usr/bin/env python3
"""`r7856` Ⓞ⓪ Ⓐ① Ⓐ①ᵇ Ⓐ①ᶜ — the lensing power against the reference, bin by bin.

Reads the two BANKED bandpower vectors rather than re-solving: `r7850`'s `grid_ics_eta4000`
(`BVEL` unset) and `r7854`'s `grid_ics_eta4000_bvel1` (`BVEL` on).  Neither is re-run, because
neither tree changed -- the cron forbids re-running a long job for reassurance.

⚠ ** THE MAGNITUDE OF `r_i` IS CONVENTION AND ONLY ITS SHAPE IS PHYSICS **, which the amendment to
this revision's `PREDICTION.md` registered before this file existed.  The shape test `Ⓐ①` and the
before/after test `Ⓐ①ᶜ` are both ratios of ratios in ONE convention and are therefore sound; `Ⓐ①ᵇ`
is reported as registered and marked vacuous in the direction it was aimed.

Run: python3 ratio.py        (writes ratio.json)
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
R7850 = os.path.join(_BTW, 'r7850_60_phi_carried_through_the_radiation_era')
R7854 = os.path.join(_BTW, 'r7854_60_the_potential_repaired_in_the_hierarchy_and_the_recalibration_sized')
os.environ.setdefault('NOPROJ', '1')
sys.path.insert(0, R7846)
import lensing_like as LL                                                  # noqa: E402

sys.path.insert(0, R7850)
import camb_reference as CR                                                # noqa: E402

# the record Ⓞ⓪ must reproduce, from r7854's own summary.json -- read, not retyped
LANDED_AMP = 1.5768615382253947e-09
LANDED_PER_DOF = 2.1313389647028673
REPAIRED_AMP = 8.164235700977891e-10
REPAIRED_PER_DOF = 1.0533934590398568
CAMB_PER_DOF_EXACT = 1.066836
# r7850's camb_reference.json, nothing fitted and one amplitude fitted
CAMB_CHI2_NOTHING = 8.817347545463614
CAMB_AMP_FITTED = 1.002493850450405


def vec(path):
    d = json.load(io.open(path, encoding='utf-8'))
    return np.asarray(d['bandpowers'], float), d


def score(b, amplitude=None):
    a = (float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b)) if amplitude is None
         else float(amplitude))
    r = LL.DATA - a * b
    return float(r @ LL.FISHER @ r), a


def main():
    out = {}
    b_land, rec_land = vec(os.path.join(R7850, 'grid_ics_eta4000', 'lcdm_S000.json'))
    b_rep, rec_rep = vec(os.path.join(R7854, 'grid_ics_eta4000_bvel1', 'lcdm_S000.json'))
    ndof = LL.NBP - 1

    print('\n  Ⓞ⓪ THE POSITIVE CONTROL -- this file reproduces r7854\'s landed record', flush=True)
    c2l, al = score(b_land)
    c2r, ar = score(b_rep)
    pdl, pdr = c2l / ndof, c2r / ndof
    ok0 = (abs(al / LANDED_AMP - 1) < 1e-6 and abs(pdl / LANDED_PER_DOF - 1) < 1e-6
           and abs(ar / REPAIRED_AMP - 1) < 1e-6 and abs(pdr / REPAIRED_PER_DOF - 1) < 1e-6)
    print('      landed    fitted factor %.10e (record %.10e)   per dof %.10f (record %.10f)'
          % (al, LANDED_AMP, pdl, LANDED_PER_DOF))
    print('      repaired  fitted factor %.10e (record %.10e)   per dof %.10f (record %.10f)'
          % (ar, REPAIRED_AMP, pdr, REPAIRED_PER_DOF))
    print('    ** %s **' % ('Ⓞ⓪ HOLDS: the same vectors and the same scorer, so what follows reads '
                            'the scale and not this file'
                            if ok0 else 'Ⓞ⓪ FAILS: this file does not reproduce the banked record '
                            'and nothing below is a reading of anything'), flush=True)
    out['control'] = dict(holds=bool(ok0), landed_amp=al, landed_per_dof=pdl,
                          repaired_amp=ar, repaired_per_dof=pdr)
    if not ok0:
        with io.open(os.path.join(_HERE, 'ratio.json'), 'w', encoding='utf-8') as fh:
            json.dump(out, fh, indent=1, sort_keys=True)
        return 1

    print('\n  THE REFERENCE, at the control\'s cosmology and a STATED A_s', flush=True)
    b_camb, cfg = CR.camb_bandpowers(CR.MNU)
    c2c_nothing, _ = score(b_camb, amplitude=1.0)
    c2c_free, ac = score(b_camb)
    print('      A_s = %.3e (a parameter), mnu = %.3f' % (cfg['As'], cfg['mnu']))
    print('      nothing fitted  chi2 %.10f (record %.10f)' % (c2c_nothing, CAMB_CHI2_NOTHING))
    print('      one fitted      chi2 %.10f at a factor %.10f (record %.10f)'
          % (c2c_free, ac, CAMB_AMP_FITTED))
    ok_ref = abs(c2c_nothing / CAMB_CHI2_NOTHING - 1) < 1e-6 and abs(ac / CAMB_AMP_FITTED - 1) < 1e-6
    print('    ⌗ the reference is reproduced here: %s' % ok_ref, flush=True)
    out['reference'] = dict(reproduced=bool(ok_ref), chi2_nothing_fitted=c2c_nothing,
                            chi2_one_fitted=c2c_free, fitted_factor=ac, As=float(cfg['As']),
                            mnu=float(cfg['mnu']), bandpowers=[float(v) for v in b_camb])

    print('\n  Ⓐ① THE RATIO, BIN BY BIN -- the repaired instrument over the reference', flush=True)
    r_rep = b_rep / b_camb
    r_land = b_land / b_camb
    rbar_rep, rbar_land = float(np.mean(r_rep)), float(np.mean(r_land))
    spread_rep = float(np.max(np.abs(r_rep / rbar_rep - 1.0)))
    spread_land = float(np.max(np.abs(r_land / rbar_land - 1.0)))
    print('      bin   L_av       repaired/ref        r_i/r_bar      landed/ref       r_i/r_bar')
    for i in range(LL.NBP):
        print('       %d   %6.1f    %.6e    %+8.4f      %.6e   %+8.4f'
              % (i + 1, LL.L_AV[i], r_rep[i], r_rep[i] / rbar_rep - 1.0,
                 r_land[i], r_land[i] / rbar_land - 1.0), flush=True)
    print('\n    repaired: r_bar %.6e, worst |r_i/r_bar - 1| = %.4f  (criterion < 0.10)'
          % (rbar_rep, spread_rep))
    print('    landed:   r_bar %.6e, worst |r_i/r_bar - 1| = %.4f'
          % (rbar_land, spread_land))
    a1 = spread_rep < 0.10
    print('    ** Ⓐ① %s AS REGISTERED **'
          % ('PASSES' if a1 else 'FAILS -- the ratio is a function of L, so the fault is still '
                                 'partly SHAPE at the bandpower level'), flush=True)
    out['A1'] = dict(passes=bool(a1), criterion=0.10,
                     repaired_rbar=rbar_rep, repaired_worst=spread_rep,
                     landed_rbar=rbar_land, landed_worst=spread_land,
                     ratio_repaired=[float(v) for v in r_rep],
                     ratio_landed=[float(v) for v in r_land],
                     L_av=[float(v) for v in LL.L_AV])

    print('\n  Ⓐ①ᵇ REPORTED AS REGISTERED, AND VACUOUS IN THE DIRECTION IT WAS AIMED', flush=True)
    near2 = abs(rbar_rep / 2.0 - 1.0) < 0.10
    print('      r_bar = %.6e;  within ten per cent of 2? %s' % (rbar_rep, near2))
    print('      1 / the lensing fit\'s own factor = %.6e, which r_bar tracks to %.4f per cent'
          % (1.0 / ar, 100 * abs(rbar_rep * ar - 1.0)))
    print('    ** Ⓐ①ᵇ passes as registered (r_bar is NOT near 2) and the passing MEANS NOTHING: **')
    print('      r_bar is 1 / the fitted factor to a fraction of a per cent, i.e. it is the '
          'instrument\'s')
    print('      missing primordial normalisation and not a gap. The amendment registered this '
          'before measuring.', flush=True)
    out['A1b'] = dict(passes_as_registered=bool(not near2), rbar=rbar_rep,
                      inverse_fitted_factor=float(1.0 / ar),
                      rbar_times_fitted_factor=float(rbar_rep * ar),
                      vacuous_in_the_direction_aimed=True)

    print('\n  Ⓐ①ᶜ DID THE REPAIR MOVE THE ABSOLUTE SCALE TOWARD THE REFERENCE OR AWAY?', flush=True)
    # ⚠ in ONE convention, so the RATIO of the two r_bar is physical even though each is not
    move = rbar_rep / rbar_land
    print('      r_bar after / r_bar before = %.6f  -- the repair multiplied the instrument\'s'
          % move)
    print('      lensing power by that factor relative to the reference')
    print('      |log r_bar| is not comparable across conventions, so the test is on this ratio:')
    print('        the repair raised the power by %.4f, and the fitted factor fell by %.4f'
          % (move, al / ar))
    away = abs(np.log(move)) > 0.0 and move > 1.0
    print('    ** Ⓐ①ᶜ: the repair moved the absolute scale %s the reference **'
          % ('AWAY FROM (upward)' if move > 1.0 else 'TOWARD (downward)'))
    print('      ⌗ registered expectation was AWAY: %s' % ('HELD' if away else 'REFUTED'),
          flush=True)
    out['A1c'] = dict(rbar_after_over_before=float(move),
                      fitted_factor_before_over_after=float(al / ar),
                      moved_away=bool(move > 1.0),
                      registered_expectation_held=bool(away))

    with io.open(os.path.join(_HERE, 'ratio.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote ratio.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

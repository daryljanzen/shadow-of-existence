#!/usr/bin/env python3
"""** THE DEFECT, LOCATED AND CLOSED ARITHMETICALLY: THE BARYONS NEVER CLUSTER. **

`locate.py` ruled out the two candidates this seat could name in advance:

  ⒷⒷ the RATE is consistent with its own source to `8.882e-16` -- machine precision -- so the
     registered expectation that the Friedmann relation was broken is REFUTED outright.
  ⒶⒶ the potential TRACKS its own Poisson relation to `0.9985`-`1.0000` on every mode with
     `k/Hc > 40`, so its equation is doing exactly what it should.

** What moves is the SOURCE, and it moves because the contrasts grow too slowly: ** the exponent
`dln d_cb / dln a` converges to about `0.899` where matter domination demands `1`.

⇒ ** AND THE SHORTFALL IS THE BARYONS. **  `delta_b / delta_c` is `1.0` at the largest scales and
falls to a few parts in a thousand for `k >= 0.02` -- the modes the lensing kernel weights.  So the
Poisson source carries the COLD MATTER ALONE, which is `OCDM/(OCDM+OB)` of the clustering matter.

** The arithmetic closes without a free parameter. **  In matter domination `d'' + Hc d' =
(3/2) Hc^2 Om_eff d` with `Hc = 2/eta` and `a ~ eta^2` gives `n^2 + n - 6 Om_eff = 0` and
`d ~ a^(n/2)`:

    Om_eff = 1         ->  a^1.0000      (all the matter clusters)
    Om_eff = 0.843463  ->  a^0.9023      (the cold matter alone)
    measured, k >= 0.02, late intervals  ->  about a^0.899

and a potential tracking `Hc^2 d / k^2` with `d ~ a^p` moves as `a^(p-1)`, which over the probed
interval is the factor `r7852` measured.  ** Three independent readings, one cause. **

** THE MECHANISM IS ONE LINE OF THE HIERARCHY. **  The solver's baryon continuity is
`out[:, I_DB] = -tg + DRC * 3 * Php` -- the PHOTON velocity, at every time, because the state
carries no baryon velocity of its own.  *Before decoupling that is the tight-coupling approximation
and it is right.*  ⛔ **After decoupling the photons free-stream and the baryons are left with no
velocity at all, so `delta_b` can never catch `delta_c`.**  ⌗ The same file's OTHER solver already
carries `tb` and the slip term `tp * (tb - tg)`, so the correct structure exists in the tree; it is
the solve the lensing path uses that does not have it.

Run: python3 diagnosis.py        (writes diagnosis.json; reads locate.py's banked state)
"""
import io
import json
import math
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
sys.path.insert(0, _BTW)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

import ACOUSTIC_two_arm as A                                                 # noqa: E402

SUBH = 0.02          # the wavenumber above which every probed mode has k/Hc > 40


def exponent(om):
    """`d ~ a^p` in matter domination with a clustering fraction `om` -- the quadratic, not a fit

    ⚠ The quadratic `n^2 + n - 6 om = 0` is in CONFORMAL TIME, where `d ~ eta^n`, and `a ~ eta^2`
    there, so the exponent in `a` is `n/2`.  *The first draft of this function returned `n` and
    printed it as the exponent in `a`, which made both predictions twice their true value and the
    comparison meaningless.*
    """
    n = 0.5 * (-1.0 + math.sqrt(1.0 + 24.0 * om))
    return 0.5 * n


def main():
    st = np.load(os.path.join(_HERE, 'locate_state.npz'))
    loc = json.load(io.open(os.path.join(_HERE, 'locate.json'), encoding='utf-8'))
    Y, etas, kk = st['Y'], [float(v) for v in st['etas']], st['kk']
    NV = Y.shape[2]
    # ⚠ ** ASKED FOR, NOT DERIVED. **  *`locate_state.npz` is the PRE-repair bank, so `NV - 1` is in
    # fact the baryon contrast in it -- but deriving the index is the silent-failure machine this
    # revision's own guard names, and a bank re-made under `BVEL=1` would hand this line the baryon
    # VELOCITY without a word.  The index is read from the instrument, and the bank's own width is
    # asserted against it so that a WIDER bank is refused here rather than silently mis-read.*
    assert NV == A.I_DB_F + 1, (
        'this file reads the PRE-repair bank, whose width must be the BVEL-off one: got NV=%d '
        'against I_DB_F=%d' % (NV, A.I_DB_F))
    dc, db = Y[:, :, 0], Y[:, :, A.I_DB_F]
    ratio = db / dc

    wc = float(A.OCDM) / (float(A.OCDM) + float(A.OB))
    p_cold, p_all = exponent(wc), exponent(1.0)

    sub = kk >= SUBH
    # ** the comparison is on the LAST interval, the deepest in matter domination, and the trend
    #    over the earlier ones is reported beside it rather than averaged into it. **  Averaging
    #    across intervals mixes times at which the radiation share differs by a factor thirty.
    # ⚠ ** SORTED BY THE INTERVAL'S OWN START TIME, not by the order a JSON object happens to
    #   hold its keys in. **  *The first draft read the keys as written and took `914-1200` for the
    #   last interval, which is the one place this comparison must not be approximate.*
    keys = sorted(loc['growth_exponent'], key=lambda s_: float(s_.split('-')[0]))
    meas = list(np.array(loc['growth_exponent'][keys[-1]])[sub])
    p_meas = float(np.mean(meas))
    spread = float(np.max(meas) - np.min(meas))
    trend = [(k, float(np.mean(np.array(loc['growth_exponent'][k])[sub]))) for k in keys]

    print('\n  THE DEFECT: delta_b / delta_c, at the last banked time')
    print('      k [/Mpc]   db/dc      k/Hc')
    for j, k in enumerate(kk):
        print('      %8.4g   %+8.5f  %8.1f' % (k, ratio[-1, j], loc['k_over_Hc_at_last'][j]))
    worst_sub = float(np.max(np.abs(ratio[-1][sub])))
    print('    ⇒ above k = %g the baryons carry at most %.4f of the cold matter\'s contrast'
          % (SUBH, worst_sub))

    print('\n  THE ARITHMETIC, with no free parameter')
    print('      all the matter clusters                 d ~ a^%.4f' % p_all)
    print('      the cold matter alone (%.6f)         d ~ a^%.4f' % (wc, p_cold))
    print('      measured, k >= %g, the LAST interval     d ~ a^%.4f  (spread %.4f over %d '
          'modes)' % (SUBH, p_meas, spread, len(meas)))
    print('      and the trend toward it, interval by interval:')
    for k, v in trend:
        print('          %-14s a^%.4f' % (k, v))
    print('    ⇒ the measured exponent sits %.4f from the cold-matter-only prediction and %.4f '
          'from the all-matter one' % (abs(p_meas - p_cold), abs(p_meas - p_all)))
    closes = abs(p_meas - p_cold) < 0.2 * abs(p_meas - p_all)
    print('    ** %s **' % ('THE COLD-MATTER-ONLY PREDICTION IS THE ONE THE MEASUREMENT PICKS'
                            if closes else 'neither prediction is picked, and the cause is not this'))

    print('\n  AND THE RULED-OUT CANDIDATES, from locate.json')
    print('      the rate against its source, worst residual   %.3e  (registered as BROKEN, '
          'and it is not)' % loc['friedmann_worst'])
    qs = np.array(loc['phi_over_quasistatic'])[-1][sub]
    print('      the potential over its Poisson value, k >= %g  %.4f .. %.4f'
          % (SUBH, qs.min(), qs.max()))

    src = ' '.join(io.open(os.path.join(_BTW, 'ACOUSTIC_two_arm.py'),
                           encoding='utf-8').read().split())
    has_tg = 'out[:, I_DB] = -tg + DRC * 3 * Php' in src
    has_tb_elsewhere = 'tp * (tb - tg)' in src
    print('\n  THE MECHANISM, read off the solver')
    print('      the baryon continuity is driven by the photon velocity:  %s' % has_tg)
    print('      and the same file\'s other solver carries a baryon velocity: %s'
          % has_tb_elsewhere)

    out = dict(k=[float(v) for v in kk], etas=etas,
               db_over_dc_last=[float(v) for v in ratio[-1]],
               db_over_dc_all=[[float(v) for v in row] for row in ratio],
               subhorizon_k=SUBH,
               worst_db_over_dc_subhorizon=worst_sub,
               cold_fraction=wc,
               exponent_all_matter=p_all, exponent_cold_only=p_cold,
               exponent_measured=p_meas, exponent_spread=spread,
               exponent_trend={k: v for k, v in trend},
               n_readings=len(meas),
               picks_cold_only=bool(closes),
               friedmann_worst=loc['friedmann_worst'],
               rate_registered_broken_and_is_not=bool(loc['rate_is_consistent']),
               phi_over_quasistatic_subhorizon=[float(qs.min()), float(qs.max())],
               baryon_continuity_uses_photon_velocity=bool(has_tg),
               other_solver_carries_baryon_velocity=bool(has_tb_elsewhere))
    with io.open(os.path.join(_HERE, 'diagnosis.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote diagnosis.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

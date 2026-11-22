#!/usr/bin/env python3
"""** Ⓒ③/Ⓓ④: THE REPAIR, WITH THE EDIT'S OWN POSITIVE CONTROL FIRST. **

`diagnosis.py` located the defect in one line of the solver and `BVEL=1` repairs it: the baryons
carry their own velocity, single-fluid while `tau' > TCSW` and on `evolve_hier`'s own Euler equation
below it.

⚠ ** THE CONTROL COMES FIRST, because the edit moves the state layout. **  With `BVEL` unset the
solver must reproduce the state `locate.py` banked BEFORE the edit existed, to the integrator's own
tolerance.  *An edit to a shared instrument that cannot show that is not a repair, whatever the
repaired run says* -- and `r7852`'s first version was wrong by a factor eight thousand with no
symptom until its control was built.

Then three readings on the repaired solver, each against what `PREDICTION.md` registered:

  Ⓒ③  `|Phi(k, eta)/Phi(k, 4000) - 1| < 0.02` on every mode in `1e-3 .. 1` over `500 .. 4000`,
      against `0.053`-`0.539` measured before.  ** And the PRECISION THE CLOSED TEST CAN SHOW is
      stated: ** the residual the comparison itself carries, taken as the spread over the modes
      whose contrasts are not the thing being tested.
  Ⓐ①ᵈ the growth exponent, which should move from `0.9011` to `1`, and `delta_b/delta_c`, which
      should move from `2e-4` toward `1` on the modes the kernel weights.
  Ⓓ④  the repaired potential's shape against CAMB's Weyl at the control's fixed cosmology.

Run: BVEL=1 python3 repair.py         (writes repair.json; two solves, both cached)
"""
import io
import json
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7852 = os.path.join(_BTW, 'r7852_60_the_lensing_potential_reconciled_with_camb_term_by_term')
sys.path.insert(0, _BTW)
sys.path.insert(0, R7852)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

ETAS = [500.0, 700.0, 914.0, 1200.0, 1400.0, 1893.0, 2500.0, 3200.0, 4000.0]
KK = np.array([2e-4, 1e-3, 5e-3, 1e-2, 2e-2, 5e-2, 1e-1, 3e-1, 1.0])
SUBH = 0.02
NSTILT = 0.965


def _instrument_tag():
    """⚠ the cache is keyed by the INSTRUMENT'S OWN SOURCE as well as the switch, because a cache
    keyed by the switch alone is read by a LATER instrument and silently answers for the earlier
    one.  *That is the defect this line recorded at `r7852` -- a solve keyed in one place and not
    the other is not keyed -- and the fix belongs here rather than in a note.*"""
    import hashlib
    with io.open(os.path.join(_BTW, 'ACOUSTIC_two_arm.py'), 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:10]


def solve(bvel):
    """one solve at the banked configuration, with `BVEL` as given -- cached by that flag AND by
    the instrument's own source, so a changed instrument cannot read an earlier instrument's state"""
    cache = os.path.join(_HERE, 'repair_state_bvel%d_%s.npz' % (int(bvel), _instrument_tag()))
    if os.path.exists(cache):
        z = np.load(cache)
        return z['Y'], int(z['NV']), int(z['I_DB']), None
    env = dict(os.environ)
    env['BVEL'] = '1' if bvel else '0'
    code = (
        'import os, sys, numpy as np\n'
        'sys.path.insert(0, %r)\n'
        'import ACOUSTIC_two_arm as A\n'
        'kk = np.array(%r)\n'
        'etas = np.array(%r)\n'
        'sol, nk, NV = A.evolve(kk, t_eval=etas, e_end=float(etas[-1]))\n'
        'assert sol.status == 0, sol.message\n'
        'Y = sol.y.T.reshape(len(etas), nk, NV)\n'
        'np.savez_compressed(%r, Y=Y, NV=NV, I_DB=A.I_DB_F, bvel=A.BVEL)\n'
        % (_BTW, list(KK), ETAS, cache))
    import subprocess
    t0 = time.time()
    r = subprocess.run([sys.executable, '-c', code], env=env, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit('the BVEL=%d solve failed:\n%s' % (int(bvel), r.stdout[-3000:]
                                                            + r.stderr[-3000:]))
    secs = round(time.time() - t0, 2)
    z = np.load(cache)
    return z['Y'], int(z['NV']), int(z['I_DB']), secs


def main():
    t_all = time.time()
    out = dict(etas=ETAS, k=[float(v) for v in KK], subhorizon_k=SUBH, timings={})

    # ── ⓪ the control: BVEL off must reproduce the state banked before the edit
    print('\n  ⓪ THE POSITIVE CONTROL -- BVEL off against the state banked before the edit',
          flush=True)
    Y0, NV0, IDB0, s0 = solve(False)
    out['timings']['solve_bvel0'] = dict(seconds=s0, etas=len(ETAS), modes=len(KK), bvel=0)
    pre = np.load(os.path.join(_HERE, 'locate_state.npz'))['Y']
    assert pre.shape == Y0.shape, 'the control and the banked state are different shapes'
    den = np.maximum(np.abs(pre), 1e-300)
    rel = np.abs(Y0 - pre) / den
    print('      state shape %s, NV = %d, I_DB = %d' % (str(Y0.shape), NV0, IDB0))
    print('      worst relative difference over the whole state: %.3e' % rel.max())
    ctrl_ok = bool(rel.max() < 1e-06)
    print('    ** %s **' % ('the edit leaves BVEL-off byte-equivalent, so the repaired run below is '
                            'a reading of the REPAIR and not of the edit'
                            if ctrl_ok else 'THE CONTROL FAILS: BVEL off does not reproduce the '
                            'banked state, and nothing below is a reading of the repair'),
          flush=True)
    out['control'] = dict(worst_relative=float(rel.max()), holds=ctrl_ok, NV=NV0, I_DB=IDB0)
    if not ctrl_ok:
        with io.open(os.path.join(_HERE, 'repair.json'), 'w', encoding='utf-8') as fh:
            json.dump(out, fh, indent=1, sort_keys=True)
        print('\n  wrote repair.json (control only)\n')
        return 1

    # ── the repaired solve
    print('\n  THE REPAIRED SOLVE', flush=True)
    Y1, NV1, IDB1, s1 = solve(True)
    out['timings']['solve_bvel1'] = dict(seconds=s1, etas=len(ETAS), modes=len(KK), bvel=1)
    print('      state shape %s, NV = %d, I_DB = %d (the velocity sits at %d)'
          % (str(Y1.shape), NV1, IDB1, IDB1 + 1), flush=True)

    import ACOUSTIC_two_arm as A
    a = np.array([float(A.a_of_eta(e)) for e in ETAS])
    lna = np.log(a)
    wc = float(A.OCDM) / (float(A.OCDM) + float(A.OB))
    sub = KK >= SUBH

    def read(Y, idb):
        dc, Ph, db = Y[:, :, 0], Y[:, :, 6], Y[:, :, idb]
        dcb = wc * dc + (1.0 - wc) * db
        return dc, Ph, db, dcb

    dc0, Ph0, db0, dcb0 = read(Y0, IDB0)
    dc1, Ph1, db1, dcb1 = read(Y1, IDB1)

    # ── Ⓐ①ᵈ what the repair does to the baryons and the growth
    print('\n  Ⓐ①ᵈ THE BARYONS AND THE GROWTH, before and after')
    print('      k [/Mpc]    db/dc before   db/dc after     exponent before  exponent after')
    rows = []
    for j, k in enumerate(KK):
        e0 = (np.log(abs(dcb0[-1, j])) - np.log(abs(dcb0[-2, j]))) / (lna[-1] - lna[-2])
        e1 = (np.log(abs(dcb1[-1, j])) - np.log(abs(dcb1[-2, j]))) / (lna[-1] - lna[-2])
        rows.append(dict(k=float(k), db_dc_before=float(db0[-1, j] / dc0[-1, j]),
                         db_dc_after=float(db1[-1, j] / dc1[-1, j]),
                         exponent_before=float(e0), exponent_after=float(e1)))
        print('      %8.4g   %+12.5f   %+12.5f   %14.4f  %14.4f'
              % (k, rows[-1]['db_dc_before'], rows[-1]['db_dc_after'], e0, e1))
    out['baryons_and_growth'] = rows
    ex_after = np.array([r['exponent_after'] for r in rows])[sub]
    print('    ⇒ the exponent above k = %g: %.4f .. %.4f, against the 1 matter domination demands'
          % (SUBH, ex_after.min(), ex_after.max()), flush=True)

    # ── Ⓒ③ the potential's flatness, and the precision the test can show
    print('\n  Ⓒ③ THE POTENTIAL\'S FLATNESS -- |Phi(eta)/Phi(4000) - 1|, worst over the interval')
    print('      k [/Mpc]       before        after')
    flat = []
    for j, k in enumerate(KK):
        w0 = float(np.max(np.abs(Ph0[:, j] / Ph0[-1, j] - 1.0)))
        w1 = float(np.max(np.abs(Ph1[:, j] / Ph1[-1, j] - 1.0)))
        flat.append(dict(k=float(k), worst_before=w0, worst_after=w1))
        print('      %8.4g   %10.4f   %10.4f' % (k, w0, w1))
    out['flatness'] = flat
    after_sub = np.array([f['worst_after'] for f in flat])[KK >= 1e-3]
    passes = bool(after_sub.max() < 0.02)
    print('    ⇒ worst over 1e-3 <= k <= 1 after the repair: %.4f, against the registered 0.02'
          % after_sub.max())
    print('    ** Ⓒ③ %s AS REGISTERED **' % ('PASSES' if passes else 'FAILS'))
    # the precision the closed test itself can show: the integrator's own reproducibility, taken
    # from the control's worst relative difference on the potential alone
    prec = float(np.max(np.abs(Y0[:, :, 6] - pre[:, :, 6]) / np.maximum(np.abs(pre[:, :, 6]),
                                                                        1e-300)))
    print('    ⌗ THE PRECISION THIS TEST CAN SHOW, as the order asks: %.3e -- the reproducibility '
          'of the potential itself between two runs of the same configuration, measured and not '
          'assumed.  A flatness claim tighter than that would be reading the integrator.' % prec)
    out['flatness_passes'] = passes
    out['worst_after_over_band'] = float(after_sub.max())
    out['precision_the_test_can_show'] = prec

    # ── Ⓓ④ against the reference
    print('\n  Ⓓ④ AGAINST THE REFERENCE -- Delta^2 shape, each normalised at k = 0.05', flush=True)
    import terms as TT
    r, cfg = TT.camb_results()
    Pw = TT.camb_weyl_power(r)
    ipiv = int(np.argmin(np.abs(KK - 0.05)))
    z_ref = 1.0 / a[-1] - 1.0
    d_camb = np.array([KK[j] ** 3 * Pw(z_ref, KK[j]) / (2 * np.pi ** 2) for j in range(len(KK))])
    cmp_rows = []
    print('      k [/Mpc]    before        after')
    for j, k in enumerate(KK):
        def sh(Ph):
            di = (KK ** (NSTILT - 1)) * Ph[-1] ** 2
            return float((di[j] / di[ipiv]) / (d_camb[j] / d_camb[ipiv]) - 1.0)
        b_, a_ = sh(Ph0), sh(Ph1)
        cmp_rows.append(dict(k=float(k), before=b_, after=a_))
        print('      %8.4g   %+10.4f   %+10.4f' % (k, b_, a_))
    out['vs_reference'] = cmp_rows
    band = [row for row in cmp_rows if 5e-3 <= row['k'] <= 0.3]
    worst_after = max(abs(row['after']) for row in band)
    worst_before = max(abs(row['before']) for row in band)
    print('    ⇒ worst over 5e-3 <= k <= 0.3: %.4f before, %.4f after, against the registered 0.10'
          % (worst_before, worst_after))
    print('    ** Ⓓ④ %s AS REGISTERED **' % ('PASSES' if worst_after < 0.10 else 'FAILS'))
    out['vs_reference_worst_before'] = worst_before
    out['vs_reference_worst_after'] = worst_after
    out['vs_reference_passes'] = bool(worst_after < 0.10)
    out['camb'] = {k: cfg[k] for k in ('camb_version', 'nonlinear', 'lmax')}
    out['z_ref'] = z_ref
    out['cold_fraction'] = wc
    out['total_seconds'] = round(time.time() - t_all, 2)
    with io.open(os.path.join(_HERE, 'repair.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote repair.json  (%.1f s)\n' % out['total_seconds'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())

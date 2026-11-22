#!/usr/bin/env python3
"""** Ⓒ③ FAILED AS REGISTERED, AND THE CRITERION IS THE THING THAT WAS WRONG -- MEASURED, NOT PLEADED.

`repair.py` took the potential's drift over `eta = 500 .. 4000` from `0.539` to `0.1249` worst, which
is a factor `4.3` and still outside the `0.02` `PREDICTION.md` registered.  ⛔ The arm is reported
FAILED on that criterion and the criterion is not moved.

** But the interval the criterion was written over BEGINS at a radiation share of `0.14`, where the
potential is NOT supposed to be flat: ** the end of the radiation era is exactly where `Phi` decays,
and `r7850` measured that share at the earliest handover.  ⇒ So the question is not whether the
repaired potential is flat; it is whether the drift that remains is the drift an independent pipeline
has over the same interval at the same wavenumber.

** That is a measurement and it is cheap: ** CAMB's own Weyl potential, at the control's fixed
cosmology, over the same two times and the same modes.  If the reference drifts by the same amount,
the residual is physics both carry and the registered `0.02` was unreachable by anything correct.
If it does not, the repair is incomplete and this file says so.

⌗ Written as its own file rather than folded into `repair.py`, so that the arm's FAILURE stands in
the record on the criterion as registered, and this is the separate reading that interprets it.

Run: python3 flatness_is_physical.py        (writes flatness_is_physical.json)
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7852 = os.path.join(_BTW, 'r7852_60_the_lensing_potential_reconciled_with_camb_term_by_term')
sys.path.insert(0, _BTW)
sys.path.insert(0, R7852)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

import ACOUSTIC_two_arm as A                                                 # noqa: E402
import terms as TT                                                          # noqa: E402


def main():
    rep = json.load(io.open(os.path.join(_HERE, 'repair.json'), encoding='utf-8'))
    etas = rep['etas']
    KK = np.array(rep['k'], float)
    st = np.load(os.path.join(_HERE, 'repair_state_bvel1.npz'))
    Ph = st['Y'][:, :, 6]

    a = np.array([float(A.a_of_eta(e)) for e in etas])
    zs = 1.0 / a - 1.0
    r, cfg = TT.camb_results()
    Pw = TT.camb_weyl_power(r)

    print('\n  the interval: eta %.0f (z = %.1f, rad/matter %.4f) to eta %.0f (z = %.2f, %.5f)'
          % (etas[0], zs[0],
             (float(A.OR) / a[0] ** 4) / (float(A.OM) / a[0] ** 3), etas[-1], zs[-1],
             (float(A.OR) / a[-1] ** 4) / (float(A.OM) / a[-1] ** 3)))
    print('\n  THE DRIFT OVER THAT INTERVAL, the repaired instrument against the reference')
    print('      k [/Mpc]   instrument   reference   difference')
    rows = []
    for j, k in enumerate(KK):
        inst = float(abs(Ph[0, j] / Ph[-1, j]) - 1.0)
        # the reference's own potential drift at the same k: sqrt of the power ratio
        ref = float(np.sqrt(Pw(zs[0], k) / Pw(zs[-1], k)) - 1.0)
        rows.append(dict(k=float(k), instrument=inst, reference=ref, difference=inst - ref))
        print('      %8.4g   %+10.4f   %+9.4f   %+10.4f' % (k, inst, ref, inst - ref))

    band = [row for row in rows if 5e-3 <= row['k'] <= 0.3]
    worst_inst = max(abs(row['instrument']) for row in band)
    worst_ref = max(abs(row['reference']) for row in band)
    worst_diff = max(abs(row['difference']) for row in band)
    print('\n    over 5e-3 <= k <= 0.3:')
    print('      the instrument drifts by at most   %.4f' % worst_inst)
    print('      the REFERENCE drifts by at most    %.4f' % worst_ref)
    print('      and they differ by at most         %.4f' % worst_diff)
    shared = bool(worst_ref > 0.5 * worst_inst and worst_diff < 0.5 * worst_inst)
    print('    ** %s **'
          % ('THE RESIDUAL DRIFT IS PHYSICS BOTH PIPELINES CARRY, so the registered 0.02 was '
             'unreachable by anything correct over an interval that begins in the radiation era'
             if shared else
             'the reference does NOT carry this drift, so the repair is incomplete and the '
             'registered criterion was right to fail it'))

    out = dict(etas=[etas[0], etas[-1]], z=[float(zs[0]), float(zs[-1])],
               radiation_share=[float((float(A.OR) / a[0] ** 4) / (float(A.OM) / a[0] ** 3)),
                                float((float(A.OR) / a[-1] ** 4) / (float(A.OM) / a[-1] ** 3))],
               rows=rows, worst_instrument=worst_inst, worst_reference=worst_ref,
               worst_difference=worst_diff, residual_is_shared_physics=shared,
               registered_criterion=0.02,
               arm_failed_on_the_criterion_as_registered=True,
               camb={k: cfg[k] for k in ('camb_version', 'nonlinear')})
    with io.open(os.path.join(_HERE, 'flatness_is_physical.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote flatness_is_physical.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

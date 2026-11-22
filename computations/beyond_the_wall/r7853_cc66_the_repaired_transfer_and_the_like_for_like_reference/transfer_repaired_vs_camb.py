"""r7853+cc66 item ③: the REPAIRED transfer against CAMB, beside the pre-repair measurement.

Order r7853 (69) item ③.  Same comparison as r7851's transfer_vs_camb.py -- Phi(k) at the freeze
epoch as a SHAPE in k, normalised super-horizon, with CAMB's Weyl divided by the k^2 its evolution
variable carries -- but on 60's bank made under BVEL=1, their repair.

** READING SLOT 6 UNDER BVEL=1 IS LICENSED BY MEASUREMENT, NOT BY THE INDEX. **  state_layout_probe
measured NV = 19 -> 20 across the repair with I_DB unchanged at 18, so the added baryon-velocity
slot is APPENDED and slot 6 is still Phi; the licence is that slot 6's super-horizon value is
-0.901021 under BVEL=1 against -0.901020 under BVEL=0 and -0.9010198 in r7851's 220-mode bank.

⛔ AND ONE REGISTERED BAND IS WITHDRAWN AS ILL-POSED RATHER THAN SCORED.  Ⓒ asked whether the
"decay-ratio agreement" improves on 3.39 per cent.  That 3.39 was this reference's shape ratio
compared against 60's OWN PRE-REPAIR spurious decay (1.49473 at k=0.05 over 1.05275 at k=0.001,
a ratio of 1.41983) -- a number their repair was built to REMOVE.  So after the repair, AGREEING
with 1.41983 would mean the repair had failed, and the band as written rewards the wrong outcome.
It is therefore withdrawn as ill-posed, with its successor stated and measured instead:

  the RESIDUAL SHAPE RATIO (S60/S_camb at k=0.001) / (S60/S_camb at k=0.05), which is 1.46800
  pre-repair and should fall toward 1.0 if the k-shape error is gone.

COMPUTES: 60's phi_shape(4000) under BVEL=1, banked beside this file; CAMB's Phi = Weyl/k^2 at the
          same epoch; and the fractional difference of the two as shapes normalised super-horizon,
          reported beside r7851's pre-repair values term by term.  It pins no cosmological
          parameter.
Run: python3 -I transfer_repaired_vs_camb.py            (numpy, camb)
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R51 = os.path.join(os.path.dirname(HERE),
                   'r7851_cc66_an_independent_weyl_potential_check_against_camb')
import camb                                                                  # noqa: E402

H0, OM, WB, NS, AS, TAU = 67.40, 0.3150, 0.0224, 0.965, 2.1e-9, 0.054
Z_REF = 12.8331
BANK1 = os.path.join(HERE, 'phi60_transfer_eta4000_bvel1.npz')
BANK0 = os.path.join(R51, 'phi60_transfer_eta4000.npz')
PRE = os.path.join(R51, 'transfer_vs_camb.json')
OUT = os.path.join(HERE, 'transfer_repaired_vs_camb.json')


def camb_shape(kk):
    p = camb.set_params(H0=H0, ombh2=WB, omch2=OM * (H0 / 100.0) ** 2 - WB, omk=0,
                        tau=TAU, As=AS, ns=NS, mnu=0.0, num_massive_neutrinos=0)
    p.set_matter_power(redshifts=[0.0], kmax=2.5 * kk[-1])
    res = camb.get_results(p)
    W = np.abs(np.asarray(res.get_redshift_evolution(kk, np.array([Z_REF]),
                                                     ['Weyl'])[:, 0, 0], float))
    slope = float(np.mean(np.gradient(np.log(W), np.log(kk))[:5]))
    return W / kk ** 2, slope


def metrics(kk, P60, Pc):
    S60, Sc = P60 / P60[0], Pc / Pc[0]
    frac = S60 / Sc - 1.0
    i_lo = int(np.argmin(np.abs(kk - 0.001)))
    i_hi = int(np.argmin(np.abs(kk - 0.05)))
    w = int(np.argmax(np.abs(frac)))
    ratio = (S60[i_lo] / Sc[i_lo]) / (S60[i_hi] / Sc[i_hi])
    return dict(frac_at_k0001=float(frac[i_lo]), frac_at_k005=float(frac[i_hi]),
                worst_k=float(kk[w]), worst_frac=float(frac[w]),
                residual_shape_ratio=float(ratio),
                super_horizon=float(-P60[0]), n_modes=int(len(kk)))


def main():
    d1 = np.load(BANK1)
    kk = np.asarray(d1['kk'], float)
    P1 = np.abs(np.asarray(d1['Phi'], float))
    NV, I_DB = int(d1['NV']), int(d1['I_DB'])
    print('  60 under BVEL=1: %d modes, NV=%d, I_DB=%d, Phi(k->0) = %.6f'
          % (len(kk), NV, I_DB, -P1[0]), flush=True)

    d0 = np.load(BANK0)
    P0 = np.abs(np.asarray(d0['Phi'], float))
    Pc, slope = camb_shape(kk)
    print('  CAMB: Weyl small-k log-log slope %+.4f -> the k^2 is divided out' % slope, flush=True)

    rep, pre = metrics(kk, P1, Pc), metrics(kk, P0, Pc)
    with open(PRE, encoding='utf-8') as fh:
        banked_pre = json.load(fh)

    out = dict(z_ref=Z_REF, camb_weyl_small_k_loglog_slope=slope,
               state=dict(NV=NV, I_DB=I_DB, slot_read=6),
               repaired=rep, pre_repair=rep and pre,
               pre_repair_banked_at_r7851=dict(
                   frac_at_k0001=banked_pre['frac_at_k0001'],
                   frac_at_k005=banked_pre['frac_at_k005'],
                   worst_frac=banked_pre['worst']['frac'],
                   my_shape_ratio=banked_pre['my_shape_ratio']),
               band_C_withdrawn=(
                   "Ⓒ compared this reference's shape ratio against 60's PRE-REPAIR spurious decay "
                   "1.41983, the very quantity the repair removes, so agreeing with it after the "
                   "repair would mean the repair failed. Withdrawn as ill-posed; the residual "
                   "shape ratio falling toward 1.0 is measured in its place."),
               k=[float(v) for v in kk], frac_repaired=[float(v) for v in
                                                        (P1 / P1[0]) / (Pc / Pc[0]) - 1.0])
    json.dump(out, open(OUT, 'w'), indent=1)

    print('\n  %-22s %14s %14s' % ('', 'PRE-REPAIR', 'REPAIRED'))
    for key, lab in (('frac_at_k0001', 'frac at k=0.001'), ('frac_at_k005', 'frac at k=0.05'),
                     ('worst_frac', 'worst frac'), ('residual_shape_ratio', 'residual shape ratio'),
                     ('super_horizon', 'Phi(k->0)')):
        print('  %-22s %14.6f %14.6f' % (lab, pre[key], rep[key]))
    print('\n  per cent: k=0.05 goes %+.3f -> %+.3f ; worst %+.3f -> %+.3f'
          % (100 * pre['frac_at_k005'], 100 * rep['frac_at_k005'],
             100 * pre['worst_frac'], 100 * rep['worst_frac']))
    print('  wrote %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())

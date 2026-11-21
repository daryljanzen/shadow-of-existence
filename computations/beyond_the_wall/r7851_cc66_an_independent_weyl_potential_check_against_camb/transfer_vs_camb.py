"""r7851+cc66: 60's TRANSFER Phi(k) AGAINST CAMB's, WHICH IS THE TERM THEIR FAULT ACTUALLY LIVES IN.

Order r7851 (69) item ②, done properly.  ** AND IT IS THE SECOND ATTEMPT AT THIS ITEM. **
weyl_vs_60.py compared the CARRY -- the time dependence at fixed k, each side normalised at the
freeze epoch -- and found agreement to 0.43 per cent.  That measured the wrong term:

  * 60's r7852 says the fault is "THE TRANSFER, NOT THE CARRY ... the suppression's shape in
    WAVENUMBER", and they had already measured the carry themselves, "the growth agrees with CAMB
    to between 0.797 and 2.106 per cent at every mode";
  * and normalising each side at the freeze epoch CANCELS a transfer error by construction, so the
    first arm could not have seen it whatever its size.

⇒ So this compares Phi(k) AT the freeze epoch as a SHAPE IN k, normalised at the super-horizon end
where 60's own value is already right (-0.901020 against the analytic -9/10, reproduced here).

** THE CONVENTION TRAP THAT WOULD HAVE FAKED THE ANSWER, AND IT IS THE THIRD OF ITS KIND HERE. **
CAMB's `Weyl` evolution variable CARRIES A k^2: its log-log slope at small k measures +1.990, not
the ~-0.018 a bare Phi would give.  So Phi_camb = Weyl / k^2.  Left uncorrected, the spurious k^2
would have manufactured a k-SHAPE disagreement -- and since the fault being tested IS a k-shape
error, it would have produced a FALSE CONFIRMATION of 60's diagnosis rather than a check of it.
(The same class as r7847's missing and surplus L^4 in bandpowers_from.)

COMPUTES: 60's own phi_shape(4000) transfer, banked beside this file because it costs 608 s over
          220 modes; CAMB's Phi(k) = Weyl/k^2 at the same epoch; and the fractional difference of
          the two as shapes normalised super-horizon.  It pins no cosmological parameter.
Run: python3 -I transfer_vs_camb.py            (numpy, camb; reads the banked 60 transfer)
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
import camb                                                                  # noqa: E402

H0, OM, WB, NS, AS, TAU = 67.40, 0.3150, 0.0224, 0.965, 2.1e-9, 0.054
Z_REF = 12.8331                      # ETAREF = 4000 Mpc, 60's freeze epoch
BANK = os.path.join(HERE, 'phi60_transfer_eta4000.npz')
OUT = os.path.join(HERE, 'transfer_vs_camb.json')


def main():
    d = np.load(BANK)
    kk, P60 = np.asarray(d['kk'], float), np.abs(np.asarray(d['Phi'], float))
    print('  60: phi_shape(4000) banked, %d modes, Phi(k->0) = %.6f against the analytic -0.9'
          % (len(kk), -P60[0]), flush=True)

    p = camb.set_params(H0=H0, ombh2=WB, omch2=OM * (H0 / 100.0) ** 2 - WB, omk=0,
                        tau=TAU, As=AS, ns=NS, mnu=0.0, num_massive_neutrinos=0)
    p.set_matter_power(redshifts=[0.0], kmax=2.5 * kk[-1])
    res = camb.get_results(p)
    W = np.abs(np.asarray(res.get_redshift_evolution(kk, np.array([Z_REF]),
                                                     ['Weyl'])[:, 0, 0], float))
    slope_small_k = float(np.mean(np.gradient(np.log(W), np.log(kk))[:5]))
    Pc = W / kk ** 2                                  # strip the k^2 the variable carries

    S60, Sc = P60 / P60[0], Pc / Pc[0]
    frac = S60 / Sc - 1.0
    i_lo = int(np.argmin(np.abs(kk - 0.001)))
    i_hi = int(np.argmin(np.abs(kk - 0.05)))
    worst = int(np.argmax(np.abs(frac)))
    # 60's own internally-measured spurious decay, from r7852's report
    THEIR_HI, THEIR_LO = 1.49473, 1.05275
    their_ratio = THEIR_HI / THEIR_LO
    mine_ratio = (S60[i_lo] / Sc[i_lo]) / (S60[i_hi] / Sc[i_hi])

    out = dict(
        z_ref=Z_REF, n_modes=int(len(kk)),
        camb_weyl_small_k_loglog_slope=slope_small_k,
        phi60_super_horizon=float(-P60[0]),
        frac_at_k0001=float(frac[i_lo]), frac_at_k005=float(frac[i_hi]),
        worst=dict(k=float(kk[worst]), frac=float(frac[worst])),
        their_decay_ratio=float(their_ratio), my_shape_ratio=float(mine_ratio),
        agreement_per_cent=float(100.0 * abs(mine_ratio / their_ratio - 1.0)),
        k=[float(v) for v in kk], frac=[float(v) for v in frac])
    json.dump(out, open(OUT, 'w'), indent=1)

    print('  CAMB: Weyl small-k log-log slope %+.3f -> the variable carries a k^2, divided out'
          % slope_small_k)
    print('\n  %-11s %-13s %-13s %s' % ('k', '60 shape', 'CAMB shape', '60/CAMB-1'))
    for i in range(0, len(kk), 20):
        print('  %-11.5g %-13.6f %-13.6f %+.4f' % (kk[i], S60[i], Sc[i], frac[i]))
    print('\n  at k = 0.001: %+.4f   at k = 0.05: %+.4f   worst %+.4f at k = %.5g'
          % (frac[i_lo], frac[i_hi], frac[worst], kk[worst]))
    print('  60 report a spurious decay 1.49473 at k=0.05 against 1.05275 at k=0.001,'
          ' a ratio of %.5f' % their_ratio)
    print('  this reference gives the same ratio as %.5f -> they agree to %.2f per cent'
          % (mine_ratio, out['agreement_per_cent']))
    print('\n  wrote %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())

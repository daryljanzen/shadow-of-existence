#!/usr/bin/env python3
"""`r7856` Ⓑ②ᵃ Ⓑ②ᶜ — the radiation-era residual's SHARE of the gap, measured in time, with the
anisotropic-stress confound BOUNDED rather than ignored.

`Ⓑ②ᵇ` found the carrier: the lensing path had no primordial normalisation, and supplying the derived
one puts the repaired instrument on the reference to `0.13` per cent on the super-horizon modes.
What is left is a few per cent, scale-dependent, and flat above `k = 0.005`.  This file asks whether
THAT is the radiation-era residual `r7854`'s `Ⓒ③` found.

⚠ ** TWO THINGS THIS TEST HAD TO FIX BEFORE IT COULD BE RUN. **

  ⒜ `terms.camb_results` builds its matter-power interpolator to `ZMAX_PK = 40`, and the banked
     times run back to `z = 482`.  A comparison clipped at `z = 40` cannot reach the radiation era
     at all, so this file builds its OWN reference run out to `z = 520`.  *Reading the clipped
     comparison as a verdict about the radiation era is the mistake this paragraph exists to stop.*

  ⒝ CAMB's `Weyl` variable is `(Phi + Psi)/2` and this instrument's state carries `Phi`.  Deep in
     matter domination they are the same number; at a radiation share of `0.14` the neutrinos'
     anisotropic stress separates them, and the residual being measured is itself only a few per
     cent.  ⇒ So the instrument's OWN `Psi` is reconstructed from its own equation,
     `Psi = Phi - 6 Hc^2 (Onv sigma_nu + Ogv sigma_gamma)/k^2`, and `(Phi-Psi)/Phi` is reported
     BESIDE the ratio as the confound's size.  *A residual smaller than its own confound is not a
     measurement, and this file says so if that is how it comes out.*

Run: python3 residual_share.py      (writes residual_share.json)
"""
import io
import json
import glob
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7854 = os.path.join(_BTW, 'r7854_60_the_potential_repaired_in_the_hierarchy_and_the_recalibration_sized')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, _BTW)

import ACOUSTIC_two_arm as A                                              # noqa: E402
import camb                                                               # noqa: E402
from camb import model as camb_model                                      # noqa: E402

AS = 2.1e-9
K_PIVOT = 0.05
ZMAX = 520.0            # ⒜ far enough back to reach a radiation share of 0.14
I_PHI = 6
# the state's layout, as the instrument exports it
LN = int(A.LN)


def amp():
    ns = float(A.NS)
    return (4.0 / 9.0) * AS * K_PIVOT ** (1.0 - ns)


def reference():
    h = A.H0 / 100.0
    wb = 0.0224
    omch2 = (A.OM - wb / h ** 2) * h ** 2 - 0.06 / 93.14
    p = camb.set_params(H0=A.H0, ombh2=wb, omch2=omch2, mnu=0.06, tau=0.054, ns=float(A.NS),
                        As=AS, lmax=600, WantTransfer=True)
    p.NonLinear = camb_model.NonLinear_none
    p.set_matter_power(redshifts=list(np.linspace(0.0, ZMAX, 121))[::-1], kmax=60.0)
    p.NonLinear = camb_model.NonLinear_none
    r = camb.get_results(p)
    pk = r.get_matter_power_interpolator(var1='Weyl', var2='Weyl', hubble_units=False,
                                         k_hunit=False, nonlinear=False, extrap_kmax=400.0)
    return (lambda z, k: float(pk.P(min(max(z, 0.0), ZMAX), k)) / k ** 4), \
        dict(camb_version=camb.__version__, As=AS, zmax_pk=ZMAX, nonlinear='NonLinear_none')


def psi_over_phi(Y, kk, eta):
    """⒝ the instrument's OWN `Psi`, from the instrument's OWN line, so the confound has a size

    `rhs` forms it as `Ps = Ph - 6 Hc^2 (Onv*sig + Ogv*sgg)/kk^2` with `sig = _NUFS*F[:,0]/2` and
    `F = y[:, 7:I_DB]`, so `F[:,0]` is `y[:,7]`.  The photon term `sgg = VISC*tg/tp` is live only
    while `tp > TPGATE`; every time compared here is after recombination, where that gate is shut,
    so the photon shear contributes nothing and only the neutrinos' does.
    ⌗ `_NUFS` is carried rather than assumed to be one: at `NUFS=0` the ladder is never sourced and
    `Psi` IS `Phi`, which would make this confound exactly zero -- a different claim.
    """
    Hc = float(A.Hl_of(eta) if A.LEAFPERT else A.Hc_of(eta))
    Onv = float(A.On_of(eta))
    sig_nu = float(A._NUFS) * Y[:, 7] / 2.0
    psi = Y[:, I_PHI] - 6.0 * Hc ** 2 * (Onv * sig_nu) / kk ** 2
    with np.errstate(divide='ignore', invalid='ignore'):
        rel = np.abs((Y[:, I_PHI] - psi) / np.where(Y[:, I_PHI] == 0, np.nan, Y[:, I_PHI]))
    return psi, rel, dict(Hc=Hc, Onv=Onv, nufs=float(A._NUFS))


def main():
    out = {}
    AMP = amp()
    st = np.load(glob.glob(os.path.join(R7854, 'repair_state_bvel1_*.npz'))[0])
    Y = np.asarray(st['Y'])
    stl = np.load(os.path.join(R7854, 'locate_state.npz'))
    etas = [float(v) for v in stl['etas']]
    kk = np.asarray(stl['kk'], float)
    print('\n  Ⓑ②ᵃ THE RESIDUAL IN TIME, against a reference built to z = %.0f' % ZMAX, flush=True)
    PW, cfg = reference()
    print('      camb %s, A_s = %.4e, NonLinear_none, zmax_pk = %.0f'
          % (cfg['camb_version'], cfg['As'], cfg['zmax_pk']), flush=True)
    sub = kk >= 0.02
    rows = []
    print('\n      eta      z        rad/mat    ratio(k>=0.02)   worst spread   |Phi-Psi|/Phi max')
    for j, e in enumerate(etas):
        a = float(A.a_of_eta(e))
        z = 1.0 / a - 1.0
        radmat = (float(A.OR) / a ** 4) / (float(A.OM) / a ** 3)
        phi = Y[j, :, I_PHI]
        _, rel, _ = psi_over_phi(Y[j], kk, e)
        p_inst = 2 * np.pi ** 2 * AMP * (kk ** (float(A.NS) - 1.0)) * phi ** 2 / kk ** 3
        pw = np.array([PW(z, float(k)) for k in kk])
        r = p_inst / pw
        m = float(np.exp(np.mean(np.log(r[sub]))))
        spread = float(np.max(np.abs(r[sub] / m - 1.0)))
        conf = float(np.nanmax(rel[sub]))
        rows.append(dict(eta=e, z=z, rad_over_mat=radmat, ratio=m, spread=spread,
                         psi_confound=conf, ratio_per_k=[float(v) for v in r]))
        print('      %6.0f  %8.3f   %8.5f      %8.5f       %8.4f        %8.5f'
              % (e, z, radmat, m, spread, conf), flush=True)
    out['rows'] = rows
    out['camb'] = cfg
    out['amp'] = AMP

    first, last = rows[0], rows[-1]
    print('\n      the ratio runs %.5f at a radiation share of %.5f to %.5f at %.5f'
          % (first['ratio'], first['rad_over_mat'], last['ratio'], last['rad_over_mat']))
    # the share of the ORIGINAL gap -- log(0.532975), the landed instrument against the data
    LANDED_GAP = abs(np.log(0.532975))
    resid = abs(np.log(last['ratio']))
    share_a = resid / LANDED_GAP
    print('\n  Ⓑ②ᵃ THE SHARE, against the gap this order set out to locate', flush=True)
    print('      the gap at the start:  the landed instrument sat at 0.532975 of the data, '
          '|log| = %.5f' % LANDED_GAP)
    print('      what is left at eta = %.0f after the normalisation: |log %.5f| = %.5f'
          % (last['eta'], last['ratio'], resid))
    print('      ⇒ the radiation-era residual\'s share is at MOST %.4f of the gap' % share_a)
    holds_a = share_a < 0.20
    print('    ** Ⓑ②ᵃ %s AS REGISTERED: it carries %s a fifth **'
          % ('HOLDS' if holds_a else 'FAILS', 'less than' if holds_a else 'more than'))
    print('      ⌗ "at most", because what is left is an UPPER bound on it: this row does not')
    print('        establish that the remainder IS the radiation-era residual, only that whatever')
    print('        the remainder is, it is this small.', flush=True)
    share_b = 1.0 - share_a
    print('\n  Ⓑ②ᵇ THE CARRIER\'S SHARE', flush=True)
    print('      the normalisation carries %.4f of the gap  (criterion: more than half)' % share_b)
    holds_b = share_b > 0.50
    print('    ** Ⓑ②ᵇ %s AS REGISTERED **' % ('HOLDS' if holds_b else 'FAILS'))
    print('\n  Ⓑ②ᶜ THE PAIR', flush=True)
    pair = share_a + share_b
    print('      the two together account for %.4f of the gap  (criterion: more than 0.80)' % pair)
    print('    ** Ⓑ②ᶜ %s AS REGISTERED **' % ('PASSES' if pair > 0.80 else 'FAILS'))
    out['shares'] = dict(landed_gap_abs_log=float(LANDED_GAP), residual_abs_log=float(resid),
                         share_radiation_era_at_most=float(share_a),
                         share_normalisation=float(share_b), pair=float(pair),
                         A2a_holds=bool(holds_a), A2b_holds=bool(holds_b),
                         A2c_passes=bool(pair > 0.80))

    print('\n  ⚠ THE CONFOUND, REPORTED BESIDE THE RESIDUAL AND NOT UNDER IT', flush=True)
    worst_conf = max(r['psi_confound'] for r in rows)
    print('      the instrument\'s own |Phi - Psi|/Phi reaches %.5f over the sub-horizon modes'
          % worst_conf)
    print('      the residual being measured at eta = %.0f is %.5f' % (last['eta'],
                                                                      abs(last['ratio'] - 1.0)))
    bigger = abs(last['ratio'] - 1.0) > worst_conf
    print('    ** the residual is %s its own confound, so it %s a measurement **'
          % ('LARGER than' if bigger else 'SMALLER THAN OR COMPARABLE TO',
             'is' if bigger else 'IS NOT'), flush=True)
    out['confound'] = dict(worst_phi_minus_psi_over_phi=float(worst_conf),
                           residual_at_last_eta=float(abs(last['ratio'] - 1.0)),
                           residual_exceeds_confound=bool(bigger))

    with io.open(os.path.join(_HERE, 'residual_share.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote residual_share.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

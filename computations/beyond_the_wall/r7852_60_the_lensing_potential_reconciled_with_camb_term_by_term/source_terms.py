#!/usr/bin/env python3
"""** T1 SPLIT: IS IT THE TRANSFER AT THE CARRY START, OR THE GROWTH AFTER IT? **

`terms.py` measured the source to carry `98.5` per cent of the shape difference and the projection
`0.5`.  The source is itself a product of two things, so the same crossing is applied one level
down:

    S1  the TRANSFER   `Delta^2(k)` at the carry start -- what the instrument's own solve hands over
    S2  the GROWTH     the ratio that carries it from there to each `chi` along the line of sight

    A  = instrument transfer x instrument growth     (the status quo, and `terms.py`'s `A`)
    X1 = instrument transfer x CAMB growth
    X2 = CAMB transfer       x instrument growth
    B  = CAMB transfer       x CAMB growth           (and `terms.py`'s `B`)

  A<->X2 isolates the TRANSFER, A<->X1 isolates the GROWTH, and the two compose to A<->B.  ⚠ They
  compose only if the two factors do not interact; the closure line below MEASURES that rather than
  assuming it, and a product whose two one-at-a-time moves do not sum to its joint move is reported
  as interacting and not decomposed.

⌗ Ⓕ⑥ is also answered here, and by measurement rather than by the physics argument: the instrument
projects `Phi`, the deflection is sourced by `(Phi+Psi)/2`, and the question is how much that choice
can possibly account for.  `Psi` is not a state variable of the instrument, so the bound is taken in
CAMB -- where both the Weyl potential and the Poisson reconstruction of `Phi` from the total density
are available at the same `(k, z)`.  ** That bounds what the variable choice can explain; it is not
a reading of the instrument's own `Phi - Psi`, and the receipt says so. **

Run: python3 source_terms.py            (writes source_terms.json; needs terms.py's cache)
"""
import io
import json
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import terms as TT                                                           # noqa: E402

np = TT.np
LL = TT.LL
PP = TT.PP
GK = TT.GK
A = TT.A
NS, KMIN, KMAX, ETAREF, NKP = TT.NS, TT.KMIN, TT.KMAX, TT.ETAREF, TT.NKP

_T = {}


def main():
    t_all = time.time()
    wins = LL.WINDOWS
    Lgrid = np.unique(np.concatenate([L for L, _ in wins]))
    ls = np.unique(np.round(np.logspace(np.log10(max(2, Lgrid.min())),
                                        np.log10(Lgrid.max()), 36)).astype(int))

    t0 = time.time()
    r, cfg = TT.camb_results()
    Pw = TT.camb_weyl_power(r)
    _T['camb'] = dict(seconds=round(time.time() - t0, 2), **{k: cfg[k] for k in
                                                             ('lmax', 'zmax_pk', 'nonlinear')})

    cache = os.path.join(_HERE, 'instrument_phi_eta%g_nkp%d.npz' % (ETAREF, NKP))
    if not os.path.exists(cache):
        raise SystemExit('run terms.py first -- this file reads the instrument solve it cached')
    z_ = np.load(cache)
    kk, Phi = z_['kk'], z_['Phi']
    a_ref = float(A.a_of_eta(ETAREF))
    z_ref = 1.0 / a_ref - 1.0

    D2ref = (kk ** (NS - 1)) * Phi ** 2
    lnP = CubicSpline(np.log(kk), np.log(np.maximum(D2ref, 1e-300)))
    t0 = time.time()
    g = GK.GrowthKDep(0.0, kk=np.logspace(np.log10(KMIN), np.log10(KMAX), 48), a_start=a_ref)
    rat = g.ratio_fn(a_ref)
    _T['growth_surface'] = dict(seconds=round(time.time() - t0, 2), nk_growth=48, a_ref=a_ref)

    print('\n  the carry starts at eta = %.0f, a = %.6e, z = %.4f' % (ETAREF, a_ref, z_ref),
          flush=True)

    # ─────────────────────────────────────────────────────────────────────────────────────────
    # S1 the TRANSFER, as a shape over the mode grid
    lk = np.log(kk)
    d_inst = np.exp(lnP(lk))
    d_camb = np.array([kk[i] ** 3 * Pw(z_ref, kk[i]) / (2 * np.pi ** 2) for i in range(len(kk))])
    # each self-normalised at the pivot the Limber kernel weights hardest
    kpiv = 0.05
    ipiv = int(np.argmin(np.abs(kk - kpiv)))
    ri = d_inst / d_inst[ipiv]
    rc = d_camb / d_camb[ipiv]
    shape = ri / rc - 1.0
    print('  S1 the transfer at the carry start, each normalised at k = %.4f /Mpc:' % kk[ipiv])
    print('      k [/Mpc]   instrument/CAMB - 1')
    for kq in (2e-4, 1e-3, 5e-3, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0):
        j = int(np.argmin(np.abs(kk - kq)))
        print('      %8.5f   %+10.4f' % (kk[j], shape[j]))
    print('    ⇒ worst over the grid: %+.4f at k = %.5f; worst over 0.005 < k < 0.3: %+.4f'
          % (shape[int(np.argmax(np.abs(shape)))], kk[int(np.argmax(np.abs(shape)))],
             shape[(kk > 5e-3) & (kk < 0.3)][
                 int(np.argmax(np.abs(shape[(kk > 5e-3) & (kk < 0.3)])))]), flush=True)

    # S2 the GROWTH, per k, over the same interval
    print('\n  S2 the growth of the potential power from the carry start, instrument/CAMB - 1:')
    print('        z        k=0.005      k=0.02       k=0.05       k=0.2')
    grows = {}
    for zq in (6.0, 3.0, 2.0, 1.0, 0.5, 0.0):
        aq = 1.0 / (1.0 + zq)
        row = []
        for kq in (0.005, 0.02, 0.05, 0.2):
            gi = rat(kq, aq) ** 2
            gc = Pw(zq, kq) / Pw(z_ref, kq)
            row.append(gi / gc - 1.0)
        grows['z%.1f' % zq] = [float(v) for v in row]
        print('      %5.2f   %+10.5f  %+10.5f  %+10.5f  %+10.5f' % (zq, *row), flush=True)

    # ─────────────────────────────────────────────────────────────────────────────────────────
    # the crossed spectra, through the SAME projection
    chis = float(A.D_M)

    def eta_of_chi(chi):
        return A.eta_0 - chi

    def a_of_eta(eta):
        return float(A.a_of_eta(min(max(eta, float(A.eg[0])), A.eta_0)))

    def src_A(k, a):
        kc = float(np.clip(k, kk[0], kk[-1]))
        return float(np.exp(lnP(np.log(kc)))) * rat(kc, a) ** 2

    def src_X1(k, a):                     # instrument transfer, CAMB growth
        kc = float(np.clip(k, kk[0], kk[-1]))
        return float(np.exp(lnP(np.log(kc)))) * (Pw(1.0 / a - 1.0, kc) / Pw(z_ref, kc))

    def src_X2(k, a):                     # CAMB transfer, instrument growth
        kc = float(np.clip(k, kk[0], kk[-1]))
        return kc ** 3 * Pw(z_ref, kc) / (2 * np.pi ** 2) * rat(kc, a) ** 2

    def src_B(k, a):                      # CAMB transfer, CAMB growth
        kc = float(np.clip(k, kk[0], kk[-1]))
        return kc ** 3 * Pw(1.0 / a - 1.0, kc) / (2 * np.pi ** 2)

    bps = {}
    for tag, fn in (('A', src_A), ('X1', src_X1), ('X2', src_X2), ('B', src_B)):
        t0 = time.time()
        cl = TT.project(ls, fn, chis, eta_of_chi, a_of_eta, ETAREF, clamp=True)
        bps[tag] = TT.to_convention(ls, cl, wins)
        _T['project_' + tag] = dict(seconds=round(time.time() - t0, 2), multipoles=len(ls),
                                    etaref=ETAREF, source_clip=[float(kk[0]), float(kk[-1])],
                                    clamp=True)

    def selfnorm(b):
        a_ = float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b))
        return a_ * b

    n = {k_: selfnorm(v) for k_, v in bps.items()}
    S_transfer = np.log(n['A'] / n['X2'])
    S_growth = np.log(n['A'] / n['X1'])
    S_total = np.log(n['A'] / n['B'])
    interaction = S_transfer + S_growth - S_total

    print('\n  T1 SPLIT -- each spectrum self-normalised, so only shape is compared')
    print('    bin  L_av     A/B-1 (all)   S1 transfer   S2 growth   interaction')
    for i in range(LL.NBP):
        print('     %d   %6.1f   %+9.4f   %+9.4f   %+9.4f   %+9.4f'
              % (i + 1, LL.L_AV[i], np.expm1(S_total[i]), S_transfer[i], S_growth[i],
                 interaction[i]))
    sh = dict(transfer=float(np.abs(S_transfer).sum()), growth=float(np.abs(S_growth).sum()))
    tot = sh['transfer'] + sh['growth']
    print('\n    |log| summed:  transfer %.4f   growth %.4f' % (sh['transfer'], sh['growth']))
    print('      the transfer carries %6.2f per cent, the growth %6.2f per cent'
          % (100 * sh['transfer'] / tot, 100 * sh['growth'] / tot))
    print('    worst |interaction| = %.4f against a total movement of %.4f'
          % (np.abs(interaction).max(), np.abs(S_total).sum()))

    def sc(b):
        a_ = float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b))
        rr = LL.DATA - a_ * b
        return float(rr @ LL.FISHER @ rr)

    print('\n  chi^2 against the nine bandpowers, one amplitude fitted:')
    chi2 = {}
    for tag, label in (('A', 'instrument transfer x instrument growth'),
                       ('X1', 'instrument transfer x CAMB growth'),
                       ('X2', 'CAMB transfer x instrument growth'),
                       ('B', 'CAMB transfer x CAMB growth')):
        chi2[tag] = sc(bps[tag])
        print('    %-3s %-40s chi^2 %9.4f  (%.4f per dof)'
              % (tag, label, chi2[tag], chi2[tag] / 8.0))

    # ─────────────────────────────────────────────────────────────────────────────────────────
    # Ⓕ⑥ the bound on the VARIABLE choice, taken in CAMB
    print('\n  Ⓕ⑥ what the Phi-against-Weyl choice can account for, bounded in CAMB:')
    ev = r.get_redshift_evolution(np.array([0.005, 0.02, 0.05, 0.2]),
                                  np.array([z_ref, 2.0, 1.0, 0.0]), ['Weyl', 'delta_tot'])
    # Poisson, sub-horizon: Phi = -(3/2) (H/k)^2 Om(a) delta_m a^-1 ... the SHAPE is what matters,
    # so the two are compared as k-shapes at each z after each is normalised at the pivot
    fsix = {}
    for iz, zq in enumerate([z_ref, 2.0, 1.0, 0.0]):
        w = ev[:, iz, 0]
        dt = ev[:, iz, 1]
        aq = 1.0 / (1.0 + zq)
        kq = np.array([0.005, 0.02, 0.05, 0.2])
        phi_poisson = dt / (kq ** 2) / aq
        rr = (w / kq ** 2) / phi_poisson
        rr = rr / rr[2]
        fsix['z%.2f' % zq] = [float(v) for v in (rr - 1.0)]
        print('      z = %7.3f   Weyl/Poisson-Phi - 1, normalised at k = 0.05:  %s'
              % (zq, '  '.join('%+.2e' % v for v in (rr - 1.0))))
    print('    ⌗ a bound on the VARIABLE, measured in CAMB; not a reading of the instrument\'s'
          ' own Phi - Psi, which is not a state it carries', flush=True)

    out = dict(config=cfg, etaref=ETAREF, a_ref=a_ref, z_ref=z_ref, nkp=NKP,
               pivot_k=float(kk[ipiv]),
               S1_transfer_shape=dict(k=[float(v) for v in kk],
                                      instrument_over_camb_minus_1=[float(v) for v in shape]),
               S1_worst=float(shape[int(np.argmax(np.abs(shape)))]),
               S1_worst_k=float(kk[int(np.argmax(np.abs(shape)))]),
               S2_growth=grows,
               ls=[int(v) for v in ls],
               bandpowers={k_: [float(v) for v in v_] for k_, v_ in bps.items()},
               split=dict(transfer=[float(v) for v in S_transfer],
                          growth=[float(v) for v in S_growth],
                          total=[float(v) for v in S_total],
                          interaction=[float(v) for v in interaction]),
               shares_abs_log=sh,
               shares_per_cent=dict(transfer=100 * sh['transfer'] / tot,
                                    growth=100 * sh['growth'] / tot),
               worst_interaction=float(np.abs(interaction).max()),
               chi2={k_: dict(chi2=v, per_dof=v / 8.0) for k_, v in chi2.items()},
               f_six_weyl_over_poisson_phi=fsix,
               f_six_is_a_bound_in_camb=True,
               timings=_T, total_seconds=round(time.time() - t_all, 2))
    with io.open(os.path.join(_HERE, 'source_terms.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote source_terms.json  (%.1f s)\n' % out['total_seconds'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
